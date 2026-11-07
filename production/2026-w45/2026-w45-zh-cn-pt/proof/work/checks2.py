# -*- coding: utf-8 -*-
"""P7 golden sentences, readers corner, B1 glossline, P6 chart-label element check."""
import re, glob, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib

CORE_BUILD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zhcn-build")
PT_BUILD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zh-cn-pt-build")
ED_SVG = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg")
CORE_SVG = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhcn-core/svg")

# ---- golden sentences ----
pt7 = open(os.path.join(PT_BUILD, "content7.py"), encoding="utf-8").read()
core7 = open(os.path.join(CORE_BUILD, "content7.py"), encoding="utf-8").read()
pt_phrases = re.findall(r'\("([^"]+)", "([^"]+)", "(Página \d+)"\)', pt7)
core_phrases = re.findall(r'\("([^"]+)", "([^"]+)", "\(Page (\d+)\)"\)', core7)
print("PT phrases:", len(pt_phrases), "core phrases:", len(core_phrases))
print("PT phrase Chinese == core phrase Chinese:", [p[0] for p in pt_phrases] == [p[0] for p in core_phrases])
print("PT page tags:", [p[2] for p in pt_phrases], "core page tags:", ["Page " + p[2] for p in core_phrases])
# article sources: all core content files concatenated (target text)
arts = ""
for f in ["content12.py", "content34.py", "content56.py", "content7.py"]:
    arts += open(os.path.join(CORE_BUILD, f), encoding="utf-8").read()
for ch, pt_tr, pg in pt_phrases:
    bare = ch.strip("「」")
    # contiguous: bare must occur in article sources outside the P7 phrases block
    arts_no_p7 = arts.split("phrases of the week")[0]
    print(f"  {ch} {pg}: in-articles-contiguous={bare in arts_no_p7}")
# rendered P7 SVG contains each phrase + page tag?
p7svg = open(os.path.join(ED_SVG, "p7-ciyu.svg"), encoding="utf-8").read()
for ch, pt_tr, pg in pt_phrases:
    print(f"  rendered P7: {ch} present={ch in p7svg} | tag ({pg}) present={('(' + pg + ')') in p7svg} | PT transl present={pt_tr in p7svg}")

# ---- B1 glossline ----
for name, build, needle in [("core", CORE_BUILD, "Saturday evening"), ("PT", PT_BUILD, "sábado à noite")]:
    src = open(os.path.join(build, "content7.py"), encoding="utf-8").read()
    for line in src.splitlines():
        if needle in line:
            print(f"B1 glossline {name}: {line.strip()[:220]}")
# Chinese result string in that glossline must be unchanged: find the line with the Chinese order example
for name, build in [("core", CORE_BUILD), ("PT", PT_BUILD)]:
    src = open(os.path.join(build, "content7.py"), encoding="utf-8").read()
    for line in src.splitlines():
        if "11月7日" in line and ("星期六" in line or "晚上" in line):
            print(f"  date-order line {name}: {line.strip()[:200]}")

# ---- readers corner ----
m = re.search(r'Exemplo da redaçã[^"]*próximo número\."', pt7)
print("PT disclosure+invitation in content7:", bool(m))
if m:
    print("  full text:", m.group(0))
inv = "Escreva-nos! Envie a sua carta em chinês — duas frases já bastam — e ela pode sair no próximo número."
print("invitation verbatim in PT content7:", inv in pt7)
print("invitation verbatim in delivered P7 SVG (as rendered lines joined):", end=" ")
# rendered lines: disclosure wraps; join all P7 text nodes in order and search with whitespace collapsed
texts = re.findall(r'<text[^>]*>([^<]*)</text>', p7svg)
joined = " ".join(texts)
joined_nospace = re.sub(r'\s+', ' ', joined)
print(inv in joined_nospace)
# disclosure wrapped lines: nodes containing disclosure fragments, distinct y
disc_words = ["Exemplo", "redação", "VOL.1", "prometeu", "cartas", "verdadeiras", "leitores", "Adiado", "cancelado", "Escreva-nos"]
nodes = re.findall(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>([^<]*)</text>', p7svg)
disc_nodes = [(float(x), float(y), t) for x, y, t in nodes if any(w in t for w in disc_words) and float(x) < 1000]
print("disclosure-region nodes (x<1000, col3 area):", len(disc_nodes))
for x, y, t in disc_nodes:
    print(f"   y={y} x={x} {t[:90]}")
print("distinct disclosure baselines:", sorted(set(y for _, y, _ in disc_nodes)))

# ---- P6 chart-label element check: text ink vs later-drawn rects ----
def ink_boxes(path):
    src = open(path, encoding="utf-8").read()
    # tokenise in paint order: rects and texts
    toks = []
    for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^/]*/>|<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"( font-weight="700")?[^>]*?(?: text-anchor="(start|middle|end)")?[^>]*>([^<]*)</text>', src):
        if m.group(1) is not None:
            toks.append(("rect", float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4))))
        else:
            x, y, fam, size = float(m.group(5)), float(m.group(6)), m.group(7), float(m.group(8))
            bold = bool(m.group(9)); anchor = m.group(10) or "start"; t = m.group(11)
            if not t.strip():
                continue
            kind = "serif" if "Serif" in fam else "sans"
            f = svglib._font(kind, bold, int(round(size * 4)))
            bb = f.getbbox(t)
            adv = f.getlength(t) / 4.0
            l, r = bb[0] / 4.0, bb[2] / 4.0
            top, bot = bb[1] / 4.0, bb[3] / 4.0
            if anchor == "start":
                a, b = x + l, x + r
            elif anchor == "end":
                a, b = x - adv + l, x - adv + r
            else:
                a, b = x - adv / 2 + l, x - adv / 2 + r
            toks.append(("text", a, y + top, b, y + bot, t))
    return toks
for name, path in [("core", os.path.join(CORE_SVG, "p6-shendu.svg")), ("ed", os.path.join(ED_SVG, "p6-shendu.svg"))]:
    toks = ink_boxes(path)
    hits = []
    for i, tk in enumerate(toks):
        if tk[0] != "text":
            continue
        _, a, top, b, bot, t = tk
        for tk2 in toks[i + 1:]:
            if tk2[0] != "rect":
                continue
            _, rx, ry, rw, rh = tk2
            if a < rx + rw and b > rx and top < ry + rh and bot > ry:
                # overlap area fraction of ink box
                ox = min(b, rx + rw) - max(a, rx); oy = min(bot, ry + rh) - max(top, ry)
                frac = (ox * oy) / max(1.0, (b - a) * (bot - top))
                hits.append((t[:40], rx, ry, rw, rh, round(frac, 3)))
    print(f"P6 chart-label element check {name}: later-rect overlaps on text ink: {len(hits)}")
    for h in hits:
        print("   ", h)
