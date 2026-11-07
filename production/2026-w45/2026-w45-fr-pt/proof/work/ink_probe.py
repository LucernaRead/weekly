# -*- coding: utf-8 -*-
"""Proofreader ink probe: reuses canonical tools/occlusion_audit.py ink_box
(read-only import) to compute true-ink bottoms/right edges for named nodes.
Also: advance-width right-edge scan, frame-line scan, same-baseline spacing
on P1 top band, P6 chart-label baseline-anchored coverage, line-start ':' ,
overflow scan (any ink below 2580 excl footer baseline 2624 nodes, any ink
outside inner frame 40..1910 x / 40..2660 y excl outer/inner frame rects).
"""
import sys, os, re, json
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
from occlusion_audit import ink_box, get_font
import xml.etree.ElementTree as ET
from PIL import ImageFont

HOME = os.path.expanduser("~")
BASE = os.path.join(HOME, "workspace/goals/lucernaread-social-media-operations/files")
ED = os.path.join(BASE, "weekly-report-w45-fr-pt", "svg")
CORE = os.path.join(BASE, "weekly-report-w45-fr-core", "svg")
WORK = os.path.join(HOME, "workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-pt-proof/work")

def parse(path):
    tree = ET.parse(path)
    texts, rects = [], []
    for el in tree.getroot().iter():
        if el.tag.endswith("text") and (el.text or "").strip():
            texts.append({"x": float(el.get("x", 0)), "y": float(el.get("y", 0)),
                          "fs": float(el.get("font-size", 0)), "fam": el.get("font-family", ""),
                          "bold": (el.get("font-weight") in ("700", "bold")),
                          "anchor": el.get("text-anchor", "start"), "text": el.text})
        elif el.tag.endswith("rect"):
            rects.append({"x": float(el.get("x", 0)), "y": float(el.get("y", 0)),
                          "w": float(el.get("width", 0)), "h": float(el.get("height", 0)),
                          "sw": float(el.get("stroke-width", 0))})
    return texts, rects

def ink(n):
    return ink_box(n["text"], n["fam"], n["fs"], n["bold"], n["x"], n["y"], n["anchor"])

def adv_right(n):
    f = get_font(n["fam"], n["fs"], n["bold"])
    adv = f.getlength(n["text"]) / 4.0
    if n["anchor"] == "middle":
        return n["x"] + adv / 2, adv
    if n["anchor"] == "end":
        return n["x"], adv
    return n["x"] + adv, adv

out = {}
for label, d in [("ed", ED), ("core", CORE)]:
    out[label] = {}
    for name in sorted(os.listdir(d)):
        texts, rects = parse(os.path.join(d, name))
        # named ink bottoms
        named = {}
        for n in texts:
            b = ink(n)
            if b is None:
                continue
            named.setdefault("max_ink_bottom_excl_footer", 0)
            if n["y"] < 2580 and b[3] > named["max_ink_bottom_excl_footer"]:
                named["max_ink_bottom_excl_footer"] = b[3]
                named["max_ink_bottom_node"] = (n["x"], n["y"], n["fs"], n["text"][:100])
        # advance right-edge > 1885
        adv_over = []
        ink_over_inner = []
        for n in texts:
            r, _ = adv_right(n)
            if r > 1885:
                adv_over.append((n["x"], n["y"], round(r, 1), n["text"][:90]))
            b = ink(n)
            if b and b[2] > 1910 and n["y"] != 2624:
                ink_over_inner.append((n["x"], n["y"], round(b[2], 1), n["text"][:90]))
        out[label][name] = {"named": named, "adv_over_1885": adv_over,
                            "ink_over_inner1910": ink_over_inner}
    # P8 specifics
    texts, _ = parse(os.path.join(d, "p8-exercices.svg"))
    def inkbot(x, y, substr):
        for n in texts:
            if n["x"] == x and abs(n["y"] - y) < 0.01 and substr in n["text"]:
                b = ink(n)
                return {"node": (n["x"], n["y"], n["fs"], n["text"][:120]), "ink": b, "ink_bottom": b[3] if b else None}
        return None
    out[label]["p8_detail"] = {
        "sep_pagina4": inkbot(65, 2544.03, "Página 4"),
        "sep_core4": inkbot(65, 2498.93, "第 4"),
        "answer_col527": inkbot(527, 2532.82, "calendário") or inkbot(527, 2532.82, "excitante"),
        "answer_col989": inkbot(989, 2532.82, "reprendre"),
        "battery_merci": inkbot(1451, 1446.4, "Merci"),
        "battery_core_last": inkbot(65, 1455.825, "C. des"),
        "tail1451": inkbot(1451, 2270.35, "pontos") or inkbot(1451, 2137.45, "点给分"),
    }
    # P7 specifics: preview last line + reader box last line: find max-y nodes excl footer, and nodes with preview text
    texts7, _ = parse(os.path.join(d, "p7-langue.svg"))
    tail7 = sorted([n for n in texts7 if n["y"] < 2580], key=lambda n: n["y"])[-6:]
    out[label]["p7_tail"] = [{"x": n["x"], "y": n["y"], "fs": n["fs"], "text": n["text"][:120],
                              "ink_bottom": (ink(n)[3] if ink(n) else None)} for n in tail7]
    # P7 reader box: nodes between reader head and preview head - approximate by y range of reader section:
    # report all nodes y in 2000..2300 for inspection
    out[label]["p7_reader_zone"] = [{"x": n["x"], "y": n["y"], "text": n["text"][:100],
                                     "ink_bottom": (ink(n)[3] if ink(n) else None)}
                                    for n in texts7 if 2050 <= n["y"] <= 2300]
    # P5 / P6 / P1 / P2 tails
    for pg in ["p5-jeunesse.svg", "p6-politique.svg", "p1-une.svg", "p2-vie.svg"]:
        t, _ = parse(os.path.join(d, pg))
        tail = sorted([n for n in t if n["y"] < 2580], key=lambda n: n["y"])[-5:]
        out[label][pg + "_tail"] = [{"x": n["x"], "y": n["y"], "fs": n["fs"], "text": n["text"][:110],
                                     "ink_bottom": (ink(n)[3] if ink(n) else None)} for n in tail]

# P6 chart-label coverage, baseline-anchored: for each P6 text node, if a LATER-drawn
# rect overlaps its baseline-anchored box (x..x+adv, baseline-descent..baseline+cap? use
# getmetrics ascent/descent: box = (x, y-ascent, x+adv, y+descent)), coverage = overlap area / box area
def chart_coverage(d):
    path = os.path.join(d, "p6-politique.svg")
    tree = ET.parse(path)
    els = []
    for el in tree.getroot().iter():
        if el.tag.endswith("text") and (el.text or "").strip():
            els.append(("text", el))
        elif el.tag.endswith("rect"):
            els.append(("rect", el))
    worst = []
    for i, (k, el) in enumerate(els):
        if k != "text":
            continue
        x, y = float(el.get("x", 0)), float(el.get("y", 0))
        fs, fam = float(el.get("font-size", 0)), el.get("font-family", "")
        bold = el.get("font-weight") in ("700", "bold")
        f = get_font(fam, fs, bold)
        adv = f.getlength(el.text) / 4.0
        asc, desc = f.getmetrics()[0] / 4.0, f.getmetrics()[1] / 4.0
        box = (x, y - asc, x + adv, y + desc)
        area = (box[2] - box[0]) * (box[3] - box[1])
        for k2, el2 in els[i + 1:]:
            if k2 != "rect":
                continue
            rx, ry = float(el2.get("x", 0)), float(el2.get("y", 0))
            rw, rh = float(el2.get("width", 0)), float(el2.get("height", 0))
            sw = float(el2.get("stroke-width", 0))
            rx -= sw / 2; ry -= sw / 2; rw += sw; rh += sw
            ox = max(0, min(box[2], rx + rw) - max(box[0], rx))
            oy = max(0, min(box[3], ry + rh) - max(box[1], ry))
            if ox > 0 and oy > 0 and area > 0:
                worst.append((round(ox * oy / area * 100, 2), x, y, el.text[:80], (rx, ry, rw, rh)))
    worst.sort(reverse=True)
    return worst[:10]

out["chart_coverage"] = {"ed": chart_coverage(ED), "core": chart_coverage(CORE)}
json.dump(out, open(os.path.join(WORK, "ink_probe.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1)[:6000])
print("CHART ed:", out["chart_coverage"]["ed"])
print("CHART core:", out["chart_coverage"]["core"])
for label in ("ed", "core"):
    print(label, "p8_detail:", out[label]["p8_detail"])
    print(label, "p7_tail:", out[label]["p7_tail"])
    for pg in ["p5-jeunesse.svg", "p6-politique.svg", "p1-une.svg", "p2-vie.svg"]:
        print(label, pg, out[label][pg + "_tail"])
    for name in sorted(out[label]):
        if name.endswith(".svg"):
            print(label, name, "adv_over:", out[label][name]["adv_over_1885"], "ink_over1910:", out[label][name]["ink_over_inner1910"])
