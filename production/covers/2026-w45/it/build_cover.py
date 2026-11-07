# -*- coding: utf-8 -*-
"""W45 weekly cover, reader language ITALIAN. 8 pages, 1950x2700.
Headlines/excerpts loaded verbatim from cover-backfill/headlines-w45.json
at build time (never retyped). Explanations in Italian, traceable to
headline+excerpt only. Cover-original text uses ASCII apostrophes only.
Adapted from the proven cover-w45-en-build (same layout, same svglib copy).
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

# Italian reader-language labels + native label from tables.json.
IT_NAME = {"en": "INGLESE", "de": "TEDESCO", "fr": "FRANCESE", "es": "SPAGNOLO",
           "it": "ITALIANO", "pt": "PORTOGHESE", "nl": "OLANDESE", "ru": "RUSSO",
           "ja": "GIAPPONESE", "ko": "COREANO", "zh-cn": "CINESE SEMPLIFICATO",
           "zh-tw": "CINESE TRADIZIONALE"}

EXPLAIN = {
 "en": "Negli Stati Uniti si vota in elezioni di medio termine: in palio ci sono tutti i 435 seggi della Camera, circa un terzo del Senato e i governatori di molti Stati.",
 "de": "Una settimana piena di calcio: Champions League martedì e mercoledì, Europa League giovedì e da venerdì la nona giornata di Bundesliga.",
 "fr": "In Francia la scuola ricomincia dopo le vacanze di Ognissanti e la settimana si chiude nel fine settimana del 7 e 8 novembre con tre finali in contemporanea, tra cui le finali del Rolex Paris Masters a Nanterre domenica 8 novembre.",
 "es": "Con le liste già presentate, i partiti ora scrivono i loro programmi in vista delle elezioni generali di domenica 29 novembre, una campagna in cui la casa decide.",
 "it": "Lunedì 2 novembre arriva il primo freddo vero della stagione, con piogge sul versante adriatico e la prima neve leggera in montagna; novembre potrebbe essere più freddo della media, ma si tratta di una probabilità, non di una certezza.",
 "pt": "La settimana va dalla festività di Finados di lunedì 2 novembre al primo giorno dell'Enem domenica 8 novembre: riposo, ripasso e prova per tutto il paese.",
 "nl": "Dal 2 all'8 novembre nei Paesi Bassi è la Settimana del Clima: i comuni di tutto il paese organizzano azioni come piantare alberi, risparmiare energia e andare in bicicletta invece che in auto, e tutti possono partecipare.",
 "ru": "Una settimana insolita in Russia: si lavora lunedì e martedì, poi mercoledì 4 novembre è giorno libero, proprio nel mezzo della settimana lavorativa.",
 "ja": "Il Giorno della Cultura cade martedì 3 novembre: è una festività nazionale, scuole e aziende chiudono e in tutto il paese si svolgono eventi culturali.",
 "ko": "La settimana dal 2 all'8 novembre segna l'arrivo dell'inverno: sabato 7 novembre è Ip-dong, la prima stagione solare dell'inverno tra le 24.",
 "zh-cn": "Il periodo di saldi del Doppio 11 è già iniziato, con merci in vendita da metà ottobre fino al 13 novembre, proprio mentre arriva l'inverno.",
 "zh-tw": "La Settimana FinTech di Hong Kong x StartmeupHK 2026 si apre lunedì 2 novembre e dura cinque giorni fino a venerdì 6 novembre, con conferenza ed esposizione principali, più oltre 100 eventi di comunità e oltre 45.000 partecipanti attesi.",
}
assert set(EXPLAIN) == {i["source_lang"] for i in ITEMS}
# No curly apostrophes anywhere in cover-original text.
for _k, _v in EXPLAIN.items():
    assert "\u2019" not in _v, _k

W, H = 1950, 2700
MX, CW = 130, 1690
FOOT_Y = 2624

def new_page():
    return Page(W, H)

def header(p, label):
    p.text(975, 128, label, 30, "sans", False, GREY, anchor="middle")

def footer(p, num):
    p.hline(MX, MX + CW, 2570, LINE, 1.2)
    p.text(MX, FOOT_Y, "La Lucerna  ·  COVER  ·  2-8 novembre 2026", 28, "sans", False, GREY)
    p.text(MX + CW, FOOT_Y, num, 28, "sans", False, GREY, anchor="end")

def para(p, x, y, s, size, kind, bold, fill, max_w, lh, family=None):
    for ln in wrap(s, kind, bold, size, max_w):
        p.text(x, y, ln, size, kind, bold, fill, family=family)
        y += size * lh
    return y

def tag_of(it):
    lang = it["source_lang"]
    return IT_NAME[lang] + "  ·  " + LANGS[lang]["label"]

# ---------------- P1 ----------------
p = new_page()
header(p, "COPERTINA SETTIMANALE  ·  2-8 NOVEMBRE 2026")
p.text(975, 330, "La Lucerna", 168, "serif", True, INK, anchor="middle")
bw = text_w("C O V E R", "sans", True, 44) + 90
p.rect(975 - bw / 2, 385, bw, 78, fill=OLIVE, rx=10)
p.text(975, 440, "C O V E R", 44, "sans", True, PAPER, anchor="middle")
p.text(975, 560, "2-8 novembre 2026", 52, "serif", False, OLIVE, anchor="middle")
p.hline(375, 1575, 620, GOLD, 3)
title = "Dodici prime pagine, una settimana"
assert text_w(title, "serif", True, 84) < 1690, "P1 title too wide"
p.text(975, 740, title, 84, "serif", True, INK, anchor="middle")
y = para(p, 220, 850, "Dodici giornali, dodici lingue, una settimana di novembre: ogni titolo qui sotto apre la sua prima pagina, nella sua lingua, con una breve nota in italiano su che cosa dice e perché merita attenzione.", 46, "serif", False, GREY, 1510, 1.45)
y += 40
p.hline(MX, MX + CW, y, GOLD, 2)
y += 55
for it in ITEMS:
    p.text(MX, y, tag_of(it).upper(), 28, "sans", True, OLIVE)
    y += 40
    y = para(p, MX, y, it["headline"], 40, "serif", True, INK, CW, 1.28, family=FAMILY[it["source_lang"]])
    y += 18
    assert y < 2520, f"P1 overflow at {it['source_lang']}: y={y}"
footer(p, "1")
p.save(os.path.join(OUT, "p1-cover.svg"))

# ---------------- P2-P7: two items per page ----------------
PAIRS = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
for pi, (a, b) in enumerate(PAIRS):
    p = new_page()
    header(p, "LA LUCERNA  ·  COVER  ·  2-8 NOVEMBRE 2026")
    y = 210
    for idx in (a, b):
        it = ITEMS[idx]
        lang = it["source_lang"]
        p.text(MX, y, tag_of(it).upper(), 34, "sans", True, OLIVE)
        y += 74
        y = para(p, MX, y, it["headline"], 60, "serif", True, INK, CW, 1.28, family=FAMILY[lang])
        y += 30
        y = para(p, MX, y, it["excerpt"], 44, "serif", False, INK, CW, 1.5, family=FAMILY[lang])
        y += 34
        p.hline(MX, MX + 180, y, GOLD, 2.5)
        y += 48
        p.text(MX, y, "SPIEGAZIONE", 30, "sans", True, OLIVE)
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
header(p, "LA LUCERNA  ·  COVER  ·  2-8 NOVEMBRE 2026")
p.text(975, 300, "I dodici giornali di questa settimana", 88, "serif", True, INK, anchor="middle")
p.text(975, 390, "I dodici giornali principali dietro questa copertina, in ordine.", 44, "serif", False, GREY, anchor="middle")
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
