# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS　Exercices et réponses", "The Lucerna", "FINAL TEST　Test final　Answers at the bottom of this page　Les réponses sont en bas de cette page")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "Le 11 novembre est un mercredi"),
    ("A2", "A", "poppy = le coquelicot"),
    ("B1", "C", "silence = le silence"),
    ("A2", "B", "eleven = onze"),
    ("A2", "A", "Pudsey, le petit ours jaune"),
    ("A2", "C", "will + verbe de base : know"),
    ("B1", "B", "be going to → is going"),
    ("B1", "A", "still = toujours"),
]
cnums = [reg_ex(lv, "Texte à trous", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　CLOZE　Texte à trous", 24, gap=8)
bf.para(f"Maya is sixteen. On ({cnums[0]})___, November 11, she wears a red ({cnums[1]})___ to school. At eleven o'clock, the whole school stands in ({cnums[2]})___ for two minutes. « ({cnums[3]})___, eleven, eleven », says her teacher. On Friday, Maya bakes cakes for ({cnums[4]})___, the yellow bear. « When ({cnums[5]})___ we know the total ? » asks Maya. « On Friday night », says her mother. « On Sunday, Maya is ({cnums[6]})___ to watch the game from Munich — and the poppy will ({cnums[7]})___ be on her coat. »", 21.5)
bf.instrline("Les choix :")
for n, (lv, _k, _nt), opts in zip(cnums, cloze_defs, [
    "A. Monday · B. Wednesday · C. Friday",
    "A. poppy · B. hat · C. ticket",
    "A. noise · B. music · C. silence",
    "A. Ten · B. Eleven · C. Twelve",
    "A. Pudsey · B. Scrooge · C. Dickens",
    "A. do · B. are · C. will",
    "A. goes · B. going · C. go",
    "A. still · B. never · C. soon",
]):
    bf.para(f"{n}. [{lv}] {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B　MULTIPLE CHOICE　QCM", 24, gap=8)
mcq = [
    ("A2", "B", "11 heures = eleven o'clock", "The silence begins at 11 a.m. In words : ... A. ten o'clock · B. eleven o'clock · C. twelve o'clock"),
    ("A2", "A", "we → wear (infinitif)", "On Wednesday, we ___ a poppy. A. wear · B. wears · C. wearing"),
    ("B1", "B", "Pour le passé, on emploie wrote", "Dickens ___ the story in 1843. A. writes · B. wrote · C. writing"),
    ("B1", "B", "than → comparatif bigger", "The Allianz Arena is ___ than most NFL stadiums. A. big · B. bigger · C. biggest"),
    ("B2", "A", "despite + nom : malgré la pluie", "___ the rain, the ceremony went on all morning. A. Despite · B. Because · C. Unless"),
    ("B2", "A", "whether = si", "Nobody knows ___ this year will be faster. A. whether · B. what · C. who"),
    ("A2", "A", "Futur : will + verbe de base", "The film ___ on Friday, November 13. A. will open · B. will opened · C. will opens"),
    ("B1", "A", "be going to + infinitif watch", "They are going to ___ the game on Sunday. A. watch · B. watches · C. watched"),
    ("B1", "C", "challenge yourself = relève le défi", "« Challenge yourself » means... A. the show is over · B. voting is closed · C. take on a challenge"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "Choix multiple", k, nt, body, size=20.5, gap=8)

# ---- C. reading ----
bf.head("C　READING　Compréhension", 24, gap=8)
bf.para("On Wednesday morning, Tom, a teacher from Manchester, finished his breakfast and walked to school early. At eleven o'clock, the whole school stood still for two minutes. There was no sound in the hall. « We remember them », said Tom, quietly. In the afternoon, his class baked 26 cakes for Children in Need, and a poppy box stood by the door. On Friday night, Tom watched the appeal show with his family — and Pudsey was, as always, yellow and smiling.", 21.5)
read_qs = [
    ("A2", "B", "Dans le texte : a teacher from Manchester", "Tom is... A. a nurse · B. a teacher · C. a driver"),
    ("A2", "B", "Toute l’école observe deux minutes de silence", "At eleven o'clock, the school... A. sang · B. stood still for two minutes · C. went home"),
    ("B1", "A", "La classe a cuisiné 26 gâteaux", "His class baked... A. 26 cakes · B. 11 cakes · C. 13 cakes", ),
    ("B1", "B", "Pudsey est jaune comme toujours", "On Friday night, Pudsey was... A. red · B. yellow and smiling · C. asleep"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "Compréhension écrite", k, nt, body, size=20.5, gap=8)

# ---- D. sentence building ----
bf.head("D　SENTENCES　Phrases à former", 24, gap=8)
d_items = [
    ("A2", "On Friday, they will watch the appeal show.", "will + infinitif",
     "Will future : « On Friday, they (watch) the appeal show. » → ___"),
    ("B1", "The guns fell silent in 1918.", "fall → fell (verbe irrégulier)",
     "Past simple : « The guns (fall) silent in 1918. »"),
    ("B1", "bigger", "big → bigger (comparatif)",
     "Comparative : « The arena is ___ (big) than most stadiums. »"),
    ("B2", "Whether", "whether introduit une subordonnée en « si »",
     "Whether : « ___ this year will be faster, nobody knows yet. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "Compléter", k, nt, body, size=20.5, gap=8)

# ---- E. translation ----
bf.head("E　TRANSLATION　Traduction", 24, gap=8)
e_items = [
    ("B2", "La patience fait partie du système, et non un échec de celui-ci.", "part of = une partie de ; not a failure = pas un échec",
     "Translate : « Patience is part of the system, not a failure of it. »"),
    ("A2", "Le mercredi 11 novembre, à 11 h, la Grande-Bretagne observe deux minutes de silence.", "at 11 a.m.；two minutes of silence",
     "Traduis : At 11 a.m. on Wednesday, November 11, Britain holds two minutes of silence."),
    ("B1", "Ce dimanche, la NFL joue à Munich.", "on Sunday；in Munich",
     "Traduis : On Sunday, the NFL plays in Munich."),
    ("B1", "Chaque pays ne l’appelle pas de la même façon.", "not every = pas chaque ; call = appeler",
     "Translate : « Not every country calls it by the same name. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "Traduction", k, nt, body, size=20.5, gap=8)

# ---- F. matching ----
bf.head("F　WORDS　Mots à associer", 24, gap=8)
bf.match_set("B1", "Appariement",
             ["a silence", "an armistice", "a runoff", "a miser"],
             ["the second vote, when no one wins a majority",
              "a quiet time with no speaking",
              "an agreement to stop fighting",
              "a person who loves money and hates spending it"],
             ["b", "c", "a", "d"],
             ["silence = le silence b", "armistice = l’armistice c", "runoff = le second tour a", "miser = l’avare d"],
             instr="Associez")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ticket", "ticket = le billet"),
    ("A2", "line", "line = la file d’attente (anglais américain)"),
    ("A2", "scarf", "scarf = l’écharpe"),
    ("A2", "anthem", "anthem = l’hymne"),
    ("B1", "Sunday", "Le match a lieu le dimanche 15 novembre"),
]
gnums = [reg_ex(lv, "Dialogue à compléter", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　À compléter", 24, gap=8)
bf.para(f"— Good morning ! Is this the way to the Allianz Arena ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long ? — No, five minutes only. It is my first NFL game. What do I do with the ({gnums[2]})___ ? — Wear it with pride, and cheer for the Lions. — And the famous ({gnums[3]})___ ? — Two anthems, one game. Enjoy Munich. — I will ! See you on ({gnums[4]})___ ! — Have a good day.", 20.5)
bf.para("Levels : 145–148 [A2] · 149 [B1]", 19.5, "sans", False, GREY, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "Écriture", "Tâche ouverte — points dans le cadre d’écriture ; texte modèle dans le cadre de cette page", "Noté sur les points")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　WRITING　Écriture [B1]", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Wednesday, November 11 ». Tell us : did you stand still at eleven, what did you wear, what did you watch on Friday — and one sentence about the game in Munich on Sunday. The best texts will appear in VOL.4 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "Écris en anglais (80–100 mots) : « Mon mercredi 11 novembre ». Dis si tu es resté immobile à 11 h, ce que tu portais, ce que tu as regardé vendredi — et une phrase sur le match de Munich dimanche.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, "MODEL　Texte modèle", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Wednesday, November 11, our school stopped for two minutes. At eleven o'clock, the hall went quiet, and I thought about the soldiers of the First World War. In the evening, we watched the news from London, and my mother wore her poppy at dinner. On Friday, we baked 26 cakes for Children in Need, and Pudsey smiled from the television. On Sunday, we watched the game from Munich. It was a week of silence, kindness and sport — and I slept well, because I had remembered.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANSWERS　Toutes les réponses commentées (pages 1 à 8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Page {pg} —", 16, "sans", True, OLIVE, 1.26, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13.5, "sans", False, INK, 1.26, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
