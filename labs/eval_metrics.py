"""Offline, synthetic evaluation demonstration. No personal data or dependencies."""
import argparse
import csv
from pathlib import Path

DATA = Path(__file__).parent / 'data' / 'synthetic_outreach.csv'

def safe_rate(numerator, denominator):
    return None if denominator == 0 else numerator / denominator

def evaluate(rows, threshold=0.5):
    if not 0 <= threshold <= 1:
        raise ValueError('threshold must be within [0, 1]')
    counts = {}
    for r in rows:
        actual = int(r['actual']); score = float(r['score'])
        if actual not in (0, 1) or not 0 <= score <= 1:
            raise ValueError('invalid synthetic row')
        group = r['group']
        for name in ('all', group):
            c = counts.setdefault(name, dict(tp=0, fp=0, tn=0, fn=0))
            predicted = int(score >= threshold)
            label = ('tp' if actual else 'fp') if predicted else ('fn' if actual else 'tn')
            c[label] += 1
    result = {}
    for name,c in counts.items():
        tp,fp,tn,fn = (c[x] for x in ('tp','fp','tn','fn'))
        result[name] = dict(**c, n=tp+fp+tn+fn,
                            precision=safe_rate(tp,tp+fp), recall=safe_rate(tp,tp+fn),
                            fnr=safe_rate(fn,tp+fn), fpr=safe_rate(fp,fp+tn),
                            accuracy=safe_rate(tp+tn,tp+fp+tn+fn))
    return result

def read_data(path=DATA):
    with Path(path).open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--threshold',type=float,default=0.5)
    a=p.parse_args()
    for group, m in sorted(evaluate(read_data(),a.threshold).items()):
        rates = ' '.join(f'{x}={m[x]:.3f}' if m[x] is not None else f'{x}=undefined' for x in ('precision','recall','fnr','fpr','accuracy'))
        print(f'{group:8} n={m["n"]:2} TP={m["tp"]} FP={m["fp"]} TN={m["tn"]} FN={m["fn"]} {rates}')
    print('These 32 invented records are for practicing arithmetic only; no generalization or causal claim follows.')
if __name__=='__main__': main()
