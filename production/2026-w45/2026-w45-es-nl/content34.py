# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　Cultuur", "La Lucerna", "A2 → B1　La semana pasada: tres noches de otoño　De drie herfstnachten van vorige week")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("La semana pasada: memoria, disfraces y flores", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: A2 → B1")
f.para("La semana pasada, España vivió tres noches seguidas de otoño. El jueves 29 de octubre, Valencia recordó a las víctimas de la DANA de 2024, dos años después de la tormenta. Fueron actos sobrios, de memoria y de homenaje, en los pueblos que más sufrieron.")
f.para("El sábado 31 llegó la noche de los disfraces. Halloween llenó las calles de niños y de monstruos de mentira; en Cataluña, la Castanyada puso castañas asadas, boniatos y panellets en la mesa; en Galicia, el Samaín recordó la fiesta más antigua de la noche de los muertos.")
f.para("Tres fiestas, una misma noche de otoño.")
f.para("Y el domingo 1, Día de Todos los Santos, las familias llevaron flores a los cementerios, como cada año. Después de tres noches de fiesta y de memoria, el lunes 2 llegó el puente para unos y el trabajo para otros (página 2).")
f.gloss("sobrio — ingetogen · el homenaje — een herdenking · el disfraz — een kostuum · el boniato — een zoete aardappel · el cementerio — een begraafplaats.")
f.head("LO QUE QUEDA DEL OTOÑO", 25)
f.para("El otoño sigue: las tardes cortas, las castañas en la calle y, en la cocina, los primeros guisos de la temporada. Y en la agenda, una fecha que ya mira toda España: el domingo 29 de noviembre, las elecciones generales (página 6).")
f.end_report()

# col 3: chestnut image + facts + ¿Y tú? (sequential)
ix = COLX[3]
image(p, "castanas.jpg", ix, 200, CW, 430)
cy3 = caption(p, ix, 630, CW, "Castañas asadas, las protagonistas de la Castanyada: en Cataluña, la noche del 31 de octubre huele a castaña caliente y a boniato asado.",
              "Foto: Wikimedia Commons — CC0 (dominio público)")
facts = ["El jueves 29, Valencia recordó a las víctimas de la DANA de 2024, dos años después.",
         "El sábado 31 se juntaron Halloween, la Castanyada y el Samaín en una sola noche.",
         "El domingo 1, las familias llevaron flores a los cementerios."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "TRES NOCHES, UNA SEMANA", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Qué noche te gusta más: la del 29, la del 31 o la del 1? ¿Y qué comiste el 31? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Welke nacht vind je het mooist: de 29e, de 31e of de 1e? En wat at je op de 31e? Schrijf twee zinnen en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　En jij?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Welke nacht vind je het mooist: de 29e, de 31e of de 1e? En wat at je op de 31e? Schrijf twee zinnen en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　Oefeningen van pagina 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　Niveaus door elkaar — zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　¿VERDADERO O FALSO?", 25)
e.expl("Lees het artikel op pagina 3: waar of niet waar?")
e.ex("A2", "Lezen: waar/onwaar", "Verdadero", "DANA-herdenking: donderdag 29 oktober",
     "Los actos de memoria de la DANA fueron el jueves 29 de octubre. ¿Verdadero o falso?", instr="W/NW", size=20, gap=8)
e.ex("A2", "Lezen: waar/onwaar", "Verdadero", "geroosterde kastanjes, zoete aardappelen en panellets bij de Castanyada",
     "En la Castanyada se comen castañas asadas y panellets. ¿Verdadero o falso?", instr="W/NW", size=20, gap=8)
e.ex("A2", "Lezen: waar/onwaar", "Falso", "de Samaín is een oud Galicisch feest, geen naam voor Halloween",
     "El Samaín es el nombre gallego de Halloween. ¿Verdadero o falso?", instr="W/NW", size=20, gap=8)
e.ex("B1", "Lezen: waar/onwaar", "Falso", "Allerheiligen is op 1 november, niet op 31 oktober",
     "El Día de Todos los Santos es el 31 de octubre. ¿Verdadero o falso?", instr="W/NW", size=20, gap=8)
e.ex("A2", "Lezen: waar/onwaar", "Verdadero", "op zondag brachten families bloemen naar de begraafplaatsen",
     "El domingo 1, las familias llevaron flores a los cementerios. ¿Verdadero o falso?", instr="W/NW", size=20, gap=8)
e.head("B　PALABRAS DEL TEXTO", 25)
e.expl("Vul de gaten in met de woorden uit het kader.")
e.para("flores · cementerio · castañas · disfraz · memoria", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Zinnen aanvullen", "flores", "flores = bloemen, voor de overledenen",
     "Las familias llevan ___ a los cementerios.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "cementerio", "cementerio = begraafplaats",
     "El 1 de noviembre las familias van al ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "castañas", "castañas asadas = geroosterde kastanjes",
     "En la Castanyada comemos ___ asadas.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "disfraz", "disfraz = kostuum",
     "El 31 de octubre los niños llevan ___.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "memoria", "actos de memoria = herdenkingen",
     "El 29 de octubre fueron actos de ___.", instr="Vul in", size=20, gap=8)
e.head("C　COMPRENSIÓN", 25)
e.expl("Kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "de DANA-herdenking was twee jaar na de storm van 2024",
     "¿Qué se recordó el jueves 29? A. un partido · B. la DANA de 2024 · C. una boda", size=20, gap=8)
e.ex("A2", "Meerkeuze", "A", "de Castanyada is in Catalonië",
     "¿Dónde se celebra la Castanyada? A. en Cataluña · B. en Galicia · C. en Madrid", size=20, gap=8)
e.ex("B1", "Meerkeuze", "C", "de Samaín is een heel oud Galicisch feest",
     "¿Qué es el Samaín? A. un dulce · B. un disfraz · C. una fiesta gallega muy antigua", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "na de drie nachten heeft de een maandag een lang weekend en werkt de ander",
     "Después de las tres noches, el lunes 2... A. es fiesta en todas partes · B. unos hacen puente y otros trabajan · C. no pasa nada", size=20, gap=8)
e.head("D　CONSTRUIR FRASES", 25)
e.expl("Zet de woorden in de juiste volgorde.")
e.ex("A2", "Zinnen maken", "Las familias llevan flores al cementerio.", "het werkwoord op de tweede plaats",
     "las familias / llevan / flores / al cementerio → ___", instr="Zinnen maken", size=20, gap=8)
e.ex("B1", "Zinnen maken", "El sábado comemos castañas asadas.", "tijd eerst, werkwoord als tweede",
     "el sábado / comemos / castañas asadas → ___", instr="Zinnen maken", size=20, gap=8)
e.ex("B1", "Zinnen maken", "En Galicia celebran el Samaín.", "plaats eerst, werkwoord als tweede",
     "en Galicia / celebran / el Samaín → ___", instr="Zinnen maken", size=20, gap=8)
e.ex("B1", "Zinnen omvormen", "Todos preguntan si el lunes es fiesta.", "indirecte vragen met si",
     "«¿El lunes es fiesta?» (todos preguntan) → ___", instr="Herschrijf", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · DEPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("DEPORTE　Sport", "La Lucerna", "NIVEL B1　Europa primero, el domingo a las 21:00　Eerst Europa, zondag om 21:00")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Europa primero, el domingo a las 21:00", 32)
f.byline("De la redacción deportiva de La Lucerna　Nivel de lectura: B1")
f.para("El Madrid ganó 2–1 en el Camp Nou: fue la primera derrota liguera del Barça.")
f.para("El Clásico del domingo 25 ya tiene resultado: Kylian Mbappé marcó dos goles y el Real Madrid ganó 2–1 en Barcelona. El Barça, líder hasta entonces, perdió su primer partido de Liga; el Madrid de José Mourinho recortó la distancia a tres puntos. Ahora, una semana después, el Barça tiene su semana de respuesta: primero Europa, luego el Metropolitano.")
f.para("El martes 3 se juega la jornada 4 de la Champions: el Barça recibe al Aston Villa en el Camp Nou, el Atlético recibe al Bayern de Múnich y el Villarreal recibe al París Saint-Germain. El miércoles 4, a las 18:45, el Real Madrid visita al AEK de Atenas. Y el jueves 5, también a las 18:45, la Real Sociedad recibe al Olympique de Lyon en la Europa League.")
f.para("Y el fin de semana, la jornada 12 de Liga: el viernes 6 abre el Sevilla–Alavés (21:00); el sábado 7, el Valencia–Real Madrid en Mestalla (21:00); y el domingo 8, el Atlético–Barça en el Metropolitano (21:00). Entre medias, el domingo por la tarde, el Bernabéu cambia de deporte: la NFL llega a Madrid (página 5).")
f.gloss("la jornada — een speelronde · recortar la distancia — de achterstand verkleinen · recibir — thuis spelen · visitar — op bezoek spelen · el Metropolitano — het stadion van Atlético.")
f.end_report()

# col 3: Clásico data box + ¿Y tú? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX)
p.text(bx + 22, 240, "EL CLÁSICO, UNA SEMANA DESPUÉS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Domingo 25 de octubre, 21:00 · Spotify Camp Nou · Jornada 10 de LaLiga. El Madrid ganó 2–1 con dos goles de Mbappé: primera derrota liguera del Barça. Una semana después, el Barça responde en Europa (martes, Aston Villa) y en el Metropolitano (domingo, Atlético).", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "¿Y tú? El domingo a las 21:00, ¿qué miras: el Atlético–Barça o la NFL? ¿Y quién gana en el Metropolitano? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Welke wedstrijd kijk je zondag om 21:00? Wie wint in het Metropolitano? Schrijf twee zinnen in het Spaans en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "¿Y TÚ?　En jij?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Welke wedstrijd kijk je zondag om 21:00? Wie wint in het Metropolitano? Schrijf twee zinnen in het Spaans en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SEMANA EUROPEA Y LA JORNADA 12　De Europese week en speelronde 12", 26, "sans", True, OLIVE)
rows = [
    ("Mar 3.11.", "Champions · J4", "FC Barcelona – Aston Villa · Atlético – Bayern · Villarreal – PSG"),
    ("Mié 4.11.", "18:45", "AEK Atenas – Real Madrid (Champions)"),
    ("Jue 5.11.", "18:45", "Real Sociedad – Olympique Lyon (Europa League)"),
    ("Vie 6.11.", "21:00", "Sevilla – Alavés (abre la jornada 12)"),
    ("Sáb 7.11.", "14:00–21:00", "Málaga – Racing · Espanyol – Deportivo · Osasuna – Athletic · Valencia – Real Madrid (21:00)"),
    ("Dom 8.11.", "14:00–21:00", "Elche – Betis · Real Sociedad – Rayo · Celta – Levante · Villarreal – Getafe · Atlético – Barça (21:00)"),
    ("Dom 8.11.", "15:30", "NFL EN EL BERNABÉU: Cincinnati Bengals – Atlanta Falcons (página 5)"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Horarios en hora peninsular. La jornada 12 completa, con todos los partidos del domingo, está en la tabla: el domingo 8 se juega también la NFL en el Bernabéu."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　Oefeningen van pagina 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　Niveaus door elkaar — zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPRENSIÓN", 25)
e.expl("Lees het artikel op pagina 4 en kies het juiste antwoord.")
e.ex("B1", "Meerkeuze", "A", "Real Madrid won de Clásico met 2–1",
     "¿Cómo terminó el Clásico del 25? A. 2–1 para el Madrid · B. 2–2 · C. 2–1 para el Barça", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Mbappé scoorde beide doelpunten",
     "¿Quién marcó los dos goles del Madrid? A. Yamal · B. Mbappé · C. Mourinho", size=20, gap=8)
e.ex("B1", "Meerkeuze", "C", "drie Spaanse clubs spelen dinsdag in de Champions League",
     "El martes 3 juegan en Champions... A. solo el Barça · B. solo el Madrid · C. Barça, Atlético y Villarreal", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "Atlético–Barça: zondag, 21:00",
     "El Atlético–Barça se juega... A. el domingo a las 21:00 · B. el sábado a las 18:00 · C. el miércoles", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "zondagmiddag is er ook de NFL in Madrid",
     "El domingo por la tarde, en el Bernabéu, hay... A. un concierto · B. la NFL · C. una fiesta", size=20, gap=8)
e.head("B　LAS PALABRAS", 25)
e.match_set("B1", "Woorden combineren",
            ["la jornada", "recibir", "visitar", "recortar"],
            ["jugar en casa, como local",
             "cada una de las rondas de una liga",
             "reducir una distancia en la tabla",
             "jugar fuera de casa"],
            ["b", "a", "d", "c"],
            ["jornada = een speelronde — b", "recibir = thuis spelen — a", "visitar = op bezoek spelen — d", "recortar = de achterstand verkleinen — c"],
            instr="Combineer")
e.head("C　COMPARATIVOS", 25)
e.expl("Vul de gaten in met de vergrotende trap of de -ísimo-vorm van het woord tussen haakjes.")
e.ex("B1", "Zinnen aanvullen", "más importante", "más + importante (Atlético–Barça telt zwaarder)",
     "El Atlético–Barça es ___ que un partido normal de Liga. (importante)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "muchísimos", "muchísimos partidos = heel, heel veel wedstrijden",
     "El domingo hay ___ partidos: ¡toda la jornada 12! (muchos)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "peor", "de vergrotende trap van malo is peor",
     "El Barça sufrió su ___ (malo) noche de Liga en el Camp Nou.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "mejor", "de vergrotende trap van bueno is mejor",
     "Mbappé firmó su ___ (bueno) noche del año en Barcelona.", instr="Vul in", size=20, gap=8)
e.head("D　EL PRETÉRITO INDEFINIDO", 25)
e.expl("Zet de zinnen in de verleden tijd (pretérito indefinido).")
e.ex("B1", "Zinnen omvormen", "El Madrid ganó 2–1 en el Camp Nou.", "ganar → ganó (hij won)",
     "El Madrid gana 2–1 en el Camp Nou. → ___", instr="Herschrijf", size=20, gap=8)
e.ex("B1", "Zinnen omvormen", "Mbappé marcó dos goles.", "marcar → marcó (hij scoorde)",
     "Mbappé marca dos goles. → ___", instr="Herschrijf", size=20, gap=8)
e.ex("B1", "Zinnen omvormen", "El Barça perdió su primer partido.", "perder → perdió (zij verloren)",
     "El Barça pierde su primer partido. → ___", instr="Herschrijf", size=20, gap=8)
e.ex("B1", "Zinnen omvormen", "Mourinho recortó la distancia.", "recortar → recortó (hij verkleinde)",
     "Mourinho recorta la distancia. → ___", instr="Herschrijf", size=20, gap=8)
e.ex("B1", "Zinnen omvormen", "Los aficionados fueron al estadio.", "ir in de verleden tijd is fueron (zij gingen)",
     "Los aficionados van al estadio. → ___", instr="Herschrijf", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-deporte.svg")
print("P4 saved, exercises so far:", len(REG))
