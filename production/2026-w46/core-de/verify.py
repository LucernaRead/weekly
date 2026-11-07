# -*- coding: utf-8 -*-
"""Verification for W46 DE core. REG stats via a one-process runpy run
(same as run.py); SVGs re-hashed to prove determinism. No content-module
imports outside the build dir (tools/README lesson 11)."""
import os, re, sys, glob, hashlib
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
BUILD = os.path.join(GOAL, "hidden_files/weekly-report-w46-de-build")
sys.path.insert(0, BUILD)
ED = os.path.join(GOAL, "files/weekly-report-w46-de-core")
SVG = os.path.join(ED, "svg")

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

before = {os.path.basename(p): sha(p) for p in glob.glob(os.path.join(SVG, "*.svg"))}

import runpy
os.chdir(BUILD)
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
REG = bslib4.REG
from collections import Counter
bypage = Counter(e["page"] for e in REG)
bylevel = Counter(e["level"] for e in REG)
bytype = Counter(e["type"] for e in REG)
print("TOTAL:", len(REG))
print("by page:", dict(sorted(bypage.items())))
print("by level:", dict(sorted(bylevel.items())))
print("by type:", dict(sorted(bytype.items())))
nums = [e["n"] for e in REG]
print("numbering continuous 1..N:", nums == list(range(1, len(REG) + 1)))

after = {os.path.basename(p): sha(p) for p in glob.glob(os.path.join(SVG, "*.svg"))}
print("SVGs byte-identical after verify run:", before == after)

def texts_of(path):
    raw = open(path, encoding="utf-8").read()
    return re.findall(r"<text[^>]*>(.*?)</text>", raw)

all_texts = {}
for p in sorted(glob.glob(os.path.join(SVG, "*.svg"))):
    all_texts[os.path.basename(p)] = texts_of(p)
vol = sum(len(t) for ts in all_texts.values() for t in ts)
print("text volume (chars, no separators):", vol)

def norm(s):
    s = s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    return re.sub(r"\s+", " ", s).strip()

joined = norm(" ".join(norm(t) for ts in all_texts.values() for t in ts))
phrases = [
    "Die Bundesliga pausiert — aber die Nationalmannschaft spielt.",
    "Um 11.11 Uhr beginnt in Köln die neue Karnevalssession.",
    "Sein Gedenktag ist der 11. November.",
    "Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut.",
    "Der November ist dunkel, aber er ist nicht still: Er singt, leuchtet und feiert.",
    "Das Spiel ist ausverkauft, RTL überträgt live.",
    "Gedenken heißt hier: innehalten, erinnern — und für Frieden und Versöhnung einstehen.",
    "Am Sonntag ist es still im Land.",
]
print("P7 verbatim check (expect exactly 2 each):")
ok = True
for ph in phrases:
    c = joined.count(norm(ph))
    print(f"  {c}x :: {ph[:60]}")
    ok = ok and (c == 2)
print("verbatim OK:", ok)

for bad in ["桥接", "Le Lucerna", "The Lucerna", "VOL.2", "Tankrabatt", "14,04",
            "Hart aber fair", "Klassiker", "Allerheiligen", "8,35", "ZEW"]:
    hits = [pg for pg, ts in all_texts.items() if any(bad in t for t in ts)]
    print(f"stale/forbidden {bad!r} on pages:", hits)

# furniture: footer + page line on all 8 pages, badge slot on P1
foot = "Die Lucerna · 德语周报 VOL.3 · LUCERNA GERMAN WEEKLY"
for pg, ts in sorted(all_texts.items()):
    print(pg, "footer:", sum(1 for t in ts if t == foot),
          "pageline:", [t for t in ts if re.match(r"第 \d 版 / 共 8 版", t)])
raw1 = open(os.path.join(SVG, "p1-front.svg"), encoding="utf-8").read()
print("P1 masthead:", "Die Lucerna" in raw1,
      "subtitle slot:", "DIE WOCHENZEITUNG FÜR LERNENDE" in raw1,
      "week header:", "WOCHE VOM 9. BIS 15. NOVEMBER 2026" in raw1)

# P1 top-band same-baseline intervals
from svglib import text_w
checks = [
    ("VOL. 3 · DRITTE AUSGABE", 65, "start", 23, "sans", True),
    ("WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语", 975, "middle", 21, "sans", False),
    ("WOCHE VOM 9. BIS 15. NOVEMBER 2026", 1885, "end", 23, "sans", False),
]
ivs = []
for s, x, a, size, kind, bold in checks:
    w = text_w(s, kind, bold, size)
    iv = (x - w / 2, x + w / 2) if a == "middle" else ((x - w, x) if a == "end" else (x, x + w))
    ivs.append((s[:20], iv))
    print(f"  topband {s[:30]:32s} {iv[0]:.0f}..{iv[1]:.0f}")
for i in range(len(ivs)):
    for j in range(i + 1, len(ivs)):
        assert ivs[i][1][1] <= ivs[j][1][0] or ivs[j][1][1] <= ivs[i][1][0], f"OVERLAP {ivs[i]} {ivs[j]}"
print("P1 top band: no same-baseline overlap")

# P6 chart graze: label ink ends vs bar starts (bars from x=535 in code)
raw6 = open(os.path.join(SVG, "p6-vertiefung.svg"), encoding="utf-8").read()
rects = re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="#3e4c2a"', raw6)
print("P6 olive bars (chart):", rects)
labels = [("Nations League und NFL", 22, True), ("St. Martin und Karneval", 22, True),
          ("Volkstrauertag und Gedenken", 22, True)]
for lab, size, bold in labels:
    print(f"  label {lab!r} ink ends x={65 + text_w(lab, 'serif', bold, size):.0f} (bars start 535; CN labels at 425)")

# MUSTER word count (whitespace split, as in W45)
raw8 = open(os.path.join(SVG, "p8-uebungen.svg"), encoding="utf-8").read()
m = re.search(r"MUSTER · 范文（(\d+) Wörter）", raw8)
print("MUSTER label:", m.group(0) if m else "MISSING")
model = ("In dieser Woche bastle ich eine Laterne. Am Mittwoch singe ich mit meiner Klasse "
         "Martinslieder und gehe beim Laternenumzug mit. Am Freitag schaue ich mit meiner Familie "
         "Deutschland in Belgrad im Fernsehen. Das Spiel ist ein Geisterspiel — ohne Zuschauer. "
         "Am Sonntag schaue ich die NFL in München im Fernsehen. Die Lions spielen gegen die "
         "Patriots. Der Karneval beginnt um 11.11 Uhr in Köln. Am Sonntag esse ich Brezeln und "
         "trinke Apfelschorle. Am Montag gehe ich wieder in die Schule. Die Woche macht Spaß!")
print("MUSTER words (whitespace split):", len(model.split()))

# chart arithmetic + key arithmetic spot checks
print("chart sum 46+34+20 =", 46 + 34 + 20)
print("time arithmetic 11:11 + 4h19 = 15:30:", (11 * 60 + 11) + (4 * 60 + 19) == 15 * 60 + 30)
