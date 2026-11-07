# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-es-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS · Упражнения и ответы", "La Lucerna", "Страница 8 · La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "Выбор в тексте", "B", "ganó 2–1 = победа 2–1",
     "El Madrid ___ 2–1 en el Camp Nou. (A. perdió · B. ganó)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "B", "marcar dos goles = забить два гола",
     "Mbappé ___ dos goles en Barcelona. (A. paró · B. marcó)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "primera derrota liguera = первое поражение в лиге",
     "Fue la primera ___ del Barça en la Liga. (A. derrota · B. victoria)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "B", "recortar = сократить отставание",
     "El Madrid ___ la distancia a tres puntos. (A. aumentó · B. recortó)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "acoger = принимать («Бернабеу» принимает NFL)",
     "El Bernabéu ___ un partido de la NFL. (A. acoge · B. cierra)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "B", "el emparrillado = поле для американского футбола",
     "El Bernabéu cambia el césped por el ___. (A. puente · B. emparrillado)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "в воскресенье — «Атлетико» — «Барса»",
     "El domingo se juega el ___ en el Metropolitano. (A. Atlético–Barça · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "himno = гимн",
     "Antes del partido suenan dos ___: el de España y el de EE. UU. (A. himnos · B. puentes)", size=15.5, gap=1)
f.head("B · PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Выбор ответа", "B", "в понедельник выходной в 9 сообществах",
     "El lunes 2 es fiesta en... A. todas · B. nueve comunidades · C. ninguna", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "A", "День всех святых — 1 ноября",
     "Todos los Santos es el... A. 1 de noviembre · B. 2 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "C", "«Атлетико» — «Барса» и NFL — в воскресенье",
     "El domingo 8 hay... A. solo fútbol · B. solo NFL · C. la NFL y el Atlético–Barça", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "B", "на Кастаньяду едят panellets",
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "A", "мероприятия памяти DANA — в четверг, 29 октября",
     "Los actos de memoria de la DANA fueron el... A. jueves 29 de octubre · B. sábado 31 · C. lunes 2", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "C", "выборы — 29 ноября",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "Выбор ответа", "B", "опрос CIS за октябрь: жильё — 55,7%",
     "Según el CIS de octubre, la vivienda es el principal problema para el... A. 20,9 % · B. 55,7 % · C. 17,1 %", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "A", "кампания начинается 13 ноября",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C · LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el lunes 2 es festivo en su comunidad y hace puente. Ana vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El domingo por la tarde, Ana ve la NFL en televisión; por la noche, Pablo ve el Atlético–Barça.", 16.5, lh=1.3, split=False)
f.ex("A2", "Выбор ответа", "B", "Мадрид — в списке выходного дня",
     "¿Quién hace puente? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "A", "в Каталонии понедельник — рабочий день",
     "El lunes 2, Ana... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "A", "Ana смотрит только NFL; «Атлетико» — «Барса» вечером смотрит Pablo",
     "El domingo, Ana ve... A. solo la NFL · B. solo el Barça · C. la NFL y, por la noche, el Atlético–Barça", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "B", "заголовок передаёт контраст двух городов",
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D · CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Составьте предложение", "El lunes es festivo en Madrid.", "подлежащее + глагол + место",
     "el lunes / es festivo / en Madrid → ___", instr="Составьте предложение", size=15.5, gap=1)
f.ex("A2", "Составьте предложение", "El domingo vemos la NFL en el Bernabéu.", "время — сначала",
     "el domingo / vemos / la NFL / en el Bernabéu → ___", instr="Составьте предложение", size=15.5, gap=1)
f.ex("B1", "Составьте предложение", "El Atlético–Barça empieza a las nueve.", "a las nueve = в девять часов",
     "el Atlético–Barça / empieza / a las nueve → ___", instr="Составьте предложение", size=15.5, gap=1)
f.ex("B1", "Составьте предложение", "¿A qué hora empieza el partido?", "вопросительное слово — в начале",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Составьте предложение", size=15.5, gap=1)
f.head("E · TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Перевод", "Понедельник — выходной в девяти сообществах.", "см. оригинал",
     "El lunes es festivo en nueve comunidades. → ___", instr="Перевод", size=15.5, gap=1)
f.ex("A2", "Перевод", "В воскресенье мы смотрим NFL и «Атлетико» — «Барса».", "см. оригинал",
     "El domingo vemos la NFL y el Atlético–Barça. → ___", instr="Перевод", size=15.5, gap=1)
f.ex("B1", "Перевод", "El Bernabéu acoge un partido de la NFL.", "acoger = принимать",
     "«Бернабеу» принимает матч NFL. → ___", instr="Перевод", size=15.5, gap=1)
f.ex("B2", "Перевод", "Cada gráfico tiene que llevar su fuente.", "tener que = должен",
     "Каждый график должен указывать источник. → ___", instr="Перевод", size=15.5, gap=1)
f.head("F · LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "Соотнесите слова",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo = опрос (c)", "muestra = выборка (d)", "margen de error = погрешность (b)", "junta electoral = избирательная комиссия (a)"],
            instr="Соотнесите")
f.head("G · DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "Выбор в тексте", "A", "alquiler = аренда",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "tres habitaciones = три комнаты",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "¿cuánto cuesta? = сколько стоит?",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "firmar = подписать (договор)",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "mudanza = переезд",
     "— La ___ es el lunes 2, que es fiesta. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H · ESCRIBE TÚ", 22, OLIVE, 5)
f.expl("Письменное задание (без единственного ответа); образец (84 слова) — ниже.")
f.ex("B1", "Письмо", "(открытый вопрос — образец ниже)", "образец — в разделе H этой страницы (84 слова)",
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del puente y tu domingo 8.", instr="Письмо", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y aquí el lunes 2 de noviembre sí es festivo: hago puente con mi familia. "
          "El sábado 7 vemos el Valencia–Real Madrid en televisión, y el domingo 8 tenemos dos citas: por la tarde, la NFL en el Bernabéu, y por la noche, el Atlético–Barça. "
          "Mis amigos de Barcelona no tienen puente: el lunes trabajan. Yo, en cambio, descanso un día más y preparo la semana con calma. "
          "El viernes 13 empieza la campaña, y el 29 votamos todos. ¡Qué mes!")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPUESTAS · Ответы — по страницам, ищите по номеру", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "К каждому заданию — короткое пояснение · ✓ — задание с образцом", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 14, "sans", True, OLIVE, lh=1.12, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Письмо":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.2, lh=1.12, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
