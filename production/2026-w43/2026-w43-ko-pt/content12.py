# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 표지 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1　제1호", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "매주 한국어로　Toda semana　한국 사람이 읽는 한국어를 읽어요", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "2026년 10월 19일(월) ~ 25일(일)", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SEMANÁRIO COREANO　VOL.1　태풍 참피　가을야구　단풍", 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)
p.text(975, 366, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 16, "sans", False, GREY, anchor="middle")
p.text(975, 394, "TEXTOS EM COREANO　EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "태풍 참피가 오고 있어요 — 주말 날씨를 꼭 확인하세요!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "가을야구 준플레이오프도 이번 주에 끝나요. 이긴 팀은 일요일에 삼성을 만나요.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "O TUFÃO AVANÇA PARA O NORTE", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "Confira a previsão mais recente　Preparação na pág. 2", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "톱 뉴스　Manchete", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "태풍 참피가 오고 있어요", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 30, "기상청은 21일에 예보를 바꿨어요 — 경로는 아직 바뀔 수 있어요", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "Lucerna 편집부　읽기 레벨: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("제30호 태풍 '참피'가 북상하고 있어요. '참피'는 라오스가 낸 이름으로, 꽃의 이름이에요. 기상청은 21일 아침, 참피가 아주 강한 태풍이라고 했어요. 중심 기압은 약 900~905헥토파스칼, 최대 풍속은 초속 59미터예요.", size=24)
f.para("그런데 21일, 기상청은 예보를 바꿨어요. 참피는 중국 쪽으로 가지 않고, 동중국해를 지나 북쪽으로 올 수 있어요. 25일에서 26일쯤 제주도 남쪽 바다 근처까지 올 수 있어요.", size=24)
f.para("하지만 아직 모르는 것이 많아요. 한국 기상청과 일본 기상청, 미국 합동태풍경보센터의 예상 진로가 서로 달라요. 참피가 한국에 상륙할지는 아직 정해지지 않았어요. 경로는 아직 바뀔 수 있어요.", size=24)
f.para("그래서 이번 주말에는 날씨 소식을 자주 확인하세요. 기상청 홈페이지와 '날씨누리'에서 최신 정보를 볼 수 있어요. 태풍 준비 방법은 2면에 있어요.", size=24)
f.para("야구 소식도 있어요. 가을야구 준플레이오프가 이번 주에 끝나요. 이긴 팀은 일요일에 삼성과 플레이오프를 시작해요. 자세한 소식은 4면에 있어요.", size=24)
f.para("'Lucerna' 한국어판 제1호예요. 매주 진짜 한국 소식을 쉬운 한국어로 전해요. 재미있게 읽어 주세요!", size=24)
f.gloss("북상하다 = avançar para o norte · 진로 = trajetória, rota · 상륙하다 = chegar à costa · 헥토파스칼 = hectopascal (unidade de pressão)")
f.box("숫자로 보는 이번 주　Em números", [
    ("30 — '참피'는 올해 제30호 태풍이에요", "serif", False, INK, 20, 1.35),
    ("59 — 참피의 최대 풍속, 초속 59미터예요 (기상청 21일 발표)", "serif", False, INK, 20, 1.35),
    ("25~26일 — 참피가 제주도 남쪽 바다 근처에 올 수 있는 날 (예상)", "serif", False, INK, 20, 1.35),
    ("1 — 21일 한국 검색 1위는 '태풍 참피'였어요", "serif", False, INK, 20, 1.35),
])
f.head("지금 바로 연습　Pratique já", 25)
f.ex("A2", "Complete a frase", "30", "Champi é o tufão n.º 30 deste ano",
     "참피는 제___호 태풍이에요.", size=19.5, gap=6)
f.ex("A2", "Complete a frase", "라오스", "Champi é um nome de flor proposto pelo Laos",
     "'참피'는 ___가 낸 꽃의 이름이에요.", size=19.5, gap=6)
f.ex("A2", "Complete a frase", "21", "A agência de meteorologia mudou a previsão na manhã do dia 21",
     "기상청은 ___일 아침에 예보를 바꿨어요.", size=19.5, gap=6)
f.ex("A2", "Complete a frase", "제주도", "Nos dias 25-26, mar ao sul de Jeju (previsão)",
     "참피는 25일에서 26일쯤 ___ 남쪽 바다 근처에 올 수 있어요.", size=19.5, gap=6)
f.ex("A2", "Complete a frase", "진로", "A trajetória do tufão ainda pode mudar",
     "태풍의 ___는 아직 바뀔 수 있어요.", size=19.5, gap=6)
f.ex("A2", "Complete a frase", "날씨누리", "As últimas notícias da agência e do «날씨누리»",
     "최신 날씨 정보는 기상청과 '___'에서 볼 수 있어요.", size=19.5, gap=6)
f.end_report()

# ---- search heat box (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "이번 주 검색어", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "한국의 뜨거운 말", 24, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "날짜가 있는 자료만 모았어요", 19, "sans", False, GREY)
topics = [
    "태풍 참피 — 10월 21일 검색 1위 (KoreaTrendBoard)",
    "KIA LG · 가을야구 — 10월 17일 2,000회 이상 검색",
    "치이카와 — 10월 17일 3위, 1,000회 이상 검색",
    "청송사과축제 — 10월 17일 5위, 200회 이상 검색",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 10
yy_n = p.para(gx + 22, byy + 12, "검색 수는 대략적인 숫자예요. '지금 한국에서 뜨거운 말'을 보는 눈금으로 봐 주세요.", 19, "serif", False, GREY, gw - 44, 1.35)
yy_m = p.para(gx + 22, yy_n + 24, "이 네 가지 말은 이번 주 신문의 주제예요.", 19, "serif", False, GREY, gw - 44, 1.35)
p.para(gx + 22, yy_m + 2, "Quatro palavras: os temas desta edição.", 18.5, "sans", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 662, "자료: Google 트렌드 한국 (10월 17일)", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 690, "KoreaTrendBoard (10월 21일)　Valores aprox.", 17, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f0eee5")
p.text(gx + 22, sy + 40, "이번 호의 내용　Índice", 24, "sans", True, OLIVE)
som = [
    ("2면", "태풍 준비와 수능 D-29", "A2"),
    ("3면", "억새축제와 사과의 계절", "A2→B1"),
    ("4면", "가을야구 준플레이오프", "B1"),
    ("5면", "엔믹스와 치이카와", "B1"),
    ("6면", "단풍 절정은 왜 두 개?", "B2"),
    ("7면", "날씨와 날짜의 말", "A2→B2"),
    ("8면", "시험과 답", "Todos"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

# ---- word of the week (col 3) ----
my = 1636
p.text(gx, my + 24, "이번 주의 말　A palavra da semana", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "「북상하다」", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 102, "북쪽으로 올라가다. 태풍 소식에서 자주 보는 말이에요. 예: '태풍이 북상하고 있어요.'", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 8, "북상하다 = avançar para o norte.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "typhoon.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "우주에서 본 슈퍼 태풍의 눈. (2015년 태풍 마이삭, NASA 사진) 참피도 아주 강한 태풍이에요.",
        "사진: NASA — Public domain (Wikimedia Commons)")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-weekend")
f2.head("바쁜 주말", 25)
f2.para("토요일과 일요일, 야구 플레이오프가 시작돼요. 억새축제는 금요일에 끝나요. 주말 계획이 있으면 날씨와 날짜를 먼저 확인하세요.", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX)
p.text(bx + 22, 1914, "짧은 소식　Em resumo", 24, "sans", True, OLIVE)
brefs = [
    ("억새", "서울억새축제는 금요일이 마지막 날이에요. (3면)"),
    ("단풍", "설악산 단풍 절정 날짜가 두 개예요. 왜일까요? (6면)"),
    ("수능", "수능까지 29일 남았어요. 오늘이 D-29예요. (2면)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "퀴즈　Quiz relâmpago", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Leia a primeira página e escolha a resposta certa　Respostas na pág. 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "Escolha múltipla", "B", "Champi é um nome de flor proposto pelo Laos",
      "'참피'는 무슨 이름이에요? A. 나라 이름 · B. 꽃 이름 · C. 사람 이름", size=21)
qf.ex("A2", "Escolha múltipla", "C", "A agência mudou a previsão no dia 21",
      "기상청이 예보를 바꾼 날은 언제예요? A. 19일 · B. 20일 · C. 21일", size=21)
qf.ex("A2", "Escolha múltipla", "A", "O mar ao sul de Jeju, por volta dos dias 25-26 (previsão)",
      "참피가 올 수 있는 곳은 어디예요? A. 제주도 남쪽 바다 · B. 서울 · C. 부산 앞바다", size=21)
qf.ex("A2", "Escolha múltipla", "B", "O vencedor enfrenta o Samsung no domingo",
      "준플레이오프에서 이긴 팀은 일요일에 누구를 만나요? A. kt · B. 삼성 · C. 두산", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-pyoji.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 생활 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("생활　Vida cotidiana", "Lucerna", "레벨 A2　태풍 준비와 수능 D-29　Preparação para o tufão e contagem regressiva para o exame")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("태풍이 오면, 먼저 창문부터 보세요", 32)
f.byline("Lucerna 편집부　읽기 레벨: A2")
f.para("태풍이 가까이 오면 바람이 아주 강해져요. 창문이 깨지거나 베란다의 물건이 날아갈 수 있어요. 그래서 태풍이 오기 전에 집을 한 번 보는 것이 좋아요.")
f.para("준비 목록은 길지 않아요. 첫째, 창문을 단단히 닫고 흔들리는지 봐요. 둘째, 베란다의 화분과 가벼운 물건을 집 안으로 옮겨요. 셋째, 주말에 밖에 나갈 계획이 있으면 날씨를 보고 다시 정해요.")
f.para("그리고 가장 중요한 것! 태풍 소식은 자주 바뀌어요. 어제 본 예보와 오늘 본 예보가 다를 수 있어요. 나가기 전에 기상청의 최신 소식을 꼭 확인하세요.")
f.gloss("단단히 = firmemente · 흔들리다 = balançar · 옮기다 = deslocar · 최신 = o mais recente")
f.head("수능까지 29일 — 오늘은 D-29", 25)
f.para("대학수학능력시험, 줄여서 수능은 11월 19일 목요일에 있어요. 오늘이 10월 21일이니까, 시험까지 29일이 남았어요. 한국에서는 이렇게 'D-29'라고 써요. D는 영어 Day의 D예요.")
f.para("올해 수험생은 551,864명이에요. 시험장은 전국에 1,312곳이에요. 20일, 교육부는 시험 날 아침의 계획을 발표했어요. 회사와 관공서는 10시부터 일을 시작하고, 지하철도 더 자주 다녀요.")
f.para("시험 날에는 비행기도 조용해요. 영어 듣기 시험 시간인 13시 10분부터 13시 35분까지는 비행기가 뜨거나 내리지 않아요. 온 나라가 수험생을 응원해요.")
f.para("시험 날 아침, 가족과 친구들은 시험장 앞에서 수험생을 응원해요. '힘내세요!', '떨지 마세요!', '잘할 수 있어요!' — 이 말이 시험장의 아침을 가득 채워요.")
f.gloss("수험생 = candidato ao exame · 시험장 = local de prova · 관공서 = órgão público · 발표하다 = anunciar, divulgar")
f.box("「D-데이」 사용법　O uso do D-day", [
    ("「수능까지 29일 남았어요 = D-29」", "serif", False, INK, 20, 1.35),
    ("「생일까지 일주일 남았어요 = D-7」", "serif", False, INK, 20, 1.35),
    ("「오늘이 시험 날이에요 = D-데이」", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: study image + facts + 당신 (sequential, measured)
ix = COLX[3]
image(p, "study.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "도서관에서 공부하는 학생들. 수험생에게 가을은 가장 바쁜 계절이에요.",
              "사진: Gary Todd — CC0 (Wikimedia Commons) · 자료 사진")
facts = ["수능은 11월 19일 목요일에 있어요.",
         "올해 수험생은 551,864명이에요.",
         "시험 날 13시 10분부터 13시 35분까지, 비행기도 뜨거나 내리지 않아요."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "알고 있나요", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "당신은? 시험이나 중요한 날까지 며칠 남았어요? 한국어로 두 문장 써서 보내 주세요."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("E você? Quantos dias faltam para o seu exame ou um dia importante? Escreva duas frases em coreano e envie.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "당신은?　E você?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "E você? Quantos dias faltam para o seu exame ou um dia importante? Escreva duas frases em coreano e envie.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- D-day words strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "날짜 세는 말　Contando os dias", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "D-데이로 날짜를 세는 네 가지 말　Quatro formas de contar com o D-day", 20, "sans", False, GREY, anchor="end")
words = [
    ("D-29", "시험까지 29일 남았어요", "Faltam 29 dias"),
    ("D-7", "일주일 남았어요", "Falta uma semana"),
    ("D-1", "내일이에요", "É amanhã"),
    ("D-데이", "오늘이 바로 그날이에요", "É hoje"),
]
for i, (t, lab, cn) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 228, "문장으로 외워요: 「수능까지 29일 남았어요. 오늘이 D-29예요.」", 20.5, "serif", False, INK, RIGHT - MX, 1.42)  # PATCH 2026-10-21: was dy+234 (baseline 1800, 4px above the exercises rule at 1804 — rule grazed glyph bottoms); moved up 6px to match the KO x EN edition's fix

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "연습　Exercícios pág. 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na pág. 8　Os exercícios misturam os níveis: procure pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　이해", 25)
e.expl("Leia os textos da pág. 2 e escolha a resposta certa.")
e.ex("A2", "Escolha múltipla", "B", "Antes do tufão, confira as janelas",
     "태풍이 오기 전에 먼저 보는 것은 무엇이에요? A. 텔레비전 · B. 창문 · C. 냉장고", size=19, gap=6)
e.ex("A2", "Escolha múltipla", "B", "Os vasos da varanda vão para dentro de casa",
     "베란다의 화분은 어떻게 해요? A. 물을 줘요 · B. 집 안으로 옮겨요 · C. 버려요", size=19, gap=6)
e.ex("A2", "Escolha múltipla", "A", "A previsão muda: confira sempre",
     "태풍 소식을 왜 자주 확인해요? A. 예보가 바뀔 수 있어서 · B. 재미있어서 · C. 숙제라서", size=19, gap=6)
e.ex("A2", "Escolha múltipla", "A", "O exame de admissão é quinta-feira, 19 de novembro",
     "수능은 며칠에 있어요? A. 11월 19일 · B. 10월 21일 · C. 11월 9일", size=19, gap=6)
e.ex("A2", "Escolha múltipla", "B", "D-29 = faltam 29 dias",
     "D-29는 무슨 뜻이에요? A. 29일이 지났어요 · B. 29일이 남았어요 · C. 29일에 시작해요", size=19, gap=6)
e.head("B　말 넣기", 25)
e.expl("Coloque a palavra certa no espaço.")
e.ex("A2", "Complete a frase", "단단히", "단단히 = firmemente",
     "창문을 ___ 닫아요.", instr="Complete", size=19, gap=6)
e.ex("A2", "Complete a frase", "옮겨요", "Leve os vasos da varanda para dentro",
     "베란다의 화분을 집 안으로 ___.", instr="Complete", size=19, gap=6)
e.ex("A2", "Complete a frase", "수험생", "수험생 = o aluno que faz o exame de admissão",
     "수능을 보는 학생을 ___이라고 해요.", instr="Complete", size=19, gap=6)
e.ex("A2", "Complete a frase", "시험장", "시험장 = o local onde se faz a prova",
     "시험을 보는 장소를 ___이라고 해요.", instr="Complete", size=19, gap=6)
e.ex("B1", "Complete a frase", "발표", "O ministério anunciou o plano no dia 20",
     "교육부는 20일에 시험 날 계획을 ___했어요.", instr="Complete", size=19, gap=6)
e.head("C　숫자와 날짜", 25)
e.expl("Responda com os números e as datas das págs. 1 e 2.")
e.ex("A2", "Complete a frase", "551,864", "Este ano os candidatos são 551.864",
     "올해 수험생은 ___명이에요.", instr="Complete", size=19, gap=6)
e.ex("A2", "Complete a frase", "1,312", "Os locais de prova são 1.312 em todo o país",
     "시험장은 전국에 ___곳이에요.", instr="Complete", size=19, gap=6)
e.ex("A2", "Complete a frase", "10", "No dia da prova, escritórios e órgãos começam às 10",
     "시험 날, 회사와 관공서는 ___시부터 일을 시작해요.", instr="Complete", size=19, gap=6)
e.ex("B1", "Complete a frase", "35", "Sem decolagens nem pousos das 13:10 às 13:35",
     "비행기가 뜨거나 내리지 않는 시간은 13시 10분부터 13시 ___분까지예요.", instr="Complete", size=19, gap=6)
e.head("D　짝 맞추기", 25)
e.match_set("A2", "Associação",
            ["창문", "화분", "최신 소식", "D-29"],
            ["시험까지 29일이 남았어요",
             "단단히 닫아요",
             "기상청에서 확인해요",
             "집 안으로 옮겨요"],
            ["b", "d", "c", "a"],
            ["창문 = fecha-se firmemente (b)", "화분 = levam-se para dentro (d)", "최신 소식 = confere-se na agência de meteorologia (c)", "D-29 = faltam 29 dias para o exame (a)"],
            instr="Associe")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-saenghwal.svg")
print("P2 saved, exercises so far:", len(REG))
