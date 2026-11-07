# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-es-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band('EJERCICIOS Y RESPUESTAS · 연습과 답', "La Lucerna", '제 8면 · La gran prueba de la semana + todas las respuestas')

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", '빈칸 채우기', "B", 'abrir el marcador = 첫 골을 넣다',
     "Doué ___ el marcador en París. (A. cerró · B. abrió)", size=15.5, gap=1)
f.ex("B1", '빈칸 채우기', "B", 'poner el 1–1 = 동점 골을 넣다',
     "Espart ___ el 1–1 para el Barça. (A. perdió · B. puso)", size=15.5, gap=1)
f.ex("B1", '빈칸 채우기', "A", 'de cabeza = 헤딩',
     "Lucas Hernández marcó el 2–1 de ___. (A. cabeza · B. penalti)", size=15.5, gap=1)
f.ex("B1", '빈칸 채우기', "B", 'volver a + 동사 원형 = 다시 ~해요',
     "Yamal ___ a empatar: 2–2. (A. salió · B. volvió)", size=15.5, gap=1)
f.ex("B1", '빈칸 채우기', "B", 'cerrar el partido = 승리를 확정 짓다',
     "Vitinha y Fabián Ruiz ___ el 4–2 al final. (A. abrieron · B. cerraron)", size=15.5, gap=1)
f.ex("B1", '빈칸 채우기', "B", 'derrota = 패배',
     "Fue la primera ___ del Barça este año. (A. victoria · B. derrota)", size=15.5, gap=1)
f.ex("B1", '빈칸 채우기', "A", '일요일에 엘 클라시코가 열려요',
     "El domingo se juega el ___ en el Camp Nou. (A. Clásico · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", '빈칸 채우기', "A", 'camiseta = 유니폼',
     "El Barça lleva una ___ de GOLF WANG. (A. camiseta · B. bufanda)", size=15.5, gap=1)
f.head("B · PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", '객관식', "B", '일요일 새벽 03:00가 02:00이 돼요',
     "El cambio: a las... A. 02→03 · B. 03→02 · C. 00→01", size=15.5, gap=1)
f.ex("A2", '객관식', "A", '카나리아는 한 시간 적어요',
     "¿Dónde hay una hora menos? A. Canarias · B. Madrid · C. Barcelona", size=15.5, gap=1)
f.ex("A2", '객관식', "C", '엘 클라시코와 F1이 모두 21:00예요',
     "El domingo, 21:00: hay... A. solo fútbol · B. solo coches · C. los dos", size=15.5, gap=1)
f.ex("B1", '객관식', "B", 'Castanyada에는 panellets를 먹어요',
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", '객관식', "A", 'Halloween은 10월 31일 토요일이에요',
     "Halloween es... A. sáb. 31.10 · B. dom. 1.11 · C. lun. 2.11", size=15.5, gap=1)
f.ex("B1", '객관식', "C", '총선은 11월 29일이에요',
     "Las elecciones generales son el... A. 29.10 · B. 1.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", '객관식', "B", '두 여론조사는 섞으면 안 돼요',
     "¿Por qué no mezclamos las series? A. son secretas · B. métodos distintos · C. son viejas", size=15.5, gap=1)
f.ex("B1", '객관식', "A", 'DANA Adam은 이번 시즌 이름 붙은 첫 폭풍이에요',
     "La DANA Adam es... A. la primera tormenta con nombre · B. una fiesta gallega · C. un equipo", size=15.5, gap=1)
f.head("C · LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Lucía vive en Sevilla: el lunes 2 es festivo en Andalucía y hace puente. Marta vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El sábado por la noche, Marta celebra la Castanyada con sus amigos: castañas y panellets.", 16.5, lh=1.3, split=False)
f.ex("A2", '객관식', "B", '안달루시아는 쉬는 지역 명단에 있어요',
     "¿Quién hace puente? A. Marta · B. Lucía · C. las dos", size=15.5, gap=1)
f.ex("A2", '객관식', "A", '카탈루냐는 월요일이 근무일이에요',
     "El lunes 2, Marta... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", '객관식', "C", 'Castanyada에는 밤과 panellets를 먹어요',
     "¿Qué comen Marta y sus amigos? A. flores · B. dulces de Halloween · C. castañas y panellets", size=15.5, gap=1)
f.ex("A2", '객관식', "B", '제목이 두 곳의 대조를 담아요',
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D · CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", '문장 만들기', "El domingo dormimos una hora más.", '시간이 앞에 와요',
     "el domingo / dormimos / una hora más → ___", instr='문장 만들기', size=15.5, gap=1)
f.ex("A2", '문장 만들기', "El lunes es festivo en Madrid.", '주어 + 동사 + 장소',
     "el lunes / es festivo / en Madrid → ___", instr='문장 만들기', size=15.5, gap=1)
f.ex("B1", '문장 만들기', "El Clásico empieza a las nueve.", 'a las nueve = 9시에',
     "el Clásico / empieza / a las nueve → ___", instr='문장 만들기', size=15.5, gap=1)
f.ex("B1", '문장 만들기', "¿A qué hora empieza el partido?", '의문사는 문장 맨 앞에 와요',
     "¿ / a qué hora / empieza / el partido / ? → ___", instr='문장 만들기', size=15.5, gap=1)
f.head("E · TRADUCE", 22, OLIVE, 5)
f.ex("A2", '번역', '일요일에 우리는 한 시간 더 자요.', '원문과 대조해 보세요',
     "El domingo dormimos una hora más. → ___", instr='번역', size=15.5, gap=1)
f.ex("A2", '번역', '월요일은 아홉 개 자치주에서 공휴일이에요.', '원문과 대조해 보세요',
     "El lunes es festivo en nueve comunidades. → ___", instr='번역', size=15.5, gap=1)
f.ex("B1", '번역', "El Clásico se juega el domingo a las nueve de la noche.", 'se juega = 열리다/경기가 치러지다',
     '엘 클라시코는 일요일 밤 9시에 열려요. → ___', instr='번역', size=15.5, gap=1)
f.ex("B2", '번역', "Cada gráfico tiene que llevar su fuente.", 'tener que = 해야 함',
     '모든 도표는 출처를 밝혀야 해요. → ___', instr='번역', size=15.5, gap=1)
f.head("F · LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", '단어 짝짓기',
            ["el sondeo", "el indeciso", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "quien aún no sabe a quién votar"],
            ["c", "d", "b", "a"],
            ['sondeo=여론조사 c', 'indeciso=아직 정하지 않은 사람 d', 'margen de error=오차 범위 b', 'junta electoral=선거관리위원회 a'],
            instr='단어와 뜻 짝짓기')
f.head("G · DIÁLOGO EN LA TIENDA", 22, OLIVE, 5)
f.ex("B1", '빈칸 채우기', "A", 'disfraz = 변장 의상',
     "— Busco un ___ para mi hija. (A. disfraz · B. paraguas)", size=15.5, gap=1)
f.ex("B1", '빈칸 채우기', "A", 'Monster High는 아이들에게 인기예요',
     "— Le encanta ___. (A. Monster High · B. el Samaín)", size=15.5, gap=1)
f.ex("B1", '빈칸 채우기', "A", '¿cuánto cuesta? 얼마예요?',
     "— ¿Cuánto ___? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", '빈칸 채우기', "A", 'pagar = 계산하다',
     "— ¿Cómo va a ___: con tarjeta o en efectivo? (A. pagar · B. votar)", size=15.5, gap=1)
f.ex("B1", '빈칸 채우기', "A", 'Halloween은 토요일이에요',
     "— Con tarjeta. La fiesta es el ___. (A. sábado · B. lunes)", size=15.5, gap=1)
f.head("H · ESCRIBE TÚ", 22, OLIVE, 5)
f.expl('쓰기 문제예요 (정답은 하나가 아니에요). 모범 답안 (82단어)은 아래에 있어요.')
f.ex("B1", '쓰기', '(열린 문제 — 모범 답안은 아래에 있어요)', '모범 답안은 이 면 H 구역에 있어요 (82단어)',
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del 31 y del 1, y tu lunes.", instr='쓰기', size=15.5, gap=1)
MODELO = ("Vivo en Valencia, y aquí el lunes 2 de noviembre no es festivo: trabajo como un lunes normal. "
          "Mis amigos de Madrid sí hacen puente, ¡qué suerte! El sábado 31 celebro Halloween con mi familia, "
          "y el domingo llevamos flores al cementerio, como cada año. Por la tarde leo un libro en el sofá "
          "y preparo la semana con calma. El lunes, mientras Madrid descansa, yo abro la tienda a las nueve. "
          "No es justo… pero en diciembre, seguro, llega mi puente.")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, 'RESPUESTAS · 정답 — 면별로 나누어 실었어요, 번호로 찾으세요', 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, '문제마다 한국어 해설 한 줄 · ✓ 표시는 모범 답안 문제예요', 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 제 {pg} 면 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == '쓰기':
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
