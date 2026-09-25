"""Offline repository integrity: files, internal Markdown links and source catalog."""
import csv
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]
LINK=re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')

def validate():
    errors=[]
    catalog=list(csv.DictReader((ROOT/'shared/resources.csv').open(encoding='utf-8')))
    ids=[r['id'] for r in catalog]
    if len(ids)<40 or len(ids)!=len(set(ids)):
        errors.append('resource IDs missing or duplicated')
    required={'CSA_CCM','CSA_CAIQ','CSA_STAR','CSA_STAR_AI','ATLAS','MITRE_ATTACK','MITRE_D3FEND','COSO_IC','COSO_ERM','COSO_GENAI','COBIT','IIA_THREE','SOC2','NIST_53A','IMDA_AGENT','AI_VERIFY','SLSA','SPDX_AI'}
    if required-set(ids):
        errors.append(f'core governance/security source families missing: {sorted(required-set(ids))}')
    for r in catalog:
        if not r['url'].startswith('https://'):
            errors.append(f'non-HTTPS resource: {r["id"]}')
        if not r['edition_status'] or not r['access']:
            errors.append(f'missing status/access: {r["id"]}')
    courses=sorted((ROOT/'courses').glob('[0-9][0-9]-*'))
    if len(courses)!=4:
        errors.append(f'expected four courses, got {len(courses)}')
    for course in courses:
        for f in ('README.md','syllabus.md','instructor-guide.md','assignments.md','assessments.md'):
            if not (course/f).is_file():errors.append(f'missing {course.name}/{f}')
        modules=sorted((course/'modules').glob('week-*.md'))
        slides=sorted((course/'slides').glob('week-*.md'))
        if len(modules)!=12 or len(slides)!=12:
            errors.append(f'{course.name}: expected 12 modules/decks; got {len(modules)}/{len(slides)}')
        for module in modules:
            data=module.read_text(encoding='utf-8')
            if '## 150-minute lesson plan' not in data or '## Student studio instructions' not in data:
                errors.append(f'incomplete lesson {module.relative_to(ROOT)}')
    with (ROOT/'shared/competency-map.csv').open(encoding='utf-8') as f:
        for outcome in csv.DictReader(f):
            for source in outcome['source_ids'].split(';'):
                if source not in ids:
                    errors.append(f'unknown competency source ID {source}')
    for doc in ROOT.rglob('*.md'):
        if '.git' in doc.parts:continue
        data=doc.read_text(encoding='utf-8')
        for match in LINK.finditer(data):
            target=match.group(1).split(' ',1)[0]
            u=urlsplit(target)
            if u.scheme in ('https','http','mailto'):continue
            if u.scheme or target.startswith('#'):continue
            path=(doc.parent/unquote(u.path)).resolve()
            if not path.is_file() or not path.is_relative_to(ROOT):
                errors.append(f'{doc.relative_to(ROOT)}: broken relative link {target}')
    return errors
if __name__=='__main__':
    errs=validate()
    if errs:
        print('\n'.join(errs));sys.exit(1)
    print('OK: four complete courses, resource IDs and local Markdown links')
