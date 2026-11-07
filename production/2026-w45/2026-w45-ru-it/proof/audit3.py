# -*- coding: utf-8 -*-
import re, os
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = os.path.join(GOAL, "files/weekly-report-w45-ru-core/svg")
ED = os.path.join(GOAL, "files/weekly-report-w45-ru-it/svg")

def elements(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"<text\s+([^>]*)>(.*?)</text>", s, re.S):
        attrs, inner = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()
        def a(n):
            mm = re.search(n + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else None
        out.append({"x": a("x"), "y": a("y"), "text": inner})
    return out

print("== P8 elements y>2350 (both editions) ==")
for label, d in [("core", CORE), ("ed", ED)]:
    print(f"--- {label}")
    for e in elements(f"{d}/p8-test.svg"):
        if e["y"] and float(e["y"]) > 2350:
            print(f"  x={e['x']} y={e['y']}: {e['text'][:130]!r}")
print("== P8 138 continuation line ==")
for label, d in [("core", CORE), ("ed", ED)]:
    els = elements(f"{d}/p8-test.svg")
    for i, e in enumerate(els):
        if e["text"].startswith("138."):
            print(f"  {label} 138 line: y={e['y']} {e['text']!r}")
            for j in range(i+1, min(i+4, len(els))):
                print(f"    next y={els[j]['y']}: {els[j]['text'][:100]!r}")
print("== P8 150 line ==")
for label, d in [("core", CORE), ("ed", ED)]:
    for e in elements(f"{d}/p8-test.svg"):
        if e["text"].startswith("150."):
            print(f"  {label}: x={e['x']} y={e['y']}: {e['text']!r}")

print("== GOLDEN SENTENCES from content7 source ==")
src = open(os.path.join(GOAL, "hidden_files/weekly-report-w45-ru-it-build/content7.py"), encoding="utf-8").read()
# find ФРАЗЫ section: print region
i = src.find("ФРАЗЫ")
print(src[i-200:i+2500])
