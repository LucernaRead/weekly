# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/en-es-proof/reg-ed/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND · A fondo", "The Lucerna", "A2 → B2 · Phrases of the week · Frases de la semana")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("LEVEL A2 · Base", 27)
cA.head("FALLING BACK", 24)
cA.para("« The clocks fell back. » Fall back = to go back one hour. The past is fell back, not « falled back ». The repeated hour on November 1 is the example of the week (page 2).", 22.5)
cA.head("GOING TO + VERB", 24)
cA.para("For a plan : « She is going to vote on Tuesday. » be + going to + the verb, with no change. It is the friendliest future in English — use it for every plan of the week.", 22.5)
cA.box("THE EXAMPLE · El ejemplo", [
    ("« Americans are going to vote on Tuesday. » — the election story, from page 1.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("LEVEL B1 · Intermedio", 27)
cB.head("COMPARATIVES", 24)
cB.para("Short adjective + -er + than : « The Bernabéu is bigger than most stadiums. » Long adjective : more + adjective : « more convenient ». And good becomes better — never « more good ». Page 4 is full of them.", 22.5)
cB.head("THE PAST SIMPLE", 24)
cB.para("Regular verbs add -ed : changed, watched. Irregular verbs change : fall → fell, go → went, choose → chose. Use it for what is already finished — the clocks that fell back on November 1, and the « as-if-finished » retellings on page 4. The November 3 election and the November 8 games are still to come at press time, so their results are not past yet.", 22.5)
cB.box("THE EXAMPLE · El ejemplo", [
    ("« The clocks fell back on Sunday, November 1. » — fall → fell (page 2).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW)], 200, 1150, tag="P7-B2")
cC.head("LEVEL B2 · Desafío", 27)
cC.head("HEADLINE PRESENT", 24)
cC.para("Headlines speak of yesterday in the present : « America votes », « Bengals play in Madrid ». The present simple makes old news feel live. Read the front page again and find three.", 22.5)
cC.head("WHETHER = IF ?", 24)
cC.para("« Nobody knows whether the race is called yet. » Whether introduces an open question inside a sentence — more elegant than if, and safe everywhere. It is the word for election-night uncertainty.", 22.5)
cC.box("THE EXAMPLE · El ejemplo", [
    ("« Patience is part of the system, not a failure of it. » — part of = una parte (page 6).", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-tools")
cD.head("THE TOOLBOX · Herramientas", 27)
cD.para("Three sentences to keep in your pocket, one for each level :", 22.5)
cD.para("A2 — « It is one o'clock — again ! »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « The clocks fell back on Sunday. »", 22.5)
cD.para("B2 — « Nobody knows whether the race is called yet. »", 22.5, "serif", True, OLIVE)
cD.para("And the newspaper reflex : every phrase of the week comes from an article of this issue. Re-read the article, and the phrase becomes easy.", 22.5)
cD.bridge("Tres frases de bolsillo, una por nivel; todas las frases de la semana salen de los artículos de este número: relee el original y resultan fáciles.")
cD.end_report()

# --- phrases of the week ---
py = 1210
p.hline(MX, RIGHT, py - 14, GOLD, 2)
p.text(MX, py + 26, "PHRASES OF THE WEEK · Frases de la semana", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "Cada frase: un punto de gramática y una pregunta · Respuestas en la página 8", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« Tuesday, November 3, is Election Day in the United States. » (page 1)",
     "Nota — is = es; la fecha es el atributo del sujeto.",
     "A2", "Election Day ___ on Tuesday, November 3. (be)", "is", "is = es"),
    ("« The hour from 1 to 2 happened twice. » (page 2)",
     "Nota — el pasado de happen es happened, forma regular.",
     "A2", "The hour ___ twice on Sunday. (happen)", "happened", "happen → happened"),
    ("« Which film would you choose ? » (page 3)",
     "Nota — would + verbo en infinitivo, para expresar preferencia.",
     "B1", "Which film ___ you choose ? (would)", "would", "would + infinitivo"),
    ("« Two games, two continents, one league — that is the modern NFL. » (page 4)",
     "Nota — that is = es decir; resume tras la raya.",
     "B1", "That ___ the modern NFL. (be)", "is", "that is = es decir"),
    ("« The results will still be there in the morning. » (page 5)",
     "Nota — will still = todavía; still va después de will.",
     "B2", "The results ___ still be there. (will)", "will", "will still = todavía"),
    ("« Patience is part of the system, not a failure of it. » (page 6)",
     "Nota — part of = parte de; not marca el contraste.",
     "B2", "Patience ___ part of the system. (be)", "is", "is part of = parte de"),
    ("« Not every place changes. » (page 2)",
     "Nota — not every + verbo en singular: no todo cambia.",
     "A2", "Not every place ___ . (change)", "changes", "not every → changes"),
    ("« One Sunday is not enough — good thing the week has seven days. » (page 4)",
     "Nota — has = tiene; the week, en singular, lleva has.",
     "B1", "The week ___ seven days. (have)", "has", "have → has"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 20.5, "serif", True, INK, 1.34, 3)
    pf.bridge(point, 19, 4)
    pf.ex(lv, "Practicar", key, note, q, size=20.5)
pf.end_report()

# --- bottom: clinic (left) + readers' corner & teaser (right) ---
by7 = 1870
p.hline(MX, RIGHT, by7 - 14, GOLD, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("THE ERROR CLINIC · Errores", 25)
cf.bridge("Cada frase tiene un error: búscalo y corrígelo.")
cf.ex("A2", "Corregir", "He doesn't like voting early.", "la negación en tercera persona usa doesn't + infinitivo",
     "✗ « He don't like voting early. »", instr="Corrige", size=22.5)
cf.ex("A2", "Corregir", "Yesterday the clocks fell back.", "el pasado de fall es fell",
     "✗ « Yesterday the clocks falled back. »", instr="Corrige", size=22.5)
cf.ex("B1", "Corregir", "This game is bigger than last week's.", "bigger ya es comparativo: no añadas more",
     "✗ « This game is more bigger than last week's. »", instr="Corrige", size=22.5)
cf.ex("B1", "Corregir", "She is going to watch the film on Friday.", "después de going to va el infinitivo",
     "✗ « She is going to watches the film on Friday. »", instr="Corrige", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(rx + 24, by7 + 48, "READERS' CORNER · Rincón de los lectores", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)", 21.5, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 206, "Nota de la redacción: VOL.1 prometió cartas reales en VOL.2, pero no llegó ninguna carta ni el mejor texto de la página 8 de VOL.1; no inventamos nada y el ejemplo sigue marcado. ¡Envíanos tu carta y tu texto! En VOL.3 publicaremos las cartas recibidas.", 20, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 332
p.rect(rx, ty7, rw, 2540 - ty7, fill=DARK)
p.text(rx + 24, ty7 + 46, "NEXT WEEK · VOL.3 · Avance", 24, "sans", True, "#f3edda")
p.para(rx + 24, ty7 + 84, "Wednesday, November 11 : Veterans Day. Sunday, November 15 : the NFL in Munich. And the midterm results, reported — who won, and what changes.", 21.5, "serif", False, "#e8dfc8", rw - 48, 1.45)
p.para(rx + 24, ty7 + 218, "El miércoles, Día de los Veteranos; el domingo, la NFL en Múnich; y los resultados de las elecciones de mitad de mandato.", 20, "sans", False, "#b3a06a", rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
