# -*- coding: utf-8 -*-
"""DE x IT fan-out transform for W46 DE core build copy.
Generated from the EN pair table + tr-it.py. German body text is
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
    rep(f, "weekly-report-w46-de-core", "weekly-report-w46-de-it", 1)

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
    '"Die Lucerna · SETTIMANALE TEDESCO VOL.3 · TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO"', 1)
rep("bslib4.py", 'f"\u7b2c {n} \u7248 / \u5171 {total} \u7248"', 'f"Pagina {n} di {total}"', 1)
rep("bslib4.py", '"\u8bd1\u6ce8\uff5c" + s', '"Nota — " + s', 1)

# ================= content12.py =================
C12 = [
    ('WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语', 'WÖCHENTLICH AUF DEUTSCH · OGNI SETTIMANA · IL TEDESCO CHE LEGGONO I TEDESCHI'),
    ('德 语 周 报 · VOL.3 · 国 家 队 · 圣 马 丁 · NFL', 'SETTIMANALE TEDESCO · VOL.3 · NAZIONALE · SAN MARTINO · NFL'),
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")', 'p.text(975, 372, "TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO — L\'EDIZIONE PER I LETTORI ITALIANI", 20, "sans", True, BRICK, anchor="middle")'),
    ('本周国家队周 · 圣马丁节与 NFL', 'SETTIMANA DELLA NAZIONALE · SAN MARTINO E NFL'),
    ('详见第 4 版 · Seite 4', 'Vedi pagina 4'),
    ('DIE TOPMELDUNG · 头条', 'DIE TOPMELDUNG · Titolo'),
    ('讲解｜die Länderspielpause 国家队比赛间歇期 · das Viertelfinale 四分之一决赛 · ausverkauft 售罄。', 'Note — die Länderspielpause = sosta per le nazionali · das Viertelfinale = quarti di finale · ausverkauft = esaurito.'),
    ('DIE WOCHE IN ZAHLEN · 数字看本周', 'DIE WOCHE IN ZAHLEN · In numeri'),
    ('5 — Punkte hat Deutschland nach vier Spielen in der Nations League（四轮过后德国队 5 分）', '5 — Punkte hat Deutschland nach vier Spielen in der Nations League (la Germania ha 5 punti dopo quattro partite)'),
    ('11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（11 点 11 分狂欢季开幕）', '11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln (la sessione di carnevale inizia alle 11.11)'),
    ('15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（周日 15 点 30 分 NFL 开球）', '15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München (la partita NFL inizia domenica alle 15.30)'),
    ('JETZT ÜBEN · 即学即练', 'JETZT ÜBEN · Ora tocca a te'),
    ('国家队比赛周', 'settimana di sosta per le nazionali'),
    ('塞尔维亚首都', 'capitale della Serbia'),
    ('狂欢季 11 点 11 分开幕', 'il carnevale inizia alle 11.11'),
    ('NFL 在慕尼黑', 'la NFL a Monaco'),
    ('四轮 5 分', '5 punti dopo quattro partite'),
    ('周日是纪念日', 'domenica è il giorno del ricordo'),
    ('圣马丁节 11 月 11 日', "San Martino è l'11 novembre"),
    ('11 月 11 日是星期三', "l'11 novembre è mercoledì"),
    ('本周大问题 · Die Fragen der Woche', 'Grandi domande · Die Fragen der Woche'),
    ('德国本周最热议的五个问题。', 'Le cinque domande che agitano la Germania.'),
    ('IN DIESER AUSGABE · 本期目录', 'IN DIESER AUSGABE · Sommario'),
    ('空场比赛（无观众）。详见第 4 版。', 'Una partita senza spettatori. Vedi pagina 4.'),
    ('KURZ & GUT · 快讯', 'KURZ & GUT · In breve'),
    ('BLITZQUIZ · 闪电问答', 'BLITZQUIZ · Quiz lampo'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Leggi la prima pagina e scegli la risposta giusta · Risposte a pagina 8'),
    ('周五客战塞尔维亚', 'in trasferta in Serbia venerdì'),
    ('NFL 下午 3 点半开球', 'la NFL inizia alle 15.30'),
    ('纪念日在周日', 'il giorno del ricordo è domenica'),
    ('LEBEN · 生活', 'LEBEN · La vita'),
    ('LEVEL A2 · Der 11. November & der Alltag · 11 月 11 日与日常生活', "LEVEL A2 · Der 11. November & der Alltag · L'11 novembre e la vita quotidiana"),
    ('der Jeck 狂欢者（科隆方言） · die fünfte Jahreszeit 第五个季节（狂欢季） · die Laterne 灯笼 · der Weckmann 面人面包 · die Martinsgans 圣马丁鹅。', 'der Jeck = festaiolo del carnevale (dialetto di Colonia) · die fünfte Jahreszeit = la quinta stagione (carnevale) · die Laterne = lanterna · der Weckmann = omino di pane · die Martinsgans = oca di San Martino.'),
    ('DER 11. NOVEMBER · 11 月 11 日', 'DER 11. NOVEMBER'),
    ('你过狂欢节还是圣马丁节？写两句德语寄来。', 'Carnevale o San Martino? Scrivi due frasi in tedesco!'),
    ('UND SIE? · 说说你自己', 'UND SIE? · E tu?'),
    ('MARTIN IN KÜRZE · 圣马丁简讯', 'MARTIN IN KÜRZE · In breve'),
    ('RECHNEN WIR MAL · 算一算', 'RECHNEN WIR MAL · Calcoliamo'),
    ('Die Uhrzeiten der Woche · 本周时刻', 'Die Uhrzeiten der Woche · Gli orari della settimana'),
    ('注意：11 月 11 日是工作日。去科隆要早到：老城很挤，晚上街道属于提灯笼的孩子们。', "Nota: l'11 novembre è lavorativo. Arriva presto a Colonia: il centro storico è affollato e la sera le strade sono dei bambini con le loro lanterne."),
    ('ÜBUNGEN · 第 2 版练习', 'ÜBUNGEN · Esercizi pagina 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Risposte a pagina 8 · I livelli si mescolano: trova ogni risposta dal suo numero'),
    ('看第 2 版文章，用时间填空。', "Leggi l'articolo di pagina 2 e completa gli orari."),
    ('WDR 10 点半直播', 'la WDR in diretta dalle 10.30'),
    ('Weckmann 是面人面包', 'un Weckmann è un omino di pane'),
    ('11 月 11 日不是法定假日', "l'11 novembre non è festivo"),
    ('圣马丁鹅配红甘蓝和丸子', "l'oca di San Martino con cavolo rosso e canederli"),
    ('改成 Perfekt 现在完成时。', 'Riscrivi al Perfekt (passato prossimo).'),
    ('读第 2 版文章，选出正确答案。', "Leggi l'articolo di pagina 2 e scegli la risposta giusta."),
    ('Jeck=狂欢者 c', 'Jeck=festaiolo del carnevale c'),
    ('Laterne=灯笼 a', 'Laterne=lanterna a'),
    ('Weckmann=面人面包 b', 'Weckmann=omino di pane b'),
    ('Martinsgans=圣马丁鹅 d', 'Martinsgans=oca di San Martino d'),
]
rep_all("content12.py", C12)

# ================= content34.py =================
C34 = [
    ('KULTUR · 文化', 'KULTUR · Cultura'),
    ('A2 → B1 · St. Martin, Karneval & Rückblick · 圣马丁、狂欢节与回顾', 'A2 → B1 · St. Martin, Karneval & Rückblick · San Martino, carnevale e uno sguardo indietro'),
    ('der Bettler 乞丐 · der Mantel 斗篷 · das Geschnatter 鹅叫声 · der Gänsestall 鹅棚 · das Dreigestirn 狂欢节三人组。', 'der Bettler = mendicante · der Mantel = mantello · das Geschnatter = starnazzare · der Gänsestall = stalla delle oche · das Dreigestirn = triumvirato del carnevale.'),
    ('ST. MARTIN · 圣马丁', 'ST. MARTIN · San Martino'),
    ('die Laterne — 灯笼', 'die Laterne — lanterna'),
    ('der Mantel — 斗篷', 'der Mantel — mantello'),
    ('die Gans — 鹅', 'die Gans — oca'),
    ('der Weckmann — 面人面包', 'der Weckmann — omino di pane'),
    ('das Martinsfeuer — 圣马丁篝火', 'das Martinsfeuer — falò di San Martino'),
    ('das Kostüm — 服装', 'das Kostüm — costume'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · San Martino'),
    ('UND SIE? · 说说你自己', 'UND SIE? · E tu?'),
    ('你做过灯笼吗？你们国家的孩子唱什么歌？写两句德语寄来。', 'Hai fatto una lanterna? Scrivi due frasi in tedesco!'),
    ('DER TIPP · 编辑部建议', 'DER TIPP · Consiglio'),
    ('ÜBUNGEN · 第 3 版练习', 'ÜBUNGEN · Esercizi pagina 3'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Risposte a pagina 8 · I livelli si mescolano: trova ogni risposta dal suo numero'),
    ('读第 3 版文章，判断对错。', "Leggi l'articolo di pagina 3. Vero o falso?"),
    ('传说马丁是罗马士兵', 'la leggenda dice che Martino era un soldato romano'),
    ('传说鹅叫声暴露了他', 'la leggenda dice che le oche lo tradirono'),
    ('纪念日 11 月 11 日', "il giorno del ricordo è l'11 novembre"),
    ('截稿时 11 月 3–8 日结果未知', "risultati dal 3 all'8 novembre sconosciuti alla chiusura"),
    ('狂欢季 11 点 11 分开幕', 'il carnevale inizia alle 11.11'),
    ('用方框里的词填空。', 'Completa con le parole del riquadro.'),
    ('斗篷分给乞丐', 'il mantello condiviso con il mendicante'),
    ('纸灯笼', 'una lanterna di carta'),
    ('圣马丁鹅', "l'oca di San Martino"),
    ('圣马丁鹅配红甘蓝和丸子', "l'oca di San Martino con cavolo rosso e canederli"),
    ('狂欢节服装', 'un costume di carnevale'),
    ('游行在篝火处结束', 'la processione finisce al falò'),
    ('选出正确答案。', 'Scegli la risposta giusta.'),
    ('马丁后来成为图尔主教', 'Martino divenne poi vescovo di Tours'),
    ('灯笼游行常在前后晚上举行', 'le processioni con le lanterne sono spesso nelle sere vicine'),
    ('VOL.4 报道 11 月 3–8 日结果', "VOL.4 racconterà i risultati dal 3 all'8 novembre"),
    ('把词组成正确的句子。', 'Metti le parole in una frase corretta.'),
    ('主谓宾顺序', 'ordine soggetto–verbo–oggetto'),
    ('时间状语开头，动词第二位', 'il tempo prima, il verbo al secondo posto'),
    ('地点开头，动词第二位', 'il luogo prima, il verbo al secondo posto'),
    ('SPORT · 体育', 'SPORT · Sport'),
    ('LEVEL B1 · Nationalelf & NFL · 国家队与 NFL', 'LEVEL B1 · Nationalelf & NFL · Nazionale e NFL'),
    ('das Geisterspiel 空场比赛 · das Hinspiel 首回合 · ausverkauft 售罄 · der Star 明星 · gewinnen 获胜。', 'das Geisterspiel = partita fantasma · das Hinspiel = partita di andata · ausverkauft = esaurito · der Star = stella · gewinnen = vincere.'),
    ('你更爱看足球还是美式橄榄球？贝尔格莱德谁赢？写两句德语寄来。', 'Calcio o football americano? Chi vince? Due frasi!'),
    ('DER SPIELPLAN · 本周与下周赛程', 'DER SPIELPLAN · Questa settimana e la prossima'),
    ('ÜBUNGEN · 第 4 版练习', 'ÜBUNGEN · Esercizi pagina 4'),
    ('读第 4 版文章，选出正确答案。', "Leggi l'articolo di pagina 4 e scegli la risposta giusta."),
    ('德国 5 分，荷兰希腊各 8 分', 'Germania 5 punti, Olanda e Grecia 8 a testa'),
    ('主教练 11 月 5 日公布名单', 'il ct annuncia la lista il 5 novembre'),
    ('贝尔格莱德空场', 'stadio vuoto a Belgrado'),
    ('首回合德国 2:0 胜塞尔维亚', "la Germania ha vinto l'andata 2-0 contro la Serbia"),
    ('NFL 慕尼黑赛售罄', 'la partita NFL di Monaco è esaurita'),
    ('Geisterspiel=空场比赛 b', 'Geisterspiel=partita fantasma b'),
    ('Hinspiel=首回合 a', 'Hinspiel=partita di andata a'),
    ('Ausrüster=装备赞助商 c', 'Ausrüster=fornitore tecnico c'),
    ('ausverkauft=售罄 d', 'ausverkauft=esaurito d'),
    ('用比较级完成句子（括号里是原级）。', 'Completa con il comparativo (la parola tra parentesi è al positivo).'),
    ('viel → mehr（荷兰 8 分多于德国 5 分）', "viel → mehr (l'Olanda ha 8 punti, più dei 5 della Germania)"),
    ('spät → später（15:30 晚于 11:11）', 'spät → später (le 15.30 è più tardi delle 11.11)'),
    ('leise → leiser（空场比主场安静）', 'leise → leiser (uno stadio vuoto è più silenzioso di una partita in casa)'),
    ('früh → früher（11 月 5 日早于 11 月 13 日）', 'früh → früher (il 5 novembre è prima del 13 novembre)'),
    ('看上面的赛程表，选出正确答案。', 'Guarda il calendario qui sopra e scegli la risposta giusta.'),
    ('塞尔维亚–德国周五 20:45', 'Serbia–Germania venerdì alle 20.45'),
    ('NFL 周日 15:30', 'NFL domenica alle 15.30'),
    ('德国–荷兰周一 20:45', 'Germania–Olanda lunedì alle 20.45'),
    ('拜仁–科隆周五 20:30', 'Bayern–Colonia venerdì alle 20.30'),
    ('沙尔克–斯图加特周六 17:30', 'Schalke–Stoccarda sabato alle 17.30'),
]
rep_all("content34.py", C34)

# ================= content56.py =================
C56 = [
    ('JUGEND · 青年', 'JUGEND · Giovani'),
    ('LEVEL B1 · Laternen, Lieder & Schule · 灯笼、歌曲与学校', 'LEVEL B1 · Laternen, Lieder & Schule · Lanterne, canzoni e scuola'),
    ('basteln 制作 · der Pausenhof 课间操场 · sich verkleiden 乔装打扮 · die Stimmung 气氛 · der Pirat 海盗。', 'basteln = costruire · der Pausenhof = cortile · sich verkleiden = travestirsi · die Stimmung = atmosfera · der Pirat = pirata.'),
    ('SCHULWOCHE · 开学周', 'SCHULWOCHE · A scuola'),
    ('die Laterne — 灯笼', 'die Laterne — lanterna'),
    ('basteln — 制作', 'basteln — costruire'),
    ('das Lied — 歌曲', 'das Lied — canzone'),
    ('das Kostüm — 服装', 'das Kostüm — costume'),
    ('der Umzug — 游行', 'der Umzug — corteo'),
    ('der Stern — 星星', 'der Stern — stella'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · San Martino'),
    ('UND SIE? · 说说你自己', 'UND SIE? · E tu?'),
    ('你小时候做过灯笼吗？11 月你唱哪首歌？写两句德语寄来。', 'Una lanterna da bambino? La tua canzone? Due frasi!'),
    ('DER WOCHENPLAN DER REDAKTION · 编辑部一周计划', 'DER WOCHENPLAN DER REDAKTION · La settimana della redazione'),
    ('ÜBUNGEN · 第 5 版练习', 'ÜBUNGEN · Esercizi pagina 5'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Risposte a pagina 8 · I livelli si mescolano: trova ogni risposta dal suo numero'),
    ('读第 5 版文章，选出正确答案。', "Leggi l'articolo di pagina 5 e scegli la risposta giusta."),
    ('11 月 9 日全德复课', 'la scuola ricomincia ovunque il 9 novembre'),
    ('孩子们做纸灯笼', 'i bambini fanno lanterne di carta'),
    ('纸灯笼', 'una lanterna di carta'),
    ('上午狂欢，下午圣马丁', 'carnevale al mattino, San Martino al pomeriggio'),
    ('NFL 周日在电视上', 'la NFL in TV domenica'),
    ('周五看国家队比赛', 'guardare la nazionale venerdì'),
    ('用方框里的词填空。', 'Completa con le parole del riquadro.'),
    ('做灯笼', 'fare le lanterne'),
    ('唱圣马丁歌曲', 'cantare le canzoni di San Martino'),
    ('狂欢节服装', 'un costume di carnevale'),
    ('灯笼游行', 'un corteo con le lanterne'),
    ('灯笼上的星星', 'la stella sulla lanterna'),
    ('用 weil 连接两个句子（动词放句末）。', 'Unisci le due frasi con weil (il verbo va alla fine).'),
    ('weil 句动词置尾', 'in una subordinata con weil il verbo va alla fine'),
    ('ist 置尾', 'ist va alla fine'),
    ('will 置尾', 'will va alla fine'),
    ('beginnt 置尾', 'beginnt va alla fine'),
    ('判断对错。', 'Vero o falso?'),
    ('11 月 9 日巴伐利亚也复课', 'anche la Baviera torna il 9 novembre'),
    ('灯笼游行在晚上', 'il corteo con le lanterne è la sera'),
    ('孩子们唱圣马丁歌曲', 'i bambini cantano le canzoni di San Martino'),
    ('VERTIEFUNG · 深读', 'VERTIEFUNG · Approfondimento'),
    ('LEVEL B2 · Volkstrauertag & Stromsteuer · 纪念日与电力税', "LEVEL B2 · Volkstrauertag & Stromsteuer · Giorno del ricordo e tassa sull'elettricità"),
    ('gedenken 纪念 · die Kranzniederlegung 献花圈 · der stille Tag 安静日 · die Verbundenheit 联系 · die Versöhnung 和解。', 'gedenken = commemorare · Kranzniederlegung = corona · stille Tag = giorno di silenzio · Verbundenheit = legame · Versöhnung = riconciliazione.'),
    ('DIE ZAHLEN · 本周数字', 'DIE ZAHLEN · I numeri'),
    ('纪念日：纪念需要安静——对此几乎人人赞同。电力税：降多少尚未确定。两者都关系到几乎每个家庭。', "Giorno del ricordo: ricordare chiede silenzio — quasi tutti sono d'accordo. Tassa sull'elettricità: quanto scenderà è ancora aperto. Entrambi riguardano quasi ogni famiglia."),
    ('ZWEI SONNTAGE IM NOVEMBER · 十一月的两个周日', 'ZWEI SONNTAGE IM NOVEMBER · Due domeniche di novembre'),
    ('WAS INTERESSIERT DIE LESER? · 读者最关心什么？', 'WAS INTERESSIERT DIE LESER? · Cosa interessa ai lettori?'),
    ('("Nations League und NFL", 46, "足球")', '("Nations League und NFL", 46, "calcio")'),
    ('("St. Martin und Karneval", 34, "节日")', '("St. Martin und Karneval", 34, "feste")'),
    ('("Volkstrauertag und Gedenken", 20, "纪念")', '("Volkstrauertag und Gedenken", 20, "memoria")'),
    ('ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）', 'ÜBUNGSDATEN · Dati di esercizio — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Dati di esercizio, non un vero sondaggio.)'),
    ('ÜBUNGEN · 第 6 版练习', 'ÜBUNGEN · Esercizi pagina 6'),
    ('看上面的练习图表，选出正确答案。', 'Usa il grafico di esercizio qui sopra.'),
    ('46% 足球最受关注', 'il calcio in testa con il 46%'),
    ('节日 34% 第二', 'le feste seconde con il 34%'),
    ('纪念 20% 最小', 'il ricordo il più piccolo con il 20%'),
    ('纪念 20%', 'il ricordo 20%'),
    ('读第 6 版深读文章，选出正确答案。', "Leggi l'articolo di pagina 6."),
    ('11 月 15 日纪念日', 'il giorno del ricordo è il 15 novembre'),
    ('ZDF 13 点半直播纪念仪式', 'la ZDF in diretta dalle 13.30'),
    ('家庭电力税 2.05 欧分', 'la tassa delle famiglie è di 2,05 centesimi'),
    ('2027 年预算 11 月 27 日表决', 'voto del bilancio 2027 il 27 novembre'),
    ('用括号里的形式填空。', 'Completa con la forma tra parentesi.'),
    ('被动：wird + Partizip II', 'passivo: wird + participio passato'),
    ('ob 引导间接疑问句', 'ob introduce una domanda indiretta'),
    ('献花圈仪式', 'una cerimonia di deposizione di corone'),
    ('为和平与和解', 'per la pace e la riconciliazione'),
    ('德奥联系', 'il legame tedesco-austriaco'),
    ('纪念受害者', 'ricordare le vittime'),
]
rep_all("content56.py", C56)

# ================= content7.py =================
C7 = [
    ('SPRACHE · 语言', 'SPRACHE · La lingua'),
    ('A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所', 'A2 → B2 · Sätze der Woche & Fehlerklinik · Frasi della settimana e clinica degli errori'),
    ('本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。', 'Questa pagina è tutta lingua: tre brevi lezioni, le frasi della settimana (citate parola per parola dagli articoli di questo numero), la clinica degli errori e le lettere dei lettori.'),
    ('BEISPIELE · 例句', 'BEISPIELE · Esempi'),
    ('被动：wird + Partizip II', 'passivo: wird + participio passato'),
    ('复数：werden', 'plurale: werden'),
    ('werden + 原形表将来', 'werden + infinito per il futuro'),
    ('被动语态', 'forma passiva'),
    ('lang → länger（夜晚比白天长）', 'lang → länger (la notte è più lunga del giorno)'),
    ('weil 引导原因', 'weil introduce una causa'),
    ('weil 句动词置尾', 'in una subordinata con weil il verbo va alla fine'),
    ('länger als = 比……更长', 'länger als = più lungo di'),
    ('„Länger als sonst“ heißt... A. 比平时更长 · B. 和平时一样 · C. 比平时更短', '„Länger als sonst“ significa... A. più lungo del solito · B. come al solito · C. più corto del solito'),
    ('ob 引导间接疑问', 'ob introduce una domanda indiretta'),
    ('Es ist fraglich, ob ... = 是否还难说', 'Es ist fraglich, ob ... = è dubbio che ...'),
    ('dass 句动词置尾', 'in una subordinata con dass il verbo va alla fine'),
    ('礼貌表达观点', "un modo gentile di dare un'opinione"),
    ('11.11 Uhr = 11 点 11 分', '11.11 Uhr = 11.11'),
    ('vor leeren Rängen = 空场，没有观众', 'vor leeren Rängen = stadio vuoto'),
    ('Es wird gespielt. = 比赛将进行（被动）', 'Es wird gespielt. = Si giocherà'),
    ('Meiner Meinung nach ... = 在我看来……', 'Meiner Meinung nach = secondo me'),
    ('Ich finde, dass ... = 我觉得……', 'Ich finde, dass = penso che'),
    ('Es ist fraglich, ob ... = 是否……还难说', 'Es ist fraglich, ob ... = è dubbio che'),
    ('DER WERKZEUGKASTEN · 工具箱', 'DER WERKZEUGKASTEN'),
    ('label = "Ein Beispiel der Redaktion!"', 'label = "Un esempio della redazione!"'),
    ('编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.4。请寄来您的习作，优秀者刊登于 VOL.4。', 'Esempio della redazione, non una vera lettera: nessuna vera lettera era arrivata alla chiusura. Mandateci le vostre per VOL.4!'),
    ('LESERBRIEFE · 读者来信', 'LESERBRIEFE · Lettere'),
    ('NOCH EIN WORT · 再学一词', 'NOCH EIN WORT · Ancora una parola'),
    ('«das Geisterspiel»（Seite 4）: ein Spiel ohne Zuschauer im Stadion. 空场比赛。', '«das Geisterspiel» (Seite 4) : ein Spiel ohne Zuschauer im Stadion. Partita fantasma: una partita senza spettatori.'),
    ('SÄTZE DER WOCHE · 本周金句', 'SÄTZE DER WOCHE · Frasi della settimana'),
    ('原文摘录，逐字引自本期文章 · 括号内为出处', 'Citato parola per parola dagli articoli di questo numero · fonte tra parentesi'),
    ('德甲休战——但国家队要比赛。', 'La Bundesliga si ferma — ma gioca la nazionale.'),
    ('11 点 11 分，科隆新一季狂欢季开幕。', 'Alle 11.11 inizia a Colonia la nuova sessione di carnevale.'),
    ('他的纪念日是 11 月 11 日。', "Il suo giorno del ricordo è l'11 novembre."),
    ('书包收拾好了，操场上又热闹起来。', 'Gli zaini sono pronti, i cortili tornano rumorosi.'),
    ('十一月黑暗，但并不安静：它歌唱、发光、庆祝。', 'Novembre è buio, ma non silenzioso: canta, brilla e festeggia.'),
    ('比赛售罄，RTL 现场直播。', 'La partita è esaurita; RTL trasmette in diretta.'),
    ('这里的纪念意味着：停下来、记住——并为和平与和解挺身而出。', 'Qui ricordare significa: fermarsi, ricordare — e difendere la pace e la riconciliazione.'),
    ('周日，全国一片安静。', 'Domenica il paese è silenzioso.'),
    ('FEHLERKLINIK · 纠错诊所', 'FEHLERKLINIK · La clinica degli errori'),
    ('学习者最常犯的四个错 · 先自己改，再看答案', 'Quattro errori frequenti degli studenti · correggili prima, poi controlla'),
    ('动词第二位：主语不在句首时，动词仍居第二。', 'Verbo al secondo posto: anche se il soggetto non è primo, il verbo resta secondo.'),
    ('halb zwölf = 十一点半（zwölf 之前）。', "halb zwölf = 11.30, mezz'ora prima di zwölf."),
    ('Perfekt 中 Partizip II 放句末。', 'Nel Perfekt il participio passato va alla fine.'),
    ('ob 从句动词放句末。', 'In una subordinata con ob il verbo va alla fine.'),
    ('IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.4)', 'IN DER NÄCHSTEN AUSGABE · Prossimo numero (VOL.4)'),
]
rep_all("content7.py", C7)

# ================= content8.py =================
C8 = [
    ('ÜBUNGEN & ANTWORTEN · 练习与答案', 'ÜBUNGEN & ANTWORTEN · Esercizi e risposte'),
    ('SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方', 'SCHLUSSTEST · Test finale · Alle Antworten unten auf dieser Seite — tutte le risposte in fondo a questa pagina'),
    ('beginnt（第三人称单数）', 'beginnt (3ª pers. sing.)'),
    ('bastelt（第三人称单数）', 'bastelt (3ª pers. sing.)'),
    ('geht（第三人称单数）', 'geht (3ª pers. sing.)'),
    ('singt（第三人称单数）', 'singt (3ª pers. sing.)'),
    ('schaut（第三人称单数）', 'schaut (3ª pers. sing.)'),
    ('sieht（第三人称单数）', 'sieht (3ª pers. sing.)'),
    ('erzählt（第三人称单数）', 'erzählt (3ª pers. sing.)'),
    ('A · LÜCKENTEXT · 完形填空', 'A · LÜCKENTEXT · Testo a buchi'),
    ('选项：', 'Opzioni:'),
    ('B · WISSENSFRAGEN · 综合问答', 'B · WISSENSFRAGEN · Quiz'),
    ('狂欢季 11 点 11 分开幕', 'il carnevale inizia alle 11.11'),
    ('周五客战塞尔维亚', 'in trasferta in Serbia venerdì'),
    ('NFL 周日 15:30', 'NFL domenica alle 15.30'),
    ('纪念日 11 月 15 日', 'il giorno del ricordo è il 15 novembre'),
    ('家庭电力税 2.05 欧分', 'la tassa delle famiglie è di 2,05 centesimi'),
    ('主教练 11 月 5 日公布名单', 'il ct annuncia la lista il 5 novembre'),
    ('ZDF 13 点半直播纪念仪式', 'la ZDF in diretta dalle 13.30'),
    ('亡灵主日 11 月 22 日', 'Totensonntag è il 22 novembre'),
    ('C · LESEVERSTEHEN · 阅读理解', 'C · LESEVERSTEHEN · Lettura'),
    ('周三做灯笼', 'fare una lanterna mercoledì'),
    ('周五看德国队', 'guardare la Germania venerdì'),
    ('D · SÄTZE BAUEN · 造句', 'D · SÄTZE BAUEN · Frasi'),
    ('时间状语，动词第二位', 'il tempo, il verbo al secondo posto'),
    ('主谓宾顺序', 'ordine soggetto–verbo–oggetto'),
    ('时间状语开头，动词第二位', 'il tempo prima, il verbo al secondo posto'),
    ('地点时间开头，动词第二位', 'luogo e tempo prima, verbo al secondo posto'),
    ('E · ÜBERSETZEN · 翻译', 'E · ÜBERSETZEN · Traduzione'),
    ('狂欢节 11 点 11 分在科隆开幕。', 'Il carnevale inizia alle 11.11 a Colonia.'),
    ('beginnen = 开始', 'beginnen = iniziare'),
    ('Der Karneval beginnt um 11.11 Uhr in Köln.（译成中文）', 'Der Karneval beginnt um 11.11 Uhr in Köln. (traduci in italiano)'),
    ('我周三做一个灯笼。', 'Faccio una lanterna mercoledì.'),
    ('basteln = 制作', 'basteln = costruire'),
    ('Ich bastle am Mittwoch eine Laterne.（译成中文）', 'Ich bastle am Mittwoch eine Laterne. (traduci in italiano)'),
    ('学校 11 月 9 日又开学了。', 'La scuola è ricominciata il 9 novembre.'),
    ('wieder begonnen = 又开始', 'wieder begonnen = ricominciato'),
    ('Die Schule hat am 9. November wieder begonnen.（译成中文）', 'Die Schule hat am 9. November wieder begonnen. (traduci in italiano)'),
    ('看比赛 = das Spiel schauen', 'guardare una partita = das Spiel schauen'),
    ('"我周日看 NFL 比赛。（译成德语）", instr="翻译"', '"Guardo la partita NFL domenica. (traduci in tedesco)", instr="Traduci in tedesco"'),
    ('F · WÖRTER PAAREN · 词汇配对', 'F · WÖRTER PAAREN · Coppie'),
    ('Mantel=斗篷 b', 'Mantel=mantello b'),
    ('Laterne=灯笼 a', 'Laterne=lanterna a'),
    ('Geisterspiel=空场比赛 d', 'Geisterspiel=partita fantasma d'),
    ('Versöhnung=和解 c', 'Versöhnung=riconciliazione c'),
    ('singst（第二人称单数）', 'singst (2ª pers. sing.)'),
    ('macht（第二人称复数）', 'macht (2ª pers. plur.)'),
    ('essen（第一人称复数）', 'essen (1ª pers. plur.)'),
    ('machst（第二人称单数）', 'machst (2ª pers. sing.)'),
    ('schaue（第一人称单数）', 'schaue (1ª pers. sing.)'),
    ('G · DIALOG · 对话补全', 'G · DIALOG · Completare il dialogo'),
    ('开放题 — 要点见写作框，范文在第 8 版写作框内', 'Compito aperto — segui i punti del riquadro; il testo modello è nel riquadro di questa pagina'),
    ('按要点给分', 'Valutato secondo i punti elencati'),
    ('H · SCHREIBEN · 写作', 'H · SCHREIBEN · Scrittura'),
    ('用德语写 80–100 词：《我的十一月的一周》。写清做什么手工、看哪几场比赛、和谁一起，并写一句关于圣马丁节或纪念日的话。', "Scrivi in tedesco, 80–100 parole: «La mia settimana di novembre». Di' cosa costruisci, quali partite guardi e con chi — e aggiungi una frase su San Martino o sul giorno del ricordo."),
    ('MUSTER · 范文（84 Wörter）', 'MUSTER · Testo modello (84 parole)'),
    ('ANTWORTEN · 全部答案与简析（第 1–8 版）', 'ANTWORTEN · Tutte le risposte con note (pagine 1–8)'),
]
rep_all("content8.py", C8)

# ---------- P8 keys ----------
rep("content8.py", 'kf.para(f"— \u7b2c {pg} \u7248 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— PAGINA {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"\uff08{e[\'note\']}\uff09"',
    's += f" ({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)', 1)

# ---------- generic value maps ----------
TYPEMAP = [('完成句子', 'completare'), ('单选', 'scelta multipla'), ('句型转换', 'trasformazione'), ('词汇配对', 'abbinamento'), ('判断对错', 'vero/falso'), ('完形填空', 'testo a buchi'), ('造句', 'costruire frasi'), ('对话补全', 'completare il dialogo'), ('翻译', 'traduzione'), ('写作', 'scrittura')]
INSTRMAP = [('instr="填空"', 'instr="Completa"'), ('instr="改写"', 'instr="Riscrivi"'), ('instr="判断"', 'instr="Vero o falso?"'), ('instr="造句"', 'instr="Costruisci la frase"'), ('instr="翻译"', 'instr="Traduci in italiano"'), ('instr="把词和释义配对"', 'instr="Abbina le coppie"')]
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
