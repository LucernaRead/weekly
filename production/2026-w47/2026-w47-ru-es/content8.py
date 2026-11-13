# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ　TEST Y RESPUESTAS", "Lucerna", "PÁGINA 8　Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Opción múltiple", "A", "Lunes 16 de noviembre",
     "Неделя 16–22 ноября начинается ___ ноября. (A. 16 · B. 17)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "17 de noviembre — Día del Estudiante",
     "День студента — ___ ноября. (A. 17 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "18 de noviembre — cumpleaños de Ded Moroz",
     "День рождения Деда Мороза — ___ ноября. (A. 17 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "El martes — contra Venezuela",
     "Сборная играет с Венесуэлой ___ ноября. (A. 17 · B. 12)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Cinco estrenos el 19 de noviembre",
     "Пять премьер выходят ___ ноября. (A. 19 · B. 26)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "La jornada 15 empieza el 20 de noviembre",
     "15-й тур начнётся ___ ноября. (A. 20 · B. 15)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "El Black Friday empieza el 16 de noviembre",
     "«Чёрная пятница» на Wildberries — с ___ ноября. (A. 16 · B. 27)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "El Cyber Monday es el 30 de noviembre",
     "«Киберпонедельник» будет ___ ноября. (A. 30 · B. 27)", size=13.8, gap=0)
f.head("B　ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Opción múltiple", "B", "17 de noviembre — Día del Estudiante",
     "Когда День студента? A. 16 ноября · B. 17 ноября · C. 18 ноября", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "5 días laborables en la semana",
     "Сколько рабочих дней на этой неделе? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Opción múltiple", "C", "Zenit y Dinamo tienen 31 puntos cada uno",
     "Сколько очков у «Зенита» и «Динамо»? A. 26 · B. 29 · C. 31", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Krasnodar ganó al CSKA 4:2",
     "Как сыграли «Краснодар» и ЦСКА? A. 4:2 · B. 2:4 · C. 0:0", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Black Friday en Ozon: 13 de noviembre–2 de diciembre",
     "Когда «чёрная пятница» на Ozon? A. 13 ноября – 2 декабря · B. 16–30 ноября · C. 25–27 ноября", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Según los meteorólogos: lluvia con nieve mojada",
     "Что обещают синоптики? A. Жаркое лето · B. Дождь с мокрым снегом · C. Устойчивый снег", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "El Dinamo de Majachkalá ganó al Baltika 1:0",
     "Кто победил в матче «Балтика» — «Динамо» Мх? A. «Балтика» 1:0 · B. «Динамо» Мх 1:0 · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Un paquete debe rastrearse, recogerse y revisarse",
     "Что надо сделать с посылкой? A. Выбросить · B. Отследить, получить и проверить · C. Вернуть в кино", size=13.8, gap=0)
f.head("C　ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в университете в Москве. На этой неделе у неё обычная неделя: пять учебных дней и никаких праздников. Во вторник, 17 ноября, Маша поздравляет друга-студента с Днём студента. В четверг, 19 ноября, Маша идёт в кино с друзьями: они смотрят фильм «Рокки — это я». В пятницу Маша заказывает подарок на «чёрную пятницу». А в субботу Маша получает посылку в пункте выдачи и проверяет подарок.", 15, lh=1.3, split=False)
f.ex("A2", "Opción múltiple", "B", "Masha es estudiante universitaria",
     "Кто такая Маша? A. Школьница · B. Студентка · C. Учительница", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "Felicitar a un amigo estudiante el martes",
     "Кого Маша поздравляет во вторник? A. Деда Мороза · B. Друга-студента · C. Преподавателя", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "Ir al cine con amigos el jueves",
     "Куда Маша идёт в четверг? A. В университет · B. В кино с друзьями · C. На рынок", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Recoger el paquete en el punto de recogida el sábado",
     "Где Маша получает посылку? A. В кино · B. В пункте выдачи · C. В университете", size=13.8, gap=0)
f.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Frases", "Во вторник Маша поздравляет друга-студента.", "Sujeto + verbo + objeto",
     "во вторник / Маша / поздравляет друга-студента → ___", instr="Frases", size=13.8, gap=0)
f.ex("A2", "Frases", "В четверг Маша идёт в кино.", "Sujeto + verbo + objeto",
     "в четверг / Маша / идёт в кино → ___", instr="Frases", size=13.8, gap=0)
f.ex("B1", "Frases", "В пятницу Маша заказывает подарок.", "El tiempo primero, el verbo en segundo lugar",
     "в пятницу / Маша / заказывает подарок → ___", instr="Frases", size=13.8, gap=0)
f.ex("B1", "Frases", "Сначала составьте список покупок.", "Imperativo + objeto",
     "сначала / составьте / список покупок → ___", instr="Frases", size=13.8, gap=0)
f.head("E　ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Traducción", "Martes 17 de noviembre, Día del Estudiante.", "Ver página 2",
     "Во вторник, 17 ноября, — День студента. → ___", instr="Traducir al español", size=13.8, gap=0)
f.ex("B1", "Traducción", "Un paquete debe rastrearse, recogerse y revisarse.", "Ver página 5",
     "Посылку нужно отследить, получить и проверить. → ___", instr="Traducir al español", size=13.8, gap=0)
f.ex("B1", "Traducción", "El martes Rusia juega contra Venezuela.", "Atención: играть + с + instrumental",
     "Во вторник сборная России играет с Венесуэлой. → ___", instr="Traducir al español", size=13.8, gap=0)
f.ex("B2", "Traducción", "¡Feliz Día del Estudiante a todos!", "поздравляю + с + instrumental",
     "Поздравляю с Днём студента! → ___", instr="Traducir al español", size=13.8, gap=0)
f.head("F　СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Emparejamiento",
            ["оттепель", "распродажа", "счёт", "гололедица"],
            ["результат матча, например 2:2",
             "лёд на дороге",
             "тепло зимой: снег тает",
             "большая продажа со скидками"],
            ["c", "d", "a", "b"],
            ["Deshielo c", "Gran venta d", "Resultado a", "el hielo en la calzada b"],
            instr="Empareja")
f.head("G　ДИАЛОГ В МАГАЗИНЕ", 21, OLIVE, 5)
f.ex("B1", "Opción múltiple", "A", "Querer comprar un regalo en rebajas",
     "— Здравствуйте! Я хочу купить подарок со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Hoy es Black Friday",
     "— Да, сегодня у нас ___. (A. пятница · B. «чёрная пятница»)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Por favor, comprueba el código promocional",
     "— Проверьте ___, пожалуйста. (A. посылку · B. промокод)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "El regalo está intacto",
     "— Всё в порядке, спасибо! Подарок ___. (A. целый · B. мокрый)", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Felices compras",
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
f.bridge(f"Redacción (sin respuesta única); texto modelo ({NWORDS} palabras) abajo.")
f.ex("B1", "Redacción", "(Pregunta abierta, texto modelo abajo)", f"Véase el texto modelo en la sección H de esta página ({NWORDS} palabras)",
     "«Моя неделя 16–22 ноября» Напишите 80–100 слов: что вы будете делать каждый день недели?", instr="Redacción", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ОТВЕТЫ　SOLUCIONES — ORDENADAS POR PÁGINA; BUSCA EL NÚMERO DE EJERCICIO", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Cada respuesta con una breve nota en español　✓ = texto modelo", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Redacción":
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
