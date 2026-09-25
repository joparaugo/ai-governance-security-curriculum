# Maintenance and release playbook

**Owner to fill before launch:** GitHub handle, editorial lead, security contact, review board, issue triage rotation and release calendar. No automated process silently changes course claims.

## Once per academic term

1. Check the [62 publisher and regulator resource pages](shared/resources.csv) for status, edition, access and moved links. Run `python3 scripts/check_sources.py --remote`; investigate transient blocks separately from confirmed missing pages.
2. Check EU AI Act [base text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng), [2026 amendment](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng) and [Commission timeline](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai). Check NIST [AI RMF](https://airc.nist.gov/) and [Privacy Framework update](https://www.nist.gov/privacy-framework/new-projects/privacy-framework-version-11). Check ISO publisher pages and OWASP releases.
3. For each changed source: record what changed and effective date, identify affected module/slide/assessment, have an expert review the revision, and update the crosswalk and catalog. Preserve a note if a resource remains a draft.
4. Ask an instructor to run one exercise in each course and confirm time/accessibility. Validate links and lab tests. Check that public answer keys match questions.
5. Update `CHANGELOG.md`, version in `CITATION.cff` and root README, then tag a GitHub release (e.g. `v0.2.0`) with a short migration note. Keep old tags for syllabi already in use.

## Version convention

- Major: course sequence or learning outcomes break.
- Minor: new units, lab changes, substantive law/standards revision.
- Patch: broken links, typos, clarifications that do not change assessed outcomes.

## Issue labels and policy

Use `source-update`, `law-update`, `pedagogy`, `accessibility`, `security-lab`, and `good-first-issue`. Never merge a legal claim solely on a link checker result. Reuse verified official URLs and note date checked. If a paywalled standard is essential, offer a free alternative to meet the assessed outcome.
