# -*- coding: utf-8 -*-
"""DE x NL fan-out transform for W46 DE core build copy.
Generated from the EN pair table + tr-nl.py. German body text is
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
    rep(f, "weekly-report-w46-de-core", "weekly-report-w46-de-nl", 1)

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
    '"Die Lucerna · DUITS WEEKBLAD VOL.3 · TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS"', 1)
rep("bslib4.py", 'f"\u7b2c {n} \u7248 / \u5171 {total} \u7248"', 'f"Pagina {n} van {total}"', 1)
rep("bslib4.py", '"\u8bd1\u6ce8\uff5c" + s', '"Uitleg — " + s', 1)

# ================= content12.py =================
C12 = [
    ('WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语', 'WÖCHENTLICH AUF DEUTSCH · ELKE WEEK · HET DUITS DAT DE DUITSERS LEZEN'),
    ('德 语 周 报 · VOL.3 · 国 家 队 · 圣 马 丁 · NFL', 'DUITS WEEKBLAD · VOL.3 · NATIONALE PLOEG · SINT MAARTEN · NFL'),
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")', 'p.text(975, 372, "TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 20, "sans", True, BRICK, anchor="middle")'),
    ('本周国家队周 · 圣马丁节与 NFL', 'INTERLANDWEEK · SINT MAARTEN EN NFL'),
    ('详见第 4 版 · Seite 4', 'Zie pagina 4'),
    ('DIE TOPMELDUNG · 头条', 'DIE TOPMELDUNG · Hoofdverhaal'),
    ('讲解｜die Länderspielpause 国家队比赛间歇期 · das Viertelfinale 四分之一决赛 · ausverkauft 售罄。', 'Uitleg — die Länderspielpause = interlandperiode · das Viertelfinale = kwartfinale · ausverkauft = uitverkocht.'),
    ('DIE WOCHE IN ZAHLEN · 数字看本周', 'DIE WOCHE IN ZAHLEN · In cijfers'),
    ('5 — Punkte hat Deutschland nach vier Spielen in der Nations League（四轮过后德国队 5 分）', '5 — Punkte hat Deutschland nach vier Spielen in der Nations League (Duitsland heeft 5 punten na vier wedstrijden)'),
    ('11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（11 点 11 分狂欢季开幕）', '11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln (het carnavalsseizoen begint om 11.11 uur)'),
    ('15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（周日 15 点 30 分 NFL 开球）', '15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München (de NFL-wedstrijd begint zondag om 15.30 uur)'),
    ('JETZT ÜBEN · 即学即练', 'JETZT ÜBEN · Nu oefenen'),
    ('国家队比赛周', 'interlandweek'),
    ('塞尔维亚首都', 'hoofdstad van Servië'),
    ('狂欢季 11 点 11 分开幕', 'carnaval begint om 11.11 uur'),
    ('NFL 在慕尼黑', 'de NFL in München'),
    ('四轮 5 分', '5 punten na vier wedstrijden'),
    ('周日是纪念日', 'zondag is de herdenkingsdag'),
    ('圣马丁节 11 月 11 日', 'Sint Maarten is op 11 november'),
    ('11 月 11 日是星期三', '11 november is een woensdag'),
    ('本周大问题 · Die Fragen der Woche', 'Grote vragen · Die Fragen der Woche'),
    ('德国本周最热议的五个问题。', 'De vijf hete vragen van Duitsland deze week.'),
    ('IN DIESER AUSGABE · 本期目录', 'IN DIESER AUSGABE · Inhoud'),
    ('空场比赛（无观众）。详见第 4 版。', 'Een wedstrijd zonder toeschouwers. Zie pagina 4.'),
    ('KURZ & GUT · 快讯', 'KURZ & GUT · Kort & goed'),
    ('BLITZQUIZ · 闪电问答', 'BLITZQUIZ · Bliksemquiz'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Lees pagina 1 en kies het juiste antwoord · Antwoorden op pagina 8'),
    ('周五客战塞尔维亚', 'uit in Servië op vrijdag'),
    ('NFL 下午 3 点半开球', 'NFL begint om 15.30 uur'),
    ('纪念日在周日', 'de herdenkingsdag is op zondag'),
    ('LEBEN · 生活', 'LEBEN · Het leven'),
    ('LEVEL A2 · Der 11. November & der Alltag · 11 月 11 日与日常生活', 'LEVEL A2 · Der 11. November & der Alltag · 11 november en het dagelijks leven'),
    ('der Jeck 狂欢者（科隆方言） · die fünfte Jahreszeit 第五个季节（狂欢季） · die Laterne 灯笼 · der Weckmann 面人面包 · die Martinsgans 圣马丁鹅。', 'der Jeck = carnavalsvierder (Keuls dialect) · die fünfte Jahreszeit = het vijfde seizoen (carnaval) · die Laterne = lantaarn · der Weckmann = broodmannetje · die Martinsgans = Sint-Maartensgans.'),
    ('DER 11. NOVEMBER · 11 月 11 日', 'DER 11. NOVEMBER'),
    ('你过狂欢节还是圣马丁节？写两句德语寄来。', 'Carnaval of Sint Maarten? Schrijf twee Duitse zinnen!'),
    ('UND SIE? · 说说你自己', 'UND SIE? · En u?'),
    ('MARTIN IN KÜRZE · 圣马丁简讯', 'MARTIN IN KÜRZE · In het kort'),
    ('RECHNEN WIR MAL · 算一算', 'RECHNEN WIR MAL · Laten we rekenen'),
    ('Die Uhrzeiten der Woche · 本周时刻', 'Die Uhrzeiten der Woche · De tijden van de week'),
    ('注意：11 月 11 日是工作日。去科隆要早到：老城很挤，晚上街道属于提灯笼的孩子们。', "Let op: 11 november is een werkdag. Kom vroeg naar Keulen: de oude stad is druk, en 's avonds zijn de straten van de kinderen met hun lantaarns."),
    ('ÜBUNGEN · 第 2 版练习', 'ÜBUNGEN · Oefeningen pagina 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Antwoorden op pagina 8 · De niveaus lopen door elkaar — vind elk antwoord op nummer'),
    ('看第 2 版文章，用时间填空。', 'Lees het artikel op pagina 2 en vul de tijden in.'),
    ('WDR 10 点半直播', 'WDR live vanaf 10.30 uur'),
    ('Weckmann 是面人面包', 'een Weckmann is een broodmannetje'),
    ('11 月 11 日不是法定假日', '11 november is geen feestdag'),
    ('圣马丁鹅配红甘蓝和丸子', 'Sint-Maartensgans met rodekool en knoedels'),
    ('改成 Perfekt 现在完成时。', 'Herschrijf in de Perfekt (voltooid tegenwoordige tijd).'),
    ('读第 2 版文章，选出正确答案。', 'Lees het artikel op pagina 2 en kies het juiste antwoord.'),
    ('Jeck=狂欢者 c', 'Jeck=carnavalsvierder c'),
    ('Laterne=灯笼 a', 'Laterne=lantaarn a'),
    ('Weckmann=面人面包 b', 'Weckmann=broodmannetje b'),
    ('Martinsgans=圣马丁鹅 d', 'Martinsgans=Sint-Maartensgans d'),
]
rep_all("content12.py", C12)

# ================= content34.py =================
C34 = [
    ('KULTUR · 文化', 'KULTUR · Cultuur'),
    ('A2 → B1 · St. Martin, Karneval & Rückblick · 圣马丁、狂欢节与回顾', 'A2 → B1 · St. Martin, Karneval & Rückblick · Sint Maarten, carnaval en een terugblik'),
    ('der Bettler 乞丐 · der Mantel 斗篷 · das Geschnatter 鹅叫声 · der Gänsestall 鹅棚 · das Dreigestirn 狂欢节三人组。', 'der Bettler = bedelaar · der Mantel = mantel · das Geschnatter = gesnater · der Gänsestall = ganzenstal · das Dreigestirn = carnavalstriumviraat.'),
    ('ST. MARTIN · 圣马丁', 'ST. MARTIN · Sint Maarten'),
    ('die Laterne — 灯笼', 'die Laterne — lantaarn'),
    ('der Mantel — 斗篷', 'der Mantel — mantel'),
    ('die Gans — 鹅', 'die Gans — gans'),
    ('der Weckmann — 面人面包', 'der Weckmann — broodmannetje'),
    ('das Martinsfeuer — 圣马丁篝火', 'das Martinsfeuer — Sint-Maartensvuur'),
    ('das Kostüm — 服装', 'das Kostüm — kostuum'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · Sint Maarten'),
    ('UND SIE? · 说说你自己', 'UND SIE? · En u?'),
    ('你做过灯笼吗？你们国家的孩子唱什么歌？写两句德语寄来。', 'Heb je een lantaarn gemaakt? Twee Duitse zinnen!'),
    ('DER TIPP · 编辑部建议', 'DER TIPP · Tip'),
    ('ÜBUNGEN · 第 3 版练习', 'ÜBUNGEN · Oefeningen pagina 3'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Antwoorden op pagina 8 · De niveaus lopen door elkaar — vind elk antwoord op nummer'),
    ('读第 3 版文章，判断对错。', 'Lees het artikel op pagina 3. Juist of onjuist?'),
    ('传说马丁是罗马士兵', 'de legende zegt dat Maarten een Romeinse soldaat was'),
    ('传说鹅叫声暴露了他', 'de legende zegt dat de ganzen hem verraadden'),
    ('纪念日 11 月 11 日', 'de herdenkingsdag is 11 november'),
    ('截稿时 11 月 3–8 日结果未知', 'uitslagen van 3–8 november onbekend bij het ter perse gaan'),
    ('狂欢季 11 点 11 分开幕', 'carnaval begint om 11.11 uur'),
    ('用方框里的词填空。', 'Vul in met de woorden uit het kader.'),
    ('斗篷分给乞丐', 'de mantel gedeeld met de bedelaar'),
    ('纸灯笼', 'een papieren lantaarn'),
    ('圣马丁鹅', 'de Sint-Maartensgans'),
    ('圣马丁鹅配红甘蓝和丸子', 'Sint-Maartensgans met rodekool en knoedels'),
    ('狂欢节服装', 'een carnavalskostuum'),
    ('游行在篝火处结束', 'de optocht eindigt bij het vuur'),
    ('选出正确答案。', 'Kies het juiste antwoord.'),
    ('马丁后来成为图尔主教', 'Maarten werd later bisschop van Tours'),
    ('灯笼游行常在前后晚上举行', 'lantaarnoptochten zijn vaak op avonden in de buurt'),
    ('VOL.4 报道 11 月 3–8 日结果', 'VOL.4 meldt de uitslagen van 3–8 november'),
    ('把词组成正确的句子。', 'Zet de woorden in een correcte zin.'),
    ('主谓宾顺序', 'volgorde onderwerp–werkwoord–voorwerp'),
    ('时间状语开头，动词第二位', 'tijdsbepaling eerst, werkwoord tweede'),
    ('地点开头，动词第二位', 'plaats eerst, werkwoord tweede'),
    ('SPORT · 体育', 'SPORT · Sport'),
    ('LEVEL B1 · Nationalelf & NFL · 国家队与 NFL', 'LEVEL B1 · Nationalelf & NFL · Nationale ploeg en NFL'),
    ('das Geisterspiel 空场比赛 · das Hinspiel 首回合 · ausverkauft 售罄 · der Star 明星 · gewinnen 获胜。', 'das Geisterspiel = spookwedstrijd · das Hinspiel = heenwedstrijd · ausverkauft = uitverkocht · der Star = ster · gewinnen = winnen.'),
    ('你更爱看足球还是美式橄榄球？贝尔格莱德谁赢？写两句德语寄来。', 'Voetbal of American football? Wie wint? Twee zinnen!'),
    ('DER SPIELPLAN · 本周与下周赛程', 'DER SPIELPLAN · Deze week en volgende week'),
    ('ÜBUNGEN · 第 4 版练习', 'ÜBUNGEN · Oefeningen pagina 4'),
    ('读第 4 版文章，选出正确答案。', 'Lees het artikel op pagina 4 en kies het juiste antwoord.'),
    ('德国 5 分，荷兰希腊各 8 分', 'Duitsland 5 punten, Nederland en Griekenland elk 8'),
    ('主教练 11 月 5 日公布名单', 'de bondscoach noemt de selectie op 5 november'),
    ('贝尔格莱德空场', 'leeg stadion in Belgrado'),
    ('首回合德国 2:0 胜塞尔维亚', 'Duitsland won de heenwedstrijd met 2-0 van Servië'),
    ('NFL 慕尼黑赛售罄', 'de NFL-wedstrijd in München is uitverkocht'),
    ('Geisterspiel=空场比赛 b', 'Geisterspiel=spookwedstrijd b'),
    ('Hinspiel=首回合 a', 'Hinspiel=heenwedstrijd a'),
    ('Ausrüster=装备赞助商 c', 'Ausrüster=tenueleverancier c'),
    ('ausverkauft=售罄 d', 'ausverkauft=uitverkocht d'),
    ('用比较级完成句子（括号里是原级）。', 'Vul in met de vergrotende trap (het woord tussen haakjes is de stellende trap).'),
    ('viel → mehr（荷兰 8 分多于德国 5 分）', 'viel → mehr (Nederland heeft 8 punten, meer dan de 5 van Duitsland)'),
    ('spät → später（15:30 晚于 11:11）', 'spät → später (15.30 uur is later dan 11.11 uur)'),
    ('leise → leiser（空场比主场安静）', 'leise → leiser (een leeg stadion is stiller dan een thuiswedstrijd)'),
    ('früh → früher（11 月 5 日早于 11 月 13 日）', 'früh → früher (5 november is eerder dan 13 november)'),
    ('看上面的赛程表，选出正确答案。', 'Kijk naar het speelschema hierboven en kies het juiste antwoord.'),
    ('塞尔维亚–德国周五 20:45', 'Servië–Duitsland op vrijdag om 20.45 uur'),
    ('NFL 周日 15:30', 'NFL op zondag om 15.30 uur'),
    ('德国–荷兰周一 20:45', 'Duitsland–Nederland op maandag om 20.45 uur'),
    ('拜仁–科隆周五 20:30', 'Bayern–Keulen op vrijdag om 20.30 uur'),
    ('沙尔克–斯图加特周六 17:30', 'Schalke–Stuttgart op zaterdag om 17.30 uur'),
]
rep_all("content34.py", C34)

# ================= content56.py =================
C56 = [
    ('JUGEND · 青年', 'JUGEND · Jeugd'),
    ('LEVEL B1 · Laternen, Lieder & Schule · 灯笼、歌曲与学校', 'LEVEL B1 · Laternen, Lieder & Schule · Lantaarns, liedjes en school'),
    ('basteln 制作 · der Pausenhof 课间操场 · sich verkleiden 乔装打扮 · die Stimmung 气氛 · der Pirat 海盗。', 'basteln = knutselen · der Pausenhof = schoolplein · sich verkleiden = verkleden · die Stimmung = sfeer · der Pirat = piraat.'),
    ('SCHULWOCHE · 开学周', 'SCHULWOCHE · Naar school'),
    ('die Laterne — 灯笼', 'die Laterne — lantaarn'),
    ('basteln — 制作', 'basteln — knutselen'),
    ('das Lied — 歌曲', 'das Lied — lied'),
    ('das Kostüm — 服装', 'das Kostüm — kostuum'),
    ('der Umzug — 游行', 'der Umzug — optocht'),
    ('der Stern — 星星', 'der Stern — ster'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · Sint Maarten'),
    ('UND SIE? · 说说你自己', 'UND SIE? · En u?'),
    ('你小时候做过灯笼吗？11 月你唱哪首歌？写两句德语寄来。', 'Een lantaarn als kind? Jouw lied? Twee zinnen!'),
    ('DER WOCHENPLAN DER REDAKTION · 编辑部一周计划', 'DER WOCHENPLAN DER REDAKTION · De week van de redactie'),
    ('ÜBUNGEN · 第 5 版练习', 'ÜBUNGEN · Oefeningen pagina 5'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Antwoorden op pagina 8 · De niveaus lopen door elkaar — vind elk antwoord op nummer'),
    ('读第 5 版文章，选出正确答案。', 'Lees het artikel op pagina 5 en kies het juiste antwoord.'),
    ('11 月 9 日全德复课', 'school begint overal weer op 9 november'),
    ('孩子们做纸灯笼', 'kinderen maken papieren lantaarns'),
    ('纸灯笼', 'een papieren lantaarn'),
    ('上午狂欢，下午圣马丁', "carnaval 's ochtends, Sint Maarten 's middags"),
    ('NFL 周日在电视上', 'de NFL op tv op zondag'),
    ('周五看国家队比赛', 'het nationale team kijken op vrijdag'),
    ('用方框里的词填空。', 'Vul in met de woorden uit het kader.'),
    ('做灯笼', 'lantaarns maken'),
    ('唱圣马丁歌曲', 'Sint-Maartensliedjes zingen'),
    ('狂欢节服装', 'een carnavalskostuum'),
    ('灯笼游行', 'een lantaarnoptocht'),
    ('灯笼上的星星', 'de ster op de lantaarn'),
    ('用 weil 连接两个句子（动词放句末）。', 'Verbind de twee zinnen met weil (het werkwoord gaat naar het eind).'),
    ('weil 句动词置尾', 'in een weil-zin gaat het werkwoord naar het eind'),
    ('ist 置尾', 'ist gaat naar het eind'),
    ('will 置尾', 'will gaat naar het eind'),
    ('beginnt 置尾', 'beginnt gaat naar het eind'),
    ('判断对错。', 'Juist of onjuist?'),
    ('11 月 9 日巴伐利亚也复课', 'Beieren ook terug op 9 november'),
    ('灯笼游行在晚上', "de lantaarnoptocht is 's avonds"),
    ('孩子们唱圣马丁歌曲', 'kinderen zingen Sint-Maartensliedjes'),
    ('VERTIEFUNG · 深读', 'VERTIEFUNG · Verdieping'),
    ('LEVEL B2 · Volkstrauertag & Stromsteuer · 纪念日与电力税', 'LEVEL B2 · Volkstrauertag & Stromsteuer · Herdenkingsdag en stroomtaks'),
    ('gedenken 纪念 · die Kranzniederlegung 献花圈 · der stille Tag 安静日 · die Verbundenheit 联系 · die Versöhnung 和解。', 'gedenken = herdenken · Kranzniederlegung = krans · stille Tag = stille dag · verbondenheid · verzoening.'),
    ('DIE ZAHLEN · 本周数字', 'DIE ZAHLEN · De cijfers'),
    ('纪念日：纪念需要安静——对此几乎人人赞同。电力税：降多少尚未确定。两者都关系到几乎每个家庭。', 'Herdenkingsdag: herdenken vraagt stilte — bijna iedereen is het eens. Stroomtaks: hoeveel hij daalt is nog open. Beide raken bijna elk huishouden.'),
    ('ZWEI SONNTAGE IM NOVEMBER · 十一月的两个周日', 'ZWEI SONNTAGE IM NOVEMBER · Twee zondagen in november'),
    ('WAS INTERESSIERT DIE LESER? · 读者最关心什么？', 'WAS INTERESSIERT DIE LESER? · Wat interesseert de lezers?'),
    ('("Nations League und NFL", 46, "足球")', '("Nations League und NFL", 46, "voetbal")'),
    ('("St. Martin und Karneval", 34, "节日")', '("St. Martin und Karneval", 34, "feesten")'),
    ('("Volkstrauertag und Gedenken", 20, "纪念")', '("Volkstrauertag und Gedenken", 20, "herdenken")'),
    ('ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）', 'ÜBUNGSDATEN · Oefengegevens — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Oefengegevens, geen echte enquête.)'),
    ('ÜBUNGEN · 第 6 版练习', 'ÜBUNGEN · Oefeningen pagina 6'),
    ('看上面的练习图表，选出正确答案。', 'Gebruik de oefengrafiek hierboven.'),
    ('46% 足球最受关注', 'voetbal leidt met 46%'),
    ('节日 34% 第二', 'feesten tweede met 34%'),
    ('纪念 20% 最小', 'herdenken het kleinst met 20%'),
    ('纪念 20%', 'herdenken 20%'),
    ('读第 6 版深读文章，选出正确答案。', 'Lees het artikel op pagina 6.'),
    ('11 月 15 日纪念日', 'de herdenkingsdag is 15 november'),
    ('ZDF 13 点半直播纪念仪式', 'ZDF live vanaf 13.30 uur'),
    ('家庭电力税 2.05 欧分', 'de stroomtaks voor huishoudens is 2,05 cent'),
    ('2027 年预算 11 月 27 日表决', 'stemming over de begroting 2027 op 27 november'),
    ('用括号里的形式填空。', 'Vul in met de vorm tussen haakjes.'),
    ('被动：wird + Partizip II', 'passief: wird + voltooid deelwoord'),
    ('ob 引导间接疑问句', 'ob leidt een indirecte vraag in'),
    ('献花圈仪式', 'een kransleggingsceremonie'),
    ('为和平与和解', 'voor vrede en verzoening'),
    ('德奥联系', 'Duits-Oostenrijkse verbondenheid'),
    ('纪念受害者', 'de slachtoffers herdenken'),
]
rep_all("content56.py", C56)

# ================= content7.py =================
C7 = [
    ('SPRACHE · 语言', 'SPRACHE · Taal'),
    ('A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所', 'A2 → B2 · Sätze der Woche & Fehlerklinik · Zinnen van de week en foutenkliniek'),
    ('本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。', 'Deze pagina gaat helemaal over taal: drie korte lessen, de zinnen van de week (allemaal woord voor woord geciteerd uit de artikelen van dit nummer), de foutenkliniek en lezersbrieven.'),
    ('BEISPIELE · 例句', 'BEISPIELE · Voorbeelden'),
    ('被动：wird + Partizip II', 'passief: wird + voltooid deelwoord'),
    ('复数：werden', 'meervoud: werden'),
    ('werden + 原形表将来', 'werden + infinitief voor de toekomst'),
    ('被动语态', 'lijdende vorm'),
    ('lang → länger（夜晚比白天长）', 'lang → länger (de nacht is langer dan de dag)'),
    ('weil 引导原因', 'weil leidt een reden in'),
    ('weil 句动词置尾', 'in een weil-zin gaat het werkwoord naar het eind'),
    ('länger als = 比……更长', 'länger als = langer dan'),
    ('„Länger als sonst“ heißt... A. 比平时更长 · B. 和平时一样 · C. 比平时更短', '„Länger als sonst“ betekent... A. langer dan anders · B. hetzelfde als anders · C. korter dan anders'),
    ('ob 引导间接疑问', 'ob leidt een indirecte vraag in'),
    ('Es ist fraglich, ob ... = 是否还难说', 'Es ist fraglich, ob ... = het is twijfelachtig of ...'),
    ('dass 句动词置尾', 'in een dass-zin gaat het werkwoord naar het eind'),
    ('礼貌表达观点', 'een beleefde manier om een mening te geven'),
    ('11.11 Uhr = 11 点 11 分', '11.11 Uhr = 11.11 uur'),
    ('vor leeren Rängen = 空场，没有观众', 'vor leeren Rängen = leeg stadion'),
    ('Es wird gespielt. = 比赛将进行（被动）', 'Es wird gespielt. = Er wordt gespeeld'),
    ('Meiner Meinung nach ... = 在我看来……', 'Meiner Meinung nach = naar mijn mening'),
    ('Ich finde, dass ... = 我觉得……', 'Ich finde, dass = ik vind dat'),
    ('Es ist fraglich, ob ... = 是否……还难说', 'Es ist fraglich, ob ... = twijfelachtig of'),
    ('DER WERKZEUGKASTEN · 工具箱', 'DER WERKZEUGKASTEN'),
    ('label = "Ein Beispiel der Redaktion!"', 'label = "Een voorbeeld van de redactie!"'),
    ('编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.4。请寄来您的习作，优秀者刊登于 VOL.4。', 'Voorbeeld van de redactie, geen echte brief: er waren bij het ter perse gaan geen echte brieven binnen. Stuur ons die van jou voor VOL.4!'),
    ('LESERBRIEFE · 读者来信', 'LESERBRIEFE · Lezersbrieven'),
    ('NOCH EIN WORT · 再学一词', 'NOCH EIN WORT · Nog één woord'),
    ('«das Geisterspiel»（Seite 4）: ein Spiel ohne Zuschauer im Stadion. 空场比赛。', '«das Geisterspiel» (Seite 4) : ein Spiel ohne Zuschauer im Stadion. Spookwedstrijd: geen toeschouwers.'),
    ('SÄTZE DER WOCHE · 本周金句', 'SÄTZE DER WOCHE · Zinnen van de week'),
    ('原文摘录，逐字引自本期文章 · 括号内为出处', 'Woord voor woord geciteerd uit de artikelen van dit nummer · bron tussen haakjes'),
    ('德甲休战——但国家队要比赛。', 'De Bundesliga pauzeert — maar het nationale team speelt.'),
    ('11 点 11 分，科隆新一季狂欢季开幕。', 'Om 11.11 uur begint in Keulen het nieuwe carnavalsseizoen.'),
    ('他的纪念日是 11 月 11 日。', 'Zijn herdenkingsdag is 11 november.'),
    ('书包收拾好了，操场上又热闹起来。', 'De rugzakken zijn gepakt, de schoolpleinen zijn weer luid.'),
    ('十一月黑暗，但并不安静：它歌唱、发光、庆祝。', 'November is donker, maar niet stil: hij zingt, schijnt en viert feest.'),
    ('比赛售罄，RTL 现场直播。', 'De wedstrijd is uitverkocht; RTL zendt live uit.'),
    ('这里的纪念意味着：停下来、记住——并为和平与和解挺身而出。', 'Herdenken betekent hier: stilstaan, herinneren — en opkomen voor vrede en verzoening.'),
    ('周日，全国一片安静。', 'Op zondag is het land stil.'),
    ('FEHLERKLINIK · 纠错诊所', 'FEHLERKLINIK · De foutenkliniek'),
    ('学习者最常犯的四个错 · 先自己改，再看答案', 'Vier fouten die leerlingen het vaakst maken · corrigeer ze eerst, controleer dan'),
    ('动词第二位：主语不在句首时，动词仍居第二。', 'Werkwoord tweede: ook als het onderwerp niet eerst staat, blijft het werkwoord tweede.'),
    ('halb zwölf = 十一点半（zwölf 之前）。', 'halb zwölf = 11.30 uur, een halfuur voor twaalf.'),
    ('Perfekt 中 Partizip II 放句末。', 'In de Perfekt gaat het voltooid deelwoord naar het eind.'),
    ('ob 从句动词放句末。', 'In een ob-zin gaat het werkwoord naar het eind.'),
    ('IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.4)', 'IN DER NÄCHSTEN AUSGABE · Volgend nummer (VOL.4)'),
]
rep_all("content7.py", C7)

# ================= content8.py =================
C8 = [
    ('ÜBUNGEN & ANTWORTEN · 练习与答案', 'ÜBUNGEN & ANTWORTEN · Oefeningen & antwoorden'),
    ('SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方', 'SCHLUSSTEST · Eindtoets · Alle Antworten unten auf dieser Seite — alle antwoorden onderaan deze pagina'),
    ('beginnt（第三人称单数）', 'beginnt (3e persoon enkelvoud)'),
    ('bastelt（第三人称单数）', 'bastelt (3e persoon enkelvoud)'),
    ('geht（第三人称单数）', 'geht (3e persoon enkelvoud)'),
    ('singt（第三人称单数）', 'singt (3e persoon enkelvoud)'),
    ('schaut（第三人称单数）', 'schaut (3e persoon enkelvoud)'),
    ('sieht（第三人称单数）', 'sieht (3e persoon enkelvoud)'),
    ('erzählt（第三人称单数）', 'erzählt (3e persoon enkelvoud)'),
    ('A · LÜCKENTEXT · 完形填空', 'A · LÜCKENTEXT · Gatentekst'),
    ('选项：', 'Opties:'),
    ('B · WISSENSFRAGEN · 综合问答', 'B · WISSENSFRAGEN · Quiz'),
    ('狂欢季 11 点 11 分开幕', 'carnaval begint om 11.11 uur'),
    ('周五客战塞尔维亚', 'uit in Servië op vrijdag'),
    ('NFL 周日 15:30', 'NFL op zondag om 15.30 uur'),
    ('纪念日 11 月 15 日', 'de herdenkingsdag is 15 november'),
    ('家庭电力税 2.05 欧分', 'de stroomtaks voor huishoudens is 2,05 cent'),
    ('主教练 11 月 5 日公布名单', 'de bondscoach noemt de selectie op 5 november'),
    ('ZDF 13 点半直播纪念仪式', 'ZDF live vanaf 13.30 uur'),
    ('亡灵主日 11 月 22 日', 'Totensonntag is 22 november'),
    ('C · LESEVERSTEHEN · 阅读理解', 'C · LESEVERSTEHEN · Lezen'),
    ('周三做灯笼', 'een lantaarn maken op woensdag'),
    ('周五看德国队', 'Duitsland kijken op vrijdag'),
    ('D · SÄTZE BAUEN · 造句', 'D · SÄTZE BAUEN · Zinnen'),
    ('时间状语，动词第二位', 'tijdsbepaling, werkwoord tweede'),
    ('主谓宾顺序', 'volgorde onderwerp–werkwoord–voorwerp'),
    ('时间状语开头，动词第二位', 'tijdsbepaling eerst, werkwoord tweede'),
    ('地点时间开头，动词第二位', 'plaats en tijd eerst, werkwoord tweede'),
    ('E · ÜBERSETZEN · 翻译', 'E · ÜBERSETZEN · Vertalen'),
    ('狂欢节 11 点 11 分在科隆开幕。', 'Het carnaval begint om 11.11 uur in Keulen.'),
    ('beginnen = 开始', 'beginnen = beginnen'),
    ('Der Karneval beginnt um 11.11 Uhr in Köln.（译成中文）', 'Der Karneval beginnt um 11.11 Uhr in Köln. (vertaal naar het Nederlands)'),
    ('我周三做一个灯笼。', 'Ik maak een lantaarn op woensdag.'),
    ('basteln = 制作', 'basteln = knutselen'),
    ('Ich bastle am Mittwoch eine Laterne.（译成中文）', 'Ich bastle am Mittwoch eine Laterne. (vertaal naar het Nederlands)'),
    ('学校 11 月 9 日又开学了。', 'School begon weer op 9 november.'),
    ('wieder begonnen = 又开始', 'wieder begonnen = weer begonnen'),
    ('Die Schule hat am 9. November wieder begonnen.（译成中文）', 'Die Schule hat am 9. November wieder begonnen. (vertaal naar het Nederlands)'),
    ('看比赛 = das Spiel schauen', 'een wedstrijd kijken = das Spiel schauen'),
    ('"我周日看 NFL 比赛。（译成德语）", instr="翻译"', '"Ik kijk de NFL-wedstrijd op zondag. (vertaal naar het Duits)", instr="Vertaal naar het Duits"'),
    ('F · WÖRTER PAAREN · 词汇配对', 'F · WÖRTER PAAREN · Koppelen'),
    ('Mantel=斗篷 b', 'Mantel=mantel b'),
    ('Laterne=灯笼 a', 'Laterne=lantaarn a'),
    ('Geisterspiel=空场比赛 d', 'Geisterspiel=spookwedstrijd d'),
    ('Versöhnung=和解 c', 'Versöhnung=verzoening c'),
    ('singst（第二人称单数）', 'singst (2e persoon enkelvoud)'),
    ('macht（第二人称复数）', 'macht (2e persoon meervoud)'),
    ('essen（第一人称复数）', 'essen (1e persoon meervoud)'),
    ('machst（第二人称单数）', 'machst (2e persoon enkelvoud)'),
    ('schaue（第一人称单数）', 'schaue (1e persoon enkelvoud)'),
    ('G · DIALOG · 对话补全', 'G · DIALOG · Dialoog aanvullen'),
    ('开放题 — 要点见写作框，范文在第 8 版写作框内', 'Open taak — volg de punten in het schrijfkader; de modeltekst staat in het kader op deze pagina'),
    ('按要点给分', 'Beoordeeld op de genoemde punten'),
    ('H · SCHREIBEN · 写作', 'H · SCHREIBEN · Schrijven'),
    ('用德语写 80–100 词：《我的十一月的一周》。写清做什么手工、看哪几场比赛、和谁一起，并写一句关于圣马丁节或纪念日的话。', 'Schrijf in het Duits, 80–100 woorden: «Mijn week in november». Zeg wat je maakt, welke wedstrijden je kijkt en met wie — en voeg één zin toe over Sint Maarten of de herdenkingsdag.'),
    ('MUSTER · 范文（84 Wörter）', 'MUSTER · Voorbeeldtekst (84 woorden)'),
    ('ANTWORTEN · 全部答案与简析（第 1–8 版）', 'ANTWORTEN · Alle antwoorden met notities (pagina 1–8)'),
]
rep_all("content8.py", C8)

# ---------- P8 keys ----------
rep("content8.py", 'kf.para(f"— \u7b2c {pg} \u7248 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— Pagina {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"\uff08{e[\'note\']}\uff09"',
    's += f"({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)', 1)

# ---------- generic value maps ----------
TYPEMAP = [('完成句子', 'invullen'), ('单选', 'meerkeuze'), ('句型转换', 'omvormen'), ('词汇配对', 'koppelen'), ('判断对错', 'juist-onjuist'), ('完形填空', 'gatentekst'), ('造句', 'zinnen bouwen'), ('对话补全', 'dialoog aanvullen'), ('翻译', 'vertalen'), ('写作', 'schrijven')]
INSTRMAP = [('instr="填空"', 'instr="Vul in"'), ('instr="改写"', 'instr="Herschrijf"'), ('instr="判断"', 'instr="Beoordeel"'), ('instr="造句"', 'instr="Vorm de zin"'), ('instr="翻译"', 'instr="Vertaal naar het Nederlands"'), ('instr="把词和释义配对"', 'instr="Combineer"')]
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
