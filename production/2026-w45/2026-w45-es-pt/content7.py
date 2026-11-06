# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-es-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LENGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LENGUA · LÍNGUA", "La Lucerna", "FOCO NA LÍNGUA · Tres niveles, tres herramientas · TRÊS NÍVEIS, TRÊS FERRAMENTAS")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · LAS FECHAS", 24)
a.para("Para decir la fecha: «el lunes 2 de noviembre». Primero el día, luego el número y luego el mes. Los días y los meses van en minúscula: lunes, noviembre.", 21.5)
a.para("Y ojo con el 1: el primer día del mes es «el uno», no «el primero»: el 1 de noviembre, el Día de Todos los Santos.", 21.5)
a.bridge("O formato da data: el lunes 2 de noviembre; dias e meses em minúsculas; o dia 1 é el uno.")
a.ex("A2", "Completar frases", "2", "el lunes 2 de noviembre (dia de ponte)",
     "El puente es el lunes ___ de noviembre.", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Completar frases", "uno", "el 1 = el uno",
     "Todos los Santos es el ___ de noviembre.", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Completar frases", "domingo", "o dia 29 é domingo",
     "Las elecciones son el ___ 29 de noviembre.", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Escolha múltipla", "B", "o mês em minúsculas: noviembre",
     "¿Cómo se escribe el mes? A. Noviembre · B. noviembre · C. NOVIEMBRE", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · COMPARATIVOS", 24)
b.para("Para comparar: más / menos + adjetivo + que; tan + adjetivo + como. Dos irregulares para recordar: bueno → mejor, malo → peor. Y nunca «más mejor»: mejor ya es comparativo.", 21.5)
b.para("La vivienda de esta semana sirve para practicar: más cara que, tan alta como, mejor que, peor que.", 21.5)
b.bridge("O comparativo: más…que, tan…como; bueno→mejor, malo→peor; nunca se diz más mejor.")
b.ex("B1", "Completar frases", "más cara", "más + cara (a habitação está mais cara)",
     "La vivienda es ___ que hace un año. (cara)", instr="Complete", size=20.5, gap=10)
b.ex("B1", "Completar frases", "tan alta", "tan + alta + como (igualmente alta)",
     "La preocupación es ___ como en septiembre. (alta)", instr="Complete", size=20.5, gap=10)
b.ex("B1", "Completar frases", "mejor", "o comparativo de bueno é melhor (sem más)",
     "Un programa claro es ___ (bueno) que un titular.", instr="Complete", size=20.5, gap=10)
b.ex("B1", "Escolha múltipla", "B", "más mejor está errado",
     "¿Qué forma es correcta? A. más mejor · B. mejor · C. muy mejor", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · EL SUBJUNTIVO", 24)
c.para("Las promesas usan el subjuntivo: «es necesario que», «para que», «ojalá» van con subjuntivo — tenga, sea, baje. Pero «creo que» afirma y va con indicativo: creo que es.", 21.5)
c.para("Es la gramática de la página 6: opinar sobre encuestas y programas sin afirmar más de lo que sabemos.", 21.5)
c.bridge("es necesario que, para que e ojalá pedem o subjuntivo; creo que pede o indicativo.")
c.ex("B2", "Completar frases", "baje", "es necesario que + subjuntivo (baje)",
     "Es necesario que el precio ___ (bajar).", instr="Complete", size=20.5, gap=10)
c.ex("B2", "Completar frases", "sea", "para que + subjuntivo (sea)",
     "Publicamos la fuente para que todo ___ (ser) claro.", instr="Complete", size=20.5, gap=10)
c.ex("B2", "Completar frases", "es", "creo que + indicativo (es)",
     "Creo que la vivienda ___ (ser) el tema del 29-N.", instr="Complete", size=20.5, gap=10)
c.ex("B2", "Escolha múltipla", "B", "ojalá + subjuntivo: baje",
     "«Ojalá que el precio...» A. baja · B. baje · C. bajar", size=20.5, gap=10)
c.end_report()

# ---- col 3: errores típicos + palabra + lectores ----
bx = COLX[3]
errs = [
    ("«El lunes 2 son fiesta.»", "→ «El lunes 2 es festivo.» El lunes es singular: es, no son.", "lunes é singular: usa-se es."),
    ("«La vivienda es más mejor.»", "→ «La vivienda es mejor.» Mejor ya es comparativo: sin más.", "mejor já é comparativo: sem mais."),
    ("«La gente votan el 29.»", "→ «La gente vota el 29.» Gente es singular, como un solo grupo.", "gente é singular, como um só grupo."),
    ("«Creo que la vivienda sea el tema.»", "→ «Creo que la vivienda es el tema.» Creo que afirma: indicativo.", "creo que afirma: modo indicativo (es)."),
]
# 盒高 = 绘制循环精确模拟（W43 回补修法：逐项模拟，不用平均行高）
_sim = 216 + 44
for _w, _r, _n in errs:
    _sim += 17 + len(wrap(_w, "serif", True, 21.5, CW - 44)) * 21.5 * 1.36 \
          + 17 + len(wrap(_r, "serif", False, 20.5, CW - 44)) * 20.5 * 1.36 \
          + 16 + len(wrap(_n, "sans", False, 19.5, CW - 44)) * 19.5 * 1.36 + 4
eh = _sim - 200 + 12
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS · Erros comuns", 20, "sans", True, OLIVE)
yy3 += 44
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 17, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 17, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 16, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 4
wy = 200 + eh + 16
wt = "« la precampaña » es el tiempo antes de la campaña oficial: las semanas en que los partidos cierran sus listas y escriben sus programas. Esta edición entera es precampaña."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("precampaña = a pré-campanha: as semanas antes da campanha. A campanha começa sexta, dia 13.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PALABRA · A palavra da semana", 22, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "precampaña = a pré-campanha: as semanas antes da campanha. A campanha começa sexta, dia 13.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 16
lt = "«¡Hola! Soy Ana, estudio español en Shanghái. El lunes 2 no tengo puente, pero el domingo veo el Atlético–Barça con mis amigos — ¡y antes, la NFL! ¡Gracias por el periódico!» — Ana （ejemplo, escrito por la redacción）"
# FIX1 Problem 2: on-page disclosure (parent decision) — no real letters / best P8
# texts had arrived by press time, so the labeled editor's example is printed and
# the W43 promise carries to VOL.3. Spanish + matching Chinese note, inside this box.
ld = "Nota de la redacción: al cierre no había cartas reales ni los mejores textos de la página 8; publicamos este ejemplo y la promesa pasa al VOL.3."
ldcn = "Nota da redação: ao fecho, sem cartas reais nem textos da pág. 8; sai este exemplo. Promessa: VOL.3."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20, CW - 44)) * 29 + 10 + len(wrap(ldcn, "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DE LOS LECTORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, ld, 20, "serif", False, GREY, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, ldcn, 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases de la semana (verbatim from this issue) ----
# FIX1: y is computed from the readers' box end (disclosure grew it) so the
# frases block always clears col 3 with the same 21px gap as before.
fy = ly + lh + 35
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASES DE LA SEMANA · Frases da semana (retiradas dos textos desta edição)", 27, "sans", True, OLIVE)
quotes = [
    ("«Las listas ya están presentadas: ahora los partidos escriben sus programas.»", "As listas já foram apresentadas: agora os partidos escrevem os seus programas.", "Página 1"),
    ("«El lunes 2 de noviembre es festivo en nueve comunidades — y día de trabajo en las demás.»", "Na segunda, 2 de novembro, nove comunidades têm feriado — e as outras trabalham.", "Página 2"),
    ("«Tres fiestas, una misma noche de otoño.»", "Três festas, uma mesma noite de outono.", "Página 3"),
    ("«El Madrid ganó 2–1 en el Camp Nou: fue la primera derrota liguera del Barça.»", "O Madrid ganhou 2–1 no Camp Nou: foi a primeira derrota do Barça na Liga.", "Página 4"),
    ("«El Bernabéu cambia el césped por el emparrillado: el fútbol americano llega a Madrid.»", "O Bernabéu troca a relva pelo emparrillado: o futebol americano chega a Madrid.", "Página 5"),
    ("«La vivienda es el principal problema para el 55,7 % de los españoles.»", "A habitação é o principal problema para 55,7% dos espanhóis.", "Página 6"),
    ("«Una encuesta es una foto con margen de error, tomada en un día concreto.»", "Uma sondagem é uma foto com margem de erro, tirada num dia concreto.", "Página 6"),
    ("«El domingo 8, Madrid tiene dos citas: la NFL a las 15:30 y el Atlético–Barça a las 21:00.»", "No domingo 8, Madrid tem dois compromissos: a NFL às 15:30 e o Atlético–Barça às 21:00.", "Página 1"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 128
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
# FIX1: computed from the frases block end (last row top + ~105 block + 30 gap)
# so the preview box clears the quotes and still clears the footer line at 2580.
py = fy + 66 + 3 * 128 + 105 + 30
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "LA PRÓXIMA SEMANA · Na próxima semana (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "El viernes 13: empieza la campaña electoral. El domingo 29: España vota. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lengua.svg")
print("P7 saved, exercises so far:", len(REG))
