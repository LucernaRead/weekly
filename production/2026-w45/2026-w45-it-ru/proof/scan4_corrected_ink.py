#!/usr/bin/env python3
"""Corrected ink measurements (PIL anchor='ls' at 4x) for IT x RU W45 proofread.
Supersedes the tight-ink pass in proof_scan3.py, whose getbbox origin handling
(mistaking the ascender origin for the baseline) overstated ink bottoms by ~ascent.
Replicated builder edge_row_chart.py ls-box method for P6 chart coverage."""
import re, os
from xml.etree import ElementTree as ET
from PIL import ImageFont
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = f"{BASE}/files/weekly-report-w45-it-ru/svg"
SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SERIFB = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SANSB = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
def fnum(v, d=0.0):
    try: return float(v)
    except: return d
def ink(text, fam, size, weight, x, y, anchor):
    base = SERIFB if ("Serif" in (fam or "") and weight in ("700", "bold")) else SERIF if "Serif" in (fam or "") else SANSB if weight in ("700", "bold") else SANS
    f = ImageFont.truetype(base, int(round(size * 4)), index=2)
    bb = f.getbbox(text, anchor="ls")
    adv = f.getlength(text) / 4.0
    top, bot = y + bb[1] / 4.0, y + bb[3] / 4.0
    if anchor == "middle": l, r = x - adv / 2.0, x + adv / 2.0
    elif anchor == "end": l, r = x - adv, x
    else: l, r = x, x + adv
    return (l, top, r, bot, adv)
def load(p):
    out = []
    for el in ET.parse(p).iter():
        if el.tag.split("}")[-1] == "text":
            out.append({"x": el.get("x"), "y": el.get("y"), "fs": el.get("font-size"),
                        "anchor": el.get("text-anchor"), "fam": el.get("font-family"),
                        "weight": el.get("font-weight"), "text": "".join(el.itertext())})
    return out
OUT = []
ed7, ed1, ed8 = load(f"{ED}/p7-lingua.svg"), load(f"{ED}/p1-prima.svg"), load(f"{ED}/p8-valutazione.svg")
col3 = [t for t in ed7 if fnum(t["x"]) >= 989 and fnum(t["y"]) < 1724]
mx = max(ink(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])[3] for t in col3)
OUT.append(f"P7 col3 max ink bottom (ls-anchor) = {mx:.1f}; FRASI rule y=1686 stroke 2 (top 1685); clearance = {1685-mx:.1f}px; stream claim 1646.0")
for t in ed7:
    if t["text"].startswith("assaggio ="):
        b = ink(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])
        OUT.append(f"P7 parola gloss ink bottom = {b[3]:.1f}; parola box rect (1451,1039.5,434,247) bottom = 1286.5; inside by {1286.5-b[3]:.1f}px")
for t in ed7:
    if t["text"].startswith("нет. Напишите"):
        b = ink(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])
        OUT.append(f"P7 disclosure last line ink bottom = {b[3]:.1f}; letter box rect (1451,1312.5,434,333.5) bottom = 1646.0; inside by {1646.0-b[3]:.1f}px")
for t in ed1:
    if "«il primo freddo»" in t["text"] and "холод" in t["text"]:
        b = ink(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])
        OUT.append(f"P1 parola note ink bottom = {b[3]:.1f}; row-B rule y=1864; clearance = {1864-b[3]:.1f}px")
keys = [t for t in ed8 if 1400 <= fnum(t["y"]) < 2580]
mxk = max(ink(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])[3] for t in keys)
mxb = max(fnum(t["y"]) for t in keys)
OUT.append(f"P8 keys max baseline = {mxb}; max ink bottom (ls-anchor) = {mxk:.1f}; footer rule 2580; clearance = {2580-mxk:.1f}px; stream claim 2484/bottom 2552")
for t in ed1:
    if "ТЕКСТЫ НА ИТАЛЬЯНСКОМ" in t["text"] and fnum(t["y"]) == 574:
        b = ink(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])
        OUT.append(f"Badge ink = ({b[0]:.1f},{b[1]:.1f})-({b[2]:.1f},{b[3]:.1f}); width = {b[2]-b[0]:.2f}px; band bottom 542 -> gap {b[1]-542:.1f}px")
for t in ed1:
    if t["text"].startswith("LA NOTIZIA"):
        b = ink(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])
        OUT.append(f"LA NOTIZIA ink top = {b[1]:.1f}; badge ink bottom 578.8 -> gap {b[1]-578.8:.1f}px")
# P6 chart coverage, builder ls-box method
tree = ET.parse(f"{ED}/p6-approfondimento.svg"); elems = []
for el in tree.iter():
    tag = el.tag.split("}")[-1]
    if tag == "text": elems.append(("text", el))
    elif tag == "rect": elems.append(("rect", el))
maxcov, worst = 0.0, None
for i, (k, el) in enumerate(elems):
    if k != "text": continue
    txt = "".join(el.itertext())
    if not (any(c in txt for c in ["Torino", "Milano", "Bologna", "Roma", "Napoli"]) or re.fullmatch(r"[0-9]+°?", txt.strip())): continue
    x, y = fnum(el.get("x")), fnum(el.get("y")); size = fnum(el.get("font-size")); fam = el.get("font-family"); bold = el.get("font-weight") == "700"
    base = SERIFB if ("Serif" in (fam or "") and bold) else SERIF if "Serif" in (fam or "") else SANSB if bold else SANS
    fn = ImageFont.truetype(base, int(round(size)), index=2); asc, desc = fn.getmetrics(); w = fn.getlength(txt); anc = el.get("text-anchor", "start")
    l = x if anc == "start" else (x - w if anc == "end" else x - w / 2); box = (l, y - asc, l + w, y + desc)
    for k2, r in elems[i + 1:]:
        if k2 != "rect" or r.get("fill") in ("none", "transparent"): continue
        rx, ry, rw, rh = fnum(r.get("x")), fnum(r.get("y")), fnum(r.get("width")), fnum(r.get("height"))
        ix = max(0, min(box[2], rx + rw) - max(box[0], rx)); iy = max(0, min(box[3], ry + rh) - max(box[1], ry))
        cov = ix * iy / ((box[2] - box[0]) * (box[3] - box[1])) if box[2] > box[0] else 0
        if cov > maxcov: maxcov, worst = cov, (txt, (rx, ry, rw, rh))
OUT.append(f"P6 chart-label coverage (builder ls-box method replicated) = {maxcov*100:.1f}%; worst = {worst}; threshold <30%")
open(f"{BASE}/hidden_files/w45/it-ru-proof/scan4.txt", "w").write("\n".join(OUT) + "\n")
print("\n".join(OUT))
