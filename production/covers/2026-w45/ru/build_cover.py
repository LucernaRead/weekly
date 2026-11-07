# -*- coding: utf-8 -*-
"""W45 weekly cover, reader language RUSSIAN. 8 pages, 1950x2700.
Headlines/excerpts loaded verbatim from cover-backfill/headlines-w45.json
at build time, never retyped. Explanations in Russian, traceable to
headline+excerpt only. Cover itself carries NO vol number (COVER mark
instead); P8 lists each core paper's own VOL (FR VOL.3, others VOL.2).
Adapted from the W45 DE cover build (same layout constants, including
the 64 px tag->headline gap that cleared the occlusion audit there).
Cover-original text uses ASCII apostrophes only, never U+2019.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import Page, wrap, text_w, esc, INK, OLIVE, GOLD, PAPER, BOX, LINE, GREY

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "svg")
os.makedirs(OUT, exist_ok=True)

ITEMS = json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/cover-backfill/headlines-w45.json"))
assert [i["source_lang"] for i in ITEMS] == ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"], "fixed order changed!"
assert all(i["vol"] == (3 if i["source_lang"] == "fr" else 2) for i in ITEMS), "VOL mismatch vs task"

TABLES = json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/tools/tables.json"))
LANGS = TABLES["languages"]

# Russian-language names for the source languages.
RU_NAME = {"en": "Английский", "de": "Немецкий", "fr": "Французский",
           "es": "Испанский", "it": "Итальянский", "pt": "Португальский",
           "nl": "Нидерландский", "ru": "Русский", "ja": "Японский",
           "ko": "Корейский", "zh-cn": "Китайский (упрощённый)",
           "zh-tw": "Китайский (традиционный)"}
FAMILY = {"en": "Noto Serif CJK SC", "de": "Noto Serif CJK SC", "fr": "Noto Serif CJK SC",
          "es": "Noto Serif CJK SC", "it": "Noto Serif CJK SC", "pt": "Noto Serif CJK SC",
          "nl": "Noto Serif CJK SC", "ru": "Noto Serif CJK SC",
          "ja": "Noto Serif CJK JP", "ko": "Noto Serif CJK KR",
          "zh-cn": "Noto Serif CJK SC", "zh-tw": "Noto Serif CJK TC"}

# 1-2 sentence explanations in Russian. Every claim traceable to that
# item's headline + excerpt ONLY; no facts beyond the source article.
EXPLAIN = {
 "en": "В США проходят промежуточные выборы: разыгрываются все 435 мест в Палате представителей, около трети мест в Сенате и посты губернаторов во многих штатах.",
 "de": "Футбольная неделя: во вторник и в среду играет Лига чемпионов, в четверг — Лига Европы, а в пятницу начинается 9-й тур Бундеслиги; во вторник «Бавария» играет у «Атлетико», а «Штутгарт» — у «Галатасарая».",
 "fr": "После каникул ко Дню всех святых французские школьники возвращаются в школу, а неделя завершится тремя финалами в выходные 7–8 ноября, в том числе финалами Rolex Paris Masters в Нантере в воскресенье.",
 "es": "Списки уже поданы, партии пишут программы, а в воскресенье 29 ноября Испания голосует на всеобщих выборах; тема жилья, по заголовку, решает кампанию.",
 "it": "В понедельник 2 ноября в Италию приходит первое настоящее похолодание сезона: дожди на адриатическом побережье и первый лёгкий снег в горах на высоте около 1300–1500 метров; ноябрь обещает быть холоднее среднего — это вероятность, а не уверенность.",
 "pt": "Неделя идёт от праздничного дня Finados в понедельник 2 ноября до первого дня экзамена Enem в воскресенье 8 ноября: отдохнуть, повторить и сдать экзамен.",
 "nl": "Со 2 по 8 ноября в Нидерландах проходит Климатическая неделя: муниципалитеты по всей стране организуют акции — сажать деревья, экономить энергию, ездить на велосипеде вместо автомобиля; участвовать может каждый.",
 "ru": "Необычная неделя в России: в понедельник и во вторник люди работают, а в среду 4 ноября — выходной посреди рабочей недели.",
 "ja": "День культуры — 3 ноября, вторник, праздничный день: школы и компании отдыхают, а по всей стране проходят культурные мероприятия.",
 "ko": "Неделя со 2 по 8 ноября — начало зимы: суббота 7 ноября открывает зиму как первый из 24 сезонных периодов.",
 "zh-cn": "Распродажа «11.11» уже идёт: товары в наличии продаются до 13 ноября — а ещё наступает зима.",
 "zh-tw": "Неделя финансовых технологий в Гонконге открывается в понедельник 2 ноября в Гонконге и длится пять дней до пятницы 6 ноября: главная конференция и выставка, более 100 общественных мероприятий и ожидаемые более 45 000 участников.",
}
assert set(EXPLAIN) == {i["source_lang"] for i in ITEMS}

W, H = 1950, 2700
MX, CW = 130, 1690
FOOT_Y = 2624
WEEK = "2–8 ноября 2026 года"
WEEK_UP = "2–8 НОЯБРЯ 2026 ГОДА"

def new_page():
    return Page(W, H)

def header(p, label):
    p.text(975, 128, label, 30, "sans", False, GREY, anchor="middle")

def footer(p, num):
    p.hline(MX, MX + CW, 2570, LINE, 1.2)
    p.text(MX, FOOT_Y, "Lucerna  ·  COVER  ·  " + WEEK, 28, "sans", False, GREY)
    p.text(MX + CW, FOOT_Y, num, 28, "sans", False, GREY, anchor="end")

def para(p, x, y, s, size, kind, bold, fill, max_w, lh, family=None):
    for ln in wrap(s, kind, bold, size, max_w):
        p.text(x, y, ln, size, kind, bold, fill, family=family)
        y += size * lh
    return y

def tag_of(it):
    lang = it["source_lang"]
    return (RU_NAME[lang] + "  ·  " + LANGS[lang]["label"]).upper()

# ---------------- P1 ----------------
p = new_page()
header(p, "НЕДЕЛЬНАЯ ОБЛОЖКА  ·  " + WEEK_UP)
p.text(975, 330, "Lucerna", 168, "serif", True, INK, anchor="middle")
bw = text_w("C O V E R", "sans", True, 44) + 90
p.rect(975 - bw / 2, 385, bw, 78, fill=OLIVE, rx=10)
p.text(975, 440, "C O V E R", 44, "sans", True, PAPER, anchor="middle")
p.text(975, 560, WEEK, 52, "serif", False, OLIVE, anchor="middle")
p.hline(375, 1575, 620, GOLD, 3)
p.text(975, 740, "Двенадцать первых полос, одна неделя", 76, "serif", True, INK, anchor="middle")
y = para(p, 220, 850, "Двенадцать газет, двенадцать языков, одна ноябрьская неделя: каждый заголовок ниже открывает свою первую полосу — на её собственном языке, с коротким пояснением по-русски о том, что он говорит и почему привлекает внимание.", 46, "serif", False, GREY, 1510, 1.45)
y += 40
p.hline(MX, MX + CW, y, GOLD, 2)
y += 55
for it in ITEMS:
    p.text(MX, y, tag_of(it), 28, "sans", True, OLIVE)
    y += 38
    y = para(p, MX, y, it["headline"], 38, "serif", True, INK, CW, 1.28, family=FAMILY[it["source_lang"]])
    y += 14
    assert y < 2520, f"P1 overflow at {it['source_lang']}: y={y}"
footer(p, "1")
p.save(os.path.join(OUT, "p1-cover.svg"))

# ---------------- P2-P7: two items per page ----------------
PAIRS = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
for pi, (a, b) in enumerate(PAIRS):
    p = new_page()
    header(p, "LUCERNA  ·  COVER  ·  " + WEEK_UP)
    y = 210
    for idx in (a, b):
        it = ITEMS[idx]
        lang = it["source_lang"]
        p.text(MX, y, tag_of(it), 34, "sans", True, OLIVE)
        y += 64
        y = para(p, MX, y, it["headline"], 60, "serif", True, INK, CW, 1.28, family=FAMILY[lang])
        y += 30
        y = para(p, MX, y, it["excerpt"], 44, "serif", False, INK, CW, 1.5, family=FAMILY[lang])
        y += 34
        p.hline(MX, MX + 180, y, GOLD, 2.5)
        y += 48
        p.text(MX, y, "ЧТО ЭТО ЗНАЧИТ", 30, "sans", True, OLIVE)
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
header(p, "LUCERNA  ·  COVER  ·  " + WEEK_UP)
p.text(975, 300, "Двенадцать газет этой недели", 88, "serif", True, INK, anchor="middle")
p.text(975, 390, "Двенадцать основных газет, стоящих за этой обложкой, по порядку.", 44, "serif", False, GREY, anchor="middle")
p.hline(MX, MX + CW, 440, GOLD, 3)
y = 520
for it in ITEMS:
    lang = it["source_lang"]
    vol = it["vol"]
    p.text(MX, y, f"{it['masthead']}  ·  VOL.{vol}", 36, "sans", True, OLIVE)
    y += 50
    y = para(p, MX, y, it["headline"], 44, "serif", True, INK, CW, 1.32, family=FAMILY[lang])
    y += 40
    assert y < 2520, f"P8 overflow at {lang}: y={y}"
footer(p, "8")
p.save(os.path.join(OUT, "p8-cover.svg"))
print("OK: 8 SVGs in", OUT)
