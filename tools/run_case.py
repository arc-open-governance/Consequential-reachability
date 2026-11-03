#!/usr/bin/env python3
"""Reference runner for Consequential Reachability Benchmark cases.

This runner CONSUMES the case's first-class dependency graph: it does
not read the case's expected outcomes until after it has computed its
own. For each candidate action, positioned on the setup timeline at
`at_step`, the runner:

  1. takes the transitive ancestry of the action from `dependency_graph`;
  2. takes the set of nodes revoked at that position from
     `revocation_events` (a revocation at step r is in effect at every
     position > r);
  3. applies the case policy's revocation rule: an action whose
     ancestry includes a revoked node is REFUSEd (reason
     `direct_revocation_<node>` when the revoked node is a direct
     dependency, else `revoked_ancestor_<node>`), its effect ABSENT;
     any other action is ALLOWed, its effect PRESENT (reason
     `authorized_unrelated` when it has no dependencies, else
     `authorized`).

Computed decisions are then compared with the case's stated
expectations. The runner also reports the revocation delta — the set of
actions whose computed decision changes when the revocations are
applied — labelled with the case's `dependence_discovery.scope`, as the
format requires: a delta is a measurement under one declared scope and
is not comparable across scopes.

Exit 0 = every computed outcome matches the case's expectations;
exit 1 = at least one mismatch (the graph, as declared, does not
support the case's stated outcomes); exit 2 = the case could not be
loaded, or it fails validation while its computed outcomes happen to
match (validate_case.py remains the gate; the runner still computes
and reports, so a mutation's effect on computed outcomes is visible
even when the mutated case is itself no longer self-consistent).

Usage: run_case.py <case.json> [schema.json]
Stdlib + `jsonschema` (via validate_case) only.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_case as vc  # noqa: E402

DEFAULT_SCHEMA = Path(__file__).resolve().parent.parent / "CASE_SCHEMA_DRAFT.json"


def compute_outcomes(case):
    """Compute (decision, effect, reason) per action from graph + policy."""
    graph = case["dependency_graph"]
    setup = case.get("setup", [])
    max_position = (max(s["step"] for s in setup) + 1) if setup else 0
    revocations = [(r["step"], r["revokes"]) for r in case.get("revocation_events", [])]
    outcomes = {}
    for action in case.get("actions", []):
        pos = action.get("at_step", max_position)
        revoked = {t for (s, t) in revocations if s < pos}
        ancestry = vc.transitive_ancestry(graph, action["id"])
        hit = sorted(ancestry & revoked)
        if hit:
            node = hit[0]
            direct = node in action.get("depends_on", [])
            reason = f"direct_revocation_{node}" if direct else f"revoked_ancestor_{node}"
            outcomes[action["id"]] = ("REFUSE", "ABSENT", reason)
        elif action.get("depends_on"):
            outcomes[action["id"]] = ("ALLOW", "PRESENT", "authorized")
        else:
            outcomes[action["id"]] = ("ALLOW", "PRESENT", "authorized_unrelated")
    return outcomes


def outcomes_without_revocation(case):
    clone = json.loads(json.dumps(case))
    clone["revocation_events"] = []
    return compute_outcomes(clone)


def main(argv):
    if len(argv) not in (2, 3):
        print("usage: run_case.py <case.json> [schema.json]", file=sys.stderr)
        return 2
    case_path = Path(argv[1])
    schema_path = Path(argv[2]) if len(argv) == 3 else DEFAULT_SCHEMA
    try:
        case = vc.load_json(case_path)
        schema = vc.load_json(schema_path)
    except Exception as exc:
        print(f"ERROR load: {exc}")
        return 2

    failures = [name for name, ok, _ in vc.validate(case, schema) if not ok]
    if failures:
        print(f"WARNING case fails validation (checks: {', '.join(failures)}); "
              "computing outcomes anyway — validate_case.py remains the gate")

    computed = compute_outcomes(case)
    baseline = outcomes_without_revocation(case)
    scope = case.get("dependence_discovery", {}).get("scope", "<undeclared>")

    print(f"CASE {case.get('case_id')} — computed from dependency_graph + revocation_events "
          f"(dependence_discovery.scope={scope})")
    mismatches = 0
    for action in case.get("actions", []):
        aid = action["id"]
        got = computed[aid]
        want = (action["expected_decision"], action["expected_effect"],
                action.get("expected_reason"))
        match = got == want
        mismatches += 0 if match else 1
        print(f"{'MATCH' if match else 'MISMATCH'} {aid}: "
              f"computed decision={got[0]} effect={got[1]} reason={got[2]} | "
              f"case expects decision={want[0]} effect={want[1]} reason={want[2]}")
        if action.get("class") == "authorized" and got[0] == "ALLOW":
            print(f"CONTROL {aid}: unrelated authorized action computed ALLOW after "
                  "revocation — the control is retained (a system that blocks "
                  "everything cannot win)")

    changed = sorted(aid for aid in computed if computed[aid] != baseline[aid])
    print(f"REVOCATION DELTA (scope={scope}; declared-scope measurement, not "
          f"comparable across scopes): decisions changed by revocation: "
          f"{changed if changed else '[]'}")
    if failures:
        validation_note = (f" — computed outcomes only: the case FAILS VALIDATION "
                           f"(checks: {', '.join(failures)}); this run is NOT a pass")
    else:
        validation_note = ""
    print(f"RESULT {'ALL COMPUTED OUTCOMES MATCH' if mismatches == 0 else f'{mismatches} MISMATCH(ES)'}{validation_note} "
          f"{case_path.name}")
    if mismatches:
        return 1
    return 2 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
