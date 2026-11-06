import json, re, xml.etree.ElementTree as ET
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
NO_START_KO=set("。、，．！？：；）」』】ー…‥・)]}〉》.,!?%:;\"")
NO_END=set("「『（【〈《([{\"")
SMALL_KANA=set("ぁぃぅぇぉゃゅょっァィゥェォャュョッ")
JA_CLOSERS=set("、。！？：；）」』】ー…‥・")
HANG=re.compile(r"[\uac00-\ud7af]")
def texts(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.endswith('text'):
            out.append((float(el.get('x')), float(el.get('y')), ''.join(el.itertext())))
    return out
pages=["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"]
COLBANDS=[(65,499),(527,961),(989,1423),(1451,1885)]
tot=0
for i,p in enumerate(pages,1):
    nodes=[(x,y,t) for x,y,t in texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg") if t.strip()]
    pairs=0; flags=[]
    for ci,(lo,hi) in enumerate(COLBANDS):
        col=sorted([(y,t) for x,y,t in nodes if lo<=x<=hi])
        for (y1,t1),(y2,t2) in zip(col,col[1:]):
            if 10<=y2-y1<=45:
                pairs+=1
                if t2[0] in NO_START_KO or t2[0] in SMALL_KANA: flags.append((ci,y2,t2[:30]))
                if t1[-1] in NO_END: flags.append((ci,y1,"END-OPENER "+t1[-20:]))
    ja=[(x,y,t[:30]) for x,y,t in nodes if t[0] in JA_CLOSERS or t[0] in SMALL_KANA]
    print(f"p{i}: band pairs={pairs} window flags={len(flags)} {flags[:3]} | JA flags={len(ja)} {ja[:3]}")
    tot+=pairs
print(f"TOTAL band pairs={tot}")
# wrap analysis, exact head/tail definition
calls=[json.loads(l) for l in open(f"{BASE}/hidden_files/w45/ko-ja-proof/work/wrap-proof.log", encoding='utf-8')]
n_calls=len(calls); ls=[]; le=[]; ge=[]; lt=[]
for rec in calls:
    pre, post, orig = rec['pre'], rec['post'], rec['text']
    for a,b in zip(post,post[1:]):
        if b and b[0] in NO_START_KO: ls.append((a[-20:],b[:20]))
        if a and a[-1] in NO_END: le.append((a[-20:],b[:20]))
    # nospace space-after map
    nxt={}; cnt=0; chs=list(orig)
    for j,ch in enumerate(chs):
        if ch==' ': continue
        nxt[cnt]=(chs[j+1]==' ' if j+1<len(chs) else True); cnt+=1
    pos=0
    for a,b in zip(pre,pre[1:]):
        pos+=len(re.sub(r"\s+","",a))
        tail=""
        k=0
        while k<len(b) and HANG.match(b[k]): tail+=b[k]; k+=1
        head=""
        k=len(a)-1
        while k>=0 and HANG.match(a[k]): head=a[k]+head; k-=1
        if head and tail and nxt.get(pos-1) is False:
            if len(tail)>=3: ge.append((a[-20:],b[:20],len(tail)))
            else: lt.append((a[-20:],b[:20],len(tail)))
print(f"wrap calls={n_calls} POST start={len(ls)} POST end={len(le)} midword>=3={len(ge)} {ge[:5]} midword1-2={len(lt)} {lt[:5]}")
# bracket boundaries in POST (rendered form): line ends with opener or starts with closer
br=[]
for rec in calls:
    for a,b in zip(rec['post'],rec['post'][1:]):
        if a and a[-1] in NO_END: br.append(('END-OPEN',a[-20:],b[:20]))
        if b and b[0] in set("」』）】〉》)]}"): br.append(('START-CLOSE',a[-20:],b[:20]))
print(f"POST bracket boundaries: {len(br)} {br[:5]}")
