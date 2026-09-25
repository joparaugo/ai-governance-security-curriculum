---
marp: true
theme: default
paginate: true
---
# Detection, incident response and recovery
### SEC 430 · Week 11

<!-- Speaker: Ask for one case assumption before revealing the outline. -->
---
## Today’s decision

A retrieval page causes 14 blocked outbound email attempts in one hour.

**What should the institution do next, and what evidence would change your mind?**

<!-- Speaker: Give groups 90 seconds to make a first call. -->
---
## 1 · System and context

- Define signals for poisoning, injection, data leak and unauthorized tool actions.
- Identify an affected person and the decision owner.

<!-- Speaker: Ask for the boundary of the claim. -->
---
## 2 · Competing interpretations

- Specify triage, containment, evidence preservation, notification assessment and rollback.
- Record a plausible alternative explanation.

<!-- Speaker: Challenge a confident generalization. -->
---
## 3 · Operational test

- Exercise an incident without exposing real secrets or student data.
- Specify observable evidence and review date.

<!-- Speaker: Ask who verifies this claim. -->
---
## Source comparison and evidence

- Triangulate a suspicious cloud token event, page-content change and denied outbound email. Search ATT&CK for enterprise behavior and ATLAS for AI behavior; decide which telemetry would confirm or reject each.
- **Deliver:** Detection coverage row and incident triage decision.

<!-- Speaker: Insist on claim boundaries and a testable evidence request. -->
---
## Studio: produce an artifact

Hold a tabletop with timed incident injects and role assignments.

**Deliver:** Incident runbook and after-action review

<!-- Speaker: Use the module’s studio instructions and public rubric. -->
---
## Challenge and exit

- What is still uncertain?
- Which person or team is accountable?
- Which evidence would justify a different decision?

**Reading anchors:** MITRE_CLOUD, MITRE_D3FEND, IR, CSF, MONITOR

<!-- Speaker: Collect a 100-word individual defense. -->
