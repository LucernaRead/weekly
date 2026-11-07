# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-en-es/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS · Ejercicios y respuestas", "The Lucerna", "FINAL TEST · Evaluación final · Answers at the bottom of this page · Las respuestas están al final de esta página")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "El 11 de noviembre es miércoles"),
    ("A2", "A", "poppy = la amapola"),
    ("B1", "C", "silence = el silencio"),
    ("A2", "B", "eleven = once"),
    ("A2", "A", "Pudsey, el osito amarillo"),
    ("A2", "C", "will + infinitivo: know"),
    ("B1", "B", "be going to → is going"),
    ("B1", "A", "still = todavía"),
]
cnums = [reg_ex(lv, "Completar el texto", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · CLOZE · Completa el texto", 24, gap=8)
bf.para(f"Maya is sixteen. On ({cnums[0]})___, November 11, she wears a red ({cnums[1]})___ to school. At eleven o'clock, the whole school stands in ({cnums[2]})___ for two minutes. « ({cnums[3]})___, eleven, eleven », says her teacher. On Friday, Maya bakes cakes for ({cnums[4]})___, the yellow bear. « When ({cnums[5]})___ we know the total ? » asks Maya. « On Friday night », says her mother. « On Sunday, Maya is ({cnums[6]})___ to watch the game from Munich — and the poppy will ({cnums[7]})___ be on her coat. »", 21.5)
bf.bridge("Opciones:")
for n, (lv, _k, _nt), opts in zip(cnums, cloze_defs, [
    "A. Monday · B. Wednesday · C. Friday",
    "A. poppy · B. hat · C. ticket",
    "A. noise · B. music · C. silence",
    "A. Ten · B. Eleven · C. Twelve",
    "A. Pudsey · B. Scrooge · C. Dickens",
    "A. do · B. are · C. will",
    "A. goes · B. going · C. go",
    "A. still · B. never · C. soon",
]):
    bf.para(f"{n}. [{lv}] {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B · MULTIPLE CHOICE · Opción", 24, gap=8)
mcq = [
    ("A2", "B", "Las 11 = eleven o'clock", "The silence begins at 11 a.m. In words : ... A. ten o'clock · B. eleven o'clock · C. twelve o'clock"),
    ("A2", "A", "we → wear (infinitivo)", "On Wednesday, we ___ a poppy. A. wear · B. wears · C. wearing"),
    ("B1", "B", "Para el pasado se usa wrote", "Dickens ___ the story in 1843. A. writes · B. wrote · C. writing"),
    ("B1", "B", "than → comparativo: bigger", "The Allianz Arena is ___ than most NFL stadiums. A. big · B. bigger · C. biggest"),
    ("B2", "A", "despite + sustantivo: a pesar de la lluvia", "___ the rain, the ceremony went on all morning. A. Despite · B. Because · C. Unless"),
    ("B2", "A", "whether = si", "Nobody knows ___ this year will be faster. A. whether · B. what · C. who"),
    ("A2", "A", "futuro: will + infinitivo", "The film ___ on Friday, November 13. A. will open · B. will opened · C. will opens"),
    ("B1", "A", "be going to + infinitivo watch", "They are going to ___ the game on Sunday. A. watch · B. watches · C. watched"),
    ("B1", "C", "challenge yourself = acepta el reto", "« Challenge yourself » means... A. the show is over · B. voting is closed · C. take on a challenge"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "Opción múltiple", k, nt, body, size=20.5, gap=8)

# ---- C. reading ----
bf.head("C · READING · Comprensión", 24, gap=8)
bf.para("On Wednesday morning, Tom, a teacher from Manchester, finished his breakfast and walked to school early. At eleven o'clock, the whole school stood still for two minutes. There was no sound in the hall. « We remember them », said Tom, quietly. In the afternoon, his class baked 26 cakes for Children in Need, and a poppy box stood by the door. On Friday night, Tom watched the appeal show with his family — and Pudsey was, as always, yellow and smiling.", 21.5)
read_qs = [
    ("A2", "B", "En el texto: a teacher from Manchester", "Tom is... A. a nurse · B. a teacher · C. a driver"),
    ("A2", "B", "Toda la escuela guarda dos minutos de silencio", "At eleven o'clock, the school... A. sang · B. stood still for two minutes · C. went home"),
    ("B1", "A", "La clase horneó 26 pasteles", "His class baked... A. 26 cakes · B. 11 cakes · C. 13 cakes", ),
    ("B1", "B", "Pudsey es amarillo como siempre", "On Friday night, Pudsey was... A. red · B. yellow and smiling · C. asleep"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "Comprensión lectora", k, nt, body, size=20.5, gap=8)

# ---- D. sentence building ----
bf.head("D · SENTENCES · A completar", 24, gap=8)
d_items = [
    ("A2", "On Friday, they will watch the appeal show.", "will + infinitivo",
     "Will future : « On Friday, they (watch) the appeal show. » → ___"),
    ("B1", "The guns fell silent in 1918.", "fall → fell, irregular",
     "Past simple : « The guns (fall) silent in 1918. »"),
    ("B1", "bigger", "big → bigger (comparativo)",
     "Comparative : « The arena is ___ (big) than most stadiums. »"),
    ("B2", "Whether", "whether introduce una subordinada con «si»",
     "Whether : « ___ this year will be faster, nobody knows yet. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "Completar frases", k, nt, body, size=20.5, gap=8)

# ---- E. translation ----
bf.head("E · TRANSLATION · Traducción", 24, gap=8)
e_items = [
    ("B2", "La paciencia es parte del sistema, no un fallo del sistema.", "part of = parte de; not a failure = no un fallo",
     "Translate : « Patience is part of the system, not a failure of it. »"),
    ("A2", "El miércoles 11 de noviembre, a las 11 h, el Reino Unido guarda dos minutos de silencio.", "at 11 a.m.；two minutes of silence",
     "Traduce: At 11 a.m. on Wednesday, November 11, Britain holds two minutes of silence."),
    ("B1", "Este domingo, la NFL juega en Múnich.", "on Sunday；in Munich",
     "Traduce: On Sunday, the NFL plays in Munich."),
    ("B1", "No todos los países lo llaman igual.", "not every = no todos; call = llamar",
     "Translate : « Not every country calls it by the same name. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "Traducir", k, nt, body, size=20.5, gap=8)

# ---- F. matching ----
bf.head("F · WORDS · Empareja", 24, gap=8)
bf.match_set("B1", "Emparejar",
             ["a silence", "an armistice", "a runoff", "a miser"],
             ["the second vote, when no one wins a majority",
              "a quiet time with no speaking",
              "an agreement to stop fighting",
              "a person who loves money and hates spending it"],
             ["b", "c", "a", "d"],
             ["silence = el silencio b", "armistice = el armisticio c", "runoff = la segunda vuelta a", "miser = el avaro d"],
             instr="Empareja")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ticket", "ticket = la entrada"),
    ("A2", "line", "line = cola, inglés americano"),
    ("A2", "scarf", "scarf = la bufanda"),
    ("A2", "anthem", "anthem = el himno"),
    ("B1", "Sunday", "El partido es el domingo 15 de noviembre"),
]
gnums = [reg_ex(lv, "Completar el diálogo", k, nt) for lv, k, nt in dlg_defs]
bf.head("G · DIALOGUE · El diálogo", 24, gap=8)
bf.para(f"— Good morning ! Is this the way to the Allianz Arena ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long ? — No, five minutes only. It is my first NFL game. What do I do with the ({gnums[2]})___ ? — Wear it with pride, and cheer for the Lions. — And the famous ({gnums[3]})___ ? — Two anthems, one game. Enjoy Munich. — I will ! See you on ({gnums[4]})___ ! — Have a good day.", 20.5)
bf.para("Levels : 145–148 [A2] · 149 [B1]", 19.5, "sans", False, GREY, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "Redacción", "Pregunta abierta: véanse los puntos en el recuadro de redacción; el modelo está en el recuadro de esta página", "Se puntúa por puntos")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · WRITING · Escritura [B1]", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Wednesday, November 11 ». Tell us : did you stand still at eleven, what did you wear, what did you watch on Friday — and one sentence about the game in Munich on Sunday. The best texts will appear in VOL.4 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "Escribe en inglés (80–100 palabras): «Mi miércoles 11 de noviembre». Cuenta si estuviste quieto a las 11, qué llevabas puesto, qué viste el viernes — y una frase sobre el partido de Múnich del domingo.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MODEL · Modelo", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Wednesday, November 11, our school stopped for two minutes. At eleven o'clock, the hall went quiet, and I thought about the soldiers of the First World War. In the evening, we watched the news from London, and my mother wore her poppy at dinner. On Friday, we baked 26 cakes for Children in Need, and Pudsey smiled from the television. On Sunday, we watched the game from Munich. It was a week of silence, kindness and sport — and I slept well, because I had remembered.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "ANSWERS · Respuestas y notas (páginas 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")
PRINT_NOTES = [8, 9, 15, 23, 31, 32, 37, 39, 48, 50, 55, 57, 67, 68, 72, 82, 83, 84, 85, 86, 87, 89, 90, 92, 103, 104, 106, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Página {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and (pg == 8 or e["n"] in PRINT_NOTES):
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
