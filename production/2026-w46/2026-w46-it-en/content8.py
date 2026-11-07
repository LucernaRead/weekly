# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · Test and answers", "La Lucerna", "Page 8 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Cloze choice", "B", "St Martin = San Martino",
     "Mercoledì 11 novembre è ___. (A. Natale · B. San Martino)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "Must becomes new wine",
     "A San Martino ogni mosto diventa ___. (A. vino · B. latte)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "Italy v France is at San Siro",
     "Italia–Francia si gioca a ___. (A. San Siro · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "The chocolate festival opens on Friday",
     "Eurochocolate apre venerdì a ___. (A. Perugia · B. Cuneo)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "The torrone festival is in Cremona",
     "La Festa del Torrone continua a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "The Festival dei Popoli showed 86 films",
     "Il Festival dei Popoli ha presentato ___ film. (A. 50 · B. 86)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "Belgium v Italy is on Sunday evening",
     "Belgio–Italia si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "Scrittorincittà is in Cuneo",
     "Scrittorincittà è a ___. (A. Milano · B. Cuneo)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Multiple choice", "B", "St Martin's summer lasts three days and a little more",
     "L'estate di San Martino dura... A. un mese · B. tre giorni e un pochino · C. un'ora", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "B", "The cloak is what Martin shared with the beggar",
     "Martino divide... A. il pane · B. il mantello · C. il vino", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "A", "The chocolate festival is in its 32nd edition",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 67ª edizione", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "B", "France top the group on 10 points",
     "Nel girone di Nations League, la Francia ha... A. 7 punti · B. 10 punti · C. 0 punti", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "C", "The Alba truffle fair runs to 6 December",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "A", "The DPB went out on 15 October",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "Multiple choice", "B", "A government proposal is not yet law",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "Multiple choice", "B", "The Festival dei Popoli closed on 8 November",
     "Il Festival dei Popoli si è chiuso... A. il 31 ottobre · B. l'8 novembre · C. il 15 novembre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Cuneo: mercoledì 11 novembre va a Scrittorincittà e ascolta un autore. Paolo vive a Cremona: sabato 14 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano Belgio–Italia: è San Martino, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "Multiple choice", "B", "Giulia goes to Scrittorincittà on Wednesday",
     "Chi va a Scrittorincittà? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "A", "Paolo goes to the torrone festival on Saturday",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Cuneo · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "B", "Giulia is the one listening to the author",
     "L'autore è ascoltato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Multiple choice", "A", "The title sums up two cities, two festivals",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Make sentences", "Mercoledì è San Martino.", "Time word first",
     "mercoledì / è / San Martino → ___", instr="Reorder", size=15.5, gap=1)
f.ex("B1", "Make sentences", "Eurochocolate è a Perugia dal 13 novembre.", "Subject + essere + place + date",
     "Eurochocolate / è a Perugia / dal 13 novembre → ___", instr="Reorder", size=15.5, gap=1)
f.ex("B1", "Make sentences", "A che ora gioca l'Italia?", "Question phrase first",
     "a che ora / gioca / l'Italia / ? → ___", instr="Reorder", size=15.5, gap=1)
f.ex("B1", "Make sentences", "Il vino nuovo si assaggia in cantina.", "subject + verb + place",
     "il vino nuovo / si assaggia / in cantina → ___", instr="Reorder", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "At San Martino, grape must becomes wine.", "Compare with the original",
     "A San Martino ogni mosto diventa vino. → ___", instr="Translate into English", size=15.5, gap=1)
f.ex("B1", "翻译", "On Thursday evening, Italy play France.", "si gioca = is played",
     "Giovedì sera si gioca Italia–Francia. → ___", instr="Translate into English", size=15.5, gap=1)
f.ex("B1", "翻译", "On Sunday evening, Belgium v Italy.", "si gioca = is played",
     "Domenica sera si gioca Belgio–Italia. → ___", instr="Translate into English", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni cifra deve essere chiara.", "dovere = must",
     "Every figure must be clear. → ___", instr="Translate into Italian", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "Match words",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["la parte del sistema fiscale, un livello di reddito",
             "i soldi che pagano una misura, la sua fonte",
             "la differenza tra spese ed entrate, in rosso",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra=budget bill d", "deficit=deficit c", "copertura=funding b", "scaglione=tax bracket a"],
            instr="Match the pairs")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Cloze choice", "B", "torrone = nougat",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "mandorle = almonds",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "quanto costa? = how much?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "A", "pagare con carta = to pay by card",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Cloze choice", "B", "The torrone festival runs to 22 November",
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
f.bridge(f"Writing task (no single right answer); the model text ({NWORDS} words) follows.")
f.ex("B1", "Writing", "(open task — model text below)", f"Model text in section H below ({NWORDS} words)",
     "«La tua settimana di San Martino» Scrivi 80–100 parole: San Martino, cosa assaggi, un evento o una festa del tuo weekend.", instr="Write", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, GOLD, 2)
p.text(MX, 1382, "RISPOSTE · ANSWER KEY — grouped by page: find your exercise number", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "Each answer has a one-line note in English · ✓ = model-text task", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.14, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Writing":
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
