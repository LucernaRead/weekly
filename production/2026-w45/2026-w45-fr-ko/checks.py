# Gate battery for W45 FR x KO round 1: rowcheck / right-edge /
# frame-line / chart-label / kinsoku / orphan (10-45, >=3-syllable
# tails, line-start closers, paren fragments) / Han nodes / frozen
# strings / gloss counts / image payloads.
import sys, os, re, glob, hashlib, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageFont
import xml.etree.ElementTree as ET

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = f"{BASE}/files/weekly-report-w45-fr-ko"
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
    # Canonical anchoring (tools/occlusion_audit.py ink_box): PIL getbbox
    # is ascender-relative, so subtract getmetrics ascent to get
    # baseline-relative ink. (An earlier revision omitted this and
    # shifted every ink box down by ~ascent.)
    f = font(n["fam"], n["bold"], n["size"])
    try:
        bb = f.getbbox(n["s"])
    except Exception:
        return None
    if bb is None: return None
    adv = f.getlength(n["s"]) / 4
    asc = f.getmetrics()[0] / 4
    if n["anchor"] == "middle":
        left = n["x"] - adv / 2
    elif n["anchor"] == "end":
        left = n["x"] - adv
    else:
        left = n["x"]
    ox0 = bb[0] / 4
    return (left + ox0, n["y"] - asc + bb[1] / 4, left + ox0 + (bb[2] - bb[0]) / 4, n["y"] - asc + bb[3] / 4)

def svgfiles(d):
    return sorted(glob.glob(d + "/svg/*.svg"))

print("== 1. same-baseline rowcheck (y<200 bands + footer y=2624) ==")
bad = 0
for f in svgfiles(ED):
    ns = texts(f)
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
                print(f"  OVERLAP {os.path.basename(f)} y={y}: {s1!r} x1={b1[2]:.0f} vs {s2!r} x0={b2[0]:.0f}")
                bad += 1
print("  rowcheck overlaps:", bad)

print("== 2. ADVANCE right-edge scan (ink right >1885.5) ==")
over = 0
for f in svgfiles(ED):
    for n in texts(f):
        b = inkbox(n)
        if b and b[2] > 1885.5:
            print(f"  {os.path.basename(f)} y={n['y']:.0f} right={b[2]:.0f} :: {n['s'][:60]!r}")
            over += 1
print("  right-edge overflows:", over)

print("== 3. frame-line scan (ink vs outer 28/frame 1922, inner 40/1910) ==")
cross = 0
for f in svgfiles(ED):
    for n in texts(f):
        b = inkbox(n)
        if not b: continue
        if b[0] < 40 or b[2] > 1910 or b[1] < 40 or b[3] > 2660:
            print(f"  {os.path.basename(f)} y={n['y']:.0f} box={tuple(round(v) for v in b)} :: {n['s'][:50]!r}")
            cross += 1
print("  frame crossings:", cross)

print("== 4. P6 chart-label rect overlap (any coverage, element check) ==")
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
                pass
            elif not (b[2] < rx or b[0] > rx + rw or b[3] < ry or b[1] > ry + rh):
                print(f"  chart overlap y={n['y']:.0f} rect=({rx:.0f},{ry:.0f},{rw:.0f}x{rh:.0f}) :: {n['s'][:50]!r}")
                hits += 1
print("  chart-label rect overlaps:", hits)

print("== 5. kinsoku line-start scan (closers) ==")
CLOSERS = set(")]}〉》.,!?%:;\"'」』）〕，。、！？；：")
starts = 0
for f in svgfiles(ED):
    for n in texts(f):
        s = n["s"].strip()
        if s and s[0] in CLOSERS:
            print(f"  {os.path.basename(f)} y={n['y']:.0f} :: {s[:60]!r}")
            starts += 1
print("  line-start closers:", starts)

print("== 6. Han ideographs in rendered edition SVGs (text nodes) ==")
han = re.compile(r'[\u4e00-\u9fff]')
tot = 0
for f in svgfiles(ED):
    n = sum(1 for x in texts(f) if han.search(x["s"]))
    print(f"  {os.path.basename(f)}: {n} Han nodes")
    tot += n
print("  total Han nodes:", tot)

print("== 7. frozen strings in edition SVGs (text nodes only, never raw file: base64 noise) ==")
alls = ""
for f in svgfiles(ED):
    alls += " " + " ".join(n["s"] for n in texts(f))
for s in ["41e édition en 2026 (40e anniversaire)",
          "Si j'étais libre dimanche, j'___ à Nanterre.",
          "plus excitante ou plus frustrante ?",
          "Les jeunes créateurs y rencontrent leur public, en vrai.",
          "Ce calendrier peut encore bouger."]:
    print(f"  {alls.count(s)}x :: {s}")
print("  standalone 40e:", len(re.findall(r"(?<!\d)40e", alls)), " standalone 41e:", len(re.findall(r"(?<!\d)41e", alls)))

print("== 8. orphan scan, dy window 10-45: line-start closers + >=3-syllable mid-word tails + lone fragments ==")
HANG = re.compile(r'[\uac00-\ud7a3]')
def syllables(s):
    return len(HANG.findall(s))
# Source text (transformed content files) adjudicates space-break vs
# mid-word split: tail+head concatenated present in source with no space
# (and NOT with a space) => true mid-word split; spaced form only =>
# ordinary word wrap, not a defect.
SRC = ""
for sf in sorted(glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/content*.py")):
    SRC += open(sf, encoding="utf-8").read() + "\n"
flags = 0
for f in svgfiles(ED):
    ns = texts(f)
    from collections import defaultdict
    cols = defaultdict(list)
    for n in ns:
        cols[round(n["x"])].append(n)
    for x, group in cols.items():
        group.sort(key=lambda n: n["y"])
        for prev, cur in zip(group, group[1:]):
            dy = cur["y"] - prev["y"]
            if dy < 10 or dy > 45: continue
            ps, cs = prev["s"], cur["s"]
            if cs and cs[0] in CLOSERS:
                print(f"  START-CLOSER {os.path.basename(f)} y={cur['y']:.0f} :: {cs[:40]!r} (prev {ps[-20:]!r})")
                flags += 1
            if ps and cs and HANG.search(ps[-1]) and HANG.search(cs[0]) and ps[-1] not in " .,;:!?·—-":
                run = cs.split(" ")[0]
                if syllables(run) >= 3:
                    tail = ps.split(" ")[-1]
                    # Keys-flow notes gain a printed " (note)" wrapper the
                    # source lacks; strip it before matching.
                    tail_c = tail.lstrip("(")
                    run_c = run.rstrip(")")
                    nospace = (tail_c + run_c) in SRC
                    spaced = (tail_c + " " + run_c) in SRC
                    if nospace and not spaced:
                        verdict = "SPLIT>=3"
                    elif spaced and not nospace:
                        verdict = "SPACE-BREAK"
                    elif nospace and spaced:
                        verdict = "AMBIG"
                    else:
                        verdict = "CROSS-BLOCK"
                    if verdict in ("SPLIT>=3", "AMBIG"):
                        print(f"  {verdict} {os.path.basename(f)} y={cur['y']:.0f} :: prev-end {ps[-12:]!r} cur {cs[:30]!r} tail-syll={syllables(run_c)}")
                        flags += 1
            cst = cs.strip()
            if len(cst) <= 2 and HANG.search(cst or " ") and len(ps.strip()) > 10:
                print(f"  LONE-FRAG {os.path.basename(f)} y={cur['y']:.0f} :: {cst!r} (prev {ps[-20:]!r})")
                flags += 1
print("  orphan flags (SPLIT>=3 + START-CLOSER + LONE-FRAG, SPACE-BREAK excluded):", flags)

print("== 9. gloss counts (split gloss() call strings on ·, README #21) ==")
total = 0
for sf in sorted(glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/content*.py")):
    for m in re.finditer(r'\.gloss\("([^"]*)"\)', open(sf, encoding="utf-8").read()):
        items = m.group(1).split("·")
        print(f"  {os.path.basename(sf)}: {len(items)} items :: {m.group(1)[:40]!r}")
        total += len(items)
print("  gloss total:", total, "(core 38)")
