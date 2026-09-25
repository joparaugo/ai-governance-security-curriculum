# Lab 5: CSA cloud and AI supplier assurance

**Use:** Course 4 weeks 4 and 8; Course 3 weeks 1 and 12. **Time:** 80 minutes. **Materials:** the [fictional case](../shared/case-campusassist.md), [vendor worksheet](../templates/vendor-due-diligence.md), [control evidence worksheet](../templates/control-evidence-matrix.csv), [assurance scope note](../templates/assurance-scope-note.md). No account or paid standard is required.

## Official source anchors

- [CSA CCM and CAIQ v4.1](https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4-1): cloud security controls, responsibility and supplier questions.
- [CSA AICM v1.1 and AI-CAIQ](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1): AI-specific objectives and supplier assertions.
- [CSA STAR cloud](https://cloudsecurityalliance.org/star) and [STAR for AI](https://cloudsecurityalliance.org/star/ai): compare declared and independently assessed scope.
- [AICPA SOC 2 resources](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2): examine coverage and report period, rather than accepting a brochure claim.
- [NIST SP 800-161](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final): supplier and update risks. [IIA Three Lines](https://www.theiia.org/en/standards/documents/): decision and independent review roles.

## Fictional inject (read aloud)

Northstar answers a CAIQ excerpt with “yes, access restricted” and attaches a two-year-old architecture diagram. Its AI-CAIQ excerpt says “model changes are logged,” without an owner or a customer notification commitment. Marketing says “SOC 2 Type 2 and STAR compliant”; the team has neither the scoped report nor a current STAR entry. The proposed contract still permits unilateral updates and indefinite log retention.

## Student instructions

1. **10 minutes — split the system.** Name cloud hosting, AI model, campus data and customer application boundaries. Assign the provider and customer to each risk.
2. **20 minutes — classify claims.** Ask two CCM/CAIQ cloud questions and two AICM/AI-CAIQ questions. For each, record the claim, requested artifact, period, owner, plausible exception and control test. Use your own words; do not copy publisher control text.
3. **15 minutes — test assurance labels.** For STAR, STAR for AI and SOC 2, record whether the asserted assurance exists in the packet, its actual system boundary, period and assurance type. Use **unknown** where no evidence was supplied. A vendor's self-assessment is not an independent audit.
4. **20 minutes — make the decision.** Draft a conditional procurement recommendation with a notice/rollback term, customer tool-authorization responsibility, retention limit and a stop trigger. Assign first-line and second-line owners, plus an independent audit challenge.
5. **15 minutes — peer review.** Swap worksheets. The reviewer must name one unsupported assertion, one missing control owner and one next evidence request.

**Submit:** completed [control evidence worksheet](../templates/control-evidence-matrix.csv) and a one-page [scope note](../templates/assurance-scope-note.md). This is a fictional exercise, not a STAR application or SOC 2 attestation.

## Instructor key and rubric

**Indicative answer:** The hosting diagram can support an architecture description only; it does not establish current operation. A CAIQ “yes” needs IAM configuration and a current access-test sample. The AI-CAIQ answer needs model version log, notice records and regression reports. No provided item substantiates the brochure's current SOC 2 or STAR claims. HSU owns its advisor access, retrieval policy and tool authorization even if Northstar hosts the model. Defer or condition contracting until scope and change-control evidence is supplied.

**Score (100):** boundary/owner separation 20; correctly distinguished cloud and AI questions 20; testable evidence and dates 25; assurance-scope limits 20; feasible decision, dissent and escalation 15. Alternative risk treatments earn full credit when supported by the packet and stated uncertainty.
