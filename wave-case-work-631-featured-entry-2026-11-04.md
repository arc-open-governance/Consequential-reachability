# Featured Entry — The Wave Case: WORK 631 (2026-11-04)

*A featured entry in the Book of Consequences: ARC's failure-inclusive,
inspectable record of consequential machine actions — what was proposed,
admitted or denied, what exposure and bounds applied, what it cost, and
how it ended.*

---

**5/5** required evidence elements at PIN · **0** duplicate effects · **1** cold completion of the governed work

The execution session failed.
The work object survived.
Another session completed the authorized work once.

---

Published November 4, 2026. This entry restates one frozen, graded case
at the strength its pinned evidence supports, under the exact scope its
founder ruling states. Nothing here extends the case beyond its pins.

## The milestone, in the ruling's own words

> ARC has documented a real infrastructure-failure case in which a
> governed work record survived execution-session termination, enabled
> successful continuation in another session, and supported an
> externally verified, nonduplicated result.

The founder's ruling of November 4, 2026 classifies the case as **an
achieved work-object continuity and consequence-reconciliation
milestone, with the exact scope of WORK 631 stated**. The unit of the
milestone is the governed work record — not any single execution
session. Continuity despite replacement of the execution session is
the capability under test, and it is the capability the case exercises.

## The demonstration

| | |
|---|---|
| Execution session | **FAILED** |
| Governed work identity | **PRESERVED** |
| Continuation in a new session | **DEMONSTRATED** |
| External effect | **VERIFIED** |
| Duplicate publications | **0** |

Reported findings for the bounded desk-02 case (WORK 631), subject to
examination of the pinned evidence below.

## What happened

On the morning of November 4, 2026, a connection-pool fault in the
platform orchestrating ARC's own work killed agent runs in bursts. The
failure signature, verbatim, was:

`sqlx error: pool timed out while waiting for an open connection`

For every killed run, the platform's terminal report was that
transport string and nothing else: it did not say what the run had
done, what it had not done, or what was left open. Every one of those
questions was settled from ARC's own book — the engagement ledger, the
platform readbacks, and disk state — with zero duplicates fired and
zero work lost across the wave.

### The desk-02 arc — one uncertain effect, resolved end to end

1. **Intent recorded.** A first execution session (hand 4) staged the
   desk-02 post under the full gate stack — stage packet sha256
   f8aa07cd…, text pin 1,188 bytes / sha256 94f77f4c…, duplicate guard
   clear — and attempted the governed WORK append. The session then
   died on the pool fault at 13:53:21Z. From the platform's report
   alone, whether the append had landed was undecidable.
2. **Effect absent, intent present.** A second session's gate stack
   read the ledger and found event **631** — the desk-02 WORK record,
   digest sha256:c9c774b5… — with no acknowledgement, no outcome, and
   no post behind it: the platform showed no desk-02 post
   (posts_count still 32).
3. **Cold adoption.** A third session (hand 6), working only from the
   record, adopted WORK 631, re-ran the full gate stack at ledger head
   634, and fired desk-02 at 14:26:23Z under the *original* work
   record.
4. **Exactly one effect.** Post
   `29ccae32-8096-4d08-84e4-56f103c23bd5`, HTTP 201, byte-exact against
   pin 94f77f4c…, independent challenge agreement 245.00, verification
   successful, posts_count 32 → 33 — exactly +1.
5. **Closed one to one.** ACK 635 / OUTCOME 636 under WORK 631;
   ledger VERIFIED through 636, digest sha256:b71dc606…, decision
   delivered_verified. The full chain — intent, absence, adoption,
   single effect, close — is inspectable from the ledger and the
   readback files.

### Session handoffs

| Object | Role in the case |
|---|---|
| WORK 631 | Persistent logical work identity |
| First hand (hand 4) | Encountered the infrastructure failure; died 13:53:21Z |
| The ledger and the Book | Preserved the identity, history and evidence |
| Hand 5's gate stack | Established from the record that event 631 had landed, with no post behind it |
| Hand 6 | Continued the work from its recorded state; fired and closed it |
| External post 29ccae32… | Independently observable outcome |

### The second instance — fw-08

In the same wave, a different failure pattern. Hand 5's fw-08 post
(`44e61513-8e96-4fa6-944d-5b00984c322c`) was created on-platform at
14:11:04Z, read back byte-exact, and verified; its ledger chain closed
WORK 632 / ACK 633 / OUTCOME 634 (ledger VERIFIED through 634, digest
sha256:af0b689b…) — all *before* hand 5 itself died on the same fault
at 14:23:24Z. The platform's report of that death says nothing of the
completed effect; the Book preserves it.

Together the two instances show why a single SUCCESS or FAILED field
cannot describe the state of persistent consequential work: desk-02 is
safely completing work *after* a session failure; fw-08 is preserving
an already completed effect *despite* a later session failure.

## Grading — the Proof Case's five elements

Unit of grading: the desk-02 governed run — ledger WORK 631, one exact
governed fire, executed by successive sessions across a pool-fault
kill.

| # | Element | Grade |
|---|---|---|
| 1 | Run record incl. verbatim failure signature | **PIN STRENGTH** |
| 2 | Independent effect readback | **PIN STRENGTH** |
| 3 | ARC reconciliation tie | **PIN STRENGTH** |
| 4 | No-duplicate proof | **PIN STRENGTH — demonstrated** (intent present, effect absent, effect executed once under the original WORK, posts_count exactly +1, duplicate guard clear before firing; zero duplicates across the wave) |
| 5 | Cold reproduction method | **PIN STRENGTH — demonstrated live** (hand 6 reproduced the fire cold, from the record alone, and completed it exactly once) |

## Evidence digest

- Case document: `WAVE-CASE.md` — 13,852 bytes, sha256
  `60af2b52279658085637bbd844f027195954e8e17e73e2384d0e6bdad48b4f3f`
- Case manifest: `MANIFEST.md` — 4,621 bytes, sha256
  `11e94478b2c0aeca672511cfa2916d3c0808a048416ef7a468316bfec29f40a4`
- Freeze window: 2026-11-04T12:30:00Z → 14:45:00Z (signature export
  widened to 00:00Z).
- Raw layer, pinned in the manifest:
  - scheduler signature rows — 15,998 bytes, sha256
    `1ce19cbeb4246e497d5494ac8369b887a5f831ceee4b0ead98d41b4bd97300b9`
  - scheduler window counts — 4,211 bytes, sha256
    `3ecb271042d4882845374235a8578467da2ae2868e73ac02111afe2d165bb420`
  - agent spawns window — 5,501 bytes, sha256
    `c9fd406cb284b3913e6b60f083d322b0ace642b0b05976d704011e946d688347`
  - effect evidence index — 5,051 bytes, sha256
    `f7ec25ac33301e0844852c8fc95dd6ad16f3f9621e6023f9b497db6d0215799d`
- Ledger digests at every head of the case's chains: fb938649…
  (through 627), ca3edbea… (through 630), c9c774b5… (event 631),
  af0b689b… (through 634), b71dc606… (through 636). A separate run
  (BOOK-01 run 2) independently read the same head 634 /
  sha256:af0b689b… from a different surface.
- The wave in the frozen window: 534 scheduled job runs started —
  399 succeeded, 120 failed, 14 running, 1 cancelled at read time;
  75 carried a pool / write-admission signature. Trailing-24-hour
  vitals, counted from the tables with families never summed
  (disjoint surfaces): scheduler family 232 job runs carrying the
  signature; agent family 47 of 200 completed spawns carrying the
  same signature.

## Scope — what this case does and does not show

- This is **not** one uninterrupted session, and it is not claimed as
  one. The first session died; the work record is what continued.
- It does **not** claim that every production action path is covered.
  The graded unit is WORK 631, with fw-08 standing beside it as a
  second instance in the same wave.
- The case does not by itself show the complete native Field →
  protected KORE → effect → computed Statement chain. Separate proof
  records stand for production-boundary enforcement; this entry claims
  the demonstrated continuity and reconciliation capabilities, at the
  scope stated.
- The record claimed here is an independent **operator-side** record.
  What the platform internally possesses is not established by this
  case and is never asserted, either way. No violation by any party
  is alleged.

## Carried openly

The case also preserves what did not go well in the same window; a
Book that only records successes would not be this Book.

- A Fieldwalker successor session (hand 7) died with no effects, and
  the next post in that surface's queue, **fw-09, was already
  overdue** when its successor took over. Correctness held; the
  recovery was slower than the schedule.
- **desk-03 was published but closed `delivered_not_verified`**: its
  verification challenge answer — on which the automated solver and a
  plain reading agreed — was rejected by the platform, and the close
  records the outcome truthfully rather than retrying around the
  rejection.
- One item from the wave was still pending at the case freeze: a
  reply whose governed WORK state could not be established before its
  session died. The case carries it open, by name, with its owner and
  resolution path stated (read the ledger head, read the platform,
  fire at most once under a duplicate guard).
- The founder's ruling directs that recovery latency, overdue work,
  human intervention and missed windows be captured alongside effect
  correctness as product-level operating metrics. Those are separate
  questions from the outcome proven here: a system can preserve the
  right work and still recover too slowly, and this entry does not
  grade the speed.

## Examination

The founder's ruling commissions a separately controlled examination
of this case — an examiner re-deriving the case cold from the pinned
artifacts and challenging the identity joins link by link. This
entry's claims stand at the grades above on the pinned evidence; the
examination's result, when it lands, will be recorded against this
entry.
