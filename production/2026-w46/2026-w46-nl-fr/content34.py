# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTUUR (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTUUR　CULTURE", "De Lucerna", "NIVEAU A2 → B1　Sinterklaasjournaal en Het diner　Le journal de Sinterklaas et Het diner")

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
f.gloss("het journaal : le journal télévisé · de flessenpost : la bouteille à la mer · de burgemeester : le maire · de stoet : le cortège · de leeskring : le cercle de lecture.")
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
p.text(MX, ey + 28, "OEFENINGEN　EXERCICES PAGE 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　niveaux mélangés ; cherche ton numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Lis l'article page 3 et choisis la bonne réponse.")
e.ex("A2", "Choix unique", "B", "Le journal de Sinterklaas passe chaque jour à 18 h 00",
     "Het Sinterklaasjournaal is elke dag om... A. 12:00 uur · B. 18:00 uur · C. 20:45 uur", size=20, gap=8)
e.ex("A2", "Choix unique", "B", "L'arrivée nationale a lieu à Grave",
     "De landelijke intocht is in... A. Amsterdam · B. Grave · C. Utrecht", size=20, gap=8)
e.ex("A2", "Choix unique", "C", "Le bateau d'Amsterdam part de De Omval à 10 h 15",
     "De boot in Amsterdam vertrekt om... A. 12:00 uur · B. 13:00 uur · C. 10:15 uur", size=20, gap=8)
e.ex("A2", "Choix unique", "A", "Het diner a été écrit par Herman Koch",
     "Heel Nederland Leest leest dit jaar... A. Het diner van Herman Koch · B. een boek van Merel Westrik · C. een boek over Grave", size=20, gap=8)
e.ex("A2", "Choix unique", "B", "Het diner est gratuit à la bibliothèque",
     "Het diner is gratis af te halen in... A. de boekwinkel · B. de bibliotheek · C. het museum", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("Complète avec les mots de l'encadré.")
e.para("journaal · burgemeester · stoet · leeskring · flessenpost", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Compléter les phrases", "journaal", "journaal = journal télévisé",
     "Het Sinterklaas___ begint op 9 november.", instr="Compléter", size=20, gap=8)
e.ex("A2", "Compléter les phrases", "burgemeester", "burgemeester = maire",
     "De ___ ontvangt Sinterklaas in Grave.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "stoet", "stoet = cortège",
     "Om 13:00 uur begint de ___ te paard.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "flessenpost", "flessenpost = bouteille à la mer",
     "De ___ leidde naar Grave.", instr="Compléter", size=20, gap=8)
e.ex("A2", "Compléter les phrases", "leeskring", "leeskring = cercle de lecture",
     "In de bibliotheek is er een ___ over Het diner.", instr="Compléter", size=20, gap=8)
e.head("C　HET PERFECTUM", 25)
e.bridge("Complète au passé composé. Attention aux auxiliaires hebben/zijn.")
e.ex("B1", "Compléter les phrases", "is begonnen", "beginnen prend zijn : is begonnen",
     "Het Sinterklaasjournaal ___ (beginnen) op 9 november.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "heeft gevonden", "vinden au parfait : heeft gevonden",
     "Iemand ___ (vinden) de flessenpost.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "is aangekomen", "aankomen prend zijn : is aangekomen",
     "Sinterklaas ___ (aankomen) in Grave.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "hebben gelezen", "lezen au parfait : hebben gelezen",
     "Veel mensen ___ (lezen) Het diner in november.", instr="Compléter", size=20, gap=8)
e.head("D　REKENEN", 25)
e.bridge("Calcule : réponds par les chiffres de la page 3.")
e.ex("B1", "Compléter les phrases", "5", "Du 9 au 14 novembre, cela fait 5 jours",
     "Van 9 tot 14 november: ___ dagen.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "6", "Du 9 au 15 novembre, cela fait 6 jours",
     "Van 9 tot 15 november: ___ dagen.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "4", "Le programme de Grave, de 12 h 00 à 16 h 00, dure 4 heures",
     "Het programma in Grave duurt van 12:00 tot 16:00 uur: ___ uur.", instr="Compléter", size=20, gap=8)
e.ex("B2", "Compléter les phrases", "17", "Het diner date de 2009 : il y a 17 ans en 2026",
     "Het diner is uit 2009; in 2026 is dat ___ jaar geleden.", instr="Compléter", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultuur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　SPORT", "De Lucerna", "NIVEAU B1　Oranje en de Nations League　Oranje et la Ligue des nations")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P4-feature")
f.title("Oranje: twee wedstrijden, één doel", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Op vrijdag 13 november speelt Oranje thuis tegen Griekenland. De wedstrijd begint om 20:45 uur in de Johan Cruijff ArenA in Amsterdam. Het is de vijfde wedstrijd in de groepsfase van de Nations League — en een beslissende: de nummers één en twee van de groep gaan naar de kwartfinales in maart 2027.")
f.para("Na vier wedstrijden staan Nederland en Griekenland samen bovenaan met 8 punten. Duitsland heeft 5 punten, Servië heeft 0 punten. Nederland staat eerste, omdat het meer doelpunten maakte: 7 tegen 5. Oranje is nog ongeslagen: 1–1 thuis tegen Duitsland, 2–1 uit bij Servië, 2–2 uit bij Griekenland en 2–1 thuis tegen Servië.")
f.para("Drie dagen later, op maandag 16 november, speelt Oranje uit tegen Duitsland in Berlijn, ook om 20:45 uur. De spelers melden zich op maandag 9 november in Zeist. Daarna is er geen interland meer tot maart: dan zijn de kwartfinales.")
f.para("De Eredivisie ligt deze week stil: het is interlandperiode. Speelronde 13 is pas op 21 en 22 november, met zaterdag NEC tegen PSV en Feyenoord tegen Excelsior, en zondag Twente tegen Willem II en Ajax tegen ADO Den Haag. Vorige week, in speelronde 11, won PSV met 7–0 van Willem II en won Ajax met 1–0 van AZ.")
f.head("DE STAND IN GROEP 2", 25)
f.para("Nederland 8 punten, Griekenland 8, Duitsland 5, Servië 0. Twee landen gaan door. Vrijdag tegen Griekenland is dus bijna een finale — en maandag in Berlijn de tweede.")
f.gloss("de groepsfase : la phase de groupes · de kwartfinale : le quart de finale · ongeslagen : invaincu · de interland : le match international · de stand : le classement.")
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
p.text(MX, ey + 28, "OEFENINGEN　EXERCICES PAGE 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8　niveaux mélangés ; cherche ton numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Lis l'article page 4 et choisis la bonne réponse.")
e.ex("B1", "Choix unique", "B", "Pays-Bas–Grèce, vendredi 20 h 45, à Amsterdam",
     "Nederland – Griekenland is op... A. maandag 16 november · B. vrijdag 13 november · C. zaterdag 14 november", size=20, gap=8)
e.ex("B1", "Choix unique", "C", "Les Pays-Bas et la Grèce ont tous les deux 8 points",
     "Na vier wedstrijden hebben Nederland en Griekenland... A. 5 punten · B. 7 punten · C. 8 punten", size=20, gap=8)
e.ex("B1", "Choix unique", "A", "Les Pays-Bas ont marqué plus de buts dans le groupe : 7 contre 5",
     "Nederland staat eerste, omdat het... A. meer doelpunten maakte · B. meer wedstrijden speelde · C. thuis speelt", size=20, gap=8)
e.ex("B1", "Choix unique", "B", "Allemagne–Pays-Bas, lundi, à Berlin",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=20, gap=8)
e.ex("B1", "Choix unique", "B", "La 13e journée d'Eredivisie a lieu les 21–22 novembre",
     "Speelronde 13 is op... A. 13 en 14 november · B. 21 en 22 november · C. 9 en 10 november", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("Complète avec les mots de l'encadré. Attention aux formes verbales.")
e.para("groepsfase · kwartfinale · ongeslagen · interland · stand", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Compléter les phrases", "groepsfase", "groepsfase = phase de groupes",
     "Het is de vijfde wedstrijd in de ___.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "kwartfinales", "kwartfinale, pluriel : kwartfinales",
     "De nummers één en twee gaan naar de ___.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "ongeslagen", "ongeslagen = invaincu",
     "Oranje is nog ___ na vier wedstrijden.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "stand", "stand = classement",
     "Op de ___ staat Servië onderaan met 0 punten.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "interland", "interland = match international",
     "Na deze week is er geen ___ meer tot maart.", instr="Compléter", size=20, gap=8)
e.head("C　VERLEDEN TIJD", 25)
e.bridge("Complète au passé simple ou au parfait.")
e.ex("B1", "Compléter les phrases", "speelde", "spelen au passé : speelde",
     "Oranje ___ (spelen) 1–1 tegen Duitsland.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "won", "winnen au passé : won",
     "PSV ___ (winnen) met 7–0 van Willem II.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "maakte", "maken au passé : maakte",
     "Nederland ___ (maken) 7 doelpunten in vier wedstrijden.", instr="Compléter", size=20, gap=8)
e.ex("B2", "Compléter les phrases", "zijn gekomen", "komen au parfait prend zijn",
     "De spelers ___ (komen) maandag in Zeist bij elkaar.", instr="Compléter", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "Vrai ou faux", "Waar", "Vrai : Pays-Bas–Grèce, vendredi 20 h 45",
     "Nederland – Griekenland begint vrijdag om 20:45 uur. Waar of niet waar?", instr="Vrai ou faux", size=20, gap=8)
e.ex("B1", "Vrai ou faux", "Niet waar", "Faux : la Serbie est dernière avec 0 point",
     "Servië heeft 8 punten in groep 2. Waar of niet waar?", instr="Vrai ou faux", size=20, gap=8)
e.ex("B1", "Vrai ou faux", "Niet waar", "Faux : la 13e journée d'Eredivisie a lieu les 21–22 novembre",
     "Speelronde 13 is deze week. Waar of niet waar?", instr="Vrai ou faux", size=20, gap=8)
e.ex("B1", "Vrai ou faux", "Waar", "Vrai : le PSV a battu Willem II 7–0",
     "PSV won met 7–0 van Willem II. Waar of niet waar?", instr="Vrai ou faux", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
