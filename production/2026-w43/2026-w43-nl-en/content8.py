# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-nl-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · TEST AND ANSWERS", "De Lucerna", "Page 8 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "cloze choice", "B", "In autumn the clock goes back",
     "In de nacht van zaterdag op zondag gaat de klok één uur ___. (A. vooruit · B. achteruit)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "The Midden and Zuid break runs to 25 October",
     "De herfstvakantie van Midden en Zuid duurt tot en met zondag ___ oktober. (A. 25 · B. 18)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "Design Week is in Eindhoven",
     "De Dutch Design Week is in ___. (A. Eindhoven · B. Amsterdam)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "PSV won away at Porto",
     "PSV won in de Champions League bij ___. (A. Atalanta · B. FC Porto)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "ADE turns 30 this year",
     "ADE wordt dit jaar ___ jaar. (A. 25 · B. 30)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "Robinson starts in November",
     "Expeditie Robinson begint op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "The biggest clock search term was wintertijd",
     "De grootste zoekterm over de klok was «___». (A. wintertijd · B. klok vooruit)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "half drie = 2:30",
     "«Half drie» is ___. (A. 03:30 · B. 02:30)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "choice", "B", "Winter time starts at 03:00",
     "De wintertijd begint om... A. 02:00 uur · B. 03:00 uur · C. middernacht", size=13.8, gap=0)
f.ex("A2", "choice", "A", "Noord had its break from 10 to 18 October",
     "Welke regio had vakantie van 10 tot en met 18 oktober? A. Noord · B. Midden · C. Zuid", size=13.8, gap=0)
f.ex("A2", "choice", "C", "A student ticket is € 19,50",
     "Een studentenkaartje voor de DDW kost... A. € 32,50 · B. € 25,00 · C. € 19,50", size=13.8, gap=0)
f.ex("B1", "choice", "A", "Feyenoord plays in Seville on Wednesday",
     "Feyenoord speelt woensdag in... A. Sevilla · B. Porto · C. Eindhoven", size=13.8, gap=0)
f.ex("B1", "choice", "B", "Sparta–Ajax starts at 16:45",
     "Sparta – Ajax begint zondag om... A. 14:30 uur · B. 16:45 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("B1", "choice", "B", "The 19 contestants are Dutch and Flemish",
     "De 19 kandidaten van Expeditie Robinson zijn... A. allemaal dj's · B. Nederlanders en Vlamingen · C. alleen sporters", size=13.8, gap=0)
f.ex("B2", "choice", "B", "The 6,600 searches asked about vooruit (the wrong way)",
     "De 6.600 zoekopdrachten vroegen naar... A. achteruit · B. vooruit · C. wintertijd", size=13.8, gap=0)
f.ex("B1", "choice", "A", "The platforms will now show all extra costs clearly",
     "Thuisbezorgd laat voortaan... A. alle extra kosten duidelijk zien · B. geen eten meer bezorgen · C. alleen kortingsbonnen zien", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht, in de regio Midden. Zij heeft de hele week herfstvakantie. Op woensdag gaat zij met haar zus naar Eindhoven, naar de Dutch Design Week. Zaterdagavond zet zij alle klokken in huis één uur achteruit — behalve haar telefoon, die doet het zelf. Zondag slaapt zij lang uit: het is de laatste dag van de vakantie.", 15, lh=1.3, split=False)
f.ex("A2", "choice", "B", "Sanne lives in Utrecht",
     "Waar woont Sanne? A. in Venlo · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "choice", "B", "It is the autumn break in her region",
     "Waarom heeft Sanne de hele week vrij? A. Zij is ziek · B. Het is herfstvakantie in haar regio · C. Zij werkt niet", size=13.8, gap=0)
f.ex("A2", "choice", "B", "She changes the clocks on Saturday evening",
     "Wat doet Sanne zaterdagavond? A. Zij gaat dansen · B. Zij zet de klokken achteruit · C. Zij pakt haar koffer", size=13.8, gap=0)
f.ex("B1", "choice", "C", "Her phone changes itself — no hand needed",
     "Welke klok zet Sanne NIET met de hand achteruit? A. de ovenklok · B. de wekker · C. haar telefoon", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "make sentences", "De klok gaat één uur achteruit.", "Subject + verb + object + direction",
     "de klok / gaat / één uur / achteruit → ___", instr="Make the sentence", size=13.8, gap=0)
f.ex("B1", "make sentences", "Wij gaan zondag naar de topper.", "Subject + verb + time + place",
     "wij / gaan / zondag / naar de topper → ___", instr="Make the sentence", size=13.8, gap=0)
f.ex("B1", "make sentences", "Hoe laat begint de wedstrijd?", "The question phrase comes first",
     "hoe laat / begint / de wedstrijd / ? → ___", instr="Make the sentence", size=13.8, gap=0)
f.ex("B1", "make sentences", "PSV won met 1–0 in Porto.", "Subject + verb + score + place",
     "psv / won / met 1–0 / in porto → ___", instr="Make the sentence", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "translation", "On Sunday the clock goes back: sleep an hour longer!", "The banner headline on page 1",
     "Zondag gaat de klok terug: een uur langer slapen! → ___", instr="Translate into English", size=13.8, gap=0)
f.ex("B1", "translation", "Your phone and your computer change the time themselves.", "A sentence from page 2 · veranderen = to change",
     "Je telefoon en je computer veranderen de tijd zelf. → ___", instr="Translate into English", size=13.8, gap=0)
f.ex("B1", "translation", "De Dutch Design Week is in Eindhoven.", "Watch the place phrase: in Eindhoven",
     "Dutch Design Week is in Eindhoven. → ___", instr="Translate into Dutch", size=13.8, gap=0)
f.ex("B2", "translation", "Zondag heb ik een uur langer geslapen.", "Perfectum: heb geslapen",
     "On Sunday I slept an hour longer. → ___", instr="Translate into Dutch", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "matching",
            ["de klok verzetten", "het ezelsbruggetje", "eropuit gaan", "bijslapen"],
            ["extra slapen om uit te rusten",
             "het huis uit gaan voor iets leuks",
             "een hulpmiddel om iets te onthouden",
             "de tijd op een klok veranderen"],
            ["d", "c", "b", "a"],
            ["verzetten = to change a clock — d", "ezelsbruggetje = a memory trick — c", "eropuit = going out — b", "bijslapen = catching up on sleep — a"],
            instr="Match word to meaning")
f.head("G · DIALOOG BIJ DE DDW", 21, OLIVE, 5)
f.ex("B1", "cloze choice", "B", "kaartje = a ticket",
     "— Goedemorgen! Een ___ voor de Dutch Design Week, alstublieft. (A. ezelsbruggetje · B. kaartje)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "student (ticket € 19,50)",
     "— Natuurlijk. Bent u ___? Studenten betalen € 19,50. (A. student · B. ontwerper)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "tot hoe laat = until what time",
     "— Ja! Hier is mijn studentenkaart. En tot hoe ___ zijn jullie open? (A. lang · B. laat)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "A", "veel plezier = have fun",
     "— Tot 18:00 uur. Veel ___ met de ontwerpen! (A. plezier · B. slaap)", size=13.8, gap=0)
f.ex("B1", "cloze choice", "B", "tot ziens = goodbye",
     "— Dank u wel, tot ___! (A. straks · B. ziens)", size=13.8, gap=0)
f.head("H · SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Zondag 25 oktober word ik laat wakker: het is de laatste dag van mijn herfstvakantie. "
          "Ik heb een uur langer geslapen, want vannacht ging de klok achteruit. "
          "Na het ontbijt ga ik met mijn vrienden naar het bos; de bladeren zijn geel en rood. "
          "'s Middags kijken wij thuis naar PSV tegen Feyenoord op televisie. "
          "Mijn zus gaat naar Amsterdam voor ADE, maar ik blijf liever thuis met een boek. "
          "'s Avonds pak ik mijn tas voor school: morgen begint het gewone leven weer. "
          "Wat een week!")
NWORDS = len(MODELO.split())
f.note(f"Writing task (no single right answer); the model text ({NWORDS} words) is below.")
f.ex("B1", "writing", "(open task — model text below)", f"Model text in section H of this page ({NWORDS} words)",
     "«Jouw zondag 25 oktober» Schrijf 80–100 woorden: wat doe jij op de laatste vakantiedag, hoe laat sta jij op, en wat doe jij 's middags?", instr="Write", size=13.8, gap=0)
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
