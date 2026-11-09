# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTUUR (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTUUR　CULTURA", "De Lucerna", "NIVEAU A2 → B1　Sinterklaasjournaal en Het diner　As notícias do Sinterklaas e Het diner")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Het Sinterklaasjournaal begint: aftellen naar Grave", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2 → B1")
f.para("Op maandag 9 november begint het Sinterklaasjournaal op NPO Zapp. Elke dag om 18:00 uur vertelt presentatrice Merel Westrik hoe de voorbereidingen gaan. Aan het einde van vorig jaar gooide Sinterklaas een fles in zee met een aanwijzing — de flessenpost werd gevonden en leidde naar Grave.")
f.para("Op zaterdag 14 november komt Sinterklaas officieel aan in Grave. Rond 12:00 uur meert de stoomboot aan bij de Maaskade, aan de Maas. Burgemeester Marieke Moorman ontvangt Sinterklaas. Het programma in Grave duurt van 12:00 tot 16:00 uur en is live te zien op NPO Zapp (NPO 3), vanaf 12:00 uur.")
f.para("Een dag later vaart Sinterklaas in Amsterdam: de boot vertrekt om 10:15 uur bij De Omval en vaart over de Amstel naar het Scheepvaartmuseum, waar hij rond 11:30 uur aankomt. Daar krijgt hij de sleutel van de stad van burgemeester Halsema en de kinderburgemeester. Om 13:00 uur begint de stoet te paard bij de Stopera, via het Rembrandtplein en de Utrechtsestraat naar het Leidseplein.")
f.para("November is ook de maand van Heel Nederland Leest: heel Nederland leest dit jaar Het diner van Herman Koch, uit 2009. Het boek is vanaf 1 november gratis af te halen in de bibliotheek, ook als je geen lid bent. Er is ook een grootletterboek, een Makkelijk Lezen-editie, een e-book en een luisterboek. In bibliotheken zijn er leeskringen — ook voor mensen die Nederlands leren.")
f.head("LEZEN EN KIJKEN", 25)
f.para("Twee feesten in één week: 's avonds om 18:00 uur het Sinterklaasjournaal kijken, en overdag een boek lezen. Neem Het diner mee naar huis en praat erover met vrienden: samen lezen is leuker dan alleen lezen.")
f.para("En wie zaterdag naar Grave kijkt op televisie, ziet de eerste intocht van dit jaar. Zondag volgt Amsterdam. Daarna begint de tijd van de schoen — en van verlanglijstjes.")
f.gloss("het journaal = o noticiário · de flessenpost = a mensagem na garrafa · de burgemeester = o presidente da câmara · de stoet = o cortejo · de leeskring = o círculo de leitura.")
f.end_report()

# col 3: image + facts box (sequential, measured)
ix = COLX[3]
image(p, "gracht.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Een boot in een Amsterdamse gracht. Zondag vaart de stoomboot van Sinterklaas over de Amstel naar het Scheepvaartmuseum.",
              "Foto: W. Punt / Anefo, Nationaal Archief — CC0")
facts = ["Sinterklaasjournaal: vanaf maandag 9 november, elke dag 18:00 uur, NPO Zapp.",
         "Landelijke intocht: zaterdag 14 november, Grave, Maaskade, vanaf 12:00 uur op tv.",
         "Amsterdam: zondag 15 november, boot 10:15 uur, stoet 13:00 uur, 88e editie.",
         "Heel Nederland Leest: Het diner, gratis in de bibliotheek, heel november."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 64
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SINTERKLAAS IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　EXERCÍCIOS DA PÁGINA 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8　níveis misturados; procura o teu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Lê o artigo da página 3 e escolhe a resposta certa.")
e.ex("A2", "choice", "B", "As notícias do Sinterklaas passam todos os dias às 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 12:00 uur · B. 18:00 uur · C. 20:45 uur", size=20, gap=8)
e.ex("A2", "choice", "B", "A chegada nacional é em Grave",
     "De landelijke intocht is in... A. Amsterdam · B. Grave · C. Utrecht", size=20, gap=8)
e.ex("A2", "choice", "C", "O barco de Amesterdão parte de De Omval às 10:15",
     "De boot in Amsterdam vertrekt om... A. 12:00 uur · B. 13:00 uur · C. 10:15 uur", size=20, gap=8)
e.ex("A2", "choice", "A", "Het diner foi escrito por Herman Koch",
     "Heel Nederland Leest leest dit jaar... A. Het diner van Herman Koch · B. een boek van Merel Westrik · C. een boek over Grave", size=20, gap=8)
e.ex("A2", "choice", "B", "Het diner levanta-se grátis na biblioteca",
     "Het diner is gratis af te halen in... A. de boekwinkel · B. de bibliotheek · C. het museum", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("Completa com as palavras do quadro.")
e.para("journaal · burgemeester · stoet · leeskring · flessenpost", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "complete", "journaal", "journaal = noticiário",
     "Het Sinterklaas___ begint op 9 november.", instr="Complete", size=20, gap=8)
e.ex("A2", "complete", "burgemeester", "burgemeester = presidente da câmara",
     "De ___ ontvangt Sinterklaas in Grave.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "stoet", "stoet = cortejo",
     "Om 13:00 uur begint de ___ te paard.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "flessenpost", "flessenpost = mensagem na garrafa",
     "De ___ leidde naar Grave.", instr="Complete", size=20, gap=8)
e.ex("A2", "complete", "leeskring", "leeskring = círculo de leitura",
     "In de bibliotheek is er een ___ over Het diner.", instr="Complete", size=20, gap=8)
e.head("C　HET PERFECTUM", 25)
e.bridge("Completa no pretérito perfeito. Atenção aos auxiliares hebben/zijn.")
e.ex("B1", "complete", "is begonnen", "beginnen leva zijn: is begonnen",
     "Het Sinterklaasjournaal ___ (beginnen) op 9 november.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "heeft gevonden", "vinden no perfeito: heeft gevonden",
     "Iemand ___ (vinden) de flessenpost.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "is aangekomen", "aankomen leva zijn: is aangekomen",
     "Sinterklaas ___ (aankomen) in Grave.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "hebben gelezen", "lezen no perfeito: hebben gelezen",
     "Veel mensen ___ (lezen) Het diner in november.", instr="Complete", size=20, gap=8)
e.head("D　REKENEN", 25)
e.bridge("Calcula: responde com números da página 3.")
e.ex("B1", "complete", "5", "De 9 a 14 de novembro são 5 dias",
     "Van 9 tot 14 november: ___ dagen.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "6", "De 9 a 15 de novembro são 6 dias",
     "Van 9 tot 15 november: ___ dagen.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "4", "O programa de Grave, 12:00–16:00, dura 4 horas",
     "Het programma in Grave duurt van 12:00 tot 16:00 uur: ___ uur.", instr="Complete", size=20, gap=8)
e.ex("B2", "complete", "17", "Het diner é de 2009: há 17 anos em 2026",
     "Het diner is uit 2009; in 2026 is dat ___ jaar geleden.", instr="Complete", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultuur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT", "De Lucerna", "NIVEAU B1　Oranje en de Nations League　Oranje e a Liga das Nações")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P4-feature")
f.title("Oranje: twee wedstrijden, één doel", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Op vrijdag 13 november speelt Oranje thuis tegen Griekenland. De wedstrijd begint om 20:45 uur in de Johan Cruijff ArenA in Amsterdam. Het is de vijfde wedstrijd in de groepsfase van de Nations League — en een beslissende: de nummers één en twee van de groep gaan naar de kwartfinales in maart 2027.")
f.para("Na vier wedstrijden staan Nederland en Griekenland samen bovenaan met 8 punten. Duitsland heeft 5 punten, Servië heeft 0 punten. Nederland staat eerste, omdat het meer doelpunten maakte: 7 tegen 5. Oranje is nog ongeslagen: 1–1 thuis tegen Duitsland, 2–1 uit bij Servië, 2–2 uit bij Griekenland en 2–1 thuis tegen Servië.")
f.para("Drie dagen later, op maandag 16 november, speelt Oranje uit tegen Duitsland in Berlijn, ook om 20:45 uur. De spelers melden zich op maandag 9 november in Zeist. Daarna is er geen interland meer tot maart: dan zijn de kwartfinales.")
f.para("De Eredivisie ligt deze week stil: het is interlandperiode. Speelronde 13 is pas op 21 en 22 november, met zaterdag NEC tegen PSV en Feyenoord tegen Excelsior, en zondag Twente tegen Willem II en Ajax tegen ADO Den Haag. Vorige week, in speelronde 11, won PSV met 7–0 van Willem II en won Ajax met 1–0 van AZ.")
f.head("DE STAND IN GROEP 2", 25)
f.para("Nederland 8 punten, Griekenland 8, Duitsland 5, Servië 0. Twee landen gaan door. Vrijdag tegen Griekenland is dus bijna een finale — en maandag in Berlijn de tweede.")
f.gloss("de groepsfase = a fase de grupos · de kwartfinale = os quartos de final · ongeslagen = invicto · de interland = o jogo internacional · de stand = a classificação.")
f.end_report()

# col 3: image + programme box (sequential, measured)
ix = COLX[3]
image(p, "elftal1912.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Het Nederlands elftal in 1912. Oranje speelt al meer dan honderd jaar in het oranje.",
              "Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein")
facts = ["Vrijdag 13 november, 20:45 uur: Nederland – Griekenland, Johan Cruijff ArenA.",
         "Maandag 16 november, 20:45 uur: Duitsland – Nederland, Berlijn.",
         "Stand na 4 wedstrijden: Nederland 8, Griekenland 8, Duitsland 5, Servië 0 punten.",
         "Speelronde 11: PSV – Willem II 7–0; Ajax – AZ 1–0; Feyenoord – Fortuna 1–1; Cambuur – Go Ahead Eagles 4–0."]
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
p.text(MX, ey + 28, "OEFENINGEN　EXERCÍCIOS DA PÁGINA 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8　níveis misturados; procura o teu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Lê o artigo da página 4 e escolhe a resposta certa.")
e.ex("B1", "choice", "B", "Países Baixos–Grécia, sexta-feira 20:45, em Amesterdão",
     "Nederland – Griekenland is op... A. maandag 16 november · B. vrijdag 13 november · C. zaterdag 14 november", size=20, gap=8)
e.ex("B1", "choice", "C", "Os Países Baixos e a Grécia têm ambos 8 pontos",
     "Na vier wedstrijden hebben Nederland en Griekenland... A. 5 punten · B. 7 punten · C. 8 punten", size=20, gap=8)
e.ex("B1", "choice", "A", "Os Países Baixos marcaram mais golos no grupo: 7 a 5",
     "Nederland staat eerste, omdat het... A. meer doelpunten maakte · B. meer wedstrijden speelde · C. thuis speelt", size=20, gap=8)
e.ex("B1", "choice", "B", "Alemanha–Países Baixos, segunda-feira, em Berlim",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=20, gap=8)
e.ex("B1", "choice", "B", "A 13.ª jornada da Eredivisie é a 21–22 de novembro",
     "Speelronde 13 is op... A. 13 en 14 november · B. 21 en 22 november · C. 9 en 10 november", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("Completa com as palavras do quadro. Atenção às formas verbais.")
e.para("groepsfase · kwartfinale · ongeslagen · interland · stand", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "complete", "groepsfase", "groepsfase = fase de grupos",
     "Het is de vijfde wedstrijd in de ___.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "kwartfinales", "kwartfinale, plural: kwartfinales",
     "De nummers één en twee gaan naar de ___.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "ongeslagen", "ongeslagen = invicto",
     "Oranje is nog ___ na vier wedstrijden.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "stand", "stand = classificação",
     "Op de ___ staat Servië onderaan met 0 punten.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "interland", "interland = jogo internacional",
     "Na deze week is er geen ___ meer tot maart.", instr="Complete", size=20, gap=8)
e.head("C　VERLEDEN TIJD", 25)
e.bridge("Completa no passado ou no perfeito.")
e.ex("B1", "complete", "speelde", "spelen no passado: speelde",
     "Oranje ___ (spelen) 1–1 tegen Duitsland.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "won", "winnen no passado: won",
     "PSV ___ (winnen) met 7–0 van Willem II.", instr="Complete", size=20, gap=8)
e.ex("B1", "complete", "maakte", "maken no passado: maakte",
     "Nederland ___ (maken) 7 doelpunten in vier wedstrijden.", instr="Complete", size=20, gap=8)
e.ex("B2", "complete", "zijn gekomen", "komen no perfeito leva zijn",
     "De spelers ___ (komen) maandag in Zeist bij elkaar.", instr="Complete", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "true or false", "Waar", "Verdadeiro: Países Baixos–Grécia, sexta-feira 20:45",
     "Nederland – Griekenland begint vrijdag om 20:45 uur. Waar of niet waar?", instr="Verdadeiro ou falso?", size=20, gap=8)
e.ex("B1", "true or false", "Niet waar", "Falso: a Sérvia é última com 0 pontos",
     "Servië heeft 8 punten in groep 2. Waar of niet waar?", instr="Verdadeiro ou falso?", size=20, gap=8)
e.ex("B1", "true or false", "Niet waar", "Falso: a 13.ª jornada da Eredivisie é a 21–22 de novembro",
     "Speelronde 13 is deze week. Waar of niet waar?", instr="Verdadeiro ou falso?", size=20, gap=8)
e.ex("B1", "true or false", "Waar", "Verdadeiro: o PSV bateu o Willem II por 7–0",
     "PSV won met 7–0 van Willem II. Waar of niet waar?", instr="Verdadeiro ou falso?", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
