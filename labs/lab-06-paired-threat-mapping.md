# Lab 6: MITRE ATT&CK, ATLAS and D3FEND

**Use:** Course 3 weeks 2, 5 or 11; Course 2 week 9 as an assurance extension. **Time:** 75 minutes. **Materials:** [fictional case](../shared/case-campusassist.md), [threat model template](../templates/threat-model.md), [incident runbook](../templates/incident-runbook.md). This is a paper/offline tabletop; there is no live target or account.

## Official source anchors

- [MITRE Enterprise ATT&CK introduction](https://attack.mitre.org/resources/) and [cloud matrix](https://attack.mitre.org/matrices/enterprise/cloud/): identity, SaaS, infrastructure and conventional enterprise behaviors.
- [MITRE ATLAS](https://atlas.mitre.org/): AI-specific behavior against the model, data, retrieval or tool workflow.
- [MITRE D3FEND](https://d3fend.mitre.org/about/): candidate defensive techniques. [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final): incident response roles and recovery.

## Fictional event

At 09:00 an identity alert reports a new service-token sign-in from an unfamiliar IP. At 09:05 a public scholarship page is edited to contain text telling CampusAssist to send an email. At 09:10 the local monitor records 14 denied email attempts; no successful email or data exfiltration has been established. Event order alone does not prove a common attacker or a successful compromise.

## Student instructions

1. **0–15 min:** draw the boundaries from internet page to retriever, agent, send-email tool, IAM and logs. List two alternative explanations for the sign-in and the changed page.
2. **15–35 min:** find a plausible Enterprise/cloud ATT&CK technique for identity misuse and an ATLAS technique for AI workflow manipulation. Record publisher page links, IDs if visible, and whether each is **observed**, **suspected** or **hypothetical**. Do not infer an ATT&CK mapping from alert text alone.
3. **35–50 min:** pick one detection for identity activity and one for tool-action attempts. Ask who owns each log, what is retained, expected signal, false-positive cause and a falsifying observation.
4. **50–65 min:** choose one candidate defensive idea from D3FEND or the MITRE mitigations, then design a local control test: tampered page, valid identity, tool denial and independently checked alert. A taxonomy relationship is a hypothesis until tested.
5. **65–75 min:** draft the incident decision: immediate containment, preservation, communications threshold, recovery and date for reassessment; explicitly state whether exfiltration is known.

**Submit:** [threat model](../templates/threat-model.md), paired technique/evidence table, two detection specifications and a two-paragraph incident decision. The student may browse official source pages during preparation and complete the mapping offline from notes.

## Instructor key and rubric

**Indicative answer:** The new sign-in suggests an identity investigation, not proof of account takeover. The altered public page supports a prompt-injection hypothesis; denied email attempts support a tool-boundary observation, not an exfiltration claim. A good plan preserves IAM and retrieval logs, temporarily narrows tool privilege and checks who edited the page. Selection of precise technique IDs can vary as the MITRE catalogs evolve.

**Score (100):** boundaries and separate chains 20; relevant publisher-linked techniques with correct evidence status 25; telemetry and alternate explanations 20; testable defense and authorization 20; proportionate response and uncertainty 15. Do not score mere count of technique labels.
