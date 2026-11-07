# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-nl-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · VOORPAGINA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3", 23, "sans", True, OLIVE)
p.text(975, 92, "ELKE WEEK IN HET NEDERLANDS · O NEERLANDÊS QUE OS NEERLANDESES LEEM", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "WEEK VAN 9 TOT EN MET 15 NOVEMBER 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "De Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "WEEKBLAD IN HET NEDERLANDS · VOL.3 · SINTERKLAAS · SINT-MAARTEN · ORANJE", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "TEXTOS EM NEERLANDÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 19.5, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "SINTERKLAAS KOMT ERAAN!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Eerst het Sinterklaasjournaal, dan de intocht in Grave en in Amsterdam.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "O SINTERKLAAS ESTÁ A CHEGAR", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "Esta semana: o Sinterklaas chega aos Países Baixos · ver página 3", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "HET NIEUWS · MANCHETE", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Sinterklaas komt eraan: eerst Grave, dan Amsterdam", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Van de redactie van De Lucerna · Leesniveau: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Op maandag 9 november begint het Sinterklaasjournaal op televisie. Elke dag om 18:00 uur volgen kinderen op NPO Zapp hoe Sinterklaas en zijn Pieten zich voorbereiden op de reis naar Nederland.")
f.para("Op zaterdag 14 november komt Sinterklaas officieel aan in Nederland. De landelijke intocht is dit jaar in Grave, een vestingstad aan de Maas in Noord-Brabant. Rond 12:00 uur meert de stoomboot aan bij de Maaskade. De intocht is live te zien op NPO 3.")
f.para("Een dag later, op zondag 15 november, is de intocht in Amsterdam: de 88e editie. De boot vertrekt om 10:15 uur bij De Omval en vaart over de Amstel naar het Scheepvaartmuseum. Daar krijgt Sinterklaas de sleutel van de stad. Daarna gaat hij te paard door de stad naar het Leidseplein.")
f.para("Eerder in de week, op woensdag 11 november, is het Sint-Maarten: kinderen gaan met lampionnen zingend langs de deuren (pagina 2). En op vrijdag 13 november speelt Oranje thuis tegen Griekenland (pagina 4).")
f.para("Na de intocht zetten kinderen hun schoen. Sinterklaas komt dan 's nachts met cadeautjes. Pakjesavond is dit jaar op zaterdag 5 december.")
f.bridge("Nota — de intocht = a chegada · de stoomboot = o barco a vapor · de lampion = a lanterna.")
f.box("DE WEEK IN CIJFERS · NÚMEROS", [
    ("9 — november: het Sinterklaasjournaal begint (9 nov.: notícias do Sinterklaas)", "serif", False, INK, 20, 1.35),
    ("14 — november: de landelijke intocht in Grave (14 nov.: chegada nacional, Grave)", "serif", False, INK, 20, 1.35),
    ("15 — november: de intocht in Amsterdam, de 88e editie (15 nov.: 88.ª edição)", "serif", False, INK, 20, 1.35),
    ("20:45 — uur: Oranje tegen Griekenland op vrijdag (sex. 20:45)", "serif", False, INK, 20, 1.35),
])
f.head("NU JIJ · A TUA VEZ", 25)
f.ex("A2", "complete", "9", "As notícias do Sinterklaas começam a 9 de novembro",
     "Het Sinterklaasjournaal begint op maandag ___ november.", size=19.5, gap=6)
f.ex("A2", "complete", "Grave", "A chegada nacional é em Grave",
     "De landelijke intocht is dit jaar in ___.", size=19.5, gap=6)
f.ex("A2", "complete", "15", "A chegada a Amesterdão é no domingo, 15 de novembro",
     "De intocht in Amsterdam is op zondag ___ november.", size=19.5, gap=6)
f.ex("A2", "complete", "11", "O São Martinho é na quarta-feira, 11 de novembro",
     "Sint-Maarten is op woensdag ___ november.", size=19.5, gap=6)
f.ex("A2", "complete", "20:45", "Países Baixos–Grécia, pontapé inicial às 20:45",
     "Oranje tegen Griekenland begint vrijdag om ___ uur.", size=19.5, gap=6)
f.ex("B1", "complete", "zetten", "Plural → zetten.",
     "Na de intocht ___ (zetten) kinderen hun schoen.", size=19.5, gap=6)
f.end_report()

# ---- deze week agenda (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "DEZE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "· ESTA SEMANA", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Agenda van de week · ACONTECIMENTOS", 19, "sans", False, GREY)
gt = [
    ("MA 9", "Sinterklaasjournaal begint"),
    ("WO 11", "Sint-Maarten, lampionnen"),
    ("VR 13", "Oranje – Griekenland"),
    ("ZA 14", "Intocht in Grave"),
    ("ZO 15", "Intocht Amsterdam"),
]
byy = gy + 150
for i, (lab, vol) in enumerate(gt):
    p.text(gx + 22, byy + 22, lab, 20, "serif", True, BRICK)
    p.text(gx + 110, byy + 22, vol, 20, "serif", False, INK)
    byy += 62
p.text(gx + 22, byy + 16, "Alle data en tijden staan ook", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "in de artikelen op pagina 2–4.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "Todas as datas e horas, páginas 2–4.", 19, "sans", False, GREY)

# ---- inhoud (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "IN DEZE EDITIE · NESTE NÚMERO", 24, "sans", True, OLIVE)
som = [
    ("Pag. 2", "Sint-Maarten: licht en delen", "A2"),
    ("Pag. 3", "Sinterklaasjournaal", "A2→B1"),
    ("Pag. 4", "Oranje: beslissende week", "B1"),
    ("Pag. 5", "Robinson en de schoen", "B1"),
    ("Pag. 6", "Sint-Maarten of Halloween?", "B2"),
    ("Pag. 7", "Woorden van de week", "A2→B2"),
    ("Pag. 8", "Oefeningen en antwoorden", "alle"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- woord van de week (col 3) ----
my = 1652
p.text(gx, my + 24, "HET WOORD VAN DE WEEK", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "«de intocht»: de feestelijke aankomst van Sinterklaas in een stad, met de boot en daarna te paard.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "«A intocht»: o Sinterklaas chega a uma cidade de barco e depois a cavalo, em desfile festivo.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1853, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "westertoren.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "De Westertoren in Amsterdam. Zondag 15 november vaart Sinterklaas over de Amstel naar het Scheepvaartmuseum en rijdt hij daarna te paard naar het Leidseplein. (Pagina 3)",
        "Foto: Wim van Rossem / Anefo, Nationaal Archief — CC0")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-extra")
f2.head("NA DE INTOCHT: DE SCHOEN", 25)
f2.para("Na de intocht mag de schoen: kinderen zetten 's avonds hun schoen bij de deur, met een wortel voor het paard en een tekening voor Sinterklaas. 's Nachts komt Sinterklaas met een cadeautje.", 22.5)
f2.para("Pakjesavond, de avond met de grote cadeaus, is dit jaar op zaterdag 5 december.", 22.5)
f2.end_report()
# col 3 IN HET KORT
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "IN HET KORT · EM RESUMO", 24, "sans", True, OLIVE)
brefs = [
    ("SINTERKLAAS · P.3", "Maandag Sinterklaasjournaal; zaterdag intocht in Grave."),
    ("SINT-MAARTEN · P.2", "Woensdag: kinderen met lampionnen langs de deuren."),
    ("ORANJE · P.4", "Vrijdag: Nederland – Griekenland, 20:45 uur, Amsterdam."),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz bliksem ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "BLIKSEMQUIZ · QUIZ RELÂMPAGO", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lê a página 1, escolhe a resposta certa · respostas na página 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "choice", "B", "As notícias do Sinterklaas começam na segunda-feira, 9 de novembro",
      "Het Sinterklaasjournaal begint op... A. zaterdag 14 november · B. maandag 9 november · C. zondag 15 november", size=21)
qf.ex("A2", "choice", "B", "A chegada nacional é em Grave",
      "De landelijke intocht is in... A. Amsterdam · B. Grave · C. Utrecht", size=21)
qf.ex("A2", "choice", "C", "A chegada a Amesterdão é a 88.ª edição",
      "De intocht in Amsterdam is de... A. 26e editie · B. 30e editie · C. 88e editie", size=21)
qf.ex("A2", "choice", "B", "Países Baixos–Grécia, pontapé inicial na sexta-feira às 20:45",
      "Oranje – Griekenland begint om... A. 18:00 uur · B. 20:45 uur · C. 12:00 uur", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-voorpagina.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LEVEN (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LEVEN · VIDA", "De Lucerna", "NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · São Martinho: lanternas e canções")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Sint-Maarten: lichtjes in het donker", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: A2")
f.para("Op woensdag 11 november is het Sint-Maarten. Als het donker wordt, gaan kinderen met een lampion langs de deuren. Ze zingen een liedje en krijgen snoep of fruit. Het bekendste liedje begint zo: «Elf november is de dag, dat mijn lichtje branden mag.»")
f.para("Het feest gaat over Sint-Maarten, of Martinus. Volgens de legende sneed hij zijn mantel in tweeën en gaf hij de helft aan een bedelaar in de kou. Daarom is Sint-Maarten het feest van het delen: licht delen, eten delen, aandacht delen.")
f.para("Sint-Maarten wordt niet overal in Nederland even uitbundig gevierd. Sterke gebieden zijn het noorden, de stad Utrecht, Noord-Holland boven het IJ, Noord-Brabant en Limburg. In Utrecht, de stad van Sint-Maarten, staat de viering op de lijst van het immaterieel erfgoed. Daar lopen kinderen 's avonds «lichies lope»: met lampionnen zingend langs de deuren.")
f.para("Wil je meedoen? Maak zelf een lampion van papier en versier hem met vliegerpapier, zodat het licht er mooi doorheen schijnt. Gebruik een ledlampje op batterijen, nooit een kaarsje. En zing een liedje bij elke deur — dan is het feest compleet.")
f.para("Sint-Maarten valt dit jaar midden in de Sinterklaastijd: maandag begon het Sinterklaasjournaal en zaterdag komt Sinterklaas aan in Grave. Twee feesten van licht en geven, in één week.")
f.head("DRIE DINGEN VOOR 11 NOVEMBER", 25)
f.para("Eén: maak een lampion, met een ledlampje erin. Twee: leer een liedje, bijvoorbeeld «Elf november is de dag». Drie: ga zingend langs de deuren — en deel wat je krijgt.")
f.box("ZO ONTHOUD JE HET · LEMBRA-TE", [
    ("«Sint-Maarten is het feest van het delen: licht, eten en aandacht.» En de lampion gaat aan als het donker wordt.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("de lampion = a lanterna · delen = partilhar · de mantel = o manto · de bedelaar = o mendigo · het erfgoed = o património · het ledlampje = a luzinha LED.")
f.end_report()

# col 3: image + facts + en jij (sequential, measured)
ix = COLX[3]
image(p, "kinderdijk.jpg", ix, 200, CW, 272)
cy3 = caption(p, ix, 472, CW, "Molens bij Kinderdijk. In november wordt het vroeg donker — dan schijnen de lampionnen van Sint-Maarten extra fel.",
              "Foto: Nationaal Archief — CC0")
facts = ["Sint-Maarten: woensdag 11 november, 's avonds met lampionnen langs de deuren.",
         "De legende: Martinus sneed zijn mantel in tweeën voor een bedelaar.",
         "Utrecht is de stad van Sint-Maarten; de viering staat op de erfgoedlijst."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 40
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WIST JE DAT?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Loop jij op 11 november met een lampion langs de deuren, of kijk je liever naar het Sinterklaasjournaal? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie: de mooiste komen in VOL.4 (pagina 7, «Brieven van lezers»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("A 11 de novembro, vais cantar de porta em porta com uma lanterna ou preferes ver as notícias do Sinterklaas? Escreve duas frases em neerlandês e envia-as à redação.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ? · E TU?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "A 11 de novembro, vais cantar de porta em porta com uma lanterna ou preferes ver as notícias do Sinterklaas? Escreve duas frases em neerlandês e envia-as à redação.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- lichtjes row: 4 boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "SINT-MAARTEN IN VIER WOORDEN · QUATRO PALAVRAS-CHAVE", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Wat hoort bij het feest? · Que palavras pertencem à festa?", 20, "sans", False, GREY, anchor="end")
codes = [
    ("LAMPION", "het lichtje", "uma lanterna de papel, com uma luz LED dentro"),
    ("LIEDJE", "het zingen", "cantar as canções de São Martinho de porta em porta"),
    ("DELEN", "het geven", "partilhar: dar metade do manto a um mendigo"),
    ("UTRECHT", "de stad", "a cidade de São Martinho, património"),
]
for i, (t, lab, cn) in enumerate(codes):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 110, t, 32, "serif", True, OLIVE)
    lx = bx + 22 + text_w(t, "serif", True, 32) + 14
    lw = bx + CW - 22 - lx
    yy = p.para(lx, dy + 92, lab, 21.5, "serif", False, INK, lw, 1.36)
    p.para(lx, yy + 20, cn, 19, "sans", False, GREY, lw, 1.3)
p.para(MX, dy + 234, "Let op: een lampion met een ledlampje is veilig — een kaarsje in papier is dat niet. Meer over Sint-Maarten en Halloween lees je op pagina 6.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "OEFENINGEN · EXERCÍCIOS DA PÁGINA 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8 · níveis misturados; procura o teu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · BEGRIJPEN", 25)
e.bridge("Lê o artigo da página 2 e escolhe a resposta certa.")
e.ex("A2", "choice", "B", "O São Martinho é na quarta-feira, 11 de novembro",
     "Sint-Maarten is op... A. maandag 9 november · B. woensdag 11 november · C. zaterdag 14 november", size=20, gap=8)
e.ex("A2", "choice", "B", "As crianças vão de porta em porta com lanternas",
     "Kinderen gaan langs de deuren met... A. een boek · B. een lampion · C. een fiets", size=20, gap=8)
e.ex("A2", "choice", "C", "Martinus deu metade do seu manto a um mendigo",
     "Martinus gaf de helft van zijn mantel aan... A. een kind · B. Sinterklaas · C. een bedelaar", size=20, gap=8)
e.ex("A2", "choice", "B", "Utrecht é a cidade de São Martinho",
     "De stad van Sint-Maarten is... A. Amsterdam · B. Utrecht · C. Grave", size=20, gap=8)
e.ex("A2", "choice", "B", "Uma lanterna leva uma luz LED, não uma vela",
     "In een lampion hoort... A. een kaarsje · B. een ledlampje · C. een lucifer", size=20, gap=8)
e.head("B · WOORDEN", 25)
e.bridge("Completa com as palavras da página 2.")
e.ex("A2", "complete", "11", "O São Martinho é a 11 de novembro",
     "Sint-Maarten is op ___ november.", instr="Complete", size=20, gap=8)
e.ex("A2", "complete", "lampion", "lampion = lanterna (de)",
     "Kinderen lopen met een ___ langs de deuren.", instr="Complete", size=20, gap=8)
e.ex("A2", "complete", "delen", "delen = partilhar",
     "Sint-Maarten is het feest van het ___.", instr="Complete", size=20, gap=8)
e.ex("A2", "complete", "mantel", "mantel = manto (de)",
     "Martinus sneed zijn ___ in tweeën.", instr="Complete", size=20, gap=8)
e.ex("A2", "complete", "Utrecht", "A cidade de São Martinho é Utrecht",
     "De viering in ___ staat op de erfgoedlijst.", instr="Complete", size=20, gap=8)
e.head("C · LIEDJE EN LICHT", 25)
e.bridge("Completa com as palavras da canção e o conselho de segurança.")
e.ex("A2", "complete", "lichtje", "Palavras da canção: a minha luzinha pode brilhar",
     "«Elf november is de dag, dat mijn ___ branden mag.»", instr="Complete", size=20, gap=8)
e.ex("A2", "complete", "donker", "As lanternas brilham mais quando está escuro",
     "Als het ___ wordt, gaan de kinderen op pad.", instr="Complete", size=20, gap=8)
e.ex("A2", "complete", "ledlampje", "Uma luz LED é segura",
     "Gebruik een ___ op batterijen, nooit een kaarsje.", instr="Complete", size=20, gap=8)
e.ex("A2", "complete", "5", "O Pakjesavond é a 5 de dezembro",
     "Pakjesavond is op zaterdag ___ december.", instr="Complete", size=20, gap=8)
e.head("D · WOORDEN", 25)
e.match_set("A2", "matching",
            ["de lampion", "delen", "de mantel", "het erfgoed"],
            ["licht delen met anderen, eten delen",
             "een papieren lichtje voor 11 november",
             "wat een land bewaart uit het verleden",
             "een lange jas tegen de kou"],
            ["b", "a", "d", "c"],
            ["lampion = lanterna b", "delen = partilhar a", "mantel = manto d", "erfgoed = património c"],
            instr="Ligue palavra-significado")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leven.svg")
print("P2 saved, exercises so far:", len(REG))
