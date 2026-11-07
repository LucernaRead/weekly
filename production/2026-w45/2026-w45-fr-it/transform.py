# -*- coding: utf-8 -*-
"""FR x IT fan-out transform for W45 FR core build copy (VOL.3).

Rules (tools/README #17/#18): whole-string or exact-unique-literal
replacements with count assertions; value maps use bare text, never repr.
French target text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token, except the documented re-aimed P8 translation items
(E1 key/note/stem, E2-E5 stems) and the P8 printing rule (see below).
Furniture follows the SHIPPED W43 FR x IT edition
(files/weekly-report-fr-it/), which wins over any generic rule:
badge INSERTED at y=574, 22pt BRICK, centred, Italian form;
footer VOL.3 in the canonical IT template; gloss prefix "Nota — ";
short bilingual heads (TOCCA A TE, LESSICO, IL DIBATTITO, ALLENAMENTO,
LIVELLO BASE / INTERMEDIO / SFIDA, STRUMENTI, CLINICA, IL MESE,
SOMMARIO, L'ANGOLO DEI LETTORI).

P8 printed-note set: the core's rule (page 8 always, or note <= 10 chars,
or clinic/chart types) cannot survive translation, because Italian notes
are longer. Following the W43 FR x IT precedent, the edition carries
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
    rep(f, "weekly-report-w45-fr-core", "weekly-report-w45-fr-it", 1)

# ---------- bslib4: furniture + gloss prefix (W43 shipped forms, VOL.3) ----------
rep("bslib4.py",
    '"Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文"',
    '"Le Lucerna · SETTIMANALE FRANCESE VOL.3 · TESTI IN FRANCESE · SPIEGAZIONI IN ITALIANO"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} di {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Nota — " + s', 1)

# ---------- content12: P1 + P2 ----------
rep_all("content12.py", [
    ("VOL. 3 · 总第 3 期", "VOL. 3 · N. 3"),
    ("HEBDOMADAIRE EN FRANÇAIS · 每周一期 · 读法国人正在读的法语",
     "HEBDOMADAIRE EN FRANÇAIS · OGNI SETTIMANA · IL FRANCESE CHE LEGGONO I FRANCESI"),
    ("法 语 周 报 · VOL.3 · 决 赛 周 末", "SETTIMANALE IN FRANCESE · VOL.3 · WEEKEND DELLE FINALI"),
    ("周一开学 · 全法同步复课", "LUNEDÌ SI TORNA A SCUOLA · TUTTA LA FRANCIA"),
    ("大师赛开赛 · 音乐节开幕 · 详见第 2 版", "INIZIANO IL MASTERS E IL FESTIVAL · VEDI PAGINA 2"),
    ("法语正文 · 简体中文讲解 — 给简体中文读者的版本",
     "TESTI IN FRANCESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI"),
    ("SPORT · CULTURE · GASTRONOMIE · LA UNE · 决赛周末",
     "SPORT · CULTURE · GASTRONOMIE · LA UNE · WEEKEND DELLE FINALI"),
    ("se jouer 决出胜负、上演 · une finale 决赛 · une demi-finale 半决赛 · un quart de finale 四分之一决赛 · une nocturne 夜场活动 · un frisson 战栗、刺激感 · la coquille Saint-Jacques 扇贝。",
     "se jouer decidere, svolgersi · une finale finale · une demi-finale semifinale · un quart de finale quarto di finale · une nocturne evento notturno · un frisson brivido, emozione · la coquille Saint-Jacques capasanta."),
    ("LES DATES · 决赛周末日程", "LES DATES · WEEKEND DELLE FINALI"),
    ("À VOUS ! · 即学即练", "À VOUS ! · TOCCA A TE"),
    ("周日 8 日举行决赛", "Finale domenica 8 novembre"),
    ("周六 7 日晚是最后夜场", "Ultimo evento notturno sabato 7 novembre sera"),
    ("波尔诺曼底卖扇贝", "A Port-en-Bessin si vendono capesante"),
    ("周一 2 日全法复课", "Si torna a scuola lunedì 2 novembre, in tutta la Francia"),
    ("半决赛后才知道决赛选手", "I finalisti si conoscono solo dopo le semifinali"),
    ("三个决赛：网球、刺激、美味", "Tre finali: tennis, brivido, gusto"),
    ("本周日程 · 11 月 2 日至 8 日", "PROGRAMMA DELLA SETTIMANA · 2–8 NOVEMBRE"),
    ("周末决赛结果周六晚、周日揭晓。", "I risultati delle finali: sabato sera e domenica."),
    ("DANS CE NUMÉRO · 本期目录", "DANS CE NUMÉRO · SOMMARIO"),
    ("决出胜负；上演。本周末一切都将见分晓。",
     "Decidere; svolgersi. Questo fine settimana si decide tutto."),
    ("EN BREF · 快讯", "EN BREF · IN BREVE"),
    ("QUIZ ÉCLAIR · 闪电问答", "QUIZ ÉCLAIR · QUIZ LAMPO"),
    ("读头版，选出正确答案 · 答案见第 8 版",
     "Leggi la prima pagina, scegli la risposta giusta · Risposte a pagina 8"),
    ("决赛在周日 8 日", "La finale è domenica 8 novembre"),
    ("扇贝节在滨海波尔", "La festa delle capesante a Port-en-Bessin"),
    ("周一 2 日早上全区复课", "Si torna a scuola lunedì 2 novembre mattina"),
    ("最后夜场周六 7 日", "Ultimo evento notturno sabato 7 novembre"),
    ("VIE QUOTIDIENNE · 生活", "VIE QUOTIDIENNE · VITA QUOTIDIANA"),
    ("NIVEAU A2 · La rentrée · 开学复课", "NIVEAU A2 · La rentrée · RITORNO A SCUOLA"),
    ("la rentrée 开学、复课 · reprendre 重新开始、复课 · un cartable 书包 · un décalage 错开、时差 · en revanche 相反、反之 · un rituel 习惯、仪式。",
     "la rentrée ritorno a scuola · reprendre ricominciare · un cartable cartella · un décalage scarto, differenza di fuso · en revanche invece, al contrario · un rituel abitudine, rito."),
    ("译注｜une valise 行李箱 · une ambiance 气氛 · le bilan 总结、盘点。",
     "Nota — une valise valigia · une ambiance atmosfera · le bilan bilancio, resoconto."),
    ("说说你的开学：周一早上你在哪里？假期读了哪本书？写两句法语寄给编辑部。",
     "Racconta il tuo ritorno a scuola: dove eri lunedì mattina? Quale libro hai letto in vacanza? Scrivi due frasi in francese alla redazione."),
    ("ET VOUS ? · 说说你自己", "ET VOUS ? · E TU?"),
    ("DIRE LA DATE · 这样说日期", "DIRE LA DATE · COSÌ SI DICE LA DATA"),
    ("lundi 2 novembre · 注意：1 日说 le premier，其余用基数词",
     "lundi 2 novembre · Attenzione: il 1° si dice le premier, gli altri con i numeri cardinali"),
    ("11 月 2 日星期一 · la rentrée", "Lunedì 2 novembre · la rentrée"),
    ("11 月 3 日星期二 · votes à l'Assemblée", "Martedì 3 novembre · votes à l'Assemblée"),
    ("11 月 4 日星期三 · sorties cinéma", "Mercoledì 4 novembre · sorties cinéma"),
    ("11 月 7 日星期六 · nocturne et demis", "Sabato 7 novembre · nocturne et demis"),
    ("11 月 8 日星期日 · les finales", "Domenica 8 novembre · les finales"),
    ("EXERCICES · 第 2 版练习", "EXERCICES · ESERCIZI DI PAGINA 2"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Risposte a pagina 8 · Livelli misti; cerca per numero"),
    ("用法语补全日期（注意星期与数字）。",
     "Completa la data in francese (attenzione al giorno e al numero)."),
    ("复课在星期一", "Si torna a scuola di lunedì"),
    ("11 月 1 日说 le premier", "Il 1° novembre si dice le premier"),
    ("最后夜场在星期六", "L'ultimo evento notturno è di sabato"),
    ("决赛在星期日", "La finale è di domenica"),
    ("用 aller + 动词原形改写（最近将来时）。",
     "Riscrivi con aller + infinito (futur proche)."),
    ("读第 2 版文章，选出正确答案。",
     "Leggi l'articolo di pagina 2 e scegli la risposta giusta."),
    ("三区同一周一早上复课", "Tutte e tre le zone ricominciano lunedì mattina"),
    ("冬令时从 10 月 25 日开始", "L'ora solare è in vigore dal 25 ottobre"),
    ("11 月晚上天黑得早", "A novembre di sera fa buio presto"),
    ("rentrée=开学 a", "rentrée=ritorno a scuola a"),
    ("reprendre=重新开始 b", "reprendre=ricominciare b"),
    ("cartable=书包 c", "cartable=cartella c"),
    ("rituel=习惯 d", "rituel=abitudine d"),
])

# ---------- content34: P3 + P4 ----------
rep_all("content34.py", [
    ("CULTURE · 文化", "CULTURE · CULTURA"),
    ("NIVEAU A2 → B1 · Halloween, Toussaint · 万圣与诸圣",
     "NIVEAU A2 → B1 · Halloween, Toussaint · HALLOWEEN E OGNISSANTI"),
    ("se déguiser 变装、装扮 · un sort 魔法、恶作剧 · une ambiance 气氛 · le souvenir 回忆、纪念 · confondre 混淆 · discret 低调的、安静的。",
     "se déguiser travestirsi · un sort incantesimo, scherzo · une ambiance atmosfera · le souvenir ricordo, commemorazione · confondre confondere · discret discreto, sobrio."),
    ("判断对错（Vrai / Faux）。", "Vero o falso? (Vrai / Faux)"),
    ("万圣节在 10 月 31 日星期六", "Halloween era sabato 31 ottobre"),
    ("诸圣节墓园摆满菊花", "A Ognissanti i cimiteri sono pieni di crisantemi"),
    ("菊花绝不能当礼物送人", "I crisantemi non si regalano mai"),
    ("11 月 2 日是 jour des morts，不是诸圣节", "Il 2 novembre è jour des morts, non Ognissanti"),
    ("文中：le rire d'abord, le souvenir ensuite", "Nel testo: le rire d'abord, le souvenir ensuite"),
    ("用 déguisement / tombe / citrouille / souvenir 填空。",
     "Completa con déguisement / tombe / citrouille / souvenir."),
    ("万圣节穿变装服装", "A Halloween i bambini indossano costumi"),
    ("花放在墓碑上", "I fiori stanno sulla tomba"),
    ("南瓜是万圣节的象征", "La zucca è il simbolo di Halloween"),
    ("诸圣节是纪念之日", "Ognissanti è un giorno di commemorazione"),
    ("改写句子（用 ne...jamais / ne...plus / ne...pas）。",
     "Riscrivi le frasi (con ne...jamais / ne...plus / ne...pas)."),
    ("jamais + de（无冠词变化）", "jamais + de (senza cambio di articolo)"),
    ("ne...plus = 不再", "ne...plus = non più"),
    ("n'est pas = 不是", "n'est pas = non è"),
    ("即学即练 · 公园万圣节小题。", "Allenamento rapido · Domande su Halloween al parco."),
    ("周六 7 日是最后夜场", "Sabato 7: ultimo evento notturno"),
    ("敏感儿童有免费驱怪徽章", "I bambini sensibili ricevono un distintivo gratuito contro i mostri"),
    ("阿斯泰里克斯公园在 Plailly", "Il Parc Astérix si trova a Plailly"),
    ("Peur sur le Parc 10 月 3 日至 11 月 8 日", "Peur sur le Parc dal 3 ottobre all'8 novembre"),
    ("恐惧等级用颜色区分", "I livelli di paura si distinguono per colore"),
    ("夜场从 19 点到凌晨 1 点", "L'evento notturno dura dalle 19 all'1"),
    ("LES MOTS DES FÊTES · 节日词表", "LES MOTS DES FÊTES · LESSICO"),
    ("un saint — 圣人", "un saint — santo"),
    ("un cimetière — 墓园", "un cimetière — cimitero"),
    ("une tombe — 坟墓", "une tombe — tomba"),
    ("un jour férié — 公共假日", "un jour férié — giorno festivo"),
    ("se souvenir — 纪念、想起", "se souvenir — ricordare, commemorare"),
    ("un déguisement — 变装服装", "un déguisement — costume"),
    ("une citrouille — 南瓜", "une citrouille — zucca"),
    ("un bonbon — 糖果", "un bonbon — caramella"),
    ("un fantôme — 幽灵", "un fantôme — fantasma"),
    ("un sort — 魔法、诅咒", "un sort — incantesimo, maledizione"),
    ("10 月 3 日至 11 月 8 日，12 场夜场；最后夜场 11 月 7 日；白天 10 点至 19 点开放。",
     "Dal 3 ottobre all'8 novembre: 12 eventi notturni, l'ultimo sabato 7 novembre. Di giorno aperto dalle 10 alle 19."),
    ("DATES À RETENIR · 本周日历", "DATES À RETENIR · IL MESE"),
    ("注意：迪耶普扇贝集市在 11 月 14–15 日，不在本周。",
     "Attenzione: Dieppe solo il 14–15 novembre, non questa settimana."),
    ("SPORT · 体育", "SPORT"),
    ("À VOUS ! · 即学即练", "À VOUS ! · TOCCA A TE"),
    ("决赛在周日 8 日", "Finale domenica 8 novembre"),
    ("LE DÉBAT · 讨论", "LE DÉBAT · IL DIBATTITO"),
    ("un tournoi 锦标赛、赛事 · sur dur 硬地球场 · en salle 室内 · un tableau principal 正赛签表 · le tenant du titre 卫冕冠军 · basculer 逆转、倾斜 · les tribunes 看台。",
     "un tournoi torneo · sur dur sul cemento · en salle al coperto · un tableau principal tabellone principale · le tenant du titre detentore del titolo · basculer ribaltarsi, inclinarsi · les tribunes tribune."),
    ("读第 4 版文章，选出正确答案。",
     "Leggi l'articolo di pagina 4 e scegli la risposta giusta."),
    ("大师赛在室内硬地球场举行", "Il Masters si gioca al coperto sul cemento"),
    ("2025 年卫冕冠军是辛纳", "Il detentore del titolo 2025 è Sinner"),
    ("法甲第十轮大场面：朗斯–马赛", "Big match della 10ª giornata di Ligue 1: Lens – Marsiglia"),
    ("周日 8 日还有轮椅单打决赛（中午）", "Domenica 8: anche finale singolare in carrozzina (mezzogiorno)"),
    ("把网球词和释义配对。", "Abbina le parole del tennis ai significati."),
    ("tournoi=赛事 a", "tournoi=torneo a"),
    ("raquette=球拍 b", "raquette=racchetta b"),
    ("tribunes=看台 c", "tribunes=tribune c"),
    ("tenant=卫冕者 d", "tenant=detentore d"),
    ("用比较级完成句子（plus / moins）。", "Completa con il comparativo (plus / moins)."),
    ("室内球速更快", "Al coperto la palla è più veloce"),
    ("大师赛是仅次于大满贯的级别", "Un Masters 1000 è il livello sotto i Grande Slam"),
    ("室内赛季比室外短", "La stagione al coperto è più corta di quella estiva"),
    ("译注｜un choc 强强对决 · recevoir 迎战、接待 · familier 熟悉的。",
     "Nota — un choc big match · recevoir affrontare, accogliere · familier familiare."),
    ("« Allez ! » — 加油！ · « Quelle action ! » — 好球！",
     "« Allez ! » — Forza! · « Quelle action ! » — Che azione!"),
    ("« Il marque ! » — 他得分了！ · « C'est gagné ! » — 赢了！",
     "« Il marque ! » — Segna! · « C'est gagné ! » — Vinto!"),
    ("« Quel point ! » — 好球！（网球） · « Balle de match ! » — 赛点！",
     "« Quel point ! » — Che punto! (tennis) · « Balle de match ! » — Match point!"),
    ("LES MOTS DU TENNIS · 网球词表", "LES MOTS DU TENNIS · LESSICO"),
    ("le tennis — 网球", "le tennis — tennis"),
    ("une balle — 球", "une balle — palla"),
    ("un set — 一盘", "un set — set"),
    ("un match — 比赛", "un match — partita"),
    ("un point — 一分", "un point — punto"),
    ("la finale — 决赛", "la finale — finale"),
    ("un adversaire — 对手", "un adversaire — avversario"),
    ("un titre — 冠军头衔", "un titre — titolo"),
    ("À SUIVRE · 拭目以待", "À SUIVRE · CONTINUA"),
    ("MICRO-DRILLS · 即学即练", "MICRO-DRILLS · ALLENAMENTO"),
    ("用 finale / quarts / demi-finales / tableau / fauteuil / choc 填空。",
     "Completa con finale / quarts / demi-finales / tableau / fauteuil / choc."),
    ("四分之一决赛在周五", "Quarti di finale venerdì"),
    ("半决赛在周六", "Semifinali sabato"),
    ("单打决赛在周日", "Finale singolare domenica"),
    ("正赛签表从周一开始", "Il tabellone principale inizia lunedì"),
    ("轮椅赛事周五至周日", "Torneo in carrozzina da venerdì a domenica"),
    ("朗斯–马赛是周末焦点战", "Lens – Marsiglia è il big match del fine settimana"),
    ("事先不知道决赛选手，是更刺激还是更扫兴？写两句支持、两句反对。",
     "Finalisti sconosciuti in anticipo: più emozionante o più frustrante? Scrivi due frasi a favore e due contro."),
])

# ---------- content56: P5 + P6 ----------
rep_all("content56.py", [
    ("JEUNESSE & MUSIQUE · 青年", "JEUNESSE & MUSIQUE · GIOVANI"),
    ("NIVEAU B1 · Pitchfork Paris · 音乐节", "NIVEAU B1 · Pitchfork Paris · FESTIVAL"),
    ("un lieu 场所、场地 · une affiche 海报 · les paroles 歌词 · donner le ton 定调子 · se promener 漫步、穿梭 · pile 正好、恰好。",
     "un lieu luogo, sede · une affiche manifesto · les paroles testi delle canzoni · donner le ton dare il tono · se promener passeggiare, spostarsi · pile esattamente, proprio."),
    ("À VOUS ! · 即学即练", "À VOUS ! · TOCCA A TE"),
    ("读第 5 版文章，选出正确答案。",
     "Leggi l'articolo di pagina 5 e scegli la risposta giusta."),
    ("音乐节 11 月 2–8 日，整整一周", "Festival dal 2 all'8 novembre, una settimana intera"),
    ("15 届音乐节", "15ª edizione del festival"),
    ("Avant-Garde 在巴士底各场地，周四至周六", "Avant-Garde alla Bastiglia, da giovedì a sabato"),
    ("俱乐部之夜在周五、周六", "Serate club venerdì e sabato"),
    ("开幕夜：Headache、Iceage、DIIV", "Serata di apertura: Headache, Iceage, DIIV"),
    ("用 lieux / paroles / affiche / ambiance / danse / découvre 填空。",
     "Completa con lieux / paroles / affiche / ambiance / danse / découvre."),
    ("10 个场地", "Dieci sedi"),
    ("歌词也是法语学习材料", "I testi aiutano a imparare il francese"),
    ("海报上写着演出信息", "Sul manifesto ci sono i nomi dei gruppi"),
    ("每晚气氛各不相同", "Ogni sera un'atmosfera diversa"),
    ("音乐节上人们跳舞", "Al festival si balla"),
    ("发现不认识的乐队", "Scoprire gruppi sconosciuti"),
    ("把音乐词和释义配对。", "Abbina le parole della musica ai significati."),
    ("concert=音乐会 a", "concert=concerto a"),
    ("scène=舞台 b", "scène=palco b"),
    ("groupe=乐队 c", "groupe=gruppo c"),
    ("billet=门票 d", "billet=biglietto d"),
    ("补全对话（音乐节门口）。", "Completa il dialogo (all'ingresso del festival)."),
    ("今晚演出的乐队", "Il gruppo di stasera"),
    ("买两张票", "Comprare due biglietti"),
    ("MOTS DE LA MUSIQUE · 音乐词表", "MOTS DE LA MUSIQUE · LESSICO"),
    ("un festival — 音乐节", "un festival — festival"),
    ("un concert — 音乐会", "un concert — concerto"),
    ("une chanson — 歌曲", "une chanson — canzone"),
    ("un chanteur — 歌手", "un chanteur — cantante"),
    ("danser — 跳舞", "danser — ballare"),
    ("écouter — 聆听", "écouter — ascoltare"),
    ("une salle — 演出厅", "une salle — sala"),
    ("le public — 观众", "le public — pubblico"),
    ("PARIS CREATOR WEEK · 创作者周", "PARIS CREATOR WEEK · CREATOR"),
    ("11 月 4–5 日拉维莱特：创作者周，线上创作者与观众线下见面。",
     "4–5 novembre a La Villette: Creator Week — i creator online incontrano il pubblico dal vivo."),
    ("LE DÉBAT · 讨论", "LE DÉBAT · IL DIBATTITO"),
    ("十个场地的音乐节，比单一大场馆更好吗？你听什么音乐学法语？",
     "Un festival in dieci sedi: meglio di un'unica grande sala? Quale musica ascolti per imparare il francese?"),
    ("POLITIQUE & CHIFFRES · 时事", "POLITIQUE & CHIFFRES · ATTUALITÀ"),
    ("NIVEAU B2 · Budget 2027 · 预算周", "NIVEAU B2 · Budget 2027 · SETTIMANA DEL BILANCIO"),
    ("un budget 预算 · une mission （预算）分项 · un député 国民议会议员 · rejeter 否决 · à l'unanimité 一致通过/否决 · un amendement 修正案。",
     "un budget bilancio · une mission capitolo di bilancio · un député deputato · rejeter respingere · à l'unanimité all'unanimità · un amendement emendamento."),
    ("LE CALENDRIER PRÉVU · 计划中的投票日程（结果未出）",
     "LE CALENDRIER PRÉVU · PREVISTO, SENZA RISULTATI"),
    ("本页日程为计划安排，结果尚未产生，下期跟进。",
     "Questo calendario è provvisorio; i risultati seguiranno nel prossimo numero."),
    ("LIRE LE CALENDRIER · 读日程", "LIRE LE CALENDRIER · LEGGERE"),
    ("读上图日程，选出正确答案。",
     "Leggi il calendario sopra e scegli la risposta giusta."),
    ("周二 3 日：文化与媒体", "Martedì 3: cultura e media"),
    ("周三 4 日：农业", "Mercoledì 4: agricoltura"),
    ("周四 5 日：国土协调与科研", "Giovedì 5: coesione e ricerca"),
    ("周五 6 日：公共财政与经济", "Venerdì 6: finanze pubbliche ed economia"),
    ("10 月 23 日社保预算收入被 115–1 否决",
     "Il 23 ottobre: entrate del bilancio sociale respinte 115 a 1"),
    ("参议院从 11 月 9 日起审议", "Il Senato esamina dal 9 novembre"),
    ("LES MOTS · 词汇", "LES MOTS · LESSICO"),
    ("député=议员 a", "député=deputato a"),
    ("rejeter=否决 b", "rejeter=respingere b"),
    ("vote=投票 c", "vote=voto c"),
    ("amendement=修正案 d", "amendement=emendamento d"),
    ("« Le texte part au Sénat. » — 法案送交参议院。",
     "« Le texte part au Sénat. » — Il testo va al Senato."),
    ("« Ce calendrier peut encore bouger. » — 日程仍可能变动。",
     "« Ce calendrier peut encore bouger. » — Il calendario può ancora cambiare."),
    ("« Les résultats ne sont pas connus. » — 结果尚未揭晓。",
     "« Les résultats ne sont pas connus. » — I risultati non sono ancora noti."),
    ("译注｜prévu 预定的、计划的 · réaliser 实现、完成 · distinguer 区分。",
     "Nota — prévu previsto, programmato · réaliser realizzare, attuare · distinguer distinguere."),
    ("用比较级完成句子。", "Completa con il comparativo."),
    ("预算辩论比一场音乐会长", "Un dibattito sul bilancio è più lungo di un concerto"),
    ("预算比时间表复杂", "Il bilancio è più complesso di un calendario"),
    ("文化预算与农业预算同样重要", "Il bilancio della cultura e quello dell'agricoltura sono ugualmente importanti"),
    ("MICRO-DRILLS · 即学即练", "MICRO-DRILLS · ALLENAMENTO"),
    ("用 examine / ont rejeté / part / peut / connus 填空。",
     "Completa con examine / ont rejeté / part / peut / connus."),
    ("国民议会审议预算", "L'Assemblea nazionale esamina il bilancio"),
    ("议员们否决收入部分", "I deputati hanno respinto le entrate"),
    ("法案送交参议院", "Il testo va al Senato"),
    ("日程仍可能变动", "Il calendario può ancora cambiare"),
    ("结果尚未揭晓", "I risultati non sono ancora noti"),
    ("讨论｜结果未出时，该不该先公布日程？区分 prévu（计划）与 décidé（已定）。",
     "Discussione: si deve annunciare un calendario prima dei risultati? Distingui prévu (previsto) e décidé (deciso)."),
])

# ---------- content7: P7 ----------
rep_all("content7.py", [
    ("LANGUE EN MAIN · 精讲", "LANGUE EN MAIN · LINGUA"),
    ("A2 → B2 · Les phrases de la semaine · 本周金句",
     "A2 → B2 · Les phrases de la semaine · FRASI DELLA SETTIMANA"),
    ("NIVEAU A2 · 基础", "NIVEAU A2 · LIVELLO BASE"),
    ("NIVEAU B1 · 进阶", "NIVEAU B1 · INTERMEDIO"),
    ("NIVEAU B2 · 挑战", "NIVEAU B2 · SFIDA"),
    ("BOÎTE À OUTILS · 工具箱", "BOÎTE À OUTILS · STRUMENTI"),
    ("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。",
     "Strumenti: tre frasi da portare con sé, una per livello; tutte le frasi vengono dagli articoli di questo numero — rileggerle nell'originale è il modo migliore."),
    ("LES PHRASES DE LA SEMAINE · 本周金句（全部出自本期文章）",
     "LES PHRASES DE LA SEMAINE · FRASI DELLA SETTIMANA"),
    ("每句一个语法点 + 一道小题 · 答案见第 8 版",
     "Per ogni frase un punto di grammatica + un esercizio · Risposte a pagina 8"),
    ("语法点｜reprendre：复课、重新开始（pause 后）。",
     "Grammatica: reprendre — tornare a scuola, ricominciare (dopo una pausa)."),
    ("语法点｜ne...pas encore：尚未、还不。", "Grammatica: ne...pas encore — non ancora."),
    ("pas encore 尚未", "pas encore = non ancora"),
    ("语法点｜passé composé 代动词：se + être + 过去分词。",
     "Grammatica: passé composé riflessivo — se + être + participio."),
    ("语法点｜comparatif：plus + 形容词，ou 对举。",
     "Grammatica: comparatif — plus + aggettivo, ou mette a confronto."),
    ("plus + 形容词", "plus + aggettivo"),
    ("语法点｜se promener：代动词，漫步、穿梭。",
     "Grammatica: se promener — riflessivo, passeggiare, spostarsi."),
    ("语法点｜pouvoir + 动词原形：可能、可以。",
     "Grammatica: pouvoir + infinito — potere, essere possibile."),
    ("语法点｜se jouer：决出胜负、上演（代动词）。",
     "Grammatica: se jouer — decidere, svolgersi (riflessivo)."),
    ("语法点｜rencontrer：与观众见面；y 代指地点。",
     "Grammatica: rencontrer — incontrare il pubblico; y indica il luogo."),
    ("CLINIQUE DES ERREURS · 易错诊所", "CLINIQUE DES ERREURS · CLINICA"),
    ("每句有一处错误：找出来并改正。",
     "Ogni frase contiene un errore: trovalo e correggilo."),
    ("jamais + de：否定句中 des 变 de", "jamais + de: nella negazione des diventa de"),
    ("主谓一致：créateurs 复数 → rencontrent，不是 rencontre",
     "Accordo soggetto-verbo: créateurs (plurale) → rencontrent, non rencontre"),
    ("虚拟式：il examine，不加 s", "Congiuntivo: il examine, senza s"),
    ("事实：决赛在 8 日，不是 7 日", "Fatto: la finale è l'8, non il 7 novembre"),
    ("LE COURRIER DES LECTEURS · 读者园地", "LE COURRIER DES LECTEURS · L'ANGOLO DEI LETTORI"),
    ("小墨点评｜编辑部示例：周末叙事用 passé composé 很稳，分号连接两天值得学。下期读者园地将点评真实投稿。",
     "Xiao Mo commenta (testo di esempio): il passé composé è solido per raccontare il fine settimana; il punto e virgola unisce i due giorni. Nel VOL.4 commenteremo testi veri."),
    ("编辑部说明：截至付印，编辑部尚未收到 VOL.2 第 8 版的投稿作文（W44 未出刊），故本期刊登标注明确的编辑部示例；VOL.4 将兑现点评真实投稿的承诺。",
     "Nota della redazione: al momento di andare in stampa non era arrivata nessuna lettera vera dei lettori e nessun miglior testo del VOL.2 (il numero W44 non è uscito); qui pubblichiamo un esempio della redazione, chiaramente indicato. Nel VOL.4 pubblicheremo lettere vere e i migliori testi. Mandateci le vostre lettere e i vostri migliori testi!"),
    ("LA SEMAINE PROCHAINE · VOL.4 下周预告", "LA SEMAINE PROCHAINE · LA PROSSIMA SETTIMANA · VOL.4"),
    ("下周：参议院审议社保预算、11 月 11 日停战纪念日、迪耶普扇贝集市；还有你们的来信！",
     "La prossima settimana: il Senato esamina il bilancio della Sécurité sociale, l'11 novembre è l'Armistizio, il 14–15 novembre la fiera delle capesante a Dieppe — e finalmente le vostre lettere!"),
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
    'kf.para(f"— PAGINA {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep_all("content8.py", [
    ("EXERCICES & RÉPONSES · 练习与答案", "EXERCICES & RÉPONSES · ESERCIZI E RISPOSTE"),
    ("综合评估 ÉVALUATION · 答案在本版下方",
     "VALUTAZIONE · ÉVALUATION · RISPOSTE IN FONDO A QUESTA PAGINA"),
    ("11 月 8 日 2026 是星期日", "L'8 novembre 2026 è domenica"),
    ("去南泰尔看决赛", "A Nanterre per la finale"),
    ("决赛选手周六晚才揭晓", "I finalisti si conoscono solo sabato sera"),
    ("品尝语境（un régal）→ goûté", "Contesto di degustazione (un régal) → goûté"),
    ("se promener 漫步", "se promener = passeggiare"),
    ("avoir + 过去分词 goûté（不配合）", "avoir + participio goûté (senza accordo)"),
    ("les finales 主语复数 → ont lieu", "les finales (plurale) → ont lieu"),
    ("elle écrit 她写", "elle écrit = lei scrive"),
    ("A · TEXTE À TROUS · 完形填空", "A · TEXTE À TROUS · COMPLETA"),
    ("选项：", "Opzioni:"),
    ("B · CHOIX MULTIPLE · 单选", "B · CHOIX MULTIPLE · OPZIONI"),
    ("7 nov. = samedi（最后夜场）", "7 nov. = sabato (ultimo evento notturno)"),
    ("s'intéresser aux（à+les）", "s'intéresser aux (à + les)"),
    ("si + imparfait（未完成过去时）→ conditionnel présent（条件式现在时）；j' 是 je 在元音前的省音",
     "si + imparfait → conditionnel présent; j' è je davanti a vocale (elisione)"),
    ("主语 ce programme 三单 → semble", "Soggetto ce programme (3ª persona singolare) → semble"),
    ("将来时 aura lieu（决赛在周日）", "Futuro aura lieu (finale domenica)"),
    ("三区同日复课", "Tutte e tre le zone ricominciano lo stesso giorno"),
    ("扇贝节在 11 月 7–8 日", "Festa delle capesante il 7–8 novembre"),
    ("C · LECTURE · 阅读理解", "C · LECTURE · LETTURA"),
    ("夜场 19 点至凌晨 1 点", "Evento notturno dalle 19 all'1"),
    ("小徽章给小 Léo 驱怪", "Il distintivo è per il piccolo Léo, contro i mostri"),
    ("周日先看决赛再吃扇贝", "Domenica: prima la finale, poi le capesante"),
    ("周日晚上早睡因为周一上学", "Domenica sera a letto presto, perché lunedì c'è scuola"),
    ("周一是上学日（复课后正常周一）", "Lunedì è giorno di scuola (dopo le vacanze, lunedì normale)"),
    ("D · PHRASES · 完成句子与转换", "D · PHRASES · COSTRUISCI FRASI"),
    ("aller + 原形（futur proche）", "aller + infinito (futur proche)"),
    ("si + 半过去时 venais", "si + imparfait (venais)"),
    ("passé composé : a + 过去分词", "passé composé: a + participio"),
    ("selon moi = 在我看来", "selon moi = secondo me"),
    ("il est prévu que + 虚拟式", "il est prévu que + congiuntivo"),
    ("E · TRADUCTION · 翻译", "E · TRADUCTION · TRADUZIONE"),
    # Re-aimed translation items (W43 precedent): E1 flips to FR->IT;
    # E2-E5 stems become Italian, French keys unchanged.
    ("读一份日程，本身就是在了解法国。", "Leggere un programma è già capire la Francia."),
    ("lire un programme = 读日程", "lire un programme = leggere un programma"),
    ("Traduisez : « Lire un programme, c'est déjà comprendre la France. »",
     "Traduci in italiano: « Lire un programme, c'est déjà comprendre la France. »"),
    ("比较级 plus vite + court", "comparativo: plus vite + court"),
    ("Traduisez : 他跑得比他哥哥更快。",
     "Traduci in francese: Corre più veloce di suo fratello."),
    ("Traduisez : 学生们自 10 月 17 日起就在放假。",
     "Traduci in francese: Gli studenti sono in vacanza dal 17 ottobre."),
    ("Traduisez : 今晚，我们要准备书包。",
     "Traduci in francese: Stasera prepariamo le cartelle."),
    ("ne...pas encore = 尚未", "ne...pas encore = non ancora"),
    ("Traduisez : 人们尚不知道决赛选手是谁。",
     "Traduci in francese: Non si conoscono ancora i finalisti."),
    ("F · LES MOTS · 词汇配对", "F · LES MOTS · VOCABOLARIO"),
    ("tournoi=赛事 a", "tournoi=torneo a"),
    ("nocturne=夜场 b", "nocturne=evento notturno b"),
    ("budget=预算 c", "budget=bilancio c"),
    ("coquille=扇贝 d", "coquille=capasanta d"),
    ("festival=音乐节 e", "festival=festival e"),
    ("G · DIALOGUE · 对话补全", "G · DIALOGUE · DIALOGO"),
    ("11 月 7 日是星期六", "Il 7 novembre è sabato"),
    ("在市场买扇贝", "Al mercato comprare capesante"),
    ("goûter 品尝（原形）", "goûter = assaggiare (infinito)"),
    ("à la portaise 是一种做法", "à la portaise è un modo di cucinare"),
    ("Bon week-end ! 周末愉快", "Bon week-end ! = Buon fine settimana!"),
    ('reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")',
     'reg_ex("B1", "Scrittura", "Domanda aperta — i punti sono nel riquadro di scrittura e il modello è nel riquadro MODÈLE di questa pagina", "si valuta in base ai punti")'),
    ("H · ÉCRITURE · 写作", "H · ÉCRITURE · SCRITTURA"),
    ("用法语写 80–100 词：我的 11 月 7–8 日周末。写清一场比赛、一个节日、一道菜。",
     "Scrivete in francese 80–100 parole: il mio fine settimana del 7–8 novembre. Descrivete una partita, una festa, un piatto. I migliori testi appariranno nel VOL.4 (pagina 7, « Le courrier des lecteurs »)."),
    ("MODÈLE · 范文", "MODÈLE · MODELLO"),
    ("RÉPONSES · 全部答案与简析（第 1–8 版）",
     "RÉPONSES · TUTTE LE RISPOSTE CON NOTE (PAGINE 1–8)"),
])

# ---------- shared type/instr tokens LAST (registry only, except instr) ----------
TYPE_MAP = [
    ("完成句子", "Completamento"),
    ("单选", "Scelta multipla"),
    ("句型转换", "Trasformazione"),
    ("词汇配对", "Abbinamento"),
    ("跟练", "Esercizio guidato"),
    ("改错", "Correzione errori"),
    ("完形填空", "Completamento testo"),
    ("阅读判断", "Vero/Falso"),
    ("阅读理解", "Comprensione"),
    ("对话补全", "Completamento dialogo"),
    ("翻译", "Traduzione"),
    ("写作", "Scrittura"),
    ("图表读数", "Lettura dati"),
]
INSTR_MAP = [
    ('instr="把词和释义配对"', 'instr="Abbina"'),
    ('instr="填空"', 'instr="Completa"'),
    ('instr="改写"', 'instr="Riscrivi"'),
    ('instr="配对"', 'instr="Abbina"'),
    ('instr="改错"', 'instr="Correggi"'),
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

# ---------- FIX ROUND 1 (2026-10-28, after round-1 render + gates) ----------
# Round-1 defects (all layout, no content change to French text):
#  (a) P1 headline FLOW OVERFLOW 127px into row B (ended 1939 vs bottom
#      1812): the Italian P1 gloss wrapped longer than the core's.
#      Shorten the gloss to single-word glosses and set the 5 frozen
#      French headline paras to 24pt / lh 1.45 (text byte-identical,
#      only presentation size/leading changes; FR x DE precedent).
#  (b) P1 box titles over borders: LES DATES title 1428 > 1423 and the
#      agenda title 1922.2 > 1885 (frame-line hit). Shorten both.
#  (c) P2 ET VOUS box spilled past the date-section rule (1557): the
#      Italian ET VOUS para wrapped to 4 lines (core Chinese: 2).
#      Shorten to a 2-line Italian para; box bottom returns to core.
#  (d) P2 date header note too long (starts 1107, crosses the ET VOUS
#      box border 1451 in the audit's assignment): shorten so it
#      starts at 1496.5, inside the right column.
#  (e) P3 word-list item 'se souvenir — ricordare, commemorare'
#      1885.8 > 1885 (0.8px): shorten to 'ricordare'.
#  (f) P7 reader disclosure 4 lines spilled past the reader box bottom
#      (2258) and under the teaser rect (COVER 100%): shorten to a
#      2-line Italian disclosure that still states all three facts
#      (no real letters, no best P8 texts, both deferred to VOL.4)
#      plus the imperative call covering both letters and best texts.
#  (g) P7 Italian teaser 3 lines ends baseline 2522 (ink ~2528, tight
#      vs 2540): shorten to 2 lines.
#  (h) P8 battery ended 1526 (limit 1485) and keys ended 2605 (limit
#      2545): battery paras 21pt -> 20pt, battery ex gap -> 6, F
#      match gap -> 6, keys 15.5pt -> 14.5pt (FR x DE precedent set;
#      wy shift held for round 2 if still over).
rep("content12.py",
    "se jouer decidere, svolgersi · une finale finale · une demi-finale semifinale · un quart de finale quarto di finale · une nocturne evento notturno · un frisson brivido, emozione · la coquille Saint-Jacques capasanta.",
    "se jouer decidere · une finale finale · une demi-finale semifinale · un quart de finale quarto di finale · une nocturne evento notturno · un frisson brivido · la coquille Saint-Jacques capasanta.", 1)
for tail in [
    "avec trois finales en même temps.",
    "ils seront connus samedi soir, après les demi-finales.",
    "un badge gratuit contre les monstres.",
    "on goûte des recettes au bord de la mer.",
    "Suite en pages 3 et 4.",
]:
    rep("content12.py", tail + '")', tail + '", 24, "serif", False, INK, 1.45)', 1)
rep("content12.py", "LES DATES · WEEKEND DELLE FINALI", "LES DATES · WEEKEND FINALI", 1)
rep("content12.py", "PROGRAMMA DELLA SETTIMANA · 2–8 NOVEMBRE", "PIANO SETTIMANALE · 2–8 NOVEMBRE", 1)
rep("content12.py",
    "Racconta il tuo ritorno a scuola: dove eri lunedì mattina? Quale libro hai letto in vacanza? Scrivi due frasi in francese alla redazione.",
    "Lunedì mattina: dove eravate, quale libro? Due frasi alla redazione!", 2)
rep("content12.py",
    "lundi 2 novembre · Attenzione: il 1° si dice le premier, gli altri con i numeri cardinali",
    "lundi 2 novembre · il 1° si dice le premier", 1)
rep("content34.py", "se souvenir — ricordare, commemorare", "se souvenir — ricordare", 1)
rep("content7.py",
    "Nota della redazione: al momento di andare in stampa non era arrivata nessuna lettera vera dei lettori e nessun miglior testo del VOL.2 (il numero W44 non è uscito); qui pubblichiamo un esempio della redazione, chiaramente indicato. Nel VOL.4 pubblicheremo lettere vere e i migliori testi. Mandateci le vostre lettere e i vostri migliori testi!",
    "Nota della redazione: ancora nessuna lettera vera né migliori testi (W44 non uscito); è un esempio. Nel VOL.4 i veri! Mandateci lettere e migliori testi!", 1)
rep("content7.py",
    "La prossima settimana: il Senato esamina il bilancio della Sécurité sociale, l'11 novembre è l'Armistizio, il 14–15 novembre la fiera delle capesante a Dieppe — e finalmente le vostre lettere!",
    "La prossima settimana: Senato e bilancio sociale, 11 novembre Armistizio, 14–15 novembre fiera di Dieppe — e le vostre lettere!", 1)
rep("content8.py", 'dans son cahier.", 21)', 'dans son cahier.", 20)', 1)
rep("content8.py", "c'est l'école.\", 21)", "c'est l'école.\", 20)", 1)
rep("content8.py", "— Merci !\", 21)", "— Merci !\", 20)", 1)
rep("content8.py", ", size=20)", ", size=20, gap=6)", 4)
rep("content8.py", 'instr="Abbina")', 'instr="Abbina", gap=6)', 1)
rep("content8.py",
    'kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)', 1)

with open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(LOG) + "\n")
print(f"transform done (with fix round 1), replacements: {len(LOG)}")
