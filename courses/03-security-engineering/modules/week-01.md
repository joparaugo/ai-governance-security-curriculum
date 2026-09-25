# Week 01: AI architecture and assets

**Learning target.** By the end, a learner can explain ai architecture and assets, apply it to the CampusAssist case, and defend the evidence in **architecture diagram and asset inventory**.

**Before class (60–90 min).** Read the linked publisher overviews and the [case dossier](../../../shared/case-campusassist.md). Write two questions about the evidence you would need to approve the scenario. Required links are free; publisher pages for ISO standards are optional background.

## Reading and standards anchors

- [ISO23053: ISO/IEC 23053:2022, ML AI system framework](https://www.iso.org/standard/74438.html) — System component boundaries
- [SSDF_AI: SP 800-218A, Secure Development Practices for Generative AI and Dual-Use Foundation Models](https://csrc.nist.gov/pubs/sp/800/218/a/final) — AI-specific SSDF profile
- [CSF: Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) — Govern plus Identify, Protect, Detect, Respond, Recover

## Teach the concepts

### 1. Concept, decision and evidence

Map data, training, model registry, retrieval index, application, tools, users and logs. Locate this concept in the system workflow: who makes the decision, whose opportunity changes, and what record would verify the account?

### 2. Competing interpretation and limit

Identify trust boundaries and privileged actions before cataloging vulnerabilities. Ask which plausible competing explanation could produce the same observation. State the sample, role or jurisdiction that limits any conclusion.

### 3. Operational test and owner

Separate model safety behavior from infrastructure confidentiality and availability. Convert the concept into a test or review action with an owner, deadline and observable pass/fail or decision criterion.

## Worked case

CampusAssist has an external model API, internal record store and email tool. **Instructor model:** The external model API, internal records, public retrieval and email tool create separate trust boundaries. Map who can invoke each action. On the board, distinguish **observed fact**, **assumption**, **potential harm**, **control**, and **unanswered question**. Ask the room for one reason a reasonable reviewer might disagree with the model reasoning. Use the source anchors to identify a relevant outcome without claiming a framework automatically approves the system.

## 150-minute lesson plan

1. **0–10 min — diagnostic:** students state the system boundary and a likely affected person.
2. **10–45 min — mini-lesson:** explain the three concepts above and connect each to a case decision.
3. **45–65 min — worked example:** unpack the case fact, identify who can challenge the decision and what evidence is missing.
4. **65–75 min — break.**
5. **75–115 min — studio:** Draw data and control flows; mark three trust boundaries. Have each team record one rejected alternative and why.
6. **115–135 min — cross-team review:** trade artifacts; reviewers check assumptions, source fit, affected parties and feasibility.
7. **135–150 min — individual exit check:** submit architecture diagram and asset inventory and a 100-word defense of the most uncertain claim.

## Student studio instructions

Submit **Architecture diagram and asset inventory**. Include a purpose and scope statement; a small table of claims, evidence, owners and limitations; at least one affected-person perspective; and a test or review date. Where numbers are used, show the denominator. Where the question is legal, label jurisdiction and effective date. Cite at least two reading links from above. The case is fictional; do not use real student information.

## 75-minute supervised extension

In a scheduled studio or supervised online session, spend 20 minutes gathering the linked publisher evidence, 35 minutes revising **architecture diagram and asset inventory** against a peer's challenge, and 20 minutes writing an individual note that identifies which claim changed, what evidence caused the change, and the next verification step. The instructor records attendance/engagement under local policy. This extension supplies the additional structured contact time in the suggested 12-week, 3-credit format.

## Facilitator cues and assessment

- Probe the misconception: **“The model itself is the only important asset.”** Request a counterexample grounded in the scenario.
- Strong submission: specific facts and assumptions are separated, at least one plausible alternative is tested, a named actor owns the next step, and the conclusion is appropriately limited.
- Developing submission: lists framework names without tying them to a decision or evidence.
- Extension: change one case fact (vendor role, data source, user population or deployment scale); ask which conclusion must change and which remains robust.

## Slide deck

Use the editable [Week 01 deck](../slides/week-01.md); speaker prompts are also in slide comments.
