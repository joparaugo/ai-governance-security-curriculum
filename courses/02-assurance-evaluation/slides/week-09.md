---
marp: true
theme: default
paginate: true
---
# Agent and tool evaluation
### AIE 420 · Week 09

<!-- Speaker: Ask for one case assumption before revealing the outline. -->
---
## Today’s decision

An agent attempts to email a student on the strength of an untrusted web page.

**What should the institution do next, and what evidence would change your mind?**

<!-- Speaker: Give groups 90 seconds to make a first call. -->
---
## 1 · System and context

- Measure behavior of the full agent workflow, permissions and tools, not only its language model.
- Identify an affected person and the decision owner.

<!-- Speaker: Ask for the boundary of the claim. -->
---
## 2 · Competing interpretations

- Test undesired tool calls, unauthorized data access and user-intervention checkpoints.
- Record a plausible alternative explanation.

<!-- Speaker: Challenge a confident generalization. -->
---
## 3 · Operational test

- Record the action trace, time and recovery from a failed task.
- Specify observable evidence and review date.

<!-- Speaker: Ask who verifies this claim. -->
---
## Studio: produce an artifact

Design a task trace with positive and adversarial cases.

**Deliver:** Agent test matrix with approval gates

<!-- Speaker: Use the module’s studio instructions and public rubric. -->
---
## Challenge and exit

- What is still uncertain?
- Which person or team is accountable?
- Which evidence would justify a different decision?

**Reading anchors:** OWASP_AGENT, AISVS, ATLAS

<!-- Speaker: Collect a 100-word individual defense. -->
