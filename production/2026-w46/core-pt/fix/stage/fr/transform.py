# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x FR fan-out transform for W46 VOL.3.

Run inside the already-copied build dir. Every replacement is an exact
literal match (longest strings first); missing literals warn, and the
final pass asserts ZERO CJK chars remain in the build sources.
Frozen Portuguese text, the P7 example letter (lt), the PT disclosure
(disc_pt) and the P7 quote strings + page tags are never touched.
P1 subtitle (330) and badge (372) lines are replaced whole (size/color).
Subtitle size 35pt is measured (40pt overflows the page frame).
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
        t = t.replace('weekly-report-w46-pt-core', 'weekly-report-w46-pt-fr')
        save(fn, t)
t = load('render.py')
t = sub(t, 'A-Lucerna-VOL3.pdf', 'A-Lucerna-VOL3-FR.pdf', 'render.py')
save('render.py', t)

# ---------- 1. bslib4 furniture ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.3 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · HEBDOMADAIRE PORTUGAIS VOL.3 · TEXTE EN PORTUGAIS · EXPLICATIONS EN FRANÇAIS', 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} sur {total}"', 'bslib4.py')
t = sub(t, '("译注｜" + s', '("Note — " + s', 'bslib4.py')
save('bslib4.py', t)

# ---------- 2. P1 masthead lines (whole-line) ----------
t = load('content12.py')
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "JOURNAL PORTUGAIS · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE", 35, "serif", True, INK, anchor="middle")',
    'content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "TEXTES EN PORTUGAIS · EXPLICATIONS EN FRANÇAIS — L\u2019ÉDITION POUR LES LECTEURS FRANCOPHONES", 19, "sans", True, BRICK, anchor="middle")',
    'content12.py')
save('content12.py', t)

# ---------- 3. type / instr labels ----------
INSTR = [
    ('instr="造句"', 'instr="Forme une phrase"'),
    ('instr="翻译"', 'instr="Traduis"'),
    ('instr="判断"', 'instr="Vrai ou faux ?"'),
    ('instr="写作"', 'instr="Écris"'),
    ('instr="填空"', 'instr="Complète"'),
    ('instr="把词和释义配对"', 'instr="Associe les mots"'),
]
TYP = [
    ('"完成句子"', '"Compléter la phrase"'),
    ('"词汇配对"', '"Associer le vocabulaire"'),
    ('"判断对错"', '"Vrai ou faux"'),
    ('"完形单选"', '"Texte à trous"'),
    ('"单选"', '"Choix multiple"'),
    ('"造句"', '"Former une phrase"'),
    ('"翻译"', '"Traduction"'),
    ('"写作"', '"Écriture"'),
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
    ('NÍVEL A2 · Prova e feriado no mesmo domingo', 'NIVEAU A2 · Examen et jour férié le même dimanche'),
    ('A2 → B1 · Proclamação da República: 137 anos · 共和国宣言 137 周年', 'A2 → B1 · Proclamação da República : 137 ans'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'NIVEAU B1 · La semaine du football'),
    ('NÍVEL B1 · A última semana dos jovens · 最后一周：年轻人的冲刺', 'NIVEAU B1 · La dernière semaine des jeunes'),
    ('NÍVEL B2 · O segundo domingo explicado · 第二个周日详解', 'NIVEAU B2 · Le deuxième dimanche expliqué'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具', 'Três níveis, três ferramentas · Trois niveaux, trois outils'),
    ('第 8 版 · A grande prova da semana + todas as respostas', 'PAGE 8 · La grande épreuve de la semaine + toutes les réponses'),
    # top strip / kickers
    ('TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语', 'TODA SEMANA EM PORTUGUÊS · LE PORTUGAIS QUE LE BRÉSIL LIT, CHAQUE SEMAINE'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · À LA UNE'),
    ('VIDA · 生活', 'VIDA · LA VIE'),
    ('CULTURA · 文化', 'CULTURA · CULTURE'),
    ('ESPORTE · 体育', 'ESPORTE · SPORT'),
    ('JOVENS · 青年', 'JOVENS · LES JEUNES'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · APPROFONDISSEMENT'),
    ('LÍNGUA · 语言', 'LÍNGUA · LANGUE'),
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · TEST ET RÉPONSES'),
    # P1
    ('高考第二天', 'ENEM, JOUR 2'),
    ('11 月 15 日第二场考试 · 共和国宣言日假期', '15 nov. : deuxième jour d\u2019examen · jour férié de la Proclamation de la République'),
    ('讲解｜a proclamação 宣布、宣告 · o feriado 假日 · a natureza 自然科学 · a matemática 数学。', 'Mots-clés | a proclamação = proclamation · o feriado = jour férié · a natureza = sciences de la nature · a matemática = mathématiques.'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · EN CHIFFRES'),
    ('12h — os portões abrem no domingo 15（周日 12 点开门）', '12h — os portões abrem no domingo 15 (dimanche : ouverture à 12h)'),
    ('13h — os portões fecham（13 点关门，过时不入）', '13h — os portões fecham (13h : fermeture, les retardataires restent dehors)'),
    ('13h30–18h30 — a prova do dia 15（考试 13:30 至 18:30）', '13h30–18h30 — a prova do dia 15 (l\u2019épreuve du 15, de 13h30 à 18h30)'),
    ('90 — as questões do dia 15: 45 + 45（90 道题：45 + 45）', '90 — as questões do dia 15: 45 + 45 (90 questions : 45 + 45)'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · À TOI DE JOUER'),
    ('proclamação = 宣布（共和国宣言）', 'proclamação = proclamation (de la République)'),
    ('proclamação = 宣布（共和国宣言）。', 'proclamação = proclamation (de la République).'),
    ('feriado = 假日', 'feriado = jour férié'),
    ('portões = 大门（考场大门）', 'portões = les grilles (du centre d\u2019examen)'),
    ('18h30 结束', 'fin à 18h30'),
    ('90 道题', '90 questions'),
    ('fazer 现在时 eles 形式：fazem', 'fazer, présent, forme eles : fazem'),
    ('迟到不得入内：13 点后关门', 'Après 13h, on n\u2019entre plus.'),
    # .text.md variant of the line above: the export source carries a trailing 。 which the bare entry leaves behind (F-2).
    ('迟到不得入内：13 点后关门。', 'Après 13h, on n\u2019entre plus.'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · SOMMAIRE'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · EN BREF'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · QUIZ ÉCLAIR'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Lis la une et choisis · Réponses page 8'),
    ('共和国宣言日在 11 月 15 日', 'La Proclamation de la République, c\u2019est le 15 novembre'),
    ('13 点关门', 'Fermeture à 13h'),
    ('第 2 天考自然科学与数学', 'Jour 2 : sciences de la nature et mathématiques'),
    ('18:30 结束', 'Fin à 18h30'),
    # P2
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · LE TRUC'),
    ('a proclamação 宣布 · o feriado 假日 · a natureza 自然科学 · a matemática 数学 · conferir 核对 · a escala 排班。', 'a proclamação = proclamation · o feriado = jour férié · a natureza = sciences de la nature · a matemática = mathématiques · conferir = vérifier · a escala = le planning.'),
    ('在你的国家，落在周日的假日会在周一补休吗？写两句寄来。', 'Dans ton pays, un jour férié qui tombe un dimanche est-il récupéré le lundi ? Écris deux phrases et envoie-les-nous.'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · ET TOI ?'),
    ('OS HORÁRIOS DO DOMINGO 15 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 15 · LES HORAIRES DU DIMANCHE 15'),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · Un pays, plusieurs fuseaux'),
    ('周日 12 点开门', 'Ouverture le dimanche à 12h'),
    ('13:30 开考', 'Début de l\u2019épreuve à 13h30'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · EXERCICES PAGE 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Réponses page 8 · Niveaux mélangés — cherche par numéro'),
    ('读第 2 版文章，选出正确答案。', 'Lis la page 2 et choisis la bonne réponse.'),
    ('假日落在周日，周一不补休', 'Le jour férié tombe un dimanche, pas de récupération le lundi'),
    # P7-clinic/.text.md variant of the line above: the source carries a trailing 。 (F-2/F-3).
    ('假日落在周日，周一不补休。', 'Le jour férié tombe un dimanche, pas de récupération le lundi.'),
    ('确认卡显示考试地点', 'La carte de confirmation indique le lieu d\u2019examen'),
    ('巴西没有夏令时，钟表不动', 'Le Brésil n\u2019a pas d\u2019heure d\u2019été : les horloges ne bougent pas'),
    ('补全动词的现在时形式。', 'Complète avec la forme au présent du verbe.'),
    ('用第 1、2 版的数字填空。', 'Complète avec les chiffres des pages 1 et 2.'),
    ('12 点到 13 点 = 1 小时', 'De 12h à 13h = 1 heure'),
    ('13:30 至 18:30 = 5 小时', 'De 13h30 à 18h30 = 5 heures'),
    ('5×60 = 300 分钟', '5×60 = 300 minutes'),
    ('proclamação=宣布一个变化 b', 'proclamação = annoncer un changement (b)'),
    ('feriado=法律规定的休息日 c', 'feriado = un jour de repos fixé par la loi (c)'),
    ('natureza=生命、物理与化学的科学 d', 'natureza = la science du vivant, de la physique et de la chimie (d)'),
    ('matemática=数字与图形的科学 a', 'matemática = la science des nombres et des figures (a)'),
    ('把词和释义配对', 'Associe les mots et les définitions'),
]
REPL += [
    # P3
    ('a monarquia 君主制 · a república 共和国 · o marechal 元帅 · o exílio 流亡 · o governo 政府 · a lei 法律。', 'a monarquia = monarchie · a república = république · o marechal = maréchal · o exílio = exil · o governo = gouvernement · a lei = loi.'),
    ('在你的国家，有纪念共和国建立的假日吗？写两句寄来。', 'Dans ton pays, y a-t-il un jour férié pour la fondation de la République ? Écris deux phrases et envoie-les-nous.'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · EXERCICES PAGE 3'),
    ('读第 3 版文章，选出正确答案。', 'Lis la page 3 et choisis la bonne réponse.'),
    ('共和国宣言在 1889 年 11 月 15 日', 'La Proclamation de la République a eu lieu le 15 novembre 1889'),
    ('德奥多罗成为巴西第一任总统', 'Deodoro est devenu le premier président du Brésil'),
    ('全国性假日，任何城市都不能改为工作日', 'Un jour férié national, qu\u2019aucune ville ne peut transformer en jour de travail'),
    ('2026 年假日落在周日', 'En 2026, le jour férié tombe un dimanche'),
    ('共和国里总统由选举产生、任期有限', 'En république, le président est élu et le pouvoir est limité dans le temps'),
    ('用方框里的词填空。', 'Complète avec les mots de l\u2019encadré.'),
    ('monarquia = 君主制', 'monarquia = monarchie'),
    ('república = 共和国', 'república = république'),
    ('marechal = 元帅', 'marechal = maréchal'),
    ('exílio = 流亡', 'exílio = exil'),
    ('governo = 政府', 'governo = gouvernement'),
    ('lei = 法律', 'lei = loi'),
    ('用过去时（pretérito perfeito）补全。', 'Complète au passé (pretérito perfeito).'),
    ('tomar 过去时 elas 形式：tomaram', 'tomar, passé, forme elas : tomaram'),
    ('acabar 过去时 ela 形式：acabou', 'acabar, passé, forme ela : acabou'),
    ('ser 过去时 ele 形式：foi', 'ser, passé, forme ele : foi'),
    ('assumir 过去时 ele 形式：assumiu', 'assumir, passé, forme ele : assumiu'),
    ('把词组成正确的句子。', 'Mets les mots dans le bon ordre.'),
    ('主语 + é + 表语', 'Sujet + é + attribut'),
    ('主语 + 动词 + 表语', 'Sujet + verbe + attribut'),
    ('主语 + 动词 + 宾语 + 时间', 'Sujet + verbe + objet + temps'),
    # P4
    ('a ida 首回合 · a volta 次回合 · o gol 进球 · o pênalti 点球 · a pausa 休整期 · o amistoso 友谊赛。', 'a ida = le match aller · a volta = le match retour · o gol = le but · o pênalti = le penalty · a pausa = la pause · o amistoso = le match amical.'),
    ('你在巴西杯支持哪支球队？谁能进决赛？写两句寄来。', 'Quelle équipe soutiens-tu en Copa do Brasil — et qui ira en finale ? Écris deux phrases et envoie-les-nous.'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · LA SEMAINE FOOT'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · EXERCICES PAGE 4'),
    ('读第 4 版文章，选出正确答案。', 'Lis la page 4 et choisis la bonne réponse.'),
    ('首回合格雷米奥 2 比 0 战胜米内罗竞技', 'À l\u2019aller, Grêmio a battu l\u2019Atlético-MG 2 à 0'),
    ('帕尔梅拉斯 1 比 0 战胜瓦斯科，毛里西奥进球', 'Palmeiras a battu Vasco 1 à 0, but de Maurício'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点', 'Le retour Atlético-MG × Grêmio, c\u2019est samedi 7 à 18h'),
    ('决赛 12 月 6 日单场，在马内·加林查', 'La finale : un seul match, le 6 décembre, au Mané Garrincha'),
    ('第 35 轮本周只有一场：米拉索尔 × 米内罗竞技', 'La 35e journée n\u2019a qu\u2019un match cette semaine : Mirassol × Atlético-MG'),
    ('gol=射入球网的得分 b', 'gol = le point marqué dans le filet (b)'),
    ('ida=对决的第一场 d', 'ida = le premier match d\u2019un duel (d)'),
    ('volta=对决的第二场 a', 'volta = le deuxième match d\u2019un duel (a)'),
    ('pênalti=十一米点的罚球 c', 'pênalti = le tir depuis le point de penalty (c)'),
    ('用括号里正确的比较形式填空。', 'Complète avec la bonne forme comparative entre parenthèses.'),
    ('5 小时 < 5.5 小时：menos', '5 heures < 5,5 heures : menos'),
    ('把句子补全成过去时（pretérito perfeito）。', 'Complète les phrases au passé (pretérito perfeito).'),
    ('vencer 过去时 ele 形式：venceu', 'vencer, passé, forme ele : venceu'),
    ('marcar 过去时 eles 形式：marcaram', 'marcar, passé, forme eles : marcaram'),
    ('marcar 过去时 ele 形式：marcou', 'marcar, passé, forme ele : marcou'),
    ('convocar 过去时 ele 形式：convocou', 'convocar, passé, forme ele : convocou'),
    ('ser 过去时复数：foram', 'ser, passé, pluriel : foram'),
    # P5
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）', '1. Confira o Cartão de Confirmação do Enem (vérifie ta carte de confirmation de l\u2019Enem)'),
    ('2. Revise um pouco por dia: Natureza e Matemática（每天复习一点：自然科学与数学）', '2. Revise um pouco por dia: Natureza e Matemática (révise un peu chaque jour : sciences de la nature et maths)'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）', '3. Durma bem na véspera da prova (dors bien la veille de l\u2019épreuve)'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）', '4. Separe documento e caneta preta no dia anterior (prépare ta pièce d\u2019identité et ton stylo noir la veille)'),
    ('5. Domingo 15: chegue antes das 12h（周日 15 日：12 点前到达）', '5. Domingo 15: chegue antes das 12h (dimanche 15 : arrive avant 12h)'),
    ('a natureza 自然科学 · a matemática 数学 · a maratona 突击马拉松 · a véspera 前夕 · comparar 比较价格 · a cabeça 头脑、状态。', 'a natureza = sciences de la nature · a matemática = mathématiques · a maratona = le marathon de révision · a véspera = la veille · comparar = comparer les prix · a cabeça = la tête, la forme.'),
    ('重要考试前一晚，你是复习到很晚还是早睡？写两句寄来。', 'La veille d\u2019un examen important : tu révises tard ou tu te couches tôt ? Écris deux phrases et envoie-les-nous.'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · EXERCICES PAGE 5'),
    ('读第 5 版文章，选出正确答案。', 'Lis la page 5 et choisis la bonne réponse.'),
    ('最后一周在 11 月 15 日周日结束', 'La dernière semaine se termine dimanche 15 novembre'),
    ('每天复习一点', 'Réviser un peu chaque jour'),
    ('提前一天备好证件和黑笔', 'Préparer sa pièce d\u2019identité et son stylo noir la veille'),
    ('黑五在 11 月 27 日', 'Le Black Friday, c\u2019est le 27 novembre'),
    ('11 月 14 日周六巴西 × 日本 7:15', 'Samedi 14 : Brésil × Japon à 7h15'),
    ('用方框里的词填空。注意：有的词要变成复数。', 'Complète avec les mots de l\u2019encadré. Attention : un mot passe au pluriel.'),
    ('última semana = 最后一周', 'última semana = la dernière semaine'),
    ('inscrito 配合复数：inscritos', 'inscrito s\u2019accorde au pluriel : inscritos'),
    ('véspera = 前夕', 'véspera = la veille'),
    ('maratona = 突击马拉松', 'maratona = le marathon de révision'),
    ('local = 地点', 'local = le lieu'),
    ('separar 祈使式：separe', 'separar, impératif : separe'),
    ('用将来时（futuro do presente）补全。', 'Complète au futur (futuro do presente).'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer, futur, forme eles irrégulière : farão'),
    ('mostrar 将来时：mostrará', 'mostrar, futur : mostrará'),
    ('sair 将来时复数：sairão', 'sair, futur, pluriel : sairão'),
    ('chegar 将来时：chegará', 'chegar, futur : chegará'),
    ('错：考前突击不是好计划，每天复习一点才好', 'Faux : bachoter la veille n\u2019est pas un bon plan — un peu chaque jour, c\u2019est mieux'),
    ('对：13:30 至 18:30', 'Vrai : de 13h30 à 18h30'),
    # P6
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。', 'os portões = les grilles · a segunda chamada = une deuxième session, un deuxième accès · conferir = vérifier · a correria = la précipitation.'),
    ('O DOMINGO 15 EM NÚMEROS · 11 月 15 日的数字 (horários oficiais do Inep)', 'O DOMINGO 15 EM NÚMEROS · LES CHIFFRES DU 15 NOVEMBRE (horaires officiels de l\u2019Inep)'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · EXERCICES PAGE 6'),
    ('看上面两张图，选出正确答案。', 'Regarde les deux graphiques ci-dessus et choisis la bonne réponse.'),
    ('大门开放 60 分钟', 'Les grilles restent ouvertes 60 minutes'),
    ('关门到开考之间等 30 分钟', 'L\u2019attente entre la fermeture et l\u2019épreuve est de 30 minutes'),
    ('考试 300 分钟', 'L\u2019épreuve dure 300 minutes'),
    ('中午到 18:30 = 6 个半小时', 'De midi à 18h30 = six heures et demie'),
    ('图表数字是 Inep 官方时间', 'Les chiffres du graphique sont les horaires officiels de l\u2019Inep'),
    ('高考分 8 日和 15 日两个周日', 'L\u2019Enem se joue sur deux dimanches : le 8 et le 15'),
    ('13 点后到场不得入内', 'Après 13h, on n\u2019entre plus'),
    ('根据句子意思，补全正确的动词形式。', 'Complète avec la bonne forme verbale pour chaque phrase.'),
    ('将来时：começará', 'Futur : começará'),
    ('quem + 虚拟式将来：chegar', 'quem + futur du subjonctif : chegar'),
    ('现在时：fecham', 'Présent : fecham'),
    ('现在时：pede', 'Présent : pede'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir', 'Complète avec les mots de l\u2019encadré : portões · segunda chamada · local · conferir'),
    ('portões = 大门', 'portões = les grilles'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = une deuxième session, un deuxième accès'),
    ('祈使式：confira', 'Impératif : confira'),
    # P7
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro', 'Questions : que horas (à quelle heure) + verbe ; onde fica demande où se trouve un lieu ; conferir est irrégulier à la forme eu : confiro.'),
    ('conferir：eu → confiro（不规则）', 'conferir : eu → confiro (irrégulier)'),
    ('onde 问地点', 'onde demande le lieu'),
    ('讲一周的事用过去时（pretérito perfeito）；vencer 规则（venceu）；marcar/chegar/dormir 的过去时注意重音。', 'Pour raconter la semaine, on utilise le passé (pretérito perfeito) ; vencer est régulier (venceu) ; attention à l\u2019accent au passé de marcar, chegar et dormir.'),
    ('vencer 过去时：venceu', 'vencer, passé : venceu'),
    ('marcar 过去时：marcou', 'marcar, passé : marcou'),
    ('chegar 过去时：chegou', 'chegar, passé : chegou'),
    ('venceram 是 vencer 的过去时复数', 'venceram est le passé, pluriel, de vencer'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。', 'Après quando, se et quem, le futur du subjonctif : tiver, for, chegar — la grammaire des hypothèses du dimanche.'),
    ('quem + 虚拟式将来：tiver', 'quem + futur du subjonctif : tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + futur du subjonctif : chegar'),
    ('se + ser 的虚拟式将来：for', 'se + futur du subjonctif de ser : for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + futur → futur du subjonctif for'),
    ('高考用黑笔，蓝笔不行。', 'Stylo noir seulement — le bleu ne passe pas.'),
    ('13 点关门，13:30 到就晚了。', 'Fermeture à 13h — 13h30, c\u2019est trop tard.'),
    ('15 日考试 18:30 结束，19 点是 8 日的时间。', 'Le 15, l\u2019épreuve finit à 18h30 ; 19h, c\u2019est pour le 8.'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · ERREURS'),
    ('proclamação = 宣布；1889 年君主制结束、共和国开始。', 'proclamação = proclamation ; en 1889, la monarchie s\u2019achève et la République commence.'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · LE MOT'),
    ('编辑部说明：上期（VOL.2）承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期（VOL.4）。', 'Note de la rédaction : ni lettres ni meilleurs textes du VOL.2 avant le bouclage — l\u2019exemple reste, la promesse passe au VOL.4.'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！', 'Exemple de la rédaction — pas une vraie lettre.'),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）', 'FRASES DA SEMANA · PHRASES DE LA SEMAINE (citées mot à mot dans ce numéro)'),
    ('两个周日、一个假日：巴西迎来高考第二天。', 'Deux dimanches, un jour férié : le Brésil passe le deuxième jour de l\u2019Enem.'),
    ('考试和假日在同一天到来。', 'L\u2019examen et le jour férié arrivent le même jour.'),
    ('假日不改变时钟。', 'Le jour férié ne change pas l\u2019horloge.'),
    ('君主制结束了。', 'La monarchie est finie.'),
    ('谁能进巴西杯决赛？', 'Qui ira en finale de la Copa do Brasil ?'),
    ('睡得好，记得牢。', 'Bien dormir, mieux se souvenir.'),
    ('先做容易的，再做难的。', 'D\u2019abord les faciles, puis les difficiles.'),
    ('核对确认卡、睡好、早到。', 'Vérifie ta carte, dors bien, arrive tôt.'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.4)', 'A PRÓXIMA SEMANA · LA SEMAINE PROCHAINE (VOL.4)'),
    # P8
    ('第 2 天在 11 月 15 日', 'Le jour 2, c\u2019est le 15 novembre'),
    ('第 1 天在 11 月 8 日', 'Le jour 1, c\u2019est le 8 novembre'),
    ('确认卡是高考的文件', 'La carte de confirmation appartient à l\u2019Enem'),
    ('共和国宣言日在 11 月 15 日', 'La Proclamation de la République, c\u2019est le 15 novembre'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', 'Le retour Vasco × Palmeiras, c\u2019est le 8'),
    ('第二天共 90 道题', 'Le jour 2 compte 90 questions en tout'),
    ('考试时长 5 小时', 'L\u2019épreuve dure 5 heures'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场', 'Le retour Atlético-MG × Grêmio se joue à l\u2019Arena MRV'),
    ('第 35 轮本周只有一场，在 14 日', 'La 35e journée n\u2019a qu\u2019un match cette semaine, le 14'),
    ('共和国宣言在 1889 年', 'La Proclamation de la République date de 1889'),
    ('11.11 是促销日', 'Le 11.11, c\u2019est le jour des promos'),
    ('300 是考试的分钟数', '300, c\u2019est la durée de l\u2019épreuve en minutes'),
    ('德奥多罗是第一任总统', 'Deodoro a été le premier président'),
    ('玛丽娜住在圣保罗', 'Marina habite à São Paulo'),
    ('她每天复习一点自然科学', 'Elle révise un peu de sciences de la nature chaque jour'),
    ('前一晚她备好证件和黑笔、早睡', 'La veille, elle prépare sa pièce d\u2019identité et son stylo noir et se couche tôt'),
    ('她 11:30 到达考场', 'Elle arrive au centre d\u2019examen à 11h30'),
    ('时间词在前', 'Le mot de temps est en tête'),
    ('主语 + 动词 + 宾语 + 地点', 'Sujet + verbe + objet + lieu'),
    ('疑问词组在句首', 'La phrase interrogative est en tête'),
    ('主语 + 动词 + 宾语', 'Sujet + verbe + objet'),
    ('11 月 15 日周日是高考的第二天。', 'Dimanche 15 novembre, c\u2019est le deuxième jour de l\u2019Enem.'),
    ('对照第 6 版标题', 'Voir le titre de la page 6'),
    ('周日前核对确认卡。', 'Vérifie la carte avant dimanche.'),
    ('Confira = 请核对', 'Confira = vérifie'),
    ('“假日落在周日。” → ___', '« Le jour férié tombe un dimanche. » → ___'),
    ('虚拟式将来 chegar + 祈使 apresente', 'Futur du subjonctif chegar + impératif apresente'),
    ('你到达时，请出示带照片的证件。 → ___', 'Quand tu arrives, montre ta pièce d\u2019identité avec photo. → ___'),
    ('proclamação=宣布一个变化 b', 'proclamação = annoncer un changement (b)'),
    ('portão=考场入口 d', 'portão = l\u2019entrée du centre d\u2019examen (d)'),
    ('república=1889 年后的国家形式 a', 'república = la forme d\u2019État après 1889 (a)'),
    ('segunda chamada=关门后的再入场（高考没有） c', 'segunda chamada = réadmission après fermeture (n\u2019existe pas à l\u2019Enem) (c)'),
    ('documento com foto 带照片的证件', 'documento com foto = pièce d\u2019identité avec photo'),
    ('seção = 考场分区（房间）', 'seção = la salle d\u2019examen (le secteur)'),
    ('大门 13 点关闭', 'Fermeture des grilles à 13h'),
    ('考试 18:30 结束', 'L\u2019épreuve finit à 18h30'),
    ('obrigado = 谢谢', 'obrigado = merci'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。', 'Exercice d\u2019écriture (pas de réponse unique) ; le texte modèle ({NWORDS} mots) est ci-dessous.'),
    ('（开放题，范文如下）', '(exercice ouvert — texte modèle ci-dessous)'),
    ('范文见本版 H 区（{NWORDS} 词）', 'Voir le texte modèle dans la partie H de cette page ({NWORDS} mots)'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可', 'RESPOSTAS · RÉPONSES — classées par page ; trouve ton numéro'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', 'Une courte note par réponse · ✓ = l\u2019exercice d\u2019écriture'),
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

# ---------- 5. disclosure rename + layout tweaks (EN/DE precedent) ----------
t = load('content7.py')
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_fr')
old_wh = 'len(wrap("proclamação = proclamation ; en 1889, la monarchie s’achève et la République commence.", "sans", False, 20, CW - 44)) * 29 + 20'
assert t.count(old_wh) == 1, 'word-box pad line not found'
t = t.replace(old_wh, 'len(wrap("proclamação = proclamation ; en 1889, la monarchie s’achève et la République commence.", "sans", False, 20, CW - 44)) * 29 + 30')
assert t.count(')) * 29 + 35') == 1, 'letters-box pad line not found'
t = t.replace(')) * 29 + 35', ')) * 29 + 22')
t = line_replace(t, 'fy = max(1712,', 'fy = max(1712, ly + lh + 6)', 'content7.py')
t = line_replace(t, 'cyq = fy + 66', '    cyq = fy + 66 + (i % 4) * 86', 'content7.py')
save('content7.py', t)

t = load('content8.py')
t = line_replace(t, 'af.para(txt, 13.5',
    '        af.para(txt, 13, lh=1.12, gap=0.5, split=False)',
    'content8.py')
save('content8.py', t)

t = load('content12.py')
old_box = '    ("90 — as questões do dia 15: 45 + 45 (90 questions : 45 + 45)", "serif", False, INK, 20, 1.35),\n])'
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
