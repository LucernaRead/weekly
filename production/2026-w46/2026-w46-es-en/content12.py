# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — fresh text, week 9–15 Nov 2026. Structure/counts mirror W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · PORTADA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3 · TERCERA EDICIÓN", 23, "sans", True, OLIVE)
p.text(975, 92, "CADA SEMANA EN ESPAÑOL · REAL SPANISH, EVERY WEEK", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "SEMANA DEL 9 AL 15 DE NOVIEMBRE DE 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "La Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SPANISH WEEKLY · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA", 46, "serif", True, INK, anchor="middle")
p.text(975, 372, "TEXT IN SPANISH · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 19.5, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "¡EL VIERNES 13 EMPIEZA LA CAMPAÑA!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Faltan 20 días para el 29-N: el miércoles 11, huelga general de 24 horas.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "THE CAMPAIGN STARTS FRI 13 · STRIKE WED 11", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "TOP STORY · SEE PAGES 2 AND 6", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "LA NOTICIA · Top story", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Del 11-N a la campaña: España vota en 20 días", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "De la redacción de La Lucerna · Nivel de lectura: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("España entra en su semana más intensa antes de las elecciones. El miércoles 11 hay huelga general y el viernes 13, a las 00:00, empieza la campaña electoral.")
f.para("El domingo 29 de noviembre, España vota en elecciones generales. La campaña dura quince días: del viernes 13 al viernes 27 de noviembre. El sábado 28 es la jornada de reflexión, sin actos de campaña.")
f.para("¿Por qué esta semana decide tanto? Porque la vivienda sigue siendo el primer problema del país: según el Barómetro de Vivienda del CIS, el 91,4 % pide más vivienda pública (página 6).")
f.para("Y el que quiera votar por correo tiene que pedirlo antes del jueves 19: la documentación llega a casa desde el lunes 9 (página 2).")
f.para("El domingo 15, la selección cierra la fase de grupos de la Liga de Naciones contra Inglaterra, en el Metropolitano, a las 20:45.")
f.para("Esta es la tercera edición de La Lucerna en español: cada semana, la España real contigo. ¡Bienvenidos!")
f.bridge("Note | la huelga general = general strike · la campaña electoral = election campaign · el voto por correo = postal vote · la jornada de reflexión = reflection day.")
f.box("LA SEMANA EN CIFRAS · Numbers", [
    ("20 — días faltan el lunes 9 para las elecciones del domingo 29 (20 days to the election)", "serif", False, INK, 20.5, 1.35),
    ("24 — horas dura la huelga general del miércoles 11 de noviembre (the 11 November strike lasts 24 hours)", "serif", False, INK, 20.5, 1.35),
    ("91,4 — % que pide más vivienda pública, según el CIS de octubre (CIS housing barometer, October)", "serif", False, INK, 20.5, 1.35),
])
f.head("AHORA TÚ · Now you try", 25)
f.ex("A2", "Sentence completion", "13", "The campaign starts on Friday 13 November",
     "La campaña electoral empieza el viernes ___ de noviembre.", size=20.5)
f.ex("A2", "Sentence completion", "11", "The general strike is on Wednesday 11 November",
     "La huelga general es el miércoles ___ de noviembre.", size=20.5)
f.ex("A2", "Sentence completion", "29", "The election is on Sunday 29 November",
     "España vota en elecciones generales el domingo ___ de noviembre.", size=20.5)
f.ex("A2", "Sentence completion", "19", "Postal votes must be requested before the 19th",
     "El voto por correo se pide antes del jueves ___ de noviembre.", size=20.5)
f.ex("B1", "Sentence completion", "20:45", "Spain–England kicks off Sunday at 20:45",
     "El España–Inglaterra del domingo se juega a las ___.", size=20.5)
f.ex("B1", "Sentence completion", "15", "The campaign lasts 15 days",
     "La campaña electoral dura ___ días.", size=20.5)
f.end_report()

# ---- claves de la semana (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "CINCO", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "CLAVES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Five keys · Para entender la semana", 19, "sans", False, GREY)
gt = [
    ("La huelga del 11-N", 250),
    ("La campaña del 13", 226),
    ("El voto por correo", 196),
    ("La Roja: Praga e Inglaterra", 158),
    ("San Martín y el veranillo", 122),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE if i == 0 else GOLD)
    byy += 92
p.text(gx + 22, byy + 16, "Cinco claves, sin números", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "inventados: todo está explicado", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 68, "en esta edición.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 102, "Five keys — no invented numbers.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "EN ESTA EDICIÓN · In this issue", 24, "sans", True, OLIVE)
som = [
    ("Pág. 2", "El miércoles 11, huelga", "A2"),
    ("Pág. 3", "San Martín y el otoño", "A2→B1"),
    ("Pág. 4", "Praga y el domingo", "B1"),
    ("Pág. 5", "Votar desde casa", "B1"),
    ("Pág. 6", "La vivienda decide", "B2"),
    ("Pág. 7", "Fechas y promesas", "A2→B2"),
    ("Pág. 8", "Ejercicios y respuestas", "todos"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "LA PALABRA DE LA SEMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "« la huelga general » : todos paran a la vez, un día entero.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "“la huelga general”: all workers stop work for 24 hours.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
p.rect(ix, iy, iw, 320, fill=BOX, stroke=LINE, sw=1.4)
illus_voto(p, ix + 240, iy + 30, s=1.7)
caption(p, ix, iy + 320, iw,
        "La urna y el sobre: votar por correo o en persona, el 29 de noviembre España decide. En la página 2, cómo pedir el voto por correo antes del jueves 19, y en la página 6, los datos del CIS sobre la vivienda. (Ilustración de la redacción, no una fotografía)",
        "Ilustración: La Lucerna")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-otono")
f2.head("UNA SEMANA, DOS ESPAÑAS", 25)
f2.para("El miércoles, la calle en huelga; el viernes, la campaña en marcha. El domingo, el Metropolitano con la Roja. Entre medias, San Martín y su veranillo: esta semana España vive a la vez su protesta y su fiesta.", 22.5)
f2.para("Nuestro consejo para esta semana: lee el programa, no solo el titular. En la página 6 te enseñamos cómo.", 22.5)
f2.end_report()
# col 3 BREVES
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "BREVES · News in brief", 24, "sans", True, OLIVE)
brefs = [
    ("LA HUELGA", "El miércoles 11, huelga de 24 horas en todo el país. (Página 2)"),
    ("LA ROJA", "Jueves: Chequia–España. Domingo: España–Inglaterra. (Página 4)"),
    ("SAN MARTÍN", "El miércoles 11 es San Martín: castañas y veranillo. (Página 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "QUIZ RELÁMPAGO · Lightning quiz", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Read the front page and choose · Answers on page 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "Multiple choice", "C", "The election is on 29 November",
      "Las elecciones generales son el... A. 11 de noviembre · B. 13 de noviembre · C. 29 de noviembre", size=21)
qf.ex("A2", "Multiple choice", "B", "The strike lasts 24 hours",
      "La huelga general del miércoles dura... A. una hora · B. 24 horas · C. una semana", size=21)
qf.ex("A2", "Multiple choice", "A", "The campaign starts on 13 November",
      "La campaña electoral empieza el... A. viernes 13 · B. lunes 9 · C. domingo 15", size=21)
qf.ex("A2", "Multiple choice", "B", "Spain–England, Sunday 20:45",
      "El España–Inglaterra se juega el domingo a las... A. 15:30 · B. 20:45 · C. 18:30", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-portada.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VIDA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIDA · Life", "La Lucerna", "NIVEL A2 · El miércoles 11, huelga general · General strike, Wednesday 11 November")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("El miércoles 11: huelga general de 24 horas", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: A2")
f.para("El miércoles 11 de noviembre hay huelga general en toda España: un paro de 24 horas, convocado por los sindicatos.")
f.para("La convocan Comisiones Obreras (CCOO) y la Unión General de Trabajadores (UGT), junto con la Confederación General del Trabajo (CGT), la Confederación Nacional del Trabajo (CNT) y la Confederación de Sindicatos de Inquilinas, entre otras organizaciones. El lema es «Salarios, vivienda y precios».")
f.para("¿Qué piden? Subir los salarios, bajar el precio de la vivienda, regular el alquiler y frenar la subida de los precios. La huelga llega dos días antes de que empiece la campaña electoral, el viernes 13.")
f.para("En un día de huelga, no todo se para igual: hay servicios mínimos en el transporte y en la sanidad. Los servicios mínimos de esta huelga se anuncian antes del miércoles: consulta los avisos de tu ciudad y de tu empresa.")
f.box("EL CALENDARIO · This week", [
    ("Lunes 9 — la selección se concentra en Las Rozas; la documentación del voto por correo empieza a llegar a casa (national team gathers; postal-vote papers start arriving)", "serif", False, INK, 21, 1.36),
    ("Martes 10 — último día de calma antes de la huelga: los sindicatos ultiman los servicios mínimos (last preparations before the strike)", "serif", False, INK, 21, 1.36),
    ("Miércoles 11 — huelga general de 24 horas; San Martín, castañas y vino nuevo (general strike; St Martin's Day)", "serif", False, INK, 21, 1.36),
    ("Jueves 12 — Liga de Naciones: Chequia–España, 20:45, en Praga (Nations League: Czechia v Spain)", "serif", False, INK, 21, 1.36),
    ("Viernes 13 — a las 00:00 empieza la campaña electoral del 29-N (the campaign starts at midnight)", "serif", False, INK, 21, 1.36),
    ("Sábado 14 — final de la Copa Federación en Sestao, 19:00 (Federation Cup final in Sestao)", "serif", False, INK, 21, 1.36),
    ("Domingo 15 — Liga de Naciones: España–Inglaterra, 20:45, en el Metropolitano (Nations League: Spain v England)", "serif", False, INK, 21, 1.36),
])
f.head("DECIR LA FECHA", 25)
f.para("En español, la fecha se dice así: «el miércoles 11 de noviembre». Primero el día de la semana, luego el número y luego el mes. Los días y los meses van en minúscula: miércoles, noviembre. Y ojo: el primero del mes no es «el primero», es «el uno»: el 1 de noviembre.", 23)
f.gloss("la huelga = strike · el sindicato = trade union · el salario = wage · el alquiler = rent · los servicios mínimos = minimum services.")
f.end_report()

# col 3: facts + ¿Y tú? (sequential, measured)
ix = COLX[3]
facts = ["La huelga del miércoles 11 dura 24 horas y llega a todo el país.",
         "La convocan CCOO, UGT, CGT, CNT y los sindicatos de inquilinas.",
         "El lema es «Salarios, vivienda y precios»: tres palabras, tres problemas."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "¿SABÍAS QUE…?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Qué harías el miércoles 11: vas a la huelga, trabajas o te quedas en casa? ¿Qué te preocupa más: el salario, la vivienda o los precios? Escribe dos frases en español y envíalas a la redacción: las mejores salen en la página 7, «Cartas de los lectores»."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("What will you do on Wednesday 11 November: strike, work, or stay at home? What worries you most: wages, housing, or prices? Write two sentences in Spanish and send them to the editors.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ? · Your turn", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "What will you do on Wednesday 11 November: strike, work, or stay at home? What worries you most: wages, housing, or prices? Write two sentences in Spanish and send them to the editors.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Decir la fecha wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "LOS DÍAS DE LA SEMANA · Saying the date", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "lunes 9 – domingo 15 de noviembre · Monday 9 to Sunday 15 November", 20, "sans", False, GREY, anchor="end")
lx = MX
ly = dy + 58
for d, t in [
    ("lunes 9", "el lunes 9 — la Roja se concentra en Las Rozas"),
    ("martes 10", "el martes 10 — antes de la huelga"),
    ("miércoles 11", "el miércoles 11 — huelga general, 24 horas"),
    ("jueves 12", "el jueves 12 — Chequia–España, 20:45"),
]:
    p.text(lx, ly + 24, d, 24, "serif", True, OLIVE)
    p.text(lx + 240, ly + 24, t, 21, "sans", False, GREY)
    ly += 36
ly = dy + 58
rx = MX + 910
for d, t in [
    ("viernes 13", "el viernes 13 — empieza la campaña, 00:00"),
    ("sábado 14", "el sábado 14 — Copa Federación, 19:00"),
    ("domingo 15", "el domingo 15 — España–Inglaterra, 20:45"),
]:
    p.text(rx, ly + 24, d, 24, "serif", True, OLIVE)
    p.text(rx + 240, ly + 24, t, 21, "sans", False, GREY)
    ly += 36
p.para(lx, dy + 226, "Ojo: los días de la semana y los meses van en minúscula en español — miércoles, noviembre — y el 1 del mes es «el uno», no «el primero».", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · Page 2 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels are mixed — find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · LAS FECHAS", 25)
e.bridge("Complete the sentences with the right date form.")
e.ex("A2", "Sentence completion", "11", "Wednesday 11 November",
     "La huelga general es el miércoles ___ de noviembre.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "15", "Sunday 15 November",
     "El España–Inglaterra se juega el domingo ___ de noviembre.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "29", "The election is on 29 November",
     "Las elecciones generales son el ___ de noviembre.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "uno", "The 1st is el uno",
     "El Día de Todos los Santos fue el ___ de noviembre.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "noviembre", "Months are lower case",
     "El miércoles 11 de ___ hay huelga general.", instr="Fill in", size=20, gap=8)
e.head("B · EL PRESENTE", 25)
e.bridge("Complete the verbs in the present tense.")
e.ex("A2", "Sentence completion", "piden", "los sindicatos → piden",
     "Los sindicatos ___ subir los salarios.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "dura", "la huelga → dura",
     "La huelga ___ 24 horas.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "empieza", "la campaña → empieza",
     "La campaña ___ el viernes 13.", instr="Fill in", size=20, gap=8)
e.ex("B1", "Sentence completion", "convocan", "CCOO y UGT → convocan",
     "CCOO y UGT ___ la huelga general.", instr="Fill in", size=20, gap=8)
e.ex("A2", "Sentence completion", "llega", "la documentación → llega",
     "La documentación del voto por correo ___ desde el lunes 9.", instr="Fill in", size=20, gap=8)
e.head("C · COMPRENSIÓN", 25)
e.bridge("Read the page 2 article and choose the correct answer.")
e.ex("A2", "Multiple choice", "B", "The general strike is on Wednesday 11 November",
     "¿Cuándo es la huelga general? A. el lunes 9 · B. el miércoles 11 · C. el viernes 13", size=20, gap=8)
e.ex("A2", "Multiple choice", "A", "The strike slogan: wages, housing, prices",
     "El lema de la huelga es... A. «Salarios, vivienda y precios» · B. «Fútbol y fiesta» · C. «Cine y series»", size=20, gap=8)
e.ex("A2", "Multiple choice", "C", "The campaign starts two days after the strike",
     "La campaña empieza... A. antes de la huelga · B. el mismo día · C. dos días después de la huelga", size=20, gap=8)
e.ex("B1", "Multiple choice", "B", "Minimum services run on strike day",
     "En un día de huelga hay... A. fiesta total · B. servicios mínimos · C. vacaciones", size=20, gap=8)
e.head("D · LAS PALABRAS", 25)
e.match_set("A2", "Vocabulary matching",
            ["la huelga", "el sindicato", "el salario", "el alquiler"],
            ["lo que se paga por trabajar",
             "una organización de trabajadores",
             "un paro de todos los trabajadores",
             "lo que se paga por vivir en un piso"],
            ["c", "b", "a", "d"],
            ["huelga=strike c", "sindicato=trade union b", "salario=wage a", "alquiler=rent d"],
            instr="Match word to definition")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vida.svg")
print("P2 saved, exercises so far:", len(REG))
