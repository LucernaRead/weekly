# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P8: 38 exercises + registry-generated answers. Dash style, as W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS · Упражнения и ответы", "La Lucerna", "Страница 8 · La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "Выбор в тексте", "B", "visita a Chequia = выезд в Чехию",
     "El jueves, la Roja ___ a Chequia en Praga. (A. recibe · B. visita)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "B", "recibir a Inglaterra = принимать Англию дома",
     "El domingo, España ___ a Inglaterra en Madrid. (A. visita · B. recibe)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "la lista = список вызванных",
     "De la Fuente dio ___ el viernes 6. (A. la lista · B. la huelga)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "B", "la huelga dura 24 horas = забастовка длится 24 часа",
     "La huelga del miércoles ___ 24 horas. (A. empieza · B. dura)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "empieza la campaña = кампания начинается",
     "El viernes 13 ___ la campaña electoral. (A. empieza · B. termina)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "B", "el sobre = конверт",
     "El voto por correo llega en un ___. (A. puente · B. sobre)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "Испания — Англия в воскресенье",
     "El domingo se juega el ___ en el Metropolitano. (A. España–Inglaterra · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "veranillo = бабье лето",
     "En noviembre llega el ___ de San Martín. (A. veranillo · B. puente)", size=15.5, gap=1)
f.head("B · PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "Выбор ответа", "B", "Всеобщая забастовка — в среду, 11 ноября",
     "La huelga general es el... A. lunes 9 · B. miércoles 11 · C. viernes 13", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "A", "День святого Мартина, 11 ноября",
     "San Martín es el... A. 11 de noviembre · B. 12 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "C", "Испания — Англия и забастовка — на этой неделе",
     "Esta semana hay... A. solo fútbol · B. solo huelga · C. la huelga y el España–Inglaterra", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "B", "На magosto едят жареные каштаны",
     "¿Qué se come en el magosto? A. flan · B. castañas asadas · C. chocolate", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "A", "Лозунг забастовки: зарплаты, жильё, цены",
     "El lema de la huelga es... A. «Salarios, vivienda y precios» · B. «Fútbol y fiesta» · C. «Cine y series»", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "C", "Выборы — 29 ноября",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "Выбор ответа", "B", "Жилищный барометр CIS: 86,9% обеспокоены",
     "Según el CIS de vivienda, está preocupado el... A. 13,5 % · B. 86,9 % · C. 79 %", size=15.5, gap=1)
f.ex("B1", "Выбор ответа", "A", "Кампания начинается 13 ноября",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C · LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el miércoles 11 sigue la huelga en las noticias y el domingo ve el España–Inglaterra en el Metropolitano. Ana vive en Barcelona: el miércoles 11 trabaja, y el domingo ve el partido por televisión. Los dos leen los programas antes de votar el 29.", 16.5, lh=1.3, split=False)
f.ex("A2", "Выбор ответа", "B", "Пабло идёт в воскресенье на «Метрополитано»",
     "¿Quién ve el partido en el Metropolitano? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "A", "Ана работает в среду",
     "El miércoles 11, Ana... A. trabaja · B. va a la huelga · C. duerme", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "A", "Оба читают программы перед голосованием",
     "Antes de votar, los dos... A. leen los programas · B. ven «Infamia» · C. viajan a Praga", size=15.5, gap=1)
f.ex("A2", "Выбор ответа", "B", "Заголовок обобщает контраст двух мест",
     "El mejor título es... A. «Una tormenta» · B. «Dos miércoles» · C. «El Clásico»", size=15.5, gap=1)
f.head("D · CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "Составьте предложение", "El miércoles hay huelga general.", "Подлежащее + глагол + место",
     "el miércoles / hay / huelga general → ___", instr="Составьте предложение", size=15.5, gap=1)
f.ex("A2", "Составьте предложение", "El domingo vemos el España–Inglaterra.", "Время впереди",
     "el domingo / vemos / el España–Inglaterra → ___", instr="Составьте предложение", size=15.5, gap=1)
f.ex("B1", "Составьте предложение", "La campaña empieza a las cero horas.", "a las cero horas = в полночь",
     "la campaña / empieza / a las cero horas → ___", instr="Составьте предложение", size=15.5, gap=1)
f.ex("B1", "Составьте предложение", "¿A qué hora empieza el partido?", "Вопросительное слово в начале",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="Составьте предложение", size=15.5, gap=1)
f.head("E · TRADUCE", 22, OLIVE, 5)
f.ex("A2", "Перевод", "В среду по всей Испании всеобщая забастовка.", "Сверьтесь с оригиналом.",
     "El miércoles hay huelga general en toda España. → ___", instr="Перевод", size=15.5, gap=1)
f.ex("A2", "Перевод", "В воскресенье мы смотрим Испания — Англия.", "Сверьтесь с оригиналом.",
     "El domingo vemos el España–Inglaterra. → ___", instr="Перевод", size=15.5, gap=1)
f.ex("B1", "Перевод", "El voto por correo llega a casa.", "llegar a casa = приходить домой",
     "Голосование по почте приходит домой. → ___", instr="Перевод", size=15.5, gap=1)
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
            ["sondeo=опрос c", "muestra=выборка d", "margen de error=погрешность b", "junta electoral=избирательная комиссия a"],
            instr="Соотнесите")
f.head("G · DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "Выбор в тексте", "A", "alquiler = арендная плата",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "tres habitaciones = три комнаты",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "¿cuánto cuesta? = сколько стоит?",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "firmar = подписать (договор)",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "Выбор в тексте", "A", "mudanza = переезд",
     "— La ___ es el miércoles 11, día de huelga. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H · ESCRIBE TÚ", 22, OLIVE, 5)
f.expl("Письменное задание (без единственного ответа); образец (84 слова) — ниже.")
f.ex("B1", "Письмо", "(открытый вопрос — образец ниже)", "Образец — в разделе H этой страницы (84 слова)",
     "«¿Qué harías tú por la vivienda?» Escribe 80–100 palabras: tu plan del miércoles 11, tu domingo 15 y tu voto del 29.", instr="Письмо", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y el miércoles 11 sigo la huelga en las noticias: salarios, vivienda y precios, los tres temas de la semana. "
          "El viernes 13 empieza la campaña, y el domingo 15 veo el España–Inglaterra con mi familia. "
          "El jueves 12 veo el Chequia–España en Praga por televisión, a las 20:45. "
          "Mis amigos de Barcelona no tienen huelga en su empresa: el miércoles trabajan. Yo, en cambio, leo los programas con calma y preparo mi voto por correo. "
          "El 29 votamos. ¡Qué semana!")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPUESTAS · Ответы — по страницам, ищите по номеру", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "К каждому ответу — короткое пояснение · ✓ = задание с образцом", 19.5, "sans", False, GREY, anchor="end")
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
