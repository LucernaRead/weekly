#!/usr/bin/env python3
"""Independent RUxKO W45 proof script 6: P7 phrases structure, golden x2 across issue,
model rendered, svglib Han, own orphan scan, same-baseline ink scan (venv PIL)."""
import re, collections
from pathlib import Path

BASE = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/files")
CORE = BASE/"weekly-report-w45-ru-core/svg"
ED = BASE/"weekly-report-w45-ru-ko/svg"
BUILD = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-ko-build")
PAGES = ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]

def elems(path):
    t = Path(path).read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', t):
        attrs = m.group(1); s = m.group(2)
        def g(k):
            mm = re.search(rf'{k}="([^"]*)"', attrs); return mm.group(1) if mm else ""
        out.append({"x": float(g("x") or 0), "y": float(g("y") or 0),
                    "size": float(g("font-size") or 0), "weight": g("font-weight"), "s": s})
    return out

print("== P7 phrases section (y 1840-2400) edition ==")
for e in elems(ED/"p7-yazyk.svg"):
    if e["y"] >= 1840:
        print(f"  x={e['x']} y={e['y']} size={e['size']} {e['s']!r}")

print("\n== Golden sentences: Russian phrase lines on P7, occurrences across whole issue ==")
# phrase items: Russian line(s) immediately above each (Страница N) tag line, same column
ed7 = elems(ED/"p7-yazyk.svg")
tags = [e for e in ed7 if "(Страница" in e["s"]]
print(f"  tag lines: {len(tags)}")
phrases = []
for t in tags:
    # Russian lines in same column (x within 30) with y in [t.y-90, t.y)
    cands = [e for e in ed7 if abs(e["x"] - t["x"]) < 40 and t["y"]-95 <= e["y"] < t["y"] and re.search(r"[\u0400-\u04FF]", e["s"])]
    rus = " ".join(e["s"] for e in sorted(cands, key=lambda e: e["y"]))
    phrases.append((rus, t["s"]))
    print(f"  TAG {t['s']!r} <- RU: {rus!r}")
# count each phrase's Russian core sentence across all edition pages (element-joined text)
def joined_text(d):
    parts = []
    for p in PAGES:
        for e in elems(d/f"{p}.svg"):
            parts.append(e["s"])
    return " ".join(parts)
ed_all = re.sub(r"\s+", " ", joined_text(ED))
co_all = re.sub(r"\s+", " ", joined_text(CORE))
for rus, tag in phrases:
    core_sent = rus.strip().strip("«»")
    # count occurrences of the sentence text (without guillemets) in joined text
    print(f"  phrase count ed={ed_all.count(core_sent)} core={co_all.count(core_sent)} :: {core_sent[:70]!r}")

print("\n== Model rendered on P8 (element reconstruction) ==")
ed8 = elems(ED/"p8-test.svg")
for e in ed8:
    if "Моя неделя" in e["s"] or "начинается в понедельник" in e["s"]:
        print(f"  x={e['x']} y={e['y']} size={e['size']} {e['s']!r}")
# find the H section: headers on P8
for e in ed8:
    if re.match(r"^[A-H] ·", e["s"]):
        print(f"  P8 header y={e['y']} {e['s']!r}")

print("\n== svglib Han chars (build copy) ==")
svg = (BUILD/"svglib.py").read_text(encoding="utf-8")
for m in re.finditer(r"[\u4E00-\u9FFF]", svg):
    ch = m.group(0); pos = m.start()
    print(f"  {ch!r} context: {svg[max(0,pos-100):pos+40]!r}")
print(f"  total Han in build svglib.py: {len(re.findall(r'[\\u4E00-\\u9FFF]', svg))}")
print(f"  total Han in all edition SVGs: {sum(len(re.findall(r'[\\u4E00-\\u9FFF]', (ED/f'{p}.svg').read_text(encoding='utf-8'))) for p in PAGES)}")

print("\n== OWN orphan scan ==")
PUNCT = set(".!?…)]»」")
for p in PAGES:
    lines = []
    for m in re.finditer(r'<text[^>]*x="([\d.]+)"[^>]*y="([\d.]+)"[^>]*font-size="([\d.]+)"[^>]*>([^<]*)</text>', (ED/f"{p}.svg").read_text(encoding="utf-8")):
        lines.append((float(m.group(1)), float(m.group(2)), float(m.group(3)), m.group(4)))
    flags = []
    for x, y, sz, s in lines:
        st = s.strip()
        if not st: continue
        toks = st.split()
        if toks and all(ch in PUNCT for ch in toks[-1]): flags.append(f"END-PUNCT-ONLY y={y} {s!r}")
        if st[0] in PUNCT: flags.append(f"START-PUNCT y={y} {s!r}")
    shorts = [(y, s) for x, y, sz, s in lines if 0 < len(s.strip()) <= 3]
    print(f"  {p}: flags={flags} short_lines={shorts}")
