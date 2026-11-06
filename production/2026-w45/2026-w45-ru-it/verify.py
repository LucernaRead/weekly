# -*- coding: utf-8 -*-
"""Independent verification battery for W45 RU x IT (builder self-check;
does not replace the independent proofread). Run from this build dir."""
import re, sys, os, hashlib, json
from collections import Counter
sys.path.insert(0, os.getcwd())
from svglib import text_w

CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg")
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-it/svg")
PAGES = ["p1-pervaya", "p2-zhizn", "p3-kultura", "p4-sport", "p5-molodezh", "p6-razbor", "p7-yazyk", "p8-test"]

def texts(path):
    t = open(path, encoding="utf-8").read()
    return re.findall(r"<text[^>]*>([^<]*)</text>", t)

def raw(path):
    return open(path, encoding="utf-8").read()

CYR = re.compile(r"[\u0400-\u04FF]+")
CJK = re.compile(r"[\u4e00-\u9fff]")

print("== 1. Cyrillic token multiset per page (core vs edition) ==")
for pg in PAGES:
    c = Counter(tok for s in texts(f"{CORE}/{pg}.svg") for tok in CYR.findall(s))
    e = Counter(tok for s in texts(f"{ED}/{pg}.svg") for tok in CYR.findall(s))
    diff = {k: (c.get(k, 0), e.get(k, 0)) for k in set(c) | set(e) if c.get(k, 0) != e.get(k, 0)}
    print(f"  {pg}: core total {sum(c.values())} edition total {sum(e.values())} diff-tokens {len(diff)}")
    for k, v in sorted(diff.items()):
        print(f"    {k}: core {v[0]} -> ed {v[1]}")

print("== 2. CJK totals ==")
for pg in PAGES:
    e = "".join(texts(f"{ED}/{pg}.svg"))
    print(f"  {pg}: CJK chars {len(CJK.findall(e))}")

print("== 3. P8 dash-parse: split each printed answer line on first ' — ' ==")
def p8keys(path):
    keys = {}
    for s in texts(path):
        m = re.match(r"^(\d+)\.\s+(.*)$", s.strip())
        if m:
            n = int(m.group(1))
            rest = m.group(2)
            if rest.startswith("✓"):
                keys[n] = "✓"
            elif " — " in rest:
                keys[n] = rest.split(" — ", 1)[0]
            else:
                keys[n] = rest
    return keys
ck, ek = p8keys(f"{CORE}/p8-test.svg"), p8keys(f"{ED}/p8-test.svg")
print(f"  core keys {len(ck)} edition keys {len(ek)}")
kd = {n: (ck.get(n), ek.get(n)) for n in sorted(set(ck) | set(ek)) if ck.get(n) != ek.get(n)}
print(f"  key diffs: {kd}")
print(f"  139/140 identical: {ck.get(139) == ek.get(139) and ck.get(140) == ek.get(140)}")
print(f"  150: core {ck.get(150)!r} ed {ek.get(150)!r}")

print("== 4. Gloss counts (split on · itself) ==")
import ast
for fn, expect in [("content12.py", (3, 3, 3)), ("content34.py", (3, 3, 3)), ("content56.py", (3, 2, 3))]:
    src = open(fn, encoding="utf-8").read()
    calls = re.findall(r"\.gloss\((\"(?:[^\"\\]|\\.)*\")\)", src)
    counts = []
    for c in calls:
        s = ast.literal_eval(c)
        items = [i for i in s.split("·")]
        counts.append(len(items))
    print(f"  {fn}: {len(calls)} calls counts {counts} expected {expect} match={tuple(counts) == expect}")

print("== 5. Image payloads per page (base64 blob sha256) ==")
for pg in PAGES:
    def imgs(path):
        t = raw(path)
        return sorted(hashlib.sha256(b.encode()).hexdigest()[:16] for b in re.findall(r'href="data:image/[^;]+;base64,([^"]+)"', t))
    ci, ei = imgs(f"{CORE}/{pg}.svg"), imgs(f"{ED}/{pg}.svg")
    print(f"  {pg}: core {ci} edition {ei} identical={ci == ei}")

print("== 6. P7 golden sentences: bare Russian quote occurrences, page-joined text ==")
quotes = [
    "Среда, 4 ноября, — выходной посреди рабочей недели",
    "Как жить неделю с праздником посреди недели",
    "Во вторник, 3 ноября, рабочий день короче на час",
    "В среду города устраивают ярмарки и концерты",
    "В воскресенье, 8 ноября, — три матча",
    "Сначала — список: что вам правда нужно",
    "Многие берут отпуск в четверг и в пятницу",
    "Пять дней — почти маленькие каникулы",
]
joined = " ".join(" ".join(texts(f"{ED}/{pg}.svg")) for pg in PAGES)
for q in quotes:
    print(f"  {joined.count(q)}x {q[:50]}")

print("== 7. P7 letters-box geometry (core vs edition) ==")
def p7geom(path):
    t = raw(path)
    # letters box: the rect whose y is ly; find rects in col3 (x=1451) with height lh:
    rects = re.findall(r'<rect x="1451" y="([\d.]+)" width="434" height="([\d.]+)"', t)
    # disclosure line-2: find the disclosure text element(s) by content
    disc_it = [m for m in re.finditer(r'<text x="1473" y="([\d.]+)"[^>]*>([^<]*esempio redazionale[^<]*)</text>', t)]
    disc_ru = [m for m in re.finditer(r'<text x="1473" y="([\d.]+)"[^>]*>([^<]*Настоящих писем[^<]*)</text>', t)]
    return rects, [(m.group(1), m.group(2)[:40]) for m in disc_it], [(m.group(1), m.group(2)[:40]) for m in disc_ru]
print("  core:", p7geom(f"{CORE}/p7-yazyk.svg"))
print("  ed  :", p7geom(f"{ED}/p7-yazyk.svg"))

print("== 8. P6 chart element check: labels, values, later-rect overlap ==")
def chart_check(path):
    t = raw(path)
    # elements in paint order: text and rect with y
    els = []
    for m in re.finditer(r'<(text|rect)[^>]*>', t):
        tag, attrs = m.group(1), m.group(0)
        y = re.search(r'y="([\d.]+)"', attrs)
        els.append((tag, float(y.group(1)) if y else -1, attrs))
    labs = ["Дома с семьёй", "Короткая поездка", "Ярмарка или концерт", "Просто выспятся"]
    vals = ["34%", "28%", "22%", "16%"]
    txt = " ".join(texts(path))
    print("  labels present:", {l: (l in txt) for l in labs})
    print("  values present:", {v: (v in txt) for v in vals})
    # check: any text element whose bbox (advance width, baseline band) is overlapped by a later rect
    texts_els = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*font-size="([\d.]+)"[^>]*>([^<]*)</text>', t):
        x, y, size, s = float(m.group(1)), float(m.group(2)), float(m.group(3)), m.group(4)
        w = text_w(s, "serif" if "Serif" in m.group(0) else "sans", "700" in m.group(0), size)
        texts_els.append((s, x, y, w, size))
    # crude: for chart region y 1550..1800, list rects drawn after each label/value text
    print("  chart-region text elements (from SVG order):")
    for s, x, y, w, size in texts_els:
        if 1500 < y < 1820:
            print(f"    y={y} x={x} w={w:.1f} {s[:40]!r}")
chart_check(f"{ED}/p6-razbor.svg")

print("== 9. Full-width parens + quote-digit leak scan ==")
for pg in PAGES:
    t = "".join(texts(f"{ED}/{pg}.svg"))
    fw = t.count("（") + t.count("）")
    leak = re.findall(r"'[0-9]", t)
    print(f"  {pg}: full-width parens {fw} quote-digit {leak}")

print("== 10. Same-baseline scan, P1 furniture bands (advance widths, gap < 5px) ==")
def same_baseline(path, ymax=600):
    t = raw(path)
    els = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"( font-weight="700")?[^>]*?( text-anchor="(\w+)")?>([^<]*)</text>', t):
        x, y, fam, size = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4))
        bold = m.group(5) is not None
        anchor = m.group(7) or "start"
        s = m.group(8)
        kind = "serif" if "Serif" in fam else "sans"
        if "Unifraktur" in fam:
            continue
        w = text_w(s, kind, bold, size)
        if anchor == "middle":
            x0, x1 = x - w / 2, x + w / 2
        elif anchor == "end":
            x0, x1 = x - w, x
        else:
            x0, x1 = x, x + w
        els.append((y, x0, x1, s))
    flags = 0
    for y in sorted(set(e[0] for e in els)):
        if y > ymax:
            continue
        row = sorted([e for e in els if e[0] == y], key=lambda e: e[1])
        for a, b in zip(row, row[1:]):
            gap = b[1] - a[2]
            if gap < 5:
                print(f"  FLAG y={y} gap={gap:.1f} {a[3][:30]!r} vs {b[3][:30]!r}")
                flags += 1
    print(f"  {path.split('/')[-2]}: {flags} flags (y<={ymax})")
same_baseline(f"{ED}/p1-pervaya.svg")
same_baseline(f"{CORE}/p1-pervaya.svg")

print("== 11. PDFs + cards ==")
from pypdf import PdfReader
import glob as _g
for f in ["Lucerna-VOL2-IT.pdf", "Lucerna-VOL2-IT-web.pdf"]:
    p = os.path.expanduser(f"~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-it/{f}")
    r = PdfReader(p)
    print(f"  {f}: {os.path.getsize(p)} bytes, {len(r.pages)} pages")
from PIL import Image
for f in sorted(_g.glob(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-it/cards/*.png"))):
    im = Image.open(f)
    print(f"  {os.path.basename(f)}: {im.size}")
