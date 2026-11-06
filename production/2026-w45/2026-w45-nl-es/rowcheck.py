# Same-baseline advance-width spacing scan (README #10) + P6 chart label/bar check.
import re, sys, glob, os
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-nl-es-build')
from svglib import text_w
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-es/svg'
def parse(path):
    txt=open(path,encoding='utf-8').read()
    els=[]
    for m in re.finditer(r'<text x="([^"]*)" y="([^"]*)" font-family="([^"]*)" font-size="([^"]*)"(?: font-weight="([^"]*)")?(?: fill="[^"]*")?(?: text-anchor="([^"]*)")?>([^<]*)</text>', txt):
        x,y,fam,size,wt,anchor,t=m.groups()
        kind='sans' if 'Sans' in fam else 'serif'
        bold=(wt=='700')
        w=text_w(t,kind,bold,float(size))
        x=float(x)
        if anchor=='middle': x0=x-w/2
        elif anchor=='end': x0=x-w
        else: x0=x
        els.append((float(y),x0,x0+w,t))
    return els
issues=0
for path in sorted(glob.glob(ED+'/*.svg')):
    els=parse(path)
    by={}
    for y,x0,x1,t in els: by.setdefault(round(y,1),[]).append((x0,x1,t))
    for y,items in by.items():
        items.sort()
        for (a0,a1,ta),(b0,b1,tb) in zip(items,items[1:]):
            gap=b0-a1
            if gap < 4:
                print(f"{os.path.basename(path)} y={y} gap={gap:.1f} {ta[:50]!r} || {tb[:50]!r}"); issues+=1
print("same-baseline advance-gap<4px flags:", issues)
# P6 chart: rows from content56: labels at ix=1451+22=1473 baseline yy3+20, bars y=yy3+30 h=18 x=1473 w=bw; yy3 starts 216+58=274? recompute from code: yy3=216; title at yy3+26; yy3+=58 -> 274; rows at yy3+20 baseline, bar yy3+30.
# Instead verify geometrically from SVG: find bar rects (fill OLIVE #3e4c2a) in P6 col3 region and label texts; check label ink bottom < bar top.
txt=open(ED+'/p6-verdieping.svg',encoding='utf-8').read()
bars=re.findall(r'<rect x="1473" y="([^"]*)" width="(\d+)" height="18"[^>]*fill="#3e4c2a"', txt)
labels=[]
for m in re.finditer(r'<text x="1473" y="([^"]*)" font-family="[^"]*" font-size="19.5"[^>]*>([^<]*)</text>', txt):
    labels.append((float(m.group(1)),m.group(2)))
print("P6 bars (y, w):", bars)
print("P6 col3 label baselines:", labels)
for (by,bw),(ly,lt) in zip(bars,labels):
    by=float(by)
    ink_bottom=ly+19.5*0.30
    print(f"  label {lt[:30]!r} ink_bottom~{ink_bottom:.0f} bar_top={by:.0f} clearance={by-ink_bottom:.0f} {'OK' if by-ink_bottom>0 else 'OVERLAP'}")
