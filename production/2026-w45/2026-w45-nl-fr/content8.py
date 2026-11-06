# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · TEST ET RÉPONSES", "De Lucerna", "Page 8 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "完形单选", "B", "La Semaine du climat dure jusqu'au 8 novembre",
     "De Klimaatweek duurt van 2 tot en met ___ november. (A. 7 · B. 8)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Coevorden distribue 200 arbres et arbustes",
     "Coevorden deelt ___ bomen en struiken uit. (A. 100 · B. 200)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "La Nuit des musées : samedi 7 novembre",
     "Museumnacht is op zaterdag ___ november. (A. 6 · B. 7)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Twente – Ajax : coup d'envoi à 13 h 30",
     "Twente – Ajax begint om ___ uur. (A. 11:15 · B. 13:30)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "L'Ajax bat l'Atalanta 2–0",
     "Ajax won van Atalanta met ___. (A. 2–0 · B. 4–1)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Robinson commence en novembre",
     "Expeditie Robinson begon op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Code orange : temps dangereux",
     "Code oranje betekent: het weer is ___. (A. veilig · B. gevaarlijk)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "meedoen = participer",
     "«Meedoen» betekent ___. (A. weggaan · B. deelnemen)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "单选", "A", "La Semaine du climat commence lundi 2 novembre",
     "De Klimaatweek begint op... A. maandag 2 november · B. dinsdag 3 november · C. zaterdag 7 november", size=13.8, gap=0)
f.ex("A2", "单选", "B", "Le lieu de distribution est Zweeloo",
     "De bomen in Coevorden worden uitgedeeld in... A. Amsterdam · B. Zweeloo · C. Rotterdam", size=13.8, gap=0)
f.ex("A2", "单选", "B", "Crossing Border a lieu à La Haye",
     "Crossing Border is in... A. Amsterdam · B. Den Haag · C. Utrecht", size=13.8, gap=0)
f.ex("B1", "单选", "A", "PAN se tient au RAI",
     "PAN Amsterdam is in... A. de RAI · B. het Rijksmuseum · C. de Jaarbeurs", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Le Real Betis bat Feyenoord 1–0",
     "Real Betis – Feyenoord eindigde... A. 0–0 · B. 1–0 · C. 0–1", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Après 10 journées, l'Ajax a 21 points",
     "Na 10 ronden heeft Ajax ___ punten. A. 24 · B. 21 · C. 20", size=13.8, gap=0)
f.ex("B2", "单选", "B", "Lassitude des alertes : trop d'alertes, on ne fait plus attention",
     "Waarschuwingsmoeheid betekent... A. moe van het weer · B. minder opletten door te veel waarschuwingen · C. een nieuwe code", size=13.8, gap=0)
f.ex("B1", "单选", "C", "La Snuffelmarkt de Zaandam compte environ 250 stands",
     "De Snuffelmarkt in Zaandam heeft zo'n ___ kramen. A. 70 · B. 200 · C. 250", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Coevorden. Op zaterdag 7 november gaat hij naar de Fair Groen in Zweeloo en haalt hij een gratis struik op. 's Avonds kijkt hij naar de foto's van Museumnacht in Amsterdam — zelf gaat hij niet, want zondag speelt zijn club Twente tegen Ajax om 13:30 uur. En in de Klimaatweek fietst Daan elke dag naar school, ook als het regent.", 15, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Daan habite à Coevorden",
     "Waar woont Daan? A. in Zweeloo · B. in Coevorden · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "单选", "B", "Samedi, il récupère un arbuste gratuit",
     "Wat haalt Daan op zaterdag op? A. een fiets · B. een gratis struik · C. een kaartje", size=13.8, gap=0)
f.ex("A2", "单选", "B", "Dimanche, Twente joue contre l'Ajax",
     "Waarom gaat Daan zaterdagavond niet naar Amsterdam? A. Hij heeft geen kaartje · B. Zondag speelt Twente tegen Ajax · C. Hij houdt niet van musea", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Pendant la Semaine du climat, il va à l'école à vélo chaque jour",
     "Wat doet Daan in de Klimaatweek? A. Hij rijdt elke dag met de auto · B. Hij fietst elke dag naar school · C. Hij blijft thuis", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "造句", "De Klimaatweek begint op maandag.", "Sujet + verbe + temps",
     "de klimaatweek / begint / op maandag → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "造句", "Wij planten een boom in de tuin.", "Sujet + verbe + complément + lieu",
     "wij / planten / een boom / in de tuin → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "造句", "Twente speelt zondag tegen Ajax.", "Sujet + verbe + temps + adversaire",
     "twente / speelt / zondag / tegen ajax → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "造句", "Ik doe mee aan de Klimaatweek.", "Le verbe à particule mee va en fin de phrase",
     "ik / doe / mee / aan de klimaatweek → ___", instr="Former la phrase", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "翻译", "La Semaine du climat dure sept jours.", "Voir le titre de la page 1",
     "De Klimaatweek duurt zeven dagen. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B1", "翻译", "Le code orange signifie : préparez-vous.", "Phrase de la page 2 · bereid je voor : préparez-vous",
     "Code oranje betekent: bereid je voor. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B1", "翻译", "Museumnacht duurt van 19:00 uur tot 02:00 uur.", "Attention à l'expression du temps van...tot...",
     "La Nuit des musées dure de 19 heures à 2 heures du matin. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B2", "翻译", "Ik doe mee aan de Klimaatweek.", "meedoen est un verbe à particule",
     "Je participe à la Semaine du climat. → ___", instr="Traduire", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["het klimaat", "meedoen", "de waarschuwing", "vastzetten"],
            ["een bericht over gevaarlijk weer",
             "deelnemen, erbij zijn",
             "het weer en de natuur over een lange tijd",
             "losse spullen stevig maken"],
            ["c", "b", "a", "d"],
            ["klimaat=climat c", "meedoen=participer b", "waarschuwing=avertissement a", "vastzetten=bien fixer d"],
            instr="Associez les paires")
f.head("G · DIALOOG BIJ DE BOMEN", 21, OLIVE, 5)
f.ex("B1", "完形单选", "A", "boom = arbre",
     "— Goedemiddag! Ik kom voor een ___. (A. boom · B. fiets)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "struik = arbuste",
     "— Natuurlijk. Wilt u een boom of een ___? (A. struik · B. auto)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "planten = planter",
     "— Een struik, graag. En waar moet ik hem ___? (A. planten · B. kopen)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "zachte = souple, pour la terre",
     "— In de tuin, in de ___ grond. (A. harde · B. zachte)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "La distribution se termine à 16 h",
     "— De uitdeling duurt tot ___ uur. (A. 16:00 · B. 20:00)", size=13.8, gap=0)
f.head("H · SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Maandag 2 november begint de Klimaatweek in Nederland. "
          "Ik doe mee: ik fiets elke dag naar school en ik zet de verwarming één graad lager. "
          "Op zaterdag 7 november ga ik met mijn vader naar Coevorden, want daar deelt de gemeente gratis bomen uit. "
          "Wij nemen een struik mee voor onze tuin. "
          "'s Avonds kijken wij op televisie naar de foto's van Museumnacht in Amsterdam. "
          "Zondag kijken wij naar Twente tegen Ajax. "
          "Mijn zus plant ook een boom op haar balkon. "
          "Wat een week voor het klimaat!")
NWORDS = len(MODELO.split())
f.bridge(f"Question ouverte, sans réponse unique ; texte modèle de {NWORDS} mots ci-dessous.")
f.ex("B1", "写作", "Question ouverte, texte modèle ci-dessous", f"Texte modèle dans la section H de cette page, {NWORDS} mots",
     "«Jouw week in de Klimaatweek» Schrijf 80–100 woorden: wat doe jij in de Klimaatweek, plant jij iets, fiets jij, en kijk jij naar Museumnacht of voetbal?", instr="Écrire", size=13.8, gap=0)
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
        if e_["type"] == "写作":
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
