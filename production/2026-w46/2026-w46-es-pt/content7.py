# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P7 language focus. Fresh text; golden sentences verbatim from P1–P6.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LENGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LENGUA　LÍNGUA", "La Lucerna", "FOCO NA LÍNGUA　Tres niveles, tres herramientas　TRÊS NÍVEIS, TRÊS FERRAMENTAS")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　LAS FECHAS", 24)
a.para("Para decir la fecha: «el miércoles 11 de noviembre». Primero el día, luego el número y luego el mes. Los días y los meses van en minúscula: miércoles, noviembre.", 21.5)
a.para("Y ojo con el 1: el primer día del mes es «el uno», no «el primero»: el 1 de noviembre, el Día de Todos los Santos.", 21.5)
a.bridge("Datas: el miércoles 11 de noviembre; dias e meses em minúscula; o dia 1 se diz el uno.")
a.ex("A2", "Completar frases", "11", "el miércoles 11 de noviembre: greve geral",
     "La huelga general es el miércoles ___ de noviembre.", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Completar frases", "uno", "el 1 = el uno",
     "Todos los Santos es el ___ de noviembre.", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Completar frases", "domingo", "o dia 15 é domingo",
     "El España–Inglaterra es el ___ 15 de noviembre.", instr="Complete", size=20.5, gap=10)
a.ex("A2", "Escolha múltipla", "B", "meses em minúscula: noviembre",
     "¿Cómo se escribe el mes? A. Noviembre · B. noviembre · C. NOVIEMBRE", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　COMPARATIVOS", 24)
b.para("Para comparar: más / menos + adjetivo + que; tan + adjetivo + como. Dos irregulares para recordar: bueno → mejor, malo → peor. Y nunca «más mejor»: mejor ya es comparativo.", 21.5)
b.para("La vivienda de esta semana sirve para practicar: más cara que, tan alta como, mejor que, peor que.", 21.5)
b.bridge("Comparativos: más … que, tan … como; bueno → mejor, malo → peor; nunca diga más mejor.")
b.ex("B1", "Completar frases", "más cara", "más + cara (moradia mais cara)",
     "La vivienda es ___ que hace un año. (cara)", instr="Complete", size=20.5, gap=10)
b.ex("B1", "Completar frases", "tan alta", "tan + alta + como (tão alta quanto)",
     "La preocupación es ___ como en octubre. (alta)", instr="Complete", size=20.5, gap=10)
b.ex("B1", "Completar frases", "mejor", "o comparativo de bueno é mejor (sem más)",
     "Un programa claro es ___ (bueno) que un titular.", instr="Complete", size=20.5, gap=10)
b.ex("B1", "Escolha múltipla", "B", "más mejor está errado",
     "¿Qué forma es correcta? A. más mejor · B. mejor · C. muy mejor", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　EL SUBJUNTIVO", 24)
c.para("Las promesas usan el subjuntivo: «es necesario que», «para que», «ojalá» van con subjuntivo — tenga, sea, baje. Pero «creo que» afirma y va con indicativo: creo que es.", 21.5)
c.para("Es la gramática de la página 6: opinar sobre encuestas y programas sin afirmar más de lo que sabemos.", 21.5)
c.bridge("es necesario que, para que, ojalá com o subjuntivo; creo que com o indicativo.")
c.ex("B2", "Completar frases", "baje", "es necesario que + subjuntivo: baje",
     "Es necesario que el precio ___ (bajar).", instr="Complete", size=20.5, gap=10)
c.ex("B2", "Completar frases", "sea", "para que + subjuntivo: sea",
     "Publicamos la fuente para que todo ___ (ser) claro.", instr="Complete", size=20.5, gap=10)
c.ex("B2", "Completar frases", "es", "creo que + indicativo: es",
     "Creo que la vivienda ___ (ser) el tema del 29-N.", instr="Complete", size=20.5, gap=10)
c.ex("B2", "Escolha múltipla", "B", "ojalá + subjuntivo: baje",
     "«Ojalá que el precio...» A. baja · B. baje · C. bajar", size=20.5, gap=10)
c.end_report()

# ---- col 3: errores típicos + palabra + lectores ----
bx = COLX[3]
errs = [
    ("«El domingo 15 son el partido.»", "→ «El domingo 15 es el partido.» El domingo es singular: es, no son.", "domingo é singular: verbo es."),
    ("«La vivienda es más mejor.»", "→ «La vivienda es mejor.» Mejor ya es comparativo: sin más.", "mejor já é comparativo: sem más."),
    ("«La gente votan el 29.»", "→ «La gente vota el 29.» Gente es singular, como un solo grupo.", "gente é singular: verbo no singular."),
    ("«Creo que la vivienda sea el tema.»", "→ «Creo que la vivienda es el tema.» Creo que afirma: indicativo.", "creo que afirma: indicativo es."),
]
_sim = 216 + 44
for _w, _r, _n in errs:
    _sim += 17 + len(wrap(_w, "serif", True, 21.5, CW - 44)) * 21.5 * 1.36 \
          + 17 + len(wrap(_r, "serif", False, 20.5, CW - 44)) * 20.5 * 1.36 \
          + 16 + len(wrap(_n, "sans", False, 19.5, CW - 44)) * 19.5 * 1.36 + 4
eh = _sim - 200 + 12
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS　Erros comuns", 20, "sans", True, OLIVE)
yy3 += 44
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 17, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 17, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 16, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 4
wy = 200 + eh + 16
wt = "« la huelga general » es el paro de todos a la vez, un día entero: el miércoles 11, por los salarios, la vivienda y los precios."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("huelga general = greve geral: todos param no mesmo dia.", "sans", False, 20, CW - 44)) * 29 + 42
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PALABRA　A palavra da semana", 22, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "huelga general = greve geral: todos param no mesmo dia.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 16
lt = "«¡Hola! Soy Ana, estudio español en Shanghái. El miércoles 11 sigo la huelga en las noticias y el domingo veo el España–Inglaterra con mis amigos. ¡Gracias por el periódico!» — Ana (ejemplo, escrito por la redacción)"
ld = "Nota de la redacción: al cierre no había cartas reales ni los mejores textos de la página 8; publicamos este ejemplo y la promesa pasa al VOL.4."
ldcn = "Nota da redação: ao fecho, sem cartas reais nem textos da pág. 8; sai este exemplo. Promessa: VOL.4."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20, CW - 44)) * 29 + 10 + len(wrap(ldcn, "sans", False, 20, CW - 44)) * 29 + 42
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DE LOS LECTORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, ld, 20, "serif", False, GREY, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, ldcn, 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases de la semana (verbatim from this issue) ----
fy = ly + lh + 35
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "FRASES DE LA SEMANA　Frases da semana (ipsis litteris, desta edição)", 27, "sans", True, OLIVE)
quotes = [
    ("«El miércoles 11 hay huelga general y el viernes 13, a las 00:00, empieza la campaña electoral.»", "Na quarta, 11, há greve geral, e na sexta, 13, à 00:00, começa a campanha eleitoral.", "Página 1"),
    ("«El miércoles 11 de noviembre hay huelga general en toda España: un paro de 24 horas, convocado por los sindicatos.»", "Na quarta, 11 de novembro, há greve geral em toda a Espanha: uma paralisação de 24 horas, convocada pelos sindicatos.", "Página 2"),
    ("«Cuenta la leyenda que Martín, soldado romano, partió su capa en dos con la espada para cubrir a un mendigo que moría de frío.»", "Conta a lenda que Martinho, soldado romano, partiu a capa em duas com a espada para cobrir um mendigo que morria de frio.", "Página 3"),
    ("«España, vigente campeona del mundo y de Europa, juega en el grupo A3 con Croacia, Inglaterra y la República Checa.»", "A Espanha, atual campeã do mundo e da Europa, joga no grupo A3 com Croácia, Inglaterra e Chéquia.", "Página 4"),
    ("«No hace falta ir al colegio electoral para votar: el voto por correo llega a casa.»", "Não é preciso ir à seção eleitoral para votar: o voto pelo correio chega em casa.", "Página 5"),
    ("«La vivienda preocupa al 86,9 % de los españoles.»", "A habitação preocupa 86,9% dos espanhóis.", "Página 6"),
    ("«Una encuesta es una foto con margen de error, tomada en un día concreto.»", "Uma pesquisa é uma foto com margem de erro, tirada num dia certo.", "Página 6"),
    ("«El domingo 15, la selección cierra la fase de grupos de la Liga de Naciones contra Inglaterra, en el Metropolitano, a las 20:45.»", "No domingo, 15, a seleção fecha a fase de grupos da Liga das Nações contra a Inglaterra, no Metropolitano, às 20:45.", "Página 1"),
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
p.text(MX + 28, py + 44, "LA PRÓXIMA SEMANA　A próxima semana (VOL.4)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "La primera semana de campaña, la jornada 13 de Liga y la vuelta de la Champions. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lengua.svg")
print("P7 saved, exercises so far:", len(REG))
