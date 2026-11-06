# -*- coding: utf-8 -*-
"""W45 ES core -> ES x NL fan-out transform for the BUILD COPY ONLY.

Literal replacements only (README #17): each (files, old, new) asserts the
total occurrence count across the listed files before replacing. Spanish
target-language text is never a replacement target; only the explanation
layer (Chinese notes/bridges/titles/furniture) and the P8 E-section
redirection (W43 ESxNL KIT ruling: 137/138 re-aimed at Dutch, 139/140
stems re-aimed with keys unchanged) change. Furniture strings are copied
verbatim from the shipped W43 ESxNL edition (files/weekly-report-es-nl/),
VOL.1 -> VOL.2 only. The explanation method bridge() is renamed to expl()
(def + 20 call sites), as in the W43 ESxNL build code.
"""
import pathlib, sys

B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-nl-build')
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
rep(ALL, 'weekly-report-w45-es-core', 'weekly-report-w45-es-nl', 5)
rep(['render.py'], 'weekly-report-w45-es-core', 'weekly-report-w45-es-nl', 1)
rep(['render.py'], 'La-Lucerna-VOL2-web.pdf', 'La-Lucerna-VOL2-NL-web.pdf', 1)
rep(['render.py'], 'La-Lucerna-VOL2.pdf', 'La-Lucerna-VOL2-NL.pdf', 1)
rep(['render.py'], 'Render the ES core edition', 'Render the ES x NL edition', 1)

# ---------- bslib4 furniture (W43 ESxNL verbatim, VOL.1 -> VOL.2) ----------
rep([BS], '"La Lucerna · 西班牙语周报 VOL.2 · LUCERNA SPANISH WEEKLY"',
    '"La Lucerna · SPAANS WEEKBLAD VOL.2 · TEKSTEN IN HET SPAANS · UITLEG IN HET NEDERLANDS"', 1)
rep([BS], 'f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} van {total}"', 1)
rep([BS], '"译注｜" + s', '"Uitleg — " + s', 1)
# method rename bridge -> expl (W43 ESxNL build code precedent)
rep([BS], 'def bridge(self, s', 'def expl(self, s', 1)
rep(ALL, '.bridge(', '.expl(', 20)

# ---------- global explanation-layer vocab (W43 ESxNL precedents) ----------
# NOTE: '完形单选' BEFORE '单选' (substring), and the P8 writing bridge
# BEFORE the global '写作' replacement (it contains '写作' as substring).
rep([C8], '写作题（无唯一答案）；范文（84 词）见下。',
    'Schrijfopdracht (geen uniek antwoord); voorbeeldtekst (84 woorden) hieronder.', 1)
for old, new in [
    ('完形单选', 'Cloze-meerkeuze'), ('完成句子', 'Zinnen aanvullen'),
    ('单选', 'Meerkeuze'),
    ('判断对错', 'Lezen: waar/onwaar'), ('造句', 'Zinnen maken'),
    ('句型转换', 'Zinnen omvormen'), ('词汇配对', 'Woorden combineren'),
    ('翻译', 'Vertalen'), ('写作', 'Schrijven'),
]:
    for lv in ('A2', 'B1', 'B2'):
        rep(ALL, '("%s", "%s", ' % (lv, old), '("%s", "%s", ' % (lv, new), allow_zero=True)
# P8 answer-code type check (paired with the typ translation; dash format untouched)
rep([C8], '== "写作"', '== "Schrijven"', 1)
rep(ALL, 'instr="填空"', 'instr="Vul in"')
rep(ALL, 'instr="判断"', 'instr="W/NW"')
rep(ALL, 'instr="造句"', 'instr="Zinnen maken"')
rep(ALL, 'instr="改写"', 'instr="Herschrijf"')
rep(ALL, 'instr="翻译"', 'instr="Vertalen"')
rep(ALL, 'instr="写作"', 'instr="Schrijven"')
rep(ALL, 'instr="把词和释义配对"', 'instr="Combineer"')
rep(ALL, '答案见第 8 版 · 题目可跨级混排，按题号找答案',
    'Antwoorden op pagina 8 · Niveaus door elkaar — zoek op nummer', 5)
rep(ALL, '¿Y TÚ? · 说说你自己', '¿Y TÚ? · En jij?', 4)
rep([C12], 'EJERCICIOS · 第 2 版练习', 'EJERCICIOS · Oefeningen van pagina 2', 1)
rep([C34], 'EJERCICIOS · 第 3 版练习', 'EJERCICIOS · Oefeningen van pagina 3', 1)
rep([C34], 'EJERCICIOS · 第 4 版练习', 'EJERCICIOS · Oefeningen van pagina 4', 1)
rep([C56], 'EJERCICIOS · 第 5 版练习', 'EJERCICIOS · Oefeningen van pagina 5', 1)
rep([C56], 'EJERCICIOS · 第 6 版练习', 'EJERCICIOS · Oefeningen van pagina 6', 1)
rep([C34], 'CULTURA · 文化', 'CULTURA · Cultuur', 1)
rep([C34], 'DEPORTE · 体育', 'DEPORTE · Sport', 1)
rep([C56], 'JUVENTUD · 青年', 'JUVENTUD · Jeugd', 1)
rep([C56], 'A FONDO · 深读', 'A FONDO · Achtergrond', 1)
rep([C7], 'LENGUA · 语言', 'LENGUA · Taal', 1)
rep([C8], 'EJERCICIOS Y RESPUESTAS · 练习与答案', 'EJERCICIOS Y RESPUESTAS · Oefeningen en antwoorden', 1)
rep([C8], '第 8 版 · La gran prueba de la semana + todas las respuestas',
    'Pagina 8 · La gran prueba de la semana + todas las respuestas', 1)

print('PART 1 OK')

# ---------- content12: P1 ----------
rep([C12], 'CADA SEMANA EN ESPAÑOL · 每周一期 · 读西班牙人正在读的西班牙语',
    'CADA SEMANA EN ESPAÑOL · ELKE WEEK · HET SPAANS DAT DE SPANJAARDEN LEZEN', 1)
rep([C12], '西 班 牙 语 周 报 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL',
    'SPAANS WEEKBLAD · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL', 1)
rep([C12], 'p.text(975, 372, "EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA", 19, "sans", False, GREY, anchor="middle")',
    'p.text(975, 372, "TEKSTEN IN HET SPAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 19.5, "sans", True, BRICK, anchor="middle")', 1)
rep([C12], '距大选还有 27 天 · 住房决定选战', 'NOG 27 DAGEN · HUISVESTING BESLIST DE CAMPAGNE', 1)
rep([C12], '本期头条 · 详见第 2、6 版', 'HOOFDVERHAAL · ZIE PAGINA 2 EN 6', 1)
rep([C12], 'LA NOTICIA · 头条', 'LA NOTICIA · Hoofdverhaal', 1)
rep([C12], 'f.expl("讲解｜la cuenta atrás 倒计时 · disolver las Cortes 解散议会 · el decreto 法令 · la candidatura 候选人名单。")',
    'f.expl("Uitleg — la cuenta atrás = de countdown · disolver las Cortes = het parlement ontbinden · el decreto = een decreet · la candidatura = een kandidatuur.")', 1)
rep([C12], 'LA SEMANA EN CIFRAS · 数字看本周', 'LA SEMANA EN CIFRAS · In cijfers', 1)
rep([C12], '（距 29 日大选 27 天）', '(nog 27 dagen tot de verkiezingen van 29 november)', 1)
rep([C12], '（11 月 2 日放假的自治区）', "(regio's met een feestdag op 2 november)", 1)
rep([C12], '（CIS 十月数据）', '(CIS, oktober)', 1)
rep([C12], 'AHORA TÚ · 即学即练', 'AHORA TÚ · Probeer het nu', 1)
rep([C12], '"las listas ya están presentadas; ahora se escriben los programas"',
    '"de lijsten zijn ingediend; nu worden de programma\'s geschreven"', 1)
rep([C12], '"大选在 11 月 29 日周日"', '"de verkiezingen zijn op zondag 29 november"', 1)
rep([C12], '"住房是选战的决定性议题"', '"huisvesting beslist de campagne"', 1)
rep([C12], '"周一放假的自治区有 9 个"', '"negen regio\'s hebben maandag vrij"', 2)
rep([C12], '"马竞–巴萨周日 21:00 开球"', '"Atlético–Barça begint zondag om 21:00"', 1)
rep([C12], '"NFL 马德里站周日 15:30 开球"', '"de NFL komt zondag om 15:30 naar het Bernabéu"', 1)
rep([C12], '本周五大看点 · Para entender la semana', 'Vijf sleutels · Para entender la semana', 1)
rep([C12], '五大看点，不编数字：全在本期里讲清。', 'Vijf sleutels — geen verzonnen cijfers.', 1)
rep([C12], 'EN ESTA EDICIÓN · 本期目录', 'EN ESTA EDICIÓN · In dit nummer', 1)
rep([C12], '“竞选预热期”：正式竞选前的几周。', 'De precampagne: de weken vóór de campagne.', 1)
rep([C12], 'BREVES · 快讯', 'BREVES · Kort nieuws', 1)
rep([C12], 'QUIZ RELÁMPAGO · 闪电问答', 'QUIZ RELÁMPAGO · Bliksemquiz', 1)
rep([C12], '读头版，选出正确答案 · 答案见第 8 版', 'Lees de voorpagina en kies · Antwoorden op pagina 8', 1)
rep([C12], '"大选在 11 月 29 日"', '"de verkiezingen zijn op 29 november"', 2)
rep([C12], '"NFL 马德里站周日下午"', '"de NFL komt zondagmiddag naar het Bernabéu"', 1)
rep([C12], '"马竞–巴萨周日 21:00"', '"Atlético–Barça begint zondag om 21:00"', 1)

print('PART 2a OK')

# ---------- content12: P2 ----------
rep([C12], 'VIDA · 生活', 'VIDA · Leven', 1)
rep([C12], 'NIVEL A2 · El puente del lunes 2 · 11 月 2 日的连休',
    'NIVEL A2 · El puente del lunes 2 · Het lange weekend van 2 november', 1)
rep([C12], 'EL CALENDARIO · 本周日历', 'EL CALENDARIO · Deze week', 1)
rep([C12], '（周一九地连休；周二《官方公报》公布正式候选名单）',
    "(maandag: lang weekend in negen regio's; dinsdag: het BOE publiceert de officiële kandidatenlijsten)", 1)
rep([C12], '（周二欧冠三场西甲球队比赛）', '(dinsdag: drie Spaanse clubs in de Champions League)', 1)
rep([C12], '（周三皇马客场对雅典 AEK）', '(woensdag: Real Madrid op bezoek bij AEK Athene)', 1)
rep([C12], '（周四皇家社会欧联对里昂）', '(donderdag: Real Sociedad tegen Lyon in de Europa League)', 1)
rep([C12], '（周五联赛第 12 轮开球）', '(vrijdag: speelronde 12 begint)', 1)
rep([C12], '（周六瓦伦西亚对皇马）', '(zaterdag: Valencia tegen Real Madrid)', 1)
rep([C12], '（周日 NFL 马德里站＋马竞对巴萨）', '(zondag: de NFL in Madrid + Atlético tegen Barça)', 1)
rep([C12], 'f.gloss("festivo 放假的 · el puente 连休 · la comunidad 自治区 · anochecer 天黑 · el horario de invierno 冬令时。")',
    'f.gloss("festivo — een feestdag (bijv. nw.) · el puente — een lang weekend · la comunidad — een autonome regio · anochecer — het donker worden · el horario de invierno — de wintertijd.")', 1)
rep([C12], '11 月 2 日你那里放假吗？连休你做什么：旅行、休息还是看球？写两句西班牙语寄给编辑部。',
    'Is maandag 2 november bij jou een feestdag? Wat doe je met het lange weekend: reizen, rusten of voetbal kijken? Schrijf twee zinnen in het Spaans en stuur ze naar de redactie.', 2)
rep([C12], 'LOS DÍAS DE LA SEMANA · 这样说日期', 'LOS DÍAS DE LA SEMANA · Zo zeg je de datum', 1)
rep([C12], 'lunes 2 – domingo 8 de noviembre · 11 月 2 日周一至 8 日周日',
    'lunes 2 – domingo 8 de noviembre · maandag 2 tot zondag 8 november', 1)
rep([C12], '用正确的日期形式补全句子。', 'Vul de zinnen aan met de juiste datumvorm.', 1)
rep([C12], '补全动词的现在时形式。', 'Vul de werkwoorden in de tegenwoordige tijd in.', 1)
rep([C12], '读第 2 版文章，选出正确答案。', 'Lees het artikel op pagina 2 en kies het juiste antwoord.', 1)
rep([C12], '"11 月 2 日周一"', '"maandag 2 november"', 1)
rep([C12], '"11 月 8 日周日"', '"zondag 8 november"', 1)
rep([C12], '"每月 1 号说 el uno"', '"de 1e van de maand is el uno"', 1)
rep([C12], '"月份小写"', '"maanden met kleine letters"', 1)
rep([C12], '"el lunes → es（单数）"', '"el lunes → es (enkelvoud)"', 1)
rep([C12], '"todos → preguntan"', '"todos → preguntan (zij vragen)"', 1)
rep([C12], '"anochecer → anochece"', '"anochecer → anochece (het wordt donker)"', 1)
rep([C12], '"nosotros → descansamos"', '"nosotros → descansamos (wij rusten)"', 1)
rep([C12], '"el fin de semana → dura"', '"el fin de semana → dura (het duurt)"', 1)
rep([C12], '"九个自治区周一放假"', '"negen regio\'s hebben maandag vrij"', 1)
rep([C12], '"诸圣节 11 月 1 日落在周日"', '"Allerheiligen, 1 november, viel op een zondag"', 1)
rep([C12], '"加泰罗尼亚周一是工作日"', '"in Catalonië is maandag een werkdag"', 1)
rep([C12], '"冬令时第二周，天黑得早"', '"tweede week van de wintertijd: het wordt vroeg donker"', 1)
rep([C12], '"puente=三天连休 b"', '"puente = een driedaags lang weekend — b"', 1)
rep([C12], '"festivo=放假的 a"', '"festivo = een feestdag — a"', 1)
rep([C12], '"anochecer=天黑 c"', '"anochecer = donker worden — c"', 1)
rep([C12], '"comunidad=自治区 d"', '"comunidad = een autonome regio — d"', 1)

print('PART 2b OK')

# ---------- content34: P3 ----------
rep([C34], 'A2 → B1 · La semana pasada: tres noches de otoño · 上周的三个秋夜',
    'A2 → B1 · La semana pasada: tres noches de otoño · De drie herfstnachten van vorige week', 1)
rep([C34], 'f.gloss("sobrio 克制的 · el homenaje 纪念表彰 · el disfraz 服装（化装） · el boniato 红薯 · el cementerio 墓地。")',
    'f.gloss("sobrio — ingetogen · el homenaje — een herdenking · el disfraz — een kostuum · el boniato — een zoete aardappel · el cementerio — een begraafplaats.")', 1)
rep([C34], '你最喜欢哪一夜：29 日、31 日还是 1 日？31 日你吃了什么？写两句寄来。',
    'Welke nacht vind je het mooist: de 29e, de 31e of de 1e? En wat at je op de 31e? Schrijf twee zinnen en stuur ze op.', 2)
rep([C34], '读第 3 版文章，判断对错。', 'Lees het artikel op pagina 3: waar of niet waar?', 1)
rep([C34], '用方框里的词填空。', 'Vul de gaten in met de woorden uit het kader.', 1)
rep([C34], 'e.expl("选出正确答案。")', 'e.expl("Kies het juiste antwoord.")', 1)
rep([C34], '把词组成正确的句子。', 'Zet de woorden in de juiste volgorde.', 1)
rep([C34], '"DANA 纪念活动在 10 月 29 日周四"', '"de DANA-herdenking was op donderdag 29 oktober"', 1)
rep([C34], '"Castanyada 吃烤栗子、红薯和 panellets"', '"geroosterde kastanjes, zoete aardappelen en panellets bij de Castanyada"', 1)
rep([C34], '"Samaín 是加利西亚古节，不是万圣节译名"', '"de Samaín is een oud Galicisch feest, geen naam voor Halloween"', 1)
rep([C34], '"诸圣节在 11 月 1 日，不是 10 月 31 日"', '"Allerheiligen is op 1 november, niet op 31 oktober"', 1)
rep([C34], '"周日家属去墓地献花"', '"op zondag brachten families bloemen naar de begraafplaatsen"', 1)
rep([C34], '"给逝者带花 flores"', '"flores = bloemen, voor de overledenen"', 1)
rep([C34], '"cementerio = 墓地"', '"cementerio = begraafplaats"', 1)
rep([C34], '"castañas asadas 烤栗子"', '"castañas asadas = geroosterde kastanjes"', 1)
rep([C34], '"disfraz = 化装服装"', '"disfraz = kostuum"', 1)
rep([C34], '"actos de memoria 纪念活动"', '"actos de memoria = herdenkingen"', 1)
rep([C34], '"DANA 纪念是 2024 年风暴两周年"', '"de DANA-herdenking was twee jaar na de storm van 2024"', 1)
rep([C34], '"Castanyada 在加泰罗尼亚"', '"de Castanyada is in Catalonië"', 1)
rep([C34], '"Samaín 是加利西亚古老节日"', '"de Samaín is een heel oud Galicisch feest"', 1)
rep([C34], '"三夜之后周一有人连休有人上班"', '"na de drie nachten heeft de een maandag een lang weekend en werkt de ander"', 1)
rep([C34], '"动词第二位"', '"het werkwoord op de tweede plaats"', 1)
rep([C34], '"时间在前，动词第二"', '"tijd eerst, werkwoord als tweede"', 1)
rep([C34], '"地点在前，动词第二"', '"plaats eerst, werkwoord als tweede"', 1)
rep([C34], '"间接疑问用 si"', '"indirecte vragen met si"', 1)

# ---------- content34: P4 ----------
rep([C34], 'NIVEL B1 · Europa primero, el domingo a las 21:00 · 欧战在先，周日晚九点',
    'NIVEL B1 · Europa primero, el domingo a las 21:00 · Eerst Europa, zondag om 21:00', 1)
rep([C34], 'f.gloss("la jornada 轮次 · recortar la distancia 缩小分差 · recibir 主场迎战 · visitar 客场挑战 · el Metropolitano 马竞主场。")',
    'f.gloss("la jornada — een speelronde · recortar la distancia — de achterstand verkleinen · recibir — thuis spelen · visitar — op bezoek spelen · el Metropolitano — het stadion van Atlético.")', 1)
rep([C34], '周日 21:00 你看哪一场？马竞主场谁赢？写两句西班牙语寄来。',
    'Welke wedstrijd kijk je zondag om 21:00? Wie wint in het Metropolitano? Schrijf twee zinnen in het Spaans en stuur ze op.', 2)
rep([C34], 'LA SEMANA EUROPEA Y LA JORNADA 12 · 欧战周与联赛第 12 轮',
    'LA SEMANA EUROPEA Y LA JORNADA 12 · De Europese week en speelronde 12', 1)
rep([C34], '读第 4 版文章，选出正确答案。', 'Lees het artikel op pagina 4 en kies het juiste antwoord.', 1)
rep([C34], '"皇马 2–1 赢下国家德比"', '"Real Madrid won de Clásico met 2–1"', 1)
rep([C34], '"姆巴佩进了两球"', '"Mbappé scoorde beide doelpunten"', 1)
rep([C34], '"周二欧冠三场西甲球队比赛"', '"drie Spaanse clubs spelen dinsdag in de Champions League"', 1)
rep([C34], '"周日 21:00 马竞–巴萨"', '"Atlético–Barça: zondag, 21:00"', 1)
rep([C34], '"周日下午还有 NFL 马德里站"', '"zondagmiddag is er ook de NFL in Madrid"', 1)
rep([C34], '"jornada=轮次 b"', '"jornada = een speelronde — b"', 1)
rep([C34], '"recibir=主场迎战 a"', '"recibir = thuis spelen — a"', 1)
rep([C34], '"visitar=客场挑战 d"', '"visitar = op bezoek spelen — d"', 1)
rep([C34], '"recortar=缩小分差 c"', '"recortar = de achterstand verkleinen — c"', 1)
rep([C34], '用括号里词的比较级或 -ísimo 形式填空。',
    'Vul de gaten in met de vergrotende trap of de -ísimo-vorm van het woord tussen haakjes.', 1)
rep([C34], '"más + importante（马竞–巴萨更重要）"', '"más + importante (Atlético–Barça telt zwaarder)"', 1)
rep([C34], '"muchísimos partidos 比赛很多"', '"muchísimos partidos = heel, heel veel wedstrijden"', 1)
rep([C34], '"malo 的比较级是 peor"', '"de vergrotende trap van malo is peor"', 1)
rep([C34], '"bueno 的比较级是 mejor"', '"de vergrotende trap van bueno is mejor"', 1)
rep([C34], '把句子改成过去时（pretérito indefinido）。', 'Zet de zinnen in de verleden tijd (pretérito indefinido).', 1)
rep([C34], '"ganar → ganó"', '"ganar → ganó (hij won)"', 1)
rep([C34], '"marcar → marcó"', '"marcar → marcó (hij scoorde)"', 1)
rep([C34], '"perder → perdió"', '"perder → perdió (zij verloren)"', 1)
rep([C34], '"recortar → recortó"', '"recortar → recortó (hij verkleinde)"', 1)
rep([C34], '"ir 的过去时是 fueron"', '"ir in de verleden tijd is fueron (zij gingen)"', 1)

print('PART 3 OK')

# ---------- content56: P5 ----------
rep([C56], 'NIVEL B1 · La NFL en Madrid · NFL 来到马德里',
    'NIVEL B1 · La NFL en Madrid · De NFL komt naar Madrid', 1)
rep([C56], 'EL PLAN DEL PUENTE · 连休计划', 'EL PLAN DEL PUENTE · Het plan', 1)
rep([C56], '（周一：休息陪家人；若你那里连休，就去旅行）',
    '(maandag: rusten met familie — of reizen, als jouw regio een lang weekend heeft)', 1)
rep([C56], '（周六晚：瓦伦西亚对皇马）', '(zaterdagavond: Valencia tegen Real Madrid)', 1)
rep([C56], '（周日下午：NFL 马德里站）', '(zondagmiddag: de NFL in Madrid)', 1)
rep([C56], '（周日晚：马竞对巴萨）', '(zondagavond: Atlético tegen Barça)', 1)
rep([C56], '（返校返工；竞选 13 日开始）', '(terug naar school en werk; de campagne begint op de 13e)', 1)
rep([C56], 'f.gloss("el emparrillado 美式足球场（烤架形场地） · el himno 国歌 · el touchdown 达阵得分 · la calabaza 南瓜。")',
    'f.gloss("el emparrillado — het gridiron (het American footballveld) · el himno — een volkslied · el touchdown — een touchdown · la calabaza — een pompoen.")', 1)
rep([C56], '你看过美式足球比赛吗？你更喜欢足球还是美式足球？写两句寄来。',
    'Heb je ooit een American footballwedstrijd gezien? Wat vind je leuker: voetbal of American football? Schrijf twee zinnen en stuur ze op.', 2)
rep([C56], '读第 5 版文章，选出正确答案。', 'Lees het artikel op pagina 5 en kies het juiste antwoord.', 1)
rep([C56], '"NFL 马德里站周日 15:30"', '"de NFL in Madrid: zondag, 15:30"', 1)
rep([C56], '"孟加拉虎对猎鹰"', '"Bengals tegen Falcons"', 1)
rep([C56], '"西班牙国歌由吉他手演奏"', '"het Spaanse volkslied wordt gespeeld door een gitarist"', 1)
rep([C56], '"首场 NFL 伯纳乌赛在 2025 年 11 月 16 日"', '"de eerste NFL-wedstrijd in het Bernabéu was op 16 november 2025"', 1)
rep([C56], '"美式足球用手打、四次进攻"', '"American football speel je met de handen, in vier downs"', 1)
rep([C56], '用方框里的词填空。注意：有的词要变位。',
    'Vul de gaten in met de woorden uit het kader. Let op: sommige werkwoorden moet je vervoegen.', 1)
rep([C56], '"estadio = 体育场"', '"estadio = stadion"', 1)
rep([C56], '"himno = 国歌"', '"himno = volkslied"', 1)
rep([C56], '"acoger 变位 → acoge"', '"acoger → acoge (het organiseert)"', 1)
rep([C56], '"touchdown = 达阵得分"', '"touchdown = een touchdown"', 1)
rep([C56], '"calabaza = 南瓜"', '"calabaza = pompoen"', 1)
rep([C56], '"disfraz = 化装服装"', '"disfraz = kostuum"', 1)
rep([C56], '用 ir a + 原形动词改写句子，表示“将要”。',
    'Herschrijf de zinnen met ir a + infinitief (de nabije toekomst).', 1)
rep([C56], '"vamos a + 原形"', '"vamos a + infinitief"', 1)
rep([C56], '"va a + 原形"', '"va a + infinitief"', 1)
rep([C56], '"vas a + 原形"', '"vas a + infinitief"', 1)
rep([C56], '"van a + 原形"', '"van a + infinitief"', 1)
rep([C56], '"NFL 马德里站是伯纳乌第二场 NFL 比赛"', '"de NFL-wedstrijd in Madrid is de tweede NFL-wedstrijd in het Bernabéu"', 1)
rep([C56], '"美国国歌由 Momsen 演唱，不是 Sáinz-Villegas"', '"het Amerikaanse volkslied wordt gezongen door Momsen, niet door Sáinz-Villegas"', 1)
rep([C56], '"万圣节之夜在周六 31 日"', '"Halloweenavond was zaterdag de 31e"', 1)

# ---------- content56: P6 ----------
rep([C56], 'NIVEL B2 · La vivienda decide la campaña · 住房决定选战',
    'NIVEL B2 · La vivienda decide la campaña · Huisvesting beslist de campagne', 1)
rep([C56], '看上面两张图，选出正确答案。', 'Kijk naar de twee grafieken hierboven en kies het juiste antwoord.', 1)
rep([C56], '"CIS 里 PSOE 第一（34%）"', '"in de CIS-barometer staat de PSOE eerste (34%)"', 1)
rep([C56], '"CIS 里 PP 22,2%"', '"in de CIS-barometer heeft de PP 22,2%"', 1)
rep([C56], '"住房是首要问题（55,7%）"', '"huisvesting is het grootste probleem (55,7%)"', 1)
rep([C56], '"调查在 10 月 1–6 日进行"', '"het veldwerk was van 1–6 oktober"', 1)
rep([C56], '"34 + 22,2 + 17,1 = 73,3"', '"34 + 22,2 + 17,1 = 73,3"', 1)
rep([C56], '"本报只刊登 CIS 这一组数据并注明来源日期"',
    '"La Lucerna publiceert hier alleen de CIS-reeks, met bron en datum"', 1)
rep([C56], '"10 月 2 日议会否决两项住房法令"', '"op 2 oktober verwierp het parlement twee woningdecreten"', 1)
rep([C56], '"10 月 5 日解散议会并召集大选"', '"op 5 oktober werden de Cortes ontbonden en verkiezingen uitgeschreven"', 1)
rep([C56], '"民调是带误差的具体某天的照片"', '"een peiling is een momentopname met een foutmarge, van één dag"', 1)
rep([C56], '"竞选 11 月 13 日开始"', '"de campagne begint op 13 november"', 1)
rep([C56], '"es posible que + 虚拟式 tenga"', '"es posible que + aanvoegende wijs tenga"', 1)
rep([C56], '"es importante que + 虚拟式 sea"', '"es importante que + aanvoegende wijs sea"', 1)
rep([C56], '"para que + 虚拟式（目的）"', '"para que + aanvoegende wijs (doel)"', 1)
rep([C56], '"Aunque 后接陈述式（已知事实）"', '"Aunque + indicatief hier (een bekend feit)"', 1)
rep([C56], '用方框里的词填空：sondeo · muestra · indecisos · margen de error',
    'Vul de gaten in met de woorden uit het kader: sondeo · muestra · indecisos · margen de error', 1)
rep([C56], '"sondeo = 民调"', '"sondeo = een peiling"', 1)
rep([C56], '"muestra = 样本（5.025 人）"', '"muestra = een steekproef (5.025 mensen)"', 1)
rep([C56], '"indecisos = 未决定者"', '"indecisos = zwevende kiezers"', 1)
rep([C56], '"margen de error = 误差范围"', '"margen de error = foutmarge"', 1)

print('PART 4 OK')

# ---------- content7: P7 ----------
rep([C7], '语言聚焦 · Tres niveles, tres herramientas · 三个级别，三件工具',
    'Tres niveles, tres herramientas · Drie niveaus, drie hulpmiddelen', 1)
rep([C7], '日期格式：el lunes 2 de noviembre；星期、月份小写；1 号说 el uno。',
    'Datums: el lunes 2 de noviembre; dagen en maanden met kleine letters; de 1e is el uno.', 1)
rep([C7], '比较级 más…que、tan…como；bueno→mejor、malo→peor；绝不说 más mejor。',
    'Vergrotende trap: más … que, tan … como; bueno → mejor, malo → peor; nooit más mejor.', 1)
rep([C7], 'es necesario que、para que、ojalá 后用虚拟式；creo que 后用陈述式。',
    'es necesario que, para que en ojalá krijgen de aanvoegende wijs; creo que krijgt de indicatief.', 1)
rep([C7], '"el lunes 2 de noviembre 连休"', '"el lunes 2 de noviembre = het lange weekend"', 1)
rep([C7], '"el 1 = el uno"', '"de 1e = el uno"', 1)
rep([C7], '"29 日是周日"', '"de 29e is een zondag"', 1)
rep([C7], '"月份小写：noviembre"', '"maanden met kleine letters: noviembre"', 1)
rep([C7], '"más + cara（房价更高）"', '"más + cara (wonen kost meer)"', 1)
rep([C7], '"tan + alta + como（同样高）"', '"tan + alta + como (even hoog)"', 1)
rep([C7], '"bueno 的比较级是 mejor（不用 más）"', '"de vergrotende trap van bueno is mejor (geen más nodig)"', 1)
rep([C7], '"más mejor 是错误说法"', '"más mejor is fout"', 1)
rep([C7], '"es necesario que + 虚拟式 baje"', '"es necesario que + aanvoegende wijs baje"', 1)
rep([C7], '"para que + 虚拟式 sea"', '"para que + aanvoegende wijs sea"', 1)
rep([C7], '"creo que + 陈述式 es"', '"creo que + indicatief es"', 1)
rep([C7], '"ojalá + 虚拟式：baje"', '"ojalá + aanvoegende wijs: baje"', 1)
rep([C7], 'ERRORES TÍPICOS · 常见错误', 'ERRORES TÍPICOS · Fouten', 1)
rep([C7], '"lunes 是单数，动词用 es。"', '"lunes is enkelvoud, dus es."', 1)
rep([C7], '"mejor 本身就是比较级，不加 más。"', '"mejor is al een vergrotende trap: geen más."', 1)
rep([C7], '"gente 是单数集合名词，动词用单数。"', '"gente is enkelvoud, als één groep."', 1)
rep([C7], '"creo que 表肯定，用陈述式 es。"', '"creo que stelt een feit: indicatief es."', 1)
rep([C7], 'LA PALABRA · 本周生词', 'LA PALABRA · Woord van de week', 1)
rep([C7], 'precampaña = 竞选预热期：正式竞选前的几周。本期就是 precampaña；竞选 13 日周五开始。',
    'precampaña = de precampagne: de weken vóór de officiële campagne. Dit hele nummer is precampaña; de campagne begint vrijdag de 13e.', 2)
# Letter attribution: KEPT full-width parens, as in the shipped W43 ESxNL
# build (family precedent) — the Spanish letter body and name Ana are frozen.
rep([C7], '编辑部说明：截至本期截稿，未收到真实读者来信与第 8 版最佳作文，故本期登载编辑部示例信，承诺顺延至 VOL.3。欢迎来信！',
    'Opmerking van de redactie: bij het ter perse gaan waren er geen echte brieven of beste pagina-8-teksten binnen; daarom drukken we deze voorbeeldbrief af en de belofte schuift door naar VOL.3.', 1)
rep([C7], 'FRASES DE LA SEMANA · 本周金句（逐字摘自本期文章）',
    'FRASES DE LA SEMANA · Zinnen van de week (letterlijk uit dit nummer)', 1)
rep([C7], '"名单已提交：现在各党开始撰写纲领。"', '"De lijsten zijn ingediend: nu schrijven de partijen hun programma\'s."', 1)
rep([C7], '"11 月 2 日周一九个自治区放假，其他地区照常上班。"',
    '"Maandag 2 november is een feestdag in negen regio\'s — en een werkdag elders."', 1)
rep([C7], '"三个节日，同一个秋夜。"', '"Drie feesten, één herfstnacht."', 1)
rep([C7], '"皇马在诺坎普 2–1 获胜：这是巴萨本赛季联赛首败。"',
    '"Real Madrid won met 2–1 in Camp Nou: de eerste competitienederlaag van Barça dit seizoen."', 1)
rep([C7], '"伯纳乌把草皮换成烤架形球场：美式足球来到马德里。"',
    '"Het Bernabéu ruilt gras in voor het gridiron: American football komt naar Madrid."', 1)
rep([C7], '"住房是 55.7% 的西班牙人的首要问题。"', '"Huisvesting is het grootste probleem voor 55,7% van de Spanjaarden."', 1)
rep([C7], '"一次民调就是一张带误差的照片，拍于某一天。"',
    '"Een peiling is een momentopname met een foutmarge, van één dag."', 1)
rep([C7], '"11 月 8 日周日，马德里有两场约会：15:30 的 NFL 和 21:00 的马竞对巴萨。"',
    '"Op zondag 8 november heeft Madrid twee afspraken: de NFL om 15:30 en Atlético–Barça om 21:00."', 1)
rep([C7], 'LA PRÓXIMA SEMANA · 下期预告 (VOL.3)', 'LA PRÓXIMA SEMANA · Volgende week (VOL.3)', 1)

print('PART 5a OK')

# ---------- content7: P7 page tags (W43 ESxNL precedent) ----------
rep([C7], '"Página 1"', '"Pagina 1"', 2)
rep([C7], '"Página 2"', '"Pagina 2"', 1)
rep([C7], '"Página 3"', '"Pagina 3"', 1)
rep([C7], '"Página 4"', '"Pagina 4"', 1)
rep([C7], '"Página 5"', '"Pagina 5"', 1)
rep([C7], '"Página 6"', '"Pagina 6"', 2)

# ---------- content8: P8 ----------
rep([C8], '"ganó 2–1 = 以 2–1 获胜"', '"ganó 2–1 = won met 2–1"', 1)
rep([C8], '"marcar dos goles = 进两球"', '"marcar dos goles = scoorde twee doelpunten"', 1)
rep([C8], '"primera derrota liguera = 联赛首败"', '"primera derrota liguera = eerste competitienederlaag"', 1)
rep([C8], '"recortar = 缩小分差"', '"recortar = de achterstand verkleinen"', 1)
rep([C8], '"acoger = 承办（伯纳乌承办 NFL）"', '"acoger = organiseren (het Bernabéu organiseert de NFL)"', 1)
rep([C8], '"el emparrillado = 美式足球场"', '"el emparrillado = het gridiron"', 1)
rep([C8], '"周日上演马竞–巴萨"', '"zondag is het Atlético–Barça"', 1)
rep([C8], '"himno = 国歌"', '"himno = volkslied"', 1)
rep([C8], '"周一放假的自治区有 9 个"', '"negen regio\'s hebben maandag vrij"', 1)
rep([C8], '"诸圣节 11 月 1 日"', '"Allerheiligen: 1 november"', 1)
rep([C8], '"马竞–巴萨与 NFL 都在周日"', '"Atlético–Barça en de NFL zijn beide op zondag"', 1)
rep([C8], '"Castanyada 吃 panellets"', '"panellets horen bij de Castanyada"', 1)
rep([C8], '"DANA 纪念活动在 10 月 29 日周四"', '"de DANA-herdenking was op donderdag 29 oktober"', 1)
rep([C8], '"大选在 11 月 29 日"', '"de verkiezingen zijn op 29 november"', 1)
rep([C8], '"CIS 十月调查：住房 55,7%"', '"CIS, oktober: huisvesting 55,7%"', 1)
rep([C8], '"竞选 11 月 13 日开始"', '"de campagne begint op 13 november"', 1)
rep([C8], '"马德里在放假名单里"', '"Madrid staat op de feestdagenlijst"', 1)
rep([C8], '"加泰罗尼亚周一是工作日"', '"in Catalonië is maandag een werkdag"', 1)
rep([C8], '"Ana 只看 NFL；晚上看马竞–巴萨的是 Pablo"',
    '"Ana kijkt alleen naar de NFL; Pablo kijkt \'s avonds naar Atlético–Barça"', 1)
rep([C8], '"标题概括两地对比"', '"de titel vat het contrast tussen twee steden samen"', 1)
rep([C8], '"主语 + 动词 + 地点"', '"onderwerp + werkwoord + plaats"', 1)
rep([C8], '"时间在前"', '"tijd eerst"', 1)
rep([C8], '"a las nueve = 在九点"', '"a las nueve = om negen uur"', 1)
rep([C8], '"疑问词在句首"', '"het vraagwoord staat vooraan"', 1)
# E-section redirection (W43 ESxNL KIT ruling): ES<->NL, not ES<->ZH
rep([C8], '"周一在九个自治区是假日。"', '"Maandag is een feestdag in negen autonome regio\'s."', 1)
rep([C8], '"周日我们看 NFL 和马竞–巴萨。"', '"Op zondag kijken we naar de NFL en Atlético–Barça."', 1)
rep([C8], '"对照原文"', '"zie het origineel"', 2)
rep([C8], '"伯纳乌承办一场 NFL 比赛。→ ___"', '"Het Bernabéu organiseert een NFL-wedstrijd. → ___"', 1)
rep([C8], '"acoger = 承办"', '"acoger = organiseren"', 1)
rep([C8], '"每个图表都必须标明来源。→ ___"', '"Elke grafiek moet zijn bron vermelden. → ___"', 1)
rep([C8], '"tener que = 必须"', '"tener que = moeten"', 1)
rep([C8], '"sondeo=民调 c"', '"sondeo = een opiniepeiling — c"', 1)
rep([C8], '"muestra=样本 d"', '"muestra = de geïnterviewden — d"', 1)
rep([C8], '"margen de error=误差范围 b"', '"margen de error = foutmarge — b"', 1)
rep([C8], '"junta electoral=选举委员会 a"', '"junta electoral = het stembureau — a"', 1)
rep([C8], '"alquiler = 租金"', '"alquiler = huur"', 1)
rep([C8], '"tres habitaciones = 三居室"', '"tres habitaciones = drie slaapkamers"', 1)
rep([C8], '"¿cuánto cuesta? 多少钱"', '"¿cuánto cuesta? = hoeveel kost het?"', 1)
rep([C8], '"firmar = 签（合同）"', '"firmar = tekenen (het contract)"', 1)
rep([C8], '"mudanza = 搬家"', '"mudanza = verhuizen"', 1)
rep([C8], '"（开放题，范文如下）"', '"(open vraag — de voorbeeldtekst staat hieronder)"', 1)
rep([C8], '"范文见本版 H 区（84 词）"', '"voorbeeldtekst in deel H (84 woorden)"', 1)
rep([C8], 'RESPUESTAS · 参考答案 — 按版面分页排列，找到题号即可',
    'RESPUESTAS · Antwoorden — per pagina gerangschikt; zoek op nummer', 1)
rep([C8], '每题附一句中文简析 · 带 ✓ 的为范文题',
    'Bij elk antwoord een korte uitleg in het Nederlands · ✓ = met voorbeeldtekst', 1)
# P8 separators: NL family form (W43 ESxNL build code)
rep([C8], 'f"— PÁGINA {pg} —"', 'f"— Pagina {pg} —"', 1)

print('PART 5b OK — transform complete')
