# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTUUR (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTUUR　KULTUR", "De Lucerna", "NIVEAU A2 → B1　Sinterklaasjournaal en Het diner　Sinterklaasjournaal und Het diner")

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
f.gloss("het journaal = Nachrichtensendung · de flessenpost = Flaschenpost · de burgemeester = Bürgermeister · de stoet = Festzug · de leeskring = Lesekreis.")
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
p.text(MX, ey + 28, "OEFENINGEN　ÜBUNGEN AUF SEITE 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8　Niveaus gemischt; Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Lies den Artikel auf Seite 3 und wähle die richtige Antwort.")
e.ex("A2", "wählen", "B", "Das Sinterklaasjournaal läuft jeden Tag um 18:00 Uhr",
     "Het Sinterklaasjournaal is elke dag om... A. 12:00 uur · B. 18:00 uur · C. 20:45 uur", size=20, gap=8)
e.ex("A2", "wählen", "B", "Der landesweite Einzug ist in Grave",
     "De landelijke intocht is in... A. Amsterdam · B. Grave · C. Utrecht", size=20, gap=8)
e.ex("A2", "wählen", "C", "Das Amsterdamer Boot legt um 10:15 Uhr in De Omval ab",
     "De boot in Amsterdam vertrekt om... A. 12:00 uur · B. 13:00 uur · C. 10:15 uur", size=20, gap=8)
e.ex("A2", "wählen", "A", "Het diner wurde von Herman Koch geschrieben",
     "Heel Nederland Leest leest dit jaar... A. Het diner van Herman Koch · B. een boek van Merel Westrik · C. een boek over Grave", size=20, gap=8)
e.ex("A2", "wählen", "B", "Het diner gibt es gratis in der Bibliothek",
     "Het diner is gratis af te halen in... A. de boekwinkel · B. de bibliotheek · C. het museum", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("Ergänze mit den Wörtern aus dem Kasten.")
e.para("journaal · burgemeester · stoet · leeskring · flessenpost", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "ergänzen", "journaal", "journaal = Nachrichtensendung",
     "Het Sinterklaas___ begint op 9 november.", instr="Einsetzen", size=20, gap=8)
e.ex("A2", "ergänzen", "burgemeester", "burgemeester = Bürgermeister",
     "De ___ ontvangt Sinterklaas in Grave.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "stoet", "stoet = Festzug",
     "Om 13:00 uur begint de ___ te paard.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "flessenpost", "flessenpost = Flaschenpost",
     "De ___ leidde naar Grave.", instr="Einsetzen", size=20, gap=8)
e.ex("A2", "ergänzen", "leeskring", "leeskring = Lesekreis",
     "In de bibliotheek is er een ___ over Het diner.", instr="Einsetzen", size=20, gap=8)
e.head("C　HET PERFECTUM", 25)
e.bridge("Ergänze im Perfekt. Achte auf die Hilfsverben hebben/zijn.")
e.ex("B1", "ergänzen", "is begonnen", "beginnen mit zijn: is begonnen",
     "Het Sinterklaasjournaal ___ (beginnen) op 9 november.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "heeft gevonden", "vinden im Perfekt: heeft gevonden",
     "Iemand ___ (vinden) de flessenpost.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "is aangekomen", "aankomen mit zijn: is aangekomen",
     "Sinterklaas ___ (aankomen) in Grave.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "hebben gelezen", "lezen im Perfekt: hebben gelezen",
     "Veel mensen ___ (lezen) Het diner in november.", instr="Einsetzen", size=20, gap=8)
e.head("D　REKENEN", 25)
e.bridge("Rechne: Antworte mit den Zahlen von Seite 3.")
e.ex("B1", "ergänzen", "5", "Vom 9. bis 14. November sind es 5 Tage",
     "Van 9 tot 14 november: ___ dagen.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "6", "Vom 9. bis 15. November sind es 6 Tage",
     "Van 9 tot 15 november: ___ dagen.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "4", "Das Programm in Grave, 12:00–16:00 Uhr, dauert 4 Stunden",
     "Het programma in Grave duurt van 12:00 tot 16:00 uur: ___ uur.", instr="Einsetzen", size=20, gap=8)
e.ex("B2", "ergänzen", "17", "Het diner ist von 2009: 17 Jahre her im Jahr 2026",
     "Het diner is uit 2009; in 2026 is dat ___ jaar geleden.", instr="Einsetzen", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultuur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT", "De Lucerna", "NIVEAU B1　Oranje en de Nations League　Oranje und die Nations League")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P4-feature")
f.title("Oranje: twee wedstrijden, één doel", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Op vrijdag 13 november speelt Oranje thuis tegen Griekenland. De wedstrijd begint om 20:45 uur in de Johan Cruijff ArenA in Amsterdam. Het is de vijfde wedstrijd in de groepsfase van de Nations League — en een beslissende: de nummers één en twee van de groep gaan naar de kwartfinales in maart 2027.")
f.para("Na vier wedstrijden staan Nederland en Griekenland samen bovenaan met 8 punten. Duitsland heeft 5 punten, Servië heeft 0 punten. Nederland staat eerste, omdat het meer doelpunten maakte: 7 tegen 5. Oranje is nog ongeslagen: 1–1 thuis tegen Duitsland, 2–1 uit bij Servië, 2–2 uit bij Griekenland en 2–1 thuis tegen Servië.")
f.para("Drie dagen later, op maandag 16 november, speelt Oranje uit tegen Duitsland in Berlijn, ook om 20:45 uur. De spelers melden zich op maandag 9 november in Zeist. Daarna is er geen interland meer tot maart: dan zijn de kwartfinales.")
f.para("De Eredivisie ligt deze week stil: het is interlandperiode. Speelronde 13 is pas op 21 en 22 november, met zaterdag NEC tegen PSV en Feyenoord tegen Excelsior, en zondag Twente tegen Willem II en Ajax tegen ADO Den Haag. Vorige week, in speelronde 11, won PSV met 7–0 van Willem II en won Ajax met 1–0 van AZ.")
f.head("DE STAND IN GROEP 2", 25)
f.para("Nederland 8 punten, Griekenland 8, Duitsland 5, Servië 0. Twee landen gaan door. Vrijdag tegen Griekenland is dus bijna een finale — en maandag in Berlijn de tweede.")
f.gloss("de groepsfase = Gruppenphase · de kwartfinale = Viertelfinale · ongeslagen = ungeschlagen · de interland = Länderspiel · de stand = Tabelle.")
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
p.text(MX, ey + 28, "OEFENINGEN　ÜBUNGEN AUF SEITE 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8　Niveaus gemischt; Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Lies den Artikel auf Seite 4 und wähle die richtige Antwort.")
e.ex("B1", "wählen", "B", "Niederlande–Griechenland, Freitag 20:45 Uhr, in Amsterdam",
     "Nederland – Griekenland is op... A. maandag 16 november · B. vrijdag 13 november · C. zaterdag 14 november", size=20, gap=8)
e.ex("B1", "wählen", "C", "Die Niederlande und Griechenland haben beide 8 Punkte",
     "Na vier wedstrijden hebben Nederland en Griekenland... A. 5 punten · B. 7 punten · C. 8 punten", size=20, gap=8)
e.ex("B1", "wählen", "A", "Die Niederlande schossen in der Gruppe mehr Tore: 7 zu 5",
     "Nederland staat eerste, omdat het... A. meer doelpunten maakte · B. meer wedstrijden speelde · C. thuis speelt", size=20, gap=8)
e.ex("B1", "wählen", "B", "Deutschland–Niederlande, Montag, in Berlin",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=20, gap=8)
e.ex("B1", "wählen", "B", "Eredivisie-Spieltag 13 ist am 21.–22. November",
     "Speelronde 13 is op... A. 13 en 14 november · B. 21 en 22 november · C. 9 en 10 november", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("Ergänze mit den Wörtern aus dem Kasten. Achte auf die Verbformen.")
e.para("groepsfase · kwartfinale · ongeslagen · interland · stand", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "ergänzen", "groepsfase", "groepsfase = Gruppenphase",
     "Het is de vijfde wedstrijd in de ___.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "kwartfinales", "kwartfinale, Plural: kwartfinales",
     "De nummers één en twee gaan naar de ___.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "ongeslagen", "ongeslagen = ungeschlagen",
     "Oranje is nog ___ na vier wedstrijden.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "stand", "stand = Tabelle",
     "Op de ___ staat Servië onderaan met 0 punten.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "interland", "interland = Länderspiel",
     "Na deze week is er geen ___ meer tot maart.", instr="Einsetzen", size=20, gap=8)
e.head("C　VERLEDEN TIJD", 25)
e.bridge("Ergänze im Präteritum oder Perfekt.")
e.ex("B1", "ergänzen", "speelde", "spelen im Präteritum: speelde",
     "Oranje ___ (spelen) 1–1 tegen Duitsland.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "won", "winnen im Präteritum: won",
     "PSV ___ (winnen) met 7–0 van Willem II.", instr="Einsetzen", size=20, gap=8)
e.ex("B1", "ergänzen", "maakte", "maken im Präteritum: maakte",
     "Nederland ___ (maken) 7 doelpunten in vier wedstrijden.", instr="Einsetzen", size=20, gap=8)
e.ex("B2", "ergänzen", "zijn gekomen", "komen im Perfekt mit zijn",
     "De spelers ___ (komen) maandag in Zeist bij elkaar.", instr="Einsetzen", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "richtig/falsch", "Waar", "Richtig: Niederlande–Griechenland, Freitag 20:45 Uhr",
     "Nederland – Griekenland begint vrijdag om 20:45 uur. Waar of niet waar?", instr="Richtig oder falsch?", size=20, gap=8)
e.ex("B1", "richtig/falsch", "Niet waar", "Falsch: Serbien ist Letzter mit 0 Punkten",
     "Servië heeft 8 punten in groep 2. Waar of niet waar?", instr="Richtig oder falsch?", size=20, gap=8)
e.ex("B1", "richtig/falsch", "Niet waar", "Falsch: Eredivisie-Spieltag 13 ist am 21.–22. November",
     "Speelronde 13 is deze week. Waar of niet waar?", instr="Richtig oder falsch?", size=20, gap=8)
e.ex("B1", "richtig/falsch", "Waar", "Richtig: PSV schlug Willem II mit 7–0",
     "PSV won met 7–0 van Willem II. Waar of niet waar?", instr="Richtig oder falsch?", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
