# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · PORTADA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1　PRIMERA EDICIÓN", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "CADA SEMANA EN ESPAÑOL　ELKE WEEK　HET SPAANS DAT DE SPANJAARDEN LEZEN", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "SEMANA DEL 19 AL 25 DE OCTUBRE DE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "La Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SPAANS WEEKBLAD　VOL.1　EL RELOJ　EL CLÁSICO　LA F1", 36, "serif", True, OLIVE, anchor="middle", spacing=8)
p.text(975, 372, "TEKSTEN IN HET SPAANS　UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 150, fill=CLOTH)
p.text(MX + 30, 524, "¡ESTE DOMINGO DORMIMOS UNA HORA MÁS… Y SE JUEGA EL CLÁSICO!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 560, "En la madrugada del domingo, el reloj se atrasa una hora: a las 03:00 serán las 02:00.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 596, "ZONDAG: EEN UUR LANGER SLAPEN", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 560, "ÉN DE CLÁSICO　ZIE PAGINA 2 EN 4", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 622
p.text(MX, hy + 26, "LA NOTICIA　Hoofdverhaal", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Este domingo: dormimos una hora más… ¡y se juega el Clásico!", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "De la redacción de La Lucerna　Nivel de lectura: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Este domingo pasa todo a la vez. Primero, en la madrugada, España cambia la hora: a las 03:00, el reloj vuelve a las 02:00. La noche tiene 25 horas y dormimos una hora más.")
f.para("Y por la noche, a las 21:00, el Camp Nou recibe el primer Clásico de la temporada: el FC Barcelona contra el Real Madrid. El Barça llega líder y sin perder un solo partido de Liga; el Madrid de José Mourinho llega a seis puntos, después de perder el derbi madrileño.")
f.para("¿Solo fútbol? No: a la misma hora, las 21:00, los coches de Fórmula 1 corren en Austin, en Estados Unidos. Fernando Alonso y Carlos Sainz llegan empatados a siete puntos. España tiene que elegir pantalla.")
f.para("La semana también trae tiempo de otoño: la DANA Adam, la primera gran tormenta mediterránea de la temporada, trajo lluvia fuerte y tormentas a la costa mediterránea y a Baleares entre el sábado y el lunes.")
f.para("Esta es la primera edición de La Lucerna en español. Cada semana leemos la España real contigo: despacio, claro y con honestidad. ¡Bienvenidos!")
f.expl("Uitleg — la madrugada = de vroege ochtend · atrasar el reloj = de klok terugzetten · empatados = gelijk in punten · la tormenta = de storm.")
f.box("LA SEMANA EN CIFRAS　In cijfers", [
    ("25 — horas tiene la noche del sábado al domingo (de nacht van zaterdag op zondag telt 25 uur)", "serif", False, INK, 20.5, 1.35),
    ("21:00 — el Clásico y la carrera de F1, a la misma hora (de Clásico en de F1-race, op hetzelfde tijdstip)", "serif", False, INK, 20.5, 1.35),
    ("9 — comunidades donde el lunes 2 de noviembre es fiesta (negen regio's waar maandag 2 november een feestdag is)", "serif", False, INK, 20.5, 1.35),
])
f.head("AHORA TÚ　Probeer het nu", 25)
f.ex("A2", "Zinnen aanvullen", "se atrasa", "el reloj se atrasa = de klok wordt teruggezet",
     "En la madrugada del domingo, el reloj ___ una hora.", size=20.5)
f.ex("A2", "Zinnen aanvullen", "25", "de nacht van 25 uur",
     "La noche del sábado al domingo tiene ___ horas.", size=20.5)
f.ex("A2", "Zinnen aanvullen", "el Clásico", "de eerste Clásico van het seizoen",
     "El domingo a las 21:00 se juega el primer ___ de la temporada: Barça – Madrid.", size=20.5)
f.ex("A2", "Zinnen aanvullen", "líder", "Barça leidt en is ongeslagen in de competitie",
     "El Barça llega ___ y sin perder en la Liga.", size=20.5)
f.ex("B1", "Zinnen aanvullen", "empatados", "empatados a siete puntos = 7 punten, gelijk",
     "Alonso y Sainz llegan ___ a siete puntos a Austin.", size=20.5)
f.ex("B1", "Zinnen aanvullen", "tormenta", "tormenta = de storm",
     "La DANA Adam es la primera gran ___ mediterránea de la temporada.", size=20.5)
f.end_report()

# ---- claves de la semana (col 3) ----
gx, gw = COLX[3], CW
gy = 620
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "CINCO", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "CLAVES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Vijf sleutelpunten　Para entender la semana", 19, "sans", False, GREY)
gt = [
    ("El cambio de hora", 250),
    ("El Clásico, el domingo", 226),
    ("La F1, ¡a la misma hora!", 196),
    ("La DANA Adam", 158),
    ("El puente partido en dos", 122),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE)
    byy += 92
p.text(gx + 22, byy + 16, "Cinco claves, sin números", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "inventados: todo está explicado", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 68, "en esta edición.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 102, "Vijf sleutelpunten, zonder verzonnen cijfers.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1344
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "EN ESTA EDICIÓN　In dit nummer", 24, "sans", True, OLIVE)
som = [
    ("Pág. 2", "El reloj y el tiempo", "A2"),
    ("Pág. 3", "Fiestas de otoño", "A2→B1"),
    ("Pág. 4", "La semana del Clásico", "B1"),
    ("Pág. 5", "Pantallas y disfraces", "B1"),
    ("Pág. 6", "Rumbo al 29N", "B2"),
    ("Pág. 7", "Frases de la semana", "A2→B2"),
    ("Pág. 8", "Ejercicios y respuestas", "todos"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1684
p.text(gx, my + 24, "LA PALABRA DE LA SEMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "« hacer puente »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "fiesta cerca del fin de semana = descanso de tres días.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "Een «puente» verbindt een feestdag met het weekend: drie dagen vrij.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1899, LINE, 1.2)
iy = 1906
ix, iw = span_x(0, 2)
image(p, "atomuhr.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "El reloj atómico NIST-F1, en Estados Unidos: uno de los relojes más exactos del mundo. La hora oficial de España también nace en relojes atómicos — y en la madrugada del domingo, todos atrasan una hora. (Página 2)",
        "Foto: NIST (EE. UU.) — dominio público")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], iy, 2300, tag="P1-otono")
f2.head("EL OTOÑO EMPIEZA DE VERDAD", 25)
f2.para("Días más cortos, la primera gran tormenta del Mediterráneo, un descanso partido en dos y un domingo con tres citas a la vez: el otoño enseña esta semana todo su programa.", 22.5)
f2.para("Su regalo para todos los lectores es una hora más de sueño. Tómala — ¡y sigue leyendo en la página 2!", 22.5)
f2.end_report()
# col 3 BREVES
bx = COLX[3]
p.rect(bx, iy, CW, 416, fill=BOX)
p.text(bx + 22, 1914, "BREVES　Kort nieuws", 24, "sans", True, OLIVE)
brefs = [
    ("LA HORA", "El domingo a las 03:00, los relojes vuelven a las 02:00. En Canarias: de las 02:00 a la 01:00. (Página 2)"),
    ("FÚTBOL", "Champions el martes: el PSG ganó 4–2 al Barça. El domingo, el Clásico a las 21:00. (Página 4)"),
    ("FIESTAS", "El lunes 2 de noviembre solo es fiesta en 9 comunidades de 17. (Página 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2344
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "QUIZ RELÁMPAGO　Bliksemquiz", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lees de voorpagina en kies het juiste antwoord　Antwoorden op pagina 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "Meerkeuze", "B", "zondagochtend gaat de klok een uur terug",
      "El reloj se atrasa en la madrugada del... A. viernes · B. domingo · C. lunes", size=21)
qf.ex("A2", "Meerkeuze", "C", "de Clásico wordt in Camp Nou gespeeld",
      "El Clásico se juega en... A. Madrid · B. Austin · C. el Camp Nou", size=21)
qf.ex("A2", "Meerkeuze", "A", "beiden hebben 7 punten",
      "Alonso y Sainz llegan a Austin... A. empatados a 7 puntos · B. con 20 puntos · C. sin puntos", size=21)
qf.ex("A2", "Meerkeuze", "B", "de nacht van zaterdag op zondag telt 25 uur",
      "La noche del sábado al domingo tiene... A. 23 horas · B. 25 horas · C. 26 horas", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-portada.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VIDA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIDA　Leven", "La Lucerna", "NIVEL A2　El cambio de hora y el tiempo　De klok en het weer")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Una hora más: la noche de las 25 horas", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: A2")
f.para("Solo pasa una vez al año: una noche con 25 horas. En la madrugada del sábado 24 al domingo 25 de octubre termina en España el horario de verano. A las 03:00, los relojes vuelven a las 02:00 — y todos dormimos una hora más.")
f.para("La hora de las 02:00 a las 03:00 existe dos veces en esta noche. Pero atención: el cambio no es igual en todo el país. En la Península, las Baleares, Ceuta y Melilla, el cambio es a las 03:00. En Canarias hay una hora menos que en la Península: allí, a las 02:00 será la 01:00.")
f.para("¿Qué relojes cambian solos? El móvil y el ordenador cambian solos. Pero el reloj del horno, el reloj viejo de la cocina y el reloj del coche necesitan tu mano. Nuestro consejo: cambia los relojes el sábado por la noche — y el domingo por la mañana todo está tranquilo.")
f.para("Este cambio es especial: es el último del calendario de cinco años que España publicó en el Boletín Oficial del Estado en 2022. ¿Es el último cambio de la historia? No es seguro: la Comisión Europea ya publicó en marzo de 2026 las fechas de cambio para 2027–2031. El sistema sigue — si la ley europea no cambia.")
f.box("LA FRASE PARA RECORDAR　Spreuk", [
    ("«En primavera se adelanta, en otoño se atrasa.» Así recuerda España la dirección del cambio: adelante en marzo, atrás en octubre — y en otoño, una hora más de sueño.", "serif", False, INK, 21.5, 1.4),
])
f.head("EL TIEMPO DESPUÉS DE ADAM", 25)
f.para("La semana empezó con mal tiempo en el Mediterráneo. La DANA Adam — la primera tormenta con nombre de la temporada — trajo su peor parte entre el domingo 18 y el lunes 19: lluvia fuerte y tormentas en la costa mediterránea y en Baleares. Los mapas de la AEMET anunciaban acumulaciones locales de 150 a 300 litros por metro cuadrado. Ojo: son cifras de pronóstico, no el agua final caída.", 23.5)
f.para("El martes y el miércoles, la cola de la tormenta todavía deja nubes y algo de lluvia en el norte y el noreste. Después, el tiempo se calma poco a poco. Y para el domingo, todos miran el pronóstico: nadie quiere lluvia a las 21:00 en el Camp Nou.", 23.5)
f.para("Las palabras del tiempo de esta semana: lluvia, tormenta y paraguas. Las practicamos ya mismo, en los ejercicios de abajo.", 23.5)
f.gloss("el horario de verano = de zomertijd · atrasar = terugzetten · adelantar = vooruitzetten · el pronóstico = de weersverwachting · la acumulación = de neerslag.")
f.end_report()

# col 3: facts + ¿Y tú? (sequential, measured)
ix = COLX[3]
facts = ["La noche del sábado al domingo tiene 25 horas: es la noche más larga del año.",
         "En Canarias hay siempre una hora menos que en la Península: cuando en Madrid son las 03:00, en Las Palmas son las 02:00.",
         "El horario de invierno dura hasta el domingo 28 de marzo de 2027."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "¿SABÍAS QUE…?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Qué haces con una hora más: duermes, lees o sales a la calle? Escribe dos frases en español y envíalas a la redacción: las mejores salen en el VOL.2 (página 7, «Cartas de los lectores»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Waar gebruik je dat extra uur voor: slapen, lezen of naar buiten? Schrijf twee zinnen in het Spaans en stuur ze naar de redactie.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　En jij?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Waar gebruik je dat extra uur voor: slapen, lezen of naar buiten? Schrijf twee zinnen in het Spaans en stuur ze naar de redactie.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Decir la hora wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "DECIR LA HORA　Zo zeg je de tijd", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Las horas de la semana　De tijden van deze week", 20, "sans", False, GREY, anchor="end")

def clock(cx, cy, r, hh, mm, label):
    p.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fdfaf0" stroke="{INK}" stroke-width="3"/>')
    import math
    for k in range(12):
        a = math.radians(k * 30)
        x1, y1 = cx + (r - 12) * math.sin(a), cy - (r - 12) * math.cos(a)
        x2, y2 = cx + r * math.sin(a), cy - r * math.cos(a)
        p.add(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{INK}" stroke-width="2.4"/>')
    ah = math.radians((hh % 12) * 30 + mm * 0.5)
    am = math.radians(mm * 6)
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.55)*math.sin(ah):.0f}" y2="{cy - (r*0.55)*math.cos(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.82)*math.sin(am):.0f}" y2="{cy - (r*0.82)*math.cos(am):.0f}" stroke="{OLIVE}" stroke-width="4" stroke-linecap="round"/>')
    p.text(cx, cy + r + 34, label, 22, "serif", True, INK, anchor="middle")

clock(240, dy + 130, 70, 1, 0, "Es la una.")
clock(560, dy + 130, 70, 2, 30, "Son las dos y media.")
clock(880, dy + 130, 70, 2, 45, "Son las tres menos cuarto.")
lx = 1090
ly = dy + 58
for line in [
    ("Es la una", "= 1:00 (alleen bij één uur: es)"),
    ("y cuarto / y media", "= +15 min / +30 min"),
    ("menos cuarto", "= kwart voor (2:45 = tres menos cuarto)"),
    ("mediodía / medianoche", "= 12:00 's middags / 0:00 's nachts"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 330, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 36
p.para(lx, ly + 22, "Ojo con el domingo: el Clásico empieza a las 21:00 — «son las nueve de la noche». La carrera de Austin empieza a la misma hora peninsular.", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　Oefeningen van pagina 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　Niveaus door elkaar — zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　¿QUÉ HORA ES?", 25)
e.expl("Kijk naar de klokken en vul de zinnen in het Spaans aan.")
e.ex("A2", "Zinnen aanvullen", "la una", "om 1:00 zeg je altijd Es la una",
     "1:00 — Es ___ en punto.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "y media", "y media = het halve uur (+30 min)",
     "2:30 — Son las dos ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "menos cuarto", "menos cuarto = kwart voor",
     "2:45 — Son las tres ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "y cuarto", "y cuarto = kwart over (+15 min)",
     "5:15 — Son las cinco ___.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "medianoche", "0:00 = middernacht, medianoche",
     "0:00 — Es ___. La ciudad duerme.", instr="Vul in", size=20, gap=8)
e.head("B　EL PRESENTE", 25)
e.expl("Vul de tegenwoordige tijd van de werkwoorden in.")
e.ex("A2", "Zinnen aanvullen", "duermo", "dormir verandert: o → ue (duermo)",
     "Yo ___ (dormir) una hora más el domingo.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "dormimos", "bij nosotros blijft het dormimos",
     "El domingo ___ (dormir) todos una hora más.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "cambian", "los relojes → cambian (ellos)",
     "Los relojes del móvil ___ (cambiar) solos.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "se despierta", "wederkerend: despertarse → se despierta",
     "María ___ (despertarse) a las ocho.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Zinnen aanvullen", "se atrasa", "el reloj se atrasa (él)",
     "El reloj ___ (atrasar) una hora.", instr="Vul in", size=20, gap=8)
e.head("C　COMPRENSIÓN", 25)
e.expl("Lees het artikel op pagina 2 en kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "C", "het uur 02:00–03:00 komt twee keer voor",
     "La hora de 02:00 a 03:00 existe... A. nunca · B. una vez · C. dos veces", size=20, gap=8)
e.ex("A2", "Meerkeuze", "B", "op de Canarische eilanden wordt 02:00 dan 01:00",
     "En Canarias, a las 02:00 será... A. las 02:00 · B. la 01:00 · C. las 03:00", size=20, gap=8)
e.ex("A2", "Meerkeuze", "A", "de ovenklok moet je met de hand verzetten",
     "¿Qué reloj NO cambia solo? A. el del horno · B. el del móvil · C. el del ordenador", size=20, gap=8)
e.ex("A2", "Meerkeuze", "B", "de wintertijd duurt tot 28 maart 2027",
     "El horario de invierno dura hasta... A. el 1 de noviembre · B. el 28 de marzo de 2027 · C. el 29 de noviembre", size=20, gap=8)
e.head("D　LAS PALABRAS", 25)
e.match_set("A2", "Woorden combineren",
            ["la tormenta", "el pronóstico", "atrasar", "el paraguas"],
            ["lo abres cuando llueve",
             "lluvia fuerte con truenos y rayos",
             "poner el reloj una hora antes",
             "el informe sobre el tiempo de mañana"],
            ["b", "d", "c", "a"],
            ["tormenta = zware regenbui met onweer b", "pronóstico = de weersverwachting d", "atrasar = de klok een uur terugzetten c", "paraguas = de paraplu a"],
            instr="Combineer")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vida.svg")
print("P2 saved, exercises so far:", len(REG))
