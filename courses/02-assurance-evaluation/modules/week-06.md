# Week 06: Robustness, drift and distribution shift

**Learning target.** By the end, a learner can explain robustness, drift and distribution shift, apply it to the CampusAssist case, and defend the evidence in **robustness test plan and monitoring trigger**.

**Before class (60–90 min).** Read the linked publisher overviews and the [case dossier](../../../shared/case-campusassist.md). Write two questions about the evidence you would need to approve the scenario. Required links are free; publisher pages for ISO standards are optional background.

## Reading and standards anchors

- [ISO25059: ISO/IEC 25059:2023, Quality model for AI systems](https://www.iso.org/standard/80655.html) — Specify quality requirements
- [ISO24029: ISO/IEC TR 24029-1:2021, Neural-network robustness overview](https://www.iso.org/standard/77609.html) — Robustness assessment
- [MONITOR: AI 800-4, Challenges to the Monitoring of Deployed AI Systems](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-4.pdf) — Postdeployment monitoring limitations
- [AML: AI 100-2e2025, Adversarial ML Taxonomy](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) — Attacker goals, knowledge, life-cycle stages

## Teach the concepts

### 1. Concept, decision and evidence

Distinguish input perturbation, environmental change, data drift and performance drift. Locate this concept in the system workflow: who makes the decision, whose opportunity changes, and what record would verify the account?

### 2. Competing interpretation and limit

Test plausible shifts tied to known deployment conditions and failure costs. Ask which plausible competing explanation could produce the same observation. State the sample, role or jurisdiction that limits any conclusion.

### 3. Operational test and owner

Specify drift alert thresholds, investigation and rollback rather than automatic retraining. Convert the concept into a test or review action with an owner, deadline and observable pass/fail or decision criterion.

## Worked case

A new aid policy changes which students receive support. **Instructor model:** A policy change can alter the meaning of “support need” even if input distributions look similar. Name an outcome review and an owner before proposing retraining. On the board, distinguish **observed fact**, **assumption**, **potential harm**, **control**, and **unanswered question**. Ask the room for one reason a reasonable reviewer might disagree with the model reasoning. Use the source anchors to identify a relevant outcome without claiming a framework automatically approves the system.

## 150-minute lesson plan

1. **0–10 min — diagnostic:** students state the system boundary and a likely affected person.
2. **10–45 min — mini-lesson:** explain the three concepts above and connect each to a case decision.
3. **45–65 min — worked example:** unpack the case fact, identify who can challenge the decision and what evidence is missing.
4. **65–75 min — break.**
5. **75–115 min — studio:** Design three shift tests and an investigation runbook. Have each team record one rejected alternative and why.
6. **115–135 min — cross-team review:** trade artifacts; reviewers check assumptions, source fit, affected parties and feasibility.
7. **135–150 min — individual exit check:** submit robustness test plan and monitoring trigger and a 100-word defense of the most uncertain claim.

## Student studio instructions

Submit **Robustness test plan and monitoring trigger**. Include a purpose and scope statement; a small table of claims, evidence, owners and limitations; at least one affected-person perspective; and a test or review date. Where numbers are used, show the denominator. Where the question is legal, label jurisdiction and effective date. Cite at least two reading links from above. The case is fictional; do not use real student information.

## 75-minute supervised extension

In a scheduled studio or supervised online session, spend 20 minutes gathering the linked publisher evidence, 35 minutes revising **robustness test plan and monitoring trigger** against a peer's challenge, and 20 minutes writing an individual note that identifies which claim changed, what evidence caused the change, and the next verification step. The instructor records attendance/engagement under local policy. This extension supplies the additional structured contact time in the suggested 12-week, 3-credit format.

## Facilitator cues and assessment

- Probe the misconception: **“Retraining is always the right response to drift.”** Request a counterexample grounded in the scenario.
- Strong submission: specific facts and assumptions are separated, at least one plausible alternative is tested, a named actor owns the next step, and the conclusion is appropriately limited.
- Developing submission: lists framework names without tying them to a decision or evidence.
- Extension: change one case fact (vendor role, data source, user population or deployment scale); ask which conclusion must change and which remains robust.

## Slide deck

Use the editable [Week 06 deck](../slides/week-06.md); speaker prompts are also in slide comments.
