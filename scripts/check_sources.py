"""Source catalog link check; remote mode only flags confirmed 404/410, reports blocks."""
import argparse
import csv
import urllib.error
import urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def remote_status(url):
    req=urllib.request.Request(url,headers={'User-Agent':'OpenCurriculumLinkCheck/0.1 (+GitHub educational project)'})
    try:
        with urllib.request.urlopen(req,timeout=18) as r:return r.status, r.geturl()
    except urllib.error.HTTPError as e:
        return e.code,url
    except (urllib.error.URLError,TimeoutError,OSError) as e:
        return None,type(e).__name__

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--remote',action='store_true',help='check public pages; uses network')
    args=p.parse_args()
    rows=list(csv.DictReader((ROOT/'shared/resources.csv').open(encoding='utf-8')))
    missing=[]; uncertain=[]
    for row in rows:
        if not row['url'].startswith('https://'):
            missing.append((row['id'],'invalid URL'))
            continue
        if args.remote:
            code,detail=remote_status(row['url'])
            if code in (404,410):missing.append((row['id'],f'HTTP {code} {detail}'))
            elif code is None or code in (401,403,429) or (code and code>=500):
                uncertain.append((row['id'],f'{code or "network error"} {detail}'))
            print(f'{row["id"]:12} {code or "?"} {detail}')
    print(f'Catalog: {len(rows)} links; confirmed missing: {len(missing)}; manual review: {len(uncertain)}')
    for k,v in uncertain:print('REVIEW',k,v)
    for k,v in missing:print('MISSING',k,v)
    return int(bool(missing))
if __name__=='__main__':raise SystemExit(main())
