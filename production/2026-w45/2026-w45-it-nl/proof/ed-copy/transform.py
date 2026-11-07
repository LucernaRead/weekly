# -*- coding: utf-8 -*-
"""W45 IT core -> IT x NL fan-out transform for the BUILD COPY ONLY.

Literal replacements only (tools README #17): each rep() fails loudly if
its old string is absent, so a typo can never silently skip a translation.
Italian target-language text is never a replacement target; only the
explanation layer (Chinese notes/bridges/titles/furniture) and the P8
E-section re-aiming change. Furniture follows the shipped W43 IT x NL
SVGs (badge REPLACES the 372 strapline at 20pt BRICK; footer; gloss
prefix "Uitleg — "; P8 separators "— Pagina n —"), which outrank the
generic rules in tools README #20. P7 readers'-corner disclosure is
bilingual BY CONSTRUCTION (see the content7 section): one 19pt note
block carrying the Italian disclosure sentence AND its Dutch equivalent
plus the imperative invitation "Schrijf ons voor VOL.3!".
"""
import pathlib, re, sys

B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-it-nl-build')
C12, C34, C56, C7, C8, BS, SV, RN = 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py', 'bslib4.py', 'svglib.py', 'render.py'
ALL = [C12, C34, C56, C7, C8]
CJK = re.compile(r'[\u4e00-\u9fff]')

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
rep(ALL, 'weekly-report-w45-it-core', 'weekly-report-w45-it-nl', 5)
rep([RN], 'weekly-report-w45-it-core', 'weekly-report-w45-it-nl', 1)
rep([RN], 'La-Lucerna-VOL2-web.pdf', 'La-Lucerna-VOL2-NL-web.pdf', 1)
rep([RN], 'La-Lucerna-VOL2.pdf', 'La-Lucerna-VOL2-NL.pdf', 1)
rep([RN], 'Render the IT weekly', 'Render the IT x NL edition', 1)

# ---------- bslib4 furniture (W43 IT x NL shipped strings, VOL.2) ----------
rep([BS], '"La Lucerna · 意大利语周报 VOL.2 · LUCERNA ITALIAN WEEKLY"',
    '"La Lucerna · ITALIAANS WEEKBLAD VOL.2 · TEKSTEN IN HET ITALIAANS · UITLEG IN HET NEDERLANDS"', 1)
rep([BS], 'f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} van {total}"', 1)
rep([BS], '"译注｜" + s', '"Uitleg — " + s', 1)
# svglib: one CJK docstring in an unused illustration helper; prints nothing.
rep([SV], 'for 重阳.', 'for Double Ninth Festival.', 1)

# ---------- exercise type names + printed instructions (W43 IT x NL) ----------
# instr first (printed labels), then bare type tokens (registry-only).
rep(ALL, 'instr="填空"', 'instr="Vul in"')
rep(ALL, 'instr="造句"', 'instr="Bouw de zin"')
rep(ALL, 'instr="翻译"', 'instr="Vertaal"')
rep(ALL, 'instr="把词和释义配对"', 'instr="Koppel woord en betekenis"')
rep(ALL, 'instr="判断"', 'instr="Waar of onwaar?"')
rep(ALL, 'instr="写作"', 'instr="Schrijf"')
rep(ALL, '"完成句子"', '"Voltooi de zin"')
rep(ALL, '"完形单选"', '"Meerkeuze invullen"')
rep(ALL, '"单选"', '"Meerkeuze"')
rep(ALL, '"造句"', '"Zinnen bouwen"')
rep(ALL, '"翻译"', '"Vertaling"')
rep(ALL, '"词汇配对"', '"Woorden koppelen"')
rep(ALL, '"判断对错"', '"Juist of onjuist"')
rep(ALL, '"句型转换"', '"Zin ombouwen"')
rep(ALL, '"写作"', '"Schrijven"')

# ---------- P1 masthead + pairing badge (W43 geometry: REPLACES 372 line, 20pt BRICK) ----------
rep([C12], '"OGNI SETTIMANA IN ITALIANO · 每周一期 · 读意大利人正在读的意大利语"',
    '"OGNI SETTIMANA IN ITALIANO · ELKE WEEK · HET ITALIAANS DAT DE ITALIANEN LEZEN"', 1)
rep([C12], 'p.text(975, 330, "意 大 利 语 周 报 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A", 46, "serif", True, INK, anchor="middle")',
    'p.text(975, 330, "ITALIAANS WEEKBLAD · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A", 43, "serif", True, INK, anchor="middle")', 1)
rep([C12], 'p.text(975, 372, "IL GIORNALE SETTIMANALE PER IMPARARE — L\'ITALIA VERA, IN ITALIANO, DALL\'ITALIA", 19, "sans", False, GREY, anchor="middle")',
    'p.text(975, 372, "TEKSTEN IN HET ITALIAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 20, "sans", True, BRICK, anchor="middle")', 1)
rep([C12], 'p.text(RIGHT - 30, 478, "本周迎来第一场寒冷", 24, "sans", True, "#b3a06a", anchor="end")',
    'p.text(RIGHT - 30, 478, "DE EERSTE KOU KOMT ERAAN", 24, "sans", True, "#b3a06a", anchor="end")', 1)
rep([C12], 'p.text(RIGHT - 30, 522, "初寒之周 · 详见第 2 版", 21, "sans", False, "#b3a06a", anchor="end")',
    'p.text(RIGHT - 30, 522, "De week van de eerste kou · zie pagina 2", 21, "sans", False, "#b3a06a", anchor="end")', 1)
rep([C12], '"LA NOTIZIA · 头条"', '"LA NOTIZIA · HET HOOFDNIEUWS"', 1)
rep([C12], '"讲解｜il primo freddo 第一场寒冷 · il versante adriatico 亚得里亚海一侧 · la previsione 预报 · assaggi 品尝。"',
    '"Uitleg — il primo freddo = eerste kou · il versante adriatico = Adriatische kant · la previsione = prognose · assaggi = proeven."', 1)
rep([C12], '"LA SETTIMANA IN CIFRE · 数字看本周"', '"LA SETTIMANA IN CIFRE · IN CIJFERS"', 1)
rep([C12], '（可能下初雪的海拔）', '(hoogte van de eerste lichte sneeuw)', 1)
rep([C12], '（米兰文化论坛 50 多场活动）', '(50+ Forum Cultura-evenementen in Milaan)', 1)
rep([C12], '（参加米兰潘妮托尼决赛的国家数）', '(landen bij de Panettone-finale in Milaan)', 1)
rep([C12], '（本周末意甲第 11 轮）', '(speelronde 11 dit weekend)', 1)
rep([C12], '"ADESSO TU · 即学即练"', '"ADESSO TU · NU JIJ"', 1)
rep([C12], '"本周日程 · Cosa succede, giorno per giorno"', '"Deze week · Cosa succede, giorno per giorno"', 1)
rep([C12], '"日程以各活动日历为准，时间可能有变。"', '"Data volgens de kalenders van de evenementen; tijden kunnen veranderen."', 1)
rep([C12], '"IN QUESTO NUMERO · 本期目录"', '"IN QUESTO NUMERO · INHOUD"', 1)
# P1 parola note MUST stay 1 line: the row-B rule sits at y=1864, 13px below
# the core's single note line. The fuller Dutch sentence wraps to 2 lines
# and would be struck by the rule.
rep([C12], '"“第一场寒冷”：温和秋天后的第一波寒冷。"', '"Eerste serieuze kou na een milde herfst."', 1)
rep([C12], '"IN BREVE · 快讯"', '"IN BREVE · IN HET KORT"', 1)
rep([C12], '"QUIZ LAMPO · 闪电问答"', '"QUIZ LAMPO · BLITSQUIZ"', 1)
rep([C12], '"读头版，选出正确答案 · 答案见第 8 版"', '"Lees de voorpagina en kies het juiste antwoord · Antwoorden op pagina 8"', 1)

# ---------- band titles / subs ----------
rep([C12], '"VITA · 生活"', '"VITA · LEVEN"', 1)
rep([C12], '"LIVELLO A2 · Il primo freddo e il 2 novembre · 初寒与追思日"',
    '"LIVELLO A2 · Il primo freddo e il 2 novembre · Eerste kou en 2 november"', 1)
rep([C34], '"CULTURA · 文化"', '"CULTURA · CULTUUR"', 1)
rep([C34], '"A2 → B1 · Panettone, torrone e musei aperti · 甜点与博物馆"',
    '"A2 → B1 · Panettone, torrone e musei aperti · Zoetigheid en open musea"', 1)
rep([C34], '"SPORT · 体育"', '"SPORT · SPORT"', 1)
rep([C34], '"LIVELLO B1 · La Serie A e l\'Europa · 意甲与欧战"',
    '"LIVELLO B1 · La Serie A e l\'Europa · Serie A en Europa"', 1)
rep([C56], '"GIOVANI · 青年"', '"GIOVANI · JONGEREN"', 1)
rep([C56], '"LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · 卢卡之后"',
    '"LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · Na Lucca"', 1)
rep([C56], '"APPROFONDIMENTO · 深读"', '"APPROFONDIMENTO · VERDIEPING"', 1)
rep([C56], '"LIVELLO B2 · Leggere le previsioni · 怎样读天气预报"',
    '"LIVELLO B2 · Leggere le previsioni · Voorspellingen leren lezen"', 1)
rep([C7], '"LINGUA · 语言"', '"LINGUA · TAAL"', 1)
rep([C7], '"聚焦语言 · Tre livelli, tre strumenti · 三个级别，三件工具"',
    '"Focus op de taal · Tre livelli, tre strumenti · Drie niveaus, drie hulpmiddelen"', 1)
rep([C8], '"VALUTAZIONE E RISPOSTE · 练习与答案"', '"VALUTAZIONE E RISPOSTE · TOETS EN ANTWOORDEN"', 1)
rep([C8], '"第 8 版 · La grande prova della settimana + tutte le risposte"',
    '"Pagina 8 · La grande prova della settimana + tutte le risposte"', 1)

# ---------- section heads / shared apparatus ----------
rep(ALL, '"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
    '"Antwoorden op pagina 8 · Niveaus staan door elkaar: zoek op nummer"')
rep(ALL, '"E TU? · 说说你自己"', '"E TU? · EN JIJ?"')
rep([C12], '"ESERCIZI · 第 2 版练习"', '"ESERCIZI · OEFENINGEN VAN PAGINA 2"', 1)
rep([C34], '"ESERCIZI · 第 3 版练习"', '"ESERCIZI · OEFENINGEN VAN PAGINA 3"', 1)
rep([C34], '"ESERCIZI · 第 4 版练习"', '"ESERCIZI · OEFENINGEN VAN PAGINA 4"', 1)
rep([C56], '"ESERCIZI · 第 5 版练习"', '"ESERCIZI · OEFENINGEN VAN PAGINA 5"', 1)
rep([C56], '"ESERCIZI · 第 6 版练习"', '"ESERCIZI · OEFENINGEN VAN PAGINA 6"', 1)
rep([C12], '"IL 2 NOVEMBRE · 追思日"', '"IL 2 NOVEMBRE · ALLERZIELEN"', 1)
rep([C34], '"LA SETTIMANA DEL CALCIO · 足球周"', '"LA SETTIMANA DEL CALCIO · VOETBALWEEK"', 1)
rep([C56], '"LE MINIME DI ESEMPIO · 练习用示例最低温 (DATI INVENTATI PER L\'ESERCIZIO)"',
    '"LE MINIME DI ESEMPIO · VOORBEELDMINIMA (DATI INVENTATI PER L\'ESERCIZIO)"', 1)
rep([C56], '"PROBABILITÀ · 概率"', '"PROBABILITÀ · KANS"', 1)

# ---------- bridges (printed grey sans) ----------
rep([C12], '"发稿时表决结果尚未确认，详见第 6 版。"',
    '"Bij het ter perse gaan was de uitslag nog niet bevestigd — zie pagina 6."', 1)
rep([C12], '"用意大利语补全句子。"', '"Vul de zinnen aan in het Italiaans."', 1)
rep([C12], '"补全动词的现在时形式。"', '"Vul de tegenwoordige tijd van de werkwoorden in."', 1)
rep([C12], '"读第 2 版文章，选出正确答案。"', '"Lees het artikel op pagina 2 en kies het juiste antwoord."', 1)
rep([C34], '"读第 3 版文章，选出正确答案。"', '"Lees het artikel op pagina 3 en kies het juiste antwoord."', 1)
rep([C34], '"用方框里的词填空。"', '"Vul in met de woorden uit het kader."', 1)
rep([C34], '"用 passato prossimo（近过去时）补全，注意助动词 avere / essere。"',
    '"Vul aan met de passato prossimo (voltooid tegenwoordige tijd); let op avere / essere."', 1)
rep([C34], '"把词组成正确的句子。"', '"Maak van de woorden correcte zinnen."', 1)
rep([C34], '"读第 4 版文章，选出正确答案。"', '"Lees het artikel op pagina 4 en kies het juiste antwoord."', 1)
rep([C34], '"用括号里词的比较级填空（数据看赛程表）。"',
    '"Vul de vergrotende trap van het woord tussen haakjes in (zie het speelschema)."', 1)
rep([C34], '"用 passato prossimo 补全。"', '"Vul aan met de passato prossimo."', 1)
rep([C56], '"读第 5 版文章，选出正确答案。"', '"Lees het artikel op pagina 5 en kies het juiste antwoord."', 1)
rep([C56], '"用方框里的词填空。注意：有的词要变成复数。"',
    '"Vul in met de woorden uit het kader. Let op: sommige woorden moeten in het meervoud."', 1)
rep([C56], '"用将来时（futuro semplice）补全。"', '"Vul aan met de toekomende tijd (futuro semplice)."', 1)
rep([C56], '"发稿时 10 月 28 日表决结果尚未确认：本期只写预期日期、争议点和 DPB 数字，不写结果。"',
    '"Bij het ter perse gaan was de uitslag van 28 oktober nog niet bevestigd: alleen de verwachte datum, het twistpunt en de DPB-cijfers staan in dit nummer."', 1)
# P6-A bridge MUST stay 1 line: the P6 exercise flow ends 11px above its
# bottom in the core; a 2-line Dutch bridge would overflow it.
rep([C56], '"看上面的练习图表，选出正确答案。"', '"Grafiek hierboven: kies het antwoord."', 1)
rep([C56], '"用方框里的词填空：probabilità · media · bollettino · modello"',
    '"Vul in met de woorden uit het kader: probabilità · media · bollettino · modello"', 1)
rep([C7], '"天气用无人称动词（第三人称单数）；“我冷”说 ho freddo，“外面冷”说 fa freddo。"',
    '"Het weer gebruikt onpersoonlijke werkwoorden (derde persoon enkelvoud): «ik heb het koud» is ho freddo, «het is koud» is fa freddo."', 1)
rep([C7], '"讲过去用近过去时：arrivare/andare 等用 essere，分词配合性数；avere 的分词不变。"',
    '"Over het verleden vertel je met de passato prossimo: arrivare/andare en zo gebruiken essere, het deelwoord past zich aan; met avere verandert het deelwoord niet."', 1)
rep([C7], '"è probabile che / è possibile che / bisogna che 后用虚拟式；so che、scrivono che 后用陈述式。"',
    '"Na è probabile che, è possibile che en bisogna che staat de aanvoegende wijs; na so che en scrivono che de aantonende wijs."', 1)

# ---------- gloss boxes (rendered gloss() strings; split on ·, counts must match core [6,5,4,4,5]) ----------
rep([C12], '"il cappotto 大衣 · la sciarpa 围巾 · i guanti 手套 · a strati 分层穿衣 · il termosifone 暖气片 · il crisantemo 菊花"',
    '"il cappotto = jas · la sciarpa = sjaal · i guanti = handschoenen · a strati = in laagjes · il termosifone = radiator · il crisantemo = chrysant"', 1)
rep([C34], '"il panettone 米兰圣诞面包 · il torrone 牛轧糖 · l\'assaggio 品尝 · la bancarella 摊位 · il cantiere 施工现场/修复工地。"',
    '"il panettone = zoet Milanees kerstbrood · il torrone = noga · l\'assaggio = proeven · la bancarella = kraam · il cantiere = bouwplaats/restauratie."', 1)
rep([C34], '"la giornata 轮次 · la presentazione 赛前介绍 · gli spalti 看台 · la sera 晚上。"',
    '"la giornata = speelronde · la presentazione = voorbeschouwing · gli spalti = tribunes · la sera = avond."', 1)
rep([C56], '"il cosplay 角色扮演服装 · gratuito 免费的 · il documentario 纪录片 · lo schermo 银幕。"',
    '"il cosplay = cosplaykostuum · gratuito = gratis · il documentario = documentaire · lo schermo = scherm."', 1)
rep([C56], '"la probabilità 概率 · la media 平均值 · il modello 模型/预报模式 · il bollettino 公报/预报 · aggiornare 更新。"',
    '"la probabilità = kans · la media = gemiddelde · il modello = weermodel · il bollettino = weerbericht · aggiornare = bijwerken."', 1)

# ---------- E TU notes (each string occurs twice per file: eh formula + para) ----------
rep([C12], '"初寒来了你穿什么：大衣、围巾还是手套？写两句意大利语寄给编辑部。"',
    '"Jas, sjaal of handschoenen? Schrijf twee zinnen in het Italiaans."')
rep([C34], '"你更喜欢传统潘妮托尼还是巧克力味的？写两句寄来。"',
    '"Panettone tradizionale of met chocolade? Schrijf twee zinnen en stuur ze op."')
rep([C34], '"周日晚上你看哪场比赛？写两句意大利语寄来。"',
    '"Welke wedstrijd kijk jij zondagavond? Schrijf twee zinnen in het Italiaans."')
rep([C56], '"卢卡之后你去哪：文化论坛、电影还是美食节？写两句寄来。"',
    '"Na Lucca: Forum Cultura, film of sagra? Schrijf twee zinnen en stuur ze op."')

# ---------- P5 week-plan parentheticals ----------
rep([C56], '（周二：米兰文化论坛开幕）', '(dinsdag: Forum Cultura opent in Milaan)', 1)
rep([C56], '（周三至周四：欧战直播）', '(woensdag–donderdag: Europees voetbal op tv)', 1)
rep([C56], '（周五准备周末）', '(vrijdag: weekend voorbereiden)', 1)
rep([C56], '（周六：米兰或克雷莫纳品尝）', '(zaterdag: proeven in Milaan of Cremona)', 1)
rep([C56], '（周日：意甲与返程）', '(zondag: Serie A en terugreis)', 1)

# ---------- exercise notes, content12 ----------
rep(ALL, '"il primo freddo = 第一场寒冷"', '"il primo freddo = de eerste kou"')
rep(ALL, '"la prima neve leggera = 初雪"', '"la prima neve leggera = eerste lichte sneeuw"')
rep(ALL, '"文化论坛与潘妮托尼决赛都在米兰"', '"Forum Cultura en Panettone-finale: allebei in Milaan"')
rep(ALL, '"克雷莫纳的节日叫 Festa del Torrone"', '"Het feest in Cremona heet Festa del Torrone"')
rep(ALL, '"意甲第 11 轮周日收官"', '"Speelronde 11 sluit op zondag"')
rep(ALL, '"previsioni = 预报（复数）"', '"previsioni = voorspellingen (meervoud)"')
rep(ALL, '"第一场寒冷在周一 11 月 2 日到来"', '"De eerste kou komt op maandag 2 november"')
rep(ALL, '"初雪在 1300–1500 米左右"', '"Eerste sneeuw rond 1.300–1.500 meter"')
rep(ALL, '"潘妮托尼决赛在米兰"', '"De Panettone-finale is in Milaan"')
rep(ALL, '"cappotto = 大衣"', '"cappotto = jas"')
rep(ALL, '"sciarpa = 围巾"', '"sciarpa = sjaal"')
rep(ALL, '"guanti = 手套（复数）"', '"guanti = handschoenen (meervoud)"')
rep(ALL, '"crisantemi = 菊花（复数）"', '"crisantemi = chrysanten (meervoud)"')
rep(ALL, '"termosifoni = 暖气片（复数）"', '"termosifoni = radiatoren (meervoud)"')
rep(ALL, '"fare freddo：fa freddo（天气）"', '"fare freddo: fa freddo (weer)"')
rep(ALL, '"mettere：io → metto"', '"mettere: io → metto"')
rep(ALL, '"portare：loro → portano"', '"portare: loro → portano"')
rep(ALL, '"guardare：loro → guardano"', '"guardare: loro → guardano"')
rep(ALL, '"restare：la scuola → resta（lei）"', '"restare: la scuola → resta (lei)"')
rep(ALL, '"11 月 2 日是追思日"', '"2 november is de herdenking"')
rep(ALL, '"追思日的花是菊花"', '"De bloem van 2 november is de chrysant"')
rep(ALL, '"分层穿衣：a strati"', '"In laagjes kleden: a strati"')
rep(ALL, '"诸圣节今年是周日、无连休"', '"Allerheiligen valt dit jaar op zondag, geen lang weekend"')
rep(ALL, '"cappotto=御寒大衣 c"', '"cappotto = warme jas c"')
rep(ALL, '"sciarpa=围巾 d"', '"sciarpa = sjaal d"')
rep(ALL, '"crisantemo=十一月的花 a"', '"crisantemo = novemberbloem a"')
rep(ALL, '"termosifone=暖气片 b"', '"termosifone = radiator b"')

# ---------- exercise notes, content34 ----------
rep(ALL, '"克雷莫纳牛轧糖节到 11 月 22 日"', '"Festa del Torrone duurt tot 22 november"')
rep(ALL, '"潘妮托尼决赛有 19 国糕点师"', '"19 landen doen mee aan de Panettone-finale"')
rep(ALL, '"文化论坛 11 月 3 日周二开幕"', '"Forum Cultura opent op dinsdag 3 november"')
rep(ALL, '"阿尔巴松露节到 12 月 6 日"', '"Truffelbeurs Alba sluit op 6 december"')
rep(ALL, '"panettone = 米兰圣诞面包"', '"panettone = zoet Milanees kerstbrood"')
rep(ALL, '"torrone = 牛轧糖"', '"torrone = noga"')
rep(ALL, '"assaggio = 品尝"', '"assaggio = proeven"')
rep(ALL, '"bancarella = 摊位"', '"bancarella = kraam"')
rep(ALL, '"mandorle = 杏仁（复数）"', '"mandorle = amandelen (meervoud)"')
rep(ALL, '"tartufo = 松露"', '"tartufo = truffel"')
rep(ALL, '"arrivare 用 essere：è arrivato"', '"arrivare gebruikt essere: è arrivato"')
rep(ALL, '"assaggiare 用 avere：abbiamo assaggiato"', '"assaggiare gebruikt avere: abbiamo assaggiato"')
rep(ALL, '"andare 用 essere，复数 sono andati"', '"andare gebruikt essere, meervoud: sono andati"')
rep(ALL, '"aprire 用 avere：ha aperto"', '"aprire gebruikt avere: ha aperto"')
rep(ALL, '"主语 + essere + 地点 + 日期"', '"onderwerp + essere + plaats + datum"')
rep(ALL, '"地点在前，主语在后"', '"plaats vooraan, onderwerp erna"')
rep(ALL, '"dura fino a = 持续到"', '"dura fino a = duurt tot"')
rep(ALL, '"周日晚上佛罗伦萨对尤文图斯"', '"Zondagavond: Fiorentina–Juventus"')
rep(ALL, '"欧战第 4 轮在 11 月 3–5 日"', '"Europese speelronde 4: 3–5 november"')
rep(ALL, '"欧战比赛只作前瞻、无结果"', '"Europese wedstrijden: alleen voorbeschouwing, geen uitslagen"')
rep(ALL, '"国米对科莫在圣西罗"', '"Inter–Como in San Siro"')
rep(ALL, '"giornata=联赛的一轮 c"', '"giornata = speelronde c"')
rep(ALL, '"presentazione=赛前介绍 b"', '"presentazione = voorbeschouwing b"')
rep(ALL, '"spalti=看台 a"', '"spalti = tribunes a"')
rep(ALL, '"sera=晚上 d"', '"sera = avond d"')
rep(ALL, '"周日晚上的比赛晚于周五的：più tardi"', '"Zondagavond later dan vrijdag: più tardi"')
rep(ALL, '"周五的比赛早于周日的：più presto"', '"Vrijdag eerder dan zondag: più presto"')
rep(ALL, '"più + bella 周日晚最美（主观评价）"', '"più + bella: zondagavond is het mooist (mening)"')
rep(ALL, '"bene 的比较级是不规则的 meglio"', '"vergrotende trap van bene is onregelmatig: meglio"')
rep(ALL, '"vincere：ha vinto"', '"vincere: ha vinto"')
rep(ALL, '"pareggiare：ha pareggiato"', '"pareggiare: ha pareggiato"')
rep(ALL, '"arrivare 用 essere，复数 sono arrivati"', '"arrivare gebruikt essere, meervoud: sono arrivati"')
rep(ALL, '"guardare 用 avere：abbiamo guardato"', '"guardare gebruikt avere: abbiamo guardato"')
rep(ALL, '"prendere 的分词是 preso：ha preso"', '"voltooid deelwoord van prendere is preso: ha preso"')

# ---------- exercise notes, content56 ----------
rep(ALL, '"卢卡漫画节是第 60 届"', '"Lucca Comics is de 60e editie"')
rep(ALL, '"文化论坛 11 月 3 日开幕"', '"Forum Cultura opent op 3 november"')
rep(ALL, '"民俗电影节在佛罗伦萨"', '"Festival dei Popoli is in Florence"')
rep(ALL, '"文化论坛有 50 多场活动"', '"Forum Cultura: meer dan 50 evenementen"')
rep(ALL, '"卢卡漫画节主题是 Legacy"', '"Thema van Lucca Comics is «Legacy»"')
rep(ALL, '"armadio = 衣柜"', '"armadio = kast"')
rep(ALL, '"gratuiti = 免费的（阳性复数）"', '"gratuiti = gratis (mannelijk meervoud)"')
rep(ALL, '"documentario = 纪录片"', '"documentario = documentaire"')
rep(ALL, '"schermo = 银幕"', '"schermo = scherm"')
rep(ALL, '"castagne arrosto 烤栗子（复数）"', '"castagne arrosto = geroosterde kastanjes (meervoud)"')
rep(ALL, '"cosplay = 角色扮演服装"', '"cosplay = cosplaykostuum"')
rep(ALL, '"andare 将来时 noi：andremo"', '"andare, toekomende tijd, noi: andremo"')
rep(ALL, '"esserci 将来时：ci sarà（将有）"', '"esserci, toekomende tijd: ci sarà (er zal zijn)"')
rep(ALL, '"guardare 将来时 noi：guarderemo"', '"guardare, toekomende tijd, noi: guarderemo"')
rep(ALL, '"durare 将来时：durerà"', '"durare, toekomende tijd: durerà"')
rep(ALL, '"示例数据中最冷的是都灵 3°"', '"Koudste voorbeeldstad is Turijn (3°)"')
rep(ALL, '"示例数据中最暖的是那不勒斯 12°"', '"Warmste voorbeeldstad is Napels (12°)"')
rep(ALL, '"图表数据是练习用的、不是真实预报"', '"De grafiekcijfers zijn oefendata, geen echte voorspelling"')
rep(ALL, '"高概率不等于确定"', '"Grote kans is geen zekerheid"')
rep(ALL, '"预报基于 ECMWF 等模型"', '"Voorspellingen steunen op modellen als ECMWF"')
rep(ALL, '"预报会变，因为大气变化快"', '"Voorspellingen veranderen: de atmosfeer verandert snel"')
rep(ALL, '"DPB 于 10 月 15 日送布鲁塞尔"', '"DPB ging op 15 oktober naar Brussel"')
rep(ALL, '"2027 增长预测 +0,8%"', '"Groei 2027 voorspeld op +0,8%"')
rep(ALL, '"è probabile che + 虚拟式 piova"', '"è probabile che + aanvoegende wijs: piova"')
rep(ALL, '"è possibile che + 虚拟式 nevichi"', '"è possibile che + aanvoegende wijs: nevichi"')
rep(ALL, '"bisogna che + 虚拟式 controllino"', '"bisogna che + aanvoegende wijs: controllino"')
rep(ALL, '"è importante che + 虚拟式 sia"', '"è importante che + aanvoegende wijs: sia"')
rep(ALL, '"probabilità = 概率"', '"probabilità = kans"')
rep(ALL, '"media = 平均值"', '"media = gemiddelde"')
rep(ALL, '"bollettino = 预报公报"', '"bollettino = weerbericht"')
rep(ALL, '"modello = 预报模型"', '"modello = weermodel"')

# ---------- exercise notes, content7 ----------
rep(ALL, '"piovere 天气动词：piove"', '"piovere, weerwerkwoord: piove"')
rep(ALL, '"fa freddo = 天气冷"', '"fa freddo = het is koud (weer)"')
rep(ALL, '"nevicare：nevica"', '"nevicare: nevica"')
rep(ALL, '"“我冷”说 ho freddo"', '"«ik heb het koud» is ho freddo"')
rep(ALL, '"assaggiare 用 avere"', '"assaggiare gebruikt avere"')
rep(ALL, '"aprire 用 avere + 不变分词"', '"aprire gebruikt avere + onveranderd deelwoord"')
rep(ALL, '"bisogna che + 虚拟式 sia"', '"bisogna che + aanvoegende wijs: sia"')
rep(ALL, '"so che + 陈述式 arriva"', '"so che + aantonende wijs: arriva"')

# ---------- P7 language columns ----------
rep([C7], '"ERRORI TIPICI · 常见错误"', '"ERRORI TIPICI · VEEL FOUTEN"', 1)
rep([C7], '"fa 后面的 freddo 永远不变。"', '"Na fa blijft freddo onveranderd."', 1)
rep([C7], '"nevicare 只用第三人称单数。"', '"Nevicare: alleen 3e persoon enkelvoud."', 1)
rep([C7], '"预报给的是概率，不是确定性。"', '"Voorspelling = kans, geen zekerheid."', 1)
rep([C7], '"gente 是单数，动词形容词用单数阴性。"', '"Gente is enkelvoud, vrouwelijk."', 1)
# P7 word box: Italian definition sentence stays VERBATIM (blocking gate);
# only the gloss is localized. Short gloss keeps the parola box at its
# core height, which pays for the longer readers'-corner note below.
rep([C7], '"assaggio = 品尝。本周见第 3 版：潘妮托尼决赛上观众可以免费品尝。"',
    '"assaggio = proeven (gratis, p. 3)."')
rep([C7], '"LA PAROLA · 本周生词"', '"LA PAROLA · WOORD VAN DE WEEK"', 1)
# Readers' corner (coordinator clarification 2026-10-27, following the
# IT x EN B1 adjudication): the core carries NO Italian disclosure
# sentence to preserve — its Italian elements are the letter verbatim,
# the "(esempio della redazione)" label, and the VOL.3 preview promise,
# all kept untouched. The disclosure sentence itself is therefore written
# in Dutch only: all 3 facts (no real letters, no best page-8 essay,
# example + promise deferred to VOL.3) + the imperative invitation
# "Schrijf ons voor VOL.3!". NO new Italian disclosure sentence is
# invented. Rendered at 19pt (not 20pt): 4 lines, so the letter box grows
# by one line only, exactly offset by the shorter parola gloss above —
# P7 column 3 still ends clear of the FRASI rule at y=1686.
# Printed note is Dutch only (no Italian disclosure sentence is invented):
_DISC_PRINT = ("Voorbeeld van de redactie, geen echte brief: nog geen echte brieven, "
               "geen beste opstel van pagina 8 — beide in VOL.3. Schrijf ons voor VOL.3!")
rep([C7], 'len(wrap("这是编辑部示例信，非真实来信。来信请寄编辑部，VOL.3 刊登真实来信与第 8 版最佳作文！", "sans", False, 20, CW - 44)) * 29 + 20',
    'len(wrap("' + _DISC_PRINT + '", "sans", False, 19, CW - 44)) * 27 + 20', 1)
rep([C7], 'p.para(bx + 22, yy3 + 20, "这是编辑部示例信，非真实来信。来信请寄编辑部，VOL.3 刊登真实来信与第 8 版最佳作文！", 20, "sans", False, GREY, CW - 44, 1.42)',
    'p.para(bx + 22, yy3 + 20, "' + _DISC_PRINT + '", 19, "sans", False, GREY, CW - 44, 1.42)', 1)
rep([C7], '"FRASI DELLA SETTIMANA · 本周金句（逐字摘自本期文章）"',
    '"FRASI DELLA SETTIMANA · ZINNEN VAN DE WEEK (woordelijk uit dit nummer)"', 1)
rep([C7], '"第一场真正的寒冷到来了。"', '"De eerste echte kou van het seizoen komt eraan."', 1)
rep([C7], '"这不是确定性，而是概率。"', '"Het is geen zekerheid, het is een kans."', 1)
rep([C7], '"11 月 2 日是追思日。"', '"2 november is de herdenking van de overledenen."', 1)
rep([C7], '"天冷，穿暖和点！"', '"Het is koud, kleed je warm aan!"', 1)
rep([C7], '"观众可以免费品尝。"', '"Het publiek kan gratis proeven."', 1)
rep([C7], '"足球不会因为第一场寒冷而停下。"', '"Voetbal stopt niet voor de eerste kou."', 1)
rep([C7], '"文化继续。"', '"De cultuur gaat door."', 1)
rep([C7], '"高概率不等于确定性。"', '"Een grote kans is geen zekerheid."', 1)
rep([C7], '"LA PROSSIMA SETTIMANA · 下期预告 (VOL.3)"', '"LA PROSSIMA SETTIMANA · VOLGENDE WEEK (VOL.3)"', 1)

# ---------- four stragglers found by the CJK safety net (round 1) ----------
rep([C12], '"LA FRASE PER RICORDARE · 口诀"', '"LA FRASE PER RICORDARE · EZELSBRUG"', 1)
rep(ALL, '"卢卡漫画节到 11 月 8 日才结束是错的"', '"Lucca Comics sloot al op 1 november"')
rep(ALL, '"概率不等于确定"', '"Kans is geen zekerheid"')

# ---------- P8: E-section re-aiming (W43 IT x NL ruling), H writing, RISPOSTE ----------
# (P8 band sub was already replaced in the band-titles section above.)
# E-section: 137/138 re-aimed IT->NL (Dutch keys); 139 reverse (Dutch stem,
# Italian key byte-identical); 140 reverse (Dutch stem, Italian key kept).
rep([C8], '"周一第一场寒冷来了。"', '"Op maandag komt de eerste kou."', 1)
rep([C8], '"对照原文"', '"zie de originele zin"', 1)
rep([C8], '"观众可以免费品尝。"', '"Het publiek kan gratis proeven."', 1)
rep([C8], '"assaggiare gratis = 免费品尝"', '"assaggiare gratis = gratis proeven"', 1)
rep([C8], '"周日晚上，佛罗伦萨对尤文图斯。"', '"Domenica sera si gioca Fiorentina–Juventus."', 1)
rep([C8], '"si gioca = 进行比赛"', '"si gioca = er wordt gespeeld"', 1)
rep([C8], '"Domenica sera si gioca Fiorentina–Juventus. → ___"',
    '"Op zondagavond speelt Fiorentina tegen Juventus. → ___"', 1)
rep([C8], '"每个预报都必须清楚。→ ___"', '"Elke voorspelling moet duidelijk zijn. → ___"', 1)
rep([C8], '"dovere = 必须"', '"dovere = moeten"', 1)
rep([C8], 'f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。"',
    'f"Schrijfopdracht (geen uniek antwoord); het model ({NWORDS} woorden) staat hieronder."', 1)
rep([C8], '"（开放题，范文如下）"', '"(open vraag — het model staat hieronder)"', 1)
rep([C8], 'f"范文见本版 H 区（{NWORDS} 词）"',
    'f"Het model staat in sectie H van deze pagina ({NWORDS} woorden)"', 1)
rep([C8], '"RISPOSTE · 参考答案 — 按版面分页排列，找到题号即可"',
    '"RISPOSTE · ANTWOORDEN — per pagina gerangschikt: zoek op nummer"', 1)
rep([C8], '"每题附一句中文简析 · 带 ✓ 的为范文题"',
    '"Elke opgave heeft een korte uitleg in het Nederlands · ✓ = schrijfopgave met model"', 1)
rep([C8], 'f"— PAGINA {pg} —"', 'f"— Pagina {pg} —"', 1)

# ---------- exercise notes, content8 ----------
rep(ALL, '"primo freddo = 第一场寒冷"', '"primo freddo = de eerste kou"')
rep(ALL, '"追思日在 11 月 2 日"', '"Herdenking op 2 november"')
rep(ALL, '"文化论坛在米兰开幕"', '"Forum Cultura opent in Milaan"')
rep(ALL, '"潘妮托尼决赛在周六日"', '"Panettone-finale op zaterdag en zondag"')
rep(ALL, '"牛轧糖节在克雷莫纳"', '"Festa del Torrone in Cremona"')
rep(ALL, '"意甲第 11 轮周日收官：chiude"', '"Speelronde 11 sluit zondag: chiude"')
rep(ALL, '"佛罗伦萨对尤文图斯在周日晚上"', '"Fiorentina–Juventus op zondagavond"')
rep(ALL, '"DPB 于 10 月 15 日送出"', '"DPB vertrok op 15 oktober naar Brussel"')
rep(ALL, '"卢卡漫画节 11 月 1 日闭幕"', '"Lucca Comics sloot op 1 november"')
rep(ALL, '"Giulia 去米兰潘妮托尼决赛"', '"Giulia gaat naar de Panettone-finale in Milaan"')
rep(ALL, '"Paolo 周六去牛轧糖节"', '"Paolo gaat zaterdag naar de Festa del Torrone"')
rep(ALL, '"传统潘妮托尼是 Giulia 品尝的"', '"De traditionele panettone wordt door Giulia geproefd"')
rep(ALL, '"标题概括两个城市、两个节日"', '"De titel vat twee steden en twee feesten samen"')
rep(ALL, '"时间词在前"', '"tijdwoord vooraan"')
rep(ALL, '"疑问词组在句首"', '"vraagwoordgroep vooraan"')
rep(ALL, '"主语 + 动词 + 时间"', '"onderwerp + werkwoord + tijd"')
rep(ALL, '"probabilità=可能性 d"', '"probabilità = kans d"')
rep(ALL, '"media=平均值 a"', '"media = gemiddelde a"')
rep(ALL, '"bollettino=预报公报 b"', '"bollettino = weerbericht b"')
rep(ALL, '"modello=预报模型 c"', '"modello = weermodel c"')
rep(ALL, '"mandorle 杏仁"', '"mandorle: amandelen"')
rep(ALL, '"quanto costa? 多少钱"', '"quanto costa? = hoeveel kost het?"')
rep(ALL, '"pagare con carta 刷卡"', '"pagare con carta = met kaart betalen"')
rep(ALL, '"牛轧糖节持续到 11 月 22 日"', '"Festa del Torrone duurt tot 22 november"')

# ---------- Fix round 2 (round-1 defects; all wording-only, in transform.py) ----------
# R1-1: P1-headline FLOW OVERFLOW x2, ended 1945 vs bottom 1828 (core ends
#   1497 — the Dutch bridge + cifre growth shifted a column break, adding
#   ~448px). Fix: restore the core's exact line counts — bridge 4->3 lines
#   (edited above) and cifre item 4 3->2 lines (edited above).
# R1-2: P7 col3 ended 1694, 8px past the FRASI rule at 1686. Cause: the
#   parola gloss was measured at width 434 (1 line) but renders at 390
#   (2 lines). Fix: gloss shortened to a verified 1-line string at 390
#   (edited above) — col3 now ends 1665, 21px clear of the rule.
# R1-3: P8-keys ended 2561, 9px past its 2552 bottom (core ends 2484).
#   Fix: trim three 2-line answer notes to 1 line each (meaning kept):
rep(ALL, '"assaggiare gebruikt avere: abbiamo assaggiato"', '"assaggiare gebruikt avere"')
rep(ALL, '"Europese wedstrijden: alleen voorbeschouwing, geen uitslagen"', '"Europese wedstrijden: alleen voorbeschouwing"')
rep(ALL, '"assaggiare gratis = gratis proeven"', '"assaggiare gratis = proeven"')

# ---------- Fix round 3 (round-2 occlusion audit: 3 BOXTITLE flags) ----------
# R2-1: P1 settimana footnote at x=1473 ran to ink 2048.5, past the box
#   border (1885) and the page frame (1910) — a single unwrapped p.text
#   whose Dutch translation (575.6px at 16.5pt) outgrew the core's short
#   Chinese line. Fix: shorten to 323.2px (right 1796.2, inside the box),
#   keeping both disclaimer facts (dates per calendar; times may change).
#   (EN precedent: EN shortened the same footnote to fit.)
rep(ALL, '"Data volgens de kalenders van de evenementen; tijden kunnen veranderen."',
    '"Data per kalender; tijden kunnen wijzigen."')
# R2-2: P2 frase box title at 23pt bold ran to ink 1005.5, 44.5px past its
#   box border (961) into empty gutter (no text overlap, but sloppy).
#   Fix: tsize=20 — the exact W43 NL precedent for this same title.
rep([C12], 'vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),\n])',
    'vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),\n], tsize=20)')
# R2-3: P7 parola gloss descenders reached ink 1285.6, 1.1px past the box
#   bottom (1284.5) — the wh formula leaves only ~3.9px below the last
#   baseline, but Latin descenders need ~5px (core's CJK gloss had none).
#   Fix: +3px box padding (bottom 1287.5, ink inside by 1.9px); the letter
#   box shifts +3 with it, col3 ends 1668, still 18px clear of the rule.
rep([C7], 'len(wrap("assaggio = proeven (gratis, p. 3).", "sans", False, 20, CW - 44)) * 29 + 20',
    'len(wrap("assaggio = proeven (gratis, p. 3).", "sans", False, 20, CW - 44)) * 29 + 23')

# ---------- Fix round 4 (round-2 audit flag missed under tail truncation) ----------
# R2-4: P1 numbers box title at 23pt bold ran to ink 967.0, 6px past its
#   box border (961) — the core's title just fits (CJK tail narrower than
#   the Dutch "IN CIJFERS" tail). Fix: tsize=20, the exact W43 NL precedent
#   for this same title (W43 ships it at 20pt). Predicted ink right ~912.
rep([C12], 'la giornata di Serie A del fine settimana(speelronde 11 dit weekend)", "serif", False, INK, 20.5, 1.35),\n])',
    'la giornata di Serie A del fine settimana(speelronde 11 dit weekend)", "serif", False, INK, 20.5, 1.35),\n], tsize=20)')

# ---------- final safety net: no CJK may remain in any rendered-code file ----------
for fn in [C12, C34, C56, C7, C8, BS, SV]:
    t = (B / fn).read_text(encoding='utf-8')
    left = sorted(set(CJK.findall(t)))
    if left:
        print(f'CJK REMAINS in {fn}: {left}'); sys.exit(1)
print('transform OK: all replacements applied, no CJK remains in build code')
