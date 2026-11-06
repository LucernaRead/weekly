# Gate battery: rowcheck / right-edge / frame-line / chart-label / kinsoku
# / freeze-diff / registry / gloss / gold sentences / 40e / images / CJK.
import sys, os, re, glob, hashlib, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageFont
import xml.etree.ElementTree as ET

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = f"{BASE}/files/weekly-report-w45-fr-en"
CO = f"{BASE}/files/weekly-report-w45-fr-core"
FONTS = "/usr/share/fonts/opentype/noto/"
def font(fam, bold, size):
    if fam == "serif":
        p = FONTS + ("NotoSerifCJK-Bold.ttc" if bold else "NotoSerifCJK-Regular.ttc")
    elif fam == "sans":
        p = FONTS + ("NotoSansCJK-Bold.ttc" if bold else "NotoSansCJK-Regular.ttc")
    else:
        p = os.path.expanduser("~/.local/share/fonts/UnifrakturMaguntia.ttf")
    try:
        return ImageFont.truetype(p, int(round(size * 4)), index=2)
    except Exception:
        return ImageFont.truetype(p, int(round(size * 4)))

def texts(path):
    t = ET.parse(path).getroot(); out = []
    for el in t.iter():
        if el.tag.endswith("text"):
            out.append({"x": float(el.get("x") or 0), "y": float(el.get("y") or 0),
                        "size": float(el.get("font-size") or 20),
                        "bold": el.get("font-weight") == "bold",
                        "anchor": el.get("text-anchor") or "start",
                        "fam": "serif" if "serif" in (el.get("font-family") or "") else ("sans" if "sans" in (el.get("font-family") or "") else "other"),
                        "s": "".join(el.itertext())})
    return out

def inkbox(n):
    # 4x supersampled true ink via getbbox, like the canonical audit
    f = font(n["fam"], n["bold"], n["size"])
    try:
        bb = f.getbbox(n["s"])
    except Exception:
        return None
    if bb is None: return None
    x0, y0, x1, y1 = [v / 4 for v in bb]
    if n["anchor"] == "middle":
        cx = n["x"]; x0, x1 = cx + x0 - (x1 - x0) / 2 - x0, 0  # placeholder, recomputed below
    # simpler: use getlength for advance + bbox offsets
    adv = f.getlength(n["s"]) / 4
    if n["anchor"] == "middle":
        left = n["x"] - adv / 2
    elif n["anchor"] == "end":
        left = n["x"] - adv
    else:
        left = n["x"]
    # bbox offsets are relative to origin at baseline start for start-anchor
    ox0 = bb[0] / 4
    return (left + ox0, n["y"] + bb[1] / 4, left + ox0 + (bb[2] - bb[0]) / 4, n["y"] + bb[3] / 4)

print("== 1. same-baseline rowcheck (furniture bands) ==")
bad = 0
for p in range(1, 9):
    ns = texts(f"{ED}/svg/{sorted(glob.glob(ED+'/svg/*.svg'))[p-1].split('/')[-1]}")
    # group by baseline y (rounded) within furniture bands: y<200 (bands) and footer y=2624
    from collections import defaultdict
    rows = defaultdict(list)
    for n in ns:
        if n["y"] < 200 or abs(n["y"] - 2624) < 1:
            rows[round(n["y"])].append(n)
    for y, group in rows.items():
        boxes = []
        for n in group:
            b = inkbox(n)
            if b: boxes.append((b, n["s"][:40]))
        boxes.sort()
        for (b1, s1), (b2, s2) in zip(boxes, boxes[1:]):
            if b2[0] < b1[2] - 1:
                print(f"  OVERLAP p{p} y={y}: {s1!r} x1={b1[2]:.0f} vs {s2!r} x0={b2[0]:.0f}")
                bad += 1
print("  rowcheck overlaps:", bad)

print("== 2. ADVANCE right-edge scan (all pages, ink vs x=1885 inner / 1922 frame) ==")
over = 0
for f in sorted(glob.glob(ED + "/svg/*.svg")):
    for n in texts(f):
        b = inkbox(n)
        if b and b[2] > 1885.5:
            print(f"  {os.path.basename(f)} y={n['y']:.0f} right={b[2]:.0f} :: {n['s'][:60]!r}")
            over += 1
print("  right-edge overflows:", over)

print("== 3. frame-line scan (text ink vs page frame rects x=28/40, y=28/40, w=1894/1870) ==")
# frame rects: outer (28,28,1894,2644), inner (40,40,1870,2620). Flag ink crossing them.
cross = 0
for f in sorted(glob.glob(ED + "/svg/*.svg")):
    for n in texts(f):
        b = inkbox(n)
        if not b: continue
        if b[0] < 40 or b[2] > 1910 or b[1] < 40 or b[3] > 2660:
            # allow masthead wordmark? wordmark is inside; flag all for review
            print(f"  {os.path.basename(f)} y={n['y']:.0f} box={tuple(round(v) for v in b)} :: {n['s'][:50]!r}")
            cross += 1
print("  frame crossings:", cross)

print("== 4. P6 chart-label baseline-anchored coverage (getmetrics method) ==")
# chart rows on P6: day labels at x=chx+22, values at chx+200; bars? P6 chart has
# no bars (text rows only) -- check label ink vs any later-drawn rect on P6.
# Use card pixels: for each chart row text, sample its ink bbox region and
# report % of dark pixels covered by rect fills is not applicable (no bars);
# instead verify no rect element overlaps a chart text ink box.
t = ET.parse(f"{ED}/svg/p6-politique.svg").getroot()
rects = []
for el in t.iter():
    if el.tag.endswith("rect"):
        try: rects.append((float(el.get("x")), float(el.get("y")), float(el.get("width")), float(el.get("height"))))
        except (TypeError, ValueError): pass
hits = 0
for n in texts(f"{ED}/svg/p6-politique.svg"):
    if 1330 <= n["y"] <= 1800 and n["x"] < 1000:
        b = inkbox(n)
        if not b: continue
        for (rx, ry, rw, rh) in rects:
            if rx <= b[0] and ry <= b[1] and rx + rw >= b[2] and ry + rh >= b[3]:
                pass  # containing box, not a cover
            elif not (b[2] < rx or b[0] > rx + rw or b[3] < ry or b[1] > ry + rh):
                # partial overlap with a non-containing rect drawn later = cover risk
                print(f"  chart overlap y={n['y']:.0f} rect=({rx:.0f},{ry:.0f},{rw:.0f}x{rh:.0f}) :: {n['s'][:50]!r}")
                hits += 1
print("  chart-label rect overlaps:", hits, "(chart has text rows only, no bars)")

print("== 5. kinsoku line-start scan (all pages) ==")
CLOSERS = set(")]}〉》.,!?%:;\"'」』）〕，。、！？；：")
starts = 0
for f in sorted(glob.glob(ED + "/svg/*.svg")):
    for n in texts(f):
        s = n["s"].strip()
        if s and s[0] in CLOSERS:
            print(f"  {os.path.basename(f)} y={n['y']:.0f} :: {s[:60]!r}")
            starts += 1
print("  line-start closers:", starts)

print("== 6. CJK in rendered edition SVGs (text nodes) ==")
cjk = re.compile(r'[\u4e00-\u9fff]')
tot = 0
for f in sorted(glob.glob(ED + "/svg/*.svg")):
    n = sum(1 for x in texts(f) if cjk.search(x["s"]))
    print(f"  {os.path.basename(f)}: {n} CJK nodes")
    tot += n
print("  total CJK nodes:", tot)
