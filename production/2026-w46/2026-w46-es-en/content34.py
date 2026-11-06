# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P3 San Martín / P4 Nations League. Fresh text, structure mirrors W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · Culture", "La Lucerna", "A2 → B1 · San Martín, castañas y vino nuevo · St Martin, chestnuts and new wine")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("San Martín: la capa, las castañas y el veranillo", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: A2 → B1")
f.para("El miércoles 11 de noviembre es San Martín, y en muchos pueblos de España es día de fiesta, de castañas y de vino nuevo.")
f.para("Cuenta la leyenda que Martín, soldado romano, partió su capa en dos con la espada para cubrir a un mendigo que moría de frío. Y el cielo le regaló unos días de sol: el veranillo de San Martín, ese calor suave que llega a mitad del otoño, justo antes de que el frío se instale de verdad.")
f.para("En Moreda de Aller, en Asturias, la Fiesta de San Martín o de los Humanitarios empieza con una misa cantada al son de las gaitas. Después llega la puya del ramu, la subasta del pan de escanda bendecido, y un desfile de carrozas con bandas de gaitas y trajes tradicionales.")
f.para("Y en la mesa, la comida de San Martín: fabada, casadiellas y panchón. En Galicia y en Castilla y León, el magosto pone castañas asadas y vino nuevo en la mesa. Tres fiestas, una misma tarde de otoño.")
f.gloss("la capa = cloak · el mendigo = beggar · el veranillo = St Martin's little summer · la gaita = bagpipes · el magosto = chestnut festival.")
f.head("LO QUE QUEDA DEL OTOÑO", 25)
f.para("El otoño sigue: las tardes cortas, las castañas en la calle y, en la cocina, los primeros guisos de la temporada. Y en la agenda, una fecha que ya mira toda España: el domingo 29 de noviembre, las elecciones generales (página 6).")
f.end_report()

# col 3: chestnut image + facts + ¿Y tú? (sequential)
ix = COLX[3]
image(p, "castanas.jpg", ix, 200, CW, 430)
cy3 = caption(p, ix, 630, CW, "Castañas asadas, las protagonistas del magosto: en noviembre, la noche huele a castaña caliente y a vino nuevo, de Galicia a Castilla y León.",
              "Foto: Wikimedia Commons — CC0 (dominio público)")
facts = ["El miércoles 11 es San Martín: fiesta, castañas y vino nuevo en muchos pueblos.",
         "En Moreda de Aller, la fiesta empieza con misa cantada y gaitas, y sigue con la puya del ramu.",
         "El veranillo de San Martín trae unos días de sol suave a mitad del otoño."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SAN MARTÍN, EN TRES DATOS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Has probado las castañas asadas? ¿Conoces el veranillo de San Martín en tu país? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Have you ever eaten roast chestnuts? Does your country have a ‘little summer’ like the veranillo? Write two sentences and send them in.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ? · Your turn", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Have you ever eaten roast chestnuts? Does your country have a ‘little summer’ like the veranillo? Write two sentences and send them in.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · Page 3 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels are mixed — find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · ¿VERDADERO O FALSO?", 25)
e.bridge("Read the page 3 article: true or false?")
e.ex("A2", "True or false", "Verdadero", "St Martin's Day is on Wednesday 11 November",
     "San Martín se celebra el miércoles 11 de noviembre. ¿Verdadero o falso?", instr="True or false", size=20, gap=8)
e.ex("A2", "True or false", "Verdadero", "Martin shared his cloak with the beggar",
     "Martín partió su capa para cubrir a un mendigo. ¿Verdadero o falso?", instr="True or false", size=20, gap=8)
e.ex("A2", "True or false", "Falso", "The Humanitarios festival is in Asturias, not Galicia",
     "La Fiesta de los Humanitarios se celebra en Galicia. ¿Verdadero o falso?", instr="True or false", size=20, gap=8)
e.ex("B1", "True or false", "Falso", "The veranillo is a few warm days in autumn, not summer",
     "El veranillo de San Martín es el verano. ¿Verdadero o falso?", instr="True or false", size=20, gap=8)
e.ex("A2", "True or false", "Verdadero", "The St Martin meal includes fabada, casadiellas and panchón",
     "La comida de San Martín incluye fabada y casadiellas. ¿Verdadero o falso?", instr="True or false", size=20, gap=8)
e.head("B · PALABRAS DEL TEXTO", 25)
e.bridge("Fill the gaps with the words in the box.")
e.para("capa · mendigo · castañas · gaita · veranillo", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Sentence completion", "capa", "Martin cut his own cloak (capa) in two",
     "Martín partió su ___ en dos.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "mendigo", "mendigo = beggar",
     "El ___ moría de frío junto a la puerta.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "castañas", "castañas asadas = roast chestnuts",
     "En el magosto comemos ___ asadas.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "gaita", "gaita = bagpipes",
     "La misa de San Martín suena al son de la ___.", instr="Fill in", size=20, gap=8)
e.ex("B1", "Sentence completion", "veranillo", "veranillo de San Martín = little summer",
     "En noviembre llega el ___ de San Martín.", instr="Fill in", size=20, gap=8)
e.head("C · COMPRENSIÓN", 25)
e.bridge("Choose the correct answer.")
e.ex("A2", "Multiple choice", "B", "The Humanitarios festival is in Moreda de Aller",
     "¿Dónde se celebra la Fiesta de los Humanitarios? A. en Galicia · B. en Moreda de Aller · C. en Madrid", size=20, gap=8)
e.ex("A2", "Multiple choice", "A", "The puya del ramu is an auction of blessed bread",
     "¿Qué es la puya del ramu? A. la subasta del pan bendecido · B. un baile · C. un dulce", size=20, gap=8)
e.ex("B1", "Multiple choice", "C", "The veranillo is a few days of mild weather in autumn",
     "¿Qué es el veranillo de San Martín? A. una fiesta · B. un plato · C. unos días de sol suave en otoño", size=20, gap=8)
e.ex("B1", "Multiple choice", "B", "After St Martin's Day, the election is on 29 November",
     "Después de San Martín, la próxima gran fecha es... A. el puente · B. las elecciones del 29 · C. la Navidad", size=20, gap=8)
e.head("D · CONSTRUIR FRASES", 25)
e.bridge("Put the words in order to make a correct sentence.")
e.ex("A2", "Sentence building", "Martín parte su capa en dos.", "The verb comes second",
     "Martín / parte / su capa / en dos → ___", instr="Build the sentence", size=20, gap=8)
e.ex("B1", "Sentence building", "En noviembre comemos castañas asadas.", "Time first, verb second",
     "en noviembre / comemos / castañas asadas → ___", instr="Build the sentence", size=20, gap=8)
e.ex("B1", "Sentence building", "En Moreda celebran San Martín.", "Place first, verb second",
     "en Moreda / celebran / San Martín → ___", instr="Build the sentence", size=20, gap=8)
e.ex("B1", "Sentence transformation", "Todos preguntan si hay veranillo.", "Indirect questions use si",
     "«¿Hay veranillo?» (todos preguntan) → ___", instr="Rewrite", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · DEPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("DEPORTE · Sport", "La Lucerna", "NIVEL B1 · Praga el jueves, Inglaterra el domingo · Prague Thursday, England Sunday")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Praga el jueves, Inglaterra el domingo", 37)
f.byline("De la redacción deportiva de La Lucerna · Nivel de lectura: B1")
f.para("La Liga se para y juega la selección: dos partidos de la Liga de Naciones deciden el grupo A3.")
f.para("España, vigente campeona del mundo y de Europa, juega en el grupo A3 con Croacia, Inglaterra y la República Checa. La fase de grupos se cierra esta semana: el jueves 12, a las 20:45, la Roja visita a Chequia en el estadio Letná de Praga; el domingo 15, a las 20:45, recibe a Inglaterra en el Metropolitano de Madrid.")
f.para("El seleccionador Luis de la Fuente dio la lista el viernes 6 de noviembre, y los convocados se concentran el lunes 9 en la Ciudad del Fútbol de Las Rozas. El domingo 15 puede decidir el primer puesto del grupo y la plaza en la fase final de la Liga de Naciones.")
f.para("Y el viernes 13, a las 19:00, la selección sub-21 juega un amistoso contra Japón en Almendralejo (Badajoz). Entre la Roja y la sub-21, esta semana el fútbol español no se para: cambia de camiseta.")
f.gloss("la fase de grupos = group stage · el seleccionador = national coach · la lista = squad list · la plaza = place · el amistoso = friendly.")
f.end_report()

# col 3: last-Sunday box + ¿Y tú? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "EL DOMINGO 8, DOS CITAS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "El domingo 8, Madrid tuvo dos citas: por la tarde, la NFL en el Bernabéu, y por la noche, el Atlético–Barça en el Metropolitano. Al cierre de esta edición, los resultados no estaban disponibles: esta página no inventa marcadores.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "¿Y tú? El domingo a las 20:45, ¿qué miras: la Roja o la tele? ¿Quién gana el grupo A3: España o Inglaterra? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Which match will you watch on Sunday at 20:45? Who tops group A3: Spain or England? Write two sentences in Spanish and send them in.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "¿Y TÚ? · Your turn", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Which match will you watch on Sunday at 20:45? Who tops group A3: Spain or England? Write two sentences in Spanish and send them in.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA LIGA DE NACIONES · GRUPO A3 · Nations League, group A3 fixtures", 26, "sans", True, OLIVE)
rows = [
    ("J1 · 26.09", "20:45", "Inglaterra – España (en Londres, abre la fase)"),
    ("J2 · 29.09", "20:45", "España – Croacia (estreno ante la afición)"),
    ("J3 · 03.10", "20:45", "España – República Checa (en casa)"),
    ("J4 · 06.10", "20:45", "Croacia – España (a domicilio)"),
    ("J5 · 12.11", "20:45", "República Checa – España (Letná, Praga)"),
    ("J6 · 15.11", "20:45", "España – Inglaterra (Metropolitano, Madrid)"),
    ("SUB-21 · 13.11", "19:00", "España – Japón, amistoso en Almendralejo (Badajoz)"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Horarios en hora peninsular. La fase de grupos se cierra el domingo 15: el partido contra Inglaterra puede decidir el primer puesto del grupo A3."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · Page 4 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels are mixed — find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPRENSIÓN", 25)
e.bridge("Read the page 4 article and choose the correct answer.")
e.ex("B1", "Multiple choice", "A", "Spain are in group A3",
     "España juega en el grupo... A. A3 · B. A1 · C. B3", size=20, gap=8)
e.ex("B1", "Multiple choice", "B", "Czechia on Thursday, England on Sunday",
     "Esta semana, la Roja juega... A. dos partidos en casa · B. en Praga y en Madrid · C. solo en Praga", size=20, gap=8)
e.ex("B1", "Multiple choice", "C", "Both matches kick off at 20:45",
     "Los dos partidos de la Roja son a las... A. 18:45 · B. 21:00 · C. 20:45", size=20, gap=8)
e.ex("B1", "Multiple choice", "A", "The Sunday match is at the Metropolitano",
     "El España–Inglaterra se juega en... A. el Metropolitano · B. el Bernabéu · C. Las Rozas", size=20, gap=8)
e.ex("B1", "Multiple choice", "B", "The under-21s play Japan on Friday",
     "La sub-21 juega el viernes contra... A. Inglaterra · B. Japón · C. Croacia", size=20, gap=8)
e.head("B · LAS PALABRAS", 25)
e.match_set("B1", "Vocabulary matching",
            ["la fase de grupos", "el seleccionador", "la lista", "el amistoso"],
            ["un partido sin puntos en juego",
             "la primera parte de un torneo, en grupos",
             "quien elige a los jugadores de la selección",
             "los jugadores convocados para un partido"],
            ["b", "c", "d", "a"],
            ["fase de grupos=group stage b", "seleccionador=national coach c", "lista=squad list d", "amistoso=friendly a"],
            instr="Match word to definition")
e.head("C · COMPARATIVOS", 25)
e.bridge("Fill the gaps with the comparative or -ísimo form of the word in brackets.")
e.ex("B1", "Sentence completion", "más importante", "más + importante (topping the group matters more)",
     "El partido del domingo es ___ que un amistoso. (importante)", instr="Fill in", size=20, gap=8)
e.ex("B1", "Sentence completion", "muchísimos", "muchísimos aficionados = very many fans",
     "El Metropolitano espera a ___ aficionados. (muchos)", instr="Fill in", size=20, gap=8)
e.ex("B1", "Sentence completion", "peor", "The comparative of malo is peor",
     "Perder en Praga sería la ___ (malo) noticia de la semana.", instr="Fill in", size=20, gap=8)
e.ex("B1", "Sentence completion", "mejor", "The comparative of bueno is mejor",
     "Ganar el grupo sería la ___ (bueno) noticia del otoño.", instr="Fill in", size=20, gap=8)
e.head("D · EL PRETÉRITO INDEFINIDO", 25)
e.bridge("Put the sentences into the past (pretérito indefinido).")
e.ex("B1", "Sentence transformation", "De la Fuente dio la lista el viernes.", "dar → dio",
     "De la Fuente da la lista el viernes. → ___", instr="Rewrite", size=20, gap=8)
e.ex("B1", "Sentence transformation", "La Roja abrió la fase en Londres.", "abrir → abrió",
     "La Roja abre la fase en Londres. → ___", instr="Rewrite", size=20, gap=8)
e.ex("B1", "Sentence transformation", "España jugó en Praga el jueves.", "jugar → jugó",
     "España juega en Praga el jueves. → ___", instr="Rewrite", size=20, gap=8)
e.ex("B1", "Sentence transformation", "Los convocados fueron a Las Rozas.", "The past of ir is fueron",
     "Los convocados van a Las Rozas. → ___", instr="Rewrite", size=20, gap=8)
e.ex("B1", "Sentence transformation", "El grupo cerró la fase el domingo.", "cerrar → cerró",
     "El grupo cierra la fase el domingo. → ___", instr="Rewrite", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-deporte.svg")
print("P4 saved, exercises so far:", len(REG))
