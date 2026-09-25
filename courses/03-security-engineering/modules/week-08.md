# Week 08: Model and software supply chain

**Learning target.** By the end, a learner can explain model and software supply chain, apply it to the CampusAssist case, and defend the evidence in **supply-chain acceptance checklist and change gate**.

**Before class (60–90 min).** Read the linked publisher overviews and the [case dossier](../../../shared/case-campusassist.md). Write two questions about the evidence you would need to approve the scenario. Required links are free; publisher pages for ISO standards are optional background.

## Reading and standards anchors

- [SSDF: SP 800-218, Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) — Secure development activities
- [SSDF_AI: SP 800-218A, Secure Development Practices for Generative AI and Dual-Use Foundation Models](https://csrc.nist.gov/pubs/sp/800/218/a/final) — AI-specific SSDF profile
- [ISO27001: ISO/IEC 27001:2022, Information security management](https://www.iso.org/standard/27001) — ISMS assurance

## Teach the concepts

### 1. Concept, decision and evidence

Record model origin, licenses, hashes, dependencies, signed artifacts and change approval. Locate this concept in the system workflow: who makes the decision, whose opportunity changes, and what record would verify the account?

### 2. Competing interpretation and limit

Review risks in third-party weights, packages and hosted inference terms. Ask which plausible competing explanation could produce the same observation. State the sample, role or jurisdiction that limits any conclusion.

### 3. Operational test and owner

Apply secure development practices and staged promotion with rollback. Convert the concept into a test or review action with an owner, deadline and observable pass/fail or decision criterion.

## Worked case

The vendor silently swaps the model after an audit. **Instructor model:** A SOC report on cloud hosting does not identify model weights or training provenance. Request a model version and change-control evidence. On the board, distinguish **observed fact**, **assumption**, **potential harm**, **control**, and **unanswered question**. Ask the room for one reason a reasonable reviewer might disagree with the model reasoning. Use the source anchors to identify a relevant outcome without claiming a framework automatically approves the system.

## 150-minute lesson plan

1. **0–10 min — diagnostic:** students state the system boundary and a likely affected person.
2. **10–45 min — mini-lesson:** explain the three concepts above and connect each to a case decision.
3. **45–65 min — worked example:** unpack the case fact, identify who can challenge the decision and what evidence is missing.
4. **65–75 min — break.**
5. **75–115 min — studio:** Build an SBOM-like inventory and provenance checklist. Have each team record one rejected alternative and why.
6. **115–135 min — cross-team review:** trade artifacts; reviewers check assumptions, source fit, affected parties and feasibility.
7. **135–150 min — individual exit check:** submit supply-chain acceptance checklist and change gate and a 100-word defense of the most uncertain claim.

## Student studio instructions

Submit **Supply-chain acceptance checklist and change gate**. Include a purpose and scope statement; a small table of claims, evidence, owners and limitations; at least one affected-person perspective; and a test or review date. Where numbers are used, show the denominator. Where the question is legal, label jurisdiction and effective date. Cite at least two reading links from above. The case is fictional; do not use real student information.

## 75-minute supervised extension

In a scheduled studio or supervised online session, spend 20 minutes gathering the linked publisher evidence, 35 minutes revising **supply-chain acceptance checklist and change gate** against a peer's challenge, and 20 minutes writing an individual note that identifies which claim changed, what evidence caused the change, and the next verification step. The instructor records attendance/engagement under local policy. This extension supplies the additional structured contact time in the suggested 12-week, 3-credit format.

## Facilitator cues and assessment

- Probe the misconception: **“A vendor’s SOC report automatically covers its model behavior.”** Request a counterexample grounded in the scenario.
- Strong submission: specific facts and assumptions are separated, at least one plausible alternative is tested, a named actor owns the next step, and the conclusion is appropriately limited.
- Developing submission: lists framework names without tying them to a decision or evidence.
- Extension: change one case fact (vendor role, data source, user population or deployment scale); ask which conclusion must change and which remains robust.

## Slide deck

Use the editable [Week 08 deck](../slides/week-08.md); speaker prompts are also in slide comments.
