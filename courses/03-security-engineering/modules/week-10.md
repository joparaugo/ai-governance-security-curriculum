# Week 10: Security requirements and verification

**Learning target.** By the end, a learner can explain security requirements and verification, apply it to the CampusAssist case, and defend the evidence in **control verification matrix with test ids**.

**Before class (60–90 min).** Read the linked publisher overviews and the [case dossier](../../../shared/case-campusassist.md). Write two questions about the evidence you would need to approve the scenario. Required links are free; publisher pages for ISO standards are optional background.

## Reading and standards anchors

- [AISVS: Artificial Intelligence Security Verification Standard 1.0](https://owasp.org/projects/artificial-intelligence-security-verification-standard-aisvs-docs) — Select verifiable requirements by assurance level
- [ASVS: Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) — Conventional application controls
- [SP53: SP 800-53 Rev. 5, Security and Privacy Controls](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — Tailor controls; no automatic AI compliance claim

## Teach the concepts

### 1. Concept, decision and evidence

Select concrete, testable AISVS requirements plus ordinary ASVS requirements for surrounding apps. Locate this concept in the system workflow: who makes the decision, whose opportunity changes, and what record would verify the account?

### 2. Competing interpretation and limit

For each control state owner, implementation evidence and negative test. Ask which plausible competing explanation could produce the same observation. State the sample, role or jurisdiction that limits any conclusion.

### 3. Operational test and owner

Use CSF 2.0 for program outcomes and SP 800-53 for tailored controls. Convert the concept into a test or review action with an owner, deadline and observable pass/fail or decision criterion.

## Worked case

The team lists “secure AI” as a control with no pass criterion. **Instructor model:** Replace “secure AI” with a test such as “an unassigned advisor cannot retrieve a private note by direct API call,” including expected deny and log evidence. On the board, distinguish **observed fact**, **assumption**, **potential harm**, **control**, and **unanswered question**. Ask the room for one reason a reasonable reviewer might disagree with the model reasoning. Use the source anchors to identify a relevant outcome without claiming a framework automatically approves the system.

## 150-minute lesson plan

1. **0–10 min — diagnostic:** students state the system boundary and a likely affected person.
2. **10–45 min — mini-lesson:** explain the three concepts above and connect each to a case decision.
3. **45–65 min — worked example:** unpack the case fact, identify who can challenge the decision and what evidence is missing.
4. **65–75 min — break.**
5. **75–115 min — studio:** Turn five vague controls into pass/fail statements. Have each team record one rejected alternative and why.
6. **115–135 min — cross-team review:** trade artifacts; reviewers check assumptions, source fit, affected parties and feasibility.
7. **135–150 min — individual exit check:** submit control verification matrix with test ids and a 100-word defense of the most uncertain claim.

## Student studio instructions

Submit **Control verification matrix with test IDs**. Include a purpose and scope statement; a small table of claims, evidence, owners and limitations; at least one affected-person perspective; and a test or review date. Where numbers are used, show the denominator. Where the question is legal, label jurisdiction and effective date. Cite at least two reading links from above. The case is fictional; do not use real student information.

## 75-minute supervised extension

In a scheduled studio or supervised online session, spend 20 minutes gathering the linked publisher evidence, 35 minutes revising **control verification matrix with test ids** against a peer's challenge, and 20 minutes writing an individual note that identifies which claim changed, what evidence caused the change, and the next verification step. The instructor records attendance/engagement under local policy. This extension supplies the additional structured contact time in the suggested 12-week, 3-credit format.

## Facilitator cues and assessment

- Probe the misconception: **“Mapping to a control catalog means the control is operating.”** Request a counterexample grounded in the scenario.
- Strong submission: specific facts and assumptions are separated, at least one plausible alternative is tested, a named actor owns the next step, and the conclusion is appropriately limited.
- Developing submission: lists framework names without tying them to a decision or evidence.
- Extension: change one case fact (vendor role, data source, user population or deployment scale); ask which conclusion must change and which remains robust.

## Slide deck

Use the editable [Week 10 deck](../slides/week-10.md); speaker prompts are also in slide comments.
