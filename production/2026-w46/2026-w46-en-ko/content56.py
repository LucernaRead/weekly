# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-en-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("YOUTH · 청년", "The Lucerna", "LEVEL B1 · Pudsey, 26 & kindness · 퍼지, 26 그리고 친절")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P5-main")
f.title("Friday, November 13 : Pudsey, 26 and Kindness", 37)
f.byline("By The Lucerna newsroom · Reading level : B1")
f.para("On Friday, November 13, Britain turns yellow. It is the BBC Children in Need appeal show, live from Salford, on BBC One and iPlayer — a night of music, comedy and stories, to raise money for children and young people across the UK. The star is a yellow bear with a spotted bandage over one eye : Pudsey Bear.")
f.para("This year's idea is simple : Challenge Yourself 2026. Take on a challenge inspired by the number 26 — 26 miles, 26 cakes, 26 songs. Run with Pudsey and Joe Wicks asks people to walk, run or roll two miles a day for two weeks, until they reach a marathon. Every mile, every pound, helps a child who needs someone by their side.")
f.para("The presenters are Alex Jones, Sara Cox, Rylan and Mel Giedroyc, with Tyler West. Schools join in too : in the week of November 9, children run, bake and dress up, and the money goes to projects near their homes. One night, one bear, thousands of small challenges.")
f.para("Friday, November 13, is also World Kindness Day. Kindness is the week's other word : a small act, a kind message, help for a stranger. On social media, young people post their 26 challenges with the same sentence : « Challenge yourself — and be kind. » That is the most repeated sentence of the week.")
f.para("And the children ? They watch Pudsey, and they ask the best questions : « Why does Pudsey wear a bandage ? » « Can we do 26 too ? » « How much money will we raise ? » The answer to the last question is : we will know on Friday night. The total will still be there in the morning — and so will the kindness.")
f.box("26, IN NUMBERS · 숫자 26", [
    ("26 miles is a marathon, more or less. Two miles a day adds up to 26 — that is why the number is 26. One challenge, one number, thousands of children helped.", "serif", False, INK, 21.5, 1.4),
])
f.para("If you want to practise Friday-night English, try this : watch ten minutes of the appeal show in English, and write down five sentences you hear. « Challenge yourself » will certainly be one of them. The other four are your homework.")
f.gloss("an appeal 모금 호소 · a challenge 도전 · to raise money 모금하다 · kindness 친절.")
f.head("A · COMPREHENSION", 25)
f.bridge("5면 기사를 읽고 정답을 고르세요.")
f.ex("B1", "객관식", "B", "모금 갈라쇼 11월 13일 금요일",
     "The Children in Need appeal show is on... A. Wednesday, November 11 · B. Friday, November 13 · C. Sunday, November 15", size=22)
f.ex("B1", "객관식", "A", "퍼지는 노란 곰이에요",
     "Pudsey Bear is... A. a yellow bear · B. a red poppy · C. a footballer", size=22)
f.ex("B1", "객관식", "C", "도전은 숫자 26에서 영감을 받았어요",
     "Challenge Yourself 2026 is inspired by... A. 11 · B. 13 · C. 26", size=22)
f.ex("B1", "객관식", "B", "매일 2마일",
     "Run with Pudsey asks for... A. one mile a day · B. two miles a day · C. 26 miles a day", size=22)
f.ex("B1", "객관식", "A", "모금 갈라쇼는 솔퍼드에서 생방송돼요",
     "The appeal show is live from... A. Salford · B. Munich · C. Turin", size=22)
f.ex("B1", "객관식", "C", "11월 13일은 세계 친절의 날이기도 해요",
     "Friday, November 13, is also... A. Veterans Day · B. Diwali · C. World Kindness Day", size=22)
f.head("B · SENTENCES", 25)
f.bridge("주어진 단어로 문장을 완성하세요.")
f.ex("B1", "문장 완성", "challenge", "challenge = 도전",
     "Take on a ___ inspired by 26.", instr="빈칸 채우기")
f.ex("B1", "문장 완성", "raise", "raise money = 모금하다",
     "The show helps to ___ money for children.", instr="빈칸 채우기")
f.ex("A2", "문장 완성", "kind", "kind = 친절한",
     "Be ___ : help a stranger today.", instr="빈칸 채우기")
f.ex("A2", "문장 완성", "live", "live = 생방송의",
     "The show is ___ from Salford.", instr="빈칸 채우기")
f.head("C · THE WORDS", 25)
f.match_set("B1", "단어 짝짓기",
            ["an appeal", "a challenge", "kindness", "a marathon"],
            ["being kind to other people",
             "a race of about 26 miles",
             "a public call for help and money",
             "a hard task you take on"],
            ["c", "d", "a", "b"],
            ["appeal = 모금 호소 c", "challenge = 도전 d", "kindness = 친절 a", "marathon = 마라톤 b"],
            instr="단어와 뜻 짝짓기")
f.head("D · PRESENT CONTINUOUS", 25)
f.bridge("현재진행형으로 바꿔 쓰세요(지금 일어나는 일).")
f.ex("B1", "문장 바꾸기", "Children are running two miles today.", "run → are running",
     "Children (run) two miles today. → ___", instr="바꿔 쓰기")
f.ex("B1", "문장 바꾸기", "Schools are baking 26 cakes this week.", "bake → are baking",
     "Schools (bake) 26 cakes this week. → ___", instr="바꿔 쓰기")
f.ex("B1", "문장 바꾸기", "We are watching Pudsey tonight.", "watch → are watching",
     "We (watch) Pudsey tonight. → ___", instr="바꿔 쓰기")
f.ex("B1", "문장 바꾸기", "She is raising money for children.", "raise → is raising",
     "She (raise) money for children. → ___", instr="바꿔 쓰기")
f.end_report()

# col 3: side flow
ix = COLX[3]
v5 = Flow(p, [(ix, CW)], 200, 2540, tag="P5-col3")
v5.box("FIVE SENTENCES · 다섯 문장 과제", [
    ("Watch ten minutes of the appeal show in English. Write down five sentences you hear. « Challenge yourself » will be one of them.", "serif", False, INK, 21.5, 1.42),
])
v5.head("FRIDAY-NIGHT PHRASES", 25)
v5.para("« Challenge yourself ! » « Every mile helps. » « Be kind ! » — three sentences for one night. Learn them, and Friday night in English is yours.", 22)
v5.para("« Every mile helps » means : each small step counts. After that sentence, the running begins — and the giving too.", 22)
v5.bridge("매 마일이 도움이 돼요｜Every mile helps = 매 걸음이 소중해요.")
v5.head("MUNICH WEEKEND", 25)
v5.para("After Friday, the weekend keeps going : the Lions' Fan Fest in Munich on Friday and Saturday, November 13–14, at Odeonsplatz, before Sunday's game. The weekend warms up for Munich.", 22)
v5.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jeunesse.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("DEEP READ · 시사 심층", "The Lucerna", "LEVEL B2 · After November 3 · 11월 3일 이후")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P6-main")
f.title("After November 3 : Why the Results Take Time", 37)
f.byline("By The Lucerna newsroom · Reading level : B2")
f.para("On Tuesday, November 3, Americans voted in the midterm election — all 435 seats in the House of Representatives, about a third of the Senate, and governorships in many states. This issue went to press on Monday, November 2, the day before the vote. That is why it prints no results. There were no results to print — and this paper invents none.")
f.para("Some races are called on election night. A news organisation « calls » a race when the maths is clear : the candidate behind cannot catch up. But a call is not the official result. The official result comes later, when each state checks — the canvass — and certifies its count. States certify between November 10 and December 18, and in some states there is no fixed date at all.")
f.para("Why does counting take days ? Mail ballots take time : every envelope must be opened, every signature checked. Some states count mail ballots that arrive after Election Day, if they were posted in time. In Alaska and Maine, ranked-choice voting can add rounds — and days. In Georgia and Mississippi, a Senate race with no majority winner goes to a runoff on December 1.")
f.para("Leads can change as the count goes on. In some states, the votes cast on the day are counted first ; in others, mail votes come first. A candidate who leads at midnight can trail by Friday — and that is normal. It is not a sign of anything wrong. It is the system, working slowly, in public.")
f.para("The last midterm, in 2022, tells the same story. The Senate was not decided until the Saturday after Election Day, and the House until the Wednesday after. Nobody knows whether this year will be faster or slower — and this paper will not guess.")
f.box("A PRACTICE BALLOT · 연습용 투표", [
    ("For Governor : ☐ Candidate A · ☐ Candidate B. For the House : ☐ Candidate C · ☐ Candidate D. Names are codes here — this ballot teaches how to mark, not whom to choose.", "serif", False, INK, 21.5, 1.4),
])
f.para("A note on numbers in this issue : this paper prints no poll figures and no predictions, and no results it cannot verify. When the verified results are in, VOL.4 will report them — who won, and what changes. Patience is part of the system, not a failure of it.")
f.gloss("to call a race 선거 결과를 발표하다 · to certify 공식 확인하다(인증) · a runoff 결선 투표 · patience 인내심.")
# practice chart
f.head("READ THE CHART · 도표 읽기", 25)
f.para("How long did the last midterm take ? In 2022, the count ran past election night. The chart is history, not a prediction for 2026.", 22)
for lab in ["Senate decided : 4 days after Election Day (2022)",
            "House decided : 8 days after Election Day (2022)",
            "States certify : November 10 to December 18 (2026 calendar)",
            "Runoff, if needed : December 1 (Georgia / Mississippi)"]:
    f.para(lab, 22, "serif", True, OLIVE, 1.3, 2)
f.head("A · CHART READING", 25)
f.bridge("위의 역사 도표를 읽고 정답을 고르세요.")
f.ex("B2", "도표 읽기", "B", "2022년에는 상원이 4일 후에야 정해졌어요",
     "In 2022, the Senate was decided... A. on election night · B. 4 days after Election Day · C. 18 days after", size=22)
f.ex("B2", "도표 읽기", "C", "2022년에는 하원이 8일 후에야 정해졌어요",
     "In 2022, the House was decided... A. 4 days after · B. 6 days after · C. 8 days after", size=22)
f.ex("B2", "도표 읽기", "A", "각 주 인증은 11월 10일부터 12월 18일 사이에 있어요",
     "States certify between... A. November 10 and December 18 · B. November 3 and 10 · C. December 1 and 31", size=22)
f.ex("B2", "도표 읽기", "B", "결선 투표 12월 1일",
     "A runoff, if needed, is on... A. November 10 · B. December 1 · C. December 18", size=22)
f.ex("B2", "도표 읽기", "A", "도표는 역사예요, 2026년에 대한 예측이 아니에요",
     "This chart is... A. history, not a prediction · B. a prediction · C. a poll", size=22)
f.ex("B2", "도표 읽기", "C", "하원은 상원보다 4일 늦게 정해졌어요",
     "The House took longer than the Senate by... A. 2 days · B. 12 days · C. 4 days", size=22)
f.head("B · COMPREHENSION", 25)
f.bridge("6면 기사를 읽고 정답을 고르세요.")
f.ex("B2", "객관식", "B", "이번 호는 11월 2일 인쇄, 투표 전이에요",
     "This issue went to press on... A. November 3 · B. November 2 · C. November 11", size=22)
f.ex("B2", "객관식", "A", "공식 결과는 각 주 인증에서 나와요",
     "The official result comes when... A. the state certifies its count · B. TV calls the race · C. the first votes arrive", size=22)
f.ex("B2", "객관식", "C", "우편 투표 개표에는 시간이 걸려요",
     "Counting takes time because... A. TV is slow · B. voters are late · C. mail ballots must be opened and checked", size=22)
f.ex("B2", "객관식", "B", "알래스카와 메인은 순위 선택 투표제를 써요",
     "Ranked-choice voting is used in... A. Texas and Florida · B. Alaska and Maine · C. Ohio and Georgia", size=22)
f.ex("B2", "객관식", "A", "선두가 바뀌는 건 정상이에요",
     "A lead that changes is... A. normal · B. a sign of fraud · C. impossible", size=22)
f.ex("B2", "객관식", "C", "VOL.4에서 확인된 결과를 보도할 거예요",
     "The verified results will be reported in... A. VOL.2 · B. this issue · C. VOL.4", size=22)
f.head("C · SENTENCES", 25)
f.bridge("주어진 단어로 문장을 완성하세요.")
f.ex("B2", "문장 완성", "certify", "certify = 공식 확인하다",
     "Each state must ___ its count.", instr="빈칸 채우기")
f.ex("B2", "문장 완성", "call", "call a race = 선거 결과를 발표하다",
     "News organisations ___ a race when the maths is clear.", instr="빈칸 채우기")
f.ex("B2", "문장 완성", "patience", "patience = 인내심",
     "___ is part of the system.", instr="빈칸 채우기")
f.ex("B1", "문장 완성", "takes", "take time = 시간이 걸리다",
     "Counting ___ time in every state.", instr="빈칸 채우기")
f.ex("B1", "문장 완성", "differs", "differ 3인칭 단수 differs",
     "The rule ___ from state to state.", instr="빈칸 채우기")
f.ex("B1", "문장 완성", "official", "official = 공식적인",
     "A call is not the ___ result.", instr="빈칸 채우기")
f.end_report()

# col 3: image + terms box
ix = COLX[3]
image(p, "voting.jpg", ix, 200, CW, 300)
cy6 = caption(p, ix, 500, CW, "A voting booth in the Old State House, Hartford, Connecticut : one voter, one ballot, one private moment. On Tuesday, November 3, millions of Americans did the same.",
              "Kenneth C. Zirkel — CC0, via Wikimedia Commons")
v6 = Flow(p, [(ix, CW)], int(cy6) + 18, 2540, tag="P6-col3")
v6.box("HOW LONG ? · 임기는 얼마나?", [
    ("House : 2 years, all 435 seats each midterm. Senate : 6 years, about a third each election. President : 4 years. Governor : usually 4 years.", "serif", False, INK, 21.5, 1.42),
])
v6.head("FIFTY ELECTIONS", 25)
v6.para("One country, fifty systems : that is why American election night is a map, not a single number. Learn the map, and the night makes sense.", 22)
v6.bridge("한 장의 지도｜쉰 개 주, 쉰 가지 규칙 — 그래서 선거의 밤에 보는 건 지도가 되지, 숫자가 아니에요.")
v6.end_report()
p.foot(6)
p.save(f"{OUT}/p6-politique.svg")
print("P6 saved, exercises so far:", len(REG))
