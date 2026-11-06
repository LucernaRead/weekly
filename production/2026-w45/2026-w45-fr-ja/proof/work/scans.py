import sys, re
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import occlusion_audit as oa
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-ja/svg/'
CO='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg/'
pages=['p1-une.svg','p2-vie.svg','p3-culture.svg','p4-sport.svg','p5-jeunesse.svg','p6-politique.svg','p7-langue.svg','p8-exercices.svg']
def load(base,pg): return oa.parse_svg(open(base+pg,encoding='utf-8').read())[0]
COLS=[65,527,989,1451]
print('=== ORPHAN scan window [10,45), cols, consecutive baselines<=60, runs>=2 ===')
for pg in pages:
    for label,base in [('ED',ED),('CO',CO)]:
        els=load(base,pg); ts=[e for e in els if e.kind=='text' and e.box]
        for col in COLS:
            colts=sorted([e for e in ts if abs(float(e.attrs.get('x',-999))-col)<1.0], key=lambda e:e.baseline)
            # runs: consecutive with gap<=60
            runs=[]; cur=[colts[0]] if colts else []
            for e in colts[1:]:
                if e.baseline-cur[-1].baseline<=60: cur.append(e)
                else: runs.append(cur); cur=[e]
            if cur: runs.append(cur)
            for run in runs:
                if len(run)>=2:
                    last=run[-1]; w=last.box[2]-last.box[0]
                    if 10<=w<45:
                        print(pg,label,'col',col,'final-baseline',round(last.baseline,1),'width',round(w,1),repr(last.text))
print('=== LINE-START scan ===')
# NO_START from JA svglib
import re as _re
sv=open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-ja-build/svglib.py',encoding='utf-8').read()
m=_re.search(r'NO_START\s*=\s*(\{[^}]*\}|set\([^)]*\))', sv)
print('svglib NO_START def found:', bool(m), m.group(0)[:300] if m else '')
NO_START=set('、。,.・）〕］｝」』】〉》!?‼⁇⁈⁉:;：；…―ー〜') | set('ゃゅょぁぃぅぇぉっゎ')
for pg in pages:
    for label,base in [('ED',ED)]:
        els=load(base,pg)
        for e in els:
            if e.kind=='text' and e.text and e.text[0] in NO_START:
                print(pg,label,round(e.baseline,1),repr(e.text[:50]))
print('=== SAME-BASELINE TEXTX (same y, ink overlap/gap<0) ===')
for pg in pages:
    els=load(ED,pg); ts=[e for e in els if e.kind=='text' and e.box]
    from collections import defaultdict
    byy=defaultdict(list)
    for e in ts: byy[round(e.baseline,2)].append(e)
    for y,grp in byy.items():
        grp=sorted(grp,key=lambda e:e.box[0])
        for a,b in zip(grp,grp[1:]):
            gap=b.box[0]-a.box[2]
            if gap<2: print(pg,'y',y,'gap',round(gap,1),repr(a.text[:40]),'||',repr(b.text[:40]))
print('=== LATIN SPLIT detector ===')
vocab=set()
for base in [ED,CO]:
    for pg in pages:
        for e in load(base,pg):
            if e.kind=='text':
                for tok in re.findall(r"[A-Za-zÀ-ÿ]+(?:['’][A-Za-zÀ-ÿ]+)?", e.text): vocab.add(tok.lower())
print('vocab size', len(vocab))
for pg in pages:
    els=load(ED,pg); ts=[e for e in els if e.kind=='text' and e.box]
    for col in COLS:
        colts=sorted([e for e in ts if abs(float(e.attrs.get('x',-999))-col)<1.0], key=lambda e:e.baseline)
        for a,b in zip(colts,colts[1:]):
            if b.baseline-a.baseline>60: continue
            fa=re.findall(r"[A-Za-zÀ-ÿ]+", a.text); fb=re.findall(r"[A-Za-zÀ-ÿ]+", b.text)
            if not fa or not fb: continue
            x,y=fa[-1].lower(), fb[0].lower()
            if x+y in vocab and x not in vocab and y not in vocab:
                print(pg,'col',col,round(a.baseline,1),repr(a.text[-40:]),'||',repr(b.text[:40]),'->',x+y)
print('=== P6 CHART coverage (later rect vs chart text ink) ===')
for label,base in [('ED',ED),('CO',CO)]:
    els=load(base,'p6-politique.svg')
    # chart texts: heuristic - texts in P6 chart area: all texts; report any covered >0% by later opaque rect
    n=0; mx=0; worst=None
    for i,e in enumerate(els):
        if e.kind!='text' or not e.box: continue
        area=(e.box[2]-e.box[0])*(e.box[3]-e.box[1])
        if area<=0: continue
        for f in els[i+1:]:
            if f.kind=='rect' and oa.is_opaque(f) and f.box:
                ov,wh=oa.overlap(e.box,f.box)
                if ov>0:
                    cov=ov/area; n+=1
                    if cov>mx: mx=cov; worst=(round(e.baseline,1),e.text[:40],round(cov,3))
    print('P6',label,'texts with any later-rect overlap:',n,'max coverage',round(mx,4),worst)
print('=== OVERFLOW in repro render logs ===')
for f in ['repro-render.log','repro-render2.log']:
    t=open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-ja-proof/work/'+f,encoding='utf-8').read()
    print(f,'OVERFLOW',t.count('OVERFLOW'),'HEAD TOO WIDE',t.count('HEAD TOO WIDE'),'TOTAL exercises line:', 'TOTAL exercises: 150' in t)
