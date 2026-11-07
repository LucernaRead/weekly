import os, re, sys
from xml.etree import ElementTree as ET
from PIL import ImageFont
NS="{http://www.w3.org/2000/svg}"
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ko-core/svg"
SERIF_R="/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SERIF_B="/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
SANS_R="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SANS_B="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
BLACK="/home/hatch/.local/share/fonts/UnifrakturMaguntia.ttf"
_fonts={}
def font(fam,size,bold):
    key=(fam,size,bold)
    if key in _fonts: return _fonts[key]
    if "Unifraktur" in fam: f=ImageFont.truetype(BLACK,int(size*4))
    elif "Serif" in fam: f=ImageFont.truetype(SERIF_B if bold else SERIF_R,int(size*4),index=1)
    else: f=ImageFont.truetype(SANS_B if bold else SANS_R,int(size*4),index=1)
    _fonts[key]=f; return f
def inkbox(t,x,y,fam,size,anchor,bold):
    f=font(fam,size,bold)
    bb=f.getbbox(t)  # at 4x
    l,t_,r,b=[v/4.0 for v in bb]
    w=r-l
    if anchor=="middle": x0=x-w/2-l; x1=x+w/2-l+ (0)  # approx: ink left = x - w/2 ... use bbox offsets
    # proper: text drawn with origin at (x,y) baseline; ink spans [x+l, x+r] for start anchor
    if anchor=="start": x0,x1=x+l,x+r
    elif anchor=="end": x0,x1=x-l-(r-l)+l, x  # end anchor: right edge at x; ink right = x - (advance-right offset)... approximate with bbox
    else: x0,x1=x-(r-l)/2, x+(r-l)/2
    # simpler robust: use getlength for advance
    adv=f.getlength(t)/4.0
    if anchor=="start": ax0,ax1=x,x+adv
    elif anchor=="end": ax0,ax1=x-adv,x
    else: ax0,ax1=x-adv/2,x+adv/2
    # ink box: intersect advance box with bbox offsets (bbox l may be >0 for first glyph bearing)
    ix0=max(ax0, x+l if anchor=="start" else ax0+l)
    ix1=min(ax1, x+r if anchor=="start" else ax1)
    if ix1<=ix0: ix0,ix1=ax0,ax1
    # vertical: SOP ink band baseline -0.88em .. +0.30em (PIL default anchor is ascender-based, so bbox y is unusable here)
    return (ix0, y-0.88*size, ix1, y+0.30*size)

HANG=re.compile(r"[가-힣]+")
CJK=re.compile(r"[\u4e00-\u9fff]")
CLOSE_START=set(")]}〉》.,!?%:;\"'」』")
PARTICLES={"는","은","이","가","을","를","에","의","과","와","로","으로","에서","에게","한테","부터","까지","도","만","라도","이나","나","요","다","어요","예요","아요","지요","세요","돼요","해요","네요","군요","죠","자","까","고","며","면서","거나","든지"}
for fn in sorted(os.listdir(BASE)):
    if not fn.endswith(".svg"): continue
    root=ET.parse(os.path.join(BASE,fn)).getroot()
    texts=[]; shapes=[]  # shapes: (order, kind, box)
    order=0
    for el in root.iter():
        tag=el.tag.replace(NS,"")
        if tag=="text":
            t="".join(el.itertext())
            texts.append({"o":order,"x":float(el.get("x",0)),"y":float(el.get("y",0)),"size":float(el.get("font-size",20)),"anchor":el.get("text-anchor","start"),"fam":el.get("font-family",""),"bold":el.get("font-weight")=="700","text":t})
        elif tag=="rect":
            try:
                rx,ry,rw,rh=float(el.get("x",0)),float(el.get("y",0)),float(el.get("width",0)),float(el.get("height",0))
            except: continue
            fill=el.get("fill","none")
            if fill not in ("none",None) and rw>0 and rh>0 and not (rx==0 and ry==0 and rw==1950 and rh==2700):
                shapes.append((order,"rect",(rx,ry,rx+rw,ry+rh)))
        elif tag=="image":
            try:
                rx,ry,rw,rh=float(el.get("x",0)),float(el.get("y",0)),float(el.get("width",0)),float(el.get("height",0))
                shapes.append((order,"image",(rx,ry,rx+rw,ry+rh)))
            except: pass
        order+=1
    # ink boxes
    for t in texts:
        t["box"]=inkbox(t["text"],t["x"],t["y"],t["fam"],t["size"],t["anchor"],t["bold"])
    print(f"\n===== {fn} =====")
    # 1. same-baseline overlaps
    by_y={}
    for t in texts: by_y.setdefault(round(t["y"]/1.5),[]).append(t)
    nbase=0
    for k,grp in by_y.items():
        if len(grp)<2: continue
        grp=sorted(grp,key=lambda z:z["box"][0])
        for a,b in zip(grp,grp[1:]):
            if b["box"][0] < a["box"][2]-0.5:
                print(f"  SAMEBASE y={a['y']} OVERLAP: {a['text'][:40]!r} | {b['text'][:40]!r} boxes {a['box']} {b['box']}"); nbase+=1
    if not nbase: print("  same-baseline: no overlaps")
    # 2. later-rect/image graze (any overlap >0)
    grazes=[]
    for t in texts:
        tb=t["box"]; area=(tb[2]-tb[0])*(tb[3]-tb[1])
        if area<=0: continue
        for (o,kind,sb) in shapes:
            if o<=t["o"]: continue
            ox=max(0,min(tb[2],sb[2])-max(tb[0],sb[0])); oy=max(0,min(tb[3],sb[3])-max(tb[1],sb[1]))
            if ox>0 and oy>0:
                frac=ox*oy/area
                grazes.append((frac,kind,t["text"][:50],sb))
    grazes.sort(reverse=True)
    if grazes:
        for frac,kind,tx,sb in grazes[:25]: print(f"  GRAZE {frac*100:.1f}% {kind} text={tx!r} shape={sb}")
    else: print("  later-rect/image graze: none")
    # 3a. line-start orphan punct / particle
    for t in texts:
        s=t["text"].strip()
        if not s: continue
        if s[0] in CLOSE_START:
            print(f"  LINESTART-PUNCT y={t['y']} x={t['x']}: {s[:60]!r}")
        else:
            m=re.match(r"^(\S+)",s)
            if m and m.group(1) in PARTICLES:
                print(f"  LINESTART-PARTICLE y={t['y']} x={t['x']}: {s[:60]!r}")
    # 3b. block-final fragments: group by (x,size) runs on y-gap>55
    from collections import defaultdict
    groups=defaultdict(list)
    for t in texts: groups[(t["x"],t["size"])].append(t)
    for (gx,gs),grp in sorted(groups.items()):
        grp=sorted(grp,key=lambda z:z["y"])
        runs=[]; cur=[grp[0]]
        for prev,cur_ in zip(grp,grp[1:]):
            if cur_["y"]-prev["y"]>55: runs.append(cur); cur=[cur_]
            else: cur.append(cur_)
        runs.append(cur)
        for run in runs:
            last=run[-1]; s=last["text"].strip()
            syl=len(HANG.findall(s)); sylcount=sum(len(m) for m in HANG.findall(s))
            hang_only = bool(s) and not CJK.search(s)
            if hang_only and gs>=19:
                if sylcount<=4 or (s.endswith(")") and len(s)<=10):
                    print(f"  BLOCKFINAL-CAND x={gx} y={last['y']} sz={gs} syl={sylcount}: {s!r} (run len {len(run)})")
    # 4. repeated eojeol in a line
    for t in texts:
        m=re.search(r"(\S+) \1(\s|$|[,.])",t["text"])
        if m: print(f"  REPEAT y={t['y']}: {t['text'][:70]!r}")
    # 5. mixed-script lines (gloss candidates): list Hangul runs + stem check vs page Korean text
    pagetext="".join(t["text"] for t in texts).replace(" ","")
    for t in texts:
        s=t["text"]
        if HANG.search(s) and CJK.search(s):
            runs=HANG.findall(s)
            # skip pure furniture straplines? keep, adjudicate
            for r in runs:
                stem=r[:-1] if r.endswith("다") and len(r)>1 else r
                if stem and stem not in pagetext:
                    print(f"  GLOSS-MISS y={t['y']}: run={r!r} stem={stem!r} line={s[:70]!r}")
