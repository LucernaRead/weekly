# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P5 youth / P6 deep read. Fresh text, structure mirrors W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JUVENTUD (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUVENTUD · Jeugd", "La Lucerna", "NIVEL B1 · Votar desde casa · Stemmen vanuit huis")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Votar desde casa: el voto por correo", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: B1")
f.para("No hace falta ir al colegio electoral para votar: el voto por correo llega a casa.")
f.para("El voto por correo se pide desde la convocatoria y hasta el jueves 19 de noviembre, en cualquier oficina de Correos o por internet, en la web de Correos. La Oficina del Censo Electoral envía la documentación a la dirección indicada a partir del lunes 9 de noviembre. Después, votas en casa, con calma, y envías el sobre.")
f.para("Y si prefieres votar en persona, el domingo 29 los colegios electorales abren de 9:00 a 20:00, con tu documento de identidad. El sábado 28, jornada de reflexión, no hay propaganda ni actos de campaña: un día de silencio antes de votar.")
f.para("Y el viernes 13, la otra cita de la semana joven: llega a HBO Max «Infamia», un thriller español de seis episodios con Susana Abaitua, que adapta la novela de la escritora gallega Ledicia Costas. La serie tuvo su estreno mundial en el festival de series de Cádiz.")
f.box("EL PLAN DE LA SEMANA · Het weekplan", tsize=20, paras=[
    ("1. El lunes 9: llega la documentación del voto por correo a casa (maandag: de stembiljetten worden verstuurd)", "serif", False, INK, 21, 1.36),
    ("2. El miércoles 11: huelga general de 24 horas (woensdag: 24 uur algemene staking)", "serif", False, INK, 21, 1.36),
    ("3. El jueves 12: Chequia–España, 20:45, en Praga (donderdagavond: Tsjechië–Spanje)", "serif", False, INK, 21, 1.36),
    ("4. El viernes 13: empieza la campaña; se estrena «Infamia» (vrijdag: de campagne begint; Infamia gaat in première)", "serif", False, INK, 21, 1.36),
    ("5. Y el domingo 15: España–Inglaterra, 20:45, en el Metropolitano (zondag: Spanje–Engeland)", "serif", False, INK, 21, 1.36),
])
f.gloss("el sobre = de envelop · la papeleta = het stembiljet · el censo = het kiezersregister · la jornada de reflexión = de dag van bezinning.")
f.end_report()

# col 3: typographic plate + facts + ¿Y tú?
ix = COLX[3]
p.rect(ix, 200, CW, 290, fill=DARK, stroke=LINE, sw=1.4)
p.text(ix + CW / 2, 300, "INFAMIA", 54, "sans", True, "#f3edda", anchor="middle")
p.text(ix + CW / 2, 352, "VIERNES 13 · HBO MAX", 24, "sans", True, "#b3a06a", anchor="middle")
p.text(ix + CW / 2, 404, "Seis episodios · Susana Abaitua", 21, "serif", False, "#e8dfc8", anchor="middle")
p.text(ix + CW / 2, 444, "Novela de Ledicia Costas", 21, "serif", False, "#e8dfc8", anchor="middle")
cy3 = caption(p, ix, 490, CW, "«Infamia», el thriller español del viernes 13: una abogada obsesionada con una desaparición de hace veinte años. El domingo 15, la otra pantalla: la Roja contra Inglaterra.",
              "Placa tipográfica: La Lucerna")
facts = ["El voto por correo se pide hasta el jueves 19: en Correos o por internet.",
         "La documentación llega a casa a partir del lunes 9 de noviembre.",
         "«Infamia» se estrena el viernes 13: seis episodios, en HBO Max."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "VOTAR DESDE CASA", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Votarías por correo o en persona? ¿Qué serie ves esta semana: «Infamia» o el fútbol? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Stem jij per post of ga je persoonlijk? Wat kijk jij deze week: Infamia of voetbal? Schrijf twee zinnen en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ? · En jij?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Stem jij per post of ga je persoonlijk? Wat kijk jij deze week: Infamia of voetbal? Schrijf twee zinnen en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · Oefeningen van pagina 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · Niveaus door elkaar — zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · COMPRENSIÓN", 25)
e.expl("Lees het artikel op pagina 5 en kies het juiste antwoord.")
e.ex("B1", "Meerkeuze", "B", "Stemmen per post moet vóór de 19e worden aangevraagd",
     "El voto por correo se pide hasta... A. el lunes 9 · B. el jueves 19 · C. el domingo 29", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "De documenten worden verstuurd vanaf 9 november",
     "La documentación del voto por correo llega desde... A. el lunes 9 · B. el viernes 13 · C. el sábado 28", size=20, gap=8)
e.ex("B1", "Meerkeuze", "C", "De stembureaus zijn open van 9:00 tot 20:00",
     "El domingo 29, los colegios abren... A. todo el día · B. de noche · C. de 9:00 a 20:00", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Infamia heeft 6 afleveringen",
     "«Infamia» tiene... A. dos episodios · B. seis episodios · C. veinte episodios", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "Op de dag van bezinning geen propaganda",
     "El sábado 28, jornada de reflexión, no hay... A. propaganda ni actos · B. fútbol · C. series", size=20, gap=8)
e.head("B · PALABRAS DEL TEXTO", 25)
e.expl("Vul in met de woorden uit het kader. Let op: sommige woorden moet je vervoegen.")
e.para("sobre · papeleta · censo · identidad · reflexión · correo", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Zinnen aanvullen", "correo", "correo = de post / per post",
     "Pido el voto por ___.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "papeleta", "papeleta = stembiljet",
     "En casa, relleno la ___.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "envío", "enviar vervoegd → envío",
     "Después ___ (infinitief enviar) el sobre.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "identidad", "documento de identidad = identiteitsbewijs",
     "Para votar en persona llevo mi documento de ___.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "censo", "censo = kiezersregister",
     "La Oficina del ___ envía la documentación.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Zinnen aanvullen", "reflexión", "jornada de reflexión = dag van bezinning",
     "El sábado 28 es la jornada de ___.", instr="Vul in", size=20, gap=8)
e.head("C · IR A + INFINITIVO", 25)
e.expl("Herschrijf de zinnen met ir a + infinitief (nabije toekomst).")
e.ex("B1", "Zinnen omvormen", "Voy a pedir el voto por correo.", "voy a + infinitief",
     "Pido el voto por correo. → ___", instr="Herschrijf", size=20, gap=8)
e.ex("B1", "Zinnen omvormen", "Va a estrenarse «Infamia».", "va a + infinitief",
     "Se estrena «Infamia». → ___", instr="Herschrijf", size=20, gap=8)
e.ex("B1", "Zinnen omvormen", "Vas a ver el España–Inglaterra.", "vas a + infinitief",
     "Ves el España–Inglaterra. → ___", instr="Herschrijf", size=20, gap=8)
e.ex("B1", "Zinnen omvormen", "Van a votar el domingo 29.", "van a + infinitief",
     "Votan el domingo 29. → ___", instr="Herschrijf", size=20, gap=8)
e.head("D · ¿VERDADERO O FALSO?", 25)
e.ex("B1", "Lezen: waar/onwaar", "Verdadero", "Stemmen per post vraag je aan bij Correos",
     "El voto por correo se pide en una oficina de Correos. ¿Verdadero o falso?", instr="W/NW", size=20, gap=8)
e.ex("B1", "Lezen: waar/onwaar", "Falso", "De dag van bezinning is zaterdag 28, niet zondag",
     "La jornada de reflexión es el domingo 29. ¿Verdadero o falso?", instr="W/NW", size=20, gap=8)
e.ex("B1", "Lezen: waar/onwaar", "Verdadero", "Infamia is gebaseerd op een roman van Ledicia Costas",
     "«Infamia» adapta una novela de Ledicia Costas. ¿Verdadero o falso?", instr="W/NW", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-juventud.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · A FONDO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("A FONDO · Achtergrond", "La Lucerna", "NIVEL B2 · La vivienda decide la campaña · Huisvesting beslist de campagne")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P6-main")
f.title("La vivienda decide la campaña", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: B2 · La política nacional española")
f.para("La vivienda preocupa al 86,9 % de los españoles.")
f.para("Ese dato es del Barómetro de Vivienda 2026 del CIS, el instituto público de encuestas: estudio número 3532, con 6.019 entrevistas, un margen de error de ±1,3 puntos, publicado el 8 de octubre. Es la primera vez que el CIS dedica un estudio monográfico a la vivienda.")
f.para("El barómetro pregunta por soluciones, y las respuestas son claras: el 91,4 % cree que las administraciones deberían construir más vivienda pública, y el 76,3 % defiende que el Estado intervenga en el mercado «tanto como sea necesario». El 79 % quiere que la vivienda se trate como un derecho constitucional, frente al 13,5 % que la ve como un bien de mercado.")
f.para("Una encuesta es una foto con margen de error, tomada en un día concreto.")
f.para("Y mientras tanto, la campaña ya tiene su calendario: el miércoles 11, huelga general; el viernes 13 empieza la campaña; el jueves 19 termina el plazo del voto por correo; el viernes 27 termina la campaña; y el domingo 29, la única encuesta que no admite error: la votación, con papeletas de verdad.")
f.para("El 28 de octubre, un grave accidente ferroviario en Urda (Toledo) detuvo la precampaña unos días. La investigación sigue abierta: esta página no adelanta conclusiones.")
f.end_report()

# col 3: timeline + poll-reading box (sequential, measured)
bx = COLX[3]
steps = [
    "2 OCT. — El Congreso rechaza dos decretos de vivienda.",
    "5 OCT. — Sánchez disuelve las Cortes; elecciones el 29-N.",
    "6 OCT. — El decreto de convocatoria sale en el BOE.",
    "21–26 OCT. — Se presentan las candidaturas.",
    "28 OCT. — Grave accidente en Urda: la precampaña se detiene.",
    "3 NOV. — El BOE difunde las candidaturas proclamadas.",
    "9 NOV. — La documentación del voto por correo llega a casa.",
    "11 NOV. — Huelga general de 24 horas.",
    "13 NOV. — Empieza la campaña electoral.",
    "19 NOV. — Termina el plazo para pedir el voto por correo.",
    "27 NOV. — Termina la campaña; el 29, España vota.",
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

# ---- bar charts (CIS Barómetro de Vivienda 2026, honestly captioned) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, GOLD, 2)
p.text(MX, gy + 10, "EL BARÓMETRO DE VIVIENDA DEL CIS · % que apoya cada medida", 26, "sans", True, OLIVE)
cis = [("1ª vivienda: menos impuestos", 95.4), ("Más vivienda pública", 91.4), ("Empresa pública de vivienda", 76.3), ("Limitar pisos turísticos", 75.6), ("Congelar alquileres 2 años", 70.6)]
bx1, bw_, bhh = MX, 2 * CW + GUT, 322
p.rect(bx1, gy + 28, bw_, bhh, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx1 + 22, gy + 68, "BARÓMETRO DE VIVIENDA (CIS) · apoyo a cada medida, %", 21, "sans", True, INK)
yy = gy + 96
for lab, v in cis:
    p.text(bx1 + 22, yy + 24, lab, 21, "serif", True, INK)
    p.rect(bx1 + 430, yy + 6, v * 3.2, 22, fill=OLIVE)
    p.text(bx1 + 448 + v * 3.2, yy + 24, f"{v:.1f}".replace(".", ",") + " %", 20.5, "serif", False, INK)
    yy += 31
p.para(bx1 + 22, gy + bhh - 30, "CIS, instituto público · estudio 3532 · 6.019 entrevistas · margen ±1,3 puntos · publicado el 8 de octubre. Solo se publica esta serie, con su fuente y su fecha.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right column: housing as a right
rx = COLX[2]
p.rect(rx, gy + 28, 2 * CW + GUT, bhh, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(rx + 22, gy + 68, "LA VIVIENDA: ¿DERECHO O MERCADO?", 21, "sans", True, INK)
yy = gy + 96
for lab, v in [("Preocupados por la vivienda", 86.9), ("Derecho constitucional", 79.0), ("Bien de mercado", 13.5)]:
    p.text(rx + 22, yy + 24, lab, 21, "serif", True, INK)
    p.rect(rx + 430, yy + 6, v * 3.2, 22, fill=BRICK)
    p.text(rx + 448 + v * 3.2, yy + 24, f"{v:.1f}".replace(".", ",") + " %", 20.5, "serif", False, INK)
    yy += 31
p.para(rx + 22, gy + bhh - 30, "Según el mismo barómetro: el 86,9 % está preocupado por la vivienda; el 79 % la ve como un derecho constitucional y solo el 13,5 % como un bien de mercado.", 17.5, "sans", False, GREY, 2 * CW + GUT - 44, 1.3)

# ---- P6 exercises ----
ey = 1940
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · Oefeningen van pagina 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · Niveaus door elkaar — zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LEER LOS GRÁFICOS", 25)
e.expl("Kijk naar de twee grafieken en kies het juiste antwoord.")
e.ex("B2", "Meerkeuze", "A", "De belastingverlaging heeft de meeste steun (95,4%)",
     "La medida con más apoyo es... A. bajar impuestos a la 1ª vivienda · B. limitar pisos turísticos · C. congelar alquileres", size=18.5, gap=2)
e.ex("B2", "Meerkeuze", "B", "Meer sociale woningen: 91,4% steun",
     "Construir más vivienda pública lo apoya el... A. 76,3 % · B. 91,4 % · C. 70,6 %", size=18.5, gap=2)
e.ex("B2", "Meerkeuze", "C", "Bezorgd over huisvesting: 86,9%",
     "Está preocupado por la vivienda el... A. 13,5 % · B. 79 % · C. 86,9 %", size=18.5, gap=2)
e.ex("B2", "Meerkeuze", "A", "Onderzoek onder 6.019 mensen, foutmarge ±1,3",
     "El barómetro se hizo con... A. 6.019 entrevistas · B. 5.025 entrevistas · C. 3532 entrevistas", size=18.5, gap=2)
e.ex("B2", "Meerkeuze", "B", "95,4 − 91,4 = 4,0",
     "Entre la medida más apoyada y la segunda hay... A. 19,1 puntos · B. 4,0 puntos · C. 24,8 puntos", size=18.5, gap=2)
e.ex("B2", "Meerkeuze", "C", "Deze krant publiceert alleen de CIS-huisvestingsreeks, met bron en datum",
     "La Lucerna publica aquí... A. una media mezclada · B. todos los sondeos · C. solo la serie del CIS, con fuente y fecha", size=18.5, gap=2)
e.head("B · COMPRENSIÓN", 25)
e.ex("B2", "Meerkeuze", "B", "Op 2 oktober verwierp het Congres twee huisvestingsdecreten",
     "El 2 de octubre, el Congreso... A. aprobó dos decretos · B. rechazó dos decretos de vivienda · C. disolvió las Cortes", size=18.5, gap=2)
e.ex("B2", "Meerkeuze", "A", "Op 5 oktober ontbond Sánchez de Cortes en riep verkiezingen uit",
     "El 5 de octubre, Sánchez... A. disolvió las Cortes y convocó elecciones · B. publicó las listas · C. empezó la campaña", size=18.5, gap=2)
e.ex("B2", "Meerkeuze", "C", "Een peiling is een foto met foutmarge, genomen op één bepaalde dag",
     "Según el texto, una encuesta es... A. un resultado final · B. una promesa · C. una foto con margen de error", size=18.5, gap=2)
e.ex("B2", "Meerkeuze", "B", "De campagne begint op 13 november",
     "La campaña electoral empieza el... A. 3 de noviembre · B. 13 de noviembre · C. 29 de noviembre", size=18.5, gap=2)
e.head("C · EL SUBJUNTIVO", 25)
e.ex("B2", "Zinnen aanvullen", "tenga", "es posible que + aanvoegende wijs: tenga",
     "Es posible que el CIS ___ (tener) otro método.", instr="Vul in", size=18.5, gap=2)
e.ex("B2", "Zinnen aanvullen", "sea", "es importante que + aanvoegende wijs: sea",
     "Es importante que cada gráfico ___ (ser) claro.", instr="Vul in", size=18.5, gap=2)
e.ex("B2", "Zinnen aanvullen", "para que", "para que + aanvoegende wijs (doel)",
     "Publicamos la fuente ___ todos puedan comprobarla.", instr="Vul in", size=18.5, gap=2)
e.ex("B2", "Zinnen aanvullen", "Aunque", "Aunque + aantonende wijs (bekend feit)",
     "___ las encuestas difieren, ninguna miente.", instr="Vul in", size=18.5, gap=2)
e.head("D · PALABRAS DEL DEBATE", 25)
e.expl("Vul in met de woorden: sondeo · muestra · indecisos · margen de error")
e.ex("B2", "Zinnen aanvullen", "sondeo", "sondeo = peiling",
     "Un ___ pregunta a una muestra de ciudadanos.", instr="Vul in", size=18.5, gap=2)
e.ex("B2", "Zinnen aanvullen", "muestra", "muestra = steekproef (6.019 mensen)",
     "El CIS entrevistó a una ___ de 6.019 personas.", instr="Vul in", size=18.5, gap=2)
e.ex("B2", "Zinnen aanvullen", "indecisos", "indecisos = twijfelaars",
     "Los ___ todavía no saben a quién votar.", instr="Vul in", size=18.5, gap=2)
e.ex("B2", "Zinnen aanvullen", "margen de error", "margen de error = foutmarge",
     "Toda encuesta tiene un ___.", instr="Vul in", size=18.5, gap=2)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-afondo.svg")
print("P6 saved, exercises so far:", len(REG))
