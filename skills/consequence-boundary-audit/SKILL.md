---
name: consequence-boundary-audit
description: >-
  Run a consequence boundary audit: can your agent still act after permission
  is withdrawn? Reproduce a pinned Examiner Kit case and report exactly what
  it proves, scaffold a reachability case for your own authorized system, and
  prepare a source-backed result or challenge for the Consequential
  Reachability Benchmark. Use when an agent's authorization, revocation, or
  tool-call boundary needs a reproducible test instead of an opinion.
license: Apache-2.0 (code) / CC BY 4.0 (documentation)
metadata:
  version: 0.1.0
  kit: arc-examiner-kit v0.2.0 (pinned, sha256-verified at runtime)
---

# Consequence Boundary Audit

**Can your agent still act after permission is withdrawn?**

This skill runs a synthetic examination, checks the evidence, states what
was and was not proven, and helps you prepare a reproducible case. It solves
a concrete problem first — a failing authorization test, a revoked API
permission, a workflow that acts despite a hold — and introduces the wider
consequential-reachability method through that evidence afterward.

## What this skill does, in order

1. **Reproduce an existing case.** `scripts/reproduce_case.py` downloads the
   pinned ARC Examiner Kit v0.2.0 release asset, verifies its sha256 against
   the pin in this skill before trusting a single byte, runs its examination
   end to end, and reports the outcome control by control.
2. **Build a test for your own authorized system.** `scripts/build_case.py`
   scaffolds a Consequential Reachability Benchmark case — frozen situation,
   permission graph, revocation events, actions, and the oracle that decides
   each action — and validates it with the benchmark's own validator and
   runner, shipped in this package at their pins.
3. **Hand off a source-backed result.** `references/HANDOFF.md` gives the
   routes for submitting a reproduced result, a divergence, or a new case
   for independent examination.

## Ground rules — read before running anything

- **Synthetic results are not production evidence.** The Examiner Kit ships
  a fixture reference engine. A pass establishes that the claimed semantics
  hold inside an inspectable implementation the examiner controls, at local
  record-layer strength. It establishes nothing about any deployed system.
  Every report this skill produces carries that distinction on its face.
- **Your own systems only.** Build and run tests against systems you are
  authorized to test, and permitted synthetic environments. This skill
  authorizes no testing of anyone else's system, and no posting anywhere.
- **Outcomes are reported as observed.** FAILED, UNKNOWN, and NOT
  EXPRESSIBLE are honest results. Never round an outcome up, and never
  present a fixture result as a production finding.
- **Pins before trust.** The kit asset, the case schema, and the worked
  example in this package are all sha256-pinned. If a digest does not match,
  stop and report the mismatch — that is a finding, not an inconvenience.

## Job 1 — Reproduce an Examiner Kit case

```sh
python3 scripts/reproduce_case.py --workdir ./audit-work
```

The script:

- fetches `examiner-kit-v0.2.tar.gz` from the public release
  (`arc-open-governance/arc-examiner-kit`, tag `v0.2.0`) and verifies
  sha256 `aba968025892f5aa87bbdabfae2f749ead638ecb108c09bc093422f912977167`
  (24,740 bytes) before extraction; a mismatch aborts the run;
- runs the kit's single entry command (`python3 run_exam.py`), which
  verifies the kit's own `MANIFEST.json` (13 files) before testing;
- reports the six original tests (12/12 controls) and the two v0.2
  adversarial tests (13/13 controls) against their frozen expectations,
  plus the run's `results_digest`, and writes `reproduction-report.json`
  into the work directory.

What those numbers mean: v0.2 corrects exactly two defects that an outside
source-level audit raised against v0.1 and a governed reproduction then
confirmed at fixture strength — receipt-field completeness (a receipt
altered in one field at a time was still verified by v0.1) and multilevel
revocation (v0.1 detected revoked ancestry transitively but enforced it
only at direct reliance). The adversarial tests A1 and A2 encode those
reproductions. If your run reproduces them, you have replicated a public,
checkable result — the starting point for examining your own stack.

## Job 2 — Build a case for your own authorized system

```sh
python3 scripts/build_case.py --out ./my-case.json --title "Short case title"
python3 scripts/validate_case.py ./my-case.json references/CASE_SCHEMA_DRAFT.json
python3 scripts/run_case.py ./my-case.json references/CASE_SCHEMA_DRAFT.json
```

A benchmark case states, in a fixed form:

1. the **frozen situation** — the initial state, in full;
2. the **permission graph** — who holds what, and what depends on what
   (declared dependencies are first-class; revocation propagates over them);
3. the **revocation events** — what is withdrawn, and when, on the same
   timeline as the setup;
4. the **actions** — each prospective consequential action, its position on
   the timeline, and what it depends on;
5. the **oracle** — the expected decision and expected effect for every
   action, stated before the run, so the runner's computed outcomes can be
   compared against a claim rather than an impression.

The headline measurement is the **revocation delta**: the set of actions
whose correct outcome changes because a permission was withdrawn. Worked
example: `references/CR-02-candidate.json` (transitive revocation must
prevent indirect new reliance without blocking unrelated actions) validates
13/13 and its computed outcomes match its oracle, including the delta. The
schema is `references/CASE_SCHEMA_DRAFT.json`
(sha256 `b0b0c9a37b93305dfe5433e47c89200aaf649de369ad346f90814e21e42fc44c`).

Map your own system onto the same shape: name the permission your agent
acts under, one action that should survive its withdrawal, one that should
not, and the observation that would decide between them. The scaffold marks
every field you must replace; a case that validates and runs is a test your
future examiners can repeat exactly.

## Job 3 — Hand off the result

See `references/HANDOFF.md`. In brief: kit results and divergences go to the
Examiner Kit repository under its `SUBMITTING.md` rules (failures are
first-class submissions); benchmark cases and challenges go to the
Consequential Reachability Benchmark
(`arc-open-governance/consequential-reachability`). That repository's
opening is in progress — its README stands publicly and its full payload is
being landed; the kit repository and the benchmark schema it carries are
the live public routes today, and HANDOFF.md names them exactly.

## Files in this package

| File | What it is |
|---|---|
| `scripts/reproduce_case.py` | Fetch, pin-verify, run, and report the Examiner Kit v0.2.0 examination |
| `scripts/build_case.py` | Scaffold a benchmark case for your own authorized system |
| `scripts/validate_case.py` | The benchmark's case validator (13 checks), at its pin |
| `scripts/run_case.py` | The benchmark's case runner (computed outcomes vs oracle, revocation delta), at its pin |
| `references/CASE_SCHEMA_DRAFT.json` | The benchmark case schema, at its pin |
| `references/CR-02-candidate.json` | A worked example case, at its pin |
| `references/KIT.md` | Examiner Kit pins, provenance, and strength lines |
| `references/HANDOFF.md` | Submission routes for results, divergences, and cases |
| `LICENSE.md` | Terms: Apache-2.0 for code, CC BY 4.0 for documentation |

## Provenance

The six kit tests answer an examination question credited to the outside
examiner **vina** (ARC Issue #35): is a receipt bound to the consequential
update, or merely to the query that retrieves it? The kit's answer, at
fixture strength: a receipt is anchored to the consequential request and
its settlement, not to the query — and the observed external effect is a
separate claim that must be established by evidence. This skill exists so
any agent can check that answer, and its limits, for itself.
