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
f.ex("B1", "Lückentext", "B", "Im Herbst geht die Uhr zurück",
     "In de nacht van zaterdag op zondag gaat de klok één uur ___. (A. vooruit · B. achteruit)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Herbstferien in Midden und Zuid bis zum 25. Oktober",
     "De herfstvakantie van Midden en Zuid duurt tot en met zondag ___ oktober. (A. 25 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die Design Week ist in Eindhoven",
     "De Dutch Design Week is in ___. (A. Eindhoven · B. Amsterdam)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "PSV gewann auswärts in Porto",
     "PSV won in de Champions League bij ___. (A. Atalanta · B. FC Porto)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "ADE wird dieses Jahr 30",
     "ADE wordt dit jaar ___ jaar. (A. 25 · B. 30)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Robinson beginnt im November",
     "Expeditie Robinson begint op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "Die größte Uhr-Suche war «wintertijd»",
     "De grootste zoekterm over de klok was «___». (A. wintertijd · B. klok vooruit)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "half drie = 2:30",
     "«Half drie» is ___. (A. 03:30 · B. 02:30)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "wählen", "B", "Die Winterzeit beginnt um 03:00 Uhr nachts",
     "De wintertijd begint om... A. 02:00 uur · B. 03:00 uur · C. middernacht", size=13.8, gap=0)
f.ex("A2", "wählen", "A", "Region Noord hatte vom 10. bis 18. Oktober Ferien",
     "Welke regio had vakantie van 10 tot en met 18 oktober? A. Noord · B. Midden · C. Zuid", size=13.8, gap=0)
f.ex("A2", "wählen", "C", "Studententicket: € 19,50",
     "Een studentenkaartje voor de DDW kost... A. € 32,50 · B. € 25,00 · C. € 19,50", size=13.8, gap=0)
f.ex("B1", "wählen", "A", "Feyenoord spielt am Mittwoch in Sevilla",
     "Feyenoord speelt woensdag in... A. Sevilla · B. Porto · C. Eindhoven", size=13.8, gap=0)
f.ex("B1", "wählen", "B", "Sparta – Ajax beginnt um 16:45 Uhr",
     "Sparta – Ajax begint zondag om... A. 14:30 uur · B. 16:45 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("B1", "wählen", "B", "Die 19 Teilnehmer sind Niederländer und Flamen",
     "De 19 kandidaten van Expeditie Robinson zijn... A. allemaal dj's · B. Nederlanders en Vlamingen · C. alleen sporters", size=13.8, gap=0)
f.ex("B2", "wählen", "B", "Die 6.600 Suchen fragten nach »vooruit« (die falsche Richtung)",
     "De 6.600 zoekopdrachten vroegen naar... A. achteruit · B. vooruit · C. wintertijd", size=13.8, gap=0)
f.ex("B1", "wählen", "A", "Die Plattform zeigt künftig alle Zusatzkosten deutlich",
     "Thuisbezorgd laat voortaan... A. alle extra kosten duidelijk zien · B. geen eten meer bezorgen · C. alleen kortingsbonnen zien", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht, in de regio Midden. Zij heeft de hele week herfstvakantie. Op woensdag gaat zij met haar zus naar Eindhoven, naar de Dutch Design Week. Zaterdagavond zet zij alle klokken in huis één uur achteruit — behalve haar telefoon, die doet het zelf. Zondag slaapt zij lang uit: het is de laatste dag van de vakantie.", 15, lh=1.3, split=False)
f.ex("A2", "wählen", "B", "Sanne wohnt in Utrecht",
     "Waar woont Sanne? A. in Venlo · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "In ihrer Region sind Herbstferien",
     "Waarom heeft Sanne de hele week vrij? A. Zij is ziek · B. Het is herfstvakantie in haar regio · C. Zij werkt niet", size=13.8, gap=0)
f.ex("A2", "wählen", "B", "Sie stellt am Samstagabend die Uhren um",
     "Wat doet Sanne zaterdagavond? A. Zij gaat dansen · B. Zij zet de klokken achteruit · C. Zij pakt haar koffer", size=13.8, gap=0)
f.ex("B1", "wählen", "C", "Das Telefon stellt die Zeit selbst um — nicht von Hand",
     "Welke klok zet Sanne NIET met de hand achteruit? A. de ovenklok · B. de wekker · C. haar telefoon", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Sätze bilden", "De klok gaat één uur achteruit.", "Subjekt + Verb + Objekt + Richtung",
     "de klok / gaat / één uur / achteruit → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Wij gaan zondag naar de topper.", "Subjekt + Verb + Zeit + Ort",
     "wij / gaan / zondag / naar de topper → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "Hoe laat begint de wedstrijd?", "Die Frageformel steht am Anfang",
     "hoe laat / begint / de wedstrijd / ? → ___", instr="Sätze bilden", size=13.8, gap=0)
f.ex("B1", "Sätze bilden", "PSV won met 1–0 in Porto.", "Subjekt + Verb + Ergebnis + Ort",
     "psv / won / met 1–0 / in porto → ___", instr="Sätze bilden", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "übersetzen", "Am Sonntag geht die Uhr zurück: eine Stunde länger schlafen!", "Vergleiche das Spitzenband auf Seite 1",
     "Zondag gaat de klok terug: een uur langer slapen! → ___", instr="Übersetzen", size=13.8, gap=0)
f.ex("B1", "übersetzen", "Dein Telefon und dein Computer stellen die Zeit von selbst um.", "Originalsatz von Seite 2 · veranderen = ändern, umstellen",
     "Je telefoon en je computer veranderen de tijd zelf. → ___", instr="Übersetzen", size=13.8, gap=0)
f.ex("B1", "übersetzen", "De Dutch Design Week is in Eindhoven.", "Achte auf die Ortsangabe »in Eindhoven«",
     "Die Dutch Design Week ist in Eindhoven. → ___", instr="Übersetzen", size=13.8, gap=0)
f.ex("B2", "übersetzen", "Zondag heb ik een uur langer geslapen.", "Perfectum: heb geslapen",
     "Am Sonntag habe ich eine Stunde länger geschlafen. → ___", instr="Übersetzen", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "zuordnen",
            ["de klok verzetten", "het ezelsbruggetje", "eropuit gaan", "bijslapen"],
            ["extra slapen om uit te rusten",
             "het huis uit gaan voor iets leuks",
             "een hulpmiddel om iets te onthouden",
             "de tijd op een klok veranderen"],
            ["d", "c", "b", "a"],
            ["verzetten = die Uhr verstellen, d", "ezelsbruggetje = Merksatz, c", "eropuit = hinausgehen, b", "bijslapen = nachschlafen, a"],
            instr="Wörter zuordnen")
f.head("G　DIALOOG BIJ DE DDW", 21, OLIVE, 5)
f.ex("B1", "Lückentext", "B", "kaartje = Eintrittskarte, Ticket",
     "— Goedemorgen! Een ___ voor de Dutch Design Week, alstublieft. (A. ezelsbruggetje · B. kaartje)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "student = Student (Ticket € 19,50)",
     "— Natuurlijk. Bent u ___? Studenten betalen € 19,50. (A. student · B. ontwerper)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "tot hoe laat = bis wie viel Uhr geöffnet",
     "— Ja! Hier is mijn studentenkaart. En tot hoe ___ zijn jullie open? (A. lang · B. laat)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "A", "veel plezier = viel Spaß, viel Vergnügen",
     "— Tot 18:00 uur. Veel ___ met de ontwerpen! (A. plezier · B. slaap)", size=13.8, gap=0)
f.ex("B1", "Lückentext", "B", "tot ziens = auf Wiedersehen",
     "— Dank u wel, tot ___! (A. straks · B. ziens)", size=13.8, gap=0)
f.head("H　SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Zondag 25 oktober word ik laat wakker: het is de laatste dag van mijn herfstvakantie. "
          "Ik heb een uur langer geslapen, want vannacht ging de klok achteruit. "
          "Na het ontbijt ga ik met mijn vrienden naar het bos; de bladeren zijn geel en rood. "
          "'s Middags kijken wij thuis naar PSV tegen Feyenoord op televisie. "
          "Mijn zus gaat naar Amsterdam voor ADE, maar ik blijf liever thuis met een boek. "
          "'s Avonds pak ik mijn tas voor school: morgen begint het gewone leven weer. "
          "Wat een week!")
NWORDS = len(MODELO.split())
f.note_line(f"Schreibaufgabe (keine einzige richtige Antwort); der Mustertext ({NWORDS} Wörter) steht unten.")
f.ex("B1", "schreiben", "(Offene Aufgabe — Mustertext unten)", f"Mustertext in Abschnitt H auf dieser Seite ({NWORDS} Wörter)",
     "«Jouw zondag 25 oktober» Schrijf 80–100 woorden: wat doe jij op de laatste vakantiedag, hoe laat sta jij op, en wat doe jij 's middags?", instr="Schreiben", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　ANTWORTEN — nach Seiten geordnet, finde deine Nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Jede Nummer mit kurzer deutscher Erklärung　✓ = Mustertext", 19.5, "sans", False, GREY, anchor="end")
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
        af.para(txt, 13.0, lh=1.12, gap=0.4, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-toets.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
