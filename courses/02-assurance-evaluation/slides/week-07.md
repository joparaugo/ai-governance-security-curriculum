---
marp: true
theme: default
paginate: true
---
# Privacy and information leakage
### AIE 420 · Week 07

<!-- Speaker: Ask for one case assumption before revealing the outline. -->
---
## Today’s decision

A tutoring assistant quotes a private advisor note to the wrong student.

**What should the institution do next, and what evidence would change your mind?**

<!-- Speaker: Give groups 90 seconds to make a first call. -->
---
## 1 · System and context

- Test for exposure of personal information in prompts, outputs, logs and retrieval.
- Identify an affected person and the decision owner.

<!-- Speaker: Ask for the boundary of the claim. -->
---
## 2 · Competing interpretations

- Separate data minimization and access control from post-hoc output filters.
- Record a plausible alternative explanation.

<!-- Speaker: Challenge a confident generalization. -->
---
## 3 · Operational test

- Use synthetic canaries and authorized local data; do not probe real student records.
- Specify observable evidence and review date.

<!-- Speaker: Ask who verifies this claim. -->
---
## Studio: produce an artifact

Map leak paths and test a fake record with allowed/denied identities.

**Deliver:** Leakage test log and remediation evidence

<!-- Speaker: Use the module’s studio instructions and public rubric. -->
---
## Challenge and exit

- What is still uncertain?
- Which person or team is accountable?
- Which evidence would justify a different decision?

**Reading anchors:** PRIV, ISO27701, ICO

<!-- Speaker: Collect a 100-word individual defense. -->
