# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P8: 38 exercises + registry-generated answers. Dash style, as W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS　Exercises and answers", "La Lucerna", "Page 8　La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "Cloze choice", "B", "visita a Chequia = away at Czechia",
     "El jueves, la Roja ___ a Chequia en Praga. (A. recibe · B. visita)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "recibir a Inglaterra = at home to England",
     "El domingo, España ___ a Inglaterra en Madrid. (A. visita · B. recibe)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "la lista = squad list",
     "De la Fuente dio ___ el viernes 6. (A. la lista · B. la huelga)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "la huelga dura 24 horas = the strike lasts 24 hours",
     "La huelga del miércoles ___ 24 horas. (A. empieza · B. dura)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "empieza la campaña = the campaign begins",
     "El viernes 13 ___ la campaña electoral. (A. empieza · B. termina)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "el sobre = envelope",
     "El voto por correo llega en un ___. (A. puente · B. sobre)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "Spain–England on Sunday",
     "El domingo se juega el ___ en el Metropolitano. (A. España–Inglaterra · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "veranillo = little summer",
     "En noviembre llega el ___ de San Martín. (A. veranillo · B. puente)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Multiple choice", "B", "The general strike is on Wednesday 11 November",
     "La huelga general es el... A. lunes 9 · B. miércoles 11 · C. viernes 13", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "A", "St Martin's Day, 11 November",
     "San Martín es el... A. 11 de noviembre · B. 12 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "C", "Spain–England and the strike are both this week",
     "Esta semana hay... A. solo fútbol · B. solo huelga · C. la huelga y el España–Inglaterra", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "B", "At the magosto we eat roast chestnuts",
     "¿Qué se come en el magosto? A. flan · B. castañas asadas · C. chocolate", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "A", "The strike slogan: wages, housing, prices",
     "El lema de la huelga es... A. «Salarios, vivienda y precios» · B. «Fútbol y fiesta» · C. «Cine y series»", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "C", "The election is on 29 November",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "Multiple choice", "B", "CIS housing barometer: 86.9% worried about housing",
     "Según el CIS de vivienda, está preocupado el... A. 13,5 % · B. 86,9 % · C. 79 %", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "A", "The campaign starts on 13 November",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el miércoles 11 sigue la huelga en las noticias y el domingo ve el España–Inglaterra en el Metropolitano. Ana vive en Barcelona: el miércoles 11 trabaja, y el domingo ve el partido por televisión. Los dos leen los programas antes de votar el 29.", 16.5, lh=1.3, split=False)
f.ex("A2", "Multiple choice", "B", "Pablo goes to the Metropolitano on Sunday",
     "¿Quién ve el partido en el Metropolitano? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "A", "Ana works on Wednesday",
     "El miércoles 11, Ana... A. trabaja · B. va a la huelga · C. duerme", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "A", "Both read the manifestos before voting",
     "Antes de votar, los dos... A. leen los programas · B. ven «Infamia» · C. viajan a Praga", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "B", "The title sums up the two-place contrast",
     "El mejor título es... A. «Una tormenta» · B. «Dos miércoles» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Sentence building", "El miércoles hay huelga general.", "Subject + verb + place",
     "el miércoles / hay / huelga general → ___", instr="Build the sentence", size=15.5, gap=1)
f.ex("A2", "Sentence building", "El domingo vemos el España–Inglaterra.", "Time first",
     "el domingo / vemos / el España–Inglaterra → ___", instr="Build the sentence", size=15.5, gap=1)
f.ex("B1", "Sentence building", "La campaña empieza a las cero horas.", "a las cero horas = at midnight",
     "la campaña / empieza / a las cero horas → ___", instr="Build the sentence", size=15.5, gap=1)
f.ex("B1", "Sentence building", "¿A qué hora empieza el partido?", "The question word comes first",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Build the sentence", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Translation", "There is a general strike all over Spain on Wednesday.", "Compare with the original.",
     "El miércoles hay huelga general en toda España. → ___", instr="Translate", size=15.5, gap=1)
f.ex("A2", "Translation", "On Sunday we watch Spain–England.", "Compare with the original.",
     "El domingo vemos el España–Inglaterra. → ___", instr="Translate", size=15.5, gap=1)
f.ex("B1", "Translation", "El voto por correo llega a casa.", "llegar a casa = to arrive at home",
     "The postal vote arrives at home. → ___", instr="Translate", size=15.5, gap=1)
f.ex("B2", "Translation", "Cada gráfico tiene que llevar su fuente.", "tener que = must",
     "Every chart must show its source. → ___", instr="Translate", size=15.5, gap=1)
f.head("F　LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "Vocabulary matching",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo=poll c", "muestra=sample d", "margen de error=margin of error b", "junta electoral=electoral board a"],
            instr="Match word to definition")
f.head("G　DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "Cloze choice", "A", "alquiler = rent",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "tres habitaciones = three bedrooms",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "¿cuánto cuesta? = how much does it cost?",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "firmar = to sign (a contract)",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "mudanza = house move",
     "— La ___ es el miércoles 11, día de huelga. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("A writing task (no single right answer); the model text (84 words) is below.")
f.ex("B1", "Writing", "(open question — the model text follows)", "Model text in section H on this page (84 words)",
     "«¿Qué harías tú por la vivienda?» Escribe 80–100 palabras: tu plan del miércoles 11, tu domingo 15 y tu voto del 29.", instr="Write", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y el miércoles 11 sigo la huelga en las noticias: salarios, vivienda y precios, los tres temas de la semana. "
          "El viernes 13 empieza la campaña, y el domingo 15 veo el España–Inglaterra con mi familia. "
          "El jueves 12 veo el Chequia–España en Praga por televisión, a las 20:45. "
          "Mis amigos de Barcelona no tienen huelga en su empresa: el miércoles trabajan. Yo, en cambio, leo los programas con calma y preparo mi voto por correo. "
          "El 29 votamos. ¡Qué semana!")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPUESTAS　Answer key — arranged by page; just find the number", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "One short English note per item　✓ marks the writing task", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
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
