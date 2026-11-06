# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ko-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 청년 (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("청년 · Juventud", "Lucerna", "레벨 B1 · 수능 카운트다운과 할로윈 · Cuenta atrás del examen y Halloween")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-feature")
f.title("수능까지 12일 — 고3의 가을, 온 나라의 응원", 37)
f.byline("Lucerna 편집부 · 읽기 레벨: B1")
f.para("이번 주 토요일 11월 7일에는 수능까지 12일이 남아요. 수능은 11월 19일 목요일이에요. 올해 수험생은 551,864명이에요. 시험장은 전국에 1,312곳이에요. 고3 교실에서는 마지막 정리가 한창이에요.")
f.para("수능이 가까워지면 온 나라가 수험생을 응원해요. 시험장 앞에서는 '힘내세요!', '떨지 마세요!', '잘할 수 있어요!'라는 말이 가득해요. 합격을 비는 마음으로 찹쌀떡이나 엿을 선물하기도 해요. 끈끈한 음식은 '꼭 붙어라'는 뜻을 담고 있어요.", w=414)
f.para("그런데 조심해야 할 말이 있어요. 시험 날의 특별한 조치는 11월 19일에만 적용돼요. 회사와 관공서가 10시부터 일을 시작하고, 지하철이 더 자주 다니고, 영어 듣기 시간(13시 10분~13시 35분)에 비행기가 뜨거나 내리지 않는 것 — 모두 11월 19일의 일이에요. 이번 주(11월 2~8일)의 조치가 아니에요. 자세한 이야기는 6면에 있어요.")
f.gloss("정리 = repaso, orden · 끈끈하다 = pegajoso · 합격 = aprobado")
f.head("할로윈 — 미리 알려진 안전 계획", 25)
f.para("지난 토요일 10월 31일은 할로윈이었어요. 이 신문이 마감된 10월 26일 현재, 당일의 모습은 아직 알 수 없어요. 다만 미리 발표된 안전 계획은 있어요.", w=424)
f.para("내무부는 10월 23일부터 11월 1일까지를 특별 관리 기간으로 정했어요. 전국 28곳을 중점 관리 지역으로 정했어요. 서울시는 14곳을 관리해요. 그중 8곳이 중점 지역이에요. 이태원, 홍대, 익선동, 명동, 성수, 건대, 강남역, 압구정이에요.")
f.para("서울시의 안전 인력은 3,271명이에요. 그중 이태원에 1,620명이 배치돼요. 10월 31일에는 이태원로가 통제돼요. 인파를 살피는 인공지능 카메라와 드론도 쓰인다고 발표됐어요.")
f.para("할로윈을 즐기려면 사람이 많은 곳에서는 천천히 걷고, 안내를 잘 들으세요. 안전 계획부터 알아두는 것이 좋아요.", w=354)
f.gloss("중점 = prioritario · 배치하다 = desplegar · 통제하다 = controlar")
f.box("이번 주 청년 숫자 · Cifras de la semana", [
    ("551,864명 — 올해 수험생", "serif", False, INK, 20.5, 1.4),
    ("1,312곳 — 전국 시험장", "serif", False, INK, 20.5, 1.4),
    ("3,271명 — 서울시 할로윈 안전 인력 (이태원 1,620명)", "serif", False, INK, 20.5, 1.4),
    ("13시 10분~13시 35분 — 11월 19일 영어 듣기 시간", "serif", False, INK, 20.5, 1.4, 338),
])
f.head("시험 전날의 하루", 25)
f.para("시험 전날에는 일찍 자요. 밤늦게까지 공부하면 아침에 피곤해져요. 준비물은 미리 챙겨요. 수험표와 신분증, 연필을 가방에 넣어요.")
f.para("아침밥은 꼭 먹어요. 밥을 먹어야 머리가 잘 돌아가요. 너무 많이 먹으면 졸려요. 평소 먹던 대로 먹는 것이 좋아요.")
f.gloss("챙기다 = preparar · 졸리다 = tener sueño · 평소 = habitualmente")
f.head("합격 기원 음식", 25)
f.para("합격을 비는 마음으로 찹쌀떡이나 엿을 선물해요. 엿을 먹으면 시험에 '붙어라'는 뜻이에요. 끈끈한 음식은 꼭 붙으라는 뜻을 담고 있어요.")
f.para("미역국을 피하는 사람도 있어요. 미역은 미끄럽다는 뜻이 있기 때문이에요. 미끄러지면 안 되니까, 시험 날 아침에는 미역국을 먹지 않아요.")
f.gloss("비다 = desear, rogar · 피하다 = evitar · 미끄럽다 = resbaladizo")
f.end_report()

# col 3: study image + 당신
ix = COLX[3]
image(p, "study.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "도서관에서 공부하는 학생들. 수험생에게 가을은 가장 바쁜 계절이에요.",
              "사진: Gary Todd — CC0 (Wikimedia Commons) · 자료 사진")
ey3 = cy3 + 24
etvous = "당신은? 수험생에게 해 주고 싶은 응원 한마디는 뭐예요? 한국어로 두 문장 써서 보내 주세요."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("¿Y tú? ¿Qué ánimo quieres dar a un candidato? Escribe dos frases en coreano; envíalas.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "당신은? · ¿Y tú?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "¿Y tú? ¿Qué ánimo quieres dar a un candidato? Escribe dos frases en coreano; envíalas.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "연습 · Ejercicios pág. 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la pág. 8 · Los ejercicios mezclan niveles: busca por número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · 이해", 25)
e.glossline("Lee los textos de la pág. 5 y elige la respuesta correcta.")
e.ex("B1", "Opción múltiple", "A", "El 7 de noviembre es D-12",
     "11월 7일에는 수능까지 며칠이 남아요? A. 12일 · B. 17일 · C. 29일", size=20, gap=7)
e.ex("B1", "Opción múltiple", "B", "El examen es el jueves 19 de noviembre",
     "수능은 며칠에 있어요? A. 11월 7일 · B. 11월 19일 · C. 11월 28일", size=20, gap=7)
e.ex("B1", "Opción múltiple", "A", "Sin vuelos durante la escucha",
     "영어 듣기 시간에 비행기는 어떻게 돼요? A. 뜨거나 내리지 않아요 · B. 평소대로 다녀요 · C. 더 자주 다녀요", size=20, gap=7)
e.ex("B1", "Opción múltiple", "B", "Seguridad de Halloween en Seúl: 3.271 personas",
     "서울시 할로윈 안전 인력은 몇 명이에요? A. 1,620명 · B. 3,271명 · C. 551,864명", size=20, gap=7)
e.ex("B1", "Opción múltiple", "A", "La calle de Itaewon se cierra el 31 de octubre",
     "이태원로가 통제되는 날은 언제예요? A. 10월 31일 · B. 11월 7일 · C. 11월 19일", size=20, gap=7)
e.head("B · 말 넣기", 25)
e.glossline("Pon la palabra adecuada en el hueco.")
e.ex("B1", "Completar", "응원", "Todo el país anima a los candidatos",
     "온 나라가 수험생을 ___해요.", instr="Completa", size=20, gap=7)
e.ex("B1", "Completar", "카운트다운", "La cuenta atrás continúa",
     "수능 ___이 계속돼요.", instr="Completa", size=20, gap=7)
e.ex("B1", "Completar", "선물", "Regalo de tteok y caramelo para aprobar",
     "합격을 비는 마음으로 찹쌀떡이나 엿을 ___하기도 해요.", instr="Completa", size=20, gap=7, bw=424)
e.ex("B1", "Completar", "인력", "El personal de seguridad de Seúl: 3.271 personas",
     "서울시의 안전 ___은 3,271명이에요.", instr="Completa", size=20, gap=7)
e.ex("B1", "Completar", "통제", "La calle de Itaewon se cierra el 31 de octubre",
     "10월 31일에는 이태원로가 ___돼요.", instr="Completa", size=20, gap=7)
e.head("C · 숫자와 날짜", 25)
e.glossline("Responde con las cifras de la pág. 5.")
e.ex("B1", "Completar", "551,864", "Este año hay 551.864 candidatos",
     "올해 수험생은 ___명이에요.", instr="Completa", size=20, gap=7)
e.ex("B1", "Completar", "1,312", "Hay 1.312 centros de examen en todo el país",
     "시험장은 전국에 ___곳이에요.", instr="Completa", size=20, gap=7)
e.ex("B1", "Completar", "10", "El día del examen, las oficinas abren a las 10",
     "시험 날, 회사와 관공서는 ___시부터 일을 시작해요.", instr="Completa", size=20, gap=7, bw=354)
e.ex("B1", "Completar", "1,620", "En Itaewon se despliegan 1.620 personas",
     "이태원에 배치되는 안전 인력은 ___명이에요.", instr="Completa", size=20, gap=7)
e.head("D · 문장 만들기", 25)
e.glossline("Ordena las palabras y forma la frase.")
e.ex("B1", "Formar una frase", "수험생은 열심히 공부해요.", "Orden: sujeto + adverbio + verbo",
     "수험생은 / 열심히 / 공부해요 → ___", instr="Forma la frase", size=20, gap=7)
e.ex("B1", "Formar una frase", "우리는 수험생을 응원해요.", "Orden: sujeto + objeto + verbo",
     "우리는 / 수험생을 / 응원해요 → ___", instr="Forma la frase", size=20, gap=7)
e.ex("B1", "Formar una frase", "비행기는 듣기 시간에 뜨지 않아요.", "Sin vuelos durante la escucha",
     "비행기는 / 듣기 시간에 / 뜨지 않아요 → ___", instr="Forma la frase", size=20, gap=7)
e.ex("B1", "Formar una frase", "서울시는 14곳을 관리해요.", "Seúl gestiona 14 lugares",
     "서울시는 / 14곳을 / 관리해요 → ___", instr="Forma la frase", size=20, gap=7)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-cheongnyeon.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 깊이 읽기 (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("깊이 읽기 · Lectura profunda", "Lucerna", "레벨 B2 · 수능 카운트다운을 읽는 법 · Cómo leer la cuenta atrás del examen")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-feature")
f.title("수능 카운트다운을 읽는 법 — 날짜, 조치, 분위기를 나누세요", 37)
f.byline("Lucerna 편집부 · 읽기 레벨: B2")
f.para("이번 주 신문에는 수능 이야기가 많아요. 그런데 수능 이야기를 읽을 때는 세 가지를 나눠야 해요. 날짜, 조치, 분위기예요. 날짜는 11월 19일 목요일이에요. 조치는 시험 날에만 적용돼요. 분위기는 지금, 이번 주에 있어요. 세 가지를 섞으면 뉴스를 잘못 읽게 돼요.", w=404)
f.para("분위기부터 봐요. 이번 주는 D-17에서 D-12로 가는 주간이에요. 교실과 집에서는 마지막 정리가 한창이에요. 시험장 앞의 응원, 찹쌀떡과 엿의 선물 — 이 모두가 분위기예요. 분위기는 날짜가 정해져 있지 않아요. 시험이 가까워질수록 짙어져요.")
f.para("조치는 달라요. 11월 19일 시험 날에는 회사와 관공서가 10시부터 일을 시작해요. 지하철이 더 자주 다녀요. 영어 듣기 시간인 13시 10분부터 13시 35분까지는 비행기가 뜨거나 내리지 않아요. 시험장 앞 200미터 안에서는 차가 통제돼요. 이 조치는 11월 19일의 조치예요. 11월 2일부터 8일까지의 조치로 읽으면 안 돼요.")
f.para("숫자도 읽는 법이 있어요. 올해 수험생은 551,864명, 시험장은 1,312곳이에요. 큰 숫자는 나라 전체의 규모를 보여줘요. 숫자가 크다고 해서 개인의 시험이 더 어려워지는 것은 아니에요. 내 시험장은 1,312곳 중 한 곳일 뿐이에요.")
f.para("그래서 뉴스를 읽을 때는 날짜를 먼저 보세요. '수능이 가까워졌다'는 말은 분위기예요. '수능 조치가 시작됐다'는 말은 11월 19일의 일이에요. 날짜와 조치를 나누면, 뉴스가 훨씬 쉽게 읽혀요.", w=394)
f.gloss("짙어지다 = intensificarse · 규모 = escala · 섞다 = mezclar")
f.head("숫자를 읽을 때", 25)
f.para("큰 숫자를 보면 겁이 날 수 있어요. 551,864명이라는 숫자는 나라 전체의 수험생이에요. 그중 한 명이 바로 나예요. 큰 숫자보다 내 준비가 더 중요해요.", w=374)
f.gloss("겁이 나다 = tener miedo · 중요하다 = importante")
f.head("뉴스의 날짜 찾기", 25)
f.para("뉴스를 읽을 때는 제목보다 날짜를 먼저 봐요. 날짜가 있는 뉴스가 믿을 수 있어요.", w=374)
f.para("'예정'과 '확정'도 나눠야 해요. 예정은 아직 정해지지 않은 일, 확정은 정해진 일이에요. 예정된 일을 확정된 일처럼 읽으면 안 돼요.")
f.gloss("예정 = previsto · 확정 = confirmado · 믿다 = creer")
f.end_report()

# ---- comparison table (cols 0-2) ----
ty = 1210
p.text(MX, ty + 26, "이번 주와 시험 날, 한눈에 보기 · Esta semana y el día del examen, de un vistazo", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "연습 · Ejercicios pág. 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la pág. 8 · Los ejercicios mezclan niveles: busca por número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · 표 읽기", 25)
e.glossline("Lee la tabla de la pág. 6 y elige la respuesta correcta.")
e.ex("B2", "Opción múltiple", "B", "Esta semana, la cuenta atrás va de D-17 a D-12",
     "이번 주의 날짜 세기는 뭐예요? A. D-데이 · B. D-17 ~ D-12 · C. D-1", size=20, gap=7)
e.ex("B2", "Opción múltiple", "A", "El día del examen hay medidas especiales",
     "시험 날의 특별 조치는 있어요? A. 있어요 · B. 없어요 · C. 아직 몰라요", size=20, gap=7)
e.ex("B2", "Opción múltiple", "B", "Esta semana no hay medidas especiales",
     "이번 주의 특별 조치는 있어요? A. 있어요 · B. 없어요 · C. 10시 출근만 있어요", size=20, gap=7)
e.ex("B2", "Opción múltiple", "C", "El día del examen es el día D",
     "시험 날의 날짜 세기는 뭐예요? A. D-17 · B. D-12 · C. D-데이", size=20, gap=7)
e.ex("B2", "Opción múltiple", "A", "El ambiente de esta semana es la cuenta atrás",
     "이번 주의 분위기는 뭐예요? A. 카운트다운 · B. 시험 당일 · C. 방학", size=20, gap=7)
e.head("B · 이해", 25)
e.glossline("Lee los textos de la pág. 6 y elige la respuesta correcta.")
e.ex("B2", "Opción múltiple", "A", "El ambiente está ahora, esta semana",
     "분위기는 언제 있어요? A. 지금, 이번 주 · B. 11월 19일에만 · C. 지난주에만", size=20, gap=7)
e.ex("B2", "Opción múltiple", "B", "Las medidas solo se aplican el 19 de noviembre",
     "특별 조치는 언제 적용돼요? A. 11월 2일부터 · B. 11월 19일에만 · C. 11월 7일부터", size=20, gap=7)
e.ex("B2", "Opción múltiple", "A", "La comprensión auditiva es de 13:10 a 13:35",
     "영어 듣기 시간은 언제예요? A. 13시 10분~13시 35분 · B. 10시~12시 · C. 자정", size=20, gap=7)
e.ex("B2", "Opción múltiple", "A", "Este año hay 551.864 candidatos",
     "올해 수험생은 몇 명이에요? A. 551,864명 · B. 1,312명 · C. 3,271명", size=20, gap=7)
e.ex("B2", "Opción múltiple", "B", "Hay 1.312 centros de examen en todo el país",
     "시험장은 전국에 몇 곳이에요? A. 551,864곳 · B. 1,312곳 · C. 3,271곳", size=20, gap=7)
e.head("C · 말 넣기", 25)
e.glossline("Pon la palabra adecuada en el hueco.")
e.ex("B2", "Completar", "분위기", "La cuenta atrás es el ambiente de esta semana",
     "카운트다운은 이번 주의 ___예요.", instr="Completa", size=20, gap=7)
e.ex("B2", "Completar", "조치", "Las medidas especiales solo se aplican el día del examen",
     "특별 ___는 11월 19일에만 적용돼요.", instr="Completa", size=20, gap=7)
e.ex("B2", "Completar", "카운트다운", "La semana que va de D-17 a D-12",
     "이번 주는 D-17에서 D-12로 가는 ___ 주간이에요.", instr="Completa", size=20, gap=7)
e.ex("B2", "Completar", "규모", "Las cifras grandes muestran la escala nacional",
     "큰 숫자는 나라 전체의 ___를 보여줘요.", instr="Completa", size=20, gap=7)
e.head("D · 맞다 틀리다", 25)
e.glossline("Elige «verdadero» si la frase es correcta y «falso» si no lo es.")
e.ex("B2", "Verdadero o falso", "틀리다", "Las medidas especiales: solo el 19 de noviembre",
     "특별 조치는 11월 2일부터 적용돼요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.ex("B2", "Verdadero o falso", "맞다", "El 7 de noviembre es D-12",
     "11월 7일은 D-12예요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.ex("B2", "Verdadero o falso", "틀리다", "Aviones restringidos durante la comprensión auditiva",
     "시험 날 비행기는 평소대로 다녀요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.ex("B2", "Verdadero o falso", "맞다", "Esta semana es ambiente de cuenta atrás",
     "이번 주는 카운트다운 분위기예요. A. 맞다 · B. 틀리다", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-gipi.svg")
print("P6 saved, exercises so far:", len(REG))
