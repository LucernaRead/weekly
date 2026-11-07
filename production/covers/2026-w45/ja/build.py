# -*- coding: utf-8 -*-
"""W45 weekly cover for JAPANESE readers (cover-w45-ja).

Layout patterns follow the W43 JA cover build (1950x2700 pages, warm
ivory #f7f1e2, deep olive accents, serif headlines); the WRAP function
follows the JA core's PATCHED svglib (hidden_files/weekly-report-ja-build/
svglib.py, md5 d73e23b3, copied verbatim into this dir as
svglib_ja_core.py -- never imported, never edited): kinsoku NO_START
oidashi + seam repair that RE-MEASURES final line widths
(SEAM_SLACK=28). Adaptation vs the core file, same as the W43 JA cover:
the width function is parameterized per font family (the core measures
JP face only; this cover sets 12 source languages in their shipped-core
faces), and the NO_START set is extended with the ASCII closer set per
tools/README rule 19 (KO x JA precedent), so ASCII-punctuated bodies
cannot strand closers at line starts. The core file itself is never
edited and never imported.

Headlines + excerpts are loaded VERBATIM from the shared backfill file
headlines-w45.json and are never edited here. Explanations are written
in Japanese and trace only to each item's headline + excerpt.
No cover-original text uses U+2019; Japanese text has no apostrophes.
"""
import json, os
from PIL import ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/"
                         "hidden_files/cover-backfill/headlines-w45.json")
OUT = os.path.join(HERE, "svg")

FONTS_DIR = "/usr/share/fonts/opentype/noto"
# Face indices inside the CJK TTCs (tables.json convention).
FACE = {"JP": 0, "KR": 1, "SC": 2, "TC": 3}
# Font family per source language (shipped-core convention, as in the
# EN cover build). Reader-language (Japanese) text always uses JP.
FAMILY = {
    "en": "SC", "de": "SC", "fr": "SC", "es": "SC", "it": "SC",
    "pt": "SC", "nl": "SC", "ru": "SC", "ja": "JP", "ko": "KR",
    "zh-cn": "SC", "zh-tw": "TC",
}
LABEL = {
    "en": "英語", "de": "ドイツ語", "fr": "フランス語", "es": "スペイン語",
    "it": "イタリア語", "pt": "ポルトガル語", "nl": "オランダ語",
    "ru": "ロシア語", "ja": "日本語", "ko": "韓国語",
    "zh-cn": "中国語（簡体字）", "zh-tw": "中国語（繁体字）",
}

def serif_family(lang):
    return "Noto Serif CJK " + FAMILY[lang]

def sans_family(lang):
    return "Noto Sans CJK " + FAMILY[lang]

JP_SERIF, JP_SANS = "Noto Serif CJK JP", "Noto Sans CJK JP"

_cache = {}

def _font(family, bold, size):
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

# --- wrap: mechanism COPIED from the JA core's patched svglib
SEAM_SLACK = 28
# JA core NO_START + ASCII closer extension (tools/README rule 19).
NO_START = "。、，．！？：；）」』】ー…‥・)]}〉》.,!?%:;\""

def wrap(text, family, bold, size, max_w):
    """Greedy wrap: Latin words kept whole, CJK per char; then kinsoku
    oidashi (no line starts with a closer) + seam repair that re-measures
    every final line width. Copied mechanism from JA core svglib."""
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
    # kinsoku shori: a line must not START with closing punctuation --
    # pull the previous line's last character down (oidashi).
    pre_w = [text_w(ln, family, bold, size) for ln in lines]
    for i in range(1, len(lines)):
        while lines[i] and lines[i][0] in NO_START and len(lines[i - 1]) > 1:
            lines[i] = lines[i - 1][-1] + lines[i]
            lines[i - 1] = lines[i - 1][:-1].rstrip()
    # Seam repair: oidashi never re-measures the receiving line, so a
    # line grown by oidashi can end past max_w. Repair ONLY such lines
    # (pre_w <= max_w + SEAM_SLACK): shed trailing glyphs to the head
    # of the next line until the line fits max_w again, cascading
    # forward. A NO_START glyph is shed together with the glyph before
    # it, so the next line never starts with one.
    cascade = False
    for i in range(len(lines)):
        if text_w(lines[i], family, bold, size) <= max_w + SEAM_SLACK:
            cascade = False
            continue
        if not cascade and pre_w[i] > max_w + SEAM_SLACK:
            continue  # unbreakable token, already seam-crossing pre-kinsoku
        cascade = True
        while text_w(lines[i], family, bold, size) > max_w and len(lines[i]) > 1:
            if lines[i][-1] in NO_START and len(lines[i]) > 2:
                move, lines[i] = lines[i][-2:], lines[i][:-2]
            else:
                move, lines[i] = lines[i][-1], lines[i][:-1]
            if i + 1 < len(lines):
                lines[i + 1] = move + lines[i + 1]
            else:
                lines.append(move)
        lines[i] = lines[i].rstrip()
    # Final-width re-check (task gate): every wrapped line must fit
    # max_w + SEAM_SLACK, and any line over max_w must be a single
    # unbreakable token (the documented exception above).
    for ln in lines:
        w = text_w(ln, family, bold, size)
        assert w <= max_w + SEAM_SLACK, \
            f"wrapped line over width: {w:.1f} > {max_w} for {ln!r}"
        assert w <= max_w or len(ln.strip().split()) <= 1, \
            f"line over max_w is not a single token: {ln!r}"
    # Kinsoku re-check: no line (except the first) starts with a closer.
    for ln in lines[1:]:
        assert not ln or ln[0] not in NO_START, \
            f"kinsoku violation, line starts with closer: {ln!r}"
    return lines

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

INK = "#28251d"; OLIVE = "#3e4c2a"; GOLD = "#b3a06a"; PAPER = "#f7f1e2"
BOX = "#fdfaf0"; LINE = "#d8cfb4"; GREY = "#57523f"; DARK = "#2c2822"
PW, PH = 1950, 2700
MX, RIGHT = 65, 1885
BOTTOM = 2540
WEEK = "2026年11月2日～8日"

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
        self.text(MX, 2624, f"Lucerna · COVER · {WEEK}",
                  20, JP_SANS, False, GREY)
        self.text(RIGHT, 2624, f"{n} / 8 ページ", 20, JP_SANS,
                  False, GREY, anchor="end")

    def save(self, path):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{PW}" height="{PH}" '
               f'viewBox="0 0 {PW} {PH}">' + "".join(self.parts) + "</svg>")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        return path

# ---------------------------------------------------------------- explanations
# Japanese, 1-2 sentences each, every claim traceable to the item's own
# headline + excerpt only. No facts beyond the source article.
EXPL = {
    "en": "11月3日は米国の投票日で、大統領の4年の任期の真ん中に行われる中間選挙である。下院の435議席すべてに加え、上院の約3分の1や多くの州の知事も選ばれる。",
    "de": "今週はサッカーの週で、火曜日と水曜日にチャンピオンズリーグ、木曜日にヨーロッパリーグが行われ、金曜日にブンデスリーガの第9節が始まる。火曜日21時にはバイエルンがアトレティコ・マドリードと対戦し、シュトゥットガルトは18時45分にガラタサライと対戦する。",
    "fr": "11月2日(月曜日)にトゥーサンの休暇が終わって生徒たちは学校に戻り、フランスは大きな一週間を迎える。週末の11月7日と8日には3つの決勝が同時に行われ、日曜日8日にはナンテールでシーズン最後の大きなテニス大会、ロレックス・パリ・マスターズの決勝が行われる。",
    "es": "スペインは選挙運動前の決定的な週に入り、候補者名簿はすでに提出され、各党はいま綱領を書いている。11月29日(日曜日)にはスペインで総選挙が行われ、住宅問題が選挙戦を決める。",
    "it": "11月2日(月曜日)にイタリアは様変わりし、シーズン最初の本格的な寒さがやってきて、アドリア海側では雨、標高1,300～1,500メートルほどの山では最初の軽い雪が降る。11月は平均より寒くなるという予報だが、それは確実なことではなく確率である。",
    "pt": "週は10月31日(土曜日)から11月2日(月曜日・祝日)の連休で始まり、11月8日(日曜日)のエネム初日で終わる。その間、国中が休み、復習し、試験を受ける同じ週を過ごす。",
    "nl": "11月2日(月曜日)から8日(日曜日)まで、オランダでは気候週間である。全国の自治体が植樹や省エネ、自家用車の代わりに自転車を使うなどの取り組みを行い、誰でも参加できる。",
    "ru": "ロシアでは今週は変わった週で、月曜日と火曜日は働き、水曜日は休みである。11月4日(水曜日)は、働く週の真ん中の休日である。",
    "ja": "文化の日は11月3日(火曜日)で、祝日のため学校も会社も休みである。文化の日には全国で文化のイベントがある。",
    "ko": "11月2日(月曜日)から8日(日曜日)まで、今週は冬が始まる週である。11月7日(土曜日)は立冬で、24節気のうち冬の最初の節気である。",
    "zh-cn": "今年の双11はすでに始まっており、京東は10月12日夜8時に現物販売を始め、淘宝と天猫は10月15日夜8時に予約販売を始め、10月20日夜8時に残りの代金の支払いと現物販売が始まった。現物販売は11月13日まで続く。",
    "zh-tw": "香港金融科技週×StartmeupHK 2026は11月2日(月曜日)に香港で開幕し、11月6日(金曜日)まで5日間続く。メインの会議と展示は11月2日と3日の2日間、香港会議展覧中心で行われ、週を通して100を超える地域イベントが香港各地で開かれる。",
}

def main():
    items = json.load(open(SRC, encoding="utf-8"))
    assert [it["source_lang"] for it in items] == ["en", "de", "fr", "es", "it",
        "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"], "fixed order changed!"
    # VOLs from the JSON itself (FR VOL.3, all others VOL.2).
    assert items[2]["vol"] == 3 and all(
        it["vol"] == 2 for i, it in enumerate(items) if i != 2), "VOL mismatch!"
    assert set(EXPL) == {it["source_lang"] for it in items}
    os.makedirs(OUT, exist_ok=True)

    # ---------------------------------------------------------- P1: cover
    p = Page()
    p.text(975, 235, "Lucerna", 150, JP_SERIF, True, INK, "middle")
    # COVER badge (rect painted before its text, so the audit never sees a cover)
    p.rect(975 - 150, 278, 300, 66, fill=OLIVE, rx=8)
    p.text(975, 278 + 45, "COVER", 34, JP_SANS, True, "#f3edda", "middle")
    p.text(975, 420, f"{WEEK}  ·  日本語で読む、今週の十二の第一面",
           30, JP_SANS, False, GREY, "middle")
    p.hline(375, 1575, 460, GOLD, 2.5)
    y = p.para_center(975, 580, "今週の十二の見出し", 92, JP_SERIF,
                      True, INK, 1700, 1.2)
    intro = ("十二の言語の第一面、十二の見出しを一冊に集めました。各見出しは"
             "それぞれの新聞の第一面に載ったままの言葉で、本文も原文のままです。"
             "日本語の解説とともに、今週の世界をめぐってみましょう。")
    y = p.para_center(975, y + 30, intro, 31, JP_SERIF, False, GREY, 1560, 1.5)
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
        sf = serif_family(it["source_lang"])
        p.text(x, yy, f"{idx+1:02d}  ·  {LABEL[it['source_lang']]}",
               22, JP_SANS, True, OLIVE)
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
        el = len(wrap(EXPL[it["source_lang"]], JP_SANS, False, 32, RIGHT - MX - 56))
        boxh = 28 + 34 + el * 32 * 1.5 + 24
        return 62 + hl + 18 + ex + 26 + boxh

    pairs = [(items[i], items[i + 1]) for i in range(0, 12, 2)]
    for pi, (a, b) in enumerate(pairs):
        p = Page()
        p.text(MX, 150, "Lucerna", 54, JP_SERIF, True, INK)
        p.text(RIGHT, 150, f"COVER  ·  {WEEK}", 26, JP_SANS, False,
               GREY, anchor="end")
        p.hline(MX, RIGHT, 185, GOLD, 2)
        # Vertically centre the two blocks in the content area (220..2540).
        total = item_h(a) + 120 + item_h(b)
        y = 220 + max(0, (2540 - 220 - total) // 2)
        for j, it in enumerate((a, b)):
            sf = serif_family(it["source_lang"])
            p.text(MX, y, f"{LABEL[it['source_lang']]}  —  {it['masthead']}",
                   30, JP_SANS, True, OLIVE)
            y = p.para(MX, y + 70, it["headline"], 60, sf, True, INK, RIGHT - MX, 1.25)
            y = p.para(MX, y + 22, it["excerpt"], 37, sf, False, INK, RIGHT - MX, 1.5)
            # Explanation box (measured first, rect painted before its texts)
            expl = EXPL[it["source_lang"]]
            iw = RIGHT - MX - 56
            elines = wrap(expl, JP_SANS, False, 32, iw)
            boxh = 28 + 34 + len(elines) * 32 * 1.5 + 24
            yb = y + 26
            p.rect(MX, yb, RIGHT - MX, boxh, fill=BOX, stroke=LINE, sw=1.4)
            p.text(MX + 28, yb + 28 + 24, "解説", 25, JP_SANS, True, OLIVE)
            yy = yb + 28 + 34
            for ln in elines:
                p.text(MX + 28, yy + 32, ln, 32, JP_SANS, False, GREY)
                yy += 32 * 1.5
            y = yb + boxh
            if j == 0:
                y += 120
                p.hline(MX, RIGHT, y - 60, LINE, 1.2)
            print(f"P{pi+2} {it['source_lang']} block ends y={y:.0f}")
            assert y <= BOTTOM, f"P{pi+2} overflow on {it['source_lang']}"
        p.foot(pi + 2)
        p.save(os.path.join(OUT, f"p{pi+2}-cover.svg"))

    # ------------------------------------------------- P8: cores at a glance
    p = Page()
    p.text(MX, 150, "Lucerna", 54, JP_SERIF, True, INK)
    p.text(RIGHT, 150, f"COVER  ·  {WEEK}", 26, JP_SANS, False,
           GREY, anchor="end")
    p.hline(MX, RIGHT, 185, GOLD, 2)
    y = p.para(MX, 270, "今週の十二紙——一覧", 52,
               JP_SERIF, True, INK, RIGHT - MX, 1.2)
    y = p.para(MX, y + 12, "各紙の刊頭と巻号、そしてこの号に収めたものと"
               "同じ第一面の見出しです。",
               28, JP_SERIF, False, GREY, RIGHT - MX, 1.45)
    y += 30
    for it in items:
        sf = serif_family(it["source_lang"])
        p.text(MX, y, f"{it['masthead']}  ·  VOL.{it['vol']}",
               25, JP_SANS, True, OLIVE)
        y = p.para(MX, y + 46, f"{LABEL[it['source_lang']]}：{it['headline']}",
                   32, sf, True, INK, RIGHT - MX, 1.28)
        y += 34
        p.hline(MX, RIGHT, y - 12, LINE, 1.0)
        y += 12
        assert y <= BOTTOM, f"P8 overflow on {it['source_lang']}"
    print("P8 ends y:", y)
    p.foot(8)
    p.save(os.path.join(OUT, "p8-cover.svg"))
    print("Wrote 8 SVGs to", OUT)

if __name__ == "__main__":
    main()
