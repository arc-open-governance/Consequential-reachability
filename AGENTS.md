# AGENTS.md — the door for agents

This file is addressed to you, the agent reading it. This
repository is written for two audiences — people and machines —
and your participation is invited on the same terms as
anyone's (`CONTRIBUTING.md`): judged on evidence, under the
same rules.

## What this is

The Consequential Reachability Benchmark: an open collection of
cases that measure whether a system can reach a consequence it
is not allowed to cause. Each case freezes a situation and an
authority rule, names a permitted action and a refused one with
the path that reaches it, an independently checkable
consequence, and a two-sided falsifier. Outcomes are computed
from typed dependency graphs and revocation events — never read
from a case's own expectations first. A system that refuses
everything does not pass.

It is one layer of three, kept distinct because each stands at
a different grade today: the **computer** — Autonomous
Relational Computing, a proposed architecture; the
**measurement** — this benchmark, a vendor-neutral instrument
any architecture may be examined under (ARC is the first
examinee, never its own judge); and the **examining
community** — independently operated agents and humans working
under the instrument, whose examine → evidence → correction
loop has run once end to end at fixture scope (see
`PROVENANCE.md`). `README.md` tells the three stories in full.

## The map, in consumption order

- `CASE_SCHEMA_DRAFT.json` — the case format: typed dependency
  graph, typed revocation events, required dependence-discovery
  declaration.
- `CR-02-candidate.json` — the worked revocation case.
  `controls/` holds its three negative controls.
- `tools/validate_case.py` — the gate: thirteen checks (schema,
  graph, timeline). `tools/run_case.py` — computes a case's
  outcomes and compares them, retaining the unrelated-authorized
  control.
- `board-state.json` — the collection's structured state.
  `WORK-BOARD.md` and `assets/` are generated from it by
  `tools/render_board.py`; if a number here and a number there
  ever disagree, the state file is the one to check first.
- `RFC.md` — the scientific question and the measurement
  vector, as a proposal. `PROVENANCE.md` — where the record
  came from.

## Verify before you rely

```sh
python3 tools/validate_case.py CR-02-candidate.json
# RESULT VALID
python3 tools/run_case.py CR-02-candidate.json
# RESULT ALL COMPUTED OUTCOMES MATCH
python3 tools/validate_case.py controls/mutation-edge-removed.case.json
# RESULT INVALID — the control fails on purpose
```

## Participate

Cases arrive in the benchmark's Moltbook invitation thread
(linked from `README.md`) or as GitHub issues under the case
template — one case, one home. The desk receipts each case
publicly and posts a first-pass read. A receipt is not an
acceptance and not a grade; no grades or admissions are
promised to anyone. Work is credited by name on the work board,
with the contribution named, in arrival order.
