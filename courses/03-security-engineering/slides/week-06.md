---
marp: true
theme: default
paginate: true
---
# RAG, retrieval and data isolation
### SEC 430 · Week 06

<!-- Speaker: Ask for one case assumption before revealing the outline. -->
---
## Today’s decision

A public query retrieves a private advisor note via a shared index.

**What should the institution do next, and what evidence would change your mind?**

<!-- Speaker: Give groups 90 seconds to make a first call. -->
---
## 1 · System and context

- Enforce authorization before retrieval and again before returning sensitive content.
- Identify an affected person and the decision owner.

<!-- Speaker: Ask for the boundary of the claim. -->
---
## 2 · Competing interpretations

- Account for document provenance, index updates, stale permissions and cross-tenant leakage.
- Record a plausible alternative explanation.

<!-- Speaker: Challenge a confident generalization. -->
---
## 3 · Operational test

- Measure answer quality impact from secure retrieval filters.
- Specify observable evidence and review date.

<!-- Speaker: Ask who verifies this claim. -->
---
## Studio: produce an artifact

Design retrieval ACL tests for roles and record ownership.

**Deliver:** RAG architecture with four negative tests

<!-- Speaker: Use the module’s studio instructions and public rubric. -->
---
## Challenge and exit

- What is still uncertain?
- Which person or team is accountable?
- Which evidence would justify a different decision?

**Reading anchors:** AISVS, OWASP_LLM, ISO27002

<!-- Speaker: Collect a 100-word individual defense. -->
