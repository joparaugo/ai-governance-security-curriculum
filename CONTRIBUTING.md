# Contributing

Thank you for helping educators teach AI governance and security accurately.

## A useful contribution

Open a GitHub issue with the affected course/week, exact publisher URL, observed edition/status, date checked and proposed teaching change. For a pull request, explain the pedagogical objective, update resource IDs and version status when needed, keep the required student path free, and run local checks. New examples must use synthetic data and have accessible noncoding alternatives where possible. Do not copy copyrighted standard text, licensed training material or personal records.

## Review steps

1. Link to an authoritative source, preferably publisher/regulator/legal text or original research. Mark proposals and drafts as such.
2. Update the lesson, relevant slide deck, assignments/keys and [crosswalk](shared/framework-crosswalk.md) together; document changes in [CHANGELOG](CHANGELOG.md).
3. Run `python3 scripts/validate_repo.py` and `python3 -m unittest discover -s labs/tests -v`.
4. For substantive law/version changes, request two reviewers (subject expert and instructor) and record the verification date. Resolve comments and squash or merge under the maintainer's chosen policy.
5. For new security labs, preserve offline operation, explicit authorization boundaries and a paper alternative.

## Source review cadence

The monthly workflow checks whether resource URLs return confirmed 404/410 responses. A maintainer reviews versions and legal changes at least once each academic term and after a major release or statutory amendment. The review checklist is in [MAINTENANCE](MAINTENANCE.md). Link health cannot determine legal correctness.

By submitting original work, contributors agree it will be distributed under the repository's CC BY 4.0 content and MIT code licenses. Identify third-party assets and their licenses before submission. Use the [Code of Conduct](CODE_OF_CONDUCT.md).
