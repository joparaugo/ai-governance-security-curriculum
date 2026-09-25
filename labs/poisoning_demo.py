"""Tiny local nearest-neighbor label integrity exercise; no external ML package."""
# Features are fabricated positions, labels are fabricated outcomes.
TRAIN=[(0.0,0,'A'),(0.2,0,'B'),(0.4,0,'C'),(0.6,1,'D'),(0.8,1,'E')]

def predict(rows, target=0.7, k=3):
    nearest=sorted(rows,key=lambda r:(abs(r[0]-target),r[2]))[:k]
    return int(sum(r[1] for r in nearest) >= (k//2+1)), [r[2] for r in nearest]

def main():
    clean,neighbors=predict(TRAIN)
    changed=[(x, 0 if ident=='D' else label, ident) for x,label,ident in TRAIN]
    tainted,neighbors2=predict(changed)
    print('clean:',clean,'neighbors:',neighbors)
    print('single unauthorized label change, D:',tainted,'neighbors:',neighbors2)
    print('Interpretation: this constructed edge case is a sensitivity example, not a realistic attack-rate estimate.')
if __name__=='__main__': main()
