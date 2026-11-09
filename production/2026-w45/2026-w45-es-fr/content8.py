# -*- coding: utf-8 -*-
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
f.ex("B1", "完形单选", "B", "ganó 2–1 = gagner 2–1",
     "El Madrid ___ 2–1 en el Camp Nou. (A. perdió · B. ganó)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "marcar dos goles = marquer deux buts",
     "Mbappé ___ dos goles en Barcelona. (A. paró · B. marcó)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "primera derrota liguera = première défaite en Liga",
     "Fue la primera ___ del Barça en la Liga. (A. derrota · B. victoria)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "recortar = réduire l'écart",
     "El Madrid ___ la distancia a tres puntos. (A. aumentó · B. recortó)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "acoger = accueillir (le Bernabéu accueille la NFL)",
     "El Bernabéu ___ un partido de la NFL. (A. acoge · B. cierra)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "el emparrillado = le terrain de football américain",
     "El Bernabéu cambia el césped por el ___. (A. puente · B. emparrillado)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "dimanche : Atlético–Barça au Metropolitano",
     "El domingo se juega el ___ en el Metropolitano. (A. Atlético–Barça · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "himno = l'hymne",
     "Antes del partido suenan dos ___: el de España y el de EE. UU. (A. himnos · B. puentes)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "9 communautés en congé le lundi",
     "El lunes 2 es fiesta en... A. todas · B. nueve comunidades · C. ninguna", size=15.5, gap=1)
f.ex("A2", "单选", "A", "la Toussaint, le 1er novembre",
     "Todos los Santos es el... A. 1 de noviembre · B. 2 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "单选", "C", "l'Atlético–Barça et la NFL ont lieu le dimanche",
     "El domingo 8 hay... A. solo fútbol · B. solo NFL · C. la NFL y el Atlético–Barça", size=15.5, gap=1)
f.ex("B1", "单选", "B", "à la Castanyada, on mange des panellets",
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", "单选", "A", "les actes de mémoire de la DANA ont eu lieu le jeudi 29 octobre",
     "Los actos de memoria de la DANA fueron el... A. jueves 29 de octubre · B. sábado 31 · C. lunes 2", size=15.5, gap=1)
f.ex("B1", "单选", "C", "élections le 29 novembre",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "单选", "B", "au baromètre CIS d'octobre : le logement à 55,7 %",
     "Según el CIS de octubre, la vivienda es el principal problema para el... A. 20,9 % · B. 55,7 % · C. 17,1 %", size=15.5, gap=1)
f.ex("B1", "单选", "A", "la campagne commence le 13 novembre",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el lunes 2 es festivo en su comunidad y hace puente. Ana vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El domingo por la tarde, Ana ve la NFL en televisión; por la noche, Pablo ve el Atlético–Barça.", 16.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Madrid figure sur la liste des congés",
     "¿Quién hace puente? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "单选", "A", "en Catalogne, le lundi est un jour de travail",
     "El lunes 2, Ana... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", "单选", "A", "Ana ne regarde que la NFL ; c'est Pablo qui voit l'Atlético–Barça le soir",
     "El domingo, Ana ve... A. solo la NFL · B. solo el Barça · C. la NFL y, por la noche, el Atlético–Barça", size=15.5, gap=1)
f.ex("A2", "单选", "B", "le titre résume le contraste entre les deux villes",
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "造句", "El lunes es festivo en Madrid.", "sujet + verbe + lieu",
     "el lunes / es festivo / en Madrid → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("A2", "造句", "El domingo vemos la NFL en el Bernabéu.", "le temps d'abord",
     "el domingo / vemos / la NFL / en el Bernabéu → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("B1", "造句", "El Atlético–Barça empieza a las nueve.", "a las nueve = à neuf heures",
     "el Atlético–Barça / empieza / a las nueve → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("B1", "造句", "¿A qué hora empieza el partido?", "le mot interrogatif en tête",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Former une phrase", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "翻译", "Le lundi est férié dans neuf communautés.", "d'après le texte",
     "El lunes es festivo en nueve comunidades. → ___", instr="Traduire", size=15.5, gap=1)
f.ex("A2", "翻译", "Le dimanche, nous regardons la NFL et l'Atlético–Barça.", "d'après le texte",
     "El domingo vemos la NFL y el Atlético–Barça. → ___", instr="Traduire", size=15.5, gap=1)
f.ex("B1", "翻译", "El Bernabéu acoge un partido de la NFL.", "acoger = accueillir",
     "Le Bernabéu accueille un match de la NFL. → ___", instr="Traduire", size=15.5, gap=1)
f.ex("B2", "翻译", "Cada gráfico tiene que llevar su fuente.", "tener que = devoir",
     "Chaque graphique doit indiquer sa source. → ___", instr="Traduire", size=15.5, gap=1)
f.head("F　LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo = le sondage (c)", "muestra = l'échantillon (d)", "margen de error = la marge d'erreur (b)", "junta electoral = la commission électorale (a)"],
            instr="Associer")
f.head("G　DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "A", "alquiler = le loyer",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "tres habitaciones = trois pièces",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "¿cuánto cuesta ? = combien ça coûte ?",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "firmar = signer (le contrat)",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "mudanza = le déménagement",
     "— La ___ es el lunes 2, que es fiesta. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("Exercice d'écriture (pas de réponse unique) ; texte modèle (84 mots) ci-dessous.")
f.ex("B1", "写作", "Question ouverte — texte modèle ci-dessous sur cette page", "Texte modèle dans la section H de cette page (84 mots)",
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del puente y tu domingo 8.", instr="Écrire", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y aquí el lunes 2 de noviembre sí es festivo: hago puente con mi familia. "
          "El sábado 7 vemos el Valencia–Real Madrid en televisión, y el domingo 8 tenemos dos citas: por la tarde, la NFL en el Bernabéu, y por la noche, el Atlético–Barça. "
          "Mis amigos de Barcelona no tienen puente: el lunes trabajan. Yo, en cambio, descanso un día más y preparo la semana con calma. "
          "El viernes 13 empieza la campaña, y el 29 votamos todos. ¡Qué mes!")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPUESTAS　CORRIGÉS — classés par page, cherchez le numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Une courte explication en français pour chaque exercice　✓ = exercice d'écriture", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.12, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "写作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.2, lh=1.12, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
