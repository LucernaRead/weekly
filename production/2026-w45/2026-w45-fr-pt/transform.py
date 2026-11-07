# -*- coding: utf-8 -*-
"""FR x PT fan-out transform for W45 FR core build copy (VOL.3).

Rules (tools/README #17/#18): whole-string or exact-unique-literal
replacements with count assertions; value maps use bare text, never repr.
French target text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token, except the documented re-aimed P8 translation items
(E1 key/note/stem, E2-E5 stems) and the P8 printing rule (see below).
Within each file, replacements run longest-old-first so a short token
(e.g. 配对, 填空, 完成句子) never corrupts a longer string containing it.

Furniture follows the SHIPPED W43 FR x PT edition
(files/weekly-report-fr-pt/), which wins over any generic rule:
badge INSERTED at y=574, 22pt BRICK, centred, PT form;
footer VOL.3 in the canonical PT template; gloss prefix "Nota — ";
short bilingual heads; LES MOTS box titles take "PALAVRAS" (W43
deviation: VOCABULÁRIO overflows the right-column boxes), while the
P6 LES MOTS flow head and the P8 F head keep VOCABULÁRIO (W43: fits).
Toolbox head takes "PARA LEVAR" (W43 deviation: FERRAMENTAS too wide).

P8 printed-note set: the core's rule (page 8 always, or note <= 10 chars,
or clinic/chart types) cannot survive translation, because Portuguese
notes are longer. Following the W43 FR x PT precedent, the edition
carries the core's printed set EXPLICITLY (PRINT_NOTES, measured from
the core P8 with tools/p8.py extract --json: 97 numbers) so the same
exercises carry printed notes in both editions. Bare keys (53) untouched.
Run once from the build dir copy. Idempotent? No — run once only.
"""
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
        assert n >= 1, f"{fname}: {old!r} not found in {fname}"
    LOG.append(f"{fname}: {n}x {old!r} -> {new!r}")
    open(p, "w", encoding="utf-8").write(s.replace(old, new))


def rep_all(fname, pairs):
    # longest old first: avoids a short literal corrupting a longer one
    # that contains it (e.g. a note inside a longer note string).
    for old, new in sorted(pairs, key=lambda t: -len(t[0])):
        rep(fname, old, new)


# ---------- OUT repoint (1 per content file) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w45-fr-core", "weekly-report-w45-fr-pt", 1)

# ---------- bslib4: furniture + gloss prefix (W43 shipped forms, VOL.3) ----------
rep("bslib4.py",
    '"Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文"',
    '"Le Lucerna · SEMANÁRIO FRANCÊS VOL.3 · TEXTOS EM FRANCÊS · EXPLICAÇÕES EM PORTUGUÊS"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Nota — " + s', 1)

# ---------- content8 P8 code edits FIRST (before string rep_all, so the
# rule line's type tokens are not touched by the string pass) ----------
rep("content8.py",
    '    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
    '    kf.para(f"— Página {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py",
    '        if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):\n            s += f"（{e[\'note\']}）"',
    '        if e["note"] and e["n"] in PRINT_NOTES:\n            s += f" ({e[\'note\']})"', 1)
rep("content8.py",
    'kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")',
    'PRINT_NOTES = [1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]\nkf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")', 1)

# ---------- content12: P1 + P2 ----------
rep_all("content12.py", [
    ("HEBDOMADAIRE EN FRANÇAIS · 每周一期 · 读法国人正在读的法语",
     "HEBDOMADAIRE EN FRANÇAIS · TODA SEMANA · O FRANCÊS QUE OS FRANCESES LEEM"),
    ("法语正文 · 简体中文讲解 — 给简体中文读者的版本",
     "TEXTOS EM FRANCÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA"),
    ("SPORT · CULTURE · GASTRONOMIE · LA UNE · 决赛周末",
     "SPORT · CULTURE · GASTRONOMIE · LA UNE · FIM DE SEMANA DECISIVO"),
    ("se jouer 决出胜负、上演 · une finale 决赛 · une demi-finale 半决赛 · un quart de finale 四分之一决赛 · une nocturne 夜场活动 · un frisson 战栗、刺激感 · la coquille Saint-Jacques 扇贝。",
     "se jouer decidir o resultado, acontecer · une finale final · une demi-finale meia-final · un quart de finale quarto de final · une nocturne evento noturno · un frisson arrepio, emoção · la coquille Saint-Jacques vieira."),
    ("LES DATES · 决赛周末日程", "LES DATES · FIM DE SEMANA DECISIVO"),
    ("法 语 周 报 · VOL.3 · 决 赛 周 末", "SEMANÁRIO EM FRANCÊS · VOL.3 · FIM DE SEMANA DECISIVO"),
    ("VOL. 3 · 总第 3 期", "VOL. 3 · Nº 3"),
    ("周一开学 · 全法同步复课", "SEGUNDA, VOLTA ÀS AULAS · EM TODA A FRANÇA"),
    ("大师赛开赛 · 音乐节开幕 · 详见第 2 版", "COMEÇO DO MASTERS · ABERTURA DO FESTIVAL · VER PÁGINA 2"),
    ("À VOUS ! · 即学即练", "À VOUS ! · A VOSSA VEZ"),
    ("周日 8 日举行决赛", "A final é no domingo, dia 8"),
    ("周六 7 日晚是最后夜场", "A última noite é no sábado, dia 7"),
    ("波尔诺曼底卖扇贝", "Em Port-en-Bessin vendem-se vieiras"),
    ("周一 2 日全法复课", "A volta às aulas é na segunda, dia 2, em toda a França"),
    ("半决赛后才知道决赛选手", "Os finalistas só serão conhecidos após as meias-finais"),
    ("三个决赛：网球、刺激、美味", "Três finais: ténis, emoção, sabores"),
    ("本周日程 · 11 月 2 日至 8 日", "Agenda da semana · 2 a 8 de novembro"),
    ("周末决赛结果周六晚、周日揭晓。", "Os resultados do fim de semana final serão conhecidos no sábado à noite e no domingo."),
    ("DANS CE NUMÉRO · 本期目录", "DANS CE NUMÉRO · NESTE NÚMERO"),
    ("决出胜负；上演。本周末一切都将见分晓。", "Decidir o resultado; acontecer. Neste fim de semana, tudo se decide."),
    ("EN BREF · 快讯", "EN BREF · EM RESUMO"),
    ("QUIZ ÉCLAIR · 闪电问答", "QUIZ ÉCLAIR · QUIZ RELÂMPAGO"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Leiam a primeira página e escolham a resposta certa · respostas na página 8"),
    ("决赛在周日 8 日", "A final é no domingo, dia 8"),
    ("扇贝节在滨海波尔", "A festa da vieira é em Port-en-Bessin"),
    ("周一 2 日早上全区复课", "A volta às aulas é na segunda, dia 2, de manhã, em todas as zonas"),
    ("最后夜场周六 7 日", "A última noite é no sábado, dia 7"),
    ("VIE QUOTIDIENNE · 生活", "VIE QUOTIDIENNE · VIDA QUOTIDIANA"),
    ("NIVEAU A2 · La rentrée · 开学复课", "NIVEAU A2 · La rentrée · VOLTA ÀS AULAS"),
    ("la rentrée 开学、复课 · reprendre 重新开始、复课 · un cartable 书包 · un décalage 错开、时差 · en revanche 相反、反之 · un rituel 习惯、仪式。",
     "la rentrée volta às aulas · reprendre recomeçar, voltar às aulas · un cartable mochila · un décalage desfasamento, diferença de horário · en revanche pelo contrário · un rituel hábito, ritual."),
    ("译注｜une valise 行李箱 · une ambiance 气氛 · le bilan 总结、盘点。",
     "Nota — une valise mala · une ambiance ambiente · le bilan balanço, resumo."),
    ("说说你的开学：周一早上你在哪里？假期读了哪本书？写两句法语寄给编辑部。",
     "Contem-nos a vossa volta às aulas: onde estavam na segunda de manhã? Que livro leram nas férias? Escrevam duas frases em francês para a redação."),
    ("ET VOUS ? · 说说你自己", "ET VOUS ? · E VOCÊS?"),
    ("DIRE LA DATE · 这样说日期", "DIRE LA DATE · COMO DIZER A DATA"),
    ("lundi 2 novembre · 注意：1 日说 le premier，其余用基数词",
     "lundi 2 novembre · atenção: no dia 1 diz-se le premier; nos outros, o número cardinal"),
    ("11 月 2 日星期一 · la rentrée", "2 de novembro, segunda-feira · la rentrée"),
    ("11 月 3 日星期二 · votes à l'Assemblée", "3 de novembro, terça-feira · votes à l'Assemblée"),
    ("11 月 4 日星期三 · sorties cinéma", "4 de novembro, quarta-feira · sorties cinéma"),
    ("11 月 7 日星期六 · nocturne et demis", "7 de novembro, sábado · nocturne et demis"),
    ("11 月 8 日星期日 · les finales", "8 de novembro, domingo · les finales"),
    ("EXERCICES · 第 2 版练习", "EXERCICES · EXERCÍCIOS DA PÁGINA 2"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案", "Respostas na página 8 · os exercícios podem misturar níveis; procurem pelo número"),
    ("用法语补全日期（注意星期与数字）。", "Completem as datas em francês (atenção ao dia da semana e ao número)."),
    ("用 aller + 动词原形改写（最近将来时）。", "Reescrevam com aller + infinitivo (futuro próximo)."),
    ("读第 2 版文章，选出正确答案。", "Leiam o artigo da página 2 e escolham a resposta certa."),
    ("三区同一周一早上复课", "As três zonas voltam na mesma segunda de manhã"),
    ("冬令时从 10 月 25 日开始", "O horário de inverno começou a 25 de outubro"),
    ("11 月晚上天黑得早", "Em novembro, à noite, escurece cedo"),
    ("复课在星期一", "A volta às aulas é na segunda-feira"),
    ("11 月 1 日说 le premier", "No dia 1 de novembro diz-se le premier"),
    ("最后夜场在星期六", "A última noite é no sábado"),
    ("决赛在星期日", "A final é no domingo"),
    ("rentrée=开学 a", "rentrée=volta às aulas a"),
    ("reprendre=重新开始 b", "reprendre=recomeçar b"),
    ("cartable=书包 c", "cartable=mochila c"),
    ("rituel=习惯 d", "rituel=hábito d"),
    ("把词和释义配对", "Associar"),
    ("完成句子", "Completar frases"),
    ("句型转换", "Transformação"),
    ("词汇配对", "Associação"),
    ("单选", "Escolha múltipla"),
    ("填空", "Preencher"),
    ("改写", "Reescrever"),
])
print(f"content12 done, {len(LOG)} replacements so far")

# ---------- content34: P3 + P4 ----------
rep_all("content34.py", [
    ("NIVEAU A2 → B1 · Halloween, Toussaint · 万圣与诸圣",
     "NIVEAU A2 → B1 · Halloween, Toussaint · HALLOWEEN E TODOS OS SANTOS"),
    ("se déguiser 变装、装扮 · un sort 魔法、恶作剧 · une ambiance 气氛 · le souvenir 回忆、纪念 · confondre 混淆 · discret 低调的、安静的。",
     "se déguiser disfarçar-se, fantasiar-se · un sort feitiço, partida · une ambiance ambiente · le souvenir recordação, memória · confondre confundir · discret discreto, calmo."),
    ("À VOUS ! · 即学即练", "À VOUS ! · A VOSSA VEZ"),
    ("判断对错（Vrai / Faux）。", "Verdadeiro ou falso (Vrai / Faux)."),
    ("万圣节在 10 月 31 日星期六", "O Halloween foi no sábado, 31 de outubro"),
    ("诸圣节墓园摆满菊花", "No dia de Todos os Santos, os cemitérios enchem-se de crisântemos"),
    ("菊花绝不能当礼物送人", "Nunca se oferecem crisântemos"),
    ("11 月 2 日是 jour des morts，不是诸圣节", "O dia 2 de novembro é o jour des morts, não a Toussaint"),
    ("文中：le rire d'abord, le souvenir ensuite", "No texto: le rire d'abord, le souvenir ensuite"),
    ("用 déguisement / tombe / citrouille / souvenir 填空。", "Completem com déguisement / tombe / citrouille / souvenir."),
    ("万圣节穿变装服装", "No Halloween, as crianças vestem fantasias"),
    ("花放在墓碑上", "As flores colocam-se sobre a campa"),
    ("南瓜是万圣节的象征", "A abóbora é o símbolo do Halloween"),
    ("诸圣节是纪念之日", "A Toussaint é o dia da recordação"),
    ("改写句子（用 ne...jamais / ne...plus / ne...pas）。", "Reescrevam as frases (com ne...jamais / ne...plus / ne...pas)."),
    ("jamais + de（无冠词变化）", "jamais + de (sem artigo)"),
    ("ne...plus = 不再", "ne...plus = já não"),
    ("n'est pas = 不是", "n'est pas = não é"),
    ("即学即练 · 公园万圣节小题。", "Prática · pequenos exercícios sobre o parque."),
    ("周六 7 日是最后夜场", "O sábado, dia 7, é a última noite"),
    ("敏感儿童有免费驱怪徽章", "As crianças sensíveis recebem um distintivo gratuito contra monstros"),
    ("阿斯泰里克斯公园在 Plailly", "O parque Astérix fica em Plailly"),
    ("Peur sur le Parc 10 月 3 日至 11 月 8 日", "Peur sur le Parc vai de 3 de outubro a 8 de novembro"),
    ("恐惧等级用颜色区分", "A escala do medo usa cores"),
    ("夜场从 19 点到凌晨 1 点", "A noite começa às 19 horas"),
    ("LES MOTS DES FÊTES · 节日词表", "LES MOTS DES FÊTES · PALAVRAS"),
    ("un saint — 圣人", "un saint — santo"),
    ("un cimetière — 墓园", "un cimetière — cemitério"),
    ("une tombe — 坟墓", "une tombe — campa"),
    ("un jour férié — 公共假日", "un jour férié — feriado"),
    ("se souvenir — 纪念、想起", "se souvenir — recordar, lembrar"),
    ("un déguisement — 变装服装", "un déguisement — fantasia"),
    ("une citrouille — 南瓜", "une citrouille — abóbora"),
    ("un bonbon — 糖果", "un bonbon — doce"),
    ("un fantôme — 幽灵", "un fantôme — fantasma"),
    ("un sort — 魔法、诅咒", "un sort — feitiço, maldição"),
    ("10 月 3 日至 11 月 8 日，12 场夜场；最后夜场 11 月 7 日；白天 10 点至 19 点开放。",
     "De 3 de outubro a 8 de novembro, 12 noites; a última noite é a 7 de novembro; de dia, aberto das 10 às 19 horas."),
    ("DATES À RETENIR · 本周日历", "DATES À RETENIR · DATAS DESTA SEMANA"),
    ("注意：迪耶普扇贝集市在 11 月 14–15 日，不在本周。", "Atenção: a feira de Dieppe é a 14–15 de novembro, não esta semana."),
    ("CULTURE · 文化", "CULTURE · CULTURA"),
    ("un tournoi 锦标赛、赛事 · sur dur 硬地球场 · en salle 室内 · un tableau principal 正赛签表 · le tenant du titre 卫冕冠军 · basculer 逆转、倾斜 · les tribunes 看台。",
     "un tournoi torneio, competição · sur dur em piso duro · en salle em recinto coberto · un tableau principal quadro principal · le tenant du titre detentor do título · basculer virar, inclinar · les tribunes bancadas."),
    ("读第 4 版文章，选出正确答案。", "Leiam o artigo da página 4 e escolham a resposta certa."),
    ("大师赛在室内硬地球场举行", "O Masters joga-se em recinto coberto, em piso duro"),
    ("2025 年卫冕冠军是辛纳", "O detentor do título em 2025 é Sinner"),
    ("法甲第十轮大场面：朗斯–马赛", "O grande jogo da 10.ª jornada: Lens – Marseille"),
    ("周日 8 日还有轮椅单打决赛（中午）", "No domingo, dia 8, há também a final em cadeira de rodas (ao meio-dia)"),
    ("把网球词和释义配对。", "Associem as palavras do ténis aos significados."),
    ("tournoi=赛事 a", "tournoi=torneio a"),
    ("raquette=球拍 b", "raquette=raquete b"),
    ("tribunes=看台 c", "tribunes=bancadas c"),
    ("tenant=卫冕者 d", "tenant=detentor do título d"),
    ("用比较级完成句子（plus / moins）。", "Completem as frases com o comparativo (plus / moins)."),
    ("室内球速更快", "Em recinto coberto, a bola vai mais depressa"),
    ("大师赛是仅次于大满贯的级别", "Um Masters 1000 é maior do que um torneio pequeno"),
    ("室内赛季比室外短", "A época em recinto coberto é mais curta que a de verão"),
    ("译注｜un choc 强强对决 · recevoir 迎战、接待 · familier 熟悉的。",
     "Nota — un choc grande jogo · recevoir receber, defrontar · familier familiar."),
    ("« Allez ! » — 加油！ · « Quelle action ! » — 好球！", "« Allez ! » — Força! · « Quelle action ! » — Que jogada!"),
    ("« Il marque ! » — 他得分了！ · « C'est gagné ! » — 赢了！", "« Il marque ! » — Marcou! · « C'est gagné ! » — Ganhámos!"),
    ("« Quel point ! » — 好球！（网球） · « Balle de match ! » — 赛点！", "« Quel point ! » — Que ponto! (ténis) · « Balle de match ! » — Ponto de jogo!"),
    ("LES MOTS DU TENNIS · 网球词表", "LES MOTS DU TENNIS · PALAVRAS"),
    ("le tennis — 网球", "le tennis — ténis"),
    ("une balle — 球", "une balle — bola"),
    ("un set — 一盘", "un set — set"),
    ("un match — 比赛", "un match — jogo"),
    ("un point — 一分", "un point — ponto"),
    ("la finale — 决赛", "la finale — final"),
    ("un adversaire — 对手", "un adversaire — adversário"),
    ("un titre — 冠军头衔", "un titre — título"),
    ("À SUIVRE · 拭目以待", "À SUIVRE · A SEGUIR"),
    ("MICRO-DRILLS · 即学即练", "MICRO-DRILLS · TREINO"),
    ("用 finale / quarts / demi-finales / tableau / fauteuil / choc 填空。", "Completem com finale / quarts / demi-finales / tableau / fauteuil / choc."),
    ("四分之一决赛在周五", "Os quartos de final são na sexta-feira"),
    ("半决赛在周六", "As meias-finais são no sábado"),
    ("单打决赛在周日", "A final de singulares é no domingo"),
    ("正赛签表从周一开始", "O quadro principal começa na segunda-feira"),
    ("轮椅赛事周五至周日", "O torneio em cadeira de rodas é de sexta a domingo"),
    ("朗斯–马赛是周末焦点战", "Lens – Marseille é o grande jogo do fim de semana"),
    ("LE DÉBAT · 讨论", "LE DÉBAT · O DEBATE"),
    ("事先不知道决赛选手，是更刺激还是更扫兴？写两句支持、两句反对。", "Não saber os finalistas de antemão é mais emocionante ou mais frustrante? Escrevam duas frases a favor e duas contra."),
    ("决赛在周日 8 日", "A final é no domingo, dia 8"),
    ("SPORT · 体育", "SPORT · DESPORTO"),
    ("完成句子", "Completar frases"),
    ("句型转换", "Transformação"),
    ("词汇配对", "Associação"),
    ("阅读判断", "Verdadeiro ou falso"),
    ("单选", "Escolha múltipla"),
    ("改写", "Reescrever"),
    ("配对", "Associar"),
])
print(f"content34 done, {len(LOG)} replacements so far")

# ---------- content56: P5 + P6 ----------
rep_all("content56.py", [
    ("À VOUS ! · 即学即练", "À VOUS ! · A VOSSA VEZ"),
    ("JEUNESSE & MUSIQUE · 青年", "JEUNESSE & MUSIQUE · JUVENTUDE"),
    ("NIVEAU B1 · Pitchfork Paris · 音乐节", "NIVEAU B1 · Pitchfork Paris · FESTIVAL DE MÚSICA"),
    ("un lieu 场所、场地 · une affiche 海报 · les paroles 歌词 · donner le ton 定调子 · se promener 漫步、穿梭 · pile 正好、恰好。",
     "un lieu lugar, sala · une affiche cartaz · les paroles letra · donner le ton dar o tom · se promener passear, andar · pile exatamente, mesmo."),
    ("读第 5 版文章，选出正确答案。", "Leiam o artigo da página 5 e escolham a resposta certa."),
    ("音乐节 11 月 2–8 日，整整一周", "O festival é de 2 a 8 de novembro, uma semana inteira"),
    ("15 届音乐节", "É a 15.ª edição do festival"),
    ("Avant-Garde 在巴士底各场地，周四至周六", "O Avant-Garde é em Bastille, de quinta a sábado"),
    ("俱乐部之夜在周五、周六", "As noites club são na sexta e no sábado"),
    ("开幕夜：Headache、Iceage、DIIV", "Noite de abertura: Headache, Iceage, DIIV"),
    ("用 lieux / paroles / affiche / ambiance / danse / découvre 填空。", "Completem com lieux / paroles / affiche / ambiance / danse / découvre."),
    ("10 个场地", "Dez lugares"),
    ("歌词也是法语学习材料", "A letra das canções também ajuda a aprender francês"),
    ("海报上写着演出信息", "No cartaz do festival lêem-se os nomes dos grupos"),
    ("每晚气氛各不相同", "Cada noite tem um ambiente diferente"),
    ("音乐节上人们跳舞", "No festival, dança-se entre dois concertos"),
    ("发现不认识的乐队", "Descobrem-se grupos que não se conhecem"),
    ("把音乐词和释义配对。", "Associem as palavras da música aos significados."),
    ("concert=音乐会 a", "concert=concerto a"),
    ("scène=舞台 b", "scène=palco b"),
    ("groupe=乐队 c", "groupe=grupo c"),
    ("billet=门票 d", "billet=bilhete d"),
    ("补全对话（音乐节门口）。", "Completem o diálogo (à entrada do festival)."),
    ("今晚演出的乐队", "O grupo que toca esta noite"),
    ("买两张票", "Dois bilhetes"),
    ("MOTS DE LA MUSIQUE · 音乐词表", "MOTS DE LA MUSIQUE · PALAVRAS"),
    ("un festival — 音乐节", "un festival — festival"),
    ("un concert — 音乐会", "un concert — concerto"),
    ("une chanson — 歌曲", "une chanson — canção"),
    ("un chanteur — 歌手", "un chanteur — cantor"),
    ("danser — 跳舞", "danser — dançar"),
    ("écouter — 聆听", "écouter — ouvir"),
    ("une salle — 演出厅", "une salle — sala"),
    ("le public — 观众", "le public — público"),
    ("PARIS CREATOR WEEK · 创作者周", "PARIS CREATOR WEEK · SEMANA DOS CRIADORES"),
    ("11 月 4–5 日拉维莱特：创作者周，线上创作者与观众线下见面。",
     "4–5 de novembro, La Villette: semana dos criadores, criadores em linha encontram o público ao vivo."),
    ("十个场地的音乐节，比单一大场馆更好吗？你听什么音乐学法语？",
     "Um festival em dez lugares é melhor do que uma única grande sala? E vocês, que música ouvem para aprender francês?"),
    ("POLITIQUE & CHIFFRES · 时事", "POLITIQUE & CHIFFRES · ATUALIDADE"),
    ("NIVEAU B2 · Budget 2027 · 预算周", "NIVEAU B2 · Budget 2027 · SEMANA DO ORÇAMENTO"),
    ("un budget 预算 · une mission （预算）分项 · un député 国民议会议员 · rejeter 否决 · à l'unanimité 一致通过/否决 · un amendement 修正案。",
     "un budget orçamento · une mission rubrica (do orçamento) · un député deputado da Assembleia Nacional · rejeter rejeitar · à l'unanimité por unanimidade · un amendement alteração."),
    ("LE CALENDRIER PRÉVU · 计划中的投票日程（结果未出）", "LE CALENDRIER PRÉVU · CALENDÁRIO PREVISTO (SEM RESULTADOS)"),
    ("本页日程为计划安排，结果尚未产生，下期跟进。", "Este calendário é um programa previsto; os resultados ainda não existem — acompanhem no próximo número."),
    ("LIRE LE CALENDRIER · 读日程", "LIRE LE CALENDRIER · LER O CALENDÁRIO"),
    ("读上图日程，选出正确答案。", "Leiam o calendário acima e escolham a resposta certa."),
    ("周二 3 日：文化与媒体", "Terça, dia 3: Cultura e Média"),
    ("周三 4 日：农业", "Quarta, dia 4: Agricultura"),
    ("周四 5 日：国土协调与科研", "Quinta, dia 5: Coesão e Investigação"),
    ("周五 6 日：公共财政与经济", "Sexta, dia 6: Finanças públicas e Economia"),
    ("10 月 23 日社保预算收入被 115–1 否决", "A 23 de outubro, as receitas foram rejeitadas por 115–1"),
    ("参议院从 11 月 9 日起审议", "O Senado examina o texto a partir de 9 de novembro"),
    ("LES MOTS · 词汇", "LES MOTS · VOCABULÁRIO"),
    ("député=议员 a", "député=deputado a"),
    ("rejeter=否决 b", "rejeter=rejeitar b"),
    ("vote=投票 c", "vote=voto c"),
    ("amendement=修正案 d", "amendement=alteração d"),
    ("« Le texte part au Sénat. » — 法案送交参议院。", "« Le texte part au Sénat. » — O texto segue para o Senado."),
    ("« Ce calendrier peut encore bouger. » — 日程仍可能变动。", "« Ce calendrier peut encore bouger. » — O calendário ainda pode mudar."),
    ("« Les résultats ne sont pas connus. » — 结果尚未揭晓。", "« Les résultats ne sont pas connus. » — Os resultados ainda não são conhecidos."),
    ("译注｜prévu 预定的、计划的 · réaliser 实现、完成 · distinguer 区分。",
     "Nota — prévu previsto, planeado · réaliser realizar, concretizar · distinguer distinguir."),
    ("用比较级完成句子。", "Completem as frases com o comparativo."),
    ("预算辩论比一场音乐会长", "Um debate sobre o orçamento é mais longo que um concerto"),
    ("预算比时间表复杂", "O orçamento é menos simples que um calendário"),
    ("文化预算与农业预算同样重要", "O orçamento da Cultura é tão importante como o da Agricultura"),
    ("MICRO-DRILLS · 即学即练", "MICRO-DRILLS · TREINO"),
    ("用 examine / ont rejeté / part / peut / connus 填空。", "Completem com examine / ont rejeté / part / peut / connus."),
    ("国民议会审议预算", "A Assembleia examina o orçamento"),
    ("议员们否决收入部分", "Os deputados rejeitaram as receitas"),
    ("法案送交参议院", "O texto segue para o Senado"),
    ("日程仍可能变动", "O calendário ainda pode mudar"),
    ("结果尚未揭晓", "Os resultados ainda não são conhecidos"),
    ("讨论｜结果未出时，该不该先公布日程？区分 prévu（计划）与 décidé（已定）。",
     "Debate — Quando os resultados ainda não saíram, deve-se anunciar o programa? Distinguir prévu (previsto) de décidé (decidido)."),
    ("LE DÉBAT · 讨论", "LE DÉBAT · O DEBATE"),
    ("完成句子", "Completar frases"),
    ("词汇配对", "Associação"),
    ("图表读数", "Leitura de gráficos"),
    ("单选", "Escolha múltipla"),
    ("配对", "Associar"),
])
print(f"content56 done, {len(LOG)} replacements so far")

# ---------- content7: P7 ----------
rep_all("content7.py", [
    ("LANGUE EN MAIN · 精讲", "LANGUE EN MAIN · LÍNGUA"),
    ("A2 → B2 · Les phrases de la semaine · 本周金句", "A2 → B2 · Les phrases de la semaine · FRASES DA SEMANA"),
    ("NIVEAU A2 · 基础", "NIVEAU A2 · NÍVEL BÁSICO"),
    ("NIVEAU B1 · 进阶", "NIVEAU B1 · INTERMEDIÁRIO"),
    ("NIVEAU B2 · 挑战", "NIVEAU B2 · DESAFIO"),
    ("BOÎTE À OUTILS · 工具箱", "BOÎTE À OUTILS · PARA LEVAR"),
    ("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。",
     "Caixa de ferramentas: três frases para levar, uma por nível; todas as frases vêm dos artigos deste número — releiam o artigo e a frase fica."),
    ("LES PHRASES DE LA SEMAINE · 本周金句（全部出自本期文章）", "LES PHRASES DE LA SEMAINE · FRASES DA SEMANA"),
    ("每句一个语法点 + 一道小题 · 答案见第 8 版", "Cada frase, um ponto de gramática + um exercício · respostas na página 8"),
    ("语法点｜reprendre：复课、重新开始（pause 后）。", "Ponto de gramática: reprendre — voltar às aulas, recomeçar (após uma pausa)."),
    ("语法点｜ne...pas encore：尚未、还不。", "Ponto de gramática: ne...pas encore — ainda não."),
    ("语法点｜passé composé 代动词：se + être + 过去分词。", "Ponto de gramática: passé composé reflexo — se + être + particípio passado."),
    ("语法点｜comparatif：plus + 形容词，ou 对举。", "Ponto de gramática: comparatif — plus + adjetivo; ou opõe os dois termos."),
    ("语法点｜se promener：代动词，漫步、穿梭。", "Ponto de gramática: se promener — verbo reflexo, passear, andar."),
    ("语法点｜pouvoir + 动词原形：可能、可以。", "Ponto de gramática: pouvoir + infinitivo — poder, ser possível."),
    ("语法点｜se jouer：决出胜负、上演（代动词）。", "Ponto de gramática: se jouer — decidir o resultado, acontecer (verbo reflexo)."),
    ("语法点｜rencontrer：与观众见面；y 代指地点。", "Ponto de gramática: rencontrer — encontrar o público; y refere-se ao lugar."),
    ("pas encore 尚未", "pas encore = ainda não"),
    ("plus + 形容词", "plus + adjetivo"),
    ("CLINIQUE DES ERREURS · 易错诊所", "CLINIQUE DES ERREURS · CLÍNICA"),
    ("每句有一处错误：找出来并改正。", "Cada frase tem um erro: encontrem-no e corrijam-no."),
    ("jamais + de：否定句中 des 变 de", "jamais + de: na negação, des passa a de"),
    ("主谓一致：créateurs 复数 → rencontrent，不是 rencontre", "Concordância: créateurs (plural) → rencontrent, não rencontre"),
    ("虚拟式：il examine，不加 s", "Subjuntivo: il examine, sem s"),
    ("事实：决赛在 8 日，不是 7 日", "Facto: a final é no dia 8, não no dia 7"),
    ("LE COURRIER DES LECTEURS · 读者园地", "LE COURRIER DES LECTEURS · CARTAS DOS LEITORES"),
    ("小墨点评｜编辑部示例：周末叙事用 passé composé 很稳，分号连接两天值得学。下期读者园地将点评真实投稿。",
     "Xiao Mo comenta (texto-exemplo): o passé composé está seguro na narrativa do fim de semana; o ponto e vírgula liga os dois dias e vale a pena imitar. No próximo número, a secção comentará textos reais."),
    ("编辑部说明：截至付印，编辑部尚未收到 VOL.2 第 8 版的投稿作文（W44 未出刊），故本期刊登标注明确的编辑部示例；VOL.4 将兑现点评真实投稿的承诺。",
     "Nota da redação: sem cartas nem redações do VOL.2 até ao fecho (o W44 não saiu) — exemplo identificado. Enviem-nos cartas e as melhores redações da página 8 para o VOL.4!"),
    ("LA SEMAINE PROCHAINE · VOL.4 下周预告", "LA SEMAINE PROCHAINE · PRÓXIMA SEMANA · VOL.4"),
    ("下周：参议院审议社保预算、11 月 11 日停战纪念日、迪耶普扇贝集市；还有你们的来信！",
     "Na próxima semana: o Senado e o orçamento da Segurança Social, 11 de novembro, Dia do Armistício, feira de Dieppe — e as vossas cartas, finalmente!"),
    ("跟练", "Prática"),
    ("改错", "Correção de erros"),
])
print(f"content7 done, {len(LOG)} replacements so far")

# ---------- content8: P8 ----------
rep_all("content8.py", [
    ("EXERCICES & RÉPONSES · 练习与答案", "EXERCICES & RÉPONSES · EXERCÍCIOS E RESPOSTAS"),
    ("综合评估 ÉVALUATION · 答案在本版下方", "AVALIAÇÃO COMPLETA · ÉVALUATION · RESPOSTAS NO FIM DESTA PÁGINA"),
    ("11 月 8 日 2026 是星期日", "8 de novembro de 2026 é domingo"),
    ("去南泰尔看决赛", "Ir a Nanterre ver a final"),
    ("决赛选手周六晚才揭晓", "Os finalistas só serão conhecidos no sábado à noite"),
    ("品尝语境（un régal）→ goûté", "Contexto de prova (un régal) → goûté"),
    ("se promener 漫步", "se promener = passear"),
    ("avoir + 过去分词 goûté（不配合）", "avoir + particípio passado goûté (sem concordância)"),
    ("les finales 主语复数 → ont lieu", "les finales (plural) → ont lieu"),
    ("elle écrit 她写", "elle écrit = ela escreve"),
    ("A · TEXTE À TROUS · 完形填空", "A · TEXTE À TROUS · TEXTO COM LACUNAS"),
    ("选项：", "Opções:"),
    ("B · CHOIX MULTIPLE · 单选", "B · CHOIX MULTIPLE · ESCOLHA MÚLTIPLA"),
    ("7 nov. = samedi（最后夜场）", "7 nov. = samedi (última noite)"),
    ("s'intéresser aux（à+les）", "s'intéresser aux (à + les)"),
    ("si + imparfait（未完成过去时）→ conditionnel présent（条件式现在时）；j' 是 je 在元音前的省音",
     "si + imparfait → conditionnel présent; j' é je antes de vogal (elisão)"),
    ("主语 ce programme 三单 → semble", "Sujeito ce programme (3.ª pessoa do singular) → semble"),
    ("将来时 aura lieu（决赛在周日）", "Futuro aura lieu (a final é no domingo)"),
    ("三区同日复课", "As três zonas voltam no mesmo dia"),
    ("扇贝节在 11 月 7–8 日", "A festa da vieira é a 7–8 de novembro"),
    ("C · LECTURE · 阅读理解", "C · LECTURE · COMPREENSÃO DE LEITURA"),
    ("夜场 19 点至凌晨 1 点", "A noite é das 19 horas à 1 da manhã"),
    ("小徽章给小 Léo 驱怪", "O distintivo é para o pequeno Léo, contra monstros"),
    ("周日先看决赛再吃扇贝", "No domingo, primeiro vêem a final e depois provam vieiras"),
    ("周日晚上早睡因为周一上学", "No domingo à noite, Léo deita-se cedo porque na segunda há escola"),
    ("周一是上学日（复课后正常周一）", "A segunda é dia de escola (segunda normal após as férias)"),
    ("D · PHRASES · 完成句子与转换", "D · PHRASES · FRASES"),
    ("aller + 原形（futur proche）", "aller + infinitivo (futur proche)"),
    ("si + 半过去时 venais", "si + imparfait (venais)"),
    ("passé composé : a + 过去分词", "passé composé: a + particípio passado"),
    ("selon moi = 在我看来", "selon moi = na minha opinião"),
    ("il est prévu que + 虚拟式", "il est prévu que + subjuntivo"),
    ("E · TRADUCTION · 翻译", "E · TRADUCTION · TRADUÇÃO"),
    ("读一份日程，本身就是在了解法国。", "Ler um programa já é compreender a França."),
    ("lire un programme = 读日程", "lire un programme = ler um programa"),
    ("Traduisez : « Lire un programme, c'est déjà comprendre la France. »",
     "Traduza para o português: « Lire un programme, c'est déjà comprendre la France. »"),
    ("比较级 plus vite + court", "Comparativo: plus vite + court"),
    ("Traduisez : 他跑得比他哥哥更快。", "Traduza para o francês: Ele corre mais rápido que o irmão."),
    ("Traduisez : 学生们自 10 月 17 日起就在放假。", "Traduza para o francês: Os alunos estão de férias desde 17 de outubro."),
    ("Traduisez : 今晚，我们要准备书包。", "Traduza para o francês: Hoje à noite, vamos preparar as nossas mochilas."),
    ("ne...pas encore = 尚未", "ne...pas encore = ainda não"),
    ("Traduisez : 人们尚不知道决赛选手是谁。", "Traduza para o francês: Ainda não se conhecem os finalistas."),
    ("F · LES MOTS · 词汇配对", "F · LES MOTS · VOCABULÁRIO"),
    ("tournoi=赛事 a", "tournoi=torneio a"),
    ("nocturne=夜场 b", "nocturne=noite b"),
    ("budget=预算 c", "budget=orçamento c"),
    ("coquille=扇贝 d", "coquille=vieira d"),
    ("festival=音乐节 e", "festival=festival e"),
    ("11 月 7 日是星期六", "7 de novembro é sábado"),
    ("在市场买扇贝", "Comprar vieiras no mercado"),
    ("goûter 品尝（原形）", "goûter = provar (infinitivo)"),
    ("à la portaise 是一种做法", "à la portaise é um modo de preparação"),
    ("Bon week-end ! 周末愉快", "Bon week-end ! = Bom fim de semana!"),
    ("G · DIALOGUE · 对话补全", "G · DIALOGUE · DIÁLOGO"),
    ("开放题 — 要点见写作框，范文在第 8 版写作框内",
     "Questão aberta — os pontos estão no quadro de escrita e o modelo está no quadro MODÈLE desta página"),
    ("按要点给分", "Avaliação por pontos"),
    ("H · ÉCRITURE · 写作", "H · ÉCRITURE · REDAÇÃO"),
    ("用法语写 80–100 词：我的 11 月 7–8 日周末。写清一场比赛、一个节日、一道菜。",
     "Escrevam 80–100 palavras em francês: o meu fim de semana de 7–8 de novembro. Descrevam um jogo, uma festa, um prato. Os melhores textos sairão no VOL.4 (página 7, « Le courrier des lecteurs »)."),
    ("MODÈLE · 范文", "MODÈLE · MODELO"),
    ("RÉPONSES · 全部答案与简析（第 1–8 版）", "RÉPONSES · TODAS AS RESPOSTAS COM NOTAS (PÁGINAS 1–8)"),
    ("完成句子", "Completar frases"),
    ("完形填空", "Texto com lacunas"),
    ("阅读理解", "Compreensão de leitura"),
    ("对话补全", "Completar diálogos"),
    ("词汇配对", "Associação"),
    ("单选", "Escolha múltipla"),
    ("翻译", "Tradução"),
    ("写作", "Redação"),
    ("配对", "Associar"),
])
print(f"content8 done, {len(LOG)} replacements total")
with open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(LOG) + "\n")
print("LOG WRITTEN", len(LOG))

# ================= FIX ROUND 2 (after r1 render: P1 overflow, P2 overlap,
# P6-ex/P8 heads too wide, P8 battery+keys overflow) =================
# All fixes below target the PT v1 strings produced above, so a fresh
# pristine-core + transform.py run reproduces the fixed paper exactly.
# Pre-fix baseline: pre-fix-hashes-r1-full.txt (r1 SVG/card/PDF sha256).

# (a) P1 gloss: PT v1 wrapped to 7 lines vs core 5 -> headline flow spilled
# 127px past its 1812 bottom and overprinted the row-B head (r1 card).
# Shorten meanings to single/short words: back to 5 lines, all 7 items kept.
rep("content12.py",
    "se jouer decidir o resultado, acontecer · une finale final · une demi-finale meia-final · un quart de finale quarto de final · une nocturne evento noturno · un frisson arrepio, emoção · la coquille Saint-Jacques vieira.",
    "se jouer decidir, acontecer · une finale final · une demi-finale meia-final · un quart de finale quarto de final · une nocturne evento · un frisson arrepio · la coquille Saint-Jacques vieira.", 1)
# (b) P1 headline French paras 25pt/1.52 -> 24pt/1.45 (fr-de precedent for the
# same headline flow): line-based edit, scoped to the P1-headline flow.
_p = os.path.join(BASE, "content12.py")
_lines = open(_p, encoding="utf-8").read().splitlines(keepends=True)
_in = False
_n = 0
for _i, _ln in enumerate(_lines):
    if 'tag="P1-headline"' in _ln:
        _in = True
        continue
    if _in and _ln.strip().startswith("f.gloss("):
        break
    if _in and _ln.strip().startswith("f.para("):
        _s = _ln.rstrip("\n")
        assert _s.endswith('")'), f"unexpected headline para line: {_s[-40:]}"
        _lines[_i] = _s[:-1] + ', 24, "serif", False, INK, 1.45)\n'
        _n += 1
assert _n == 5, f"P1 headline paras edited: {_n} != 5"
open(_p, "w", encoding="utf-8").write("".join(_lines))
LOG.append("content12.py: P1-headline 5 paras 25/1.52 -> 24/1.45")
# (c) P2 ET VOUS PT v1 wrapped to 4 lines -> box bottom 1596.6 overlapped the
# DIRE LA DATE rule (1558) and subtitle on the r1 card. 2-line form restores
# the core/DE box bottom 1538.6 (eh drops exactly 58px: 2 fewer lines x 29).
rep("content12.py",
    "Contem-nos a vossa volta às aulas: onde estavam na segunda de manhã? Que livro leram nas férias? Escrevam duas frases em francês para a redação.",
    "Segunda de manhã: onde estavam? Que livro leram? Duas frases para a redação!", 2)
# (d) P6-ex head too wide at 25pt (525.8 > 434): shorter suffix + 24pt (430.5).
rep("content56.py",
    'e6.head("LIRE LE CALENDRIER · LER O CALENDÁRIO", 25)',
    'e6.head("LIRE LE CALENDRIER · CALENDÁRIO", 24)', 1)
# (e) P8 battery heads too wide at 24pt (> 434): shorten PT suffixes.
rep("content8.py", '"A · TEXTE À TROUS · TEXTO COM LACUNAS"', '"A · TEXTE À TROUS · LACUNAS"', 1)
rep("content8.py", '"B · CHOIX MULTIPLE · ESCOLHA MÚLTIPLA"', '"B · CHOIX MULTIPLE · ESCOLHA"', 1)
rep("content8.py", '"C · LECTURE · COMPREENSÃO DE LEITURA"', '"C · LECTURE · COMPREENSÃO"', 1)
# (f) P8 battery: PT E stems wrap to 2 lines (+116px vs core) -> battery ended
# 1526 past its 1485 bottom, into the writing strip. DE-precedent adaptation:
# battery ex gap 11 -> 6, battery paras 21 -> 20, F match gap 14 -> 6.
_p = os.path.join(BASE, "content8.py")
_lines = open(_p, encoding="utf-8").read().splitlines(keepends=True)
_n_ex = _n_pa = 0
for _i, _ln in enumerate(_lines):
    _s = _ln.rstrip("\n")
    if _s.startswith("    bf.ex(") and _s.endswith(", size=20)"):
        _lines[_i] = _s[:-len(", size=20)")] + ", size=20, gap=6)\n"
        _n_ex += 1
    if _s.startswith("bf.para(") and _s.endswith(", 21)"):
        _lines[_i] = _s[:-len(", 21)")] + ", 20)\n"
        _n_pa += 1
assert _n_ex == 4, f"battery bf.ex gap edits: {_n_ex} != 4"
assert _n_pa == 3, f"battery bf.para size edits: {_n_pa} != 3"
open(_p, "w", encoding="utf-8").write("".join(_lines))
LOG.append("content8.py: battery bf.ex gap=6 x4, bf.para 21->20 x3")
rep("content8.py", 'instr="Associar")', 'instr="Associar", gap=6)', 1)
# (g) P8 keys: PT notes overflowed keys flow to 2625 (bottom 2545, footer
# zone). DE-precedent: keys 15.5 -> 14.5pt (writing strip wy stays 1500:
# battery fix (f) clears the strip, so no wy move is needed).
rep("content8.py",
    'kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)', 1)
with open(os.path.join(BASE, "transform-log.txt"), "a", encoding="utf-8") as f:
    f.write("\n".join(LOG[340:]) + "\n")
print(f"FIX ROUND 2 done, {len(LOG)} replacements total")

# ================= FIX ROUND 3 (after r2 gates: 5 PT overflow defects;
# P8-F right-edge + line-start ':' proven core-identical, NOT fixed) =====
# Pre-fix baseline: pre-fix-hashes-r2-full.txt (r2 SVG/card/PDF sha256).
# (a) P1 agenda note: p.text does not wrap; PT v2 ran to x1=2249.5, past
# the page edge. Short form fits the col-3 box (390.5 < 412).
rep("content12.py",
    "Os resultados do fim de semana final serão conhecidos no sábado à noite e no domingo.",
    "Resultados no sábado à noite e no domingo.", 1)
# (b) P1 sommaire title over box border (x1=1908.9 > 1885): W43 PT form.
rep("content12.py", '"DANS CE NUMÉRO · NESTE NÚMERO"', '"DANS CE NUMÉRO · SUMÁRIO"', 1)
# (c) P3 dates box title over box border (x1=1951.8): shorter suffix.
rep("content34.py", '"DATES À RETENIR · DATAS DESTA SEMANA"', '"DATES À RETENIR · DATAS"', 1)
# (d) P5 creator box title over box border (x1=2038.6, audit BOXTITLE):
# shorter suffix (393.1 < 412); the English head already says WEEK.
rep("content56.py", '"PARIS CREATOR WEEK · SEMANA DOS CRIADORES"', '"PARIS CREATOR WEEK · CRIADORES"', 1)
# (e) P6 chart note: p.text does not wrap; PT v2 ran to x1=1063, past the
# chart box border (961) and over a col-2 exercise line (audit TEXTX +
# BOXTITLE). Short form fits the chart box inner width (640.0 < 874).
rep("content56.py",
    "Este calendário é um programa previsto; os resultados ainda não existem — acompanhem no próximo número.",
    "Este calendário é um programa previsto; os resultados ainda não saíram.", 1)
print(f"FIX ROUND 3 done, {len(LOG)} replacements total")
with open(os.path.join(BASE, "transform-log.txt"), "a", encoding="utf-8") as f:
    f.write("FIX ROUND 3: 5 reps\n")

# ================= FIX ROUND 4 (after r3 gates: 2 BOXTITLE flags) =========
# Pre-fix baseline: pre-fix-hashes-r3-full.txt (r3 SVG/card/PDF sha256).
# (a) P1 LES DATES Flow-box title over its box border (ink 986 > 961,
# visible on the r3 card spilling into the next column): shorter suffix
# (329.0 < 398 inner width). Box height unchanged (title stays 1 line).
rep("content12.py", '"LES DATES · FIM DE SEMANA DECISIVO"', '"LES DATES · FIM DE SEMANA"', 1)
# (b) P2 ET VOUS box: last-line 'ç' descender ink 1539.5 grazed the box
# bottom border (1538.6) by 0.9px on the r3 card. Add 8px bottom padding
# to the computed box height: bottom 1546.6, ink clearance ~7px, still
# 11.4px clear of the DIRE LA DATE rule (1558). Line-based edit.
_p = os.path.join(BASE, "content12.py")
_lines = open(_p, encoding="utf-8").read().splitlines(keepends=True)
_n = 0
for _i, _ln in enumerate(_lines):
    if _ln.startswith("eh = 62 +"):
        assert _ln.rstrip("\n").endswith("+ 20"), f"unexpected eh line: {_ln[-60:]}"
        _lines[_i] = _ln.rstrip("\n")[:-len("+ 20")] + "+ 28\n"
        _n += 1
assert _n == 1, f"eh edits: {_n} != 1"
open(_p, "w", encoding="utf-8").write("".join(_lines))
LOG.append("content12.py: ET VOUS box bottom padding +20 -> +28")
print(f"FIX ROUND 4 done, {len(LOG)} replacements total")
with open(os.path.join(BASE, "transform-log.txt"), "a", encoding="utf-8") as f:
    f.write("FIX ROUND 4: 2 edits\n")
