import sys, re
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import occlusion_audit as OA
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-de/svg/'
import glob
def parse(path):
    src=open(path,encoding='utf-8').read()
    els=[]
    for m in OA.TAG_RE.finditer(src):
        if m.group('tattrs') is not None:
            a=OA.parse_attrs(m.group('tattrs')); txt=OA.clean_text(m.group('tcontent'))
            e=OA.El('text', len(els), a, txt)
            size=OA.fnum(a,'font-size',20.0); bold=a.get('font-weight','') in ('700','bold')
            e.box=OA.ink_box(txt, a.get('font-family',''), size, bold, OA.fnum(a,'x'), OA.fnum(a,'y'), a.get('text-anchor','start'))
            e.baseline=OA.fnum(a,'y')
            els.append(e)
        else:
            a=OA.parse_attrs(m.group('attrs')); e=OA.El(m.group('tag'), len(els), a)
            e.box=OA.shape_box(e); els.append(e)
    return els
def overlap_area(b1,b2):
    x=max(0,min(b1[2],b2[2])-max(b1[0],b2[0])); y=max(0,min(b1[3],b2[3])-max(b1[1],b2[1])); return x*y
# 1. same-baseline collisions, all pages
for path in sorted(glob.glob(ED+'*.svg')):
    els=parse(path); texts=[e for e in els if e.kind=='text' and e.box]
    by={}
    for e in texts: by.setdefault(round(e.baseline,2),[]).append(e)
    bad=[]
    for y,grp in by.items():
        grp=sorted(grp,key=lambda e:e.box[0])
        for a,b in zip(grp,grp[1:]):
            gap=b.box[0]-a.box[2]
            if gap<3: bad.append((y,round(gap,1),a.text[:50],b.text[:50]))
    print(path.split('/')[-1], "same-baseline pairs gap<3px:", len(bad))
    for r in bad: print("   ",r)
# 2. P6 chart-label coverage by later rects (bbox-area upper bound)
els=parse(ED+'p6-verdieping.svg'); texts=[e for e in els if e.kind=='text' and e.box]
worst=[]
for i,e in enumerate(texts):
    area=(e.box[2]-e.box[0])*(e.box[3]-e.box[1])
    if area<=0: continue
    cov=0; coverer=None
    for f in els[i+1:]:
        if f.kind=='rect' and f.box:
            ov=overlap_area(e.box,f.box)/area
            if ov>cov: cov=ov; coverer=f.attrs
    if cov>0: worst.append((round(cov*100,1), e.text[:60], e.baseline, coverer))
worst.sort(key=lambda w: -w[0])
print("P6 max later-rect bbox coverage (upper bound):")
for w in worst[:8]: print("   ",w)
# 3. P1 graze geometry
els=parse(ED+'p1-voorpagina.svg')
for e in els:
    if e.kind=='text' and e.text and ('Klima' in e.text or 'IN HET KORT' in e.text or 'lange Zeit' in e.text):
        print("P1 TEXT:", round(e.baseline,1), e.box and tuple(round(v,1) for v in e.box), repr(e.text[:80]))
for e in els:
    if e.kind=='rect':
        b=e.box
        if b and 1800<b[1]<1950: print("P1 RECT near 1800-1950:", tuple(round(v,1) for v in b), e.attrs.get('fill'), e.attrs.get('stroke'))
    if e.kind=='line':
        b=e.box
        if b and 1800<b[1]<1900: print("P1 LINE:", tuple(round(v,1) for v in b))
