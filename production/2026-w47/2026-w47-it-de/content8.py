# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-it-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE　TEST UND ANTWORTEN", "La Lucerna", "Seite 8　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Lückentext-Auswahl", "B", "Lazio",
     "La prima in classifica è la ___. (A. Roma · B. Lazio)", size=15.5, gap=1)
f.ex("B1", "Lückentext-Auswahl", "A", "24 Tore am 11. Spieltag",
     "L'11ª giornata ha portato ___ gol. (A. 24 · B. 31)", size=15.5, gap=1)
f.ex("B1", "Lückentext-Auswahl", "A", "Atalanta gegen Inter in Bergamo",
     "Atalanta–Inter si gioca a ___. (A. Bergamo · B. Torino)", size=15.5, gap=1)
f.ex("B1", "Lückentext-Auswahl", "A", "Das Torrone-Fest endet am Sonntag",
     "La Festa del Torrone chiude domenica a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "Lückentext-Auswahl", "B", "Das Schokoladenfestival ist in Perugia",
     "Eurochocolate chiude a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "Lückentext-Auswahl", "B", "Die Madonna della Salute ist am 21. November",
     "La Madonna della Salute si celebra il ___ novembre. (A. 20 · B. 21)", size=15.5, gap=1)
f.ex("B1", "Lückentext-Auswahl", "A", "BookCity eröffnet am 23. November",
     "BookCity apre lunedì ___. (A. 23 novembre · B. 22 novembre)", size=15.5, gap=1)
f.ex("B1", "Lückentext-Auswahl", "B", "Das Torino Film Festival eröffnet am 24. November",
     "Il Torino Film Festival apre... A. il 20 novembre · B. il 24 novembre", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Mehrfachauswahl", "B", "Lazio führt mit 29 Punkten",
     "La prima in classifica ha... A. 28 punti · B. 29 punti · C. 27 punti", size=15.5, gap=1)
f.ex("A2", "Mehrfachauswahl", "B", "Inter schlug Como 2:0",
     "L'Inter vince 2–0 con... A. la Roma · B. il Como · C. il Milan", size=15.5, gap=1)
f.ex("A2", "Mehrfachauswahl", "A", "Das Schokoladenfestival ist in seiner 32. Ausgabe",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 15ª edizione", size=15.5, gap=1)
f.ex("B1", "Mehrfachauswahl", "C", "Udinese ist Letzter mit 5 Punkten",
     "L'ultima in classifica è... A. il Monza · B. il Venezia · C. l'Udinese", size=15.5, gap=1)
f.ex("B1", "Mehrfachauswahl", "C", "Die Trüffelmesse in Alba läuft bis zum 6. Dezember",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "Mehrfachauswahl", "A", "Die Frist für Änderungsanträge ist der 17. November, 18 Uhr",
     "Il termine per gli emendamenti è... A. il 17 novembre · B. il 9 novembre · C. il 31 dicembre", size=15.5, gap=1)
f.ex("B2", "Mehrfachauswahl", "B", "Ein Regierungsvorschlag ist noch kein Gesetz",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "Mehrfachauswahl", "B", "Geht auf ein Gelübde von 1630 zurück",
     "La festa della Salute nasce da un voto del... A. 1687 · B. 1630 · C. 1898", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Venezia: sabato 21 novembre attraversa il ponte votivo e porta una candela in basilica. Paolo vive a Cremona: domenica 22 novembre guarda il corteo del Torrone e assaggia il dolce con la sua famiglia. Domenica sera, Giulia e Paolo guardano Atalanta–Inter: è la festa del torrone, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "Mehrfachauswahl", "B", "Giulia geht am Samstag zur Madonna della Salute",
     "Chi va alla Madonna della Salute? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Mehrfachauswahl", "A", "Paolo sieht sich am Sonntag den Torrone-Umzug an",
     "Paolo, domenica, guarda... A. il corteo del Torrone · B. il ponte votivo · C. lo stadio", size=15.5, gap=1)
f.ex("A2", "Mehrfachauswahl", "B", "Die Kerze bringt Giulia mit",
     "La candela è portata da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Mehrfachauswahl", "A", "Der Titel fasst zwei Städte und zwei Feste zusammen",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Sätze bilden", "Domenica è il 22 novembre.", "Zeitangabe zuerst",
     "domenica / è / il 22 novembre → ___", instr="Sätze bilden", size=15.5, gap=1)
f.ex("B1", "Sätze bilden", "Eurochocolate chiude a Perugia il 22 novembre.", "Subjekt + Verb + Ort + Datum",
     "Eurochocolate / chiude / a Perugia / il 22 novembre → ___", instr="Sätze bilden", size=15.5, gap=1)
f.ex("B1", "Sätze bilden", "A che ora gioca la Lazio?", "Fragewortgruppe am Satzanfang",
     "a che ora / gioca / la Lazio / ? → ___", instr="Sätze bilden", size=15.5, gap=1)
f.ex("B1", "Sätze bilden", "Il torrone si assaggia a Cremona.", "Subjekt + Verb + Ort",
     "il torrone / si assaggia / a Cremona → ___", instr="Sätze bilden", size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", "Übersetzen", "Zur Madonna della Salute überqueren die Menschen die Votivbrücke.", "Vergleiche mit dem Original",
     "Per la Madonna della Salute si attraversa il ponte votivo. → ___", instr="Ins Deutsche übersetzen", size=15.5, gap=1)
f.ex("B1", "Übersetzen", "Am Sonntagabend spielt Atalanta gegen Inter.", "wird gespielt",
     "Domenica sera si gioca Atalanta–Inter. → ___", instr="Ins Deutsche übersetzen", size=15.5, gap=1)
f.ex("B1", "Übersetzen", "Am Samstag spielt Lazio zu Hause gegen Lecce.", "zu Hause",
     "Sabato la Lazio gioca in casa con il Lecce. → ___", instr="Ins Deutsche übersetzen", size=15.5, gap=1)
f.ex("B2", "Übersetzen", "Ogni cifra deve essere chiara.", "dovere = müssen",
     "Jede Zahl muss klar sein. → ___", instr="Ins Italienische übersetzen", size=15.5, gap=1)
f.head("F　LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "Wörter zuordnen",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["un livello di reddito del sistema fiscale",
             "i soldi che pagano una misura",
             "la differenza tra spese ed entrate",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra = Haushaltsentwurf, d", "deficit = Defizit, c", "copertura = Finanzierung, b", "scaglione = Steuerstufe, a"],
            instr="Wörter zuordnen")
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Lückentext-Auswahl", "B", "torrone = Nougat",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "Lückentext-Auswahl", "A", "mandorle = Mandeln",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "Lückentext-Auswahl", "B", "quanto costa? = Wie viel kostet es?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Lückentext-Auswahl", "A", "pagare con carta = mit Karte zahlen",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Lückentext-Auswahl", "B", "Das Torrone-Fest dauert bis zum 22. November",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 22 novembre metto la sciarpa e vado a Cremona: è l'ultimo giorno della Festa del Torrone e il corteo passa in piazza del Comune. "
          "Assaggio il torrone con la mia famiglia: preferisco quello con le mandorle e il miele, a forma di Torrazzo. "
          "La sera guardiamo Atalanta–Inter, alle 20.45, e la Lazio è ancora prima con 29 punti. "
          "Sabato, a Venezia, c'era la Madonna della Salute: il ponte votivo e le candele accese. "
          "La settimana è dolce e azzurra: torrone, cioccolato e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove della settimana.")
NWORDS = len(MODELO.split())
f.bridge(f"Schreibaufgabe (keine eindeutige Antwort); Modelltext ({NWORDS} Wörter) unten.")
f.ex("B1", "Schreiben", "(Offene Aufgabe — Modelltext unten)", f"Modelltext in Abschnitt H unten ({NWORDS} Wörter)",
     "«La tua domenica del 22 novembre» Scrivi 80–100 parole: una festa, una partita, cosa assaggi.", instr="Schreiben", size=15.5, gap=1)
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
p.text(MX, 1382, "RISPOSTE　LÖSUNGEN — NACH SEITEN GEORDNET: NUMMER SUCHEN", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "Jede Antwort hat eine einzeilige Notiz auf Deutsch　✓ = Modelltext-Aufgabe", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.14, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schreiben":
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
