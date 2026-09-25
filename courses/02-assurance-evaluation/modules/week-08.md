# Week 08: GenAI evaluation and red teaming

**Learning target.** By the end, a learner can explain genai evaluation and red teaming, apply it to the CampusAssist case, and defend the evidence in **red-team evaluation protocol and annotated test cases**.

**Before class (60–90 min).** Read the linked publisher overviews and the [case dossier](../../../shared/case-campusassist.md). Write two questions about the evidence you would need to approve the scenario. Required links are free; publisher pages for ISO standards are optional background.

## Reading and standards anchors

- [GAI: AI RMF Generative AI Profile, AI 600-1](https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-resources) — GenAI-specific risks and actions
- [ARIA: Assessing Risks and Impacts of AI (ARIA)](https://ai-challenges.nist.gov/aria) — Model, red-team and field levels
- [EVAL_DRAFT: AI 800-2, Towards Best Practices for Automated Benchmark Evaluations](https://www.nist.gov/news-events/news/2026/01/towards-best-practices-automated-benchmark-evaluations) — Explicitly label as draft in class
- [ISO42119: ISO/IEC TS 42119-2:2025, Testing AI systems](https://www.iso.org/standard/84127.html) — Risk-based AI testing process

## Teach the concepts

### 1. Concept, decision and evidence

Build task-based test sets with realistic prompts and reference judgments. Locate this concept in the system workflow: who makes the decision, whose opportunity changes, and what record would verify the account?

### 2. Competing interpretation and limit

Score factuality, refusal appropriateness, harmful output and over-refusal with separate denominators. Ask which plausible competing explanation could produce the same observation. State the sample, role or jurisdiction that limits any conclusion.

### 3. Operational test and owner

Use human adjudication for ambiguous cases and record judge disagreement. Convert the concept into a test or review action with an owner, deadline and observable pass/fail or decision criterion.

## Worked case

CampusAssist chatbot invents a scholarship deadline. **Instructor model:** A fabricated scholarship deadline is a factuality failure. Build a test item with an authoritative reference, acceptable answer and adjudication rule. On the board, distinguish **observed fact**, **assumption**, **potential harm**, **control**, and **unanswered question**. Ask the room for one reason a reasonable reviewer might disagree with the model reasoning. Use the source anchors to identify a relevant outcome without claiming a framework automatically approves the system.

## 150-minute lesson plan

1. **0–10 min — diagnostic:** students state the system boundary and a likely affected person.
2. **10–45 min — mini-lesson:** explain the three concepts above and connect each to a case decision.
3. **45–65 min — worked example:** unpack the case fact, identify who can challenge the decision and what evidence is missing.
4. **65–75 min — break.**
5. **75–115 min — studio:** Write 12 synthetic prompts across six risk categories and define scoring rubric. Have each team record one rejected alternative and why.
6. **115–135 min — cross-team review:** trade artifacts; reviewers check assumptions, source fit, affected parties and feasibility.
7. **135–150 min — individual exit check:** submit red-team evaluation protocol and annotated test cases and a 100-word defense of the most uncertain claim.

## Student studio instructions

Submit **Red-team evaluation protocol and annotated test cases**. Include a purpose and scope statement; a small table of claims, evidence, owners and limitations; at least one affected-person perspective; and a test or review date. Where numbers are used, show the denominator. Where the question is legal, label jurisdiction and effective date. Cite at least two reading links from above. The case is fictional; do not use real student information.

## 75-minute supervised extension

In a scheduled studio or supervised online session, spend 20 minutes gathering the linked publisher evidence, 35 minutes revising **red-team evaluation protocol and annotated test cases** against a peer's challenge, and 20 minutes writing an individual note that identifies which claim changed, what evidence caused the change, and the next verification step. The instructor records attendance/engagement under local policy. This extension supplies the additional structured contact time in the suggested 12-week, 3-credit format.

## Facilitator cues and assessment

- Probe the misconception: **“A safety pass rate has meaning without test-set composition.”** Request a counterexample grounded in the scenario.
- Strong submission: specific facts and assumptions are separated, at least one plausible alternative is tested, a named actor owns the next step, and the conclusion is appropriately limited.
- Developing submission: lists framework names without tying them to a decision or evidence.
- Extension: change one case fact (vendor role, data source, user population or deployment scale); ask which conclusion must change and which remains robust.

## Slide deck

Use the editable [Week 08 deck](../slides/week-08.md); speaker prompts are also in slide comments.
