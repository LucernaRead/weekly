# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-es-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LENGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LENGUA · LA LINGUA", "La Lucerna", "Focus lingua · Tres niveles, tres herramientas · Tre livelli, tre strumenti")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · LAS FECHAS", 24)
a.para("Para decir la fecha: «el lunes 2 de noviembre». Primero el día, luego el número y luego el mes. Los días y los meses van en minúscula: lunes, noviembre.", 21.5)
a.para("Y ojo con el 1: el primer día del mes es «el uno», no «el primero»: el 1 de noviembre, el Día de Todos los Santos.", 21.5)
a.bridge("Il formato della data: el lunes 2 de noviembre; giorni e mesi in minuscolo; il giorno 1 si dice el uno.")
a.ex("A2", "完成句子", "2", "el lunes 2 de noviembre, giorno di ponte",
     "El puente es el lunes ___ de noviembre.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "完成句子", "uno", "il giorno 1 = el uno",
     "Todos los Santos es el ___ de noviembre.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "完成句子", "domingo", "il 29 è domenica",
     "Las elecciones son el ___ 29 de noviembre.", instr="Completa", size=20.5, gap=10)
a.ex("A2", "单选", "B", "i mesi in minuscolo: noviembre",
     "¿Cómo se escribe el mes? A. Noviembre · B. noviembre · C. NOVIEMBRE", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · COMPARATIVOS", 24)
b.para("Para comparar: más / menos + adjetivo + que; tan + adjetivo + como. Dos irregulares para recordar: bueno → mejor, malo → peor. Y nunca «más mejor»: mejor ya es comparativo.", 21.5)
b.para("La vivienda de esta semana sirve para practicar: más cara que, tan alta como, mejor que, peor que.", 21.5)
b.bridge("Il comparativo: más…que, tan…como; bueno→mejor, malo→peor; mai dire más mejor.")
b.ex("B1", "完成句子", "más cara", "más + cara (la casa è più cara)",
     "La vivienda es ___ que hace un año. (cara)", instr="Completa", size=20.5, gap=10)
b.ex("B1", "完成句子", "tan alta", "tan + alta + como (alta come)",
     "La preocupación es ___ como en septiembre. (alta)", instr="Completa", size=20.5, gap=10)
b.ex("B1", "完成句子", "mejor", "il comparativo di bueno è mejor (senza más)",
     "Un programa claro es ___ (bueno) que un titular.", instr="Completa", size=20.5, gap=10)
b.ex("B1", "单选", "B", "más mejor è una forma sbagliata",
     "¿Qué forma es correcta? A. más mejor · B. mejor · C. muy mejor", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · EL SUBJUNTIVO", 24)
c.para("Las promesas usan el subjuntivo: «es necesario que», «para que», «ojalá» van con subjuntivo — tenga, sea, baje. Pero «creo que» afirma y va con indicativo: creo que es.", 21.5)
c.para("Es la gramática de la página 6: opinar sobre encuestas y programas sin afirmar más de lo que sabemos.", 21.5)
c.bridge("es necesario que, para que e ojalá + congiuntivo; creo que + indicativo.")
c.ex("B2", "完成句子", "baje", "es necesario que + congiuntivo: baje",
     "Es necesario que el precio ___ (bajar).", instr="Completa", size=20.5, gap=10)
c.ex("B2", "完成句子", "sea", "para que + congiuntivo: sea",
     "Publicamos la fuente para que todo ___ (ser) claro.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "完成句子", "es", "creo que + indicativo: es",
     "Creo que la vivienda ___ (ser) el tema del 29-N.", instr="Completa", size=20.5, gap=10)
c.ex("B2", "单选", "B", "ojalá + congiuntivo: baje",
     "«Ojalá que el precio...» A. baja · B. baje · C. bajar", size=20.5, gap=10)
c.end_report()

# ---- col 3: errores típicos + palabra + lectores ----
bx = COLX[3]
errs = [
    ("«El lunes 2 son fiesta.»", "→ «El lunes 2 es festivo.» El lunes es singular: es, no son.", "lunes è singolare: il verbo è es."),
    ("«La vivienda es más mejor.»", "→ «La vivienda es mejor.» Mejor ya es comparativo: sin más.", "mejor è già un comparativo: niente más."),
    ("«La gente votan el 29.»", "→ «La gente vota el 29.» Gente es singular, como un solo grupo.", "gente è singolare: verbo al singolare."),
    ("«Creo que la vivienda sea el tema.»", "→ «Creo que la vivienda es el tema.» Creo que afirma: indicativo.", "creo que afferma: indicativo, es."),
]
# altezza del riquadro = simulazione esatta del ciclo di disegno (correzione W43: simulazione voce per voce, non altezza media di riga)
_sim = 216 + 44
for _w, _r, _n in errs:
    _sim += 17 + len(wrap(_w, "serif", True, 21.5, CW - 44)) * 21.5 * 1.36 \
          + 17 + len(wrap(_r, "serif", False, 20.5, CW - 44)) * 20.5 * 1.36 \
          + 16 + len(wrap(_n, "sans", False, 19.5, CW - 44)) * 19.5 * 1.36 + 4
eh = _sim - 200 + 12
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS · ERRORI TIPICI", 23, "sans", True, OLIVE)
yy3 += 44
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 17, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 17, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 16, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 4
wy = 200 + eh + 16
wt = "« la precampaña » es el tiempo antes de la campaña oficial: las semanas en que los partidos cierran sus listas y escriben sus programas. Esta edición entera es precampaña."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("precampaña = precampagna: prima della campagna ufficiale.", "sans", False, 20, CW - 44)) * 29 + 22
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PALABRA · LA PAROLA", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "precampaña = precampagna: prima della campagna ufficiale.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 16
lt = "«¡Hola! Soy Ana, estudio español en Shanghái. El lunes 2 no tengo puente, pero el domingo veo el Atlético–Barça con mis amigos — ¡y antes, la NFL! ¡Gracias por el periódico!» — Ana (ejemplo, escrito por la redacción)"
# FIX1 Problem 2: on-page disclosure (parent decision) — no real letters / best P8
# texts had arrived by press time, so the labeled editor's example is printed and
# the W43 promise carries to VOL.3. Spanish + matching Chinese note, inside this box.
ld = "Nota de la redacción: al cierre no había cartas reales ni los mejores textos de la página 8; publicamos este ejemplo y la promesa pasa al VOL.3."
ldcn = "Nota della redazione: senza lettere vere né migliori testi di pagina 8, pubblichiamo questo esempio; la promessa passa al VOL.3. Scriveteci!"
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
p.text(MX, fy + 24, "FRASES DE LA SEMANA · LE FRASI DELLA SETTIMANA (testuali, da questo numero)", 27, "sans", True, OLIVE)
quotes = [
    ("«Las listas ya están presentadas: ahora los partidos escriben sus programas.»", "Le liste sono presentate: ora i partiti scrivono i programmi.", "Página 1"),
    ("«El lunes 2 de noviembre es festivo en nueve comunidades — y día de trabajo en las demás.»", "Lunedì 2 novembre è festa in nove comunità e giorno di lavoro nelle altre.", "Página 2"),
    ("«Tres fiestas, una misma noche de otoño.»", "Tre feste, una stessa notte d'autunno.", "Página 3"),
    ("«El Madrid ganó 2–1 en el Camp Nou: fue la primera derrota liguera del Barça.»", "Il Real vince 2–1 al Camp Nou: è la prima sconfitta in Liga del Barça.", "Página 4"),
    ("«El Bernabéu cambia el césped por el emparrillado: el fútbol americano llega a Madrid.»", "Il Bernabéu cambia l'erba con la griglia: il football americano arriva a Madrid.", "Página 5"),
    ("«La vivienda es el principal problema para el 55,7 % de los españoles.»", "La casa è il primo problema per il 55,7% degli spagnoli.", "Página 6"),
    ("«Una encuesta es una foto con margen de error, tomada en un día concreto.»", "Un sondaggio è una foto con margine di errore, scattata in un giorno preciso.", "Página 6"),
    ("«El domingo 8, Madrid tiene dos citas: la NFL a las 15:30 y el Atlético–Barça a las 21:00.»", "Domenica 8, Madrid ha due appuntamenti: la NFL alle 15:30 e l'Atlético–Barça alle 21:00.", "Página 1"),
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
p.text(MX + 28, py + 44, "LA PRÓXIMA SEMANA · LA PROSSIMA SETTIMANA (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "El viernes 13: empieza la campaña electoral. El domingo 29: España vota. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lengua.svg")
print("P7 saved, exercises so far:", len(REG))
