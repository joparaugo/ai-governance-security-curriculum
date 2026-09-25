# AI threat model — [system / version / date]

1. **Architecture:** data ingestion, training, registry, retrieval, API, model, user interface, tools, logs and identity; draw trust boundaries.
2. **Assets and attackers:** valuable data/actions, capability, access and motivation. Include ordinary web, identity and supply-chain threats.
3. **Scenario table:** source/entry, adversary objective, prerequisites, path, affected asset, consequence, likelihood rationale, detection signal, prevention, owner and negative test.
4. **Control verification:** map selected [OWASP AISVS](https://owasp.org/projects/artificial-intelligence-security-verification-standard-aisvs-docs) and [NIST SSDF AI](https://csrc.nist.gov/pubs/sp/800/218/a/final) to *tested* behavior and evidence IDs. An [ATLAS](https://atlas.mitre.org/) label describes a technique, not a proven compromise.
5. **Residual risks:** untreated scenario, exception owner, expiry, incident trigger and rollback.

**Required negative tests:** untrusted document requests privileged tool; unauthorized user accesses another person's document; direct API action without approval; stale permissions; changed model artifact; poisoned source; benign input falsely blocked.
