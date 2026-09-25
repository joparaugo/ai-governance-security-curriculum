# SEC 430: AI Security Engineering and Adversarial Testing

Threat-model and secure AI systems, run authorized local adversarial exercises, implement defenses, and verify them.

[Teach this course](syllabus.md) · [Instructor guide](instructor-guide.md) · [Assignments](assignments.md) · [Assessments](assessments.md) · [Common case](../../shared/case-campusassist.md) · [Resource catalog](../../shared/resources.md)

## Learning outcomes

1. Map AI-specific and ordinary application threats to attack surfaces and controls.
2. Explain poisoning, evasion, extraction, prompt injection and agent misuse.
3. Implement least-privilege tool access and data isolation in a local simulation.
4. Design testable defenses across build, deployment and incident response.
5. Produce a threat model, evidence-backed control plan and response runbook.

## Weekly teaching units

| Week | Module | Source IDs | Slide deck |
|---:|---|---|---|
| 01 | [AI architecture and assets](modules/week-01.md) | ISO23053, SSDF_AI, CSF, CSA_CCM, ISO27017, CIS_CONTROLS | [Slides](slides/week-01.md) |
| 02 | [ATT&CK and ATLAS threat modeling](modules/week-02.md) | ATLAS, AML, ASVS, MITRE_ATTACK, MITRE_CLOUD, MITRE_D3FEND | [Slides](slides/week-02.md) |
| 03 | [Data poisoning and training integrity](modules/week-03.md) | AML, AISVS, SSDF_AI | [Slides](slides/week-03.md) |
| 04 | [Evasion and robustness](modules/week-04.md) | AML, ISO24029_2, ISO29119, AISVS | [Slides](slides/week-04.md) |
| 05 | [Prompt injection and instruction hierarchy](modules/week-05.md) | OWASP_LLM, ATLAS, AISVS, MITRE_ATTACK | [Slides](slides/week-05.md) |
| 06 | [RAG, retrieval and data isolation](modules/week-06.md) | AISVS, OWASP_LLM, ISO27002 | [Slides](slides/week-06.md) |
| 07 | [Agent and tool privilege](modules/week-07.md) | OWASP_AGENT, AISVS, CSF, NIST_ZTA, OWASP_API, CSA_AICM_GUIDE | [Slides](slides/week-07.md) |
| 08 | [Model and software supply chain](modules/week-08.md) | SSDF, SSDF_AI, ISO27001, NIST_SCRM, NCSC_SECUREAI, SLSA | [Slides](slides/week-08.md) |
| 09 | [Privacy, extraction and abuse](modules/week-09.md) | AML, GAI, PRIV | [Slides](slides/week-09.md) |
| 10 | [Security requirements and verification](modules/week-10.md) | AISVS, ASVS, SP53, CSA_CCM, NIST_53A, CIS_CONTROLS | [Slides](slides/week-10.md) |
| 11 | [Detection, incident response and recovery](modules/week-11.md) | IR, CSF, MONITOR, MITRE_CLOUD, MITRE_D3FEND | [Slides](slides/week-11.md) |
| 12 | [Secure release exercise](modules/week-12.md) | AISVS, SSDF_AI, AICM, CSA_CCM | [Slides](slides/week-12.md) |

Each module contains teachable explanations, a 150-minute session plan, group exercise, assessment prompt and instructor cues. Slide files use Marp-compatible Markdown with speaker prompts. Assignment briefs, answer guidance and rubrics are provided separately. All weekly required readings link to free publisher material; ISO full texts are optional institutional-library extensions.
