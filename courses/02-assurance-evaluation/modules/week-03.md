# Week 03: Dataset provenance and quality

**Learning target.** By the end, a learner can explain dataset provenance and quality, apply it to the CampusAssist case, and defend the evidence in **dataset card and quality remediation list**.

**Before class (60–90 min).** Read the linked publisher overviews and the [case dossier](../../../shared/case-campusassist.md). Write two questions about the evidence you would need to approve the scenario. Required links are free; publisher pages for ISO standards are optional background.

## Reading and standards anchors

- [ISO5259: ISO/IEC 5259-1:2024, Data quality for analytics and ML](https://www.iso.org/standard/81088.html) — Data quality scope and measures
- [ISO5259_2: ISO/IEC 5259-2:2024, Data quality model and measures](https://www.iso.org/standard/81860.html) — Specify and report dataset quality measures
- [ISO5259_4: ISO/IEC 5259-4:2024, Data quality process framework](https://www.iso.org/standard/81093.html) — Lifecycle and labeling processes
- [ISO5338: ISO/IEC 5338:2023, AI system life cycle processes](https://www.iso.org/standard/81118.html) — Lifecycle artifacts and transitions
- [PRIV: Privacy Framework 1.0](https://www.nist.gov/privacy-framework) — Do not label 1.1 final until NIST does

- [SPDX_AI: SPDX AI profile and AI bill of materials](https://spdx.dev/learn/areas-of-interest/ai/) — Trace model, dataset and software component dependencies; do not conflate SPDX 3.x with ISO/IEC 5962:2021.

## Teach the concepts

### 1. Concept, decision and evidence

Trace source, collection permission, transformations, label generation, missingness and dataset versions. Locate this concept in the system workflow: who makes the decision, whose opportunity changes, and what record would verify the account?

### 2. Competing interpretation and limit

Analyze representativeness and construct validity, not just duplicate and null counts. Ask which plausible competing explanation could produce the same observation. State the sample, role or jurisdiction that limits any conclusion.

### 3. Operational test and owner

Set retention and access rules for data and training artifacts. Convert the concept into a test or review action with an owner, deadline and observable pass/fail or decision criterion.

### Additional official source exercise

Draft a minimal model/data/software dependency record and explain how a changed dataset or package would be traced to a specific evaluation version.

**Observable evidence:** AI component provenance and impact row.

## Worked case

The “missed support” label comes from advisor notes written inconsistently. **Instructor model:** Advisor notes may encode who previously received attention rather than who needed it. Provenance documentation should identify the label rule, author and missingness. On the board, distinguish **observed fact**, **assumption**, **potential harm**, **control**, and **unanswered question**. Ask the room for one reason a reasonable reviewer might disagree with the model reasoning. Use the source anchors to identify a relevant outcome without claiming a framework automatically approves the system.

## 150-minute lesson plan

1. **0–10 min — diagnostic:** students state the system boundary and a likely affected person.
2. **10–45 min — mini-lesson:** explain the three concepts above and connect each to a case decision.
3. **45–65 min — worked example:** unpack the case fact, identify who can challenge the decision and what evidence is missing.
4. **65–75 min — break.**
5. **75–115 min — studio:** Create a dataset card and find three provenance gaps. Have each team record one rejected alternative and why.
6. **115–135 min — cross-team review:** trade artifacts; reviewers check assumptions, source fit, affected parties and feasibility.
7. **135–150 min — individual exit check:** submit dataset card and quality remediation list and a 100-word defense of the most uncertain claim.

## Student studio instructions

Submit **Dataset card and quality remediation list**. Include a purpose and scope statement; a small table of claims, evidence, owners and limitations; at least one affected-person perspective; and a test or review date. Where numbers are used, show the denominator. Where the question is legal, label jurisdiction and effective date. Cite at least two reading links from above. The case is fictional; do not use real student information.

**Additional source check.** AI component provenance and impact row. Explain why the source does or does not fit the CampusAssist system and cite its official page.

## 75-minute supervised extension

In a scheduled studio or supervised online session, spend 20 minutes gathering the linked publisher evidence, 35 minutes revising **dataset card and quality remediation list** against a peer's challenge, and 20 minutes writing an individual note that identifies which claim changed, what evidence caused the change, and the next verification step. The instructor records attendance/engagement under local policy. This extension supplies the additional structured contact time in the suggested 12-week, 3-credit format.

## Facilitator cues and assessment

- Probe the misconception: **“A clean spreadsheet guarantees valid labels.”** Request a counterexample grounded in the scenario.
- Strong submission: specific facts and assumptions are separated, at least one plausible alternative is tested, a named actor owns the next step, and the conclusion is appropriately limited.
- Developing submission: lists framework names without tying them to a decision or evidence.
- Extension: change one case fact (vendor role, data source, user population or deployment scale); ask which conclusion must change and which remains robust.

## Slide deck

Use the editable [Week 03 deck](../slides/week-03.md); speaker prompts are also in slide comments.
