# -*- coding: utf-8 -*-
"""Independent geometry re-measurement for W45 PT x ZH-TW (own code, TC faces)."""
import re, os
from PIL import ImageFont
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-pt-zh-tw/svg")
CO = os.path.join(BASE, "files/weekly-report-w45-pt-core/svg")
PAGES = ["p1-capa", "p2-vida", "p3-cultura", "p4-esporte", "p5-jovens",
         "p6-aprofundamento", "p7-lingua", "p8-avaliacao"]
TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]+)"')

def F(fam, bold, size):
    serif = "Serif" in fam
    path = ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc" if serif and bold else
            "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc" if serif else
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")
    if "Unifraktur" in fam:
        return ImageFont.truetype("/home/hatch/.local/share/fonts/UnifrakturMaguntia.ttf", int(round(size)))
    return ImageFont.truetype(path, int(round(size)), index=3)

def texts_of(path):
    s = open(path, encoding='utf-8').read()
    out = []
    for m in TEXT_RE.finditer(s):
        bold = 'font-weight="700"' in m.group(5)
        anchor = "middle" if 'text-anchor="middle"' in m.group(5) else ("end" if 'text-anchor="end"' in m.group(5) else "start")
        out.append({"x": float(m.group(1)), "y": float(m.group(2)), "fam": m.group(3),
                    "size": float(m.group(4)), "bold": bold, "anchor": anchor, "t": m.group(6)})
    return out, s

def inkbox(t):
    f = F(t["fam"], t["bold"], t["size"])
    try:
        l, tp, r, b = f.getbbox(t["t"], anchor="ls")
        adv = f.getlength(t["t"])
    except Exception:
        return (t["x"], t["y"] - t["size"], t["x"] + len(t["t"]) * t["size"], t["y"])
    ox = t["x"] - adv / 2 if t["anchor"] == "middle" else (t["x"] - adv if t["anchor"] == "end" else t["x"])
    return (ox + l, t["y"] + tp, ox + r, t["y"] + b)

def adv_end(t):
    f = F(t["fam"], t["bold"], t["size"])
    adv = f.getlength(t["t"])
    return t["x"] + adv / 2 if t["anchor"] == "middle" else (t["x"] if t["anchor"] == "end" else t["x"] + adv)

def adv_start(t):
    f = F(t["fam"], t["bold"], t["size"])
    adv = f.getlength(t["t"])
    return t["x"] - adv / 2 if t["anchor"] == "middle" else (t["x"] - adv if t["anchor"] == "end" else t["x"])

print("=== ADVANCE right-edge scan (edge=1885, frame=1910), core vs edition ===")
for label, D in [("core", CO), ("edition", ED)]:
    print(f"  --- {label} ---")
    for pg in PAGES:
        ts, _ = texts_of(os.path.join(D, pg + ".svg"))
        for t in ts:
            ae, ast_ = adv_end(t), adv_start(t)
            if (ae > 1885.5 or ast_ < 64.5) and not (pg == "p1-capa" and t["size"] == 168):
                print(f"    {pg} y={t['y']} adv=[{ast_:.1f},{ae:.1f}] {t['t'][:55]!r}")
print("=== max right INK per page (edition) + any ink beyond frame 1910 ===")
for pg in PAGES:
    ts, _ = texts_of(os.path.join(ED, pg + ".svg"))
    mx = max(inkbox(t)[2] for t in ts)
    over = [(t["t"][:40], round(inkbox(t)[2], 1)) for t in ts if inkbox(t)[2] > 1910]
    print(f"  {pg}: max right ink={mx:.1f} over-frame={over}")

print("=== same-baseline ink collision scan (edition) ===")
flags = 0
for pg in PAGES:
    ts, _ = texts_of(os.path.join(ED, pg + ".svg"))
    by_y = {}
    for t in ts:
        by_y.setdefault(round(t["y"], 1), []).append(t)
    for y, group in by_y.items():
        if len(group) < 2:
            continue
        boxes = sorted((inkbox(t), t["t"]) for t in group)
        for (b1, t1), (b2, t2) in zip(boxes, boxes[1:]):
            if b2[0] < b1[2] - 0.5:
                print(f"  COLLIDE {pg} y={y}: {t1[:40]!r} vs {t2[:40]!r}"); flags += 1
print(f"  same-baseline flags: {flags}")

print("=== P6 chart-label coverage, baseline-anchored ink vs later rects (edition + core) ===")
for label, D in [("core", CO), ("edition", ED)]:
    s = open(os.path.join(D, "p6-aprofundamento.svg"), encoding='utf-8').read()
    elems = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>|<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]+)"', s):
        if m.group(6) is not None:
            bold = 'font-weight="700"' in m.group(5)
            anchor = "middle" if 'text-anchor="middle"' in m.group(5) else ("end" if 'text-anchor="end"' in m.group(5) else "start")
            elems.append(("text", {"x": float(m.group(1)), "y": float(m.group(2)), "fam": m.group(3),
                                   "size": float(m.group(4)), "bold": bold, "anchor": anchor, "t": m.group(6)}))
        else:
            elems.append(("rect", (float(m.group(7)), float(m.group(8)), float(m.group(7)) + float(m.group(9)),
                                   float(m.group(8)) + float(m.group(10)), m.group(11))))
    worst = []
    for i, (k, t) in enumerate(elems):
        if k != "text":
            continue
        b = inkbox(t)
        for k2, r in elems[i + 1:]:
            if k2 != "rect" or r[4] in ("none",):
                continue
            ix = max(0, min(b[2], r[2]) - max(b[0], r[0])); iy = max(0, min(b[3], r[3]) - max(b[1], r[1]))
            area = (b[2] - b[0]) * (b[3] - b[1])
            if area > 0 and ix * iy / area >= 0.05:
                worst.append((ix * iy / area, t["t"][:45], r[:4]))
    worst.sort(reverse=True)
    print(f"  {label}: max coverage: {worst[0][0]:.0%}" if worst else f"  {label}: max coverage: 0%")
    for cov, t, r in worst[:5]:
        print(f"    cover {cov:.0%} {t!r} rect={r}")

print("=== P7 quotes vs preview box (top 2404) + garden box ===")
ts7, s7 = texts_of(os.path.join(ED, "p7-lingua.svg"))
for t in ts7:
    if t["y"] >= 2300 and t["y"] < 2404:
        b = inkbox(t)
        print(f"  quote-row y={t['y']} ink-bottom={b[3]:.1f} clearance-to-2404={2404 - b[3]:.1f} :: {t['t'][:60]}")
for m in RECT_RE.finditer(s7):
    x, y, w, h = (float(m.group(i)) for i in (1, 2, 3, 4))
    if 1400 <= x <= 1500 and y >= 1300 and y <= 1400:
        print(f"  garden-area rect x={x} y={y} w={w} h={h} fill={m.group(5)} bottom={y + h}")
print("  P7 rects with x=65 w=1820 (preview band):")
for m in RECT_RE.finditer(s7):
    x, y, w, h = (float(m.group(i)) for i in (1, 2, 3, 4))
    if x == 65.0 and w == 1820.0:
        print(f"    y={y} h={h} bottom={y + h} fill={m.group(5)}")
print("  lone 。 ink box:")
for t in ts7:
    if t["t"].strip() == "。":
        print(f"    x={t['x']} y={t['y']} ink={tuple(round(v, 1) for v in inkbox(t))}")
print("  invitation rows ink boxes:")
for t in ts7:
    if "請把你的來信" in t["t"] or t["t"].strip() == "來信！":
        print(f"    y={t['y']} ink={tuple(round(v, 1) for v in inkbox(t))} :: {t['t'][:40]}")
