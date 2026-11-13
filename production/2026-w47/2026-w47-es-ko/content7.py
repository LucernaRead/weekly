# -*- coding: utf-8 -*-
# W47 ES core (VOL.4) — P7 language focus. Fresh text; golden sentences verbatim from P1–P6.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LENGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LENGUA　언어", "La Lucerna", "언어 특집　Tres niveles, tres herramientas　세 단계, 세 가지 도구")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　LA HORA", 24)
a.para("Para decir la hora: «Es la una» en singular, «Son las dos» en plural. Para los minutos: «Son las 20:45» o «las nueve menos cuarto». Y el partido se juega «a las 21:00»: con la preposición a.", 21.5)
a.para("Y ojo con la fecha: «el lunes 16 de noviembre», con el mes en minúscula y el 1 como «el uno».", 21.5)
a.bridge("시간: es la una(단수), son las dos(복수). 경기는 a las 21:00에 시작해요.")
a.ex("A2", "문장 완성", "Es", "1시는 단수 Es를 써요",
     "___ la una en punto.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "Son", "여러 시에는 복수 Son을 써요",
     "___ las nueve de la noche.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "문장 완성", "las", "a las 21:00(a 전치사와 함께)",
     "El derbi es el sábado a ___ 18:30.", instr="빈칸 채우기", size=20.5, gap=10)
a.ex("A2", "객관식", "B", "1시는 Es la una예요",
     "¿Cómo se dice la 1:00? A. Son la una · B. Es la una · C. Es las una", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　COMPARATIVOS", 24)
b.para("Para comparar: más / menos + adjetivo + que; tan + adjetivo + como. Dos irregulares para recordar: bueno → mejor, malo → peor. Y nunca «más mejor»: mejor ya es comparativo.", 21.5)
b.para("El fútbol de esta semana sirve para practicar: más goles que, tan rápido como, mejor que, peor que.", 21.5)
b.bridge("비교급은 más…que, tan…como예요. bueno→mejor, malo→peor예요. más mejor라고 절대 말하지 마세요.")
b.ex("B1", "문장 완성", "más goles", "más + goles(더 많은 골)",
     "El Barça marca ___ que el año pasado. (goles)", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "tan rápido", "tan + rápido + como(똑같이 빨라요)",
     "El derbi es ___ como siempre. (rápido)", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "문장 완성", "mejor", "bueno의 비교급은 mejor예요 (más는 없어요)",
     "Un debate claro es ___ (bueno) que un titular.", instr="빈칸 채우기", size=20.5, gap=10)
b.ex("B1", "객관식", "B", "más mejor는 틀린 말이에요",
     "¿Qué forma es correcta? A. más mejor · B. mejor · C. muy mejor", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　EL SUBJUNTIVO", 24)
c.para("Los debates usan el subjuntivo: «es necesario que», «para que», «ojalá» van con subjuntivo — tenga, sea, baje. Pero «creo que» afirma y va con indicativo: creo que es.", 21.5)
c.para("Es la gramática de la página 6: opinar sobre debates y programas sin afirmar más de lo que sabemos.", 21.5)
c.bridge("es necesario que, para que, ojalá — 뒤에는 접속법. creo que — 뒤에는 직설법.")
c.ex("B2", "문장 완성", "baje", "es necesario que + 접속법: baje",
     "Es necesario que el precio ___ (bajar).", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "sea", "para que + 접속법: sea",
     "Publicamos la fuente para que todo ___ (ser) claro.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "문장 완성", "es", "creo que + 직설법: es",
     "Creo que el debate ___ (ser) útil.", instr="빈칸 채우기", size=20.5, gap=10)
c.ex("B2", "객관식", "B", "ojalá + 접속법: tenga",
     "«Ojalá que el debate...» A. tiene datos · B. tenga datos · C. tener datos", size=20.5, gap=10)
c.end_report()

# ---- col 3: manuscript image + errores + palabra + lectores ----
bx = COLX[3]
image(p, "book_hours.jpg", bx, 200, CW, 120)
cy3 = caption(p, bx, 320, CW, "Un libro de horas medieval: letras decoradas que abrían la oración.",
              "Manuscrito medieval — dominio público")
errs = [
    ("«Son la una en punto.»", "→ «Es la una.» Es singular.", "1시는 단수라서 동사는 es를 써요."),
    ("«El derbi es más mejor.»", "→ «Es mejor.» Sin más.", "mejor 자체가 비교급이에요. más는 없어요."),
    ("«La gente votan el 29.»", "→ «La gente vota.» Es singular.", "gente는 단수 집합 명사예요. 동사도 단수예요."),
    ("«Creo que el debate sea útil.»", "→ «Creo que el debate es útil.»", "creo que는 확신해요. 직설법 es를 써요."),
]
ey0 = cy3 + 24
_sim = 216 + 44
for _w, _r, _n in errs:
    _sim += 17 + len(wrap(_w, "serif", True, 21.5, CW - 44)) * 21.5 * 1.36 \
          + 17 + len(wrap(_r, "serif", False, 20.5, CW - 44)) * 20.5 * 1.36 \
          + 16 + len(wrap(_n, "sans", False, 19.5, CW - 44)) * 19.5 * 1.36 + 4
eh = _sim - 200 + 12
p.rect(bx, ey0, CW, eh, fill=BOX)
yy3 = ey0 + 16
p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS　자주 하는 실수", 23, "sans", True, OLIVE)
yy3 += 44
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 17, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 17, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 16, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 4
wy = ey0 + eh + 16
wt = "« el debate » es la discusión con turnos: cuatro portavoces el viernes 13; el lunes 16, un cara a cara propuesto."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("debate = 토론: 차례대로 하는 공개 토론. 이번 주는 토론 주간; 선거는 29일이에요.", "sans", False, 20, CW - 44)) * 29 + 42
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PALABRA　이번 주 단어", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "debate = 토론: 차례대로 하는 공개 토론. 이번 주는 토론 주간; 선거는 29일이에요.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 16
lt = "«¡Hola! Soy Marta, estudio español en Pekín. El lunes 16 escucho flamenco y el sábado veo el derbi. ¡Gracias por el periódico!» — Marta (ejemplo, escrito por la redacción)"
ld = "Nota de la redacción: sin cartas reales ni mejores textos al cierre, publicamos este ejemplo; la promesa pasa al VOL.5."
ldcn = "편집부 알림: 마감 때까지 실제 독자 편지와 우수 작문이 도착하지 않아서, 이번 호에는 편집부가 쓴 예시 편지를 실어요. 약속은 VOL.5로 미뤄요. 편지를 보내 주세요!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20, CW - 44)) * 29 + 10 + len(wrap(ldcn, "sans", False, 19, CW - 44)) * 27 + 42
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DE LOS LECTORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, ld, 20, "serif", False, GREY, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, ldcn, 19, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases de la semana (verbatim from this issue) ----
fy = ly + lh + 35
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "FRASES DE LA SEMANA　이번 주 문장 (이번 호 글에서 그대로 뽑았어요)", 27, "sans", True, OLIVE)
quotes = [
    ("«La campaña electoral empezó el viernes 13, a las 00:00, y dura quince días: hasta el viernes 27 de noviembre.»", "선거운동은 13일 자정에 시작해 15일간 이어지고 27일에 끝나요.", "Página 1"),
    ("«El jueves 19 es un día clave: termina el plazo para pedir el voto por correo.»", "목요일 19일은 중요한 날이에요. 우편 투표 신청 마감일이에요.", "Página 2"),
    ("«El lunes 16 de noviembre es el Día Internacional del Flamenco, y en España suena la guitarra en todos los rincones.»", "11월 16일 월요일은 세계 플라멩코의 날이고, 기타 소리가 스페인 전역에 울려요.", "Página 3"),
    ("«No es solo un baile: es cante, toque y baile, con palmas, taconeo y compás.»", "플라멩코는 춤만이 아니에요. 노래, 기타, 춤, 박수, 발구름과 리듬이에요.", "Página 3"),
    ("«La Liga se para y vuelve: después del parón de selecciones, la jornada 13 se juega del viernes 20 al lunes 23 de noviembre.»", "리그가 멈췄다가 다시 시작해요. 13라운드는 11월 20일 금요일부터 23일 월요일까지예요.", "Página 4"),
    ("«¿Votas por primera vez el 29 de noviembre? Tienes dos maneras de votar: en persona o por correo.»", "11월 29일에 처음 투표해요? 두 가지 방법: 직접 가거나 우편으로.", "Página 5"),
    ("«En campaña, no todo lo que se anuncia está cerrado.»", "선거운동 기간에는 발표된 모든 것이 확정된 것은 아니에요.", "Página 6"),
    ("«Una encuesta es una foto con margen de error, tomada en un día concreto.»", "여론조사는 오차가 있는 사진이에요, 어느 하루에 찍은 사진이에요.", "Página 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 128
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = fy + 66 + 3 * 128 + 105 + 30
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "LA PRÓXIMA SEMANA　다음 주 예고 (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "El domingo 29, España vota: los resultados, el Black Friday y la jornada 5 de la Champions. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lengua.svg")
print("P7 saved, exercises so far:", len(REG))
