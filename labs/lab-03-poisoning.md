# Lab 3: label change and provenance

**Time:** 50 minutes. **Use:** Course 3 week 3 and Course 2 week 3. **Source anchors:** [NIST adversarial ML taxonomy](https://csrc.nist.gov/pubs/ai/100/2/e2025/final), [NIST SSDF AI profile](https://csrc.nist.gov/pubs/sp/800/218/a/final).

1. Run `python3 labs/poisoning_demo.py`. Five fabricated training items use a one-dimensional feature and nearest-three vote. Record the nearest IDs and prediction before and after an unauthorized label change to record D.
2. Explain exactly which record changed, why the selected neighbors stayed the same, and why the decision changed. This is a constructed boundary example, not an attack success-rate estimate.
3. Design three checks at ingest (origin, review of label change, approved version hash), one independent validation check, and one rollback procedure. State where logs and separation of duties apply.
4. Submit a one-page threat hypothesis with attacker capability, evidence and a non-AI comparison such as malicious changes to a rules engine.

**Paper route:** compute the same vote by sorting the five distances and tallying three labels. **Instructor note:** ask students whether a legitimate correction of a label could look identical, and what provenance/approval evidence would distinguish it.
