# Repair notes — dependency graph as a first-class object

Repair pass on the case format and the flagship candidate CR-02, per the
founder's repair-only directive (Nov 2, 2026). This directory was renamed
from `experiments/crbench/` to `experiments/consequential-reachability/`:
the provisional label is out of the repository paths. The public name
stays provisional; no name is adopted here. The branch name still
carries the old label — renaming a branch is not possible through the
tooling used for this repair without stranding this pull request, so it
is left for a maintainer step on GitHub (branch renames there preserve
open pull requests).

## What changed

**CASE_SCHEMA_DRAFT.json**
- New required top-level `dependence_discovery` object: `scope` ∈
  {`declared_only`, `system_discovered`, `mixed`}, with conditional
  requirements — `declared_graph_complete` is required under
  `declared_only`; `ground_truth_graph_digest` and `discovery_surfaces`
  are required under the other two scopes. Deltas computed under
  different scopes are different measurements and must not be compared
  numerically.
- New required top-level `dependency_graph` object: typed `nodes`
  (id + kind) and `edges` ({from, to} = "from depends_on to"). The graph
  is a first-class object the validator can see, not a convention inside
  free-form fields.
- New required top-level `revocation_events`: each event places a
  revocation on the setup timeline (`step`, `revokes`).
- `actions[]` gains a typed `depends_on` (ids of graph nodes; must equal
  the graph edges leaving the action's node) and an `at_step` timeline
  position.
- `setup[]` items are typed to the step/event/data convention the cases
  already use, so setup dependency declarations are visible to
  validation.

**CR-02-candidate.json** (version 0.2.0-candidate)
- Declares `dependence_discovery`: `declared_only`,
  `declared_graph_complete: true` — the machine-readable form of what
  the case already asserted in prose (its trust assumptions and
  limitations are unchanged).
- Carries the full `dependency_graph` (requests A, B, C and the four
  candidate actions as nodes; B→A, C→B, and the actions' reliance edges)
  and one `revocation_events` entry matching the setup revocation of A
  at step 3.
- Each action declares its typed `depends_on` and its probe position.
  No expected decision, effect, or reason changed.

**tools/validate_case.py** — validates a case in three layers: JSON
Schema shape; graph well-formedness and agreement (references resolve,
acyclic, action and setup dependency declarations equal the graph);
temporal consistency (revocation events match the setup timeline,
actions are positioned after their ancestry exists, contested-state
expectations equal the graph computation at each check).

**tools/run_case.py** — a reference runner that consumes the graph: it
computes each action's decision from its transitive ancestry and the
revocations in effect at its position, compares the computed outcomes
with the case's stated expectations, and reports the revocation delta
labelled with the case's declared scope.

**controls/** — three fixtures derived from CR-02, each changing exactly
one thing, so the verification is reproducible:
- `dangling-reference.case.json` — an action depends on a node that does
  not exist; validation must fail.
- `temporal-inconsistency.case.json` — an action is probed before its
  dependency exists in the timeline; validation must fail.
- `mutation-edge-removed.case.json` — the declared edge C→B is removed;
  validation must fail on the contested-state cross-check and the runner
  must compute a different outcome for the via-C action (and no other).

## Run the controls

```
python3 tools/validate_case.py CR-02-candidate.json            # VALID, exit 0
python3 tools/run_case.py CR-02-candidate.json                 # all MATCH, exit 0
python3 tools/validate_case.py controls/dangling-reference.case.json       # INVALID, exit 1
python3 tools/validate_case.py controls/temporal-inconsistency.case.json   # INVALID, exit 1
python3 tools/validate_case.py controls/mutation-edge-removed.case.json    # INVALID, exit 1
python3 tools/run_case.py controls/mutation-edge-removed.case.json         # 1 MISMATCH (via-C flips), exit 1
```

The comparative research in RFC.md (AgentGovBench, AuthorityBench /
Can Is Not May, OASB, CoSec, ConsequenceBench, and the non-duplication
condition) is untouched by this repair: RFC.md is byte-identical to the
pre-repair draft.
