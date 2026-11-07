#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round 3 independent fix verification: gloss lines, counts, D3/D4 stems,
same-class sweeps from RENDERED SVG text, D-7 context, P3 gloss-box geometry.
Reads SVGs only. Expected gloss strings are the Round 2 verdict §2.4
restoration strings (typed here from the verdict, cross-checked vs FIX-REPORT §1)."""
import os, re, json
from xml.etree import ElementTree as ET
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
R3 = os.path.join(GOAL, "hidden_files", "w46", "ko-proofread-gates-round3")
NS = "{http://www.w3.org/2000/svg}"
EDITIONS = {"zh-cn": "weekly-report-w46-ko-core", "de": "weekly-report-w46-ko-de",
            "en": "weekly-report-w46-ko-en", "es": "weekly-report-w46-ko-es",
            "fr": "weekly-report-w46-ko-fr", "it": "weekly-report-w46-ko-it",
            "ja": "weekly-report-w46-ko-ja", "nl": "weekly-report-w46-ko-nl",
            "pt": "weekly-report-w46-ko-pt", "ru": "weekly-report-w46-ko-ru",
            "zh-tw": "weekly-report-w46-ko-zh-tw"}
EXPECTED = {
 "zh-cn": "译注｜겹치다 重叠 · 가늘다 细 · 감사하다 感谢 · 나누다 区分、分享。",
 "de": "HINWEIS · 겹치다 = sich überschneiden · 가늘다 = dünn · 감사하다 = danken · 나누다 = unterscheiden, teilen",
 "en": "Note — 겹치다 = to overlap · 가늘다 = thin · 감사하다 = to thank · 나누다 = to tell apart, to share",
 "es": "Nota — 겹치다 = coincidir, solaparse · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, compartir",
 "fr": "Note — 겹치다 = se chevaucher · 가늘다 = fin · 감사하다 = remercier · 나누다 = distinguer, partager",
 "it": "Nota — 겹치다 = sovrapporsi · 가늘다 = sottile · 감사하다 = ringraziare · 나누다 = distinguere, condividere",
 "ja": "解説 — 겹치다 = 重なる · 가늘다 = 細い · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う",
 "nl": "Uitleg — 겹치다 = samenvallen · 가늘다 = dun · 감사하다 = bedanken · 나누다 = onderscheiden, delen",
 "pt": "Nota — 겹치다 = sobrepor-se · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, partilhar",
 "ru": "Пояснение — 겹치다 = совпадать · 가늘다 = тонкий · 감사하다 = благодарить · 나누다 = различать, делиться",
 "zh-tw": "譯注｜겹치다 重疊 · 가늘다 細 · 감사하다 感謝 · 나누다 區分、分享。",
}
PAGES = ["p1-pyoji.svg","p2-saenghwal.svg","p3-munhwa.svg","p4-seupocheu.svg",
         "p5-cheongnyeon.svg","p6-gipi.svg","p7-mal.svg","p8-siheom.svg"]

def els_of(path):
    root = ET.parse(path).getroot()
    return [(float(t.get("x")), float(t.get("y")), "".join(t.itertext()), t)
            for t in root.iter(NS + "text")]

def rects_of(path):
    root = ET.parse(path).getroot()
    out = []
    for r in root.iter(NS + "rect"):
        try:
            out.append((float(r.get("x")), float(r.get("y")), float(r.get("width")),
                        float(r.get("height")), r.get("fill"), r.get("stroke")))
        except (TypeError, ValueError):
            pass
    return out

out = {}
for code, d in EDITIONS.items():
    edir = os.path.join(GOAL, "files", d)
    joined = "\n".join(t for pg in PAGES for _, _, t, _ in els_of(os.path.join(edir, "svg", pg)))
    # gloss: anchor on 겹치다 in P3, same-x nodes within +90px
    p3 = els_of(os.path.join(edir, "svg", "p3-munhwa.svg"))
    anchor = [e for e in p3 if "겹치다" in e[2]][0]
    ax, ay = anchor[0], anchor[1]
    lines = sorted([e for e in p3 if abs(e[0]-ax) < 6 and ay-1 <= e[1] <= ay+90], key=lambda e: e[1])
    gloss = " ".join(e[2] for e in lines)
    # gloss box geometry: rects containing the gloss lines' x-range, y-range
    rects = rects_of(os.path.join(edir, "svg", "p3-munhwa.svg"))
    boxes = [r for r in rects if r[0] <= ax+1 and r[0]+r[2] >= ax+400 and r[1] <= ay and r[1]+r[3] >= lines[-1][1]+10]
    box = min(boxes, key=lambda r: r[2]*r[3]) if boxes else None
    geom = None
    if box:
        geom = {"box": box, "first_line_y": lines[0][1], "last_line_y": lines[-1][1],
                "top_margin": lines[0][1]-box[1], "bottom_margin": box[1]+box[3]-lines[-1][1],
                "n_lines": len(lines)}
    # D-7 contexts: every text node containing D-7, plus full joined neighbours
    d7 = [(pg, x, y, t) for pg in PAGES for x, y, t, _ in els_of(os.path.join(edir, "svg", pg)) if "D-7" in t]
    # quotative contexts
    quot = [(pg, x, y, t) for pg in PAGES for x, y, t, _ in els_of(os.path.join(edir, "svg", pg)) if "이라고" in t or "라고" in t]
    out[code] = {
        "ganeul": joined.count("가늘"), "ganeun": joined.count("가늰"),
        "gloss_lines": [e[2] for e in lines], "gloss_joined": gloss,
        "gloss_match": gloss == EXPECTED[code], "gloss_geom": geom,
        "gui_simp": joined.count("规"), "gui_trad": joined.count("規"),
        "d7_nodes": d7, "quot_nodes": quot,
        "ganeun_contexts": [(pg, t) for pg in PAGES for _, _, t, _ in els_of(os.path.join(edir, "svg", pg)) if "가늰" in t],
    }
    print(code, "gloss", "MATCH" if gloss == EXPECTED[code] else "MISMATCH",
          "| 가늘=", out[code]["ganeul"], "가늰=", out[code]["ganeun"],
          "| box=", geom)
    print("   gloss:", gloss)
    for pg, x, y, t in d7:
        print("   D7", pg, y, repr(t))

json.dump(out, open(os.path.join(R3, "fix-verification.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("D7 nodes per edition:", {c: len(o["d7_nodes"]) for c, o in out.items()})
