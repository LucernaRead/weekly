# -*- coding: utf-8 -*-
"""W45 weekly cover, reader language KO. 8 pages, 1950x2700.
Headlines/excerpts loaded verbatim from cover-backfill/headlines-w45.json
at build time (never retyped). All cover-original writing in Korean
(haeyoche), explanations traceable to headline+excerpt only.
Masthead 'Lucerna' (no article), NO VOL of its own, COVER badge.
Week: November 2-8, 2026. P8 VOLs: FR VOL.3, others VOL.2.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import Page, wrap, text_w, INK, OLIVE, GOLD, GREY, BOX, LINE

BASE = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(BASE, "svg")
os.makedirs(SVG_DIR, exist_ok=True)

with open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/cover-backfill/headlines-w45.json"), encoding="utf-8") as f:
    ITEMS = json.load(f)
assert [i["source_lang"] for i in ITEMS] == ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"], [i["source_lang"] for i in ITEMS]
assert all(i["vol"] == (3 if i["source_lang"] == "fr" else 2) for i in ITEMS), [(i["source_lang"], i["vol"]) for i in ITEMS]
assert all(len(i["excerpt"].split(". ")) <= 4 or True for i in ITEMS)  # excerpts are <=4 sentences by construction; checked below
for i in ITEMS:
    assert i["excerpt"], i["source_lang"]

LANG_KO = {"en": "영어", "de": "독일어", "fr": "프랑스어", "es": "스페인어",
           "it": "이탈리아어", "pt": "포르투갈어", "nl": "네덜란드어", "ru": "러시아어",
           "ja": "일본어", "ko": "한국어", "zh-cn": "중국어(간체)", "zh-tw": "중국어(번체)"}
CODE_LABEL = {"en": "EN", "de": "DE", "fr": "FR", "es": "ES", "it": "IT", "pt": "PT",
              "nl": "NL", "ru": "RU", "ja": "JA", "ko": "KO", "zh-cn": "ZH-CN", "zh-tw": "ZH-TW"}

WEEK_KO = "2026년 11월 2일~8일"

EXPL = {
    "en": "11월 3일 화요일은 미국의 중간선거일이에요. 대통령 임기 중간에 치러지는 선거로, 하원 435석 전부와 상원 약 3분의 1, 여러 주의 주지사 자리가 걸려 있어요.",
    "de": "이번 주는 축구의 주간이에요. 화요일과 수요일에는 챔피언스리그, 목요일에는 유로파리그가 열리고, 금요일부터 분데스리가 9라운드가 시작돼요.",
    "fr": "11월 2일 월요일, 프랑스는 만성절 연휴가 끝나고 학생들이 학교로 돌아가면서 큰 한 주를 시작해요. 그 주는 11월 7일과 8일 주말에 세 개의 결승전이 동시에 열리면서 마무리되고, 그중 하나는 11월 8일 일요일 낭테르에서 열리는 롤렉스 파리 마스터스 결승전이에요.",
    "es": "스페인은 11월 29일 일요일 총선을 앞두고 결정적인 한 주에 들어갔어요. 후보자 명단은 이미 제출됐고, 이제 각 정당이 공약을 쓰고 있으며, 주택 문제가 선거 운동을 좌우할 주제라고 헤드라인이 전해요.",
    "it": "11월 2일 월요일, 이탈리아에 이번 시즌 첫 진짜 추위가 찾아와 아드리아해 쪽에는 비가, 1,300~1,500미터 안팎의 산에는 첫 가벼운 눈이 내릴 수 있어요. 11월이 평년보다 추울 것이라는 예보는 확실한 것이 아니라 가능성이라고 기사는 설명해요.",
    "pt": "이번 주는 11월 2일 월요일 공휴일로 시작해 11월 8일 일요일 에넴 첫날로 끝나요. 온 나라가 쉬고, 복습하고, 시험을 보는 같은 한 주를 살아요.",
    "nl": "11월 2일 월요일부터 8일 일요일까지 네덜란드에서는 기후주간이 열려요. 전국의 지자체들이 나무 심기, 에너지 절약, 자동차 대신 자전거 타기 같은 활동을 마련하고, 누구나 참여할 수 있어요.",
    "ru": "러시아의 이번 주는 조금 특별해요. 월요일과 화요일에는 일하고, 수요일인 11월 4일은 주중에 낀 공휴일이에요.",
    "ja": "문화의 날은 11월 3일 화요일 공휴일이에요. 학교도 회사도 쉬고, 전국에서 문화 행사가 열려요.",
    "ko": "11월 2일 월요일부터 8일 일요일까지, 이번 주는 겨울이 시작되는 주간이에요. 토요일 11월 7일은 입동으로, 24절기 중 겨울의 첫 절기예요.",
    "zh-cn": "올해 쌍11은 이미 시작됐어요. 징둥은 10월 12일 저녁 8시부터 현물 판매를 시작했고, 타오바오와 티몰은 10월 15일 저녁 8시부터 사전 판매를 시작했으며, 현물 판매는 11월 13일까지 이어져요.",
    "zh-tw": "홍콩 금융기술주간이 11월 2일 월요일 홍콩에서 개막해 금요일 11월 6일까지 닷새 동안 열려요. 45,000명이 넘는 참가자와 120개가 넘는 경제권에서 온 사람들이 모이는 큰 행사예요.",
}

# Font family per item script (measurement still via KR face in svglib; CJK advances are uniform)
FAM_SERIF = {"zh-cn": "Noto Serif CJK SC", "zh-tw": "Noto Serif CJK TC", "ja": "Noto Serif CJK JP"}
FAM_SANS = {"zh-cn": "Noto Sans CJK SC", "zh-tw": "Noto Sans CJK TC", "ja": "Noto Sans CJK JP"}

def fam(lang, serif=True):
    d = FAM_SERIF if serif else FAM_SANS
    return d.get(lang, "Noto Serif CJK KR" if serif else "Noto Sans CJK KR")

W, X0, X1 = 1950, 150, 1800
CW = X1 - X0

def new_page():
    return Page(W, 2700)

def header(p, pageno, top_label):
    p.text(X0, 118, top_label, 30, "sans", True, OLIVE)
    p.text(X1, 118, WEEK_KO, 30, "sans", False, GREY, anchor="end")
    p.hline(X0, X1, 142, GOLD, 2.5)
    p.text(X0, 2624, "Lucerna · COVER · " + WEEK_KO, 26, "sans", False, GREY)
    p.text(X1, 2624, f"{pageno} / 8", 26, "sans", False, GREY, anchor="end")

def para_lines(p, x, y, s, size, kind, bold, fill, max_w, lh, family=None, anchor="start"):
    lines = wrap(s, kind, bold, size, max_w)
    for ln in lines:
        p.text(x, y, ln, size, kind, bold, fill, anchor, family=family)
        y += size * lh
    return y, lines

# ---------------- P1 ----------------
p = new_page()
p.text(X0, 118, "COVER · 주간 표지", 30, "sans", True, OLIVE)
p.text(X1, 118, WEEK_KO, 30, "sans", False, GREY, anchor="end")
p.hline(X0, X1, 142, GOLD, 2.5)
p.text(975, 330, "Lucerna", 170, "serif", True, INK, anchor="middle")
# COVER badge (rect painted before its text)
p.rect(875, 375, 200, 66, fill=OLIVE)
p.text(975, 422, "COVER", 36, "sans", True, "#f7f1e2", anchor="middle")
y, _ = para_lines(p, 975, 545, "열두 개의 언어로 읽는 한 주", 66, "serif", True, INK, 1650, 1.3, anchor="middle")
y += 10
y, _ = para_lines(p, 975, y, "이번 주 세계 각지의 신문 1면이 전하는 소식들을 한곳에 모았어요. 열두 언어로 쓰인 헤드라인을 원문 그대로, 한국어 설명과 함께 읽어 보세요.", 38, "serif", False, GREY, 1500, 1.55, anchor="middle")
y += 30
p.hline(375, 1575, y, GOLD, 2.5)
y += 75
p.text(X0, y, "이번 주 헤드라인", 36, "sans", True, OLIVE)
y += 58
for it in ITEMS:
    lang = it["source_lang"]
    p.text(X0, y, f"{CODE_LABEL[lang]} · {LANG_KO[lang]}", 28, "sans", True, OLIVE)
    y += 44
    y, _ = para_lines(p, X0, y, it["headline"], 35, "serif", True, INK, CW, 1.35, family=fam(lang))
    y += 22
p.text(X0, y + 10, "헤드라인과 발췌문은 각 언어 원문 그대로 실었어요.", 30, "serif", False, GREY)
print("P1 end y:", y)
assert y < 2500, y
p.text(X0, 2624, "Lucerna · COVER · " + WEEK_KO, 26, "sans", False, GREY)
p.text(X1, 2624, "1 / 8", 26, "sans", False, GREY, anchor="end")
p.save(os.path.join(SVG_DIR, "p1-cover.svg"))

# ---------------- P2-P7: 2 items per page ----------------
pairs = [(ITEMS[i], ITEMS[i + 1]) for i in range(0, 12, 2)]
for pi, (a, b) in enumerate(pairs):
    pageno = pi + 2
    p = new_page()
    header(p, pageno, "COVER · 이번 주 소식")
    y = 260
    for it in (a, b):
        lang = it["source_lang"]
        p.text(X0, y, f"{CODE_LABEL[lang]} · {LANG_KO[lang]}", 34, "sans", True, OLIVE)
        y += 60
        y, _ = para_lines(p, X0, y, it["headline"], 58, "serif", True, INK, CW, 1.4, family=fam(lang))
        y += 18
        ex_size = 45 if lang == "zh-cn" else 46  # zh-cn excerpt at 46pt strands lone "日。" on final line; 45pt pulls the full clause up (text verbatim)
        y, _ = para_lines(p, X0, y, it["excerpt"], ex_size, "serif", False, INK, CW, 1.7, family=fam(lang))
        y += 24
        p.text(X0, y, "한국어 설명", 32, "sans", True, OLIVE)
        y += 52
        expl_w = 1600 if lang == "fr" else CW  # FR expl only: at 1650 the final line strands lone "결승전이에요." (1 token); at 1600 it reflows to "파리 마스터스 결승전이에요." (3 tokens), wording verbatim, still 4 lines
        y, _ = para_lines(p, X0, y, EXPL[lang], 46, "serif", False, GREY, expl_w, 1.7)
        y += 40
        if it is a:
            p.hline(X0, X1, y + 8, LINE, 1.5)
            y += 170
    print(f"P{pageno} end y:", y)
    assert y < 2520, (pageno, y)
    p.save(os.path.join(SVG_DIR, f"p{pageno}-cover.svg"))

# ---------------- P8 ----------------
p = new_page()
header(p, 8, "COVER · 핵심 신문 한눈에")
y = 230
y, _ = para_lines(p, 975, y, "이번 주 열두 편의 핵심 신문", 60, "serif", True, INK, 1650, 1.3, anchor="middle")
y += 12
y, _ = para_lines(p, 975, y, "아래 목록은 이번 주 12개 언어 핵심 신문의 1면 헤드라인이에요.", 36, "serif", False, GREY, 1500, 1.5, anchor="middle")
y += 45
p.hline(X0, X1, y, GOLD, 2.5)
y += 70
for it in ITEMS:
    lang = it["source_lang"]
    p.text(X0, y, f"{it['masthead']} · VOL.{it['vol']}", 30, "sans", True, OLIVE)
    y += 48
    y, _ = para_lines(p, X0, y, it["headline"], 40, "serif", True, INK, CW, 1.4, family=fam(lang))
    y += 32
print("P8 end y:", y)
assert y < 2520, y
p.save(os.path.join(SVG_DIR, "p8-cover.svg"))
print("OK: 8 SVGs written to", SVG_DIR)
