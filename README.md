# AI Governance & Security Curriculum

**Four independent, adaptable university courses | 12 weeks each | governance + evaluation + security + management and policy | version 0.2.0 (2026-09-25)**

This open educational repository gives instructors lesson plans, editable Markdown slide decks, syllabi, case exercises, rubrics, public answer keys, workpapers, offline labs and direct links to publisher resources. It develops practical competencies across technical and nontechnical AI governance and security. Each course can be taught separately; [adaptation paths](shared/teaching-and-accessibility.md) explain shorter sequences. All sample student data are invented.

| Course | Main competency | Prerequisite | Open course |
|---|---|---|---|
| 1. Foundations of AI Governance and Responsible Use | System boundaries, ethics, inventories, risk, impacts, rights and policy | None beyond introductory IS/policy | [GOV 310](courses/01-foundations-governance/README.md) |
| 2. AI Assurance, Data Governance, and Evaluation | Dataset quality, metrics, fairness, GenAI/agent tests and monitoring | Course 1 or equivalent | [AIE 420](courses/02-assurance-evaluation/README.md) |
| 3. AI Security Engineering and Adversarial Testing | Threat modeling, poisoning, prompt injection, secure tools and incident response | Python/web fundamentals; alternative noncode route | [SEC 430](courses/03-security-engineering/README.md) |
| 4. Enterprise AI Governance, Audit, and Public Policy | AIMS, procurement, audit, law, board decisions and public policy | Course 1 + 2 or 3, or equivalent | [GRC 510](courses/04-program-audit-policy/README.md) |

## What is in the repository?

- **48 weekly modules** with outcomes, linked readings, teaching explanations, 150-minute session plans, studio tasks, student deliverables and instructor cues; **48 editable Marp Markdown slide decks**.
- **Four complete course syllabi and instructor guides**, plus course-specific applied assignments, capstones, rubrics and assessments with public answer guidance.
- A common [fictional case dossier](shared/case-campusassist.md) with evidence exhibits and incident injects; [six labs](labs/README.md) including offline Python evaluation, simulated prompt injection, poisoning, audit, supplier assurance and paired threat-mapping tabletops.
- **95 linked publisher, standards and research resources** in a [human-readable guide](shared/resources.md) and [machine-readable catalog](shared/resources.csv), with a [coverage audit](shared/coverage-audit.md), [framework-to-competency crosswalk](shared/framework-crosswalk.md), [outcome map](shared/competency-map.csv), [transfer cases](shared/alternative-cases.md) and reusable [workpapers](templates/README.md).
- Repository governance: licenses, contribution guide, version log, issue templates and CI that checks internal links/tests, plus a scheduled source-link check. Human maintainers must check editions and legal status each term.

## Adopt in 20 minutes

1. Choose a course above and copy its [syllabus](courses/01-foundations-governance/syllabus.md) to your course site; update local schedule and accommodation contacts.
2. Read the [teaching/accessibility guide](shared/teaching-and-accessibility.md), [case](shared/case-campusassist.md), and [source/version notes](shared/framework-crosswalk.md).
3. Assign each module’s linked readings, use its slide deck and run its studio exercise. Grade using that course’s assignments and public answer guidance.
4. Run labs locally with Python 3 if applicable. For example `python3 labs/eval_metrics.py` and `python3 -m unittest discover -s labs/tests -v`.
5. Before each term, check [official sources](shared/resources.md), especially laws and drafts; record updates in [CHANGELOG](CHANGELOG.md). Use [CONTRIBUTING](CONTRIBUTING.md) to submit a version correction.

## Standards and law: how to read this courseware

The catalog includes NIST AI RMF, GenAI Profile, CSF 2.0, Privacy Framework, SP 800-53/53A, SP 800-37, SP 800-30, SP 800-161 and SSDF AI; ISO/IEC 42001, 23894, 42005, 42006, 38507, 5338, 5259, 25059, 27001/27002/27005, 27017, 27018 and 27701, ISO 31000, 37301 and 19011; OWASP LLM/agentic/AISVS/API; MITRE ATLAS, ATT&CK and D3FEND; CSA AICM, CCM, CAIQ and STAR; COSO, COBIT, IIA, CIS and SOC 2; SLSA provenance and SPDX AI component records; Singapore AI Verify and agentic AI governance; OECD, UNESCO and Council of Europe policy instruments; GDPR and the EU AI Act as amended in 2026. A [crosswalk](shared/framework-crosswalk.md) and [audit](shared/coverage-audit.md) link these to skills, activities and evidence. **No single mapping proves certification or legal compliance.** Complete ISO and some COSO, ISACA and AICPA publications may require a license; students use accessible publisher overviews and public readings for required work.

The EU AI Act is time-sensitive. The [Commission’s current timeline](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) and [2026 amendment](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng) are linked and dated; instructors must recheck them. The NIST Privacy Framework 1.1 was still an **initial public draft** as checked 2026-09-25, so the course uses 1.0 as the released baseline.

## Rights, attribution and updates

Course prose, decks, templates, rubrics and fictional data are licensed under [CC BY 4.0](LICENSE-CONTENT.md); original code under [MIT](LICENSE-CODE). External resources keep their own terms and are linked rather than copied. Cite as shown in [CITATION.cff](CITATION.cff). Contributions are welcome via [CONTRIBUTING](CONTRIBUTING.md); security issues follow [SECURITY](SECURITY.md).

**Repository:** [joparaugo/ai-governance-security-curriculum](https://github.com/joparaugo/ai-governance-security-curriculum). Maintainers should confirm public visibility, add a security contact, enable Actions, and review institutional contributor policies before inviting outside contributions.
