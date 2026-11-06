# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-en-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · FRONT PAGE (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3", 23, "sans", True, OLIVE)
p.text(975, 92, "WEEKLY IN ENGLISH · Todas as semanas · Do que se fala no mundo anglófono", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "WEEK OF NOVEMBER 9 TO 15, 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "The Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 338, "SEMANÁRIO EM INGLÊS · VOL.3 · COMEMORAÇÃO · FUTEBOL · CINEMA", 46, "serif", True, INK, anchor="middle")
p.text(975, 372, "TEXTOS EM INGLÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 19.5, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# dark band: eleven eleven
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "ELEVEN ELEVEN — AND TWO MINUTES OF SILENCE !", 38, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Wednesday, November 11, at 11 a.m., Britain, Canada, Australia and America stop for two minutes.", 23.5, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "11 de novembro, 11h · Dois minutos de silêncio", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "Veterans Day · Remembrance Day · Ver página 2", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "THE BIG STORY · Manchete", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Eleven Eleven : The Two Minutes When the English-Speaking World Stops", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "By The Lucerna newsroom · Reading level : A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("On Wednesday, November 11, at eleven o'clock in the morning, something quiet happens across the English-speaking world. In London, Ottawa, Canberra and Washington, people stop what they are doing, and for two minutes they stand still and say nothing. It is the two-minute silence — for the soldiers who died in war, and for all who served.")
f.para("The date is not an accident. At 11 a.m. on November 11, 1918, the guns of the First World War fell silent. The armistice — the agreement to stop fighting — began at the eleventh hour of the eleventh day of the eleventh month. In Britain it is Remembrance Day ; in the United States, Veterans Day, for all who served.")
f.para("The symbol is the poppy, a small red flower. Poppies grew on the battlefields of Flanders, where so many soldiers died. People wear a paper poppy in November, to help veterans and their families. In London, the King leads the National Act of Remembrance at the Cenotaph in Whitehall — the monument to the dead with no grave of their own.")
f.para("This week is full of other dates too. On Friday, November 13, the BBC's Children in Need appeal fills British television, and a new Scrooge comes to the cinema. On Sunday, November 15, American football comes to Munich, tennis opens its season finale in Turin, and England play Spain in Madrid.")
f.para("And one promise from last issue : the midterm election results. This issue went to press on November 2, before the November 3 vote — so it prints no results, and invents none. Page 6 explains why counting takes time. Welcome back to VOL.3 !")
f.bridge("an armistice, o armistício · a veteran, um veterano · to fall silent, ficar em silêncio.", size=19.5)
f.box("THE WEEK IN NUMBERS · Números", [
    ("11 nov, 11:00 — the silence (o silêncio) · 1918 — the armistice (o armistício)", "serif", False, INK, 20.5, 1.35),
    ("13 nov (sex.) — Children in Need + Ebenezer · 15 nov (dom.) — NFL Munique + ATP Finals", "serif", False, INK, 20.5, 1.35),
])
f.head("TRY IT NOW · Pratique agora", 25)
f.ex("A2", "Completar frases", "armistice", "armistice = o armistício",
     "The fighting stopped with an ___ in 1918.", size=20.5)
f.ex("A2", "Completar frases", "veteran", "veteran = o veterano",
     "A ___ is a person who served in the armed forces.", size=20.5)
f.ex("A2", "Completar frases", "November 11", "Dia da memória, 11 de novembro (quarta-feira)",
     "The silence is on Wednesday, ___.", size=20.5)
f.ex("A2", "Completar frases", "poppy", "poppy = a papoula",
     "People wear a red ___ in November.", size=20.5)
f.ex("B1", "Completar frases", "silent", "fall silent = ficar em silêncio",
     "At 11 a.m., the guns fell ___.", size=20.5)
f.ex("B1", "Completar frases", "two", "two minutes = dois minutos",
     "The silence lasts ___ minutes.", size=20.5)
f.end_report()

# ---- searches chart (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 668, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "SEARCHES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "OF THE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Pesquisas da semana · Google Trends", 19, "sans", False, GREY)
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
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE if i == 0 else GOLD)
    byy += 92
p.text(gx + 22, byy + 16, "Snapshots, early November :", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "search interest changes during the day.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "Interesse relativo, não números exatos.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1280
p.rect(gx, sy, gw, 372, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "IN THIS ISSUE · Nesta edição", 24, "sans", True, OLIVE)
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
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 72, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "THE WORD OF THE WEEK", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
p.para(gx, my + 76, "« remembrance » : the act of remembering those who died in war.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, my + 168, "Memória. Remembrance Day = dia da memória.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "poppyfield.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "A field of poppies, painted by Claude Monet. The poppy is the flower of remembrance : it grew on the battlefields of Flanders, and it is worn every November.",
        "Claude Monet — public domain, via Wikimedia Commons")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-countries")
f2.head("FOUR COUNTRIES, ONE MINUTE", 25)
f2.para("One silence, four names. In the United States it is Veterans Day. In Britain it is Remembrance Day. In Canada and Australia, the name is the same too — with the same poppy and the same 11 a.m. silence.", 22.5)
f2.para("Remember on Wednesday, laugh on Friday, watch sport on Sunday. See you on page 2 !", 22.5)
f2.end_report()
# col 3 IN BRIEF
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "IN BRIEF · Em resumo", 24, "sans", True, OLIVE)
brefs = [
    ("ELECTION", "Nov 3 : Americans voted. Press time Nov 2 : no results, none invented. (p. 6)"),
    ("SILENCE", "Wed, Nov 11, 11 a.m. : two minutes of silence in Britain, Canada, Australia, US. (p. 2)"),
    ("MUNICH", "Sunday, November 15 : Patriots–Lions, Allianz Arena, Munich, 3:30 p.m. (p. 4)"),
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
qf.ex("A2", "Múltipla escolha", "B", "O silêncio, quarta-feira 11 de novembro",
      "The two-minute silence is on... A. November 13 · B. Wednesday, November 11 · C. November 15", size=21)
qf.ex("A2", "Múltipla escolha", "C", "O armistício, em 1918",
      "The armistice began in... A. 1914 · B. 1939 · C. 1918", size=21)
qf.ex("A2", "Múltipla escolha", "A", "As pessoas usam uma papoula vermelha",
      "People wear... A. a red poppy · B. a white hat · C. a blue ribbon", size=21)
qf.ex("A2", "Múltipla escolha", "B", "O jogo da NFL em Munique, domingo 15 de novembro",
      "The NFL game in Munich is on... A. Friday · B. Sunday, November 15 · C. Tuesday", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LIFE · Vida", "The Lucerna", "LEVEL A2 · Silence, poppies & your week · O silêncio, as papoulas e a tua semana")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Wednesday, November 11 : Two Minutes That Stop a Country", 37)
f.byline("By The Lucerna newsroom · Reading level : A2")
f.para("On Wednesday, November 11, at 11 a.m., Britain stops. Buses stop. Shops go quiet. In schools, children stand still. For two minutes, nobody speaks. The silence remembers the soldiers who died in the First World War — and in every war since.")
f.para("Why eleven eleven ? The First World War ended at 11 a.m. on November 11, 1918. The armistice was signed that morning, and the guns stopped. In 1920, Britain built the Cenotaph in Whitehall, London — a stone monument with no body inside it, for all the dead. Every year since, people have gathered there.")
f.para("In Canada, Australia and New Zealand, the day is the same : Remembrance Day, the same poppy, the same silence at 11 a.m. In the United States, November 11 is Veterans Day — a day for all veterans, living and dead. The names are different. The silence is the same.")
f.para("The poppy is small, red and paper. Volunteers sell it on streets and in shops, and the money helps veterans and their families. Many people wear it on the left, near the heart — and they wear it all through November, until the day itself is past.")
f.para("And what about the weekend just gone ? On Sunday, November 8, it was Remembrance Sunday in Britain — the main ceremony, three days before Armistice Day itself. And in India and in Indian homes around the world, Sunday, November 8, was Diwali, the festival of lights : a five-day festival of lamps, sweets and family, with the main night on Sunday. Two festivals of light and memory, one weekend — both just passed, not coming.")
f.para("This week looks forward too. On Wednesday, November 11, shoppers mark Singles' Day — 11.11, the biggest online shopping day in China, now copied around the world. On Friday, November 13, Britain's Children in Need appeal takes over television. Page 5 has the story of Pudsey the bear.")
f.box("ELEVEN ELEVEN · Onze e onze", [
    ("11 a.m. on the 11th day of the 11th month : the eleventh hour. Two minutes of silence — 120 seconds. Tradition says the first minute is for the dead, the second for the living who came home.", "serif", False, INK, 21.5, 1.4),
])
f.head("WHAT IS ON THIS WEEK ?", 25)
f.para("Second story of the week — and it is on your screen. On Friday, November 13, two films open : « Ebenezer », a dark new Scrooge from Dickens, and « How to Rob a Bank », a heist comedy. One ghost story, one bank story — and both for a Friday night out.", 23.5)
f.para("On television, the week is just as full. The Children in Need appeal show is live on Friday night, and the ATP Finals begin in Turin on Sunday. Page 3 has the film guide, page 4 the sport.", 23.5)
f.para("How do you say the time of the silence ? « At eleven o'clock — eleven eleven. » is the sentence of the week. The phrase box below shows three ways to say it.", 23.5)
f.gloss("a silence, o silêncio · an armistice, o armistício · a poppy, a papoula · a veteran, um veterano.")
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
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DID YOU KNOW ?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "And you ? Do you wear a poppy in November ? What does your country do on November 11 ? Write two sentences in English for VOL.4."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Escreve em inglês: o que faz o teu país a 11 de novembro?", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "AND YOU ? · E você?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Escreve em inglês: o que faz o teu país a 11 de novembro?", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Say it wide box ----
dy = 1570
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "SAY IT : ELEVEN ELEVEN · Dizer as horas", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "The silence, in three sentences · O silêncio em três frases", 20, "sans", False, GREY, anchor="end")

def phrase_panel(cx, label, sub):
    p.rect(cx - 140, dy + 66, 280, 132, fill="#fdfaf0", stroke=LINE, sw=1.4)
    p.text(cx, dy + 126, label, 20, "serif", True, INK, anchor="middle")
    p.text(cx, dy + 168, sub, 20, "sans", False, GREY, anchor="middle")

phrase_panel(240, "At eleven o'clock.", "As 11 da manhã.")
phrase_panel(560, "Two minutes of silence.", "Dois minutos de silêncio.")
phrase_panel(880, "We will remember them.", "Lembrar-nos-emos deles.")
lx = 1090
ly = dy + 66
for line in [
    ("remember", "= to keep in your mind (lembrar)"),
    ("silent", "= saying nothing (ficar em silêncio)"),
    ("to honour", "= to show respect (mostrar respeito)"),
    ("a ceremony", "= a formal event (uma cerimónia)"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 240, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 40
p.para(lx, ly + 24, "This week : on Wednesday, November 11, at 11 a.m., the silence begins. Two minutes — for the dead, and for all who served.", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 340
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EXERCISES · Exercícios da página 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8 · Os exercícios misturam níveis; procure pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2562, tag="P2-ex")
e.head("A · THE DATE", 25)
e.bridge("Complete as frases segundo a data e a hora.")
e.ex("A2", "Completar frases", "eleven", "As 11 = eleven o'clock",
     "The silence begins at ___ o'clock.", instr="Complete", size=22)
e.ex("A2", "Completar frases", "November", "O mês 11 = November",
     "Remembrance Day is on 11 ___.", instr="Complete", size=22)
e.ex("A2", "Completar frases", "two", "dois minutos = two minutes",
     "The silence lasts ___ minutes.", instr="Complete", size=22)
e.ex("A2", "Completar frases", "poppy", "poppy = a papoula",
     "People wear a red ___ in November.", instr="Complete", size=22)
e.ex("A2", "Completar frases", "1918", "O ano do armistício: 1918",
     "The armistice began in ___.", instr="Complete", size=22)
e.head("B · WILL", 25)
e.bridge("Reescreva com will + verbo (promessas).")
e.ex("A2", "Transformação", "They will remember them.", "they → will remember",
     "They (remember) them. → ___", instr="Reescreva")
e.ex("A2", "Transformação", "She will wear a poppy.", "she → will wear",
     "She (wear) a poppy. → ___", instr="Reescreva")
e.ex("A2", "Transformação", "We will stand still.", "we → will stand",
     "We (stand) still. → ___", instr="Reescreva")
e.ex("B1", "Transformação", "Will they watch the ceremony ?", "Pergunta: will vai para o início",
     "They (watch) the ceremony ? → ___", instr="Reescreva")
e.head("C · COMPREHENSION", 25)
e.bridge("Leia a página 2 e escolha.")
e.ex("A2", "Múltipla escolha", "B", "O silêncio começa às 11 da manhã",
     "The silence begins at... A. 10 a.m. · B. 11 a.m. · C. noon", size=22)
e.ex("A2", "Múltipla escolha", "C", "O monumento foi inaugurado em 1920",
     "The Cenotaph was unveiled in... A. 1918 · B. 1919 · C. 1920", size=22)
e.ex("A2", "Múltipla escolha", "A", "A noite principal do Diwali foi domingo, 8 de novembro",
     "Diwali's main night was... A. Sun, Nov 8 · B. Wed, Nov 11 · C. Fri, Nov 13", size=22)
e.ex("A2", "Múltipla escolha", "B", "Nos Estados Unidos chama-se Veterans Day",
     "In the US, November 11 is... A. Remembrance Day · B. Veterans Day · C. Singles' Day", size=22)
e.head("D · THE WORDS", 25)
e.match_set("A2", "Emparelhamento",
            ["a poppy", "an armistice", "a veteran", "a ceremony"],
            ["a red flower worn in November",
             "an agreement to stop fighting",
             "a person who served in the forces",
             "a formal public event"],
            ["a", "b", "c", "d"],
            ["poppy = a papoula a", "armistice = o armistício b", "veteran = o veterano c", "ceremony = a cerimónia d"],
            instr="Emparelhe")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-life.svg")
print("P2 saved, exercises so far:", len(REG))
