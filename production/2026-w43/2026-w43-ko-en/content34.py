# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 문화 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("문화　Culture", "Lucerna", "레벨 A2→B1　억새축제와 사과의 계절　Silver grass and apple season")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-feature")
f.title("금요일이 마지막 날 — 서울억새축제", 32)
f.byline("Lucerna 편집부　읽기 레벨: A2→B1")
f.para("서울 하늘공원에서 '제25회 서울억새축제'가 열리고 있어요. 축제는 10월 17일에 시작해서 23일 금요일에 끝나요. 아침 10시부터 밤 9시까지 열려요. 밤에는 불빛 쇼도 있어요.")
f.para("올해 축제의 주제는 '억새, 자연이 건네는 위로'예요. 하늘공원은 옛날에 쓰레기를 묻던 땅이었어요. 지금은 억새가 가득한 생태 공원이 됐어요.")
f.para("축제에서는 억새 꽃다발을 만들 수 있어요. 버스킹 공연도 있고, 소원을 쓰는 곳도 있어요. 이번 주 금요일이 마지막 날이에요. 가고 싶은 사람은 서두르세요!")
f.para("하늘공원은 월드컵공원 안에 있어요. 입장료는 없어요. 누구나 갈 수 있어요.")
f.gloss("억새 = silver grass · 묻다 = to bury · 가득하다 = to be full · 서두르다 = to hurry")
f.head("사과의 계절 — 청송사과축제", 25)
f.para("가을은 사과의 계절이에요. 경상북도 청송에서는 '제20회 청송사과축제'가 열려요. 현장 축제는 11월 4일부터 8일까지예요. 하지만 온라인 축제는 지금 한창이에요.")
f.para("온라인 축제는 9월 24일부터 11월 8일까지 다음(Daum)에서 열려요. 게임도 하고 사과 선물도 받을 수 있어요. 청송군은 14일부터 '청이와 송이' 카카오톡 이모티콘을 무료로 나눠 주기 시작했어요. 먼저 내려받는 75,000명까지 받을 수 있어요.")
f.para("청송은 사과로 유명한 곳이에요. 그래서 축제의 이름도 '청송사과축제'예요. 가을이 되면 많은 사람이 청송 사과를 찾아요.")
f.gloss("한창 = in full swing · 현장 = on-site, at the scene · 나눠 주다 = to hand out · 먼저 = first, ahead")
f.end_report()

# col 3: susuki painting + facts + apples + 당신
ix = COLX[3]
image(p, "susuki.jpg", ix, 200, CW, 185)
cy3 = caption(p, ix, 385, CW, "억새 사이에서 먹이를 찾는 메추라기. 억새는 가을의 얼굴이에요.",
              "그림: Matsumura Keibun — Public domain (Wikimedia Commons)")
facts = ["서울억새축제: 10월 17일~23일, 하늘공원",
         "청송사과축제 온라인: ~11월 8일",
         "청송 현장 축제: 11월 4일~8일"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "축제 달력", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
image(p, "apples.jpg", ix, ay3, CW, 200)
cy4 = caption(p, ix, ay3 + 200, CW, "사과는 가을의 과일이에요. 화가 세잔이 그린 사과예요.",
              "그림: Paul Cézanne — Public domain (Wikimedia Commons)")
ey3 = cy4 + 18
etvous = "당신은? 가을에 먹고 싶은 과일은 뭐예요? 한국어로 두 문장 써서 보내 주세요."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("And you? Which fruit do you want to eat in autumn? Write two sentences in Korean and send them in.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "당신은?　Your turn", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "And you? Which fruit do you want to eat in autumn? Write two sentences in Korean and send them in.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "연습　Page 3 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8　Items may mix levels; find them by number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　이해", 25)
e.glossline("Read the page 3 articles and choose the correct answer.")
e.ex("A2", "multiple choice", "B", "The festival is held at Haneul Park",
     "억새축제는 어디에서 열려요? A. 청송 · B. 하늘공원 · C. 제주도", size=20, gap=7)
e.ex("A2", "multiple choice", "A", "The last day is Friday the 23rd",
     "억새축제의 마지막 날은 언제예요? A. 23일 금요일 · B. 25일 일요일 · C. 17일 토요일", size=20, gap=7)
e.ex("A2", "multiple choice", "B", "Haneul Park used to be a landfill",
     "하늘공원은 옛날에 무엇이었어요? A. 학교 · B. 쓰레기를 묻던 땅 · C. 야구장", size=20, gap=7)
e.ex("B1", "multiple choice", "C", "The on-site Cheongsong festival starts Nov 4",
     "청송 현장 축제는 언제예요? A. 지금 · B. 10월 23일 · C. 11월 4일부터", size=20, gap=7)
e.ex("A2", "multiple choice", "B", "Emoticons for the first 75,000 people",
     "이모티콘은 몇 명까지 받을 수 있어요? A. 7,500명 · B. 75,000명 · C. 750,000명", size=20, gap=7)
e.head("B　말 넣기", 25)
e.glossline("Put the right word in each blank.")
e.ex("A2", "fill-in", "억새", "The grass that fills Haneul Park in autumn",
     "가을에 하늘공원에 가득한 풀은 ___예요.", instr="Fill in", size=20, gap=7)
e.ex("A2", "fill-in", "주제", "The theme is 'silver grass, comfort handed over by nature'",
     "올해 축제의 ___는 '억새, 자연이 건네는 위로'예요.", instr="Fill in", size=20, gap=7)
e.ex("B1", "fill-in", "한창", "The online festival is in full swing",
     "온라인 축제는 지금 ___이에요.", instr="Fill in", size=20, gap=7)
e.ex("A2", "fill-in", "무료", "The emoticons can be received for free",
     "이모티콘은 돈 없이, ___로 받을 수 있어요.", instr="Fill in", size=20, gap=7)
e.ex("B1", "fill-in", "서두르세요", "The last day is near - hurry",
     "마지막 날이 가까워요. 가고 싶은 사람은 ___!", instr="Fill in", size=20, gap=7)
e.head("C　숫자와 날짜", 25)
e.glossline("Answer with the numbers and dates from page 3.")
e.ex("A2", "fill-in", "25", "The 25th Seoul Silver Grass Festival",
     "서울억새축제는 제___회예요.", instr="Fill in", size=20, gap=7)
e.ex("A2", "fill-in", "9", "The festival stays open until 9 p.m.",
     "축제는 밤 ___시까지 열려요.", instr="Fill in", size=20, gap=7)
e.ex("A2", "fill-in", "20", "The 20th Cheongsong Apple Festival",
     "청송사과축제는 제___회예요.", instr="Fill in", size=20, gap=7)
e.ex("A2", "fill-in", "8", "The online festival runs until Nov 8",
     "온라인 축제는 11월 ___일까지예요.", instr="Fill in", size=20, gap=7)
e.head("D　짝 맞추기", 25)
e.match_set("A2", "matching",
            ["하늘공원", "청송", "억새", "청이와 송이"],
            ["카카오톡 이모티콘의 이름",
             "쓰레기를 묻던 땅이었어요",
             "사과 축제가 열리는 곳",
             "가을에 피는 풀"],
            ["b", "c", "d", "a"],
            ["하늘공원 = once a landfill (b)", "청송 = where the apple festival is held (c)", "억새 = the grass of autumn (d)", "청이와 송이 = the emoticons' names (a)"],
            instr="Match the pairs")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-munhwa.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · 스포츠 (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("스포츠　Sports", "Lucerna", "레벨 B1　가을야구 준플레이오프　Autumn baseball semi-playoff")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P4-feature")
f.title("가을야구, 이번 주에 큰 경기가 많아요", 32)
f.byline("Lucerna 편집부　읽기 레벨: B1")
f.para("한국의 가을은 야구의 계절이에요. 프로야구 포스트시즌, '가을야구'가 한창이에요. 지금은 준플레이오프예요. KIA 타이거즈와 LG 트윈스가 싸우고 있어요.")
f.para("준플레이오프는 다섯 번 싸워서 세 번 이긴 팀이 올라가요. 3차전은 20일 화요일, 4차전은 21일 수요일에 있어요. 필요하면 5차전은 23일 금요일에 열려요.")
f.para("LG는 와일드카드에서 두산을 4대 1로 이기고 준플레이오프에 왔어요.")
f.para("준플레이오프에서 이긴 팀은 25일 일요일에 삼성 라이온즈와 플레이오프를 시작해요. 그리고 정규시즌 1위 kt wiz는 한국시리즈에서 기다리고 있어요. 한국시리즈는 11월 2일 월요일에 시작해요.")
f.para("가을야구는 정규시즌이 끝난 뒤에 열려요. 아래 그림처럼 한 칸씩 올라가서, 마지막에 한국시리즈에서 싸워요.")
f.para("야구장에서는 응원도 재미있어요. 팬들은 노래를 부르고 큰 소리로 응원해요. '힘내세요!' '이겨라!' 하는 소리가 경기장에 가득해요.")
f.para("경기 결과는 다음 주 신문에서 알려 드릴게요. 누가 올라갈까요? 함께 지켜봐요.")
f.gloss("포스트시즌 = postseason · 와일드카드 = wild card · 정규시즌 = regular season · 지켜보다 = to keep watching")
f.end_report()

# ---- ladder diagram (cols 0-2) ----
ly = 1210
p.text(MX, ly + 26, "한국시리즈까지의 길　The road to the Korean Series", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ly + 40, OLIVE, 2)
steps = [
    ("와일드카드", "LG가 두산에\n4대 1로 승리"),
    ("준플레이오프", "KIA vs LG\n이번 주에 끝나요"),
    ("플레이오프", "삼성 라이온즈\n10월 25일 시작"),
    ("한국시리즈", "kt wiz가 기다려요\n11월 2일 시작"),
]
bw, bh, by0 = 320, 118, ly + 58
for i, (t, d) in enumerate(steps):
    x0 = MX + i * (bw + 26)
    p.rect(x0, by0, bw, bh, fill=BOX if i != 1 else "#f0eee5", stroke=OLIVE if i == 1 else LINE, sw=1.6 if i == 1 else 1.2)
    p.text(x0 + bw / 2, by0 + 40, t, 24, "sans", True, OLIVE, anchor="middle")
    for j, ln in enumerate(d.split("\n")):
        p.text(x0 + bw / 2, by0 + 76 + j * 28, ln, 20, "serif", False, INK, anchor="middle")
    if i < 3:
        ax = x0 + bw + 3
        p.add(f'<path d="M{ax} {by0 + bh/2 - 9} L{ax + 20} {by0 + bh/2} L{ax} {by0 + bh/2 + 9}" fill="none" stroke="{OLIVE}" stroke-width="2.6"/>')
p.para(MX, by0 + bh + 34, "위 그림은 가을야구의 순서예요. 지금은 두 번째 칸, 준플레이오프예요.", 20.5, "serif", False, GREY, 1388, 1.4)

# col 3: baseball image + calendar facts
ix = COLX[3]
image(p, "baseball.jpg", ix, 200, CW, 240)
cy3 = caption(p, ix, 440, CW, "20세기 초 미국의 야구팀. 야구의 가을은 길어요.",
              "사진: Bain News Service — Public domain (Wikimedia Commons)")
facts = ["3차전: 10월 20일 (화)",
         "4차전: 10월 21일 (수)",
         "5차전: 10월 23일 (금) — 필요하면",
         "플레이오프 시작: 10월 25일 (일)",
         "한국시리즈: 11월 2일 (월)부터"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "가을야구 달력", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P4 col3 ends", sy3 + sh)

# ---- P4 exercises ----
ey = 1560
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "연습　Page 4 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8　Items may mix levels; find them by number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　이해", 25)
e.glossline("Read the page 4 articles and choose the correct answer.")
e.ex("B1", "multiple choice", "B", "The semi-playoff is on now",
     "지금은 무슨 경기예요? A. 한국시리즈 · B. 준플레이오프 · C. 와일드카드", size=20, gap=7)
e.ex("B1", "multiple choice", "A", "The semi-playoff is KIA vs LG",
     "준플레이오프에서 싸우는 두 팀은 어디예요? A. KIA와 LG · B. 삼성과 kt · C. 두산과 LG", size=20, gap=7)
e.ex("B1", "multiple choice", "B", "Game 5, if needed, is Friday the 23rd",
     "5차전은 언제예요? A. 21일 · B. 23일 (필요하면) · C. 25일", size=20, gap=7)
e.ex("B1", "multiple choice", "C", "The playoff opponent is the Samsung Lions",
     "이긴 팀은 플레이오프에서 누구를 만나요? A. kt · B. 두산 · C. 삼성", size=20, gap=7)
e.ex("B1", "multiple choice", "B", "The Korean Series starts Nov 2",
     "한국시리즈는 언제 시작해요? A. 10월 25일 · B. 11월 2일 · C. 11월 19일", size=20, gap=7)
e.head("B　말 넣기", 25)
e.glossline("Put the right word in each blank.")
e.ex("B1", "fill-in", "가을야구", "가을야구 = autumn postseason baseball",
     "가을의 포스트시즌을 ___라고 해요.", instr="Fill in", size=20, gap=7)
e.ex("B1", "fill-in", "와일드카드", "LG beat Doosan in the wild-card round",
     "LG는 ___에서 두산을 이겼어요.", instr="Fill in", size=20, gap=7)
e.ex("B1", "fill-in", "삼성", "The playoff opponent is the Samsung Lions",
     "플레이오프 상대는 ___ 라이온즈예요.", instr="Fill in", size=20, gap=7)
e.ex("B1", "fill-in", "kt", "Regular-season No. 1 kt is waiting",
     "정규시즌 1위 ___ wiz는 한국시리즈에서 기다리고 있어요.", instr="Fill in", size=20, gap=7)
e.ex("B1", "fill-in", "다음", "The results are in next week's paper",
     "경기 결과는 ___ 주 신문에서 알려 드릴게요.", instr="Fill in", size=20, gap=7)
e.head("C　문장 바꾸기", 25)
e.glossline("Rewrite each sentence in the past tense.")
e.ex("B1", "transformation", "LG는 와일드카드에서 두산을 이겼어요.", "The past tense of 이기다 is 이겼어요",
     "LG는 와일드카드에서 두산을 이겨요. → ___", instr="Rewrite", size=20, gap=7)
e.ex("B1", "transformation", "축제가 17일에 시작했어요.", "The past tense of 시작하다 is 시작했어요",
     "축제가 17일에 시작해요. → ___", instr="Rewrite", size=20, gap=7)
e.ex("B1", "transformation", "기상청이 예보를 바꿨어요.", "The past tense of 바꾸다 is 바꿨어요",
     "기상청이 예보를 바꿔요. → ___", instr="Rewrite", size=20, gap=7)
e.ex("B1", "transformation", "엔믹스가 새 앨범을 냈어요.", "The past tense of 내다 is 냈어요",
     "엔믹스가 새 앨범을 내요. → ___", instr="Rewrite", size=20, gap=7)
e.head("D　짝 맞추기", 25)
e.match_set("B1", "matching",
            ["준플레이오프", "플레이오프", "한국시리즈", "와일드카드"],
            ["kt wiz가 기다려요",
             "KIA와 LG가 싸워요",
             "삼성이 기다려요",
             "LG가 두산을 이겼어요"],
            ["b", "c", "a", "d"],
            ["준플레이오프 = KIA vs LG (b)", "플레이오프 = Samsung is waiting (c)", "한국시리즈 = kt is waiting (a)", "와일드카드 = LG won it (d)"],
            instr="Match the pairs")
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-seupocheu.svg")
print("P4 saved, exercises so far:", len(REG))
