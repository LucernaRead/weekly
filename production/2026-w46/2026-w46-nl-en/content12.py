# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · VOORPAGINA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "ELKE WEEK IN HET NEDERLANDS　EVERY WEEK　REAL DUTCH", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "WEEK VAN 9 TOT EN MET 15 NOVEMBER 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "De Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "WEEKBLAD IN HET NEDERLANDS　VOL.3　SINTERKLAAS　SINT-MAARTEN　ORANJE", 34, "serif", True, OLIVE, anchor="middle", spacing=0)
p.text(975, 372, "TEXT IN DUTCH　EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "SINTERKLAAS KOMT ERAAN!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Eerst het Sinterklaasjournaal, dan de intocht in Grave en in Amsterdam.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "SINTERKLAAS IS COMING", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "This week: Sinterklaas comes to the Netherlands　see page 3", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "HET NIEUWS　TOP STORY", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Sinterklaas komt eraan: eerst Grave, dan Amsterdam", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Van de redactie van De Lucerna　Leesniveau: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Op maandag 9 november begint het Sinterklaasjournaal op televisie. Elke dag om 18:00 uur volgen kinderen op NPO Zapp hoe Sinterklaas en zijn Pieten zich voorbereiden op de reis naar Nederland.")
f.para("Op zaterdag 14 november komt Sinterklaas officieel aan in Nederland. De landelijke intocht is dit jaar in Grave, een vestingstad aan de Maas in Noord-Brabant. Rond 12:00 uur meert de stoomboot aan bij de Maaskade. De intocht is live te zien op NPO 3.")
f.para("Een dag later, op zondag 15 november, is de intocht in Amsterdam: de 88e editie. De boot vertrekt om 10:15 uur bij De Omval en vaart over de Amstel naar het Scheepvaartmuseum. Daar krijgt Sinterklaas de sleutel van de stad. Daarna gaat hij te paard door de stad naar het Leidseplein.")
f.para("Eerder in de week, op woensdag 11 november, is het Sint-Maarten: kinderen gaan met lampionnen zingend langs de deuren (pagina 2). En op vrijdag 13 november speelt Oranje thuis tegen Griekenland (pagina 4).")
f.para("Na de intocht zetten kinderen hun schoen. Sinterklaas komt dan 's nachts met cadeautjes. Pakjesavond is dit jaar op zaterdag 5 december.")
f.bridge("Note | de intocht = arrival · de stoomboot = steamboat · de lampion = lantern.")
f.box("DE WEEK IN CIJFERS　IN NUMBERS", [
    ("9 — november: het Sinterklaasjournaal begint (9 Nov: Sinterklaas news)", "serif", False, INK, 20, 1.35),
    ("14 — november: de landelijke intocht in Grave (14 Nov: national arrival, Grave)", "serif", False, INK, 20, 1.35),
    ("15 — november: de intocht in Amsterdam, de 88e editie (15 Nov: 88th)", "serif", False, INK, 20, 1.35),
    ("20:45 — uur: Oranje tegen Griekenland op vrijdag (Fri 20:45)", "serif", False, INK, 20, 1.35),
])
f.head("NU JIJ　YOUR TURN", 25)
f.ex("A2", "complete", "9", "The Sinterklaas news starts on 9 November",
     "Het Sinterklaasjournaal begint op maandag ___ november.", size=19.5, gap=6)
f.ex("A2", "complete", "Grave", "The national arrival is in Grave",
     "De landelijke intocht is dit jaar in ___.", size=19.5, gap=6)
f.ex("A2", "complete", "15", "The Amsterdam arrival is on Sunday 15 November",
     "De intocht in Amsterdam is op zondag ___ november.", size=19.5, gap=6)
f.ex("A2", "complete", "11", "St Martin's Day is on Wednesday 11 November",
     "Sint-Maarten is op woensdag ___ november.", size=19.5, gap=6)
f.ex("A2", "complete", "20:45", "Netherlands–Greece kicks off at 20:45",
     "Oranje tegen Griekenland begint vrijdag om ___ uur.", size=19.5, gap=6)
f.ex("B1", "complete", "zetten", "Plural subject, so zetten",
     "Na de intocht ___ (zetten) kinderen hun schoen.", size=19.5, gap=6)
f.end_report()

# ---- deze week agenda (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "DEZE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "　THIS WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Agenda van de week　THIS WEEK'S EVENTS", 19, "sans", False, GREY)
gt = [
    ("MA 9", "Sinterklaasjournaal begint"),
    ("WO 11", "Sint-Maarten, lampionnen"),
    ("VR 13", "Oranje – Griekenland"),
    ("ZA 14", "Intocht in Grave"),
    ("ZO 15", "Intocht Amsterdam"),
]
byy = gy + 150
for i, (lab, vol) in enumerate(gt):
    p.text(gx + 22, byy + 22, lab, 20, "serif", True, OLIVE)
    p.text(gx + 110, byy + 22, vol, 20, "serif", False, INK)
    byy += 62
p.text(gx + 22, byy + 16, "Alle data en tijden staan ook", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "in de artikelen op pagina 2–4.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "See pages 2–4 for all dates and times.", 19, "sans", False, GREY)

# ---- inhoud (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "IN DEZE EDITIE　IN THIS ISSUE", 24, "sans", True, OLIVE)
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
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- woord van de week (col 3) ----
my = 1652
p.text(gx, my + 24, "HET WOORD VAN DE WEEK", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "«de intocht»", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "de feestelijke aankomst van Sinterklaas in een stad, met de boot en daarna te paard.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 26, "«The intocht»: Sinterklaas arrives in a town by boat, then on horseback, in a festive parade.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1853, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "westertoren.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "De Westertoren in Amsterdam. Zondag 15 november vaart Sinterklaas over de Amstel naar het Scheepvaartmuseum en rijdt hij daarna te paard naar het Leidseplein. (Pagina 3)",
        "Foto: Wim van Rossem / Anefo, Nationaal Archief — CC0")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-extra")
f2.head("NA DE INTOCHT: DE SCHOEN", 25)
f2.para("Na de intocht mag de schoen: kinderen zetten 's avonds hun schoen bij de deur, met een wortel voor het paard en een tekening voor Sinterklaas. 's Nachts komt Sinterklaas met een cadeautje.", 22.5)
f2.para("Pakjesavond, de avond met de grote cadeaus, is dit jaar op zaterdag 5 december.", 22.5)
f2.end_report()
# col 3 IN HET KORT
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX)
p.text(bx + 22, 1914, "IN HET KORT　IN BRIEF", 24, "sans", True, OLIVE)
brefs = [
    ("SINTERKLAAS · P.3", "Maandag Sinterklaasjournaal; zaterdag intocht in Grave."),
    ("SINT-MAARTEN · P.2", "Woensdag: kinderen met lampionnen langs de deuren."),
    ("ORANJE · P.4", "Vrijdag: Nederland – Griekenland, 20:45 uur, Amsterdam."),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz bliksem ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "BLIKSEMQUIZ　LIGHTNING QUIZ", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Read page 1, choose the right answer　answers on page 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "choice", "B", "The Sinterklaas news starts on Monday 9 November",
      "Het Sinterklaasjournaal begint op... A. zaterdag 14 november · B. maandag 9 november · C. zondag 15 november", size=21)
qf.ex("A2", "choice", "B", "The national arrival is in Grave",
      "De landelijke intocht is in... A. Amsterdam · B. Grave · C. Utrecht", size=21)
qf.ex("A2", "choice", "C", "The Amsterdam arrival is the 88th edition",
      "De intocht in Amsterdam is de... A. 26e editie · B. 30e editie · C. 88e editie", size=21)
qf.ex("A2", "choice", "B", "Netherlands–Greece kicks off at 20:45 on Friday",
      "Oranje – Griekenland begint om... A. 18:00 uur · B. 20:45 uur · C. 12:00 uur", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-voorpagina.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LEVEN (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LEVEN　LIFE", "De Lucerna", "NIVEAU A2　Sint-Maarten: lichtjes en liedjes　St Martin's Day: lanterns and songs")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Sint-Maarten: lichtjes in het donker", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2")
f.para("Op woensdag 11 november is het Sint-Maarten. Als het donker wordt, gaan kinderen met een lampion langs de deuren. Ze zingen een liedje en krijgen snoep of fruit. Het bekendste liedje begint zo: «Elf november is de dag, dat mijn lichtje branden mag.»")
f.para("Het feest gaat over Sint-Maarten, of Martinus. Volgens de legende sneed hij zijn mantel in tweeën en gaf hij de helft aan een bedelaar in de kou. Daarom is Sint-Maarten het feest van het delen: licht delen, eten delen, aandacht delen.")
f.para("Sint-Maarten wordt niet overal in Nederland even uitbundig gevierd. Sterke gebieden zijn het noorden, de stad Utrecht, Noord-Holland boven het IJ, Noord-Brabant en Limburg. In Utrecht, de stad van Sint-Maarten, staat de viering op de lijst van het immaterieel erfgoed. Daar lopen kinderen 's avonds «lichies lope»: met lampionnen zingend langs de deuren.")
f.para("Wil je meedoen? Maak zelf een lampion van papier en versier hem met vliegerpapier, zodat het licht er mooi doorheen schijnt. Gebruik een ledlampje op batterijen, nooit een kaarsje. En zing een liedje bij elke deur — dan is het feest compleet.")
f.para("Sint-Maarten valt dit jaar midden in de Sinterklaastijd: maandag begon het Sinterklaasjournaal en zaterdag komt Sinterklaas aan in Grave. Twee feesten van licht en geven, in één week.")
f.head("DRIE DINGEN VOOR 11 NOVEMBER", 25)
f.para("Eén: maak een lampion, met een ledlampje erin. Twee: leer een liedje, bijvoorbeeld «Elf november is de dag». Drie: ga zingend langs de deuren — en deel wat je krijgt.")
f.box("ZO ONTHOUD JE HET　REMEMBER", [
    ("«Sint-Maarten is het feest van het delen: licht, eten en aandacht.» En de lampion gaat aan als het donker wordt.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("de lampion = lantern · delen = to share · de mantel = cloak, coat · de bedelaar = beggar · het erfgoed = heritage · het ledlampje = little LED light.")
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
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WIST JE DAT?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Loop jij op 11 november met een lampion langs de deuren, of kijk je liever naar het Sinterklaasjournaal? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie: de mooiste komen in VOL.4 (pagina 7, «Brieven van lezers»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("On 11 November, will you go singing door to door with a lantern, or would you rather watch the Sinterklaas news? Write two sentences in Dutch and send them to the editors.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ?　AND YOU?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "On 11 November, will you go singing door to door with a lantern, or would you rather watch the Sinterklaas news? Write two sentences in Dutch and send them to the editors.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- lichtjes row: 4 boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "SINT-MAARTEN IN VIER WOORDEN　FOUR KEY WORDS", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Wat hoort bij het feest?　Which words belong to the festival?", 20, "sans", False, GREY, anchor="end")
codes = [
    ("LAMPION", "het lichtje", "a paper lantern, with an LED light inside"),
    ("LIEDJE", "het zingen", "singing St Martin's songs door to door"),
    ("DELEN", "het geven", "sharing: giving half a cloak to a beggar"),
    ("UTRECHT", "de stad", "St Martin's city, on the heritage list"),
]
for i, (t, lab, cn) in enumerate(codes):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 110, t, 32, "serif", True, OLIVE)
    lx = bx + 22 + text_w(t, "serif", True, 32) + 14
    lw = bx + CW - 22 - lx
    yy = p.para(lx, dy + 92, lab, 21.5, "serif", False, INK, lw, 1.36)
    p.para(lx, yy + 20, cn, 19, "sans", False, GREY, lw, 1.3)
p.para(MX, dy + 234, "Let op: een lampion met een ledlampje is veilig — een kaarsje in papier is dat niet. Meer over Sint-Maarten en Halloween lees je op pagina 6.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　EXERCISES ON PAGE 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8　levels are mixed; find your number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Read the article on page 2 and choose the right answer.")
e.ex("A2", "choice", "B", "St Martin's Day is on Wednesday 11 November",
     "Sint-Maarten is op... A. maandag 9 november · B. woensdag 11 november · C. zaterdag 14 november", size=20, gap=8)
e.ex("A2", "choice", "B", "Children go door to door with lanterns",
     "Kinderen gaan langs de deuren met... A. een boek · B. een lampion · C. een fiets", size=20, gap=8)
e.ex("A2", "choice", "C", "Martinus gave half his cloak to a beggar",
     "Martinus gaf de helft van zijn mantel aan... A. een kind · B. Sinterklaas · C. een bedelaar", size=20, gap=8)
e.ex("A2", "choice", "B", "Utrecht is St Martin's city",
     "De stad van Sint-Maarten is... A. Amsterdam · B. Utrecht · C. Grave", size=20, gap=8)
e.ex("A2", "choice", "B", "A lantern takes an LED light, not a candle",
     "In een lampion hoort... A. een kaarsje · B. een ledlampje · C. een lucifer", size=20, gap=8)
e.head("B　WOORDEN", 25)
e.bridge("Fill in with words from page 2.")
e.ex("A2", "complete", "11", "St Martin's Day is on 11 November",
     "Sint-Maarten is op ___ november.", instr="Fill in", size=20, gap=8)
e.ex("A2", "complete", "lampion", "lampion = lantern (de)",
     "Kinderen lopen met een ___ langs de deuren.", instr="Fill in", size=20, gap=8)
e.ex("A2", "complete", "delen", "delen = to share",
     "Sint-Maarten is het feest van het ___.", instr="Fill in", size=20, gap=8)
e.ex("A2", "complete", "mantel", "mantel = cloak (de)",
     "Martinus sneed zijn ___ in tweeën.", instr="Fill in", size=20, gap=8)
e.ex("A2", "complete", "Utrecht", "St Martin's city is Utrecht",
     "De viering in ___ staat op de erfgoedlijst.", instr="Fill in", size=20, gap=8)
e.head("C　LIEDJE EN LICHT", 25)
e.bridge("Fill in with the song words and the safety tip.")
e.ex("A2", "complete", "lichtje", "Song words: my little light may shine",
     "«Elf november is de dag, dat mijn ___ branden mag.»", instr="Fill in", size=20, gap=8)
e.ex("A2", "complete", "donker", "Lanterns shine brightest when it is dark",
     "Als het ___ wordt, gaan de kinderen op pad.", instr="Fill in", size=20, gap=8)
e.ex("A2", "complete", "ledlampje", "An LED light is safe",
     "Gebruik een ___ op batterijen, nooit een kaarsje.", instr="Fill in", size=20, gap=8)
e.ex("A2", "complete", "5", "Pakjesavond is on 5 December",
     "Pakjesavond is op zaterdag ___ december.", instr="Fill in", size=20, gap=8)
e.head("D　WOORDEN", 25)
e.match_set("A2", "matching",
            ["de lampion", "delen", "de mantel", "het erfgoed"],
            ["licht delen met anderen, eten delen",
             "een papieren lichtje voor 11 november",
             "wat een land bewaart uit het verleden",
             "een lange jas tegen de kou"],
            ["b", "a", "d", "c"],
            ["lampion = lantern b", "delen = to share a", "mantel = cloak d", "erfgoed = heritage c"],
            instr="Match word to meaning")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leven.svg")
print("P2 saved, exercises so far:", len(REG))
