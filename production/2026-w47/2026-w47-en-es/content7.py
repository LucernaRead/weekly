# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE (A2→B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND　La lengua en mano", "The Lucerna", "A2 → B2　Phrases of the week　Frases de la semana")

f = Flow(p, [(COLX[i], CW) for i in range(3)], 200, 2560, tag="P7-main")

f.head("WORDS　A2　win / won", 28)
f.gloss("Win está en presente (se gana cada vez); won está en pasado (ya se ha ganado) — esta semana se usa sobre todo el pasado.")
f.para("win = to get first place. won = the past of win.", 23.5)
f.para("A2: “The Democrats won the House.” The vote is over, so the verb is in the past: won, not win.", 23.5)
f.para("Try it: win / won — ask “Will England win the next Ashes?” about the future: the next series is in England, in June 2027. About last year: “Australia won the first Test.”", 23.5)

f.head("WORDS　B1　more than", 28)
f.gloss("comparative = el comparativo: con more than hablamos de cantidad y de tamaño.")
f.para("more than = a bigger number than. In the House, 254 is more than 218. The majority is 218 — and 254 is 36 more than the majority.", 23.5)
f.para("B1: “254 seats is more than the 218 needed.” With numbers, use more than: more people, more seats, more votes.", 23.5)
f.para("Try it: “The film is longer than the trailer.” “The book is cheaper than the film.”", 23.5)

f.head("GRAMMAR　A2　will + verb", 28)
f.gloss("will + infinitivo: para lo que va a pasar; en las preguntas, will va al principio.")
f.para("The counting will continue. The new Congress will meet in January. Will the count change? Nobody knows.", 23.5)
f.para("Rule: will + verb, no -s, no -ed. “She will win.” “They will vote.” Question: “Will they watch the jungle?”", 23.5)

f.head("GRAMMAR　B1　past simple", 28)
f.gloss("past simple = el pasado simple: para lo que ya ha pasado; hay que aprender los verbos irregulares.")
f.para("Use the past for the past: Collins published the novel in 2025. Haymitch won the 50th Games. England lost 4–0 in 2021–22. India beat Australia by 295 runs.", 23.5)
f.para("Irregular verbs in this issue: win → won, lose → lost, beat → beat, choose → chose, run → ran.", 23.5)

f.head("GRAMMAR　B2　headlines", 28)
f.gloss("headline present = el presente de los titulares: los periódicos cuentan en presente lo que ya ha pasado.")
f.para("Newspapers use the present in headlines for what already happened: “Democrats Win the House and the Senate” — the vote was on November 3, but the headline says Win, not Won. The present makes the news feel fresh.", 23.5)

f.head("GRAMMAR　B2　whether", 28)
f.gloss("whether introduce una subordinada: para lo que no se sabe, se usa whether.")
f.para("Nobody knows whether the count will change. Nobody knows whether it will rain in Perth. Whether = if — for what you do not know.", 23.5)

f.head("GOLDEN SENTENCES", 28)
f.bridge("Frases de oro (frases originales de este número): memorízalas y la próxima vez podrás escribir así.")
gold = [
    ("The vote is over. The counting is not.", "P2"),
    ("A “call” is not the official result.", "P1"),
    ("The Ashes are not a sport for early nights.", "P4"),
    ("A midterm changes Congress, not the President.", "P6"),
    ("The map is drawn. The work starts in January.", "P6"),
    ("Two jungles, one week: a painted jungle in the cinema, and a real jungle on television.", "P3"),
    ("A small act is not small to the person it helps — and a loud voice starts with one sentence.", "P5"),
    ("On Tuesday, November 3, Americans voted in the midterm election — for all 435 seats in the House of Representatives, for 35 seats in the Senate, and for governor in 36 states.", "P1"),
]
for en, src in gold:
    f.para(f"“{en}”", 23.5, "serif", False, INK, 1.42, 2)
    f.para(f"—— From page {src.replace('P', '')} of this issue.", 19, "sans", False, GREY, 1.4, 2)
f.head("THE DRILLS　Ejercicios", 28)
f.bridge("Completa con estas palabras: won / more / lost / will / published / whether / chose / win.")
f.ex("A2", "Frases de oro", "won", "won = el pasado de win (ya se ha ganado)",
     "“The Democrats ___ the House.”", instr="Completa")
f.ex("B1", "Comparativos", "more", "more than = más que",
     "254 is ___ than 218.", instr="Completa")
f.ex("B1", "Pasado", "lost", "lose → lost",
     "England ___ 4–0 in 2021–22.", instr="Completa")
f.ex("A2", "Futuro", "will", "will + infinitivo",
     "The new Congress ___ meet in January.", instr="Completa")
f.ex("B1", "Tiempos verbales", "published", "publish → published",
     "Collins ___ the novel in 2025.", instr="Completa")
f.ex("B2", "Subordinadas", "whether", "whether = si (para lo que no se sabe)",
     "Nobody knows ___ the count will change.", instr="Completa")
f.ex("B2", "Pasado", "chose", "choose → chose",
     "ITV ___ Monday for the launch.", instr="Completa")
f.ex("A2", "Completar frases", "win", "Con sujeto plural se usa win (el presente de los titulares)",
     "“Democrats ___ the House” is a headline.", instr="Completa")
f.head("ERROR CLINIC　Errores", 28)
f.ex("A2", "Corrección", "Correct: The Democrats won the House.", "won / win, error de tiempo verbal",
     "“The Democrats win the House in 2026.” (wrong tense)", instr="Corrige")
f.ex("A2", "Corrección", "Correct: The count continued after the vote.", "El pasado de continue es continued",
     "“The count continue after the vote.” (wrong tense)", instr="Corrige")
f.ex("B1", "Corrección", "Correct: 254 is more than 218.", "more than, la estructura",
     "“254 is more then 218.” (wrong word)", instr="Corrige")
f.ex("B2", "Corrección", "Correct: Nobody knows whether it will change.", "whether introduce una subordinada",
     "“Nobody knows if the count will change or not whether.” (wrong structure)", instr="Corrige")
f.end_report()

# ---- col 3: image + toolbox + drills ----
ix = COLX[3]
image(p, "johnson.jpg", ix, 200, CW, 290)
cy7 = caption(p, ix, 490, CW, "Samuel Johnson, painted by Sir Joshua Reynolds in 1772. Johnson's dictionary fixed English words — and this page fixes yours.",
              "Sir Joshua Reynolds — public domain, via Wikimedia Commons")
v7 = Flow(p, [(ix, CW)], int(cy7) + 18, 2560, tag="P7-col3")
v7.box("THE TOOLBOX　Herramientas", [
    ("A2 — “The Democrats won the House.” Los demócratas ganaron la Cámara.", "serif", False, INK, 21.5, 1.42),
    ("B1 — “254 is more than 218.” 254 es más que 218.", "serif", False, INK, 21.5, 1.42),
    ("B2 — “Nobody knows whether the count will change.” Nadie sabe si el recuento volverá a cambiar.", "serif", False, INK, 21.5, 1.42),
])
v7.head("READERS' CORNER　Cartas", 25)
v7.para("VOL.3 promised real letters from VOL.4. No letters arrived by press time. This page keeps the promise open: send your letter, your three sentences, or your five-sentence film review to the newsroom. Real letters, with your name and city only if you give them, will appear here from VOL.5.", 22)
v7.para("El VOL.3 lo prometió: a partir del VOL.4 publicamos las cartas reales de los lectores. Cuando fuimos a imprenta no había llegado ninguna carta — la promesa sigue en pie: envía tu carta, tus tres frases o tu crítica de cine en cinco frases a la redacción. Las cartas reales aparecerán a partir del VOL.5, con tu nombre y tu ciudad solo si lo aceptas.", 20, "sans", False, GREY, 1.4, 2)
v7.head("AN EXAMPLE LETTER　Ejemplo", 24)  # D5: 25->24, HEAD TOO WIDE +3.5px advance at 25
v7.para("This letter is written by the editor, only to show the shape. It is not a reader's letter. No name and no city are given, because no real letter has arrived yet.", 20, "sans", False, GREY, 1.4, 2)
v7.para("“Dear Lucerna, I read the midterm story with my class. We counted the seats together — 254, 162, 19. My question: when will the count be final? Thank you for the numbers.” — A reader, somewhere in the world.", 22)
v7.para("Esta carta la ha escrito la redacción, solo para mostrar el formato. No es una carta de un lector. No lleva nombre ni ciudad, porque aún no ha llegado ninguna carta real.", 20, "sans", False, GREY, 1.4, 2)
v7.head("NEXT WEEK　Avance del VOL.5", 25)
v7.para("Thanksgiving in America. The Ashes: England's rematch waits until June 2027. More certified results of the midterm election. And your letters — the first real ones.", 22)
v7.end_report()
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
