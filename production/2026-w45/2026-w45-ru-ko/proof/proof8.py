#!/usr/bin/env python3
"""Independent RUxKO W45 proof script 8: same-baseline ink scan (venv PIL, build svglib fonts)
+ badge ink span. Run with tools/venv/bin/python."""
import re, sys
from pathlib import Path
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-ko-build")
import svglib

BASE = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/files")
ED = BASE/"weekly-report-w45-ru-ko/svg"
CORE = BASE/"weekly-report-w45-ru-core/svg"
PAGES = ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]

def elems(path):
    t = Path(path).read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', t):
        attrs = m.group(1); s = m.group(2)
        def g(k):
            mm = re.search(rf'{k}="([^"]*)"', attrs); return mm.group(1) if mm else ""
        out.append({"x": float(g("x") or 0), "y": float(g("y") or 0),
                    "size": float(g("font-size") or 0), "weight": g("font-weight"),
                    "anchor": g("text-anchor") or "start", "fam": g("font-family"), "s": s})
    return out

def ink(e):
    kind = "sans" if "Sans" in e["fam"] else "serif"
    bold = (e["weight"] == "700")
    size = int(round(e["size"]))
    f = svglib._font(kind, bold, size)
    bb = f.getbbox(e["s"])  # (left, top, right, bottom)
    adv = f.getlength(e["s"])
    if e["anchor"] == "middle":
        x0 = e["x"] - adv/2 + bb[0]; x1 = e["x"] - adv/2 + bb[2]
    elif e["anchor"] == "end":
        x0 = e["x"] - adv + bb[0]; x1 = e["x"] - adv + bb[2]
    else:
        x0 = e["x"] + bb[0]; x1 = e["x"] + bb[2]
    return x0, x1

for label, d in (("edition", ED), ("core", CORE)):
    total_flags = 0
    for p in PAGES:
        els = elems(d/f"{p}.svg")
        by_y = {}
        for e in els:
            by_y.setdefault(e["y"], []).append(e)
        flags = []
        for y, group in by_y.items():
            if len(group) < 2: continue
            boxes = sorted([(ink(e)[0], ink(e)[1], e) for e in group], key=lambda b: b[0])
            for (x0a, x1a, ea), (x0b, x1b, eb) in zip(boxes, boxes[1:]):
                gap = x0b - x1a
                if gap < 5:
                    flags.append(f"y={y} gap={gap:.2f} {ea['s']!r} | {eb['s']!r}")
        total_flags += len(flags)
        print(f"  {label} {p}: same-baseline flags={len(flags)}")
        for fl in flags: print(f"    {fl}")
    print(f"  {label} TOTAL flags={total_flags}")

print("\n== Badge ink span (sans bold 22, centred x=975) ==")
badge = "러시아어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판"
f = svglib._font("sans", True, 22)
bb = f.getbbox(badge); adv = f.getlength(badge)
print(f"  advance={adv:.2f} ink_bbox={bb} ink_width={bb[2]-bb[0]:.2f}")
print(f"  span centred: {975 - adv/2 + bb[0]:.2f} – {975 - adv/2 + bb[2]:.2f}")
print(f"  KIT claim: 716.16–1233.84 (w 517.67)")
# P1 badge row neighbours: dark-band bottom 542, headline-head baseline 606
for e in elems(ED/"p1-pervaya.svg"):
    if e["y"] in (574.0, 606.0) or "КАЖДУЮ НЕДЕЛЮ" in e["s"]:
        print(f"  P1 y={e['y']} x={e['x']} {e['s']!r} ink={ink(e)}")
