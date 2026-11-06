# -*- coding: utf-8 -*-
"""W45 ES core -> ES x RU fan-out transform for the BUILD COPY ONLY.

Literal replacements only (README #17): whole lines or exact unique
literals, each with an asserted occurrence count (fail on zero). Spanish
target-language text is never a replacement target, except the two
furniture slots the shipped W43 ESxRU edition replaces in place (P1
masthead subtitle slot -> pairing badge; P1 top-strip Chinese segment ->
shipped Russian strapline) and the P8 E-section re-aiming (W43 ESxRU
KIT section 4 precedent: keys 137/138 become Russian sentences,
prompts 139/140 become Russian source sentences, Spanish keys stay).
Furniture strings are copied verbatim from the shipped W43 ESxRU
edition (files/weekly-report-es-ru/ SVG + KIT section 3), VOL.1->VOL.2
only. The word for the forbidden intermediary concept never appears in
the build copy, the edition, or this script: the explanation-layer
method is renamed bridge -> expl (W43 ESxRU precedent).
Value maps use bare text, never repr literals (README #18).
"""
import pathlib, sys

B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-ru-build')
C12, C34, C56, C7, C8, BS, RN = 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py', 'bslib4.py', 'render.py'
ALL = [C12, C34, C56, C7, C8]

def rep(files, old, new, expect=None):
    total = 0
    for fn in files:
        p = B / fn
        t = p.read_text(encoding='utf-8')
        c = t.count(old)
        total += c
        if c:
            p.write_text(t.replace(old, new), encoding='utf-8')
    if expect is not None and total != expect:
        print(f'COUNT MISMATCH: {old!r} found {total}, expected {expect}'); sys.exit(1)
    if total == 0:
        print(f'NOT FOUND: {old!r}'); sys.exit(1)
    print(f'  {total}x :: {old[:60]!r} -> {new[:60]!r}')
    return total

print('== repoint OUT + render names (copy only; core untouched) ==')
rep(ALL, 'weekly-report-w45-es-core', 'weekly-report-w45-es-ru', 5)
rep([RN], 'weekly-report-w45-es-core', 'weekly-report-w45-es-ru', 1)
rep([RN], 'La-Lucerna-VOL2-web.pdf', 'La-Lucerna-VOL2-RU-web.pdf', 1)
rep([RN], 'La-Lucerna-VOL2.pdf', 'La-Lucerna-VOL2-RU.pdf', 1)
rep([RN], 'Render the ES core edition', 'Render the ES x RU edition', 1)

print('== bslib4 furniture (shipped W43 ESxRU forms, VOL.2) ==')
rep([BS], '"La Lucerna · 西班牙语周报 VOL.2 · LUCERNA SPANISH WEEKLY"',
    '"La Lucerna · ИСПАНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА ИСПАНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ"', 1)
rep([BS], 'f"第 {n} 版 / 共 {total} 版"', 'f"Страница {n} из {total}"', 1)
rep([BS], '"译注｜" + s', '"Пояснение — " + s', 1)
rep([BS], 'def bridge(self, s, size=20.5, gap=9, fill=GREY):',
    'def expl(self, s, size=20.5, gap=9, fill=GREY):', 1)
rep(ALL, '.bridge(', '.expl(', 20)

print('== P1 masthead furniture (shipped W43 ESxRU forms) ==')
rep([C12], '"CADA SEMANA EN ESPAÑOL · 每周一期 · 读西班牙人正在读的西班牙语"',
    '"CADA SEMANA EN ESPAÑOL · КАЖДУЮ НЕДЕЛЮ · ИСПАНСКИЙ ГЛАЗАМИ ИСПАНИИ"', 1)
rep([C12], '"西 班 牙 语 周 报 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL"',
    '"ИСПАНСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL"', 1)
rep([C12], '"EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA", 19, "sans", False, GREY',
    '"ТЕКСТЫ НА ИСПАНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", 19.5, "sans", True, BRICK', 1)

def rep0(files, old, new):
    total = 0
    for fn in files:
        p = B / fn
        t = p.read_text(encoding='utf-8')
        c = t.count(old)
        total += c
        if c:
            p.write_text(t.replace(old, new), encoding='utf-8')
    return total

print('== exercise type names (scoped to ("LEVEL", "TYPE", ) ==')
# 完形单选 is not a prefix of 单选 under this scoping, but keep long-first anyway.
for old, new in [
    ('完形单选', 'Выбор в тексте'), ('完成句子', 'Дополните предложение'),
    ('单选', 'Выбор ответа'), ('判断对错', 'Верно или неверно'),
    ('造句', 'Составьте предложение'), ('句型转换', 'Преобразуйте предложение'),
    ('词汇配对', 'Соотнесите слова'), ('翻译', 'Перевод'), ('写作', 'Письмо'),
]:
    tot = 0
    for lv in ('A2', 'B1', 'B2'):
        # No trailing space: match_set calls break the line right after the
        # type comma, so a trailing-space pattern would miss them.
        tot += rep0(ALL, '("%s", "%s",' % (lv, old), '("%s", "%s",' % (lv, new))
    if tot == 0:
        print(f'NOT FOUND TYPE: {old}'); sys.exit(1)
    print(f'  TYPE TOTAL {tot}x :: {old} -> {new}')
rep([C8], '== "写作"', '== "Письмо"', 1)

print('== instruction labels (instr= scoped) ==')
for old, new in [
    ('instr="填空"', 'instr="Вставьте"'), ('instr="判断"', 'instr="В/НВ"'),
    ('instr="造句"', 'instr="Составьте предложение"'), ('instr="改写"', 'instr="Перепишите"'),
    ('instr="翻译"', 'instr="Перевод"'), ('instr="写作"', 'instr="Письмо"'),
    ('instr="把词和释义配对"', 'instr="Соотнесите"'),
]:
    rep(ALL, old, new)

print('== explanation layer: full-literal pairs (longest-first within overlap sets) ==')
PAIRS = [
    # --- P8 E-section re-aiming + writing apparatus (W43 ESxRU KIT sec 4) ---
    ('写作题（无唯一答案）；范文（84 词）见下。', 'Письменное задание (без единственного ответа); образец (84 слова) — ниже.'),
    ('（开放题，范文如下）', '(открытый вопрос — образец ниже)'),
    ('范文见本版 H 区（84 词）', 'образец — в разделе H этой страницы (84 слова)'),
    ('周一在九个自治区是假日。', 'Понедельник — выходной в девяти сообществах.'),
    ('周日我们看 NFL 和马竞–巴萨。', 'В воскресенье мы смотрим NFL и «Атлетико» — «Барса».'),
    ('伯纳乌承办一场 NFL 比赛。→ ___', '«Бернабеу» принимает матч NFL. → ___'),
    ('每个图表都必须标明来源。→ ___', 'Каждый график должен указывать источник. → ___'),
    ('对照原文', 'см. оригинал'),
    ('tener que = 必须', 'tener que = должен'),
    # --- P8 furniture ---
    ('EJERCICIOS Y RESPUESTAS · 练习与答案', 'EJERCICIOS Y RESPUESTAS · Упражнения и ответы'),
    ('第 8 版 · La gran prueba de la semana + todas las respuestas', 'Страница 8 · La gran prueba de la semana + todas las respuestas'),
    ('RESPUESTAS · 参考答案 — 按版面分页排列，找到题号即可', 'RESPUESTAS · Ответы — по страницам, ищите по номеру'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', 'К каждому заданию — короткое пояснение · ✓ — задание с образцом'),
    ('— PÁGINA {pg} —', '— СТРАНИЦА {pg} —'),
    # --- section / band heads ---
    ('LA NOTICIA · 头条', 'LA NOTICIA · Главная новость'),
    ('LA SEMANA EN CIFRAS · 数字看本周', 'LA SEMANA EN CIFRAS · В цифрах'),
    ('AHORA TÚ · 即学即练', 'AHORA TÚ · Теперь ты'),
    ('本周五大看点 · Para entender la semana', 'Пять главных тем · Para entender la semana'),
    ('五大看点，不编数字：全在本期里讲清。', 'Пять тем, без выдуманных цифр.'),
    ('EN ESTA EDICIÓN · 本期目录', 'EN ESTA EDICIÓN · В выпуске'),
    ('BREVES · 快讯', 'BREVES · Коротко'),
    ('QUIZ RELÁMPAGO · 闪电问答', 'QUIZ RELÁMPAGO · Блиц-викторина'),
    ('VIDA · 生活', 'VIDA · Жизнь'),
    ('CULTURA · 文化', 'CULTURA · Культура'),
    ('DEPORTE · 体育', 'DEPORTE · Спорт'),
    ('JUVENTUD · 青年', 'JUVENTUD · Молодёжь'),
    ('A FONDO · 深读', 'A FONDO · Разбор'),
    ('LENGUA · 语言', 'LENGUA · Язык'),
    ('ERRORES TÍPICOS · 常见错误', 'ERRORES TÍPICOS · Ошибки'),
    ('LA PALABRA · 本周生词', 'LA PALABRA · Слово недели'),
    ('LA PRÓXIMA SEMANA · 下期预告 (VOL.3)', 'LA PRÓXIMA SEMANA · Следующий выпуск (VOL.3)'),
    ('FRASES DE LA SEMANA · 本周金句（逐字摘自本期文章）', 'FRASES DE LA SEMANA · Фразы недели (дословно из статей выпуска)'),
    ('EL CALENDARIO · 本周日历', 'EL CALENDARIO · Календарь недели'),
    ('EL PLAN DEL PUENTE · 连休计划', 'EL PLAN DEL PUENTE · План на пуэнте'),
    ('LA SEMANA EUROPEA Y LA JORNADA 12 · 欧战周与联赛第 12 轮', 'LA SEMANA EUROPEA Y LA JORNADA 12 · Еврокубковая неделя и 12-й тур'),
    ('LOS DÍAS DE LA SEMANA · 这样说日期', 'LOS DÍAS DE LA SEMANA · Как называть даты'),
    ('EJERCICIOS · 第 2 版练习', 'EJERCICIOS · Упражнения страницы 2'),
    ('EJERCICIOS · 第 3 版练习', 'EJERCICIOS · Упражнения страницы 3'),
    ('EJERCICIOS · 第 4 版练习', 'EJERCICIOS · Упражнения страницы 4'),
    ('EJERCICIOS · 第 5 版练习', 'EJERCICIOS · Упражнения страницы 5'),
    ('EJERCICIOS · 第 6 版练习', 'EJERCICIOS · Упражнения страницы 6'),
    ('NIVEL A2 · El puente del lunes 2 · 11 月 2 日的连休', 'NIVEL A2 · El puente del lunes 2 · Пуэнте 2 ноября'),
    ('A2 → B1 · La semana pasada: tres noches de otoño · 上周的三个秋夜', 'A2 → B1 · La semana pasada: tres noches de otoño · Три осенние ночи прошлой недели'),
    ('NIVEL B1 · Europa primero, el domingo a las 21:00 · 欧战在先，周日晚九点', 'NIVEL B1 · Europa primero, el domingo a las 21:00 · Сначала Европа, в воскресенье в 21:00'),
    ('NIVEL B1 · La NFL en Madrid · NFL 来到马德里', 'NIVEL B1 · La NFL en Madrid · NFL в Мадриде'),
    ('NIVEL B2 · La vivienda decide la campaña · 住房决定选战', 'NIVEL B2 · La vivienda decide la campaña · Жильё решает кампанию'),
    ('语言聚焦 · Tres niveles, tres herramientas · 三个级别，三件工具', 'Фокус на языке · Tres niveles, tres herramientas · Три уровня, три инструмента'),
    # --- shared furniture sentences ---
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Ответы на странице 8 · Уровни перемешаны — ищите по номеру задания'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Прочитайте первую полосу и выберите правильный ответ · Ответы на странице 8'),
    ('¿Y TÚ? · 说说你自己', '¿Y TÚ? · А ты?'),
    ('距大选还有 27 天 · 住房决定选战', 'ДО ВЫБОРОВ 27 ДНЕЙ · ЖИЛЬЁ РЕШАЕТ КАМПАНИЮ'),
    ('本期头条 · 详见第 2、6 版', 'ГЛАВНАЯ ТЕМА · СМ. СТРАНИЦЫ 2 И 6'),
    ('lunes 2 – domingo 8 de noviembre · 11 月 2 日周一至 8 日周日', 'lunes 2 – domingo 8 de noviembre · понедельник 2 — воскресенье 8 ноября'),
    # --- P1 expl + number box + word note (longest-first where nested) ---
    ('讲解｜la cuenta atrás 倒计时 · disolver las Cortes 解散议会 · el decreto 法令 · la candidatura 候选人名单。',
     'Пояснение — la cuenta atrás = обратный отсчёт · disolver las Cortes = распустить парламент · el decreto = указ · la candidatura = кандидатура.'),
    ('27 — días faltan el lunes 2 para las elecciones del domingo 29（距 29 日大选 27 天）',
     '27 — días faltan el lunes 2 para las elecciones del domingo 29 (до выборов 29 ноября — 27 дней)'),
    ('9 — comunidades donde el lunes 2 de noviembre es fiesta（11 月 2 日放假的自治区）',
     '9 — comunidades donde el lunes 2 de noviembre es fiesta (9 сообществ, где 2 ноября — выходной)'),
    ('55,7 — % que cita la vivienda como el principal problema, según el CIS de octubre（CIS 十月数据）',
     '55,7 — % que cita la vivienda como el principal problema, según el CIS de octubre (CIS, октябрь)'),
    ('“竞选预热期”：正式竞选前的几周。', '«Предкампания»: недели перед официальной кампанией.'),
    # --- glosses (split on · : P2 5, P3 5, P4 5, P5 4 = 19) ---
    ('festivo 放假的 · el puente 连休 · la comunidad 自治区 · anochecer 天黑 · el horario de invierno 冬令时。',
     'festivo = выходной · el puente = длинные выходные · la comunidad = автономное сообщество · anochecer = темнеть · el horario de invierno = зимнее время.'),
    ('sobrio 克制的 · el homenaje 纪念表彰 · el disfraz 服装（化装） · el boniato 红薯 · el cementerio 墓地。',
     'sobrio = сдержанный · el homenaje = дань памяти · el disfraz = костюм (маскарадный) · el boniato = батат · el cementerio = кладбище.'),
    ('la jornada 轮次 · recortar la distancia 缩小分差 · recibir 主场迎战 · visitar 客场挑战 · el Metropolitano 马竞主场。',
     'la jornada = тур · recortar la distancia = сократить отставание · recibir = принимать дома · visitar = играть в гостях · el Metropolitano = стадион «Атлетико».'),
    ('el emparrillado 美式足球场（烤架形场地） · el himno 国歌 · el touchdown 达阵得分 · la calabaza 南瓜。',
     'el emparrillado = поле для американского футбола (в виде решётки) · el himno = гимн · el touchdown = тачдаун · la calabaza = тыква.'),
    # --- P2 calendar box ---
    ('Lunes 2 — puente en nueve comunidades; las candidaturas proclamadas llegan al BOE el martes 3（周一九地连休；周二《官方公报》公布正式候选名单）',
     'Lunes 2 — puente en nueve comunidades; las candidaturas proclamadas llegan al BOE el martes 3 (пуэнте в 9 сообществах; во вторник в BOE — утверждённые списки)'),
    ('Martes 3 — Champions: Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG（周二欧冠三场西甲球队比赛）',
     'Martes 3 — Champions: Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG (во вторник — три матча Лиги чемпионов с испанскими клубами)'),
    ('Miércoles 4 — Champions: AEK–Real Madrid, 18:45（周三皇马客场对雅典 AEK）',
     'Miércoles 4 — Champions: AEK–Real Madrid, 18:45 (в среду «Реал» в гостях у афинского АЕКа)'),
    ('Jueves 5 — Europa League: Real Sociedad–Lyon, 18:45（周四皇家社会欧联对里昂）',
     'Jueves 5 — Europa League: Real Sociedad–Lyon, 18:45 (в четверг «Реал Сосьедад» — «Лион» в Лиге Европы)'),
    ('Viernes 6 — Liga, jornada 12: Sevilla–Alavés, 21:00（周五联赛第 12 轮开球）',
     'Viernes 6 — Liga, jornada 12: Sevilla–Alavés, 21:00 (в пятницу старт 12-го тура: «Севилья» — «Алавес»)'),
    ('Sábado 7 — Valencia–Real Madrid, 21:00, en Mestalla（周六瓦伦西亚对皇马）',
     'Sábado 7 — Valencia–Real Madrid, 21:00, en Mestalla (в субботу «Валенсия» — «Реал» на «Месталье»)'),
    ('Domingo 8 — NFL en el Bernabéu, 15:30; Atlético–Barça, 21:00（周日 NFL 马德里站＋马竞对巴萨）',
     'Domingo 8 — NFL en el Bernabéu, 15:30; Atlético–Barça, 21:00 (в воскресенье NFL на «Бернабеу» и «Атлетико» — «Барса»)'),
    # --- P5 plan box ---
    ('1. El lunes 2: descanso y familia — o viaje, si tu comunidad hace puente（周一：休息陪家人；若你那里连休，就去旅行）',
     '1. El lunes 2: descanso y familia — o viaje, si tu comunidad hace puente (понедельник: отдых с семьёй; а если у вас пуэнте — путешествие)'),
    ('2. El sábado 7: Valencia–Real Madrid, 21:00, en Mestalla（周六晚：瓦伦西亚对皇马）',
     '2. El sábado 7: Valencia–Real Madrid, 21:00, en Mestalla (в субботу вечером «Валенсия» — «Реал»)'),
    ('3. El domingo 8, 15:30: la NFL en el Bernabéu（周日下午：NFL 马德里站）',
     '3. El domingo 8, 15:30: la NFL en el Bernabéu (в воскресенье днём NFL на «Бернабеу»)'),
    ('4. El domingo 8, 21:00: Atlético–Barça en el Metropolitano（周日晚：马竞对巴萨）',
     '4. El domingo 8, 21:00: Atlético–Barça en el Metropolitano (в воскресенье вечером «Атлетико» — «Барса» на «Метрополитано»)'),
    ('5. Y el lunes 9: vuelta a clase y al trabajo; la campaña empieza el viernes 13（返校返工；竞选 13 日开始）',
     '5. Y el lunes 9: vuelta a clase y al trabajo; la campaña empieza el viernes 13 (возвращение в школу и на работу; кампания стартует в пятницу, 13-го)'),
    # --- reader-letter prompts (¿Y TÚ? notes) ---
    ('11 月 2 日你那里放假吗？连休你做什么：旅行、休息还是看球？写两句西班牙语寄给编辑部。',
     'У вас 2 ноября выходной? Что вы делаете на пуэнте: путешествуете, отдыхаете или смотрите футбол? Напишите два предложения по-испански и пришлите в редакцию.'),
    ('你最喜欢哪一夜：29 日、31 日还是 1 日？31 日你吃了什么？写两句寄来。',
     'Какая ночь вам нравится больше: 29-го, 31-го или 1-го? Что вы ели 31-го? Напишите два предложения и пришлите нам.'),
    ('周日 21:00 你看哪一场？马竞主场谁赢？写两句西班牙语寄来。',
     'В воскресенье в 21:00 что вы смотрите? Кто выиграет на «Метрополитано»? Напишите два предложения по-испански и пришлите нам.'),
    ('你看过美式足球比赛吗？你更喜欢足球还是美式足球？写两句寄来。',
     'Вы когда-нибудь видели матч по американскому футболу? Что вам нравится больше: футбол или американский футбол? Напишите два предложения и пришлите нам.'),
    # --- bridges: longer instruction strings BEFORE bare substrings ---
    ('读第 2 版文章，选出正确答案。', 'Прочитайте текст страницы 2 и выберите правильный ответ.'),
    ('读第 3 版文章，判断对错。', 'Прочитайте текст страницы 3. Верно или неверно?'),
    ('读第 4 版文章，选出正确答案。', 'Прочитайте текст страницы 4 и выберите правильный ответ.'),
    ('读第 5 版文章，选出正确答案。', 'Прочитайте текст страницы 5 и выберите правильный ответ.'),
    ('用方框里的词填空。注意：有的词要变位。', 'Вставьте слова из рамки. Обратите внимание: некоторые слова нужно изменить по форме.'),
    ('用方框里的词填空：sondeo · muestra · indecisos · margen de error', 'Вставьте слова из рамки: sondeo · muestra · indecisos · margen de error'),
    ('用方框里的词填空。', 'Вставьте слова из рамки.'),
    ('用正确的日期形式补全句子。', 'Дополните предложения правильной формой даты.'),
    ('补全动词的现在时形式。', 'Дополните глагол в настоящем времени.'),
    ('看上面两张图，选出正确答案。', 'Посмотрите на два графика выше и выберите правильный ответ.'),
    ('选出正确答案。', 'Выберите правильный ответ.'),
    ('把词组成正确的句子。', 'Составьте из слов правильное предложение.'),
    ('用括号里词的比较级或 -ísimo 形式填空。', 'Вставьте сравнительную степень или форму на -ísimo слова в скобках.'),
    ('把句子改成过去时（pretérito indefinido）。', 'Перепишите предложения в прошедшем времени (pretérito indefinido).'),
    ('用 ir a + 原形动词改写句子，表示“将要”。', 'Перепишите предложения с ir a + инфинитив — значение «собираться».'),
    ('日期格式：el lunes 2 de noviembre；星期、月份小写；1 号说 el uno。', 'Формат даты: el lunes 2 de noviembre; дни недели и месяцы — со строчной буквы; 1-е число — el uno.'),
    ('比较级 más…que、tan…como；bueno→mejor、malo→peor；绝不说 más mejor。', 'Сравнение: más…que, tan…como; bueno→mejor, malo→peor; никогда не говорите más mejor.'),
    ('es necesario que、para que、ojalá 后用虚拟式；creo que 后用陈述式。', 'После es necesario que, para que, ojalá — сослагательное наклонение; после creo que — изъявительное.'),
    # --- P7 errors / word / disclosure (three disclosure facts kept) ---
    ('lunes 是单数，动词用 es。', 'lunes — единственное число, глагол es.'),
    ('mejor 本身就是比较级，不加 más。', 'mejor уже сравнительная степень, más не нужен.'),
    ('gente 是单数集合名词，动词用单数。', 'gente — собирательное существительное в единственном числе, глагол тоже.'),
    ('creo que 表肯定，用陈述式 es。', 'creo que выражает уверенность — изъявительное наклонение: es.'),
    ('precampaña = 竞选预热期：正式竞选前的几周。本期就是 precampaña；竞选 13 日周五开始。',
     'precampaña = предкампания: недели перед официальной кампанией. Весь выпуск — предкампания; кампания стартует в пятницу, 13-го.'),
    ('编辑部说明：截至本期截稿，未收到真实读者来信与第 8 版最佳作文，故本期登载编辑部示例信，承诺顺延至 VOL.3。欢迎来信！',
     'Примечание редакции: к сдаче номера настоящих писем читателей и лучших сочинений со страницы 8 не поступило, поэтому печатаем редакционный пример, а обещание переносится на VOL.3. Присылайте письма!'),
    # --- P7 quotes: glosses + page labels (labels are bare "Página N" below) ---
    ('名单已提交：现在各党开始撰写纲领。', 'Списки поданы: теперь партии пишут программы.'),
    ('11 月 2 日周一九个自治区放假，其他地区照常上班。', 'В понедельник 2 ноября в девяти сообществах выходной, в остальных — обычный рабочий день.'),
    ('三个节日，同一个秋夜。', 'Три праздника в одну осеннюю ночь.'),
    ('皇马在诺坎普 2–1 获胜：这是巴萨本赛季联赛首败。', '«Реал» выиграл на «Камп Ноу» 2–1: первое поражение «Барсы» в лиге в этом сезоне.'),
    ('伯纳乌把草皮换成烤架形球场：美式足球来到马德里。', '«Бернабеу» меняет газон на решётку: американский футбол приходит в Мадрид.'),
    ('住房是 55.7% 的西班牙人的首要问题。', 'Жильё — главная проблема для 55,7% испанцев.'),
    ('一次民调就是一张带误差的照片，拍于某一天。', 'Опрос — снимок с погрешностью, сделанный в конкретный день.'),
    ('11 月 8 日周日，马德里有两场约会：15:30 的 NFL 和 21:00 的马竞对巴萨。', 'В воскресенье 8 ноября у Мадрида две встречи: NFL в 15:30 и «Атлетико» — «Барса» в 21:00.'),
    ('Página 1', 'Страница 1'),
    ('Página 2', 'Страница 2'),
    ('Página 3', 'Страница 3'),
    ('Página 4', 'Страница 4'),
    ('Página 5', 'Страница 5'),
    ('Página 6', 'Страница 6'),
    # --- exercise notes: longer strings BEFORE their substrings ---
    ('大选在 11 月 29 日周日', 'выборы — в воскресенье, 29 ноября'),
    ('大选在 11 月 29 日', 'выборы — 29 ноября'),
    ('马竞–巴萨周日 21:00 开球', '«Атлетико» — «Барса» — в воскресенье в 21:00'),
    ('马竞–巴萨周日 21:00', '«Атлетико» — «Барса» — в воскресенье в 21:00'),
    ('NFL 马德里站周日 15:30 开球', 'NFL в Мадриде — в воскресенье в 15:30'),
    ('NFL 马德里站周日 15:30', 'NFL в Мадриде — в воскресенье в 15:30'),
    ('NFL 马德里站周日下午', 'NFL в Мадриде — в воскресенье днём'),
    ('诸圣节 11 月 1 日落在周日', 'День всех святых 1 ноября выпал на воскресенье'),
    ('诸圣节 11 月 1 日', 'День всех святых — 1 ноября'),
    ('诸圣节在 11 月 1 日，不是 10 月 31 日', 'День всех святых — 1 ноября, а не 31 октября'),
    ('acoger = 承办（伯纳乌承办 NFL）', 'acoger = принимать («Бернабеу» принимает NFL)'),
    ('acoger = 承办', 'acoger = принимать'),
    ('bueno 的比较级是 mejor（不用 más）', 'сравнительная степень от bueno — mejor (без más)'),
    ('bueno 的比较级是 mejor', 'сравнительная степень от bueno — mejor'),
    ('月份小写：noviembre', 'месяц со строчной буквы: noviembre'),
    ('月份小写', 'месяц — со строчной буквы'),
    ('时间在前，动词第二', 'время — сначала, глагол — вторым'),
    ('时间在前', 'время — сначала'),
    ('地点在前，动词第二', 'место — сначала, глагол — вторым'),
    ('动词第二位', 'глагол — на втором месте'),
    ('间接疑问用 si', 'косвенный вопрос — с si'),
    ('11 月 2 日周一', 'понедельник, 2 ноября'),
    ('11 月 8 日周日', 'воскресенье, 8 ноября'),
    ('29 日是周日', '29-е — воскресенье'),
    ('每月 1 号说 el uno', '1-е число — el uno'),
    ('el lunes → es（单数）', 'el lunes → es (единственное число)'),
    ('el lunes 2 de noviembre 连休', 'el lunes 2 de noviembre — пуэнте'),
    ('住房是选战的决定性议题', 'жильё решает исход кампании'),
    ('周一放假的自治区有 9 个', 'в понедельник выходной в 9 сообществах'),
    ('九个自治区周一放假', 'в девяти сообществах в понедельник выходной'),
    ('加泰罗尼亚周一是工作日', 'в Каталонии понедельник — рабочий день'),
    ('冬令时第二周，天黑得早', 'вторая неделя зимнего времени: темнеет рано'),
    ('周二欧冠三场西甲球队比赛', 'во вторник — три матча Лиги чемпионов с испанскими клубами'),
    ('周日 21:00 马竞–巴萨', 'в воскресенье в 21:00 — «Атлетико» — «Барса»'),
    ('周日下午还有 NFL 马德里站', 'в воскресенье днём — NFL в Мадриде'),
    ('周日上演马竞–巴萨', 'в воскресенье — «Атлетико» — «Барса»'),
    ('周日家属去墓地献花', 'в воскресенье семьи несут цветы на кладбища'),
    ('三夜之后周一有人连休有人上班', 'после трёх ночей в понедельник одни отдыхают, другие работают'),
    ('DANA 纪念活动在 10 月 29 日周四', 'мероприятия памяти DANA — в четверг, 29 октября'),
    ('DANA 纪念是 2024 年风暴两周年', 'память о шторме DANA 2024 года, два года спустя'),
    ('Castanyada 吃烤栗子、红薯和 panellets', 'на Кастаньяду едят жареные каштаны, батат и panellets'),
    ('Castanyada 吃 panellets', 'на Кастаньяду едят panellets'),
    ('Castanyada 在加泰罗尼亚', 'Кастаньяда — в Каталонии'),
    ('Samaín 是加利西亚古节，不是万圣节译名', 'Самайн — древний галисийский праздник, а не перевод Хэллоуина'),
    ('Samaín 是加利西亚古老节日', 'Самайн — древний галисийский праздник'),
    ('给逝者带花 flores', 'нести цветы усопшим: flores'),
    ('cementerio = 墓地', 'cementerio = кладбище'),
    ('castañas asadas 烤栗子', 'castañas asadas = жареные каштаны'),
    ('disfraz = 化装服装', 'disfraz = маскарадный костюм'),
    ('actos de memoria 纪念活动', 'actos de memoria = мероприятия памяти'),
    ('皇马 2–1 赢下国家德比', '«Реал» выиграл Класико 2–1'),
    ('姆巴佩进了两球', 'Мбаппе забил два гола'),
    ('jornada=轮次 b', 'jornada = тур (b)'),
    ('recibir=主场迎战 a', 'recibir = играть дома (a)'),
    ('visitar=客场挑战 d', 'visitar = играть в гостях (d)'),
    ('recortar=缩小分差 c', 'recortar = сократить отставание (c)'),
    ('más + importante（马竞–巴萨更重要）', 'más + importante («Атлетико» — «Барса» важнее)'),
    ('muchísimos partidos 比赛很多', 'muchísimos partidos = очень много матчей'),
    ('malo 的比较级是 peor', 'сравнительная степень от malo — peor'),
    ('ir 的过去时是 fueron', 'прошедшее время от ir — fueron'),
    ('孟加拉虎对猎鹰', '«Бенгалс» против «Фэлконс»'),
    ('西班牙国歌由吉他手演奏', 'гимн Испании исполняет гитарист'),
    ('首场 NFL 伯纳乌赛在 2025 年 11 月 16 日', 'первый матч NFL на «Бернабеу» — 16 ноября 2025 года'),
    ('美式足球用手打、四次进攻', 'в американский футбол играют руками, за четыре попытки'),
    ('estadio = 体育场', 'estadio = стадион'),
    ('himno = 国歌', 'himno = гимн'),
    ('acoger 变位 → acoge', 'acoger → acoge'),
    ('touchdown = 达阵得分', 'touchdown = тачдаун'),
    ('calabaza = 南瓜', 'calabaza = тыква'),
    ('NFL 马德里站是伯纳乌第二场 NFL 比赛', 'это второй матч NFL на «Бернабеу»'),
    ('美国国歌由 Momsen 演唱，不是 Sáinz-Villegas', 'гимн США поёт Momsen, а не Sáinz-Villegas'),
    ('万圣节之夜在周六 31 日', 'ночь Хэллоуина — в субботу, 31-го'),
    ('CIS 里 PSOE 第一（34%）', 'по CIS первый — PSOE (34%)'),
    ('CIS 里 PP 22,2%', 'у PP по CIS — 22,2%'),
    ('住房是首要问题（55,7%）', 'жильё — главная проблема (55,7%)'),
    ('调查在 10 月 1–6 日进行', 'опрос проведён 1–6 октября'),
    ('本报只刊登 CIS 这一组数据并注明来源日期', 'публикуем только ряд CIS, с источником и датой'),
    ('10 月 2 日议会否决两项住房法令', '2 октября парламент отклонил два жилищных указа'),
    ('10 月 5 日解散议会并召集大选', '5 октября парламент распущен, выборы назначены'),
    ('民调是带误差的具体某天的照片', 'опрос — снимок с погрешностью, сделанный в конкретный день'),
    ('竞选 11 月 13 日开始', 'кампания начинается 13 ноября'),
    ('es posible que + 虚拟式 tenga', 'es posible que + сослагательное наклонение: tenga'),
    ('es importante que + 虚拟式 sea', 'es importante que + сослагательное наклонение: sea'),
    ('para que + 虚拟式（目的）', 'para que + сослагательное наклонение (цель)'),
    ('Aunque 后接陈述式（已知事实）', 'после Aunque — изъявительное наклонение (известный факт)'),
    ('sondeo = 民调', 'sondeo = опрос'),
    ('muestra = 样本（5.025 人）', 'muestra = выборка (5.025 человек)'),
    ('indecisos = 未决定者', 'indecisos = неопределившиеся'),
    ('margen de error = 误差范围', 'margen de error = погрешность'),
    ('El Bernabéu ___ (原形 acoger) un partido de la NFL.', 'El Bernabéu ___ (infinitivo: acoger) un partido de la NFL.'),
    ('más + cara（房价更高）', 'más + cara (жильё дороже)'),
    ('tan + alta + como（同样高）', 'tan + alta + como (так же высоко)'),
    ('más mejor 是错误说法', 'más mejor — неправильно'),
    ('es necesario que + 虚拟式 baje', 'es necesario que + сослагательное наклонение: baje'),
    ('para que + 虚拟式 sea', 'para que + сослагательное наклонение: sea'),
    ('creo que + 陈述式 es', 'creo que + изъявительное наклонение: es'),
    ('ojalá + 虚拟式：baje', 'ojalá + сослагательное наклонение: baje'),
    ('ganó 2–1 = 以 2–1 获胜', 'ganó 2–1 = победа 2–1'),
    ('marcar dos goles = 进两球', 'marcar dos goles = забить два гола'),
    ('primera derrota liguera = 联赛首败', 'primera derrota liguera = первое поражение в лиге'),
    ('recortar = 缩小分差', 'recortar = сократить отставание'),
    ('el emparrillado = 美式足球场', 'el emparrillado = поле для американского футбола'),
    ('CIS 十月调查：住房 55,7%', 'опрос CIS за октябрь: жильё — 55,7%'),
    ('马德里在放假名单里', 'Мадрид — в списке выходного дня'),
    ('Ana 只看 NFL；晚上看马竞–巴萨的是 Pablo', 'Ana смотрит только NFL; «Атлетико» — «Барса» вечером смотрит Pablo'),
    ('标题概括两地对比', 'заголовок передаёт контраст двух городов'),
    ('主语 + 动词 + 地点', 'подлежащее + глагол + место'),
    ('a las nueve = 在九点', 'a las nueve = в девять часов'),
    ('疑问词在句首', 'вопросительное слово — в начале'),
    ('sondeo=民调 c', 'sondeo = опрос (c)'),
    ('muestra=样本 d', 'muestra = выборка (d)'),
    ('margen de error=误差范围 b', 'margen de error = погрешность (b)'),
    ('junta electoral=选举委员会 a', 'junta electoral = избирательная комиссия (a)'),
    ('alquiler = 租金', 'alquiler = аренда'),
    ('tres habitaciones = 三居室', 'tres habitaciones = три комнаты'),
    ('¿cuánto cuesta? 多少钱', '¿cuánto cuesta? = сколько стоит?'),
    ('firmar = 签（合同）', 'firmar = подписать (договор)'),
    ('mudanza = 搬家', 'mudanza = переезд'),
    ('puente=三天连休 b', 'puente = трёхдневные выходные (b)'),
    ('festivo=放假的 a', 'festivo = выходной (a)'),
    ('anochecer=天黑 c', 'anochecer = темнеть (c)'),
    ('comunidad=自治区 d', 'comunidad = автономное сообщество (d)'),
]
for old, new in PAIRS:
    rep(ALL, old, new)
print('TRANSFORM DONE')
