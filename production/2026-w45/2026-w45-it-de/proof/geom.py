from xml.etree import ElementTree as ET
from PIL import ImageFont
from collections import defaultdict
SERIF_R='/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc'
SERIF_B='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'
SANS_R='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
SANS_B='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
def font_for(fam, weight, size):
    if 'Serif' in fam:
        base = SERIF_B if weight=='700' else SERIF_R
    else:
        base = SANS_B if weight=='700' else SANS_R
    return ImageFont.truetype(base, int(round(float(size))), index=2)
def parse(path):
    t=ET.parse(path); els=[]
    for e in t.iter():
        if e.tag.endswith('text') and e.text: els.append(('text', e))
        elif e.tag.endswith('rect'): els.append(('rect', e))
    return els
pages=['p1-prima','p2-vita','p3-cultura','p4-sport','p5-giovani','p6-approfondimento','p7-lingua','p8-valutazione']
print("=== ADVANCE scan [40,1910] band ===")
tot=0
for pg in pages:
    els=parse(f'files/weekly-report-w45-it-de/svg/{pg}.svg'); flags=[]
    for kind,e in els:
        if kind!='text': continue
        x=float(e.get('x')); y=float(e.get('y')); fs=e.get('font-size'); fam=e.get('font-family',''); fw=e.get('font-weight','400'); ta=e.get('text-anchor','start')
        f=font_for(fam,fw,fs); L=f.getlength(e.text)
        if ta=='middle': x0,x1=x-L/2,x+L/2
        elif ta=='end': x0,x1=x-L,x
        else: x0,x1=x,x+L
        if x0<40 or x1>1910: flags.append((e.text[:40],round(x0,1),round(x1,1),round(y,1)))
    tot+=len(flags); print(f"  {pg}: {len(flags)} flags {flags[:6]}")
print(f"  TOTAL advance flags: {tot}")
print("=== Same-baseline scan ===")
for pg in pages:
    els=parse(f'files/weekly-report-w45-it-de/svg/{pg}.svg'); nodes=[]
    for kind,e in els:
        if kind!='text': continue
        x=float(e.get('x')); y=float(e.get('y')); fs=e.get('font-size'); fam=e.get('font-family',''); fw=e.get('font-weight','400'); ta=e.get('text-anchor','start')
        f=font_for(fam,fw,fs); L=f.getlength(e.text)
        x0=x-L/2 if ta=='middle' else x-L if ta=='end' else x
        nodes.append((round(y,1),x0,x0+L,e.text))
    byy=defaultdict(list)
    for y,x0,x1,tx in nodes: byy[y].append((x0,x1,tx))
    ovs=[]
    for y,items in byy.items():
        items.sort()
        for a,b in zip(items,items[1:]):
            if b[0]-a[1]<0: ovs.append((y,a[2][:30],b[2][:30],round(b[0]-a[1],1)))
    print(f"  {pg}: same-baseline overlaps={len(ovs)} {ovs[:5]}")
    band=sorted([(x0,x1,tx) for y,x0,x1,tx in nodes if abs(y-92)<1.5])
    if pg=='p1-prima': print(f"   P1 top band: {[(round(a,1),round(b,1),t) for a,b,t in band]} gaps={[round(band[i+1][0]-band[i][1],1) for i in range(len(band)-1)]}")
    ft=sorted([(x0,x1,tx) for y,x0,x1,tx in nodes if abs(y-2624)<1.5])
    print(f"   footer: {[(round(a,1),round(b,1),t[:28]) for a,b,t in ft]} gap={round(ft[1][0]-ft[0][1],1) if len(ft)>1 else None}")
print("=== P6 chart-label coverage ===")
els=parse('files/weekly-report-w45-it-de/svg/p6-approfondimento.svg')
seq=[]
for kind,e in els:
    if kind=='text' and e.text:
        x=float(e.get('x')); y=float(e.get('y')); fs=e.get('font-size'); fam=e.get('font-family',''); fw=e.get('font-weight','400'); ta=e.get('text-anchor','start')
        f=font_for(fam,fw,fs)
        bb=f.getbbox(e.text, anchor='ls')
        L=f.getlength(e.text)
        ax = x-L/2 if ta=='middle' else x-L if ta=='end' else x
        ink=(ax+bb[0], y+bb[1], ax+bb[2], y+bb[3])
        seq.append(('text',ink,e.text))
    elif kind=='rect':
        try: rx,ry,rw,rh=float(e.get('x',0)),float(e.get('y',0)),float(e.get('width',0)),float(e.get('height',0))
        except Exception: continue
        seq.append(('rect',(rx,ry,rx+rw,ry+rh),e.get('fill','')))
res=[]
for i,(kind,box,tx) in enumerate(seq):
    if kind!='text': continue
    ia=(box[2]-box[0])*(box[3]-box[1])
    if ia<=0: continue
    mx=0
    for kind2,box2,_ in seq[i+1:]:
        if kind2!='rect': continue
        ix=max(0,min(box[2],box2[2])-max(box[0],box2[0])); iy=max(0,min(box[3],box2[3])-max(box[1],box2[1]))
        mx=max(mx, ix*iy/ia)
    res.append((mx,tx,box))
res.sort(reverse=True)
print(f"  P6 max coverage overall: {res[0][0]*100:.1f}% on {res[0][1][:40]!r}")
for mx,tx,box in res[:8]: print(f"    {mx*100:.1f}% {tx[:40]!r} ink={[round(v,1) for v in box]}")
for mx,tx,box in res:
    if any(c in tx for c in ['Torino','Milano','Bologna','Roma','Napoli']): print(f"    city label {tx!r}: {mx*100:.1f}%")
print("=== Flow-end corroboration ===")
def tnodes(pg):
    out=[]
    for kind,e in parse(f'files/weekly-report-w45-it-de/svg/{pg}.svg'):
        if kind=='text' and e.text: out.append((float(e.get('x')),float(e.get('y')),e.get('font-size'),e.text))
    return out
keys=[n for n in tnodes('p8-valutazione') if 1400<n[1]<2600]
print(f"  P8 keys last node: {keys[-1]} (log end 2529)")
col3=[n for n in tnodes('p7-lingua') if n[0]>=1473 and n[1]<1686]
print(f"  P7 col3 last node: {col3[-1]} (log end 1673.0; FRASI rule 1686)")
ns6=tnodes('p6-approfondimento')
print(f"  P6 last nodes: {ns6[-3:]} (log P6-ex end 2569)")
ns1=tnodes('p1-prima')
print(f"  P1 x>=989,y<1830 last: {[n for n in ns1 if n[0]>=989 and n[1]<1830][-3:]} (log P1-headline end 1497)")
# footer advance widths
for pg in pages:
    ftn=[n for n in tnodes(pg) if abs(n[1]-2624)<1.5]
    print(f"  {pg} footer nodes: {ftn}")
