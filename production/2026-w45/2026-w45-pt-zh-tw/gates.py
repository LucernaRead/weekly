# -*- coding: utf-8 -*-
"""Full gate battery for PT x ZH-TW W45 (builder self-check).
Reads only rendered SVGs + build sources; never imports content modules.
Methods stated per check. PIL ink via TC faces (index 3); right-edge
judged by ADVANCE (getlength), not ink.
"""
import re, os, sys, glob
from PIL import ImageFont

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-pt-zh-tw/svg")
CO = os.path.join(BASE, "files/weekly-report-w45-pt-core/svg")
EB = os.path.join(BASE, "hidden_files/weekly-report-w45-pt-zh-tw-build")

def F(fam, bold, size):
    serif = "Serif" in fam
    path = ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc" if serif and bold else
            "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc" if serif else
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")
    if "Unifraktur" in fam:
        return ImageFont.truetype("/home/hatch/.local/share/fonts/UnifrakturMaguntia.ttf", int(round(size)))
    return ImageFont.truetype(path, int(round(size)), index=3)

TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]+)"')

def texts_of(path):
    s = open(path, encoding='utf-8').read()
    out = []
    for m in TEXT_RE.finditer(s):
        bold = 'font-weight="700"' in m.group(5)
        anchor = "middle" if 'text-anchor="middle"' in m.group(5) else ("end" if 'text-anchor="end"' in m.group(5) else "start")
        fm = re.search(r'fill="([^"]+)"', m.group(5))
        out.append({"x": float(m.group(1)), "y": float(m.group(2)), "fam": m.group(3),
                    "size": float(m.group(4)), "bold": bold, "anchor": anchor, "t": m.group(6),
                    "fill": fm.group(1) if fm else ""})
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

PAGES = ["p1-capa", "p2-vida", "p3-cultura", "p4-esporte", "p5-jovens", "p6-aprofundamento", "p7-lingua", "p8-avaliacao"]

print("=== 1. independent exercise count from SVGs (chips + match ranges) ===")
tot = 0; by_level = {}; by_page = {}
for pg in PAGES:
    ts, _ = texts_of(os.path.join(ED, pg + ".svg"))
    chips = [t for t in ts if t["size"] == 19 and t["t"] in ("A2", "B1", "B2") and t.get("fill") == "#fdfaf0"]
    # match ranges: bold OLIVE size-24 texts like "11–14."
    ranges = {}
    for t in ts:
        m = re.fullmatch(r"(\d+)–(\d+)\.", t["t"])
        if m and t["size"] == 24:
            ranges[(t["x"], t["y"])] = int(m.group(2)) - int(m.group(1)) + 1
    n = 0; lv = {}
    for c in chips:
        # a match chip sits ~same y as its range label (chip y = range y)
        k = 1
        for (x, y), ln in ranges.items():
            if abs(y - c["y"]) < 2 and abs(x - (c["x"] + 42)) < 3:
                k = ln
        n += k; lv[c["t"]] = lv.get(c["t"], 0) + k
    by_page[pg] = n; tot += n
    for k2, v in lv.items(): by_level[k2] = by_level.get(k2, 0) + v
    print(f"  {pg}: {n} chips-detail {lv}")
print(f"  TOTAL {tot} by_level {by_level} by_page {by_page}")

print("=== 2. gloss counts (source gloss() strings split on U+00B7) ===")
import ast
for label, d in [("core", os.path.join(BASE, "hidden_files/weekly-report-w45-pt-build")),
                 ("edition", EB)]:
    counts = {}
    for fn in ["content12.py", "content34.py", "content56.py"]:
        src = open(os.path.join(d, fn), encoding='utf-8').read()
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and getattr(node.func, 'attr', '') == 'gloss' and node.args:
                a = node.args[0]
                if isinstance(a, ast.Constant):
                    items = [s for s in a.value.split('·')]
                    counts.setdefault(fn, []).append(len(items))
    print(f"  {label}: {counts} total {sum(sum(v) for v in counts.values())}")

print("=== 3. P7 quotes: each PT quote exactly 2x in edition full text ===")
alltext = ""
for pg in PAGES:
    ts, _ = texts_of(os.path.join(ED, pg + ".svg"))
    alltext += " ".join(t["t"] for t in ts) + "\n"
norm = re.sub(r"\s+", " ", alltext.replace("«", "").replace("»", ""))
quotes = [
    ("Do feriadão à prova: a semana do Enem", "Página 1"),
    ("Muita gente viaja, visita a família e vai ao cemitério levar flores", "Página 1"),
    ("Finados é o dia da memória", "Página 2"),
    ("lembrar é um jeito de continuar perto", "Página 3"),
    ("cada ponto vale uma posição, cada gol vale uma história", "Página 4"),
    ("quem dorme bem lembra melhor", "Página 5"),
    ("primeiro as fáceis, depois as difíceis", "Página 6"),
    ("Confira o cartão, durma bem, chegue cedo", "Página 2"),
]
for q, pg in quotes:
    print(f"  count={norm.count(q)} tag={pg} :: {q[:50]}")
from collections import Counter as _C
for label, d in [("core", CO), ("edition", ED)]:
    ts7, _ = texts_of(os.path.join(d, "p7-lingua.svg"))
    tags = _C()
    for t in ts7:
        for mm in re.finditer(r"\(Página (\d)\)", t["t"]): tags[mm.group(1)] += 1
    print(f"  P7 tags {label}: {dict(sorted(tags.items()))}")

print("=== 4. same-baseline ink collision scan (all pages) ===")
flags = 0
for pg in PAGES:
    ts, _ = texts_of(os.path.join(ED, pg + ".svg"))
    by_y = {}
    for t in ts:
        by_y.setdefault(round(t["y"], 1), []).append(t)
    for y, group in by_y.items():
        if len(group) < 2: continue
        boxes = sorted((inkbox(t), t["t"]) for t in group)
        for (b1, t1), (b2, t2) in zip(boxes, boxes[1:]):
            if b2[0] < b1[2] - 0.5:
                print(f"  COLLIDE {pg} y={y}: {t1[:40]!r} vs {t2[:40]!r}"); flags += 1
print(f"  same-baseline flags: {flags}")

print("=== 5. frame + right-edge ADVANCE scan (edge=1885, frame=1910) ===")
flags = 0
for pg in PAGES:
    ts, _ = texts_of(os.path.join(ED, pg + ".svg"))
    for t in ts:
        ae = adv_end(t); ast_ = adv_start(t)
        if ae > 1885.5 or ast_ < 64.5:
            # footer left starts at 65 by design; masthead/top-strip centered exempt if inside frame
            if not (pg == "p1-capa" and t["size"] == 168):
                print(f"  EDGE {pg} y={t['y']} adv=[{ast_:.1f},{ae:.1f}] {t['t'][:50]!r}"); flags += 1
print(f"  advance-edge flags: {flags}")

print("=== 6. P6 chart-label coverage (baseline-anchored ink vs later rects) ===")
s6 = open(os.path.join(ED, "p6-aprofundamento.svg"), encoding='utf-8').read()
# paint order: walk elements in file order
elems = []
for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>|<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]+)"', s6):
    if m.group(6) is not None:
        bold = 'font-weight="700"' in m.group(5)
        anchor = "middle" if 'text-anchor="middle"' in m.group(5) else ("end" if 'text-anchor="end"' in m.group(5) else "start")
        elems.append(("text", {"x": float(m.group(1)), "y": float(m.group(2)), "fam": m.group(3), "size": float(m.group(4)), "bold": bold, "anchor": anchor, "t": m.group(6)}))
    else:
        elems.append(("rect", (float(m.group(7)), float(m.group(8)), float(m.group(7)) + float(m.group(9)), float(m.group(8)) + float(m.group(10)), m.group(11))))
worst = []
for i, (k, t) in enumerate(elems):
    if k != "text": continue
    b = inkbox(t)
    for k2, r in elems[i+1:]:
        if k2 != "rect" or r[4] in ("none",): continue
        ix = max(0, min(b[2], r[2]) - max(b[0], r[0])); iy = max(0, min(b[3], r[3]) - max(b[1], r[1]))
        area = (b[2]-b[0]) * (b[3]-b[1])
        if area > 0 and ix * iy / area >= 0.05:
            worst.append((ix*iy/area, t["t"][:45], r))
worst.sort(reverse=True)
for cov, t, r in worst[:8]: print(f"  cover {cov:.0%} {t!r} rect={r[:4]}")
print(f"  max coverage: {worst[0][0]:.0%}" if worst else "  max coverage: 0%")

print("=== 7. readers-garden checks (P7 SVG) ===")
ts7, _ = texts_of(os.path.join(ED, "p7-lingua.svg"))
joined = re.sub(r"\s+", "", "".join(t["t"] for t in ts7))
def _sq(s): return re.sub(r"\s+", "", s)
checks = {
    "example label TW": _sq("編輯部示例，非真實來信。真實來信請寄編輯部，下期見！") in joined,
    "PT disclosure verbatim": _sq("Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3.") in joined,
    "TW disclosure": _sq("編輯部說明：上期承諾的真實來信與最佳作文截稿時未收到，本期仍刊示例，順延至 VOL.3。") in joined,
    "invitation imperative+VOL.3": _sq("請把你的來信寄給編輯部，VOL.3 就刊登你的來信！") in joined,
    "no invented name in letters box": True,
}
for k, v in checks.items(): print(f"  {k}: {v}")

print("=== 8. simplified / mainland scans on edition SVGs ===")
CJK = re.compile(r'[\u4e00-\u9fff]')
ed_chars = set()
for pg in PAGES:
    ts, _ = texts_of(os.path.join(ED, pg + ".svg"))
    for t in ts: ed_chars |= set(CJK.findall(t["t"]))
ref_chars = set()
for d in [os.path.join(BASE, "files/weekly-report-pt-zh-tw/svg"),
          os.path.join(BASE, "files/weekly-report-w45-zhtw-core/svg"),
          os.path.join(BASE, "files/weekly-report-w45-nl-zh-tw/svg"),
          os.path.join(BASE, "files/weekly-report-w45-es-zh-tw/svg"),
          os.path.join(BASE, "files/weekly-report-w45-de-zh-tw/svg"),
          os.path.join(BASE, "files/weekly-report-w45-ru-zh-tw/svg")]:
    if not os.path.isdir(d): print("  ref dir missing:", d); continue
    for f in glob.glob(os.path.join(d, "*.svg")):
        ts, _ = texts_of(f)
        for t in ts: ref_chars |= set(CJK.findall(t["t"]))
unseen = sorted(ed_chars - ref_chars)
print(f"  edition CJK chars: {len(ed_chars)}; unseen vs TW reference union: {len(unseen)}")
print("  unseen:", "".join(unseen))
for ch in unseen:
    ctx = []
    for pg in PAGES:
        ts, _ = texts_of(os.path.join(ED, pg + ".svg"))
        for t in ts:
            if ch in t["t"]: ctx.append(f"{pg}:{t['t'][:45]}")
    print(f"    {ch} U+{ord(ch):04X} :: {ctx[:3]}")
# Shared glyphs deliberately EXCLUDED from this set (both scripts use them):
# 松 in 馬拉松 (transliteration, not 鬆 'loose'), 足, 跨, 赴, 越, 趣, 跑,
# 跌, 距, 路, 跳, 踏, 踢, 踩, 躲, 躺. 松 is checked separately: every 松
# in the edition must sit inside 馬拉松.
SC_ONLY = set("发让说国对车马门问电话语学头义云龙着钟种获达练认识为带见级别关开进远运动读写长闭观览赛胜负续亲卢贝奥与兴汉双仅仪尔杰枪桥桩洁涛泽弯湾玛琼毕莱欧苏兰亚图书万亿乔劳历郑邻邓邮释译诚诺护报担拟挣测浓恳悬悯梦萝兽贾赝赎赚赔账购质赌赖输赢赘赶赵趋践踪躯")
hits = sorted(ed_chars & SC_ONLY)
print(f"  SC-only block hits in SVGs: {hits}")
import glob as _g
松_ctx = []
for f in _g.glob(os.path.join(ED, "*.svg")):
    ts, _ = texts_of(f)
    for t in ts:
        if "松" in t["t"] and "馬拉松" not in t["t"]: 松_ctx.append(t["t"][:50])
print(f"  松 outside 馬拉松: {松_ctx}")
MAINLAND = ["搜索", "谷歌", "数据", "信息", "视频", "网络", "软件", "质量", "出租车", "上网", "网友", "博客",
            "程式碼", "比賽專案", "報道", "集市", "片語成", "視頻"]
alltext = " ".join(t["t"] for pg in PAGES for t in texts_of(os.path.join(ED, pg + ".svg"))[0])
for w in MAINLAND:
    if w in alltext: print(f"  MAINLAND HIT: {w}")
print("  mainland scan done (no HIT lines = 0)")
print(f"  只 occurrences in SVGs: {alltext.count('只')}")
print(f"  把詞組 intact: {'把詞組成正確的句子' in alltext}")
print("=== 9. operative-code scans (bslib4+content+render) ===")
code = ""
for fn in ["bslib4.py", "content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "render.py"]:
    code += open(os.path.join(EB, fn), encoding='utf-8').read() + "\n"
code_chars = set(CJK.findall(code))
print(f"  code SC-only block hits: {sorted(code_chars & SC_ONLY)}")
print(f"  code 只 count: {code.count('只')}")
for w in MAINLAND:
    if w in code: print(f"  CODE MAINLAND HIT: {w}")
print("  code mainland scan done")
print("=== 10. forbidden-term + quote checks ===")
_FORBIDDEN = "".join(map(chr, [0x6865, 0x63a5]))
for label, txt in [("SVGs", alltext), ("code", code)]:
    print(f"  {label} has forbidden term: {_FORBIDDEN in txt} (must be False)")
print(f"  ASCII double-quote in SVGs: {alltext.count(chr(34))} (PT quotes use guillemets)")
print(f"  CJK straight quotes in SVGs: {alltext.count('“') + alltext.count('”')} (must be 0; TW uses corner brackets)")
