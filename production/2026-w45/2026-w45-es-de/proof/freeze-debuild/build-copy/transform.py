# -*- coding: utf-8 -*-
"""W45 ES core -> ES x DE fan-out transform (assertion-checked literal replacements).

Rules honoured here (tools/README #17/#18):
- line-based / exact-literal splicing only, never AST byte offsets;
- `type` arguments of ex()/match_set() are INTERNAL registry keys and stay
  byte-identical (W43 es-de KIT §4: page/level/type diff = 0); only rendered
  strings (instr, bridges, notes, heads, boxes, gloss) are translated;
- P8 answer-generation code is NOT touched (dash family, "— PÁGINA N —"
  separators as shipped in W43 es-de);
- badge follows the W43 es-de shipped precedent (y=574, 22pt BRICK below the
  dark band, strapline kept) -- see WEEKLY-KIT.md §6 for the README #20
  discrepancy note (README claims a 372/19.5pt slot; the shipped DE edition
  inserts at 574/22pt).
Run: ./venv/bin/python transform.py  (from the tools dir, or python3 here)
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# (old, new) -- applied in order; bridges/heads first, instr= last so that
# bare CJK fragments inside bridges are not clobbered by instr replacement.
PAIRS = {
"bslib4.py": [
    ('"La Lucerna · 西班牙语周报 VOL.2 · LUCERNA SPANISH WEEKLY"',
     '"La Lucerna · SPANISCHE WOCHENZEITUNG VOL.2 · TEXT AUF SPANISCH · ERKLÄRUNGEN AUF DEUTSCH"'),
    ('f"第 {n} 版 / 共 {total} 版"', 'f"Seite {n} von {total}"'),
    ('("译注｜" + s', '("HINWEIS · " + s'),
],
"content12.py": [
    ('"CADA SEMANA EN ESPAÑOL · 每周一期 · 读西班牙人正在读的西班牙语"',
     '"CADA SEMANA EN ESPAÑOL · JEDE WOCHE · SPANISCH, WIE SPANIEN ES LIEST"'),
    # 46pt German edition line would ink to x=1913.9, crossing the inner frame
    # (1910); 45pt keeps every word and clears it (1893.5). See KIT §6.
    ('p.text(975, 330, "西 班 牙 语 周 报 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL", 46,',
     'p.text(975, 330, "SPANISCHE WOCHENZEITUNG · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL", 45,'),
    ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)\n\n# band',
     'p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)\np.text(975, 574, "SPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", 22, "sans", True, BRICK, anchor="middle")\n\n# band'),
    ('"距大选还有 27 天 · 住房决定选战"', '"NOCH 27 TAGE BIS ZUR WAHL · DIE WOHNUNG ENTSCHEIDET"'),
    ('"本期头条 · 详见第 2、6 版"', '"TITELTHEMA · SEITEN 2 UND 6"'),
    ('"LA NOTICIA · 头条"', '"LA NOTICIA · SCHLAGZEILE"'),
    ('"讲解｜la cuenta atrás 倒计时 · disolver las Cortes 解散议会 · el decreto 法令 · la candidatura 候选人名单。"',
     '"Hinweis · la cuenta atrás der Countdown · disolver las Cortes das Parlament auflösen · el decreto das Dekret · la candidatura die Kandidatenliste."'),
    ('"LA SEMANA EN CIFRAS · 数字看本周"', '"LA SEMANA EN CIFRAS · ZAHLEN"'),
    ('"27 — días faltan el lunes 2 para las elecciones del domingo 29（距 29 日大选 27 天）"',
     '"27 — días faltan el lunes 2 para las elecciones del domingo 29 (noch 27 Tage bis zur Wahl am 29.)"'),
    ('"9 — comunidades donde el lunes 2 de noviembre es fiesta（11 月 2 日放假的自治区）"',
     '"9 — comunidades donde el lunes 2 de noviembre es fiesta (Regionen mit Feiertag am 2. November)"'),
    ('"55,7 — % que cita la vivienda como el principal problema, según el CIS de octubre（CIS 十月数据）"',
     '"55,7 — % que cita la vivienda como el principal problema, según el CIS de octubre (CIS vom Oktober)"'),
    ('"AHORA TÚ · 即学即练"', '"AHORA TÚ · DU BIST DRAN"'),
    ('"大选在 11 月 29 日周日"', '"die Wahl ist am Sonntag, dem 29. November"'),
    ('"周一放假的自治区有 9 个"', '"in neun Regionen ist am Montag Feiertag"'),
    ('"住房是选战的决定性议题"', '"die Wohnung ist das entscheidende Wahlkampfthema"'),
    ('"马竞–巴萨周日 21:00 开球"', '"Atlético–Barça beginnt am Sonntag um 21:00 Uhr"'),
    ('"NFL 马德里站周日 15:30 开球"', '"die NFL in Madrid beginnt am Sonntag um 15:30 Uhr"'),
    ('"本周五大看点 · Para entender la semana"', '"Fünf Themen · Para entender la semana"'),
    ('"五大看点，不编数字：全在本期里讲清。"', '"Nichts erfunden — alles erklärt."'),
    ('"EN ESTA EDICIÓN · 本期目录"', '"EN ESTA EDICIÓN · INHALT"'),
    ('"“竞选预热期”：正式竞选前的几周。"', '"„Vorwahlzeit“: die Wochen vor dem offiziellen Wahlkampf."'),
    ('"BREVES · 快讯"', '"BREVES · KURZNACHRICHTEN"'),
    ('"QUIZ RELÁMPAGO · 闪电问答"', '"QUIZ RELÁMPAGO · BLITZQUIZ"'),
    ('"读头版，选出正确答案 · 答案见第 8 版"', '"Lies die Titelseite und wähle richtig · Antworten auf Seite 8"'),
    ('"大选在 11 月 29 日"', '"die Wahl ist am 29. November"'),
    ('"NFL 马德里站周日下午"', '"die NFL in Madrid ist am Sonntagnachmittag"'),
    ('"马竞–巴萨周日 21:00"', '"Atlético–Barça am Sonntag um 21:00 Uhr"'),
    ('"VIDA · 生活"', '"VIDA · LEBEN"'),
    ('"NIVEL A2 · El puente del lunes 2 · 11 月 2 日的连休"', '"NIVEL A2 · El puente del lunes 2 · Der Brückentag am Montag, dem 2."'),
    ('"EL CALENDARIO · 本周日历"', '"EL CALENDARIO · DIE WOCHE"'),
    ('"Lunes 2 — puente en nueve comunidades; las candidaturas proclamadas llegan al BOE el martes 3（周一九地连休；周二《官方公报》公布正式候选名单）"',
     '"Lunes 2 — puente en nueve comunidades; las candidaturas proclamadas llegan al BOE el martes 3 (montags Brückentag in neun Regionen; dienstags veröffentlicht das BOE die offiziellen Listen)"'),
    ('"Martes 3 — Champions: Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG（周二欧冠三场西甲球队比赛）"',
     '"Martes 3 — Champions: Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG (dienstags drei Champions-League-Spiele spanischer Teams)"'),
    ('"Miércoles 4 — Champions: AEK–Real Madrid, 18:45（周三皇马客场对雅典 AEK）"',
     '"Miércoles 4 — Champions: AEK–Real Madrid, 18:45 (mittwochs Real auswärts bei AEK Athen)"'),
    ('"Jueves 5 — Europa League: Real Sociedad–Lyon, 18:45（周四皇家社会欧联对里昂）"',
     '"Jueves 5 — Europa League: Real Sociedad–Lyon, 18:45 (donnerstags Real Sociedad in der Europa League gegen Lyon)"'),
    ('"Viernes 6 — Liga, jornada 12: Sevilla–Alavés, 21:00（周五联赛第 12 轮开球）"',
     '"Viernes 6 — Liga, jornada 12: Sevilla–Alavés, 21:00 (freitags Start des 12. Spieltags)"'),
    ('"Sábado 7 — Valencia–Real Madrid, 21:00, en Mestalla（周六瓦伦西亚对皇马）"',
     '"Sábado 7 — Valencia–Real Madrid, 21:00, en Mestalla (samstags Valencia gegen Real Madrid)"'),
    ('"Domingo 8 — NFL en el Bernabéu, 15:30; Atlético–Barça, 21:00（周日 NFL 马德里站＋马竞对巴萨）"',
     '"Domingo 8 — NFL en el Bernabéu, 15:30; Atlético–Barça, 21:00 (sonntags NFL in Madrid und Atlético–Barça)"'),
    ('"festivo 放假的 · el puente 连休 · la comunidad 自治区 · anochecer 天黑 · el horario de invierno 冬令时。"',
     '"festivo Feiertag, frei · el puente Brückentag · la comunidad autonome Region · anochecer dunkel werden · el horario de invierno Winterzeit."'),
    ('"¿Y TÚ? · 说说你自己"', '"¿Y TÚ? · UND DU?"'),
    ('"11 月 2 日你那里放假吗？连休你做什么：旅行、休息还是看球？写两句西班牙语寄给编辑部。"',
     '"Ist der 2. November bei dir Feiertag? Was machst du mit dem Brückentag: reisen, ausruhen oder Fußball schauen? Schreibe zwei Sätze auf Spanisch an die Redaktion."'),
    ('"LOS DÍAS DE LA SEMANA · 这样说日期"', '"LOS DÍAS DE LA SEMANA · SO SAGT MAN DAS DATUM"'),
    ('"lunes 2 – domingo 8 de noviembre · 11 月 2 日周一至 8 日周日"',
     '"lunes 2 – domingo 8 de noviembre · Montag, 2. bis Sonntag, 8. November"'),
    ('"EJERCICIOS · 第 2 版练习"', '"EJERCICIOS · ÜBUNGEN"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Antworten auf Seite 8 · Aufgaben gemischt, nach Nummer suchen"'),
    ('"用正确的日期形式补全句子。"', '"Ergänze die Sätze mit der richtigen Datumsform."'),
    ('"补全动词的现在时形式。"', '"Ergänze die Verbformen im Präsens."'),
    ('"读第 2 版文章，选出正确答案。"', '"Lies den Text auf Seite 2 und wähle die richtige Antwort."'),
    ('"11 月 2 日周一"', '"Montag, der 2. November"'),
    ('"11 月 8 日周日"', '"Sonntag, der 8. November"'),
    ('"每月 1 号说 el uno"', '"der 1. heißt el uno"'),
    ('"月份小写"', '"Monate klein"'),
    ('"el lunes → es（单数）"', '"el lunes → es (Singular)"'),
    ('"九个自治区周一放假"', '"in neun Regionen ist am Montag Feiertag"'),
    ('"诸圣节 11 月 1 日落在周日"', '"Allerheiligen am 1. November fällt auf einen Sonntag"'),
    ('"加泰罗尼亚周一是工作日"', '"in Katalonien ist der Montag ein Arbeitstag"'),
    ('"冬令时第二周，天黑得早"', '"zweite Woche mit Winterzeit, es wird früh dunkel"'),
    ('"把词和释义配对"', '"Zuordnen"'),
    ('"puente=三天连休 b"', '"puente = Brückentag, drei Tage frei (b)"'),
    ('"festivo=放假的 a"', '"festivo = Feiertag, frei (a)"'),
    ('"anochecer=天黑 c"', '"anochecer = dunkel werden (c)"'),
    ('"comunidad=自治区 d"', '"comunidad = autonome Region (d)"'),
],
"content34.py": [
    ('"CULTURA · 文化"', '"CULTURA · KULTUR"'),
    ('"A2 → B1 · La semana pasada: tres noches de otoño · 上周的三个秋夜"',
     '"A2 → B1 · La semana pasada: tres noches de otoño · Drei Herbstnächte letzte Woche"'),
    ('"sobrio 克制的 · el homenaje 纪念表彰 · el disfraz 服装（化装） · el boniato 红薯 · el cementerio 墓地。"',
     '"sobrio schlicht, zurückhaltend · el homenaje Ehrung, Gedenken · el disfraz Kostüm · el boniato Süßkartoffel · el cementerio Friedhof."'),
    ('"¿Y TÚ? · 说说你自己"', '"¿Y TÚ? · UND DU?"'),
    ('"你最喜欢哪一夜：29 日、31 日还是 1 日？31 日你吃了什么？写两句寄来。"',
     '"Welche Nacht magst du am liebsten: die vom 29., 31. oder 1.? Was hast du am 31. gegessen? Schreibe zwei Sätze."'),
    ('"EJERCICIOS · 第 3 版练习"', '"EJERCICIOS · ÜBUNGEN"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Antworten auf Seite 8 · Aufgaben gemischt, nach Nummer suchen"'),
    ('"读第 3 版文章，判断对错。"', '"Lies den Text auf Seite 3: richtig oder falsch?"'),
    ('"DANA 纪念活动在 10 月 29 日周四"', '"das DANA-Gedenken ist am Donnerstag, dem 29. Oktober"'),
    ('"Castanyada 吃烤栗子、红薯和 panellets"', '"zur Castanyada gibt es geröstete Kastanien, Süßkartoffeln und panellets"'),
    ('"Samaín 是加利西亚古节，不是万圣节译名"', '"Samaín ist ein altes galicisches Fest, kein Halloween-Name"'),
    ('"诸圣节在 11 月 1 日，不是 10 月 31 日"', '"Allerheiligen ist am 1. November, nicht am 31. Oktober"'),
    ('"周日家属去墓地献花"', '"am Sonntag bringen Familien Blumen auf die Friedhöfe"'),
    ('"用方框里的词填空。"', '"Fülle die Lücken mit den Wörtern aus dem Kasten."'),
    ('"给逝者带花 flores"', '"Blumen für die Verstorbenen: flores"'),
    ('"cementerio = 墓地"', '"cementerio = Friedhof"'),
    ('"castañas asadas 烤栗子"', '"castañas asadas = geröstete Kastanien"'),
    ('"disfraz = 化装服装"', '"disfraz = Kostüm"'),
    ('"actos de memoria 纪念活动"', '"actos de memoria = Gedenkveranstaltungen"'),
    ('"选出正确答案。"', '"Wähle die richtige Antwort."'),
    ('"DANA 纪念是 2024 年风暴两周年"', '"das DANA-Gedenken ist zwei Jahre nach dem Sturm von 2024"'),
    ('"Castanyada 在加泰罗尼亚"', '"die Castanyada ist in Katalonien"'),
    ('"Samaín 是加利西亚古老节日"', '"Samaín ist ein sehr altes galicisches Fest"'),
    ('"三夜之后周一有人连休有人上班"', '"nach den drei Nächten haben am Montag einige frei, andere arbeiten"'),
    ('"把词组成正确的句子。"', '"Bilde aus den Wörtern richtige Sätze."'),
    ('"动词第二位"', '"Verb an 2. Stelle"'),
    ('"时间在前，动词第二"', '"Zeitangabe vorn, Verb an 2. Stelle"'),
    ('"地点在前，动词第二"', '"Ortsangabe vorn, Verb an 2. Stelle"'),
    ('"间接疑问用 si"', '"indirekte Frage mit si"'),
    ('"DEPORTE · 体育"', '"DEPORTE · SPORT"'),
    ('"NIVEL B1 · Europa primero, el domingo a las 21:00 · 欧战在先，周日晚九点"',
     '"NIVEL B1 · Europa primero, el domingo a las 21:00 · Erst Europa, dann der Sonntag um 21 Uhr"'),
    ('"la jornada 轮次 · recortar la distancia 缩小分差 · recibir 主场迎战 · visitar 客场挑战 · el Metropolitano 马竞主场。"',
     '"la jornada Spieltag · recortar la distancia den Rückstand verkürzen · recibir zu Hause empfangen · visitar auswärts antreten · el Metropolitano Stadion von Atlético."'),
    ('"周日 21:00 你看哪一场？马竞主场谁赢？写两句西班牙语寄来。"',
     '"Was schaust du am Sonntag um 21:00 Uhr — und wer gewinnt im Metropolitano? Schreibe zwei Sätze auf Spanisch."'),
    ('"LA SEMANA EUROPEA Y LA JORNADA 12 · 欧战周与联赛第 12 轮"',
     '"LA SEMANA EUROPEA Y LA JORNADA 12 · EUROPÄISCHE WOCHE UND 12. SPIELTAG"'),
    ('"EJERCICIOS · 第 4 版练习"', '"EJERCICIOS · ÜBUNGEN"'),
    ('"读第 4 版文章，选出正确答案。"', '"Lies den Text auf Seite 4 und wähle die richtige Antwort."'),
    ('"皇马 2–1 赢下国家德比"', '"Real gewinnt den Clásico mit 2:1"'),
    ('"姆巴佩进了两球"', '"Mbappé schießt zwei Tore"'),
    ('"周二欧冠三场西甲球队比赛"', '"am Dienstag spielen drei spanische Teams in der Champions League"'),
    ('"周日 21:00 马竞–巴萨"', '"Atlético–Barça am Sonntag um 21:00 Uhr"'),
    ('"周日下午还有 NFL 马德里站"', '"am Sonntagnachmittag gibt es auch die NFL in Madrid"'),
    ('"jornada=轮次 b"', '"jornada = Spieltag (b)"'),
    ('"recibir=主场迎战 a"', '"recibir = zu Hause empfangen (a)"'),
    ('"visitar=客场挑战 d"', '"visitar = auswärts antreten (d)"'),
    ('"recortar=缩小分差 c"', '"recortar = Rückstand verkürzen (c)"'),
    ('"用括号里词的比较级或 -ísimo 形式填空。"', '"Ergänze den Komparativ oder die -ísimo-Form des Wortes in Klammern."'),
    ('"más + importante（马竞–巴萨更重要）"', '"más + importante (Atlético–Barça ist wichtiger)"'),
    ('"muchísimos partidos 比赛很多"', '"muchísimos partidos = sehr viele Spiele"'),
    ('"malo 的比较级是 peor"', '"der Komparativ von malo ist peor"'),
    ('"bueno 的比较级是 mejor"', '"der Komparativ von bueno ist mejor"'),
    ('"把句子改成过去时（pretérito indefinido）。"', '"Setze die Sätze ins pretérito indefinido (Vergangenheit)."'),
    ('"ir 的过去时是 fueron"', '"die Vergangenheit von ir ist fueron"'),
],
"content56.py": [
    ('"JUVENTUD · 青年"', '"JUVENTUD · JUGEND"'),
    ('"NIVEL B1 · La NFL en Madrid · NFL 来到马德里"', '"NIVEL B1 · La NFL en Madrid · Die NFL in Madrid"'),
    ('"EL PLAN DEL PUENTE · 连休计划"', '"EL PLAN DEL PUENTE · DEIN PLAN"'),
    ('"1. El lunes 2: descanso y familia — o viaje, si tu comunidad hace puente（周一：休息陪家人；若你那里连休，就去旅行）"',
     '"1. El lunes 2: descanso y familia — o viaje, si tu comunidad hace puente (montags: ausruhen mit der Familie; wenn bei dir Brückentag ist, verreisen)"'),
    ('"2. El sábado 7: Valencia–Real Madrid, 21:00, en Mestalla（周六晚：瓦伦西亚对皇马）"',
     '"2. El sábado 7: Valencia–Real Madrid, 21:00, en Mestalla (samstagabends: Valencia gegen Real Madrid)"'),
    ('"3. El domingo 8, 15:30: la NFL en el Bernabéu（周日下午：NFL 马德里站）"',
     '"3. El domingo 8, 15:30: la NFL en el Bernabéu (sonntagnachmittags: die NFL im Bernabéu)"'),
    ('"4. El domingo 8, 21:00: Atlético–Barça en el Metropolitano（周日晚：马竞对巴萨）"',
     '"4. El domingo 8, 21:00: Atlético–Barça en el Metropolitano (sonntagabends: Atlético–Barça im Metropolitano)"'),
    ('"5. Y el lunes 9: vuelta a clase y al trabajo; la campaña empieza el viernes 13（返校返工；竞选 13 日开始）"',
     '"5. Y el lunes 9: vuelta a clase y al trabajo; la campaña empieza el viernes 13 (zurück in Schule und Arbeit; der Wahlkampf beginnt am 13.)"'),
    ('"el emparrillado 美式足球场（烤架形场地） · el himno 国歌 · el touchdown 达阵得分 · la calabaza 南瓜。"',
     '"el emparrillado Spielfeld (in Grillform) · el himno Hymne · el touchdown Touchdown · la calabaza Kürbis."'),
    ('"¿Y TÚ? · 说说你自己"', '"¿Y TÚ? · UND DU?"'),
    ('"你看过美式足球比赛吗？你更喜欢足球还是美式足球？写两句寄来。"',
     '"Hast du schon einmal ein American-Football-Spiel gesehen? Magst du Fußball oder American Football lieber? Schreibe zwei Sätze."'),
    ('"EJERCICIOS · 第 5 版练习"', '"EJERCICIOS · ÜBUNGEN"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Antworten auf Seite 8 · Aufgaben gemischt, nach Nummer suchen"'),
    ('"读第 5 版文章，选出正确答案。"', '"Lies den Text auf Seite 5 und wähle die richtige Antwort."'),
    ('"NFL 马德里站周日 15:30"', '"die NFL in Madrid am Sonntag um 15:30 Uhr"'),
    ('"孟加拉虎对猎鹰"', '"Bengals gegen Falcons"'),
    ('"西班牙国歌由吉他手演奏"', '"die spanische Hymne spielt ein Gitarrist"'),
    ('"首场 NFL 伯纳乌赛在 2025 年 11 月 16 日"', '"das erste NFL-Spiel im Bernabéu war am 16. November 2025"'),
    ('"美式足球用手打、四次进攻"', '"American Football spielt man mit den Händen, in vier Versuchen"'),
    ('"用方框里的词填空。注意：有的词要变位。"', '"Fülle die Lücken mit den Wörtern aus dem Kasten. Achtung: Manche Verben musst du beugen."'),
    ('"estadio = 体育场"', '"estadio = Stadion"'),
    ('"himno = 国歌"', '"himno = Hymne"'),
    ('"acoger 变位 → acoge"', '"acoger konjugiert → acoge"'),
    ('"touchdown = 达阵得分"', '"touchdown = Touchdown"'),
    ('"calabaza = 南瓜"', '"calabaza = Kürbis"'),
    ('"disfraz = 化装服装"', '"disfraz = Kostüm"'),
    ('"用 ir a + 原形动词改写句子，表示“将要”。"', '"Forme die Sätze mit ir a + Infinitiv um (nahe Zukunft)."'),
    ('"vamos a + 原形"', '"vamos a + Infinitiv"'),
    ('"va a + 原形"', '"va a + Infinitiv"'),
    ('"vas a + 原形"', '"vas a + Infinitiv"'),
    ('"van a + 原形"', '"van a + Infinitiv"'),
    ('(原形 acoger)', '(Infinitiv: acoger)'),
    ('"NFL 马德里站是伯纳乌第二场 NFL 比赛"', '"die NFL in Madrid ist das zweite NFL-Spiel im Bernabéu"'),
    ('"美国国歌由 Momsen 演唱，不是 Sáinz-Villegas"', '"die US-Hymne singt Momsen, nicht Sáinz-Villegas"'),
    ('"万圣节之夜在周六 31 日"', '"die Halloween-Nacht ist am Samstag, dem 31."'),
    ('"A FONDO · 深读"', '"A FONDO · HINTERGRUND"'),
    ('"NIVEL B2 · La vivienda decide la campaña · 住房决定选战"',
     '"NIVEL B2 · La vivienda decide la campaña · Die Wohnungsfrage entscheidet den Wahlkampf"'),
    ('"EJERCICIOS · 第 6 版练习"', '"EJERCICIOS · ÜBUNGEN"'),
    ('"看上面两张图，选出正确答案。"', '"Lies die Grafiken und wähle richtig."'),
    ('"CIS 里 PSOE 第一（34%）"', '"im CIS liegt die PSOE vorn (34 %)"'),
    ('"CIS 里 PP 22,2%"', '"im CIS hat die PP 22,2 %"'),
    ('"住房是首要问题（55,7%）"', '"die Wohnung ist das wichtigste Problem (55,7 %)"'),
    ('"调查在 10 月 1–6 日进行"', '"die Befragung war vom 1. bis 6. Oktober"'),
    ('"本报只刊登 CIS 这一组数据并注明来源日期"', '"wir drucken nur die CIS-Reihe, mit Quelle und Datum"'),
    ('"10 月 2 日议会否决两项住房法令"', '"am 2. Oktober lehnte das Parlament zwei Wohnungsdekrete ab"'),
    ('"10 月 5 日解散议会并召集大选"', '"am 5. Oktober löste Sánchez das Parlament auf und rief Wahlen aus"'),
    ('"民调是带误差的具体某天的照片"', '"eine Umfrage ist ein Foto mit Fehlermarge"'),
    ('"竞选 11 月 13 日开始"', '"der Wahlkampf beginnt am 13. November"'),
    ('"es posible que + 虚拟式 tenga"', '"es posible que + Subjuntivo: tenga"'),
    ('"es importante que + 虚拟式 sea"', '"es importante que + Subjuntivo: sea"'),
    ('"para que + 虚拟式（目的）"', '"para que + Subjuntivo (Zweck)"'),
    ('"Aunque 后接陈述式（已知事实）"', '"Aunque steht mit Indikativ (bekannte Tatsache)"'),
    ('"用方框里的词填空：sondeo · muestra · indecisos · margen de error"',
     '"Setze ein: sondeo · muestra · indecisos · margen de error"'),
    ('"sondeo = 民调"', '"sondeo = Umfrage"'),
    ('"muestra = 样本（5.025 人）"', '"muestra = Stichprobe (5.025 Personen)"'),
    ('"indecisos = 未决定者"', '"indecisos = Unentschlossene"'),
    ('"margen de error = 误差范围"', '"margen de error = Fehlermarge"'),
],
"content7.py": [
    ('"LENGUA · 语言"', '"LENGUA · SPRACHE"'),
    ('"语言聚焦 · Tres niveles, tres herramientas · 三个级别，三件工具"',
     '"Sprachfokus · Tres niveles, tres herramientas · Drei Stufen, drei Werkzeuge"'),
    ('"日期格式：el lunes 2 de noviembre；星期、月份小写；1 号说 el uno。"',
     '"Datumsform: el lunes 2 de noviembre; Wochentage und Monate klein; die 1 heißt el uno."'),
    ('"el lunes 2 de noviembre 连休"', '"el lunes 2 de noviembre Brückentag"'),
    ('"el 1 = el uno"', '"der 1. heißt el uno"'),
    ('"29 日是周日"', '"der 29. ist ein Sonntag"'),
    ('"月份小写：noviembre"', '"Monate klein: noviembre"'),
    ('"比较级 más…que、tan…como；bueno→mejor、malo→peor；绝不说 más mejor。"',
     '"Komparativ: más … que, tan … como; bueno → mejor, malo → peor; nie mehr mejor."'),
    ('"más + cara（房价更高）"', '"más + cara (Wohnung teurer)"'),
    ('"tan + alta + como（同样高）"', '"tan + alta + como (genauso hoch)"'),
    ('"bueno 的比较级是 mejor（不用 más）"', '"der Komparativ von bueno ist mejor (ohne más)"'),
    ('"más mejor 是错误说法"', '"más mejor ist falsch"'),
    ('"es necesario que、para que、ojalá 后用虚拟式；creo que 后用陈述式。"',
     '"Nach es necesario que, para que und ojalá steht der Subjuntivo; nach creo que der Indikativ."'),
    ('"es necesario que + 虚拟式 baje"', '"es necesario que + Subjuntivo: baje"'),
    ('"para que + 虚拟式 sea"', '"para que + Subjuntivo: sea"'),
    ('"creo que + 陈述式 es"', '"creo que + Indikativ: es"'),
    ('"ojalá + 虚拟式：baje"', '"ojalá + Subjuntivo: baje"'),
    ('"ERRORES TÍPICOS · 常见错误"', '"ERRORES TÍPICOS · TYPISCHE FEHLER"'),
    # W43 es-de proofread fix: this title overflows its box at 23pt
    # (ink to 1914.8 > box 1885); 20pt lands at 1857.2. Same string, same box.
    ('p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS · TYPISCHE FEHLER", 23,',
     'p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS · TYPISCHE FEHLER", 20,'),
    ('"lunes 是单数，动词用 es。"', '"lunes ist Singular, Verb im Singular: es."'),
    ('"mejor 本身就是比较级，不加 más。"', '"mejor ist schon Komparativ, kein más dazu."'),
    ('"gente 是单数集合名词，动词用单数。"', '"gente ist ein Kollektivum im Singular."'),
    ('"creo que 表肯定，用陈述式 es。"', '"creo que behauptet, also Indikativ: es."'),
    ('"LA PALABRA · 本周生词"', '"LA PALABRA · WORT DER WOCHE"'),
    ('"precampaña = 竞选预热期：正式竞选前的几周。本期就是 precampaña；竞选 13 日周五开始。"',
     '"precampaña = Vorwahlzeit: die Wochen vor dem offiziellen Wahlkampf. Diese Ausgabe ist precampaña; der Wahlkampf beginnt am Freitag, dem 13."'),
    ('（ejemplo, escrito por la redacción）', '(ejemplo, escrito por la redacción)'),
    ('"编辑部说明：截至本期截稿，未收到真实读者来信与第 8 版最佳作文，故本期登载编辑部示例信，承诺顺延至 VOL.3。欢迎来信！"',
     '"Anmerkung der Redaktion: Bis zum Redaktionsschluss sind keine echten Leserbriefe und keine besten Texte von Seite 8 eingegangen; wir drucken daher diesen Beispielbrief, und das Versprechen gilt für VOL.3. Schreib uns!"'),
    ('"FRASES DE LA SEMANA · 本周金句（逐字摘自本期文章）"',
     '"FRASES DE LA SEMANA · SÄTZE DER WOCHE (WÖRTLICH AUS DIESER AUSGABE)"'),
    ('"名单已提交：现在各党开始撰写纲领。"', '"Die Listen sind eingereicht: Jetzt schreiben die Parteien ihre Programme."'),
    ('"11 月 2 日周一九个自治区放假，其他地区照常上班。"', '"Am Montag, dem 2. November, ist in neun Regionen Feiertag, in den anderen wird gearbeitet."'),
    ('"三个节日，同一个秋夜。"', '"Drei Feste, eine Herbstnacht."'),
    ('"皇马在诺坎普 2–1 获胜：这是巴萨本赛季联赛首败。"', '"Real gewinnt 2:1 im Camp Nou: die erste Liga-Niederlage des Barça in dieser Saison."'),
    ('"伯纳乌把草皮换成烤架形球场：美式足球来到马德里。"', '"Das Bernabéu tauscht den Rasen gegen das Spielfeld: American Football kommt nach Madrid."'),
    ('"住房是 55.7% 的西班牙人的首要问题。"', '"Die Wohnung ist für 55,7 % der Spanier das wichtigste Problem."'),
    ('"一次民调就是一张带误差的照片，拍于某一天。"', '"Eine Umfrage ist ein Foto mit Fehlermarge, an einem bestimmten Tag aufgenommen."'),
    ('"11 月 8 日周日，马德里有两场约会：15:30 的 NFL 和 21:00 的马竞对巴萨。"',
     '"Am Sonntag, dem 8., hat Madrid zwei Termine: die NFL um 15:30 Uhr und Atlético–Barça um 21:00 Uhr."'),
    ('"LA PRÓXIMA SEMANA · 下期预告 (VOL.3)"', '"LA PRÓXIMA SEMANA · NÄCHSTE AUSGABE (VOL.3)"'),
],
"content8.py": [
    ('"EJERCICIOS Y RESPUESTAS · 练习与答案"', '"EJERCICIOS Y RESPUESTAS · ÜBUNGEN UND ANTWORTEN"'),
    ('"第 8 版 · La gran prueba de la semana + todas las respuestas"', '"Seite 8 · La gran prueba de la semana + todas las respuestas"'),
    ('"ganó 2–1 = 以 2–1 获胜"', '"ganó 2–1 = mit 2:1 gewinnen"'),
    ('"marcar dos goles = 进两球"', '"marcar dos goles = zwei Tore schießen"'),
    ('"primera derrota liguera = 联赛首败"', '"primera derrota liguera = erste Liga-Niederlage"'),
    ('"recortar = 缩小分差"', '"recortar = Rückstand verkürzen"'),
    ('"acoger = 承办（伯纳乌承办 NFL）"', '"acoger = beherbergen (das Bernabéu beherbergt die NFL)"'),
    ('"el emparrillado = 美式足球场"', '"el emparrillado = Spielfeld (American Football)"'),
    ('"周日上演马竞–巴萨"', '"am Sonntag steigt Atlético–Barça"'),
    ('"himno = 国歌"', '"himno = Hymne"'),
    ('"周一放假的自治区有 9 个"', '"in neun Regionen ist am Montag Feiertag"'),
    ('"诸圣节 11 月 1 日"', '"Allerheiligen ist am 1. November"'),
    ('"马竞–巴萨与 NFL 都在周日"', '"Atlético–Barça und die NFL sind beide am Sonntag"'),
    ('"Castanyada 吃 panellets"', '"zur Castanyada gibt es panellets"'),
    ('"DANA 纪念活动在 10 月 29 日周四"', '"das DANA-Gedenken ist am Donnerstag, dem 29. Oktober"'),
    ('"大选在 11 月 29 日"', '"die Wahl ist am 29. November"'),
    ('"CIS 十月调查：住房 55,7%"', '"im CIS vom Oktober: Wohnen 55,7 %"'),
    ('"竞选 11 月 13 日开始"', '"der Wahlkampf beginnt am 13. November"'),
    ('"马德里在放假名单里"', '"Madrid steht auf der Feiertagsliste"'),
    ('"加泰罗尼亚周一是工作日"', '"in Katalonien ist der Montag ein Arbeitstag"'),
    ('"Ana 只看 NFL；晚上看马竞–巴萨的是 Pablo"', '"Ana sieht nur die NFL; Atlético–Barça am Abend sieht Pablo"'),
    ('"标题概括两地对比"', '"die Überschrift zeigt den Gegensatz der beiden Montage"'),
    ('"主语 + 动词 + 地点"', '"Subjekt + Verb + Ortsangabe"'),
    ('"时间在前"', '"Zeitangabe vorn"'),
    ('"a las nueve = 在九点"', '"a las nueve = um neun Uhr"'),
    ('"疑问词在句首"', '"Fragewort am Anfang"'),
    # §E re-aim (W43 es-de KIT §5 pattern): ES->DE items get German keys;
    # DE->ES items get German stems, Spanish keys byte-identical.
    ('"周一在九个自治区是假日。"', '"Am Montag ist in neun Regionen Feiertag."'),
    ('"周日我们看 NFL 和马竞–巴萨。"', '"Am Sonntag sehen wir die NFL und Atlético–Barça."'),
    ('"伯纳乌承办一场 NFL 比赛。→ ___"', '"Das Bernabéu ist Gastgeber eines NFL-Spiels. → ___"'),
    ('"每个图表都必须标明来源。→ ___"', '"Jede Grafik muss ihre Quelle angeben. → ___"'),
    ('"对照原文"', '"Übersetzung"'),
    ('"acoger = 承办"', '"acoger = beherbergen"'),
    ('"tener que = 必须"', '"tener que = müssen"'),
    ('"sondeo=民调 c"', '"sondeo = Umfrage (c)"'),
    ('"muestra=样本 d"', '"muestra = Stichprobe (d)"'),
    ('"margen de error=误差范围 b"', '"margen de error = Fehlermarge (b)"'),
    ('"junta electoral=选举委员会 a"', '"junta electoral = Wahlkommission (a)"'),
    ('"alquiler = 租金"', '"alquiler = Miete"'),
    ('"tres habitaciones = 三居室"', '"tres habitaciones = drei Zimmer"'),
    ('"¿cuánto cuesta? 多少钱"', '"¿cuánto cuesta? = Was kostet es?"'),
    ('"firmar = 签（合同）"', '"firmar = unterschreiben (Vertrag)"'),
    ('"mudanza = 搬家"', '"mudanza = Umzug"'),
    ('"写作题（无唯一答案）；范文（84 词）见下。"', '"Schreibaufgabe (ohne Musterlösung); der Mustertext (84 Wörter) steht unten."'),
    ('"（开放题，范文如下）"', '"Offene Aufgabe — Mustertext unten auf dieser Seite"'),
    ('"范文见本版 H 区（84 词）"', '"Mustertext in Abschnitt H auf dieser Seite (84 Wörter)"'),
    ('"RESPUESTAS · 参考答案 — 按版面分页排列，找到题号即可"', '"RESPUESTAS · ANTWORTEN — nach Seiten geordnet"'),
    ('"每题附一句中文简析 · 带 ✓ 的为范文题"', '"Zu jeder Aufgabe ein deutscher Kurzhinweis · ✓ = Schreibaufgabe"'),
],
}


# P8 overflow fix (W43 es-de KIT §6 precedent): German notes that wrapped to
# 2 lines in the P8 answer flow are shortened to measured 1-line forms.
# Frozen keys (#1, #44, #138, #139) legitimately stay 2 lines.
SHORTEN_PAIRS = {
"content12.py": [
    ('"die Wohnung ist das entscheidende Wahlkampfthema"', '"die Wohnung entscheidet den Wahlkampf"'),
],
"content34.py": [
    ('"das DANA-Gedenken ist am Donnerstag, dem 29. Oktober"', '"das DANA-Gedenken ist am 29. Oktober"'),
    ('"zur Castanyada gibt es geröstete Kastanien, Süßkartoffeln und panellets"', '"Castanyada: Kastanien, Süßkartoffeln, panellets"'),
    ('"Samaín ist ein altes galicisches Fest, kein Halloween-Name"', '"Samaín: altes galicisches Fest, kein Halloween"'),
    ('"Allerheiligen ist am 1. November, nicht am 31. Oktober"', '"Allerheiligen ist am 1., nicht am 31. Oktober"'),
    ('"am Sonntag bringen Familien Blumen auf die Friedhöfe"', '"sonntags bringen Familien Blumen auf Friedhöfe"'),
    ('"das DANA-Gedenken ist zwei Jahre nach dem Sturm von 2024"', '"das DANA-Gedenken, zwei Jahre nach 2024"'),
    ('"nach den drei Nächten haben am Montag einige frei, andere arbeiten"', '"nach den drei Nächten: montags frei oder arbeiten"'),
    ('"Ortsangabe vorn, Verb an 2. Stelle"', '"Ort vorn, Verb an 2. Stelle"'),
    ('"am Dienstag spielen drei spanische Teams in der Champions League"', '"dienstags drei spanische Teams in der Champions League"'),
    ('"más + importante (Atlético–Barça ist wichtiger)"', '"más + importante (wichtiger)"'),
    ('"die Vergangenheit von ir ist fueron"', '"ir → fueron"'),
],
"content56.py": [
    ('"das erste NFL-Spiel im Bernabéu war am 16. November 2025"', '"erstes NFL-Spiel im Bernabéu: 16.11.2025"'),
    ('"American Football spielt man mit den Händen, in vier Versuchen"', '"American Football: mit den Händen, vier Versuche"'),
    ('"die NFL in Madrid ist das zweite NFL-Spiel im Bernabéu"', '"die NFL in Madrid: zweites Spiel im Bernabéu"'),
    ('"am 2. Oktober lehnte das Parlament zwei Wohnungsdekrete ab"', '"am 2. Oktober: zwei Wohnungsdekrete abgelehnt"'),
    ('"am 5. Oktober löste Sánchez das Parlament auf und rief Wahlen aus"', '"am 5. Oktober: Parlament aufgelöst, Wahlen ausgerufen"'),
],
"content8.py": [
    ('"acoger = beherbergen (das Bernabéu beherbergt die NFL)"', '"acoger = beherbergen"'),
    ('"das DANA-Gedenken ist am Donnerstag, dem 29. Oktober"', '"das DANA-Gedenken ist am 29. Oktober"'),
    ('"Ana sieht nur die NFL; Atlético–Barça am Abend sieht Pablo"', '"Ana: nur NFL; abends Atlético–Barça: Pablo"'),
    ('"a las nueve = um neun Uhr"', '"a las neun = 9 Uhr"'),
],
}


# FIX2 (occlusion audit 3 NEW flags, 2026-10-27): the edition's own German
# text overflowed core geometry -- P1 word note grazed the y=1844 rule,
# P7 col3 pushed the preview box onto the footer, and frases #2/#5/#8
# translations wrapped to 2 lines over the fixed 128px row pitch. All
# shortenings below are measured 1-line (word note, frases) or save the
# exact lines needed to pull P7 col3 back above the footer (clinic2 2->1,
# palabra 4->3, ldcn 6->3; the Spanish disclosure above ldcn keeps the
# full facts incl. the missing best texts).
FIX2_PAIRS = {
"content12.py": [
    ('"„Vorwahlzeit“: die Wochen vor dem offiziellen Wahlkampf."', '"„Vorwahlzeit“: die Wochen vor dem Wahlkampf."'),
],
"content7.py": [
    ('"mejor ist schon Komparativ, kein más dazu."', '"mejor ist schon Komparativ."'),
    ('"precampaña = Vorwahlzeit: die Wochen vor dem offiziellen Wahlkampf. Diese Ausgabe ist precampaña; der Wahlkampf beginnt am Freitag, dem 13."',
     '"precampaña = Vorwahlzeit. Diese Ausgabe ist precampaña; Wahlkampf ab Freitag, dem 13."'),
    ('"Anmerkung der Redaktion: Bis zum Redaktionsschluss sind keine echten Leserbriefe und keine besten Texte von Seite 8 eingegangen; wir drucken daher diesen Beispielbrief, und das Versprechen gilt für VOL.3. Schreib uns!"',
     '"Anmerkung der Redaktion: Keine echten Briefe eingegangen — daher dieser Beispielbrief. Versprechen gilt für VOL.3!"'),
    ('"Am Montag, dem 2. November, ist in neun Regionen Feiertag, in den anderen wird gearbeitet."',
     '"Montag, 2. November: neun Regionen frei, die anderen arbeiten."'),
    ('"Das Bernabéu tauscht den Rasen gegen das Spielfeld: American Football kommt nach Madrid."',
     '"Das Bernabéu tauscht Rasen gegen Spielfeld: American Football in Madrid."'),
    ('"Am Sonntag, dem 8., hat Madrid zwei Termine: die NFL um 15:30 Uhr und Atlético–Barça um 21:00 Uhr."',
     '"Sonntag, 8.: Madrid hat zwei Termine — NFL 15:30 Uhr, Atlético–Barça 21:00 Uhr."'),
],
}

OUT_OLD = "files/weekly-report-w45-es-core"
OUT_NEW = "files/weekly-report-w45-es-de"

def main():
    # Final forms of notes later shortened by SHORTEN_PAIRS: a PAIRS new
    # string may legitimately be absent on re-runs (replaced by its shorten).
    _shorten_final = {}
    for _pairs in SHORTEN_PAIRS.values():
        for _o, _n in _pairs:
            _shorten_final[_o] = _n
    total = 0
    for fname, pairs in PAIRS.items():
        path = os.path.join(HERE, fname)
        src = io.open(path, encoding="utf-8").read()
        for old, new in pairs:
            n = src.count(old)
            if n == 0 and (new in src or _shorten_final.get(new, "") in src):
                print(f"{fname}: SKIP already applied :: {old[:70]}")
                continue
            assert n >= 1, f"{fname}: NOT FOUND (0x): {old[:90]}"
            src = src.replace(old, new)
            total += n
            print(f"{fname}: x{n} :: {old[:70]}")
        # OUT repoint for content files
        if fname.startswith("content"):
            if OUT_OLD in src:
                src = src.replace(OUT_OLD, OUT_NEW)
                print(f"{fname}: OUT repointed -> {OUT_NEW}")
            elif OUT_NEW in src:
                print(f"{fname}: OUT already repointed")
            else:
                assert False, f"{fname}: OUT path not found"
        io.open(path, "w", encoding="utf-8").write(src)
    for fname, pairs in SHORTEN_PAIRS.items():
        path = os.path.join(HERE, fname)
        src = io.open(path, encoding="utf-8").read()
        for old, new in pairs:
            n = src.count(old)
            if n == 0 and new in src:
                print(f"{fname}: SHORTEN SKIP already applied :: {old[:70]}")
                continue
            assert n >= 1, f"{fname}: SHORTEN NOT FOUND: {old[:90]}"
            src = src.replace(old, new)
            print(f"{fname}: SHORTEN x{n} :: {old[:70]}")
        io.open(path, "w", encoding="utf-8").write(src)
    for fname, pairs in FIX2_PAIRS.items():
        path = os.path.join(HERE, fname)
        src = io.open(path, encoding="utf-8").read()
        for old, new in pairs:
            n = src.count(old)
            if n == 0 and new in src:
                print(f"{fname}: FIX2 SKIP already applied :: {old[:70]}")
                continue
            assert n >= 1, f"{fname}: FIX2 NOT FOUND: {old[:90]}"
            src = src.replace(old, new)
            print(f"{fname}: FIX2 x{n} :: {old[:70]}")
        io.open(path, "w", encoding="utf-8").write(src)
    # render.py BASE repoint
    rp = os.path.join(HERE, "render.py")
    src = io.open(rp, encoding="utf-8").read()
    if OUT_OLD in src:
        src = src.replace(OUT_OLD, OUT_NEW)
        io.open(rp, "w", encoding="utf-8").write(src)
        print(f"render.py: BASE repointed -> {OUT_NEW}")
    elif OUT_NEW in src:
        print("render.py: BASE already repointed")
    else:
        assert False, "render.py: BASE not found"
    # instr= translations (after all bridges, so bare fragments are safe)
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        path = os.path.join(HERE, fname)
        src = io.open(path, encoding="utf-8").read()
        for old, new in [('instr="填空"', 'instr="Ausfüllen"'),
                         ('instr="判断"', 'instr="Richtig oder falsch"'),
                         ('instr="造句"', 'instr="Sätze bilden"'),
                         ('instr="改写"', 'instr="Umformen"'),
                         ('instr="翻译"', 'instr="Übersetzen"'),
                         ('instr="写作"', 'instr="Schreiben"'),
                         ('instr="把词和释义配对"', 'instr="Zuordnen"')]:
            n = src.count(old)
            if n:
                src = src.replace(old, new)
                print(f"{fname}: instr x{n} :: {old} -> {new}")
        io.open(path, "w", encoding="utf-8").write(src)
    print(f"TOTAL literal replacements: {total}")

if __name__ == "__main__":
    main()
