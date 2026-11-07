# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P7 language focus. Fresh text; golden sentences verbatim from P1–P6.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LENGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LENGUA · 언어", "La Lucerna", "언어 특집 · Tres niveles, tres herramientas · 세 단계, 세 가지 도구")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · LAS FECHAS", 24)
a.para("Para decir la fecha: «el miércoles 11 de noviembre». Primero el día, luego el número y luego el mes. Los días y los meses van en minúscula: miércoles, noviembre.", 21.5)
a.para("Y ojo con el 1: el primer día del mes es «el uno», no «el primero»: el 1 de noviembre, el Día de Todos los Santos.", 21.5)
a.bridge("요일과 월은 소문자로 써요. 날짜는 el miércoles 11 de noviembre, 1일은 el uno예요.")
a.ex("A2", "문장 완성", "11", "el miércoles 11 de noviembre: 총파업",
     "La huelga general es el miércoles ___ de noviembre.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "uno", "el 1 = el uno",
     "Todos los Santos es el ___ de noviembre.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "domingo", "15일은 일요일이에요",
     "El España–Inglaterra es el ___ 15 de noviembre.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "객관식", "B", "월은 소문자: noviembre",
     "¿Cómo se escribe el mes? A. Noviembre · B. noviembre · C. NOVIEMBRE", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · COMPARATIVOS", 24)
b.para("Para comparar: más / menos + adjetivo + que; tan + adjetivo + como. Dos irregulares para recordar: bueno → mejor, malo → peor. Y nunca «más mejor»: mejor ya es comparativo.", 21.5)
b.para("La vivienda de esta semana sirve para practicar: más cara que, tan alta como, mejor que, peor que.", 21.5)
b.bridge("비교급은 más…que, tan…como예요. bueno→mejor, malo→peor예요. más mejor라고 절대 말하지 마세요.")
b.ex("B1", "문장 완성", "más cara", "más + cara (더 비싼 집)",
     "La vivienda es ___ que hace un año. (cara)", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "tan alta", "tan + alta + como (똑같이 높아요)",
     "La preocupación es ___ como en octubre. (alta)", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "mejor", "bueno의 비교급은 mejor예요 (más는 없어요)",
     "Un programa claro es ___ (bueno) que un titular.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "객관식", "B", "más mejor는 틀린 말이에요",
     "¿Qué forma es correcta? A. más mejor · B. mejor · C. muy mejor", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · EL SUBJUNTIVO", 24)
c.para("Las promesas usan el subjuntivo: «es necesario que», «para que», «ojalá» van con subjuntivo — tenga, sea, baje. Pero «creo que» afirma y va con indicativo: creo que es.", 21.5)
c.para("Es la gramática de la página 6: opinar sobre encuestas y programas sin afirmar más de lo que sabemos.", 21.5)
c.bridge("es necesario que, para que, ojalá — 뒤에는 접속법. creo que — 뒤에는 직설법.")
c.ex("B2", "문장 완성", "baje", "es necesario que + 접속법: baje",
     "Es necesario que el precio ___ (bajar).", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "sea", "para que + 접속법: sea",
     "Publicamos la fuente para que todo ___ (ser) claro.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "es", "creo que + 직설법: es",
     "Creo que la vivienda ___ (ser) el tema del 29-N.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "객관식", "B", "ojalá + 접속법: baje",
     "«Ojalá que el precio...» A. baja · B. baje · C. bajar", size=20.5, gap=10)
c.end_report()

# ---- col 3: errores típicos + palabra + lectores ----
bx = COLX[3]
errs = [
    ("«El domingo 15 son el partido.»", "→ «El domingo 15 es el partido.» El domingo es singular: es, no son.", "domingo는 단수예요. 동사는 es예요."),
    ("«La vivienda es más mejor.»", "→ «La vivienda es mejor.» Mejor ya es comparativo: sin más.", "mejor 자체가 비교급이에요. más는 없어요."),
    ("«La gente votan el 29.»", "→ «La gente vota el 29.» Gente es singular, como un solo grupo.", "gente는 단수 집합 명사예요. 동사도 단수예요."),
    ("«Creo que la vivienda sea el tema.»", "→ «Creo que la vivienda es el tema.» Creo que afirma: indicativo.", "creo que는 확신해요. 직설법 es를 써요."),
]
_sim = 216 + 44
for _w, _r, _n in errs:
    _sim += 17 + len(wrap(_w, "serif", True, 21.5, CW - 44)) * 21.5 * 1.36 \
          + 17 + len(wrap(_r, "serif", False, 20.5, CW - 44)) * 20.5 * 1.36 \
          + 16 + len(wrap(_n, "sans", False, 19.5, CW - 44)) * 19.5 * 1.36 + 4
eh = _sim - 200 + 12
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS · 자주 하는 실수", 20, "sans", True, OLIVE)
yy3 += 44
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 17, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 17, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 16, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 4
wy = 200 + eh + 16
wt = "« la huelga general » es el paro de todos a la vez, un día entero: el miércoles 11, por los salarios, la vivienda y los precios."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("huelga general = 총파업: 모두가 같은 날 일을 멈춰요.", "sans", False, 20, CW - 44)) * 29 + 42
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PALABRA · 이번 주 단어", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "huelga general = 총파업: 모두가 같은 날 일을 멈춰요.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 16
lt = "«¡Hola! Soy Ana, estudio español en Shanghái. El miércoles 11 sigo la huelga en las noticias y el domingo veo el España–Inglaterra con mis amigos. ¡Gracias por el periódico!» — Ana (ejemplo, escrito por la redacción)"
ld = "Nota de la redacción: al cierre no había cartas reales ni los mejores textos de la página 8; publicamos este ejemplo y la promesa pasa al VOL.4."
ldcn = "편집부 알림: 실제 편지와 8면 최고 글이 없어서 예시 편지를 실어요. 약속은 다음 호로 이어져요."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20, CW - 44)) * 29 + 10 + len(wrap(ldcn, "sans", False, 20, CW - 44)) * 29 + 42
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DE LOS LECTORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, ld, 20, "serif", False, GREY, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, ldcn, 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases de la semana (verbatim from this issue) ----
fy = ly + lh + 35
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASES DE LA SEMANA · 이번 주 문장 (이번 호 글에서 그대로 뽑았어요)", 27, "sans", True, OLIVE)
quotes = [
    ("«El miércoles 11 hay huelga general y el viernes 13, a las 00:00, empieza la campaña electoral.»", "수요일 11일에는 총파업이 있고, 금요일 13일 0시에는 선거 운동이 시작해요.", "Página 1"),
    ("«El miércoles 11 de noviembre hay huelga general en toda España: un paro de 24 horas, convocado por los sindicatos.»", "11월 11일 수요일 스페인 전역에서 총파업이 있어요. 노조가 부른 24시간 파업이에요.", "Página 2"),
    ("«Cuenta la leyenda que Martín, soldado romano, partió su capa en dos con la espada para cubrir a un mendigo que moría de frío.»", "전설에 따르면 로마 군인 마르틴은 검으로 망토를 둘로 잘라 추위에 죽어 가던 거지를 덮어 주었어요.", "Página 3"),
    ("«España, vigente campeona del mundo y de Europa, juega en el grupo A3 con Croacia, Inglaterra y la República Checa.»", "현 세계 챔피언이자 유럽 챔피언인 스페인은 크로아티아, 잉글랜드, 체코와 함께 A3조에 있어요.", "Página 4"),
    ("«No hace falta ir al colegio electoral para votar: el voto por correo llega a casa.»", "투표하러 투표소에 갈 필요가 없어요. 우편 투표가 집으로 와요.", "Página 5"),
    ("«La vivienda preocupa al 86,9 % de los españoles.»", "주택 때문에 스페인 사람의 86.9%가 걱정해요.", "Página 6"),
    ("«Una encuesta es una foto con margen de error, tomada en un día concreto.»", "여론조사는 오차가 있는 사진이에요, 어느 하루에 찍은 사진이에요.", "Página 6"),
    ("«El domingo 15, la selección cierra la fase de grupos de la Liga de Naciones contra Inglaterra, en el Metropolitano, a las 20:45.»", "11월 15일 일요일, 대표팀은 메트로폴리타노에서 20:45에 잉글랜드와 조별 리그 마지막 경기를 해요.", "Página 1"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 128
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = fy + 66 + 3 * 128 + 105 + 30
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "LA PRÓXIMA SEMANA · 다음 호 예고 (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "La primera semana de campaña, la jornada 13 de Liga y la vuelta de la Champions. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lengua.svg")
print("P7 saved, exercises so far:", len(REG))
