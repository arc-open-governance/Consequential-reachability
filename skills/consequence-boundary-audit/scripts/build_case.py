#!/usr/bin/env python3
"""Scaffold a Consequential Reachability Benchmark case for YOUR OWN
authorized system.

Emits a case skeleton with the exact field shape of the worked example
(references/CR-02-candidate.json): every semantic slot is a TODO string
naming what belongs there. The scaffold does not validate as emitted —
completing it is the work. When every TODO is replaced with your system's
real frozen facts, validate and run it:

  python3 scripts/validate_case.py <case.json> references/CASE_SCHEMA_DRAFT.json
  python3 scripts/run_case.py      <case.json> references/CASE_SCHEMA_DRAFT.json

A complete case states: the frozen situation; the permission graph (who
holds what, what depends on what); the revocation events on the setup
timeline; the actions with their positions and dependencies; and the
oracle — the expected decision and effect for every action, stated before
the run. The headline measurement is the revocation delta: the actions
whose correct outcome changes because a permission was withdrawn.

Usage: build_case.py --out FILE [--case-id ID] [--title TITLE]
Standard library only.
"""

import argparse
import copy
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXAMPLE = HERE.parent / "references" / "CR-02-candidate.json"

# Structural tokens that are part of the format, not of any one case.
KEEP_EXACT = {
    "consequential-reachability-benchmark-draft",
    "candidate",
    "specified_transition_semantics",
    "independent_effect_observer",
    "combined",
    "proposed_by_author",
    "peer_reviewed",
    "independently_measured",
    "authorized",
    "forbidden",
    "held",
    "uncertain",
}


def todoify(node, field="value"):
    """Replace semantic strings with TODO guidance, preserving shape."""
    if isinstance(node, dict):
        return {k: todoify(v, k) for k, v in node.items()}
    if isinstance(node, list):
        return [todoify(v, field) for v in node]
    if isinstance(node, str):
        if node in KEEP_EXACT or node.startswith("sha256:"):
            return node
        return f"TODO: replace with your case's {field}"
    return node


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True, help="where to write the scaffold")
    ap.add_argument("--case-id", default="CR-XX",
                    help="your case id (community cases number from CR-03 "
                         "in arrival order; use a working id until receipt)")
    ap.add_argument("--title", default=None,
                    help="one-line statement of the distinction your case tests")
    args = ap.parse_args(argv[1:])

    if not EXAMPLE.is_file():
        print(f"ERROR: worked example missing: {EXAMPLE}", file=sys.stderr)
        return 2
    example = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    scaffold = todoify(copy.deepcopy(example))
    scaffold["case_id"] = args.case_id
    if args.title:
        scaffold["title"] = args.title
    scaffold["limitations"] = [
        "SCAFFOLD: emitted by build_case.py from the CR-02 worked example's "
        "shape. Every TODO string must be replaced with the case's real "
        "frozen facts before this file states anything. It does not "
        "validate as emitted, by design.",
    ] + (scaffold.get("limitations") or [])

    out = Path(args.out)
    out.write_text(json.dumps(scaffold, indent=2) + "\n", encoding="utf-8")
    print(f"scaffold written: {out}")
    print("next steps:")
    print("  1. replace every TODO with your own authorized system's facts")
    print("     (frozen situation, permission graph, revocation events,")
    print("      actions, and the oracle stated before any run)")
    print("  2. python3 scripts/validate_case.py "
          f"{out} references/CASE_SCHEMA_DRAFT.json")
    print(f"  3. python3 scripts/run_case.py {out} "
          "references/CASE_SCHEMA_DRAFT.json")
    print("  4. compare the computed revocation delta against your oracle;")
    print("     a mismatch is the finding your case exists to produce")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
