# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · FRONT PAGE (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 4", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "WEEKLY IN ENGLISH　매주 한 번　영어권에서 지금 화제가 되는 일 읽기", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "WEEK OF NOVEMBER 16 TO 22, 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "The Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "영어 주간지　VOL.4　선거　정글　영화", 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)
p.text(975, 372, "영어 텍스트　한국어 해설 — 한국어 독자를 위한 판", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# dark band: midterms
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "DEMOCRATS WIN BOTH HOUSES!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Tuesday, November 3: America voted. By Sunday, November 8, the count was clear.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "11월 3일 투표　민주당이 양원에서 승리", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "중간 선거　발표된 결과　6면 참조", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "THE BIG STORY　헤드라인", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Democrats Win the House and the Senate", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "By The Lucerna newsroom　Reading level: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("On Tuesday, November 3, Americans voted in the midterm election — for all 435 seats in the House of Representatives, for 35 seats in the Senate, and for governor in 36 states. By Sunday, November 8, the count was clear enough to call: the Democrats won the House, and the Democrats won the Senate.")
f.para("The numbers, as called by the Associated Press on Sunday, November 8: in the House, 254 seats for the Democrats and 162 for the Republicans, with 19 races still uncalled. The majority is 218. In the Senate, the Democrats won 20 of the 33 races called, and the Republicans 13, with two races — in Alaska and Mississippi — still uncalled.")
f.para("Before the vote, the Republicans held the House, 218 seats to 214, and the Senate, 53 to 47. On election night, seven Senate seats changed hands — in Iowa, Kansas, Maine, North Carolina, Ohio, South Carolina and Texas — and all seven went to the Democrats. Five governors' offices changed hands too: Georgia, Iowa, Nevada, Ohio and Texas.")
f.para("A “call” is not the official result. News organisations call a race when the maths is clear. The official result comes later, when each state checks its count and certifies it — between November 10 and December 18. Until then, the numbers can still move a little. Page 6 explains how to read them.")
f.para("The new Congress meets in January 2027. Until then, the old Congress finishes its work — and the winners plan theirs. This week also brings the jungle back to television, a look back at last year's Ashes, and a new Hunger Games film to the cinema. Welcome back to VOL.4!")
f.bridge("해설 — a midterm = 중간 선거 · to call a race = 선거 결과를 발표하다 · a seat = 의석。")
f.box("THE WEEK IN NUMBERS　숫자", [
    ("Nov 3 — the vote（투표일） · 254–162 — the House, as called on Nov 8（하원）", "serif", False, INK, 20.5, 1.35),
    ("218 — the majority（과반수） · 7 — Senate seats that changed hands（정당이 바뀐 상원 의석）", "serif", False, INK, 20.5, 1.35),
])
f.head("TRY IT NOW　바로 연습", 25)
f.ex("A2", "문장 완성", "midterm", "midterm = 중간 선거",
     "Americans voted in the ___ election on November 3.", size=20.5)
f.ex("A2", "문장 완성", "call", "call a race = 선거 결과를 발표하다",
     "News organisations ___ a race when the maths is clear.", size=20.5)
f.ex("A2", "문장 완성", "seats", "seat = 의석",
     "All 435 ___ in the House were on the ballot.", size=20.5)
f.ex("A2", "문장 완성", "majority", "majority = 과반수",
     "The ___ in the House is 218 seats.", size=20.5)
f.ex("B1", "문장 완성", "changed", "change hands = 정당이 바뀌다",
     "Seven Senate seats ___ hands on election night.", size=20.5)
f.ex("B1", "문장 완성", "January", "새 의회는 2027년 1월에 개회한다",
     "The new Congress meets in ___ 2027.", size=20.5)
f.end_report()

# ---- searches chart (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 668, fill=BOX)
p.text(gx + 22, gy + 40, "SEARCHES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "OF THE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "이번 주 영어권 인기 검색어　Google Trends", 19, "sans", False, GREY)
gt = [
    ("midterm results", 250),
    ("thanksgiving", 218),
    ("hunger games", 186),
    ("i'm a celebrity", 140),
    ("anti-bullying week", 108),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE)
    byy += 86  # fix1: was 92 — last footnote baseline sat at 1274, 18px
    # below the box bottom (1256); step 86 pulls the footnotes to
    # baselines 1184/1210/1244, last ink ~1247, inside the box.
p.text(gx + 22, byy + 16, "Snapshots, early November:", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "search interest changes during the day.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "상대적 인기 표시예요, 정확한 수치 아니에요.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1280
p.rect(gx, sy, gw, 372, fill="#f0eee5")
p.text(gx + 22, sy + 40, "IN THIS ISSUE　이번 호 목차", 24, "sans", True, OLIVE)
som = [
    ("p.2", "After the vote: what now?", "A2"),
    ("p.3", "Haymitch in the arena", "A2→B1"),
    ("p.4", "Perth, Turin & football", "B1"),
    ("p.5", "Break the silence", "B1"),
    ("p.6", "Reading the results", "B2"),
    ("p.7", "Phrases of the week", "A2→B2"),
    ("p.8", "Exercises & answers", "all"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 72, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "THE WORD OF THE WEEK", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "“midterm”", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "an election in the middle of a president's four-year term.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "중간 선거: 하원은 전 의석, 상원은 3분의 1。", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1862, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "capitol.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "The United States Capitol in Washington, D.C. — the home of Congress. The new Congress, with a Democratic House and a Democratic Senate, meets in January 2027.",
        "Noclip — public domain, via Wikimedia Commons")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-countries")
f2.head("TWO HOUSES, ONE MAP", 25)
f2.para("One country, two houses. The House of Representatives has 435 seats, and all of them were on the ballot. The Senate has 100 seats, and 35 were on the ballot. That is why the map changed in one night — and why it will take weeks to finish.", 22.5)
f2.para("Read page 6 for the full map — and the numbers behind it.", 22.5)
f2.end_report()
# col 3 IN BRIEF
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX)
p.text(bx + 22, 1914, "IN BRIEF　단신", 24, "sans", True, OLIVE)
brefs = [
    ("ELECTION", "Nov 3: America voted. Democrats win both houses, as called on Nov 8. (p. 6)"),
    ("JUNGLE", "Mon, Nov 16, 9 p.m.: I'm a Celebrity returns to ITV1. (p. 3)"),
    ("ASHES", "A year ago: Australia beat England 4–1 in the 2025–26 Ashes. (p. 4)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "LIGHTNING QUIZ　번개 퀴즈", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "1면을 읽고 정답을 고르세요　정답은 8면에", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "객관식", "B", "민주당은 하원에서 254석을 차지했다（11월 8일 발표 수）",
      "The Democrats won the House with... A. 218 seats called · B. 254 seats called · C. 162 seats called", size=21)
qf.ex("A2", "객관식", "A", "투표일은 11월 3일 화요일",
      "The midterm vote was on... A. Tuesday, November 3 · B. Sunday, November 8 · C. Monday, November 16", size=21)
qf.ex("A2", "객관식", "C", "하원 과반수는 218석",
      "A majority in the House is... A. 100 seats · B. 435 seats · C. 218 seats", size=21)
qf.ex("A2", "객관식", "C", "새 의회는 2027년 1월에 개회한다",
      "The new Congress meets in... A. November · B. December · C. January 2027", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LIFE　생활", "The Lucerna", "LEVEL A2　After the vote　투표 뒤에")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("The Week After the Vote: What Happens Now?", 32)
f.byline("By The Lucerna newsroom　Reading level: A2")
f.para("The vote is over. The counting is not. On Monday, November 9, the day this issue went to press, election workers in many states were still opening mail ballots and checking signatures. In Alaska and Mississippi, the Senate races were still too close to call.")
f.para("What happens next? First, the states certify their counts — between November 10 and December 18. Georgia law calls for a runoff on December 1 only if no candidate wins a majority — but Jon Ossoff won reelection with about 59% of the vote, so there is no runoff. Mississippi has no runoff: the most votes win. Then the winners are sworn in, and the new Congress meets in January 2027.")
f.para("In Washington, the parties choose their leaders. The Republicans in the House vote on Tuesday, November 10. The Democrats in the House vote on November 18 and 19. The Speaker — the leader of the House — is chosen when the new Congress meets in January. The Speaker, Mike Johnson, has said he will not run to lead the Republicans in the new Congress.")
f.head("TWO HOUSES, TWO JOBS", 25)
f.para("Why two houses? The House of Representatives has 435 seats, and every seat is on the ballot every two years. The Senate has 100 seats, and about a third of them are on the ballot each time. A senator serves for six years. A member of the House serves for two. That is why the House changes fast, and the Senate changes slowly.")
f.box("SENATE IN NUMBERS　상원", [
    ("100 — seats in the Senate. 35 — seats on the ballot on November 3. 6 — years in a senator's term.", "serif", False, INK, 21.5, 1.4),
])
f.para("Life goes on around the politics. Next week is Thanksgiving week in America. Thanksgiving Day is Thursday, November 26 — a day for family, for a big dinner, and for the turkey. Many families travel home, and the Friday after it, November 27, is Black Friday, the biggest shopping day of the year.")
f.para("And in Britain? The week is quieter — but the television is not. On Monday, November 16, at 9 p.m., the jungle opens again: I'm a Celebrity is back on ITV1. Page 3 has the story — and the words you need for the jungle.")
f.box("THE CALENDAR　이번 주 달력", [
    ("11월 10일 — 공화당이 대표를 뽑다 · 11월 18–19일 — 민주당이 투표하다", "serif", False, INK, 21.5, 1.4),
    ("11월 20일 — 세계 아동의 날 · 11월 26일 — 추수감사절 · 11월 27일 — 블랙프라이데이", "serif", False, INK, 21.5, 1.4),
])
f.head("WHAT IS ON THIS WEEK?", 25)
f.para("Second story of the week — and it is on your screen. On Friday, November 20, the new Hunger Games film opens in cinemas, and the ATP Finals end in Turin on Sunday, November 22. On Saturday, November 21, the Premier League is back — and page 4 looks back at the Ashes. Page 3 has the film guide, page 4 the sport.", 23.5)
f.para("On television, the week is just as full. I'm a Celebrity opens on Monday night, and the jungle will be on every night for weeks. Thanksgiving is a week away — and the turkey is already in the shops.", 23.5)
f.para("How do you say the date of the new Congress? “In January 2027.” is the sentence of the week. The phrase box below shows three ways to say it.", 23.5)
f.gloss("to certify = 공식 확인하다 · a runoff = 결선 투표.")
f.end_report()

# col 3: image + facts (sequential, measured)
ix = COLX[3]
image(p, "turkey.jpg", ix, 200, CW, 440)
cy3 = caption(p, ix, 640, CW, "A wild turkey, drawn by John James Audubon. The turkey is the bird of Thanksgiving — on Thursday, November 26, it is the centre of the American dinner table.",
              "John James Audubon — public domain, via Wikimedia Commons")
sav = ["The new Congress meets in January 2027 — two months after the vote.",
       "Thanksgiving is always the fourth Thursday of November.",
       "The House has 435 seats — and every one of them was on the ballot on November 3."]
sy3 = cy3 + 24
sh = 89 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in sav) + 14
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DID YOU KNOW?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "And you? What happens after an election in your country? Who counts the votes, and how long does it take? Write three sentences in English for VOL.5."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("당신의 나라에서는 선거 뒤에 무슨 일이 일어나나요? 영어 세 문장을 써서 편집부에 보내세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "AND YOU?　당신은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "당신의 나라에서는 선거 뒤에 무슨 일이 일어나나요? 영어 세 문장을 써서 편집부에 보내세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Say it wide box ----
dy = 1570
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "SAY IT: IN JANUARY 2027　날짜를 말하는 법", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "The new Congress, in three sentences　새 의회를 세 문장으로", 20, "sans", False, GREY, anchor="end")

def phrase_panel(cx, label, sub, w=280):
    p.rect(cx - w // 2, dy + 66, w, 132, fill="#f0eee5")
    p.text(cx, dy + 126, label, 20, "serif", True, INK, anchor="middle")
    p.text(cx, dy + 168, sub, 20, "sans", False, GREY, anchor="middle")

phrase_panel(299, "The counting continues.", "개표가 아직 계속되고 있다.")
phrase_panel(750, "The new Congress meets in January.", "새 의회는 1월에 개회한다.", w=380)
phrase_panel(1200, "Happy Thanksgiving!", "추수감사절 잘 보내세요!")
lx = 1370
ly = dy + 66
for line in [
    ("to certify", "= to confirm（공식 확인하다）"),
    ("a runoff", "= a second vote（결선 투표）"),
    ("sworn in", "= to take the oath（선서하다）"),
    ("a turkey", "= the bird of Thanksgiving（칠면조）"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 140, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 40
p.para(lx, ly + 24, "This week: on Monday, November 9, this issue went to press. The numbers in it are the calls of Sunday, November 8 — and the counting goes on.", 19, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 340
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCISES　2면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에　문제는 단계를 넘나들어요, 번호로 정답을 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P2-ex")
e.head("A　THE DATE", 25)
e.bridge("날짜와 시간에 따라 영어로 문장을 완성하세요.")
e.ex("A2", "문장 완성", "November", "11월 = November",
     "The vote was on Tuesday, ___ 3.", instr="빈칸 채우기", size=22)
e.ex("A2", "문장 완성", "January", "새 의회는 2027년 1월에 개회한다",
     "The new Congress meets in ___ 2027.", instr="빈칸 채우기", size=22)
e.ex("A2", "문장 완성", "1", "결선 투표 12월 1일",
     "A runoff, if needed, is on December ___.", instr="빈칸 채우기", size=22)
e.ex("A2", "문장 완성", "Thursday", "추수감사절은 목요일",
     "Thanksgiving is on ___, November 26.", instr="빈칸 채우기", size=22)
e.ex("A2", "문장 완성", "27", "블랙프라이데이는 11월 27일",
     "Black Friday is on November ___.", instr="빈칸 채우기", size=22)
e.head("B　WILL", 25)
e.bridge("will + 동사로 바꿔 쓰세요(약속)。")
e.ex("A2", "문장 바꾸기", "The new Congress will meet in January.", "meet → will meet",
     "The new Congress (meet) in January. → ___", instr="바꿔 쓰기")
e.ex("A2", "문장 바꾸기", "States will certify their counts.", "certify → will certify",
     "States (certify) their counts. → ___", instr="바꿔 쓰기")
e.ex("A2", "문장 바꾸기", "Families will travel home.", "travel → will travel",
     "Families (travel) home for Thanksgiving. → ___", instr="바꿔 쓰기")
e.ex("B1", "문장 바꾸기", "Will they watch the jungle on Monday?", "의문문: will을 앞으로",
     "They (watch) the jungle on Monday? → ___", instr="바꿔 쓰기")
e.head("C　COMPREHENSION", 25)
e.bridge("2면 기사를 읽고 정답을 고르세요.")
e.ex("A2", "객관식", "B", "각 주의 확인은 11월 10일부터 12월 18일까지",
     "Certification runs... A. Nov 3–9 · B. Nov 10–Dec 18 · C. Jan–Feb", size=22)
e.ex("A2", "객관식", "C", "결선 투표는 12월 1일",
     "A runoff, if needed, is on... A. November 10 · B. November 26 · C. December 1", size=22)
e.ex("A2", "객관식", "A", "추수감사절은 11월 26일 목요일",
     "Thanksgiving Day is... A. Thu, Nov 26 · B. Fri, Nov 27 · C. Mon, Nov 16", size=22)
e.ex("A2", "객관식", "B", "정글 프로그램은 11월 16일 월요일 밤 9시에 시작한다",
     "I'm a Celebrity returns on... A. Sun, Nov 15 · B. Mon, Nov 16 · C. Fri, Nov 20", size=22)
e.head("D　THE WORDS", 25)
e.match_set("A2", "단어 짝짓기",
            ["a runoff", "to certify", "a turkey", "Thanksgiving"],
            ["the bird of the Thanksgiving dinner",
             "a second vote, when nobody wins",
             "to confirm a count officially",
             "the American family holiday"],
            ["b", "c", "a", "d"],
            ["runoff = 결선 투표 b", "certify = 공식 확인하다 c", "turkey = 칠면조 a", "Thanksgiving = 추수감사절 d"],
            instr="단어와 뜻 짝짓기")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-life.svg")
print("P2 saved, exercises so far:", len(REG))
