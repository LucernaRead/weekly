# -*- coding: utf-8 -*-
"""NL core (Chinese explanation layer) -> NL x ES (Spanish explanation layer).
Exact quoted-literal replacements only, with per-string occurrence assertions.
Frozen Dutch target text is never touched; the only Dutch-text exceptions are:
 (a) P8 E-section: 2 keys translated NL->ES, 2 prompts flipped ES->NL (W43 precedent);
 (b) P7 readers'-corner example persona Li/Shanghai -> Lucia/Madrid (W43 NLxES precedent,
     documented reader-language entry, still labeled voorbeeldbrief van de redactie);
 (c) P7 word-box gloss line only (definition sentence verbatim).
Type names: renamed to Spanish ONLY in content8 (W43 NLxES precedent: 38 P8 items).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

def rep(path, old, new, expect=None):
    with open(path, encoding="utf-8") as fh:
        txt = fh.read()
    qold, qnew = '"%s"' % old, '"%s"' % new
    n = txt.count(qold)
    if expect is not None:
        assert n == expect, "%s: %r found %d times, expected %d" % (path, old, n, expect)
    else:
        assert n >= 1, "%s: %r not found" % (path, old)
    txt = txt.replace(qold, qnew)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(txt)
    return n

def apply_map(path, mapping):
    for old, new, *exp in mapping:
        rep(path, old, new, exp[0] if exp else None)

GLOBAL = [
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案", "Respuestas en la página 8 · Busca tu número para encontrar la respuesta"),
    ("科弗登发放 200 棵树木灌木", "Coevorden reparte 200 árboles y arbustos"),
    ("博物馆之夜在 11 月 7 日周六", "La Museumnacht es el sábado 7 de noviembre"),
    ("特温特–阿贾克斯 13:30 开球", "El Twente – Ajax empieza a las 13:30"),
    ("阿贾克斯 2–0 赢亚特兰大", "El Ajax ganó 2–0 al Atalanta"),
    ("皇家贝蒂斯 1–0 赢费耶诺德", "El Real Betis ganó 1–0 al Feyenoord"),
    ("Crossing Border 在海牙", "Crossing Border es en La Haya"),
    ("发放地点在兹韦洛", "El reparto es en Zweeloo"),
    ("预警疲劳：警告太多导致不再注意", "Cansancio ante las alertas: tantas alertas que ya no se presta atención"),
    ("用方框里的词填空。", "Completa con las palabras del recuadro."),
    ("把词和释义配对", "Relacionar"),
]
INSTR = [("填空", "Completar"), ("判断", "¿Verdadero o falso?"), ("造句", "Formar la frase")]

for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    p = os.path.join(HERE, f)
    for old, new in GLOBAL:
        with open(p, encoding="utf-8") as fh:
            txt = fh.read()
        if ('"%s"' % old) in txt:
            rep(p, old, new)
    for old, new in INSTR:
        with open(p, encoding="utf-8") as fh:
            txt = fh.read()
        key = 'instr="%s"' % old
        if key in txt:
            n = txt.count(key)
            txt = txt.replace(key, 'instr="%s"' % new)
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(txt)
            print(f, "instr", old, "->", new, "x", n)

C12 = os.path.join(HERE, "content12.py")
apply_map(C12, [
    ("ELKE WEEK IN HET NEDERLANDS · 每周一期 · 读荷兰人正在读的荷兰语", "ELKE WEEK IN HET NEDERLANDS · CADA SEMANA EN NEERLANDÉS", 1),
    ("荷 兰 语 周 报 · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12", "SEMANARIO NEERLANDÉS · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12", 1),
    ("气候周", "SEMANA DEL CLIMA", 1),
    ("本周全国气候周 · 详见第 2 版", "TODA LA SEMANA · MÁS EN LA PÁGINA 2", 1),
    ("HET NIEUWS · 头条", "HET NIEUWS · TITULARES", 1),
    ("讲解｜de Klimaatweek 气候周 · de boom planten 种树 · besparen 节约 · de waarschuwing 警告、预警。", "de Klimaatweek: la Semana del Clima · de boom planten: plantar un árbol · besparen: ahorrar · de waarschuwing: la advertencia, la alerta.", 1),
    ("DE WEEK IN CIJFERS · 数字看本周", "DE WEEK IN CIJFERS · EN CIFRAS", 1),
    ("7 — de dagen van de Klimaatweek（气候周的天数）", "7 — de dagen van de Klimaatweek (los días de la Semana del Clima)", 1),
    ("200 — de bomen en struiken die Coevorden zaterdag uitdeelt（周六科弗登发放的树木和灌木）", "200 — de bomen en struiken die Coevorden zaterdag uitdeelt (los árboles y arbustos que Coevorden reparte el sábado)", 1),
    ("70+ — de musea die open zijn op Museumnacht（博物馆之夜开放的博物馆，70 多家）", "70+ — de musea die open zijn op Museumnacht (los museos abiertos en la Museumnacht, más de 70)", 1),
    ("9 — de wedstrijden van speelronde 12 in de Eredivisie（荷甲第 12 轮的比赛场数）", "9 — de wedstrijden van speelronde 12 in de Eredivisie (los partidos de la jornada 12 de la Eredivisie)", 1),
    ("NU JIJ · 即学即练", "NU JIJ · AHORA TÚ", 1),
    ("气候周 11 月 2–8 日", "La Semana del Clima es del 2 al 8 de noviembre", 1),
    ("海伦芬–费耶诺德 11:15 开球", "El Heerenveen – Feyenoord empieza a las 11:15", 1),
    ("veel mensen → planten", "Sujeto plural → planten", 1),
    ("· 本周日程", "· ESTA SEMANA", 1),
    ("Agenda van de week · 本周大事", "Agenda van de week · Agenda de la semana", 1),
    ("本周日程见第 2–4 版文章", "Ver la agenda en las páginas 2–4.", 1),
    ("IN DEZE EDITIE · 本期目录", "IN DEZE EDITIE · CONTENIDO", 1),
    ("“气候”：我们周围长期的天气与自然。气候周讲的就是我们的气候。", "«El clima»: el tiempo y la naturaleza que nos rodean, a largo plazo. La Semana del Clima trata de nuestro clima.", 1),
    ("IN HET KORT · 快讯", "IN HET KORT · EN BREVE", 1),
    ("BLIKSEMQUIZ · 闪电问答", "BLIKSEMQUIZ · QUIZ RELÁMPAGO", 1),
    ("读头版，选出正确答案 · 答案见第 8 版", "Lee la portada y elige la respuesta correcta · Respuestas en la página 8", 1),
    ("气候周共 7 天（11 月 2–8 日）", "La Semana del Clima dura 7 días (2–8 de noviembre)", 1),
    ("博物馆之夜在阿姆斯特丹", "La Museumnacht es en Ámsterdam", 1),
    ("LEVEN · 生活", "LEVEN · VIDA", 1),
    ("NIVEAU A2 · De Klimaatweek, stap voor stap · 一步一步讲气候周", "NIVEAU A2 · De Klimaatweek, stap voor stap · La Semana del Clima, paso a paso", 1),
    ("ZO ONTHOUD JE HET · 口诀", "ZO ONTHOUD JE HET · EL TRUCO", 1),
    ("het klimaat 气候 · wortelen 生根 · besparen 节约 · de verwarming 暖气 · de waarschuwing 预警 · lokaal 当地的、本地的。", "het klimaat: el clima · wortelen: echar raíces · besparen: ahorrar · de verwarming: la calefacción · de waarschuwing: la advertencia · lokaal: local.", 1),
    ("EN JIJ? · 说说你自己", "EN JIJ? · ¿Y TÚ?", 1),
    ("气候周你做什么？种树、节约能源还是骑车。写两句荷兰语寄给编辑部。", "¿Qué haces tú en la Semana del Clima: plantar un árbol, ahorrar energía o ir en bici? Escribe dos frases en neerlandés y envíalas a la redacción.", 2),
    ("DE CODES VAN HET KNMI · 气象预警颜色", "DE CODES VAN HET KNMI · LOS CÓDIGOS DEL KNMI", 1),
    ("Wat betekent elke kleur? · 每种颜色是什么意思", "Wat betekent elke kleur? · ¿Qué significa cada color?", 1),
    ("天气可能危险，要当心", "El tiempo puede ser peligroso: ¡atención!", 1),
    ("危险，做好准备", "Peligroso: prepárate", 1),
    ("非常危险，尽量待在室内", "Muy peligroso: mejor quedarse dentro", 1),
    ("预警针对你所在的地区", "La alerta vale para tu zona", 1),
    ("OEFENINGEN · 第 2 版练习", "OEFENINGEN · EJERCICIOS", 1),
    ("读第 2 版文章，选出正确答案。", "Lee el artículo de la página 2 y elige la respuesta correcta.", 1),
    ("用第 2 版的词填空。", "Completa con las palabras de la página 2.", 1),
    ("用颜色代码和日期填空。", "Completa con los códigos de color y las fechas.", 1),
    ("气候周不做：更多开车", "En la Semana del Clima NO se hace: conducir más", 1),
    ("红色预警：非常危险，待在室内", "Código rojo: muy peligroso, quedarse dentro", 1),
    ("预警针对本地，不针对整个省", "Las alertas son locales, no para toda la provincia", 1),
    ("节约能源：暖气调低一度", "Ahorrar energía: bajar la calefacción un grado", 1),
    ("气候周 11 月 2–8 日共 7 天", "La Semana del Clima dura 7 días, del 2 al 8 de noviembre", 1),
    ("wortelen = 生根（复数主语）", "wortelen = echar raíces (sujeto plural)", 1),
    ("besparen = 节约", "besparen = ahorrar", 1),
    ("fiets = 自行车", "fiets = la bicicleta", 1),
    ("黄色代码：当心", "Código amarillo: atención", 1),
    ("橙色代码：危险", "Código naranja: peligroso", 1),
    ("发放从 13:00 开始", "El reparto empieza a las 13:00", 1),
    ("气候周 11 月 8 日周日结束", "La Semana del Clima termina el domingo 8 de noviembre", 1),
    ("Klimaatweek=气候周 b", "Klimaatweek=la Semana del Clima b", 1),
    ("besparen=节约 d", "besparen=ahorrar d", 1),
    ("waarschuwing=预警 a", "waarschuwing=la advertencia a", 1),
    ("lokaal=本地的 c", "lokaal=local c", 1),
])
with open(C12, encoding="utf-8") as fh:
    txt = fh.read()
anchor = 'p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)'
assert anchor in txt and "TEXTOS EN NEERLANDÉS" not in txt
txt = txt.replace(anchor, anchor + '\np.text(975, 568, "TEXTOS EN NEERLANDÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 20, "sans", True, BRICK, anchor="middle")')
with open(C12, "w", encoding="utf-8") as fh:
    fh.write(txt)
print("P1 badge inserted at y=568")

C34 = os.path.join(HERE, "content34.py")
apply_map(C34, [
    ("CULTUUR · 文化", "CULTUUR · CULTURA", 1),
    ("NIVEAU A2 → B1 · Museumnacht, boeken en kunst · 博物馆之夜、书籍与艺术", "NIVEAU A2 → B1 · Museumnacht, boeken en kunst · Museumnacht, libros y arte", 1),
    ("het museum 博物馆 · de rondleiding 导览 · het tijdslot 时间段 · tweedehands 二手的 · de beurs 展会、集市。", "het museum: el museo · de rondleiding: la visita guiada · het tijdslot: el turno, la franja horaria · tweedehands: de segunda mano · de beurs: la feria.", 1),
    ("OEFENINGEN · 第 3 版练习", "OEFENINGEN · EJERCICIOS", 1),
    ("读第 3 版文章，选出正确答案。", "Lee el artículo de la página 3 y elige la respuesta correcta.", 1),
    ("用方框里的词填空。注意：有的词要变成复数。", "Completa con las palabras del recuadro. Atención: algunas van en plural.", 1),
    ("用现在完成时补全，注意助动词 hebben/zijn。", "Completa en perfecto, con los auxiliares hebben/zijn.", 1),
    ("算一算：用第 3 版的数字回答。", "Calcula: responde con los números de la página 3.", 1),
    ("博物馆开放到凌晨 2 点", "Los museos abren hasta las 02:00", 1),
    ("Crossing Border 结合书籍与音乐", "Crossing Border combina libros y música", 1),
    ("PAN 艺术博览会到 11 月 8 日", "PAN Amsterdam dura hasta el 8 de noviembre", 1),
    ("museum 复数：musea", "museum en plural: musea", 1),
    ("rondleiding = 导览", "rondleiding = la visita guiada", 1),
    ("tijdslot = 时间段", "tijdslot = el turno", 1),
    ("tweedehands = 二手的", "tweedehands = de segunda mano", 1),
    ("beurs = 展会、集市", "beurs = la feria", 1),
    ("zijn 的 perfectum：zijn geweest", "Perfecto de zijn: zijn geweest", 1),
    ("kopen 的 perfectum：hebben gekocht", "Perfecto de kopen: hebben gekocht", 1),
    ("voorlezen 的 perfectum：hebben voorgelezen", "Perfecto de voorlezen: hebben voorgelezen", 1),
    ("komen 用 zijn：zijn gekomen", "komen va con zijn: zijn gekomen", 1),
    ("19:00 到 02:00 共 7 小时", "De 19:00 a 02:00 son 7 horas", 1),
    ("11 月 1–8 日共 8 天", "Del 1 al 8 de noviembre son 8 días", 1),
    ("11 月 3–8 日共 6 天", "Del 3 al 8 de noviembre son 6 días", 1),
    ("250 的一半是 125", "La mitad de 250 es 125", 1),
    ("SPORT · 体育", "SPORT · DEPORTE", 1),
    ("NIVEAU B1 · Europese week en speelronde 12 · 欧战周与第 12 轮", "NIVEAU B1 · Europese week en speelronde 12 · Semana europea y jornada 12", 1),
    ("de balans 成绩单、总结 · gelijkspelen 打平 · de speelronde 轮次 · de topper 焦点战 · de stand 积分榜。", "de balans: el balance · gelijkspelen: empatar · de speelronde: la jornada · de topper: el partidazo · de stand: la clasificación.", 1),
    ("OEFENINGEN · 第 4 版练习", "OEFENINGEN · EJERCICIOS", 1),
    ("读第 4 版文章，选出正确答案。", "Lee el artículo de la página 4 y elige la respuesta correcta.", 1),
    ("用方框里的词填空。注意动词形式。", "Completa con las palabras del recuadro. Atención a la forma del verbo.", 1),
    ("用过去时或完成时补全。", "Completa en pasado o en perfecto.", 1),
    ("特温特 4–1 赢林肯红魔", "El Twente ganó 4–1 al Lincoln", 1),
    ("NEC 2–4 输给萨格勒布迪纳摩", "El NEC perdió 2–4 ante el Dinamo de Zagreb", 1),
    ("10 轮后费耶诺德 24 分领跑", "Tras 10 jornadas, el Feyenoord lidera con 24 puntos", 1),
    ("balans = 成绩单、总结", "balans = el balance", 1),
    ("gelijkspelen 过去时复数：speelden gelijk", "Pasado plural de gelijkspelen: speelden gelijk", 1),
    ("topper = 焦点战", "topper = el partidazo", 1),
    ("stand = 积分榜", "stand = la clasificación", 1),
    ("doelpunt = 进球", "doelpunt = el gol", 1),
    ("winnen 过去时：won", "Pasado de winnen: won", 1),
    ("gaan 过去时：ging", "Pasado de gaan: ging", 1),
    ("verliezen 过去时：verloor", "Pasado de verliezen: verloor", 1),
    ("komen 的 perfectum 用 zijn", "Perfecto de komen, con zijn", 1),
    ("对：阿贾克斯 2–0 获胜", "Verdadero: el Ajax ganó 2–0", 1),
    ("错：NEC 2–4 输了", "Falso: el NEC perdió 2–4", 1),
    ("错：特温特–阿贾克斯 13:30；11:15 是海伦芬–费耶诺德", "Falso: el Twente – Ajax es a las 13:30; a las 11:15 es el Heerenveen – Feyenoord", 1),
    ("对：10 轮后费耶诺德 24 分第一", "Verdadero: tras 10 jornadas el Feyenoord lidera con 24 puntos", 1),
])

C56 = os.path.join(HERE, "content56.py")
apply_map(C56, [
    ("JONGEREN · 青年", "JONGEREN · JUVENTUD", 1),
    ("NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · 荒岛节目开播、音乐节与设计周落幕", "NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · Robinson ha empezado; ADE y DDW han terminado", 1),
    ("1. Kijk zondag om 20:00 uur op RTL 4（周日晚 20:00 在 RTL 4 收看）", "1. Kijk zondag om 20:00 uur op RTL 4 (el domingo a las 20:00 en RTL 4)", 1),
    ("2. Let op de proeven: daar worden de punten verdeeld（注意比赛项目：分数在那里决出）", "2. Let op de proeven: daar worden de punten verdeeld (atención a las pruebas: allí se reparten los puntos)", 1),
    ("3. Raad met vrienden wie het langst blijft（和朋友猜谁能留到最后）", "3. Raad met vrienden wie het langst blijft (adivina con tus amigos quién aguantará más)", 1),
    ("4. Volgende week lees je hier hoe het verder ging（下周这里继续报道进展）", "4. Volgende week lees je hier hoe het verder ging (la semana que viene leerás aquí cómo sigue)", 1),
    ("het eiland 岛 · de proef 比赛项目、考验 · stemmen 投票 · de aflevering （一）集 · voorbij 过去了、结束了。", "het eiland: la isla · de proef: la prueba · stemmen: votar · de aflevering: el episodio · voorbij: pasado, terminado.", 1),
    ("EN JIJ? · 说说你自己", "EN JIJ? · ¿Y TÚ?", 1),
    ("你看《荒岛远征》吗，还是更爱自己出门活动？写两句荷兰语寄来。", "¿Ves Expeditie Robinson o prefieres hacer algo fuera? Escribe dos frases en neerlandés y envíalas.", 2),
    ("OEFENINGEN · 第 5 版练习", "OEFENINGEN · EJERCICIOS", 1),
    ("读第 5 版文章，选出正确答案。", "Lee el artículo de la página 5 y elige la respuesta correcta.", 1),
    ("用 gaan + 不定式说将来。", "Habla del futuro con gaan + infinitivo.", 1),
    ("Robinson 在 11 月 1 日周日开始", "Robinson empezó el domingo 1 de noviembre", 1),
    ("19 位参赛者", "19 concursantes", 1),
    ("ADE 今年 30 年", "ADE cumple 30 años este año", 1),
    ("设计周约 2.500 位设计师", "La Design Week mostró trabajo de unos 2.500 diseñadores", 1),
    ("ADE 与 DDW 在 10 月 25 日周日落幕", "ADE y la Design Week terminaron el domingo 25 de octubre", 1),
    ("eiland = 岛（het）", "eiland = la isla (het)", 1),
    ("proef = 比赛项目、考验（de）", "proef = la prueba (de)", 1),
    ("stemmen = 投票", "stemmen = votar", 1),
    ("aflevering = （一）集", "aflevering = el episodio", 1),
    ("voorbij = 过去了、结束了", "voorbij = pasado, terminado", 1),
    ("kandidaat 复数：kandidaten", "Plural de kandidaat: kandidaten", 1),
    ("gaat winnen = 会赢（只是猜测）", "gaat winnen = va a ganar (solo una suposición)", 1),
    ("wij → gaan + 不定式 kijken", "wij → gaan + infinitivo kijken", 1),
    ("hij → gaat praten", "hij → gaat praten", 1),
    ("zij (复数) → gaan zoeken", "zij (plural) → gaan zoeken", 1),
    ("对：11 月 1 日开始", "Verdadero: empezó el 1 de noviembre", 1),
    ("错：ADE 今年 30 年", "Falso: ADE cumple 30 años", 1),
    ("错：10 月 25 日已落幕", "Falso: ya terminó el 25 de octubre", 1),
    ("VERDIEPING · 深读", "VERDIEPING · EN PROFUNDIDAD", 1),
    ("NIVEAU B2 · De codes van het KNMI · 气象预警深度解读", "NIVEAU B2 · De codes van het KNMI · Los códigos del KNMI", 1),
    ("DE GRAFIEK · 图表（练习数据）", "DE GRAFIEK · EL GRÁFICO (DATOS DE PRÁCTICA)", 1),
    ("练习数据：虚构数字，仅供练习，非真实调查。问题：橙色预警时你会怎么做？（100 名年轻人）", "Datos de práctica: cifras inventadas, solo para practicar, no una encuesta real. Pregunta: ¿qué haces tú con el código naranja? (100 jóvenes)", 1),
    ("VOOR OF TEGEN? · 正方还是反方", "VOOR OF TEGEN? · ¿A FAVOR O EN CONTRA?", 1),
    ("de meteoroloog 气象学家 · waarschuwingsmoeheid 预警疲劳 · vastzetten 固定好 · het advies 建议、忠告 · de voorstander 支持者。", "de meteoroloog: el meteorólogo · waarschuwingsmoeheid: el cansancio ante las alertas · vastzetten: fijar, asegurar · het advies: el consejo · de voorstander: el partidario.", 1),
    ("OEFENINGEN · 第 6 版练习", "OEFENINGEN · EJERCICIOS", 1),
    ("看第 6 版图表（练习数据）回答。", "Mira el gráfico de la página 6 (datos de práctica) y responde.", 1),
    ("读第 6 版文章，选出正确答案。", "Lee el artículo de la página 6 y elige la respuesta correcta.", 1),
    ("把词组成正确的句子。", "Forma frases correctas con las palabras.", 1),
    ("45 名年轻人选择待在家里", "45 jóvenes eligen quedarse en casa", 1),
    ("25 人先看预警文字", "25 miran primero el texto de la alerta", 1),
    ("10 人不知道", "10 no lo saben", 1),
    ("图表共 100 人：45+25+20+10", "El gráfico suma 100 jóvenes: 45+25+20+10", 1),
    ("以前预警针对整个省", "Antes las alertas valían para toda una provincia", 1),
    ("如今预警是本地的", "Hoy las alertas son locales", 1),
    ("红色：非常危险，非必要不上路", "Rojo: muy peligroso, no salgas a la carretera si no es necesario", 1),
    ("KNMI 说：看代码旁边的文字", "El KNMI dice: mira el texto junto al código", 1),
    ("lokaal = 本地的", "lokaal = local", 1),
    ("waarschuwingsmoeheid = 预警疲劳", "waarschuwingsmoeheid = el cansancio ante las alertas", 1),
    ("vastzetten = 固定好", "vastzetten = fijar, asegurar", 1),
    ("advies = 建议（het）", "advies = el consejo (het)", 1),
    ("主语 + 动词 + 地点", "Sujeto + verbo + lugar", 1),
    ("祈使句：动词在首位", "Imperativo: el verbo va primero", 1),
    ("weinig voor = 很少出现", "weinig voor = aparece poco", 1),
    ("raakt + 宾语 + 方式", "raakt + objeto + manera", 1),
])

C7 = os.path.join(HERE, "content7.py")
apply_map(C7, [
    ("TAAL · 语言", "TAAL · LENGUA", 1),
    ("聚焦语言 · Drie niveaus, drie gereedschappen · 三个级别，三件工具", "La lengua, en primer plano · Drie niveaus, drie gereedschappen · Tres niveles, tres herramientas", 1),
    ("het klimaat 气候（长期）；een boom planten 种树；besparen 节约；de waarschuwing 预警。", "het klimaat: el clima (a largo plazo); een boom planten: plantar un árbol; besparen: ahorrar; de waarschuwing: la advertencia.", 1),
    ("气候是长期的天气与自然", "El clima es el tiempo y la naturaleza a largo plazo", 1),
    ("meedoen 参加：ik doe mee；opruimen 收拾：wij hebben opgeruimd；vastzetten 固定：zij zette vast。", "meedoen: participar — ik doe mee; opruimen: recoger — wij hebben opgeruimd; vastzetten: fijar — zij zette vast.", 1),
    ("opruimen 的分词：opgeruimd", "Participio de opruimen: opgeruimd", 1),
    ("vastzetten 过去时：zette vast", "Pasado de vastzetten: zette vast", 1),
    ("meedoen = 参加、参与", "meedoen = participar", 1),
    ("Ik vind dat… 我认为；Volgens mij… 依我看；Het lijkt me dat… 在我看来。", "Ik vind dat…: yo creo que; Volgens mij…: en mi opinión; Het lijkt me dat…: me parece que.", 1),
    ("Volgens mij… = 依我看", "Volgens mij… = en mi opinión", 2),
    ("Ik vind dat… 表达看法", "Ik vind dat… expresa una opinión", 1),
    ("Het lijkt me dat… = 在我看来", "Het lijkt me dat… = me parece que", 1),
    ("PAS OP! · 易错诊所", "PAS OP! · ERRORES FRECUENTES", 1),
    ("气候是长期的天气自然，不是今天的天气。", "El clima es el tiempo y la naturaleza a largo plazo, no el tiempo de hoy.", 1),
    ("Klimaatweek 是专名，首字母大写。", "Klimaatweek es un nombre propio: va con mayúscula.", 1),
    ("een 是单数：een boom；复数直接用 bomen。", "een es singular: een boom; en plural, simplemente bomen.", 1),
    ("omdat 从句后，主句动词在第二位：blijf ik thuis。", "Tras la subordinada con omdat, el verbo de la principal va en segundo lugar: blijf ik thuis.", 1),
    ("HET WOORD · 本周生词", "HET WOORD · PALABRA SEMANAL", 1),
    ("meedoen = 参加、参与：气候周全荷兰都参加。", "meedoen = participar: en la Semana del Clima participa todo el país.", 2),
    ("«Hallo! Ik ben Li en ik leer Nederlands in Shanghai. In de Klimaatweek plant ik een boom op mijn balkon!» — Li (voorbeeldbrief van de redactie)", "«Hallo! Ik ben Lucía en ik leer Nederlands in Madrid. In de Klimaatweek plant ik een boom op mijn balkon!» — Lucía (voorbeeldbrief van de redactie)", 1),
    ("截稿时未收到真实来信或第 8 版最佳作文，刊登示例信，承诺顺延 VOL.3。", "Al cierre no habían llegado cartas reales ni los mejores textos de la página 8: por eso publicamos este ejemplo, con la promesa de publicarlos en el VOL.3.", 1),
    ("编辑部示例信，非真实来信。欢迎寄来你的真实来信和第 8 版最佳作文，VOL.3 刊登！", "Ejemplo de la redacción, no es una carta real. ¡Envíanos tu carta real y tu mejor texto de la página 8: los publicaremos en el VOL.3!", 2),
    ("ZINNEN VAN DE WEEK · 本周金句（逐字摘自本期文章）", "ZINNEN VAN DE WEEK · FRASES DE LA SEMANA (PALABRA POR PALABRA, DE ESTA EDICIÓN)", 1),
    ("从 11 月 2 日周一到 8 日周日，荷兰是气候周。", "Del lunes 2 al domingo 8 de noviembre, en los Países Bajos es la Semana del Clima.", 1),
    ("秋天是种树的最好时节。", "El otoño es la mejor época para plantar.", 1),
    ("黄色意味着：当心，天气可能危险。", "El amarillo significa: atención, el tiempo puede ser peligroso.", 1),
    ("70 多家博物馆从晚上 19 点开放到凌晨 2 点。", "Más de 70 museos abren desde las 19:00 hasta las 02:00 de la madrugada.", 1),
    ("阿贾克斯 10 月 22 日周四 2–0 战胜亚特兰大。", "El Ajax ganó el jueves 22 de octubre 2–0 al Atalanta.", 1),
    ("11 月 1 日周日，《荒岛远征》在 RTL 4 开播，20 点。", "El domingo 1 de noviembre, Expeditie Robinson empezó en RTL 4, a las 20:00.", 1),
    ("预警代码不是禁令，而是一条建议。", "Un código no es una prohibición, sino un consejo.", 1),
    ("天气属于我们所有人，但对每个人的影响各不相同。", "El tiempo es de todos, pero nos afecta a todos de forma diferente.", 1),
    ("VOLGENDE WEEK · 下期预告 (VOL.3)", "VOLGENDE WEEK · LA SEMANA QUE VIENE (VOL.3)", 1),
])

C8 = os.path.join(HERE, "content8.py")
apply_map(C8, [
    ("TOETS EN ANTWOORDEN · 练习与答案", "TOETS EN ANTWOORDEN · PRUEBA Y RESPUESTAS", 1),
    ("第 8 版 · De grote toets van de week + alle antwoorden", "Página 8 · De grote toets van de week + alle antwoorden", 1),
    ("气候周到 11 月 8 日", "La Semana del Clima dura hasta el 8 de noviembre", 1),
    ("博物馆之夜在 11 月 7 日", "La Museumnacht es el 7 de noviembre", 1),
    ("Robinson 在 11 月开始", "Robinson empezó en noviembre", 1),
    ("橙色预警：天气危险", "Código naranja: el tiempo es peligroso", 1),
    ("meedoen = 参加", "meedoen = participar", 1),
    ("气候周 11 月 2 日周一开始", "La Semana del Clima empieza el lunes 2 de noviembre", 1),
    ("PAN 在 RAI 展览中心", "PAN Amsterdam está en la RAI", 1),
    ("10 轮后阿贾克斯 21 分", "Tras 10 jornadas, el Ajax tiene 21 puntos", 1),
    ("扎安丹旧货市场约 250 个摊位", "La Snuffelmarkt de Zaandam tiene unos 250 puestos", 1),
    ("Daan 住在科弗登", "Daan vive en Coevorden", 1),
    ("他周六领了一棵免费灌木", "El sábado recoge un arbusto gratis", 1),
    ("周日特温特对阿贾克斯", "El domingo el Twente juega contra el Ajax", 1),
    ("气候周他每天骑车上学", "En la Semana del Clima va cada día en bici al colegio", 1),
    ("主语 + 动词 + 时间", "Sujeto + verbo + tiempo", 1),
    ("主语 + 动词 + 宾语 + 地点", "Sujeto + verbo + objeto + lugar", 1),
    ("主语 + 动词 + 时间 + 对手", "Sujeto + verbo + tiempo + rival", 1),
    ("可分动词 mee 在句末", "El verbo separable mee va al final", 1),
    ("气候周持续七天。", "La Semana del Clima dura siete días.", 1),
    ("对照第 1 版头条", "Compara el titular de la página 1", 1),
    ("橙色预警意味着：做好准备。", "El código naranja significa: prepárate.", 1),
    ("第 2 版原句 · bereid je voor 做好准备", "Frase de la página 2 · bereid je voor = prepárate", 1),
    ("博物馆之夜从晚上 19 点到凌晨 2 点。→ ___", "La Museumnacht dura desde las 19:00 hasta las 02:00. → ___", 1),
    ("注意时间表达 van...tot...", "Atención a la expresión de tiempo van...tot...", 1),
    ("我参加气候周。→ ___", "Participo en la Semana del Clima. → ___", 1),
    ("meedoen 是可分动词", "meedoen es un verbo separable", 1),
    ("klimaat=气候 c", "klimaat=el clima c", 1),
    ("meedoen=参加 b", "meedoen=participar b", 1),
    ("waarschuwing=预警 a", "waarschuwing=la advertencia a", 1),
    ("vastzetten=固定好 d", "vastzetten=fijar d", 1),
    ("boom = 树", "boom = el árbol", 1),
    ("struik = 灌木", "struik = el arbusto", 1),
    ("planten = 种", "planten = plantar", 1),
    ("zachte = 柔软的（土壤）", "zachte = blanda (la tierra)", 1),
    ("发放到 16:00 结束", "El reparto dura hasta las 16:00", 1),
    ("写作题（无唯一答案）；范文（{NWORDS} 词）见下。", "Pregunta abierta (sin una única respuesta); el modelo ({NWORDS} palabras) está abajo.", 1),
    ("（开放题，范文如下）", "(Pregunta abierta — modelo a continuación)", 1),
    ("范文见本版 H 区（{NWORDS} 词）", "El modelo está en la sección H de esta página ({NWORDS} palabras)", 1),
    ("ANTWOORDEN · 参考答案 — 按版面分页排列，找到题号即可", "ANTWOORDEN · RESPUESTAS — ordenadas por página, busca tu número", 1),
    ("每题附一句中文简析 · 带 ✓ 的为范文题", "Una explicación breve por número · ✓ = modelo de redacción", 1),
])
with open(C8, encoding="utf-8") as fh:
    txt = fh.read()
for old, new in [("完形单选", "Huecos"), ("单选", "Elección"), ("造句", "Frases"),
                 ("翻译", "Traducción"), ("词汇配对", "Relacionar"), ("写作", "Redacción")]:
    n = txt.count('"%s"' % old)
    assert n >= 1, ("content8 type missing", old)
    txt = txt.replace('"%s"' % old, '"%s"' % new)
    print("content8 type", old, "->", new, "x", n)
with open(C8, "w", encoding="utf-8") as fh:
    fh.write(txt)
with open(C8, encoding="utf-8") as fh:
    txt = fh.read()
assert 'af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)' in txt
txt = txt.replace('af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)',
                  'af.para(txt, 13.0, lh=1.12, gap=0.4, split=False)')
with open(C8, "w", encoding="utf-8") as fh:
    fh.write(txt)
print("P8 answer flow set to 13.0/1.12/0.4 (W43 ES precedent)")

B = os.path.join(HERE, "bslib4.py")
apply_map(B, [
    ("De Lucerna · 荷兰语周报 VOL.2 · LUCERNA DUTCH WEEKLY", "De Lucerna · SEMANARIO NEERLANDÉS VOL.2 · TEXTO EN NEERLANDÉS · EXPLICACIONES EN ESPAÑOL", 1),
    ("第 {n} 版 / 共 {total} 版", "Página {n} de {total}", 1),
    ("译注｜", "Nota — ", 1),
])
print("TRANSFORM DONE")
