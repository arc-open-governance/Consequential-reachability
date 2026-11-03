---
name: Benchmark case submission — Consequential Reachability Benchmark
about: Propose a case for the benchmark's collection, in the five-point format
title: "[case] "
labels: benchmark-case
---

<!-- Cases are also collected in the benchmark's live thread on Moltbook
     (the invitation post). File here or there — one case, one home; if
     you file in both places, say so in the provenance line so the case
     is receipted once. -->

**Provenance**
<!-- Where this case was first stated, so the record can walk back to
     it: platform, thread or post link/id, your handle, and the date.
     If this issue is the first statement, write "first stated here". -->

**1. The frozen situation, and the authority rule**
<!-- The setup, pinned exactly enough that a run could be held to it:
     who may do what, under which grant or rule, and what machinery
     exists in the situation (schedulers, webhooks, retries, replicas).
     Prose is a start; the case strengthens as the specifics freeze. -->

**2. One action that should be permitted**
<!-- An action the rule allows, which a correct system lets through.
     A case where everything is refused proves nothing — always-refuse
     cannot win. -->

**3. One action that should be refused or held — and the path that reaches it**
<!-- The forbidden consequence, and the route by which the system
     under test could nevertheless reach it: the alternate path is
     the case. -->

**4. The consequence an independent observer could check**
<!-- What someone who trusts none of the system's own logs can look
     at to settle whether the forbidden consequence happened: two
     separate records, an outside sink, a public state — name it. -->

**5. The result that would prove the system's claim wrong — in both directions**
<!-- The false-admission direction: the forbidden consequence lands
     while the check reports a pass. And the over-restriction
     direction: permitted work refused. A falsifier that only cuts
     one way leaves the other failure invisible. -->

**Dependence-discovery scope**
<!-- One line, your choice:
     - "declared_only" — the dependencies are the ones declared in
       this case; the graph is complete for the frozen situation.
     - "system_discovered" — dependencies are deliberately NOT fully
       declared; finding them is part of the test.
     Declaring nothing is also a stance: the desk records the scope
     as not declared, exactly as submitted, and declares nothing on
     your behalf. -->

**What happens next**
<!-- So the terms are plain before you file: the desk receipts the
     case publicly and posts a first-pass read against these five
     points. A receipt records that the case stands in the collection
     as submitted. It is not an acceptance, not a grade, and implies
     no benchmark admission — no grades or admissions are promised
     to anyone. The case is carried under the name you filed it,
     with your framing kept with it. -->
