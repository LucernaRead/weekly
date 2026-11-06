# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P3 San Martín / P4 Nations League. Fresh text, structure mirrors W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · Cultuur", "La Lucerna", "A2 → B1 · San Martín, castañas y vino nuevo · San Martín, kastanjes en nieuwe wijn")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("San Martín: la capa, las castañas y el veranillo", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: A2 → B1")
f.para("El miércoles 11 de noviembre es San Martín, y en muchos pueblos de España es día de fiesta, de castañas y de vino nuevo.")
f.para("Cuenta la leyenda que Martín, soldado romano, partió su capa en dos con la espada para cubrir a un mendigo que moría de frío. Y el cielo le regaló unos días de sol: el veranillo de San Martín, ese calor suave que llega a mitad del otoño, justo antes de que el frío se instale de verdad.")
f.para("En Moreda de Aller, en Asturias, la Fiesta de San Martín o de los Humanitarios empieza con una misa cantada al son de las gaitas. Después llega la puya del ramu, la subasta del pan de escanda bendecido, y un desfile de carrozas con bandas de gaitas y trajes tradicionales.")
f.para("Y en la mesa, la comida de San Martín: fabada, casadiellas y panchón. En Galicia y en Castilla y León, el magosto pone castañas asadas y vino nuevo en la mesa. Tres fiestas, una misma tarde de otoño.")
f.gloss("la capa = de mantel · el mendigo = de bedelaar · el veranillo = de nazomer · la gaita = de doedelzak · el magosto = het kastanjefeest.")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Heb je wel eens geroosterde kastanjes gegeten? Kent jouw land een «nazomer» zoals de veranillo? Schrijf twee zinnen en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ? · En jij?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Heb je wel eens geroosterde kastanjes gegeten? Kent jouw land een «nazomer» zoals de veranillo? Schrijf twee zinnen en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · Oefeningen van pagina 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · Niveaus door elkaar — zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · ¿VERDADERO O FALSO?", 25)
e.expl("Lees het artikel op pagina 3: waar of niet waar?")
e.ex("A2", "Lezen: waar/onwaar", "Verdadero", "Sint-Maarten is woensdag 11 november",
     "San Martín se celebra el miércoles 11 de noviembre. ¿Verdadero o falso?", instr="W/NW", size=20, gap=8)
e.ex("A2", "Lezen: waar/onwaar", "Verdadero", "Maarten deelde zijn mantel met de bedelaar",
     "Martín partió su capa para cubrir a un mendigo. ¿Verdadero o falso?", instr="W/NW", size=20, gap=8)
e.ex("A2", "Lezen: waar/onwaar", "Falso", "Het feest van de Humanitarios is in Asturië, niet in Galicië",
     "La Fiesta de los Humanitarios se celebra en Galicia. ¿Verdadero o falso?", instr="W/NW", size=20, gap=8)
e.ex("B1", "Lezen: waar/onwaar", "Falso", "De veranillo zijn een paar milde dagen in de herfst, geen zomer",
     "El veranillo de San Martín es el verano. ¿Verdadero o falso?", instr="W/NW", size=20, gap=8)
e.ex("A2", "Lezen: waar/onwaar", "Verdadero", "De maaltijd van Sint-Maarten heeft fabada, casadiellas en panchón",
     "La comida de San Martín incluye fabada y casadiellas. ¿Verdadero o falso?", instr="W/NW", size=20, gap=8)
e.head("B · PALABRAS DEL TEXTO", 25)
e.expl("Vul in met de woorden uit het kader.")
e.para("capa · mendigo · castañas · gaita · veranillo", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Zinnen aanvullen", "capa", "Maarten sneed zijn eigen mantel (capa) doormidden",
     "Martín partió su ___ en dos.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "mendigo", "mendigo = bedelaar",
     "El ___ moría de frío junto a la puerta.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "castañas", "castañas asadas = geroosterde kastanjes",
     "En el magosto comemos ___ asadas.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "gaita", "gaita = doedelzak",
     "La misa de San Martín suena al son de la ___.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "veranillo", "veranillo de San Martín = nazomer van Sint-Maarten",
     "En noviembre llega el ___ de San Martín.", instr="Vul in", size=20, gap=8)
e.head("C · COMPRENSIÓN", 25)
e.expl("Kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "Het feest van de Humanitarios is in Moreda de Aller",
     "¿Dónde se celebra la Fiesta de los Humanitarios? A. en Galicia · B. en Moreda de Aller · C. en Madrid", size=20, gap=8)
e.ex("A2", "Meerkeuze", "A", "De puya del ramu is de veiling van het gezegende brood",
     "¿Qué es la puya del ramu? A. la subasta del pan bendecido · B. un baile · C. un dulce", size=20, gap=8)
e.ex("B1", "Meerkeuze", "C", "De veranillo zijn een paar dagen mild weer in de herfst",
     "¿Qué es el veranillo de San Martín? A. una fiesta · B. un plato · C. unos días de sol suave en otoño", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Na Sint-Maarten zijn de verkiezingen op 29 november",
     "Después de San Martín, la próxima gran fecha es... A. el puente · B. las elecciones del 29 · C. la Navidad", size=20, gap=8)
e.head("D · CONSTRUIR FRASES", 25)
e.expl("Zet de woorden in de juiste volgorde voor een correcte zin.")
e.ex("A2", "Zinnen maken", "Martín parte su capa en dos.", "Het werkwoord op de tweede plaats",
     "Martín / parte / su capa / en dos → ___", instr="Zinnen maken", size=20, gap=8)
e.ex("B1", "Zinnen maken", "En noviembre comemos castañas asadas.", "De tijd vooraan, het werkwoord als tweede",
     "en noviembre / comemos / castañas asadas → ___", instr="Zinnen maken", size=20, gap=8)
e.ex("B1", "Zinnen maken", "En Moreda celebran San Martín.", "De plaats vooraan, het werkwoord als tweede",
     "en Moreda / celebran / San Martín → ___", instr="Zinnen maken", size=20, gap=8)
e.ex("B1", "Zinnen omvormen", "Todos preguntan si hay veranillo.", "Indirecte vragen met si",
     "«¿Hay veranillo?» (todos preguntan) → ___", instr="Herschrijf", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · DEPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("DEPORTE · Sport", "La Lucerna", "NIVEL B1 · Praga el jueves, Inglaterra el domingo · Donderdag Praag, zondag Engeland")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Praga el jueves, Inglaterra el domingo", 37)
f.byline("De la redacción deportiva de La Lucerna · Nivel de lectura: B1")
f.para("La Liga se para y juega la selección: dos partidos de la Liga de Naciones deciden el grupo A3.")
f.para("España, vigente campeona del mundo y de Europa, juega en el grupo A3 con Croacia, Inglaterra y la República Checa. La fase de grupos se cierra esta semana: el jueves 12, a las 20:45, la Roja visita a Chequia en el estadio Letná de Praga; el domingo 15, a las 20:45, recibe a Inglaterra en el Metropolitano de Madrid.")
f.para("El seleccionador Luis de la Fuente dio la lista el viernes 6 de noviembre, y los convocados se concentran el lunes 9 en la Ciudad del Fútbol de Las Rozas. El domingo 15 puede decidir el primer puesto del grupo y la plaza en la fase final de la Liga de Naciones.")
f.para("Y el viernes 13, a las 19:00, la selección sub-21 juega un amistoso contra Japón en Almendralejo (Badajoz). Entre la Roja y la sub-21, esta semana el fútbol español no se para: cambia de camiseta.")
f.gloss("la fase de grupos = de groepsfase · el seleccionador = de bondscoach · la lista = de selectielijst · la plaza = de plaats · el amistoso = de oefenwedstrijd.")
f.end_report()

# col 3: last-Sunday box + ¿Y tú? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "EL DOMINGO 8, DOS CITAS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "El domingo 8, Madrid tuvo dos citas: por la tarde, la NFL en el Bernabéu, y por la noche, el Atlético–Barça en el Metropolitano. Al cierre de esta edición, los resultados no estaban disponibles: esta página no inventa marcadores.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "¿Y tú? El domingo a las 20:45, ¿qué miras: la Roja o la tele? ¿Quién gana el grupo A3: España o Inglaterra? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Welke wedstrijd kijk jij zondag om 20:45? Wie wordt eerste in groep A3: Spanje of Engeland? Schrijf twee zinnen in het Spaans en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "¿Y TÚ? · En jij?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Welke wedstrijd kijk jij zondag om 20:45? Wie wordt eerste in groep A3: Spanje of Engeland? Schrijf twee zinnen in het Spaans en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA LIGA DE NACIONES · GRUPO A3 · Nations League, groep A3: speelschema", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "EJERCICIOS · Oefeningen van pagina 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · Niveaus door elkaar — zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPRENSIÓN", 25)
e.expl("Lees het artikel op pagina 4 en kies het juiste antwoord.")
e.ex("B1", "Meerkeuze", "A", "Spanje speelt in groep A3",
     "España juega en el grupo... A. A3 · B. A1 · C. B3", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Donderdag tegen Tsjechië, zondag tegen Engeland",
     "Esta semana, la Roja juega... A. dos partidos en casa · B. en Praga y en Madrid · C. solo en Praga", size=20, gap=8)
e.ex("B1", "Meerkeuze", "C", "Beide wedstrijden zijn om 20:45",
     "Los dos partidos de la Roja son a las... A. 18:45 · B. 21:00 · C. 20:45", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "De wedstrijd van zondag is in het Metropolitano",
     "El España–Inglaterra se juega en... A. el Metropolitano · B. el Bernabéu · C. Las Rozas", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Jong Spanje (U21) speelt vrijdag tegen Japan",
     "La sub-21 juega el viernes contra... A. Inglaterra · B. Japón · C. Croacia", size=20, gap=8)
e.head("B · LAS PALABRAS", 25)
e.match_set("B1", "Woorden combineren",
            ["la fase de grupos", "el seleccionador", "la lista", "el amistoso"],
            ["un partido sin puntos en juego",
             "la primera parte de un torneo, en grupos",
             "quien elige a los jugadores de la selección",
             "los jugadores convocados para un partido"],
            ["b", "c", "d", "a"],
            ["fase de grupos=groepsfase b", "seleccionador=bondscoach c", "lista=selectielijst d", "amistoso=oefenwedstrijd a"],
            instr="Combineer")
e.head("C · COMPARATIVOS", 25)
e.expl("Vul in met de vergrotende trap of de -ísimo-vorm van het woord tussen haakjes.")
e.ex("B1", "Zinnen aanvullen", "más importante", "más + importante (de groepswinst is belangrijker)",
     "El partido del domingo es ___ que un amistoso. (importante)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "muchísimos", "muchísimos aficionados = heel veel supporters",
     "El Metropolitano espera a ___ aficionados. (muchos)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "peor", "De vergrotende trap van malo is peor",
     "Perder en Praga sería la ___ (malo) noticia de la semana.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "mejor", "De vergrotende trap van bueno is mejor",
     "Ganar el grupo sería la ___ (bueno) noticia del otoño.", instr="Vul in", size=20, gap=8)
e.head("D · EL PRETÉRITO INDEFINIDO", 25)
e.expl("Zet de zinnen in de verleden tijd (pretérito indefinido).")
e.ex("B1", "Zinnen omvormen", "De la Fuente dio la lista el viernes.", "dar → dio",
     "De la Fuente da la lista el viernes. → ___", instr="Herschrijf", size=20, gap=8)
e.ex("B1", "Zinnen omvormen", "La Roja abrió la fase en Londres.", "abrir → abrió",
     "La Roja abre la fase en Londres. → ___", instr="Herschrijf", size=20, gap=8)
e.ex("B1", "Zinnen omvormen", "España jugó en Praga el jueves.", "jugar → jugó",
     "España juega en Praga el jueves. → ___", instr="Herschrijf", size=20, gap=8)
e.ex("B1", "Zinnen omvormen", "Los convocados fueron a Las Rozas.", "De verleden tijd van ir is fueron",
     "Los convocados van a Las Rozas. → ___", instr="Herschrijf", size=20, gap=8)
e.ex("B1", "Zinnen omvormen", "El grupo cerró la fase el domingo.", "cerrar → cerró",
     "El grupo cierra la fase el domingo. → ___", instr="Herschrijf", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-deporte.svg")
print("P4 saved, exercises so far:", len(REG))
