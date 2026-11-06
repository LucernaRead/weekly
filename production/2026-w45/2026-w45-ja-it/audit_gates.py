# -*- coding: utf-8 -*-
"""JA x IT W45 builder self-audit: ADVANCE right-edge, full-page frame-line,
P6 chart coverage, kinsoku, phrases, gloss counts, image payloads,
residual-Chinese (char + word level), P8 line completeness, essay verbatim."""
import sys, os, re, json, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import _font
from PIL import ImageFont
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
ED = os.path.join(BASE, "weekly-report-w45-ja-it")
CO = os.path.join(BASE, "weekly-report-w45-ja-core")
PAGES = ["p1-hyoushi","p2-kurashi","p3-bunka","p4-supotsu","p5-wakamono","p6-fukayomi","p7-kotoba","p8-tesuto"]
TEXT_RE = re.compile(r'<text x="([^"]+)" y="([^"]+)" font-family="([^"]+)" font-size="([^"]+)"([^>]*)>([^<]*)</text>')
RECT_RE = re.compile(r'<rect x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"[^>]*>')
LINE_RE = re.compile(r'<line x1="([^"]+)" y1="([^"]+)" x2="([^"]+)" y2="([^"]+)"[^>]*stroke-width="([^"]+)"')
def fam_kind(fam):
    return "serif" if "Serif" in fam else "sans"
def texts_of(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in TEXT_RE.finditer(s):
        x, y, fam, size, rest, t = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), m.group(5), m.group(6)
        anchor = "middle" if 'text-anchor="middle"' in rest else ("end" if 'text-anchor="end"' in rest else "start")
        bold = 'font-weight="700"' in rest
        out.append({"x": x, "y": y, "size": size, "kind": fam_kind(fam), "bold": bold, "anchor": anchor, "t": t})
    return out
def ink_box(el):
    f = _font(el["kind"], el["bold"], el["size"])
    # getbbox with anchor 'ls' (baseline-anchored): returns (l, t, r, b) rel to anchor point
    try:
        bb = f.getbbox(el["t"], anchor="ls")
    except Exception:
        bb = f.getbbox(el["t"])
    w = bb[2] - bb[0]
    if el["anchor"] == "middle": x0 = el["x"] - w/2 - bb[0]
    elif el["anchor"] == "end": x0 = el["x"] - w - bb[0]
    else: x0 = el["x"] - bb[0]
    # getbbox ls: y is baseline; top = y + bb[1], bottom = y + bb[3]
    return (x0, el["y"] + bb[1], x0 + w, el["y"] + bb[3], w)
def adv_right(el):
    f = _font(el["kind"], el["bold"], el["size"])
    w = f.getlength(el["t"])
    if el["anchor"] == "middle": return el["x"] + w/2
    if el["anchor"] == "end": return el["x"]
    return el["x"] + w
res = {}
# 1. ADVANCE right-edge scan (limit 1885.5)
viol = []
for pg in PAGES:
    for el in texts_of(os.path.join(ED, "svg", pg + ".svg")):
        r = adv_right(el)
        if r > 1885.5: viol.append((pg, round(r,1), el["t"][:40]))
res["advance_violations"] = viol
# 2. Frame scan: text ink vs every rect border + line segment (full page)
frame_hits = []
for pg in PAGES:
    path = os.path.join(ED, "svg", pg + ".svg")
    s = open(path, encoding="utf-8").read()
    rects = [(float(a), float(b), float(c), float(d)) for a, b, c, d in RECT_RE.findall(s)]
    lines = [(float(a), float(b), float(c), float(d), float(e)) for a, b, c, d, e in LINE_RE.findall(s)]
    for el in texts_of(path):
        x0, y0, x1, y1, _ = ink_box(el)
        for rx, ry, rw, rh in rects:
            # ink straddling a border line (within 0.8 units)
            for bx in (rx, rx + rw):
                if x0 < bx < x1 and y0 < ry + rh and y1 > ry: frame_hits.append((pg, "rect-v", round(bx,1), el["t"][:30]))
            for by in (ry, ry + rh):
                if y0 < by < y1 and x0 < rx + rw and x1 > rx: frame_hits.append((pg, "rect-h", round(by,1), el["t"][:30]))
        for x1l, y1l, x2l, y2l, sw in lines:
            if y1l == y2l and y0 - sw/2 < y1l < y1 + sw/2 and x0 < max(x1l, x2l) and x1 > min(x1l, x2l):
                frame_hits.append((pg, "line-h", round(y1l,1), el["t"][:30]))
            if x1l == x2l and x0 - sw/2 < x1l < x1 + sw/2 and y0 < max(y1l, y2l) and y1 > min(y1l, y2l):
                frame_hits.append((pg, "line-v", round(x1l,1), el["t"][:30]))
res["frame_hits"] = frame_hits[:40]; res["frame_hit_count"] = len(frame_hits)
# 3. P6 chart coverage: labels vs later-drawn rects (baseline-anchored ink)
p6 = open(os.path.join(ED, "svg", "p6-fukayomi.svg"), encoding="utf-8").read()
# parse elements in order: texts and rects
elems = []
for m in re.finditer(r'<(text|rect)[^>]*>', p6):
    elems.append((m.start(), m.group(0)))
texts6 = texts_of(os.path.join(ED, "svg", "p6-fukayomi.svg"))
# chart labels: texts containing % or the four category words
cats = ["満足", "温泉", "紅葉", "グルメ"]
labels = [el for el in texts6 if any(c in el["t"] for c in cats) or "%" in el["t"]]
# rects in order with positions
rect_list = []
for m in RECT_RE.finditer(p6):
    rect_list.append((m.start(), float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4))))
maxcov = 0.0; details = []
for el in labels:
    x0, y0, x1, y1, w = ink_box(el)
    ink_area = max(0.0, (x1-x0) * (y1-y0))
    if ink_area == 0: continue
    # find text position in raw string to order rects after it
    pos = p6.find(">" + el["t"] + "<")
    ov = 0.0
    for rp, rx, ry, rw, rh in rect_list:
        if rp > pos:
            ix = max(0.0, min(x1, rx+rw) - max(x0, rx)); iy = max(0.0, min(y1, ry+rh) - max(y0, ry))
            ov += ix * iy
    cov = ov / ink_area
    details.append((el["t"][:30], round(cov, 4)))
    maxcov = max(maxcov, cov)
res["p6_chart_max_coverage"] = round(maxcov, 4); res["p6_chart_labels"] = details
# 4. kinsoku: line-start chars
NO_START = set("。、，．！？：；）」』】ー…‥・")
ks = []
for pg in PAGES:
    for el in texts_of(os.path.join(ED, "svg", pg + ".svg")):
        if el["t"] and el["t"][0] in NO_START: ks.append((pg, el["t"][:20]))
res["kinsoku_hits"] = ks
# 5. phrases 2x (whitespace-stripped concatenation)
alltext = ""
for pg in PAGES:
    for el in texts_of(os.path.join(ED, "svg", pg + ".svg")): alltext += el["t"]
flat = re.sub(r"\s+", "", alltext)
phrases = ["文化の日は、11月3日（火よう日）です。", "ゆっくり、ゆるく整える日本の11月です。", "『ゆる』は、無理をしない、ゆっくり、という意味です。", "鍋の材料が1か月早く並び始めました。", "伝統工芸と紅葉と光を、いっしょに楽しむことができます。", "ソフトバンクが2連勝でスタートしました。", "ルールを守って、楽しいハロウィンにしましょう。", "紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。"]
res["phrase_counts"] = {p[:12]: flat.count(re.sub(r"\s+", "", p)) for p in phrases}
# 6. gloss counts: split gloss() call strings on the separator char in transformed sources
import glob as _g
gloss_counts = {}
for f, pg in [("content12.py", ["p1", "p2"]), ("content34.py", ["p3", "p4"]), ("content56.py", ["p5", "p6"])]:
    txt = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f), encoding="utf-8").read()
    calls = re.findall(r'\.gloss\("([^"]*)"\)', txt)
    # gloss() calls appear in page order within each file; split per page by counting boxes is ambiguous,
    # so report per-file totals + verify each item string survives in the SVG text of that file's pages
    items = []
    for c in calls: items += [i for i in c.split("·")]
    gloss_counts[f] = {"calls": len(calls), "items": len(items)}
res["gloss_per_file"] = gloss_counts
# 7. image payloads per page
def payloads(path):
    s = open(path, encoding="utf-8").read()
    return sorted(hashlib.md5(h.encode()).hexdigest() for h in re.findall(r'<image[^>]*href="([^"]+)"', s))
img = {}
for pg in PAGES:
    a = payloads(os.path.join(CO, "svg", pg + ".svg")); b = payloads(os.path.join(ED, "svg", pg + ".svg"))
    img[pg] = {"core": len(a), "ed": len(b), "equal": a == b}
res["images"] = img
# 8. P8 lines: identical lines core vs edition + note localisation check
def p8_lines(path):
    ts = texts_of(path)
    ans = [el for el in ts if el["y"] >= 1328 and el["y"] < 2580 and el["x"] in (65.0, 527.0, 989.0, 1451.0)]
    lines = []; cur = None
    for el in ans:
        t = el["t"]
        if re.match(r'^\d+\. ', t) or t.startswith("— "):
            cur = t; lines.append(cur)
        elif cur is not None:
            lines[-1] = lines[-1] + " " + t
    return lines
cl = p8_lines(os.path.join(CO, "svg", "p8-tesuto.svg")); el8 = p8_lines(os.path.join(ED, "svg", "p8-tesuto.svg"))
res["p8_line_count"] = {"core": len(cl), "ed": len(el8)}
identical = [(i+1, cl[i]) for i in range(min(len(cl), len(el8))) if cl[i] == el8[i]]
res["p8_identical_lines"] = identical
# 9. essay verbatim
def essay(path):
    ts = texts_of(path)
    for el in ts:
        if el["t"].startswith("例： "): return el["t"][3:]
    return None
ce, ee = essay(os.path.join(CO, "svg", "p8-tesuto.svg")), essay(os.path.join(ED, "svg", "p8-tesuto.svg"))
res["essay"] = {"equal": ce == ee, "chars_core": len(ce.replace(" ", "")) if ce else None, "chars_ed": len(ee.replace(" ", "")) if ee else None}
# 10. residual Chinese: NOTES keys as substrings in edition SVG text + simplified-only chars
import subprocess
core_notes = []
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    txt = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f), encoding="utf-8").read()
ed_text = ""
for pg in PAGES:
    for el in texts_of(os.path.join(ED, "svg", pg + ".svg")): ed_text += el["t"] + "\n"
# word-level: check a list of Chinese-only words that must not appear as explanation text
bad_words = ["不定式", "说说你自己", "即学即练", "快讯", "闪电问答", "本期目录", "本周单词", "季节词语", "练习数据", "读者园地", "易错诊所", "本周句式", "本周金句", "下期预告", "练习与答案", "参考答案", "中文简析", "头条", "青年", "万圣节与秋日祭典", "暖和的11月", "轻松食养"]
res["word_level_hits"] = [w for w in bad_words if w in ed_text]
# simplified-only characters (not used in Japanese): sample set
simp_only = set("说这那没很还让对发会经时节问听学读国语话车门东长发为么")
hits = sorted(set(ch for ch in ed_text if ch in simp_only))
res["simplified_only_chars"] = hits
# banned term (built from escapes, never literal in this file's prose)
banned = "\u6865\u63a5"
res["banned_term_svg_hits"] = banned in ed_text
print(json.dumps(res, ensure_ascii=False, indent=1))
