# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TEST (all levels) =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCISES & ANSWERS　Упражнения и ответы", "The Lucerna", "ALL LEVELS　Test yourself　Проверь себя")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1555, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "Tuesday", "Вторник, 3 ноября, день голосования"),
    ("A2", "call", "call = объявить результат"),
    ("A2", "continues", "continues — настоящее время"),
    ("A2", "will meet", "will meet, будущее время"),
    ("B1", "writes", "writes, 3-е лицо единственного числа"),
    ("B1", "will certify", "will certify, будущее время"),
    ("B1", "wears", "wears, 3-е лицо единственного числа"),
    ("B1", "will watch", "will watch, будущее время"),
]
cnums = [reg_ex(lv, "Заполнить пропуски", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　CLOZE　Заполнить пропуски", 24, gap=8)
bf.para(f"Maya is a student in London. This week, she is following the American election. On ({cnums[0]})___ morning, November 3, she reads the news about the midterm election. She learns a new word: a ({cnums[1]})___ is a news organisation's judgement — not the official result. On Wednesday, she writes a sentence: “The vote is over, but the counting ({cnums[2]})___.” Her teacher smiles: “The new Congress ({cnums[3]})___ in January.” Maya ({cnums[4]})___ the dates in her notebook: states ({cnums[5]})___ their counts by December 18. On Monday, she ({cnums[6]})___ odd socks to school for Anti-Bullying Week. And on Friday, she ({cnums[7]})___ the new Hunger Games film with her class.", 21.5)
bf.bridge("Варианты:")
for n, (lv, _k, _nt), opts in zip(cnums, cloze_defs, [
    "A. Monday · B. Tuesday · C. Friday",
    "A. vote · B. call · C. seat",
    "A. continuing · B. was continued · C. continues",
    "A. meet · B. met · C. will meet",
    "A. writes · B. write · C. is wrote",
    "A. certified · B. will certify · C. certifies",
    "A. wears · B. is wear · C. wearing",
    "A. watched · B. watch · C. will watch",
]):
    bf.para(f"{n}. [{lv}] {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B　MULTIPLE CHOICE　Выбор", 24, gap=8)
mcq = [
    ("A2", "B", "У демократов 254 мандата в Палате представителей", "How many House seats did the Democrats win, as called? A. 218 · B. 254 · C. 162"),
    ("A2", "A", "День голосования — 3 ноября", "The vote was on... A. Tue, Nov 3 · B. Sun, Nov 8 · C. Mon, Nov 16"),
    ("A2", "C", "Семь мест в Сенате перешли к другой партии", "How many Senate seats changed hands? A. 2 · B. 5 · C. 7"),
    ("A2", "B", "Новый фильм выходит 20 ноября", "“Sunrise on the Reaping” opens on... A. Nov 16 · B. Fri, Nov 20 · C. Nov 22"),
    ("A2", "A", "Шоу в джунглях, 16 ноября в 9 вечера", "“I'm a Celebrity” starts... A. Mon, Nov 16, 9 p.m. · B. Sun, Nov 15 · C. Fri, Nov 20"),
    ("B1", "A", "Австралия выиграла Эшес 2025–26 со счётом 4–1", "Australia won the 2025–26 Ashes by... A. 4–1 · B. 1–4 · C. 2–2"),
    ("B1", "B", "Тема Недели против травли: «Нарушь молчание»", "The theme of Anti-Bullying Week is... A. “Odd Socks” · B. “Break the Silence” · C. “My day”"),
    ("B1", "A", "Всемирный день ребёнка — 20 ноября", "World Children's Day is on... A. Fri, Nov 20 · B. Thu, Nov 26 · C. Mon, Nov 16"),
    ("B1", "C", "День благодарения — четверг, 26 ноября", "Thanksgiving is on... A. Mon, Nov 16 · B. Fri, Nov 27 · C. Thu, Nov 26"),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "Выбрать ответ", k, nt, body, size=20.5)

# ---- C. reading ----
bf.head("C　READING　Понимание текста", 24, gap=8)
bf.para("Tom is a teacher in Manchester. On Monday, November 16, his class is reading about the American election. “The Democrats won the House with 254 seats,” he says. “And the Senate, with 20 of 33 seats called.” The class asks: “Is it finished?” “No,” says Tom. “The states must certify their counts. And two Senate races are still uncalled.” Then Tom opens the second story: “Today is Odd Socks Day.” The children laugh — Tom is wearing one red sock and one blue sock.", 21.5)
read_qs = [
    ("B1", "B", "Том преподаёт в Манчестере", "Tom is... A. a student · B. a teacher in Manchester · C. a reporter"),
    ("B1", "A", "У демократов 254 мандата в Палате представителей", "The Democrats won the House with... A. 254 seats · B. 218 seats · C. 162 seats"),
    ("B1", "C", "Том надел один красный и один синий носок", "Tom is wearing... A. one red sock · B. one blue sock · C. one red sock and one blue sock"),
    ("B1", "B", "Класс Тома читает новости о выборах", "Tom's class is reading about... A. the Ashes · B. the American election · C. the film"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "Понимание текста", k, nt, body, size=20.5)

# ---- D. sentence building ----
bf.head("D　SENTENCES　Предложения", 24, gap=8)
d_items = [
    ("B1", "will meet", "will + инфинитив",
     "Will future: “The new Congress (meet) in January.” → ___"),
    ("B1", "won", "win → won",
     "Past simple: “The Democrats (win) the House.” → ___"),
    ("B1", "more", "more than, сравнительная степень",
     "Comparative: “254 is ___ than 218.”"),
    ("B2", "whether", "whether = ли",
     "Whether: “Nobody knows ___ the count will change.”"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "Дополнить предложения", k, nt, body, size=20.5)

# ---- E. translation ----
bf.head("E　TRANSLATION　Перевод", 24, gap=8)
e_items = [
    ("B2", "Демократы выиграли Палату представителей и Сенат.", "the House and the Senate = Палата представителей и Сенат",
     "Переведи: “The Democrats won the House and the Senate.”"),
    ("B2", "Подсчёт голосов продолжается.", "continues = всё ещё продолжается",
     "Переведи: “The counting continues.”"),
    ("B2", "Новый Конгресс соберётся в январе 2027 года.", "will meet = соберётся",
     "Переведи: “The new Congress will meet in January 2027.”"),
    ("B1", "Нарушь молчание.", "Break the silence.",
     "Переведи: “Break the silence.”"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "Перевести", k, nt, body, size=20.5)

# ---- F. matching ----
bf.head("F　WORDS　Подобрать пары", 24, gap=8)
bf.match_set("A2", "Подобрать пары",
             ["a call", "a runoff", "to certify", "a midterm"],
             ["an election in the middle of a President's term",
              "a news organisation's judgement on a race",
              "a second vote, when nobody wins",
              "to confirm a count officially"],
             ["b", "c", "d", "a"],
             ["call = объявить результат b", "runoff = второй тур c", "certify = официально утвердить d", "midterm = промежуточные выборы a"],
             instr="Подбери пары")

# ---- G. dialogue (register first) ----
dlg_defs = [
    ("A2", "row", "row = ряд мест"),
    ("A2", "film", "film = фильм"),
    ("A2", "popcorn", "popcorn = попкорн"),
    ("A2", "show", "show = сеанс"),
    ("A2", "Friday", "Friday = пятница"),
]
gnums = [reg_ex(lv, "Диалог", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　Диалог", 24, gap=8)
bf.para(f"— Two tickets for the new Hunger Games film, please. — Which ({gnums[0]})___? — The front row, please. — Here you are. Is this the ({gnums[1]})___ about Haymitch? — Yes, the young Haymitch. — One large ({gnums[2]})___ and two drinks, please. — What time is the next ({gnums[3]})___? — At eight. — And the film opens on ({gnums[4]})___, November 20? — Yes, Friday. Enjoy the film!", 21.5)
bf.para(f"Levels: {gnums[0]}–{gnums[-1]} [A2]", 19.5, "sans", False, GREY, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1570
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "Сочинение", "Открытый вопрос — критерии в рамке сочинения; образец — в рамке на этой странице", "Оценка по пунктам")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　WRITING　Письмо [B1]", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Write a short text (80 to 100 words): “My Monday, November 16”. Tell us: did you wear odd socks, what did you watch on television, what did you read about the election — and one sentence about the film on Friday. The best texts will appear in VOL.5 (page 7, “Readers' Corner”).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "Напиши 80–100 слов по-английски: «Мой понедельник, 16 ноября». Расскажи, надел ли ты разные носки, что смотрел по телевизору вечером, что читал о выборах, и добавь одно предложение о фильме в пятницу.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
image(p, "readingroom.jpg", mx2, wy, mw2, 110)
p.text(mx2, wy + 128, "The Main Reading Room, Library of Congress — Carol M. Highsmith, public domain.", 15.5, "sans", False, GREY)
p.rect(mx2, wy + 150, mw2, 280, fill=BOX)
p.text(mx2 + 22, wy + 188, "MODEL　Образец", 23, "sans", True, OLIVE)
MODEL_TEXT = "On Monday, November 16, I wore odd socks to school — one red, one blue. My teacher smiled and said, “Break the silence.” In the evening, we watched the jungle on television together with my family. On Tuesday, we read about the election in class: the Democrats won the House with 254 seats. On Friday, we will watch the new Hunger Games film. It is a busy week of votes, socks and stories — and I am learning to say it all in English."
p.para(mx2 + 22, wy + 224, MODEL_TEXT, 20, "serif", False, INK, mw2 - 44, 1.42)
print("MODEL words:", sum(1 for t in MODEL_TEXT.split() if any(ch.isalnum() for ch in t)))

# ---- keys ----
ky = wy + 462
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANSWERS　Все ответы с пояснениями (стр. 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
PRINT_NOTES = [3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82, 83, 84, 85, 86, 87, 89, 108, 109, 110, 111]
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— СТРАНИЦА {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and (pg == 8 or e["n"] in PRINT_NOTES):
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13.5, "sans", False, INK, 1.26, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, TOTAL exercises:", len(REG))
