# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ru-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · МОЛОДЁЖЬ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("МОЛОДЁЖЬ · Juventud", "Lucerna", "УРОВЕНЬ B1 · Хэллоуин и планы на каникулы · Halloween y los planes de vacaciones")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P5-feature")
f.title("Хэллоуин — 31 октября: Москва готовится", 37)
f.byline("От редакции Lucerna · Уровень чтения: B1")
f.para("В субботу, 31 октября, Москва празднует Хэллоуин. До праздника — ещё неделя, но подготовка уже идёт: молодые москвичи выбирают костюмы и покупают билеты. В этом году Хэллоуин — в субботу, и это удобно: на следующий день не надо рано вставать.")
f.para("Что будет в городе? Открытый фестиваль «Хиллоуин'26» в парке ужасов обещает парад костюмов. А конкурс костюмов в Reels идёт уже с 1 октября: участники показывают свои костюмы в коротких видео.")
f.para("Для тех, кто любит вечеринки, клуб Loft Hall делает ночь UNDR Halloween: 31 октября с 23:00 до 06:00. Билеты на странице события стоят 900 рублей — и их уже покупают.")
f.para("Подготовка идёт и дома: кто-то покупает готовый костюм, а кто-то делает его сам — из старой одежды, бумаги и красок. До субботы ещё есть время, но все хотят успеть: хороший костюм — половина праздника.")
f.gloss("костюмы los disfraces · парад el desfile · билеты las entradas.")
f.head("КАНИКУЛЫ + ХЭЛЛОУИН = ПЛАНЫ", 25)
f.para("Хэллоуин в этом году — внутри каникул: школьники отдыхают с 24 октября по 4 ноября. Поэтому планы простые: днём — гулять и смотреть новые сказки в кино, а 31 октября — праздник с друзьями.")
f.para("Не забудьте: в среду, 28 октября, — День бабушек и дедушек. Позвоните бабушке и дедушке или приедьте в гости. А в субботу вечером наденьте костюм: ведьма, вампир или привидение — что выберете вы?")
f.para("Социальные сети уже полны видео с костюмами: конкурс в Reels идёт с 1 октября, и участники каждую неделю показывают новые идеи. А вы уже выбрали костюм?")
f.gloss("привидение el fantasma · в гости = de visita (en casa de alguien)")
f.end_report()

# col 3: image + facts box
ix = COLX[3]
image(p, "pumpkins.jpg", ix, 200, CW, 280)
cy5 = caption(p, ix, 480, CW, "Тыквы — главный символ Хэллоуина. Из тыквы делают фонарь со страшной или смешной рожицей.",
              "Фото: Министерство сельского хозяйства США — общественное достояние")
facts = ["31 октября, суббота — Хэллоуин.",
         "UNDR Halloween в Loft Hall: ночь с 23:00 до 06:00, билеты — 900 рублей.",
         "Конкурс костюмов в Reels идёт с 1 октября.",
         "28 октября — День бабушек и дедушек."]
sy5 = cy5 + 24
sh5 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy5, CW, sh5, fill=BOX, stroke=LINE, sw=1.4)
yy5 = sy5 + 16
p.text(ix + 22, yy5 + 26, "ХЭЛЛОУИН В ЦИФРАХ", 24, "sans", True, OLIVE)
yy5 += 52
for t in facts:
    yy5 = p.para(ix + 22, yy5 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 ends", sy5 + sh5)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Ejercicios de la página 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8 · niveles mezclados: busca por el número de ejercicio", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.expl("Lee los textos de la página 5 y elige la respuesta correcta.")
e.ex("A2", "Opción múltiple", "B", "Halloween es el 31 de octubre",
     "Хэллоуин в 2026 году — ... A. 25 октября · B. 31 октября · C. 1 ноября", size=20, gap=8)
e.ex("A2", "Opción múltiple", "C", "El 31 de octubre es sábado",
     "31 октября — это... A. пятница · B. воскресенье · C. суббота", size=20, gap=8)
e.ex("B1", "Opción múltiple", "A", "El concurso de disfraces empezó el 1 de octubre",
     "Конкурс костюмов в Reels идёт... A. с 1 октября · B. с 25 октября · C. с 31 октября", size=20, gap=8)
e.ex("B1", "Opción múltiple", "B", "La entrada cuesta 900 rublos",
     "Билет на UNDR Halloween стоит... A. 500 рублей · B. 900 рублей · C. 100 рублей", size=20, gap=8)
e.ex("A2", "Opción múltiple", "A", "El Día de los Abuelos es el 28 de octubre",
     "День бабушек и дедушек — ... A. 28 октября · B. 24 октября · C. 4 ноября", size=20, gap=8)
e.head("B · СЛОВА НЕДЕЛИ", 25)
e.expl("Completa con las palabras de la página 5.")
e.ex("A2", "Completar", "костюмы", "костюмы = los disfraces",
     "Молодые москвичи выбирают ___ и покупают билеты.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "парад", "парад костюмов = el desfile de disfraces",
     "Фестиваль обещает ___ костюмов.", instr="Completar", size=20, gap=8)
e.ex("A2", "Completar", "23:00", "La fiesta empieza a las 23:00",
     "Вечеринка в Loft Hall начинается в ___ (время).", instr="Completar", size=20, gap=8)
e.ex("A2", "Completar", "бабушек", "День бабушек и дедушек",
     "28 октября — День ___ и дедушек.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "фонарь", "фонарь из тыквы = el farol de calabaza",
     "Из тыквы делают ___ со смешной рожицей.", instr="Completar", size=20, gap=8)
e.head("C · КОСТЮМЫ", 25)
e.match_set("B1", "Emparejamiento",
            ["ведьма", "вампир", "привидение", "тыква"],
            ["овощ — главный символ Хэллоуина",
             "женщина с метлой в сказках",
             "оно живёт в старом доме и пугает людей",
             "он пьёт кровь и боится солнца"],
            ["b", "d", "c", "a"],
            ["la bruja b", "el vampiro d", "el fantasma c", "la calabaza a"],
            instr="Relacionar")
e.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.expl("Forma frases correctas con las palabras dadas.")
e.ex("B1", "Frases", "Мы покупаем билеты на вечеринку.", "Verbo + complemento + dirección",
     "мы / покупаем / билеты / на вечеринку → ___", instr="Formar la frase", size=20, gap=8)
e.ex("A2", "Frases", "Конкурс костюмов идёт с первого октября.", "Sujeto + verbo + tiempo",
     "конкурс костюмов / идёт / с первого октября → ___", instr="Formar la frase", size=20, gap=8)
e.ex("B1", "Frases", "Из тыквы делают фонарь.", "из + genitivo: из тыквы",
     "из тыквы / делают / фонарь → ___", instr="Formar la frase", size=20, gap=8)
e.ex("B1", "Frases", "В среду я позвоню бабушке.", "Primero el tiempo; позвонить + dativo",
     "в среду / я / позвоню бабушке → ___", instr="Formar la frase", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-molodezh.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · БОЛЬШОЙ РАЗБОР (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("БОЛЬШОЙ РАЗБОР · Análisis en profundidad", "Lucerna", "УРОВЕНЬ B2 · Двенадцать дней каникул · Doce días de vacaciones")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-main")
f.title("12 дней каникул: самые длинные осенние каникулы за десять лет", 36)
f.byline("От редакции Lucerna · Уровень чтения: B2")
f.para("В этом году осенние каникулы у российских школьников получаются особенными. Министерство просвещения рекомендует школам дни каникул с понедельника, 26 октября, по вторник, 3 ноября. Это девять дней.")
f.para("Но посчитайте внимательно. Перед каникулами — выходные: суббота 24 октября и воскресенье 25 октября. А после каникул, в среду 4 ноября, — государственный праздник, День народного единства. Каникулы получаются длинными: двенадцать дней подряд, с 24 октября по 4 ноября. Журналисты пишут: это самые длинные осенние каникулы примерно за десять лет.")
f.para("Важно: даты министерства — это рекомендация, а не приказ. Каждая школа может выбирать свои даты, и обычно школы слушают рекомендацию. У школ с триместрами система другая: у них каникулы чаще, но короче.")
f.para("Что делают семьи? Многие едут в путешествие по России или к бабушкам и дедушкам. Дачники закрывают дачный сезон: убирают дом, выключают воду и говорят даче «до весны». А те, кто остаётся в городе, идут в кино — не зря четыре сказки выходят именно 22 октября.")
f.gloss("рекомендация una recomendación · триместрами los trimestres (tres periodos escolares) · дачный сезон la temporada de la dacha (casa de campo).")
f.end_report()

# col 3: calendar summary + pro/contra
bx = COLX[3]
cal = ["24–25 октября — выходные дни",
       "26 октября – 3 ноября — каникулы (даты рекомендует министерство)",
       "4 ноября — День народного единства, праздник",
       "5 ноября — снова в школу!"]
sy6 = 200
sh6 = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in cal) + 32
p.rect(bx, sy6, CW, sh6, fill=BOX, stroke=LINE, sw=1.4)
yy6 = sy6 + 16
p.text(bx + 22, yy6 + 26, "КАЛЕНДАРЬ КАНИКУЛ", 24, "sans", True, OLIVE)
yy6 += 52
for t in cal:
    yy6 = p.para(bx + 22, yy6 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
pc = ["За: дети хорошо отдохнут, а семьи смогут путешествовать.",
      "Против: родители работают, а после длинных каникул трудно начинать учёбу."]
sy6b = sy6 + sh6 + 24
sh6b = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in pc) + 32
p.rect(bx, sy6b, CW, sh6b, fill="#f1ead6", stroke=LINE, sw=1.4)
yy6 = sy6b + 16
p.text(bx + 22, yy6 + 26, "ЗА И ПРОТИВ · Pros y contras", 24, "sans", True, OLIVE)
yy6 += 52
for t in pc:
    yy6 = p.para(bx + 22, yy6 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", sy6b + sh6b)

# col 3: autumn photo under the pro/contra box (CC0, see assets/CREDITS.md)
image(p, "autumn_path.jpg", bx, sy6b + sh6b + 25, CW, 225, par="xMidYMax slice")
caption(p, bx, sy6b + sh6b + 25 + 225, CW,
        "Осень в парке: аллея, жёлтые листья и пустые скамейки.",
        "Фото: Toxer427 — лицензия CC0 (Wikimedia Commons)")

# ---- calendar strip (full width): 12 days ----
dy = 1300
p.text(MX, dy + 26, "КАНИКУЛЫ ДЕНЬ ЗА ДНЁМ · Las vacaciones día a día", 26, "sans", True, OLIVE)
days = [("24", "сб"), ("25", "вс"), ("26", "пн"), ("27", "вт"), ("28", "ср"), ("29", "чт"),
        ("30", "пт"), ("31", "сб"), ("1", "вс"), ("2", "пн"), ("3", "вт"), ("4", "ср")]
cellw = (RIGHT - MX) // 12
for i, (dn, wd) in enumerate(days):
    cx = MX + i * cellw
    if i in (0, 1):
        fillc = "#efe3bd"          # weekend before
    elif i == 11:
        fillc = "#e3b7a4"          # Unity Day holiday
    else:
        fillc = BOX                # school holidays
    p.rect(cx + 2, dy + 44, cellw - 4, 96, fill=fillc, stroke=LINE, sw=1.2)
    p.text(cx + cellw / 2, dy + 92, dn, 30, "serif", True, INK, anchor="middle")
    p.text(cx + cellw / 2, dy + 124, wd, 19, "sans", False, GREY, anchor="middle")
p.para(MX, dy + 168, "Жёлтое — выходные перед каникулами · светлое — каникулы (26 октября – 3 ноября) · розовое — праздник 4 ноября. Октябрь: 24–31, ноябрь: 1–4.", 20, "serif", False, GREY, RIGHT - MX, 1.35)

# ---- practice chart ----
chy = dy + 226
p.text(MX, chy + 26, "ЧТО БУДУТ ДЕЛАТЬ ШКОЛЬНИКИ НА КАНИКУЛАХ? · УЧЕБНЫЕ ДАННЫЕ · Datos de práctica", 26, "sans", True, OLIVE)
p.text(MX, chy + 56, "Это учебный опрос редакции для упражнений — не настоящая статистика. Una encuesta de práctica de la redacción, para entrenarse: no son estadísticas reales.", 19.5, "sans", False, BRICK)
chart = [("Поедут к бабушке и дедушке", 34), ("Останутся дома", 28),
         ("Поедут в путешествие", 22), ("Кино, прогулки и спорт", 16)]
yy = chy + 84
for lab, val in chart:
    w_px = round(val * 600 / 34)
    p.text(MX, yy + 24, lab, 21.5, "serif", False, INK)
    p.rect(MX + 620, yy + 2, w_px, 30, fill=OLIVE)
    p.text(MX + 620 + w_px + 14, yy + 24, f"{val}%", 21.5, "sans", True, BRICK)
    yy += 46
print("P6 chart ends", yy)

# ---- P6 exercises ----
ey = yy + 44
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Ejercicios de la página 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8 · niveles mezclados: busca por el número de ejercicio", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · КАЛЕНДАРЬ И ДИАГРАММА", 25)
e.expl("Responde con ayuda del calendario y del gráfico de práctica.")
e.ex("B2", "Opción múltiple", "C", "12 días en total",
     "Сколько дней длятся каникулы вместе с выходными и праздником? A. 9 · B. 11 · C. 12", size=20, gap=8)
e.ex("B2", "Completar", "3", "Las vacaciones recomendadas terminan el 3 de noviembre",
     "Каникулы по рекомендации министерства — с 26 октября по ___ ноября.", instr="Completar", size=20, gap=8)
e.ex("B2", "Opción múltiple", "B", "Datos de práctica: la mayoría va a casa de los abuelos",
     "По учебным данным, больше всего школьников... A. останутся дома · B. поедут к бабушке и дедушке · C. поедут в путешествие", size=20, gap=8)
e.ex("B2", "Completar", "22", "Datos de práctica: 22 %",
     "По учебным данным, в путешествие поедут ___ % школьников.", instr="Completar", size=20, gap=8)
e.ex("B2", "Completar", "28", "Datos de práctica: 28 %",
     "По учебным данным, дома останутся ___ % школьников.", instr="Completar", size=20, gap=8)
e.ex("B2", "Opción múltiple", "B", "El 4 de noviembre es el Día de la Unidad Nacional",
     "4 ноября — это... A. обычный учебный день · B. День народного единства · C. начало каникул", size=20, gap=8)
e.head("B · ПО ТЕКСТУ", 25)
e.expl("Completa con las palabras de la página 6.")
e.ex("B2", "Completar", "рекомендация", "рекомендация = una recomendación",
     "Даты министерства — это ___, а не приказ.", instr="Completar", size=20, gap=8)
e.ex("B2", "Completar", "слушают", "слушать → слушают",
     "Школы обычно ___ рекомендацию министерства.", instr="Completar", size=20, gap=8)
e.ex("B2", "Completar", "триместрами", "с + instrumental: с триместрами",
     "У школ с ___ каникулы чаще, но короче.", instr="Completar", size=20, gap=8)
e.ex("B2", "Completar", "закрывают", "закрывать сезон = cerrar la temporada",
     "Дачники осенью ___ дачный сезон.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "бабушкам", "к + dativo plural: к бабушкам",
     "Многие семьи едут к ___ и дедушкам.", instr="Completar", size=20, gap=8)
e.ex("B2", "Completar", "5", "El 5 de noviembre vuelve la escuela",
     "После каникул, ___ ноября, снова начинается учёба.", instr="Completar", size=20, gap=8)
e.ex("B2", "Completar", "десять", "unos diez años: за десять лет",
     "Журналисты пишут: это самые длинные осенние каникулы примерно за ___ лет.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar", "22", "Los cuentos salen el 22 de octubre",
     "Четыре сказки выходят в кино ___ октября.", instr="Completar", size=20, gap=8)
e.head("C · СОЕДИНИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.expl("Une las dos frases en una sola.")
e.ex("B2", "Transformación", "Каникулы начинаются 24 октября и длятся до 4 ноября.", "Une con и y длятся",
     "Каникулы начинаются 24 октября. Они длятся до 4 ноября. → ___", instr="Transformar", size=20, gap=8)
e.ex("B2", "Transformación", "Даты — только рекомендация, поэтому школы могут выбирать свои даты.", "поэтому = por eso",
     "Даты — рекомендация. Школы могут выбирать свои даты. → ___ (поэтому)", instr="Transformar", size=20, gap=8)
e.ex("B1", "Transformación", "Дети отдыхают, а родители работают.", "а marca el contraste",
     "Дети отдыхают. Родители работают. → ___ (а)", instr="Transformar", size=20, gap=8)
e.ex("B1", "Transformación", "Семьи едут в путешествие или к бабушкам.", "или = o",
     "Семьи едут в путешествие. Семьи едут к бабушкам. → ___ (или)", instr="Transformar", size=20, gap=8)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-razbor.svg")
print("P6 saved, exercises so far:", len(REG))
