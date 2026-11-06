# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-it-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · TEST AND ANSWERS", "La Lucerna", "Page 8 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "tornare indietro = to go back",
     "Domenica l'orologio torna ___ di un'ora. (A. avanti · B. indietro)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "the clock-change night has 25 hours",
     "La notte tra sabato e domenica dura ___ ore. (A. 25 · B. 23)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "incontrare = to meet, to face (an opponent)",
     "Alle 12:30 l'Inter ___ la Fiorentina a San Siro. (A. incontra · B. visita)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "Napoli–Roma is on Saturday",
     "Napoli–Roma si gioca ___ alle 18:00. (A. sabato · B. domenica)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "Montaione hosts the truffle festival",
     "A Montaione è la festa del ___. (A. tartufo · B. cinema)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "the festival closes on Sunday: chiude",
     "La Festa del Cinema di Roma ___ domenica 25. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "Lucca opens on 28 October: apre",
     "Lucca Comics ___ il 28 ottobre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "28 October is a Wednesday",
     "Il voto sulla manovra è atteso per ___ 28 ottobre. (A. lunedì · B. mercoledì)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "03:00 goes back to 02:00",
     "Il cambio dell'ora: alle 03:00 → ... A. 04:00 · B. 02:00 · C. 01:00", size=15.5, gap=1)
f.ex("A2", "单选", "B", "«meteo oggi» is the No. 1 search",
     "«Meteo oggi» è... A. un film · B. la ricerca numero uno · C. una festa", size=15.5, gap=1)
f.ex("A2", "单选", "A", "the storm is called Adam",
     "La tempesta della settimana si chiama... A. Adam · B. Legacy · C. Bagòss", size=15.5, gap=1)
f.ex("B1", "单选", "B", "the white truffle fair is in Alba",
     "La Fiera del Tartufo Bianco è a... A. Volterra · B. Alba · C. Bagolino", size=15.5, gap=1)
f.ex("B1", "单选", "C", "the Artemisia exhibition is in Florence",
     "La mostra su Artemisia è a... A. Roma · B. Lucca · C. Firenze", size=15.5, gap=1)
f.ex("B1", "单选", "A", "the DPB was sent on 15 October",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "单选", "B", "the DPB figures are forecasts",
     "Le cifre del DPB sono... A. risultati · B. previsioni · C. voti", size=15.5, gap=1)
f.ex("B1", "单选", "B", "All Saints' Day this year is Sunday 1 November",
     "Ognissanti, quest'anno, è... A. lunedì 2 novembre · B. domenica 1° novembre · C. sabato 31 ottobre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Lucca: mercoledì 28 ottobre va a Lucca Comics con il suo cosplay. Paolo vive a Roma: domenica 25 va all'Auditorium per l'ultimo giorno della Festa del Cinema. Sabato, Giulia e Paolo dormono un'ora in più: domenica comincia l'ora solare.", 16.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Giulia goes to Lucca Comics",
     "Chi va a Lucca Comics? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "单选", "A", "Paolo goes to the Film Festival on Sunday",
     "Paolo, domenica, va... A. alla Festa del Cinema · B. a Lucca · C. a una sagra", size=15.5, gap=1)
f.ex("A2", "单选", "B", "the cosplay is Giulia's",
     "Il cosplay è di... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "单选", "A", "the title sums up two cities, two festivals",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "造句", "Domenica dormiamo un'ora in più.", "time word first",
     "domenica / dormiamo / un'ora in più → ___", instr="Reorder", size=15.5, gap=1)
f.ex("B1", "造句", "La fiera è iniziata il 10 ottobre.", "essere + participle + date",
     "la fiera / è iniziata / il 10 ottobre → ___", instr="Reorder", size=15.5, gap=1)
f.ex("B1", "造句", "A che ora comincia la partita?", "question phrase first",
     "a che ora / comincia / la partita / ? → ___", instr="Reorder", size=15.5, gap=1)
f.ex("B1", "造句", "Il voto slitta a mercoledì.", "subject + verb + phrase",
     "il voto / slitta / a mercoledì → ___", instr="Reorder", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "On Sunday we sleep an hour longer.", "lit. 'one hour more'",
     "Domenica dormiamo un'ora in più. → ___", instr="Translate into English", size=15.5, gap=1)
f.ex("B1", "翻译", "The show stays open till April.", "resta aperta = stays open",
     "La mostra resta aperta fino ad aprile. → ___", instr="Translate into English", size=15.5, gap=1)
f.ex("B1", "翻译", "Sabato alle 18:00 si gioca Napoli–Roma.", "si gioca = played",
     "On Saturday at 18:00, Napoli play Roma. → ___", instr="Translate into Italian", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni cifra deve avere una fonte.", "dovere = to have to",
     "Every figure must have a source. → ___", instr="Translate into Italian", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["la manovra", "il rinvio", "il miliardo", "la previsione"],
            ["un numero che descrive il futuro",
             "la legge di bilancio dello Stato",
             "quando una cosa arriva più tardi del previsto",
             "mille milioni"],
            ["b", "c", "d", "a"],
            ["manovra = the budget law b", "rinvio = arriving later than planned c", "miliardo = a billion (a thousand million) d", "previsione = a number that describes the future a"],
            instr="Match the pairs")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "tartufo = truffle",
     "— Cerco il ___ bianco famoso. (A. biglietto · B. tartufo)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "castagne arrosto = roast chestnuts",
     "— Vuole anche le castagne ___? (A. arrosto · B. mute)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "quanto costa? = how much does it cost?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "pagare con carta = to pay by card",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "the festival runs until Sunday",
     "— La sagra è in piazza fino a ___. (A. aprile · B. domenica)", size=15.5, gap=1)
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 25 ottobre mi sveglio tardi: nella notte l'orologio è tornato indietro e ho dormito un'ora in più. "
          "Sabato sera ho cambiato gli orologi di casa: quello del forno e quello vecchio in cucina. "
          "Faccio colazione con calma e vado al mercato con mia sorella. A pranzo guardiamo Inter–Fiorentina: "
          "è la prima partita con l'ora solare. Nel pomeriggio leggo un libro e preparo la settimana. "
          "La sera è già buio presto, ma non mi dispiace: l'autunno è la mia stagione preferita, "
          "con le sagre, il tartufo e le castagne calde.")
NWORDS = len(MODELO.split())
f.bridge(f"Writing task (no single correct answer); the model text ({NWORDS} words) is below.")
f.ex("B1", "写作", "(open task — model text below)", f"see the model text in section H on this page ({NWORDS} words)",
     "«La tua domenica 25 ottobre» Scrivi 80–100 parole: il cambio dell'ora, cosa fai con l'ora in più, una partita o una festa del tuo weekend.", instr="Writing", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RISPOSTE · ANSWER KEY — grouped by page: find your exercise number", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Each answer has a one-line note in English · ✓ = model-text task", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
# proofread fix (IT x EN): key flow bottom 2606 -> 2562 and lh 1.21 -> 1.15.
# At the old values column 2's last key (#75, baseline y=2588) was struck
# through by the footer rule (y=2580); the tighter leading lifts every
# column end clear of the rule. Keys/notes themselves unchanged.
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2562, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.15, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "写作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 14, lh=1.15, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-valutazione.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
