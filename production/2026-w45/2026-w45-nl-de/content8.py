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
f.ex("B1", "Lückentext", "B", "Die Klimaatweek dauert bis zum 8. November",
     "De Klimaatweek duurt van 2 tot en met ___ november. (A. 7 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Coevorden verteilt 200 Bäume und Sträucher",
     "Coevorden deelt ___ bomen en struiken uit. (A. 100 · B. 200)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Die Museumsnacht ist am 7. November",
     "Museumnacht is op zaterdag ___ november. (A. 6 · B. 7)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Twente–Ajax beginnt um 13:30 Uhr",
     "Twente – Ajax begint om ___ uur. (A. 11:15 · B. 13:30)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Ajax gewann mit 2–0 gegen Atalanta",
     "Ajax won van Atalanta met ___. (A. 2–0 · B. 4–1)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Robinson startete im November",
     "Expeditie Robinson begon op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "Code Orange: das Wetter ist gefährlich",
     "Code oranje betekent: het weer is ___. (A. veilig · B. gevaarlijk)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "meedoen = teilnehmen",
     "«Meedoen» betekent ___. (A. weggaan · B. deelnemen)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "wählen", "A", "Die Klimaatweek beginnt am Montag, 2. November",
     "De Klimaatweek begint op... A. maandag 2 november · B. dinsdag 3 november · C. zaterdag 7 november", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "Der Verteilort ist Zweeloo",
     "De bomen in Coevorden worden uitgedeeld in... A. Amsterdam · B. Zweeloo · C. Rotterdam", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "Crossing Border ist in Den Haag",
     "Crossing Border is in... A. Amsterdam · B. Den Haag · C. Utrecht", size=13.8, gap=0)
f.ex("B1", "wählen", "A", "PAN ist in der RAI",
     "PAN Amsterdam is in... A. de RAI · B. het Rijksmuseum · C. de Jaarbeurs", size=13.8, gap=0)
f.ex("B1", "wählen", "B", "Real Betis gewann mit 1–0 gegen Feyenoord",
     "Real Betis – Feyenoord eindigde... A. 0–0 · B. 1–0 · C. 0–1", size=13.8, gap=0)
f.ex("B1", "wählen", "B", "Nach 10 Runden hat Ajax 21 Punkte",
     "Na 10 ronden heeft Ajax ___ punten. A. 24 · B. 21 · C. 20", size=13.8, gap=0)
f.ex("B2", "wählen", "B", "Warnmüdigkeit: zu viele Warnungen, man passt nicht mehr auf",
     "Waarschuwingsmoeheid betekent... A. moe van het weer · B. minder opletten door te veel waarschuwingen · C. een nieuwe code", size=13.8, gap=0)
f.ex("B1", "wählen", "C", "Der Flohmarkt in Zaandam hat etwa 250 Stände",
     "De Snuffelmarkt in Zaandam heeft zo'n ___ kramen. A. 70 · B. 200 · C. 250", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Coevorden. Op zaterdag 7 november gaat hij naar de Fair Groen in Zweeloo en haalt hij een gratis struik op. 's Avonds kijkt hij naar de foto's van Museumnacht in Amsterdam — zelf gaat hij niet, want zondag speelt zijn club Twente tegen Ajax om 13:30 uur. En in de Klimaatweek fietst Daan elke dag naar school, ook als het regent.", 15, lh=1.3, split=False)
f.ex("A2", "wählen", "B", "Daan wohnt in Coevorden",
     "Waar woont Daan? A. in Zweeloo · B. in Coevorden · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "Am Samstag holt er einen kostenlosen Strauch ab",
     "Wat haalt Daan op zaterdag op? A. een fiets · B. een gratis struik · C. een kaartje", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "Am Sonntag spielt Twente gegen Ajax",
     "Waarom gaat Daan zaterdagavond niet naar Amsterdam? A. Hij heeft geen kaartje · B. Zondag speelt Twente tegen Ajax · C. Hij houdt niet van musea", size=13.8, gap=0)
f.ex("B1", "wählen", "B", "In der Klimaatweek fährt er jeden Tag mit dem Rad zur Schule",
     "Wat doet Daan in de Klimaatweek? A. Hij rijdt elke dag met de auto · B. Hij fietst elke dag naar school · C. Hij blijft thuis", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Sätze bilden", "De Klimaatweek begint op maandag.", "Subjekt + Verb + Zeit",
     "de klimaatweek / begint / op maandag → ___", instr="Bilde den Satz", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Wij planten een boom in de tuin.", "Subjekt + Verb + Objekt + Ort",
     "wij / planten / een boom / in de tuin → ___", instr="Bilde den Satz", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Twente speelt zondag tegen Ajax.", "Subjekt + Verb + Zeit + Gegner",
     "twente / speelt / zondag / tegen ajax → ___", instr="Bilde den Satz", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Ik doe mee aan de Klimaatweek.", "Trennbares Verb: mee steht am Ende",
     "ik / doe / mee / aan de klimaatweek → ___", instr="Bilde den Satz", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "übersetzen", "Die Klimaatweek dauert sieben Tage.", "Vergleiche die Schlagzeile auf Seite 1",
     "De Klimaatweek duurt zeven dagen. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "übersetzen", "Code Orange bedeutet: Bereite dich vor.", "Originalsatz von Seite 2 · bereid je voor = bereite dich vor",
     "Code oranje betekent: bereid je voor. → ___", instr="Ins Deutsche übersetzen", size=13.8, gap=0)
f.ex("B1", "übersetzen", "Museumnacht duurt van 19:00 uur tot 02:00 uur.", "Beachte die Zeitangabe van...tot...",
     "Die Museumsnacht dauert von 19:00 Uhr bis 02:00 Uhr. → ___", instr="Ins Niederländische übersetzen", size=13.8, gap=0)
f.ex("B2", "übersetzen", "Ik doe mee aan de Klimaatweek.", "meedoen ist ein trennbares Verb",
     "Ich mache bei der Klimaatweek mit. → ___", instr="Ins Niederländische übersetzen", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "zuordnen",
            ["het klimaat", "meedoen", "de waarschuwing", "vastzetten"],
            ["een bericht over gevaarlijk weer",
             "deelnemen, erbij zijn",
             "het weer en de natuur over een lange tijd",
             "losse spullen stevig maken"],
            ["c", "b", "a", "d"],
            ["klimaat = Klima c", "meedoen = teilnehmen b", "waarschuwing = Warnung a", "vastzetten = befestigen d"],
            instr="Wort und Bedeutung")
f.head("G　DIALOOG BIJ DE BOMEN", 21, OLIVE, 5)
f.ex("B1", "Lückentext", "A", "boom = Baum",
     "— Goedemiddag! Ik kom voor een ___. (A. boom · B. fiets)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "struik = Strauch",
     "— Natuurlijk. Wilt u een boom of een ___? (A. struik · B. auto)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "planten = pflanzen",
     "— Een struik, graag. En waar moet ik hem ___? (A. planten · B. kopen)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "zachte = weich (Boden)",
     "— In de tuin, in de ___ grond. (A. harde · B. zachte)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die Verteilung endet um 16:00 Uhr",
     "— De uitdeling duurt tot ___ uur. (A. 16:00 · B. 20:00)", size=13.8, gap=0)
f.head("H　SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Maandag 2 november begint de Klimaatweek in Nederland. "
          "Ik doe mee: ik fiets elke dag naar school en ik zet de verwarming één graad lager. "
          "Op zaterdag 7 november ga ik met mijn vader naar Coevorden, want daar deelt de gemeente gratis bomen uit. "
          "Wij nemen een struik mee voor onze tuin. "
          "'s Avonds kijken wij op televisie naar de foto's van Museumnacht in Amsterdam. "
          "Zondag kijken wij naar Twente tegen Ajax. "
          "Mijn zus plant ook een boom op haar balkon. "
          "Wat een week voor het klimaat!")
NWORDS = len(MODELO.split())
f.bridge(f"Schreibaufgabe (keine einzige richtige Antwort); Mustertext ({NWORDS} Wörter) unten.")
f.ex("B1", "schreiben", "(offene Aufgabe, Mustertext unten)", f"Mustertext in Abschnitt H auf dieser Seite ({NWORDS} Wörter)",
     "«Jouw week in de Klimaatweek» Schrijf 80–100 woorden: wat doe jij in de Klimaatweek, plant jij iets, fiets jij, en kijk jij naar Museumnacht of voetbal?", instr="Schreiben", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　ANTWORTEN — nach Seiten geordnet, finde deine Nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Jede Antwort hat eine kurze Erklärung auf Deutsch　✓ markiert die Schreibaufgabe", 19.5, "sans", False, GREY, anchor="end")
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
