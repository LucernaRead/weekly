# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-en-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND · 정밀 해설", "The Lucerna", "A2 → B2 · Phrases of the week · 이번 주의 명문장")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("LEVEL A2 · 기초", 27)
cA.head("FALLING BACK", 24)
cA.para("« The clocks fell back. » Fall back = to go back one hour. The past is fell back, not « falled back ». The repeated hour on November 1 is the example of the week (page 2).", 22.5)
cA.head("GOING TO + VERB", 24)
cA.para("For a plan : « She is going to vote on Tuesday. » be + going to + the verb, with no change. It is the friendliest future in English — use it for every plan of the week.", 22.5)
cA.box("THE EXAMPLE · 예문", [
    ("« Americans are going to vote on Tuesday. » — the election story, from page 1.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("LEVEL B1 · 중급", 27)
cB.head("COMPARATIVES", 24)
cB.para("Short adjective + -er + than : « The Bernabéu is bigger than most stadiums. » Long adjective : more + adjective : « more convenient ». And good becomes better — never « more good ». Page 4 is full of them.", 22.5)
cB.head("THE PAST SIMPLE", 24)
cB.para("Regular verbs add -ed : changed, watched. Irregular verbs change : fall → fell, go → went, choose → chose. Use it for what is already finished — the clocks that fell back on November 1, and the « as-if-finished » retellings on page 4. The November 3 election and the November 8 games are still to come at press time, so their results are not past yet.", 22.5)
cB.box("THE EXAMPLE · 예문", [
    ("« The clocks fell back on Sunday, November 1. » — fall → fell (page 2).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW)], 200, 1150, tag="P7-B2")
cC.head("LEVEL B2 · 도전", 27)
cC.head("HEADLINE PRESENT", 24)
cC.para("Headlines speak of yesterday in the present : « America votes », « Bengals play in Madrid ». The present simple makes old news feel live. Read the front page again and find three.", 22.5)
cC.head("WHETHER = IF ?", 24)
cC.para("« Nobody knows whether the race is called yet. » Whether introduces an open question inside a sentence — more elegant than if, and safe everywhere. It is the word for election-night uncertainty.", 22.5)
cC.box("THE EXAMPLE · 예문", [
    ("« Patience is part of the system, not a failure of it. » — part of = 일부분 (page 6).", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-tools")
cD.head("THE TOOLBOX · 도구 상자", 27)
cD.para("Three sentences to keep in your pocket, one for each level :", 22.5)
cD.para("A2 — « It is one o'clock — again ! »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « The clocks fell back on Sunday. »", 22.5)
cD.para("B2 — « Nobody knows whether the race is called yet. »", 22.5, "serif", True, OLIVE)
cD.para("And the newspaper reflex : every phrase of the week comes from an article of this issue. Re-read the article, and the phrase becomes easy.", 22.5)
cD.bridge("도구 상자 — 이번 호 휴대 문장 세 개, 단계마다 하나; 명문장은 전부 이번 호 기사에서 왔어요. 원문을 다시 읽는 게 가장 효과적이에요.")
cD.end_report()

# --- phrases of the week ---
py = 1210
p.hline(MX, RIGHT, py - 14, GOLD, 2)
p.text(MX, py + 26, "PHRASES OF THE WEEK · 이번 주의 명문장(전부 이번 호 기사에서)", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "문장마다 문법 포인트 하나 + 작은 문제 하나 · 정답은 8면에", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« Tuesday, November 3, is Election Day in the United States. » (page 1)",
     "문법 포인트 — is = 이다; 날짜가 주어 보어로 쓰여요.",
     "A2", "Election Day ___ on Tuesday, November 3. (be)", "is", "is = 이다"),
    ("« The hour from 1 to 2 happened twice. » (page 2)",
     "문법 포인트 — happen의 과거형은 happened, 규칙 변화예요.",
     "A2", "The hour ___ twice on Sunday. (happen)", "happened", "happen → happened"),
    ("« Which film would you choose ? » (page 3)",
     "문법 포인트 — would + 동사원형, 선택 의지예요.",
     "B1", "Which film ___ you choose ? (would)", "would", "would + 원형"),
    ("« Two games, two continents, one league — that is the modern NFL. » (page 4)",
     "문법 포인트 — that is = 그게 바로; 대시 뒤에 요약해요.",
     "B1", "That ___ the modern NFL. (be)", "is", "that is = 그게 바로"),
    ("« The results will still be there in the morning. » (page 5)",
     "문법 포인트 — will still = 여전히 ~할 것이다; still은 will 뒤에 와요.",
     "B2", "The results ___ still be there. (will)", "will", "will still = 여전히 ~할 것이다"),
    ("« Patience is part of the system, not a failure of it. » (page 6)",
     "문법 포인트 — part of = ~의 일부분; not은 부정 대조를 나타내요.",
     "B2", "Patience ___ part of the system. (be)", "is", "is part of = 일부분"),
    ("« Not every place changes. » (page 2)",
     "문법 포인트 — not every + 단수 동사: 모든 곳이 바뀌는 건 아니에요.",
     "A2", "Not every place ___ . (change)", "changes", "not every → changes"),
    ("« One Sunday is not enough — good thing the week has seven days. » (page 4)",
     "문법 포인트 — has = 가지다; the week은 단수라서 has를 써요.",
     "B1", "The week ___ seven days. (have)", "has", "have → has"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 20.5, "serif", True, INK, 1.34, 3)
    pf.bridge(point, 19, 4)
    pf.ex(lv, "따라 연습", key, note, q, size=20.5)
pf.end_report()

# --- bottom: clinic (left) + readers' corner & teaser (right) ---
by7 = 1870
p.hline(MX, RIGHT, by7 - 14, GOLD, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("THE ERROR CLINIC · 오류 클리닉", 25)
cf.bridge("문장마다 오류가 하나씩 있어요: 찾아서 고치세요.")
cf.ex("A2", "오류 고치기", "He doesn't like voting early.", "3인칭 단수 부정에는 doesn't + 동사원형",
     "✗ « He don't like voting early. »", instr="오류 고치기", size=22.5)
cf.ex("A2", "오류 고치기", "Yesterday the clocks fell back.", "fall의 과거형은 fell예요",
     "✗ « Yesterday the clocks falled back. »", instr="오류 고치기", size=22.5)
cf.ex("B1", "오류 고치기", "This game is bigger than last week's.", "bigger에는 이미 비교급이 들어 있어요, more를 더하지 마세요",
     "✗ « This game is more bigger than last week's. »", instr="오류 고치기", size=22.5)
cf.ex("B1", "오류 고치기", "She is going to watch the film on Friday.", "going to 뒤에는 동사원형",
     "✗ « She is going to watches the film on Friday. »", instr="오류 고치기", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(rx + 24, by7 + 48, "READERS' CORNER · 독자 코너", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)", 21.5, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 206, "편집부 알림｜VOL.1에서는 VOL.2에 실제 편지를 싣겠다고 약속했지만, 발행 때까지 실제 편지도 VOL.1 쓰기 투고도 도착하지 않았어요. 편지를 지어내지 않고 예시를 싣습니다. 여러분의 편지와 쓰기를 보내 주세요. VOL.3부터 실제 편지를 싣겠습니다.", 20, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 332
p.rect(rx, ty7, rw, 2540 - ty7, fill=DARK)
p.text(rx + 24, ty7 + 46, "NEXT WEEK · VOL.3 다음 호 예고", 24, "sans", True, "#f3edda")
p.para(rx + 24, ty7 + 84, "Wednesday, November 11 : Veterans Day. Sunday, November 15 : the NFL in Munich. And the midterm results, reported — who won, and what changes.", 21.5, "serif", False, "#e8dfc8", rw - 48, 1.45)
p.para(rx + 24, ty7 + 218, "다음 주 수요일 재향군인의 날, 일요일 NFL 뮌헨 경기, 그리고 중간선거 결과 보도.", 20, "sans", False, "#b3a06a", rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
