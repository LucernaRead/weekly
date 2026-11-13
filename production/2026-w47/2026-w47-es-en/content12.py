# -*- coding: utf-8 -*-
# W47 ES core (VOL.4) — fresh text, week 16–22 Nov 2026. Structure/counts mirror W46.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · PORTADA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 4　CUARTA EDICIÓN", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "CADA SEMANA EN ESPAÑOL　REAL SPANISH, EVERY WEEK", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "SEMANA DEL 16 AL 22 DE NOVIEMBRE DE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "La Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SPANISH WEEKLY　VOL.4　LA CAMPAÑA　LA LIGA　EL FLAMENCO", 36, "serif", True, OLIVE, anchor="middle", spacing=8)
p.text(975, 372, "EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA", 16, "sans", False, GREY, anchor="middle")
p.text(975, 614, "TEXT IN SPANISH　EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "¡LA CAMPAÑA ARRANCA!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Faltan 13 días para el 29-N: la primera semana de campaña.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "FIRST CAMPAIGN WEEK　13 DAYS TO THE ELECTION", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "TOP STORY　SEE PAGES 2 AND 6", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "LA NOTICIA　Top story", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "La campaña arranca: trece días para el 29-N", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "De la redacción de La Lucerna　Nivel de lectura: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("La campaña electoral empezó el viernes 13, a las 00:00, y dura quince días: hasta el viernes 27 de noviembre. El sábado 28 es la jornada de reflexión: un día de silencio, sin propaganda ni actos de campaña. El domingo 29, España vota en elecciones generales.")
f.para("El primer debate fue también el viernes 13: a las 21:30, en laSexta, cuatro portavoces hablaron de economía. Fue el único debate cerrado al cierre de esta edición.")
f.para("El lunes 16, el PP propone un cara a cara entre Sánchez y Feijóo. Los dos partidos aceptan la cita, pero no hay hora publicada: esta página no da por cerrado lo que aún se negocia (página 6).")
f.para("¿Y el que quiera votar por correo? Tiene que pedirlo hasta el jueves 19: la documentación llega a casa desde el lunes 9 (página 5).")
f.para("Y esta semana la música manda: el lunes 16 es el Día Internacional del Flamenco, y el domingo 22, Santa Cecilia, la patrona de los músicos (página 3).")
f.para("El viernes 20 vuelve el fútbol de verdad: la jornada 13 de Liga, con el derbi Sevilla–Betis el sábado (página 4).")
f.bridge("Note | la campaña electoral = election campaign · el debate = debate · el cara a cara = face-to-face debate · el voto por correo = postal vote · la jornada de reflexión = reflection day.")
f.box("LA SEMANA EN CIFRAS　Numbers", [
    ("13 — días faltan el lunes 16 para las elecciones del domingo 29 (13 days to the election)", "serif", False, INK, 20.5, 1.35),
    ("15 — días dura la campaña electoral, del viernes 13 al viernes 27 (a 15-day campaign)", "serif", False, INK, 20.5, 1.35),
    ("19 — jueves, último día para pedir el voto por correo (Thursday 19: last day to apply for a postal vote)", "serif", False, INK, 20.5, 1.35),
], tsize=21)
f.head("AHORA TÚ　Now you try", 25)
f.ex("A2", "Sentence completion", "13", "The campaign starts on Friday 13 November at midnight",
     "La campaña electoral empieza el viernes ___ de noviembre.", size=20.5)
f.ex("A2", "Sentence completion", "29", "The election is on Sunday 29 November",
     "España vota en elecciones generales el domingo ___ de noviembre.", size=20.5)
f.ex("A2", "Sentence completion", "19", "Postal votes must be requested by the 19th at the latest",
     "El voto por correo se pide hasta el jueves ___ de noviembre.", size=20.5)
f.ex("A2", "Sentence completion", "16", "International Flamenco Day, Monday 16 November",
     "El Día Internacional del Flamenco es el lunes ___ de noviembre.", size=20.5)
f.ex("B1", "Sentence completion", "20", "Matchday 13 kicks off on Friday 20 November",
     "La jornada 13 de Liga vuelve el viernes ___ de noviembre.", size=20.5)
f.ex("B1", "Sentence completion", "15", "The campaign lasts 15 days",
     "La campaña electoral dura ___ días.", size=20.5)
f.end_report()

# ---- claves de la semana (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 720, fill=BOX)
p.text(gx + 22, gy + 40, "CINCO", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "CLAVES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Five keys　Para entender la semana", 19, "sans", False, GREY)
gt = [
    ("El primer debate", 250),
    ("El cara a cara del lunes", 226),
    ("El voto por correo", 196),
    ("La Liga vuelve", 158),
    ("Flamenco y Santa Cecilia", 122),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE)
    byy += 92
p.text(gx + 22, byy + 16, "Cinco claves, sin números", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "inventados: todo está explicado", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 68, "en esta edición.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 102, "Five keys — no invented numbers.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "EN ESTA EDICIÓN　In this issue", 24, "sans", True, OLIVE)
som = [
    ("Pág. 2", "La semana, día a día", "A2"),
    ("Pág. 3", "Flamenco y música", "A2→B1"),
    ("Pág. 4", "Vuelve la Liga", "B1"),
    ("Pág. 5", "Votar por primera vez", "B1"),
    ("Pág. 6", "Leer la campaña", "B2"),
    ("Pág. 7", "La hora y el debate", "A2→B2"),
    ("Pág. 8", "Ejercicios y respuestas", "todos"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "LA PALABRA DE LA SEMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "« el debate »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "dos o más personas discuten en público, con turnos y preguntas.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "“Debate”: two or more people discuss in public.", 18, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
p.rect(ix, iy, iw, 320, fill=BOX)
illus_voto(p, ix + 240, iy + 30, s=1.7)
caption(p, ix, iy + 320, iw,
        "La urna y el sobre: votar por correo o en persona, el 29 de noviembre España decide. En la página 5, cómo pedir el voto por correo hasta el jueves 19, y en la página 6, cómo leer un debate sin perderse. (Ilustración de la redacción, no una fotografía)",
        "Ilustración: La Lucerna")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-otono")
f2.head("UNA SEMANA, TRES ESCENARIOS", 23)
f2.para("El lunes, el flamenco en la calle; el viernes, el fútbol en casa; y entre medias, la campaña en la tele. Esta semana España vive a la vez su música, su debate y su Liga.", 22.5)
f2.para("Nuestro consejo para esta semana: escucha el debate entero, no solo el titular. En la página 6 te enseñamos cómo leer un debate sin perderse.", 22.5)
f2.end_report()
# col 3 BREVES
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX)
p.text(bx + 22, 1914, "BREVES　News in brief", 24, "sans", True, OLIVE)
brefs = [
    ("EL DEBATE", "El viernes 13, debate de portavoces en laSexta, 21:30. (Página 6)"),
    ("LA LIGA", "Viernes 20: Athletic–Espanyol abre la jornada 13. (Página 4)"),
    ("EL FLAMENCO", "El lunes 16 es el Día Internacional del Flamenco. (Página 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "QUIZ RELÁMPAGO　Lightning quiz", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Read the front page and choose　Answers on page 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "Multiple choice", "C", "The election is on 29 November",
      "Las elecciones generales son el... A. 16 de noviembre · B. 13 de noviembre · C. 29 de noviembre", size=21)
qf.ex("A2", "Multiple choice", "B", "The campaign lasts 15 days",
      "La campaña electoral dura... A. una semana · B. 15 días · C. un mes", size=21)
qf.ex("A2", "Multiple choice", "A", "Postal votes must be requested by the 19th at the latest",
      "El voto por correo se pide hasta el... A. jueves 19 · B. lunes 16 · C. domingo 29", size=21)
qf.ex("A2", "Multiple choice", "B", "International Flamenco Day, 16 November",
      "El Día Internacional del Flamenco es el... A. domingo 22 · B. lunes 16 · C. viernes 20", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-portada.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VIDA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIDA　Life", "La Lucerna", "NIVEL A2　La semana, día a día　The week, day by day")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("La semana, día a día: del lunes 16 al domingo 22", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: A2")
f.para("El lunes 16 de noviembre empieza la primera semana entera de campaña: los partidos recorren España, la tele prepara los debates y los votantes escuchan los programas.")
f.para("El lunes es también el Día Internacional del Flamenco: en 2010, la UNESCO declaró el flamenco Patrimonio Cultural Inmaterial de la Humanidad (página 3). Y ese mismo lunes, el PP propone un cara a cara entre Sánchez y Feijóo: los dos partidos aceptan la cita, pero no hay hora publicada.")
f.para("El jueves 19 es un día clave: termina el plazo para pedir el voto por correo. Quien quiera votar desde casa tiene que pedirlo en Correos o por internet hasta ese día (página 5).")
f.para("Y el viernes 20 vuelve el fútbol: la jornada 13 de Liga abre con el Athletic–Espanyol a las 21:00. El sábado, el derbi Sevilla–Betis; el domingo, el Barça–Villarreal y Santa Cecilia, la patrona de los músicos (página 4).")
f.box("EL CALENDARIO　This week", [
    ("Lunes 16 — Día Internacional del Flamenco; el PP propone el cara a cara Sánchez–Feijóo (Monday: International Flamenco Day; the PP proposes the Sánchez–Feijóo face-off)", "serif", False, INK, 21, 1.36),
    ("Martes 17 — la campaña recorre España: mítines y entrevistas en la tele (Tuesday: the campaign travels across Spain)", "serif", False, INK, 21, 1.36),
    ("Miércoles 18 — debate sobre vivienda en la Cadena SER: Isabel Rodríguez (PSOE) y Juan Bravo (PP) (Wednesday: the housing debate on the radio, PSOE v PP)", "serif", False, INK, 21, 1.36),
    ("Jueves 19 — último día para pedir el voto por correo (Thursday: last day to apply for a postal vote)", "serif", False, INK, 21, 1.36),
    ("Viernes 20 — vuelve la Liga: Athletic–Espanyol, 21:00 (Friday evening: the League is back)", "serif", False, INK, 21, 1.36),
    ("Sábado 21 — derbi Sevilla–Betis, 18:30; Real Madrid–Celta, 21:00 (Saturday: the Seville derby)", "serif", False, INK, 21, 1.36),
    ("Domingo 22 — Barça–Villarreal, 14:00; Santa Cecilia, patrona de la música (Sunday: Barça v Villarreal; St Cecilia's Day)", "serif", False, INK, 21, 1.36),
])
f.head("DECIR LA HORA", 25)
f.para("En español, la hora se dice así: «Son las nueve» para las 9:00, pero «Es la una» para la 1:00. Para la hora exacta: «Son las 20:45» o «las nueve menos cuarto». Y para citar un partido: «a las 21:00», nunca «en las 21:00».", 23)
f.gloss("el debate = debate · el mitin = campaign rally · el cartel = poster · el escaño = seat in parliament.")
f.end_report()

# col 3: facts + ¿Y tú? (sequential, measured)
ix = COLX[3]
facts = ["La campaña dura 15 días: del viernes 13 al viernes 27 de noviembre.",
         "El voto por correo se pide hasta el jueves 19: en Correos o por internet.",
         "Del martes 24 al sábado 28 no se publican encuestas: así lo manda la ley."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "¿SABÍAS QUE…?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Qué harías el lunes 16: ves el flamenco, sigues la campaña o ves el fútbol? ¿Qué te gusta más: un debate o un derbi? Escribe dos frases en español y envíalas a la redacción: las mejores salen en la página 7, «Cartas de los lectores»."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("What will you do on Monday 16 November: watch flamenco, follow the campaign or watch football? What do you like more: a debate or a derby? Write two sentences in Spanish and send them to the editors.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　Your turn", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "What will you do on Monday 16 November: watch flamenco, follow the campaign or watch football? What do you like more: a debate or a derby? Write two sentences in Spanish and send them to the editors.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Decir la hora wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "LOS DÍAS DE LA SEMANA　Saying the date", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "lunes 16 – domingo 22 de noviembre　Monday 16 to Sunday 22 November", 20, "sans", False, GREY, anchor="end")
lx = MX
ly = dy + 58
for d, t in [
    ("lunes 16", "el lunes 16 — Día del Flamenco"),
    ("martes 17", "el martes 17 — la campaña en la calle"),
    ("miércoles 18", "el miércoles 18 — debate de vivienda en la radio"),
    ("jueves 19", "el jueves 19 — último día del voto por correo"),
]:
    p.text(lx, ly + 24, d, 24, "serif", True, OLIVE)
    p.text(lx + 240, ly + 24, t, 21, "sans", False, GREY)
    ly += 36
ly = dy + 58
rx = MX + 910
for d, t in [
    ("viernes 20", "el viernes 20 — vuelve la Liga, 21:00"),
    ("sábado 21", "el sábado 21 — derbi Sevilla–Betis, 18:30"),
    ("domingo 22", "el domingo 22 — Barça–Villarreal, 14:00"),
]:
    p.text(rx, ly + 24, d, 24, "serif", True, OLIVE)
    p.text(rx + 240, ly + 24, t, 21, "sans", False, GREY)
    ly += 36
p.para(lx, dy + 226, "Ojo: para la hora, «es la una» en singular y «son las dos» en plural — y el partido se juega «a las 21:00», con la preposición a.", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　Page 2 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8　Levels are mixed — find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　LAS FECHAS", 25)
e.bridge("Complete the sentences with the right date form.")
e.ex("A2", "Sentence completion", "16", "Monday 16 November",
     "El Día del Flamenco es el lunes ___ de noviembre.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "19", "Thursday 19 November",
     "El voto por correo se pide hasta el jueves ___ de noviembre.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "29", "The election is on 29 November",
     "Las elecciones generales son el ___ de noviembre.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "22", "Sunday 22 November",
     "Santa Cecilia es el domingo ___ de noviembre.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "noviembre", "Months are lower case",
     "El lunes 16 de ___ es el Día del Flamenco.", instr="Fill in", size=20, gap=8)
e.head("B　EL PRESENTE", 25)
e.bridge("Complete the verbs in the present tense.")
e.ex("A2", "Sentence completion", "empieza", "la campaña → empieza",
     "La campaña ___ el viernes 13.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "dura", "la campaña → dura",
     "La campaña ___ 15 días.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "vuelve", "la Liga → vuelve",
     "La Liga ___ el viernes 20.", instr="Fill in", size=20, gap=8)
e.ex("B1", "Sentence completion", "recorren", "los partidos → recorren",
     "Los partidos ___ España en campaña.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "llega", "la documentación → llega",
     "La documentación del voto por correo ___ desde el lunes 9.", instr="Fill in", size=20, gap=8)
e.head("C　COMPRENSIÓN", 25)
e.bridge("Read the article and choose the answer.")
e.ex("A2", "Multiple choice", "B", "International Flamenco Day, Monday 16 November",
     "El Día del Flamenco es... A. el domingo 22 · B. el lunes 16 · C. el viernes 20", size=20, gap=8)
e.ex("A2", "Multiple choice", "A", "Postal votes must be requested by the 19th at the latest",
     "El voto por correo se pide hasta... A. el jueves 19 · B. el lunes 16 · C. el domingo 29", size=20, gap=8)
e.ex("A2", "Multiple choice", "C", "The League is back on Friday 20 November",
     "La Liga vuelve el... A. lunes 16 · B. jueves 19 · C. viernes 20", size=20, gap=8)
e.ex("B1", "Multiple choice", "B", "No polls published 24–28 November",
     "Del 24 al 28 de noviembre no se publican... A. debates · B. encuestas · C. partidos", size=20, gap=8)
e.head("D　LAS PALABRAS", 25)
e.match_set("A2", "Vocabulary matching",
            ["el debate", "el mitin", "el cartel", "el escaño"],
            ["un asiento en el Parlamento",
             "una reunión de campaña con discursos",
             "una discusión pública con turnos",
             "un papel grande con un mensaje en la calle"],
            ["c", "b", "d", "a"],
            ["debate = debate c", "mitin = rally b", "cartel = poster d", "escaño = seat in parliament a"],
            instr="Match word to definition")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vida.svg")
print("P2 saved, exercises so far:", len(REG))
