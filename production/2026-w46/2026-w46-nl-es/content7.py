# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · TAAL (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("TAAL　LENGUA", "De Lucerna", "La lengua, en primer plano　Drie niveaus, drie gereedschappen　Tres niveles, tres herramientas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　SINTERKLAASWOORDEN", 24)
a.para("De woorden van deze week horen bij Sinterklaas: de stoomboot, de intocht, de schoen zetten en de lampion. De stoomboot brengt Sinterklaas uit Spanje. De intocht is zijn feestelijke aankomst in een stad.", 21.5)
a.para("En de schoen: na de intocht zetten kinderen hun schoen bij de deur, met een wortel voor het paard. 's Nachts komt Sinterklaas met een cadeautje. Onthoud ook: Sint-Maarten is het feest van het delen.", 21.5)
a.bridge("de stoomboot: el barco de vapor; de intocht: la llegada festiva; de schoen zetten: poner el zapato; de lampion: el farolillo.")
a.ex("A2", "Completar las frases", "stoomboot", "de stoomboot = barco de vapor",
     "Sinterklaas komt met de ___ uit Spanje.", instr="Completar", size=20.5, gap=10)
a.ex("A2", "Completar las frases", "schoen", "schoen zetten = poner el zapato",
     "Na de intocht zetten kinderen hun ___.", instr="Completar", size=20.5, gap=10)
a.ex("A2", "Una opción", "B", "La intocht es la llegada festiva de Sinterklaas",
     "«De intocht» is... A. een boek · B. de feestelijke aankomst van Sinterklaas · C. een liedje", size=20.5, gap=10)
a.ex("A2", "Completar las frases", "lampion", "lampion = farolillo",
     "Op Sint-Maarten lopen kinderen met een ___.", instr="Completar", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　VERKLEINWOORDEN", 24)
b.para("Nederlands maakt graag kleine woorden met -je: de schoen wordt het schoentje, het licht wordt het lichtje, het cadeau wordt het cadeautje. Klein betekent hier: lief, klein of gezellig — niet altijd echt klein.", 21.5)
b.para("Let op de spelling: de medeklinker verdubbelt soms, maar niet altijd — het is het boekje, het worteltje, het liedje. En na -ing komt -tje: de lampion wordt het lampionnetje. Oefen met de woorden van deze week.", 21.5)
b.bridge("schoentje: zapatito; lichtje: lucecita; cadeautje: regalito. -je significa pequeño y cariñoso.")
b.ex("B1", "Completar las frases", "schoentje", "schoen + -tje: schoentje",
     "Zet je ___ bij de deur, met een wortel erin.", instr="Completar", size=20.5, gap=10)
b.ex("B1", "Completar las frases", "lichtje", "licht + -je: lichtje",
     "«Elf november is de dag, dat mijn ___ branden mag.»", instr="Completar", size=20.5, gap=10)
b.ex("B1", "Completar las frases", "cadeautje", "cadeau + -tje: cadeautje",
     "Sinterklaas brengt een ___ in de schoen.", instr="Completar", size=20.5, gap=10)
b.ex("B1", "Una opción", "B", "-je significa pequeño y cariñoso, no siempre realmente pequeño",
     "Een verkleinwoord met -je betekent... A. altijd heel klein · B. klein, lief of gezellig · C. heel groot", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　ZINNEN MET ALS", 24)
c.para("Met «als» zeg je wanneer iets gebeurt: «Als het donker wordt, gaan de kinderen op pad.» «Als Sinterklaas komt, staat de schoen klaar.» De bijzin met «als» staat eerst; daarna komt het werkwoord op plaats 1 in de hoofdzin.", 21.5)
c.para("Voorbeeld: «Als Oranje wint, gaat Nederland naar de kwartfinales.» «Als het regent, loop ik toch met mijn lampion.» Een als-zin is geen vraag — het is een voorwaarde: dit gebeurt, dan dat.", 21.5)
c.bridge("Als…: si… / cuando…; als het donker wordt: cuando oscurece; als Sinterklaas komt: cuando viene Sinterklaas.")
c.ex("B2", "Completar las frases", "Als", "Als…: si… / cuando…",
     "___ het donker wordt, gaan de kinderen op pad.", instr="Completar", size=20.5, gap=10)
c.ex("B2", "Una opción", "B", "Una cláusula con als es una condición, no una pregunta",
     "«Als Sinterklaas komt, staat de schoen klaar» is... A. een vraag · B. een voorwaarde · C. een bevel", size=20.5, gap=10)
c.ex("B2", "Completar las frases", "gaat", "El verbo va primero en la oración principal: gaat de lampion aan",
     "Als het donker wordt, ___ de lampion aan.", instr="Completar", size=20.5, gap=10)
c.ex("B2", "Completar las frases", "wint", "Als Oranje wint…: si Oranje gana…",
     "Als Oranje ___, gaat Nederland naar de kwartfinales.", instr="Completar", size=20.5, gap=10)
c.end_report()

# ---- col 3: pas op + het woord + brieven ----
bx = COLX[3]
errs = [
    ("«De Sinterklaas komt zaterdag.»", "→ Fout: Sinterklaas is een naam, zonder lidwoord: «Sinterklaas komt zaterdag.»", "Sinterklaas es un nombre, sin artículo."),
    ("«Ik zet de schoen.»", "→ «De schoen zetten» vraagt een bezittelijk woord: «Ik zet mijn schoen.»", "mijn schoen = mi zapato."),
    ("«Kinderen lopen langs de deur.»", "→ Het is een vaste uitdrukking: «langs de deuren» (meervoud).", "Expresión fija: langs de deuren."),
    ("«Als Sinterklaas komt, ik ben blij.»", "→ Na de als-zin staat het werkwoord vooraan: «... ben ik blij.»", "Verbo primero: ben ik blij."),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 192
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "PAS OP!　CLÍNICA DE ERRORES", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 18
wt = "«de schoen zetten» betekent: je schoen neerzetten, met een wortel en een tekening erin, voor Sinterklaas."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("schoen zetten = poner el zapato, con una zanahoria y un dibujo dentro.", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "HET WOORD　LA PALABRA", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "schoen zetten = poner el zapato, con una zanahoria y un dibujo dentro.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 18
lt = "«Hallo! Ik ben Anna en ik leer Nederlands. Op 11 november loop ik met een lampion langs de deuren!» — Anna (voorbeeldbrief van de redactie)"
dt_nl = "Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.4."
dt_es = "Sin cartas reales ni mejores textos: ejemplo; promesa para el VOL.4."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(dt_nl, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(dt_es, "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap("Ejemplo de la redacción. ¡Envíanos cartas y textos para el VOL.4!", "sans", False, 20, CW - 44)) * 29 + 34 + 50
# +50 measured correction carried from W45 Fix-1 (rendered spacing runs above formula).
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "BRIEVEN VAN LEZERS", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, dt_nl, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, dt_es, 20, "sans", False, GREY, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Ejemplo de la redacción. ¡Envíanos cartas y textos para el VOL.4!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- zinnen van de week (verbatim from this issue) ----
fy = 1951
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "ZINNEN VAN DE WEEK　FRASES DE LA SEMANA (LITERALES DE ESTE NÚMERO)", 27, "sans", True, OLIVE)
quotes = [
    ("«Op maandag 9 november begint het Sinterklaasjournaal op televisie»", "El lunes 9 de noviembre empieza en televisión el noticiario de Sinterklaas.", "Pagina 1"),
    ("«Een dag later, op zondag 15 november, is de intocht in Amsterdam: de 88e editie»", "Al día siguiente, domingo 15 de noviembre: Ámsterdam, 88.ª edición.", "Pagina 1"),
    ("«Daarom is Sint-Maarten het feest van het delen: licht delen, eten delen, aandacht delen»", "San Martín es la fiesta de compartir: compartir luz, comida y atención.", "Pagina 2"),
    ("«Op zaterdag 14 november komt Sinterklaas officieel aan in Grave»", "El sábado 14 de noviembre, Sinterklaas llega oficialmente a Grave.", "Pagina 3"),
    ("«Op vrijdag 13 november speelt Oranje thuis tegen Griekenland»", "El viernes 13 de noviembre, Oranje juega en casa contra Grecia.", "Pagina 4"),
    ("«Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4»", "Cada domingo a las 20:00, Expeditie Robinson se emite en RTL 4.", "Pagina 5"),
    ("«Sint-Maarten is een oude traditie in Nederland»", "San Martín es una vieja tradición en los Países Bajos.", "Pagina 6"),
    ("«Een traditie leeft als mensen haar blijven vieren»", "Una tradición vive cuando la gente sigue celebrándola.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 90 + (16 if (i % 4) >= 3 else 0)
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- volgende week ----
py = 2439
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "VOLGENDE WEEK　LA SEMANA QUE VIENE (VOL.4)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Maandag 16 november speelt Oranje in Berlijn tegen Duitsland — de uitslag lees je volgende week. Zaterdag 5 december is het pakjesavond. Verder: jullie brieven en de beste teksten van pagina 8. Tot maandag!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-taal.svg")
print("P7 saved, exercises so far:", len(REG))
