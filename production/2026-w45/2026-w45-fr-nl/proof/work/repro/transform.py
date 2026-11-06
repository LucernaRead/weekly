# -*- coding: utf-8 -*-
"""W45 FR core VOL.3 -> FR x NL edition transform. SINGLE SOURCE for all
explanation-layer edits (fix-round edits go here, never only into content
files). Every replacement is a whole line or a unique literal, asserted.
French target text is NEVER a replacement target. Registry type names
(Chinese internal metadata, never printed) are intentionally kept, per the
W43 FR x NL / W45 FR x EN precedents; they are the only CJK allowed to
survive. P7 French definition sentences are frozen: only the explanation
lines (grammar-point lines, toolbox bridge, clinic notes, reader-corner
Dutch paras, heads' Dutch suffixes) are localised.
Run from this directory: ../../tools/venv/bin/python transform.py
It rewrites content12/34/56/7/8.py and bslib4.py in place. Re-running it
after a first run fails loudly (old strings gone) -- restore from the
core copy first; never run twice on the same tree.
"""
import re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROUND = int(os.environ.get("TRANSFORM_ROUND", "2"))
_SECTION = [1]
def section(n):
    _SECTION[0] = n

# Core P8 noted set, measured from the shipped core P8 SVG with
# tools/p8.py extract --json (noted 97/150, parse: joined). This becomes
# the edition's explicit PRINT_NOTES set (W43 FR x NL / W45 FR x EN
# precedent), so the Dutch edition prints notes for exactly the same
# exercises even though Dutch notes are longer than the core's <=10-char
# rule. P8 separator + half-width parens follow the W43 FR x NL forms.
PRINT_NOTES = [1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33,
               34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71,
               72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95,
               96, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115,
               116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128,
               129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141,
               142, 143, 144, 145, 146, 147, 148, 149, 150]
assert len(PRINT_NOTES) == 97, len(PRINT_NOTES)
BARE = sorted(set(range(1, 151)) - set(PRINT_NOTES))
assert len(BARE) == 53, len(BARE)

def rep(text, old, new, count=1):
    n = text.count(old)
    assert n == count, f"expected {count}x {old[:60]!r}, found {n}x"
    return text.replace(old, new)

def apply_file(fname, pairs):
    if _SECTION[0] != ROUND:
        print(f"skip section {_SECTION[0]} for {fname} (ROUND={ROUND})")
        return
    path = os.path.join(HERE, fname)
    text = open(path, encoding="utf-8").read()
    for old, new, *rest in pairs:
        text = rep(text, old, new, rest[0] if rest else 1)
    open(path, "w", encoding="utf-8").write(text)
    print(f"{fname}: {len(pairs)} replacements applied")

section(1)
# ---------------- OUT repoint (core -> this edition) + bslib4 furniture
for _f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    apply_file(_f, [
        ('os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg")',
         'os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-nl/svg")'),
    ])
apply_file("bslib4.py", [
    ('"Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文"',
     '"Le Lucerna · FRANS WEEKBLAD VOL.3 · TEKSTEN IN HET FRANS · UITLEG IN HET NEDERLANDS"'),
    ('f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} van {total}"'),
    ('("译注｜" + s', '("Uitleg — " + s'),
])

# ---------------- content12: P1 + P2
apply_file("content12.py", [
    ('# ================= P1 · 头版 (A2) =================',
     '# ================= P1 · voorpagina (A2) ================='),
    ('"VOL. 3 · 总第 3 期"', '"VOL. 3 · NR. 3"'),
    ('"HEBDOMADAIRE EN FRANÇAIS · 每周一期 · 读法国人正在读的法语"',
     '"HEBDOMADAIRE EN FRANÇAIS · ELKE WEEK · HET FRANS DAT DE FRANSEN LEZEN"'),
    ('"法 语 周 报 · VOL.3 · 决 赛 周 末"', '"WEEKBLAD IN HET FRANS · VOL.3 · FINALEWEEKEND"'),
    ('"周一开学 · 全法同步复课"', '"MAANDAG · TERUG NAAR SCHOOL IN HEEL FRANKRIJK"'),
    ('"大师赛开赛 · 音乐节开幕 · 详见第 2 版"', '"Masters begint · Pitchfork opent · zie pagina 2"'),
    ('"法语正文 · 简体中文讲解 — 给简体中文读者的版本"',
     '"TEKSTEN IN HET FRANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS"'),
    ('"SPORT · CULTURE · GASTRONOMIE · LA UNE · 决赛周末"',
     '"SPORT · CULTURE · GASTRONOMIE · LA UNE · FINALEWEEKEND"'),
    # P1 gloss: bare short form, measured 5 wrapped lines INCLUDING the
    # "Uitleg — " prefix (wrap("Uitleg — "+gloss, sans, 20.5, 398)).
    ('f.gloss("se jouer 决出胜负、上演 · une finale 决赛 · une demi-finale 半决赛 · un quart de finale 四分之一决赛 · une nocturne 夜场活动 · un frisson 战栗、刺激感 · la coquille Saint-Jacques 扇贝。")',
     'f.gloss("se jouer beslist worden · une finale finale · une demi-finale halve finale · un quart de finale kwartfinale · une nocturne nachtevent · un frisson rilling · la coquille Saint-Jacques schelp.")'),
    ('f.box("LES DATES · 决赛周末日程"', 'f.box("LES DATES · FINALEWEEKEND"'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · JOUW BEURT", 25)'),
    ('"周日 8 日举行决赛"', '"de finales zijn op zondag 8 november"'),
    ('"周六 7 日晚是最后夜场"', '"het laatste nachtevent is op zaterdag 7 november"'),
    ('"波尔诺曼底卖扇贝"', '"schelpen verkocht in Port-en-Bessin"'),
    ('"周一 2 日全法复课"', '"heel Frankrijk gaat terug op maandag 2 november"'),
    ('"半决赛后才知道决赛选手"', '"finalisten pas bekend na de halve finales"'),
    ('"三个决赛：网球、刺激、美味"', '"drie finales: tennis, spanning, smaken"'),
    ('"本周日程 · 11 月 2 日至 8 日"', '"DEZE WEEK · 2 TOT 8 NOVEMBER"'),
    ('"周末决赛结果周六晚、周日揭晓。"', '"Weekendfinales bekend op zaterdagavond en zondag."'),
    ('"DANS CE NUMÉRO · 本期目录"', '"DANS CE NUMÉRO · INHOUD"'),
    ('"决出胜负；上演。本周末一切都将见分晓。"', '"Beslist worden; zich afspelen. Dit weekend wordt alles beslist."'),
    ('"EN BREF · 快讯"', '"EN BREF · IN HET KORT"'),
    ('"QUIZ ÉCLAIR · 闪电问答"', '"QUIZ ÉCLAIR · BLITZQUIZ"'),
    ('"读头版，选出正确答案 · 答案见第 8 版"', '"Lees pagina 1, kies het juiste antwoord · antwoorden op pagina 8"'),
    ('"决赛在周日 8 日"', '"de finales zijn op zondag 8 november"'),
    ('"扇贝节在滨海波尔"', '"het schelpenfeest is in Port-en-Bessin"'),
    ('"周一 2 日早上全区复课"', '"alle zones gaan terug op maandagochtend 2 november"'),
    ('"最后夜场周六 7 日"', '"het laatste nachtevent is op zaterdag 7 november"'),
    ('# ================= P2 · 生活 (A2) =================',
     '# ================= P2 · dagelijks leven (A2) ================='),
    ('p.band("VIE QUOTIDIENNE · 生活", "Le Lucerna", "NIVEAU A2 · La rentrée · 开学复课")',
     'p.band("VIE QUOTIDIENNE · DAGELIJKS LEVEN", "Le Lucerna", "NIVEAU A2 · La rentrée · TERUG NAAR SCHOOL")'),
    ('f.gloss("la rentrée 开学、复课 · reprendre 重新开始、复课 · un cartable 书包 · un décalage 错开、时差 · en revanche 相反、反之 · un rituel 习惯、仪式。")',
     'f.gloss("la rentrée terugkeer naar school · reprendre opnieuw beginnen · un cartable schooltas · un décalage verschil, tijdsverschil · en revanche daarentegen · un rituel gewoonte, ritueel.")'),
    ('f.bridge("译注｜une valise 行李箱 · une ambiance 气氛 · le bilan 总结、盘点。")',
     'f.bridge("Uitleg — une valise koffer · une ambiance sfeer · le bilan de balans, het overzicht.")'),
    ('"说说你的开学：周一早上你在哪里？假期读了哪本书？写两句法语寄给编辑部。"',
     '"Waar was je maandagochtend? Wat las je? Schrijf twee zinnen."', 2),
    ('"ET VOUS ? · 说说你自己"', '"ET VOUS ? · JOUW BEURT"'),
    ('"DIRE LA DATE · 这样说日期"', '"DIRE LA DATE · ZO ZEG JE DE DATUM"'),
    ('"lundi 2 novembre · 注意：1 日说 le premier，其余用基数词"',
     '"lundi 2 novembre · let op: de 1e is le premier, andere dagen gebruiken hoofdtelwoorden"'),
    ('("lundi 2 novembre", "11 月 2 日星期一 · la rentrée")',
     '("lundi 2 novembre", "maandag 2 november · la rentrée")'),
    ('("mardi 3 novembre", "11 月 3 日星期二 · votes à l\'Assemblée")',
     '("mardi 3 novembre", "dinsdag 3 november · votes à l\'Assemblée")'),
    ('("mercredi 4 novembre", "11 月 4 日星期三 · sorties cinéma")',
     '("mercredi 4 novembre", "woensdag 4 november · sorties cinéma")'),
    ('("samedi 7 novembre", "11 月 7 日星期六 · nocturne et demis")',
     '("samedi 7 novembre", "zaterdag 7 november · nocturne et demis")'),
    ('("dimanche 8 novembre", "11 月 8 日星期日 · les finales")',
     '("dimanche 8 novembre", "zondag 8 november · les finales")'),
    ('"EXERCICES · 第 2 版练习"', '"EXERCICES · OEFENINGEN PAGINA 2"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Antwoorden op pagina 8 · oefeningen zijn gemengd per niveau; zoek antwoorden op nummer"'),
    ('e.bridge("用法语补全日期（注意星期与数字）。")',
     'e.bridge("Vul de data in het Frans in (let op weekdag en getal).")'),
    ('"复课在星期一"', '"terug naar school op maandag"'),
    ('"11 月 1 日说 le premier"', '"1 november is le premier"'),
    ('"最后夜场在星期六"', '"het laatste nachtevent is op zaterdag"'),
    ('"决赛在星期日"', '"de finales zijn op zondag"'),
    ('instr="填空"', 'instr="Vul in"', 4),
    ('e.bridge("用 aller + 动词原形改写（最近将来时）。")',
     'e.bridge("Herschrijf met aller + infinitief (futur proche).")'),
    ('e.bridge("读第 2 版文章，选出正确答案。")',
     'e.bridge("Lees pagina 2 en kies het juiste antwoord.")'),
    ('"三区同一周一早上复课"', '"alle drie zones gaan terug op dezelfde maandagochtend"'),
    ('"冬令时从 10 月 25 日开始"', '"de wintertijd begon op 25 oktober"'),
    ('"11 月晚上天黑得早"', '"in november wordt het \'s avonds vroeg donker"'),
    ('["rentrée=开学 a", "reprendre=重新开始 b", "cartable=书包 c", "rituel=习惯 d"]',
     '["rentrée = terugkeer naar school a", "reprendre = opnieuw beginnen b", "cartable = schooltas c", "rituel = gewoonte d"]'),
    ('instr="把词和释义配对"', 'instr="Combineer"'),
    ('instr="改写"', 'instr="Herschrijf"', 4),
])

# ---------------- content34: P3 + P4
apply_file("content34.py", [
    ('# ================= P3 · 文化 (A2→B1) =================',
     '# ================= P3 · cultuur (A2->B1) ================='),
    ('p.band("CULTURE · 文化", "Le Lucerna", "NIVEAU A2 → B1 · Halloween, Toussaint · 万圣与诸圣")',
     'p.band("CULTURE · FEESTEN", "Le Lucerna", "NIVEAU A2 → B1 · Halloween, Toussaint · HALLOWEEN EN ALLERHEILIGEN")'),
    ('f.gloss("se déguiser 变装、装扮 · un sort 魔法、恶作剧 · une ambiance 气氛 · le souvenir 回忆、纪念 · confondre 混淆 · discret 低调的、安静的。")',
     'f.gloss("se déguiser zich verkleden · un sort een toverspreuk, een grap · une ambiance een sfeer · le souvenir een herinnering · confondre verwarren · discret discreet, rustig.")'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · JOUW BEURT", 25)', 2),
    ('f.bridge("判断对错（Vrai / Faux）。")', 'f.bridge("Juist of onjuist (Vrai / Faux).")'),
    ('"万圣节在 10 月 31 日星期六"', '"Halloween was op zaterdag 31 oktober"'),
    ('"诸圣节墓园摆满菊花"', '"op Allerheiligen staan de begraafplaatsen vol chrysanten"'),
    ('"菊花绝不能当礼物送人"', '"chrysanten worden nooit als cadeau gegeven"'),
    ('"11 月 2 日是 jour des morts，不是诸圣节"', '"2 november is de jour des morts, niet Allerheiligen"'),
    ('"文中：le rire d\'abord, le souvenir ensuite"', '"in de tekst: le rire d\'abord, le souvenir ensuite"'),
    ('f.bridge("用 déguisement / tombe / citrouille / souvenir 填空。")',
     'f.bridge("Vul in met déguisement / tombe / citrouille / souvenir.")'),
    ('"万圣节穿变装服装"', '"kinderen dragen een kostuum met Halloween"'),
    ('"花放在墓碑上"', '"bloemen worden op het graf gelegd"'),
    ('"南瓜是万圣节的象征"', '"de pompoen is het symbool van Halloween"'),
    ('"诸圣节是纪念之日"', '"Allerheiligen is een dag van herdenking"'),
    ('f.bridge("改写句子（用 ne...jamais / ne...plus / ne...pas）。")',
     'f.bridge("Herschrijf de zinnen (met ne...jamais / ne...plus / ne...pas).")'),
    ('"jamais + de（无冠词变化）"', '"jamais + de (geen lidwoordverandering)"'),
    ('"ne...plus = 不再"', '"ne...plus = niet meer"'),
    ('"n\'est pas = 不是"', '"n\'est pas = is niet"'),
    ('instr="改写"', 'instr="Herschrijf"', 3),
    ('f.bridge("即学即练 · 公园万圣节小题。")',
     'f.bridge("Jouw beurt · kleine vragen over het park met Halloween.")'),
    ('"周六 7 日是最后夜场"', '"zaterdag 7 november is het laatste nachtevent"'),
    ('"敏感儿童有免费驱怪徽章"', '"gevoelige kinderen krijgen een gratis monsterwerende badge"'),
    ('"阿斯泰里克斯公园在 Plailly"', '"het Astérixpark ligt in Plailly"'),
    ('"Peur sur le Parc 10 月 3 日至 11 月 8 日"', '"Peur sur le Parc loopt van 3 oktober tot 8 november"'),
    ('"恐惧等级用颜色区分"', '"de angst-schaal gebruikt kleuren"'),
    ('"夜场从 19 点到凌晨 1 点"', '"het nachtevent loopt van 19 uur tot 1 uur"'),
    ('"LES MOTS DES FÊTES · 节日词表"', '"LES MOTS DES FÊTES · WOORDEN"'),
    ('"un saint — 圣人"', '"un saint — een heilige"'),
    ('"un cimetière — 墓园"', '"un cimetière — een begraafplaats"'),
    ('"une tombe — 坟墓"', '"une tombe — een graf"'),
    ('"un jour férié — 公共假日"', '"un jour férié — een feestdag"'),
    ('"se souvenir — 纪念、想起"', '"se souvenir — zich herinneren"'),
    ('"un déguisement — 变装服装"', '"un déguisement — een kostuum"'),
    ('"une citrouille — 南瓜"', '"une citrouille — een pompoen"'),
    ('"un bonbon — 糖果"', '"un bonbon — een snoepje"'),
    ('"un fantôme — 幽灵"', '"un fantôme — een spook"'),
    ('"un sort — 魔法、诅咒"', '"un sort — een toverspreuk, een vloek"'),
    ('"10 月 3 日至 11 月 8 日，12 场夜场；最后夜场 11 月 7 日；白天 10 点至 19 点开放。"',
     '"Van 3 oktober tot 8 november: 12 nachtevenementen; de laatste op 7 november; overdag open van 10 tot 19 uur."'),
    ('"DATES À RETENIR · 本周日历"', '"DATES À RETENIR · DE MAAND"'),
    ('"注意：迪耶普扇贝集市在 11 月 14–15 日，不在本周。"',
     '"Let op: de schelpenbeurs in Dieppe is op 14–15 november, niet deze week."'),
    ('# ================= P4 · 体育 (B1) =================',
     '# ================= P4 · sport (B1) ================='),
    ('p.band("SPORT · 体育", "Le Lucerna", "NIVEAU B1 · Tennis · Masters de Paris")',
     'p.band("SPORT · SPORT", "Le Lucerna", "NIVEAU B1 · Tennis · Masters de Paris")'),
    ('f.gloss("un tournoi 锦标赛、赛事 · sur dur 硬地球场 · en salle 室内 · un tableau principal 正赛签表 · le tenant du titre 卫冕冠军 · basculer 逆转、倾斜 · les tribunes 看台。")',
     'f.gloss("un tournoi een toernooi · sur dur op hardcourt · en salle binnen · un tableau principal het hoofdschema · le tenant du titre de titelverdediger · basculer omslaan, kantelen · les tribunes de tribunes.")'),
    ('f.bridge("读第 4 版文章，选出正确答案。")',
     'f.bridge("Lees pagina 4 en kies het juiste antwoord.")'),
    ('"决赛在周日 8 日"', '"de finales zijn op zondag 8 november"'),
    ('"大师赛在室内硬地球场举行"', '"de Masters wordt binnen gespeeld, op hardcourt"'),
    ('"2025 年卫冕冠军是辛纳"', '"de titelverdediger van 2025 is Sinner"'),
    ('"法甲第十轮大场面：朗斯–马赛"', '"de grote Ligue 1-wedstrijd van het weekend: Lens – Marseille"'),
    ('"周日 8 日还有轮椅单打决赛（中午）"', '"op zondag 8 november is er ook de rolstoel-enkelfinale (\'s middags)"'),
    ('f.bridge("把网球词和释义配对。")', 'f.bridge("Combineer de tenniswoorden met hun betekenis.")'),
    ('["tournoi=赛事 a", "raquette=球拍 b", "tribunes=看台 c", "tenant=卫冕者 d"]',
     '["tournoi = toernooi a", "raquette = racket b", "tribunes = tribunes c", "tenant = titelverdediger d"]'),
    ('instr="配对"', 'instr="Combineer"'),
    ('f.bridge("用比较级完成句子（plus / moins）。")',
     'f.bridge("Vul in met de comparatief (plus / moins).")'),
    ('"室内球速更快"', '"de bal is sneller binnen"'),
    ('"大师赛是仅次于大满贯的级别"', '"een Masters 1000 zit net onder de Grand Slams"'),
    ('"室内赛季比室外短"', '"het binnenseizoen is korter dan het zomerseizoen"'),
    ('f.bridge("译注｜un choc 强强对决 · recevoir 迎战、接待 · familier 熟悉的。")',
     'f.bridge("Uitleg — un choc een topwedstrijd · recevoir ontvangen, gastheer zijn · familier vertrouwd.")'),
    ('"« Allez ! » — 加油！ · « Quelle action ! » — 好球！"',
     '"« Allez ! » — Kom op! · « Quelle action ! » — Wat een actie!"'),
    ('"« Il marque ! » — 他得分了！ · « C\'est gagné ! » — 赢了！"',
     '"« Il marque ! » — Hij scoort! · « C\'est gagné ! » — Gewonnen!"'),
    ('"« Quel point ! » — 好球！（网球） · « Balle de match ! » — 赛点！"',
     '"« Quel point ! » — Wat een punt! (tennis) · « Balle de match ! » — Matchpoint!"'),
    ('"LES MOTS DU TENNIS · 网球词表"', '"LES MOTS DU TENNIS · WOORDEN"'),
    ('"le tennis — 网球"', '"le tennis — tennis"'),
    ('"une balle — 球"', '"une balle — een bal"'),
    ('"un set — 一盘"', '"un set — een set"'),
    ('"un match — 比赛"', '"un match — een wedstrijd"'),
    ('"un point — 一分"', '"un point — een punt"'),
    ('"la finale — 决赛"', '"la finale — de finale"'),
    ('"un adversaire — 对手"', '"un adversaire — een tegenstander"'),
    ('"un titre — 冠军头衔"', '"un titre — een titel"'),
    ('"À SUIVRE · 拭目以待"', '"À SUIVRE · WORDT VERVOLGD"'),
    ('mf.head("MICRO-DRILLS · 即学即练", 24)', 'mf.head("MICRO-DRILLS · TRAINING", 24)'),
    ('mf.bridge("用 finale / quarts / demi-finales / tableau / fauteuil / choc 填空。")',
     'mf.bridge("Vul in met finale / quarts / demi-finales / tableau / fauteuil / choc.")'),
    ('"四分之一决赛在周五"', '"de kwartfinales zijn op vrijdag"'),
    ('"半决赛在周六"', '"de halve finales zijn op zaterdag"'),
    ('"单打决赛在周日"', '"de enkelfinale is op zondag"'),
    ('"正赛签表从周一开始"', '"het hoofdschema begint op maandag"'),
    ('"轮椅赛事周五至周日"', '"het rolstoeltoernooi loopt van vrijdag tot zondag"'),
    ('"朗斯–马赛是周末焦点战"', '"Lens – Marseille is de topwedstrijd van het weekend"'),
    ('p.text(ix + 22, db4 + 40, "LE DÉBAT · 讨论", 23, "sans", True, OLIVE)', 'p.text(ix + 22, db4 + 40, "LE DÉBAT · HET DEBAT", 23, "sans", True, OLIVE)'),
    ('"事先不知道决赛选手，是更刺激还是更扫兴？写两句支持、两句反对。"',
     '"Van tevoren niet weten wie de finalisten zijn: spannender of frustrerender? Schrijf twee zinnen voor, twee tegen."'),
])

# ---------------- content56: P5 + P6
apply_file("content56.py", [
    ('# ================= P5 · 青年 (B1) =================',
     '# ================= P5 · jeugd (B1) ================='),
    ('p.band("JEUNESSE & MUSIQUE · 青年", "Le Lucerna", "NIVEAU B1 · Pitchfork Paris · 音乐节")',
     'p.band("JEUNESSE & MUSIQUE · JEUGD", "Le Lucerna", "NIVEAU B1 · Pitchfork Paris · MUZIEKFESTIVAL")'),
    ('f.gloss("un lieu 场所、场地 · une affiche 海报 · les paroles 歌词 · donner le ton 定调子 · se promener 漫步、穿梭 · pile 正好、恰好。")',
     'f.gloss("un lieu een locatie · une affiche een affiche · les paroles de songteksten · donner le ton de toon zetten · se promener rondzwerven, wandelen · pile precies, net.")'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · JOUW BEURT", 25)'),
    ('f.bridge("读第 5 版文章，选出正确答案。")',
     'f.bridge("Lees pagina 5 en kies het juiste antwoord.")'),
    ('"音乐节 11 月 2–8 日，整整一周"', '"het festival loopt van 2 tot 8 november, een volle week"'),
    ('"15 届音乐节"', '"de 15e editie van het festival"'),
    ('"Avant-Garde 在巴士底各场地，周四至周六"', '"Avant-Garde is in de Bastille-zalen, van donderdag tot zaterdag"'),
    ('"俱乐部之夜在周五、周六"', '"de clubnachten zijn op vrijdag en zaterdag"'),
    ('"开幕夜：Headache、Iceage、DIIV"', '"openingsavond: Headache, Iceage, DIIV"'),
    ('f.bridge("用 lieux / paroles / affiche / ambiance / danse / découvre 填空。")',
     'f.bridge("Vul in met lieux / paroles / affiche / ambiance / danse / découvre.")'),
    ('"10 个场地"', '"tien locaties"'),
    ('"歌词也是法语学习材料"', '"songteksten zijn ook Frans leermateriaal"'),
    ('"海报上写着演出信息"', '"op de affiche staat de line-up"'),
    ('"每晚气氛各不相同"', '"elke avond een andere sfeer"'),
    ('"音乐节上人们跳舞"', '"op het festival dansen mensen"'),
    ('"发现不认识的乐队"', '"bands ontdekken die je niet kent"'),
    ('f.bridge("把音乐词和释义配对。")', 'f.bridge("Combineer de muziekwoorden met hun betekenis.")'),
    ('["concert=音乐会 a", "scène=舞台 b", "groupe=乐队 c", "billet=门票 d"]',
     '["concert = concert a", "scène = podium b", "groupe = band c", "billet = kaartje d"]'),
    ('instr="配对"', 'instr="Combineer"', 2),
    ('f.bridge("补全对话（音乐节门口）。")',
     'f.bridge("Vul de dialoog in (bij de festivallingang).")'),
    ('"今晚演出的乐队"', '"de band die vanavond speelt"'),
    ('"买两张票"', '"twee kaartjes kopen"'),
    ('"MOTS DE LA MUSIQUE · 音乐词表"', '"MOTS DE LA MUSIQUE · WOORDEN"'),
    ('"un festival — 音乐节"', '"un festival — een festival"'),
    ('"un concert — 音乐会"', '"un concert — een concert"'),
    ('"une chanson — 歌曲"', '"une chanson — een lied"'),
    ('"un chanteur — 歌手"', '"un chanteur — een zanger"'),
    ('"danser — 跳舞"', '"danser — dansen"'),
    ('"écouter — 聆听"', '"écouter — luisteren"'),
    ('"une salle — 演出厅"', '"une salle — een zaal"'),
    ('"le public — 观众"', '"le public — het publiek"'),
    ('"PARIS CREATOR WEEK · 创作者周"', '"PARIS CREATOR WEEK"'),
    ('"11 月 4–5 日拉维莱特：创作者周，线上创作者与观众线下见面。"',
     '"4–5 november in La Villette: Creator Week, online makers ontmoeten hun publiek in het echt."'),
    ('p.text(ix + 22, ty5 + 40, "LE DÉBAT · 讨论", 23, "sans", True, OLIVE)', 'p.text(ix + 22, ty5 + 40, "LE DÉBAT · HET DEBAT", 23, "sans", True, OLIVE)'),
    ('"十个场地的音乐节，比单一大场馆更好吗？你听什么音乐学法语？"',
     '"Een festival op tien locaties: beter dan één grote zaal? Welke muziek luister jij om Frans te leren?"'),
    ('# ================= P6 · 时事 (B2) =================',
     '# ================= P6 · actualiteit (B2) ================='),
    ('p.band("POLITIQUE & CHIFFRES · 时事", "Le Lucerna", "NIVEAU B2 · Budget 2027 · 预算周")',
     'p.band("POLITIQUE & CHIFFRES · POLITIEK & CIJFERS", "Le Lucerna", "NIVEAU B2 · Budget 2027 · BEGROTINGSWEEK")'),
    ('f.gloss("un budget 预算 · une mission （预算）分项 · un député 国民议会议员 · rejeter 否决 · à l\'unanimité 一致通过/否决 · un amendement 修正案。")',
     'f.gloss("un budget een begroting · une mission een (begrotings)onderdeel · un député een parlementslid · rejeter verwerpen · à l\'unanimité unaniem · un amendement een amendement.")'),
    ('"LE CALENDRIER PRÉVU · 计划中的投票日程（结果未出）"',
     '"LE CALENDRIER PRÉVU · GEPLANDE KALENDER (NOG GEEN RESULTATEN)"'),
    ('"本页日程为计划安排，结果尚未产生，下期跟进。"',
     '"Deze kalender is de planning; nog geen resultaten — vervolg in het volgende nummer."'),
    ('e6.head("LIRE LE CALENDRIER · 读日程", 25)',
     'e6.head("LIRE LE CALENDRIER · KALENDER", 25)'),
    ('e6.bridge("读上图日程，选出正确答案。")',
     'e6.bridge("Lees de kalender hierboven en kies het juiste antwoord.")'),
    ('"周二 3 日：文化与媒体"', '"dinsdag 3 november: Cultuur en Media"'),
    ('"周三 4 日：农业"', '"woensdag 4 november: Landbouw"'),
    ('"周四 5 日：国土协调与科研"', '"donderdag 5 november: Territoriale Cohesie en Onderzoek"'),
    ('"周五 6 日：公共财政与经济"', '"vrijdag 6 november: Overheidsfinanciën en Economie"'),
    ('"10 月 23 日社保预算收入被 115–1 否决"', '"op 23 oktober is de inkomstenzijde van de socialezekerheidsbegroting verworpen met 115–1"'),
    ('"参议院从 11 月 9 日起审议"', '"de Senaat bespreekt de tekst vanaf 9 november"'),
    ('e6.head("LES MOTS · 词汇", 25)', 'e6.head("LES MOTS · WOORDEN", 25)'),
    ('["député=议员 a", "rejeter=否决 b", "vote=投票 c", "amendement=修正案 d"]',
     '["député = parlementslid a", "rejeter = verwerpen b", "vote = stemming c", "amendement = amendement d"]'),
    ('"« Le texte part au Sénat. » — 法案送交参议院。"',
     '"« Le texte part au Sénat. » — Het wetsvoorstel gaat naar de Senaat."'),
    ('"« Ce calendrier peut encore bouger. » — 日程仍可能变动。"',
     '"« Ce calendrier peut encore bouger. » — De kalender kan nog veranderen."'),
    ('"« Les résultats ne sont pas connus. » — 结果尚未揭晓。"',
     '"« Les résultats ne sont pas connus. » — De resultaten zijn nog niet bekend."'),
    ('g.bridge("译注｜prévu 预定的、计划的 · réaliser 实现、完成 · distinguer 区分。")',
     'g.bridge("Uitleg — prévu gepland · réaliser uitvoeren · distinguer onderscheiden.")'),
    ('g2.bridge("用比较级完成句子。")', 'g2.bridge("Vul in met de comparatief.")'),
    ('"预算辩论比一场音乐会长"', '"een begrotingsdebat is langer dan een concert"'),
    ('"预算比时间表复杂"', '"de begroting is ingewikkelder dan een kalender"'),
    ('"文化预算与农业预算同样重要"', '"de Cultuurbegroting is even belangrijk als de Landbouwbegroting"'),
    ('g2.head("MICRO-DRILLS · 即学即练", 25)', 'g2.head("MICRO-DRILLS · TRAINING", 25)'),
    ('g2.bridge("用 examine / ont rejeté / part / peut / connus 填空。")',
     'g2.bridge("Vul in met examine / ont rejeté / part / peut / connus.")'),
    ('"国民议会审议预算"', '"de Nationale Assemblee bespreekt de begroting"'),
    ('"议员们否决收入部分"', '"de parlementsleden verwierpen de inkomstenzijde"'),
    ('"法案送交参议院"', '"het wetsvoorstel gaat naar de Senaat"'),
    ('"日程仍可能变动"', '"de kalender kan nog veranderen"'),
    ('"结果尚未揭晓"', '"de resultaten zijn nog niet bekend"'),
    ('g2.head("LE DÉBAT · 讨论", 25)', 'g2.head("LE DÉBAT · HET DEBAT", 25)'),
    ('g2.bridge("讨论｜结果未出时，该不该先公布日程？区分 prévu（计划）与 décidé（已定）。")',
     'g2.bridge("Debat · Moet een planning worden aangekondigd vóór de resultaten? Onderscheid prévu (gepland) van décidé (beslist).")'),
])

# ---------------- content7: P7 (French definition sentences FROZEN)
apply_file("content7.py", [
    ('p.band("LANGUE EN MAIN · 精讲", "Le Lucerna", "A2 → B2 · Les phrases de la semaine · 本周金句")',
     'p.band("LANGUE EN MAIN · TAAL IN DE PRAKTIJK", "Le Lucerna", "A2 → B2 · Les phrases de la semaine · ZINNEN VAN DE WEEK")'),
    ('cA.head("NIVEAU A2 · 基础", 27)', 'cA.head("NIVEAU A2 · BASISNIVEAU", 27)'),
    ('cB.head("NIVEAU B1 · 进阶", 27)', 'cB.head("NIVEAU B1 · GEMIDDELD", 27)'),
    ('cC.head("NIVEAU B2 · 挑战", 27)', 'cC.head("NIVEAU B2 · UITDAGING", 27)'),
    ('cD.head("BOÎTE À OUTILS · 工具箱", 27)', 'cD.head("BOÎTE À OUTILS · OP ZAK", 27)'),
    ('cD.bridge("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。")',
     'cD.bridge("Gereedschapskist · Drie meeneemzinnen, één per niveau; alle zinnen van de week komen uit artikelen in dit nummer — lees het artikel opnieuw en de zin wordt makkelijk.")'),
    ('p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE · 本周金句（全部出自本期文章）", 27, "sans", True, OLIVE)',
     'p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE · ZINNEN VAN DE WEEK", 27, "sans", True, OLIVE)'),
    ('p.text(RIGHT, py + 26, "每句一个语法点 + 一道小题 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")',
     'p.text(RIGHT, py + 26, "Eén grammaticapunt + één mini-oefening per zin · antwoorden op pagina 8", 20, "sans", False, GREY, anchor="end")'),
    ('"语法点｜reprendre：复课、重新开始（pause 后）。"',
     '"Grammaticapunt · reprendre: weer beginnen, na een pauze."'),
    ('"语法点｜ne...pas encore：尚未、还不。"',
     '"Grammaticapunt · ne...pas encore: nog niet."'),
    ('"pas encore 尚未"', '"pas encore = nog niet"'),
    ('"语法点｜passé composé 代动词：se + être + 过去分词。"',
     '"Grammaticapunt · passé composé met wederkerende werkwoorden: se + être + voltooid deelwoord."'),
    ('"语法点｜comparatif：plus + 形容词，ou 对举。"',
     '"Grammaticapunt · comparatif: plus + bijvoeglijk naamwoord, twee tegenstellingen met ou."'),
    ('"plus + 形容词"', '"plus + bijvoeglijk naamwoord"'),
    ('"语法点｜se promener：代动词，漫步、穿梭。"',
     '"Grammaticapunt · se promener: wederkerend werkwoord, wandelen, rondzwerven."'),
    ('"语法点｜pouvoir + 动词原形：可能、可以。"',
     '"Grammaticapunt · pouvoir + infinitief: kunnen, mogen."'),
    ('"语法点｜se jouer：决出胜负、上演（代动词）。"',
     '"Grammaticapunt · se jouer: beslist worden, zich afspelen (wederkerend)."'),
    ('"语法点｜rencontrer：与观众见面；y 代指地点。"',
     '"Grammaticapunt · rencontrer: je publiek ontmoeten; y verwijst naar de plaats."'),
    ('cf.head("CLINIQUE DES ERREURS · 易错诊所", 25)',
     'cf.head("CLINIQUE DES ERREURS · PAS OP!", 25)'),
    ('cf.bridge("每句有一处错误：找出来并改正。")',
     'cf.bridge("Elke zin bevat één fout: vind hem en verbeter hem.")'),
    ('"jamais + de：否定句中 des 变 de"', '"jamais + de: in een ontkenning wordt des de"'),
    ('"主谓一致：créateurs 复数 → rencontrent，不是 rencontre"',
     '"Congruentie: créateurs is meervoud → rencontrent, niet rencontre"'),
    ('"虚拟式：il examine，不加 s"', '"Aanvoegende wijs: il examine, zonder -s"'),
    ('"事实：决赛在 8 日，不是 7 日"', '"Feit: de finale is op de 8e, niet op de 7e"'),
    ('instr="改错"', 'instr="Corrigeer"', 4),
    ('p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS · 读者园地", 24, "sans", True, OLIVE)',
     'p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS · LEZERSRUBRIEK", 24, "sans", True, OLIVE)'),
    # Reader's corner: labelled editorial example (FR, frozen) + NL comment
    # WITH an explicit imperative call covering BOTH a letter AND the best
    # P8 text, + NL disclosure of the three facts (no real letters, no
    # VOL.2 P8 best text, both deferred to VOL.4). Both NL paras measured
    # at 2 wrapped lines (width 848) so nothing spills past the box.
    ('p.para(rx + 24, by7 + 196, "小墨点评｜编辑部示例：周末叙事用 passé composé 很稳，分号连接两天值得学。下期读者园地将点评真实投稿。", 20, "sans", False, GREY, rw - 48, 1.4)',
     'p.para(rx + 24, by7 + 196, "Redactiecommentaar · Stabiele passé composé, puntkomma verbindt twee dagen. Stuur je brief én je beste pagina-8-tekst in voor VOL.4!", 20, "sans", False, GREY, rw - 48, 1.4)'),
    ('p.para(rx + 24, by7 + 336, "编辑部说明：截至付印，编辑部尚未收到 VOL.2 第 8 版的投稿作文（W44 未出刊），故本期刊登标注明确的编辑部示例；VOL.4 将兑现点评真实投稿的承诺。", 19.5, "sans", False, GREY, rw - 48, 1.4)',
     'p.para(rx + 24, by7 + 336, "Opmerking van de redactie: geen echte brieven en geen beste VOL.2-pagina-8-tekst binnen (geen W44-nummer); beide volgen in VOL.4.", 19.5, "sans", False, GREY, rw - 48, 1.4)'),
    ('p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE · VOL.4 下周预告", 24, "sans", True, "#f3edda")',
     'p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE · VOL.4 VOLGENDE WEEK", 24, "sans", True, "#f3edda")'),
    ('p.para(rx + 24, ty7 + 196, "下周：参议院审议社保预算、11 月 11 日停战纪念日、迪耶普扇贝集市；还有你们的来信！", 20, "sans", False, "#b3a06a", rw - 48, 1.4)',
     'p.para(rx + 24, ty7 + 196, "Volgende week: de Senaat bespreekt de begroting voor sociale zekerheid, 11 november Wapenstilstand, de haring- en sint-jakobsschelpenbeurs in Dieppe; en jullie brieven!", 20, "sans", False, "#b3a06a", rw - 48, 1.4)'),
])

# ---------------- content8: P8
OLD_KEYS = '''for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):
            s += f"（{e['note']}）"
        parts.append(s)'''
NEW_KEYS = '''# Notes printed on this page = exactly the set printed in the core
# edition, computed from the core registry (its rule was: page 8 always, or
# note <= 10 chars, or type 改错/图表读数). Reproduced as an explicit set so
# the Dutch edition shows the same notes for the same exercises.
PRINT_NOTES = {%s}
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— PAGINA {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and e["n"] in PRINT_NOTES:
            s += f" ({e['note']})"
        parts.append(s)''' % ", ".join(str(n) for n in PRINT_NOTES)
apply_file("content8.py", [
    ('p.band("EXERCICES & RÉPONSES · 练习与答案", "Le Lucerna", "综合评估 ÉVALUATION · 答案在本版下方")',
     'p.band("EXERCICES & RÉPONSES · OEFENINGEN & ANTWOORDEN", "Le Lucerna", "ÉVALUATION · ANTWOORDEN ONDERAAN DEZE PAGINA")'),
    ('"11 月 8 日 2026 是星期日"', '"8 november 2026 is een zondag"'),
    ('"去南泰尔看决赛"', '"naar Nanterre voor de finales"'),
    ('"决赛选手周六晚才揭晓"', '"finalisten pas zaterdagavond bekend"'),
    ('"品尝语境（un régal）→ goûté"', '"proefcontext (un régal) → goûté"'),
    ('"se promener 漫步"', '"se promener = wandelen"'),
    ('"avoir + 过去分词 goûté（不配合）"', '"avoir + voltooid deelwoord goûté (geen congruentie)"'),
    ('"les finales 主语复数 → ont lieu"', '"les finales is meervoud → ont lieu"'),
    ('"elle écrit 她写"', '"elle écrit = zij schrijft"'),
    ('bf.head("A · TEXTE À TROUS · 完形填空", 24)', 'bf.head("A · TEXTE À TROUS · GATENTEKST", 24)'),
    ('bf.bridge("选项：")', 'bf.bridge("Opties:")'),
    ('bf.head("B · CHOIX MULTIPLE · 单选", 24)', 'bf.head("B · CHOIX MULTIPLE · MEERKEUZE", 24)'),
    ('"7 nov. = samedi（最后夜场）"', '"7 nov. = zaterdag (laatste nachtevent)"'),
    ('"s\'intéresser aux（à+les）"', '"s\'intéresser aux (à + les)"'),
    ('"si + imparfait（未完成过去时）→ conditionnel présent（条件式现在时）；j\' 是 je 在元音前的省音"',
     '"si + imparfait → conditionnel; j\' = je geëlideerd"'),
    ('"主语 ce programme 三单 → semble"', '"ce programme is 3e persoon enkelvoud → semble"'),
    ('"将来时 aura lieu（决赛在周日）"', '"toekomstige tijd aura lieu (finale op zondag)"'),
    ('"三区同日复课"', '"drie zones tegelijk terug"'),
    ('"扇贝节在 11 月 7–8 日"', '"schelpenfeest op 7–8 november"'),
    ('bf.head("C · LECTURE · 阅读理解", 24)', 'bf.head("C · LECTURE · LEZEN", 24)'),
    ('"夜场 19 点至凌晨 1 点"', '"nachtevent van 19 uur tot 1 uur"'),
    ('"小徽章给小 Léo 驱怪"', '"het badge is voor kleine Léo, tegen monsters"'),
    ('"周日先看决赛再吃扇贝"', '"zondag eerst finales, dan schelpen"'),
    ('"周日晚上早睡因为周一上学"', '"zondagavond vroeg naar bed: maandag is school"'),
    ('"周一是上学日（复课后正常周一）"', '"maandag is een schooldag"'),
    ('bf.head("D · PHRASES · 完成句子与转换", 24)', 'bf.head("D · PHRASES · ZINNEN", 24)'),
    ('"aller + 原形（futur proche）"', '"aller + infinitief (futur proche)"'),
    ('"si + 半过去时 venais"', '"si + imparfait venais"'),
    ('"passé composé : a + 过去分词"', '"passé composé: a + voltooid deelwoord"'),
    ('"selon moi = 在我看来"', '"selon moi = volgens mij"'),
    ('"il est prévu que + 虚拟式"', '"il est prévu que + aanvoegende wijs"'),
    ('bf.head("E · TRADUCTION · 翻译", 24)', 'bf.head("E · TRADUCTION · VERTALEN", 24)'),
    # Translation items re-aimed for Dutch readers (W43 FR x NL precedent):
    # FR->reader key becomes the Dutch translation; reader->FR items
    # print a Dutch source sentence, French key unchanged.
    ('"读一份日程，本身就是在了解法国。"', '"Een programma lezen is al Frankrijk begrijpen."'),
    ('"lire un programme = 读日程"', '"lire un programme = een programma lezen"'),
    ('"Traduisez : « Lire un programme, c\'est déjà comprendre la France. »"',
     '"Vertaal naar het Nederlands: « Lire un programme, c\'est déjà comprendre la France. »"'),
    ('"比较级 plus vite + court"', '"comparatief plus vite + court"'),
    ('"Traduisez : 他跑得比他哥哥更快。"', '"Vertaal naar het Frans: Hij rent sneller dan zijn broer."'),
    ('"être en vacances + depuis"', '"être en vacances + depuis"'),
    ('"Traduisez : 学生们自 10 月 17 日起就在放假。"', '"Vertaal naar het Frans: De leerlingen zijn al sinds 17 oktober op vakantie."'),
    ('"futur proche + préparer"', '"futur proche + préparer"'),
    ('"Traduisez : 今晚，我们要准备书包。"', '"Vertaal naar het Frans: Vanavond gaan we onze schooltassen klaarmaken."'),
    ('"ne...pas encore = 尚未"', '"ne...pas encore = nog niet"'),
    ('"Traduisez : 人们尚不知道决赛选手是谁。"', '"Vertaal naar het Frans: Mensen weten nog niet wie de finalisten zijn."'),
    ('bf.head("F · LES MOTS · 词汇配对", 24)', 'bf.head("F · LES MOTS · WOORDEN", 24)'),
    ('["tournoi=赛事 a", "nocturne=夜场 b", "budget=预算 c", "coquille=扇贝 d", "festival=音乐节 e"]',
     '["tournoi = toernooi a", "nocturne = nachtevent b", "budget = begroting c", "coquille = sint-jakobsschelp d", "festival = festival e"]'),
    ('instr="配对"', 'instr="Combineer"'),
    ('"11 月 7 日是星期六"', '"7 november is een zaterdag"'),
    ('"在市场买扇贝"', '"schelpen kopen op de markt"'),
    ('"goûter 品尝（原形）"', '"goûter = proeven (infinitief)"'),
    ('"à la portaise 是一种做法"', '"à la portaise is een bereidingswijze"'),
    ('"Bon week-end ! 周末愉快"', '"Bon week-end ! = fijn weekend"'),
    ('bf.head("G · DIALOGUE · 对话补全", 24)', 'bf.head("G · DIALOGUE · DIALOOG", 24)'),
    ('reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")',
     'reg_ex("B1", "写作", "Open opdracht — punten in het schrijfkader; voorbeeldtekst in het MODÈLE-kader op deze pagina", "beoordeeld op de punten")'),
    ('p.text(wx, wy + 26, "H · ÉCRITURE · 写作", 25, "sans", True, OLIVE)',
     'p.text(wx, wy + 26, "H · ÉCRITURE · SCHRIJVEN", 25, "sans", True, OLIVE)'),
    ('p.para(wx, wy + 190, "用法语写 80–100 词：我的 11 月 7–8 日周末。写清一场比赛、一个节日、一道菜。", 20, "sans", False, GREY, ww, 1.4)',
     'p.para(wx, wy + 190, "Schrijf in het Frans 80–100 woorden: mijn weekend van 7–8 november. Beschrijf één wedstrijd, één feest, één gerecht.", 20, "sans", False, GREY, ww, 1.4)'),
    ('p.text(mx2 + 22, wy + 38, "MODÈLE · 范文", 23, "sans", True, OLIVE)',
     'p.text(mx2 + 22, wy + 38, "MODÈLE · VOORBEELDTEKST", 23, "sans", True, OLIVE)'),
    ('p.text(MX, ky + 26, "RÉPONSES · 全部答案与简析（第 1–8 版）", 26, "sans", True, OLIVE)',
     'p.text(MX, ky + 26, "RÉPONSES · ALLE ANTWOORDEN MET NOTEN (PAGINA 1–8)", 26, "sans", True, OLIVE)'),
    (OLD_KEYS, NEW_KEYS),
])

# ---------------- final gate: no CJK outside the kept registry type names
ALLOWED = ["完成句子", "单选", "词汇配对", "阅读判断", "句型转换",
           "图表读数", "改错", "跟练", "完形填空", "阅读理解", "翻译",
           "对话补全", "写作"]
CJK = re.compile(r'[\u4e00-\u9fff]')
for fname in ["content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "bslib4.py"]:
    text = open(os.path.join(HERE, fname), encoding="utf-8").read()
    scrubbed = text
    for a in ALLOWED:
        scrubbed = scrubbed.replace(a, "")
    bad = CJK.findall(scrubbed)
    assert not bad, f"{fname}: surviving CJK after transform: {bad[:10]}"
    print(f"{fname}: CJK gate clean (only registry type names remain)")
print("TRANSFORM OK")

# ================= FIX ROUND 2 (render-1 findings) =================
# R1-1 P1 agenda Dutch line crossed the page edge (ink 1948.5 > 1885):
# single-line short form, measured 398.0px at 19pt (budget 412px).
# R1-2 P8 battery ended 1526 > 1485 (last lines crossed the writing-strip
# rule and sat under the MODÈLE box): the E translation stems wrapped to
# 2 lines each in Dutch (core: 1). Arrow direction markers restore the
# core line counts (135: 2 lines = core; 136: 1 = core; 139: 1 = core;
# 137/138 stay at 2 lines, +2 lines total -> battery ~1468 < 1485).
# Arrow convention: item 135 translates INTO Dutch, items 136-139 translate
# INTO French; the first item demonstrates the convention for the section.
# R1-3 P8 keys ended 2646 > 2545 (footer rule 2580): shorten the longest
# printed Dutch notes / the item-150 apparatus key (keys unchanged;
# note text is explanation layer). Total ~430 chars saved across the
# 8 page-group paras.
section(2)
apply_file("content12.py", [
    ('"Weekendfinales bekend op zaterdagavond en zondag."',
     '"Finales bekend op zaterdagavond en zondag."'),
    ('"heel Frankrijk gaat terug op maandag 2 november"',
     '"heel Frankrijk terug op maandag 2 november"'),
    ('"het laatste nachtevent is op zaterdag 7 november"',
     '"laatste nachtevent op zaterdag 7 november"', 2),
    ('"de finales zijn op zondag 8 november"',
     '"finales op zondag 8 november"', 2),
    ('"schelpen verkocht in Port-en-Bessin"',
     '"schelpen in Port-en-Bessin"'),
    ('"het schelpenfeest is in Port-en-Bessin"',
     '"schelpenfeest in Port-en-Bessin"'),
    ('"alle drie zones gaan terug op dezelfde maandagochtend"',
     '"alle zones terug op dezelfde maandagochtend"'),
])
apply_file("content34.py", [
    ('"de finales zijn op zondag 8 november"',
     '"finales op zondag 8 november"'),
    ('"op Allerheiligen staan de begraafplaatsen vol chrysanten"',
     '"Allerheiligen: begraafplaatsen vol chrysanten"'),
    ('"2 november is de jour des morts, niet Allerheiligen"',
     '"2 november is jour des morts, niet Allerheiligen"'),
    ('"gevoelige kinderen krijgen een gratis monsterwerende badge"',
     '"gevoelige kinderen krijgen een gratis badge"'),
    ('"de grote Ligue 1-wedstrijd van het weekend: Lens – Marseille"',
     '"topwedstrijd van het weekend: Lens – Marseille"'),
    ('"op zondag 8 november is er ook de rolstoel-enkelfinale (\'s middags)"',
     '"zondag 8 november ook rolstoelfinale (\'s middags)"'),
])
apply_file("content56.py", [
    ('"Avant-Garde is in de Bastille-zalen, van donderdag tot zaterdag"',
     '"Avant-Garde in Bastille, donderdag tot zaterdag"'),
    ('"de clubnachten zijn op vrijdag en zaterdag"',
     '"clubnachten op vrijdag en zaterdag"'),
    ('"donderdag 5 november: Territoriale Cohesie en Onderzoek"',
     '"donderdag 5 november: Cohesie en Onderzoek"'),
    ('"vrijdag 6 november: Overheidsfinanciën en Economie"',
     '"vrijdag 6 november: Financiën en Economie"'),
    ('"op 23 oktober is de inkomstenzijde van de socialezekerheidsbegroting verworpen met 115–1"',
     '"23 oktober: inkomsten verworpen met 115–1"'),
    ('"de Senaat bespreekt de tekst vanaf 9 november"',
     '"Senaat bespreekt tekst vanaf 9 november"'),
    ('"de Nationale Assemblee bespreekt de begroting"',
     '"Assemblee bespreekt de begroting"'),
    ('"de parlementsleden verwierpen de inkomstenzijde"',
     '"parlementsleden verwierpen inkomsten"'),
])
apply_file("content7.py", [
    ('"Congruentie: créateurs is meervoud → rencontrent, niet rencontre"',
     '"créateurs meervoud → rencontrent"'),
    ('"jamais + de: in een ontkenning wordt des de"',
     '"jamais + de: des wordt de"'),
    ('"Aanvoegende wijs: il examine, zonder -s"',
     '"il examine, zonder -s"'),
    ('"Feit: de finale is op de 8e, niet op de 7e"',
     '"finale op de 8e, niet de 7e"'),
])
apply_file("content8.py", [
    ('"Vertaal naar het Nederlands: « Lire un programme, c\'est déjà comprendre la France. »"',
     '"→ NL: « Lire un programme, c\'est déjà comprendre la France. »"'),
    ('"Vertaal naar het Frans: Hij rent sneller dan zijn broer."',
     '"→ FR: Hij rent sneller dan zijn broer."'),
    ('"Vertaal naar het Frans: De leerlingen zijn al sinds 17 oktober op vakantie."',
     '"→ FR: De leerlingen zijn sinds 17 oktober op vakantie."'),
    ('"Vertaal naar het Frans: Vanavond gaan we onze schooltassen klaarmaken."',
     '"→ FR: Vanavond gaan we onze schooltassen klaarmaken."'),
    ('"Vertaal naar het Frans: Mensen weten nog niet wie de finalisten zijn."',
     '"→ FR: Men kent de finalisten nog niet."'),
    ('"avoir + voltooid deelwoord goûté (geen congruentie)"',
     '"avoir + goûté (geen congruentie)"'),
    ('"les finales is meervoud → ont lieu"',
     '"les finales meervoud → ont lieu"'),
    ('"ce programme is 3e persoon enkelvoud → semble"',
     '"ce programme enkelvoud → semble"'),
    ('"toekomstige tijd aura lieu (finale op zondag)"',
     '"toekomst aura lieu (finale zondag)"'),
    ('"het badge is voor kleine Léo, tegen monsters"',
     '"badge voor kleine Léo, tegen monsters"'),
    ('"zondagavond vroeg naar bed: maandag is school"',
     '"vroeg naar bed: maandag is school"'),
    ('"passé composé: a + voltooid deelwoord"',
     '"passé composé: a + deelwoord"'),
    ('"lire un programme = een programma lezen"',
     '"lire un programme = programma lezen"'),
    ('"Open opdracht — punten in het schrijfkader; voorbeeldtekst in het MODÈLE-kader op deze pagina"',
     '"Open opdracht — punten in schrijfkader, voorbeeld in MODÈLE-kader"'),
])
