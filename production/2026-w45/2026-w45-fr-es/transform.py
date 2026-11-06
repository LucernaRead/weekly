# -*- coding: utf-8 -*-
"""FR x ES fan-out transform for W45 FR core build copy (VOL.3).

Rules (tools/README #17/#18): whole-string or exact-unique-literal
replacements with count assertions; value maps use bare text, never repr.
French target text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token, except the documented re-aimed P8 translation items
(E1 key/note/stem, E2-E5 stems) and the P8 printing rule (see below).
Furniture follows the SHIPPED W43 FR x ES edition
(files/weekly-report-fr-es/), which wins over any generic rule:
badge INSERTED at y=574, 22pt BRICK, centred, Spanish form;
footer VOL.3 in the canonical ES template; gloss prefix "Nota — ";
short bilingual heads (LÉXICO, FECHAS, EL DEBATE, A PRACTICAR,
VOCABULARIO, RECURSOS, CLÍNICA, EL RINCÓN DE LOS LECTORES).

P8 printed-note set: the core's rule (page 8 always, or note <= 10 chars,
or clinic/chart types) cannot survive translation, because Spanish notes
are longer. Following the W43 FR x ES precedent, the edition carries
the core's printed set EXPLICITLY (PRINT_NOTES, measured from the core
P8 with tools/p8.py extract --json: 97 numbers) so the same exercises
carry printed notes in both editions. Bare keys (53) are untouched.
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
    rep(f, "weekly-report-w45-fr-core", "weekly-report-w45-fr-es", 1)

# ---------- bslib4: furniture + gloss prefix (W43 shipped forms, VOL.3) ----------
rep("bslib4.py",
    '"Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文"',
    '"Le Lucerna · SEMANARIO FRANCÉS VOL.3 · TEXTO EN FRANCÉS · EXPLICACIONES EN ESPAÑOL"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Nota — " + s', 1)

# ---------- content12: P1 + P2 ----------
rep_all("content12.py", [
    ("VOL. 3 · 总第 3 期", "VOL. 3 · N.º 3"),
    ("HEBDOMADAIRE EN FRANÇAIS · 每周一期 · 读法国人正在读的法语",
     "HEBDOMADAIRE EN FRANÇAIS · CADA SEMANA · EL FRANCÉS QUE LEEN LOS FRANCESES"),
    ("法 语 周 报 · VOL.3 · 决 赛 周 末", "SEMANARIO EN FRANCÉS · VOL.3 · FIN DE SEMANA DE FINALES"),
    ("周一开学 · 全法同步复课", "LUNES, VUELTA AL COLE · EN TODA FRANCIA"),
    ("大师赛开赛 · 音乐节开幕 · 详见第 2 版", "EMPIEZA EL MASTERS · ABRE EL FESTIVAL · VER PÁGINA 2"),
    ("法语正文 · 简体中文讲解 — 给简体中文读者的版本",
     "TEXTOS EN FRANCÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES"),
    ("SPORT · CULTURE · GASTRONOMIE · LA UNE · 决赛周末",
     "SPORT · CULTURE · GASTRONOMIE · LA UNE · FIN DE SEMANA DE FINALES"),
    ("se jouer 决出胜负、上演 · une finale 决赛 · une demi-finale 半决赛 · un quart de finale 四分之一决赛 · une nocturne 夜场活动 · un frisson 战栗、刺激感 · la coquille Saint-Jacques 扇贝。",
     "se jouer decidirse, celebrarse · une finale final · une demi-finale semifinal · un quart de finale cuartos de final · une nocturne evento nocturno · un frisson escalofrío, emoción · la coquille Saint-Jacques vieira."),
    ("LES DATES · 决赛周末日程", "LES DATES · FINALES"),
    ("À VOUS ! · 即学即练", "À VOUS ! · A PRACTICAR"),
    ("周日 8 日举行决赛", "La final es el domingo 8"),
    ("周六 7 日晚是最后夜场", "Último evento nocturno, sábado 7 por la noche"),
    ("波尔诺曼底卖扇贝", "En Port-en-Bessin venden vieiras"),
    ("周一 2 日全法复课", "Toda Francia vuelve el lunes 2"),
    ("半决赛后才知道决赛选手", "Finalistas solo tras las semifinales"),
    ("三个决赛：网球、刺激、美味", "Tres finales: tenis, emoción, sabor"),
    ("本周日程 · 11 月 2 日至 8 日", "PLAN SEMANAL · 2 AL 8 DE NOVIEMBRE"),
    ("周末决赛结果周六晚、周日揭晓。", "Resultados de las finales: sábado noche y domingo."),
    ("DANS CE NUMÉRO · 本期目录", "DANS CE NUMÉRO · EN ESTE NÚMERO"),
    ("决出胜负；上演。本周末一切都将见分晓。",
     "Decidirse; celebrarse. Este fin de semana todo se decide."),
    ("EN BREF · 快讯", "EN BREF · BREVES"),
    ("QUIZ ÉCLAIR · 闪电问答", "QUIZ ÉCLAIR · QUIZ RELÁMPAGO"),
    ("读头版，选出正确答案 · 答案见第 8 版",
     "Lee la portada y elige la respuesta correcta · Respuestas en la página 8"),
    ("决赛在周日 8 日", "La final es el domingo 8"),
    ("扇贝节在滨海波尔", "La fiesta de la vieira, en Port-en-Bessin"),
    ("周一 2 日早上全区复课", "Vuelta al cole el lunes 2 por la mañana"),
    ("最后夜场周六 7 日", "Último evento nocturno, sábado 7"),
    ("VIE QUOTIDIENNE · 生活", "VIE QUOTIDIENNE · VIDA COTIDIANA"),
    ("NIVEAU A2 · La rentrée · 开学复课", "NIVEAU A2 · La rentrée · VUELTA AL COLE"),
    ("la rentrée 开学、复课 · reprendre 重新开始、复课 · un cartable 书包 · un décalage 错开、时差 · en revanche 相反、反之 · un rituel 习惯、仪式。",
     "la rentrée vuelta al cole · reprendre volver a empezar · un cartable mochila · un décalage desfase, diferencia · en revanche en cambio · un rituel costumbre, ritual."),
    ("译注｜une valise 行李箱 · une ambiance 气氛 · le bilan 总结、盘点。",
     "Nota — une valise maleta · une ambiance ambiente · le bilan balance, resumen."),
    ("说说你的开学：周一早上你在哪里？假期读了哪本书？写两句法语寄给编辑部。",
     "Lunes por la mañana: ¿dónde estabas, qué libro? ¡Dos frases a la redacción!"),
    ("ET VOUS ? · 说说你自己", "ET VOUS ? · ¿Y TÚ?"),
    ("DIRE LA DATE · 这样说日期", "DIRE LA DATE · ASÍ SE DICE LA FECHA"),
    ("lundi 2 novembre · 注意：1 日说 le premier，其余用基数词",
     "lundi 2 novembre · Ojo: el día 1 se dice le premier; los demás, con cardinales"),
    ("11 月 2 日星期一 · la rentrée", "Lunes 2 de noviembre · la rentrée"),
    ("11 月 3 日星期二 · votes à l'Assemblée", "Martes 3 de noviembre · votes à l'Assemblée"),
    ("11 月 4 日星期三 · sorties cinéma", "Miércoles 4 de noviembre · sorties cinéma"),
    ("11 月 7 日星期六 · nocturne et demis", "Sábado 7 de noviembre · nocturne et demis"),
    ("11 月 8 日星期日 · les finales", "Domingo 8 de noviembre · les finales"),
    ("EXERCICES · 第 2 版练习", "EXERCICES · EJERCICIOS DE LA PÁGINA 2"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Respuestas en la página 8 · Niveles mezclados; busca por el número"),
    ("用法语补全日期（注意星期与数字）。",
     "Completa la fecha en francés (ojo con el día y el número)."),
    ("复课在星期一", "La vuelta al cole es el lunes"),
    ("11 月 1 日说 le premier", "El 1 de noviembre se dice le premier"),
    ("最后夜场在星期六", "El último evento nocturno es el sábado"),
    ("决赛在星期日", "La final es el domingo"),
    ("用 aller + 动词原形改写（最近将来时）。",
     "Reescribe con aller + infinitivo (futur proche)."),
    ("读第 2 版文章，选出正确答案。",
     "Lee el artículo de la página 2 y elige la respuesta correcta."),
    ("三区同一周一早上复课", "Las tres zonas vuelven el mismo lunes por la mañana"),
    ("冬令时从 10 月 25 日开始", "El horario de invierno empezó el 25 de octubre"),
    ("11 月晚上天黑得早", "En noviembre anochece temprano"),
    ("rentrée=开学 a", "rentrée=vuelta al cole a"),
    ("reprendre=重新开始 b", "reprendre=volver a empezar b"),
    ("cartable=书包 c", "cartable=mochila c"),
    ("rituel=习惯 d", "rituel=costumbre d"),
])

# ---------- content34: P3 + P4 ----------
rep_all("content34.py", [
    ("CULTURE · 文化", "CULTURE · CULTURA"),
    ("NIVEAU A2 → B1 · Halloween, Toussaint · 万圣与诸圣",
     "NIVEAU A2 → B1 · Halloween, Toussaint · HALLOWEEN Y TODOS LOS SANTOS"),
    ("se déguiser 变装、装扮 · un sort 魔法、恶作剧 · une ambiance 气氛 · le souvenir 回忆、纪念 · confondre 混淆 · discret 低调的、安静的。",
     "se déguiser disfrazarse · un sort hechizo, broma · une ambiance ambiente · le souvenir recuerdo, conmemoración · confondre confundir · discret discreto, silencioso."),
    ("判断对错（Vrai / Faux）。", "¿Verdadero o falso? (Vrai / Faux)."),
    ("万圣节在 10 月 31 日星期六", "Halloween fue el sábado 31 de octubre"),
    ("诸圣节墓园摆满菊花", "En Todos los Santos los cementerios se llenan de crisantemos"),
    ("菊花绝不能当礼物送人", "Los crisantemos nunca se regalan"),
    ("11 月 2 日是 jour des morts，不是诸圣节", "El 2 de noviembre es jour des morts, no Toussaint"),
    ("文中：le rire d'abord, le souvenir ensuite", "En el texto: le rire d'abord, le souvenir ensuite"),
    ("用 déguisement / tombe / citrouille / souvenir 填空。",
     "Completa con déguisement / tombe / citrouille / souvenir."),
    ("万圣节穿变装服装", "En Halloween los niños se disfrazan"),
    ("花放在墓碑上", "Las flores se ponen sobre la tumba"),
    ("南瓜是万圣节的象征", "La calabaza es el símbolo de Halloween"),
    ("诸圣节是纪念之日", "Todos los Santos es un día de recuerdo"),
    ("改写句子（用 ne...jamais / ne...plus / ne...pas）。",
     "Reescribe las frases (con ne...jamais / ne...plus / ne...pas)."),
    ("jamais + de（无冠词变化）", "jamais + de (sin cambio de artículo)"),
    ("ne...plus = 不再", "ne...plus = ya no"),
    ("n'est pas = 不是", "n'est pas = no es"),
    ("即学即练 · 公园万圣节小题。", "Practica · Preguntas sobre Halloween en el parque."),
    ("周六 7 日是最后夜场", "Sábado 7: último evento nocturno"),
    ("敏感儿童有免费驱怪徽章", "Los niños sensibles reciben una insignia gratuita contra monstruos"),
    ("阿斯泰里克斯公园在 Plailly", "El parque Astérix está en Plailly"),
    ("Peur sur le Parc 10 月 3 日至 11 月 8 日", "Peur sur le Parc, del 3 de octubre al 8 de noviembre"),
    ("恐惧等级用颜色区分", "Los niveles de miedo se distinguen por colores"),
    ("夜场从 19 点到凌晨 1 点", "El evento nocturno dura de 19 h a 1 h"),
    ("LES MOTS DES FÊTES · 节日词表", "LES MOTS DES FÊTES · LÉXICO"),
    ("un saint — 圣人", "un saint — santo"),
    ("un cimetière — 墓园", "un cimetière — cementerio"),
    ("une tombe — 坟墓", "une tombe — tumba"),
    ("un jour férié — 公共假日", "un jour férié — día festivo"),
    ("se souvenir — 纪念、想起", "se souvenir — recordar, conmemorar"),
    ("un déguisement — 变装服装", "un déguisement — disfraz"),
    ("une citrouille — 南瓜", "une citrouille — calabaza"),
    ("un bonbon — 糖果", "un bonbon — caramelo"),
    ("un fantôme — 幽灵", "un fantôme — fantasma"),
    ("un sort — 魔法、诅咒", "un sort — hechizo, maldición"),
    ("10 月 3 日至 11 月 8 日，12 场夜场；最后夜场 11 月 7 日；白天 10 点至 19 点开放。",
     "Del 3 de octubre al 8 de noviembre: 12 eventos nocturnos, el último el sábado 7. De día, abierto de 10 a 19 h."),
    ("DATES À RETENIR · 本周日历", "DATES À RETENIR · FECHAS"),
    ("注意：迪耶普扇贝集市在 11 月 14–15 日，不在本周。",
     "Ojo: Dieppe, el 14–15 de noviembre, no esta semana."),
    ("SPORT · 体育", "SPORT · DEPORTE"),
    ("À VOUS ! · 即学即练", "À VOUS ! · A PRACTICAR"),
    ("决赛在周日 8 日", "La final es el domingo 8"),
    ("LE DÉBAT · 讨论", "LE DÉBAT · EL DEBATE"),
    ("un tournoi 锦标赛、赛事 · sur dur 硬地球场 · en salle 室内 · un tableau principal 正赛签表 · le tenant du titre 卫冕冠军 · basculer 逆转、倾斜 · les tribunes 看台。",
     "un tournoi torneo · sur dur en pista dura · en salle en pista cubierta · un tableau principal cuadro principal · le tenant du titre defensor del título · basculer cambiar, inclinarse · les tribunes gradas."),
    ("读第 4 版文章，选出正确答案。",
     "Lee el artículo de la página 4 y elige la respuesta correcta."),
    ("大师赛在室内硬地球场举行", "El Masters se juega en pista cubierta y dura"),
    ("2025 年卫冕冠军是辛纳", "El defensor del título 2025 es Sinner"),
    ("法甲第十轮大场面：朗斯–马赛", "Gran partido de la 10.ª jornada de Ligue 1: Lens – Marsella"),
    ("周日 8 日还有轮椅单打决赛（中午）", "Domingo 8: también final individual en silla de ruedas (mediodía)"),
    ("把网球词和释义配对。", "Une cada palabra de tenis con su significado."),
    ("tournoi=赛事 a", "tournoi=torneo a"),
    ("raquette=球拍 b", "raquette=raqueta b"),
    ("tribunes=看台 c", "tribunes=gradas c"),
    ("tenant=卫冕者 d", "tenant=defensor del título d"),
    ("用比较级完成句子（plus / moins）。", "Completa con el comparativo (plus / moins)."),
    ("室内球速更快", "En pista cubierta la pelota va más rápido"),
    ("大师赛是仅次于大满贯的级别", "Un Masters 1000 está por debajo de los Grand Slams"),
    ("室内赛季比室外短", "La temporada en pista cubierta es más corta que la de verano"),
    ("译注｜un choc 强强对决 · recevoir 迎战、接待 · familier 熟悉的。",
     "Nota — un choc gran partido · recevoir recibir, enfrentarse a · familier familiar."),
    ("« Allez ! » — 加油！ · « Quelle action ! » — 好球！",
     "« Allez ! » — ¡Vamos! · « Quelle action ! » — ¡Qué jugada!"),
    ("« Il marque ! » — 他得分了！ · « C'est gagné ! » — 赢了！",
     "« Il marque ! » — ¡Marca! · « C'est gagné ! » — ¡Ganado!"),
    ("« Quel point ! » — 好球！（网球） · « Balle de match ! » — 赛点！",
     "« Quel point ! » — ¡Qué punto! (Tenis) · « Balle de match ! » — ¡Punto de partido!"),
    ("LES MOTS DU TENNIS · 网球词表", "LES MOTS DU TENNIS · LÉXICO"),
    ("le tennis — 网球", "le tennis — tenis"),
    ("une balle — 球", "une balle — pelota"),
    ("un set — 一盘", "un set — set"),
    ("un match — 比赛", "un match — partido"),
    ("un point — 一分", "un point — punto"),
    ("la finale — 决赛", "la finale — final"),
    ("un adversaire — 对手", "un adversaire — rival"),
    ("un titre — 冠军头衔", "un titre — título"),
    ("À SUIVRE · 拭目以待", "À SUIVRE · CONTINUARÁ"),
    ("MICRO-DRILLS · 即学即练", "MICRO-DRILLS · A PRACTICAR"),
    ("用 finale / quarts / demi-finales / tableau / fauteuil / choc 填空。",
     "Completa con finale / quarts / demi-finales / tableau / fauteuil / choc."),
    ("四分之一决赛在周五", "Los cuartos de final son el viernes"),
    ("半决赛在周六", "Las semifinales son el sábado"),
    ("单打决赛在周日", "La final individual es el domingo"),
    ("正赛签表从周一开始", "El cuadro principal empieza el lunes"),
    ("轮椅赛事周五至周日", "El torneo en silla de ruedas, de viernes a domingo"),
    ("朗斯–马赛是周末焦点战", "Lens – Marsella es el gran partido del fin de semana"),
    ("事先不知道决赛选手，是更刺激还是更扫兴？写两句支持、两句反对。",
     "¿Finalistas desconocidos de antemano: más emocionante o más frustrante? Escribe dos frases a favor y dos en contra."),
])

# ---------- content56: P5 + P6 ----------
rep_all("content56.py", [
    ("JEUNESSE & MUSIQUE · 青年", "JEUNESSE & MUSIQUE · JUVENTUD"),
    ("NIVEAU B1 · Pitchfork Paris · 音乐节", "NIVEAU B1 · Pitchfork Paris · FESTIVAL"),
    ("un lieu 场所、场地 · une affiche 海报 · les paroles 歌词 · donner le ton 定调子 · se promener 漫步、穿梭 · pile 正好、恰好。",
     "un lieu lugar, sala · une affiche cartel · les paroles letras · donner le ton marcar la pauta · se promener pasear, moverse · pile justo, exactamente."),
    ("À VOUS ! · 即学即练", "À VOUS ! · A PRACTICAR"),
    ("读第 5 版文章，选出正确答案。",
     "Lee el artículo de la página 5 y elige la respuesta correcta."),
    ("音乐节 11 月 2–8 日，整整一周", "El festival, del 2 al 8 de noviembre, una semana entera"),
    ("15 届音乐节", "15.ª edición del festival"),
    ("Avant-Garde 在巴士底各场地，周四至周六", "Avant-Garde en las salas de Bastille, de jueves a sábado"),
    ("俱乐部之夜在周五、周六", "Noches de club el viernes y el sábado"),
    ("开幕夜：Headache、Iceage、DIIV", "Noche inaugural: Headache, Iceage, DIIV"),
    ("用 lieux / paroles / affiche / ambiance / danse / découvre 填空。",
     "Completa con lieux / paroles / affiche / ambiance / danse / découvre."),
    ("10 个场地", "Diez salas"),
    ("歌词也是法语学习材料", "Las letras también sirven para aprender francés"),
    ("海报上写着演出信息", "En el cartel están los nombres de los grupos"),
    ("每晚气氛各不相同", "Cada noche, un ambiente distinto"),
    ("音乐节上人们跳舞", "En el festival se baila"),
    ("发现不认识的乐队", "Descubrir grupos que no conoces"),
    ("把音乐词和释义配对。", "Une cada palabra de música con su significado."),
    ("concert=音乐会 a", "concert=concierto a"),
    ("scène=舞台 b", "scène=escenario b"),
    ("groupe=乐队 c", "groupe=grupo c"),
    ("billet=门票 d", "billet=entrada d"),
    ("补全对话（音乐节门口）。", "Completa el diálogo (en la entrada del festival)."),
    ("今晚演出的乐队", "El grupo que toca esta noche"),
    ("买两张票", "Comprar dos entradas"),
    ("MOTS DE LA MUSIQUE · 音乐词表", "MOTS DE LA MUSIQUE · LÉXICO"),
    ("un festival — 音乐节", "un festival — festival"),
    ("un concert — 音乐会", "un concert — concierto"),
    ("une chanson — 歌曲", "une chanson — canción"),
    ("un chanteur — 歌手", "un chanteur — cantante"),
    ("danser — 跳舞", "danser — bailar"),
    ("écouter — 聆听", "écouter — escuchar"),
    ("une salle — 演出厅", "une salle — sala"),
    ("le public — 观众", "le public — público"),
    ("PARIS CREATOR WEEK · 创作者周", "PARIS CREATOR WEEK · CREADORES"),
    ("11 月 4–5 日拉维莱特：创作者周，线上创作者与观众线下见面。",
     "4–5 de noviembre en La Villette: Creator Week, creadores en línea con su público en persona."),
    ("LE DÉBAT · 讨论", "LE DÉBAT · EL DEBATE"),
    ("十个场地的音乐节，比单一大场馆更好吗？你听什么音乐学法语？",
     "¿Un festival en diez salas: mejor que una sola gran sala? ¿Qué música escuchas para aprender francés?"),
    ("POLITIQUE & CHIFFRES · 时事", "POLITIQUE & CHIFFRES · ACTUALIDAD"),
    ("NIVEAU B2 · Budget 2027 · 预算周", "NIVEAU B2 · Budget 2027 · SEMANA DEL PRESUPUESTO"),
    ("un budget 预算 · une mission （预算）分项 · un député 国民议会议员 · rejeter 否决 · à l'unanimité 一致通过/否决 · un amendement 修正案。",
     "un budget presupuesto · une mission partida (del presupuesto) · un député diputado · rejeter rechazar · à l'unanimité por unanimidad · un amendement enmienda."),
    ("LE CALENDRIER PRÉVU · 计划中的投票日程（结果未出）",
     "LE CALENDRIER PRÉVU · PREVISTO, SIN RESULTADOS"),
    ("本页日程为计划安排，结果尚未产生，下期跟进。",
     "Este calendario es provisional; los resultados, en el próximo número."),
    ("LIRE LE CALENDRIER · 读日程", "LIRE LE CALENDRIER · LEE EL CALENDARIO"),
    ("读上图日程，选出正确答案。",
     "Lee el calendario de arriba y elige la respuesta correcta."),
    ("周二 3 日：文化与媒体", "Martes 3: Cultura y Medios"),
    ("周三 4 日：农业", "Miércoles 4: Agricultura"),
    ("周四 5 日：国土协调与科研", "Jueves 5: Cohesión territorial e Investigación"),
    ("周五 6 日：公共财政与经济", "Viernes 6: Finanzas públicas y Economía"),
    ("10 月 23 日社保预算收入被 115–1 否决",
     "El 23 de octubre: ingresos del presupuesto social rechazados por 115–1"),
    ("参议院从 11 月 9 日起审议", "El Senado lo examina desde el 9 de noviembre"),
    ("LES MOTS · 词汇", "LES MOTS · VOCABULARIO"),
    ("député=议员 a", "député=diputado a"),
    ("rejeter=否决 b", "rejeter=rechazar b"),
    ("vote=投票 c", "vote=votación c"),
    ("amendement=修正案 d", "amendement=enmienda d"),
    ("« Le texte part au Sénat. » — 法案送交参议院。",
     "« Le texte part au Sénat. » — El texto va al Senado."),
    ("« Ce calendrier peut encore bouger. » — 日程仍可能变动。",
     "« Ce calendrier peut encore bouger. » — El calendario aún puede cambiar."),
    ("« Les résultats ne sont pas connus. » — 结果尚未揭晓。",
     "« Les résultats ne sont pas connus. » — Los resultados aún no se conocen."),
    ("译注｜prévu 预定的、计划的 · réaliser 实现、完成 · distinguer 区分。",
     "Nota — prévu previsto, planificado · réaliser realizar, cumplir · distinguer distinguir."),
    ("用比较级完成句子。", "Completa con el comparativo."),
    ("预算辩论比一场音乐会长", "Un debate presupuestario dura más que un concierto"),
    ("预算比时间表复杂", "El presupuesto es más complejo que un calendario"),
    ("文化预算与农业预算同样重要", "El presupuesto de Cultura y el de Agricultura son igual de importantes"),
    ("MICRO-DRILLS · 即学即练", "MICRO-DRILLS · A PRACTICAR"),
    ("用 examine / ont rejeté / part / peut / connus 填空。",
     "Completa con examine / ont rejeté / part / peut / connus."),
    ("国民议会审议预算", "La Asamblea Nacional examina el presupuesto"),
    ("议员们否决收入部分", "Los diputados rechazaron los ingresos"),
    ("法案送交参议院", "El texto va al Senado"),
    ("日程仍可能变动", "El calendario aún puede cambiar"),
    ("结果尚未揭晓", "Los resultados aún no se conocen"),
    ("讨论｜结果未出时，该不该先公布日程？区分 prévu（计划）与 décidé（已定）。",
     "Debate: ¿anunciar un calendario antes de conocer los resultados? Distingue prévu (previsto) y décidé (decidido)."),
])

# ---------- content7: P7 ----------
rep_all("content7.py", [
    ("LANGUE EN MAIN · 精讲", "LANGUE EN MAIN · LA LENGUA EN MANO"),
    ("A2 → B2 · Les phrases de la semaine · 本周金句",
     "A2 → B2 · Les phrases de la semaine · FRASES DE LA SEMANA"),
    ("NIVEAU A2 · 基础", "NIVEAU A2 · NIVEL BÁSICO"),
    ("NIVEAU B1 · 进阶", "NIVEAU B1 · NIVEL INTERMEDIO"),
    ("NIVEAU B2 · 挑战", "NIVEAU B2 · DESAFÍO"),
    ("BOÎTE À OUTILS · 工具箱", "BOÎTE À OUTILS · RECURSOS"),
    ("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。",
     "Recursos: tres frases para llevar, una por nivel; todas salen de los artículos de este número: releer el original es lo más eficaz."),
    ("LES PHRASES DE LA SEMAINE · 本周金句（全部出自本期文章）",
     "LES PHRASES DE LA SEMAINE · FRASES DE LA SEMANA"),
    ("每句一个语法点 + 一道小题 · 答案见第 8 版",
     "Un punto de gramática y un ejercicio por frase · Respuestas en la página 8"),
    ("语法点｜reprendre：复课、重新开始（pause 后）。",
     "Gramática: reprendre — volver al cole, volver a empezar (tras una pausa)."),
    ("语法点｜ne...pas encore：尚未、还不。", "Gramática: ne...pas encore — todavía no."),
    ("pas encore 尚未", "pas encore = todavía no"),
    ("语法点｜passé composé 代动词：se + être + 过去分词。",
     "Gramática: passé composé reflexivo — se + être + participio."),
    ("语法点｜comparatif：plus + 形容词，ou 对举。",
     "Gramática: comparatif — plus + adjetivo, ou contrapone."),
    ("plus + 形容词", "plus + adjetivo"),
    ("语法点｜se promener：代动词，漫步、穿梭。",
     "Gramática: se promener — reflexivo, pasear, moverse."),
    ("语法点｜pouvoir + 动词原形：可能、可以。",
     "Gramática: pouvoir + infinitivo — poder, ser posible."),
    ("语法点｜se jouer：决出胜负、上演（代动词）。",
     "Gramática: se jouer — decidirse, celebrarse (reflexivo)."),
    ("语法点｜rencontrer：与观众见面；y 代指地点。",
     "Gramática: rencontrer — encontrarse con el público; y remite al lugar."),
    ("CLINIQUE DES ERREURS · 易错诊所", "CLINIQUE DES ERREURS · CLÍNICA"),
    ("每句有一处错误：找出来并改正。",
     "Cada frase tiene un error: encuéntralo y corrígelo."),
    ("jamais + de：否定句中 des 变 de", "jamais + de: en la negación, des pasa a de"),
    ("主谓一致：créateurs 复数 → rencontrent，不是 rencontre",
     "Concordancia: créateurs (plural) → rencontrent, no rencontre"),
    ("虚拟式：il examine，不加 s", "Subjuntivo: il examine, sin s"),
    ("事实：决赛在 8 日，不是 7 日", "Dato: la final es el 8, no el 7"),
    ("LE COURRIER DES LECTEURS · 读者园地", "LE COURRIER DES LECTEURS · EL RINCÓN DE LOS LECTORES"),
    ("小墨点评｜编辑部示例：周末叙事用 passé composé 很稳，分号连接两天值得学。下期读者园地将点评真实投稿。",
     "Comentario de Xiao Mo (ejemplo): el passé composé es seguro; el punto y coma une ambos días. El próximo rincón comentará textos reales."),
    ("编辑部说明：截至付印，编辑部尚未收到 VOL.2 第 8 版的投稿作文（W44 未出刊），故本期刊登标注明确的编辑部示例；VOL.4 将兑现点评真实投稿的承诺。",
     "Nota de la redacción: no llegó ningún texto del VOL.2 antes del cierre (no hubo número W44); aquí va un ejemplo de la redacción. El VOL.4 comentará textos reales. ¡Envíanos tu carta o tu mejor texto de la página 8 para el VOL.4!"),
    ("LA SEMAINE PROCHAINE · VOL.4 下周预告", "LA SEMAINE PROCHAINE · VOL.4 LA SEMANA QUE VIENE"),
    ("下周：参议院审议社保预算、11 月 11 日停战纪念日、迪耶普扇贝集市；还有你们的来信！",
     "La semana que viene: el Senado examina el presupuesto social, 11 de noviembre Día del Armisticio, 14–15 de noviembre mercado de Dieppe… ¡y por fin vuestras cartas!"),
])

# ---------- content8: P8 ----------
# Printed-note set measured from the core P8 (tools/p8.py extract --json):
# 97 numbers; the other 53 are bare keys and stay bare.
PRINT_NOTES = [1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
rep("content8.py",
    'for pg, grp in groupby(REG, key=lambda e: e["page"]):',
    'PRINT_NOTES = ' + repr(PRINT_NOTES) + '\nfor pg, grp in groupby(REG, key=lambda e: e["page"]):', 1)
rep("content8.py",
    'if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):',
    'if e["note"] and e["n"] in PRINT_NOTES:', 1)
rep("content8.py", 's += f"（{e[\'note\']}）"', 's += f" ({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— PÁGINA {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep_all("content8.py", [
    ("EXERCICES & RÉPONSES · 练习与答案", "EXERCICES & RÉPONSES · EJERCICIOS Y RESPUESTAS"),
    ("综合评估 ÉVALUATION · 答案在本版下方",
     "EVALUACIÓN · LAS RESPUESTAS, AL FINAL DE ESTA PÁGINA"),
    ("11 月 8 日 2026 是星期日", "El 8 de noviembre de 2026 es domingo"),
    ("去南泰尔看决赛", "Ir a Nanterre a ver la final"),
    ("决赛选手周六晚才揭晓", "Los finalistas solo se conocen el sábado por la noche"),
    ("品尝语境（un régal）→ goûté", "Contexto de degustación (un régal) → goûté"),
    ("se promener 漫步", "se promener = pasear"),
    ("avoir + 过去分词 goûté（不配合）", "avoir + participio goûté (sin concordancia)"),
    ("les finales 主语复数 → ont lieu", "les finales (plural) → ont lieu"),
    ("elle écrit 她写", "elle écrit = ella escribe"),
    ("A · TEXTE À TROUS · 完形填空", "A · TEXTE À TROUS · COMPLETAR"),
    ("选项：", "Opciones:"),
    ("B · CHOIX MULTIPLE · 单选", "B · CHOIX MULTIPLE · OPCIONES"),
    ("7 nov. = samedi（最后夜场）", "7 nov. = sábado (último evento nocturno)"),
    ("s'intéresser aux（à+les）", "s'intéresser aux (à + les)"),
    ("si + imparfait（未完成过去时）→ conditionnel présent（条件式现在时）；j' 是 je 在元音前的省音",
     "si + imparfait → conditionnel présent; j' es je ante vocal (elisión)"),
    ("主语 ce programme 三单 → semble", "Sujeto ce programme (3.ª persona singular) → semble"),
    ("将来时 aura lieu（决赛在周日）", "Futuro aura lieu (la final es el domingo)"),
    ("三区同日复课", "Las tres zonas vuelven el mismo día"),
    ("扇贝节在 11 月 7–8 日", "La fiesta de la vieira, el 7–8 de noviembre"),
    ("C · LECTURE · 阅读理解", "C · LECTURE · LECTURA"),
    ("夜场 19 点至凌晨 1 点", "Evento nocturno de 19 h a 1 h"),
    ("小徽章给小 Léo 驱怪", "La insignia es para el pequeño Léo, contra monstruos"),
    ("周日先看决赛再吃扇贝", "Domingo: primero ver la final, luego comer vieiras"),
    ("周日晚上早睡因为周一上学", "Domingo por la noche, a dormir temprano porque el lunes hay cole"),
    ("周一是上学日（复课后正常周一）", "El lunes es día de cole (lunes normal tras las vacaciones)"),
    ("D · PHRASES · 完成句子与转换", "D · PHRASES · CONSTRUIR FRASES"),
    ("aller + 原形（futur proche）", "aller + infinitivo (futur proche)"),
    ("si + 半过去时 venais", "si + imparfait (venais)"),
    ("passé composé : a + 过去分词", "passé composé: a + participio"),
    ("selon moi = 在我看来", "selon moi = en mi opinión"),
    ("il est prévu que + 虚拟式", "il est prévu que + subjuntivo"),
    ("E · TRADUCTION · 翻译", "E · TRADUCTION · TRADUCCIÓN"),
    # Re-aimed translation items (W43 precedent): E1 flips to FR->ES;
    # E2-E5 stems become Spanish, French keys unchanged.
    ("读一份日程，本身就是在了解法国。", "Leer un programa ya es entender Francia."),
    ("lire un programme = 读日程", "lire un programme = leer un programa"),
    ("Traduisez : « Lire un programme, c'est déjà comprendre la France. »",
     "Traduce al español: « Lire un programme, c'est déjà comprendre la France. »"),
    ("比较级 plus vite + court", "Comparativo: plus vite + court"),
    ("Traduisez : 他跑得比他哥哥更快。",
     "Traduce al francés: Corre más rápido que su hermano."),
    ("Traduisez : 学生们自 10 月 17 日起就在放假。",
     "Traduce al francés: Los alumnos están de vacaciones desde el 17 de octubre."),
    ("Traduisez : 今晚，我们要准备书包。",
     "Traduce al francés: Esta noche vamos a preparar nuestras mochilas."),
    ("ne...pas encore = 尚未", "ne...pas encore = todavía no"),
    ("Traduisez : 人们尚不知道决赛选手是谁。",
     "Traduce al francés: Todavía no se sabe quiénes son los finalistas."),
    ("F · LES MOTS · 词汇配对", "F · LES MOTS · VOCABULARIO"),
    ("tournoi=赛事 a", "tournoi=torneo a"),
    ("nocturne=夜场 b", "nocturne=evento nocturno b"),
    ("budget=预算 c", "budget=presupuesto c"),
    ("coquille=扇贝 d", "coquille=vieira d"),
    ("festival=音乐节 e", "festival=festival e"),
    ("G · DIALOGUE · 对话补全", "G · DIALOGUE · DIÁLOGO"),
    ("11 月 7 日是星期六", "El 7 de noviembre es sábado"),
    ("在市场买扇贝", "Comprar vieiras en el mercado"),
    ("goûter 品尝（原形）", "goûter = probar (infinitivo)"),
    ("à la portaise 是一种做法", "à la portaise es una forma de prepararlas"),
    ("Bon week-end ! 周末愉快", "Bon week-end ! = ¡Buen fin de semana!"),
    ('reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")',
     'reg_ex("B1", "写作", "Pregunta abierta — los puntos están en el recuadro de escritura y el modelo, en el recuadro MODÈLE de esta página", "se puntúa según los puntos")'),
    ("H · ÉCRITURE · 写作", "H · ÉCRITURE · ESCRIBIR"),
    ("用法语写 80–100 词：我的 11 月 7–8 日周末。写清一场比赛、一个节日、一道菜。",
     "Escribe 80–100 palabras en francés: mi fin de semana del 7–8 de noviembre. Describe un partido, una fiesta y un plato. Los mejores textos aparecerán en el VOL.4 (página 7, « Le courrier des lecteurs »)."),
    ("MODÈLE · 范文", "MODÈLE · MODELO"),
    ("RÉPONSES · 全部答案与简析（第 1–8 版）",
     "RÉPONSES · TODAS LAS RESPUESTAS CON NOTAS (PÁGINAS 1–8)"),
])

# ---------- shared type/instr tokens LAST (registry only, except instr) ----------
TYPE_MAP = [
    ("完成句子", "Completar"),
    ("单选", "Opción múltiple"),
    ("句型转换", "Reescribir"),
    ("词汇配对", "Emparejar"),
    ("跟练", "Practicar"),
    ("改错", "Corregir"),
    ("完形填空", "Completar texto"),
    ("阅读判断", "Verdadero/Falso"),
    ("阅读理解", "Comprensión"),
    ("对话补全", "Completar diálogo"),
    ("翻译", "Traducir"),
    ("写作", "Escribir"),
    ("图表读数", "Leer gráfico"),
]
INSTR_MAP = [
    ('instr="把词和释义配对"', 'instr="Une palabra y definición"'),
    ('instr="填空"', 'instr="Completa"'),
    ('instr="改写"', 'instr="Reescribe"'),
    ('instr="配对"', 'instr="Une"'),
    ('instr="改错"', 'instr="Corrige"'),
]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in TYPE_MAP:
        p = os.path.join(BASE, f)
        if old in open(p, encoding="utf-8").read():
            rep(f, old, new)
    for old, new in INSTR_MAP:
        p = os.path.join(BASE, f)
        if old in open(p, encoding="utf-8").read():
            rep(f, old, new)

with open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(LOG) + "\n")
print(f"transform done, replacements: {len(LOG)}")

# ---------- FIX ROUND 2 (after round-1 render + gates) ----------
# R1 defects (all layout, no content change):
#  (a) P1 headline flow overflowed 127px (ended 1939, bottom 1812):
#      the Spanish P1 gloss wrapped longer than the core's 5 lines.
#      Shorten to single-word glosses and set the 5 frozen French
#      headline paras to 24pt / lh 1.45 (text byte-identical, only
#      presentation size/leading changes) — same remedy as FR x DE.
#  (b) P6-ex HEAD TOO WIDE: "LIRE LE CALENDRIER · LEE EL CALENDARIO"
#      measures 513.5 > 434; "LIRE LE CALENDRIER · CALENDARIO" = 430.5.
#  (c) P8 battery ended 1526 (limit 1485) and keys ended 2625
#      (limit 2545): battery paras 21 -> 20pt, battery ex gap 11 -> 6,
#      F match_set gap 14 -> 6, keys 15.5 -> 14.5pt, writing strip
#      wy 1500 -> 1540 (full FR x DE package, applied at once here
#      because the Spanish keys overflow is 80px, larger than DE's).
rep("content12.py",
    "se jouer decidirse, celebrarse · une finale final · une demi-finale semifinal · un quart de finale cuartos de final · une nocturne evento nocturno · un frisson escalofrío, emoción · la coquille Saint-Jacques vieira.",
    "se jouer decidirse · une finale final · une demi-finale semifinal · un quart de finale cuartos · une nocturne velada · un frisson emoción · la coquille Saint-Jacques vieira.", 1)
for tail in [
    "avec trois finales en même temps.",
    "ils seront connus samedi soir, après les demi-finales.",
    "un badge gratuit contre les monstres.",
    "on goûte des recettes au bord de la mer.",
    "Suite en pages 3 et 4.",
]:
    rep("content12.py", tail + '")', tail + '", 24, "serif", False, INK, 1.45)', 1)
rep("content56.py",
    "LIRE LE CALENDRIER · LEE EL CALENDARIO", "LIRE LE CALENDRIER · CALENDARIO", 1)
rep("content8.py", 'dans son cahier.", 21)', 'dans son cahier.", 20)', 1)
rep("content8.py", "c'est l'école.\", 21)", "c'est l'école.\", 20)", 1)
rep("content8.py", "— Merci !\", 21)", "— Merci !\", 20)", 1)
rep("content8.py",
    'kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)', 1)
rep("content8.py", ", size=20)", ", size=20, gap=6)", 4)
rep("content8.py", 'instr="Une")', 'instr="Une", gap=6)', 1)
rep("content8.py", "wy = 1500", "wy = 1540", 1)

with open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(LOG) + "\n")
print(f"transform done (with fix round 2), replacements: {len(LOG)}")

# ---------- FIX ROUND 3 (after round-2 render) ----------
# Round-2 remaining warning: P6-ex HEAD TOO WIDE persists because
# head() measures at 25pt, not 24pt: "LIRE LE CALENDRIER · CALENDARIO"
# is 430.5 at 24pt but 448.3 at 25pt > column width 434. Shorten to
# "LIRE LE CALENDRIER · FECHAS" = 386.1 at 25pt.
# P8 battery cursor 1487 (nominal flow bottom 1485) is NOT a defect:
# last battery ink baseline is 1446.4 (Merci !), 79.6px above the
# writing-strip rule at 1526 and 93.6px above MODÈLE top 1540 — no
# change made for it; recorded here so a later round does not
# "fix" it by moving the strip.
rep("content56.py",
    "LIRE LE CALENDRIER · CALENDARIO", "LIRE LE CALENDRIER · FECHAS", 1)

with open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(LOG) + "\n")
print(f"transform done (with fix round 3), replacements: {len(LOG)}")

# ---------- FIX ROUND 4 (after round-3 render + canonical audit) ----------
# Canonical audit: 4 NEW BOXTITLE flags, all real (pixel-adjudicated
# from the SVG geometry, not measurement artifacts):
#  (a) P1 plan-box line "Resultados de las finales: sábado noche y
#      domingo." is a single p.text line, 453.2px > 412px available
#      (1473 -> 1885), crossing the inner frame (1910). Shorten to
#      "Resultados: sábado noche y domingo." (334.6).
#  (b) P1 "DANS CE NUMÉRO · EN ESTE NÚMERO" at 24pt bold = 456.1 >
#      412. Replace with the SHIPPED W43 FR x ES form "DANS CE
#      NUMÉRO · CONTENIDO" (390.1).
#  (c) P5 "PARIS CREATOR WEEK · CREADORES" at 23pt bold = 418.4 >
#      412 (6.2px over). Replace with the single name "PARIS CREATOR
#      WEEK" (247.0) — the FR x EN round-4 precedent for this box.
#  (d) P7 reader-corner disclosure para ran 3 lines; its last line's
#      ink bottom (2265.6) passed the fixed box bottom (2258.0) by
#      7.6px. Shorten to the 2-line form below (wrap-verified at
#      19.5pt / 848px): attribution + no-VOL.2-text disclosure +
#      VOL.4 promise + explicit solicitation covering letters AND
#      best P8 texts ("tu carta o tu mejor texto de la página 8").
rep("content12.py",
    "Resultados de las finales: sábado noche y domingo.",
    "Resultados: sábado noche y domingo.", 1)
rep("content12.py",
    "DANS CE NUMÉRO · EN ESTE NÚMERO", "DANS CE NUMÉRO · CONTENIDO", 1)
rep("content56.py",
    "PARIS CREATOR WEEK · CREADORES", "PARIS CREATOR WEEK", 1)
rep("content7.py",
    "Nota de la redacción: no llegó ningún texto del VOL.2 antes del cierre (no hubo número W44); aquí va un ejemplo de la redacción. El VOL.4 comentará textos reales. ¡Envíanos tu carta o tu mejor texto de la página 8 para el VOL.4!",
    "Nota de la redacción: ningún texto del VOL.2 llegó a tiempo (no hubo W44); aquí un ejemplo. El VOL.4 comentará textos reales. ¡Envíanos tu carta o tu mejor texto de la página 8!", 1)

with open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(LOG) + "\n")
print(f"transform done (with fix round 4), replacements: {len(LOG)}")
