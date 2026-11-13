# -*- coding: utf-8 -*-
"""Verification for W47 DE x IT. REG stats via a one-process runpy run
(same as run.py); SVGs re-hashed to prove determinism. No content-module
imports outside the build dir (tools/README lesson 11)."""
import os, re, sys, glob, hashlib
from datetime import date
BUILD = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-de-it")
sys.path.insert(0, BUILD)
ED = BUILD
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

# SOP 1.1 style audit (coordinator 2026-11-10): paper/badges/palette + no old style
import svglib
style_ok = (
    svglib.PAPER == "#fbfaf6" and svglib.INK == "#302c28" and svglib.OLIVE == "#46581f"
    and svglib.CLOTH == "#37402f" and svglib.GOOSE == "#f6e08e" and svglib.ONCLOTH == "#f4efe1"
    and svglib.BOX == "#f0eee5" and svglib.LINE == "#d8d2c4" and svglib.GREY == "#6f675d"
    and bslib4.LV_COLOR == {"A2": "#5c6e30", "B1": "#46581f", "B2": "#37402f"}
    and bslib4.MX == 88 and bslib4.CONTENT_BOTTOM == 2560)
src_all = ""
for _f in ["bslib4.py", "svglib.py", "content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    src_all += open(os.path.join(BUILD, _f), encoding="utf-8").read()
old_style = [h for h in ["#f7f1e2", "#c9a227", "#d4af37", "#8b6914"] if h in src_all.lower()]
print("SOP 1.1 style audit (paper/badges/palette/margins):", style_ok,
      "| old-style hexes found:", old_style)

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
    "Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln.",
    "Es geht ums Viertelfinale der Nations League.",
    "Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag.",
    "Die Märkte beginnen fast zwei Wochen früher.",
    "Hinter jedem Türchen wartet eine kleine Überraschung.",
    "Der FC Bayern gewann in Mainz mit 2:1.",
    "Die stille Woche ist der Übergang: vom November in den Advent.",
    "Am Sonntag ist es still im Land.",
]
print("P7 verbatim check (expect exactly 2 each):")
ok = True
for ph in phrases:
    c = joined.count(norm(ph))
    print(f"  {c}x :: {ph[:60]}")
    ok = ok and (c == 2)
print("verbatim OK:", ok)

for bad in ["桥接", "Le Lucerna", "The Lucerna", "VOL.3", "VOL.2", "Geisterspiel",
            "Karneval", "Volkstrauertag", "NFL", "American Football", "11.11", "Tankrabatt", "14,04",
            "Hart aber fair", "Klassiker", "Allerheiligen", "8,35", "ZEW"]:
    hits = [pg for pg, ts in all_texts.items() if any(bad in t for t in ts)]
    print(f"stale/forbidden {bad!r} on pages:", hits)

# headline length (SOP: LIMITS.headline other = 56, whitespace-stripped)
hl = "Die Bundesliga kehrt zurück — Bayern gegen Köln"
print("P1 headline stripped chars:", len(re.sub(r"\s", "", hl)), "(limit 56)")

# furniture: footer + page line on all 8 pages, badge slot on P1
foot = "Die Lucerna　SETTIMANALE TEDESCO VOL.4　Testo tedesco　Spiegazioni in italiano"
for pg, ts in sorted(all_texts.items()):
    print(pg, "footer:", sum(1 for t in ts if t == foot),
          "pageline:", [t for t in ts if re.match(r"Pagina \d di 8", t)])
raw1 = open(os.path.join(SVG, "p1-front.svg"), encoding="utf-8").read()
print("P1 masthead:", "Die Lucerna" in raw1,
      "subtitle slot:", "TESTO IN TEDESCO" in raw1,
      "week header:", "WOCHE VOM 16. BIS 22. NOVEMBER 2026" in raw1)

# P1 top-band same-baseline intervals (sizes as rendered: 17pt all three)
from svglib import text_w
from bslib4 import MX, RIGHT
checks = [
    ("VOL. 4　VIERTE AUSGABE", MX, "start", 17, "sans", True),
    ("WÖCHENTLICH AUF DEUTSCH　UN NUMERO A SETTIMANA　IL TEDESCO CHE LEGGONO I TEDESCHI", 975, "middle", 17, "sans", False),
    ("WOCHE VOM 16. BIS 22. NOVEMBER 2026", RIGHT, "end", 17, "sans", False),
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

# P6 chart: olive bars + label ink ends vs bar starts (bars at MX+470)
from bslib4 import OLIVE
raw6 = open(os.path.join(SVG, "p6-vertiefung.svg"), encoding="utf-8").read()
rects = [r for r in re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="' + re.escape(OLIVE) + r'"', raw6) if float(r[2]) > 100]
print("P6 olive bars (chart widths, expect 748/561/391):", [r[2] for r in rects])
labels = [("Bundesliga und Nations League", 22, True), ("Weihnachtsmärkte", 22, True),
          ("Stille Tage", 22, True)]
for lab, size, bold in labels:
    print(f"  label {lab!r} ink ends x={MX + text_w(lab, 'serif', bold, size):.0f} (bars start {MX + 470}; CN labels at {MX + 360})")

# MUSTER word count (whitespace split, as in W45)
raw8 = open(os.path.join(SVG, "p8-uebungen.svg"), encoding="utf-8").read()
m = re.search(r"MUSTER\s*Testo modello \((\d+) parole\)", raw8)
print("MUSTER label:", m.group(0) if m else "MISSING")
model = ("In dieser Woche bastle ich einen Adventskalender. Am Mittwoch öffne ich kein Türchen — das erste Türchen öffnet sich erst am 1. Dezember. Am Montag schaue ich mit meiner Familie die Nationalelf gegen die Niederlande. Am Freitag schaue ich Bayern gegen Köln im Fernsehen. Die Bayern führen die Tabelle an. Am Mittwoch ist Buß- und Bettag: In Bayern habe ich keinen Unterricht. Am Sonntag ist Totensonntag. Die Weihnachtsmärkte in Köln sind geschlossen. Ich lese ein Buch und bleibe zu Hause. Die Woche macht Spaß!")
print("MUSTER words (whitespace split):", len(model.split()))

# min font size per page in PDF points (SVG units x 0.75: page 1462.5pt / 1950 units)
for p in sorted(glob.glob(os.path.join(SVG, "*.svg"))):
    raw = open(p, encoding="utf-8").read()
    sizes = [float(x) for x in re.findall(r'font-size="([0-9.]+)"', raw)]
    print(os.path.basename(p), "min SVG font:", min(sizes), "-> PDF pt:", min(sizes) * 0.75)
print("P8 answers floor check (>= 9.75pt):",
      min(float(x) for x in re.findall(r'font-size="([0-9.]+)"', raw8)) * 0.75 >= 9.75)

# chart + date arithmetic spot checks
print("chart sum 44+33+23 =", 44 + 33 + 23)
print("18 Nov + 11 days =", date(2026, 11, 18).toordinal() + 11 == date(2026, 11, 29).toordinal())
print("15 Nov + 7 days =", date(2026, 11, 15).toordinal() + 7 == date(2026, 11, 22).toordinal())
print("16 Nov + 6 days =", date(2026, 11, 16).toordinal() + 6 == date(2026, 11, 22).toordinal())
