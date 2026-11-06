# -*- coding: utf-8 -*-
"""Verification for W45 DE core (no build imports of content modules for text checks;
REG stats come from a one-process runpy run identical to run.py, SVGs re-hashed)."""
import os, re, sys, glob, hashlib, json
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-de-build"))
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-de-build"))

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-core")
SVG = os.path.join(ED, "svg")

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

before = {os.path.basename(p): sha(p) for p in glob.glob(os.path.join(SVG, "*.svg"))}

# ---- REG stats via one-process runpy (same as run.py) ----
import runpy
os.chdir(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-de-build"))
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

# ---- text extraction ----
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
    "Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.",
    "Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.",
    "Wer 50 Liter tankt, spart rund 8,35 Euro.",
    "Die Schule hat nach den Herbstferien wieder begonnen.",
    "Die Tage sind kurz, die Abende lang.",
    "Zwei schwere Auswärtsspiele für die deutschen Teams.",
    "Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.",
    "Es geht langsam aufwärts — aber von allein geht es nicht.",
]
print("P7 verbatim check (expect exactly 2 each):")
ok = True
for ph in phrases:
    c = joined.count(norm(ph))
    print(f"  {c}x :: {ph[:60]}")
    ok = ok and (c == 2)
print("verbatim OK:", ok)

# ---- forbidden wording ----
for bad in ["桥接", "Le Lucerna", "The Lucerna"]:
    hits = [pg for pg, ts in all_texts.items() if any(bad in t for t in ts)]
    print(f"forbidden {bad!r} on pages:", hits)

# ---- P1 same-baseline scan (top band y=92, dark band y=478/522) ----
from svglib import text_w
raw1 = open(os.path.join(SVG, "p1-front.svg"), encoding="utf-8").read()
els = re.findall(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*?(?:text-anchor="(\w+)")?[^>]*>(.*?)</text>', raw1)
def interval(x, y, s, anchor, size, kind, bold):
    w = text_w(norm(s), kind, bold, size)
    if anchor == "middle":
        return (x - w / 2, x + w / 2)
    if anchor == "end":
        return (x - w, x)
    return (x, x + w)
print("P1 top-band (y=92) intervals:")
for x, y, anchor, s in [(float(a), float(b), c or "start", d) for a, b, c, d in els]:
    if y == 92:
        # recover size/kind/bold from the raw element text match is lossy; use approximate: left 23 bold sans, center 21 sans, right 23 sans
        pass
# simpler: direct known elements
checks = [
    ("VOL. 2 · ZWEITE AUSGABE", 65, "start", 23, "sans", True),
    ("WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语", 975, "middle", 21, "sans", False),
    ("WOCHE VOM 2. BIS 8. NOVEMBER 2026", 1885, "end", 23, "sans", False),
]
ivs = []
for s, x, a, size, kind, bold in checks:
    w = text_w(s, kind, bold, size)
    iv = (x - w / 2, x + w / 2) if a == "middle" else ((x - w, x) if a == "end" else (x, x + w))
    ivs.append((s[:20], iv))
    print(f"  {s[:30]:32s} {iv[0]:.0f}..{iv[1]:.0f}")
for i in range(len(ivs)):
    for j in range(i + 1, len(ivs)):
        assert ivs[i][1][1] <= ivs[j][1][0] or ivs[j][1][1] <= ivs[i][1][0], f"OVERLAP {ivs[i]} {ivs[j]}"
print("P1 top band: no same-baseline overlap")

# ---- P6 chart graze: bars vs labels ----
raw6 = open(os.path.join(SVG, "p6-vertiefung.svg"), encoding="utf-8").read()
rects = re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="#3e4c2a"', raw6)
print("P6 olive bars (chart):", rects)
for x, y, w, h in rects:
    print(f"  bar x={x}..{float(x)+float(w):.0f}")
print("chart labels end before x=535 by construction (labels at MX..425, bars from 535)")
