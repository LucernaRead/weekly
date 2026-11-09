# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS　Ejercicios y respuestas", "The Lucerna", "FINAL TEST　Evaluación final　Answers at the bottom of this page　Las respuestas están al final de esta página")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "el 3 de noviembre es martes"),
    ("A2", "A", "pizza"),
    ("B1", "C", "el mapa cambia estado a estado"),
    ("A2", "B", "close = reñido"),
    ("A2", "A", "sticker = pegatina"),
    ("A2", "C", "will + infinitivo: know"),
    ("B1", "B", "be going to → is going"),
    ("B1", "A", "still = todavía"),
]
cnums = [reg_ex(lv, "Completar el texto", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　CLOZE　Completa el texto", 24, gap=8)
bf.para(f"Leo is sixteen. On Tuesday, November 3, it is ({cnums[0]})___. His family does not cook dinner : they order ({cnums[1]})___. On television, the ({cnums[2]})___ changes colour, state by state. « Ohio is very ({cnums[3]})___ ! » says his father. At nine o'clock, Leo's mother comes home from voting, with a ({cnums[4]})___ on her jacket : « I VOTED ». « When ({cnums[5]})___ we know the results ? » asks Leo. « Tomorrow », says his mother. « Tomorrow, Leo is ({cnums[6]})___ to read the results at school — and the map will ({cnums[7]})___ be on television tonight. »", 21.5)
bf.bridge("Opciones:")
for n, (lv, _k, _nt), opts in zip(cnums, cloze_defs, [
    "A. Monday · B. Election Day · C. Halloween",
    "A. pizza · B. salad · C. soup",
    "A. phone · B. table · C. map",
    "A. far · B. close · C. big",
    "A. sticker · B. hat · C. ticket",
    "A. do · B. are · C. will",
    "A. goes · B. going · C. go",
    "A. still · B. never · C. soon",
]):
    bf.para(f"{n}. [{lv}] {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B　MULTIPLE CHOICE　Opción", 24, gap=8)
mcq = [
    ("A2", "B", "1:30 = half past one", "The clocks show 1:30. In words : ... A. one o'clock · B. half past one · C. a quarter to one"),
    ("A2", "A", "we → get, infinitivo", "On Sunday, we ___ an extra hour of sleep. A. get · B. gets · C. getting"),
    ("B1", "B", "lo ya ocurrido usa fell", "The clocks ___ back on Sunday. A. fall · B. fell · C. falling"),
    ("B1", "B", "than → comparativo: bigger", "The Bernabéu is ___ than most stadiums. A. big · B. bigger · C. biggest"),
    ("B2", "A", "despite + sustantivo: a pesar de la lluvia", "___ the rain, the game went on all evening. A. Despite · B. Because · C. Unless"),
    ("B2", "A", "whether = si", "Nobody knows ___ the race is called yet. A. whether · B. what · C. who"),
    ("A2", "A", "futuro: will + infinitivo", "The film ___ on Friday, November 6. A. will open · B. will opened · C. will opens"),
    ("B1", "A", "be going to + infinitivo: vote", "They are going to ___ on Tuesday. A. vote · B. votes · C. voted"),
    ("B1", "C", "too close to call = aún no se sabe", "« Too close to call » means... A. the winner is clear · B. voting is over · C. we do not know yet"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "Opción múltiple", k, nt, body, size=20.5)

# ---- C. reading ----
bf.head("C　READING　Comprensión", 24, gap=8)
bf.para("On Saturday morning, Sam, a teacher from Ohio, finished his breakfast and walked to the early-voting place near his school. There was no line. « On Tuesday, I teach all day », he explains. « Today, I have time. » Five minutes later, his ballot was in the box, and a sticker on his jacket said : I VOTED. On Tuesday night, Sam watched the map with his family — and Ohio was, as always, too close to call.", 21.5)
read_qs = [
    ("A2", "B", "en el texto: a teacher from Ohio", "Sam is... A. a nurse · B. a teacher · C. a driver"),
    ("A2", "B", "el martes enseña todo el día", "He voted early because on Tuesday he... A. travels · B. teaches all day · C. sleeps"),
    ("B1", "A", "en la pegatina pone I VOTED", "His sticker said... A. I VOTED · B. VOTE ON TUESDAY · C. OHIO FIRST"),
    ("B1", "B", "Ohio, como siempre, demasiado reñido", "On Tuesday night, Ohio was... A. clear · B. too close to call · C. finished early"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "Comprensión lectora", k, nt, body, size=20.5)

# ---- D. sentence building ----
bf.head("D　SENTENCES　A completar", 24, gap=8)
d_items = [
    ("A2", "On Friday, they are going to watch the cat film.", "are going to + infinitivo",
     "Be going to : « On Friday, they (watch) the cat film. » → ___"),
    ("B1", "The clocks fell back on Sunday.", "fall → fell, irregular",
     "Past simple : « The clocks (fall) back on Sunday. »"),
    ("B1", "taller", "tall → taller, comparativo",
     "Comparative : « The hat is ___ (tall) than the Cat. »"),
    ("B2", "Whether", "whether introduce una subordinada con «si»",
     "Whether : « ___ the race is called, nobody knows yet. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "Completar frases", k, nt, body, size=20.5)

# ---- E. translation ----
bf.head("E　TRANSLATION　Traducción", 24, gap=8)
e_items = [
    ("B2", "La paciencia es parte del sistema, no un fallo del sistema.", "part of = parte de; not a failure = no un fallo",
     "Translate : « Patience is part of the system, not a failure of it. »"),
    ("A2", "El martes 3 de noviembre es el día de las elecciones en Estados Unidos.", "Election Day = día de elecciones; on Tuesday",
     "Traduce: Tuesday, November 3, is Election Day in the United States."),
    ("B1", "El domingo, la NFL juega en Madrid.", "on Sunday; in Madrid",
     "Traduce: On Sunday, the NFL plays in Madrid."),
    ("B1", "No todos los lugares cambian.", "not every = no todo; change = cambiar",
     "Translate : « Not every place changes. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "Traducir", k, nt, body, size=20.5, gap=4)

# ---- F. matching ----
bf.head("F　WORDS　Empareja", 24, gap=8)
bf.match_set("B1", "Emparejar",
             ["a midterm", "a governor", "a ballot", "turnout"],
             ["the number of people who vote",
              "an election in the middle of a term",
              "the person who leads a state",
              "the paper you mark your choice on"],
             ["b", "c", "d", "a"],
             ["midterm = elecciones de mitad de mandato b", "governor = gobernador c", "ballot = papeleta d", "turnout = participación a"],
             instr="Empareja")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ID", "enseña tu documento de identidad al votar"),
    ("A2", "line", "line = cola, inglés americano"),
    ("A2", "ballot", "ballot = papeleta"),
    ("A2", "sticker", "sticker = pegatina"),
    ("B1", "Tuesday", "el día de elecciones es el martes 3 de noviembre"),
]
gnums = [reg_ex(lv, "Completar el diálogo", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　El diálogo", 24, gap=8)
bf.para(f"— Good morning ! Is this the voting place ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long today ? — No, five minutes only. On Tuesday it will be very long ! — Good. It is my first vote. What do I do with the ({gnums[2]})___ ? — Mark your choices, check them twice, then put it in the box. — Thank you. And the famous ({gnums[3]})___ ? Everybody has one on their jacket. — The sticker ! Here it is : « I VOTED ». Wear it with pride. — I will ! See you on ({gnums[4]})___ , in the results ! — Ha ! Have a good day.", 21.5)
bf.para("Levels : 145–148 [A2] · 149 [B1]", 19.5, "sans", False, GREY, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "Redacción", "Pregunta abierta: véanse los puntos en el recuadro de redacción; el modelo está en el recuadro de esta página", "Se puntúa por puntos")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　WRITING　Escritura [B1]", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Tuesday, November 3 ». Tell us : did you watch the results, what did you eat, what did the map show — and one sentence about the clocks that fell back on Sunday night. The best texts will appear in VOL.3 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "Escribe en inglés de 80 a 100 palabras: tu martes 3 de noviembre. Di si viste los resultados, qué comiste, qué mostró el mapa, y una frase sobre los relojes atrasados el domingo por la noche.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, "MODEL　Modelo", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Tuesday, November 3, our family watched the election results at home. We ate pizza, because nobody wanted to cook on such a night. On television, the map changed colour, state by state, and my father said : « Ohio is too close to call ! » I did not understand every state, but I understood the pizza and the excitement. On Sunday night, the clocks had fallen back, so I slept one hour more. It was a long night, and a very American one.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANSWERS　Respuestas y notas (páginas 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Página {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        NOTAS_EXTRA = {11, 12, 14, 19, 29, 30, 31, 33, 41, 44, 47, 48, 51, 58, 64, 66, 67, 68, 69, 71, 74, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 100, 102, 107, 108, 109, 110, 111}
        if e["note"] and (pg == 8 or e["n"] in NOTAS_EXTRA):
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
