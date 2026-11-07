# -*- coding: utf-8 -*-
"""W43 weekly cover for SIMPLIFIED CHINESE readers (cover-w43-zh-cn).

Self-contained builder. Layout scaffolding follows the proven sibling
cover builds (cover-w43-en-build/build.py); text measurement follows the
Simplified Chinese core build (weekly-report-zhcn-build/svglib.py):
PIL-measured wrap, 1950x2700 pages, warm ivory #f7f1e2, deep olive
accents, serif headlines. Code is COPIED here, never imported from a
core build dir (importing a core content module would execute
module-level code that writes into the core's files dir).

Hard rules observed here:
- Headlines + excerpts are loaded VERBATIM from the shared backfill file
  headlines-w43.json and are never edited, re-punctuated, or converted
  between scripts. The zh-tw item's headline/excerpt stay TRADITIONAL
  verbatim; only this builder's OWN writing (title, intro, labels,
  explanations, footers) is in SIMPLIFIED Chinese, written natively.
- My own Chinese text already uses full-width punctuation natively, so
  NO punctuation rewriting (_fw-style) is applied to anything: verbatim
  text is measured and rendered byte-for-byte as loaded.
- Kinsoku post-processing (copied from the zh-cn core svglib) adjusts
  line starts/ends, then every final line width is RE-CHECKED against
  max_w; the build asserts on any violation.
- Masthead is "Lucerna" with NO article (tables.json zh-cn entry:
  article null). NO VOL number for the cover itself; it is marked COVER.
- Explanations are in Simplified Chinese, 1-2 sentences each, every
  claim traceable to that item's own headline + excerpt only.
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
# Font family per source language (shipped-core convention).
FAMILY = {
    "en": "SC", "de": "SC", "fr": "SC", "es": "SC", "it": "SC",
    "pt": "SC", "nl": "SC", "ru": "SC", "ja": "JP", "ko": "KR",
    "zh-cn": "SC", "zh-tw": "TC",
}
# Reader-facing language labels, in SIMPLIFIED Chinese (own writing).
LABEL = {
    "en": "英语", "de": "德语", "fr": "法语", "es": "西班牙语",
    "it": "意大利语", "pt": "葡萄牙语", "nl": "荷兰语", "ru": "俄语",
    "ja": "日语", "ko": "韩语", "zh-cn": "简体中文",
    "zh-tw": "繁体中文",
}


def serif_family(lang):
    return "Noto Serif CJK " + FAMILY[lang]


def sans_family(lang):
    return "Noto Sans CJK " + FAMILY[lang]


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


# Kinsoku sets, copied from the zh-cn core svglib.py.
NO_START = "。、，．！？：；）」』】％ー…‥・)]}〉》.,!?%:;\""
NO_END = "「『（【〈《([{\""


def wrap(text, family, bold, size, max_w):
    """Greedy wrap: Latin/Cyrillic words kept whole, CJK per char;
    then kinsoku adjustment, then final line widths re-checked.
    Wrapping uses a slack of 70 units so a kinsoku pull-down of one
    character cannot push a final line past max_w."""
    slack_w = max_w - 70
    lines, cur = [], ""
    tokens, buf = [], ""
    for ch in text:
        if ord(ch) < 0x2E80 and ch != " ":
            buf += ch
        else:
            if buf:
                tokens.append(buf)
                buf = ""
            tokens.append(ch)
    if buf:
        tokens.append(buf)
    for tok in tokens:
        trial = cur + tok
        if text_w(trial, family, bold, size) <= slack_w or not cur.strip():
            cur = trial
        else:
            lines.append(cur.rstrip())
            cur = tok.lstrip() if tok == " " else tok
    if cur.strip():
        lines.append(cur.rstrip())
    # Kinsoku: a line must not START with closing punctuation (pull the
    # previous line's last character down); must not END with opening
    # punctuation (push it to the next line). Line count unchanged.
    for i in range(1, len(lines)):
        guard = 0
        while lines[i] and lines[i][0] in NO_START and len(lines[i - 1]) > 1 and guard < 8:
            lines[i] = lines[i - 1][-1] + lines[i]
            lines[i - 1] = lines[i - 1][:-1].rstrip()
            guard += 1
    for i in range(len(lines) - 1):
        guard = 0
        while lines[i] and lines[i][-1] in NO_END and len(lines[i]) > 1 and guard < 8:
            lines[i + 1] = lines[i][-1] + lines[i + 1]
            lines[i] = lines[i][:-1].rstrip()
            guard += 1
    # Re-check final line widths (task requirement).
    for ln in lines:
        w = text_w(ln, family, bold, size)
        assert w <= max_w, f"kinsoku line over width: {w:.0f} > {max_w} in {ln!r}"
    return lines


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


INK = "#28251d"
OLIVE = "#3e4c2a"
GOLD = "#b3a06a"
PAPER = "#f7f1e2"
BOX = "#fdfaf0"
LINE = "#d8cfb4"
GREY = "#57523f"
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
        self.text(MX, 2624, "Lucerna · COVER · 2026年10月19日至25日",
                  20, "Noto Sans CJK SC", False, GREY)
        self.text(RIGHT, 2624, f"第{n}页 共8页", 20, "Noto Sans CJK SC",
                  False, GREY, anchor="end")

    def save(self, path):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{PW}" height="{PH}" '
               f'viewBox="0 0 {PW} {PH}">' + "".join(self.parts) + "</svg>")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        return path


# ---------------------------------------------------------------- explanations
# SIMPLIFIED Chinese, 1-2 sentences each, every claim traceable to the
# item's own headline + excerpt only. No facts beyond the source article.
# Keywords glossed only: Clásico → 国家德比, 참피 → 灿比 (name gloss).
EXPL = {
    "en": "美国大选日定在11月3日，但多州的投票已经开始：得克萨斯州以及阿拉斯加、阿肯色、康涅狄格和科罗拉多州10月19日星期一起开放提前投票。",
    "de": "德国将在周六夜间至周日凌晨结束夏令时，凌晨3点钟表拨回2点，多出一个小时；同时有十一个州正在放假。",
    "fr": "2027年法国总统大选虽然还没到，但法国人已经开始关注：本周法国谷歌搜索第一名就是“2027年总统大选民调”，每天有成千上万人搜索这些词。",
    "es": "本周日凌晨西班牙将调表：3点钟表拨回2点，夜晚长达25小时，可以多睡一小时；同一天还有国家德比。",
    "it": "意大利将在10月24日星期六夜间至25日星期日调表，凌晨3点钟表拨回2点，夜晚多出一小时；在七个月的夏令时之后，冬令时回来了。",
    "pt": "巴西人将在10月25日星期日、巴西利亚时间上午8点至下午5点再次投票，参加总统选举第二轮，对决双方是卢拉和弗拉维奥·博索纳罗。",
    "nl": "这是荷兰内容满满的一周：中部和南部地区整个星期都在放秋假，从10月17日星期六到25日星期日；北部地区上周已经放假，星期一重新开学。",
    "ru": "初雪可能就在本周降临：预报说第一片雪花可能出现在10月21日至23日的星期三到星期五，气温在零度左右。",
    "ja": "日本系列赛第一场将于10月24日星期六18点30分在横滨体育场举行，对阵双方是横滨DeNA海湾之星和福冈软银鹰，两队上次交手是两年前。",
    "ko": "第30号台风“灿比”正在北上，名字由老挝提供，意思是花的名字；气象厅21日早上说，它是非常强的台风。",
    "zh-cn": "今年的双11来得早：京东10月12日晚上8点开始卖现货，10月20日晚上8点还有“开门红”；淘宝和天猫10月15日晚上8点开始预售，本周正是“付尾款”的一周。",
    "zh-tw": "强台风正向台湾东侧海面移动，预计周五、周六风雨最大；台风外围环流加上东北季风的“共伴效应”，会让雨下得更大、更久。",
}


def main():
    items = json.load(open(SRC, encoding="utf-8"))
    assert [it["source_lang"] for it in items] == ["en", "de", "fr", "es", "it",
        "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"], "fixed order changed!"
    # Verbatim guard: what we render must be exactly what the JSON holds.
    # (No transformation is applied to headline/excerpt anywhere below.)
    for it in items:
        assert it["excerpt"], it["source_lang"]
    os.makedirs(OUT, exist_ok=True)
    SC_SERIF, SC_SANS = "Noto Serif CJK SC", "Noto Sans CJK SC"

    # ---------------------------------------------------------- P1: cover
    p = Page()
    p.text(975, 235, "Lucerna", 150, SC_SERIF, True, INK, "middle")
    # COVER badge (rect painted before its text, so the audit never sees a cover)
    p.rect(975 - 150, 278, 300, 66, fill=OLIVE, rx=8)
    p.text(975, 278 + 45, "COVER", 34, SC_SANS, True, "#f3edda", "middle")
    p.text(975, 420, "2026年10月19日至25日  ·  简体中文读者每周封面",
           30, SC_SANS, False, GREY, "middle")
    p.hline(375, 1575, 460, GOLD, 2.5)
    y = p.para_center(975, 580, "一周十二条头条", 92, SC_SERIF,
                      True, INK, 1700, 1.2)
    intro = ("十二份报纸，十二种语言，同一周。每条头条都以原文原样登载，"
             "内页附上原文摘录和简体中文讲解。")
    y = p.para_center(975, y + 30, intro, 31, SC_SERIF, False, GREY, 1560, 1.5)
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
               22, SC_SANS, True, OLIVE)
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
        el = len(wrap(EXPL[it["source_lang"]], SC_SANS, False, 32, RIGHT - MX - 56))
        boxh = 28 + 34 + el * 32 * 1.5 + 24
        return 62 + hl + 18 + ex + 26 + boxh

    pairs = [(items[i], items[i + 1]) for i in range(0, 12, 2)]
    for pi, (a, b) in enumerate(pairs):
        p = Page()
        p.text(MX, 150, "Lucerna", 54, SC_SERIF, True, INK)
        p.text(RIGHT, 150, "COVER  ·  2026年10月19日至25日", 26, SC_SANS, False,
               GREY, anchor="end")
        p.hline(MX, RIGHT, 185, GOLD, 2)
        # Vertically centre the two blocks in the content area (220..2540).
        total = item_h(a) + 120 + item_h(b)
        y = 220 + max(0, (2540 - 220 - total) // 2)
        for j, it in enumerate((a, b)):
            sf = serif_family(it["source_lang"])
            p.text(MX, y, f"{LABEL[it['source_lang']]}  —  {it['masthead']}",
                   30, SC_SANS, True, OLIVE)
            y = p.para(MX, y + 70, it["headline"], 60, sf, True, INK, RIGHT - MX, 1.25)
            y = p.para(MX, y + 22, it["excerpt"], 37, sf, False, INK, RIGHT - MX, 1.5)
            # Explanation box (measured first, rect painted before its texts)
            expl = EXPL[it["source_lang"]]
            iw = RIGHT - MX - 56
            elines = wrap(expl, SC_SANS, False, 32, iw)
            boxh = 28 + 34 + len(elines) * 32 * 1.5 + 24
            yb = y + 26
            p.rect(MX, yb, RIGHT - MX, boxh, fill=BOX, stroke=LINE, sw=1.4)
            p.text(MX + 28, yb + 28 + 24, "简体中文讲解", 25, SC_SANS, True, OLIVE)
            yy = yb + 28 + 34
            for ln in elines:
                p.text(MX + 28, yy + 32, ln, 32, SC_SANS, False, GREY)
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
    p.text(MX, 150, "Lucerna", 54, SC_SERIF, True, INK)
    p.text(RIGHT, 150, "COVER  ·  2026年10月19日至25日", 26, SC_SANS, False,
           GREY, anchor="end")
    p.hline(MX, RIGHT, 185, GOLD, 2)
    y = p.para(MX, 270, "本周十二篇核心报纸一览", 52,
               SC_SERIF, True, INK, RIGHT - MX, 1.2)
    y = p.para(MX, y + 12, "每篇核心报纸的刊头和卷号，配上本封面内页登载的同一条头版头条。",
               28, SC_SERIF, False, GREY, RIGHT - MX, 1.45)
    y += 30
    for it in items:
        sf = serif_family(it["source_lang"])
        p.text(MX, y, f"{it['masthead'].upper()}  ·  VOL.{it['vol']}",
               25, SC_SANS, True, OLIVE)
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
