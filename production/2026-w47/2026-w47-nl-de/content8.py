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
f.ex("B1", "Lückentext", "B", "Deutschland–Niederlande, Montag, in Berlin",
     "Duitsland – Nederland is op maandag in ___. (A. Amsterdam · B. Berlijn)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Die Niederlande und Griechenland haben beide 8 Punkte",
     "Nederland en Griekenland hebben allebei ___ punten. (A. 5 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die Niederlande schossen 7 Tore",
     "Nederland maakte ___ doelpunten in vier wedstrijden. (A. 7 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Pakjesavond ist im Dezember",
     "Pakjesavond is op ___ december. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Die Sinterklaas-Nachrichten um 18:00 Uhr",
     "Het Sinterklaasjournaal is elke dag om ___ uur. (A. 12:00 · B. 18:00)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Robinson läuft auf RTL 4",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "In einer surprise steckt ein Gedicht",
     "Bij een surprise hoort een ___. (A. liedje · B. gedicht)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "groepswinst = Gruppensieg",
     "«De groepswinst» betekent ___. (A. de laatste plaats · B. de eerste plaats in de groep)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "wählen", "A", "Das Sinterklaasjournaal läuft jeden Tag um 18:00 Uhr",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "Grave liegt an der Maas",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "Der Einzug in Amsterdam ist die 88. Ausgabe",
     "De intocht in Amsterdam was de... A. 26e editie · B. 88e editie · C. 30e editie", size=13.8, gap=0)
f.ex("B1", "wählen", "A", "Het diner erschien 2009",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "wählen", "B", "Deutschland verlor zu Hause mit 0–1 gegen Griechenland",
     "Duitsland verloor thuis met 0–1 van... A. Servië · B. Griekenland · C. Nederland", size=13.8, gap=0)
f.ex("B1", "wählen", "B", "PSV führt die Eredivisie mit 26 Punkten an",
     "PSV staat bovenaan in de Eredivisie met ___ punten. A. 25 · B. 26 · C. 8", size=13.8, gap=0)
f.ex("B2", "wählen", "B", "Eine Tradition lebt, wenn Menschen sie weiter feiern",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "wählen", "C", "Eredivisie-Spieltag 13 ist am 21.–22. November",
     "Speelronde 13 is op... A. 13 en 14 november · B. 16 november · C. 21 en 22 november", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Rotterdam. Op maandag 16 november kijkt hij om 20:45 uur naar Duitsland – Nederland in Berlijn. Elke dag kijkt hij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag 21 november kijkt hij naar NEC – PSV. Zondag zet hij zijn schoen met een wortel en een verlanglijstje. Op zondagavond kijkt hij ook naar Expeditie Robinson.", 15, lh=1.3, split=False)
f.ex("A2", "wählen", "B", "Daan wohnt in Rotterdam",
     "Waar woont Daan? A. in Grave · B. in Rotterdam · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "Am Montag schaut er Deutschland–Niederlande",
     "Wat doet Daan op maandag 16 november? A. Hij kijkt naar Robinson · B. Hij kijkt naar Duitsland – Nederland · C. Hij leest Het diner", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "Karotte und Wunschzettel in den Schuh",
     "Wat zit er in de schoen van Daan? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "wählen", "B", "Er schaut jeden Tag um 18:00 Uhr das Sinterklaasjournaal",
     "Wanneer kijkt Daan naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Sätze bilden", "Het Sinterklaasjournaal begint om 18:00 uur.", "Subjekt + Verb + Zeit",
     "het sinterklaasjournaal / begint / om 18:00 uur → ___", instr="Bilde den Satz", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Wij zetten onze schoen bij de deur.", "Subjekt + Verb + Objekt + Ort",
     "wij / zetten / onze schoen / bij de deur → ___", instr="Bilde den Satz", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Oranje speelt maandag in Berlijn.", "Subjekt + Verb + Zeit + Ort",
     "oranje / speelt / maandag / in berlijn → ___", instr="Bilde den Satz", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Ik zet mijn schoen met een wortel.", "Subjekt + Verb + Objekt + Art und Weise",
     "ik / zet / mijn schoen / met een wortel → ___", instr="Bilde den Satz", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "übersetzen", "Das Sinterklaasjournaal läuft jeden Tag um 18:00 Uhr.", "Mit dem Artikel auf Seite 3 vergleichen",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "übersetzen", "Die ersten beiden ziehen ins Viertelfinale ein.", "Originalsatz von Seite 4 · kwartfinale = Viertelfinale",
     "De nummers één en twee gaan naar de kwartfinales. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "übersetzen", "De intocht in Amsterdam was de 88e editie.", "Auf die Ordnungszahl 88e achten",
     "Der Einzug in Amsterdam ist die 88. Ausgabe. → ___", instr="Ins Niederländische übersetzen", size=13.8, gap=0)
f.ex("B2", "übersetzen", "Ik maak een surprise met een kort gedicht.", "surprise ist eine feste Wendung",
     "Ich mache eine Surprise mit einem kurzen Gedicht. → ___", instr="Ins Niederländische übersetzen", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "zuordnen",
            ["het journaal", "de groepswinst", "de schoen", "het gedicht"],
            ["een klein versje bij een cadeau",
             "een dagelijks nieuwsprogramma op televisie",
             "de eerste plaats in de groep",
             "die staat 's avonds bij de deur"],
            ["b", "c", "d", "a"],
            ["journaal = Nachrichtensendung b", "groepswinst=Gruppensieg c", "schoen = Schuh d", "gedicht=Gedicht a"],
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
MODELO = ("Maandag 16 november speelt Oranje in Berlijn tegen Duitsland. "
          "Ik kijk om 20:45 uur naar NPO 3. "
          "Elke dag kijk ik om 18:00 uur naar het Sinterklaasjournaal. "
          "Op woensdag schrijf ik een gedicht voor mijn surprise. "
          "Zaterdag kijk ik naar NEC – PSV. "
          "Zondag zet ik mijn schoen met een wortel en een verlanglijstje. "
          "Zondagavond kijk ik naar Expeditie Robinson. "
          "Daarna is het bijna pakjesavond, op zaterdag 5 december. "
          "Ik hoop op een boek. "
          "Wat een week vol voetbal en licht!")
NWORDS = len(MODELO.split())
f.bridge(f"Schreibaufgabe (keine eindeutige Antwort); Mustertext ({NWORDS} Wörter) unten.")
f.ex("B1", "schreiben", "(offene Aufgabe, Mustertext unten)", f"Mustertext in Abschnitt H ({NWORDS} Wörter)",
     "«Mijn week met Oranje en Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, kijk jij naar Duitsland – Nederland, en zet jij je schoen?", instr="Schreiben", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()
print("P8-ex flow ended col", f.ci, "y", round(f.y, 1), "(bottom 1252)")

# ---- P8 photo (W47: every page carries a public-domain image) ----
# Placed in the final exercise column, below the flow, only if it fits
# above the answers rule at y=1264 (image + caption must end by 1252).
if f.ci == 3 and f.y + 16 + 200 + 78 <= 1252:
    _px = COLX[f.ci]
    _py = f.y + 16
    image(p, "pen.jpg", _px, _py, CW, 200)
    _cy = caption(p, _px, _py + 200, CW, "Een vulpen op een schrift. Schrijf je opstel eerst met de hand — dan in het net.",
                  "Foto: Aaron Burden / Unsplash — CC0")
    print("P8 photo placed at", _px, _py, "ends", _cy)
else:
    print("!! P8 photo NOT placed: flow ended col", f.ci, "y", round(f.y, 1))

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　LÖSUNGEN — nach Seiten geordnet: sucht eure Nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Jede Antwort hat eine kurze Erklärung auf Deutsch　✓ markiert die Schreibaufgabe", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "schreiben":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-toets.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
