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
p.text(MX, 92, "VOL. 4", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "WEEKLY IN ENGLISH　Todas as semanas　Do que se fala no mundo anglófono", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "WEEK OF NOVEMBER 16 TO 22, 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "The Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SEMANÁRIO EM INGLÊS　VOL.4　ELEIÇÕES　SELVA　CINEMA", 36, "serif", True, OLIVE, anchor="middle", spacing=6.9)
p.text(975, 372, "TEXTOS EM INGLÊS　EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# dark band: midterms
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "DEMOCRATS WIN BOTH HOUSES!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Tuesday, November 3: America voted. By Sunday, November 8, the count was clear.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "Voto de 3 de novembro　Os democratas vencem as duas casas", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "Eleições de meio mandato　Resultados anunciados　Ver página 6", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "THE BIG STORY　Manchete", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Democrats Win the House and the Senate", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "By The Lucerna newsroom　Reading level: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("On Tuesday, November 3, Americans voted in the midterm election — for all 435 seats in the House of Representatives, for 35 seats in the Senate, and for governor in 36 states. By Sunday, November 8, the count was clear enough to call: the Democrats won the House, and the Democrats won the Senate.")
f.para("The numbers, as called by the Associated Press on Sunday, November 8: in the House, 254 seats for the Democrats and 162 for the Republicans, with 19 races still uncalled. The majority is 218. In the Senate, the Democrats won 20 of the 33 races called, and the Republicans 13, with two races — in Alaska and Mississippi — still uncalled.")
f.para("Before the vote, the Republicans held the House, 218 seats to 214, and the Senate, 53 to 47. On election night, seven Senate seats changed hands — in Iowa, Kansas, Maine, North Carolina, Ohio, South Carolina and Texas — and all seven went to the Democrats. Five governors' offices changed hands too: Georgia, Iowa, Nevada, Ohio and Texas.")
f.para("A “call” is not the official result. News organisations call a race when the maths is clear. The official result comes later, when each state checks its count and certifies it — between November 10 and December 18. Until then, the numbers can still move a little. Page 6 explains how to read them.")
f.para("The new Congress meets in January 2027. Until then, the old Congress finishes its work — and the winners plan theirs. This week also brings the jungle back to television, a look back at last year's Ashes, and a new Hunger Games film to the cinema. Welcome back to VOL.4!")
f.bridge("Nota — a midterm = as eleições de meio mandato · to call a race = anunciar o resultado · a seat = um assento.", size=19.5)
f.box("THE WEEK IN NUMBERS　Números", [  # D5: tsize 23->21, +23.5px over
    ("Nov 3 — the vote (dia do voto) · 254–162 — the House, as called on Nov 8 (a Câmara)", "serif", False, INK, 20.5, 1.35),
    ("218 — the majority (a maioria) · 7 — Senate seats that changed hands (assentos do Senado que mudaram de lado)", "serif", False, INK, 20.5, 1.35),
], tsize=21)
f.head("TRY IT NOW　Pratique agora", 25)
f.ex("A2", "Completar frases", "midterm", "midterm = as eleições de meio mandato",
     "Americans voted in the ___ election on November 3.", size=20.5)
f.ex("A2", "Completar frases", "call", "call a race = anunciar o resultado da eleição",
     "News organisations ___ a race when the maths is clear.", size=20.5)
f.ex("A2", "Completar frases", "seats", "seat = um assento",
     "All 435 ___ in the House were on the ballot.", size=20.5)
f.ex("A2", "Completar frases", "majority", "majority = a maioria",
     "The ___ in the House is 218 seats.", size=20.5)
f.ex("B1", "Completar frases", "changed", "change hands = mudar de lado",
     "Seven Senate seats ___ hands on election night.", size=20.5)
f.ex("B1", "Completar frases", "January", "O novo Congresso se reunirá em janeiro de 2027",
     "The new Congress meets in ___ 2027.", size=20.5)
f.end_report()

# ---- searches chart (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 668, fill=BOX)
p.text(gx + 22, gy + 40, "SEARCHES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "OF THE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Pesquisas da semana　Google Trends", 19, "sans", False, GREY)
gt = [
    ("midterm results", 250),
    ("thanksgiving", 218),
    ("hunger games", 186),
    ("i'm a celebrity", 140),
    ("anti-bullying week", 108),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE)
    byy += 86  # fix1: was 92 — last footnote baseline sat at 1274, 18px
    # below the box bottom (1256); step 86 pulls the footnotes to
    # baselines 1184/1210/1244, last ink ~1247, inside the box.
p.text(gx + 22, byy + 16, "Snapshots, early November:", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "search interest changes during the day.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "Interesse relativo, não números exatos.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1280
p.rect(gx, sy, gw, 372, fill="#f0eee5")
p.text(gx + 22, sy + 40, "IN THIS ISSUE　Nesta edição", 24, "sans", True, OLIVE)
som = [
    ("p.2", "After the vote: what now?", "A2"),
    ("p.3", "Haymitch in the arena", "A2→B1"),
    ("p.4", "Perth, Turin & football", "B1"),
    ("p.5", "Break the silence", "B1"),
    ("p.6", "Reading the results", "B2"),
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
p.text(gx, my + 76, "“midterm”", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "an election in the middle of a president's four-year term.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "Eleições de meio mandato: toda a Câmara e um terço do Senado.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1862, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "capitol.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "The United States Capitol in Washington, D.C. — the home of Congress. The new Congress, with a Democratic House and a Democratic Senate, meets in January 2027.",
        "Noclip — public domain, via Wikimedia Commons")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-countries")
f2.head("TWO HOUSES, ONE MAP", 25)
f2.para("One country, two houses. The House of Representatives has 435 seats, and all of them were on the ballot. The Senate has 100 seats, and 35 were on the ballot. That is why the map changed in one night — and why it will take weeks to finish.", 22.5)
f2.para("Read page 6 for the full map — and the numbers behind it.", 22.5)
f2.end_report()
# col 3 IN BRIEF
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX)
p.text(bx + 22, 1914, "IN BRIEF　Em resumo", 24, "sans", True, OLIVE)
brefs = [
    ("ELECTION", "Nov 3: America voted. Democrats win both houses, as called on Nov 8. (p. 6)"),
    ("JUNGLE", "Mon, Nov 16, 9 p.m.: I'm a Celebrity returns to ITV1. (p. 3)"),
    ("ASHES", "A year ago: Australia beat England 4–1 in the 2025–26 Ashes. (p. 4)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "LIGHTNING QUIZ　Quiz-relâmpago", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Leia a capa e escolha a resposta certa　Respostas na página 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "Múltipla escolha", "B", "Os democratas venceram 254 assentos na Câmara (dados de 8 de novembro)",
      "The Democrats won the House with... A. 218 seats called · B. 254 seats called · C. 162 seats called", size=21)
qf.ex("A2", "Múltipla escolha", "A", "O dia do voto é terça-feira, 3 de novembro",
      "The midterm vote was on... A. Tuesday, November 3 · B. Sunday, November 8 · C. Monday, November 16", size=21)
qf.ex("A2", "Múltipla escolha", "C", "A maioria na Câmara é de 218 assentos",
      "A majority in the House is... A. 100 seats · B. 435 seats · C. 218 seats", size=21)
qf.ex("A2", "Múltipla escolha", "C", "O novo Congresso se reunirá em janeiro de 2027",
      "The new Congress meets in... A. November · B. December · C. January 2027", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LIFE　Vida", "The Lucerna", "LEVEL A2　After the vote　Depois do voto")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("The Week After the Vote: What Happens Now?", 32)
f.byline("By The Lucerna newsroom　Reading level: A2")
f.para("The vote is over. The counting is not. On Monday, November 9, the day this issue went to press, election workers in many states were still opening mail ballots and checking signatures. In Alaska and Mississippi, the Senate races were still too close to call.")
f.para("What happens next? First, the states certify their counts — between November 10 and December 18. Georgia law calls for a runoff on December 1 only if no candidate wins a majority — but Jon Ossoff won reelection with about 59% of the vote, so there is no runoff. Mississippi has no runoff: the most votes win. Then the winners are sworn in, and the new Congress meets in January 2027.")
f.para("In Washington, the parties choose their leaders. The Republicans in the House vote on Tuesday, November 10. The Democrats in the House vote on November 18 and 19. The Speaker — the leader of the House — is chosen when the new Congress meets in January. The Speaker, Mike Johnson, has said he will not run to lead the Republicans in the new Congress.")
f.head("TWO HOUSES, TWO JOBS", 25)
f.para("Why two houses? The House of Representatives has 435 seats, and every seat is on the ballot every two years. The Senate has 100 seats, and about a third of them are on the ballot each time. A senator serves for six years. A member of the House serves for two. That is why the House changes fast, and the Senate changes slowly.")
f.box("SENATE IN NUMBERS　O Senado", [
    ("100 — seats in the Senate. 35 — seats on the ballot on November 3. 6 — years in a senator's term.", "serif", False, INK, 21.5, 1.4),
])
f.para("Life goes on around the politics. Next week is Thanksgiving week in America. Thanksgiving Day is Thursday, November 26 — a day for family, for a big dinner, and for the turkey. Many families travel home, and the Friday after it, November 27, is Black Friday, the biggest shopping day of the year.")
f.para("And in Britain? The week is quieter — but the television is not. On Monday, November 16, at 9 p.m., the jungle opens again: I'm a Celebrity is back on ITV1. Page 3 has the story — and the words you need for the jungle.")
f.box("THE CALENDAR　Calendário", [
    ("10 nov. — os republicanos escolhem seu líder · 18–19 nov. — os democratas votam", "serif", False, INK, 21.5, 1.4),
    ("20 nov. — Dia Mundial da Criança · 26 nov. — Thanksgiving · 27 nov. — Black Friday", "serif", False, INK, 21.5, 1.4),
])
f.head("WHAT IS ON THIS WEEK?", 25)
f.para("Second story of the week — and it is on your screen. On Friday, November 20, the new Hunger Games film opens in cinemas, and the ATP Finals end in Turin on Sunday, November 22. On Saturday, November 21, the Premier League is back — and page 4 looks back at the Ashes. Page 3 has the film guide, page 4 the sport.", 23.5)
f.para("On television, the week is just as full. I'm a Celebrity opens on Monday night, and the jungle will be on every night for weeks. Thanksgiving is a week away — and the turkey is already in the shops.", 23.5)
f.para("How do you say the date of the new Congress? “In January 2027.” is the sentence of the week. The phrase box below shows three ways to say it.", 23.5)
f.gloss("to certify = certificar oficialmente · a runoff = um segundo turno.")
f.end_report()

# col 3: image + facts (sequential, measured)
ix = COLX[3]
image(p, "turkey.jpg", ix, 200, CW, 440)
cy3 = caption(p, ix, 640, CW, "A wild turkey, drawn by John James Audubon. The turkey is the bird of Thanksgiving — on Thursday, November 26, it is the centre of the American dinner table.",
              "John James Audubon — public domain, via Wikimedia Commons")
sav = ["The new Congress meets in January 2027 — two months after the vote.",
       "Thanksgiving is always the fourth Thursday of November.",
       "The House has 435 seats — and every one of them was on the ballot on November 3."]
sy3 = cy3 + 24
sh = 89 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in sav) + 14
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DID YOU KNOW?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "And you? What happens after an election in your country? Who counts the votes, and how long does it take? Write three sentences in English for VOL.5."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("No seu país, o que acontece depois das eleições? Escreva três frases em inglês para a redação.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "AND YOU?　E você?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "No seu país, o que acontece depois das eleições? Escreva três frases em inglês para a redação.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Say it wide box ----
dy = 1570
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "SAY IT: IN JANUARY 2027　Como dizer a data", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "The new Congress, in three sentences　O novo Congresso em três frases", 20, "sans", False, GREY, anchor="end")

def phrase_panel(cx, label, sub, w=280):
    p.rect(cx - w // 2, dy + 66, w, 132, fill="#f0eee5")
    p.text(cx, dy + 126, label, 20, "serif", True, INK, anchor="middle")
    p.text(cx, dy + 168, sub, 20, "sans", False, GREY, anchor="middle")

phrase_panel(299, "The counting continues.", "A apuração continua ainda.")
phrase_panel(750, "The new Congress meets in January.", "O novo Congresso se reunirá em janeiro.", w=380)
phrase_panel(1200, "Happy Thanksgiving!", "Feliz Dia de Ação de Graças!")
lx = 1370
ly = dy + 66
for line in [
    ("to certify", "= to confirm (confirmar oficialmente)"),
    ("a runoff", "= a second vote (um segundo turno)"),
    ("sworn in", "= to take the oath (prestar juramento)"),
    ("a turkey", "= the bird of Thanksgiving (o peru)"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 140, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 40
p.para(lx, ly + 24, "This week: on Monday, November 9, this issue went to press. The numbers in it are the calls of Sunday, November 8 — and the counting goes on.", 19, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 340
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCISES　Exercícios da página 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8　Os exercícios misturam níveis; procure pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P2-ex")
e.head("A　THE DATE", 25)
e.bridge("Complete as frases segundo a data e a hora.")
e.ex("A2", "Completar frases", "November", "O mês 11 = November",
     "The vote was on Tuesday, ___ 3.", instr="Complete", size=22)
e.ex("A2", "Completar frases", "January", "O novo Congresso se reunirá em janeiro de 2027",
     "The new Congress meets in ___ 2027.", instr="Complete", size=22)
e.ex("A2", "Completar frases", "1", "Segunda volta a 1 de dezembro",
     "A runoff, if needed, is on December ___.", instr="Complete", size=22)
e.ex("A2", "Completar frases", "Thursday", "O Dia de Ação de Graças é uma quinta-feira",
     "Thanksgiving is on ___, November 26.", instr="Complete", size=22)
e.ex("A2", "Completar frases", "27", "A Black Friday é em 27 de novembro",
     "Black Friday is on November ___.", instr="Complete", size=22)
e.head("B　WILL", 25)
e.bridge("Reescreva com will + verbo (promessas).")
e.ex("A2", "Transformação", "The new Congress will meet in January.", "meet → will meet",
     "The new Congress (meet) in January. → ___", instr="Reescreva")
e.ex("A2", "Transformação", "States will certify their counts.", "certify → will certify",
     "States (certify) their counts. → ___", instr="Reescreva")
e.ex("A2", "Transformação", "Families will travel home.", "travel → will travel",
     "Families (travel) home for Thanksgiving. → ___", instr="Reescreva")
e.ex("B1", "Transformação", "Will they watch the jungle on Monday?", "Pergunta: will vai para o início",
     "They (watch) the jungle on Monday? → ___", instr="Reescreva")
e.head("C　COMPREHENSION", 25)
e.bridge("Leia a página 2 e escolha.")
e.ex("A2", "Múltipla escolha", "B", "Os estados certificam de 10 de novembro a 18 de dezembro",
     "Certification runs... A. Nov 3–9 · B. Nov 10–Dec 18 · C. Jan–Feb", size=22)
e.ex("A2", "Múltipla escolha", "C", "O segundo turno será em 1º de dezembro",
     "A runoff, if needed, is on... A. November 10 · B. November 26 · C. December 1", size=22)
e.ex("A2", "Múltipla escolha", "A", "O Dia de Ação de Graças cai na quinta-feira, 26 de novembro",
     "Thanksgiving Day is... A. Thu, Nov 26 · B. Fri, Nov 27 · C. Mon, Nov 16", size=22)
e.ex("A2", "Múltipla escolha", "B", "O programa da selva estreia na segunda-feira, 16 de novembro, às 9 da noite",
     "I'm a Celebrity returns on... A. Sun, Nov 15 · B. Mon, Nov 16 · C. Fri, Nov 20", size=22)
e.head("D　THE WORDS", 25)
e.match_set("A2", "Emparelhamento",
            ["a runoff", "to certify", "a turkey", "Thanksgiving"],
            ["the bird of the Thanksgiving dinner",
             "a second vote, when nobody wins",
             "to confirm a count officially",
             "the American family holiday"],
            ["b", "c", "a", "d"],
            ["runoff = um segundo turno b", "certify = certificar oficialmente c", "turkey = um peru a", "Thanksgiving = o Dia de Ação de Graças d"],
            instr="Emparelhe")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-life.svg")
print("P2 saved, exercises so far:", len(REG))
