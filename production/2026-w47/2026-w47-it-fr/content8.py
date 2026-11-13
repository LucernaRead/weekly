# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-it-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE　EXERCICES ET RÉPONSES", "La Lucerna", "Page 8　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Texte à trous", "B", "Lazio",
     "La prima in classifica è la ___. (A. Roma · B. Lazio)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "24 buts lors de la 11e journée",
     "L'11ª giornata ha portato ___ gol. (A. 24 · B. 31)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "Atalanta–Inter se joue à Bergame",
     "Atalanta–Inter si gioca a ___. (A. Bergamo · B. Torino)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "La fête du Torrone se termine dimanche",
     "La Festa del Torrone chiude domenica a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "Le festival du chocolat est à Pérouse",
     "Eurochocolate chiude a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "La Madonna della Salute est le 21 novembre",
     "La Madonna della Salute si celebra il ___ novembre. (A. 20 · B. 21)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "BookCity ouvre le 23 novembre",
     "BookCity apre lunedì ___. (A. 23 novembre · B. 22 novembre)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "Le Torino Film Festival ouvre le 24 novembre",
     "Il Torino Film Festival apre... A. il 20 novembre · B. il 24 novembre", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Choix multiple", "B", "La Lazio est première avec 29 points",
     "La prima in classifica ha... A. 28 punti · B. 29 punti · C. 27 punti", size=15.5, gap=1)
f.ex("A2", "Choix multiple", "B", "L'Inter a battu Côme 2–0",
     "L'Inter vince 2–0 con... A. la Roma · B. il Como · C. il Milan", size=15.5, gap=1)
f.ex("A2", "Choix multiple", "A", "Le festival du chocolat en est à sa 32e édition",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 15ª edizione", size=15.5, gap=1)
f.ex("B1", "Choix multiple", "C", "L'Udinese est dernière avec 5 points",
     "L'ultima in classifica è... A. il Monza · B. il Venezia · C. l'Udinese", size=15.5, gap=1)
f.ex("B1", "Choix multiple", "C", "La foire de la truffe d'Alba dure jusqu'au 6 décembre",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "Choix multiple", "A", "La date limite des amendements est le 17 novembre à 18 h",
     "Il termine per gli emendamenti è... A. il 17 novembre · B. il 9 novembre · C. il 31 dicembre", size=15.5, gap=1)
f.ex("B2", "Choix multiple", "B", "Une proposition du gouvernement n'est pas encore une loi",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "Choix multiple", "B", "La Madonna della Salute vient d'un vœu de 1630",
     "La festa della Salute nasce da un voto del... A. 1687 · B. 1630 · C. 1898", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Venezia: sabato 21 novembre attraversa il ponte votivo e porta una candela in basilica. Paolo vive a Cremona: domenica 22 novembre guarda il corteo del Torrone e assaggia il dolce con la sua famiglia. Domenica sera, Giulia e Paolo guardano Atalanta–Inter: è la festa del torrone, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "Choix multiple", "B", "Giulia va à la Madonna della Salute samedi",
     "Chi va alla Madonna della Salute? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Choix multiple", "A", "Paolo regarde le cortège du Torrone dimanche",
     "Paolo, domenica, guarda... A. il corteo del Torrone · B. il ponte votivo · C. lo stadio", size=15.5, gap=1)
f.ex("A2", "Choix multiple", "B", "La bougie est apportée par Giulia",
     "La candela è portata da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Choix multiple", "A", "Le titre résume deux villes, deux fêtes",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Forme des phrases", "Domenica è il 22 novembre.", "Le mot de temps d'abord",
     "domenica / è / il 22 novembre → ___", instr="Forme des phrases", size=15.5, gap=1)
f.ex("B1", "Forme des phrases", "Eurochocolate chiude a Perugia il 22 novembre.", "Sujet + verbe + lieu + date",
     "Eurochocolate / chiude / a Perugia / il 22 novembre → ___", instr="Forme des phrases", size=15.5, gap=1)
f.ex("B1", "Forme des phrases", "A che ora gioca la Lazio?", "Le groupe interrogatif en tête",
     "a che ora / gioca / la Lazio / ? → ___", instr="Forme des phrases", size=15.5, gap=1)
f.ex("B1", "Forme des phrases", "Il torrone si assaggia a Cremona.", "Sujet + verbe + lieu",
     "il torrone / si assaggia / a Cremona → ___", instr="Forme des phrases", size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", "Traduire", "Pour la Madonna della Salute, on traverse le pont votif.", "Compare avec l'original",
     "Per la Madonna della Salute si attraversa il ponte votivo. → ___", instr="Traduire en français", size=15.5, gap=1)
f.ex("B1", "Traduire", "Dimanche soir, l'Atalanta joue contre l'Inter.", "si gioca = se joue",
     "Domenica sera si gioca Atalanta–Inter. → ___", instr="Traduire en français", size=15.5, gap=1)
f.ex("B1", "Traduire", "Samedi, la Lazio joue à domicile contre Lecce.", "in casa = à domicile",
     "Sabato la Lazio gioca in casa con il Lecce. → ___", instr="Traduire en français", size=15.5, gap=1)
f.ex("B2", "Traduire", "Ogni cifra deve essere chiara.", "dovere = devoir",
     "Chaque chiffre doit être clair. → ___", instr="Traduire en italien", size=15.5, gap=1)
f.head("F　LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "Associe les mots",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["un livello di reddito del sistema fiscale",
             "i soldi che pagano una misura",
             "la differenza tra spese ed entrate",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra = projet de budget, d", "deficit = déficit, c", "copertura = financement, b", "scaglione = tranche fiscale, a"],
            instr="Associe mots et définitions")
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Texte à trous", "B", "torrone = le nougat",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "mandorle = amandes",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "quanto costa? = combien ça coûte ?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "pagare con carta = payer par carte",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "La fête du Torrone dure jusqu'au 22 novembre",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 22 novembre metto la sciarpa e vado a Cremona: è l'ultimo giorno della Festa del Torrone e il corteo passa in piazza del Comune. "
          "Assaggio il torrone con la mia famiglia: preferisco quello con le mandorle e il miele, a forma di Torrazzo. "
          "La sera guardiamo Atalanta–Inter, alle 20.45, e la Lazio è ancora prima con 29 punti. "
          "Sabato, a Venezia, c'era la Madonna della Salute: il ponte votivo e le candele accese. "
          "La settimana è dolce e azzurra: torrone, cioccolato e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove della settimana.")
NWORDS = len(MODELO.split())
f.bridge(f"Tâche de rédaction (pas de réponse unique) ; texte modèle ({NWORDS} mots) ci-dessous.")
f.ex("B1", "Rédaction", "(Tâche ouverte — texte modèle ci-dessous)", f"Texte modèle en section H ci-dessous ({NWORDS} mots)",
     "«La tua domenica del 22 novembre» Scrivi 80–100 parole: una festa, una partita, cosa assaggi.", instr="Écrire", size=15.5, gap=1)
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
p.text(MX, 1382, "RISPOSTE　CORRIGÉ — PAR PAGE : CHERCHE TON NUMÉRO", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "Chaque réponse a une note d'une ligne en français　✓ = tâche avec texte modèle", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.14, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Rédaction":
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
