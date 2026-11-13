# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-it-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE　EJERCICIOS Y RESPUESTAS", "La Lucerna", "Página 8　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Cloze", "B", "Lazio",
     "La prima in classifica è la ___. (A. Roma · B. Lazio)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "24 goles en la jornada 11",
     "L'11ª giornata ha portato ___ gol. (A. 24 · B. 31)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "El Atalanta–Inter es en Bérgamo",
     "Atalanta–Inter si gioca a ___. (A. Bergamo · B. Torino)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "La fiesta del Torrone cierra el domingo",
     "La Festa del Torrone chiude domenica a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "Cloze", "B", "El festival del chocolate es en Perugia",
     "Eurochocolate chiude a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "Cloze", "B", "La Madonna della Salute es el 21 de noviembre",
     "La Madonna della Salute si celebra il ___ novembre. (A. 20 · B. 21)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "BookCity abre el 23 de noviembre",
     "BookCity apre lunedì ___. (A. 23 novembre · B. 22 novembre)", size=15.5, gap=1)
f.ex("B1", "Cloze", "B", "El Festival de Cine de Turín abre el 24 de noviembre",
     "Il Torino Film Festival apre... A. il 20 novembre · B. il 24 novembre", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Opción múltiple", "B", "La Lazio lidera con 29 puntos",
     "La prima in classifica ha... A. 28 punti · B. 29 punti · C. 27 punti", size=15.5, gap=1)
f.ex("A2", "Opción múltiple", "B", "El Inter ganó 2–0 al Como",
     "L'Inter vince 2–0 con... A. la Roma · B. il Como · C. il Milan", size=15.5, gap=1)
f.ex("A2", "Opción múltiple", "A", "El festival del chocolate está en su 32.ª edición",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 15ª edizione", size=15.5, gap=1)
f.ex("B1", "Opción múltiple", "C", "El Udinese es colista con 5 puntos",
     "L'ultima in classifica è... A. il Monza · B. il Venezia · C. l'Udinese", size=15.5, gap=1)
f.ex("B1", "Opción múltiple", "C", "La feria de la trufa de Alba dura hasta el 6 de diciembre",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "Opción múltiple", "A", "El plazo de enmiendas vence el 17 de noviembre a las 18:00",
     "Il termine per gli emendamenti è... A. il 17 novembre · B. il 9 novembre · C. il 31 dicembre", size=15.5, gap=1)
f.ex("B2", "Opción múltiple", "B", "Una propuesta del gobierno aún no es ley",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "Opción múltiple", "B", "La Madonna della Salute nace de un voto de 1630",
     "La festa della Salute nasce da un voto del... A. 1687 · B. 1630 · C. 1898", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Venezia: sabato 21 novembre attraversa il ponte votivo e porta una candela in basilica. Paolo vive a Cremona: domenica 22 novembre guarda il corteo del Torrone e assaggia il dolce con la sua famiglia. Domenica sera, Giulia e Paolo guardano Atalanta–Inter: è la festa del torrone, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "Opción múltiple", "B", "Giulia va a la Madonna della Salute el sábado",
     "Chi va alla Madonna della Salute? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Opción múltiple", "A", "Paolo ve el desfile del Torrone el domingo",
     "Paolo, domenica, guarda... A. il corteo del Torrone · B. il ponte votivo · C. lo stadio", size=15.5, gap=1)
f.ex("A2", "Opción múltiple", "B", "La vela la lleva Giulia",
     "La candela è portata da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Opción múltiple", "A", "El título resume dos ciudades, dos fiestas",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Forma frases", "Domenica è il 22 novembre.", "La palabra de tiempo primero",
     "domenica / è / il 22 novembre → ___", instr="Forma frases", size=15.5, gap=1)
f.ex("B1", "Forma frases", "Eurochocolate chiude a Perugia il 22 novembre.", "Sujeto + verbo + lugar + fecha",
     "Eurochocolate / chiude / a Perugia / il 22 novembre → ___", instr="Forma frases", size=15.5, gap=1)
f.ex("B1", "Forma frases", "A che ora gioca la Lazio?", "El grupo interrogativo al inicio",
     "a che ora / gioca / la Lazio / ? → ___", instr="Forma frases", size=15.5, gap=1)
f.ex("B1", "Forma frases", "Il torrone si assaggia a Cremona.", "Sujeto + verbo + lugar",
     "il torrone / si assaggia / a Cremona → ___", instr="Forma frases", size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", "Traducir", "Para la Madonna della Salute, la gente cruza el puente votivo.", "Compara con el original",
     "Per la Madonna della Salute si attraversa il ponte votivo. → ___", instr="Traducir al español", size=15.5, gap=1)
f.ex("B1", "Traducir", "El domingo por la noche, el Atalanta juega contra el Inter.", "si gioca = se juega",
     "Domenica sera si gioca Atalanta–Inter. → ___", instr="Traducir al español", size=15.5, gap=1)
f.ex("B1", "Traducir", "El sábado, la Lazio juega en casa contra el Lecce.", "in casa = en casa",
     "Sabato la Lazio gioca in casa con il Lecce. → ___", instr="Traducir al español", size=15.5, gap=1)
f.ex("B2", "Traducir", "Ogni cifra deve essere chiara.", "dovere = deber",
     "Cada cifra debe ser clara. → ___", instr="Traducir al italiano", size=15.5, gap=1)
f.head("F　LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "Relaciona las palabras",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["un livello di reddito del sistema fiscale",
             "i soldi che pagano una misura",
             "la differenza tra spese ed entrate",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra = proyecto de presupuestos, d", "deficit = déficit, c", "copertura = financiación, b", "scaglione = tramo fiscal, a"],
            instr="Relaciona las palabras")
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Cloze", "B", "torrone = el turrón",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "mandorle = almendras",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "Cloze", "B", "quanto costa? = ¿cuánto cuesta?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "pagare con carta = pagar con tarjeta",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Cloze", "B", "La fiesta del Torrone dura hasta el 22 de noviembre",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 22 novembre metto la sciarpa e vado a Cremona: è l'ultimo giorno della Festa del Torrone e il corteo passa in piazza del Comune. "
          "Assaggio il torrone con la mia famiglia: preferisco quello con le mandorle e il miele, a forma di Torrazzo. "
          "La sera guardiamo Atalanta–Inter, alle 20.45, e la Lazio è ancora prima con 29 punti. "
          "Sabato, a Venezia, c'era la Madonna della Salute: il ponte votivo e le candele accese. "
          "La settimana è dolce e azzurra: torrone, cioccolato e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove della settimana.")
NWORDS = len(MODELO.split())
f.bridge(f"Tarea de escritura (sin respuesta única); texto modelo ({NWORDS} palabras) abajo.")
f.ex("B1", "Escritura", "(Tarea abierta: texto modelo abajo)", f"Texto modelo en la sección H abajo ({NWORDS} palabras)",
     "«La tua domenica del 22 novembre» Scrivi 80–100 parole: una festa, una partita, cosa assaggi.", instr="Escribir", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()
print("P8 exercises flow ends col", f.ci, "y=", f.y)
# ---- Vermeer image under the exercises flow (measured slot, col 3) ----
if f.y + 10 + 170 + 70 <= 1332:
    image(p, "lettera.jpg", COLX[3], f.y + 10, CW, 170)
    caption(p, COLX[3], f.y + 180, CW, "Una donna scrive una lettera: la scrittura è l'ultimo esercizio della settimana.",
            "Foto: Johannes Vermeer — Wikimedia Commons, dominio pubblico")
    print("P8 lettera image placed at y=", f.y + 10)
else:
    print("  !! P8 LETTERA NOSPACE: flow ends y=", f.y)

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, OLIVE, 2)
p.text(MX, 1382, "RISPOSTE　RESPUESTAS — POR PÁGINA: BUSCA TU NÚMERO", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "Cada respuesta lleva una nota de una línea en español　✓ = tarea con texto modelo", 19.5, "sans", False, GREY, anchor="end")
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
        af.para(txt, 13, lh=1.14, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-valutazione.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
