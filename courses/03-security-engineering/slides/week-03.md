---
marp: true
theme: default
paginate: true
---
# Data poisoning and training integrity
### SEC 430 · Week 03

<!-- Speaker: Ask for one case assumption before revealing the outline. -->
---
## Today’s decision

One fraudulent training row claims a failed student succeeded.

**What should the institution do next, and what evidence would change your mind?**

<!-- Speaker: Give groups 90 seconds to make a first call. -->
---
## 1 · System and context

- Compare malicious label changes, dataset contamination and source-provenance manipulation.
- Identify an affected person and the decision owner.

<!-- Speaker: Ask for the boundary of the claim. -->
---
## 2 · Competing interpretations

- Design ingest checks, approval, immutable versions and rollback evidence.
- Record a plausible alternative explanation.

<!-- Speaker: Challenge a confident generalization. -->
---
## 3 · Operational test

- Explain why clean validation data and separation of duties matter.
- Specify observable evidence and review date.

<!-- Speaker: Ask who verifies this claim. -->
---
## Studio: produce an artifact

Run local perturbation or paper simulation; compare decisions and trace source.

**Deliver:** Poisoning hypothesis and prevention/detection tests

<!-- Speaker: Use the module’s studio instructions and public rubric. -->
---
## Challenge and exit

- What is still uncertain?
- Which person or team is accountable?
- Which evidence would justify a different decision?

**Reading anchors:** AML, AISVS, SSDF_AI

<!-- Speaker: Collect a 100-word individual defense. -->
