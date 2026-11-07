# -*- coding: utf-8 -*-
"""W43 weekly cover for ENGLISH readers (cover-w43-en).

Self-contained builder. Patterns copied (not imported) from the EN core
build (svglib.py / bslib4.py): PIL-measured wrap, 1950x2700 pages,
warm ivory #f7f1e2, deep olive accents, serif headlines.

Headlines + excerpts are loaded VERBATIM from the shared backfill file
headlines-w43.json and are never edited here. Explanations are written
in English and trace only to each item's headline + excerpt.
"""
import json, os, sys
from PIL import ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/"
                         "hidden_files/cover-backfill/headlines-w43.json")
OUT = os.path.join(HERE, "svg")

FONTS_DIR = "/usr/share/fonts/opentype/noto"
# Face indices inside the CJK TTCs (tables.json convention).
FACE = {"JP": 0, "KR": 1, "SC": 2, "TC": 3}
# Font family per source language (shipped-core convention).
FAMILY = {
    "en": "SC", "de": "SC", "fr": "SC", "es": "SC", "it": "SC",
    "pt": "SC", "nl": "SC", "ru": "SC", "ja": "JP", "ko": "KR",
    "zh-cn": "SC", "zh-tw": "TC",
}
LABEL = {
    "en": "English", "de": "German", "fr": "French", "es": "Spanish",
    "it": "Italian", "pt": "Portuguese", "nl": "Dutch", "ru": "Russian",
    "ja": "Japanese", "ko": "Korean", "zh-cn": "Simplified Chinese",
    "zh-tw": "Traditional Chinese",
}

def serif_family(lang):
    return "Noto Serif CJK " + FAMILY[lang]

def sans_family(lang):
    return "Noto Sans CJK " + FAMILY[lang]

_cache = {}

def _font(family, bold, size):
    # family like "Noto Serif CJK JP"
    kind = "serif" if "Serif" in family else "sans"
    face = family.strip().split()[-1]
    path = os.path.join(FONTS_DIR,
                        ("NotoSerifCJK-Bold.ttc" if bold else "NotoSerifCJK-Regular.ttc")
                        if kind == "serif" else
                        ("NotoSansCJK-Bold.ttc" if bold else "NotoSansCJK-Regular.ttc"))
    key = (path, FACE[face], size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, size, index=FACE[face])
    return _cache[key]

def text_w(s, family, bold, size):
    if not s:
        return 0.0
    return _font(family, bold, size).getlength(s)

def wrap(text, family, bold, size, max_w):
    """Greedy wrap: Latin/Cyrillic words kept whole, CJK per char."""
    lines, cur = [], ""
    tokens, buf = [], ""
    for ch in text:
        if ord(ch) < 0x2E80 and ch != " ":
            buf += ch
        else:
            if buf:
                tokens.append(buf); buf = ""
            tokens.append(ch)
    if buf:
        tokens.append(buf)
    for tok in tokens:
        trial = cur + tok
        if text_w(trial, family, bold, size) <= max_w or not cur.strip():
            cur = trial
        else:
            lines.append(cur.rstrip())
            cur = tok.lstrip() if tok == " " else tok
    if cur.strip():
        lines.append(cur.rstrip())
    return lines

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

INK = "#28251d"; OLIVE = "#3e4c2a"; GOLD = "#b3a06a"; PAPER = "#f7f1e2"
BOX = "#fdfaf0"; LINE = "#d8cfb4"; GREY = "#57523f"; DARK = "#2c2822"
PW, PH = 1950, 2700
MX, RIGHT = 65, 1885
BOTTOM = 2540

class Page:
    def __init__(self):
        self.parts = []
        self.add(f'<rect width="{PW}" height="{PH}" fill="{PAPER}"/>')
        self.add(f'<rect x="28" y="28" width="{PW-56}" height="{PH-56}" fill="none" stroke="{INK}" stroke-width="3.4"/>')
        self.add(f'<rect x="40" y="40" width="{PW-80}" height="{PH-80}" fill="none" stroke="{INK}" stroke-width="1.2"/>')

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, size, family, bold=False, fill=INK, anchor="start"):
        wt = ' font-weight="700"' if bold else ""
        self.add(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}"{wt} '
                 f'fill="{fill}" text-anchor="{anchor}">{esc(s)}</text>')

    def para(self, x, y, s, size, family, bold=False, fill=INK, max_w=900,
             lh=1.5, anchor="start"):
        for ln in wrap(s, family, bold, size, max_w):
            self.text(x, y, ln, size, family, bold, fill, anchor)
            y += size * lh
        return y

    def para_center(self, x_center, y, s, size, family, bold=False, fill=INK,
                    max_w=900, lh=1.5):
        for ln in wrap(s, family, bold, size, max_w):
            self.text(x_center, y, ln, size, family, bold, fill, "middle")
            y += size * lh
        return y

    def hline(self, x1, x2, y, color=LINE, wdt=1.2):
        self.add(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="{wdt}"/>')

    def rect(self, x, y, w, h, fill="none", stroke=None, sw=1.2, rx=0):
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st}/>')

    def foot(self, n):
        self.hline(MX, RIGHT, 2580, GOLD, 1.6)
        self.text(MX, 2624, "The Lucerna · COVER · October 19–25, 2026",
                  20, "Noto Sans CJK SC", False, GREY)
        self.text(RIGHT, 2624, f"Page {n} of 8", 20, "Noto Sans CJK SC",
                  False, GREY, anchor="end")

    def save(self, path):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{PW}" height="{PH}" '
               f'viewBox="0 0 {PW} {PH}">' + "".join(self.parts) + "</svg>")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        return path

# ---------------------------------------------------------------- explanations
# English, 1-2 sentences each, every claim traceable to the item's own
# headline + excerpt only. No facts beyond the source article.
EXPL = {
    "en": "Voting is already under way in several states ahead of Election Day on November 3, and the headline also points to the week's first games.",
    "de": "Germany turns its clocks back one hour in the early hours of Sunday, ending summer time, while eleven German states are on holiday.",
    "fr": "The presidential election is still in 2027, but French voters are already talking about it — this week the country's top Google search was for the 2027 presidential polls.",
    "es": "Spain gains an extra hour of sleep as the clocks go back in the early hours of Sunday, and the same day brings the Clásico.",
    "it": "Italy returns to standard time on the night of October 24–25, after seven months of daylight saving time, so the night — and everyone's sleep — lasts an hour longer.",
    "pt": "Brazilians vote on Sunday, October 25, from 8h to 17h Brasília time, in the presidential run-off between Lula and Flávio Bolsonaro.",
    "nl": "It is a full week in the Netherlands: the Central and South regions are on autumn holiday all week, while schools in the North start again on Monday.",
    "ru": "The first snow may fall this week, with forecasters expecting the first flakes between Wednesday and Friday, October 21–23, as temperatures sit around zero.",
    "ja": "The Japan Series opens on Saturday, October 24, at Yokohama Stadium, where the Yokohama DeNA BayStars meet the Fukuoka SoftBank Hawks in a match-up last seen two years ago.",
    "ko": "Typhoon Champi, the season's 30th typhoon, is heading north; named by Laos after a flower, it was described by the weather agency on the morning of the 21st as a very strong typhoon.",
    "zh-cn": "Double 11 has come early this year, and this is the week for paying final balances. JD began selling in-stock goods on October 12, with an opening promotion on October 20, while Taobao and Tmall opened pre-sales on October 15.",
    "zh-tw": "Strong Typhoon Jangmi is approaching the seas east of Taiwan, with the heaviest wind and rain expected on Friday and Saturday, and a combined effect with the northeast monsoon set to make the rain heavier and longer-lasting.",
}

def main():
    items = json.load(open(SRC, encoding="utf-8"))
    assert [it["source_lang"] for it in items] == ["en", "de", "fr", "es", "it",
        "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"], "fixed order changed!"
    for it in items:
        assert it["excerpt"].count(".") + it["excerpt"].count("。") >= 0
    os.makedirs(OUT, exist_ok=True)
    EN_SERIF, EN_SANS = "Noto Serif CJK SC", "Noto Sans CJK SC"

    # ---------------------------------------------------------- P1: cover
    p = Page()
    p.text(975, 235, "The Lucerna", 150, EN_SERIF, True, INK, "middle")
    # COVER badge (rect painted before its text, so the audit never sees a cover)
    p.rect(975 - 150, 278, 300, 66, fill=OLIVE, rx=8)
    p.text(975, 278 + 45, "COVER", 34, EN_SANS, True, "#f3edda", "middle")
    p.text(975, 420, "October 19–25, 2026  ·  Weekly Cover for English Readers",
           30, EN_SANS, False, GREY, "middle")
    p.hline(375, 1575, 460, GOLD, 2.5)
    y = p.para_center(975, 580, "The Week in Twelve Headlines", 92, EN_SERIF,
                      True, INK, 1700, 1.2)
    intro = ("Twelve front pages, twelve languages, one week. Each headline below "
             "appears in its original language, exactly as it led its own paper — "
             "turn the page to read each story in full, with a short explanation in English.")
    y = p.para_center(975, y + 30, intro, 31, EN_SERIF, False, GREY, 1560, 1.5)
    # Teasers: numbered 01-12 in fixed order, left column 1-6, right column 7-12.
    top = y + 55
    p.hline(MX, RIGHT, top - 30, LINE, 1.2)
    colx = [95, 1005]
    colw = 850
    pitch = 205
    for idx, it in enumerate(items):
        col = 0 if idx < 6 else 1
        row = idx % 6
        x = colx[col]
        yy = top + row * pitch
        sf, ss = serif_family(it["source_lang"]), sans_family(it["source_lang"])
        p.text(x, yy, f"{idx+1:02d}  ·  {LABEL[it['source_lang']].upper()}",
               22, EN_SANS, True, OLIVE)
        yy2 = p.para(x, yy + 42, it["headline"], 30, sf, True, INK, colw, 1.28)
        assert yy2 <= top + (row + 1) * pitch - 8, f"P1 teaser overflow: {it['source_lang']}"
    p.foot(1)
    p.save(os.path.join(OUT, "p1-cover.svg"))
    print("P1 teasers end y:", top + 6 * pitch)

    # ------------------------------------------------- P2-P7: two items each
    def item_h(it):
        sf = serif_family(it["source_lang"])
        hl = len(wrap(it["headline"], sf, True, 60, RIGHT - MX)) * 60 * 1.25
        ex = len(wrap(it["excerpt"], sf, False, 37, RIGHT - MX)) * 37 * 1.5
        el = len(wrap(EXPL[it["source_lang"]], EN_SANS, False, 32, RIGHT - MX - 56))
        boxh = 28 + 34 + el * 32 * 1.5 + 24
        return 62 + hl + 18 + ex + 26 + boxh

    pairs = [(items[i], items[i + 1]) for i in range(0, 12, 2)]
    for pi, (a, b) in enumerate(pairs):
        p = Page()
        p.text(MX, 150, "The Lucerna", 54, EN_SERIF, True, INK)
        p.text(RIGHT, 150, "COVER  ·  October 19–25, 2026", 26, EN_SANS, False,
               GREY, anchor="end")
        p.hline(MX, RIGHT, 185, GOLD, 2)
        # Vertically centre the two blocks in the content area (220..2540).
        total = item_h(a) + 120 + item_h(b)
        y = 220 + max(0, (2540 - 220 - total) // 2)
        for j, it in enumerate((a, b)):
            sf, ss = serif_family(it["source_lang"]), sans_family(it["source_lang"])
            p.text(MX, y, f"{LABEL[it['source_lang']].upper()}  —  {it['masthead']}",
                   30, EN_SANS, True, OLIVE)
            y = p.para(MX, y + 70, it["headline"], 60, sf, True, INK, RIGHT - MX, 1.25)
            y = p.para(MX, y + 22, it["excerpt"], 37, sf, False, INK, RIGHT - MX, 1.5)
            # Explanation box (measured first, rect painted before its texts)
            expl = EXPL[it["source_lang"]]
            iw = RIGHT - MX - 56
            elines = wrap(expl, EN_SANS, False, 32, iw)
            boxh = 28 + 34 + len(elines) * 32 * 1.5 + 24
            yb = y + 26
            p.rect(MX, yb, RIGHT - MX, boxh, fill=BOX, stroke=LINE, sw=1.4)
            p.text(MX + 28, yb + 28 + 24, "IN ENGLISH", 25, EN_SANS, True, OLIVE)
            yy = yb + 28 + 34
            for ln in elines:
                p.text(MX + 28, yy + 32, ln, 32, EN_SANS, False, GREY)
                yy += 32 * 1.5
            y = yb + boxh
            if j == 0:
                y += 120
                p.hline(MX, RIGHT, y - 60, LINE, 1.2)
            print(f"P{pi+2} {it['source_lang']} block ends y={y:.0f}")
            assert y <= BOTTOM, f"P{pi+2} overflow on {it['source_lang']}"
        p.foot(pi + 2)
        p.save(os.path.join(OUT, f"p{pi+2}-items.svg"))

    # ------------------------------------------------- P8: cores at a glance
    p = Page()
    p.text(MX, 150, "The Lucerna", 54, EN_SERIF, True, INK)
    p.text(RIGHT, 150, "COVER  ·  October 19–25, 2026", 26, EN_SANS, False,
           GREY, anchor="end")
    p.hline(MX, RIGHT, 185, GOLD, 2)
    y = p.para(MX, 270, "The Week's Twelve Core Papers — At a Glance", 52,
               EN_SERIF, True, INK, RIGHT - MX, 1.2)
    y = p.para(MX, y + 12, "Each core paper's masthead and volume, with the same "
               "front-page headline carried inside this cover.",
               28, EN_SERIF, False, GREY, RIGHT - MX, 1.45)
    y += 30
    for it in items:
        sf = serif_family(it["source_lang"])
        p.text(MX, y, f"{it['masthead'].upper()}  ·  VOL.{it['vol']}",
               25, EN_SANS, True, OLIVE)
        y = p.para(MX, y + 46, f"{LABEL[it['source_lang']]}: {it['headline']}",
                   32, sf, True, INK, RIGHT - MX, 1.28)
        y += 34
        p.hline(MX, RIGHT, y - 12, LINE, 1.0)
        y += 12
        assert y <= BOTTOM, f"P8 overflow on {it['source_lang']}"
    print("P8 ends y:", y)
    p.foot(8)
    p.save(os.path.join(OUT, "p8-cores.svg"))
    print("Wrote 8 SVGs to", OUT)

if __name__ == "__main__":
    main()
