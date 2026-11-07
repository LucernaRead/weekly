# -*- coding: utf-8 -*-
"""W45 FR core VOL.3 — P8 (battery 42 + writing + all keys from REG)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-it/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCICES & RÉPONSES · ESERCIZI E RISPOSTE", "Le Lucerna", "VALUTAZIONE · ÉVALUATION · RISPOSTE IN FONDO A QUESTA PAGINA")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze ----
cloze_defs = [
    ("A2", "C", "L'8 novembre 2026 è domenica"),
    ("A2", "A", "A Nanterre per la finale"),
    ("A2", "B", "I finalisti si conoscono solo sabato sera"),
    ("A2", "B", "Contesto di degustazione (un régal) → goûté"),
    ("B1", "C", "se promener = passeggiare"),
    ("B1", "A", "avoir + participio goûté (senza accordo)"),
    ("B1", "C", "les finales (plurale) → ont lieu"),
    ("A2", "A", "elle écrit = lei scrive"),
]
cnums = [reg_ex(lv, "Completamento testo", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · TEXTE À TROUS · COMPLETA", 24)
bf.para(f"Léa a seize ans. Le ({cnums[0]})___ 8 novembre, elle se lève tôt : c'est le jour des finales. Avec son frère, elle va à ({cnums[1]})___ pour voir le tennis. « On ne connaît pas encore les ({cnums[2]})___ », dit son frère. Le soir, Léa raconte : « À Port-en-Bessin, on a ({cnums[3]})___ des coquilles, un régal ! » Le festival ({cnums[4]})___ dans Paris. Léa a ({cnums[5]})___ la musique. Les finales ({cnums[6]})___ dimanche, et elle l'({cnums[7]})___ dans son cahier.", 20)
bf.bridge("Opzioni:")
for n, opts in zip(cnums, [
    "A. lundi · B. samedi · C. dimanche",
    "A. Nanterre · B. Plailly · C. Dieppe",
    "A. vainqueurs · B. finalistes · C. spectateurs",
    "A. acheté · B. goûté · C. vendu",
    "A. promène · B. promènent · C. se promène",
    "A. goûté · B. goûtée · C. goûter",
    "A. a lieu · B. ont lieus · C. ont lieu",
    "A. écrit · B. écrivent · C. écris",
]):
    bf.para(f"{n}. {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B · CHOIX MULTIPLE · OPZIONI", 24)
mcq = [
    ("A2", "B", "7 nov. = sabato (ultimo evento notturno)", "La dernière nocturne a lieu... A. vendredi 6 · B. samedi 7 · C. dimanche 8"),
    ("A2", "A", "nous → allons", "Lundi, nous ___ reprendre les cours. A. allons · B. allez · C. vont"),
    ("B1", "B", "s'intéresser aux (à + les)", "Elle s'intéresse ___ festivals. A. à les · B. aux · C. des"),
    ("B2", "B", "si + imparfait → conditionnel présent; j' è je davanti a vocale (elisione)", "Si j'étais libre dimanche, j'___ à Nanterre. A. irai · B. irais · C. vais"),
    ("B2", "A", "Soggetto ce programme (3ª persona singolare) → semble", "À mon avis, ce programme ___ très riche. A. semble · B. sembler · C. semblant"),
    ("B1", "B", "Futuro aura lieu (finale domenica)", "Dimanche, la finale ___ à Nanterre. A. a lieu · B. aura lieu · C. avait lieu"),
    ("A2", "A", "Tutte e tre le zone ricominciano lo stesso giorno", "Les trois zones reprennent... A. le même jour · B. à des jours différents · C. en décembre"),
    ("B1", "C", "Festa delle capesante il 7–8 novembre", "Le Goût du Large, c'est... A. 14–15 nov. · B. 31 oct. · C. 7–8 nov."),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "Scelta multipla", k, nt, body, size=20, gap=6)

# ---- C. reading ----
bf.head("C · LECTURE · LETTURA", 24)
bf.para("Samedi soir, la famille Martin prépare son week-end. Samedi 7 novembre, ils iront à Plailly pour la dernière nocturne : de 19 heures à 1 heure du matin, avec un badge repousse-monstres pour le petit Léo. Dimanche 8, ils regarderont les finales à la télévision, puis ils goûteront des coquilles de Port-en-Bessin. « Trois finales en un week-end ! » dit Monsieur Martin. Le soir, Léo dormira tôt : demain, c'est l'école.", 20)
read_qs = [
    ("A2", "C", "Evento notturno dalle 19 all'1", "La nocturne dure de... A. 10 h à 19 h · B. 18 h à 20 h · C. 19 h à 1 h"),
    ("A2", "A", "Il distintivo è per il piccolo Léo, contro i mostri", "Le badge repousse-monstres, c'est pour... A. le petit Léo · B. le père · C. la mère"),
    ("B1", "B", "Domenica: prima la finale, poi le capesante", "Dimanche, la famille... A. va à Plailly · B. regarde les finales puis goûte des coquilles · C. reste au lit"),
    ("B1", "A", "Domenica sera a letto presto, perché lunedì c'è scuola", "Dimanche soir, Léo dort tôt parce que... A. demain, c'est l'école · B. il est malade · C. il pleut"),
    ("B2", "A", "Lunedì è giorno di scuola (dopo le vacanze, lunedì normale)", "Lundi, Léo... A. retourne à l'école · B. reste en vacances · C. va à Plailly"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "Comprensione", k, nt, body, size=20, gap=6)

# ---- D. sentence building ----
bf.head("D · PHRASES · COSTRUISCI FRASI", 24)
d_items = [
    ("A2", "Les élèves vont reprendre les cours lundi.", "aller + infinito (futur proche)",
     "Futur proche : « Les élèves reprennent les cours lundi. » → ___"),
    ("B2", "Si tu venais samedi, tu verrais la nocturne.", "si + imparfait (venais)",
     "Hypothèse : « Si tu (venir) samedi, tu verrais la nocturne. »"),
    ("B1", "Elle a goûté les coquilles à Port-en-Bessin.", "passé composé: a + participio",
     "Passé composé : « Elle (goûter) les coquilles à Port-en-Bessin. »"),
    ("B2", "Selon moi, les finales sont excitantes.", "selon moi = secondo me",
     "Opinion : « ___ moi, les finales sont excitantes. »"),
    ("B1", "Il est prévu que le Sénat examine le texte lundi.", "il est prévu que + congiuntivo",
     "Subjonctif : « Il est prévu que le Sénat (examiner) le texte lundi. » → ___"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "Completamento", k, nt, body, size=20, gap=6)

# ---- E. translation ----
bf.head("E · TRADUCTION · TRADUZIONE", 24)
e_items = [
    ("B2", "Leggere un programma è già capire la Francia.", "lire un programme = leggere un programma",
     "Traduci in italiano: « Lire un programme, c'est déjà comprendre la France. »"),
    ("A2", "Il court plus vite que son frère.", "comparativo: plus vite + court",
     "Traduci in francese: Corre più veloce di suo fratello."),
    ("B1", "Les élèves sont en vacances depuis le 17 octobre.", "être en vacances + depuis",
     "Traduci in francese: Gli studenti sono in vacanza dal 17 ottobre."),
    ("B1", "Ce soir, nous allons préparer nos cartables.", "futur proche + préparer",
     "Traduci in francese: Stasera prepariamo le cartelle."),
    ("B2", "On ne connaît pas encore les finalistes.", "ne...pas encore = non ancora",
     "Traduci in francese: Non si conoscono ancora i finalisti."),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "Traduzione", k, nt, body, size=20, gap=6)

# ---- F. matching ----
bf.head("F · LES MOTS · VOCABOLARIO", 24)
bf.match_set("B1", "Abbinamento",
             ["un tournoi", "une nocturne", "un budget", "une coquille", "un festival"],
             ["une compétition avec plusieurs matchs", "une soirée qui dure jusqu'à la nuit",
              "le plan des dépenses de l'État", "le coquillage fêté à Port-en-Bessin",
              "plusieurs concerts en une semaine"],
             ["a", "b", "c", "d", "e"],
             ["tournoi=torneo a", "nocturne=evento notturno b", "budget=bilancio c", "coquille=capasanta d", "festival=festival e"],
             instr="Abbina", gap=6)

# ---- G. dialogue ----
dlg_defs = [
    ("A2", "samedi", "Il 7 novembre è sabato"),
    ("A2", "coquilles (des coquilles Saint-Jacques)", "Al mercato comprare capesante"),
    ("B1", "goûter", "goûter = assaggiare (infinito)"),
    ("A2", "recette", "à la portaise è un modo di cucinare"),
    ("A2", "week-end", "Bon week-end ! = Buon fine settimana!"),
]
gnums = [reg_ex(lv, "Completamento dialogo", k, nt) for lv, k, nt in dlg_defs]
bf.head("G · DIALOGUE · DIALOGO", 24)
bf.para(f"— Bonjour madame, c'est le marché du Goût du Large ? — Oui ! — Pour ({gnums[0]})___, le 7 novembre : je veux des ({gnums[1]})___ pour ma famille. — Goûtez celle-ci ! Vous voulez les ({gnums[2]})___ à la portaise ? — Oui, donnez-moi votre ({gnums[3]})___. — Voilà. Bon ({gnums[4]})___ ! — Merci !", 20)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "Scrittura", "Domanda aperta — i punti sono nel riquadro di scrittura e il modello è nel riquadro MODÈLE di questa pagina", "si valuta in base ai punti")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · ÉCRITURE · SCRITTURA", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Écrivez un petit texte (80 à 100 mots) : « Mon week-end du 7–8 novembre ». Racontez : un match, une fête, un plat. Les meilleurs textes paraîtront dans le VOL.4 (page 7, « Le courrier des lecteurs »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "Scrivete in francese 80–100 parole: il mio fine settimana del 7–8 novembre. Descrivete una partita, una festa, un piatto. I migliori testi appariranno nel VOL.4 (pagina 7, « Le courrier des lecteurs »).", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 288, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MODÈLE · MODELLO", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Samedi 7 novembre, j'ai regardé les demi-finales du Masters à la télévision : quelle ambiance ! Le soir, nous avons fêté la dernière nocturne avec des amis, déguisés en fantômes. Dimanche 8, nous avons goûté des coquilles Saint-Jacques à la portaise, achetées au marché de Port-en-Bessin. Le matin, nous avons marché au bord de la mer et nous avons acheté des fleurs pour ma grand-mère. Le soir, nous avons écouté de la musique et j'ai lu vingt pages de mon roman français. C'était un week-end parfait.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "RÉPONSES · TUTTE LE RISPOSTE CON NOTE (PAGINE 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")
from itertools import groupby
PRINT_NOTES = [1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— PAGINA {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and e["n"] in PRINT_NOTES:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
