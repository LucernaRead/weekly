# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-es-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS · Exercises and answers", "La Lucerna", "Page 8 · La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "Cloze choice", "B", "abrir el marcador = to open the scoring",
     "Doué ___ el marcador en París. (A. cerró · B. abrió)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "poner el 1–1 = to make it 1–1",
     "Espart ___ el 1–1 para el Barça. (A. perdió · B. puso)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "de cabeza = with a header",
     "Lucas Hernández marcó el 2–1 de ___. (A. cabeza · B. penalti)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "volver a + infinitive = to do (something) again",
     "Yamal ___ a empatar: 2–2. (A. salió · B. volvió)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "cerrar el partido = to seal the win",
     "Vitinha y Fabián Ruiz ___ el 4–2 al final. (A. abrieron · B. cerraron)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "derrota = defeat",
     "Fue la primera ___ del Barça este año. (A. victoria · B. derrota)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "the Clásico is played on Sunday",
     "El domingo se juega el ___ en el Camp Nou. (A. Clásico · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "camiseta = shirt",
     "El Barça lleva una ___ de GOLF WANG. (A. camiseta · B. bufanda)", size=15.5, gap=1)
f.head("B · PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Multiple choice", "B", "on Sunday night, 03:00 becomes 02:00",
     "El cambio: a las... A. 02→03 · B. 03→02 · C. 00→01", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "A", "the Canaries are one hour behind",
     "¿Dónde hay una hora menos? A. Canarias · B. Madrid · C. Barcelona", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "C", "El Clásico and F1 are both at 21:00",
     "El domingo, 21:00: hay... A. solo fútbol · B. solo coches · C. los dos", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "B", "panellets are the Castanyada sweet",
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "A", "Halloween is Saturday 31 October",
     "Halloween es... A. sáb. 31.10 · B. dom. 1.11 · C. lun. 2.11", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "C", "the general election is on 29 November",
     "Las elecciones generales son el... A. 29.10 · B. 1.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "Multiple choice", "B", "the two poll series must never be mixed",
     "¿Por qué no mezclamos las series? A. son secretas · B. métodos distintos · C. son viejas", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "A", "DANA Adam is the season's first named storm",
     "La DANA Adam es... A. la primera tormenta con nombre · B. una fiesta gallega · C. un equipo", size=15.5, gap=1)
f.head("C · LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Lucía vive en Sevilla: el lunes 2 es festivo en Andalucía y hace puente. Marta vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El sábado por la noche, Marta celebra la Castanyada con sus amigos: castañas y panellets.", 16.5, lh=1.3, split=False)
f.ex("A2", "Multiple choice", "B", "Andalusia is on the holiday list",
     "¿Quién hace puente? A. Marta · B. Lucía · C. las dos", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "A", "Monday is a working day in Catalonia",
     "El lunes 2, Marta... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "C", "chestnuts and panellets at the Castanyada",
     "¿Qué comen Marta y sus amigos? A. flores · B. dulces de Halloween · C. castañas y panellets", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "B", "the title sums up the two places",
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D · CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Sentence building", "El domingo dormimos una hora más.", "the time comes first",
     "el domingo / dormimos / una hora más → ___", instr="Build the sentence", size=15.5, gap=1)
f.ex("A2", "Sentence building", "El lunes es festivo en Madrid.", "subject + verb + place",
     "el lunes / es festivo / en Madrid → ___", instr="Build the sentence", size=15.5, gap=1)
f.ex("B1", "Sentence building", "El Clásico empieza a las nueve.", "a las nueve = at nine o'clock",
     "el Clásico / empieza / a las nueve → ___", instr="Build the sentence", size=15.5, gap=1)
f.ex("B1", "Sentence building", "¿A qué hora empieza el partido?", "the question word comes first",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Build the sentence", size=15.5, gap=1)
f.head("E · TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Translation", "On Sunday we sleep one hour more.", "Compare with the Spanish sentence.",
     "El domingo dormimos una hora más. → ___", instr="Translate", size=15.5, gap=1)
f.ex("A2", "Translation", "Monday is a public holiday in nine communities.", "Compare with the Spanish sentence.",
     "El lunes es festivo en nueve comunidades. → ___", instr="Translate", size=15.5, gap=1)
f.ex("B1", "Translation", "El Clásico se juega el domingo a las nueve de la noche.", "se juega = is played, kicks off",
     "El Clásico is played on Sunday at nine in the evening. → ___", instr="Translate", size=15.5, gap=1)
f.ex("B2", "Translation", "Cada gráfico tiene que llevar su fuente.", "tener que = to have to, must",
     "Every chart must give its source. → ___", instr="Translate", size=15.5, gap=1)
f.head("F · LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "Vocabulary matching",
            ["el sondeo", "el indeciso", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "quien aún no sabe a quién votar"],
            ["c", "d", "b", "a"],
            ["sondeo = an opinion poll — c", "indeciso = an undecided voter — d", "margen de error = margin of error — b", "junta electoral = the electoral board — a"],
            instr="Match word to definition")
f.head("G · DIÁLOGO EN LA TIENDA", 22, OLIVE, 5)
f.ex("B1", "Cloze choice", "A", "disfraz = costume",
     "— Busco un ___ para mi hija. (A. disfraz · B. paraguas)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "Monster High is a children's favourite",
     "— Le encanta ___. (A. Monster High · B. el Samaín)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "¿cuánto cuesta? = how much does it cost?",
     "— ¿Cuánto ___? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "pagar = to pay",
     "— ¿Cómo va a ___: con tarjeta o en efectivo? (A. pagar · B. votar)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "Halloween is on Saturday",
     "— Con tarjeta. La fiesta es el ___. (A. sábado · B. lunes)", size=15.5, gap=1)
f.head("H · ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("A writing task (no single right answer); the model text (82 words) follows.")
f.ex("B1", "Writing", "(Open task — model text below)", "Model text in section H on this page (82 words)",
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del 31 y del 1, y tu lunes.", instr="Write", size=15.5, gap=1)
MODELO = ("Vivo en Valencia, y aquí el lunes 2 de noviembre no es festivo: trabajo como un lunes normal. "
          "Mis amigos de Madrid sí hacen puente, ¡qué suerte! El sábado 31 celebro Halloween con mi familia, "
          "y el domingo llevamos flores al cementerio, como cada año. Por la tarde leo un libro en el sofá "
          "y preparo la semana con calma. El lunes, mientras Madrid descansa, yo abro la tienda a las nueve. "
          "No es justo… pero en diciembre, seguro, llega mi puente.")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPUESTAS · Answer key — arranged by page; just find the number", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Every answer with a short English note · ✓ marks the writing task", 19.5, "sans", False, GREY, anchor="end")
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
        af.para(txt, 13.2, lh=1.12, gap=0.25, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
