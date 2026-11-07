#!/usr/bin/env python3
"""Independent RUxKO W45 proof script 5: P2 box bottom, golden sentences, model literal,
svglib Han docstring, own orphan scan."""
import re, collections
from pathlib import Path

BASE = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/files")
CORE = BASE/"weekly-report-w45-ru-core/svg"
ED = BASE/"weekly-report-w45-ru-ko/svg"
BUILD = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-ko-build")
CBUILD = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-build")

def raw(d, p): return (d/f"{p}.svg").read_text(encoding="utf-8")

print("== P2 rects with bottom 1155.5 (core vs edition) ==")
for label, d in (("core", CORE), ("edition", ED)):
    hits = []
    for m in re.finditer(r'<rect([^>]*)/>', raw(d, "p2-zhizn")):
        attrs = m.group(1)
        def g(k):
            mm = re.search(rf'{k}="([^"]*)"', attrs); return mm.group(1) if mm else ""
        try: x, y, w, h = float(g("x")), float(g("y")), float(g("width")), float(g("height"))
        except: continue
        if abs((y+h) - 1155.5) < 0.01: hits.append((x, y, w, h))
    print(f"  {label}: {hits}")

print("\n== Golden sentences: from content7.py string lists ==")
def long_ru_literals(path):
    import ast
    out = []
    tree = ast.parse(Path(path).read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            v = node.value
            if len(v) > 40 and re.search(r"[\u0400-\u04FF]", v) and "Страница" not in v:
                out.append(v)
    return out
ed_lits = long_ru_literals(BUILD/"content7.py")
co_lits = long_ru_literals(CBUILD/"content7.py")
print(f"  edition long-RU literals: {len(ed_lits)}, core: {len(co_lits)}")
ed7_text = re.sub(r"<[^>]+>", "", raw(ED, "p7-yazyk"))
ed7_text = re.sub(r"\s+", " ", ed7_text)
co7_text = re.sub(r"<[^>]+>", "", raw(CORE, "p7-yazyk"))
co7_text = re.sub(r"\s+", " ", co7_text)
for v in ed_lits:
    norm = re.sub(r"\s+", " ", v).strip()
    print(f"  ed-lit len={len(norm)} count_in_edP7={ed7_text.count(norm)} count_in_coreP7={co7_text.count(norm)} start={norm[:60]!r}")
print("  core-only literals not in edition build:")
for v in co_lits:
    if v not in ed_lits: print(f"    {v[:80]!r}")
print("  edition-only literals not in core build:")
for v in ed_lits:
    if v not in co_lits: print(f"    {v[:80]!r}")

print("\n== Model literal core vs edition build ==")
import ast
def model(path):
    tree = ast.parse(Path(path).read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and node.value.startswith("Моя неделя с праздником"):
            return node.value
    return None
em, cm = model(BUILD/"content8.py"), model(CBUILD/"content8.py")
print(f"  identical: {em == cm}, words ed={len(em.split()) if em else 0} core={len(cm.split()) if cm else 0}")
ed8 = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", raw(ED, "p8-test")))
co8 = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", raw(CORE, "p8-test")))
print(f"  model rendered in ed P8 (full, whitespace-normalized): {re.sub(chr(32)+'+', ' ', em).strip() in ed8 if em else False}")
print(f"  model rendered in core P8: {re.sub(chr(32)+'+', ' ', cm).strip() in co8 if cm else False}")
# partial: first 60 chars
print(f"  ed P8 contains model start: {em[:60] in ed8 if em else False}")

print("\n== svglib Han chars (build copy) ==")
svg = (BUILD/"svglib.py").read_text(encoding="utf-8")
han = [(m.start(), ch) for m in re.finditer(r"[\u4E00-\u9FFF]", svg)]
print(f"  Han chars in build svglib.py: {len(han)}")
for pos, ch in han:
    print(f"    pos {pos}: {ch!r} context: {svg[max(0,pos-90):pos+30]!r}")
ed_svg_raw = "".join(raw(ED, p) for p in ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"])
print(f"  Han chars in all edition SVGs combined: {len(re.findall(chr(0x4E00)+'-'+chr(0x9FFF), ed_svg_raw)) if False else len(re.findall(r'[\\u4E00-\\u9FFF]', ed_svg_raw))}")

print("\n== OWN orphan scan (all pages, rendered lines) ==")
PUNCT = set(".!?…)]»」")
for p in ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]:
    t = raw(ED, p)
    lines = []
    for m in re.finditer(r'<text[^>]*x="([\d.]+)"[^>]*y="([\d.]+)"[^>]*font-size="([\d.]+)"[^>]*>([^<]*)</text>', t):
        lines.append((float(m.group(1)), float(m.group(2)), float(m.group(3)), m.group(4)))
    flags = []
    for x, y, sz, s in lines:
        st = s.strip()
        if not st: continue
        toks = st.split()
        if toks and all(ch in PUNCT for ch in toks[-1]):
            flags.append(f"END-PUNCT-ONLY y={y} {s!r}")
        if st[0] in PUNCT:
            flags.append(f"START-PUNCT y={y} {s!r}")
        # lone short final line: last token is a lone particle/short frag (report, not flag)
    print(f"  {p}: start/end-punct flags={len(flags)}")
    for f in flags: print(f"    {f}")
    # short final lines (<=3 chars) for eyeball
    shorts = [(y, s) for x, y, sz, s in lines if 0 < len(s.strip()) <= 3]
    print(f"    short lines (<=3 chars): {shorts}")
