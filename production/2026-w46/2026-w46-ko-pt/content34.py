# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ko-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 문화 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("문화 · Cultura", "Lucerna", "레벨 A2→B1 · 단풍과 11월 11일의 세 이름 · Folhas de outono e os três nomes de 11 de novembro")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-feature")
f.title("단풍은 아직, 11월 11일은 세 가지 이름", 37)
f.byline("Lucerna 편집부 · 읽기 레벨: A2→B1")
f.para("단풍 이야기는 이번 주에도 계속돼요. 산림청·국립수목원 예보(9월 22일 발표)는 월출산 절정을 11월 9일로 봐요. 두륜산 절정은 11월 11일로 봐요. 국립공원공단·웨더아이 예보는 내장산 절정을 11월 11일로 봐요. 날짜를 말할 때는 어느 기관의 예보인지 꼭 말해야 해요.")
f.para("그런데 예보 날짜와 실제 관측 날짜는 달라요. 기상청 관측으로는 10월 24일 현재 내장산은 아직 단풍 전이었어요. 설악산 실제 관측 절정은 10월 16일이었어요. 이 신문이 마감한 11월 2일 현재, 내장산과 월출산의 실제 관측 절정은 아직 발표되지 않았어요. 관측 결과는 날씨누리에서 확인하세요.", w=424)
f.para("정읍시 전망도 있어요. 정읍시는 내장산 절정을 11월 7~8일경으로 봤어요. 산림청 예보 11월 4일, 공단 예보 11월 11일과 또 달라요. 전망과 예보와 관측 — 세 가지 말을 나누면 단풍 뉴스가 쉽게 읽혀요. 구간별 공식 수치는 없어요. 기관이 구간별로 값을 내지 않아요.")
f.para("내장산에 갈 때는 차를 조심하세요. 10월 30일부터 11월 15일까지는 공원 안에서 차가 통제돼요. 내장호주차장에서 무료 순환버스를 타야 해요. 산불조심기간이라는 것도 잊지 마세요. 11월 1일부터 12월 15일까지예요.")
f.gloss("전망 = perspetiva, previsão · 나누다 = distinguir · 통제하다 = controlar · 순환버스 = autocarro circular")
f.head("11월 11일 — 이름이 세 개인 날", 25)
f.para("수요일 11월 11일은 이름이 세 개예요. 빼빼로데이, 농업인의 날, 가래떡데이예요. 빼빼로데이는 숫자 1이 네 개 겹치는 모양에서 왔어요. 길고 가늰 과자를 친구와 나누는 날이에요. 빼빼로는 1983년에 나왔어요.", w=414)
f.para("농업인의 날은 법으로 정한 기념일이에요. 1996년부터 11월 11일이 농업인의 날이에요. 흙 토(土) 자를 열 십(十)과 한 일(一)로 나눌 수 있어서예요. 농업을 생각하고 농업인에게 감사하는 날이에요.")
f.para("가래떡데이는 2006년부터 시작됐어요. 우리 쌀로 만든 가래떡을 나누는 날이에요. 빼빼로 대신 가래떡을 선물하는 사람도 있어요. 같은 날짜, 다른 이름 — 세 이름의 뜻을 알면 11월 11일이 더 재미있어요.")
f.gloss("겹치다 = sobrepor-se · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, partilhar")
f.head("단풍 구경, 이렇게 가세요", 25)
f.para("단풍 구경을 갈 때는 대중교통을 이용하면 편해요. 차를 가져가면 길이 막힐 수 있어요. 내장산에서는 무료 순환버스를 타세요.")
f.para("산에서는 쓰레기를 가져와요. 먹고 마신 것은 가방에 넣어요. 자연을 깨끗이 두는 것이 단풍 구경의 예의예요.")
f.gloss("이용하다 = usar · 막히다 = congestionado · 예의 = boas maneiras.")
f.head("가을 산책의 옷차림", 25)
f.para("가을 산책에서는 옷을 겹쳐 입어요. 아침은 춥고 낮에는 따뜻해져요. 겹쳐 입으면 더울 때 벗을 수 있어요.")
f.para("신발은 편한 것으로 신어요. 산길은 돌이 많아요. 미끄러지지 않는 신발이 좋아요. 물도 챙겨요.")
f.gloss("겹쳐 입다 = vestir em camadas · 미끄러지다 = escorregar · 돌 = pedra.")
f.box("단풍 구경 준비물 · O que levar", [
    ("물", "serif", False, INK, 20, 1.35),
    ("간식", "serif", False, INK, 20, 1.35),
    ("카메라", "serif", False, INK, 20, 1.35),
    ("따뜻한 옷", "serif", False, INK, 20, 1.35),
    ("쓰레기 봉투", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: bukhansan-ui image + facts + apples + 당신
ix = COLX[3]
image(p, "bukhansan-ui.jpg", ix, 200, CW, 185)
cy3 = caption(p, ix, 385, CW, "북한산우이역 승강장. 단풍철에는 대중교통이 편해요.",
              "사진: Udonhan1992 — CC0 (Wikimedia Commons) · 자료 사진")
facts = ["월출산 절정: 산림청 예보 11월 9일",
         "내장산 절정: 공단 예보 11월 11일",
         "두륜산 절정: 산림청 예보 11월 11일",
         "11월 11일: 이름이 세 개인 날"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "단풍 달력", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
image(p, "apples.jpg", ix, ay3, CW, 200)
cy4 = caption(p, ix, ay3 + 200, CW - 80, "사과는 가을의 과일이에요. 화가 세잔이 그린 사과예요.",
              "그림: Paul Cézanne — Public domain (Wikimedia Commons)")
ey3 = cy4 + 18
etvous = "당신은? 11월 11일에 빼빼로와 가래떡 중 무엇을 나누고 싶어요? 한국어로 두 문장 써서 보내 주세요."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44 - 60)) * 30.5 + 12 + len(wrap("E tu? A 11 de novembro, preferes partilhar Pepero ou garaetteok? Escreve duas frases em coreano e envia-nos.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "당신은? · E você?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44 - 60, 1.42) + 10
p.para(ix + 22, yy3 + 20, "E tu? A 11 de novembro, preferes partilhar Pepero ou garaetteok? Escreve duas frases em coreano e envia-nos.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "연습 · Exercícios pág. 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na pág. 8 · Os exercícios misturam os níveis: procure pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · 이해", 25)
e.glossline("Leia os textos da pág. 3 e escolha a resposta certa.")
e.ex("A2", "Escolha múltipla", "A", "Wolchulsan, serviço florestal: pico a 9 de novembro",
     "월출산 산림청 예보의 절정은 언제예요? A. 11월 9일 · B. 11월 11일 · C. 11월 4일", size=20, gap=7)
e.ex("A2", "Escolha múltipla", "B", "Naejangsan, corporação de parques: pico a 11 de novembro",
     "내장산 공단 예보의 절정은 언제예요? A. 11월 4일 · B. 11월 11일 · C. 11월 9일", size=20, gap=7)
e.ex("B1", "Escolha múltipla", "A", "Seoraksan, observação real: pico a 16 de outubro",
     "설악산 실제 관측 절정은 언제였어요? A. 10월 16일 · B. 10월 20일 · C. 10월 24일", size=20, gap=7)
e.ex("A2", "Escolha múltipla", "B", "11 de novembro tem três nomes",
     "11월 11일은 이름이 몇 개예요? A. 한 개 · B. 세 개 · C. 다섯 개", size=20, gap=7)
e.ex("B1", "Escolha múltipla", "A", "O dia do garaetteok existe desde 2006",
     "가래떡데이는 언제부터 시작됐어요? A. 2006년부터 · B. 1983년부터 · C. 1996년부터", size=20, gap=7)
e.head("B · 말 넣기", 25)
e.glossline("Coloque a palavra certa no espaço.")
e.ex("A2", "Complete a frase", "절정", "O auge das folhas de outono chama-se 절정",
     "단풍이 가장 아름다운 때를 ___이라고 해요.", instr="Preencha", size=20, gap=7)
e.ex("B1", "Complete a frase", "예보", "As datas previstas e as observadas são diferentes",
     "___ 날짜와 실제 관측 날짜는 달라요.", instr="Preencha", size=20, gap=7)
e.ex("B1", "Complete a frase", "관측", "Observação real: 16 de outubro",
     "설악산 실제 ___ 절정은 10월 16일이었어요.", instr="Preencha", size=20, gap=7)
e.ex("A2", "Complete a frase", "농업인", "11 de novembro é o dia do agricultor",
     "11월 11일은 ___의 날이에요.", instr="Preencha", size=20, gap=7)
e.ex("A2", "Complete a frase", "가래떡", "No dia do garaetteok partilham-se garaetteok",
     "가래떡데이에는 ___을 나눠요.", instr="Preencha", size=20, gap=7)
e.head("C · 숫자와 날짜", 25)
e.glossline("Responda com os números e as datas da pág. 3.")
e.ex("A2", "Complete a frase", "9", "Wolchulsan, serviço florestal: dia 9",
     "월출산 산림청 예보의 절정은 11월 ___일이에요.", instr="Preencha", size=20, gap=7)
e.ex("A2", "Complete a frase", "11", "Naejangsan, corporação de parques: dia 11",
     "내장산 공단 예보의 절정은 11월 ___일이에요.", instr="Preencha", size=20, gap=7)
e.ex("B1", "Complete a frase", "11", "Duryunsan, serviço florestal: dia 11",
     "두륜산 산림청 예보의 절정은 11월 ___일이에요.", instr="Preencha", size=20, gap=7)
e.ex("B1", "Complete a frase", "16", "Seoraksan, observação real: dia 16",
     "설악산 실제 관측 절정은 10월 ___일이었어요.", instr="Preencha", size=20, gap=7)
e.head("D · 짝 맞추기", 25)
e.match_set("A2", "Associe pares",
            ["내장산", "월출산", "두륜산", "설악산"],
            ["산림청 예보 11월 9일",
             "공단 예보 11월 11일",
             "실제 관측 10월 16일",
             "산림청 예보 11월 11일"],
            ["b", "a", "d", "c"],
            ["내장산 = previsão da corporação de parques: dia 11 b", "월출산 = previsão florestal: dia 9 a", "두륜산 = previsão florestal: dia 11 d", "설악산 = observação real a 16 de outubro c"],
            instr="Associe", narrow={3: 340})
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-munhwa.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · 스포츠 (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("스포츠 · Esporte", "Lucerna", "레벨 B1 · 플레이오프 결과와 한국시리즈 · Resultado do playoff e Korean Series")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P4-feature")
f.title("삼성이 올라갔어요 — 한국시리즈는 kt wiz와 삼성", 37)
f.byline("Lucerna 편집부 · 읽기 레벨: B1")
f.para("플레이오프 결과가 나왔어요. 삼성 라이온즈가 KIA 타이거즈를 3승 2패로 이겼어요. 1차전은 10월 26일 대구에서 KIA가 5대 1로 이겼어요. 2차전은 10월 27일 대구에서 삼성이 8대 3으로 이겼어요. 3차전은 10월 29일 광주에서 삼성이 6대 4로 이겼어요. 4차전은 10월 30일 광주에서 KIA가 4대 2로 이겼어요. 5차전은 11월 1일 대구에서 삼성이 6대 1로 이겼어요.")
f.para("이제 한국시리즈예요. 정규시즌 1위 kt wiz와 삼성이 싸워요. 발표된 일정은 1차전 11월 3일 수원, 2차전 11월 4일 수원, 3차전 11월 6일 대구, 4차전 11월 7일 대구, 5차전 11월 8일 대구, 6차전 11월 10일 수원, 7차전 11월 11일 수원이에요. 평일은 18시 30분, 토요일과 일요일은 14시에 시작해요.")
f.para("조심해야 할 말이 있어요. 이 신문은 11월 2일에 마감했어요. 그래서 1차전부터 5차전까지의 결과는 이 신문에 없어요. 결과는 KBO 홈페이지에서 확인하세요. 6차전과 7차전은 시리즈가 그만큼 이어질 때만 열려요. 한 팀이 먼저 4승을 하면 남은 경기는 열리지 않아요.")
f.para("한국시리즈 일정이 하루 밀린 이유도 알아두세요. 플레이오프 1차전이 10월 25일 비 때문에 미뤄졌고, 플레이오프가 5차전까지 갔어요. 시리즈 사이에는 이동일이 하루 필요해요. 그래서 처음 발표된 11월 2일 시작이 11월 3일로 밀렸어요.")
f.para("지난 소식도 확인해요. 준플레이오프에서는 KIA가 LG를 3연승으로 이겼어요. 1차전 5대 1, 2차전 6대 3, 3차전 13대 1이었어요. 가을야구는 정규시즌이 끝난 뒤에 열려요. 아래 그림처럼 한 칸씩 올라가서, 마지막에 한국시리즈에서 싸워요.", w=384)
f.gloss("밀리다 = ser adiado · 이동일 = dia de deslocação · 이어지다 = continuar · 먼저 = primeiro")
f.head("야구장의 응원", 25)
f.para("야구장에서는 응원이 또 하나의 재미예요. 팬들은 노래를 부르고 손을 흔들어요. 응원하는 팀의 노래를 함께 부르면 경기장이 하나가 돼요.")
f.gloss("흔들다 = agitar · 하나가 되다 = tornar-se um só.")
f.head("결과 없는 경기", 25)
f.para("아직 열리지 않은 경기는 점수가 없어요. 그래서 이 신문은 결과만 전해요. 예상 점수를 진짜 점수처럼 말하면 안 돼요. 마감일 뒤의 경기는 직접 확인하세요.")
f.gloss("예상 = previsão.")
f.end_report()

# ---- ladder diagram (cols 0-2) ----
ly = 1210
p.text(MX, ly + 26, "한국시리즈까지의 길 · O caminho até a Série Coreana", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ly + 40, GOLD, 2)
steps = [
    ("와일드카드", "LG가 두산에\n4대 1로 승리"),
    ("준플레이오프", "KIA가 LG에\n3연승으로 승리"),
    ("플레이오프", "삼성이 KIA에\n3승 2패로 승리"),
    ("한국시리즈", "kt wiz vs 삼성\n11월 3일 시작"),
]
bw, bh, by0 = 320, 118, ly + 58
for i, (t, d) in enumerate(steps):
    x0 = MX + i * (bw + 26)
    p.rect(x0, by0, bw, bh, fill=BOX if i != 2 else "#f1ead6", stroke=OLIVE if i == 2 else LINE, sw=1.6 if i == 2 else 1.2)
    p.text(x0 + bw / 2, by0 + 40, t, 24, "sans", True, OLIVE, anchor="middle")
    for j, ln in enumerate(d.split("\n")):
        p.text(x0 + bw / 2, by0 + 76 + j * 28, ln, 20, "serif", False, INK, anchor="middle")
    if i < 3:
        ax = x0 + bw + 3
        p.add(f'<path d="M{ax} {by0 + bh/2 - 9} L{ax + 20} {by0 + bh/2} L{ax} {by0 + bh/2 + 9}" fill="none" stroke="{OLIVE}" stroke-width="2.6"/>')
p.para(MX, by0 + bh + 34, "위 그림은 가을야구의 순서예요. 지금은 마지막 칸, 한국시리즈예요.", 20.5, "serif", False, GREY, 1388, 1.4)

# col 3: baseball image + calendar facts
ix = COLX[3]
image(p, "baseball.jpg", ix, 200, CW, 240)
cy3 = caption(p, ix, 440, CW, "20세기 초 미국의 야구팀. 야구의 가을은 길어요.",
              "사진: Bain News Service — Public domain (Wikimedia Commons)")
facts = ["플레이오프: 삼성 3승 2패 (KIA 상대)",
         "1차전: 10월 26일 KIA 5-1",
         "5차전: 11월 1일 삼성 6-1",
         "한국시리즈: 11월 3일 수원 시작"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "가을야구 달력", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P4 col3 ends", sy3 + sh)

# ---- P4 exercises ----
ey = 1560
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "연습 · Exercícios pág. 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na pág. 8 · Os exercícios misturam os níveis: procure pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · 이해", 25)
e.glossline("Leia os textos da pág. 4 e escolha a resposta certa.")
e.ex("B1", "Escolha múltipla", "A", "Samsung ganhou o playoff",
     "플레이오프에서 이긴 팀은 어디예요? A. 삼성 · B. KIA · C. LG", size=20, gap=7)
e.ex("B1", "Escolha múltipla", "C", "A série: 3 vitórias e 2 derrotas",
     "플레이오프 시리즈 전적은 어떻게 돼요? A. 3연승 · B. 2승 3패 · C. 3승 2패", size=20, gap=7)
e.ex("B1", "Escolha múltipla", "B", "Jogo 5, 1 de novembro, Daegu: Samsung 6–1",
     "5차전은 어디에서, 몇 대 몇이었어요? A. 광주 4대 2 · B. 대구 6대 1 · C. 수원 5대 1", size=20, gap=7)
e.ex("B1", "Escolha múltipla", "A", "As Korean Series começam a 3 de novembro em Suwon",
     "한국시리즈 1차전은 언제, 어디예요? A. 11월 3일 수원 · B. 11월 2일 수원 · C. 11월 6일 대구", size=20, gap=7)
e.ex("B1", "Escolha múltipla", "B", "Fecho a 2 de novembro; resultados dos jogos 1 a 5 desconhecidos",
     "이 신문에 한국시리즈 1~5차전 결과가 없어요. 왜예요? A. 경기가 취소됐어요 · B. 신문이 11월 2일에 마감했어요 · C. 결과가 비밀이에요", size=20, gap=7)
e.head("B · 말 넣기", 25)
e.glossline("Coloque a palavra certa no espaço.")
e.ex("B1", "Complete a frase", "3승 2패", "Samsung vence KIA 3–2",
     "삼성이 KIA를 ___로 이겼어요.", instr="Preencha", size=20, gap=7)
e.ex("B1", "Complete a frase", "수원", "Korean Series, jogos 1 e 2 em Suwon",
     "한국시리즈 1차전과 2차전은 ___에서 열려요.", instr="Preencha", size=20, gap=7)
e.ex("B1", "Complete a frase", "밀렸어요", "A abertura atrasa um dia por causa da chuva e do jogo 5",
     "한국시리즈 시작이 하루 ___.", instr="Preencha", size=20, gap=7)
e.ex("B1", "Complete a frase", "4승", "Quem ganhar 4 jogos é campeão; os outros não se jogam",
     "한 팀이 먼저 ___을 하면 남은 경기는 열리지 않아요.", instr="Preencha", size=20, gap=7)
e.ex("B1", "Complete a frase", "이동일", "É preciso um dia de deslocação entre séries",
     "시리즈 사이에는 ___이 하루 필요해요.", instr="Preencha", size=20, gap=7)
e.head("C · 문장 바꾸기", 25)
e.glossline("Passe as frases para o passado. (Todas estão nesta edição.)")
e.ex("B1", "Reescreva", "삼성이 KIA를 이겼어요.", "O passado de 이기다 é 이겼어요",
     "삼성이 KIA를 이겨요. → ___", instr="Reescreva", size=20, gap=7)
e.ex("B1", "Reescreva", "1차전이 대구에서 열렸어요.", "O passado de 열리다 é 열렸어요",
     "1차전이 대구에서 열려요. → ___", instr="Reescreva", size=20, gap=7)
e.ex("B1", "Reescreva", "한국시리즈가 하루 밀렸어요.", "O passado de 밀리다 é 밀렸어요",
     "한국시리즈가 하루 밀려요. → ___", instr="Reescreva", size=20, gap=7)
e.ex("B1", "Reescreva", "삼성이 5차전에서 이겼어요.", "O passado de 이기다 é 이겼어요",
     "삼성이 5차전에서 이겨요. → ___", instr="Reescreva", size=20, gap=7)
e.head("D · 짝 맞추기", 25)
e.match_set("B1", "Associe pares",
            ["준플레이오프", "플레이오프", "한국시리즈", "이동일"],
            ["kt wiz와 삼성이 싸워요",
             "KIA가 LG를 3연승으로 이겼어요",
             "시리즈 사이에 하루가 필요해요",
             "삼성이 KIA를 3승 2패로 이겼어요"],
            ["b", "d", "a", "c"],
            ["준플레이오프 = KIA venceu três seguidas b", "플레이오프 = Samsung 3–2 d", "한국시리즈 = kt contra Samsung a", "이동일 = um dia entre séries c"],
            instr="Associe")
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-seupocheu.svg")
print("P4 saved, exercises so far:", len(REG))
