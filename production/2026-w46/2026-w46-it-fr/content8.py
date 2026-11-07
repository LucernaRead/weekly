# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · EXERCICES ET RÉPONSES", "La Lucerna", "Page 8 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Texte à trous", "B", "Saint-Martin = San Martino",
     "Mercoledì 11 novembre è ___. (A. Natale · B. San Martino)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "Le moût devient vin nouveau",
     "A San Martino ogni mosto diventa ___. (A. vino · B. latte)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "Italie–France à San Siro",
     "Italia–Francia si gioca a ___. (A. San Siro · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "Le festival du chocolat ouvre vendredi",
     "Eurochocolate apre venerdì a ___. (A. Perugia · B. Cuneo)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "La fête du torrone est à Crémone",
     "La Festa del Torrone continua a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "Festival dei Popoli : 86 films",
     "Il Festival dei Popoli ha presentato ___ film. (A. 50 · B. 86)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "Belgique–Italie dimanche soir",
     "Belgio–Italia si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "Scrittorincittà est à Cuneo",
     "Scrittorincittà è a ___. (A. Milano · B. Cuneo)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Choix unique", "B", "L'été de la Saint-Martin dure trois jours et un peu plus",
     "L'estate di San Martino dura... A. un mese · B. tre giorni e un pochino · C. un'ora", size=15.5, gap=1)
f.ex("A2", "Choix unique", "B", "Le manteau, Martin l'a partagé avec le mendiant",
     "Martino divide... A. il pane · B. il mantello · C. il vino", size=15.5, gap=1)
f.ex("A2", "Choix unique", "A", "Le festival du chocolat en est à sa 32e édition",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 67ª edizione", size=15.5, gap=1)
f.ex("B1", "Choix unique", "B", "Première du groupe : la France, 10 points",
     "Nel girone di Nations League, la Francia ha... A. 7 punti · B. 10 punti · C. 0 punti", size=15.5, gap=1)
f.ex("B1", "Choix unique", "C", "La foire de la truffe d'Alba dure jusqu'au 6 décembre",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "Choix unique", "A", "Le DPB est parti le 15 octobre",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "Choix unique", "B", "Une proposition du gouvernement n'est pas encore une loi",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "Choix unique", "B", "Le Festival dei Popoli s'est terminé le 8 novembre",
     "Il Festival dei Popoli si è chiuso... A. il 31 ottobre · B. l'8 novembre · C. il 15 novembre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Cuneo: mercoledì 11 novembre va a Scrittorincittà e ascolta un autore. Paolo vive a Cremona: sabato 14 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano Belgio–Italia: è San Martino, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "Choix unique", "B", "Giulia va à Scrittorincittà mercredi",
     "Chi va a Scrittorincittà? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Choix unique", "A", "Paolo va à la fête du torrone samedi",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Cuneo · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "Choix unique", "B", "C'est Giulia qui écoute l'auteur",
     "L'autore è ascoltato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Choix unique", "A", "Le titre résume deux villes, deux fêtes",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Faire des phrases", "Mercoledì è San Martino.", "Le mot de temps d'abord",
     "mercoledì / è / San Martino → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("B1", "Faire des phrases", "Eurochocolate è a Perugia dal 13 novembre.", "Sujet + essere + lieu + date",
     "Eurochocolate / è a Perugia / dal 13 novembre → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("B1", "Faire des phrases", "A che ora gioca l'Italia?", "Interrogatif d'abord",
     "a che ora / gioca / l'Italia / ? → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("B1", "Faire des phrases", "Il vino nuovo si assaggia in cantina.", "sujet + verbe + lieu",
     "il vino nuovo / si assaggia / in cantina → ___", instr="Former une phrase", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "À la Saint-Martin, le moût devient vin.", "Comparer avec l'original",
     "A San Martino ogni mosto diventa vino. → ___", instr="Traduire en français", size=15.5, gap=1)
f.ex("B1", "翻译", "Jeudi soir : Italie–France.", "si gioca = se joue",
     "Giovedì sera si gioca Italia–Francia. → ___", instr="Traduire en français", size=15.5, gap=1)
f.ex("B1", "翻译", "Dimanche soir : Belgique–Italie.", "si gioca = se joue",
     "Domenica sera si gioca Belgio–Italia. → ___", instr="Traduire en français", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni cifra deve essere chiara.", "dovere = devoir",
     "Chaque chiffre doit être clair. → ___", instr="Traduire en italien", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "Associer les mots",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["la parte del sistema fiscale, un livello di reddito",
             "i soldi che pagano una misura, la sua fonte",
             "la differenza tra spese ed entrate, in rosso",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra=loi de finances d", "deficit=déficit c", "copertura=financement b", "scaglione=tranche a"],
            instr="Associer")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Texte à trous", "B", "torrone = nougat",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "mandorle = amandes",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "quanto costa ? = combien ça coûte ?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "pagare con carta = payer par carte",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "La fête du torrone dure jusqu'au 22 novembre",
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
f.bridge(f"Exercice d'écriture (pas de réponse unique) ; le texte modèle ({NWORDS} mots) suit.")
f.ex("B1", "Écriture", "(exercice ouvert — texte modèle ci-dessous)", f"Texte modèle dans la section H ci-dessous ({NWORDS} mots)",
     "«La tua settimana di San Martino» Scrivi 80–100 parole: San Martino, cosa assaggi, un evento o una festa del tuo weekend.", instr="Écrire", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, GOLD, 2)
p.text(MX, 1382, "RISPOSTE · CORRIGÉS — classés par page, cherchez le numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "Chaque réponse est accompagnée d'une note d'une ligne en français · ✓ = exercice du texte modèle", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.14, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Écriture":
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
