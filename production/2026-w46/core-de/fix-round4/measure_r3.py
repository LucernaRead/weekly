#!/usr/bin/env python3
"""Round 4 measurement: advance + true-ink extents for zh-cn P8 (Round 3 state)
and the de-core duplicate (Round 2 state). Read-only."""
import re, html, sys, os, json
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-de-zh-cn-build"))
import occlusion_audit as OA
from svglib import text_w

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")

def elements(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'<text[^>]*>(.*?)</text>', s, re.S):
        tag = m.group(0)
        attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', tag.split(">", 1)[0]))
        t = html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))
        out.append((attrs, t))
    return out

def report(label, svgdir):
    p8 = os.path.join(svgdir, "p8-uebungen.svg")
    els = elements(p8)
    print(f"== {label}: {len(els)} text elements ==")
    keys = []
    for attrs, t in els:
        size = float(attrs.get("font-size", "0"))
        if size == 14.5:
            keys.append((attrs, t))
    print(f"keys-size (14.5) elements: {len(keys)}")
    COLX = [65, 527, 989, 1451]
    over_adv, over_ink = [], []
    for attrs, t in keys:
        x = float(attrs["x"]); y = float(attrs["y"])
        fam = attrs.get("font-family", "Noto Sans CJK SC")
        bold = attrs.get("font-weight") == "700"
        adv = text_w(t, "sans", bold, 14.5)
        box = OA.ink_box(t, fam, 14.5, bold, x, y, attrs.get("text-anchor", "start"))
        col = COLX.index(x) if x in COLX else None
        edge = x + 434 if col is not None else None
        if adv > 434:
            over_adv.append((x, y, adv, box[2] if box else None, t[:70]))
        if box and col is not None and box[2] > edge:
            over_ink.append((x, y, adv, box[2], edge, t[:70]))
    print(f"keys lines advance>434: {len(over_adv)}")
    for r in over_adv:
        print(f"  ADV x={r[0]} y={r[1]} adv={r[2]:.1f} inkR={r[3]} :: {r[4]!r}")
    print(f"keys lines inkR>column edge: {len(over_ink)}")
    for r in over_ink:
        print(f"  INK x={r[0]} y={r[1]} adv={r[2]:.1f} inkR={r[3]:.1f} edge={r[4]} :: {r[5]!r}")
    ys = [float(a["y"]) for a, t in keys]
    print(f"keys baseline range: {min(ys)} .. {max(ys)}; last keys line y={max(ys)}")
    # the two defect lines specifically
    for attrs, t in keys:
        if "singen" in t and float(attrs["y"]) == 2198.02:
            x = float(attrs["x"]); y = float(attrs["y"])
            print(f"D-R3-2 line: x={x} y={y} adv={text_w(t,'sans',False,14.5):.1f} ink={OA.ink_box(t, attrs.get('font-family','Noto Sans CJK SC'), 14.5, False, x, y)} :: {t!r}")
        if "Falsch" in t and float(attrs["y"]) == 2523.12:
            x = float(attrs["x"]); y = float(attrs["y"])
            print(f"D-R3-1 line: x={x} y={y} adv={text_w(t,'sans',False,14.5):.1f} ink={OA.ink_box(t, attrs.get('font-family','Noto Sans CJK SC'), 14.5, False, x, y)} :: {t!r}")
    return keys

report("zh-cn Round3", os.path.join(GOAL, "weekly-report-w46-de-zh-cn/svg"))
report("de-core Round2", os.path.join(GOAL, "weekly-report-w46-de-core/svg"))

# P1-P7 census: any line (any size) with advance > its column width?
print("== P1-P7 advance census (zh-cn, all sizes; wrap max_w varies, report >434 only for info) ==")
for pg in ["p1-front.svg","p2-leben.svg","p3-kultur.svg","p4-sport.svg","p5-jugend.svg","p6-vertiefung.svg","p7-sprache.svg"]:
    els = elements(os.path.join(GOAL, "weekly-report-w46-de-zh-cn/svg", pg))
    n = 0
    for attrs, t in els:
        size = float(attrs.get("font-size", "0"))
        kind = "serif" if "Serif" in attrs.get("font-family","") else "sans"
        bold = attrs.get("font-weight") == "700"
        adv = text_w(t, kind, bold, size) if size else 0
        if adv > 434:
            n += 1
            print(f"  {pg} x={attrs.get('x')} y={attrs.get('y')} size={size} adv={adv:.1f} :: {t[:50]!r}")
    print(f"  {pg}: {n} lines advance>434 (of {len(els)})")
