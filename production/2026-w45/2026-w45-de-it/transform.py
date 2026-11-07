# -*- coding: utf-8 -*-
"""DE x IT fan-out transform for W45 DE core build copy.
Rules: whole-line or exact-unique-literal replacements with count
assertions; value maps use bare text, never repr.
German body text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token. Run once from the build dir copy.
Furniture follows the shipped W43 DE x IT SVG verbatim (badge slot
y=372, 20pt bold BRICK; footer; Pagina N di 8; gloss prefix Nota — ;
P8 separators — PAGINA N —; P8 keys half-width parens, 13pt, 1.26).
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
    rep(f, "weekly-report-w45-de-core", "weekly-report-w45-de-it", 1)

# ---------- svglib docstring comment only (not rendered) ----------
rep("svglib.py", "for 重阳.", "for Double Ninth.", 1)

# ---------- bslib4: furniture + gloss prefix (W43 DE x IT shipped forms, VOL.2) ----------
rep("bslib4.py",
    '"Die Lucerna · 德语周报 VOL.2 · LUCERNA GERMAN WEEKLY"',
    '"Die Lucerna · SETTIMANALE TEDESCO VOL.2 · TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} di {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Nota — " + s', 1)

# ---------- shared furniture strings ----------
SHARED = [
    ("UND SIE? · 说说你自己", "UND SIE? · E tu?"),
    ("FERIENWECHSEL · 假期交接", "FERIENWECHSEL · Vacanze"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Risposte a pagina 8 · Cerca ogni risposta per numero"),
    ("BEISPIELE · 例句", "BEISPIELE · Esempi"),
]
for f in ["content12.py", "content34.py", "content56.py"]:
    for old, new in SHARED:
        p = os.path.join(BASE, f)
        if old in open(p, encoding="utf-8").read():
            rep(f, old, new)

# ================= content12 (P1 + P2) =================
C12 = [
    ("WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语",
     "WÖCHENTLICH AUF DEUTSCH · OGNI SETTIMANA · IL TEDESCO CHE LEGGONO I TEDESCHI"),
    ("德 语 周 报 · VOL.2 · 足 球 周 · 油 价 · 护 理",
     "SETTIMANALE TEDESCO · VOL.2 · CALCIO · SCONTO · ASSISTENZA"),
    # P1 subtitle slot -> W43 shipped badge, verbatim string, 20pt bold BRICK
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO — L\'EDIZIONE PER I LETTORI ITALIANI", 20, "sans", True, BRICK, anchor="middle")'),
    ("本周足球周 · 欧冠欧联德甲连轴转", "Settimana di calcio · Champions, Europa League, Bundesliga"),
    ("详见第 4 版 · Seite 4", "Vedi pagina 4 · Seite 4"),
    ("DIE TOPMELDUNG · 头条", "DIE TOPMELDUNG · Il titolo principale"),
    ("讲解｜die Englische Woche 一周双赛 · der Spieltag 比赛日 · empfangen 主场迎战 · die Bundesliga 德甲。",
     "Note — Englische Woche = settimana inglese · Spieltag = giornata · empfangen = ospitare · Bundesliga = Bundesliga."),
    ("DIE WOCHE IN ZAHLEN · 数字看本周", "DIE WOCHE IN ZAHLEN · In cifre"),
    ("9 — Spiele hat der 9. Spieltag der Bundesliga（德甲第 9 轮共 9 场比赛）",
     "9 — Spiele hat der 9. Spieltag der Bundesliga (9 partite, 9ª giornata)"),
    ("6 — deutsche Teams spielen in Europa（6 支德国球队出战欧战）",
     "6 — deutsche Teams spielen in Europa (6 squadre tedesche in Europa)"),
    ("14,04 — Cent pro Liter beträgt der Tankrabatt（每升油减税 14.04 欧分）",
     "14,04 — Cent pro Liter beträgt der Tankrabatt (14,04 cent in meno al litro)"),
    ("JETZT ÜBEN · 即学即练", "JETZT ÜBEN · Pratica subito"),
    ("一周双赛", "settimana inglese"),
    ("多特主场迎战贝蒂斯", "il Dortmund ospita il Betis"),
    ("欧联在周四", "Europa League di giovedì"),
    ("周五汉堡–门兴开轮", "Amburgo–Gladbach aprono venerdì"),
    ("第 9 轮共 9 场", "9 partite nella 9ª giornata"),
    ("减税到 12 月 31 日", "sconto fino al 31 dicembre"),
    ("拜仁周二客战马竞", "il Bayern in trasferta dall'Atlético martedì"),
    ("霍芬海姆欧联客战水晶宫", "l'Hoffenheim in Europa League dal Crystal Palace"),
    ("本周大问题 · Die Fragen der Woche", "Le grandi domande · Die Fragen der Woche"),
    ("德国本周最热议的五个问题。", "Le cinque domande della Germania."),
    ("IN DIESER AUSGABE · 本期目录", "IN DIESER AUSGABE · Sommario"),
    ("油价减税（加油折扣）。详见第 2 版。", "Sconto sul carburante. Vedi pagina 2."),
    ("KURZ & GUT · 快讯", "KURZ & GUT · In breve"),
    ("BLITZQUIZ · 闪电问答", "BLITZQUIZ · Quiz lampo"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Leggi la prima pagina e scegli la risposta giusta · Risposte a pagina 8"),
    # P2
    ("LEBEN · 生活", "LEBEN · Vita quotidiana"),
    ("LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · 油价、电力税与护理",
     "LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · Sconto carburante, tassa elettrica e assistenza"),
    ("der Tankrabatt 油价减税 · die Zapfsäule 加油机 · die Energiesteuer 能源税 · die Mehrwertsteuer 增值税 · der Angehörige 亲属。",
     "der Tankrabatt = sconto sul carburante · die Zapfsäule = pompa di benzina · die Energiesteuer = tassa sull'energia · die Mehrwertsteuer = IVA · der Angehörige = familiare."),
    ("AN DER ZAPFSÄULE · 加油机旁", "AN DER ZAPFSÄULE · Alla pompa"),
    ("你开车吗？你那里的油价是多少？写两句德语寄来。",
     "Guidi? Quanto costa la benzina da te? Scrivi due frasi in tedesco!"),
    ("ZEW IN KÜRZE · ZEW 指数简讯", "ZEW IN KÜRZE · ZEW in breve"),
    ("RECHNEN WIR MAL · 算一算", "RECHNEN WIR MAL · Facciamo i conti"),
    ("Die Zahlen der Woche · 本周数字", "Die Zahlen der Woche · I numeri della settimana"),
    ("注意：减的是税，定价的是油站。出发前比比价。",
     "Attenzione: cala la tassa, ma il prezzo lo fa il distributore. Confronta i prezzi prima di fare benzina!"),
    ("ÜBUNGEN · 第 2 版练习", "ÜBUNGEN · Esercizi della pagina 2"),
    ("看第 2 版文章，用数字填空。", "Leggi l'articolo di pagina 2 e completa con i numeri."),
    ("每升减税 14.04 欧分", "14,04 cent di tasse in meno al litro"),
    ("50 升省约 8.35 欧元", "circa 8,35 euro risparmiati con 50 litri"),
    ("减税到 2026 年底", "sconto fino alla fine del 2026"),
    ("国家少收约 25 亿欧元", "lo Stato rinuncia a circa 2,5 miliardi di euro"),
    ("加油机旁的实际降幅", "il calo effettivo alla pompa"),
    ("改成 Perfekt 现在完成时。", "Trasforma al Perfekt."),
    ("beschließen → beschlossen", "beschließen → beschlossen"),
    ("fallen 用 sein", "fallen va con sein"),
    ("tanken → getankt", "tanken → getankt"),
    ("weitergeben 可分动词", "weitergeben è separabile"),
    ("ZEW 预期下降", "le attese ZEW sono calate"),
    ("读第 2 版文章，选出正确答案。", "Leggi l'articolo di pagina 2 e scegli la risposta giusta."),
    ("减的是能源税", "cala la tassa sull'energia"),
    ("油站定价", "il distributore fa il prezzo"),
    ("联盟党与社民党", "Unione e SPD"),
    ("家属居家护理", "i familiari assistono a casa"),
    ("Tankrabatt=油价减税 b", "Tankrabatt = sconto sul carburante b"),
    ("Zapfsäule=加油机 d", "Zapfsäule = pompa di benzina d"),
    ("Mehrwertsteuer=增值税 a", "Mehrwertsteuer = IVA a"),
    ("Angehörige=亲属 c", "Angehörige = familiare c"),
]
rep_all("content12.py", C12)

# ================= content34 (P3 + P4) =================
C34 = [
    ("KULTUR · 文化", "KULTUR · Cultura"),
    ("A2 → B1 · Ferienwechsel & Herbst · 假期交接与秋天",
     "A2 → B1 · Ferienwechsel & Herbst · Cambio di vacanze e autunno"),
    ("der Ferienwechsel 假期交接 · die Schülerin 女学生 · der Ausflug 短途出游 · der Advent 将临期 · die Lesung 朗读会。",
     "der Ferienwechsel = cambio di vacanze · die Schülerin = studentessa · der Ausflug = gita · der Advent = Avvento · die Lesung = lettura."),
    ("der Nebel — 雾", "der Nebel — nebbia"),
    ("das Laub — 落叶", "das Laub — foglie cadute"),
    ("der Kürbis — 南瓜", "der Kürbis — zucca"),
    ("die Kerze — 蜡烛", "die Kerze — candela"),
    ("der Spaziergang — 散步", "der Spaziergang — passeggiata"),
    ("die Lesung — 朗读会", "die Lesung — lettura"),
    ("HERBSTWÖRTER · 秋天词汇", "HERBSTWÖRTER · Autunno"),
    ("秋天你比夏天读得多吗？你的床头现在放着哪本书？写两句德语寄来。",
     "In autunno leggi più che in estate? Che libro hai sul comodino? Scrivi due frasi in tedesco!"),
    ("DER TIPP · 编辑部建议", "DER TIPP · Il consiglio"),
    ("ÜBUNGEN · 第 3 版练习", "ÜBUNGEN · Esercizi della pagina 3"),
    ("读第 3 版文章，判断对错。", "Leggi l'articolo di pagina 3. Vero o falso?"),
    ("BW 周一起复课", "il Baden-Württemberg ricomincia lunedì"),
    ("巴伐利亚本周仍在放假", "la Baviera è ancora in vacanza questa settimana"),
    ("诸圣节 11 月 1 日", "Ognissanti è il 1° novembre"),
    ("10 月 31 日也是宗教改革日（九个州）", "il 31 ottobre è anche la Giornata della Riforma (nove Stati)"),
    ("诸圣节商店关门", "i negozi chiudono a Ognissanti"),
    ("用方框里的词填空。", "Completa con le parole del riquadro."),
    ("假期交接", "cambio di vacanze"),
    ("去山区短途出游", "una gita in montagna"),
    ("图书馆的朗读会", "una lettura in biblioteca"),
    ("将临期在 11 月筹划", "l'Avvento si prepara a novembre"),
    ("湖面上的雾", "la nebbia sul lago"),
    ('e.bridge("选出正确答案。")', 'e.bridge("Scegli la risposta giusta.")'),
    ("BW 假期已结束", "le vacanze nel Baden-Württemberg sono finite"),
    ("安静的节日", "una festa tranquilla"),
    ("诸圣节扫墓", "visitare le tombe a Ognissanti"),
    ("白天短所以夜晚长", "giorni corti, quindi sere lunghe"),
    ("把词组成正确的句子。", "Ordina le parole e forma frasi corrette."),
    ("时间地点开头，动词第二位", "tempo e luogo all'inizio, verbo in seconda posizione"),
    ("数量时间状语，动词第二位", "indicazione di tempo all'inizio, verbo in seconda posizione"),
    ("主谓宾顺序", "ordine soggetto–verbo–oggetto"),
    ("bleiben + geschlossen", "bleiben + geschlossen"),
    # P4
    ("SPORT · 体育", "SPORT · Sport"),
    ("LEVEL B1 · Europapokal & Bundesliga · 欧战与德甲",
     "LEVEL B1 · Europapokal & Bundesliga · Coppe europee e Bundesliga"),
    ("die Englische Woche 一周双赛 · auswärts 客场 · empfangen 主场迎战 · der Favorit 夺冠热门 · eröffnen 揭开序幕。",
     "die Englische Woche = settimana inglese · auswärts = in trasferta · empfangen = ospitare · der Favorit = favorito · eröffnen = aprire."),
    ("本周你支持谁？周六焦点战谁赢？写两句德语寄给编辑部。",
     "Per chi tifi questa settimana? Chi vince la partita clou di sabato? Scrivi due frasi in tedesco!"),
    ("DER 9. SPIELTAG · 第 9 轮赛程", "DER 9. SPIELTAG · Le partite della 9ª giornata"),
    ("ÜBUNGEN · 第 4 版练习", "ÜBUNGEN · Esercizi della pagina 4"),
    ("读第 4 版文章，选出正确答案。", "Leggi l'articolo di pagina 4 e scegli la risposta giusta."),
    ("拜仁周二客战马竞", "il Bayern in trasferta dall'Atlético martedì"),
    ("斯图加特 18:45 开球", "lo Stoccarda inizia alle 18:45"),
    ("多特主场迎战贝蒂斯", "il Dortmund ospita il Betis"),
    ("霍芬海姆欧联客战水晶宫", "l'Hoffenheim in Europa League dal Crystal Palace"),
    ("周六焦点战斯图加特–不来梅", "la partita clou di sabato è Stoccarda–Brema"),
    ("Englische Woche=一周双赛 a", "Englische Woche = settimana inglese a"),
    ("auswärts=客场 b", "auswärts = in trasferta b"),
    ("Favorit=热门 c", "Favorit = favorito c"),
    ("eröffnen=揭开序幕 d", "eröffnen = aprire d"),
    ("用比较级完成句子（括号里是原级）。", "Completa con il comparativo (tra parentesi c'è il positivo)."),
    ("schwer → schwerer", "schwer → schwerer"),
    ("spät → später（19:30 最晚）", "spät → später (le 19:30 sono le più tardi)"),
    ("viel → mehr（球迷想要更多）", "viel → mehr (i tifosi vogliono di più)"),
    ("früh → früher（18:45 早于 21:00）", "früh → früher (le 18:45 sono prima delle 21:00)"),
    ("看上面的赛程表，选出正确答案。", "Guarda la tabella delle partite qui sopra e scegli la risposta giusta."),
    ("汉堡–门兴周五 20:30", "Amburgo–Gladbach venerdì alle 20:30"),
    ("斯图加特–不来梅周六 18:30", "Stoccarda–Brema sabato alle 18:30"),
    ("霍芬海姆–沙尔克周日 19:30", "Hoffenheim–Schalke domenica alle 19:30"),
    ("弗赖堡–柏林联周日 17:30", "Friburgo–Union domenica alle 17:30"),
    ("欧联周四霍芬海姆 18:45", "Europa League giovedì, Hoffenheim alle 18:45"),
]
rep_all("content34.py", C34)

# ================= content56 (P5 + P6) =================
C56 = [
    ("JUGEND · 青年", "JUGEND · Giovani"),
    ("LEVEL B1 · Zurück in die Schule · 重返校园",
     "LEVEL B1 · Zurück in die Schule · Ritorno a scuola"),
    ("der Pausenhof 课间操场 · die Klassenarbeit 课堂测验 · das Referat 课堂报告 · ausschlafen 睡懒觉 · die Probe 排练。",
     "der Pausenhof = cortile della scuola · die Klassenarbeit = compito in classe · das Referat = relazione · ausschlafen = dormire fino a tardi · die Probe = prova."),
    ("der Pausenhof — 课间操场", "der Pausenhof — cortile della scuola"),
    ("die Klassenarbeit — 课堂测验", "die Klassenarbeit — compito in classe"),
    ("das Referat — 课堂报告", "das Referat — relazione"),
    ("der Rucksack — 书包", "der Rucksack — zaino"),
    ("ausschlafen — 睡懒觉", "ausschlafen — dormire fino a tardi"),
    ("die Probe — 排练", "die Probe — prova"),
    ("SCHULWÖRTER · 校园词汇", "SCHULWÖRTER · Scuola"),
    ("你的学校假期后哪天开学？第一节是什么课？写两句德语寄来。",
     "Quando è ricominciata la tua scuola dopo le vacanze? Qual è stata la prima lezione? Scrivi due frasi in tedesco!"),
    ("DER WOCHENPLAN DER REDAKTION · 编辑部一周计划",
     "DER WOCHENPLAN DER REDAKTION · Il piano della redazione"),
    ("ÜBUNGEN · 第 5 版练习", "ÜBUNGEN · Esercizi della pagina 5"),
    ("读第 5 版文章，选出正确答案。", "Leggi l'articolo di pagina 5 e scegli la risposta giusta."),
    ("BW 11 月 2 日开学", "il Baden-Württemberg ricomincia il 2 novembre"),
    ("巴伐利亚假期未结束", "le vacanze in Baviera non sono finite"),
    ("开学周有课堂测验", "compiti in classe nella prima settimana"),
    ("Referat = 课堂报告", "Referat = relazione"),
    ("巴伐利亚学生周五可去球场", "gli studenti bavaresi possono andare allo stadio venerdì"),
    ("课间操场上玩", "giocare nel cortile della scuola"),
    ("数学课堂测验", "un compito in classe di matematica"),
    ("报告要读三本书", "tre libri da leggere per la relazione"),
    ("假期可以睡懒觉", "dormire fino a tardi in vacanza"),
    ("圣诞演出的第一次排练", "la prima prova per la festa di Natale"),
    ("书包里有本子铅笔", "zaino pronto: quaderni, penne"),
    ("用 weil 连接两个句子（动词放句末）。", "Unisci le due frasi con weil (il verbo va alla fine)."),
    ("weil 句动词置尾", "con weil il verbo va alla fine"),
    ("ist 置尾", "ist va alla fine"),
    ("muss 置尾", "muss va alla fine"),
    ("liegen 置尾", "liegen va alla fine"),
    ("判断对错。", "Vero o falso?"),
    ("BW 11 月 2 日复课", "il Baden-Württemberg ricomincia il 2 novembre"),
    ("全德假期并未都结束", "le vacanze non sono finite in tutta la Germania"),
    ("开学周有测验与报告", "compiti e relazioni nella prima settimana"),
    # P6
    ("VERTIEFUNG · 深读", "VERTIEFUNG · Approfondimento"),
    ("LEVEL B2 · Pflege & Stromsteuer · 护理与电力税",
     "LEVEL B2 · Pflege & Stromsteuer · Assistenza e tassa elettrica"),
    ("der Angehörige 亲属 · die Pflegeversicherung 护理保险 · der Pflegedienst 护理服务机构 · die Stagnation 停滞 · der Aufschwung 复苏。",
     "der Angehörige = familiare · die Pflegeversicherung = assicurazione per l'assistenza · der Pflegedienst = servizio di assistenza · die Stagnation = stagnazione · der Aufschwung = ripresa."),
    ("DIE ZAHLEN · 本周数字", "DIE ZAHLEN · Numeri"),
    ("护理：在家护理需要更多帮助——对此政界仍在争论。电力税：降多少尚未确定。两者都花钱，都关系到几乎每个家庭。",
     "Assistenza: chi assiste a casa ha bisogno di più aiuto — la politica ne discute ancora. Tassa elettrica: di quanto calerà non è ancora deciso. Entrambe costano e riguardano quasi ogni famiglia."),
    ("PRO & CONTRA · 正方与反方 — die Argumente der Debatte",
     "PRO & CONTRA · Pro e contro — die Argumente der Debatte"),
    ("WER PFLEGT ZU HAUSE? · 谁在家护理？", "WER PFLEGT ZU HAUSE? · Chi assiste a casa?"),
    # longer ex-note strings FIRST: bare chart labels are substrings of them
    ("68% 家属护理", "68% in famiglia"),
    ("专业上门 20% 第二", "servizio 20% secondo"),
    ("养老院 12% 最小", "in istituto 12% minimo"),
    ("家属护理", "in famiglia"),
    ("专业上门", "servizio"),
    ("住养老院", "in istituto"),
    ("ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）",
     "ÜBUNGSDATEN · Dati per esercitarsi — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Esempio della redazione, non un vero sondaggio.)"),
    ("ÜBUNGEN · 第 6 版练习", "ÜBUNGEN · Esercizi della pagina 6"),
    ("看上面的练习图表，选出正确答案。", "Guarda il grafico per esercitarsi qui sopra e scegli la risposta giusta."),
    ("68+20=88", "68 + 20 = 88"),
    ("养老院 12%", "in istituto 12%"),
    ("68+20+12=100", "68 + 20 + 12 = 100"),
    ("读第 6 版深读文章，选出正确答案。", "Leggi l'articolo di approfondimento di pagina 6 e scegli la risposta giusta."),
    ("10 月 26 日节目讨论居家护理", "il programma del 26 ottobre ha discusso l'assistenza a casa"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，600 多万人需要护理",
     "secondo il programma ARD Hart aber fair del 26 ottobre, oltre sei milioni di persone hanno bisogno di assistenza"),
    ("家属居家护理", "i familiari assistono a casa"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，约 1000 万人护理亲属",
     "secondo il programma ARD Hart aber fair del 26 ottobre, circa dieci milioni di persone assistono familiari"),
    ("用括号里的形式填空。", "Completa con la forma tra parentesi."),
    ("被动：wird + Partizip II", "passivo: wird + Partizip II"),
    ("ob 引导间接疑问句", "ob introduce una domanda indiretta"),
    ("steigen → steigt", "steigen → steigt"),
    ("sagen 过去时 sagte", "sagen al passato: sagte"),
    ("用方框里的词填空。", "Completa con le parole del riquadro."),
    ("护理保险出更多钱", "l'assicurazione per l'assistenza dovrebbe pagare di più"),
    ("亲属居家护理", "i familiari assistono a casa"),
    ("走出停滞", "uscire dalla stagnazione"),
    ("复苏尚未自我维持", "la ripresa non si regge ancora da sola"),
]
rep_all("content56.py", C56)

# ================= content7 (P7) =================
C7 = [
    ("SPRACHE · 语言", "SPRACHE · Lingua"),
    ("A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所",
     "A2 → B2 · Sätze der Woche & Fehlerklinik · Frasi della settimana e clinica degli errori"),
    ("本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。",
     "Questa pagina è tutta dedicata alla lingua: tre brevi lezioni, le frasi della settimana (citate parola per parola dagli articoli di questo numero), la clinica degli errori e le lettere dei lettori."),
    ("被动：wird + Partizip II", "passivo: wird + Partizip II"),
    ("复数：werden", "plurale: werden"),
    ("werden + 原形表将来", "werden + infinito per il futuro"),
    ("被动语态", "voce passiva"),
    ("spät → später（19:30 最晚）", "spät → später (le 19:30 sono le più tardi)"),
    ("weil 引导原因", "weil introduce la causa"),
    ("weil 句动词置尾", "con weil il verbo va alla fine"),
    ("länger als = 比……更长", "länger als = più lungo di"),
    ("A. 比平时更长 · B. 和平时一样 · C. 比平时更短",
     "A. più lungo del solito · B. come al solito · C. più corto del solito"),
    ("ob 引导间接疑问", "ob introduce una domanda indiretta"),
    ("Es ist fraglich, ob ... = 是否还难说", "Es ist fraglich, ob ... = non è chiaro se ..."),
    ("dass 句动词置尾", "con dass il verbo va alla fine"),
    ("礼貌表达观点", "esprimere un'opinione con cortesia"),
    ("14,04 Cent = 每升 14.04 欧分", "14,04 Cent = 14,04 cent al litro"),
    ("rund 8,35 Euro = 大约省 8.35 欧元", "rund 8,35 Euro = circa 8,35 euro"),
    ("Es wird gespielt. = 比赛将进行（被动）", "Es wird gespielt. = si giocherà (passivo)"),
    ("Meiner Meinung nach ... = 在我看来……", "Meiner Meinung nach ... = secondo me"),
    ("Ich finde, dass ... = 我觉得……", "Ich finde, dass ... = penso che ..."),
    ("Es ist fraglich, ob ... = 是否……还难说", "Es ist fraglich, ob ... = non è chiaro se"),
    ("DER WERKZEUGKASTEN · 工具箱", "DER WERKZEUGKASTEN · Gli utili"),
    ("LESERBRIEFE · 读者来信", "LESERBRIEFE · Le vostre lettere"),
    ("NOCH EIN WORT · 再学一词", "NOCH EIN WORT · Una parola in più"),
    ("«der Tankrabatt»（Seite 2）: die gesenkte Steuer auf Benzin und Diesel. 油价减税。",
     "«der Tankrabatt» (Seite 2): die gesenkte Steuer auf Benzin und Diesel. Sconto sul carburante."),
    ("SÄTZE DER WOCHE · 本周金句", "SÄTZE DER WOCHE · Frasi della settimana"),
    ("原文摘录，逐字引自本期文章 · 括号内为出处", "Citazioni letterali dagli articoli di questo numero · la fonte tra parentesi"),
    ("连续四个足球之夜，然后是整周末联赛。", "Quattro serate di calcio di fila, poi un intero fine settimana di campionato."),
    ("汽油和柴油的能源税每升降低 14.04 欧分。", "La tassa sull'energia per benzina e diesel cala di 14,04 cent al litro."),
    ("加 50 升油，大约省 8.35 欧元。", "Con 50 litri si risparmiano circa 8,35 euro."),
    ("秋假过后，学校又开学了。", "Dopo le vacanze autunnali la scuola è ricominciata."),
    ("白天短，夜晚长。", "I giorni sono corti, le sere lunghe."),
    ("德国球队的两场艰难客场之战。", "Due difficili trasferte per le squadre tedesche."),
    ("德国经济正在缓慢走出停滞，但复苏还不能自我维持。",
     "L'economia tedesca esce lentamente dalla stagnazione, ma la ripresa non regge da sola."),
    ("缓慢向好——但不会自动变好。", "Va lentamente meglio — ma non da sola."),
    ("FEHLERKLINIK · 纠错诊所", "FEHLERKLINIK · Clinica degli errori"),
    ("学习者最常犯的四个错 · 先自己改，再看答案",
     "I quattro errori più frequenti · Correggili prima tu, poi guarda la risposta"),
    ("动词第二位：主语不在句首时，动词仍居第二。",
     "Verbo in seconda posizione: anche se il soggetto non è all'inizio, il verbo resta secondo."),
    ("halb acht = 七点半（acht 之前）。", "halb acht = le sette e mezza (prima di acht)."),
    ("Perfekt 中 Partizip II 放句末。", "Nel Perfekt il Partizip II va alla fine."),
    ("ob 从句动词放句末。", "Nella frase con ob il verbo va alla fine."),
    ("IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.3)", "IN DER NÄCHSTEN AUSGABE · Nel prossimo numero (VOL.3)"),
]
rep_all("content7.py", C7)

# P7 readers box: label + two Italian paras replacing the Chinese note.
# German defer / reader / invite strings are FROZEN and stay untouched.
rep("content7.py", 'label = "Ein Beispiel der Redaktion!"',
    'label = "Un esempio della redazione!"', 1)
p7 = open(os.path.join(BASE, "content7.py"), encoding="utf-8").read()
_lines = p7.splitlines()
_i = next(i for i, ln in enumerate(_lines) if ln.startswith("rh = "))
OLD_RH = "\n".join(_lines[_i:_i + 5])
assert OLD_RH.count("wrap(chinese") == 1, OLD_RH
NEW_RH = ('rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \\n'
          '    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\n'
          '    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \\n'
          '    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\n'
          '    + len(wrap(note_it, "sans", False, 19.5, CW - 44)) * 28 + 8 \\n'
          '    + len(wrap(invite_it, "serif", False, 20.5, CW - 44)) * 29.5 + 40 + 32')
rep("content7.py", OLD_RH, NEW_RH, 1)
rep("content7.py",
    'chinese = "编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.3。请寄来您的习作，优秀者刊登于 VOL.3。"',
    'note_it = "Nessuna lettera vera, nessun miglior testo di pagina 8; tutto rinviato a VOL.3."\n'
    'invite_it = "Scriveteci! Mandateci lettere vere e testi di pagina 8: i migliori in VOL.3."', 1)
rep("content7.py",
    'p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)',
    'yy3 = p.para(ix + 22, yy3 + 19.5, note_it, 19.5, "sans", False, GREY, CW - 44, 1.42) + 8\n'
    'p.para(ix + 22, yy3 + 20.5, invite_it, 20.5, "serif", False, INK, CW - 44, 1.42)', 1)

# ================= content8 (P8) =================
# E-section full lines FIRST (they contain the type token 翻译, handled
# here so the generic map never corrupts instr="翻译").
rep("content8.py",
    'bf.ex("A2", "翻译", "油价减税持续到十二月。", "laufen = 持续",\n      "Der Tankrabatt läuft bis Dezember.（译成中文）", instr="翻译", size=19.5, gap=8)',
    'bf.ex("A2", "traduzione", "Lo sconto sul carburante dura fino a dicembre.", "laufen = durare",\n      "Der Tankrabatt läuft bis Dezember.", instr="Traduci in italiano", size=19.5, gap=8)', 1)
rep("content8.py",
    'bf.ex("A2", "翻译", "我周二看足球。", "schauen = 看",\n      "Ich schaue am Dienstag Fußball.（译成中文）", instr="翻译", size=19.5, gap=8)',
    'bf.ex("A2", "traduzione", "Guardo il calcio di martedì.", "schauen = guardare",\n      "Ich schaue am Dienstag Fußball.", instr="Traduci in italiano", size=19.5, gap=8)', 1)
rep("content8.py",
    'bf.ex("B1", "翻译", "学校又开学了。", "wieder begonnen = 又开始",\n      "Die Schule hat wieder begonnen.（译成中文）", instr="翻译", size=19.5, gap=8)',
    'bf.ex("B1", "traduzione", "La scuola è ricominciata.", "wieder begonnen = ricominciato",\n      "Die Schule hat wieder begonnen.", instr="Traduci in italiano", size=19.5, gap=8)', 1)
# Reverse item 140: key STAYS German; only prompt + instr re-aim to Italian.
rep("content8.py",
    'bf.ex("B1", "翻译", "Am Sonntag schlafe ich eine Stunde länger.", "多睡一小时 = eine Stunde länger schlafen",\n      "我周日多睡一小时。（译成德语）", instr="翻译", size=19.5, gap=8)',
    'bf.ex("B1", "traduzione", "Am Sonntag schlafe ich eine Stunde länger.", "dormire un\'ora in più = eine Stunde länger schlafen",\n      "Domenica dormo un\'ora in più.", instr="Traduci in tedesco", size=19.5, gap=8)', 1)
C8 = [
    ("ÜBUNGEN & ANTWORTEN · 练习与答案", "ÜBUNGEN & ANTWORTEN · Esercizi e risposte"),
    ("SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方",
     "SCHLUSSTEST · Prova finale · Tutte le risposte in fondo a questa pagina"),
    ("spielt（第三人称单数）", "spielt (terza persona singolare)"),
    ("beginnt（第三人称单数）", "beginnt (terza persona singolare)"),
    ("kauft（第三人称单数）", "kauft (terza persona singolare)"),
    ("schnitzt 雕刻南瓜", "schnitzt = intagliare la zucca"),
    ("schläft（第三人称单数）", "schläft (terza persona singolare)"),
    ("Tankrabatt 油价减税", "Tankrabatt = sconto sul carburante"),
    ("geht（第三人称单数）", "geht (terza persona singolare)"),
    ("erzählt（第三人称单数）", "erzählt (terza persona singolare)"),
    ("A · LÜCKENTEXT · 完形填空", "A · LÜCKENTEXT · Testo a buchi"),
    ("选项：", "Opzioni:"),
    ("B · WISSENSFRAGEN · 综合问答", "B · WISSENSFRAGEN · Quiz"),
    ("减税到 2026 年 12 月 31 日", "sconto fino al 31 dicembre 2026"),
    ("拜仁周二客战马竞", "il Bayern in trasferta dall'Atlético martedì"),
    ("霍芬海姆欧联客战水晶宫", "l'Hoffenheim in Europa League dal Crystal Palace"),
    ("BW 假期已结束", "le vacanze nel Baden-Württemberg sono finite"),
    ("ZEW 预期 28.1", "le attese ZEW a 28,1"),
    ("周五汉堡–门兴开轮", "Amburgo–Gladbach aprono venerdì"),
    ("10 月 26 日节目讨论居家护理", "il programma del 26 ottobre ha discusso l'assistenza a casa"),
    ("诸圣节 11 月 1 日", "Ognissanti è il 1° novembre"),
    ("C · LESEVERSTEHEN · 阅读理解", "C · LESEVERSTEHEN · Lettura"),
    ("halb acht = 7:30", "halb acht = 7:30"),
    ("周二看拜仁客战马竞", "guardare il Bayern in trasferta dall'Atlético martedì"),
    ("周六买南瓜", "comprare una zucca sabato"),
    ("霍芬海姆–沙尔克周日 19:30", "Hoffenheim–Schalke domenica alle 19:30"),
    ("D · SÄTZE BAUEN · 造句", "D · SÄTZE BAUEN · Costruisci frasi"),
    ("时间状语，动词第二位", "indicazione di tempo all'inizio, verbo in seconda posizione"),
    ("主谓宾顺序", "ordine soggetto–verbo–oggetto"),
    ("时间状语开头，动词第二位", "indicazione di tempo all'inizio, verbo in seconda posizione"),
    ("地点开头，动词第二位", "luogo all'inizio, verbo in seconda posizione"),
    ("E · ÜBERSETZEN · 翻译", "E · ÜBERSETZEN · Traduzione"),
    ("F · WÖRTER PAAREN · 词汇配对", "F · WÖRTER PAAREN · Le coppie"),
    ("Tankrabatt=油价减税 b", "Tankrabatt = sconto sul carburante b"),
    ("Pflege=护理 d", "Pflege = assistenza d"),
    ("Advent=将临期 a", "Advent = Avvento a"),
    ("Pausenhof=课间操场 c", "Pausenhof = cortile della scuola c"),
    ("G · DIALOG · 对话补全", "G · DIALOG · Completa il dialogo"),
    ("schaust（第二人称单数）", "schaust (seconda persona singolare)"),
    ("siehst（第二人称单数）", "siehst (seconda persona singolare)"),
    ("kochen（第一人称复数）", "kochen (prima persona plurale)"),
    ("machst（第二人称单数）", "machst (seconda persona singolare)"),
    ("gehe（第一人称单数）", "gehe (prima persona singolare)"),
    ("开放题 — 要点见写作框，范文在第 8 版写作框内",
     "Domanda aperta — segui i punti del riquadro di scrittura; il testo modello è nel riquadro di questa pagina"),
    ("按要点给分", "Si valuta secondo i punti indicati"),
    ("H · SCHREIBEN · 写作", "H · SCHREIBEN · Scrittura"),
    ("用德语写 80–100 词：《我的足球周》。写清看哪几场比赛、和谁一起、看球时吃什么，并写一句关于油价减税或护理的话。",
     "Scrivi in tedesco 80–100 parole: «La mia settimana di calcio». Racconta quali partite guardi, con chi, e cosa mangi durante la partita — e aggiungi una frase sullo sconto sul carburante o sull'assistenza."),
    ("MUSTER · 范文（84 Wörter）", "MUSTER · Testo modello (84 parole)"),
    ("ANTWORTEN · 全部答案与简析（第 1–8 版）", "ANTWORTEN · TUTTE LE RISPOSTE CON NOTE (PAGINE 1–8)"),
]
rep_all("content8.py", C8)
# ---------- generic value maps (bare text) ----------
# instr tokens FIRST: TYPEMAP would otherwise corrupt instr="造句".
TYPEMAP = [("完成句子", "completare"), ("单选", "scelta multipla"),
           ("句型转换", "trasformazione"), ("词汇配对", "abbinamento"),
           ("判断对错", "vero/falso"), ("完形填空", "testo a buchi"),
           ("造句", "costruire frasi"), ("对话补全", "completare il dialogo"),
           ("写作", "scrittura")]
INSTRMAP = [('instr="填空"', 'instr="Completa"'),
            ('instr="改写"', 'instr="Riscrivi"'),
            ('instr="判断"', 'instr="Vero o falso?"'),
            ('instr="造句"', 'instr="Costruisci la frase"'),
            ('instr="把词和释义配对"', 'instr="Abbina le coppie"')]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTRMAP + TYPEMAP:
        pth = os.path.join(BASE, f)
        n = open(pth, encoding="utf-8").read().count(old)
        if n == 0:
            LOG.append(f"{f}: 0x {old!r} (absent, skipped)")
        else:
            rep(f, old, new)
# P8 keys: W43 DE x IT shipped form — half-width parens, 13pt keys,
# Italian page separators.
rep("content8.py", 'kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— PAGINA {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"（{e[\'note\']}）"', 's += f" ({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)', 1)

print("\n".join(LOG))
print(f"TOTAL replacements: {len(LOG)}")
