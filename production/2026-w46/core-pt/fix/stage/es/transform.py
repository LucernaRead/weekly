# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x ES fan-out transform for W46 VOL.3.

Run inside the already-copied build dir. Every replacement is an exact
literal match (longest strings first); missing literals warn, and the
final pass asserts ZERO CJK chars remain in the build sources.
Frozen Portuguese text, the P7 example letter (lt), the PT disclosure
(disc_pt) and the P7 quote strings + page tags are never touched.
P1 subtitle (330) and badge (372) lines are replaced whole (size/color).
Subtitle size 33pt is measured (38pt overflows the page frame).
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
CJK = re.compile(r'[\u4e00-\u9fff]')

def load(fn):
    with open(os.path.join(HERE, fn), encoding='utf-8') as f:
        return f.read()

def save(fn, txt):
    with open(os.path.join(HERE, fn), 'w', encoding='utf-8') as f:
        f.write(txt)

def sub(txt, old, new, fn=''):
    n = txt.count(old)
    assert n >= 1, f'{fn}: {old!r} not found'
    return txt.replace(old, new)

def line_replace(txt, anchor, newline, fn=''):
    lines = txt.split('\n')
    hits = [i for i, ln in enumerate(lines) if anchor in ln]
    assert len(hits) == 1, f'{fn}: anchor {anchor!r} hits {hits}'
    lines[hits[0]] = newline
    return '\n'.join(lines)

FILES = ['bslib4.py', 'content12.py', 'content34.py', 'content56.py',
         'content7.py', 'content8.py', 'render.py']

# ---------- 0. OUT / BASE repoint + print PDF name ----------
for fn in FILES:
    t = load(fn)
    if 'weekly-report-w46-pt-core' in t:
        t = t.replace('weekly-report-w46-pt-core', 'weekly-report-w46-pt-es')
        save(fn, t)
t = load('render.py')
t = sub(t, 'A-Lucerna-VOL3.pdf', 'Lucerna-VOL3-ES.pdf', 'render.py')
save('render.py', t)

# ---------- 1. bslib4 furniture ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.3 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · SEMANARIO PORTUGUÉS VOL.3 · TEXTO EN PORTUGUÉS · EXPLICACIONES EN ESPAÑOL', 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"', 'bslib4.py')
t = sub(t, '("译注｜" + s', '("Nota — " + s', 'bslib4.py')
save('bslib4.py', t)

# ---------- 2. P1 masthead lines (whole-line) ----------
t = load('content12.py')
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "SEMANARIO EN PORTUGUÉS · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE", 33, "serif", True, INK, anchor="middle")',
    'content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "TEXTOS EN PORTUGUÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 19, "sans", True, BRICK, anchor="middle")',
    'content12.py')
save('content12.py', t)

# ---------- 3. type / instr labels ----------
INSTR = [
    ('instr="造句"', 'instr="Forma una frase"'),
    ('instr="翻译"', 'instr="Traduce"'),
    ('instr="判断"', 'instr="¿Verdadero o falso?"'),
    ('instr="写作"', 'instr="Escribe"'),
    ('instr="填空"', 'instr="Completa"'),
    ('instr="把词和释义配对"', 'instr="Empareja"'),
]
TYP = [
    ('"完成句子"', '"Completar la frase"'),
    ('"词汇配对"', '"Emparejar vocabulario"'),
    ('"判断对错"', '"Verdadero o falso"'),
    ('"完形单选"', '"Texto con huecos"'),
    ('"单选"', '"Opción múltiple"'),
    ('"造句"', '"Formar frases"'),
    ('"翻译"', '"Traducción"'),
    ('"写作"', '"Escritura"'),
]
for fn in ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    for old, new in INSTR:
        if old in t:
            t = sub(t, old, new, fn=fn)
    for old, new in TYP:
        if old in t:
            t = sub(t, old, new, fn=fn)
    save(fn, t)

# ---------- 4. content replacements (global table, longest-first) ----------
REPL = [
    # bands
    ('NÍVEL A2 · Prova e feriado no mesmo domingo', 'NIVEL A2 · Examen y festivo el mismo domingo'),
    ('A2 → B1 · Proclamação da República: 137 anos · 共和国宣言 137 周年', 'A2 → B1 · Proclamação da República: 137 años'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'NIVEL B1 · La semana del fútbol'),
    ('NÍVEL B1 · A última semana dos jovens · 最后一周：年轻人的冲刺', 'NIVEL B1 · La última semana de los jóvenes'),
    ('NÍVEL B2 · O segundo domingo explicado · 第二个周日详解', 'NIVEL B2 · El segundo domingo, explicado'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具', 'Três níveis, três ferramentas · Tres niveles, tres herramientas'),
    ('第 8 版 · A grande prova da semana + todas as respostas', 'PÁGINA 8 · La gran prueba de la semana + todas las respuestas'),
    # top strip / kickers
    ('TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语', 'TODA SEMANA EM PORTUGUÊS · EL PORTUGUÉS QUE LEE BRASIL, CADA SEMANA'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · TITULAR'),
    ('VIDA · 生活', 'VIDA · LA VIDA'),
    ('CULTURA · 文化', 'CULTURA · CULTURA'),
    ('ESPORTE · 体育', 'ESPORTE · DEPORTE'),
    ('JOVENS · 青年', 'JOVENS · LOS JÓVENES'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · EN PROFUNDIDAD'),
    ('LÍNGUA · 语言', 'LÍNGUA · LENGUA'),
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · PRUEBA Y RESPUESTAS'),
    # P1
    ('高考第二天', 'ENEM, DÍA 2'),
    ('11 月 15 日第二场考试 · 共和国宣言日假期', '15 de nov.: segundo día de examen · festivo de la Proclamación de la República'),
    ('讲解｜a proclamação 宣布、宣告 · o feriado 假日 · a natureza 自然科学 · a matemática 数学。', 'Palabras clave | a proclamação = proclamación · o feriado = festivo · a natureza = ciencias de la naturaleza · a matemática = matemáticas.'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · EN CIFRAS'),
    ('12h — os portões abrem no domingo 15（周日 12 点开门）', '12h — os portões abrem no domingo 15 (domingo: apertura a las 12h)'),
    ('13h — os portões fecham（13 点关门，过时不入）', '13h — os portões fecham (13h: cierre, quien llega tarde no entra)'),
    ('13h30–18h30 — a prova do dia 15（考试 13:30 至 18:30）', '13h30–18h30 — a prova do dia 15 (la prueba del 15, de 13:30 a 18:30)'),
    ('90 — as questões do dia 15: 45 + 45（90 道题：45 + 45）', '90 — as questões do dia 15: 45 + 45 (90 preguntas: 45 + 45)'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · AHORA TÚ'),
    ('proclamação = 宣布（共和国宣言）', 'proclamação = proclamación (de la República)'),
    ('proclamação = 宣布（共和国宣言）。', 'proclamação = proclamación (de la República).'),
    ('feriado = 假日', 'feriado = festivo'),
    ('portões = 大门（考场大门）', 'portões = las puertas (del centro de examen)'),
    ('18h30 结束', 'termina a las 18h30'),
    ('90 道题', '90 preguntas'),
    ('fazer 现在时 eles 形式：fazem', 'fazer, presente, forma eles: fazem'),
    ('迟到不得入内：13 点后关门', 'Después de las 13h ya no se entra.'),
    # .text.md variant of the line above: the export source carries a trailing 。 which the bare entry leaves behind (F-2).
    ('迟到不得入内：13 点后关门。', 'Después de las 13h ya no se entra.'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · EN ESTA EDICIÓN'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · BREVE'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · QUIZ RELÁMPAGO'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Lee la portada y elige · Respuestas en la página 8'),
    ('共和国宣言日在 11 月 15 日', 'La Proclamación de la República es el 15 de noviembre'),
    ('13 点关门', 'Cierre a las 13h'),
    ('第 2 天考自然科学与数学', 'Día 2: ciencias de la naturaleza y matemáticas'),
    ('18:30 结束', 'Termina a las 18:30'),
    # P2
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · EL TRUCO'),
    ('a proclamação 宣布 · o feriado 假日 · a natureza 自然科学 · a matemática 数学 · conferir 核对 · a escala 排班。', 'a proclamação = proclamación · o feriado = festivo · a natureza = ciencias de la naturaleza · a matemática = matemáticas · conferir = comprobar · a escala = el turno.'),
    ('在你的国家，落在周日的假日会在周一补休吗？写两句寄来。', 'En tu país, ¿un festivo que cae en domingo se recupera el lunes? Escribe dos frases y envíanoslas.'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · ¿Y TÚ?'),
    ('OS HORÁRIOS DO DOMINGO 15 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 15 · HORARIOS DEL DOMINGO 15'),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · Un país, varios relojes'),
    ('周日 12 点开门', 'Apertura el domingo a las 12h'),
    ('13:30 开考', 'La prueba empieza a las 13:30'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · EJERCICIOS PÁGINA 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Respuestas en la página 8 · Niveles mezclados: busca por número'),
    ('读第 2 版文章，选出正确答案。', 'Lee la página 2 y elige la respuesta correcta.'),
    ('假日落在周日，周一不补休', 'El festivo cae en domingo, el lunes no se recupera'),
    # P7-clinic/.text.md variant of the line above: the source carries a trailing 。 (F-2/F-3).
    ('假日落在周日，周一不补休。', 'El festivo cae en domingo, el lunes no se recupera.'),
    ('确认卡显示考试地点', 'La tarjeta de confirmación muestra el lugar del examen'),
    ('巴西没有夏令时，钟表不动', 'Brasil no tiene horario de verano: los relojes no se mueven'),
    ('补全动词的现在时形式。', 'Completa con la forma en presente del verbo.'),
    ('用第 1、2 版的数字填空。', 'Completa con los números de las páginas 1 y 2.'),
    ('12 点到 13 点 = 1 小时', 'De 12h a 13h = 1 hora'),
    ('13:30 至 18:30 = 5 小时', 'De 13:30 a 18:30 = 5 horas'),
    ('5×60 = 300 分钟', '5×60 = 300 minutos'),
    ('proclamação=宣布一个变化 b', 'proclamação = anunciar un cambio (b)'),
    ('feriado=法律规定的休息日 c', 'feriado = un día de descanso fijado por ley (c)'),
    ('natureza=生命、物理与化学的科学 d', 'natureza = la ciencia de la vida, la física y la química (d)'),
    ('matemática=数字与图形的科学 a', 'matemática = la ciencia de los números y las figuras (a)'),
    ('把词和释义配对', 'Empareja las palabras y las definiciones'),
]
REPL += [
    # P3
    ('a monarquia 君主制 · a república 共和国 · o marechal 元帅 · o exílio 流亡 · o governo 政府 · a lei 法律。', 'a monarquia = monarquía · a república = república · o marechal = mariscal · o exílio = exilio · o governo = gobierno · a lei = ley.'),
    ('在你的国家，有纪念共和国建立的假日吗？写两句寄来。', 'En tu país, ¿hay un festivo que conmemore la fundación de la república? Escribe dos frases y envíanoslas.'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · EJERCICIOS PÁGINA 3'),
    ('读第 3 版文章，选出正确答案。', 'Lee la página 3 y elige la respuesta correcta.'),
    ('共和国宣言在 1889 年 11 月 15 日', 'La Proclamación de la República fue el 15 de noviembre de 1889'),
    ('德奥多罗成为巴西第一任总统', 'Deodoro se convirtió en el primer presidente de Brasil'),
    ('全国性假日，任何城市都不能改为工作日', 'Un festivo nacional que ninguna ciudad puede convertir en día laborable'),
    ('2026 年假日落在周日', 'En 2026 el festivo cae en domingo'),
    ('共和国里总统由选举产生、任期有限', 'En la república, el presidente se elige y el poder tiene límite de tiempo'),
    ('用方框里的词填空。', 'Completa con las palabras del recuadro.'),
    ('monarquia = 君主制', 'monarquia = monarquía'),
    ('república = 共和国', 'república = república'),
    ('marechal = 元帅', 'marechal = mariscal'),
    ('exílio = 流亡', 'exílio = exilio'),
    ('governo = 政府', 'governo = gobierno'),
    ('lei = 法律', 'lei = ley'),
    ('用过去时（pretérito perfeito）补全。', 'Completa en pasado (pretérito perfeito).'),
    ('tomar 过去时 elas 形式：tomaram', 'tomar, pasado, forma elas: tomaram'),
    ('acabar 过去时 ela 形式：acabou', 'acabar, pasado, forma ela: acabou'),
    ('ser 过去时 ele 形式：foi', 'ser, pasado, forma ele: foi'),
    ('assumir 过去时 ele 形式：assumiu', 'assumir, pasado, forma ele: assumiu'),
    ('把词组成正确的句子。', 'Pon las palabras en el orden correcto.'),
    ('主语 + é + 表语', 'Sujeto + é + atributo'),
    ('主语 + 动词 + 表语', 'Sujeto + verbo + atributo'),
    ('主语 + 动词 + 宾语 + 时间', 'Sujeto + verbo + objeto + tiempo'),
    # P4
    ('a ida 首回合 · a volta 次回合 · o gol 进球 · o pênalti 点球 · a pausa 休整期 · o amistoso 友谊赛。', 'a ida = el partido de ida · a volta = el partido de vuelta · o gol = el gol · o pênalti = el penalti · a pausa = la pausa · o amistoso = el amistoso.'),
    ('你在巴西杯支持哪支球队？谁能进决赛？写两句寄来。', '¿A qué equipo apoyas en la Copa do Brasil, y quién llegará a la final? Escribe dos frases y envíanoslas.'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · LA SEMANA DEL FÚTBOL'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · EJERCICIOS PÁGINA 4'),
    ('读第 4 版文章，选出正确答案。', 'Lee la página 4 y elige la respuesta correcta.'),
    ('首回合格雷米奥 2 比 0 战胜米内罗竞技', 'En la ida, Grêmio ganó 2 a 0 al Atlético-MG'),
    ('帕尔梅拉斯 1 比 0 战胜瓦斯科，毛里西奥进球', 'Palmeiras ganó 1 a 0 a Vasco, gol de Maurício'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点', 'La vuelta Atlético-MG × Grêmio es el sábado 7 a las 18h'),
    ('决赛 12 月 6 日单场，在马内·加林查', 'La final: un solo partido, el 6 de diciembre, en el Mané Garrincha'),
    ('第 35 轮本周只有一场：米拉索尔 × 米内罗竞技', 'La jornada 35 solo tiene un partido esta semana: Mirassol × Atlético-MG'),
    ('gol=射入球网的得分 b', 'gol = el tanto marcado en la red (b)'),
    ('ida=对决的第一场 d', 'ida = el primer partido de una eliminatoria (d)'),
    ('volta=对决的第二场 a', 'volta = el segundo partido de una eliminatoria (a)'),
    ('pênalti=十一米点的罚球 c', 'pênalti = el tiro desde el punto de penalti (c)'),
    ('用括号里正确的比较形式填空。', 'Completa con la forma comparativa correcta entre paréntesis.'),
    ('5 小时 < 5.5 小时：menos', '5 horas < 5,5 horas: menos'),
    ('把句子补全成过去时（pretérito perfeito）。', 'Completa las frases en pasado (pretérito perfeito).'),
    ('vencer 过去时 ele 形式：venceu', 'vencer, pasado, forma ele: venceu'),
    ('marcar 过去时 eles 形式：marcaram', 'marcar, pasado, forma eles: marcaram'),
    ('marcar 过去时 ele 形式：marcou', 'marcar, pasado, forma ele: marcou'),
    ('convocar 过去时 ele 形式：convocou', 'convocar, pasado, forma ele: convocou'),
    ('ser 过去时复数：foram', 'ser, pasado, plural: foram'),
    # P5
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）', '1. Confira o Cartão de Confirmação do Enem (comprueba tu tarjeta de confirmación del Enem)'),
    ('2. Revise um pouco por dia: Natureza e Matemática（每天复习一点：自然科学与数学）', '2. Revise um pouco por dia: Natureza e Matemática (repasa un poco cada día: ciencias de la naturaleza y matemáticas)'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）', '3. Durma bem na véspera da prova (duerme bien la víspera de la prueba)'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）', '4. Separe documento e caneta preta no dia anterior (prepara el documento y el bolígrafo negro el día anterior)'),
    ('5. Domingo 15: chegue antes das 12h（周日 15 日：12 点前到达）', '5. Domingo 15: chegue antes das 12h (domingo 15: llega antes de las 12h)'),
    ('a natureza 自然科学 · a matemática 数学 · a maratona 突击马拉松 · a véspera 前夕 · comparar 比较价格 · a cabeça 头脑、状态。', 'a natureza = ciencias de la naturaleza · a matemática = matemáticas · a maratona = el maratón de repaso · a véspera = la víspera · comparar = comparar precios · a cabeça = la cabeza, el estado.'),
    ('重要考试前一晚，你是复习到很晚还是早睡？写两句寄来。', 'La noche antes de un examen importante, ¿repasas hasta tarde o te acuestas pronto? Escribe dos frases y envíanoslas.'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · EJERCICIOS PÁGINA 5'),
    ('读第 5 版文章，选出正确答案。', 'Lee la página 5 y elige la respuesta correcta.'),
    ('最后一周在 11 月 15 日周日结束', 'La última semana termina el domingo 15 de noviembre'),
    ('每天复习一点', 'Repasar un poco cada día'),
    ('提前一天备好证件和黑笔', 'Preparar el documento y el bolígrafo negro el día anterior'),
    ('黑五在 11 月 27 日', 'El Black Friday es el 27 de noviembre'),
    ('11 月 14 日周六巴西 × 日本 7:15', 'Sábado 14: Brasil × Japón a las 7:15'),
    ('用方框里的词填空。注意：有的词要变成复数。', 'Completa con las palabras del recuadro. Ojo: una palabra va en plural.'),
    ('última semana = 最后一周', 'última semana = la última semana'),
    ('inscrito 配合复数：inscritos', 'inscrito concuerda en plural: inscritos'),
    ('véspera = 前夕', 'véspera = la víspera'),
    ('maratona = 突击马拉松', 'maratona = el maratón de repaso'),
    ('local = 地点', 'local = el lugar'),
    ('separar 祈使式：separe', 'separar, imperativo: separe'),
    ('用将来时（futuro do presente）补全。', 'Completa en futuro (futuro do presente).'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer, futuro, forma eles irregular: farão'),
    ('mostrar 将来时：mostrará', 'mostrar, futuro: mostrará'),
    ('sair 将来时复数：sairão', 'sair, futuro, plural: sairão'),
    ('chegar 将来时：chegará', 'chegar, futuro: chegará'),
    ('错：考前突击不是好计划，每天复习一点才好', 'Falso: atracarse la víspera no es buen plan; un poco cada día es mejor'),
    ('对：13:30 至 18:30', 'Verdadero: de 13:30 a 18:30'),
    # P6
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。', 'os portões = las puertas · a segunda chamada = una segunda convocatoria, un segundo acceso · conferir = comprobar · a correria = la prisa.'),
    ('O DOMINGO 15 EM NÚMEROS · 11 月 15 日的数字 (horários oficiais do Inep)', 'O DOMINGO 15 EM NÚMEROS · LOS NÚMEROS DEL 15 DE NOVIEMBRE (horarios oficiales del Inep)'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · EJERCICIOS PÁGINA 6'),
    ('看上面两张图，选出正确答案。', 'Mira los dos gráficos de arriba y elige la respuesta correcta.'),
    ('大门开放 60 分钟', 'Las puertas están abiertas 60 minutos'),
    ('关门到开考之间等 30 分钟', 'La espera entre el cierre y la prueba es de 30 minutos'),
    ('考试 300 分钟', 'La prueba dura 300 minutos'),
    ('中午到 18:30 = 6 个半小时', 'Del mediodía a las 18:30 = seis horas y media'),
    ('图表数字是 Inep 官方时间', 'Los números del gráfico son los horarios oficiales del Inep'),
    ('高考分 8 日和 15 日两个周日', 'El Enem se hace en dos domingos: el 8 y el 15'),
    ('13 点后到场不得入内', 'Después de las 13h ya no se entra'),
    ('根据句子意思，补全正确的动词形式。', 'Completa con la forma verbal correcta para cada frase.'),
    ('将来时：começará', 'Futuro: começará'),
    ('quem + 虚拟式将来：chegar', 'quem + futuro de subjuntivo: chegar'),
    ('现在时：fecham', 'Presente: fecham'),
    ('现在时：pede', 'Presente: pede'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir', 'Completa con las palabras del recuadro: portões · segunda chamada · local · conferir'),
    ('portões = 大门', 'portões = las puertas'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = una segunda convocatoria, un segundo acceso'),
    ('祈使式：confira', 'Imperativo: confira'),
    # P7
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro', 'Preguntas: que horas (¿a qué hora?) + verbo; onde fica pregunta por el lugar; conferir es irregular en la forma eu: confiro.'),
    ('conferir：eu → confiro（不规则）', 'conferir: eu → confiro (irregular)'),
    ('onde 问地点', 'onde pregunta por el lugar'),
    ('讲一周的事用过去时（pretérito perfeito）；vencer 规则（venceu）；marcar/chegar/dormir 的过去时注意重音。', 'Para contar la semana usamos el pasado (pretérito perfeito); vencer es regular (venceu); ojo con la acentuación en el pasado de marcar, chegar y dormir.'),
    ('vencer 过去时：venceu', 'vencer, pasado: venceu'),
    ('marcar 过去时：marcou', 'marcar, pasado: marcou'),
    ('chegar 过去时：chegou', 'chegar, pasado: chegou'),
    ('venceram 是 vencer 的过去时复数', 'venceram es el pasado, plural, de vencer'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。', 'Después de quando, se y quem va el futuro de subjuntivo: tiver, for, chegar — la gramática de las hipótesis del domingo.'),
    ('quem + 虚拟式将来：tiver', 'quem + futuro de subjuntivo: tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + futuro de subjuntivo: chegar'),
    ('se + ser 的虚拟式将来：for', 'se + futuro de subjuntivo de ser: for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + futuro → futuro de subjuntivo for'),
    ('高考用黑笔，蓝笔不行。', 'Solo bolígrafo negro: el azul no vale.'),
    ('13 点关门，13:30 到就晚了。', 'Cierre a las 13h: llegar a las 13:30 es tarde.'),
    ('15 日考试 18:30 结束，19 点是 8 日的时间。', 'El 15 la prueba termina a las 18:30; las 19h son del día 8.'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · ERRORES'),
    ('proclamação = 宣布；1889 年君主制结束、共和国开始。', 'proclamação = proclamación; en 1889 termina la monarquía y empieza la república.'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · LA PALABRA'),
    ('编辑部说明：上期（VOL.2）承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期（VOL.4）。', 'Nota de la redacción: las cartas reales y los mejores textos prometidos en el VOL.2 no habían llegado al cierre — queda el ejemplo y la promesa pasa al VOL.4.'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！', 'Ejemplo de la redacción, no una carta real. ¡Envíanos tu carta!'),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）', 'FRASES DA SEMANA · FRASES DE LA SEMANA (citadas palabra por palabra en este número)'),
    ('两个周日、一个假日：巴西迎来高考第二天。', 'Dos domingos, un festivo: Brasil afronta el segundo día del Enem.'),
    ('考试和假日在同一天到来。', 'El examen y el festivo llegan el mismo día.'),
    ('假日不改变时钟。', 'El festivo no cambia el reloj.'),
    ('君主制结束了。', 'La monarquía se acabó.'),
    ('谁能进巴西杯决赛？', '¿Quién llegará a la final de la Copa do Brasil?'),
    ('睡得好，记得牢。', 'Dormir bien, recordar mejor.'),
    ('先做容易的，再做难的。', 'Primero las fáciles, luego las difíciles.'),
    ('核对确认卡、睡好、早到。', 'Comprueba la tarjeta, duerme bien, llega pronto.'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.4)', 'A PRÓXIMA SEMANA · LA PRÓXIMA SEMANA (VOL.4)'),
    # P8
    ('第 2 天在 11 月 15 日', 'El día 2 es el 15 de noviembre'),
    ('第 1 天在 11 月 8 日', 'El día 1 es el 8 de noviembre'),
    ('确认卡是高考的文件', 'La tarjeta de confirmación pertenece al Enem'),
    ('共和国宣言日在 11 月 15 日', 'La Proclamación de la República es el 15 de noviembre'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', 'La vuelta Vasco × Palmeiras es el día 8'),
    ('第二天共 90 道题', 'El día 2 tiene 90 preguntas en total'),
    ('考试时长 5 小时', 'La prueba dura 5 horas'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场', 'La vuelta Atlético-MG × Grêmio es en la Arena MRV'),
    ('第 35 轮本周只有一场，在 14 日', 'La jornada 35 solo tiene un partido esta semana, el día 14'),
    ('共和国宣言在 1889 年', 'La Proclamación de la República fue en 1889'),
    ('11.11 是促销日', 'El 11.11 es el día de las ofertas'),
    ('300 是考试的分钟数', '300 es la duración de la prueba en minutos'),
    ('德奥多罗是第一任总统', 'Deodoro fue el primer presidente'),
    ('玛丽娜住在圣保罗', 'Marina vive en São Paulo'),
    ('她每天复习一点自然科学', 'Ella repasa un poco de ciencias de la naturaleza cada día'),
    ('前一晚她备好证件和黑笔、早睡', 'La víspera prepara el documento y el bolígrafo negro y se acuesta pronto'),
    ('她 11:30 到达考场', 'Llega al centro de examen a las 11:30'),
    ('时间词在前', 'La palabra de tiempo va delante'),
    ('主语 + 动词 + 宾语 + 地点', 'Sujeto + verbo + objeto + lugar'),
    ('疑问词组在句首', 'El grupo interrogativo va al principio'),
    ('主语 + 动词 + 宾语', 'Sujeto + verbo + objeto'),
    ('11 月 15 日周日是高考的第二天。', 'El domingo 15 de noviembre es el segundo día del Enem.'),
    ('对照第 6 版标题', 'Mira el título de la página 6'),
    ('周日前核对确认卡。', 'Comprueba la tarjeta antes del domingo.'),
    ('Confira = 请核对', 'Confira = comprueba'),
    ('“假日落在周日。” → ___', '«El festivo cae en domingo.» → ___'),
    ('虚拟式将来 chegar + 祈使 apresente', 'Futuro de subjuntivo chegar + imperativo apresente'),
    ('你到达时，请出示带照片的证件。 → ___', 'Cuando llegues, muestra el documento con foto. → ___'),
    ('proclamação=宣布一个变化 b', 'proclamação = anunciar un cambio (b)'),
    ('portão=考场入口 d', 'portão = la entrada del centro de examen (d)'),
    ('república=1889 年后的国家形式 a', 'república = la forma de Estado después de 1889 (a)'),
    ('segunda chamada=关门后的再入场（高考没有） c', 'segunda chamada = reentrada tras el cierre (no existe en el Enem) (c)'),
    ('documento com foto 带照片的证件', 'documento com foto = documento con foto'),
    ('seção = 考场分区（房间）', 'seção = el aula de examen (la sección)'),
    ('大门 13 点关闭', 'Las puertas cierran a las 13h'),
    ('考试 18:30 结束', 'La prueba termina a las 18:30'),
    ('obrigado = 谢谢', 'obrigado = gracias'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。', 'Ejercicio de escritura (sin respuesta única); el texto modelo ({NWORDS} palabras) está abajo.'),
    ('（开放题，范文如下）', '(ejercicio abierto: texto modelo abajo)'),
    ('范文见本版 H 区（{NWORDS} 词）', 'Mira el texto modelo en la parte H de esta página ({NWORDS} palabras)'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可', 'RESPOSTAS · RESPUESTAS — ordenadas por página; busca tu número'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', 'Una nota breve por respuesta · ✓ = el ejercicio de escritura'),
]

for fn, reps in [('content12.py', REPL), ('content34.py', REPL),
                 ('content56.py', REPL), ('content7.py', REPL), ('content8.py', REPL)]:
    seen, ordered = set(), []
    for old, new in reps:
        if old not in seen:
            seen.add(old); ordered.append((old, new))
    reps = sorted(ordered, key=lambda r: -len(r[0]))
    t = load(fn)
    for old, new in reps:
        if old in t:
            t = sub(t, old, new, fn=fn)
        else:
            print(f'WARN {fn}: not found (skipped): {old[:60]!r}')
    save(fn, t)

# ---------- 5. disclosure rename + layout tweaks (EN/DE/FR precedent) ----------
t = load('content7.py')
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_es')
old_wh = 'len(wrap("proclamação = proclamación; en 1889 termina la monarquía y empieza la república.", "sans", False, 20, CW - 44)) * 29 + 20'
assert t.count(old_wh) == 1, 'word-box pad line not found'
t = t.replace(old_wh, 'len(wrap("proclamação = proclamación; en 1889 termina la monarquía y empieza la república.", "sans", False, 20, CW - 44)) * 29 + 30')
assert t.count(')) * 29 + 35') == 1, 'letters-box pad line not found'
t = t.replace(')) * 29 + 35', ')) * 29 + 22')
t = line_replace(t, 'fy = max(1712,', 'fy = max(1712, ly + lh + 14)', 'content7.py')
t = line_replace(t, 'cyq = fy + 66', '    cyq = fy + 66 + (i % 4) * 88', 'content7.py')
save('content7.py', t)

t = load('content8.py')
t = line_replace(t, 'af.para(txt, 13.5',
    '        af.para(txt, 13, lh=1.12, gap=0.5, split=False)',
    'content8.py')
save('content8.py', t)

t = load('content12.py')
old_box = '    ("90 — as questões do dia 15: 45 + 45 (90 preguntas: 45 + 45)", "serif", False, INK, 20, 1.35),\n])'
assert t.count(old_box) == 1, 'numbers box close not found'
t = t.replace(old_box, old_box[:-2] + '], tsize=20)')
save('content12.py', t)

# ---------- 5c. FIX F-1 (Round 1 proofread): fullwidth colon in P8 notes ----------
# The 10 note strings below are pure Portuguese (no CJK gloss) inherited from
# the core register with U+FF1A (：). In Latin-script editions they must use
# an ASCII colon, matching neighbouring notes (e.g. item 101). CJK editions
# (ja/zh-cn/zh-tw) legitimately keep ： inside CJK glosses, so this block is
# present ONLY in the 8 Latin-script transforms. Runs after the REPL loop.
for _fn, _old, _new in [
    ("content12.py", "conferir：ele → confere", "conferir: ele → confere"),
    ("content12.py", "abrir：ele → abre", "abrir: ele → abre"),
    ("content12.py", "levar：nós → levamos", "levar: nós → levamos"),
    ("content12.py", "começar：ela → começa", "começar: ela → começa"),
    ("content12.py", "terminar：ela → termina", "terminar: ela → termina"),
    ("content34.py", "2 > 0：mais", "2 > 0: mais"),
    ("content34.py", "3 > 2：mais", "3 > 2: mais"),
    ("content34.py", "17 < 18：mais cedo", "17 < 18: mais cedo"),
    ("content7.py", "conferir：você → confere", "conferir: você → confere"),
    ("content7.py", "terminar：ela → termina", "terminar: ela → termina"),
]:
    _t = load(_fn)
    _t = sub(_t, _old, _new, _fn)
    save(_fn, _t)

# ---------- 6. verify: zero CJK in build sources ----------
for fn in ['bslib4.py', 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    hits = CJK.findall(t)
    assert not hits, f'{fn}: {len(hits)} CJK chars remain, e.g. {hits[:10]}'
    print(f'{fn}: CJK 0 OK')
print('TRANSFORM COMPLETE')
