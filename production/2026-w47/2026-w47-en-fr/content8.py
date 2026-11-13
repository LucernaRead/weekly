# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TEST (all levels) =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS　Exercices et réponses", "The Lucerna", "ALL LEVELS　Test yourself　Testez-vous")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1555, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "Tuesday", "Jour du vote : mardi 3 novembre"),
    ("A2", "call", "call = annoncer le résultat"),
    ("A2", "continues", "continues, au présent"),
    ("A2", "will meet", "will meet, au futur"),
    ("B1", "writes", "writes, 3e personne"),
    ("B1", "will certify", "will certify, au futur"),
    ("B1", "wears", "wears, 3e personne"),
    ("B1", "will watch", "will watch, au futur"),
]
cnums = [reg_ex(lv, "Texte à trous", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　CLOZE　Texte à trous", 24, gap=8)
bf.para(f"Maya is a student in London. This week, she is following the American election. On ({cnums[0]})___ morning, November 3, she reads the news about the midterm election. She learns a new word: a ({cnums[1]})___ is a news organisation's judgement — not the official result. On Wednesday, she writes a sentence: “The vote is over, but the counting ({cnums[2]})___.” Her teacher smiles: “The new Congress ({cnums[3]})___ in January.” Maya ({cnums[4]})___ the dates in her notebook: states ({cnums[5]})___ their counts by December 18. On Monday, she ({cnums[6]})___ odd socks to school for Anti-Bullying Week. And on Friday, she ({cnums[7]})___ the new Hunger Games film with her class.", 21.5)
bf.bridge("Les choix :")
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
bf.head("B　MULTIPLE CHOICE　QCM", 24, gap=8)
mcq = [
    ("A2", "B", "254 sièges démocrates à la Chambre", "How many House seats did the Democrats win, as called? A. 218 · B. 254 · C. 162"),
    ("A2", "A", "Jour du vote : 3 novembre", "The vote was on... A. Tue, Nov 3 · B. Sun, Nov 8 · C. Mon, Nov 16"),
    ("A2", "C", "7 sièges du Sénat changent de camp", "How many Senate seats changed hands? A. 2 · B. 5 · C. 7"),
    ("A2", "B", "Le nouveau film sort le 20 novembre", "“Sunrise on the Reaping” opens on... A. Nov 16 · B. Fri, Nov 20 · C. Nov 22"),
    ("A2", "A", "La jungle commence le 16 novembre à 21 h", "“I'm a Celebrity” starts... A. Mon, Nov 16, 9 p.m. · B. Sun, Nov 15 · C. Fri, Nov 20"),
    ("B1", "A", "L'Australie a remporté les Ashes 2025–26 par 4–1", "Australia won the 2025–26 Ashes by... A. 4–1 · B. 1–4 · C. 2–2"),
    ("B1", "B", "Thème de la Semaine contre le harcèlement : « Brisez le silence »", "The theme of Anti-Bullying Week is... A. “Odd Socks” · B. “Break the Silence” · C. “My day”"),
    ("B1", "A", "Journée mondiale de l'enfance, le 20 novembre", "World Children's Day is on... A. Fri, Nov 20 · B. Thu, Nov 26 · C. Mon, Nov 16"),
    ("B1", "C", "Thanksgiving, jeudi 26 novembre", "Thanksgiving is on... A. Mon, Nov 16 · B. Fri, Nov 27 · C. Thu, Nov 26"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "Choix multiple", k, nt, body, size=20.5)

# ---- C. reading ----
bf.head("C　READING　Compréhension", 24, gap=8)
bf.para("Tom is a teacher in Manchester. On Monday, November 16, his class is reading about the American election. “The Democrats won the House with 254 seats,” he says. “And the Senate, with 20 of 33 seats called.” The class asks: “Is it finished?” “No,” says Tom. “The states must certify their counts. And two Senate races are still uncalled.” Then Tom opens the second story: “Today is Odd Socks Day.” The children laugh — Tom is wearing one red sock and one blue sock.", 21.5)
read_qs = [
    ("B1", "B", "Tom enseigne à Manchester", "Tom is... A. a student · B. a teacher in Manchester · C. a reporter"),
    ("B1", "A", "254 sièges démocrates à la Chambre", "The Democrats won the House with... A. 254 seats · B. 218 seats · C. 162 seats"),
    ("B1", "C", "Tom porte une chaussette rouge et une bleue", "Tom is wearing... A. one red sock · B. one blue sock · C. one red sock and one blue sock"),
    ("B1", "B", "La classe de Tom lit les nouvelles de l'élection", "Tom's class is reading about... A. the Ashes · B. the American election · C. the film"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "Compréhension écrite", k, nt, body, size=20.5)

# ---- D. sentence building ----
bf.head("D　SENTENCES　Phrases à former", 23, gap=8)  # D5: 24->23, HEAD TOO WIDE +1.2px advance at 24
d_items = [
    ("B1", "will meet", "will + verbe à l'infinitif",
     "Will future: “The new Congress (meet) in January.” → ___"),
    ("B1", "won", "win → won",
     "Past simple: “The Democrats (win) the House.” → ___"),
    ("B1", "more", "more than, comparatif",
     "Comparative: “254 is ___ than 218.”"),
    ("B2", "whether", "whether = si",
     "Whether: “Nobody knows ___ the count will change.”"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "Compléter", k, nt, body, size=20.5)

# ---- E. translation ----
bf.head("E　TRANSLATION　Traduction", 24, gap=8)
e_items = [
    ("B2", "Les démocrates ont remporté la Chambre et le Sénat.", "the House and the Senate = les deux chambres",
     "Traduis: “The Democrats won the House and the Senate.”"),
    ("B2", "Le dépouillement continue.", "continues = continue encore",
     "Traduis: “The counting continues.”"),
    ("B2", "Le nouveau Congrès se réunira en janvier 2027.", "will meet = se réunira",
     "Traduis: “The new Congress will meet in January 2027.”"),
    ("B1", "Brisez le silence.", "Break the silence.",
     "Traduis: “Break the silence.”"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "Traduction", k, nt, body, size=20.5)

# ---- F. matching ----
bf.head("F　WORDS　Mots à associer", 24, gap=8)
bf.match_set("A2", "Appariement",
             ["a call", "a runoff", "to certify", "a midterm"],
             ["an election in the middle of a President's term",
              "a news organisation's judgement on a race",
              "a second vote, when nobody wins",
              "to confirm a count officially"],
             ["b", "c", "d", "a"],
             ["call = annoncer le résultat b", "runoff = un second tour c", "certify = confirmer officiellement d", "midterm = une élection de mi-mandat a"],
             instr="Associez")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "row", "row = une rangée"),
    ("A2", "film", "film = un film"),
    ("A2", "popcorn", "popcorn = du pop-corn"),
    ("A2", "show", "show = une séance"),
    ("A2", "Friday", "Friday = vendredi"),
]
gnums = [reg_ex(lv, "Dialogue à compléter", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　À compléter", 24, gap=8)
bf.para(f"— Two tickets for the new Hunger Games film, please. — Which ({gnums[0]})___? — The front row, please. — Here you are. Is this the ({gnums[1]})___ about Haymitch? — Yes, the young Haymitch. — One large ({gnums[2]})___ and two drinks, please. — What time is the next ({gnums[3]})___? — At eight. — And the film opens on ({gnums[4]})___, November 20? — Yes, Friday. Enjoy the film!", 21.5)
bf.para(f"Levels: {gnums[0]}–{gnums[-1]} [A2]", 19.5, "sans", False, GREY, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1570
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "Écriture", "Tâche ouverte — points dans le cadre d'écriture ; texte modèle dans le cadre de cette page", "Noté sur les points")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　WRITING　Écriture [B1]", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words): “My Monday, November 16”. Tell us: did you wear odd socks, what did you watch on television, what did you read about the election — and one sentence about the film on Friday. The best texts will appear in VOL.5 (page 7, “Readers' Corner”).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "Écrivez 80–100 mots en anglais : « Mon lundi 16 novembre ». Dites si vous avez porté des chaussettes dépareillées, ce que vous avez regardé à la télévision le soir, ce que vous avez lu sur l'élection — et une phrase sur le film de vendredi.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
image(p, "readingroom.jpg", mx2, wy, mw2, 110)
p.text(mx2, wy + 128, "The Main Reading Room, Library of Congress — Carol M. Highsmith, public domain.", 15.5, "sans", False, GREY)
p.rect(mx2, wy + 150, mw2, 280, fill=BOX)
p.text(mx2 + 22, wy + 188, "MODEL　Texte modèle", 23, "sans", True, OLIVE)
MODEL_TEXT = "On Monday, November 16, I wore odd socks to school — one red, one blue. My teacher smiled and said, “Break the silence.” In the evening, we watched the jungle on television together with my family. On Tuesday, we read about the election in class: the Democrats won the House with 254 seats. On Friday, we will watch the new Hunger Games film. It is a busy week of votes, socks and stories — and I am learning to say it all in English."
p.para(mx2 + 22, wy + 224, MODEL_TEXT, 20, "serif", False, INK, mw2 - 44, 1.42)
print("MODEL words:", sum(1 for t in MODEL_TEXT.split() if any(ch.isalnum() for ch in t)))

# ---- keys ----
ky = wy + 462
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANSWERS　Toutes les réponses commentées (pages 1 à 8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
PRINT_NOTES = [3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82, 83, 84, 85, 86, 87, 89, 108, 109, 110, 111]
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Page {pg} —", 16, "sans", True, OLIVE, 1.28, 3)
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
