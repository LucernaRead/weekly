# Independent same-baseline / advance-width extent scan.
# For each text, advance box = [x (+anchor adjust), baseline-ascent, x+adv, baseline+descent] via PIL getlength/getmetrics.
# Flags: (a) two texts on the SAME baseline whose advance boxes overlap horizontally;
# (b) same-baseline neighbours with 0<=gap<5px (tight, listed not failed unless overlap).
# Also: text advance box vs later/earlier rect borders crossing (for P7 box context, reported separately).
import re, html, os, sys, json
sys.path.insert(0,'/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import tables as T
from occlusion_audit import get_font, fnum, parse_attrs
FONTS=T.load()["fonts"]
def adv_box(text, family, size, bold, x, y, anchor):
    f=get_font(family,size,bold)
    adv=f.getlength(text)/4
    asc,desc=[v/4 for v in f.getmetrics()]
    if anchor=="middle": l=x-adv/2; r=x+adv/2
    elif anchor=="end": l=x-adv; r=x
    else: l=x; r=x+adv
    return (l, y-asc, r, y+desc)
for label,base in [('core','/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg'),('ed','/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-en/svg')]:
    tot_overlap=0; tot_tight=0
    print('==',label)
    for fn in sorted(os.listdir(base)):
        s=open(os.path.join(base,fn),encoding='utf-8').read()
        items=[]
        for m in re.finditer(r"<text([^>]*)>(.*?)</text>",s,re.S):
            a=parse_attrs(m.group(1)); t=html.unescape(re.sub(r"<[^>]+>","",m.group(2)))
            if not t.strip(): continue
            items.append((fnum(a,'y'), adv_box(t,a.get('font-family',''),fnum(a,'font-size',20),a.get('font-weight','') in ('700','bold'),fnum(a,'x'),fnum(a,'y'),a.get('text-anchor','start')), t))
        from collections import defaultdict
        groups=defaultdict(list)
        for y,b,t in items: groups[round(y,2)].append((b,t))
        ov=[]; tight=[]
        for y, lst in groups.items():
            lst.sort(key=lambda z: z[0][0])
            for (b1,t1),(b2,t2) in zip(lst,lst[1:]):
                gap=b2[0]-b1[2]
                if gap<0: ov.append((y,t1[:30],t2[:30],round(gap,1)))
                elif gap<5: tight.append((y,t1[:30],t2[:30],round(gap,1)))
        print(f' {fn}: same-baseline overlaps={len(ov)} tight-gaps(<5px)={len(tight)}')
        for o in ov: print('   OVERLAP',o)
        for t in tight: print('   TIGHT',t)
        tot_overlap+=len(ov); tot_tight+=len(tight)
    print(f' TOTAL {label}: overlaps={tot_overlap} tight={tot_tight}')
