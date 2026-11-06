# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-nl-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · TEST E RISPOSTE", "De Lucerna", "Pagina 8 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "Cloze", "B", "Il notiziario di Sinterklaas inizia il 9 novembre",
     "Het Sinterklaasjournaal begint op 9 ___. (A. oktober · B. november)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "L'arrivo nazionale è a Grave",
     "De landelijke intocht is in ___. (A. Amsterdam · B. Grave)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "L'arrivo ad Amsterdam è l'88ª edizione",
     "De intocht in Amsterdam is de ___ editie. (A. 26e · B. 88e)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Paesi Bassi–Grecia, calcio d'inizio alle 20:45",
     "Oranje – Griekenland begint om ___ uur. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "San Martino cade l'11 novembre",
     "Sint-Maarten is op 11 ___. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Robinson va in onda su RTL 4",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "San Martino è la festa della condivisione",
     "Sint-Maarten is het feest van het ___. (A. griezelen · B. delen)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "schoen zetten = mettere fuori la scarpa",
     "«De schoen zetten» betekent ___. (A. schoenen kopen · B. je schoen neerzetten)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "Scelta multipla", "A", "Il notiziario di Sinterklaas va in onda ogni giorno alle 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Grave si trova sul fiume Mosa",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Sinterklaas riceve la chiave della città al Museo marittimo",
     "In Amsterdam krijgt Sinterklaas de sleutel bij... A. de Stopera · B. het Scheepvaartmuseum · C. het Leidseplein", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Het diner è stato pubblicato nel 2009",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Paesi Bassi e Grecia hanno entrambi 8 punti",
     "Na vier wedstrijden hebben Nederland en Griekenland ___ punten. A. 5 · B. 8 · C. 0", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Germania–Paesi Bassi, lunedì, a Berlino",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=13.8, gap=0)
f.ex("B2", "Scelta multipla", "B", "Una tradizione vive quando la gente continua a festeggiarla",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "C", "Pakjesavond cade sabato 5 dicembre",
     "Pakjesavond is op... A. 11 november · B. 14 november · C. 5 december", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht. Op woensdag 11 november loopt zij met een lampion mee in de Sint Maarten Parade en zingt zij bij elke deur. Elke dag kijkt zij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag kijkt zij op televisie naar de intocht in Grave. Zondag zet zij haar schoen met een wortel en een verlanglijstje. Vrijdag kijkt zij naar Oranje tegen Griekenland.", 15, lh=1.3, split=False)
f.ex("A2", "Scelta multipla", "B", "Sanne vive a Utrecht",
     "Waar woont Sanne? A. in Grave · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Mercoledì si unisce alla sfilata di San Martino",
     "Wat doet Sanne op woensdag 11 november? A. Ze kijkt naar Oranje · B. Ze loopt mee in de Sint Maarten Parade · C. Ze leest Het diner", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Mette una carota e una lista dei desideri nella sua scarpa",
     "Wat zit er in de schoen van Sanne? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Guarda il notiziario di Sinterklaas ogni giorno alle 18:00",
     "Wanneer kijkt Sanne naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Forma la frase", "Het Sinterklaasjournaal begint op maandag.", "Soggetto + verbo + tempo",
     "het sinterklaasjournaal / begint / op maandag → ___", instr="Forma la frase", size=13.8, gap=0)
f.ex("B1", "Forma la frase", "Wij zetten onze schoen bij de deur.", "Soggetto + verbo + complemento + luogo",
     "wij / zetten / onze schoen / bij de deur → ___", instr="Forma la frase", size=13.8, gap=0)
f.ex("B1", "Forma la frase", "Oranje speelt vrijdag tegen Griekenland.", "Soggetto + verbo + tempo + avversario",
     "oranje / speelt / vrijdag / tegen griekenland → ___", instr="Forma la frase", size=13.8, gap=0)
f.ex("B1", "Forma la frase", "Ik loop met een lampion langs de deuren.", "Soggetto + verbo + modo + luogo",
     "ik / loop / met een lampion / langs de deuren → ___", instr="Forma la frase", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "Traduzione", "Il notiziario di Sinterklaas va in onda ogni giorno alle 18:00.", "Confronta con l'articolo di pagina 3",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "San Martino è la festa della condivisione.", "Frase originale da pagina 2 · delen = condividere",
     "Sint-Maarten is het feest van het delen. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "De intocht in Amsterdam is de 88e editie.", "Attenzione all'ordinale 88e",
     "L'arrivo ad Amsterdam è l'88ª edizione. → ___", instr="Traduci in olandese", size=13.8, gap=0)
f.ex("B2", "Traduzione", "Ik zet mijn schoen met een verlanglijstje.", "schoen zetten è un'espressione fissa",
     "Metto fuori la scarpa, con una lista dei desideri dentro. → ___", instr="Traduci in olandese", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "Abbinamento",
            ["het journaal", "de intocht", "de lampion", "delen"],
            ["een papieren lichtje voor 11 november",
             "een dagelijks nieuwsprogramma op televisie",
             "licht en eten geven aan anderen",
             "de feestelijke aankomst van Sinterklaas"],
            ["b", "d", "a", "c"],
            ["journaal = notiziario b", "intocht = arrivo festoso d", "lampion = lanterna a", "delen = condividere c"],
            instr="Abbina la parola al significato")
f.head("G · DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "schoen = scarpa",
     "— Mama, waar moet mijn ___? (A. schoen · B. boek)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "wortel = carota (per il cavallo)",
     "— Bij de deur, met een ___ voor het paard. (A. wortel · B. lampion)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "verlanglijstje = lista dei desideri",
     "— En mijn ___ erin? (A. verlanglijstje · B. journaal)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "cadeautje = regalino",
     "— Ja. Sinterklaas brengt 's nachts een ___. (A. mantel · B. cadeautje)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "18:00 = l'ora del notiziario di Sinterklaas",
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
f.bridge(f"Compito di scrittura (senza risposta unica); testo modello ({NWORDS} parole) sotto.")
f.ex("B1", "Scrittura", "(compito aperto, testo modello sotto)", f"Vedi il testo modello nella sezione H ({NWORDS} parole)",
     "«Mijn week met Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, loop jij met een lampion, kijk jij naar het Sinterklaasjournaal, en zet jij je schoen?", instr="Scrivi", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ANTWOORDEN · CHIAVE DELLE RISPOSTE — raggruppate per pagina: trova il tuo numero", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Ogni risposta con una breve nota in italiano · ✓ segna il compito di scrittura", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 13.5, "sans", True, OLIVE, lh=1.17, gap=1.5, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Scrittura":
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
