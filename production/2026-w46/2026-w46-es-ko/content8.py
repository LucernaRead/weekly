# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P8: 38 exercises + registry-generated answers. Dash style, as W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS · 연습과 답", "La Lucerna", "8면 · La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "B", "visita a Chequia = 체코 원정",
     "El jueves, la Roja ___ a Chequia en Praga. (A. recibe · B. visita)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "recibir a Inglaterra = 잉글랜드를 홈에서 맞이해요",
     "El domingo, España ___ a Inglaterra en Madrid. (A. visita · B. recibe)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "la lista = 소집 명단",
     "De la Fuente dio ___ el viernes 6. (A. la lista · B. la huelga)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "la huelga dura 24 horas = 파업은 24시간 계속돼요",
     "La huelga del miércoles ___ 24 horas. (A. empieza · B. dura)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "empieza la campaña = 선거 운동이 시작해요",
     "El viernes 13 ___ la campaña electoral. (A. empieza · B. termina)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "B", "el sobre = 봉투",
     "El voto por correo llega en un ___. (A. puente · B. sobre)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "일요일에는 스페인–잉글랜드 경기가 있어요",
     "El domingo se juega el ___ en el Metropolitano. (A. España–Inglaterra · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "veranillo = 늦가을 따뜻한 날",
     "En noviembre llega el ___ de San Martín. (A. veranillo · B. puente)", size=15.5, gap=1)
f.head("B · PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "객관식", "B", "총파업은 11월 11일 수요일이에요",
     "La huelga general es el... A. lunes 9 · B. miércoles 11 · C. viernes 13", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "성 마르틴 축일 11월 11일",
     "San Martín es el... A. 11 de noviembre · B. 12 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "객관식", "C", "스페인–잉글랜드와 파업 모두 이번 주에 있어요",
     "Esta semana hay... A. solo fútbol · B. solo huelga · C. la huelga y el España–Inglaterra", size=15.5, gap=1)
f.ex("B1", "객관식", "B", "magosto에서는 군밤을 먹어요",
     "¿Qué se come en el magosto? A. flan · B. castañas asadas · C. chocolate", size=15.5, gap=1)
f.ex("B1", "객관식", "A", "파업 구호: 월급, 주택, 물가",
     "El lema de la huelga es... A. «Salarios, vivienda y precios» · B. «Fútbol y fiesta» · C. «Cine y series»", size=15.5, gap=1)
f.ex("B1", "객관식", "C", "총선거는 11월 29일이에요",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "객관식", "B", "CIS 주택 지표: 주택이 걱정되는 사람 86.9%",
     "Según el CIS de vivienda, está preocupado el... A. 13,5 % · B. 86,9 % · C. 79 %", size=15.5, gap=1)
f.ex("B1", "객관식", "A", "선거 운동은 11월 13일에 시작해요",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C · LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el miércoles 11 sigue la huelga en las noticias y el domingo ve el España–Inglaterra en el Metropolitano. Ana vive en Barcelona: el miércoles 11 trabaja, y el domingo ve el partido por televisión. Los dos leen los programas antes de votar el 29.", 16.5, lh=1.3, split=False)
f.ex("A2", "객관식", "B", "파블로는 일요일에 메트로폴리타노에 가요",
     "¿Quién ve el partido en el Metropolitano? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "아나는 수요일에 일해요",
     "El miércoles 11, Ana... A. trabaja · B. va a la huelga · C. duerme", size=15.5, gap=1)
f.ex("A2", "객관식", "A", "두 사람 모두 강령을 읽고 투표해요",
     "Antes de votar, los dos... A. leen los programas · B. ven «Infamia» · C. viajan a Praga", size=15.5, gap=1)
f.ex("A2", "객관식", "B", "제목은 두 곳의 대비를 요약해요",
     "El mejor título es... A. «Una tormenta» · B. «Dos miércoles» · C. «El Clásico»", size=15.5, gap=1)
f.head("D · CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "문장 만들기", "El miércoles hay huelga general.", "주어 + 동사 + 장소",
     "el miércoles / hay / huelga general → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("A2", "문장 만들기", "El domingo vemos el España–Inglaterra.", "시간이 앞에 있어요",
     "el domingo / vemos / el España–Inglaterra → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "La campaña empieza a las cero horas.", "a las cero horas = 0시",
     "la campaña / empieza / a las cero horas → ___", instr="문장 만들기", size=15.5, gap=1)
f.ex("B1", "문장 만들기", "¿A qué hora empieza el partido?", "의문사는 문장 맨 앞에 있어요",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="문장 만들기", size=15.5, gap=1)
f.head("E · TRADUCE", 22, OLIVE, 5)
f.ex("A2", "번역", "수요일 스페인 전역에서 총파업이 있어요.", "원문과 대조해 보세요.",
     "El miércoles hay huelga general en toda España. → ___", instr="번역", size=15.5, gap=1)
f.ex("A2", "번역", "일요일에 우리는 스페인–잉글랜드를 봐요.", "원문과 대조해 보세요.",
     "El domingo vemos el España–Inglaterra. → ___", instr="번역", size=15.5, gap=1)
f.ex("B1", "번역", "El voto por correo llega a casa.", "llegar a casa = 집으로 와요",
     "우편 투표가 집으로 와요. → ___", instr="번역", size=15.5, gap=1)
f.ex("B2", "번역", "Cada gráfico tiene que llevar su fuente.", "tener que = 반드시 ~해야 해요",
     "모든 도표는 출처를 밝혀야 해요. → ___", instr="번역", size=15.5, gap=1)
f.head("F · LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "단어 짝짓기",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo=여론조사 c", "muestra=표본 d", "margen de error=오차 범위 b", "junta electoral=선거관리위원회 a"],
            instr="단어와 뜻 짝짓기")
f.head("G · DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "A", "alquiler = 임대료",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "tres habitaciones = 방 세 개",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "¿cuánto cuesta? = 얼마예요?",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "firmar = 서명해요 (계약서에)",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "빈칸 채우기", "A", "mudanza = 이사",
     "— La ___ es el miércoles 11, día de huelga. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H · ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("쓰기 문제 (정답이 하나가 아니에요). 모범 답안 (84단어)은 아래에 있어요.")
f.ex("B1", "쓰기", "(열린 문제 — 모범 답안은 아래에 있어요)", "모범 답안은 이 면 H 구역에 있어요 (84단어)",
     "«¿Qué harías tú por la vivienda?» Escribe 80–100 palabras: tu plan del miércoles 11, tu domingo 15 y tu voto del 29.", instr="쓰기", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y el miércoles 11 sigo la huelga en las noticias: salarios, vivienda y precios, los tres temas de la semana. "
          "El viernes 13 empieza la campaña, y el domingo 15 veo el España–Inglaterra con mi familia. "
          "El jueves 12 veo el Chequia–España en Praga por televisión, a las 20:45. "
          "Mis amigos de Barcelona no tienen huelga en su empresa: el miércoles trabajan. Yo, en cambio, leo los programas con calma y preparo mi voto por correo. "
          "El 29 votamos. ¡Qué semana!")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPUESTAS · 정답 — 면별로 나누어 실었어요, 번호로 찾으세요", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "문제마다 한국어 해설 한 줄 · ✓ 표시는 모범 답안 문제예요", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
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
