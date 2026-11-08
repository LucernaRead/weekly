# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P8: 38 exercises + registry-generated answers. Dash style, as W45.
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
f.ex("B1", "完形单选", "B", "visita a Chequia = en déplacement en Tchéquie",
     "El jueves, la Roja ___ a Chequia en Praga. (A. recibe · B. visita)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "recibir a Inglaterra = recevoir l'Angleterre à domicile",
     "El domingo, España ___ a Inglaterra en Madrid. (A. visita · B. recibe)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "la lista = liste des convoqués",
     "De la Fuente dio ___ el viernes 6. (A. la lista · B. la huelga)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "la huelga dura 24 horas = la grève dure 24 heures",
     "La huelga del miércoles ___ 24 horas. (A. empieza · B. dura)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "empieza la campaña = la campagne commence",
     "El viernes 13 ___ la campaña electoral. (A. empieza · B. termina)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "el sobre = enveloppe",
     "El voto por correo llega en un ___. (A. puente · B. sobre)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "Espagne–Angleterre dimanche",
     "El domingo se juega el ___ en el Metropolitano. (A. España–Inglaterra · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "veranillo = été de la Saint-Martin",
     "En noviembre llega el ___ de San Martín. (A. veranillo · B. puente)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "La grève générale a lieu mercredi 11 novembre",
     "La huelga general es el... A. lunes 9 · B. miércoles 11 · C. viernes 13", size=15.5, gap=1)
f.ex("A2", "单选", "A", "Saint-Martin, 11 novembre",
     "San Martín es el... A. 11 de noviembre · B. 12 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "单选", "C", "Espagne–Angleterre et la grève, tous les deux cette semaine",
     "Esta semana hay... A. solo fútbol · B. solo huelga · C. la huelga y el España–Inglaterra", size=15.5, gap=1)
f.ex("B1", "单选", "B", "Au magosto, on mange des châtaignes grillées",
     "¿Qué se come en el magosto? A. flan · B. castañas asadas · C. chocolate", size=15.5, gap=1)
f.ex("B1", "单选", "A", "Slogan de la grève : salaires, logement, prix",
     "El lema de la huelga es... A. «Salarios, vivienda y precios» · B. «Fútbol y fiesta» · C. «Cine y series»", size=15.5, gap=1)
f.ex("B1", "单选", "C", "L'élection a lieu le 29 novembre",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "单选", "B", "Baromètre logement du CIS : 86,9 % inquiets pour le logement",
     "Según el CIS de vivienda, está preocupado el... A. 13,5 % · B. 86,9 % · C. 79 %", size=15.5, gap=1)
f.ex("B1", "单选", "A", "La campagne commence le 13 novembre",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el miércoles 11 sigue la huelga en las noticias y el domingo ve el España–Inglaterra en el Metropolitano. Ana vive en Barcelona: el miércoles 11 trabaja, y el domingo ve el partido por televisión. Los dos leen los programas antes de votar el 29.", 16.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Pablo va au Metropolitano dimanche",
     "¿Quién ve el partido en el Metropolitano? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "单选", "A", "Ana travaille mercredi",
     "El miércoles 11, Ana... A. trabaja · B. va a la huelga · C. duerme", size=15.5, gap=1)
f.ex("A2", "单选", "A", "Tous les deux lisent les programmes avant de voter",
     "Antes de votar, los dos... A. leen los programas · B. ven «Infamia» · C. viajan a Praga", size=15.5, gap=1)
f.ex("A2", "单选", "B", "Le titre résume le contraste entre deux lieux",
     "El mejor título es... A. «Una tormenta» · B. «Dos miércoles» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "造句", "El miércoles hay huelga general.", "Sujet + verbe + lieu",
     "el miércoles / hay / huelga general → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("A2", "造句", "El domingo vemos el España–Inglaterra.", "Le temps d'abord",
     "el domingo / vemos / el España–Inglaterra → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("B1", "造句", "La campaña empieza a las cero horas.", "a las cero horas = à minuit",
     "la campaña / empieza / a las cero horas → ___", instr="Former une phrase", size=15.5, gap=1)
f.ex("B1", "造句", "¿A qué hora empieza el partido?", "Le mot interrogatif en tête",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Former une phrase", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "翻译", "Mercredi, grève générale dans toute l'Espagne.", "Compare avec l'original.",
     "El miércoles hay huelga general en toda España. → ___", instr="Traduire", size=15.5, gap=1)
f.ex("A2", "翻译", "Dimanche, nous regardons Espagne–Angleterre.", "Compare avec l'original.",
     "El domingo vemos el España–Inglaterra. → ___", instr="Traduire", size=15.5, gap=1)
f.ex("B1", "翻译", "El voto por correo llega a casa.", "llegar a casa = arriver à la maison",
     "Le vote par correspondance arrive à la maison. → ___", instr="Traduire", size=15.5, gap=1)
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
            ["sondeo=sondage c", "muestra=échantillon d", "margen de error=marge d'erreur b", "junta electoral=commission électorale a"],
            instr="Associer")
f.head("G　DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "A", "alquiler = loyer",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "tres habitaciones = trois pièces",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "¿cuánto cuesta? = combien ça coûte ?",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "firmar = signer (un contrat)",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "mudanza = déménagement",
     "— La ___ es el miércoles 11, día de huelga. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("Exercice d'écriture (pas de réponse unique) ; texte modèle (84 mots) ci-dessous.")
f.ex("B1", "写作", "Question ouverte — texte modèle ci-dessous sur cette page", "Texte modèle dans la section H de cette page (84 mots)",
     "«¿Qué harías tú por la vivienda?» Escribe 80–100 palabras: tu plan del miércoles 11, tu domingo 15 y tu voto del 29.", instr="Écrire", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y el miércoles 11 sigo la huelga en las noticias: salarios, vivienda y precios, los tres temas de la semana. "
          "El viernes 13 empieza la campaña, y el domingo 15 veo el España–Inglaterra con mi familia. "
          "El jueves 12 veo el Chequia–España en Praga por televisión, a las 20:45. "
          "Mis amigos de Barcelona no tienen huelga en su empresa: el miércoles trabajan. Yo, en cambio, leo los programas con calma y preparo mi voto por correo. "
          "El 29 votamos. ¡Qué semana!")
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
