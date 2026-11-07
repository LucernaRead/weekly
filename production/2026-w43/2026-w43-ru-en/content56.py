# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ru-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · МОЛОДЁЖЬ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("МОЛОДЁЖЬ · Youth", "Lucerna", "УРОВЕНЬ B1 · Хэллоуин и планы на каникулы · Halloween and holiday plans")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P5-feature")
f.title("Хэллоуин — 31 октября: Москва готовится", 37)
f.byline("От редакции Lucerna · Уровень чтения: B1")
f.para("В субботу, 31 октября, Москва празднует Хэллоуин. До праздника — ещё неделя, но подготовка уже идёт: молодые москвичи выбирают костюмы и покупают билеты. В этом году Хэллоуин — в субботу, и это удобно: на следующий день не надо рано вставать.")
f.para("Что будет в городе? Открытый фестиваль «Хиллоуин'26» в парке ужасов обещает парад костюмов. А конкурс костюмов в Reels идёт уже с 1 октября: участники показывают свои костюмы в коротких видео.")
f.para("Для тех, кто любит вечеринки, клуб Loft Hall делает ночь UNDR Halloween: 31 октября с 23:00 до 06:00. Билеты на странице события стоят 900 рублей — и их уже покупают.")
f.para("Подготовка идёт и дома: кто-то покупает готовый костюм, а кто-то делает его сам — из старой одежды, бумаги и красок. До субботы ещё есть время, но все хотят успеть: хороший костюм — половина праздника.")
f.gloss("костюмы costumes · парад a parade · билеты tickets.")
f.head("КАНИКУЛЫ + ХЭЛЛОУИН = ПЛАНЫ", 25)
f.para("Хэллоуин в этом году — внутри каникул: школьники отдыхают с 24 октября по 4 ноября. Поэтому планы простые: днём — гулять и смотреть новые сказки в кино, а 31 октября — праздник с друзьями.")
f.para("Не забудьте: в среду, 28 октября, — День бабушек и дедушек. Позвоните бабушке и дедушке или приедьте в гости. А в субботу вечером наденьте костюм: ведьма, вампир или привидение — что выберете вы?")
f.para("Социальные сети уже полны видео с костюмами: конкурс в Reels идёт с 1 октября, и участники каждую неделю показывают новые идеи. А вы уже выбрали костюм?")
f.gloss("привидение a ghost · в гости = to visit someone at home")
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
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Page 5 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels may mix — find your item by number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.note("Read the page 5 articles and choose the right answer.")
e.ex("A2", "multiple choice", "B", "Halloween is 31 October",
     "Хэллоуин в 2026 году — ... A. 25 октября · B. 31 октября · C. 1 ноября", size=20, gap=8)
e.ex("A2", "multiple choice", "C", "31 October is a Saturday",
     "31 октября — это... A. пятница · B. воскресенье · C. суббота", size=20, gap=8)
e.ex("B1", "multiple choice", "A", "The costume contest runs from 1 October",
     "Конкурс костюмов в Reels идёт... A. с 1 октября · B. с 25 октября · C. с 31 октября", size=20, gap=8)
e.ex("B1", "multiple choice", "B", "The ticket costs 900 rubles",
     "Билет на UNDR Halloween стоит... A. 500 рублей · B. 900 рублей · C. 100 рублей", size=20, gap=8)
e.ex("A2", "multiple choice", "A", "Grandparents Day is 28 October",
     "День бабушек и дедушек — ... A. 28 октября · B. 24 октября · C. 4 ноября", size=20, gap=8)
e.head("B · СЛОВА НЕДЕЛИ", 25)
e.note("Fill in the words from page 5.")
e.ex("A2", "fill-in", "костюмы", "костюмы = costumes",
     "Молодые москвичи выбирают ___ и покупают билеты.", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "парад", "парад костюмов = a costume parade",
     "Фестиваль обещает ___ костюмов.", instr="Fill in", size=20, gap=8)
e.ex("A2", "fill-in", "23:00", "The party starts at 23:00",
     "Вечеринка в Loft Hall начинается в ___ (время).", instr="Fill in", size=20, gap=8)
e.ex("A2", "fill-in", "бабушек", "День бабушек и дедушек",
     "28 октября — День ___ и дедушек.", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "фонарь", "фонарь из тыквы = a pumpkin lantern",
     "Из тыквы делают ___ со смешной рожицей.", instr="Fill in", size=20, gap=8)
e.head("C · КОСТЮМЫ", 25)
e.match_set("B1", "matching",
            ["ведьма", "вампир", "привидение", "тыква"],
            ["овощ — главный символ Хэллоуина",
             "женщина с метлой в сказках",
             "оно живёт в старом доме и пугает людей",
             "он пьёт кровь и боится солнца"],
            ["b", "d", "c", "a"],
            ["witch b", "vampire d", "ghost c", "pumpkin a"],
            instr="Match the pairs")
e.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.note("Put the words in order to make a sentence.")
e.ex("B1", "sentence building", "Мы покупаем билеты на вечеринку.", "Verb + object + direction",
     "мы / покупаем / билеты / на вечеринку → ___", instr="Build a sentence", size=20, gap=8)
e.ex("A2", "sentence building", "Конкурс костюмов идёт с первого октября.", "Subject + verb + time",
     "конкурс костюмов / идёт / с первого октября → ___", instr="Build a sentence", size=20, gap=8)
e.ex("B1", "sentence building", "Из тыквы делают фонарь.", "из + genitive: из тыквы",
     "из тыквы / делают / фонарь → ___", instr="Build a sentence", size=20, gap=8)
e.ex("B1", "sentence building", "В среду я позвоню бабушке.", "Time first; позвонить + dative",
     "в среду / я / позвоню бабушке → ___", instr="Build a sentence", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-molodezh.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · БОЛЬШОЙ РАЗБОР (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("БОЛЬШОЙ РАЗБОР · The deep read", "Lucerna", "УРОВЕНЬ B2 · Двенадцать дней каникул · Twelve days of holidays")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-main")
f.title("12 дней каникул: самые длинные осенние каникулы за десять лет", 36)
f.byline("От редакции Lucerna · Уровень чтения: B2")
f.para("В этом году осенние каникулы у российских школьников получаются особенными. Министерство просвещения рекомендует школам дни каникул с понедельника, 26 октября, по вторник, 3 ноября. Это девять дней.")
f.para("Но посчитайте внимательно. Перед каникулами — выходные: суббота 24 октября и воскресенье 25 октября. А после каникул, в среду 4 ноября, — государственный праздник, День народного единства. Каникулы получаются длинными: двенадцать дней подряд, с 24 октября по 4 ноября. Журналисты пишут: это самые длинные осенние каникулы примерно за десять лет.")
f.para("Важно: даты министерства — это рекомендация, а не приказ. Каждая школа может выбирать свои даты, и обычно школы слушают рекомендацию. У школ с триместрами система другая: у них каникулы чаще, но короче.")
f.para("Что делают семьи? Многие едут в путешествие по России или к бабушкам и дедушкам. Дачники закрывают дачный сезон: убирают дом, выключают воду и говорят даче «до весны». А те, кто остаётся в городе, идут в кино — не зря четыре сказки выходят именно 22 октября.")
f.gloss("рекомендация a recommendation · триместрами trimesters · дачный сезон the dacha season.")
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
p.text(bx + 22, yy6 + 26, "ЗА И ПРОТИВ · For and against", 24, "sans", True, OLIVE)
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
p.text(MX, dy + 26, "КАНИКУЛЫ ДЕНЬ ЗА ДНЁМ · The holidays day by day", 26, "sans", True, OLIVE)
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
p.text(MX, chy + 26, "ЧТО БУДУТ ДЕЛАТЬ ШКОЛЬНИКИ НА КАНИКУЛАХ? · УЧЕБНЫЕ ДАННЫЕ · Practice data", 26, "sans", True, OLIVE)
p.text(MX, chy + 56, "Это учебный опрос редакции для упражнений — не настоящая статистика. A practice survey by the editors for the exercises — not real statistics.", 19.5, "sans", False, BRICK)
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
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Page 6 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels may mix — find your item by number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · КАЛЕНДАРЬ И ДИАГРАММА", 25)
e.note("Answer from the calendar strip and the practice chart.")
e.ex("B2", "multiple choice", "C", "12 days in total",
     "Сколько дней длятся каникулы вместе с выходными и праздником? A. 9 · B. 11 · C. 12", size=20, gap=8)
e.ex("B2", "fill-in", "3", "The recommended holidays end 3 November",
     "Каникулы по рекомендации министерства — с 26 октября по ___ ноября.", instr="Fill in", size=20, gap=8)
e.ex("B2", "multiple choice", "B", "Practice chart: most go to grandparents",
     "По учебным данным, больше всего школьников... A. останутся дома · B. поедут к бабушке и дедушке · C. поедут в путешествие", size=20, gap=8)
e.ex("B2", "fill-in", "22", "Practice data: 22%",
     "По учебным данным, в путешествие поедут ___ % школьников.", instr="Fill in", size=20, gap=8)
e.ex("B2", "fill-in", "28", "Practice data: 28%",
     "По учебным данным, дома останутся ___ % школьников.", instr="Fill in", size=20, gap=8)
e.ex("B2", "multiple choice", "B", "4 November is Unity Day",
     "4 ноября — это... A. обычный учебный день · B. День народного единства · C. начало каникул", size=20, gap=8)
e.head("B · ПО ТЕКСТУ", 25)
e.note("Fill in the words from page 6.")
e.ex("B2", "fill-in", "рекомендация", "рекомендация = a recommendation",
     "Даты министерства — это ___, а не приказ.", instr="Fill in", size=20, gap=8)
e.ex("B2", "fill-in", "слушают", "слушать → слушают",
     "Школы обычно ___ рекомендацию министерства.", instr="Fill in", size=20, gap=8)
e.ex("B2", "fill-in", "триместрами", "с + instrumental: с триместрами",
     "У школ с ___ каникулы чаще, но короче.", instr="Fill in", size=20, gap=8)
e.ex("B2", "fill-in", "закрывают", "закрывать сезон = to close the season",
     "Дачники осенью ___ дачный сезон.", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "бабушкам", "к + dative plural: к бабушкам",
     "Многие семьи едут к ___ и дедушкам.", instr="Fill in", size=20, gap=8)
e.ex("B2", "fill-in", "5", "Back to school on 5 November",
     "После каникул, ___ ноября, снова начинается учёба.", instr="Fill in", size=20, gap=8)
e.ex("B2", "fill-in", "десять", "about ten years: за десять лет",
     "Журналисты пишут: это самые длинные осенние каникулы примерно за ___ лет.", instr="Fill in", size=20, gap=8)
e.ex("B1", "fill-in", "22", "The fairy-tale films open 22 October",
     "Четыре сказки выходят в кино ___ октября.", instr="Fill in", size=20, gap=8)
e.head("C · СОЕДИНИТЕ ПРЕДЛОЖЕНИЯ", 25)
e.note("Join the two sentences into one.")
e.ex("B2", "transformation", "Каникулы начинаются 24 октября и длятся до 4 ноября.", "Join with и длятся",
     "Каникулы начинаются 24 октября. Они длятся до 4 ноября. → ___", instr="Rewrite", size=20, gap=8)
e.ex("B2", "transformation", "Даты — только рекомендация, поэтому школы могут выбирать свои даты.", "поэтому = so, therefore",
     "Даты — рекомендация. Школы могут выбирать свои даты. → ___ (поэтому)", instr="Rewrite", size=20, gap=8)
e.ex("B1", "transformation", "Дети отдыхают, а родители работают.", "а marks the contrast",
     "Дети отдыхают. Родители работают. → ___ (а)", instr="Rewrite", size=20, gap=8)
e.ex("B1", "transformation", "Семьи едут в путешествие или к бабушкам.", "или = or",
     "Семьи едут в путешествие. Семьи едут к бабушкам. → ___ (или)", instr="Rewrite", size=20, gap=8)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-razbor.svg")
print("P6 saved, exercises so far:", len(REG))
