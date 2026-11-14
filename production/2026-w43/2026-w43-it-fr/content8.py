# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE　EXERCICES ET RÉPONSES", "La Lucerna", "Page 8　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Texte à trous", "B", "tornare indietro = reculer",
     "Domenica l'orologio torna ___ di un'ora. (A. avanti · B. indietro)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "la nuit du changement d'heure dure 25 heures",
     "La notte tra sabato e domenica dura ___ ore. (A. 25 · B. 23)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "incontrare = affronter, rencontrer (un adversaire)",
     "Alle 12:30 l'Inter ___ la Fiorentina a San Siro. (A. incontra · B. visita)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "Napoli–Roma se joue samedi",
     "Napoli–Roma si gioca ___ alle 18:00. (A. sabato · B. domenica)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "à Montaione, c'est la fête de la truffe",
     "A Montaione è la festa del ___. (A. tartufo · B. cinema)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "le festival ferme dimanche : chiude",
     "La Festa del Cinema di Roma ___ domenica 25. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "Lucca ouvre le 28 octobre : apre",
     "Lucca Comics ___ il 28 ottobre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "le 28 octobre est un mercredi",
     "Il voto sulla manovra è atteso per ___ 28 ottobre. (A. lunedì · B. mercoledì)", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Choix unique", "B", "à 03:00, retour à 02:00",
     "Il cambio dell'ora: alle 03:00 → ... A. 04:00 · B. 02:00 · C. 01:00", size=15.5, gap=1)
f.ex("A2", "Choix unique", "B", "« meteo oggi » est la recherche n° 1",
     "«Meteo oggi» è... A. un film · B. la ricerca numero uno · C. una festa", size=15.5, gap=1)
f.ex("A2", "Choix unique", "A", "la tempête s'appelle Adam",
     "La tempesta della settimana si chiama... A. Adam · B. Legacy · C. Bagòss", size=15.5, gap=1)
f.ex("B1", "Choix unique", "B", "la foire de la truffe blanche est à Alba",
     "La Fiera del Tartufo Bianco è a... A. Volterra · B. Alba · C. Bagolino", size=15.5, gap=1)
f.ex("B1", "Choix unique", "C", "l'exposition Artemisia est à Florence",
     "La mostra su Artemisia è a... A. Roma · B. Lucca · C. Firenze", size=15.5, gap=1)
f.ex("B1", "Choix unique", "A", "le DPB est parti le 15 octobre",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "Choix unique", "B", "les chiffres du DPB sont des prévisions",
     "Le cifre del DPB sono... A. risultati · B. previsioni · C. voti", size=15.5, gap=1)
f.ex("B1", "Choix unique", "B", "la Toussaint tombe cette année le dimanche 1er novembre",
     "Ognissanti, quest'anno, è... A. lunedì 2 novembre · B. domenica 1° novembre · C. sabato 31 ottobre", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Lucca: mercoledì 28 ottobre va a Lucca Comics con il suo cosplay. Paolo vive a Roma: domenica 25 va all'Auditorium per l'ultimo giorno della Festa del Cinema. Sabato, Giulia e Paolo dormono un'ora in più: domenica comincia l'ora solare.", 16.5, lh=1.3, split=False)
f.ex("A2", "Choix unique", "B", "Giulia va à Lucca Comics",
     "Chi va a Lucca Comics? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Choix unique", "A", "Paolo va dimanche à la Festa du Cinéma",
     "Paolo, domenica, va... A. alla Festa del Cinema · B. a Lucca · C. a una sagra", size=15.5, gap=1)
f.ex("A2", "Choix unique", "B", "le cosplay est celui de Giulia",
     "Il cosplay è di... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Choix unique", "A", "le titre résume les deux villes et les deux fêtes",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Faire des phrases", "Domenica dormiamo un'ora in più.", "le mot de temps en tête",
     "domenica / dormiamo / un'ora in più → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("B1", "Faire des phrases", "La fiera è iniziata il 10 ottobre.", "sujet + essere + participe + date",
     "la fiera / è iniziata / il 10 ottobre → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("B1", "Faire des phrases", "A che ora comincia la partita?", "le groupe interrogatif d'abord",
     "a che ora / comincia / la partita / ? → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("B1", "Faire des phrases", "Il voto slitta a mercoledì.", "sujet + verbe + préposition",
     "il voto / slitta / a mercoledì → ___", instr="Former une phrase", size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "Le dimanche, nous dormons une heure de plus.", "traduction",
     "Domenica dormiamo un'ora in più. → ___", instr="Traduire", size=15.5, gap=1)
f.ex("B1", "翻译", "L'exposition reste ouverte jusqu'en avril.", "= reste ouverte",
     "La mostra resta aperta fino ad aprile. → ___", instr="Traduire", size=15.5, gap=1)
f.ex("B1", "翻译", "Sabato alle 18:00 si gioca Napoli–Roma.", "si gioca = se joue",
     "Samedi, 18:00 : Napoli–Roma. → ___", instr="Traduire", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni cifra deve avere una fonte.", "dovere = devoir, il faut",
     "Chaque chiffre doit avoir une source. → ___", instr="Traduire", size=15.5, gap=1)
f.head("F　LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "Associer les mots",
            ["la manovra", "il rinvio", "il miliardo", "la previsione"],
            ["un numero che descrive il futuro",
             "la legge di bilancio dello Stato",
             "quando una cosa arriva più tardi del previsto",
             "mille milioni"],
            ["b", "c", "d", "a"],
            ["manovra = le budget, la loi de finances b", "rinvio = l'arrivée plus tard que prévu c", "miliardo = un milliard d", "previsione = un nombre qui décrit l'avenir a"],
            instr="Associer")
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Texte à trous", "B", "tartufo = la truffe",
     "— Cerco il ___ bianco famoso. (A. biglietto · B. tartufo)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "castagne arrosto = châtaignes grillées",
     "— Vuole anche le castagne ___? (A. arrosto · B. mute)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "quanto costa ? = combien ça coûte ?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "A", "pagare con carta = payer par carte",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Texte à trous", "B", "la sagra dure jusqu'à dimanche",
     "— La sagra è in piazza fino a ___. (A. aprile · B. domenica)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 25 ottobre mi sveglio tardi: nella notte l'orologio è tornato indietro e ho dormito un'ora in più. "
          "Sabato sera ho cambiato gli orologi di casa: quello del forno e quello vecchio in cucina. "
          "Faccio colazione con calma e vado al mercato con mia sorella. A pranzo guardiamo Inter–Fiorentina: "
          "è la prima partita con l'ora solare. Nel pomeriggio leggo un libro e preparo la settimana. "
          "La sera è già buio presto, ma non mi dispiace: l'autunno è la mia stagione preferita, "
          "con le sagre, il tartufo e le castagne calde.")
NWORDS = len(MODELO.split())
f.expl(f"Exercice d'écriture (sans réponse unique) ; le texte modèle ({NWORDS} mots) est ci-dessous.")
f.ex("B1", "Écriture", "Question ouverte — texte modèle ci-dessous sur cette page", f"Texte modèle dans la section H de cette page ({NWORDS} mots)",
     "«La tua domenica 25 ottobre» Scrivi 80–100 parole: il cambio dell'ora, cosa fai con l'ora in più, una partita o una festa del tuo weekend.", instr="Écrire", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RISPOSTE　CORRIGÉS — classés par page, cherchez le numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Une courte explication en français pour chaque exercice　✓ = exercice d'écriture", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Écriture":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-valutazione.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
