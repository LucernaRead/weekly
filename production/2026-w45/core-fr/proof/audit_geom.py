# Read-only geometric supplement: same-baseline ink spacing + later-rect vs text (chart-area) check.
# Uses PIL/FreeType DejaVu approximations (same approach family as occlusion_audit); flags are candidates for adjudication, not verdicts.
import re, glob
from PIL import ImageFont
import os
def font(sz, bold):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"]:
        if os.path.exists(p): return ImageFont.truetype(p, int(sz))
    return ImageFont.load_default()
base='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg/'
for f in sorted(glob.glob(base+'*.svg')):
    data=open(f,encoding='utf-8').read()
    # ordered elements: text and rect/image in paint order
    elems=[]
    for m in re.finditer(r'<(text|rect|image)\b([^>]*?)(/>|>(.*?)</\1>)', data, re.S):
        tag,attrs=m.group(1),m.group(2)
        inner=m.group(4) or ''
        def num(a):
            mm=re.search(a+r'="([\d.]+)"',attrs); return float(mm.group(1)) if mm else 0
        if tag=='text':
            t=re.sub(r'<[^>]+>','',inner).strip()
            if not t: continue
            sz=num('font-size') or 20
            bold='700' in attrs or 'bold' in attrs
            try: w=font(sz,bold).getlength(t)
            except Exception: w=len(t)*sz*0.5
            x,y=num('x'),num('y')
            elems.append(('text',x,y-sz*0.8,x+w,y+sz*0.3,t))
        else:
            x,y,w,h=num('x'),num('y'),num('width'),num('height')
            if w and h: elems.append((tag,x,y,x+w,y+h,''))
    # same-baseline: group texts by rounded y, sort by x, report gap < 3px between consecutive ink boxes
    from collections import defaultdict
    byy=defaultdict(list)
    for e in elems:
        if e[0]=='text': byy[round(e[2])].append(e)
    same=[]
    for y,ts in byy.items():
        ts.sort(key=lambda e:e[1])
        for a,b in zip(ts,ts[1:]):
            gap=b[1]-a[3]
            if gap<3: same.append((y,a[5][:40],b[5][:40],round(gap,1)))
    # later-rect vs earlier text: any overlap (candidate; containing boxes drawn BEFORE text don't count)
    later=[]
    for i,e in enumerate(elems):
        if e[0] in ('rect','image'):
            for t in elems[:i]:
                if t[0]!='text': continue
                if e[1]<t[3] and e[3]>t[1] and e[2]<t[4] and e[4]>t[2]:
                    # overlap area fraction of text box
                    ox=min(e[3],t[3])-max(e[1],t[1]); oy=min(e[4],t[4])-max(e[2],t[2])
                    frac=(ox*oy)/max(1,(t[3]-t[1])*(t[4]-t[2]))
                    later.append((e[0],t[5][:40],round(frac,2)))
    print('==',f.split('/')[-1],'same-baseline gaps<3px:',len(same))
    for s in same: print('   SAME',s)
    print('   later-shape vs text overlaps:',len(later))
    # only print overlaps where shape is NOT a full containing box (frac<0.95) to focus on grazes
    for l in later:
        if l[2]<0.95: print('   GRAZE?',l)
