#!/usr/bin/env python3
"""Pixel-adjudicate occlusion_audit flags against the rendered PNG cards.
For TEXTX: find runs a/b in the SVG, take the junction column J = b.x (png),
and measure the widest all-background column run within J+-10 over the
flag's ink band. gap>=1px -> CLEAR (false positive), else OVERLAP (real).
For LINEX: check whether text ink extends below the rule's bottom row.
PNG mapping: x_svg * 1.0, y_svg * 1.0 — SVG canvas and cards are both
1950x2700, so svg px == card px. (The old 1950/1800 assumed 1800-wide
cards; that shifted every junction J by up to ~150px and masked
boundary cases — run-log L2785/L2879.)
"""
import json, re, html, sys
from PIL import Image

SX = 1.0
CORE = sys.argv[2] if len(sys.argv) > 2 else "/home/hatch/workspace/weekly-git/production/2026-w47/core-ru"
FLAGS = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ru/occlusion-run1.json"))["flags"]

TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>([^<]*)</text>')
LINE_RE = re.compile(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"')

def load_els(page):
    s = open(f"{CORE}/svg/{page}", encoding="utf-8").read()
    els = []
    for m in TEXT_RE.finditer(s):
        els.append({"x": float(m.group(1)), "y": float(m.group(2)),
                    "t": html.unescape(m.group(3))})
    return els, s

cards = {}
def card(page):
    if page not in cards:
        cards[page] = Image.open(f"{CORE}/cards/{page.replace('.svg', '.png')}").convert("L")
    return cards[page]

def bg_dark(im, x, y0, y1):
    # background = median over a wide strip above and below the band
    vals = []
    for yy in (max(0, y0 - 20), min(im.height - 1, y1 + 20)):
        for dx in range(-100, 101, 10):
            xx = int(x) + dx
            if 0 <= xx < im.width:
                vals.append(im.load()[xx, yy])
    vals.sort()
    return (vals[len(vals) // 2] if vals else 240) < 128

results = []
for f in FLAGS:
    page, cls = f["page"], f["class"]
    box = f["box"]  # svg units [l, t, r, b]
    im = card(page)
    px = im.load()
    if cls == "TEXTX":
        m = re.search(r"ink overlaps '([^']*)'", f["detail"])
        btxt = m.group(1).strip() if m else ""
        btxt = re.sub(r"\\u([0-9a-fA-F]{4})", lambda mm: chr(int(mm.group(1), 16)), btxt).strip()
        els, _ = load_els(page)
        a_cands = [e for e in els if e["t"].strip() == f["text"].strip() and abs(e["x"] - box[0]) < 5
                   and box[1] - 2 <= e["y"] <= box[3] + 10]
        if not a_cands:
            # flag text may be a substring of a longer run (e.g. '! ' inside '!»')
            a_cands = [e for e in els if f["text"].strip() and f["text"].strip() in e["t"]
                       and box[1] - 2 <= e["y"] <= box[3] + 10]
        a = a_cands[0] if a_cands else None
        b = None
        if a:
            # b may sit on EITHER side (audit pairs boxes regardless of order)
            bs = [e for e in els if e["t"].lstrip().startswith(btxt[:12]) and abs(e["y"] - a["y"]) < 5 and e is not a]
            bs.sort(key=lambda e: abs(e["x"] - a["x"]))
            b = bs[0] if bs else None
        if not a or not b:
            results.append((page, cls, f["text"], "UNRESOLVED", ""))
            continue
        J = max(a["x"], b["x"]) * SX  # boundary column between the two runs
        y0, y1 = max(0, int(box[1])), min(im.height - 1, int(box[3]))
        dark_bg = bg_dark(im, J, y0, y1)
        def is_ink(v):
            return v > 160 if dark_bg else v < 180
        # a column counts as ink only with >=2 ink pixels in the band
        # (kills single-row noise from a neighbouring badge/line)
        best, cur = 0, 0
        for cx in range(int(J) - 10, int(J) + 11):
            n = sum(1 for yy in range(y0, y1 + 1) if 0 <= cx < im.width and is_ink(px[cx, yy]))
            col_ink = n >= 2
            cur = 0 if col_ink else cur + 1
            best = max(best, cur)
        verdict = "CLEAR gap=%dpx" % best if best >= 1 else "OVERLAP"
        results.append((page, cls, f["text"], verdict, "vs %r J=%.0f %s" % (b["t"][:20], J, "darkbg" if dark_bg else "lightbg")))
    elif cls == "LINEX":
        m = re.search(r"\[([\d.]+), ([\d.]+), ([\d.]+), ([\d.]+)\]", f["detail"])
        rl, rt, rr, rb = [float(v) for v in m.groups()]
        x0, x1 = max(0, int(box[0] * SX)), min(im.width - 1, int(box[2] * SX))
        # lowest ink row in [rt-40, rb+25] within the ink x-range,
        # excluding the rule rows themselves (rule spans full width;
        # restrict to the ink x-range and check rows below rb)
        rows_below = []
        for yy in range(int(rb) + 1, int(rb) + 26):
            if any(px[xx, yy] < 180 for xx in range(x0, x1)):
                rows_below.append(yy)
        verdict = ("REAL ink %d rows below rule" % len(rows_below)) if rows_below else "CLEAR"
        results.append((page, cls, f["text"], verdict, "rule y=%.1f-%.1f" % (rt, rb)))
    else:
        results.append((page, cls, f["text"], "UNHANDLED", ""))

from collections import Counter
print(Counter(r[3].split()[0] for r in results))
for r in results:
    if not r[3].startswith("CLEAR"):
        print(" !!", r)
print("--- all ---")
for r in results:
    print(r[0], r[1], repr(r[2][:28]), r[3], r[4])
