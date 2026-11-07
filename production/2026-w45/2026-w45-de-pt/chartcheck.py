# P6 chart graze check (README #12 blind spot): every chart text's ink vs
# every rect drawn AFTER it must overlap 0. Chart region: the P6 practice
# chart (bars at y ~1420-1600 in p6-vertiefung.svg). Reports max overlap.
import sys, os, re
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
from occlusion_audit import ink_box, parse_attrs, TAG_RE

path = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-pt/svg/p6-vertiefung.svg")
svg = open(path, encoding="utf-8").read()
events = []  # (order, kind, box_or_rect, label)
order = 0
for m in TAG_RE.finditer(svg):
    if m.group("tcontent") is not None:
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
        box = ink_box(t, a.get("font-family", ""), size, bold, x, y, a.get("text-anchor", "start"))
        if box:
            events.append((order, "text", box, t))
    else:
        tag = m.group("tag")
        if tag == "rect":
            a = parse_attrs(m.group("attrs"))
            try:
                r = (float(a["x"]), float(a["y"]), float(a["x"]) + float(a["width"]), float(a["y"]) + float(a["height"]))
            except (KeyError, ValueError):
                continue
            events.append((order, "rect", r, f'rect@{r[0]},{r[1]}'))
    order += 1
worst = []
for i, (o1, k1, b1, t1) in enumerate(events):
    if k1 != "text":
        continue
    # chart texts only: y in the chart band (bars + labels + caption)
    if not (1300 <= b1[1] <= 1700):
        continue
    for (o2, k2, b2, t2) in events[i + 1:]:
        if k2 != "rect":
            continue
        ox = max(0.0, min(b1[2], b2[2]) - max(b1[0], b2[0]))
        oy = max(0.0, min(b1[3], b2[3]) - max(b1[1], b2[1]))
        if ox > 0 and oy > 0:
            worst.append((ox * oy, t1, t2, round(ox, 1), round(oy, 1)))
worst.sort(reverse=True)
print(f"chart-band text-vs-later-rect overlaps: {len(worst)}")
for w in worst[:20]:
    print(" ", w)
