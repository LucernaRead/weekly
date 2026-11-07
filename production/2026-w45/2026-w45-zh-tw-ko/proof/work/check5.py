# -*- coding: utf-8 -*-
"""P7 letter-box ink measurement (SVG PIL + card pixels), chart-label graze, regen."""
import re, os
import xml.etree.ElementTree as ET
from PIL import Image, ImageFont
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = BASE + "/files/weekly-report-w45-zh-tw-ko/svg"
CARD = BASE + "/files/weekly-report-w45-zh-tw-ko/cards/p7-lang.png"
NS = "{http://www.w3.org/2000/svg}"
t = ET.parse(f"{ED}/p7-lang.svg")
root = t.getroot()
print("SVG size attrs:", root.get("width"), root.get("height"), root.get("viewBox"))
box = None
for el in root.iter(NS+"rect"):
    if el.get("x")=="1451" and abs(float(el.get("y","0"))-1184.86)<0.01:
        box = el; print("readers box rect:", el.attrib)
bx, by, bw, bh = 1451.0, 1184.86, 434.0, 551.5
print(f"box bottom = {by+bh:.2f}, inner edge (stroke 1.4) = {by+bh-0.7:.2f}")
# last box text node
nodes = []
for el in root.iter(NS+"text"):
    x, y = float(el.get("x",0)), float(el.get("y",0))
    if 1451 <= x < 1885 and y > 1500 and y < 2600:
        nodes.append((y, x, float(el.get("font-size","20")), el.get("font-family",""), el.get("font-weight",""), el.text or ""))
nodes.sort()
for n in nodes[-3:]: print("  last box nodes:", n)
y, x, sz, fam, wt, s = nodes[-1]
bold = wt in ("700","bold")
path = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
if "Serif" in fam: path = path.replace("Sans","Serif")
f = ImageFont.truetype(path, int(round(sz*4)), index=3)
bb = f.getbbox(s, anchor="ls")
ink_bottom = y + bb[3]/4
print(f"last line: {s!r} baseline={y} size={sz} fam={fam} bold={bold}")
print(f"PIL 4x bbox={bb} -> ink bottom = {ink_bottom:.2f}; clearance to inner border = {by+bh-0.7-ink_bottom:.2f}px; to outer border = {by+bh+0.7-ink_bottom:.2f}px")
print(f"baseline clearance (builder number) = {by+bh-y:.2f}px")

print("\n=== card-pixel measurement (delivered p7 card) ===")
im = Image.open(CARD).convert("RGB")
print("card size:", im.size)
# scan box column region x 1460..1880, rows 1680..1780: dark text pixels vs border pixels
def is_dark(px): return sum(px) < 450
def is_border(px): return abs(px[0]-0xd8)<25 and abs(px[1]-0xcf)<25 and abs(px[2]-0xb4)<25
last_text_row = None; border_rows = []
for row in range(1650, 1800):
    dark = 0; bord = 0
    for col in range(1460, 1880, 2):
        px = im.getpixel((col, row))
        if is_dark(px): dark += 1
        if is_border(px): bord += 1
    if dark >= 3: last_text_row = row
    if bord >= 100: border_rows.append(row)
print("last text-ink row in box column:", last_text_row)
print("border rows (>=100 border px) in 1650..1800:", border_rows[:10], "..." if len(border_rows)>10 else "")
if last_text_row and border_rows:
    print(f"card clearance = {border_rows[0]-last_text_row}px (border row {border_rows[0]} - last ink row {last_text_row})")
# teaser: last ink row in teaser region (x 65..1400, y 2400..2600, excluding footer rule 2580)
last_teaser = None
for row in range(2400, 2580):
    dark = sum(1 for col in range(65, 1400, 2) if is_dark(im.getpixel((col, row))))
    if dark >= 3: last_teaser = row
print("teaser last ink row on card:", last_teaser, "(footer rule at y=2580; margin =", 2580-last_teaser if last_teaser else None, "px)")

print("\n=== chart-label graze: text ink vs later-drawn bar rects (P4/P6) ===")
def graze(page, barfills):
    tt = ET.parse(f"{ED}/{page}.svg"); rr = tt.getroot()
    # document order: collect rects (bars) and texts with their order index
    items = []
    for i, el in enumerate(rr.iter()):
        if el.tag == NS+"rect": items.append(("rect", i, el))
        elif el.tag == NS+"text": items.append(("text", i, el))
    bars = []
    for kind, i, el in items:
        if kind=="rect" and el.get("fill") in barfills:
            bars.append((i, float(el.get("x",0)), float(el.get("y",0)), float(el.get("width",0)), float(el.get("height",0))))
    print(f"  {page}: bars={bars}")
    hits = 0
    for kind, i, el in items:
        if kind!="text": continue
        s = el.text or ""
        if not s.strip(): continue
        x, y = float(el.get("x",0)), float(el.get("y",0)); sz=float(el.get("font-size","20"))
        fam = el.get("font-family",""); bold = el.get("font-weight") in ("700","bold")
        pth = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
        if "Serif" in fam: pth = pth.replace("Sans","Serif")
        try: ff = ImageFont.truetype(pth, int(round(sz*4)), index=3)
        except Exception: continue
        bb = ff.getbbox(s, anchor="ls")
        tx0, tx1 = x + bb[0]/4, x + bb[2]/4
        ty0, ty1 = y + bb[1]/4, y + bb[3]/4
        for (bi, rx, ry, rw, rh) in bars:
            if bi > i:  # bar drawn after text -> could cover it
                if tx0 < rx+rw and tx1 > rx and ty0 < ry+rh and ty1 > ry:
                    print(f"    GRAZE? text {s[:50]!r} at y={y} ink=({tx0:.1f},{ty0:.1f})-({tx1:.1f},{ty1:.1f}) vs bar x={rx} y={ry} w={rw} h={rh}")
                    hits += 1
    print(f"  {page}: graze hits={hits}")
graze("p4-sport", {"#a4553a"})
graze("p6-deep", {"#3e4c2a"})
