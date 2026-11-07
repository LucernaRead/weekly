# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · TOETS EN ANTWOORDEN", "La Lucerna", "Pagina 8 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Meerkeuze invullen", "B", "Sint-Maarten = San Martino",
     "Mercoledì 11 novembre è ___. (A. Natale · B. San Martino)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "A", "Most wordt nieuwe wijn",
     "A San Martino ogni mosto diventa ___. (A. vino · B. latte)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "A", "Italië–Frankrijk in San Siro",
     "Italia–Francia si gioca a ___. (A. San Siro · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "A", "Chocoladefestival opent op vrijdag",
     "Eurochocolate apre venerdì a ___. (A. Perugia · B. Cuneo)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "B", "Festa del Torrone in Cremona",
     "La Festa del Torrone continua a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "B", "Festival dei Popoli: 86 films",
     "Il Festival dei Popoli ha presentato ___ film. (A. 50 · B. 86)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "A", "België–Italië op zondagavond",
     "Belgio–Italia si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "B", "Scrittorincittà is in Cuneo",
     "Scrittorincittà è a ___. (A. Milano · B. Cuneo)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Meerkeuze", "B", "De zomer van Sint-Maarten duurt drie dagen en een beetje",
     "L'estate di San Martino dura... A. un mese · B. tre giorni e un pochino · C. un'ora", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "B", "De mantel deelde Martin met de bedelaar",
     "Martino divide... A. il pane · B. il mantello · C. il vino", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "Chocoladefestival: 32e editie",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 67ª edizione", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "B", "Poulewinnaar Frankrijk, 10 punten",
     "Nel girone di Nations League, la Francia ha... A. 7 punti · B. 10 punti · C. 0 punti", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "C", "Truffelbeurs Alba sluit op 6 december",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "A", "DPB vertrok op 15 oktober naar Brussel",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "Meerkeuze", "B", "Een regeringsvoorstel is nog geen wet",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "B", "Festival dei Popoli eindigde op 8 november",
     "Il Festival dei Popoli si è chiuso... A. il 31 ottobre · B. l'8 novembre · C. il 15 novembre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Cuneo: mercoledì 11 novembre va a Scrittorincittà e ascolta un autore. Paolo vive a Cremona: sabato 14 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano Belgio–Italia: è San Martino, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "Meerkeuze", "B", "Giulia gaat woensdag naar Scrittorincittà",
     "Chi va a Scrittorincittà? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "Paolo gaat zaterdag naar de Festa del Torrone",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Cuneo · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "B", "Giulia luistert naar de auteur",
     "L'autore è ascoltato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "De titel vat twee steden en twee feesten samen",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Zinnen bouwen", "Mercoledì è San Martino.", "tijdwoord vooraan",
     "mercoledì / è / San Martino → ___", instr="Bouw de zin", size=15.5, gap=1)
f.ex("B1", "Zinnen bouwen", "Eurochocolate è a Perugia dal 13 novembre.", "onderwerp + essere + plaats + datum",
     "Eurochocolate / è a Perugia / dal 13 novembre → ___", instr="Bouw de zin", size=15.5, gap=1)
f.ex("B1", "Zinnen bouwen", "A che ora gioca l'Italia?", "vraagwoordgroep vooraan",
     "a che ora / gioca / l'Italia / ? → ___", instr="Bouw de zin", size=15.5, gap=1)
f.ex("B1", "Zinnen bouwen", "Il vino nuovo si assaggia in cantina.", "onderwerp + werkwoord + plaats",
     "il vino nuovo / si assaggia / in cantina → ___", instr="Bouw de zin", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "Vertaling", "Met Sint-Maarten wordt most wijn.", "Vergelijk met het origineel",
     "A San Martino ogni mosto diventa vino. → ___", instr="Vertaal", size=15.5, gap=1)
f.ex("B1", "Vertaling", "Donderdagavond: Italië–Frankrijk.", "si gioca = wordt gespeeld",
     "Giovedì sera si gioca Italia–Francia. → ___", instr="Vertaal", size=15.5, gap=1)
f.ex("B1", "Vertaling", "Zondagavond: België–Italië.", "si gioca = wordt gespeeld",
     "Domenica sera si gioca Belgio–Italia. → ___", instr="Vertaal", size=15.5, gap=1)
f.ex("B2", "Vertaling", "Ogni cifra deve essere chiara.", "dovere = moeten",
     "Elk cijfer moet duidelijk zijn. → ___", instr="Vertaal", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "Woorden koppelen",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["la parte del sistema fiscale, un livello di reddito",
             "i soldi che pagano una misura, la sua fonte",
             "la differenza tra spese ed entrate, in rosso",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra=begrotingswet d", "deficit=tekort c", "copertura=dekking b", "scaglione=belastingschijf a"],
            instr="Koppel woord en betekenis")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Meerkeuze invullen", "B", "torrone = noga",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "A", "mandorle = amandelen",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "B", "quanto costa? = hoeveel kost het?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "A", "pagare con carta = met kaart betalen",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "B", "Festa del Torrone duurt tot 22 november",
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
f.bridge(f"Schrijfopdracht (geen uniek antwoord); het model ({NWORDS} woorden) staat hieronder.")
f.ex("B1", "Schrijven", "(open vraag — het model staat hieronder)", f"Het model staat in sectie H van deze pagina ({NWORDS} woorden)",
     "«La tua settimana di San Martino» Scrivi 80–100 parole: San Martino, cosa assaggi, un evento o una festa del tuo weekend.", instr="Schrijf", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, GOLD, 2)
p.text(MX, 1382, "RISPOSTE · ANTWOORDEN — per pagina gerangschikt: zoek op nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "Elke opgave heeft een korte uitleg in het Nederlands · ✓ = schrijfopgave met model", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Pagina {pg} —", 14, "sans", True, OLIVE, lh=1.14, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schrijven":
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
