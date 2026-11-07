# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-nl-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · TEST AND ANSWERS", "De Lucerna", "Page 8 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "cloze choice", "B", "The Sinterklaas news starts on 9 November",
     "Het Sinterklaasjournaal begint op 9 ___. (A. oktober · B. november)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "The national arrival is in Grave",
     "De landelijke intocht is in ___. (A. Amsterdam · B. Grave)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "The Amsterdam arrival is the 88th edition",
     "De intocht in Amsterdam is de ___ editie. (A. 26e · B. 88e)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "Netherlands–Greece kicks off at 20:45",
     "Oranje – Griekenland begint om ___ uur. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "St Martin's Day is on 11 November",
     "Sint-Maarten is op 11 ___. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "Robinson is on RTL 4",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "St Martin's Day is the festival of sharing",
     "Sint-Maarten is het feest van het ___. (A. griezelen · B. delen)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "schoen zetten = to put out your shoe",
     "«De schoen zetten» betekent ___. (A. schoenen kopen · B. je schoen neerzetten)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "choice", "A", "The Sinterklaas news is on every day at 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "choice", "B", "Grave lies on the river Maas",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "choice", "B", "Sinterklaas receives the key to the city at the Maritime Museum",
     "In Amsterdam krijgt Sinterklaas de sleutel bij... A. de Stopera · B. het Scheepvaartmuseum · C. het Leidseplein", size=13.8, gap=0)
f.ex("B1", "choice", "A", "Het diner was published in 2009",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "choice", "B", "The Netherlands and Greece both have 8 points",
     "Na vier wedstrijden hebben Nederland en Griekenland ___ punten. A. 5 · B. 8 · C. 0", size=13.8, gap=0)
f.ex("B1", "choice", "B", "Germany–Netherlands, Monday, in Berlin",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=13.8, gap=0)
f.ex("B2", "choice", "B", "A tradition lives on when people keep celebrating it",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "choice", "C", "Pakjesavond is on Saturday 5 December",
     "Pakjesavond is op... A. 11 november · B. 14 november · C. 5 december", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht. Op woensdag 11 november loopt zij met een lampion mee in de Sint Maarten Parade en zingt zij bij elke deur. Elke dag kijkt zij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag kijkt zij op televisie naar de intocht in Grave. Zondag zet zij haar schoen met een wortel en een verlanglijstje. Vrijdag kijkt zij naar Oranje tegen Griekenland.", 15, lh=1.3, split=False)
f.ex("A2", "choice", "B", "Sanne lives in Utrecht",
     "Waar woont Sanne? A. in Grave · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "choice", "B", "On Wednesday she joins the St Martin's parade",
     "Wat doet Sanne op woensdag 11 november? A. Ze kijkt naar Oranje · B. Ze loopt mee in de Sint Maarten Parade · C. Ze leest Het diner", size=13.8, gap=0)
f.ex("A2", "choice", "B", "She puts a carrot and a wish list in her shoe",
     "Wat zit er in de schoen van Sanne? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "choice", "B", "She watches the Sinterklaas news every day at 18:00",
     "Wanneer kijkt Sanne naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "make sentences", "Het Sinterklaasjournaal begint op maandag.", "Subject + verb + time",
     "het sinterklaasjournaal / begint / op maandag → ___", instr="Make the sentence", size=13.8, gap=0)
f.ex("B1", "make sentences", "Wij zetten onze schoen bij de deur.", "Subject + verb + object + place",
     "wij / zetten / onze schoen / bij de deur → ___", instr="Make the sentence", size=13.8, gap=0)
f.ex("B1", "make sentences", "Oranje speelt vrijdag tegen Griekenland.", "Subject + verb + time + opponent",
     "oranje / speelt / vrijdag / tegen griekenland → ___", instr="Make the sentence", size=13.8, gap=0)
f.ex("B1", "make sentences", "Ik loop met een lampion langs de deuren.", "Subject + verb + manner + place",
     "ik / loop / met een lampion / langs de deuren → ___", instr="Make the sentence", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "translate", "The Sinterklaas news is on every day at 18:00.", "Compare with the page 3 article",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Translate into English", size=13.8, gap=0)
f.ex("B1", "translate", "St Martin's Day is the festival of sharing.", "Original sentence from page 2 · delen = to share",
     "Sint-Maarten is het feest van het delen. → ___", instr="Translate into English", size=13.8, gap=0)
f.ex("B1", "translate", "De intocht in Amsterdam is de 88e editie.", "Watch the ordinal 88e",
     "The arrival in Amsterdam is the 88th edition. → ___", instr="Translate into Dutch", size=13.8, gap=0)
f.ex("B2", "translate", "Ik zet mijn schoen met een verlanglijstje.", "schoen zetten is a fixed expression",
     "I put out my shoe, with a wish list inside. → ___", instr="Translate into Dutch", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "matching",
            ["het journaal", "de intocht", "de lampion", "delen"],
            ["een papieren lichtje voor 11 november",
             "een dagelijks nieuwsprogramma op televisie",
             "licht en eten geven aan anderen",
             "de feestelijke aankomst van Sinterklaas"],
            ["b", "d", "a", "c"],
            ["journaal = news programme b", "intocht = the festive arrival d", "lampion = lantern a", "delen = to share c"],
            instr="Match word to meaning")
f.head("G · DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
f.ex("B1", "cloze choice", "A", "schoen = shoe",
     "— Mama, waar moet mijn ___? (A. schoen · B. boek)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "wortel = carrot (for the horse)",
     "— Bij de deur, met een ___ voor het paard. (A. wortel · B. lampion)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "verlanglijstje = wish list",
     "— En mijn ___ erin? (A. verlanglijstje · B. journaal)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "cadeautje = little present",
     "— Ja. Sinterklaas brengt 's nachts een ___. (A. mantel · B. cadeautje)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "18:00 = the Sinterklaas news time",
     "— Eerst kijken we om ___ uur naar het Sinterklaasjournaal. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.head("H · SCHRIJF ZELF", 21, OLIVE, 5)
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
f.bridge(f"Writing task (no single answer); model text ({NWORDS} words) below.")
f.ex("B1", "writing", "(open task, model text below)", f"See the model text in section H ({NWORDS} words)",
     "«Mijn week met Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, loop jij met een lampion, kijk jij naar het Sinterklaasjournaal, en zet jij je schoen?", instr="Write", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ANTWOORDEN · ANSWER KEY — grouped by page: find your number", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Every answer has a short note in English · ✓ marks the writing task", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 13.5, "sans", True, OLIVE, lh=1.17, gap=1.5, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "writing":
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
