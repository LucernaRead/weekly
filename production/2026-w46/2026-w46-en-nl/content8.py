# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS　Oefeningen en antwoorden", "The Lucerna", "FINAL TEST　Eindtoets　Answers at the bottom of this page　Antwoorden onderaan deze pagina")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "11 november is een woensdag"),
    ("A2", "A", "poppy = de klaproos"),
    ("B1", "C", "silence = de stilte"),
    ("A2", "B", "eleven = elf"),
    ("A2", "A", "Pudsey, de gele teddybeer"),
    ("A2", "C", "will + infinitief know"),
    ("B1", "B", "be going to → is going"),
    ("B1", "A", "still = nog steeds"),
]
cnums = [reg_ex(lv, "Gatentekst", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　CLOZE　Gatentekst", 24, gap=8)
bf.para(f"Maya is sixteen. On ({cnums[0]})___, November 11, she wears a red ({cnums[1]})___ to school. At eleven o'clock, the whole school stands in ({cnums[2]})___ for two minutes. « ({cnums[3]})___, eleven, eleven », says her teacher. On Friday, Maya bakes cakes for ({cnums[4]})___, the yellow bear. « When ({cnums[5]})___ we know the total ? » asks Maya. « On Friday night », says her mother. « On Sunday, Maya is ({cnums[6]})___ to watch the game from Munich — and the poppy will ({cnums[7]})___ be on her coat. »", 21.5)
bf.bridge("Opties:")
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
bf.head("B　MULTIPLE CHOICE　Meerkeuze", 24, gap=8)
mcq = [
    ("A2", "B", "11 uur = eleven o'clock", "The silence begins at 11 a.m. In words : ... A. ten o'clock · B. eleven o'clock · C. twelve o'clock"),
    ("A2", "A", "we → wear (infinitief)", "On Wednesday, we ___ a poppy. A. wear · B. wears · C. wearing"),
    ("B1", "B", "Voor het verleden gebruik je wrote", "Dickens ___ the story in 1843. A. writes · B. wrote · C. writing"),
    ("B1", "B", "than → vergrotende trap bigger", "The Allianz Arena is ___ than most NFL stadiums. A. big · B. bigger · C. biggest"),
    ("B2", "A", "despite + zelfstandig naamwoord: ondanks de regen", "___ the rain, the ceremony went on all morning. A. Despite · B. Because · C. Unless"),
    ("B2", "A", "whether = of", "Nobody knows ___ this year will be faster. A. whether · B. what · C. who"),
    ("A2", "A", "Toekomst: will + infinitief", "The film ___ on Friday, November 13. A. will open · B. will opened · C. will opens"),
    ("B1", "A", "be going to + infinitief watch", "They are going to ___ the game on Sunday. A. watch · B. watches · C. watched"),
    ("B1", "C", "challenge yourself = ga de uitdaging aan", "« Challenge yourself » means... A. the show is over · B. voting is closed · C. take on a challenge"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "Meerkeuze", k, nt, body, size=20.5, gap=8)

# ---- C. reading ----
bf.head("C　READING　Leestekst", 24, gap=8)
bf.para("On Wednesday morning, Tom, a teacher from Manchester, finished his breakfast and walked to school early. At eleven o'clock, the whole school stood still for two minutes. There was no sound in the hall. « We remember them », said Tom, quietly. In the afternoon, his class baked 26 cakes for Children in Need, and a poppy box stood by the door. On Friday night, Tom watched the appeal show with his family — and Pudsey was, as always, yellow and smiling.", 21.5)
read_qs = [
    ("A2", "B", "In de tekst: a teacher from Manchester", "Tom is... A. a nurse · B. a teacher · C. a driver"),
    ("A2", "B", "De hele school houdt twee minuten stilte", "At eleven o'clock, the school... A. sang · B. stood still for two minutes · C. went home"),
    ("B1", "A", "De klas bakte 26 taarten", "His class baked... A. 26 cakes · B. 11 cakes · C. 13 cakes", ),
    ("B1", "B", "Pudsey is geel zoals altijd", "On Friday night, Pudsey was... A. red · B. yellow and smiling · C. asleep"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "Begrijpend lezen", k, nt, body, size=20.5, gap=8)

# ---- D. sentence building ----
bf.head("D　SENTENCES　Zinnen vormen", 24, gap=8)
d_items = [
    ("A2", "On Friday, they will watch the appeal show.", "will + infinitief",
     "Will future : « On Friday, they (watch) the appeal show. » → ___"),
    ("B1", "The guns fell silent in 1918.", "fall → fell (onregelmatig)",
     "Past simple : « The guns (fall) silent in 1918. »"),
    ("B1", "bigger", "big → bigger (vergrotende trap)",
     "Comparative : « The arena is ___ (big) than most stadiums. »"),
    ("B2", "Whether", "whether leidt een of-zin in",
     "Whether : « ___ this year will be faster, nobody knows yet. »"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "Zinnen aanvullen", k, nt, body, size=20.5, gap=8)

# ---- E. translation ----
bf.head("E　TRANSLATION　Vertalen", 24, gap=8)
e_items = [
    ("B2", "Geduld is een deel van het systeem, geen falen van het systeem.", "part of = een deel; not a failure = geen falen",
     "Vertaal: « Patience is part of the system, not a failure of it. »"),
    ("A2", "Op woensdag 11 november, om 11 uur, houdt het Verenigd Koninkrijk twee minuten stilte.", "at 11 a.m.；two minutes of silence",
     "Vertaal: At 11 a.m. on Wednesday, November 11, Britain holds two minutes of silence."),
    ("B1", "Deze zondag speelt de NFL in München.", "on Sunday；in Munich",
     "Vertaal: On Sunday, the NFL plays in Munich."),
    ("B1", "Niet elk land noemt het hetzelfde.", "not every = niet elke; call = noemen",
     "Translate : « Not every country calls it by the same name. »"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "Vertalen", k, nt, body, size=20.5, gap=8)

# ---- F. matching ----
bf.head("F　WORDS　Woorden combineren", 24, gap=8)
bf.match_set("B1", "Woorden combineren",
             ["a silence", "an armistice", "a runoff", "a miser"],
             ["the second vote, when no one wins a majority",
              "a quiet time with no speaking",
              "an agreement to stop fighting",
              "a person who loves money and hates spending it"],
             ["b", "c", "a", "d"],
             ["silence = de stilte b", "armistice = de wapenstilstand c", "runoff = de tweede ronde a", "miser = de vrek d"],
             instr="Combineer")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "ticket", "ticket = het kaartje"),
    ("A2", "line", "line = rij (Amerikaans Engels)"),
    ("A2", "scarf", "scarf = de sjaal"),
    ("A2", "anthem", "anthem = het volkslied"),
    ("B1", "Sunday", "De wedstrijd is op zondag 15 november"),
]
gnums = [reg_ex(lv, "Dialoog aanvullen", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　Dialoog aanvullen", 24, gap=8)
bf.para(f"— Good morning ! Is this the way to the Allianz Arena ? — Yes, welcome. May I see your ({gnums[0]})___ ? — Here it is. Is the ({gnums[1]})___ long ? — No, five minutes only. It is my first NFL game. What do I do with the ({gnums[2]})___ ? — Wear it with pride, and cheer for the Lions. — And the famous ({gnums[3]})___ ? — Two anthems, one game. Enjoy Munich. — I will ! See you on ({gnums[4]})___ ! — Have a good day.", 20.5)
bf.para("Levels : 145–148 [A2] · 149 [B1]", 19.5, "sans", False, GREY, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "Schrijven", "Open vraag — punten in het schrijfblok; voorbeeldtekst in het kader op pagina 8", "Beoordeel op punten")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　WRITING　Schrijven [B1]", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words) : « My Wednesday, November 11 ». Tell us : did you stand still at eleven, what did you wear, what did you watch on Friday — and one sentence about the game in Munich on Sunday. The best texts will appear in VOL.4 (page 7, « Readers' Corner »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "Schrijf in het Engels (80–100 woorden): «Mijn woensdag 11 november». Vertel of je om 11 uur stil hebt gestaan, wat je droeg, wat je vrijdag hebt gezien — en één zin over de wedstrijd van zondag in München.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, "MODEL　Voorbeeldtekst", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "On Wednesday, November 11, our school stopped for two minutes. At eleven o'clock, the hall went quiet, and I thought about the soldiers of the First World War. In the evening, we watched the news from London, and my mother wore her poppy at dinner. On Friday, we baked 26 cakes for Children in Need, and Pudsey smiled from the television. On Sunday, we watched the game from Munich. It was a week of silence, kindness and sport — and I slept well, because I had remembered.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANSWERS　Alle antwoorden met toelichting (pagina 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Pagina {pg} —", 16, "sans", True, OLIVE, 1.26, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13.5, "sans", False, INK, 1.26, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
