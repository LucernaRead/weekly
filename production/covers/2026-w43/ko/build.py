# -*- coding: utf-8 -*-
"""W43 weekly cover, reader language KO. 8 pages, 1950x2700.
Headlines/excerpts copied verbatim from cover-backfill/headlines-w43.json.
All cover-original writing in Korean (haeyoche), explanations traceable
to headline+excerpt only. Masthead 'Lucerna' (no article), NO VOL, COVER badge.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import Page, wrap, text_w, INK, OLIVE, GOLD, GREY, BOX, LINE

BASE = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(BASE, "svg")
os.makedirs(SVG_DIR, exist_ok=True)

with open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/cover-backfill/headlines-w43.json"), encoding="utf-8") as f:
    ITEMS = json.load(f)
assert [i["source_lang"] for i in ITEMS] == ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"], [i["source_lang"] for i in ITEMS]

LANG_KO = {"en": "영어", "de": "독일어", "fr": "프랑스어", "es": "스페인어",
           "it": "이탈리아어", "pt": "포르투갈어", "nl": "네덜란드어", "ru": "러시아어",
           "ja": "일본어", "ko": "한국어", "zh-cn": "중국어(간체)", "zh-tw": "중국어(번체)"}
CODE_LABEL = {"en": "EN", "de": "DE", "fr": "FR", "es": "ES", "it": "IT", "pt": "PT",
              "nl": "NL", "ru": "RU", "ja": "JA", "ko": "KO", "zh-cn": "ZH-CN", "zh-tw": "ZH-TW"}

EXPL = {
    "en": "11월 3일 선거일을 앞두고 텍사스를 비롯한 여러 주에서 이미 조기 투표가 시작됐어요. 헤드라인은 선거와 함께 이번 주를 미국의 큰 한 주라고 소개해요.",
    "de": "독일에서는 일요일 새벽에 서머타임이 끝나고 시계가 3시에서 2시로 한 시간 뒤로 돌아가요. 헤드라인은 독일의 열한 개 주가 휴가 중이라는 소식도 함께 전해요.",
    "fr": "2027년 프랑스 대선이 아직 멀었지만, 프랑스 사람들이 벌써 여론조사를 찾아보고 있어요. 이번 주 프랑스에서 가장 많이 검색된 말이 \u201c2027 대선 여론조사\u201d라는 점이 눈길을 끌어요.",
    "es": "스페인에서는 일요일 새벽 3시 시계가 2시로 돌아가면서 밤이 25시간이 되고 한 시간 더 잘 수 있어요. 같은 날 클라시코도 열린다고 헤드라인이 전해요.",
    "it": "이탈리아에서는 10월 24일 밤부터 25일 새벽 사이에 3시 시계가 2시로 돌아가면서 밤이 한 시간 길어져요. 이렇게 일곱 달간의 서머타임이 끝나고 동계 시간으로 돌아간다는 이야기예요.",
    "pt": "브라질에서는 10월 25일 일요일 오전 8시부터 오후 5시까지 대통령 선거 결선 투표가 열려요. 룰라와 플라비우 보우소나루, 두 후보만이 경쟁하고 있어요.",
    "nl": "네덜란드 중부와 남부 지역은 10월 17일부터 25일까지 일주일 내내 가을 방학이에요. 북부 지역은 지난주에 쉬었고 이번 주 월요일부터 학교가 다시 시작해요.",
    "ru": "러시아에서는 이번 주에 첫눈이 내릴 수 있어요. 10월 21일부터 23일 사이, 기온 0도 안팎에서 첫 눈송이가 예상돼요.",
    "ja": "일본 시리즈 1차전은 10월 24일 토요일 저녁 6시 30분 요코하마 스타디움에서 열려요. 요코하마 DeNA 베이스타즈와 후쿠오카 소프트뱅크 호크스의 대결은 2년 만이에요.",
    "ko": "제30호 태풍 참피가 북상하고 있어요. \u201c참피\u201d는 라오스가 낸 꽃 이름이고, 기상청은 21일 아침에 아주 강한 태풍이라고 했어요.",
    "zh-cn": "올해 중국의 \u201c双11\u201d 행사가 일찍 시작됐어요. 징둥은 10월 12일 저녁 8시부터 현물 판매를 시작했고 10월 20일 저녁 8시에는 \u300c开门红\u300d 행사가 열렸으며, 타오바오와 티몰은 10월 15일 저녁 8시부터 사전 판매를 시작했어요.",
    "zh-tw": "강력한 태풍 「薔琵」가 대만 동쪽 해상을 향해 다가오고 있어요. 10월 20일 저녁 기준으로 중심 부근 최대 풍속은 초속 60미터이고 폭풍 반경은 280킬로미터이며, 동북 계절풍과 태풍 외곽 순환이 합쳐지는 \u300c共伴效應\u300d 때문에 비가 더 크고 오래 내릴 수 있어요.",
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
    p.text(X1, 118, "2026년 10월 19일~25일", 30, "sans", False, GREY, anchor="end")
    p.hline(X0, X1, 142, GOLD, 2.5)
    p.text(X0, 2624, "Lucerna · COVER · 2026년 10월 19일~25일", 26, "sans", False, GREY)
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
p.text(X1, 118, "2026년 10월 19일~25일", 30, "sans", False, GREY, anchor="end")
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
p.text(X0, 2624, "Lucerna · COVER · 2026년 10월 19일~25일", 26, "sans", False, GREY)
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
        ex_size = 45 if lang == "en" else 46  # EN excerpt at 46pt strands lone "too." on final line; 45pt pulls the clause up
        y, _ = para_lines(p, X0, y, it["excerpt"], ex_size, "serif", False, INK, CW, 1.7, family=fam(lang))
        y += 24
        p.text(X0, y, "한국어 설명", 32, "sans", True, OLIVE)
        y += 52
        # 2026-10-28 orphan fix (wording untouched): NL + JA explanations at
        # 46pt strand a 1-token final line ("시작해요.", "만이에요."); at 45pt
        # each reflows to 2 lines with a multi-token final line. All other
        # explanations stay at 46pt.
        expl_size = 45 if lang in ("nl", "ja") else 46
        y, _ = para_lines(p, X0, y, EXPL[lang], expl_size, "serif", False, GREY, CW, 1.7)
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
