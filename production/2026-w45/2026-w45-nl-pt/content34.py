# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTUUR (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTUUR　Cultura", "De Lucerna", "NIVEAU A2 → B1　Museumnacht, boeken en kunst　Noite dos Museus, livros e arte")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Amsterdam blijft wakker: de Museumnacht", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2 → B1")
f.para("Zaterdagavond 7 november blijft Amsterdam wakker: het is Museumnacht, de 26e editie. Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts, met muziek, workshops en rondleidingen. Eén kaartje geeft toegang tot alle deelnemende musea.")
f.para("Let op: de Museumkaart geldt deze avond niet — je hebt een apart kaartje nodig. Populaire musea werken met tijdsloten: reserveer op tijd, anders sta je in de rij. Veel bezoekers gaan op de fiets van museum naar museum; er rijden ook extra nachtbussen.")
f.para("In Den Haag is het deze week Crossing Border Festival, van dinsdag tot en met zondag: schrijvers en muzikanten delen het podium. Literatuur en muziek horen bij elkaar, zeggen de organisatoren — een boek kan klinken als een lied, en een lied kan lezen als een verhaal.")
f.para("En de kunstbeurs PAN Amsterdam in de RAI loopt nog tot en met zondag 8 november: kunst, antiek en design uit alle eeuwen, van oud porselein tot nieuwe meubels.")
f.head("TWEEDEHANDS IS OOK CULTUUR", 25)
f.para("In Zaandam is op 7 en 8 november de Mega Snuffelmarkt, met zo'n 250 kramen vol tweedehands spullen: boeken, platen, kleding en speelgoed. Tweedehands kopen is ook klimaatvriendelijk: wat al bestaat, hoeft niet opnieuw gemaakt te worden.")
f.para("En wie na de markt nog energie heeft, fietst 's avonds naar Amsterdam: daar begint om 19:00 uur de Museumnacht.")
f.gloss("het museum = museu · de rondleiding = visita guiada · het tijdslot = horário marcado · tweedehands = em segunda mão · de beurs = feira, mercado.")
f.end_report()

# col 3: image + facts box (sequential, measured)
ix = COLX[3]
image(p, "gracht.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Een boot in een Amsterdamse gracht. Tijdens Museumnacht fietst en vaart de stad de hele nacht door.",
              "Foto: W. Punt / Anefo, Nationaal Archief — CC0")
facts = ["26e editie van Museumnacht, zaterdag 7 november, 19:00–02:00 uur.",
         "Meer dan 70 musea doen mee; de Museumkaart geldt niet.",
         "PAN Amsterdam in de RAI, tot en met zondag 8 november."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "MUSEUMNACHT IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　Exercícios da página 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8　Níveis misturados: procure pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Leia o artigo da página 3 e escolha a resposta certa.")
e.ex("A2", "choice", "B", "A Noite dos Museus é no sábado, 7 de novembro",
     "Museumnacht is op... A. vrijdag 6 november · B. zaterdag 7 november · C. zondag 8 november", size=20, gap=8)
e.ex("A2", "choice", "B", "Os museus ficam abertos até as 2h00",
     "De musea zijn open tot... A. 24:00 uur · B. 02:00 uur · C. 19:00 uur", size=20, gap=8)
e.ex("A2", "choice", "C", "O Crossing Border é em Haia",
     "Crossing Border is in... A. Amsterdam · B. Rotterdam · C. Den Haag", size=20, gap=8)
e.ex("A2", "choice", "A", "O Crossing Border combina livros e música",
     "Crossing Border combineert... A. boeken en muziek · B. voetbal en dans · C. film en eten", size=20, gap=8)
e.ex("A2", "choice", "B", "A feira de arte PAN vai até 8 de novembro",
     "PAN Amsterdam loopt tot en met... A. zaterdag 7 november · B. zondag 8 november · C. maandag 9 november", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("Complete com as palavras do quadro. Nota: algumas palavras têm de ir para o plural.")
e.para("museum · rondleiding · tijdslot · tweedehands · beurs", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "complete", "musea", "plural de museum: musea",
     "Op Museumnacht zijn meer dan 70 ___ open.", instr="Complete", size=20, gap=8)
e.ex("A2", "complete", "rondleiding", "rondleiding = visita guiada",
     "Een ___ laat je de mooiste zalen zien.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "tijdslot", "tijdslot = horário marcado",
     "Reserveer een ___ voor populaire musea.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "tweedehands", "tweedehands = em segunda mão",
     "Op de Snuffelmarkt koop je ___ spullen.", instr="Complete", size=20, gap=8)
e.ex("A2", "complete", "beurs", "beurs = feira, mercado",
     "PAN is een ___ voor kunst en antiek.", instr="Complete", size=20, gap=8)
e.head("C　HET PERFECTUM", 25)
e.bridge("Complete com o pretérito perfeito. Atenção aos verbos auxiliares hebben/zijn.")
e.ex("B1", "complete", "zijn geweest", "perfectum de zijn: zijn geweest",
     "De musea ___ (zijn) tot 02:00 uur open.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "hebben gekocht", "perfectum de kopen: hebben gekocht",
     "Wij ___ (kopen) één kaartje voor alle musea.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "hebben voorgelezen", "perfectum de voorlezen: hebben voorgelezen",
     "De schrijvers ___ (voorlezen) hun werk op het podium.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "zijn gekomen", "komen leva zijn: zijn gekomen",
     "Veel bezoekers ___ (komen) met de fiets.", instr="Complete", size=20, gap=8)
e.head("D　REKENEN", 25)
e.bridge("Calcule: responda com os números da página 3.")
e.ex("B1", "complete", "7", "De 19h00 às 2h00 são 7 horas",
     "Museumnacht duurt van 19:00 tot 02:00 uur: ___ uur.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "8", "De 1 a 8 de novembro são 8 dias",
     "PAN Amsterdam loopt van 1 tot en met 8 november: ___ dagen.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "6", "De 3 a 8 de novembro são 6 dias",
     "Crossing Border duurt van dinsdag 3 tot en met zondag 8 november: ___ dagen.", instr="Complete", size=20, gap=8)
e.ex("B2", "complete", "125", "A metade de 250 é 125",
     "De Snuffelmarkt heeft zo'n 250 kramen; de helft is ___.", instr="Complete", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultuur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　Esporte", "De Lucerna", "NIVEAU B1　Europese week en speelronde 12　Semana europeia e 12.ª rodada")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P4-feature")
f.title("Europa: drie keer feest, twee keer verlies", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("De Europese week is voorbij — en de balans is drie keer feest, twee keer verlies. Ajax won donderdag 22 oktober met 2–0 van Atalanta in de Conference League. Twente won met 4–1 bij Lincoln Red Imps in Gibraltar. AZ won met 4–0 van Ararat-Armenia. NEC verloor: 2–4 bij Dinamo Zagreb.")
f.para("En woensdag 21 oktober verloor Feyenoord in de Champions League: Real Betis won met 1–0 in Sevilla, door een doelpunt van Isco in de 59e minuut. Feyenoord had wel meer balbezit, maar schoot te weinig op doel.")
f.para("In de Eredivisie was het zondag 25 oktober ook spannend: PSV en Feyenoord speelden 1–1 gelijk. Ajax won met 2–1 bij Sparta. En Twente won met 2–0 bij AZ. Na 10 ronden staat Feyenoord bovenaan met 24 punten, Ajax heeft 21, en PSV, Twente en AZ hebben elk 20 punten.")
f.para("Nu speelronde 12. Vrijdagavond: Willem II tegen PEC Zwolle (19:00 uur). Zaterdag: Fortuna tegen Telstar (15:30), ADO tegen Sparta (17:45) en Excelsior tegen Go Ahead Eagles (20:00). Zondag de topper: Heerenveen tegen Feyenoord (11:15) en Twente tegen Ajax (13:30), plus Cambuur tegen PSV, AZ tegen Groningen (15:45) en Utrecht tegen NEC (19:00).")
f.head("DE STAND NA 10 RONDEN", 25)
f.para("Feyenoord 24 punten, Ajax 21, PSV 20, Twente 20, AZ 20. Onderaan staan ADO en Telstar met 6 punten en Willem II met 2 punten. Maar er zijn nog 24 ronden te gaan: alles kan nog veranderen.")
f.gloss("de balans = o balanço final · gelijkspelen = empatar · de speelronde = rodada · de topper = o grande jogo · de stand = a classificação.")
f.end_report()

# col 3: image + programme box (sequential, measured)
ix = COLX[3]
image(p, "elftal1912.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Het Nederlands elftal in 1912. Voetbal is al meer dan honderd jaar de sport van Nederland.",
              "Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein")
facts = ["Donderdag 22 oktober: Ajax – Atalanta 2–0; Twente – Lincoln 4–1; AZ – Ararat 4–0; Dinamo – NEC 4–2.",
         "Woensdag 21 oktober: Real Betis – Feyenoord 1–0.",
         "Zondag 25 oktober: PSV – Feyenoord 1–1; Sparta – Ajax 1–2; AZ – Twente 0–2.",
         "Speelronde 12: vrijdag Willem II – PEC; zondag Heerenveen – Feyenoord (11:15) en Twente – Ajax (13:30)."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "HET PROGRAMMA", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P4 col3 ends", sy3 + sh)

# ---- P4 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　Exercícios da página 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8　Níveis misturados: procure pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Leia o artigo da página 4 e escolha a resposta certa.")
e.ex("B1", "choice", "B", "O Ajax venceu o Atalanta por 2–0",
     "Ajax won donderdag met... A. 1–0 · B. 2–0 · C. 4–1", size=20, gap=8)
e.ex("B1", "choice", "C", "O Twente venceu o Lincoln por 4–1",
     "Twente won bij Lincoln met... A. 2–0 · B. 4–0 · C. 4–1", size=20, gap=8)
e.ex("B1", "choice", "A", "O NEC perdeu por 2–4 para o Dínamo Zagreb",
     "NEC verloor met... A. 2–4 · B. 4–2 · C. 1–0", size=20, gap=8)
e.ex("B1", "choice", "B", "O Real Betis venceu o Feyenoord por 1–0",
     "Real Betis – Feyenoord eindigde... A. 0–0 · B. 1–0 · C. 0–1", size=20, gap=8)
e.ex("B1", "choice", "B", "Após 10 rodadas, o Feyenoord lidera com 24 pontos",
     "Na 10 ronden staat Feyenoord... A. tweede · B. eerste met 24 punten · C. derde", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("Complete com as palavras do quadro. Atenção às formas verbais.")
e.para("balans · gelijkspelen · topper · stand · doelpunt", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "complete", "balans", "balans = o balanço final",
     "De ___ van de Europese week is: drie keer feest, twee keer verlies.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "speelden gelijk", "pretérito plural de gelijkspelen: speelden gelijk",
     "PSV en Feyenoord ___ (gelijkspelen): 1–1.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "topper", "topper = o grande jogo",
     "Heerenveen – Feyenoord is de ___ van zondag.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "stand", "stand = a classificação",
     "Op de ___ staat Feyenoord bovenaan.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "doelpunt", "doelpunt = gol",
     "Isco maakte het enige ___ van Betis – Feyenoord.", instr="Complete", size=20, gap=8)
e.head("C　VERLEDEN TIJD", 25)
e.bridge("Complete com o pretérito ou o pretérito perfeito.")
e.ex("B1", "complete", "won", "pretérito de winnen: won",
     "Ajax ___ (winnen) donderdag met 2–0.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "ging", "pretérito de gaan: ging",
     "De bal ___ (gaan) in het doel: 1–0 voor Betis.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "verloor", "pretérito de verliezen: verloor",
     "Feyenoord ___ (verliezen) met 1–0 in Sevilla.", instr="Complete", size=20, gap=8)
e.ex("B2", "complete", "zijn gekomen", "perfectum de komen leva zijn",
     "Veel supporters ___ (komen) naar het stadion.", instr="Complete", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "true or false", "Waar", "Verdadeiro: o Ajax venceu por 2–0",
     "Ajax won donderdag met 2–0 van Atalanta. Waar of niet waar?", instr="Verdadeiro ou falso?", size=20, gap=8)
e.ex("B1", "true or false", "Niet waar", "Falso: o NEC perdeu por 2–4",
     "NEC won met 4–2 bij Dinamo Zagreb. Waar of niet waar?", instr="Verdadeiro ou falso?", size=20, gap=8)
e.ex("B1", "true or false", "Niet waar", "Falso: Twente–Ajax é às 13h30; 11h15 é Heerenveen–Feyenoord",
     "Twente – Ajax is zondag om 11:15 uur. Waar of niet waar?", instr="Verdadeiro ou falso?", size=20, gap=8)
e.ex("B1", "true or false", "Waar", "Verdadeiro: após 10 rodadas, o Feyenoord lidera com 24 pontos",
     "Feyenoord staat na 10 ronden bovenaan met 24 punten. Waar of niet waar?", instr="Verdadeiro ou falso?", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
