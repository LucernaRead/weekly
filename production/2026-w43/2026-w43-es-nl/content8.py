# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-es-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS · Oefeningen en antwoorden", "La Lucerna", "Pagina 8 · La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "Cloze-meerkeuze", "B", "abrir el marcador = de score openen",
     "Doué ___ el marcador en París. (A. cerró · B. abrió)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "B", "poner el 1–1 = de gelijkmaker scoren",
     "Espart ___ el 1–1 para el Barça. (A. perdió · B. puso)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "de cabeza = met een kopbal",
     "Lucas Hernández marcó el 2–1 de ___. (A. cabeza · B. penalti)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "B", "volver a + infinitief = opnieuw …",
     "Yamal ___ a empatar: 2–2. (A. salió · B. volvió)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "B", "cerrar el partido = de wedstrijd beslissen",
     "Vitinha y Fabián Ruiz ___ el 4–2 al final. (A. abrieron · B. cerraron)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "B", "derrota = de nederlaag",
     "Fue la primera ___ del Barça este año. (A. victoria · B. derrota)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "zondag wordt de Clásico gespeeld",
     "El domingo se juega el ___ en el Camp Nou. (A. Clásico · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "camiseta = het shirt",
     "El Barça lleva una ___ de GOLF WANG. (A. camiseta · B. bufanda)", size=15.5, gap=1)
f.head("B · PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Meerkeuze", "B", "zondagochtend verandert 03:00 in 02:00",
     "El cambio: a las... A. 02→03 · B. 03→02 · C. 00→01", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "op de Canarische eilanden is het een uur vroeger",
     "¿Dónde hay una hora menos? A. Canarias · B. Madrid · C. Barcelona", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "C", "de Clásico en de F1 zijn allebei om 21:00",
     "El domingo, 21:00: hay... A. solo fútbol · B. solo coches · C. los dos", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "B", "bij de Castanyada eet je panellets",
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "A", "Halloween is op zaterdag 31 oktober",
     "Halloween es... A. sáb. 31.10 · B. dom. 1.11 · C. lun. 2.11", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "C", "de verkiezingen zijn op 29 november",
     "Las elecciones generales son el... A. 29.10 · B. 1.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "Meerkeuze", "B", "de twee peilingreeksen mag je niet mengen",
     "¿Por qué no mezclamos las series? A. son secretas · B. métodos distintos · C. son viejas", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "A", "DANA Adam: eerste storm met naam van het seizoen",
     "La DANA Adam es... A. la primera tormenta con nombre · B. una fiesta gallega · C. un equipo", size=15.5, gap=1)
f.head("C · LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Lucía vive en Sevilla: el lunes 2 es festivo en Andalucía y hace puente. Marta vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El sábado por la noche, Marta celebra la Castanyada con sus amigos: castañas y panellets.", 16.5, lh=1.3, split=False)
f.ex("A2", "Meerkeuze", "B", "Andalusië staat op de lijst met vrije dagen",
     "¿Quién hace puente? A. Marta · B. Lucía · C. las dos", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "in Catalonië is maandag een werkdag",
     "El lunes 2, Marta... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "C", "bij de Castanyada eet je kastanjes en panellets",
     "¿Qué comen Marta y sus amigos? A. flores · B. dulces de Halloween · C. castañas y panellets", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "B", "de titel vat het contrast tussen de twee plaatsen samen",
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D · CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Zinnen maken", "El domingo dormimos una hora más.", "tijdsaanduiding vooraan",
     "el domingo / dormimos / una hora más → ___", instr="Zinnen maken", size=15.5, gap=1)
f.ex("A2", "Zinnen maken", "El lunes es festivo en Madrid.", "onderwerp + werkwoord + plaats",
     "el lunes / es festivo / en Madrid → ___", instr="Zinnen maken", size=15.5, gap=1)
f.ex("B1", "Zinnen maken", "El Clásico empieza a las nueve.", "a las nueve = om negen uur",
     "el Clásico / empieza / a las nueve → ___", instr="Zinnen maken", size=15.5, gap=1)
f.ex("B1", "Zinnen maken", "¿A qué hora empieza el partido?", "vraagwoord vooraan",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Zinnen maken", size=15.5, gap=1)
f.head("E · TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Vertalen", "Op zondag slapen we een uur langer.", "zie het origineel",
     "El domingo dormimos una hora más. → ___", instr="Vertalen", size=15.5, gap=1)
f.ex("A2", "Vertalen", "Maandag is een feestdag in negen autonome regio's.", "zie het origineel",
     "El lunes es festivo en nueve comunidades. → ___", instr="Vertalen", size=15.5, gap=1)
f.ex("B1", "Vertalen", "El Clásico se juega el domingo a las nueve de la noche.", "se juega = wordt gespeeld",
     "De Clásico wordt zondagavond om negen uur gespeeld. → ___", instr="Vertalen", size=15.5, gap=1)
f.ex("B2", "Vertalen", "Cada gráfico tiene que llevar su fuente.", "tener que = moeten",
     "Elke grafiek moet zijn bron vermelden. → ___", instr="Vertalen", size=15.5, gap=1)
f.head("F · LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "Woorden combineren",
            ["el sondeo", "el indeciso", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "quien aún no sabe a quién votar"],
            ["c", "d", "b", "a"],
            ["sondeo = de peiling c", "indeciso = de zwevende kiezer d", "margen de error = de foutmarge b", "junta electoral = de kiescommissie a"],
            instr="Combineer")
f.head("G · DIÁLOGO EN LA TIENDA", 22, OLIVE, 5)
f.ex("B1", "Cloze-meerkeuze", "A", "disfraz = het kostuum",
     "— Busco un ___ para mi hija. (A. disfraz · B. paraguas)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "Monster High is populair bij kinderen",
     "— Le encanta ___. (A. Monster High · B. el Samaín)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "¿cuánto cuesta? = hoeveel kost het?",
     "— ¿Cuánto ___? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "pagar = betalen",
     "— ¿Cómo va a ___: con tarjeta o en efectivo? (A. pagar · B. votar)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "Halloween valt op zaterdag",
     "— Con tarjeta. La fiesta es el ___. (A. sábado · B. lunes)", size=15.5, gap=1)
f.head("H · ESCRIBE TÚ", 22, OLIVE, 5)
f.expl("Schrijfopdracht (geen uniek antwoord); voorbeeldtekst (82 woorden) hieronder.")
f.ex("B1", "Schrijven", "(open vraag — de voorbeeldtekst staat hieronder)", "voorbeeldtekst in deel H (82 woorden)",
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del 31 y del 1, y tu lunes.", instr="Schrijven", size=15.5, gap=1)
MODELO = ("Vivo en Valencia, y aquí el lunes 2 de noviembre no es festivo: trabajo como un lunes normal. "
          "Mis amigos de Madrid sí hacen puente, ¡qué suerte! El sábado 31 celebro Halloween con mi familia, "
          "y el domingo llevamos flores al cementerio, como cada año. Por la tarde leo un libro en el sofá "
          "y preparo la semana con calma. El lunes, mientras Madrid descansa, yo abro la tienda a las nueve. "
          "No es justo… pero en diciembre, seguro, llega mi puente.")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPUESTAS · Antwoorden — per pagina gerangschikt; zoek op nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Bij elk antwoord een korte uitleg in het Nederlands · ✓ = met voorbeeldtekst", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Pagina {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schrijven":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
