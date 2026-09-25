# Lab 1: evaluation and group error rates

**Time:** 75 minutes. **Use:** Course 2 weeks 4–5. **Source anchors:** [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/), [NIST AI 800-3](https://www.nist.gov/publications/expanding-ai-evaluation-toolbox-statistical-models), [ISO/IEC 25059 overview](https://www.iso.org/standard/80655.html).

1. Open [synthetic_outreach.csv](data/synthetic_outreach.csv). Positive class means the invented record has a support-need label, which is not a ground-truth measure of intervention benefit. Predict positive when `score >= 0.5`.
2. By hand or spreadsheet, compute TP, FP, TN, FN for all records and separately for `day` and `evening`. Precision = TP/(TP+FP), recall = TP/(TP+FN), FNR = FN/(TP+FN); explicitly report denominators.
3. Reproduce with `python3 labs/eval_metrics.py` from root. Check expected default counts: overall TP=9, FP=5, TN=11, FN=7; day FNR=2/8=.25; evening FNR=5/8=.625.
4. Run `--threshold 0.6` and discuss review capacity versus missed support. Recompute rather than assuming monotonic improvement in all metrics.
5. Write a 400-word decision note: propose a threshold for a small pilot, argue why these 32 records are insufficient for assurance, suggest an additional data collection and human-impact study, and consider label bias.

**Instructor check:** do not let learners merge this CSV with the separate fictional 240-case vendor claim; require positive-class definition and small-sample caution. **Paper route:** use the provided CSV as printed cards, sort above/below threshold and tally. **Extension:** ask for a simple uncertainty interval and state its assumptions; no group disparity claim from these 8 positives per group should be generalized.
