# -*- coding: utf-8 -*-
"""DE x ES fan-out transform for W46 DE core build copy.
Generated from the EN pair table + tr-es.py. German body text is
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
    rep(f, "weekly-report-w46-de-core", "weekly-report-w46-de-es", 1)

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
    '"Die Lucerna · SEMANARIO ALEMÁN VOL.3 · TEXTO EN ALEMÁN · EXPLICACIONES EN ESPAÑOL"', 1)
rep("bslib4.py", 'f"\u7b2c {n} \u7248 / \u5171 {total} \u7248"', 'f"Página {n} de {total}"', 1)
rep("bslib4.py", '"\u8bd1\u6ce8\uff5c" + s', '"Nota — " + s', 1)

# ================= content12.py =================
C12 = [
    ('WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语', 'WÖCHENTLICH AUF DEUTSCH · CADA SEMANA · EL ALEMÁN QUE LEEN LOS ALEMANES'),
    ('德 语 周 报 · VOL.3 · 国 家 队 · 圣 马 丁 · NFL', 'SEMANARIO ALEMÁN · VOL.3 · SELECCIÓN · SAN MARTÍN · NFL'),
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")', 'p.text(975, 372, "TEXTOS EN ALEMÁN · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 20, "sans", True, BRICK, anchor="middle")'),
    ('本周国家队周 · 圣马丁节与 NFL', 'SEMANA DE SELECCIONES · SAN MARTÍN Y NFL'),
    ('详见第 4 版 · Seite 4', 'Ver página 4'),
    ('DIE TOPMELDUNG · 头条', 'DIE TOPMELDUNG · Titular'),
    ('讲解｜die Länderspielpause 国家队比赛间歇期 · das Viertelfinale 四分之一决赛 · ausverkauft 售罄。', 'Notas — die Länderspielpause = parón de selecciones · das Viertelfinale = cuartos de final · ausverkauft = agotado.'),
    ('DIE WOCHE IN ZAHLEN · 数字看本周', 'DIE WOCHE IN ZAHLEN · En cifras'),
    ('5 — Punkte hat Deutschland nach vier Spielen in der Nations League（四轮过后德国队 5 分）', '5 — Punkte hat Deutschland nach vier Spielen in der Nations League (Alemania suma 5 puntos tras cuatro partidos)'),
    ('11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（11 点 11 分狂欢季开幕）', '11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln (el carnaval empieza a las 11.11)'),
    ('15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（周日 15 点 30 分 NFL 开球）', '15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München (el partido de la NFL empieza el domingo a las 15.30)'),
    ('JETZT ÜBEN · 即学即练', 'JETZT ÜBEN · A practicar'),
    ('国家队比赛周', 'semana de parón de selecciones'),
    ('塞尔维亚首都', 'capital de Serbia'),
    ('狂欢季 11 点 11 分开幕', 'el carnaval empieza a las 11.11'),
    ('NFL 在慕尼黑', 'la NFL en Múnich'),
    ('四轮 5 分', '5 puntos tras cuatro partidos'),
    ('周日是纪念日', 'el domingo es el día de recuerdo'),
    ('圣马丁节 11 月 11 日', 'San Martín es el 11 de noviembre'),
    ('11 月 11 日是星期三', 'el 11 de noviembre es miércoles'),
    ('本周大问题 · Die Fragen der Woche', 'Grandes preguntas · Die Fragen der Woche'),
    ('德国本周最热议的五个问题。', 'Las cinco preguntas que agitan Alemania.'),
    ('IN DIESER AUSGABE · 本期目录', 'IN DIESER AUSGABE · Sumario'),
    ('空场比赛（无观众）。详见第 4 版。', 'Un partido sin espectadores. Ver página 4.'),
    ('KURZ & GUT · 快讯', 'KURZ & GUT · En breve'),
    ('BLITZQUIZ · 闪电问答', 'BLITZQUIZ · Quiz relámpago'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Lee la portada y elige la respuesta correcta · Respuestas en la página 8'),
    ('周五客战塞尔维亚', 'fuera, en Serbia, el viernes'),
    ('NFL 下午 3 点半开球', 'la NFL empieza a las 15.30'),
    ('纪念日在周日', 'el día de recuerdo es el domingo'),
    ('LEBEN · 生活', 'LEBEN · La vida'),
    ('LEVEL A2 · Der 11. November & der Alltag · 11 月 11 日与日常生活', 'LEVEL A2 · Der 11. November & der Alltag · El 11 de noviembre y la vida diaria'),
    ('der Jeck 狂欢者（科隆方言） · die fünfte Jahreszeit 第五个季节（狂欢季） · die Laterne 灯笼 · der Weckmann 面人面包 · die Martinsgans 圣马丁鹅。', 'der Jeck = juerguista del carnaval (dialecto de Colonia) · die fünfte Jahreszeit = la quinta estación (carnaval) · die Laterne = farolillo · der Weckmann = muñeco de pan · die Martinsgans = oca de San Martín.'),
    ('DER 11. NOVEMBER · 11 月 11 日', 'DER 11. NOVEMBER'),
    ('你过狂欢节还是圣马丁节？写两句德语寄来。', '¿Carnaval o San Martín? ¡Escribe dos frases en alemán!'),
    ('UND SIE? · 说说你自己', 'UND SIE? · ¿Y tú?'),
    ('MARTIN IN KÜRZE · 圣马丁简讯', 'MARTIN IN KÜRZE · En breve'),
    ('RECHNEN WIR MAL · 算一算', 'RECHNEN WIR MAL · Calculemos'),
    ('Die Uhrzeiten der Woche · 本周时刻', 'Die Uhrzeiten der Woche · Las horas de la semana'),
    ('注意：11 月 11 日是工作日。去科隆要早到：老城很挤，晚上街道属于提灯笼的孩子们。', 'Nota: el 11 de noviembre es laborable. Llega pronto a Colonia: el casco antiguo está lleno y por la noche las calles son de los niños con sus farolillos.'),
    ('ÜBUNGEN · 第 2 版练习', 'ÜBUNGEN · Ejercicios página 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Respuestas en la página 8 · Los niveles se mezclan: busca cada respuesta por su número'),
    ('看第 2 版文章，用时间填空。', 'Lee el artículo de la página 2 y completa las horas.'),
    ('WDR 10 点半直播', 'la WDR en directo desde las 10.30'),
    ('Weckmann 是面人面包', 'un Weckmann es un muñeco de pan'),
    ('11 月 11 日不是法定假日', 'el 11 de noviembre no es festivo'),
    ('圣马丁鹅配红甘蓝和丸子', 'la oca de San Martín con lombarda y albóndigas de pan'),
    ('改成 Perfekt 现在完成时。', 'Reescribe en Perfekt (pretérito perfecto).'),
    ('读第 2 版文章，选出正确答案。', 'Lee el artículo de la página 2 y elige la respuesta correcta.'),
    ('Jeck=狂欢者 c', 'Jeck=juerguista del carnaval c'),
    ('Laterne=灯笼 a', 'Laterne=farolillo a'),
    ('Weckmann=面人面包 b', 'Weckmann=muñeco de pan b'),
    ('Martinsgans=圣马丁鹅 d', 'Martinsgans=oca de San Martín d'),
]
rep_all("content12.py", C12)

# ================= content34.py =================
C34 = [
    ('KULTUR · 文化', 'KULTUR · Cultura'),
    ('A2 → B1 · St. Martin, Karneval & Rückblick · 圣马丁、狂欢节与回顾', 'A2 → B1 · St. Martin, Karneval & Rückblick · San Martín, carnaval y mirada atrás'),
    ('der Bettler 乞丐 · der Mantel 斗篷 · das Geschnatter 鹅叫声 · der Gänsestall 鹅棚 · das Dreigestirn 狂欢节三人组。', 'der Bettler = mendigo · der Mantel = manto · das Geschnatter = graznido · der Gänsestall = establo de las ocas · das Dreigestirn = triunvirato del carnaval.'),
    ('ST. MARTIN · 圣马丁', 'ST. MARTIN · San Martín'),
    ('die Laterne — 灯笼', 'die Laterne — farolillo'),
    ('der Mantel — 斗篷', 'der Mantel — manto'),
    ('die Gans — 鹅', 'die Gans — oca'),
    ('der Weckmann — 面人面包', 'der Weckmann — muñeco de pan'),
    ('das Martinsfeuer — 圣马丁篝火', 'das Martinsfeuer — hoguera de San Martín'),
    ('das Kostüm — 服装', 'das Kostüm — disfraz'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · San Martín'),
    ('UND SIE? · 说说你自己', 'UND SIE? · ¿Y tú?'),
    ('你做过灯笼吗？你们国家的孩子唱什么歌？写两句德语寄来。', '¿Hiciste un farolillo? ¡Escribe dos frases en alemán!'),
    ('DER TIPP · 编辑部建议', 'DER TIPP · Consejo'),
    ('ÜBUNGEN · 第 3 版练习', 'ÜBUNGEN · Ejercicios página 3'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Respuestas en la página 8 · Los niveles se mezclan: busca cada respuesta por su número'),
    ('读第 3 版文章，判断对错。', 'Lee el artículo de la página 3. ¿Verdadero o falso?'),
    ('传说马丁是罗马士兵', 'la leyenda dice que Martín era soldado romano'),
    ('传说鹅叫声暴露了他', 'la leyenda dice que las ocas lo delataron'),
    ('纪念日 11 月 11 日', 'el día conmemorativo es el 11 de noviembre'),
    ('截稿时 11 月 3–8 日结果未知', 'resultados del 3 al 8 de noviembre desconocidos al cierre'),
    ('狂欢季 11 点 11 分开幕', 'el carnaval empieza a las 11.11'),
    ('用方框里的词填空。', 'Completa con las palabras del recuadro.'),
    ('斗篷分给乞丐', 'el manto compartido con el mendigo'),
    ('纸灯笼', 'un farolillo de papel'),
    ('圣马丁鹅', 'la oca de San Martín'),
    ('圣马丁鹅配红甘蓝和丸子', 'la oca de San Martín con lombarda y albóndigas de pan'),
    ('狂欢节服装', 'un disfraz de carnaval'),
    ('游行在篝火处结束', 'la procesión termina en la hoguera'),
    ('选出正确答案。', 'Elige la respuesta correcta.'),
    ('马丁后来成为图尔主教', 'Martín llegó a ser obispo de Tours'),
    ('灯笼游行常在前后晚上举行', 'las procesiones de farolillos suelen ser en noches cercanas'),
    ('VOL.4 报道 11 月 3–8 日结果', 'VOL.4 contará los resultados del 3 al 8 de noviembre'),
    ('把词组成正确的句子。', 'Ordena las palabras en una frase correcta.'),
    ('主谓宾顺序', 'orden sujeto–verbo–objeto'),
    ('时间状语开头，动词第二位', 'el tiempo primero, el verbo en segundo lugar'),
    ('地点开头，动词第二位', 'el lugar primero, el verbo en segundo lugar'),
    ('SPORT · 体育', 'SPORT · Deporte'),
    ('LEVEL B1 · Nationalelf & NFL · 国家队与 NFL', 'LEVEL B1 · Nationalelf & NFL · Selección y NFL'),
    ('das Geisterspiel 空场比赛 · das Hinspiel 首回合 · ausverkauft 售罄 · der Star 明星 · gewinnen 获胜。', 'das Geisterspiel = partido fantasma · das Hinspiel = partido de ida · ausverkauft = agotado · der Star = estrella · gewinnen = ganar.'),
    ('你更爱看足球还是美式橄榄球？贝尔格莱德谁赢？写两句德语寄来。', '¿Fútbol o fútbol americano? ¿Quién gana? ¡Dos frases!'),
    ('DER SPIELPLAN · 本周与下周赛程', 'DER SPIELPLAN · Esta semana y la siguiente'),
    ('ÜBUNGEN · 第 4 版练习', 'ÜBUNGEN · Ejercicios página 4'),
    ('读第 4 版文章，选出正确答案。', 'Lee el artículo de la página 4 y elige la respuesta correcta.'),
    ('德国 5 分，荷兰希腊各 8 分', 'Alemania 5 puntos, Países Bajos y Grecia 8 cada uno'),
    ('主教练 11 月 5 日公布名单', 'el seleccionador anuncia la lista el 5 de noviembre'),
    ('贝尔格莱德空场', 'estadio vacío en Belgrado'),
    ('首回合德国 2:0 胜塞尔维亚', 'Alemania ganó la ida 2-0 contra Serbia'),
    ('NFL 慕尼黑赛售罄', 'el partido de la NFL en Múnich está agotado'),
    ('Geisterspiel=空场比赛 b', 'Geisterspiel=partido fantasma b'),
    ('Hinspiel=首回合 a', 'Hinspiel=partido de ida a'),
    ('Ausrüster=装备赞助商 c', 'Ausrüster=proveedor de equipaciones c'),
    ('ausverkauft=售罄 d', 'ausverkauft=agotado d'),
    ('用比较级完成句子（括号里是原级）。', 'Completa con el comparativo (la palabra entre paréntesis es el positivo).'),
    ('viel → mehr（荷兰 8 分多于德国 5 分）', 'viel → mehr (Países Bajos tiene 8 puntos, más que los 5 de Alemania)'),
    ('spät → später（15:30 晚于 11:11）', 'spät → später (las 15.30 es más tarde que las 11.11)'),
    ('leise → leiser（空场比主场安静）', 'leise → leiser (un estadio vacío es más silencioso que un partido en casa)'),
    ('früh → früher（11 月 5 日早于 11 月 13 日）', 'früh → früher (el 5 de noviembre es antes que el 13 de noviembre)'),
    ('看上面的赛程表，选出正确答案。', 'Mira el calendario de arriba y elige la respuesta correcta.'),
    ('塞尔维亚–德国周五 20:45', 'Serbia–Alemania el viernes a las 20.45'),
    ('NFL 周日 15:30', 'NFL el domingo a las 15.30'),
    ('德国–荷兰周一 20:45', 'Alemania–Países Bajos el lunes a las 20.45'),
    ('拜仁–科隆周五 20:30', 'Bayern–Colonia el viernes a las 20.30'),
    ('沙尔克–斯图加特周六 17:30', 'Schalke–Stuttgart el sábado a las 17.30'),
]
rep_all("content34.py", C34)

# ================= content56.py =================
C56 = [
    ('JUGEND · 青年', 'JUGEND · Juventud'),
    ('LEVEL B1 · Laternen, Lieder & Schule · 灯笼、歌曲与学校', 'LEVEL B1 · Laternen, Lieder & Schule · Farolillos, canciones y escuela'),
    ('basteln 制作 · der Pausenhof 课间操场 · sich verkleiden 乔装打扮 · die Stimmung 气氛 · der Pirat 海盗。', 'basteln = hacer manualidades · der Pausenhof = patio · sich verkleiden = disfrazarse · die Stimmung = ambiente · der Pirat = pirata.'),
    ('SCHULWOCHE · 开学周', 'SCHULWOCHE · Vuelta al cole'),
    ('die Laterne — 灯笼', 'die Laterne — farolillo'),
    ('basteln — 制作', 'basteln — hacer manualidades'),
    ('das Lied — 歌曲', 'das Lied — canción'),
    ('das Kostüm — 服装', 'das Kostüm — disfraz'),
    ('der Umzug — 游行', 'der Umzug — procesión'),
    ('der Stern — 星星', 'der Stern — estrella'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · San Martín'),
    ('UND SIE? · 说说你自己', 'UND SIE? · ¿Y tú?'),
    ('你小时候做过灯笼吗？11 月你唱哪首歌？写两句德语寄来。', '¿Un farolillo de niño? ¿Tu canción? ¡Dos frases!'),
    ('DER WOCHENPLAN DER REDAKTION · 编辑部一周计划', 'DER WOCHENPLAN DER REDAKTION · La semana de la redacción'),
    ('ÜBUNGEN · 第 5 版练习', 'ÜBUNGEN · Ejercicios página 5'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Respuestas en la página 8 · Los niveles se mezclan: busca cada respuesta por su número'),
    ('读第 5 版文章，选出正确答案。', 'Lee el artículo de la página 5 y elige la respuesta correcta.'),
    ('11 月 9 日全德复课', 'las clases vuelven en todas partes el 9 de noviembre'),
    ('孩子们做纸灯笼', 'los niños hacen farolillos de papel'),
    ('纸灯笼', 'un farolillo de papel'),
    ('上午狂欢，下午圣马丁', 'carnaval por la mañana, San Martín por la tarde'),
    ('NFL 周日在电视上', 'la NFL en la tele el domingo'),
    ('周五看国家队比赛', 'ver a la selección el viernes'),
    ('用方框里的词填空。', 'Completa con las palabras del recuadro.'),
    ('做灯笼', 'hacer farolillos'),
    ('唱圣马丁歌曲', 'cantar canciones de San Martín'),
    ('狂欢节服装', 'un disfraz de carnaval'),
    ('灯笼游行', 'una procesión de farolillos'),
    ('灯笼上的星星', 'la estrella del farolillo'),
    ('用 weil 连接两个句子（动词放句末）。', 'Une las dos frases con weil (el verbo va al final).'),
    ('weil 句动词置尾', 'en una subordinada con weil, el verbo va al final'),
    ('ist 置尾', 'ist va al final'),
    ('will 置尾', 'will va al final'),
    ('beginnt 置尾', 'beginnt va al final'),
    ('判断对错。', '¿Verdadero o falso?'),
    ('11 月 9 日巴伐利亚也复课', 'Baviera también vuelve el 9 de noviembre'),
    ('灯笼游行在晚上', 'la procesión de farolillos es por la noche'),
    ('孩子们唱圣马丁歌曲', 'los niños cantan canciones de San Martín'),
    ('VERTIEFUNG · 深读', 'VERTIEFUNG · Lectura a fondo'),
    ('LEVEL B2 · Volkstrauertag & Stromsteuer · 纪念日与电力税', 'LEVEL B2 · Volkstrauertag & Stromsteuer · Día de recuerdo e impuesto eléctrico'),
    ('gedenken 纪念 · die Kranzniederlegung 献花圈 · der stille Tag 安静日 · die Verbundenheit 联系 · die Versöhnung 和解。', 'gedenken = conmemorar · Kranzniederlegung = ofrenda · stille Tag = día de silencio · Verbundenheit = vínculo · Versöhnung = reconciliación.'),
    ('DIE ZAHLEN · 本周数字', 'DIE ZAHLEN · Las cifras'),
    ('纪念日：纪念需要安静——对此几乎人人赞同。电力税：降多少尚未确定。两者都关系到几乎每个家庭。', 'Día de recuerdo: recordar pide silencio — casi todos están de acuerdo. Impuesto eléctrico: cuánto baja sigue abierto. Ambos afectan a casi cada hogar.'),
    ('ZWEI SONNTAGE IM NOVEMBER · 十一月的两个周日', 'ZWEI SONNTAGE IM NOVEMBER · Dos domingos de noviembre'),
    ('WAS INTERESSIERT DIE LESER? · 读者最关心什么？', 'WAS INTERESSIERT DIE LESER? · ¿Qué interesa a los lectores?'),
    ('("Nations League und NFL", 46, "足球")', '("Nations League und NFL", 46, "fútbol")'),
    ('("St. Martin und Karneval", 34, "节日")', '("St. Martin und Karneval", 34, "fiestas")'),
    ('("Volkstrauertag und Gedenken", 20, "纪念")', '("Volkstrauertag und Gedenken", 20, "memoria")'),
    ('ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）', 'ÜBUNGSDATEN · Datos de práctica — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Datos de práctica, no una encuesta real.)'),
    ('ÜBUNGEN · 第 6 版练习', 'ÜBUNGEN · Ejercicios página 6'),
    ('看上面的练习图表，选出正确答案。', 'Usa el gráfico de práctica de arriba.'),
    ('46% 足球最受关注', 'el fútbol lidera con el 46 %'),
    ('节日 34% 第二', 'las fiestas segundas con el 34 %'),
    ('纪念 20% 最小', 'el recuerdo el menor con el 20 %'),
    ('纪念 20%', 'el recuerdo 20 %'),
    ('读第 6 版深读文章，选出正确答案。', 'Lee el artículo de la página 6.'),
    ('11 月 15 日纪念日', 'el día de recuerdo es el 15 de noviembre'),
    ('ZDF 13 点半直播纪念仪式', 'la ZDF en directo desde las 13.30'),
    ('家庭电力税 2.05 欧分', 'el impuesto de los hogares es 2,05 céntimos'),
    ('2027 年预算 11 月 27 日表决', 'votación del presupuesto 2027 el 27 de noviembre'),
    ('用括号里的形式填空。', 'Completa con la forma entre paréntesis.'),
    ('被动：wird + Partizip II', 'pasiva: wird + participio pasado'),
    ('ob 引导间接疑问句', 'ob introduce una pregunta indirecta'),
    ('献花圈仪式', 'una ceremonia de ofrenda floral'),
    ('为和平与和解', 'por la paz y la reconciliación'),
    ('德奥联系', 'el vínculo germano-austríaco'),
    ('纪念受害者', 'recordar a las víctimas'),
]
rep_all("content56.py", C56)

# ================= content7.py =================
C7 = [
    ('SPRACHE · 语言', 'SPRACHE · La lengua'),
    ('A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所', 'A2 → B2 · Sätze der Woche & Fehlerklinik · Frases de la semana y clínica de errores'),
    ('本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。', 'Esta página va de lengua: tres lecciones cortas, las frases de la semana (citadas palabra por palabra de los artículos de este número), la clínica de errores y las cartas de los lectores.'),
    ('BEISPIELE · 例句', 'BEISPIELE · Ejemplos'),
    ('被动：wird + Partizip II', 'pasiva: wird + participio pasado'),
    ('复数：werden', 'plural: werden'),
    ('werden + 原形表将来', 'werden + infinitivo para el futuro'),
    ('被动语态', 'voz pasiva'),
    ('lang → länger（夜晚比白天长）', 'lang → länger (la noche es más larga que el día)'),
    ('weil 引导原因', 'weil introduce una causa'),
    ('weil 句动词置尾', 'en una subordinada con weil, el verbo va al final'),
    ('länger als = 比……更长', 'länger als = más largo que'),
    ('„Länger als sonst“ heißt... A. 比平时更长 · B. 和平时一样 · C. 比平时更短', '„Länger als sonst“ significa... A. más largo que de costumbre · B. igual que de costumbre · C. más corto que de costumbre'),
    ('ob 引导间接疑问', 'ob introduce una pregunta indirecta'),
    ('Es ist fraglich, ob ... = 是否还难说', 'Es ist fraglich, ob ... = es dudoso que ...'),
    ('dass 句动词置尾', 'en una subordinada con dass, el verbo va al final'),
    ('礼貌表达观点', 'una forma educada de dar una opinión'),
    ('11.11 Uhr = 11 点 11 分', '11.11 Uhr = 11.11'),
    ('vor leeren Rängen = 空场，没有观众', 'vor leeren Rängen = estadio vacío'),
    ('Es wird gespielt. = 比赛将进行（被动）', 'Es wird gespielt. = Se jugará'),
    ('Meiner Meinung nach ... = 在我看来……', 'Meiner Meinung nach = en mi opinión'),
    ('Ich finde, dass ... = 我觉得……', 'Ich finde, dass = creo que'),
    ('Es ist fraglich, ob ... = 是否……还难说', 'Es ist fraglich, ob ... = es dudoso que'),
    ('DER WERKZEUGKASTEN · 工具箱', 'DER WERKZEUGKASTEN'),
    ('label = "Ein Beispiel der Redaktion!"', 'label = "¡Un ejemplo de la redacción!"'),
    ('编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.4。请寄来您的习作，优秀者刊登于 VOL.4。', 'Ejemplo de la redacción, no una carta real: ninguna carta real había llegado al cierre. ¡Envíanos las tuyas para VOL.4!'),
    ('LESERBRIEFE · 读者来信', 'LESERBRIEFE · Cartas'),
    ('NOCH EIN WORT · 再学一词', 'NOCH EIN WORT · Una palabra más'),
    ('«das Geisterspiel»（Seite 4）: ein Spiel ohne Zuschauer im Stadion. 空场比赛。', '«das Geisterspiel» (Seite 4) : ein Spiel ohne Zuschauer im Stadion. Partido fantasma: un partido sin espectadores.'),
    ('SÄTZE DER WOCHE · 本周金句', 'SÄTZE DER WOCHE · Frases de la semana'),
    ('原文摘录，逐字引自本期文章 · 括号内为出处', 'Citado palabra por palabra de los artículos de este número · fuente entre corchetes'),
    ('德甲休战——但国家队要比赛。', 'La Bundesliga se detiene — pero la selección juega.'),
    ('11 点 11 分，科隆新一季狂欢季开幕。', 'A las 11.11 empieza en Colonia la nueva sesión del carnaval.'),
    ('他的纪念日是 11 月 11 日。', 'Su día conmemorativo es el 11 de noviembre.'),
    ('书包收拾好了，操场上又热闹起来。', 'Las mochilas están listas, los patios vuelven a sonar.'),
    ('十一月黑暗，但并不安静：它歌唱、发光、庆祝。', 'Noviembre es oscuro, pero no silencioso: canta, brilla y celebra.'),
    ('比赛售罄，RTL 现场直播。', 'El partido está agotado; RTL transmite en directo.'),
    ('这里的纪念意味着：停下来、记住——并为和平与和解挺身而出。', 'Aquí, recordar significa: detenerse, recordar — y defender la paz y la reconciliación.'),
    ('周日，全国一片安静。', 'El domingo, el país está en silencio.'),
    ('FEHLERKLINIK · 纠错诊所', 'FEHLERKLINIK · La clínica de errores'),
    ('学习者最常犯的四个错 · 先自己改，再看答案', 'Cuatro errores frecuentes de los estudiantes · corrígelos primero, luego comprueba'),
    ('动词第二位：主语不在句首时，动词仍居第二。', 'Verbo en segundo lugar: aunque el sujeto no vaya primero, el verbo queda segundo.'),
    ('halb zwölf = 十一点半（zwölf 之前）。', 'halb zwölf = las 11.30, media hora antes de zwölf.'),
    ('Perfekt 中 Partizip II 放句末。', 'En el Perfekt, el participio pasado va al final.'),
    ('ob 从句动词放句末。', 'En una subordinada con ob, el verbo va al final.'),
    ('IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.4)', 'IN DER NÄCHSTEN AUSGABE · Próximo número (VOL.4)'),
]
rep_all("content7.py", C7)

# ================= content8.py =================
C8 = [
    ('ÜBUNGEN & ANTWORTEN · 练习与答案', 'ÜBUNGEN & ANTWORTEN · Ejercicios y respuestas'),
    ('SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方', 'SCHLUSSTEST · Prueba final · Alle Antworten unten auf dieser Seite — todas las respuestas abajo en esta página'),
    ('beginnt（第三人称单数）', 'beginnt (3.ª pers. sing.)'),
    ('bastelt（第三人称单数）', 'bastelt (3.ª pers. sing.)'),
    ('geht（第三人称单数）', 'geht (3.ª pers. sing.)'),
    ('singt（第三人称单数）', 'singt (3.ª pers. sing.)'),
    ('schaut（第三人称单数）', 'schaut (3.ª pers. sing.)'),
    ('sieht（第三人称单数）', 'sieht (3.ª pers. sing.)'),
    ('erzählt（第三人称单数）', 'erzählt (3.ª pers. sing.)'),
    ('A · LÜCKENTEXT · 完形填空', 'A · LÜCKENTEXT · Huecos'),
    ('选项：', 'Opciones:'),
    ('B · WISSENSFRAGEN · 综合问答', 'B · WISSENSFRAGEN · Quiz'),
    ('狂欢季 11 点 11 分开幕', 'el carnaval empieza a las 11.11'),
    ('周五客战塞尔维亚', 'fuera, en Serbia, el viernes'),
    ('NFL 周日 15:30', 'NFL el domingo a las 15.30'),
    ('纪念日 11 月 15 日', 'el día de recuerdo es el 15 de noviembre'),
    ('家庭电力税 2.05 欧分', 'el impuesto de los hogares es 2,05 céntimos'),
    ('主教练 11 月 5 日公布名单', 'el seleccionador anuncia la lista el 5 de noviembre'),
    ('ZDF 13 点半直播纪念仪式', 'la ZDF en directo desde las 13.30'),
    ('亡灵主日 11 月 22 日', 'Totensonntag es el 22 de noviembre'),
    ('C · LESEVERSTEHEN · 阅读理解', 'C · LESEVERSTEHEN · Lectura'),
    ('周三做灯笼', 'hacer un farolillo el miércoles'),
    ('周五看德国队', 'ver a Alemania el viernes'),
    ('D · SÄTZE BAUEN · 造句', 'D · SÄTZE BAUEN · Formar frases'),
    ('时间状语，动词第二位', 'el tiempo, el verbo en segundo lugar'),
    ('主谓宾顺序', 'orden sujeto–verbo–objeto'),
    ('时间状语开头，动词第二位', 'el tiempo primero, el verbo en segundo lugar'),
    ('地点时间开头，动词第二位', 'lugar y tiempo primero, verbo en segundo lugar'),
    ('E · ÜBERSETZEN · 翻译', 'E · ÜBERSETZEN · Traducción'),
    ('狂欢节 11 点 11 分在科隆开幕。', 'El carnaval empieza a las 11.11 en Colonia.'),
    ('beginnen = 开始', 'beginnen = empezar'),
    ('Der Karneval beginnt um 11.11 Uhr in Köln.（译成中文）', 'Der Karneval beginnt um 11.11 Uhr in Köln. (traducir al español)'),
    ('我周三做一个灯笼。', 'Hago un farolillo el miércoles.'),
    ('basteln = 制作', 'basteln = hacer manualidades'),
    ('Ich bastle am Mittwoch eine Laterne.（译成中文）', 'Ich bastle am Mittwoch eine Laterne. (traducir al español)'),
    ('学校 11 月 9 日又开学了。', 'Las clases volvieron a empezar el 9 de noviembre.'),
    ('wieder begonnen = 又开始', 'wieder begonnen = vuelto a empezar'),
    ('Die Schule hat am 9. November wieder begonnen.（译成中文）', 'Die Schule hat am 9. November wieder begonnen. (traducir al español)'),
    ('看比赛 = das Spiel schauen', 'ver un partido = das Spiel schauen'),
    ('"我周日看 NFL 比赛。（译成德语）", instr="翻译"', '"Veo el partido de la NFL el domingo. (traducir al alemán)", instr="Traduce al alemán"'),
    ('F · WÖRTER PAAREN · 词汇配对', 'F · WÖRTER PAAREN · Parejas'),
    ('Mantel=斗篷 b', 'Mantel=manto b'),
    ('Laterne=灯笼 a', 'Laterne=farolillo a'),
    ('Geisterspiel=空场比赛 d', 'Geisterspiel=partido fantasma d'),
    ('Versöhnung=和解 c', 'Versöhnung=reconciliación c'),
    ('singst（第二人称单数）', 'singst (2.ª pers. sing.)'),
    ('macht（第二人称复数）', 'macht (2.ª pers. pl.)'),
    ('essen（第一人称复数）', 'essen (1.ª pers. pl.)'),
    ('machst（第二人称单数）', 'machst (2.ª pers. sing.)'),
    ('schaue（第一人称单数）', 'schaue (1.ª pers. sing.)'),
    ('G · DIALOG · 对话补全', 'G · DIALOG · Completar el diálogo'),
    ('开放题 — 要点见写作框，范文在第 8 版写作框内', 'Tarea abierta — sigue los puntos del recuadro; el texto modelo está en el recuadro de esta página'),
    ('按要点给分', 'Se evalúa según los puntos listados'),
    ('H · SCHREIBEN · 写作', 'H · SCHREIBEN · Redacción'),
    ('用德语写 80–100 词：《我的十一月的一周》。写清做什么手工、看哪几场比赛、和谁一起，并写一句关于圣马丁节或纪念日的话。', 'Escribe en alemán, 80–100 palabras: «Mi semana de noviembre». Di qué haces, qué partidos ves y con quién — y añade una frase sobre San Martín o el día de recuerdo.'),
    ('MUSTER · 范文（84 Wörter）', 'MUSTER · Texto modelo (84 palabras)'),
    ('ANTWORTEN · 全部答案与简析（第 1–8 版）', 'ANTWORTEN · Todas las respuestas con notas (páginas 1–8)'),
]
rep_all("content8.py", C8)

# ---------- P8 keys ----------
rep("content8.py", 'kf.para(f"— \u7b2c {pg} \u7248 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— Página {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"\uff08{e[\'note\']}\uff09"',
    's += f" ({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 12, "sans", False, INK, 1.22, 9)', 1)

# ---------- generic value maps ----------
TYPEMAP = [('完成句子', 'completar'), ('单选', 'opción múltiple'), ('句型转换', 'transformación'), ('词汇配对', 'emparejar'), ('判断对错', 'verdadero/falso'), ('完形填空', 'Huecos'), ('造句', 'formar frases'), ('对话补全', 'Completar el diálogo'), ('翻译', 'traducción'), ('写作', 'Redacción')]
INSTRMAP = [('instr="填空"', 'instr="Completa"'), ('instr="改写"', 'instr="Reescribe"'), ('instr="判断"', 'instr="¿Verdadero o falso?"'), ('instr="造句"', 'instr="Forma la frase"'), ('instr="翻译"', 'instr="Traduce al español"'), ('instr="把词和释义配对"', 'instr="Une las parejas"')]
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
