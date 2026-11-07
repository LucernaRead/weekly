import re, pathlib, html, json
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def load(path):
    s=path.read_text()
    return [html.unescape(re.sub(r'<[^>]+>','',c)).strip() for c in re.findall(r"<text[^>]*>(.*?)</text>", s, flags=re.S)]
def dash_parse(path):
    ts=load(path)
    # answers start at first separator header
    start=next(i for i,t in enumerate(ts) if re.match(r'^—\s*.*\d.*—$', t))
    els=ts[start:-2]  # drop footers, same boundary as tool (for comparability of segment set only)
    # split into segments by "N. " markers in element order; wrapped continuations join with space
    segs={}; cur=None; buf=''
    for t in els:
        m=re.match(r'^(\d+)\.\s+(.*)$', t)
        if m:
            if cur is not None: segs[cur]=buf.strip()
            cur=int(m.group(1)); buf=m.group(2)
        elif cur is not None:
            if re.match(r'^—\s*.*\d.*—$', t):
                segs[cur]=buf.strip(); cur=None; buf=''
            else:
                buf += ' ' + t
    if cur is not None: segs[cur]=buf.strip()
    keys={}
    for n,seg in segs.items():
        if seg.startswith('✓'):
            keys[n]='✓'
        elif ' — ' in seg:
            keys[n]=seg.split(' — ',1)[0].strip()
        else:
            keys[n]=seg
    return segs, keys
res={}
for label,f in [('core','files/weekly-report-w45-ru-core/svg/p8-test.svg'),('ed','files/weekly-report-w45-ru-fr/svg/p8-test.svg')]:
    segs,keys=dash_parse(base/f)
    res[label]=(segs,keys)
    print(label,'segments',len(segs),'nums',min(segs),max(segs),'missing',[n for n in range(1,151) if n not in segs])
    for n in [83,137,138,139,140,148,150]:
        print(f"  {n}: key={keys[n]!r} seg={segs[n][:160]!r}")
csegs,ckeys=res['core']; esegs,ekeys=res['ed']
diffs=[n for n in range(1,151) if ckeys.get(n)!=ekeys.get(n)]
print('DASH-PARSE key diffs:',diffs)
for n in diffs: print(n,'core=',ckeys[n],'| ed=',ekeys[n])
# 150 model word count: find MODELO / model section in P8? Actually model text is in §H of P8 exercises area; check build content8 model string
import subprocess
print('--- p8 extract keys for comparison ---')
