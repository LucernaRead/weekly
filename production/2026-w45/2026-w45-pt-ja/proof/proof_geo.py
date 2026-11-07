#!/usr/bin/env python3
"""Independent geometry supplement: frame/right-edge ADVANCE scan,
same-baseline collision scan, P6 chart-label ink coverage (baseline-anchored)."""
import glob, re
from xml.etree import ElementTree as ET
from PIL import ImageFont

GOAL = "/home/hatch/workspace/goals/lucernaread-social-media-operations"
ED = GOAL + "/files/weekly-report-w45-pt-ja/svg"
CO = GOAL + "/files/weekly-report-w45-pt-core/svg"
PAGES = ["p1-capa","p2-vida","p3-cultura","p4-esporte","p5-jovens","p6-aprofundamento","p7-lingua","p8-avaliacao"]
NS = "{http://www.w3.org/2000/svg}"

def load(p):
    return ET.parse(p).getroot()

# locate fonts
import subprocess
def fontpath(pat):
    out = subprocess.run(["fc-list", ":", "file"], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if pat in line:
            return line.split(":")[0]
    return None
SERIF = None; SANS = None
for cand in glob.glob("/usr/share/fonts/**/NotoSerifCJK-Regular.ttc", recursive=True) + \
             glob.glob("/usr/share/fonts/**/NotoSerifCJK*.ttc", recursive=True):
    SERIF = cand; break
for cand in glob.glob("/usr/share/fonts/**/NotoSansCJK-Regular.ttc", recursive=True) + \
             glob.glob("/usr/share/fonts/**/NotoSansCJK*.ttc", recursive=True):
    SANS = cand; break
print("SERIF:", SERIF); print("SANS:", SANS)

def font_for(el):
    fam = el.get("font-family","")
    size = float(el.get("font-size","20"))
    bold = el.get("font-weight") in ("700","bold")
    base = SERIF if "Serif" in fam else SANS
    # TTC face index JP=0
    try:
        return ImageFont.truetype(base, int(size), index=0)
    except Exception as e:
        return ImageFont.truetype(base, int(size))

def advance_w(f, s):
    try:
        return f.getlength(s)
    except Exception:
        return sum(f.getbbox(c)[2] for c in s)

print("=== FRAME / RIGHT-EDGE ADVANCE SCAN (inner frame x: find vertical lines near 40/1910) ===")
for dd, name in [(ED,"ed"), (CO,"core")]:
    maxright = 0; maxinfo = None; flags = 0
    for pg in PAGES:
        root = load(f"{dd}/{pg}.svg")
        # frame verticals: line/rect edges
        vx = set()
        for el in root.iter():
            if el.tag == NS+"line":
                x1, x2 = float(el.get("x1")), float(el.get("x2"))
                if x1 == x2: vx.add(x1)
            if el.tag == NS+"rect" and el.get("x") is not None:
                vx.add(float(el.get("x"))); vx.add(float(el.get("x"))+float(el.get("width")))
        for el in root.iter():
            if el.tag != NS+"text" or not el.text: continue
            f = font_for(el); w = advance_w(f, el.text)
            x = float(el.get("x")); a = el.get("text-anchor","start")
            left = x if a=="start" else (x-w if a=="end" else x-w/2)
            right = left + w
            if right > maxright: maxright, maxinfo = right, (pg, el.text[:40], a, x)
            if right > 1910 or left < 40:
                print(f"  FLAG {name} {pg} {el.text!r} left={left:.1f} right={right:.1f}"); flags += 1
    print(f"{name}: max_right_advance={maxright:.1f} at {maxinfo} flags={flags}")

print("=== SAME-BASELINE COLLISION SCAN (ink boxes, same page+y) ===")
for dd, name in [(ED,"ed")]:
    flags = 0
    for pg in PAGES:
        root = load(f"{dd}/{pg}.svg")
        rows = {}
        for el in root.iter():
            if el.tag != NS+"text" or not el.text: continue
            f = font_for(el); w = advance_w(f, el.text)
            x = float(el.get("x")); y = float(el.get("y")); a = el.get("text-anchor","start")
            left = x if a=="start" else (x-w if a=="end" else x-w/2)
            rows.setdefault(round(y,1), []).append((left, left+w, el.text))
        for y, items in rows.items():
            items.sort()
            for (l1,r1,t1),(l2,r2,t2) in zip(items, items[1:]):
                if r1 > l2 + 0.5:
                    print(f"  OVERLAP {pg} y={y}: {t1!r} | {t2!r}"); flags += 1
    print(f"{name} same-baseline flags={flags}")

print("=== P6 CHART LABEL INK vs LATER BARS (anchor ls, Serif JP Bold 20pt) ===")
for dd, name in [(ED,"ed"), (CO,"core")]:
    root = load(f"{dd}/p6-aprofundamento.svg")
    elems = list(root.iter())
    # find label texts
    for el in root.iter():
        if el.tag == NS+"text" and el.text and el.text.strip() in ("portões abertos","espera","prova"):
            print(f"  {name} label {el.text!r} x={el.get('x')} y={el.get('y')} size={el.get('font-size')} anchor={el.get('text-anchor')}")
    # bars: rects on P6; report rects drawn after each label in document order
    order = [(i, el) for i, el in enumerate(root.iter())]
    print(f"  {name} total elements={len(order)}")
