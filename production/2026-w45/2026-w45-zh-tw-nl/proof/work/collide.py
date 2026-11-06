# -*- coding: utf-8 -*-
"""Own same-baseline ink-collision scan + P4/P6 chart-label element check.
Read-only; uses the audit tool's ink_box."""
import re, os, html, importlib.util
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
spec = importlib.util.spec_from_file_location("oa", os.path.join(BASE, "tools/occlusion_audit.py"))
oa = importlib.util.module_from_spec(spec); spec.loader.exec_module(oa)
TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)"([^>]*)>([^<]*)</text>')
RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"([^>]*)>')
ED = os.path.join(BASE, "files/weekly-report-w45-zh-tw-nl/svg")

def parse(path):
    s = open(path, encoding="utf-8").read()
    els = []
    for m in TEXT_RE.finditer(s):
        t = html.unescape(m.group(4))
        x, y, attrs = float(m.group(1)), float(m.group(2)), m.group(3)
        fm = re.search(r'font-family="([^"]+)"', attrs); sm = re.search(r'font-size="([\d.]+)"', attrs)
        bold = 'font-weight="700"' in attrs or 'font-weight="bold"' in attrs
        anchor = "middle" if 'text-anchor="middle"' in attrs else ("end" if 'text-anchor="end"' in attrs else "start")
        box = oa.ink_box(t, fm.group(1) if fm else "", float(sm.group(1)) if sm else 20.0, bold, x, y, anchor, 0.0)
        els.append({"x": x, "y": y, "t": t, "box": box})
    return s, els

print("== same-baseline collisions (edition, all 8) ==")
nflag = 0
for fn in sorted(os.listdir(ED)):
    _, els = parse(os.path.join(ED, fn))
    byy = {}
    for e in els:
        byy.setdefault(e["y"], []).append(e)
    for y, group in byy.items():
        if len(group) < 2:
            continue
        group = sorted(group, key=lambda e: e["box"][0])
        for a, b in zip(group, group[1:]):
            gap = b["box"][0] - a["box"][2]
            if gap < 0:
                print(f"  COLLISION {fn} y={y}: {a['t'][:40]!r} vs {b['t'][:40]!r} gap={gap:.2f}")
                nflag += 1
print("  total:", nflag)

print("== chart-label element check (P4/P6) ==")
nflag2 = 0
for fn in ["p4-sport.svg", "p6-deep.svg"]:
    s, els = parse(os.path.join(ED, fn))
    items = []
    for m in TEXT_RE.finditer(s):
        items.append(("text", m.start()))
    for m in RECT_RE.finditer(s):
        items.append(("rect", m.start(), (float(m.group(1)), float(m.group(2)),
                                          float(m.group(1)) + float(m.group(3)),
                                          float(m.group(2)) + float(m.group(4)))))
    items.sort(key=lambda z: z[1])
    titer = iter(els)
    seq = []
    for it in items:
        if it[0] == "text":
            seq.append(("text", next(titer)))
        else:
            seq.append(("rect", it[2]))
    for i, (kind, obj) in enumerate(seq):
        if kind != "text":
            continue
        l, t, r, b = obj["box"]
        for kind2, rbox in seq[i + 1:]:
            if kind2 != "rect":
                continue
            rl, rt, rr, rb = rbox
            if l < rr and r > rl and t < rb and b > rt:
                if (rr - rl) == 60.0 and (rb - rt) == 30.0:
                    continue
                if (rr - rl) > 1800:
                    continue
                print(f"  OVERLAP {fn}: {obj['t'][:50]!r} ink {[round(v,1) for v in obj['box']]} vs rect {[round(v,1) for v in rbox]}")
                nflag2 += 1
print("  total:", nflag2)

print("== P7 heads / col ends (edition) ==")
_, els = parse(os.path.join(ED, "p7-lang.svg"))
for e in els:
    if e["t"].startswith(("A2 ·", "B1 ·", "B2 ·")) and e["y"] < 400:
        print(f"  head ink right={e['box'][2]:.1f} text={e['t'][:60]!r}")
