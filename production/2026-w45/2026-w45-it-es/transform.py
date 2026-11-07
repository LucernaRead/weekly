# -*- coding: utf-8 -*-
"""IT x ES fan-out transform for W45 IT core build copy.
Rules: whole-string or exact-unique-literal replacements with count
assertions; value maps use bare text, never repr. Italian body text is
NEVER touched: every `old` below is a Chinese explanation-layer string,
a bilingual furniture string, or a printed instruction token.
Furniture follows the shipped W43 IT x ES SVG verbatim (badge string,
footer VOL.2, Pagina N de 8, gloss prefix Nota, P8 separators PAGINA,
instruction words Completa/Empareja/Escribe/Forma la frase/Traduce/
Verdadero o falso, section-head Spanish halves) -- the tasking brief
rules that the W43 same-pair shipped SVG outranks the README #20
generalisation. Badge geometry follows the W43 shipped instance:
y=372, 20pt bold BRICK, replacing the masthead strapline slot (the
W43 core carried the identical strapline and its ES edition replaced
it; the W45 DE/EN/FR 574-insertion is the other families' W45 choice,
not this pair's shipped precedent). Edition line at y=330 is shortened
to fit the frame (measured 1763.8px at 46pt; the full SEMANARIO form
measures 1899.8px and would cross the frame).
P7 word-box rule: the Italian definition sentence (wt) is byte-frozen;
only the Spanish gloss note below it is localised.
P8 section E: items 137/138/139 keep their Italian stems and re-aim
Italian -> Spanish (keys become Spanish); item 140 keeps its Italian
key byte-identical and its stem is re-aimed Chinese -> Spanish.
Registry type tokens (Chinese) are never printed and stay byte-identical
(DE precedent); only printed instr tokens are localised.
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
    rep(f, "weekly-report-w45-it-core", "weekly-report-w45-it-es", 1)
rep("render.py", "weekly-report-w45-it-core", "weekly-report-w45-it-es", 1)
rep("render.py", "La-Lucerna-VOL2.pdf", "La-Lucerna-VOL2-ES.pdf", 1)
rep("render.py", "La-Lucerna-VOL2-web.pdf", "La-Lucerna-VOL2-ES-web.pdf", 1)

# ---------- svglib docstring comment only (not rendered) ----------
rep("svglib.py", "for 重阳.", "for Double Ninth.", 1)

# ---------- bslib4: furniture + gloss prefix (W43 IT x ES shipped forms, VOL.2) ----------
rep("bslib4.py",
    '"La Lucerna · 意大利语周报 VOL.2 · LUCERNA ITALIAN WEEKLY"',
    '"La Lucerna · SEMANARIO ITALIANO VOL.2 · TEXTO EN ITALIANO · EXPLICACIONES EN ESPAÑOL"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Nota — " + s', 1)

# ---------- shared printed instruction tokens (only where present) ----------
INSTR = [
    ('instr="填空"', 'instr="Completa"'),
    ('instr="造句"', 'instr="Forma la frase"'),
    ('instr="翻译"', 'instr="Traduce"'),
    ('instr="判断"', 'instr="Verdadero o falso"'),
    ('instr="写作"', 'instr="Escribe"'),
    ('instr="把词和释义配对"', 'instr="Empareja"'),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Respuestas en la página 8 · busca por número de ejercicio"),
    ("E TU? · 说说你自己", "E TU? · ¿Y TÚ?"),
]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTR:
        rep_if(f, old, new)

# ================= content12 (P1 + P2) =================
pairs("content12.py", [
    ("OGNI SETTIMANA IN ITALIANO · 每周一期 · 读意大利人正在读的意大利语",
     "OGNI SETTIMANA IN ITALIANO · CADA SEMANA · EL ITALIANO QUE LEE ITALIA"),
    ("意 大 利 语 周 报 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A",
     "SEMANARIO ITALIANO · VOL.2 · IL PRIMO FREDDO · PANETTONE · SERIE A"),
    # masthead strapline slot -> pairing badge (W43 shipped geometry: y=372, 20pt bold BRICK)
    ('p.text(975, 372, "IL GIORNALE SETTIMANALE PER IMPARARE — L\'ITALIA VERA, IN ITALIANO, DALL\'ITALIA", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "TEXTOS EN ITALIANO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 20, "sans", True, BRICK, anchor="middle")'),
    ('p.text(RIGHT - 30, 478, "本周迎来第一场寒冷", 24, "sans", True, "#b3a06a", anchor="end")\n'
     'p.text(RIGHT - 30, 522, "初寒之周 · 详见第 2 版", 21, "sans", False, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 478, "ESTA SEMANA LLEGA EL PRIMER FRÍO", 24, "sans", True, "#b3a06a", anchor="end")\n'
     'p.text(RIGHT - 30, 522, "La semana del primer frío · ver página 2", 21, "sans", False, "#b3a06a", anchor="end")'),
    ("LA NOTIZIA · 头条", "LA NOTIZIA · EL TITULAR"),
    ("讲解｜il primo freddo 第一场寒冷 · il versante adriatico 亚得里亚海一侧 · la previsione 预报 · assaggi 品尝。",
     "Nota — il primo freddo = el primer frío · il versante adriatico = la vertiente adriática · la previsione = la previsión · assaggi = degustaciones."),
    ("LA SETTIMANA IN CIFRE · 数字看本周", "LA SETTIMANA IN CIFRE · EN CIFRAS"),
    ("（可能下初雪的海拔）", "(posible cota de la primera nieve)"),
    ("（米兰文化论坛 50 多场活动）", "(más de 50 eventos del Forum Cultura de Milán)"),
    ("（参加米兰潘妮托尼决赛的国家数）", "(países en la final del Panettone en Milán)"),
    ("（本周末意甲第 11 轮）", "(11.ª jornada de la Serie A del fin de semana)"),
    ("ADESSO TU · 即学即练", "ADESSO TU · AHORA TÚ"),
    ("il primo freddo = 第一场寒冷", "il primo freddo = el primer frío"),
    ("la prima neve leggera = 初雪", "la prima neve leggera = la primera nieve ligera"),
    ("文化论坛与潘妮托尼决赛都在米兰", "El Forum Cultura y la final del Panettone están en Milán"),
    ("克雷莫纳的节日叫 Festa del Torrone", "La fiesta de Cremona se llama Festa del Torrone"),
    ("意甲第 11 轮周日收官", "La 11.ª jornada termina el domingo"),
    ("previsioni = 预报（复数）", "previsioni = previsiones (plural)"),
    ("本周日程 · Cosa succede, giorno per giorno", "La semana · Cosa succede, giorno per giorno"),
    ("日程以各活动日历为准，时间可能有变。", "Fechas según los calendarios; horarios variables."),
    ("IN QUESTO NUMERO · 本期目录", "IN QUESTO NUMERO · ÍNDICE"),
    ("“第一场寒冷”：温和秋天后的第一波寒冷。", "«il primo freddo»: el primer frío serio tras un otoño suave."),
    ("IN BREVE · 快讯", "IN BREVE · EN BREVE"),
    ("QUIZ LAMPO · 闪电问答", "QUIZ LAMPO · QUIZ RELÁMPAGO"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Lee la portada y elige la respuesta correcta · respuestas en la página 8"),
    ("第一场寒冷在周一 11 月 2 日到来", "El primer frío llega el lunes 2 de noviembre"),
    ("初雪在 1300–1500 米左右", "La primera nieve, hacia los 1.300–1.500 metros"),
    ("潘妮托尼决赛在米兰", "La final del Panettone es en Milán"),
    # P2
    ("VITA · 生活", "VITA · VIDA COTIDIANA"),
    ("LIVELLO A2 · Il primo freddo e il 2 novembre · 初寒与追思日",
     "LIVELLO A2 · Il primo freddo e il 2 novembre · Primer frío y Día de Difuntos"),
    ("发稿时表决结果尚未确认，详见第 6 版。", "Al cierre, el resultado de la votación aún no estaba confirmado: ver página 6."),
    ("LA FRASE PER RICORDARE · 口诀", "LA FRASE PER RICORDARE · LA CLAVE"),
    ("il cappotto 大衣 · la sciarpa 围巾 · i guanti 手套 · a strati 分层穿衣 · il termosifone 暖气片 · il crisantemo 菊花",
     "il cappotto = abrigo · la sciarpa = bufanda · i guanti = guantes · a strati = en capas · il termosifone = radiador · il crisantemo = crisantemo"),
    ("初寒来了你穿什么：大衣、围巾还是手套？写两句意大利语寄给编辑部。",
     "¿Con qué te abrigas cuando llega el primer frío: abrigo, bufanda o guantes? Escribe dos frases en italiano y envíalas a la redacción."),
    ("IL 2 NOVEMBRE · 追思日", "IL 2 NOVEMBRE · DÍA DE DIFUNTOS"),
    ("ESERCIZI · 第 2 版练习", "ESERCIZI · EJERCICIOS DE LA PÁGINA 2"),
    ("用意大利语补全句子。", "Completa las frases en italiano."),
    ("cappotto = 大衣", "cappotto = abrigo"),
    ("sciarpa = 围巾", "sciarpa = bufanda"),
    ("guanti = 手套（复数）", "guanti = guantes (plural)"),
    ("crisantemi = 菊花（复数）", "crisantemi = crisantemos (plural)"),
    ("termosifoni = 暖气片（复数）", "termosifoni = radiadores (plural)"),
    ("补全动词的现在时形式。", "Completa con el presente del verbo."),
    ("fare freddo：fa freddo（天气）", "fare freddo: fa freddo (tiempo)"),
    ("mettere：io → metto", "mettere: io → metto"),
    ("portare：loro → portano", "portare: loro → portano"),
    ("guardare：loro → guardano", "guardare: loro → guardano"),
    ("restare：la scuola → resta（lei）", "restare: la scuola → resta (lei)"),
    ("读第 2 版文章，选出正确答案。", "Lee el artículo de la página 2 y elige la respuesta correcta."),
    ("11 月 2 日是追思日", "El 2 de noviembre es el Día de Difuntos"),
    ("追思日的花是菊花", "La flor del 2 de noviembre es el crisantemo"),
    ("分层穿衣：a strati", "Vestirse a strati: en capas"),
    ("诸圣节今年是周日、无连休", "Ognissanti este año cae en domingo, sin puente"),
    ("cappotto=御寒大衣 c", "cappotto=abrigo de invierno c"),
    ("sciarpa=围巾 d", "sciarpa=bufanda d"),
    ("crisantemo=十一月的花 a", "crisantemo=flor de noviembre a"),
    ("termosifone=暖气片 b", "termosifone=radiador b"),
])
print("content12 done")

# ================= content34 (P3 + P4) =================
pairs("content34.py", [
    ("CULTURA · 文化", "CULTURA · CULTURA"),
    ("A2 → B1 · Panettone, torrone e musei aperti · 甜点与博物馆",
     "A2 → B1 · Panettone, torrone e musei aperti · Dulces y museos abiertos"),
    ("il panettone 米兰圣诞面包 · il torrone 牛轧糖 · l'assaggio 品尝 · la bancarella 摊位 · il cantiere 施工现场/修复工地。",
     "il panettone = pan dulce de Milán · il torrone = turrón · l'assaggio = degustación · la bancarella = puesto · il cantiere = obra de restauración."),
    ("你更喜欢传统潘妮托尼还是巧克力味的？写两句寄来。",
     "¿Prefieres el panettone tradicional o el de chocolate? Escribe dos frases y envíalas."),
    ("ESERCIZI · 第 3 版练习", "ESERCIZI · EJERCICIOS DE LA PÁGINA 3"),
    ("读第 3 版文章，选出正确答案。", "Lee el artículo de la página 3 y elige la respuesta correcta."),
    ("潘妮托尼决赛在米兰", "La final del Panettone es en Milán"),
    ("克雷莫纳牛轧糖节到 11 月 22 日", "La Festa del Torrone dura hasta el 22 de noviembre"),
    ("潘妮托尼决赛有 19 国糕点师", "En la final del Panettone hay pasteleros de 19 países"),
    ("文化论坛 11 月 3 日周二开幕", "El Forum Cultura abre el martes 3 de noviembre"),
    ("阿尔巴松露节到 12 月 6 日", "La Feria del Tartufo de Alba cierra el 6 de diciembre"),
    ("用方框里的词填空。", "Completa con las palabras del recuadro."),
    ("panettone = 米兰圣诞面包", "panettone = pan dulce de Milán"),
    ("torrone = 牛轧糖", "torrone = turrón"),
    ("assaggio = 品尝", "assaggio = degustación"),
    ("bancarella = 摊位", "bancarella = puesto"),
    ("mandorle = 杏仁（复数）", "mandorle = almendras (plural)"),
    ("tartufo = 松露", "tartufo = trufa"),
    ("用 passato prossimo（近过去时）补全，注意助动词 avere / essere。",
     "Completa con el passato prossimo. Atención al auxiliar avere / essere."),
    ("arrivare 用 essere：è arrivato", "arrivare con essere: è arrivato"),
    ("assaggiare 用 avere：abbiamo assaggiato", "assaggiare con avere: abbiamo assaggiato"),
    ("andare 用 essere，复数 sono andati", "andare con essere, plural: sono andati"),
    ("aprire 用 avere：ha aperto", "aprire con avere: ha aperto"),
    ("把词组成正确的句子。", "Forma las frases correctas con las palabras."),
    ("主语 + essere + 地点 + 日期", "Sujeto + essere + lugar + fecha"),
    ("地点在前，主语在后", "El lugar primero, el sujeto después"),
    ("dura fino a = 持续到", "dura fino a = dura hasta"),
    # P4
    ("SPORT · 体育", "SPORT · DEPORTE"),
    ("LIVELLO B1 · La Serie A e l'Europa · 意甲与欧战",
     "LIVELLO B1 · La Serie A e l'Europa · Serie A y copas europeas"),
    ("la giornata 轮次 · la presentazione 赛前介绍 · gli spalti 看台 · la sera 晚上。",
     "la giornata = jornada · la presentazione = previa · gli spalti = gradas · la sera = noche."),
    ("周日晚上你看哪场比赛？写两句意大利语寄来。",
     "¿Qué partido ves el domingo por la noche? Escribe dos frases en italiano."),
    ("LA SETTIMANA DEL CALCIO · 足球周", "LA SETTIMANA DEL CALCIO · SEMANA DE FÚTBOL"),
    ("ESERCIZI · 第 4 版练习", "ESERCIZI · EJERCICIOS DE LA PÁGINA 4"),
    ("读第 4 版文章，选出正确答案。", "Lee el artículo de la página 4 y elige la respuesta correcta."),
    ("意甲第 11 轮周日收官", "La 11.ª jornada termina el domingo 8 de noviembre"),
    ("周日晚上佛罗伦萨对尤文图斯", "El domingo por la noche, en Florencia: Fiorentina–Juventus"),
    ("欧战第 4 轮在 11 月 3–5 日", "La 4.ª jornada europea es del 3 al 5 de noviembre"),
    ("欧战比赛只作前瞻、无结果", "Los partidos europeos son solo previas, sin resultados"),
    ("国米对科莫在圣西罗", "Inter–Como se juega en San Siro"),
    ("giornata=联赛的一轮 c", "giornata=jornada de liga c"),
    ("presentazione=赛前介绍 b", "presentazione=previa b"),
    ("spalti=看台 a", "spalti=gradas a"),
    ("sera=晚上 d", "sera=noche d"),
    ("用括号里词的比较级填空（数据看赛程表）。",
     "Completa con el comparativo de la palabra entre paréntesis (datos en el calendario)."),
    ("周日晚上的比赛晚于周五的：più tardi", "El domingo por la noche, más tarde que el viernes: più tardi"),
    ("周五的比赛早于周日的：più presto", "El viernes, más pronto que el domingo: più presto"),
    ("più + bella 周日晚最美（主观评价）", "più + bella: la noche del domingo, la más bella (opinión)"),
    ("bene 的比较级是不规则的 meglio", "El comparativo de bene es irregular: meglio"),
    ("用 passato prossimo 补全。", "Completa con el passato prossimo."),
    ("vincere：ha vinto", "vincere: ha vinto"),
    ("pareggiare：ha pareggiato", "pareggiare: ha pareggiato"),
    ("arrivare 用 essere，复数 sono arrivati", "arrivare con essere, plural: sono arrivati"),
    ("guardare 用 avere：abbiamo guardato", "guardare con avere: abbiamo guardato"),
    ("prendere 的分词是 preso：ha preso", "El participio de prendere es preso: ha preso"),
])
print("content34 done")

# ================= content56 (P5 + P6) =================
pairs("content56.py", [
    ("GIOVANI · 青年", "GIOVANI · JÓVENES"),
    ("LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · 卢卡之后",
     "LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · Después de Lucca"),
    ("（周二：米兰文化论坛开幕）", "(martes: el Forum Cultura abre en Milán)"),
    ("（周三至周四：欧战直播）", "(miércoles–jueves: copas europeas en TV)"),
    ("（周五准备周末）", "(viernes: preparar el fin de semana)"),
    ("（周六：米兰或克雷莫纳品尝）", "(sábado: degustaciones en Milán o Cremona)"),
    ("（周日：意甲与返程）", "(domingo: Serie A y regreso)"),
    ("il cosplay 角色扮演服装 · gratuito 免费的 · il documentario 纪录片 · lo schermo 银幕。",
     "il cosplay = disfraz cosplay · gratuito = gratuito · il documentario = documental · lo schermo = pantalla."),
    ("卢卡之后你去哪：文化论坛、电影还是美食节？写两句寄来。",
     "Después de Lucca, ¿adónde vas: al Forum Cultura, al cine o a una sagra? Escribe dos frases."),
    ("ESERCIZI · 第 5 版练习", "ESERCIZI · EJERCICIOS DE LA PÁGINA 5"),
    ("读第 5 版文章，选出正确答案。", "Lee el artículo de la página 5 y elige la respuesta correcta."),
    ("卢卡漫画节是第 60 届", "Lucca Comics es la 60.ª edición"),
    ("文化论坛 11 月 3 日开幕", "El Forum Cultura abre el 3 de noviembre"),
    ("民俗电影节在佛罗伦萨", "El Festival dei Popoli es en Florencia"),
    ("文化论坛有 50 多场活动", "El Forum Cultura tiene más de 50 eventos"),
    ("卢卡漫画节主题是 Legacy", "El tema de Lucca Comics es «Legacy»"),
    ("用方框里的词填空。注意：有的词要变成复数。",
     "Completa con las palabras del recuadro. Atención: algunas van en plural."),
    ("armadio = 衣柜", "armadio = armario"),
    ("gratuiti = 免费的（阳性复数）", "gratuiti = gratuitos (masculino, plural)"),
    ("documentario = 纪录片", "documentario = documental"),
    ("schermo = 银幕", "schermo = pantalla"),
    ("castagne arrosto 烤栗子（复数）", "castagne arrosto = castañas asadas (plural)"),
    ("cosplay = 角色扮演服装", "cosplay = disfraz cosplay"),
    ("用将来时（futuro semplice）补全。", "Completa con el futuro (futuro semplice)."),
    ("andare 将来时 noi：andremo", "andare, futuro, noi: andremo"),
    ("esserci 将来时：ci sarà（将有）", "esserci, futuro: ci sarà (habrá)"),
    ("guardare 将来时 noi：guarderemo", "guardare, futuro, noi: guarderemo"),
    ("durare 将来时：durerà", "durare, futuro: durerà"),
    ("卢卡漫画节到 11 月 8 日才结束是错的", "Lucca Comics no termina el 8 de noviembre"),
    # P6
    ("APPROFONDIMENTO · 深读", "APPROFONDIMENTO · EN PROFUNDIDAD"),
    ("LIVELLO B2 · Leggere le previsioni · 怎样读天气预报",
     "LIVELLO B2 · Leggere le previsioni · Cómo leer una previsión"),
    ("发稿时 10 月 28 日表决结果尚未确认：本期只写预期日期、争议点和 DPB 数字，不写结果。",
     "Al cierre, el resultado de la votación del 28 de octubre aún no estaba confirmado: este número solo da la fecha prevista, el punto en disputa y las cifras del DPB, sin resultado."),
    ("la probabilità 概率 · la media 平均值 · il modello 模型/预报模式 · il bollettino 公报/预报 · aggiornare 更新。",
     "la probabilità = probabilidad · la media = media · il modello = modelo de previsión · il bollettino = boletín meteorológico · aggiornare = actualizar."),
    ("LE MINIME DI ESEMPIO · 练习用示例最低温 (DATI INVENTATI PER L'ESERCIZIO)",
     "LE MINIME DI ESEMPIO · MÍNIMAS DE EJEMPLO (DATI INVENTATI PER L'ESERCIZIO)"),
    ("PROBABILITÀ · 概率", "PROBABILITÀ · PROBABILIDAD"),
    ("ESERCIZI · 第 6 版练习", "ESERCIZI · EJERCICIOS DE LA PÁGINA 6"),
    ("看上面的练习图表，选出正确答案。", "Mira el gráfico de práctica de arriba y elige la respuesta correcta."),
    ("示例数据中最冷的是都灵 3°", "En los datos de ejemplo, Turín es la más fría: 3°"),
    ("示例数据中最暖的是那不勒斯 12°", "En los datos de ejemplo, Nápoles es la más cálida: 12°"),
    ("图表数据是练习用的、不是真实预报", "Los datos del gráfico son de práctica, no previsiones reales"),
    ("高概率不等于确定", "Una probabilidad alta no es una certeza"),
    ("预报基于 ECMWF 等模型", "Las previsiones se basan en modelos como el ECMWF"),
    ("预报会变，因为大气变化快", "Las previsiones cambian porque la atmósfera cambia rápido"),
    ("DPB 于 10 月 15 日送布鲁塞尔", "El DPB se envió a Bruselas el 15 de octubre"),
    ("2027 增长预测 +0,8%", "Crecimiento previsto para 2027: +0,8 %"),
    ("è probabile che + 虚拟式 piova", "è probabile che + subjuntivo: piova"),
    ("è possibile che + 虚拟式 nevichi", "è possibile che + subjuntivo: nevichi"),
    ("bisogna che + 虚拟式 controllino", "bisogna che + subjuntivo: controllino"),
    ("è importante che + 虚拟式 sia", "è importante che + subjuntivo: sia"),
    ("用方框里的词填空：probabilità · media · bollettino · modello",
     "Completa con las palabras del recuadro: probabilità · media · bollettino · modello"),
    ("probabilità = 概率", "probabilità = probabilidad"),
    ("media = 平均值", "media = media"),
    ("bollettino = 预报公报", "bollettino = boletín meteorológico"),
    ("modello = 预报模型", "modello = modelo de previsión"),
])
print("content56 done")

# ================= content7 (P7) =================
# NOTE: wt (the Italian definition sentence of LA PAROLA) is NOT in this
# list on purpose: it stays byte-identical. Only its Spanish gloss note
# below is localised.
pairs("content7.py", [
    ("LINGUA · 语言", "LINGUA · LENGUA"),
    ("聚焦语言 · Tre livelli, tre strumenti · 三个级别，三件工具",
     "Enfoque: lengua · Tre livelli, tre strumenti · Tres niveles, tres herramientas"),
    ("天气用无人称动词（第三人称单数）；“我冷”说 ho freddo，“外面冷”说 fa freddo。",
     "Tiempo impersonal (3.ª persona del singular): ho freddo = tengo frío; fa freddo = hace frío."),
    ("piovere 天气动词：piove", "piovere, verbo del tiempo: piove"),
    ("fa freddo = 天气冷", "fa freddo = hace frío (tiempo)"),
    ("nevicare：nevica", "nevicare: nevica"),
    ("“我冷”说 ho freddo", "«Tengo frío» se dice ho freddo"),
    ("讲过去用近过去时：arrivare/andare 等用 essere，分词配合性数；avere 的分词不变。",
     "El pasado se cuenta con el passato prossimo: con essere el participio concuerda; con avere no cambia."),
    ("arrivare 用 essere：è arrivato", "arrivare con essere: è arrivato"),
    ("assaggiare 用 avere", "assaggiare con avere"),
    ("andare 用 essere，复数 sono andati", "andare con essere, plural: sono andati"),
    ("aprire 用 avere + 不变分词", "aprire con avere + participio invariable"),
    ("è probabile che / è possibile che / bisogna che 后用虚拟式；so che、scrivono che 后用陈述式。",
     "Tras è probabile che / è possibile che / bisogna che va subjuntivo; tras so che y scrivono che va indicativo."),
    ("è probabile che + 虚拟式 piova", "è probabile che + subjuntivo: piova"),
    ("è possibile che + 虚拟式 nevichi", "è possibile che + subjuntivo: nevichi"),
    ("bisogna che + 虚拟式 sia", "bisogna che + subjuntivo: sia"),
    ("so che + 陈述式 arriva", "so che + indicativo: arriva"),
    ("fa 后面的 freddo 永远不变。", "Tras fa, freddo no cambia nunca."),
    ("nevicare 只用第三人称单数。", "Nevicare: solo 3.ª persona del singular."),
    ("预报给的是概率，不是确定性。", "Probabilidad, no certeza."),
    ("gente 是单数，动词形容词用单数阴性。", "Gente es singular femenino."),
    ("ERRORI TIPICI · 常见错误", "ERRORI TIPICI · ERRORES TÍPICOS"),
    ("assaggio = 品尝。本周见第 3 版：潘妮托尼决赛上观众可以免费品尝。",
     "assaggio = degustación. Página 3: en la final del Panettone se prueba gratis."),
    ("LA PAROLA · 本周生词", "LA PAROLA · PALABRA CLAVE"),
    ("这是编辑部示例信，非真实来信。来信请寄编辑部，VOL.3 刊登真实来信与第 8 版最佳作文！",
     "Ejemplo de la redacción, no carta real; sin mejor texto de página 8. ¡Escríbenos! Las mejores salen en VOL.3."),
    ("FRASI DELLA SETTIMANA · 本周金句（逐字摘自本期文章）",
     "FRASI DELLA SETTIMANA · FRASES DE LA SEMANA (TEXTUALES, DE ESTE NÚMERO)"),
    ("第一场真正的寒冷到来了。", "Llega el primer frío de verdad de la temporada."),
    ("这不是确定性，而是概率。", "No es una certeza, es una probabilidad."),
    ("11 月 2 日是追思日。", "El 2 de noviembre es la Conmemoración de los Difuntos."),
    ("天冷，穿暖和点！", "¡Hace frío, abrígate bien!"),
    ("观众可以免费品尝。", "El público puede probar gratis."),
    ("足球不会因为第一场寒冷而停下。", "El fútbol no se detiene por el primer frío."),
    ("文化继续。", "La cultura continúa."),
    ("高概率不等于确定性。", "Una probabilidad alta no es una certeza."),
    ("LA PROSSIMA SETTIMANA · 下期预告 (VOL.3)", "LA PROSSIMA SETTIMANA · LA PRÓXIMA SEMANA (VOL.3)"),
])
print("content7 done")

# ================= content8 (P8) =================
pairs("content8.py", [
    ("VALUTAZIONE E RISPOSTE · 练习与答案", "VALUTAZIONE E RISPOSTE · EJERCICIOS Y RESPUESTAS"),
    ("第 8 版 · La grande prova della settimana + tutte le risposte",
     "Página 8 · La grande prova della settimana + tutte le risposte"),
    ("primo freddo = 第一场寒冷", "primo freddo = el primer frío"),
    ("追思日在 11 月 2 日", "El Día de Difuntos es el 2 de noviembre"),
    ("文化论坛在米兰开幕", "El Forum Cultura abre en Milán"),
    ("潘妮托尼决赛在周六日", "La final del Panettone es sábado y domingo"),
    ("牛轧糖节在克雷莫纳", "La Festa del Torrone abre en Cremona"),
    ("意甲第 11 轮周日收官：chiude", "La 11.ª jornada termina el domingo 8 de noviembre: chiude"),
    ("佛罗伦萨对尤文图斯在周日晚上", "Fiorentina–Juventus se juega el domingo por la noche"),
    ("民俗电影节在佛罗伦萨", "El Festival dei Popoli es en Florencia"),
    ("初雪在 1300–1500 米左右", "La primera nieve, hacia los 1.300–1.500 m"),
    ("追思日的花是菊花", "La flor del 2 de noviembre es el crisantemo"),
    ("潘妮托尼决赛有 19 国糕点师", "En la final del Panettone hay pasteleros de 19 países"),
    ("文化论坛有 50 多场活动", "El Forum Cultura tiene más de 50 eventos"),
    ("阿尔巴松露节到 12 月 6 日", "La Feria del Tartufo de Alba cierra el 6 de diciembre"),
    ("DPB 于 10 月 15 日送出", "El DPB partió hacia Bruselas el 15 de octubre"),
    ("概率不等于确定", "Una probabilidad alta no es una certeza"),
    ("卢卡漫画节 11 月 1 日闭幕", "Lucca Comics se cerró el 1 de noviembre"),
    ("Giulia 去米兰潘妮托尼决赛", "Giulia va a la final del Panettone en Milán"),
    ("Paolo 周六去牛轧糖节", "Paolo va el sábado a la Festa del Torrone"),
    ("传统潘妮托尼是 Giulia 品尝的", "El panettone tradicional lo prueba Giulia"),
    ("标题概括两个城市、两个节日", "El mejor título: dos ciudades, dos dulces"),
    ("时间词在前", "La indicación de tiempo va primero"),
    ("主语 + essere + 地点 + 日期", "Sujeto + essere + lugar + fecha"),
    ("疑问词组在句首", "La interrogación va al principio"),
    ("主语 + 动词 + 时间", "Sujeto + verbo + tiempo"),
    # section E: 137/138/139 re-aim Italian -> Spanish; 140 stem re-aimed, key frozen
    ('f.ex("A2", "翻译", "周一第一场寒冷来了。", "对照原文",',
     'f.ex("A2", "翻译", "El lunes llega el primer frío.", "Compara con el original",'),
    ('f.ex("B1", "翻译", "观众可以免费品尝。", "assaggiare gratis = 免费品尝",',
     'f.ex("B1", "翻译", "El público puede probar gratis.", "assaggiare gratis = probar gratis",'),
    ('f.ex("B1", "翻译", "周日晚上，佛罗伦萨对尤文图斯。", "si gioca = 进行比赛",',
     'f.ex("B1", "翻译", "El domingo por la noche se juega Fiorentina–Juventus.", "si gioca = se juega",'),
    ('"每个预报都必须清楚。→ ___"', '"Cada previsión debe ser clara. → ___"'),
    ("dovere = 必须", "dovere = deber"),
    ("probabilità=可能性 d", "probabilità=posibilidad d"),
    ("media=平均值 a", "media=media a"),
    ("bollettino=预报公报 b", "bollettino=boletín meteorológico b"),
    ("modello=预报模型 c", "modello=modelo de previsión c"),
    ("torrone = 牛轧糖", "torrone = turrón"),
    ("mandorle 杏仁", "mandorle = almendras"),
    ("quanto costa? 多少钱", "quanto costa? = ¿cuánto cuesta?"),
    ("pagare con carta 刷卡", "pagare con carta = pagar con tarjeta"),
    ("牛轧糖节持续到 11 月 22 日", "La fiesta dura hasta el 22 de noviembre"),
    ('f.bridge(f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。")',
     'f.bridge(f"Ejercicio de escritura (sin respuesta única); el modelo ({NWORDS} palabras) está abajo.")'),
    ('"（开放题，范文如下）", f"范文见本版 H 区（{NWORDS} 词）"',
     '"（开放题，范文如下）", f"El modelo está en la sección H ({NWORDS} palabras)"'),
    ("RISPOSTE · 参考答案 — 按版面分页排列，找到题号即可",
     "RISPOSTE · RESPUESTAS — por página, busca el número del ejercicio"),
    ("每题附一句中文简析 · 带 ✓ 的为范文题",
     "Cada respuesta lleva una nota breve · ✓ marca el ejercicio de escritura"),
])
print("content8 done")
print("LOG lines:", len(LOG))
open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8").write("\n".join(LOG) + "\n")

# ================= FIX ROUND 1 (from R0 render: P1 headline spill, P2 box title, P7 parola box, P8 keys overflow) =================
# P1: bridge 4->3 lines and cifre item 4 3->2 lines, so the cifre box fits
# col 1 again (R0: box spilled to col 2, exercises overran row B).
pairs("content12.py", [
    ("Nota — il primo freddo = el primer frío · il versante adriatico = la vertiente adriática · la previsione = la previsión · assaggi = degustaciones.",
     "Nota — il primo freddo = el primer frío · versante adriatico = Adriático · previsione = previsión · assaggi = degustaciones."),
    ("(11.ª jornada de la Serie A del fin de semana)", "(11.ª jornada)"),
    # P2 box title crossed its box border by 14px (right ink 975 > border 961)
    ("LA FRASE PER RICORDARE · LA CLAVE", "FRASE PER RICORDARE · LA CLAVE"),
])
# P7 parola box: last-line descender ink exceeded the box border by 0.5px
# (1314.0 > 1313.5); +6 bottom pad moves the border clear. Letter box shifts
# down 6, col3 ends 1679, still 7px clear of the FRASI rule at 1686.
rep("content7.py",
    'wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("assaggio = degustación. Página 3: en la final del Panettone se prueba gratis.", "sans", False, 20, CW - 44)) * 29 + 20',
    'wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("assaggio = degustación. Página 3: en la final del Panettone se prueba gratis.", "sans", False, 20, CW - 44)) * 29 + 26')
# P8 keys: shorten the 8 wrapped notes to one line each (measured with wrap()
# at 13pt serif / 434px). 139 stays 2-line deliberately (key too long to fit
# with any faithful note; DE left 138/139 2-line for the same reason).
pairs("content34.py", [
    ("Sujeto + essere + lugar + fecha", "Sujeto + essere + lugar"),
    ("El lugar primero, el sujeto después", "Lugar antes, sujeto después"),
    ("El domingo por la noche, más tarde que el viernes: più tardi", "Domingo noche, más tarde que el viernes"),
    ("più + bella: la noche del domingo, la más bella (opinión)", "più + bella: la más bella (opinión)"),
])
pairs("content8.py", [
    ("Sujeto + essere + lugar + fecha", "Sujeto + essere + lugar"),
    ("La indicación de tiempo va primero", "El tiempo va primero"),
    ("La interrogación va al principio", "Interrogación primero"),
    ("assaggiare gratis = probar gratis", "assaggiare = probar"),
])
print("FIX ROUND 1 done")
open(os.path.join(BASE, "transform-log.txt"), "a", encoding="utf-8").write("\n".join(LOG) + "\n")

# ================= FIX ROUND 2 (from R1 audit: 1 NEW LINEX on P1) =================
# P1 parola grey note wrapped to 2 lines and its second line ("otoño suave.")
# was struck by the row-B rule at y=1864. Shortened to one measured line
# (326.7px at 19pt sans, box width 434); the full "dopo un autunno mite"
# definition stands directly above it in Italian.
rep("content12.py",
    "«il primo freddo»: el primer frío serio tras un otoño suave.",
    "«il primo freddo»: el primer frío serio.")
print("FIX ROUND 2 done")
open(os.path.join(BASE, "transform-log.txt"), "a", encoding="utf-8").write("\n".join(LOG) + "\n")
