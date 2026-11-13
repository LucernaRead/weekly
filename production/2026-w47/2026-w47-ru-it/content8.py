# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ　TEST E RISPOSTE", "Lucerna", "PAGINA 8　Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Scelta multipla", "A", "Lunedì 16 novembre",
     "Неделя 16–22 ноября начинается ___ ноября. (A. 16 · B. 17)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "17 novembre — Giorno degli studenti",
     "День студента — ___ ноября. (A. 17 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "18 novembre — compleanno di Nonno Gelo",
     "День рождения Деда Мороза — ___ ноября. (A. 17 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Martedì — contro il Venezuela",
     "Сборная играет с Венесуэлой ___ ноября. (A. 17 · B. 12)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Cinque prime il 19 novembre",
     "Пять премьер выходят ___ ноября. (A. 19 · B. 26)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "La 15ª giornata inizia il 20 novembre",
     "15-й тур начнётся ___ ноября. (A. 20 · B. 15)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Il Black Friday inizia il 16 novembre",
     "«Чёрная пятница» на Wildberries — с ___ ноября. (A. 16 · B. 27)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Il Cyber Monday è il 30 novembre",
     "«Киберпонедельник» будет ___ ноября. (A. 30 · B. 27)", size=13.8, gap=0)
f.head("B　ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Scelta multipla", "B", "17 novembre — Giorno degli studenti",
     "Когда День студента? A. 16 ноября · B. 17 ноября · C. 18 ноября", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "5 giorni lavorativi nella settimana",
     "Сколько рабочих дней на этой неделе? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Scelta multipla", "C", "Zenit e Dinamo hanno 31 punti ciascuno",
     "Сколько очков у «Зенита» и «Динамо»? A. 26 · B. 29 · C. 31", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Il Krasnodar ha battuto il CSKA 4:2",
     "Как сыграли «Краснодар» и ЦСКА? A. 4:2 · B. 2:4 · C. 0:0", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Black Friday su Ozon: 13 novembre–2 dicembre",
     "Когда «чёрная пятница» на Ozon? A. 13 ноября – 2 декабря · B. 16–30 ноября · C. 25–27 ноября", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Secondo i meteorologi: pioggia con neve bagnata",
     "Что обещают синоптики? A. Жаркое лето · B. Дождь с мокрым снегом · C. Устойчивый снег", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "La Dinamo di Machačkala ha battuto il Baltika 1:0",
     "Кто победил в матче «Балтика» — «Динамо» Мх? A. «Балтика» 1:0 · B. «Динамо» Мх 1:0 · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Un pacco va tracciato, ritirato, controllato",
     "Что надо сделать с посылкой? A. Выбросить · B. Отследить, получить и проверить · C. Вернуть в кино", size=13.8, gap=0)
f.head("C　ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в университете в Москве. На этой неделе у неё обычная неделя: пять учебных дней и никаких праздников. Во вторник, 17 ноября, Маша поздравляет друга-студента с Днём студента. В четверг, 19 ноября, Маша идёт в кино с друзьями: они смотрят фильм «Рокки — это я». В пятницу Маша заказывает подарок на «чёрную пятницу». А в субботу Маша получает посылку в пункте выдачи и проверяет подарок.", 15, lh=1.3, split=False)
f.ex("A2", "Scelta multipla", "B", "Masha è una studentessa universitaria",
     "Кто такая Маша? A. Школьница · B. Студентка · C. Учительница", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Fare gli auguri a un amico studente martedì",
     "Кого Маша поздравляет во вторник? A. Деда Мороза · B. Друга-студента · C. Преподавателя", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "B", "Andare al cinema con gli amici giovedì",
     "Куда Маша идёт в четверг? A. В университет · B. В кино с друзьями · C. На рынок", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Ritirare il pacco al punto di ritiro sabato",
     "Где Маша получает посылку? A. В кино · B. В пункте выдачи · C. В университете", size=13.8, gap=0)
f.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Frasi", "Во вторник Маша поздравляет друга-студента.", "Soggetto + verbo + oggetto",
     "во вторник / Маша / поздравляет друга-студента → ___", instr="Frasi", size=13.8, gap=0)
f.ex("A2", "Frasi", "В четверг Маша идёт в кино.", "Soggetto + verbo + oggetto",
     "в четверг / Маша / идёт в кино → ___", instr="Frasi", size=13.8, gap=0)
f.ex("B1", "Frasi", "В пятницу Маша заказывает подарок.", "Il tempo prima, il verbo al secondo posto",
     "в пятницу / Маша / заказывает подарок → ___", instr="Frasi", size=13.8, gap=0)
f.ex("B1", "Frasi", "Сначала составьте список покупок.", "Imperativo + oggetto",
     "сначала / составьте / список покупок → ___", instr="Frasi", size=13.8, gap=0)
f.head("E　ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Traduzione", "Martedì 17 novembre, Giorno degli studenti.", "Vedi pagina 2",
     "Во вторник, 17 ноября, — День студента. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "Un pacco va tracciato, ritirato e controllato.", "Vedi pagina 5",
     "Посылку нужно отследить, получить и проверить. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B1", "Traduzione", "Martedì la Russia gioca contro il Venezuela.", "Attenzione: играть + с + strumentale",
     "Во вторник сборная России играет с Венесуэлой. → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.ex("B2", "Traduzione", "Buon Giorno degli studenti a tutti!", "поздравляю + с + strumentale",
     "Поздравляю с Днём студента! → ___", instr="Traduci in italiano", size=13.8, gap=0)
f.head("F　СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Abbinamento",
            ["оттепель", "распродажа", "счёт", "гололедица"],
            ["результат матча, например 2:2",
             "лёд на дороге",
             "тепло зимой: снег тает",
             "большая продажа со скидками"],
            ["c", "d", "a", "b"],
            ["Disgelo c", "Grande vendita d", "Risultato a", "il ghiaccio sulla strada b"],
            instr="Abbina")
f.head("G　ДИАЛОГ В МАГАЗИНЕ", 21, OLIVE, 5)
f.ex("B1", "Scelta multipla", "A", "Voler comprare un regalo in saldo",
     "— Здравствуйте! Я хочу купить подарок со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Oggi è il Black Friday",
     "— Да, сегодня у нас ___. (A. пятница · B. «чёрная пятница»)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Controlla il codice promozionale, per favore",
     "— Проверьте ___, пожалуйста. (A. посылку · B. промокод)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Il regalo è intatto",
     "— Всё в порядке, спасибо! Подарок ___. (A. целый · B. мокрый)", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Buoni acquisti",
     "— Спасибо! Хороших ___! (A. скидок · B. покупок)", size=13.8, gap=0)
f.head("H　НАПИШИТЕ САМИ", 21, OLIVE, 5)
MODELO = ("Моя неделя 16–22 ноября начинается в понедельник, 16 ноября. "
          "В понедельник я работаю, а вечером читаю книгу. "
          "Во вторник, 17 ноября, я поздравляю друга-студента с Днём студента. "
          "В среду я пишу письмо Деду Морозу: прошу снег и хорошую зиму. "
          "В четверг, 19 ноября, я иду в кино с друзьями: мы смотрим фильм «Рокки — это я». "
          "В пятницу вечером я проверяю промокоды и заказываю подарок на «чёрную пятницу». "
          "В субботу я получаю посылку, проверяю покупку и смотрю футбол: начинается 15-й тур! "
          "В воскресенье я отдыхаю, гуляю в парке и готовлюсь к новой неделе. "
          "Мне нравится такая неделя!")
NWORDS = len(MODELO.split())
f.bridge(f"Composizione (senza risposta unica); testo modello ({NWORDS} parole) sotto.")
f.ex("B1", "Composizione", "(Domanda aperta, testo modello qui sotto)", f"Vedi il testo modello nella sezione H di questa pagina ({NWORDS} parole)",
     "«Моя неделя 16–22 ноября» Напишите 80–100 слов: что вы будете делать каждый день недели?", instr="Composizione", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ОТВЕТЫ　SOLUZIONI — ORDINATE PER PAGINA; CERCA IL NUMERO DELL'ESERCIZIO", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Ogni risposta con una breve nota in italiano　✓ = testo modello", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Composizione":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.0, lh=1.13, gap=0.5, split=False)
af.end_report()
print("P8 keys end col", af.ci, "y", af.y)
# --- Morozko image in the free space below the keys (last column only) ---
img_y = af.y + 24
img_h = 250
if af.ci == 3 and img_y + img_h + 90 < 2560:
    image(p, "morozko.jpg", COLX[3], img_y, CW, img_h)
    cy8 = caption(p, COLX[3], img_y + img_h, CW, "«Морозко»: иллюстрация Ивана Билибина, 1932 год. Зимняя сказка — к ноябрю.",
                  "Иллюстрация: Иван Билибин — общественное достояние (Wikimedia Commons)")
    print("P8 morozko ends", cy8)
else:
    print("P8 morozko SKIPPED: no room (col", af.ci, "y", af.y, ")")
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model words:", NWORDS)
