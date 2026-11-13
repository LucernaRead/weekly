# -*- coding: utf-8 -*-
# W47 ES core (VOL.4) — P5 first vote / P6 deep read. Fresh text, structure mirrors W46.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JUVENTUD (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUVENTUD　Молодёжь", "La Lucerna", "NIVEL B1　Votar por primera vez　Голосовать впервые")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Votar por primera vez: el jueves 19 se cierra el plazo", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: B1")
f.para("¿Votas por primera vez el 29 de noviembre? Tienes dos maneras de votar: en persona o por correo.")
f.para("El voto por correo se pide desde la convocatoria y hasta el jueves 19 de noviembre, en cualquier oficina de Correos o por internet, en la web de Correos. La Oficina del Censo Electoral envía la documentación a la dirección indicada a partir del lunes 9 de noviembre. Después, votas en casa, con calma, y envías el sobre.")
f.para("Y si prefieres votar en persona, el domingo 29 los colegios electorales abren de 9:00 a 20:00, con tu documento de identidad. Novedad de este año: también vale identificarse con la aplicación oficial MiDNI en el móvil. La Junta Electoral Central levantó el 5 de noviembre la suspensión de la aplicación.")
f.para("Y el sábado 28, jornada de reflexión, no hay propaganda ni actos de campaña: un día de silencio antes de votar. Y el viernes 27, la otra cita joven de la semana: el Black Friday, con ofertas en las tiendas y en internet. Compra con cabeza: compara precios antes de pagar.")
f.box("EL PLAN DE LA SEMANA　План", [
    ("1. El lunes 16: Día del Flamenco y primer lunes de campaña (понедельник: День фламенко и первый понедельник кампании)", "serif", False, INK, 21, 1.36),
    ("2. El jueves 19: último día para pedir el voto por correo (четверг: последний день заявки на голосование по почте)", "serif", False, INK, 21, 1.36),
    ("3. El viernes 20: vuelve la Liga, Athletic–Espanyol, 21:00 (вечер пятницы: Лига возвращается)", "serif", False, INK, 21, 1.36),
    ("4. El sábado 21: derbi Sevilla–Betis, 18:30 (суббота: севильское дерби)", "serif", False, INK, 21, 1.36),
    ("5. El domingo 22: Barça–Villarreal, 14:00; Santa Cecilia (воскресенье: «Барса» — «Вильярреал»; день святой Цецилии)", "serif", False, INK, 21, 1.36),
])
f.gloss("el sobre = конверт · la papeleta = бюллетень · el censo = список избирателей · el plazo = срок · la urna = урна для голосования.")
f.end_report()

# col 3: ballot-box photo + facts + ¿Y tú?
ix = COLX[3]
image(p, "urna_small.jpg", ix, 200, CW, 520)
cy3 = caption(p, ix, 720, CW, "Una urna de votación en bronce, con la inscripción «Suffrage universel» (sufragio universal). Tu voto va a una urna como esta: por correo llega en un sobre y en persona la echas tú mismo el domingo 29, de 9:00 a 20:00.",
              "Foto: Jebulon — CC0 (dominio público, Wikimedia Commons)")
facts = ["El voto por correo se pide hasta el jueves 19: en Correos o por internet.",
         "Para votar en persona vale el DNI y también la aplicación oficial MiDNI.",
         "El Black Friday es el viernes 27: compara precios antes de pagar."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "VOTAR POR PRIMERA VEZ", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Votarías por correo o en persona? ¿Qué comprarías en el Black Friday: algo útil o un capricho? Escribe dos frases en español."
ru_tu = "Вы голосовали бы по почте или лично? Что бы вы купили в «чёрную пятницу»: что-то полезное или каприз? Напишите два предложения и пришлите их."
# F1 fix (2026-11-13): pure geometry — tighten this box so its bottom clears the
# EJERCICIOS divider at y=1608. Old eh=356.0 put the box bottom at 1633.55
# (25.55px past the line). New leading/gaps save 34.56px: title->body gap
# 52->46, ES lh 1.42->1.38, ES->RU gap 10->2, RU first-line offset 20->12,
# RU lh 1.42->1.30. Text and font sizes unchanged. eh is derived from the
# same drawing offsets below, so the formula cannot drift from the drawing:
# top pad 16, title baseline +26, gap 46, ES first +21, ES step 21.5*1.38,
# ES para return adds one step, gap 2, RU first +12, RU step 19*1.30,
# bottom pad 7 below the last baseline.
es_n = len(wrap(etvous, "serif", False, 21.5, CW - 44))
ru_n = len(wrap(ru_tu, "sans", False, 19, CW - 44))
es_first = 16 + 46 + 21
ru_first = es_first + es_n * 21.5 * 1.38 + 2 + 12
ru_last = ru_first + (ru_n - 1) * 19 * 1.30
eh = ru_last + 7
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　А вы?", 24, "sans", True, OLIVE)
yy3 += 46
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.38) + 2
p.para(ix + 22, yy3 + 12, ru_tu, 19, "sans", False, GREY, CW - 44, 1.30)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　Упражнения страницы 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8　Уровни перемешаны — ищите по номеру задания", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　COMPRENSIÓN", 25)
e.bridge("Прочитайте статью на странице 5 и выберите правильный ответ.")
e.ex("B1", "Выбор ответа", "B", "Заявка на голосование по почте — до 19-го",
     "El voto por correo se pide hasta... A. el lunes 9 · B. el jueves 19 · C. el domingo 29", size=20, gap=8)
e.ex("B1", "Выбор ответа", "A", "Документы отправляются с 9 ноября",
     "La documentación del voto por correo llega desde... A. el lunes 9 · B. el viernes 13 · C. el sábado 28", size=20, gap=8)
e.ex("B1", "Выбор ответа", "C", "Избирательные участки работают с 9:00 до 20:00",
     "El domingo 29, los colegios abren... A. todo el día · B. de noche · C. de 9:00 a 20:00", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "MiDNI — новый способ подтвердить личность",
     "Para votar en persona, este año también vale... A. un billete · B. la aplicación MiDNI · C. una entrada", size=20, gap=8)
e.ex("B1", "Выбор ответа", "A", "«Чёрная пятница», пятница, 27 ноября",
     "El Black Friday es el... A. viernes 27 · B. lunes 16 · C. domingo 29", size=20, gap=8)
e.head("B　PALABRAS DEL TEXTO", 25)
e.bridge("Вставьте слова из рамки. Внимание: некоторые слова нужно проспрягать.")
e.para("sobre · papeleta · censo · identidad · plazo · urna", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Дополните предложение", "correo", "correo = почта / почтовый",
     "Pido el voto por ___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "papeleta", "papeleta = бюллетень",
     "En casa, relleno la ___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "envío", "enviar в спряжении → envío",
     "Después ___ (инфинитив: enviar) el sobre.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "identidad", "identidad = удостоверение личности",
     "Para votar en persona llevo mi documento de ___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "censo", "censo = список избирателей",
     "La Oficina del ___ envía la documentación.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "plazo", "plazo = срок (19-е)",
     "El jueves 19 termina el ___ del voto por correo.", instr="Вставьте", size=20, gap=8)
e.head("C　IR A + INFINITIVO", 25)
e.bridge("Перепишите предложения с ir a + инфинитив (ближайшее будущее).")
e.ex("B1", "Преобразуйте предложение", "Voy a pedir el voto por correo.", "voy a + инфинитив",
     "Pido el voto por correo. → ___", instr="Перепишите", size=20, gap=8)
e.ex("B1", "Преобразуйте предложение", "Vas a votar el domingo 29.", "vas a + инфинитив",
     "Votas el domingo 29. → ___", instr="Перепишите", size=20, gap=8)
e.ex("B1", "Преобразуйте предложение", "Va a abrirse la urna a las 9:00.", "va a + инфинитив",
     "La urna se abre a las 9:00. → ___", instr="Перепишите", size=20, gap=8)
e.ex("B1", "Преобразуйте предложение", "Van a comparar precios antes de pagar.", "van a + инфинитив",
     "Comparan precios antes de pagar. → ___", instr="Перепишите", size=20, gap=8)
e.head("D　¿VERDADERO O FALSO?", 25)
e.ex("B1", "Верно или неверно", "Verdadero", "Голосование по почте — через Correos",
     "El voto por correo se pide en una oficina de Correos. ¿Verdadero o falso?", instr="В/НВ", size=20, gap=8)
e.ex("B1", "Верно или неверно", "Falso", "День тишины — суббота, 28-е, а не воскресенье",
     "La jornada de reflexión es el domingo 29. ¿Verdadero o falso?", instr="В/НВ", size=20, gap=8)
e.ex("B1", "Верно или неверно", "Verdadero", "В этом году можно голосовать с MiDNI",
     "Este año se puede votar identificándose con MiDNI. ¿Verdadero o falso?", instr="В/НВ", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-juventud.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · A FONDO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("A FONDO　Разбор", "La Lucerna", "NIVEL B2　Leer la campaña: debates, programas y encuestas　Читать кампанию: дебаты, программы и опросы")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P6-main")
f.title("Leer la campaña: debates, programas y encuestas", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: B2　La política nacional española")
f.para("En campaña, no todo lo que se anuncia está cerrado.")
f.para("Al cierre de esta edición, el 10 de noviembre, solo hay un debate cerrado: el de portavoces de laSexta, el viernes 13 a las 21:30, con Ana Pastor. Van Carlos Cuerpo (PSOE), Juan Bravo (PP), Pablo Bustinduy (Frente Amplio) y José María Figaredo (Vox), a hablar de economía, con público en el plató.")
f.para("El debate de vivienda en la Cadena SER, el miércoles 18, ya está acordado (Rodríguez–Bravo), pero no se había publicado la hora al cierre de esta edición: acordado no es cerrado. El PP propone un cara a cara entre Sánchez y Feijóo para el lunes 16, y un debate a cuatro para el jueves 26; el lunes 9, PSOE y PP acuerdan que la Academia de Televisión organice los dos debates, pero las fechas, las horas y los participantes siguen sin cerrarse. Atresmedia convoca su propio debate a cuatro para el lunes 23, sin el PSOE confirmado. RTVE propone un debate a ocho, con los portavoces de los ocho grupos, para el lunes 23. Un debate «propuesto» no es un debate «cerrado»: la primera lección de esta página es leer el verbo.")
f.para("Una encuesta es una foto con margen de error, tomada en un día concreto.")
f.para("Y ojo con el calendario: del martes 24 al sábado 28 no se pueden publicar encuestas, y el sábado 28 es la jornada de reflexión. Hay poco tiempo de campaña y poco tiempo de silencio: el domingo 29, la única encuesta que no admite error: la votación, con papeletas de verdad.")
f.para("Leer un debate es fácil si preguntas tres cosas: ¿quién habla, de qué tema y con qué datos? El que promete sin datos promete humo.")
f.end_report()

# col 3: timeline + poll-reading box (sequential, measured)
bx = COLX[3]
steps = [
    "13 NOV. — Empieza la campaña; debate de portavoces en laSexta, 21:30.",
    "16 NOV. — El PP propone el cara a cara Sánchez–Feijóo (sin confirmar).",
    "18 NOV. — Debate sobre vivienda en la Cadena SER (Rodríguez–Bravo).",
    "19 NOV. — Termina el plazo para pedir el voto por correo.",
    "23 NOV. — Atresmedia convoca un debate a cuatro (sin el PSOE confirmado).",
    "23 NOV. — RTVE propone un debate a ocho, con los portavoces de los ocho grupos.",
    "24–28 NOV. — Prohibido publicar encuestas.",
    "26 NOV. — El PP propone un debate a cuatro de la Academia (sin fecha pactada).",
    "27 NOV. — Termina la campaña; el 28, jornada de reflexión.",
    "29 NOV. — España vota, de 9:00 a 20:00.",
]
tl_h = 68 + sum(len(wrap(t, "serif", False, 19, CW - 44)) * 19 * 1.35 + 29 for t in steps) + 20
p.rect(bx, 200, CW, tl_h, fill=BOX)
yy3 = 200 + 16
p.text(bx + 22, yy3 + 26, "EL CAMINO AL 29N", 24, "sans", True, OLIVE)
yy3 += 52
for t in steps:
    yy3 = p.para(bx + 22, yy3 + 19, t, 19, "serif", False, INK, CW - 44, 1.35) + 10
tl_end = 200 + tl_h
by3 = tl_end + 26
bb = ("Para leer cualquier debate, pregunta tres cosas: ¿quién habla? "
      "¿De qué tema? ¿Con qué datos? "
      "Sin esas tres respuestas, una promesa no dice casi nada.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f0eee5")
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LEER UN DEBATE", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh, "timeline box height", tl_h)

# ---- bar charts (RTVE free slots, JEC — honestly captioned) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, OLIVE, 2)
p.text(MX, gy + 10, "LOS MINUTOS GRATIS EN RTVE　minutos de propaganda por partido", 26, "sans", True, OLIVE)
rtve = [("PSOE", 45), ("PP", 45), ("Vox", 30), ("Frente Amplio", 30), ("Podemos", 15)]
bx1, bw_, bhh = MX, 2 * CW + GUT, 322
p.rect(bx1, gy + 28, bw_, bhh, fill=BOX)
p.text(bx1 + 22, gy + 68, "PROPAGANDA GRATIS EN RTVE　minutos", 21, "sans", True, INK)
yy = gy + 96
for lab, v in rtve:
    p.text(bx1 + 22, yy + 24, lab, 21, "serif", True, INK)
    p.rect(bx1 + 430, yy + 6, v * 6.4, 22, fill=OLIVE)
    p.text(bx1 + 448 + v * 6.4, yy + 24, f"{v} min", 20.5, "serif", False, INK)
    yy += 31
p.para(bx1 + 22, gy + bhh - 30, "Acuerdo de la Junta Electoral Central del 4 de noviembre: 195 minutos en total, del 13 al 27 de noviembre. Tres formaciones más tienen 10 minutos cada una: Frente Obrero, PCTE y SALF.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right column: the poll ban
rx = COLX[2]
p.rect(rx, gy + 28, 2 * CW + GUT, bhh, fill="#f0eee5")
p.text(rx + 22, gy + 68, "¿POR QUÉ NO HAY ENCUESTAS?", 21, "sans", True, INK)
yy = gy + 96
for lab, v in [("Prohibido publicar encuestas", 5), ("Días de campaña en total", 15), ("Días de silencio (reflexión)", 1)]:
    p.text(rx + 22, yy + 24, lab, 21, "serif", True, INK)
    p.rect(rx + 430, yy + 6, v * 6.4, 22, fill=OLIVE)
    p.text(rx + 448 + v * 6.4, yy + 24, f"{v}", 20.5, "serif", False, INK)
    yy += 31
p.para(rx + 22, gy + bhh - 30, "Del martes 24 al sábado 28 de noviembre no se pueden publicar encuestas. El sábado 28 es la jornada de reflexión: sin propaganda ni actos de campaña.", 17.5, "sans", False, GREY, 2 * CW + GUT - 44, 1.3)

# ---- P6 exercises ----
ey = 1940
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　Упражнения страницы 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8　Уровни перемешаны — ищите по номеру задания", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEER LOS GRÁFICOS", 25)
e.bridge("Посмотрите на графики и выберите правильный ответ.")
e.ex("B2", "Выбор ответа", "A", "По 45 бесплатных минут у PSOE и PP",
     "El PSOE y el PP tienen en RTVE... A. 45 minutos · B. 30 minutos · C. 15 minutos", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "B", "Всего 195 минут бесплатного эфира",
     "La propaganda gratuita en RTVE suma... A. 120 minutos · B. 195 minutos · C. 45 minutos", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "C", "Podemos: 15 минут",
     "Podemos tiene en RTVE... A. 45 minutos · B. 30 minutos · C. 15 minutos", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "A", "5 дней без публикации опросов (24–28 ноября)",
     "Prohibido publicar encuestas durante... A. 5 días · B. 15 días · C. 1 día", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "B", "45 − 30 = 15",
     "Entre el PSOE y Vox hay... A. 30 minutos · B. 15 minutos · C. 45 minutos", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "C", "Только бесплатный эфир, с источником",
     "La Lucerna publica aquí... A. una media mezclada · B. todos los sondeos · C. solo datos oficiales, con fuente", size=18.5, gap=2)
e.head("B　COMPRENSIÓN", 25)
e.ex("B2", "Выбор ответа", "B", "На 10 ноября подтверждены только дебаты laSexta",
     "El único debate cerrado es... A. el cara a cara · B. el de laSexta · C. el debate a cuatro", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "A", "Дебаты laSexta, пятница, 13 ноября, в 21:30",
     "El debate de portavoces es el... A. viernes 13, a las 21:30 · B. lunes 16 · C. jueves 26", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "C", "«Предложено» — не значит «подтверждено»",
     "Un debate «propuesto» es... A. cerrado · B. en la tele · C. aún sin confirmar", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "B", "Опрос: фото с погрешностью на один день",
     "Según el texto, una encuesta es... A. un resultado final · B. una foto con margen de error · C. una promesa", size=18.5, gap=2)
e.head("C　EL SUBJUNTIVO", 25)
e.ex("B2", "Дополните предложение", "tenga", "es posible que + сослагательное: tenga",
     "Es posible que el debate ___ (tener) cuatro portavoces.", instr="Вставьте", size=18.5, gap=2)
e.ex("B2", "Дополните предложение", "sea", "es importante que + сослагательное: sea",
     "Es importante que cada dato ___ (ser) claro.", instr="Вставьте", size=18.5, gap=2)
e.ex("B2", "Дополните предложение", "para que", "para que + сослагательное (цель)",
     "Publicamos la fuente ___ todos puedan comprobarla.", instr="Вставьте", size=18.5, gap=2)
e.ex("B2", "Дополните предложение", "Aunque", "Aunque + изъявительное (известный факт)",
     "___ los debates difieren, ninguno miente.", instr="Вставьте", size=18.5, gap=2)
e.head("D　PALABRAS DEL DEBATE", 25)
e.bridge("Вставьте слова из рамки: sondeo · muestra · indecisos · margen de error")
e.ex("B2", "Дополните предложение", "sondeo", "sondeo = опрос",
     "Un ___ pregunta a una muestra de ciudadanos.", instr="Вставьте", size=18.5, gap=2)
e.ex("B2", "Дополните предложение", "muestra", "muestra = выборка",
     "El sondeo preguntó a una ___ de ciudadanos.", instr="Вставьте", size=18.5, gap=2)
e.ex("B2", "Дополните предложение", "indecisos", "indecisos = неопределившиеся",
     "Los ___ todavía no saben a quién votar.", instr="Вставьте", size=18.5, gap=2)
e.ex("B2", "Дополните предложение", "margen de error", "margen de error = погрешность",
     "Toda encuesta tiene un ___.", instr="Вставьте", size=18.5, gap=2)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-afondo.svg")
print("P6 saved, exercises so far:", len(REG))
