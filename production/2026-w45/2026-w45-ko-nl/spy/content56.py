# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ko-nl-build/spy/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 청년 (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("청년 · Jongeren", "Lucerna", "레벨 B1 · 수능 카운트다운과 할로윈 · Aftelling naar het examen en Halloween")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-feature")
f.title("수능까지 12일 — 고3의 가을, 온 나라의 응원", 37)
f.byline("Lucerna 편집부 · 읽기 레벨: B1")
f.para("이번 주 토요일 11월 7일에는 수능까지 12일이 남아요. 수능은 11월 19일 목요일이에요. 올해 수험생은 551,864명이에요. 시험장은 전국에 1,312곳이에요. 고3 교실에서는 마지막 정리가 한창이에요.")
f.para("수능이 가까워지면 온 나라가 수험생을 응원해요. 시험장 앞에서는 '힘내세요!', '떨지 마세요!', '잘할 수 있어요!'라는 말이 가득해요. 합격을 비는 마음으로 찹쌀떡이나 엿을 선물하기도 해요. 끈끈한 음식은 '꼭 붙어라'는 뜻을 담고 있어요.", w=414)
f.para("그런데 조심해야 할 말이 있어요. 시험 날의 특별한 조치는 11월 19일에만 적용돼요. 회사와 관공서가 10시부터 일을 시작하고, 지하철이 더 자주 다니고, 영어 듣기 시간(13시 10분~13시 35분)에 비행기가 뜨거나 내리지 않는 것 — 모두 11월 19일의 일이에요. 이번 주(11월 2~8일)의 조치가 아니에요. 자세한 이야기는 6면에 있어요.")
f.gloss("정리 = ordenen, herhalen · 끈끈하다 = kleverig · 합격 = slagen.")
f.head("할로윈 — 미리 알려진 안전 계획", 25)
f.para("지난 토요일 10월 31일은 할로윈이었어요. 이 신문이 마감된 10월 26일 현재, 당일의 모습은 아직 알 수 없어요. 다만 미리 발표된 안전 계획은 있어요.", w=424)
f.para("내무부는 10월 23일부터 11월 1일까지를 특별 관리 기간으로 정했어요. 전국 28곳을 중점 관리 지역으로 정했어요. 서울시는 14곳을 관리해요. 그중 8곳이 중점 지역이에요. 이태원, 홍대, 익선동, 명동, 성수, 건대, 강남역, 압구정이에요.")
f.para("서울시의 안전 인력은 3,271명이에요. 그중 이태원에 1,620명이 배치돼요. 10월 31일에는 이태원로가 통제돼요. 인파를 살피는 인공지능 카메라와 드론도 쓰인다고 발표됐어요.")
f.para("할로윈을 즐기려면 사람이 많은 곳에서는 천천히 걷고, 안내를 잘 들으세요. 안전 계획부터 알아두는 것이 좋아요.", w=354)
f.gloss("중점 = zwaartepunt · 배치하다 = inzetten · 통제하다 = controleren.")
f.box("이번 주 청년 숫자 · In cijfers", [
    ("551,864명 — 올해 수험생", "serif", False, INK, 20.5, 1.4),
    ("1,312곳 — 전국 시험장", "serif", False, INK, 20.5, 1.4),
    ("3,271명 — 서울시 할로윈 안전 인력 (이태원 1,620명)", "serif", False, INK, 20.5, 1.4),
    ("13시 10분~13시 35분 — 11월 19일 영어 듣기 시간", "serif", False, INK, 20.5, 1.4, 338),
])
f.head("시험 전날의 하루", 25)
f.para("시험 전날에는 일찍 자요. 밤늦게까지 공부하면 아침에 피곤해져요. 준비물은 미리 챙겨요. 수험표와 신분증, 연필을 가방에 넣어요.")
f.para("아침밥은 꼭 먹어요. 밥을 먹어야 머리가 잘 돌아가요. 너무 많이 먹으면 졸려요. 평소 먹던 대로 먹는 것이 좋아요.")
f.gloss("챙기다 = klaarmaken · 졸리다 = slaperig zijn · 평소 = normaal.")
f.head("합격 기원 음식", 25)
f.para("합격을 비는 마음으로 찹쌀떡이나 엿을 선물해요. 엿을 먹으면 시험에 '붙어라'는 뜻이에요. 끈끈한 음식은 꼭 붙으라는 뜻을 담고 있어요.")
f.para("미역국을 피하는 사람도 있어요. 미역은 미끄럽다는 뜻이 있기 때문이에요. 미끄러지면 안 되니까, 시험 날 아침에는 미역국을 먹지 않아요.")
f.gloss("비다 = bidden, wensen · 피하다 = vermijden · 미끄럽다 = glad.")
f.end_report()

# col 3: study image + 당신
ix = COLX[3]
image(p, "study.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "도서관에서 공부하는 학생들. 수험생에게 가을은 가장 바쁜 계절이에요.",
              "사진: Gary Todd — CC0 (Wikimedia Commons) · 자료 사진")
ey3 = cy3 + 24
etvous = "당신은? 수험생에게 해 주고 싶은 응원 한마디는 뭐예요? 한국어로 두 문장 써서 보내 주세요."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("En jij? Wat is jouw aanmoediging voor de kandidaten? Schrijf twee zinnen in het Koreaans en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "당신은? · En jij?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "En jij? Wat is jouw aanmoediging voor de kandidaten? Schrijf twee zinnen in het Koreaans en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "연습 · Oefeningen blz. 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op blz. 8 · Niveaus kunnen gemengd staan — zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · 이해", 25)
e.glossline("Lees de teksten op blz. 5 en kies het juiste antwoord.")
e.ex("B1", "单选", "A", "7 november is D-12",
     "11월 7일에는 수능까지 며칠이 남아요? A. 12일 · B. 17일 · C. 29일", size=20, gap=7)
e.ex("B1", "单选", "B", "Het examen is op donderdag 19 november",
     "수능은 며칠에 있어요? A. 11월 7일 · B. 11월 19일 · C. 11월 28일", size=20, gap=7)
e.ex("B1", "单选", "A", "Tijdens het luisterdeel geen vluchten",
     "영어 듣기 시간에 비행기는 어떻게 돼요? A. 뜨거나 내리지 않아요 · B. 평소대로 다녀요 · C. 더 자주 다녀요", size=20, gap=7)
e.ex("B1", "单选", "B", "Seoul, Halloween: 3.271 medewerkers",
     "서울시 할로윈 안전 인력은 몇 명이에요? A. 1,620명 · B. 3,271명 · C. 551,864명", size=20, gap=7)
e.ex("B1", "单选", "A", "Itaewon-ro afgesloten op 31 oktober",
     "이태원로가 통제되는 날은 언제예요? A. 10월 31일 · B. 11월 7일 · C. 11월 19일", size=20, gap=7)
e.head("B · 말 넣기", 25)
e.glossline("Vul het juiste woord in.")
e.ex("B1", "完成句子", "응원", "Het hele land moedigt de kandidaten aan",
     "온 나라가 수험생을 ___해요.", instr="Vul in", size=20, gap=7)
e.ex("B1", "完成句子", "카운트다운", "De aftelling gaat door",
     "수능 ___이 계속돼요.", instr="Vul in", size=20, gap=7)
e.ex("B1", "完成句子", "선물", "Kleverige rijstkoek en moutsuiker als geluksgeschenk",
     "합격을 비는 마음으로 찹쌀떡이나 엿을 ___하기도 해요.", instr="Vul in", size=20, gap=7, bw=424)
e.ex("B1", "完成句子", "인력", "Seoul: 3.271 medewerkers",
     "서울시의 안전 ___은 3,271명이에요.", instr="Vul in", size=20, gap=7)
e.ex("B1", "完成句子", "통제", "Itaewon-ro afgesloten op 31 oktober",
     "10월 31일에는 이태원로가 ___돼요.", instr="Vul in", size=20, gap=7)
e.head("C · 숫자와 날짜", 25)
e.glossline("Antwoord met de getallen van blz. 5.")
e.ex("B1", "完成句子", "551,864", "Dit jaar: 551.864 kandidaten",
     "올해 수험생은 ___명이에요.", instr="Vul in", size=20, gap=7)
e.ex("B1", "完成句子", "1,312", "1.312 examenlocaties in het hele land",
     "시험장은 전국에 ___곳이에요.", instr="Vul in", size=20, gap=7)
e.ex("B1", "完成句子", "10", "Op de examendag beginnen diensten om 10 uur",
     "시험 날, 회사와 관공서는 ___시부터 일을 시작해요.", instr="Vul in", size=20, gap=7, bw=354)
e.ex("B1", "完成句子", "1,620", "Itaewon: 1.620 medewerkers",
     "이태원에 배치되는 안전 인력은 ___명이에요.", instr="Vul in", size=20, gap=7)
e.head("D · 문장 만들기", 25)
e.glossline("Zet de woorden in de juiste volgorde en maak een zin.")
e.ex("B1", "造句", "수험생은 열심히 공부해요.", "Volgorde: onderwerp + bijwoord + werkwoord",
     "수험생은 / 열심히 / 공부해요 → ___", instr="Bouw", size=20, gap=7)
e.ex("B1", "造句", "우리는 수험생을 응원해요.", "Volgorde: onderwerp + lijdend voorwerp + werkwoord",
     "우리는 / 수험생을 / 응원해요 → ___", instr="Bouw", size=20, gap=7)
e.ex("B1", "造句", "비행기는 듣기 시간에 뜨지 않아요.", "Tijdens het luisterdeel geen vluchten",
     "비행기는 / 듣기 시간에 / 뜨지 않아요 → ___", instr="Bouw", size=20, gap=7)
e.ex("B1", "造句", "서울시는 14곳을 관리해요.", "Seoul beheert 14 locaties",
     "서울시는 / 14곳을 / 관리해요 → ___", instr="Bouw", size=20, gap=7)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-cheongnyeon.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 깊이 읽기 (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("깊이 읽기 · Dieper lezen", "Lucerna", "레벨 B2 · 수능 카운트다운을 읽는 법 · De aftelling naar het examen leren lezen")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-feature")
f.title("수능 카운트다운을 읽는 법 — 날짜, 조치, 분위기를 나누세요", 37)
f.byline("Lucerna 편집부 · 읽기 레벨: B2")
f.para("이번 주 신문에는 수능 이야기가 많아요. 그런데 수능 이야기를 읽을 때는 세 가지를 나눠야 해요. 날짜, 조치, 분위기예요. 날짜는 11월 19일 목요일이에요. 조치는 시험 날에만 적용돼요. 분위기는 지금, 이번 주에 있어요. 세 가지를 섞으면 뉴스를 잘못 읽게 돼요.", w=404)
f.para("분위기부터 봐요. 이번 주는 D-17에서 D-12로 가는 주간이에요. 교실과 집에서는 마지막 정리가 한창이에요. 시험장 앞의 응원, 찹쌀떡과 엿의 선물 — 이 모두가 분위기예요. 분위기는 날짜가 정해져 있지 않아요. 시험이 가까워질수록 짙어져요.")
f.para("조치는 달라요. 11월 19일 시험 날에는 회사와 관공서가 10시부터 일을 시작해요. 지하철이 더 자주 다녀요. 영어 듣기 시간인 13시 10분부터 13시 35분까지는 비행기가 뜨거나 내리지 않아요. 시험장 앞 200미터 안에서는 차가 통제돼요. 이 조치는 11월 19일의 조치예요. 11월 2일부터 8일까지의 조치로 읽으면 안 돼요.")
f.para("숫자도 읽는 법이 있어요. 올해 수험생은 551,864명, 시험장은 1,312곳이에요. 큰 숫자는 나라 전체의 규모를 보여줘요. 숫자가 크다고 해서 개인의 시험이 더 어려워지는 것은 아니에요. 내 시험장은 1,312곳 중 한 곳일 뿐이에요.")
f.para("그래서 뉴스를 읽을 때는 날짜를 먼저 보세요. '수능이 가까워졌다'는 말은 분위기예요. '수능 조치가 시작됐다'는 말은 11월 19일의 일이에요. 날짜와 조치를 나누면, 뉴스가 훨씬 쉽게 읽혀요.", w=394)
f.gloss("짙어지다 = sterker worden · 규모 = schaal · 섞다 = verwarren.")
f.head("숫자를 읽을 때", 25)
f.para("큰 숫자를 보면 겁이 날 수 있어요. 551,864명이라는 숫자는 나라 전체의 수험생이에요. 그중 한 명이 바로 나예요. 큰 숫자보다 내 준비가 더 중요해요.", w=374)
f.gloss("겁이 나다 = bang zijn · 중요하다 = belangrijk.")
f.head("뉴스의 날짜 찾기", 25)
f.para("뉴스를 읽을 때는 제목보다 날짜를 먼저 봐요. 날짜가 있는 뉴스가 믿을 수 있어요.", w=374)
f.para("'예정'과 '확정'도 나눠야 해요. 예정은 아직 정해지지 않은 일, 확정은 정해진 일이에요. 예정된 일을 확정된 일처럼 읽으면 안 돼요.")
f.gloss("예정 = gepland · 확정 = bevestigd · 믿다 = geloven.")
f.end_report()

# ---- comparison table (cols 0-2) ----
ty = 1210
p.text(MX, ty + 26, "이번 주와 시험 날, 한눈에 보기 · Deze week en de examendag naast elkaar", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ty + 40, GOLD, 2)
rows = [
    ("구분", "이번 주 (11월 2~8일)", "시험 날 (11월 19일)"),
    ("날짜 세기", "D-17 ~ D-12", "D-데이"),
    ("분위기", "카운트다운", "시험 당일"),
    ("특별 조치", "없어요 (평상시)", "있어요 (10시 출근 등)"),
]
tw = [300, 544, 544]
yy = ty + 58
for r, (c0, c1, c2) in enumerate(rows):
    x0 = MX
    for j, cell in enumerate((c0, c1, c2)):
        hdr = (r == 0)
        p.rect(x0, yy, tw[j], 52, fill=DARK if hdr else (BOX if r % 2 else "#f1ead6"), stroke=LINE, sw=1.1)
        p.text(x0 + 18, yy + 35, cell, 21 if not hdr else 20, "sans" if hdr else "serif", hdr,
               "#f3edda" if hdr else INK)
        x0 += tw[j]
    yy += 52
p.para(MX, yy + 30, "표의 자료: 교육부 발표 (10월 20일) — 조치는 11월 19일에만 적용돼요. 이번 주에는 특별 조치가 없어요.", 19.5, "serif", False, GREY, 1388, 1.4)

# col 3: how-to-read boxes (no image on P6)
ix = COLX[3]
howto = ["① 날짜를 봐요", "② 조치를 봐요", "③ 분위기를 봐요"]
sy3 = 200 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in howto) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "수능 뉴스 읽는 법", 24, "sans", True, OLIVE)
yy3 += 52
for t in howto:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
dy3 = sy3 + sh + 26
dlist = ["D-17 — 11월 2일", "D-12 — 11월 7일", "D-1 — 11월 18일", "D-데이 — 11월 19일"]
sh2 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in dlist) + 32
p.rect(ix, dy3, CW, sh2, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = dy3 + 16
p.text(ix + 22, yy3 + 26, "이번 달의 D-데이", 24, "sans", True, OLIVE)
yy3 += 52
for t in dlist:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", dy3 + sh2)

# ---- P6 exercises ----
ey = 1560
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "연습 · Oefeningen blz. 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op blz. 8 · Niveaus kunnen gemengd staan — zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · 표 읽기", 25)
e.glossline("Bekijk de tabel op blz. 6 en antwoord.")
e.ex("B2", "单选", "B", "Deze week: aftelling D-17 tot D-12",
     "이번 주의 날짜 세기는 뭐예요? A. D-데이 · B. D-17 ~ D-12 · C. D-1", size=20, gap=7)
e.ex("B2", "单选", "A", "Op de examendag zijn er bijzondere maatregelen",
     "시험 날의 특별 조치는 있어요? A. 있어요 · B. 없어요 · C. 아직 몰라요", size=20, gap=7)
e.ex("B2", "单选", "B", "Deze week geen bijzondere maatregelen",
     "이번 주의 특별 조치는 있어요? A. 있어요 · B. 없어요 · C. 10시 출근만 있어요", size=20, gap=7)
e.ex("B2", "单选", "C", "De examendag is D-day",
     "시험 날의 날짜 세기는 뭐예요? A. D-17 · B. D-12 · C. D-데이", size=20, gap=7)
e.ex("B2", "单选", "A", "Deze week: aftelsfeer",
     "이번 주의 분위기는 뭐예요? A. 카운트다운 · B. 시험 당일 · C. 방학", size=20, gap=7)
e.head("B · 이해", 25)
e.glossline("Lees de teksten op blz. 6 en kies het juiste antwoord.")
e.ex("B2", "单选", "A", "Sfeer: nu, deze week",
     "분위기는 언제 있어요? A. 지금, 이번 주 · B. 11월 19일에만 · C. 지난주에만", size=20, gap=7)
e.ex("B2", "单选", "B", "Maatregelen alleen op 19 november",
     "특별 조치는 언제 적용돼요? A. 11월 2일부터 · B. 11월 19일에만 · C. 11월 7일부터", size=20, gap=7)
e.ex("B2", "单选", "A", "Luisterdeel 13:10–13:35",
     "영어 듣기 시간은 언제예요? A. 13시 10분~13시 35분 · B. 10시~12시 · C. 자정", size=20, gap=7)
e.ex("B2", "单选", "A", "Dit jaar: 551.864 kandidaten",
     "올해 수험생은 몇 명이에요? A. 551,864명 · B. 1,312명 · C. 3,271명", size=20, gap=7)
e.ex("B2", "单选", "B", "1.312 examenlocaties in het hele land",
     "시험장은 전국에 몇 곳이에요? A. 551,864곳 · B. 1,312곳 · C. 3,271곳", size=20, gap=7)
e.head("C · 말 넣기", 25)
e.glossline("Vul het juiste woord in.")
e.ex("B2", "完成句子", "분위기", "Aftelsfeer deze week",
     "카운트다운은 이번 주의 ___예요.", instr="Vul in", size=20, gap=7)
e.ex("B2", "完成句子", "조치", "Bijzondere maatregelen alleen op de examendag",
     "특별 ___는 11월 19일에만 적용돼요.", instr="Vul in", size=20, gap=7)
e.ex("B2", "完成句子", "카운트다운", "Week van D-17 tot D-12",
     "이번 주는 D-17에서 D-12로 가는 ___ 주간이에요.", instr="Vul in", size=20, gap=7)
e.ex("B2", "完成句子", "규모", "Grote getallen tonen de landelijke schaal",
     "큰 숫자는 나라 전체의 ___를 보여줘요.", instr="Vul in", size=20, gap=7)
e.head("D · 맞다 틀리다", 25)
e.glossline("Klopt de zin, kies 맞다; klopt hij niet, kies 틀리다.")
e.ex("B2", "判断", "틀리다", "Maatregelen alleen op 19 november",
     "특별 조치는 11월 2일부터 적용돼요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.ex("B2", "判断", "맞다", "7 november is D-12",
     "11월 7일은 D-12예요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.ex("B2", "判断", "틀리다", "Vluchten beperkt tijdens het luisterdeel",
     "시험 날 비행기는 평소대로 다녀요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.ex("B2", "判断", "맞다", "Deze week is aftelsfeer",
     "이번 주는 카운트다운 분위기예요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-gipi.svg")
print("P6 saved, exercises so far:", len(REG))
