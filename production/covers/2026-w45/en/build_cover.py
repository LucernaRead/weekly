# -*- coding: utf-8 -*-
"""W45 weekly cover, reader language ENGLISH. 8 pages, 1950x2700.
Headlines/excerpts copied verbatim from cover-backfill/headlines-w45.json.
Explanations in English, traceable to headline+excerpt only.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import Page, wrap, text_w, esc, INK, OLIVE, GOLD, PAPER, BOX, LINE, GREY

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "svg")
os.makedirs(OUT, exist_ok=True)

ITEMS = json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/cover-backfill/headlines-w45.json"))
assert [i["source_lang"] for i in ITEMS] == ["en","de","fr","es","it","pt","nl","ru","ja","ko","zh-cn","zh-tw"], "fixed order changed!"

TABLES = json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/tools/tables.json"))
LANGS = TABLES["languages"]
VOL = {"fr": 3}  # all other 11 cores VOL.2 (verified per task)

FAMILY = {"en": "Noto Serif CJK SC", "de": "Noto Serif CJK SC", "fr": "Noto Serif CJK SC",
          "es": "Noto Serif CJK SC", "it": "Noto Serif CJK SC", "pt": "Noto Serif CJK SC",
          "nl": "Noto Serif CJK SC", "ru": "Noto Serif CJK SC",
          "ja": "Noto Serif CJK JP", "ko": "Noto Serif CJK KR",
          "zh-cn": "Noto Serif CJK SC", "zh-tw": "Noto Serif CJK TC"}
SANSF = "Noto Sans CJK SC"

EXPLAIN = {
 "en": "The United States votes in a midterm election, with every House seat, about a third of Senate seats, and many governorships on the ballot.",
 "de": "A week packed with football: European matches on Tuesday, Wednesday and Thursday, then the Bundesliga's ninth matchday starts on Friday.",
 "fr": "School is back after the All Saints' holidays, and the week builds to three finals on the November 7-8 weekend, including the Rolex Paris Masters tennis finals at Nanterre on Sunday.",
 "es": "With candidate lists already filed, parties are now writing their programmes ahead of Spain's general election on Sunday, November 29, when housing is set to decide the campaign.",
 "it": "The season's first real cold arrives on Monday, November 2, with Adriatic rain and light mountain snow, and November is forecast to run colder than average, though that is a probability, not a certainty.",
 "pt": "The week runs from the Finados holiday on Monday, November 2, to the first day of the Enem exam on Sunday, November 8: a week of rest, revision and the exam itself.",
 "nl": "It is Climate Week in the Netherlands, November 2-8, with towns across the country organising tree-planting, energy-saving and cycling actions that anyone can join.",
 "ru": "An unusual week in Russia: work on Monday and Tuesday, then a day off on Wednesday, November 4, right in the middle of the working week.",
 "ja": "Culture Day falls on Tuesday, November 3, a public holiday when schools and workplaces close and cultural events take place across the country.",
 "ko": "The week of November 2-8 marks winter's arrival: Saturday, November 7, is Ip-dong, the first of the 24 solar terms belonging to winter.",
 "zh-cn": "The Double 11 sales period is already under way, with goods on sale from mid-October through November 13, just as winter approaches.",
 "zh-tw": "Hong Kong FinTech Week x StartmeupHK 2026 opens on Monday, November 2, running five days to Friday, November 6, with a main conference and exhibition plus more than 100 community events, and an expected 45,000-plus participants.",
}
assert set(EXPLAIN) == {i["source_lang"] for i in ITEMS}

W, H = 1950, 2700
MX, CW = 130, 1690  # content x, width (130..1820)
FOOT_Y = 2624

def new_page():
    return Page(W, H)

def header(p, label):
    p.text(975, 128, label, 30, "sans", False, GREY, anchor="middle")

def footer(p, num):
    p.hline(MX, MX + CW, 2570, LINE, 1.2)
    p.text(MX, FOOT_Y, "The Lucerna  ·  COVER  ·  November 2-8, 2026", 28, "sans", False, GREY)
    p.text(MX + CW, FOOT_Y, num, 28, "sans", False, GREY, anchor="end")

def para(p, x, y, s, size, kind, bold, fill, max_w, lh, family=None):
    for ln in wrap(s, kind, bold, size, max_w):
        p.text(x, y, ln, size, kind, bold, fill, family=family)
        y += size * lh
    return y

# ---------------- P1 ----------------
p = new_page()
header(p, "WEEKLY COVER  ·  NOVEMBER 2-8, 2026")
p.text(975, 330, "The Lucerna", 168, "serif", True, INK, anchor="middle")
# COVER badge (olive pill, cream letters)
bw = text_w("C O V E R", "sans", True, 44) + 90
p.rect(975 - bw / 2, 385, bw, 78, fill=OLIVE, rx=10)
p.text(975, 440, "C O V E R", 44, "sans", True, PAPER, anchor="middle")
p.text(975, 560, "November 2-8, 2026", 52, "serif", False, OLIVE, anchor="middle")
p.hline(375, 1575, 620, GOLD, 3)
p.text(975, 740, "Twelve Front Pages, One Week", 84, "serif", True, INK, anchor="middle")
y = para(p, 220, 850, "Twelve papers, twelve languages, one week in November: each headline below opens its own front page, in its own language, with a short note in English on what it says and why it catches the eye.", 46, "serif", False, GREY, 1510, 1.45)
# center the intro block: para() above is left-aligned at 220; acceptable, but
# re-measure: keep left-aligned for readability (matches core body style).
y += 40
p.hline(MX, MX + CW, y, GOLD, 2)
y += 55
for it in ITEMS:
    lang = it["source_lang"]
    tag = LANGS[lang]["name_en"] + "  ·  " + LANGS[lang]["label"]
    p.text(MX, y, tag.upper(), 28, "sans", True, OLIVE)
    y += 40
    y = para(p, MX, y, it["headline"], 40, "serif", True, INK, CW, 1.28, family=FAMILY[lang])
    y += 18
    assert y < 2520, f"P1 overflow at {lang}: y={y}"
footer(p, "1")
p.save(os.path.join(OUT, "p1-cover.svg"))

# ---------------- P2-P7: two items per page ----------------
PAIRS = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
for pi, (a, b) in enumerate(PAIRS):
    p = new_page()
    header(p, "THE LUCERNA  ·  COVER  ·  NOVEMBER 2-8, 2026")
    y = 210
    for idx in (a, b):
        it = ITEMS[idx]
        lang = it["source_lang"]
        tag = LANGS[lang]["name_en"] + "  ·  " + LANGS[lang]["label"]
        p.text(MX, y, tag.upper(), 34, "sans", True, OLIVE)
        y += 74
        y = para(p, MX, y, it["headline"], 60, "serif", True, INK, CW, 1.28, family=FAMILY[lang])
        y += 30
        y = para(p, MX, y, it["excerpt"], 44, "serif", False, INK, CW, 1.5, family=FAMILY[lang])
        y += 34
        p.hline(MX, MX + 180, y, GOLD, 2.5)
        y += 48
        p.text(MX, y, "WHAT THIS MEANS", 30, "sans", True, OLIVE)
        y += 46
        y = para(p, MX, y, EXPLAIN[lang], 44, "sans", False, GREY, CW, 1.5)
        y += 58
        if idx == a:
            p.hline(MX, MX + CW, y, LINE, 1.5)
            y += 62
        assert y < 2540, f"P{pi+2} overflow at {lang}: y={y}"
    footer(p, str(pi + 2))
    p.save(os.path.join(OUT, f"p{pi+2}-cover.svg"))

# ---------------- P8: twelve cores at a glance ----------------
p = new_page()
header(p, "THE LUCERNA  ·  COVER  ·  NOVEMBER 2-8, 2026")
p.text(975, 300, "This Week's Twelve Papers", 88, "serif", True, INK, anchor="middle")
p.text(975, 390, "The twelve core papers behind this cover, in order.", 44, "serif", False, GREY, anchor="middle")
p.hline(MX, MX + CW, 440, GOLD, 3)
y = 520
for it in ITEMS:
    lang = it["source_lang"]
    vol = VOL.get(lang, 2)
    mast = it["masthead"]
    p.text(MX, y, f"{mast}  ·  VOL.{vol}", 36, "sans", True, OLIVE)
    y += 50
    y = para(p, MX, y, it["headline"], 44, "serif", True, INK, CW, 1.32, family=FAMILY[lang])
    y += 40
    assert y < 2520, f"P8 overflow at {lang}: y={y}"
footer(p, "8")
p.save(os.path.join(OUT, "p8-cover.svg"))
print("OK: 8 SVGs in", OUT)
