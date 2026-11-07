# -*- coding: utf-8 -*-
"""W43 weekly cover, reader language FRENCH. 8 pages, 1950x2700.

Headlines + excerpts are loaded verbatim from the shared extraction
(cover-backfill/headlines-w43.json) and never retyped. Explanations in
French are written from each item's headline + excerpt ONLY.
Cover itself carries NO vol number; P8 lists each core's masthead + VOL
from the same JSON. No git operations in this build.
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
    "hidden_files/cover-backfill/headlines-w43.json")
with open(SRC, encoding="utf-8") as f:
    ITEMS = json.load(f)
assert len(ITEMS) == 12, len(ITEMS)
assert [i["source_lang"] for i in ITEMS] == [
    "en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"]

# French names for the source languages (tables.json fr column, T_BADGE forms).
LANG_FR = {
    "en": "ANGLAIS", "de": "ALLEMAND", "fr": "FRANÇAIS", "es": "ESPAGNOL",
    "it": "ITALIEN", "pt": "PORTUGAIS", "nl": "NÉERLANDAIS", "ru": "RUSSE",
    "ja": "JAPONAIS", "ko": "CORÉEN", "zh-cn": "CHINOIS SIMPLIFIÉ",
    "zh-tw": "CHINOIS TRADITIONNEL",
}

# French explanations: 1-2 sentences each, every claim traceable to that
# item's headline + excerpt only. No facts beyond the source article.
EXPL = {
    "en": "Le jour officiel de l'élection est le mardi 3 novembre, mais le vote a déjà commencé dans plusieurs États : le lundi 19 octobre, le vote anticipé a ouvert au Texas ainsi qu'en Alaska, en Arkansas, au Connecticut et au Colorado.",
    "de": "Dans la nuit de samedi à dimanche, l'Allemagne quitte l'heure d'été : à 3 heures, les horloges reculent à 2 heures, ce qui offre une heure de plus, pendant une semaine où onze pays sont en vacances.",
    "fr": "L'élection présidentielle n'aura lieu qu'en 2027, mais elle occupe déjà les Français : cette semaine, la recherche numéro un en France sur Google est « sondage présidentielle 2027 », cherchée chaque jour par des milliers de personnes.",
    "es": "Tout se joue dimanche en Espagne : la nuit dure 25 heures, car à 3 heures les horloges reviennent à 2 heures et l'on dort une heure de plus — le jour même du Clásico.",
    "it": "Dans la nuit du samedi 24 au dimanche 25 octobre, l'Italie revient à l'heure solaire : à 3 heures, l'horloge recule d'une heure et indique de nouveau 2 heures, après sept mois d'heure d'été, et la nuit dure une heure de plus.",
    "pt": "Le dimanche 25 octobre, de 8 heures à 17 heures (heure de Brasilia), les Brésiliens retournent aux urnes pour le second tour de l'élection présidentielle, qui oppose Lula (PT) à Flávio Bolsonaro (PL).",
    "nl": "La semaine est bien remplie aux Pays-Bas : les régions du Centre et du Sud passent toute la semaine en vacances d'automne, du samedi 17 au dimanche 25 octobre, tandis que le Nord, en vacances la semaine précédente, reprend l'école lundi.",
    "ru": "Les premiers flocons pourraient tomber dès cette semaine : les météorologues les attendent entre mercredi et vendredi, du 21 au 23 octobre, avec des températures proches de zéro degré.",
    "ja": "Le premier match des Japan Series se joue le samedi 24 octobre à 18 h 30 au stade de Yokohama, opposant les Yokohama DeNA BayStars aux Fukuoka SoftBank Hawks — une confrontation qui n'avait plus eu lieu depuis deux ans.",
    "ko": "Le typhon n° 30, Champi — un nom proposé par le Laos, qui désigne une fleur — remonte vers le nord, et l'agence météorologique l'a qualifié de typhon très fort le matin du 21.",
    "zh-cn": "C'est la semaine où l'on paie le solde du Double 11, et il arrive tôt cette année : JD vendait déjà des articles en stock dès le 12 octobre à 20 heures, puis a lancé son « ouverture » le 20 octobre à 20 heures, tandis que Taobao et Tmall ont ouvert leurs préventes le 15 octobre à 20 heures.",
    "zh-tw": "Le typhon puissant Jangmi s'approche des eaux à l'est de Taïwan : le 20 octobre au soir, son centre se trouvait à environ 1 390 kilomètres à l'est-sud-est d'Eluanbi, avec des vents proches de 60 mètres par seconde. L'effet combiné avec la mousson du nord-est risque de rendre les pluies plus fortes et plus longues.",
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
        self.text(MX, 2624, "Le Lucerna · COVER · 19-25 octobre 2026", 20, "sans", False, GREY)
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
    p.text(MX, y + tag_size, f"{LANG_FR[lang]} — {it['masthead']}", tag_size, "sans", True, OLIVE)
    y += tag_size + 22
    # headline (verbatim)
    y = p.para(MX, y + head_size, it["headline"], head_size, "serif", True, INK, W, 1.25) + 18
    # excerpt (verbatim)
    y = p.para(MX, y + ex_size, it["excerpt"], ex_size, "serif", False, INK, W, 1.5) + 26
    # explanation box
    note = "Note — " + EXPL[lang]
    lines = wrap(note, "sans", False, note_size, W - 60)
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
    y = p.centered(448, "Semaine du 19-25 octobre 2026", 40, "sans", False, GREY)
    # cover title + generic framing intro (no new facts)
    y = p.centered(y + 34, "Douze langues, une semaine d'actualités", 66, "serif", True, INK, lh=1.2) + 30
    intro = ("Chaque semaine, les rédactions de Lucerna choisissent, dans douze langues, "
             "le fait qui a marqué leurs lecteurs. Voici leurs douze unes, réunies dans "
             "un seul numéro, avec des explications en français.")
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
        p.text(x, yy + 28, f"{idx + 1} · {LANG_FR[it['source_lang']]}", 28, "sans", True, OLIVE)
        yy += 28 + 16
        yy = p.para(x, yy + 34, it["headline"], 34, "serif", True, INK, colw, 1.3) + 30
        tops[col] = yy
    y = max(tops) + 30
    y = p.centered(y, "Chaque une est reproduite dans sa langue d'origine ; "
                      "les explications sont en français.", 26, "sans", False, GREY)
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
    y = p.centered(y, "Chaque journal, sa une — dans sa langue d'origine.",
                   30, "sans", False, GREY) + 40
    p.hline(MX, RIGHT, y + 6, GOLD, 2)
    y += 56
    for it in ITEMS:
        p.text(MX, y + 26, f"{it['masthead']} · VOL.{it['vol']}", 26, "sans", True, OLIVE)
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
