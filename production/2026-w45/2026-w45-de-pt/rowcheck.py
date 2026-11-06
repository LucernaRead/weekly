# Same-baseline ink scan (README #10 blind spot): two text runs sharing one
# baseline must not overlap in ink. Uses the canonical audit's ink boxes.
import sys, os, re, glob
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
from occlusion_audit import ink_box, parse_attrs, TAG_RE

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-pt")
problems = []
for path in sorted(glob.glob(os.path.join(ED, "svg", "*.svg"))):
    svg = open(path, encoding="utf-8").read()
    nodes = []
    for m in TAG_RE.finditer(svg):
        if m.group("tcontent") is None:
            continue
        a = parse_attrs(m.group("tattrs"))
        t = m.group("tcontent")
        if not t.strip():
            continue
        try:
            x, y = float(a["x"]), float(a["y"])
            size = float(a.get("font-size", "20"))
        except (KeyError, ValueError):
            continue
        bold = a.get("font-weight", "") in ("700", "bold")
        fam = a.get("font-family", "")
        anchor = a.get("text-anchor", "start")
        box = ink_box(t, fam, size, bold, x, y, anchor)
        if box:
            nodes.append((y, box, t))
    by_y = {}
    for y, box, t in nodes:
        by_y.setdefault(round(y, 2), []).append((box, t))
    for y, items in by_y.items():
        items.sort()
        for (b1, t1), (b2, t2) in zip(items, items[1:]):
            if b2[0] < b1[2] - 0.5:  # 0.5px tolerance
                problems.append((os.path.basename(path), y, t1, t2, round(b1[2], 1), round(b2[0], 1)))
print(f"same-baseline collisions: {len(problems)}")
for p in problems:
    print(" ", p)
