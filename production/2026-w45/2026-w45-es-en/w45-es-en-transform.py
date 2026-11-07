# -*- coding: utf-8 -*-
"""W45 ES core -> ES x EN fan-out transform for the BUILD COPY ONLY.

Literal replacements only (README #17): each (files, old, new) asserts the
total occurrence count across the listed files before replacing. Spanish
target-language text is never a replacement target; only the explanation
layer (Chinese notes/bridges/titles/furniture) and the P8 E-section
redirection (W43 ESxEN KIT ruling 1) change.
"""
import pathlib, sys

B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-en-build')
C12, C34, C56, C7, C8, BS = 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py', 'bslib4.py'
ALL = [C12, C34, C56, C7, C8]

def rep(files, old, new, expect=None, allow_zero=False):
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
    if total == 0 and not allow_zero:
        print(f'NOT FOUND: {old!r}'); sys.exit(1)

# ---------- repoint OUT + render names (copy only; core untouched) ----------
rep(ALL, 'weekly-report-w45-es-core', 'weekly-report-w45-es-en', 5)
rep(['render.py'], 'weekly-report-w45-es-core', 'weekly-report-w45-es-en', 1)
rep(['render.py'], 'La-Lucerna-VOL2-web.pdf', 'La-Lucerna-VOL2-EN-web.pdf', 1)
rep(['render.py'], 'La-Lucerna-VOL2.pdf', 'La-Lucerna-VOL2-EN.pdf', 1)
rep(['render.py'], 'Render the ES core edition', 'Render the ES x EN edition', 1)

# ---------- bslib4 furniture ----------
rep([BS], '"La Lucerna · 西班牙语周报 VOL.2 · LUCERNA SPANISH WEEKLY"',
    '"La Lucerna · Spanish Weekly VOL.2 · Text in Spanish · Explanations in English"', 1)
rep([BS], 'f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} of {total}"', 1)
rep([BS], '"译注｜" + s', '"Note | " + s', 1)

# ---------- global explanation-layer vocab (W43 ESxEN precedents) ----------
# NOTE: '完形单选' BEFORE '单选' (substring), and the P8 writing bridge
# BEFORE the global '写作' replacement (it contains '写作' as substring).
rep([C8], '写作题（无唯一答案）；范文（84 词）见下。',
    'A writing task (no single right answer); the model text (84 words) follows.', 1)
for old, new in [
    ('完形单选', 'Cloze choice'), ('完成句子', 'Sentence completion'),
    ('单选', 'Multiple choice'),
    ('判断对错', 'True or false'), ('造句', 'Sentence building'),
    ('句型转换', 'Sentence transformation'), ('词汇配对', 'Vocabulary matching'),
    ('翻译', 'Translation'), ('写作', 'Writing'),
]:
    # Type names are the 2nd positional arg: only match ("<level>", "<typ>",
    # so instr="..." values and bridge sentences containing the same words
    # (e.g. bridge "读第 3 版文章，判断对错。") are never touched.
    for lv in ('A2', 'B1', 'B2'):
        rep(ALL, '("%s", "%s", ' % (lv, old), '("%s", "%s", ' % (lv, new), allow_zero=True)
# P8 answer-code type check (paired with the typ translation; dash format untouched)
rep([C8], '== "写作"', '== "Writing"', 1)
rep(ALL, 'instr="填空"', 'instr="Fill in"')
rep(ALL, 'instr="判断"', 'instr="True or false"')
rep(ALL, 'instr="造句"', 'instr="Build the sentence"')
rep(ALL, 'instr="改写"', 'instr="Rewrite"')
rep(ALL, 'instr="翻译"', 'instr="Translate"')
rep(ALL, 'instr="写作"', 'instr="Write"')
rep(ALL, 'instr="把词和释义配对"', 'instr="Match word to definition"')
rep(ALL, '答案见第 8 版 · 题目可跨级混排，按题号找答案',
    'Answers on page 8 · Levels are mixed — find answers by number', 5)
rep(ALL, '¿Y TÚ? · 说说你自己', '¿Y TÚ? · Over to you', 4)
rep([C12], 'EJERCICIOS · 第 2 版练习', 'EJERCICIOS · Page 2 exercises', 1)
rep([C34], 'EJERCICIOS · 第 3 版练习', 'EJERCICIOS · Page 3 exercises', 1)
rep([C34], 'EJERCICIOS · 第 4 版练习', 'EJERCICIOS · Page 4 exercises', 1)
rep([C56], 'EJERCICIOS · 第 5 版练习', 'EJERCICIOS · Page 5 exercises', 1)
rep([C56], 'EJERCICIOS · 第 6 版练习', 'EJERCICIOS · Page 6 exercises', 1)
rep([C34], 'CULTURA · 文化', 'CULTURA · Culture', 1)
rep([C34], 'DEPORTE · 体育', 'DEPORTE · Sport', 1)
rep([C56], 'JUVENTUD · 青年', 'JUVENTUD · Youth', 1)
rep([C56], 'A FONDO · 深读', 'A FONDO · In depth', 1)
rep([C7], 'LENGUA · 语言', 'LENGUA · Language focus', 1)
rep([C8], 'EJERCICIOS Y RESPUESTAS · 练习与答案', 'EJERCICIOS Y RESPUESTAS · Exercises and answers', 1)

print('PART 1 OK')

# ---------- content12: P1 ----------
rep([C12], 'CADA SEMANA EN ESPAÑOL · 每周一期 · 读西班牙人正在读的西班牙语',
    'CADA SEMANA EN ESPAÑOL · REAL SPANISH, EVERY WEEK', 1)
rep([C12], '西 班 牙 语 周 报 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL',
    'SPANISH WEEKLY · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL', 1)
rep([C12], 'p.text(975, 372, "EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA", 19, "sans", False, GREY, anchor="middle")',
    'p.text(975, 372, "TEXT IN SPANISH · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 19.5, "sans", True, BRICK, anchor="middle")', 1)
rep([C12], '距大选还有 27 天 · 住房决定选战', '27 DAYS TO THE ELECTION · HOUSING DECIDES THE CAMPAIGN', 1)
rep([C12], '本期头条 · 详见第 2、6 版', "THIS ISSUE'S TOP STORY · SEE PAGES 2 AND 6", 1)
rep([C12], 'LA NOTICIA · 头条', 'LA NOTICIA · Top story', 1)
rep([C12], 'f.bridge("讲解｜la cuenta atrás 倒计时 · disolver las Cortes 解散议会 · el decreto 法令 · la candidatura 候选人名单。")',
    'f.bridge("Notes | la cuenta atrás — the countdown · disolver las Cortes — to dissolve parliament · el decreto — a decree · la candidatura — a candidacy.")', 1)
rep([C12], 'LA SEMANA EN CIFRAS · 数字看本周', 'LA SEMANA EN CIFRAS · Numbers', 1)
rep([C12], '（距 29 日大选 27 天）', '(27 days to the 29 November election)', 1)
rep([C12], '（11 月 2 日放假的自治区）', '(communities with a holiday on 2 November)', 1)
rep([C12], '（CIS 十月数据）', '(CIS, October)', 1)
rep([C12], 'AHORA TÚ · 即学即练', 'AHORA TÚ · Now you try', 1)
rep([C12], '"las listas ya están presentadas; ahora se escriben los programas"',
    '"the lists are in; now the programmes are being written"', 1)
rep([C12], '"大选在 11 月 29 日周日"', '"the election is on Sunday 29 November"', 1)
rep([C12], '"住房是选战的决定性议题"', '"housing decides the campaign"', 1)
rep([C12], '"周一放假的自治区有 9 个"', '"nine communities have Monday off"', 2)
rep([C12], '"马竞–巴萨周日 21:00 开球"', '"Atlético–Barça kicks off Sunday at 21:00"', 1)
rep([C12], '"NFL 马德里站周日 15:30 开球"', '"the NFL comes to the Bernabéu Sunday at 15:30"', 1)
rep([C12], '本周五大看点 · Para entender la semana', 'Five keys · Para entender la semana', 1)
rep([C12], '五大看点，不编数字：全在本期里讲清。', 'Five keys, no invented numbers — all explained in this issue.', 1)
rep([C12], 'EN ESTA EDICIÓN · 本期目录', 'EN ESTA EDICIÓN · In this issue', 1)
rep([C12], '“竞选预热期”：正式竞选前的几周。', 'The pre-campaign: the weeks before the official campaign begins.', 1)
rep([C12], 'BREVES · 快讯', 'BREVES · News in brief', 1)
rep([C12], 'QUIZ RELÁMPAGO · 闪电问答', 'QUIZ RELÁMPAGO · Lightning quiz', 1)
rep([C12], '读头版，选出正确答案 · 答案见第 8 版', 'Read the front page and choose · Answers on page 8', 1)
rep([C12], '"大选在 11 月 29 日"', '"the election is on 29 November"', 2)
rep([C12], '"NFL 马德里站周日下午"', '"the NFL comes to the Bernabéu on Sunday afternoon"', 1)
rep([C12], '"马竞–巴萨周日 21:00"', '"Atlético–Barça kicks off Sunday at 21:00"', 1)

# ---------- content12: P2 ----------
rep([C12], 'VIDA · 生活', 'VIDA · Life', 1)
rep([C12], 'NIVEL A2 · El puente del lunes 2 · 11 月 2 日的连休',
    'NIVEL A2 · El puente del lunes 2 · The 2 November long weekend', 1)
rep([C12], 'EL CALENDARIO · 本周日历', 'EL CALENDARIO · This week', 1)
rep([C12], '（周一九地连休；周二《官方公报》公布正式候选名单）',
    '(Monday: the long weekend in nine communities; Tuesday: the BOE publishes the official candidate lists)', 1)
rep([C12], '（周二欧冠三场西甲球队比赛）', '(Tuesday: three Spanish clubs in the Champions League)', 1)
rep([C12], '（周三皇马客场对雅典 AEK）', '(Wednesday: Real Madrid away at AEK Athens)', 1)
rep([C12], '（周四皇家社会欧联对里昂）', '(Thursday: Real Sociedad vs Lyon in the Europa League)', 1)
rep([C12], '（周五联赛第 12 轮开球）', '(Friday: matchday 12 kicks off)', 1)
rep([C12], '（周六瓦伦西亚对皇马）', '(Saturday: Valencia vs Real Madrid)', 1)
rep([C12], '（周日 NFL 马德里站＋马竞对巴萨）', '(Sunday: the NFL in Madrid + Atlético vs Barça)', 1)
rep([C12], 'f.gloss("festivo 放假的 · el puente 连休 · la comunidad 自治区 · anochecer 天黑 · el horario de invierno 冬令时。")',
    'f.gloss("festivo — a public holiday (adj.) · el puente — a long weekend · la comunidad — an autonomous community · anochecer — nightfall, to get dark · el horario de invierno — winter time.")', 1)
rep([C12], '11 月 2 日你那里放假吗？连休你做什么：旅行、休息还是看球？写两句西班牙语寄给编辑部。',
    'Is Monday 2 November a holiday where you live? What do you do with the long weekend: travel, rest or watch football? Write two sentences in Spanish and send them to the editors.', 2)
rep([C12], 'LOS DÍAS DE LA SEMANA · 这样说日期', 'LOS DÍAS DE LA SEMANA · Saying the date', 1)
rep([C12], 'lunes 2 – domingo 8 de noviembre · 11 月 2 日周一至 8 日周日',
    'lunes 2 – domingo 8 de noviembre · Monday 2 to Sunday 8 November', 1)
rep([C12], '用正确的日期形式补全句子。', 'Complete the sentences with the right date form.', 1)
rep([C12], '补全动词的现在时形式。', 'Complete the verbs in the present tense.', 1)
rep([C12], '读第 2 版文章，选出正确答案。', 'Read the page 2 article and choose the correct answer.', 1)
rep([C12], '"11 月 2 日周一"', '"Monday 2 November"', 1)
rep([C12], '"11 月 8 日周日"', '"Sunday 8 November"', 1)
rep([C12], '"每月 1 号说 el uno"', '"the 1st of the month is el uno"', 1)
rep([C12], '"月份小写"', '"months are lower case"', 1)
rep([C12], '"el lunes → es（单数）"', '"el lunes → es (singular)"', 1)
rep([C12], '"todos → preguntan"', '"todos → preguntan (they ask)"', 1)
rep([C12], '"anochecer → anochece"', '"anochecer → anochece (it gets dark)"', 1)
rep([C12], '"nosotros → descansamos"', '"nosotros → descansamos (we rest)"', 1)
rep([C12], '"el fin de semana → dura"', '"el fin de semana → dura (it lasts)"', 1)
rep([C12], '"九个自治区周一放假"', '"nine communities have Monday off"', 1)
rep([C12], '"诸圣节 11 月 1 日落在周日"', '"All Saints\' Day, 1 November, fell on a Sunday"', 1)
rep([C12], '"加泰罗尼亚周一是工作日"', '"in Catalonia Monday is a working day"', 1)
rep([C12], '"冬令时第二周，天黑得早"', '"the second week of winter time: it gets dark early"', 1)
rep([C12], '"puente=三天连休 b"', '"puente = a three-day long weekend — b"', 1)
rep([C12], '"festivo=放假的 a"', '"festivo = a public holiday — a"', 1)
rep([C12], '"anochecer=天黑 c"', '"anochecer = to get dark — c"', 1)
rep([C12], '"comunidad=自治区 d"', '"comunidad = an autonomous community — d"', 1)

print('PART 2 OK')

# ---------- content34: P3 ----------
rep([C34], 'A2 → B1 · La semana pasada: tres noches de otoño · 上周的三个秋夜',
    'A2 → B1 · La semana pasada: tres noches de otoño · Last week\'s three autumn nights', 1)
rep([C34], 'f.gloss("sobrio 克制的 · el homenaje 纪念表彰 · el disfraz 服装（化装） · el boniato 红薯 · el cementerio 墓地。")',
    'f.gloss("sobrio — restrained, sober · el homenaje — a tribute · el disfraz — a costume · el boniato — a sweet potato · el cementerio — a cemetery.")', 1)
rep([C34], '你最喜欢哪一夜：29 日、31 日还是 1 日？31 日你吃了什么？写两句寄来。',
    'Which night do you like best: the 29th, the 31st or the 1st? And what did you eat on the 31st? Write two sentences and send them in.', 2)
rep([C34], '读第 3 版文章，判断对错。', 'Read the page 3 article: true or false?', 1)
rep([C34], '用方框里的词填空。', 'Fill the gaps with the words in the box.', 1)
rep([C34], 'e.bridge("选出正确答案。")', 'e.bridge("Choose the correct answer.")', 1)
rep([C34], '把词组成正确的句子。', 'Put the words in order to make a sentence.', 1)
rep([C34], '"DANA 纪念活动在 10 月 29 日周四"', '"the DANA memorial events were on Thursday 29 October"', 1)
rep([C34], '"Castanyada 吃烤栗子、红薯和 panellets"', '"roasted chestnuts, sweet potatoes and panellets at the Castanyada"', 1)
rep([C34], '"Samaín 是加利西亚古节，不是万圣节译名"', '"the Samaín is an old Galician festival, not a name for Halloween"', 1)
rep([C34], '"诸圣节在 11 月 1 日，不是 10 月 31 日"', '"All Saints\' Day is on 1 November, not 31 October"', 1)
rep([C34], '"周日家属去墓地献花"', '"on Sunday families took flowers to the cemeteries"', 1)
rep([C34], '"给逝者带花 flores"', '"flores = flowers, taken to the dead"', 1)
rep([C34], '"cementerio = 墓地"', '"cementerio = cemetery"', 1)
rep([C34], '"castañas asadas 烤栗子"', '"castañas asadas = roasted chestnuts"', 1)
rep([C34], '"disfraz = 化装服装"', '"disfraz = costume"', 1)
rep([C34], '"actos de memoria 纪念活动"', '"actos de memoria = memorial events"', 1)
rep([C34], '"DANA 纪念是 2024 年风暴两周年"', '"the DANA memorial marked two years since the 2024 storm"', 1)
rep([C34], '"Castanyada 在加泰罗尼亚"', '"the Castanyada is in Catalonia"', 1)
rep([C34], '"Samaín 是加利西亚古老节日"', '"the Samaín is a very old Galician festival"', 1)
rep([C34], '"三夜之后周一有人连休有人上班"', '"after the three nights, some have the long weekend on Monday and others work"', 1)
rep([C34], '"动词第二位"', '"the verb comes second"', 1)
rep([C34], '"时间在前，动词第二"', '"time first, the verb second"', 1)
rep([C34], '"地点在前，动词第二"', '"place first, the verb second"', 1)
rep([C34], '"间接疑问用 si"', '"reported questions use si"', 1)

# ---------- content34: P4 ----------
rep([C34], 'NIVEL B1 · Europa primero, el domingo a las 21:00 · 欧战在先，周日晚九点',
    'NIVEL B1 · Europa primero, el domingo a las 21:00 · Europe first, Sunday at 21:00', 1)
rep([C34], 'f.gloss("la jornada 轮次 · recortar la distancia 缩小分差 · recibir 主场迎战 · visitar 客场挑战 · el Metropolitano 马竞主场。")',
    'f.gloss("la jornada — a round of matches · recortar la distancia — to cut the gap · recibir — to play at home · visitar — to play away · el Metropolitano — Atlético\'s stadium.")', 1)
rep([C34], '周日 21:00 你看哪一场？马竞主场谁赢？写两句西班牙语寄来。',
    'On Sunday at 21:00, which do you watch? Who wins at the Metropolitano? Write two sentences in Spanish and send them in.', 2)
rep([C34], 'LA SEMANA EUROPEA Y LA JORNADA 12 · 欧战周与联赛第 12 轮',
    'LA SEMANA EUROPEA Y LA JORNADA 12 · The European week and matchday 12', 1)
rep([C34], '读第 4 版文章，选出正确答案。', 'Read the page 4 article and choose the correct answer.', 1)
rep([C34], '"皇马 2–1 赢下国家德比"', '"Real Madrid won El Clásico 2–1"', 1)
rep([C34], '"姆巴佩进了两球"', '"Mbappé scored both goals"', 1)
rep([C34], '"周二欧冠三场西甲球队比赛"', '"three Spanish clubs play in the Champions League on Tuesday"', 1)
rep([C34], '"周日 21:00 马竞–巴萨"', '"Atlético–Barça: Sunday, 21:00"', 1)
rep([C34], '"周日下午还有 NFL 马德里站"', '"on Sunday afternoon there is also the NFL in Madrid"', 1)
rep([C34], '"jornada=轮次 b"', '"jornada = a round of matches — b"', 1)
rep([C34], '"recibir=主场迎战 a"', '"recibir = to play at home — a"', 1)
rep([C34], '"visitar=客场挑战 d"', '"visitar = to play away — d"', 1)
rep([C34], '"recortar=缩小分差 c"', '"recortar = to cut the gap — c"', 1)
rep([C34], '用括号里词的比较级或 -ísimo 形式填空。',
    'Fill the gaps with the comparative or -ísimo form of the word in brackets.', 1)
rep([C34], '"más + importante（马竞–巴萨更重要）"', '"más + importante (Atlético–Barça matters more)"', 1)
rep([C34], '"muchísimos partidos 比赛很多"', '"muchísimos partidos = very, very many matches"', 1)
rep([C34], '"malo 的比较级是 peor"', '"the comparative of malo is peor"', 1)
rep([C34], '"bueno 的比较级是 mejor"', '"the comparative of bueno is mejor"', 1)
rep([C34], '把句子改成过去时（pretérito indefinido）。', 'Put the sentences into the past (pretérito indefinido).', 1)
rep([C34], '"ganar → ganó"', '"ganar → ganó (he won)"', 1)
rep([C34], '"marcar → marcó"', '"marcar → marcó (he scored)"', 1)
rep([C34], '"perder → perdió"', '"perder → perdió (they lost)"', 1)
rep([C34], '"recortar → recortó"', '"recortar → recortó (he cut)"', 1)
rep([C34], '"ir 的过去时是 fueron"', '"ir in the past is fueron (they went)"', 1)

print('PART 3 OK')

# ---------- content56: P5 ----------
rep([C56], 'NIVEL B1 · La NFL en Madrid · NFL 来到马德里',
    'NIVEL B1 · La NFL en Madrid · The NFL comes to Madrid', 1)
rep([C56], 'EL PLAN DEL PUENTE · 连休计划', 'EL PLAN DEL PUENTE · The long-weekend plan', 1)
rep([C56], '（周一：休息陪家人；若你那里连休，就去旅行）',
    '(Monday: rest with family — or travel, if your community has the long weekend)', 1)
rep([C56], '（周六晚：瓦伦西亚对皇马）', '(Saturday evening: Valencia vs Real Madrid)', 1)
rep([C56], '（周日下午：NFL 马德里站）', '(Sunday afternoon: the NFL in Madrid)', 1)
rep([C56], '（周日晚：马竞对巴萨）', '(Sunday evening: Atlético vs Barça)', 1)
rep([C56], '（返校返工；竞选 13 日开始）', '(back to school and work; the campaign starts on the 13th)', 1)
rep([C56], 'f.gloss("el emparrillado 美式足球场（烤架形场地） · el himno 国歌 · el touchdown 达阵得分 · la calabaza 南瓜。")',
    'f.gloss("el emparrillado — the gridiron (the American football field) · el himno — an anthem · el touchdown — a touchdown · la calabaza — a pumpkin.")', 1)
rep([C56], '你看过美式足球比赛吗？你更喜欢足球还是美式足球？写两句寄来。',
    'Have you ever watched an American football game? Which do you like better: football or American football? Write two sentences and send them in.', 2)
rep([C56], '读第 5 版文章，选出正确答案。', 'Read the page 5 article and choose the correct answer.', 1)
rep([C56], '"NFL 马德里站周日 15:30"', '"the NFL in Madrid: Sunday, 15:30"', 1)
rep([C56], '"孟加拉虎对猎鹰"', '"Bengals vs Falcons"', 1)
rep([C56], '"西班牙国歌由吉他手演奏"', '"the Spanish anthem is played by a guitarist"', 1)
rep([C56], '"首场 NFL 伯纳乌赛在 2025 年 11 月 16 日"', '"the first NFL game at the Bernabéu was on 16 November 2025"', 1)
rep([C56], '"美式足球用手打、四次进攻"', '"American football is played with the hands, in four downs"', 1)
rep([C56], '用方框里的词填空。注意：有的词要变位。',
    'Fill the gaps with the words in the box. Careful: some verbs must be conjugated.', 1)
rep([C56], '"estadio = 体育场"', '"estadio = stadium"', 1)
rep([C56], '"himno = 国歌"', '"himno = anthem"', 1)
rep([C56], '"acoger 变位 → acoge"', '"acoger → acoge (it hosts)"', 1)
rep([C56], '"touchdown = 达阵得分"', '"touchdown = a touchdown"', 1)
rep([C56], '"calabaza = 南瓜"', '"calabaza = pumpkin"', 1)
rep([C56], '"disfraz = 化装服装"', '"disfraz = costume"', 1)
rep([C56], '用 ir a + 原形动词改写句子，表示“将要”。',
    'Rewrite the sentences with ir a + infinitive (the near future).', 1)
rep([C56], '"vamos a + 原形"', '"vamos a + infinitive"', 1)
rep([C56], '"va a + 原形"', '"va a + infinitive"', 1)
rep([C56], '"vas a + 原形"', '"vas a + infinitive"', 1)
rep([C56], '"van a + 原形"', '"van a + infinitive"', 1)
rep([C56], '"NFL 马德里站是伯纳乌第二场 NFL 比赛"', '"the Madrid NFL game is the second NFL game at the Bernabéu"', 1)
rep([C56], '"美国国歌由 Momsen 演唱，不是 Sáinz-Villegas"', '"the US anthem is sung by Momsen, not Sáinz-Villegas"', 1)
rep([C56], '"万圣节之夜在周六 31 日"', '"Halloween night was Saturday the 31st"', 1)

# ---------- content56: P6 ----------
rep([C56], 'NIVEL B2 · La vivienda decide la campaña · 住房决定选战',
    'NIVEL B2 · La vivienda decide la campaña · Housing decides the campaign', 1)
rep([C56], '看上面两张图，选出正确答案。', 'Look at the two charts above and choose the correct answer.', 1)
rep([C56], '"CIS 里 PSOE 第一（34%）"', '"in the CIS barometer the PSOE is first (34%)"', 1)
rep([C56], '"CIS 里 PP 22,2%"', '"in the CIS barometer the PP has 22.2%"', 1)
rep([C56], '"住房是首要问题（55,7%）"', '"housing is the top problem (55.7%)"', 1)
rep([C56], '"调查在 10 月 1–6 日进行"', '"the fieldwork was done 1–6 October"', 1)
rep([C56], '"34 + 22,2 + 17,1 = 73,3"', '"34 + 22.2 + 17.1 = 73.3"', 1)
rep([C56], '"本报只刊登 CIS 这一组数据并注明来源日期"',
    '"La Lucerna publishes only the CIS series here, with its source and date"', 1)
rep([C56], '"10 月 2 日议会否决两项住房法令"', '"on 2 October parliament rejected two housing decrees"', 1)
rep([C56], '"10 月 5 日解散议会并召集大选"', '"on 5 October the Cortes were dissolved and the election called"', 1)
rep([C56], '"民调是带误差的具体某天的照片"', '"a poll is a snapshot with a margin of error, taken on one day"', 1)
rep([C56], '"竞选 11 月 13 日开始"', '"the campaign starts on 13 November"', 1)
rep([C56], '"es posible que + 虚拟式 tenga"', '"es posible que + subjunctive tenga"', 1)
rep([C56], '"es importante que + 虚拟式 sea"', '"es importante que + subjunctive sea"', 1)
rep([C56], '"para que + 虚拟式（目的）"', '"para que + subjunctive (purpose)"', 1)
rep([C56], '"Aunque 后接陈述式（已知事实）"', '"Aunque + indicative here (a known fact)"', 1)
rep([C56], '用方框里的词填空：sondeo · muestra · indecisos · margen de error',
    'Fill the gaps with the words in the box: sondeo · muestra · indecisos · margen de error', 1)
rep([C56], '"sondeo = 民调"', '"sondeo = a poll"', 1)
rep([C56], '"muestra = 样本（5.025 人）"', '"muestra = a sample (5,025 people)"', 1)
rep([C56], '"indecisos = 未决定者"', '"indecisos = undecided voters"', 1)
rep([C56], '"margen de error = 误差范围"', '"margen de error = margin of error"', 1)

print('PART 4 OK')

# ---------- content7: P7 ----------
rep([C7], '语言聚焦 · Tres niveles, tres herramientas · 三个级别，三件工具',
    'Tres niveles, tres herramientas · Three levels, three tools', 1)
rep([C7], '日期格式：el lunes 2 de noviembre；星期、月份小写；1 号说 el uno。',
    'Dates: el lunes 2 de noviembre; days and months are lower case; the 1st is el uno.', 1)
rep([C7], '比较级 más…que、tan…como；bueno→mejor、malo→peor；绝不说 más mejor。',
    'Comparatives: más … que, tan … como; bueno → mejor, malo → peor; never más mejor.', 1)
rep([C7], 'es necesario que、para que、ojalá 后用虚拟式；creo que 后用陈述式。',
    'es necesario que, para que and ojalá take the subjunctive; creo que takes the indicative.', 1)
rep([C7], '"el lunes 2 de noviembre 连休"', '"el lunes 2 de noviembre = the long weekend"', 1)
rep([C7], '"el 1 = el uno"', '"the 1st = el uno"', 1)
rep([C7], '"29 日是周日"', '"the 29th is a Sunday"', 1)
rep([C7], '"月份小写：noviembre"', '"months are lower case: noviembre"', 1)
rep([C7], '"más + cara（房价更高）"', '"más + cara (housing costs more)"', 1)
rep([C7], '"tan + alta + como（同样高）"', '"tan + alta + como (just as high)"', 1)
rep([C7], '"bueno 的比较级是 mejor（不用 más）"', '"the comparative of bueno is mejor (no más needed)"', 1)
rep([C7], '"más mejor 是错误说法"', '"más mejor is wrong"', 1)
rep([C7], '"es necesario que + 虚拟式 baje"', '"es necesario que + subjunctive baje"', 1)
rep([C7], '"para que + 虚拟式 sea"', '"para que + subjunctive sea"', 1)
rep([C7], '"creo que + 陈述式 es"', '"creo que + indicative es"', 1)
rep([C7], '"ojalá + 虚拟式：baje"', '"ojalá + subjunctive: baje"', 1)
rep([C7], 'ERRORES TÍPICOS · 常见错误', 'ERRORES TÍPICOS · Common mistakes', 1)
rep([C7], '"lunes 是单数，动词用 es。"', '"lunes is singular, so the verb is es."', 1)
rep([C7], '"mejor 本身就是比较级，不加 más。"', '"mejor is already a comparative: no más."', 1)
rep([C7], '"gente 是单数集合名词，动词用单数。"', '"gente is a singular collective noun, so the verb is singular."', 1)
rep([C7], '"creo que 表肯定，用陈述式 es。"', '"creo que states a fact, so it takes the indicative es."', 1)
rep([C7], 'LA PALABRA · 本周生词', 'LA PALABRA · Word of the week', 1)
rep([C7], 'precampaña = 竞选预热期：正式竞选前的几周。本期就是 precampaña；竞选 13 日周五开始。',
    'precampaña = the pre-campaign: the weeks before the official campaign. This whole issue is precampaña; the campaign starts Friday the 13th.', 2)
rep([C7], '（ejemplo, escrito por la redacción）', '(ejemplo, escrito por la redacción)', 1)
rep([C7], '编辑部说明：截至本期截稿，未收到真实读者来信与第 8 版最佳作文，故本期登载编辑部示例信，承诺顺延至 VOL.3。欢迎来信！',
    "Editors' note: by press time no real letters or best page 8 texts had arrived, so this issue prints the editors' example letter and the promise carries to VOL.3. Write in!", 1)
rep([C7], 'FRASES DE LA SEMANA · 本周金句（逐字摘自本期文章）',
    'FRASES DE LA SEMANA · Sentences of the week (quoted word for word from this issue)', 1)
rep([C7], '"名单已提交：现在各党开始撰写纲领。"', '"The lists are in: now the parties are writing their programmes."', 1)
rep([C7], '"11 月 2 日周一九个自治区放假，其他地区照常上班。"',
    '"Monday 2 November is a holiday in nine communities — and a working day elsewhere."', 1)
rep([C7], '"三个节日，同一个秋夜。"', '"Three festivals, one autumn night."', 1)
rep([C7], '"皇马在诺坎普 2–1 获胜：这是巴萨本赛季联赛首败。"',
    '"Real Madrid won 2–1 at the Camp Nou: Barça\'s first league defeat of the season."', 1)
rep([C7], '"伯纳乌把草皮换成烤架形球场：美式足球来到马德里。"',
    '"The Bernabéu swaps grass for the gridiron: American football comes to Madrid."', 1)
rep([C7], '"住房是 55.7% 的西班牙人的首要问题。"', '"Housing is the main problem for 55.7% of Spaniards."', 1)
rep([C7], '"一次民调就是一张带误差的照片，拍于某一天。"',
    '"A poll is a snapshot with a margin of error, taken on one day."', 1)
rep([C7], '"11 月 8 日周日，马德里有两场约会：15:30 的 NFL 和 21:00 的马竞对巴萨。"',
    '"On Sunday 8 November, Madrid has two dates: the NFL at 15:30 and Atlético–Barça at 21:00."', 1)
rep([C7], 'LA PRÓXIMA SEMANA · 下期预告 (VOL.3)', 'LA PRÓXIMA SEMANA · Next week (VOL.3)', 1)

# ---------- content8: P8 ----------
rep([C8], '第 8 版 · La gran prueba de la semana + todas las respuestas',
    'Page 8 · La gran prueba de la semana + todas las respuestas', 1)
rep([C8], '"ganó 2–1 = 以 2–1 获胜"', '"ganó 2–1 = won 2–1"', 1)
rep([C8], '"marcar dos goles = 进两球"', '"marcar dos goles = scored two goals"', 1)
rep([C8], '"primera derrota liguera = 联赛首败"', '"primera derrota liguera = first league defeat"', 1)
rep([C8], '"recortar = 缩小分差"', '"recortar = to cut the gap"', 1)
rep([C8], '"acoger = 承办（伯纳乌承办 NFL）"', '"acoger = to host (the Bernabéu hosts the NFL)"', 1)
rep([C8], '"el emparrillado = 美式足球场"', '"el emparrillado = the gridiron"', 1)
rep([C8], '"周日上演马竞–巴萨"', '"on Sunday it\'s Atlético–Barça"', 1)
rep([C8], '"himno = 国歌"', '"himno = anthem"', 1)
rep([C8], '"周一放假的自治区有 9 个"', '"nine communities have Monday off"', 1)
rep([C8], '"诸圣节 11 月 1 日"', '"All Saints\' Day: 1 November"', 1)
rep([C8], '"马竞–巴萨与 NFL 都在周日"', '"Atlético–Barça and the NFL are both on Sunday"', 1)
rep([C8], '"Castanyada 吃 panellets"', '"panellets are a Castanyada sweet"', 1)
rep([C8], '"DANA 纪念活动在 10 月 29 日周四"', '"the DANA memorial events were on Thursday 29 October"', 1)
rep([C8], '"大选在 11 月 29 日"', '"the election is on 29 November"', 1)
rep([C8], '"CIS 十月调查：住房 55,7%"', '"CIS, October: housing at 55.7%"', 1)
rep([C8], '"竞选 11 月 13 日开始"', '"the campaign starts on 13 November"', 1)
rep([C8], '"马德里在放假名单里"', '"Madrid is on the holiday list"', 1)
rep([C8], '"加泰罗尼亚周一是工作日"', '"in Catalonia Monday is a working day"', 1)
rep([C8], '"Ana 只看 NFL；晚上看马竞–巴萨的是 Pablo"',
    '"Ana watches only the NFL; Pablo watches Atlético–Barça in the evening"', 1)
rep([C8], '"标题概括两地对比"', '"the title sums up the two-city contrast"', 1)
rep([C8], '"主语 + 动词 + 地点"', '"subject + verb + place"', 1)
rep([C8], '"时间在前"', '"time first"', 1)
rep([C8], '"a las nueve = 在九点"', '"a las nueve = at nine"', 1)
rep([C8], '"疑问词在句首"', '"the question word comes first"', 1)
# E-section redirection (W43 ESxEN KIT ruling 1): ES<->EN, not ES<->ZH
rep([C8], '"周一在九个自治区是假日。"', '"Monday is a public holiday in nine communities."', 1)
rep([C8], '"周日我们看 NFL 和马竞–巴萨。"', '"On Sunday we watch the NFL and Atlético–Barça."', 1)
rep([C8], '"对照原文"', '"Compare with the Spanish sentence."', 2)
rep([C8], '"伯纳乌承办一场 NFL 比赛。→ ___"', '"The Bernabéu hosts an NFL game. → ___"', 1)
rep([C8], '"acoger = 承办"', '"acoger = to host"', 1)
rep([C8], '"每个图表都必须标明来源。→ ___"', '"Every chart must show its source. → ___"', 1)
rep([C8], '"tener que = 必须"', '"tener que = to have to, must"', 1)
rep([C8], '"sondeo=民调 c"', '"sondeo = an opinion poll — c"', 1)
rep([C8], '"muestra=样本 d"', '"muestra = the people interviewed — d"', 1)
rep([C8], '"margen de error=误差范围 b"', '"margen de error = margin of error — b"', 1)
rep([C8], '"junta electoral=选举委员会 a"', '"junta electoral = the electoral board — a"', 1)
rep([C8], '"alquiler = 租金"', '"alquiler = rent"', 1)
rep([C8], '"tres habitaciones = 三居室"', '"tres habitaciones = three bedrooms"', 1)
rep([C8], '"¿cuánto cuesta? 多少钱"', '"¿cuánto cuesta? = how much does it cost?"', 1)
rep([C8], '"firmar = 签（合同）"', '"firmar = to sign (the contract)"', 1)
rep([C8], '"mudanza = 搬家"', '"mudanza = moving house"', 1)
rep([C8], '"（开放题，范文如下）"', '"(Open task — model text below)"', 1)
rep([C8], '"范文见本版 H 区（84 词）"', '"Model text in section H on this page (84 words)"', 1)
rep([C8], 'RESPUESTAS · 参考答案 — 按版面分页排列，找到题号即可',
    'RESPUESTAS · Answer key — arranged by page; just find the number', 1)
rep([C8], '每题附一句中文简析 · 带 ✓ 的为范文题',
    'One short English note per item · ✓ marks the writing task', 1)

print('PART 5 OK — transform complete')
