# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-es-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · KULTUR", "La Lucerna", "A2 → B1 · Las fiestas del otoño · Die Feste des Herbstes")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Fiestas de otoño: un puente partido en dos Españas", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: A2 → B1")
f.para("El domingo 1 de noviembre es el Día de Todos los Santos, una de las fiestas más queridas de España. Las familias van al cementerio, llevan flores a sus muertos y comen dulces de la temporada. Este año la fiesta cae en domingo — y ahí empieza el problema.")
f.para("Cuando una fiesta cae en domingo, algunas comunidades pasan el día libre al lunes. Este año, el lunes 2 de noviembre es festivo solo en nueve comunidades: Andalucía, Aragón, Asturias, Canarias, Castilla-La Mancha, Castilla y León, Extremadura, Madrid y Navarra. Allí, el fin de semana dura tres días: del 31 de octubre al 2 de noviembre.")
f.para("En las demás — Baleares, Cantabria, Cataluña, Galicia, Murcia, el País Vasco, La Rioja, la Comunitat Valenciana, Ceuta y Melilla — el lunes 2 es un día de trabajo normal. España se divide en dos: unos hacen puente y otros, no. Por eso estos días todos preguntan lo mismo: «¿El lunes es fiesta en mi comunidad?»")
f.para("La noche anterior, el sábado 31 de octubre, llega Halloween — una fiesta que viene de fuera, pero que ya es parte del otoño español, sobre todo para los niños. En la página 5 contamos qué disfraces busca España este año.")
f.para("Pero España también tiene sus fiestas propias para estas fechas. En Cataluña, la Castanyada: castañas asadas, boniatos y panellets, unos dulces pequeños de mazapán. En Galicia, el Samaín, una fiesta muy antigua de la noche de los muertos. Tres fiestas, una misma noche de otoño.")
f.gloss("el cementerio der Friedhof · el dulce die Süßigkeit · festivo Feiertag, frei · el homenaje die Ehrung, das Gedenken · el mazapán das Marzipan.")
f.head("RECORDAR JUNTOS · GEDENKEN", 25)
f.para("El jueves 29 de octubre se cumplen dos años de la DANA de Valencia de 2024, la tormenta que dejó 233 muertos, según la cifra de las asociaciones de víctimas.")
f.para("Esta semana, Catarroja homenajeó a los servicios de emergencia y a los voluntarios de aquellos días, con unas 1.300 distinciones. Los representantes de las entidades locales han pedido que el día 29 no haya plenos en los ayuntamientos, para facilitar los actos de memoria. Desde La Lucerna, nos sumamos al recuerdo.")
f.end_report()

# col 3: chestnut image + facts + ¿Y tú? (sequential)
ix = COLX[3]
image(p, "castanas.jpg", ix, 200, CW, 430)
cy3 = caption(p, ix, 630, CW, "Castañas asadas, las protagonistas de la Castanyada: en Cataluña, la noche del 31 de octubre huele a castaña caliente y a boniato asado.",
              "Foto: Wikimedia Commons — CC0 (dominio público)")
facts = ["El lunes 2 de noviembre es festivo en 9 comunidades — y día de trabajo en las demás.",
         "En la Castanyada se comen castañas asadas, boniatos y panellets, dulces de mazapán.",
         "El Samaín gallego es una fiesta muy antigua: la noche de los muertos."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "TRES FIESTAS, UNA NOCHE", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Qué fiesta te gusta más: Halloween, la Castanyada o el Samaín? ¿Y qué comes ese día? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Welches Fest magst du am liebsten? Was isst du an dem Tag? Schreibe zwei Sätze auf Spanisch.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ? · UND DU?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Welches Fest magst du am liebsten? Was isst du an dem Tag? Schreibe zwei Sätze auf Spanisch.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · ÜBUNGEN", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8 · Aufgaben gemischt, nach Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · ¿VERDADERO O FALSO?", 25)
e.bridge("Lies den Text auf Seite 3: richtig oder falsch?")
e.ex("A2", "判断对错", "Verdadero", "Allerheiligen ist am 1. November",
     "El Día de Todos los Santos es el 1 de noviembre. ¿Verdadero o falso?", instr="Richtig oder falsch", size=20, gap=8)
e.ex("A2", "判断对错", "Falso", "nur 9 Regionen frei, nicht ganz Spanien",
     "El lunes 2 de noviembre es festivo en toda España. ¿Verdadero o falso?", instr="Richtig oder falsch", size=20, gap=8)
e.ex("A2", "判断对错", "Verdadero", "zur Castanyada isst man Kastanien und panellets",
     "En la Castanyada se comen castañas asadas y panellets. ¿Verdadero o falso?", instr="Richtig oder falsch", size=20, gap=8)
e.ex("B1", "判断对错", "Falso", "altes galicisches Fest, nicht Halloween",
     "El Samaín es el nombre gallego de Halloween. ¿Verdadero o falso?", instr="Richtig oder falsch", size=20, gap=8)
e.ex("A2", "判断对错", "Verdadero", "Madrid: eine der 9, drei Tage frei",
     "En Madrid, el fin de semana del 31 al 2 dura tres días. ¿Verdadero o falso?", instr="Richtig oder falsch", size=20, gap=8)
e.head("B · PALABRAS DEL TEXTO", 25)
e.bridge("Fülle die Lücken mit den Wörtern aus dem Kasten.")
e.para("flores · cementerio · festivo · castañas · puente", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "完成句子", "flores", "Blumen für die Verstorbenen: flores",
     "Las familias llevan ___ al cementerio.", instr="Ausfüllen", size=20, gap=8)
e.ex("A2", "完成句子", "cementerio", "cementerio = Friedhof",
     "El 1 de noviembre las familias van al ___.", instr="Ausfüllen", size=20, gap=8)
e.ex("A2", "完成句子", "festivo", "festivo = Feiertag, frei",
     "El lunes 2 es ___ en nueve comunidades.", instr="Ausfüllen", size=20, gap=8)
e.ex("A2", "完成句子", "castañas", "castañas asadas = geröstete Kastanien",
     "En la Castanyada comemos ___ asadas.", instr="Ausfüllen", size=20, gap=8)
e.ex("A2", "完成句子", "puente", "hacer puente = einen Brückentag machen",
     "Con tres días libres, hacemos ___.", instr="Ausfüllen", size=20, gap=8)
e.head("C · COMPRENSIÓN", 25)
e.bridge("Wähle die richtige Antwort.")
e.ex("A2", "单选", "B", "Allerheiligen am 1. November",
     "¿Cuándo es Todos los Santos? A. el 31 de octubre · B. el 1 de noviembre · C. el 2 de noviembre", size=20, gap=8)
e.ex("A2", "单选", "A", "neun Regionen",
     "¿En cuántas comunidades es festivo el lunes 2? A. en nueve · B. en todas · C. en ninguna", size=20, gap=8)
e.ex("B1", "单选", "B", "der Samaín ist ein sehr altes galicisches Fest",
     "¿Qué es el Samaín? A. un dulce de mazapán · B. una fiesta gallega muy antigua · C. un disfraz", size=20, gap=8)
e.ex("B1", "单选", "C", "Catarroja ehrte Rettungsdienste und Freiwillige",
     "¿Qué pasó en Catarroja esta semana? A. un partido · B. una fiesta de Halloween · C. un homenaje a emergencias y voluntarios", size=20, gap=8)
e.head("D · CONSTRUIR FRASES", 25)
e.bridge("Bilde aus den Wörtern richtige Sätze.")
e.ex("A2", "造句", "Las familias llevan flores al cementerio.", "Verb an 2. Stelle",
     "las familias / llevan / flores / al cementerio → ___", instr="Sätze bilden", size=20, gap=8)
e.ex("B1", "造句", "El lunes es festivo en nueve comunidades.", "Ortsangabe am Ende",
     "el lunes / es festivo / en nueve comunidades → ___", instr="Sätze bilden", size=20, gap=8)
e.ex("B1", "造句", "En Cataluña comemos castañas asadas.", "Ortsangabe vorn, Verb an 2. Stelle",
     "en Cataluña / comemos / castañas asadas → ___", instr="Sätze bilden", size=20, gap=8)
e.ex("B1", "句型转换", "Todos preguntan si el lunes es fiesta.", "indirekte Frage mit si",
     "«¿El lunes es fiesta?» (todos preguntan) → ___", instr="Umformen", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · DEPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("DEPORTE · SPORT", "La Lucerna", "NIVEL B1 · La semana del Clásico · Die Woche des Clásico")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("La semana del Clásico: Europa primero, el domingo a las 21:00", 37)
f.byline("De la redacción deportiva de La Lucerna · Nivel de lectura: B1")
f.para("¡Qué semana de fútbol! El martes y el miércoles se juega la jornada 3 de la Champions, y el domingo llega el partido más grande: el primer Clásico de la temporada, en el Camp Nou, a las 21:00.")
f.para("El martes fue una noche de 40 goles en Europa — y de malas noticias para el Barça. El PSG ganó 4–2 en París: fue la primera derrota azulgrana de la temporada. Doué marcó el primero; Espart empató; Lucas Hernández puso el 2–1 de cabeza; Yamal empató otra vez; y al final, Vitinha y Fabián Ruiz cerraron el 4–2.")
f.para("Los otros dos equipos españoles jugaron también el martes: el Liverpool ganó 4–3 al Villarreal en un partido loco, y el Atlético empató 1–1 en Stuttgart. El gol rojiblanco fue de Julián Álvarez, que cortó así una sequía de casi medio año sin marcar.")
f.para("Esta noche (21:00) juegan los otros dos equipos españoles: el Real Madrid recibe al RB Leipzig en el Bernabéu — la última prueba antes del Clásico — y el Real Betis recibe al Feyenoord en La Cartuja. Los resultados llegan después del cierre de esta edición: los contamos la próxima semana.")
f.para("Y el domingo, la gran pregunta no es solo quién gana. A las 21:00 empieza también la carrera de Fórmula 1 en Austin: Alonso y Sainz, empatados a siete puntos, corren a la misma hora que el Clásico. Este domingo, España elige: ¿fútbol o coches?")
f.gloss("la jornada der Spieltag · el marcador der Spielstand · empatar unentschieden spielen · la sequía die Torflaute · cerrar el partido den Sieg sichern.")
f.end_report()

# col 3: Clásico data box + ¿Y tú? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "EL CLÁSICO EN DATOS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Domingo 25 de octubre, 21:00 · Spotify Camp Nou · Jornada 10 de LaLiga. El Barça llega líder, sin perder en la Liga. El Madrid de Mourinho llega a seis puntos, después de perder el derbi. El partido está declarado de alto riesgo, y LaLiga prepara una semana especial: «El 25 de octubre los astros se alinean».", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "¿Y tú? El domingo a las 21:00, ¿qué miras: el Clásico o la Fórmula 1? ¿Y quién gana el Clásico? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Was schaust du am Sonntag um 21:00 Uhr — und wer gewinnt den Clásico? Schreibe zwei Sätze auf Spanisch.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "¿Y TÚ? · UND DU?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Was schaust du am Sonntag um 21:00 Uhr — und wer gewinnt den Clásico? Schreibe zwei Sätze auf Spanisch.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SEMANA EUROPEA Y EL GRAN DOMINGO · DIE EUROPÄISCHE WOCHE UND DER GROSSE SONNTAG", 26, "sans", True, OLIVE)
rows = [
    ("Mar 20.10.", "Champions · J3", "PSG 4–2 FC Barcelona — primera derrota azulgrana de la temporada"),
    ("Mar 20.10.", "Champions · J3", "Liverpool FC 4–3 Villarreal CF — un partido loco"),
    ("Mar 20.10.", "Champions · J3", "VfB Stuttgart 1–1 Atlético de Madrid (gol de Julián Álvarez)"),
    ("Mié 21.10.", "21:00", "Real Madrid – RB Leipzig (Bernabéu) · Real Betis – Feyenoord (La Cartuja)"),
    ("Vie–Dom", "F1 · Austin", "Entrenamientos el viernes · clasificación el sábado (23:00, hora peninsular)"),
    ("Dom 25.10.", "21:00", "EL CLÁSICO: FC Barcelona – Real Madrid (Camp Nou) + la carrera de F1 en Austin"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Atención: los partidos del miércoles terminan después del cierre de esta edición — por eso aquí son previa, sin resultados."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · ÜBUNGEN", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8 · Aufgaben gemischt, nach Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPRENSIÓN", 25)
e.bridge("Lies den Text auf Seite 4 und wähle die richtige Antwort.")
e.ex("B1", "单选", "A", "PSG gewinnt 4:2",
     "¿Cómo terminó el PSG – Barça? A. 4–2 para el PSG · B. 2–2 · C. 4–2 para el Barça", size=20, gap=8)
e.ex("B1", "单选", "B", "Julián Álvarez schießt das Tor",
     "¿Quién marcó el gol del Atlético en Stuttgart? A. Vitinha · B. Julián Álvarez · C. Lamine Yamal", size=20, gap=8)
e.ex("B1", "单选", "C", "Villarreal verliert 4:3 in Liverpool",
     "El Villarreal perdió... A. 0–1 en casa · B. 2–2 · C. 4–3 en Liverpool", size=20, gap=8)
e.ex("B1", "单选", "A", "der Clásico ist am Sonntag um 21:00 Uhr",
     "El Clásico se juega... A. el domingo a las 21:00 · B. el sábado a las 18:00 · C. el miércoles", size=20, gap=8)
e.ex("B1", "单选", "B", "zur selben Zeit fährt die Formel 1 in Austin",
     "El domingo a las 21:00 también hay... A. un concierto · B. la carrera de F1 en Austin · C. una fiesta", size=20, gap=8)
e.head("B · LAS PALABRAS", 25)
e.match_set("B1", "词汇配对",
            ["el marcador", "la jornada", "el banquillo", "empatar"],
            ["el sitio del entrenador junto al campo",
             "el resultado de un partido, con los goles",
             "terminar un partido con el mismo resultado",
             "cada una de las rondas de una liga"],
            ["b", "d", "a", "c"],
            ["marcador = Spielstand (b)", "jornada = Spieltag (d)", "banquillo = Trainerbank (a)", "empatar = unentschieden spielen (c)"],
            instr="Zuordnen")
e.head("C · COMPARATIVOS", 25)
e.bridge("Ergänze den Komparativ oder die -ísimo-Form des Wortes in Klammern.")
e.ex("B1", "完成句子", "más grande", "más + grande bildet den Komparativ",
     "El Clásico es ___ que un partido normal de Liga. (grande)", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "完成句子", "muchísimos", "muchísimos goles (40 in ganz Europa)",
     "El martes hubo ___ goles: ¡40 en toda Europa! (muchos)", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "完成句子", "peor", "der Komparativ von malo ist peor",
     "El Barça tuvo su ___ (malo) noche de la temporada en París.", instr="Ausfüllen", size=20, gap=8)
e.ex("B1", "完成句子", "mejor", "der Komparativ von bueno ist mejor",
     "Alonso quiere su ___ (bueno) resultado del año en Austin.", instr="Ausfüllen", size=20, gap=8)
e.head("D · EL PRETÉRITO INDEFINIDO", 25)
e.bridge("Setze die Sätze ins pretérito indefinido (Vergangenheit).")
e.ex("B1", "句型转换", "El PSG ganó 4–2 en París.", "ganar → ganó",
     "El PSG gana 4–2 en París. → ___", instr="Umformen", size=20, gap=8)
e.ex("B1", "句型转换", "Lamine Yamal marcó el 2–2.", "marcar → marcó",
     "Lamine Yamal marca el 2–2. → ___", instr="Umformen", size=20, gap=8)
e.ex("B1", "句型转换", "El Villarreal perdió 4–3 en Liverpool.", "perder → perdió",
     "El Villarreal pierde 4–3 en Liverpool. → ___", instr="Umformen", size=20, gap=8)
e.ex("B1", "句型转换", "Julián Álvarez cortó su sequía.", "cortar → cortó",
     "Julián Álvarez corta su sequía. → ___", instr="Umformen", size=20, gap=8)
e.ex("B1", "句型转换", "Los aficionados fueron al estadio.", "ir → fueron (wie ser)",
     "Los aficionados van al estadio. → ___", instr="Umformen", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-deporte.svg")
print("P4 saved, exercises so far:", len(REG))
