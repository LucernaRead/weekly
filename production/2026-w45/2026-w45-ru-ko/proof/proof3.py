#!/usr/bin/env python3
"""Independent RUxKO W45 proof script 3: differing-rect adjudication + P6 bars + P7 box + P8 flow."""
import re, collections
from pathlib import Path

BASE = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/files")
CORE = BASE/"weekly-report-w45-ru-core/svg"
ED = BASE/"weekly-report-w45-ru-ko/svg"

def elems(path):
    t = Path(path).read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', t):
        attrs = m.group(1); s = m.group(2)
        def g(k):
            mm = re.search(rf'{k}="([^"]*)"', attrs); return mm.group(1) if mm else ""
        out.append({"x": float(g("x") or 0), "y": float(g("y") or 0),
                    "size": float(g("font-size") or 0), "s": s})
    return out

def inside(els, x, y, w, h):
    return [e for e in els if x <= e["x"] <= x+w and y <= e["y"] <= y+h]

print("== P2 differing rect (989,200,434) contents ==")
for label, d in (("core h=115.95", CORE), ("edition h=145.675", ED)):
    h = 115.95 if label.startswith("core") else 145.675
    print(f"--- {label} ---")
    for e in inside(elems(d/"p2-zhizn.svg"), 989, 200, 434, h):
        print(f"  y={e['y']} size={e['size']} {e['s']!r}")
    # also texts just below box
    print("  texts y 200-400 x 989-1423 (all):")
    for e in elems(d/"p2-zhizn.svg"):
        if 989 <= e["x"] <= 1423 and 200 <= e["y"] <= 400:
            print(f"    y={e['y']} {e['s']!r}")

print("\n== P5 differing rect (527,828.95,434) contents ==")
for label, d, h in (("core h=86.225", CORE, 86.225), ("edition h=115.95", ED, 115.95)):
    print(f"--- {label} ---")
    for e in inside(elems(d/"p5-molodezh.svg"), 527, 828.95, 434, h):
        print(f"  y={e['y']} size={e['size']} {e['s']!r}")

print("\n== P8 chip shift: texts around x=1451 y 380-480 ==")
for label, d in (("core", CORE), ("edition", ED)):
    print(f"--- {label} ---")
    for e in elems(d/"p8-test.svg"):
        if 1400 <= e["x"] <= 1900 and 360 <= e["y"] <= 500:
            print(f"  x={e['x']} y={e['y']} size={e['size']} {e['s']!r}")
print("== P8 column bottoms (max answer-line y per column x) ==")
for label, d in (("core", CORE), ("edition", ED)):
    els = [e for e in elems(d/"p8-test.svg") if e["size"] in (13.3, 13.0)]
    for colx in (65, 527, 989, 1451):
        col = [e for e in els if e["x"] == colx]
        if col: print(f"  {label} col x={colx}: n={len(col)} max_y={max(e['y'] for e in col)}")

print("\n== P6 bars (widths 600/494/388/282) ==")
for label, d in (("core", CORE), ("edition", ED)):
    t = (d/"p6-razbor.svg").read_text(encoding="utf-8")
    bars = []
    for m in re.finditer(r'<rect([^>]*)/>', t):
        attrs = m.group(1)
        def g(k):
            mm = re.search(rf'{k}="([^"]*)"', attrs); return mm.group(1) if mm else ""
        try: w, h, x, y = float(g("width")), float(g("height")), float(g("x")), float(g("y"))
        except: continue
        if w in (600.0, 494.0, 388.0, 282.0):
            bars.append((w, h, x, y, g("fill")))
    print(f"  {label}: {sorted(bars, key=lambda b: -b[0])}")
    # % label baselines vs bar geometry: labels y from before: 1634/1680/1726/1772 step 46
    els = elems(d/"p6-razbor.svg")
    for e in els:
        if e["s"].strip().endswith("%"):
            print(f"    label {e['s']} x={e['x']} y={e['y']}")

print("\n== P7 rects with bottom near 1727.58 ==")
for label, d in (("core", CORE), ("edition", ED)):
    t = (d/"p7-yazyk.svg").read_text(encoding="utf-8")
    hits = []
    for m in re.finditer(r'<rect([^>]*)/>', t):
        attrs = m.group(1)
        def g(k):
            mm = re.search(rf'{k}="([^"]*)"', attrs); return mm.group(1) if mm else ""
        try: x, y, w, h = float(g("x")), float(g("y")), float(g("width")), float(g("height"))
        except: continue
        if abs((y+h) - 1727.58) < 1.0:
            hits.append((x, y, w, h, y+h))
    print(f"  {label}: {hits}")
    # lines near 1756
    for m in re.finditer(r'<line([^>]*)/>', t):
        attrs = m.group(1)
        mm = re.search(r'y1="([^"]*)"', attrs)
        if mm and abs(float(mm.group(1)) - 1756) < 1:
            print(f"    line: {attrs}")

print("\n== P7 disclosure full block (both languages, y 1600-1760, x col?) ==")
for label, d in (("core", CORE), ("edition", ED)):
    print(f"--- {label} ---")
    for e in elems(d/"p7-yazyk.svg"):
        if 1600 <= e["y"] <= 1760:
            print(f"  x={e['x']} y={e['y']} size={e['size']} {e['s']!r}")
