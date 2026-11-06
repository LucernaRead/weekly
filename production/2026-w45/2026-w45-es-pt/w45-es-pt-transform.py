# -*- coding: utf-8 -*-
"""W45 ES core -> ES x PT fan-out transform for the BUILD COPY ONLY.

Literal replacements only (README #17/#18): each (files, old, new) asserts
the total occurrence count across the listed files before replacing.
No AST byte-offset splicing; value maps use bare text, never repr literals.
Spanish target-language text is never a replacement target, EXCEPT the
explanation layer itself: notes/bridges/glosses/box titles/furniture and
the P8 E-section redirection (W43 ESxPT KIT §3 precedent: keys 137/138
re-aimed to PT, stems 139/140 re-aimed to PT, keys 139/140 byte-identical
Spanish, apparatus key 150 per the same precedent). Pure form derivations
("todos -> preguntan", "ganar -> gano", "el 1 = el uno", the P7 clinic's
Spanish middle comments, the Ana letter body + attribution) stay
byte-identical: they are language-neutral or frozen target text.
Furniture copied verbatim from shipped W43 ESxPT (files/weekly-report-es-pt
+ its build dir), VOL.1 -> VOL.2 only. Where W43 shipped practice and the
tools README #20 generic description differ, W43 shipped wins (badge
19.5pt BRICK in the y=372 subtitle slot; top strip first segment SEMANAL
per W43 KIT D1, measured: CADA form ends x=1429.5 vs date ink start
x=1420.7, i.e. a real collision; SEMANAL form ends x=1406.3, 14.4px clear).
On any COUNT MISMATCH: restore the build copy from
hidden_files/weekly-report-w45-es-build and re-run this script from scratch.
"""
import pathlib, sys

B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-pt-build')
C12, C34, C56, C7, C8, BS = 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py', 'bslib4.py'
ALL = [C12, C34, C56, C7, C8]

def rep(files, old, new, expect=None, allow_zero=False):
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
    if total == 0 and not allow_zero:
        print(f'NOT FOUND: {old!r}'); sys.exit(1)

# ---------- repoint OUT + render names (copy only; core untouched) ----------
rep(ALL, 'weekly-report-w45-es-core', 'weekly-report-w45-es-pt', 5)
rep(['render.py'], 'weekly-report-w45-es-core', 'weekly-report-w45-es-pt', 1)
rep(['render.py'], 'La-Lucerna-VOL2-web.pdf', 'La-Lucerna-VOL2-PT-web.pdf', 1)
rep(['render.py'], 'La-Lucerna-VOL2.pdf', 'La-Lucerna-VOL2-PT.pdf', 1)
rep(['render.py'], 'Render the ES core edition', 'Render the ES x PT edition', 1)

# ---------- bslib4 furniture (W43 ESxPT verbatim, VOL.1 -> VOL.2) ----------
rep([BS], '"La Lucerna · 西班牙语周报 VOL.2 · LUCERNA SPANISH WEEKLY"',
    '"La Lucerna · SEMANÁRIO ESPANHOL VOL.2 · TEXTOS EM ESPANHOL · EXPLICAÇÕES EM PORTUGUÊS"', 1)
rep([BS], 'f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"', 1)
rep([BS], '"译注｜" + s', '"Nota — " + s', 1)

# ---------- P8 writing bridge + type names + instruction chips (longest first) ----------
rep([C8], '写作题（无唯一答案）；范文（84 词）见下。',
    'Questão de redação (sem resposta única); o texto-modelo (84 palavras) segue abaixo.', 1)
for old, new in [
    ('完形单选', 'Escolha no texto'), ('完成句子', 'Completar frases'),
    ('单选', 'Escolha múltipla'),
    ('判断对错', 'Verdadeiro ou falso'), ('造句', 'Formar frases'),
    ('句型转换', 'Reescrever frases'), ('词汇配对', 'Associar palavras'),
    ('翻译', 'Tradução'), ('写作', 'Escrita'),
]:
    for lv in ('A2', 'B1', 'B2'):
        rep(ALL, '("%s", "%s", ' % (lv, old), '("%s", "%s", ' % (lv, new), allow_zero=True)
rep([C8], '== "写作"', '== "Escrita"', 1)
rep(ALL, 'instr="填空"', 'instr="Complete"')
rep(ALL, 'instr="判断"', 'instr="Verdadeiro ou falso"')
rep(ALL, 'instr="造句"', 'instr="Forme a frase"')
rep(ALL, 'instr="改写"', 'instr="Reescreva"')
rep(ALL, 'instr="翻译"', 'instr="Traduza"')
rep(ALL, 'instr="写作"', 'instr="Escreva"')
rep(ALL, 'instr="把词和释义配对"', 'instr="Associe"')

# ---------- shared furniture ----------
rep(ALL, '答案见第 8 版 · 题目可跨级混排，按题号找答案',
    'Respostas na página 8 · Os exercícios podem misturar os níveis: procure pelo número', 5)
rep(ALL, '¿Y TÚ? · 说说你自己', '¿Y TÚ? · E você?', 4)
rep([C12], 'EJERCICIOS · 第 2 版练习', 'EJERCICIOS · EXERCÍCIOS DA PÁGINA 2', 1)
rep([C34], 'EJERCICIOS · 第 3 版练习', 'EJERCICIOS · EXERCÍCIOS DA PÁGINA 3', 1)
rep([C34], 'EJERCICIOS · 第 4 版练习', 'EJERCICIOS · EXERCÍCIOS DA PÁGINA 4', 1)
rep([C56], 'EJERCICIOS · 第 5 版练习', 'EJERCICIOS · EXERCÍCIOS DA PÁGINA 5', 1)
rep([C56], 'EJERCICIOS · 第 6 版练习', 'EJERCICIOS · EXERCÍCIOS DA PÁGINA 6', 1)
rep([C12], 'VIDA · 生活', 'VIDA · VIDA COTIDIANA', 1)
rep([C34], 'CULTURA · 文化', 'CULTURA · CULTURA', 1)
rep([C34], 'DEPORTE · 体育', 'DEPORTE · ESPORTE', 1)
rep([C56], 'JUVENTUD · 青年', 'JUVENTUD · JUVENTUDE', 1)
rep([C56], 'A FONDO · 深读', 'A FONDO · EM PROFUNDIDADE', 1)
rep([C7], 'LENGUA · 语言', 'LENGUA · LÍNGUA', 1)
rep([C8], 'EJERCICIOS Y RESPUESTAS · 练习与答案', 'EJERCICIOS Y RESPUESTAS · EXERCÍCIOS E RESPOSTAS', 1)

print('PART 1 OK')

# ---------- P1 ----------
rep([C12], 'p.text(975, 92, "CADA SEMANA EN ESPAÑOL · 每周一期 · 读西班牙人正在读的西班牙语", 21, "sans", False, GREY, anchor="middle")',
    'p.text(975, 92, "SEMANAL EN ESPAÑOL · UM NÚMERO POR SEMANA · O ESPANHOL QUE A ESPANHA LÊ", 21, "sans", False, GREY, anchor="middle")', 1)
rep([C12], 'p.text(975, 330, "西 班 牙 语 周 报 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL", 46, "serif", True, INK, anchor="middle")',
    'p.text(975, 330, "SEMANÁRIO ESPANHOL · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL", 46, "serif", True, INK, anchor="middle")', 1)
rep([C12], 'p.text(975, 372, "EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA", 19, "sans", False, GREY, anchor="middle")',
    'p.text(975, 372, "TEXTOS EM ESPANHOL · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 19.5, "sans", True, BRICK, anchor="middle")', 1)
rep([C12], '距大选还有 27 天 · 住房决定选战', 'Faltam 27 dias para o 29-N · A habitação decide a campanha', 1)
rep([C12], '本期头条 · 详见第 2、6 版', 'A manchete desta edição · Ver páginas 2 e 6', 1)
rep([C12], 'LA NOTICIA · 头条', 'LA NOTICIA · A notícia', 1)
rep([C12], 'f.bridge("讲解｜la cuenta atrás 倒计时 · disolver las Cortes 解散议会 · el decreto 法令 · la candidatura 候选人名单。")',
    'f.bridge("Nota — la cuenta atrás (contagem decrescente) · disolver las Cortes (dissolver o parlamento) · el decreto (o decreto) · la candidatura (a candidatura).")', 1)
rep([C12], 'f.box("LA SEMANA EN CIFRAS · 数字看本周", [', 'f.box("LA SEMANA EN CIFRAS · Em números", [', 1)
rep([C12], '27 — días faltan el lunes 2 para las elecciones del domingo 29（距 29 日大选 27 天）',
    '27 — días faltan el lunes 2 para las elecciones del domingo 29 (faltam 27 dias para o dia 29)', 1)
rep([C12], '9 — comunidades donde el lunes 2 de noviembre es fiesta（11 月 2 日放假的自治区）',
    '9 — comunidades donde el lunes 2 de noviembre es fiesta (feriado na segunda, 2 de novembro)', 1)
rep([C12], '55,7 — % que cita la vivienda como el principal problema, según el CIS de octubre（CIS 十月数据）", "serif", False, INK, 20.5, 1.35),\n])',
    '55,7 — % que cita la vivienda como el principal problema, según el CIS de octubre (dados do CIS de outubro)", "serif", False, INK, 20.5, 1.35),\n], tsize=20)', 1)
rep([C12], 'f.head("AHORA TÚ · 即学即练", 25)', 'f.head("AHORA TÚ · Agora você", 25)', 1)
rep([C12], 'las listas ya están presentadas; ahora se escriben los programas',
    'as listas já foram apresentadas; agora escrevem-se os programas', 1)
rep([C12], '大选在 11 月 29 日周日', 'as eleições são no domingo, 29 de novembro', 1)
rep([C12], '住房是选战的决定性议题', 'a habitação decide a campanha', 1)
rep([C12], '周一放假的自治区有 9 个', 'nove comunidades têm feriado na segunda', 2)
rep([C12], '马竞–巴萨周日 21:00 开球', 'o Atlético–Barça é no domingo às 21:00', 1)
rep([C12], 'NFL 马德里站周日 15:30 开球', 'a NFL chega ao Bernabéu no domingo às 15:30', 1)
rep([C12], '本周五大看点 · Para entender la semana', 'Os cinco temas · Para entender la semana', 1)
rep([C12], '五大看点，不编数字：全在本期里讲清。', 'Nada inventado: tudo explicado aqui.', 1)
rep([C12], 'EN ESTA EDICIÓN · 本期目录', 'EN ESTA EDICIÓN · Nesta edição', 1)
rep([C12], '“竞选预热期”：正式竞选前的几周。', '«Pré-campanha»: semanas antes da campanha.', 1)
rep([C12], 'BREVES · 快讯', 'BREVES · Em resumo', 1)
rep([C12], 'QUIZ RELÁMPAGO · 闪电问答', 'QUIZ RELÁMPAGO · Quiz-relâmpago', 1)
rep([C12], '读头版，选出正确答案 · 答案见第 8 版', 'Leia a capa, escolha a resposta certa · Respostas na página 8', 1)
rep([C12], '大选在 11 月 29 日', 'as eleições são no dia 29 de novembro', 2)
rep([C12], 'NFL 马德里站周日下午', 'a NFL chega ao Bernabéu no domingo', 1)
rep([C12], '马竞–巴萨周日 21:00', 'o Atlético–Barça é no domingo às 21:00', 1)

# ---------- P2 ----------
rep([C12], 'NIVEL A2 · El puente del lunes 2 · 11 月 2 日的连休',
    'NIVEL A2 · El puente del lunes 2 · A PONTE DE SEGUNDA, 2 DE NOVEMBRO', 1)
rep([C12], 'f.box("EL CALENDARIO · 本周日历", [', 'f.box("EL CALENDARIO · O calendário da semana", [', 1)
rep([C12], 'Lunes 2 — puente en nueve comunidades; las candidaturas proclamadas llegan al BOE el martes 3（周一九地连休；周二《官方公报》公布正式候选名单）',
    'Lunes 2 — puente en nueve comunidades; las candidaturas proclamadas llegan al BOE el martes 3 (ponte em nove comunidades; candidaturas oficiais no BOE na terça)', 1)
rep([C12], 'Martes 3 — Champions: Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG（周二欧冠三场西甲球队比赛）',
    'Martes 3 — Champions: Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG (terça: três jogos da Champions)', 1)
rep([C12], 'Miércoles 4 — Champions: AEK–Real Madrid, 18:45（周三皇马客场对雅典 AEK）',
    'Miércoles 4 — Champions: AEK–Real Madrid, 18:45 (quarta: o Real Madrid visita o AEK)', 1)
rep([C12], 'Jueves 5 — Europa League: Real Sociedad–Lyon, 18:45（周四皇家社会欧联对里昂）',
    'Jueves 5 — Europa League: Real Sociedad–Lyon, 18:45 (quinta: Real Sociedad–Lyon)', 1)
rep([C12], 'Viernes 6 — Liga, jornada 12: Sevilla–Alavés, 21:00（周五联赛第 12 轮开球）',
    'Viernes 6 — Liga, jornada 12: Sevilla–Alavés, 21:00 (sexta: abre a jornada 12)', 1)
rep([C12], 'Sábado 7 — Valencia–Real Madrid, 21:00, en Mestalla（周六瓦伦西亚对皇马）',
    'Sábado 7 — Valencia–Real Madrid, 21:00, en Mestalla (sábado: Valencia–Real Madrid)', 1)
rep([C12], 'Domingo 8 — NFL en el Bernabéu, 15:30; Atlético–Barça, 21:00（周日 NFL 马德里站＋马竞对巴萨）", "serif", False, INK, 21, 1.36),\n])',
    'Domingo 8 — NFL en el Bernabéu, 15:30; Atlético–Barça, 21:00 (domingo: NFL e Atlético–Barça)", "serif", False, INK, 21, 1.36),\n], tsize=19)', 1)
rep([C12], 'f.gloss("festivo 放假的 · el puente 连休 · la comunidad 自治区 · anochecer 天黑 · el horario de invierno 冬令时。")',
    'f.gloss("festivo (de festa) · el puente (a ponte) · la comunidad (a comunidade autónoma) · anochecer (anoitecer) · el horario de invierno (o horário de inverno).")', 1)
rep([C12], '11 月 2 日你那里放假吗？连休你做什么：旅行、休息还是看球？写两句西班牙语寄给编辑部。',
    'Na tua comunidade, a segunda, 2, é feriado? O que fazes na ponte: viajas, descansas ou vês futebol? Escreve duas frases em espanhol e envia-as à redação.', 2)
rep([C12], 'LOS DÍAS DE LA SEMANA · 这样说日期', 'LOS DÍAS DE LA SEMANA · Como dizer as datas', 1)
rep([C12], 'lunes 2 – domingo 8 de noviembre · 11 月 2 日周一至 8 日周日',
    'lunes 2 – domingo 8 de noviembre · 2 a 8 de novembro', 1)
rep([C12], 'e.bridge("用正确的日期形式补全句子。")', 'e.bridge("Complete as frases com a forma correta da data.")', 1)
rep([C12], '"11 月 2 日周一"', '"segunda, 2 de novembro"', 1)
rep([C12], '"11 月 8 日周日"', '"domingo, 8 de novembro"', 1)
rep([C12], '"每月 1 号说 el uno"', '"o dia 1 do mês é el uno"', 1)
rep([C12], '"月份小写"', '"o mês em minúsculas"', 1)
rep([C12], 'e.bridge("补全动词的现在时形式。")', 'e.bridge("Complete com a forma correta do verbo no presente.")', 1)
rep([C12], '"el lunes → es（单数）"', '"el lunes → es (singular)"', 1)
rep([C12], 'e.bridge("读第 2 版文章，选出正确答案。")', 'e.bridge("Leia o artigo da página 2 e escolha a resposta certa.")', 1)
rep([C12], '"九个自治区周一放假"', '"nove comunidades têm feriado na segunda"', 1)
rep([C12], '"诸圣节 11 月 1 日落在周日"', '"o Dia de Todos os Santos caiu num domingo, 1 de novembro"', 1)
rep([C12], '"加泰罗尼亚周一是工作日"', '"na Catalunha, a segunda é dia de trabalho"', 1)
rep([C12], '"冬令时第二周，天黑得早"', '"é a segunda semana de horário de inverno: anoitece cedo"', 1)
rep([C12], '["puente=三天连休 b", "festivo=放假的 a", "anochecer=天黑 c", "comunidad=自治区 d"]',
    '["puente=ponte de três dias b", "festivo=de festa a", "anochecer=anoitecer c", "comunidad=comunidade autónoma d"]', 1)

print('PART 2 OK')

# ---------- P3 ----------
rep([C34], 'A2 → B1 · La semana pasada: tres noches de otoño · 上周的三个秋夜',
    'A2 → B1 · La semana pasada: tres noches de otoño · A SEMANA PASSADA: TRÊS NOITES DE OUTONO', 1)
rep([C34], 'f.gloss("sobrio 克制的 · el homenaje 纪念表彰 · el disfraz 服装（化装） · el boniato 红薯 · el cementerio 墓地。")',
    'f.gloss("sobrio (sóbrio) · el homenaje (a homenagem) · el disfraz (o disfarce) · el boniato (a batata-doce) · el cementerio (o cemitério).")', 1)
rep([C34], '你最喜欢哪一夜：29 日、31 日还是 1 日？31 日你吃了什么？写两句寄来。',
    'De que noite gostas mais: 29, 31 ou 1? O que comeste no dia 31? Escreve duas frases e envia-as.', 2)
rep([C34], 'e.bridge("读第 3 版文章，判断对错。")', 'e.bridge("Leia o artigo da página 3 e diga se é verdadeiro ou falso.")', 1)
rep([C34], '"DANA 纪念活动在 10 月 29 日周四"', '"os atos de memória da DANA foram na quinta, 29 de outubro"', 1)
rep([C34], '"Castanyada 吃烤栗子、红薯和 panellets"', '"na Castanyada comem-se castanhas assadas, boniatos e panellets"', 1)
rep([C34], '"Samaín 是加利西亚古节，不是万圣节译名"', '"o Samaín é uma festa antiga galega, não o nome galego do Halloween"', 1)
rep([C34], '"诸圣节在 11 月 1 日，不是 10 月 31 日"', '"o Dia de Todos os Santos é 1 de novembro, não 31 de outubro"', 1)
rep([C34], '"周日家属去墓地献花"', '"no domingo, as famílias levaram flores aos cemitérios"', 1)
rep([C34], 'e.bridge("用方框里的词填空。")', 'e.bridge("Complete com as palavras do quadro.")', 1)
rep([C34], '"给逝者带花 flores"', '"levar flores aos falecidos (flores)"', 1)
rep([C34], '"cementerio = 墓地"', '"cementerio = o cemitério"', 1)
rep([C34], '"castañas asadas 烤栗子"', '"castañas asadas = castanhas assadas"', 1)
rep([C34], '"disfraz = 化装服装"', '"disfraz = o disfarce"', 1)
rep([C34], '"actos de memoria 纪念活动"', '"actos de memoria = atos de memória"', 1)
rep([C34], 'e.bridge("选出正确答案。")', 'e.bridge("Escolha a resposta certa.")', 1)
rep([C34], '"DANA 纪念是 2024 年风暴两周年"', '"a memória da DANA é dos dois anos da tempestade de 2024"', 1)
rep([C34], '"Castanyada 在加泰罗尼亚"', '"a Castanyada é na Catalunha"', 1)
rep([C34], '"Samaín 是加利西亚古老节日"', '"o Samaín é uma festa galega muito antiga"', 1)
rep([C34], '"三夜之后周一有人连休有人上班"', '"depois das três noites, na segunda uns fazem ponte e outros trabalham"', 1)
rep([C34], 'e.bridge("把词组成正确的句子。")', 'e.bridge("Forme frases corretas com as palavras.")', 1)
rep([C34], '"动词第二位"', '"o verbo em segundo lugar"', 1)
rep([C34], '"时间在前，动词第二"', '"o tempo primeiro, o verbo em segundo"', 1)
rep([C34], '"地点在前，动词第二"', '"o lugar primeiro, o verbo em segundo"', 1)
rep([C34], '"间接疑问用 si"', '"pergunta indireta com si"', 1)

# ---------- P4 ----------
rep([C34], 'NIVEL B1 · Europa primero, el domingo a las 21:00 · 欧战在先，周日晚九点',
    'NIVEL B1 · Europa primero, el domingo a las 21:00 · A EUROPA PRIMEIRO, DOMINGO ÀS 21:00', 1)
rep([C34], 'f.gloss("la jornada 轮次 · recortar la distancia 缩小分差 · recibir 主场迎战 · visitar 客场挑战 · el Metropolitano 马竞主场。")',
    'f.gloss("la jornada (a jornada) · recortar la distancia (reduzir a diferença) · recibir (jogar em casa) · visitar (jogar fora) · el Metropolitano (o estádio do Atlético).")', 1)
rep([C34], '周日 21:00 你看哪一场？马竞主场谁赢？写两句西班牙语寄来。',
    'No domingo às 21:00, que jogo vês? Quem ganha no Metropolitano? Escreve duas frases em espanhol e envia-as.', 2)
rep([C34], 'LA SEMANA EUROPEA Y LA JORNADA 12 · 欧战周与联赛第 12 轮',
    'LA SEMANA EUROPEA Y LA JORNADA 12 · A semana europeia e a jornada 12', 1)
rep([C34], 'e.bridge("读第 4 版文章，选出正确答案。")', 'e.bridge("Leia o artigo da página 4 e escolha a resposta certa.")', 1)
rep([C34], '"皇马 2–1 赢下国家德比"', '"o Madrid ganhou o Clásico por 2–1"', 1)
rep([C34], '"姆巴佩进了两球"', '"Mbappé marcou dois golos"', 1)
rep([C34], '"周二欧冠三场西甲球队比赛"', '"na terça, três jogos da Champions com equipas espanholas"', 1)
rep([C34], '"周日 21:00 马竞–巴萨"', '"o Atlético–Barça é no domingo às 21:00"', 1)
rep([C34], '"周日下午还有 NFL 马德里站"', '"no domingo à tarde há também a NFL em Madrid"', 1)
rep([C34], '["jornada=轮次 b", "recibir=主场迎战 a", "visitar=客场挑战 d", "recortar=缩小分差 c"]',
    '["jornada=a jornada b", "recibir=jogar em casa a", "visitar=jogar fora d", "recortar=reduzir a diferença c"]', 1)
rep([C34], 'e.bridge("用括号里词的比较级或 -ísimo 形式填空。")',
    'e.bridge("Complete com o comparativo ou a forma em -ísimo da palavra entre parênteses.")', 1)
rep([C34], '"más + importante（马竞–巴萨更重要）"', '"más + importante (o Atlético–Barça é mais importante)"', 1)
rep([C34], '"muchísimos partidos 比赛很多"', '"muchísimos partidos (muitíssimos jogos)"', 1)
rep([C34], '"malo 的比较级是 peor"', '"o comparativo de malo é peor"', 1)
rep([C34], '"bueno 的比较级是 mejor"', '"o comparativo de bueno é melhor"', 1)
rep([C34], 'e.bridge("把句子改成过去时（pretérito indefinido）。")',
    'e.bridge("Passe as frases para o pretérito indefinido.")', 1)
rep([C34], '"ir 的过去时是 fueron"', '"o passado de ir é foram"', 1)

print('PART 3 OK')

# ---------- P5 ----------
rep([C56], 'NIVEL B1 · La NFL en Madrid · NFL 来到马德里',
    'NIVEL B1 · La NFL en Madrid · A NFL EM MADRID', 1)
rep([C56], 'f.box("EL PLAN DEL PUENTE · 连休计划", [', 'f.box("EL PLAN DEL PUENTE · O plano da ponte", [', 1)
rep([C56], '1. El lunes 2: descanso y familia — o viaje, si tu comunidad hace puente（周一：休息陪家人；若你那里连休，就去旅行）',
    '1. El lunes 2: descanso y familia — o viaje, si tu comunidad hace puente (segunda: descanso e família; viagem, se a tua comunidade faz ponte)', 1)
rep([C56], '2. El sábado 7: Valencia–Real Madrid, 21:00, en Mestalla（周六晚：瓦伦西亚对皇马）',
    '2. El sábado 7: Valencia–Real Madrid, 21:00, en Mestalla (sábado à noite: Valencia–Real Madrid)', 1)
rep([C56], '3. El domingo 8, 15:30: la NFL en el Bernabéu（周日下午：NFL 马德里站）',
    '3. El domingo 8, 15:30: la NFL en el Bernabéu (domingo à tarde: a NFL em Madrid)', 1)
rep([C56], '4. El domingo 8, 21:00: Atlético–Barça en el Metropolitano（周日晚：马竞对巴萨）',
    '4. El domingo 8, 21:00: Atlético–Barça en el Metropolitano (domingo à noite: Atlético–Barça)', 1)
rep([C56], '5. Y el lunes 9: vuelta a clase y al trabajo; la campaña empieza el viernes 13（返校返工；竞选 13 日开始）", "serif", False, INK, 21, 1.36),\n])',
    '5. Y el lunes 9: vuelta a clase y al trabajo; la campaña empieza el viernes 13 (volta às aulas e ao trabalho; a campanha começa dia 13)", "serif", False, INK, 21, 1.36),\n], tsize=20)', 1)
rep([C56], 'f.gloss("el emparrillado 美式足球场（烤架形场地） · el himno 国歌 · el touchdown 达阵得分 · la calabaza 南瓜。")',
    'f.gloss("el emparrillado (o campo com forma de grelha) · el himno (o hino) · el touchdown (o touchdown) · la calabaza (a abóbora).")', 1)
rep([C56], '你看过美式足球比赛吗？你更喜欢足球还是美式足球？写两句寄来。',
    'Já viste um jogo de futebol americano? Preferes futebol ou futebol americano? Escreve duas frases e envia-as.', 2)
rep([C56], 'e.bridge("读第 5 版文章，选出正确答案。")', 'e.bridge("Leia o artigo da página 5 e escolha a resposta certa.")', 1)
rep([C56], '"NFL 马德里站周日 15:30"', '"a NFL em Madrid: domingo, 15:30"', 1)
rep([C56], '"孟加拉虎对猎鹰"', '"Bengals contra Falcons"', 1)
rep([C56], '"西班牙国歌由吉他手演奏"', '"o hino de Espanha é tocado por um guitarrista"', 1)
rep([C56], '"首场 NFL 伯纳乌赛在 2025 年 11 月 16 日"', '"o primeiro jogo da NFL no Bernabéu foi em 16 de novembro de 2025"', 1)
rep([C56], '"美式足球用手打、四次进攻"', '"o futebol americano joga-se com as mãos, em quatro tentativas"', 1)
rep([C56], 'e.bridge("用方框里的词填空。注意：有的词要变位。")',
    'e.bridge("Complete com as palavras do quadro. Atenção: algumas palavras mudam de forma.")', 1)
rep([C56], '"estadio = 体育场"', '"estadio = o estádio"', 1)
rep([C56], '"himno = 国歌"', '"himno = o hino"', 1)
rep([C56], '"acoger 变位 → acoge"', '"a conjugação de acoger → acoge"', 1)
rep([C56], '"touchdown = 达阵得分"', '"touchdown = o touchdown"', 1)
rep([C56], '"calabaza = 南瓜"', '"calabaza = a abóbora"', 1)
rep([C56], '"disfraz = 化装服装"', '"disfraz = o disfarce"', 1)
rep([C56], 'e.bridge("用 ir a + 原形动词改写句子，表示“将要”。")',
    'e.bridge("Reescreva as frases com ir a + infinitivo, para exprimir o futuro.")', 1)
rep([C56], '"vamos a + 原形"', '"vamos a + infinitivo"', 1)
rep([C56], '"va a + 原形"', '"va a + infinitivo"', 1)
rep([C56], '"vas a + 原形"', '"vas a + infinitivo"', 1)
rep([C56], '"van a + 原形"', '"van a + infinitivo"', 1)
rep([C56], '"NFL 马德里站是伯纳乌第二场 NFL 比赛"', '"o jogo da NFL em Madrid é o segundo no Bernabéu"', 1)
rep([C56], '"美国国歌由 Momsen 演唱，不是 Sáinz-Villegas"', '"o hino dos EUA é cantado por Momsen, não por Sáinz-Villegas"', 1)
rep([C56], '"万圣节之夜在周六 31 日"', '"a noite de Halloween foi no sábado 31"', 1)

# ---------- P6 ----------
rep([C56], 'NIVEL B2 · La vivienda decide la campaña · 住房决定选战',
    'NIVEL B2 · La vivienda decide la campaña · A HABITAÇÃO DECIDE A CAMPANHA', 1)
rep([C56], 'e.bridge("看上面两张图，选出正确答案。")', 'e.bridge("Veja os dois gráficos acima e escolha a resposta certa.")', 1)
rep([C56], '"CIS 里 PSOE 第一（34%）"', '"no CIS, o PSOE vai em primeiro (34%)"', 1)
rep([C56], '"CIS 里 PP 22,2%"', '"no CIS, o PP tem 22,2%"', 1)
rep([C56], '"住房是首要问题（55,7%）"', '"a habitação é o principal problema (55,7%)"', 1)
rep([C56], '"调查在 10 月 1–6 日进行"', '"o trabalho de campo foi de 1 a 6 de outubro"', 1)
rep([C56], '"本报只刊登 CIS 这一组数据并注明来源日期"', '"o jornal publica só a série do CIS, com fonte e data"', 1)
rep([C56], '"10 月 2 日议会否决两项住房法令"', '"no dia 2 de outubro, o parlamento rejeitou dois decretos de habitação"', 1)
rep([C56], '"10 月 5 日解散议会并召集大选"', '"no dia 5 de outubro, dissolveram-se as Cortes e convocaram-se eleições"', 1)
rep([C56], '"民调是带误差的具体某天的照片"', '"uma sondagem é uma foto com margem de erro"', 1)
rep([C56], '"竞选 11 月 13 日开始"', '"a campanha começa no dia 13 de novembro"', 1)
rep([C56], '"es posible que + 虚拟式 tenga"', '"es posible que + subjuntivo (tenga)"', 1)
rep([C56], '"es importante que + 虚拟式 sea"', '"es importante que + subjuntivo (sea)"', 1)
rep([C56], '"para que + 虚拟式（目的）"', '"para que + subjuntivo (finalidade)"', 1)
rep([C56], '"Aunque 后接陈述式（已知事实）"', '"Aunque + indicativo (facto conhecido)"', 1)
rep([C56], 'e.bridge("用方框里的词填空：sondeo · muestra · indecisos · margen de error")',
    'e.bridge("Complete com as palavras do quadro: sondeo · muestra · indecisos · margen de error")', 1)
rep([C56], '"sondeo = 民调"', '"sondeo = a sondagem"', 1)
rep([C56], '"muestra = 样本（5.025 人）"', '"muestra = a amostra (5.025 pessoas)"', 1)
rep([C56], '"indecisos = 未决定者"', '"indecisos = os indecisos"', 1)
rep([C56], '"margen de error = 误差范围"', '"margen de error = a margem de erro"', 1)

print('PART 4 OK')

# ---------- P7 ----------
rep([C7], '语言聚焦 · Tres niveles, tres herramientas · 三个级别，三件工具',
    'FOCO NA LÍNGUA · Tres niveles, tres herramientas · TRÊS NÍVEIS, TRÊS FERRAMENTAS', 1)
rep([C7], 'a.bridge("日期格式：el lunes 2 de noviembre；星期、月份小写；1 号说 el uno。")',
    'a.bridge("O formato da data: el lunes 2 de noviembre; dias e meses em minúsculas; o dia 1 é el uno.")', 1)
rep([C7], '"el lunes 2 de noviembre 连休"', '"el lunes 2 de noviembre (dia de ponte)"', 1)
rep([C7], '"29 日是周日"', '"o dia 29 é domingo"', 1)
rep([C7], '"月份小写：noviembre"', '"o mês em minúsculas: noviembre"', 1)
rep([C7], 'b.bridge("比较级 más…que、tan…como；bueno→mejor、malo→peor；绝不说 más mejor。")',
    'b.bridge("O comparativo: más…que, tan…como; bueno→mejor, malo→peor; nunca se diz más mejor.")', 1)
rep([C7], '"más + cara（房价更高）"', '"más + cara (a habitação está mais cara)"', 1)
rep([C7], '"tan + alta + como（同样高）"', '"tan + alta + como (igualmente alta)"', 1)
rep([C7], '"bueno 的比较级是 mejor（不用 más）"', '"o comparativo de bueno é melhor (sem más)"', 1)
rep([C7], '"más mejor 是错误说法"', '"más mejor está errado"', 1)
rep([C7], 'c.bridge("es necesario que、para que、ojalá 后用虚拟式；creo que 后用陈述式。")',
    'c.bridge("es necesario que, para que e ojalá pedem o subjuntivo; creo que pede o indicativo.")', 1)
rep([C7], '"es necesario que + 虚拟式 baje"', '"es necesario que + subjuntivo (baje)"', 1)
rep([C7], '"para que + 虚拟式 sea"', '"para que + subjuntivo (sea)"', 1)
rep([C7], '"creo que + 陈述式 es"', '"creo que + indicativo (es)"', 1)
rep([C7], '"ojalá + 虚拟式：baje"', '"ojalá + subjuntivo: baje"', 1)
rep([C7], '"lunes 是单数，动词用 es。"', '"lunes é singular: o verbo vai no singular (es)."', 1)
rep([C7], '"mejor 本身就是比较级，不加 más。"', '"mejor já é comparativo: sem mais."', 1)
rep([C7], '"gente 是单数集合名词，动词用单数。"', '"gente é singular, como um só grupo."', 1)
rep([C7], '"creo que 表肯定，用陈述式 es。"', '"creo que afirma: modo indicativo (es)."', 1)
rep([C7], 'p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS · 常见错误", 23, "sans", True, OLIVE)',
    'p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS · Erros comuns", 20, "sans", True, OLIVE)', 1)
rep([C7], 'precampaña = 竞选预热期：正式竞选前的几周。本期就是 precampaña；竞选 13 日周五开始。',
    'precampaña = a pré-campanha: as semanas antes da campanha oficial. Esta edição é pré-campanha; a campanha começa na sexta, dia 13.', 2)
rep([C7], 'p.text(bx + 22, yy3 + 26, "LA PALABRA · 本周生词", 23, "sans", True, OLIVE)',
    'p.text(bx + 22, yy3 + 26, "LA PALABRA · A palavra da semana", 22, "sans", True, OLIVE)', 1)
rep([C7], 'ldcn = "编辑部说明：截至本期截稿，未收到真实读者来信与第 8 版最佳作文，故本期登载编辑部示例信，承诺顺延至 VOL.3。欢迎来信！"',
    'ldcn = "Nota da redação: até o fecho desta edição não chegaram cartas reais de leitores nem os melhores textos da página 8; publicamos esta carta de exemplo e a promessa passa para o VOL.3. Escreva-nos!"', 1)
rep([C7], 'FRASES DE LA SEMANA · 本周金句（逐字摘自本期文章）',
    'FRASES DE LA SEMANA · Frases da semana (retiradas dos textos desta edição)', 1)
rep([C7], '"名单已提交：现在各党开始撰写纲领。"', '"As listas já foram apresentadas: agora os partidos escrevem os seus programas."', 1)
rep([C7], '"11 月 2 日周一九个自治区放假，其他地区照常上班。"', '"Na segunda, 2 de novembro, nove comunidades têm feriado — e as outras trabalham."', 1)
rep([C7], '"三个节日，同一个秋夜。"', '"Três festas, uma mesma noite de outono."', 1)
rep([C7], '"皇马在诺坎普 2–1 获胜：这是巴萨本赛季联赛首败。"', '"O Madrid ganhou 2–1 no Camp Nou: foi a primeira derrota do Barça na Liga."', 1)
rep([C7], '"伯纳乌把草皮换成烤架形球场：美式足球来到马德里。"', '"O Bernabéu troca a relva pelo emparrillado: o futebol americano chega a Madrid."', 1)
rep([C7], '"住房是 55.7% 的西班牙人的首要问题。"', '"A habitação é o principal problema para 55,7% dos espanhóis."', 1)
rep([C7], '"一次民调就是一张带误差的照片，拍于某一天。"', '"Uma sondagem é uma foto com margem de erro, tirada num dia concreto."', 1)
rep([C7], '"11 月 8 日周日，马德里有两场约会：15:30 的 NFL 和 21:00 的马竞对巴萨。"', '"No domingo 8, Madrid tem dois compromissos: a NFL às 15:30 e o Atlético–Barça às 21:00."', 1)
rep([C7], 'LA PRÓXIMA SEMANA · 下期预告 (VOL.3)', 'LA PRÓXIMA SEMANA · Na próxima semana (VOL.3)', 1)

# ---------- P8 ----------
rep([C8], '第 8 版 · La gran prueba de la semana + todas las respuestas',
    'PÁGINA 8 · La gran prueba de la semana + todas las respuestas', 1)
rep([C8], '"ganó 2–1 = 以 2–1 获胜"', '"ganó 2–1 = venceu por 2–1"', 1)
rep([C8], '"marcar dos goles = 进两球"', '"marcar dos goles = marcar dois golos"', 1)
rep([C8], '"primera derrota liguera = 联赛首败"', '"primera derrota liguera = primeira derrota na Liga"', 1)
rep([C8], '"recortar = 缩小分差"', '"recortar = reduzir a diferença"', 1)
rep([C8], '"acoger = 承办（伯纳乌承办 NFL）"', '"acoger = receber (o Bernabéu recebe a NFL)"', 1)
rep([C8], '"el emparrillado = 美式足球场"', '"el emparrillado = o campo de futebol americano"', 1)
rep([C8], '"周日上演马竞–巴萨"', '"no domingo há Atlético–Barça"', 1)
rep([C8], '"himno = 国歌"', '"himno = o hino"', 1)
rep([C8], '"周一放假的自治区有 9 个"', '"nove comunidades têm feriado na segunda"', 1)
rep([C8], '"诸圣节 11 月 1 日"', '"o Dia de Todos os Santos é 1 de novembro"', 1)
rep([C8], '"马竞–巴萨与 NFL 都在周日"', '"o Atlético–Barça e a NFL são ambos no domingo"', 1)
rep([C8], '"Castanyada 吃 panellets"', '"na Castanyada comem-se panellets"', 1)
rep([C8], '"DANA 纪念活动在 10 月 29 日周四"', '"os atos de memória da DANA foram na quinta, 29 de outubro"', 1)
rep([C8], '"大选在 11 月 29 日"', '"as eleições são no dia 29 de novembro"', 1)
rep([C8], '"CIS 十月调查：住房 55,7%"', '"no CIS de outubro: a habitação, 55,7%"', 1)
rep([C8], '"竞选 11 月 13 日开始"', '"a campanha começa no dia 13 de novembro"', 1)
rep([C8], '"马德里在放假名单里"', '"Madrid está na lista de feriados"', 1)
rep([C8], '"加泰罗尼亚周一是工作日"', '"na Catalunha, a segunda é dia de trabalho"', 1)
rep([C8], '"Ana 只看 NFL；晚上看马竞–巴萨的是 Pablo"', '"Ana só vê a NFL; quem vê o Atlético–Barça à noite é o Pablo"', 1)
rep([C8], '"标题概括两地对比"', '"o título resume o contraste entre os dois lugares"', 1)
rep([C8], '"主语 + 动词 + 地点"', '"sujeito + verbo + lugar"', 1)
rep([C8], '"时间在前"', '"o tempo primeiro"', 1)
rep([C8], '"a las nueve = 在九点"', '"a las nueve = às nove horas"', 1)
rep([C8], '"疑问词在句首"', '"a palavra interrogativa no início"', 1)
# E-section redirection (W43 ESxPT KIT §3 precedent, verbatim pattern)
rep([C8], 'f.ex("A2", "Tradução", "周一在九个自治区是假日。", "对照原文"',
    'f.ex("A2", "Tradução", "Na segunda-feira é feriado em nove comunidades.", "Confira no original"', 1)
rep([C8], 'f.ex("A2", "Tradução", "周日我们看 NFL 和马竞–巴萨。", "对照原文"',
    'f.ex("A2", "Tradução", "No domingo vemos a NFL e o Atlético–Barça.", "Confira no original"', 1)
rep([C8], '"acoger = 承办"', '"acoger = receber"', 1)
rep([C8], '"伯纳乌承办一场 NFL 比赛。→ ___"', '"O Bernabéu recebe um jogo da NFL. → ___"', 1)
rep([C8], '"tener que = 必须"', '"tener que = ter de"', 1)
rep([C8], '"每个图表都必须标明来源。→ ___"', '"Cada gráfico tem de indicar a sua fonte. → ___"', 1)
rep([C8], '["sondeo=民调 c", "muestra=样本 d", "margen de error=误差范围 b", "junta electoral=选举委员会 a"]',
    '["sondeo=sondagem c", "muestra=amostra d", "margen de error=margem de erro b", "junta electoral=comissão eleitoral a"]', 1)
rep([C8], '"alquiler = 租金"', '"alquiler = o aluguer"', 1)
rep([C8], '"tres habitaciones = 三居室"', '"tres habitaciones = três quartos"', 1)
rep([C8], '"¿cuánto cuesta? 多少钱"', '"¿cuánto cuesta? = quanto custa?"', 1)
rep([C8], '"firmar = 签（合同）"', '"firmar = assinar (o contrato)"', 1)
rep([C8], '"mudanza = 搬家"', '"mudanza = a mudança"', 1)
rep([C8], '"（开放题，范文如下）"', '"Questão aberta — texto-modelo abaixo, nesta página"', 1)
rep([C8], '"范文见本版 H 区（84 词）"', '"Texto-modelo na seção H desta página (84 palavras)"', 1)
rep([C8], 'RESPUESTAS · 参考答案 — 按版面分页排列，找到题号即可',
    'RESPUESTAS · Respostas — por página, procure pelo número', 1)
rep([C8], '每题附一句中文简析 · 带 ✓ 的为范文题',
    'Cada resposta traz uma breve nota · ✓ marca a questão de redação', 1)

print('PART 5 OK')
print('TRANSFORM COMPLETE')

# ---------- PART 6 (misses found by post-transform CJK scan) ----------
# match_set() calls use a different call shape than ex() so the Part 1
# ("LV", "typ", pattern missed them; the only remaining "词汇配对" strings
# are these three calls. Stem-embedded ZH gloss in P5 (EN/FR/IT siblings
# all translated this fragment the same way).
rep(ALL, '"词汇配对"', '"Associar palavras"', 3)
rep([C56], 'El Bernabéu ___ (原形 acoger) un partido de la NFL.',
    'El Bernabéu ___ (infinitivo: acoger) un partido de la NFL.', 1)
print('PART 6 OK')

# ---------- PART 7 (line-parity fix-ups, W43 D6 method; keys untouched) ----------
# P6 bridges: A 2->1 lines, D 3->2 lines (measured with wrap()).
rep([C56], 'e.bridge("Veja os dois gráficos acima e escolha a resposta certa.")',
    'e.bridge("Veja os gráficos e escolha a certa.")', 1)
rep([C56], 'e.bridge("Complete com as palavras do quadro: sondeo · muestra · indecisos · margen de error")',
    'e.bridge("Complete com as palavras: sondeo · muestra · indecisos · margen de error")', 1)
# P7 col3: errs1 2->1, palabra 4->3, disclosure 6->3 lines (restores core
# preview geometry; disclosure keeps all three facts, drops the invitation
# per the W45 ESxEN §3.7 precedent).
rep([C7], '"lunes é singular: o verbo vai no singular (es)."', '"lunes é singular: usa-se es."', 1)
rep([C7], 'precampaña = a pré-campanha: as semanas antes da campanha oficial. Esta edição é pré-campanha; a campanha começa na sexta, dia 13.',
    'precampaña = a pré-campanha: as semanas antes da campanha. A campanha começa sexta, dia 13.', 2)
rep([C7], 'ldcn = "Nota da redação: até o fecho desta edição não chegaram cartas reais de leitores nem os melhores textos da página 8; publicamos esta carta de exemplo e a promessa passa para o VOL.3. Escreva-nos!"',
    'ldcn = "Nota da redação: ao fecho, sem cartas reais nem textos da pág. 8; sai este exemplo. Promessa: VOL.3."', 1)
# P8 answer-note shortenings: each verified 1 line with wrap() at 13.5pt
# serif in 434px (the full "N. key — note" string). #137/#138 deliberately
# NOT shortened: their PT keys are full sentences and wrap to 2 lines,
# the accepted W43 ESxPT exception (same +1-line absorption).
rep([C12], '"o Dia de Todos os Santos caiu num domingo, 1 de novembro"', '"Todos os Santos: domingo, 1 de novembro"', 1)
rep([C34, C8], '"os atos de memória da DANA foram na quinta, 29 de outubro"', '"atos da DANA: quinta, 29 de outubro"', 2)
rep([C34], '"na Castanyada comem-se castanhas assadas, boniatos e panellets"', '"Castanyada: castanhas, boniatos e panellets"', 1)
rep([C34], '"o Samaín é uma festa antiga galega, não o nome galego do Halloween"', '"Samaín: festa antiga galega, não Halloween"', 1)
rep([C34], '"o Dia de Todos os Santos é 1 de novembro, não 31 de outubro"', '"Todos os Santos: 1 de novembro, não 31 de outubro"', 1)
rep([C34], '"no domingo, as famílias levaram flores aos cemitérios"', '"no domingo, flores aos cemitérios"', 1)
rep([C34], '"a memória da DANA é dos dois anos da tempestade de 2024"', '"DANA 2024: dois anos depois"', 1)
rep([C34], '"depois das três noites, na segunda uns fazem ponte e outros trabalham"', '"na segunda, uns fazem ponte e outros trabalham"', 1)
rep([C34], '"o verbo em segundo lugar"', '"verbo em 2.º lugar"', 1)
rep([C34], '"o tempo primeiro, o verbo em segundo"', '"tempo 1.º, verbo 2.º"', 1)
rep([C34], '"o lugar primeiro, o verbo em segundo"', '"lugar em 1.º, verbo em 2.º"', 1)
rep([C34], '"pergunta indireta com si"', '"pergunta indireta: si"', 1)
rep([C34], '"na terça, três jogos da Champions com equipas espanholas"', '"terça: três jogos da Champions"', 1)
rep([C34], '"más + importante (o Atlético–Barça é mais importante)"', '"más + importante (o Atlético–Barça)"', 1)
rep([C56], '"o primeiro jogo da NFL no Bernabéu foi em 16 de novembro de 2025"', '"primeiro jogo no Bernabéu: 16 de novembro de 2025"', 1)
rep([C56], '"o futebol americano joga-se com as mãos, em quatro tentativas"', '"futebol americano: mãos, quatro tentativas"', 1)
rep([C56], '"o jogo da NFL em Madrid é o segundo no Bernabéu"', '"segundo jogo da NFL no Bernabéu"', 1)
rep([C56], '"o hino dos EUA é cantado por Momsen, não por Sáinz-Villegas"', '"hino dos EUA: Momsen, não Sáinz-Villegas"', 1)
rep([C56], '"no dia 2 de outubro, o parlamento rejeitou dois decretos de habitação"', '"2 de outubro: dois decretos rejeitados"', 1)
rep([C56], '"no dia 5 de outubro, dissolveram-se as Cortes e convocaram-se eleições"', '"5 de outubro: Cortes dissolvidas, eleições marcadas"', 1)
rep([C8], '"Ana só vê a NFL; quem vê o Atlético–Barça à noite é o Pablo"', '"Ana: só a NFL; Pablo: Atlético–Barça à noite"', 1)
rep([C8], '"o tempo primeiro"', '"tempo em 1.º"', 1)
rep([C8], '"a las nueve = às nove horas"', '"a las nueve = às 9h"', 1)
rep([C8], '"a palavra interrogativa no início"', '"interrogativa no início"', 1)
print('PART 7 OK')
