# SEC 430: AI Security Engineering and Adversarial Testing — adoptable syllabus

**Format:** 12 teaching weeks; suggested 3 credits subject to local policy. Each week has 150 minutes of seminar plus a 75-minute instructor-supervised studio or online equivalent: 45 supervised hours across the term. Plan another 4–6 hours of independent reading and writing per week. **Level:** undergraduate upper division / graduate technical. **Prerequisite:** Basic Python and web application concepts; course 1 recommended. Noncoding alternative available.. **Updated:** 2026-09-25. Instructor should fill institution-specific term, meeting, office hour and accessibility contact details.

## Catalog description

Threat-model and secure AI systems, run authorized local adversarial exercises, implement defenses, and verify them. Students learn to analyze evidence, affected people and organizational controls using official frameworks and synthetic examples. The course is suitable for information systems, cybersecurity, public policy, business and interdisciplinary programs.

## Learning outcomes

1. Map AI-specific and ordinary application threats to attack surfaces and controls.
2. Explain poisoning, evasion, extraction, prompt injection and agent misuse.
3. Implement least-privilege tool access and data isolation in a local simulation.
4. Design testable defenses across build, deployment and incident response.
5. Produce a threat model, evidence-backed control plan and response runbook.

## Materials and cost

All required public readings and supplied exercises are free. Read module links before class. Optional full ISO standards may require institutional subscription; no student must buy a standard. Security labs use Python 3 standard library, a spreadsheet, or paper alternative. No cloud account, API key or real personal data is required. See [resources](../../shared/resources.md) and [computing options](../../shared/teaching-and-accessibility.md).

## Assessment and grading

| Item | Weight | Evidence |
|---|---:|---|
| Weekly learning checks (best 10 of 12) | 20% | One-page exit response per module |
| Applied assignment 1 | 15% | [Brief and rubric](assignments.md) |
| Applied assignment 2 | 15% | [Brief and rubric](assignments.md) |
| Midcourse assessment | 15% | [Question bank and key](assessments.md) |
| Integrated capstone (milestones and final) | 35% | [Brief and rubric](assignments.md) |

**Grade standard:** 90–100 A; 80–89 B; 70–79 C; 60–69 D; below 60 F, subject to local policy. Rubrics reward substantiated reasoning and reproducible evidence, not confident prose. Provide feedback on milestones within a week where feasible.

## Weekly plan

| Week | Topic | Primary sources | Materials |
|---:|---|---|---|
| 01 | [AI architecture and assets](modules/week-01.md) | ISO23053, SSDF_AI, CSF | [Slides](slides/week-01.md) |
| 02 | [Threat modeling with ATLAS](modules/week-02.md) | ATLAS, AML, ASVS | [Slides](slides/week-02.md) |
| 03 | [Data poisoning and training integrity](modules/week-03.md) | AML, AISVS, SSDF_AI | [Slides](slides/week-03.md) |
| 04 | [Evasion and robustness](modules/week-04.md) | AML, ISO24029_2, ISO29119, AISVS | [Slides](slides/week-04.md) |
| 05 | [Prompt injection and instruction hierarchy](modules/week-05.md) | OWASP_LLM, ATLAS, AISVS | [Slides](slides/week-05.md) |
| 06 | [RAG, retrieval and data isolation](modules/week-06.md) | AISVS, OWASP_LLM, ISO27002 | [Slides](slides/week-06.md) |
| 07 | [Agent and tool privilege](modules/week-07.md) | OWASP_AGENT, AISVS, CSF | [Slides](slides/week-07.md) |
| 08 | [Model and software supply chain](modules/week-08.md) | SSDF, SSDF_AI, ISO27001 | [Slides](slides/week-08.md) |
| 09 | [Privacy, extraction and abuse](modules/week-09.md) | AML, GAI, PRIV | [Slides](slides/week-09.md) |
| 10 | [Security requirements and verification](modules/week-10.md) | AISVS, ASVS, SP53 | [Slides](slides/week-10.md) |
| 11 | [Detection, incident response and recovery](modules/week-11.md) | IR, CSF, MONITOR | [Slides](slides/week-11.md) |
| 12 | [Secure release exercise](modules/week-12.md) | AISVS, SSDF_AI, AICM | [Slides](slides/week-12.md) |

## Participation, accessibility and responsible work

Students may choose written, spoken with transcript, or accessible structured-table submission where learning outcomes permit. Offer equivalent paper/spreadsheet routes for technical exercises. Use synthetic data only and attack only the local exercise simulation; no scanning third-party systems. Cite sources and describe any AI assistance, including prompts/tool name, what was checked and what was independently produced. Students remain responsible for factual and technical accuracy. See [teaching policy](../../shared/teaching-and-accessibility.md).

## Academic integrity and copyright

Publisher standards and readings remain with their owners; links are supplied, texts are not copied. Instructor answer keys are public in this open repository: adapt items and request explanations, oral defense or individualized case facts for summative assessment. Accessibility and accommodation requests follow local institutional policy.
