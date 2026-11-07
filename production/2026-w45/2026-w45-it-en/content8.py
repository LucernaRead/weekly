# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-it-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · Test and answers", "La Lucerna", "Page 8 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "primo freddo = the first cold",
     "Lunedì 2 novembre arriva il primo ___ della stagione. (A. caldo · B. freddo)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "All Souls' Day is on 2 November",
     "Il 2 novembre è la Commemorazione dei ___. (A. defunti · B. santi)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "The Forum Cultura opens in Milan",
     "Il Forum Cultura apre martedì a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "The Panettone final is on Saturday and Sunday",
     "La finale del Panettone è sabato e ___ a Milano. (A. domenica · B. lunedì)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "The torrone festival is in Cremona",
     "La Festa del Torrone apre a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "Serie A matchday 11 ends on Sunday: chiude",
     "L'undicesima giornata ___ domenica 8 novembre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "Fiorentina play Juventus on Sunday evening",
     "Fiorentina–Juventus si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "The Festival dei Popoli is in Florence",
     "Il Festival dei Popoli è a ___. (A. Milano · B. Firenze)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "The first snow falls around 1,300-1,500 metres",
     "La prima neve leggera può cadere intorno ai... A. 500 m · B. 1.300–1.500 m · C. 3.000 m", size=15.5, gap=1)
f.ex("A2", "单选", "B", "The flower of All Souls' Day is the chrysanthemum",
     "Il fiore del 2 novembre è... A. la rosa · B. il crisantemo · C. il tulipano", size=15.5, gap=1)
f.ex("A2", "单选", "A", "19 countries send pastry chefs to the Panettone final",
     "Alla finale del Panettone partecipano pasticceri da... A. 19 paesi · B. 5 paesi · C. 50 paesi", size=15.5, gap=1)
f.ex("B1", "单选", "B", "The Forum Cultura has 50+ events",
     "Il Forum Cultura ha... A. 5 eventi · B. più di 50 eventi · C. 19 eventi", size=15.5, gap=1)
f.ex("B1", "单选", "C", "The Alba truffle fair runs to 6 December",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "单选", "A", "The DPB went out on 15 October",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "单选", "B", "A probability is not a certainty",
     "Una probabilità alta... A. è una certezza · B. non è una certezza · C. è un errore", size=15.5, gap=1)
f.ex("B1", "单选", "B", "Lucca Comics closed on 1 November",
     "Lucca Comics si è chiusa... A. il 28 ottobre · B. il 1° novembre · C. l'8 novembre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Milano: sabato 7 novembre va alla finale del Panettone e assaggia il panettone tradizionale. Paolo vive a Cremona: sabato 7 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano la Serie A: fa freddo, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Giulia goes to the Panettone final in Milan",
     "Chi va alla finale del Panettone? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "单选", "A", "Paolo goes to the torrone festival on Saturday",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Milano · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "单选", "B", "The traditional panettone is tasted by Giulia",
     "Il panettone tradizionale è assaggiato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "单选", "A", "The title sums up two cities, two sweets",
     "Il titolo migliore è... A. «Due città, due dolci» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "造句", "Lunedì arriva il primo freddo.", "Time word first",
     "lunedì / arriva / il primo freddo → ___", instr="Reorder", size=15.5, gap=1)
f.ex("B1", "造句", "La finale è a Milano il 7 novembre.", "Subject + essere + place",
     "la finale / è a Milano / il 7 novembre → ___", instr="Reorder", size=15.5, gap=1)
f.ex("B1", "造句", "A che ora apre il Forum Cultura?", "Question phrase first",
     "a che ora / apre / il Forum Cultura / ? → ___", instr="Reorder", size=15.5, gap=1)
f.ex("B1", "造句", "Il freddo arriva lunedì.", "Subject + verb + time",
     "il freddo / arriva / lunedì → ___", instr="Reorder", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "On Monday the first cold arrives.", "Compare with the original.",
     "Lunedì arriva il primo freddo. → ___", instr="Translate into English", size=15.5, gap=1)
f.ex("B1", "翻译", "The public can taste for free.", "assaggiare gratis = taste free",
     "Il pubblico può assaggiare gratis. → ___", instr="Translate into English", size=15.5, gap=1)
f.ex("B1", "翻译", "Sunday evening: Fiorentina play Juventus.", "si gioca = is played",
     "Domenica sera si gioca Fiorentina–Juventus. → ___", instr="Translate into English", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni previsione deve essere chiara.", "dovere = must",
     "Every forecast must be clear. → ___", instr="Translate into Italian", size=15.5, gap=1)
f.head("F · LE PAROLE DEL METEO", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["la probabilità", "la media", "il bollettino", "il modello"],
            ["il valore medio, tra tanti valori",
             "il documento con le previsioni più recenti",
             "il calcolo che prevede il tempo, come l'ECMWF",
             "quanto è possibile che una cosa succeda"],
            ["d", "a", "b", "c"],
            ["probabilità = possibility, d", "media = average, a", "bollettino = forecast bulletin, b", "modello = forecast model, c"],
            instr="Match the pairs")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "torrone = nougat",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "mandorle = almonds",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "quanto costa? = how much?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "pagare con carta = to pay by card",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "The torrone festival runs to 22 November",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Lunedì 2 novembre metto il cappotto e la sciarpa: arriva il primo freddo e la mattina è pungente. "
          "A scuola parliamo del Forum Cultura di Milano e del Festival dei Popoli di Firenze. "
          "Sabato assaggio il panettone con la mia famiglia: preferisco quello tradizionale, con i canditi. "
          "Domenica sera guardiamo Fiorentina–Juventus in televisione. "
          "Il freddo è arrivato, ma la settimana è dolce: cultura, dolci e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove del freddo.")
NWORDS = len(MODELO.split())
f.bridge(f"Writing task (no single right answer); the model text ({NWORDS} words) follows.")
f.ex("B1", "写作", "(open task — model text below)", f"Model text in section H below ({NWORDS} words)",
     "«La tua settimana del primo freddo» Scrivi 80–100 parole: il freddo, cosa metti, un evento o una festa del tuo weekend.", instr="Write", size=15.5, gap=1)
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
        if e_["type"] == "写作":
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
