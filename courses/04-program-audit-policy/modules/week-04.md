# Week 04: Procurement and third-party risk

**Learning target.** By the end, a learner can explain procurement and third-party risk, apply it to the CampusAssist case, and defend the evidence in **vendor due diligence pack and decision recommendation**.

**Before class (60–90 min).** Read the first three publisher overviews and the [case dossier](../../../shared/case-campusassist.md); skim additional comparison sources according to the studio task. Write two questions about the evidence you would need to approve the scenario. Required links are free; publisher pages for ISO standards are optional background.

## Reading and standards anchors

- [AICM: AI Controls Matrix v1.1](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1) — Cloud AI control evidence
- [SSDF_AI: SP 800-218A, Secure Development Practices for Generative AI and Dual-Use Foundation Models](https://csrc.nist.gov/pubs/sp/800/218/a/final) — AI-specific SSDF profile
- [ISO27001: ISO/IEC 27001:2022, Information security management](https://www.iso.org/standard/27001) — ISMS assurance

**Additional publisher references:** skim the links relevant to this week’s studio; use free overviews where complete standards require purchase.

- [CSA_CAIQ: STAR Level 1 Security Questionnaire (CAIQ v4.1)](https://cloudsecurityalliance.org/artifacts/star-level-1-security-questionnaire-caiq-v4-1) — Collect provider control assertions and evidence; use STAR-submittable version.
- [CSA_AI_CAIQ: AI-CAIQ in the AICM v1.1 resource bundle](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1) — Assess AI-specific supplier claims; STAR for AI submission formats can differ by date.
- [CSA_STAR: STAR cloud assurance program and registry](https://cloudsecurityalliance.org/star) — Distinguish self-assessment, third-party assurance and scope.
- [CSA_STAR_AI: STAR for AI program](https://cloudsecurityalliance.org/star/ai) — Compare AI self-assessment with independent certification and its stated scope.
- [NIST_SCRM: SP 800-161 Rev. 1 update 1, Cybersecurity Supply Chain Risk Management](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final) — Evaluate model, dataset, component and service supplier risk.
- [ISO27017: ISO/IEC 27017:2026, Cloud Security Controls](https://www.iso.org/standard/27017) — Cloud service provider and customer controls.
- [ISO27018: ISO/IEC 27018:2025, Public Cloud PII Protection](https://www.iso.org/standard/27018) — Public-cloud PII processor considerations; clarify legal and contractual role.
- [SOC2: SOC 2 and Trust Services Criteria resources](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2) — Read report period, service boundary, criteria, exceptions and user controls; never infer model assurance.

## Teach the concepts

### 1. Concept, decision and evidence

Collect model provenance, training/data terms, subprocessors, evaluation reports, audit rights and exit terms. Locate this concept in the system workflow: who makes the decision, whose opportunity changes, and what record would verify the account?

### 2. Competing interpretation and limit

Assign responsibilities for incidents, model changes, notification and data deletion. Ask which plausible competing explanation could produce the same observation. State the sample, role or jurisdiction that limits any conclusion.

### 3. Operational test and owner

Test vendor claims with sample evidence rather than only questionnaires. Convert the concept into a test or review action with an owner, deadline and observable pass/fail or decision criterion.

### Applied comparison: new governance and security sources

Issue separate CAIQ cloud and AI-CAIQ AI questions. Evaluate STAR/STAR for AI declarations, any SOC 2 scope and the vendor's model-update rights. Mark unanswered items; assign provider/customer ownership and a contractual remedy.

**Observable evidence:** Supplier assurance grid with claims, scope, period, exceptions, owners and decision.

## Worked case

Vendor refuses evaluation access and permits unilateral model updates. **Instructor model:** Unilateral model updates undermine prior tests. Ask for notice, regression evidence, rollback rights and responsibility for notification. On the board, distinguish **observed fact**, **assumption**, **potential harm**, **control**, and **unanswered question**. Ask the room for one reason a reasonable reviewer might disagree with the model reasoning. Use the source anchors to identify a relevant outcome without claiming a framework automatically approves the system.

## 150-minute lesson plan

1. **0–10 min — diagnostic:** students state the system boundary and a likely affected person.
2. **10–45 min — mini-lesson:** explain the three concepts above and connect each to a case decision.
3. **45–65 min — worked example:** unpack the case fact, identify who can challenge the decision and what evidence is missing.
4. **65–75 min — break.**
5. **75–115 min — studio:** Negotiate a redlined contract term sheet and assurance request. Have each team record one rejected alternative and why.
6. **115–135 min — cross-team review:** trade artifacts; reviewers check assumptions, source fit, affected parties and feasibility.
7. **135–150 min — individual exit check:** submit vendor due diligence pack and decision recommendation and a 100-word defense of the most uncertain claim.

## Student studio instructions

Submit **Vendor due diligence pack and decision recommendation**. Include a purpose and scope statement; a small table of claims, evidence, owners and limitations; at least one affected-person perspective; and a test or review date. Where numbers are used, show the denominator. Where the question is legal, label jurisdiction and effective date. Cite at least two reading links from above. The case is fictional; do not use real student information.

**Source-application check.** Supplier assurance grid with claims, scope, period, exceptions, owners and decision. Cite the relevant primary publisher pages above, specify source scope and status, and do not claim that a questionnaire answer or technique label proves effectiveness.

## 75-minute supervised extension

In a scheduled studio or supervised online session, spend 20 minutes gathering the linked publisher evidence, 35 minutes revising **vendor due diligence pack and decision recommendation** against a peer's challenge, and 20 minutes writing an individual note that identifies which claim changed, what evidence caused the change, and the next verification step. The instructor records attendance/engagement under local policy. This extension supplies the additional structured contact time in the suggested 12-week, 3-credit format.

## Facilitator cues and assessment

- Probe the misconception: **“The vendor alone owns all deployment risk.”** Request a counterexample grounded in the scenario.
- Strong submission: specific facts and assumptions are separated, at least one plausible alternative is tested, a named actor owns the next step, and the conclusion is appropriately limited.
- Developing submission: lists framework names without tying them to a decision or evidence.
- Extension: change one case fact (vendor role, data source, user population or deployment scale); ask which conclusion must change and which remains robust.

## Slide deck

Use the editable [Week 04 deck](../slides/week-04.md); speaker prompts are also in slide comments.
