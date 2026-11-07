#!/usr/bin/env python3
"""Independent RUxKO W45 proof script 4: numbering/chips core-vs-ed, P2 para, P3 gloss2,
golden sentences, KIT hashes, abstract, latin tokens, model words, orphan scan."""
import re, hashlib, collections
from pathlib import Path

BASE = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/files")
CORE = BASE/"weekly-report-w45-ru-core/svg"
ED = BASE/"weekly-report-w45-ru-ko/svg"
BUILD = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-ko-build")
CBUILD = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-build")
PAGES = ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]

def elems(path):
    t = Path(path).read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', t):
        attrs = m.group(1); s = m.group(2)
        def g(k):
            mm = re.search(rf'{k}="([^"]*)"', attrs); return mm.group(1) if mm else ""
        out.append({"x": float(g("x") or 0), "y": float(g("y") or 0),
                    "size": float(g("font-size") or 0), "s": s})
    return out

print("== Leading-number sets per page, core vs edition ==")
for p in PAGES:
    def lead(d):
        s = collections.Counter()
        for e in elems(d/f"{p}.svg"):
            m = re.match(r"^(\d+)\.", e["s"].strip())
            if m: s[int(m.group(1))] += 1
        return s
    c, e = lead(CORE), lead(ED)
    print(f"{p}: core_keys={len(c)} ed_keys={len(e)} core-only={sorted(set(c)-set(e))} ed-only={sorted(set(e)-set(c))} countdiffs={ {k:(c[k],e[k]) for k in sorted(set(c)&set(e)) if c[k]!=e[k]} }")

print("\n== Level chips core vs edition (exact A2/B1/B2, all sizes) ==")
for label, d in (("core", CORE), ("edition", ED)):
    chips = collections.Counter()
    for p in PAGES:
        for el in elems(d/f"{p}.svg"):
            if el["s"].strip() in ("A2","B1","B2"):
                chips[(el["s"].strip(), el["size"])] += 1
    print(f"  {label}: {dict(chips)} total={sum(chips.values())}")

print("\n== P2 reader-call column (x 1451-1885, y 1000-1250) edition ==")
for e in elems(ED/"p2-zhizn.svg"):
    if 1451 <= e["x"] <= 1885 and 1000 <= e["y"] <= 1250:
        print(f"  y={e['y']} size={e['size']} {e['s']!r}")
print("== P2 reader-call column core (same window) ==")
for e in elems(CORE/"p2-zhizn.svg"):
    if 1451 <= e["x"] <= 1885 and 1000 <= e["y"] <= 1250:
        print(f"  y={e['y']} size={e['size']} {e['s']!r}")

print("\n== P3 gloss continuation (y ~973) ==")
for e in elems(ED/"p3-kultura.svg"):
    if 900 <= e["y"] <= 1010 and e["x"] < 1100:
        print(f"  x={e['x']} y={e['y']} {e['s']!r}")

print("\n== P7 golden sentences: core quotes, edition counts ==")
core7 = elems(CORE/"p7-yazyk.svg")
ed7 = elems(ED/"p7-yazyk.svg")
# golden sentences: Russian quoted lines? Find core P7 lines that are full Russian sentences with « » or quotes
# Strategy: take core P7 text lines containing Cyrillic sentences longer than 20 chars, in the golden area.
# Instead: use KIT claim - 8 sentences; find repeated Russian sentences in edition P7 (count==2).
ed_text = [e["s"] for e in ed7]
cnt = collections.Counter(ed_text)
print("  edition P7 duplicated Russian lines (count==2, len>15, has Cyrillic):")
for s, n in cnt.items():
    if n == 2 and len(s) > 15 and re.search(r"[\u0400-\u04FF]", s):
        print(f"    x2 {s!r}")
print("  edition P7 page tags:")
for e in ed7:
    if "Страница" in e["s"]:
        print(f"    y={e['y']} {e['s']!r}")
print("  core P7 page tags:")
for e in core7:
    if "Страница" in e["s"]:
        print(f"    y={e['y']} {e['s']!r}")

print("\n== KIT hash verification ==")
kit = (BASE/"weekly-report-w45-ru-ko/WEEKLY-KIT.md").read_text(encoding="utf-8")
ok = True
for p in PAGES:
    h = hashlib.sha256((ED/f"{p}.svg").read_bytes()).hexdigest()
    present = h in kit
    print(f"  {p}: {h[:16]}... in KIT full-hash: {present}")
    ok = ok and present
from PIL import Image
for p in PAGES:
    im = Image.open(BASE/f"weekly-report-w45-ru-ko/cards/{p}.png")
    sz = (BASE/f"weekly-report-w45-ru-ko/cards/{p}.png").stat().st_size
    print(f"  card {p}: {im.size} bytes={sz}")
for f in ["Lucerna-VOL2-KO.pdf","Lucerna-VOL2-KO-web.pdf"]:
    fp = BASE/f"weekly-report-w45-ru-ko/{f}"
    print(f"  {f}: bytes={fp.stat().st_size} sha={hashlib.sha256(fp.read_bytes()).hexdigest()[:16]}...")

print("\n== ABSTRACT checks ==")
ab = (BASE/"weekly-report-w45-ru-ko/ABSTRACT.txt").read_text(encoding="utf-8")
print(f"  lines={ab.strip().splitlines()} nlines={len(ab.strip().splitlines())} has_ascii_quote={'\"' in ab}")
for kw in ["Lucerna","러시아어","11월 4일","11월 3일","11.11","14라운드","A2","B2","150"]:
    print(f"  contains {kw!r}: {kw in ab}")

print("\n== Latin-script tokens in edition (beyond furniture) ==")
lat = collections.Counter()
for p in PAGES:
    for e in elems(ED/f"{p}.svg"):
        for tok in re.findall(r"[A-Za-z][A-Za-z0-9.]*", e["s"]):
            lat[tok] += 1
print(f"  {dict(lat)}")

print("\n== Model 84 words: find in content8.py + rendered location ==")
src = (CBUILD/"content8.py").read_text(encoding="utf-8")
# search for a long Russian string literal; print candidates containing 'праздник' model-ish
import ast
tree = ast.parse((BUILD/"content8.py").read_text(encoding="utf-8"))
for node in ast.walk(tree):
    if isinstance(node, ast.Constant) and isinstance(node.value, str) and len(node.value) > 200 and re.search(r"[\u0400-\u04FF]", node.value):
        words = node.value.split()
        print(f"  long-RU literal words={len(words)} start={node.value[:80]!r}")
