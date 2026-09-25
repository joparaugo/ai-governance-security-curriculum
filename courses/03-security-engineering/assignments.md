# Assignments, answer guidance and rubric

All assignments use the [fictional case](../../shared/case-campusassist.md). Source links and edition status are in [resources](../../shared/resources.md). Students may use prose, tables and a short recorded defense with transcript; technical submissions also have a paper/spreadsheet route.

## Applied assignment 1: AI threat model

**Due:** Week 3. **Scenario:** The scholarship retriever reads public pages, while internal notes and a draft-email tool are nearby.

**Student task.** An architecture/data-flow diagram, assets, trust boundaries, two ATLAS-mapped AI attacks, two [Enterprise/cloud ATT&CK](https://attack.mitre.org/matrices/enterprise/cloud/)-mapped ordinary application or identity attacks, attacker capabilities, detection signals and risk-based priority. For one candidate [D3FEND](https://d3fend.mitre.org/about/) countermeasure, specify a local test; the mapping itself does not prove the defense works. Use the [paired-threat tabletop](../../labs/lab-06-paired-threat-mapping.md).

**Required process.** Start with the case evidence IDs and identify one fact you would verify with a primary source. Distinguish observation, assumption, decision and residual uncertainty. Cite at least three publisher links from [the catalog](../../shared/resources.md). Name at least one affected person, an accountable owner and a review date. In the final paragraph, defend a rejected alternative. Submit accessible text plus any table/code artifacts. Mark all synthetic calculations as teaching examples.

**Instructor answer guidance (public).** Strong response separates untrusted retrieved content from authority, includes conventional access control and does not present a framework label as proof of compromise. Accept more than one recommendation if the evidence, tradeoffs and limits support it. Ask for an oral challenge: “Which fact, if reversed, changes your recommendation?”

**Rubric (100 points).**

| Dimension | Weight | Excellent | Developing | Insufficient |
|---|---:|---|---|---|
| Problem framing and authority | 20% | Correct scope, actors, legal/framework status and assumptions | Some missing scope or ambiguous authority | Treats voluntary guidance as binding or omits affected people |
| Evidence and method | 25% | Reproducible evidence, denominators/versions and counterevidence | Evidence partly traceable; limits incomplete | Claims unsupported or numbers unrepeatable |
| Risk, equity and security | 20% | Distinct harms, causes, controls and residual risk with owners | Several issues recognized but controls vague | Material harm or attack surface ignored |
| Feasible decision and review | 20% | Action, owner, timeframe, test and stop criteria | Decision given without all follow-up | No implementable decision |
| Writing and citations | 15% | Clear accessible structure, primary links, explicit uncertainty | Understandable but incomplete citations | Unclear or uncredited claims |


## Applied assignment 2: Injection, isolation and verification

**Due:** Week 7. **Scenario:** An untrusted page instructs the local toy app to send a bulk email.

**Student task.** Run the offline simulator in insecure and secure mode; attach traces; propose retrieval authorization and tool-call policy, at least six negative tests, and a false-positive/usability check. Noncoding option: annotate provided traces and write pseudocode policy.

**Required process.** Start with the case evidence IDs and identify one fact you would verify with a primary source. Distinguish observation, assumption, decision and residual uncertainty. Cite at least three publisher links from [the catalog](../../shared/resources.md). Name at least one affected person, an accountable owner and a review date. In the final paragraph, defend a rejected alternative. Submit accessible text plus any table/code artifacts. Mark all synthetic calculations as teaching examples.

**Instructor answer guidance (public).** Strong response places permission checking at the tool boundary and ties each negative test to a verifiable outcome. Accept more than one recommendation if the evidence, tradeoffs and limits support it. Ask for an oral challenge: “Which fact, if reversed, changes your recommendation?”

**Rubric (100 points).**

| Dimension | Weight | Excellent | Developing | Insufficient |
|---|---:|---|---|---|
| Problem framing and authority | 20% | Correct scope, actors, legal/framework status and assumptions | Some missing scope or ambiguous authority | Treats voluntary guidance as binding or omits affected people |
| Evidence and method | 25% | Reproducible evidence, denominators/versions and counterevidence | Evidence partly traceable; limits incomplete | Claims unsupported or numbers unrepeatable |
| Risk, equity and security | 20% | Distinct harms, causes, controls and residual risk with owners | Several issues recognized but controls vague | Material harm or attack surface ignored |
| Feasible decision and review | 20% | Action, owner, timeframe, test and stop criteria | Decision given without all follow-up | No implementable decision |
| Writing and citations | 15% | Clear accessible structure, primary links, explicit uncertainty | Understandable but incomplete citations | Unclear or uncredited claims |


## Integrated capstone: Secure release dossier

**Due:** Week 12. **Scenario:** The pilot is due next week with a vendor model update and an unresolved injection alert.

**Student task.** Produce threat model, asset and supply-chain inventory, AISVS/ASVS test matrix, verified lab traces, privacy/leakage controls, incident runbook, residual-risk memo, rollout/rollback plan and five-minute security review.

**Added source application (assessed).** Include a [CSA CCM cloud](https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4-1) and [AICM AI](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1) control comparison with separate customer/provider owners, one [NIST SP 800-161](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final) supplier risk and one [SP 800-53A](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) style control test. Ten evidence/method points require an observed pass/fail and a bounded release decision.

**Provenance extension:** Add a [SLSA](https://slsa.dev/spec/v1.2/) build evidence request and an [SPDX AI profile](https://spdx.dev/learn/areas-of-interest/ai/) dependency row. Distinguish a reproducible software build from a verified or safe model.

**Required process.** Start with the case evidence IDs and identify one fact you would verify with a primary source. Distinguish observation, assumption, decision and residual uncertainty. Cite at least three publisher links from [the catalog](../../shared/resources.md). Name at least one affected person, an accountable owner and a review date. In the final paragraph, defend a rejected alternative. Submit accessible text plus any table/code artifacts. Mark all synthetic calculations as teaching examples.

**Instructor answer guidance (public).** Strong response holds or conditions release based on gaps, names independent verification, includes ordinary app risks and provides alert triage evidence. Accept more than one recommendation if the evidence, tradeoffs and limits support it. Ask for an oral challenge: “Which fact, if reversed, changes your recommendation?”

**Rubric (100 points).**

| Dimension | Weight | Excellent | Developing | Insufficient |
|---|---:|---|---|---|
| Problem framing and authority | 20% | Correct scope, actors, legal/framework status and assumptions | Some missing scope or ambiguous authority | Treats voluntary guidance as binding or omits affected people |
| Evidence and method | 25% | Reproducible evidence, denominators/versions and counterevidence | Evidence partly traceable; limits incomplete | Claims unsupported or numbers unrepeatable |
| Risk, equity and security | 20% | Distinct harms, causes, controls and residual risk with owners | Several issues recognized but controls vague | Material harm or attack surface ignored |
| Feasible decision and review | 20% | Action, owner, timeframe, test and stop criteria | Decision given without all follow-up | No implementable decision |
| Writing and citations | 15% | Clear accessible structure, primary links, explicit uncertainty | Understandable but incomplete citations | Unclear or uncredited claims |
