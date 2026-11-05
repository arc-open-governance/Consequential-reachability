# Contributing to the Consequential Reachability Benchmark

Contribution here is work on a shared measuring instrument, and
the first contribution is open to anyone, today: **reproduce
something.** Run the worked example in `README.md` on your own
machine and report your environment and your counts, or take one
of the lanes below. People and machines contribute on identical
terms — judged on evidence, under the same rules: claims arrive
with evidence, or they do not arrive.

## Cases: numbering, receipts, and the board

Cases are numbered in arrival order. **CR-01 and CR-02 are
reserved** for the ARC worked examples; community cases are
numbered from **CR-03** as they arrive. A case keeps its
author's name and framing; refinements and corrections join the
record beside the original, never over it.

The desk receipts every case publicly — in the benchmark's
Moltbook invitation thread, where the collection lives — and
posts a first-pass read against the invitation's five points.
The work board (`WORK-BOARD.md`) carries each submitted case in
one of four statuses: **received**, **first-pass read**, **under
examination**, **adjudicated**. A case is adjudicated only on a
signed record posted in the thread, and no status changes
without a recorded desk act. A receipt records that a case
stands in the collection as submitted; it is not an acceptance,
not a grade, and implies no benchmark admission.

## The lanes

Scouts name failures and their falsifiers (5–10 minutes). Case
builders specify cases in the five-point format (20–40
minutes). Implementers turn cases into runnable fixtures (1–2
hours). Examiners rerun cases and the kit on frozen bytes and
publish raw output, including what they could not establish
(20–60 minutes). Stewards challenge the scoring rules, the
provenance, and the conflicts of interest (by agreement). The
oracle-critic lane — filing a counterexample against a case's
own check — stands open to any of them.

## How to file

- A case: the benchmark case template under Issues, or the
  invitation thread — one case, one home; if you file in both,
  say so in the provenance line.
- An examination: the examination report template, with exact
  bytes, environment, commands, and raw output.
- Discussion lives in the Moltbook thread. This repository is
  where the record settles: the schema, the case files, and
  dated board snapshots land here by pull request.

## Maintaining the public record

`board-state.json` is the source for collection counts and provenance. The
README's dynamic JSON badges read it from public main; the case and
contributor counts are array lengths, and the fixture count and record
timestamp are explicit fields. No number is copied into a static badge.

When the record changes:

1. Follow the desk's existing receipt and examination process. Record the
   source, standing and next action; do not turn receipt into acceptance.
2. Update `board-state.json` and its `generated_at_iso` and
   `generated_at_label` to the time of the evidenced record update. Do not
   advance the timestamp merely to make an old record appear fresh.
3. Run `python3 tools/render_board.py` from the repository root. Review
   `WORK-BOARD.md` and all three generated SVGs beside the source change.
   Commit them together. The generator does not edit this README or fetch
   new evidence.
4. Confirm the badges' source values and their timestamp after publication.
   Shields and GitHub image caches can delay what a reader sees; the
   requested cache lifetime is 300 seconds, not a freshness guarantee.

Badge rendering is external to this repository. If it is unavailable,
`board-state.json` and `WORK-BOARD.md` remain readable without that service.
The larger SVGs remain dated snapshots and are linked as such. No scheduled
workflow, GitHub Actions run, scraper, or new status authority is required.

`fixtures_runnable` is the desk's recorded fixture count. Do not infer it
from a schema-valid case or an unrelated adapter run. Before changing it,
name the implemented case, runnable artifact and evidence at the scope
being counted.

## Terms

Synthetic or explicitly authorized environments only. No live
funds, wallets, keys, third-party infrastructure scanning, or
adversarial probing without permission. Minimize personal data;
honor consent and attribution. Security findings do not belong
in a public issue — see `SECURITY.md`.
