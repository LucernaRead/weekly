# -*- coding: utf-8 -*-
"""Round-2 geometry supplements (tools/occlusion_audit.py is canonical and
already reads 0/0/0; these cover its known blind spots):
 - ADVANCE right-edge scan: every text element, PIL advance width, limit
   x=1885.5 (RIGHT=1885); centered/end anchors handled.
 - Frame-line scan: every <line> vs every text ink band
   (baseline -0.88em .. +0.30em) with x-overlap -> flag for adjudication.
 - P6 chart label coverage, baseline-anchored ink method: label ink boxes
   (PIL getbbox at 4x, JP faces) vs later-drawn bar rects; gate <30%.
 - Kinsoku: rendered lines starting with a canonical NO_START closer.
Run with the tools venv python."""
import glob
import os
import re
import sys

from PIL import ImageFont

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-ja-ko/svg")
CORE = os.path.join(BASE, "files/weekly-report-w45-ja-core/svg")
FONTS = "/usr/share/fonts/opentype/noto"


def sc_index(path):
    for i in range(12):
        try:
            f = ImageFont.truetype(path, 40, index=i)
            if f.getname()[0].endswith("JP"):
                return i
        except Exception:
            break
    return 0


_cache = {}


def font(kind, bold, size):
    path = {"serif": os.path.join(FONTS, "NotoSerifCJK-Bold.ttc" if bold else "NotoSerifCJK-Regular.ttc"),
            "sans": os.path.join(FONTS, "NotoSansCJK-Bold.ttc" if bold else "NotoSansCJK-Regular.ttc")}[kind]
    key = (path, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, size, index=sc_index(path))
    return _cache[key]


def parse(path):
    src = open(path, encoding="utf-8").read()
    els = []
    for m in re.finditer(r'<text ([^>]*)>([^<]*)</text>', src):
        a, t = m.group(1), m.group(2)
        x = float(re.search(r'x="([\d.]+)"', a).group(1))
        y = float(re.search(r'y="([\d.]+)"', a).group(1))
        size = float(re.search(r'font-size="([\d.]+)"', a).group(1))
        fam = re.search(r'font-family="([^"]+)"', a).group(1)
        bold = 'font-weight="700"' in a
        anch = re.search(r'text-anchor="([^"]+)"', a)
        anch = anch.group(1) if anch else "start"
        kind = "serif" if "Serif" in fam else ("sans" if "Sans" in fam else "other")
        els.append({"x": x, "y": y, "size": size, "bold": bold, "anchor": anch, "kind": kind, "text": t})
    lines = []
    for m in re.finditer(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"[^>]*stroke-width="([\d.]+)"', src):
        lines.append({"x1": float(m.group(1)), "y1": float(m.group(2)),
                      "x2": float(m.group(3)), "y2": float(m.group(4)), "w": float(m.group(5))})
    rects = []
    for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]+)"', src):
        rects.append({"x": float(m.group(1)), "y": float(m.group(2)),
                      "w": float(m.group(3)), "h": float(m.group(4)), "fill": m.group(5)})
    return src, els, lines, rects


def adv(e):
    if e["kind"] == "other" or not e["text"]:
        return 0.0
    return font(e["kind"], e["bold"], int(e["size"]) if e["size"] == int(e["size"]) else e["size"]).getlength(e["text"])


print("=== ADVANCE right-edge scan (limit 1885.5) ===")
for d, label in [(ED, "ed"), (CORE, "core")]:
    bad = []
    for f in sorted(glob.glob(os.path.join(d, "*.svg"))):
        _, els, _, _ = parse(f)
        for e in els:
            w = adv(e)
            if e["anchor"] == "start":
                right = e["x"] + w
            elif e["anchor"] == "end":
                right = e["x"]
            else:
                right = e["x"] + w / 2
            if right > 1885.5:
                bad.append((os.path.basename(f), e["x"], e["y"], right, e["text"][:50]))
    print(f"  {label}: violations={len(bad)}")
    for b in bad:
        print("   ", b)

print("=== frame-line scan (line y inside a text ink band + x overlap) ===")
for d, label in [(ED, "ed"), (CORE, "core")]:
    flags = []
    for f in sorted(glob.glob(os.path.join(d, "*.svg"))):
        _, els, lines, _ = parse(f)
        for ln in lines:
            if ln["y1"] != ln["y2"]:
                continue
            ly = ln["y1"]
            for e in els:
                if not e["text"]:
                    continue
                top, bot = e["y"] - 0.88 * e["size"], e["y"] + 0.30 * e["size"]
                if top <= ly <= bot:
                    w = adv(e)
                    if e["anchor"] == "start":
                        x0, x1 = e["x"], e["x"] + w
                    elif e["anchor"] == "end":
                        x0, x1 = e["x"] - w, e["x"]
                    else:
                        x0, x1 = e["x"] - w / 2, e["x"] + w / 2
                    if x0 <= ln["x2"] and x1 >= ln["x1"]:
                        flags.append((os.path.basename(f), ly, e["text"][:50], e["y"]))
    print(f"  {label}: flags={len(flags)}")
    for fl in flags:
        print("   ", fl)

print("=== P6 chart-label ink coverage vs bars (gate <30%) ===")
for d, label in [(ED, "ed"), (CORE, "core")]:
    src, els, _, rects = parse(os.path.join(d, "p6-fukayomi.svg"))
    # chart labels: the 4 category texts + value texts near the chart area;
    # bars are the wide rects drawn after them in document order.
    # Identify by document order: find label texts, then rects after them.
    order = []
    for m in re.finditer(r'<text ([^>]*)>([^<]*)</text>|<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]+)"', src):
        if m.group(2) is not None:
            a, t = m.group(1), m.group(2)
            order.append(("text", float(re.search(r'x="([\d.]+)"', a).group(1)),
                          float(re.search(r'y="([\d.]+)"', a).group(1)), t, a))
        else:
            order.append(("rect", float(m.group(3)), float(m.group(4)),
                          float(m.group(5)), float(m.group(6)), m.group(7)))
    labels = ["近場の満足", "温泉", "紅葉", "グルメ"]
    maxcov = 0.0
    for kind, x, y, t, a in [o for o in order if o[0] == "text"]:
        if t not in labels:
            continue
        size = float(re.search(r'font-size="([\d.]+)"', a).group(1))
        bold = 'font-weight="700"' in a
        fam = re.search(r'font-family="([^"]+)"', a).group(1)
        k = "serif" if "Serif" in fam else "sans"
        fnt = font(k, bold, int(size) if size == int(size) else size)
        # 4x supersampled ink box
        bb = fnt.getbbox(t)
        # getbbox is relative to anchor baseline-left; approximate ink box:
        ix0, iy0, ix1, iy1 = x + bb[0], y + bb[1], x + bb[2], y + bb[3]
        ink_area = max(0.0, (ix1 - ix0) * (iy1 - iy0))
        idx = order.index(("text", x, y, t, a))
        for o in order[idx + 1:]:
            if o[0] != "rect":
                continue
            _, rx, ry, rw, rh, fill = o
            if fill in ("none", "#f7f1e2"):
                continue
            ox = max(0.0, min(ix1, rx + rw) - max(ix0, rx))
            oy = max(0.0, min(iy1, ry + rh) - max(iy0, ry))
            if ink_area:
                maxcov = max(maxcov, ox * oy / ink_area)
    print(f"  {label}: max label ink coverage = {maxcov:.3f}")

print("=== kinsoku (rendered lines starting with canonical NO_START) ===")
NO_START = set("。、，．！？：；）」』】ー…‥・")
for d, label in [(ED, "ed"), (CORE, "core")]:
    hits = []
    for f in sorted(glob.glob(os.path.join(d, "*.svg"))):
        _, els, _, _ = parse(f)
        for e in els:
            if e["text"] and e["text"][0] in NO_START:
                hits.append((os.path.basename(f), e["y"], e["text"][:40]))
    print(f"  {label}: hits={len(hits)}")
    for h in hits:
        print("   ", h)
