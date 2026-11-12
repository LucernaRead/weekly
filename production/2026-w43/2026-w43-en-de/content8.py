# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS　Übungen & Antworten", "The Lucerna", "FINAL TEST　Abschlusstest　Answers at the bottom of this page")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "C", "31. Oktober = Halloween"),
    ("A2", "A", "carve = eine Kürbislaterne schnitzen"),
    ("B1", "B", "neither … nor = weder … noch"),
    ("A2", "A", "costume = Halloween-Kostüm"),
    ("A2", "B", "she (3. Person) → wears"),
    ("A2", "B", "trick or treat bringt Süßigkeiten"),
    ("B1", "A", "will + Grundform: fall"),
    ("B1", "C", "be going to → is going"),
]
cnums = [reg_ex(lv, "Lückentext", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　CLOZE　Lückentext", 24, gap=8)
bf.para(f"Maya is twelve. On Saturday, October 31, it is ({cnums[0]})___. In the morning, she helps her father ({cnums[1]})___ a pumpkin on the porch. « ({cnums[2]})___ rain nor cold can stop us », laughs her mother. In the evening, Maya puts on her ({cnums[3]})___ : she ({cnums[4]})___ a gold crown, like a Greek goddess. She takes her bag and goes from house to house : « Trick or treat ! » The neighbours give her ({cnums[5]})___. At nine o'clock, the street is quiet — and in the night, the clocks will ({cnums[6]})___ back : one more hour of sleep ! Tomorrow, Maya is ({cnums[7]})___ to sleep late, very late.", 21.5)
bf.bridge("Die Auswahl:")
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
bf.head("B　MULTIPLE CHOICE　Auswahl", 24, gap=8)
mcq = [
    ("A2", "B", "9:15 = a quarter past nine", "The game starts at 9:15. In words : ... A. a quarter to nine · B. a quarter past nine · C. half past nine"),
    ("A2", "A", "we → get (Grundform)", "On Sunday, we ___ an extra hour of sleep. A. get · B. gets · C. getting"),
    ("B1", "B", "Spiel vorbei → won", "The 76ers ___ the game 106–100. A. win · B. won · C. wins"),
    ("B1", "B", "than → Komparativ: hotter", "Austin is ___ than Milwaukee in October. A. hot · B. hotter · C. hottest"),
    ("B2", "A", "despite + Nomen: trotz Regen", "___ the rain, the parade went on all evening. A. Despite · B. Because · C. Unless"),
    ("B2", "A", "whether = ob", "Nobody knows ___ the Brewers will win the Series. A. whether · B. what · C. who"),
    ("A2", "A", "Vergangenheit → opened", "Early voting in Texas ___ on Monday. A. opened · B. open · C. opens"),
    ("B1", "A", "be going to + Grundform: cast", "She is going to ___ her ballot on Saturday. A. cast · B. casts · C. casted"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "Multiple Choice", k, nt, body, size=20.5, gap=8)

# ---- C. reading ----
bf.head("C　READING　Leseverstehen", 24, gap=8)
bf.para("On Monday morning, Rosa Delgado, a nurse from Houston, finished her night work at six o'clock. She did not go home to sleep. She drove to the early-voting place near the hospital and joined a short line. « On November 3, I work all day », she explains. « Today, I have time. » Ten minutes later, her ballot was in the box, and a sticker on her jacket said : I VOTED EARLY. By Friday, October 30, when early voting ends in Texas, millions of Texans will do the same.", 21.5)
read_qs = [
    ("A2", "B", "Im Text: a nurse from Houston", "Rosa is... A. a teacher · B. a nurse · C. a driver"),
    ("A2", "B", "Am 3. November arbeitet sie den ganzen Tag", "She voted early because on November 3 she... A. travels · B. works all day · C. sleeps"),
    ("B1", "A", "Auf dem Sticker steht: I VOTED EARLY", "Her sticker said... A. I VOTED EARLY · B. VOTE ON TUESDAY · C. TEXAS FIRST"),
    ("B1", "B", "Texas: Ende der Frühwahl am 30. Oktober", "Early voting in Texas ends on... A. October 19 · B. October 30 · C. November 3"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "Leseverstehen", k, nt, body, size=20.5, gap=8)

# ---- D. sentence building ----
bf.head("D　SENTENCES　Sätze formen", 24, gap=8)
d_items = [
    ("A2", "On Saturday, they are going to carve a pumpkin.", "are going to + Grundform",
     "Be going to : « On Saturday, they (carve) a pumpkin. » → ___"),
    ("B1", "The Knicks raised their first banner since 1973.", "raise → raised (regelmäßig)",
     "Past simple : « The Knicks (raise) their first banner since 1973. »"),
    ("B1", "scarier", "scary → scarier (y wird zu i + er)",
     "Comparative : « My costume is ___ (scary) than yours. »"),
    ("B2", "Whether", "whether leitet einen Ob-Satz ein",
     "Whether : « ___ the parade will happen, nobody knows. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "Satzergänzung", k, nt, body, size=20.5, gap=8)

# ---- E. translation ----
bf.head("E　TRANSLATION　Übersetzung", 24, gap=8)
e_items = [
    ("B2", "Das Wählen ist nicht länger ein Tag; es ist eine Jahreszeit.", "no longer = nicht länger",
     "Translate : « Voting is no longer a day ; it is a season. »"),
    ("A2", "The 76ers won the game 106–100.", "win → won; Ergebnis 106–100",
     "Übersetze: Die 76ers siegten 106 zu 100."),
    ("B1", "This year, early voting opened on Monday.", "open → opened; on Monday",
     "Übersetze: Die vorzeitige Stimmabgabe begann dieses Jahr am Montag."),
    ("B1", "Keiner der beiden Klubs hat je die World Series gewonnen.", "neither = keiner von beiden; has ever won = Present Perfect",
     "Translate : « Neither club has ever won the Series. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "Übersetzung", k, nt, body, size=20.5, gap=8)

# ---- F. matching ----
bf.head("F　WORDS　Zuordnung", 24, gap=8)
bf.match_set("B1", "Zuordnung",
             ["a midterm", "an incumbent", "a margin", "turnout"],
             ["the number of people who vote", "an election in the middle of a president's term",
              "the person who holds the job now", "the difference between two results"],
             ["b", "c", "d", "a"],
             ["midterm = Zwischenwahl b", "incumbent = Amtsinhaber c", "margin = Abstand d", "turnout = Wahlbeteiligung a"],
             instr="Ordne zu", gap=8)

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ID", "Beim Wählen den Ausweis (ID) zeigen"),
    ("A2", "line", "line = Schlange (amerikanisches Englisch)"),
    ("A2", "ballot", "ballot = Stimmzettel"),
    ("A2", "sticker", "sticker = Aufkleber"),
    ("B1", "November", "Wahltag ist der 3. November"),
]
gnums = [reg_ex(lv, "Dialogergänzung", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　Dialog", 24, gap=8)
bf.para(f"— Good morning ! Is this the early-voting place ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long today ? — No, five minutes only. Yesterday it was very long ! — Good. It is my first early vote. What do I do with the ({gnums[2]})___ ? — Mark your choices, check them twice, then put it in the box. — Thank you. And the famous ({gnums[3]})___ ? Everybody has one on their jacket. — The sticker ! Here it is : « I VOTED ». Wear it with pride. — I will ! See you on ({gnums[4]})___ 3rd, in the results ! — Ha ! Have a good day.", 21.5)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "Schreiben", "Offene Aufgabe — Stichpunkte im Schreibkasten; Mustertext im Kasten auf Seite 8", "Bewertung nach Stichpunkten")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　WRITING　Schreiben", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Saturday, October 31 ». Tell us : your costume, your street, the candy, the pumpkins — and one sentence about the clocks that fall back in the night. The best texts will appear in VOL.2 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "Schreibe auf Englisch (80–100 Wörter): « Mein Samstag, der 31. Oktober ». Beschreibe dein Kostüm, deine Straße, die Süßigkeiten und die Kürbisse — und einen Satz über die Uhren, die in der Nacht zurückgestellt werden.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, "MODEL　Mustertext", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Saturday, October 31, our street becomes a small Halloween town. In the morning, I carve a pumpkin with my father and we put a candle inside. At six o'clock, I wear my pirate costume and take my bag. House after house, I say « Trick or treat ! » and the neighbours smile and give me candy. My bag is heavy at nine o'clock ! In the night, the clocks fall back, so I sleep one hour more on Sunday. It is my favourite weekend of the autumn.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANSWERS　Alle Antworten mit Anmerkungen (Seiten 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Seite {pg} —", 16, "sans", True, OLIVE, 1.26, 3)
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
