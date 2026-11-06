# -*- coding: utf-8 -*-
"""Badge / P7 / P6 / same-baseline measurements, reusing the canonical
occlusion_audit ink_box (PIL/FreeType true ink)."""
import os, sys, re
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
from xml.etree import ElementTree as ET

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
NS = "{http://www.w3.org/2000/svg}"
ED1 = BASE + "/files/weekly-report-w45-ru-es/svg/p1-pervaya.svg"
W431 = BASE + "/files/weekly-report-ru-es/svg/p1-pervaya.svg"
CORE1 = BASE + "/files/weekly-report-w45-ru-core/svg/p1-pervaya.svg"

def texts(path):
    root = ET.parse(path).getroot()
    out = []
    for el in root.iter():
        if el.tag.replace(NS, "") == "text":
            out.append({"t": "".join(el.itertext()), "x": float(el.get("x") or 0),
                        "y": float(el.get("y") or 0), "fs": float(el.get("font-size") or 20),
                        "fill": el.get("fill"), "fw": el.get("font-weight"),
                        "anchor": el.get("text-anchor") or "start",
                        "fam": el.get("font-family") or ""})
    return out

def find(ts, needle):
    return [d for d in ts if needle in d["t"]]

print("== 6 badge ink (canonical ink_box) ==")
for label, path, needle in [("ED-W45", ED1, "TEXTOS EN RUSO"), ("W43", W431, "TEXTOS EN RUSO")]:
    d = find(texts(path), needle)[0]
    box = OA.ink_box(d["t"], d["fam"], d["fs"], d["fw"] in ("700", "bold"), d["x"], d["y"], d["anchor"])
    print(f"{label}: text x={d['x']} baseline y={d['y']} fs={d['fs']} fill={d['fill']} fw={d['fw']} anchor={d['anchor']}")
    print(f"   ink box l={box[0]:.2f} t={box[1]:.2f} r={box[2]:.2f} b={box[3]:.2f} width={box[2]-box[0]:.2f}")
print("-- ED P1 vertical neighbours --")
ed = texts(ED1)
badge = find(ed, "TEXTOS EN RUSO")[0]
bbox = OA.ink_box(badge["t"], badge["fam"], badge["fs"], True, badge["x"], badge["y"], badge["anchor"])
print(f"dark band rect bottom 542.0 -> badge ink top {bbox[1]:.2f} = gap {bbox[1]-542.0:.2f}")
head = find(ed, "ГЛАВНАЯ ТЕМА")[0]
hbox = OA.ink_box(head["t"], head["fam"], head["fs"], head["fw"] in ("700", "bold"), head["x"], head["y"], head["anchor"])
print(f"headline {head['t']!r} baseline {head['y']} ink top {hbox[1]:.2f} bottom {hbox[3]:.2f}; badge ink bottom {bbox[3]:.2f} -> headline ink top gap {hbox[1]-bbox[3]:.2f}")
print(f"side box rect x=1451 y=580 top 580 -> badge ink bottom {bbox[3]:.2f} = gap {580-bbox[3]:.2f} (x-overlap region 1451-1547.5, vertical clearance only)")
print("-- ED P1 y=372 strapline retained? --")
for d in ed:
    if d["y"] == 372:
        print("   ", repr(d["t"]), "fs=", d["fs"], "fill=", d["fill"])
print("-- CORE P1 y=372 --")
for d in texts(CORE1):
    if d["y"] == 372:
        print("   ", repr(d["t"]), "fs=", d["fs"], "fill=", d["fill"])
print("-- W43 P1 y=372 (badge slot, no strapline) --")
for d in texts(W431):
    if d["y"] == 372:
        print("   ", repr(d["t"]), "fs=", d["fs"], "fill=", d["fill"])

print("\n== 7 P7 readers-corner geometry ED vs CORE ==")
for label, path in [("CORE", BASE + "/files/weekly-report-w45-ru-core/svg/p7-yazyk.svg"),
                    ("ED", BASE + "/files/weekly-report-w45-ru-es/svg/p7-yazyk.svg")]:
    root = ET.parse(path).getroot()
    print(f"-- {label} rects/lines with bottom in 1700-1760 --")
    for el in root.iter():
        tag = el.tag.replace(NS, "")
        if tag == "rect":
            x, y, w, h = (float(el.get(k) or 0) for k in ("x", "y", "width", "height"))
            if 1700 <= y + h <= 1760 or 1700 <= y <= 1760:
                print(f"   rect x={x} y={y} w={w} h={h} bottom={y+h} fill={el.get('fill')} stroke={el.get('stroke')}")
        if tag == "line":
            x1, y1, x2, y2 = (float(el.get(k) or 0) for k in ("x1", "y1", "x2", "y2"))
            if 1700 <= y1 <= 1760 or 1700 <= y2 <= 1760:
                print(f"   line ({x1},{y1})-({x2},{y2}) stroke={el.get('stroke')}")
    print(f"-- {label} texts y 1300-1760 in letters-box columns (x<1451, y>1300) --")
    for d in texts(path):
        if d["y"] and 1300 <= d["y"] <= 1760:
            print(f"   y={d['y']} x={d['x']} fs={d['fs']} {d['t'][:130]!r}")

print("\n== 4 P6 chart element check ED vs CORE ==")
for label, path in [("CORE", BASE + "/files/weekly-report-w45-ru-core/svg/p6-razbor.svg"),
                    ("ED", BASE + "/files/weekly-report-w45-ru-es/svg/p6-razbor.svg")]:
    root = ET.parse(path).getroot()
    print(f"-- {label} --")
    for el in root.iter():
        tag = el.tag.replace(NS, "")
        if tag == "rect":
            w = float(el.get("width") or 0)
            if w in (600.0, 494.0, 388.0, 282.0):
                print(f"   bar rect x={el.get('x')} y={el.get('y')} w={w} h={el.get('height')} fill={el.get('fill')}")
    for d in texts(path):
        if d["t"].strip() in ("34", "28", "22", "16") or re.search(r"(?<!\d)(34|28|22|16)(?!\d)", d["t"]):
            print(f"   text y={d['y']} x={d['x']} fs={d['fs']} {d['t'][:100]!r}")

print("\n== 4 same-baseline ink scan (ED + CORE, all pages) ==")
PAGES = ["p1-pervaya", "p2-zhizn", "p3-kultura", "p4-sport",
         "p5-molodezh", "p6-razbor", "p7-yazyk", "p8-test"]
for label, svgdir in [("CORE", BASE + "/files/weekly-report-w45-ru-core/svg"),
                      ("ED", BASE + "/files/weekly-report-w45-ru-es/svg")]:
    total_flags = 0
    for p in PAGES:
        ts = texts(f"{svgdir}/{p}.svg")
        by_y = {}
        for d in ts:
            by_y.setdefault(d["y"], []).append(d)
        for y, group in by_y.items():
            if len(group) < 2:
                continue
            boxes = []
            for d in group:
                b = OA.ink_box(d["t"], d["fam"], d["fs"], d["fw"] in ("700", "bold"), d["x"], d["y"], d["anchor"])
                if b:
                    boxes.append((d, b))
            for i in range(len(boxes)):
                for j in range(i + 1, len(boxes)):
                    (d1, b1), (d2, b2) = boxes[i], boxes[j]
                    if b1[0] < b2[2] and b2[0] < b1[2] and b1[1] < b2[3] and b2[1] < b1[3]:
                        print(f"   FLAG {label} {p} y={y}: {d1['t'][:40]!r} vs {d2['t'][:40]!r} boxes {b1} {b2}")
                        total_flags += 1
    print(f"{label} same-baseline ink flags total: {total_flags}")
