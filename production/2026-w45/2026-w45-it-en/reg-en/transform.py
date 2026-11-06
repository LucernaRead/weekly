# -*- coding: utf-8 -*-
"""W45 IT core -> IT x EN fan-out transform for the BUILD COPY ONLY.

Literal replacements only (tools README #17): each rep() fails loudly if
its old string is absent, so a typo can never silently skip a translation.
Italian target-language text is never a replacement target; only the
explanation layer (Chinese notes/bridges/titles/furniture) and the P8
E-section re-aiming change. Registry exercise-type names stay in Chinese
(never printed anywhere, W43 IT x EN precedent) so the registry stays
byte-comparable with the core; the P8 writing type check therefore also
stays. Furniture follows the shipped W43 IT x EN SVGs (badge y=574,
22pt BRICK; footer; gloss prefix "NOTE · "; P8 separators stay Italian
"— PAGINA n —"), which outrank the generic rules in tools README #20.
"""
import pathlib, sys

B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-it-en-build')
C12, C34, C56, C7, C8, BS, SV = 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py', 'bslib4.py', 'svglib.py'
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
    return total

# ---------- repoint OUT + render names (copy only; core untouched) ----------
rep(ALL, 'weekly-report-w45-it-core', 'weekly-report-w45-it-en', 5)
rep(['render.py'], 'weekly-report-w45-it-core', 'weekly-report-w45-it-en', 1)
rep(['render.py'], 'La-Lucerna-VOL2-web.pdf', 'La-Lucerna-VOL2-EN-web.pdf', 1)
rep(['render.py'], 'La-Lucerna-VOL2.pdf', 'La-Lucerna-VOL2-EN.pdf', 1)
rep(['render.py'], 'Render the IT weekly', 'Render the IT x EN edition', 1)

# ---------- bslib4 furniture (W43 IT x EN shipped strings, VOL.2) ----------
rep([BS], '"La Lucerna · 意大利语周报 VOL.2 · LUCERNA ITALIAN WEEKLY"',
    '"La Lucerna · ITALIAN WEEKLY VOL.2 · TEXT IN ITALIAN · EXPLANATIONS IN ENGLISH"', 1)
rep([BS], 'f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} of {total}"', 1)
rep([BS], '"译注｜" + s', '"NOTE · " + s', 1)
# svglib: one CJK docstring in an unused illustration helper; prints nothing.
rep([SV], 'for 重阳.', 'for Double Ninth Festival.', 1)

# ---------- P1 masthead + pairing badge (W43 geometry: y=574, 22pt BRICK) ----------
rep([C12], '"OGNI SETTIMANA IN ITALIANO · 每周一期 · 读意大利人正在读的意大利语"',
    '"OGNI SETTIMANA IN ITALIANO · THE ITALIAN ITALIANS ARE READING"', 1)
rep([C12], '"意 大 利 语 周 报 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A"',
    '"THE ITALIAN WEEKLY · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A"', 1)
rep([C12], 'p.text(RIGHT - 30, 522, "初寒之周 · 详见第 2 版", 21, "sans", False, "#b3a06a", anchor="end")',
    'p.text(RIGHT - 30, 522, "The first-cold week · See page 2", 21, "sans", False, "#b3a06a", anchor="end")\np.text(975, 574, "Text in Italian · Explanations in English — the edition for English-speaking readers", 22, "sans", True, BRICK, anchor="middle")', 1)
rep([C12], '"本周迎来第一场寒冷"', '"THE FIRST COLD ARRIVES THIS WEEK"', 1)
rep([C12], '"LA NOTIZIA · 头条"', '"LA NOTIZIA · THE TOP STORY"', 1)
rep([C12], '"讲解｜il primo freddo 第一场寒冷 · il versante adriatico 亚得里亚海一侧 · la previsione 预报 · assaggi 品尝。"',
    '"Notes: il primo freddo, the first cold · il versante adriatico, the Adriatic side · la previsione, forecast · assaggi, tastings."', 1)
rep([C12], '"LA SETTIMANA IN CIFRE · 数字看本周"', '"LA SETTIMANA IN CIFRE · Numbers"', 1)
rep([C12], '（可能下初雪的海拔）', '(altitude of the first light snow)', 1)
rep([C12], '（米兰文化论坛 50 多场活动）', '(50+ Forum Cultura events in Milan, 3-8 November)', 1)
rep([C12], '（参加米兰潘妮托尼决赛的国家数）', '(countries at the Panettone final in Milan)', 1)
rep([C12], '（本周末意甲第 11 轮）', '(Serie A matchday this weekend)', 1)
rep([C12], '"ADESSO TU · 即学即练"', '"ADESSO TU · Now you try"', 1)
rep([C12], '"本周日程 · Cosa succede, giorno per giorno"', '"This week\'s diary · Cosa succede, giorno per giorno"', 1)
rep([C12], '"日程以各活动日历为准，时间可能有变。"', '"Dates per event calendars; times may change."', 1)
rep([C12], '"IN QUESTO NUMERO · 本期目录"', '"IN QUESTO NUMERO · CONTENTS"', 1)
rep([C12], '"“第一场寒冷”：温和秋天后的第一波寒冷。"', '"‘Il primo freddo’: the first serious cold after a mild autumn."', 1)
rep([C12], '"IN BREVE · 快讯"', '"IN BREVE · In brief"', 1)
rep([C12], '"QUIZ LAMPO · 闪电问答"', '"QUIZ LAMPO · Lightning quiz"', 1)
rep([C12], '"读头版，选出正确答案 · 答案见第 8 版"', '"Read page 1, choose the right answer · Answers on page 8"', 1)

# ---------- band titles / subs ----------
rep([C12], '"VITA · 生活"', '"VITA · DAILY LIFE"', 1)
rep([C12], '"LIVELLO A2 · Il primo freddo e il 2 novembre · 初寒与追思日"',
    '"LIVELLO A2 · Il primo freddo e il 2 novembre · First cold and 2 November"', 1)
rep([C34], '"CULTURA · 文化"', '"CULTURA · Culture"', 1)
rep([C34], '"A2 → B1 · Panettone, torrone e musei aperti · 甜点与博物馆"',
    '"A2 → B1 · Panettone, torrone e musei aperti · Sweets and open museums"', 1)
rep([C34], '"SPORT · 体育"', '"SPORT · Sport"', 1)
rep([C34], '"LIVELLO B1 · La Serie A e l\'Europa · 意甲与欧战"',
    '"LIVELLO B1 · La Serie A e l\'Europa · Serie A and Europe"', 1)
rep([C56], '"GIOVANI · 青年"', '"GIOVANI · Youth"', 1)
rep([C56], '"LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · 卢卡之后"',
    '"LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · After Lucca"', 1)
rep([C56], '"APPROFONDIMENTO · 深读"', '"APPROFONDIMENTO · In depth"', 1)
rep([C56], '"LIVELLO B2 · Leggere le previsioni · 怎样读天气预报"',
    '"LIVELLO B2 · Leggere le previsioni · How to read a forecast"', 1)
rep([C7], '"LINGUA · 语言"', '"LINGUA · Language"', 1)
rep([C7], '"聚焦语言 · Tre livelli, tre strumenti · 三个级别，三件工具"',
    '"Language focus · Tre livelli, tre strumenti · Three levels, three tools"', 1)
rep([C8], '"VALUTAZIONE E RISPOSTE · 练习与答案"', '"VALUTAZIONE E RISPOSTE · Test and answers"', 1)
rep([C8], '"第 8 版 · La grande prova della settimana + tutte le risposte"',
    '"Page 8 · La grande prova della settimana + tutte le risposte"', 1)

# ---------- section heads / shared apparatus ----------
rep(ALL, '"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
    '"Answers on page 8 · Levels are mixed — find answers by number"', 5)
rep(ALL, '"E TU? · 说说你自己"', '"E TU? · Over to you"')
rep([C12], '"ESERCIZI · 第 2 版练习"', '"ESERCIZI · Page 2 exercises"', 1)
rep([C34], '"ESERCIZI · 第 3 版练习"', '"ESERCIZI · Page 3 exercises"', 1)
rep([C34], '"ESERCIZI · 第 4 版练习"', '"ESERCIZI · Page 4 exercises"', 1)
rep([C56], '"ESERCIZI · 第 5 版练习"', '"ESERCIZI · Page 5 exercises"', 1)
rep([C56], '"ESERCIZI · 第 6 版练习"', '"ESERCIZI · Page 6 exercises"', 1)
rep([C12], '"IL 2 NOVEMBRE · 追思日"', '"IL 2 NOVEMBRE · All Souls\' Day"', 1)
rep([C34], '"LA SETTIMANA DEL CALCIO · 足球周"', '"LA SETTIMANA DEL CALCIO · Football week"', 1)
rep([C56], '"LE MINIME DI ESEMPIO · 练习用示例最低温 (DATI INVENTATI PER L\'ESERCIZIO)"',
    '"LE MINIME DI ESEMPIO · Practice minima (DATI INVENTATI PER L\'ESERCIZIO)"', 1)
rep([C56], '"PROBABILITÀ · 概率"', '"PROBABILITÀ · Probability"', 1)

# ---------- bridges (printed grey sans) ----------
rep([C12], '"发稿时表决结果尚未确认，详见第 6 版。"',
    '"At press time the vote result was not yet confirmed — see page 6."', 1)
rep([C12], '"用意大利语补全句子。"', '"Complete the sentences in Italian."', 1)
rep([C12], '"补全动词的现在时形式。"', '"Complete with the present tense."', 1)
rep([C12], '"读第 2 版文章，选出正确答案。"', '"Read the page 2 article and choose the right answer."', 1)
rep([C34], '"读第 3 版文章，选出正确答案。"', '"Read the page 3 article and choose the right answer."', 1)
rep([C34], '"用方框里的词填空。"', '"Fill in with the words in the box."', 1)
rep([C34], '"用 passato prossimo（近过去时）补全，注意助动词 avere / essere。"',
    '"Complete with the passato prossimo — watch the auxiliaries avere / essere."', 1)
rep([C34], '"把词组成正确的句子。"', '"Put the words in the right order."', 1)
rep([C34], '"读第 4 版文章，选出正确答案。"', '"Read the page 4 article and choose the right answer."', 1)
rep([C34], '"用括号里词的比较级填空（数据看赛程表）。"',
    '"Fill in with the comparative of the word in brackets (see the fixture table)."', 1)
rep([C34], '"用 passato prossimo 补全。"', '"Complete with the passato prossimo."', 1)
rep([C56], '"读第 5 版文章，选出正确答案。"', '"Read the page 5 article and choose the right answer."', 1)
rep([C56], '"用方框里的词填空。注意：有的词要变成复数。"',
    '"Fill in with the words in the box. Note: some words need the plural."', 1)
rep([C56], '"用将来时（futuro semplice）补全。"', '"Complete with the futuro semplice."', 1)
rep([C56], '"发稿时 10 月 28 日表决结果尚未确认：本期只写预期日期、争议点和 DPB 数字，不写结果。"',
    '"At press time the 28 October vote result was not yet confirmed: this issue gives only the expected date, the disputed point and the DPB figures, no result."', 1)
rep([C56], '"看上面的练习图表，选出正确答案。"',
    '"Look at the practice chart above and choose the right answer."', 1)
rep([C56], '"用方框里的词填空：probabilità · media · bollettino · modello"',
    '"Fill in with the words in the box: probabilità · media · bollettino · modello"', 1)
rep([C7], '"天气用无人称动词（第三人称单数）；“我冷”说 ho freddo，“外面冷”说 fa freddo。"',
    '"Weather uses impersonal verbs (third person singular): ‘I am cold’ is ho freddo, ‘it is cold outside’ is fa freddo."', 1)
rep([C7], '"讲过去用近过去时：arrivare/andare 等用 essere，分词配合性数；avere 的分词不变。"',
    '"For the past use the passato prossimo: arrivare/andare take essere and the participle agrees; with avere it never changes."', 1)
rep([C7], '"è probabile che / è possibile che / bisogna che 后用虚拟式；so che、scrivono che 后用陈述式。"',
    '"After è probabile che / è possibile che / bisogna che use the subjunctive; after so che / scrivono che use the indicative."', 1)

# ---------- gloss() argument strings (counts must stay 1:1 with the core) ----------
rep([C12], '"il cappotto 大衣 · la sciarpa 围巾 · i guanti 手套 · a strati 分层穿衣 · il termosifone 暖气片 · il crisantemo 菊花"',
    '"il cappotto overcoat · la sciarpa scarf · i guanti gloves · a strati in layers · il termosifone radiator · il crisantemo chrysanthemum"', 1)
rep([C34], '"il panettone 米兰圣诞面包 · il torrone 牛轧糖 · l\'assaggio 品尝 · la bancarella 摊位 · il cantiere 施工现场/修复工地。"',
    '"il panettone Milan\'s Christmas cake · il torrone nougat · l\'assaggio tasting · la bancarella stall · il cantiere building site"', 1)
rep([C34], '"la giornata 轮次 · la presentazione 赛前介绍 · gli spalti 看台 · la sera 晚上。"',
    '"la giornata matchday · la presentazione preview · gli spalti stands · la sera evening"', 1)
rep([C56], '"il cosplay 角色扮演服装 · gratuito 免费的 · il documentario 纪录片 · lo schermo 银幕。"',
    '"il cosplay cosplay costume · gratuito free · il documentario documentary · lo schermo screen"', 1)
rep([C56], '"la probabilità 概率 · la media 平均值 · il modello 模型/预报模式 · il bollettino 公报/预报 · aggiornare 更新。"',
    '"la probabilità probability · la media average · il modello forecast model · il bollettino bulletin · aggiornare to update"', 1)

# ---------- P1/P2/P3/P4/P5 box parentheticals + E TU notes ----------
rep([C56], '（周二：米兰文化论坛开幕）', '(Tuesday: Forum Cultura opens in Milan)', 1)
rep([C56], '（周三至周四：欧战直播）', '(Wednesday-Thursday: European cups on TV)', 1)
rep([C56], '（周五准备周末）', '(Friday: getting the weekend ready)', 1)
rep([C56], '（周六：米兰或克雷莫纳品尝）', '(Saturday: tastings in Milan or Cremona)', 1)
rep([C56], '（周日：意甲与返程）', '(Sunday: Serie A and the way home)', 1)
rep([C12], '"初寒来了你穿什么：大衣、围巾还是手套？写两句意大利语寄给编辑部。"',
    '"When the first cold arrives, what do you wear: coat, scarf or gloves? Write two sentences in Italian and send them to us."', 2)
rep([C34], '"你更喜欢传统潘妮托尼还是巧克力味的？写两句寄来。"',
    '"Do you prefer traditional panettone or chocolate panettone? Write two sentences and send them to us."', 2)
rep([C34], '"周日晚上你看哪场比赛？写两句意大利语寄来。"',
    '"Which match will you watch on Sunday evening? Write two sentences in Italian and send them to us."', 2)
rep([C56], '"卢卡之后你去哪：文化论坛、电影还是美食节？写两句寄来。"',
    '"After Lucca, where are you going: the Forum Cultura, the cinema or a food festival? Write two sentences and send them to us."', 2)

# ---------- P2 FRASE box: title size 19 (W43 IT x EN precedent; 23pt overflows) ----------
rep([C12], 'f.box("LA FRASE PER RICORDARE · 口诀", [\n    ("«Fa freddo, copriti bene!» Così dicono le nonne italiane: quando arriva il primo freddo, il consiglio è uno solo — vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),\n])',
    'f.box("LA FRASE PER RICORDARE · Remember", [\n    ("«Fa freddo, copriti bene!» Così dicono le nonne italiane: quando arriva il primo freddo, il consiglio è uno solo — vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),\n], tsize=19)', 1)

# ---------- P7: errori notes (compressed to hold the core's col3 geometry) ----------
# Core col3 ends y=1673, 13px clear of the FRASI rule at 1686. Each errori
# note is kept to ONE wrapped line at 19.5pt, so eh stays 813.5 exactly.
rep([C7], '"fa 后面的 freddo 永远不变。"', '"After fa, freddo never changes."', 1)
rep([C7], '"nevicare 只用第三人称单数。"', '"Nevicare takes third person singular only."', 1)
rep([C7], '"预报给的是概率，不是确定性。"', '"Probabilities, not certainties."', 1)
rep([C7], '"gente 是单数，动词形容词用单数阴性。"', '"Gente is singular feminine."', 1)
rep([C7], '"ERRORI TIPICI · 常见错误"', '"ERRORI TIPICI · Common mistakes"', 1)
# P7 parola: Italian definition sentence is FROZEN verbatim; only the gloss
# line below it is localised into English.
rep([C7], '"LA PAROLA · 本周生词"', '"LA PAROLA · Word of the week"', 1)
rep([C7], '"assaggio = 品尝。本周见第 3 版：潘妮托尼决赛上观众可以免费品尝。"',
    '"assaggio = tasting. See page 3: free tasting at the Panettone final."', 2)
# P7 letters: Italian letter text frozen verbatim, including its
# "(esempio della redazione)" label. The English note states all three
# disclosure facts (no real letters yet, no best page-8 essay yet, the
# sample stands in and both are promised for VOL.3) plus an explicit
# imperative invitation with a VOL.3 publication promise. This mirrors
# the W45 ES x EN precedent (frozen target-language disclosure + English
# note); adding a further Italian disclosure sentence would push col3
# past the FRASI rule, so none is added.
rep([C7], '"这是编辑部示例信，非真实来信。来信请寄编辑部，VOL.3 刊登真实来信与第 8 版最佳作文！"',
    '"Editor\'s sample, not a real letter: no real letters yet, no best page-8 essay yet — both promised for VOL.3. Write to us!"', 2)
rep([C7], '"FRASI DELLA SETTIMANA · 本周金句（逐字摘自本期文章）"',
    '"FRASI DELLA SETTIMANA · PHRASES OF THE WEEK (verbatim from this issue)"', 1)
rep([C7], '"第一场真正的寒冷到来了。"', '"The first real cold of the season arrives."', 1)
rep([C7], '"这不是确定性，而是概率。"', '"It is not a certainty, it is a probability."', 1)
rep([C7], '"11 月 2 日是追思日。"', '"2 November is the Commemoration of the Dead."', 1)
rep([C7], '"天冷，穿暖和点！"', '"It\'s cold, wrap up well!"', 1)
rep([C7], '"观众可以免费品尝。"', '"The public can taste for free."', 1)
rep([C7], '"足球不会因为第一场寒冷而停下。"', '"Football does not stop for the first cold."', 1)
rep([C7], '"文化继续。"', '"Culture goes on."', 1)
rep([C7], '"高概率不等于确定性。"', '"A high probability is not a certainty."', 1)
rep([C7], '"LA PROSSIMA SETTIMANA · 下期预告 (VOL.3)"', '"LA PROSSIMA SETTIMANA · NEXT WEEK (VOL.3)"', 1)

# ---------- printed instructions (instr= values sit beside exercise numbers) ----------
rep(ALL, 'instr="填空"', 'instr="Fill in"')
rep(ALL, 'instr="造句"', 'instr="Reorder"')
rep(ALL, 'instr="判断"', 'instr="True or false"')
rep(ALL, 'instr="把词和释义配对"', 'instr="Match words to definitions"')
rep(ALL, 'instr="写作"', 'instr="Write"')
# P8 E-section instructions, per item direction (W43 IT x EN ruling)
rep([C8], 'f.ex("A2", "翻译", "周一第一场寒冷来了。", "对照原文",\n     "Lunedì arriva il primo freddo. → ___", instr="翻译"',
    'f.ex("A2", "翻译", "On Monday the first cold arrives.", "Compare with the original.",\n     "Lunedì arriva il primo freddo. → ___", instr="Translate into English"', 1)
rep([C8], 'f.ex("B1", "翻译", "观众可以免费品尝。", "assaggiare gratis = 免费品尝",\n     "Il pubblico può assaggiare gratis. → ___", instr="翻译"',
    'f.ex("B1", "翻译", "The public can taste for free.", "assaggiare gratis = to taste for free",\n     "Il pubblico può assaggiare gratis. → ___", instr="Translate into English"', 1)
rep([C8], 'f.ex("B1", "翻译", "周日晚上，佛罗伦萨对尤文图斯。", "si gioca = 进行比赛",\n     "Domenica sera si gioca Fiorentina–Juventus. → ___", instr="翻译"',
    'f.ex("B1", "翻译", "On Sunday evening, Fiorentina play Juventus.", "si gioca = is played",\n     "Domenica sera si gioca Fiorentina–Juventus. → ___", instr="Translate into English"', 1)
rep([C8], 'f.ex("B2", "翻译", "Ogni previsione deve essere chiara.", "dovere = 必须",\n     "每个预报都必须清楚。→ ___", instr="翻译"',
    'f.ex("B2", "翻译", "Ogni previsione deve essere chiara.", "dovere = must",\n     "Every forecast must be clear. → ___", instr="Translate into Italian"', 1)

# ---------- exercise notes, pages 1-2 (printed on P8) ----------
rep([C12], '"il primo freddo = 第一场寒冷"', '"il primo freddo = the first cold"', 1)
rep([C12], '"la prima neve leggera = 初雪"', '"la prima neve leggera = the first light snow"', 1)
rep([C12], '"文化论坛与潘妮托尼决赛都在米兰"', '"Both the Forum Cultura and the Panettone final are in Milan"', 1)
rep([C12], '"克雷莫纳的节日叫 Festa del Torrone"', '"The Cremona festival is the Festa del Torrone"', 1)
rep([C12], '"previsioni = 预报（复数）"', '"previsioni = forecasts (plural)"', 1)
rep([C12], '"第一场寒冷在周一 11 月 2 日到来"', '"The first cold arrives on Monday 2 November"', 1)
rep([C12], '"初雪在 1300–1500 米左右"', '"The first snow falls around 1,300-1,500 metres"', 1)
rep([C12], '"潘妮托尼决赛在米兰"', '"The Panettone final is in Milan"', 1)
rep([C12], '"意甲第 11 轮周日收官"', '"Serie A matchday 11 ends on Sunday"', 2)
rep([C12], '"cappotto = 大衣"', '"cappotto = overcoat"', 1)
rep([C12], '"sciarpa = 围巾"', '"sciarpa = scarf"', 1)
rep([C12], '"guanti = 手套（复数）"', '"guanti = gloves (plural)"', 1)
rep([C12], '"crisantemi = 菊花（复数）"', '"crisantemi = chrysanthemums (plural)"', 1)
rep([C12], '"termosifoni = 暖气片（复数）"', '"termosifoni = radiators (plural)"', 1)
rep([C12], '"fare freddo：fa freddo（天气）"', '"fare freddo: fa freddo (weather)"', 1)
rep([C12], '"mettere：io → metto"', '"mettere: io gives metto"', 1)
rep([C12], '"portare：loro → portano"', '"portare: loro gives portano"', 1)
rep([C12], '"guardare：loro → guardano"', '"guardare: loro gives guardano"', 1)
rep([C12], '"restare：la scuola → resta（lei）"', '"restare: la scuola gives resta (lei)"', 1)
rep([C12], '"11 月 2 日是追思日"', '"2 November is All Souls\' Day"', 1)
rep([C12], '"追思日的花是菊花"', '"The flower of All Souls\' Day is the chrysanthemum"', 1)
rep([C12], '"分层穿衣：a strati"', '"Dressing in layers: a strati"', 1)
rep([C12], '"诸圣节今年是周日、无连休"', '"All Saints\' Day falls on Sunday this year, so no long weekend"', 1)
rep([C12], '"cappotto=御寒大衣 c"', '"cappotto = warm winter coat, c"', 1)
rep([C12], '"sciarpa=围巾 d"', '"sciarpa = scarf, d"', 1)
rep([C12], '"crisantemo=十一月的花 a"', '"crisantemo = November flower, a"', 1)
rep([C12], '"termosifone=暖气片 b"', '"termosifone = radiator, b"', 1)

# ---------- exercise notes, pages 3-4 ----------
rep([C34], '"潘妮托尼决赛在米兰"', '"The Panettone final is in Milan"', 1)
rep([C34], '"克雷莫纳牛轧糖节到 11 月 22 日"', '"The Cremona torrone festival runs to 22 November"', 1)
rep([C34], '"潘妮托尼决赛有 19 国糕点师"', '"19 countries send pastry chefs to the Panettone final"', 1)
rep([C34], '"文化论坛 11 月 3 日周二开幕"', '"The Forum Cultura opens on Tuesday 3 November"', 1)
rep([C34], '"阿尔巴松露节到 12 月 6 日"', '"The Alba truffle fair runs to 6 December"', 1)
rep([C34], '"panettone = 米兰圣诞面包"', '"panettone = Milan\'s Christmas cake"', 1)
rep([C34], '"torrone = 牛轧糖"', '"torrone = nougat"', 1)
rep([C34], '"assaggio = 品尝"', '"assaggio = tasting"', 1)
rep([C34], '"bancarella = 摊位"', '"bancarella = stall"', 1)
rep([C34], '"mandorle = 杏仁（复数）"', '"mandorle = almonds (plural)"', 1)
rep([C34], '"tartufo = 松露"', '"tartufo = truffle"', 1)
rep([C34], '"arrivare 用 essere：è arrivato"', '"arrivare takes essere: è arrivato"', 1)
rep([C34], '"assaggiare 用 avere：abbiamo assaggiato"', '"assaggiare takes avere: abbiamo assaggiato"', 1)
rep([C34], '"andare 用 essere，复数 sono andati"', '"andare takes essere, plural sono andati"', 1)
rep([C34], '"aprire 用 avere：ha aperto"', '"aprire takes avere: ha aperto"', 1)
rep([C34], '"主语 + essere + 地点 + 日期"', '"Subject + essere + place + date"', 1)
rep([C34], '"地点在前，主语在后"', '"Place first, subject after"', 1)
rep([C34], '"dura fino a = 持续到"', '"dura fino a = lasts until"', 1)
rep([C34], '"意甲第 11 轮周日收官"', '"Serie A matchday 11 ends on Sunday"', 1)
rep([C34], '"周日晚上佛罗伦萨对尤文图斯"', '"Fiorentina play Juventus on Sunday evening"', 1)
rep([C34], '"欧战第 4 轮在 11 月 3–5 日"', '"European matchday 4 runs 3-5 November"', 1)
rep([C34], '"欧战比赛只作前瞻、无结果"', '"European matches are previews here, with no results"', 1)
rep([C34], '"国米对科莫在圣西罗"', '"Inter play Como at San Siro"', 1)
rep([C34], '"giornata=联赛的一轮 c"', '"giornata = one matchday, c"', 1)
rep([C34], '"presentazione=赛前介绍 b"', '"presentazione = preview, b"', 1)
rep([C34], '"spalti=看台 a"', '"spalti = stands, a"', 1)
rep([C34], '"sera=晚上 d"', '"sera = evening, d"', 1)
rep([C34], '"周日晚上的比赛晚于周五的：più tardi"', '"Sunday evening matches are later than Friday\'s: più tardi"', 1)
rep([C34], '"周五的比赛早于周日的：più presto"', '"Friday matches are earlier than Sunday\'s: più presto"', 1)
rep([C34], '"più + bella 周日晚最美（主观评价）"', '"più + bella: Sunday evening is the finest (a judgement)"', 1)
rep([C34], '"bene 的比较级是不规则的 meglio"', '"The comparative of bene is the irregular meglio"', 1)
rep([C34], '"vincere：ha vinto"', '"vincere: ha vinto"', 1)
rep([C34], '"pareggiare：ha pareggiato"', '"pareggiare: ha pareggiato"', 1)
rep([C34], '"arrivare 用 essere，复数 sono arrivati"', '"arrivare takes essere, plural sono arrivati"', 1)
rep([C34], '"guardare 用 avere：abbiamo guardato"', '"guardare takes avere: abbiamo guardato"', 1)
rep([C34], '"prendere 的分词是 preso：ha preso"', '"The participle of prendere is preso: ha preso"', 1)

# ---------- exercise notes, pages 5-6 ----------
rep([C56], '"卢卡漫画节是第 60 届"', '"Lucca Comics is in its 60th edition"', 1)
rep([C56], '"文化论坛 11 月 3 日开幕"', '"The Forum Cultura opens on 3 November"', 1)
rep([C56], '"民俗电影节在佛罗伦萨"', '"The Festival dei Popoli is in Florence"', 2)
rep([C56], '"文化论坛有 50 多场活动"', '"The Forum Cultura has 50+ events"', 2)
rep([C56], '"卢卡漫画节主题是 Legacy"', '"The Lucca Comics theme is Legacy"', 1)
rep([C56], '"armadio = 衣柜"', '"armadio = wardrobe"', 1)
rep([C56], '"gratuiti = 免费的（阳性复数）"', '"gratuiti = free (masculine plural)"', 1)
rep([C56], '"documentario = 纪录片"', '"documentario = documentary"', 1)
rep([C56], '"schermo = 银幕"', '"schermo = screen"', 1)
rep([C56], '"castagne arrosto 烤栗子（复数）"', '"castagne arrosto = roast chestnuts (plural)"', 1)
rep([C56], '"cosplay = 角色扮演服装"', '"cosplay = cosplay costume"', 1)
rep([C56], '"andare 将来时 noi：andremo"', '"andare, future noi: andremo"', 1)
rep([C56], '"esserci 将来时：ci sarà（将有）"', '"esserci, future: ci sarà (there will be)"', 1)
rep([C56], '"guardare 将来时 noi：guarderemo"', '"guardare, future noi: guarderemo"', 1)
rep([C56], '"durare 将来时：durerà"', '"durare, future: durerà"', 1)
rep([C56], '"卢卡漫画节到 11 月 8 日才结束是错的"', '"Lucca Comics ending on 8 November is false"', 1)
rep([C56], '"示例数据中最冷的是都灵 3°"', '"The coldest practice-data city is Turin at 3°"', 1)
rep([C56], '"示例数据中最暖的是那不勒斯 12°"', '"The warmest practice-data city is Naples at 12°"', 1)
rep([C56], '"12 − 9 = 3"', '"12 minus 9 = 3"', 1)
rep([C56], '"4 + 5 = 9"', '"4 plus 5 = 9"', 1)
rep([C56], '"图表数据是练习用的、不是真实预报"', '"The chart figures are practice data, not real forecasts"', 1)
rep([C56], '"高概率不等于确定"', '"A high probability is not a certainty"', 1)
rep([C56], '"预报基于 ECMWF 等模型"', '"Forecasts rest on models like the ECMWF"', 1)
rep([C56], '"预报会变，因为大气变化快"', '"Forecasts change because the atmosphere changes fast"', 1)
rep([C56], '"DPB 于 10 月 15 日送布鲁塞尔"', '"The DPB went to Brussels on 15 October"', 1)
rep([C56], '"2027 增长预测 +0,8%"', '"Growth forecast for 2027: +0.8%"', 1)
rep([C56], '"è probabile che + 虚拟式 piova"', '"è probabile che + subjunctive piova"', 1)
rep([C56], '"è possibile che + 虚拟式 nevichi"', '"è possibile che + subjunctive nevichi"', 1)
rep([C56], '"bisogna che + 虚拟式 controllino"', '"bisogna che + subjunctive controllino"', 1)
rep([C56], '"è importante che + 虚拟式 sia"', '"è importante che + subjunctive sia"', 1)
rep([C56], '"probabilità = 概率"', '"probabilità = probability"', 1)
rep([C56], '"media = 平均值"', '"media = average"', 1)
rep([C56], '"bollettino = 预报公报"', '"bollettino = forecast bulletin"', 1)
rep([C56], '"modello = 预报模型"', '"modello = forecast model"', 1)

# ---------- exercise notes, page 7 ----------
rep([C7], '"piovere 天气动词：piove"', '"piovere, weather verb: piove"', 1)
rep([C7], '"fa freddo = 天气冷"', '"fa freddo = the weather is cold"', 1)
rep([C7], '"nevicare：nevica"', '"nevicare: nevica"', 1)
rep([C7], '"“我冷”说 ho freddo"', '"‘I am cold’ is ho freddo"', 1)
rep([C7], '"arrivare 用 essere：è arrivato"', '"arrivare takes essere: è arrivato"', 1)
rep([C7], '"assaggiare 用 avere"', '"assaggiare takes avere"', 1)
rep([C7], '"andare 用 essere，复数 sono andati"', '"andare takes essere, plural sono andati"', 1)
rep([C7], '"aprire 用 avere + 不变分词"', '"aprire takes avere + invariable participle"', 1)
rep([C7], '"è probabile che + 虚拟式 piova"', '"è probabile che + subjunctive piova"', 1)
rep([C7], '"è possibile che + 虚拟式 nevichi"', '"è possibile che + subjunctive nevichi"', 1)
rep([C7], '"bisogna che + 虚拟式 sia"', '"bisogna che + subjunctive sia"', 1)
rep([C7], '"so che + 陈述式 arriva"', '"so che + indicative arriva"', 1)

# ---------- exercise notes, page 8 ----------
rep([C8], '"primo freddo = 第一场寒冷"', '"primo freddo = the first cold"', 1)
rep([C8], '"追思日在 11 月 2 日"', '"All Souls\' Day is on 2 November"', 1)
rep([C8], '"文化论坛在米兰开幕"', '"The Forum Cultura opens in Milan"', 1)
rep([C8], '"潘妮托尼决赛在周六日"', '"The Panettone final is on Saturday and Sunday"', 1)
rep([C8], '"牛轧糖节在克雷莫纳"', '"The torrone festival is in Cremona"', 1)
rep([C8], '"意甲第 11 轮周日收官：chiude"', '"Serie A matchday 11 ends on Sunday: chiude"', 1)
rep([C8], '"佛罗伦萨对尤文图斯在周日晚上"', '"Fiorentina play Juventus on Sunday evening"', 1)
rep([C8], '"民俗电影节在佛罗伦萨"', '"The Festival dei Popoli is in Florence"', 1)
rep([C8], '"初雪在 1300–1500 米左右"', '"The first snow falls around 1,300-1,500 metres"', 1)
rep([C8], '"追思日的花是菊花"', '"The flower of All Souls\' Day is the chrysanthemum"', 1)
rep([C8], '"潘妮托尼决赛有 19 国糕点师"', '"19 countries send pastry chefs to the Panettone final"', 1)
rep([C8], '"文化论坛有 50 多场活动"', '"The Forum Cultura has 50+ events"', 1)
rep([C8], '"阿尔巴松露节到 12 月 6 日"', '"The Alba truffle fair runs to 6 December"', 1)
rep([C8], '"DPB 于 10 月 15 日送出"', '"The DPB went out on 15 October"', 1)
rep([C8], '"概率不等于确定"', '"A probability is not a certainty"', 1)
rep([C8], '"卢卡漫画节 11 月 1 日闭幕"', '"Lucca Comics closed on 1 November"', 1)
rep([C8], '"Giulia 去米兰潘妮托尼决赛"', '"Giulia goes to the Panettone final in Milan"', 1)
rep([C8], '"Paolo 周六去牛轧糖节"', '"Paolo goes to the torrone festival on Saturday"', 1)
rep([C8], '"传统潘妮托尼是 Giulia 品尝的"', '"The traditional panettone is tasted by Giulia"', 1)
rep([C8], '"标题概括两个城市、两个节日"', '"The title sums up two cities, two sweets"', 1)
rep([C8], '"时间词在前"', '"Time word first"', 1)
rep([C8], '"主语 + essere + 地点 + 日期"', '"Subject + essere + place + date"', 1)
rep([C8], '"疑问词组在句首"', '"Question phrase first"', 1)
rep([C8], '"主语 + 动词 + 时间"', '"Subject + verb + time"', 1)
rep([C8], '"probabilità=可能性 d"', '"probabilità = possibility, d"', 1)
rep([C8], '"media=平均值 a"', '"media = average, a"', 1)
rep([C8], '"bollettino=预报公报 b"', '"bollettino = forecast bulletin, b"', 1)
rep([C8], '"modello=预报模型 c"', '"modello = forecast model, c"', 1)
rep([C8], '"torrone = 牛轧糖"', '"torrone = nougat"', 1)
rep([C8], '"mandorle 杏仁"', '"mandorle = almonds"', 1)
rep([C8], '"quanto costa? 多少钱"', '"quanto costa? = how much?"', 1)
rep([C8], '"pagare con carta 刷卡"', '"pagare con carta = to pay by card"', 1)
rep([C8], '"牛轧糖节持续到 11 月 22 日"', '"The torrone festival runs to 22 November"', 1)
# P8 H writing bridge + writing item (key is not printed for writing items;
# the note is printed as "150. ✓ <note>").
rep([C8], 'f.bridge(f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。")',
    'f.bridge(f"Writing task (no single right answer); the model text ({NWORDS} words) follows.")', 1)
rep([C8], '"（开放题，范文如下）"', '"(open task — model text below)"', 1)
rep([C8], 'f"范文见本版 H 区（{NWORDS} 词）"', 'f"Model text in section H below ({NWORDS} words)"', 1)
# P8 answer-key titles (W43 IT x EN shipped strings; separators stay Italian)
rep([C8], '"RISPOSTE · 参考答案 — 按版面分页排列，找到题号即可"',
    '"RISPOSTE · ANSWER KEY — grouped by page: find your exercise number"', 1)
rep([C8], '"每题附一句中文简析 · 带 ✓ 的为范文题"',
    '"Each answer has a one-line note in English · ✓ = model-text task"', 1)

# ---------- FIX ROUND 1 (P8 key-flow overflow, round-1 render) ----------
# Round 1 overflowed the P8 key flow by 8 wrapped lines (col2 +4, col4 +3,
# col1 +1 over the core's counts), pushing items 149-150 onto the footer
# rule. Wording-only trims below, each verified 1 line at 13pt serif in
# width 434 with the build's own wrap(); no layout parameter changes.
rep([C12], '"Both the Forum Cultura and the Panettone final are in Milan"',
    '"Forum Cultura and Panettone final: both in Milan"', 1)
rep([C34], '"assaggiare takes avere: abbiamo assaggiato"',
    '"assaggiare takes avere"', 1)
rep([C34, C8], '"Subject + essere + place + date"',
    '"Subject + essere + place"', 2)
rep([C34], '"Sunday evening matches are later than Friday\'s: più tardi"',
    '"Sunday matches are later than Friday\'s: più tardi"', 1)
rep([C34], '"più + bella: Sunday evening is the finest (a judgement)"',
    '"più + bella: Sunday evening is the finest"', 1)
rep([C8], '"assaggiare gratis = to taste for free"',
    '"assaggiare gratis = taste free"', 1)
rep([C8], '"On Sunday evening, Fiorentina play Juventus."',
    '"Sunday evening: Fiorentina play Juventus."', 1)

# ---------- FIX ROUND 2 (occlusion audit: 2 NEW P1 flags) ----------
# (a) Settimana subtitle overflowed its box (ink right 1934.8 > border
# 1885): shorten to a 398.3px line inside the 412px slot.
rep([C12], '"This week\'s diary · Cosa succede, giorno per giorno"',
    '"This week · Cosa succede, giorno per giorno"', 1)
# (b) Parola gloss wrapped to 2 lines and the 1864 row-B rule struck the
# second line ("mild autumn."). Shorten to a verified 1-line gloss at
# 19pt (402.1px < 434); the quoted Italian phrase itself carries
# "first cold", the gloss keeps "after a mild autumn".
rep([C12], '"‘Il primo freddo’: the first serious cold after a mild autumn."',
    '"‘Il primo freddo’: cold after a mild autumn."', 1)

print('TRANSFORM COMPLETE')
