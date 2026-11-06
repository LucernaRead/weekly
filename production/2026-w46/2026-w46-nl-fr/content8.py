# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-nl-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · TEST ET RÉPONSES", "De Lucerna", "Page 8 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "完形单选", "B", "Le journal de Sinterklaas commence le 9 novembre",
     "Het Sinterklaasjournaal begint op 9 ___. (A. oktober · B. november)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "L'arrivée nationale a lieu à Grave",
     "De landelijke intocht is in ___. (A. Amsterdam · B. Grave)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "L'arrivée à Amsterdam est la 88e édition",
     "De intocht in Amsterdam is de ___ editie. (A. 26e · B. 88e)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Pays-Bas–Grèce, coup d'envoi à 20 h 45",
     "Oranje – Griekenland begint om ___ uur. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "La Saint-Martin tombe le 11 novembre",
     "Sint-Maarten is op 11 ___. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Robinson passe sur RTL 4",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "La Saint-Martin est la fête du partage",
     "Sint-Maarten is het feest van het ___. (A. griezelen · B. delen)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "schoen zetten = poser sa chaussure",
     "«De schoen zetten» betekent ___. (A. schoenen kopen · B. je schoen neerzetten)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "单选", "A", "Le journal de Sinterklaas passe chaque jour à 18 h 00",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "单选", "B", "Grave se trouve sur la Meuse",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "单选", "B", "Sinterklaas reçoit la clé de la ville au musée maritime",
     "In Amsterdam krijgt Sinterklaas de sleutel bij... A. de Stopera · B. het Scheepvaartmuseum · C. het Leidseplein", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Het diner a paru en 2009",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Les Pays-Bas et la Grèce ont tous les deux 8 points",
     "Na vier wedstrijden hebben Nederland en Griekenland ___ punten. A. 5 · B. 8 · C. 0", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Allemagne–Pays-Bas, lundi, à Berlin",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=13.8, gap=0)
f.ex("B2", "单选", "B", "Une tradition vit quand les gens continuent de la fêter",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "单选", "C", "Pakjesavond tombe samedi 5 décembre",
     "Pakjesavond is op... A. 11 november · B. 14 november · C. 5 december", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht. Op woensdag 11 november loopt zij met een lampion mee in de Sint Maarten Parade en zingt zij bij elke deur. Elke dag kijkt zij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag kijkt zij op televisie naar de intocht in Grave. Zondag zet zij haar schoen met een wortel en een verlanglijstje. Vrijdag kijkt zij naar Oranje tegen Griekenland.", 15, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Sanne habite à Utrecht",
     "Waar woont Sanne? A. in Grave · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "单选", "B", "Mercredi, elle rejoint le défilé de la Saint-Martin",
     "Wat doet Sanne op woensdag 11 november? A. Ze kijkt naar Oranje · B. Ze loopt mee in de Sint Maarten Parade · C. Ze leest Het diner", size=13.8, gap=0)
f.ex("A2", "单选", "B", "Elle met une carotte et une liste de souhaits dans sa chaussure",
     "Wat zit er in de schoen van Sanne? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Elle regarde le journal de Sinterklaas chaque jour à 18 h 00",
     "Wanneer kijkt Sanne naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "造句", "Het Sinterklaasjournaal begint op maandag.", "Sujet + verbe + temps",
     "het sinterklaasjournaal / begint / op maandag → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "造句", "Wij zetten onze schoen bij de deur.", "Sujet + verbe + objet + lieu",
     "wij / zetten / onze schoen / bij de deur → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "造句", "Oranje speelt vrijdag tegen Griekenland.", "Sujet + verbe + temps + adversaire",
     "oranje / speelt / vrijdag / tegen griekenland → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "造句", "Ik loop met een lampion langs de deuren.", "Sujet + verbe + manière + lieu",
     "ik / loop / met een lampion / langs de deuren → ___", instr="Former la phrase", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "翻译", "Le journal de Sinterklaas passe chaque jour à 18 h 00.", "Comparez avec l'article page 3",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B1", "翻译", "La Saint-Martin est la fête du partage.", "Phrase d'origine, page 2 · delen = partager",
     "Sint-Maarten is het feest van het delen. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B1", "翻译", "De intocht in Amsterdam is de 88e editie.", "Attention à l'ordinal 88e",
     "L'arrivée à Amsterdam est la 88e édition. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B2", "翻译", "Ik zet mijn schoen met een verlanglijstje.", "schoen zetten est une expression fixe",
     "Je pose ma chaussure, avec une liste de souhaits dedans. → ___", instr="Traduire", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["het journaal", "de intocht", "de lampion", "delen"],
            ["een papieren lichtje voor 11 november",
             "een dagelijks nieuwsprogramma op televisie",
             "licht en eten geven aan anderen",
             "de feestelijke aankomst van Sinterklaas"],
            ["b", "d", "a", "c"],
            ["journaal = journal télévisé b", "intocht = arrivée festive d", "lampion = lanterne a", "delen = partager c"],
            instr="Associez les paires")
f.head("G · DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
f.ex("B1", "完形单选", "A", "schoen = chaussure",
     "— Mama, waar moet mijn ___? (A. schoen · B. boek)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "wortel = carotte pour le cheval",
     "— Bij de deur, met een ___ voor het paard. (A. wortel · B. lampion)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "verlanglijstje = liste de souhaits",
     "— En mijn ___ erin? (A. verlanglijstje · B. journaal)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "cadeautje = petit cadeau",
     "— Ja. Sinterklaas brengt 's nachts een ___. (A. mantel · B. cadeautje)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "18 h 00 = l'heure du journal de Sinterklaas",
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
f.bridge(f"Tâche d'écriture (pas de réponse unique) ; texte modèle ({NWORDS} mots) ci-dessous.")
f.ex("B1", "写作", "(tâche ouverte, texte modèle ci-dessous)", f"Voir le texte modèle, section H ({NWORDS} mots)",
     "«Mijn week met Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, loop jij met een lampion, kijk jij naar het Sinterklaasjournaal, en zet jij je schoen?", instr="Écrire", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ANTWOORDEN · CORRIGÉ — classé par page : trouve ton numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Chaque réponse avec une courte note en français · ✓ marque la tâche d'écriture", 19.5, "sans", False, GREY, anchor="end")
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
