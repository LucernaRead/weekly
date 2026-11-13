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
p.text(MX, 92, "VOL. 1　FIRST ISSUE", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "WEEKLY IN ENGLISH　UNA EDICIÓN CADA SEMANA　EL INGLÉS QUE LEE AMÉRICA", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "WEEK OF OCTOBER 19 TO 25, 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "The Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SEMANARIO EN INGLÉS　VOL.1　ESTADIOS　VOTOS　CALABAZAS", 36, "serif", True, OLIVE, anchor="middle", spacing=9.5)
p.text(975, 372, "TEXTOS EN INGLÉS　EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# clock-contrast band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "EUROPE TURNS ITS CLOCKS BACK SUNDAY — AMERICA WAITS !", 42, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Daylight saving ends one week later in the United States : on Sunday, November 1. Do not change your clock this week !", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "CAMBIA LA HORA", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "EE. UU., EL 1 DE NOVIEMBRE (P. 7)", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "THE BIG STORY　El titular", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "First Votes, First Games : America's Biggest Week of the Autumn", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "By The Lucerna newsroom　Reading level : A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Election Day is Tuesday, November 3. But in much of America, the election has already started. This Monday, October 19, early voting opened in Texas — and in Alaska, Arkansas, Connecticut and Colorado too. Millions of people are asking the same questions : where do I vote, and when ?")
f.para("Early voting is simple : you go to a voting place before Election Day, you show your ID, you mark your ballot, and your vote counts on election night. No November lines, no problem if you work on Tuesdays. In Texas, it runs from October 19 to October 30.")
f.para("And that is only half of the week. On Tuesday night, the new NBA season tips off. On Friday night, the World Series begins in Milwaukee. On Sunday, the fastest cars in the world race in Austin, Texas.")
f.para("One thing is sure : this year, baseball will have a champion for the very first time. The Milwaukee Brewers and the Tampa Bay Rays have never won the World Series. One of them will win it now. Our sport dossier is on page 4.")
f.para("This is the first issue of The Lucerna in English. Every week, we read America's real life with you — slowly, clearly, and always from the week's real news. Welcome !")
f.expl("Nota — early voting, votación anticipada · ballot, papeleta · tip-off, salto inicial.")
f.box("THE WEEK IN NUMBERS　En cifras", [
    ("Nov 3 — Election Day (día electoral) · Oct 19 — early voting opens in Texas (primer día)", "serif", False, INK, 20.5, 1.35),
    ("43 — NBA games from Tuesday to Sunday (martes a domingo) · 2 — teams in the World Series, both after a first title (su primer título)", "serif", False, INK, 20.5, 1.35),
], tsize=21)
f.head("TRY IT NOW　Practica al momento", 24)
f.ex("A2", "Completar frases", "ballot", "ballot = la papeleta",
     "You mark your choice on a ___ and put it in the box.", size=20.5)
f.ex("A2", "Completar frases", "early", "early voting = la votación anticipada",
     "Voting before Election Day is called ___ voting.", size=20.5)
f.ex("A2", "Completar frases", "November 3", "Election Day = el martes 3 de noviembre",
     "Election Day is Tuesday, ___.", size=20.5)
f.ex("A2", "Completar frases", "champion", "champion = el campeón",
     "The winner of the World Series is the ___ of baseball.", size=20.5)
f.ex("B1", "Completar frases", "opened", "empezó el lunes: usa el pasado opened",
     "Early voting ___ in Texas on Monday, October 19.", size=20.5)
f.ex("B1", "Completar frases", "first", "first title = el primer título",
     "One team will now win the World Series for the ___ time.", size=20.5)
f.end_report()

# ---- searches chart (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 668, fill=BOX)
p.text(gx + 22, gy + 40, "SEARCHES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "OF THE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Tendencias en EE. UU.　Google Trends", 19, "sans", False, GREY)
gt = [
    ("early voting", 250),
    ("world series schedule", 218),
    ("hot dog recall", 186),
    ("lakers roster", 140),
    ("barca vs real madrid", 108),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE)
    byy += 92
p.text(gx + 22, byy + 16, "Snapshots, Mon–Wed Oct 19–21 :", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "search interest changes during the day.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "“hot dog recall”, lunes: 200K+ (pág. 2)", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1280
p.rect(gx, sy, gw, 372, fill="#f0eee5")
p.text(gx + 22, sy + 40, "IN THIS ISSUE　En esta edición", 24, "sans", True, OLIVE)
som = [
    ("p.2", "Checks, fridges & clocks", "A2"),
    ("p.3", "Halloween in America", "A2→B1"),
    ("p.4", "The biggest sports week", "B1"),
    ("p.5", "Screens, streams & AI", "B1"),
    ("p.6", "The midterm deep read", "B2"),
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
p.text(gx, my + 76, "« fall back »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "when clocks go back one hour in autumn. Spring forward, fall back.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "El reloj se atrasa: fall back.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "ws1912.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Boston fans at the Polo Grounds, New York, on October 8, 1912 : Game 1 of the World Series. The Fall Classic was already America's autumn ritual 114 years ago.",
        "Bain News Service, Library of Congress — public domain")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-fall")
f2.head("FALL, THE SEASON OF FIRSTS", 25)
f2.para("Autumn in America is a season of firsts : the first votes, the first games, the first cold evenings. There is a first champion coming in baseball, and a first issue of this paper in your hands.", 22.5)
f2.para("All week, our reporters follow the same rhythm : vote early, play hard, read slowly. See you on page 2 !", 22.5)
f2.end_report()
# col 3 IN BRIEF
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX)
p.text(bx + 22, 1914, "IN BRIEF　Breves", 24, "sans", True, OLIVE)
brefs = [
    ("WORLD SERIES", "Game 1 is Friday night in Milwaukee. Neither team has ever won it. (page 4)"),
    ("CLOCKS", "Europe changes its clocks on Sunday. America waits until November 1. (page 7)"),
    ("HALLOWEEN", "Saturday, October 31 : costumes, candy — and maybe a Game 7. (page 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "LIGHTNING QUIZ　Quiz relámpago", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lee la portada y elige bien　Respuestas en la página 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "Opción múltiple", "B", "la votación anticipada en Texas empezó el lunes 19 de octubre",
      "Early voting in Texas starts on... A. November 3 · B. Monday, October 19 · C. November 1", size=21)
qf.ex("A2", "Opción múltiple", "C", "EE. UU. atrasa el reloj el 1 de noviembre",
      "America turns its clocks back on... A. October 25 · B. October 31 · C. November 1", size=21)
qf.ex("A2", "Opción múltiple", "A", "el Juego 1 de la Serie Mundial es en Milwaukee",
      "Game 1 of the World Series is in... A. Milwaukee · B. Tampa · C. Los Angeles", size=21)
qf.ex("A2", "Opción múltiple", "B", "la nueva temporada de la NBA empezó el martes 20 de octubre",
      "The new NBA season starts on... A. Friday · B. Tuesday · C. Sunday", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LIFE　Vida", "The Lucerna", "LEVEL A2　Money, checks & your fridge　Dinero, cheques y tu nevera")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Social Security Checks Grow by 3.6% in January", 32)
f.byline("By The Lucerna newsroom　Reading level : A2")
f.para("Good news for nearly 72 million Americans : on Wednesday, October 14, the Social Security Administration announced a cost-of-living adjustment — a « COLA » — of 3.6% for 2027. From January, the average retired worker will get about 75 dollars more every month.")
f.para("Why do the checks grow ? Because life costs more. When the prices of food, homes and energy go up, the checks go up too — that is the idea of the cost-of-living adjustment. Workers on SSI, a second program for people with very low incomes, see their increase a little earlier : on December 31, 2026. About 7.3 million people receive SSI.")
f.para("When will you see your number ? Personal notices come online at the end of November, and by mail in December. Every household does the same maths this week : 3.6% of my check is... how much, exactly ?")
f.para("How is the number chosen ? Government statisticians follow the prices of a basket of everyday things — food, homes, energy, transport. When the basket costs more, the COLA rises. It is a promise written into the system : your check follows the cost of life.")
f.para("Will 3.6% make anyone rich ? No. But for many households, 75 dollars is the difference between a hard month and an easier one — a full fridge, a warm house. That is why one small percentage is the week's biggest kitchen-table story.")
f.para("The system is old. The first monthly check went to Ida May Fuller, of Vermont, on January 31, 1940. It was 22.54 dollars. In three years of work, Miss Fuller had paid 24.75 dollars into the system. She lived to be 100 years old, and in her long retirement she received more than 22,000 dollars in checks.")
f.box("DO THE MATHS　A calcular", [
    ("3.6% of $1,000 is $36. Of $2,000, it is $72. The average increase — about $75 — tells you the average check is a little over $2,000 a month.", "serif", False, INK, 21.5, 1.4),
])
f.head("CHECK YOUR FRIDGE !", 25)
f.para("Second story of the week — and it is in your kitchen. On Saturday, October 17, the US Department of Agriculture announced a big recall : about 1.58 million pounds of hot dogs, bacon and deli meats from one company, Kayem Foods. A cooler in the factory did not work correctly, and the food was not cold enough.", 23.5)
f.para("What must you do ? Do not eat the food. Throw it away, or take it back to the shop. At the time of the announcement, no illnesses were reported — but the rule with a recall is simple : when in doubt, throw it out.", 23.5)
f.para("How do you read a recall notice ? Look for three things : the name of the food, the dates on the packet, and the lot number — a code printed near the date. If your packet matches, it goes in the bin, not on the table. A recall sounds frightening, but it is also good news : it means the safety system works.", 23.5)
f.gloss("cost-of-living, el costo de vida · a check, un cheque (el pago mensual) · a notice, un aviso · a pound, una libra (unos 0,45 kg) · to recall, retirar un producto.")
f.end_report()

# col 3: image + facts (sequential, measured)
ix = COLX[3]
image(p, "sscard.jpg", ix, 200, CW, 440)
cy3 = caption(p, ix, 640, CW, "A Social Security card from 1943 : the program began in 1935, and the first monthly check — 22.54 dollars — was paid in 1940.",
              "Social Security Administration — public domain")
sav = ["Nearly 72 million people receive Social Security money every month.",
       "The first check, in 1940, was 22.54 dollars. The average increase in 2027 is about 75 dollars a month.",
       "Notices arrive online in late November and by mail in December. Check your number !"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in sav) + 34
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DID YOU KNOW ?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "And you ? Is there a hot dog in your fridge today ? What money comes into your house every month ? Write two sentences in English and send them to the newsroom : the best ones will be printed in VOL.2 (page 7, « Readers' Corner »)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("¿Hay perritos calientes en tu nevera? ¿Qué dinero entra en tu casa?", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "AND YOU ?　¿Y tú?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "¿Hay perritos calientes en tu nevera? ¿Qué dinero entra en tu casa?", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Telling the time wide box ----
dy = 1570
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "TELLING THE TIME　Así se dice la hora", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Game times this week　Para todos los partidos de la semana", 20, "sans", False, GREY, anchor="end")

def clock(cx, cy, r, hh, mm, label):
    p.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fbfaf6" stroke="{INK}" stroke-width="3"/>')
    import math
    for k in range(12):
        a = math.radians(k * 30)
        x1, y1 = cx + (r - 12) * math.sin(a), cy - (r - 12) * math.cos(a)
        x2, y2 = cx + r * math.sin(a), cy - r * math.cos(a)
        p.add(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{INK}" stroke-width="2.4"/>')
    ah = math.radians((hh % 12) * 30 + mm * 0.5)
    am = math.radians(mm * 6)
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.55)*math.sin(ah):.0f}" y2="{cy - (r*0.55)*math.cos(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.82)*math.sin(am):.0f}" y2="{cy - (r*0.82)*math.cos(am):.0f}" stroke="{OLIVE}" stroke-width="4" stroke-linecap="round"/>')
    p.text(cx, cy + r + 34, label, 22, "serif", True, INK, anchor="middle")

clock(240, dy + 140, 74, 8, 0, "It is eight o'clock.")
clock(560, dy + 140, 74, 2, 30, "It is half past two.")
clock(880, dy + 140, 74, 7, 45, "It is quarter to eight.")
lx = 1090
ly = dy + 66
for line in [
    ("half past", "= 30 minutes after the hour (y media)"),
    ("quarter past", "= 15 minutes after (y cuarto)"),
    ("quarter to", "= 15 minutes before (menos cuarto)"),
    ("noon / midnight", "= 12:00 day / night (mediodía / medianoche)"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 240, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 40
p.para(lx, ly + 24, "This week : Game 1 of the World Series starts at 8 p.m. on Friday. In Europe, the clocks fall back on Sunday — in America, on Sunday, November 1 : spring forward, fall back.", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 340
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCISES　Ejercicios de la página 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8　Niveles mezclados: busca por número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P2-ex")
e.head("A　WHAT TIME IS IT ?", 25)
e.expl("Según la hora, completa las frases en inglés.")
e.ex("A2", "Completar frases", "half past", "8:30 = las ocho y media",
     "8:30 — It is ___ eight.", instr="Completa", size=22)
e.ex("A2", "Completar frases", "quarter past", "9:15 = las nueve y cuarto",
     "9:15 — It is ___ nine.", instr="Completa", size=22)
e.ex("A2", "Completar frases", "quarter to", "7:45 = las ocho menos cuarto",
     "7:45 — It is ___ eight.", instr="Completa", size=22)
e.ex("A2", "Completar frases", "midnight", "0:00 = medianoche",
     "0:00 — It is ___ . The city sleeps.", instr="Completa", size=22)
e.ex("A2", "Completar frases", "o'clock", "3:00 = las tres en punto",
     "3:00 — It is three ___ . The game starts !", instr="Completa", size=22)
e.head("B　GOING TO", 25)
e.expl("Reescribe con be going to + verbo (planes y cosas que van a pasar).")
e.ex("A2", "Transformación", "Checks are going to grow in January.", "checks es plural → are going to",
     "Checks (grow) in January. → ___", instr="Reescribe")
e.ex("A2", "Transformación", "Milwaukee is going to play Game 1 on Friday.", "Milwaukee es singular → is going to",
     "Milwaukee (play) Game 1 on Friday. → ___", instr="Reescribe")
e.ex("A2", "Transformación", "We are going to check the fridge tonight.", "we → are going to",
     "We (check) the fridge tonight. → ___", instr="Reescribe")
e.ex("B1", "Transformación", "Are you going to vote early this year ?", "pregunta: el verbo be va primero",
     "You (vote) early this year ? → ___", instr="Reescribe")
e.head("C　COMPREHENSION", 25)
e.expl("Lee los artículos de la página 2 y elige la respuesta correcta.")
e.ex("A2", "Opción múltiple", "B", "el COLA sube 3.6% (dato oficial de la SSA)",
     "In 2027, checks grow by... A. 1.6% · B. 3.6% · C. 6.3%", size=22)
e.ex("A2", "Opción múltiple", "B", "los avisos llegan a fines de noviembre y por correo en diciembre",
     "COLA notices arrive... A. in October · B. in late Nov. and Dec. · C. next summer", size=22)
e.ex("A2", "Opción múltiple", "C", "la causa de la retirada: falló un refrigerador",
     "The hot dogs were recalled because... A. they were old · B. the price was wrong · C. a cooler failed", size=22)
e.ex("A2", "Opción múltiple", "A", "el primer cheque mensual: 22.54 dólares (1940)",
     "The first check, in 1940, was... A. $22.54 · B. $75 · C. $225.40", size=22)
e.head("D　THE WORDS", 25)
e.match_set("A2", "Emparejar",
            ["a benefit", "a recall", "a pound", "the cost of living"],
            ["the price of everyday life",
             "money the government pays regularly",
             "about 0.45 kilos — 16 ounces",
             "the company takes its food back"],
            ["b", "d", "c", "a"],
            ["benefit = el dinero que paga el gobierno b", "recall = la empresa retira la comida d", "pound = unos 0,45 kg c", "cost of living = los precios de cada día a"],
            instr="Empareja")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-life.svg")
print("P2 saved, exercises so far:", len(REG))
