# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE　TOETS EN ANTWOORDEN", "La Lucerna", "Pagina 8　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Cloze", "B", "tornare indietro = terugzetten",
     "Domenica l'orologio torna ___ di un'ora. (A. avanti · B. indietro)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "de nacht van de klokwissel duurt 25 uur",
     "La notte tra sabato e domenica dura ___ ore. (A. 25 · B. 23)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "incontrare = treffen, spelen tegen",
     "Alle 12:30 l'Inter ___ la Fiorentina a San Siro. (A. incontra · B. visita)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "Napoli–Roma is op zaterdag",
     "Napoli–Roma si gioca ___ alle 18:00. (A. sabato · B. domenica)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "in Montaione is het truffelfeest",
     "A Montaione è la festa del ___. (A. tartufo · B. cinema)", size=15.5, gap=1)
f.ex("B1", "Cloze", "B", "het festival sluit op zondag: chiude",
     "La Festa del Cinema di Roma ___ domenica 25. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "Lucca opent op 28 oktober: apre",
     "Lucca Comics ___ il 28 ottobre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "Cloze", "B", "28 oktober is een woensdag",
     "Il voto sulla manovra è atteso per ___ 28 ottobre. (A. lunedì · B. mercoledì)", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Meerkeuze", "B", "03:00 wordt weer 02:00",
     "Il cambio dell'ora: alle 03:00 → ... A. 04:00 · B. 02:00 · C. 01:00", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "B", "«meteo oggi» is de meest gezochte term",
     "«Meteo oggi» è... A. un film · B. la ricerca numero uno · C. una festa", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "de storm heet Adam",
     "La tempesta della settimana si chiama... A. Adam · B. Legacy · C. Bagòss", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "B", "het witte-truffelfeest is in Alba",
     "La Fiera del Tartufo Bianco è a... A. Volterra · B. Alba · C. Bagolino", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "C", "de Artemisia-tentoonstelling is in Florence",
     "La mostra su Artemisia è a... A. Roma · B. Lucca · C. Firenze", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "A", "het DPB is op 15 oktober verzonden",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "Meerkeuze", "B", "de DPB-cijfers zijn prognoses",
     "Le cifre del DPB sono... A. risultati · B. previsioni · C. voti", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "B", "Allerheiligen valt dit jaar op zondag 1 november",
     "Ognissanti, quest'anno, è... A. lunedì 2 novembre · B. domenica 1° novembre · C. sabato 31 ottobre", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Lucca: mercoledì 28 ottobre va a Lucca Comics con il suo cosplay. Paolo vive a Roma: domenica 25 va all'Auditorium per l'ultimo giorno della Festa del Cinema. Sabato, Giulia e Paolo dormono un'ora in più: domenica comincia l'ora solare.", 16.5, lh=1.3, split=False)
f.ex("A2", "Meerkeuze", "B", "Giulia gaat naar Lucca Comics",
     "Chi va a Lucca Comics? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "Paolo gaat zondag naar het filmfestival",
     "Paolo, domenica, va... A. alla Festa del Cinema · B. a Lucca · C. a una sagra", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "B", "de cosplay is van Giulia",
     "Il cosplay è di... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "de titel vat twee steden en twee feesten samen",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Zinnen bouwen", "Domenica dormiamo un'ora in più.", "tijdwoord voorop",
     "domenica / dormiamo / un'ora in più → ___", instr="Bouw de zin", size=15.5, gap=1)
f.ex("B1", "Zinnen bouwen", "La fiera è iniziata il 10 ottobre.", "essere + deelwoord + datum",
     "la fiera / è iniziata / il 10 ottobre → ___", instr="Bouw de zin", size=15.5, gap=1)
f.ex("B1", "Zinnen bouwen", "A che ora comincia la partita?", "vraagwoordgroep vooraan",
     "a che ora / comincia / la partita / ? → ___", instr="Bouw de zin", size=15.5, gap=1)
f.ex("B1", "Zinnen bouwen", "Il voto slitta a mercoledì.", "ond. + ww. + voorzetselgroep",
     "il voto / slitta / a mercoledì → ___", instr="Bouw de zin", size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", "Vertaling", "Op zondag slapen we een uur langer.", "zie de originele zin",
     "Domenica dormiamo un'ora in più. → ___", instr="Vertaal", size=15.5, gap=1)
f.ex("B1", "Vertaling", "De tentoonstelling blijft open tot april.", "resta aperta = open",
     "La mostra resta aperta fino ad aprile. → ___", instr="Vertaal", size=15.5, gap=1)
f.ex("B1", "Vertaling", "Sabato alle 18:00 si gioca Napoli–Roma.", "si gioca = spelen",
     "Zaterdag om 18:00: Napoli tegen Roma. → ___", instr="Vertaal", size=15.5, gap=1)
f.ex("B2", "Vertaling", "Ogni cifra deve avere una fonte.", "dovere = moeten",
     "Elk cijfer moet een bron hebben. → ___", instr="Vertaal", size=15.5, gap=1)
f.head("F　LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "Woorden koppelen",
            ["la manovra", "il rinvio", "il miliardo", "la previsione"],
            ["un numero che descrive il futuro",
             "la legge di bilancio dello Stato",
             "quando una cosa arriva più tardi del previsto",
             "mille milioni"],
            ["b", "c", "d", "a"],
            ["manovra = begrotingswet b", "rinvio = later aankomen dan gepland c", "miliardo = miljard d", "previsione = een cijfer dat de toekomst beschrijft a"],
            instr="Koppel woord en betekenis")
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Cloze", "B", "tartufo = truffel",
     "— Cerco il ___ bianco famoso. (A. biglietto · B. tartufo)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "castagne arrosto = geroosterde kastanjes",
     "— Vuole anche le castagne ___? (A. arrosto · B. mute)", size=15.5, gap=1)
f.ex("B1", "Cloze", "B", "quanto costa? = hoeveel kost het?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Cloze", "A", "pagare con carta = met de kaart betalen",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Cloze", "B", "het eetfeest duurt tot zondag",
     "— La sagra è in piazza fino a ___. (A. aprile · B. domenica)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 25 ottobre mi sveglio tardi: nella notte l'orologio è tornato indietro e ho dormito un'ora in più. "
          "Sabato sera ho cambiato gli orologi di casa: quello del forno e quello vecchio in cucina. "
          "Faccio colazione con calma e vado al mercato con mia sorella. A pranzo guardiamo Inter–Fiorentina: "
          "è la prima partita con l'ora solare. Nel pomeriggio leggo un libro e preparo la settimana. "
          "La sera è già buio presto, ma non mi dispiace: l'autunno è la mia stagione preferita, "
          "con le sagre, il tartufo e le castagne calde.")
NWORDS = len(MODELO.split())
f.expl(f"Schrijfopdracht (geen uniek antwoord); het model ({NWORDS} woorden) staat hieronder.")
f.ex("B1", "Schrijven", "(open vraag — het model staat hieronder)", f"Het model staat in sectie H van deze pagina ({NWORDS} woorden)",
     "«La tua domenica 25 ottobre» Scrivi 80–100 parole: il cambio dell'ora, cosa fai con l'ora in più, una partita o una festa del tuo weekend.", instr="Schrijf", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RISPOSTE　ANTWOORDEN — per pagina gerangschikt: zoek op nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Elke opgave heeft een korte uitleg in het Nederlands　✓ = schrijfopgave met model", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Pagina {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schrijven":
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
