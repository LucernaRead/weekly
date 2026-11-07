# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-es-proof/repro-edition/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · PRUEBA Y RESPUESTAS", "De Lucerna", "Página 8 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "Huecos", "B", "La Semana del Clima dura hasta el 8 de noviembre",
     "De Klimaatweek duurt van 2 tot en met ___ november. (A. 7 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Huecos", "B", "Coevorden reparte 200 árboles y arbustos",
     "Coevorden deelt ___ bomen en struiken uit. (A. 100 · B. 200)", size=13.8, gap=0)
f.ex("B1", "Huecos", "B", "La Museumnacht es el 7 de noviembre",
     "Museumnacht is op zaterdag ___ november. (A. 6 · B. 7)", size=13.8, gap=0)
f.ex("B1", "Huecos", "B", "El Twente – Ajax empieza a las 13:30",
     "Twente – Ajax begint om ___ uur. (A. 11:15 · B. 13:30)", size=13.8, gap=0)
f.ex("B1", "Huecos", "A", "El Ajax ganó 2–0 al Atalanta",
     "Ajax won van Atalanta met ___. (A. 2–0 · B. 4–1)", size=13.8, gap=0)
f.ex("B1", "Huecos", "A", "Robinson empezó en noviembre",
     "Expeditie Robinson begon op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "Huecos", "B", "Código naranja: el tiempo es peligroso",
     "Code oranje betekent: het weer is ___. (A. veilig · B. gevaarlijk)", size=13.8, gap=0)
f.ex("B1", "Huecos", "B", "meedoen = participar",
     "«Meedoen» betekent ___. (A. weggaan · B. deelnemen)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "Elección", "A", "La Semana del Clima empieza el lunes 2 de noviembre",
     "De Klimaatweek begint op... A. maandag 2 november · B. dinsdag 3 november · C. zaterdag 7 november", size=13.8, gap=0)
f.ex("A2", "Elección", "B", "El reparto es en Zweeloo",
     "De bomen in Coevorden worden uitgedeeld in... A. Amsterdam · B. Zweeloo · C. Rotterdam", size=13.8, gap=0)
f.ex("A2", "Elección", "B", "Crossing Border es en La Haya",
     "Crossing Border is in... A. Amsterdam · B. Den Haag · C. Utrecht", size=13.8, gap=0)
f.ex("B1", "Elección", "A", "PAN Amsterdam está en la RAI",
     "PAN Amsterdam is in... A. de RAI · B. het Rijksmuseum · C. de Jaarbeurs", size=13.8, gap=0)
f.ex("B1", "Elección", "B", "El Real Betis ganó 1–0 al Feyenoord",
     "Real Betis – Feyenoord eindigde... A. 0–0 · B. 1–0 · C. 0–1", size=13.8, gap=0)
f.ex("B1", "Elección", "B", "Tras 10 jornadas, el Ajax tiene 21 puntos",
     "Na 10 ronden heeft Ajax ___ punten. A. 24 · B. 21 · C. 20", size=13.8, gap=0)
f.ex("B2", "Elección", "B", "Cansancio ante las alertas: tantas alertas que ya no se presta atención",
     "Waarschuwingsmoeheid betekent... A. moe van het weer · B. minder opletten door te veel waarschuwingen · C. een nieuwe code", size=13.8, gap=0)
f.ex("B1", "Elección", "C", "La Snuffelmarkt de Zaandam tiene unos 250 puestos",
     "De Snuffelmarkt in Zaandam heeft zo'n ___ kramen. A. 70 · B. 200 · C. 250", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Coevorden. Op zaterdag 7 november gaat hij naar de Fair Groen in Zweeloo en haalt hij een gratis struik op. 's Avonds kijkt hij naar de foto's van Museumnacht in Amsterdam — zelf gaat hij niet, want zondag speelt zijn club Twente tegen Ajax om 13:30 uur. En in de Klimaatweek fietst Daan elke dag naar school, ook als het regent.", 15, lh=1.3, split=False)
f.ex("A2", "Elección", "B", "Daan vive en Coevorden",
     "Waar woont Daan? A. in Zweeloo · B. in Coevorden · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "Elección", "B", "El sábado recoge un arbusto gratis",
     "Wat haalt Daan op zaterdag op? A. een fiets · B. een gratis struik · C. een kaartje", size=13.8, gap=0)
f.ex("A2", "Elección", "B", "El domingo el Twente juega contra el Ajax",
     "Waarom gaat Daan zaterdagavond niet naar Amsterdam? A. Hij heeft geen kaartje · B. Zondag speelt Twente tegen Ajax · C. Hij houdt niet van musea", size=13.8, gap=0)
f.ex("B1", "Elección", "B", "En la Semana del Clima va cada día en bici al colegio",
     "Wat doet Daan in de Klimaatweek? A. Hij rijdt elke dag met de auto · B. Hij fietst elke dag naar school · C. Hij blijft thuis", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Frases", "De Klimaatweek begint op maandag.", "Sujeto + verbo + tiempo",
     "de klimaatweek / begint / op maandag → ___", instr="Formar la frase", size=13.8, gap=0)
f.ex("B1", "Frases", "Wij planten een boom in de tuin.", "Sujeto + verbo + objeto + lugar",
     "wij / planten / een boom / in de tuin → ___", instr="Formar la frase", size=13.8, gap=0)
f.ex("B1", "Frases", "Twente speelt zondag tegen Ajax.", "Sujeto + verbo + tiempo + rival",
     "twente / speelt / zondag / tegen ajax → ___", instr="Formar la frase", size=13.8, gap=0)
f.ex("B1", "Frases", "Ik doe mee aan de Klimaatweek.", "El verbo separable mee va al final",
     "ik / doe / mee / aan de klimaatweek → ___", instr="Formar la frase", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "Traducción", "La Semana del Clima dura siete días.", "Compara el titular de la página 1",
     "De Klimaatweek duurt zeven dagen. → ___", instr="Traducir", size=13.8, gap=0)
f.ex("B1", "Traducción", "El código naranja significa: prepárate.", "Frase de la página 2 · bereid je voor = prepárate",
     "Code oranje betekent: bereid je voor. → ___", instr="Traducir", size=13.8, gap=0)
f.ex("B1", "Traducción", "Museumnacht duurt van 19:00 uur tot 02:00 uur.", "Atención a la expresión de tiempo van...tot...",
     "La Museumnacht dura desde las 19:00 hasta las 02:00. → ___", instr="Traducir", size=13.8, gap=0)
f.ex("B2", "Traducción", "Ik doe mee aan de Klimaatweek.", "meedoen es un verbo separable",
     "Participo en la Semana del Clima. → ___", instr="Traducir", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "Relacionar",
            ["het klimaat", "meedoen", "de waarschuwing", "vastzetten"],
            ["een bericht over gevaarlijk weer",
             "deelnemen, erbij zijn",
             "het weer en de natuur over een lange tijd",
             "losse spullen stevig maken"],
            ["c", "b", "a", "d"],
            ["klimaat=el clima c", "meedoen=participar b", "waarschuwing=la advertencia a", "vastzetten=fijar d"],
            instr="Relacionar")
f.head("G · DIALOOG BIJ DE BOMEN", 21, OLIVE, 5)
f.ex("B1", "Huecos", "A", "boom = el árbol",
     "— Goedemiddag! Ik kom voor een ___. (A. boom · B. fiets)", size=13.8, gap=0)
f.ex("B1", "Huecos", "A", "struik = el arbusto",
     "— Natuurlijk. Wilt u een boom of een ___? (A. struik · B. auto)", size=13.8, gap=0)
f.ex("B1", "Huecos", "A", "planten = plantar",
     "— Een struik, graag. En waar moet ik hem ___? (A. planten · B. kopen)", size=13.8, gap=0)
f.ex("B1", "Huecos", "B", "zachte = blanda (la tierra)",
     "— In de tuin, in de ___ grond. (A. harde · B. zachte)", size=13.8, gap=0)
f.ex("B1", "Huecos", "A", "El reparto dura hasta las 16:00",
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
f.bridge(f"Pregunta abierta (sin una única respuesta); el modelo ({NWORDS} palabras) está abajo.")
f.ex("B1", "Redacción", "(Pregunta abierta — modelo a continuación)", f"El modelo está en la sección H de esta página ({NWORDS} palabras)",
     "«Jouw week in de Klimaatweek» Schrijf 80–100 woorden: wat doe jij in de Klimaatweek, plant jij iets, fiets jij, en kijk jij naar Museumnacht of voetbal?", instr="Escribir", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ANTWOORDEN · RESPUESTAS — ordenadas por página, busca tu número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Una explicación breve por número · ✓ = modelo de redacción", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Redacción":
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
