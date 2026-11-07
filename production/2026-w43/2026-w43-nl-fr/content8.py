# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-nl-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · TEST ET RÉPONSES", "De Lucerna", "Page 8 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "Cloze", "B", "En automne, l'horloge recule",
     "In de nacht van zaterdag op zondag gaat de klok één uur ___. (A. vooruit · B. achteruit)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Les vacances du Centre et du Sud vont jusqu'au 25 octobre",
     "De herfstvakantie van Midden en Zuid duurt tot en met zondag ___ oktober. (A. 25 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "La Design Week est à Eindhoven",
     "De Dutch Design Week is in ___. (A. Eindhoven · B. Amsterdam)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Le PSV a gagné à Porto",
     "PSV won in de Champions League bij ___. (A. Atalanta · B. FC Porto)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "L'ADE a 30 ans cette année",
     "ADE wordt dit jaar ___ jaar. (A. 25 · B. 30)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Robinson commence en novembre",
     "Expeditie Robinson begint op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Le plus gros mot cherché pour l'horloge : wintertijd",
     "De grootste zoekterm over de klok was «___». (A. wintertijd · B. klok vooruit)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "half drie = 2 h 30",
     "«Half drie» is ___. (A. 03:30 · B. 02:30)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "Choix", "B", "L'heure d'hiver commence à 03 h 00",
     "De wintertijd begint om... A. 02:00 uur · B. 03:00 uur · C. middernacht", size=13.8, gap=0)
f.ex("A2", "Choix", "A", "Le Nord est en vacances du 10 au 18 octobre",
     "Welke regio had vakantie van 10 tot en met 18 oktober? A. Noord · B. Midden · C. Zuid", size=13.8, gap=0)
f.ex("A2", "Choix", "C", "Le billet étudiant coûte € 19,50",
     "Een studentenkaartje voor de DDW kost... A. € 32,50 · B. € 25,00 · C. € 19,50", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "Feyenoord joue mercredi à Séville",
     "Feyenoord speelt woensdag in... A. Sevilla · B. Porto · C. Eindhoven", size=13.8, gap=0)
f.ex("B1", "Choix", "B", "Sparta – Ajax commence à 16 h 45",
     "Sparta – Ajax begint zondag om... A. 14:30 uur · B. 16:45 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("B1", "Choix", "B", "Les 19 candidats sont Néerlandais et Flamands",
     "De 19 kandidaten van Expeditie Robinson zijn... A. allemaal dj's · B. Nederlanders en Vlamingen · C. alleen sporters", size=13.8, gap=0)
f.ex("B2", "Choix", "B", "6.600 personnes ont cherché « vooruit » (le mauvais sens)",
     "De 6.600 zoekopdrachten vroegen naar... A. achteruit · B. vooruit · C. wintertijd", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "Les plateformes afficheront clairement tous les frais",
     "Thuisbezorgd laat voortaan... A. alle extra kosten duidelijk zien · B. geen eten meer bezorgen · C. alleen kortingsbonnen zien", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht, in de regio Midden. Zij heeft de hele week herfstvakantie. Op woensdag gaat zij met haar zus naar Eindhoven, naar de Dutch Design Week. Zaterdagavond zet zij alle klokken in huis één uur achteruit — behalve haar telefoon, die doet het zelf. Zondag slaapt zij lang uit: het is de laatste dag van de vakantie.", 15, lh=1.3, split=False)
f.ex("A2", "Choix", "B", "Sanne habite à Utrecht",
     "Waar woont Sanne? A. in Venlo · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "Choix", "B", "Sa région est en vacances d'automne",
     "Waarom heeft Sanne de hele week vrij? A. Zij is ziek · B. Het is herfstvakantie in haar regio · C. Zij werkt niet", size=13.8, gap=0)
f.ex("A2", "Choix", "B", "Elle règle l'horloge samedi soir",
     "Wat doet Sanne zaterdagavond? A. Zij gaat dansen · B. Zij zet de klokken achteruit · C. Zij pakt haar koffer", size=13.8, gap=0)
f.ex("B1", "Choix", "C", "Le téléphone change l'heure tout seul",
     "Welke klok zet Sanne NIET met de hand achteruit? A. de ovenklok · B. de wekker · C. haar telefoon", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Phrase", "De klok gaat één uur achteruit.", "Sujet + verbe + complément + direction",
     "de klok / gaat / één uur / achteruit → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "Phrase", "Wij gaan zondag naar de topper.", "Sujet + verbe + temps + lieu",
     "wij / gaan / zondag / naar de topper → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "Phrase", "Hoe laat begint de wedstrijd?", "Le mot interrogatif en tête",
     "hoe laat / begint / de wedstrijd / ? → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "Phrase", "PSV won met 1–0 in Porto.", "Sujet + verbe + score + lieu",
     "psv / won / met 1–0 / in porto → ___", instr="Former la phrase", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "Traduction", "Dimanche, l'horloge recule : une heure de sommeil en plus !", "Compare avec la bande de la page 1",
     "Zondag gaat de klok terug: een uur langer slapen! → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B1", "Traduction", "Ton téléphone et ton ordinateur changent l'heure tout seuls.", "Phrase de la page 2 · veranderen = changer",
     "Je telefoon en je computer veranderen de tijd zelf. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B1", "Traduction", "De Dutch Design Week is in Eindhoven.", "Attention au groupe de lieu : in Eindhoven",
     "La Dutch Design Week est à Eindhoven. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B2", "Traduction", "Zondag heb ik een uur langer geslapen.", "Perfectum : heb geslapen",
     "Dimanche, j'ai dormi une heure de plus. → ___", instr="Traduire", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "Appariement",
            ["de klok verzetten", "het ezelsbruggetje", "eropuit gaan", "bijslapen"],
            ["extra slapen om uit te rusten",
             "het huis uit gaan voor iets leuks",
             "een hulpmiddel om iets te onthouden",
             "de tijd op een klok veranderen"],
            ["d", "c", "b", "a"],
            ["verzetten=régler l'horloge d", "ezelsbruggetje=moyen mnémotechnique c", "eropuit=sortir, partir en balade b", "bijslapen=rattraper son sommeil a"],
            instr="Associer")
f.head("G · DIALOOG BIJ DE DDW", 21, OLIVE, 5)
f.ex("B1", "Cloze", "B", "kaartje = le billet",
     "— Goedemorgen! Een ___ voor de Dutch Design Week, alstublieft. (A. ezelsbruggetje · B. kaartje)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "student = l'étudiant (billet € 19,50)",
     "— Natuurlijk. Bent u ___? Studenten betalen € 19,50. (A. student · B. ontwerper)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "tot hoe laat = jusqu'à quelle heure",
     "— Ja! Hier is mijn studentenkaart. En tot hoe ___ zijn jullie open? (A. lang · B. laat)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "veel plezier = amuse-toi bien",
     "— Tot 18:00 uur. Veel ___ met de ontwerpen! (A. plezier · B. slaap)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "tot ziens = au revoir",
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
f.expl(f"(Question ouverte — texte modèle ci-dessous)")
f.ex("B1", "Rédaction", "(Question ouverte — texte modèle ci-dessous)", f"Texte modèle dans la section H de cette page ({NWORDS} mots)",
     "«Jouw zondag 25 oktober» Schrijf 80–100 woorden: wat doe jij op de laatste vakantiedag, hoe laat sta jij op, en wat doe jij 's middags?", instr="Écrire", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ANTWOORDEN · RÉPONSES — classées par page, trouvez votre numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Une courte explication par numéro · ✓ = texte modèle", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Rédaction":
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
