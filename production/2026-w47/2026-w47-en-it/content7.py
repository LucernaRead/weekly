# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE (A2→B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND　La lingua in mano", "The Lucerna", "A2 → B2　Phrases of the week　Frasi della settimana")

f = Flow(p, [(COLX[i], CW) for i in range(3)], 200, 2560, tag="P7-main")

f.head("WORDS　A2　win / won", 28)
f.gloss("Win è al presente (si vince ogni volta); won è al passato (si è già vinto) — questa settimana si usa soprattutto il passato.")
f.para("win = to get first place. won = the past of win.", 23.5)
f.para("A2: “The Democrats won the House.” The vote is over, so the verb is in the past: won, not win.", 23.5)
f.para("Try it: win / won — ask “Will England win the next Ashes?” about the future: the next series is in England, in June 2027. About last year: “Australia won the first Test.”", 23.5)

f.head("WORDS　B1　more than", 28)
f.gloss("comparative = il comparativo: con more than parliamo di quantità e dimensioni.")
f.para("more than = a bigger number than. In the House, 254 is more than 218. The majority is 218 — and 254 is 36 more than the majority.", 23.5)
f.para("B1: “254 seats is more than the 218 needed.” With numbers, use more than: more people, more seats, more votes.", 23.5)
f.para("Try it: “The film is longer than the trailer.” “The book is cheaper than the film.”", 23.5)

f.head("GRAMMAR　A2　will + verb", 28)
f.gloss("will + infinito: per ciò che accadrà; nelle domande, will va all'inizio.")
f.para("The counting will continue. The new Congress will meet in January. Will the count change? Nobody knows.", 23.5)
f.para("Rule: will + verb, no -s, no -ed. “She will win.” “They will vote.” Question: “Will they watch the jungle?”", 23.5)

f.head("GRAMMAR　B1　past simple", 28)
f.gloss("past simple = il passato semplice: per ciò che è già successo; i verbi irregolari vanno imparati.")
f.para("Use the past for the past: Collins published the novel in 2025. Haymitch won the 50th Games. England lost 4–0 in 2021–22. India beat Australia by 295 runs.", 23.5)
f.para("Irregular verbs in this issue: win → won, lose → lost, beat → beat, choose → chose, run → ran.", 23.5)

f.head("GRAMMAR　B2　headlines", 28)
f.gloss("headline present = il presente dei titoli: i giornali raccontano al presente ciò che è già successo.")
f.para("Newspapers use the present in headlines for what already happened: “Democrats Win the House and the Senate” — the vote was on November 3, but the headline says Win, not Won. The present makes the news feel fresh.", 23.5)

f.head("GRAMMAR　B2　whether", 28)
f.gloss("whether introduce una subordinata: per quello che non si sa, si usa whether.")
f.para("Nobody knows whether the count will change. Nobody knows whether it will rain in Perth. Whether = if — for what you do not know.", 23.5)

f.head("GOLDEN SENTENCES", 28)
f.bridge("Frasi d'oro (frasi originali di questo numero): imparale a memoria e la prossima volta potrai scrivere così.")
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
f.head("THE DRILLS　Esercizi", 28)
f.bridge("Completa con queste parole: won / more / lost / will / published / whether / chose / win.")
f.ex("A2", "Frasi d'oro", "won", "won = il passato di win (si è già vinto)",
     "“The Democrats ___ the House.”", instr="Completa")
f.ex("B1", "Comparativi", "more", "more than = più di",
     "254 is ___ than 218.", instr="Completa")
f.ex("B1", "Passato", "lost", "lose → lost",
     "England ___ 4–0 in 2021–22.", instr="Completa")
f.ex("A2", "Futuro", "will", "will + infinito",
     "The new Congress ___ meet in January.", instr="Completa")
f.ex("B1", "Tempi verbali", "published", "publish → published",
     "Collins ___ the novel in 2025.", instr="Completa")
f.ex("B2", "Subordinate", "whether", "whether = se (per quello che non si sa)",
     "Nobody knows ___ the count will change.", instr="Completa")
f.ex("B2", "Passato", "chose", "choose → chose",
     "ITV ___ Monday for the launch.", instr="Completa")
f.ex("A2", "Completare le frasi", "win", "Con il soggetto plurale si usa win (il presente dei titoli)",
     "“Democrats ___ the House” is a headline.", instr="Completa")
f.head("ERROR CLINIC　Errori", 28)
f.ex("A2", "Correzione", "Correct: The Democrats won the House.", "won / win, errore di tempo verbale",
     "“The Democrats win the House in 2026.” (wrong tense)", instr="Correggi")
f.ex("A2", "Correzione", "Correct: The count continued after the vote.", "Il passato di continue è continued",
     "“The count continue after the vote.” (wrong tense)", instr="Correggi")
f.ex("B1", "Correzione", "Correct: 254 is more than 218.", "more than, la struttura",
     "“254 is more then 218.” (wrong word)", instr="Correggi")
f.ex("B2", "Correzione", "Correct: Nobody knows whether it will change.", "whether introduce una subordinata",
     "“Nobody knows if the count will change or not whether.” (wrong structure)", instr="Correggi")
f.end_report()

# ---- col 3: image + toolbox + drills ----
ix = COLX[3]
image(p, "johnson.jpg", ix, 200, CW, 290)
cy7 = caption(p, ix, 490, CW, "Samuel Johnson, painted by Sir Joshua Reynolds in 1772. Johnson's dictionary fixed English words — and this page fixes yours.",
              "Sir Joshua Reynolds — public domain, via Wikimedia Commons")
v7 = Flow(p, [(ix, CW)], int(cy7) + 18, 2560, tag="P7-col3")
v7.box("THE TOOLBOX　Strumenti", [
    ("A2 — “The Democrats won the House.” I democratici hanno vinto la Camera.", "serif", False, INK, 21.5, 1.42),
    ("B1 — “254 is more than 218.” 254 è più di 218.", "serif", False, INK, 21.5, 1.42),
    ("B2 — “Nobody knows whether the count will change.” Nessuno sa se lo spoglio cambierà ancora.", "serif", False, INK, 21.5, 1.42),
])
v7.head("READERS' CORNER　Lettere", 25)
v7.para("VOL.3 promised real letters from VOL.4. No letters arrived by press time. This page keeps the promise open: send your letter, your three sentences, or your five-sentence film review to the newsroom. Real letters, with your name and city only if you give them, will appear here from VOL.5.", 22)
v7.para("Il VOL.3 lo aveva promesso: dal VOL.4 pubblichiamo le lettere vere dei lettori. Al momento di andare in stampa non era arrivata nessuna lettera — la promessa resta valida: manda la tua lettera, le tue tre frasi o la tua recensione di un film in cinque frasi alla redazione. Le lettere vere appariranno dal VOL.5, con il tuo nome e la tua città solo se lo accetti.", 20, "sans", False, GREY, 1.4, 2)
v7.head("AN EXAMPLE LETTER　Esempio", 24)  # D5: 25->24, HEAD TOO WIDE +8.0px advance at 25
v7.para("This letter is written by the editor, only to show the shape. It is not a reader's letter. No name and no city are given, because no real letter has arrived yet.", 20, "sans", False, GREY, 1.4, 2)
v7.para("“Dear Lucerna, I read the midterm story with my class. We counted the seats together — 254, 162, 19. My question: when will the count be final? Thank you for the numbers.” — A reader, somewhere in the world.", 22)
v7.para("Questa lettera è stata scritta dalla redazione, solo per mostrare il formato. Non è una lettera di un lettore. Non riporta nome né città, perché non è ancora arrivata nessuna lettera vera.", 20, "sans", False, GREY, 1.4, 2)
v7.head("NEXT WEEK　Anteprima VOL.5", 25)
v7.para("Thanksgiving in America. The Ashes: England's rematch waits until June 2027. More certified results of the midterm election. And your letters — the first real ones.", 22)
v7.end_report()
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
