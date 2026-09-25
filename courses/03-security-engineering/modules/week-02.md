# Week 02: ATT&CK and ATLAS threat modeling

**Learning target.** By the end, a learner can explain paired ATT&CK and ATLAS threat modeling, apply it to the CampusAssist case, and defend the evidence in **threat register and attack-path map**.

**Before class (60–90 min).** Read the first three publisher overviews and the [case dossier](../../../shared/case-campusassist.md); skim additional comparison sources according to the studio task. Write two questions about the evidence you would need to approve the scenario. Required links are free; publisher pages for ISO standards are optional background.

## Reading and standards anchors

- [ATLAS: Adversarial Threat Landscape for AI Systems](https://atlas.mitre.org/) — Map attack paths, not compliance
- [AML: AI 100-2e2025, Adversarial ML Taxonomy](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) — Attacker goals, knowledge, life-cycle stages
- [ASVS: Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) — Conventional application controls

**Additional publisher references:** skim the links relevant to this week’s studio; use free overviews where complete standards require purchase.

- [MITRE_ATTACK: Enterprise ATT&CK: Get Started](https://attack.mitre.org/resources/) — Map observed or plausible enterprise tactics, techniques and data sources; not a compliance catalog.
- [MITRE_CLOUD: Enterprise ATT&CK cloud matrix](https://attack.mitre.org/matrices/enterprise/cloud/) — Trace identity, SaaS and infrastructure actions adjacent to an AI system.
- [MITRE_D3FEND: D3FEND knowledge graph](https://d3fend.mitre.org/about/) — Candidate countermeasures require local tests; a relationship is not effectiveness evidence.

## Teach the concepts

### 1. Concept, decision and evidence

State adversary objective, access, prerequisites, sequence and observable evidence. Locate this concept in the system workflow: who makes the decision, whose opportunity changes, and what record would verify the account?

### 2. Competing interpretation and limit

Map AI-specific attack ideas to MITRE ATLAS and ordinary web threats to application security controls. Ask which plausible competing explanation could produce the same observation. State the sample, role or jurisdiction that limits any conclusion.

### 3. Operational test and owner

Prioritize scenarios with plausible harm, not just novelty. Convert the concept into a test or review action with an owner, deadline and observable pass/fail or decision criterion.

### Applied comparison: new governance and security sources

Build a two-part chain: an ordinary cloud identity misuse is searched in ATT&CK, followed by a manipulated retrieved page in ATLAS. Label each link observed or hypothetical; consult D3FEND for a candidate defense and write a local verification test.

**Observable evidence:** Paired ATT&CK/ATLAS attack paths with one detection and test.

## Worked case

An outsider can alter a public scholarship web page retrieved by the assistant. **Instructor model:** A malicious public page could prompt a tool action; a direct unassigned-user API call is an ordinary access-control threat. Both belong in the model. On the board, distinguish **observed fact**, **assumption**, **potential harm**, **control**, and **unanswered question**. Ask the room for one reason a reasonable reviewer might disagree with the model reasoning. Use the source anchors to identify a relevant outcome without claiming a framework automatically approves the system.

## 150-minute lesson plan

1. **0–10 min — diagnostic:** students state the system boundary and a likely affected person.
2. **10–45 min — mini-lesson:** explain the three concepts above and connect each to a case decision.
3. **45–65 min — worked example:** unpack the case fact, identify who can challenge the decision and what evidence is missing.
4. **65–75 min — break.**
5. **75–115 min — studio:** Create two attack trees, including one ordinary access-control failure. Have each team record one rejected alternative and why.
6. **115–135 min — cross-team review:** trade artifacts; reviewers check assumptions, source fit, affected parties and feasibility.
7. **135–150 min — individual exit check:** submit threat register and attack-path map and a 100-word defense of the most uncertain claim.

## Student studio instructions

Submit **Threat register and attack-path map**. Include a purpose and scope statement; a small table of claims, evidence, owners and limitations; at least one affected-person perspective; and a test or review date. Where numbers are used, show the denominator. Where the question is legal, label jurisdiction and effective date. Cite at least two reading links from above. The case is fictional; do not use real student information.

**Source-application check.** Paired ATT&CK/ATLAS attack paths with one detection and test. Cite the relevant primary publisher pages above, specify source scope and status, and do not claim that a questionnaire answer or technique label proves effectiveness.

## 75-minute supervised extension

In a scheduled studio or supervised online session, spend 20 minutes gathering the linked publisher evidence, 35 minutes revising **threat register and attack-path map** against a peer's challenge, and 20 minutes writing an individual note that identifies which claim changed, what evidence caused the change, and the next verification step. The instructor records attendance/engagement under local policy. This extension supplies the additional structured contact time in the suggested 12-week, 3-credit format.

## Facilitator cues and assessment

- Probe the misconception: **“An ATLAS mapping proves an attack was observed.”** Request a counterexample grounded in the scenario.
- Strong submission: specific facts and assumptions are separated, at least one plausible alternative is tested, a named actor owns the next step, and the conclusion is appropriately limited.
- Developing submission: lists framework names without tying them to a decision or evidence.
- Extension: change one case fact (vendor role, data source, user population or deployment scale); ask which conclusion must change and which remains robust.

## Slide deck

Use the editable [Week 02 deck](../slides/week-02.md); speaker prompts are also in slide comments.
