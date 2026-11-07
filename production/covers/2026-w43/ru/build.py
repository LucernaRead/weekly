# -*- coding: utf-8 -*-
"""W43 weekly COVER for RUSSIAN readers (cover-w43-ru).

Headlines + excerpts are read verbatim from
cover-backfill/headlines-w43.json — never retyped here.
All cover-original writing (title, intro, explanations, furniture)
is in Russian. The cover itself carries NO vol number (it is marked
COVER); VOL numbers appear ONLY on P8, where they belong to the
12 core papers being listed. Masthead is bare "Lucerna" (Russian
takes no article — tables.json ru entry: article null).
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import (Page, wrap, text_w, esc, INK, OLIVE, GOLD, PAPER,
                    BOX, LINE, GREY, DARK)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "svg")
os.makedirs(OUT, exist_ok=True)

PW, PH = 1950, 2700
MX, RIGHT = 65, 1885
CW = RIGHT - MX
CX = (MX + RIGHT) // 2
WEEK = "19–25 октября 2026"

ITEMS = json.load(open(
    "/home/hatch/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/cover-backfill/headlines-w43.json", encoding="utf-8"))
assert [i["source_lang"] for i in ITEMS] == [
    "en", "de", "fr", "es", "it", "pt", "nl", "ru",
    "ja", "ko", "zh-cn", "zh-tw"], "fixed order violated"

LANG_RU = {
    "en": "АНГЛИЙСКИЙ", "de": "НЕМЕЦКИЙ", "fr": "ФРАНЦУЗСКИЙ",
    "es": "ИСПАНСКИЙ", "it": "ИТАЛЬЯНСКИЙ", "pt": "ПОРТУГАЛЬСКИЙ",
    "nl": "НИДЕРЛАНДСКИЙ", "ru": "РУССКИЙ", "ja": "ЯПОНСКИЙ",
    "ko": "КОРЕЙСКИЙ", "zh-cn": "КИТАЙСКИЙ (УПРОЩЁННЫЙ)",
    "zh-tw": "КИТАЙСКИЙ (ТРАДИЦИОННЫЙ)",
}

# Russian explanations: 1-2 sentences each, every claim traceable to
# that item's headline + excerpt ONLY (no facts beyond the source).
# Source terms are kept verbatim in quotes (참피, 双11, 开门红, 薔琵,
# 共伴效應) rather than re-transliterated, except 鵝鑾鼻 glossed as
# мыс Элуаньби following the DE cover's Kap Eluanbi precedent.
EXPL = {
    "en": ("В Америке выборы уже начались: в понедельник 19 октября "
           "досрочное голосование открылось в Техасе, а также в Аляске, "
           "Арканзасе, Коннектикуте и Колорадо, — хотя сам день выборов "
           "будет только 3 ноября. Поэтому заголовок называет эту неделю "
           "самой большой неделей осени в Америке."),
    "de": ("В Германии в ночь с субботы на воскресенье переводят часы: "
           "в 3:00 стрелки переводят на 2:00, и летнее время заканчивается. "
           "Заголовок обещает также каникулы в одиннадцати странах — "
           "подаренный час."),
    "fr": ("Президентские выборы во Франции пройдут только в 2027 году, "
           "но французы уже говорят о них. На этой неделе главный "
           "поисковый запрос во Франции в Google — «sondage "
           "présidentielle 2027», и эти слова ищут тысячи людей каждый "
           "день."),
    "es": ("В Испании в это воскресенье всё происходит сразу: ночью часы "
           "переводят с 03:00 на 02:00, ночь длится 25 часов, и можно "
           "спать на час дольше. А ещё в этот день играют «Класико»."),
    "it": ("В Италии в ночь с субботы 24 на воскресенье 25 октября часы "
           "в 03:00 переводят на час назад. После семи месяцев летнего "
           "времени возвращается зимнее время, и ночь становится на час "
           "длиннее."),
    "pt": ("В Бразилии в воскресенье 25 октября с 8 до 17 часов (время "
           "Бразилиа) пройдёт второй тур выборов. За пост президента "
           "борются только два имени: Лула (PT) и Флавио Болсонаро (PL)."),
    "nl": ("В Нидерландах насыщенная неделя: в регионах Центр и Юг всю "
           "неделю осенние каникулы — с субботы 17 по воскресенье "
           "25 октября, а на Севере школа снова начинается в понедельник. "
           "Заголовок упоминает также дизайн, танцы и час лишнего сна."),
    "ru": ("Первый снег может выпасть уже на этой неделе. "
           "Синоптики ждут первые снежинки в среду, четверг или пятницу — "
           "с 21 по 23 октября, при температуре около нуля градусов."),
    "ja": ("В Японии в субботу 24 октября в 18:30 на стадионе в Йокогаме "
           "начинается Японская серия. Играют Yokohama DeNA BayStars "
           "против Fukuoka SoftBank Hawks — такое противостояние впервые "
           "за два года."),
    "ko": ("Тайфун № 30 «참피» движется на север; его имя предложено "
           "Лаосом и означает название цветка. Утром 21-го "
           "метеорологическое управление сообщило, что «참피» — очень "
           "сильный тайфун."),
    "zh-cn": ("Торговый фестиваль «双11» в этом году начался рано: JD "
              "начал продавать товары со склада уже 12 октября в 20:00, "
              "а 20 октября в 20:00 прошла акция «开门红». Taobao и "
              "Tmall начали предпродажу 15 октября в 20:00."),
    "zh-tw": ("Сильный тайфун «薔琵» приближается к морю к востоку от "
              "Тайваня: вечером 20 октября его центр был примерно в "
              "1 390 километрах к востоку-юго-востоку от мыса Элуаньби, при "
              "максимальной скорости ветра около 60 метров в секунду. "
              "Из-за северо-восточного муссона дожди по так называемому "
              "«共伴效應» будут сильнее и дольше."),
}


class CoverPage(Page):
    def __init__(self):
        self.w, self.h = PW, PH
        self.parts = []
        self.add(f'<rect width="{PW}" height="{PH}" fill="{PAPER}"/>')
        self.add(f'<rect x="28" y="28" width="{PW-56}" height="{PH-56}" '
                 f'fill="none" stroke="{INK}" stroke-width="3.4"/>')
        self.add(f'<rect x="40" y="40" width="{PW-80}" height="{PH-80}" '
                 f'fill="none" stroke="{INK}" stroke-width="1.2"/>')

    def band(self, left, right):
        self.rect(52, 52, PW - 104, 98, fill=DARK)
        self.text(78, 116, left, 36, "sans", True, "#f3edda")
        self.text(PW - 78, 116, right, 36, "serif", True, "#f3edda",
                  anchor="end")
        return 178

    def foot(self, n):
        self.hline(MX, RIGHT, 2580, GOLD, 1.6)
        self.text(MX, 2624, "Lucerna · COVER · Неделя "
                 + WEEK, 20, "sans", False, GREY)
        self.text(RIGHT, 2624, f"Страница {n} из 8", 20, "sans", False,
                  GREY, anchor="end")


def check(y, label):
    assert y <= 2540, f"OVERFLOW {label}: y={y}"
    print(f"  {label}: ends y={y}")
    return y


# ---------------- P1 ----------------
p = CoverPage()
bw = text_w("COVER", "sans", True, 30) + 70
p.rect(CX - bw / 2, 78, bw, 58, fill=OLIVE, rx=8)
p.text(CX, 118, "COVER", 30, "sans", True, "#fdfaf0", anchor="middle")
p.text(CX, 300, "Lucerna", 150, "serif", True, INK, anchor="middle")
p.text(CX, 372, WEEK, 34, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 412, GOLD, 2)
y = 500
y = p.para(CX, y, "Двенадцать языков, двенадцать заголовков "
           "— неделя чтения",
           58, "serif", True, INK, 1700, 1.3, anchor="middle") + 18
y = p.para(CX, y, "В этом выпуске мы собрали заголовки недели на "
           "двенадцати языках — каждый в оригинале и с кратким "
           "пояснением на русском. Листайте и читайте, о чём говорит "
           "мир на этой неделе.",
           34, "serif", False, GREY, 1600, 1.5, anchor="middle") + 34
p.text(MX, y, "ЗАГОЛОВКИ НЕДЕЛИ", 30, "sans", True, OLIVE)
p.hline(MX, RIGHT, y + 14, GOLD, 2)
y += 58
for it in ITEMS:
    p.text(MX, y, LANG_RU[it["source_lang"]], 26, "sans", True, OLIVE)
    y += 40
    y = p.para(MX, y, it["headline"], 34, "serif", True, INK, CW, 1.3) + 26
check(y, "P1 teasers")
p.foot(1)
p.save(os.path.join(OUT, "p1-cover.svg"))
print("P1 saved")

# ---------------- P2-P7: 2 items per page ----------------
def item_block(p, y, it):
    p.text(MX, y, LANG_RU[it["source_lang"]] + " · " + it["masthead"],
           28, "sans", True, OLIVE)
    # 70 (not 44): tall CJK headline ink at 54pt otherwise touches the tag
    # line — caught by occlusion_audit TEXTX on the DE cover P6/P7.
    y += 70
    y = p.para(MX, y, it["headline"], 60, "serif", True, INK, CW, 1.28) + 10
    p.hline(MX, RIGHT, y + 8, GOLD, 2)
    # Rule must clear the excerpt's ink top entirely (CJK ink at 44pt
    # reaches ~40px above its baseline). 70px rule->baseline gap; the
    # previous 22px gap let the rule graze tall glyph tops (DE cover P3).
    y += 78
    y = p.para(MX, y, it["excerpt"], 44, "serif", False, INK, CW, 1.6) + 30
    # explanation box (measured height, no overlap by construction)
    expl = EXPL[it["source_lang"]]
    lines = wrap(expl, "serif", False, 38, CW - 72)
    box_h = 32 + 36 + 16 + len(lines) * 38 * 1.5 + 32
    p.rect(MX, y, CW, box_h, fill=BOX, stroke=LINE, sw=1.4)
    p.text(MX + 36, y + 32 + 26, "ПОЯСНЕНИЕ НА РУССКОМ", 26,
           "sans", True, OLIVE)
    yy = y + 32 + 36 + 16
    for ln in lines:
        p.text(MX + 36, yy + 38, ln, 38, "serif", False, INK)
        yy += 38 * 1.5
    y += box_h
    return y

pairs = [(ITEMS[i], ITEMS[i + 1]) for i in range(0, 12, 2)]
for pi, (a, b) in enumerate(pairs):
    n = pi + 2
    p = CoverPage()
    p.band("Lucerna · COVER", f"Страница {n} из 8")
    y = 240
    y = item_block(p, y, a)
    p.hline(MX, RIGHT, y + 40, LINE, 1.2)
    y += 170
    y = item_block(p, y, b)
    check(y, f"P{n} items")
    p.text(CX, 2480, "Все двенадцать заголовков — обзор на страницах "
           "1 и 8.", 24, "sans", False, GREY,
           anchor="middle")
    p.foot(n)
    p.save(os.path.join(OUT, f"p{n}-cover.svg"))
    print(f"P{n} saved")

# ---------------- P8 ----------------
p = CoverPage()
p.band("Lucerna · COVER", "Страница 8 из 8")
y = 240
y = p.para(MX, y, "Все двенадцать центральных газет — одним взглядом",
           56, "serif", True, INK, CW, 1.3) + 14
y = p.para(MX, y, "Каждая строка называет центральную газету, её номер "
           "тома и её заголовок в оригинале.",
           32, "serif", False, GREY, CW, 1.5) + 36
for it in ITEMS:
    p.text(MX, y, f'{it["masthead"]} · VOL.{it["vol"]} — '
           + LANG_RU[it["source_lang"]], 26, "sans", True, OLIVE)
    y += 40
    y = p.para(MX, y, it["headline"], 38, "serif", True, INK, CW, 1.3) + 52
check(y, "P8 rows")
p.foot(8)
p.save(os.path.join(OUT, "p8-cover.svg"))
print("P8 saved")
print("ALL PAGES BUILT")
