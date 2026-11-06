# Independent dash-parse: use p8.py's extract to get segments (lines parse), then
# split each segment on FIRST " — " and compare printed keys byte-for-byte.
# Also print full segments for 83,137,138,139,140,148,150 in both editions.
import sys, json
sys.path.insert(0,'/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
from p8 import extract
CORE='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg/p8-test.svg'
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-en/svg/p8-test.svg'
ref, rh = extract(CORE,150); res, h = extract(ED,150)
print('parse:',rh,h)
def dashkey(seg):
    seg=seg.strip()
    if seg.startswith('✓'):
        return '✓'
    if ' — ' in seg:
        return seg.split(' — ',1)[0].strip()
    return seg  # no dash: whole segment is key (bare)
diffs=[]; notediff=[]
for n in range(1,151):
    ck, ek = dashkey(ref[n]['seg']), dashkey(res[n]['seg'])
    if ck!=ek: diffs.append(n)
    # note-only check: segment minus key must differ only in note part; report seg for diffs
print('dash-parse keydiff:',diffs)
for n in [83,137,138,139,140,148,150]:
    print(f"--- {n} CORE seg: {ref[n]['seg']!r}")
    print(f"    CORE dashkey: {dashkey(ref[n]['seg'])!r} method={ref[n]['method']} p8key={ref[n]['key']!r}")
    print(f"--- {n} ED   seg: {res[n]['seg']!r}")
    print(f"    ED   dashkey: {dashkey(res[n]['seg'])!r} method={res[n]['method']} p8key={res[n]['key']!r}")
    print(f"    dashkeys equal: {dashkey(ref[n]['seg'])==dashkey(res[n]['seg'])}")
# 139/140 byte-identical dashkeys?
# 150 word count: model text in section H - find in p8 svg texts
import re, html
for label,path in [('core',CORE),('ed',ED)]:
    s=open(path,encoding='utf-8').read()
    texts=[html.unescape(re.sub(r"<[^>]+>","",c)) for c in re.findall(r"<text[^>]*>(.*?)</text>",s,re.S)]
    # section H model: look for texts after 'H' header? Print candidates containing model markers
    for i,t in enumerate(texts):
        if '84 words' in t or '84 слов' in t or 'Model text' in t or 'Образец' in t:
            print(label,'model-note idx',i,repr(t))
    # Also dump all texts near end (section H area) - find 'H ' headers
    print(label,'total texts',len(texts))
json.dump({'dash_keydiff':diffs},open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ru-en-proof/dash-parse.json','w'),ensure_ascii=False,indent=1)
