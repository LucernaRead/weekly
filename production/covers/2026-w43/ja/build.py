# -*- coding: utf-8 -*-
"""W43 weekly cover for JAPANESE readers (cover-w43-ja).

Self-contained builder. Layout patterns copied (not imported) from the
sibling cover-w43-en build (1950x2700 pages, warm ivory #f7f1e2, deep
olive accents, serif headlines); the WRAP function is copied from the
JA core's PATCHED svglib (hidden_files/weekly-report-ja-build/svglib.py,
md5 d73e23b3, copied verbatim into this dir as svglib_ja_core.py):
kinsoku NO_START oidashi + seam repair that RE-MEASURES final line
widths (SEAM_SLACK=28). Adaptation vs the core file: the width function
is parameterized per font family (the core measures JP face only; this
cover sets 12 source languages in their shipped-core faces), and the
NO_START set is extended with the ASCII closer set per tools/README
rule 19 (KO x JA precedent: `)]}>.,!?%:;"` plus full-width closers),
so ASCII-punctuated bodies cannot strand closers at line starts.
The core file itself is never edited and never imported (its content
modules are not imported either, per the no-import rule).

Headlines + excerpts are loaded VERBATIM from the shared backfill file
headlines-w43.json and are never edited here. Explanations are written
in Japanese and trace only to each item's headline + excerpt.
"""
import json, os
from PIL import ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/"
                         "hidden_files/cover-backfill/headlines-w43.json")
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

# --- wrap: COPIED from the JA core's patched svglib (kinsoku + seam repair)
SEAM_SLACK = 28
# JA core NO_START + ASCII closer extension (tools/README rule 19),
# plus small kana (sutegana, JIS X 4051) — FIX 2026-10-28: a line must
# not start with a sutegana. Unlike closers, a sutegana is NOT handled
# by the generic oidashi below (pulling the previous line's last char
# down would strand it differently); it is pulled UP to the end of the
# previous line by the sutegana pass in wrap(), so it stays attached
# to the kana it modifies.
SUTEGANA = "ぁぃぅぇぉっゃゅょァィゥェォッャュョ"
NO_START = "。、，．！？：；）」』】ー…‥・)]}〉》.,!?%:;\"" + SUTEGANA

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
    # Sutegana pass (FIX 2026-10-28): a line must not START with a small
    # kana — pull it UP to the end of the previous line (rewrap only,
    # no wording change). The pulled-up line may exceed max_w by up to
    # one kana width; the final-width assert allows max_w + SEAM_SLACK.
    for i in range(1, len(lines)):
        while lines[i] and lines[i][0] in SUTEGANA and lines[i - 1]:
            lines[i - 1] = lines[i - 1] + lines[i][0]
            lines[i] = lines[i][1:]
    # kinsoku shori: a line must not START with closing punctuation —
    # pull the previous line's last character down (oidashi). Sutegana
    # are excluded here: they were handled by the pull-up pass above,
    # and any survivor must fail the final assert loudly, not be
    # silently re-mangled by oidashi.
    pre_w = [text_w(ln, family, bold, size) for ln in lines]
    for i in range(1, len(lines)):
        while lines[i] and lines[i][0] in NO_START and lines[i][0] not in SUTEGANA and len(lines[i - 1]) > 1:
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
WEEK = "2026年10月19日～25日"

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
# headline + excerpt only. No facts beyond the source article. The only
# gloss is zh-cn 「付尾款」 rendered as 「残りの代金を支払うこと」
# (a gloss of the headline's own words, no new fact).
EXPL = {
    "en": "投票日は11月3日だが、すでに多くの地域で投票が始まっており、10月19日にはテキサスなどで期日前投票が始まった。見出しは、今週の最初の試合にも触れている。",
    "de": "土曜から日曜にかけての夜、ドイツは時計を1時間戻して夏時間を終える。見出しによれば、11の州が休暇中である。",
    "fr": "大統領選挙は2027年だが、フランス人はすでに世論調査に注目している。今週フランスで最も検索されたのは「2027年大統領選の世論調査」だった。",
    "es": "日曜日の早朝にスペインは時計を戻し、夜は25時間になって1時間多く眠れる。同じ日にはクラシコも行われる。",
    "it": "10月24日（土）から25日（日）の夜、イタリアは時計を1時間戻し、7か月の夏時間のあと冬時間に戻る。夜は1時間長くなり、1時間多く眠れる。",
    "pt": "10月25日（日）8時から17時（ブラジリア時間）に、ブラジル人は大統領選挙の決選投票に向かう。候補はルラ氏とフラヴィオ・ボルソナロ氏の2人だけである。",
    "nl": "オランダは盛りだくさんの一週間で、中部と南部は10月17日から25日まで秋休み、北部は月曜日に学校が再開する。見出しはデザインやダンス、1時間の余分な睡眠にも触れている。",
    "ru": "今週にも初雪が降るかもしれない。予報では10月21日から23日（水～金）に最初の雪が予想され、気温は0度前後である。",
    "ja": "日本シリーズ第1戦は10月24日（土）18時30分に横浜スタジアムで行われる。横浜DeNAベイスターズと福岡ソフトバンクホークスが、2年ぶりに対決する。",
    "ko": "第30号台風チャンピーが北上している。名前はラオスがつけた花の名前で、気象庁は21日朝に非常に強い台風だと発表した。",
    "zh-cn": "今年の双11は早く始まっており、今週は「付尾款」、つまり残りの代金を支払う週である。京東は10月12日夜8時に現物販売を始め、10月20日夜8時に「開門紅」があり、淘宝と天猫は10月15日夜8時に予約販売を始めた。",
    "zh-tw": "強い台風薔琵が台湾の東の海に近づいており、金曜日と土曜日に風雨が最も強くなる。台風の外側の流れに東北季節風が加わる「共伴效應」で、雨はさらに多く、さらに長く降る。",
}

def main():
    items = json.load(open(SRC, encoding="utf-8"))
    assert [it["source_lang"] for it in items] == ["en", "de", "fr", "es", "it",
        "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"], "fixed order changed!"
    os.makedirs(OUT, exist_ok=True)

    # ---------------------------------------------------------- P1: cover
    p = Page()
    p.text(975, 235, "Lucerna", 150, JP_SERIF, True, INK, "middle")
    # COVER badge (rect painted before its text, so the audit never sees a cover)
    p.rect(975 - 150, 278, 300, 66, fill=OLIVE, rx=8)
    p.text(975, 278 + 45, "COVER", 34, JP_SANS, True, "#f3edda", "middle")
    p.text(975, 420, f"{WEEK}  ·  日本語読者のための週間カバー",
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
        p.save(os.path.join(OUT, f"p{pi+2}-items.svg"))

    # ------------------------------------------------- P8: cores at a glance
    p = Page()
    p.text(MX, 150, "Lucerna", 54, JP_SERIF, True, INK)
    p.text(RIGHT, 150, f"COVER  ·  {WEEK}", 26, JP_SANS, False,
           GREY, anchor="end")
    p.hline(MX, RIGHT, 185, GOLD, 2)
    y = p.para(MX, 270, "今週の十二の正刊——一覧", 52,
               JP_SERIF, True, INK, RIGHT - MX, 1.2)
    y = p.para(MX, y + 12, "各正刊の刊頭と巻号、そしてこのカバーに収めたものと"
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
    p.save(os.path.join(OUT, "p8-cores.svg"))
    print("Wrote 8 SVGs to", OUT)

if __name__ == "__main__":
    main()
