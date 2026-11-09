# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　CULTURA", "La Lucerna", "A2 → B1　La semana pasada: tres noches de otoño　Tre notti d'autunno, la settimana scorsa")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("La semana pasada: memoria, disfraces y flores", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: A2 → B1")
f.para("La semana pasada, España vivió tres noches seguidas de otoño. El jueves 29 de octubre, Valencia recordó a las víctimas de la DANA de 2024, dos años después de la tormenta. Fueron actos sobrios, de memoria y de homenaje, en los pueblos que más sufrieron.")
f.para("El sábado 31 llegó la noche de los disfraces. Halloween llenó las calles de niños y de monstruos de mentira; en Cataluña, la Castanyada puso castañas asadas, boniatos y panellets en la mesa; en Galicia, el Samaín recordó la fiesta más antigua de la noche de los muertos.")
f.para("Tres fiestas, una misma noche de otoño.")
f.para("Y el domingo 1, Día de Todos los Santos, las familias llevaron flores a los cementerios, como cada año. Después de tres noches de fiesta y de memoria, el lunes 2 llegó el puente para unos y el trabajo para otros (página 2).")
f.gloss("sobrio sobrio, composto · el homenaje l'omaggio · el disfraz il costume · el boniato la patata dolce · el cementerio il cimitero.")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Quale notte preferisci: quella del 29, del 31 o del 1º? E il 31 cosa hai mangiato? Scrivi due frasi e mandale.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　TOCCA A TE", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Quale notte preferisci: quella del 29, del 31 o del 1º? E il 31 cosa hai mangiato? Scrivi due frasi e mandale.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　ESERCIZI　PAGINA 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　livelli misti: cerca per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　¿VERDADERO O FALSO?", 25)
e.bridge("Leggi l'articolo di pagina 3 e di' se è vero o falso.")
e.ex("A2", "判断对错", "Verdadero", "gli atti in memoria della DANA sono stati giovedì 29 ottobre",
     "Los actos de memoria de la DANA fueron el jueves 29 de octubre. ¿Verdadero o falso?", instr="Vero o falso", size=20, gap=8)
e.ex("A2", "判断对错", "Verdadero", "alla Castanyada si mangiano castagne arrosto, patate dolci e panellets",
     "En la Castanyada se comen castañas asadas y panellets. ¿Verdadero o falso?", instr="Vero o falso", size=20, gap=8)
e.ex("A2", "判断对错", "Falso", "il Samaín è un'antica festa galiziana, non la traduzione di Halloween",
     "El Samaín es el nombre gallego de Halloween. ¿Verdadero o falso?", instr="Vero o falso", size=20, gap=8)
e.ex("B1", "判断对错", "Falso", "Ognissanti è il 1º novembre, non il 31 ottobre",
     "El Día de Todos los Santos es el 31 de octubre. ¿Verdadero o falso?", instr="Vero o falso", size=20, gap=8)
e.ex("A2", "判断对错", "Verdadero", "domenica le famiglie hanno portato fiori ai cimiteri",
     "El domingo 1, las familias llevaron flores a los cementerios. ¿Verdadero o falso?", instr="Vero o falso", size=20, gap=8)
e.head("B　PALABRAS DEL TEXTO", 25)
e.bridge("Completa con le parole del riquadro.")
e.para("flores · cementerio · castañas · disfraz · memoria", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "完成句子", "flores", "per i defunti si portano fiori: flores",
     "Las familias llevan ___ a los cementerios.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "cementerio", "cementerio = cimitero",
     "El 1 de noviembre las familias van al ___.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "castañas", "castañas asadas = castagne arrosto",
     "En la Castanyada comemos ___ asadas.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "disfraz", "disfraz = costume",
     "El 31 de octubre los niños llevan ___.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "memoria", "actos de memoria = atti in memoria",
     "El 29 de octubre fueron actos de ___.", instr="Completa", size=20, gap=8)
e.head("C　COMPRENSIÓN", 25)
e.bridge("Scegli la risposta giusta.")
e.ex("A2", "单选", "B", "la memoria della DANA è il secondo anniversario della tempesta del 2024",
     "¿Qué se recordó el jueves 29? A. un partido · B. la DANA de 2024 · C. una boda", size=20, gap=8)
e.ex("A2", "单选", "A", "la Castanyada è in Catalogna",
     "¿Dónde se celebra la Castanyada? A. en Cataluña · B. en Galicia · C. en Madrid", size=20, gap=8)
e.ex("B1", "单选", "C", "il Samaín è un'antica festa galiziana",
     "¿Qué es el Samaín? A. un dulce · B. un disfraz · C. una fiesta gallega muy antigua", size=20, gap=8)
e.ex("B1", "单选", "B", "dopo le tre notti, lunedì c'è chi fa ponte e chi lavora",
     "Después de las tres noches, el lunes 2... A. es fiesta en todas partes · B. unos hacen puente y otros trabajan · C. no pasa nada", size=20, gap=8)
e.head("D　CONSTRUIR FRASES", 25)
e.bridge("Metti le parole in ordine e forma la frase giusta.")
e.ex("A2", "造句", "Las familias llevan flores al cementerio.", "il verbo va al secondo posto",
     "las familias / llevan / flores / al cementerio → ___", instr="Costruisci", size=20, gap=8)
e.ex("B1", "造句", "El sábado comemos castañas asadas.", "il tempo prima, il verbo secondo",
     "el sábado / comemos / castañas asadas → ___", instr="Costruisci", size=20, gap=8)
e.ex("B1", "造句", "En Galicia celebran el Samaín.", "il luogo prima, il verbo secondo",
     "en Galicia / celebran / el Samaín → ___", instr="Costruisci", size=20, gap=8)
e.ex("B1", "句型转换", "Todos preguntan si el lunes es fiesta.", "la domanda indiretta usa si",
     "«¿El lunes es fiesta?» (todos preguntan) → ___", instr="Riscrivi", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · DEPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("DEPORTE　SPORT", "La Lucerna", "NIVEL B1　Europa primero, el domingo a las 21:00　Prima l'Europa, domenica alle 21:00")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Europa primero, el domingo a las 21:00", 32)
f.byline("De la redacción deportiva de La Lucerna　Nivel de lectura: B1")
f.para("El Madrid ganó 2–1 en el Camp Nou: fue la primera derrota liguera del Barça.")
f.para("El Clásico del domingo 25 ya tiene resultado: Kylian Mbappé marcó dos goles y el Real Madrid ganó 2–1 en Barcelona. El Barça, líder hasta entonces, perdió su primer partido de Liga; el Madrid de José Mourinho recortó la distancia a tres puntos. Ahora, una semana después, el Barça tiene su semana de respuesta: primero Europa, luego el Metropolitano.")
f.para("El martes 3 se juega la jornada 4 de la Champions: el Barça recibe al Aston Villa en el Camp Nou, el Atlético recibe al Bayern de Múnich y el Villarreal recibe al París Saint-Germain. El miércoles 4, a las 18:45, el Real Madrid visita al AEK de Atenas. Y el jueves 5, también a las 18:45, la Real Sociedad recibe al Olympique de Lyon en la Europa League.")
f.para("Y el fin de semana, la jornada 12 de Liga: el viernes 6 abre el Sevilla–Alavés (21:00); el sábado 7, el Valencia–Real Madrid en Mestalla (21:00); y el domingo 8, el Atlético–Barça en el Metropolitano (21:00). Entre medias, el domingo por la tarde, el Bernabéu cambia de deporte: la NFL llega a Madrid (página 5).")
f.gloss("la jornada la giornata · recortar la distancia ridurre il distacco · recibir giocare in casa contro · visitar giocare in trasferta contro · el Metropolitano lo stadio dell'Atlético.")
f.end_report()

# col 3: Clásico data box + ¿Y tú? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX)
p.text(bx + 22, 240, "EL CLÁSICO, UNA SEMANA DESPUÉS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Domingo 25 de octubre, 21:00 · Spotify Camp Nou · Jornada 10 de LaLiga. El Madrid ganó 2–1 con dos goles de Mbappé: primera derrota liguera del Barça. Una semana después, el Barça responde en Europa (martes, Aston Villa) y en el Metropolitano (domingo, Atlético).", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "¿Y tú? El domingo a las 21:00, ¿qué miras: el Atlético–Barça o la NFL? ¿Y quién gana en el Metropolitano? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Domenica alle 21:00 quale partita guardi? E in casa dell'Atlético chi vince? Scrivi due frasi in spagnolo e mandale.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "¿Y TÚ?　TOCCA A TE", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Domenica alle 21:00 quale partita guardi? E in casa dell'Atlético chi vince? Scrivi due frasi in spagnolo e mandale.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SEMANA EUROPEA Y LA JORNADA 12　LA SETTIMANA EUROPEA E LA 12ª GIORNATA", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "EJERCICIOS　ESERCIZI　PAGINA 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　livelli misti: cerca per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPRENSIÓN", 25)
e.bridge("Leggi l'articolo di pagina 4 e scegli la risposta giusta.")
e.ex("B1", "单选", "A", "il Real ha vinto il Clásico 2–1",
     "¿Cómo terminó el Clásico del 25? A. 2–1 para el Madrid · B. 2–2 · C. 2–1 para el Barça", size=20, gap=8)
e.ex("B1", "单选", "B", "Mbappé ha segnato due gol",
     "¿Quién marcó los dos goles del Madrid? A. Yamal · B. Mbappé · C. Mourinho", size=20, gap=8)
e.ex("B1", "单选", "C", "martedì tre partite di Champions di squadre spagnole",
     "El martes 3 juegan en Champions... A. solo el Barça · B. solo el Madrid · C. Barça, Atlético y Villarreal", size=20, gap=8)
e.ex("B1", "单选", "A", "domenica alle 21:00 Atlético–Barça",
     "El Atlético–Barça se juega... A. el domingo a las 21:00 · B. el sábado a las 18:00 · C. el miércoles", size=20, gap=8)
e.ex("B1", "单选", "B", "domenica pomeriggio c'è anche la NFL a Madrid",
     "El domingo por la tarde, en el Bernabéu, hay... A. un concierto · B. la NFL · C. una fiesta", size=20, gap=8)
e.head("B　LAS PALABRAS", 25)
e.match_set("B1", "词汇配对",
            ["la jornada", "recibir", "visitar", "recortar"],
            ["jugar en casa, como local",
             "cada una de las rondas de una liga",
             "reducir una distancia en la tabla",
             "jugar fuera de casa"],
            ["b", "a", "d", "c"],
            ["jornada=giornata b", "recibir=giocare in casa contro a", "visitar=giocare in trasferta contro d", "recortar=ridurre il distacco c"],
            instr="Abbina le parole")
e.head("C　COMPARATIVOS", 25)
e.bridge("Completa con il comparativo o la forma in -ísimo della parola tra parentesi.")
e.ex("B1", "完成句子", "más importante", "más + importante (l'Atlético–Barça è più importante)",
     "El Atlético–Barça es ___ que un partido normal de Liga. (importante)", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "muchísimos", "muchísimos partidos = moltissime partite",
     "El domingo hay ___ partidos: ¡toda la jornada 12! (muchos)", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "peor", "il comparativo di malo è peor",
     "El Barça sufrió su ___ (malo) noche de Liga en el Camp Nou.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "mejor", "il comparativo di bueno è mejor",
     "Mbappé firmó su ___ (bueno) noche del año en Barcelona.", instr="Completa", size=20, gap=8)
e.head("D　EL PRETÉRITO INDEFINIDO", 25)
e.bridge("Metti le frasi al passato (pretérito indefinido).")
e.ex("B1", "句型转换", "El Madrid ganó 2–1 en el Camp Nou.", "ganar → ganó",
     "El Madrid gana 2–1 en el Camp Nou. → ___", instr="Riscrivi", size=20, gap=8)
e.ex("B1", "句型转换", "Mbappé marcó dos goles.", "marcar → marcó",
     "Mbappé marca dos goles. → ___", instr="Riscrivi", size=20, gap=8)
e.ex("B1", "句型转换", "El Barça perdió su primer partido.", "perder → perdió",
     "El Barça pierde su primer partido. → ___", instr="Riscrivi", size=20, gap=8)
e.ex("B1", "句型转换", "Mourinho recortó la distancia.", "recortar → recortó",
     "Mourinho recorta la distancia. → ___", instr="Riscrivi", size=20, gap=8)
e.ex("B1", "句型转换", "Los aficionados fueron al estadio.", "il passato di ir è fueron",
     "Los aficionados van al estadio. → ___", instr="Riscrivi", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-deporte.svg")
print("P4 saved, exercises so far:", len(REG))
