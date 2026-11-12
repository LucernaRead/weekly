# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · FRONT PAGE (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1　FIRST ISSUE", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "WEEKLY IN ENGLISH　КАЖДУЮ НЕДЕЛЮ　АНГЛИЙСКИЙ, КОТОРЫЙ ЧИТАЕТ АМЕРИКА", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "WEEK OF OCTOBER 19 TO 25, 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "The Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК　VOL.1　СТАДИОНЫ　ГОЛОСА　ТЫКВЫ", 36, "serif", True, OLIVE, anchor="middle", spacing=6.7)
p.text(975, 372, "ТЕКСТЫ НА АНГЛИЙСКОМ　ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# clock-contrast band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "EUROPE TURNS ITS CLOCKS BACK SUNDAY — AMERICA WAITS !", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Daylight saving ends one week later in the United States : on Sunday, November 1. Do not change your clock this week !", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "В ВОСКРЕСЕНЬЕ", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "АМЕРИКА — ТОЛЬКО 1 НОЯБРЯ", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "THE BIG STORY　Главная тема", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "First Votes, First Games : America's Biggest Week of the Autumn", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "By The Lucerna newsroom　Reading level : A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Election Day is Tuesday, November 3. But in much of America, the election has already started. This Monday, October 19, early voting opened in Texas — and in Alaska, Arkansas, Connecticut and Colorado too. Millions of people are asking the same questions : where do I vote, and when ?")
f.para("Early voting is simple : you go to a voting place before Election Day, you show your ID, you mark your ballot, and your vote counts on election night. No November lines, no problem if you work on Tuesdays. In Texas, it runs from October 19 to October 30.")
f.para("And that is only half of the week. On Tuesday night, the new NBA season tips off. On Friday night, the World Series begins in Milwaukee. On Sunday, the fastest cars in the world race in Austin, Texas.")
f.para("One thing is sure : this year, baseball will have a champion for the very first time. The Milwaukee Brewers and the Tampa Bay Rays have never won the World Series. One of them will win it now. Our sport dossier is on page 4.")
f.para("This is the first issue of The Lucerna in English. Every week, we read America's real life with you — slowly, clearly, and always from the week's real news. Welcome !")
f.expl("Пояснение — early voting — досрочное голосование · ballot — бюллетень · tip off — начало матча · champion — чемпион.")
f.box("THE WEEK IN NUMBERS　Цифры", [
    ("Nov 3 — Election Day (выборы) · Oct 19 — early voting opens in Texas (старт досрочного голосования в Техасе)", "serif", False, INK, 20.5, 1.35),
    ("43 — NBA games from Tuesday to Sunday (43 игры, вт–вс) · 2 — teams in the World Series, both after a first title (обе — за первым титулом)", "serif", False, INK, 20.5, 1.35),
])
f.head("TRY IT NOW　Попробуйте сразу", 25)
f.ex("A2", "Дополните предложение", "ballot", "ballot = бумажный бюллетень",
     "You mark your choice on a ___ and put it in the box.", size=20.5)
f.ex("A2", "Дополните предложение", "early", "early voting = досрочное голосование",
     "Voting before Election Day is called ___ voting.", size=20.5)
f.ex("A2", "Дополните предложение", "November 3", "день выборов: 3 ноября (вторник)",
     "Election Day is Tuesday, ___.", size=20.5)
f.ex("A2", "Дополните предложение", "champion", "champion = чемпион",
     "The winner of the World Series is the ___ of baseball.", size=20.5)
f.ex("B1", "Дополните предложение", "opened", "началось ещё в понедельник: прошедшее время opened",
     "Early voting ___ in Texas on Monday, October 19.", size=20.5)
f.ex("B1", "Дополните предложение", "first", "first title = первый титул",
     "One team will now win the World Series for the ___ time.", size=20.5)
f.end_report()

# ---- searches chart (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 668, fill=BOX)
p.text(gx + 22, gy + 40, "SEARCHES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "OF THE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Тренды поиска　Google Trends США", 19, "sans", False, GREY)
gt = [
    ("early voting", 250),
    ("world series schedule", 218),
    ("hot dog recall", 186),
    ("lakers roster", 140),
    ("barca vs real madrid", 108),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE)
    byy += 92
p.text(gx + 22, byy + 16, "Snapshots, Mon–Wed Oct 19–21 :", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "search interest changes during the day.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "“hot dog recall” 200K+ в пн. (стр. 2)", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1280
p.rect(gx, sy, gw, 372, fill="#f0eee5")
p.text(gx + 22, sy + 40, "IN THIS ISSUE　В этом выпуске", 24, "sans", True, OLIVE)
som = [
    ("p.2", "Checks, fridges & clocks", "A2"),
    ("p.3", "Halloween in America", "A2→B1"),
    ("p.4", "The biggest sports week", "B1"),
    ("p.5", "Screens, streams & AI", "B1"),
    ("p.6", "The midterm deep read", "B2"),
    ("p.7", "Phrases of the week", "A2→B2"),
    ("p.8", "Exercises & answers", "all"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 72, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "THE WORD OF THE WEEK", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "« fall back »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "when clocks go back one hour in autumn. Spring forward, fall back.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "(часы) переводят назад: fall back.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "ws1912.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Boston fans at the Polo Grounds, New York, on October 8, 1912 : Game 1 of the World Series. The Fall Classic was already America's autumn ritual 114 years ago.",
        "Bain News Service, Library of Congress — public domain")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-fall")
f2.head("FALL, THE SEASON OF FIRSTS", 25)
f2.para("Autumn in America is a season of firsts : the first votes, the first games, the first cold evenings. There is a first champion coming in baseball, and a first issue of this paper in your hands.", 22.5)
f2.para("All week, our reporters follow the same rhythm : vote early, play hard, read slowly. See you on page 2 !", 22.5)
f2.end_report()
# col 3 IN BRIEF
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX)
p.text(bx + 22, 1914, "IN BRIEF　Коротко", 24, "sans", True, OLIVE)
brefs = [
    ("WORLD SERIES", "Game 1 is Friday night in Milwaukee. Neither team has ever won it. (page 4)"),
    ("CLOCKS", "Europe changes its clocks on Sunday. America waits until November 1. (page 7)"),
    ("HALLOWEEN", "Saturday, October 31 : costumes, candy — and maybe a Game 7. (page 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "LIGHTNING QUIZ　Блиц-опрос", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Читайте первую полосу, выбирайте ответ　Ответы на странице 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "Выбор ответа", "B", "досрочное голосование в Техасе начинается в понедельник, 19 октября",
      "Early voting in Texas starts on... A. November 3 · B. Monday, October 19 · C. November 1", size=21)
qf.ex("A2", "Выбор ответа", "C", "Америка переводит часы назад только 1 ноября",
      "America turns its clocks back on... A. October 25 · B. October 31 · C. November 1", size=21)
qf.ex("A2", "Выбор ответа", "A", "первый матч Мировой серии — в Милуоки",
      "Game 1 of the World Series is in... A. Milwaukee · B. Tampa · C. Los Angeles", size=21)
qf.ex("A2", "Выбор ответа", "B", "новый сезон НБА начинается во вторник, 20 октября",
      "The new NBA season starts on... A. Friday · B. Tuesday · C. Sunday", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LIFE　Жизнь", "The Lucerna", "LEVEL A2　Money, checks & your fridge　Деньги, чеки и ваш холодильник")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Social Security Checks Grow by 3.6% in January", 32)
f.byline("By The Lucerna newsroom　Reading level : A2")
f.para("Good news for nearly 72 million Americans : on Wednesday, October 14, the Social Security Administration announced a cost-of-living adjustment — a « COLA » — of 3.6% for 2027. From January, the average retired worker will get about 75 dollars more every month.")
f.para("Why do the checks grow ? Because life costs more. When the prices of food, homes and energy go up, the checks go up too — that is the idea of the cost-of-living adjustment. Workers on SSI, a second program for people with very low incomes, see their increase a little earlier : on December 31, 2026. About 7.3 million people receive SSI.")
f.para("When will you see your number ? Personal notices come online at the end of November, and by mail in December. Every household does the same maths this week : 3.6% of my check is... how much, exactly ?")
f.para("How is the number chosen ? Government statisticians follow the prices of a basket of everyday things — food, homes, energy, transport. When the basket costs more, the COLA rises. It is a promise written into the system : your check follows the cost of life.")
f.para("Will 3.6% make anyone rich ? No. But for many households, 75 dollars is the difference between a hard month and an easier one — a full fridge, a warm house. That is why one small percentage is the week's biggest kitchen-table story.")
f.para("The system is old. The first monthly check went to Ida May Fuller, of Vermont, on January 31, 1940. It was 22.54 dollars. In three years of work, Miss Fuller had paid 24.75 dollars into the system. She lived to be 100 years old, and in her long retirement she received more than 22,000 dollars in checks.")
f.box("DO THE MATHS　Посчитаем", [
    ("3.6% of $1,000 is $36. Of $2,000, it is $72. The average increase — about $75 — tells you the average check is a little over $2,000 a month.", "serif", False, INK, 21.5, 1.4),
])
f.head("CHECK YOUR FRIDGE !", 25)
f.para("Second story of the week — and it is in your kitchen. On Saturday, October 17, the US Department of Agriculture announced a big recall : about 1.58 million pounds of hot dogs, bacon and deli meats from one company, Kayem Foods. A cooler in the factory did not work correctly, and the food was not cold enough.", 23.5)
f.para("What must you do ? Do not eat the food. Throw it away, or take it back to the shop. At the time of the announcement, no illnesses were reported — but the rule with a recall is simple : when in doubt, throw it out.", 23.5)
f.para("How do you read a recall notice ? Look for three things : the name of the food, the dates on the packet, and the lot number — a code printed near the date. If your packet matches, it goes in the bin, not on the table. A recall sounds frightening, but it is also good news : it means the safety system works.", 23.5)
f.gloss("cost-of-living — стоимость жизни · a check — чек; ежемесячная выплата · a notice — уведомление · a pound — фунт (около 0,45 кг) · to recall — отзывать (товар).")
f.end_report()

# col 3: image + facts (sequential, measured)
ix = COLX[3]
image(p, "sscard.jpg", ix, 200, CW, 440)
cy3 = caption(p, ix, 640, CW, "A Social Security card from 1943 : the program began in 1935, and the first monthly check — 22.54 dollars — was paid in 1940.",
              "Social Security Administration — public domain")
sav = ["Nearly 72 million people receive Social Security money every month.",
       "The first check, in 1940, was 22.54 dollars. The average increase in 2027 is about 75 dollars a month.",
       "Notices arrive online in late November and by mail in December. Check your number !"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in sav) + 14
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DID YOU KNOW ?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "And you ? Is there a hot dog in your fridge today ? What money comes into your house every month ? Write two sentences in English and send them to the newsroom : the best ones will be printed in VOL.2 (page 7, « Readers' Corner »)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Есть ли у вас хот-дог в холодильнике? Какой доход приходит в семью?", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "AND YOU ?　А вы?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Есть ли у вас хот-дог в холодильнике? Какой доход приходит в семью?", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Telling the time wide box ----
dy = 1570
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "TELLING THE TIME　Как назвать время", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Game times this week　Время начала игр этой недели", 20, "sans", False, GREY, anchor="end")

def clock(cx, cy, r, hh, mm, label):
    p.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fbfaf6" stroke="{INK}" stroke-width="3"/>')
    import math
    for k in range(12):
        a = math.radians(k * 30)
        x1, y1 = cx + (r - 12) * math.sin(a), cy - (r - 12) * math.cos(a)
        x2, y2 = cx + r * math.sin(a), cy - r * math.cos(a)
        p.add(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{INK}" stroke-width="2.4"/>')
    ah = math.radians((hh % 12) * 30 + mm * 0.5)
    am = math.radians(mm * 6)
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.55)*math.sin(ah):.0f}" y2="{cy - (r*0.55)*math.cos(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.82)*math.sin(am):.0f}" y2="{cy - (r*0.82)*math.cos(am):.0f}" stroke="{OLIVE}" stroke-width="4" stroke-linecap="round"/>')
    p.text(cx, cy + r + 34, label, 22, "serif", True, INK, anchor="middle")

clock(240, dy + 140, 74, 8, 0, "It is eight o'clock.")
clock(560, dy + 140, 74, 2, 30, "It is half past two.")
clock(880, dy + 140, 74, 7, 45, "It is quarter to eight.")
lx = 1090
ly = dy + 66
for line in [
    ("half past", "= 30 minutes after the hour (половина часа)"),
    ("quarter past", "= 15 minutes after (четверть часа)"),
    ("quarter to", "= 15 minutes before (без четверти)"),
    ("noon / midnight", "= 12:00 in the day / at night (полдень / полночь)"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 240, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 40
p.para(lx, ly + 24, "This week : Game 1 of the World Series starts at 8 p.m. on Friday. In Europe, the clocks fall back on Sunday — in America, on Sunday, November 1 : spring forward, fall back.", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 340
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCISES　Упражнения (страница 2)", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы — на странице 8", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P2-ex")
e.head("A　WHAT TIME IS IT ?", 25)
e.expl("Дополните предложения по времени.")
e.ex("A2", "Дополните предложение", "half past", "8:30 = половина девятого",
     "8:30 — It is ___ eight.", instr="Вставьте", size=22)
e.ex("A2", "Дополните предложение", "quarter past", "9:15 = четверть десятого",
     "9:15 — It is ___ nine.", instr="Вставьте", size=22)
e.ex("A2", "Дополните предложение", "quarter to", "7:45 = без четверти восемь",
     "7:45 — It is ___ eight.", instr="Вставьте", size=22)
e.ex("A2", "Дополните предложение", "midnight", "0:00 = полночь",
     "0:00 — It is ___ . The city sleeps.", instr="Вставьте", size=22)
e.ex("A2", "Дополните предложение", "o'clock", "3:00 = ровно три",
     "3:00 — It is three ___ . The game starts !", instr="Вставьте", size=22)
e.head("B　GOING TO", 25)
e.expl("Перепишите с be going to + глагол.")
e.ex("A2", "Преобразование предложения", "Checks are going to grow in January.", "checks — множественное число: are going to",
     "Checks (grow) in January. → ___", instr="Перепишите")
e.ex("A2", "Преобразование предложения", "Milwaukee is going to play Game 1 on Friday.", "Milwaukee — единственное число: is going to",
     "Milwaukee (play) Game 1 on Friday. → ___", instr="Перепишите")
e.ex("A2", "Преобразование предложения", "We are going to check the fridge tonight.", "we → are going to",
     "We (check) the fridge tonight. → ___", instr="Перепишите")
e.ex("B1", "Преобразование предложения", "Are you going to vote early this year ?", "вопрос: be выносится вперёд",
     "You (vote) early this year ? → ___", instr="Перепишите")
e.head("C　COMPREHENSION", 25)
e.expl("Статья (стр. 2): выберите ответ.")
e.ex("A2", "Выбор ответа", "B", "COLA вырастет на 3,6% (данные SSA)",
     "In 2027, checks grow by... A. 1.6% · B. 3.6% · C. 6.3%", size=22)
e.ex("A2", "Выбор ответа", "B", "уведомления: онлайн в конце ноября, по почте в декабре",
     "COLA notices arrive... A. in October · B. in late Nov. and Dec. · C. next summer", size=22)
e.ex("A2", "Выбор ответа", "C", "причина отзыва: сломался холодильник на заводе",
     "The hot dogs were recalled because... A. they were old · B. the price was wrong · C. a cooler failed", size=22)
e.ex("A2", "Выбор ответа", "A", "первый ежемесячный чек — 22,54 доллара (1940)",
     "The first check, in 1940, was... A. $22.54 · B. $75 · C. $225.40", size=22)
e.head("D　THE WORDS", 25)
e.match_set("A2", "Пары слов",
            ["a benefit", "a recall", "a pound", "the cost of living"],
            ["the price of everyday life",
             "money the government pays regularly",
             "about 0.45 kilos — 16 ounces",
             "the company takes its food back"],
            ["b", "d", "c", "a"],
            ["benefit = регулярные выплаты государства, b", "recall = отзыв товара компанией, d", "pound = около 0,45 кг, c", "cost of living = цены повседневной жизни, a"],
            instr="Соедините пары слов")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-life.svg")
print("P2 saved, exercises so far:", len(REG))
