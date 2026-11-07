# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ · Test y respuestas", "Lucerna", "PÁGINA 8 · Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "El 4 de noviembre es festivo",
     "Выходной посреди недели — ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "El 3 de noviembre es un día de trabajo más corto",
     "Короткий день — ___ ноября. (A. 2 · B. 3)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Las ofertas terminan el 12 de noviembre",
     "Распродажа 11.11 закончится ___ ноября. (A. 12 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "El partido destacado es el sábado",
     "Матч «Краснодар» — ЦСКА будет в ___. (A. субботу · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "El derbi terminó 2:0",
     "Дерби ЦСКА — «Спартак» закончилось со счётом ___. (A. 2:0 · B. 0:0)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "La jornada 15 será el 20 de noviembre",
     "15-й тур будет ___ ноября. (A. 20 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Vuelta al colegio el 5 de noviembre",
     "Школьники идут в школу ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Un código promocional es un código de descuento",
     "Промокод — это код со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.head("B · ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Opción múltiple", "B", "El 4 de noviembre es el Día de la Unidad Nacional",
     "Когда День народного единства? A. 2 ноября · B. 4 ноября · C. 5 ноября", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Con vacaciones jueves y viernes: 5 días seguidos libres",
     "Сколько дней отдыха подряд, если взять отпуск в четверг и в пятницу? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Opción múltiple", "B", "Días festivos: miércoles, sábado y domingo",
     "Сколько выходных дней в неделе 2–8 ноября? A. 2 · B. 3 · C. 4", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Las ofertas empezaron el 22 de octubre",
     "Когда началась распродажа 11.11? A. 22 октября · B. 2 ноября · C. 12 ноября", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Según la prensa comercial: los descuentos podrían ser menores",
     "Что пишет торговая пресса о скидках? A. Их будет больше · B. Их может быть меньше · C. Их не будет", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "A", "El ganador del derbi es el CSKA",
     "Кто победил в дерби? A. ЦСКА · B. «Спартак» · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "La jornada 13 termina el lunes",
     "Когда закрывается 13-й тур? A. 2 ноября · B. 6 ноября · C. 8 ноября", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "Un código promocional es un código de descuento",
     "Что такое промокод? A. Список · B. Код со скидкой · C. Магазин", size=13.8, gap=0)
f.head("C · ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в школе в Москве. На этой неделе у неё последние дни каникул: в среду, 4 ноября, — праздник, а в четверг — снова в школу. В среду Маша пойдёт на ярмарку с семьёй. А в субботу она будет смотреть футбол: «Краснодар» играет с ЦСКА. Маша болеет за «Краснодар».", 15, lh=1.3, split=False)
f.ex("A2", "Opción múltiple", "B", "Masha pasa los últimos días de vacaciones",
     "Что у Маши на этой неделе? A. Экзамены · B. Последние дни каникул · C. Новая школа", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "El miércoles, al mercado",
     "Куда Маша пойдёт в среду? A. В школу · B. На ярмарку · C. На футбол", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "Vuelta al colegio el jueves",
     "Когда Маша снова идёт в школу? A. В среду · B. В четверг · C. В субботу", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Masha es del Krasnodar",
     "За кого болеет Маша? A. За ЦСКА · B. За «Краснодар» · C. За «Спартак»", size=13.8, gap=0)
f.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Frases", "В четверг школьники идут в школу.", "Primero el tiempo, el verbo en segundo lugar",
     "в четверг / школьники / идут в школу → ___", instr="Frases", size=13.8, gap=0)
f.ex("A2", "Frases", "Мы берём отпуск в четверг и в пятницу.", "Sujeto + verbo + tiempo",
     "мы / берём отпуск / в четверг и в пятницу → ___", instr="Frases", size=13.8, gap=0)
f.ex("B1", "Frases", "В субботу будет главный матч тура.", "Primero el tiempo, el verbo en segundo lugar",
     "в субботу / будет / главный матч тура → ___", instr="Frases", size=13.8, gap=0)
f.ex("B1", "Frases", "Сначала составьте список покупок.", "Imperativo + objeto",
     "сначала / составьте / список покупок → ___", instr="Frases", size=13.8, gap=0)
f.head("E · ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Traducción", "El miércoles 4 de noviembre es festivo.", "Compáralo con la página 3",
     "В среду, 4 ноября, — выходной. → ___", instr="Traducir al español", size=13.8, gap=0)
f.ex("B1", "Traducción", "Un código promocional es un código de descuento.", "Compáralo con la página 5",
     "Промокод — это код со скидкой. → ___", instr="Traducir al español", size=13.8, gap=0)
f.ex("B1", "Traducción", "В субботу «Краснодар» играет с ЦСКА.", "Fíjate en: играть + с + instrumental",
     "El sábado, el Krasnodar juega contra el CSKA. → ___", instr="Traducir al ruso", size=13.8, gap=0)
f.ex("B2", "Traducción", "Поздравляю с Днём народного единства!", "поздравляю + с + instrumental",
     "¡Feliz Día de la Unidad Nacional para todos! → ___", instr="Traducir al ruso", size=13.8, gap=0)
f.head("F · СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Emparejamiento",
            ["выходной", "промокод", "пауза", "ярмарка"],
            ["код со скидкой",
             "место, где продают еду и подарки",
             "перерыв в чемпионате",
             "день, когда не работают"],
            ["d", "a", "c", "b"],
            ["Día festivo d", "Código promocional a", "Pausa c", "Feria b"],
            instr="Relacionar")
f.head("G · ДИАЛОГ В МАГАЗИНЕ", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "скидка = descuento",
     "— Здравствуйте! На эту куртку есть ___? (A. скидка · B. список)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "скидка 20%",
     "— Да, сегодня ___ 20%. (A. цена · B. скидка)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "у меня есть = tengo un código promocional",
     "— А у меня есть ___! (A. промокод · B. выходной)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "его = el código promocional (masculino)",
     "— Отлично! Введите ___ в приложении. (A. его · B. её)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "¡Felices compras!",
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
f.bridge(f"Ejercicio de redacción (sin una única respuesta); el texto modelo ({NWORDS} palabras) está abajo.")
f.ex("B1", "Redacción", "(Pregunta abierta — texto modelo a continuación)", f"El texto modelo está en la sección H de esta página ({NWORDS} palabras)",
     "«Моя неделя с праздником посреди недели» Напишите 80–100 слов: что вы будете делать в среду, в выходные и куда поедете?", instr="Redacción", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ОТВЕТЫ · Respuestas — ordenadas por página; busca tu número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Cada respuesta con una breve nota en español · ✓ = ejercicio de redacción", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Redacción":
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
