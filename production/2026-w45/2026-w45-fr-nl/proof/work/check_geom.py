import re, sys, json
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/tools")
from occlusion_audit import ink_box, get_font, SCALE
from pathlib import Path
BASE=Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
ATTR = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
RECT = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]*)"')
def texts(p):
    raw=p.read_text(encoding="utf-8"); out=[]
    for m in ATTR.finditer(raw):
        x,y,fam,fs,rest,s=float(m.group(1)),float(m.group(2)),m.group(3),float(m.group(4)),m.group(5),m.group(6)
        bold='font-weight="700"' in rest
        am=re.search(r'text-anchor="([^"]*)"',rest); anchor=am.group(1) if am else "start"
        out.append(dict(x=x,y=y,fam=fam,size=fs,bold=bold,anchor=anchor,s=s))
    return out,raw
def adv_end(e):
    f=get_font(e["fam"],e["size"],e["bold"]); adv=f.getlength(e["s"])/SCALE
    if e["anchor"]=="middle": return e["x"]+adv/2
    if e["anchor"]=="end": return e["x"]
    return e["x"]+adv
for label,d in [("ED",BASE/"weekly-report-w45-fr-nl/svg"),("CORE",BASE/"weekly-report-w45-fr-core/svg")]:
    print(f"===== {label} right-edge (ink_right>1885 or adv_end>1885) =====")
    for p in sorted(d.glob("*.svg")):
        for e in texts(p)[0]:
            ib=ink_box(e["s"],e["fam"],e["size"],e["bold"],e["x"],e["y"],e["anchor"])
            if ib is None: continue
            ae=adv_end(e)
            if ib[2]>1885 or ae>1885:
                print(f" {p.name} adv={ae:.2f} ink_right={ib[2]:.2f} y={e['y']} x={e['x']} {e['s'][:80]!r}")
    print(f"===== {label} same-baseline P1 y=92 + footers y=2624 =====")
    for p in sorted(d.glob("*.svg")):
        for yy in (92.0,2624.0):
            segs=[]
            for e in texts(p)[0]:
                if e["y"]==yy:
                    ib=ink_box(e["s"],e["fam"],e["size"],e["bold"],e["x"],e["y"],e["anchor"])
                    if ib: segs.append((ib[0],ib[2],e["s"][:60]))
            segs.sort()
            gaps=[round(segs[i+1][0]-segs[i][1],1) for i in range(len(segs)-1)]
            print(f" {p.name} y={yy}: {len(segs)} segs gaps={gaps}")
    print(f"===== {label} orphan scan window 10-45 =====")
    for p in sorted(d.glob("*.svg")):
        els=texts(p)[0]
        # blocks: same x/size/fam/bold? builder def: same page/x/size/family, consecutive y gaps in [10,45]
        els_sorted=sorted(els,key=lambda e:(e["x"],e["size"],e["fam"],e["y"]))
        blocks=[]; cur=[]
        for e in els_sorted:
            if cur and (e["x"],e["size"],e["fam"])==(cur[-1]["x"],cur[-1]["size"],cur[-1]["fam"]) and 10<=e["y"]-cur[-1]["y"]<=45:
                cur.append(e)
            else:
                if len(cur)>=2: blocks.append(cur)
                cur=[e]
        if len(cur)>=2: blocks.append(cur)
        for b in blocks:
            # line-start punct on non-first lines
            for e in b[1:]:
                s=e["s"].strip()
                if s and s[0] in ".,;:!?%)]}":
                    print(f" {p.name} LINESTART y={e['y']}: {s[:60]!r}")
            last=b[-1]["s"].strip()
            toks=last.split()
            if len(toks)==1 and len(toks[0])<=3:
                print(f" {p.name} SHORT-FINAL y={b[-1]['y']}: {last!r} (block {len(b)} lines)")
    print(f"===== {label} P8 calibers =====")
    p8,_=texts(d/"p8-exercices.svg")
    batt=[e for e in p8 if e["y"]<1526 and e["y"]>200]  # battery texts (exclude band head at 116? include? battery flow starts 194; head at 116 is band)
    batt2=[e for e in p8 if 194<=e["y"]<1526]
    ans=[e for e in p8 if e["y"]>=1838 and e["y"]<2580]
    for name,grp in [("battery(194-1526)",batt2),("answers(>=1838,excl footer)",ans)]:
        maxbase=max(e["y"] for e in grp)
        maxink=max(ink_box(e["s"],e["fam"],e["size"],e["bold"],e["x"],e["y"],e["anchor"])[3] for e in grp)
        print(f"  {name}: n={len(grp)} max_baseline={maxbase:.2f} max_ink_bottom={maxink:.2f} gap_to_2580={2580-maxink:.2f}")
        # also per-column max baseline
        for x in sorted(set(e["x"] for e in grp)):
            col=[e for e in grp if e["x"]==x]
            print(f"    col x={x}: n={len(col)} maxbase={max(e['y'] for e in col):.2f} maxink={max(ink_box(e['s'],e['fam'],e['size'],e['bold'],e['x'],e['y'],e['anchor'])[3] for e in col):.2f}")
    print(f"===== {label} P7 reader box + preview =====")
    p7,raw7=texts(d/"p7-langue.svg")
    rects=[(float(a),float(b),float(a)+float(c),float(b)+float(d),f) for a,b,c,d,f in RECT.findall(raw7)]
    print("  rects:",[(r) for r in rects if r[1]>1500 or r[3]>2000][:20])
    # reader box: find rect containing reader texts? print all rects with y>1800
    for r in rects:
        if r[1]>1700: print("   rect",r)
    # preview strip: texts with 'LA SEMAINE PROCHAINE' head y; find its y
    for e in p7:
        if "SEMAINE PROCHAINE" in e["s"]: print("  preview head",e)
    # last text ink bottom overall excl footer
    nonfoot=[e for e in p7 if e["y"]<2580]
    print(f"  P7 max ink bottom excl footer: {max(ink_box(e['s'],e['fam'],e['size'],e['bold'],e['x'],e['y'],e['anchor'])[3] for e in nonfoot):.2f} at baseline {max(nonfoot,key=lambda e:e['y'])['y']}")
    print(f"===== {label} P6 chart coverage =====")
    p6,raw6=texts(d/"p6-politique.svg")
    rects6=[(float(a),float(b),float(a)+float(c),float(b)+float(d)) for a,b,c,d,f in RECT.findall(raw6) if f!="none"]
    chart=[e for e in p6 if 1330<=e["y"]<=1800 and 65<=e["x"]<=961]
    print(f"  chart texts: {len(chart)}")
    maxcov=0
    for e in chart:
        ib=ink_box(e["s"],e["fam"],e["size"],e["bold"],e["x"],e["y"],e["anchor"]); l,t,r,b=ib; area=max(0.0,(r-l)*(b-t))
        cov=0.0
        for (rl,rt,rr,rb) in rects6:
            if abs(rl-65)<1 and abs(rt-1330)<1: continue
            ow=max(0.0,min(r,rr)-max(l,rl)); oh=max(0.0,min(b,rb)-max(t,rt))
            if area: cov=max(cov,ow*oh/area)
        maxcov=max(maxcov,cov)
        if cov>0: print(f"   cov {cov:.1%}: {e['s'][:60]!r}")
    print(f"  max coverage: {maxcov:.1%}")
    print(f"===== {label} P1 gloss wrapped lines =====")
    p1,_=texts(d/"p1-une.svg")
    for e in p1:
        if "Uitleg" in e["s"] or "se jouer" in e["s"]: print(f"  y={e['y']} x={e['x']} fs={e['size']} {e['s'][:120]!r}")
