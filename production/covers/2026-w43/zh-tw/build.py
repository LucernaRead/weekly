# -*- coding: utf-8 -*-
"""Lucerna weekly COVER, W43 (19-25 Oct 2026), reader language TRADITIONAL CHINESE.

Source material: cover-backfill/headlines-w43.json ONLY (headlines + excerpts
verbatim, fixed order). Explanations in Traditional Chinese restate
headline+excerpt only. Written NATIVELY in Traditional Chinese — never
converted from a Simplified version.
No VOL number on P1 (COVER badge instead); P8 carries masthead + VOL
(FR VOL.2, all others VOL.1, per the JSON).
Page size 1950x2700, weekly visual system (ivory #f7f1e2, olive, serif).
Font faces per language so PIL measurement matches the audit's face_index:
  Latin + RU -> SC (2), JA -> JP (0), KO -> KR (1), zh-cn -> SC (2), zh-tw -> TC (3)
Own writing uses lang zh-tw (TC face, index 3) throughout.
"""
import json, os
from PIL import ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/cover-backfill/headlines-w43.json")
OUT = os.path.join(BASE, "svg")
os.makedirs(OUT, exist_ok=True)

with open(SRC, encoding="utf-8") as f:
    ITEMS = json.load(f)
assert len(ITEMS) == 12, len(ITEMS)
ORDER = ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"]
assert [i["source_lang"] for i in ITEMS] == ORDER

# Traditional Chinese reader-language labels for the source languages
LABEL = {
    "en": "英語", "de": "德語", "fr": "法語", "es": "西班牙語",
    "it": "義大利語", "pt": "葡萄牙語", "nl": "荷蘭語", "ru": "俄語",
    "ja": "日語", "ko": "韓語", "zh-cn": "簡體中文",
    "zh-tw": "繁體中文",
}
FACE = {"ja": 0, "ko": 1, "zh-tw": 3}  # default SC = 2
SUFFIX = {"ja": "JP", "ko": "KR", "zh-tw": "TC"}  # default SC

FONTS_DIR = "/usr/share/fonts/opentype/noto"
SERIF = os.path.join(FONTS_DIR, "NotoSerifCJK-Regular.ttc")
SERIF_B = os.path.join(FONTS_DIR, "NotoSerifCJK-Bold.ttc")
SANS = os.path.join(FONTS_DIR, "NotoSansCJK-Regular.ttc")
SANS_B = os.path.join(FONTS_DIR, "NotoSansCJK-Bold.ttc")
_cache = {}

def font(kind, bold, size, lang):
    idx = FACE.get(lang, 2)
    path = (SERIF_B if bold else SERIF) if kind == "serif" else (SANS_B if bold else SANS)
    key = (path, size, idx)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, size, index=idx)
    return _cache[key]

def text_w(s, kind, bold, size, lang):
    return font(kind, bold, size, lang).getlength(s) if s else 0.0

def wrap(text, kind, bold, size, max_w, lang):
    """Greedy wrap: Latin words whole, CJK chars individually."""
    lines, cur, buf, tokens = [], "", "", []
    for ch in text:
        if ord(ch) < 0x2E80 and ch != " ":
            buf += ch
        else:
            if buf:
                tokens.append(buf); buf = ""
            tokens.append(ch)
    if buf:
        tokens.append(buf)
    # Kinsoku: closing punctuation never starts a line (attach to previous
    # token); opening punctuation never ends a line (attach to next token).
    _closers = set("。，、；：！？」』）》·…")
    _openers = set("「『（《〈")
    _merged = []
    _i = 0
    while _i < len(tokens):
        tok = tokens[_i]
        if tok in _closers and _merged and _merged[-1] != " ":
            _merged[-1] = _merged[-1] + tok
        elif tok in _openers and _i + 1 < len(tokens):
            _merged.append(tok + tokens[_i + 1])
            _i += 1
        else:
            _merged.append(tok)
        _i += 1
    tokens = _merged
    for tok in tokens:
        trial = cur + tok
        if text_w(trial, kind, bold, size, lang) <= max_w or not cur.strip():
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
BOX = "#fdfaf0"; LINE = "#d8cfb4"; GREY = "#57523f"; BRICK = "#a4553a"
W, H = 1950, 2700
MX = 110            # side margin (inside frame)
CW = W - 2 * MX     # content width 1730
RL = "zh-tw"        # reader language for all cover-original writing

def fam(kind, lang):
    suf = SUFFIX.get(lang, "SC")
    return ("Noto Serif CJK " + suf) if kind == "serif" else ("Noto Sans CJK " + suf)

class Page:
    def __init__(self):
        self.parts = [
            f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
            f'<rect x="26" y="26" width="{W-52}" height="{H-52}" fill="none" stroke="{INK}" stroke-width="3"/>',
            f'<rect x="37" y="37" width="{W-74}" height="{H-74}" fill="none" stroke="{INK}" stroke-width="1.2"/>',
        ]
    def add(self, s):
        self.parts.append(s)
    def text(self, x, y, s, size=28, kind="serif", bold=False, fill=INK, anchor="start", lang=RL):
        wt = ' font-weight="700"' if bold else ""
        self.add(f'<text x="{x}" y="{y}" font-family="{fam(kind, lang)}" font-size="{size}"{wt} fill="{fill}" text-anchor="{anchor}">{esc(s)}</text>')
        return y
    def para(self, x, y, s, size=28, kind="serif", bold=False, fill=INK, max_w=CW, lh=1.5, lang=RL):
        for ln in wrap(s, kind, bold, size, max_w, lang):
            self.text(x, y, ln, size, kind, bold, fill, lang=lang)
            y += size * lh
        return y
    def para_h(self, s, size, kind, bold, max_w, lh, lang):
        return len(wrap(s, kind, bold, size, max_w, lang)) * size * lh
    def hline(self, x1, x2, y, color=LINE, wdt=1.2):
        self.add(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="{wdt}"/>')
    def rect(self, x, y, w, h, fill="none", stroke=None, sw=1.2):
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"{st}/>')
    def footer(self, n):
        self.text(W // 2, 2624, f"Lucerna · 每週封面 · 第 {n} 頁，共 8 頁", 28, "sans", False, GREY, anchor="middle", lang=RL)
    def save(self, name):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
               f'viewBox="0 0 {W} {H}">' + "".join(self.parts) + "</svg>")
        path = os.path.join(OUT, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        return path

def masthead(p, y=210):
    p.text(W // 2, y, "Lucerna", 150, "serif", True, INK, anchor="middle", lang=RL)
    return y

def cover_badge(p):
    # Top-right COVER badge, clear of the masthead block.
    p.rect(1630, 78, 210, 64, fill=OLIVE)
    p.text(1735, 124, "COVER", 34, "sans", True, "#f7f1e2", anchor="middle", lang=RL)

WEEK_LABEL = "2026年10月19日至25日"

# --- Traditional Chinese explanations: restatements of headline + excerpt ONLY ---
# Names kept verbatim where a transliteration would invent a form:
#   PT candidates stay Lula (PT) / Flávio Bolsonaro (PL);
#   KO typhoon named 참피, glossed (Champi) — the only correct Latin form;
#   no invented Chinese transliteration, never Chanpi/Changpi/Fung-wong;
#   JA team names stay verbatim (横浜DeNAベイスターズ / 福岡ソフトバンクホークス).
EXPL = {
    "en": "美國的投票已經開始：提前投票於十月十九日星期一在德州，以及阿拉斯加、阿肯色、康乃狄克與科羅拉多展開，正式的投票日則是十一月三日星期二。",
    "de": "德國將在星期六夜裡到星期天把時鐘撥慢一小時：凌晨三點的鐘會回到兩點，夏令時間就此結束，而本週有十一個國家放假。",
    "fr": "雖然總統大選在2027年，法國人已經開始談論它：本週法國 Google 搜尋第一名就是「2027年總統大選民調」，每天都有成千上萬人搜尋這些字詞。",
    "es": "本週日西班牙有兩件大事同時發生：凌晨三點時鐘會回到兩點，夜晚因此有二十五個小時、可以多睡一小時，而且當天還要踢國家德比。",
    "it": "在十月二十四日星期六夜裡到二十五日星期天，義大利將改回標準時間：凌晨三點的鐘會倒撥一小時回到兩點，夜晚因此多出一小時，結束了七個月的夏令時間。",
    "pt": "十月二十五日星期天上午八點到下午五點（巴西利亞時間），巴西人將再次走進投票所，參加總統大選第二輪投票，對決的只剩下兩位候選人：Lula（PT）與 Flávio Bolsonaro（PL）。",
    "nl": "荷蘭本週十分熱鬧：中部與南部地區從十月十七日星期六到二十五日星期天放秋假，北部地區上週放假、星期一重新開學，此外還有設計、舞蹈，以及多睡一小時。",
    "ru": "第一場雪可能就在本週降臨：氣象預報說，十月二十一日到二十三日星期三到星期五之間可能出現初雪，戶外氣溫大約在零度上下。",
    "ja": "日本大賽第一戰將於十月二十四日星期六晚上六點三十分在橫濱球場開打，對戰組合是横浜DeNAベイスターズ與福岡ソフトバンクホークス，這是兩隊睽違兩年的對決。",
    "ko": "第30號颱風「참피 (Champi)」正向北移動：這個名字由寮國提供，意思是花的名字，氣象廳在21日早上表示，참피是個非常強烈的颱風。",
    "zh-cn": "今年的雙十一來得早：京東從十月十二日晚上八點開始販售現貨，十月二十日晚上八點還有「開門紅」，淘寶與天貓則從十月十五日晚上八點開始預售。",
    "zh-tw": "強烈颱風「薔琵」正朝台灣東邊海面走來：十月二十日星期二晚上，颱風中心在鵝鑾鼻東南東方約1,390公里，近中心最大風速約每秒60公尺，暴風半徑280公里；再加上東北季風的外圍環流共伴效應，雨會下得更大、更久。",
}

TITLE = "十二種語言，一週大事"
INTRO = ("十二條頭條，十二種語言：本期封面集結了本週十二種語言版本的開篇新聞，"
         "讓讀者用正在學習的語言，看見世界的一週。")

def build_p1():
    p = Page()
    cover_badge(p)
    masthead(p)
    p.text(W // 2, 300, WEEK_LABEL, 40, "sans", False, GREY, anchor="middle", lang=RL)
    p.hline(MX, W - MX, 340, GOLD, 3)
    y = 470
    y = p.text(W // 2, y, TITLE, 88, "serif", True, OLIVE, anchor="middle", lang=RL)
    y += 70
    y = p.para(MX, y, INTRO, 40, "serif", False, INK, max_w=CW, lh=1.5, lang=RL)
    y += 45
    p.hline(MX, W - MX, y, GOLD, 2)
    y += 70
    _heights = []
    for _it in ITEMS:
        _hl = p.para_h(_it["headline"], 37, "serif", True, CW, 1.35, _it["source_lang"])
        _heights.append(42 + _hl)
    _gap = max(18, int((2500 - y - sum(_heights)) // 12))
    for it in ITEMS:
        lang = it["source_lang"]
        y = p.text(MX, y, LABEL[lang].upper() + "  ·  " + it["masthead"], 27, "sans", True, OLIVE, lang=RL)
        y += 42
        y = p.para(MX, y, it["headline"], 37, "serif", True, INK, max_w=CW, lh=1.35, lang=lang)
        y += _gap
    assert y < 2560, f"P1 overflow: ends at {y}"
    p.footer(1)
    p.save("p1-cover.svg")

def build_item_pages():
    pairs = [(ITEMS[i], ITEMS[i + 1]) for i in range(0, 12, 2)]
    for pi, (a, b) in enumerate(pairs):
        p = Page()
        p.text(MX, 150, "Lucerna · 每週封面", 34, "sans", True, OLIVE, lang=RL)
        p.text(W - MX, 150, WEEK_LABEL, 34, "sans", False, GREY, anchor="end", lang=RL)
        p.hline(MX, W - MX, 185, GOLD, 2)
        y = 270
        for it in (a, b):
            lang = it["source_lang"]
            y = p.text(MX, y, LABEL[lang].upper() + "  ·  " + it["masthead"], 30, "sans", True, OLIVE, lang=RL)
            y += 50
            y = p.para(MX, y, it["headline"], 50, "serif", True, INK, max_w=CW, lh=1.35, lang=lang)
            y += 28
            y = p.para(MX, y, it["excerpt"], 42, "serif", False, INK, max_w=CW, lh=1.5, lang=lang)
            y += 30
            y = p.text(MX, y, "繁體中文解說", 27, "sans", True, BRICK, lang=RL)
            y += 48
            y = p.para(MX, y, EXPL[lang], 42, "serif", False, GREY, max_w=CW, lh=1.5, lang=RL)
            y += 55
            if it is a:
                p.hline(MX, W - MX, y, LINE, 1.5)
                y += 70
        assert y < 2560, f"P{pi+2} overflow: ends at {y}"
        p.footer(pi + 2)
        p.save(f"p{pi+2}-cover.svg")

def build_p8():
    p = Page()
    p.text(W // 2, 150, "Lucerna", 110, "serif", True, INK, anchor="middle", lang=RL)
    p.text(W // 2, 235, "本週十二份核心報一覽", 44, "serif", False, OLIVE, anchor="middle", lang=RL)
    p.text(W // 2, 300, WEEK_LABEL, 36, "sans", False, GREY, anchor="middle", lang=RL)
    p.hline(MX, W - MX, 340, GOLD, 3)
    y = 450
    _heights = []
    for _it in ITEMS:
        _hl = p.para_h(_it["headline"], 37, "serif", True, CW, 1.35, _it["source_lang"])
        _heights.append(42 + _hl)
    _gap = max(18, int((2500 - y - sum(_heights)) // 12))
    for it in ITEMS:
        lang = it["source_lang"]
        y = p.text(MX, y, f'{it["masthead"]} · VOL. {it["vol"]}  ·  {LABEL[lang]}', 28, "sans", True, OLIVE, lang=RL)
        y += 42
        y = p.para(MX, y, it["headline"], 37, "serif", True, INK, max_w=CW, lh=1.35, lang=lang)
        y += _gap
    assert y < 2560, f"P8 overflow: ends at {y}"
    p.footer(8)
    p.save("p8-cover.svg")

build_p1()
build_item_pages()
build_p8()
print("SVGs written to", OUT)
for n in sorted(os.listdir(OUT)):
    print(" ", n, os.path.getsize(os.path.join(OUT, n)), "bytes")
