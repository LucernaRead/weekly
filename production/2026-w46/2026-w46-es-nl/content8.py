# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P8: 38 exercises + registry-generated answers. Dash style, as W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS · Oefeningen en antwoorden", "La Lucerna", "Pagina 8 · La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "Cloze-meerkeuze", "B", "visita a Chequia = uitwedstrijd in Tsjechië",
     "El jueves, la Roja ___ a Chequia en Praga. (A. recibe · B. visita)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "B", "recibir a Inglaterra = Engeland thuis ontvangen",
     "El domingo, España ___ a Inglaterra en Madrid. (A. visita · B. recibe)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "la lista = selectielijst",
     "De la Fuente dio ___ el viernes 6. (A. la lista · B. la huelga)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "B", "la huelga dura 24 horas = de staking duurt 24 uur",
     "La huelga del miércoles ___ 24 horas. (A. empieza · B. dura)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "empieza la campaña = de campagne begint",
     "El viernes 13 ___ la campaña electoral. (A. empieza · B. termina)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "B", "el sobre = envelop",
     "El voto por correo llega en un ___. (A. puente · B. sobre)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "Spanje–Engeland op zondag",
     "El domingo se juega el ___ en el Metropolitano. (A. España–Inglaterra · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "veranillo = nazomer",
     "En noviembre llega el ___ de San Martín. (A. veranillo · B. puente)", size=15.5, gap=1)
f.head("B · PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Meerkeuze", "B", "De algemene staking is woensdag 11 november",
     "La huelga general es el... A. lunes 9 · B. miércoles 11 · C. viernes 13", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "Sint-Maarten, 11 november",
     "San Martín es el... A. 11 de noviembre · B. 12 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "C", "Spanje–Engeland en staking, allebei deze week",
     "Esta semana hay... A. solo fútbol · B. solo huelga · C. la huelga y el España–Inglaterra", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "B", "Op het magosto eet men geroosterde kastanjes",
     "¿Qué se come en el magosto? A. flan · B. castañas asadas · C. chocolate", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "A", "Leus van de staking: lonen, huisvesting, prijzen",
     "El lema de la huelga es... A. «Salarios, vivienda y precios» · B. «Fútbol y fiesta» · C. «Cine y series»", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "C", "De verkiezingen zijn op 29 november",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "Meerkeuze", "B", "CIS-huisvestingsbarometer: 86,9% bezorgd",
     "Según el CIS de vivienda, está preocupado el... A. 13,5 % · B. 86,9 % · C. 79 %", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "A", "De campagne begint op 13 november",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C · LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el miércoles 11 sigue la huelga en las noticias y el domingo ve el España–Inglaterra en el Metropolitano. Ana vive en Barcelona: el miércoles 11 trabaja, y el domingo ve el partido por televisión. Los dos leen los programas antes de votar el 29.", 16.5, lh=1.3, split=False)
f.ex("A2", "Meerkeuze", "B", "Pablo gaat zondag naar het Metropolitano",
     "¿Quién ve el partido en el Metropolitano? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "Ana werkt op woensdag",
     "El miércoles 11, Ana... A. trabaja · B. va a la huelga · C. duerme", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "Beiden lezen eerst de programma's en stemmen dan",
     "Antes de votar, los dos... A. leen los programas · B. ven «Infamia» · C. viajan a Praga", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "B", "De titel vat het contrast tussen twee plaatsen samen",
     "El mejor título es... A. «Una tormenta» · B. «Dos miércoles» · C. «El Clásico»", size=15.5, gap=1)
f.head("D · CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Zinnen maken", "El miércoles hay huelga general.", "Onderwerp + werkwoord + plaats",
     "el miércoles / hay / huelga general → ___", instr="Zinnen maken", size=15.5, gap=1)
f.ex("A2", "Zinnen maken", "El domingo vemos el España–Inglaterra.", "De tijd vooraan",
     "el domingo / vemos / el España–Inglaterra → ___", instr="Zinnen maken", size=15.5, gap=1)
f.ex("B1", "Zinnen maken", "La campaña empieza a las cero horas.", "a las cero horas = om middernacht",
     "la campaña / empieza / a las cero horas → ___", instr="Zinnen maken", size=15.5, gap=1)
f.ex("B1", "Zinnen maken", "¿A qué hora empieza el partido?", "Het vraagwoord vooraan",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Zinnen maken", size=15.5, gap=1)
f.head("E · TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Vertalen", "Woensdag algemene staking in heel Spanje.", "Vergelijk met het origineel.",
     "El miércoles hay huelga general en toda España. → ___", instr="Vertalen", size=15.5, gap=1)
f.ex("A2", "Vertalen", "Zondag kijken wij Spanje–Engeland.", "Vergelijk met het origineel.",
     "El domingo vemos el España–Inglaterra. → ___", instr="Vertalen", size=15.5, gap=1)
f.ex("B1", "Vertalen", "El voto por correo llega a casa.", "llegar a casa = thuiskomen",
     "De stem per post komt thuis. → ___", instr="Vertalen", size=15.5, gap=1)
f.ex("B2", "Vertalen", "Cada gráfico tiene que llevar su fuente.", "tener que = moeten",
     "Elke grafiek moet de bron vermelden. → ___", instr="Vertalen", size=15.5, gap=1)
f.head("F · LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "Woorden combineren",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo=peiling c", "muestra=steekproef d", "margen de error=foutmarge b", "junta electoral=verkiezingscommissie a"],
            instr="Combineer")
f.head("G · DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "Cloze-meerkeuze", "A", "alquiler = huur",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "tres habitaciones = drie kamers",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "¿cuánto cuesta? = hoeveel kost het?",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "firmar = tekenen (een contract)",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "mudanza = verhuizing",
     "— La ___ es el miércoles 11, día de huelga. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H · ESCRIBE TÚ", 22, OLIVE, 5)
f.expl("Schrijfopdracht (geen uniek antwoord); de voorbeeldtekst (84 woorden) staat hieronder.")
f.ex("B1", "Schrijven", "Open vraag — voorbeeldtekst hieronder op deze pagina", "Voorbeeldtekst in deel H van deze pagina (84 woorden)",
     "«¿Qué harías tú por la vivienda?» Escribe 80–100 palabras: tu plan del miércoles 11, tu domingo 15 y tu voto del 29.", instr="Schrijven", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y el miércoles 11 sigo la huelga en las noticias: salarios, vivienda y precios, los tres temas de la semana. "
          "El viernes 13 empieza la campaña, y el domingo 15 veo el España–Inglaterra con mi familia. "
          "El jueves 12 veo el Chequia–España en Praga por televisión, a las 20:45. "
          "Mis amigos de Barcelona no tienen huelga en su empresa: el miércoles trabajan. Yo, en cambio, leo los programas con calma y preparo mi voto por correo. "
          "El 29 votamos. ¡Qué semana!")
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
