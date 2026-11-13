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
p.band("EJERCICIOS Y RESPUESTAS　EXERCICES ET RÉPONSES", "La Lucerna", "Page 8　La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "Texte à trous (choix)", "A", "el flamenco suena = le flamenco résonne",
     "El lunes, el flamenco ___ en la calle. (A. suena · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Texte à trous (choix)", "B", "empieza la campaña = la campagne commence",
     "La campaña ___ el viernes 13. (A. termina · B. empieza)", size=15.5, gap=1)
f.ex("B1", "Texte à trous (choix)", "A", "Le débat laSexta à 21 h 30",
     "El debate de laSexta fue a las ___. (A. 21:30 · B. 9:00)", size=15.5, gap=1)
f.ex("B1", "Texte à trous (choix)", "A", "el voto por correo se pide hasta el jueves 19",
     "El voto por correo se pide hasta el ___. (A. jueves 19 · B. lunes 16)", size=15.5, gap=1)
f.ex("B1", "Texte à trous (choix)", "A", "la Liga vuelve = la Liga est de retour",
     "La Liga ___ el viernes 20. (A. vuelve · B. para)", size=15.5, gap=1)
f.ex("B1", "Texte à trous (choix)", "B", "Le derby de Séville a lieu samedi",
     "El derbi Sevilla–Betis es el ___. (A. domingo · B. sábado)", size=15.5, gap=1)
f.ex("B1", "Texte à trous (choix)", "A", "Santa Cecilia = sainte patronne des musiciens",
     "Santa Cecilia es la patrona de los ___. (A. músicos · B. futbolistas)", size=15.5, gap=1)
f.ex("B1", "Texte à trous (choix)", "A", "L'Espagne vote le dimanche 29",
     "El domingo 29, España ___. (A. vota · B. duerme)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Choix multiple", "A", "La campagne commence vendredi 13 novembre",
     "La campaña electoral empieza el... A. viernes 13 · B. lunes 16 · C. domingo 29", size=15.5, gap=1)
f.ex("A2", "Choix multiple", "B", "Journée internationale du flamenco, 16 novembre",
     "El Día del Flamenco es el... A. domingo 22 · B. lunes 16 · C. viernes 20", size=15.5, gap=1)
f.ex("A2", "Choix multiple", "A", "Vote par correspondance : à demander le 19 au plus tard",
     "El voto por correo se pide hasta... A. jueves 19 · B. viernes 20 · C. sábado 28", size=15.5, gap=1)
f.ex("B1", "Choix multiple", "C", "Le derby de Séville, samedi 18 h 30",
     "El derbi Sevilla–Betis es el sábado a las... A. 14:00 · B. 21:00 · C. 18:30", size=15.5, gap=1)
f.ex("B1", "Choix multiple", "B", "Black Friday, vendredi 27 novembre",
     "El Black Friday es el... A. domingo 29 · B. viernes 27 · C. lunes 16", size=15.5, gap=1)
f.ex("B1", "Choix multiple", "C", "MiDNI est l'appli officielle d'identité",
     "MiDNI es... A. un billete · B. una entrada · C. una aplicación oficial", size=15.5, gap=1)
f.ex("B2", "Choix multiple", "B", "Aucun sondage publié du 24 au 28 novembre",
     "No se publican encuestas del... A. 16 al 19 · B. 24 al 28 · C. 13 al 15", size=15.5, gap=1)
f.ex("B1", "Choix multiple", "C", "Ligue des champions, 5e journée, 24–25 novembre",
     "La jornada 5 de la Champions es el... A. 20–21 · B. 29–30 · C. 24–25", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Lucía vive en Sevilla: el sábado 21 ve el derbi Sevilla–Betis en el Sánchez-Pizjuán. Diego vive en Madrid: el sábado ve el Real Madrid–Celta en el Bernabéu. Los dos escuchan flamenco el lunes 16 y leen los programas antes de votar el 29.", 16.5, lh=1.3, split=False)
f.ex("A2", "Choix multiple", "A", "Lucía regarde le derby à Séville samedi",
     "¿Quién ve el derbi en Sevilla? A. Lucía · B. Diego · C. los dos", size=15.5, gap=1)
f.ex("A2", "Choix multiple", "A", "Diego regarde le Real Madrid–Celta samedi",
     "El sábado, Diego... A. ve el Madrid–Celta · B. ve el derbi · C. duerme", size=15.5, gap=1)
f.ex("A2", "Choix multiple", "A", "Tous les deux lisent les programmes avant de voter",
     "Antes de votar, los dos... A. leen los programas · B. ven «Infamia» · C. viajan a Praga", size=15.5, gap=1)
f.ex("A2", "Choix multiple", "B", "Le titre résume deux villes et un samedi",
     "El mejor título es... A. «Una tormenta» · B. «Dos ciudades, un sábado» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Former des phrases", "El lunes suena el flamenco.", "Le temps d'abord, puis le verbe",
     "el lunes / suena / el flamenco → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("A2", "Former des phrases", "El sábado vemos el derbi.", "Le temps d'abord",
     "el sábado / vemos / el derbi → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("B1", "Former des phrases", "La campaña dura quince días.", "Sujet + verbe + temps",
     "la campaña / dura / quince días → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("B1", "Former des phrases", "¿A qué hora empieza el debate?", "Le mot interrogatif en tête",
     "¿ / a qué hora / empieza / el debate / ? → ___", instr="Former une phrase", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Traduire", "Lundi, c'est la Journée internationale du flamenco.", "Cf. l'original.",
     "El lunes es el Día del Flamenco. → ___", instr="Traduire", size=15.5, gap=1)
f.ex("A2", "Traduire", "Samedi, nous regardons le derby de Séville.", "Cf. l'original.",
     "El sábado vemos el derbi Sevilla–Betis. → ___", instr="Traduire", size=15.5, gap=1)
f.ex("B1", "Traduire", "El voto por correo se pide hasta el jueves 19.", "pedir hasta el jueves 19",
     "Le vote par correspondance doit être demandé le jeudi 19 au plus tard. → ___", instr="Traduire", size=15.5, gap=1)
f.ex("B2", "Traduire", "Cada promesa tiene que llevar datos.", "tener que = devoir",
     "Chaque promesse doit s'appuyer sur des données. → ___", instr="Traduire", size=15.5, gap=1)
f.head("F　LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "Associer les mots",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo=sondage c", "muestra=échantillon d", "margen de error=marge d'erreur b", "junta electoral=commission électorale a"],
            instr="Associer")
f.head("G　DIÁLOGO EN EL COLEGIO", 22, OLIVE, 5)
f.ex("B1", "Texte à trous (choix)", "A", "vengo a votar = je viens voter",
     "— Buenos días, vengo a ___. (A. votar · B. cantar)", size=15.5, gap=1)
f.ex("B1", "Texte à trous (choix)", "A", "documento de identidad = carte d'identité",
     "— ¿Tiene su documento de ___? (A. identidad · B. puente)", size=15.5, gap=1)
f.ex("B1", "Texte à trous (choix)", "A", "¿dónde está la urna ? Où est l'urne ?",
     "— ¿Dónde está la ___? (A. urna · B. guitarra)", size=15.5, gap=1)
f.ex("B1", "Texte à trous (choix)", "A", "la papeleta va en el sobre = le bulletin va dans l'enveloppe",
     "— La papeleta va en el ___. (A. sobre · B. derbi)", size=15.5, gap=1)
f.ex("B1", "Texte à trous (choix)", "A", "¿a qué hora cierra el colegio ? À quelle heure ferme-t-il ?",
     "— ¿A qué hora ___ el colegio? (A. cierra · B. canta)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("Exercice d'écriture (pas de réponse unique) ; texte modèle (97 mots) ci-dessous.")
f.ex("B1", "Écrire", "Question ouverte — texte modèle ci-dessous sur cette page", "Voir le modèle, partie H (97 mots)",
     "«¿Qué harías tú en la primera semana de campaña?» Escribe 80–100 palabras: tu lunes 16, tu viernes 20 y tu voto del 29.", instr="Écrire", size=15.5, gap=1)
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
p.text(MX, 1337, "RESPUESTAS　CORRIGÉS — classés par page, cherchez le numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1337, "Une courte explication en français pour chaque exercice　✓ = exercice d'écriture", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1363, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Écrire":
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
