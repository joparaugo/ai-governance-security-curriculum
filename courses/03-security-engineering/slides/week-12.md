---
marp: true
theme: default
paginate: true
---
# Secure release exercise
### SEC 430 · Week 12

<!-- Speaker: Ask for one case assumption before revealing the outline. -->
---
## Today’s decision

CampusAssist will launch to one department next week.

**What should the institution do next, and what evidence would change your mind?**

<!-- Speaker: Give groups 90 seconds to make a first call. -->
---
## 1 · System and context

- Combine architecture, threats, secure design, local tests and response into a release decision.
- Identify an affected person and the decision owner.

<!-- Speaker: Ask for the boundary of the claim. -->
---
## 2 · Competing interpretations

- Explain residual risks and who accepts them.
- Record a plausible alternative explanation.

<!-- Speaker: Challenge a confident generalization. -->
---
## 3 · Operational test

- Demand reproducible evidence and treat untested integrations as conditions.
- Specify observable evidence and review date.

<!-- Speaker: Ask who verifies this claim. -->
---
## Source comparison and evidence

- At the release gate, verify at least one cloud/customer control and one AI-specific control; name their separate owners and evidence. A green cloud posture is insufficient if the tool-action boundary remains open.
- **Deliver:** Release gate table with two owners and stop condition.

<!-- Speaker: Insist on claim boundaries and a testable evidence request. -->
---
## Studio: produce an artifact

Peer red team challenges another team’s release package.

**Deliver:** Security capstone: threat model, tests, control plan, release memo

<!-- Speaker: Use the module’s studio instructions and public rubric. -->
---
## Challenge and exit

- What is still uncertain?
- Which person or team is accountable?
- Which evidence would justify a different decision?

**Reading anchors:** CSA_CCM, AISVS, SSDF_AI, AICM

<!-- Speaker: Collect a 100-word individual defense. -->
