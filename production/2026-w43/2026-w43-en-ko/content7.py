# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-en-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND · 정밀 해설", "The Lucerna", "A2 → B2 · Phrases of the week · 이번 주 명문장")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("LEVEL A2 · 기초", 27)
cA.head("TELLING THE TIME", 24)
cA.para("It's eight o'clock. · It's half past two. · It's a quarter to eight. For the hour, English always starts with « It's » — never « it has ». The three clocks on page 2 show the week's three times.", 22.5)
cA.head("GOING TO + VERB", 24)
cA.para("For a plan : « She is going to vote on Saturday. » be + going to + the verb, with no change. It is the friendliest future in English — use it for every plan of the week.", 22.5)
cA.box("THE EXAMPLE · 예문", [
    ("« Checks are going to grow in January. » — the Social Security story, from page 2.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("LEVEL B1 · 중급", 27)
cB.head("COMPARATIVES", 24)
cB.para("Short adjective + -er + than : « Austin is hotter than Milwaukee. » Long adjective : more + adjective : « more convenient ». And good becomes better — never « more good ». Page 4 and page 6 are full of them.", 22.5)
cB.head("THE PAST SIMPLE", 24)
cB.para("Regular verbs add -ed : raised, watched. Irregular verbs change : win → won, sweep → swept, beat → beat, go → went. Sports pages are written in this tense — every result is past.", 22.5)
cB.box("THE EXAMPLE · 예문", [
    ("« Maxey scored more points than Brunson. » — comparison and past simple in one line (page 4).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW)], 200, 1150, tag="P7-B2")
cC.head("LEVEL B2 · 도전", 27)
cC.head("HEADLINE PRESENT", 24)
cC.para("Headlines speak of yesterday in the present : « 76ers win opener », « Early voting opens in Texas ». The present simple makes old news feel live. Read the front page again and find three.", 22.5)
cC.head("WHETHER = IF ?", 24)
cC.para("« Nobody knows whether the Brewers can finish the story. » Whether introduces an open question inside a sentence — more elegant than if, and safe everywhere. It is the word of the deep read (page 6).", 22.5)
cC.box("THE EXAMPLE · 예문", [
    ("« Voting is no longer a day ; it is a season. » — no longer = 더 이상 ~않다 (page 6).", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-tools")
cD.head("THE TOOLBOX · 도구 상자", 27)
cD.para("Three sentences to keep in your pocket, one for each level :", 22.5)
cD.para("A2 — « It's a quarter to eight. »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « The 76ers won, and Maxey scored more than Brunson. »", 22.5)
cD.para("B2 — « Nobody knows whether the story ends with a trophy. »", 22.5, "serif", True, OLIVE)
cD.para("And the newspaper reflex : every phrase of the week comes from an article of this issue. Re-read the article, and the phrase becomes easy.", 22.5)
cD.expl("도구 상자 — 이번 호 휴대 문장 세 개, 단계마다 하나; 명문장은 전부 이번 호 기사에서 왔어요. 원문을 다시 읽는 게 가장 효과적이에요.")
cD.end_report()

# --- phrases of the week ---
py = 1210
p.hline(MX, RIGHT, py - 14, GOLD, 2)
p.text(MX, py + 26, "PHRASES OF THE WEEK · 이번 주 명문장 (전부 이번 호 기사에서)", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "문장마다 문법 포인트 하나 + 작은 문제 하나 · 정답은 8면에", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« On Tuesday, October 20, the 2026–27 season opened with something new : a tripleheader. » (page 4)",
     "문법 포인트 — 일반 과거형: open → opened, 규칙 변화예요.",
     "B1", "The World Series ___ (open) on Friday.", "opened", "open → opened"),
    ("« When the prices of food, homes and energy go up, the checks go up too. » (page 2)",
     "문법 포인트 — go up = 오르다; when 절은 일반 현재형으로 법칙을 말해요.",
     "A2", "When energy costs more, the bills ___ too. (go up)", "go up", "go up 오르다"),
    ("« Milwaukee swept the Los Angeles Dodgers. » (page 4)",
     "문법 포인트 — sweep의 과거형은 swept, 불규칙.",
     "B1", "Tampa Bay ___ (beat) Cleveland on Monday.", "beat", "beat → beat (변화 없음)"),
    ("« Neither club has ever won the World Series. » (page 4)",
     "문법 포인트 — neither + 단수 동사: 두 팀 (둘 다 우승한 적이 없어요).",
     "B2", "Neither team ___ (have) a trophy yet.", "has", "neither → has"),
    ("« Voting is no longer a day ; it is a season. » (page 6)",
     "문법 포인트 — no longer = 더 이상 ~않다, be동사 뒤에 와요.",
     "B2", "The game is ___ on television only ; it is on phones too.", "no longer", "no longer = 더 이상 ~않다"),
    ("« Voters head to the polls. » (page 6)",
     "문법 포인트 — head to = ~로 향하다 (헤드라인의 현재형).",
     "A2", "On Tuesday, fans ___ to the stadium. (head)", "head", "fans → head (기본형)"),
    ("« The average retired worker will get about 75 dollars more every month. » (page 2)",
     "문법 포인트 — about = 약, 대략: 어림수에 써요.",
     "A2", "The average check is ___ two thousand dollars a month.", "about", "about 약, 대략"),
    ("« In Europe, the clocks fall back on Sunday — in America, on Sunday, November 1. » (page 2)",
     "문법 포인트 — fall back = (시계를) 되돌리다; 봄에는 spring forward.",
     "B1", "In spring, the clocks ___ forward. (spring)", "spring", "spring forward 앞으로 돌리다"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 20.5, "serif", True, INK, 1.34, 3)
    pf.expl(point, 19, 4)
    pf.ex(lv, "따라 연습", key, note, q, size=20.5)
pf.end_report()

# --- bottom: clinic (left) + readers' corner & teaser (right) ---
by7 = 1870
p.hline(MX, RIGHT, by7 - 14, GOLD, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("THE ERROR CLINIC · 실수 클리닉", 25)
cf.expl("문장마다 오류가 하나씩 있어요: 찾아서 고치세요.")
cf.ex("A2", "오류 고치기", "I agree with you.", "agree는 동사라서 앞에 am이 필요 없어요",
     "✗ « I am agree with you. »", instr="오류 고치기", size=22.5)
cf.ex("A2", "오류 고치기", "Yesterday I went to the game.", "go의 과거형은 went",
     "✗ « Yesterday I go to the game. »", instr="오류 고치기", size=22.5)
cf.ex("B1", "오류 고치기", "This week is busier than last week.", "busier에 이미 비교급이 들어 있어 more는 쓰지 않아요",
     "✗ « This week is more busier than last week. »", instr="오류 고치기", size=22.5)
cf.ex("B1", "오류 고치기", "He doesn't like early voting.", "3인칭 단수 부정은 doesn't + 기본형",
     "✗ « He don't like early voting. »", instr="오류 고치기", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(rx + 24, by7 + 48, "READERS' CORNER · 독자 코너", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« This autumn, I read my first book in English — one page every night, with Lucerna. » — R. T., a reader in Toronto (editor's example : the first real reader letters will take this place in VOL.2)", 21.5, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 206, "편집부 답글 — one page every night는 가장 꾸준한 습관이에요: 일반 현재형이 바로 습관을 말하죠. 안내: 이 편지는 편집부 예시예요. VOL.2부터 실제 독자 편지를 싣고, 이번 호 8면 쓰기 투고도 평가해요.", 20, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 332
p.rect(rx, ty7, rw, 2540 - ty7, fill=DARK)
p.text(rx + 24, ty7 + 46, "NEXT WEEK · VOL.2 다음 주 예고", 24, "sans", True, "#f3edda")
p.para(rx + 24, ty7 + 84, "Saturday, October 31 : Halloween night, live. Sunday, November 1 : America falls back — one more hour of sleep. Tuesday, November 3 : Election Day. What do Americans read, watch and eat while they wait for the results ?", 21.5, "serif", False, "#e8dfc8", rw - 48, 1.45)
p.para(rx + 24, ty7 + 218, "다음 주 토요일은 할로윈 밤, 일요일에는 미국 전역이 시계를 되돌리고, 11월 3일 화요일 선거일에 결과가 나와요.", 20, "sans", False, "#b3a06a", rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
