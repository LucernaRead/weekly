# -*- coding: utf-8 -*-
"""W45 IT x KO builder scans (not deliverables):
1. Han chars per edition SVG (must be 0).
2. Korean orphan scan, window 10-45 (README #16, W45 extension):
   consecutive SVG text nodes in file order (same column wrap, or column
   transition) whose break splits a source word; tail = first token of the
   continuation line, syllables counted in Hangul; gate is tail >= 3.
   Also: continuation lines starting with orphan punctuation, and lone
   block-final fragments.
3. Right-edge ADVANCE scan (PIL advance widths per anchor, band [40,1910]).
4. Same-baseline collision scan on P1 top band (y=92) and footers (y=2624).
5. P6 chart-label coverage, baseline-anchored ink (PIL getmetrics, anchor
   ls), later-drawn rects vs label ink; gate <30%.
Usage: tools/venv/bin/python ko_scans.py <edition-svg-dir> <build-dir>
"""
import os
import re
import sys
import glob
from PIL import ImageFont

ED = sys.argv[1]
BUILD = sys.argv[2]

FONTS = {
    ("serif", False): "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc",
    ("serif", True): "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc",
    ("sans", False): "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    ("sans", True): "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
}
# tables.json font table: split TTC face indices JP=0 KR=1 SC=2 TC=3 HK=4.
# The SVGs declare "Noto Sans/Serif CJK SC", so measurement uses the SC
# face (index 2) to match the declared family; CJK advances are em-wide
# in every face, so the choice does not move any gate.
KR = 2


def font(family, bold, size):
    path = FONTS.get((family, bold), FONTS[("sans", False)])
    try:
        return ImageFont.truetype(path, size, index=KR)
    except Exception:
        return ImageFont.truetype(path, size)


def parse_svg(path):
    s = open(path, encoding="utf-8").read()
    nodes = []
    for m in re.finditer(
            r'<text x="([\d.]+)" y="([\d.]+)"(?: font-family="([^"]*)")?'
            r'(?: font-size="([\d.]+)")?(?: font-weight="([^"]*)")?'
            r'(?: fill="([^"]*)")?(?: text-anchor="([^"]*)")?[^>]*>([^<]*)</text>',
            s):
        x, y = float(m.group(1)), float(m.group(2))
        fam = m.group(3) or ""
        size = float(m.group(4)) if m.group(4) else 20.0
        bold = (m.group(5) == "700")
        anchor = m.group(7) or "start"
        nodes.append({"x": x, "y": y, "fam": fam, "size": size,
                      "bold": bold, "anchor": anchor, "t": m.group(8)})
    rects = []
    for m in re.finditer(
            r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"',
            s):
        rects.append(tuple(float(v) for v in m.groups()))
    # rect draw order relative to texts: use file positions
    order = []
    for m in re.finditer(r'<(text|rect)[ >]', s):
        order.append(m.group(1))
    return nodes, rects, s


def is_hangul(ch):
    return "\uac00" <= ch <= "\ud7a3"


def syllables(tok):
    return sum(1 for c in tok if is_hangul(c))


def strip_punct(tok):
    return tok.strip("()[]{}<>\"'“”‘’·,.;:!?。，、：；？！）》」』")


# ---- source tokens (Korean words) ----
src_tokens = set()
for f in ["content12.py", "content34.py", "content56.py", "content7.py",
          "content8.py"]:
    s = open(os.path.join(BUILD, f), encoding="utf-8").read()
    for lit in re.findall(r'"(?:[^"\\]|\\.)*"', s):
        body = lit[1:-1]
        if any(is_hangul(c) for c in body):
            for tok in body.split():
                st = strip_punct(tok)
                if st:
                    src_tokens.add(st)

ORPHAN_START = set("。，、：；？！）》」』.?!)")

print("=== 1. Han chars per page (gate 0) ===")
han_total = 0
for p in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    s = open(p, encoding="utf-8").read()
    texts = re.findall(r'<text[^>]*>([^<]*)</text>', s)
    n = sum(1 for t in texts for c in t if "\u4e00" <= c <= "\u9fff")
    han_total += n
    print(f"  {os.path.basename(p)}: Han={n}")
print("  TOTAL Han:", han_total)

print("=== 2. Korean orphan scan (window 10-45) ===")
cands = []
line_start_orphan = []
for p in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    nodes, _, _ = parse_svg(p)
    pg = os.path.basename(p)
    for a, b in zip(nodes, nodes[1:]):
        if not any(is_hangul(c) for c in a["t"]):
            continue
        dy = b["y"] - a["y"]
        same_col = abs(b["x"] - a["x"]) < 1
        col_trans = b["x"] > a["x"] + 100 and b["y"] < a["y"]
        if not ((same_col and 10 <= dy <= 45) or col_trans):
            continue
        if re.match(r"^\d+[.\-–]", b["t"].strip()):
            continue
        # line-start orphan punctuation (Korean continuation lines)
        if b["t"] and b["t"][0] in ORPHAN_START and any(
                is_hangul(c) for c in b["t"]):
            line_start_orphan.append((pg, a["y"], b["y"], a["t"], b["t"]))
        atoks = a["t"].split()
        btoks = b["t"].split()
        if not atoks or not btoks:
            continue
        frag1 = strip_punct(atoks[-1])
        frag2 = strip_punct(btoks[0])
        if frag1 and frag2 and (frag1 + frag2) in src_tokens:
            cands.append((pg, a["y"], b["y"], a["t"], b["t"],
                          frag1, frag2, syllables(frag2)))
print(f"  mid-word split candidates: {len(cands)}")
for c in cands:
    flag = "GATE>=3" if c[7] >= 3 else "ok(<3)"
    print(f"  [{flag}] {c[0]} y {c[1]}->{c[2]} tail_syll={c[7]} "
          f"frag {c[5]}|{c[6]} :: {c[3]!r} // {c[4]!r}")
print(f"  line-start orphan punctuation: {len(line_start_orphan)}")
for o in line_start_orphan:
    print(f"  [ORPHAN-START] {o[0]} y {o[1]}->{o[2]} :: {o[3]!r} // {o[4]!r}")

print("=== 3. Right-edge ADVANCE scan (band [40,1910]) ===")
edge_flags = 0
for p in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    nodes, _, _ = parse_svg(p)
    pg = os.path.basename(p)
    for nd in nodes:
        fam = "serif" if "Serif" in nd["fam"] else "sans"
        f = font(fam, nd["bold"], int(round(nd["size"])))
        adv = f.getlength(nd["t"])
        if nd["anchor"] == "middle":
            lo, hi = nd["x"] - adv / 2, nd["x"] + adv / 2
        elif nd["anchor"] == "end":
            lo, hi = nd["x"] - adv, nd["x"]
        else:
            lo, hi = nd["x"], nd["x"] + adv
        if lo < 40 or hi > 1910:
            edge_flags += 1
            print(f"  [EDGE] {pg} y={nd['y']} anchor={nd['anchor']} "
                  f"[{lo:.1f},{hi:.1f}] {nd['t'][:60]!r}")
print("  EDGE flags:", edge_flags)

print("=== 4. Same-baseline collisions (P1 y=92, footers y=2624) ===")
base_flags = 0
for p in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    nodes, _, _ = parse_svg(p)
    pg = os.path.basename(p)
    for yy in (92.0, 2624.0):
        band = [nd for nd in nodes if abs(nd["y"] - yy) < 1]
        ivs = []
        for nd in band:
            fam = "serif" if "Serif" in nd["fam"] else "sans"
            f = font(fam, nd["bold"], int(round(nd["size"])))
            adv = f.getlength(nd["t"])
            if nd["anchor"] == "middle":
                lo, hi = nd["x"] - adv / 2, nd["x"] + adv / 2
            elif nd["anchor"] == "end":
                lo, hi = nd["x"] - adv, nd["x"]
            else:
                lo, hi = nd["x"], nd["x"] + adv
            ivs.append((lo, hi, nd["t"]))
        ivs.sort()
        for (l1, h1, t1), (l2, h2, t2) in zip(ivs, ivs[1:]):
            if h1 > l2:
                base_flags += 1
                print(f"  [BASE] {pg} y={yy}: {t1!r} overlaps {t2!r}")
print("  BASE flags:", base_flags)

print("=== 5. P6 chart-label coverage (baseline-anchored ink, gate <30%) ===")
p6 = os.path.join(ED, "p6-approfondimento.svg")
s = open(p6, encoding="utf-8").read()
# text nodes with file order + rect nodes with file order
events = []
for m in re.finditer(
        r'<text x="([\d.]+)" y="([\d.]+)"(?: font-family="([^"]*)")?'
        r'(?: font-size="([\d.]+)")?(?: font-weight="([^"]*)")?'
        r'(?: fill="([^"]*)")?(?: text-anchor="([^"]*)")?[^>]*>([^<]*)</text>',
        s):
    events.append((m.start(), "text", m))
for m in re.finditer(
        r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*>',
        s):
    events.append((m.start(), "rect", m))
events.sort()
labels = ["Torino", "Milano", "Bologna", "Roma", "Napoli"]
maxcov = 0.0
for pos, kind, m in events:
    if kind != "text":
        continue
    t = m.group(8)
    if t not in labels and not re.fullmatch(r"\d+°", t):
        continue
    x, y = float(m.group(1)), float(m.group(2))
    fam = "serif" if "Serif" in (m.group(3) or "") else "sans"
    size = float(m.group(4)) if m.group(4) else 20.0
    bold = (m.group(5) == "700")
    f = font(fam, bold, int(round(size)))
    # baseline-anchored ink: getmetrics ascent/descent, anchor ls
    asc, desc = f.getmetrics()
    left, top, right, bottom = f.getbbox(t, anchor="ls")
    # getbbox with anchor ls returns box relative to (0,0)=baseline start;
    # approximate ink box: (x+left, y+top, x+right, y+bottom)
    ix0, iy0, ix1, iy1 = x + left, y + top, x + right, y + bottom
    iarea = max(0.0, ix1 - ix0) * max(0.0, iy1 - iy0)
    if iarea == 0:
        continue
    for pos2, kind2, m2 in events:
        if pos2 <= pos or kind2 != "rect":
            continue
        rx, ry, rw, rh = (float(v) for v in m2.groups())
        ox = max(0.0, min(ix1, rx + rw) - max(ix0, rx))
        oy = max(0.0, min(iy1, ry + rh) - max(iy0, ry))
        cov = ox * oy / iarea * 100
        if cov > maxcov:
            maxcov = cov
        if cov > 0:
            print(f"  label {t!r} covered {cov:.1f}% by rect "
                  f"({rx},{ry},{rw}x{rh})")
print(f"  MAX chart-label coverage: {maxcov:.1f}% (gate <30%)")
