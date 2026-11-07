# -*- coding: utf-8 -*-
"""Builder's extra scans for ENxFR (complements tools/occlusion_audit.py):
1. same-baseline furniture-band spacing (decoded text, PIL advance);
2. right-edge ADVANCE scan (text advance vs page/frame edges);
3. P6 chart-label baseline-anchored ink vs later rects (<30% gate).
Run with tools/venv/bin/python. Reads the EDITION svgs only."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import text_w, wrap
from PIL import ImageFont
import xml.etree.ElementTree as ET

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-en-fr/svg")
FONTS = "/usr/share/fonts/opentype/noto"
BL = os.path.expanduser("~/.local/share/fonts/UnifrakturMaguntia.ttf")
def font(kind, bold, size):
    if kind == "black":
        return ImageFont.truetype(BL, int(size))
    p = {"serif": "NotoSerifCJK-Bold.ttc" if bold else "NotoSerifCJK-Regular.ttc",
         "sans": "NotoSansCJK-Bold.ttc" if bold else "NotoSansCJK-Regular.ttc"}[kind]
    return ImageFont.truetype(os.path.join(FONTS, p), int(size), index=2)

def adv(text, kind, bold, size):
    if kind == "black":
        return font("black", bold, size).getlength(text)
    return text_w(text, kind, bold, size)

def texts(page):
    t = ET.parse(os.path.join(ED, page))
    out = []
    for el in t.getroot().iter("{http://www.w3.org/2000/svg}text"):
        s = "".join(el.itertext())
        out.append({"x": float(el.get("x", 0)), "y": float(el.get("y", 0)),
                    "size": float(el.get("font-size", 20)),
                    "bold": el.get("font-weight") in ("bold", "700"),
                    "anchor": el.get("text-anchor", "start"),
                    "fam": el.get("font-family", ""), "text": s})
    return out

def famkind(fam):
    if "Unifraktur" in fam: return "black"
    return "serif" if "Serif" in fam else "sans"

print("== 1. same-baseline furniture bands (decoded, advance widths) ==")
for page in sorted(os.listdir(ED)):
    ts = texts(page)
    by_y = {}
    for el in ts:
        by_y.setdefault(round(el["y"]), []).append(el)
    for y, els in sorted(by_y.items()):
        if len(els) < 2: continue
        # only furniture bands: top strip y=92, dark band 478/522, band heads 116/142, footers 2624
        if y not in (92, 116, 142, 478, 522, 2624): continue
        spans = []
        for el in els:
            w = text_w(el["text"], famkind(el["fam"]), el["bold"], el["size"])
            if el["anchor"] == "middle": l, r = el["x"] - w / 2, el["x"] + w / 2
            elif el["anchor"] == "end": l, r = el["x"] - w, el["x"]
            else: l, r = el["x"], el["x"] + w
            spans.append((l, r, el["text"][:40]))
        spans.sort()
        for (l1, r1, t1), (l2, r2, t2) in zip(spans, spans[1:]):
            gap = l2 - r1
            flag = "OVERLAP!" if gap < 0 else ("tight" if gap < 10 else "ok")
            if gap < 40: print(f"  {page} y={y} gap={gap:.1f} {flag} :: {t1!r} || {t2!r}")
print("  (only gaps < 40px listed)")

print("== 2. right-edge ADVANCE scan ==")
worst = []
for page in sorted(os.listdir(ED)):
    for el in texts(page):
        w = adv(el["text"], famkind(el["fam"]), el["bold"], el["size"])
        if el["anchor"] == "middle": r = el["x"] + w / 2
        elif el["anchor"] == "end": r = el["x"]
        else: r = el["x"] + w
        if r > 1885: worst.append((page, el["y"], r, el["text"][:50]))
        if r > 1922: worst.append(("PAGE-EDGE! " + page, el["y"], r, el["text"][:50]))
print("  advance-right > 1885 (content edge) or > 1922 (frame):", len(worst))
for w_ in worst: print("   ", w_)

print("== 3. P6 chart labels, baseline-anchored ink vs later rects ==")
# chart label lines are drawn as flow paras; find their text nodes on p6
# and every rect drawn after them in document order; report coverage %.
tree = ET.parse(os.path.join(ED, "p6-politique.svg"))
root = tree.getroot()
NS = "{http://www.w3.org/2000/svg}"
elems = list(root.iter())
labels = ["No lines : 38%", "Work on Tuesday : 29%", "Travel plans : 21%", "Habit : 12%"]
for i, el in enumerate(elems):
    if el.tag == NS + "text" and "".join(el.itertext()).strip() in labels:
        lab = "".join(el.itertext()).strip()
        y = float(el.get("y")); x = float(el.get("x")); size = float(el.get("font-size", 22))
        f = font("serif", True, size)
        asc, desc = f.getmetrics()
        # baseline-anchored ink: use getbbox of the string, shifted by baseline
        bb = f.getbbox(lab)
        top, bot = y - asc + bb[1], y - asc + bb[3]
        w = f.getlength(lab)
        cover = 0.0
        for el2 in elems[i + 1:]:
            if el2.tag == NS + "rect":
                rx, ry = float(el2.get("x", 0)), float(el2.get("y", 0))
                rw, rh = float(el2.get("width", 0)), float(el2.get("height", 0))
                if el2.get("fill") in (None, "none"): continue
                ox = max(0, min(x + w, rx + rw) - max(x, rx))
                oy = max(0, min(bot, ry + rh) - max(top, ry))
                cover = max(cover, ox * oy / max(1, w * (bot - top)))
        print(f"  {lab!r} baseline={y} ink=({top:.1f},{bot:.1f}) max-later-rect-coverage={cover*100:.1f}% {'PASS <30%' if cover < 0.30 else 'FAIL'}")
print("scans done")
