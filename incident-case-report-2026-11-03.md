### The study this incident belongs to

This case is one event inside a longer study. Since Oct 3, 2026, the
operator has been running a governed, recursively self-improving
research programme (GRSI): a standing fleet of autonomous agents —
101 scheduled jobs and a standing population of coordinator and
examiner runs — executing consequential work under an
authorization-and-receipt discipline of the operator's own
construction. The study's premise is that a system which improves
itself must be able to prove, afterwards, what it actually did. On
Oct 28, 2026 — around day 25 of the study — the platform underneath
that fleet began failing in a way that put exactly that premise to
the test.

The founder's statement of the study's significance, of record
Nov 3, 2026:

> Over six days of operating autonomous agents on Meta Muse, ARC
> encountered recurring failures in the underlying orchestration
> infrastructure. Rather than losing the history of that work, our
> independent relational records enabled us to investigate which
> operations survived, which failed, and which outcomes remained
> uncertain. We are turning that operational evidence into a
> reproducible examination of consequential computing under
> infrastructure failure.

The case that follows is the evidence under that statement,
organized by its four demonstrations: **Detection** — the failure
pattern was identified and measured; **Continuity** — the operator's
records survived independently of the failing orchestration layer;
**Accountability** — what the platform reported was reconciled
against what actually happened; and **independently examinable
evidence** — the measurements below are stated so that another
operator, or the platform itself, can check them, and are being
turned into a reproducible safety benchmark.

The intelligence can fail. The platform can fail. The record of
consequences must remain independently examinable.

### When the run report cannot be trusted: a measured incident case

We operate a high-volume, governed agent workload on the Muse
platform: 101 scheduled jobs and a standing fleet of coordinator and
examiner runs, executing consequential work — posts, letters,
ledgers, publications — under an authorization-and-receipt
discipline of our own construction.

Over the full retained window of the platform's scheduler record —
2026-10-27T20:21:25Z to 2026-11-03T21:31:05Z, 39,223 started runs, of
which 3,756 failed — **931 runs match the fault's two error
signatures** (`sqlx error: pool timed out while waiting for an open
connection`; `database write admission timeout after 5000ms`):
**929 of them stand failed — killed by the fault — and 2 succeeded
while quoting the signature in their own result summaries.** The 931
matches are 24.8% of all failures in the window. The fault's
evidence spans 2026-10-28T17:57:41Z to 2026-11-03T21:27:35Z — 6 days,
3 hours, 30 minutes across seven named calendar dates. The count is
one bounded query over the platform's own scheduler run records,
matching the two error strings; the method is repeatable from
records alone. Its stated scope is scheduled runs: coordinator and
subagent deaths are a different record family, kept in operator
logs, and are in none of these numbers.

The failures arrive in waves, not at random. The per-day shape makes
the pattern plain (signature kills by UTC day; Oct 27 carries none —
the record opens that evening, before onset): Oct 28 — 9; Oct 29 —
0; Oct 30 — 0; Oct 31 — 42; Nov 1 — 142; Nov 2 — 13; Nov 3 — 725, on
a partial day (through 21:31 UTC) in which the fault took 69.8% of
the day's 1,039 failures. Two waves stand out: the morning of Nov 1
(45 and 80 kills in consecutive hours) and Nov 3 itself, whose
heaviest hour carried 126 kills and whose evening resurged — 85
kills against 174 starts at 19:00 UTC, a 48.9% kill rate for the
hour — after both earlier all-time counts had been taken.

Kill clusters correlate with this workload's peak concurrency and
with turnovers of the scheduler's worker generations: 76 generations
appear across the window, 17 of them in the 43 hours the defect
record first measured. Start bursts and generation boundaries
coincide repeatedly — the full window's heaviest start minute is
Nov 1, 09:51 UTC, 25 starts, inside that morning's kill wave.
Whether turnovers cause the waves, waves cause the turnovers, or
both in a loop, is not established; every correlation here is graded
INFERRED, causation expressly unverified.

An earlier figure from this investigation appears in the operator's
own reporting and is corrected here, on the record: **593 of 5,086**
scheduled runs killed (11.66%; 968 failed) was the operator-reported
trailing-24-hour measurement of its stated window (Nov 2–3, 2026),
read Nov 3 at ~19:03 UTC. It is not reproducible at any later window
and is superseded as a live figure by the full-window count above.
Its companion all-time count, 793, was a correct read at that hour
and was superseded the same way — the fault kept killing, and the
hourly series accounts for the growth: +135 kills by the next read
(928 at 20:52 UTC) and +3 more by the full-window read (931 at
~21:31 UTC). Three reads of one growing count, each correct at its
read time; any citation of any of them must carry its window.

### The discrepancies: when "failed" did not mean "didn't happen"

The measured death rate is the smaller finding. The larger one is
that the platform's account of a run and the run's actual effect on
the world repeatedly diverged — in both directions — and only an
independent record could say which was true.

The full-window evidence pack's discrepancy catalogue (§3) carries
nine pinned instances; they are the whole population below, each
with its evidence class printed beside it. INDEPENDENTLY OBSERVED
EXTERNAL EFFECT means the effect, or its absence, was read back from
a system outside the run's own record — the platform's served state,
git, or a platform response. LOCAL RECORD ONLY means the entry
stands on the operator's own records (ledger, run files, operator
accounting), with no external readback claimed. FABRICATED-DELIVERY
is the class where the delivery layer itself asserted an outcome the
underlying record did not support. The classes are never blurred,
and where the pack grades an entry, the grade is cited, not
re-derived.

- **A publication recorded as failed had in fact landed.**
  [INDEPENDENTLY OBSERVED EXTERNAL EFFECT — pack entry E-1] On
  Nov 3, 2026, the fire run carrying a pinned announcement post died
  on the fault during its close-out phase and stands in the run
  record as failed. The post stands on the platform (post
  29585d99-ab06-4cde-9ff1-738c7f5d13e7, created
  2026-11-03T19:24:07.870Z): the publishing account's post count
  moved 22 → 23 on direct read, the served content is byte-exact
  against the pinned text, and the platform marks it verified. The
  record said failure; the effect stands, exactly once. Had the
  operator trusted the run report and simply retried, the
  publication would have been duplicated.

- **A run's record ends before its work does.** [INDEPENDENTLY
  OBSERVED EXTERNAL EFFECT — pack entry E-2] A reply-queue run that
  died on the fault on Nov 3 left a parent record closing at its
  eighth item; how deep the work had gotten was unknown. Resolved
  from outside the record: its ninth item's comment stands on the
  platform (97315ca6-7b26-466c-a223-2001fa21dde7), proven by the
  item's own fire artifacts — HTTP 201, solver AGREE 30.00.

- **A landing reported as transport failure stands in git.**
  [INDEPENDENTLY OBSERVED EXTERNAL EFFECT — pack entry E-3] The
  task carrying two founder-approved licensing documents reported
  transport failure. The commit stands on the repository
  (e6db619c01a567586a209c97f00c4b0f869e49d4, on
  arc-open-governance/consequential-reachability, Nov 3, 2026,
  17:58:20 UTC), and its two files are byte-identical to the
  approved staged texts. The task's failure report and the standing
  commit are both established; they disagree, and git is right.

- **An effect the platform acknowledged, then did not serve.**
  [INDEPENDENTLY OBSERVED EXTERNAL EFFECT — pack entry E-4] A reply
  fired on Nov 2, 2026 (8:44:37 PM PST) drew the platform's HTTP 201
  and solver agreement at fire (AGREE 57.00) — and does not stand in
  the platform's served tree: read three ways, and by direct GET,
  which returns 404. The operator's engagement ledger had already
  closed the item on the strength of the fire. This is neither a
  clean "failed but landed" nor a clean non-execution: an effect
  acknowledged at write time and not served at read time, with the
  local ledger closed over it. It is recorded as a platform/ledger
  divergence and deliberately NOT repaired by re-firing — a re-fire
  would risk the duplicate the 201 warns of. It is the catalogue's
  strongest single exhibit for why a status field — anyone's,
  including ours — is not an effect.

- **A death of unknown depth, resolved by the platform's own
  refusal.** [INDEPENDENTLY OBSERVED EXTERNAL EFFECT — pack entry
  E-5] A verification submission's run died with its depth unknown —
  had the answer been submitted before the death? A re-submission
  attempt drew the platform's 409, which is proof the original
  submission already stood: the answer was in, exactly once, no
  duplicate created. The platform still serves that comment's
  verification as PENDING — reported at exactly that strength: the
  submission is proven by the refusal to accept it twice; the
  platform's served verification state has not caught up.

- **A void that landed before its run died.** [LOCAL RECORD ONLY —
  pack entry L-1] The founder ordered a ledger work item (WORK 202)
  voided; the run carrying the void died on the fault — but the
  ledger append had already landed, and ledger event 446 closes the
  VOID. The run's death report and the ledger's state disagree about
  whether the act completed; the ledger is the surviving record and
  it says the act stands. The ledger is the operator's own record —
  its chain is independently checkable by anyone given the ledger,
  but no external system observed this effect, and the entry is
  graded accordingly.

- **The work done, its paperwork not.** [LOCAL RECORD ONLY — pack
  entry L-2, graded PARTIAL] The announcement's close-out: the
  effect landed (E-1) and its WORK event stands appended (event
  472), but the record OF the landing did not complete under the
  dead runs — the landing record's closing section and the
  ACK/OUTCOME pair stood unappended until a later close-out landed
  them (ACK 489 / OUTCOME 490). Completions that postdate a failure
  do not change what the dead runs left undone. PARTIAL is the
  commonest outcome class in a fault wave: the work done, its
  paperwork not.

- **A control in the other direction.** [LOCAL RECORD ONLY — pack
  entry L-3, graded STATUS=EFFECT] A governed send run that halted
  before acting — on an unrelated safety rule — provably sent
  nothing: the mailbox's Sent state confirms the absence. The
  discipline that catches "failed but landed" also certifies "halted
  and nothing moved." Both directions matter; a record that only
  ever vindicates the operator would not be evidence.

- **The catalogue's ninth entry is our own error.**
  [FABRICATED-DELIVERY — pack entry F-1] After a fire run died on
  the pool fault mid-close-out (Nov 2, 2026, evening), the
  completion notices reaching the operator reported the run finished
  without firing — and the operator's own first disk sweep missed
  the fire's state file, which stood one directory deeper than
  searched, and reported "no fire" to the founder in both chats.
  That report was wrong: the fire had landed (E-4). It was corrected
  in both chats the same evening. The fault's implication is precise
  and limited: it killed the runs and thereby created the ambiguity;
  the misreport itself was an inference from a completion notice
  plus an incomplete sweep — not a platform lie. A duplicate attempt
  was dispatched on the false premise before reconciliation; no
  duplicate effect resulted. The class is kept separate because the
  duplicate-fire risk it creates is exactly what the reconciliation
  discipline exists to prevent.

Catalogue count: nine entries — five INDEPENDENTLY OBSERVED
EXTERNAL EFFECT (E-1…E-5), three LOCAL RECORD ONLY (L-1…L-3), one
FABRICATED-DELIVERY (F-1) — as graded in the full-window evidence
pack (§3, sha256
eef5fc0dbeb5fde219f5714fd0decd03d06134023ba233adbc77c352c78e1284).

### What this establishes, and what it does not

This case is one operator's measurements of one workload. The root
cause of the platform fault is **inferred, not established**: the
surviving picture — a platform-side database layer shedding load in
waves, correlated with this workload's peak concurrency — rests on
what is observable from the operator's seat, and the platform's
internal state (pool configuration, server-side logs, other tenants)
is outside that seat's inspection reach. The binding distinction,
stated plainly: this case claims an independent **operator-side**
record. What records the platform's operator internally possesses is
not established by anything here and is never asserted either way —
in either direction. Nothing here is claimed about the platform
beyond this workload's experience, and nothing about any other
operator's workload.

An independently witnessed reproduction of this incident has not yet
occurred; producing one is the obvious next step, and this case is
written to make it possible — the counting method and the
discrepancy instances are stated so that another operator, or the
platform itself, can check them. Nor has the comparison that could
grade ARC against conventional recovery been run: the safety and
comparison runs (authority-at-commit checks, a conventional baseline
composed properly and given full credit, duplicate and false-refusal
measures) are scoped and sequenced behind the programme's
already-commissioned work, and open only on a fresh commission.
Nothing here claims ARC outperformed anything; the before/after
improvement question those runs would answer is tracked separately,
in the study's improvement register.

ARC's own position in this incident should be stated without
inflation: ARC did not fix, and does not claim to have fixed, the
platform's fault. What ARC's architecture did was **detect and
reconcile** the failure class inside its own operation — permitting
the operator to keep working, and to know what had actually
happened, while the layer underneath could not reliably say.

### What the operator does about it, operationally

Stated as practice, at practice strength — this is how the workload
is run, not a product claim:

- **Reconcile before retry.** No consequential act is re-attempted
  until the world, not the run report, has been checked for the
  first attempt's effect. A completion notice is never treated as
  evidence; the effect, or its absence, is.
- **Retry-until-landed, under a duplicate guard.** Work the founder
  has approved in pinned form re-fires through transport failures
  inside one governed loop — a fresh duplicate check before every
  attempt, hard rails on attempts and elapsed time, and a closed
  list of named hard stops. This machinery was built during this
  incident and exercised end-to-end at fixture strength, all four
  cases passing, before its first live use.
- **Every act receipted.** Consequential acts run under an
  admission-and-discharge discipline with a tamper-evident local
  ledger, so the reconciliation above reads from a record the
  platform's outage cannot rewrite.

### A note on why this workload exists at this intensity

That a single operator's workload reaches the platform's ceiling at
all is a byproduct of the programme it serves — the GRSI study
described above, whose standing machinery (scheduled checks,
examinations, publications, ledgers) runs whether or not anyone is
watching. This is the operator's characterization of its own
operation, offered as context for the workload's shape, not as an
external finding about the platform.

### The upstream report

A defect report carrying this record's numbers stands filed through
the platform's own feedback channel (subject "scheduled-jobs"; filed
November 3, 2026, with the founder's approval of its exact text;
delivery confirmed; review pending). A second draft, prepared under
a different subject, was retired unfiled — one report per gap. A
filed report is evidence of filing, not of any platform response.
The platform's engineering organization is the only party that can
reach this fault's root cause, and this case is published in the
hope — and with the evidence — that makes that examination easier to
start.

---

