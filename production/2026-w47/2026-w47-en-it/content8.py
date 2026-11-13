# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TEST (all levels) =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS　Esercizi e risposte", "The Lucerna", "ALL LEVELS　Test yourself　Mettiti alla prova")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1555, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "Tuesday", "Martedì 3 novembre, giorno del voto"),
    ("A2", "call", "call = annunciare il risultato"),
    ("A2", "continues", "continues è al presente"),
    ("A2", "will meet", "will meet, al futuro"),
    ("B1", "writes", "writes, terza persona singolare"),
    ("B1", "will certify", "will certify, al futuro"),
    ("B1", "wears", "wears, terza persona singolare"),
    ("B1", "will watch", "will watch, al futuro"),
]
cnums = [reg_ex(lv, "Completa il testo", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　CLOZE　Completa il testo", 24, gap=8)
bf.para(f"Maya is a student in London. This week, she is following the American election. On ({cnums[0]})___ morning, November 3, she reads the news about the midterm election. She learns a new word: a ({cnums[1]})___ is a news organisation's judgement — not the official result. On Wednesday, she writes a sentence: “The vote is over, but the counting ({cnums[2]})___.” Her teacher smiles: “The new Congress ({cnums[3]})___ in January.” Maya ({cnums[4]})___ the dates in her notebook: states ({cnums[5]})___ their counts by December 18. On Monday, she ({cnums[6]})___ odd socks to school for Anti-Bullying Week. And on Friday, she ({cnums[7]})___ the new Hunger Games film with her class.", 21.5)
bf.bridge("Opzioni:")
for n, (lv, _k, _nt), opts in zip(cnums, cloze_defs, [
    "A. Monday · B. Tuesday · C. Friday",
    "A. vote · B. call · C. seat",
    "A. continuing · B. was continued · C. continues",
    "A. meet · B. met · C. will meet",
    "A. writes · B. write · C. is wrote",
    "A. certified · B. will certify · C. certifies",
    "A. wears · B. is wear · C. wearing",
    "A. watched · B. watch · C. will watch",
]):
    bf.para(f"{n}. [{lv}] {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B　MULTIPLE CHOICE　Scelta", 24, gap=8)
mcq = [
    ("A2", "B", "I democratici hanno 254 seggi alla Camera", "How many House seats did the Democrats win, as called? A. 218 · B. 254 · C. 162"),
    ("A2", "A", "Il giorno del voto è il 3 novembre", "The vote was on... A. Tue, Nov 3 · B. Sun, Nov 8 · C. Mon, Nov 16"),
    ("A2", "C", "Sette seggi del Senato cambiano schieramento", "How many Senate seats changed hands? A. 2 · B. 5 · C. 7"),
    ("A2", "B", "Il nuovo film esce il 20 novembre", "“Sunrise on the Reaping” opens on... A. Nov 16 · B. Fri, Nov 20 · C. Nov 22"),
    ("A2", "A", "Il programma della giungla, il 16 novembre alle 9 di sera", "“I'm a Celebrity” starts... A. Mon, Nov 16, 9 p.m. · B. Sun, Nov 15 · C. Fri, Nov 20"),
    ("B1", "A", "L'Australia ha vinto le Ashes 2025–26 per 4–1", "Australia won the 2025–26 Ashes by... A. 4–1 · B. 1–4 · C. 2–2"),
    ("B1", "B", "Tema della Settimana contro il Bullismo: «Rompi il silenzio»", "The theme of Anti-Bullying Week is... A. “Odd Socks” · B. “Break the Silence” · C. “My day”"),
    ("B1", "A", "La Giornata Mondiale dell'Infanzia è il 20 novembre", "World Children's Day is on... A. Fri, Nov 20 · B. Thu, Nov 26 · C. Mon, Nov 16"),
    ("B1", "C", "Il Giorno del Ringraziamento è giovedì 26 novembre", "Thanksgiving is on... A. Mon, Nov 16 · B. Fri, Nov 27 · C. Thu, Nov 26"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "Scelta multipla", k, nt, body, size=20.5)

# ---- C. reading ----
bf.head("C　READING　Comprensione", 24, gap=8)
bf.para("Tom is a teacher in Manchester. On Monday, November 16, his class is reading about the American election. “The Democrats won the House with 254 seats,” he says. “And the Senate, with 20 of 33 seats called.” The class asks: “Is it finished?” “No,” says Tom. “The states must certify their counts. And two Senate races are still uncalled.” Then Tom opens the second story: “Today is Odd Socks Day.” The children laugh — Tom is wearing one red sock and one blue sock.", 21.5)
read_qs = [
    ("B1", "B", "Tom insegna a Manchester", "Tom is... A. a student · B. a teacher in Manchester · C. a reporter"),
    ("B1", "A", "I democratici hanno 254 seggi alla Camera", "The Democrats won the House with... A. 254 seats · B. 218 seats · C. 162 seats"),
    ("B1", "C", "Tom indossa un calzino rosso e uno blu", "Tom is wearing... A. one red sock · B. one blue sock · C. one red sock and one blue sock"),
    ("B1", "B", "La classe di Tom sta leggendo notizie sulle elezioni", "Tom's class is reading about... A. the Ashes · B. the American election · C. the film"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "Comprensione", k, nt, body, size=20.5)

# ---- D. sentence building ----
bf.head("D　SENTENCES　Completa", 24, gap=8)
d_items = [
    ("B1", "will meet", "will + infinito",
     "Will future: “The new Congress (meet) in January.” → ___"),
    ("B1", "won", "win → won",
     "Past simple: “The Democrats (win) the House.” → ___"),
    ("B1", "more", "more than, il comparativo",
     "Comparative: “254 is ___ than 218.”"),
    ("B2", "whether", "whether = se",
     "Whether: “Nobody knows ___ the count will change.”"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "Completare le frasi", k, nt, body, size=20.5)

# ---- E. translation ----
bf.head("E　TRANSLATION　Traduzione", 24, gap=8)
e_items = [
    ("B2", "I democratici hanno vinto la Camera e il Senato.", "the House and the Senate = la Camera e il Senato",
     "Traduci: “The Democrats won the House and the Senate.”"),
    ("B2", "Lo spoglio continua.", "continues = continua ancora",
     "Traduci: “The counting continues.”"),
    ("B2", "Il nuovo Congresso si riunirà a gennaio 2027.", "will meet = si riunirà",
     "Traduci: “The new Congress will meet in January 2027.”"),
    ("B1", "Rompi il silenzio.", "Break the silence.",
     "Traduci: “Break the silence.”"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "Traduzione", k, nt, body, size=20.5)

# ---- F. matching ----
bf.head("F　WORDS　Abbina", 24, gap=8)
bf.match_set("A2", "Abbinamento",
             ["a call", "a runoff", "to certify", "a midterm"],
             ["an election in the middle of a President's term",
              "a news organisation's judgement on a race",
              "a second vote, when nobody wins",
              "to confirm a count officially"],
             ["b", "c", "d", "a"],
             ["call = annunciare il risultato b", "runoff = un ballottaggio c", "certify = certificare ufficialmente d", "midterm = le elezioni di medio termine a"],
             instr="Abbina")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "row", "row = una fila di posti"),
    ("A2", "film", "film = un film"),
    ("A2", "popcorn", "popcorn = i popcorn"),
    ("A2", "show", "show = uno spettacolo"),
    ("A2", "Friday", "Friday = venerdì"),
]
gnums = [reg_ex(lv, "Dialogo", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　Dialogo", 24, gap=8)
bf.para(f"— Two tickets for the new Hunger Games film, please. — Which ({gnums[0]})___? — The front row, please. — Here you are. Is this the ({gnums[1]})___ about Haymitch? — Yes, the young Haymitch. — One large ({gnums[2]})___ and two drinks, please. — What time is the next ({gnums[3]})___? — At eight. — And the film opens on ({gnums[4]})___, November 20? — Yes, Friday. Enjoy the film!", 21.5)
bf.para(f"Levels: {gnums[0]}–{gnums[-1]} [A2]", 19.5, "sans", False, GREY, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1570
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "Scrittura", "Compito aperto — punti chiave nel riquadro di scrittura; testo modello nel riquadro a pagina 8", "Valutazione per punti chiave")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　WRITING　Scrittura [B1]", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words): “My Monday, November 16”. Tell us: did you wear odd socks, what did you watch on television, what did you read about the election — and one sentence about the film on Friday. The best texts will appear in VOL.5 (page 7, “Readers' Corner”).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "Scrivi 80–100 parole in inglese: «Il mio lunedì 16 novembre». Di' se hai indossato calzini spaiati, che cosa hai guardato alla televisione la sera, che cosa hai letto sulle elezioni, e una frase sul film di venerdì.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
image(p, "readingroom.jpg", mx2, wy, mw2, 110)
p.text(mx2, wy + 128, "The Main Reading Room, Library of Congress — Carol M. Highsmith, public domain.", 15.5, "sans", False, GREY)
p.rect(mx2, wy + 150, mw2, 280, fill=BOX)
p.text(mx2 + 22, wy + 188, "MODEL　Testo modello", 23, "sans", True, OLIVE)
MODEL_TEXT = "On Monday, November 16, I wore odd socks to school — one red, one blue. My teacher smiled and said, “Break the silence.” In the evening, we watched the jungle on television together with my family. On Tuesday, we read about the election in class: the Democrats won the House with 254 seats. On Friday, we will watch the new Hunger Games film. It is a busy week of votes, socks and stories — and I am learning to say it all in English."
p.para(mx2 + 22, wy + 224, MODEL_TEXT, 20, "serif", False, INK, mw2 - 44, 1.42)
print("MODEL words:", sum(1 for t in MODEL_TEXT.split() if any(ch.isalnum() for ch in t)))

# ---- keys ----
ky = wy + 462
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANSWERS　Risposte e note (pagine 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
PRINT_NOTES = [3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82, 83, 84, 85, 86, 87, 89, 108, 109, 110, 111]
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Pagina {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and (pg == 8 or e["n"] in PRINT_NOTES):
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13.5, "sans", False, INK, 1.26, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, TOTAL exercises:", len(REG))
