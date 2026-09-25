# AI incident runbook — [service/version/on-call]

1. **Intake and triage:** report ID, timestamp, reporter, affected people, suspected security/privacy/model harm, confidence and immediate safety action.
2. **Preserve evidence:** model/dataset/prompt/retrieval/tool versions, access and decision logs, original reports; handle sensitive data with controlled access.
3. **Contain:** disable risky tool or integration, restrict access, pause pilot or roll back; record approver and business impact.
4. **Investigate:** reconstruct timeline and compare observed behavior with policy; check direct API, tool, model, data and human routes; avoid presuming every blocked action was successful.
5. **Notify and support:** involve security, privacy/legal, owner and affected-person support; determine applicable notification duties from current law.
6. **Recover:** independent verification, controlled re-enable, postincident monitoring and student remediation.
7. **Learn:** root cause, corrective action, owner, date, test and board report.

Reference [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final). This is a teaching template; an institution must integrate local emergency procedures.
