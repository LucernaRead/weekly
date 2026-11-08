# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P5 youth / P6 deep read. Fresh text, structure mirrors W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JUVENTUD (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUVENTUD　Молодёжь", "La Lucerna", "NIVEL B1　Votar desde casa　Голосование из дома")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Votar desde casa: el voto por correo", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: B1")
f.para("No hace falta ir al colegio electoral para votar: el voto por correo llega a casa.")
f.para("El voto por correo se pide desde la convocatoria y hasta el jueves 19 de noviembre, en cualquier oficina de Correos o por internet, en la web de Correos. La Oficina del Censo Electoral envía la documentación a la dirección indicada a partir del lunes 9 de noviembre. Después, votas en casa, con calma, y envías el sobre.")
f.para("Y si prefieres votar en persona, el domingo 29 los colegios electorales abren de 9:00 a 20:00, con tu documento de identidad. El sábado 28, jornada de reflexión, no hay propaganda ni actos de campaña: un día de silencio antes de votar.")
f.para("Y el viernes 13, la otra cita de la semana joven: llega a HBO Max «Infamia», un thriller español de seis episodios con Susana Abaitua, que adapta la novela de la escritora gallega Ledicia Costas. La serie tuvo su estreno mundial en el festival de series de Cádiz.")
f.box("EL PLAN DE LA SEMANA　План", tsize=20, paras=[
    ("1. El lunes 9: llega la documentación del voto por correo a casa (понедельник: документы для голосования по почте отправлены)", "serif", False, INK, 21, 1.36),
    ("2. El miércoles 11: huelga general de 24 horas (среда: 24-часовая всеобщая забастовка)", "serif", False, INK, 21, 1.36),
    ("3. El jueves 12: Chequia–España, 20:45, en Praga (четверг вечером: Чехия — Испания)", "serif", False, INK, 21, 1.36),
    ("4. El viernes 13: empieza la campaña; se estrena «Infamia» (пятница: начало кампании; премьера «Infamia»)", "serif", False, INK, 21, 1.36),
    ("5. Y el domingo 15: España–Inglaterra, 20:45, en el Metropolitano (воскресенье: Испания — Англия)", "serif", False, INK, 21, 1.36),
])
f.gloss("el sobre = конверт · la papeleta = бюллетень · el censo = список избирателей · la jornada de reflexión = день тишины.")
f.end_report()

# col 3: typographic plate + facts + ¿Y tú?
ix = COLX[3]
p.rect(ix, 200, CW, 290, fill=CLOTH)
p.text(ix + CW / 2, 300, "INFAMIA", 54, "sans", True, ONCLOTH, anchor="middle")
p.text(ix + CW / 2, 352, "VIERNES 13　HBO MAX", 24, "sans", True, GOOSE, anchor="middle")
p.text(ix + CW / 2, 404, "Seis episodios　Susana Abaitua", 21, "serif", False, "#cac8ba", anchor="middle")
p.text(ix + CW / 2, 444, "Novela de Ledicia Costas", 21, "serif", False, "#cac8ba", anchor="middle")
cy3 = caption(p, ix, 490, CW, "«Infamia», el thriller español del viernes 13: una abogada obsesionada con una desaparición de hace veinte años. El domingo 15, la otra pantalla: la Roja contra Inglaterra.",
              "Placa tipográfica: La Lucerna")
facts = ["El voto por correo se pide hasta el jueves 19: en Correos o por internet.",
         "La documentación llega a casa a partir del lunes 9 de noviembre.",
         "«Infamia» se estrena el viernes 13: seis episodios, en HBO Max."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "VOTAR DESDE CASA", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Votarías por correo o en persona? ¿Qué serie ves esta semana: «Infamia» o el fútbol? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Вы голосуете по почте или идёте лично? Что смотрите на этой неделе: «Infamia» или футбол? Напишите два предложения и пришлите.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　А вы?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Вы голосуете по почте или идёте лично? Что смотрите на этой неделе: «Infamia» или футбол? Напишите два предложения и пришлите.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　Упражнения страницы 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8　Уровни перемешаны — ищите по номеру задания", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　COMPRENSIÓN", 25)
e.expl("Прочитайте статью на странице 5 и выберите правильный ответ.")
e.ex("B1", "Выбор ответа", "B", "Голосование по почте нужно запросить до 19-го числа",
     "El voto por correo se pide hasta... A. el lunes 9 · B. el jueves 19 · C. el domingo 29", size=20, gap=8)
e.ex("B1", "Выбор ответа", "A", "Документы отправляются с 9 ноября",
     "La documentación del voto por correo llega desde... A. el lunes 9 · B. el viernes 13 · C. el sábado 28", size=20, gap=8)
e.ex("B1", "Выбор ответа", "C", "Избирательные участки работают с 9:00 до 20:00",
     "El domingo 29, los colegios abren... A. todo el día · B. de noche · C. de 9:00 a 20:00", size=20, gap=8)
e.ex("B1", "Выбор ответа", "B", "В «Infamia» 6 серий",
     "«Infamia» tiene... A. dos episodios · B. seis episodios · C. veinte episodios", size=20, gap=8)
e.ex("B1", "Выбор ответа", "A", "В день тишины нет агитации",
     "El sábado 28, jornada de reflexión, no hay... A. propaganda ni actos · B. fútbol · C. series", size=20, gap=8)
e.head("B　PALABRAS DEL TEXTO", 25)
e.expl("Вставьте слова из рамки. Внимание: некоторые слова нужно проспрягать.")
e.para("sobre · papeleta · censo · identidad · reflexión · correo", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Дополните предложение", "correo", "correo = почта / почтовый",
     "Pido el voto por ___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "papeleta", "papeleta = бюллетень",
     "En casa, relleno la ___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "envío", "enviar в спряжении → envío",
     "Después ___ (инфинитив enviar) el sobre.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "identidad", "documento de identidad = документ, удостоверяющий личность",
     "Para votar en persona llevo mi documento de ___.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "censo", "censo = список избирателей",
     "La Oficina del ___ envía la documentación.", instr="Вставьте", size=20, gap=8)
e.ex("B1", "Дополните предложение", "reflexión", "jornada de reflexión = день тишины",
     "El sábado 28 es la jornada de ___.", instr="Вставьте", size=20, gap=8)
e.head("C　IR A + INFINITIVO", 25)
e.expl("Перепишите предложения с ir a + инфинитив (ближайшее будущее).")
e.ex("B1", "Преобразуйте предложение", "Voy a pedir el voto por correo.", "voy a + инфинитив",
     "Pido el voto por correo. → ___", instr="Перепишите", size=20, gap=8)
e.ex("B1", "Преобразуйте предложение", "Va a estrenarse «Infamia».", "va a + инфинитив",
     "Se estrena «Infamia». → ___", instr="Перепишите", size=20, gap=8)
e.ex("B1", "Преобразуйте предложение", "Vas a ver el España–Inglaterra.", "vas a + инфинитив",
     "Ves el España–Inglaterra. → ___", instr="Перепишите", size=20, gap=8)
e.ex("B1", "Преобразуйте предложение", "Van a votar el domingo 29.", "van a + инфинитив",
     "Votan el domingo 29. → ___", instr="Перепишите", size=20, gap=8)
e.head("D　¿VERDADERO O FALSO?", 25)
e.ex("B1", "Верно или неверно", "Verdadero", "Голосование по почте запрашивается в Correos",
     "El voto por correo se pide en una oficina de Correos. ¿Verdadero o falso?", instr="В/НВ", size=20, gap=8)
e.ex("B1", "Верно или неверно", "Falso", "День тишины — суббота, 28-е, а не воскресенье",
     "La jornada de reflexión es el domingo 29. ¿Verdadero o falso?", instr="В/НВ", size=20, gap=8)
e.ex("B1", "Верно или неверно", "Verdadero", "«Infamia» — экранизация романа Ледисии Костас",
     "«Infamia» adapta una novela de Ledicia Costas. ¿Verdadero o falso?", instr="В/НВ", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-juventud.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · A FONDO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("A FONDO　Разбор", "La Lucerna", "NIVEL B2　La vivienda decide la campaña　Жильё решает кампанию")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P6-main")
f.title("La vivienda decide la campaña", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: B2　La política nacional española")
f.para("La vivienda preocupa al 86,9 % de los españoles.")
f.para("Ese dato es del Barómetro de Vivienda 2026 del CIS, el instituto público de encuestas: estudio número 3532, con 6.019 entrevistas, un margen de error de ±1,3 puntos, publicado el 8 de octubre. Es la primera vez que el CIS dedica un estudio monográfico a la vivienda.")
f.para("El barómetro pregunta por soluciones, y las respuestas son claras: el 91,4 % cree que las administraciones deberían construir más vivienda pública, y el 76,3 % defiende que el Estado intervenga en el mercado «tanto como sea necesario». El 79 % quiere que la vivienda se trate como un derecho constitucional, frente al 13,5 % que la ve como un bien de mercado.")
f.para("Una encuesta es una foto con margen de error, tomada en un día concreto.")
f.para("Y mientras tanto, la campaña ya tiene su calendario: el miércoles 11, huelga general; el viernes 13 empieza la campaña; el jueves 19 termina el plazo del voto por correo; el viernes 27 termina la campaña; y el domingo 29, la única encuesta que no admite error: la votación, con papeletas de verdad.")
f.para("El 28 de octubre, un grave accidente ferroviario en Urda (Toledo) detuvo la precampaña unos días. La investigación sigue abierta: esta página no adelanta conclusiones.")
f.end_report()

# col 3: timeline + poll-reading box (sequential, measured)
bx = COLX[3]
steps = [
    "2 OCT. — El Congreso rechaza dos decretos de vivienda.",
    "5 OCT. — Sánchez disuelve las Cortes; elecciones el 29-N.",
    "6 OCT. — El decreto de convocatoria sale en el BOE.",
    "21–26 OCT. — Se presentan las candidaturas.",
    "28 OCT. — Grave accidente en Urda: la precampaña se detiene.",
    "3 NOV. — El BOE difunde las candidaturas proclamadas.",
    "9 NOV. — La documentación del voto por correo llega a casa.",
    "11 NOV. — Huelga general de 24 horas.",
    "13 NOV. — Empieza la campaña electoral.",
    "19 NOV. — Termina el plazo para pedir el voto por correo.",
    "27 NOV. — Termina la campaña; el 29, España vota.",
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
bb = ("Para leer cualquier encuesta, pregunta tres cosas: ¿quién la publica? "
      "¿Cuándo se hizo el trabajo de campo? ¿Qué margen de error tiene? "
      "Sin esas tres respuestas, un porcentaje no dice casi nada.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f0eee5")
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LEER UNA ENCUESTA", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh, "timeline box height", tl_h)

# ---- bar charts (CIS Barómetro de Vivienda 2026, honestly captioned) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, OLIVE, 2)
p.text(MX, gy + 10, "EL BARÓMETRO DE VIVIENDA DEL CIS　% que apoya cada medida", 26, "sans", True, OLIVE)
cis = [("1ª vivienda: menos impuestos", 95.4), ("Más vivienda pública", 91.4), ("Empresa pública de vivienda", 76.3), ("Limitar pisos turísticos", 75.6), ("Congelar alquileres 2 años", 70.6)]
bx1, bw_, bhh = MX, 2 * CW + GUT, 322
p.rect(bx1, gy + 28, bw_, bhh, fill=BOX)
p.text(bx1 + 22, gy + 68, "BARÓMETRO DE VIVIENDA (CIS)　apoyo a cada medida, %", 21, "sans", True, INK)
yy = gy + 96
for lab, v in cis:
    p.text(bx1 + 22, yy + 24, lab, 21, "serif", True, INK)
    p.rect(bx1 + 430, yy + 6, v * 3.2, 22, fill=OLIVE)
    p.text(bx1 + 448 + v * 3.2, yy + 24, f"{v:.1f}".replace(".", ",") + " %", 20.5, "serif", False, INK)
    yy += 31
p.para(bx1 + 22, gy + bhh - 30, "CIS, instituto público · estudio 3532 · 6.019 entrevistas · margen ±1,3 puntos · publicado el 8 de octubre. Solo se publica esta serie, con su fuente y su fecha.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right column: housing as a right
rx = COLX[2]
p.rect(rx, gy + 28, 2 * CW + GUT, bhh, fill="#f0eee5")
p.text(rx + 22, gy + 68, "LA VIVIENDA: ¿DERECHO O MERCADO?", 21, "sans", True, INK)
yy = gy + 96
for lab, v in [("Preocupados por la vivienda", 86.9), ("Derecho constitucional", 79.0), ("Bien de mercado", 13.5)]:
    p.text(rx + 22, yy + 24, lab, 21, "serif", True, INK)
    p.rect(rx + 430, yy + 6, v * 3.2, 22, fill=OLIVE)
    p.text(rx + 448 + v * 3.2, yy + 24, f"{v:.1f}".replace(".", ",") + " %", 20.5, "serif", False, INK)
    yy += 31
p.para(rx + 22, gy + bhh - 30, "Según el mismo barómetro: el 86,9 % está preocupado por la vivienda; el 79 % la ve como un derecho constitucional y solo el 13,5 % como un bien de mercado.", 17.5, "sans", False, GREY, 2 * CW + GUT - 44, 1.3)

# ---- P6 exercises ----
ey = 1940
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　Упражнения страницы 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8　Уровни перемешаны — ищите по номеру задания", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEER LOS GRÁFICOS", 25)
e.expl("Посмотрите на графики и выберите правильный ответ.")
e.ex("B2", "Выбор ответа", "A", "Снижение налогов — самая большая поддержка (95,4%)",
     "La medida con más apoyo es... A. bajar impuestos a la 1ª vivienda · B. limitar pisos turísticos · C. congelar alquileres", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "B", "Больше государственного жилья: поддержка 91,4%",
     "Construir más vivienda pública lo apoya el... A. 76,3 % · B. 91,4 % · C. 70,6 %", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "C", "Обеспокоены жильём: 86,9%",
     "Está preocupado por la vivienda el... A. 13,5 % · B. 79 % · C. 86,9 %", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "A", "Опрос: 6 019 респондентов, погрешность ±1,3",
     "El barómetro se hizo con... A. 6.019 entrevistas · B. 5.025 entrevistas · C. 3532 entrevistas", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "B", "95,4 − 91,4 = 4,0",
     "Entre la medida más apoyada y la segunda hay... A. 19,1 puntos · B. 4,0 puntos · C. 24,8 puntos", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "C", "Газета публикует только жилищную серию CIS, с источником и датой",
     "La Lucerna publica aquí... A. una media mezclada · B. todos los sondeos · C. solo la serie del CIS, con fuente y fecha", size=18.5, gap=2)
e.head("B　COMPRENSIÓN", 25)
e.ex("B2", "Выбор ответа", "B", "2 октября Конгресс отклонил два жилищных указа",
     "El 2 de octubre, el Congreso... A. aprobó dos decretos · B. rechazó dos decretos de vivienda · C. disolvió las Cortes", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "A", "5 октября Санчес распустил Кортесы и назначил выборы",
     "El 5 de octubre, Sánchez... A. disolvió las Cortes y convocó elecciones · B. publicó las listas · C. empezó la campaña", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "C", "Опрос — это фото с погрешностью, сделанное в конкретный день",
     "Según el texto, una encuesta es... A. un resultado final · B. una promesa · C. una foto con margen de error", size=18.5, gap=2)
e.ex("B2", "Выбор ответа", "B", "Кампания начинается 13 ноября",
     "La campaña electoral empieza el... A. 3 de noviembre · B. 13 de noviembre · C. 29 de noviembre", size=18.5, gap=2)
e.head("C　EL SUBJUNTIVO", 25)
e.ex("B2", "Дополните предложение", "tenga", "es posible que + сослагательное: tenga",
     "Es posible que el CIS ___ (tener) otro método.", instr="Вставьте", size=18.5, gap=2)
e.ex("B2", "Дополните предложение", "sea", "es importante que + сослагательное: sea",
     "Es importante que cada gráfico ___ (ser) claro.", instr="Вставьте", size=18.5, gap=2)
e.ex("B2", "Дополните предложение", "para que", "para que + сослагательное (цель)",
     "Publicamos la fuente ___ todos puedan comprobarla.", instr="Вставьте", size=18.5, gap=2)
e.ex("B2", "Дополните предложение", "Aunque", "Aunque + изъявительное (известный факт)",
     "___ las encuestas difieren, ninguna miente.", instr="Вставьте", size=18.5, gap=2)
e.head("D　PALABRAS DEL DEBATE", 25)
e.expl("Вставьте слова из рамки: sondeo · muestra · indecisos · margen de error")
e.ex("B2", "Дополните предложение", "sondeo", "sondeo = опрос",
     "Un ___ pregunta a una muestra de ciudadanos.", instr="Вставьте", size=18.5, gap=2)
e.ex("B2", "Дополните предложение", "muestra", "muestra = выборка (6 019 человек)",
     "El CIS entrevistó a una ___ de 6.019 personas.", instr="Вставьте", size=18.5, gap=2)
e.ex("B2", "Дополните предложение", "indecisos", "indecisos = неопределившиеся",
     "Los ___ todavía no saben a quién votar.", instr="Вставьте", size=18.5, gap=2)
e.ex("B2", "Дополните предложение", "margen de error", "margen de error = погрешность",
     "Toda encuesta tiene un ___.", instr="Вставьте", size=18.5, gap=2)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-afondo.svg")
print("P6 saved, exercises so far:", len(REG))
