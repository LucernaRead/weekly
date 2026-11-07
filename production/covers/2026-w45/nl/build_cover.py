# -*- coding: utf-8 -*-
"""W45 weekly cover, reader language DUTCH. 8 pages, 1950x2700.
Headlines/excerpts loaded verbatim from cover-backfill/headlines-w45.json
at build time (never retyped). Explanations in Dutch, traceable to
headline+excerpt only. Adapted from the W45 EN cover build pattern;
no content module from any core build dir is imported.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import Page, wrap, text_w, esc, INK, OLIVE, GOLD, PAPER, BOX, LINE, GREY

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "svg")
os.makedirs(OUT, exist_ok=True)

ITEMS = json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/cover-backfill/headlines-w45.json"))
assert [i["source_lang"] for i in ITEMS] == ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"], "fixed order changed!"

TABLES = json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/tools/tables.json"))
LANGS = TABLES["languages"]
VOL = {"fr": 3}  # all other 11 cores VOL.2 (per task)

FAMILY = {"en": "Noto Serif CJK SC", "de": "Noto Serif CJK SC", "fr": "Noto Serif CJK SC",
          "es": "Noto Serif CJK SC", "it": "Noto Serif CJK SC", "pt": "Noto Serif CJK SC",
          "nl": "Noto Serif CJK SC", "ru": "Noto Serif CJK SC",
          "ja": "Noto Serif CJK JP", "ko": "Noto Serif CJK KR",
          "zh-cn": "Noto Serif CJK SC", "zh-tw": "Noto Serif CJK TC"}
NLNAME = {"en": "Engels", "de": "Duits", "fr": "Frans", "es": "Spaans",
          "it": "Italiaans", "pt": "Portugees", "nl": "Nederlands",
          "ru": "Russisch", "ja": "Japans", "ko": "Koreaans",
          "zh-cn": "Chinees (vereenvoudigd)", "zh-tw": "Chinees (traditioneel)"}

EXPLAIN = {
 "en": "De Verenigde Staten stemmen bij tussentijdse verkiezingen: alle 435 zetels in het Huis van Afgevaardigden, ongeveer een derde van de Senaat en gouverneursposten in veel staten staan op het stembiljet.",
 "de": "Een week vol voetbal: Champions League op dinsdag en woensdag, Europa League op donderdag, en op vrijdag begint de 9e speeldag van de Bundesliga.",
 "fr": "Na de vakantie van Allerheiligen (Toussaint) gaan de leerlingen weer naar school, en de week eindigt met drie finales tegelijk in het weekend van 7 en 8 november, waaronder de finales van het Rolex Paris Masters in Nanterre op zondag 8 november.",
 "es": "De lijsten zijn al ingediend en de partijen schrijven nu hun programma's, in aanloop naar de algemene verkiezingen op zondag 29 november, waarbij huisvesting de campagne bepaalt.",
 "it": "Op maandag 2 november komt de eerste echte kou van het seizoen, met regen aan de Adriatische kant en lichte sneeuw in de bergen rond 1.300-1.500 meter, en november wordt naar verwachting kouder dan gemiddeld - een kans, geen zekerheid.",
 "pt": "De week loopt van de feestdag Finados op maandag 2 november tot de eerste dag van het Enem-examen op zondag 8 november: een week van rusten, herhalen en het examen zelf.",
 "nl": "Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland, met acties in het hele land - bomen planten, energie besparen, de fiets nemen in plaats van de auto - waar iedereen aan mee kan doen.",
 "ru": "Een ongewone week in Rusland: werken op maandag en dinsdag, en dan een vrije dag op woensdag 4 november, midden in de werkweek.",
 "ja": "Cultuurdag valt op dinsdag 3 november, een feestdag waarop scholen en bedrijven dicht zijn en er in het hele land culturele evenementen plaatsvinden.",
 "ko": "De week van maandag 2 tot en met zondag 8 november is de week waarin de winter begint: zaterdag 7 november is Ip-dong, de eerste van de 24 seizoensindelingen die bij de winter hoort.",
 "zh-cn": "De Double 11-verkoop is al begonnen en de aanbiedingen lopen door tot 13 november, terwijl ook de winter eraan komt.",
 "zh-tw": "Hong Kong FinTech Week x StartmeupHK 2026 opent op maandag 2 november in Hongkong en duurt vijf dagen tot vrijdag 6 november, met een hoofdconferentie en tentoonstelling plus meer dan 100 community-evenementen, en naar verwachting meer dan 45.000 deelnemers.",
}
assert set(EXPLAIN) == {i["source_lang"] for i in ITEMS}
# ASCII apostrophes only in cover-original text (no U+2019)
for _k, _v in EXPLAIN.items():
    assert "\u2019" not in _v, _k

W, H = 1950, 2700
MX, CW = 130, 1690
FOOT_Y = 2624

def header(p, label):
    p.text(975, 128, label, 30, "sans", False, GREY, anchor="middle")

def footer(p, num):
    p.hline(MX, MX + CW, 2570, LINE, 1.2)
    p.text(MX, FOOT_Y, "De Lucerna  ·  COVER  ·  2-8 november 2026", 28, "sans", False, GREY)
    p.text(MX + CW, FOOT_Y, num, 28, "sans", False, GREY, anchor="end")

def para(p, x, y, s, size, kind, bold, fill, max_w, lh, family=None):
    for ln in wrap(s, kind, bold, size, max_w):
        p.text(x, y, ln, size, kind, bold, fill, family=family)
        y += size * lh
    return y

def tag(lang):
    return (NLNAME[lang] + "  ·  " + LANGS[lang]["label"]).upper()

# ---------------- P1 ----------------
p = Page(W, H)
header(p, "WEEKCOVER  ·  2-8 NOVEMBER 2026")
p.text(975, 330, "De Lucerna", 168, "serif", True, INK, anchor="middle")
bw = text_w("C O V E R", "sans", True, 44) + 90
p.rect(975 - bw / 2, 385, bw, 78, fill=OLIVE, rx=10)
p.text(975, 440, "C O V E R", 44, "sans", True, PAPER, anchor="middle")
p.text(975, 560, "2-8 november 2026", 52, "serif", False, OLIVE, anchor="middle")
p.hline(375, 1575, 620, GOLD, 3)
p.text(975, 740, "Twaalf voorpagina's, een week", 84, "serif", True, INK, anchor="middle")
y = para(p, 220, 850, "Twaalf kranten, twaalf talen, een week in november: elke kop hieronder opent zijn eigen voorpagina, in zijn eigen taal, met een korte toelichting in het Nederlands over wat er staat en waarom het opvalt.", 46, "serif", False, GREY, 1510, 1.45)
y += 40
p.hline(MX, MX + CW, y, GOLD, 2)
y += 55
for it in ITEMS:
    lang = it["source_lang"]
    p.text(MX, y, tag(lang), 28, "sans", True, OLIVE)
    y += 44
    y = para(p, MX, y, it["headline"], 40, "serif", True, INK, CW, 1.28, family=FAMILY[lang])
    y += 10
    assert y < 2520, f"P1 overflow at {lang}: y={y}"
footer(p, "1")
p.save(os.path.join(OUT, "p1-cover.svg"))

# ---------------- P2-P7: two items per page ----------------
PAIRS = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
for pi, (a, b) in enumerate(PAIRS):
    p = Page(W, H)
    header(p, "DE LUCERNA  ·  COVER  ·  2-8 NOVEMBER 2026")
    y = 210
    for idx in (a, b):
        it = ITEMS[idx]
        lang = it["source_lang"]
        p.text(MX, y, tag(lang), 34, "sans", True, OLIVE)
        y += 74
        y = para(p, MX, y, it["headline"], 60, "serif", True, INK, CW, 1.28, family=FAMILY[lang])
        y += 30
        y = para(p, MX, y, it["excerpt"], 44, "serif", False, INK, CW, 1.5, family=FAMILY[lang])
        y += 34
        p.hline(MX, MX + 180, y, GOLD, 2.5)
        y += 48
        p.text(MX, y, "WAT DIT BETEKENT", 30, "sans", True, OLIVE)
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
p = Page(W, H)
header(p, "DE LUCERNA  ·  COVER  ·  2-8 NOVEMBER 2026")
p.text(975, 300, "De twaalf kranten van deze week", 88, "serif", True, INK, anchor="middle")
p.text(975, 390, "De twaalf kernkranten achter deze cover, in volgorde.", 44, "serif", False, GREY, anchor="middle")
p.hline(MX, MX + CW, 440, GOLD, 3)
y = 520
for it in ITEMS:
    lang = it["source_lang"]
    vol = VOL.get(lang, 2)
    p.text(MX, y, f"{it['masthead']}  ·  VOL.{vol}", 36, "sans", True, OLIVE)
    y += 50
    y = para(p, MX, y, it["headline"], 44, "serif", True, INK, CW, 1.32, family=FAMILY[lang])
    y += 40
    assert y < 2520, f"P8 overflow at {lang}: y={y}"
footer(p, "8")
p.save(os.path.join(OUT, "p8-cover.svg"))
print("OK: 8 SVGs in", OUT)
