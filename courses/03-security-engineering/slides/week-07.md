---
marp: true
theme: default
paginate: true
---
# Agent and tool privilege
### SEC 430 · Week 07

<!-- Speaker: Ask for one case assumption before revealing the outline. -->
---
## Today’s decision

An agent is asked to bulk-email students but the task only approved a draft.

**What should the institution do next, and what evidence would change your mind?**

<!-- Speaker: Give groups 90 seconds to make a first call. -->
---
## 1 · System and context

- Inventory each tool’s action scope and require human confirmation for consequential changes.
- Identify an affected person and the decision owner.

<!-- Speaker: Ask for the boundary of the claim. -->
---
## 2 · Competing interpretations

- Bind authorization to the caller, target resource and action; do not let model text confer permission.
- Record a plausible alternative explanation.

<!-- Speaker: Challenge a confident generalization. -->
---
## 3 · Operational test

- Test tool misuse, forged tool results, memory poisoning and runaway loops.
- Specify observable evidence and review date.

<!-- Speaker: Ask who verifies this claim. -->
---
## Source comparison and evidence

- Define a per-call policy for the send-email tool: caller identity, purpose, resource, audience, rate and approval. Test unauthorized object access and denied calls even when an agent text prompt claims authority.
- **Deliver:** Tool-authorization decision table and negative tests.

<!-- Speaker: Insist on claim boundaries and a testable evidence request. -->
---
## Studio: produce an artifact

Patch the simulation policy; run the local adversarial fixtures.

**Deliver:** Tool permission matrix and before/after trace

<!-- Speaker: Use the module’s studio instructions and public rubric. -->
---
## Challenge and exit

- What is still uncertain?
- Which person or team is accountable?
- Which evidence would justify a different decision?

**Reading anchors:** NIST_ZTA, OWASP_API, CSA_AICM_GUIDE, OWASP_AGENT, AISVS, CSF

<!-- Speaker: Collect a 100-word individual defense. -->
