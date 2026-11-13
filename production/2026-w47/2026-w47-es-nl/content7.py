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
p.band("LENGUA　Taal", "La Lucerna", "Tres niveles, tres herramientas　Drie niveaus, drie hulpmiddelen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　LA HORA", 24)
a.para("Para decir la hora: «Es la una» en singular, «Son las dos» en plural. Para los minutos: «Son las 20:45» o «las nueve menos cuarto». Y el partido se juega «a las 21:00»: con la preposición a.", 21.5)
a.para("Y ojo con la fecha: «el lunes 16 de noviembre», con el mes en minúscula y el 1 como «el uno».", 21.5)
a.bridge("Tijd: es la una (enkelvoud), son las dos (meervoud); een wedstrijd begint om a las 21:00.")
a.ex("A2", "Zinnen aanvullen", "Es", "Voor 1 uur gebruik je het enkelvoud Es",
     "___ la una en punto.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Zinnen aanvullen", "Son", "Voor meer dan één uur gebruik je het meervoud Son",
     "___ las nueve de la noche.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Zinnen aanvullen", "las", "a las 21:00 (met het voorzetsel a)",
     "El derbi es el sábado a ___ 18:30.", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "Meerkeuze", "B", "1 uur is Es la una",
     "¿Cómo se dice la 1:00? A. Son la una · B. Es la una · C. Es las una", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　COMPARATIVOS", 24)
b.para("Para comparar: más / menos + adjetivo + que; tan + adjetivo + como. Dos irregulares para recordar: bueno → mejor, malo → peor. Y nunca «más mejor»: mejor ya es comparativo.", 21.5)
b.para("El fútbol de esta semana sirve para practicar: más goles que, tan rápido como, mejor que, peor que.", 21.5)
b.bridge("Vergrotende trap: más … que, tan … como; bueno → mejor, malo → peor; zeg nooit más mejor.")
b.ex("B1", "Zinnen aanvullen", "más goles", "más + goles (meer doelpunten)",
     "El Barça marca ___ que el año pasado. (goles)", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Zinnen aanvullen", "tan rápido", "tan + rápido + como (even snel)",
     "El derbi es ___ como siempre. (rápido)", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Zinnen aanvullen", "mejor", "de vergrotende trap van bueno is mejor (zonder más)",
     "Un debate claro es ___ (bueno) que un titular.", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "Meerkeuze", "B", "más mejor is fout",
     "¿Qué forma es correcta? A. más mejor · B. mejor · C. muy mejor", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　EL SUBJUNTIVO", 24)
c.para("Los debates usan el subjuntivo: «es necesario que», «para que», «ojalá» van con subjuntivo — tenga, sea, baje. Pero «creo que» afirma y va con indicativo: creo que es.", 21.5)
c.para("Es la gramática de la página 6: opinar sobre debates y programas sin afirmar más de lo que sabemos.", 21.5)
c.bridge("es necesario que, para que, ojalá met de aanvoegende wijs; creo que met de aantonende wijs.")
c.ex("B2", "Zinnen aanvullen", "baje", "es necesario que + aanvoegende wijs: baje",
     "Es necesario que el precio ___ (bajar).", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Zinnen aanvullen", "sea", "para que + aanvoegende wijs: sea",
     "Publicamos la fuente para que todo ___ (ser) claro.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Zinnen aanvullen", "es", "creo que + aantonende wijs: es",
     "Creo que el debate ___ (ser) útil.", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "Meerkeuze", "B", "ojalá + aanvoegende wijs: tenga",
     "«Ojalá que el debate...» A. tiene datos · B. tenga datos · C. tener datos", size=20.5, gap=10)
c.end_report()

# ---- col 3: manuscript image + errores + palabra + lectores ----
bx = COLX[3]
image(p, "book_hours.jpg", bx, 200, CW, 120)
cy3 = caption(p, bx, 320, CW, "Un libro de horas medieval: letras decoradas que abrían la oración.",
              "Manuscrito medieval — dominio público")
errs = [
    ("«Son la una en punto.»", "→ «Es la una.» Es singular.", "1 uur is enkelvoud: gebruik es."),
    ("«El derbi es más mejor.»", "→ «Es mejor.» Sin más.", "mejor is al een vergrotende trap."),
    ("«La gente votan el 29.»", "→ «La gente vota.» Es singular.", "gente is enkelvoud: werkwoord dus ook."),
    ("«Creo que el debate sea útil.»", "→ «Creo que el debate es útil.»", "creo que bevestigt: aantonende wijs es."),
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
p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS　Fouten", 23, "sans", True, OLIVE)
yy3 += 44
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 17, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 17, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 16, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 4
wy = ey0 + eh + 16
wt = "« el debate » es la discusión con turnos: cuatro portavoces el viernes 13; el lunes 16, un cara a cara propuesto."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("debate = debat: een openbare discussie; de verkiezingen zijn op de 29e.", "sans", False, 20, CW - 44)) * 29 + 42
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PALABRA　Woord van de week", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "debate = debat: een openbare discussie; de verkiezingen zijn op de 29e.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 16
lt = "«¡Hola! Soy Marta, estudio español en Pekín. El lunes 16 escucho flamenco y el sábado veo el derbi. ¡Gracias por el periódico!» — Marta (ejemplo, escrito por la redacción)"
ld = "Nota de la redacción: sin cartas reales ni mejores textos al cierre, publicamos este ejemplo; la promesa pasa al VOL.5."
ldcn = "Noot van de redactie: bij het sluiten geen echte brieven of beste teksten; dit nummer drukt een voorbeeldbrief. De belofte schuift door naar VOL.5."
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
p.text(MX, fy + 24, "FRASES DE LA SEMANA　Zinnen van de week (letterlijk uit dit nummer)", 27, "sans", True, OLIVE)
quotes = [
    ("«La campaña electoral empezó el viernes 13, a las 00:00, y dura quince días: hasta el viernes 27 de noviembre.»", "De campagne begint op de 13e om middernacht, duurt 15 dagen en eindigt op de 27e.", "Pagina 1"),
    ("«El jueves 19 es un día clave: termina el plazo para pedir el voto por correo.»", "Donderdag 19 is een sleuteldag: laatste dag om een briefstem aan te vragen.", "Pagina 2"),
    ("«El lunes 16 de noviembre es el Día Internacional del Flamenco, y en España suena la guitarra en todos los rincones.»", "Maandag 16 november is de Internationale Flamencodag, en de gitaar klinkt in heel Spanje.", "Pagina 3"),
    ("«No es solo un baile: es cante, toque y baile, con palmas, taconeo y compás.»", "Flamenco is niet alleen dans: zang, gitaar, dans, handgeklap, voetwerk en ritme.", "Pagina 3"),
    ("«La Liga se para y vuelve: después del parón de selecciones, la jornada 13 se juega del viernes 20 al lunes 23 de noviembre.»", "De competitie stopt en begint weer: speelronde 13 loopt van vrijdag 20 tot maandag 23 november.", "Pagina 4"),
    ("«¿Votas por primera vez el 29 de noviembre? Tienes dos maneras de votar: en persona o por correo.»", "Stem je op 29 november voor het eerst? Twee manieren: in persoon of per post.", "Pagina 5"),
    ("«En campaña, no todo lo que se anuncia está cerrado.»", "Tijdens de campagne is niet alles wat wordt aangekondigd al beslist.", "Pagina 6"),
    ("«Una encuesta es una foto con margen de error, tomada en un día concreto.»", "Een peiling is een foto met foutmarge, genomen op één bepaalde dag.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 128
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = fy + 66 + 3 * 128 + 105 + 1  # D6: align banner with core (2464.5); nl fy sits 29 lower, +30 would put the rect over the footer ink
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "LA PRÓXIMA SEMANA　Volgende week (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "El domingo 29, España vota: los resultados, el Black Friday y la jornada 5 de la Champions. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lengua.svg")
print("P7 saved, exercises so far:", len(REG))
