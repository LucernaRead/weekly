# -*- coding: utf-8 -*-
# W47 ES core (VOL.4) — P8: 38 exercises + registry-generated answers. Dash style, as W46.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS　연습과 답", "La Lucerna", "8면　La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "A", "el flamenco suena = 플라멩코가 울려요",
     "El lunes, el flamenco ___ en la calle. (A. suena · B. duerme)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "empieza la campaña = 선거 운동이 시작해요",
     "La campaña ___ el viernes 13. (A. termina · B. empieza)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "laSexta 토론 21:30",
     "El debate de laSexta fue a las ___. (A. 21:30 · B. 9:00)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "el voto por correo se pide hasta el jueves 19",
     "El voto por correo se pide hasta el ___. (A. jueves 19 · B. lunes 16)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "la Liga vuelve = 리그가 돌아와요",
     "La Liga ___ el viernes 20. (A. vuelve · B. para)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "세비야 더비는 토요일이에요",
     "El derbi Sevilla–Betis es el ___. (A. domingo · B. sábado)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "Santa Cecilia = 음악가들의 수호성인",
     "Santa Cecilia es la patrona de los ___. (A. músicos · B. futbolistas)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "스페인이 29일 일요일에 투표해요",
     "El domingo 29, España ___. (A. vota · B. duerme)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "객관식", "A", "선거 운동은 11월 13일 금요일에 시작해요",
     "La campaña electoral empieza el... A. viernes 13 · B. lunes 16 · C. domingo 29", size=15.5, gap=1)
f.ex("A2", "객관식", "B", "세계 플라멩코의 날, 11월 16일",
     "El Día del Flamenco es el... A. domingo 22 · B. lunes 16 · C. viernes 20", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "우편 투표는 19일까지 신청해야 해요",
     "El voto por correo se pide hasta... A. jueves 19 · B. viernes 20 · C. sábado 28", size=15.5, gap=1)
f.ex("B1", "객관식", "C", "세비야 더비, 토요일 18:30",
     "El derbi Sevilla–Betis es el sábado a las... A. 14:00 · B. 21:00 · C. 18:30", size=15.5, gap=1)
f.ex("B1", "객관식", "B", "블랙프라이데이, 11월 27일 금요일",
     "El Black Friday es el... A. domingo 29 · B. viernes 27 · C. lunes 16", size=15.5, gap=1)
f.ex("B1", "객관식", "C", "MiDNI는 공식 신분 확인 앱이에요",
     "MiDNI es... A. un billete · B. una entrada · C. una aplicación oficial", size=15.5, gap=1)
f.ex("B2", "객관식", "B", "11월 24~28일에는 여론조사를 발표하지 않아요",
     "No se publican encuestas del... A. 16 al 19 · B. 24 al 28 · C. 13 al 15", size=15.5, gap=1)
f.ex("B1", "객관식", "C", "챔피언스리그 5라운드, 11월 24~25일",
     "La jornada 5 de la Champions es el... A. 20–21 · B. 29–30 · C. 24–25", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Lucía vive en Sevilla: el sábado 21 ve el derbi Sevilla–Betis en el Sánchez-Pizjuán. Diego vive en Madrid: el sábado ve el Real Madrid–Celta en el Bernabéu. Los dos escuchan flamenco el lunes 16 y leen los programas antes de votar el 29.", 16.5, lh=1.3, split=False)
f.ex("A2", "객관식", "A", "루시아는 토요일에 세비야에서 더비를 봐요",
     "¿Quién ve el derbi en Sevilla? A. Lucía · B. Diego · C. los dos", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "디에고는 토요일에 레알 마드리드 대 셀타 경기를 봐요",
     "El sábado, Diego... A. ve el Madrid–Celta · B. ve el derbi · C. duerme", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "두 사람 모두 강령을 읽고 투표해요",
     "Antes de votar, los dos... A. leen los programas · B. ven «Infamia» · C. viajan a Praga", size=15.5, gap=1)
f.ex("A2", "객관식", "B", "제목은 두 도시와 하나의 토요일을 요약해요",
     "El mejor título es... A. «Una tormenta» · B. «Dos ciudades, un sábado» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "문장 만들기", "El lunes suena el flamenco.", "시간이 앞에, 동사는 두 번째예요",
     "el lunes / suena / el flamenco → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("A2", "문장 만들기", "El sábado vemos el derbi.", "시간이 앞에 있어요",
     "el sábado / vemos / el derbi → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "La campaña dura quince días.", "주어 + 동사 + 시간",
     "la campaña / dura / quince días → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "¿A qué hora empieza el debate?", "의문사는 문장 맨 앞에 있어요",
     "¿ / a qué hora / empieza / el debate / ? → ___", instr="문장 만들기", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "번역", "월요일은 세계 플라멩코의 날이에요.", "원문과 대조해 보세요.",
     "El lunes es el Día del Flamenco. → ___", instr="번역", size=15.5, gap=1)
f.ex("A2", "번역", "토요일에 세비야 더비를 봐요.", "원문과 대조해 보세요.",
     "El sábado vemos el derbi Sevilla–Betis. → ___", instr="번역", size=15.5, gap=1)
f.ex("B1", "번역", "El voto por correo se pide hasta el jueves 19.", "pedir hasta el jueves 19",
     "우편 투표는 목요일 19일까지 신청해야 해요. → ___", instr="번역", size=15.5, gap=1)
f.ex("B2", "번역", "Cada promesa tiene que llevar datos.", "tener que = ~해야 해요",
     "모든 약속에는 근거 자료가 있어야 해요. → ___", instr="번역", size=15.5, gap=1)
f.head("F　LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "단어 짝짓기",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo=여론조사 c", "muestra=표본 d", "margen de error=오차 범위 b", "junta electoral=선거관리위원회 a"],
            instr="단어와 뜻 짝짓기")
f.head("G　DIÁLOGO EN EL COLEGIO", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "A", "vengo a votar = 투표하러 왔어요",
     "— Buenos días, vengo a ___. (A. votar · B. cantar)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "documento de identidad = 신분증",
     "— ¿Tiene su documento de ___? (A. identidad · B. puente)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "¿dónde está la urna? 투표함은 어디에 있어요?",
     "— ¿Dónde está la ___? (A. urna · B. guitarra)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "la papeleta va en el sobre = 투표 용지는 봉투에 넣어요",
     "— La papeleta va en el ___. (A. sobre · B. derbi)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "¿a qué hora cierra el colegio? 투표소는 몇 시에 닫아요?",
     "— ¿A qué hora ___ el colegio? (A. cierra · B. canta)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("쓰기 문제(정답이 하나가 아니에요). 모범 답안(97단어)은 아래에 있어요.")
f.ex("B1", "쓰기", "(열린 문제 — 모범 답안은 아래에 있어요)", "모범 답안은 이 페이지 H 부분을 보세요(97단어)",
     "«¿Qué harías tú en la primera semana de campaña?» Escribe 80–100 palabras: tu lunes 16, tu viernes 20 y tu voto del 29.", instr="쓰기", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y el lunes 16 escucho flamenco en la calle: cante, toque y baile, la música de la semana. "
          "El viernes 13 empezó la campaña, y el domingo 29 voto por primera vez: pido el voto por correo hasta el jueves 19. "
          "El viernes 20 vuelve la Liga, y el sábado veo el derbi Sevilla–Betis con mi familia. "
          "El domingo 22 escucho a la banda de Santa Cecilia. "
          "Mis amigos de Barcelona no tienen duende en su barrio: el lunes trabajan. Yo, en cambio, leo los programas con calma y preparo mi voto. "
          "¡Qué semana!")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()
print("P8-ex flow ended y=", f.y)

# ---- P8 image: swan pen, in the free space of the last exercise column ----
iy8 = f.y + 24
ih8 = 240
image(p, "swan_pen.jpg", COLX[3], iy8, CW, ih8)
caption(p, COLX[3], iy8 + ih8, CW,
        "La pluma del escritor: esta página es para escribir. El texto modelo de arriba tiene 97 palabras: tu texto, entre 80 y 100.",
        "Pluma de cisne — dominio público (Wikimedia Commons)")
print("P8 image bottom approx", iy8 + ih8 + 90)

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1337, "RESPUESTAS　정답 — 면별로 나누어 실었어요, 번호로 찾으세요", 25, "sans", True, OLIVE)
p.text(RIGHT, 1337, "문제마다 한국어 해설 한 줄　✓ 표시는 모범 답안 문제예요", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1363, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "쓰기":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("MODELO words:", len(MODELO.split()))
