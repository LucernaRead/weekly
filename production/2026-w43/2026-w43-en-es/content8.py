# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS　Ejercicios y respuestas", "The Lucerna", "FINAL TEST　Evaluación final　Las respuestas están al final de esta página")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "C", "el 31 de octubre es Halloween"),
    ("A2", "A", "carve = tallar la calabaza"),
    ("B1", "B", "neither...nor = ni... ni..."),
    ("A2", "A", "costume = el disfraz de Halloween"),
    ("A2", "B", "she, tercera persona → wears"),
    ("A2", "B", "con trick or treat se consiguen dulces"),
    ("B1", "A", "will + forma base: fall"),
    ("B1", "C", "be going to → is going"),
]
cnums = [reg_ex(lv, "Completar el texto", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　CLOZE　Completa el texto", 24)
bf.para(f"Maya is twelve. On Saturday, October 31, it is ({cnums[0]})___. In the morning, she helps her father ({cnums[1]})___ a pumpkin on the porch. « ({cnums[2]})___ rain nor cold can stop us », laughs her mother. In the evening, Maya puts on her ({cnums[3]})___ : she ({cnums[4]})___ a gold crown, like a Greek goddess. She takes her bag and goes from house to house : « Trick or treat ! » The neighbours give her ({cnums[5]})___. At nine o'clock, the street is quiet — and in the night, the clocks will ({cnums[6]})___ back : one more hour of sleep ! Tomorrow, Maya is ({cnums[7]})___ to sleep late, very late.", 21.5)
bf.expl("Opciones:")
for n, opts in zip(cnums, [
    "A. Christmas · B. Easter · C. Halloween",
    "A. carve · B. eat · C. sell",
    "A. Both · B. Neither · C. Also",
    "A. costume · B. uniform · C. pyjamas",
    "A. wear · B. wears · C. wearing",
    "A. money · B. candy · C. flowers",
    "A. fall · B. falls · C. falling",
    "A. goes · B. go · C. going",
]):
    bf.para(f"{n}. {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B　MULTIPLE CHOICE　Opción", 24)
mcq = [
    ("A2", "B", "9:15 = a quarter past nine", "The game starts at 9:15. In words : ... A. a quarter to nine · B. a quarter past nine · C. half past nine"),
    ("A2", "A", "we → get, forma base", "On Sunday, we ___ an extra hour of sleep. A. get · B. gets · C. getting"),
    ("B1", "B", "partido terminado: usa won", "The 76ers ___ the game 106–100. A. win · B. won · C. wins"),
    ("B1", "B", "than → comparativo: hotter", "Austin is ___ than Milwaukee in October. A. hot · B. hotter · C. hottest"),
    ("B2", "A", "despite + nombre: a pesar de la lluvia", "___ the rain, the parade went on all evening. A. Despite · B. Because · C. Unless"),
    ("B2", "A", "whether = si, en pregunta indirecta", "Nobody knows ___ the Brewers will win the Series. A. whether · B. what · C. who"),
    ("A2", "A", "algo pasado: usa el pasado opened", "Early voting in Texas ___ on Monday. A. opened · B. open · C. opens"),
    ("B1", "A", "be going to + forma base: cast", "She is going to ___ her ballot on Saturday. A. cast · B. casts · C. casted"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "Opción múltiple", k, nt, body, size=20.5)

# ---- C. reading ----
bf.head("C　READING　Comprensión", 24)
bf.para("On Monday morning, Rosa Delgado, a nurse from Houston, finished her night work at six o'clock. She did not go home to sleep. She drove to the early-voting place near the hospital and joined a short line. « On November 3, I work all day », she explains. « Today, I have time. » Ten minutes later, her ballot was in the box, and a sticker on her jacket said : I VOTED EARLY. By Friday, October 30, when early voting ends in Texas, millions of Texans will do the same.", 21.5)
read_qs = [
    ("A2", "B", "en el texto: a nurse from Houston", "Rosa is... A. a teacher · B. a nurse · C. a driver"),
    ("A2", "B", "el 3 de noviembre trabaja todo el día", "She voted early because on November 3 she... A. travels · B. works all day · C. sleeps"),
    ("B1", "A", "su pegatina decía I VOTED EARLY", "Her sticker said... A. I VOTED EARLY · B. VOTE ON TUESDAY · C. TEXAS FIRST"),
    ("B1", "B", "la votación anticipada en Texas termina el 30 de octubre", "Early voting in Texas ends on... A. October 19 · B. October 30 · C. November 3"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "Comprensión lectora", k, nt, body, size=20.5)

# ---- D. sentence building ----
bf.head("D　SENTENCES　A completar", 24)
d_items = [
    ("A2", "On Saturday, they are going to carve a pumpkin.", "are going to + forma base",
     "Be going to : « On Saturday, they (carve) a pumpkin. » → ___"),
    ("B1", "The Knicks raised their first banner since 1973.", "raise → raised (cambio regular)",
     "Past simple : « The Knicks (raise) their first banner since 1973. »"),
    ("B1", "scarier", "scary → scarier (la y pasa a i + er)",
     "Comparative : « My costume is ___ (scary) than yours. »"),
    ("B2", "Whether", "whether = si, en pregunta indirecta",
     "Whether : « ___ the parade will happen, nobody knows. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "Completar frases", k, nt, body, size=20.5)

# ---- E. translation ----
bf.head("E　TRANSLATION　Traducción", 24)
e_items = [
    ("B2", "Votar ya no es cosa de un solo día; es una temporada.", "no longer = ya no",
     "Translate : « Voting is no longer a day ; it is a season. »"),
    ("A2", "The 76ers won the game 106–100.", "win → won; el marcador: 106–100",
     "Traduce: Los 76ers ganaron por 106 a 100."),
    ("B1", "This year, early voting opened on Monday.", "open → opened; on Monday",
     "Traduce: Este año, la votación anticipada empezó el lunes."),
    ("B1", "Ninguno de los dos clubes ha ganado nunca la Serie Mundial.", "neither niega a los dos; has ever won, presente perfecto",
     "Translate : « Neither club has ever won the Series. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "Traducción", k, nt, body, size=20.5)

# ---- F. matching ----
bf.head("F　WORDS　Empareja", 24)
bf.match_set("B1", "Emparejar",
             ["a midterm", "an incumbent", "a margin", "turnout"],
             ["the number of people who vote", "an election in the middle of a president's term",
              "the person who holds the job now", "the difference between two results"],
             ["b", "c", "d", "a"],
             ["midterm = elecciones de mitad de mandato b", "incumbent = el titular del cargo c", "margin = la diferencia d", "turnout = la participación a"],
             instr="Empareja")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ID", "al votar se muestra un documento: ID"),
    ("A2", "line", "line = la fila (inglés americano)"),
    ("A2", "ballot", "ballot = la papeleta"),
    ("A2", "sticker", "sticker = la pegatina"),
    ("B1", "November", "el día de las elecciones es el 3 de noviembre"),
]
gnums = [reg_ex(lv, "Completar el diálogo", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　El diálogo", 24)
bf.para(f"— Good morning ! Is this the early-voting place ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long today ? — No, five minutes only. Yesterday it was very long ! — Good. It is my first early vote. What do I do with the ({gnums[2]})___ ? — Mark your choices, check them twice, then put it in the box. — Thank you. And the famous ({gnums[3]})___ ? Everybody has one on their jacket. — The sticker ! Here it is : « I VOTED ». Wear it with pride. — I will ! See you on ({gnums[4]})___ 3rd, in the results ! — Ha ! Have a good day.", 21.5)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "Escritura", "(pregunta abierta — el modelo está en el recuadro de escritura)", "se puntúa por puntos")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　WRITING　Escritura", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Saturday, October 31 ». Tell us : your costume, your street, the candy, the pumpkins — and one sentence about the clocks that fall back in the night. The best texts will appear in VOL.2 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "Escríbelo en inglés (80–100 palabras): mi sábado 31 de octubre. Cuenta tu disfraz, la calle, los dulces y las calabazas, y una frase sobre el reloj que se atrasa en la noche.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, "MODEL　Modelo", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Saturday, October 31, our street becomes a small Halloween town. In the morning, I carve a pumpkin with my father and we put a candle inside. At six o'clock, I wear my pirate costume and take my bag. House after house, I say « Trick or treat ! » and the neighbours smile and give me candy. My bag is heavy at nine o'clock ! In the night, the clocks fall back, so I sleep one hour more on Sunday. It is my favourite weekend of the autumn.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANSWERS　Respuestas y notas (páginas 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
# Independent-proofread fix (2026-10-21): the len<=10 rule mirrors the core,
# whose Chinese notes are <=10 chars and therefore print. The Spanish notes
# for the items below are longer, so the rule silently dropped 14 printed
# notes that the core edition shows. They are listed explicitly so the
# printed-note coverage of this edition is identical to the core's (62).
NOTAS_EXTRA = {11, 14, 15, 19, 35, 36, 40, 42, 49, 65, 74, 89, 101, 106}
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Página {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("Corrección", "Lectura de gráfico") or e["n"] in NOTAS_EXTRA):
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
