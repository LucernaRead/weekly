import re, os, glob
from PIL import ImageFont
FONTS_DIR="/usr/share/fonts/opentype/noto"
def sc_index(path):
    for i in range(12):
        try:
            f=ImageFont.truetype(path,40,index=i)
            if f.getname()[0].endswith("SC"): return i
        except Exception: break
    return 0
SERIF=FONTS_DIR+"/NotoSerifCJK-Regular.ttc"; SERIF_B=FONTS_DIR+"/NotoSerifCJK-Bold.ttc"
SANS=FONTS_DIR+"/NotoSansCJK-Regular.ttc"; SANS_B=FONTS_DIR+"/NotoSansCJK-Bold.ttc"
IDX={p:sc_index(p) for p in (SERIF,SERIF_B,SANS,SANS_B)}
def font(kind,bold,size):
    path={"serif":SERIF_B if bold else SERIF,"sans":SANS_B if bold else SANS}[kind]
    return ImageFont.truetype(path,int(round(size)),index=IDX[path])
def parse(dire,f):
    s=open(dire+'/'+f,encoding='utf-8').read()
    els=[]
    for m in re.finditer(r'<text\s+([^>]*)>([^<]*)</text>', s):
        a,t=m.group(1),m.group(2)
        def g(n):
            mm=re.search(n+r'="([^"]*)"',a); return mm.group(1) if mm else None
        if g('x') and g('y') and g('font-size'):
            els.append({'x':float(g('x')),'y':float(g('y')),'fam':g('font-family') or '','size':float(g('font-size')),'bold':g('font-weight')=='700','anchor':g('text-anchor') or 'start','text':t})
    rects=[]
    for m in re.finditer(r'<rect\s+([^>]*)/?>', s):
        a=m.group(1)
        def g(n):
            mm=re.search(n+r'="([^"]*)"',a); return mm.group(1) if mm else None
        if g('x') and g('y') and g('width') and g('height'):
            rects.append({'x':float(g('x')),'y':float(g('y')),'w':float(g('width')),'h':float(g('height')),'fill':g('fill') or '','stroke':g('stroke') or ''})
    return s,els,rects
def inkbox(e):
    kind='serif' if 'Serif' in e['fam'] else 'sans'
    f=font(kind,e['bold'],e['size'])
    anch={'start':'ls','middle':'ms','end':'rs'}[e['anchor']]
    l,t,r,b=f.getbbox(e['text'],anchor=anch)
    return (e['x']+l, e['y']+t, e['x']+r, e['y']+b)
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-ko/svg'
CORE='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-core/svg'
print("=== SVG root ===")
for f in ['p1-voorpagina.svg']:
    s,_,_=parse(ED,f); print(s[:300])
print()
print("=== 1. SAME-BASELINE ink collisions (>1.5px) ED vs CORE ===")
for dire,label in [(ED,'ED'),(CORE,'CORE')]:
    print('--',label)
    for f in sorted(os.listdir(dire)):
        _,els,_=parse(dire,f)
        rows={}
        for e in els:
            if e['text'].strip(): rows.setdefault(e['y'],[]).append(e)
        for y,items in rows.items():
            boxes=[(inkbox(e),e['text']) for e in items]
            for i in range(len(boxes)):
                for j in range(i+1,len(boxes)):
                    (x0a,ya,x1a,yb),sa=boxes[i]; (x0b,yc,x1b,yd),sb=boxes[j]
                    ov=min(x1a,x1b)-max(x0a,x0b); voy=min(yb,yd)-max(ya,yc)
                    if ov>1.5 and voy>0:
                        print(f'  COLL {f} y={y} overlap={ov:.1f} :: {sa[:40]!r} vs {sb[:40]!r}')
print()
print("=== 2. P6 chart-label coverage (baseline-anchored) ===")
s,els,rects=parse(ED,'p6-verdieping.svg')
# ordered events: need document order; reparse in order
txt=open(ED+'/p6-verdieping.svg',encoding='utf-8').read()
events=[]
for m in re.finditer(r'<(text|rect)\b([^>]*)>([^<]*)?</', txt):
    kind,attrs=m.group(1),m.group(2)
    if kind=='rect':
        def g(n):
            mm=re.search(n+r'="([^"]+)"',attrs); return mm.group(1) if mm else None
        if g('x') and g('y') and g('width') and g('height'):
            events.append(('rect',(float(g('x')),float(g('y')),float(g('width')),float(g('height')))))
    else:
        def g(n):
            mm=re.search(n+r'="([^"]+)"',attrs); return mm.group(1) if mm else None
        if g('x') and g('y') and g('font-size'):
            events.append(('text',(float(g('x')),float(g('y')),'serif' if g('font-family') and 'Serif' in g('font-family') else 'sans',float(g('font-size')),g('font-weight')=='700',g('text-anchor') or 'start',m.group(3) or '')))
LABELS=("Ik blijf thuis","Ik kijk eerst naar de tekst","Ik ga toch naar buiten","Ik weet het niet","45","25","20","10")
worst=0
for idx,(k,v) in enumerate(events):
    if k!='text': continue
    x,y,kind,size,bold,anchor,t=v
    if t not in LABELS: continue
    f=font(kind,bold,size); anch={'start':'ls','middle':'ms','end':'rs'}[anchor]
    l,tt,r,b=f.getbbox(t,anchor=anch); ib=(x+l,y+tt,x+r,y+b); area=max(0.0,(r-l)*(b-tt))
    cov=0.0
    for k2,rv in events[idx+1:]:
        if k2!='rect': continue
        rx,ry,rw,rh=rv
        ix=max(0.0,min(ib[2],rx+rw)-max(ib[0],rx)); iy=max(0.0,min(ib[3],ry+rh)-max(ib[1],ry))
        if area: cov=max(cov,ix*iy/area)
    worst=max(worst,cov)
    print(f'  label {t!r} ink={[round(vv,1) for vv in ib]} coverage={cov*100:.1f}%')
print(f'  WORST={worst*100:.1f}% (pass <30%)')
print()
print("=== 3. Box-title widths P1/P6 final ===")
for f,title in [('p1-voorpagina.svg','DE WEEK IN CIJFERS'),('p6-verdieping.svg','VOOR OF TEGEN?')]:
    s,els,rects=parse(ED,f)
    for e in els:
        if e['text'].startswith(title):
            ib=inkbox(e)
            print(f'  {f} title {e["text"]!r} size={e["size"]} ink_left={ib[0]:.1f} ink_right={ib[2]:.1f} ink_width={ib[2]-ib[0]:.1f}')
            # candidate containing boxes: rects whose y-span contains title y and x-span contains title x-range
            for r in rects:
                if r['y']<=e['y']<=r['y']+r['h'] and r['x']<=ib[0] and ib[2]<=r['x']+r['w']+50:
                    print(f'    containing rect x={r["x"]} y={r["y"]} w={r["w"]} h={r["h"]} right={r["x"]+r["w"]:.1f} fill={r["fill"]} stroke={r["stroke"]}')
print()
print("=== 4. Frame / right-edge scan (all pages) ===")
for f in sorted(os.listdir(ED)):
    s,els,rects=parse(ED,f)
    frames=[r for r in rects if r['w']>1500]
    frames_sorted=sorted(set(round(r['x']+r['w'],1) for r in frames))
    maxr=0; flags=[]
    for e in els:
        if not e['text'].strip(): continue
        ib=inkbox(e); maxr=max(maxr,ib[2])
        for r in frames:
            fr=r['x']+r['w']
            if ib[2]>fr+0.01 and r['y']<=e['y']<=r['y']+r['h']:
                flags.append((e['text'][:40],round(ib[2],1),round(fr,1),'past-frame'))
            if ib[0]<fr<ib[2] and r['y']<=e['y']<=r['y']+r['h']:
                flags.append((e['text'][:40],round(ib[0],1),round(ib[2],1),'crosses-frame-edge '+str(fr)))
        if ib[2]>1950: flags.append((e['text'][:40],round(ib[2],1),1950,'past-page-edge'))
        if ib[0]<0: flags.append((e['text'][:40],round(ib[0],1),0,'past-left-edge'))
    print(f'  {f} frames(right)={frames_sorted} max_ink_right={maxr:.1f} flags={flags}')
