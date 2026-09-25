# CampusAssist: fictional longitudinal teaching case

**All people, records, organizations and figures here are invented.** This case is designed for governance, assurance, security and policy instruction. It is intentionally ambiguous: instructors should reward stated assumptions and proportionate decisions. No learner should upload real student records or attack a real service.

## Mission and actors

Harbor State University (HSU) wants to improve access to academic support. Its Student Success Office proposes **CampusAssist**, a weekly early-support system that estimates which enrolled students may benefit from an advisor invitation and drafts optional outreach messages. The service is not allowed to determine admissions, grades, financial aid or discipline. Student advisors decide whether and how to contact a student; students can ask for an explanation, correct information and decline further outreach.

| Actor | Role and concern |
|---|---|
| University board | Authorizes scope, resources, risk appetite and independent review. |
| Student Success Office | Business owner; bears workload and missed-support consequences. |
| Registrar/data steward | Controls source records, purposes, quality and retention. |
| Security/privacy teams | Review architecture, access, vendor terms and incidents. |
| Students and advocates | Want fair access, dignity, privacy, useful notices and appeal. |
| Northstar Analytics (fictional) | Hosted model/API and chat interface; may change its model. |
| Faculty and advisors | Interpret alerts, record outcomes and may over-rely on automation. |

## Design on the table

1. HSU sends a weekly batch of synthetic-style fields in the prototype: enrollment status, course load, aggregate engagement indicator, whether previous outreach was accepted, and self-reported scheduling preference. **The production proposal includes real education records, but none are supplied in this repository.** HSU has not established whether attendance data or disability accommodations will be included; the current design says no.
2. The vendor produces a 0–1 outreach-priority score and three short reasons, then an internal advisor dashboard displays the score. A separate retrieval chatbot answers questions from approved public scholarship pages and may draft (not send) an email. A proposed phase two adds a restricted send-email tool.
3. The initial pilot covers 600 students in one department for eight weeks. An advisor has 12 seconds, on average, to review an alert. The office can investigate about 100 alerts each week.
4. Model training involved older HSU data from three cohorts; the vendor cannot yet provide a dataset card, a subgroup sample table or immutable model version IDs. Labels mean “staff recorded a support need within one term,” which can reflect who staff noticed.
5. The vendor's draft contract permits indefinite storage of logs and unilateral model changes. Its security report covers the hosting environment but does not explicitly assess the model's behavior, retrieval access control or the email tool.

## Illustrative pilot figures (invented; for discussion, not inference)

Of 600 scored students, 100 are selected for weekly review. A prior offline evaluation on 240 different synthetic cases reported 92% overall accuracy and 70% recall for the positive class; it supplied no confusion matrix, sampling details or confidence interval. Twenty students filed contact-preference corrections during a manual pilot, and 4 said the explanation felt misleading. The team cannot infer causal benefit from any of these figures. See the separate [32-row synthetic CSV](../labs/data/synthetic_outreach.csv) for **practice calculations only**; it is not a sample from the 240 cases.

## Event injects

- **Week A — scope:** A student advocate asks whether students can opt out of prediction entirely; the system owner has only addressed opting out of outreach.
- **Week B — data:** The registrar learns that “support need” labels are based on inconsistent human notes, and the scheduling-preference field is missing for many working students.
- **Week C — vendor:** Northstar rolls out a new model under an unchanged marketing name, with no regression report.
- **Week D — privacy:** Logs contain synthetic advisor-note excerpts. The vendor proposes keeping analogous production logs indefinitely for retraining.
- **Week E — security:** A public scholarship page contains a prompt-injection instruction to email a student list. The local [toy lab](../labs/README.md) demonstrates how a flawed tool boundary can fail.
- **Week F — monitoring:** Complaints increase after launch even while the vendor's aggregate accuracy estimate remains stable; outcome labels arrive only at term end.
- **Week G — law:** A separate EU partner university asks whether it can use the service for **access to** a higher education program. This is a different use from HSU's support pilot. Identify provider/deployer roles, classification facts and dates from current law; ask counsel for an applicability opinion.

## Evidence packet for an audit exercise

| ID | Item | Evidentiary limitation |
|---|---|---|
| E-01 | Board minutes approve an eight-week pilot, not full deployment. | No named stop criterion. |
| E-02 | Vendor brochure: “unbiased, secure and NIST certified.” | No scope or certification evidence supplied. |
| E-03 | Access matrix restricts the dashboard to assigned advisors. | No retrieval-index tests or access log sample. |
| E-04 | Spreadsheet contains offline aggregate accuracy and recall. | No denominator by group, holdout description or version ID. |
| E-05 | Draft retention clause: indefinite logs. | No data-purpose review. |
| E-06 | Two student interview summaries object to opaque alerts. | Nonrepresentative feedback, yet relevant to design. |
| E-07 | Security team lists “prompt filter enabled.” | No bypass test or tool-action authorization check. |
| E-08 | A synthetic incident ticket records 14 denied outbound email attempts. | Root cause and any successful sends still under investigation. |

## Decision constraints

Budget is limited to a pilot this term. The board can choose **reject**, **defer pending evidence**, **limited pilot with conditions**, or **broader release**. A defensible recommendation specifies why, whose interests it weighs, named owners, test evidence, rollback and a date for reevaluation. It must avoid implying that a voluntary framework or an ISO publisher overview establishes legal compliance.

## Instructor variations

For a different assessment, change the country, tool privilege, source data, pilot population, adverse outcome or vendor right to change models. Tell students which facts changed. For technical labs, use only the included synthetic data and simulated local tools; there is no real model, vendor, email service or account.
