# -*- coding: utf-8 -*-
"""W43 weekly COVER for DUTCH readers (cover-w43-nl).

Headlines + excerpts are read verbatim from
cover-backfill/headlines-w43.json — never retyped here.
All cover-original writing (title, intro, explanations, furniture)
is in Dutch. The cover itself carries NO vol number (it is marked
COVER); VOL numbers appear ONLY on P8, where they belong to the
12 core papers being listed.
Adapted from the proven cover-w43-de build (same geometry, same
gap fixes: tag-to-headline 70px, headline-rule-to-excerpt 78px).
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
WEEK = "19-25 oktober 2026"

ITEMS = json.load(open(
    "/home/hatch/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/cover-backfill/headlines-w43.json", encoding="utf-8"))
assert [i["source_lang"] for i in ITEMS] == [
    "en", "de", "fr", "es", "it", "pt", "nl", "ru",
    "ja", "ko", "zh-cn", "zh-tw"], "fixed order violated"

LANG_NL = {
    "en": "ENGELS", "de": "DUITS", "fr": "FRANS",
    "es": "SPAANS", "it": "ITALIAANS", "pt": "PORTUGEES",
    "nl": "NEDERLANDS", "ru": "RUSSISCH", "ja": "JAPANS",
    "ko": "KOREAANS", "zh-cn": "CHINEES (VEREENVOUDIGD)",
    "zh-tw": "CHINEES (TRADITIONEEL)",
}

# Dutch explanations: 1-2 sentences each, every claim traceable to
# that item's headline + excerpt ONLY (no facts beyond the source).
# Source terms are kept verbatim where a translation would invent
# facts (e.g. 「薔琵」, 「共伴效應」, 참피, 「开门红」).
EXPL = {
    "en": ("In Amerika is de verkiezing al begonnen: op maandag 19 oktober "
           "ging vervroegd stemmen van start in Texas, en ook in Alaska, "
           "Arkansas, Connecticut en Colorado — terwijl de verkiezingsdag "
           "zelf pas op dinsdag 3 november is. De kop noemt deze week "
           "daarom de grootste week van de herfst in Amerika."),
    "de": ("Duitsland zet in de nacht van zaterdag op zondag de klok terug: "
           "om 3.00 uur gaat de klok een uur terug, naar 2.00 uur, en "
           "eindigt de zomertijd. De kop belooft daarnaast vakantie in "
           "elf landen — een uur cadeau dus."),
    "fr": ("De Franse presidentsverkiezing is pas in 2027, maar de Fransen "
           "praten er nu al over. Deze week is de nummer één zoekopdracht "
           "in Frankrijk op Google: « sondage présidentielle 2027 », en "
           "duizenden mensen zoeken die woorden elke dag."),
    "es": ("In Spanje gebeurt deze zondag alles tegelijk: in de vroege "
           "ochtend gaat de klok om 03:00 uur terug naar 02:00 uur, zodat "
           "de nacht 25 uur duurt en men een uur langer slaapt. Bovendien "
           "wordt de Clásico gespeeld."),
    "it": ("In Italië gaat in de nacht van zaterdag 24 op zondag 25 oktober "
           "de klok om 03:00 uur een uur terug en wijst weer 02:00 uur "
           "aan. De nacht duurt een uur langer en na zeven maanden "
           "zomertijd keert de wintertijd terug."),
    "pt": ("In Brazilië gaan de Brazilianen op zondag 25 oktober, van 8 tot "
           "17 uur (Brasília-tijd), opnieuw naar de stembus voor de tweede "
           "ronde van de verkiezingen. Voor het presidentschap strijden "
           "nog maar twee namen: Lula (PT) en Flávio Bolsonaro (PL)."),
    "nl": ("In Nederland is het een volle week: de regio's Midden en Zuid "
           "hebben de hele week herfstvakantie, van zaterdag 17 tot en met "
           "zondag 25 oktober, terwijl in Noord de school op maandag weer "
           "begint. De kop noemt daarnaast design, dance en een uur extra "
           "slaap."),
    "ru": ("In Rusland kan de eerste sneeuw al deze week vallen. "
           "Weerkundigen verwachten de eerste sneeuwvlokken op woensdag, "
           "donderdag of vrijdag — 21 tot en met 23 oktober — bij "
           "temperaturen rond nul graden."),
    "ja": ("In Japan begint op zaterdag 24 oktober om 18.30 uur in het "
           "Yokohama-stadion de Japan Series. Het gaat tussen de Yokohama "
           "DeNA BayStars en de Fukuoka SoftBank Hawks — een confrontatie "
           "die er twee jaar niet is geweest."),
    "ko": ("Tyfoon nummer 30, « 참피 », trekt naar het noorden; de naam "
           "komt uit Laos en is de naam van een bloem. Het weerbureau zei "
           "op de ochtend van de 21e dat « 참피 » een zeer sterke tyfoon "
           "is."),
    "zh-cn": ("Het koopjesfestival « 双11 » begint dit jaar vroeg: JD begon "
              "al op 12 oktober om 20.00 uur met de verkoop van voorraad, "
              "en op 20 oktober om 20.00 uur volgde de « 开门红 »-actie. "
              "Taobao en Tmall begonnen op 15 oktober om 20.00 uur met de "
              "voorverkoop."),
    "zh-tw": ("Een sterke tyfoon, « 薔琵 », nadert de zee ten oosten van "
              "Taiwan: op de avond van 20 oktober lag het centrum ongeveer "
              "1.390 kilometer ten oost-zuidoosten van 鵝鑾鼻, met windsnelheden "
              "tot ongeveer 60 meter per seconde. Omdat ook de "
              "noordoostmoesson waait, valt de regen door het zogeheten "
              "« 共伴效應 » nog zwaarder en langer."),
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
        self.text(MX, 2624, "De Lucerna · COVER · Week "
                 + WEEK, 20, "sans", False, GREY)
        self.text(RIGHT, 2624, f"Pagina {n} van 8", 20, "sans", False,
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
p.text(CX, 300, "De Lucerna", 150, "serif", True, INK, anchor="middle")
p.text(CX, 372, WEEK, 34, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 412, GOLD, 2)
y = 500
y = p.para(CX, y, "Twaalf talen, twaalf krantenkoppen "
           "— één week om te lezen",
           58, "serif", True, INK, 1700, 1.3, anchor="middle") + 18
y = p.para(CX, y, "In deze uitgave verzamelen we de krantenkoppen van de "
           "week uit twaalf talen — telkens in het origineel en met een "
           "korte uitleg in het Nederlands. Blader door en lees wat er "
           "deze week de krantenkoppen haalt.",
           34, "serif", False, GREY, 1600, 1.5, anchor="middle") + 34
p.text(MX, y, "DE KRANTENKOPPEN VAN DE WEEK", 30, "sans", True, OLIVE)
p.hline(MX, RIGHT, y + 14, GOLD, 2)
y += 58
for it in ITEMS:
    p.text(MX, y, LANG_NL[it["source_lang"]], 26, "sans", True, OLIVE)
    y += 40
    y = p.para(MX, y, it["headline"], 34, "serif", True, INK, CW, 1.3) + 26
check(y, "P1 teasers")
p.foot(1)
p.save(os.path.join(OUT, "p1-cover.svg"))
print("P1 saved")

# ---------------- P2-P7: 2 items per page ----------------
def item_block(p, y, it):
    p.text(MX, y, LANG_NL[it["source_lang"]] + " · " + it["masthead"],
           28, "sans", True, OLIVE)
    # 70 (not 44): tall CJK headline ink at 60pt otherwise touches the tag
    # line — caught by occlusion_audit TEXTX on the DE cover's P6/P7.
    y += 70
    y = p.para(MX, y, it["headline"], 60, "serif", True, INK, CW, 1.28) + 10
    p.hline(MX, RIGHT, y + 8, GOLD, 2)
    # Rule must clear the excerpt's ink top entirely (CJK ink at 44pt
    # reaches ~40px above its baseline). 70px rule->baseline gap.
    y += 78
    y = p.para(MX, y, it["excerpt"], 44, "serif", False, INK, CW, 1.6) + 30
    # explanation box (measured height, no overlap by construction)
    expl = EXPL[it["source_lang"]]
    lines = wrap(expl, "serif", False, 38, CW - 72)
    box_h = 32 + 36 + 16 + len(lines) * 38 * 1.5 + 32
    p.rect(MX, y, CW, box_h, fill=BOX, stroke=LINE, sw=1.4)
    p.text(MX + 36, y + 32 + 26, "UITLEG IN HET NEDERLANDS", 26,
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
    p.band("De Lucerna · COVER", f"Pagina {n} van 8")
    y = 240
    y = item_block(p, y, a)
    p.hline(MX, RIGHT, y + 40, LINE, 1.2)
    y += 170
    y = item_block(p, y, b)
    check(y, f"P{n} items")
    p.text(CX, 2480, "Alle twaalf krantenkoppen in overzicht: "
           "pagina 1 en pagina 8.", 24, "sans", False, GREY,
           anchor="middle")
    p.foot(n)
    p.save(os.path.join(OUT, f"p{n}-cover.svg"))
    print(f"P{n} saved")

# ---------------- P8 ----------------
p = CoverPage()
p.band("De Lucerna · COVER", "Pagina 8 van 8")
y = 240
y = p.para(MX, y, "Alle twaalf kernkranten in één oogopslag",
           56, "serif", True, INK, CW, 1.3) + 14
y = p.para(MX, y, "Elke regel noemt de kernkrant met haar volumenummer "
           "en haar krantenkop in de originele taal.",
           32, "serif", False, GREY, CW, 1.5) + 36
for it in ITEMS:
    p.text(MX, y, f'{it["masthead"]} · VOL.{it["vol"]} — '
           + LANG_NL[it["source_lang"]], 26, "sans", True, OLIVE)
    y += 40
    y = p.para(MX, y, it["headline"], 38, "serif", True, INK, CW, 1.3) + 52
check(y, "P8 rows")
p.foot(8)
p.save(os.path.join(OUT, "p8-cover.svg"))
print("P8 saved")
print("ALL PAGES BUILT")
