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
    ("A2", "B", "Der 3. November ist ein Dienstag"),
    ("A2", "A", "pizza = Pizza"),
    ("B1", "C", "map = Karte, die sich Bundesstaat für Bundesstaat färbt"),
    ("A2", "B", "close = knapp"),
    ("A2", "A", "sticker = Aufkleber"),
    ("A2", "C", "will + Grundform know"),
    ("B1", "B", "be going to → is going"),
    ("B1", "A", "still = weiterhin"),
]
cnums = [reg_ex(lv, "Lückentext", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　CLOZE　Lückentext", 24, gap=8)
bf.para(f"Leo is sixteen. On Tuesday, November 3, it is ({cnums[0]})___. His family does not cook dinner : they order ({cnums[1]})___. On television, the ({cnums[2]})___ changes colour, state by state. « Ohio is very ({cnums[3]})___ ! » says his father. At nine o'clock, Leo's mother comes home from voting, with a ({cnums[4]})___ on her jacket : « I VOTED ». « When ({cnums[5]})___ we know the results ? » asks Leo. « Tomorrow », says his mother. « Tomorrow, Leo is ({cnums[6]})___ to read the results at school — and the map will ({cnums[7]})___ be on television tonight. »", 21.5)
bf.bridge("Optionen:")
for n, (lv, _k, _nt), opts in zip(cnums, cloze_defs, [
    "A. Monday · B. Election Day · C. Halloween",
    "A. pizza · B. salad · C. soup",
    "A. phone · B. table · C. map",
    "A. far · B. close · C. big",
    "A. sticker · B. hat · C. ticket",
    "A. do · B. are · C. will",
    "A. goes · B. going · C. go",
    "A. still · B. never · C. soon",
]):
    bf.para(f"{n}. [{lv}] {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B　MULTIPLE CHOICE　Auswahl", 24, gap=8)
mcq = [
    ("A2", "B", "1:30 = half past one", "The clocks show 1:30. In words : ... A. one o'clock · B. half past one · C. a quarter to one"),
    ("A2", "A", "we → get (Grundform)", "On Sunday, we ___ an extra hour of sleep. A. get · B. gets · C. getting"),
    ("B1", "B", "Vergangenes: fell", "The clocks ___ back on Sunday. A. fall · B. fell · C. falling"),
    ("B1", "B", "than → Komparativ bigger", "The Bernabéu is ___ than most stadiums. A. big · B. bigger · C. biggest"),
    ("B2", "A", "despite + Substantiv: trotz Regen", "___ the rain, the game went on all evening. A. Despite · B. Because · C. Unless"),
    ("B2", "A", "whether = ob", "Nobody knows ___ the race is called yet. A. whether · B. what · C. who"),
    ("A2", "A", "Futur: will + Grundform", "The film ___ on Friday, November 6. A. will open · B. will opened · C. will opens"),
    ("B1", "A", "be going to + Grundform vote", "They are going to ___ on Tuesday. A. vote · B. votes · C. voted"),
    ("B1", "C", "too close to call = zu knapp, um es zu entscheiden", "« Too close to call » means... A. the winner is clear · B. voting is over · C. we do not know yet"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "Multiple Choice", k, nt, body, size=20.5, gap=8)

# ---- C. reading ----
bf.head("C　READING　Leseverstehen", 24, gap=8)
bf.para("On Saturday morning, Sam, a teacher from Ohio, finished his breakfast and walked to the early-voting place near his school. There was no line. « On Tuesday, I teach all day », he explains. « Today, I have time. » Five minutes later, his ballot was in the box, and a sticker on his jacket said : I VOTED. On Tuesday night, Sam watched the map with his family — and Ohio was, as always, too close to call.", 21.5)
read_qs = [
    ("A2", "B", "Im Text: a teacher from Ohio", "Sam is... A. a nurse · B. a teacher · C. a driver"),
    ("A2", "B", "Am Dienstag unterrichtet er den ganzen Tag", "He voted early because on Tuesday he... A. travels · B. teaches all day · C. sleeps"),
    ("B1", "A", "Auf dem Aufkleber steht I VOTED", "His sticker said... A. I VOTED · B. VOTE ON TUESDAY · C. OHIO FIRST"),
    ("B1", "B", "Ohio ist wie immer zu knapp, um es zu entscheiden", "On Tuesday night, Ohio was... A. clear · B. too close to call · C. finished early"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "Leseverstehen", k, nt, body, size=20.5, gap=8)

# ---- D. sentence building ----
bf.head("D　SENTENCES　Sätze formen", 24, gap=8)
d_items = [
    ("A2", "On Friday, they are going to watch the cat film.", "are going to + Grundform",
     "Be going to : « On Friday, they (watch) the cat film. » → ___"),
    ("B1", "The clocks fell back on Sunday.", "fall → fell (unregelmäßig)",
     "Past simple : « The clocks (fall) back on Sunday. »"),
    ("B1", "taller", "tall → taller (Komparativ)",
     "Comparative : « The hat is ___ (tall) than the Cat. »"),
    ("B2", "Whether", "whether leitet einen Ob-Satz ein",
     "Whether : « ___ the race is called, nobody knows yet. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "Satzergänzung", k, nt, body, size=20.5, gap=8)

# ---- E. translation ----
bf.head("E　TRANSLATION　Übersetzung", 24, gap=8)
e_items = [
    ("B2", "Geduld ist Teil des Systems, nicht ein Versagen des Systems.", "part of = ein Teil von; not a failure = kein Versagen",
     "Translate : « Patience is part of the system, not a failure of it. »"),
    ("A2", "Tuesday, November 3, is Election Day in the United States.", "Wahltag = Election Day; am Dienstag = on Tuesday",
     "Übersetze: Dienstag, der 3. November, ist Wahltag in den Vereinigten Staaten."),
    ("B1", "On Sunday, the NFL plays in Madrid.", "an diesem Sonntag = on Sunday; in Madrid = in Madrid",
     "Übersetze: An diesem Sonntag spielt die NFL in Madrid."),
    ("B1", "Nicht jeder Ort stellt die Uhren zurück.", "not every = nicht jeder; changes = stellt zurück",
     "Translate : « Not every place changes. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "Übersetzung", k, nt, body, size=20.5)

# ---- F. matching ----
bf.head("F　WORDS　Zuordnung", 24, gap=8)
bf.match_set("B1", "Zuordnung",
             ["a midterm", "a governor", "a ballot", "turnout"],
             ["the number of people who vote",
              "an election in the middle of a term",
              "the person who leads a state",
              "the paper you mark your choice on"],
             ["b", "c", "d", "a"],
             ["midterm = Zwischenwahl b", "governor = Gouverneur c", "ballot = Stimmzettel d", "turnout = Wahlbeteiligung a"],
             instr="Ordne zu")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ID", "Beim Wählen den Ausweis (ID) zeigen"),
    ("A2", "line", "line = Schlange (amerikanisches Englisch)"),
    ("A2", "ballot", "ballot = Stimmzettel"),
    ("A2", "sticker", "sticker = Aufkleber"),
    ("B1", "Tuesday", "Wahltag ist Dienstag, der 3. November"),
]
gnums = [reg_ex(lv, "Dialogergänzung", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　Dialog", 24, gap=8)
bf.para(f"— Good morning ! Is this the voting place ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long today ? — No, five minutes only. On Tuesday it will be very long ! — Good. It is my first vote. What do I do with the ({gnums[2]})___ ? — Mark your choices, check them twice, then put it in the box. — Thank you. And the famous ({gnums[3]})___ ? Everybody has one on their jacket. — The sticker ! Here it is : « I VOTED ». Wear it with pride. — I will ! See you on ({gnums[4]})___ , in the results ! — Ha ! Have a good day.", 21.5)
bf.para("Levels : 145–148 [A2] · 149 [B1]", 19.5, "sans", False, GREY, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "Schreiben", "Offene Aufgabe — Stichpunkte im Schreibkasten; Mustertext im Kasten auf Seite 8", "Bewertung nach Stichpunkten")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　WRITING　Schreiben [B1]", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Tuesday, November 3 ». Tell us : did you watch the results, what did you eat, what did the map show — and one sentence about the clocks that fell back on Sunday night. The best texts will appear in VOL.3 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "Schreibe auf Englisch (80–100 Wörter): « Mein Dienstag, der 3. November ». Beschreibe, ob du die Ergebnisse verfolgt hast, was du gegessen hast, was die Karte gezeigt hat — und einen Satz über die Uhren, die in der Sonntagnacht zurückgestellt wurden.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, "MODEL　Mustertext", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Tuesday, November 3, our family watched the election results at home. We ate pizza, because nobody wanted to cook on such a night. On television, the map changed colour, state by state, and my father said : « Ohio is too close to call ! » I did not understand every state, but I understood the pizza and the excitement. On Sunday night, the clocks had fallen back, so I slept one hour more. It was a long night, and a very American one.", 21, "serif", False, INK, mw2 - 44, 1.42)

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
