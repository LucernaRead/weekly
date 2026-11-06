# -*- coding: utf-8 -*-
"""Verification for W46 DE x NL. One-process runpy re-run; SVGs re-hashed
for determinism. No content-module imports outside the build dir."""
import os, re, sys, glob, hashlib
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
BUILD = os.path.join(GOAL, "hidden_files/weekly-report-w46-de-nl-build")
sys.path.insert(0, BUILD)
ED = os.path.join(GOAL, "files/weekly-report-w46-de-nl")
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

# CJK leak scan: no CJK-range character may survive in the EN edition.
CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
for pg, ts in sorted(all_texts.items()):
    hits = [t for t in ts if CJK.search(t)]
    print(pg, "CJK texts:", len(hits), hits[:3])
for bad in ["VOL.2", "Tankrabatt", "14,04", "Hart aber fair", "Klassiker", "Allerheiligen"]:
    hits = [pg for pg, ts in all_texts.items() if any(bad in t for t in ts)]
    print(f"stale/forbidden {bad!r} on pages:", hits)

foot = 'Die Lucerna · DUITS WEEKBLAD VOL.3 · TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS'
for pg, ts in sorted(all_texts.items()):
    print(pg, "footer:", sum(1 for t in ts if t == foot),
          "pageline:", [t for t in ts if re.match(r"Pagina \d van 8", t)])
raw1 = open(os.path.join(SVG, "p1-front.svg"), encoding="utf-8").read()
print("P1 badge:", 'TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS' in raw1,
      "masthead:", "Die Lucerna" in raw1,
      "week header:", "WOCHE VOM 9. BIS 15. NOVEMBER 2026" in raw1)

from svglib import text_w
checks = [
    ("VOL. 3 · DRITTE AUSGABE", 65, "start", 23, "sans", True),
    ('WÖCHENTLICH AUF DEUTSCH · ELKE WEEK · HET DUITS DAT DE DUITSERS LEZEN', 975, "middle", 21, "sans", False),
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

raw6 = open(os.path.join(SVG, "p6-vertiefung.svg"), encoding="utf-8").read()
rects = re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="#3e4c2a"', raw6)
print("P6 olive bars (chart):", rects)
for lab in ['voetbal', 'feesten', 'herdenking']:
    print(f"  chart label {lab!r} ink ends x={425 + text_w(lab, 'serif', True, 22):.0f} (bars start 535)")

raw8 = open(os.path.join(SVG, "p8-uebungen.svg"), encoding="utf-8").read()
m = re.search(r"MUSTER · Voorbeeldtekst \((\d+) woorden\)", raw8)
print("MUSTER label:", m.group(0) if m else "MISSING")
print("P8 separators:", len(re.findall(r"— Pagina \d —", raw8)), "half-width paren keys present:", '(3e persoon enkelvoud)' in raw8)
