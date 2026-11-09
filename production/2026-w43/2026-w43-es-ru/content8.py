# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS　Упражнения и ответы", "La Lucerna", "Страница 8　La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "Выбор в тексте", "B", "abrir el marcador = открыть счёт",
     "Doué ___ el marcador en París. (A. cerró · B. abrió)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "B", "poner el 1–1 = сравнять счёт",
     "Espart ___ el 1–1 para el Barça. (A. perdió · B. puso)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "de cabeza = головой",
     "Lucas Hernández marcó el 2–1 de ___. (A. cabeza · B. penalti)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "B", "volver a + инфинитив = снова …",
     "Yamal ___ a empatar: 2–2. (A. salió · B. volvió)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "B", "cerrar el partido = решить исход матча",
     "Vitinha y Fabián Ruiz ___ el 4–2 al final. (A. abrieron · B. cerraron)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "B", "derrota = поражение",
     "Fue la primera ___ del Barça este año. (A. victoria · B. derrota)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "в воскресенье играют Класико",
     "El domingo se juega el ___ en el Camp Nou. (A. Clásico · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "camiseta = футболка",
     "El Barça lleva una ___ de GOLF WANG. (A. camiseta · B. bufanda)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Выбор ответа", "B", "в воскресенье утром 03:00 станет 02:00",
     "El cambio: a las... A. 02→03 · B. 03→02 · C. 00→01", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "A", "на Канарах на час раньше",
     "¿Dónde hay una hora menos? A. Canarias · B. Madrid · C. Barcelona", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "C", "Класико и Ф1 — оба в 21:00",
     "El domingo, 21:00: hay... A. solo fútbol · B. solo coches · C. los dos", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "B", "на Кастаньяду едят panellets",
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "A", "Хэллоуин — в субботу 31 октября",
     "Halloween es... A. sáb. 31.10 · B. dom. 1.11 · C. lun. 2.11", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "C", "выборы — 29 ноября",
     "Las elecciones generales son el... A. 29.10 · B. 1.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "Выбор ответа", "B", "два ряда опросов нельзя смешивать",
     "¿Por qué no mezclamos las series? A. son secretas · B. métodos distintos · C. son viejas", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "A", "DANA Adam — первый именованный шторм сезона",
     "La DANA Adam es... A. la primera tormenta con nombre · B. una fiesta gallega · C. un equipo", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Lucía vive en Sevilla: el lunes 2 es festivo en Andalucía y hace puente. Marta vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El sábado por la noche, Marta celebra la Castanyada con sus amigos: castañas y panellets.", 16.5, lh=1.3, split=False)
f.ex("A2", "Выбор ответа", "B", "Андалусия — в списке выходных",
     "¿Quién hace puente? A. Marta · B. Lucía · C. las dos", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "A", "в Каталонии понедельник — рабочий день",
     "El lunes 2, Marta... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "C", "на Кастаньяду едят каштаны и panellets",
     "¿Qué comen Marta y sus amigos? A. flores · B. dulces de Halloween · C. castañas y panellets", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "B", "заголовок обобщает контраст двух мест",
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Составьте предложение", "El domingo dormimos una hora más.", "время — впереди",
     "el domingo / dormimos / una hora más → ___", instr="Составьте предложение", size=15.5, gap=1)
f.ex("A2", "Составьте предложение", "El lunes es festivo en Madrid.", "подлежащее + глагол",
     "el lunes / es festivo / en Madrid → ___", instr="Составьте предложение", size=15.5, gap=1)
f.ex("B1", "Составьте предложение", "El Clásico empieza a las nueve.", "a las nueve = в девять",
     "el Clásico / empieza / a las nueve → ___", instr="Составьте предложение", size=15.5, gap=1)
f.ex("B1", "Составьте предложение", "¿A qué hora empieza el partido?", "вопрос — в начале",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Составьте предложение", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Перевод", "В воскресенье мы спим на час дольше.", "см. текст",
     "El domingo dormimos una hora más. → ___", instr="Перевод", size=15.5, gap=1)
f.ex("A2", "Перевод", "Понедельник — выходной в 9 сообществах.", "см. текст",
     "El lunes es festivo en nueve comunidades. → ___", instr="Перевод", size=15.5, gap=1)
f.ex("B1", "Перевод", "El Clásico se juega el domingo a las nueve de la noche.", "se juega = играется",
     "Класико играют в воскресенье в девять вечера. → ___", instr="Перевод", size=15.5, gap=1)
f.ex("B2", "Перевод", "Cada gráfico tiene que llevar su fuente.", "tener que = нужно",
     "Каждый график должен указывать источник. → ___", instr="Перевод", size=15.5, gap=1)
f.head("F　LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "Соотнесите слова",
            ["el sondeo", "el indeciso", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "quien aún no sabe a quién votar"],
            ["c", "d", "b", "a"],
            ["sondeo = опрос c", "indeciso = неопределившийся d", "margen de error = погрешность b", "junta electoral = избирательная комиссия a"],
            instr="Соотнесите")
f.head("G　DIÁLOGO EN LA TIENDA", 22, OLIVE, 5)
f.ex("B1", "Выбор в тексте", "A", "disfraz = карнавальный костюм",
     "— Busco un ___ para mi hija. (A. disfraz · B. paraguas)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "Monster High популярен у детей",
     "— Le encanta ___. (A. Monster High · B. el Samaín)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "¿cuánto cuesta? = сколько стоит?",
     "— ¿Cuánto ___? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "pagar = платить",
     "— ¿Cómo va a ___: con tarjeta o en efectivo? (A. pagar · B. votar)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "Хэллоуин выпадает на субботу",
     "— Con tarjeta. La fiesta es el ___. (A. sábado · B. lunes)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.expl("Письменное задание (без единственного ответа); образец (82 слова) — ниже.")
f.ex("B1", "Письмо", "(открытый вопрос — образец ниже)", "образец — в разделе H этой страницы (82 слова)",
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del 31 y del 1, y tu lunes.", instr="Письмо", size=15.5, gap=1)
MODELO = ("Vivo en Valencia, y aquí el lunes 2 de noviembre no es festivo: trabajo como un lunes normal. "
          "Mis amigos de Madrid sí hacen puente, ¡qué suerte! El sábado 31 celebro Halloween con mi familia, "
          "y el domingo llevamos flores al cementerio, como cada año. Por la tarde leo un libro en el sofá "
          "y preparo la semana con calma. El lunes, mientras Madrid descansa, yo abro la tienda a las nueve. "
          "No es justo… pero en diciembre, seguro, llega mi puente.")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPUESTAS　Ответы — по страницам; ищите по номеру", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "К каждому ответу — короткое пояснение на русском　✓ — задание с образцом", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Письмо":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
