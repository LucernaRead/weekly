# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/es-it-proof/transform-svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · PORTADA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2 · SEGUNDA EDICIÓN", 23, "sans", True, OLIVE)
p.text(975, 92, "CADA SEMANA EN ESPAÑOL · OGNI SETTIMANA · LO SPAGNOLO DEGLI SPAGNOLI", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "SEMANA DEL 2 AL 8 DE NOVIEMBRE DE 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "La Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SETTIMANALE SPAGNOLO · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL", 46, "serif", True, INK, anchor="middle")
p.text(975, 372, "EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA", 19, "sans", False, GREY, anchor="middle")
p.text(975, 574, "TESTI IN SPAGNOLO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI", 22, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "¡LA VIVIENDA DECIDE LA CAMPAÑA!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Faltan 27 días para el 29-N: las listas están cerradas y los programas, en marcha.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "MANCANO 27 GIORNI AL 29-N · LA CASA DECIDE LA CAMPAGNA", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "Il tema di copertina · vedi le pagine 2 e 6", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "LA NOTICIA · LA NOTIZIA", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "La cuenta atrás del 29-N: la vivienda decide la campaña", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "De la redacción de La Lucerna · Nivel de lectura: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("España entra en la semana decisiva antes de la campaña. Las listas ya están presentadas: ahora los partidos escriben sus programas.")
f.para("El domingo 29 de noviembre, España vota en elecciones generales. El presidente Pedro Sánchez disolvió las Cortes el 5 de octubre, después de que el Congreso rechazara dos decretos de vivienda el 2 de octubre. Entre el 21 y el 26 de octubre, los partidos presentaron sus candidaturas.")
f.para("¿Por qué la vivienda decide la campaña? Porque, según el barómetro de octubre del CIS, más de la mitad de los españoles la cita como el primer problema del país. Ningún otro tema llega tan alto (página 6).")
f.para("Y esta semana empieza con un descanso largo para millones de españoles: el lunes 2 es fiesta en nueve comunidades (página 2).")
f.para("El domingo 8, Madrid tiene dos citas: la NFL a las 15:30 y el Atlético–Barça a las 21:00.")
f.para("Esta es la segunda edición de La Lucerna en español: cada semana, la España real contigo. ¡Bienvenidos!")
f.bridge("la cuenta atrás il conto alla rovescia · disolver las Cortes sciogliere il Parlamento · el decreto il decreto · la candidatura la candidatura.")
f.box("LA SEMANA EN CIFRAS · IN CIFRE", [
    ("27 — días faltan el lunes 2 para las elecciones del domingo 29(ancora 27 giorni alle elezioni di domenica 29)", "serif", False, INK, 20.5, 1.35),
    ("9 — comunidades donde el lunes 2 de noviembre es fiesta(il 2 novembre è festa in 9 comunità)", "serif", False, INK, 20.5, 1.35),
    ("55,7 — % que cita la vivienda como el principal problema, según el CIS de octubre(dati CIS di ottobre)", "serif", False, INK, 20.5, 1.35),
])
f.head("AHORA TÚ · TOCCA A TE", 25)
f.ex("A2", "完成句子", "programas", "las listas ya están presentadas; ahora se escriben los programas",
     "Las listas ya están presentadas: ahora los partidos escriben sus ___.", size=20.5)
f.ex("A2", "完成句子", "29", "le elezioni sono domenica 29 novembre",
     "España vota en elecciones generales el domingo ___ de noviembre.", size=20.5)
f.ex("A2", "完成句子", "vivienda", "la casa è il tema decisivo della campagna",
     "La ___ decide la campaña del 29-N.", size=20.5)
f.ex("A2", "完成句子", "nueve", "il lunedì è festa in nove comunità",
     "El lunes 2 es fiesta en ___ comunidades.", size=20.5)
f.ex("B1", "完成句子", "21:00", "l'Atlético–Barça inizia domenica alle 21:00",
     "El Atlético–Barça del domingo se juega a las ___.", size=20.5)
f.ex("B1", "完成句子", "15:30", "la NFL a Madrid inizia domenica alle 15:30",
     "La NFL llega al Bernabéu el domingo a las ___.", size=20.5)
f.end_report()

# ---- claves de la semana (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "CINCO", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "CLAVES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Cinque chiavi · Para entender la semana", 19, "sans", False, GREY)
gt = [
    ("La precampaña del 29-N", 250),
    ("El puente del lunes 2", 226),
    ("La semana europea", 196),
    ("Atlético–Barça, el domingo", 158),
    ("La NFL en el Bernabéu", 122),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE if i == 0 else GOLD)
    byy += 92
p.text(gx + 22, byy + 16, "Cinco claves, sin números", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "inventados: todo está explicado", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 68, "en esta edición.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 102, "Cinque chiavi, zero numeri inventati.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "EN ESTA EDICIÓN · IL NUMERO", 24, "sans", True, OLIVE)
som = [
    ("Pág. 2", "El puente del lunes 2", "A2"),
    ("Pág. 3", "Tres noches de otoño", "A2→B1"),
    ("Pág. 4", "Europa y el domingo", "B1"),
    ("Pág. 5", "La NFL en Madrid", "B1"),
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
y2 = p.para(gx, my + 76, "« la precampaña » : los partidos cierran listas y escriben programas.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "«La precampagna»: prima della campagna.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
p.rect(ix, iy, iw, 320, fill=BOX, stroke=LINE, sw=1.4)
illus_houses(p, ix + 188, iy + 30, s=2.2)
caption(p, ix, iy + 320, iw,
        "Casas, pisos y alquileres: la vivienda es el tema que decide la campaña del 29-N. En la página 6, los datos del CIS y el calendario completo hacia el 29 de noviembre. (Ilustración de la redacción, no una fotografía)",
        "Ilustración: La Lucerna")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-otono")
f2.head("UNA SEMANA, DOS ESPAÑAS", 25)
f2.para("El lunes, unos de puente y otros, a trabajar. El domingo, Madrid con dos citas a la vez. Entre medias, Europa y las listas: esta semana España vive a la vez su descanso y su campaña.", 22.5)
f2.para("Nuestro consejo para esta semana: lee el programa, no solo el titular. En la página 6 te enseñamos cómo.", 22.5)
f2.end_report()
# col 3 BREVES
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "BREVES · IN BREVE", 24, "sans", True, OLIVE)
brefs = [
    ("EL PUENTE", "El lunes 2 es fiesta en 9 comunidades de 17. La lista completa, en la página 2."),
    ("EUROPA", "Champions el martes: Barça–Aston Villa, Atlético–Bayern y Villarreal–PSG. (Página 4)"),
    ("EL DOMINGO", "La NFL en el Bernabéu por la tarde y el Atlético–Barça por la noche. (Páginas 4 y 5)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "QUIZ RELÁMPAGO · QUIZ LAMPO", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Leggi la prima pagina e scegli la risposta giusta · risposte a pagina 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "单选", "C", "le elezioni sono il 29 novembre",
      "Las elecciones generales son el... A. 2 de noviembre · B. 13 de noviembre · C. 29 de noviembre", size=21)
qf.ex("A2", "单选", "B", "il lunedì è festa in nove comunità",
      "El lunes 2 es fiesta en... A. todas las comunidades · B. nueve comunidades · C. ninguna", size=21)
qf.ex("A2", "单选", "A", "la NFL a Madrid è domenica pomeriggio",
      "La NFL llega al Bernabéu el... A. domingo 8 · B. lunes 2 · C. viernes 6", size=21)
qf.ex("A2", "单选", "B", "l'Atlético–Barça è domenica alle 21:00",
      "El Atlético–Barça se juega el domingo a las... A. 15:30 · B. 21:00 · C. 18:30", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-portada.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VIDA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIDA · VITA QUOTIDIANA", "La Lucerna", "NIVEL A2 · El puente del lunes 2 · Il ponte di lunedì 2")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("El puente del lunes 2: tres días para unos, lunes normal para otros", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: A2")
f.para("El lunes 2 de noviembre es festivo en nueve comunidades — y día de trabajo en las demás.")
f.para("Las nueve son: Andalucía, Aragón, Asturias, Canarias, Castilla-La Mancha, Castilla y León, Extremadura, Madrid y Navarra. Allí, el fin de semana dura tres días: del sábado 31 de octubre al lunes 2 de noviembre. En las demás — Baleares, Cantabria, Cataluña, Galicia, Murcia, el País Vasco, La Rioja, la Comunitat Valenciana, Ceuta y Melilla — el lunes 2 es un día de trabajo normal.")
f.para("¿Por qué pasa esto? Porque el Día de Todos los Santos, el 1 de noviembre, cayó en domingo. Cuando una fiesta cae en domingo, algunas comunidades pasan el día libre al lunes. Por eso todos preguntan lo mismo: «¿El lunes es fiesta en mi comunidad?»")
f.para("Es la segunda semana con horario de invierno: anochece pronto y las tardes se hacen cortas. El puente, entonces, sabe mejor: tres días para descansar, leer y ver a la familia antes de una semana llena de fútbol y de precampaña.")
f.box("EL CALENDARIO · IL CALENDARIO", [
    ("Lunes 2 — puente en nueve comunidades; las candidaturas proclamadas llegan al BOE el martes 3(lunedì: ponte in nove comunità; martedì il BOE pubblica le liste ufficiali)", "serif", False, INK, 21, 1.36),
    ("Martes 3 — Champions: Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG(martedì: tre partite di Champions di squadre spagnole)", "serif", False, INK, 21, 1.36),
    ("Miércoles 4 — Champions: AEK–Real Madrid, 18:45(mercoledì: il Real in trasferta contro l'AEK Atene)", "serif", False, INK, 21, 1.36),
    ("Jueves 5 — Europa League: Real Sociedad–Lyon, 18:45(giovedì: la Real Sociedad in Europa League contro il Lione)", "serif", False, INK, 21, 1.36),
    ("Viernes 6 — Liga, jornada 12: Sevilla–Alavés, 21:00(venerdì: inizia la 12ª giornata di Liga)", "serif", False, INK, 21, 1.36),
    ("Sábado 7 — Valencia–Real Madrid, 21:00, en Mestalla(sabato: Valencia–Real Madrid)", "serif", False, INK, 21, 1.36),
    ("Domingo 8 — NFL en el Bernabéu, 15:30; Atlético–Barça, 21:00(domenica: NFL a Madrid + Atlético–Barça)", "serif", False, INK, 21, 1.36),
])
f.head("DECIR LA FECHA", 25)
f.para("En español, la fecha se dice así: «el lunes 2 de noviembre». Primero el día de la semana, luego el número y luego el mes. Los días y los meses van en minúscula: lunes, noviembre. Y ojo: el primero del mes no es «el primero», es «el uno»: el 1 de noviembre.", 23)
f.gloss("festivo in festa · el puente il ponte · la comunidad la comunità autonoma · anochecer il calare della sera · el horario de invierno l'ora solare.")
f.end_report()

# col 3: facts + ¿Y tú? (sequential, measured)
ix = COLX[3]
facts = ["El lunes 2 es festivo en 9 comunidades — y día de trabajo en las demás.",
         "Todos los Santos cayó en domingo 1: por eso algunas comunidades pasan la fiesta al lunes.",
         "Es la segunda semana con horario de invierno: anochece pronto."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "¿SABÍAS QUE…?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿El lunes 2 es fiesta en tu comunidad? ¿Qué haces con el puente: viajas, descansas o ves fútbol? Escribe dos frases en español y envíalas a la redacción: las mejores salen en la página 7, «Cartas de los lectores»."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Il 2 novembre da te è festa? E con il ponte cosa fai: viaggi, riposi o guardi calcio? Scrivi due frasi in spagnolo e mandale alla redazione.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ? · TOCCA A TE", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Il 2 novembre da te è festa? E con il ponte cosa fai: viaggi, riposi o guardi calcio? Scrivi due frasi in spagnolo e mandale alla redazione.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Decir la fecha wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "LOS DÍAS DE LA SEMANA · DIRE LE DATE", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "lunes 2 – domingo 8 de noviembre · da lunedì 2 a domenica 8 novembre", 20, "sans", False, GREY, anchor="end")
lx = MX
ly = dy + 58
for d, t in [
    ("lunes 2", "el lunes 2 — festivo en nueve comunidades"),
    ("martes 3", "el martes 3 — Champions y BOE"),
    ("miércoles 4", "el miércoles 4 — AEK–Real Madrid, 18:45"),
    ("jueves 5", "el jueves 5 — Real Sociedad–Lyon, 18:45"),
]:
    p.text(lx, ly + 24, d, 24, "serif", True, OLIVE)
    p.text(lx + 240, ly + 24, t, 21, "sans", False, GREY)
    ly += 36
ly = dy + 58
rx = MX + 910
for d, t in [
    ("viernes 6", "el viernes 6 — Sevilla–Alavés, 21:00"),
    ("sábado 7", "el sábado 7 — Valencia–Real Madrid, 21:00"),
    ("domingo 8", "el domingo 8 — NFL, 15:30; Atlético–Barça, 21:00"),
]:
    p.text(rx, ly + 24, d, 24, "serif", True, OLIVE)
    p.text(rx + 240, ly + 24, t, 21, "sans", False, GREY)
    ly += 36
p.para(lx, dy + 226, "Ojo: los días de la semana y los meses van en minúscula en español — lunes, noviembre — y el 1 del mes es «el uno», no «el primero».", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · ESERCIZI · PAGINA 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8 · livelli misti: cerca per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · LAS FECHAS", 25)
e.bridge("Completa con la forma giusta della data.")
e.ex("A2", "完成句子", "2", "lunedì 2 novembre",
     "El puente es el lunes ___ de noviembre.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "8", "domenica 8 novembre",
     "El Atlético–Barça se juega el domingo ___ de noviembre.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "29", "le elezioni sono il 29 novembre",
     "Las elecciones generales son el ___ de noviembre.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "uno", "il giorno 1 si dice el uno",
     "El Día de Todos los Santos es el ___ de noviembre.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "noviembre", "i mesi si scrivono in minuscolo",
     "El lunes 2 de ___ es festivo en nueve comunidades.", instr="Completa", size=20, gap=8)
e.head("B · EL PRESENTE", 25)
e.bridge("Completa con il presente del verbo.")
e.ex("A2", "完成句子", "es", "el lunes → es (singolare)",
     "El lunes 2 ___ festivo en Madrid.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "preguntan", "todos → preguntan",
     "Todos ___ lo mismo: «¿El lunes es fiesta?»", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "anochece", "anochecer → anochece",
     "En noviembre ___ pronto.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "descansamos", "nosotros → descansamos",
     "Con el puente, ___ tres días.", instr="Completa", size=20, gap=8)
e.ex("A2", "完成句子", "dura", "el fin de semana → dura",
     "El fin de semana ___ tres días en Madrid.", instr="Completa", size=20, gap=8)
e.head("C · COMPRENSIÓN", 25)
e.bridge("Leggi l'articolo di pagina 2 e scegli la risposta giusta.")
e.ex("A2", "单选", "B", "il lunedì è festa in nove comunità",
     "¿En cuántas comunidades es festivo el lunes 2? A. en todas · B. en nueve · C. en ninguna", size=20, gap=8)
e.ex("A2", "单选", "A", "Ognissanti, il 1º novembre, cade di domenica",
     "Todos los Santos cayó en... A. domingo · B. lunes · C. sábado", size=20, gap=8)
e.ex("A2", "单选", "C", "in Catalogna il lunedì si lavora",
     "El lunes 2, en Cataluña... A. es fiesta · B. hay puente · C. se trabaja", size=20, gap=8)
e.ex("B1", "单选", "B", "seconda settimana di ora solare: fa buio presto",
     "Es la segunda semana con... A. horario de verano · B. horario de invierno · C. vacaciones", size=20, gap=8)
e.head("D · LAS PALABRAS", 25)
e.match_set("A2", "词汇配对",
            ["el puente", "festivo", "anochecer", "la comunidad"],
            ["día de fiesta, sin trabajo",
             "descanso largo de tres días",
             "hacerse de noche",
             "una región con gobierno propio"],
            ["b", "a", "c", "d"],
            ["puente=ponte di tre giorni b", "festivo=di festa a", "anochecer=il far buio c", "comunidad=comunità autonoma d"],
            instr="Abbina le parole")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vida.svg")
print("P2 saved, exercises so far:", len(REG))
