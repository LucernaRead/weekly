# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ru-pt-proof/repro-svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · ПЕРВАЯ ПОЛОСА (A2) =================
CURPAGE[0] = 1
p = BSPage4()

p.text(MX, 92, "VOL. 2 · ВТОРОЙ ВЫПУСК", 23, "sans", True, OLIVE)
p.text(975, 92, "КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · TODA SEMANA · O RUSSO QUE A RÚSSIA LÊ", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "НЕДЕЛЯ СО 2 ПО 8 НОЯБРЯ 2026 ГОДА", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SEMANÁRIO RUSSO · VOL.2 · ПРАЗДНИК · СКИДКИ · ФУТБОЛ", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "TEXTOS EM RUSSO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 20, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "ОДНА СРЕДА ПОСРЕДИ НЕДЕЛИ!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "4 ноября — выходной, а 3 ноября — короткий день. Плюс скидки 11.11 и футбол.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "UMA QUARTA-FEIRA NO MEIO DA SEMANA", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "4 de novembro é feriado · ver páginas 2 e 6", 21, "sans", False, "#b3a06a", anchor="end")

hy = 580
p.text(MX, hy + 26, "ГЛАВНАЯ ТЕМА · Tema principal", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Одна среда посреди недели", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "Праздник, скидки и футбол: как Россия живёт неделю с выходным в среду", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "От редакции Lucerna · Уровень чтения: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Эта неделя в России — необычная. В понедельник и во вторник люди работают, а в среду — выходной. Среда, 4 ноября, — выходной посреди рабочей недели.", size=24)
f.para("Во вторник, 3 ноября, день короче на час. Это правило: день перед праздником всегда короче на один час.", size=24)
f.para("У школьников — последние дни каникул: они отдыхают со 2 по 4 ноября, а в четверг, 5 ноября, снова идут в школу.", size=24)
f.para("Всю неделю идёт распродажа 11.11: она началась 22 октября и закончится 12 ноября. А в выходные — футбол: 14-й тур чемпионата России, последний перед паузой.", size=24)
f.para("Как жить неделю с праздником посреди недели? Об этом — весь наш номер. Приятного чтения!", size=24)
f.bridge("посреди no meio · короче на час uma hora a menos · пауза um intervalo.")
f.box("НЕДЕЛЯ В ЦИФРАХ · Em números", [
    ("1 — выходной посреди недели: среда, 4 ноября", "serif", False, INK, 20, 1.35),
    ("1 — час: на столько короче рабочий день 3 ноября (3 de novembro: uma hora a menos)", "serif", False, INK, 20, 1.35),
    ("12 — ноября закончится распродажа 11.11 (liquidação até 12 de novembro)", "serif", False, INK, 20, 1.35),
    ("19:30 — начало матча «Краснодар» — ЦСКА в субботу (sábado, 19:30)", "serif", False, INK, 20, 1.35),
])
f.head("СЕЙЧАС ВЫ · Agora é com você", 25)
f.ex("A2", "Completar frases", "4", "Quarta-feira, 4 de novembro",
     "Выходной посреди недели — ___ ноября.", size=19.5, gap=6)
f.ex("A2", "Completar frases", "3", "Terça-feira, 3 de novembro",
     "Короткий день — ___ ноября.", size=19.5, gap=6)
f.ex("A2", "Completar frases", "час", "uma hora a menos: на час",
     "День перед праздником короче на один ___.", size=19.5, gap=6)
f.ex("A2", "Completar frases", "5", "Quinta-feira, 5 de novembro: volta às aulas",
     "Школьники снова идут в школу ___ ноября.", size=19.5, gap=6)
f.ex("A2", "Completar frases", "12", "Liquidação até 12 de novembro",
     "Распродажа 11.11 закончится ___ ноября.", size=19.5, gap=6)
f.ex("B1", "Completar frases", "последний", "последний перед паузой = a última rodada antes da pausa",
     "14-й тур — ___ тур перед паузой.", size=19.5, gap=6)
f.end_report()

gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "О ЧЁМ ПИШУТ", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "СМИ · Na mídia", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Главные темы недели в российских СМИ", 19, "sans", False, GREY)
topics = [
    "Неделя с выходным в среду: как её прожить?",
    "Распродажа 11.11: скидки и промокоды",
    "14-й тур: последний перед паузой",
    "Последние дни школьных каникул",
    "Что меняется с 1 ноября?",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 26
p.text(gx + 22, gy + 636, "По российским СМИ, октябрь 2026 г.", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "Segundo a mídia russa, outubro de 2026", 19, "sans", False, GREY)

sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "В ЭТОМ НОМЕРЕ · Sumário", 24, "sans", True, OLIVE)
som = [
    ("Стр. 2", "Короткий день и 1 ноября", "A2"),
    ("Стр. 3", "Праздник 4 ноября", "A2→B1"),
    ("Стр. 4", "14-й тур: футбол", "B1"),
    ("Стр. 5", "Скидки 11.11", "B1"),
    ("Стр. 6", "Неделя: разбор", "B2"),
    ("Стр. 7", "Фразы недели", "A2→B2"),
    ("Стр. 8", "Тест и все ответы", "все"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

my = 1636
p.text(gx, my + 24, "СЛОВО НЕДЕЛИ · A palavra", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "«сокращённый день» — рабочий день на час короче. 3 ноября — сокращённый день.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "сокращённый день = dia de trabalho reduzido.", 19, "sans", False, GREY, gw, 1.35)

p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "autumn_path.jpg", ix, iy, iw, 320, par="xMidYMax slice")
caption(p, ix, iy + 320, iw,
        "Ноябрь в парке: аллея, жёлтые листья и пустые скамейки. На этой неделе — последние дни каникул.",
        "Фото: Toxer427 — лицензия CC0 (Wikimedia Commons)")
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-school")
f2.head("ПОСЛЕДНИЕ ДНИ КАНИКУЛ", 25)
f2.para("Понедельник, 2 ноября, — ещё каникулы. Вторник, 3 ноября, — тоже каникулы. А в среду, 4 ноября, — праздник. В четверг, 5 ноября, — снова в школу!", 22.5)
f2.para("Три дня — и снова уроки. Успейте отдохнуть! Подробнее — на 2-й странице.", 22.5)
f2.end_report()
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "КОРОТКО · Em resumo", 24, "sans", True, OLIVE)
brefs = [
    ("СРЕДА", "4 ноября — выходной. 3 ноября — день на час короче."),
    ("СКИДКИ", "Распродажа 11.11 идёт всю неделю, до 12 ноября."),
    ("ФУТБОЛ", "В выходные — 14-й тур. В субботу «Краснодар» — ЦСКА в 19:30."),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "БЛИЦ-ВИКТОРИНА · Quiz-relâmpago", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Leia a primeira página e escolha a resposta certa · Respostas na página 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "Escolha múltipla", "B", "Quarta-feira, 4 de novembro",
      "Выходной посреди недели — это... A. вторник · B. среда · C. пятница", size=21)
qf.ex("A2", "Escolha múltipla", "B", "3 de novembro: uma hora a menos",
      "Короткий день — это... A. 2 ноября · B. 3 ноября · C. 5 ноября", size=21)
qf.ex("A2", "Escolha múltipla", "C", "Liquidação até 12 de novembro",
      "Распродажа 11.11 закончится... A. 4 ноября · B. 8 ноября · C. 12 ноября", size=21)
qf.ex("A2", "Escolha múltipla", "A", "Sábado: Krasnodar contra o CSKA",
      "В субботу играют... A. «Краснодар» — ЦСКА · B. «Спартак» — «Акрон» · C. «Зенит» — «Ростов»", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-pervaya.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · ЖИЗНЬ (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("ЖИЗНЬ · Vida", "Lucerna", "УРОВЕНЬ A2 · Короткий день, 1 ноября и прошлая неделя · Dia curto, 1.º de novembro e a semana passada")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Вторник короче на час", 37)
f.byline("От редакции Lucerna · Уровень чтения: A2")
f.para("Во вторник, 3 ноября, рабочий день короче на час. Это правило: день перед праздником всегда короче на один час. Если вы обычно работаете до шести, во вторник вы уйдёте в пять.")
f.para("А в среду, 4 ноября, — выходной. В четверг и в пятницу — снова рабочие дни. Получается странная неделя: два дня работаем, один день отдыхаем, два дня работаем — и выходные.")
f.para("Что делать в среду? Многие поедут на один день в другой город или к родным. Другие останутся дома: выспаться и отдохнуть тоже важно.")
f.gloss("перед праздником antes do feriado · уйдёте você sai do trabalho · выспаться dormir até tarde.")
f.head("ЧТО МЕНЯЕТСЯ С 1 НОЯБРЯ", 25)
f.para("С 1 ноября в России меняются некоторые правила: налоги, аренда, платежи. А ещё из-за праздника меняются даты выплат: пенсии, которые должны прийти 4 ноября, придут раньше — 3 ноября.")
f.para("Проверьте свои даты: если выплата должна прийти в праздник, она придёт раньше. Это обычное правило: в праздник банки и почта не работают.")
f.gloss("выплат pagamentos · раньше antes · почта os correios.")
f.head("ПРОШЛАЯ НЕДЕЛЯ: ЧТО БЫЛО", 25)
f.para("В воскресенье, 25 октября, ЦСКА победил «Спартак» в дерби со счётом 2:0. Оба гола забили в первом тайме: Глебов и Мусаев. В прошлом номере мы писали о дерби до игры — теперь результат известен.")
f.para("А первый снег в Москве в обещанные дни не выпал: конец октября выдался тёплым. 26 октября в Москве было +12 градусов. Прогнозы не сбылись — и это тоже новость.")
f.para("В среду, 28 октября, был День бабушек и дедушек, а в субботу, 31 октября, — Хэллоуин. Обе даты уже прошли: о них мы писали в прошлом номере.")
f.gloss("сбылись se confirmaram (de uma previsão) · дерби o dérbi · в прошлом номере no número anterior.")
f.end_report()

ix = COLX[3]
last = ["Дерби 25 октября: ЦСКА — «Спартак» 2:0.",
        "Первый снег в Москве не выпал: 26 октября было +12°.",
        "28 октября — День бабушек и дедушек.",
        "31 октября — Хэллоуин.",
        "Каникулы заканчиваются 4 ноября."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in last) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ПРОШЛАЯ НЕДЕЛЯ", 24, "sans", True, OLIVE)
yy3 += 52
for t in last:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "А вы? Как вы проведёте среду, 4 ноября: поедете в другой город, пойдёте на ярмарку или просто выспитесь? Напишите два предложения по-русски и пришлите в редакцию: лучшие мы напечатаем в VOL.3 (страница 7, «Письма читателей»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("E você? Como vai passar a quarta-feira, 4 de novembro? Escreva duas frases em russo e envie à redação.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "А ВЫ? · E você?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "E você? Como vai passar a quarta-feira, 4 de novembro? Escreva duas frases em russo e envie à redação.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "СЛОВА НЕДЕЛИ · Palavras da semana", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Четыре слова о неделе с праздником · Quatro palavras sobre uma semana com feriado", 20, "sans", False, GREY, anchor="end")
words = [
    ("выходной", "день, когда не работают", "dia de folga"),
    ("будни", "рабочие дни недели", "dias úteis"),
    ("сокращённый день", "день на час короче", "dia de trabalho reduzido"),
    ("отпуск", "дни отдыха от работы", "férias"),
]
for i, (t, lab, cn) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 234, "Запомните: выходной — это день отдыха, а будни — рабочие дни. 4 ноября — выходной, а 3 ноября — сокращённый день.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "УПРАЖНЕНИЯ · Exercícios da página 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8 · Níveis misturados — procure o seu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · ПОНИМАНИЕ", 25)
e.bridge("Leia os textos da página 2 e escolha a resposta certa.")
e.ex("A2", "Escolha múltipla", "B", "3 de novembro: uma hora a menos",
     "Короткий день — это... A. 2 ноября · B. 3 ноября · C. 4 ноября", size=19, gap=6)
e.ex("A2", "Escolha múltipla", "B", "O dia de trabalho antes do feriado é uma hora mais curto",
     "Почему 3 ноября короче? A. Это выходной · B. Это день перед праздником · C. Это воскресенье", size=19, gap=6)
e.ex("A2", "Escolha múltipla", "A", "A aposentadoria de 4 de novembro chega em 3 de novembro",
     "Пенсии за 4 ноября придут... A. 3 ноября · B. 4 ноября · C. 5 ноября", size=19, gap=6)
e.ex("A2", "Escolha múltipla", "C", "Placar do dérbi: 2 a 0",
     "Дерби ЦСКА — «Спартак» закончилось... A. 1:0 · B. 0:0 · C. 2:0", size=19, gap=6)
e.ex("A2", "Escolha múltipla", "B", "26 de outubro em Moscou: +12 graus",
     "Почему первый снег не выпал? A. Было холодно · B. Было тепло: +12° · C. Был дождь", size=19, gap=6)
e.head("B · СЛОВА НЕДЕЛИ", 25)
e.bridge("Complete com as palavras da página 2.")
e.ex("A2", "Completar frases", "выходной", "выходной = dia de folga",
     "4 ноября — ___.", instr="Complete", size=19, gap=6)
e.ex("A2", "Completar frases", "будни", "будни = dias úteis",
     "Понедельник и вторник — это ___.", instr="Complete", size=19, gap=6)
e.ex("A2", "Completar frases", "сокращённый", "сокращённый день = dia de trabalho reduzido",
     "3 ноября — ___ день.", instr="Complete", size=19, gap=6)
e.ex("B1", "Completar frases", "отпуск", "взять отпуск = tirar férias",
     "Многие берут ___ в четверг и в пятницу.", instr="Complete", size=19, gap=6)
e.ex("B1", "Completar frases", "выспаться", "выспаться = dormir até tarde",
     "В выходной можно хорошо ___.", instr="Complete", size=19, gap=6)
e.head("C · ЧИСЛА И ДАТЫ", 25)
e.bridge("Complete com os números e as datas das páginas 1 e 2.")
e.ex("A2", "Completar frases", "2", "Segunda-feira, 2 de novembro",
     "Неделя начинается ___ ноября.", instr="Complete", size=19, gap=6)
e.ex("B1", "Completar frases", "5", "Quinta-feira, 5 de novembro: volta às aulas",
     "Школьники идут в школу ___ ноября.", instr="Complete", size=19, gap=6)
e.ex("A2", "Completar frases", "12", "Liquidação até 12 de novembro",
     "Распродажа закончится ___ ноября.", instr="Complete", size=19, gap=6)
e.ex("B1", "Completar frases", "25", "Dérbi em 25 de outubro",
     "Дерби было ___ октября.", instr="Complete", size=19, gap=6)
e.head("D · ПРОШЛАЯ НЕДЕЛЯ", 25)
e.match_set("A2", "Associação de palavras",
            ["25 октября", "26 октября", "28 октября", "31 октября"],
            ["День бабушек и дедушек",
             "Хэллоуин",
             "дерби ЦСКА — «Спартак» 2:0",
             "в Москве было +12 градусов"],
            ["c", "d", "a", "b"],
            ["Dérbi c", "+12 graus d", "Dia dos Avós a", "Halloween b"],
            instr="Associe")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-zhizn.svg")
print("P2 saved, exercises so far:", len(REG))
