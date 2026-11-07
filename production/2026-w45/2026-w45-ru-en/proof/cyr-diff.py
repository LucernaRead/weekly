import re, html, os, json
from collections import Counter
CORE='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg'
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-en/svg'
TEXT_RE=re.compile(r"<text[^>]*>(.*?)</text>",re.S)
CYR=re.compile(r"[А-Яа-яЁё]+")
def tokens(d,fn):
    s=open(os.path.join(d,fn),encoding='utf-8').read()
    texts=[html.unescape(re.sub(r"<[^>]+>","",c)) for c in TEXT_RE.findall(s)]
    c=Counter()
    for t in texts: c.update(CYR.findall(t))
    return c, texts
out={}
for fn in sorted(os.listdir(CORE)):
    if not fn.endswith('.svg'): continue
    cc,_=tokens(CORE,fn); ec,_=tokens(ED,fn)
    diff_c=cc-ec; diff_e=ec-cc
    print(fn, 'core_total',sum(cc.values()),'ed_total',sum(ec.values()),'only_core',dict(diff_c),'only_ed',dict(diff_e))
    out[fn]={'core_total':sum(cc.values()),'ed_total':sum(ec.values()),'only_core':dict(diff_c),'only_ed':dict(diff_e)}
json.dump(out,open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ru-en-proof/cyr-diff.json','w'),ensure_ascii=False,indent=1)
# P1 subtitle line check: which texts contain badge vs subtitle
for label,d in [('core',CORE),('ed',ED)]:
    _,texts=tokens(d,'p1-pervaya.svg')
    print(label,'p1 subtitle/badge candidates:',[t for t in texts if 'ЕЖЕНЕДЕЛЬНАЯ' in t or 'TEXT IN RUSSIAN' in t])
# contents Стр.8 row check
for label,d in [('core',CORE),('ed',ED)]:
    s=open(os.path.join(d,'p1-pervaya.svg'),encoding='utf-8').read()
    texts=[html.unescape(re.sub(r"<[^>]+>","",c)) for c in TEXT_RE.findall(s)]
    # print neighbours of Стр. 8
    for i,t in enumerate(texts):
        if t.strip()=='Стр. 8':
            print(label,'contents around Стр8:',texts[max(0,i-3):i+4])
