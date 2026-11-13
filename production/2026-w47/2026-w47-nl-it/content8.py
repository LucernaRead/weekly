# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN　TEST E RISPOSTE", "De Lucerna", "Pagina 8　De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "Testo con lacune", "B", "Germania–Paesi Bassi, lunedì, a Berlino",
     "Duitsland – Nederland is op maandag in ___. (A. Amsterdam · B. Berlijn)", size=13.8, gap=0)
f.ex("B1", "Testo con lacune", "B", "Paesi Bassi e Grecia hanno entrambi 8 punti",
     "Nederland en Griekenland hebben allebei ___ punten. (A. 5 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Testo con lacune", "A", "I Paesi Bassi hanno segnato 7 gol",
     "Nederland maakte ___ doelpunten in vier wedstrijden. (A. 7 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Testo con lacune", "B", "Pakjesavond è in dicembre",
     "Pakjesavond is op ___ december. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "Testo con lacune", "B", "Il notiziario di Sinterklaas alle 18:00",
     "Het Sinterklaasjournaal is elke dag om ___ uur. (A. 12:00 · B. 18:00)", size=13.8, gap=0)
f.ex("B1", "Testo con lacune", "B", "Robinson va in onda su RTL 4",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "Testo con lacune", "B", "Un regalo travestito contiene una poesia",
     "Bij een surprise hoort een ___. (A. liedje · B. gedicht)", size=13.8, gap=0)
f.ex("B1", "Testo con lacune", "B", "groepswinst = vittoria del girone",
     "«De groepswinst» betekent ___. (A. de laatste plaats · B. de eerste plaats in de groep)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "Scelta multipla", "A", "Il notiziario di Sinterklaas va in onda ogni giorno alle 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Grave si trova sul fiume Mosa",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "L'arrivo ad Amsterdam è l'88ª edizione",
     "De intocht in Amsterdam was de... A. 26e editie · B. 88e editie · C. 30e editie", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Het diner è stato pubblicato nel 2009",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "La Germania ha perso 0–1 in casa contro la Grecia",
     "Duitsland verloor thuis met 0–1 van... A. Servië · B. Griekenland · C. Nederland", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Il PSV è in testa all'Eredivisie con 26 punti",
     "PSV staat bovenaan in de Eredivisie met ___ punten. A. 25 · B. 26 · C. 8", size=13.8, gap=0)
f.ex("B2", "Scelta multipla", "B", "Una tradizione vive quando la gente continua a festeggiarla",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "C", "La 13ª giornata di Eredivisie è il 21–22 novembre",
     "Speelronde 13 is op... A. 13 en 14 november · B. 16 november · C. 21 en 22 november", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Rotterdam. Op maandag 16 november kijkt hij om 20:45 uur naar Duitsland – Nederland in Berlijn. Elke dag kijkt hij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag 21 november kijkt hij naar NEC – PSV. Zondag zet hij zijn schoen met een wortel en een verlanglijstje. Op zondagavond kijkt hij ook naar Expeditie Robinson.", 15, lh=1.3, split=False)
f.ex("A2", "Scelta multipla", "B", "Daan abita a Rotterdam",
     "Waar woont Daan? A. in Grave · B. in Rotterdam · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Il lunedì guarda Germania–Paesi Bassi",
     "Wat doet Daan op maandag 16 november? A. Hij kijkt naar Robinson · B. Hij kijkt naar Duitsland – Nederland · C. Hij leest Het diner", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Mette una carota e una lista dei desideri nella scarpa",
     "Wat zit er in de schoen van Daan? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Guarda il notiziario di Sinterklaas ogni giorno alle 18:00",
     "Wanneer kijkt Daan naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Forma la frase", "Het Sinterklaasjournaal begint om 18:00 uur.", "S + V + tempo",
     "het sinterklaasjournaal / begint / om 18:00 uur → ___", instr="Forma la frase", size=13.8, gap=0)
f.ex("B1", "Forma la frase", "Wij zetten onze schoen bij de deur.", "S + V + C + luogo",
     "wij / zetten / onze schoen / bij de deur → ___", instr="Forma la frase", size=13.8, gap=0)
f.ex("B1", "Forma la frase", "Oranje speelt maandag in Berlijn.", "S + V + tempo + luogo",
     "oranje / speelt / maandag / in berlijn → ___", instr="Forma la frase", size=13.8, gap=0)
f.ex("B1", "Forma la frase", "Ik zet mijn schoen met een wortel.", "S + V + O + modo",
     "ik / zet / mijn schoen / met een wortel → ___", instr="Forma la frase", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "Traduzione", "Il notiziario di Sinterklaas va in onda ogni giorno alle 18:00.", "Confronta con l'articolo di pagina 3",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "I primi due passano ai quarti di finale.", "Frase originale da pagina 4 · kwartfinale = quarti di finale",
     "De nummers één en twee gaan naar de kwartfinales. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "De intocht in Amsterdam was de 88e editie.", "Ordinale 88e",
     "L'arrivo ad Amsterdam è l'88ª edizione. → ___", instr="Traduci in olandese", size=13.8, gap=0)
f.ex("B2", "Traduzione", "Ik maak een surprise met een kort gedicht.", "surprise è un'espressione fissa",
     "Faccio una surprise con una breve poesia. → ___", instr="Traduci in olandese", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "Abbinamento",
            ["het journaal", "de groepswinst", "de schoen", "het gedicht"],
            ["een klein versje bij een cadeau",
             "een dagelijks nieuwsprogramma op televisie",
             "de eerste plaats in de groep",
             "die staat 's avonds bij de deur"],
            ["b", "c", "d", "a"],
            ["journaal = notiziario b", "groepswinst=vittoria del girone c", "schoen = scarpa d", "gedicht=poesia a"],
            instr="Parola e significato")
f.head("G　DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
f.ex("B1", "Testo con lacune", "A", "schoen = scarpa",
     "— Mama, waar moet mijn ___? (A. schoen · B. boek)", size=13.8, gap=0)
f.ex("B1", "Testo con lacune", "A", "wortel = carota (per il cavallo)",
     "— Bij de deur, met een ___ voor het paard. (A. wortel · B. lampion)", size=13.8, gap=0)
f.ex("B1", "Testo con lacune", "A", "verlanglijstje = lista dei desideri",
     "— En mijn ___ erin? (A. verlanglijstje · B. journaal)", size=13.8, gap=0)
f.ex("B1", "Testo con lacune", "B", "cadeautje = regalino",
     "— Ja. Sinterklaas brengt 's nachts een ___. (A. mantel · B. cadeautje)", size=13.8, gap=0)
f.ex("B1", "Testo con lacune", "A", "18:00 = l'ora del notiziario di Sinterklaas",
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
f.bridge(f"Compito di scrittura (senza risposta unica); testo modello ({NWORDS} parole) sotto.")
f.ex("B1", "Scrittura", "(compito aperto, testo modello sotto)", f"Vedi il testo modello nella sezione H ({NWORDS} parole)",
     "«Mijn week met Oranje en Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, kijk jij naar Duitsland – Nederland, en zet jij je schoen?", instr="Scrivi", size=13.8, gap=0)
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
p.text(MX, 1302, "ANTWOORDEN　SOLUZIONI — ordinate per pagina: trova il tuo numero", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Ogni risposta ha una breve nota in italiano　✓ indica l'esercizio di scrittura", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Scrittura":
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
