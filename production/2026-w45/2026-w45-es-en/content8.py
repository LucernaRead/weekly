# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-es-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS · Exercises and answers", "La Lucerna", "Page 8 · La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "Cloze choice", "B", "ganó 2–1 = won 2–1",
     "El Madrid ___ 2–1 en el Camp Nou. (A. perdió · B. ganó)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "marcar dos goles = scored two goals",
     "Mbappé ___ dos goles en Barcelona. (A. paró · B. marcó)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "primera derrota liguera = first league defeat",
     "Fue la primera ___ del Barça en la Liga. (A. derrota · B. victoria)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "recortar = to cut the gap",
     "El Madrid ___ la distancia a tres puntos. (A. aumentó · B. recortó)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "acoger = to host (the Bernabéu hosts the NFL)",
     "El Bernabéu ___ un partido de la NFL. (A. acoge · B. cierra)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "el emparrillado = the gridiron",
     "El Bernabéu cambia el césped por el ___. (A. puente · B. emparrillado)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "on Sunday it's Atlético–Barça",
     "El domingo se juega el ___ en el Metropolitano. (A. Atlético–Barça · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "himno = anthem",
     "Antes del partido suenan dos ___: el de España y el de EE. UU. (A. himnos · B. puentes)", size=15.5, gap=1)
f.head("B · PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Multiple choice", "B", "nine communities have Monday off",
     "El lunes 2 es fiesta en... A. todas · B. nueve comunidades · C. ninguna", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "A", "All Saints' Day: 1 November",
     "Todos los Santos es el... A. 1 de noviembre · B. 2 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "C", "Atlético–Barça and the NFL are both on Sunday",
     "El domingo 8 hay... A. solo fútbol · B. solo NFL · C. la NFL y el Atlético–Barça", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "B", "panellets are a Castanyada sweet",
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "A", "the DANA memorial events were on Thursday 29 October",
     "Los actos de memoria de la DANA fueron el... A. jueves 29 de octubre · B. sábado 31 · C. lunes 2", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "C", "the election is on 29 November",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "Multiple choice", "B", "CIS, October: housing at 55.7%",
     "Según el CIS de octubre, la vivienda es el principal problema para el... A. 20,9 % · B. 55,7 % · C. 17,1 %", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "A", "the campaign starts on 13 November",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C · LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el lunes 2 es festivo en su comunidad y hace puente. Ana vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El domingo por la tarde, Ana ve la NFL en televisión; por la noche, Pablo ve el Atlético–Barça.", 16.5, lh=1.3, split=False)
f.ex("A2", "Multiple choice", "B", "Madrid is on the holiday list",
     "¿Quién hace puente? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "A", "in Catalonia Monday is a working day",
     "El lunes 2, Ana... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "A", "Ana watches only the NFL; Pablo watches Atlético–Barça in the evening",
     "El domingo, Ana ve... A. solo la NFL · B. solo el Barça · C. la NFL y, por la noche, el Atlético–Barça", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "B", "the title sums up the two-city contrast",
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D · CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Sentence building", "El lunes es festivo en Madrid.", "subject + verb + place",
     "el lunes / es festivo / en Madrid → ___", instr="Build the sentence", size=15.5, gap=1)
f.ex("A2", "Sentence building", "El domingo vemos la NFL en el Bernabéu.", "time first",
     "el domingo / vemos / la NFL / en el Bernabéu → ___", instr="Build the sentence", size=15.5, gap=1)
f.ex("B1", "Sentence building", "El Atlético–Barça empieza a las nueve.", "a las nueve = at nine",
     "el Atlético–Barça / empieza / a las nueve → ___", instr="Build the sentence", size=15.5, gap=1)
f.ex("B1", "Sentence building", "¿A qué hora empieza el partido?", "the question word comes first",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Build the sentence", size=15.5, gap=1)
f.head("E · TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Translation", "Monday is a public holiday in nine communities.", "Compare with the Spanish sentence.",
     "El lunes es festivo en nueve comunidades. → ___", instr="Translate", size=15.5, gap=1)
f.ex("A2", "Translation", "On Sunday we watch the NFL and Atlético–Barça.", "Compare with the Spanish sentence.",
     "El domingo vemos la NFL y el Atlético–Barça. → ___", instr="Translate", size=15.5, gap=1)
f.ex("B1", "Translation", "El Bernabéu acoge un partido de la NFL.", "acoger = to host",
     "The Bernabéu hosts an NFL game. → ___", instr="Translate", size=15.5, gap=1)
f.ex("B2", "Translation", "Cada gráfico tiene que llevar su fuente.", "tener que = to have to, must",
     "Every chart must show its source. → ___", instr="Translate", size=15.5, gap=1)
f.head("F · LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "Vocabulary matching",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo = an opinion poll — c", "muestra = the people interviewed — d", "margen de error = margin of error — b", "junta electoral = the electoral board — a"],
            instr="Match word to definition")
f.head("G · DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "Cloze choice", "A", "alquiler = rent",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "tres habitaciones = three bedrooms",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "¿cuánto cuesta? = how much does it cost?",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "firmar = to sign (the contract)",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "mudanza = moving house",
     "— La ___ es el lunes 2, que es fiesta. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H · ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("A writing task (no single right answer); the model text (84 words) follows.")
f.ex("B1", "Writing", "(Open task — model text below)", "Model text in section H on this page (84 words)",
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del puente y tu domingo 8.", instr="Write", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y aquí el lunes 2 de noviembre sí es festivo: hago puente con mi familia. "
          "El sábado 7 vemos el Valencia–Real Madrid en televisión, y el domingo 8 tenemos dos citas: por la tarde, la NFL en el Bernabéu, y por la noche, el Atlético–Barça. "
          "Mis amigos de Barcelona no tienen puente: el lunes trabajan. Yo, en cambio, descanso un día más y preparo la semana con calma. "
          "El viernes 13 empieza la campaña, y el 29 votamos todos. ¡Qué mes!")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPUESTAS · Answer key — arranged by page; just find the number", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "One short English note per item · ✓ marks the writing task", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.12, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Writing":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.2, lh=1.12, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
