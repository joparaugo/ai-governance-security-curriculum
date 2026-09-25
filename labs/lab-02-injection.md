# Lab 2: untrusted text and tool authorization

**Time:** 75 minutes. **Use:** Course 3 weeks 5–7. **Source anchors:** [OWASP LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/), [OWASP AISVS](https://owasp.org/projects/artificial-intelligence-security-verification-standard-aisvs-docs), [MITRE ATLAS](https://atlas.mitre.org/).

1. Read `MALICIOUS_PAGE` and `simulate()` in [agent_tool_sim.py](agent_tool_sim.py). The page is untrusted content retrieved for a benign scholarship question.
2. Run `python3 labs/agent_tool_sim.py --mode insecure`. Observe `WOULD_SEND_SIMULATED` for the injected page. This is **a printed trace only**: the code has no sending function.
3. Run `--mode secure`; expect `DENIED`. Locate the separate authorization check at the tool boundary. Write an explicit policy over caller, task intent, action and recipient, with a negative case for a student caller.
4. Propose tests for malicious page, forged tool result, private document from another student, unauthorized direct API action, authorized single-recipient action and ambiguous user instruction. For each, specify allow/deny and one log field.
5. Describe limitations: this toy parser is not a language model; the demo proves a policy boundary in one simulated path, not comprehensive resistance to prompt injection.

**Paper route:** draw a four-column table (`source`, `claimed authority`, `requested action`, `policy decision`) for normal and injected pages; annotate where the flawed design crosses the trust boundary. **Instructor challenge:** ask why “ignore the injected text” as a prompt alone is weaker than an independent tool permission check.
