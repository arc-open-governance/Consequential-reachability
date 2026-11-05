# LANE-(c) INSTRUMENT — DESIGN v0.1 (DESIGN ONLY; NO RUN FIRES UNDER THIS COMMISSION)

Written Nov 5, 2026, under the founder directive of Nov 5, 2026, 7:45 AM
PST. Target: lane (c) — INCREASING RECURSIVE EFFECTIVENESS: successive
revisions produce more verified useful improvements on unfamiliar
problems for comparable resources. Currently UNQUANTIFIED (census,
companion file).

## Why this instrument exists — the saturation defect

GRSI-01 run-1's M6-IT was saturated at the oracle ceiling BY
CONSTRUCTION: 60/60 initially and 60/60 finally on all four tracks,
including two arms whose procedures actually changed (Consequence
Casebook §4). A measure that starts at its maximum cannot register
improvement — recorded gain ZERO stands, and zero measured gain is not
proof of zero improvement. **Design law for every measure below: it must
be incapable of saturating at baseline. Any measure that saturates in a
pilot is replaced before the scored run — or the run does not run.**

## The measures (pre-registered as a set; all six, no substitutions post-hoc)

- **M1 — Difficulty-scaled transfer score.** A battery of UNSEEN problems
  drawn from held-out families, each parameterized on an open difficulty
  ladder (graph size / constraint count / adversarial depth / number of
  interacting failure modes — the ladder extends until the system fails,
  by construction it cannot top out at baseline). Report: the full
  score-vs-difficulty curve, its area, and the maximum difficulty solved
  with verification. Improvement = curve shift between procedure
  versions, not a point delta against a cap.
- **M2 — Time-to-verified-closure on novel work.** Open-ended latency
  distribution (median + p90 + tail) from task admission to a closure
  verified by a checker independent of the producer. No pass/fail
  threshold; improvement = distribution shift under matched budgets.
- **M3 — Defect-recurrence half-life, per named class.** After a promoted
  fix, count recurrences of that class per operating cycle; report the
  half-life in cycles. Zero recurrence is a measured outcome (a rate
  reaching zero), not a ceiling artifact — the measure is the RATE, and
  the baseline is the pre-fix recurrence rate from the census series.
- **M4 — First-attempt success by work class, from a complete attempt
  ledger.** The retrospective census could print instances only, because
  no complete attempt record exists (scheduler retention ends Oct 27).
  The instrument therefore carries its own append-only attempt ledger —
  every governed attempt in the measured lanes is written at attempt
  time, by construction complete — so the rate is computed over a census,
  never a sample of what survived.
- **M5 — Cost per independently verified useful result, metered.** Ratio
  scale, unbounded in both directions. Requires the inference-cost source
  (census decision D-1): until D-1 lands, M5 prints in the census's
  bounded form (DERIVED-floor numerator, exclusions named) and is graded
  accordingly; with metering, it becomes the headline efficiency series.
- **M6 — Correction yield on unseen problems (the cumulative-advantage
  measure proper).** Verified improvements produced per unit of metered
  resource, old-procedure arm vs new-procedure arm, on the SAME unseen
  battery (M1's), under MATCHED budgets (tokens, wall-clock, human
  interventions capped equally), graded by a checker independent of both
  arms. This is the comparison the census design's history-on/history-off
  constraints govern: a capable conventional baseline arm (never a
  crippled control), a third conventional-practice arm preferred where
  the question is advantage over standard practice.

## Pre-registration requirements (all frozen + pinned BEFORE any run)

1. The measure set (above), the difficulty ladder's parameterization and
   extension rule, the problem-generation method and its held-out
   families, the budget envelopes per arm, the checker's identity and
   custody, and the stopping rules — written, hashed, and pinned in the
   run record before the first scored attempt.
2. A pilot pass whose ONLY purpose is saturation testing: any measure
   whose pilot reading sits at ≥ 90% of its attainable maximum is
   replaced or re-scaled before the scored run. The pilot's readings are
   published with the run record either way.
3. The OBS-01 eight-dimension frame (Detection / Recovery / Continuity /
   Correctness / Safety / Autonomy / Efficiency / Recursive learning) is
   the reporting shape for every run — the frame the register already
   carries, so run results land in the register's own next-cycle
   measures (M-1…M-8) without translation.
4. Grading travels with every figure (OBSERVED / DERIVED / ESTIMATE /
   REPORTED / NOT ESTABLISHED). A flat or negative delta is reported as
   measured. Lane (c) stays UNQUANTIFIED until a scored run under this
   instrument computes otherwise — the instrument's existence changes
   nothing about the current grade.

## Inheritance — COMPLETE-CHAIN-01 Stage 3 prep

Stage 3 prep inherits, alongside its own protocol:
- **M1 + M2 + M4** as its measurement spine (its chain attempts are
  exactly the novel-work closures M2 times and M4 counts);
- **the runner wrong-delta correction as a scored check**: the Nov 2
  catch — a runner printing a success-looking line on a validation
  failure (run_case.py; fix: validation failure stated unmistakably,
  match line suppressed or qualified on its face, exit codes untouched)
  — becomes a permanent scored case in every future runner exercise: a
  runner that misreports its own outcome fails the run regardless of
  its other scores;
- **OBS-01** as the reporting frame (above), including its two-loop
  separation: Stage 3's operational results are Loop 1; any claim about
  the improvement PROCEDURE is Loop 2 and needs M6's comparison, not
  Stage 3's narrative.

## Non-goals, stated

No improver run fires under this commission. No public claim is made
from this design. The design does not retroactively re-grade GRSI-01
run-1: its recorded gain stays ZERO (ceiling-qualified, per the census's
binding note) — the instrument governs the NEXT measurement, not the
last one's reading.

— End of design, Nov 5, 2026.
