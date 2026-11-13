# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTUUR (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTUUR　CULTURA", "De Lucerna", "NIVEAU A2 → B1　Sinterklaas is er!　Sinterklaas chegou!")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Sinterklaas is er: Grave, Amsterdam en het journaal", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2 → B1")
f.para("Op zaterdag 14 november kwam Sinterklaas officieel aan in Nederland. De landelijke intocht was dit jaar in Grave, een vestingstad aan de Maas in Noord-Brabant. Rond 12:00 uur meerde de stoomboot aan bij de Maaskade. Burgemeester Marieke Moorman ontving Sinterklaas. Het programma duurde van 12:00 tot 16:00 uur en was live te zien op NPO 3.")
f.para("Een dag later voer Sinterklaas in Amsterdam: de boot vertrok om 10:15 uur bij De Omval en voer over de Amstel naar het Scheepvaartmuseum, waar hij rond 11:30 uur aankwam. Daar kreeg hij de sleutel van de stad. Om 13:00 uur begon de stoet te paard bij de Stopera, via het Rembrandtplein en de Utrechtsestraat naar het Leidseplein. Het was de 88e editie van de Amsterdamse intocht.")
f.para("Het Sinterklaasjournaal is er elke dag om 18:00 uur op NPO Zapp. Presentatrice Merel Westrik vertelt hoe de voorbereidingen gaan: de schoen, de verlanglijstjes en — over negentien dagen — pakjesavond op zaterdag 5 december.")
f.para("November is ook de maand van Heel Nederland Leest: heel Nederland leest dit jaar Het diner van Herman Koch, uit 2009. Het boek is gratis af te halen in de bibliotheek, ook als je geen lid bent. Er is ook een grootletterboek, een Makkelijk Lezen-editie, een e-book en een luisterboek. In bibliotheken zijn er leeskringen — ook voor mensen die Nederlands leren.")
f.head("LEZEN EN KIJKEN", 25)
f.para("Twee dingen in november: 's avonds om 18:00 uur het Sinterklaasjournaal kijken, en overdag een boek lezen. Neem Het diner mee naar huis en praat erover met vrienden: samen lezen is leuker dan alleen lezen.")
f.para("En wie zijn schoen zet, kan er een verlanglijstje in doen — of een tekening. Sinterklaas leest alles.")
f.gloss("de vestingstad cidade fortificada · ontvangen receber · de sleutel chave · de editie edição · de leeskring círculo de leitura.")
f.end_report()

# col 3: image + facts box (sequential, measured)
ix = COLX[3]
image(p, "gracht.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Een boot in een Amsterdamse gracht. Zondag voer de stoomboot van Sinterklaas over de Amstel naar het Scheepvaartmuseum.",
              "Foto: W. Punt / Anefo, Nationaal Archief — CC0")
facts = ["Landelijke intocht: zaterdag 14 november, Grave, Maaskade, vanaf 12:00 uur op tv.",
         "Amsterdam: zondag 15 november, boot 10:15 uur, stoet 13:00 uur, 88e editie.",
         "Sinterklaasjournaal: elke dag 18:00 uur, NPO Zapp, met Merel Westrik.",
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
p.text(RIGHT, ey + 28, "Respostas na página 8　Os níveis estão misturados; procura o teu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Lê o artigo da página 3 e escolhe a resposta certa.")
e.ex("A2", "Escolha múltipla", "B", "A chegada nacional é em Grave",
     "De landelijke intocht was in... A. Amsterdam · B. Grave · C. Utrecht", size=20, gap=8)
e.ex("A2", "Escolha múltipla", "B", "O barco atraca na Maaskade por volta das 12:00",
     "De stoomboot meerde aan om... A. 18:00 uur · B. 12:00 uur · C. 20:45 uur", size=20, gap=8)
e.ex("A2", "Escolha múltipla", "C", "O barco de Amesterdão parte de De Omval às 10:15",
     "De boot in Amsterdam vertrok om... A. 12:00 uur · B. 13:00 uur · C. 10:15 uur", size=20, gap=8)
e.ex("A2", "Escolha múltipla", "A", "A chegada a Amesterdão é a 88.ª edição",
     "De intocht in Amsterdam was de... A. 88e editie · B. 26e editie · C. 30e editie", size=20, gap=8)
e.ex("A2", "Escolha múltipla", "B", "Het diner levanta-se grátis na biblioteca",
     "Het diner is gratis af te halen in... A. de boekwinkel · B. de bibliotheek · C. het museum", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("Completa com as palavras do quadro.")
e.para("vestingstad · ontvangen · sleutel · editie · leeskring", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Completa a frase", "vestingstad", "vestingstad = cidade fortificada",
     "Grave is een oude ___ aan de Maas.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "ontving", "ontvangen no passado: ontving",
     "Burgemeester Moorman ___ Sinterklaas in Grave.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "sleutel", "sleutel = chave",
     "Sinterklaas kreeg de ___ van de stad.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "editie", "editie = edição",
     "Het was de 88e ___ van de Amsterdamse intocht.", instr="Complete", size=20, gap=8)
e.ex("A2", "Completa a frase", "leeskring", "leeskring = círculo de leitura",
     "In de bibliotheek is er een ___ over Het diner.", instr="Complete", size=20, gap=8)
e.head("C　HET PERFECTUM", 25)
e.bridge("Completa no pretérito perfeito. Atenção aos auxiliares hebben/zijn.", w=464.7)  # delta D6: width-scan band 416.7–512.7px keeps the 2 lines; mid 464.7
e.ex("B1", "Completa a frase", "is aangekomen", "aankomen leva zijn: is aangekomen",
     "Sinterklaas ___ (aankomen) in Grave.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "heeft ontvangen", "ontvangen no perfeito: heeft ontvangen",
     "De burgemeester ___ (ontvangen) Sinterklaas.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "is gevaren", "varen com zijn: is gevaren",
     "De boot ___ (varen) van De Omval naar het Scheepvaartmuseum.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "hebben gelezen", "lezen no perfeito: hebben gelezen",
     "Veel mensen ___ (lezen) Het diner in november.", instr="Complete", size=20, gap=8)
e.head("D　REKENEN", 25)
e.bridge("Calcula: responde com números da página 3.")
e.ex("B1", "Completa a frase", "1", "De 14 a 15 de novembro é 1 dia",
     "Van zaterdag 14 tot zondag 15 november: ___ dag.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "4", "O programa de Grave, 12:00–16:00, dura 4 horas",
     "Het programma in Grave duurde van 12:00 tot 16:00 uur: ___ uur.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "19", "De 16 de novembro a 5 de dezembro são 19 dias",
     "Van 16 november tot 5 december: ___ dagen.", instr="Complete", size=20, gap=8)
e.ex("B2", "Completa a frase", "17", "Het diner é de 2009: há 17 anos em 2026",
     "Het diner is uit 2009; in 2026 is dat ___ jaar geleden.", instr="Complete", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultuur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　DESPORTO", "De Lucerna", "NIVEAU B1　Oranje en de Nations League　Oranje e a Liga das Nações")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P4-feature")
f.title("Oranje: de beslissing in Berlijn", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Op maandag 16 november speelt Oranje in Berlijn tegen Duitsland. De wedstrijd begint om 20:45 uur in het Olympiastadion en is live te zien op NPO 3. Het is de zesde en laatste wedstrijd in de groepsfase van de Nations League — en de beslissing in groep 2: de nummers één en twee gaan naar de kwartfinales in maart 2027.")
f.para("Na vier wedstrijden staan Nederland en Griekenland samen bovenaan met 8 punten. Duitsland heeft 5 punten, Servië heeft 0 punten. Nederland staat eerste, omdat het meer doelpunten maakte: 7 tegen 5. Oranje is nog ongeslagen: 1–1 thuis tegen Duitsland, 2–1 uit bij Servië, 2–2 uit bij Griekenland en 2–1 thuis tegen Servië.")
f.para("Duitsland moet winnen in Berlijn. De Duitsers verloren thuis met 0–1 van Griekenland, wonnen met 2–0 van Servië en speelden met 0–0 gelijk in Griekenland. Vrijdag speelde Duitsland in Belgrado tegen Servië; Oranje speelde vrijdag thuis tegen Griekenland. Maandagavond in Berlijn valt de beslissing.")
f.para("De Eredivisie begint zaterdag weer: speelronde 13 is op 21 en 22 november. Zaterdag speelt PSV om 16:30 uur uit bij NEC en speelt Feyenoord om 18:45 uur thuis tegen Excelsior. Zondag speelt Ajax om 14:30 uur thuis tegen ADO Den Haag en speelt FC Twente om 12:15 uur thuis tegen Willem II. Vóór de interlandperiode won PSV met 2–5 van Cambuur en werd het 5–3 bij Heerenveen – Feyenoord.")
f.head("DE STAND IN GROEP 2", 25)
f.para("Nederland 8 punten, Griekenland 8, Duitsland 5, Servië 0. Twee landen gaan door. Maandag in Berlijn is dus bijna een finale — de laatste wedstrijd van de groep.")
f.gloss("de groepswinst vitória do grupo · de kwartfinale quartos de final · ongeslagen invicto · de interland jogo internacional · de stand classificação.")
f.end_report()

# col 3: image + programme box (sequential, measured)
ix = COLX[3]
image(p, "elftal1912.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Het Nederlands elftal in 1912. Oranje speelt al meer dan honderd jaar in het oranje.",
              "Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein")
facts = ["Maandag 16 november, 20:45 uur: Duitsland – Nederland, Berlijn, NPO 3.",
         "Stand na 4 wedstrijden: Nederland 8, Griekenland 8, Duitsland 5, Servië 0 punten.",
         "Speelronde 12: Heerenveen – Feyenoord 5–3; Cambuur – PSV 2–5; Twente – Ajax 2–2.",
         "Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten.",
         "Speelronde 13: zaterdag NEC – PSV 16:30 uur; Feyenoord – Excelsior 18:45 uur."]
sy3 = cy3 + 24
# Fix5 D11: top reserve was 62 but box-top -> first baseline is really
# 16 (pad) + 52 (title block) + 21 (para y-offset) = 89; the 27px shortfall
# put the last baseline 6.89px below the box bottom. With 89 the last
# baseline (1209.49) sits 20.11px above the new box bottom (1229.6).
sh = 89 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
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
p.text(RIGHT, ey + 28, "Respostas na página 8　Os níveis estão misturados; procura o teu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Lê o artigo da página 4 e escolhe a resposta certa.")
e.ex("B1", "Escolha múltipla", "C", "Alemanha–Países Baixos, segunda-feira, em Berlim",
     "Duitsland – Nederland is op... A. vrijdag 13 november · B. zaterdag 14 november · C. maandag 16 november", size=20, gap=8)
e.ex("B1", "Escolha múltipla", "B", "Os Países Baixos e a Grécia têm ambos 8 pontos",
     "Na vier wedstrijden hebben Nederland en Griekenland... A. 5 punten · B. 8 punten · C. 0 punten", size=20, gap=8)
e.ex("B1", "Escolha múltipla", "B", "A Alemanha perdeu 0–1 em casa contra a Grécia",
     "Duitsland verloor thuis met 0–1 van... A. Servië · B. Griekenland · C. Nederland", size=20, gap=8)
e.ex("B1", "Escolha múltipla", "B", "A 13.ª jornada da Eredivisie é a 21–22 de novembro",
     "Speelronde 13 is op... A. 13 en 14 november · B. 21 en 22 november · C. 9 en 10 november", size=20, gap=8)
e.ex("B1", "Escolha múltipla", "B", "O PSV ganhou 2–5 ao Cambuur",
     "PSV won met 2–5 van... A. Feyenoord · B. Cambuur · C. Ajax", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("Completa com as palavras do quadro. Atenção às formas verbais.")
e.para("groepswinst · kwartfinale · ongeslagen · interland · stand", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Completa a frase", "groepswinst", "groepswinst = vitória do grupo",
     "Maandag valt de beslissing om de ___.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "kwartfinales", "kwartfinale, plural: kwartfinales",
     "De nummers één en twee gaan naar de ___.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "ongeslagen", "ongeslagen = invicto",
     "Oranje is nog ___ na vier wedstrijden.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "stand", "stand = classificação",
     "Op de ___ staat Servië onderaan met 0 punten.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "interland", "interland = jogo internacional",
     "Na maandag is er geen ___ meer tot maart.", instr="Complete", size=20, gap=8)
e.head("C　VERLEDEN TIJD", 25)
e.bridge("Completa no passado ou no perfeito.")
e.ex("B1", "Completa a frase", "speelde", "spelen no passado: speelde",
     "Oranje ___ (spelen) 1–1 tegen Duitsland.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "won", "winnen no passado: won",
     "PSV ___ (winnen) met 2–5 van Cambuur.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completa a frase", "verloor", "verliezen no passado: verloor",
     "Feyenoord ___ (verliezen) met 5–3 bij Heerenveen.", instr="Complete", size=20, gap=8)
e.ex("B2", "Completa a frase", "speelden", "spelen no passado, plural: speelden",
     "Twente en Ajax ___ (spelen) 2–2 gelijk.", instr="Complete", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "Verdadeiro ou falso", "Waar", "Verdadeiro: Alemanha–Países Baixos, segunda-feira às 20:45",
     "Duitsland – Nederland begint maandag om 20:45 uur. Waar of niet waar?", instr="Verdadeiro ou falso?", size=20, gap=8)
e.ex("B1", "Verdadeiro ou falso", "Niet waar", "Falso: a Sérvia é última com 0 pontos",
     "Servië heeft 8 punten in groep 2. Waar of niet waar?", instr="Verdadeiro ou falso?", size=20, gap=8)
e.ex("B1", "Verdadeiro ou falso", "Niet waar", "Falso: o PSV lidera a Eredivisie com 26 pontos",
     "PSV staat onderaan in de Eredivisie. Waar of niet waar?", instr="Verdadeiro ou falso?", size=20, gap=8)
e.ex("B1", "Verdadeiro ou falso", "Waar", "Verdadeiro: o Heerenveen ganhou 5–3 ao Feyenoord",
     "Heerenveen won met 5–3 van Feyenoord. Waar of niet waar?", instr="Verdadeiro ou falso?", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
