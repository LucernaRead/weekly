# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCICES & RÉPONSES　EJERCICIOS Y RESPUESTAS", "Le Lucerna", "EVALUACIÓN　LAS RESPUESTAS, AL FINAL DE ESTA PÁGINA")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "C", "el 1 de noviembre de 2026 es domingo"),
    ("A2", "A", "al cementerio, a visitar las tumbas"),
    ("A2", "B", "la flor de Todos los Santos es el crisantemo"),
    ("A2", "B", "las flores se ponen sobre la tumba"),
    ("B1", "C", "se reposer = descansar"),
    ("B1", "B", "j'ai + participio pasado: retrouvé"),
    ("B1", "C", "les cours (sujeto plural) → reprennent"),
    ("A2", "A", "elle écrit = ella escribe"),
]
cnums = [reg_ex(lv, "完形填空", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　TEXTE À TROUS　COMPLETAR", 22)
bf.para(f"Léa a quinze ans. Le ({cnums[0]})___ 1er novembre, elle se lève tôt : c'est la Toussaint. Avec sa famille, elle va au ({cnums[1]})___. Sa grand-mère porte un bouquet de ({cnums[2]})___, les fleurs du souvenir. « On les pose sur la ({cnums[3]})___ de ton grand-père », dit sa mère. L'après-midi, Léa se ({cnums[4]})___ et lit un roman en français avec un dictionnaire. Le soir, elle pense : « J'ai pensé aux morts, mais j'ai aussi ({cnums[5]})___ ma famille vivante. » Demain, les cours ({cnums[6]})___ : les vacances sont finies. Mais Léa garde une phrase de son roman et elle l'({cnums[7]})___ dans son cahier.", 21.5)
bf.expl("Opciones:")
for n, opts in zip(cnums, [
    "A. lundi · B. samedi · C. dimanche",
    "A. cimetière · B. marché · C. cinéma",
    "A. roses · B. chrysanthèmes · C. tulipes",
    "A. table · B. tombe · C. porte",
    "A. lève · B. couche · C. repose",
    "A. retrouve · B. retrouvé · C. retrouver",
    "A. reprend · B. reprendre · C. reprennent",
    "A. écrit · B. écrivent · C. écris",
]):
    bf.para(f"{n}. {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B　CHOIX MULTIPLE　OPCIONES", 23)
mcq = [
    ("A2", "B", "7 h 30 = et demie", "Il est sept heures ___. (7 h 30) A. et quart · B. et demie · C. moins le quart"),
    ("A2", "A", "nous → allons", "Dimanche, nous ___ reculer les horloges. A. allons · B. allez · C. vont"),
    ("B1", "B", "s'intéresser aux (à + les)", "Elle s'intéresse ___ sondages. A. à les · B. aux · C. des"),
    ("B2", "B", "si + imparfait → conditionnel j'irais", "Si j'étais libre dimanche, je ___ au cimetière. A. irai · B. j'irais · C. je vais"),
    ("B2", "A", "sujeto ce résultat, 3.ª persona singular → semble", "À mon avis, ce résultat ___ très surprenant. A. semble · B. sembler · C. semblant"),
    ("B1", "B", "futuro: sera (a las 3 serán las 2)", "À trois heures, il ___ deux heures. A. est · B. sera · C. était"),
    ("A2", "A", "el mandato presidencial dura cinco años", "Le président est élu pour ___ ans. A. cinq · B. sept · C. dix-huit"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "单选", k, nt, body, size=20.5)

# ---- C. reading ----
bf.head("C　LECTURE　LECTURA", 24)
bf.para("Samedi soir, la famille Martin regarde un film. À deux heures du matin, tout le monde dort. Mais quelque chose se prépare... À trois heures, les horloges du pays reculent : il est deux heures. La nuit dure une heure de plus ! Le dimanche matin, Monsieur Martin se réveille content. « On a bien dormi ! » dit-il. Sa fille rit : « Papa, tu as dormi une heure de plus, mais le chat, lui, demande son petit déjeuner à l'ancienne heure ! » Le soir, la nuit tombera plus tôt : à dix-huit heures, il fera déjà noir — l'hiver arrive.", 21.5)
read_qs = [
    ("A2", "C", "en el texto: les horloges reculent", "Que se passe-t-il à trois heures ? A. Le film commence · B. La famille se réveille · C. Les horloges reculent"),
    ("A2", "A", "durmió una hora más", "Pourquoi M. Martin a-t-il bien dormi ? A. Il a dormi une heure de plus · B. Le film était court · C. Le chat était calme"),
    ("B1", "B", "el gato pide el desayuno a la hora antigua", "Le chat demande son petit déjeuner... A. à midi · B. à l'ancienne heure · C. plus tard"),
    ("B1", "A", "con el horario de invierno anochece antes", "Le dimanche à 18 heures... A. il fait nuit · B. il fait jour · C. il neige"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "阅读理解", k, nt, body, size=20.5)

# ---- D. sentence building ----
bf.head("D　PHRASES　CONSTRUIR FRASES", 22)
d_items = [
    ("A2", "Les Français vont reculer les horloges dimanche.", "aller + infinitivo (futur proche)",
     "Futur proche : « Les Français reculent les horloges dimanche. » → ___"),
    ("B2", "Si tu venais dimanche, tu verrais la cérémonie.", "si + imperfecto: venais",
     "Hypothèse : « Si tu (venir) dimanche, tu verrais la cérémonie. »"),
    ("B1", "Elle a posé les fleurs sur la tombe.", "passé composé: a + participio pasado",
     "Passé composé : « Elle (poser) les fleurs sur la tombe. »"),
    ("B2", "Selon moi, les sondages sont utiles.", "selon moi = en mi opinión",
     "Opinion : « ___ moi, les sondages sont utiles. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "完成句子", k, nt, body, size=20.5)

# ---- E. translation ----
bf.head("E　TRADUCTION　TRADUCCIÓN", 23)
e_items = [
    ("B2", "Leer una encuesta ya es participar en política.", "lire un sondage = leer una encuesta",
     "Traduce al español: « Lire un sondage, c'est déjà faire de la politique. »"),
    ("A2", "Il est plus grand que son frère.", "comparativo: plus grand que",
     "Traduce al francés: Es más alto que su hermano."),
    ("B1", "Les élèves sont en vacances depuis samedi.", "être en vacances + depuis",
     "Traduce al francés: Los alumnos están de vacaciones desde el sábado."),
    ("B1", "Ce soir, nous allons reculer les horloges d'une heure.", "futur proche + reculer",
     "Traduce al francés: Esta noche vamos a atrasar los relojes una hora."),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "翻译", k, nt, body, size=20.5)

# ---- F. matching ----
bf.head("F　LES MOTS　VOCABULARIO", 24)
bf.match_set("B1", "词汇配对",
             ["un scrutin", "devancer", "un cimetière", "une console"],
             ["un vote organisé", "passer devant quelqu'un", "le lieu où sont les tombes",
              "une machine de jeu vidéo"],
             ["a", "b", "c", "d"],
             ["scrutin = una votación a", "devancer = adelantar b", "cimetière = un cementerio c", "console = una consola d"],
             instr="Une")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "samedi", "el 24 de octubre es sábado"),
    ("A2", "fleurs (des chrysanthèmes)", "comprar flores para el cementerio"),
    ("B1", "prenez", "vous prenez = ustedes toman, usted toma"),
    ("A2", "recule", "on recule les horloges = atrasamos los relojes"),
    ("A2", "voyage", "Bon voyage ! = ¡Buen viaje!"),
]
gnums = [reg_ex(lv, "对话补全", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　DIÁLOGO", 24)
bf.para(f"— Bonjour madame, un billet pour Lyon, s'il vous plaît. — Pour quel jour ? — Pour ({gnums[0]})___, le 24 octobre : je pars chez mes grands-parents pour la Toussaint. Je dois aussi acheter des ({gnums[1]})___ pour le cimetière. — Les chrysanthèmes sont à gauche. Vous ({gnums[2]})___ le train de 9 h 15 ? — Oui. Il arrive à quelle heure à Lyon ? — À 11 h 30. — Ah oui, cette nuit, on ({gnums[3]})___ les horloges d'une heure. Je vais dormir plus ! Voici vos billets. Bon ({gnums[4]})___ ! — Merci, au revoir !", 21.5)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "写作", "Pregunta abierta — los puntos están en el recuadro de escritura y el modelo, en el recuadro MODÈLE de esta página", "se puntúa según los puntos")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　ÉCRITURE　ESCRITURA", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Écrivez un petit texte (80 à 100 mots) : « Mes vacances de la Toussaint ». Racontez : où, avec qui, une fleur, un repas, un livre. Les meilleurs textes paraîtront dans le VOL.3 (page 7, « Le courrier des lecteurs »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "Escribe en francés de 80 a 100 palabras: «Mis vacaciones de Todos los Santos». Cuenta: dónde, con quién, una flor, una comida y un libro.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, "MODÈLE　MODELO", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Pendant les vacances, je suis allé chez mes grands-parents, à la campagne. Le matin, nous avons marché dans la forêt aux feuilles rouges et jaunes. Le dimanche 25 octobre, j'ai reculé ma montre d'une heure... et j'ai dormi très longtemps ! Le 1er novembre, nous sommes allés au cimetière avec des chrysanthèmes blancs pour la tombe de mon arrière-grand-père. Le soir, ma grand-mère a préparé une soupe délicieuse. Après le repas, nous avons regardé de vieilles photos de famille, et j'ai lu vingt pages de mon roman français.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "RÉPONSES　TODAS LAS RESPUESTAS CON NOTAS (PÁGINAS 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
# Notes printed on this page = exactly the set printed in the core edition,
# computed from the core registry (its rule was: page 8 always, or note of
# 10 chars or fewer, or chart/error-correction types). Reproduced as an
# explicit set so this edition prints the same notes for the same exercises.
PRINT_NOTES = {1, 4, 17, 22, 26, 33, 35, 41, 44, 46, 47, 55, 56, 65, 71, 72, 73, 74, 80, 81, 82, 83, 84, 85, 92, 97, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145}
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— PÁGINA {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and e["n"] in PRINT_NOTES:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
