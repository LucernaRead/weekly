# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN　TEST UND ANTWORTEN", "De Lucerna", "Seite 8　De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "Lückentext", "B", "Das Sinterklaasjournaal beginnt am 9. November",
     "Het Sinterklaasjournaal begint op 9 ___. (A. oktober · B. november)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Der landesweite Einzug ist in Grave",
     "De landelijke intocht is in ___. (A. Amsterdam · B. Grave)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Der Einzug in Amsterdam ist die 88. Ausgabe",
     "De intocht in Amsterdam is de ___ editie. (A. 26e · B. 88e)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Niederlande–Griechenland, Anstoß 20:45 Uhr",
     "Oranje – Griekenland begint om ___ uur. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Martinstag ist am 11. November",
     "Sint-Maarten is op 11 ___. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Robinson läuft auf RTL 4",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Martinstag ist das Fest des Teilens",
     "Sint-Maarten is het feest van het ___. (A. griezelen · B. delen)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "schoen zetten = den Schuh hinstellen",
     "«De schoen zetten» betekent ___. (A. schoenen kopen · B. je schoen neerzetten)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "wählen", "A", "Das Sinterklaasjournaal läuft jeden Tag um 18:00 Uhr",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "Grave liegt an der Maas",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "Sinterklaas erhält den Stadtschlüssel am Schifffahrtsmuseum",
     "In Amsterdam krijgt Sinterklaas de sleutel bij... A. de Stopera · B. het Scheepvaartmuseum · C. het Leidseplein", size=13.8, gap=0)
f.ex("B1", "wählen", "A", "Het diner erschien 2009",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "wählen", "B", "Die Niederlande und Griechenland haben beide 8 Punkte",
     "Na vier wedstrijden hebben Nederland en Griekenland ___ punten. A. 5 · B. 8 · C. 0", size=13.8, gap=0)
f.ex("B1", "wählen", "B", "Deutschland–Niederlande, Montag, in Berlin",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=13.8, gap=0)
f.ex("B2", "wählen", "B", "Eine Tradition lebt, wenn Menschen sie weiter feiern",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "wählen", "C", "Pakjesavond ist am Samstag, 5. Dezember",
     "Pakjesavond is op... A. 11 november · B. 14 november · C. 5 december", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht. Op woensdag 11 november loopt zij met een lampion mee in de Sint Maarten Parade en zingt zij bij elke deur. Elke dag kijkt zij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag kijkt zij op televisie naar de intocht in Grave. Zondag zet zij haar schoen met een wortel en een verlanglijstje. Vrijdag kijkt zij naar Oranje tegen Griekenland.", 15, lh=1.3, split=False)
f.ex("A2", "wählen", "B", "Sanne lebt in Utrecht",
     "Waar woont Sanne? A. in Grave · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "Am Mittwoch geht sie beim Martinsumzug mit",
     "Wat doet Sanne op woensdag 11 november? A. Ze kijkt naar Oranje · B. Ze loopt mee in de Sint Maarten Parade · C. Ze leest Het diner", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "Sie legt eine Karotte und einen Wunschzettel in ihren Schuh",
     "Wat zit er in de schoen van Sanne? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "wählen", "B", "Sie schaut jeden Tag um 18:00 Uhr das Sinterklaasjournaal",
     "Wanneer kijkt Sanne naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Sätze bilden", "Het Sinterklaasjournaal begint op maandag.", "Subjekt + Verb + Zeit",
     "het sinterklaasjournaal / begint / op maandag → ___", instr="Bilde den Satz", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Wij zetten onze schoen bij de deur.", "Subjekt + Verb + Objekt + Ort",
     "wij / zetten / onze schoen / bij de deur → ___", instr="Bilde den Satz", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Oranje speelt vrijdag tegen Griekenland.", "Subjekt + Verb + Zeit + Gegner",
     "oranje / speelt / vrijdag / tegen griekenland → ___", instr="Bilde den Satz", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Ik loop met een lampion langs de deuren.", "Subjekt + Verb + Art und Weise + Ort",
     "ik / loop / met een lampion / langs de deuren → ___", instr="Bilde den Satz", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "übersetzen", "Das Sinterklaasjournaal läuft jeden Tag um 18:00 Uhr.", "Mit dem Artikel auf Seite 3 vergleichen",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "übersetzen", "Martinstag ist das Fest des Teilens.", "Originalsatz von Seite 2 · delen = teilen",
     "Sint-Maarten is het feest van het delen. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "übersetzen", "De intocht in Amsterdam is de 88e editie.", "Auf die Ordnungszahl 88e achten",
     "Der Einzug in Amsterdam ist die 88. Ausgabe. → ___", instr="Ins Niederländische übersetzen", size=13.8, gap=0)
f.ex("B2", "übersetzen", "Ik zet mijn schoen met een verlanglijstje.", "schoen zetten ist eine feste Wendung",
     "Ich stelle meinen Schuh hin, mit einem Wunschzettel darin. → ___", instr="Ins Niederländische übersetzen", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "zuordnen",
            ["het journaal", "de intocht", "de lampion", "delen"],
            ["een papieren lichtje voor 11 november",
             "een dagelijks nieuwsprogramma op televisie",
             "licht en eten geven aan anderen",
             "de feestelijke aankomst van Sinterklaas"],
            ["b", "d", "a", "c"],
            ["journaal = Nachrichtensendung b", "intocht = festlicher Einzug d", "lampion = Laterne a", "delen = teilen c"],
            instr="Wort und Bedeutung")
f.head("G　DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
f.ex("B1", "Lückentext", "A", "schoen = Schuh",
     "— Mama, waar moet mijn ___? (A. schoen · B. boek)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "wortel = Karotte für das Pferd",
     "— Bij de deur, met een ___ voor het paard. (A. wortel · B. lampion)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "verlanglijstje = Wunschzettel",
     "— En mijn ___ erin? (A. verlanglijstje · B. journaal)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "cadeautje = kleines Geschenk",
     "— Ja. Sinterklaas brengt 's nachts een ___. (A. mantel · B. cadeautje)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "18:00 = Sinterklaasjournaal-Zeit",
     "— Eerst kijken we om ___ uur naar het Sinterklaasjournaal. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.head("H　SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Maandag 9 november begint het Sinterklaasjournaal. "
          "Ik kijk elke dag om 18:00 uur naar NPO Zapp. "
          "Op woensdag 11 november loop ik met een lampion langs de deuren en zing ik een liedje. "
          "Vrijdag kijk ik naar Oranje tegen Griekenland. "
          "Zaterdag kijk ik naar de intocht in Grave op televisie. "
          "Zondag vaart Sinterklaas in Amsterdam. "
          "Daarna zet ik mijn schoen met een wortel en een verlanglijstje. "
          "Ik hoop op een boek. "
          "Maandag 16 november speelt Oranje in Berlijn tegen Duitsland. "
          "Ik kijk ook dan. "
          "Wat een week vol licht!")
NWORDS = len(MODELO.split())
f.bridge(f"Schreibaufgabe (keine eindeutige Antwort); Mustertext ({NWORDS} Wörter) unten.")
f.ex("B1", "schreiben", "(offene Aufgabe, Mustertext unten)", f"Mustertext in Abschnitt H ({NWORDS} Wörter)",
     "«Mijn week met Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, loop jij met een lampion, kijk jij naar het Sinterklaasjournaal, en zet jij je schoen?", instr="Schreiben", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　LÖSUNGSSCHLÜSSEL — nach Seiten geordnet: Nummer suchen", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Jede Antwort mit kurzer Notiz auf Deutsch　✓ markiert die Schreibaufgabe", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 13.5, "sans", True, OLIVE, lh=1.17, gap=1.5, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "schreiben":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.0, lh=1.14, gap=0.3, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-toets.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
