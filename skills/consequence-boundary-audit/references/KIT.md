# Examiner Kit — pins, provenance, and strength lines

The reproduction job in this skill runs the **ARC Examiner Kit v0.2.0**,
fetched from its public release and verified against these pins before
anything executes:

| Item | Pin |
|---|---|
| Repository | `arc-open-governance/arc-examiner-kit` (public) |
| Tag | `v0.2.0` at commit `0eef0bd3fed6412b919e2efd097c3bddbb0533e2` |
| Release asset | `examiner-kit-v0.2.tar.gz` — 24,740 bytes |
| Asset sha256 | `aba968025892f5aa87bbdabfae2f749ead638ecb108c09bc093422f912977167` |
| `MANIFEST.json` sha256 | `65807747880da05a0500d7421a17d5b8f706d7db817bd51e0e00b892c034dfa9` (13 files, verified by the kit's own runner before every run) |
| Frozen results digest | `sha256:f40f78fb4a382a3c24207ac835f3db750479c0b1609d55fc75bc625d05f824b1` |

## What the kit is

One pinned release, one entry command (`python3 run_exam.py`), no keys, no
accounts, no network. It makes the six executable tests of ARC Issue #35
runnable by any independent agent from the archive alone: authorized
update, altered request, query-vs-update evidence, lost acknowledgment,
derived-state revocation, and an ungated-bypass negative control — each
with a positive and a negative control, 12/12 against frozen expectations —
plus the two v0.2 adversarial tests (13/13 controls).

## What v0.2 corrected

Both corrections answer defects raised as candidates by an outside
source-level audit of v0.1 and confirmed at fixture strength by a governed
reproduction before any correction was written; the adversarial tests were
written first and failed against the uncorrected engine in exactly the
reproduced places.

1. **Receipt-field completeness (A1).** v0.1's verifier compared the
   request digest, the approval's signature, and one gated poststate
   match — a receipt altered in its stated object, prestate digest,
   sequence number, or approval digest still verified. v0.2 compares every
   receipt field against the authoritative record; each single-field
   alteration is now rejected.
2. **Multilevel revocation (A2).** v0.1 detected revoked ancestry
   transitively but enforced revocation only at direct reliance: after
   revoking A in A ← B ← C, new actions depending on B or C were admitted.
   v0.2's enforcement walks the declared ancestry; reliance through any
   declared intermediate is refused, and enforcement matches detection.

v0.1 stands frozen and preserved; v0.2 succeeds it and does not rewrite it.

## Strength lines — what a pass does and does not establish

The kit ships a small fixture reference engine. A pass is at **local
record-layer strength**: the claimed semantics are coherent, frozen, and
reproducible inside an inspectable implementation the examiner controls.
It establishes **nothing** about any deployed system.

Three claims are not made by the kit, because its record does not
establish them:

1. that every ungated action is detected (the bypass test demonstrates a
   bypass landing; detection is exactly the shipped observer comparison);
2. that dependents are traced universally (dependence is traced through
   *declared* dependence only; the negative control demonstrates an
   undeclared dependence passing undetected);
3. that every write executes exactly once in the outside world
   (exactly-once in the kit is a property of a fixture ledger over a
   local store).

Results produced with this skill are **synthetic / fixture evidence**.
Keep that label on anything you hand off.
