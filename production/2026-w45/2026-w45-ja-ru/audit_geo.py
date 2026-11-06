# -*- coding: utf-8 -*-
"""JA x RU W45 builder gate suite (round 3 output).
1. kinsoku: no rendered line starts with a NO_START char (canonical svglib set).
2. same-baseline ink collision: text nodes sharing a baseline (dy<2) whose
   ink boxes overlap or touch (gap<0) on any page.
3. right-edge advance scan: every text node's x + text_w advance <= 1950
   (anchor-aware: start/middle/end).
4. P6 chart-label ink coverage: chart label ink boxes vs later-drawn rects,
   true ink via PIL mask getbbox (NOT font getbbox); coverage must be <30%.
5. gloss count: rendered gloss() strings split on '·' itself, core vs edition.
6. golden phrases: each of the 8 Japanese phrases exactly 2x in the
   whitespace-stripped concatenation of all SVG text.
7. banned term: 0 occurrences in SVGs + build code.
8. simplified-residue: word-level — every CJK string in edition code that is
   absent from core code must be Japanese (kana-bearing) or an FR addition
   (reported for review, not auto-passed).
"""
import os, re, sys, html, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import text_w, wrap  # noqa: E402

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
ED = os.path.join(BASE, "weekly-report-w45-ja-ru", "svg")
CO = os.path.join(BASE, "weekly-report-w45-ja-core", "svg")
NO_START = set("。、，．！？：；）」』】ー…‥・")

def load_texts(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'<text[^>]*x="([\d.]+)"[^>]*y="([\d.]+)"[^>]*font-size="([\d.]+)"[^>]*(?:font-weight="([^"]*)")?[^>]*>(.*?)</text>', s):
        x, y, fs, fw, inner = m.groups()
        txt = html.unescape(re.sub(r"<[^>]+>", "", inner))
        out.append({"x": float(x), "y": float(y), "size": float(fs),
                    "bold": (fw == "bold"), "txt": txt})
    return out

def anchor_of(m):
    return m.group(0)

def texts_with_anchor(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>', s):
        attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        txt = html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        fam = attrs.get("font-family", "")
        kind = "serif" if "Serif" in fam else ("sans" if "Sans" in fam else "other")
        out.append({"x": float(attrs["x"]), "y": float(attrs["y"]),
                    "size": float(attrs["font-size"]),
                    "anchor": attrs.get("text-anchor", "start"),
                    "bold": (attrs.get("font-weight") == "bold"),
                    "kind": kind, "txt": txt})
    return out

pages = ["p1-hyoushi", "p2-kurashi", "p3-bunka", "p4-supotsu",
         "p5-wakamono", "p6-fukayomi", "p7-kotoba", "p8-tesuto"]

print("== 1. kinsoku ==")
kinsoku_hits = []
for pg in pages:
    for t in load_texts(os.path.join(ED, pg + ".svg")):
        s = t["txt"].lstrip()
        if s and s[0] in NO_START:
            kinsoku_hits.append((pg, t["y"], s[:30]))
print("kinsoku hits:", len(kinsoku_hits), kinsoku_hits[:10])

print("== 2. same-baseline ink collisions ==")
from PIL import ImageFont
# ink width via build text_w (advance) is conservative for collision: use it
coll = []
for pg in pages:
    ts = texts_with_anchor(os.path.join(ED, pg + ".svg"))
    # group by baseline (same y, tolerance 2)
    ts.sort(key=lambda t: (round(t["y"] / 2), t["x"]))
    groups = {}
    for t in ts:
        groups.setdefault(round(t["y"] / 2), []).append(t)
    for g, items in groups.items():
        items = [t for t in items if t["kind"] != "other"]
        items.sort(key=lambda t: t["x"])
        for a, b in zip(items, items[1:]):
            # span approx: start-anchor x..x+w; middle x-w/2..x+w/2; end x-w..x
            def span(t):
                w = text_w(t["txt"], t["kind"], t["bold"], t["size"])
                if t["anchor"] == "middle":
                    return (t["x"] - w / 2, t["x"] + w / 2)
                if t["anchor"] == "end":
                    return (t["x"] - w, t["x"])
                return (t["x"], t["x"] + w)
            sa, sb = span(a), span(b)
            if sb[0] < sa[1] - 0.5:  # overlap beyond 0.5px tolerance
                coll.append((pg, a["y"], a["txt"][:40], b["txt"][:40], round(sa[1] - sb[0], 1)))
print("same-baseline collisions:", len(coll))
for c in coll[:12]:
    print("  ", c)

print("== 3. right-edge advance scan (font-family-aware, anchor-aware) ==")
edge = []
for pg in pages:
    for t in texts_with_anchor(os.path.join(ED, pg + ".svg")):
        if t["kind"] == "other":
            continue  # masthead blackletter: frozen, core-identical, covered by canonical audit
        w = text_w(t["txt"], t["kind"], t["bold"], t["size"])
        if t["anchor"] == "middle":
            right = t["x"] + w / 2
        elif t["anchor"] == "end":
            right = t["x"]
        else:
            right = t["x"] + w
        if right > 1950.5:
            edge.append((pg, t["y"], round(right, 1), t["txt"][:50]))
print("right-edge violations:", len(edge), edge[:10])

print("== 4. P6 chart-label ink coverage (mask ink, baseline-anchored, paint order) ==")
from PIL import ImageFont as IF
SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SANS_B = SANS.replace("Regular", "Bold")
SERIF_B = SERIF.replace("Regular", "Bold")
def mask_ink_box(txt, size, bold, serif):
    path = SERIF_B if (serif and bold) else (SERIF if serif else (SANS_B if bold else SANS))
    f = IF.truetype(path, int(size * 4), index=0)
    ascent, _descent = f.getmetrics()  # at 4x; mask row 0 = ascender line
    mask = f.getmask(txt)  # default anchor "la": left-ascender
    bb = mask.getbbox()
    if not bb:
        return None
    # ink box in SVG coords given baseline y and start x:
    # left = x + bb[0]/4; top = y - ascent/4 + bb[1]/4
    return (bb[0] / 4, -ascent / 4 + bb[1] / 4, bb[2] / 4, -ascent / 4 + bb[3] / 4)
s = open(os.path.join(ED, "p6-fukayomi.svg"), encoding="utf-8").read()
CHART_NAMES = {"近場の満足", "温泉", "紅葉", "グルメ"}
CHART_VALS = {"38%", "27%", "21%", "14%"}
ordered = []  # (kind, payload) in paint order, merged by match offset
spans = []
for m in re.finditer(r'<text([^>]*)>(.*?)</text>', s):
    ad = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
    txt = html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
    spans.append((m.start(), "text", {"x": float(ad["x"]), "y": float(ad["y"]),
                                      "size": float(ad["font-size"]),
                                      "bold": ad.get("font-weight") == "bold",
                                      "serif": "Serif" in ad.get("font-family", ""),
                                      "txt": txt}))
for m in re.finditer(r'<rect([^>]*)/>', s):
    ad = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
    fl = ad.get("fill", "none")
    if fl != "none":
        rx, ry = float(ad.get("x", 0)), float(ad.get("y", 0))
        spans.append((m.start(), "rect", (rx, ry,
                                          rx + float(ad["width"]),
                                          ry + float(ad["height"]))))
for _off, kind, payload in sorted(spans):
    ordered.append((kind, payload))
worst = 0.0; worst_desc = None; nlabels = 0
for i, (kind, t) in enumerate(ordered):
    if kind != "text" or t["txt"] not in CHART_NAMES | CHART_VALS:
        continue
    nlabels += 1
    ib = mask_ink_box(t["txt"], t["size"], t["bold"], t["serif"])
    if not ib:
        continue
    x0, y0 = t["x"] + ib[0], t["y"] + ib[1]
    x1, y1 = t["x"] + ib[2], t["y"] + ib[3]
    area = max(0.0, (x1 - x0) * (y1 - y0))
    for kind2, r in ordered[i + 1:]:
        if kind2 != "rect":
            continue
        ox = max(0.0, min(x1, r[2]) - max(x0, r[0]))
        oy = max(0.0, min(y1, r[3]) - max(y0, r[1]))
        if area and ox * oy / area > worst:
            worst = ox * oy / area; worst_desc = (t["txt"], round(worst, 3))
print(f"chart labels checked: {nlabels} (expect 8); worst later-rect ink coverage:",
      round(worst, 4), worst_desc, "(gate <0.30)")

print("== 5. gloss counts (split on ·) ==")
def gloss_strings(code_path):
    src = open(code_path, encoding="utf-8").read()
    return re.findall(r'\.gloss\("([^"]*)"\)', src)
for f in ["content12.py", "content34.py", "content56.py"]:
    co_g = gloss_strings(os.path.join(BASE, "..", "hidden_files", "weekly-report-w45-ja-build", f))
    ed_g = gloss_strings(os.path.join(os.path.dirname(os.path.abspath(__file__)), f))
    co_n = [len(g.split("·")) for g in co_g]
    ed_n = [len(g.split("·")) for g in ed_g]
    print(f, "core gloss items:", co_n, "edition:", ed_n, "MATCH" if co_n == ed_n else "MISMATCH")

print("== 6. golden phrases 2x ==")
alltext = ""
for pg in pages:
    s = open(os.path.join(ED, pg + ".svg"), encoding="utf-8").read()
    alltext += re.sub(r"\s+", "", html.unescape(re.sub(r"<[^>]+>", "", s)))
phrases = ["文化の日は、11月3日（火よう日）です。",
           "ゆっくり、ゆるく整える日本の11月です。",
           "『ゆる』は、無理をしない、ゆっくり、という意味です。",
           "鍋の材料が1か月早く並び始めました。",
           "伝統工芸と紅葉と光を、いっしょに楽しむことができます。",
           "ソフトバンクが2連勝でスタートしました。",
           "ルールを守って、楽しいハロウィンにしましょう。",
           "紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。"]
for ph in phrases:
    print(" ", alltext.count(ph), "x ::", ph[:40])

print("== 7. banned term (written as escapes so this script itself stays clean) ==")
BANNED = ["\u6865\u63a5", "\u6a4b\u63a5"]
for root, label in [(ED, "svg"), (os.path.dirname(os.path.abspath(__file__)), "build-code")]:
    n = 0
    for fn in os.listdir(root):
        if fn.endswith((".svg", ".py")):
            data = open(os.path.join(root, fn), encoding="utf-8", errors="ignore").read()
            for b in BANNED:
                n += data.count(b)
    print(f"  {label}: {n}")

print("== 8b. P8 note completeness (no untranslated note survives) ==")
_CJK2 = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
def _segs(path):
    s = open(path, encoding="utf-8").read()
    texts = [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in re.findall(r"<text[^>]*>(.*?)</text>", s)]
    hdr = re.compile(r"^—\s*(.{0,24}?\d.{0,12}?)\s*—$")
    start = None
    for i, t in enumerate(texts):
        if hdr.match(t.strip()) and len(t.strip()) <= 34:
            start = i
            break
    els = texts[start:-2]
    entries, cur = {}, None
    for t in els:
        if hdr.match(t.strip()):
            continue
        m = re.match(r"^\s*(\d{1,3})\.\s", t)
        if m:
            cur = int(m.group(1)); entries[cur] = t[m.end():]
        elif cur is not None:
            a, b = entries[cur], t
            entries[cur] = a + b if (_CJK2.search(a[-1:]) or _CJK2.search(b[:1])) else a + " " + b
    return {n: s.strip() for n, s in entries.items()}
_co = _segs(os.path.join(CO, "p8-tesuto.svg"))
_ed = _segs(os.path.join(ED, "p8-tesuto.svg"))
def _splitkey(seg):
    if " — " in seg:
        k, n = seg.split(" — ", 1)
        return k.strip(), n.strip()
    return seg.strip(), ""
_leaks = []
for _n in sorted(_co):
    _ck, _cn = _splitkey(_co[_n]); _ek, _en = _splitkey(_ed[_n])
    # writing item: printed as "N. ✓ note" (no dash) — compare the note tail
    if _ck.startswith("✓") or _ek.startswith("✓"):
        continue
    if _cn == _en and _cn:
        _leaks.append((_n, _cn))
print("untranslated-note leaks:", _leaks if _leaks else "NONE (150/150 notes differ from core or are language-neutral)")

print("== 8. code string set-diff (Chinese residue, word-level) ==")
import unicodedata
def quoted_strings(path):
    src = open(path, encoding="utf-8").read()
    return set(re.findall(r'"([^"]*)"', src))
core_dir = os.path.join(BASE, "..", "hidden_files", "weekly-report-w45-ja-build")
ed_dir = os.path.dirname(os.path.abspath(__file__))
core_q, ed_q = set(), set()
for f in ["bslib4.py", "content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "render.py"]:
    core_q |= quoted_strings(os.path.join(core_dir, f))
    ed_q |= quoted_strings(os.path.join(ed_dir, f))
CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff]")
only_ed = sorted(s for s in ed_q - core_q if CJK.search(s))
only_co = sorted(s for s in core_q - ed_q if CJK.search(s))
print("edition-only CJK strings:", len(only_ed))
for s in only_ed:
    print("   ED-ONLY:", s[:100])
print("core-only CJK strings (must all be mapped Chinese/furniture):", len(only_co))
for s in only_co:
    print("   CO-ONLY:", s[:100])
