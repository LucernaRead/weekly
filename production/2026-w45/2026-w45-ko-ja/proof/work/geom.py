import sys, re, math
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/tools")
import xml.etree.ElementTree as ET
from PIL import ImageFont
import importlib.util
spec=importlib.util.spec_from_file_location("occ","/home/hatch/workspace/goals/lucernaread-social-media-operations/tools/occlusion_audit.py")
# occlusion_audit has module-level code but no main run on import? check: it defines functions; importing should be safe (argparse under __main__ presumably)
occ=importlib.util.module_from_spec(spec); spec.loader.exec_module(occ)
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def texts(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.endswith('text'):
            out.append((float(el.get('x')), float(el.get('y')), el.get('font-family',''), float(el.get('font-size',20)), el.get('font-weight','') in ('700','bold'), el.get('text-anchor','start'), ''.join(el.itertext())))
    return out
pages=["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"]
print("=== ADVANCE right-edge scan (threshold 1898) ===")
for i,p in enumerate(pages,1):
    mx=0; flags=[]
    for x,y,fam,size,bold,anchor,t in texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg"):
        f=occ.get_font(fam,size,bold); adv=f.getlength(t)/occ.SCALE
        right = x+adv if anchor=='start' else (x-adv if anchor=='end' else x+adv/2)
        mx=max(mx,right)
        if right>1898: flags.append((t[:40],round(right,2)))
    print(f"p{i}: max_adv_right={mx:.2f} flags>{1898}: {flags}")
print("=== same-baseline ink collision (overlap or gap<6px, same y rounded 0.01, x-ordered neighbours) ===")
for i,p in enumerate(pages,1):
    items=[]
    for x,y,fam,size,bold,anchor,t in texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg"):
        b=occ.ink_box(t,fam,size,bold,x,y,anchor)
        if b: items.append((y,b,t))
    from collections import defaultdict
    by=defaultdict(list)
    for y,b,t in items: by[round(y,2)].append((b,t))
    ov=[]; tight=[]
    for y, lst in by.items():
        lst.sort(key=lambda z: z[0][0])
        for (b1,t1),(b2,t2) in zip(lst,lst[1:]):
            gap=b2[0]-b1[2]
            if gap<0: ov.append((y,round(gap,2),t1[:30],t2[:30]))
            elif gap<6: tight.append((y,round(gap,2),t1[:30],t2[:30]))
    print(f"p{i}: overlaps={len(ov)} tight(<6px)={len(tight)}")
    for o in ov[:5]: print("   OV",o)
    for o in tight[:5]: print("   TIGHT",o)
print("=== P8 three calibers ===")
p8=texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p8-siheom.svg")
# last key node: the 150 line '150. ✓ ...' is a text node; find max-y text among key-flow? Use all texts: last baseline = max y among nodes starting with '150.'? plus ink bottom of that node
for x,y,fam,size,bold,anchor,t in p8:
    if t.strip().startswith('150.'): print(f"  150 node: x={x} y={y} size={size} bold={bold} anchor={anchor} text={t!r} ink={occ.ink_box(t,fam,size,bold,x,y,anchor)}")
# also last key-flow node overall (max y among numbered key lines?) print top-3 max y numbered nodes
num=[(y,t) for x,y,fam,size,bold,anchor,t in p8 if re.match(r'^\d+\.', t.strip())]
num.sort()
print("  last 3 numbered nodes by y:", num[-3:])
print("=== P7 boxes ===")
# parse rects/lines from p7 svg raw
raw=open(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p7-mal.svg", encoding='utf-8').read()
for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*>', raw):
    x,y,w,h=map(float,m.groups())
    if h>100: print(f"  rect x={x} y={y} w={w} h={h} bottom={y+h:.2f}")
for m in re.finditer(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"[^>]*>', raw):
    x1,y1,x2,y2=map(float,m.groups())
    if y1>1800: print(f"  line y={y1} x1={x1} x2={x2}")
# P7 letter-box texts: find texts with y in 1250..1870 in col3? col x ranges: print texts y>1200 sorted, with ink bottoms
p7=texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p7-mal.svg")
col3=[(x,y,t,occ.ink_box(t,fam,size,bold,x,y,anchor)) for x,y,fam,size,bold,anchor,t in p7 if x>1250]
col3.sort(key=lambda z: z[1])
print("  P7 col3 (x>1250) last 8 by y:")
for x,y,t,b in col3[-8:]: print(f"    y={y} ink_bottom={b[3]:.2f} :: {t[:60]!r}")
print("  P7 all texts y>2400 (teaser tail):")
for x,y,fam,size,bold,anchor,t in sorted(p7,key=lambda z:z[1]):
    if y>2400: print(f"    y={y} :: {t[:70]!r}")
# teaser box bottom: rects near bottom
print("=== P6 label coverage (baseline-anchored ink vs later rects) ===")
raw6=open(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p6-gipi.svg", encoding='utf-8').read()
# reuse occlusion parse: simpler - run occlusion tool already covers COVER; here compute max coverage of any text ink by any later rect (paint order)
sys.path.insert(0,"/home/hatch/workspace/goals/lucernaread-social-media-operations/tools")
# parse flat order with occ.TAG_RE
els=[]
for m in occ.TAG_RE.finditer(raw6):
    if m.group('tattrs') is not None:
        a=occ.parse_attrs(m.group('tattrs')); els.append(('text',a,m.group('tcontent')))
    else:
        a=occ.parse_attrs(m.group('attrs')); els.append((m.group('tag'),a,''))
maxcov=0; worst=None
for idx,(tag,a,content) in enumerate(els):
    if tag!='text': continue
    t=content
    if not t.strip(): continue
    size=occ.fnum(a,'font-size',20.0); bold=a.get('font-weight','') in ('700','bold')
    b=occ.ink_box(t,a.get('font-family',''),size,bold,occ.fnum(a,'x'),occ.fnum(a,'y'),a.get('text-anchor','start'))
    if not b: continue
    area=(b[2]-b[0])*(b[3]-b[1])
    if area<=0: continue
    for tag2,a2,_ in els[idx+1:]:
        if tag2!='rect': continue
        rx,ry,rw,rh=occ.fnum(a2,'x'),occ.fnum(a2,'y'),occ.fnum(a2,'width'),occ.fnum(a2,'height')
        fill=a2.get('fill','')
        if fill in ('none',): continue
        ix=max(0,min(b[2],rx+rw)-max(b[0],rx)); iy=max(0,min(b[3],ry+rh)-max(b[1],ry))
        cov=ix*iy/area
        if cov>maxcov: maxcov=cov; worst=(t[:40],round(cov,4),rx,ry,rw,rh)
print(f"  max text-ink coverage by later rect: {maxcov:.4f} worst={worst} (<0.30 gate)")
