# -*- coding: utf-8 -*-
"""W45 ES core -> ES x IT fan-out transform (asserted replacements).

Applies to the COPY at hidden_files/weekly-report-w45-es-it-build/.
Every replacement asserts its exact hit count across the tree; aborts on
mismatch. Spanish body text is never touched except the documented
apparatus items (P5 infinito paren, P7 letter parens, P8 137-140 re-aim).
Furniture verbatim from shipped W43 ES x IT (files/weekly-report-es-it/),
VOL.1 -> VOL.2 only. Bridge strings follow the W43 IT bare style (no
prefix word); gloss prefix is 'Nota — '.
"""
import os, sys

BUILD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-it-build")
FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py", "render.py"]

def load(f):
    p = os.path.join(BUILD, f)
    with open(p, encoding="utf-8") as fh:
        return fh.read()

def save(f, s):
    p = os.path.join(BUILD, f)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(s)

contents = {f: load(f) for f in FILES}

def rep(old, new, count):
    """Replace old->new across all files; total hits must equal count."""
    global contents
    total = 0
    for f in FILES:
        n = contents[f].count(old)
        if n:
            contents[f] = contents[f].replace(old, new)
            total += n
    if total != count:
        print(f"MISMATCH: {old[:70]!r} expected {count} got {total}")
        sys.exit(1)

def rep1(old, new):
    rep(old, new, 1)

# ---------- structural: OUT repoint + render names ----------
rep("weekly-report-w45-es-core", "weekly-report-w45-es-it", 6)
rep1('"La-Lucerna-VOL2.pdf"', '"La-Lucerna-VOL2-IT.pdf"')
rep1('"La-Lucerna-VOL2-web.pdf"', '"La-Lucerna-VOL2-IT-web.pdf"')
rep1("Render the ES core edition", "Render the ES x IT edition")

# ---------- bslib4: footer + gloss prefix ----------
rep1('"La Lucerna · 西班牙语周报 VOL.2 · LUCERNA SPANISH WEEKLY"',
     '"La Lucerna · SETTIMANALE SPAGNOLO VOL.2 · TESTI IN SPAGNOLO · SPIEGAZIONI IN ITALIANO"')
rep1('f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} di {total}"')
rep1('("译注｜" + s', '("Nota — " + s')

# ---------- P1 badge insert (W43 IT slot y=574, strapline y=372 retained) ----------
old_strap = 'p.text(975, 372, "EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA", 19, "sans", False, GREY, anchor="middle")'
new_strap = old_strap + '\np.text(975, 574, "TESTI IN SPAGNOLO · SPIEGAZIONI IN ITALIANO — L\'EDIZIONE PER I LETTORI ITALIANI", 22, "sans", True, BRICK, anchor="middle")'
rep1(old_strap, new_strap)

# ---------- instr labels (W43 IT mapping) ----------
rep('instr="填空"', 'instr="Completa"', 42)
rep('instr="判断"', 'instr="Vero o falso"', 8)
rep('instr="造句"', 'instr="Costruisci"', 7)
rep('instr="改写"', 'instr="Riscrivi"', 10)
rep('instr="翻译"', 'instr="Traduci"', 4)
rep('instr="写作"', 'instr="Scrivi"', 1)
rep('instr="把词和释义配对"', 'instr="Abbina le parole"', 3)

# ---------- apparatus parens (W43 IT precedent) ----------
rep1("（ejemplo, escrito por la redacción）", "(ejemplo, escrito por la redacción)")
rep1("# 盒高 = 绘制循环精确模拟（W43 回补修法：逐项模拟，不用平均行高）",
     "# altezza del riquadro = simulazione esatta del ciclo di disegno (correzione W43: simulazione voce per voce, non altezza media di riga)")

# ---------- shared furniture / headers ----------
rep("答案见第 8 版 · 题目可跨级混排，按题号找答案",
    "Risposte a pagina 8 · livelli misti: cerca per numero", 5)
rep("¿Y TÚ? · 说说你自己", "¿Y TÚ? · TOCCA A TE", 4)

# ================= P1 =================
rep1("CADA SEMANA EN ESPAÑOL · 每周一期 · 读西班牙人正在读的西班牙语",
     "CADA SEMANA EN ESPAÑOL · OGNI SETTIMANA · LO SPAGNOLO DEGLI SPAGNOLI")
rep1("西 班 牙 语 周 报 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL",
     "SETTIMANALE SPAGNOLO · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL")
rep1("距大选还有 27 天 · 住房决定选战",
     "MANCANO 27 GIORNI AL 29-N · LA CASA DECIDE LA CAMPAGNA")
rep1("本期头条 · 详见第 2、6 版", "Il tema di copertina · vedi le pagine 2 e 6")
rep1("LA NOTICIA · 头条", "LA NOTICIA · LA NOTIZIA")
rep1("讲解｜la cuenta atrás 倒计时 · disolver las Cortes 解散议会 · el decreto 法令 · la candidatura 候选人名单。",
     "la cuenta atrás il conto alla rovescia · disolver las Cortes sciogliere il Parlamento · el decreto il decreto · la candidatura la candidatura.")
rep1("LA SEMANA EN CIFRAS · 数字看本周", "LA SEMANA EN CIFRAS · IN CIFRE")
rep1("（距 29 日大选 27 天）", "(ancora 27 giorni alle elezioni di domenica 29)")
rep1("（11 月 2 日放假的自治区）", "(il 2 novembre è festa in 9 comunità)")
rep1("（CIS 十月数据）", "(dati CIS di ottobre)")
rep1("AHORA TÚ · 即学即练", "AHORA TÚ · TOCCA A TE")
rep("大选在 11 月 29 日周日", "le elezioni sono domenica 29 novembre", 1)
rep1("住房是选战的决定性议题", "la casa è il tema decisivo della campagna")
rep("周一放假的自治区有 9 个", "il lunedì è festa in nove comunità", 3)
rep1("马竞–巴萨周日 21:00 开球", "l'Atlético–Barça inizia domenica alle 21:00")
rep1("NFL 马德里站周日 15:30 开球", "la NFL a Madrid inizia domenica alle 15:30")
rep1("本周五大看点 · Para entender la semana", "Cinque chiavi · Para entender la semana")
rep1("五大看点，不编数字：全在本期里讲清。", "Cinque chiavi, zero numeri inventati.")
rep1("EN ESTA EDICIÓN · 本期目录", "EN ESTA EDICIÓN · IL NUMERO")
rep1("“竞选预热期”：正式竞选前的几周。", "«La precampagna»: prima della campagna.")
rep1("BREVES · 快讯", "BREVES · IN BREVE")
rep1("QUIZ RELÁMPAGO · 闪电问答", "QUIZ RELÁMPAGO · QUIZ LAMPO")
rep1("读头版，选出正确答案 · 答案见第 8 版",
     "Leggi la prima pagina e scegli la risposta giusta · risposte a pagina 8")
rep("大选在 11 月 29 日", "le elezioni sono il 29 novembre", 3)
rep1("NFL 马德里站周日下午", "la NFL a Madrid è domenica pomeriggio")
rep1("马竞–巴萨周日 21:00", "l'Atlético–Barça è domenica alle 21:00")

# ================= P2 =================
rep1("VIDA · 生活", "VIDA · VITA QUOTIDIANA")
rep1("NIVEL A2 · El puente del lunes 2 · 11 月 2 日的连休",
     "NIVEL A2 · El puente del lunes 2 · Il ponte di lunedì 2")
rep1("EL CALENDARIO · 本周日历", "EL CALENDARIO · IL CALENDARIO")
rep1("（周一九地连休；周二《官方公报》公布正式候选名单）",
     "(lunedì: ponte in nove comunità; martedì il BOE pubblica le liste ufficiali)")
rep1("（周二欧冠三场西甲球队比赛）", "(martedì: tre partite di Champions di squadre spagnole)")
rep1("（周三皇马客场对雅典 AEK）", "(mercoledì: il Real in trasferta contro l'AEK Atene)")
rep1("（周四皇家社会欧联对里昂）", "(giovedì: la Real Sociedad in Europa League contro il Lione)")
rep1("（周五联赛第 12 轮开球）", "(venerdì: inizia la 12ª giornata di Liga)")
rep1("（周六瓦伦西亚对皇马）", "(sabato: Valencia–Real Madrid)")
rep1("（周日 NFL 马德里站＋马竞对巴萨）", "(domenica: NFL a Madrid + Atlético–Barça)")
rep1("festivo 放假的 · el puente 连休 · la comunidad 自治区 · anochecer 天黑 · el horario de invierno 冬令时。",
     "festivo in festa · el puente il ponte · la comunidad la comunità autonoma · anochecer il calare della sera · el horario de invierno l'ora solare.")
rep("11 月 2 日你那里放假吗？连休你做什么：旅行、休息还是看球？写两句西班牙语寄给编辑部。",
     "Il 2 novembre da te è festa? E con il ponte cosa fai: viaggi, riposi o guardi calcio? Scrivi due frasi in spagnolo e mandale alla redazione.", 2)
rep1("LOS DÍAS DE LA SEMANA · 这样说日期", "LOS DÍAS DE LA SEMANA · DIRE LE DATE")
rep1("lunes 2 – domingo 8 de noviembre · 11 月 2 日周一至 8 日周日",
     "lunes 2 – domingo 8 de noviembre · da lunedì 2 a domenica 8 novembre")
rep1("EJERCICIOS · 第 2 版练习", "EJERCICIOS · ESERCIZI · PAGINA 2")
rep1("用正确的日期形式补全句子。", "Completa con la forma giusta della data.")
rep1("\"11 月 2 日周一\",", "\"lunedì 2 novembre\",")
rep1("\"11 月 8 日周日\",", "\"domenica 8 novembre\",")
# (大选在 11 月 29 日 already replaced globally above, count 3)
rep1("每月 1 号说 el uno", "il giorno 1 si dice el uno")
rep1("\"月份小写\",", "\"i mesi si scrivono in minuscolo\",")
rep1("补全动词的现在时形式。", "Completa con il presente del verbo.")
rep1("el lunes → es（单数）", "el lunes → es (singolare)")
rep1("读第 2 版文章，选出正确答案。", "Leggi l'articolo di pagina 2 e scegli la risposta giusta.")
rep1("九个自治区周一放假", "il lunedì è festa in nove comunità")
rep1("诸圣节 11 月 1 日落在周日", "Ognissanti, il 1º novembre, cade di domenica")
rep("加泰罗尼亚周一是工作日", "in Catalogna il lunedì si lavora", 2)
rep1("冬令时第二周，天黑得早", "seconda settimana di ora solare: fa buio presto")
rep1("puente=三天连休 b", "puente=ponte di tre giorni b")
rep1("festivo=放假的 a", "festivo=di festa a")
rep1("anochecer=天黑 c", "anochecer=il far buio c")
rep1("comunidad=自治区 d", "comunidad=comunità autonoma d")

# ================= P3 =================
rep1("CULTURA · 文化", "CULTURA · CULTURA")
rep1("A2 → B1 · La semana pasada: tres noches de otoño · 上周的三个秋夜",
     "A2 → B1 · La semana pasada: tres noches de otoño · Tre notti d'autunno, la settimana scorsa")
rep1("sobrio 克制的 · el homenaje 纪念表彰 · el disfraz 服装（化装） · el boniato 红薯 · el cementerio 墓地。",
     "sobrio sobrio, composto · el homenaje l'omaggio · el disfraz il costume · el boniato la patata dolce · el cementerio il cimitero.")
rep("你最喜欢哪一夜：29 日、31 日还是 1 日？31 日你吃了什么？写两句寄来。",
     "Quale notte preferisci: quella del 29, del 31 o del 1º? E il 31 cosa hai mangiato? Scrivi due frasi e mandale.", 2)
rep1("EJERCICIOS · 第 3 版练习", "EJERCICIOS · ESERCIZI · PAGINA 3")
rep1("读第 3 版文章，判断对错。", "Leggi l'articolo di pagina 3 e di' se è vero o falso.")
rep("DANA 纪念活动在 10 月 29 日周四", "gli atti in memoria della DANA sono stati giovedì 29 ottobre", 2)
rep1("Castanyada 吃烤栗子、红薯和 panellets",
     "alla Castanyada si mangiano castagne arrosto, patate dolci e panellets")
rep1("Samaín 是加利西亚古节，不是万圣节译名",
     "il Samaín è un'antica festa galiziana, non la traduzione di Halloween")
rep1("诸圣节在 11 月 1 日，不是 10 月 31 日", "Ognissanti è il 1º novembre, non il 31 ottobre")
rep1("周日家属去墓地献花", "domenica le famiglie hanno portato fiori ai cimiteri")
rep1("\"用方框里的词填空。\"", "\"Completa con le parole del riquadro.\"")
rep1("给逝者带花 flores", "per i defunti si portano fiori: flores")
rep1("cementerio = 墓地", "cementerio = cimitero")
rep1("castañas asadas 烤栗子", "castañas asadas = castagne arrosto")
rep("disfraz = 化装服装", "disfraz = costume", 2)
rep1("actos de memoria 纪念活动", "actos de memoria = atti in memoria")
rep1("\"选出正确答案。\"", "\"Scegli la risposta giusta.\"")
rep1("DANA 纪念是 2024 年风暴两周年", "la memoria della DANA è il secondo anniversario della tempesta del 2024")
rep1("Castanyada 在加泰罗尼亚", "la Castanyada è in Catalogna")
rep1("Samaín 是加利西亚古老节日", "il Samaín è un'antica festa galiziana")
rep1("三夜之后周一有人连休有人上班", "dopo le tre notti, lunedì c'è chi fa ponte e chi lavora")
rep1("把词组成正确的句子。", "Metti le parole in ordine e forma la frase giusta.")
rep1("动词第二位", "il verbo va al secondo posto")
rep1("时间在前，动词第二", "il tempo prima, il verbo secondo")
rep1("地点在前，动词第二", "il luogo prima, il verbo secondo")
rep1("间接疑问用 si", "la domanda indiretta usa si")

# ================= P4 =================
rep1("DEPORTE · 体育", "DEPORTE · SPORT")
rep1("NIVEL B1 · Europa primero, el domingo a las 21:00 · 欧战在先，周日晚九点",
     "NIVEL B1 · Europa primero, el domingo a las 21:00 · Prima l'Europa, domenica alle 21:00")
rep1("la jornada 轮次 · recortar la distancia 缩小分差 · recibir 主场迎战 · visitar 客场挑战 · el Metropolitano 马竞主场。",
     "la jornada la giornata · recortar la distancia ridurre il distacco · recibir giocare in casa contro · visitar giocare in trasferta contro · el Metropolitano lo stadio dell'Atlético.")
rep("周日 21:00 你看哪一场？马竞主场谁赢？写两句西班牙语寄来。",
     "Domenica alle 21:00 quale partita guardi? E in casa dell'Atlético chi vince? Scrivi due frasi in spagnolo e mandale.", 2)
rep1("LA SEMANA EUROPEA Y LA JORNADA 12 · 欧战周与联赛第 12 轮",
     "LA SEMANA EUROPEA Y LA JORNADA 12 · LA SETTIMANA EUROPEA E LA 12ª GIORNATA")
rep1("EJERCICIOS · 第 4 版练习", "EJERCICIOS · ESERCIZI · PAGINA 4")
rep1("读第 4 版文章，选出正确答案。", "Leggi l'articolo di pagina 4 e scegli la risposta giusta.")
rep1("皇马 2–1 赢下国家德比", "il Real ha vinto il Clásico 2–1")
rep1("姆巴佩进了两球", "Mbappé ha segnato due gol")
rep1("周二欧冠三场西甲球队比赛", "martedì tre partite di Champions di squadre spagnole")
rep1("周日 21:00 马竞–巴萨", "domenica alle 21:00 Atlético–Barça")
rep1("周日下午还有 NFL 马德里站", "domenica pomeriggio c'è anche la NFL a Madrid")
rep1("jornada=轮次 b", "jornada=giornata b")
rep1("recibir=主场迎战 a", "recibir=giocare in casa contro a")
rep1("visitar=客场挑战 d", "visitar=giocare in trasferta contro d")
rep1("recortar=缩小分差 c", "recortar=ridurre il distacco c")
rep1("用括号里词的比较级或 -ísimo 形式填空。",
     "Completa con il comparativo o la forma in -ísimo della parola tra parentesi.")
rep1("más + importante（马竞–巴萨更重要）", "más + importante (l'Atlético–Barça è più importante)")
rep1("muchísimos partidos 比赛很多", "muchísimos partidos = moltissime partite")
rep1("malo 的比较级是 peor", "il comparativo di malo è peor")
rep1("\"bueno 的比较级是 mejor\",", "\"il comparativo di bueno è mejor\",")
rep1("把句子改成过去时（pretérito indefinido）。", "Metti le frasi al passato (pretérito indefinido).")
rep1("ir 的过去时是 fueron", "il passato di ir è fueron")

# ================= P5 =================
rep1("JUVENTUD · 青年", "JUVENTUD · GIOVENTÙ")
rep1("NIVEL B1 · La NFL en Madrid · NFL 来到马德里",
     "NIVEL B1 · La NFL en Madrid · La NFL arriva a Madrid")
rep1("EL PLAN DEL PUENTE · 连休计划", "EL PLAN DEL PUENTE · IL PIANO")
rep1("（周一：休息陪家人；若你那里连休，就去旅行）",
     "(lunedì: riposo e famiglia — o viaggio, se la tua comunità fa ponte)")
rep1("（周六晚：瓦伦西亚对皇马）", "(sabato sera: Valencia–Real Madrid)")
rep1("（周日下午：NFL 马德里站）", "(domenica pomeriggio: la NFL al Bernabéu)")
rep1("（周日晚：马竞对巴萨）", "(domenica sera: Atlético–Barça al Metropolitano)")
rep1("（返校返工；竞选 13 日开始）", "(ritorno a scuola e al lavoro; la campagna inizia venerdì 13)")
rep1("el emparrillado 美式足球场（烤架形场地） · el himno 国歌 · el touchdown 达阵得分 · la calabaza 南瓜。",
     "el emparrillado il campo da football americano (a forma di griglia) · el himno l'inno · el touchdown il touchdown, la meta · la calabaza la zucca.")
rep("你看过美式足球比赛吗？你更喜欢足球还是美式足球？写两句寄来。",
     "Hai mai visto una partita di football americano? Preferisci il calcio o il football americano? Scrivi due frasi e mandale.", 2)
rep1("EJERCICIOS · 第 5 版练习", "EJERCICIOS · ESERCIZI · PAGINA 5")
rep1("读第 5 版文章，选出正确答案。", "Leggi l'articolo di pagina 5 e scegli la risposta giusta.")
rep1("NFL 马德里站周日 15:30", "la NFL a Madrid è domenica alle 15:30")
rep1("孟加拉虎对猎鹰", "Bengals contro Falcons")
rep1("西班牙国歌由吉他手演奏", "l'inno spagnolo è suonato con la chitarra")
rep1("首场 NFL 伯纳乌赛在 2025 年 11 月 16 日", "la prima NFL al Bernabéu è stata il 16 novembre 2025")
rep1("美式足球用手打、四次进攻", "il football americano si gioca con le mani, con quattro tentativi")
rep1("用方框里的词填空。注意：有的词要变位。",
     "Completa con le parole del riquadro. Attenzione: alcune vanno coniugate.")
rep1("estadio = 体育场", "estadio = stadio")
rep("himno = 国歌", "himno = inno", 2)
rep1("acoger 变位 → acoge", "acoger coniugato → acoge")
rep1("(原形 acoger)", "(infinito: acoger)")
rep1("touchdown = 达阵得分", "touchdown = meta")
rep1("calabaza = 南瓜", "calabaza = zucca")
rep1("用 ir a + 原形动词改写句子，表示“将要”。",
     "Riscrivi con ir a + infinito, per dire che cosa succederà.")
rep1("vamos a + 原形", "vamos a + infinito")
rep1("va a + 原形", "va a + infinito")
rep1("vas a + 原形", "vas a + infinito")
rep1("van a + 原形", "van a + infinito")
rep1("NFL 马德里站是伯纳乌第二场 NFL 比赛", "la NFL di domenica è la seconda al Bernabéu")
rep1("美国国歌由 Momsen 演唱，不是 Sáinz-Villegas",
     "l'inno degli Stati Uniti lo canta Momsen, non Sáinz-Villegas")
rep1("万圣节之夜在周六 31 日", "la notte di Halloween è stata sabato 31")

# ================= P6 =================
rep1("A FONDO · 深读", "A FONDO · APPROFONDIMENTO")
rep1("NIVEL B2 · La vivienda decide la campaña · 住房决定选战",
     "NIVEL B2 · La vivienda decide la campaña · La casa decide la campagna")
rep1("EJERCICIOS · 第 6 版练习", "EJERCICIOS · ESERCIZI · PAGINA 6")
rep1("看上面两张图，选出正确答案。", "Guarda i due grafici qui sopra e scegli la risposta giusta.")
rep1("CIS 里 PSOE 第一（34%）", "nel CIS il PSOE è primo (34%)")
rep1("CIS 里 PP 22,2%", "nel CIS il PP è al 22,2%")
rep1("住房是首要问题（55,7%）", "la casa è il primo problema (55,7%)")
rep1("调查在 10 月 1–6 日进行", "il sondaggio è stato fatto dal 1º al 6 ottobre")
# digits-only note 34 + 22,2 + 17,1 = 73,3 kept byte-identical (ES x FR precedent)
rep1("本报只刊登 CIS 这一组数据并注明来源日期",
     "questo giornale pubblica solo la serie CIS, con fonte e data")
rep1("10 月 2 日议会否决两项住房法令", "il 2 ottobre il Parlamento ha respinto due decreti sulla casa")
rep1("10 月 5 日解散议会并召集大选",
     "il 5 ottobre scioglimento del Parlamento e convocazione delle elezioni")
rep1("民调是带误差的具体某天的照片",
     "un sondaggio è una foto con margine di errore, scattata in un giorno preciso")
rep("竞选 11 月 13 日开始", "la campagna inizia il 13 novembre", 2)
rep1("es posible que + 虚拟式 tenga", "es posible que + congiuntivo: tenga")
rep1("es importante que + 虚拟式 sea", "es importante que + congiuntivo: sea")
rep1("para que + 虚拟式（目的）", "para que + congiuntivo (scopo)")
rep1("Aunque 后接陈述式（已知事实）", "Aunque + indicativo (fatto noto)")
rep1("用方框里的词填空：sondeo · muestra · indecisos · margen de error",
     "Completa con le parole del riquadro: sondeo · muestra · indecisos · margen de error")
rep1("sondeo = 民调", "sondeo = sondaggio")
rep1("muestra = 样本（5.025 人）", "muestra = campione (5.025 persone)")
rep1("indecisos = 未决定者", "indecisos = indecisi")
rep1("margen de error = 误差范围", "margen de error = margine di errore")

# ================= P7 =================
rep1("LENGUA · 语言", "LENGUA · LA LINGUA")
rep1("语言聚焦 · Tres niveles, tres herramientas · 三个级别，三件工具",
     "Focus lingua · Tres niveles, tres herramientas · Tre livelli, tre strumenti")
rep1("日期格式：el lunes 2 de noviembre；星期、月份小写；1 号说 el uno。",
     "Il formato della data: el lunes 2 de noviembre; giorni e mesi in minuscolo; il giorno 1 si dice el uno.")
rep1("el lunes 2 de noviembre 连休", "el lunes 2 de noviembre, giorno di ponte")
rep1("el 1 = el uno", "il giorno 1 = el uno")
rep1("29 日是周日", "il 29 è domenica")
rep1("月份小写：noviembre", "i mesi in minuscolo: noviembre")
rep1("比较级 más…que、tan…como；bueno→mejor、malo→peor；绝不说 más mejor。",
     "Il comparativo: más…que, tan…como; bueno→mejor, malo→peor; mai dire más mejor.")
rep1("más + cara（房价更高）", "más + cara (la casa è più cara)")
rep1("tan + alta + como（同样高）", "tan + alta + como (alta come)")
rep1("bueno 的比较级是 mejor（不用 más）", "il comparativo di bueno è mejor (senza más)")
rep1("más mejor 是错误说法", "más mejor è una forma sbagliata")
rep1("es necesario que、para que、ojalá 后用虚拟式；creo que 后用陈述式。",
     "es necesario que, para que e ojalá + congiuntivo; creo que + indicativo.")
rep1("es necesario que + 虚拟式 baje", "es necesario que + congiuntivo: baje")
rep1("para que + 虚拟式 sea", "para que + congiuntivo: sea")
rep1("creo que + 陈述式 es", "creo que + indicativo: es")
rep1("ojalá + 虚拟式：baje", "ojalá + congiuntivo: baje")
rep1("lunes 是单数，动词用 es。", "lunes è singolare: il verbo è es.")
rep1("mejor 本身就是比较级，不加 más。", "mejor è già un comparativo: niente más.")
rep1("gente 是单数集合名词，动词用单数。", "gente è singolare: verbo al singolare.")
rep1("creo que 表肯定，用陈述式 es。", "creo que afferma: indicativo, es.")
rep1("ERRORES TÍPICOS · 常见错误", "ERRORES TÍPICOS · ERRORI TIPICI")
rep1("LA PALABRA · 本周生词", "LA PALABRA · LA PAROLA")
rep("precampaña = 竞选预热期：正式竞选前的几周。本期就是 precampaña；竞选 13 日周五开始。",
     "precampaña = precampagna: prima della campagna ufficiale.", 2)
rep1("编辑部说明：截至本期截稿，未收到真实读者来信与第 8 版最佳作文，故本期登载编辑部示例信，承诺顺延至 VOL.3。欢迎来信！",
     "Nota della redazione: senza lettere vere né migliori testi di pagina 8, pubblichiamo questo esempio; la promessa passa al VOL.3. Scriveteci!")
rep1("FRASES DE LA SEMANA · 本周金句（逐字摘自本期文章）",
     "FRASES DE LA SEMANA · LE FRASI DELLA SETTIMANA (testuali, da questo numero)")
rep1("名单已提交：现在各党开始撰写纲领。", "Le liste sono presentate: ora i partiti scrivono i programmi.")
rep1("11 月 2 日周一九个自治区放假，其他地区照常上班。",
     "Lunedì 2 novembre è festa in nove comunità e giorno di lavoro nelle altre.")
rep1("三个节日，同一个秋夜。", "Tre feste, una stessa notte d'autunno.")
rep1("皇马在诺坎普 2–1 获胜：这是巴萨本赛季联赛首败。",
     "Il Real vince 2–1 al Camp Nou: è la prima sconfitta in Liga del Barça.")
rep1("伯纳乌把草皮换成烤架形球场：美式足球来到马德里。",
     "Il Bernabéu cambia l'erba con la griglia: il football americano arriva a Madrid.")
rep1("住房是 55.7% 的西班牙人的首要问题。", "La casa è il primo problema per il 55,7% degli spagnoli.")
rep1("一次民调就是一张带误差的照片，拍于某一天。",
     "Un sondaggio è una foto con margine di errore, scattata in un giorno preciso.")
rep1("11 月 8 日周日，马德里有两场约会：15:30 的 NFL 和 21:00 的马竞对巴萨。",
     "Domenica 8, Madrid ha due appuntamenti: la NFL alle 15:30 e l'Atlético–Barça alle 21:00.")
rep1("LA PRÓXIMA SEMANA · 下期预告 (VOL.3)", "LA PRÓXIMA SEMANA · LA PROSSIMA SETTIMANA (VOL.3)")

# ================= P8 =================
rep1("EJERCICIOS Y RESPUESTAS · 练习与答案", "EJERCICIOS Y RESPUESTAS · ESERCIZI E RISPOSTE")
rep1("第 8 版 · La gran prueba de la semana + todas las respuestas",
     "Pagina 8 · La gran prueba de la semana + todas las respuestas")
rep1("ganó 2–1 = 以 2–1 获胜", "ganó 2–1 = ha vinto 2–1")
rep1("marcar dos goles = 进两球", "marcar dos goles = segnare due gol")
rep1("primera derrota liguera = 联赛首败", "primera derrota liguera = prima sconfitta in Liga")
rep1("recortar = 缩小分差", "recortar = ridurre il distacco")
rep1("acoger = 承办（伯纳乌承办 NFL）", "acoger = ospitare (il Bernabéu ospita la NFL)")
rep1("el emparrillado = 美式足球场", "el emparrillado = il campo da football americano")
rep1("周日上演马竞–巴萨", "domenica si gioca l'Atlético–Barça")
# B notes: 周一放假... / 大选在 11 月 29 日 already replaced globally above
rep1("诸圣节 11 月 1 日", "Ognissanti, il 1º novembre")
rep1("马竞–巴萨与 NFL 都在周日", "l'Atlético–Barça e la NFL sono entrambi domenica")
rep1("Castanyada 吃 panellets", "alla Castanyada si mangiano i panellets")
rep1("CIS 十月调查：住房 55,7%", "sondaggio CIS di ottobre: la casa al 55,7%")
rep1("马德里在放假名单里", "Madrid è nella lista delle feste")
rep1("Ana 只看 NFL；晚上看马竞–巴萨的是 Pablo",
     "Ana vede solo la NFL; la sera l'Atlético–Barça lo vede Pablo")
rep1("标题概括两地对比", "il titolo riassume il confronto tra due luoghi")
rep1("主语 + 动词 + 地点", "soggetto + verbo + luogo")
rep1("时间在前", "il tempo prima")
rep1("a las nueve = 在九点", "a las nueve = alle nove")
rep1("疑问词在句首", "la parola interrogativa all'inizio")
# E: translation items re-aimed (W43 IT registry pattern)
rep1("周一在九个自治区是假日。", "Il lunedì è festivo in nove comunità.")
rep1("周日我们看 NFL 和马竞–巴萨。", "La domenica vediamo la NFL e l'Atlético–Barça.")
rep("对照原文", "confronta con l'originale", 2)
rep1("伯纳乌承办一场 NFL 比赛。→ ___", "Il Bernabéu ospita una partita di NFL. → ___")
rep1("acoger = 承办", "acoger = ospitare")
rep1("每个图表都必须标明来源。→ ___", "Ogni grafico deve indicare la sua fonte. → ___")
rep1("tener que = 必须", "tener que = dovere")
rep1("sondeo=民调 c", "sondeo=sondaggio c")
rep1("muestra=样本 d", "muestra=campione d")
rep1("margen de error=误差范围 b", "margen de error=margine di errore b")
rep1("junta electoral=选举委员会 a", "junta electoral=commissione elettorale a")
rep1("alquiler = 租金", "alquiler = affitto")
rep1("tres habitaciones = 三居室", "tres habitaciones = trilocale")
rep1("¿cuánto cuesta? 多少钱", "¿cuánto cuesta? = quanto costa?")
rep1("firmar = 签（合同）", "firmar = firmare (il contratto)")
rep1("mudanza = 搬家", "mudanza = trasloco")
rep1("写作题（无唯一答案）；范文（84 词）见下。",
     "Esercizio di scrittura (senza un'unica risposta); il testo modello (84 parole) è qui sotto.")
rep1("（开放题，范文如下）", "(domanda aperta — il modello è qui sotto)")
rep1("范文见本版 H 区（84 词）", "Il modello è nella sezione H di questa pagina (84 parole)")
rep1("RESPUESTAS · 参考答案 — 按版面分页排列，找到题号即可",
     "RESPUESTAS · LE RISPOSTE — ordinate per pagina: cerca il numero")
rep1("每题附一句中文简析 · 带 ✓ 的为范文题",
     "Una nota in italiano per ogni risposta · ✓ = testo modello")

# ---------- write back + residual CJK audit ----------
for f in FILES:
    save(f, contents[f])

import re
print("transform applied OK")
for f in FILES:
    s = contents[f]
    hits = [(i + 1, ln) for i, ln in enumerate(s.splitlines())
            if re.search(r'[\u4e00-\u9fff]', ln)]
    print(f, "residual CJK lines:", len(hits))
    for i, ln in hits:
        print("   ", f, i, ln[:110])

# ---------- in-build fit fixes (applied after the translation pass) ----------
# P6: bridge A 2 lines -> 1 line + exercise gap 3 -> 1 on all 18 size-19
# items (W45 ES x FR precedent); P8: answer lines 13.5/1.16 -> 13.2/1.12
# (W45 ES x FR / ES x EN precedent). Without these the first full build
# reported P6-ex overflow to y=2662 and P8-keys overflow to y=2582.
for _f, _pairs in [
    ("content56.py", [
        ('e.bridge("Guarda i due grafici qui sopra e scegli la risposta giusta.")',
         'e.bridge("Guarda i grafici e scegli.")'),
    ]),
    ("content8.py", [
        ('af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
         'af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.12, gap=2, split=False)'),
        ('af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)',
         'af.para(txt, 13.2, lh=1.12, gap=0.5, split=False)'),
    ]),
]:
    _p = os.path.join(BUILD, _f)
    _s = open(_p, encoding="utf-8").read()
    for _a, _b in _pairs:
        assert _s.count(_a) == 1, (_f, _a)
        _s = _s.replace(_a, _b)
    if _f == "content56.py":
        _head, _tail = _s.split("# ---- P6 exercises ----", 1)
        _tail2 = _tail.replace("size=19, gap=3", "size=19, gap=1")
        assert _tail2.count("size=19, gap=1") == 18
        _s = _head + "# ---- P6 exercises ----" + _tail2
    open(_p, "w", encoding="utf-8").write(_s)
print("fit fixes applied")

# P7 palabra box-bottom graze (W45 ES x FR precedent, same 0.5px numbers):
# Latin descenders end 0.5px past the box border the core's CJK ink clears;
# box height +2px (col-3 ends move 1820.08 -> 1822.08, preview 2442.08).
_p = os.path.join(BUILD, "content7.py")
_s = open(_p, encoding="utf-8").read()
_a = 'wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("precampaña = precampagna: prima della campagna ufficiale.", "sans", False, 20, CW - 44)) * 29 + 20'
assert _s.count(_a) == 1, "palabra wh line"
_s = _s.replace(_a, _a[:-2] + "22")
open(_p, "w", encoding="utf-8").write(_s)
print("palabra box +2px applied")
