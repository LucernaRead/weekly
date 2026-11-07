# -*- coding: utf-8 -*-
"""W43 weekly COVER for GERMAN readers (cover-w43-de).

Headlines + excerpts are read verbatim from
cover-backfill/headlines-w43.json — never retyped here.
All cover-original writing (title, intro, explanations, furniture)
is in German. The cover itself carries NO vol number (it is marked
COVER); VOL numbers appear ONLY on P8, where they belong to the
12 core papers being listed.
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
WEEK = "19.-25. Oktober 2026"

ITEMS = json.load(open(
    "/home/hatch/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/cover-backfill/headlines-w43.json", encoding="utf-8"))
assert [i["source_lang"] for i in ITEMS] == [
    "en", "de", "fr", "es", "it", "pt", "nl", "ru",
    "ja", "ko", "zh-cn", "zh-tw"], "fixed order violated"

LANG_DE = {
    "en": "ENGLISCH", "de": "DEUTSCH", "fr": "FRANZÖSISCH",
    "es": "SPANISCH", "it": "ITALIENISCH", "pt": "PORTUGIESISCH",
    "nl": "NIEDERLÄNDISCH", "ru": "RUSSISCH", "ja": "JAPANISCH",
    "ko": "KOREANISCH", "zh-cn": "CHINESISCH (VEREINFACHT)",
    "zh-tw": "CHINESISCH (TRADITIONELL)",
}

# German explanations: 1-2 sentences each, every claim traceable to
# that item's headline + excerpt ONLY (no facts beyond the source).
EXPL = {
    "en": ("In Amerika hat die Wahl schon begonnen: Am Montag, dem 19. Oktober, "
           "startete die vorzeitige Stimmabgabe in Texas sowie in Alaska, "
           "Arkansas, Connecticut und Colorado \u2014 obwohl der Wahltag selbst "
           "erst am 3. November ist. Die Schlagzeile nennt diese Woche deshalb "
           "die gr\u00f6\u00dfte Woche des Herbstes in Amerika."),
    "de": ("Deutschland stellt in der Nacht von Samstag auf Sonntag die Uhren "
           "zur\u00fcck: Um 3.00 Uhr wird die Uhr auf 2.00 Uhr gestellt, und die "
           "Sommerzeit endet. Die Schlagzeile verspricht au\u00dferdem Ferien in "
           "elf L\u00e4ndern \u2014 eine geschenkte Stunde also."),
    "fr": ("Die Pr\u00e4sidentschaftswahl in Frankreich findet erst 2027 statt, "
           "doch die Franzosen sprechen schon jetzt dar\u00fcber. In dieser Woche "
           "lautet die meistgesuchte Anfrage bei Google in Frankreich "
           "\u00absondage pr\u00e9sidentielle 2027\u00bb, und Tausende Menschen "
           "suchen diese Worte jeden Tag."),
    "es": ("In Spanien passiert an diesem Sonntag alles auf einmal: In der Nacht "
           "wird die Uhr um 03:00 Uhr auf 02:00 Uhr zur\u00fcckgestellt, sodass "
           "die Nacht 25 Stunden dauert und man eine Stunde l\u00e4nger "
           "schl\u00e4ft. Au\u00dferdem wird der Cl\u00e1sico gespielt."),
    "it": ("In Italien wird in der Nacht von Samstag, dem 24., auf Sonntag, den "
           "25. Oktober, die Uhr um 03:00 Uhr eine Stunde zur\u00fcckgestellt. "
           "Damit kehrt nach sieben Monaten Sommerzeit die Winterzeit "
           "zur\u00fcck, und die Nacht dauert eine Stunde l\u00e4nger."),
    "pt": ("In Brasilien wird am Sonntag, dem 25. Oktober, von 8 bis 17 Uhr "
           "(Bras\u00edlia-Zeit) der zweite Wahlgang abgehalten. Um die "
           "Pr\u00e4sidentschaft treten nur zwei Namen an: Lula (PT) und "
           "Fl\u00e1vio Bolsonaro (PL)."),
    "nl": ("In den Niederlanden ist viel los: Die Regionen Mitte und S\u00fcd "
           "haben die ganze Woche Herbstferien, vom 17. bis zum 25. Oktober, "
           "w\u00e4hrend im Norden die Schule am Montag wieder beginnt. Die "
           "Schlagzeile nennt au\u00dferdem Design, Dance und eine Stunde extra "
           "Schlaf."),
    "ru": ("In Russland k\u00f6nnte schon in dieser Woche der erste Schnee "
           "fallen. Die Wettervorhersage erwartet die ersten Schneeflocken am "
           "Mittwoch, Donnerstag oder Freitag, vom 21. bis zum 23. Oktober, bei "
           "Temperaturen um null Grad."),
    "ja": ("In Japan beginnt am Samstag, dem 24. Oktober, um 18:30 Uhr im "
           "Yokohama-Stadion die Japan Series. Es spielen die Yokohama DeNA "
           "BayStars gegen die Fukuoka SoftBank Hawks \u2014 ein Duell, das es "
           "seit zwei Jahren nicht mehr gegeben hat."),
    "ko": ("Der Taifun Nummer 30, \u00ab\ucc38\ud53c\u00bb, zieht nach Norden; sein "
           "Name stammt aus Laos und ist ein Blumenname. Die Wetterbeh\u00f6rde "
           "meldete am Morgen des 21., dass \u00ab\ucc38\ud53c\u00bb ein sehr "
           "starker Taifun sei."),
    "zh-cn": ("Das Einkaufsfestival \u00ab\u53cc11\u00bb beginnt in diesem Jahr "
              "fr\u00fch: JD verkaufte schon ab dem 12. Oktober um 20 Uhr Ware "
              "aus Lagerbestand, und am 20. Oktober um 20 Uhr folgte die "
              "\u00ab\u5f00\u95e8\u7ea2\u00bb-Aktion. Taobao und Tmall starteten "
              "am 15. Oktober um 20 Uhr mit dem Vorverkauf."),
    "zh-tw": ("Ein starker Taifun namens \u00ab\u8594\u7435\u00bb n\u00e4hert sich "
              "dem Meer \u00f6stlich Taiwans: Am Abend des 20. Oktober lag sein "
              "Zentrum etwa 1.390 Kilometer s\u00fcd\u00f6stlich von Kap "
              "Eluanbi, mit Windgeschwindigkeiten von bis zu 60 Metern pro "
              "Sekunde. Weil zus\u00e4tzlich der Nordostmonsun weht, f\u00e4llt "
              "der Regen durch den sogenannten \u00ab\u5171\u4f34\u6548\u61c9"
              "\u00bb noch st\u00e4rker und l\u00e4nger."),
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
        self.text(MX, 2624, "Die Lucerna \u00b7 COVER \u00b7 Woche "
                 + WEEK, 20, "sans", False, GREY)
        self.text(RIGHT, 2624, f"Seite {n} von 8", 20, "sans", False,
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
p.text(CX, 300, "Die Lucerna", 150, "serif", True, INK, anchor="middle")
p.text(CX, 372, WEEK, 34, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 412, GOLD, 2)
y = 500
y = p.para(CX, y, "Zw\u00f6lf Sprachen, zw\u00f6lf Schlagzeilen "
           "\u2014 eine Woche zum Lesen",
           58, "serif", True, INK, 1700, 1.3, anchor="middle") + 18
y = p.para(CX, y, "In dieser Ausgabe versammeln wir die Schlagzeilen der "
           "Woche aus zw\u00f6lf Sprachen \u2014 jeweils im Original und mit "
           "einer kurzen Erkl\u00e4rung auf Deutsch. Bl\u00e4ttern Sie durch "
           "und lesen Sie, was in dieser Woche Schlagzeilen macht.",
           34, "serif", False, GREY, 1600, 1.5, anchor="middle") + 34
p.text(MX, y, "DIE SCHLAGZEILEN DER WOCHE", 30, "sans", True, OLIVE)
p.hline(MX, RIGHT, y + 14, GOLD, 2)
y += 58
for it in ITEMS:
    p.text(MX, y, LANG_DE[it["source_lang"]], 26, "sans", True, OLIVE)
    y += 40
    y = p.para(MX, y, it["headline"], 34, "serif", True, INK, CW, 1.3) + 26
check(y, "P1 teasers")
p.foot(1)
p.save(os.path.join(OUT, "p1-cover.svg"))
print("P1 saved")

# ---------------- P2-P7: 2 items per page ----------------
def item_block(p, y, it):
    p.text(MX, y, LANG_DE[it["source_lang"]] + " \u00b7 " + it["masthead"],
           28, "sans", True, OLIVE)
    # 70 (not 44): tall CJK headline ink at 54pt otherwise touches the tag
    # line — caught by occlusion_audit TEXTX on P6/P7, fixed here.
    y += 70
    y = p.para(MX, y, it["headline"], 60, "serif", True, INK, CW, 1.28) + 10
    p.hline(MX, RIGHT, y + 8, GOLD, 2)
    # Rule must clear the excerpt's ink top entirely (CJK ink at 44pt
    # reaches ~40px above its baseline). 70px rule->baseline gap; the
    # previous 22px gap let the rule graze tall glyph tops (visible in
    # the P3 render although the audit's LINEX only fires for lines
    # painted AFTER the text they cross).
    y += 78
    y = p.para(MX, y, it["excerpt"], 44, "serif", False, INK, CW, 1.6) + 30
    # explanation box (measured height, no overlap by construction)
    expl = EXPL[it["source_lang"]]
    lines = wrap(expl, "serif", False, 38, CW - 72)
    box_h = 32 + 36 + 16 + len(lines) * 38 * 1.5 + 32
    p.rect(MX, y, CW, box_h, fill=BOX, stroke=LINE, sw=1.4)
    p.text(MX + 36, y + 32 + 26, "ERKL\u00c4RUNG AUF DEUTSCH", 26,
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
    p.band("Die Lucerna \u00b7 COVER", f"Seite {n} von 8")
    y = 240
    y = item_block(p, y, a)
    p.hline(MX, RIGHT, y + 40, LINE, 1.2)
    y += 170
    y = item_block(p, y, b)
    check(y, f"P{n} items")
    p.text(CX, 2480, "Alle zw\u00f6lf Schlagzeilen im \u00dcberblick: "
           "Seite 1 und Seite 8.", 24, "sans", False, GREY,
           anchor="middle")
    p.foot(n)
    p.save(os.path.join(OUT, f"p{n}-cover.svg"))
    print(f"P{n} saved")

# ---------------- P8 ----------------
p = CoverPage()
p.band("Die Lucerna \u00b7 COVER", "Seite 8 von 8")
y = 240
y = p.para(MX, y, "Alle zw\u00f6lf Kernzeitungen auf einen Blick",
           56, "serif", True, INK, CW, 1.3) + 14
y = p.para(MX, y, "Jede Zeile nennt die Kernzeitung mit ihrer Bandnummer "
           "und ihrer Schlagzeile im Original.",
           32, "serif", False, GREY, CW, 1.5) + 36
for it in ITEMS:
    p.text(MX, y, f'{it["masthead"]} \u00b7 VOL.{it["vol"]} \u2014 '
           + LANG_DE[it["source_lang"]], 26, "sans", True, OLIVE)
    y += 40
    y = p.para(MX, y, it["headline"], 38, "serif", True, INK, CW, 1.3) + 52
check(y, "P8 rows")
p.foot(8)
p.save(os.path.join(OUT, "p8-cover.svg"))
print("P8 saved")
print("ALL PAGES BUILT")
