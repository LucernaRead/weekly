# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-en-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · FRONT PAGE (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2", 23, "sans", True, OLIVE)
p.text(975, 92, "WEEKLY IN ENGLISH · UM NÚMERO POR SEMANA · O INGLÊS QUE A AMÉRICA LÊ", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "WEEK OF NOVEMBER 2 TO 8, 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "The Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 338, "SEMANÁRIO EM INGLÊS · VOL.2 · VOTOS · FUTEBOL · CINEMA", 46, "serif", True, INK, anchor="middle")
p.text(975, 372, "TEXTOS EM INGLÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 19.5, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# dark band: election + clocks
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "AMERICA VOTES ON TUESDAY — AND THE CLOCKS FELL BACK !", 38, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Election Day is Tuesday, November 3. On Sunday, November 1, America turned its clocks back one hour.", 23.5, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "Terça de eleições · Relógios atrasados", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "Dia de eleições, terça-feira, 3 de novembro · Página 6", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "THE BIG STORY · Manchete", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "America Votes : Election Day Comes on Tuesday, November 3", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "By The Lucerna newsroom · Reading level : A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Tuesday, November 3, is Election Day in the United States. It is a midterm election — an election in the middle of a president's four-year term. All 435 seats in the House of Representatives are on the ballot, along with about a third of the Senate and governorships in many states.")
f.para("In many states, voting has already started. Early voting lets people vote before Election Day : you go to a voting place, you show your ID, you mark your ballot, and your vote counts on election night. On Tuesday, the voting places open early in the morning and close in the evening.")
f.para("What happens on Tuesday night ? Television channels show maps that slowly change colour, state by state. But nobody should expect every result at midnight : each state runs its own election, and counting takes time. Some races are called on Tuesday night ; others take days.")
f.para("And that is only half of the week. On Friday, November 6, two big films open in cinemas. On Sunday, November 8, American football goes to Madrid, Spain, and Formula 1 races in São Paulo, Brazil. Our sport dossier is on page 4.")
f.para("This is the second issue of The Lucerna in English. Last issue promised real readers' letters — and this week, our Readers' Corner on page 7 tells you honestly where those letters stand. Welcome back !")
f.bridge("a midterm, eleição de meio de mandato · a ballot, cédula · a race, uma disputa · to call a race, anunciar o resultado de uma disputa.")
f.box("THE WEEK IN NUMBERS · Números", [
    ("Nov 3 — Election Day (dia das eleições) · 435 — seats in the House, all on the ballot (todos em disputa)", "serif", False, INK, 20.5, 1.35),
    ("Nov 6 — two films open (dois filmes estreiam) · Nov 8 — NFL in Madrid + F1 in São Paulo (dois eventos no domingo)", "serif", False, INK, 20.5, 1.35),
])
f.head("TRY IT NOW · Pratique agora", 25)
f.ex("A2", "Completar frases", "ballot", "ballot = cédula",
     "You mark your choice on a ___ and put it in the box.", size=20.5)
f.ex("A2", "Completar frases", "midterm", "midterm = de meio de mandato",
     "An election in the middle of a term is a ___ election.", size=20.5)
f.ex("A2", "Completar frases", "November 3", "dia das eleições, terça-feira, 3 de novembro",
     "Election Day is Tuesday, ___.", size=20.5)
f.ex("A2", "Completar frases", "early", "early voting = votação antecipada",
     "Voting before Election Day is called ___ voting.", size=20.5)
f.ex("B1", "Completar frases", "called", "race called = resultado anunciado",
     "Some races are ___ on Tuesday night ; others take days.", size=20.5)
f.ex("B1", "Completar frases", "takes", "take time = levar tempo",
     "Counting ___ time in every state.", size=20.5)
f.end_report()

# ---- searches chart (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 668, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "SEARCHES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "OF THE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "As mais buscadas · Google Trends EUA", 19, "sans", False, GREY)
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
p.text(gx + 22, byy + 76, "Interesse relativo, não números exatos.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1280
p.rect(gx, sy, gw, 372, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "IN THIS ISSUE · Nesta edição", 24, "sans", True, OLIVE)
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
p.para(gx, my + 168, "A meio do mandato: midterm election.", 19, "sans", False, GREY, gw, 1.35)

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
p.text(bx + 22, 1914, "IN BRIEF · Em resumo", 24, "sans", True, OLIVE)
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
p.text(MX, qy + 36, "LIGHTNING QUIZ · Quiz-relâmpago", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Leia a capa e escolha a resposta certa · Respostas na página 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "Múltipla escolha", "B", "dia das eleições, terça-feira, 3 de novembro",
      "Election Day is... A. November 1 · B. Tuesday, November 3 · C. November 8", size=21)
qf.ex("A2", "Múltipla escolha", "C", "todos os 435 assentos da Câmara em disputa",
      "How many House seats are on the ballot ? A. 100 · B. 50 · C. 435", size=21)
qf.ex("A2", "Múltipla escolha", "A", "os EUA atrasaram os relógios em 1º de novembro",
      "America turned its clocks back on... A. November 1 · B. November 3 · C. November 8", size=21)
qf.ex("A2", "Múltipla escolha", "B", "o jogo da NFL em Madri, domingo, 8 de novembro",
      "The NFL game in Madrid is on... A. Friday · B. Sunday, November 8 · C. Tuesday", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LIFE · Vida", "The Lucerna", "LEVEL A2 · Clocks, candy & your week · Relógios, doces e a sua semana")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("One More Hour of Sleep : America Falls Back", 37)
f.byline("By The Lucerna newsroom · Reading level : A2")
f.para("On Sunday, November 1, at 2 a.m., the clocks in most of the United States went back one hour — to 1 a.m. again. The hour from 1 to 2 happened twice. Americans call it « falling back », and the prize is simple : one more hour of sleep.")
f.para("Why do we change the clocks ? In summer, we move the clocks forward so the evenings stay light longer. In autumn, we move them back, so the mornings are light again for school and work. The American memory phrase is : spring forward, fall back.")
f.para("Not every place changes. Arizona and Hawaii stay on the same time all year — no spring forward, no fall back. If you call a friend in Phoenix on Sunday, remember : their clock did not move.")
f.para("The price of the extra hour is a darker evening. From this week, the sun sets earlier, and the walk home from school or work is in the dark. Lights go on in windows, and autumn evenings begin.")
f.para("And what about Saturday night ? On Saturday, October 31, it was Halloween. Children in costumes went from house to house with the old call : « Trick or treat ! » In the morning, the pumpkins were still on the porches — and the candy bags were full.")
f.para("Halloween and the clock change belong together in America : one night of costumes, then one night of an extra hour. Two autumn rituals, one weekend — and both are now just passed, not coming.")
f.box("DO THE MATHS · Faça as contas", [
    ("From 2 a.m. back to 1 a.m. : the night of November 1 has 25 hours, not 24. One extra hour — one extra hour of sleep, if you use it well.", "serif", False, INK, 21.5, 1.4),
])
f.head("WHAT IS ON THIS WEEK ?", 25)
f.para("Second story of the week — and it is on your screen. On Friday, November 6, two films open in cinemas : « The Cat in the Hat », with the famous cat from Dr. Seuss, and « Godzilla Minus Zero », the new film from Takashi Yamazaki. One for children, one for monster fans — and both for a Friday night out.", 23.5)
f.para("On television and streaming, the week is just as full. New shows arrive on Wednesday, Thursday and Friday, and on Sunday night, a famous reality reunion closes the week. Page 3 has the full screen guide.", 23.5)
f.para("How do you say the new time ? « It is one o'clock — again ! » is the joke of the week. The clocks below show the three times of the week : the repeated hour, the half hour, and the quarter to.", 23.5)
f.gloss("to fall back (relógio), atrasar · a costume, uma fantasia · trick or treat, doces ou travessuras.")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Dormiu uma hora a mais no domingo? Envie duas frases em inglês à redação.", "sans", False, 20, CW - 44)) * 29 + 24
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "AND YOU ? · E você?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Dormiu uma hora a mais no domingo? Envie duas frases em inglês à redação.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Telling the time wide box ----
dy = 1570
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "TELLING THE TIME · Como dizer as horas", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "The repeated hour · As três horas da semana", 20, "sans", False, GREY, anchor="end")

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
    ("twice", "= two times (duas vezes)"),
    ("again", "= one more time (mais uma vez)"),
    ("to fall back", "= to go back one hour (atrasar)"),
    ("an extra hour", "= one hour more (uma hora a mais)"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 240, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 40
p.para(lx, ly + 24, "This week : on Sunday, November 1, the clocks fell back. The hour from 1 to 2 a.m. happened twice — spring forward, fall back.", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 340
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCISES · Exercícios da página 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8 · Os exercícios misturam níveis; procure pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2562, tag="P2-ex")
e.head("A · WHAT TIME IS IT ?", 25)
e.bridge("Complete em inglês conforme o horário.")
e.ex("A2", "Completar frases", "one", "1:00 = uma hora em ponto",
     "1:00 — It is ___ o'clock.", instr="Complete", size=22)
e.ex("A2", "Completar frases", "half past", "1:30 = uma e meia",
     "1:30 — It is ___ one.", instr="Complete", size=22)
e.ex("A2", "Completar frases", "quarter to", "7:45 = quinze para as oito",
     "7:45 — It is ___ eight.", instr="Complete", size=22)
e.ex("A2", "Completar frases", "twice", "duas vezes = twice",
     "The hour happened ___ on Sunday.", instr="Complete", size=22)
e.ex("A2", "Completar frases", "extra", "a mais = extra",
     "We got an ___ hour of sleep.", instr="Complete", size=22)
e.head("B · GOING TO", 25)
e.bridge("Reescreva com be going to + verbo (planos e coisas que vão acontecer).")
e.ex("A2", "Reescrever", "Americans are going to vote on Tuesday.", "Americans, plural → are going to",
     "Americans (vote) on Tuesday. → ___", instr="Reescreva")
e.ex("A2", "Reescrever", "She is going to watch the film on Friday.", "she → is going to",
     "She (watch) the film on Friday. → ___", instr="Reescreva")
e.ex("A2", "Reescrever", "We are going to sleep one hour more.", "we → are going to",
     "We (sleep) one hour more. → ___", instr="Reescreva")
e.ex("B1", "Reescrever", "Are they going to fall back on Sunday ?", "pergunta: be no início",
     "They (fall) back on Sunday ? → ___", instr="Reescreva")
e.head("C · COMPREHENSION", 25)
e.bridge("Leia o artigo da página 2 e responda.")
e.ex("A2", "Múltipla escolha", "B", "em 1º de novembro, das 2h para 1h",
     "The clocks went back at... A. 1 a.m. · B. 2 a.m. · C. 3 a.m.", size=22)
e.ex("A2", "Múltipla escolha", "C", "Arizona e Havaí não mudam a hora",
     "Which places do NOT change ? A. Texas · B. Florida · C. Arizona and Hawaii", size=22)
e.ex("A2", "Múltipla escolha", "A", "Halloween, sábado, 31 de outubro",
     "Halloween was on... A. Saturday, October 31 · B. Sunday, November 1 · C. Friday, November 6", size=22)
e.ex("A2", "Múltipla escolha", "B", "a noite de 1º de novembro tem 25 horas",
     "The night of November 1 has... A. 24 hours · B. 25 hours · C. 23 hours", size=22)
e.head("D · THE WORDS", 25)
e.match_set("A2", "Combinar",
            ["a costume", "an extra hour", "to fall back", "trick or treat"],
            ["one hour more than usual",
             "clothes for a costume role",
             "the children's Halloween call",
             "to move clocks back one hour"],
            ["b", "a", "d", "c"],
            ["costume=uma fantasia b", "extra hour=uma hora a mais a", "fall back=atrasar d", "trick or treat=doces ou travessuras c"],
            instr="Combine")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-life.svg")
print("P2 saved, exercises so far:", len(REG))
