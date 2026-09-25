# Week 02: Measurement design

**Learning target.** By the end, a learner can explain measurement design, apply it to the CampusAssist case, and defend the evidence in **pre-registered evaluation plan**.

**Before class (60–90 min).** Read the linked publisher overviews and the [case dossier](../../../shared/case-campusassist.md). Write two questions about the evidence you would need to approve the scenario. Required links are free; publisher pages for ISO standards are optional background.

## Reading and standards anchors

- [EVAL_DRAFT: AI 800-2, Towards Best Practices for Automated Benchmark Evaluations](https://www.nist.gov/news-events/news/2026/01/towards-best-practices-automated-benchmark-evaluations) — Explicitly label as draft in class
- [EVAL_STATS: AI 800-3, Expanding the AI Evaluation Toolbox with Statistical Models](https://www.nist.gov/publications/expanding-ai-evaluation-toolbox-statistical-models) — Measurement assumptions and uncertainty
- [ARIA: Assessing Risks and Impacts of AI (ARIA)](https://ai-challenges.nist.gov/aria) — Model, red-team and field levels

## Teach the concepts

### 1. Concept, decision and evidence

Define target construct, unit of analysis, sampling frame and error costs before selecting metrics. Locate this concept in the system workflow: who makes the decision, whose opportunity changes, and what record would verify the account?

### 2. Competing interpretation and limit

Estimate uncertainty and beware repeated tuning on the test set. Ask which plausible competing explanation could produce the same observation. State the sample, role or jurisdiction that limits any conclusion.

### 3. Operational test and owner

Compare offline benchmark, expert red team and real-world field study for distinct questions. Convert the concept into a test or review action with an owner, deadline and observable pass/fail or decision criterion.

## Worked case

The vendor sampled only successful students for validation. **Instructor model:** Sampling only successful students excludes the very cases in which missed support matters. Define a prospective sampling frame before the vendor tunes a threshold. On the board, distinguish **observed fact**, **assumption**, **potential harm**, **control**, and **unanswered question**. Ask the room for one reason a reasonable reviewer might disagree with the model reasoning. Use the source anchors to identify a relevant outcome without claiming a framework automatically approves the system.

## 150-minute lesson plan

1. **0–10 min — diagnostic:** students state the system boundary and a likely affected person.
2. **10–45 min — mini-lesson:** explain the three concepts above and connect each to a case decision.
3. **45–65 min — worked example:** unpack the case fact, identify who can challenge the decision and what evidence is missing.
4. **65–75 min — break.**
5. **75–115 min — studio:** Repair a flawed study protocol with stratification and a holdout. Have each team record one rejected alternative and why.
6. **115–135 min — cross-team review:** trade artifacts; reviewers check assumptions, source fit, affected parties and feasibility.
7. **135–150 min — individual exit check:** submit pre-registered evaluation plan and a 100-word defense of the most uncertain claim.

## Student studio instructions

Submit **Pre-registered evaluation plan**. Include a purpose and scope statement; a small table of claims, evidence, owners and limitations; at least one affected-person perspective; and a test or review date. Where numbers are used, show the denominator. Where the question is legal, label jurisdiction and effective date. Cite at least two reading links from above. The case is fictional; do not use real student information.

## 75-minute supervised extension

In a scheduled studio or supervised online session, spend 20 minutes gathering the linked publisher evidence, 35 minutes revising **pre-registered evaluation plan** against a peer's challenge, and 20 minutes writing an individual note that identifies which claim changed, what evidence caused the change, and the next verification step. The instructor records attendance/engagement under local policy. This extension supplies the additional structured contact time in the suggested 12-week, 3-credit format.

## Facilitator cues and assessment

- Probe the misconception: **“More decimal places make an invalid measure more valid.”** Request a counterexample grounded in the scenario.
- Strong submission: specific facts and assumptions are separated, at least one plausible alternative is tested, a named actor owns the next step, and the conclusion is appropriately limited.
- Developing submission: lists framework names without tying them to a decision or evidence.
- Extension: change one case fact (vendor role, data source, user population or deployment scale); ask which conclusion must change and which remains robust.

## Slide deck

Use the editable [Week 02 deck](../slides/week-02.md); speaker prompts are also in slide comments.
