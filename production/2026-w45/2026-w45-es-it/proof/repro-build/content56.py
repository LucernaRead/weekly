# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/es-it-proof/repro-svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JUVENTUD (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUVENTUD · GIOVENTÙ", "La Lucerna", "NIVEL B1 · La NFL en Madrid · La NFL arriva a Madrid")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Madrid, capital del fútbol americano", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: B1")
f.para("El Bernabéu cambia el césped por el emparrillado: el fútbol americano llega a Madrid.")
f.para("El domingo 8, a las 15:30, el estadio Santiago Bernabéu acoge un partido de la NFL, la liga profesional de fútbol americano: los Cincinnati Bengals contra los Atlanta Falcons. Es el segundo partido de la NFL en el Bernabéu: el primero fue el 16 de noviembre de 2025, Miami Dolphins contra Washington Commanders.")
f.para("Antes del partido, dos himnos: el guitarrista español Pablo Sáinz-Villegas toca el himno de España y la cantante Taylor Momsen canta el de Estados Unidos. El fútbol americano es otro deporte: se juega con las manos, se avanza en cuatro intentos y se marca con touchdowns. Pero el ritual es el mismo: estadio lleno, colores y ruido.")
f.para("Y el sábado 31, Madrid ya vivió su otra noche americana: Halloween llenó las calles de disfraces, calabazas y monstruos de mentira. Del susto del sábado al deporte del domingo: el puente, para los jóvenes, tiene dos noches grandes.")
f.box("EL PLAN DEL PUENTE · IL PIANO", [
    ("1. El lunes 2: descanso y familia — o viaje, si tu comunidad hace puente(lunedì: riposo e famiglia — o viaggio, se la tua comunità fa ponte)", "serif", False, INK, 21, 1.36),
    ("2. El sábado 7: Valencia–Real Madrid, 21:00, en Mestalla(sabato sera: Valencia–Real Madrid)", "serif", False, INK, 21, 1.36),
    ("3. El domingo 8, 15:30: la NFL en el Bernabéu(domenica pomeriggio: la NFL al Bernabéu)", "serif", False, INK, 21, 1.36),
    ("4. El domingo 8, 21:00: Atlético–Barça en el Metropolitano(domenica sera: Atlético–Barça al Metropolitano)", "serif", False, INK, 21, 1.36),
    ("5. Y el lunes 9: vuelta a clase y al trabajo; la campaña empieza el viernes 13(ritorno a scuola e al lavoro; la campagna inizia venerdì 13)", "serif", False, INK, 21, 1.36),
])
f.gloss("el emparrillado il campo da football americano (a forma di griglia) · el himno l'inno · el touchdown il touchdown, la meta · la calabaza la zucca.")
f.end_report()

# col 3: pumpkin image + facts + ¿Y tú?
ix = COLX[3]
image(p, "kuerbis.jpg", ix, 200, CW, 290)
cy3 = caption(p, ix, 490, CW, "Calabazas en un mercado agrícola: el sábado 31, Halloween llenó las calles de calabazas, disfraces y monstruos de mentira. El domingo 8, el Bernabéu cambia de deporte.",
              "Foto: Departamento de Agricultura de EE. UU. — dominio público")
facts = ["El domingo 8, 15:30: Bengals contra Falcons en el Bernabéu, segundo partido NFL en Madrid.",
         "Antes del partido, dos himnos: Sáinz-Villegas (España) y Taylor Momsen (EE. UU.).",
         "El primer partido NFL en el Bernabéu fue el 16 de noviembre de 2025."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LA NFL EN MADRID", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Has visto alguna vez un partido de fútbol americano? ¿Qué te gusta más: el fútbol o el fútbol americano? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Hai mai visto una partita di football americano? Preferisci il calcio o il football americano? Scrivi due frasi e mandale.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ? · TOCCA A TE", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Hai mai visto una partita di football americano? Preferisci il calcio o il football americano? Scrivi due frasi e mandale.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · ESERCIZI · PAGINA 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8 · livelli misti: cerca per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · COMPRENSIÓN", 25)
e.bridge("Leggi l'articolo di pagina 5 e scegli la risposta giusta.")
e.ex("B1", "单选", "B", "la NFL a Madrid è domenica alle 15:30",
     "La NFL llega al Bernabéu el... A. sábado 7 · B. domingo 8, 15:30 · C. lunes 2", size=20, gap=8)
e.ex("B1", "单选", "A", "Bengals contro Falcons",
     "El partido es... A. Bengals – Falcons · B. Madrid – Barça · C. Dolphins – Falcons", size=20, gap=8)
e.ex("B1", "单选", "C", "l'inno spagnolo è suonato con la chitarra",
     "El himno de España lo toca... A. Taylor Momsen · B. un coro · C. Pablo Sáinz-Villegas", size=20, gap=8)
e.ex("B1", "单选", "B", "la prima NFL al Bernabéu è stata il 16 novembre 2025",
     "El primer partido NFL en el Bernabéu fue... A. en 2024 · B. el 16 de noviembre de 2025 · C. el 8 de noviembre", size=20, gap=8)
e.ex("B1", "单选", "A", "il football americano si gioca con le mani, con quattro tentativi",
     "El fútbol americano se juega... A. con las manos, en cuatro intentos · B. con los pies, en dos tiempos · C. con las manos, en un intento", size=20, gap=8)
e.head("B · PALABRAS DEL TEXTO", 25)
e.bridge("Completa con le parole del riquadro. Attenzione: alcune vanno coniugate.")
e.para("himno · estadio · touchdown · disfraz · calabaza · acoger", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "estadio", "estadio = stadio",
     "El partido se juega en el ___ Bernabéu.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "himno", "himno = inno",
     "Antes del partido suenan dos ___: el de España y el de EE. UU.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "acoge", "acoger coniugato → acoge",
     "El Bernabéu ___ (infinito: acoger) un partido de la NFL.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "touchdown", "touchdown = meta",
     "En el fútbol americano se marca con ___.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "calabaza", "calabaza = zucca",
     "El 31 de octubre las calles se llenan de ___ y disfraces.", instr="Completa", size=20, gap=8)
e.ex("B1", "完成句子", "disfraz", "disfraz = costume",
     "Para Halloween compro un ___.", instr="Completa", size=20, gap=8)
e.head("C · IR A + INFINITIVO", 25)
e.bridge("Riscrivi con ir a + infinito, per dire che cosa succederà.")
e.ex("B1", "句型转换", "Vamos a ver la NFL el domingo.", "vamos a + infinito",
     "Vemos la NFL el domingo. → ___", instr="Riscrivi", size=20, gap=8)
e.ex("B1", "句型转换", "Va a tocar el himno de España.", "va a + infinito",
     "Toca el himno de España. → ___", instr="Riscrivi", size=20, gap=8)
e.ex("B1", "句型转换", "Vas a comprar un disfraz el sábado.", "vas a + infinito",
     "Compras un disfraz el sábado. → ___", instr="Riscrivi", size=20, gap=8)
e.ex("B1", "句型转换", "Van a llenar las calles de calabazas.", "van a + infinito",
     "Llenan las calles de calabazas. → ___", instr="Riscrivi", size=20, gap=8)
e.head("D · ¿VERDADERO O FALSO?", 25)
e.ex("B1", "判断对错", "Verdadero", "la NFL di domenica è la seconda al Bernabéu",
     "El partido del domingo es el segundo de la NFL en el Bernabéu. ¿Verdadero o falso?", instr="Vero o falso", size=20, gap=8)
e.ex("B1", "判断对错", "Falso", "l'inno degli Stati Uniti lo canta Momsen, non Sáinz-Villegas",
     "El himno de EE. UU. lo toca Pablo Sáinz-Villegas. ¿Verdadero o falso?", instr="Vero o falso", size=20, gap=8)
e.ex("B1", "判断对错", "Verdadero", "la notte di Halloween è stata sabato 31",
     "Halloween llenó las calles el sábado 31. ¿Verdadero o falso?", instr="Vero o falso", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-juventud.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · A FONDO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("A FONDO · APPROFONDIMENTO", "La Lucerna", "NIVEL B2 · La vivienda decide la campaña · La casa decide la campagna")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P6-main")
f.title("La vivienda decide la campaña", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: B2 · La política nacional española")
f.para("La vivienda es el principal problema para el 55,7 % de los españoles.")
f.para("Ese dato es del barómetro de octubre del CIS, el instituto público de encuestas: se hizo del 1 al 6 de octubre, con 5.025 entrevistas, un margen de error de ±1,4 puntos y se publicó el 14 de octubre. La vivienda (55,7 %) va muy por delante de la inmigración (20,9 %) y de la economía (20,3 %). Es una cifra récord, veinte puntos más que en septiembre.")
f.para("El barómetro también da la estimación de voto: PSOE 34 %, PP 22,2 %, Vox 17,1 %, Sumar 6,1 % y Podemos 3,1 %. Pero ojo: los demás sondeos dibujan otro mapa — la mayoría apunta a una mayoría conjunta de PP y Vox. El CIS va por su lado. Por eso esta página no publica una media mezclada: cada serie tiene su método, su fecha y su historia.")
f.para("Una encuesta es una foto con margen de error, tomada en un día concreto.")
f.para("Y mientras tanto, el precio sigue subiendo: según Idealista, la vivienda usada costaba en septiembre de 2026 unos 2.930 euros por metro cuadrado (+11,8 % en un año). Esa es la razón por la que todos los programas de esta semana hablan de vivienda: no es un tema de los partidos, es un tema de la calle.")
f.para("Las próximas semanas traerán los programas completos, los debates y, al final, la única encuesta que no admite error: la del 29 de noviembre, con papeletas de verdad.")
f.end_report()

# col 3: timeline + poll-reading box (sequential, measured)
bx = COLX[3]
steps = [
    "2 OCT. — El Congreso rechaza dos decretos de vivienda.",
    "5 OCT. — Sánchez disuelve las Cortes; elecciones el 29-N.",
    "6 OCT. — El decreto de convocatoria sale en el BOE.",
    "16 OCT. — Los partidos comunican sus coaliciones.",
    "21–26 OCT. — Se presentan las candidaturas.",
    "28 OCT. — Las listas se publican en el BOE.",
    "3 NOV. — El BOE difunde las candidaturas proclamadas.",
    "13 NOV. — Empieza la campaña electoral.",
    "29 NOV. — Elecciones generales: España vota.",
]
tl_h = 68 + sum(len(wrap(t, "serif", False, 19, CW - 44)) * 19 * 1.35 + 29 for t in steps) + 20
p.rect(bx, 200, CW, tl_h, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 200 + 16
p.text(bx + 22, yy3 + 26, "EL CAMINO AL 29N", 24, "sans", True, OLIVE)
yy3 += 52
for t in steps:
    yy3 = p.para(bx + 22, yy3 + 19, t, 19, "serif", False, INK, CW - 44, 1.35) + 10
tl_end = 200 + tl_h
by3 = tl_end + 26
bb = ("Para leer cualquier encuesta, pregunta tres cosas: ¿quién la publica? "
      "¿Cuándo se hizo el trabajo de campo? ¿Qué margen de error tiene? "
      "Sin esas tres respuestas, un porcentaje no dice casi nada.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LEER UNA ENCUESTA", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh, "timeline box height", tl_h)

# ---- bar chart (CIS October, honestly captioned) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, GOLD, 2)
p.text(MX, gy + 10, "EL BARÓMETRO CIS DE OCTUBRE · estimación de voto, %", 26, "sans", True, OLIVE)
cis = [("PSOE", 34.0), ("PP", 22.2), ("Vox", 17.1), ("Sumar", 6.1), ("Podemos", 3.1)]
bx1, bw_, bhh = MX, 2 * CW + GUT, 322
p.rect(bx1, gy + 28, bw_, bhh, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx1 + 22, gy + 68, "BARÓMETRO CIS (OCTUBRE) · estimación de voto, %", 21, "sans", True, INK)
yy = gy + 96
for lab, v in cis:
    p.text(bx1 + 22, yy + 24, lab, 21, "serif", True, INK)
    p.rect(bx1 + 150, yy + 6, v * 12, 22, fill=OLIVE)
    p.text(bx1 + 168 + v * 12, yy + 24, f"{v:.1f}".replace(".", ",") + " %", 20.5, "serif", False, INK)
    yy += 31
p.para(bx1 + 22, gy + bhh - 30, "CIS, instituto público · trabajo de campo del 1 al 6 de octubre de 2026 · 5.025 entrevistas · margen ±1,4 puntos · publicado el 14 de octubre. Los demás sondeos dibujan otro mapa: aquí solo se publica esta serie, con su fuente y su fecha.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right column: housing problem chart note
rx = COLX[2]
p.rect(rx, gy + 28, 2 * CW + GUT, bhh, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(rx + 22, gy + 68, "EL PROBLEMA Nº 1: LA VIVIENDA", 21, "sans", True, INK)
yy = gy + 96
for lab, v in [("Vivienda", 55.7), ("Inmigración", 20.9), ("Economía", 20.3)]:
    p.text(rx + 22, yy + 24, lab, 21, "serif", True, INK)
    p.rect(rx + 150, yy + 6, v * 7.5, 22, fill=BRICK)
    p.text(rx + 168 + v * 7.5, yy + 24, f"{v:.1f}".replace(".", ",") + " %", 20.5, "serif", False, INK)
    yy += 31
p.para(rx + 22, gy + bhh - 30, "«El principal problema de España», según el mismo barómetro CIS de octubre: la vivienda sube veinte puntos en un mes. Segundo: la inmigración. Tercero: la economía.", 17.5, "sans", False, GREY, 2 * CW + GUT - 44, 1.3)

# ---- P6 exercises ----
ey = 1940
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · ESERCIZI · PAGINA 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8 · livelli misti: cerca per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LEER LOS GRÁFICOS", 25)
e.bridge("Guarda i grafici e scegli.")
e.ex("B2", "单选", "A", "nel CIS il PSOE è primo (34%)",
     "En el barómetro del CIS, primero va... A. el PSOE · B. el PP · C. Vox", size=19, gap=1)
e.ex("B2", "单选", "B", "nel CIS il PP è al 22,2%",
     "En el barómetro del CIS, el PP tiene... A. 34 % · B. 22,2 % · C. 17,1 %", size=19, gap=1)
e.ex("B2", "单选", "C", "la casa è il primo problema (55,7%)",
     "El principal problema, según el CIS, es... A. la economía · B. la inmigración · C. la vivienda", size=19, gap=1)
e.ex("B2", "单选", "A", "il sondaggio è stato fatto dal 1º al 6 ottobre",
     "El trabajo de campo del CIS fue... A. del 1 al 6 de octubre · B. del 21 al 26 de octubre · C. el 14 de octubre", size=19, gap=1)
e.ex("B2", "单选", "B", "34 + 22,2 + 17,1 = 73,3",
     "PSOE + PP + Vox en el CIS suman... A. 50 % · B. 73,3 % · C. 100 %", size=19, gap=1)
e.ex("B2", "单选", "C", "questo giornale pubblica solo la serie CIS, con fonte e data",
     "La Lucerna publica aquí... A. una media mezclada · B. todos los sondeos · C. solo la serie del CIS, con fuente y fecha", size=19, gap=1)
e.head("B · COMPRENSIÓN", 25)
e.ex("B2", "单选", "B", "il 2 ottobre il Parlamento ha respinto due decreti sulla casa",
     "El 2 de octubre, el Congreso... A. aprobó dos decretos · B. rechazó dos decretos de vivienda · C. disolvió las Cortes", size=19, gap=1)
e.ex("B2", "单选", "A", "il 5 ottobre scioglimento del Parlamento e convocazione delle elezioni",
     "El 5 de octubre, Sánchez... A. disolvió las Cortes y convocó elecciones · B. publicó las listas · C. empezó la campaña", size=19, gap=1)
e.ex("B2", "单选", "C", "un sondaggio è una foto con margine di errore, scattata in un giorno preciso",
     "Según el texto, una encuesta es... A. un resultado final · B. una promesa · C. una foto con margen de error", size=19, gap=1)
e.ex("B2", "单选", "B", "la campagna inizia il 13 novembre",
     "La campaña electoral empieza el... A. 3 de noviembre · B. 13 de noviembre · C. 29 de noviembre", size=19, gap=1)
e.head("C · EL SUBJUNTIVO", 25)
e.ex("B2", "完成句子", "tenga", "es posible que + congiuntivo: tenga",
     "Es posible que el CIS ___ (tener) otro método.", instr="Completa", size=19, gap=1)
e.ex("B2", "完成句子", "sea", "es importante que + congiuntivo: sea",
     "Es importante que cada gráfico ___ (ser) claro.", instr="Completa", size=19, gap=1)
e.ex("B2", "完成句子", "para que", "para que + congiuntivo (scopo)",
     "Publicamos la fuente ___ todos puedan comprobarla.", instr="Completa", size=19, gap=1)
e.ex("B2", "完成句子", "Aunque", "Aunque + indicativo (fatto noto)",
     "___ las encuestas difieren, ninguna miente.", instr="Completa", size=19, gap=1)
e.head("D · PALABRAS DEL DEBATE", 25)
e.bridge("Completa con le parole del riquadro: sondeo · muestra · indecisos · margen de error")
e.ex("B2", "完成句子", "sondeo", "sondeo = sondaggio",
     "Un ___ pregunta a una muestra de ciudadanos.", instr="Completa", size=19, gap=1)
e.ex("B2", "完成句子", "muestra", "muestra = campione (5.025 persone)",
     "El CIS entrevistó a una ___ de 5.025 personas.", instr="Completa", size=19, gap=1)
e.ex("B2", "完成句子", "indecisos", "indecisos = indecisi",
     "Los ___ todavía no saben a quién votar.", instr="Completa", size=19, gap=1)
e.ex("B2", "完成句子", "margen de error", "margen de error = margine di errore",
     "Toda encuesta tiene un ___.", instr="Completa", size=19, gap=1)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-afondo.svg")
print("P6 saved, exercises so far:", len(REG))
