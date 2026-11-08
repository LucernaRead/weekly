# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — fresh text, week 9–15 Nov 2026. Structure/counts mirror W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · PORTADA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3　TERCERA EDICIÓN", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "CADA SEMANA EN ESPAÑOL　ELKE WEEK　HET SPAANS VAN SPANJE", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "SEMANA DEL 9 AL 15 DE NOVIEMBRE DE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "La Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SPAANS WEEKBLAD　VOL.3　LA HUELGA　LA CAMPAÑA　LA ROJA", 36, "serif", True, OLIVE, anchor="middle", spacing=8)
p.text(975, 372, "TEKSTEN IN HET SPAANS　UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "¡EL VIERNES 13 EMPIEZA LA CAMPAÑA!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Faltan 20 días para el 29-N: el miércoles 11, huelga general de 24 horas.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "DE CAMPAGNE BEGINT VRIJDAG 13　STAKING WOENSDAG 11", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "Hoofdverhaal　zie pagina 2 en 6", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "LA NOTICIA　Het nieuws", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Del 11-N a la campaña: España vota en 20 días", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "De la redacción de La Lucerna　Nivel de lectura: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("España entra en su semana más intensa antes de las elecciones. El miércoles 11 hay huelga general y el viernes 13, a las 00:00, empieza la campaña electoral.")
f.para("El domingo 29 de noviembre, España vota en elecciones generales. La campaña dura quince días: del viernes 13 al viernes 27 de noviembre. El sábado 28 es la jornada de reflexión, sin actos de campaña.")
f.para("¿Por qué esta semana decide tanto? Porque la vivienda sigue siendo el primer problema del país: según el Barómetro de Vivienda del CIS, el 91,4 % pide más vivienda pública (página 6).")
f.para("Y el que quiera votar por correo tiene que pedirlo antes del jueves 19: la documentación llega a casa desde el lunes 9 (página 2).")
f.para("El domingo 15, la selección cierra la fase de grupos de la Liga de Naciones contra Inglaterra, en el Metropolitano, a las 20:45.")
f.para("Esta es la tercera edición de La Lucerna en español: cada semana, la España real contigo. ¡Bienvenidos!")
f.expl("la huelga general = de algemene staking · la campaña electoral = de verkiezingscampagne · el voto por correo = stemmen per post · la jornada de reflexión = de dag van bezinning.")
f.box("LA SEMANA EN CIFRAS　De cijfers", tsize=20, paras=[
    ("20 — días faltan el lunes 9 para las elecciones del domingo 29 (nog 20 dagen tot de verkiezingen)", "serif", False, INK, 20.5, 1.35),
    ("24 — horas dura la huelga general del miércoles 11 de noviembre (de staking op 11 november duurt 24 uur)", "serif", False, INK, 20.5, 1.35),
    ("91,4 — % que pide más vivienda pública, según el CIS de octubre (CIS-huisvestingsbarometer, oktober)", "serif", False, INK, 20.5, 1.35),
])
f.head("AHORA TÚ　Nu jij", 25)
f.ex("A2", "Zinnen aanvullen", "13", "De campagne begint vrijdag 13 november",
     "La campaña electoral empieza el viernes ___ de noviembre.", size=20.5)
f.ex("A2", "Zinnen aanvullen", "11", "De algemene staking is woensdag 11 november",
     "La huelga general es el miércoles ___ de noviembre.", size=20.5)
f.ex("A2", "Zinnen aanvullen", "29", "De verkiezingen zijn zondag 29 november",
     "España vota en elecciones generales el domingo ___ de noviembre.", size=20.5)
f.ex("A2", "Zinnen aanvullen", "19", "Stemmen per post moet vóór de 19e worden aangevraagd",
     "El voto por correo se pide antes del jueves ___ de noviembre.", size=20.5)
f.ex("B1", "Zinnen aanvullen", "20:45", "Spanje–Engeland, zondag om 20:45",
     "El España–Inglaterra del domingo se juega a las ___.", size=20.5)
f.ex("B1", "Zinnen aanvullen", "15", "De campagne duurt 15 dagen",
     "La campaña electoral dura ___ días.", size=20.5)
f.end_report()

# ---- claves de la semana (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "CINCO", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "CLAVES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Vijf sleutels　Para entender la semana", 19, "sans", False, GREY)
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
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE)
    byy += 92
p.text(gx + 22, byy + 16, "Cinco claves, sin números", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "inventados: todo está explicado", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 68, "en esta edición.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 102, "Vijf sleutels — geen verzonnen cijfers.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "EN ESTA EDICIÓN　In dit nummer", 24, "sans", True, OLIVE)
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
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "LA PALABRA DE LA SEMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "« la huelga general »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "todos paran a la vez, un día entero.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "«La huelga general»: iedereen staakt één dag.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
p.rect(ix, iy, iw, 320, fill=BOX)
illus_voto(p, ix + 240, iy + 30, s=1.7)
caption(p, ix, iy + 320, iw,
        "La urna y el sobre: votar por correo o en persona, el 29 de noviembre España decide. En la página 2, cómo pedir el voto por correo antes del jueves 19, y en la página 6, los datos del CIS sobre la vivienda. (Ilustración de la redacción, no una fotografía)",
        "Ilustración: La Lucerna")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-otono")
f2.head("UNA SEMANA, DOS ESPAÑAS", 25)
f2.para("El miércoles, la calle en huelga; el viernes, la campaña en marcha. El domingo, el Metropolitano con la Roja. Entre medias, San Martín y su veranillo: esta semana España vive a la vez su protesta y su fiesta.", 22.5)
f2.para("Nuestro consejo para esta semana: lee el programa, no solo el titular. En la página 6 te enseñamos cómo.", 22.5)
f2.end_report()
# col 3 BREVES
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX)
p.text(bx + 22, 1914, "BREVES　Kort nieuws", 24, "sans", True, OLIVE)
brefs = [
    ("LA HUELGA", "El miércoles 11, huelga de 24 horas en todo el país. (Página 2)"),
    ("LA ROJA", "Jueves: Chequia–España. Domingo: España–Inglaterra. (Página 4)"),
    ("SAN MARTÍN", "El miércoles 11 es San Martín: castañas y veranillo. (Página 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "QUIZ RELÁMPAGO　Bliksemquiz", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lees de voorpagina en kies　Antwoorden op pagina 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "Meerkeuze", "C", "De verkiezingen zijn op 29 november",
      "Las elecciones generales son el... A. 11 de noviembre · B. 13 de noviembre · C. 29 de noviembre", size=21)
qf.ex("A2", "Meerkeuze", "B", "De staking duurt 24 uur",
      "La huelga general del miércoles dura... A. una hora · B. 24 horas · C. una semana", size=21)
qf.ex("A2", "Meerkeuze", "A", "De campagne begint op 13 november",
      "La campaña electoral empieza el... A. viernes 13 · B. lunes 9 · C. domingo 15", size=21)
qf.ex("A2", "Meerkeuze", "B", "Spanje–Engeland zondag om 20:45",
      "El España–Inglaterra se juega el domingo a las... A. 15:30 · B. 20:45 · C. 18:30", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-portada.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VIDA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIDA　Leven", "La Lucerna", "NIVEL A2　El miércoles 11, huelga general　Algemene staking op woensdag 11 november")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("El miércoles 11: huelga general de 24 horas", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: A2")
f.para("El miércoles 11 de noviembre hay huelga general en toda España: un paro de 24 horas, convocado por los sindicatos.")
f.para("La convocan Comisiones Obreras (CCOO) y la Unión General de Trabajadores (UGT), junto con la Confederación General del Trabajo (CGT), la Confederación Nacional del Trabajo (CNT) y la Confederación de Sindicatos de Inquilinas, entre otras organizaciones. El lema es «Salarios, vivienda y precios».")
f.para("¿Qué piden? Subir los salarios, bajar el precio de la vivienda, regular el alquiler y frenar la subida de los precios. La huelga llega dos días antes de que empiece la campaña electoral, el viernes 13.")
f.para("En un día de huelga, no todo se para igual: hay servicios mínimos en el transporte y en la sanidad. Los servicios mínimos de esta huelga se anuncian antes del miércoles: consulta los avisos de tu ciudad y de tu empresa.")
f.box("EL CALENDARIO　De kalender", [
    ("Lunes 9 — la selección se concentra en Las Rozas; la documentación del voto por correo empieza a llegar a casa (maandag: de selectie komt samen; de stembiljetten worden verstuurd)", "serif", False, INK, 21, 1.36),
    ("Martes 10 — último día de calma antes de la huelga: los sindicatos ultiman los servicios mínimos (dinsdag: laatste voorbereidingen voor de staking)", "serif", False, INK, 21, 1.36),
    ("Miércoles 11 — huelga general de 24 horas; San Martín, castañas y vino nuevo (woensdag: algemene staking; Sint-Maarten)", "serif", False, INK, 21, 1.36),
    ("Jueves 12 — Liga de Naciones: Chequia–España, 20:45, en Praga (donderdag Nations League: Tsjechië–Spanje)", "serif", False, INK, 21, 1.36),
    ("Viernes 13 — a las 00:00 empieza la campaña electoral del 29-N (vrijdag: de campagne begint om middernacht)", "serif", False, INK, 21, 1.36),
    ("Sábado 14 — final de la Copa Federación en Sestao, 19:00 (zaterdag: finale Copa Federación in Sestao)", "serif", False, INK, 21, 1.36),
    ("Domingo 15 — Liga de Naciones: España–Inglaterra, 20:45, en el Metropolitano (zondag Nations League: Spanje–Engeland)", "serif", False, INK, 21, 1.36),
])
f.head("DECIR LA FECHA", 25)
f.para("En español, la fecha se dice así: «el miércoles 11 de noviembre». Primero el día de la semana, luego el número y luego el mes. Los días y los meses van en minúscula: miércoles, noviembre. Y ojo: el primero del mes no es «el primero», es «el uno»: el 1 de noviembre.", 23)
f.gloss("la huelga = de staking · el sindicato = de vakbond · el salario = het loon · el alquiler = de huur · los servicios mínimos = de minimale dienstverlening.")
f.end_report()

# col 3: facts + ¿Y tú? (sequential, measured)
ix = COLX[3]
facts = ["La huelga del miércoles 11 dura 24 horas y llega a todo el país.",
         "La convocan CCOO, UGT, CGT, CNT y los sindicatos de inquilinas.",
         "El lema es «Salarios, vivienda y precios»: tres palabras, tres problemas."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "¿SABÍAS QUE…?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Qué harías el miércoles 11: vas a la huelga, trabajas o te quedas en casa? ¿Qué te preocupa más: el salario, la vivienda o los precios? Escribe dos frases en español y envíalas a la redacción: las mejores salen en la página 7, «Cartas de los lectores»."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Wat doe jij op woensdag 11 november: staken, werken of thuisblijven? Waar maak jij je het meest zorgen over: lonen, huisvesting of prijzen? Schrijf twee zinnen in het Spaans en stuur ze naar de redactie.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　En jij?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Wat doe jij op woensdag 11 november: staken, werken of thuisblijven? Waar maak jij je het meest zorgen over: lonen, huisvesting of prijzen? Schrijf twee zinnen in het Spaans en stuur ze naar de redactie.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Decir la fecha wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "LOS DÍAS DE LA SEMANA　Zo zeg je de datum", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "lunes 9 – domingo 15 de noviembre　van maandag 9 tot zondag 15 november", 20, "sans", False, GREY, anchor="end")
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
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　Oefeningen van pagina 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　Niveaus door elkaar — zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　LAS FECHAS", 25)
e.expl("Vul de zinnen aan met de juiste datumvorm.")
e.ex("A2", "Zinnen aanvullen", "11", "woensdag 11 november",
     "La huelga general es el miércoles ___ de noviembre.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "15", "zondag 15 november",
     "El España–Inglaterra se juega el domingo ___ de noviembre.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "29", "De verkiezingen zijn op 29 november",
     "Las elecciones generales son el ___ de noviembre.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "uno", "De 1e zeg je el uno",
     "El Día de Todos los Santos fue el ___ de noviembre.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "noviembre", "Maanden met kleine letters",
     "El miércoles 11 de ___ hay huelga general.", instr="Vul in", size=20, gap=8)
e.head("B　EL PRESENTE", 25)
e.expl("Vul de werkwoorden in de tegenwoordige tijd in.")
e.ex("A2", "Zinnen aanvullen", "piden", "los sindicatos → piden",
     "Los sindicatos ___ subir los salarios.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "dura", "la huelga → dura",
     "La huelga ___ 24 horas.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "empieza", "la campaña → empieza",
     "La campaña ___ el viernes 13.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "convocan", "CCOO y UGT → convocan",
     "CCOO y UGT ___ la huelga general.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "llega", "la documentación → llega",
     "La documentación del voto por correo ___ desde el lunes 9.", instr="Vul in", size=20, gap=8)
e.head("C　COMPRENSIÓN", 25)
e.expl("Lees het artikel op pagina 2 en kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "De algemene staking is woensdag 11 november",
     "¿Cuándo es la huelga general? A. el lunes 9 · B. el miércoles 11 · C. el viernes 13", size=20, gap=8)
e.ex("A2", "Meerkeuze", "A", "De leus van de staking: lonen, huisvesting, prijzen",
     "El lema de la huelga es... A. «Salarios, vivienda y precios» · B. «Fútbol y fiesta» · C. «Cine y series»", size=20, gap=8)
e.ex("A2", "Meerkeuze", "C", "De campagne begint twee dagen na de staking",
     "La campaña empieza... A. antes de la huelga · B. el mismo día · C. dos días después de la huelga", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Op de stakingsdag is er minimale dienstverlening",
     "En un día de huelga hay... A. fiesta total · B. servicios mínimos · C. vacaciones", size=20, gap=8)
e.head("D　LAS PALABRAS", 25)
e.match_set("A2", "Woorden combineren",
            ["la huelga", "el sindicato", "el salario", "el alquiler"],
            ["lo que se paga por trabajar",
             "una organización de trabajadores",
             "un paro de todos los trabajadores",
             "lo que se paga por vivir en un piso"],
            ["c", "b", "a", "d"],
            ["huelga=staking c", "sindicato=vakbond b", "salario=loon a", "alquiler=huur d"],
            instr="Combineer")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vida.svg")
print("P2 saved, exercises so far:", len(REG))
