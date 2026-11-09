# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · FRONT PAGE (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "WEEKLY IN ENGLISH　Jede Woche neu　Was die englischsprachige Welt gerade bewegt", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "WEEK OF NOVEMBER 9 TO 15, 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "The Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "ENGLISCHES WOCHENBLATT　VOL.3　GEDENKEN　FUSSBALL　FILME", 36, "serif", True, OLIVE, anchor="middle", spacing=7.4)
p.text(975, 372, "ENGLISCHER TEXT　DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# dark band: eleven eleven
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "ELEVEN ELEVEN — AND TWO MINUTES OF SILENCE !", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Wednesday, November 11, at 11 a.m., Britain, Canada, Australia and America stop for two minutes.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "11. November, 11 Uhr", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "Veterans Day　Remembrance Day　Siehe Seite 2", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "THE BIG STORY　Schlagzeile", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Eleven Eleven : The Two Minutes When the English-Speaking World Stops", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "By The Lucerna newsroom　Reading level : A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("On Wednesday, November 11, at eleven o'clock in the morning, something quiet happens across the English-speaking world. In London, Ottawa, Canberra and Washington, people stop what they are doing, and for two minutes they stand still and say nothing. It is the two-minute silence — for the soldiers who died in war, and for all who served.")
f.para("The date is not an accident. At 11 a.m. on November 11, 1918, the guns of the First World War fell silent. The armistice — the agreement to stop fighting — began at the eleventh hour of the eleventh day of the eleventh month. In Britain it is Remembrance Day ; in the United States, Veterans Day, for all who served.")
f.para("The symbol is the poppy, a small red flower. Poppies grew on the battlefields of Flanders, where so many soldiers died. People wear a paper poppy in November, to help veterans and their families. In London, the King leads the National Act of Remembrance at the Cenotaph in Whitehall — the monument to the dead with no grave of their own.")
f.para("This week is full of other dates too. On Friday, November 13, the BBC's Children in Need appeal fills British television, and a new Scrooge comes to the cinema. On Sunday, November 15, American football comes to Munich, tennis opens its season finale in Turin, and England play Spain in Madrid.")
f.para("And one promise from last issue : the midterm election results. This issue went to press on November 2, before the November 3 vote — so it prints no results, and invents none. Page 6 explains why counting takes time. Welcome back to VOL.3 !")
f.bridge("Erklärung | an armistice = Waffenstillstand · a veteran = Veteran · to fall silent = verstummen.", size=19.5)
f.box("THE WEEK IN NUMBERS　Zahlen", [
    ("Nov 11, 11:00 — Stille · 1918 — Waffenstillstand", "serif", False, INK, 20.5, 1.35),
    ("Nov 13 (Fr) — Children in Need + Ebenezer · Nov 15 (So) — NFL München + ATP Finals", "serif", False, INK, 20.5, 1.35),
])
f.head("TRY IT NOW　Jetzt üben", 25)
f.ex("A2", "Satzergänzung", "armistice", "armistice = Waffenstillstand",
     "The fighting stopped with an ___ in 1918.", size=20.5)
f.ex("A2", "Satzergänzung", "veteran", "veteran = Veteran",
     "A ___ is a person who served in the armed forces.", size=20.5)
f.ex("A2", "Satzergänzung", "November 11", "Gedenktag am 11. November (Mittwoch)",
     "The silence is on Wednesday, ___.", size=20.5)
f.ex("A2", "Satzergänzung", "poppy", "poppy = Mohnblume",
     "People wear a red ___ in November.", size=20.5)
f.ex("B1", "Satzergänzung", "silent", "fall silent = verstummen",
     "At 11 a.m., the guns fell ___.", size=20.5)
f.ex("B1", "Satzergänzung", "two", "two minutes = zwei Minuten",
     "The silence lasts ___ minutes.", size=20.5)
f.end_report()

# ---- searches chart (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 668, fill=BOX)
p.text(gx + 22, gy + 40, "SEARCHES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "OF THE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Diese Woche gesucht　Google Trends", 19, "sans", False, GREY)
gt = [
    ("veterans day", 250),
    ("nfl munich", 218),
    ("ebenezer", 186),
    ("children in need", 140),
    ("atp finals", 108),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE)
    byy += 92
p.text(gx + 22, byy + 16, "Snapshots, early November :", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "search interest changes during the day.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "Relative Beliebtheit, keine exakten Suchzahlen.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1280
p.rect(gx, sy, gw, 372, fill="#f0eee5")
p.text(gx + 22, sy + 40, "IN THIS ISSUE　Inhalt", 24, "sans", True, OLIVE)
som = [
    ("p.2", "Silence, poppies & Pudsey", "A2"),
    ("p.3", "Scrooge comes to town", "A2→B1"),
    ("p.4", "Munich, Turin & Madrid", "B1"),
    ("p.5", "Pudsey and the 26 challenge", "B1"),
    ("p.6", "Why counting takes time", "B2"),
    ("p.7", "Phrases of the week", "A2→B2"),
    ("p.8", "Exercises & answers", "all"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 72, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "THE WORD OF THE WEEK", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "« remembrance »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "the act of remembering those who died in war.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "Gedenken. Remembrance Day = Gedenktag.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "poppyfield.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "A field of poppies, painted by Claude Monet. The poppy is the flower of remembrance : it grew on the battlefields of Flanders, and it is worn every November.",
        "Claude Monet — public domain, via Wikimedia Commons")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-countries")
f2.head("FOUR COUNTRIES, ONE MINUTE", 25)
f2.para("One silence, four names. In the United States it is Veterans Day. In Britain it is Remembrance Day. In Canada and Australia, the name is the same too — with the same poppy and the same 11 a.m. silence.", 22.5)
f2.para("Remember on Wednesday, laugh on Friday, watch sport on Sunday. See you on page 2 !", 22.5)
f2.end_report()
# col 3 IN BRIEF
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX)
p.text(bx + 22, 1914, "IN BRIEF　Kurz gemeldet", 24, "sans", True, OLIVE)
brefs = [
    ("ELECTION", "Nov 3 : Americans voted. Press time Nov 2 : no results, none invented. (p. 6)"),
    ("SILENCE", "Wed, Nov 11, 11 a.m. : two minutes of silence in Britain, Canada, Australia, US. (p. 2)"),
    ("MUNICH", "Sunday, November 15 : Patriots–Lions, Allianz Arena, Munich, 3:30 p.m. (p. 4)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "LIGHTNING QUIZ　Blitzquiz", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lies Seite 1, wähle die richtige Antwort　Lösungen auf Seite 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "Multiple Choice", "B", "Stille am Mittwoch, 11. November",
      "The two-minute silence is on... A. November 13 · B. Wednesday, November 11 · C. November 15", size=21)
qf.ex("A2", "Multiple Choice", "C", "Waffenstillstand im Jahr 1918",
      "The armistice began in... A. 1914 · B. 1939 · C. 1918", size=21)
qf.ex("A2", "Multiple Choice", "A", "Die Menschen tragen eine rote Mohnblume",
      "People wear... A. a red poppy · B. a white hat · C. a blue ribbon", size=21)
qf.ex("A2", "Multiple Choice", "B", "NFL-Spiel in München am Sonntag, 15. November",
      "The NFL game in Munich is on... A. Friday · B. Sunday, November 15 · C. Tuesday", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LIFE　Leben", "The Lucerna", "LEVEL A2　Silence, poppies & your week　Stille, Mohn und deine Woche")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Wednesday, November 11 : Two Minutes That Stop a Country", 32)
f.byline("By The Lucerna newsroom　Reading level : A2")
f.para("On Wednesday, November 11, at 11 a.m., Britain stops. Buses stop. Shops go quiet. In schools, children stand still. For two minutes, nobody speaks. The silence remembers the soldiers who died in the First World War — and in every war since.")
f.para("Why eleven eleven ? The First World War ended at 11 a.m. on November 11, 1918. The armistice was signed that morning, and the guns stopped. In 1920, Britain built the Cenotaph in Whitehall, London — a stone monument with no body inside it, for all the dead. Every year since, people have gathered there.")
f.para("In Canada, Australia and New Zealand, the day is the same : Remembrance Day, the same poppy, the same silence at 11 a.m. In the United States, November 11 is Veterans Day — a day for all veterans, living and dead. The names are different. The silence is the same.")
f.para("The poppy is small, red and paper. Volunteers sell it on streets and in shops, and the money helps veterans and their families. Many people wear it on the left, near the heart — and they wear it all through November, until the day itself is past.")
f.para("And what about the weekend just gone ? On Sunday, November 8, it was Remembrance Sunday in Britain — the main ceremony, three days before Armistice Day itself. And in India and in Indian homes around the world, Sunday, November 8, was Diwali, the festival of lights : a five-day festival of lamps, sweets and family, with the main night on Sunday. Two festivals of light and memory, one weekend — both just passed, not coming.")
f.para("This week looks forward too. On Wednesday, November 11, shoppers mark Singles' Day — 11.11, the biggest online shopping day in China, now copied around the world. On Friday, November 13, Britain's Children in Need appeal takes over television. Page 5 has the story of Pudsey the bear.")
f.box("ELEVEN ELEVEN　Elf Uhr elf", [
    ("11 a.m. on the 11th day of the 11th month : the eleventh hour. Two minutes of silence — 120 seconds. Tradition says the first minute is for the dead, the second for the living who came home.", "serif", False, INK, 21.5, 1.4),
])
f.head("WHAT IS ON THIS WEEK ?", 25)
f.para("Second story of the week — and it is on your screen. On Friday, November 13, two films open : « Ebenezer », a dark new Scrooge from Dickens, and « How to Rob a Bank », a heist comedy. One ghost story, one bank story — and both for a Friday night out.", 23.5)
f.para("On television, the week is just as full. The Children in Need appeal show is live on Friday night, and the ATP Finals begin in Turin on Sunday. Page 3 has the film guide, page 4 the sport.", 23.5)
f.para("How do you say the time of the silence ? « At eleven o'clock — eleven eleven. » is the sentence of the week. The phrase box below shows three ways to say it.", 23.5)
f.gloss("Erklärung | a silence = Stille · an armistice = Waffenstillstand · a poppy = Mohnblume · a veteran = Veteran.")
f.end_report()

# col 3: image + facts (sequential, measured)
ix = COLX[3]
image(p, "cenotaph1920.jpg", ix, 200, CW, 440)
cy3 = caption(p, ix, 640, CW, "The Cenotaph in Whitehall, London, at its unveiling on November 11, 1920. More than a century later, the same stone is still the centre of Britain's Remembrance Sunday.",
              "Horace Nicholls — public domain, via Wikimedia Commons")
sav = ["The Cenotaph was unveiled on November 11, 1920 — two years after the armistice.",
       "The two-minute silence is held at 11 a.m. on November 11 in Britain, Canada, Australia and New Zealand.",
       "Diwali's main night was Sunday, November 8 : lamps, sweets and family, on the darkest night of the lunar month."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in sav) + 14
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DID YOU KNOW ?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "And you ? Do you wear a poppy in November ? What does your country do on November 11 ? Write two sentences in English for VOL.4."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Was macht dein Land am 11. November? Schreibe zwei Sätze an die Redaktion.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "AND YOU ?　Und du ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Was macht dein Land am 11. November? Schreibe zwei Sätze an die Redaktion.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Say it wide box ----
dy = 1570
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "SAY IT : ELEVEN ELEVEN　So sagt man die Uhrzeit", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "The silence, in three sentences　Die Stille in drei Sätzen", 20, "sans", False, GREY, anchor="end")

def phrase_panel(cx, label, sub):
    p.rect(cx - 140, dy + 66, 280, 132, fill="#f0eee5")
    p.text(cx, dy + 126, label, 20, "serif", True, INK, anchor="middle")
    p.text(cx, dy + 168, sub, 20, "sans", False, GREY, anchor="middle")

phrase_panel(299, "At eleven o'clock.", "11 Uhr vormittags.")
phrase_panel(750, "Two minutes of silence.", "Zwei Minuten Stille.")
phrase_panel(1200, "We will remember them.", "Wir vergessen sie nicht.")
lx = 1370
ly = dy + 66
for line in [
    ("remember", "= to keep in your mind (behalten)"),
    ("silent", "= saying nothing (nichts sagen)"),
    ("to honour", "= to show respect (Respekt zeigen)"),
    ("a ceremony", "= a formal event (Veranstaltung)"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 140, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 40
p.para(lx, ly + 24, "This week : on Wednesday, November 11, at 11 a.m., the silence begins. Two minutes — for the dead, and for all who served.", 19, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 340
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCISES　Übungen zu Seite 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8　Nach Nummern suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P2-ex")
e.head("A　THE DATE", 25)
e.bridge("Ergänze die Sätze auf Englisch nach Datum und Uhrzeit.")
e.ex("A2", "Satzergänzung", "eleven", "11 Uhr = eleven o'clock",
     "The silence begins at ___ o'clock.", instr="Ergänze", size=22, gap=9)
e.ex("A2", "Satzergänzung", "November", "11. Monat = November",
     "Remembrance Day is on 11 ___.", instr="Ergänze", size=22, gap=9)
e.ex("A2", "Satzergänzung", "two", "zwei Minuten = two minutes",
     "The silence lasts ___ minutes.", instr="Ergänze", size=22, gap=9)
e.ex("A2", "Satzergänzung", "poppy", "poppy = Mohnblume",
     "People wear a red ___ in November.", instr="Ergänze", size=22, gap=9)
e.ex("A2", "Satzergänzung", "1918", "Jahr des Waffenstillstands: 1918",
     "The armistice began in ___.", instr="Ergänze", size=22, gap=9)
e.head("B　WILL", 25)
e.bridge("Schreibe mit will + Verb um (Versprechen und was geschehen wird).")
e.ex("A2", "Umformung", "They will remember them.", "they → will remember",
     "They (remember) them. → ___", instr="Schreibe um", gap=9)
e.ex("A2", "Umformung", "She will wear a poppy.", "she → will wear",
     "She (wear) a poppy. → ___", instr="Schreibe um", gap=9)
e.ex("A2", "Umformung", "We will stand still.", "we → will stand",
     "We (stand) still. → ___", instr="Schreibe um", gap=9)
e.ex("B1", "Umformung", "Will they watch the ceremony ?", "Fragesatz: will steht vorn",
     "They (watch) the ceremony ? → ___", instr="Schreibe um", gap=9)
e.head("C　COMPREHENSION", 25, gap=8)
e.bridge("Lies Seite 2, wähle die richtige Antwort.", gap=5)
e.ex("A2", "Multiple Choice", "B", "Die Stille beginnt um 11 Uhr vormittags",
     "The silence begins at... A. 10 a.m. · B. 11 a.m. · C. noon", size=22, gap=9)
e.ex("A2", "Multiple Choice", "C", "Das Denkmal wurde 1920 enthüllt",
     "The Cenotaph was unveiled in... A. 1918 · B. 1919 · C. 1920", size=22, gap=9)
e.ex("A2", "Multiple Choice", "A", "Diwalis Hauptabend war Sonntag, der 8. November",
     "Diwali's main night was... A. Sun, Nov 8 · B. Wed, Nov 11 · C. Fri, Nov 13", size=22, gap=9)
e.ex("A2", "Multiple Choice", "B", "In den USA heißt der Tag Veterans Day",
     "In the US, November 11 is... A. Remembrance Day · B. Veterans Day · C. Singles' Day", size=22, gap=9)
e.head("D　THE WORDS", 25, gap=8)
e.match_set("A2", "Zuordnung",
            ["a poppy", "an armistice", "a veteran", "a ceremony"],
            ["a red flower worn in November",
             "an agreement to stop fighting",
             "a person who served in the forces",
             "a formal public event"],
            ["a", "b", "c", "d"],
            ["poppy = Mohnblume a", "armistice = Waffenstillstand b", "veteran = Veteran c", "ceremony = Feier d"],
            instr="Ordne zu", gap=6)
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-life.svg")
print("P2 saved, exercises so far:", len(REG))
