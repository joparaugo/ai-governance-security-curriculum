# Reproducible teaching labs

All labs use invented data and Python 3 standard library; no account, package installation, cloud service, model weights or internet access required. From repository root:

```bash
python3 labs/eval_metrics.py
python3 labs/eval_metrics.py --threshold 0.6
python3 labs/agent_tool_sim.py --mode insecure
python3 labs/agent_tool_sim.py --mode secure
python3 labs/poisoning_demo.py
python3 -m unittest discover -s labs/tests -v
```

Use [Lab 1](lab-01-evaluation.md) in course 2, [Labs 2 and 3](lab-02-injection.md) in course 3, and [Lab 4](lab-04-audit-tabletop.md) in course 4. [Lab 5](lab-05-cloud-ai-assurance.md) is a CSA/COSO/SOC 2 supplier tabletop for course 4 (with a course 3 variant). [Lab 6](lab-06-paired-threat-mapping.md) is an ATT&CK/ATLAS/D3FEND threat and detection tabletop for course 3 (with a course 2 extension). The tabletop guides and other labs offer spreadsheet/paper routes. The intentionally flawed agent mode is a **local simulation**; it never sends a message or makes a network call.
