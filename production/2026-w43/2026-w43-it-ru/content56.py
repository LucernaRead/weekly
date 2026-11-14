# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · GIOVANI (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("GIOVANI　МОЛОДЁЖЬ", "La Lucerna", "LIVELLO B1　Lucca Comics e il cinema dei giovani　Лукка и молодёжное кино")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Lucca si prepara: tra una settimana è Comics & Games", 32)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: B1")
f.para("Manca una settimana all'evento giovane più grande d'Italia: Lucca Comics & Games. La 60ª edizione, con il tema «Legacy», apre mercoledì 28 ottobre e chiude domenica 1° novembre, il giorno di Ognissanti.")
f.para("I numeri sono da record: al massimo 80.000 visitatori al giorno dentro le mura di Lucca. I biglietti costano da 26,50 a 34,50 euro; l'abbonamento per i cinque giorni costa 95 euro.")
f.para("Questa è la settimana dei preparativi: il termine per ricevere il braccialetto a casa è scaduto il 16 ottobre, e ora i fan preparano i cosplay, studiano le code e organizzano il viaggio. Per molti giovani è la festa più importante dell'autunno.")
f.para("E per chi resta a Roma? La Festa del Cinema ha una sezione per i giovani: Alice nella città. Giovedì 22 ottobre: la presentazione dell'app Rome City of Film e le serate di cinema muto alla Casa del Cinema — film di cento anni fa, grandi anche senza parole.")
f.para("Tra i titoli di cui parlano i giornali: un documentario sulla sciatrice Federica Brignone e la serie VisionQuest con Paul Bettany. Molte sono anteprime: film che il pubblico vede per la prima volta.")
f.box("IL PIANO DELLA SETTIMANA", [
    ("1. Finisci il cosplay: manca una settimana(доделать костюм: осталась неделя)", "serif", False, INK, 21, 1.36),
    ("2. Controlla il braccialetto e il biglietto(проверить браслет и билет)", "serif", False, INK, 21, 1.36),
    ("3. Studia la mappa di Lucca e le code(изучить карту Лукки и очереди)", "serif", False, INK, 21, 1.36),
    ("4. Giovedì: serata di cinema muto a Roma(четверг: вечер немого кино в Риме)", "serif", False, INK, 21, 1.36),
    ("5. Domenica: ultimo giorno della Festa del Cinema(воскресенье: последний день фестиваля)", "serif", False, INK, 21, 1.36),
])
f.gloss("il braccialetto = браслет (пропуск) · la coda = очередь · l'anteprima = премьера · muto = немой (о кино).")
f.end_report()

# col 3: chaplin image + facts + e tu? + coffee box (sequential)
ix = COLX[3]
image(p, "chaplin.jpg", ix, 200, CW, 300)
cy3 = caption(p, ix, 500, CW, "Charlie Chaplin in «La febbre dell'oro» (1925): cento anni fa il cinema era muto. Giovedì 22 ottobre, alla Casa del Cinema di Roma, una serata è dedicata ai film muti.",
              "Foto: Wikimedia Commons — dominio pubblico")
facts = ["60ª edizione, tema «Legacy»: dal 28 ottobre al 1° novembre.",
         "Massimo 80.000 visitatori al giorno, dentro le mura di Lucca.",
         "Biglietti: 26,50–34,50 €; abbonamento di 5 giorni: 95 €."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LUCCA IN NUMERI", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Vai a Lucca o resti a guardare film? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Вы едете в Лукку или остаётесь смотреть кино? Напишите две фразы и пришлите нам.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU?　А ВЫ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Вы едете в Лукку или остаётесь смотреть кино? Напишите две фразы и пришлите нам.", 20, "sans", False, GREY, CW - 44, 1.42)
ky3 = ey3 + eh + 26
kb = ("Secondo Google, nel 2026 le ricerche italiane sul caffè non sono mai state così alte: l'espresso resta il numero uno, la moka resta amatissima in Italia, e crescono il flat white e il latte d'avena. "
      "Record anche per le ricerche sulla «skincare coreana», la cura della pelle in stile coreano.")
kh = 62 + len(wrap(kb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(ix, ky3, CW, kh, fill=BOX)
yy3 = ky3 + 16
p.text(ix + 22, yy3 + 26, "COSA CERCANO GLI ITALIANI", 22, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, kb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P5 col3 ends", ky3 + kh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　УПРАЖНЕНИЯ СТРАНИЦЫ 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы — на странице 8　уровни смешаны: ищите по номеру", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P5-ex")
e.head("A　COMPRENSIONE", 25)
e.expl("Прочитайте статью на странице 5 и выберите правильный ответ.")
e.ex("B1", "Выбор ответа", "B", "Lucca Comics — 60-й выпуск",
     "Lucca Comics & Games è alla sua... A. 50ª edizione · B. 60ª edizione · C. 21ª edizione", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "открытие в среду, 28 октября",
     "Il festival di Lucca apre... A. il 25 ottobre · B. il 28 ottobre · C. il 1° novembre", size=20, gap=8)
e.ex("B1", "Выбор ответа", "C", "абонемент на 5 дней — 95 евро",
     "L'abbonamento per cinque giorni costa... A. 34,50 € · B. 80 € · C. 95 €", size=20, gap=8)
e.ex("B1", "Выбор ответа", "A", "Alice nella città — молодёжная секция",
     "Alice nella città è... A. una sezione per i giovani · B. un'app · C. un film muto", size=20, gap=8)
e.ex("B1", "Выбор ответа", "A", "срок получения браслета домой истёк 16 октября",
     "Il termine per il braccialetto a casa è scaduto... A. il 16 ottobre · B. il 22 ottobre · C. il 28 ottobre", size=20, gap=8)
e.head("B　LE PAROLE DEL TESTO", 25)
e.expl("Заполните пропуски словами из рамки. Внимание: некоторые слова нужны во множественном числе.")
e.para("cosplay · braccialetto · coda · anteprima · muto · abbonamento", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Дополните предложение", "braccialetto", "braccialetto = браслет",
     "Per entrare a Lucca serve il ___ al polso.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "anteprima", "anteprima = премьера",
     "Un film visto per la prima volta dal pubblico è un'___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "muti", "muti = немые (муж. род, мн. ч.)",
     "I film di cento anni fa sono ___: senza parole.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "abbonamento", "abbonamento = абонемент",
     "Con l'___ di cinque giorni entri sempre.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "coda", "coda = очередь",
     "Davanti ai padiglioni c'è sempre una lunga ___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "cosplay", "cosplay = косплей, костюм персонажа",
     "Molti fan preparano un ___ da indossare a Lucca.", instr="Вставьте", size=20, gap=8)
e.head("C　IL FUTURO", 25)
e.expl("Дополните глаголами в будущем времени (futuro semplice).")
e.ex("B1", "Дополните предложение", "prepareremo", "preparare, будущее время, noi: prepareremo",
     "Domani noi ___ (preparare) i cosplay.", instr="Вставьте", size=20, gap=8)
e.ex("B2", "Дополните предложение", "andrò", "andare, будущее время неправильное: andrò",
     "La prossima settimana io ___ (andare) a Lucca.", instr="Вставьте", size=20, gap=8)
e.ex("B2", "Дополните предложение", "ci saranno", "esserci, будущее время: ci saranno",
     "A Lucca ___ (esserci) migliaia di giovani.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "chiuderà", "chiudere, будущее время: chiuderà",
     "Il festival di Lucca ___ (chiudere) il 1° novembre.", instr="Вставьте", size=20, gap=8)
e.head("D　VERO O FALSO?", 25)
e.ex("B1", "Верно или неверно", "Vero", "не более 80 000 посетителей в день",
     "A Lucca entrano al massimo 80.000 visitatori al giorno. Vero o falso?", instr="Верно или нет", size=20, gap=8)
e.ex("B1", "Верно или неверно", "Vero", "вечера немого кино — в Casa del Cinema",
     "Le serate di cinema muto sono alla Casa del Cinema. Vero o falso?", instr="Верно или нет", size=20, gap=8)
e.ex("B2", "Верно или неверно", "Falso", "espresso по-прежнему запрос № 1 о кофе",
     "L'espresso non è più la ricerca numero uno sul caffè. Vero o falso?", instr="Верно или нет", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-giovani.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · APPROFONDIMENTO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("APPROFONDIMENTO　РАЗБОР", "La Lucerna", "LIVELLO B2　La manovra 2027　Бюджетный закон на 2027 год")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1520, tag="P6-main")
f.title("La manovra 2027: perché il voto slitta al 28 ottobre", 32)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: B2　La politica nazionale italiana")
f.para("È la storia politica italiana della settimana: la manovra, la legge di bilancio per il 2027. Lunedì 19 ottobre i leader della coalizione si sono incontrati a Palazzo Chigi, a Roma. Ma il voto del Consiglio dei ministri non arriva venerdì 23 ottobre, come previsto: slitta a mercoledì 28 ottobre circa.")
f.para("Perché il rinvio? Il punto difficile è il contributo di circa 5 miliardi di euro chiesto a banche e assicurazioni. La cifra è nel Documento programmatico di bilancio (il DPB), il piano che l'Italia ha mandato a Bruxelles il 15 ottobre.")
f.para("Il DPB pubblica le previsioni per il 2027: la crescita è stimata a +0,8% e il deficit è al 3,4% del PIL, il prodotto interno lordo. Sono previsioni, non risultati: numeri che descrivono un piano, non ancora la realtà.")
f.para("Dove vanno i soldi? Il piano prevede circa 5 miliardi per le famiglie e le spese sociali e circa 3,4 miliardi per aiutare le imprese. In totale, la manovra vale circa 23,5 miliardi di euro.")
f.para("Per il lettore, la lezione è una: leggi le date e le fonti. Un voto previsto non è un voto fatto: una previsione non è un dato finale. Mercoledì 28 ottobre sapremo se il Consiglio dei ministri approva il testo — La Lucerna lo racconterà nel prossimo numero.")
f.gloss("la manovra = бюджетный закон · il rinvio = перенос · i miliardi = миллиарды · il deficit = дефицит · la previsione = прогноз.")
f.end_report()

# col 3: timeline + leggere i numeri (sequential, measured)
bx = COLX[3]
p.rect(bx, 200, CW, 640, fill=BOX)
p.text(bx + 22, 240, "LA STRADA DELLA MANOVRA", 22, "sans", True, OLIVE)
steps = [
    ("15 OTT.", "L'Italia manda a Bruxelles il DPB, il documento con il piano di bilancio."),
    ("19 OTT.", "Vertice della coalizione a Palazzo Chigi: il testo non è ancora pronto."),
    ("23 OTT.", "La data prevista per il voto del Consiglio dei ministri — ma slitta."),
    ("28 OTT.", "La nuova data attesa per il voto (circa): la decisione arriva la prossima settimana."),
]
sy3 = 282
for w, t in steps:
    p.text(bx + 22, sy3 + 21, w, 20, "sans", True, OLIVE)
    sy3 = p.para(bx + 164, sy3 + 21, t, 21, "serif", False, INK, CW - 186, 1.4) + 16
by3 = 866
bb = ("Davanti a un numero politico, fai tre domande: chi lo pubblica? Quando? "
      "È una previsione o un dato finale? Senza queste tre risposte, una cifra dice poco.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f0eee5")
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LEGGERE I NUMERI", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh)

# ---- DPB chart (published figures, honestly captioned) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, OLIVE, 2)
p.text(MX, gy + 10, "LE CIFRE DEL DPB　ЦИФРЫ (Documento programmatico di bilancio, 15 ottobre 2026)", 26, "sans", True, OLIVE)
dpb = [("Banche e assicurazioni (contributo chiesto)", 5.0),
       ("Famiglie e spese sociali", 5.0),
       ("Aiuto alle imprese", 3.4)]
bx1, bw_, bhh = MX, 2 * CW + GUT, 322
p.rect(bx1, gy + 28, bw_, bhh, fill=BOX)
p.text(bx1 + 22, gy + 68, "TRE VOCI DEL PIANO　miliardi di euro", 21, "sans", True, INK)
yy = gy + 96
for lab, v in dpb:
    p.text(bx1 + 22, yy + 24, lab, 20, "serif", True, INK)
    labw = text_w(lab, "serif", True, 20)
    p.rect(bx1 + 40 + labw, yy + 6, v * 34, 22, fill=OLIVE)
    p.text(bx1 + 58 + labw + v * 34, yy + 24, f"{v:.1f}".replace(".", ",") + " miliardi", 20.5, "serif", False, INK)
    yy += 38
p.para(bx1 + 22, gy + bhh - 62, "Tre voci pubblicate nel DPB del 15 ottobre — non è il totale della manovra (circa 23,5 miliardi).", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right box: percentages
bx2 = COLX[2]
p.rect(bx2, gy + 28, bw_, bhh, fill=BOX)
p.text(bx2 + 22, gy + 68, "LE PREVISIONI 2027　ПРОГНОЗЫ НА 2027 ГОД", 21, "sans", True, INK)
p.para(bx2 + 22, gy + 118, "Crescita stimata: +0,8%", 23, "serif", True, INK, bw_ - 44, 1.35)
p.para(bx2 + 22, gy + 158, "Deficit: 3,4% del PIL", 23, "serif", True, INK, bw_ - 44, 1.35)
p.para(bx2 + 22, gy + 198, "Sono previsioni del piano, non dati finali: il futuro si scrive con i numeri che arrivano dopo.", 19.5, "serif", False, INK, bw_ - 44, 1.4)
p.para(bx2 + 22, gy + bhh - 62, "Fonte: DPB, documento mandato a Bruxelles il 15 ottobre 2026.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)

# ---- P6 exercises ----
ey = 1930
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　УПРАЖНЕНИЯ СТРАНИЦЫ 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы — на странице 8　уровни смешаны: ищите по номеру", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P6-ex")
e.head("A　LEGGERE IL GRAFICO", 25)
e.expl("Смотрите таблицы и выберите ответ.")
e.ex("B2", "Выбор ответа", "B", "взнос у банков и страховых — около 5 млрд",
     "Il contributo chiesto a banche e assicurazioni è di... A. 3,4 miliardi · B. 5 miliardi · C. 23,5 miliardi", size=18, gap=2)
e.ex("B2", "Выбор ответа", "A", "на семьи и соц. расходы — около 5 млрд",
     "Per le famiglie e le spese sociali il piano prevede... A. 5 miliardi · B. 3,4 miliardi · C. 0,8 miliardi", size=18, gap=2)
e.ex("B2", "Выбор ответа", "B", "5 + 5 + 3,4 = 13,4 (это не итог)",
     "Le tre voci del grafico, insieme, fanno... A. 10 miliardi · B. 13,4 miliardi · C. 23,5 miliardi", size=18, gap=2)
e.ex("B2", "Выбор ответа", "A", "5 − 3,4 = 1,6",
     "La differenza tra le famiglie (5) e le imprese (3,4) è... A. 1,6 miliardi · B. 2,6 miliardi · C. 8,4 miliardi", size=18, gap=2)
e.ex("B2", "Выбор ответа", "B", "прогноз роста на 2027 год: +0,8%",
     "La crescita prevista per il 2027 è... A. +3,4% · B. +0,8% · C. +5%", size=18, gap=2)
e.ex("B2", "Выбор ответа", "A", "дефицит — 3,4% ВВП",
     "Il deficit previsto è il... A. 3,4% del PIL · B. 34% del PIL · C. 0,8% del PIL", size=18, gap=2)
e.head("B　COMPRENSIONE", 25)
e.ex("B2", "Выбор ответа", "B", "голосование перенесено примерно на 28 октября",
     "Il voto del Consiglio dei ministri... A. è già avvenuto il 19 ottobre · B. slitta a circa il 28 ottobre · C. è cancellato", size=18, gap=2)
e.ex("B2", "Выбор ответа", "A", "трудный пункт — взнос банков и страховых компаний",
     "Il punto difficile della manovra è... A. il contributo di banche e assicurazioni · B. il nome della legge · C. la data del voto", size=18, gap=2)
e.ex("B2", "Выбор ответа", "A", "DPB отправлен в Брюссель 15 октября",
     "Il DPB è stato mandato a Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=18, gap=2)
e.ex("B2", "Выбор ответа", "B", "это прогнозы, а не итоговые данные",
     "Le cifre del DPB sono... A. risultati finali · B. previsioni · C. errori di stampa", size=18, gap=2)
e.head("C　IL CONGIUNTIVO", 25)
e.ex("B2", "Дополните предложение", "slitti", "è possibile che + congiuntivo: slitti",
     "È possibile che il voto ___ (slittare) ancora.", instr="Вставьте", size=18, gap=2)
e.ex("B2", "Дополните предложение", "controllino", "bisogna che + congiuntivo: controllino",
     "Bisogna che i lettori ___ (controllare) sempre la fonte.", instr="Вставьте", size=18, gap=2)
e.ex("B2", "Дополните предложение", "riunisce", "scrivono che + изъявительное: riunisce",
     "I giornali scrivono che il Consiglio si ___ (riunire) mercoledì 28.", instr="Вставьте", size=18, gap=2)
e.ex("B2", "Дополните предложение", "sia", "è importante che + congiuntivo: sia",
     "È importante che la manovra ___ (essere) chiara per tutti.", instr="Вставьте", size=18, gap=2)
e.head("D　LE PAROLE DEL DIBATTITO", 25)
e.expl("Заполните пропуски словами из рамки.")
e.ex("B2", "Дополните предложение", "manovra", "manovra = бюджетный закон",
     "La legge di bilancio si chiama anche la ___.", instr="Вставьте", size=18, gap=2)
e.ex("B2", "Дополните предложение", "miliardo", "un miliardo = миллиард",
     "Un ___ è mille milioni di euro.", instr="Вставьте", size=18, gap=2)
e.ex("B2", "Дополните предложение", "rinvio", "rinvio = перенос",
     "Il voto arriva più tardi del previsto: è un ___.", instr="Вставьте", size=18, gap=2)
e.ex("B2", "Дополните предложение", "previsione", "previsione = прогноз",
     "Un numero che descrive il futuro, non il presente, è una ___.", instr="Вставьте", size=18, gap=2)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-approfondimento.svg")
print("P6 saved, exercises so far:", len(REG))
