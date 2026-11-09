# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND　La lingua in mano", "The Lucerna", "A2 → B2　Phrases of the week　Frasi della settimana")

cA = Flow(p, [(COLX[0], CW)], 200, 1150, tag="P7-A2")
cA.head("LEVEL A2　Fondamenti", 27)
cA.head("FALLING BACK", 24)
cA.para("« The clocks fell back. » Fall back = to go back one hour. The past is fell back, not « falled back ». The repeated hour on November 1 is the example of the week (page 2).", 22.5)
cA.head("GOING TO + VERB", 24)
cA.para("For a plan : « She is going to vote on Tuesday. » be + going to + the verb, with no change. It is the friendliest future in English — use it for every plan of the week.", 22.5)
cA.box("THE EXAMPLE　Esempio", [
    ("« Americans are going to vote on Tuesday. » — the election story, from page 1.", "serif", False, INK, 21.5, 1.42),
])
cA.end_report()

cB = Flow(p, [(COLX[1], CW)], 200, 1150, tag="P7-B1")
cB.head("LEVEL B1　Intermedio", 27)
cB.head("COMPARATIVES", 24)
cB.para("Short adjective + -er + than : « The Bernabéu is bigger than most stadiums. » Long adjective : more + adjective : « more convenient ». And good becomes better — never « more good ». Page 4 is full of them.", 22.5)
cB.head("THE PAST SIMPLE", 24)
cB.para("Regular verbs add -ed : changed, watched. Irregular verbs change : fall → fell, go → went, choose → chose. Use it for what is already finished — the clocks that fell back on November 1, and the « as-if-finished » retellings on page 4. The November 3 election and the November 8 games are still to come at press time, so their results are not past yet.", 22.5)
cB.box("THE EXAMPLE　Esempio", [
    ("« The clocks fell back on Sunday, November 1. » — fall → fell (page 2).", "serif", False, INK, 21.5, 1.42),
])
cB.end_report()

cC = Flow(p, [(COLX[2], CW)], 200, 1150, tag="P7-B2")
cC.head("LEVEL B2　Sfida", 27)
cC.head("HEADLINE PRESENT", 24)
cC.para("Headlines speak of yesterday in the present : « America votes », « Bengals play in Madrid ». The present simple makes old news feel live. Read the front page again and find three.", 22.5)
cC.head("WHETHER = IF ?", 24)
cC.para("« Nobody knows whether the race is called yet. » Whether introduces an open question inside a sentence — more elegant than if, and safe everywhere. It is the word for election-night uncertainty.", 22.5)
cC.box("THE EXAMPLE　Esempio", [
    ("« Patience is part of the system, not a failure of it. » — part of = una parte di (page 6).", "serif", False, INK, 21.5, 1.42),
])
cC.end_report()

cD = Flow(p, [(COLX[3], CW)], 200, 1150, tag="P7-tools")
cD.head("THE TOOLBOX　Attrezzi", 27)
cD.para("Three sentences to keep in your pocket, one for each level :", 22.5)
cD.para("A2 — « It is one o'clock — again ! »", 22.5, "serif", True, OLIVE)
cD.para("B1 — « The clocks fell back on Sunday. »", 22.5)
cD.para("B2 — « Nobody knows whether the race is called yet. »", 22.5, "serif", True, OLIVE)
cD.para("And the newspaper reflex : every phrase of the week comes from an article of this issue. Re-read the article, and the phrase becomes easy.", 22.5)
cD.bridge("Cassetta degli attrezzi | Tre frasi da tenere in tasca, una per livello; tutte le frasi della settimana vengono da questo numero: rileggi l'articolo e ti resteranno in mente.")
cD.end_report()

# --- phrases of the week ---
py = 1210
p.hline(MX, RIGHT, py - 14, OLIVE, 2)
p.text(MX, py + 26, "PHRASES OF THE WEEK　Frasi della settimana (tutte da questo numero)", 27, "sans", True, OLIVE)
p.text(RIGHT, py + 26, "Ogni frase: un punto di grammatica + un esercizio　Risposte a pagina 8", 20, "sans", False, GREY, anchor="end")
pf = Flow(p, [(COLX[i], CW) for i in range(4)], py + 52, 1830, tag="P7-phrases")
phrases = [
    ("« Tuesday, November 3, is Election Day in the United States. » (page 1)",
     "Grammatica | is = è; la data come soggetto.",
     "A2", "Election Day ___ on Tuesday, November 3. (be)", "is", "is = è"),
    ("« The hour from 1 to 2 happened twice. » (page 2)",
     "Grammatica | il passato di happen è happened, regolare.",
     "A2", "The hour ___ twice on Sunday. (happen)", "happened", "happen → happened"),
    ("« Which film would you choose ? » (page 3)",
     "Grammatica | would + forma base, per esprimere una scelta.",
     "B1", "Which film ___ you choose ? (would)", "would", "would + forma base"),
    ("« Two games, two continents, one league — that is the modern NFL. » (page 4)",
     "Grammatica | that is = cioè; dopo il trattino il riassunto.",
     "B1", "That ___ the modern NFL. (be)", "is", "that is = cioè"),
    ("« The results will still be there in the morning. » (page 5)",
     "Grammatica | will still = continuerà a; still va dopo will.",
     "B2", "The results ___ still be there. (will)", "will", "will still = continuerà a"),
    ("« Patience is part of the system, not a failure of it. » (page 6)",
     "Grammatica | part of = una parte di; not come contrasto.",
     "B2", "Patience ___ part of the system. (be)", "is", "is part of = una parte di"),
    ("« Not every place changes. » (page 2)",
     "Grammatica | not every + verbo al singolare: non tutti i luoghi cambiano.",
     "A2", "Not every place ___ . (change)", "changes", "not every → changes"),
    ("« One Sunday is not enough — good thing the week has seven days. » (page 4)",
     "Grammatica | has = ha; the week al singolare richiede has.",
     "B1", "The week ___ seven days. (have)", "has", "have → has"),
]
for sent, point, lv, q, key, note in phrases:
    pf.para(sent, 20.5, "serif", True, INK, 1.34, 3)
    pf.bridge(point, 19, 4)
    pf.ex(lv, "Pratica guidata", key, note, q, size=20.5)
pf.end_report()

# --- bottom: clinic (left) + readers' corner & teaser (right) ---
by7 = 1870
p.hline(MX, RIGHT, by7 - 14, OLIVE, 2)
cf = Flow(p, [(COLX[0], CW), (COLX[1], CW)], by7 + 8, 2268, tag="P7-clinic")
cf.head("THE ERROR CLINIC　Errori", 25)
cf.bridge("Ogni frase contiene un errore: trovalo e correggi la frase.")
cf.ex("A2", "Correzione", "He doesn't like voting early.", "Terza persona: doesn't + forma base",
     "✗ « He don't like voting early. »", instr="Correggi", size=22.5)
cf.ex("A2", "Correzione", "Yesterday the clocks fell back.", "Passato di fall: fell",
     "✗ « Yesterday the clocks falled back. »", instr="Correggi", size=22.5)
cf.ex("B1", "Correzione", "This game is bigger than last week's.", "bigger è già il comparativo: niente more davanti",
     "✗ « This game is more bigger than last week's. »", instr="Correggi", size=22.5)
cf.ex("B1", "Correzione", "She is going to watch the film on Friday.", "Dopo going to va la forma base",
     "✗ « She is going to watches the film on Friday. »", instr="Correggi", size=22.5)
cf.end_report()

rx, rw = span_x(2, 2)
p.rect(rx, by7 + 8, rw, 300, fill=BOX)
p.text(rx + 24, by7 + 48, "READERS' CORNER　Angolo dei lettori", 24, "sans", True, OLIVE)
p.para(rx + 24, by7 + 86, "« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)", 21.5, "serif", False, INK, rw - 48, 1.42)
p.para(rx + 24, by7 + 206, "Nota della redazione | Alla chiusura di questo numero non sono arrivate vere lettere dei lettori e non ci sono testi di scrittura del VOL.1 da premiare come migliori. L'esempio qui sopra resta quindi indicato onestamente come esempio; le vere lettere usciranno dal VOL.3. Mandaci la tua lettera e il tuo testo: li pubblicheremo nel VOL.3!", 20, "sans", False, GREY, rw - 48, 1.4)
ty7 = by7 + 332
p.rect(rx, ty7, rw, 2560 - ty7, fill=CLOTH)
p.text(rx + 24, ty7 + 46, "NEXT WEEK　VOL.3　Anticipazioni", 24, "sans", True, ONCLOTH)
p.para(rx + 24, ty7 + 84, "Wednesday, November 11 : Veterans Day. Sunday, November 15 : the NFL in Munich. And the midterm results, reported — who won, and what changes.", 21.5, "serif", False, "#cac8ba", rw - 48, 1.45)
p.para(rx + 24, ty7 + 218, "Mercoledì 11 novembre: Veterans Day. Domenica 15 novembre: la NFL a Monaco. E i risultati delle elezioni di medio termine.", 20, "sans", False, GOOSE, rw - 48, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-langue.svg")
print("P7 saved, exercises so far:", len(REG))
