# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · EJERCICIOS Y RESPUESTAS", "La Lucerna", "Página 8 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Texto con huecos", "B", "San Martín = San Martino",
     "Mercoledì 11 novembre è ___. (A. Natale · B. San Martino)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "A", "El mosto se convierte en vino nuevo",
     "A San Martino ogni mosto diventa ___. (A. vino · B. latte)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "A", "Italia–Francia en San Siro",
     "Italia–Francia si gioca a ___. (A. San Siro · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "A", "El festival del chocolate abre el viernes",
     "Eurochocolate apre venerdì a ___. (A. Perugia · B. Cuneo)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "B", "La Festa del Torrone continúa en Cremona",
     "La Festa del Torrone continua a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "B", "Festival dei Popoli: 86 películas",
     "Il Festival dei Popoli ha presentato ___ film. (A. 50 · B. 86)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "A", "Bélgica–Italia el domingo por la noche",
     "Belgio–Italia si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "B", "Scrittorincittà está en Cuneo",
     "Scrittorincittà è a ___. (A. Milano · B. Cuneo)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Una opción", "B", "El verano de San Martín dura tres días y un poco más",
     "L'estate di San Martino dura... A. un mese · B. tre giorni e un pochino · C. un'ora", size=15.5, gap=1)
f.ex("A2", "Una opción", "B", "El manto, Martín lo compartió con el mendigo",
     "Martino divide... A. il pane · B. il mantello · C. il vino", size=15.5, gap=1)
f.ex("A2", "Una opción", "A", "El festival del chocolate va por su 32.ª edición",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 67ª edizione", size=15.5, gap=1)
f.ex("B1", "Una opción", "B", "Primera del grupo: Francia, 10 puntos",
     "Nel girone di Nations League, la Francia ha... A. 7 punti · B. 10 punti · C. 0 punti", size=15.5, gap=1)
f.ex("B1", "Una opción", "C", "La Feria del Tartufo de Alba cierra el 6 de diciembre",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "Una opción", "A", "El DPB partió hacia Bruselas el 15 de octubre",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "Una opción", "B", "Una propuesta del gobierno aún no es ley",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "Una opción", "B", "El Festival dei Popoli terminó el 8 de noviembre",
     "Il Festival dei Popoli si è chiuso... A. il 31 ottobre · B. l'8 novembre · C. il 15 novembre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Cuneo: mercoledì 11 novembre va a Scrittorincittà e ascolta un autore. Paolo vive a Cremona: sabato 14 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano Belgio–Italia: è San Martino, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "Una opción", "B", "Giulia va a Scrittorincittà el miércoles",
     "Chi va a Scrittorincittà? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Una opción", "A", "Paolo va el sábado a la Festa del Torrone",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Cuneo · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "Una opción", "B", "Giulia es quien escucha al autor",
     "L'autore è ascoltato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Una opción", "A", "El mejor título: dos ciudades, dos fiestas",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Formar frases", "Mercoledì è San Martino.", "El tiempo va primero",
     "mercoledì / è / San Martino → ___", instr="Formar frases", size=15.5, gap=1)
f.ex("B1", "Formar frases", "Eurochocolate è a Perugia dal 13 novembre.", "Sujeto + essere + lugar",
     "Eurochocolate / è a Perugia / dal 13 novembre → ___", instr="Formar frases", size=15.5, gap=1)
f.ex("B1", "Formar frases", "A che ora gioca l'Italia?", "Interrogación primero",
     "a che ora / gioca / l'Italia / ? → ___", instr="Formar frases", size=15.5, gap=1)
f.ex("B1", "Formar frases", "Il vino nuovo si assaggia in cantina.", "sujeto + verbo + lugar",
     "il vino nuovo / si assaggia / in cantina → ___", instr="Formar frases", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "En San Martín, el mosto se convierte en vino.", "Comparar con el original",
     "A San Martino ogni mosto diventa vino. → ___", instr="Traduce", size=15.5, gap=1)
f.ex("B1", "翻译", "El jueves por la noche: Italia–Francia.", "si gioca = se juega",
     "Giovedì sera si gioca Italia–Francia. → ___", instr="Traduce", size=15.5, gap=1)
f.ex("B1", "翻译", "El domingo por la noche: Bélgica–Italia.", "si gioca = se juega",
     "Domenica sera si gioca Belgio–Italia. → ___", instr="Traduce", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni cifra deve essere chiara.", "dovere = deber",
     "Cada cifra debe ser clara. → ___", instr="Traduce", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "Emparejar palabras",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["la parte del sistema fiscale, un livello di reddito",
             "i soldi che pagano una misura, la sua fonte",
             "la differenza tra spese ed entrate, in rosso",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra=ley de presupuestos d", "deficit=déficit c", "copertura=financiación b", "scaglione=tramo a"],
            instr="Emparejar")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Texto con huecos", "B", "torrone = turrón",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "A", "mandorle = almendras",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "B", "quanto costa? = ¿cuánto cuesta?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "A", "pagare con carta = pagar con tarjeta",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Texto con huecos", "B", "La fiesta dura hasta el 22 de noviembre",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Mercoledì 11 novembre metto la sciarpa e vado in cantina: è San Martino e il vino nuovo si assaggia. "
          "A scuola parliamo della leggenda del mantello diviso e dell'estate di tre giorni. "
          "Sabato assaggio il torrone con la mia famiglia: preferisco quello di Cremona, con le mandorle e il miele. "
          "Giovedì sera guardiamo Italia–Francia in televisione, alle 20.45. "
          "Domenica, poi, il Belgio: due notti azzurre in una settimana. "
          "San Martino è arrivato, ma la settimana è dolce: vino nuovo, castagne e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove di San Martino.")
NWORDS = len(MODELO.split())
f.bridge(f"Ejercicio de escritura (sin respuesta única); el modelo ({NWORDS} palabras) está abajo.")
f.ex("B1", "Escritura", "(Tarea abierta, modelo abajo)", f"El modelo está en la sección H ({NWORDS} palabras)",
     "«La tua settimana di San Martino» Scrivi 80–100 parole: San Martino, cosa assaggi, un evento o una festa del tuo weekend.", instr="Escritura", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, GOLD, 2)
p.text(MX, 1382, "RISPOSTE · RESPUESTAS — por página, busca el número del ejercicio", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "Cada respuesta lleva una nota breve · ✓ marca el ejercicio de escritura", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.14, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Escritura":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 12.5, lh=1.12, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-valutazione.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
