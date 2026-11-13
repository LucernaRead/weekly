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
p.band("EJERCICIOS Y RESPUESTAS　ESERCIZI E RISPOSTE", "La Lucerna", "Pagina 8　La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "Cloze (scelta)", "A", "el flamenco suena = il flamenco risuona",
     "El lunes, el flamenco ___ en la calle. (A. suena · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Cloze (scelta)", "B", "empieza la campaña = inizia la campagna",
     "La campaña ___ el viernes 13. (A. termina · B. empieza)", size=15.5, gap=1)
f.ex("B1", "Cloze (scelta)", "A", "Il dibattito laSexta alle 21:30",
     "El debate de laSexta fue a las ___. (A. 21:30 · B. 9:00)", size=15.5, gap=1)
f.ex("B1", "Cloze (scelta)", "A", "el voto por correo se pide hasta el jueves 19",
     "El voto por correo se pide hasta el ___. (A. jueves 19 · B. lunes 16)", size=15.5, gap=1)
f.ex("B1", "Cloze (scelta)", "A", "la Liga vuelve = la Liga torna",
     "La Liga ___ el viernes 20. (A. vuelve · B. para)", size=15.5, gap=1)
f.ex("B1", "Cloze (scelta)", "B", "Il derby di Siviglia è sabato",
     "El derbi Sevilla–Betis es el ___. (A. domingo · B. sábado)", size=15.5, gap=1)
f.ex("B1", "Cloze (scelta)", "A", "Santa Cecilia = patrona dei musicisti",
     "Santa Cecilia es la patrona de los ___. (A. músicos · B. futbolistas)", size=15.5, gap=1)
f.ex("B1", "Cloze (scelta)", "A", "La Spagna vota domenica 29",
     "El domingo 29, España ___. (A. vota · B. duerme)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Scelta multipla", "A", "La campagna inizia venerdì 13 novembre",
     "La campaña electoral empieza el... A. viernes 13 · B. lunes 16 · C. domingo 29", size=15.5, gap=1)
f.ex("A2", "Scelta multipla", "B", "Giornata internazionale del flamenco, 16 novembre",
     "El Día del Flamenco es el... A. domingo 22 · B. lunes 16 · C. viernes 20", size=15.5, gap=1)
f.ex("A2", "Scelta multipla", "A", "Il voto per corrispondenza va chiesto entro il 19",
     "El voto por correo se pide hasta... A. jueves 19 · B. viernes 20 · C. sábado 28", size=15.5, gap=1)
f.ex("B1", "Scelta multipla", "C", "Il derby di Siviglia, sabato ore 18:30",
     "El derbi Sevilla–Betis es el sábado a las... A. 14:00 · B. 21:00 · C. 18:30", size=15.5, gap=1)
f.ex("B1", "Scelta multipla", "B", "Black Friday, venerdì 27 novembre",
     "El Black Friday es el... A. domingo 29 · B. viernes 27 · C. lunes 16", size=15.5, gap=1)
f.ex("B1", "Scelta multipla", "C", "MiDNI è l'app ufficiale di identificazione",
     "MiDNI es... A. un billete · B. una entrada · C. una aplicación oficial", size=15.5, gap=1)
f.ex("B2", "Scelta multipla", "B", "Nessun sondaggio pubblicato dal 24 al 28 novembre",
     "No se publican encuestas del... A. 16 al 19 · B. 24 al 28 · C. 13 al 15", size=15.5, gap=1)
f.ex("B1", "Scelta multipla", "C", "Champions League, 5ª giornata, 24–25 novembre",
     "La jornada 5 de la Champions es el... A. 20–21 · B. 29–30 · C. 24–25", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Lucía vive en Sevilla: el sábado 21 ve el derbi Sevilla–Betis en el Sánchez-Pizjuán. Diego vive en Madrid: el sábado ve el Real Madrid–Celta en el Bernabéu. Los dos escuchan flamenco el lunes 16 y leen los programas antes de votar el 29.", 16.5, lh=1.3, split=False)
f.ex("A2", "Scelta multipla", "A", "Lucía guarda il derby a Siviglia sabato",
     "¿Quién ve el derbi en Sevilla? A. Lucía · B. Diego · C. los dos", size=15.5, gap=1)
f.ex("A2", "Scelta multipla", "A", "Diego guarda Real Madrid–Celta sabato",
     "El sábado, Diego... A. ve el Madrid–Celta · B. ve el derbi · C. duerme", size=15.5, gap=1)
f.ex("A2", "Scelta multipla", "A", "Tutti e due leggono i programmi prima di votare",
     "Antes de votar, los dos... A. leen los programas · B. ven «Infamia» · C. viajan a Praga", size=15.5, gap=1)
f.ex("A2", "Scelta multipla", "B", "Il titolo riassume due città e un sabato",
     "El mejor título es... A. «Una tormenta» · B. «Dos ciudades, un sábado» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Formare frasi", "El lunes suena el flamenco.", "Il tempo prima, il verbo secondo",
     "el lunes / suena / el flamenco → ___", instr="Costruisci", size=15.5, gap=1)
f.ex("A2", "Formare frasi", "El sábado vemos el derbi.", "Il tempo prima",
     "el sábado / vemos / el derbi → ___", instr="Costruisci", size=15.5, gap=1)
f.ex("B1", "Formare frasi", "La campaña dura quince días.", "Soggetto + verbo + tempo",
     "la campaña / dura / quince días → ___", instr="Costruisci", size=15.5, gap=1)
f.ex("B1", "Formare frasi", "¿A qué hora empieza el debate?", "Parola interrogativa all'inizio",
     "¿ / a qué hora / empieza / el debate / ? → ___", instr="Costruisci", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Traduci", "Lunedì è la Giornata internazionale del flamenco.", "Cfr. l'originale.",
     "El lunes es el Día del Flamenco. → ___", instr="Traduci", size=15.5, gap=1)
f.ex("A2", "Traduci", "Sabato guardiamo il derby di Siviglia.", "Cfr. l'originale.",
     "El sábado vemos el derbi Sevilla–Betis. → ___", instr="Traduci", size=15.5, gap=1)
f.ex("B1", "Traduci", "El voto por correo se pide hasta el jueves 19.", "pedir hasta el jueves 19",
     "Il voto per posta va chiesto entro giovedì 19. → ___", instr="Traduci", size=15.5, gap=1)
f.ex("B2", "Traduci", "Cada promesa tiene que llevar datos.", "tener que = dovere",
     "Ogni promessa deve avere dei dati. → ___", instr="Traduci", size=15.5, gap=1)
f.head("F　LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "Abbinare parole",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo=sondaggio c", "muestra=campione d", "margen de error=margine d'errore b", "junta electoral=commissione elettorale a"],
            instr="Abbina le parole")
f.head("G　DIÁLOGO EN EL COLEGIO", 22, OLIVE, 5)
f.ex("B1", "Cloze (scelta)", "A", "vengo a votar = vengo a votare",
     "— Buenos días, vengo a ___. (A. votar · B. cantar)", size=15.5, gap=1)
f.ex("B1", "Cloze (scelta)", "A", "documento de identidad = carta d'identità",
     "— ¿Tiene su documento de ___? (A. identidad · B. puente)", size=15.5, gap=1)
f.ex("B1", "Cloze (scelta)", "A", "¿dónde está la urna? Dov'è l'urna?",
     "— ¿Dónde está la ___? (A. urna · B. guitarra)", size=15.5, gap=1)
f.ex("B1", "Cloze (scelta)", "A", "la papeleta va en el sobre = la scheda va nella busta",
     "— La papeleta va en el ___. (A. sobre · B. derbi)", size=15.5, gap=1)
f.ex("B1", "Cloze (scelta)", "A", "¿a qué hora cierra el colegio? A che ora chiude il seggio?",
     "— ¿A qué hora ___ el colegio? (A. cierra · B. canta)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("Prova di scrittura (senza un'unica risposta giusta); testo modello (97 parole) qui sotto.")
f.ex("B1", "Scrivi", "Domanda aperta — testo modello sotto in questa pagina", "Vedi il modello, sezione H (97 parole)",
     "«¿Qué harías tú en la primera semana de campaña?» Escribe 80–100 palabras: tu lunes 16, tu viernes 20 y tu voto del 29.", instr="Scrivi", size=15.5, gap=1)
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
p.text(MX, 1337, "RESPUESTAS　LE RISPOSTE — ordinate per pagina: cerca il numero", 25, "sans", True, OLIVE)
p.text(RIGHT, 1337, "Una nota in italiano per ogni risposta　✓ = testo modello", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1363, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Scrivi":
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
