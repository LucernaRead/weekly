# -*- coding: utf-8 -*-
"""DE x RU fan-out transform for W45 DE core build copy.
Rules: whole-line or exact-unique-literal replacements with count
assertions; value maps use bare text, never repr.
German body text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token. Furniture strings are verbatim from the shipped
W43 DE x RU edition (VOL.1 -> VOL.2 here). Run once from the build dir copy.
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

def rep_all(fname, pairs):
    for old, new in pairs:
        rep(fname, old, new)

# ---------- OUT repoint (1 per content file) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w45-de-core", "weekly-report-w45-de-ru", 1)

# ---------- svglib docstring comment only (not rendered) ----------
rep("svglib.py", "for 重阳.", "for the Double Ninth festival.", 1)

# ---------- bslib4: furniture + gloss prefix (W43 DE x RU shipped forms, VOL.2) ----------
rep("bslib4.py",
    '"Die Lucerna · 德语周报 VOL.2 · LUCERNA GERMAN WEEKLY"',
    '"Die Lucerna · НЕМЕЦКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА НЕМЕЦКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Страница {n} из {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Пояснение — " + s', 1)

# ---------- shared furniture strings ----------
SHARED = [
    ("UND SIE? · 说说你自己", "UND SIE? · А вы?"),
    ("FERIENWECHSEL · 假期交接", "FERIENWECHSEL · Каникулы"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Ответы на стр. 8 · уровни перемешаны — ищите по номеру"),
    ("BEISPIELE · 例句", "BEISPIELE · Примеры"),
]
for f in ["content12.py", "content34.py", "content56.py"]:
    for old, new in SHARED:
        p = os.path.join(BASE, f)
        if old in open(p, encoding="utf-8").read():
            rep(f, old, new)

# ================= content12 (P1 + P2) =================
C12 = [
    ("WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语",
     "WÖCHENTLICH AUF DEUTSCH · КАЖДУЮ НЕДЕЛЮ · НЕМЕЦКИЙ, КОТОРЫЙ ЧИТАЮТ НЕМЦЫ"),
    ("德 语 周 报 · VOL.2 · 足 球 周 · 油 价 · 护 理",
     "НЕМЕЦКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · ФУТБОЛ · ТОПЛИВО · УХОД"),
    # P1 subtitle slot -> W43 shipped badge, verbatim string, 20pt bold brick
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "ТЕКСТЫ НА НЕМЕЦКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", 20, "sans", True, BRICK, anchor="middle")'),
    ("本周足球周 · 欧冠欧联德甲连轴转", "Футбольная неделя · еврокубки и Бундеслига"),
    ("详见第 4 版 · Seite 4", "См. стр. 4 · Seite 4"),
    ("DIE TOPMELDUNG · 头条", "DIE TOPMELDUNG · Главная новость"),
    ("讲解｜die Englische Woche 一周双赛 · der Spieltag 比赛日 · empfangen 主场迎战 · die Bundesliga 德甲。",
     "Пояснение — die Englische Woche = англ. неделя · der Spieltag = тур · empfangen = принимать · die Bundesliga = Бундеслига."),
    ("DIE WOCHE IN ZAHLEN · 数字看本周", "DIE WOCHE IN ZAHLEN · Цифры"),
    ("9 — Spiele hat der 9. Spieltag der Bundesliga（德甲第 9 轮共 9 场比赛）",
     "9 — Spiele hat der 9. Spieltag der Bundesliga (9 матчей 9-го тура)"),
    ("6 — deutsche Teams spielen in Europa（6 支德国球队出战欧战）",
     "6 — deutsche Teams spielen in Europa (6 немецких команд играют в Европе)"),
    ("14,04 — Cent pro Liter beträgt der Tankrabatt（每升油减税 14.04 欧分）",
     "14,04 — Cent pro Liter beträgt der Tankrabatt (скидка 14,04 цента)"),
    ("JETZT ÜBEN · 即学即练", "JETZT ÜBEN · Сразу к делу"),
    ("一周双赛", "английская неделя"),
    ("多特主场迎战贝蒂斯", "«Дортмунд» принимает «Бетис»"),
    ("欧联在周四", "Лига Европы в четверг"),
    ("周五汉堡–门兴开轮", "«Гамбург»–«Гладбах» открывают в пятницу"),
    ("第 9 轮共 9 场", "9 матчей в 9-м туре"),
    ("减税到 12 月 31 日", "скидка до 31 декабря"),
    ("本周大问题 · Die Fragen der Woche", "Вопросы недели · Die Fragen der Woche"),
    ("德国本周最热议的五个问题。", "Пять главных вопросов недели."),
    ("IN DIESER AUSGABE · 本期目录", "IN DIESER AUSGABE · В выпуске"),
    ("油价减税（加油折扣）。详见第 2 版。", "Скидка на топливо. Подробнее на стр. 2."),
    ("KURZ & GUT · 快讯", "KURZ & GUT · Коротко"),
    ("BLITZQUIZ · 闪电问答", "BLITZQUIZ · Блиц-викторина"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Прочитайте стр. 1 и выберите правильный ответ · Ответы на стр. 8"),
    ("拜仁周二客战马竞", "«Бавария» во вторник в гостях у «Атлетико»"),
    ("霍芬海姆欧联客战水晶宫", "«Хоффенхайм» в Лиге Европы у «Кристал Пэлас»"),
    # P2
    ("LEBEN · 生活", "LEBEN · Жизнь"),
    ("LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · 油价、电力税与护理",
     "LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · Топливо, налог на электричество и уход"),
    ("der Tankrabatt 油价减税 · die Zapfsäule 加油机 · die Energiesteuer 能源税 · die Mehrwertsteuer 增值税 · der Angehörige 亲属。",
     "der Tankrabatt = скидка на топливо · die Zapfsäule = бензоколонка · die Energiesteuer = налог на энергию · die Mehrwertsteuer = НДС · der Angehörige = родственник."),
    ("AN DER ZAPFSÄULE · 加油机旁", "AN DER ZAPFSÄULE · У колонки"),
    ("你开车吗？你那里的油价是多少？写两句德语寄来。",
     "Вы водите машину? Сколько стоит литр бензина? Напишите нам!"),
    ("ZEW IN KÜRZE · ZEW 指数简讯", "ZEW IN KÜRZE · ZEW коротко"),
    ("RECHNEN WIR MAL · 算一算", "RECHNEN WIR MAL · Посчитаем"),
    ("Die Zahlen der Woche · 本周数字", "Die Zahlen der Woche · Цифры недели"),
    ("注意：减的是税，定价的是油站。出发前比比价。",
     "Внимание: налог снижен, а цену назначает заправка. Сравните цены, прежде чем заправляться."),
    ("ÜBUNGEN · 第 2 版练习", "ÜBUNGEN · Упражнения, стр. 2"),
    ("看第 2 版文章，用数字填空。", "Посмотрите на статью на стр. 2 и вставьте числа."),
    ("每升减税 14.04 欧分", "снижение на 14,04 цента за литр"),
    ("50 升省约 8.35 欧元", "50 литров — экономия около 8,35 евро"),
    ("减税到 2026 年底", "скидка до конца 2026 года"),
    ("国家少收约 25 亿欧元", "государство недополучит около 2,5 млрд евро"),
    ("加油机旁的实际降幅", "на колонке — реальное снижение"),
    ("改成 Perfekt 现在完成时。", "Перепишите в перфект."),
    ("beschließen → beschlossen", "beschließen → beschlossen"),
    ("fallen 用 sein", "fallen с sein"),
    ("tanken → getankt", "tanken → getankt"),
    ("weitergeben 可分动词", "weitergeben — отделяемый глагол"),
    ("ZEW 预期下降", "ожидания ZEW упали"),
    ("读第 2 版文章，选出正确答案。", "Прочитайте статью на стр. 2 и выберите правильный ответ."),
    ("减的是能源税", "снижен налог на энергию"),
    ("油站定价", "цену назначает заправка"),
    ("联盟党与社民党", "«Союз» и СДПГ"),
    ("家属居家护理", "родные ухаживают дома"),
    ("Tankrabatt=油价减税 b", "Tankrabatt=скидка на топливо b"),
    ("Zapfsäule=加油机 d", "Zapfsäule=бензоколонка d"),
    ("Mehrwertsteuer=增值税 a", "Mehrwertsteuer=НДС a"),
    ("Angehörige=亲属 c", "Angehörige=родственник c"),
]
rep_all("content12.py", C12)

# ================= content34 (P3 + P4) =================
C34 = [
    ("KULTUR · 文化", "KULTUR · Культура"),
    ("A2 → B1 · Ferienwechsel & Herbst · 假期交接与秋天",
     "A2 → B1 · Ferienwechsel & Herbst · Каникулы и осень"),
    ("der Ferienwechsel 假期交接 · die Schülerin 女学生 · der Ausflug 短途出游 · der Advent 将临期 · die Lesung 朗读会。",
     "der Ferienwechsel = смена каникул · die Schülerin = школьница · der Ausflug = вылазка · der Advent = адвент · die Lesung = чтения."),
    ("der Nebel — 雾", "der Nebel — туман"),
    ("das Laub — 落叶", "das Laub — листва"),
    ("der Kürbis — 南瓜", "der Kürbis — тыква"),
    ("die Kerze — 蜡烛", "die Kerze — свеча"),
    ("der Spaziergang — 散步", "der Spaziergang — прогулка"),
    ("die Lesung — 朗读会", "die Lesung — чтения"),
    ("HERBSTWÖRTER · 秋天词汇", "HERBSTWÖRTER · Осень"),
    ("秋天你比夏天读得多吗？你的床头现在放着哪本书？写两句德语寄来。",
     "Осенью читаете больше? Какая книга на тумбочке? Напишите нам!"),
    ("DER TIPP · 编辑部建议", "DER TIPP · Совет редакции"),
    ("ÜBUNGEN · 第 3 版练习", "ÜBUNGEN · Упражнения, стр. 3"),
    ("读第 3 版文章，判断对错。", "Прочитайте статью на стр. 3 и решите: верно или неверно."),
    ("BW 周一起复课", "в Баден-Вюртемберге учёба возобновилась в понедельник"),
    ("巴伐利亚本周仍在放假", "в Баварии на этой неделе ещё каникулы"),
    ("诸圣节 11 月 1 日", "День всех святых — 1 ноября"),
    ("10 月 31 日也是宗教改革日（九个州）", "31 октября — и День Реформации (девять земель)"),
    ("诸圣节商店关门", "в День всех святых магазины закрыты"),
    ("用方框里的词填空。", "Вставьте слова из рамки."),
    ("假期交接", "смена каникул"),
    ("去山区短途出游", "вылазка в горы"),
    ("图书馆的朗读会", "чтения в библиотеке"),
    ("将临期在 11 月筹划", "адвент планируют в ноябре"),
    ("湖面上的雾", "туман над озером"),
    ("BW 假期已结束", "в Баден-Вюртемберге каникулы закончились"),
    ("安静的节日", "тихий праздник"),
    ("诸圣节扫墓", "в День всех святых посещают могилы"),
    ("白天短所以夜晚长", "дни короткие, поэтому вечера длинные"),
    ("把词组成正确的句子。", "Составьте из слов правильные предложения."),
    ("时间地点开头，动词第二位", "время и место в начале, глагол на втором месте"),
    ("数量时间状语，动词第二位", "обстоятельство количества и времени, глагол на втором месте"),
    ("主谓宾顺序", "порядок подлежащее–сказуемое–дополнение"),
    ("bleiben + geschlossen", "bleiben + geschlossen"),
    # P4
    ("SPORT · 体育", "SPORT · Спорт"),
    ("LEVEL B1 · Europapokal & Bundesliga · 欧战与德甲",
     "LEVEL B1 · Europapokal & Bundesliga · Еврокубки и Бундеслига"),
    ("die Englische Woche 一周双赛 · auswärts 客场 · empfangen 主场迎战 · der Favorit 夺冠热门 · eröffnen 揭开序幕。",
     "die Englische Woche = английская неделя · auswärts = в гостях · empfangen = принимать дома · der Favorit = фаворит · eröffnen = открывать."),
    ("本周你支持谁？周六焦点战谁赢？写两句德语寄给编辑部。",
     "За кого вы болеете? Кто выиграет топ-матч? Напишите нам!"),
    ("DER 9. SPIELTAG · 第 9 轮赛程", "DER 9. SPIELTAG · 9-й тур"),
    ("ÜBUNGEN · 第 4 版练习", "ÜBUNGEN · Упражнения, стр. 4"),
    ("读第 4 版文章，选出正确答案。", "Прочитайте статью на стр. 4 и выберите правильный ответ."),
    ("拜仁周二客战马竞", "«Бавария» во вторник в гостях у «Атлетико»"),
    ("斯图加特 18:45 开球", "«Штутгарт» начинает в 18:45"),
    ("多特主场迎战贝蒂斯", "«Дортмунд» принимает «Бетис»"),
    ("霍芬海姆欧联客战水晶宫", "«Хоффенхайм» в Лиге Европы у «Кристал Пэлас»"),
    ("周六焦点战斯图加特–不来梅", "субботний топ-матч «Штутгарт»–«Вердер»"),
    ("Englische Woche=一周双赛 a", "Englische Woche=английская неделя a"),
    ("auswärts=客场 b", "auswärts=в гостях b"),
    ("Favorit=热门 c", "Favorit=фаворит c"),
    ("eröffnen=揭开序幕 d", "eröffnen=открывать d"),
    ("用比较级完成句子（括号里是原级）。", "Дополните предложения сравнительной степенью (в скобках — исходная форма)."),
    ("schwer → schwerer", "schwer → schwerer"),
    ("spät → später（19:30 最晚）", "spät → später (19:30 — позже всех)"),
    ("viel → mehr（球迷想要更多）", "viel → mehr (болельщики хотят больше)"),
    ("früh → früher（18:45 早于 21:00）", "früh → früher (18:45 раньше, чем 21:00)"),
    ("看上面的赛程表，选出正确答案。", "Посмотрите на таблицу тура выше и выберите правильный ответ."),
    ("汉堡–门兴周五 20:30", "«Гамбург»–«Гладбах» в пятницу в 20:30"),
    ("斯图加特–不来梅周六 18:30", "«Штутгарт»–«Вердер» в субботу в 18:30"),
    ("霍芬海姆–沙尔克周日 19:30", "«Хоффенхайм»–«Шальке» в воскресенье в 19:30"),
    ("弗赖堡–柏林联周日 17:30", "«Фрайбург»–«Унион» в воскресенье в 17:30"),
    ("欧联周四霍芬海姆 18:45", "Лига Европы в четверг, «Хоффенхайм» в 18:45"),
    # NOTE: bare "选出正确答案。" (P3C bridge) LAST — both P4 bridges above
    # contain it as a substring.
    ("选出正确答案。", "Выберите правильный ответ."),
]
rep_all("content34.py", C34)

# ================= content56 (P5 + P6) =================
C56 = [
    ("JUGEND · 青年", "JUGEND · Молодёжь"),
    ("LEVEL B1 · Zurück in die Schule · 重返校园",
     "LEVEL B1 · Zurück in die Schule · Снова в школу"),
    ("der Pausenhof 课间操场 · die Klassenarbeit 课堂测验 · das Referat 课堂报告 · ausschlafen 睡懒觉 · die Probe 排练。",
     "der Pausenhof = школьный двор · die Klassenarbeit = контрольная · das Referat = доклад · ausschlafen = выспаться · die Probe = репетиция."),
    ("der Pausenhof — 课间操场", "der Pausenhof — школьный двор"),
    ("die Klassenarbeit — 课堂测验", "die Klassenarbeit — контрольная"),
    ("das Referat — 课堂报告", "das Referat — доклад"),
    ("der Rucksack — 书包", "der Rucksack — рюкзак"),
    ("ausschlafen — 睡懒觉", "ausschlafen — выспаться"),
    ("die Probe — 排练", "die Probe — репетиция"),
    ("SCHULWÖRTER · 校园词汇", "SCHULWÖRTER · Школа"),
    ("你的学校假期后哪天开学？第一节是什么课？写两句德语寄来。",
     "Когда ваша школа возобновилась после каникул? Какой был первый урок? Напишите два предложения по-немецки в редакцию."),
    ("DER WOCHENPLAN DER REDAKTION · 编辑部一周计划",
     "DER WOCHENPLAN DER REDAKTION · План редакции на неделю"),
    ("ÜBUNGEN · 第 5 版练习", "ÜBUNGEN · Упражнения, стр. 5"),
    ("读第 5 版文章，选出正确答案。", "Прочитайте статью на стр. 5 и выберите правильный ответ."),
    ("用方框里的词填空。", "Вставьте слова из рамки."),
    ("BW 11 月 2 日开学", "в Баден-Вюртемберге учёба возобновилась 2 ноября"),
    ("巴伐利亚假期未结束", "в Баварии каникулы ещё не закончились"),
    ("开学周有课堂测验", "на первой учебной неделе — контрольные"),
    ("Referat = 课堂报告", "Referat = доклад"),
    ("巴伐利亚学生周五可去球场", "баварские школьники в пятницу могут пойти на стадион"),
    ("课间操场上玩", "играть на школьном дворе"),
    ("数学课堂测验", "контрольная по математике"),
    ("报告要读三本书", "для доклада нужно прочитать три книги"),
    ("假期可以睡懒觉", "на каникулах можно выспаться"),
    ("圣诞演出的第一次排练", "первая репетиция рождественского праздника"),
    ("书包里有本子铅笔", "в рюкзаке — тетради и карандаши"),
    ("用 weil 连接两个句子（动词放句末）。", "Соедините два предложения союзом weil (глагол — в конце)."),
    ("weil 句动词置尾", "в weil-предложении глагол в конце"),
    ("ist 置尾", "ist в конце"),
    ("muss 置尾", "muss в конце"),
    ("liegen 置尾", "liegen в конце"),
    ("判断对错。", "Верно или неверно."),
    ("BW 11 月 2 日复课", "в Баден-Вюртемберге учёба возобновилась 2 ноября"),
    ("全德假期并未都结束", "каникулы закончились не по всей Германии"),
    ("开学周有测验与报告", "первая учебная неделя — контрольные и доклады"),
    # P6
    ("VERTIEFUNG · 深读", "VERTIEFUNG · Углублённо"),
    ("LEVEL B2 · Pflege & Stromsteuer · 护理与电力税",
     "LEVEL B2 · Pflege & Stromsteuer · Уход и налог на электричество"),
    ("der Angehörige 亲属 · die Pflegeversicherung 护理保险 · der Pflegedienst 护理服务机构 · die Stagnation 停滞 · der Aufschwung 复苏。",
     "der Angehörige = родственник · die Pflegeversicherung = страхование ухода · der Pflegedienst = служба ухода · die Stagnation = стагнация · der Aufschwung = подъём."),
    ("DIE ZAHLEN · 本周数字", "DIE ZAHLEN · Цифры недели"),
    ("护理：在家护理需要更多帮助——对此政界仍在争论。电力税：降多少尚未确定。两者都花钱，都关系到几乎每个家庭。",
     "Уход: тем, кто ухаживает дома, нужно больше помощи — об этом спорит политика. Налог на электричество: насколько он снизится, ещё не решено. И то и другое стоит денег и касается почти каждой семьи."),
    ("PRO & CONTRA · 正方与反方 — die Argumente der Debatte",
     "PRO & CONTRA · За и против — аргументы спора"),
    ("WER PFLEGT ZU HAUSE? · 谁在家护理？", "WER PFLEGT ZU HAUSE? · Кто ухаживает дома?"),
    ('("pflegen Angehörige zu Hause", 68, "家属护理")',
     '("pflegen Angehörige zu Hause", 68, "родные")'),
    ('("nutzen einen Pflegedienst", 20, "专业上门")',
     '("nutzen einen Pflegedienst", 20, "служба")'),
    ('("leben im Pflegeheim", 12, "住养老院")',
     '("leben im Pflegeheim", 12, "пансионат")'),
    ("ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）",
     "ÜBUNGSDATEN · Учебные данные — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Числа — учебный пример, а не опрос.)"),
    ("ÜBUNGEN · 第 6 版练习", "ÜBUNGEN · Упражнения, стр. 6"),
    ("看上面的练习图表，选出正确答案。", "Ответьте по диаграмме выше."),
    ("68% 家属护理", "68% — уход родных"),
    ("专业上门 20% 第二", "служба ухода 20% — вторая"),
    ("68+20=88", "68+20=88"),
    ("养老院 12% 最小", "дом престарелых 12% — меньше всех"),
    ("养老院 12%", "дом престарелых 12%"),
    ("68+20+12=100", "68+20+12=100"),
    ("读第 6 版深读文章，选出正确答案。", "Прочитайте стр. 6 и выберите ответ."),
    ("10 月 26 日节目讨论居家护理", "программа 26 октября об уходе дома"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，600 多万人需要护理",
     "по данным ARD «Hart aber fair» от 26 октября, более 6 млн нуждаются в уходе"),
    ("家属居家护理", "родные ухаживают дома"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，约 1000 万人护理亲属",
     "по данным ARD «Hart aber fair» от 26 октября, около 10 млн ухаживают за родными"),
    ("用括号里的形式填空。", "Вставьте форму из скобок."),
    ("被动：wird + Partizip II", "пассив: wird + Partizip II"),
    ("ob 引导间接疑问句", "ob вводит косвенный вопрос"),
    ("steigen → steigt", "steigen → steigt"),
    ("sagen 过去时 sagte", "sagen в прошедшем времени: sagte"),
    ("护理保险出更多钱", "страхование ухода платит больше"),
    ("亲属居家护理", "родные ухаживают дома"),
    ("走出停滞", "выйти из стагнации"),
    ("复苏尚未自我维持", "подъём ещё не держится сам"),
]
rep_all("content56.py", C56)

# ================= content7 (P7) =================
C7 = [
    ("BEISPIELE · 例句", "BEISPIELE · Примеры"),
    ("SPRACHE · 语言", "SPRACHE · Язык"),
    ("A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所",
     "A2 → B2 · Sätze der Woche & Fehlerklinik · Фразы недели и клиника ошибок"),
    ("本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。",
     "Эта страница — о языке: три маленьких урока, фразы недели (все — из статей этого выпуска), клиника ошибок и письма читателей."),
    ("被动：wird + Partizip II", "пассив: wird + Partizip II"),
    ("复数：werden", "множественное число: werden"),
    ("werden + 原形表将来", "werden + инфинитив — будущее"),
    ("被动语态", "пассив"),
    ("spät → später（19:30 最晚）", "spät → später (19:30 — позже всех)"),
    ("weil 引导原因", "weil вводит причину"),
    ("weil 句动词置尾", "в weil-предложении глагол в конце"),
    ("länger als = 比……更长", "länger als = дольше, чем"),
    ("比平时更长 · B. 和平时一样 · C. 比平时更短", "дольше, чем обычно · B. так же, как обычно · C. короче, чем обычно"),
    ("ob 引导间接疑问", "ob вводит косвенный вопрос"),
    ("Es ist fraglich, ob ... = 是否还难说", "Es ist fraglich, ob ... = ещё неизвестно, ... ли"),
    ("dass 句动词置尾", "в dass-предложении глагол в конце"),
    ("礼貌表达观点", "вежливо высказать мнение"),
    ("14,04 Cent = 每升 14.04 欧分", "14,04 Cent = центов за литр"),
    ("rund 8,35 Euro = 大约省 8.35 欧元", "rund 8,35 Euro = около 8,35 евро"),
    ("Es wird gespielt. = 比赛将进行（被动）", "Es wird gespielt. = Будет игра"),
    ("Meiner Meinung nach ... = 在我看来……", "Meiner Meinung nach ... = По-моему"),
    ("Ich finde, dass ... = 我觉得……", "Ich finde, dass ... = Я считаю, ..."),
    ("Es ist fraglich, ob ... = 是否……还难说", "Es ist fraglich, ob ... = Вопрос, ... ли"),
    ("DER WERKZEUGKASTEN · 工具箱", "DER WERKZEUGKASTEN · Копилка"),
    ("LESERBRIEFE · 读者来信", "LESERBRIEFE · Письма читателей"),
    ("NOCH EIN WORT · 再学一词", "NOCH EIN WORT · Ещё одно слово"),
    ("«der Tankrabatt»（Seite 2）: die gesenkte Steuer auf Benzin und Diesel. 油价减税。",
     "«der Tankrabatt» (Seite 2): die gesenkte Steuer auf Benzin und Diesel. Скидка на топливо."),
    ("SÄTZE DER WOCHE · 本周金句", "SÄTZE DER WOCHE · Фразы недели"),
    ("原文摘录，逐字引自本期文章 · 括号内为出处", "Дословные цитаты из статей выпуска · в скобках — источник"),
    ("连续四个足球之夜，然后是整周末联赛。", "Четыре футбольных вечера подряд, а потом — целый уикенд лиги."),
    ("汽油和柴油的能源税每升降低 14.04 欧分。", "Налог на энергию на бензин и дизель снижается на 14,04 цента за литр."),
    ("加 50 升油，大约省 8.35 欧元。", "Кто заправляет 50 литров, экономит около 8,35 евро."),
    ("秋假过后，学校又开学了。", "После осенних каникул школа снова началась."),
    ("白天短，夜晚长。", "Дни короткие, вечера длинные."),
    ("德国球队的两场艰难客场之战。", "Два тяжёлых выездных матча для немецких команд."),
    ("德国经济正在缓慢走出停滞，但复苏还不能自我维持。",
     "Немецкая экономика медленно выходит из стагнации, но подъём ещё не держится сам."),
    ("缓慢向好——但不会自动变好。", "Дело медленно идёт в гору — но само собой ничего не выйдет."),
    ("FEHLERKLINIK · 纠错诊所", "FEHLERKLINIK · Клиника ошибок"),
    ("学习者最常犯的四个错 · 先自己改，再看答案", "Четыре самые частые ошибки · сначала исправьте сами, потом смотрите ответ"),
    ("动词第二位：主语不在句首时，动词仍居第二。",
     "Глагол на втором месте: если подлежащее не в начале, глагол всё равно второй."),
    ("halb acht = 七点半（acht 之前）。", "halb acht = половина восьмого (до восьми)."),
    ("Perfekt 中 Partizip II 放句末。", "В перфекте Partizip II стоит в конце."),
    ("ob 从句动词放句末。", "В ob-придаточном глагол стоит в конце."),
    ("IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.3)", "IN DER NÄCHSTEN AUSGABE · В следующем выпуске (VOL.3)"),
]
rep_all("content7.py", C7)

# P7 readers box: label + two Russian paras replacing the Chinese note.
# German defer / reader / invite strings are FROZEN and stay untouched.
rep("content7.py", 'label = "Ein Beispiel der Redaktion!"',
    'label = "Пример редакции!"', 1)
# NOTE: the core rh formula spans 5 lines (first line + 4 continuations);
# a first-line-only replacement leaves dangling continuations behind, so
# replace the WHOLE block (same trap as DE x FR).
p7 = open(os.path.join(BASE, "content7.py"), encoding="utf-8").read()
_lines = p7.splitlines()
_i = next(i for i, ln in enumerate(_lines) if ln.startswith("rh = "))
OLD_RH = "\n".join(_lines[_i:_i + 5])
assert OLD_RH.count("wrap(chinese") == 1, OLD_RH
NEW_RH = ('rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \\\n'
          '    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
          '    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \\\n'
          '    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
          '    + len(wrap(note_ru, "sans", False, 19.5, CW - 44)) * 28 + 8 \\\n'
          '    + len(wrap(invite_ru, "serif", False, 20.5, CW - 44)) * 29.5 + 40 + 32')
rep("content7.py", OLD_RH, NEW_RH, 1)
rep("content7.py",
    'chinese = "编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.3。请寄来您的习作，优秀者刊登于 VOL.3。"',
    'note_ru = "Настоящих писем и лучших сочинений не поступило; продолжение — в VOL.3."\n'
    'invite_ru = "Присылайте настоящие письма — напечатаем лучшие в VOL.3."', 1)
rep("content7.py",
    'p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)',
    'yy3 = p.para(ix + 22, yy3 + 19.5, note_ru, 19.5, "sans", False, GREY, CW - 44, 1.42) + 8\n'
    'p.para(ix + 22, yy3 + 20.5, invite_ru, 20.5, "serif", False, INK, CW - 44, 1.42)', 1)

# ================= content8 (P8) =================
C8 = [
    ("ÜBUNGEN & ANTWORTEN · 练习与答案", "ÜBUNGEN & ANTWORTEN · Упражнения и ответы"),
    ("SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方",
     "SCHLUSSTEST · Итоговый тест · Все ответы — внизу на этой странице"),
    ("spielt（第三人称单数）", "spielt (3-е лицо, единственное число)"),
    ("beginnt（第三人称单数）", "beginnt (3-е лицо, ед. число)"),
    ("kauft（第三人称单数）", "kauft (3-е лицо, ед. число)"),
    ("schnitzt 雕刻南瓜", "schnitzt = вырезать тыкву"),
    ("schläft（第三人称单数）", "schläft (3-е лицо, ед. число)"),
    ("Tankrabatt 油价减税", "Tankrabatt = скидка на топливо"),
    ("geht（第三人称单数）", "geht (3-е лицо, ед. число)"),
    ("erzählt（第三人称单数）", "erzählt (3-е лицо, ед. число)"),
    ("A · LÜCKENTEXT · 完形填空", "A · LÜCKENTEXT · Пропуски"),
    ("选项：", "Варианты:"),
    ("B · WISSENSFRAGEN · 综合问答", "B · WISSENSFRAGEN · Вопросы"),
    ("减税到 2026 年 12 月 31 日", "скидка до 31 декабря 2026 года"),
    ("拜仁周二客战马竞", "«Бавария» во вторник в гостях у «Атлетико»"),
    ("霍芬海姆欧联客战水晶宫", "«Хоффенхайм» в Лиге Европы у «Кристал Пэлас»"),
    ("BW 假期已结束", "в Баден-Вюртемберге каникулы уже закончились"),
    ("ZEW 预期 28.1", "ожидания ZEW — 28,1"),
    ("周五汉堡–门兴开轮", "«Гамбург»–«Гладбах» открывают в пятницу"),
    ("10 月 26 日节目讨论居家护理", "программа 26 октября об уходе дома"),
    ("诸圣节 11 月 1 日", "День всех святых — 1 ноября"),
    ("C · LESEVERSTEHEN · 阅读理解", "C · LESEVERSTEHEN · Чтение"),
    ("周二看拜仁客战马竞", "во вторник смотрят «Баварию» у «Атлетико»"),
    ("周六买南瓜", "в субботу покупают тыкву"),
    ("霍芬海姆–沙尔克周日 19:30", "«Хоффенхайм»–«Шальке» в воскресенье в 19:30"),
    ("D · SÄTZE BAUEN · 造句", "D · SÄTZE BAUEN · Предложения"),
    ("时间状语，动词第二位", "обстоятельство времени, глагол на втором месте"),
    ("主谓宾顺序", "порядок подлежащее–сказуемое–дополнение"),
    ("时间状语开头，动词第二位", "время в начале, глагол на втором месте"),
    ("地点开头，动词第二位", "место в начале, глагол на втором месте"),
    ("E · ÜBERSETZEN · 翻译", "E · ÜBERSETZEN · Перевод"),
    ("（译成中文）", ""),
    # E keys: DE->RU re-aimed (keys change language by definition);
    # the 140 key stays German, only its prompt/instr change (below).
    ('"油价减税持续到十二月。"', '"Скидка на топливо действует до декабря."'),
    ('"我周二看足球。"', '"Во вторник я смотрю футбол."'),
    ('"学校又开学了。"', '"Школа снова началась."'),
    ("laufen = 持续", "laufen = действовать"),
    ("schauen = 看", "schauen = смотреть"),
    ("wieder begonnen = 又开始", "wieder begonnen = снова началась"),
    ("多睡一小时 = eine Stunde länger schlafen", "спать на час дольше = eine Stunde länger schlafen"),
    ("F · WÖRTER PAAREN · 词汇配对", "F · WÖRTER PAAREN · Пары слов"),
    ("Tankrabatt=油价减税 b", "Tankrabatt=скидка на топливо b"),
    ("Pflege=护理 d", "Pflege=уход d"),
    ("Advent=将临期 a", "Advent=адвент a"),
    ("Pausenhof=课间操场 c", "Pausenhof=школьный двор c"),
    ("G · DIALOG · 对话补全", "G · DIALOG · Дополните диалог"),
    ("schaust（第二人称单数）", "schaust (2-е лицо, ед. число)"),
    ("siehst（第二人称单数）", "siehst (2-е лицо, ед. число)"),
    ("kochen（第一人称复数）", "kochen (1-е лицо, мн. число)"),
    ("machst（第二人称单数）", "machst (2-е лицо, ед. число)"),
    ("gehe（第一人称单数）", "gehe (1-е лицо, ед. число)"),
    ("开放题 — 要点见写作框，范文在第 8 版写作框内",
     "открытое задание — пункты в рамке задания; образец — в рамке на этой странице"),
    ("按要点给分", "оценка по пунктам"),
    ("H · SCHREIBEN · 写作", "H · SCHREIBEN · Письмо"),
    ("MUSTER · 范文（84 Wörter）", "MUSTER · Образец (84 слова)"),
    ("ANTWORTEN · 全部答案与简析（第 1–8 版）", "ANTWORTEN · Все ответы с пояснениями (стр. 1–8)"),
]
rep_all("content8.py", C8)
# Writing RU para: replace the whole line by line number (the core line
# carries a mojibake-sensitive Chinese string; match on its unique prefix).
p8path = os.path.join(BASE, "content8.py")
_lines = open(p8path, encoding="utf-8").read().splitlines()
for _i, _ln in enumerate(_lines):
    if _ln.startswith("p.para(wx, wy + 196,"):
        _lines[_i] = ('p.para(wx, wy + 196, "Напишите по-немецки короткий текст (80–100 слов): «Моя футбольная неделя». '
                      'Расскажите: какие матчи вы смотрите? С кем? Что вы едите во время матча? Добавьте одно предложение '
                      'о скидке на топливо или об уходе. Лучшие тексты мы напечатаем в VOL.3 (стр. 7, «Письма читателей»).", '
                      '20, "sans", False, GREY, ww, 1.4)')
        LOG.append(f"content8.py: writing para line {_i+1} replaced whole-line")
        break
else:
    raise AssertionError("content8.py: writing para line not found")
open(p8path, "w", encoding="utf-8").write("\n".join(_lines) + "\n")

# ---------- generic value maps (bare text, W43 DE x RU vocabulary) ----------
TYPEMAP = [("完成句子", "Дополните предложение"), ("单选", "Выбор ответа"),
           ("句型转换", "Преобразуйте предложение"), ("词汇配对", "Соедините пары"),
           ("判断对错", "Верно или нет"), ("完形填空", "Заполните пропуски"),
           ("造句", "Составьте предложение"), ("对话补全", "Дополните диалог"),
           ("翻译", "Переведите"), ("写作", "Письмо")]
INSTRMAP = [('instr="填空"', 'instr="Вставьте"'),
            ('instr="改写"', 'instr="Перепишите"'),
            ('instr="判断"', 'instr="Верно или нет"'),
            ('instr="造句"', 'instr="Составьте"'),
            ('instr="翻译"', 'instr="Переведите"'),
            ('instr="把词和释义配对"', 'instr="Соедините пары"')]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTRMAP + TYPEMAP:  # instr tokens first: TYPEMAP would corrupt instr="翻译"
        pth = os.path.join(BASE, f)
        n = open(pth, encoding="utf-8").read().count(old)
        if n == 0:
            LOG.append(f"{f}: 0x {old!r} (absent, skipped)")
        else:
            rep(f, old, new)
# E item 140: prompt becomes Russian, instr becomes Переведите на немецкий.
# The generic INSTRMAP already turned instr="翻译" into Переведите
# everywhere; fix ONLY the 140 line (unique prompt literal).
rep("content8.py", '"我周日多睡一小时。（译成德语）", instr="Переведите"',
    '"В воскресенье я сплю на час дольше.", instr="Переведите на немецкий"', 1)
# P8 keys: W43 DE x RU shipped form — half-width parens, 13pt keys,
# 1.16 line height, Russian page separators.
rep("content8.py", '— 第 {pg} 版 —', '— СТРАНИЦА {pg} —', 1)
rep("content8.py", 's += f"（{e[\'note\']}）"', 's += f"({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13.0, "sans", False, INK, 1.16, 9)', 1)

print("\n".join(LOG))
print(f"TOTAL replacements: {len(LOG)}")
