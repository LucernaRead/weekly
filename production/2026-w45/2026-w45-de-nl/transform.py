# -*- coding: utf-8 -*-
"""DE x NL fan-out transform for W45 DE core build copy.
Rules: whole-line or exact-unique-literal replacements with count
assertions; value maps (types/instr) use bare text, never repr.
German body text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token. Run once from the build dir copy.
Furniture follows the shipped W43 DE x NL edition verbatim (VOL.2):
badge in the tagline slot y=372, 20pt sans bold BRICK; footer
'Die Lucerna · DUITS WEEKBLAD VOL.2 · TEKSTEN IN HET DUITS ·
UITLEG IN HET NEDERLANDS'; page line 'Pagina N van 8'; gloss prefix
'Uitleg — '; P8 separator '— Pagina N —'; P8 keys half-width parens.
"""
import os, sys

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

def rep_all(fname, pairs):
    for old, new in pairs:
        rep(fname, old, new)

# ---------- OUT repoint (1 per content file) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w45-de-core", "weekly-report-w45-de-nl", 1)

# ---------- svglib docstring comment only (not rendered) ----------
rep("svglib.py", "for 重阳.", "for Double Ninth.", 1)

# ---------- bslib4: furniture + gloss prefix (W43 DE x NL shipped forms, VOL.2) ----------
rep("bslib4.py",
    '"Die Lucerna · 德语周报 VOL.2 · LUCERNA GERMAN WEEKLY"',
    '"Die Lucerna · DUITS WEEKBLAD VOL.2 · TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} van {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Uitleg — " + s', 1)

# ---------- shared furniture strings ----------
SHARED = [
    ("UND SIE? · 说说你自己", "UND SIE? · En jij?"),
    ("FERIENWECHSEL · 假期交接", "FERIENWECHSEL · Vakantiewissel"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Antwoorden op pagina 8 · Niveaus lopen door elkaar — zoek per nummer"),
    ("BEISPIELE · 例句", "BEISPIELE · Voorbeelden"),
]
for f in ["content12.py", "content34.py", "content56.py"]:
    for old, new in SHARED:
        p = os.path.join(BASE, f)
        if old in open(p, encoding="utf-8").read():
            rep(f, old, new)

# ================= content12 (P1 + P2) =================
C12 = [
    ("WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语",
     "WÖCHENTLICH AUF DEUTSCH · ELKE WEEK · HET DUITS DAT DE DUITSERS LEZEN"),
    ("德 语 周 报 · VOL.2 · 足 球 周 · 油 价 · 护 理",
     "DUITS WEEKBLAD · VOL.2 · VOETBALWEEK · BRANDSTOFKORTING · ZORG"),
    # P1 subtitle slot -> W43 shipped badge, verbatim string, 20pt bold BRICK
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 20, "sans", True, BRICK, anchor="middle")'),
    ("本周足球周 · 欧冠欧联德甲连轴转", "Voetbalweek"),
    ("详见第 4 版 · Seite 4", "Zie pagina 4"),
    ("DIE TOPMELDUNG · 头条", "DIE TOPMELDUNG · Hoofdverhaal"),
    ("讲解｜die Englische Woche 一周双赛 · der Spieltag 比赛日 · empfangen 主场迎战 · die Bundesliga 德甲。",
     "Uitleg — die Englische Woche = Engelse week · der Spieltag = speeldag · empfangen = ontvangen · die Bundesliga = Bundesliga."),
    ("DIE WOCHE IN ZAHLEN · 数字看本周", "DIE WOCHE IN ZAHLEN · De week in cijfers"),
    ("9 — Spiele hat der 9. Spieltag der Bundesliga（德甲第 9 轮共 9 场比赛）",
     "9 — Spiele hat der 9. Spieltag der Bundesliga (9 wedstrijden op speeldag 9 van de Bundesliga)"),
    ("6 — deutsche Teams spielen in Europa（6 支德国球队出战欧战）",
     "6 — deutsche Teams spielen in Europa (6 Duitse teams spelen in Europa)"),
    ("14,04 — Cent pro Liter beträgt der Tankrabatt（每升油减税 14.04 欧分）",
     "14,04 — Cent pro Liter beträgt der Tankrabatt (14,04 cent minder belasting per liter)"),
    ("JETZT ÜBEN · 即学即练", "JETZT ÜBEN · Oefen nu"),
    ("一周双赛", "Engelse week"),
    ("多特主场迎战贝蒂斯", "Dortmund ontvangt Betis thuis"),
    ("欧联在周四", "Europa League op donderdag"),
    ("周五汉堡–门兴开轮", "Hamburg–Gladbach openen op vrijdag"),
    ("第 9 轮共 9 场", "9 wedstrijden op speeldag 9"),
    ("减税到 12 月 31 日", "korting tot 31 december"),
    ("拜仁周二客战马竞", "Bayern uit bij Atlético op dinsdag"),
    ("霍芬海姆欧联客战水晶宫", "Hoffenheim uit bij Crystal Palace in de Europa League"),
    ("本周大问题 · Die Fragen der Woche", "De vragen van de week"),
    ("德国本周最热议的五个问题。", "Vijf veelbesproken vragen in Duitsland deze week."),
    ("IN DIESER AUSGABE · 本期目录", "IN DIESER AUSGABE · Inhoud"),
    ("油价减税（加油折扣）。详见第 2 版。", "Brandstofkorting. Zie pagina 2."),
    ("KURZ & GUT · 快讯", "KURZ & GUT · Kort nieuws"),
    ("BLITZQUIZ · 闪电问答", "BLITZQUIZ · Bliksemquiz"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Lees pagina 1 en kies het juiste antwoord · Antwoorden op pagina 8"),
    # P2
    ("LEBEN · 生活", "LEBEN · Leven"),
    ("LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · 油价、电力税与护理",
     "LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · Brandstofkorting, stroomtaks en zorg"),
    ("der Tankrabatt 油价减税 · die Zapfsäule 加油机 · die Energiesteuer 能源税 · die Mehrwertsteuer 增值税 · der Angehörige 亲属。",
     "der Tankrabatt = brandstofkorting · die Zapfsäule = benzinepomp · die Energiesteuer = energiebelasting · die Mehrwertsteuer = btw · der Angehörige = familielid."),
    ("AN DER ZAPFSÄULE · 加油机旁", "AN DER ZAPFSÄULE · Bij de pomp"),
    ("你开车吗？你那里的油价是多少？写两句德语寄来。",
     "Rijd je auto? Wat kost benzine bij jou? Schrijf twee Duitse zinnen!"),
    ("ZEW IN KÜRZE · ZEW 指数简讯", "ZEW IN KÜRZE · ZEW in het kort"),
    ("RECHNEN WIR MAL · 算一算", "RECHNEN WIR MAL · Laten we rekenen"),
    ("Die Zahlen der Woche · 本周数字", "Die Zahlen der Woche · Cijfers van de week"),
    ("注意：减的是税，定价的是油站。出发前比比价。",
     "Let op: de belasting daalt, maar het tankstation bepaalt de prijs. Vergelijk prijzen voor je gaat tanken!"),
    ("ÜBUNGEN · 第 2 版练习", "ÜBUNGEN · Oefeningen pagina 2"),
    ("看第 2 版文章，用数字填空。", "Lees het artikel op pagina 2 en vul de cijfers in."),
    ("每升减税 14.04 欧分", "14,04 cent minder belasting per liter"),
    ("50 升省约 8.35 欧元", "ongeveer 8,35 euro bespaard op 50 liter"),
    ("减税到 2026 年底", "korting tot eind 2026"),
    ("国家少收约 25 亿欧元", "de staat loopt ongeveer 2,5 miljard euro mis"),
    ("加油机旁的实际降幅", "de verlaging aan de pomp, met btw"),
    ("改成 Perfekt 现在完成时。", "Zet in de Perfekt (voltooid tegenwoordige tijd)."),
    ("beschließen → beschlossen", "beschließen → beschlossen"),
    ("fallen 用 sein", "fallen met sein"),
    ("tanken → getankt", "tanken → getankt"),
    ("weitergeben 可分动词", "weitergeben is scheidbaar"),
    ("ZEW 预期下降", "ZEW-verwachtingen gedaald"),
    ("读第 2 版文章，选出正确答案。", "Lees het artikel op pagina 2 en kies het juiste antwoord."),
    ("减的是能源税", "de energiebelasting daalt"),
    ("油站定价", "het tankstation bepaalt de prijs"),
    ("联盟党与社民党", "Union en SPD"),
    ("家属居家护理", "familieleden zorgen thuis"),
    ("Tankrabatt=油价减税 b", "Tankrabatt = brandstofkorting b"),
    ("Zapfsäule=加油机 d", "Zapfsäule = benzinepomp d"),
    ("Mehrwertsteuer=增值税 a", "Mehrwertsteuer = btw a"),
    ("Angehörige=亲属 c", "Angehörige = familielid c"),
]
rep_all("content12.py", C12)

# ================= content34 (P3 + P4) =================
C34 = [
    ("KULTUR · 文化", "KULTUR · Cultuur"),
    ("A2 → B1 · Ferienwechsel & Herbst · 假期交接与秋天",
     "A2 → B1 · Ferienwechsel & Herbst · Vakantiewissel en herfst"),
    ("der Ferienwechsel 假期交接 · die Schülerin 女学生 · der Ausflug 短途出游 · der Advent 将临期 · die Lesung 朗读会。",
     "der Ferienwechsel = vakantiewissel · die Schülerin = scholier · der Ausflug = uitstapje · der Advent = advent · die Lesung = voorleesavond."),
    ("der Nebel — 雾", "der Nebel — mist"),
    ("das Laub — 落叶", "das Laub — bladeren"),
    ("der Kürbis — 南瓜", "der Kürbis — pompoen"),
    ("die Kerze — 蜡烛", "die Kerze — kaars"),
    ("der Spaziergang — 散步", "der Spaziergang — wandeling"),
    ("die Lesung — 朗读会", "die Lesung — voorleesavond"),
    ("HERBSTWÖRTER · 秋天词汇", "HERBSTWÖRTER · Herfstwoorden"),
    ("秋天你比夏天读得多吗？你的床头现在放着哪本书？写两句德语寄来。",
     "Lees je in de herfst meer dan in de zomer? Welk boek ligt er nu naast je bed? Schrijf twee Duitse zinnen!"),
    ("DER TIPP · 编辑部建议", "DER TIPP · Tip van de redactie"),
    ("ÜBUNGEN · 第 3 版练习", "ÜBUNGEN · Oefeningen pagina 3"),
    ("读第 3 版文章，判断对错。", "Lees het artikel op pagina 3. Juist of onjuist?"),
    ("BW 周一起复课", "Baden-Württemberg weer naar school op maandag"),
    ("巴伐利亚本周仍在放假", "Beieren nog op vakantie deze week"),
    ("诸圣节 11 月 1 日", "Allerheiligen is op 1 november"),
    ("10 月 31 日也是宗教改革日（九个州）", "31 oktober is ook Hervormingsdag in negen deelstaten"),
    ("诸圣节商店关门", "winkels gesloten op Allerheiligen"),
    ("用方框里的词填空。", "Vul in met de woorden uit het kader."),
    ("假期交接", "vakantiewissel"),
    ("去山区短途出游", "een uitstapje naar de bergen"),
    ("图书馆的朗读会", "een voorleesavond in de bibliotheek"),
    ("将临期在 11 月筹划", "advent wordt in november al gepland"),
    ("湖面上的雾", "mist boven het meer"),
    ('e.bridge("选出正确答案。")', 'e.bridge("Kies het juiste antwoord.")'),
    ("BW 假期已结束", "vakantie in Baden-Württemberg voorbij"),
    ("安静的节日", "een stille feestdag"),
    ("诸圣节扫墓", "graven bezoeken op Allerheiligen"),
    ("白天短所以夜晚长", "korte dagen, dus lange avonden"),
    ("把词组成正确的句子。", "Zet de woorden in de juiste volgorde."),
    ("时间地点开头，动词第二位", "tijd en plaats vooraan, werkwoord op plaats 2"),
    ("数量时间状语，动词第二位", "tijdsbepaling vooraan, werkwoord op plaats 2"),
    ("主谓宾顺序", "onderwerp–werkwoord–voorwerp"),
    ("bleiben + geschlossen", "bleiben + geschlossen"),
    # P4
    ("SPORT · 体育", "SPORT · Sport"),
    ("LEVEL B1 · Europapokal & Bundesliga · 欧战与德甲",
     "LEVEL B1 · Europapokal & Bundesliga · Europacups en Bundesliga"),
    ("die Englische Woche 一周双赛 · auswärts 客场 · empfangen 主场迎战 · der Favorit 夺冠热门 · eröffnen 揭开序幕。",
     "die Englische Woche = Engelse week · auswärts = uit · empfangen = ontvangen · der Favorit = favoriet · eröffnen = openen."),
    ("本周你支持谁？周六焦点战谁赢？写两句德语寄给编辑部。",
     "Wie steun jij deze week? Wie wint de topwedstrijd op zaterdag? Schrijf twee Duitse zinnen!"),
    ("DER 9. SPIELTAG · 第 9 轮赛程", "DER 9. SPIELTAG · Speeldag 9: de wedstrijden"),
    ("ÜBUNGEN · 第 4 版练习", "ÜBUNGEN · Oefeningen pagina 4"),
    ("读第 4 版文章，选出正确答案。", "Lees het artikel op pagina 4 en kies het juiste antwoord."),
    ("拜仁周二客战马竞", "Bayern uit bij Atlético op dinsdag"),
    ("斯图加特 18:45 开球", "Stuttgart begint om 18.45 uur"),
    ("多特主场迎战贝蒂斯", "Dortmund ontvangt Betis thuis"),
    ("霍芬海姆欧联客战水晶宫", "Hoffenheim uit bij Crystal Palace in de Europa League"),
    ("周六焦点战斯图加特–不来梅", "topwedstrijd op zaterdag: Stuttgart–Bremen"),
    ("Englische Woche=一周双赛 a", "Englische Woche = Engelse week a"),
    ("auswärts=客场 b", "auswärts = uit b"),
    ("Favorit=热门 c", "Favorit = favoriet c"),
    ("eröffnen=揭开序幕 d", "eröffnen = openen d"),
    ("用比较级完成句子（括号里是原级）。", "Vul in met de vergrotende trap (tussen haakjes staat de stellende trap)."),
    ("schwer → schwerer", "schwer → schwerer"),
    ("spät → später（19:30 最晚）", "spät → später (19.30 uur is het laatst)"),
    ("viel → mehr（球迷想要更多）", "viel → mehr (fans willen meer zien)"),
    ("früh → früher（18:45 早于 21:00）", "früh → früher (18.45 uur is vroeger dan 21.00 uur)"),
    ("看上面的赛程表，选出正确答案。", "Kijk naar de wedstrijdtabel hierboven en kies het juiste antwoord."),
    ("汉堡–门兴周五 20:30", "Hamburg–Gladbach op vrijdag om 20.30 uur"),
    ("斯图加特–不来梅周六 18:30", "Stuttgart–Bremen op zaterdag om 18.30 uur"),
    ("霍芬海姆–沙尔克周日 19:30", "Hoffenheim–Schalke op zondag om 19.30 uur"),
    ("弗赖堡–柏林联周日 17:30", "Freiburg–Union op zondag om 17.30 uur"),
    ("欧联周四霍芬海姆 18:45", "Europa League op donderdag, Hoffenheim om 18.45 uur"),
]
rep_all("content34.py", C34)

# ================= content56 (P5 + P6) =================
C56 = [
    ("JUGEND · 青年", "JUGEND · Jeugd"),
    ("LEVEL B1 · Zurück in die Schule · 重返校园",
     "LEVEL B1 · Zurück in die Schule · Terug naar school"),
    ("der Pausenhof 课间操场 · die Klassenarbeit 课堂测验 · das Referat 课堂报告 · ausschlafen 睡懒觉 · die Probe 排练。",
     "der Pausenhof = speelplaats · die Klassenarbeit = proefwerk · das Referat = spreekbeurt · ausschlafen = uitslapen · die Probe = repetitie."),
    ("der Pausenhof — 课间操场", "der Pausenhof — speelplaats"),
    ("die Klassenarbeit — 课堂测验", "die Klassenarbeit — proefwerk"),
    ("das Referat — 课堂报告", "das Referat — spreekbeurt"),
    ("der Rucksack — 书包", "der Rucksack — rugzak"),
    ("ausschlafen — 睡懒觉", "ausschlafen — uitslapen"),
    ("die Probe — 排练", "die Probe — repetitie"),
    ("SCHULWÖRTER · 校园词汇", "SCHULWÖRTER · Schoolwoorden"),
    ("你的学校假期后哪天开学？第一节是什么课？写两句德语寄来。",
     "Wanneer begon jouw school weer na de vakantie? Wat was je eerste les? Schrijf twee Duitse zinnen!"),
    ("DER WOCHENPLAN DER REDAKTION · 编辑部一周计划",
     "DER WOCHENPLAN DER REDAKTION · De week van de redactie"),
    ("ÜBUNGEN · 第 5 版练习", "ÜBUNGEN · Oefeningen pagina 5"),
    ("读第 5 版文章，选出正确答案。", "Lees het artikel op pagina 5 en kies het juiste antwoord."),
    ("BW 11 月 2 日开学", "Baden-Württemberg terug op 2 november"),
    ("巴伐利亚假期未结束", "vakantie in Beieren niet voorbij"),
    ("开学周有课堂测验", "proefwerken in de eerste schoolweek"),
    ("Referat = 课堂报告", "Referat = spreekbeurt"),
    ("巴伐利亚学生周五可去球场", "Beierse leerlingen kunnen vrijdag naar het stadion"),
    ("课间操场上玩", "spelen op de speelplaats"),
    ("数学课堂测验", "een proefwerk wiskunde"),
    ("报告要读三本书", "drie boeken lezen voor de spreekbeurt"),
    ("假期可以睡懒觉", "uitslapen in de vakantie"),
    ("圣诞演出的第一次排练", "de eerste repetitie voor het kerstfeest"),
    ("书包里有本子铅笔", "rugzak gepakt: schriften, pennen"),
    ("用 weil 连接两个句子（动词放句末）。", "Verbind de twee zinnen met weil (het werkwoord staat achteraan)."),
    ("weil 句动词置尾", "in een weil-zin staat het werkwoord achteraan"),
    ("ist 置尾", "ist staat achteraan"),
    ("muss 置尾", "muss staat achteraan"),
    ("liegen 置尾", "liegen staat achteraan"),
    ("判断对错。", "Juist of onjuist?"),
    ("BW 11 月 2 日复课", "Baden-Württemberg terug op 2 november"),
    ("全德假期并未都结束", "vakantie niet overal in Duitsland voorbij"),
    ("开学周有测验与报告", "proefwerken en spreekbeurten in de eerste week"),
    # P6
    ("VERTIEFUNG · 深读", "VERTIEFUNG · Verdieping"),
    ("LEVEL B2 · Pflege & Stromsteuer · 护理与电力税",
     "LEVEL B2 · Pflege & Stromsteuer · Zorg en stroomtaks"),
    ("der Angehörige 亲属 · die Pflegeversicherung 护理保险 · der Pflegedienst 护理服务机构 · die Stagnation 停滞 · der Aufschwung 复苏。",
     "der Angehörige = familielid · die Pflegeversicherung = zorgverzekering · der Pflegedienst = thuiszorgdienst · die Stagnation = stagnatie · der Aufschwung = herstel."),
    ("DIE ZAHLEN · 本周数字", "DIE ZAHLEN · Cijfers van de week"),
    ("护理：在家护理需要更多帮助——对此政界仍在争论。电力税：降多少尚未确定。两者都花钱，都关系到几乎每个家庭。",
     "Zorg thuis heeft meer hulp nodig — daarover wordt nog gedebatteerd. De verlaging van de stroomtaks staat nog open. Beide kosten geld en raken bijna elk gezin."),
    ("PRO & CONTRA · 正方与反方 — die Argumente der Debatte",
     "PRO & CONTRA · Voor en tegen — die Argumente der Debatte"),
    ("WER PFLEGT ZU HAUSE? · 谁在家护理？", "WER PFLEGT ZU HAUSE? · Wie zorgt er thuis?"),
    ("家属护理", "familiezorg"),
    ("专业上门", "thuiszorgdienst"),
    ("住养老院", "verzorgingshuis"),
    ("ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）",
     "ÜBUNGSDATEN · Oefendata — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Deze cijfers zijn een oefenvoorbeeld van de redactie om grafieken te leren lezen, geen echte enquête.)"),
    ("ÜBUNGEN · 第 6 版练习", "ÜBUNGEN · Oefeningen pagina 6"),
    ("看上面的练习图表，选出正确答案。", "Kijk naar de oefengrafiek hierboven en kies het juiste antwoord."),
    ("thuiszorgdienst 20% 第二", "thuiszorgdienst 20% is tweede"),
    ("68+20=88", "68 + 20 = 88"),
    ("养老院 12% 最小", "verzorgingshuis 12% is het kleinst"),
    ("养老院 12%", "verzorgingshuis 12%"),
    ("68+20+12=100", "68 + 20 + 12 = 100"),
    ("读第 6 版深读文章，选出正确答案。", "Lees het verdiepende artikel op pagina 6 en kies het juiste antwoord."),
    ("10 月 26 日节目讨论居家护理", "programma van 26 oktober over zorg thuis"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，600 多万人需要护理",
     "volgens het ARD-programma Hart aber fair van 26 oktober hebben meer dan zes miljoen mensen zorg nodig"),
    ("家属居家护理", "familieleden zorgen thuis"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，约 1000 万人护理亲属",
     "volgens het ARD-programma Hart aber fair van 26 oktober zorgen ongeveer tien miljoen mensen voor familieleden"),
    ("用括号里的形式填空。", "Vul in met de vorm tussen haakjes."),
    ("被动：wird + Partizip II", "passief: wird + voltooid deelwoord"),
    ("ob 引导间接疑问句", "ob leidt een indirecte vraag in"),
    ("steigen → steigt", "steigen → steigt"),
    ("sagen 过去时 sagte", "sagen in de verleden tijd: sagte"),
    ("用方框里的词填空。", "Vul in met de woorden uit het kader."),
    ("护理保险出更多钱", "de zorgverzekering moet meer betalen"),
    ("亲属居家护理", "familieleden zorgen thuis"),
    ("走出停滞", "uit de stagnatie komen"),
    ("复苏尚未自我维持", "het herstel draagt zichzelf nog niet"),
]
rep_all("content56.py", C56)

# ================= content7 (P7) =================
C7 = [
    ("SPRACHE · 语言", "SPRACHE · Taal"),
    ("BEISPIELE · 例句", "BEISPIELE · Voorbeelden"),
    ("A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所",
     "A2 → B2 · Sätze der Woche & Fehlerklinik · Zinnen van de week & foutenkliniek"),
    ("本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。",
     "Deze pagina gaat helemaal over taal: drie korte lessen, de zinnen van de week (woord voor woord uit de artikelen van dit nummer), de foutenkliniek en lezersbrieven."),
    ("被动：wird + Partizip II", "passief: wird + voltooid deelwoord"),
    ("复数：werden", "meervoud: werden"),
    ("werden + 原形表将来", "werden + infinitief voor de toekomst"),
    ("被动语态", "passief"),
    ("spät → später（19:30 最晚）", "spät → später (19.30 uur is het laatst)"),
    ("weil 引导原因", "weil geeft een reden"),
    ("weil 句动词置尾", "in een weil-zin staat het werkwoord achteraan"),
    ("länger als = 比……更长", "länger als = langer dan"),
    ("A. 比平时更长 · B. 和平时一样 · C. 比平时更短",
     "A. langer dan gewoonlijk · B. hetzelfde als gewoonlijk · C. korter dan gewoonlijk"),
    ("ob 引导间接疑问", "ob leidt een indirecte vraag in"),
    ("Es ist fraglich, ob ... = 是否还难说", "Es ist fraglich, ob ... = het is de vraag of ..."),
    ("dass 句动词置尾", "in een dass-zin staat het werkwoord achteraan"),
    ("礼貌表达观点", "een mening beleefd zeggen"),
    ("14,04 Cent = 每升 14.04 欧分", "14,04 Cent = 14,04 cent per liter"),
    ("rund 8,35 Euro = 大约省 8.35 欧元", "rund 8,35 Euro = ongeveer 8,35 euro bespaard"),
    ("Es wird gespielt. = 比赛将进行（被动）", "Es wird gespielt. = Er wordt gespeeld (passief)"),
    ("Meiner Meinung nach ... = 在我看来……", "Meiner Meinung nach ... = Naar mijn mening ..."),
    ("Ich finde, dass ... = 我觉得……", "Ich finde, dass ... = Ik vind dat ..."),
    ("Es ist fraglich, ob ... = 是否……还难说", "Es ist fraglich, ob ... = Het is de vraag of ..."),
    ("DER WERKZEUGKASTEN · 工具箱", "DER WERKZEUGKASTEN · Gereedschapskist"),
    ("LESERBRIEFE · 读者来信", "LESERBRIEFE · Lezersbrieven"),
    ("NOCH EIN WORT · 再学一词", "NOCH EIN WORT · Nog één woord"),
    ("«der Tankrabatt»（Seite 2）: die gesenkte Steuer auf Benzin und Diesel. 油价减税。",
     "«der Tankrabatt» (Seite 2): die gesenkte Steuer auf Benzin und Diesel. Brandstofkorting."),
    ("SÄTZE DER WOCHE · 本周金句", "SÄTZE DER WOCHE · Zinnen van de week"),
    ("原文摘录，逐字引自本期文章 · 括号内为出处", "Woord voor woord uit de artikelen van dit nummer"),
    ("连续四个足球之夜，然后是整周末联赛。", "Vier voetbalavonden achter elkaar, dan een heel weekend competitie."),
    ("汽油和柴油的能源税每升降低 14.04 欧分。", "De energiebelasting op benzine en diesel daalt met 14,04 cent per liter."),
    ("加 50 升油，大约省 8.35 欧元。", "Wie 50 liter tankt, bespaart ongeveer 8,35 euro."),
    ("秋假过后，学校又开学了。", "Na de herfstvakantie is de school weer begonnen."),
    ("白天短，夜晚长。", "De dagen zijn kort, de avonden lang."),
    ("德国球队的两场艰难客场之战。", "Twee zware uitwedstrijden voor de Duitse teams."),
    ("德国经济正在缓慢走出停滞，但复苏还不能自我维持。",
     "De Duitse economie komt langzaam uit de stagnatie, maar het herstel draagt zichzelf nog niet."),
    ("缓慢向好——但不会自动变好。", "Het gaat langzaam beter — maar niet vanzelf."),
    ("FEHLERKLINIK · 纠错诊所", "FEHLERKLINIK · Foutenkliniek"),
    ("学习者最常犯的四个错 · 先自己改，再看答案",
     "Vier fouten die leerders het vaakst maken · verbeter eerst zelf, kijk dan"),
    ("动词第二位：主语不在句首时，动词仍居第二。",
     "Werkwoord op plaats 2: ook als het onderwerp niet vooraan staat, blijft het werkwoord op de tweede plaats."),
    ("halb acht = 七点半（acht 之前）。", "halb acht = half acht (vóór achten)."),
    ("Perfekt 中 Partizip II 放句末。", "In de Perfekt staat het voltooid deelwoord achteraan."),
    ("ob 从句动词放句末。", "In een ob-zin staat het werkwoord achteraan."),
    ("IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.3)", "IN DER NÄCHSTEN AUSGABE · Volgend nummer (VOL.3)"),
]
rep_all("content7.py", C7)

# P7 readers box: label + two Dutch paras replacing the Chinese note.
# German defer / reader / invite strings are FROZEN and stay untouched.
rep("content7.py", 'label = "Ein Beispiel der Redaktion!"',
    'label = "Een voorbeeld van de redactie!"', 1)
OLD_RH = None
p7 = open(os.path.join(BASE, "content7.py"), encoding="utf-8").read()
for line in p7.splitlines():
    if line.startswith("rh = "):
        OLD_RH = line
        break
assert OLD_RH is not None
NEW_RH = ('rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \\\n'
          '    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
          '    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \\\n'
          '    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
          '    + len(wrap(note_nl, "sans", False, 19.5, CW - 44)) * 28 + 8 \\\n'
          '    + len(wrap(invite_nl, "serif", False, 20.5, CW - 44)) * 29.5 + 40 + 16')
rep("content7.py", OLD_RH, NEW_RH, 1)
rep("content7.py",
    'chinese = "编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.3。请寄来您的习作，优秀者刊登于 VOL.3。"',
    'note_nl = "Voorbeeld van de redactie, geen echte brief: bij het ter perse gaan waren er nog geen echte brieven en geen beste pagina-8-tekst binnen, dus de belofte schuift door naar VOL.3."\n'
    'invite_nl = "Schrijf ons! Stuur je echte brieven en je pagina-8-tekst in — de beste echte brieven drukken we af in VOL.3."', 1)
rep("content7.py",
    'p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)',
    'yy3 = p.para(ix + 22, yy3 + 19.5, note_nl, 19.5, "sans", False, GREY, CW - 44, 1.42) + 8\n'
    'p.para(ix + 22, yy3 + 20.5, invite_nl, 20.5, "serif", False, INK, CW - 44, 1.42)', 1)

# ================= content8 (P8) =================
C8 = [
    ("ÜBUNGEN & ANTWORTEN · 练习与答案", "ÜBUNGEN & ANTWORTEN · Oefeningen & antwoorden"),
    ("SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方",
     "SCHLUSSTEST · Eindtoets · Alle antwoorden staan onderaan deze pagina"),
    ("spielt（第三人称单数）", "spielt (3e persoon enkelvoud)"),
    ("beginnt（第三人称单数）", "beginnt (3e persoon enkelvoud)"),
    ("kauft（第三人称单数）", "kauft (3e persoon enkelvoud)"),
    ("schnitzt 雕刻南瓜", "schnitzt (een pompoen uithollen)"),
    ("schläft（第三人称单数）", "schläft (3e persoon enkelvoud)"),
    ("Tankrabatt 油价减税", "Tankrabatt (brandstofkorting)"),
    ("geht（第三人称单数）", "geht (3e persoon enkelvoud)"),
    ("erzählt（第三人称单数）", "erzählt (3e persoon enkelvoud)"),
    ("A · LÜCKENTEXT · 完形填空", "A · LÜCKENTEXT · Gatentekst"),
    ("选项：", "Opties:"),
    ("B · WISSENSFRAGEN · 综合问答", "B · WISSENSFRAGEN · Kennisvragen"),
    ("减税到 2026 年 12 月 31 日", "korting tot 31 december 2026"),
    ("拜仁周二客战马竞", "Bayern uit bij Atlético op dinsdag"),
    ("霍芬海姆欧联客战水晶宫", "Hoffenheim uit bij Crystal Palace in de Europa League"),
    ("BW 假期已结束", "vakantie in Baden-Württemberg voorbij"),
    ("ZEW 预期 28.1", "ZEW-verwachtingen op 28,1"),
    ("周五汉堡–门兴开轮", "Hamburg–Gladbach openen op vrijdag"),
    ("10 月 26 日节目讨论居家护理", "programma van 26 oktober over zorg thuis"),
    ("诸圣节 11 月 1 日", "Allerheiligen is op 1 november"),
    ("C · LESEVERSTEHEN · 阅读理解", "C · LESEVERSTEHEN · Leesvaardigheid"),
    ("halb acht = 7:30", "halb acht = 7.30 uur"),
    ("周二看拜仁客战马竞", "dinsdag Bayern uit bij Atlético kijken"),
    ("周六买南瓜", "zaterdag een pompoen kopen"),
    ("霍芬海姆–沙尔克周日 19:30", "Hoffenheim–Schalke op zondag om 19.30 uur"),
    ("D · SÄTZE BAUEN · 造句", "D · SÄTZE BAUEN · Zinnen bouwen"),
    ("时间状语，动词第二位", "tijdsbepaling vooraan, werkwoord op plaats 2"),
    ("主谓宾顺序", "onderwerp–werkwoord–voorwerp"),
    ("时间状语开头，动词第二位", "tijdsbepaling vooraan, werkwoord op plaats 2"),
    ("地点开头，动词第二位", "plaats vooraan, werkwoord op plaats 2"),
    ("E · ÜBERSETZEN · 翻译", "E · ÜBERSETZEN · Vertalen"),
    ("（译成中文）", ""),
    # E keys: DE->NL re-aimed (keys change language by definition);
    # the 140 key stays German, only its prompt/instr change (below).
    ('"油价减税持续到十二月。"', '"De brandstofkorting loopt tot december."'),
    ('"我周二看足球。"', '"Ik kijk op dinsdag voetbal."'),
    ('"学校又开学了。"', '"De school is weer begonnen."'),
    ("laufen = 持续", "laufen = duren"),
    ("schauen = 看", "schauen = kijken"),
    ("wieder begonnen = 又开始", "wieder begonnen = weer begonnen"),
    ("多睡一小时 = eine Stunde länger schlafen", "een uur langer slapen = eine Stunde länger schlafen"),
    ("F · WÖRTER PAAREN · 词汇配对", "F · WÖRTER PAAREN · Koppelen"),
    ("Tankrabatt=油价减税 b", "Tankrabatt = brandstofkorting b"),
    ("Pflege=护理 d", "Pflege = zorg d"),
    ("Advent=将临期 a", "Advent = advent a"),
    ("Pausenhof=课间操场 c", "Pausenhof = speelplaats c"),
    ("G · DIALOG · 对话补全", "G · DIALOG · Dialoog"),
    ("schaust（第二人称单数）", "schaust (2e persoon enkelvoud)"),
    ("siehst（第二人称单数）", "siehst (2e persoon enkelvoud)"),
    ("kochen（第一人称复数）", "kochen (1e persoon meervoud)"),
    ("machst（第二人称单数）", "machst (2e persoon enkelvoud)"),
    ("gehe（第一人称单数）", "gehe (1e persoon enkelvoud)"),
    ("开放题 — 要点见写作框，范文在第 8 版写作框内",
     "Open opdracht — zie de punten in het schrijfblok; de voorbeeldtekst staat in het schrijfblok op deze pagina"),
    ("按要点给分", "Beoordeling op basis van de punten"),
    ("H · SCHREIBEN · 写作", "H · SCHREIBEN · Schrijven"),
    ("用德语写 80–100 词：《我的足球周》。写清看哪几场比赛、和谁一起、看球时吃什么，并写一句关于油价减税或护理的话。",
     "Schrijf in het Duits 80–100 woorden: «Mijn voetbalweek». Vertel welke wedstrijden je kijkt, met wie, en wat je eet tijdens de wedstrijd — en voeg één zin toe over de brandstofkorting of de zorg. De beste teksten verschijnen in VOL.3 (pagina 7, «Lezersbrieven»)."),
    ("MUSTER · 范文（84 Wörter）", "MUSTER · Voorbeeldtekst (84 woorden)"),
    ("ANTWORTEN · 全部答案与简析（第 1–8 版）", "ANTWORTEN · Alle antwoorden met toelichting (pagina 1–8)"),
]
rep_all("content8.py", C8)
# ---------- generic value maps (bare text) ----------
TYPEMAP = [("完成句子", "invullen"), ("单选", "meerkeuze"),
           ("句型转换", "omvormen"), ("词汇配对", "koppelen"),
           ("判断对错", "juist/onjuist"), ("完形填空", "gatentekst"),
           ("造句", "zinnen bouwen"), ("对话补全", "dialoog aanvullen"),
           ("翻译", "vertalen"), ("写作", "schrijven")]
INSTRMAP = [('instr="填空"', 'instr="Vul in"'),
            ('instr="改写"', 'instr="Herschrijf"'),
            ('instr="判断"', 'instr="Beoordeel"'),
            ('instr="造句"', 'instr="Vorm de zin"'),
            ('instr="翻译"', 'instr="Vertaal naar het Nederlands"'),
            ('instr="把词和释义配对"', 'instr="Combineer"')]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTRMAP + TYPEMAP:  # instr tokens first: TYPEMAP would corrupt instr="翻译"
        pth = os.path.join(BASE, f)
        n = open(pth, encoding="utf-8").read().count(old)
        if n == 0:
            LOG.append(f"{f}: 0x {old!r} (absent, skipped)")
        else:
            rep(f, old, new)
# P8 section E: first three are DE->NL (already Vertaal naar het Nederlands
# via the generic map); the fourth is reader->DE, fix its instr + prompt.
# The generic INSTRMAP already turned instr="翻译" into Vertaal naar het
# Nederlands everywhere; fix ONLY the 140 line (unique prompt literal).
rep("content8.py", '"我周日多睡一小时。（译成德语）", instr="Vertaal naar het Nederlands"',
    '"Ik slaap op zondag een uur langer.", instr="Vertaal naar het Duits"', 1)
# P8 keys: W43 DE x NL shipped form — half-width parens, 13pt keys,
# Dutch page separators.
rep("content8.py", 'kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— Pagina {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"（{e[\'note\']}）"', 's += f"({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13, "sans", False, INK, 1.3, 9)', 1)

print("\n".join(LOG))
print(f"TOTAL replacements: {len(LOG)}")
