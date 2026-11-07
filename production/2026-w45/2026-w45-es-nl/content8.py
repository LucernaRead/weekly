# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-es-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS · Oefeningen en antwoorden", "La Lucerna", "Pagina 8 · La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "Cloze-meerkeuze", "B", "ganó 2–1 = won met 2–1",
     "El Madrid ___ 2–1 en el Camp Nou. (A. perdió · B. ganó)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "B", "marcar dos goles = scoorde twee doelpunten",
     "Mbappé ___ dos goles en Barcelona. (A. paró · B. marcó)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "primera derrota liguera = eerste competitienederlaag",
     "Fue la primera ___ del Barça en la Liga. (A. derrota · B. victoria)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "B", "recortar = de achterstand verkleinen",
     "El Madrid ___ la distancia a tres puntos. (A. aumentó · B. recortó)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "acoger = organiseren (het Bernabéu organiseert de NFL)",
     "El Bernabéu ___ un partido de la NFL. (A. acoge · B. cierra)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "B", "el emparrillado = het gridiron",
     "El Bernabéu cambia el césped por el ___. (A. puente · B. emparrillado)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "zondag is het Atlético–Barça",
     "El domingo se juega el ___ en el Metropolitano. (A. Atlético–Barça · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "himno = volkslied",
     "Antes del partido suenan dos ___: el de España y el de EE. UU. (A. himnos · B. puentes)", size=15.5, gap=1)
f.head("B · PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Meerkeuze", "B", "negen regio's hebben maandag vrij",
     "El lunes 2 es fiesta en... A. todas · B. nueve comunidades · C. ninguna", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "Allerheiligen: 1 november",
     "Todos los Santos es el... A. 1 de noviembre · B. 2 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "C", "Atlético–Barça en de NFL zijn beide op zondag",
     "El domingo 8 hay... A. solo fútbol · B. solo NFL · C. la NFL y el Atlético–Barça", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "B", "panellets horen bij de Castanyada",
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "A", "de DANA-herdenking was op donderdag 29 oktober",
     "Los actos de memoria de la DANA fueron el... A. jueves 29 de octubre · B. sábado 31 · C. lunes 2", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "C", "de verkiezingen zijn op 29 november",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "Meerkeuze", "B", "CIS, oktober: huisvesting 55,7%",
     "Según el CIS de octubre, la vivienda es el principal problema para el... A. 20,9 % · B. 55,7 % · C. 17,1 %", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "A", "de campagne begint op 13 november",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C · LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el lunes 2 es festivo en su comunidad y hace puente. Ana vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El domingo por la tarde, Ana ve la NFL en televisión; por la noche, Pablo ve el Atlético–Barça.", 16.5, lh=1.3, split=False)
f.ex("A2", "Meerkeuze", "B", "Madrid staat op de feestdagenlijst",
     "¿Quién hace puente? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "in Catalonië is maandag een werkdag",
     "El lunes 2, Ana... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "Ana: alleen NFL; Pablo: Atlético–Barça 's avonds",
     "El domingo, Ana ve... A. solo la NFL · B. solo el Barça · C. la NFL y, por la noche, el Atlético–Barça", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "B", "de titel vat het contrast tussen twee steden samen",
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D · CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Zinnen maken", "El lunes es festivo en Madrid.", "onderwerp + werkwoord + plaats",
     "el lunes / es festivo / en Madrid → ___", instr="Zinnen maken", size=15.5, gap=1)
f.ex("A2", "Zinnen maken", "El domingo vemos la NFL en el Bernabéu.", "tijd eerst",
     "el domingo / vemos / la NFL / en el Bernabéu → ___", instr="Zinnen maken", size=15.5, gap=1)
f.ex("B1", "Zinnen maken", "El Atlético–Barça empieza a las nueve.", "a las nueve = om negen uur",
     "el Atlético–Barça / empieza / a las nueve → ___", instr="Zinnen maken", size=15.5, gap=1)
f.ex("B1", "Zinnen maken", "¿A qué hora empieza el partido?", "het vraagwoord staat vooraan",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Zinnen maken", size=15.5, gap=1)
f.head("E · TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Vertalen", "Maandag is een feestdag in negen autonome regio's.", "zie het origineel",
     "El lunes es festivo en nueve comunidades. → ___", instr="Vertalen", size=15.5, gap=1)
f.ex("A2", "Vertalen", "Op zondag kijken we naar de NFL en Atlético–Barça.", "zie het origineel",
     "El domingo vemos la NFL y el Atlético–Barça. → ___", instr="Vertalen", size=15.5, gap=1)
f.ex("B1", "Vertalen", "El Bernabéu acoge un partido de la NFL.", "acoger = organiseren",
     "Het Bernabéu organiseert een NFL-wedstrijd. → ___", instr="Vertalen", size=15.5, gap=1)
f.ex("B2", "Vertalen", "Cada gráfico tiene que llevar su fuente.", "tener que = moeten",
     "Elke grafiek moet zijn bron vermelden. → ___", instr="Vertalen", size=15.5, gap=1)
f.head("F · LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "Woorden combineren",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo = een opiniepeiling — c", "muestra = de geïnterviewden — d", "margen de error = foutmarge — b", "junta electoral = het stembureau — a"],
            instr="Combineer")
f.head("G · DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "Cloze-meerkeuze", "A", "alquiler = huur",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "tres habitaciones = drie slaapkamers",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "¿cuánto cuesta? = hoeveel kost het?",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "firmar = tekenen (het contract)",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "mudanza = verhuizen",
     "— La ___ es el lunes 2, que es fiesta. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H · ESCRIBE TÚ", 22, OLIVE, 5)
f.expl("Schrijfopdracht (geen uniek antwoord); voorbeeldtekst (84 woorden) hieronder.")
f.ex("B1", "Schrijven", "(open vraag — de voorbeeldtekst staat hieronder)", "voorbeeldtekst in deel H (84 woorden)",
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del puente y tu domingo 8.", instr="Schrijven", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y aquí el lunes 2 de noviembre sí es festivo: hago puente con mi familia. "
          "El sábado 7 vemos el Valencia–Real Madrid en televisión, y el domingo 8 tenemos dos citas: por la tarde, la NFL en el Bernabéu, y por la noche, el Atlético–Barça. "
          "Mis amigos de Barcelona no tienen puente: el lunes trabajan. Yo, en cambio, descanso un día más y preparo la semana con calma. "
          "El viernes 13 empieza la campaña, y el 29 votamos todos. ¡Qué mes!")
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
    af.para(f"— Pagina {pg} —", 14, "sans", True, OLIVE, lh=1.12, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schrijven":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.2, lh=1.12, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
