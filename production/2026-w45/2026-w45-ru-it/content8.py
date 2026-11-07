# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ · Test e risposte", "Lucerna", "PAGINA 8 · Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "Il 4 novembre è festa",
     "Выходной посреди недели — ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Il 3 novembre è una giornata corta",
     "Короткий день — ___ ноября. (A. 2 · B. 3)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Saldi fino al 12 novembre",
     "Распродажа 11.11 закончится ___ ноября. (A. 12 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "La partita più importante è sabato",
     "Матч «Краснодар» — ЦСКА будет в ___. (A. субботу · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Derby: 2-0",
     "Дерби ЦСКА — «Спартак» закончилось со счётом ___. (A. 2:0 · B. 0:0)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "La 15ª giornata è il 20 novembre",
     "15-й тур будет ___ ноября. (A. 20 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Si torna a scuola il 5 novembre",
     "Школьники идут в школу ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Il codice promozionale è un codice sconto",
     "Промокод — это код со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.head("B · ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Scelta multipla", "B", "Il 4 novembre è il Giorno dell'Unità Nazionale",
     "Когда День народного единства? A. 2 ноября · B. 4 ноября · C. 5 ноября", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Ferie giovedì e venerdì: 5 giorni liberi di fila",
     "Сколько дней отдыха подряд, если взять отпуск в четверг и в пятницу? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Scelta multipla", "B", "Giorni liberi: mercoledì, sabato, domenica",
     "Сколько выходных дней в неделе 2–8 ноября? A. 2 · B. 3 · C. 4", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "I saldi sono iniziati il 22 ottobre",
     "Когда началась распродажа 11.11? A. 22 октября · B. 2 ноября · C. 12 ноября", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Stampa commerciale: gli sconti potrebbero diminuire",
     "Что пишет торговая пресса о скидках? A. Их будет больше · B. Их может быть меньше · C. Их не будет", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "A", "Il derby lo vince il CSKA",
     "Кто победил в дерби? A. ЦСКА · B. «Спартак» · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "La 13ª giornata si chiude lunedì",
     "Когда закрывается 13-й тур? A. 2 ноября · B. 6 ноября · C. 8 ноября", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Il codice promozionale è un codice sconto",
     "Что такое промокод? A. Список · B. Код со скидкой · C. Магазин", size=13.8, gap=0)
f.head("C · ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в школе в Москве. На этой неделе у неё последние дни каникул: в среду, 4 ноября, — праздник, а в четверг — снова в школу. В среду Маша пойдёт на ярмарку с семьёй. А в субботу она будет смотреть футбол: «Краснодар» играет с ЦСКА. Маша болеет за «Краснодар».", 15, lh=1.3, split=False)
f.ex("A2", "Scelta multipla", "B", "Gli ultimi giorni di vacanza di Masha",
     "Что у Маши на этой неделе? A. Экзамены · B. Последние дни каникул · C. Новая школа", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Mercoledì alla fiera",
     "Куда Маша пойдёт в среду? A. В школу · B. На ярмарку · C. На футбол", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Si torna a scuola giovedì",
     "Когда Маша снова идёт в школу? A. В среду · B. В четверг · C. В субботу", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Masha tifa Krasnodar",
     "За кого болеет Маша? A. За ЦСКА · B. За «Краснодар» · C. За «Спартак»", size=13.8, gap=0)
f.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Frasi", "В четверг школьники идут в школу.", "Prima il tempo, poi il verbo",
     "в четверг / школьники / идут в школу → ___", instr="Frasi", size=13.8, gap=0)
f.ex("A2", "Frasi", "Мы берём отпуск в четверг и в пятницу.", "Soggetto + verbo + tempo",
     "мы / берём отпуск / в четверг и в пятницу → ___", instr="Frasi", size=13.8, gap=0)
f.ex("B1", "Frasi", "В субботу будет главный матч тура.", "Prima il tempo, poi il verbo",
     "в субботу / будет / главный матч тура → ___", instr="Frasi", size=13.8, gap=0)
f.ex("B1", "Frasi", "Сначала составьте список покупок.", "Imperativo + oggetto",
     "сначала / составьте / список покупок → ___", instr="Frasi", size=13.8, gap=0)
f.head("E · ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Traduzione", "Mercoledì 4 novembre è festa.", "Confronta pagina 3",
     "В среду, 4 ноября, — выходной. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "Il codice promozionale è un codice sconto.", "Confronta pagina 5",
     "Промокод — это код со скидкой. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "В субботу «Краснодар» играет с ЦСКА.", "Nota: играть + с + strumentale",
     "Sabato il Krasnodar gioca contro il CSKA. → ___", instr="Traduci in russo", size=13.8, gap=0)
f.ex("B2", "Traduzione", "Поздравляю с Днём народного единства!", "поздравляю + с + strumentale",
     "Auguri a tutti per il Giorno dell'Unità Nazionale! → ___", instr="Traduci in russo", size=13.8, gap=0)
f.head("F · СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Abbinamento",
            ["выходной", "промокод", "пауза", "ярмарка"],
            ["код со скидкой",
             "место, где продают еду и подарки",
             "перерыв в чемпионате",
             "день, когда не работают"],
            ["d", "a", "c", "b"],
            ["Giorno libero d", "Codice promozionale a", "Pausa c", "Fiera b"],
            instr="Abbina")
f.head("G · ДИАЛОГ В МАГАЗИНЕ", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "скидка = sconto",
     "— Здравствуйте! На эту куртку есть ___? (A. скидка · B. список)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "скидка 20%",
     "— Да, сегодня ___ 20%. (A. цена · B. скидка)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "у меня есть = ho un codice promozionale",
     "— А у меня есть ___! (A. промокод · B. выходной)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "его = il codice promozionale (maschile)",
     "— Отлично! Введите ___ в приложении. (A. его · B. её)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Buoni acquisti",
     "— Спасибо! Хороших ___! (A. скидок · B. покупок)", size=13.8, gap=0)
f.head("H · НАПИШИТЕ САМИ", 21, OLIVE, 5)
MODELO = ("Моя неделя с праздником посреди недели начинается в понедельник, 2 ноября. "
          "В понедельник и во вторник я работаю, а в среду, 4 ноября, — выходной. "
          "В среду я пойду на ярмарку с семьёй: куплю еду и подарки. "
          "В четверг и в пятницу я снова работаю, но вечером смотрю футбол. "
          "В субботу, 7 ноября, «Краснодар» играет с ЦСКА, и я буду болеть за «Краснодар». "
          "В воскресенье я отдохну дома и подготовлюсь к новой неделе. "
          "Такая неделя мне нравится: праздник посреди недели — как маленький подарок!")
NWORDS = len(MODELO.split())
f.bridge(f"Compito di scrittura (senza un'unica risposta); testo modello ({NWORDS} parole) sotto.")
f.ex("B1", "Composizione", "(Domanda aperta — testo modello qui sotto)", f"Testo modello nella sezione H di questa pagina ({NWORDS} parole)",
     "«Моя неделя с праздником посреди недели» Напишите 80–100 слов: что вы будете делать в среду, в выходные и куда поедете?", instr="Composizione", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ОТВЕТЫ · Risposte — in ordine di pagina: cerca il tuo numero", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Ogni risposta ha una breve nota in italiano · ✓ = esercizio con testo modello", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Composizione":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.0, lh=1.13, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model words:", NWORDS)
