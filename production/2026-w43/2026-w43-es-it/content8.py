# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-es-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS · ESERCIZI E RISPOSTE", "La Lucerna", "Pagina 8 · La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "abrir el marcador = segnare il primo gol",
     "Doué ___ el marcador en París. (A. cerró · B. abrió)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "poner el 1–1 = segnare il gol del pareggio",
     "Espart ___ el 1–1 para el Barça. (A. perdió · B. puso)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "de cabeza = di testa",
     "Lucas Hernández marcó el 2–1 de ___. (A. cabeza · B. penalti)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "volver a + infinito = di nuovo…",
     "Yamal ___ a empatar: 2–2. (A. salió · B. volvió)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "cerrar el partido = chiudere la partita",
     "Vitinha y Fabián Ruiz ___ el 4–2 al final. (A. abrieron · B. cerraron)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "derrota = sconfitta",
     "Fue la primera ___ del Barça este año. (A. victoria · B. derrota)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "domenica si gioca il Clásico",
     "El domingo se juega el ___ en el Camp Nou. (A. Clásico · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "camiseta = maglia",
     "El Barça lleva una ___ de GOLF WANG. (A. camiseta · B. bufanda)", size=15.5, gap=1)
f.head("B · PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "domenica all'alba: dalle 03:00 alle 02:00",
     "El cambio: a las... A. 02→03 · B. 03→02 · C. 00→01", size=15.5, gap=1)
f.ex("A2", "单选", "A", "alle Canarie c'è un'ora in meno",
     "¿Dónde hay una hora menos? A. Canarias · B. Madrid · C. Barcelona", size=15.5, gap=1)
f.ex("A2", "单选", "C", "il Clásico e la F1, entrambi alle 21:00",
     "El domingo, 21:00: hay... A. solo fútbol · B. solo coches · C. los dos", size=15.5, gap=1)
f.ex("B1", "单选", "B", "alla Castanyada si mangiano i panellets",
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", "单选", "A", "Halloween è sabato 31 ottobre",
     "Halloween es... A. sáb. 31.10 · B. dom. 1.11 · C. lun. 2.11", size=15.5, gap=1)
f.ex("B1", "单选", "C", "le elezioni generali sono il 29 novembre",
     "Las elecciones generales son el... A. 29.10 · B. 1.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "单选", "B", "le due serie di sondaggi non si possono mescolare",
     "¿Por qué no mezclamos las series? A. son secretas · B. métodos distintos · C. son viejas", size=15.5, gap=1)
f.ex("B1", "单选", "A", "la DANA Adam è la prima tempesta con nome della stagione",
     "La DANA Adam es... A. la primera tormenta con nombre · B. una fiesta gallega · C. un equipo", size=15.5, gap=1)
f.head("C · LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Lucía vive en Sevilla: el lunes 2 es festivo en Andalucía y hace puente. Marta vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El sábado por la noche, Marta celebra la Castanyada con sus amigos: castañas y panellets.", 16.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "l'Andalusia è tra le comunità in festa",
     "¿Quién hace puente? A. Marta · B. Lucía · C. las dos", size=15.5, gap=1)
f.ex("A2", "单选", "A", "in Catalogna il lunedì 2 si lavora",
     "El lunes 2, Marta... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", "单选", "C", "alla Castanyada: castagne e panellets",
     "¿Qué comen Marta y sus amigos? A. flores · B. dulces de Halloween · C. castañas y panellets", size=15.5, gap=1)
f.ex("A2", "单选", "B", "il titolo migliore riassume i due lunedì diversi",
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D · CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Costruisci", "El domingo dormimos una hora más.", "il tempo va all'inizio",
     "el domingo / dormimos / una hora más → ___", instr="Costruisci", size=15.5, gap=1)
f.ex("A2", "Costruisci", "El lunes es festivo en Madrid.", "soggetto + verbo + luogo",
     "el lunes / es festivo / en Madrid → ___", instr="Costruisci", size=15.5, gap=1)
f.ex("B1", "Costruisci", "El Clásico empieza a las nueve.", "a las nueve = alle nove",
     "el Clásico / empieza / a las nueve → ___", instr="Costruisci", size=15.5, gap=1)
f.ex("B1", "Costruisci", "¿A qué hora empieza el partido?", "l'interrogativa va all'inizio",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Costruisci", size=15.5, gap=1)
f.head("E · TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Traduci", "La domenica dormiamo un'ora in più.", "confronta con l'originale",
     "El domingo dormimos una hora más. → ___", instr="Traduci", size=15.5, gap=1)
f.ex("A2", "Traduci", "Il lunedì è festivo in nove comunità.", "confronta con l'originale",
     "El lunes es festivo en nueve comunidades. → ___", instr="Traduci", size=15.5, gap=1)
f.ex("B1", "Traduci", "El Clásico se juega el domingo a las nueve de la noche.", "se juega = si gioca, si disputa",
     "Il Clásico si gioca domenica alle nove di sera. → ___", instr="Traduci", size=15.5, gap=1)
f.ex("B2", "Traduci", "Cada gráfico tiene que llevar su fuente.", "tener que = dovere",
     "Ogni grafico deve indicare la sua fonte. → ___", instr="Traduci", size=15.5, gap=1)
f.head("F · LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["el sondeo", "el indeciso", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "quien aún no sabe a quién votar"],
            ["c", "d", "b", "a"],
            ["sondeo = sondaggio (c)", "indeciso = chi non ha ancora deciso (d)", "margen de error = margine di errore (b)", "junta electoral = commissione elettorale (a)"],
            instr="Abbina le parole")
f.head("G · DIÁLOGO EN LA TIENDA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "A", "disfraz = costume",
     "— Busco un ___ para mi hija. (A. disfraz · B. paraguas)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "Monster High è il preferito dei bambini",
     "— Le encanta ___. (A. Monster High · B. el Samaín)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "¿cuánto cuesta? = quanto costa?",
     "— ¿Cuánto ___? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "pagar = pagare",
     "— ¿Cómo va a ___: con tarjeta o en efectivo? (A. pagar · B. votar)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "Halloween è di sabato",
     "— Con tarjeta. La fiesta es el ___. (A. sábado · B. lunes)", size=15.5, gap=1)
f.head("H · ESCRIBE TÚ", 22, OLIVE, 5)
f.expl("Esercizio di scrittura (senza una risposta unica); il testo modello (82 parole) è qui sotto.")
f.ex("B1", "Scrivi", "(domanda aperta — il modello è qui sotto)", "Il modello è nella sezione H di questa pagina (82 parole)",
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del 31 y del 1, y tu lunes.", instr="Scrivi", size=15.5, gap=1)
MODELO = ("Vivo en Valencia, y aquí el lunes 2 de noviembre no es festivo: trabajo como un lunes normal. "
          "Mis amigos de Madrid sí hacen puente, ¡qué suerte! El sábado 31 celebro Halloween con mi familia, "
          "y el domingo llevamos flores al cementerio, como cada año. Por la tarde leo un libro en el sofá "
          "y preparo la semana con calma. El lunes, mientras Madrid descansa, yo abro la tienda a las nueve. "
          "No es justo… pero en diciembre, seguro, llega mi puente.")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPUESTAS · LE RISPOSTE — ordinate per pagina: cerca il numero", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Una nota in italiano per ogni risposta · ✓ = testo modello", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Scrivi":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
