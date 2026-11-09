# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS　연습과 답", "La Lucerna", "제 8면　La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "B", "ganó 2–1 = 2–1로 이겼어요",
     "El Madrid ___ 2–1 en el Camp Nou. (A. perdió · B. ganó)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "marcar dos goles = 두 골을 넣었어요",
     "Mbappé ___ dos goles en Barcelona. (A. paró · B. marcó)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "primera derrota liguera = 리그 첫 패배",
     "Fue la primera ___ del Barça en la Liga. (A. derrota · B. victoria)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "recortar = 격차를 줄이다",
     "El Madrid ___ la distancia a tres puntos. (A. aumentó · B. recortó)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "acoger = 개최하다 (베르나베우가 NFL을 개최해요)",
     "El Bernabéu ___ un partido de la NFL. (A. acoge · B. cierra)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "el emparrillado = 미식축구장",
     "El Bernabéu cambia el césped por el ___. (A. puente · B. emparrillado)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "일요일에 아틀레티코–바르사가 열려요",
     "El domingo se juega el ___ en el Metropolitano. (A. Atlético–Barça · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "himno = 국가",
     "Antes del partido suenan dos ___: el de España y el de EE. UU. (A. himnos · B. puentes)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "객관식", "B", "월요일에 쉬는 자치주는 9곳이에요",
     "El lunes 2 es fiesta en... A. todas · B. nueve comunidades · C. ninguna", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "모든 성인의 날은 11월 1일이에요",
     "Todos los Santos es el... A. 1 de noviembre · B. 2 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "객관식", "C", "아틀레티코–바르사와 NFL이 모두 일요일이에요",
     "El domingo 8 hay... A. solo fútbol · B. solo NFL · C. la NFL y el Atlético–Barça", size=15.5, gap=1)
f.ex("B1", "객관식", "B", "카스타냐에서는 파넬레츠를 먹어요",
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", "객관식", "A", "DANA 추모 행사는 10월 29일 목요일이에요",
     "Los actos de memoria de la DANA fueron el... A. jueves 29 de octubre · B. sábado 31 · C. lunes 2", size=15.5, gap=1)
f.ex("B1", "객관식", "C", "선거는 11월 29일이에요",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "객관식", "B", "10월 CIS 조사: 주택 55,7%",
     "Según el CIS de octubre, la vivienda es el principal problema para el... A. 20,9 % · B. 55,7 % · C. 17,1 %", size=15.5, gap=1)
f.ex("B1", "객관식", "A", "선거운동은 11월 13일에 시작해요",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el lunes 2 es festivo en su comunidad y hace puente. Ana vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El domingo por la tarde, Ana ve la NFL en televisión; por la noche, Pablo ve el Atlético–Barça.", 16.5, lh=1.3, split=False)
f.ex("A2", "객관식", "B", "마드리드는 휴일 명단에 있어요",
     "¿Quién hace puente? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "카탈루냐에서는 월요일이 근무일이에요",
     "El lunes 2, Ana... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "아나는 NFL만, 밤 아틀레티코–바르사는 파블로예요",
     "El domingo, Ana ve... A. solo la NFL · B. solo el Barça · C. la NFL y, por la noche, el Atlético–Barça", size=15.5, gap=1)
f.ex("A2", "객관식", "B", "제목이 두 지역 대비를 요약해요",
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "문장 만들기", "El lunes es festivo en Madrid.", "주어 + 동사 + 장소",
     "el lunes / es festivo / en Madrid → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("A2", "문장 만들기", "El domingo vemos la NFL en el Bernabéu.", "시간이 앞에 와요",
     "el domingo / vemos / la NFL / en el Bernabéu → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "El Atlético–Barça empieza a las nueve.", "a las nueve = 9시에",
     "el Atlético–Barça / empieza / a las nueve → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "¿A qué hora empieza el partido?", "의문사가 문장 맨 앞에 와요",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="문장 만들기", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "번역", "월요일은 아홉 개 자치주에서 공휴일이에요.", "원문과 대조해 보세요",
     "El lunes es festivo en nueve comunidades. → ___", instr="번역", size=15.5, gap=1)
f.ex("A2", "번역", "일요일에 우리는 NFL과 아틀레티코–바르사를 봐요.", "원문과 대조해 보세요",
     "El domingo vemos la NFL y el Atlético–Barça. → ___", instr="번역", size=15.5, gap=1)
f.ex("B1", "번역", "El Bernabéu acoge un partido de la NFL.", "acoger = 개최하다",
     "베르나베우는 NFL 경기를 개최해요. → ___", instr="번역", size=15.5, gap=1)
f.ex("B2", "번역", "Cada gráfico tiene que llevar su fuente.", "tener que = 반드시 해야 해요",
     "모든 도표는 출처를 밝혀야 해요. → ___", instr="번역", size=15.5, gap=1)
f.head("F　LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "단어 짝짓기",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo = 여론조사 (c)", "muestra = 표본 (d)", "margen de error = 오차 범위 (b)", "junta electoral = 선거관리위원회 (a)"],
            instr="단어와 뜻 짝짓기")
f.head("G　DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "A", "alquiler = 임대료",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "tres habitaciones = 방 세 개",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "¿cuánto cuesta? = 얼마예요?",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "firmar = 서명하다 (계약)",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "mudanza = 이사",
     "— La ___ es el lunes 2, que es fiesta. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("쓰기 문제예요 (정답은 하나가 아니에요). 모범 답안 (84단어)은 아래에 있어요.")
f.ex("B1", "쓰기", "(열린 문제 — 모범 답안은 아래에 있어요)", "모범 답안은 이 면 H 구역에 있어요 (84단어)",
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del puente y tu domingo 8.", instr="쓰기", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y aquí el lunes 2 de noviembre sí es festivo: hago puente con mi familia. "
          "El sábado 7 vemos el Valencia–Real Madrid en televisión, y el domingo 8 tenemos dos citas: por la tarde, la NFL en el Bernabéu, y por la noche, el Atlético–Barça. "
          "Mis amigos de Barcelona no tienen puente: el lunes trabajan. Yo, en cambio, descanso un día más y preparo la semana con calma. "
          "El viernes 13 empieza la campaña, y el 29 votamos todos. ¡Qué mes!")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPUESTAS　정답 — 면별로 나누어 실었어요, 번호로 찾으세요", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "문제마다 한국어 해설 한 줄　✓ 표시는 모범 답안 문제예요", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 제 {pg} 면 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
