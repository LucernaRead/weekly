# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN　PRUEBA Y RESPUESTAS", "De Lucerna", "Página 8　De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "Texto con huecos", "B", "El noticiario de Sinterklaas empieza el 9 de noviembre",
     "Het Sinterklaasjournaal begint op 9 ___. (A. oktober · B. november)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "La llegada nacional es en Grave",
     "De landelijke intocht is in ___. (A. Amsterdam · B. Grave)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "La llegada a Ámsterdam es la 88.ª edición",
     "De intocht in Amsterdam is de ___ editie. (A. 26e · B. 88e)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "Países Bajos–Grecia, saque inicial a las 20:45",
     "Oranje – Griekenland begint om ___ uur. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "A", "San Martín cae el 11 de noviembre",
     "Sint-Maarten is op 11 ___. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "Robinson se emite en RTL 4",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "San Martín es la fiesta de compartir",
     "Sint-Maarten is het feest van het ___. (A. griezelen · B. delen)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "schoen zetten = poner el zapato",
     "«De schoen zetten» betekent ___. (A. schoenen kopen · B. je schoen neerzetten)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "Una opción", "A", "El noticiario de Sinterklaas se emite cada día a las 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "Una opción", "B", "Grave está junto al río Mosa",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "Una opción", "B", "Sinterklaas recibe la llave de la ciudad en el Museo Marítimo",
     "In Amsterdam krijgt Sinterklaas de sleutel bij... A. de Stopera · B. het Scheepvaartmuseum · C. het Leidseplein", size=13.8, gap=0)
f.ex("B1", "Una opción", "A", "Het diner se publicó en 2009",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "Una opción", "B", "Países Bajos y Grecia tienen 8 puntos cada uno",
     "Na vier wedstrijden hebben Nederland en Griekenland ___ punten. A. 5 · B. 8 · C. 0", size=13.8, gap=0)
f.ex("B1", "Una opción", "B", "Alemania–Países Bajos, lunes, en Berlín",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=13.8, gap=0)
f.ex("B2", "Una opción", "B", "Una tradición vive cuando la gente sigue celebrándola",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "Una opción", "C", "Pakjesavond cae sábado 5 de diciembre",
     "Pakjesavond is op... A. 11 november · B. 14 november · C. 5 december", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht. Op woensdag 11 november loopt zij met een lampion mee in de Sint Maarten Parade en zingt zij bij elke deur. Elke dag kijkt zij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag kijkt zij op televisie naar de intocht in Grave. Zondag zet zij haar schoen met een wortel en een verlanglijstje. Vrijdag kijkt zij naar Oranje tegen Griekenland.", 15, lh=1.3, split=False)
f.ex("A2", "Una opción", "B", "Sanne vive en Utrecht",
     "Waar woont Sanne? A. in Grave · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "Una opción", "B", "El miércoles se une al desfile de San Martín",
     "Wat doet Sanne op woensdag 11 november? A. Ze kijkt naar Oranje · B. Ze loopt mee in de Sint Maarten Parade · C. Ze leest Het diner", size=13.8, gap=0)
f.ex("A2", "Una opción", "B", "Pone una zanahoria y una lista de deseos en su zapato",
     "Wat zit er in de schoen van Sanne? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "Una opción", "B", "Ve el noticiario de Sinterklaas cada día a las 18:00",
     "Wanneer kijkt Sanne naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Formar frases", "Het Sinterklaasjournaal begint op maandag.", "Sujeto + verbo + tiempo",
     "het sinterklaasjournaal / begint / op maandag → ___", instr="Formar la frase", size=13.8, gap=0)
f.ex("B1", "Formar frases", "Wij zetten onze schoen bij de deur.", "Sujeto + verbo + objeto + lugar",
     "wij / zetten / onze schoen / bij de deur → ___", instr="Formar la frase", size=13.8, gap=0)
f.ex("B1", "Formar frases", "Oranje speelt vrijdag tegen Griekenland.", "Sujeto + verbo + tiempo + rival",
     "oranje / speelt / vrijdag / tegen griekenland → ___", instr="Formar la frase", size=13.8, gap=0)
f.ex("B1", "Formar frases", "Ik loop met een lampion langs de deuren.", "Sujeto + verbo + modo + lugar",
     "ik / loop / met een lampion / langs de deuren → ___", instr="Formar la frase", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "翻译", "El noticiario de Sinterklaas se emite cada día a las 18:00.", "Compara con el artículo de la página 3",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Traducir", size=13.8, gap=0)
f.ex("B1", "翻译", "San Martín es la fiesta de compartir.", "Frase original de la página 2 · delen = compartir",
     "Sint-Maarten is het feest van het delen. → ___", instr="Traducir", size=13.8, gap=0)
f.ex("B1", "翻译", "De intocht in Amsterdam is de 88e editie.", "Fíjate en el ordinal 88e",
     "La llegada a Ámsterdam es la 88.ª edición. → ___", instr="Traducir", size=13.8, gap=0)
f.ex("B2", "翻译", "Ik zet mijn schoen met een verlanglijstje.", "schoen zetten es una expresión fija",
     "Pongo mi zapato, con una lista de deseos dentro. → ___", instr="Traducir", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "Emparejar palabras",
            ["het journaal", "de intocht", "de lampion", "delen"],
            ["een papieren lichtje voor 11 november",
             "een dagelijks nieuwsprogramma op televisie",
             "licht en eten geven aan anderen",
             "de feestelijke aankomst van Sinterklaas"],
            ["b", "d", "a", "c"],
            ["journaal = noticiario b", "intocht = llegada festiva d", "lampion = farolillo a", "delen = compartir c"],
            instr="Relacionar")
f.head("G　DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
f.ex("B1", "Texto con huecos", "A", "schoen = zapato",
     "— Mama, waar moet mijn ___? (A. schoen · B. boek)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "A", "wortel = zanahoria para el caballo",
     "— Bij de deur, met een ___ voor het paard. (A. wortel · B. lampion)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "A", "verlanglijstje = lista de deseos",
     "— En mijn ___ erin? (A. verlanglijstje · B. journaal)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "cadeautje = regalito",
     "— Ja. Sinterklaas brengt 's nachts een ___. (A. mantel · B. cadeautje)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "A", "18:00 = la hora del noticiario de Sinterklaas",
     "— Eerst kijken we om ___ uur naar het Sinterklaasjournaal. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.head("H　SCHRIJF ZELF", 21, OLIVE, 5)
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
f.bridge(f"Tarea de escritura (sin respuesta única); texto modelo ({NWORDS} palabras) abajo.")
f.ex("B1", "Escritura", "(tarea abierta, texto modelo abajo)", f"Véase el texto modelo en la sección H ({NWORDS} palabras)",
     "«Mijn week met Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, loop jij met een lampion, kijk jij naar het Sinterklaasjournaal, en zet jij je schoen?", instr="Escribir", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　SOLUCIONES — agrupadas por página: busca tu número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Cada respuesta con una nota breve en español　✓ marca la tarea de escritura", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Escritura":
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
