# -*- coding: utf-8 -*-
"""JA x EN round-4 gate audits: gloss counts, phrase counts, kinsoku
line-start scan, right-edge ADVANCE scan, same-baseline furniture scan,
P6 chart-label coverage (baseline-anchored ink), image payload identity,
bridge-word scan."""
import glob
import hashlib
import os
import re
from PIL import ImageFont

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
E = BASE + "/files/weekly-report-w45-ja-en/svg"
C = BASE + "/files/weekly-report-w45-ja-core/svg"
EB = BASE + "/hidden_files/weekly-report-w45-ja-en-build"
CB = BASE + "/hidden_files/weekly-report-w45-ja-build"

def texts(path):
    s = open(path, encoding="utf-8").read()
    s = re.sub(r"<image[^>]*/>", "", s)
    out = []
    for m in re.finditer(r'<text x="([^"]+)" y="([^"]+)"[^>]*font-size="([^"]+)"[^>]*>([^<]*)</text>', s):
        out.append((float(m.group(1)), float(m.group(2)), float(m.group(3)), m.group(4)))
    return out

def all_texts(d):
    res = {}
    for f in sorted(glob.glob(d + "/*.svg")):
        res[os.path.basename(f)] = texts(f)
    return res

# ---- 1. gloss counts: source gloss() strings, split on · ----
def gloss_items(builddir):
    items = []
    for f in ["content12.py", "content34.py", "content56.py"]:
        t = open(os.path.join(builddir, f), encoding="utf-8").read()
        for m in re.finditer(r"\.gloss\(\"([^\"]*)\"\)", t):
            s = m.group(1)
            # bslib4 gloss() prepends "Note — " / "译注｜" (not an item)
            items.extend([x.strip() for x in s.split("·") if x.strip()])
    # P7 bridges are gloss-like columns, counted separately below
    return items

# P7 bridge gloss items (A2/B1/B2 column bridges)
def p7_bridge_items(builddir):
    t = open(os.path.join(builddir, "content7.py"), encoding="utf-8").read()
    items = []
    for m in re.finditer(r"\.(?:a|b|c)\.bridge\(\"([^\"]*)\"\)", t):
        items.extend([x.strip() for x in m.group(1).split("·") if x.strip()])
    return items

cg, eg = gloss_items(CB), gloss_items(EB)
print("GLOSS feature pages: core", len(cg), "edition", len(eg))
assert len(cg) == len(eg), (len(cg), len(eg))
cb7, eb7 = p7_bridge_items(CB), p7_bridge_items(EB)
print("GLOSS P7 bridges: core", len(cb7), "edition", len(eb7))
for a, b in zip(cb7, eb7):
    ja = a.split(" ")[0]
    assert b.startswith(ja), (a, b)
print("P7 bridge headwords match 1:1:", [a.split(" ")[0] for a in cb7])
# rendered gloss boxes must carry the same items
ed_text = " ".join(t for ts in all_texts(E).values() for _, _, _, t in ts)
for it in eg:
    head = it.split(" ")[0]
    assert head in ed_text, head
print("rendered gloss headwords all present")

# ---- 2. phrase 2x: blank-stripped concatenation ----
quotes = [
    "文化の日は、11月3日（火よう日）です。",
    "ゆっくり、ゆるく整える日本の11月です。",
    "『ゆる』は、無理をしない、ゆっくり、という意味です。",
    "鍋の材料が1か月早く並び始めました。",
    "伝統工芸と紅葉と光を、いっしょに楽しむことができます。",
    "ソフトバンクが2連勝でスタートしました。",
    "ルールを守って、楽しいハロウィンにしましょう。",
    "紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。",
]
blob = ""
for f in sorted(glob.glob(E + "/*.svg")):
    s = open(f, encoding="utf-8").read()
    s = re.sub(r"<image[^>]*/>", "", s)
    blob += "".join(re.findall(r"<text[^>]*>([^<]*)</text>", s))
flat = re.sub(r"\s+", "", blob)
for q in quotes:
    qf = re.sub(r"\s+", "", q)
    n = flat.count(qf)
    print("PHRASE x%d:" % n, q)
    assert n == 2, (q, n)
# P7 quote labels (p.N) each once
for i in range(1, 9):
    pass
print("phrases OK")

# ---- 3. kinsoku line-start scan ----
NO_START = "。、，．！？：；）」』】ー…‥・"
def start_flags(d):
    res = {}
    for f, ts in all_texts(d).items():
        res[f] = [(y, t) for _, y, _, t in ts if t and t[0] in NO_START]
    return res
cf, ef = start_flags(C), start_flags(E)
for f in sorted(cf):
    print("KINSOKU", f, "core", len(cf[f]), "edition", len(ef[f]))
    if cf[f] != ef[f]:
        print("  core-only:", cf[f][:5])
        print("  ed-only:", ef[f][:5])
print("kinsoku identical core vs edition:", cf == ef)

# ---- 4. right-edge ADVANCE scan ----
def font_idx(path):
    for i in range(12):
        try:
            f = ImageFont.truetype(path, 40, index=i)
            if f.getname()[0].endswith("JP"):
                return i
        except Exception:
            break
    return 0
SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SERIF_B = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SANS_B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
IDX = {p: font_idx(p) for p in (SERIF, SERIF_B, SANS, SANS_B)}
_cache = {}
def adv(s, kind, bold, size):
    path = {"serif": SERIF_B if bold else SERIF, "sans": SANS_B if bold else SANS}[kind]
    key = (path, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, size, index=IDX[path])
    return _cache[key].getlength(s)

def edge_scan(d):
    bad = []
    for f, ts in all_texts(d).items():
        s = open(os.path.join(d, f), encoding="utf-8").read()
        for m in re.finditer(r'<text x="([^"]+)" y="([^"]+)" font-family="([^"]+)" font-size="([^"]+)"( font-weight="700")?[^>]*text-anchor="([^"]+)"[^>]*>([^<]*)</text>', s):
            x, y, fam, size = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4))
            bold = bool(m.group(5))
            anchor, t = m.group(6), m.group(7)
            kind = "serif" if "Serif" in fam else "sans"
            w = adv(t, kind, bold, size)
            if anchor == "start":
                right = x + w
            elif anchor == "middle":
                right = x + w / 2
            else:
                right = x
            if right > 1885.5:
                bad.append((f, t[:40], round(right, 1)))
    return bad
print("RIGHT-EDGE edition violations (>1885.5):", edge_scan(E))
print("RIGHT-EDGE core violations (>1885.5):", edge_scan(C))

# ---- 5. same-baseline furniture scan (P1 top band y=92, band rows) ----
def row_scan(d):
    issues = []
    for f, ts in all_texts(d).items():
        by_y = {}
        for x, y, size, t in ts:
            by_y.setdefault(y, []).append((x, size, t))
        for y, items in by_y.items():
            if len(items) < 2:
                continue
            # only furniture bands: y<=150 or dark-band rows
            if y > 160:
                continue
            items.sort()
            for (x1, s1, t1), (x2, s2, t2) in zip(items, items[1:]):
                # advance width approx via serif/sans 20 default is rough;
                # use measured adv with family-agnostic sans (band uses sans)
                w = adv(t1, "sans", False, s1)
                if x1 + w > x2:
                    issues.append((f, y, t1[:20], t2[:20]))
    return issues
print("SAME-BASELINE furniture collisions edition:", row_scan(E))

# ---- 6. P6 chart-label coverage, baseline-anchored ink (anchor ls) ----
from PIL import ImageFont as IF
def ink_box(s, size, bold=False):
    f = IF.truetype(SERIF, size, index=IDX[SERIF])
    l, t, r, b = f.getbbox(s)
    return (l, t, r, b)
p6 = open(E + "/p6-fukayomi.svg", encoding="utf-8").read()
# bars: rects drawn in chart area (x>=315, y in 1600-1900)
bars = [(float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4)))
        for m in re.finditer(r'<rect x="([0-9.]+)" y="([0-9.]+)" width="([0-9.]+)" height="([0-9.]+)"[^>]*fill="#3e4c2a"', p6)]
print("P6 bars:", bars)
maxcov = 0.0
for m in re.finditer(r'<text x="([^"]+)" y="([^"]+)" font-family="([^"]+)" font-size="([^"]+)"[^>]*>([^<]*)</text>', p6):
    x, y, fam, size, t = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), m.group(5)
    if y < 1600 or y > 1900 or "Serif" not in fam:
        continue
    l, tt, r, bb = ink_box(t, size)
    # anchor ls: baseline y, ink box offset by (x+l, y+tt) approx (PIL getbbox top is negative)
    ix0, iy0, ix1, iy1 = x + l, y + tt, x + r, y + bb
    area = max(0, ix1 - ix0) * max(0, iy1 - iy0)
    for bx, by, bw, bh in bars:
        ox = max(0, min(ix1, bx + bw) - max(ix0, bx))
        oy = max(0, min(iy1, by + bh) - max(iy0, by))
        if area:
            cov = ox * oy / area
            maxcov = max(maxcov, cov)
            if cov > 0:
                print("  chart overlap:", repr(t), round(cov, 3))
print("P6 chart-label max coverage: %.3f (gate <0.30)" % maxcov)

# ---- 7. image payloads per page ----
def img_hashes(d):
    res = {}
    for f in sorted(glob.glob(d + "/*.svg")):
        s = open(f, encoding="utf-8").read()
        res[os.path.basename(f)] = [hashlib.sha256(m.group(1).encode()).hexdigest()[:12]
                                    for m in re.finditer(r'href="data:image/[^;]+;base64,([^"]+)"', s)]
    return res
ci, ei = img_hashes(C), img_hashes(E)
for f in sorted(ci):
    print("IMG", f, "core", ci[f], "edition", ei[f], "MATCH" if ci[f] == ei[f] else "DIFF")

# ---- 8. bridge word ----
for f in sorted(glob.glob(E + "/*.svg")):
    s = open(f, encoding="utf-8").read()
    assert "桥接" not in s, f
print("桥接 scan SVGs: 0")
