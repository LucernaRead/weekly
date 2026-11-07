# -*- coding: utf-8 -*-
"""W46 FR core VOL.4 — P8 (battery 42 + writing + all keys from REG).
Translation section: reader-language stems (E) -> French keys (frozen).
PRINT_NOTES: explicit set measured from the core P8 (see KIT); None
falls back to the W45 length rule for the first core measurement run."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-fr-ko/svg")
os.makedirs(OUT, exist_ok=True)

PRINT_NOTES = [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17, 19, 20, 21, 22, 26, 28, 30, 31, 32, 33, 34, 38, 40, 41, 42, 43, 44, 45, 46, 47, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 77, 78, 79, 80, 81, 82, 83, 84, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]

CURPAGE[0] = 8
p = BSPage4()
p.band(E["band_p8"], "Le Lucerna", E["band_p8_sub"])

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze ----
cloze_defs = [
    ("A2", "A", E["n_cloze1"]),
    ("A2", "A", E["n_cloze2"]),
    ("A2", "A", E["n_cloze3"]),
    ("A2", "B", E["n_cloze4"]),
    ("B1", "C", E["n_cloze5"]),
    ("B1", "A", E["n_cloze6"]),
    ("B1", "B", E["n_cloze7"]),
    ("A2", "A", E["n_cloze8"]),
]
cnums = [reg_ex(lv, "完形填空", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · TEXTE À TROUS · " + E["p8_cloze"], 24)
bf.para(f"Théo a dix-sept ans. Le ({cnums[0]})___ 9 novembre, il se lève tôt : le Sénat ouvre la discussion. Avec sa classe, il va à ({cnums[1]})___ pour la cérémonie du 11 novembre. « Les ({cnums[2]})___ du Masters seront dans le VOL.5 », dit son professeur. Le soir, Théo raconte : « À Dieppe, on a ({cnums[3]})___ des harengs, un régal ! » Paris Photo ({cnums[4]})___ au Grand Palais. Théo a ({cnums[5]})___ les photos. Les Bleus ({cnums[6]})___ dimanche, et il l'({cnums[7]})___ dans son cahier.", 21)
bf.bridge(E["p8_options"])
for n, opts in zip(cnums, [
    "A. lundi · B. samedi · C. dimanche",
    "A. Paris · B. Dieppe · C. Turin",
    "A. résultats · B. finalistes · C. spectateurs",
    "A. acheté · B. goûté · C. vendu",
    "A. tient · B. tiennent · C. se tient",
    "A. aimé · B. aimée · C. aimer",
    "A. joue · B. jouent · C. jouer",
    "A. écrit · B. écrivent · C. écris",
]):
    bf.para(f"{n}. {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B · CHOIX MULTIPLE · " + E["p8_mcq"], 24)
mcq = [
    ("A2", "B", E["n_mcq_b1"], "La discussion au Sénat commence... A. dimanche 8 · B. lundi 9 · C. mercredi 11"),
    ("A2", "A", E["n_mcq_b2"], "Le 11 novembre, on dépose... A. une gerbe · B. un billet · C. un ballon"),
    ("B1", "B", E["n_mcq_b3"], "Le Soldat inconnu repose... A. à Dieppe · B. sous l'Arc de Triomphe · C. à Turin"),
    ("B2", "B", E["n_mcq_b4"], "Si j'étais libre dimanche, j'___ à Dieppe. A. irai · B. irais · C. vais"),
    ("B2", "A", E["n_mcq_b5"], "À mon avis, ce programme ___ très riche. A. semble · B. sembler · C. semblant"),
    ("B1", "B", E["n_mcq_b6"], "Dimanche, la France ___ la Turquie à Bordeaux. A. reçoivent · B. reçoit · C. recevoir"),
    ("A2", "A", E["n_mcq_b7"], "Paris Photo, c'est... A. un salon de photographie · B. un match · C. une foire aux harengs"),
    ("B1", "C", E["n_mcq_b8"], "Le beaujolais nouveau arrive... A. le 11 nov. · B. le 15 nov. · C. le 19 nov."),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "单选", k, nt, body, size=20)

# ---- C. reading ----
bf.head("C · LECTURE · " + E["p8_read"], 24)
bf.para("Samedi matin, la famille Martin prend le train pour Dieppe. Samedi 14 novembre, à 10 heures, ils assistent à l'inauguration au pont Colbert, avec la Banda SP76. L'après-midi, ils goûtent des harengs grillés et ils visitent les quais. Dimanche 15, ils rentrent à Paris et ils regardent les Bleus à la télévision. « Mémoire le mercredi, saveurs le week-end ! » dit Monsieur Martin. Le soir, les enfants dorment tôt : lundi, c'est l'école.", 21)
read_qs = [
    ("A2", "C", E["n_read1"], "L'inauguration a lieu à... A. 9 h · B. 11 h · C. 10 h"),
    ("A2", "A", E["n_read2"], "La famille goûte... A. des harengs grillés · B. des bonbons · C. des gâteaux"),
    ("B1", "B", E["n_read3"], "Dimanche, la famille... A. reste à Dieppe · B. rentre et regarde les Bleus · C. va à Turin"),
    ("B1", "A", E["n_read4"], "Dimanche soir, les enfants dorment tôt parce que... A. lundi, c'est l'école · B. il pleut · C. ils sont malades"),
    ("B2", "A", E["n_read5"], "Lundi, les enfants... A. retournent à l'école · B. restent à Dieppe · C. vont au Sénat"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "阅读理解", k, nt, body, size=20)

# ---- D. sentence building ----
bf.head("D · PHRASES · " + E["p8_sent"], 24)
d_items = [
    ("A2", "Le Sénat va ouvrir la discussion lundi.", E["n_d1"],
     "Futur proche : « Le Sénat ouvre la discussion lundi. » → ___"),
    ("B2", "Si tu venais samedi, tu verrais la foire.", E["n_d2"],
     "Hypothèse : « Si tu (venir) samedi, tu verrais la foire. »"),
    ("B1", "Il a goûté les harengs à Dieppe.", E["n_d3"],
     "Passé composé : « Il (goûter) les harengs à Dieppe. »"),
    ("B2", "Selon moi, la semaine est bien remplie.", E["n_d4"],
     "Opinion : « ___ moi, la semaine est bien remplie. »"),
    ("B1", "Il est prévu que le Sénat examine le texte lundi.", E["n_d5"],
     "Subjonctif : « Il est prévu que le Sénat (examiner) le texte lundi. » → ___"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "完成句子", k, nt, body, size=20)

# ---- E. translation (reader language -> French) ----
bf.head("E · TRADUCTION · " + E["p8_trans"], 24)
e_items = [
    ("B2", "Lire un programme, c'est déjà comprendre la France.", E["n_e1"], E["stem_e1"]),
    ("A2", "Il court plus vite que son frère.", E["n_e2"], E["stem_e2"]),
    ("B1", "Les élèves sont en vacances depuis le 9 novembre.", E["n_e3"], E["stem_e3"]),
    ("B1", "Ce soir, nous allons préparer nos affaires.", E["n_e4"], E["stem_e4"]),
    ("B2", "On ne connaît pas encore les résultats.", E["n_e5"], E["stem_e5"]),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "翻译", k, nt, body, size=20)

# ---- F. matching ----
bf.head("F · LES MOTS · " + E["p8_words"], 24)
bf.match_set("B1", "词汇配对",
             ["un sénateur", "une gerbe", "un tirage", "une foire", "un bleuet"],
             ["un élu du Sénat", "un bouquet déposé en hommage",
              "une photographie imprimée", "une grande fête populaire",
              "la petite fleur bleue du 11 novembre"],
             ["a", "b", "c", "d", "e"],
             [E["m_p8a"], E["m_p8b"], E["m_p8c"], E["m_p8d"], E["m_p8e"]],
             instr=E["instr_match"])

# ---- G. dialogue ----
dlg_defs = [
    ("A2", "samedi", E["n_g1"]),
    ("A2", "harengs (des harengs)", E["n_g2"]),
    ("B1", "griller", E["n_g3"]),
    ("A2", "recette", E["n_g4"]),
    ("A2", "week-end", E["n_g5"]),
]
gnums = [reg_ex(lv, "对话补全", k, nt) for lv, k, nt in dlg_defs]
bf.head("G · DIALOGUE · " + E["p8_dialogue"], 24)
bf.para(f"— Bonjour madame, c'est la foire de Dieppe ? — Oui ! — Pour ({gnums[0]})___, le 14 novembre : je veux des ({gnums[1]})___ pour ma famille. — Goûtez celui-ci ! Vous voulez les ({gnums[2]})___ au grill ? — Oui, donnez-moi votre ({gnums[3]})___. — Voilà. Bon ({gnums[4]})___ ! — Merci !", 21)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "写作", E["writing_key"], E["writing_note"])
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · ÉCRITURE · " + E["p8_writing"], 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Écrivez un petit texte (80 à 100 mots) : « Mon mercredi 11 novembre ». Racontez : une cérémonie, un musée, une promenade. Les meilleurs textes paraîtront dans le VOL.5 (page 7, « Le courrier des lecteurs »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, E["writing_instr"], 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 288, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MODÈLE · " + E["p8_modele"], 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Mercredi 11 novembre, je me suis levé tôt : c'était un jour férié, mais un jour de mémoire. Le matin, j'ai regardé la cérémonie à la télévision : la flamme, la gerbe, la minute de silence. L'après-midi, nous avons marché jusqu'au monument aux morts de notre ville et nous avons lu les noms gravés dans la pierre. Le soir, nous avons mangé une soupe et j'ai lu vingt pages de mon roman français. Jeudi, je suis retourné à l'école avec une photo de Paris Photo dans la tête. C'était une semaine coupée en deux, mais une semaine pleine.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, E["head_keys"], 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(E["p8_sep"].format(pg=pg), 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        show = (e["n"] in PRINT_NOTES) if PRINT_NOTES else (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数"))
        if e["note"] and show:
            s += fmt_note(e["note"])
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
