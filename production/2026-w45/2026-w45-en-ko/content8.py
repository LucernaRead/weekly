# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-en-ko/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS · 연습과 정답", "The Lucerna", "FINAL TEST · 종합 평가 · Answers at the bottom of this page · 정답은 이 면 아래쪽에")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "11월 3일은 화요일이에요"),
    ("A2", "A", "pizza 피자"),
    ("B1", "C", "map 지도 주마다 색 변화"),
    ("A2", "B", "close 가까운"),
    ("A2", "A", "sticker 스티커"),
    ("A2", "C", "will + 동사원형 know"),
    ("B1", "B", "be going to → is going"),
    ("B1", "A", "still 여전히"),
]
cnums = [reg_ex(lv, "빈칸 채우기", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · CLOZE · 빈칸 채우기", 24, gap=8)
bf.para(f"Leo is sixteen. On Tuesday, November 3, it is ({cnums[0]})___. His family does not cook dinner : they order ({cnums[1]})___. On television, the ({cnums[2]})___ changes colour, state by state. « Ohio is very ({cnums[3]})___ ! » says his father. At nine o'clock, Leo's mother comes home from voting, with a ({cnums[4]})___ on her jacket : « I VOTED ». « When ({cnums[5]})___ we know the results ? » asks Leo. « Tomorrow », says his mother. « Tomorrow, Leo is ({cnums[6]})___ to read the results at school — and the map will ({cnums[7]})___ be on television tonight. »", 21.5)
bf.bridge("선택지:")
for n, (lv, _k, _nt), opts in zip(cnums, cloze_defs, [
    "A. Monday · B. Election Day · C. Halloween",
    "A. pizza · B. salad · C. soup",
    "A. phone · B. table · C. map",
    "A. far · B. close · C. big",
    "A. sticker · B. hat · C. ticket",
    "A. do · B. are · C. will",
    "A. goes · B. going · C. go",
    "A. still · B. never · C. soon",
]):
    bf.para(f"{n}. [{lv}] {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B · MULTIPLE CHOICE · 객관식", 24, gap=8)
mcq = [
    ("A2", "B", "1:30 = half past one", "The clocks show 1:30. In words : ... A. one o'clock · B. half past one · C. a quarter to one"),
    ("A2", "A", "we → get 원형", "On Sunday, we ___ an extra hour of sleep. A. get · B. gets · C. getting"),
    ("B1", "B", "이미 일어난 일에는 fell", "The clocks ___ back on Sunday. A. fall · B. fell · C. falling"),
    ("B1", "B", "than → 비교급 bigger", "The Bernabéu is ___ than most stadiums. A. big · B. bigger · C. biggest"),
    ("B2", "A", "despite + 명사: 비에도 불구하고", "___ the rain, the game went on all evening. A. Despite · B. Because · C. Unless"),
    ("B2", "A", "whether = ~인지", "Nobody knows ___ the race is called yet. A. whether · B. what · C. who"),
    ("A2", "A", "미래형 will + 동사원형", "The film ___ on Friday, November 6. A. will open · B. will opened · C. will opens"),
    ("B1", "A", "be going to + 원형 vote", "They are going to ___ on Tuesday. A. vote · B. votes · C. voted"),
    ("B1", "C", "too close to call = 승부를 알 수 없음", "« Too close to call » means... A. the winner is clear · B. voting is over · C. we do not know yet"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "객관식", k, nt, body, size=20.5)

# ---- C. reading ----
bf.head("C · READING · 읽기 이해", 24, gap=8)
bf.para("On Saturday morning, Sam, a teacher from Ohio, finished his breakfast and walked to the early-voting place near his school. There was no line. « On Tuesday, I teach all day », he explains. « Today, I have time. » Five minutes later, his ballot was in the box, and a sticker on his jacket said : I VOTED. On Tuesday night, Sam watched the map with his family — and Ohio was, as always, too close to call.", 21.5)
read_qs = [
    ("A2", "B", "원문: a teacher from Ohio", "Sam is... A. a nurse · B. a teacher · C. a driver"),
    ("A2", "B", "화요일에는 하루 종일 가르쳐요", "He voted early because on Tuesday he... A. travels · B. teaches all day · C. sleeps"),
    ("B1", "A", "스티커에는 I VOTED라고 쓰여 있어요", "His sticker said... A. I VOTED · B. VOTE ON TUESDAY · C. OHIO FIRST"),
    ("B1", "B", "오하이오는 언제나처럼 승부를 알 수 없어요", "On Tuesday night, Ohio was... A. clear · B. too close to call · C. finished early"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "읽기 이해", k, nt, body, size=20.5)

# ---- D. sentence building ----
bf.head("D · SENTENCES · 문장 완성과 바꾸기", 24, gap=8)
d_items = [
    ("A2", "On Friday, they are going to watch the cat film.", "are going to + 원형",
     "Be going to : « On Friday, they (watch) the cat film. » → ___"),
    ("B1", "The clocks fell back on Sunday.", "fall → fell(불규칙 변화)",
     "Past simple : « The clocks (fall) back on Sunday. »"),
    ("B1", "taller", "tall → taller(비교급)",
     "Comparative : « The hat is ___ (tall) than the Cat. »"),
    ("B2", "Whether", "whether는 '~인지' 절을 이끌어요",
     "Whether : « ___ the race is called, nobody knows yet. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "문장 완성", k, nt, body, size=20.5)

# ---- E. translation ----
bf.head("E · TRANSLATION · 번역", 24, gap=8)
e_items = [
    ("B2", "인내는 제도의 일부예요, 실패가 아니에요.", "part of = 일부분; not a failure = 실패가 아님",
     "Translate : « Patience is part of the system, not a failure of it. »"),
    ("A2", "11월 3일 화요일은 미국의 선거일이에요.", "Election Day = 선거일; on Tuesday = 화요일에",
     "번역: Tuesday, November 3, is Election Day in the United States."),
    ("B1", "일요일에 NFL이 마드리드에서 경기를 해요.", "on Sunday = 일요일에; in Madrid = 마드리드에서",
     "번역: On Sunday, the NFL plays in Madrid."),
    ("B1", "모든 곳이 시계를 되돌리는 건 아니에요.", "not every = 모든 ~가 아니다; change = 바뀌다",
     "Translate : « Not every place changes. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "번역", k, nt, body, size=20.5)

# ---- F. matching ----
bf.head("F · WORDS · 단어 짝짓기", 24, gap=8)
bf.match_set("B1", "단어 짝짓기",
             ["a midterm", "a governor", "a ballot", "turnout"],
             ["the number of people who vote",
              "an election in the middle of a term",
              "the person who leads a state",
              "the paper you mark your choice on"],
             ["b", "c", "d", "a"],
             ["midterm = 중간선거 b", "governor = 주지사 c", "ballot = 투표용지 d", "turnout = 투표율 a"],
             instr="짝짓기")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ID", "투표할 때 신분증 ID 제시"),
    ("A2", "line", "line = 줄 서기(미국식 영어)"),
    ("A2", "ballot", "ballot = 투표용지"),
    ("A2", "sticker", "sticker = 스티커"),
    ("B1", "Tuesday", "선거일 = 11월 3일 화요일"),
]
gnums = [reg_ex(lv, "대화 완성", k, nt) for lv, k, nt in dlg_defs]
bf.head("G · DIALOGUE · 대화 완성", 24, gap=8)
bf.para(f"— Good morning ! Is this the voting place ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long today ? — No, five minutes only. On Tuesday it will be very long ! — Good. It is my first vote. What do I do with the ({gnums[2]})___ ? — Mark your choices, check them twice, then put it in the box. — Thank you. And the famous ({gnums[3]})___ ? Everybody has one on their jacket. — The sticker ! Here it is : « I VOTED ». Wear it with pride. — I will ! See you on ({gnums[4]})___ , in the results ! — Ha ! Have a good day.", 21.5)
bf.para("Levels : 145–148 [A2] · 149 [B1]", 19.5, "sans", False, GREY, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "쓰기", "열린 문제 — 기준은 쓰기 칸에, 모범 답안은 8면 쓰기 칸 안에", "기준 항목대로 채점해요")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · WRITING · 쓰기 [B1]", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Tuesday, November 3 ». Tell us : did you watch the results, what did you eat, what did the map show — and one sentence about the clocks that fell back on Sunday night. The best texts will appear in VOL.3 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "영어로 80–100단어 쓰기: 나의 11월 3일 화요일. 결과를 봤는지, 무엇을 먹었는지, 지도가 무엇을 보여줬는지, 그리고 일요일 밤에 되돌린 시계에 대해 한 문장을 쓰세요.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MODEL · 모범 답안", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Tuesday, November 3, our family watched the election results at home. We ate pizza, because nobody wanted to cook on such a night. On television, the map changed colour, state by state, and my father said : « Ohio is too close to call ! » I did not understand every state, but I understood the pizza and the excitement. On Sunday night, the clocks had fallen back, so I slept one hour more. It was a long night, and a very American one.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "ANSWERS · 모든 정답과 간단한 설명(1–8면)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")
# Printed-note parity with the core (tools/p8.py extract on the
# core P8): the core prints a note when the item is on page 8,
# or its (Chinese) note is <= 10 chars, or its type is
# correction/chart-reading. Korean notes are longer, so the
# core printed set is applied EXPLICITLY by exercise number.
PRINT_NOTES = [11, 12, 14, 19, 29, 30, 31, 33, 41, 44, 47, 48, 51, 58, 64, 66, 67, 68, 69, 71, 74, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 100, 102, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 제 {pg} 면 —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and e["n"] in PRINT_NOTES:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
