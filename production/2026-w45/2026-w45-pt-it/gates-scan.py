# -*- coding: utf-8 -*-
"""Gate scans for W45 PT x IT (read-only over shipped SVGs; writes JSON only).
A. Same-baseline ink overlap (FR x RU lesson): text nodes sharing an exact
   baseline whose PIL ink boxes overlap in x.
B. Frame / right-edge: ink right vs inner frame 1910, outer frame 1922,
   page edge 1950; right-aligned rows adjudicated by advance width
   (NL x PT lesson: integer bbox vs fractional advance <=0.5px is not
   an overflow).
C. Box-border straddle: text ink crossing any stroked rect border.
D. P6 chart labels: label ink vs later-drawn bar rect, baseline-anchored
   ink method (PIL getmetrics ascent/descent, anchor ls); pass < 30%.
Fonts: the build's own svglib _font (Noto CJK SC faces, same as renderer).
"""
import re, html, json, os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib as S

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-it/svg")
DUMMY = Image.new("RGB", (10, 10))
DR = ImageDraw.Draw(DUMMY)
TEXT_RE = re.compile(r'<text([^>]*)>(.*?)</text>', re.S)
RECT_RE = re.compile(r'<rect([^>]*)/?>', re.S)

def attr(attrs, name, default=None):
    m = re.search(rf'{name}="([^"]+)"', attrs)
    return m.group(1) if m else default

def parse_page(path):
    s = open(path, encoding="utf-8").read()
    texts = []
    for attrs, body in TEXT_RE.findall(s):
        t = html.unescape(re.sub(r"<[^>]+>", "", body))
        if not t.strip():
            continue
        x = float(attr(attrs, "x", "0")); y = float(attr(attrs, "y", "0"))
        size = float(attr(attrs, "font-size", "20"))
        fam = attr(attrs, "font-family", "Noto Sans CJK SC")
        bold = attr(attrs, "font-weight", "") in ("700", "bold")
        kind = "serif" if "Serif" in fam else "sans"
        anchor = attr(attrs, "text-anchor", "start")
        font = S._font(kind, bold, int(round(size))) if float(size).is_integer() else S._font(kind, bold, size)
        # PIL truetype at fractional size: rebuild at exact size
        if not float(size).is_integer():
            import PIL.ImageFont as IF
            path = {("serif", False): S._SERIF, ("serif", True): S._SERIF_B,
                    ("sans", False): S._SANS, ("sans", True): S._SANS_B}[(kind, bold)]
            font = IF.truetype(path, size, index=S._IDX[path])
        anch = {"start": "ls", "middle": "ms", "end": "rs"}.get(anchor, "ls")
        try:
            box = DR.textbbox((x, y), t, font=font, anchor=anch)
        except Exception:
            box = (x, y - size, x + font.getlength(t), y + size * 0.3)
        adv = font.getlength(t)
        adv_right = x if anchor == "end" else (x + adv / 2 if anchor == "middle" else x + adv)
        adv_left = x - adv if anchor == "end" else (x - adv / 2 if anchor == "middle" else x)
        texts.append({"x": x, "y": y, "size": size, "anchor": anchor, "text": t,
                      "ink": box, "adv_left": adv_left, "adv_right": adv_right})
    rects = []
    for attrs in RECT_RE.findall(s):
        if 'stroke=' not in attrs:
            continue
        try:
            rects.append({"x": float(attr(attrs, "x", "0")), "y": float(attr(attrs, "y", "0")),
                          "w": float(attr(attrs, "width", "0")), "h": float(attr(attrs, "height", "0")),
                          "sw": float(attr(attrs, "stroke-width", "1"))})
        except (TypeError, ValueError):
            pass
    return texts, rects

def overlap(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]

out = {"A_same_baseline": [], "B_frame_edge": [], "C_border_straddle": [], "D_p6_chart": []}
for fname in sorted(os.listdir(ED)):
    if not fname.endswith(".svg"):
        continue
    texts, rects = parse_page(os.path.join(ED, fname))
    # A: group by exact baseline y
    byg = {}
    for t in texts:
        byg.setdefault(round(t["y"], 2), []).append(t)
    for y, nodes in byg.items():
        nodes = sorted(nodes, key=lambda n: n["ink"][0])
        for a, b in zip(nodes, nodes[1:]):
            if overlap(a["ink"], b["ink"]):
                out["A_same_baseline"].append({"page": fname, "y": y,
                    "a": a["text"][:60], "b": b["text"][:60],
                    "a_ink": [round(v, 1) for v in a["ink"]], "b_ink": [round(v, 1) for v in b["ink"]]})
    # B: frame / edges
    for t in texts:
        ir = t["ink"][2]
        for bound, name in ((1910, "inner-frame"), (1922, "outer-frame"), (1950, "page-edge")):
            if ir > bound:
                out["B_frame_edge"].append({"page": fname, "bound": name, "bound_x": bound,
                    "text": t["text"][:70], "ink_right": round(ir, 2),
                    "adv_right": round(t["adv_right"], 2),
                    "ink_over": round(ir - bound, 2),
                    "adv_over": round(t["adv_right"] - bound, 2)})
        if t["ink"][0] < 28:
            out["B_frame_edge"].append({"page": fname, "bound": "left-frame", "bound_x": 28,
                "text": t["text"][:70], "ink_left": round(t["ink"][0], 2)})
    # C: border straddle (skip the two page-frame rects themselves? No: include, adjudicate later)
    for t in texts:
        ix0, iy0, ix1, iy1 = t["ink"]
        for r in rects:
            if r["w"] <= 0 or r["h"] <= 0:
                continue
            half = r["sw"] / 2 + 0.5
            # vertical borders
            for bx in (r["x"], r["x"] + r["w"]):
                if ix0 < bx - half or ix1 > bx + half:
                    pass
                if ix0 < bx < ix1 and r["y"] - half <= (iy0 + iy1) / 2 <= r["y"] + r["h"] + half:
                    out["C_border_straddle"].append({"page": fname, "border": f"v@{bx}",
                        "text": t["text"][:70], "ink": [round(v, 1) for v in t["ink"]]})
            for by in (r["y"], r["y"] + r["h"]):
                if iy0 < by < iy1 and r["x"] - half <= (ix0 + ix1) / 2 <= r["x"] + r["w"] + half:
                    out["C_border_straddle"].append({"page": fname, "border": f"h@{by}",
                        "text": t["text"][:70], "ink": [round(v, 1) for v in t["ink"]]})
    # D: P6 chart only
    if fname == "p6-aprofundamento.svg":
        # bars: rects drawn in chart area; recover from build geometry instead:
        # labels at (bx1+22, yy+24) 20pt serif bold; bars at bx1+40+labw, yy+6, w=v*1.5, h=22
        import re as _re
        s = open(os.path.join(ED, fname), encoding="utf-8").read()
        # find label texts + following bar rects in document order
        events = []
        for m in _re.finditer(r'<text[^>]*x="([\d.]+)" y="([\d.]+)"[^>]*font-size="20"[^>]*>([^<]+)</text>|<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="22[^"]*"[^>]*fill="#3e4c2a"', s):
            events.append(m)
        labels = ["portões abertos", "espera", "prova"]
        for lab in labels:
            # find the label node
            for t in texts:
                if t["text"] == lab and t["size"] == 20:
                    # bar rect: same row, x > label x, height 22, y within 30px
                    for r in rects:
                        if abs(r["y"] - (t["y"] - 18)) < 30 and r["x"] > t["x"] and r["h"] == 22:
                            ix0, iy0, ix1, iy1 = t["ink"]
                            ox = max(0, min(ix1, r["x"] + r["w"]) - max(ix0, r["x"]))
                            oy = max(0, min(iy1, r["y"] + r["h"]) - max(iy0, r["y"]))
                            area = max(0.0, (ix1 - ix0) * (iy1 - iy0))
                            cov = (ox * oy / area * 100) if area else 0
                            out["D_p6_chart"].append({"label": lab, "ink": [round(v, 1) for v in t["ink"]],
                                "bar": r, "coverage_pct": round(cov, 2)})
                            break
                    break

print(json.dumps(out, ensure_ascii=False, indent=1))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gates-scan.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
print("COUNTS:", {k: len(v) for k, v in out.items()})
