# -*- coding: utf-8 -*-
"""RU x NL W45 builder self-checks (all read-only; never imports content modules).
Covers: Cyrillic token-multiset diff, golden sentences, gloss count by '.' split,
image payload hashes, Dutch orphan scan, same-baseline ink gaps, P6 chart check,
P7 letters-box geometry, furniture extraction, CJK count in rendered SVGs."""
import base64, hashlib, html, os, re, sys
from collections import Counter

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = os.path.join(BASE, "files/weekly-report-w45-ru-core/svg")
ED = os.path.join(BASE, "files/weekly-report-w45-ru-nl/svg")
BUILD = os.path.join(BASE, "hidden_files/weekly-report-w45-ru-nl-build")
sys.path.insert(0, BUILD)
from svglib import text_w

TEXT_RE = re.compile(r'<text([^>]*)>(.*?)</text>', re.S)
ATTR = re.compile(r'(\w[\w-]*)="([^"]*)"')
CYR = re.compile(r'[А-Яа-яЁё]+')
CJK = re.compile(r'[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]')

def texts(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for attrs, c in TEXT_RE.findall(s):
        d = dict(ATTR.findall(attrs))
        out.append((d, html.unescape(re.sub(r'<[^>]+>', '', c))))
    return out

def page_texts(d, fn):
    return [t for _, t in texts(os.path.join(d, fn))]

PAGES = ["p1-pervaya.svg", "p2-zhizn.svg", "p3-kultura.svg", "p4-sport.svg",
         "p5-molodezh.svg", "p6-razbor.svg", "p7-yazyk.svg", "p8-test.svg"]

print("== 1. Cyrillic token multiset diff (core vs edition) ==")
for fn in PAGES:
    a = Counter(CYR.findall(" ".join(page_texts(CORE, fn))))
    b = Counter(CYR.findall(" ".join(page_texts(ED, fn))))
    diff = {k: (a[k], b[k]) for k in set(a) | set(b) if a[k] != b[k]}
    print(f"  {fn}: core_tokens={sum(a.values())} ed_tokens={sum(b.values())} diff={diff}")

print("== 2. Golden sentences (Russian quotes from content7, bare counts) ==")
import ast as _ast
src = open(os.path.join(BUILD, "content7.py"), encoding="utf-8").read()
m = re.search(r'quotes = \[(.*?)\]\n', src, re.S)
quotes = _ast.literal_eval("[" + m.group(1) + "]")
joined_ed = " ".join(" ".join(page_texts(ED, fn)) for fn in PAGES)
joined_ed = re.sub(r'\s+', ' ', joined_ed)
joined_core = " ".join(" ".join(page_texts(CORE, fn)) for fn in PAGES)
joined_core = re.sub(r'\s+', ' ', joined_core)
for q, tr, pg in quotes:
    bare = q.strip("«»")
    print(f"  {pg}: ed={joined_ed.count(bare)} core={joined_core.count(bare)} :: {bare[:60]}")
    assert tr in joined_ed, f"missing NL translation: {tr}"
print("  all 8 NL translations present; page-tag sequence:", [pg for _, _, pg in quotes])

print("== 3. Gloss count by '·' split (source gloss() strings) ==")
def gloss_items(builddir):
    total, items = 0, []
    for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        s = open(os.path.join(builddir, fn), encoding="utf-8").read()
        for mm in re.finditer(r'\.gloss\("((?:[^"\\]|\\.)*)"\)', s):
            val = mm.group(1)
            parts = [p.strip() for p in val.split("·")]
            total += len(parts)
            items.extend(parts)
    return total, items
core_build = os.path.join(BASE, "hidden_files/weekly-report-w45-ru-build")
ct, citems = gloss_items(core_build)
nt, nitems = gloss_items(BUILD)
print(f"  core gloss items={ct} edition gloss items={nt}")
# every edition gloss item's Russian headword (leading Cyrillic run) must appear on some page
all_ed_text = joined_ed
missing = [it for it in nitems if not (CYR.findall(it) and CYR.findall(it)[0] in all_ed_text)]
print(f"  edition gloss items missing headword in render: {missing}")

print("== 4. Image payloads (per page, sha256 of image href data) ==")
IMG_RE = re.compile(r'<image[^>]*xlink:href="([^"]+)"|<image[^>]*href="([^"]+)"')
for fn in PAGES:
    def imgs(d):
        s = open(os.path.join(d, fn), encoding="utf-8").read()
        vals = [a or b for a, b in IMG_RE.findall(s)]
        return [hashlib.sha256(v.encode()).hexdigest()[:16] for v in vals]
    print(f"  {fn}: core={imgs(CORE)} ed={imgs(ED)} equal={imgs(CORE) == imgs(ED)}")

print("== 5. Dutch orphan scan (rendered text lines starting with closer punct) ==")
CLOSERS = set(".,;:!?)%»")
flags = []
for fn in PAGES:
    for d, t in texts(os.path.join(ED, fn)):
        s = t.strip()
        if s and s[0] in CLOSERS:
            flags.append((fn, s[:80]))
print(f"  orphan-start flags: {len(flags)} {flags}")

print("== 6. Same-baseline ink scan (PIL widths, gap < 5 units, same y) ==")
def ink_box(d, t):
    x = float(d.get("x", 0)); y = float(d.get("y", 0))
    size = float(d.get("font-size", 20)); bold = d.get("font-weight") == "700"
    fam = "serif" if "Serif" in d.get("font-family", "") else "sans"
    w = text_w(t, fam, bold, size)
    anchor = d.get("text-anchor", "start")
    if anchor == "middle":
        return (x - w / 2, x + w / 2, y)
    if anchor == "end":
        return (x - w, x, y)
    return (x, x + w, y)
sb_flags = []
for fn in PAGES:
    by_y = {}
    for d, t in texts(os.path.join(ED, fn)):
        if not t.strip():
            continue
        box = ink_box(d, t)
        by_y.setdefault(round(box[2], 1), []).append((box, t))
    for y, runs in by_y.items():
        runs.sort()
        for (b1, t1), (b2, t2) in zip(runs, runs[1:]):
            gap = b2[0] - b1[1]
            if gap < 5:
                sb_flags.append((fn, y, round(gap, 1), t1[:40], t2[:40]))
print(f"  same-baseline flags (<5): {len(sb_flags)}")
for f in sb_flags:
    print("   ", f)

print("== 7. P6 chart element check (text ink vs later-drawn rects) ==")
s = open(os.path.join(ED, "p6-razbor.svg"), encoding="utf-8").read()
# parse elements in order: rects and texts with geometry
elems = []
for mm in re.finditer(r'<(rect|text)([^>]*?)(?:/>|>(.*?)</text>)', s, re.S):
    kind, attrs, c = mm.group(1), mm.group(2), mm.group(3)
    d = dict(ATTR.findall(attrs))
    if kind == "rect":
        elems.append(("rect", float(d.get("x", 0)), float(d.get("y", 0)),
                      float(d.get("width", 0)), float(d.get("height", 0)), ""))
    else:
        t = html.unescape(re.sub(r'<[^>]+>', '', c or ""))
        if not t.strip():
            continue
        size = float(d.get("font-size", 20)); bold = d.get("font-weight") == "700"
        fam = "serif" if "Serif" in d.get("font-family", "") else "sans"
        w = text_w(t, fam, bold, size)
        x = float(d.get("x", 0)); y = float(d.get("y", 0))
        anchor = d.get("text-anchor", "start")
        x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
        elems.append(("text", x0, y - size, w, size, t))
overlaps = []
for i, e in enumerate(elems):
    if e[0] != "text":
        continue
    for r in elems[i + 1:]:
        if r[0] != "rect":
            continue
        ox = min(e[1] + e[3], r[1] + r[3]) - max(e[1], r[1])
        oy = min(e[2] + e[4], r[2] + r[4]) - max(e[2], r[2])
        if ox > 0 and oy > 0:
            overlaps.append((e[5][:50], round(ox, 1), round(oy, 1)))
print(f"  P6 text-vs-later-rect overlaps: {len(overlaps)} {overlaps[:10]}")

print("== 8. P7 letters box geometry + disclosure ==")
p7 = open(os.path.join(ED, "p7-yazyk.svg"), encoding="utf-8").read()
rects = [(float(d.get("x", 0)), float(d.get("y", 0)), float(d.get("width", 0)), float(d.get("height", 0)))
         for d in (dict(ATTR.findall(a)) for a in re.findall(r'<rect([^>]*)', p7))]
p7t = page_texts(ED, "p7-yazyk.svg")
print("  disclosure NL present:", any("Nog geen echte brieven" in t for t in p7t),
      "| example sig present:", any("пример от редакции" in t for t in p7t))
print("  phrases rule y=1756 expected; col3 bottom (build log) 1727.58")
print("  P7 rects in rightmost column (x=1451):", [r for r in rects if r[0] == 1451])

print("== 9. Furniture ==")
p1 = texts(os.path.join(ED, "p1-pervaya.svg"))
for d, t in p1:
    if t.startswith("TEKSTEN") or "ELKE WEEK" in t or t.startswith("Lucerna ·"):
        print("  P1:", d, repr(t))
for fn in PAGES:
    ft = [t for _, t in texts(os.path.join(ED, fn)) if t.startswith("Lucerna ·") or t.startswith("Pagina ")]
    print(f"  {fn} footer/page:", ft)
p8t = page_texts(ED, "p8-test.svg")
print("  P8 separators:", [t for t in p8t if t.startswith("— Pagina")])

print("== 10. Rendered CJK count (edition SVGs) ==")
for fn in PAGES:
    s = " ".join(page_texts(ED, fn))
    print(f"  {fn}: CJK chars={len(CJK.findall(s))}")
print("NOTE: svglib.py docstring Chinese is source-only, never rendered into SVGs.")
print("CHECKS DONE")
