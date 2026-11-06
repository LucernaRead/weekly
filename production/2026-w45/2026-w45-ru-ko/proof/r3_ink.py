#!/usr/bin/env python3
"""Reproof R3: same-baseline ink scan (venv PIL + build fonts) + badge ink span."""
import re, sys
sys.path.insert(0,"/home/hatch/workspace/goals/lucernaread-social-media-operations/tools/venv/lib/python3.12/site-packages")
from PIL import ImageFont
import os
FONTS_DIR="/usr/share/fonts/opentype/noto"
def sc_index(path):
    for i in range(12):
        try:
            f=ImageFont.truetype(path,40,index=i)
            if f.getname()[0].endswith("SC"): return i
        except Exception: break
    return 0
SERIF=os.path.join(FONTS_DIR,"NotoSerifCJK-Regular.ttc"); SERIF_B=os.path.join(FONTS_DIR,"NotoSerifCJK-Bold.ttc")
SANS=os.path.join(FONTS_DIR,"NotoSansCJK-Regular.ttc"); SANS_B=os.path.join(FONTS_DIR,"NotoSansCJK-Bold.ttc")
IDX={p:sc_index(p) for p in (SERIF,SERIF_B,SANS,SANS_B)}
_cache={}
def font(kind,bold,size):
    path={"serif":SERIF_B if bold else SERIF,"sans":SANS_B if bold else SANS}[kind]
    if (path,size) not in _cache: _cache[(path,size)]=ImageFont.truetype(path,size,index=IDX[path])
    return _cache[(path,size)]
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations/files"
def elems(path):
    t=open(path,encoding="utf-8").read(); out=[]
    for m in re.finditer(r"<text([^>]*)>(.*?)</text>",t,re.S):
        a=m.group(1)
        def g(k):
            mm=re.search(k+r'="([^"]*)"',a); return mm.group(1) if mm else ""
        if not g("x") or not g("y") or not g("font-size"): continue
        kind="serif" if "Serif" in g("font-family") else "sans"
        out.append({"x":float(g("x")),"y":float(g("y")),"size":float(g("font-size")),
                    "bold":g("font-weight")=="700","anchor":g("text-anchor") or "start","text":m.group(2),"kind":kind})
    return out
def ink(e):
    f=font(e["kind"],e["bold"],int(e["size"]) if float(e["size"]).is_integer() else e["size"])
    adv=f.getlength(e["text"]); bb=f.getbbox(e["text"])
    if e["anchor"]=="middle": org=e["x"]-adv/2
    elif e["anchor"]=="end": org=e["x"]-adv
    else: org=e["x"]
    return org+bb[0], org+bb[2], adv, bb
def scan(d,label):
    total=0
    for p in ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]:
        es=[e for e in elems(f"{d}/{p}.svg") if e["y"]!=2624.0]  # footer exempt by design
        by={}
        for e in es: by.setdefault(round(e["y"],2),[]).append(e)
        for y,grp in by.items():
            spans=[]
            for e in grp:
                l,r,adv,bb=ink(e); spans.append((l,r,e))
            spans.sort()
            for a,b in zip(spans,spans[1:]):
                gap=b[0]-a[1]
                if gap<5:
                    print(f"{label} {p} y={y} gap={gap:.2f} A={a[2]['text'][:40]!r} B={b[2]['text'][:40]!r}"); total+=1
    print(f"{label}: ink-scan flags={total}")
scan(f"{BASE}/weekly-report-w45-ru-ko/svg","EDITION")
scan(f"{BASE}/weekly-report-w45-ru-core/svg","CORE")
print("== badge ink span ==")
for label,path in (("EDITION",f"{BASE}/weekly-report-w45-ru-ko/svg/p1-pervaya.svg"),
                   ("W43",f"{BASE}/weekly-report-ru-ko/svg/p1-pervaya.svg")):
    es=elems(path); b=[e for e in es if "한국어 독자를 위한 판" in e["text"]][0]
    l,r,adv,bb=ink(b)
    print(f"{label}: elem x={b['x']} y={b['y']} size={b['size']} bold={b['bold']} anchor={b['anchor']} adv={adv:.2f} bbox={bb} span={l:.2f}-{r:.2f}")
