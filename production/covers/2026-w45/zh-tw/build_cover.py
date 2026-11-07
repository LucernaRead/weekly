# -*- coding: utf-8 -*-
"""W45 weekly cover, reader language TRADITIONAL CHINESE. 8 pages, 1950x2700.
Headlines/excerpts loaded verbatim from cover-backfill/headlines-w45.json
at build time, never retyped. Explanations written natively in Traditional
Chinese, traceable to headline+excerpt only. svglib.py is a COPY of the
W45 zh-tw core's svglib (TC face index), never imported from the core.
Verbatim items are never converted between scripts: the zh-cn item stays
Simplified, the zh-tw item stays Traditional.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import Page, wrap, text_w, esc, INK, OLIVE, GOLD, PAPER, BOX, LINE, GREY

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "svg")
os.makedirs(OUT, exist_ok=True)

ITEMS = json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/cover-backfill/headlines-w45.json"))
assert [i["source_lang"] for i in ITEMS] == ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"], "fixed order changed!"

VOL = {"fr": 3}  # all other 11 cores VOL.2 (per task)

# Per-script serif families for verbatim items (same mapping as the en cover).
FAMILY = {"en": "Noto Serif CJK SC", "de": "Noto Serif CJK SC", "fr": "Noto Serif CJK SC",
          "es": "Noto Serif CJK SC", "it": "Noto Serif CJK SC", "pt": "Noto Serif CJK SC",
          "nl": "Noto Serif CJK SC", "ru": "Noto Serif CJK SC",
          "ja": "Noto Serif CJK JP", "ko": "Noto Serif CJK KR",
          "zh-cn": "Noto Serif CJK SC", "zh-tw": "Noto Serif CJK TC"}
# Source-language tags: Traditional Chinese name + native label (tables.json label).
TAG = {"en": "英語  ·  English", "de": "德語  ·  Deutsch", "fr": "法語  ·  Français",
       "es": "西班牙語  ·  Español", "it": "義大利語  ·  Italiano", "pt": "葡萄牙語  ·  Português",
       "nl": "荷蘭語  ·  Nederlands", "ru": "俄語  ·  Русский", "ja": "日語  ·  日本語",
       "ko": "韓語  ·  한국어", "zh-cn": "簡體中文  ·  简体中文", "zh-tw": "繁體中文  ·  繁體中文"}

# Explanations, natively written in Traditional Chinese. Every direction,
# number, date and proper name matches its item's headline + excerpt exactly.
EXPLAIN = {
 "en": "美國將在11月3日星期二舉行期中選舉，眾議院全部435席、約三分之一參議院席次以及多州州長都將改選。",
 "de": "本週是足球週：星期二、星期三有歐冠聯賽，星期四有歐霸聯賽，星期五德甲第9輪開踢，連續四晚足球之後就是整個聯賽週末。其中星期二晚上9點拜仁作客馬德里競技，斯圖加特則在傍晚6點45分作客加拉塔薩雷。",
 "fr": "法國在11月2日星期一結束諸聖節假期、學生返校，整週的高潮落在11月7、8日的週末，三場決賽同時登場；其中星期日11月8日在楠泰爾舉行勞力士巴黎大師賽決賽，為本季最後一項網球大賽。",
 "es": "西班牙正進入選戰前的關鍵一週，候選人名單已經提交，各政黨現在著手撰寫政見；11月29日星期日西班牙將舉行大選，住房問題將決定選戰走向。",
 "it": "義大利在11月2日星期一迎來本季第一波真正的寒冷，亞得里亞海一側有雨，山區約1,300至1,500公尺處迎來初雪；11月預計比平均更冷，但這只是機率、不是定論。",
 "pt": "這一週從10月31日星期六、11月1日星期日到11月2日星期一亡靈節假期的連假開始，到11月8日星期日的Enem考試首日結束；全國都過著同樣的一週：休息、複習、應考。",
 "nl": "11月2日星期一至11月8日星期日是荷蘭的氣候週，全國各市鎮舉辦種樹、節能、騎單車代替開車等行動，人人都可以參加。",
 "ru": "這是俄羅斯不尋常的一週：星期一、星期二上班，星期三放假——11月4日星期三是夾在工作週中間的假日。",
 "ja": "文化日在11月3日星期二，是國定假日，學校和公司都放假，全國各地都會舉辦文化活動。",
 "ko": "11月2日星期一至11月8日星期日這一週是冬天開始的一週，11月7日星期六是立冬，是二十四節氣中屬於冬天的第一個節氣，也是泡菜醃製季的開始。",
 "zh-cn": "雙11購物節已經開始，京東10月12日晚上8點開賣現貨，淘寶和天貓10月15日晚上8點預售、10月20日晚上8點付尾款並現貨開售，現貨一路賣到11月13日，正好迎接冬天的到來。",
 "zh-tw": "香港金融科技週 x StartmeupHK 2026在11月2日星期一於香港開幕，一連五天至11月6日星期五，主會議和展覽在11月2、3日於香港會議展覽中心舉行，整週還有100多場社區活動，遍佈香港多個場地；規模盛大，預計逾45,000人參加，來自120多個經濟體，講者逾1,000人，參展商和新創公司逾800家，代表團逾30個。",
}
assert set(EXPLAIN) == {i["source_lang"] for i in ITEMS}

W, H = 1950, 2700
MX, CW = 130, 1690  # content x, width (130..1820)
FOOT_Y = 2624
WEEK = "2026年11月2日至11月8日"

def header(p):
    p.text(975, 128, "LUCERNA  ·  COVER  ·  " + WEEK, 30, "sans", False, GREY, anchor="middle")

def footer(p, num):
    p.hline(MX, MX + CW, 2570, LINE, 1.2)
    p.text(MX, FOOT_Y, "Lucerna  ·  COVER  ·  " + WEEK, 28, "sans", False, GREY)
    p.text(MX + CW, FOOT_Y, num, 28, "sans", False, GREY, anchor="end")

def para(p, x, y, s, size, kind, bold, fill, max_w, lh, family=None):
    for ln in wrap(s, kind, bold, size, max_w):
        p.text(x, y, ln, size, kind, bold, fill, family=family)
        y += size * lh
    return y

# ---------------- P1 ----------------
p = Page(W, H)
header(p)
p.text(975, 330, "Lucerna", 168, "serif", True, INK, anchor="middle")
bw = text_w("C O V E R", "sans", True, 44) + 90
p.rect(975 - bw / 2, 385, bw, 78, fill=OLIVE, rx=10)
p.text(975, 440, "C O V E R", 44, "sans", True, PAPER, anchor="middle")
p.text(975, 560, WEEK, 52, "serif", False, OLIVE, anchor="middle")
p.hline(375, 1575, 620, GOLD, 3)
p.text(975, 740, "十二張頭版，同一個星期", 84, "serif", True, INK, anchor="middle")
y = para(p, 220, 850, "十二份報紙、十二個頭版、同一個十一月的星期：下面的每一條頭條，都以自己的語言打開自己的一版頭版，並附上一段繁體中文解說，說明它說了什麼、為什麼值得一看。", 46, "serif", False, GREY, 1510, 1.45)
y += 40
p.hline(MX, MX + CW, y, GOLD, 2)
y += 55
for it in ITEMS:
    lang = it["source_lang"]
    p.text(MX, y, TAG[lang], 28, "sans", True, OLIVE)
    y += 40
    y = para(p, MX, y, it["headline"], 40, "serif", True, INK, CW, 1.28, family=FAMILY[lang])
    y += 18
    assert y < 2520, f"P1 overflow at {lang}: y={y}"
footer(p, "1")
p.save(os.path.join(OUT, "p1-cover.svg"))

# ---------------- P2-P7: two items per page ----------------
PAIRS = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
for pi, (a, b) in enumerate(PAIRS):
    p = Page(W, H)
    header(p)
    y = 210
    for idx in (a, b):
        it = ITEMS[idx]
        lang = it["source_lang"]
        p.text(MX, y, TAG[lang], 34, "sans", True, OLIVE)
        y += 74
        y = para(p, MX, y, it["headline"], 60, "serif", True, INK, CW, 1.28, family=FAMILY[lang])
        y += 30
        y = para(p, MX, y, it["excerpt"], 44, "serif", False, INK, CW, 1.5, family=FAMILY[lang])
        y += 34
        p.hline(MX, MX + 180, y, GOLD, 2.5)
        y += 48
        p.text(MX, y, "解說", 30, "sans", True, OLIVE)
        y += 46
        y = para(p, MX, y, EXPLAIN[lang], 44, "sans", False, GREY, CW, 1.5, family="Noto Sans CJK TC")
        y += 58
        if idx == a:
            p.hline(MX, MX + CW, y, LINE, 1.5)
            y += 62
        assert y < 2540, f"P{pi+2} overflow at {lang}: y={y}"
    footer(p, str(pi + 2))
    p.save(os.path.join(OUT, f"p{pi+2}-cover.svg"))

# ---------------- P8: twelve cores at a glance ----------------
p = Page(W, H)
header(p)
p.text(975, 300, "本週十二份報紙一覽", 88, "serif", True, INK, anchor="middle")
p.text(975, 390, "本封面背後的十二份核心週報，依序排列。", 44, "serif", False, GREY, anchor="middle")
p.hline(MX, MX + CW, 440, GOLD, 3)
y = 520
for it in ITEMS:
    lang = it["source_lang"]
    vol = VOL.get(lang, 2)
    p.text(MX, y, f"{it['masthead']}  ·  VOL.{vol}", 36, "sans", True, OLIVE)
    y += 48
    y = para(p, MX, y, it["headline"], 44, "serif", True, INK, CW, 1.32, family=FAMILY[lang])
    y += 36
    assert y < 2520, f"P8 overflow at {lang}: y={y}"
footer(p, "8")
p.save(os.path.join(OUT, "p8-cover.svg"))
print("OK: 8 SVGs in", OUT)
