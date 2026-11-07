# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-en-it/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS · Esercizi e risposte", "The Lucerna", "FINAL TEST · Prova finale · Le risposte sono in fondo a questa pagina")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "C", "il 31 ottobre è Halloween"),
    ("A2", "A", "carve = intagliare la zucca"),
    ("B1", "B", "neither...nor = né... né..."),
    ("A2", "A", "costume = il travestimento di Halloween"),
    ("A2", "B", "she, terza persona → wears"),
    ("A2", "B", "con trick or treat arrivano i dolci"),
    ("B1", "A", "will + forma base: fall"),
    ("B1", "C", "be going to → is going"),
]
cnums = [reg_ex(lv, "Completare il testo", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · CLOZE · Completa il testo", 24)
bf.para(f"Maya is twelve. On Saturday, October 31, it is ({cnums[0]})___. In the morning, she helps her father ({cnums[1]})___ a pumpkin on the porch. « ({cnums[2]})___ rain nor cold can stop us », laughs her mother. In the evening, Maya puts on her ({cnums[3]})___ : she ({cnums[4]})___ a gold crown, like a Greek goddess. She takes her bag and goes from house to house : « Trick or treat ! » The neighbours give her ({cnums[5]})___. At nine o'clock, the street is quiet — and in the night, the clocks will ({cnums[6]})___ back : one more hour of sleep ! Tomorrow, Maya is ({cnums[7]})___ to sleep late, very late.", 21.5)
bf.expl("Opzioni:")
for n, opts in zip(cnums, [
    "A. Christmas · B. Easter · C. Halloween",
    "A. carve · B. eat · C. sell",
    "A. Both · B. Neither · C. Also",
    "A. costume · B. uniform · C. pyjamas",
    "A. wear · B. wears · C. wearing",
    "A. money · B. candy · C. flowers",
    "A. fall · B. falls · C. falling",
    "A. goes · B. go · C. going",
]):
    bf.para(f"{n}. {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B · MULTIPLE CHOICE · Scelta", 24)
mcq = [
    ("A2", "B", "9:15 = a quarter past nine", "The game starts at 9:15. In words : ... A. a quarter to nine · B. a quarter past nine · C. half past nine"),
    ("A2", "A", "we → get, forma base", "On Sunday, we ___ an extra hour of sleep. A. get · B. gets · C. getting"),
    ("B1", "B", "partita finita: si usa won", "The 76ers ___ the game 106–100. A. win · B. won · C. wins"),
    ("B1", "B", "than → comparativo: hotter", "Austin is ___ than Milwaukee in October. A. hot · B. hotter · C. hottest"),
    ("B2", "A", "despite + nome: nonostante la pioggia", "___ the rain, the parade went on all evening. A. Despite · B. Because · C. Unless"),
    ("B2", "A", "whether = se, domanda indiretta", "Nobody knows ___ the Brewers will win the Series. A. whether · B. what · C. who"),
    ("A2", "A", "cosa passata: passato opened", "Early voting in Texas ___ on Monday. A. opened · B. open · C. opens"),
    ("B1", "A", "be going to + forma base: cast", "She is going to ___ her ballot on Saturday. A. cast · B. casts · C. casted"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "Scelta multipla", k, nt, body, size=20.5)

# ---- C. reading ----
bf.head("C · READING · Comprensione", 24)
bf.para("On Monday morning, Rosa Delgado, a nurse from Houston, finished her night work at six o'clock. She did not go home to sleep. She drove to the early-voting place near the hospital and joined a short line. « On November 3, I work all day », she explains. « Today, I have time. » Ten minutes later, her ballot was in the box, and a sticker on her jacket said : I VOTED EARLY. By Friday, October 30, when early voting ends in Texas, millions of Texans will do the same.", 21.5)
read_qs = [
    ("A2", "B", "nel testo: a nurse from Houston", "Rosa is... A. a teacher · B. a nurse · C. a driver"),
    ("A2", "B", "il 3 novembre lavora tutto il giorno", "She voted early because on November 3 she... A. travels · B. works all day · C. sleeps"),
    ("B1", "A", "l'adesivo diceva I VOTED EARLY", "Her sticker said... A. I VOTED EARLY · B. VOTE ON TUESDAY · C. TEXAS FIRST"),
    ("B1", "B", "il voto anticipato in Texas finisce il 30 ottobre", "Early voting in Texas ends on... A. October 19 · B. October 30 · C. November 3"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "Comprensione del testo", k, nt, body, size=20.5)

# ---- D. sentence building ----
bf.head("D · SENTENCES · Completa", 24)
d_items = [
    ("A2", "On Saturday, they are going to carve a pumpkin.", "are going to + forma base",
     "Be going to : « On Saturday, they (carve) a pumpkin. » → ___"),
    ("B1", "The Knicks raised their first banner since 1973.", "raise → raised (cambio regolare)",
     "Past simple : « The Knicks (raise) their first banner since 1973. »"),
    ("B1", "scarier", "scary → scarier (la y diventa i + er)",
     "Comparative : « My costume is ___ (scary) than yours. »"),
    ("B2", "Whether", "whether = se, in una domanda indiretta",
     "Whether : « ___ the parade will happen, nobody knows. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "Completare le frasi", k, nt, body, size=20.5)

# ---- E. translation ----
bf.head("E · TRANSLATION · Traduzione", 24)
e_items = [
    ("B2", "Votare non è più cosa di un solo giorno; è una stagione.", "no longer = non più",
     "Translate : « Voting is no longer a day ; it is a season. »"),
    ("A2", "The 76ers won the game 106–100.", "win → won; il punteggio: 106–100",
     "Traduci: I 76ers hanno vinto per 106 a 100."),
    ("B1", "This year, early voting opened on Monday.", "open → opened; on Monday",
     "Traduci: Quest'anno il voto anticipato è iniziato lunedì."),
    ("B1", "Nessuno dei due club ha mai vinto le World Series.", "neither nega entrambi; has ever won, present perfect",
     "Translate : « Neither club has ever won the Series. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "Traduzione", k, nt, body, size=20.5)

# ---- F. matching ----
bf.head("F · WORDS · Abbina", 24)
bf.match_set("B1", "Abbinamento",
             ["a midterm", "an incumbent", "a margin", "turnout"],
             ["the number of people who vote", "an election in the middle of a president's term",
              "the person who holds the job now", "the difference between two results"],
             ["b", "c", "d", "a"],
             ["midterm = le elezioni di metà mandato b", "incumbent = chi è in carica c", "margin = il distacco d", "turnout = l'affluenza a"],
             instr="Abbina")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ID", "al voto si mostra un documento: ID"),
    ("A2", "line", "line = la fila (inglese americano)"),
    ("A2", "ballot", "ballot = la scheda"),
    ("A2", "sticker", "sticker = l'adesivo"),
    ("B1", "November", "il giorno delle elezioni è il 3 novembre"),
]
gnums = [reg_ex(lv, "Completare il dialogo", k, nt) for lv, k, nt in dlg_defs]
bf.head("G · DIALOGUE · Il dialogo", 24)
bf.para(f"— Good morning ! Is this the early-voting place ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long today ? — No, five minutes only. Yesterday it was very long ! — Good. It is my first early vote. What do I do with the ({gnums[2]})___ ? — Mark your choices, check them twice, then put it in the box. — Thank you. And the famous ({gnums[3]})___ ? Everybody has one on their jacket. — The sticker ! Here it is : « I VOTED ». Wear it with pride. — I will ! See you on ({gnums[4]})___ 3rd, in the results ! — Ha ! Have a good day.", 21.5)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "Scrittura", "(domanda aperta — il modello è nel riquadro di scrittura)", "si valuta in base ai punti")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · WRITING · Scrittura", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Saturday, October 31 ». Tell us : your costume, your street, the candy, the pumpkins — and one sentence about the clocks that fall back in the night. The best texts will appear in VOL.2 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "Scrivi in inglese (80–100 parole): il mio sabato 31 ottobre. Racconta il costume, la strada, i dolci, le zucche — e una frase sull'orologio che nella notte si sposta indietro.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MODEL · Il modello", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Saturday, October 31, our street becomes a small Halloween town. In the morning, I carve a pumpkin with my father and we put a candle inside. At six o'clock, I wear my pirate costume and take my bag. House after house, I say « Trick or treat ! » and the neighbours smile and give me candy. My bag is heavy at nine o'clock ! In the night, the clocks fall back, so I sleep one hour more on Sunday. It is my favourite weekend of the autumn.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "ANSWERS · Risposte e note (pagine 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")
# Printed-note parity with the core (see WEEKLY-KIT): the core rule prints a
# pre-P8 note when it is <=10 chars (Chinese) or the type is correction/chart.
# The Italian notes below are longer, so the items whose notes print in the
# core are listed explicitly; printed-note coverage is then identical (62).
NOTE_EXTRA = {11, 14, 15, 19, 35, 36, 40, 42, 49, 65, 74, 89, 101, 106}
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Pagina {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("Correzione", "Lettura del grafico") or e["n"] in NOTE_EXTRA):
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
