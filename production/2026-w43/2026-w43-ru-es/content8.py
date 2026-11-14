# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ　Test y respuestas", "Lucerna", "PÁGINA 8　Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "La primera nieve: del 21 al 23",
     "Первый снег в Москве ждут 21–23 ___. (A. октября · B. ноября)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Las vacaciones empiezan el 24 de octubre",
     "Каникулы начинаются в субботу ___ октября. (A. 24 · B. 26)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "El Día del Liceísta es el 19 de octubre",
     "День лицеиста — ___ октября. (A. 19 · B. 18)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Cuatro cuentos",
     "В четверг в кино выходят ___ сказки. (A. три · B. четыре)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "El derbi es el domingo",
     "Дерби ЦСКА — «Спартак» будет в ___. (A. воскресенье · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "La entrada cuesta 900 rublos",
     "Билет на UNDR Halloween стоит ___ рублей. (A. 900 · B. 500)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "El Día de la Unidad Nacional es el 4 de noviembre",
     "4 ноября — День народного ___. (A. единства · B. отца)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Los neumáticos se cambian a +5…+7 grados",
     "Резину меняют при температуре плюс пять — ___ градусов. (A. семь · B. десять)", size=13.8, gap=0)
f.head("B　ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Opción múltiple", "A", "El Día del Padre fue el 18 de octubre",
     "Когда был День отца? A. 18 октября · B. 19 октября · C. 28 октября", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "Abrió en 1811, hace 215 años",
     "Сколько лет назад открылся лицей? A. 200 · B. 215 · C. 100", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "C", "El Zenit tiene 24 puntos",
     "У какой команды 24 очка? A. «Динамо» · B. «Спартак» · C. «Зенит»", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "La jornada 12 empieza el viernes",
     "Когда начинается 12-й тур? A. в пятницу, 23 октября · B. в воскресенье · C. в понедельник", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "El concurso va desde el 1 de octubre",
     "Конкурс костюмов в Reels идёт с... A. 1 октября · B. 22 октября · C. 31 октября", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "El Día de los Abuelos es el 28 de octubre",
     "Когда День бабушек и дедушек? A. 25 октября · B. 28 октября · C. 4 ноября", size=13.8, gap=0)
f.ex("B2", "Opción múltiple", "A", "Las vacaciones recomendadas terminan el 3 de noviembre",
     "Каникулы по рекомендации министерства заканчиваются... A. 3 ноября · B. 4 ноября · C. 26 октября", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Cierran la temporada de la dacha",
     "Что делают дачники в конце октября? A. открывают сезон · B. закрывают дачный сезон · C. покупают дачу", size=13.8, gap=0)
f.head("C　ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Антон учится в школе в Москве. На этой неделе он каждый день смотрит прогноз погоды: он очень ждёт первый снег. В пятницу у Антона последний учебный день, а в субботу начинаются каникулы. В воскресенье он будет смотреть дерби с папой: они болеют за «Спартак». А в четверг Антон пойдёт с классом в кино — на новую сказку.", 15, lh=1.3, split=False)
f.ex("A2", "Opción múltiple", "B", "Antón mira el pronóstico del tiempo",
     "Что Антон смотрит каждый день? A. телевизор · B. прогноз погоды · C. таблицу", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "Su último día de clase es el viernes",
     "Когда у Антона последний учебный день? A. в четверг · B. в пятницу · C. в субботу", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "C", "Animan al Spartak",
     "За кого болеют Антон и его папа? A. за ЦСКА · B. за «Динамо» · C. за «Спартак»", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "El jueves va al cine",
     "Куда Антон пойдёт в четверг? A. в кино · B. на дачу · C. на футбол", size=13.8, gap=0)
f.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Frases", "Первый снег может выпасть на этой неделе.", "Sujeto + grupo verbal + tiempo",
     "первый снег / может выпасть / на этой неделе → ___", instr="Formar la frase", size=13.8, gap=0)
f.ex("A2", "Frases", "Мы ждём первый снег.", "Sujeto + verbo + complemento",
     "мы / ждём / первый снег → ___", instr="Formar la frase", size=13.8, gap=0)
f.ex("B1", "Frases", "В воскресенье будет главное дерби.", "Primero el tiempo, el verbo en segundo lugar",
     "в воскресенье / будет / главное дерби → ___", instr="Formar la frase", size=13.8, gap=0)
f.ex("B1", "Frases", "Ученики отдыхают двенадцать дней.", "Sujeto + verbo + duración",
     "ученики / отдыхают / двенадцать дней → ___", instr="Formar la frase", size=13.8, gap=0)
f.head("E　ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Traducción", "El domingo, el CSKA juega contra el Spartak.", "Compáralo con la página 4",
     "В воскресенье ЦСКА играет со «Спартаком». → ___", instr="Traducir al español", size=13.8, gap=0)
f.ex("B1", "Traducción", "Los meteorólogos prometen aguanieve para finales de octubre.", "мокрый снег = aguanieve",
     "Синоптики обещают мокрый снег в конце октября. → ___", instr="Traducir al español", size=13.8, gap=0)
f.ex("B1", "Traducción", "В субботу начинаются каникулы — всего двенадцать дней.", "Ojo al caso: двенадцать дней",
     "Las vacaciones empiezan el sábado: doce días en total. → ___", instr="Traducir al ruso", size=13.8, gap=0)
f.ex("B2", "Traducción", "Поздравляю папу с Днём отца!", "поздравляю + с + instrumental",
     "¡Felicito a papá por el Día del Padre! → ___", instr="Traducir al ruso", size=13.8, gap=0)
f.head("F　СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Emparejamiento",
            ["похолодает", "рекомендация", "единоличный лидер", "шиномонтаж"],
            ["место, где меняют резину на машине",
             "команда, которая одна на первом месте",
             "станет холодно",
             "совет, а не приказ"],
            ["c", "d", "b", "a"],
            ["hará más frío c", "una recomendación d", "el líder en solitario b", "el taller de neumáticos a"],
            instr="Relacionar")
f.head("G　ДИАЛОГ В КИНО", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "два билета = dos entradas",
     "— Здравствуйте! Два ___ на «Морозко», пожалуйста. (A. билета · B. костюма)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "El 22 es jueves",
     "— На какой день? — На ___, 22 октября. (A. четверг · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Es un cuento de hadas",
     "— Хорошо. А фильм для детей? — Да, это ___. (A. сказка · B. дерби)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "до встречи = hasta la vista",
     "— Спасибо! До ___ в четверг! (A. встречи · B. утра)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "хорошего просмотра = ¡que disfrutes la película!",
     "— До встречи! Хорошего ___! (A. фильма · B. просмотра)", size=13.8, gap=0)
f.head("H　НАПИШИТЕ САМИ", 21, OLIVE, 5)
MODELO = ("Мои каникулы начинаются в субботу, 24 октября, и длятся двенадцать дней. "
          "Сначала я буду спать долго и отдыхать дома. "
          "В воскресенье мы с папой будем смотреть дерби: ЦСКА играет со «Спартаком». "
          "В понедельник мы поедем к бабушке и дедушке в деревню: там уже холодно, и, может быть, будет первый снег. "
          "В среду, 28 октября, я поздравлю бабушку и дедушку с их праздником. "
          "А 31 октября я надену костюм и пойду на Хэллоуин с друзьями. "
          "Я очень жду эти дни! Вот такие каникулы!")
NWORDS = len(MODELO.split())
f.expl(f"Ejercicio de escritura (sin solución única); el texto modelo ({NWORDS} palabras) va a continuación.")
f.ex("B1", "Redacción", "(Pregunta abierta — texto modelo a continuación)", f"El texto modelo está en la sección H de esta página ({NWORDS} palabras)",
     "«Мои каникулы» Напишите 80–100 слов: когда начинаются ваши каникулы, что вы будете делать и куда поедете?", instr="Escribir", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ОТВЕТЫ =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ОТВЕТЫ　Respuestas — ordenadas por página: busca tu número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Cada respuesta lleva una breve nota en español　✓ = ejercicio con texto modelo", 19.5, "sans", False, GREY, anchor="end")
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
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model words:", NWORDS)
