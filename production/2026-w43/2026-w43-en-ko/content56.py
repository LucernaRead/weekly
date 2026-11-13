# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("YOUTH　청년", "The Lucerna", "LEVEL B1　Screens, streams & new machines")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P5-main")
f.title("Opening Week Lives on Your Phone", 32)
f.byline("By The Lucerna newsroom　Reading level : B1")
f.head("THE GAME COMES TO YOU", 26)
f.para("For fifty years, a big game meant a television in the living room. This week, the NBA opened its season in a new way : opening night was built as a tripleheader for NBC — and for its streaming service, Peacock. Three games, one night, every screen in the house.")
f.para("Young fans do not always watch a whole game. Many meet the game first as a clip : forty seconds of the best moment, sent by a friend, watched on the bus. The full game comes later — or never. On Wednesday morning, one of the top trending searches in America was « lakers roster » : before watching the team, fans wanted the list of names. Who plays for the Lakers this year ?")
f.head("AI PLANS YOUR COSTUME", 26)
f.para("Halloween is the other screen story of the week. The NRF counts a new habit : 47% of celebrants now use AI tools to plan a costume or a decoration. You describe an idea — « a Greek god, but funny » — and the machine offers ten versions. Then the group chat votes.")
f.para("The costume itself is content now. A good costume is not finished when you put it on ; it is finished when the photo is posted. Google's Frightgeist list and the Spirit Halloween list agree on the stars of 2026 : KPop Demon Hunters, Toy Story 5, superheroes and Greek gods. This year, the gods have good lighting.")
f.head("EARNINGS, IN PLAIN ENGLISH", 25)
f.para("On Wednesday, after the markets close, two giants publish their numbers : Tesla and Meta. Netflix and SpaceX did the same on Tuesday. « Earnings » is a company's report card : how much money came in, how much went out, and what is left — the profit.")
f.para("For a few hours, every feed is green arrows and red arrows. One warning from our business desk : before the report, different experts give different numbers — nobody knows. After the close, everybody knows at the same time. That is the game, and this week, America is watching it live.")
f.head("THE SECOND SCREEN", 26)
f.para("Watch a game with young fans and you will see two games at once. On the television, the match. On the phone, the second match : live statistics, polls — « Who wins tonight ? » — and the group chat, where every goal, every basket, produces twenty messages in ten seconds. The phone does not kill the game. For this generation, the phone IS part of the game.")
f.para("The same phone plans the weekend. It holds the costume ideas, the AI pictures, the party address and the money for the pizza. One small glass rectangle runs the whole autumn : sport, money, festivals and friends. The Lucerna's advice ? Enjoy it — and sometimes, look up. The real game is also beautiful.")
f.gloss("to stream 스트리밍하다 · a highlight 하이라이트 · earnings 실적, 이익 · a feed 피드 · a roster 명단.")
f.head("A　CHOOSE　객관식", 25)
f.ex("B1", "객관식", "A", "개막일 밤 세 경기 연속 중계는 NBC와 Peacock",
     "The opening tripleheader was shown on... A. NBC and Peacock · B. FOX only · C. ESPN only", size=22.5)
f.ex("B1", "객관식", "A", "수요일 아침 인기 검색 스냅샷 중 하나",
     "On Wednesday morning, a top search was... A. lakers roster · B. world series tickets · C. tesla stock", size=22.5)
f.ex("B1", "객관식", "B", "47%가 AI로 분장과 장식을 계획해요",
     "47% of celebrants use AI to plan... A. their votes · B. costumes and decorations · C. their homework", size=22.5)
f.ex("B1", "객관식", "B", "Tesla와 Meta는 수요일 장 마감 뒤 실적 발표",
     "Tesla and Meta report their results... A. Monday morning · B. Wednesday after the close · C. Sunday night", size=22.5)
f.ex("B1", "객관식", "C", "실적 발표 전에는 전문가 수치가 제각각이에요",
     "Before a report, the experts' numbers... A. are all the same · B. are secret · C. differ from expert to expert", size=22.5)
f.head("B　SCREEN WORDS　화면 단어 빈칸", 24)
f.ex("A2", "문장 완성", "stream", "stream = 스트리밍으로 보기",
     "You can ___ the game live on your phone.", instr="빈칸 채우기", size=23)
f.ex("B1", "문장 완성", "highlights", "highlights = 하이라이트 장면",
     "No time for the full game ? Watch the ___ : three minutes of the best moments.", instr="빈칸 채우기", size=23)
f.ex("B1", "문장 완성", "viral", "go viral = 폭발적으로 퍼지다",
     "Her costume photo went ___ : a million people saw it in one day.", instr="빈칸 채우기", size=23)
f.ex("B1", "문장 완성", "roster", "roster = 팀 명단",
     "Before the season, fans study the ___ : who plays for the Lakers this year ?", instr="빈칸 채우기", size=23)
f.ex("B1", "문장 완성", "earnings", "earnings = 실적 발표",
     "Wednesday is ___ day for Tesla and Meta : the companies publish their numbers.", instr="빈칸 채우기", size=23)
f.ex("A2", "문장 완성", "feed", "feed = 피드",
     "His ___ is full of game clips and costume photos.", instr="빈칸 채우기", size=23)
f.head("C　THIS WEEK, LIVE　현재진행형", 25)
f.expl("현재진행형으로 바꿔 쓰세요: 이번 주에 일어나고 있는 일.")
f.ex("B1", "문장 바꾸기", "Tesla is reporting its results tonight.", "3인칭 단수 is + -ing",
     "Tesla (report) its results tonight. → ___", instr="바꿔 쓰기")
f.ex("B1", "문장 바꾸기", "The teams are playing 43 games this week.", "복수 are + -ing",
     "The teams (play) 43 games this week. → ___", instr="바꿔 쓰기")
f.ex("B1", "문장 바꾸기", "Fans are watching the tripleheader on their phones.", "fans → are watching",
     "Fans (watch) the tripleheader on their phones. → ___", instr="바꿔 쓰기")
f.ex("B1", "문장 바꾸기", "Milwaukee is preparing for Game 1.", "prepare → is preparing",
     "Milwaukee (prepare) for Game 1. → ___", instr="바꿔 쓰기")
f.head("D　TRUE OR FALSE ?　참 / 거짓", 25)
f.ex("B1", "읽기 판단", "True", "본문: 많은 젊은 팬이 먼저 짧은 영상으로 만나요",
     "1. Many young fans meet a game first as a short clip.", instr="참 / 거짓", size=23)
f.ex("B1", "읽기 판단", "False", "실적 발표 전에는 아무도 수치를 몰라요",
     "2. Everybody knows Tesla's numbers before Wednesday's report.", instr="참 / 거짓", size=23)
f.ex("B1", "읽기 판단", "False", "순위는 구글 Frightgeist와 상점 두 곳에서 나와요",
     "3. The costume lists come only from shops.", instr="참 / 거짓", size=23)
f.end_report()

# col 3
ix = COLX[3]
v5 = Flow(p, [(ix, CW)], 200, 2560, tag="P5-col3")
v5.box("WORDS OF THE SCREEN　화면 단어장", [
    ("to stream — 스트리밍, 온라인으로 보다", "serif", False, INK, 21.5, 1.5),
    ("a highlight — 하이라이트, 명장면 모음", "serif", False, INK, 21.5, 1.5),
    ("a clip — 짧은 영상", "serif", False, INK, 21.5, 1.5),
    ("a feed — 피드, 새 글 모아보기", "serif", False, INK, 21.5, 1.5),
    ("viral — 폭발적으로 퍼지는 (go viral 퍼지다)", "serif", False, INK, 21.5, 1.5),
    ("a roster — 명단", "serif", False, INK, 21.5, 1.5),
    ("earnings — 실적 발표, 이익", "serif", False, INK, 21.5, 1.5),
    ("to post — 글을 올리다, 게시하다", "serif", False, INK, 21.5, 1.5),
], tsize=21)
v5.box("SAY IT ONLINE　온라인 한마디", [
    ("« What a game ! » — 정말 멋진 경기예요!", "serif", False, INK, 21.5, 1.45),
    ("« Send me the highlights. » — 하이라이트 보내 줘요.", "serif", False, INK, 21.5, 1.45),
    ("« This costume wins Halloween. » — 이 분장이 할로윈을 다 가져갔어요.", "serif", False, INK, 21.5, 1.45),
])
v5.box("THE WORLD GAME AT 4 P.M.", [
    ("On Sunday at 4 p.m. Eastern, American screens turn to Spain : Barcelona vs Real Madrid, on ESPN. In one Wednesday snapshot, it was America's number one search. The world's game needs no translation.", "serif", False, INK, 21.5, 1.45),
    ("일요일 동부 시간 오후 4시 엘 클라시코, ESPN 중계; 수요일 스냅샷에서 미국 검색 1위였어요.", "sans", False, GREY, 20.5, 1.4),
])
v5.box("PLAN YOUR STREAMING WEEK", [
    ("Tue — the NBA tripleheader, on Peacock", "serif", False, INK, 21.5, 1.45),
    ("Wed — Tesla & Meta numbers, after the close", "serif", False, INK, 21.5, 1.45),
    ("Fri — World Series Game 1 · Sat — Game 2", "serif", False, INK, 21.5, 1.45),
    ("Sun — Austin Grand Prix · El Clásico, 4 p.m. ET", "serif", False, INK, 21.5, 1.45),
])
v5.box("NEXT WEEK ON YOUR SCREENS", [
    ("Mon–Tue — the Series moves to Tampa · Sat Oct 31 — Halloween night · Sun Nov 1 — the clocks fall back · Tue Nov 3 — election night. The autumn does not slow down.", "serif", False, INK, 21.5, 1.45),
])
v5.box("THE DEBATE　토론", [
    ("Is a forty-second clip really « watching the game » ? Or is the full game a thing of the past ? Two sentences, in English, to the newsroom — the best answers appear on page 7 of VOL.2.", "serif", False, INK, 21.5, 1.45),
])
v5.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jeunesse.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("IN DEPTH　시사 심층", "The Lucerna", "LEVEL B2　The 2026 midterms　2026 중간선거")

a6 = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 200, 1420, tag="P6-article")
a6.title("The Midterms : Why America Votes Early", 32)
a6.byline("By The Lucerna newsroom　Reading level : B2")
a6.para("On Tuesday, November 3, Americans vote in the midterm elections — the elections that fall in the middle of a president's term. There is no presidential race this year. Instead, voters choose the whole House of Representatives, part of the Senate, and most state governors. It is a smaller election than 2024, but in Washington, it changes everything.", 24)
a6.para("The stakes fit in one line of numbers : the House today stands at 218 Republicans to 214 Democrats, according to Reuters — a margin of four seats. A handful of districts will decide who controls Congress for the next two years. That is why the advertising never stops : spending on election ads had already reached a record 3.8 billion dollars by October 12, the analytics firm AdImpact reported.", 24)
a6.para("The newest fact of American elections is the calendar. Voting is no longer a day ; it is a season. Nurses, drivers, soldiers and parents often cannot queue for hours on a Tuesday, so states let them vote early, in person, with the same ballot. This year's wave opened on Monday, October 19, in Texas — early voting there runs to October 30 — and in Alaska, Arkansas, Connecticut and Colorado.", 24)
a6.para("Louisiana and Missouri followed on Tuesday, Delaware and Maryland on Thursday, and Michigan and Florida's mandatory period begins on Saturday, October 24. Fifty states, fifty calendars : in the United States, elections are run by the states, not by Washington, and every state keeps its own doors and its own hours.", 24)
a6.para("Early voting changes the campaign, too. Parties no longer aim everything at one Tuesday ; they aim at October. But one rule protects the suspense : early votes are counted under state rules, and the results, as always, arrive on election night. Voting early does not mean knowing early.", 24)
a6.gloss("midterm (elections) 중간선거 · the House 하원 · incumbent 현직자 · margin 격차 · turnout 투표율.")
a6.end_report()

# col 2 rail
r6rail = Flow(p, [(COLX[2], CW)], 200, 1420, tag="P6-rail")
r6rail.box("THE EARLY-VOTING WEEK", [
    ("Mon, Oct 19 — Texas, Alaska, Arkansas, Connecticut and Colorado open", "serif", False, INK, 21.5, 1.48),
    ("Tue, Oct 20 — Louisiana and Missouri follow", "serif", False, INK, 21.5, 1.48),
    ("Thu, Oct 22 — Delaware and Maryland open", "serif", False, INK, 21.5, 1.48),
    ("Sat, Oct 24 — Michigan opens ; Florida's mandatory period begins", "serif", False, INK, 21.5, 1.48),
    ("Fri, Oct 30 — early voting closes in Texas", "serif", False, INK, 21.5, 1.48),
    ("Tue, Nov 3 — ELECTION DAY", "serif", True, INK, 21.5, 1.48),
])
r6rail.box("HOW TO FOLLOW IT　따라가는 법", [
    ("Watch three numbers, not three hundred opinions : the turnout (how many vote), the House margin (218–214 today) and the ad money ($3.8 billion and counting). The rest is noise.", "serif", False, INK, 21.5, 1.45),
    ("선거는 세 숫자만 보세요: 투표율, 하원 격차, 광고비. 나머지는 대부분 소음이에요.", "sans", False, GREY, 20.5, 1.4),
])
r6rail.end_report()

# col 3 sidebar
ix = COLX[3]
image(p, "capitol.jpg", ix, 200, CW, 186)
cy6 = caption(p, ix, 386, CW, "The Capitol in Washington : control of Congress is the prize on November 3.",
              "United States Capitol — public domain")
s6 = Flow(p, [(ix, CW)], int(cy6) + 16, 1420, tag="P6-side")
s6.box("ELECTION WORDS　선거 단어장", [
    ("a midterm — 중간선거", "serif", False, INK, 21.5, 1.5),
    ("an incumbent — 현직자", "serif", False, INK, 21.5, 1.5),
    ("a margin — (표/의석) 격차", "serif", False, INK, 21.5, 1.5),
    ("turnout — 투표율", "serif", False, INK, 21.5, 1.5),
    ("a campaign — 선거 운동", "serif", False, INK, 21.5, 1.5),
    ("a district — 선거구", "serif", False, INK, 21.5, 1.5),
])
s6.box("HEADLINE LANGUAGE　헤드라인 언어", [
    ("« Early voting opens » — 사전투표 시작", "serif", False, INK, 21, 1.45),
    ("« voters head to the polls » — 유권자들이 투표소로 향해요", "serif", False, INK, 21, 1.45),
    ("« too close to call » — 너무 접전이라 예측 불가", "serif", False, INK, 21, 1.45),
], tsize=21)
s6.end_report()

# ---- practice chart (span cols 0-1) ----
chy = 1456
p.hline(MX, RIGHT, chy - 12, OLIVE, 2)
chx, chw = COLX[0], 2 * CW + GUT
p.text(chx, chy + 28, "WHY DO VOTERS VOTE EARLY ?　연습 도표", 26, "sans", True, OLIVE)
p.para(chx, chy + 58, "PRACTICE DATA — simplified and invented for this exercise ; not a real survey. 연습용 자료예요 — 실제 조사가 아니에요.", 18.5, "sans", False, OLIVE, 820.0, 1.3)
p.rect(chx, chy + 96, chw, 336, fill=BOX)
rows = [
    ("To avoid the long lines", 34, OLIVE),
    ("I work on Election Day", 27, OLIVE),
    ("I want it done early", 23, OLIVE),
    ("I will travel on Nov 3", 16, OLIVE),
]
byy = chy + 116
for lab, val, col in rows:
    p.text(chx + 24, byy + 24, lab, 22, "serif", True, INK)
    p.rect(chx + 24, byy + 36, val * 11, 24, fill=col)
    p.text(chx + 34 + val * 11, byy + 56, f"{val}%", 21, "sans", True, OLIVE)
    byy += 82
p.text(chx + 24, byy + 8, "Four answers, 100 voters. 네 가지 답, 모두 100명이에요.", 19, "sans", False, GREY)

# ---- chart questions (cols 0-1) ----
q6 = Flow(p, [(COLX[0], CW), (COLX[1], CW)], chy + 470, 2560, tag="P6-chart-ex")
q6.head("READING THE CHART　도표 읽기", 24)
q6.ex("B2", "도표 읽기", "C", "가장 큰 이유는 긴 줄 피하기 34%",
     "The biggest reason is... A. travel · B. work · C. avoiding long lines", size=22)
q6.ex("B2", "도표 읽기", "27", "선거일에 일하는 사람: 27명",
     "Out of 100 voters, how many work on Election Day ?", size=22)
q6.ex("B1", "도표 읽기", "61%", "34 + 27 = 61",
     "The top two reasons together make ___ of the voters.", size=22)
q6.ex("B2", "도표 읽기", "False", "27 + 16 = 43, 절반이 안 돼요",
     "True or false : more than half vote early because of work or travel.", size=22)
q6.ex("B1", "도표 읽기", "18 points", "34 − 16 = 18퍼센트포인트",
     "The difference between « lines » and « travel » is ___.", size=22)
q6.ex("B1", "도표 읽기", "100%", "네 항목 합계 100%",
     "All four answers together make ___ of the voters.", size=22)
q6.box("KEY SENTENCE　핵심 문장", [
    ("« Voting is no longer a day ; it is a season. »", "serif", False, INK, 21.5, 1.45),
    ("투표는 이제 하루가 아니라 한 계절이에요. — 이 면 심층 읽기의 핵심 문장.", "sans", False, GREY, 20.5, 1.4),
])
q6.end_report()

# ---- right exercises (cols 2-3) ----
r6 = Flow(p, [(COLX[2], CW), (COLX[3], CW)], chy + 14, 2560, tag="P6-ex")
r6.head("READING　읽기 객관식", 24)
r6.ex("B2", "객관식", "B", "중간선거가 의회 주도권을 결정해요",
     "The midterms decide... A. the president · B. control of Congress · C. the Supreme Court", size=22)
r6.ex("B2", "객관식", "B", "미국 선거는 각 주가 운영해요",
     "Elections in the US are run by... A. the White House · B. the states · C. the parties", size=22)
r6.ex("B2", "객관식", "B", "38억 달러는 10월 12일까지의 광고비",
     "The $3.8 billion is... A. the cost of voting machines · B. ad spending by Oct 12 · C. the price of ballots", size=22)
r6.ex("B2", "객관식", "C", "플로리다 의무 기간은 10월 24일 토요일 시작",
     "Florida's mandatory early voting starts... A. Oct 19 · B. Oct 22 · C. Oct 24", size=22)
r6.head("COMPARATIVES　비교급", 24)
r6.ex("B2", "문장 완성", "more convenient", "convenient는 more를 써요",
     "Early voting is ___ (convenient) than voting on one day only.", instr="빈칸 채우기", size=22)
r6.ex("B1", "문장 완성", "highest", "record = 역대 최고",
     "Ad spending this year is the ___ (high) ever.", instr="빈칸 채우기", size=22)
r6.ex("B1", "문장 완성", "earlier", "텍사스 10월 19일이 플로리다 24일보다 빨라요",
     "Texas starts ___ (early) than Florida.", instr="빈칸 채우기", size=22)
r6.ex("B2", "문장 완성", "smaller", "218 − 214 = 4 < 10",
     "The House margin (218–214) is ___ (small) than ten seats.", instr="빈칸 채우기", size=22)
r6.head("ELECTION WORDS　선거 단어 빈칸", 24)
r6.ex("B2", "문장 완성", "incumbent", "incumbent = 현직자",
     "The ___ is the person who holds the job now and wants to keep it.", instr="빈칸 채우기", size=22)
r6.ex("B2", "문장 완성", "margin", "margin = 격차",
     "218 to 214 is a ___ of four seats.", instr="빈칸 채우기", size=22)
r6.ex("B2", "문장 완성", "turnout", "turnout = 투표율",
     "A high ___ means many people vote.", instr="빈칸 채우기", size=22)
r6.ex("B2", "문장 완성", "campaign", "campaign = 선거 운동",
     "A ___ is the long season of work before an election.", instr="빈칸 채우기", size=22)
r6.box("SAY IT LIKE A HEADLINE", [
    ("« Early voters ___ to the polls in Texas. » (head)", "serif", False, INK, 21, 1.45),
    ("« The race is too ___ to call. » (close)", "serif", False, INK, 21, 1.45),
    ("« Turnout is ___ this year. » (up)", "serif", False, INK, 21, 1.45),
    ("신문 헤드라인 세 문장, 빈칸을 채워 직접 말해 보세요 — 답은 일상 표현 안에 있어요.", "sans", False, GREY, 20.5, 1.4),
])
r6.end_report()
p.foot(6)
p.save(f"{OUT}/p6-politique.svg")
print("P6 saved, exercises so far:", len(REG))
