# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN　TEST ET RÉPONSES", "De Lucerna", "Page 8　De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "Texte à trous", "B", "Allemagne–Pays-Bas, lundi, à Berlin",
     "Duitsland – Nederland is op maandag in ___. (A. Amsterdam · B. Berlijn)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "B", "Les Pays-Bas et la Grèce ont tous les deux 8 points",
     "Nederland en Griekenland hebben allebei ___ punten. (A. 5 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "Les Pays-Bas ont marqué 7 buts",
     "Nederland maakte ___ doelpunten in vier wedstrijden. (A. 7 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "B", "Pakjesavond est en décembre",
     "Pakjesavond is op ___ december. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "B", "Le journal de Sinterklaas à 18 h 00",
     "Het Sinterklaasjournaal is elke dag om ___ uur. (A. 12:00 · B. 18:00)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "B", "Robinson passe sur RTL 4",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "B", "Un cadeau déguisé contient un poème",
     "Bij een surprise hoort een ___. (A. liedje · B. gedicht)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "B", "groepswinst = victoire de groupe",
     "«De groepswinst» betekent ___. (A. de laatste plaats · B. de eerste plaats in de groep)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "Choix unique", "A", "Le journal de Sinterklaas passe chaque jour à 18 h 00",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "Choix unique", "B", "Grave se trouve sur la Meuse",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "Choix unique", "B", "L'arrivée à Amsterdam est la 88e édition",
     "De intocht in Amsterdam was de... A. 26e editie · B. 88e editie · C. 30e editie", size=13.8, gap=0)
f.ex("B1", "Choix unique", "A", "Het diner a paru en 2009",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "Choix unique", "B", "L'Allemagne a perdu 0–1 à domicile contre la Grèce",
     "Duitsland verloor thuis met 0–1 van... A. Servië · B. Griekenland · C. Nederland", size=13.8, gap=0)
f.ex("B1", "Choix unique", "B", "Le PSV est en tête de l'Eredivisie avec 26 points",
     "PSV staat bovenaan in de Eredivisie met ___ punten. A. 25 · B. 26 · C. 8", size=13.8, gap=0)
f.ex("B2", "Choix unique", "B", "Une tradition vit quand les gens continuent de la fêter",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "Choix unique", "C", "La 13e journée d'Eredivisie a lieu les 21–22 novembre",
     "Speelronde 13 is op... A. 13 en 14 november · B. 16 november · C. 21 en 22 november", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Rotterdam. Op maandag 16 november kijkt hij om 20:45 uur naar Duitsland – Nederland in Berlijn. Elke dag kijkt hij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag 21 november kijkt hij naar NEC – PSV. Zondag zet hij zijn schoen met een wortel en een verlanglijstje. Op zondagavond kijkt hij ook naar Expeditie Robinson.", 15, lh=1.3, split=False)
f.ex("A2", "Choix unique", "B", "Daan habite à Rotterdam",
     "Waar woont Daan? A. in Grave · B. in Rotterdam · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "Choix unique", "B", "Le lundi, il regarde Allemagne–Pays-Bas",
     "Wat doet Daan op maandag 16 november? A. Hij kijkt naar Robinson · B. Hij kijkt naar Duitsland – Nederland · C. Hij leest Het diner", size=13.8, gap=0)
f.ex("A2", "Choix unique", "B", "Carotte et liste de souhaits dans sa chaussure",
     "Wat zit er in de schoen van Daan? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "Choix unique", "B", "Il regarde le journal de Sinterklaas tous les jours à 18 h",
     "Wanneer kijkt Daan naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Faire des phrases", "Het Sinterklaasjournaal begint om 18:00 uur.", "S + V + temps",
     "het sinterklaasjournaal / begint / om 18:00 uur → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "Faire des phrases", "Wij zetten onze schoen bij de deur.", "Sujet + verbe + objet + lieu",
     "wij / zetten / onze schoen / bij de deur → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "Faire des phrases", "Oranje speelt maandag in Berlijn.", "Sujet + verbe + temps + lieu",
     "oranje / speelt / maandag / in berlijn → ___", instr="Former la phrase", size=13.8, gap=0)
f.ex("B1", "Faire des phrases", "Ik zet mijn schoen met een wortel.", "Sujet + verbe + objet",
     "ik / zet / mijn schoen / met een wortel → ___", instr="Former la phrase", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "Traduction", "Le journal de Sinterklaas passe chaque jour à 18 h 00.", "Comparez avec l'article page 3",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Traduire en français", size=13.8, gap=0)
f.ex("B1", "Traduction", "Les deux premiers passent en quart de finale.", "Phrase originale de la page 4 · kwartfinale = quart de finale",
     "De nummers één en twee gaan naar de kwartfinales. → ___", instr="Traduire en français", size=13.8, gap=0)
f.ex("B1", "Traduction", "De intocht in Amsterdam was de 88e editie.", "Ordinal 88e",
     "L'arrivée à Amsterdam est la 88e édition. → ___", instr="Traduire en néerlandais", size=13.8, gap=0)
f.ex("B2", "Traduction", "Ik maak een surprise met een kort gedicht.", "surprise est une expression fixe",
     "Je fais une surprise avec un petit poème. → ___", instr="Traduire en néerlandais", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "Associer les mots",
            ["het journaal", "de groepswinst", "de schoen", "het gedicht"],
            ["een klein versje bij een cadeau",
             "een dagelijks nieuwsprogramma op televisie",
             "de eerste plaats in de groep",
             "die staat 's avonds bij de deur"],
            ["b", "c", "d", "a"],
            ["journaal = journal télévisé b", "groepswinst=victoire de groupe c", "schoen = chaussure d", "gedicht=poème a"],
            instr="Associez les paires")
f.head("G　DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
f.ex("B1", "Texte à trous", "A", "schoen = chaussure",
     "— Mama, waar moet mijn ___? (A. schoen · B. boek)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "wortel = carotte pour le cheval",
     "— Bij de deur, met een ___ voor het paard. (A. wortel · B. lampion)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "verlanglijstje = liste de souhaits",
     "— En mijn ___ erin? (A. verlanglijstje · B. journaal)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "B", "cadeautje = petit cadeau",
     "— Ja. Sinterklaas brengt 's nachts een ___. (A. mantel · B. cadeautje)", size=13.8, gap=0)
f.ex("B1", "Texte à trous", "A", "18 h 00 = l'heure du journal de Sinterklaas",
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
f.bridge(f"Tâche d'écriture (pas de réponse unique) ; texte modèle ({NWORDS} mots) ci-dessous.")
f.ex("B1", "Écriture", "(tâche ouverte, texte modèle ci-dessous)", f"Voir le texte modèle, section H ({NWORDS} mots)",
     "«Mijn week met Oranje en Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, kijk jij naar Duitsland – Nederland, en zet jij je schoen?", instr="Écrire", size=13.8, gap=0)
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
p.text(MX, 1302, "ANTWOORDEN　CORRIGÉ — classé par page : trouvez votre numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Chaque réponse a une courte note en français　✓ marque l'exercice d'écriture", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Écriture":
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
