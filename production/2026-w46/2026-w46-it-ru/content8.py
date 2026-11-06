# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · ПРОВЕРКА И ОТВЕТЫ", "La Lucerna", "Страница 8 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "Текст с пропусками", "B", "Святой Мартин = San Martino",
     "Mercoledì 11 novembre è ___. (A. Natale · B. San Martino)", size=15.5, gap=1)
f.ex("B1", "Текст с пропусками", "A", "Сусло становится молодым вином",
     "A San Martino ogni mosto diventa ___. (A. vino · B. latte)", size=15.5, gap=1)
f.ex("B1", "Текст с пропусками", "A", "Италия–Франция на «Сан-Сиро»",
     "Italia–Francia si gioca a ___. (A. San Siro · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Текст с пропусками", "A", "Шоколадный фестиваль открывается в пятницу",
     "Eurochocolate apre venerdì a ___. (A. Perugia · B. Cuneo)", size=15.5, gap=1)
f.ex("B1", "Текст с пропусками", "B", "Фестиваль Torrone — в Кремоне",
     "La Festa del Torrone continua a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "Текст с пропусками", "B", "Festival dei Popoli: 86 фильмов",
     "Il Festival dei Popoli ha presentato ___ film. (A. 50 · B. 86)", size=15.5, gap=1)
f.ex("B1", "Текст с пропусками", "A", "Бельгия–Италия в воскресенье вечером",
     "Belgio–Italia si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "Текст с пропусками", "B", "Scrittorincittà проходит в Кунео",
     "Scrittorincittà è a ___. (A. Milano · B. Cuneo)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "Один ответ", "B", "Лето святого Мартина длится три дня и чуть больше",
     "L'estate di San Martino dura... A. un mese · B. tre giorni e un pochino · C. un'ora", size=15.5, gap=1)
f.ex("A2", "Один ответ", "B", "Плащ Мартин разделил с нищим",
     "Martino divide... A. il pane · B. il mantello · C. il vino", size=15.5, gap=1)
f.ex("A2", "Один ответ", "A", "Шоколадный фестиваль: 32-й выпуск",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 67ª edizione", size=15.5, gap=1)
f.ex("B1", "Один ответ", "B", "Первая в группе — Франция, 10 очков",
     "Nel girone di Nations League, la Francia ha... A. 7 punti · B. 10 punti · C. 0 punti", size=15.5, gap=1)
f.ex("B1", "Один ответ", "C", "Фестиваль трюфелей в Альбе идёт до 6 декабря",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "Один ответ", "A", "DPB был отправлен 15 октября",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "Один ответ", "B", "Предложение правительства — ещё не закон",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "Один ответ", "B", "Festival dei Popoli завершился 8 ноября",
     "Il Festival dei Popoli si è chiuso... A. il 31 ottobre · B. l'8 novembre · C. il 15 novembre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Cuneo: mercoledì 11 novembre va a Scrittorincittà e ascolta un autore. Paolo vive a Cremona: sabato 14 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano Belgio–Italia: è San Martino, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "Один ответ", "B", "Джулия идёт на Scrittorincittà в среду",
     "Chi va a Scrittorincittà? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "Один ответ", "A", "Паоло едет в субботу на фестиваль Torrone",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Cuneo · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "Один ответ", "B", "Именно Джулия слушает автора",
     "L'autore è ascoltato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "Один ответ", "A", "Заголовок объединяет два города и два праздника",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "Составить предложения", "Mercoledì è San Martino.", "Сначала указание времени",
     "mercoledì / è / San Martino → ___", instr="Составить предложения", size=15.5, gap=1)
f.ex("B1", "Составить предложения", "Eurochocolate è a Perugia dal 13 novembre.", "Подлежащее + essere + место + дата",
     "Eurochocolate / è a Perugia / dal 13 novembre → ___", instr="Составить предложения", size=15.5, gap=1)
f.ex("B1", "Составить предложения", "A che ora gioca l'Italia?", "Вопросительная формула в начале",
     "a che ora / gioca / l'Italia / ? → ___", instr="Составить предложения", size=15.5, gap=1)
f.ex("B1", "Составить предложения", "Il vino nuovo si assaggia in cantina.", "подлежащее + глагол + место",
     "il vino nuovo / si assaggia / in cantina → ___", instr="Составить предложения", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "В день святого Мартина сусло становится вином.", "Сверить с оригиналом",
     "A San Martino ogni mosto diventa vino. → ___", instr="Переведите", size=15.5, gap=1)
f.ex("B1", "翻译", "В четверг вечером: Италия–Франция.", "si gioca = играется",
     "Giovedì sera si gioca Italia–Francia. → ___", instr="Переведите", size=15.5, gap=1)
f.ex("B1", "翻译", "В воскресенье вечером: Бельгия–Италия.", "si gioca = играется",
     "Domenica sera si gioca Belgio–Italia. → ___", instr="Переведите", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni cifra deve essere chiara.", "dovere = должен",
     "Каждая цифра должна быть ясной. → ___", instr="Переведите", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "Слова и значения",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["la parte del sistema fiscale, un livello di reddito",
             "i soldi che pagano una misura, la sua fonte",
             "la differenza tra spese ed entrate, in rosso",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra=бюджетный закон d", "deficit=дефицит c", "copertura=финансирование b", "scaglione=налоговая ступень a"],
            instr="Соединить")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "Текст с пропусками", "B", "torrone = нуга",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "Текст с пропусками", "A", "mandorle = миндаль",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "Текст с пропусками", "B", "quanto costa? = сколько стоит?",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "Текст с пропусками", "A", "pagare con carta = платить картой",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "Текст с пропусками", "B", "Фестиваль Torrone идёт до 22 ноября",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Mercoledì 11 novembre metto la sciarpa e vado in cantina: è San Martino e il vino nuovo si assaggia. "
          "A scuola parliamo della leggenda del mantello diviso e dell'estate di tre giorni. "
          "Sabato assaggio il torrone con la mia famiglia: preferisco quello di Cremona, con le mandorle e il miele. "
          "Giovedì sera guardiamo Italia–Francia in televisione, alle 20.45. "
          "Domenica, poi, il Belgio: due notti azzurre in una settimana. "
          "San Martino è arrivato, ma la settimana è dolce: vino nuovo, castagne e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove di San Martino.")
NWORDS = len(MODELO.split())
f.bridge(f"Письменное задание (без единственного ответа); образец текста ({NWORDS} слов) ниже.")
f.ex("B1", "Письмо", "(открытое задание — образец ниже)", f"Образец — в разделе H этой страницы ({NWORDS} слов)",
     "«La tua settimana di San Martino» Scrivi 80–100 parole: San Martino, cosa assaggi, un evento o una festa del tuo weekend.", instr="Письмо", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, GOLD, 2)
p.text(MX, 1382, "RISPOSTE · ОТВЕТЫ — по страницам: ищите по номеру задачи", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "К каждой задаче — пояснение · ✓ — задание с образцом", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 14, "sans", True, OLIVE, lh=1.14, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Письмо":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 12.5, lh=1.12, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-valutazione.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
