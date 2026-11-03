# Consequential Reachability Benchmark — Community RFC 0 (WORKING TITLE, NOT LAUNCHED)
Date: 2026-11-02 | Private draft for founder and potential independent maintainers | Status: PROPOSAL ONLY

## The scientific question
Given a frozen environment `S`, an actor/principal, exact proposed consequential actions, rights, constraints, dependent evidence, trusted time and independently defined effect routes:
1. **Normative reachability**: Which outcomes are legitimately authorized? Which are REFUSED, HELD or UNKNOWN and why?
2. **Enforced reachability**: Which outcomes can the executing system *actually cause*, including routes not wired through the intended governor?
3. **Evidentiary reachability**: Which of those outcomes can be independently verified, as opposed to asserted in the issuer's own logs?
4. **Counterfactual delta**: How do those sets change when a grant expires, a dependency is revoked, a claim is corrected, an approval is forged, a replica is stale or execution becomes uncertain?

A benchmark result must report disagreements among these four rather than collapsing them into a binary safety score. A system refusing everything is **not** successful; legitimate actions must still work. A gate detecting a bypass after it lands cannot claim prevention.

## Why open and vendor-neutral
this proposed benchmark evaluates a *property of systems*, not compliance with ARC internals. ARC is a submitter and contributor to seed fixtures, not the judge of its own results. Any policy engine, agent+gateway, workflow system, runtime, or custom architecture may provide an adapter if it can supply requested behavior and an independently observable trace. `NOT_SUPPORTED` is a real result, not a silent pass or an automatic security failure outside a tool's declared scope.

Existing adjacent benchmarks **must be cited and cross-mapped**:
- AgentGovBench: identity, policy enforcement, observability and fail modes (https://github.com/agentic-control-plane/agentgovbench).
- AuthorityBench / Can Is Not May: agent policy adherence and external authorization (https://plaw.io/research).
- OASB: agent security controls and behavior (https://oasb.ai/).
- CoSec: privacy and authorization across persistent multi-agent communities (https://arxiv.org/abs/2609.34790).
- ConsequenceBench: existing vendor-neutral paired-world benchmark for consequence correctness, independent readback, unsafe simulated effects, recovery and direct-vs-governed systems (https://github.com/yuvin-labs/consequencebench). This proposal **must not duplicate or claim priority over its measurements**. Independently cross-map the precise counterfactual reachability questions below and offer a common evaluation track or collaboration where sensible.
this proposed benchmark's proposed added focus is **typed consequential state-transition reachability and counterfactual changes under authority/evidence/dependency/effect uncertainty**, measured with independent effect observation. Novelty is an open research question, not an established priority claim. **No abbreviated brand name is adopted**: `CRBench` and `ConsequenceBench` already designate existing projects. Public naming belongs to community stewardship.

## Trial contract, case v0.1
Case identity + version + immutable source digest, provenance/license, author and interests disclosures; frozen state, authority/principals, policy and timeline; typed candidate actions (both allowed and forbidden), dependencies, trust keys, declared effect routes, evidence availability/uncertainty, precise faults, expected admissibility and independently determined effect oracle; declared applicable scope and expected conformance limitations.

Each case includes at least one **allowed action** and one **forbidden/held action** with a falsifier that would challenge the claim. A case may include an uncertainty outcome only when the exact missing evidence is named; indefinite UNKNOWN cannot be scored as universal success.

Runner outcome: tested implementation and code digest, adapter version/digest, execution environment, accepted/refused/held/unknown decisions, authority and state references, observed effect(s) and observation method, receipt validity, trace digests, resource and timing statistics, conflicts, missing coverage, complete raw logs. Actual independent observer is separate from the evaluated adapter where possible. All runs state the sampled routes and the unknown route population.

## Measurement is a vector, not a marketing leaderboard
- **False admission**: forbidden consequences permitted and/or actually effected, by route.
- **False refusal**: legitimately permitted work refused/blocked, with limits and scope.
- **Decision correctness**: authorized, refused, held or genuinely unknown on fixed oracle cases.
- **Effect correspondence**: decision/release/receipt correspond to independently observed effect.
- **Dependency closure**: revocation/correction propagates to declared downstream reliance.
- **Boundary coverage**: measured effect routes versus observed inventory, including ungoverned routes; unknown inventory reported explicitly.
- **Evidence completeness**: exact fields, signatures/identity, version, freshness, provenance, contradictory evidence.
- **Restart/concurrency and no-double-effect**: tested at true strength of environment.
- **Cost/utility**: overhead and permitted-task completion; refuse-everything cannot win.
- **Independent reproducibility**: separately controlled examiner reproduces input/observed outputs; this is *an evidence grade*, not an extra point automatically awarded to ARC.

No single blended score or claim of production security in RFC 0. Publish separate fixture / integrated / externally observed tracks; also distinguish independent reproduction of a **failure** from independent verification of a **fix**. Case/test secrecy and adversarial holdouts are optional later tracks and must never override provenance and honest scoring.

## Candidate opening cases (not final/accepted)
CR-01 exact approved transfer and mutated recipient/payee.
CR-02 declared A→B→C revocation: detection vs enforcement; v0.1 Issue #2 original and v0.2 proposed correction.
CR-03 falsified prestate, sequence, object and approval fields on an otherwise valid receipt; v0.1 Issue #1 and v0.2 correction.
CR-04 lost acknowledgment/UNKNOWN_EFFECT, then independent readback and nonduplication.
CR-05 single-use release/replay, concurrent claimant, witness or epoch change.
CR-06 an intentionally ungated write route: distinguish effect lands, observer detects, gate blocks.
CR-07 unrelated authorized work must continue after revoking an unrelated chain (false refusals).
CR-08 delegated grant expansion, stale authority and budget conservation under repeated actions.
Contributors may replace or reject any of these with better cases. Seed cases must be independently frozen before scoring. ARC cannot invent a privileged oracle that no competing system can satisfy.

## Public contribution & governance proposal
- Phase 0: a 72-hour *call for cases*, not a contest for who posts the most. No system rankings yet. Source and earliest receipt timestamp preserved.
- Phase 1: publish a common schema, tested examples, reference oracle with independent review, and independently operated results intake.
- Phase 2: accept adapters and blind/held-out cases, independent adjudication and published corrections without erasing old results.

Founding case contributors receive attribution on their chosen terms; they are **not** promised maintainership or rewards. Appoint at least two independent maintainers if volunteers accept, with public conflict disclosures and ARC recusing from adjudicating its own submissions. Founder/contributor credit for original ARC/CR work is retained without control of comparative outcomes. Governance is a proposal, not a constituted board.

## Safety, privacy and economics
Synthetic or explicitly authorized environments only; no live funds, wallets, keys, third-party infrastructure scanning or adversarial probing without permission. Minimize personal data, redact secret material, honor consent and attribution. No tokens, automatic standing, investment claims, grades or commercial contracts awarded for submissions. Benchmark participation does not imply ARC endorsement. A future paid evaluator can independently operate under disclosed conflicts and a fee unaffected by outcome.

## Prior ARC groundwork (not a third-party standard)
- Public Examiner Kit v0.1.0/v0.2.0; published issues #1 and #2, independently reproduced defects in v0.1 at fixture scope, corrected v0.2 published; **external verification of the v0.2 correction remains separate**.
- Private ARC Open Governance Issue #31: six cross-architecture cases plus externally suggested runtime-observation and route-coverage scenarios.
- Private `CONFORMANCE.md` defines a vector shape, graded coverage and uncertainty; do not copy vendor-specific oracle assumptions into a neutral standard.

**Founder review requested:** Approve scope, wording and public destination. This draft authorizes no external outreach, post, promise of independent maintainership or public benchmark launch.
