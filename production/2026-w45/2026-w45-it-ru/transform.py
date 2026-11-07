# -*- coding: utf-8 -*-
"""IT x RU fan-out transform for W45 IT core build copy.
Rules: whole-string or exact-unique-literal replacements with count
assertions; value maps use bare text, never repr. Italian body text is
NEVER touched: every `old` below is a Chinese explanation-layer string,
a bilingual furniture string, or a printed instruction token.
Furniture follows the shipped W43 IT x RU string verbatim (badge inserted
at y=574, 22pt bold BRICK; footer VOL.2 per tables.py furniture ru pattern (FR x RU registry): Stranitsa N iz 8; gloss prefix Poiasnenie; P8
separators STRANITSA per the W43 IT x RU shipped precedent).
P7 word-box rule: the Italian definition sentence (wt) is byte-frozen;
only the German gloss note below it is localised.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
LOG = []


def rep(fname, old, new, expect=None):
    p = os.path.join(BASE, fname)
    s = open(p, encoding="utf-8").read()
    n = s.count(old)
    if expect is not None:
        assert n == expect, f"{fname}: {old!r} count {n} != {expect}"
    else:
        assert n >= 1, f"{fname}: {old!r} not found"
    LOG.append(f"{fname}: {n}x {old!r} -> {new!r}")
    open(p, "w", encoding="utf-8").write(s.replace(old, new))


def rep_if(fname, old, new):
    p = os.path.join(BASE, fname)
    if old in open(p, encoding="utf-8").read():
        rep(fname, old, new)


def pairs(fname, plist):
    for old, new in plist:
        rep(fname, old, new)


# ---------- OUT repoint (1 per content file + render) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w45-it-core", "weekly-report-w45-it-ru", 1)
rep("render.py", "weekly-report-w45-it-core", "weekly-report-w45-it-ru", 1)
rep("render.py", "La-Lucerna-VOL2.pdf", "La-Lucerna-VOL2-RU.pdf", 1)
rep("render.py", "La-Lucerna-VOL2-web.pdf", "La-Lucerna-VOL2-RU-web.pdf", 1)

# ---------- svglib docstring comment only (not rendered) ----------
rep("svglib.py", "for 重阳.", "for Double Ninth.", 1)

# ---------- bslib4: furniture + gloss prefix (W43 IT x DE shipped forms, VOL.2) ----------
rep("bslib4.py",
    '"La Lucerna · 意大利语周报 VOL.2 · LUCERNA ITALIAN WEEKLY"',
    '"La Lucerna · ИТАЛЬЯНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА ИТАЛЬЯНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Страница {n} из {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Пояснение — " + s', 1)

# ---------- shared printed instruction tokens (only where present) ----------
INSTR = [
    ('instr="填空"', 'instr="Вставьте"'),
    ('instr="造句"', 'instr="Составьте предложение"'),
    ('instr="翻译"', 'instr="Переведите"'),
    ('instr="判断"', 'instr="Верно или нет"'),
    ('instr="写作"', 'instr="Напишите"'),
    ('instr="把词和释义配对"', 'instr="Соедините пары"'),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Ответы — на странице 8 · уровни смешаны: ищите по номеру"),
    ("E TU? · 说说你自己", "E TU? · А ВЫ?"),
]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTR:
        rep_if(f, old, new)

# ================= content12 (P1 + P2) =================
pairs("content12.py", [
    ("OGNI SETTIMANA IN ITALIANO · 每周一期 · 读意大利人正在读的意大利语",
     "OGNI SETTIMANA IN ITALIANO · ИТАЛЬЯНСКИЙ, КОТОРЫЙ ЧИТАЮТ ИТАЛЬЯНЦЫ"),
    ("意 大 利 语 周 报 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A",
     "ИТАЛЬЯНСКИЙ · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A"),
    # band right + pairing badge (W43 shipped geometry: y=574, 22pt bold BRICK)
    ('p.text(RIGHT - 30, 478, "本周迎来第一场寒冷", 24, "sans", True, "#b3a06a", anchor="end")\n'
     'p.text(RIGHT - 30, 522, "初寒之周 · 详见第 2 版", 21, "sans", False, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 478, "НА ЭТОЙ НЕДЕЛЕ ПРИХОДИТ ПЕРВЫЙ ХОЛОД", 24, "sans", True, "#b3a06a", anchor="end")\n'
     'p.text(RIGHT - 30, 522, "Неделя первого холода · см. страницу 2", 21, "sans", False, "#b3a06a", anchor="end")\n'
     '\n'
     '# pairing badge (masthead area, below the band; W43 IT x RU string; W45 IT-family inserted geometry)\n'
     'p.text(975, 574, "ТЕКСТЫ НА ИТАЛЬЯНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", 22, "sans", True, BRICK, anchor="middle")'),
    ("LA NOTIZIA · 头条", "LA NOTIZIA · ГЛАВНАЯ НОВОСТЬ"),
    ("讲解｜il primo freddo 第一场寒冷 · il versante adriatico 亚得里亚海一侧 · la previsione 预报 · assaggi 品尝。",
     "Пояснение — il primo freddo = первый холод · il versante adriatico = адриатическая сторона · la previsione = прогноз · assaggi = дегустации."),
    ("LA SETTIMANA IN CIFRE · 数字看本周", "LA SETTIMANA IN CIFRE · В ЦИФРАХ"),
    ("（可能下初雪的海拔）", "(возможная граница снегопадов)"),
    ("（米兰文化论坛 50 多场活动）", "(более 50 мероприятий Forum Cultura)"),
    ("（参加米兰潘妮托尼决赛的国家数）", "(стран на финале Panettone в Милане)"),
    ("（本周末意甲第 11 轮）", "(11-й тур Серии А в выходные)"),
    ("ADESSO TU · 即学即练", "ADESSO TU · ТЕПЕРЬ ВЫ"),
    ("il primo freddo = 第一场寒冷", "il primo freddo = первый холод"),
    ("la prima neve leggera = 初雪", "la prima neve leggera = первый лёгкий снег"),
    ("文化论坛与潘妮托尼决赛都在米兰", "Forum Cultura и финал Panettone — оба в Милане"),
    ("克雷莫纳的节日叫 Festa del Torrone", "Праздник в Кремоне называется Festa del Torrone"),
    ("意甲第 11 轮周日收官", "11-й тур завершается в воскресенье"),
    ("previsioni = 预报（复数）", "previsioni = прогнозы (мн. ч.)"),
    ("本周日程 · Cosa succede, giorno per giorno", "План недели · Cosa succede, giorno per giorno"),
    ("日程以各活动日历为准，时间可能有变。", "Даты — по календарям мероприятий; время может измениться."),
    ("IN QUESTO NUMERO · 本期目录", "IN QUESTO NUMERO · ОБЗОР"),
    ("“第一场寒冷”：温和秋天后的第一波寒冷。", "«il primo freddo»: первый серьёзный холод после мягкой осени."),
    ("IN BREVE · 快讯", "IN BREVE · КОРОТКО"),
    ("QUIZ LAMPO · 闪电问答", "QUIZ LAMPO · БЛИЦ-ВИКТОРИНА"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Прочитайте первую страницу и выберите правильный ответ · Ответы на странице 8"),
    ("第一场寒冷在周一 11 月 2 日到来", "Первый холод приходит в понедельник, 2 ноября"),
    ("初雪在 1300–1500 米左右", "Первый снег выпадает на высоте 1300–1500 метров"),
    ("潘妮托尼决赛在米兰", "Финал Panettone — в Милане"),
    # P2
    ("VITA · 生活", "VITA · ЖИЗНЬ"),
    ("LIVELLO A2 · Il primo freddo e il 2 novembre · 初寒与追思日",
     "LIVELLO A2 · Il primo freddo e il 2 novembre · Первый холод и День поминовения"),
    ("发稿时表决结果尚未确认，详见第 6 版。", "На момент сдачи номера результат голосования ещё не подтверждён: см. страницу 6."),
    ("LA FRASE PER RICORDARE · 口诀", "LA FRASE PER RICORDARE · ПАМЯТКА"),
    ("il cappotto 大衣 · la sciarpa 围巾 · i guanti 手套 · a strati 分层穿衣 · il termosifone 暖气片 · il crisantemo 菊花",
     "il cappotto = пальто · la sciarpa = шарф · i guanti = перчатки · a strati = слоями · il termosifone = радиатор · il crisantemo = хризантема"),
    ("初寒来了你穿什么：大衣、围巾还是手套？写两句意大利语寄给编辑部。",
     "Что вы наденете, когда придёт первый холод: пальто, шарф или перчатки? Напишите два предложения по-итальянски!"),
    ("IL 2 NOVEMBRE · 追思日", "IL 2 NOVEMBRE · ДЕНЬ ПОМИНОВЕНИЯ"),
    ("ESERCIZI · 第 2 版练习", "ESERCIZI · УПРАЖНЕНИЯ СТРАНИЦЫ 2"),
    ("用意大利语补全句子。", "Дополните предложения по-итальянски."),
    ("cappotto = 大衣", "cappotto = пальто"),
    ("sciarpa = 围巾", "sciarpa = шарф"),
    ("guanti = 手套（复数）", "guanti = перчатки (мн. ч.)"),
    ("crisantemi = 菊花（复数）", "crisantemi = хризантемы (мн. ч.)"),
    ("termosifoni = 暖气片（复数）", "termosifoni = радиаторы (мн. ч.)"),
    ("补全动词的现在时形式。", "Дополните глаголы в настоящем времени."),
    ("fare freddo：fa freddo（天气）", "fare freddo: fa freddo (погода)"),
    ("mettere：io → metto", "mettere: io → metto"),
    ("portare：loro → portano", "portare: loro → portano"),
    ("guardare：loro → guardano", "guardare: loro → guardano"),
    ("restare：la scuola → resta（lei）", "restare: la scuola → resta (lei)"),
    ("读第 2 版文章，选出正确答案。", "Прочитайте статью на странице 2 и выберите правильный ответ."),
    ("11 月 2 日是追思日", "2 ноября — День поминовения"),
    ("追思日的花是菊花", "Цветок 2 ноября — хризантема"),
    ("分层穿衣：a strati", "Одеваться слоями: a strati"),
    ("诸圣节今年是周日、无连休", "День всех святых в этом году выпадает на воскресенье, без длинных выходных"),
    ("cappotto=御寒大衣 c", "cappotto = тёплое пальто, c"),
    ("sciarpa=围巾 d", "sciarpa = шарф, d"),
    ("crisantemo=十一月的花 a", "crisantemo = ноябрьский цветок, a"),
    ("termosifone=暖气片 b", "termosifone = радиатор, b"),
])
print("content12 done")

# ================= content34 (P3 + P4) =================
pairs("content34.py", [
    ("CULTURA · 文化", "CULTURA · КУЛЬТУРА"),
    ("A2 → B1 · Panettone, torrone e musei aperti · 甜点与博物馆",
     "A2 → B1 · Panettone, torrone e musei aperti · Сладости и открытые музеи"),
    ("il panettone 米兰圣诞面包 · il torrone 牛轧糖 · l'assaggio 品尝 · la bancarella 摊位 · il cantiere 施工现场/修复工地。",
     "il panettone = миланский рождественский кекс · il torrone = нуга · l'assaggio = дегустация · la bancarella = прилавок · il cantiere = стройплощадка"),
    ("你更喜欢传统潘妮托尼还是巧克力味的？写两句寄来。",
     "Традиционный или шоколадный? Напишите два предложения!"),
    ("ESERCIZI · 第 3 版练习", "ESERCIZI · УПРАЖНЕНИЯ СТРАНИЦЫ 3"),
    ("读第 3 版文章，选出正确答案。", "Прочитайте статью на странице 3 и выберите правильный ответ."),
    ("潘妮托尼决赛在米兰", "Финал Panettone — в Милане"),
    ("克雷莫纳牛轧糖节到 11 月 22 日", "Фестиваль Torrone в Кремоне идёт до 22 ноября"),
    ("潘妮托尼决赛有 19 国糕点师", "В финале Panettone участвуют кондитеры из 19 стран"),
    ("文化论坛 11 月 3 日周二开幕", "Forum Cultura открывается во вторник, 3 ноября"),
    ("阿尔巴松露节到 12 月 6 日", "Фестиваль трюфелей в Альбе идёт до 6 декабря"),
    ("用方框里的词填空。", "Дополните слова из рамки."),
    ("panettone = 米兰圣诞面包", "panettone = миланский рождественский кекс"),
    ("torrone = 牛轧糖", "torrone = нуга"),
    ("assaggio = 品尝", "assaggio = дегустация"),
    ("bancarella = 摊位", "bancarella = прилавок"),
    ("mandorle = 杏仁（复数）", "mandorle = миндаль (мн. ч.)"),
    ("tartufo = 松露", "tartufo = трюфель"),
    ("用 passato prossimo（近过去时）补全，注意助动词 avere / essere。",
     "Дополните passato prossimo. Внимание: вспомогательный глагол avere или essere."),
    ("arrivare 用 essere：è arrivato", "arrivare с essere: è arrivato"),
    ("assaggiare 用 avere：abbiamo assaggiato", "assaggiare с avere: abbiamo assaggiato"),
    ("andare 用 essere，复数 sono andati", "andare с essere, мн. ч.: sono andati"),
    ("aprire 用 avere：ha aperto", "aprire с avere: ha aperto"),
    ("把词组成正确的句子。", "Составьте из слов правильные предложения."),
    ("主语 + essere + 地点 + 日期", "Подлежащее + essere + место + дата"),
    ("地点在前，主语在后", "Сначала место, потом подлежащее"),
    ("dura fino a = 持续到", "dura fino a = длится до"),
    # P4
    ("SPORT · 体育", "SPORT · СПОРТ"),
    ("LIVELLO B1 · La Serie A e l'Europa · 意甲与欧战",
     "LIVELLO B1 · La Serie A e l'Europa · Серия А и Европа"),
    ("la giornata 轮次 · la presentazione 赛前介绍 · gli spalti 看台 · la sera 晚上。",
     "la giornata = тур · la presentazione = превью · gli spalti = трибуны · la sera = вечер"),
    ("周日晚上你看哪场比赛？写两句意大利语寄来。",
     "Какой матч вы посмотрите в воскресенье вечером? Напишите два предложения по-итальянски!"),
    ("LA SETTIMANA DEL CALCIO · 足球周", "LA SETTIMANA DEL CALCIO · ФУТБОЛЬНАЯ НЕДЕЛЯ"),
    ("ESERCIZI · 第 4 版练习", "ESERCIZI · УПРАЖНЕНИЯ СТРАНИЦЫ 4"),
    ("读第 4 版文章，选出正确答案。", "Прочитайте статью на странице 4 и выберите правильный ответ."),
    ("意甲第 11 轮周日收官", "11-й тур завершается в воскресенье"),
    ("周日晚上佛罗伦萨对尤文图斯", "В воскресенье вечером «Фиорентина» играет с «Ювентусом»"),
    ("欧战第 4 轮在 11 月 3–5 日", "4-й тур еврокубков — с 3 по 5 ноября"),
    ("欧战比赛只作前瞻、无结果", "Матчи еврокубков — только превью, без результатов"),
    ("国米对科莫在圣西罗", "«Интер» против «Комо» — на «Сан-Сиро»"),
    ("giornata=联赛的一轮 c", "giornata = тур, c"),
    ("presentazione=赛前介绍 b", "presentazione = превью, b"),
    ("spalti=看台 a", "spalti = трибуны, a"),
    ("sera=晚上 d", "sera = вечер, d"),
    ("用括号里词的比较级填空（数据看赛程表）。",
     "Дополните сравнительной степенью слова в скобках (см. расписание)."),
    ("周日晚上的比赛晚于周五的：più tardi", "Воскресные вечерние матчи позже пятничных: più tardi"),
    ("周五的比赛早于周日的：più presto", "Пятничные матчи раньше воскресных: più presto"),
    ("più + bella 周日晚最美（主观评价）", "più + bella: воскресный вечер самый красивый (субъективно)"),
    ("bene 的比较级是不规则的 meglio", "Сравнительная степень от bene — неправильная: meglio"),
    ("用 passato prossimo 补全。", "Дополните passato prossimo."),
    ("vincere：ha vinto", "vincere: ha vinto"),
    ("pareggiare：ha pareggiato", "pareggiare: ha pareggiato"),
    ("arrivare 用 essere，复数 sono arrivati", "arrivare с essere, мн. ч.: sono arrivati"),
    ("guardare 用 avere：abbiamo guardato", "guardare с avere: abbiamo guardato"),
    ("prendere 的分词是 preso：ha preso", "Причастие от prendere — preso: ha preso"),
])
print("content34 done")

# ================= content56 (P5 + P6) =================
pairs("content56.py", [
    ("GIOVANI · 青年", "GIOVANI · МОЛОДЁЖЬ"),
    ("LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · 卢卡之后",
     "LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · После Лукки"),
    ("（周二：米兰文化论坛开幕）", "(вторник: Forum Cultura открывается в Милане)"),
    ("（周三至周四：欧战直播）", "(среда–четверг: еврокубки по ТВ)"),
    ("（周五准备周末）", "(пятница: готовимся к выходным)"),
    ("（周六：米兰或克雷莫纳品尝）", "(суббота: дегустации в Милане или Кремоне)"),
    ("（周日：意甲与返程）", "(воскресенье: Серия А и возвращение домой)"),
    ("il cosplay 角色扮演服装 · gratuito 免费的 · il documentario 纪录片 · lo schermo 银幕。",
     "il cosplay = косплей-костюм · gratuito = бесплатный · il documentario = документальный фильм · lo schermo = экран"),
    ("卢卡之后你去哪：文化论坛、电影还是美食节？写两句寄来。",
     "После Лукки: Forum Cultura, кино или сагре? Напишите два предложения!"),
    ("ESERCIZI · 第 5 版练习", "ESERCIZI · УПРАЖНЕНИЯ СТРАНИЦЫ 5"),
    ("读第 5 版文章，选出正确答案。", "Прочитайте статью на странице 5 и выберите правильный ответ."),
    ("卢卡漫画节是第 60 届", "Lucca Comics — 60-й выпуск"),
    ("文化论坛 11 月 3 日开幕", "Forum Cultura открывается 3 ноября"),
    ("民俗电影节在佛罗伦萨", "Festival dei Popoli — во Флоренции"),
    ("文化论坛有 50 多场活动", "У Forum Cultura более 50 мероприятий"),
    ("卢卡漫画节主题是 Legacy", "Тема Lucca Comics — «Legacy»"),
    ("用方框里的词填空。注意：有的词要变成复数。",
     "Дополните слова из рамки. Внимание: некоторые слова — во множественном числе."),
    ("armadio = 衣柜", "armadio = шкаф"),
    ("gratuiti = 免费的（阳性复数）", "gratuiti = бесплатные (муж. р., мн. ч.)"),
    ("documentario = 纪录片", "documentario = документальный фильм"),
    ("schermo = 银幕", "schermo = экран"),
    ("castagne arrosto 烤栗子（复数）", "castagne arrosto = жареные каштаны (мн. ч.)"),
    ("cosplay = 角色扮演服装", "cosplay = косплей-костюм"),
    ("用将来时（futuro semplice）补全。", "Дополните futuro semplice (будущее время)."),
    ("andare 将来时 noi：andremo", "andare, будущее время, noi: andremo"),
    ("esserci 将来时：ci sarà（将有）", "esserci, будущее время: ci sarà (будет)"),
    ("guardare 将来时 noi：guarderemo", "guardare, будущее время, noi: guarderemo"),
    ("durare 将来时：durerà", "durare, будущее время: durerà"),
    ("卢卡漫画节到 11 月 8 日才结束是错的", "Lucca Comics заканчивается не 8 ноября"),
    # P6
    ("APPROFONDIMENTO · 深读", "APPROFONDIMENTO · РАЗБОР"),
    ("LIVELLO B2 · Leggere le previsioni · 怎样读天气预报",
     "LIVELLO B2 · Leggere le previsioni · Как читать прогнозы"),
    ("发稿时 10 月 28 日表决结果尚未确认：本期只写预期日期、争议点和 DPB 数字，不写结果。",
     "На момент сдачи номера результат голосования 28 октября ещё не подтверждён: этот выпуск называет только ожидаемую дату, спорный вопрос и цифры DPB, но не результат."),
    ("la probabilità 概率 · la media 平均值 · il modello 模型/预报模式 · il bollettino 公报/预报 · aggiornare 更新。",
     "la probabilità = вероятность · la media = среднее значение · il modello = прогностическая модель · il bollettino = сводка погоды · aggiornare = обновлять"),
    ("LE MINIME DI ESEMPIO · 练习用示例最低温 (DATI INVENTATI PER L'ESERCIZIO)",
     "LE MINIME DI ESEMPIO · ПРИМЕРЫ МИНИМАЛЬНЫХ ТЕМПЕРАТУР (DATI INVENTATI PER L'ESERCIZIO)"),
    ("PROBABILITÀ · 概率", "PROBABILITÀ · ВЕРОЯТНОСТЬ"),
    ("ESERCIZI · 第 6 版练习", "ESERCIZI · УПРАЖНЕНИЯ СТРАНИЦЫ 6"),
    ("看上面的练习图表，选出正确答案。", "Посмотрите на учебную диаграмму выше и выберите правильный ответ."),
    ("示例数据中最冷的是都灵 3°", "В примерных данных самый холодный — Турин, 3°"),
    ("示例数据中最暖的是那不勒斯 12°", "В примерных данных самый тёплый — Неаполь, 12°"),
    ("图表数据是练习用的、不是真实预报", "Данные диаграммы — учебные, а не настоящие прогнозы"),
    ("高概率不等于确定", "Высокая вероятность — ещё не уверенность"),
    ("预报基于 ECMWF 等模型", "Прогнозы основаны на моделях, например ECMWF"),
    ("预报会变，因为大气变化快", "Прогнозы меняются, потому что атмосфера быстро меняется"),
    ("DPB 于 10 月 15 日送布鲁塞尔", "DPB был отправлен в Брюссель 15 октября"),
    ("2027 增长预测 +0,8%", "Прогноз роста на 2027 год: +0,8 %"),
    ("è probabile che + 虚拟式 piova", "è probabile che + сослагательное наклонение: piova"),
    ("è possibile che + 虚拟式 nevichi", "è possibile che + сослагательное наклонение: nevichi"),
    ("bisogna che + 虚拟式 controllino", "bisogna che + сослагательное наклонение: controllino"),
    ("è importante che + 虚拟式 sia", "è importante che + сослагательное наклонение: sia"),
    ("用方框里的词填空：probabilità · media · bollettino · modello",
     "Дополните слова из рамки: probabilità · media · bollettino · modello"),
    ("probabilità = 概率", "probabilità = вероятность"),
    ("media = 平均值", "media = среднее значение"),
    ("bollettino = 预报公报", "bollettino = сводка погоды"),
    ("modello = 预报模型", "modello = прогностическая модель"),
])
print("content56 done")

# ================= content7 (P7) =================
# NOTE: wt (the Italian definition sentence of LA PAROLA) is NOT in this
# list on purpose: it stays byte-identical. Only its German gloss note
# below is localised.
pairs("content7.py", [
    ("LINGUA · 语言", "LINGUA · ЯЗЫК"),
    ("聚焦语言 · Tre livelli, tre strumenti · 三个级别，三件工具",
     "Язык в фокусе · Tre livelli, tre strumenti · Три уровня, три инструмента"),
    ("天气用无人称动词（第三人称单数）；“我冷”说 ho freddo，“外面冷”说 fa freddo。",
     "Погода — безличными глаголами (3-е лицо единственного числа): «мне холодно» — ho freddo, «на улице холодно» — fa freddo."),
    ("piovere 天气动词：piove", "piovere, глагол погоды: piove"),
    ("fa freddo = 天气冷", "fa freddo = холодно (погода)"),
    ("nevicare：nevica", "nevicare: nevica"),
    ("“我冷”说 ho freddo", "«Мне холодно» — ho freddo"),
    ("讲过去用近过去时：arrivare/andare 等用 essere，分词配合性数；avere 的分词不变。",
     "Прошедшее время — passato prossimo: arrivare/andare и др. с essere, причастие согласуется в роде и числе; с avere причастие не меняется."),
    ("arrivare 用 essere：è arrivato", "arrivare с essere: è arrivato"),
    ("assaggiare 用 avere", "assaggiare с avere"),
    ("andare 用 essere，复数 sono andati", "andare с essere, мн. ч.: sono andati"),
    ("aprire 用 avere + 不变分词", "aprire с avere + неизменяемое причастие"),
    ("è probabile che / è possibile che / bisogna che 后用虚拟式；so che、scrivono che 后用陈述式。",
     "После è probabile che / è possibile che / bisogna che — сослагательное наклонение; после so che / scrivono che — изъявительное."),
    ("è probabile che + 虚拟式 piova", "è probabile che + сослагательное наклонение: piova"),
    ("è possibile che + 虚拟式 nevichi", "è possibile che + сослагательное наклонение: nevichi"),
    ("bisogna che + 虚拟式 sia", "bisogna che + сослагательное наклонение: sia"),
    ("so che + 陈述式 arriva", "so che + изъявительное наклонение: arriva"),
    ("ERRORI TIPICI · 常见错误", "ERRORI TIPICI · ОШИБКИ"),
    ("fa 后面的 freddo 永远不变。", "После fa слово freddo не меняется."),
    ("nevicare 只用第三人称单数。", "nevicare: только 3-е лицо единственного числа."),
    ("预报给的是概率，不是确定性。", "Вероятность, а не уверенность."),
    ("gente 是单数，动词形容词用单数阴性。", "gente — единственное число (женский род)."),
    ("LA PAROLA · 本周生词", "LA PAROLA · СЛОВО НЕДЕЛИ"),
    ("assaggio = 品尝。本周见第 3 版：潘妮托尼决赛上观众可以免费品尝。",
     "assaggio = дегустация. См. страницу 3."),
    # readers' corner: Italian letter text (lt) untouched; German note covers
    # all three disclosure facts + imperative invitation with VOL.3 promise.
    # Line-counted (3 lines at 20pt, same as the Chinese note) so col3 still
    # ends at the core's 1673, 13 px clear of the FRASI rule.
    ("这是编辑部示例信，非真实来信。来信请寄编辑部，VOL.3 刊登真实来信与第 8 版最佳作文！",
     "Esempio della redazione, non posta vera, nessun miglior testo di pagina 8. / Пример редакции, а не настоящие письма; лучшего сочинения со страницы 8 нет. Напишите нам — лучшие появятся в VOL.3!"),
    ("FRASI DELLA SETTIMANA · 本周金句（逐字摘自本期文章）",
     "FRASI DELLA SETTIMANA · ФРАЗЫ НЕДЕЛИ (дословно из статей выпуска)"),
    ("第一场真正的寒冷到来了。", "Пришло первое настоящее похолодание сезона."),
    ("这不是确定性，而是概率。", "Это не уверенность, а вероятность."),
    ("11 月 2 日是追思日。", "2 ноября — День поминовения."),
    ("天冷，穿暖和点！", "Холодно, оденься теплее!"),
    ("观众可以免费品尝。", "Публика может дегустировать бесплатно."),
    ("足球不会因为第一场寒冷而停下。", "Футбол не останавливается из-за первого холода."),
    ("文化继续。", "Культура продолжается."),
    ("高概率不等于确定性。", "Высокая вероятность — ещё не уверенность."),
    ("LA PROSSIMA SETTIMANA · 下期预告 (VOL.3)", "LA PROSSIMA SETTIMANA · В СЛЕДУЮЩЕМ ВЫПУСКЕ (VOL.3)"),
])
print("content7 done")

# ================= content8 (P8) =================
pairs("content8.py", [
    ("VALUTAZIONE E RISPOSTE · 练习与答案", "VALUTAZIONE E RISPOSTE · ПРОВЕРКА И ОТВЕТЫ"),
    ("第 8 版 · La grande prova della settimana + tutte le risposte",
     "Страница 8 · La grande prova della settimana + tutte le risposte"),
    ("primo freddo = 第一场寒冷", "primo freddo = первый холод"),
    ("追思日在 11 月 2 日", "День поминовения — 2 ноября"),
    ("文化论坛在米兰开幕", "Forum Cultura открывается в Милане"),
    ("潘妮托尼决赛在周六日", "Финал Panettone — в субботу и воскресенье"),
    ("牛轧糖节在克雷莫纳", "Фестиваль Torrone — в Кремоне"),
    ("意甲第 11 轮周日收官：chiude", "11-й тур завершается в воскресенье: chiude"),
    ("佛罗伦萨对尤文图斯在周日晚上", "«Фиорентина» против «Ювентуса» в воскресенье вечером"),
    ("民俗电影节在佛罗伦萨", "Festival dei Popoli — во Флоренции"),
    ("初雪在 1300–1500 米左右", "Первый снег выпадает на высоте 1300–1500 метров"),
    ("追思日的花是菊花", "Цветок 2 ноября — хризантема"),
    ("潘妮托尼决赛有 19 国糕点师", "В финале Panettone участвуют кондитеры из 19 стран"),
    ("文化论坛有 50 多场活动", "У Forum Cultura более 50 мероприятий"),
    ("阿尔巴松露节到 12 月 6 日", "Фестиваль трюфелей в Альбе идёт до 6 декабря"),
    ("DPB 于 10 月 15 日送出", "DPB был отправлен 15 октября"),
    ("概率不等于确定", "Вероятность — ещё не уверенность"),
    ("卢卡漫画节 11 月 1 日闭幕", "Lucca Comics заканчивается 1 ноября"),
    ("Giulia 去米兰潘妮托尼决赛", "Джулия едет на финал Panettone в Милан"),
    ("Paolo 周六去牛轧糖节", "Паоло едет в субботу на фестиваль Torrone"),
    ("传统潘妮托尼是 Giulia 品尝的", "Традиционный Panettone пробует Джулия"),
    ("标题概括两个城市、两个节日", "Заголовок объединяет два города и два праздника"),
    ("时间词在前", "Сначала указание времени"),
    ("主语 + essere + 地点 + 日期", "Подлежащее + essere + место + дата"),
    ("疑问词组在句首", "Вопросительная формула в начале"),
    ("主语 + 动词 + 时间", "Подлежащее + глагол + указание времени"),
    # E · translation items re-aimed Italian -> German (W43 precedent):
    # Chinese keys become German keys; the one Italian-key item keeps its
    # Italian key and its body becomes German.
    ("周一第一场寒冷来了。", "В понедельник приходит первый холод."),
    ("对照原文", "См. оригинал"),
    ("观众可以免费品尝。", "Публика может дегустировать бесплатно."),
    ("assaggiare gratis = 免费品尝", "assaggiare gratis = дегустировать бесплатно"),
    ("周日晚上，佛罗伦萨对尤文图斯。", "В воскресенье вечером «Фиорентина» играет с «Ювентусом»."),
    ("si gioca = 进行比赛", "si gioca = играют"),
    ("dovere = 必须", "dovere = должен, нужно"),
    ("每个预报都必须清楚。→ ___", "Каждый прогноз должен быть понятным. → ___"),
    ("probabilità=可能性 d", "probabilità = вероятность, d"),
    ("media=平均值 a", "media = среднее значение, a"),
    ("bollettino=预报公报 b", "bollettino = сводка погоды, b"),
    ("modello=预报模型 c", "modello = прогностическая модель, c"),
    ("torrone = 牛轧糖", "torrone = нуга"),
    ("mandorle 杏仁", "mandorle = миндаль"),
    ("quanto costa? 多少钱", "quanto costa? = сколько стоит?"),
    ("pagare con carta 刷卡", "pagare con carta = платить картой"),
    ("牛轧糖节持续到 11 月 22 日", "Фестиваль Torrone идёт до 22 ноября"),
    ("写作题（无唯一答案）；范文（{NWORDS} 词）见下。",
     "Письменное задание (без единственного ответа); образец текста ({NWORDS} слов) ниже."),
    ("（开放题，范文如下）", "(открытое задание — образец ниже)"),
    ("范文见本版 H 区（{NWORDS} 词）", "Образец — в разделе H этой страницы ({NWORDS} слов)"),
    ("RISPOSTE · 参考答案 — 按版面分页排列，找到题号即可",
     "RISPOSTE · ОТВЕТЫ — по страницам: ищите по номеру задачи"),
    ("每题附一句中文简析 · 带 ✓ 的为范文题", "К каждой задаче — пояснение · ✓ — задание с образцом"),
])
print("content8 done")

# ---------- RU furniture extras (W43 IT x RU shipped forms) ----------
rep("content8.py", "— PAGINA {pg} —", "— СТРАНИЦА {pg} —", 1)
for _old, _new in [("Pagina 1", "Страница 1"), ("Pagina 2", "Страница 2"),
                   ("Pagina 3", "Страница 3"), ("Pagina 4", "Страница 4"),
                   ("Pagina 5", "Страница 5"), ("Pagina 6", "Страница 6")]:
    rep("content7.py", _old, _new)

# ---------- final audit: no CJK left except registry type tokens ----------
# Type tokens (完成句子/单选/完形单选/词汇配对/句型转换/判断对错/造句/翻译/写作)
# are registry-only: never printed (W43 IT x DE precedent keeps them, so the
# registry diff stays item-identical). Any other CJK is a missed string.
import re as _re
TYPE_TOKENS = {"完成句子", "单选", "完形单选", "词汇配对", "句型转换", "判断对错", "造句", "翻译", "写作"}
leftover = []
for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py", "svglib.py", "render.py", "run.py"]:
    txt = open(os.path.join(BASE, fn), encoding="utf-8").read()
    for run in sorted(set(_re.findall(r"[\u4e00-\u9fff]+", txt))):
        if run not in TYPE_TOKENS:
            leftover.append((fn, run))
assert not leftover, f"CJK leftover in build sources: {leftover}"
print(f"TOTAL replacements: {len(LOG)}")
for line in LOG:
    print(" ", line)
print("CJK audit: only registry type tokens remain (never printed)")


# ================= FIX ROUND 1 (RU) — from R0 render + audit =================
# R0 defects: (a) P1-headline flow overflow (bridge 4 lines vs core 3;
# cifre 13 lines vs core 11) -> shorten bridge to 3 lines, cifre items
# to 3/3/2/2 lines; cifre title, settimana subtitle and footnote fixes
# for BOXTITLE/EDGE flags. (b) P2 frase box title crossed its box border
# by 22.8 px at 23pt -> tsize 21 for this box only (title text unchanged).
# (c) P7 col3 ended 1790 vs FRASI rule 1686 (bilingual letter note 6
# lines) -> per coordinator clarification 2026-10-27 the disclosure is
# Russian-only (core has no Italian disclosure sentence to keep; the
# Italian letter + (esempio della redazione) label + preview promise
# stay frozen): Russian note 3 lines; parola gloss to 1 line; errori
# notes 2 and 4 to 1 line each. (d) P8-keys flow overflow: 19 answers
# wrapped to 2 lines -> telegraphic note/key shortenings below, each
# verified 1 line at 13pt serif / 434 px before applying (S = soggetto
# abbreviation in 44/134; 139 uses воскр./веч. abbreviations; 138 note
# glosses gratis, the key's verb covers assaggiare).
def rep2(fname, old, new):
    pp = os.path.join(BASE, fname)
    ss = open(pp, encoding="utf-8").read()
    nn = ss.count(old)
    assert nn >= 1, f"FIX1 {fname}: {old!r} not found"
    open(pp, "w", encoding="utf-8").write(ss.replace(old, new))
    print(f"FIX1 {fname}: {nn}x {old!r} -> {new!r}")


rep2("content12.py",
     "Пояснение — il primo freddo = первый холод · il versante adriatico = адриатическая сторона · la previsione = прогноз · assaggi = дегустации.",
     "Пояснение — primo freddo = первый холод · versante adriatico = Адриатика · previsione = прогноз · assaggi = пробы.")
rep2("content12.py", "(возможная граница снегопадов)", "(граница снегопадов)")
rep2("content12.py", "(стран на финале Panettone в Милане)", "(стран-участниц)")
rep2("content12.py", "(11-й тур Серии А в выходные)", "(11-й тур Серии А)")
rep2("content12.py", "LA SETTIMANA IN CIFRE · В ЦИФРАХ", "LA SETTIMANA IN CIFRE · ЦИФРЫ")
rep2("content12.py", "План недели · Cosa succede, giorno per giorno", "План недели · Giorno per giorno")
rep2("content12.py",
     'p.text(gx + 22, byy + 76, "Даты — по календарям мероприятий; время может измениться.", 16.5, "sans", False, GREY)',
     'p.text(gx + 22, byy + 76, "Даты — по календарям мероприятий;", 16.5, "sans", False, GREY)\n'
     'p.text(gx + 22, byy + 102, "время может измениться.", 16.5, "sans", False, GREY)')
rep2("content12.py",
     'vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),\n])',
     'vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),\n], tsize=21)')
rep2("content12.py",
     "День всех святых в этом году выпадает на воскресенье, без длинных выходных",
     "День всех святых: воскресенье, без длинных выходных")
rep2("content34.py", "Подлежащее + essere + место + дата", "S + essere + место + дата")
rep2("content34.py", "Сначала место, потом подлежащее", "Место, потом подлежащее")
rep2("content34.py", "В воскресенье вечером «Фиорентина» играет с «Ювентусом»", "В воскресенье вечером «Фиорентина» — «Ювентус»")
rep2("content34.py", "Воскресные вечерние матчи позже пятничных: più tardi", "Воскресные матчи позже пятничных: più tardi")
rep2("content34.py", "Пятничные матчи раньше воскресных: più presto", "Пятничные раньше воскресных: più presto")
rep2("content34.py", "più + bella: воскресный вечер самый красивый (субъективно)", "più + bella: воскресный вечер красивее всех")
rep2("content34.py", "Сравнительная степень от bene — неправильная: meglio", "Сравн. степень от bene — неправильная: meglio")
rep2("content56.py", "Данные диаграммы — учебные, а не настоящие прогнозы", "Данные диаграммы — учебные, не прогнозы")
rep2("content56.py", "Прогнозы меняются, потому что атмосфера быстро меняется", "Прогнозы меняются: атмосфера меняется быстро")
rep2("content56.py", "è possibile che + сослагательное наклонение: nevichi", "è possibile che + сослагат. наклонение: nevichi")
rep2("content56.py", "bisogna che + сослагательное наклонение: controllino", "bisogna che + сослагат. наклонение: controllino")
rep2("content7.py", "è possibile che + сослагательное наклонение: nevichi", "è possibile che + сослагат. наклонение: nevichi")
rep2("content7.py",
     "Esempio della redazione, non posta vera, nessun miglior testo di pagina 8. / Пример редакции, а не настоящие письма; лучшего сочинения со страницы 8 нет. Напишите нам — лучшие появятся в VOL.3!",
     "Пример редакции, а не настоящие письма; лучшего текста со страницы 8 нет. Напишите нам — лучшие в VOL.3!")
rep2("content7.py", "assaggio = дегустация. См. страницу 3.", "assaggio = дегустация (стр. 3).")
rep2("content7.py", "nevicare: только 3-е лицо единственного числа.", "nevicare: только 3-е лицо ед. ч.")
rep2("content7.py", "gente — единственное число (женский род).", "gente — ед. число (жен. род).")
rep2("content8.py", "«Фиорентина» против «Ювентуса» в воскресенье вечером", "«Фиорентина» — «Ювентус» в воскресенье вечером")
rep2("content8.py", "Подлежащее + essere + место + дата", "S + essere + место + дата")
rep2("content8.py", "Вопросительная формула в начале", "Формула вопроса в начале")
rep2("content8.py", "Подлежащее + глагол + указание времени", "Подлежащее + глагол + время")
rep2("content8.py", "Публика может дегустировать бесплатно.", "Публика может пробовать бесплатно.")
rep2("content8.py", "assaggiare gratis = дегустировать бесплатно", "gratis = бесплатно")
rep2("content8.py", "В воскресенье вечером «Фиорентина» играет с «Ювентусом».", "«Фиорентина» — «Ювентус» в воскр. веч.")
rep2("content8.py", "Образец — в разделе H этой страницы ({NWORDS} слов)", "Образец — в разделе H этой страницы ({NWORDS} слово)")
print("FIX ROUND 1 done")

# ================= FIX ROUND 2 (RU) — from R1 occlusion audit (2 NEW flags) =================
# (a) P1 parola note wrapped to 2 lines, its 2nd line ink crossed the
# row-B rule at y=1864 (core note is 1 line at baseline 1846.3) ->
# Russian note shortened to 1 line (headword itself carries "primo").
# (b) P7 parola gloss ink bottom exceeded its box border by 1.1 px
# (box-height formula underestimates the 1-line gloss descent) -> box
# height +2 px (trailing pad 20 -> 22); letter box shifts +2 px, col3
# still ends well clear of the FRASI rule.
rep2("content12.py",
     "«il primo freddo»: первый серьёзный холод после мягкой осени.",
     "«il primo freddo»: холод после мягкой осени.")
rep2("content7.py",
     'wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("assaggio = дегустация (стр. 3).", "sans", False, 20, CW - 44)) * 29 + 20',
     'wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("assaggio = дегустация (стр. 3).", "sans", False, 20, CW - 44)) * 29 + 22')
print("FIX ROUND 2 done")
