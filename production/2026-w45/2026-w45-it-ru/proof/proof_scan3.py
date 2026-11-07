#!/usr/bin/env python3
"""Proof scan 3: geometry supplements (PIL ink/advance), chip exercise sequences, badge clearance, bytes checks."""
import re, os, sys
from xml.etree import ElementTree as ET
from PIL import ImageFont

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = f"{BASE}/files/weekly-report-w45-it-core/svg"
ED = f"{BASE}/files/weekly-report-w45-it-ru/svg"
W43 = f"{BASE}/files/weekly-report-it-ru/svg"
PAGES = ["p1-prima","p2-vita","p3-cultura","p4-sport","p5-giovani","p6-approfondimento","p7-lingua","p8-valutazione"]
OUT = []
def sec(t): OUT.append("\n### " + t)
def line(s): OUT.append(s)

SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SERIFB = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SANSB = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
def font(path, size, idx=2):
    return ImageFont.truetype(path, int(round(size*4)), index=idx)
def ink_box(text, fam, size, weight, x, y, anchor):
    # returns (left, ink_top, right, ink_bottom) in page coords; y is baseline
    try:
        if "Serif" in (fam or ""):
            f = font(SERIFB if weight in ("700","bold") else SERIF, size)
        else:
            f = font(SANSB if weight in ("700","bold") else SANS, size)
    except Exception as e:
        return None
    # 4x supersample like tool: getbbox at 4x then /4
    bb = f.getbbox(text)  # (l, t, r, b) relative to anchor point? PIL getbbox: left,top,right,bottom w.r.t. origin at baseline-left? For anchor handling use getmetrics + length
    adv = f.getlength(text) / 4.0
    # getbbox top/bottom are relative to baseline origin (ascent negative?) — PIL: bbox top is distance from top? Use: ink_top = y + bb[1]/4, ink_bottom = y + bb[3]/4
    top = y + bb[1]/4.0; bot = y + bb[3]/4.0
    if anchor == "middle":
        left = x - adv/2.0; right = x + adv/2.0
    elif anchor == "end":
        left = x - adv; right = x
    else:
        left = x; right = x + adv
    return (left, top, right, bot, adv)

def load_texts(path):
    tree = ET.parse(path); out = []
    for el in tree.iter():
        if el.tag.split("}")[-1] == "text":
            out.append({"x": el.get("x"), "y": el.get("y"), "fs": el.get("font-size"),
                        "anchor": el.get("text-anchor"), "fam": el.get("font-family"),
                        "weight": el.get("font-weight"), "text": "".join(el.itertext())})
    return out
def raw(p): return open(p, encoding="utf-8").read()
def fnum(v, d=0.0):
    try: return float(v)
    except: return d

ed = {p: load_texts(f"{ED}/{p}.svg") for p in PAGES}
ce = {p: load_texts(f"{CORE}/{p}.svg") for p in PAGES}

# ---- badge width + clearance
sec("8e badge ink width + clearance (PIL, edition P1)")
for t in ed["p1-prima"]:
    if "ТЕКСТЫ НА ИТАЛЬЯНСКОМ" in t["text"] and fnum(t["y"]) == 574:
        b = ink_box(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])
        line(f"badge: {t['text']!r} ink={b} width={b[2]-b[0]:.2f} ink_top={b[1]:.1f} ink_bottom={b[3]:.1f}")
        # neighbors in y: texts with baseline between 500-700
        for u in ed["p1-prima"]:
            y = fnum(u["y"])
            if 500 <= y <= 700 and u is not t:
                bu = ink_box(u["text"], u["fam"], fnum(u["fs"]), u["weight"], fnum(u["x"]), y, u["anchor"])
                line(f"   neighbor y={u['y']} ink_top={bu[1]:.1f} ink_bottom={bu[3]:.1f} {u['text'][:60]!r}")
# band rects in ED P1: all rects with height>=10 and y in 400-600
tree = ET.parse(f"{ED}/p1-prima.svg")
for el in tree.iter():
    if el.tag.split("}")[-1] == "rect":
        y = fnum(el.get("y")); h = fnum(el.get("height")); x = fnum(el.get("x")); w = fnum(el.get("width"))
        if 400 <= y <= 600 and w > 500:
            line(f"ED P1 rect x={x} y={y} w={w} h={h} fill={el.get('fill')}")
# core P1 same band
tree = ET.parse(f"{CORE}/p1-prima.svg")
for el in tree.iter():
    if el.tag.split("}")[-1] == "rect":
        y = fnum(el.get("y")); h = fnum(el.get("height")); x = fnum(el.get("x")); w = fnum(el.get("width"))
        if 400 <= y <= 620 and w > 500:
            line(f"CORE P1 rect x={x} y={y} w={w} h={h} fill={el.get('fill')}")
line("CORE P1 nodes y 540-640:")
for t in ce["p1-prima"]:
    if 540 <= fnum(t["y"]) <= 640:
        line(f"   y={t['y']} x={t['x']} fs={t['fs']} {t['text']!r}")
line("W43 whole-issue ITALIA VERA search:")
for p in PAGES:
    s = raw(f"{W43}/{p}.svg")
    line(f"  W43 {p}: ITALIA VERA={s.count('ITALIA VERA')} GIORNALE SETTIMANALE={s.count('GIORNALE SETTIMANALE')}")
line("Siblings badge slots:")
for sib, pat in [("it-de", "ITALIENISCHER"), ("it-en", "ITALIAN")]:
    p = f"{BASE}/files/weekly-report-w45-{sib}/svg/p1-prima.svg"
    if os.path.exists(p):
        for t in load_texts(p):
            if pat in t["text"] and fnum(t["y"]) < 1000 and "ЕЖЕНЕДЕЛЬНИК" not in t["text"] and "WEEKLY" not in t["text"]:
                line(f"  {sib}: y={t['y']} x={t['x']} fs={t['fs']} w={t['weight']} {t['text']!r}")
    else:
        line(f"  {sib}: missing")

# ---- P7 col3 ink bottom vs FRASI rule
sec("5d P7 col3 ink bottom vs FRASI rule line")
# find horizontal lines/rects near y=1686 in ED P7
tree = ET.parse(f"{ED}/p7-lingua.svg")
for el in tree.iter():
    tag = el.tag.split("}")[-1]
    if tag == "line":
        y1, y2, x1, x2 = fnum(el.get("y1")), fnum(el.get("y2")), fnum(el.get("x1")), fnum(el.get("x2"))
        if 1650 <= y1 <= 1720 and y1 == y2:
            line(f"ED P7 hline x1={x1} x2={x2} y={y1} stroke={el.get('stroke')} w={el.get('stroke-width')}")
    if tag == "rect":
        y, h, x, w = fnum(el.get("y")), fnum(el.get("height")), fnum(el.get("x")), fnum(el.get("width"))
        if 1650 <= y <= 1720 and h <= 4 and w > 300:
            line(f"ED P7 thin rect x={x} y={y} w={w} h={h} fill={el.get('fill')}")
# FRASI header node y=1724; col3 = right column x>=989? P7 columns: col1 x=65, col2 x=527?, col3 x=989? Actually FRASI two cols x=65/989.
# col3 texts above FRASI header: x>=989, baseline < 1724, excluding footer; also the letter box is col? Letter at x=?? 
# Print all ED P7 texts with x>=989 and y<1724 sorted by y, with ink bottoms, tail:
col3 = [t for t in ed["p7-lingua"] if fnum(t["x"]) >= 989 and fnum(t["y"]) < 1724]
col3.sort(key=lambda t: fnum(t["y"]))
for t in col3[-14:]:
    b = ink_box(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])
    line(f"   col3 y={t['y']} ink_bottom={b[3]:.1f} {t['text'][:70]!r}")
mx = max(ink_box(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])[3] for t in col3)
line(f"col3 max ink bottom (x>=989, y<1724) = {mx:.1f}; stream col3 end claimed 1646.0")
# also all-column max ink bottom above FRASI header (excluding header itself y=1724)
above = [t for t in ed["p7-lingua"] if fnum(t["y"]) < 1724 and fnum(t["y"]) < 2580]
mx2 = max(ink_box(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])[3] for t in above)
line(f"all-col max ink bottom above FRASI header = {mx2:.1f}")

# ---- P8 keys ink bottom vs stream 2484
sec("5e P8 keys ink bottom (stream claimed 2484, bottom 2552)")
p8 = ed["p8-valutazione"]
# keys region: texts after last separator? Use y>1400 (answers region) excluding footer y=2624
keys = [t for t in p8 if 1400 <= fnum(t["y"]) < 2580]
keys.sort(key=lambda t: fnum(t["y"]))
for t in keys[-8:]:
    b = ink_box(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])
    line(f"   keys y={t['y']} baseline ink_bottom={b[3]:.1f} ink_top={b[1]:.1f} {t['text'][:80]!r}")
mxk = max(ink_box(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])[3] for t in keys)
mxb = max(fnum(t["y"]) for t in keys)
line(f"P8 keys: max baseline={mxb} max ink bottom={mxk:.1f} (stream cursor 2484; footer rule 2580)")

# ---- P1 parola note + row-B rule; P7 parola gloss vs box
sec("5f R1-flag rechecks in final SVGs")
for t in ed["p1-prima"]:
    if "«il primo freddo»" in t["text"] and "холод" in t["text"]:
        b = ink_box(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])
        line(f"P1 parola note: y={t['y']} ink_bottom={b[3]:.1f} {t['text']!r}")
tree = ET.parse(f"{ED}/p1-prima.svg")
for el in tree.iter():
    if el.tag.split("}")[-1] == "line":
        y1, y2 = fnum(el.get("y1")), fnum(el.get("y2"))
        if 1840 <= y1 <= 1900 and y1 == y2:
            line(f"P1 hline y={y1} x1={el.get('x1')} x2={el.get('x2')}")
for t in ed["p7-lingua"]:
    if t["text"].startswith("assaggio ="):
        b = ink_box(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])
        line(f"P7 parola gloss: y={t['y']} ink_bottom={b[3]:.1f} ink_top={b[1]:.1f} {t['text']!r}")
# parola box rect: rects near parola area y 1100-1330, x around parola col (which col? parola box: find rects containing gloss point)
tree = ET.parse(f"{ED}/p7-lingua.svg")
for el in tree.iter():
    if el.tag.split("}")[-1] == "rect":
        x, y, w, h = fnum(el.get("x")), fnum(el.get("y")), fnum(el.get("width")), fnum(el.get("height"))
        if 1080 <= y <= 1330 and 100 <= w <= 950:
            line(f"P7 rect x={x} y={y} w={w} h={h} bottom={y+h}")

# ---- right-edge ADVANCE scan
sec("5g right-edge ADVANCE scan (band [40,1910], masthead exempt by font)")
for p in PAGES:
    flags = []
    for t in ed[p]:
        fam = t["fam"] or ""
        if "Unifraktur" in fam: continue
        b = ink_box(t["text"], fam, fnum(t["fs"]), t["weight"], fnum(t["x"]), fnum(t["y"]), t["anchor"])
        # advance right edge: use adv-based right: for middle anchor adv/2 etc. ink_box right is ink right; compute advance right separately
        # recompute advance right:
        try:
            f = font(SERIFB if (("Serif" in fam) and t["weight"] in ("700","bold")) else SERIF if "Serif" in fam else SANSB if t["weight"] in ("700","bold") else SANS, fnum(t["fs"]))
            adv = f.getlength(t["text"]) / 4.0
        except Exception:
            adv = 0
        if t["anchor"] == "middle": ar = fnum(t["x"]) + adv/2.0
        elif t["anchor"] == "end": ar = fnum(t["x"])
        else: ar = fnum(t["x"]) + adv
        if ar > 1910 or fnum(t["x"]) < 40 and t["anchor"] != "middle":
            flags.append((t["text"][:50], fnum(t["x"]), ar))
    line(f"{p}: ADVANCE right-edge flags={len(flags)} {flags[:5]}")

# ---- frame-line scan + same-baseline furniture scan
sec("5h frame rects + footer rule + same-baseline furniture overlaps")
for p in PAGES:
    s = raw(f"{ED}/{p}.svg")
    has28 = 'width="1894"' in s or True
    tree = ET.parse(f"{ED}/{p}.svg")
    rects = [(fnum(e.get("x")), fnum(e.get("y")), fnum(e.get("width")), fnum(e.get("height"))) for e in tree.iter() if e.tag.split("}")[-1] == "rect"]
    frame = [r for r in rects if r[0] in (28, 40) or (r[2] >= 1800 and r[3] >= 2500)]
    hlines2580 = 0
    for e in tree.iter():
        if e.tag.split("}")[-1] == "line" and fnum(e.get("y1")) == 2580 and fnum(e.get("y2")) == 2580:
            hlines2580 += 1
    line(f"{p}: big rects={frame} footer-rule-2580-lines={hlines2580}")
    # same-baseline: group footer texts y=2624 + P1 top band y=92-ish? check all baselines with >=2 texts for ink overlap
    from collections import defaultdict
    bybase = defaultdict(list)
    for t in ed[p]:
        bybase[round(fnum(t["y"]), 2)].append(t)
    ov = 0
    for y, ts in bybase.items():
        if len(ts) < 2: continue
        boxes = []
        for t in ts:
            b = ink_box(t["text"], t["fam"], fnum(t["fs"]), t["weight"], fnum(t["x"]), y, t["anchor"])
            boxes.append((b[0], b[2], t["text"][:40]))
        boxes.sort()
        for i in range(len(boxes)-1):
            if boxes[i+1][0] < boxes[i][1] - 0.5:
                ov += 1; line(f"   SAME-BASELINE OVERLAP {p} y={y}: {boxes[i]} vs {boxes[i+1]}")
    if ov == 0: line(f"   {p}: same-baseline overlaps=0")

# ---- P6 chart label coverage (baseline-anchored ink)
sec("5i P6 chart label coverage (later rects vs label ink, threshold <30%)")
tree = ET.parse(f"{ED}/p6-approfondimento.svg")
elems = []
for el in tree.iter():
    tag = el.tag.split("}")[-1]
    if tag == "text":
        elems.append(("text", el))
    elif tag == "rect":
        elems.append(("rect", el))
labels = ["Torino","Milano","Bologna","Roma","Napoli","3°","4°","5°","9°","12°"]
worst = []
for i, (kind, el) in enumerate(elems):
    if kind != "text": continue
    txt = "".join(el.itertext())
    if not any(lab in txt for lab in labels): continue
    b = ink_box(txt, el.get("font-family"), fnum(el.get("font-size")), el.get("font-weight"), fnum(el.get("x")), fnum(el.get("y")), el.get("text-anchor"))
    # later rects
    cov = 0.0; area = max((b[2]-b[0])*(b[3]-b[1]), 1e-9)
    for kind2, el2 in elems[i+1:]:
        if kind2 != "rect": continue
        rx, ry, rw, rh = fnum(el2.get("x")), fnum(el2.get("y")), fnum(el2.get("width")), fnum(el2.get("height"))
        ix = max(0, min(b[2], rx+rw) - max(b[0], rx)); iy = max(0, min(b[3], ry+rh) - max(b[1], ry))
        cov = max(cov, ix*iy/area)
    worst.append((txt, b, cov))
    line(f"   label {txt!r} ink=({b[0]:.1f},{b[1]:.1f})-({b[2]:.1f},{b[3]:.1f}) maxcov={cov*100:.1f}%")
line(f"P6 worst coverage = {max(w[2] for w in worst)*100:.1f}%" if worst else "P6: no labels found")

# ---- chip exercise sequences core vs ed
sec("12c chip level sequences (core vs edition, doc order)")
LEVELS = {"A2","B1","B2","A2→B1","A2→B2","B1→B2","A2/B1","B1/B2"}
def chips(tsd):
    out = []
    for p in PAGES:
        ts = tsd[p]
        for i, t in enumerate(ts):
            if t["text"].strip() in LEVELS:
                nxt = ""
                for u in ts[i+1:i+4]:
                    if re.match(r"\s*\d+\s*(–\s*\d+)?\s*\.", u["text"]):
                        nxt = u["text"].strip(); break
                out.append((p, t["text"].strip(), nxt))
    return out
cc, ec = chips(ce), chips(ed)
line(f"core chips={len(cc)} ed chips={len(ec)} sequences identical={cc==ec}")
from collections import Counter
def expand(seq):
    nums = []
    for p, lv, nxt in seq:
        m = re.match(r"(\d+)\s*(?:–\s*(\d+))?", nxt)
        if m:
            a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
            nums.extend(range(a, b+1))
    return nums
for label, seq in [("CORE", cc), ("ED", ec)]:
    nums = expand(seq)
    line(f"{label}: chip-paired numbers: count={len(nums)} unique={len(set(nums))} missing={[n for n in range(1,151) if n not in set(nums)][:20]} dup={[n for n in set(nums) if nums.count(n)>1][:20]}")
    # level distribution: chip level per exercise (range exercises: level applies to whole range? count each number with chip level; for A2→B1 ranges ambiguous — report chip-level counts separately)
    lc = Counter(lv for _, lv, _ in seq)
    line(f"  chip-level node counts: {dict(lc)}")
    # per-page chip counts
    pc = Counter(p for p, _, _ in seq)
    line(f"  per-page chip nodes: {dict(pc)}")
if cc != ec:
    for i, (a, b) in enumerate(zip(cc, ec)):
        if a != b: line(f"  first diff at {i}: core={a} ed={b}"); break

# ---- bytes checks for suspected mojibake spots
sec("bytes: Cyrillic spot checks (codepoint-level)")
for label, path, needle in [("ED-P6-gloss", f"{ED}/p6-approfondimento.svg", "вероятность"),
                            ("ED-P1-gloss", f"{ED}/p1-prima.svg", "Пояснение"),
                            ("ED-P6-gloss-src", f"{BASE}/hidden_files/weekly-report-w45-it-ru-build/content56.py", "вероятность")]:
    s = raw(path)
    line(f"{label}: needle {needle!r} present={needle in s} count={s.count(needle)}")
    idx = s.find(needle)
    if idx >= 0:
        line(f"   context codepoints: {[hex(ord(c)) for c in s[idx-5:idx+5]]}")

open(f"{BASE}/hidden_files/w45/it-ru-proof/scan3.txt", "w").write("\n".join(OUT))
print(f"wrote {len(OUT)} lines")
