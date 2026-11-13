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
f.ex("B1", "Texto con huecos", "B", "Alemania–Países Bajos, lunes, en Berlín",
     "Duitsland – Nederland is op maandag in ___. (A. Amsterdam · B. Berlijn)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "Países Bajos y Grecia tienen 8 puntos cada uno",
     "Nederland en Griekenland hebben allebei ___ punten. (A. 5 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "A", "Países Bajos marcó 7 goles",
     "Nederland maakte ___ doelpunten in vier wedstrijden. (A. 7 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "Pakjesavond es en diciembre",
     "Pakjesavond is op ___ december. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "El noticiario de Sinterklaas a las 18:00",
     "Het Sinterklaasjournaal is elke dag om ___ uur. (A. 12:00 · B. 18:00)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "Robinson se emite en RTL 4",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "Un regalo disfrazado lleva un poema",
     "Bij een surprise hoort een ___. (A. liedje · B. gedicht)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "groepswinst = victoria de grupo",
     "«De groepswinst» betekent ___. (A. de laatste plaats · B. de eerste plaats in de groep)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "Una opción", "A", "El noticiario de Sinterklaas se emite cada día a las 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "Una opción", "B", "Grave está junto al río Mosa",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "Una opción", "B", "La llegada a Ámsterdam es la 88.ª edición",
     "De intocht in Amsterdam was de... A. 26e editie · B. 88e editie · C. 30e editie", size=13.8, gap=0)
f.ex("B1", "Una opción", "A", "Het diner se publicó en 2009",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "Una opción", "B", "Alemania perdió 0–1 en casa contra Grecia",
     "Duitsland verloor thuis met 0–1 van... A. Servië · B. Griekenland · C. Nederland", size=13.8, gap=0)
f.ex("B1", "Una opción", "B", "El PSV lidera la Eredivisie con 26 puntos",
     "PSV staat bovenaan in de Eredivisie met ___ punten. A. 25 · B. 26 · C. 8", size=13.8, gap=0)
f.ex("B2", "Una opción", "B", "Una tradición vive cuando la gente sigue celebrándola",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "Una opción", "C", "La jornada 13 de la Eredivisie es el 21–22 de noviembre",
     "Speelronde 13 is op... A. 13 en 14 november · B. 16 november · C. 21 en 22 november", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Rotterdam. Op maandag 16 november kijkt hij om 20:45 uur naar Duitsland – Nederland in Berlijn. Elke dag kijkt hij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag 21 november kijkt hij naar NEC – PSV. Zondag zet hij zijn schoen met een wortel en een verlanglijstje. Op zondagavond kijkt hij ook naar Expeditie Robinson.", 15, lh=1.3, split=False)
f.ex("A2", "Una opción", "B", "Daan vive en Róterdam",
     "Waar woont Daan? A. in Grave · B. in Rotterdam · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "Una opción", "B", "El lunes ve Alemania–Países Bajos",
     "Wat doet Daan op maandag 16 november? A. Hij kijkt naar Robinson · B. Hij kijkt naar Duitsland – Nederland · C. Hij leest Het diner", size=13.8, gap=0)
f.ex("A2", "Una opción", "B", "Pone una zanahoria y una lista de deseos en su zapato",
     "Wat zit er in de schoen van Daan? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "Una opción", "B", "Ve el noticiario de Sinterklaas todos los días a las 18:00",
     "Wanneer kijkt Daan naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "Formar frases", "Het Sinterklaasjournaal begint om 18:00 uur.", "S + V + tiempo",
     "het sinterklaasjournaal / begint / om 18:00 uur → ___", instr="Formar la frase", size=13.8, gap=0)
f.ex("B1", "Formar frases", "Wij zetten onze schoen bij de deur.", "S + V + O + lugar",
     "wij / zetten / onze schoen / bij de deur → ___", instr="Formar la frase", size=13.8, gap=0)
f.ex("B1", "Formar frases", "Oranje speelt maandag in Berlijn.", "Sujeto + verbo + tiempo + lugar",
     "oranje / speelt / maandag / in berlijn → ___", instr="Formar la frase", size=13.8, gap=0)
f.ex("B1", "Formar frases", "Ik zet mijn schoen met een wortel.", "S + V + O + modo",
     "ik / zet / mijn schoen / met een wortel → ___", instr="Formar la frase", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "Traducción", "El noticiario de Sinterklaas se emite cada día a las 18:00.", "Compara con el artículo de la página 3",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="Traducir al español", size=13.8, gap=0)
f.ex("B1", "Traducción", "Los dos primeros pasan a cuartos de final.", "Frase original de la página 4 · kwartfinale = cuartos de final",
     "De nummers één en twee gaan naar de kwartfinales. → ___", instr="Traducir al español", size=13.8, gap=0)
f.ex("B1", "Traducción", "De intocht in Amsterdam was de 88e editie.", "Ordinal 88e",
     "La llegada a Ámsterdam es la 88.ª edición. → ___", instr="Traducir al neerlandés", size=13.8, gap=0)
f.ex("B2", "Traducción", "Ik maak een surprise met een kort gedicht.", "surprise: expresión fija; corto = kort",
     "Hago un surprise con un poema corto. → ___", instr="Traducir al neerlandés", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "Emparejar palabras",
            ["het journaal", "de groepswinst", "de schoen", "het gedicht"],
            ["een klein versje bij een cadeau",
             "een dagelijks nieuwsprogramma op televisie",
             "de eerste plaats in de groep",
             "die staat 's avonds bij de deur"],
            ["b", "c", "d", "a"],
            ["journaal = noticiario b", "groepswinst=victoria de grupo c", "schoen = zapato d", "gedicht=poema a"],
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
f.bridge(f"Tarea de escritura (sin respuesta única); texto modelo ({NWORDS} palabras) abajo.")
f.ex("B1", "Escritura", "(tarea abierta, texto modelo abajo)", f"Véase el texto modelo en la sección H ({NWORDS} palabras)",
     "«Mijn week met Oranje en Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, kijk jij naar Duitsland – Nederland, en zet jij je schoen?", instr="Escribir", size=13.8, gap=0)
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
p.text(MX, 1302, "ANTWOORDEN　SOLUCIONES — ordenadas por página: buscad vuestro número", 25, "sans", True, OLIVE)
p.text(NOTE_RIGHT, 1302, "Cada respuesta tiene una nota breve en español　✓ marca el ejercicio de escritura", 19.5, "sans", False, GREY, anchor="end")  # fix1 D3: anchor NOTE_RIGHT, string unchanged
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
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-toets.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
