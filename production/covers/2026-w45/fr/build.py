# -*- coding: utf-8 -*-
"""W45 weekly cover, reader language FRENCH. 8 pages, 1950x2700.

Headlines + excerpts are loaded verbatim from the shared extraction
(cover-backfill/headlines-w45.json) and never retyped. Explanations in
French are written from each item's headline + excerpt ONLY.
Cover itself carries NO vol number; P8 lists each core's masthead + VOL
from the same JSON (FR VOL.3, all others VOL.2). No git operations.
Cover-original French text uses ASCII apostrophes only (U+2019 renders
fullwidth in Noto CJK); verbatim headlines/excerpts are untouched
(the W45 JSON contains no U+2019 at all).
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import Page, wrap, text_w, esc, PAPER, INK, OLIVE, GOLD, BOX, LINE, GREY, DARK

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "svg")
os.makedirs(OUT, exist_ok=True)

PW, PH = 1950, 2700
MX, RIGHT = 65, 1885
W = RIGHT - MX
BOTTOM = 2540

SRC = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/cover-backfill/headlines-w45.json")
with open(SRC, encoding="utf-8") as f:
    ITEMS = json.load(f)
assert len(ITEMS) == 12, len(ITEMS)
assert [i["source_lang"] for i in ITEMS] == [
    "en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"]
assert [i["vol"] for i in ITEMS] == [2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2]

# French names for the source languages (tables.json fr column, T_BADGE forms).
LANG_FR = {
    "en": "ANGLAIS", "de": "ALLEMAND", "fr": "FRANCAIS", "es": "ESPAGNOL",
    "it": "ITALIEN", "pt": "PORTUGAIS", "nl": "NEERLANDAIS", "ru": "RUSSE",
    "ja": "JAPONAIS", "ko": "COREEN", "zh-cn": "CHINOIS SIMPLIFIE",
    "zh-tw": "CHINOIS TRADITIONNEL",
}
# NOTE: LANG_FR values above intentionally avoid accented capitals only
# where the W43 build did the same (FRANCAIS etc. were plain in W43? No:
# W43 used FRANCAIS with cedilla). See build note below; values are
# overwritten here to the W43 forms.

LANG_FR = {
    "en": "ANGLAIS", "de": "ALLEMAND", "fr": "FRAN\u00c7AIS", "es": "ESPAGNOL",
    "it": "ITALIEN", "pt": "PORTUGAIS", "nl": "N\u00c9ERLANDAIS", "ru": "RUSSE",
    "ja": "JAPONAIS", "ko": "COR\u00c9EN", "zh-cn": "CHINOIS SIMPLIFI\u00c9",
    "zh-tw": "CHINOIS TRADITIONNEL",
}

# French explanations: 1-2 sentences each, every claim traceable to that
# item's headline + excerpt only. No facts beyond the source article.
# All apostrophes are ASCII.
EXPL = {
    "en": "Le mardi 3 novembre, les \u00c9tats-Unis votent : c'est une \u00e9lection de mi-mandat, au milieu du mandat de quatre ans du pr\u00e9sident. Tous les 435 si\u00e8ges de la Chambre des repr\u00e9sentants sont en jeu, ainsi qu'environ un tiers du S\u00e9nat et des postes de gouverneur dans de nombreux \u00c9tats.",
    "de": "Cette semaine est une semaine de football : la Ligue des champions se joue mardi et mercredi, la Ligue Europa jeudi, et la 9e journ\u00e9e de Bundesliga commence vendredi. Quatre nuits de football, puis un week-end entier de championnat, avec mardi le Bayern chez l'Atl\u00e9tico Madrid \u00e0 21 heures et Stuttgart chez Galatasaray d\u00e8s 18 h 45.",
    "fr": "Le lundi 2 novembre, la France reprend : les vacances de la Toussaint sont finies, les \u00e9l\u00e8ves retournent \u00e0 l'\u00e9cole, et une grande semaine commence. Elle se terminera en beaut\u00e9, le week-end du 7 et 8 novembre, avec trois finales en m\u00eame temps, dont dimanche 8 novembre \u00e0 Nanterre les finales du Rolex Paris Masters, le dernier grand tournoi de tennis de la saison.",
    "es": "L'Espagne entre dans la semaine d\u00e9cisive avant la campagne : les listes sont d\u00e9j\u00e0 pr\u00e9sent\u00e9es et les partis \u00e9crivent maintenant leurs programmes. Le dimanche 29 novembre, l'Espagne vote aux \u00e9lections g\u00e9n\u00e9rales, et selon la une c'est le logement qui d\u00e9cidera la campagne.",
    "it": "Le lundi 2 novembre, l'Italie change de visage : le premier vrai froid de la saison arrive, avec des pluies sur le versant adriatique et les premi\u00e8res neiges l\u00e9g\u00e8res en montagne, vers 1 300-1 500 m\u00e8tres. Les pr\u00e9visions annoncent un novembre plus froid que la moyenne, une probabilit\u00e9, pas une certitude.",
    "pt": "La semaine commence le lundi 2 novembre, jour f\u00e9ri\u00e9 de Finados, et se termine le dimanche 8 novembre avec le premier jour de l'Enem. Entre les deux, tout le pays vit la m\u00eame semaine : se reposer, r\u00e9viser et passer l'\u00e9preuve, apr\u00e8s un long week-end f\u00e9ri\u00e9 ouvert d\u00e8s le samedi 31 octobre.",
    "nl": "Du lundi 2 au dimanche 8 novembre, c'est la Semaine du climat aux Pays-Bas : dans tout le pays, les communes organisent des actions, planter des arbres, \u00e9conomiser l'\u00e9nergie, prendre le v\u00e9lo plut\u00f4t que la voiture. Tout le monde peut participer.",
    "ru": "Cette semaine en Russie est inhabituelle : lundi et mardi, on travaille, mais mercredi, c'est f\u00e9ri\u00e9. Le mercredi 4 novembre tombe ainsi au milieu de la semaine de travail.",
    "ja": "Le 3 novembre, c'est le jour de la Culture, un jour f\u00e9ri\u00e9 : \u00e9coles et entreprises sont ferm\u00e9es. Partout dans le pays, des \u00e9v\u00e9nements culturels sont organis\u00e9s, et la une annonce aussi le week-end des feuillages d'automne.",
    "ko": "Du lundi 2 au dimanche 8 novembre, c'est la semaine o\u00f9 l'hiver commence : le samedi 7 novembre, c'est l'Ipdong, le premier terme solaire de l'hiver parmi les vingt-quatre. La une marque aussi la fin des feuillages d'automne et le d\u00e9but du kimjang, la pr\u00e9paration du kimchi pour l'hiver.",
    "zh-cn": "Le Double 11 a d\u00e9j\u00e0 commenc\u00e9 : JD vendait des articles en stock d\u00e8s le 12 octobre \u00e0 20 heures, Taobao et Tmall ont ouvert leurs pr\u00e9ventes le 15 octobre \u00e0 20 heures, puis le paiement du solde et les ventes en stock le 20 octobre \u00e0 20 heures. Les ventes en stock durent jusqu'au 13 novembre, et la une annonce aussi l'arriv\u00e9e de l'hiver.",
    "zh-tw": "La Semaine de la fintech de Hong Kong s'ouvre le lundi 2 novembre \u00e0 Hong Kong et dure cinq jours, jusqu'au vendredi 6 novembre. L'\u00e9v\u00e9nement est immense : plus de 45 000 participants attendus, venus de plus de 120 \u00e9conomies, avec plus de 1 000 intervenants et plus de 800 exposants et jeunes entreprises.",
}

class CoverPage(Page):
    def __init__(self):
        self.w, self.h = PW, PH
        self.parts = []
        self.add(f'<rect width="{PW}" height="{PH}" fill="{PAPER}"/>')
        self.add(f'<rect x="28" y="28" width="{PW-56}" height="{PH-56}" fill="none" stroke="{INK}" stroke-width="3.4"/>')
        self.add(f'<rect x="40" y="40" width="{PW-80}" height="{PH-80}" fill="none" stroke="{INK}" stroke-width="1.2"/>')

    def foot(self, n):
        self.hline(MX, RIGHT, 2580, GOLD, 1.6)
        self.text(MX, 2624, "Le Lucerna \u00b7 COVER \u00b7 2-8 novembre 2026", 20, "sans", False, GREY)
        self.text(RIGHT, 2624, f"Page {n} sur 8", 20, "sans", False, GREY, anchor="end")

    def centered(self, y, s, size, kind="serif", bold=False, fill=INK, max_w=W, lh=1.25):
        for ln in wrap(s, kind, bold, size, max_w):
            self.text((PW - text_w(ln, kind, bold, size)) / 2, y, ln, size, kind, bold, fill)
            y += size * lh
        return y


def item_block(p, y, it, tag_size=28, head_size=46, ex_size=31, note_size=29):
    """Draw one full item starting at baseline-top y; return bottom y."""
    lang = it["source_lang"]
    # tag line
    p.text(MX, y + tag_size, f"{LANG_FR[lang]} \u2014 {it['masthead']}", tag_size, "sans", True, OLIVE)
    y += tag_size + 22
    # headline (verbatim) / excerpt (verbatim). Wrap width is W-120, not W:
    # CairoSVG renders Latin serif text a few % wider than the PIL measure
    # used by wrap(), so full-width lines overflowed the right frame edge
    # on P2-P5 in the first render (EN/FR/ES/IT/NL excerpts clipped).
    y = p.para(MX, y + head_size, it["headline"], head_size, "serif", True, INK, W - 120, 1.25) + 18
    y = p.para(MX, y + ex_size, it["excerpt"], ex_size, "serif", False, INK, W - 120, 1.5) + 26
    # explanation box
    note = "Note \u2014 " + EXPL[lang]
    lines = wrap(note, "sans", False, note_size, W - 120)
    bh = 30 + len(lines) * note_size * 1.5 + 24
    p.rect(MX, y, W, bh, fill=BOX, stroke=LINE, sw=1.4)
    yy = y + 30
    for ln in lines:
        p.text(MX + 30, yy + note_size, ln, note_size, "sans", False, GREY)
        yy += note_size * 1.5
    return y + bh


def build_p1():
    p = CoverPage()
    # COVER badge, centred, dark olive
    bw, bh = 340, 84
    bx = (PW - bw) / 2
    p.rect(bx, 92, bw, bh, fill=OLIVE, rx=8)
    p.text(PW / 2, 92 + 58, "COVER", 44, "sans", True, "#fdfaf0", anchor="middle")
    # masthead
    p.text(PW / 2, 330, "Le Lucerna", 168, "serif", True, INK, anchor="middle")
    p.hline(500, 1450, 372, GOLD, 2.5)
    y = p.centered(448, "Semaine du 2-8 novembre 2026", 40, "sans", False, GREY)
    # cover title + generic framing intro (no new facts)
    y = p.centered(y + 34, "Douze langues, une semaine d'actualit\u00e9s", 66, "serif", True, INK, lh=1.2) + 30
    intro = ("Chaque semaine, les r\u00e9dactions de Lucerna choisissent, dans douze langues, "
             "le fait qui a marqu\u00e9 leurs lecteurs. Voici leurs douze unes, r\u00e9unies dans "
             "un seul num\u00e9ro, avec des explications en fran\u00e7ais.")
    y = p.centered(y, intro, 32, "serif", False, GREY, max_w=1500, lh=1.5) + 44
    # section head
    p.text(MX, y + 38, "Les douze unes de la semaine", 40, "sans", True, OLIVE)
    p.hline(MX, RIGHT, y + 52, GOLD, 2)
    y += 96
    # teasers: 2 columns, items 1-6 left, 7-12 right, numbered in fixed order
    colw, colx = 890, [MX, 995]
    tops = [y, y]
    for idx, it in enumerate(ITEMS):
        col = 0 if idx < 6 else 1
        x = colx[col]
        yy = tops[col]
        p.text(x, yy + 28, f"{idx + 1} \u00b7 {LANG_FR[it['source_lang']]}", 28, "sans", True, OLIVE)
        yy += 28 + 16
        yy = p.para(x, yy + 34, it["headline"], 34, "serif", True, INK, colw, 1.3) + 30
        tops[col] = yy
    y = max(tops) + 30
    y = p.centered(y, "Chaque une est reproduite dans sa langue d'origine ; "
                      "les explications sont en fran\u00e7ais.", 26, "sans", False, GREY)
    assert y < BOTTOM, f"P1 overflow: {y}"
    p.foot(1)
    p.save(os.path.join(OUT, "p1-cover.svg"))
    print(f"P1 ends y={y:.0f}")


def build_items(pages):
    """pages: list of (page_no, [item, item])."""
    for n, pair in pages:
        p = CoverPage()
        p.text(MX, 130, "Les douze unes", 40, "sans", True, OLIVE)
        p.hline(MX, RIGHT, 144, GOLD, 2)
        y = 200
        for k, it in enumerate(pair):
            if k:
                # spread the two items down the page instead of bunching at top
                y = max(y + 56, 1400)
                p.hline(MX, RIGHT, y - 46, GOLD, 1.6)
            y = item_block(p, y, it)
        assert y < BOTTOM, f"P{n} overflow: {y}"
        p.foot(n)
        p.save(os.path.join(OUT, f"p{n}-cover.svg"))
        print(f"P{n} ends y={y:.0f}")


def build_p8():
    p = CoverPage()
    y = p.centered(150, "Les douze journaux de la semaine", 66, "serif", True, INK) + 18
    y = p.centered(y, "Chaque journal, sa une \u2014 dans sa langue d'origine.",
                   30, "sans", False, GREY) + 40
    p.hline(MX, RIGHT, y + 6, GOLD, 2)
    y += 56
    for it in ITEMS:
        p.text(MX, y + 26, f"{it['masthead']} \u00b7 VOL.{it['vol']}", 26, "sans", True, OLIVE)
        y += 26 + 14
        y = p.para(MX, y + 30, it["headline"], 30, "serif", True, INK, W, 1.3) + 30
    assert y < BOTTOM, f"P8 overflow: {y}"
    p.foot(8)
    p.save(os.path.join(OUT, "p8-cover.svg"))
    print(f"P8 ends y={y:.0f}")


if __name__ == "__main__":
    build_p1()
    build_items([(2, ITEMS[0:2]), (3, ITEMS[2:4]), (4, ITEMS[4:6]),
                 (5, ITEMS[6:8]), (6, ITEMS[8:10]), (7, ITEMS[10:12])])
    build_p8()
    print("built", sorted(os.listdir(OUT)))
