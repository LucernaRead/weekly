# -*- coding: utf-8 -*-
"""One-shot EN->RU explanation-layer transform for W45 zh-cn x ru.
Applies exact-literal replacements (whole-string matches, never AST byte
offsets, never regex) to the builder's OWN copy of the core build, then
asserts each pattern matched at least once and logs actual counts.
Frozen Chinese target text is never a search target: every old literal is
an English explanation string (or a bilingual furniture string whose
Chinese half is carried over verbatim into the new literal).
Order note: 'Fill in the blank' is replaced BEFORE 'Fill in'.
Run once from the build dir; re-running is a no-op only if old literals
are gone (asserts will fail loudly on a second run - that is intended).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)

CORE_DIR = "weekly-report-w45-zhcn-core"
MY_DIR = "weekly-report-w45-zh-cn-ru"

# (filename, old, new) - old must occur >= 1 time; counts are logged.
PAIRS = []
def add(fn, old, new):
    PAIRS.append((fn, old, new))

# ---- repoint OUT/BASE (expanduser form, all 6 lines) ----
add("content12.py", "files/weekly-report-w45-zhcn-core/svg", "files/weekly-report-w45-zh-cn-ru/svg")
add("content34.py", "files/weekly-report-w45-zhcn-core/svg", "files/weekly-report-w45-zh-cn-ru/svg")
add("content56.py", "files/weekly-report-w45-zhcn-core/svg", "files/weekly-report-w45-zh-cn-ru/svg")
add("content7.py", "files/weekly-report-w45-zhcn-core/svg", "files/weekly-report-w45-zh-cn-ru/svg")
add("content8.py", "files/weekly-report-w45-zhcn-core/svg", "files/weekly-report-w45-zh-cn-ru/svg")
add("render.py", "files/weekly-report-w45-zhcn-core", "files/weekly-report-w45-zh-cn-ru")

# ---- bslib4 furniture (3 lines; VOL.2 kept) ----
add("bslib4.py", "Lucerna · 简体中文周报 VOL.2 · 简体中文正文 · 英语讲解 · Simplified Chinese text · English explanations",
    "Lucerna · КИТАЙСКИЙ (УПРОЩЁННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ")
add("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Страница {n} из {total}"')
add("bslib4.py", "Notes｜", "Пояснение — ")

# ---- content12 P1 ----
add("content12.py", "每周读中文 · Read real Chinese, every week", "每周读中文 · Читайте настоящий китайский — каждую неделю")
add("content12.py", "给学中文的人的周报 — Read the real China, in Chinese", "给学中文的人的周报 — Настоящий Китай — по-китайски")
add("content12.py", 'p.text(975, 434, "简体中文正文 · 英语讲解 — Simplified Chinese text · Explanations in English · the edition for English-speaking readers", 19.5, "sans", True, OLIVE, anchor="middle")',
    'p.text(975, 434, "ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", 19.5, "sans", True, BRICK, anchor="middle")')
add("content12.py", "Shopping week meets winter · see pages 2–3", "Неделя покупок встречает зиму · см. страницы 2–3")
add("content12.py", "头条 · Top story", "头条 · Главная тема")
add("content12.py", "Lucerna editors · Reading level A2", "Редакция Lucerna · Уровень чтения A2")
add("content12.py", "xiànhuò 现货 — goods in stock, ready to ship · lìjiǎn 立减 — an instant discount at checkout · zhíjiàng 直降 — a direct price cut · jiéqì 节气 — the 24 solar terms that divide the year.",
    "xiànhuò 现货 — товар в наличии, готов к отправке · lìjiǎn 立减 — мгновенная скидка на кассе · zhíjiàng 直降 — прямое снижение цены · jiéqì 节气 — 24 солнечных термина, делящих год.")
add("content12.py", "数字看本周 · This week in numbers", "数字看本周 · Неделя в цифрах")
add("content12.py", "Nov 13 — the last day of the spot-sale period", "13 ноября — последний день продаж со склада")
add("content12.py", "Nov 7, Saturday — 立冬 (Start of Winter)", "7 ноября, суббота — 立冬 (Начало зимы)")
add("content12.py", "Oct 12, 20:00 — JD.com spot sales began", "12 октября, 20:00 — JD.com начал продажи со склада")
add("content12.py", "Nov 10, 20:00 — the peak sale (高潮场) begins next week", "10 ноября, 20:00 — пиковая распродажа (高潮场) начнётся на следующей неделе")
add("content12.py", "即学即练 · Try it now", "即学即练 · Сразу к практике")
add("content12.py", "JD.com spot sales began on Oct 12.", "JD.com начал продажи со склада 12 октября.")
add("content12.py", "Taobao and Tmall pre-sales began on Oct 15.", "Предпродажи Taobao и Tmall начались 15 октября.")
add("content12.py", "Spot sales run until Nov 13.", "Продажи со склада идут до 13 ноября.")
add("content12.py", "Start of Winter falls on Saturday, Nov 7.", "Начало зимы — в субботу, 7 ноября.")
add("content12.py", "Start of Winter is winter's first solar term.", "Начало зимы — первый солнечный термин зимы.")
add("content12.py", "This year many goods are marked down directly.", "В этом году многие товары подешевели напрямую.")
add("content12.py", "本周日历 · This week", "本周日历 · Календарь недели")
add("content12.py", "11月2日—8日 · Nov 2–8", "11月2日—8日 · 2–8 ноября")
add("content12.py", "What happens this week", "Что будет на этой неделе")
add("content12.py", "The Swiss stage ends Nov 1, so the quarter-final teams are not known at press time. Quarter-finals run Nov 4–7, the first semi-final Nov 8, all at 06:00 Beijing time.",
    "Швейцарский этап заканчивается 1 ноября, поэтому на момент сдачи номера четвертьфиналисты ещё неизвестны. Четвертьфиналы пройдут 4–7 ноября, первый полуфинал — 8 ноября, всё в 06:00 по пекинскому времени.")
add("content12.py", "All times Beijing time", "Всё время — пекинское")
add("content12.py", "S16 teams depend on the Swiss stage", "Команды S16 зависят от швейцарского этапа")
add("content12.py", "本期目录 · Contents", "本期目录 · Содержание")
add("content12.py", "本周词 · Word of the week", "本周词 · Слово недели")
add("content12.py", "「立冬」 lìdōng — Start of Winter: the first solar term of winter. 立冬到了,冬天要来了。Example: 「立冬那天,我们吃饺子。」",
    "「立冬」 lìdōng — Начало зимы: первый солнечный термин зимы. 立冬到了,冬天要来了。Пример: 「立冬那天,我们吃饺子。」")
add("content12.py", "Photo: Map hobby — CC0 (Wikimedia Commons)", "Фото: Map hobby — CC0 (Wikimedia Commons)")
add("content12.py", "快讯 · Briefs", "快讯 · Коротко")
add("content12.py", "闪电问答 · Quick quiz", "闪电问答 · Быстрый опрос")
add("content12.py", "Read page 1 and choose · 答案见第 8 版", "Прочитайте страницу 1 и выберите · 答案见第 8 版")
add("content12.py", "Start of Winter is on Saturday, Nov 7.", "Начало зимы — в субботу, 7 ноября.")

# ---- content12 P2 ----
add("content12.py", "生活 · Life", "生活 · Жизнь")
add("content12.py", "Level A2 · 双11购物生活 · 立冬生活 · Shopping & the first winter days", "Уровень A2 · 双11购物生活 · 立冬生活 · Покупки и первые зимние дни")
add("content12.py", "cāngkù 仓库 — a warehouse · píngjià 评价 — a review, what buyers say · chǐmǎ 尺码 — a size · tuìhuànhuò 退换货 — returns and exchanges.",
    "cāngkù 仓库 — склад · píngjià 评价 — отзыв, мнение покупателей · chǐmǎ 尺码 — размер · tuìhuànhuò 退换货 — возврат и обмен.")
add("content12.py", "满减与直降 · Old vs new", "满减与直降 · Старое и новое")
add("content12.py", "The old rule many shoppers knew was 「满300减50」 (spend 300 yuan, save 50). This year the common pattern is 直降 (zhíjiàng): the price itself drops, and the checkout price is what you pay. The example below uses practice numbers, not real shop prices.",
    "Старое правило, которое знали многие покупатели, — 「满300减50」 (потрать 300 юаней, сэкономь 50). В этом году обычная схема — 直降 (zhíjiàng): сама цена падает, и цена на кассе — это то, что вы платите. Пример ниже использует учебные числа, а не настоящие цены магазинов.")
add("content12.py", "Practice example · 练习例子", "Разобранный пример · 练习例子")
add("content12.py", "bǔdōng 补冬 — eating well before winter · jiāozǐ 饺子 — dumplings · cíbā 糍粑 — sticky rice cakes · qīzhōng 期中 — mid-term (exams).",
    "bǔdōng 补冬 — хорошо питаться перед зимой · jiāozǐ 饺子 — пельмени · cíbā 糍粑 — лепёшки из клейкого риса · qīzhōng 期中 — середина семестра (экзамены).")
add("content12.py", "本周生活小日历 · This week's dates", "本周生活小日历 · Даты этой недели")
add("content12.py", "Photo: Paul Gilmore — CC0 (Wikimedia Commons)", "Фото: Paul Gilmore — CC0 (Wikimedia Commons)")
add("content12.py", "你知道吗 · Did you know?", "你知道吗 · А вы знали?")
add("content12.py", "说说你自己 · And you?", "说说你自己 · А вы?")
add("content12.py", "And you? What do you want to buy this 双11? What would you eat on 立冬? Write two sentences in Chinese.",
    "А вы? Что вы хотите купить в этот 双11? Что бы вы съели на 立冬? Напишите два предложения по-китайски.")
add("content12.py", "购物词语卡 · Shopping words", "购物词语卡 · Слова для покупок")
add("content12.py", "Four words you will see on every shopping app", "Четыре слова из любого торгового приложения")
add("content12.py", '("现货", "xiànhuò · goods in stock", "in stock now, ready to ship")', '("现货", "xiànhuò · товар в наличии", "в наличии, готов к отправке")')
add("content12.py", '("直降", "zhíjiàng · a direct price cut", "the price drops directly, no maths")', '("直降", "zhíjiàng · прямое снижение цены", "цена падает напрямую, без подсчётов")')
add("content12.py", '("立减", "lìjiǎn · an instant discount", "taken off at checkout")', '("立减", "lìjiǎn · мгновенная скидка", "вычитается на кассе")')
add("content12.py", '("补冬", "bǔdōng · winter nourishment", "eating well before winter")', '("补冬", "bǔdōng · питание перед зимой", "хорошо питаться перед зимой")')
add("content12.py", "Remember the sentence: 「买现货不用等,先看结算页,再付款。」", "Запомните предложение: 「买现货不用等,先看结算页,再付款。」")
add("content12.py", "练习 · Exercises", "练习 · Упражнения")
add("content12.py", "Answers on page 8 · 答案见第 8 版", "Ответы на странице 8 · 答案见第 8 版")
add("content12.py", "A · 读一读选一选 · Read & choose", "A · 读一读选一选 · Выбор ответа")
add("content12.py", "Read page 2 and choose the best answer.", "Прочитайте страницу 2 и выберите лучший ответ.")
add("content12.py", "Taobao and Tmall spot sales began on Oct 20.", "Продажи со склада Taobao и Tmall начались 20 октября.")
add("content12.py", "直降 means the price itself drops.", "zhíjiàng — сама цена падает.")
add("content12.py", "After 立冬 the weather gets colder day by day.", "После lìdōng погода холодает день ото дня.")
add("content12.py", "The WeChat shop event runs until Nov 15.", "Акция магазина WeChat идёт до 15 ноября.")
add("content12.py", "B · 词语填空 · Word blanks", "B · 词语填空 · Впишите слово")
add("content12.py", "Fill each blank with the right word.", "Впишите в каждый пропуск верное слово.")
add("content12.py", "xiànhuò — goods in stock, ready to ship.", "xiànhuò — товар в наличии, готов к отправке.")
add("content12.py", "zhíjiàng — the price itself drops.", "zhíjiàng — сама цена падает.")
add("content12.py", "bǔdōng — eating well before winter.", "bǔdōng — хорошо питаться перед зимой.")
add("content12.py", "jiǎozǐ — northern families eat these at 立冬.", "jiǎozǐ — их едят северные семьи на lìdōng.")
add("content12.py", "qīzhōng — mid-term exams fall in early November in some schools.", "qīzhōng — экзамены середины семестра проходят в начале ноября в некоторых школах.")
add("content12.py", "C · 数字与日期 · Numbers", "C · 数字与日期 · Числа и даты")
add("content12.py", "Use the practice example on this page.", "Используйте разобранный пример на этой странице.")
add("content12.py", "The sweater costs 240 yuan in the example.", "Свитер стоит 240 юаней в примере.")
add("content12.py", "240 + 80 = 320 yuan together.", "240 + 80 = 320 юаней вместе.")
add("content12.py", "320 − 50 = 270 yuan after the direct cut.", "320 − 50 = 270 юаней после прямого снижения.")
add("content12.py", "The WeChat shop event runs 35 days in total.", "Акция магазина WeChat идёт всего 35 дней.")
add("content12.py", "D · 词语配对 · Matching", "D · 词语配对 · Сопоставьте пары")
add("content12.py", "xiànhuò 现货 = in stock, b", "xiànhuò = в наличии, b")
add("content12.py", "zhíjiàng 直降 = price drops, d", "zhíjiàng = цена падает, d")
add("content12.py", "lìjiǎn 立减 = off at checkout, c", "lìjiǎn = вычитается на кассе, c")
add("content12.py", "bǔdōng 补冬 = eat well before winter, a", "bǔdōng = хорошо питаться перед зимой, a")
# instr forms (blank BEFORE bare: P1 headline ex use the blank form)
add("content12.py", 'instr="Fill in the blank"', 'instr="Впишите слово"')
add("content12.py", 'instr="Fill in"', 'instr="Впишите"')
add("content12.py", 'instr="Match the words"', 'instr="Сопоставьте"')

# ---- content34 P3 ----
add("content34.py", "文化 · Culture", "文化 · Культура")
add("content34.py", "Level A2→B1 · 立冬:冬天的第一个节气 · Start of Winter", "Уровень A2→B1 · 立冬:冬天的第一个节气 · Начало зимы")
add("content34.py", "Lucerna editors · Reading level A2→B1", "Редакция Lucerna · Уровень чтения A2→B1")
add("content34.py", "hòu 候 — a five-day micro-season · jiāotì 交替 — one thing giving way to another · cǎifǎng 采访 — to interview, to report from the scene.",
    "hòu 候 — пятидневный микросезон · jiāotì 交替 — смена одного другим · cǎifǎng 采访 — брать интервью, репортаж с места событий.")
add("content34.py", "hòu yīfu 厚衣服 — warm clothes · rè fàn 热饭 — a hot meal · zháoliáng 着凉 — to catch cold.",
    "hòu yīfu 厚衣服 — тёплая одежда · rè fàn 热饭 — горячая еда · zháoliáng 着凉 — простудиться.")
add("content34.py", "Photo: Gerda Arendt — CC0 (Wikimedia Commons)", "Фото: Gerda Arendt — CC0 (Wikimedia Commons)")
add("content34.py", "节日小日历 · Festival dates", "节日小日历 · Праздничные даты")
add("content34.py", "Photo: Syced — CC0 (Wikimedia Commons)", "Фото: Syced — CC0 (Wikimedia Commons)")
add("content34.py", "And you? What would you eat on 立冬? Is it cold where you live? Write two sentences in Chinese.",
    "А вы? Что бы вы съели на 立冬? Холодно ли там, где вы живёте? Напишите два предложения по-китайски.")
add("content34.py", "练习 · Exercises", "练习 · Упражнения")
add("content34.py", "Answers on page 8 · 答案见第 8 版", "Ответы на странице 8 · 答案见第 8 版")
add("content34.py", "A · 读一读选一选 · Read & choose", "A · 读一读选一选 · Выбор ответа")
add("content34.py", "Read page 3 and choose the best answer.", "Прочитайте страницу 3 и выберите лучший ответ.")
add("content34.py", "立冬 is the 19th of the 24 solar terms.", "lìdōng — 19-й из 24 солнечных терминов.")
add("content34.py", "First micro-season: water begins to freeze.", "Первый микросезон: вода начинает замерзать.")
add("content34.py", "Northern families eat dumplings at 立冬.", "Северные семьи едят пельмени на lìdōng.")
add("content34.py", "A journalist interviews people and writes the news.", "Журналист берёт интервью и пишет новости.")
add("content34.py", "B · 词语填空 · Word blanks", "B · 词语填空 · Впишите слово")
add("content34.py", "Fill each blank with the right word.", "Впишите в каждый пропуск верное слово.")
add("content34.py", "lìdōng — Start of Winter, Nov 7.", "lìdōng — Начало зимы, 7 ноября.")
add("content34.py", "shuǐ shǐ bīng — water begins to freeze (1st micro-season).", "shuǐ shǐ bīng — вода начинает замерзать (1-й микросезон).")
add("content34.py", "jiǎozǐ — northern families eat these at 立冬.", "jiǎozǐ — их едят северные семьи на lìdōng.")
add("content34.py", "tāngyuán — sticky rice balls eaten in some southern places.", "tāngyuán — шарики из клейкого риса, которые едят в некоторых южных местах.")
add("content34.py", "jìzhě — a journalist interviews and writes news.", "jìzhě — журналист берёт интервью и пишет новости.")
add("content34.py", "C · 数字与日期 · Numbers", "C · 数字与日期 · Числа и даты")
add("content34.py", "Answer with dates and numbers from page 3.", "Отвечайте датами и числами со страницы 3.")
add("content34.py", "立冬 is the 19th solar term.", "lìdōng — 19-й солнечный термин.")
add("content34.py", "Start of Winter is on Nov 7.", "Начало зимы — 7 ноября.")
add("content34.py", "The solar-term moment is 17:52.", "Момент солнечного термина — 17:52.")
add("content34.py", "Journalists' Day is on Nov 8.", "День журналиста — 8 ноября.")
add("content34.py", "D · 词语配对 · Matching", "D · 词语配对 · Сопоставьте пары")
add("content34.py", "水始冰 = water begins to freeze, b", "shuǐ shǐ bīng = вода начинает замерзать, b")
add("content34.py", "地始冻 = earth begins to freeze, c", "dì shǐ dòng = земля начинает промерзать, c")
add("content34.py", "雉入大水为蜃 = the old pheasant story, d", "zhì rù dà shuǐ wéi shèn = старая история о фазане, d")
add("content34.py", "bǔdōng 补冬 = eat well before winter, a", "bǔdōng = хорошо питаться перед зимой, a")
add("content34.py", 'instr="Fill in"', 'instr="Впишите"')
add("content34.py", 'instr="Match the words"', 'instr="Сопоставьте"')

# ---- content34 P4 ----
add("content34.py", "说说你自己 · And you?", "说说你自己 · А вы?")
add("content34.py", "Start of Winter falls on Saturday, Nov 7.", "Начало зимы — в субботу, 7 ноября.")
add("content34.py", "体育 · Sport", "体育 · Спорт")
add("content34.py", "Level B1 · S16 瑞士轮与淘汰赛 · Worlds S16: Swiss stage & knockouts", "Уровень B1 · S16 瑞士轮与淘汰赛 · Чемпионат мира S16: швейцарский этап и плей-офф")
add("content34.py", "Lucerna editors · Reading level B1", "Редакция Lucerna · Уровень чтения B1")
add("content34.py", "tǎotài 淘汰 — to knock out, to eliminate · nèizhàn 内战 — a match between two teams from the same region · zhǐbù 止步 — to stop here, to go no further.",
    "tǎotài 淘汰 — выбить, устранить · nèizhàn 内战 — матч двух команд одного региона · zhǐbù 止步 — остановиться здесь, дальше не пройти.")
add("content34.py", "S16 赛程 · S16 schedule (Beijing time)", "S16 赛程 · Расписание S16 (пекинское время)")
add("content34.py", "Standings as of Oct 27, 2026: GEN and DK already 3–0 and through; AL and TSW 0–3 and out. Source: Sina Sports S16 guide (Beijing times) and match reports, Oct 26–27.",
    "Положение на 27 октября 2026 года: GEN и DK уже 3–0 и прошли дальше; AL и TSW 0–3 и выбыли. Источник: гид Sina Sports по S16 (пекинское время) и отчёты о матчах 26–27 октября.")
add("content34.py", "体育小日历 · Sports dates", "体育小日历 · Спортивные даты")
add("content34.py", "看比赛的中文 · Match words", "看比赛的中文 · Слова матча")
add("content34.py", '("通宵", "tōngxiāo — to stay up all night for a match.")', '("通宵", "tōngxiāo — не спать всю ночь ради матча.")')
add("content34.py", '("加油", "jiāyóu — come on! (what fans shout).")', '("加油", "jiāyóu — давай! (так кричат болельщики).")')
add("content34.py", '("翻盘", "fānpán — a comeback win, turning a game around.")', '("翻盘", "fānpán — волевая победа, переворот в игре.")')
add("content34.py", "Read page 4 and choose the best answer.", "Прочитайте страницу 4 и выберите лучший ответ.")
add("content34.py", "The Swiss stage is played in Allen, Texas.", "Швейцарский этап проходит в Аллене, штат Техас.")
add("content34.py", "AL lost all three of its Swiss-stage series.", "AL проиграла все три серии швейцарского этапа.")
add("content34.py", "IG beat HLE on Oct 26.", "IG обыграла HLE 26 октября.")
add("content34.py", "Quarter-finals start at 06:00 Beijing time.", "Четвертьфиналы начинаются в 06:00 по пекинскому времени.")
add("content34.py", "The final starts at 03:00 Beijing time on Nov 15.", "Финал начинается в 03:00 по пекинскому времени 15 ноября.")
add("content34.py", "Read the schedule on page 4.", "Прочитайте расписание на странице 4.")
add("content34.py", "Àilún — Allen, Texas, hosts the Swiss stage.", "Àilún — Аллен, штат Техас, принимает швейцарский этап.")
add("content34.py", "nèizhàn — AL lost the all-LPL match to TES.", "nèizhàn — AL проиграла матч внутри LPL команде TES.")
add("content34.py", "táotài — three wins send a team to the knockouts.", "táotài — три победы выводят команду в плей-офф.")
add("content34.py", "fānpán — TES turned the game against G2 around.", "fānpán — TES перевернула игру против G2.")
add("content34.py", "jiāyóu — what fans shout for their team.", "jiāyóu — так болельщики кричат за свою команду.")
add("content34.py", "Three wins send a team through from the Swiss stage.", "Три победы выводят команду из швейцарского этапа.")
add("content34.py", "AL won zero series in the Swiss stage.", "AL не выиграла ни одной серии на швейцарском этапе.")
add("content34.py", "The Swiss stage runs until Nov 1.", "Швейцарский этап идёт до 1 ноября.")
add("content34.py", "瑞士轮 = the Swiss stage, d", "ruìshìlún = швейцарский этап, d")
add("content34.py", "内战 = an all-region match, c", "nèizhàn = матч одного региона, c")
add("content34.py", "淘汰赛 = loser goes home, b", "táotàisài = проигравший едет домой, b")
add("content34.py", "总决赛 = the final, a", "zǒngjuésài = финал, a")

# ---- content56 P5 ----
add("content56.py", "青年 · Youth", "青年 · Молодёжь")
add("content56.py", "Level B1 · AI电影 · 立冬新片 · AI films & a winter film", "Уровень B1 · AI电影 · 立冬新片 · Фильмы ИИ и зимний фильм")
add("content56.py", "Lucerna editors · Reading level B1", "Редакция Lucerna · Уровень чтения B1")
add("content56.py", "shùzì xíngxiàng 数字形象 — a digital character · gōngyìng 公映 — a public cinema release · piàofáng 票房 — box-office takings.",
    "shùzì xíngxiàng 数字形象 — цифровой персонаж · gōngyìng 公映 — выход в широкий прокат · piàofáng 票房 — кассовые сборы.")
add("content56.py", "huǒhuà 火化 — cremation · jiùshú 救赎 — redemption, saving each other · yǐhòu 以后 — later, some other day.",
    "huǒhuà 火化 — кремация · jiùshú 救赎 — искупление, спасение друг друга · yǐhòu 以后 — потом, в другой день.")
add("content56.py", "这一周的高频词 · Words of the week", "这一周的高频词 · Слова недели")
add("content56.py", "AI电影 — a film made with AI: no live actors, digital characters only.", "AI电影 — фильм, сделанный с помощью ИИ: без живых актёров, только цифровые персонажи.")
add("content56.py", "Photo: Based5290 — Public domain (Wikimedia Commons)", "Фото: Based5290 — общественное достояние (Wikimedia Commons)")
add("content56.py", "电影小日历 · Film dates", "电影小日历 · Даты фильмов")
add("content56.py", "说说你自己 · And you?", "说说你自己 · А вы?")
add("content56.py", "And you? Would you watch a film made by AI? Who would you watch a film with on 立冬? Write two sentences in Chinese.",
    "А вы? Стали бы вы смотреть фильм, сделанный ИИ? С кем бы вы пошли в кино на 立冬? Напишите два предложения по-китайски.")
add("content56.py", "练习 · Exercises", "练习 · Упражнения")
add("content56.py", "Answers on page 8 · 答案见第 8 版", "Ответы на странице 8 · 答案见第 8 版")
add("content56.py", "A · 读一读选一选 · Read & choose", "A · 读一读选一选 · Выбор ответа")
add("content56.py", "Read page 5 and choose the best answer.", "Прочитайте страницу 5 и выберите лучший ответ.")
add("content56.py", "The AI film has no live actors.", "В фильме ИИ нет живых актёров.")
add("content56.py", "The AI film runs 100 minutes.", "Фильм ИИ идёт 100 минут.")
add("content56.py", "By noon on Oct 26, Maoyan showed about 1.192 million yuan.", "К полудню 26 октября Maoyan показывал около 1,192 миллиона юаней.")
add("content56.py", "The new film opens on Nov 7, Start of Winter.", "Новый фильм выходит 7 ноября, в Начало зимы.")
add("content56.py", "Huang Yan is a crematory worker.", "Хуан Янь — работница крематория.")
add("content56.py", "B · 词语填空 · Word blanks", "B · 词语填空 · Впишите слово")
add("content56.py", "Fill each blank with the right word.", "Впишите в каждый пропуск верное слово.")
add("content56.py", "shùzì — the film's characters are digital images.", "shùzì — персонажи фильма — цифровые изображения.")
add("content56.py", "piàofáng — box-office takings, about 1.192 million yuan.", "piàofáng — кассовые сборы, около 1,192 миллиона юаней.")
add("content56.py", "huǒhuà — Huang Yan works at a crematory.", "huǒhuà — Хуан Янь работает в крематории.")
add("content56.py", "jiùshú — the two women save each other.", "jiùshú — две женщины спасают друг друга.")
add("content56.py", "lìdōng — the new film opens on Start of Winter.", "lìdōng — новый фильм выходит в Начало зимы.")
add("content56.py", "C · 时间与数字 · Times & numbers", "C · 时间与数字 · Числа и даты")
add("content56.py", "Answer with dates and numbers from page 5.", "Отвечайте датами и числами со страницы 5.")
add("content56.py", "The AI film opened on Oct 23.", "Фильм ИИ вышел 23 октября.")
add("content56.py", "On Oct 24–25, each screening averaged 2 viewers.", "24–25 октября на каждый сеанс в среднем приходилось 2 зрителя.")
add("content56.py", "The new film runs 114 minutes.", "Новый фильм идёт 114 минут.")
add("content56.py", "D · 词语配对 · Matching", "D · 词语配对 · Сопоставьте пары")
add("content56.py", "数字形象 = a digital character, b", "shùzì xíngxiàng = цифровой персонаж, b")
add("content56.py", "票房 = box-office takings, a", "piàofáng = кассовые сборы, a")
add("content56.py", "火化师 = a crematory worker, d", "huǒhuàshī = работница крематория, d")
add("content56.py", "救赎 = saving each other, c", "jiùshú = спасение друг друга, c")
add("content56.py", 'instr="Fill in"', 'instr="Впишите"')
add("content56.py", 'instr="Match the words"', 'instr="Сопоставьте"')

# ---- content56 P6 ----
add("content56.py", "深读 · Deep read", "深读 · Глубокое чтение")
add("content56.py", "Level B2 · 双11深读 · Why the rules got simpler", "Уровень B2 · 双11深读 · Почему правила стали проще")
add("content56.py", "Lucerna editors · Reading level B2", "Редакция Lucerna · Уровень чтения B2")
add("content56.py", "jiésuàn 结算 — checkout, settling the bill · yùnfèi 运费 — delivery cost · guǎnggào 广告 — an advertisement.",
    "jiésuàn 结算 — касса, оплата счёта · yùnfèi 运费 — стоимость доставки · guǎnggào 广告 — реклама.")
add("content56.py", "shuōfǎ 说法 — a claim, what someone says · shùjù 数据 — data, measured numbers · tuìhuànhuò 退换货 — returns and exchanges.",
    "shuōfǎ 说法 — утверждение, то, что кто-то говорит · shùjù 数据 — данные, измеренные числа · tuìhuànhuò 退换货 — возврат и обмен.")
add("content56.py", "三个练习篮子:直降以后实付多少钱 · Practice baskets", "三个练习篮子:直降以后实付多少钱 · Учебные корзины")
add("content56.py", "Bars are drawn from 0 (3 px = 1 yuan). Practice data only — not real shop prices. Basket maths is in the article above.",
    "Столбцы построены от 0 (3 пкс = 1 юань). Только учебные данные — не настоящие цены магазинов. Расчёты корзин — в статье выше.")
add("content56.py", "深读要点 · Key points", "深读要点 · Главное")
add("content56.py", "读新闻三问 · Three questions", "读新闻三问 · Три вопроса")
add("content56.py", "And you? What do you check before you buy? Write two sentences in Chinese.",
    "А вы? Что вы проверяете перед покупкой? Напишите два предложения по-китайски.")
add("content56.py", "Read page 6 and choose the best answer.", "Прочитайте страницу 6 и выберите лучший ответ.")
add("content56.py", "This year spot sales are much bigger.", "В этом году продажи со склада гораздо больше.")
add("content56.py", "With 直降 the checkout price is what you pay.", "При zhíjiàng цена на кассе — это то, что вы платите.")
add("content56.py", "AI helps you check prices and reviews first.", "ИИ помогает сначала проверить цены и отзывы.")
add("content56.py", "The WeChat shop event runs 35 days.", "Акция магазина WeChat идёт 35 дней.")
add("content56.py", "The checkout page shows what you really pay.", "Страница кассы показывает, что вы платите на самом деле.")
add("content56.py", "xiànhuò — goods in stock, ready to ship.", "xiànhuò — товар в наличии, готов к отправке.")
add("content56.py", "zhíjiàng — the price itself drops.", "zhíjiàng — сама цена падает.")
add("content56.py", "jiésuàn — the checkout page shows the real price.", "jiésuàn — страница кассы показывает настоящую цену.")
add("content56.py", "yùnfèi — delivery cost, check whether it is included.", "yùnfèi — стоимость доставки, проверьте, включена ли она.")
add("content56.py", "guǎnggào — an advertisement's 'lowest price' needs checking.", "guǎnggào — «самую низкую цену» из рекламы нужно проверять.")
add("content56.py", "C · 练习篮子算一算 · Basket maths", "C · 练习篮子算一算 · Считаем")
add("content56.py", "Compute from the practice baskets.", "Посчитайте по учебным корзинам.")
add("content56.py", "240 + 80 = 320, minus 50 = 270 yuan.", "240 + 80 = 320, минус 50 = 270 юаней.")
add("content56.py", "199 − 20 = 179 yuan.", "199 − 20 = 179 юаней.")
add("content56.py", "120 + 40 = 160 yuan, no direct cut.", "120 + 40 = 160 юаней, без прямого снижения.")
add("content56.py", "Basket A is cut by 50 yuan.", "Корзина А снижена на 50 юаней.")
add("content56.py", "说法 = a claim, c", "shuōfǎ = утверждение, c")
add("content56.py", "数据 = measured numbers, d", "shùjù = измеренные числа, d")
add("content56.py", "结算页 = the checkout page, b", "jiésuànyè = страница кассы, b")
add("content56.py", "运费 = delivery cost, a", "yùnfèi = стоимость доставки, a")

# ---- content7 P7 ----
add("content7.py", "词语 · Language focus", "词语 · Языковой фокус")
add("content7.py", "语言聚焦 · 三个级别,三个主题 · Three levels, three topics", "语言聚焦 · 三个级别,三个主题 · Три уровня, три темы")
add("content7.py", "A2 · 双11与冬天 · Shopping", "A2 · 双11与冬天 · Покупки")
add("content7.py", "Shopping words for this week: 现货 (xiànhuò, in stock), 直降 (zhíjiàng, a direct cut), 立减 (lìjiǎn, off at checkout), 结算页 (jiésuàn yè, the checkout page). Winter words: 立冬 (lìdōng, Start of Winter), 补冬 (bǔdōng, eating well before winter), 厚衣服 (hòu yīfu, warm clothes).",
    "Слова недели о покупках: 现货 (xiànhuò — в наличии), 直降 (zhíjiàng — прямое снижение), 立减 (lìjiǎn — скидка на кассе), 结算页 (jiésuàn yè — страница кассы). Зимние слова: 立冬 (lìdōng — Начало зимы), 补冬 (bǔdōng — питание перед зимой), 厚衣服 (hòu yīfu — тёплая одежда).")
add("content7.py", "Measure words still matter: 一件毛衣 (a sweater), 一条围巾 (a scarf), 一部电影 (a film).",
    "Счётные слова всё ещё важны: 一件毛衣 (свитер), 一条围巾 (шарф), 一部电影 (фильм).")
add("content7.py", "毛衣 takes the measure word 件 jiàn.", "Для свитера счётное слово — 件 jiàn.")
add("content7.py", "直降 means the price itself drops.", "zhíjiàng — сама цена падает.")
add("content7.py", "lìdōng — Start of Winter, Nov 7.", "lìdōng — Начало зимы, 7 ноября.")
add("content7.py", "Clothes take 件, not 个 or 条.", "Для одежды — 件, а не 个 или 条.")
add("content7.py", "One more to practise: 「这件毛衣多少钱?」 (How much is this sweater?) When you shop, ask the price first, then pay.",
    "Ещё для практики: 「这件毛衣多少钱?」 (Сколько стоит этот свитер?) Когда покупаете, сначала спросите цену, потом платите.")
add("content7.py", "B1 · 时间与日期 · Time & dates", "B1 · 时间与日期 · Время и даты")
add("content7.py", "Chinese gives times big → small: year, month, day, weekday, part of day, hour. Examples from this issue: 「11月7日星期六17点52分」 (Sat Nov 7, 17:52), 「11月10日星期二20点」 (Tue Nov 10, 20:00), 「11月15日凌晨3点」 (Nov 15, 3 a.m.). The biggest unit first, nothing out of order.",
    "В китайском время идёт от большого к малому: год, месяц, день, день недели, часть дня, час. Примеры из этого номера: 「11月7日星期六17点52分」 (суббота, 7 ноября, 17:52), 「11月10日星期二20点」 (вторник, 10 ноября, 20:00), 「11月15日凌晨3点」 (15 ноября, 3 часа ночи). Самая большая единица первой, ничего не переставлено.")
add("content7.py", "So English «Saturday evening, Nov 7» becomes 11月7日星期六晚上.", "Так русское «субботний вечер, 7 ноября» становится 11月7日星期六晚上.")
add("content7.py", "凌晨 língchén — the small hours after midnight.", "língchén — глубокая ночь после полуночи.")
add("content7.py", "06:00 is 早上 (morning), not evening.", "06:00 — это zǎoshang (утро), а не вечер.")
add("content7.py", "Big → small order: Nov 7, Saturday, 17:52.", "Порядок от большого к малому: 7 ноября, суббота, 17:52.")
add("content7.py", "Nov 7 is a Saturday — 周六.", "7 ноября — суббота, zhōuliù.")
add("content7.py", "Two more words: 凌晨 (língchén) is the small hours after midnight, before dawn; 傍晚 (bàngwǎn) is the short stretch just before dark.",
    "Ещё два слова: 凌晨 (língchén) — глубокая ночь после полуночи, перед рассветом; 傍晚 (bàngwǎn) — короткий отрезок перед темнотой.")
add("content7.py", "B2 · 读新闻 · Reading the news", "B2 · 读新闻 · Читаем новости")
add("content7.py", "When a story involves a claim (说法), separate three kinds of sentence: claims (说法), data (数据) and advertisements (广告). Page 6 is the example: 「最低价」 is a claim, the practice baskets' 270元 is practice data, and the checkout page shows what you really pay.",
    "Когда в истории есть утверждение (说法), различайте три вида предложений: утверждения (说法), данные (数据) и рекламу (广告). Пример — страница 6: 「最低价」 — это утверждение, 270元 из учебных корзин — учебные данные, а страница кассы показывает, что вы платите на самом деле.")
add("content7.py", "Ask of every price: whose number is it, and where is it written?", "Спрашивайте о каждой цене: чьё это число и где оно написано?")
add("content7.py", "「最低价」 is an advertising claim, not measured data.", "zuìdījià — рекламное утверждение, а не измеренные данные.")
add("content7.py", "shùjù — measured numbers, not claims.", "shùjù — измеренные числа, а не утверждения.")
add("content7.py", "Data and the checkout page first; the headline last.", "Сначала данные и страница кассы, заголовок — последним.")
add("content7.py", "jiésuàn — the checkout page shows the real price.", "jiésuàn — страница кассы показывает настоящую цену.")
add("content7.py", "Try it yourself: in the page-1 calendar box, 「11月7日」 is a date — data. The words in an advertisement are claims. Can you tell them apart?",
    "Попробуйте сами: в календарном блоке на странице 1 「11月7日」 — это дата, то есть данные. А слова из рекламы — утверждения. Сможете их различить?")
add("content7.py", "易错诊所 · Error clinic", "易错诊所 · Клиника ошибок")
add("content7.py", "地 (de) marks how an action is done.", "Частица 地 (de) показывает, как совершается действие.")
add("content7.py", "得 (de) links verb + degree: 跑得快.", "Частица 得 (de) связывает глагол со степенью: 跑得快.")
add("content7.py", "Order: number + measure word + noun. The final 个 is one too many; sweaters take 件.", "Порядок: число + счётное слово + существительное. Последняя 个 — лишняя; для свитеров — 件.")
add("content7.py", "Times go big → small: weekday last.", "Время идёт от большого к малому: день недели — последним.")
add("content7.py", "本周句式 · Sentence frame", "本周句式 · Конструкция недели")
add("content7.py", "「先看评价,再下单。」(First check the reviews, then order.) The frame 先…再… gives the order of actions. More: 「先看天气,再出门。」",
    "「先看评价,再下单。」(Сначала проверьте отзывы, потом заказывайте.) Конструкция 先…再… задаёт порядок действий. Ещё: 「先看天气,再出门。」")
add("content7.py", "Frame: 先 … 再 … — first X, then Y.", "Конструкция: 先 … 再 … — сначала X, потом Y.")
add("content7.py", "读者园地 · Readers' corner", "读者园地 · Уголок читателей")
add("content7.py", "编辑部示例信,不是真实来信。编辑部说明:VOL.1曾预告本期(VOL.2)刊登真实读者来信和VOL.1第8版最佳作文;至今没有收到真实来信,也没有可刊登的投稿,所以本期仍刊登编辑部示例,并继续征集。延期不是取消。Editor's note: VOL.1 promised real letters and the best VOL.1 writing in VOL.2. None have arrived, so this corner still prints an editor's example. Deferred, not cancelled.",
    "Пример письма от редакции — это не настоящее письмо читателя. Пояснение редакции: в VOL.1 было обещано, что в этом номере (VOL.2) появятся настоящие письма читателей и лучшее сочинение со страницы 8 из VOL.1; до сих пор настоящих писем не пришло, и публиковать нечего, поэтому здесь снова пример от редакции. Это отсрочка, а не отмена. Присылайте ваши письма в редакцию! Напишите два предложения по-китайски о вашей неделе — о покупках, о зиме, о чём угодно — и отправьте их нам: лучшие письма мы напечатаем в VOL.3.")
add("content7.py", "本周金句 · Phrases of the week (verbatim, from this issue's own articles)", "本周金句 · Фразы недели (дословно, из статей этого номера)")
add("content7.py", '("「不用等11月11日」", "No need to wait for Nov 11.", "p. 1")', '("「不用等11月11日」", "Не нужно ждать 11 ноября.", "Страница 1")')
add("content7.py", '("「下单就能发货」", "Order it and it ships.", "p. 2")', '("「下单就能发货」", "Заказал — и уже отправлено.", "Страница 2")')
add("content7.py", '("「先看结算页,再付款」", "Check the checkout page, then pay.", "p. 2")', '("「先看结算页,再付款」", "Проверьте страницу кассы, потом платите.", "Страница 2")')
add("content7.py", '("「水开始结冰」", "The water begins to freeze.", "p. 3")', '("「水开始结冰」", "Вода начинает замерзать.", "Страница 3")')
add("content7.py", '("「三场都输了」", "All three series lost.", "p. 4")', '("「三场都输了」", "Все три серии проиграны.", "Страница 4")')
add("content7.py", '("「小局一场没赢」", "Not a single game won.", "p. 4")', '("「小局一场没赢」", "Ни одной выигранной игры.", "Страница 4")')
add("content7.py", '("「故事够不够好」", "But is the story good enough?", "p. 5")', '("「故事够不够好」", "А достаточно ли хороша история?", "Страница 5")')
add("content7.py", '("「别以后,就现在」", "Not later — now.", "p. 5")', '("「别以后,就现在」", "Не потом — сейчас.", "Страница 5")')
add("content7.py", "下期预告 · Next week (VOL.3)", "下期预告 · На следующей неделе (VOL.3)")
add("content7.py", 'instr="Fill in"', 'instr="Впишите"')

# ---- content8 P8 ----
add("content8.py", "测验与答案 · Test & keys", "测验与答案 · Тест и ответы")
add("content8.py", "第 8 版 · 本周大测验 + 全部答案 · This week's test and every answer key", "第 8 版 · 本周大测验 + 全部答案 · Большой тест недели и все ответы")
add("content8.py", "A · 判断对错 · True or false", "A · 判断对错 · Верно или неверно")
add("content8.py", "B · 本周大测验 · The big quiz", "B · 本周大测验 · Большой опрос")
add("content8.py", "C · 完成句子 · Complete", "C · 完成句子 · Закончите фразы")
add("content8.py", "D · 读一读,答一答 · Read & answer", "D · 读一读,答一答 · Читаем и отвечаем")
add("content8.py", "E · 情景说话 · In conversation", "E · 情景说话 · В разговоре")
add("content8.py", "F · 写一写 · Writing", "F · 写一写 · Письмо")
add("content8.py", "Start of Winter is on Nov 7.", "Начало зимы — 7 ноября.")
add("content8.py", "立冬 is the 19th solar term, not the 18th.", "lìdōng — 19-й солнечный термин, а не 18-й.")
add("content8.py", "Spot goods ship without a deposit wait.", "Товары со склада отправляются без ожидания задатка.")
add("content8.py", "AL lost all three of its Swiss-stage series.", "AL проиграла все три серии швейцарского этапа.")
add("content8.py", "Quarter-finals start at 06:00 Beijing time.", "Четвертьфиналы начинаются в 06:00 по пекинскому времени.")
add("content8.py", "The AI film has no live actors.", "В фильме ИИ нет живых актёров.")
add("content8.py", "The new film opens on Nov 7.", "Новый фильм выходит 7 ноября.")
add("content8.py", "Journalists' Day is on Nov 8, not Nov 7.", "День журналиста — 8 ноября, а не 7 ноября.")
add("content8.py", "Spot sales run until Nov 13.", "Продажи со склада идут до 13 ноября.")
add("content8.py", "The solar-term moment is 17:52.", "Момент солнечного термина — 17:52.")
add("content8.py", "First micro-season: water begins to freeze.", "Первый микросезон: вода начинает замерзать.")
add("content8.py", "IG beat HLE on Oct 26.", "IG обыграла HLE 26 октября.")
add("content8.py", "TES beat G2 on Oct 26.", "TES обыграла G2 26 октября.")
add("content8.py", "By noon on Oct 26, Maoyan showed about 1.192 million yuan.", "К полудню 26 октября Maoyan показывал около 1,192 миллиона юаней.")
add("content8.py", "Huang Yan is a crematory worker.", "Хуан Янь — работница крематория.")
add("content8.py", "The WeChat shop event runs 35 days.", "Акция магазина WeChat идёт 35 дней.")
add("content8.py", "Basket A pays 270 yuan after the cut.", "Корзина А платит 270 юаней после снижения.")
add("content8.py", "The final starts at 03:00 Beijing time on Nov 15.", "Финал начинается в 03:00 по пекинскому времени 15 ноября.")
add("content8.py", "zhíjiàng — the price itself drops.", "zhíjiàng — сама цена падает.")
add("content8.py", "Àilún — Allen, Texas, hosts the Swiss stage.", "Àilún — Аллен, штат Техас, принимает швейцарский этап.")
add("content8.py", "jiǎozǐ — northern families eat these at 立冬.", "jiǎozǐ — их едят северные семьи на lìdōng.")
add("content8.py", "shùzì — the AI film's characters are digital images.", "shùzì — персонажи фильма — цифровые изображения.")
add("content8.py", "piàofáng — box-office takings.", "piàofáng — кассовые сборы.")
add("content8.py", "jiésuàn — the checkout page shows the real price.", "jiésuàn — страница кассы показывает настоящую цену.")
add("content8.py", "bǔdōng — eating well before winter.", "bǔdōng — хорошо питаться перед зимой.")
add("content8.py", "jìzhě — a journalist interviews and writes news.", "jìzhě — журналист берёт интервью и пишет новости.")
add("content8.py", "lìjiǎn — taken off at checkout.", "lìjiǎn — вычитается на кассе.")
add("content8.py", "Xiao Hong lives in Beijing.", "Сяо Хун живёт в Пекине.")
add("content8.py", "On 立冬 she made dumplings with her mother.", "На lìdōng она лепила пельмени с мамой.")
add("content8.py", "She bought a scarf online.", "Она купила шарф онлайн.")
add("content8.py", "She phoned her grandmother on Sunday.", "В воскресенье она позвонила бабушке.")
add("content8.py", "Order: dumplings, then shopping, then the phone call.", "Порядок: пельмени, потом покупки, потом звонок.")
add("content8.py", "Spot goods ship right away, no pre-sale wait.", "Товары со склада отправляются сразу, без ожидания предпродажи.")
add("content8.py", "Northern families eat dumplings at 立冬.", "Северные семьи едят пельмени на lìdōng.")
add("content8.py", "Page 6's rule: data first, advertisement last.", "Правило страницы 6: сначала данные, реклама — последней.")
add("content8.py", 'f"Writing — there is no single right answer. A {NCHARS}-character model follows."', 'f"Письмо — единственно верного ответа нет. Ниже — образец из {NCHARS} иероглифов."')
add("content8.py", '"(开放题，范文如下)"', '"(открытый вопрос — образец ниже)"')
add("content8.py", 'f"Open task - the model answer is printed in section F above ({NCHARS} characters)"', 'f"Открытый вопрос — образец напечатан выше, в разделе F ({NCHARS} иероглифов)"')
add("content8.py", '"Model answer: "', '"Образец: "')
add("content8.py", "答案 · Answer keys — by page, with a note on every answer", "答案 · Ответы — по страницам, с примечанием к каждому ответу")
add("content8.py", "All notes in English · ✓ = the writing task", "Все примечания на русском · ✓ = письменное задание")
add("content8.py", 'f"— Page {pg} —"', 'f"— СТРАНИЦА {pg} —"')
add("content8.py", 'instr="Fill in"', 'instr="Впишите"')
add("content8.py", 'instr="Writing"', 'instr="Письмо"')

# ---- runner ----
def main():
    from collections import defaultdict
    by_file = defaultdict(list)
    for fn, old, new in PAIRS:
        by_file[fn].append((old, new))
    failed = []
    for fn, pairs in by_file.items():
        path = os.path.join(BUILD, fn)
        s = open(path, encoding="utf-8").read()
        orig = s
        for old, new in pairs:
            n = s.count(old)
            if n < 1:
                failed.append(f"{fn}: ZERO matches for {old[:80]!r}")
            else:
                print(f"{fn}: {n}x {old[:70]!r}")
            s = s.replace(old, new)
        if s != orig:
            open(path, "w", encoding="utf-8").write(s)
    if failed:
        print("TRANSFORM FAILED:")
        for f in failed:
            print("  " + f)
        sys.exit(1)
    print("TRANSFORM OK")

if __name__ == "__main__":
    main()
