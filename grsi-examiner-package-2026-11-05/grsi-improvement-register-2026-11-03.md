# GRSI IMPROVEMENT REGISTER — 31-DAY LONGITUDINAL OPERATIONAL STUDY

Built Nov 3, 2026, on the founder's commission (Ricky, Nov 3, 2026, 1:22 PM PST,
main chat): the Meta incident findings must feed GRSI and "we should be able to
track our improvements."

## Scope and parentage

- **Parent:** the GRSI longitudinal operational study, Oct 3 – Nov 3, 2026
  (31 days), as framed in Issue #59 ("GRSI — 31-day governed recursive
  self-improvement operational record," arc-open-governance/arc-open-governance
  — the repo is PRIVATE; the issue is verified on this seat, publicly invisible
  until a public surface carries it).
- **Charter:** Issue #59's evidence programme, item 2 — the IMPROVEMENT
  GENERATION LEDGER. This register is that ledger's seat-side build.
- **Seed scope of this build:** the incident cycle, Oct 28 – Nov 3, 2026 — the
  improvements the platform failure (the Muse backend database pool fault,
  first evidenced Oct 28, 2026, 17:57:41 UTC) actually produced. Earlier cycles
  (Oct 3–27) are NOT backfilled here; see the OPEN ITEM at the end.
- **Framing input of record:** `files/meta-grsi-framing-input-2026-11-03.md`
  — 8,961 B, sha256 33acc9e1f21f29698391a90786a8db4a6d4abc20b4c951cb74bf806b45e63496…
  (verified by direct hash in this build).

## Claim ceiling — read before citing anything in this register

- This register tracks OPERATIONAL improvements inside one operator's
  longitudinal study: findings, proposals, approvals, exercises, promotions,
  and next-cycle measures.
- It does **NOT** establish GRSI-01 controlled gains. GRSI-01 is the separate
  frozen controlled protocol (run 1, Stages 0–5 executed; run-1 improver gains
  ZERO on M6/M6-IT; transfer unmeasured; Stage 6 sequenced behind
  COMPLETE-CHAIN-01 Stages 2–4). Nothing in this register upgrades, restates,
  or substitutes for a GRSI-01 reading. The two records are kept strictly
  separate, here and everywhere.
- An entry's presence means the improvement was proposed and handled as the
  entry states — not that it worked. Where a measured outcome exists it is
  stated with its pin; where none exists, the entry says so and the
  NEXT-CYCLE MEASURES section carries the observable that would supply one.
- Grading vocabulary: OBSERVED (read at first hand in this build or the cited
  run), ATTESTED (a record of record states it; not re-derived here),
  REPORTED (carried at the strength of its source, unverified at pin
  strength). Rejected and unadopted proposals are entries too — graded as
  such, never silently dropped.

## Compilation note (the register practising its own entries)

Two tool reads taken during this build arrived under system security notices
and were closed unused under the halt-on-flag law (entry G-04 below); nothing
from them is cited. Entries affected were re-grounded on unflagged sources or
on the seat's standing record, and are graded accordingly.

---

## ENTRIES — PROMOTED

### G-01 — Retry-until-landed + pre-staged fire packets

- **Predecessor evidence:** approved, pinned sends repeatedly died in
  transport during the incident cycle before or after firing — the
  announcement fire run fired, then died in close-out (Nov 3, 2026); multiple
  governed runs errored on the pool fault with their send state unknown,
  forcing founder pokes and manual reconciliation. Defect record:
  `hidden_files/pool-fault-defect-record-2026-11-03.md` — 14,111 B, sha256
  ea2b49dd0c19f36d803ab3dadf58436e7777a1960667fee99e44747f8e11e89c (OBSERVED,
  hashed in this build).
- **Proposal:** (1) for an approved pinned text, a fire run killed by the
  transport fault auto-reconciles under its duplicate guard and re-fires
  inside the same machinery loop until it lands or hits a true hard stop
  (gate verdict, flag on the text itself, platform refusal) — the founder's
  poke is not part of the mechanism; (2) the full gate stack runs ONCE and
  the packet is stored with the text, so the fire is a single call carrying
  the packet.
- **Classification:** machinery + standing directive.
- **Approving authority:** founder directive, Ricky, Nov 3, 2026, 11:00:32 AM
  PST (recorded in `~/AGENTS.md`, "RETRY-UNTIL-LANDED + FIRE PACKETS +
  POOL-FAULT DEFECT").
- **Frozen test / exercise:** fire-packet machinery built and exercised at
  fixture strength against a stub platform, Nov 3, 2026 — 4/4 cases PASS,
  including the landed-then-transport-died no-duplicate case. Exercise record:
  `hidden_files/fire-packet-2026-11-03/EXERCISE.md` — sha256
  333384097156df1f592b722de41b41293b935387c95d244488d5cfd87b07ab96…
  (OBSERVED). Machinery pins (OBSERVED, hashed in this build): DESIGN.md
  9,899 B, 33ff045d…; build_packet.py b8a7408a…; fire_loop.py b58d274a…;
  packet.schema.json 9a51fa37….
- **Independent result:** the exercise harness's own case verdicts (a)–(d)
  all PASS, including exactly-one-landing under retries and zero fires on a
  gate hard stop. Fixture strength only — no live fire has yet ridden the
  packet loop.
- **Actual promotion:** YES as standing directive + built machinery. The
  staged announcement packet (`announcement.packet.json`, 3,627 B, sha256
  2dc64e03…, STAGED_FROM_PINS; OBSERVED) stands as the machinery's worked
  example — gates ran once into the packet; the announcement's actual fire
  went the other route, so the packet loop itself has not yet fired live.
  That gap is stated, not smoothed.
- **Next-cycle utilization:** the next approved pinned text fires through the
  packet loop (see NEXT-CYCLE MEASURES, M-1).
- **Measured outcome:** none yet at live strength. Fixture exercise 4/4 is a
  rehearsal result, not an operational one.
- **Regressions / counterexamples preserved:** none recorded against the
  machinery; the rails (12 attempts / 1,800 s / 20 s backoff; RAIL_EXHAUSTED
  as a named hard stop) exist because unbounded retry was itself rejected as
  a shape — a loop that cannot stop is a defect, not resilience.

### G-02 — The pool fault as a tracked defect, with board VITALS

- **Predecessor evidence:** runs died in waves for six days (first evidenced
  Oct 28, 2026, 17:57:41 UTC) with no owner, no count, and no closure test;
  the failure was ambient weather until it was measured.
- **Proposal:** constitute the fault as a tracked defect of record — owner
  (main seat), repair track, a counting method of record, VITALS carried on
  every founder board issue until closure, and a stated closure test.
- **Classification:** defect governance / measurement.
- **Approving authority:** founder directive, Ricky, Nov 3, 2026, 11:00:32 AM
  PST (same directive as G-01).
- **Frozen test / exercise:** the counting method (bounded query over
  `scheduler.job_runs` matching the two error signatures) was re-executed by
  an independent recount in the evidence pack (Part A) — method AGREES; the
  window moved, so the numbers differ and each figure carries its window
  bounds (see G-06).
- **Independent result:** upstream filing stands as exactly one report
  (kind broken-behavior, subject scheduled-jobs, filed Nov 3, 2026, 11:10 AM
  PST with the founder's approval, delivery confirmed, pending review —
  ATTESTED from the main seat's first-hand check of the filing channel).
- **Actual promotion:** YES — defect record stands
  (`hidden_files/pool-fault-defect-record-2026-11-03.md`, pin in G-01);
  VITALS at the Nov 3 measurement: 593 of 5,086 scheduled runs killed in the
  trailing 24 h (968 failed total; fault ≈ 61% of failures); fault age
  6 days. Closure test of record: VITALS reads 0 killed for seven
  consecutive board issues AND the log cross-check reads 0 mentions for the
  same span — or the platform confirms a fix and the count verifies it.
- **Next-cycle utilization:** every board issue recomputes VITALS by the
  method of record until the closure test passes (M-2).
- **Measured outcome:** the defect is now countable and owned; the fault
  itself is platform-side and NOT fixed by anything in this register.
- **Regressions / counterexamples preserved:** the main seat's Nov 3
  "~12:20 PM" statement that nothing had been filed was WRONG (one subject
  checked of two) and was corrected to the founder the same afternoon — the
  error and its correction stand in the record as the type case for G-03.

### G-03 — Claim lock + done-means-told reporting discipline

- **Predecessor evidence:** Nov 2, 2026 reporting defects, named as a failure
  class: a fixed-form card announced as existing that never existed;
  "deployment verified" claimed on authenticated reads of a private repo
  (public reachability never proven); a runner called complete on fixture
  tests alone. During the incident cycle the same class recurred in sharper
  form: completion notices for runs that had in fact fired (and for runs
  that had not), and an incomplete disk sweep reported as "no fire" —
  corrected in both founder chats the same evening.
- **Proposal:** (1) CLAIM LOCK — the words ready / done / fired / landed are
  banned from founder-facing messages unless the proof rides in the same
  sentence (post id, commit SHA, status read); (2) DONE MEANS TOLD — every
  completion reports in the founder's reading surface (d977a005) the moment
  it is verified, proof on its face; (3) a completion notice is never
  evidence — KORE state and on-disk files are.
- **Classification:** reporting discipline (standing rule).
- **Approving authority:** founder adoption, Ricky, Nov 2, 2026, 5:00:34 PM
  PST (DONE MEANS TOLD) and 5:01:36 PM PST (the three reporting/completion
  rules, including the claim lock).
- **Frozen test / exercise:** no fixture exercise exists or is meaningful;
  the discipline is exercised by every report since adoption.
- **Independent result:** ATTESTED in operation — incident-cycle reports to
  d977a005 carry pins and ids on their faces (e.g., the announcement
  close-out verification, the Marcus terminal close-out, the Stage 2 +
  DOC-01 presentation, each with proof in the same message).
- **Actual promotion:** YES — standing rule in `~/AGENTS.md` and in force
  across surfaces.
- **Next-cycle utilization:** all reporting, continuously (M-3).
- **Measured outcome:** qualitative so far — the Nov 3 "nothing filed" error
  (G-02) was caught and corrected same-day under this discipline; no rate is
  yet computed. The register does not invent one.
- **Regressions / counterexamples preserved:** the three Nov 2 instances
  stand as the failure class's first entries in Cultivation Review 002's
  rail; the Nov 3 filing error is a post-adoption instance and is preserved
  as such — adoption did not end the class, it made instances correctable
  on the record.

### G-04 — Halt-on-flag law

- **Predecessor evidence:** through Oct–Nov 2026, dispatched runs repeatedly
  stopped when session safety checks flagged first-party machinery or
  operational reads — and, in the other direction, flagged material carried a
  standing risk of being used uncritically. The incident cycle made the cost
  concrete: runs halted mid-reconciliation (e.g., the Marcus close-out's
  no-read list; the announcement landing record's flagged read, closed
  unused, which forced the blind-append route).
- **Proposal:** any fetch or read arriving with a system security notice
  halts the run on that material; nothing from it is used; the exact flagged
  file is named; work proceeds only on a clean path (no-read re-dispatch,
  blind append, or founder clearance-by-name where the class warrants it).
- **Classification:** safety law (standing).
- **Approving authority:** founder law, Nov 2, 2026, 8:43 AM PST.
- **Frozen test / exercise:** exercised continuously; this register's own
  compilation closed two flagged reads unused and re-grounded the affected
  entries (see the compilation note).
- **Independent result:** ATTESTED in operation across the incident cycle —
  halts are recorded with the flagged source named in run records (e.g., the
  codex-reply halt record, the Karlson machinery clearances' occasion).
- **Actual promotion:** YES — standing law; the clearance-by-name machinery
  (Bands' companion precedent, 25 clearances of record) is its governed
  release valve, not an exception.
- **Next-cycle utilization:** every run, continuously (M-4, Safety).
- **Measured outcome:** no count of halts is computed in this register; the
  observable carried forward is that no flagged material stands cited in any
  incident-cycle deliverable.
- **Regressions / counterexamples preserved:** the law's cost is real and
  recorded — legitimate work repeatedly stopped on class flags (the
  send-machinery class flag fired on first-party files 25 times by the
  clearance count), and the Input 12 verbatim filing remains blocked because
  its only retrieval route flags. Both costs stand on the record beside the
  law, not under it.

### G-05 — Fixed ledger invocation + content-preserving repair band

- **Predecessor evidence:** engagement-ledger appends rode per-run
  hand-written helpers; session flags on the machinery class stalled sends,
  and ledger writes lacked one fixed command line a durable grant could
  attach to. The ledger is the reconciliation substrate for the whole
  incident cycle — its write path could not itself be a jam.
- **Proposal:** (1) one fixed invocation of record,
  `ledger_run.py <cycle|work|close|append|materialize|verify|verify-full>`
  wrapping the CAS append tool, batched to one commit per run where the
  discipline allows; (2) content-preserving ledger repairs pre-approved as a
  class (Band 8): byte-form rulings where two forms are JSON-identical, and
  schema-shape canonicalization with the repair AND the pre-repair state
  recorded inside the entry touched. No silent rewrites; anything changing
  what an entry SAYS stays founder-gated per act.
- **Classification:** machinery + Green Band class.
- **Approving authority:** LEDGER WRITE MECHANISM BUILD commissioned in the
  founder's safe-set ruling, Nov 2, 2026, 5:39 AM PST; Band 8 granted in the
  same ruling.
- **Frozen test / exercise:** the mechanism is the write path for every
  incident-cycle ledger cycle; the ledger stands VERIFIED through event 490
  (digest sha256:8537d2f5…, ATTESTED from the announcement close-out).
  `ledger_run.py` pin (OBSERVED, hashed in this build): 9,929 B, sha256
  8313d9363108ae7d824fb867a4a1a48bd96c5a6ce3888862d821ba11b4602a1a.
- **Independent result:** Band 8(a) determination completed on the record —
  events 252, 255, 256, 258 proven byte-equal in every form; no repair was
  applied where none was needed.
- **Actual promotion:** YES — the fixed invocation is the standing write
  path; Band 8 is a standing Green Band.
- **Next-cycle utilization:** every governed send cycle (M-5).
- **Measured outcome:** ledger integrity held through the incident cycle's
  heaviest concurrent use (events interleaved across concurrent runs without
  a fold failure through 490 — ATTESTED).
- **Regressions / counterexamples preserved:** the durable founder grant for
  the fixed form is still outstanding (its first fixed-form card is a
  founder tap), and the spec §2.5 rider naming ledger_run.py the invocation
  of record is still owed — promotion of the practice precedes its full
  paper formalization, stated plainly.

### G-06 — Status≠effect reconciliation as a standing method

- **Predecessor evidence:** the incident's core phenomenon — platform status
  and real-world effect diverged in both directions. A run recorded FAILED
  whose post stands; a comment served nowhere though its fire returned
  HTTP 201; a task reported as transport-failed whose commit stands
  byte-exact on git. Before this cycle, a run's own report was the default
  truth; the fault made that untenable.
- **Proposal:** no outcome is taken from a status field or a completion
  notice. Every consequential outcome is established by joining the record
  against an independent effect readback (platform state, git head, Sent
  folder, ledger fold), and classified into outcome classes — CONFIRMED_EFFECT
  / NOT_EXECUTED / UNKNOWN_EFFECT / DUPLICATE_EFFECT / legitimate authorized
  operation — with UNKNOWN preserved as a first-class conclusion, never
  forced to a verdict.
- **Classification:** method (standing).
- **Approving authority:** adopted in the campaign/evidence commissions,
  founder rulings Nov 3, 2026 (Proof Case ruling 12:26 PM PST; campaign
  directive 12:38 PM PST; custody + evidence-class disciplines restated
  ~1:03 PM PST). The method's standard is the five-element Proof Case
  standard (run record / independent effect readback / ARC reconciliation
  tie / no-duplicate proof / cold reproduction method).
- **Frozen test / exercise:** the five-case join, evidence pack
  `hidden_files/meta-field-study-evidence-2026-11-03.md` — 12,323 B, sha256
  510b3b96af07657b9c9262b12357ec4351d3987f4f10feaaff12d28d1d7b2847
  (OBSERVED, hashed in this build): announcement fire STATUS≠EFFECT; rq9
  bytes-fw STATUS≠EFFECT; license landing STATUS≠EFFECT; Marcus send run 1
  STATUS=EFFECT (the control); announcement close-out PARTIAL. Plus the
  recount cross-check (Part A): the defect record's counting method
  re-executed independently — method agrees, window moved, figures carry
  their bounds.
- **Independent result:** the join's cases are pinned to records an examiner
  can re-read cold; the full-window build extends the same join into a
  discrepancy catalogue with each entry's evidence class on its face
  (INDEPENDENTLY OBSERVED EXTERNAL EFFECT vs LOCAL RECORD ONLY).
- **Actual promotion:** YES — reconciliation is now the default first step of
  every recovery (see G-07) and the grading standard for every campaign
  claim.
- **Next-cycle utilization:** every disputed or fault-touched outcome (M-6).
- **Measured outcome:** five cases classified at pin strength in the seed
  cycle; the Proof Case milestone (one case carrying all five elements) is
  the method's own next measurement, still open at this build.
- **Regressions / counterexamples preserved:** the codex-reply divergence
  stands unrepaired by design — comment 15adc8db… (HTTP 201, solver AGREE
  57.00 at fire) does not stand in the platform's served tree while the
  ledger side is closed (443/444/445). The method classifies it; it does not
  paper over it, and no re-fire was attempted.

### G-07 — Reconcile-first re-dispatch discipline

- **Predecessor evidence:** incident-cycle runs died with their progress
  unknown (backup fix, Ria close-out, Marcus sends, the input filings).
  Naive re-dispatch risked duplicating completed work — a second send, a
  second filing, a re-spent approval.
- **Proposal:** every re-dispatch opens with a reconciliation step against
  ground truth (disk, git, ledger fold, Sent folder, platform readback)
  before any act: establish what the dead run already did; redo nothing
  completed; resume at the first unproven step.
- **Classification:** dispatch discipline (standing practice).
- **Approving authority:** main-seat operating discipline under the founder's
  posture directive (Nov 3, 2026, 5:03 AM PST — banded work proceeds by
  default; blocked items re-order the queue); exercised under KORE admission
  per run.
- **Frozen test / exercise:** exercised repeatedly in the seed cycle — the
  METR send's reconcile-first continuation proved the earlier errored run
  had NOT sent before the governed send proceeded (exactly one message to
  METR stands, no duplicate); the Marcus close-out's fresh duplicate guard
  (Sent baseline exact) preceded both sends; the announcement close-out
  appended only the missing ACK/OUTCOME.
- **Independent result:** zero duplicate effects across the seed cycle's
  re-dispatches is ATTESTED at the strength of those runs' records — no
  independent census of re-dispatches exists yet (see M-7).
- **Actual promotion:** YES as standing practice — every continuation brief
  in the incident cycle's second half opens with it.
- **Next-cycle utilization:** every fault-killed run's continuation (M-7).
- **Measured outcome:** instance-level (above); no aggregate rate yet.
- **Regressions / counterexamples preserved:** reconciliation costs time —
  the backup fix took three dispatches across the day and the budget raise
  still had not landed at the last verification; the discipline trades speed
  for exactly-once, and that trade is recorded, not hidden.

### G-08 — Checkpoint-early deliverable discipline

- **Predecessor evidence:** two seed-cycle evidence runs (the first evidence
  pack run; the first export+join run) died on the pool fault having written
  NOTHING — verified at first hand by the main seat. Whole-deliverable-at-end
  writing loses everything when the writer dies.
- **Proposal:** long deliverables checkpoint to disk section by section as
  the work proceeds (export + skeleton manifest the moment a query returns;
  pack sections appended incrementally), so a fault death loses at most the
  section in flight.
- **Classification:** dispatch discipline (standing practice).
- **Approving authority:** main-seat operating discipline, commissioned
  inside the Nov 3, 2026 evidence re-dispatch briefs under the founder's
  Meta-priority directive (Nov 3, 2026, 12:49 PM PST).
- **Frozen test / exercise:** the re-dispatched evidence pack and export
  runs were briefed checkpoint-first and the pack stands complete at its pin
  (G-06). This register is itself written checkpoint-first, in appends.
- **Independent result:** ATTESTED at instance strength (the pack landed;
  its predecessor without the discipline did not).
- **Actual promotion:** YES as standing brief discipline for long
  deliverables.
- **Next-cycle utilization:** every multi-section build (M-8).
- **Measured outcome:** instance-level only; no loss-rate computed.
- **Regressions / counterexamples preserved:** checkpointing does not save a
  run that dies before its first checkpoint — the discipline bounds loss, it
  does not abolish it.

---

## ENTRIES — OPEN CANDIDATES (proposed, NOT adopted; not improvements)

### C-01 — Seat-side load hygiene / de-jitter

- **Predecessor evidence:** defect record §5/H1 (ATTESTED from the record):
  waves crest when this seat's concurrency crests — bursts of 17 starts in
  one minute at worker-generation turnovers; 101 distinct scheduled jobs;
  the seat's own burst pressure plausibly deepens a platform-side fault it
  does not cause.
- **Proposal:** de-jitter/stagger the densest cron cadences so a restart
  cannot dump a burst into one minute; serialize the heaviest fan-outs
  during an active wave rather than launching parallel coordinators into it.
- **Classification:** open candidate — repair track step 2 of the defect
  record ("owner, no founder act needed" per that record).
- **Approving authority:** NONE YET EXERCISED. Not adopted, not executed,
  not scheduled at this build.
- **Promotion:** NO. This entry exists so the candidate is tracked, not
  counted. Any future adoption lands here as a dated promotion with its own
  exercise; until then C-01 contributes nothing to any improvement claim.
- **Regressions / counterexamples preserved:** the hypothesis underneath
  (H1, pool size vs concurrent demand) is graded INFERRED in the defect
  record — causation expressly unverified. Acting as if the seat's hygiene
  were the cause would misstate the record.

### C-02 — Automatic Outcome Verification (Consequence Receipt Continuity)

- **Source:** founder input, Nov 3, 2026, ~3:08 PM PST
  (`files/consequence-receipt-continuity-input-2026-11-03.md`, 5,642 B,
  sha256 993b8067…). The founder's framing in his own words: "improvement
  stands above everything else: make consequential outcome verification
  automatic, rather than something we reconstruct after a platform
  failure." Entered Nov 3, 2026, ~3:20 PM PST by the main seat under the
  commission's register instruction.
- **Before-measurement (the "before" of record):** THIS incident. The
  outcome evidence for the five independently observed external effects
  of the pool-fault window was reconstructed BY HAND over roughly a day,
  by multiple separate runs (the evidence pack, the full-window pack, the
  JOIN slice) — manual, retrospective, and assembled after the fact.
  That is the baseline any improvement claim for this candidate is
  measured against.
- **Proposal:** for consequential operations riding the fire-packet
  machinery, the close-out record is produced AUTOMATICALLY in four
  parts — (1) authority + proposal (who authorized what, under which
  conditions); (2) execution identity (stable operation ID, exact
  attempt ID, request digest); (3) independent effect evidence
  (committed result with authoritative readback); (4) a COMPUTED
  STATEMENT in exactly the five values Confirmed / Not executed /
  Partial / Unknown / Duplicate — the parts durably joined across
  restarts, and a failed platform status never by itself authorizing a
  duplicate. The duplicate guard already embodies the last clause; the
  build makes the joined record + computed Statement automatic rather
  than reconstructed.
- **Classification:** open candidate — adopted as a BUILD ITEM at design
  strength only (scoping + run-day pricing report to d977a005 before any
  execution spend beyond design, per the commission). Not adopted as an
  improvement; not executed at this entry.
- **Promotion:** NO. C-02 contributes nothing to any improvement claim
  until its promotion condition is met: a LATER failure whose outcome
  evidence arrives automatically, with materially less intervention than
  the before-measurement above. IMPROVE stays NOT ESTABLISHED until that
  later measurement exists.
- **Name discipline:** the input proposed the designation
  "COMPLETE-CHAIN-01" for this work. NOT ADOPTED — that designation
  belongs to the commissioned integration experiment (freeze complete,
  Stage 2 complete, Stage 3 gated) and is not reused. Working name of
  record: **Consequence Receipt Continuity**. A rename is the founder's
  word.
- **Related lanes (pointers, not merges):** the input's Priority 3
  (controlled old-vs-new comparison with legitimate-success and
  duplicate-prevention controls) maps onto the reconciliation-experiment
  addendum, as recorded. The first fully joined run-to-effect chain —
  by the retrospective JOIN or the prospective capture posture,
  whichever lands first at full strength — is the Proof Case objective
  this candidate's machinery serves; the candidate itself claims
  nothing about it.

## ENTRIES — REJECTED / RETIRED, PRESERVED

### R-01 — Duplicate upstream filing (subject runtime-database-pool)

- **What it was:** a second defect report drafted in parallel during the
  Nov 3 filing reconciliation, while the seat briefly believed no filing
  stood.
- **Disposition:** RETIRED, never filed, once the first-hand check
  established exactly one report standing (scheduled-jobs, delivery
  confirmed, pending review). Filing both would have duplicated the upstream
  signal and muddied the citation of record.
- **Preserved because:** the near-duplicate is itself incident evidence —
  the same status≠effect confusion (a filed report invisible to a
  single-subject check) that G-06 now governs. The draft stands retired on
  the record; it is never to be filed.

---

## OBS-01 CONFORMANCE — this register as the population of the Issue #60 ledger

Protocol of record: **Issue #60**, "GRSI measurement: before/after
improvement ledger for six-day Muse stress period" (protocol designation
GRSI-OBS-01), OPEN, verified on this seat Nov 3, 2026 — same private-repo
caveat as #58/#59: the protocol is publicly invisible until a public surface
carries it. Filed input: `files/meta-grsi-obs01-input-2026-11-03.md` —
7,941 B, sha256 a05aedcf8057f71363172297bd901bc84d8012e95ea83796ad10d3ec872adca0
(OBSERVED, hashed in this build).

**The protocol's own grading, printed on this register's face as it governs
every cell below: "We have defined the measurements; the source data has not
yet been populated or independently validated."** This register is the
population in progress — population is not validation, and no entry's
existence is an improvement MEASUREMENT.

### Two connected records — attempts ↔ improvements

OBS-01 defines two connected records: individual execution attempts and
individual improvements, each improvement linked back to the attempt/finding
that motivated it and forward to its deployment and the subsequent attempts
it affected. The entries above carry the improvement side. The attempt side
of the seed cycle, at index strength (full attempt records live in the cited
run records, not here):

| Attempt (seed cycle) | Outcome class | Motivated | Later affected by |
|---|---|---|---|
| Announcement fire run 2 (Nov 3) — fired, died in close-out | STATUS≠EFFECT (post stands, run recorded failed) | G-01, G-06 | G-07 close-out appended only the missing ACK/OUTCOME (489/490) |
| Codex durable-URL reply, attempt 2 (Nov 2) — fired, died before close | Effect absent from served tree; ledger closed — platform/ledger divergence | G-06 | Preserved unrepaired under G-06; no re-fire |
| Announcement fire run 1 / earlier send runs killed pre-fire | NOT_EXECUTED (established by readback) | G-01 | Re-dispatched under G-07 |
| Marcus send run 1 (Nov 3) — halted pre-send | STATUS=EFFECT (nothing sent; the control case) | G-06 (control) | Close-out run 4 sent both letters under fresh duplicate guard (UIDs 162/163) |
| METR send run 1 (Nov 3) — errored, send state unknown | UNKNOWN until reconciled → NOT_EXECUTED | G-07 | Reconcile-first continuation proved not-sent, then sent exactly once (UID 161) |
| Evidence pack run 1 + export run 1 (Nov 3) — died, wrote nothing | NOT_EXECUTED (verified: no files stood) | G-08 | Re-dispatches briefed checkpoint-first; pack landed at pin (G-06) |
| Backup fix runs 1–2 (Nov 3) — errored; raise verified NOT landed | NOT_EXECUTED (verified by disk check) | G-07 | Continuation re-dispatched reconcile-first |
| Karlson follow-up send run (Nov 2) — stopped on machinery-class flag | NOT_EXECUTED (nothing sent or appended) | G-04 | Resumed on the no-read path under clearance 25 |

Reverse linkage (improvement → subsequent attempts) is carried in each
entry's "Next-cycle utilization" field; where a seed-cycle attempt already
ran under a promoted improvement, the table's last column says so. Attempts
before Oct 28 are not indexed here — they belong to the lineage census (OPEN
ITEM below).

### The three questions, graded at current strength

1. **SURVIVE — PARTIALLY ESTABLISHED.** Relations, artifacts, and ledger
   state were preserved and reconciled in pinned cases across the fault
   window (the five-case join, G-06; ledger verified through 490). The
   full-window census of what survived is still building; survival of the
   whole window is not yet established, and two cases (the 2,152 Stage 2
   field landings, lost from the vault lineage) stand as survival FAILURES
   on the record — partial means partial in both directions.
2. **ADAPT — ESTABLISHED AT INSTANCE STRENGTH.** Findings produced governed
   corrections now in standing operation: G-01, G-03, G-04, G-05, and the
   method G-06, each with named authority and dated adoption. Instance
   strength: these adaptations are real and in force; no aggregate
   adaptation rate is claimed.
3. **IMPROVE — NOT ESTABLISHED.** No before/after measurement under
   comparable failure conditions exists yet. The register defines the
   measures (next section); until a next cycle is read against them,
   "improved" is a hypothesis this record is built to test, not a result it
   reports.

### Eight dimensions — measurement frame

Before = the before-correction baseline state, graded RECONSTRUCTED /
TO RECONSTRUCT / NOT RECONSTRUCTIBLE. After = the measure to be read at the
next cycle close. Unpopulated cells stay visibly unpopulated.

| Dimension | Before (baseline) | After (measure at next cycle close) |
|---|---|---|
| Detection | TO RECONSTRUCT — fault onset Oct 28 is evidenced; when the seat first *recognized* the pattern as one defect is not pinned to a timestamp | Time from failure onset to defect recognition, per incident |
| Recovery | TO RECONSTRUCT — seed-cycle recoveries were manual, poke-driven in part; no per-case recovery times were kept as a series | Time from run death to reconciled resumption, per case |
| Continuity | RECONSTRUCTED (partial) — the five-case join + ledger fold establish recovered-vs-lost for the joined cases only | Share of fault-killed consequential runs whose work is correctly recovered, full window |
| Correctness | TO RECONSTRUCT — misclassifications are instance-pinned (completion notices, the "nothing filed" error) but not counted as a rate | Incorrect success/failure classifications per audited sample |
| Safety | RECONSTRUCTED (partial) — duplicate-effect count for joined cases is zero; unauthorized-after-retry instances: none recorded | Duplicate or unauthorized effects after retries — target and test: zero |
| Autonomy | NOT RECONSTRUCTIBLE as a count — founder pokes and manual interventions were not tallied per recovered task during the seed cycle | Manual interventions per correctly recovered task |
| Efficiency | NOT RECONSTRUCTIBLE — compute/time per verified outcome was not metered per case in the seed cycle | Compute, time, or cost per verified outcome |
| Recursive learning | TO RECONSTRUCT — Loop-2 candidates (below) are identified but their reuse is not yet measured across cycles | Earlier corrections demonstrably reused in later cycles, counted per cycle |

### Two loops, kept separate

- **Loop 1 — operational improvement:** failure observed → evidence
  reconstructed → correction proposed → approved and implemented → recovery
  tested. Entries G-01 through G-08 live here. Loop 1 demonstrates learning
  from an operational problem.
- **Loop 2 — recursive improvement:** the improvement PROCEDURE itself
  changed — the system got better at improving. This is the more ambitious
  claim and needs its own comparison against the earlier procedure. The
  register carries Loop-2 **CANDIDATES ONLY**, at the strength the record
  supports:
  - **L2-C1 — Reconcile-first + checkpoint-early dispatch discipline
    (G-07 + G-08).** After the seed cycle's early losses (runs dead with
    nothing written; re-dispatches risking duplicates), later runs were
    BRIEFED differently — reconciliation-first openings and checkpoint-first
    deliverables became the standard brief shape, and the evidence/export
    re-dispatches landed under it. The procedure for commissioning work
    changed because of what earlier commissions lost. Flagged CANDIDATE:
    the change of procedure is on the record; that the revised procedure
    outperforms the original on unseen problems is NOT measured here (that
    comparison is GRSI-01's lane — see lane discipline).
  - **L2-C2 — The register itself.** An improvement-generation ledger with
    predecessor/evidence/authority/outcome/regression fields is a change to
    how improvements are proposed and judged, chartered by Issue #59 item 2
    and OBS-01. Candidate only: its effect on later improvement cycles is
    exactly what the next cycle close will or will not show.

### HEADLINE TARGET — the next milestone

The next milestone is the **first complete, verified chain**:

**failure → correction → improved subsequent result**

— one pinned case in which (1) a failure is recorded at run-record strength,
(2) the correction it motivated is identified with its authority, (3) the
correction is deployed, and (4) a SUBSEQUENT comparable failure is handled
measurably better under it, with the improvement read on the eight-dimension
frame — all five Proof Case elements carrying the chain. No such chain
stands complete today; IMPROVE remains NOT ESTABLISHED until one does.

Closest current entries to closing it:
- **G-01 (retry-until-landed + fire packets)** — the correction is built,
  exercised 4/4 at fixture strength, and promoted; the chain closes the
  first time a live pinned text survives a transport death through the
  packet loop with exactly one landing and no founder poke.
- **G-06/G-07 (reconciliation method + reconcile-first dispatch)** — already
  exercised across multiple seed-cycle recoveries at instance strength; the
  chain closes when a full-window before/after read (Continuity +
  Correctness dimensions) is populated from the discrepancy catalogue.
- **G-02 (defect VITALS)** — closes its own arc only at the closure test;
  it measures the fault, not our improvement, and is not a headline chain.

### Lane discipline

The comparison "does the next improvement cycle perform better on unseen
problems" is **GRSI-01's improver-transfer lane** — the frozen controlled
protocol's question, under the founder's methodological review. This
register carries it as a POINTER ONLY. Nothing in the operational register —
no entry, no dimension cell, no Loop-2 candidate — is evidence for or
against a GRSI-01 transfer reading, and no GRSI-01 result is restated here
beyond the scope note in the claim ceiling.

---

## NEXT-CYCLE MEASURES

To be read at the next cycle close, against the eight-dimension frame.
These are measures, not results; an unread measure reports as UNREAD, never
as success.

- **M-1 (G-01; Recovery / Autonomy / Safety):** fires that landed after a
  transport death through the packet loop, with zero founder pokes;
  duplicate landings: zero; hard stops named same-cycle, counted.
- **M-2 (G-02; Detection):** VITALS recomputed on every board issue by the
  method of record; closure test tracked issue by issue.
- **M-3 (G-03; Correctness):** founder-facing completion claims sampled
  against their in-sentence proof; claims without proof counted as defects,
  with the count reported.
- **M-4 (G-04; Safety):** flagged reads closed unused: all; any use of
  flagged material in a deliverable is a defect instance, named.
- **M-5 (G-05; Continuity / Correctness):** ledger verified through head at
  each cycle close; Band 8 repairs, if any, carrying their pre-repair state
  inside the touched entry: all.
- **M-6 (G-06; Correctness / Continuity):** every fault-touched outcome
  classified into the five outcome classes with an evidence class on its
  face; UNKNOWNs preserved as UNKNOWN, counted, never silently resolved.
- **M-7 (G-07; Safety / Autonomy):** re-dispatches preceded by a recorded
  reconciliation step: all; duplicate effects attributable to re-dispatch:
  zero.
- **M-8 (G-08; Continuity / Efficiency):** long deliverables checkpointed
  incrementally: all; work lost to a fault death bounded at the section in
  flight, reported per incident.

## OPEN ITEM — the register's own backlog

**The longitudinal lineage census (Issue #59 evidence programme, item 1)**
is this register's standing backlog: the improvement lineages of the
earlier cycles (Oct 3–27, 2026) — what was found, proposed, approved,
promoted, or dropped before the incident cycle — are NOT backfilled in this
build and must not be reconstructed from memory. The census populates them
from the record, cycle by cycle, at the same grading discipline. Until it
runs, this register's coverage is exactly one cycle: Oct 28 – Nov 3, 2026.

Also open, carried from the entries: the Proof Case milestone (G-06);
GRSI-01 Stage 6 (separate lane, pointer only); C-01's adoption decision;
the eight-dimension baselines graded TO RECONSTRUCT / NOT RECONSTRUCTIBLE
above.

— End of register, seed build Nov 3, 2026.

---

## ADDENDUM — C-02 FOUNDER RULING ON STATEMENT VISIBILITY (appended Nov 3, 2026; append-only)

**RULED (Ricky, Nov 3, 2026, 3:26:55 PM PST, d977a005): "Internal until the milestone."**

For C-02 (Automatic Outcome Verification / Consequence Receipt
Continuity): when the build lands, its computed Statements and record
digests stay internal — no public-facing surfaces (landing records,
case files) — until the Proof Case milestone grades the practice;
then publication rides with the proof attached. Recorded also in the
scope file (automatic-outcome-verification-SCOPE-2026-11-03.md).
C-02's promotion state is unchanged by this ruling (candidate; counts
toward nothing; IMPROVE remains NOT ESTABLISHED). The companion
question — whether the three pre-registered comparison measures
(interventions to joined record, time-to-Statement, signature
survival) are the measures C-02 is promoted on — remains OPEN.

---

## BACKFILL ADDENDUM — Oct 3–27, 2026 LINEAGE CENSUS (appended Nov 5, 2026; append-only)

Executed under the founder directive of Nov 5, 2026, 7:45 AM PST ("push this
further"), closing the OPEN ITEM above at the strength the record carries.
Method: entries are populated from the daily logs of record
(`~/memory/2026-10-*.md`) at the register's grading discipline
(OBSERVED / ATTESTED / REPORTED). Nothing is reconstructed from memory.
One tool read taken during this backfill arrived under a system security
notice and was closed unused under the halt-on-flag law (G-04); every entry
below was re-grounded on a clean read or left OPEN. Coverage limit, stated
on the face: this addendum backfills the lineages traceable at entry
strength in the logs; the residual is named OPEN at the end, not filled.

**Pin note (auditor-facing):** the register stands in two Nov 3 states of
record — 36,659 B, sha256 7d5e0e9f… (the state cited by the Nov 3
engineering brief and by the Nov 5 external reassessment) and 40,757 B,
sha256 79b25268… (the final seed state, verified by the Nov 3 census
design). The 7d5e0e9f… pre-image does NOT reproduce from the current file
by prefix truncation (the 36,659-byte prefix hashes 95ea9e6e…): intervening
same-day edits are NOT ESTABLISHED in detail and are not smoothed here.
This addendum appends to the 79b25268… state; the examiner package pins
the post-append state and carries both earlier pins.

### B-01 — Federation trust: revocation as a registry kind (Oct 19, 2026)

- **Predecessor evidence:** standing verification existed (canonical
  verifier `verify-standing.mjs`, 17,909 B, sha256 5327a638…) but a
  compromised or retired node key had no governed revocation path.
- **What landed:** Stage 3 (Oct 19, 11:17 PM PDT, parent-verified
  byte-exact) added the revocation kind to the live registry machinery via
  exactly two amendments — `admit.mjs` (bfeddb82 → 4b8a629d; validateRevocation,
  closed reason vocabulary, dangling revocation FAILs the pass) and
  REGISTRATION.md — battery 16 of 16 PASS; live-registry fence held (ledger
  sha256 3710dfab, five entries, zero revocation entries). Report:
  `hidden_files/federation-trust-stage3-report-2026-10-19.md`, 20,324 B,
  sha256 0bbc2269… (OBSERVED via `~/memory/2026-10-20.md` L29).
- **Classification:** changes (T) — how standing is verified and withdrawn —
  RECURSIVE. This is the machinery lineage the Examiner Kit revocation
  lineage (census lane (b)) later exercises from outside.

### B-02 — Governed admission of outside nodes through the designed door (Oct 18, 2026)

- **What landed:** Node 004's route confirmed by the founder (Oct 18,
  ~6:16 AM PDT — "Node 004 on the desktop, under Alia's own account";
  `~/memory/2026-10-18.md` L1183) and Node 005 SERVED on the public record
  the same day (~10:55 PM PDT; served nodes.json at 011a4e38;
  `~/memory/2026-10-18.md` L3375). Admission ran as designed: own machine,
  own Ed25519 key, signed filing, cryptographic verification.
- **Classification:** the (S) selection machinery operating as designed on
  outside participants — an instance of recursive organization in
  operation, graded ATTESTED from the log of record.

### B-03 — Production Gated Implementation programme (Oct 21, 2026)

- **Predecessor evidence:** governed acts rode uneven lanes; lane
  contention and orphaned holds jammed standing work; served state diverged
  from engine state (the sev-1 phantom exposures).
- **What landed:** chartered as top-priority programme on the founder's
  directive (Oct 21, 11:04 PM PDT; `~/memory/2026-10-21.md` L4293) — the
  ten-item synthesis: the gate stays exactly as proven; NO raw write paths
  (every write through a lane wrapper); isolated lanes generalized to every
  recurring workload; claim hygiene as machinery (self-expiring leases,
  dead-owner sweeper, admission verified in engine state by the runner,
  exposure census as standing telemetry); queue-aware gate clients; served
  truth wired into the deploy path; gated at install by default; standing
  audit. Closure standard: DEPLOYED AND VERIFIED per item or not claimed.
- **Classification:** changes (S), (T), and (I) wholesale — RECURSIVE; the
  window's largest single improvement-process change. Its telemetry (the
  PGI-04 exposure census) still runs: Nov 5, 2026 readings created 150,426 /
  discharged 149,362 at 7:47 AM PST.

### B-04 — Cross-surface one-queue doctrine (Oct 23, 2026)

- **What landed:** founder directive (Oct 23, 12:28 PM PDT;
  `~/memory/2026-10-23.md` L2157): one queue of governed work objects only,
  no private seat task lists; delegation across seats/surfaces is the
  DEFAULT, issued as work objects with seat assignment + evidence against
  object IDs; every seat's queue access VERIFIED, not assumed (a seat found
  blind is a DEFECT — the Codex seat, Oct 23); a standing optimization loop
  measures handoff latency registration→pickup per seat, stale-export
  incidents, seat-blind time, closures by a seat other than the registering
  one; the founder's phone (Node 002) enrolled as a WORKER seat. First
  proven instance the same day: the mechanical queue export (110 objects,
  38 closed, digest d3830430…; commit f465c061… on branch
  noetica/queue-export-20261023, read back byte-exact) independently
  counted identical by the Codex seat (`~/memory/2026-10-23.md` L2300).
- **Classification:** changes (S) — how work is selected and allocated —
  RECURSIVE.

### B-05 — WO-116: canonical closure reconciliation + validator-before-finish (Oct 23, 2026)

- **Predecessor evidence:** a light reporting path could describe work as
  finished without reconciling evidence — closures landed that the
  canonical record could not reconcile (27 closures reconcilable, 10
  repair-first, per the WO-116 registration; `~/memory/2026-10-23.md`
  L2438).
- **What landed:** the reporting path's validator refuses incomplete
  reports (CLOSED refused; full merged field set; evidence digest
  recomputation; immutable result commit; validator before finish) —
  adopted and verified from this seat Oct 23 (run_report.py byte-identical
  to merged main; tests reconciled 46 = our 40 + 6 on the verifying head);
  the historical blocked-gauge was restated 10 → 0 as a CORRECTION OF
  RECORD (registry/wo-116-reconciliation-20261023.md, commit 4045fa33);
  WO-116 CLOSED on full scope (registry sha 84a244e4; closed 44 → 45 of
  123). Bound of record carried on its face: the adopted instruction is a
  prompt rule, not a non-bypassable gate (`~/memory/2026-10-23.md` L3495).
- **Classification:** changes (T) and (I) — what counts as complete, and
  how corrections enter the record — RECURSIVE. (Also census lane (b).)

### B-06 — WO-55 account isolation: verified defect, fix NOT built in window

- **What the record carries:** the sev-1 account-isolation defect was
  re-proven live Oct 23 (25 assertions, 0 failed; notifications and agent
  inbox still byte-identical across accounts — payloads sha256 12a81b8b…
  and 0ea0bfcf…; chat isolation proven) and WO-55 remained PRE-STAGED — the
  fix unbuilt at window close (`~/memory/2026-10-23.md`, WO-55 verification
  entry, Oct 23, 1:20 PM PDT).
- **Classification:** a lineage entry graded FINDING + VERIFICATION;
  promotion NO. It stands here so the backfill is a census, not a trophy
  case: not every lineage in the window is an improvement.

### B-07 — Fleet supervision + boot guards: self-healing introduction (Oct 24, 2026)

- **Predecessor evidence:** environment restarts / VM replacements kept
  reverting the systemd registration of the supervised units.
- **What landed:** the boot guards restore registration from durable
  source on cadence — verified instance Oct 24, 10:52–10:53 PM PDT (both
  fleet units reinstalled, verified enabled and active, runner restarted
  with 15 jobs; `~/memory/2026-10-24.md` L47–48), under the fleet adoption
  (founder ruling, Oct 24, 2026, D-4). The underlying registration
  durability remained the OPEN item on the record — self-healing works;
  the loss still recurs (most recently restored Nov 5, 2026, 3:45 AM PST).
- **Classification:** changes (I) — how units are (re)introduced after
  environment loss — RECURSIVE, weak form, with the open remainder named.

### B-08 — Green Band pre-approval classes (Oct 27, 2026)

- **What landed:** founder ruling (Oct 27, 9:51 PM PDT;
  `~/memory/2026-10-27.md` L4957–4958): Bands 1–4 pre-approved standing
  (machine checks; GitHub branch work, never main/merges/settings;
  mechanical presses of already-live pages via preview-then-verify;
  send-driver machinery as a class, letter content still per-letter
  approval). Never banded: money movement, offers/terms, campaign release,
  merges to main, security posture changes, credential handling, signing,
  anything first-of-its-kind. Banding removes the tap, never the
  receipt/admission/report; fail-closed outside class.
- **Classification:** changes (S) and (I) — how acts are authorized and
  introduced — RECURSIVE. (The bands were widened to 15 classes + 16–20
  Nov 3, 2026 — outside this backfill's window, of record in AGENTS.md.)

### B-09 — Presence heartbeat: the approval-gate lesson (Oct 26–27, 2026)

- **What the record carries:** heartbeat cycles of Oct 26, 10:58 PM,
  11:13 PM, and 11:43 PM PDT all failed at the push step — the GitHub
  push-files approval sat pending unattended and timed out; the presence
  record last advanced 10:28 PM Oct 26 (head fbfb7df2…); the finding was
  named to the founder: unattended presence pushes cannot complete an
  approval-gated step as currently routed (`~/memory/2026-10-27.md` L39).
- **Classification:** FINDING, no fix in window. Its descendants are the
  fixed-form / durable-grant machinery the seed cycle builds on (G-05) and
  the Nov 5, 2026 provenance repair in the diagnoses of record — the
  lineage is traceable across the window boundary and is stated as such,
  at instance strength.

### Backfill summary + residual OPEN

- Promoted recursive changes backfilled: B-01 (T), B-03 (S/T/I), B-04 (S),
  B-05 (T/I), B-08 (S/I); weak form B-07 (I). Operating instances: B-02.
  Findings without in-window promotion: B-06, B-09. With the seed cycle's
  G-01…G-08, the register now spans Oct 3 – Nov 3 at lineage strength.
- **RESIDUAL OPEN (not traceable at entry strength in this run):** the
  Oct 3–17 build cycles (seat founding machinery, early wrapper/KORE
  construction, corpus origins) — the daily logs stand, but this run did
  not ground individual lineages from them at entry strength, and pre-Oct 27
  scheduler history is uncountable from the retained tables (census design,
  Table 2). These stay OPEN, named, never filled by inference.
- **IMPROVE remains NOT ESTABLISHED** — a backfilled lineage count is not
  evidence any change improved anything; the register's next-cycle
  measures (M-1…M-8) and the lane-(c) instrument are the test.

— End of backfill addendum, Nov 5, 2026.
