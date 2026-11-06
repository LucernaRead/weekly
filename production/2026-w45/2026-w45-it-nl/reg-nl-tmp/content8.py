# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-it-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · TOETS EN ANTWOORDEN", "La Lucerna", "Pagina 8 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Meerkeuze invullen", "B", "primo freddo = de eerste kou",
     "Lunedì 2 novembre arriva il primo ___ della stagione. (A. caldo · B. freddo)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "A", "Herdenking op 2 november",
     "Il 2 novembre è la Commemorazione dei ___. (A. defunti · B. santi)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "A", "Forum Cultura opent in Milaan",
     "Il Forum Cultura apre martedì a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "A", "Panettone-finale op zaterdag en zondag",
     "La finale del Panettone è sabato e ___ a Milano. (A. domenica · B. lunedì)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "B", "Festa del Torrone in Cremona",
     "La Festa del Torrone apre a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "B", "Speelronde 11 sluit zondag: chiude",
     "L'undicesima giornata ___ domenica 8 novembre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "A", "Fiorentina–Juventus op zondagavond",
     "Fiorentina–Juventus si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "B", "Festival dei Popoli is in Florence",
     "Il Festival dei Popoli è a ___. (A. Milano · B. Firenze)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Meerkeuze", "B", "Eerste sneeuw rond 1.300–1.500 meter",
     "La prima neve leggera può cadere intorno ai... A. 500 m · B. 1.300–1.500 m · C. 3.000 m", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "B", "De bloem van 2 november is de chrysant",
     "Il fiore del 2 novembre è... A. la rosa · B. il crisantemo · C. il tulipano", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "19 landen doen mee aan de Panettone-finale",
     "Alla finale del Panettone partecipano pasticceri da... A. 19 paesi · B. 5 paesi · C. 50 paesi", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "B", "Forum Cultura: meer dan 50 evenementen",
     "Il Forum Cultura ha... A. 5 eventi · B. più di 50 eventi · C. 19 eventi", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "C", "Truffelbeurs Alba sluit op 6 december",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "A", "DPB vertrok op 15 oktober naar Brussel",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "Meerkeuze", "B", "Kans is geen zekerheid",
     "Una probabilità alta... A. è una certezza · B. non è una certezza · C. è un errore", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "B", "Lucca Comics sloot op 1 november",
     "Lucca Comics si è chiusa... A. il 28 ottobre · B. il 1° novembre · C. l'8 novembre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Milano: sabato 7 novembre va alla finale del Panettone e assaggia il panettone tradizionale. Paolo vive a Cremona: sabato 7 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano la Serie A: fa freddo, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "Meerkeuze", "B", "Giulia gaat naar de Panettone-finale in Milaan",
     "Chi va alla finale del Panettone? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "Paolo gaat zaterdag naar de Festa del Torrone",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Milano · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "B", "De traditionele panettone wordt door Giulia geproefd",
     "Il panettone tradizionale è assaggiato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "De titel vat twee steden en twee feesten samen",
     "Il titolo migliore è... A. «Due città, due dolci» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Zinnen bouwen", "Lunedì arriva il primo freddo.", "tijdwoord vooraan",
     "lunedì / arriva / il primo freddo → ___", instr="Bouw de zin", size=15.5, gap=1)
f.ex("B1", "Zinnen bouwen", "La finale è a Milano il 7 novembre.", "onderwerp + essere + plaats + datum",
     "la finale / è a Milano / il 7 novembre → ___", instr="Bouw de zin", size=15.5, gap=1)
f.ex("B1", "Zinnen bouwen", "A che ora apre il Forum Cultura?", "vraagwoordgroep vooraan",
     "a che ora / apre / il Forum Cultura / ? → ___", instr="Bouw de zin", size=15.5, gap=1)
f.ex("B1", "Zinnen bouwen", "Il freddo arriva lunedì.", "onderwerp + werkwoord + tijd",
     "il freddo / arriva / lunedì → ___", instr="Bouw de zin", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "Vertaling", "Op maandag komt de eerste kou.", "zie de originele zin",
     "Lunedì arriva il primo freddo. → ___", instr="Vertaal", size=15.5, gap=1)
f.ex("B1", "Vertaling", "Het publiek kan gratis proeven.", "assaggiare gratis = gratis proeven",
     "Il pubblico può assaggiare gratis. → ___", instr="Vertaal", size=15.5, gap=1)
f.ex("B1", "Vertaling", "Domenica sera si gioca Fiorentina–Juventus.", "si gioca = er wordt gespeeld",
     "Op zondagavond speelt Fiorentina tegen Juventus. → ___", instr="Vertaal", size=15.5, gap=1)
f.ex("B2", "Vertaling", "Ogni previsione deve essere chiara.", "dovere = moeten",
     "Elke voorspelling moet duidelijk zijn. → ___", instr="Vertaal", size=15.5, gap=1)
f.head("F · LE PAROLE DEL METEO", 22, OLIVE, 5)
f.match_set("B2", "Woorden koppelen",
            ["la probabilità", "la media", "il bollettino", "il modello"],
            ["il valore medio, tra tanti valori",
             "il documento con le previsioni più recenti",
             "il calcolo che prevede il tempo, come l'ECMWF",
             "quanto è possibile che una cosa succeda"],
            ["d", "a", "b", "c"],
            ["probabilità = kans d", "media = gemiddelde a", "bollettino = weerbericht b", "modello = weermodel c"],
            instr="Koppel woord en betekenis")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Meerkeuze invullen", "B", "torrone = noga",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "A", "mandorle: amandelen",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "B", "quanto costa? = hoeveel kost het?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "A", "pagare con carta = met kaart betalen",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Meerkeuze invullen", "B", "Festa del Torrone duurt tot 22 november",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Lunedì 2 novembre metto il cappotto e la sciarpa: arriva il primo freddo e la mattina è pungente. "
          "A scuola parliamo del Forum Cultura di Milano e del Festival dei Popoli di Firenze. "
          "Sabato assaggio il panettone con la mia famiglia: preferisco quello tradizionale, con i canditi. "
          "Domenica sera guardiamo Fiorentina–Juventus in televisione. "
          "Il freddo è arrivato, ma la settimana è dolce: cultura, dolci e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove del freddo.")
NWORDS = len(MODELO.split())
f.bridge(f"Schrijfopdracht (geen uniek antwoord); het model ({NWORDS} woorden) staat hieronder.")
f.ex("B1", "Schrijven", "(open vraag — het model staat hieronder)", f"Het model staat in sectie H van deze pagina ({NWORDS} woorden)",
     "«La tua settimana del primo freddo» Scrivi 80–100 parole: il freddo, cosa metti, un evento o una festa del tuo weekend.", instr="Schrijf", size=15.5, gap=1)
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
