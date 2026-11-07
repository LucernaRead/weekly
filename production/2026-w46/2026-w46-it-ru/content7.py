# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LINGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LINGUA · ЯЗЫК", "La Lucerna", "Язык в фокусе · Tre livelli, tre strumenti · Три уровня, три инструмента")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · IL FUTURO", 24)
a.para("Per i piani della settimana usiamo il futuro semplice: andremo a Cuneo, assaggeremo il vino nuovo, guarderemo Italia–Francia. Le forme sono regolari: andare → andrò, assaggiare → assaggerò, guardare → guarderò.", 21.5)
a.para("E per il tempo: ci sarà il sole di San Martino, durerà tre giorni. Il verbo è durare, regolare.", 21.5)
a.bridge("Планы в будущем времени: andremo, assaggeremo, guarderemo.")
a.ex("A2", "Дополнить предложения", "andremo", "andare, будущее время, noi: andremo",
     "Mercoledì noi ___ (andare) a Cuneo.", instr="Вставить", size=20.5, gap=10)
a.ex("A2", "Дополнить предложения", "assaggeremo", "assaggiare, будущее время, noi: assaggeremo",
     "Noi ___ (assaggiare) il vino nuovo.", instr="Вставить", size=20.5, gap=10)
a.ex("A2", "Дополнить предложения", "guarderemo", "guardare, будущее время, noi: guarderemo",
     "Giovedì noi ___ (guardare) Italia–Francia.", instr="Вставить", size=20.5, gap=10)
a.ex("A2", "Один ответ", "B", "durerà — будущее время глагола durare",
     "L'estate di San Martino... A. dura tre giorni · B. durerà tre giorni · C. durava tre giorni", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · IL PASSATO PROSSIMO", 24)
b.para("Per raccontare il weekend usiamo il passato prossimo: ausiliare + participio. Con essere — per verbi come arrivare e andare — il participio cambia con la persona: è arrivato (il treno), sono andati (i visitatori).", 21.5)
b.para("Con avere: abbiamo assaggiato, ha aperto. Il participio con avere non cambia.", 21.5)
b.bridge("Прошедшее время — passato prossimo: arrivare/andare и др. с essere, причастие согласуется в роде и числе; с avere причастие не меняется.")
b.ex("B1", "Дополнить предложения", "è arrivato", "arrivare с essere: è arrivato",
     "Il Treno Storico ___ (arrivare) a Cremona.", instr="Вставить", size=20.5, gap=10)
b.ex("B1", "Дополнить предложения", "abbiamo assaggiato", "assaggiare с avere",
     "Noi ___ (assaggiare) il torrone a Cremona.", instr="Вставить", size=20.5, gap=10)
b.ex("B1", "Дополнить предложения", "sono andati", "andare с essere, мн. ч.: sono andati",
     "I visitatori ___ (andare) a Perugia.", instr="Вставить", size=20.5, gap=10)
b.ex("B1", "Один ответ", "B", "aprire с avere + неизменяемое причастие",
     "Perugia ___ Eurochocolate. A. è aperta · B. ha aperto · C. sono aperti", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · IL CONGIUNTIVO", 24)
c.para("Con «è probabile che», «è possibile che» e «bisogna che» usiamo il congiuntivo: piova (piovere), nevichi (nevicare), sia (essere). È la grammatica della probabilità, la stessa di pagina 6.", 21.5)
c.para("Ma dopo «so che» e «i giornali scrivono che» resta l'indicativo: il sole torna, la Festa del Torrone è a Cremona. Opinioni sì, fatti con l'indicativo.", 21.5)
c.bridge("После è probabile che / è possibile che / bisogna che — сослагательное наклонение; после so che / scrivono che — изъявительное.")
c.ex("B2", "Дополнить предложения", "piova", "è probabile che + сослагательное наклонение: piova",
     "È probabile che domani ___ (piovere) in pianura.", instr="Вставить", size=20.5, gap=10)
c.ex("B2", "Дополнить предложения", "nevichi", "è possibile che + сослагательное наклонение: nevichi",
     "È possibile che in montagna ___ (nevicare) nel weekend.", instr="Вставить", size=20.5, gap=10)
c.ex("B2", "Дополнить предложения", "sia", "bisogna che + сослагательное наклонение: sia",
     "Bisogna che la cifra ___ (essere) chiara per tutti.", instr="Вставить", size=20.5, gap=10)
c.ex("B2", "Один ответ", "B", "so che + изъявительное наклонение: torna",
     "«So che il sole...» A. torni · B. torna · C. tornare", size=20.5, gap=10)
c.end_report()

# ---- col 3: errori tipici + parola + lettori ----
bx = COLX[3]
errs = [
    ("«Fa freddi.»", "→ «Fa freddo.» Dopo fa, freddo non cambia mai: è invariabile.", "после fa слово freddo не изменяется"),
    ("«È probabile che piove.»", "→ «È probabile che piova.» Dopo è probabile che serve il congiuntivo.", "è probabile che + сослагательное наклонение"),
    ("«Ieri ho andato a Cremona.»", "→ «Ieri sono andato a Cremona.» Andare vuole essere, non avere.", "andare употребляется с essere"),
    ("«Il mosto diventano vino.»", "→ «Il mosto diventa vino.» Mosto è singolare, il verbo è singolare.", "mosto — единственное число, глагол тоже"),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 194
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORI TIPICI · ОШИБКИ", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 26
wt = "« il mosto » è il succo d'uva prima che diventi vino. Questa settimana vive a pagina 2, a San Martino."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("mosto = сусло/молодое вино. См. стр. 2: сусло становится вином.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PAROLA · СЛОВО НЕДЕЛИ", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "mosto = сусло/молодое вино. См. стр. 2: сусло становится вином.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 26
lt = "«Ciao! Questa settimana la redazione assaggia il vino nuovo e le castagne, e guarda Italia–Francia in televisione. E voi? Scriveteci!» — esempio della redazione"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Пример от редакции, а не письмо. Пока писем и лучших сочинений нет; обещание — VOL.4. Пишите нам.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "LETTERE DEI LETTORI", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Пример от редакции, а не письмо. Пока писем и лучших сочинений нет; обещание — VOL.4. Пишите нам.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frasi della settimana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASI DELLA SETTIMANA · ФРАЗЫ НЕДЕЛИ (дословно из статей выпуска)", 27, "sans", True, OLIVE)
quotes = [
    ("«tre giorni di sole dopo il primo freddo»", "Три солнечных дня после первых холодов.", "Pagina 1"),
    ("«il sole tornò a splendere»", "Солнце снова засияло.", "Pagina 1"),
    ("«Il cinema che sceglie da che parte stare»", "Кино, которое выбирает позицию.", "Pagina 2"),
    ("«Due notti azzurre, alle 20.45»", "Две «синие» ночи, 20.45.", "Pagina 1"),
    ("«arriva anche il Treno Storico Arlecchino»", "Придёт и исторический поезд «Арлекин».", "Pagina 3"),
    ("«le due partite di questa settimana sono decisive»", "Оба матча этой недели решающие.", "Pagina 4"),
    ("«un libro in mano, un film negli occhi»", "Книга в руке, фильм перед глазами.", "Pagina 5"),
    ("«approvato dal governo non vuol dire già legge»", "Одобрение правительства ещё не значит, что это уже закон.", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- prossima settimana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "LA PROSSIMA SETTIMANA · На следующей неделе (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Domenica 22 novembre: chiude la Festa del Torrone a Cremona. La Serie A torna il 21–23 novembre, con i risultati dell'11ª giornata. E poi: le vostre lettere vere e i testi migliori della pagina 8. A lunedì!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
