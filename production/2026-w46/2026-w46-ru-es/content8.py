# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ru-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ · TEST Y RESPUESTAS", "Lucerna", "PÁGINA 8 · El gran test de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Opción múltiple", "A", "Lunes 9 de noviembre",
     "Обычная неделя начинается ___ ноября. (A. 9 · B. 10)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "10 de noviembre — Día de la Policía",
     "День полиции — ___ ноября. (A. 9 · B. 10)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Día de las rebajas: 11 de noviembre",
     "День распродажи 11.11 — ___ ноября. (A. 11 · B. 12)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Jueves contra Uzbekistán",
     "Сборная России играет с ___. (A. Узбекистаном · B. Венесуэлой)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Resultados de la jornada 14 desconocidos al cierre",
     "Итоги 14-го тура на момент сдачи номера ___. (A. неизвестны · B. известны)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Jornada 15 el 20 de noviembre",
     "15-й тур будет ___ ноября. (A. 20 · B. 15)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Lilia se estrena el 12 de noviembre",
     "Фильм «Лиля» выходит ___ ноября. (A. 13 · B. 12)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Un código promocional es un código de descuento.",
     "Промокод — это код со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.head("B · ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Opción múltiple", "B", "10 de noviembre — Día de la Policía",
     "Когда День полиции? A. 9 ноября · B. 10 ноября · C. 11 ноября", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "5 días laborables en la semana",
     "Сколько рабочих дней на этой неделе? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Opción múltiple", "B", "10 días libres en noviembre",
     "Сколько выходных и праздничных дней в ноябре? A. 20 · B. 10 · C. 5", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Las rebajas empezaron el 22 de octubre",
     "Когда началась распродажа 11.11 на Ozon? A. 22 октября · B. 9 ноября · C. 12 ноября", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Meteorólogos: posible nieve húmeda",
     "Что обещают синоптики? A. Жаркое лето · B. Первый мокрый снег · C. Устойчивый снег", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "A", "El Spartak ganó al Lokomotiv 4-0",
     "Кто победил в матче «Спартак» — «Локомотив»? A. «Спартак» 4:0 · B. «Локомотив» · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Jornada 13: CSKA 0-0 Orenburg",
     "Как сыграли ЦСКА и «Оренбург»? A. 0:0 · B. 4:0 · C. 1:2", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "Un paquete debe rastrearse, recogerse y revisarse",
     "Что надо сделать с посылкой? A. Выбросить · B. Отследить, получить и проверить · C. Вернуть в кино", size=13.8, gap=0)
f.head("C · ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в школе в Москве. На этой неделе у неё обычная неделя: пять учебных дней и никаких праздников. В среду, 11 ноября, Маша заказывает книгу на распродаже 11.11. В четверг она получает посылку в пункте выдачи и проверяет книгу. А в субботу Маша идёт в кино с друзьями: они смотрят фильм «Лиля».", 15, lh=1.3, split=False)
f.ex("A2", "Opción múltiple", "B", "La semana de Masha es una semana normal",
     "Какая неделя у Маши? A. Каникулы · B. Обычная неделя · C. Экзамены", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "El miércoles pide un libro",
     "Что Маша заказывает в среду? A. Билет в кино · B. Книгу · C. Промокод", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "El jueves recoge un paquete en el punto de recogida",
     "Где Маша получает посылку? A. В кино · B. В пункте выдачи · C. В школе", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "El sábado ve Lilia con una amiga",
     "Куда Маша идёт в субботу? A. В школу · B. В кино с друзьями · C. На ярмарку", size=13.8, gap=0)
f.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Frases", "В среду Маша заказывает книгу.", "Sujeto + verbo + objeto",
     "в среду / Маша / заказывает книгу → ___", instr="Frases", size=13.8, gap=0)
f.ex("A2", "Frases", "В четверг она получает посылку.", "Sujeto + verbo + objeto",
     "в четверг / она / получает посылку → ___", instr="Frases", size=13.8, gap=0)
f.ex("B1", "Frases", "В субботу Маша идёт в кино.", "El tiempo primero, el verbo en segundo lugar",
     "в субботу / Маша / идёт в кино → ___", instr="Frases", size=13.8, gap=0)
f.ex("B1", "Frases", "Сначала составьте список покупок.", "Imperativo + objeto",
     "сначала / составьте / список покупок → ___", instr="Frases", size=13.8, gap=0)
f.head("E · ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Traducción", "Martes 10 de noviembre — Día de la Policía.", "Compara la página 2",
     "Во вторник, 10 ноября, — День полиции. → ___", instr="Traducir al español", size=13.8, gap=0)
f.ex("B1", "Traducción", "Un paquete debe rastrearse, recogerse y revisarse.", "Compara la página 5",
     "Посылку нужно отследить, получить и проверить. → ___", instr="Traducir al español", size=13.8, gap=0)
f.ex("B1", "Traducción", "El jueves Rusia juega contra Uzbekistán.", "Atención: играть + с + instrumental",
     "В четверг сборная России играет с Узбекистаном. → ___", instr="Traducir al español", size=13.8, gap=0)
f.ex("B2", "Traducción", "¡Feliz Día de la Policía a todos!", "поздравляю + с + instrumental",
     "Поздравляю с Днём полиции! → ___", instr="Traducir al español", size=13.8, gap=0)
f.head("F · СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Emparejamiento",
            ["предзимье", "посылка", "пик", "гололедица"],
            ["самое большое число заказов",
             "лёд на дороге",
             "время между осенью и зимой",
             "товар, который прислали по почте"],
            ["c", "d", "a", "b"],
            ["preinvierno c", "paquete d", "pico a", "el hielo en la calzada b"],
            instr="Empareja")
f.head("G · ДИАЛОГ В ПУНКТЕ ВЫДАЧИ", 21, OLIVE, 5)
f.ex("B1", "Opción múltiple", "A", "Recoger un paquete: номер заказа",
     "— Здравствуйте! Я пришла за посылкой. Вот ___ заказа. (A. номер · B. пик)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "El paquete ha llegado",
     "— Да, ваша посылка уже ___. (A. ушла · B. пришла)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Por favor, revise el paquete",
     "— Проверьте ___, пожалуйста. (A. посылку · B. промокод)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Todo está bien",
     "— Всё в порядке, спасибо! Книга ___. (A. целая · B. мокрая)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Felices compras",
     "— Спасибо! Хороших ___! (A. скидок · B. покупок)", size=13.8, gap=0)
f.head("H · НАПИШИТЕ САМИ", 21, OLIVE, 5)
MODELO = ("Моя обычная неделя в ноябре начинается в понедельник, 9 ноября. "
          "В понедельник и во вторник я работаю, а вечером читаю книгу. "
          "Во вторник, 10 ноября, я поздравляю знакомого полицейского с Днём полиции. "
          "В среду, 11 ноября, — день распродажи 11.11: я заказываю книгу и проверяю промокод. "
          "В четверг я получаю посылку и проверяю покупку. "
          "В пятницу вечером я иду в кино с друзьями. "
          "В субботу я высыпаюсь и гуляю в парке, а в воскресенье готовлюсь к новой неделе. "
          "Обычная неделя мне нравится: ровный ритм — это хорошо!")
NWORDS = len(MODELO.split())
f.bridge(f"Redacción (sin respuesta única); texto modelo ({NWORDS} palabras) abajo.")
f.ex("B1", "Redacción", "(Pregunta abierta, texto modelo abajo)", f"Véase el texto modelo en la sección H de esta página ({NWORDS} palabras)",
     "«Моя обычная неделя в ноябре» Напишите 80–100 слов: что вы будете делать каждый день недели?", instr="Redacción", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ОТВЕТЫ · SOLUCIONES — ORDENADAS POR PÁGINA; BUSCA EL NÚMERO DE EJERCICIO", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Cada respuesta con una breve nota en español · ✓ = texto modelo", 19.5, "sans", False, GREY, anchor="end")
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
