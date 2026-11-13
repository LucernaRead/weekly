# -*- coding: utf-8 -*-
"""W47 FR core VOL.4 — P8 (battery 42 + writing + all keys from REG).
Translation section: reader-language stems (E) -> French keys (frozen).
PRINT_NOTES: explicit set measured from the core P8 (see KIT); None
falls back to the W45 length rule for the first core measurement run."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

PRINT_NOTES = [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17, 19, 20, 21, 22, 26, 28, 30, 31, 32, 33, 34, 38, 40, 41, 42, 43, 44, 45, 46, 47, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 77, 78, 79, 80, 81, 82, 83, 84, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]

# ---- D5 fix (W47 fix round): level chips for items that Flow.ex() never
# draws one for — the cloze option lines (Q109-116), the dialogue
# (Q145-149, one shared paragraph, no option lines) and writing (Q150).
# Both helpers DRAW ONLY: they never touch REG, so numbering is unchanged.
def badge_opt(flow, level, n, opts, size=19.5, lh=1.32, gap=2):
    """One cloze option line with its own level chip: chip at the row
    head, the option-line text shifted right by 72px.
    Under the text-export stubs (no _fit/_ph: export47.py) this only
    records the option line, exactly as the old bf.para call did."""
    body = f"{n}. {opts}"
    if not hasattr(flow, "_fit"):
        flow.p.para(flow.x, flow.y + size, body, size, "sans", False, INK, 422.5, lh)
        return flow.y
    w = flow.w - 72
    lines = wrap(body, "sans", False, size, w)
    h = size + len(lines) * size * lh
    flow._fit(h + gap)
    x, y = flow.x, flow.y
    chip(flow.p, x, y, level)
    flow.y = flow.p.para(x + 72, y + size, body, size, "sans", False, INK, w, lh) + gap
    return flow.y

def badge_strip(flow, items, size=19.5, gap=9):
    """Row(s) of level chips, one per (level, n): chip + 'N.' per item,
    packed 3 per row. For items that share one paragraph (dialogue).
    Under the text-export stubs this draws nothing (chips carry no text
    for the export; the numbers already sit in the dialogue paragraph)."""
    if not hasattr(flow, "_fit"):
        return flow.y
    widths = [60 + 6 + text_w(f"{n}.", "sans", True, size) for _lv, n in items]
    rows, cur, curw = [], [], 0.0
    for it, w in zip(items, widths):
        if cur and curw + 14 + w > flow.w:
            rows.append(cur); cur, curw = [], 0.0
        cur.append((it, w)); curw += (14 if cur else 0) + w
    if cur:
        rows.append(cur)
    h = len(rows) * 30 + (len(rows) - 1) * 8
    flow._fit(h + gap)
    x0, y0 = flow.x, flow.y
    for ri, row in enumerate(rows):
        x = x0; y = y0 + ri * 38
        for (lv, n), _w in row:
            chip(flow.p, x, y, lv)
            flow.p.text(x + 66, y + 22, f"{n}.", size, "sans", True, OLIVE)
            x += _w + 14
    flow.y = y0 + h + gap
    return flow.y

CURPAGE[0] = 8
p = BSPage4()
p.band(E["band_p8"], "Le Lucerna", E["band_p8_sub"])

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze ----
cloze_defs = [
    ("A2", "A", E["n_cloze1"]),
    ("A2", "B", E["n_cloze2"]),
    ("A2", "A", E["n_cloze3"]),
    ("A2", "B", E["n_cloze4"]),
    ("B1", "A", E["n_cloze5"]),
    ("B1", "A", E["n_cloze6"]),
    ("B1", "B", E["n_cloze7"]),
    ("A2", "A", E["n_cloze8"]),
]
cnums = [reg_ex(lv, "完形填空", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　TEXTE À TROUS　" + E["p8_cloze"], 24)
bf.para(f"Théo a dix-sept ans. Le ({cnums[0]})___ 16 novembre, il se lève tôt : les finales de Turin approchent. Avec sa classe, il va à ({cnums[1]})___ pour la fête du beaujolais nouveau. « Les ({cnums[2]})___ de Turin seront dans le VOL.5 », dit son professeur. Le soir, Théo raconte : « À Beaujeu, on a ({cnums[3]})___ le vin primeur, un régal ! » Le cinéma ({cnums[4]})___ seize films mercredi. Théo a ({cnums[5]})___ les bandes-annonces. Les Bleus ({cnums[6]})___ dimanche, et il l'({cnums[7]})___ dans son cahier.", 21)
bf.bridge(E["p8_options"])
for n, (lv, _k, _nt), opts in zip(cnums, cloze_defs, [
    "A. lundi　B. samedi　C. dimanche",
    "A. Paris　B. Beaujeu　C. Turin",
    "A. résultats　B. finalistes　C. spectateurs",
    "A. acheté　B. goûté　C. vendu",
    "A. propose　B. proposent　C. se tient",
    "A. aimé　B. aimée　C. aimer",
    "A. joue　B. jouent　C. jouer",
    "A. écrit　B. écrivent　C. écris",
]):
    badge_opt(bf, lv, n, opts)

# ---- B. single choice ----
bf.head("B　CHOIX MULTIPLE　" + E["p8_mcq"], 24)
mcq = [
    ("A2", "A", E["n_mcq_b1"], "Turin commence... A. dimanche 15　B. lundi 16　C. mercredi 18"),
    ("A2", "A", E["n_mcq_b2"], "Le beaujolais nouveau, c'est... A. un vin primeur　B. un fromage　C. un film"),
    ("B1", "B", E["n_mcq_b3"], "Le Sénat vote sur la Sécu... A. lundi 16　B. mercredi 18　C. jeudi 19"),
    ("B2", "B", E["n_mcq_b4"], "Si j'étais libre dimanche, j'___ à Turin. A. irai　B. irais　C. vais"),
    ("B2", "A", E["n_mcq_b5"], "À mon avis, ce programme ___ très riche. A. semble　B. sembler　C. semblant"),
    ("B1", "B", E["n_mcq_b6"], "Dimanche, la France ___ la Turquie à Bordeaux. A. reçoivent　B. reçoit　C. recevoir"),
    ("A2", "A", E["n_mcq_b7"], "Hunger Games, c'est... A. un prequel　B. un match　C. une foire"),
    ("B1", "C", E["n_mcq_b8"], "Le beaujolais nouveau arrive... A. le 11 nov.　B. le 15 nov.　C. le 19 nov."),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "单选", k, nt, body, size=20, gap=5)  # W47 fix round: gap 11->5 (D5 chips add ~155px to the battery; tighter spacing keeps the battery + keys + Hiroshige inside the page)

# ---- C. reading ----
bf.head("C　LECTURE　" + E["p8_read"], 24)
bf.para("Dimanche 22 novembre, la famille Martin reste à la maison. Le matin, ils lisent le journal : Alcaraz a gagné Paris, le Sénat a voté mercredi. L'après-midi, ils regardent les finales de Turin à la télévision. Le soir, ils regardent Marseille – Le Mans, à 20 h 45. « Voter, fêter, jouer ! » dit Monsieur Martin. Le soir, les enfants dorment tôt : lundi, c'est l'école.", 21)
read_qs = [
    ("A2", "A", E["n_read1"], "Le matin, la famille lit... A. le journal　B. un roman　C. une bande-annonce"),
    ("A2", "A", E["n_read2"], "L'après-midi, la famille regarde... A. les finales de Turin　B. un film　C. les Sarmentelles"),
    ("B1", "A", E["n_read3"], "Marseille – Le Mans, c'est à... A. 20 h 45　B. 17 h 15　C. 15 h"),
    ("B1", "A", E["n_read4"], "Le soir, les enfants dorment tôt parce que... A. lundi, c'est l'école　B. il pleut　C. ils sont malades"),
    ("B2", "A", E["n_read5"], "Lundi, les enfants... A. retournent à l'école　B. restent à la maison　C. vont à Turin"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "阅读理解", k, nt, body, size=20, gap=5)  # W47 fix round: gap 11->5 (see B section)

# ---- D. sentence building ----
bf.head("D　PHRASES　" + E["p8_sent"], 24)
d_items = [
    ("A2", "Le Sénat va voter mercredi.", E["n_d1"],
     "Futur proche : « Le Sénat vote mercredi. » → ___"),
    ("B2", "Si tu venais dimanche, tu verrais les finales.", E["n_d2"],
     "Hypothèse : « Si tu (venir) dimanche, tu verrais les finales. »"),
    ("B1", "Il a goûté le beaujolais à Beaujeu.", E["n_d3"],
     "Passé composé : « Il (goûter) le beaujolais à Beaujeu. »"),
    ("B2", "Selon moi, la semaine est bien remplie.", E["n_d4"],
     "Opinion : « ___ moi, la semaine est bien remplie. »"),
    ("B1", "Il est prévu que le Sénat examine le texte mercredi.", E["n_d5"],
     "Subjonctif : « Il est prévu que le Sénat (examiner) le texte mercredi. » → ___"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "完成句子", k, nt, body, size=20, gap=5)  # W47 fix round: gap 11->5 (see B section)

# ---- E. translation (reader language -> French) ----
bf.head("E　TRADUCTION　" + E["p8_trans"], 24)
e_items = [
    ("B2", "Regarder une finale, c'est déjà apprendre le français.", E["n_e1"], E["stem_e1"]),
    ("A2", "Il court plus vite que son frère.", E["n_e2"], E["stem_e2"]),
    ("B1", "Nous suivons le vote du Sénat depuis lundi.", E["n_e3"], E["stem_e3"]),
    ("B1", "Ce soir, nous allons préparer nos affaires.", E["n_e4"], E["stem_e4"]),
    ("B2", "On ne connaît pas encore les résultats.", E["n_e5"], E["stem_e5"]),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "翻译", k, nt, body, size=20, gap=5)  # W47 fix round: gap 11->5 (see B section)

# ---- F. matching ----
bf.head("F　LES MOTS　" + E["p8_words"], 24)
bf.match_set("B1", "词汇配对",
             ["un sénateur", "un vainqueur", "un tirage", "un vin primeur", "un déchet"],
             ["un élu du Sénat", "le joueur qui a gagné le tournoi",
              "le sort qui fait les groupes", "un vin de l'année, très jeune",
              "ce qu'on jette"],
             ["a", "b", "c", "d", "e"],
             [E["m_p8a"], E["m_p8b"], E["m_p8c"], E["m_p8d"], E["m_p8e"]],
             instr=E["instr_match"])

# ---- G. dialogue ----
dlg_defs = [
    ("A2", "des billets", E["n_g1"]),
    ("A2", "deux", E["n_g2"]),
    ("B1", "quelle heure", E["n_g3"]),
    ("A2", "devant le", E["n_g4"]),
    ("A2", "film", E["n_g5"]),
]
gnums = [reg_ex(lv, "对话补全", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　" + E["p8_dialogue"], 24)
badge_strip(bf, [(lv, n) for n, (lv, _k, _nt) in zip(gnums, dlg_defs)])
bf.para(f"— Tu vas au cinéma mercredi ? — Oui, pour voir Hunger Games. — Tu as pris ({gnums[0]})___ ? — Oui, ({gnums[1]})___ billets. — La séance est à ({gnums[2]})___ ? — À 20 heures. — On se retrouve ({gnums[3]})___ cinéma ? — Oui, à 19 h 30. Bon ({gnums[4]})___ ! — Merci !", 21)
bf.end_report()
print("P8 battery flow ends col", bf.ci, "y=", bf.y)

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "写作", E["writing_key"], E["writing_note"])
wx, ww = span_x(0, 2)
chip(p, wx, wy, "B1")  # D5 fix: writing (Q150) gets its own level chip
p.text(wx + 72, wy + 26, "H　ÉCRITURE　" + E["p8_writing"], 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Écrivez un petit texte (80 à 100 mots) : « Mon dimanche 22 novembre ». Racontez : une finale, une promenade, un film. Les meilleurs textes paraîtront dans le VOL.5 (page 7, « Le courrier des lecteurs »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, E["writing_instr"], 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 288, fill=BOX)
p.text(mx2 + 22, wy + 38, "MODÈLE　" + E["p8_modele"], 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Dimanche 22 novembre, je me suis levé tard : c'était le jour des finales de Turin. Le matin, j'ai lu le journal : Alcaraz a gagné Paris, le Sénat a voté mercredi. L'après-midi, nous avons regardé les finales à la télévision, avec des chips. Le soir, nous avons regardé Marseille – Le Mans, à 20 h 45. J'ai noté les mots nouveaux dans mon cahier : un vainqueur, un tirage, une finale. Lundi, je suis retourné à l'école avec une photo de Méliès dans la tête. C'était une semaine en trois temps : voter, fêter, jouer.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, E["head_keys"], 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
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
    kf.para("　".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
print("P8 keys flow ends col", kf.ci, "y=", kf.y)
# ---- Hiroshige image under the keys flow, col 3 (measured slot) ----
if kf.y + 10 + 300 + 80 <= 2560:
    image(p, "hiroshige-maple.jpg", COLX[3], kf.y + 10, CW, 300)
    caption(p, COLX[3], kf.y + 310, CW, "Novembre, près d'Edo : les feuilles rouges annoncent les soirées de lecture.",
            "Utagawa Hiroshige (1797-1858), estampe, domaine public　LACMA")
    print("P8 hiroshige image placed at y=", kf.y + 10)
else:
    print("  !! P8 HIROSHIGE NOSPACE: keys end y=", kf.y)
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
