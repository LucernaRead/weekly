# -*- coding: utf-8 -*-
"""DE x RU fan-out transform for W46 DE core build copy.
Generated from the EN pair table + tr-ru.py. German body text is
NEVER touched: every `old` is a Chinese explanation-layer string,
a bilingual furniture string, or a generic type/instr token.
Run once from the build dir copy."""
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
    LOG.append(f"{fname}: {n}x {old[:60]!r} -> {new[:60]!r}")
    open(p, "w", encoding="utf-8").write(s.replace(old, new))

def rep_all(fname, pairs):
    seen = set()
    for old, new in pairs:
        assert old not in seen, f"duplicate old in {fname}: {old!r}"
        seen.add(old)
    for old, new in sorted(pairs, key=lambda t: -len(t[0])):
        rep(fname, old, new)

# ---------- OUT repoint (1 per content file) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w46-de-core", "weekly-report-w46-de-ru", 1)

# ---------- svglib docstring comment only (not rendered) ----------
pth = os.path.join(BASE, "svglib.py")
s = open(pth, encoding="utf-8").read()
if "for \u91cd\u9633." in s:
    rep("svglib.py", "for \u91cd\u9633.", "for Double Ninth.", 1)
else:
    LOG.append("svglib.py: no Double Ninth comment (already adapted), skipped")

# ---------- bslib4: furniture + gloss prefix ----------
rep("bslib4.py",
    '"Die Lucerna · \u5fb7\u8bed\u5468\u62a5 VOL.3 · LUCERNA GERMAN WEEKLY"',
    '"Die Lucerna · НЕМЕЦКИЙ ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА НЕМЕЦКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ"', 1)
rep("bslib4.py", 'f"\u7b2c {n} \u7248 / \u5171 {total} \u7248"', 'f"Страница {n} из {total}"', 1)
rep("bslib4.py", '"\u8bd1\u6ce8\uff5c" + s', '"Пояснение — " + s', 1)

# ================= content12.py =================
C12 = [
    ('WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语', 'WÖCHENTLICH AUF DEUTSCH · КАЖДУЮ НЕДЕЛЮ · НЕМЕЦКИЙ, КОТОРЫЙ ЧИТАЮТ НЕМЦЫ'),
    ('德 语 周 报 · VOL.3 · 国 家 队 · 圣 马 丁 · NFL', 'НЕМЕЦКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.3 · СБОРНАЯ · СВЯТОЙ МАРТИН · NFL'),
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")', 'p.text(975, 372, "ТЕКСТЫ НА НЕМЕЦКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", 20, "sans", True, BRICK, anchor="middle")'),
    ('本周国家队周 · 圣马丁节与 NFL', 'НЕДЕЛЯ СБОРНОЙ · СВЯТОЙ МАРТИН И NFL'),
    ('详见第 4 版 · Seite 4', 'См. стр. 4'),
    ('DIE TOPMELDUNG · 头条', 'DIE TOPMELDUNG · Главная новость'),
    ('讲解｜die Länderspielpause 国家队比赛间歇期 · das Viertelfinale 四分之一决赛 · ausverkauft 售罄。', 'Пояснения — die Länderspielpause = пауза на сборные · das Viertelfinale = четвертьфинал · ausverkauft = распродано.'),
    ('DIE WOCHE IN ZAHLEN · 数字看本周', 'DIE WOCHE IN ZAHLEN · В цифрах'),
    ('5 — Punkte hat Deutschland nach vier Spielen in der Nations League（四轮过后德国队 5 分）', '5 — Punkte hat Deutschland nach vier Spielen in der Nations League (у Германии 5 очков после четырёх игр)'),
    ('11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（11 点 11 分狂欢季开幕）', '11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln (карнавальный сезон открывается в 11.11)'),
    ('15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（周日 15 点 30 分 NFL 开球）', '15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München (матч NFL начинается в воскресенье в 15.30)'),
    ('JETZT ÜBEN · 即学即练', 'JETZT ÜBEN · Упражняйтесь'),
    ('国家队比赛周', 'неделя сборных'),
    ('塞尔维亚首都', 'столица Сербии'),
    ('狂欢季 11 点 11 分开幕', 'карнавал открывается в 11.11'),
    ('NFL 在慕尼黑', 'NFL в Мюнхене'),
    ('四轮 5 分', '5 очков после четырёх игр'),
    ('周日是纪念日', 'воскресенье — день памяти'),
    ('圣马丁节 11 月 11 日', 'День святого Мартина — 11 ноября'),
    ('11 月 11 日是星期三', '11 ноября — среда'),
    ('本周大问题 · Die Fragen der Woche', 'Большие вопросы · Die Fragen der Woche'),
    ('德国本周最热议的五个问题。', 'Пять горячих вопросов недели.'),
    ('IN DIESER AUSGABE · 本期目录', 'IN DIESER AUSGABE'),
    ('空场比赛（无观众）。详见第 4 版。', 'Матч без зрителей. См. стр. 4.'),
    ('KURZ & GUT · 快讯', 'KURZ & GUT · Коротко'),
    ('BLITZQUIZ · 闪电问答', 'BLITZQUIZ · Блиц-викторина'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Прочитайте стр. 1 и выберите правильный ответ · Ответы на стр. 8'),
    ('周五客战塞尔维亚', 'в гостях в Сербии в пятницу'),
    ('NFL 下午 3 点半开球', 'NFL начинается в 15.30'),
    ('纪念日在周日', 'день памяти — в воскресенье'),
    ('LEBEN · 生活', 'LEBEN · Жизнь'),
    ('LEVEL A2 · Der 11. November & der Alltag · 11 月 11 日与日常生活', 'LEVEL A2 · Der 11. November & der Alltag · 11 ноября и повседневная жизнь'),
    ('der Jeck 狂欢者（科隆方言） · die fünfte Jahreszeit 第五个季节（狂欢季） · die Laterne 灯笼 · der Weckmann 面人面包 · die Martinsgans 圣马丁鹅。', 'der Jeck = карнавальный гуляка (кёльнский диалект) · die fünfte Jahreszeit = пятое время года (карнавал) · die Laterne = фонарик · der Weckmann = булочный человечек · die Martinsgans = гусь святого Мартина.'),
    ('DER 11. NOVEMBER · 11 月 11 日', 'DER 11. NOVEMBER'),
    ('你过狂欢节还是圣马丁节？写两句德语寄来。', 'Карнавал или День св. Мартина? Напишите два предложения!'),
    ('UND SIE? · 说说你自己', 'UND SIE? · А вы?'),
    ('MARTIN IN KÜRZE · 圣马丁简讯', 'MARTIN IN KÜRZE · Кратко'),
    ('RECHNEN WIR MAL · 算一算', 'RECHNEN WIR MAL · Посчитаем'),
    ('Die Uhrzeiten der Woche · 本周时刻', 'Die Uhrzeiten der Woche · Время на этой неделе'),
    ('注意：11 月 11 日是工作日。去科隆要早到：老城很挤，晚上街道属于提灯笼的孩子们。', 'Обратите внимание: 11 ноября — рабочий день. Приезжайте в Кёльн рано: старый город переполнен, а вечером улицы принадлежат детям с фонариками.'),
    ('ÜBUNGEN · 第 2 版练习', 'ÜBUNGEN · Упражнения стр. 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Ответы на стр. 8 · Уровни смешаны — ищите каждый ответ по его номеру'),
    ('看第 2 版文章，用时间填空。', 'Прочитайте статью на стр. 2 и впишите время.'),
    ('WDR 10 点半直播', 'WDR в прямом эфире с 10.30'),
    ('Weckmann 是面人面包', 'Weckmann — это булочный человечек'),
    ('11 月 11 日不是法定假日', '11 ноября — не выходной день'),
    ('圣马丁鹅配红甘蓝和丸子', 'гусь святого Мартина с красной капустой и клёцками'),
    ('改成 Perfekt 现在完成时。', 'Перепишите в Perfekt (прошедшее время).'),
    ('读第 2 版文章，选出正确答案。', 'Прочитайте статью на стр. 2 и выберите правильный ответ.'),
    ('Jeck=狂欢者 c', 'Jeck=карнавальный гуляка c'),
    ('Laterne=灯笼 a', 'Laterne=фонарик a'),
    ('Weckmann=面人面包 b', 'Weckmann=булочный человечек b'),
    ('Martinsgans=圣马丁鹅 d', 'Martinsgans=гусь святого Мартина d'),
]
rep_all("content12.py", C12)

# ================= content34.py =================
C34 = [
    ('KULTUR · 文化', 'KULTUR · Культура'),
    ('A2 → B1 · St. Martin, Karneval & Rückblick · 圣马丁、狂欢节与回顾', 'A2 → B1 · St. Martin, Karneval & Rückblick · Святой Мартин, карнавал и взгляд назад'),
    ('der Bettler 乞丐 · der Mantel 斗篷 · das Geschnatter 鹅叫声 · der Gänsestall 鹅棚 · das Dreigestirn 狂欢节三人组。', 'der Bettler = нищий · der Mantel = плащ · das Geschnatter = гогот · der Gänsestall = гусятник · das Dreigestirn = карнавальный триумвират.'),
    ('ST. MARTIN · 圣马丁', 'ST. MARTIN · Святой Мартин'),
    ('die Laterne — 灯笼', 'die Laterne — фонарик'),
    ('der Mantel — 斗篷', 'der Mantel — плащ'),
    ('die Gans — 鹅', 'die Gans — гусь'),
    ('der Weckmann — 面人面包', 'der Weckmann — булочный человечек'),
    ('das Martinsfeuer — 圣马丁篝火', 'das Martinsfeuer — костёр св. Мартина'),
    ('das Kostüm — 服装', 'das Kostüm — костюм'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · Св. Мартин'),
    ('UND SIE? · 说说你自己', 'UND SIE? · А вы?'),
    ('你做过灯笼吗？你们国家的孩子唱什么歌？写两句德语寄来。', 'Вы делали фонарик? Напишите два предложения!'),
    ('DER TIPP · 编辑部建议', 'DER TIPP · Совет'),
    ('ÜBUNGEN · 第 3 版练习', 'ÜBUNGEN · Упражнения стр. 3'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Ответы на стр. 8 · Уровни смешаны — ищите каждый ответ по его номеру'),
    ('读第 3 版文章，判断对错。', 'Прочитайте статью на стр. 3. Верно или нет?'),
    ('传说马丁是罗马士兵', 'легенда гласит, что Мартин был римским солдатом'),
    ('传说鹅叫声暴露了他', 'легенда гласит, что гуси его выдали'),
    ('纪念日 11 月 11 日', 'день памяти — 11 ноября'),
    ('截稿时 11 月 3–8 日结果未知', 'результаты 3–8 ноября на момент сдачи неизвестны'),
    ('狂欢季 11 点 11 分开幕', 'карнавал открывается в 11.11'),
    ('用方框里的词填空。', 'Дополните словами из рамки.'),
    ('斗篷分给乞丐', 'плащ, разделённый с нищим'),
    ('纸灯笼', 'бумажный фонарик'),
    ('圣马丁鹅', 'гусь святого Мартина'),
    ('圣马丁鹅配红甘蓝和丸子', 'гусь святого Мартина с красной капустой и клёцками'),
    ('狂欢节服装', 'карнавальный костюм'),
    ('游行在篝火处结束', 'шествие заканчивается у костра'),
    ('选出正确答案。', 'Выберите правильный ответ.'),
    ('马丁后来成为图尔主教', 'Мартин позже стал епископом Турским'),
    ('灯笼游行常在前后晚上举行', 'шествия с фонариками часто проходят в соседние вечера'),
    ('VOL.4 报道 11 月 3–8 日结果', 'VOL.4 сообщит результаты 3–8 ноября'),
    ('把词组成正确的句子。', 'Составьте из слов правильное предложение.'),
    ('主谓宾顺序', 'порядок подлежащее–сказуемое–дополнение'),
    ('时间状语开头，动词第二位', 'время — первым, глагол — вторым'),
    ('地点开头，动词第二位', 'место — первым, глагол — вторым'),
    ('SPORT · 体育', 'SPORT · Спорт'),
    ('LEVEL B1 · Nationalelf & NFL · 国家队与 NFL', 'LEVEL B1 · Nationalelf & NFL · Сборная и NFL'),
    ('das Geisterspiel 空场比赛 · das Hinspiel 首回合 · ausverkauft 售罄 · der Star 明星 · gewinnen 获胜。', 'das Geisterspiel = матч-призрак · das Hinspiel = первый матч · ausverkauft = распродано · der Star = звезда · gewinnen = побеждать.'),
    ('你更爱看足球还是美式橄榄球？贝尔格莱德谁赢？写两句德语寄来。', 'Футбол или американский футбол? Кто победит? Два предложения!'),
    ('DER SPIELPLAN · 本周与下周赛程', 'DER SPIELPLAN · Эта неделя и следующая'),
    ('ÜBUNGEN · 第 4 版练习', 'ÜBUNGEN · Упражнения стр. 4'),
    ('读第 4 版文章，选出正确答案。', 'Прочитайте статью на стр. 4 и выберите правильный ответ.'),
    ('德国 5 分，荷兰希腊各 8 分', 'Германия — 5 очков, Нидерланды и Греция — по 8'),
    ('主教练 11 月 5 日公布名单', 'тренер назовёт состав 5 ноября'),
    ('贝尔格莱德空场', 'пустой стадион в Белграде'),
    ('首回合德国 2:0 胜塞尔维亚', 'Германия выиграла первый матч 2:0 у Сербии'),
    ('NFL 慕尼黑赛售罄', 'билеты на матч NFL в Мюнхене распроданы'),
    ('Geisterspiel=空场比赛 b', 'Geisterspiel=матч-призрак b'),
    ('Hinspiel=首回合 a', 'Hinspiel=первый матч a'),
    ('Ausrüster=装备赞助商 c', 'Ausrüster=поставщик формы c'),
    ('ausverkauft=售罄 d', 'ausverkauft=распродано d'),
    ('用比较级完成句子（括号里是原级）。', 'Дополните сравнительной степенью (слово в скобках — в положительной степени).'),
    ('viel → mehr（荷兰 8 分多于德国 5 分）', 'viel → mehr (у Нидерландов 8 очков — больше, чем 5 у Германии)'),
    ('spät → später（15:30 晚于 11:11）', 'spät → später (15.30 позже, чем 11.11)'),
    ('leise → leiser（空场比主场安静）', 'leise → leiser (пустой стадион тише, чем домашний матч)'),
    ('früh → früher（11 月 5 日早于 11 月 13 日）', 'früh → früher (5 ноября раньше, чем 13 ноября)'),
    ('看上面的赛程表，选出正确答案。', 'Посмотрите на таблицу матчей выше и выберите правильный ответ.'),
    ('塞尔维亚–德国周五 20:45', 'Сербия–Германия в пятницу в 20.45'),
    ('NFL 周日 15:30', 'NFL в воскресенье в 15.30'),
    ('德国–荷兰周一 20:45', 'Германия–Нидерланды в понедельник в 20.45'),
    ('拜仁–科隆周五 20:30', 'Бавария–Кёльн в пятницу в 20.30'),
    ('沙尔克–斯图加特周六 17:30', 'Шальке–Штутгарт в субботу в 17.30'),
]
rep_all("content34.py", C34)

# ================= content56.py =================
C56 = [
    ('JUGEND · 青年', 'JUGEND · Молодёжь'),
    ('LEVEL B1 · Laternen, Lieder & Schule · 灯笼、歌曲与学校', 'LEVEL B1 · Laternen, Lieder & Schule · Фонарики, песни и школа'),
    ('basteln 制作 · der Pausenhof 课间操场 · sich verkleiden 乔装打扮 · die Stimmung 气氛 · der Pirat 海盗。', 'basteln = мастерить · der Pausenhof = школьный двор · sich verkleiden = наряжаться · die Stimmung = настроение · der Pirat = пират.'),
    ('SCHULWOCHE · 开学周', 'SCHULWOCHE · Снова в школу'),
    ('die Laterne — 灯笼', 'die Laterne — фонарик'),
    ('basteln — 制作', 'basteln — мастерить'),
    ('das Lied — 歌曲', 'das Lied — песня'),
    ('das Kostüm — 服装', 'das Kostüm — костюм'),
    ('der Umzug — 游行', 'der Umzug — шествие'),
    ('der Stern — 星星', 'der Stern — звезда'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · Св. Мартин'),
    ('UND SIE? · 说说你自己', 'UND SIE? · А вы?'),
    ('你小时候做过灯笼吗？11 月你唱哪首歌？写两句德语寄来。', 'Фонарик в детстве? Ваша песня? Два предложения!'),
    ('DER WOCHENPLAN DER REDAKTION · 编辑部一周计划', 'DER WOCHENPLAN DER REDAKTION · Неделя редакции'),
    ('ÜBUNGEN · 第 5 版练习', 'ÜBUNGEN · Упражнения стр. 5'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Ответы на стр. 8 · Уровни смешаны — ищите каждый ответ по его номеру'),
    ('读第 5 版文章，选出正确答案。', 'Прочитайте статью на стр. 5 и выберите правильный ответ.'),
    ('11 月 9 日全德复课', 'школа возобновляется везде 9 ноября'),
    ('孩子们做纸灯笼', 'дети делают бумажные фонарики'),
    ('纸灯笼', 'бумажный фонарик'),
    ('上午狂欢，下午圣马丁', 'карнавал утром, святой Мартин днём'),
    ('NFL 周日在电视上', 'NFL по телевизору в воскресенье'),
    ('周五看国家队比赛', 'смотреть сборную в пятницу'),
    ('用方框里的词填空。', 'Дополните словами из рамки.'),
    ('做灯笼', 'делать фонарики'),
    ('唱圣马丁歌曲', 'петь песни о святом Мартине'),
    ('狂欢节服装', 'карнавальный костюм'),
    ('灯笼游行', 'шествие с фонариками'),
    ('灯笼上的星星', 'звезда на фонарике'),
    ('用 weil 连接两个句子（动词放句末）。', 'Соедините два предложения с помощью weil (глагол — в конец).'),
    ('weil 句动词置尾', 'в придаточном с weil глагол — в конце'),
    ('ist 置尾', 'ist — в конец'),
    ('will 置尾', 'will — в конец'),
    ('beginnt 置尾', 'beginnt — в конец'),
    ('判断对错。', 'Верно или нет?'),
    ('11 月 9 日巴伐利亚也复课', 'Бавария тоже возвращается 9 ноября'),
    ('灯笼游行在晚上', 'шествие с фонариками — вечером'),
    ('孩子们唱圣马丁歌曲', 'дети поют песни о святом Мартине'),
    ('VERTIEFUNG · 深读', 'VERTIEFUNG · Углубление'),
    ('LEVEL B2 · Volkstrauertag & Stromsteuer · 纪念日与电力税', 'LEVEL B2 · Volkstrauertag & Stromsteuer · День памяти и налог на электричество'),
    ('gedenken 纪念 · die Kranzniederlegung 献花圈 · der stille Tag 安静日 · die Verbundenheit 联系 · die Versöhnung 和解。', 'gedenken = поминать · Kranzniederlegung = венок · stille Tag = тихий день · Verbundenheit = связь · Versöhnung = примирение.'),
    ('DIE ZAHLEN · 本周数字', 'DIE ZAHLEN · Цифры'),
    ('纪念日：纪念需要安静——对此几乎人人赞同。电力税：降多少尚未确定。两者都关系到几乎每个家庭。', 'День памяти: память требует тишины — почти все согласны. Налог на электричество: насколько он снизится, пока открыто. Оба касаются почти каждой семьи.'),
    ('ZWEI SONNTAGE IM NOVEMBER · 十一月的两个周日', 'ZWEI SONNTAGE IM NOVEMBER · Два воскресенья ноября'),
    ('WAS INTERESSIERT DIE LESER? · 读者最关心什么？', 'WAS INTERESSIERT DIE LESER? · Что интересует читателей?'),
    ('("Nations League und NFL", 46, "足球")', '("Nations League und NFL", 46, "футбол")'),
    ('("St. Martin und Karneval", 34, "节日")', '("St. Martin und Karneval", 34, "праздники")'),
    ('("Volkstrauertag und Gedenken", 20, "纪念")', '("Volkstrauertag und Gedenken", 20, "память")'),
    ('ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）', 'ÜBUNGSDATEN · Учебные данные — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Учебные данные, не настоящий опрос.)'),
    ('ÜBUNGEN · 第 6 版练习', 'ÜBUNGEN · Упражнения стр. 6'),
    ('看上面的练习图表，选出正确答案。', 'Используйте учебную диаграмму выше.'),
    ('46% 足球最受关注', 'футбол лидирует — 46%'),
    ('节日 34% 第二', 'праздники вторые — 34%'),
    ('纪念 20% 最小', 'память — меньше всего, 20%'),
    ('纪念 20%', 'память 20%'),
    ('读第 6 版深读文章，选出正确答案。', 'Прочитайте статью на стр. 6.'),
    ('11 月 15 日纪念日', 'день памяти — 15 ноября'),
    ('ZDF 13 点半直播纪念仪式', 'ZDF в прямом эфире с 13.30'),
    ('家庭电力税 2.05 欧分', 'налог для домохозяйств — 2,05 цента'),
    ('2027 年预算 11 月 27 日表决', 'голосование по бюджету 2027 — 27 ноября'),
    ('用括号里的形式填空。', 'Вставьте форму из скобок.'),
    ('被动：wird + Partizip II', 'пассив: wird + причастие прошедшего времени'),
    ('ob 引导间接疑问句', 'ob вводит косвенный вопрос'),
    ('献花圈仪式', 'церемония возложения венков'),
    ('为和平与和解', 'за мир и примирение'),
    ('德奥联系', 'немецко-австрийская связь'),
    ('纪念受害者', 'память о жертвах'),
]
rep_all("content56.py", C56)

# ================= content7.py =================
C7 = [
    ('SPRACHE · 语言', 'SPRACHE · Язык'),
    ('A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所', 'A2 → B2 · Sätze der Woche & Fehlerklinik · Предложения недели и клиника ошибок'),
    ('本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。', 'Эта страница — только о языке: три коротких урока, предложения недели (все процитированы слово в слово из статей этого номера), клиника ошибок и письма читателей.'),
    ('BEISPIELE · 例句', 'BEISPIELE · Примеры'),
    ('被动：wird + Partizip II', 'пассив: wird + причастие прошедшего времени'),
    ('复数：werden', 'множественное число: werden'),
    ('werden + 原形表将来', 'werden + инфинитив для будущего времени'),
    ('被动语态', 'страдательный залог'),
    ('lang → länger（夜晚比白天长）', 'lang → länger (ночь длиннее дня)'),
    ('weil 引导原因', 'weil вводит причину'),
    ('weil 句动词置尾', 'в придаточном с weil глагол — в конце'),
    ('länger als = 比……更长', 'länger als = длиннее, чем'),
    ('„Länger als sonst“ heißt... A. 比平时更长 · B. 和平时一样 · C. 比平时更短', '„Länger als sonst“ означает... A. дольше обычного · B. как обычно · C. короче обычного'),
    ('ob 引导间接疑问', 'ob вводит косвенный вопрос'),
    ('Es ist fraglich, ob ... = 是否还难说', 'Es ist fraglich, ob ... = сомнительно, ... ли'),
    ('dass 句动词置尾', 'в придаточном с dass глагол — в конце'),
    ('礼貌表达观点', 'вежливый способ высказать мнение'),
    ('11.11 Uhr = 11 点 11 分', '11.11 Uhr = 11.11'),
    ('vor leeren Rängen = 空场，没有观众', 'vor leeren Rängen = пустой стадион'),
    ('Es wird gespielt. = 比赛将进行（被动）', 'Es wird gespielt. = Будет сыграно'),
    ('Meiner Meinung nach ... = 在我看来……', 'Meiner Meinung nach = по моему мнению'),
    ('Ich finde, dass ... = 我觉得……', 'Ich finde, dass = я считаю, что'),
    ('Es ist fraglich, ob ... = 是否……还难说', 'Es ist fraglich, ob ... = сомнительно, что'),
    ('DER WERKZEUGKASTEN · 工具箱', 'DER WERKZEUGKASTEN'),
    ('label = "Ein Beispiel der Redaktion!"', 'label = "Пример от редакции!"'),
    ('编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.4。请寄来您的习作，优秀者刊登于 VOL.4。', 'Пример от редакции, не настоящее письмо: к моменту сдачи настоящих писем не поступило. Присылайте свои для VOL.4!'),
    ('LESERBRIEFE · 读者来信', 'LESERBRIEFE · Письма читателей'),
    ('NOCH EIN WORT · 再学一词', 'NOCH EIN WORT · Ещё одно слово'),
    ('«das Geisterspiel»（Seite 4）: ein Spiel ohne Zuschauer im Stadion. 空场比赛。', '«das Geisterspiel» (Seite 4): Spiel ohne Zuschauer. Матч-призрак.'),
    ('SÄTZE DER WOCHE · 本周金句', 'SÄTZE DER WOCHE · Предложения недели'),
    ('原文摘录，逐字引自本期文章 · 括号内为出处', 'Процитировано слово в слово из статей этого номера · источник в скобках'),
    ('德甲休战——但国家队要比赛。', 'Бундеслига на паузе — но сборная играет.'),
    ('11 点 11 分，科隆新一季狂欢季开幕。', 'В 11.11 в Кёльне начинается новый карнавальный сезон.'),
    ('他的纪念日是 11 月 11 日。', 'Его день памяти — 11 ноября.'),
    ('书包收拾好了，操场上又热闹起来。', 'Рюкзаки собраны, школьные дворы снова шумят.'),
    ('十一月黑暗，但并不安静：它歌唱、发光、庆祝。', 'Ноябрь тёмный, но не тихий: он поёт, светит и празднует.'),
    ('比赛售罄，RTL 现场直播。', 'Билеты распроданы; RTL ведёт прямую трансляцию.'),
    ('这里的纪念意味着：停下来、记住——并为和平与和解挺身而出。', 'Здесь память означает: остановиться, вспомнить — и отстаивать мир и примирение.'),
    ('周日，全国一片安静。', 'В воскресенье в стране тихо.'),
    ('FEHLERKLINIK · 纠错诊所', 'FEHLERKLINIK · Клиника ошибок'),
    ('学习者最常犯的四个错 · 先自己改，再看答案', 'Четыре самые частые ошибки учащихся · сначала исправьте, потом проверьте'),
    ('动词第二位：主语不在句首时，动词仍居第二。', 'Глагол — вторым: даже если подлежащее не первое, глагол остаётся вторым.'),
    ('halb zwölf = 十一点半（zwölf 之前）。', 'halb zwölf = 11.30, за полчаса до zwölf.'),
    ('Perfekt 中 Partizip II 放句末。', 'В Perfekt причастие прошедшего времени — в конец.'),
    ('ob 从句动词放句末。', 'В придаточном с ob глагол — в конец.'),
    ('IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.4)', 'IN DER NÄCHSTEN AUSGABE · Следующий номер (VOL.4)'),
]
rep_all("content7.py", C7)

# ================= content8.py =================
C8 = [
    ('ÜBUNGEN & ANTWORTEN · 练习与答案', 'ÜBUNGEN & ANTWORTEN · Упражнения и ответы'),
    ('SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方', 'SCHLUSSTEST · Итоговый тест · Alle Antworten unten auf dieser Seite — все ответы внизу этой страницы'),
    ('beginnt（第三人称单数）', 'beginnt (3-е лицо ед. ч.)'),
    ('bastelt（第三人称单数）', 'bastelt (3-е лицо ед. ч.)'),
    ('geht（第三人称单数）', 'geht (3-е лицо ед. ч.)'),
    ('singt（第三人称单数）', 'singt (3-е лицо ед. ч.)'),
    ('schaut（第三人称单数）', 'schaut (3-е лицо ед. ч.)'),
    ('sieht（第三人称单数）', 'sieht (3-е лицо ед. ч.)'),
    ('erzählt（第三人称单数）', 'erzählt (3-е лицо ед. ч.)'),
    ('A · LÜCKENTEXT · 完形填空', 'A · LÜCKENTEXT · Пропуски'),
    ('选项：', 'Варианты:'),
    ('B · WISSENSFRAGEN · 综合问答', 'B · WISSENSFRAGEN · Викторина'),
    ('狂欢季 11 点 11 分开幕', 'карнавал открывается в 11.11'),
    ('周五客战塞尔维亚', 'в гостях в Сербии в пятницу'),
    ('NFL 周日 15:30', 'NFL в воскресенье в 15.30'),
    ('纪念日 11 月 15 日', 'день памяти — 15 ноября'),
    ('家庭电力税 2.05 欧分', 'налог для домохозяйств — 2,05 цента'),
    ('主教练 11 月 5 日公布名单', 'тренер назовёт состав 5 ноября'),
    ('ZDF 13 点半直播纪念仪式', 'ZDF в прямом эфире с 13.30'),
    ('亡灵主日 11 月 22 日', 'Totensonntag — 22 ноября'),
    ('C · LESEVERSTEHEN · 阅读理解', 'C · LESEVERSTEHEN · Чтение'),
    ('周三做灯笼', 'делать фонарик в среду'),
    ('周五看德国队', 'смотреть Германию в пятницу'),
    ('D · SÄTZE BAUEN · 造句', 'D · SÄTZE BAUEN · Предложения'),
    ('时间状语，动词第二位', 'время, глагол — вторым'),
    ('主谓宾顺序', 'порядок подлежащее–сказуемое–дополнение'),
    ('时间状语开头，动词第二位', 'время — первым, глагол — вторым'),
    ('地点时间开头，动词第二位', 'место и время — первыми, глагол — вторым'),
    ('E · ÜBERSETZEN · 翻译', 'E · ÜBERSETZEN · Перевод'),
    ('狂欢节 11 点 11 分在科隆开幕。', 'Карнавал открывается в 11.11 в Кёльне.'),
    ('beginnen = 开始', 'beginnen = начинаться'),
    ('Der Karneval beginnt um 11.11 Uhr in Köln.（译成中文）', 'Der Karneval beginnt um 11.11 Uhr in Köln. (переведите на русский)'),
    ('我周三做一个灯笼。', 'Я делаю фонарик в среду.'),
    ('basteln = 制作', 'basteln = мастерить'),
    ('Ich bastle am Mittwoch eine Laterne.（译成中文）', 'Ich bastle am Mittwoch eine Laterne. (переведите на русский)'),
    ('学校 11 月 9 日又开学了。', 'Школа снова началась 9 ноября.'),
    ('wieder begonnen = 又开始', 'wieder begonnen = снова началась'),
    ('Die Schule hat am 9. November wieder begonnen.（译成中文）', 'Die Schule hat am 9. November wieder begonnen. (переведите на русский)'),
    ('看比赛 = das Spiel schauen', 'смотреть матч = das Spiel schauen'),
    ('"我周日看 NFL 比赛。（译成德语）", instr="翻译"', '"Я смотрю матч NFL в воскресенье. (переведите на немецкий)", instr="Переведите на немецкий"'),
    ('F · WÖRTER PAAREN · 词汇配对', 'F · WÖRTER PAAREN · Пары слов'),
    ('Mantel=斗篷 b', 'Mantel=плащ b'),
    ('Laterne=灯笼 a', 'Laterne=фонарик a'),
    ('Geisterspiel=空场比赛 d', 'Geisterspiel=матч-призрак d'),
    ('Versöhnung=和解 c', 'Versöhnung=примирение c'),
    ('singst（第二人称单数）', 'singst (2-е лицо ед. ч.)'),
    ('macht（第二人称复数）', 'macht (2-е лицо мн. ч.)'),
    ('essen（第一人称复数）', 'essen (1-е лицо мн. ч.)'),
    ('machst（第二人称单数）', 'machst (2-е лицо ед. ч.)'),
    ('schaue（第一人称单数）', 'schaue (1-е лицо ед. ч.)'),
    ('G · DIALOG · 对话补全', 'G · DIALOG · Диалог'),
    ('开放题 — 要点见写作框，范文在第 8 版写作框内', 'Открытое задание — следуйте пунктам в рамке для письма; образец — в рамке на этой странице'),
    ('按要点给分', 'Оценивается по перечисленным пунктам'),
    ('H · SCHREIBEN · 写作', 'H · SCHREIBEN · Письмо'),
    ('用德语写 80–100 词：《我的十一月的一周》。写清做什么手工、看哪几场比赛、和谁一起，并写一句关于圣马丁节或纪念日的话。', 'Напишите по-немецки, 80–100 слов: «Моя неделя в ноябре». Расскажите, что вы мастерите, какие матчи смотрите и с кем, — и добавьте одно предложение о Дне святого Мартина или о дне памяти.'),
    ('MUSTER · 范文（84 Wörter）', 'MUSTER · Образец (84 слова)'),
    ('ANTWORTEN · 全部答案与简析（第 1–8 版）', 'ANTWORTEN · Все ответы с пояснениями (стр. 1–8)'),
]
rep_all("content8.py", C8)

# ---------- P8 keys ----------
rep("content8.py", 'kf.para(f"— \u7b2c {pg} \u7248 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— СТРАНИЦА {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"\uff08{e[\'note\']}\uff09"',
    's += f"({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13.0, "sans", False, INK, 1.16, 9)', 1)

# ---------- generic value maps ----------
TYPEMAP = [('完成句子', 'Дополните предложение'), ('单选', 'Выбор ответа'), ('句型转换', 'Преобразуйте предложение'), ('词汇配对', 'Соедините пары'), ('判断对错', 'Верно или нет'), ('完形填空', 'Заполните пропуски'), ('造句', 'Составьте предложение'), ('对话补全', 'Дополните диалог'), ('翻译', 'Переведите'), ('写作', 'Письмо')]
INSTRMAP = [('instr="填空"', 'instr="Вставьте"'), ('instr="改写"', 'instr="Перепишите"'), ('instr="判断"', 'instr="Верно или нет"'), ('instr="造句"', 'instr="Составьте"'), ('instr="翻译"', 'instr="Переведите"'), ('instr="把词和释义配对"', 'instr="Соедините пары"')]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTRMAP + TYPEMAP:
        pth = os.path.join(BASE, f)
        n = open(pth, encoding="utf-8").read().count(old)
        if n == 0:
            LOG.append(f"{f}: 0x {old!r} (absent, skipped)")
        else:
            rep(f, old, new)

# ---------- leak check: no original Chinese literal may remain ----------
import re
CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
leaks = {}
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:
    for i, line in enumerate(open(os.path.join(BASE, f), encoding="utf-8"), 1):
        if CJK.search(line):
            leaks.setdefault(f, []).append((i, line.strip()[:80]))
print("CJK leaks:", leaks if leaks else "NONE")
assert not leaks, "CJK strings remain after transform"

print("\n".join(LOG))
print(f"TOTAL replacements: {len(LOG)}")
