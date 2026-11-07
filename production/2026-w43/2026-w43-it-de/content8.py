# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-it-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · TEST UND LÖSUNGEN", "La Lucerna", "Seite 8 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "tornare indietro = zurückstellen",
     "Domenica l'orologio torna ___ di un'ora. (A. avanti · B. indietro)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "die Nacht der Zeitumstellung hat 25 Stunden",
     "La notte tra sabato e domenica dura ___ ore. (A. 25 · B. 23)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "incontrare = antreten gegen, spielen gegen",
     "Alle 12:30 l'Inter ___ la Fiorentina a San Siro. (A. incontra · B. visita)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "Napoli–Roma ist am Samstag",
     "Napoli–Roma si gioca ___ alle 18:00. (A. sabato · B. domenica)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "in Montaione ist das Trüffelfest",
     "A Montaione è la festa del ___. (A. tartufo · B. cinema)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "das Filmfest endet am Sonntag: chiude",
     "La Festa del Cinema di Roma ___ domenica 25. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "Lucca öffnet am 28. Oktober: apre",
     "Lucca Comics ___ il 28 ottobre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "der 28. Oktober ist ein Mittwoch",
     "Il voto sulla manovra è atteso per ___ 28 ottobre. (A. lunedì · B. mercoledì)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "aus 03:00 wird 02:00",
     "Il cambio dell'ora: alle 03:00 → ... A. 04:00 · B. 02:00 · C. 01:00", size=15.5, gap=1)
f.ex("A2", "单选", "B", "«meteo oggi» ist die Suche Nummer eins",
     "«Meteo oggi» è... A. un film · B. la ricerca numero uno · C. una festa", size=15.5, gap=1)
f.ex("A2", "单选", "A", "der Sturm heißt Adam",
     "La tempesta della settimana si chiama... A. Adam · B. Legacy · C. Bagòss", size=15.5, gap=1)
f.ex("B1", "单选", "B", "das Weißtrüffelfest ist in Alba",
     "La Fiera del Tartufo Bianco è a... A. Volterra · B. Alba · C. Bagolino", size=15.5, gap=1)
f.ex("B1", "单选", "C", "die Artemisia-Ausstellung ist in Florenz",
     "La mostra su Artemisia è a... A. Roma · B. Lucca · C. Firenze", size=15.5, gap=1)
f.ex("B1", "单选", "A", "der DPB wurde am 15. Oktober geschickt",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "单选", "B", "die DPB-Zahlen sind Prognosen",
     "Le cifre del DPB sono... A. risultati · B. previsioni · C. voti", size=15.5, gap=1)
f.ex("B1", "单选", "B", "Allerheiligen ist dieses Jahr am Sonntag, 1. November",
     "Ognissanti, quest'anno, è... A. lunedì 2 novembre · B. domenica 1° novembre · C. sabato 31 ottobre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Lucca: mercoledì 28 ottobre va a Lucca Comics con il suo cosplay. Paolo vive a Roma: domenica 25 va all'Auditorium per l'ultimo giorno della Festa del Cinema. Sabato, Giulia e Paolo dormono un'ora in più: domenica comincia l'ora solare.", 16.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Giulia fährt zu Lucca Comics",
     "Chi va a Lucca Comics? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "单选", "A", "Paolo geht am Sonntag zum Filmfest",
     "Paolo, domenica, va... A. alla Festa del Cinema · B. a Lucca · C. a una sagra", size=15.5, gap=1)
f.ex("A2", "单选", "B", "das Cosplay gehört Giulia",
     "Il cosplay è di... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "单选", "A", "der Titel fasst zwei Städte und zwei Feste zusammen",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "造句", "Domenica dormiamo un'ora in più.", "Zeitangabe zuerst",
     "domenica / dormiamo / un'ora in più → ___", instr="Sätze bilden", size=15.5, gap=1)
f.ex("B1", "造句", "La fiera è iniziata il 10 ottobre.", "Subjekt + essere + Partizip",
     "la fiera / è iniziata / il 10 ottobre → ___", instr="Sätze bilden", size=15.5, gap=1)
f.ex("B1", "造句", "A che ora comincia la partita?", "Frageformel am Anfang",
     "a che ora / comincia / la partita / ? → ___", instr="Sätze bilden", size=15.5, gap=1)
f.ex("B1", "造句", "Il voto slitta a mercoledì.", "Subjekt + Verb + Zeitangabe",
     "il voto / slitta / a mercoledì → ___", instr="Sätze bilden", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "Am Sonntag schlafen wir eine Stunde länger.", "wörtlich: eine Stunde mehr",
     "Domenica dormiamo un'ora in più. → ___", instr="Übersetzen", size=15.5, gap=1)
f.ex("B1", "翻译", "Die Ausstellung bleibt bis April geöffnet.", "resta aperta = bleibt geöffnet",
     "La mostra resta aperta fino ad aprile. → ___", instr="Übersetzen", size=15.5, gap=1)
f.ex("B1", "翻译", "Sabato alle 18:00 si gioca Napoli–Roma.", "si gioca = es wird gespielt",
     "Am Samstag um 18:00 Uhr spielt Napoli gegen Roma. → ___", instr="Übersetzen", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni cifra deve avere una fonte.", "dovere = müssen",
     "Jede Zahl muss eine Quelle haben. → ___", instr="Übersetzen", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["la manovra", "il rinvio", "il miliardo", "la previsione"],
            ["un numero che descrive il futuro",
             "la legge di bilancio dello Stato",
             "quando una cosa arriva più tardi del previsto",
             "mille milioni"],
            ["b", "c", "d", "a"],
            ["manovra = Haushaltsgesetz, b", "rinvio = später als geplant, c", "miliardo = eine Milliarde, d", "previsione = eine Zahl über die Zukunft, a"],
            instr="Zuordnen")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "tartufo = Trüffel",
     "— Cerco il ___ bianco famoso. (A. biglietto · B. tartufo)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "castagne arrosto = geröstete Kastanien",
     "— Vuole anche le castagne ___? (A. arrosto · B. mute)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "quanto costa? = was kostet es?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "pagare con carta = mit Karte zahlen",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "das Fest auf dem Platz geht bis Sonntag",
     "— La sagra è in piazza fino a ___. (A. aprile · B. domenica)", size=15.5, gap=1)
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 25 ottobre mi sveglio tardi: nella notte l'orologio è tornato indietro e ho dormito un'ora in più. "
          "Sabato sera ho cambiato gli orologi di casa: quello del forno e quello vecchio in cucina. "
          "Faccio colazione con calma e vado al mercato con mia sorella. A pranzo guardiamo Inter–Fiorentina: "
          "è la prima partita con l'ora solare. Nel pomeriggio leggo un libro e preparo la settimana. "
          "La sera è già buio presto, ma non mi dispiace: l'autunno è la mia stagione preferita, "
          "con le sagre, il tartufo e le castagne calde.")
NWORDS = len(MODELO.split())
f.noteline(f"Schreibaufgabe (keine einzige richtige Lösung); den Mustertext ({NWORDS} Wörter) finden Sie unten.")
f.ex("B1", "写作", "(offene Aufgabe — Mustertext unten)", f"Mustertext in Abschnitt H auf dieser Seite ({NWORDS} Wörter)",
     "«La tua domenica 25 ottobre» Scrivi 80–100 parole: il cambio dell'ora, cosa fai con l'ora in più, una partita o una festa del tuo weekend.", instr="Schreiben", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RISPOSTE · LÖSUNGEN — nach Seiten geordnet, suchen Sie die Nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Zu jeder Aufgabe ein kurzer Hinweis · ✓ = Schreibaufgabe", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "写作":
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
