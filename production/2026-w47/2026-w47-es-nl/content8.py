# -*- coding: utf-8 -*-
# W47 ES core (VOL.4) — P8: 38 exercises + registry-generated answers. Dash style, as W46.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS　Oefeningen en antwoorden", "La Lucerna", "Pagina 8　La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "Cloze-meerkeuze", "A", "el flamenco suena = de flamenco klinkt",
     "El lunes, el flamenco ___ en la calle. (A. suena · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "B", "empieza la campaña = de campagne begint",
     "La campaña ___ el viernes 13. (A. termina · B. empieza)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "Het laSexta-debat om 21.30 uur",
     "El debate de laSexta fue a las ___. (A. 21:30 · B. 9:00)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "el voto por correo se pide hasta el jueves 19",
     "El voto por correo se pide hasta el ___. (A. jueves 19 · B. lunes 16)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "la Liga vuelve = de competitie is terug",
     "La Liga ___ el viernes 20. (A. vuelve · B. para)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "B", "De derby van Sevilla is op zaterdag",
     "El derbi Sevilla–Betis es el ___. (A. domingo · B. sábado)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "Santa Cecilia = beschermheilige van de musici",
     "Santa Cecilia es la patrona de los ___. (A. músicos · B. futbolistas)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "Spanje stemt op zondag 29",
     "El domingo 29, España ___. (A. vota · B. duerme)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Meerkeuze", "A", "De campagne begint vrijdag 13 november",
     "La campaña electoral empieza el... A. viernes 13 · B. lunes 16 · C. domingo 29", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "B", "Internationale Flamencodag, 16 november",
     "El Día del Flamenco es el... A. domingo 22 · B. lunes 16 · C. viernes 20", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "Stemmen per post: uiterlijk op de 19e aanvragen",
     "El voto por correo se pide hasta... A. jueves 19 · B. viernes 20 · C. sábado 28", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "C", "De derby van Sevilla, zaterdag 18.30 uur",
     "El derbi Sevilla–Betis es el sábado a las... A. 14:00 · B. 21:00 · C. 18:30", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "B", "Black Friday, vrijdag 27 november",
     "El Black Friday es el... A. domingo 29 · B. viernes 27 · C. lunes 16", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "C", "MiDNI is de officiële identiteitsapp",
     "MiDNI es... A. un billete · B. una entrada · C. una aplicación oficial", size=15.5, gap=1)
f.ex("B2", "Meerkeuze", "B", "Geen peilingen van 24 tot 28 november",
     "No se publican encuestas del... A. 16 al 19 · B. 24 al 28 · C. 13 al 15", size=15.5, gap=1)
f.ex("B1", "Meerkeuze", "C", "Champions League, speelronde 5, 24–25 november",
     "La jornada 5 de la Champions es el... A. 20–21 · B. 29–30 · C. 24–25", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Lucía vive en Sevilla: el sábado 21 ve el derbi Sevilla–Betis en el Sánchez-Pizjuán. Diego vive en Madrid: el sábado ve el Real Madrid–Celta en el Bernabéu. Los dos escuchan flamenco el lunes 16 y leen los programas antes de votar el 29.", 16.5, lh=1.3, split=False)
f.ex("A2", "Meerkeuze", "A", "Lucía kijkt zaterdag naar de derby in Sevilla",
     "¿Quién ve el derbi en Sevilla? A. Lucía · B. Diego · C. los dos", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "Diego kijkt zaterdag naar Real Madrid–Celta",
     "El sábado, Diego... A. ve el Madrid–Celta · B. ve el derbi · C. duerme", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "A", "Beiden lezen eerst de programma's en stemmen dan",
     "Antes de votar, los dos... A. leen los programas · B. ven «Infamia» · C. viajan a Praga", size=15.5, gap=1)
f.ex("A2", "Meerkeuze", "B", "De titel vat twee steden en één zaterdag samen",
     "El mejor título es... A. «Una tormenta» · B. «Dos ciudades, un sábado» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Zinnen maken", "El lunes suena el flamenco.", "Eerst de tijd, dan het werkwoord",
     "el lunes / suena / el flamenco → ___", instr="Zinnen maken", size=15.5, gap=1)
f.ex("A2", "Zinnen maken", "El sábado vemos el derbi.", "De tijd vooraan",
     "el sábado / vemos / el derbi → ___", instr="Zinnen maken", size=15.5, gap=1)
f.ex("B1", "Zinnen maken", "La campaña dura quince días.", "Onderwerp + werkwoord + tijd",
     "la campaña / dura / quince días → ___", instr="Zinnen maken", size=15.5, gap=1)
f.ex("B1", "Zinnen maken", "¿A qué hora empieza el debate?", "Het vraagwoord vooraan",
     "¿ / a qué hora / empieza / el debate / ? → ___", instr="Zinnen maken", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Vertalen", "Maandag is het Internationale Flamencodag.", "Vgl. origineel.",
     "El lunes es el Día del Flamenco. → ___", instr="Vertalen", size=15.5, gap=1)
f.ex("A2", "Vertalen", "Zaterdag kijken we naar de derby van Sevilla.", "Vgl. origineel.",
     "El sábado vemos el derbi Sevilla–Betis. → ___", instr="Vertalen", size=15.5, gap=1)
f.ex("B1", "Vertalen", "El voto por correo se pide hasta el jueves 19.", "pedir hasta el jueves 19",
     "De briefstem moet uiterlijk op donderdag 19 worden aangevraagd. → ___", instr="Vertalen", size=15.5, gap=1)
f.ex("B2", "Vertalen", "Cada promesa tiene que llevar datos.", "tener que = moeten",
     "Elke belofte moet met gegevens worden onderbouwd. → ___", instr="Vertalen", size=15.5, gap=1)
f.head("F　LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "Woorden combineren",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo=peiling c", "muestra=steekproef d", "margen de error=foutmarge b", "junta electoral=verkiezingscommissie a"],
            instr="Combineer")
f.head("G　DIÁLOGO EN EL COLEGIO", 22, OLIVE, 5)
f.ex("B1", "Cloze-meerkeuze", "A", "vengo a votar = ik kom stemmen",
     "— Buenos días, vengo a ___. (A. votar · B. cantar)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "documento de identidad = identiteitsbewijs",
     "— ¿Tiene su documento de ___? (A. identidad · B. puente)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "¿dónde está la urna? Waar is de stembus?",
     "— ¿Dónde está la ___? (A. urna · B. guitarra)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "la papeleta va en el sobre = het stembiljet in de envelop",
     "— La papeleta va en el ___. (A. sobre · B. derbi)", size=15.5, gap=1)
f.ex("B1", "Cloze-meerkeuze", "A", "¿a qué hora cierra el colegio? Hoe laat sluit het?",
     "— ¿A qué hora ___ el colegio? (A. cierra · B. canta)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("Schrijfopdracht (geen enkel juist antwoord); voorbeeldtekst (97 woorden) hieronder.")
f.ex("B1", "Schrijven", "Open vraag — voorbeeldtekst hieronder op deze pagina", "Zie de voorbeeldtekst in deel H op deze pagina (97 woorden)",
     "«¿Qué harías tú en la primera semana de campaña?» Escribe 80–100 palabras: tu lunes 16, tu viernes 20 y tu voto del 29.", instr="Schrijven", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y el lunes 16 escucho flamenco en la calle: cante, toque y baile, la música de la semana. "
          "El viernes 13 empezó la campaña, y el domingo 29 voto por primera vez: pido el voto por correo hasta el jueves 19. "
          "El viernes 20 vuelve la Liga, y el sábado veo el derbi Sevilla–Betis con mi familia. "
          "El domingo 22 escucho a la banda de Santa Cecilia. "
          "Mis amigos de Barcelona no tienen duende en su barrio: el lunes trabajan. Yo, en cambio, leo los programas con calma y preparo mi voto. "
          "¡Qué semana!")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()
print("P8-ex flow ended y=", f.y)

# ---- P8 image: swan pen, in the free space of the last exercise column ----
iy8 = f.y + 24
ih8 = 240
image(p, "swan_pen.jpg", COLX[3], iy8, CW, ih8)
caption(p, COLX[3], iy8 + ih8, CW,
        "La pluma del escritor: esta página es para escribir. El texto modelo de arriba tiene 97 palabras: tu texto, entre 80 y 100.",
        "Pluma de cisne — dominio público (Wikimedia Commons)")
print("P8 image bottom approx", iy8 + ih8 + 90)

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1337, "RESPUESTAS　Antwoorden — per pagina gerangschikt; zoek op nummer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1337, "Bij elk antwoord een korte uitleg in het Nederlands　✓ = met voorbeeldtekst", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1363, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Schrijven":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("MODELO words:", len(MODELO.split()))
