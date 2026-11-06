# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/en-it-proof/freeze/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · FRONT PAGE (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2", 23, "sans", True, OLIVE)
p.text(975, 92, "WEEKLY IN ENGLISH · UN NUMERO OGNI SETTIMANA · L'INGLESE CHE LEGGE L'AMERICA", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "WEEK OF NOVEMBER 2 TO 8, 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "The Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SETTIMANALE IN INGLESE · VOL.2 · ELEZIONI · FOOTBALL · FILM", 46, "serif", True, INK, anchor="middle")
p.text(975, 372, "TESTI IN INGLESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI", 19.5, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# dark band: election + clocks
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "AMERICA VOTES ON TUESDAY — AND THE CLOCKS FELL BACK !", 38, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Election Day is Tuesday, November 3. On Sunday, November 1, America turned its clocks back one hour.", 23.5, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "MARTEDÌ ELEZIONI · DOMENICA ORA INDIETRO", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "Elezioni martedì 3 novembre · Vedi p. 6", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "THE BIG STORY · Titolo", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "America Votes : Election Day Comes on Tuesday, November 3", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "By The Lucerna newsroom · Reading level : A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Tuesday, November 3, is Election Day in the United States. It is a midterm election — an election in the middle of a president's four-year term. All 435 seats in the House of Representatives are on the ballot, along with about a third of the Senate and governorships in many states.")
f.para("In many states, voting has already started. Early voting lets people vote before Election Day : you go to a voting place, you show your ID, you mark your ballot, and your vote counts on election night. On Tuesday, the voting places open early in the morning and close in the evening.")
f.para("What happens on Tuesday night ? Television channels show maps that slowly change colour, state by state. But nobody should expect every result at midnight : each state runs its own election, and counting takes time. Some races are called on Tuesday night ; others take days.")
f.para("And that is only half of the week. On Friday, November 6, two big films open in cinemas. On Sunday, November 8, American football goes to Madrid, Spain, and Formula 1 races in São Paulo, Brazil. Our sport dossier is on page 4.")
f.para("This is the second issue of The Lucerna in English. Last issue promised real readers' letters — and this week, our Readers' Corner on page 7 tells you honestly where those letters stand. Welcome back !")
f.bridge("Spiegazione | a midterm = medio termine · a ballot = scheda · a race = corsa · to call a race = proclamare il vincitore.", gap=5)
f.box("THE WEEK IN NUMBERS · In cifre", [
    ("Nov 3 — Election Day (elezioni) · 435 — seats in the House, all on the ballot (tutti i 435 seggi da rieleggere)", "serif", False, INK, 20.5, 1.35),
    ("Nov 6 — two films open (due film in uscita) · Nov 8 — NFL in Madrid + F1 in São Paulo (due gare domenica)", "serif", False, INK, 20.5, 1.35),
], gap=6)
f.head("TRY IT NOW · Prova subito", 25, gap=8)
f.ex("A2", "Completare le frasi", "ballot", "ballot = scheda elettorale",
     "You mark your choice on a ___ and put it in the box.", size=20.5)
f.ex("A2", "Completare le frasi", "midterm", "midterm = elezioni di medio termine",
     "An election in the middle of a term is a ___ election.", size=20.5)
f.ex("A2", "Completare le frasi", "November 3", "Giorno delle elezioni: martedì 3 novembre",
     "Election Day is Tuesday, ___.", size=20.5)
f.ex("A2", "Completare le frasi", "early", "early voting = voto anticipato",
     "Voting before Election Day is called ___ voting.", size=20.5)
f.ex("B1", "Completare le frasi", "called", "race called = vincitore proclamato",
     "Some races are ___ on Tuesday night ; others take days.", size=20.5)
f.ex("B1", "Completare le frasi", "takes", "take time = richiedere tempo",
     "Counting ___ time in every state.", size=20.5)
f.end_report()

# ---- searches chart (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 668, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "SEARCHES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "OF THE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Cercato negli USA · Google Trends", 19, "sans", False, GREY)
gt = [
    ("election day", 250),
    ("nfl week 9", 218),
    ("cat in the hat", 186),
    ("daylight saving", 140),
    ("f1 sao paulo", 108),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE if i == 0 else GOLD)
    byy += 92
p.text(gx + 22, byy + 16, "Snapshots, late October :", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "search interest changes during the day.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "Popolarità relativa, non numeri esatti.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1280
p.rect(gx, sy, gw, 372, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "IN THIS ISSUE · Sommario", 24, "sans", True, OLIVE)
som = [
    ("p.2", "Clocks, candy & movies", "A2"),
    ("p.3", "A cat, a monster & screens", "A2→B1"),
    ("p.4", "Madrid, São Paulo & Miami", "B1"),
    ("p.5", "Election night at home", "B1"),
    ("p.6", "How America votes", "B2"),
    ("p.7", "Phrases of the week", "A2→B2"),
    ("p.8", "Exercises & answers", "all"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 72, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "THE WORD OF THE WEEK", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
p.para(gx, my + 76, "« midterm » : in the middle of a term. A midterm election falls two years after a presidential election.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, my + 168, "Midterm election = elezioni di medio termine.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "voting.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "A voting booth in the Old State House, Hartford, Connecticut : one voter, one ballot, one private moment. On Tuesday, millions of Americans will do the same.",
        "Kenneth C. Zirkel — CC0, via Wikimedia Commons")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-fall")
f2.head("FALL, THE SEASON OF VOTES", 25)
f2.para("Autumn in America is a season of votes and games : the ballots on Tuesday, the football in Madrid on Sunday, and two films on Friday. One week, three kinds of suspense.", 22.5)
f2.para("All week, our reporters follow the same rhythm : vote early, watch late, read slowly. See you on page 2 !", 22.5)
f2.end_report()
# col 3 IN BRIEF
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "IN BRIEF · In breve", 24, "sans", True, OLIVE)
brefs = [
    ("ELECTION", "Tuesday, November 3 : Election Day. All 435 House seats on the ballot. (p. 6)"),
    ("CLOCKS", "Sunday, November 1 : America fell back. Darker evenings. (p. 2)"),
    ("MOVIES", "Friday, November 6 : « The Cat in the Hat » and « Godzilla Minus Zero ». (p. 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "LIGHTNING QUIZ · Quiz lampo", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Leggi pagina 1, scegli la risposta giusta · Risposte a pagina 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "Scelta multipla", "B", "Giorno delle elezioni: martedì 3 novembre",
      "Election Day is... A. November 1 · B. Tuesday, November 3 · C. November 8", size=21)
qf.ex("A2", "Scelta multipla", "C", "Tutti i 435 seggi della Camera da rieleggere",
      "How many House seats are on the ballot ? A. 100 · B. 50 · C. 435", size=21)
qf.ex("A2", "Scelta multipla", "A", "Gli USA hanno spostato indietro le lancette il 1 novembre",
      "America turned its clocks back on... A. November 1 · B. November 3 · C. November 8", size=21)
qf.ex("A2", "Scelta multipla", "B", "Partita NFL a Madrid domenica 8 novembre",
      "The NFL game in Madrid is on... A. Friday · B. Sunday, November 8 · C. Tuesday", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LIFE · Vita", "The Lucerna", "LEVEL A2 · Clocks, candy & your week · Orologi, dolci e la tua settimana")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("One More Hour of Sleep : America Falls Back", 37)
f.byline("By The Lucerna newsroom · Reading level : A2")
f.para("On Sunday, November 1, at 2 a.m., the clocks in most of the United States went back one hour — to 1 a.m. again. The hour from 1 to 2 happened twice. Americans call it « falling back », and the prize is simple : one more hour of sleep.")
f.para("Why do we change the clocks ? In summer, we move the clocks forward so the evenings stay light longer. In autumn, we move them back, so the mornings are light again for school and work. The American memory phrase is : spring forward, fall back.")
f.para("Not every place changes. Arizona and Hawaii stay on the same time all year — no spring forward, no fall back. If you call a friend in Phoenix on Sunday, remember : their clock did not move.")
f.para("The price of the extra hour is a darker evening. From this week, the sun sets earlier, and the walk home from school or work is in the dark. Lights go on in windows, and autumn evenings begin.")
f.para("And what about Saturday night ? On Saturday, October 31, it was Halloween. Children in costumes went from house to house with the old call : « Trick or treat ! » In the morning, the pumpkins were still on the porches — and the candy bags were full.")
f.para("Halloween and the clock change belong together in America : one night of costumes, then one night of an extra hour. Two autumn rituals, one weekend — and both are now just passed, not coming.")
f.box("DO THE MATHS · Facciamo i conti", [
    ("From 2 a.m. back to 1 a.m. : the night of November 1 has 25 hours, not 24. One extra hour — one extra hour of sleep, if you use it well.", "serif", False, INK, 21.5, 1.4),
])
f.head("WHAT IS ON THIS WEEK ?", 25)
f.para("Second story of the week — and it is on your screen. On Friday, November 6, two films open in cinemas : « The Cat in the Hat », with the famous cat from Dr. Seuss, and « Godzilla Minus Zero », the new film from Takashi Yamazaki. One for children, one for monster fans — and both for a Friday night out.", 23.5)
f.para("On television and streaming, the week is just as full. New shows arrive on Wednesday, Thursday and Friday, and on Sunday night, a famous reality reunion closes the week. Page 3 has the full screen guide.", 23.5)
f.para("How do you say the new time ? « It is one o'clock — again ! » is the joke of the week. The clocks below show the three times of the week : the repeated hour, the half hour, and the quarter to.", 23.5)
f.gloss("to fall back = (orologio) spostare indietro · a costume = costume, travestimento · trick or treat = dolcetto o scherzetto.")
f.end_report()

# col 3: image + facts (sequential, measured)
ix = COLX[3]
image(p, "halloween1912.jpg", ix, 200, CW, 440)
cy3 = caption(p, ix, 640, CW, "« A Halloween Wish » : a Halloween postcard from 1912. More than a century ago, Americans already sent Halloween greetings — the costumes change, the night stays.",
              "Public domain, via Wikimedia Commons")
sav = ["Most of the United States fell back on Sunday, November 1 — Arizona and Hawaii did not change.",
       "The night of November 1 has 25 hours : the hour from 1 to 2 a.m. happens twice.",
       "Halloween was Saturday, October 31 : costumes, pumpkins, and full candy bags."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in sav) + 14
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DID YOU KNOW ?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "And you ? Did you sleep one hour more on Sunday ? What did you do on October 31 ? Write two sentences in English for VOL.3."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Domenica hai dormito un'ora in più? Scrivi due frasi in inglese alla redazione!", "sans", False, 20, CW - 44)) * 30 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "AND YOU ? · E tu ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Domenica hai dormito un'ora in più? Scrivi due frasi in inglese alla redazione!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Telling the time wide box ----
dy = 1570
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "TELLING THE TIME · Come si dice l'ora", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "The repeated hour · Le tre ore della settimana", 20, "sans", False, GREY, anchor="end")

def clock(cx, cy, r, hh, mm, label):
    p.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fdfaf0" stroke="{INK}" stroke-width="3"/>')
    import math
    for k in range(12):
        a = math.radians(k * 30)
        x1, y1 = cx + (r - 12) * math.sin(a), cy - (r - 12) * math.cos(a)
        x2, y2 = cx + r * math.sin(a), cy - r * math.cos(a)
        p.add(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{INK}" stroke-width="2.4"/>')
    ah = math.radians((hh % 12) * 30 + mm * 0.5)
    am = math.radians(mm * 6)
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.55)*math.sin(ah):.0f}" y2="{cy - (r*0.55)*math.cos(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.82)*math.sin(am):.0f}" y2="{cy - (r*0.82)*math.cos(am):.0f}" stroke="{BRICK}" stroke-width="4" stroke-linecap="round"/>')
    p.text(cx, cy + r + 34, label, 22, "serif", True, INK, anchor="middle")

clock(240, dy + 140, 74, 1, 0, "It is one o'clock.")
clock(560, dy + 140, 74, 1, 30, "It is half past one.")
clock(880, dy + 140, 74, 7, 45, "It is quarter to eight.")
lx = 1090
ly = dy + 66
for line in [
    ("twice", "= two times (due volte)"),
    ("again", "= one more time (ancora una volta)"),
    ("to fall back", "= to go back one hour (spostare indietro di un'ora)"),
    ("an extra hour", "= one hour more (un'ora in più)"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 240, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 40
p.para(lx, ly + 24, "This week : on Sunday, November 1, the clocks fell back. The hour from 1 to 2 a.m. happened twice — spring forward, fall back.", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 340
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCISES · Esercizi di pagina 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8 · Cerca per numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2562, tag="P2-ex")
e.head("A · WHAT TIME IS IT ?", 25)
e.bridge("Completa le frasi in inglese secondo l'ora.")
e.ex("A2", "Completare le frasi", "one", "1:00 = l'una",
     "1:00 — It is ___ o'clock.", instr="Completa", size=22)
e.ex("A2", "Completare le frasi", "half past", "1:30 = l'una e mezza",
     "1:30 — It is ___ one.", instr="Completa", size=22)
e.ex("A2", "Completare le frasi", "quarter to", "7:45 = le otto meno un quarto",
     "7:45 — It is ___ eight.", instr="Completa", size=22)
e.ex("A2", "Completare le frasi", "twice", "due volte = twice",
     "The hour happened ___ on Sunday.", instr="Completa", size=22)
e.ex("A2", "Completare le frasi", "extra", "extra = in più",
     "We got an ___ hour of sleep.", instr="Completa", size=22)
e.head("B · GOING TO", 25)
e.bridge("Riscrivi con be going to (piani e cose che accadranno).")
e.ex("A2", "Trasformazione", "Americans are going to vote on Tuesday.", "Americans (plurale) → are going to",
     "Americans (vote) on Tuesday. → ___", instr="Riscrivi")
e.ex("A2", "Trasformazione", "She is going to watch the film on Friday.", "she → is going to",
     "She (watch) the film on Friday. → ___", instr="Riscrivi")
e.ex("A2", "Trasformazione", "We are going to sleep one hour more.", "we → are going to",
     "We (sleep) one hour more. → ___", instr="Riscrivi")
e.ex("B1", "Trasformazione", "Are they going to fall back on Sunday ?", "Domanda: be va all'inizio",
     "They (fall) back on Sunday ? → ___", instr="Riscrivi")
e.head("C · COMPREHENSION", 25)
e.bridge("Leggi pagina 2, scegli la risposta giusta.")
e.ex("A2", "Scelta multipla", "B", "Il 1 novembre alle 2 di notte spostate indietro all'1",
     "The clocks went back at... A. 1 a.m. · B. 2 a.m. · C. 3 a.m.", size=22)
e.ex("A2", "Scelta multipla", "C", "Arizona e Hawaii non spostano le lancette",
     "Which places do NOT change ? A. Texas · B. Florida · C. Arizona and Hawaii", size=22)
e.ex("A2", "Scelta multipla", "A", "Halloween era sabato 31 ottobre",
     "Halloween was on... A. Saturday, October 31 · B. Sunday, November 1 · C. Friday, November 6", size=22)
e.ex("A2", "Scelta multipla", "B", "La notte del 1 novembre dura 25 ore",
     "The night of November 1 has... A. 24 hours · B. 25 hours · C. 23 hours", size=22)
e.head("D · THE WORDS", 25)
e.match_set("A2", "Abbinamento",
            ["a costume", "an extra hour", "to fall back", "trick or treat"],
            ["one hour more than usual",
             "clothes for a costume role",
             "the children's Halloween call",
             "to move clocks back one hour"],
            ["b", "a", "d", "c"],
            ["costume = costume b", "extra hour = un'ora in più a", "fall back = spostare indietro d", "trick or treat = dolcetto o scherzetto c"],
            instr="Abbina")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-life.svg")
print("P2 saved, exercises so far:", len(REG))
