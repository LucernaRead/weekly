# -*- coding: utf-8 -*-
"""IT x DE fan-out transform for W45 IT core build copy.
Rules: whole-string or exact-unique-literal replacements with count
assertions; value maps use bare text, never repr. Italian body text is
NEVER touched: every `old` below is a Chinese explanation-layer string,
a bilingual furniture string, or a printed instruction token.
Furniture follows the shipped W43 IT x DE SVG verbatim (badge inserted
at y=574, 22pt bold BRICK; footer VOL.2 per tables.py furniture de
--target it --vol 2; Seite N von 8; gloss prefix HINWEIS; P8
separators stay core-style PAGINA per the W43 shipped precedent, NOT
the generic tables DE separator).
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
    rep(f, "weekly-report-w45-it-core", "weekly-report-w45-it-de", 1)
rep("render.py", "weekly-report-w45-it-core", "weekly-report-w45-it-de", 1)
rep("render.py", "La-Lucerna-VOL2.pdf", "La-Lucerna-VOL2-DE.pdf", 1)
rep("render.py", "La-Lucerna-VOL2-web.pdf", "La-Lucerna-VOL2-DE-web.pdf", 1)

# ---------- svglib docstring comment only (not rendered) ----------
rep("svglib.py", "for 重阳.", "for Double Ninth.", 1)

# ---------- bslib4: furniture + gloss prefix (W43 IT x DE shipped forms, VOL.2) ----------
rep("bslib4.py",
    '"La Lucerna · 意大利语周报 VOL.2 · LUCERNA ITALIAN WEEKLY"',
    '"La Lucerna · ITALIENISCHE WOCHENZEITUNG VOL.2 · TEXT AUF ITALIENISCH · ERKLÄRUNGEN AUF DEUTSCH"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Seite {n} von {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"HINWEIS · " + s', 1)

# ---------- shared printed instruction tokens (only where present) ----------
INSTR = [
    ('instr="填空"', 'instr="Ausfüllen"'),
    ('instr="造句"', 'instr="Sätze bilden"'),
    ('instr="翻译"', 'instr="Übersetzen"'),
    ('instr="判断"', 'instr="Entscheiden"'),
    ('instr="写作"', 'instr="Schreiben"'),
    ('instr="把词和释义配对"', 'instr="Zuordnen"'),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Lösungen auf Seite 8 · Aufgaben gemischt — nach Nummern suchen"),
    ("E TU? · 说说你自己", "E TU? · UND DU?"),
]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTR:
        rep_if(f, old, new)

# ================= content12 (P1 + P2) =================
pairs("content12.py", [
    ("OGNI SETTIMANA IN ITALIANO · 每周一期 · 读意大利人正在读的意大利语",
     "OGNI SETTIMANA IN ITALIANO · ITALIENISCH, WIE ITALIEN ES LIEST"),
    ("意 大 利 语 周 报 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A",
     "ITALIENISCH · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A"),
    # band right + pairing badge (W43 shipped geometry: y=574, 22pt bold BRICK)
    ('p.text(RIGHT - 30, 478, "本周迎来第一场寒冷", 24, "sans", True, "#b3a06a", anchor="end")\n'
     'p.text(RIGHT - 30, 522, "初寒之周 · 详见第 2 版", 21, "sans", False, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 478, "DIESE WOCHE KOMMT DIE ERSTE KÄLTE", 24, "sans", True, "#b3a06a", anchor="end")\n'
     'p.text(RIGHT - 30, 522, "Die Woche der ersten Kälte · siehe Seite 2", 21, "sans", False, "#b3a06a", anchor="end")\n'
     '\n'
     '# pairing badge (masthead area, below the band; W43 IT x DE geometry)\n'
     'p.text(975, 574, "ITALIENISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", 22, "sans", True, BRICK, anchor="middle")'),
    ("LA NOTIZIA · 头条", "LA NOTIZIA · DIE TITELSTORY"),
    ("讲解｜il primo freddo 第一场寒冷 · il versante adriatico 亚得里亚海一侧 · la previsione 预报 · assaggi 品尝。",
     "HINWEIS · il primo freddo = die erste Kälte · il versante adriatico = die Adriaseite · la previsione = die Vorhersage · assaggi = Kostproben."),
    ("LA SETTIMANA IN CIFRE · 数字看本周", "LA SETTIMANA IN CIFRE · ZAHLEN"),
    ("（可能下初雪的海拔）", "(mögliche Schneefallgrenze)"),
    ("（米兰文化论坛 50 多场活动）", "(über 50 Veranstaltungen des Forum Cultura)"),
    ("（参加米兰潘妮托尼决赛的国家数）", "(Länder beim Panettone-Finale in Mailand)"),
    ("（本周末意甲第 11 轮）", "(11. Spieltag der Serie A am Wochenende)"),
    ("ADESSO TU · 即学即练", "ADESSO TU · SIE SIND DRAN"),
    ("il primo freddo = 第一场寒冷", "il primo freddo = die erste Kälte"),
    ("la prima neve leggera = 初雪", "la prima neve leggera = der erste leichte Schnee"),
    ("文化论坛与潘妮托尼决赛都在米兰", "Forum Cultura und Panettone-Finale sind beide in Mailand"),
    ("克雷莫纳的节日叫 Festa del Torrone", "Das Fest in Cremona heißt Festa del Torrone"),
    ("意甲第 11 轮周日收官", "Der 11. Spieltag endet am Sonntag"),
    ("previsioni = 预报（复数）", "previsioni = Vorhersagen (Plural)"),
    ("本周日程 · Cosa succede, giorno per giorno", "Der Wochenplan · Cosa succede, giorno per giorno"),
    ("日程以各活动日历为准，时间可能有变。", "Die Termine folgen den Kalendern der Veranstaltungen; Uhrzeiten können sich ändern."),
    ("IN QUESTO NUMERO · 本期目录", "IN QUESTO NUMERO · INHALT"),
    ("“第一场寒冷”：温和秋天后的第一波寒冷。", "„il primo freddo“: die erste ernsthafte Kälte nach einem milden Herbst."),
    ("IN BREVE · 快讯", "IN BREVE · KURZ GEMELDET"),
    ("QUIZ LAMPO · 闪电问答", "QUIZ LAMPO · BLITZQUIZ"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Lesen Sie die Titelseite und wählen Sie die richtige Antwort · Lösungen auf Seite 8"),
    ("第一场寒冷在周一 11 月 2 日到来", "Die erste Kälte kommt am Montag, 2. November"),
    ("初雪在 1300–1500 米左右", "Der erste Schnee fällt um 1.300–1.500 Meter"),
    ("潘妮托尼决赛在米兰", "Das Panettone-Finale ist in Mailand"),
    # P2
    ("VITA · 生活", "VITA · LEBEN"),
    ("LIVELLO A2 · Il primo freddo e il 2 novembre · 初寒与追思日",
     "LIVELLO A2 · Il primo freddo e il 2 novembre · Erste Kälte und Allerseelen"),
    ("发稿时表决结果尚未确认，详见第 6 版。", "Bei Redaktionsschluss war das Abstimmungsergebnis noch nicht bestätigt: siehe Seite 6."),
    ("LA FRASE PER RICORDARE · 口诀", "LA FRASE PER RICORDARE · MERKSATZ"),
    ("il cappotto 大衣 · la sciarpa 围巾 · i guanti 手套 · a strati 分层穿衣 · il termosifone 暖气片 · il crisantemo 菊花",
     "il cappotto = Mantel · la sciarpa = Schal · i guanti = Handschuhe · a strati = in Schichten · il termosifone = Heizkörper · il crisantemo = Chrysantheme"),
    ("初寒来了你穿什么：大衣、围巾还是手套？写两句意大利语寄给编辑部。",
     "Was ziehen Sie an, wenn die erste Kälte kommt: Mantel, Schal oder Handschuhe? Schreiben Sie zwei Sätze auf Italienisch!"),
    ("IL 2 NOVEMBRE · 追思日", "IL 2 NOVEMBRE · ALLERSEELEN"),
    ("ESERCIZI · 第 2 版练习", "ESERCIZI · ÜBUNGEN ZU SEITE 2"),
    ("用意大利语补全句子。", "Ergänzen Sie die Sätze auf Italienisch."),
    ("cappotto = 大衣", "cappotto = Mantel"),
    ("sciarpa = 围巾", "sciarpa = Schal"),
    ("guanti = 手套（复数）", "guanti = Handschuhe (Plural)"),
    ("crisantemi = 菊花（复数）", "crisantemi = Chrysanthemen (Plural)"),
    ("termosifoni = 暖气片（复数）", "termosifoni = Heizkörper (Plural)"),
    ("补全动词的现在时形式。", "Ergänzen Sie die Verben im Präsens."),
    ("fare freddo：fa freddo（天气）", "fare freddo: fa freddo (Wetter)"),
    ("mettere：io → metto", "mettere: io → metto"),
    ("portare：loro → portano", "portare: loro → portano"),
    ("guardare：loro → guardano", "guardare: loro → guardano"),
    ("restare：la scuola → resta（lei）", "restare: la scuola → resta (lei)"),
    ("读第 2 版文章，选出正确答案。", "Lesen Sie den Artikel auf Seite 2 und wählen Sie die richtige Antwort."),
    ("11 月 2 日是追思日", "Der 2. November ist Allerseelen"),
    ("追思日的花是菊花", "Die Blume des 2. November ist die Chrysantheme"),
    ("分层穿衣：a strati", "In Schichten anziehen: a strati"),
    ("诸圣节今年是周日、无连休", "Allerheiligen fällt dieses Jahr auf einen Sonntag, ohne Brückentag"),
    ("cappotto=御寒大衣 c", "cappotto = warmer Mantel, c"),
    ("sciarpa=围巾 d", "sciarpa = Schal, d"),
    ("crisantemo=十一月的花 a", "crisantemo = Novemberblume, a"),
    ("termosifone=暖气片 b", "termosifone = Heizkörper, b"),
])
print("content12 done")

# ================= content34 (P3 + P4) =================
pairs("content34.py", [
    ("CULTURA · 文化", "CULTURA · KULTUR"),
    ("A2 → B1 · Panettone, torrone e musei aperti · 甜点与博物馆",
     "A2 → B1 · Panettone, torrone e musei aperti · Süßes und offene Museen"),
    ("il panettone 米兰圣诞面包 · il torrone 牛轧糖 · l'assaggio 品尝 · la bancarella 摊位 · il cantiere 施工现场/修复工地。",
     "il panettone = Mailänder Weihnachtskuchen · il torrone = Nougat · l'assaggio = Kostprobe · la bancarella = Stand · il cantiere = Baustelle"),
    ("你更喜欢传统潘妮托尼还是巧克力味的？写两句寄来。",
     "Traditionell oder mit Schokolade? Schreiben Sie zwei Sätze!"),
    ("ESERCIZI · 第 3 版练习", "ESERCIZI · ÜBUNGEN ZU SEITE 3"),
    ("读第 3 版文章，选出正确答案。", "Lesen Sie den Artikel auf Seite 3 und wählen Sie die richtige Antwort."),
    ("潘妮托尼决赛在米兰", "Das Panettone-Finale ist in Mailand"),
    ("克雷莫纳牛轧糖节到 11 月 22 日", "Das Torrone-Fest in Cremona geht bis zum 22. November"),
    ("潘妮托尼决赛有 19 国糕点师", "Am Panettone-Finale nehmen Konditoren aus 19 Ländern teil"),
    ("文化论坛 11 月 3 日周二开幕", "Das Forum Cultura eröffnet am Dienstag, 3. November"),
    ("阿尔巴松露节到 12 月 6 日", "Das Trüffelfest in Alba geht bis zum 6. Dezember"),
    ("用方框里的词填空。", "Ergänzen Sie die Wörter aus dem Kasten."),
    ("panettone = 米兰圣诞面包", "panettone = Mailänder Weihnachtskuchen"),
    ("torrone = 牛轧糖", "torrone = Nougat"),
    ("assaggio = 品尝", "assaggio = Kostprobe"),
    ("bancarella = 摊位", "bancarella = Stand"),
    ("mandorle = 杏仁（复数）", "mandorle = Mandeln (Plural)"),
    ("tartufo = 松露", "tartufo = Trüffel"),
    ("用 passato prossimo（近过去时）补全，注意助动词 avere / essere。",
     "Ergänzen Sie mit dem passato prossimo. Achtung: Hilfsverb avere oder essere."),
    ("arrivare 用 essere：è arrivato", "arrivare mit essere: è arrivato"),
    ("assaggiare 用 avere：abbiamo assaggiato", "assaggiare mit avere: abbiamo assaggiato"),
    ("andare 用 essere，复数 sono andati", "andare mit essere, Plural: sono andati"),
    ("aprire 用 avere：ha aperto", "aprire mit avere: ha aperto"),
    ("把词组成正确的句子。", "Bilden Sie aus den Wörtern richtige Sätze."),
    ("主语 + essere + 地点 + 日期", "Subjekt + essere + Ort + Datum"),
    ("地点在前，主语在后", "Ort zuerst, Subjekt danach"),
    ("dura fino a = 持续到", "dura fino a = dauert bis"),
    # P4
    ("SPORT · 体育", "SPORT · SPORT"),
    ("LIVELLO B1 · La Serie A e l'Europa · 意甲与欧战",
     "LIVELLO B1 · La Serie A e l'Europa · Serie A und Europa"),
    ("la giornata 轮次 · la presentazione 赛前介绍 · gli spalti 看台 · la sera 晚上。",
     "la giornata = Spieltag · la presentazione = Vorschau · gli spalti = Tribünen · la sera = Abend"),
    ("周日晚上你看哪场比赛？写两句意大利语寄来。",
     "Welches Spiel sehen Sie am Sonntagabend? Schreiben Sie zwei Sätze auf Italienisch!"),
    ("LA SETTIMANA DEL CALCIO · 足球周", "LA SETTIMANA DEL CALCIO · FUSSBALLWOCHE"),
    ("ESERCIZI · 第 4 版练习", "ESERCIZI · ÜBUNGEN ZU SEITE 4"),
    ("读第 4 版文章，选出正确答案。", "Lesen Sie den Artikel auf Seite 4 und wählen Sie die richtige Antwort."),
    ("意甲第 11 轮周日收官", "Der 11. Spieltag endet am Sonntag"),
    ("周日晚上佛罗伦萨对尤文图斯", "Am Sonntagabend spielt Fiorentina gegen Juventus"),
    ("欧战第 4 轮在 11 月 3–5 日", "Der 4. Europapokal-Spieltag ist vom 3. bis 5. November"),
    ("欧战比赛只作前瞻、无结果", "Die Europapokalspiele sind nur Vorschau, ohne Ergebnisse"),
    ("国米对科莫在圣西罗", "Inter gegen Como ist in San Siro"),
    ("giornata=联赛的一轮 c", "giornata = Spieltag, c"),
    ("presentazione=赛前介绍 b", "presentazione = Vorschau, b"),
    ("spalti=看台 a", "spalti = Tribünen, a"),
    ("sera=晚上 d", "sera = Abend, d"),
    ("用括号里词的比较级填空（数据看赛程表）。",
     "Ergänzen Sie mit dem Komparativ des Wortes in Klammern (siehe Spielplan)."),
    ("周日晚上的比赛晚于周五的：più tardi", "Sonntagabendspiele sind später als die vom Freitag: più tardi"),
    ("周五的比赛早于周日的：più presto", "Freitagsspiele sind früher als die vom Sonntag: più presto"),
    ("più + bella 周日晚最美（主观评价）", "più + bella: der Sonntagabend ist am schönsten (subjektiv)"),
    ("bene 的比较级是不规则的 meglio", "Der Komparativ von bene ist unregelmäßig: meglio"),
    ("用 passato prossimo 补全。", "Ergänzen Sie mit dem passato prossimo."),
    ("vincere：ha vinto", "vincere: ha vinto"),
    ("pareggiare：ha pareggiato", "pareggiare: ha pareggiato"),
    ("arrivare 用 essere，复数 sono arrivati", "arrivare mit essere, Plural: sono arrivati"),
    ("guardare 用 avere：abbiamo guardato", "guardare mit avere: abbiamo guardato"),
    ("prendere 的分词是 preso：ha preso", "Das Partizip von prendere ist preso: ha preso"),
])
print("content34 done")

# ================= content56 (P5 + P6) =================
pairs("content56.py", [
    ("GIOVANI · 青年", "GIOVANI · JUNGE LEUTE"),
    ("LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · 卢卡之后",
     "LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · Nach Lucca"),
    ("（周二：米兰文化论坛开幕）", "(Dienstag: Forum Cultura eröffnet in Mailand)"),
    ("（周三至周四：欧战直播）", "(Mittwoch–Donnerstag: Europapokal im TV)"),
    ("（周五准备周末）", "(Freitag: Wochenende vorbereiten)"),
    ("（周六：米兰或克雷莫纳品尝）", "(Samstag: Kostproben in Mailand oder Cremona)"),
    ("（周日：意甲与返程）", "(Sonntag: Serie A und Heimreise)"),
    ("il cosplay 角色扮演服装 · gratuito 免费的 · il documentario 纪录片 · lo schermo 银幕。",
     "il cosplay = Cosplay-Kostüm · gratuito = kostenlos · il documentario = Dokumentarfilm · lo schermo = Leinwand"),
    ("卢卡之后你去哪：文化论坛、电影还是美食节？写两句寄来。",
     "Nach Lucca: Forum Cultura, Kino oder Sagre? Schreiben Sie zwei Sätze!"),
    ("ESERCIZI · 第 5 版练习", "ESERCIZI · ÜBUNGEN ZU SEITE 5"),
    ("读第 5 版文章，选出正确答案。", "Lesen Sie den Artikel auf Seite 5 und wählen Sie die richtige Antwort."),
    ("卢卡漫画节是第 60 届", "Lucca Comics ist die 60. Ausgabe"),
    ("文化论坛 11 月 3 日开幕", "Das Forum Cultura eröffnet am 3. November"),
    ("民俗电影节在佛罗伦萨", "Das Festival dei Popoli ist in Florenz"),
    ("文化论坛有 50 多场活动", "Das Forum Cultura hat über 50 Veranstaltungen"),
    ("卢卡漫画节主题是 Legacy", "Das Thema von Lucca Comics ist «Legacy»"),
    ("用方框里的词填空。注意：有的词要变成复数。",
     "Ergänzen Sie die Wörter aus dem Kasten. Achtung: Manche Wörter stehen im Plural."),
    ("armadio = 衣柜", "armadio = Schrank"),
    ("gratuiti = 免费的（阳性复数）", "gratuiti = kostenlos (maskulin, Plural)"),
    ("documentario = 纪录片", "documentario = Dokumentarfilm"),
    ("schermo = 银幕", "schermo = Leinwand"),
    ("castagne arrosto 烤栗子（复数）", "castagne arrosto = geröstete Kastanien (Plural)"),
    ("cosplay = 角色扮演服装", "cosplay = Cosplay-Kostüm"),
    ("用将来时（futuro semplice）补全。", "Ergänzen Sie mit dem Futuro (futuro semplice)."),
    ("andare 将来时 noi：andremo", "andare, Futur, noi: andremo"),
    ("esserci 将来时：ci sarà（将有）", "esserci, Futur: ci sarà (es wird geben)"),
    ("guardare 将来时 noi：guarderemo", "guardare, Futur, noi: guarderemo"),
    ("durare 将来时：durerà", "durare, Futur: durerà"),
    ("卢卡漫画节到 11 月 8 日才结束是错的", "Lucca Comics endet nicht am 8. November"),
    # P6
    ("APPROFONDIMENTO · 深读", "APPROFONDIMENTO · VERTIEFUNG"),
    ("LIVELLO B2 · Leggere le previsioni · 怎样读天气预报",
     "LIVELLO B2 · Leggere le previsioni · Wettervorhersagen lesen"),
    ("发稿时 10 月 28 日表决结果尚未确认：本期只写预期日期、争议点和 DPB 数字，不写结果。",
     "Bei Redaktionsschluss war das Ergebnis der Abstimmung vom 28. Oktober noch nicht bestätigt: Diese Ausgabe nennt nur das erwartete Datum, den Streitpunkt und die DPB-Zahlen, kein Ergebnis."),
    ("la probabilità 概率 · la media 平均值 · il modello 模型/预报模式 · il bollettino 公报/预报 · aggiornare 更新。",
     "la probabilità = Wahrscheinlichkeit · la media = Durchschnitt · il modello = Vorhersagemodell · il bollettino = Wetterbericht · aggiornare = aktualisieren"),
    ("LE MINIME DI ESEMPIO · 练习用示例最低温 (DATI INVENTATI PER L'ESERCIZIO)",
     "LE MINIME DI ESEMPIO · BEISPIEL-TIEFSTWERTE (DATI INVENTATI PER L'ESERCIZIO)"),
    ("PROBABILITÀ · 概率", "PROBABILITÀ · WAHRSCHEINLICHKEIT"),
    ("ESERCIZI · 第 6 版练习", "ESERCIZI · ÜBUNGEN ZU SEITE 6"),
    ("看上面的练习图表，选出正确答案。", "Sehen Sie sich das Übungsdiagramm oben an und wählen Sie die richtige Antwort."),
    ("示例数据中最冷的是都灵 3°", "In den Beispieldaten ist Turin mit 3° am kältesten"),
    ("示例数据中最暖的是那不勒斯 12°", "In den Beispieldaten ist Neapel mit 12° am wärmsten"),
    ("图表数据是练习用的、不是真实预报", "Die Diagrammdaten sind zum Üben, keine echten Vorhersagen"),
    ("高概率不等于确定", "Hohe Wahrscheinlichkeit ist keine Gewissheit"),
    ("预报基于 ECMWF 等模型", "Vorhersagen beruhen auf Modellen wie dem ECMWF"),
    ("预报会变，因为大气变化快", "Vorhersagen ändern sich, weil sich die Atmosphäre schnell ändert"),
    ("DPB 于 10 月 15 日送布鲁塞尔", "Der DPB wurde am 15. Oktober nach Brüssel geschickt"),
    ("2027 增长预测 +0,8%", "Wachstumsprognose 2027: +0,8 %"),
    ("è probabile che + 虚拟式 piova", "è probabile che + Konjunktiv: piova"),
    ("è possibile che + 虚拟式 nevichi", "è possibile che + Konjunktiv: nevichi"),
    ("bisogna che + 虚拟式 controllino", "bisogna che + Konjunktiv: controllino"),
    ("è importante che + 虚拟式 sia", "è importante che + Konjunktiv: sia"),
    ("用方框里的词填空：probabilità · media · bollettino · modello",
     "Ergänzen Sie die Wörter aus dem Kasten: probabilità · media · bollettino · modello"),
    ("probabilità = 概率", "probabilità = Wahrscheinlichkeit"),
    ("media = 平均值", "media = Durchschnitt"),
    ("bollettino = 预报公报", "bollettino = Wetterbericht"),
    ("modello = 预报模型", "modello = Vorhersagemodell"),
])
print("content56 done")

# ================= content7 (P7) =================
# NOTE: wt (the Italian definition sentence of LA PAROLA) is NOT in this
# list on purpose: it stays byte-identical. Only its German gloss note
# below is localised.
pairs("content7.py", [
    ("LINGUA · 语言", "LINGUA · SPRACHE"),
    ("聚焦语言 · Tre livelli, tre strumenti · 三个级别，三件工具",
     "Sprache im Fokus · Tre livelli, tre strumenti · Drei Stufen, drei Werkzeuge"),
    ("天气用无人称动词（第三人称单数）；“我冷”说 ho freddo，“外面冷”说 fa freddo。",
     "Wetter mit unpersönlichen Verben (3. Person Singular): „Mir ist kalt“ heißt ho freddo, „draußen ist es kalt“ heißt fa freddo."),
    ("piovere 天气动词：piove", "piovere, Wetterverb: piove"),
    ("fa freddo = 天气冷", "fa freddo = es ist kalt (Wetter)"),
    ("nevicare：nevica", "nevicare: nevica"),
    ("“我冷”说 ho freddo", "„Mir ist kalt“ heißt ho freddo"),
    ("讲过去用近过去时：arrivare/andare 等用 essere，分词配合性数；avere 的分词不变。",
     "Vergangenheit mit dem passato prossimo: arrivare/andare u. a. mit essere, Partizip passt sich in Genus und Numerus an; mit avere bleibt das Partizip unverändert."),
    ("arrivare 用 essere：è arrivato", "arrivare mit essere: è arrivato"),
    ("assaggiare 用 avere", "assaggiare mit avere"),
    ("andare 用 essere，复数 sono andati", "andare mit essere, Plural: sono andati"),
    ("aprire 用 avere + 不变分词", "aprire mit avere + unverändertes Partizip"),
    ("è probabile che / è possibile che / bisogna che 后用虚拟式；so che、scrivono che 后用陈述式。",
     "Nach è probabile che / è possibile che / bisogna che steht der Konjunktiv; nach so che / scrivono che steht der Indikativ."),
    ("è probabile che + 虚拟式 piova", "è probabile che + Konjunktiv: piova"),
    ("è possibile che + 虚拟式 nevichi", "è possibile che + Konjunktiv: nevichi"),
    ("bisogna che + 虚拟式 sia", "bisogna che + Konjunktiv: sia"),
    ("so che + 陈述式 arriva", "so che + Indikativ: arriva"),
    ("ERRORI TIPICI · 常见错误", "ERRORI TIPICI · TYPISCHE FEHLER"),
    ("fa 后面的 freddo 永远不变。", "Nach fa bleibt freddo unverändert."),
    ("nevicare 只用第三人称单数。", "nevicare: nur 3. Person Singular."),
    ("预报给的是概率，不是确定性。", "Wahrscheinlichkeit, keine Gewissheit."),
    ("gente 是单数，动词形容词用单数阴性。", "gente ist Singular (feminin)."),
    ("LA PAROLA · 本周生词", "LA PAROLA · DAS WORT DER WOCHE"),
    ("assaggio = 品尝。本周见第 3 版：潘妮托尼决赛上观众可以免费品尝。",
     "assaggio = Kostprobe. Seite 3: gratis kosten beim Panettone-Finale."),
    # readers' corner: Italian letter text (lt) untouched; German note covers
    # all three disclosure facts + imperative invitation with VOL.3 promise.
    # Line-counted (3 lines at 20pt, same as the Chinese note) so col3 still
    # ends at the core's 1673, 13 px clear of the FRASI rule.
    ("这是编辑部示例信，非真实来信。来信请寄编辑部，VOL.3 刊登真实来信与第 8 版最佳作文！",
     "Redaktionsbeispiel, keine Leserpost, kein bester Seite-8-Text. Schreiben Sie uns — die besten erscheinen in VOL.3!"),
    ("FRASI DELLA SETTIMANA · 本周金句（逐字摘自本期文章）",
     "FRASI DELLA SETTIMANA · SÄTZE DER WOCHE (wörtlich aus dieser Ausgabe)"),
    ("第一场真正的寒冷到来了。", "Die erste wirkliche Kälte der Saison ist da."),
    ("这不是确定性，而是概率。", "Das ist keine Gewissheit, sondern eine Wahrscheinlichkeit."),
    ("11 月 2 日是追思日。", "Der 2. November ist Allerseelen."),
    ("天冷，穿暖和点！", "Es ist kalt, zieh dich warm an!"),
    ("观众可以免费品尝。", "Das Publikum darf gratis kosten."),
    ("足球不会因为第一场寒冷而停下。", "Der Fußball stoppt nicht wegen der ersten Kälte."),
    ("文化继续。", "Die Kultur geht weiter."),
    ("高概率不等于确定性。", "Eine hohe Wahrscheinlichkeit ist keine Gewissheit."),
    ("LA PROSSIMA SETTIMANA · 下期预告 (VOL.3)", "LA PROSSIMA SETTIMANA · NÄCHSTE WOCHE (VOL.3)"),
])
print("content7 done")

# ================= content8 (P8) =================
pairs("content8.py", [
    ("VALUTAZIONE E RISPOSTE · 练习与答案", "VALUTAZIONE E RISPOSTE · TEST UND LÖSUNGEN"),
    ("第 8 版 · La grande prova della settimana + tutte le risposte",
     "Seite 8 · La grande prova della settimana + tutte le risposte"),
    ("primo freddo = 第一场寒冷", "primo freddo = die erste Kälte"),
    ("追思日在 11 月 2 日", "Allerseelen ist am 2. November"),
    ("文化论坛在米兰开幕", "Das Forum Cultura eröffnet in Mailand"),
    ("潘妮托尼决赛在周六日", "Das Panettone-Finale ist am Samstag und Sonntag"),
    ("牛轧糖节在克雷莫纳", "Das Torrone-Fest ist in Cremona"),
    ("意甲第 11 轮周日收官：chiude", "Der 11. Spieltag endet am Sonntag: chiude"),
    ("佛罗伦萨对尤文图斯在周日晚上", "Fiorentina gegen Juventus am Sonntagabend"),
    ("民俗电影节在佛罗伦萨", "Das Festival dei Popoli ist in Florenz"),
    ("初雪在 1300–1500 米左右", "Der erste Schnee fällt um 1.300–1.500 Meter"),
    ("追思日的花是菊花", "Die Blume des 2. November ist die Chrysantheme"),
    ("潘妮托尼决赛有 19 国糕点师", "Am Panettone-Finale nehmen Konditoren aus 19 Ländern teil"),
    ("文化论坛有 50 多场活动", "Das Forum Cultura hat über 50 Veranstaltungen"),
    ("阿尔巴松露节到 12 月 6 日", "Das Trüffelfest in Alba geht bis zum 6. Dezember"),
    ("DPB 于 10 月 15 日送出", "Der DPB wurde am 15. Oktober geschickt"),
    ("概率不等于确定", "Wahrscheinlichkeit ist keine Gewissheit"),
    ("卢卡漫画节 11 月 1 日闭幕", "Lucca Comics endet am 1. November"),
    ("Giulia 去米兰潘妮托尼决赛", "Giulia fährt zum Panettone-Finale in Mailand"),
    ("Paolo 周六去牛轧糖节", "Paolo fährt am Samstag zum Torrone-Fest"),
    ("传统潘妮托尼是 Giulia 品尝的", "Den traditionellen Panettone kostet Giulia"),
    ("标题概括两个城市、两个节日", "Der Titel fasst zwei Städte und zwei Feste zusammen"),
    ("时间词在前", "Zeitangabe zuerst"),
    ("主语 + essere + 地点 + 日期", "Subjekt + essere + Ort + Datum"),
    ("疑问词组在句首", "Frageformel am Anfang"),
    ("主语 + 动词 + 时间", "Subjekt + Verb + Zeitangabe"),
    # E · translation items re-aimed Italian -> German (W43 precedent):
    # Chinese keys become German keys; the one Italian-key item keeps its
    # Italian key and its body becomes German.
    ("周一第一场寒冷来了。", "Am Montag kommt die erste Kälte."),
    ("对照原文", "Vgl. den Originaltext"),
    ("观众可以免费品尝。", "Das Publikum darf gratis kosten."),
    ("assaggiare gratis = 免费品尝", "assaggiare gratis = gratis kosten"),
    ("周日晚上，佛罗伦萨对尤文图斯。", "Am Sonntagabend spielt Fiorentina gegen Juventus."),
    ("si gioca = 进行比赛", "si gioca = es wird gespielt"),
    ("dovere = 必须", "dovere = müssen"),
    ("每个预报都必须清楚。→ ___", "Jede Vorhersage muss klar sein. → ___"),
    ("probabilità=可能性 d", "probabilità = Wahrscheinlichkeit, d"),
    ("media=平均值 a", "media = Durchschnitt, a"),
    ("bollettino=预报公报 b", "bollettino = Wetterbericht, b"),
    ("modello=预报模型 c", "modello = Vorhersagemodell, c"),
    ("torrone = 牛轧糖", "torrone = Nougat"),
    ("mandorle 杏仁", "mandorle = Mandeln"),
    ("quanto costa? 多少钱", "quanto costa? = was kostet es?"),
    ("pagare con carta 刷卡", "pagare con carta = mit Karte zahlen"),
    ("牛轧糖节持续到 11 月 22 日", "Das Torrone-Fest geht bis zum 22. November"),
    ("写作题（无唯一答案）；范文（{NWORDS} 词）见下。",
     "Schreibaufgabe (keine eindeutige Lösung); Mustertext ({NWORDS} Wörter) unten."),
    ("（开放题，范文如下）", "(offene Aufgabe, Mustertext unten)"),
    ("范文见本版 H 区（{NWORDS} 词）", "Mustertext in Abschnitt H auf dieser Seite ({NWORDS} Wörter)"),
    ("RISPOSTE · 参考答案 — 按版面分页排列，找到题号即可",
     "RISPOSTE · LÖSUNGEN — nach Seiten geordnet, suchen Sie die Nummer"),
    ("每题附一句中文简析 · 带 ✓ 的为范文题", "Zu jeder Aufgabe ein kurzer Hinweis · ✓ = Schreibaufgabe"),
])
print("content8 done")

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

# ================= FIX ROUND 1 (from R0 render) =================
# R0 defects: (a) P1 headline flow overflowed: the German bridge gloss ran
# 4 lines (core 3), pushing the cifre box from col 1 to col 2, so exercises
# 5-6 clamped at the bottom. Fix: bridge back to 3 lines + cifre item 4
# back to 2 lines, so the box fits col 1 again (wording only, no layout
# change). (b) P8 answer flow overflowed the footer zone by ~5 key lines:
# 13 German notes wrapped to 2 lines. Fix: shorten 9 notes to 1 line each
# (wording only); keys 44/134, 138, 139 stay 2-line, flow then fits.
def rep2(fname, old, new):
    p = os.path.join(BASE, fname)
    s = open(p, encoding="utf-8").read()
    n = s.count(old)
    assert n >= 1, f"FIX1 {fname}: {old!r} not found"
    open(p, "w", encoding="utf-8").write(s.replace(old, new))
    print(f"FIX1 {fname}: {n}x {old!r} -> {new!r}")


rep2("content12.py",
     "HINWEIS · il primo freddo = die erste Kälte · il versante adriatico = die Adriaseite · la previsione = die Vorhersage · assaggi = Kostproben.",
     "HINWEIS · il primo freddo = erste Kälte · versante adriatico = Adriaseite · previsione = Vorhersage · assaggi = Kostproben.")
rep2("content12.py",
     "(11. Spieltag der Serie A am Wochenende)",
     "(11. Serie-A-Spieltag)")
rep2("content12.py",
     "Forum Cultura und Panettone-Finale sind beide in Mailand",
     "Forum Cultura und Panettone-Finale in Mailand")
rep2("content12.py",
     "Allerheiligen fällt dieses Jahr auf einen Sonntag, ohne Brückentag",
     "Allerheiligen: dieses Jahr Sonntag, ohne Brückentag")
rep2("content34.py",
     "Am Panettone-Finale nehmen Konditoren aus 19 Ländern teil",
     "Panettone-Finale: Konditoren aus 19 Ländern")
rep2("content8.py",
     "Am Panettone-Finale nehmen Konditoren aus 19 Ländern teil",
     "Panettone-Finale: Konditoren aus 19 Ländern")
rep2("content34.py",
     "Sonntagabendspiele sind später als die vom Freitag: più tardi",
     "Sonntagabend später als Freitag: più tardi")
rep2("content34.py",
     "Freitagsspiele sind früher als die vom Sonntag: più presto",
     "Freitag früher als Sonntag: più presto")
rep2("content34.py",
     "più + bella: der Sonntagabend ist am schönsten (subjektiv)",
     "più + bella: Sonntagabend am schönsten (subjektiv)")
rep2("content56.py",
     "Die Diagrammdaten sind zum Üben, keine echten Vorhersagen",
     "Diagrammdaten: zum Üben, keine echten Vorhersagen")
rep2("content56.py",
     "Vorhersagen ändern sich, weil sich die Atmosphäre schnell ändert",
     "Vorhersagen ändern sich: Atmosphäre ändert sich schnell")
print("FIX ROUND 1 done")

# ================= FIX ROUND 2 (from R1 occlusion audit: 6 NEW flags) =================
# All six are real German-note overflows (audit exit 1, core 0): (a) P1
# settimana footnote ran off the page as one 662 px line (core Chinese fit
# 390 px) -> split into two short lines inside the box (box bottom 1280,
# second line ink ~1257, sommario at 1312 untouched); (b) P1 parola note
# wrapped to 2 lines and the row-B rule at 1864 cut line 2 -> 1 line;
# (c) P1 settimana subtitle crossed its box border -> shorter Italian tail;
# (d) P2 frase box title crossed its box border -> MERKE; (e) P7 parola box
# title crossed its box border by 5.5 px -> drop DAS. Wording only, except
# (a) which adds one p.text line inside the existing box.
rep2("content12.py",
     'p.text(gx + 22, byy + 76, "Die Termine folgen den Kalendern der Veranstaltungen; Uhrzeiten können sich ändern.", 16.5, "sans", False, GREY)',
     'p.text(gx + 22, byy + 76, "Termine nach Veranstaltungskalendern;", 16.5, "sans", False, GREY)\n'
     'p.text(gx + 22, byy + 102, "Zeiten können sich ändern.", 16.5, "sans", False, GREY)')
rep2("content12.py",
     "Der Wochenplan · Cosa succede, giorno per giorno",
     "Der Wochenplan · Giorno per giorno")
rep2("content12.py",
     "„il primo freddo“: die erste ernsthafte Kälte nach einem milden Herbst.",
     "„il primo freddo“: Kälte nach mildem Herbst.")
rep2("content12.py",
     "LA FRASE PER RICORDARE · MERKSATZ",
     "LA FRASE PER RICORDARE · MERKE")
rep2("content7.py",
     "LA PAROLA · DAS WORT DER WOCHE",
     "LA PAROLA · WORT DER WOCHE")
print("FIX ROUND 2 done")
