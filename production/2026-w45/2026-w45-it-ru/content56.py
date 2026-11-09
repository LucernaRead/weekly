# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · GIOVANI (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("GIOVANI　МОЛОДЁЖЬ", "La Lucerna", "LIVELLO B1　Dopo Lucca: cultura, cinema e weekend　После Лукки")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Dopo Lucca: la settimana giovane continua a Milano e Firenze", 32)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: B1")
f.para("Lucca Comics & Games si è chiusa domenica 1° novembre: la 60ª edizione, con il tema «Legacy», ha riempito le mura di Lucca dal 28 ottobre al 1° novembre. Per molti giovani è stata la festa più importante dell'autunno — e ora i cosplay tornano nell'armadio, ma la cultura continua.")
f.para("Da martedì 3 a domenica 8 novembre, a Milano, c'è il Forum Cultura: più di 50 eventi e aperture straordinarie di musei e biblioteche. Per i giovani è un'occasione da non perdere: molti eventi sono gratuiti, e il fine settimana il Forum si sposta alla Bovisa, al sito della Goccia.")
f.para("E da martedì 3 a lunedì 9 novembre, a Firenze, c'è il Festival dei Popoli, il festival del cinema documentario: storie vere da tutto il mondo, raccontate sullo schermo. Un festival per chi ama capire il mondo, non solo guardarlo.")
f.para("Nel weekend, poi, la scelta è dolce: la finale del Panettone a Milano e la Festa del Torrone a Cremona (pagina 3). Il consiglio della redazione: sabato si assaggia, domenica si guarda una partita — e lunedì si torna a scuola con qualcosa da raccontare.")
f.box("IL PIANO DELLA SETTIMANA", [
    ("1. Martedì: il Forum Cultura apre a Milano(вторник: Forum Cultura открывается в Милане)", "serif", False, INK, 21, 1.36),
    ("2. Mercoledì–giovedì: le coppe europee in TV(среда–четверг: еврокубки по ТВ)", "serif", False, INK, 21, 1.36),
    ("3. Venerdì: si prepara il weekend(пятница: готовимся к выходным)", "serif", False, INK, 21, 1.36),
    ("4. Sabato: assaggi a Milano o a Cremona(суббота: дегустации в Милане или Кремоне)", "serif", False, INK, 21, 1.36),
    ("5. Domenica: Serie A e rientro(воскресенье: Серия А и возвращение домой)", "serif", False, INK, 21, 1.36),
])
f.gloss("il cosplay = косплей-костюм · gratuito = бесплатный · il documentario = документальный фильм · lo schermo = экран")
f.end_report()

# col 3: castagne image + facts + e tu? (sequential)
ix = COLX[3]
image(p, "castagne.jpg", ix, 200, CW, 300)
cy3 = caption(p, ix, 500, CW, "Le castagne arrosto: il cibo di strada dell'autunno. Con il primo freddo, le piazze profumano di caldarroste — e il weekend giovane comincia così.",
              "Foto: Wikimedia Commons — CC0")
facts = ["Lucca Comics, 60ª edizione, tema «Legacy»: dal 28 ottobre al 1° novembre.",
         "Forum Cultura, Milano: dal 3 all'8 novembre, più di 50 eventi.",
         "Festival dei Popoli, Firenze: dal 3 al 9 novembre, cinema documentario."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "I GIOVANI IN NUMERI", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Dopo Lucca, dove vai: al Forum Cultura, al cinema o a una sagra? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("После Лукки: Forum Cultura, кино или сагре? Напишите два предложения!", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU?　А ВЫ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "После Лукки: Forum Cultura, кино или сагре? Напишите два предложения!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　УПРАЖНЕНИЯ СТРАНИЦЫ 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы — на странице 8　уровни смешаны: ищите по номеру", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P5-ex")
e.head("A　COMPRENSIONE", 25)
e.bridge("Прочитайте статью на странице 5 и выберите правильный ответ.")
e.ex("B1", "Один ответ", "B", "Lucca Comics — 60-й выпуск",
     "Lucca Comics & Games è alla sua... A. 50ª edizione · B. 60ª edizione · C. 21ª edizione", size=20, gap=8)
e.ex("B1", "Один ответ", "B", "Forum Cultura открывается 3 ноября",
     "Il Forum Cultura apre... A. il 2 novembre · B. il 3 novembre · C. il 7 novembre", size=20, gap=8)
e.ex("B1", "Один ответ", "C", "Festival dei Popoli — во Флоренции",
     "Il Festival dei Popoli è a... A. Milano · B. Lucca · C. Firenze", size=20, gap=8)
e.ex("B1", "Один ответ", "A", "У Forum Cultura более 50 мероприятий",
     "Il Forum Cultura ha... A. più di 50 eventi · B. 19 eventi · C. 5 eventi", size=20, gap=8)
e.ex("B1", "Один ответ", "A", "Тема Lucca Comics — «Legacy»",
     "Il tema di Lucca Comics è... A. «Legacy» · B. «Freddo» · C. «Tartufo»", size=20, gap=8)
e.head("B　LE PAROLE DEL TESTO", 25)
e.bridge("Дополните слова из рамки. Внимание: некоторые слова — во множественном числе.")
e.para("cosplay · gratuito · documentario · schermo · castagne · armadio", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Дополнить предложения", "armadio", "armadio = шкаф",
     "Dopo Lucca, i cosplay tornano nell'___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "gratuiti", "gratuiti = бесплатные (муж. р., мн. ч.)",
     "Molti eventi del Forum sono ___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "documentario", "documentario = документальный фильм",
     "Il Festival dei Popoli è un festival del cinema ___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "schermo", "schermo = экран",
     "Le storie vere si vedono sullo ___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "castagne", "castagne arrosto = жареные каштаны (мн. ч.)",
     "Le piazze profumano di ___ arrosto.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "cosplay", "cosplay = косплей-костюм",
     "Molti giovani preparano un ___ per Lucca.", instr="Вставьте", size=20, gap=8)
e.head("C　IL FUTURO", 25)
e.bridge("Дополните futuro semplice (будущее время).")
e.ex("B1", "Дополнить предложения", "andremo", "andare, будущее время, noi: andremo",
     "Sabato noi ___ (andare) a Milano per gli assaggi.", instr="Вставьте", size=20, gap=8)
e.ex("B2", "Дополнить предложения", "ci sarà", "esserci, будущее время: ci sarà (будет)",
     "Al Forum ___ (esserci) tanta gente giovane.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополнить предложения", "guarderemo", "guardare, будущее время, noi: guarderemo",
     "Domenica noi ___ (guardare) la Serie A.", instr="Вставьте", size=20, gap=8)
e.ex("B2", "Дополнить предложения", "durerà", "durare, будущее время: durerà",
     "La Festa del Torrone ___ (durare) fino al 22 novembre.", instr="Вставьте", size=20, gap=8)
e.head("D　VERO O FALSO?", 25)
e.ex("B1", "Верно или нет", "Vero", "У Forum Cultura более 50 мероприятий",
     "Il Forum Cultura ha più di 50 eventi. Vero o falso?", instr="Верно или нет", size=20, gap=8)
e.ex("B1", "Верно или нет", "Vero", "Festival dei Popoli — во Флоренции",
     "Il Festival dei Popoli è a Firenze. Vero o falso?", instr="Верно или нет", size=20, gap=8)
e.ex("B2", "Верно или нет", "Falso", "Lucca Comics заканчивается не 8 ноября",
     "Lucca Comics chiude l'8 novembre. Vero o falso?", instr="Верно или нет", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-giovani.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · APPROFONDIMENTO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("APPROFONDIMENTO　РАЗБОР", "La Lucerna", "LIVELLO B2　Leggere le previsioni　Как читать прогнозы")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1520, tag="P6-main")
f.title("Come si legge una previsione: probabilità, non certezze", 32)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: B2　Il meteo e i numeri")
f.para("Le previsioni di questa settimana parlano di un inizio di novembre più freddo della media in gran parte d'Italia, con piogge sul versante adriatico e la prima neve leggera in montagna. Le previsioni si basano su modelli come quello del Centro europeo (ECMWF): il computer calcola tanti scenari possibili e dice quale è più probabile.")
f.para("La parola chiave è «probabilità»: quando leggi «probabilità di pioggia sopra la media», non significa «pioverà di sicuro». Significa che, in passato, in situazioni simili, ha piovuto più spesso della media. Una probabilità alta non è una certezza, e una probabilità bassa non è un «no».")
f.para("Perché le previsioni cambiano? Perché l'atmosfera è un sistema che cambia in fretta: un piccolo errore all'inizio diventa grande dopo qualche giorno. Per questo i meteorologi aggiornano le previsioni ogni giorno — e il lettore saggio controlla sempre il bollettino ufficiale più recente, prima di uscire.")
f.para("E la manovra? La legge di bilancio resta il tema politico della settimana a Roma. Il Documento programmatico di bilancio (DPB), mandato a Bruxelles il 15 ottobre, prevede per il 2027 una crescita del +0,8% e un deficit del 3,4% del PIL; il voto era atteso intorno al 28 ottobre, e il punto difficile resta il contributo chiesto a banche e assicurazioni. Al momento di andare in stampa, l'esito del voto non era ancora confermato: qui riportiamo solo la data attesa, il punto difficile e i numeri del DPB, senza indicare alcun esito.")
f.bridge("На момент сдачи номера результат голосования 28 октября ещё не подтверждён: этот выпуск называет только ожидаемую дату, спорный вопрос и цифры DPB, но не результат.")
f.gloss("la probabilità = вероятность · la media = среднее значение · il modello = прогностическая модель · il bollettino = сводка погоды · aggiornare = обновлять")
f.end_report()

# col 3: timeline + leggere i numeri (sequential, measured)
bx = COLX[3]
p.rect(bx, 200, CW, 640, fill=BOX)
p.text(bx + 22, 240, "LA STRADA DEL FREDDO", 22, "sans", True, OLIVE)
steps = [
    ("FINE OTT.", "Le previsioni parlano di un novembre più freddo della media."),
    ("LUN 2 NOV.", "Arriva il primo freddo: piogge sul versante adriatico."),
    ("MAR 3 NOV.", "Apre il Forum Cultura a Milano: la cultura non ha paura del freddo."),
    ("SAB 7 NOV.", "Weekend dolce: Panettone a Milano, Torrone a Cremona."),
]
sy3 = 282
for w, t in steps:
    p.text(bx + 22, sy3 + 21, w, 20, "sans", True, OLIVE)
    sy3 = p.para(bx + 164, sy3 + 21, t, 21, "serif", False, INK, CW - 186, 1.4) + 16
by3 = 866
bb = ("Davanti a una previsione, fai tre domande: chi la pubblica? Quando? "
      "È una probabilità o una certezza? Senza queste tre risposte, un numero dice poco.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f0eee5")
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LEGGERE I NUMERI", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh)

# ---- Practice-data chart (explicitly labeled as exercise data) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, OLIVE, 2)
p.text(MX, gy + 10, "LE MINIME DI ESEMPIO　ПРИМЕРЫ МИНИМАЛЬНЫХ ТЕМПЕРАТУР (DATI INVENTATI PER L'ESERCIZIO)", 26, "sans", True, OLIVE)
dpb = [("Torino", 3.0),
       ("Milano", 4.0),
       ("Bologna", 5.0),
       ("Roma", 9.0),
       ("Napoli", 12.0)]
bx1, bw_, bhh = MX, 2 * CW + GUT, 322
p.rect(bx1, gy + 28, bw_, bhh, fill=BOX)
p.text(bx1 + 22, gy + 68, "MINIME DI ESEMPIO　gradi, dati inventati", 21, "sans", True, INK)
yy = gy + 96
for lab, v in dpb:
    p.text(bx1 + 22, yy + 24, lab, 20, "serif", True, INK)
    labw = text_w(lab, "serif", True, 20)
    p.rect(bx1 + 40 + labw, yy + 6, v * 34, 22, fill=OLIVE)
    p.text(bx1 + 58 + labw + v * 34, yy + 24, f"{v:.0f}°", 20.5, "serif", False, INK)
    yy += 38
p.para(bx1 + 22, gy + bhh - 26, "Questi numeri sono inventati per l'esercizio: servono per imparare a leggere un grafico, NON sono previsioni reali.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right box: probabilities
bx2 = COLX[2]
p.rect(bx2, gy + 28, bw_, bhh, fill=BOX)
p.text(bx2 + 22, gy + 68, "PROBABILITÀ　ВЕРОЯТНОСТЬ", 21, "sans", True, INK)
p.para(bx2 + 22, gy + 118, "Probabilità alta ≠ certezza", 23, "serif", True, INK, bw_ - 44, 1.35)
p.para(bx2 + 22, gy + 158, "Probabilità bassa ≠ «no»", 23, "serif", True, INK, bw_ - 44, 1.35)
p.para(bx2 + 22, gy + 198, "Il bollettino ufficiale più recente vale più di una previsione di una settimana fa.", 19.5, "serif", False, INK, bw_ - 44, 1.4)
p.para(bx2 + 22, gy + bhh - 62, "Le previsioni vere si aggiornano ogni giorno: controllale prima di uscire.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)

# ---- P6 exercises ----
ey = 1930
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　УПРАЖНЕНИЯ СТРАНИЦЫ 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы — на странице 8　уровни смешаны: ищите по номеру", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P6-ex")
e.head("A　LEGGERE IL GRAFICO", 25)
e.bridge("Посмотрите на учебную диаграмму выше и выберите правильный ответ.")
e.ex("B2", "Один ответ", "B", "В примерных данных самый холодный — Турин, 3°",
     "La città più fredda del grafico è... A. Milano · B. Torino · C. Napoli", size=18, gap=2)
e.ex("B2", "Один ответ", "A", "В примерных данных самый тёплый — Неаполь, 12°",
     "La città più calda del grafico è... A. Napoli · B. Roma · C. Bologna", size=18, gap=2)
e.ex("B2", "Один ответ", "B", "12 − 9 = 3",
     "La differenza tra Napoli (12°) e Roma (9°) è... A. 2° · B. 3° · C. 4°", size=18, gap=2)
e.ex("B2", "Один ответ", "A", "4 + 5 = 9",
     "Milano (4°) e Bologna (5°) insieme fanno... A. 9° · B. 10° · C. 8°", size=18, gap=2)
e.ex("B2", "Один ответ", "B", "Данные диаграммы — учебные, не прогнозы",
     "I numeri del grafico sono... A. previsioni reali · B. dati inventati per l'esercizio · C. temperature di ieri", size=18, gap=2)
e.ex("B2", "Один ответ", "A", "Высокая вероятность — ещё не уверенность",
     "Una probabilità alta... A. non è una certezza · B. è una certezza · C. è un errore", size=18, gap=2)
e.head("B　COMPRENSIONE", 25)
e.ex("B2", "Один ответ", "B", "Прогнозы основаны на моделях, например ECMWF",
     "Le previsioni si basano su... A. la fortuna · B. modelli come l'ECMWF · C. i giornali", size=18, gap=2)
e.ex("B2", "Один ответ", "A", "Прогнозы меняются: атмосфера меняется быстро",
     "Le previsioni cambiano perché... A. l'atmosfera cambia in fretta · B. i computer si rompono · C. nessuno le legge", size=18, gap=2)
e.ex("B2", "Один ответ", "A", "DPB был отправлен в Брюссель 15 октября",
     "Il DPB è stato mandato a Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=18, gap=2)
e.ex("B2", "Один ответ", "B", "Прогноз роста на 2027 год: +0,8 %",
     "La crescita prevista per il 2027 è... A. +3,4% · B. +0,8% · C. +5%", size=18, gap=2)
e.head("C　IL CONGIUNTIVO", 25)
e.ex("B2", "Дополнить предложения", "piova", "è probabile che + сослагательное наклонение: piova",
     "È probabile che domani ___ (piovere) sul versante adriatico.", instr="Вставьте", size=18, gap=2)
e.ex("B2", "Дополнить предложения", "nevichi", "è possibile che + сослагат. наклонение: nevichi",
     "È possibile che in montagna ___ (nevicare) nel weekend.", instr="Вставьте", size=18, gap=2)
e.ex("B2", "Дополнить предложения", "controllino", "bisogna che + сослагат. наклонение: controllino",
     "Bisogna che i lettori ___ (controllare) il bollettino più recente.", instr="Вставьте", size=18, gap=2)
e.ex("B2", "Дополнить предложения", "sia", "è importante che + сослагательное наклонение: sia",
     "È importante che la previsione ___ (essere) chiara per tutti.", instr="Вставьте", size=18, gap=2)
e.head("D　LE PAROLE DEL METEO", 25)
e.bridge("Дополните слова из рамки: probabilità · media · bollettino · modello")
e.ex("B2", "Дополнить предложения", "probabilità", "probabilità = вероятность",
     "La ___ di pioggia non è una certezza.", instr="Вставьте", size=18, gap=2)
e.ex("B2", "Дополнить предложения", "media", "media = среднее значение",
     "Un novembre più freddo della ___ è un novembre freddo.", instr="Вставьте", size=18, gap=2)
e.ex("B2", "Дополнить предложения", "bollettino", "bollettino = сводка погоды",
     "Prima di uscire, controlla il ___ più recente.", instr="Вставьте", size=18, gap=2)
e.ex("B2", "Дополнить предложения", "modello", "modello = прогностическая модель",
     "L'ECMWF è un ___ di previsione europeo.", instr="Вставьте", size=18, gap=2)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-approfondimento.svg")
print("P6 saved, exercises so far:", len(REG))
