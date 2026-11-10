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
f.ex("B1", "Cloze", "B", "La Settimana del clima dura fino all'8 novembre",
     "De Klimaatweek duurt van 2 tot en met ___ november. (A. 7 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Coevorden regala 200 alberi e arbusti",
     "Coevorden deelt ___ bomen en struiken uit. (A. 100 · B. 200)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "La Notte dei musei è il 7 novembre",
     "Museumnacht is op zaterdag ___ november. (A. 6 · B. 7)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Twente–Ajax inizia alle 13:30",
     "Twente – Ajax begint om ___ uur. (A. 11:15 · B. 13:30)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "L'Ajax ha battuto l'Atalanta 2–0",
     "Ajax won van Atalanta met ___. (A. 2–0 · B. 4–1)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Robinson è iniziato a novembre",
     "Expeditie Robinson begon op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Codice arancione: il tempo è pericoloso",
     "Code oranje betekent: het weer is ___. (A. veilig · B. gevaarlijk)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "meedoen = partecipare",
     "«Meedoen» betekent ___. (A. weggaan · B. deelnemen)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "Scelta multipla", "A", "La Settimana del clima inizia lunedì 2 novembre",
     "De Klimaatweek begint op... A. maandag 2 november · B. dinsdag 3 november · C. zaterdag 7 november", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Il luogo della distribuzione è Zweeloo",
     "De bomen in Coevorden worden uitgedeeld in... A. Amsterdam · B. Zweeloo · C. Rotterdam", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Crossing Border è all'Aia",
     "Crossing Border is in... A. Amsterdam · B. Den Haag · C. Utrecht", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Il PAN è al RAI",
     "PAN Amsterdam is in... A. de RAI · B. het Rijksmuseum · C. de Jaarbeurs", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Il Real Betis ha battuto il Feyenoord 1–0",
     "Real Betis – Feyenoord eindigde... A. 0–0 · B. 1–0 · C. 0–1", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Dopo 10 giornate l'Ajax ha 21 punti",
     "Na 10 ronden heeft Ajax ___ punten. A. 24 · B. 21 · C. 20", size=13.8, gap=0)
f.ex("B2", "Scelta multipla", "B", "Stanchezza da allarmi: troppi avvisi, così non si fa più attenzione",
     "Waarschuwingsmoeheid betekent... A. moe van het weer · B. minder opletten door te veel waarschuwingen · C. een nieuwe code", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "C", "Il mercatino di Zaandam ha circa 250 bancarelle",
     "De Snuffelmarkt in Zaandam heeft zo'n ___ kramen. A. 70 · B. 200 · C. 250", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Coevorden. Op zaterdag 7 november gaat hij naar de Fair Groen in Zweeloo en haalt hij een gratis struik op. 's Avonds kijkt hij naar de foto's van Museumnacht in Amsterdam — zelf gaat hij niet, want zondag speelt zijn club Twente tegen Ajax om 13:30 uur. En in de Klimaatweek fietst Daan elke dag naar school, ook als het regent.", 15, lh=1.3, split=False)
f.ex("A2", "Scelta multipla", "B", "Daan abita a Coevorden",
     "Waar woont Daan? A. in Zweeloo · B. in Coevorden · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Sabato ritira un arbusto gratuito",
     "Wat haalt Daan op zaterdag op? A. een fiets · B. een gratis struik · C. een kaartje", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Domenica il Twente gioca contro l'Ajax",
     "Waarom gaat Daan zaterdagavond niet naar Amsterdam? A. Hij heeft geen kaartje · B. Zondag speelt Twente tegen Ajax · C. Hij houdt niet van musea", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Durante la Settimana del clima va a scuola in bici ogni giorno",
     "Wat doet Daan in de Klimaatweek? A. Hij rijdt elke dag met de auto · B. Hij fietst elke dag naar school · C. Hij blijft thuis", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Forma la frase", "De Klimaatweek begint op maandag.", "Soggetto + verbo + tempo",
     "de klimaatweek / begint / op maandag → ___", instr="Forma la frase", size=13.8, gap=0)
f.ex("B1", "Forma la frase", "Wij planten een boom in de tuin.", "Soggetto + verbo + oggetto + luogo",
     "wij / planten / een boom / in de tuin → ___", instr="Forma la frase", size=13.8, gap=0)
f.ex("B1", "Forma la frase", "Twente speelt zondag tegen Ajax.", "Soggetto + verbo + tempo + avversario",
     "twente / speelt / zondag / tegen ajax → ___", instr="Forma la frase", size=13.8, gap=0)
f.ex("B1", "Forma la frase", "Ik doe mee aan de Klimaatweek.", "Verbo separabile: mee va alla fine",
     "ik / doe / mee / aan de klimaatweek → ___", instr="Forma la frase", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "Traduzione", "La Settimana del clima dura sette giorni.", "Confronta con il titolo di pagina 1",
     "De Klimaatweek duurt zeven dagen. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "Il codice arancione significa: preparati.", "Frase originale di pagina 2 · bereid je voor = preparati",
     "Code oranje betekent: bereid je voor. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "Museumnacht duurt van 19:00 uur tot 02:00 uur.", "Attenzione alla formula van...tot...",
     "La Notte dei musei dura dalle 19:00 alle 02:00. → ___", instr="Traduci in olandese", size=13.8, gap=0)
f.ex("B2", "Traduzione", "Ik doe mee aan de Klimaatweek.", "meedoen è un verbo separabile",
     "Io partecipo alla Settimana del clima. → ___", instr="Traduci in olandese", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "Abbinamento",
            ["het klimaat", "meedoen", "de waarschuwing", "vastzetten"],
            ["een bericht over gevaarlijk weer",
             "deelnemen, erbij zijn",
             "het weer en de natuur over een lange tijd",
             "losse spullen stevig maken"],
            ["c", "b", "a", "d"],
            ["klimaat = clima c", "meedoen = partecipare b", "waarschuwing = avviso a", "vastzetten = fissare bene d"],
            instr="Parola e significato")
f.head("G　DIALOOG BIJ DE BOMEN", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "boom = albero",
     "— Goedemiddag! Ik kom voor een ___. (A. boom · B. fiets)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "struik = arbusto",
     "— Natuurlijk. Wilt u een boom of een ___? (A. struik · B. auto)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "planten = piantare",
     "— Een struik, graag. En waar moet ik hem ___? (A. planten · B. kopen)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "zachte = morbido (terreno)",
     "— In de tuin, in de ___ grond. (A. harde · B. zachte)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "La distribuzione finisce alle 16:00",
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
f.bridge(f"Tema (nessuna risposta unica); testo modello ({NWORDS} parole) sotto.")
f.ex("B1", "Scrittura", "(tema aperto, testo modello sotto)", f"Vedi il testo modello nella sezione H ({NWORDS} parole)",
     "«Jouw week in de Klimaatweek» Schrijf 80–100 woorden: wat doe jij in de Klimaatweek, plant jij iets, fiets jij, en kijk jij naar Museumnacht of voetbal?", instr="Scrivi", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　RISPOSTE — in ordine di pagina: cerca il tuo numero", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Ogni risposta ha una breve nota in italiano　✓ indica il tema", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
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
