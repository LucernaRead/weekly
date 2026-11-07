# -*- coding: utf-8 -*-
"""W45 FR core VOL.3 -> FR x EN edition transform. SINGLE SOURCE for all
explanation-layer edits (fix-round edits go here, never only into content
files). Every replacement is a whole line or a unique literal, asserted.
French target text is NEVER a replacement target. Registry type names
(Chinese internal metadata, never printed) are intentionally kept, per the
W43 FR x EN precedent; they are the only CJK allowed to survive.
Run from this directory: ../../tools/venv/bin/python transform.py
It rewrites content12/34/56/7/8.py and bslib4.py in place. Re-running it
after a first run fails loudly (old strings gone) -- restore from the
core copy first; never run twice on the same tree.
"""
import re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))

# Fix rounds: ROUND=1 applies the initial translation; ROUND>=2 applies only
# the fix sections (round-1 old strings are gone after round 1, so a full
# re-run would fail). Fresh rebuild: TRANSFORM_ROUND=1, then =2, =3...
ROUND = int(os.environ.get("TRANSFORM_ROUND", "2"))
_SECTION = [1]
def section(n):
    _SECTION[0] = n

# Core P8 noted set, measured from the shipped core P8 SVG with
# tools/p8.py extract --json (noted 97/150, parse: joined). This becomes
# the edition's explicit PRINT_NOTES set (W43 FR x EN precedent), so the
# English edition prints notes for exactly the same exercises even
# though English notes are longer than the core's <=10-char rule.
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
# ---------------- bslib4: footer + gloss prefix (W43 FR x EN shipped forms)
apply_file("bslib4.py", [
    ('"Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文"',
     '"Le Lucerna · FRENCH WEEKLY VOL.3 · TEXT IN FRENCH · EXPLANATIONS IN ENGLISH"'),
    ('f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} of {total}"'),
    ('("译注｜" + s', '("NOTE · " + s'),
])

# ---------------- content12: P1 + P2
apply_file("content12.py", [
    ('# ================= P1 · 头版 (A2) =================',
     '# ================= P1 · front page (A2) ================='),
    ('"VOL. 3 · 总第 3 期"', '"VOL. 3 · ISSUE NO. 3"'),
    ('"HEBDOMADAIRE EN FRANÇAIS · 每周一期 · 读法国人正在读的法语"',
     '"HEBDOMADAIRE EN FRANÇAIS · EVERY WEEK · READ THE FRENCH THE FRENCH READ"'),
    ('"法 语 周 报 · VOL.3 · 决 赛 周 末"', '"FRENCH WEEKLY · VOL.3 · FINALS WEEKEND"'),
    ('"周一开学 · 全法同步复课"', '"MONDAY · BACK TO SCHOOL ALL OVER FRANCE"'),
    ('"大师赛开赛 · 音乐节开幕 · 详见第 2 版"', '"Masters begins · Pitchfork opens · see page 2"'),
    ('"法语正文 · 简体中文讲解 — 给简体中文读者的版本"',
     '"Text in French · Explanations in English — the edition for English-speaking readers"'),
    ('"SPORT · CULTURE · GASTRONOMIE · LA UNE · 决赛周末"',
     '"SPORT · CULTURE · GASTRONOMIE · LA UNE · FINALS WEEKEND"'),
    ('f.gloss("se jouer 决出胜负、上演 · une finale 决赛 · une demi-finale 半决赛 · un quart de finale 四分之一决赛 · une nocturne 夜场活动 · un frisson 战栗、刺激感 · la coquille Saint-Jacques 扇贝。")',
     'f.gloss("se jouer to be decided, to be played out · une finale a final · une demi-finale a semi-final · un quart de finale a quarter-final · une nocturne a night event · un frisson a thrill · la coquille Saint-Jacques a scallop.")'),
    ('f.box("LES DATES · 决赛周末日程"', 'f.box("LES DATES · FINALS WEEKEND DATES"'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · YOUR TURN", 25)'),
    ('"周日 8 日举行决赛"', '"the finals are on Sunday 8th"'),
    ('"周六 7 日晚是最后夜场"', '"the last night event is on Saturday 7th"'),
    ('"波尔诺曼底卖扇贝"', '"scallops sold in Port-en-Bessin"'),
    ('"周一 2 日全法复课"', '"all of France goes back on Monday 2nd"'),
    ('"半决赛后才知道决赛选手"', '"finalists known only after the semi-finals"'),
    ('"三个决赛：网球、刺激、美味"', '"three finals: tennis, thrills, flavours"'),
    ('"本周日程 · 11 月 2 日至 8 日"', '"THIS WEEK · 2–8 NOVEMBER"'),
    ('"周末决赛结果周六晚、周日揭晓。"', '"Results out Saturday night and Sunday."'),
    ('"DANS CE NUMÉRO · 本期目录"', '"DANS CE NUMÉRO · IN THIS ISSUE"'),
    ('"决出胜负；上演。本周末一切都将见分晓。"', '"to be decided. This weekend decides all."'),
    ('"EN BREF · 快讯"', '"EN BREF · IN BRIEF"'),
    ('"QUIZ ÉCLAIR · 闪电问答"', '"QUIZ ÉCLAIR · LIGHTNING QUIZ"'),
    ('"读头版，选出正确答案 · 答案见第 8 版"', '"Read page 1, pick the right answer · answers on page 8"'),
    ('"决赛在周日 8 日"', '"the finals are on Sunday 8th"'),
    ('"扇贝节在滨海波尔"', '"the scallop fair is in Port-en-Bessin"'),
    ('"周一 2 日早上全区复课"', '"all zones go back on Monday 2nd in the morning"'),
    ('"最后夜场周六 7 日"', '"the last night event is on Saturday 7th"'),
    ('# ================= P2 · 生活 (A2) =================',
     '# ================= P2 · everyday life (A2) ================='),
    ('p.band("VIE QUOTIDIENNE · 生活", "Le Lucerna", "NIVEAU A2 · La rentrée · 开学复课")',
     'p.band("VIE QUOTIDIENNE · EVERYDAY LIFE", "Le Lucerna", "NIVEAU A2 · La rentrée · BACK TO SCHOOL")'),
    ('f.gloss("la rentrée 开学、复课 · reprendre 重新开始、复课 · un cartable 书包 · un décalage 错开、时差 · en revanche 相反、反之 · un rituel 习惯、仪式。")',
     'f.gloss("la rentrée the return to school · reprendre to start again · un cartable a schoolbag · un décalage a gap, a time difference · en revanche on the other hand · un rituel a habit, a ritual.")'),
    ('f.bridge("译注｜une valise 行李箱 · une ambiance 气氛 · le bilan 总结、盘点。")',
     'f.bridge("NOTE · une valise a suitcase · une ambiance an atmosphere · le bilan the round-up.")'),
    ('"说说你的开学：周一早上你在哪里？假期读了哪本书？写两句法语寄给编辑部。"',
     '"Tell us about your first day back: where were you on Monday morning? Which book did you read in the holidays? Write two sentences in French and send them to the editors."', 2),
    ('"ET VOUS ? · 说说你自己"', '"ET VOUS ? · YOUR TURN"'),
    ('"DIRE LA DATE · 这样说日期"', '"DIRE LA DATE · SAYING THE DATE"'),
    ('"lundi 2 novembre · 注意：1 日说 le premier，其余用基数词"',
     '"lundi 2 novembre · note: the 1st is le premier, other days use cardinal numbers"'),
    ('("lundi 2 novembre", "11 月 2 日星期一 · la rentrée")',
     '("lundi 2 novembre", "Monday 2 November · la rentrée")'),
    ('("mardi 3 novembre", "11 月 3 日星期二 · votes à l\'Assemblée")',
     '("mardi 3 novembre", "Tuesday 3 November · votes à l\'Assemblée")'),
    ('("mercredi 4 novembre", "11 月 4 日星期三 · sorties cinéma")',
     '("mercredi 4 novembre", "Wednesday 4 November · sorties cinéma")'),
    ('("samedi 7 novembre", "11 月 7 日星期六 · nocturne et demis")',
     '("samedi 7 novembre", "Saturday 7 November · nocturne et demis")'),
    ('("dimanche 8 novembre", "11 月 8 日星期日 · les finales")',
     '("dimanche 8 novembre", "Sunday 8 November · les finales")'),
    ('"EXERCICES · 第 2 版练习"', '"EXERCICES · PAGE 2 EXERCISES"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Answers on page 8 · exercises are mixed by level; find answers by number"'),
    ('e.bridge("用法语补全日期（注意星期与数字）。")',
     'e.bridge("Complete the dates in French (mind the weekday and the number).")'),
    ('"复课在星期一"', '"back to school on Monday"'),
    ('"11 月 1 日说 le premier"', '"1 November is le premier"'),
    ('"最后夜场在星期六"', '"the last night event is on Saturday"'),
    ('"决赛在星期日"', '"the finals are on Sunday"'),
    ('instr="填空"', 'instr="Fill in"', 4),
    ('e.bridge("用 aller + 动词原形改写（最近将来时）。")',
     'e.bridge("Rewrite with aller + infinitive (futur proche).")'),
    ('e.bridge("读第 2 版文章，选出正确答案。")',
     'e.bridge("Read page 2 and choose the right answer.")'),
    ('"三区同一周一早上复课"', '"all three zones go back on the same Monday morning"'),
    ('"冬令时从 10 月 25 日开始"', '"winter time began on 25 October"'),
    ('"11 月晚上天黑得早"', '"in November the night falls early"'),
    ('["rentrée=开学 a", "reprendre=重新开始 b", "cartable=书包 c", "rituel=习惯 d"]',
     '["rentrée = the return to school a", "reprendre = to start again b", "cartable = a schoolbag c", "rituel = a habit d"]'),
    ('instr="把词和释义配对"', 'instr="Match"'),
    ('instr="改写"', 'instr="Rewrite"', 4),
])

# ---------------- content34: P3 + P4
apply_file("content34.py", [
    ('# ================= P3 · 文化 (A2→B1) =================',
     '# ================= P3 · culture (A2->B1) ================='),
    ('p.band("CULTURE · 文化", "Le Lucerna", "NIVEAU A2 → B1 · Halloween, Toussaint · 万圣与诸圣")',
     'p.band("CULTURE · FESTIVALS", "Le Lucerna", "NIVEAU A2 → B1 · Halloween, Toussaint · HALLOWEEN AND ALL SAINTS")'),
    ('f.gloss("se déguiser 变装、装扮 · un sort 魔法、恶作剧 · une ambiance 气氛 · le souvenir 回忆、纪念 · confondre 混淆 · discret 低调的、安静的。")',
     'f.gloss("se déguiser to dress up · un sort a spell, a trick · une ambiance an atmosphere · le souvenir a memory · confondre to confuse · discret discreet, quiet.")'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · YOUR TURN", 25)', 2),
    ('f.bridge("判断对错（Vrai / Faux）。")', 'f.bridge("True or false (Vrai / Faux).")'),
    ('"万圣节在 10 月 31 日星期六"', '"Halloween was on Saturday 31 October"'),
    ('"诸圣节墓园摆满菊花"', '"on All Saints\' Day the cemeteries are full of chrysanthemums"'),
    ('"菊花绝不能当礼物送人"', '"chrysanthemums are never given as a present"'),
    ('"11 月 2 日是 jour des morts，不是诸圣节"', '"2 November is the jour des morts, not All Saints\' Day"'),
    ('"文中：le rire d\'abord, le souvenir ensuite"', '"in the text: le rire d\'abord, le souvenir ensuite"'),
    ('f.bridge("用 déguisement / tombe / citrouille / souvenir 填空。")',
     'f.bridge("Fill in with déguisement / tombe / citrouille / souvenir.")'),
    ('"万圣节穿变装服装"', '"children wear costumes at Halloween"'),
    ('"花放在墓碑上"', '"flowers are placed on the grave"'),
    ('"南瓜是万圣节的象征"', '"the pumpkin is the symbol of Halloween"'),
    ('"诸圣节是纪念之日"', '"All Saints\' Day is a day of remembrance"'),
    ('f.bridge("改写句子（用 ne...jamais / ne...plus / ne...pas）。")',
     'f.bridge("Rewrite the sentences (with ne...jamais / ne...plus / ne...pas).")'),
    ('"jamais + de（无冠词变化）"', '"jamais + de (no article change)"'),
    ('"ne...plus = 不再"', '"ne...plus = no longer"'),
    ('"n\'est pas = 不是"', '"n\'est pas = is not"'),
    ('instr="改写"', 'instr="Rewrite"', 3),
    ('f.bridge("即学即练 · 公园万圣节小题。")',
     'f.bridge("Your turn · little questions about the park at Halloween.")'),
    ('"周六 7 日是最后夜场"', '"Saturday 7th is the last night event"'),
    ('"敏感儿童有免费驱怪徽章"', '"sensitive children get a free monster-repellent badge"'),
    ('"阿斯泰里克斯公园在 Plailly"', '"the Astérix park is in Plailly"'),
    ('"Peur sur le Parc 10 月 3 日至 11 月 8 日"', '"Peur sur le Parc runs 3 October to 8 November"'),
    ('"恐惧等级用颜色区分"', '"the fear scale uses colours"'),
    ('"夜场从 19 点到凌晨 1 点"', '"the night event runs 7 p.m. to 1 a.m."'),
    ('"LES MOTS DES FÊTES · 节日词表"', '"LES MOTS DES FÊTES · FESTIVAL WORDS"'),
    ('"un saint — 圣人"', '"un saint — a saint"'),
    ('"un cimetière — 墓园"', '"un cimetière — a cemetery"'),
    ('"une tombe — 坟墓"', '"une tombe — a grave"'),
    ('"un jour férié — 公共假日"', '"un jour férié — a public holiday"'),
    ('"se souvenir — 纪念、想起"', '"se souvenir — to remember"'),
    ('"un déguisement — 变装服装"', '"un déguisement — a costume"'),
    ('"une citrouille — 南瓜"', '"une citrouille — a pumpkin"'),
    ('"un bonbon — 糖果"', '"un bonbon — a sweet"'),
    ('"un fantôme — 幽灵"', '"un fantôme — a ghost"'),
    ('"un sort — 魔法、诅咒"', '"un sort — a spell, a curse"'),
    ('"10 月 3 日至 11 月 8 日，12 场夜场；最后夜场 11 月 7 日；白天 10 点至 19 点开放。"',
     '"From 3 October to 8 November: 12 night events; the last one on 7 November; open 10 a.m. to 7 p.m. in the daytime."'),
    ('"DATES À RETENIR · 本周日历"', '"DATES À RETENIR · DATES TO REMEMBER"'),
    ('"注意：迪耶普扇贝集市在 11 月 14–15 日，不在本周。"',
     '"Note: the Dieppe scallop fair is on 14–15 November, not this week."'),
    ('# ================= P4 · 体育 (B1) =================',
     '# ================= P4 · sport (B1) ================='),
    ('p.band("SPORT · 体育", "Le Lucerna", "NIVEAU B1 · Tennis · Masters de Paris")',
     'p.band("SPORT · SPORTS", "Le Lucerna", "NIVEAU B1 · Tennis · Masters de Paris")'),
    ('f.gloss("un tournoi 锦标赛、赛事 · sur dur 硬地球场 · en salle 室内 · un tableau principal 正赛签表 · le tenant du titre 卫冕冠军 · basculer 逆转、倾斜 · les tribunes 看台。")',
     'f.gloss("un tournoi a tournament · sur dur on hard court · en salle indoors · un tableau principal the main draw · le tenant du titre the defending champion · basculer to swing, to turn · les tribunes the stands.")'),
    ('f.bridge("读第 4 版文章，选出正确答案。")',
     'f.bridge("Read page 4 and choose the right answer.")'),
    ('"决赛在周日 8 日"', '"the finals are on Sunday 8th"'),
    ('"大师赛在室内硬地球场举行"', '"the Masters is played indoors, on hard court"'),
    ('"2025 年卫冕冠军是辛纳"', '"the 2025 defending champion is Sinner"'),
    ('"法甲第十轮大场面：朗斯–马赛"', '"the big Ligue 1 match of the weekend: Lens – Marseille"'),
    ('"周日 8 日还有轮椅单打决赛（中午）"', '"on Sunday 8th there is also the wheelchair singles final (at noon)"'),
    ('f.bridge("把网球词和释义配对。")', 'f.bridge("Match the tennis words with their meanings.")'),
    ('["tournoi=赛事 a", "raquette=球拍 b", "tribunes=看台 c", "tenant=卫冕者 d"]',
     '["tournoi = tournament a", "raquette = racket b", "tribunes = stands c", "tenant = defending champion d"]'),
    ('instr="配对"', 'instr="Match"'),
    ('f.bridge("用比较级完成句子（plus / moins）。")',
     'f.bridge("Complete with the comparative (plus / moins).")'),
    ('"室内球速更快"', '"the ball is faster indoors"'),
    ('"大师赛是仅次于大满贯的级别"', '"a Masters 1000 is just below the Grand Slams"'),
    ('"室内赛季比室外短"', '"the indoor season is shorter than the summer season"'),
    ('f.bridge("译注｜un choc 强强对决 · recevoir 迎战、接待 · familier 熟悉的。")',
     'f.bridge("NOTE · un choc a big match · recevoir to host, to receive · familier familiar.")'),
    ('"« Allez ! » — 加油！ · « Quelle action ! » — 好球！"',
     '"« Allez ! » — Come on! · « Quelle action ! » — What a play!"'),
    ('"« Il marque ! » — 他得分了！ · « C\'est gagné ! » — 赢了！"',
     '"« Il marque ! » — He scores! · « C\'est gagné ! » — It\'s won!"'),
    ('"« Quel point ! » — 好球！（网球） · « Balle de match ! » — 赛点！"',
     '"« Quel point ! » — What a point! (tennis) · « Balle de match ! » — Match point!"'),
    ('"LES MOTS DU TENNIS · 网球词表"', '"LES MOTS DU TENNIS · TENNIS WORDS"'),
    ('"le tennis — 网球"', '"le tennis — tennis"'),
    ('"une balle — 球"', '"une balle — a ball"'),
    ('"un set — 一盘"', '"un set — a set"'),
    ('"un match — 比赛"', '"un match — a match"'),
    ('"un point — 一分"', '"un point — a point"'),
    ('"la finale — 决赛"', '"la finale — the final"'),
    ('"un adversaire — 对手"', '"un adversaire — an opponent"'),
    ('"un titre — 冠军头衔"', '"un titre — a title"'),
    ('"À SUIVRE · 拭目以待"', '"À SUIVRE · TO BE CONTINUED"'),
    ('mf.head("MICRO-DRILLS · 即学即练", 24)', 'mf.head("MICRO-DRILLS · QUICK PRACTICE", 24)'),
    ('mf.bridge("用 finale / quarts / demi-finales / tableau / fauteuil / choc 填空。")',
     'mf.bridge("Fill in with finale / quarts / demi-finales / tableau / fauteuil / choc.")'),
    ('"四分之一决赛在周五"', '"the quarter-finals are on Friday"'),
    ('"半决赛在周六"', '"the semi-finals are on Saturday"'),
    ('"单打决赛在周日"', '"the singles final is on Sunday"'),
    ('"正赛签表从周一开始"', '"the main draw starts on Monday"'),
    ('"轮椅赛事周五至周日"', '"the wheelchair tournament runs Friday to Sunday"'),
    ('"朗斯–马赛是周末焦点战"', '"Lens – Marseille is the big match of the weekend"'),
    ('p.text(ix + 22, db4 + 40, "LE DÉBAT · 讨论", 23, "sans", True, OLIVE)', 'p.text(ix + 22, db4 + 40, "LE DÉBAT · DEBATE", 23, "sans", True, OLIVE)'),
    ('"事先不知道决赛选手，是更刺激还是更扫兴？写两句支持、两句反对。"',
     '"Not knowing the finalists in advance: more exciting or more frustrating? Two sentences for, two against."'),
])

# ---------------- content56: P5 + P6
apply_file("content56.py", [
    ('# ================= P5 · 青年 (B1) =================',
     '# ================= P5 · youth (B1) ================='),
    ('p.band("JEUNESSE & MUSIQUE · 青年", "Le Lucerna", "NIVEAU B1 · Pitchfork Paris · 音乐节")',
     'p.band("JEUNESSE & MUSIQUE · YOUTH", "Le Lucerna", "NIVEAU B1 · Pitchfork Paris · MUSIC FESTIVAL")'),
    ('f.gloss("un lieu 场所、场地 · une affiche 海报 · les paroles 歌词 · donner le ton 定调子 · se promener 漫步、穿梭 · pile 正好、恰好。")',
     'f.gloss("un lieu a venue · une affiche a poster · les paroles the lyrics · donner le ton to set the tone · se promener to wander, to stroll · pile exactly, just.")'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · YOUR TURN", 25)'),
    ('f.bridge("读第 5 版文章，选出正确答案。")',
     'f.bridge("Read page 5 and choose the right answer.")'),
    ('"音乐节 11 月 2–8 日，整整一周"', '"the festival runs 2–8 November, a full week"'),
    ('"15 届音乐节"', '"the 15th edition of the festival"'),
    ('"Avant-Garde 在巴士底各场地，周四至周六"', '"Avant-Garde is in the Bastille venues, Thursday to Saturday"'),
    ('"俱乐部之夜在周五、周六"', '"the club nights are on Friday and Saturday"'),
    ('"开幕夜：Headache、Iceage、DIIV"', '"opening night: Headache, Iceage, DIIV"'),
    ('f.bridge("用 lieux / paroles / affiche / ambiance / danse / découvre 填空。")',
     'f.bridge("Fill in with lieux / paroles / affiche / ambiance / danse / découvre.")'),
    ('"10 个场地"', '"ten venues"'),
    ('"歌词也是法语学习材料"', '"song lyrics are French-learning material too"'),
    ('"海报上写着演出信息"', '"the poster gives the line-up"'),
    ('"每晚气氛各不相同"', '"a different atmosphere every night"'),
    ('"音乐节上人们跳舞"', '"at the festival people dance"'),
    ('"发现不认识的乐队"', '"discovering bands you do not know"'),
    ('f.bridge("把音乐词和释义配对。")', 'f.bridge("Match the music words with their meanings.")'),
    ('["concert=音乐会 a", "scène=舞台 b", "groupe=乐队 c", "billet=门票 d"]',
     '["concert = concert a", "scène = stage b", "groupe = band c", "billet = ticket d"]'),
    ('instr="配对"', 'instr="Match"', 2),
    ('f.bridge("补全对话（音乐节门口）。")',
     'f.bridge("Complete the dialogue (at the festival entrance).")'),
    ('"今晚演出的乐队"', '"the band playing tonight"'),
    ('"买两张票"', '"buying two tickets"'),
    ('"MOTS DE LA MUSIQUE · 音乐词表"', '"MOTS DE LA MUSIQUE · MUSIC WORDS"'),
    ('"un festival — 音乐节"', '"un festival — a festival"'),
    ('"un concert — 音乐会"', '"un concert — a concert"'),
    ('"une chanson — 歌曲"', '"une chanson — a song"'),
    ('"un chanteur — 歌手"', '"un chanteur — a singer"'),
    ('"danser — 跳舞"', '"danser — to dance"'),
    ('"écouter — 聆听"', '"écouter — to listen"'),
    ('"une salle — 演出厅"', '"une salle — a venue"'),
    ('"le public — 观众"', '"le public — the audience"'),
    ('"PARIS CREATOR WEEK · 创作者周"', '"PARIS CREATOR WEEK · CREATOR WEEK"'),
    ('"11 月 4–5 日拉维莱特：创作者周，线上创作者与观众线下见面。"',
     '"4–5 November at La Villette: Creator Week, online creators meeting their audience in person."'),
    ('p.text(ix + 22, ty5 + 40, "LE DÉBAT · 讨论", 23, "sans", True, OLIVE)', 'p.text(ix + 22, ty5 + 40, "LE DÉBAT · DEBATE", 23, "sans", True, OLIVE)'),
    ('"十个场地的音乐节，比单一大场馆更好吗？你听什么音乐学法语？"',
     '"A festival in ten venues: better than one big hall? What music do you listen to to learn French?"'),
    ('# ================= P6 · 时事 (B2) =================',
     '# ================= P6 · current affairs (B2) ================='),
    ('p.band("POLITIQUE & CHIFFRES · 时事", "Le Lucerna", "NIVEAU B2 · Budget 2027 · 预算周")',
     'p.band("POLITIQUE & CHIFFRES · POLITICS & NUMBERS", "Le Lucerna", "NIVEAU B2 · Budget 2027 · BUDGET WEEK")'),
    ('f.gloss("un budget 预算 · une mission （预算）分项 · un député 国民议会议员 · rejeter 否决 · à l\'unanimité 一致通过/否决 · un amendement 修正案。")',
     'f.gloss("un budget a budget · une mission a (budget) heading · un député a member of parliament · rejeter to reject · à l\'unanimité unanimously · un amendement an amendment.")'),
    ('"LE CALENDRIER PRÉVU · 计划中的投票日程（结果未出）"',
     '"LE CALENDRIER PRÉVU · THE PLANNED VOTING SCHEDULE (NO RESULTS YET)"'),
    ('"本页日程为计划安排，结果尚未产生，下期跟进。"',
     '"This schedule is the plan; no results yet — follow-up next issue."'),
    ('e6.head("LIRE LE CALENDRIER · 读日程", 25)',
     'e6.head("LIRE LE CALENDRIER · READING THE SCHEDULE", 25)'),
    ('e6.bridge("读上图日程，选出正确答案。")',
     'e6.bridge("Read the schedule above and choose the right answer.")'),
    ('"周二 3 日：文化与媒体"', '"Tuesday 3rd: Culture and Media"'),
    ('"周三 4 日：农业"', '"Wednesday 4th: Agriculture"'),
    ('"周四 5 日：国土协调与科研"', '"Thursday 5th: Territorial Cohesion and Research"'),
    ('"周五 6 日：公共财政与经济"', '"Friday 6th: Public Finance and the Economy"'),
    ('"10 月 23 日社保预算收入被 115–1 否决"', '"on 23 October the Social Security budget revenue was rejected 115–1"'),
    ('"参议院从 11 月 9 日起审议"', '"the Senate debates the text from 9 November"'),
    ('e6.head("LES MOTS · 词汇", 25)', 'e6.head("LES MOTS · WORDS", 25)'),
    ('["député=议员 a", "rejeter=否决 b", "vote=投票 c", "amendement=修正案 d"]',
     '["député = member of parliament a", "rejeter = to reject b", "vote = a vote c", "amendement = an amendment d"]'),
    ('"« Le texte part au Sénat. » — 法案送交参议院。"',
     '"« Le texte part au Sénat. » — The bill goes to the Senate."'),
    ('"« Ce calendrier peut encore bouger. » — 日程仍可能变动。"',
     '"« Ce calendrier peut encore bouger. » — The schedule may still change."'),
    ('"« Les résultats ne sont pas connus. » — 结果尚未揭晓。"',
     '"« Les résultats ne sont pas connus. » — The results are not known yet."'),
    ('g.bridge("译注｜prévu 预定的、计划的 · réaliser 实现、完成 · distinguer 区分。")',
     'g.bridge("NOTE · prévu planned · réaliser to carry out · distinguer to distinguish.")'),
    ('g2.bridge("用比较级完成句子。")', 'g2.bridge("Complete with the comparative.")'),
    ('"预算辩论比一场音乐会长"', '"a budget debate is longer than a concert"'),
    ('"预算比时间表复杂"', '"the budget is more complex than a schedule"'),
    ('"文化预算与农业预算同样重要"', '"the Culture budget is as important as the Agriculture budget"'),
    ('g2.head("MICRO-DRILLS · 即学即练", 25)', 'g2.head("MICRO-DRILLS · QUICK PRACTICE", 25)'),
    ('g2.bridge("用 examine / ont rejeté / part / peut / connus 填空。")',
     'g2.bridge("Fill in with examine / ont rejeté / part / peut / connus.")'),
    ('"国民议会审议预算"', '"the National Assembly debates the budget"'),
    ('"议员们否决收入部分"', '"the deputies rejected the revenue part"'),
    ('"法案送交参议院"', '"the bill goes to the Senate"'),
    ('"日程仍可能变动"', '"the schedule may still change"'),
    ('"结果尚未揭晓"', '"the results are not known yet"'),
    ('g2.head("LE DÉBAT · 讨论", 25)', 'g2.head("LE DÉBAT · DEBATE", 25)'),
    ('g2.bridge("讨论｜结果未出时，该不该先公布日程？区分 prévu（计划）与 décidé（已定）。")',
     'g2.bridge("Debate: should a schedule be announced before the results? Distinguish prévu (planned) from décidé (decided).")'),
])


# ---------------- content7: P7
apply_file("content7.py", [
    ('p.band("LANGUE EN MAIN · 精讲", "Le Lucerna", "A2 → B2 · Les phrases de la semaine · 本周金句")',
     'p.band("LANGUE EN MAIN · LANGUAGE IN DEPTH", "Le Lucerna", "A2 → B2 · Les phrases de la semaine · PHRASES OF THE WEEK")'),
    ('cA.head("NIVEAU A2 · 基础", 27)', 'cA.head("NIVEAU A2 · THE BASICS", 27)'),
    ('cB.head("NIVEAU B1 · 进阶", 27)', 'cB.head("NIVEAU B1 · STEP UP", 27)'),
    ('cC.head("NIVEAU B2 · 挑战", 27)', 'cC.head("NIVEAU B2 · THE CHALLENGE", 27)'),
    ('cD.head("BOÎTE À OUTILS · 工具箱", 27)', 'cD.head("BOÎTE À OUTILS · TOOLBOX", 27)'),
    ('cD.bridge("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。")',
     'cD.bridge("Toolbox: this issue\'s three pocket phrases, one per level; every phrase of the week comes from an article in this issue — reread the article and the phrase becomes easy.")'),
    ('p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE · 本周金句（全部出自本期文章）", 27, "sans", True, OLIVE)',
     'p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE · PHRASES OF THE WEEK", 27, "sans", True, OLIVE)'),
    ('p.text(RIGHT, py + 26, "每句一个语法点 + 一道小题 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")',
     'p.text(RIGHT, py + 26, "One grammar point + one mini-exercise per phrase · answers on page 8", 20, "sans", False, GREY, anchor="end")'),
    ('"语法点｜reprendre：复课、重新开始（pause 后）。"',
     '"Grammar point · reprendre: to go back, to start again (after a pause)."'),
    ('"语法点｜ne...pas encore：尚未、还不。"',
     '"Grammar point · ne...pas encore: not yet."'),
    ('"pas encore 尚未"', '"pas encore = not yet"'),
    ('"语法点｜passé composé 代动词：se + être + 过去分词。"',
     '"Grammar point · passé composé with reflexive verbs: se + être + past participle."'),
    ('"语法点｜comparatif：plus + 形容词，ou 对举。"',
     '"Grammar point · comparative: plus + adjective, two opposites joined by ou."'),
    ('"plus + 形容词"', '"plus + adjective"'),
    ('"语法点｜se promener：代动词，漫步、穿梭。"',
     '"Grammar point · se promener: reflexive verb, to stroll."'),
    ('"语法点｜pouvoir + 动词原形：可能、可以。"',
     '"Grammar point · pouvoir + infinitive: can, may."'),
    ('"语法点｜se jouer：决出胜负、上演（代动词）。"',
     '"Grammar point · se jouer: to be decided, to be played out (reflexive)."'),
    ('"语法点｜rencontrer：与观众见面；y 代指地点。"',
     '"Grammar point · rencontrer: to meet one\'s audience; y stands for the place."'),
    ('cf.head("CLINIQUE DES ERREURS · 易错诊所", 25)',
     'cf.head("CLINIQUE DES ERREURS", 25)'),
    ('cf.bridge("每句有一处错误：找出来并改正。")',
     'cf.bridge("The error clinic · Each sentence has one mistake: find it and correct it.")'),
    ('"jamais + de：否定句中 des 变 de"', '"jamais + de: in a negative sentence des becomes de"'),
    ('"主谓一致：créateurs 复数 → rencontrent，不是 rencontre"',
     '"Subject-verb agreement: créateurs is plural → rencontrent, not rencontre"'),
    ('"虚拟式：il examine，不加 s"', '"Subjunctive: il examine, no -s"'),
    ('"事实：决赛在 8 日，不是 7 日"', '"Fact: the final is on the 8th, not the 7th"'),
    ('instr="改错"', 'instr="Correct it"', 4),
    ('p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS · 读者园地", 24, "sans", True, OLIVE)',
     'p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS · READERS\' CORNER", 24, "sans", True, OLIVE)'),
    # Reader's corner: labelled editorial example (FR, frozen) + EN comment
    # WITH an explicit open-call imperative + EN disclosure of the
    # no-real-letter deferral. Fixed-position box: keep both EN paras
    # short (comment 2 lines, disclosure 2 lines) so nothing spills
    # past the box into the VOL.4 teaser strip.
    ('p.para(rx + 24, by7 + 196, "小墨点评｜编辑部示例：周末叙事用 passé composé 很稳，分号连接两天值得学。下期读者园地将点评真实投稿。", 20, "sans", False, GREY, rw - 48, 1.4)',
     'p.para(rx + 24, by7 + 196, "Editor\'s comment · An editorial example: steady passé composé, and a semicolon joining two days is worth copying. Send us your letter for VOL.4!", 20, "sans", False, GREY, rw - 48, 1.4)'),
    ('p.para(rx + 24, by7 + 336, "编辑部说明：截至付印，编辑部尚未收到 VOL.2 第 8 版的投稿作文（W44 未出刊），故本期刊登标注明确的编辑部示例；VOL.4 将兑现点评真实投稿的承诺。", 19.5, "sans", False, GREY, rw - 48, 1.4)',
     'p.para(rx + 24, by7 + 336, "Editor\'s note: no VOL.2 texts had arrived by press time (no W44 issue), so this issue prints a labelled editorial example; VOL.4 will comment on real submissions.", 19.5, "sans", False, GREY, rw - 48, 1.4)'),
    ('p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE · VOL.4 下周预告", 24, "sans", True, "#f3edda")',
     'p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE · VOL.4 NEXT WEEK", 24, "sans", True, "#f3edda")'),
    ('p.para(rx + 24, ty7 + 196, "下周：参议院审议社保预算、11 月 11 日停战纪念日、迪耶普扇贝集市；还有你们的来信！", 20, "sans", False, "#b3a06a", rw - 48, 1.4)',
     'p.para(rx + 24, ty7 + 196, "Next week: the Senate debates the Social Security budget, 11 November Armistice Day, the Dieppe scallop fair — and your letters, at last!", 20, "sans", False, "#b3a06a", rw - 48, 1.4)'),
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
# the English edition shows the same notes for the same exercises.
PRINT_NOTES = {%s}
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— PAGE {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and e["n"] in PRINT_NOTES:
            s += f" ({e['note']})"
        parts.append(s)''' % ", ".join(str(n) for n in PRINT_NOTES)
apply_file("content8.py", [
    ('p.band("EXERCICES & RÉPONSES · 练习与答案", "Le Lucerna", "综合评估 ÉVALUATION · 答案在本版下方")',
     'p.band("EXERCICES & RÉPONSES · EXERCISES & ANSWERS", "Le Lucerna", "ÉVALUATION · ANSWERS AT THE BOTTOM OF THIS PAGE")'),
    ('"11 月 8 日 2026 是星期日"', '"8 November 2026 is a Sunday"'),
    ('"去南泰尔看决赛"', '"going to Nanterre to see the finals"'),
    ('"决赛选手周六晚才揭晓"', '"the finalists are only known on Saturday night"'),
    ('"品尝语境（un régal）→ goûté"', '"tasting context (un régal) → goûté"'),
    ('"se promener 漫步"', '"se promener = to stroll"'),
    ('"avoir + 过去分词 goûté（不配合）"', '"avoir + past participle goûté (no agreement)"'),
    ('"les finales 主语复数 → ont lieu"', '"les finales is plural → ont lieu"'),
    ('"elle écrit 她写"', '"elle écrit = she writes"'),
    ('bf.head("A · TEXTE À TROUS · 完形填空", 24)', 'bf.head("A · TEXTE À TROUS · CLOZE", 24)'),
    ('bf.bridge("选项：")', 'bf.bridge("Options:")'),
    ('bf.head("B · CHOIX MULTIPLE · 单选", 24)', 'bf.head("B · CHOIX MULTIPLE · MULTIPLE CHOICE", 24)'),
    ('"7 nov. = samedi（最后夜场）"', '"7 Nov. = Saturday (last night event)"'),
    ('"nous → allons"', '"nous → allons"'),
    ('"s\'intéresser aux（à+les）"', '"s\'intéresser aux (à + les)"'),
    ('"si + imparfait（未完成过去时）→ conditionnel présent（条件式现在时）；j\' 是 je 在元音前的省音"',
     '"si + imparfait → conditionnel présent; j\' is je elided before a vowel"'),
    ('"主语 ce programme 三单 → semble"', '"ce programme is 3rd singular → semble"'),
    ('"将来时 aura lieu（决赛在周日）"', '"future aura lieu (the final is on Sunday)"'),
    ('"三区同日复课"', '"all three zones go back on the same day"'),
    ('"扇贝节在 11 月 7–8 日"', '"the scallop fair is on 7–8 November"'),
    ('bf.head("C · LECTURE · 阅读理解", 24)', 'bf.head("C · LECTURE · READING", 24)'),
    ('"夜场 19 点至凌晨 1 点"', '"the night event runs 7 p.m. to 1 a.m."'),
    ('"小徽章给小 Léo 驱怪"', '"the little badge is for little Léo, against monsters"'),
    ('"周日先看决赛再吃扇贝"', '"on Sunday first the finals, then the scallops"'),
    ('"周日晚上早睡因为周一上学"', '"on Sunday night early to bed because Monday is school"'),
    ('"周一是上学日（复课后正常周一）"', '"Monday is a school day (a normal Monday after the return)"'),
    ('bf.head("D · PHRASES · 完成句子与转换", 24)', 'bf.head("D · PHRASES · SENTENCE BUILDING", 24)'),
    ('"aller + 原形（futur proche）"', '"aller + infinitive (futur proche)"'),
    ('"si + 半过去时 venais"', '"si + imperfect venais"'),
    ('"passé composé : a + 过去分词"', '"passé composé: a + past participle"'),
    ('"selon moi = 在我看来"', '"selon moi = in my opinion"'),
    ('"il est prévu que + 虚拟式"', '"il est prévu que + subjunctive"'),
    ('bf.head("E · TRADUCTION · 翻译", 24)', 'bf.head("E · TRADUCTION · TRANSLATION", 24)'),
    # Translation items re-aimed for English readers (W43 precedent):
    # FR->reader key becomes the English translation; reader->FR items
    # print an English source sentence, French key unchanged.
    ('"读一份日程，本身就是在了解法国。"', '"Reading a programme is already a way of understanding France."'),
    ('"lire un programme = 读日程"', '"lire un programme = to read a programme"'),
    ('"Traduisez : « Lire un programme, c\'est déjà comprendre la France. »"',
     '"Translate into English: « Lire un programme, c\'est déjà comprendre la France. »"'),
    ('"比较级 plus vite + court"', '"comparative plus vite + court"'),
    ('"Traduisez : 他跑得比他哥哥更快。"', '"Translate: He runs faster than his brother."'),
    ('"être en vacances + depuis"', '"être en vacances + depuis"'),
    ('"Traduisez : 学生们自 10 月 17 日起就在放假。"', '"Translate: The pupils have been on holiday since 17 October."'),
    ('"futur proche + préparer"', '"futur proche + préparer"'),
    ('"Traduisez : 今晚，我们要准备书包。"', '"Translate: Tonight, we are going to prepare our schoolbags."'),
    ('"ne...pas encore = 尚未"', '"ne...pas encore = not yet"'),
    ('"Traduisez : 人们尚不知道决赛选手是谁。"', '"Translate: People do not know who the finalists are yet."'),
    ('bf.head("F · LES MOTS · 词汇配对", 24)', 'bf.head("F · LES MOTS · WORDS", 24)'),
    ('["tournoi=赛事 a", "nocturne=夜场 b", "budget=预算 c", "coquille=扇贝 d", "festival=音乐节 e"]',
     '["tournoi = tournament a", "nocturne = night event b", "budget = budget c", "coquille = scallop d", "festival = festival e"]'),
    ('instr="配对"', 'instr="Match"'),
    ('"11 月 7 日是星期六"', '"7 November is a Saturday"'),
    ('"在市场买扇贝"', '"buying scallops at the market"'),
    ('"goûter 品尝（原形）"', '"goûter = to taste (infinitive)"'),
    ('"à la portaise 是一种做法"', '"à la portaise is a way of cooking"'),
    ('"Bon week-end ! 周末愉快"', '"Bon week-end ! = have a good weekend"'),
    ('bf.head("G · DIALOGUE · 对话补全", 24)', 'bf.head("G · DIALOGUE · DIALOGUE COMPLETION", 24)'),
    ('reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")',
     'reg_ex("B1", "写作", "Open task — points in the writing box; model text in the MODÈLE box on this page", "marked against the points")'),
    ('p.text(wx, wy + 26, "H · ÉCRITURE · 写作", 25, "sans", True, OLIVE)',
     'p.text(wx, wy + 26, "H · ÉCRITURE · WRITING", 25, "sans", True, OLIVE)'),
    ('p.para(wx, wy + 190, "用法语写 80–100 词：我的 11 月 7–8 日周末。写清一场比赛、一个节日、一道菜。", 20, "sans", False, GREY, ww, 1.4)',
     'p.para(wx, wy + 190, "Write 80–100 words in French: \'My weekend of 7–8 November\'. Cover one match, one festival, one dish.", 20, "sans", False, GREY, ww, 1.4)'),
    ('p.text(mx2 + 22, wy + 38, "MODÈLE · 范文", 23, "sans", True, OLIVE)',
     'p.text(mx2 + 22, wy + 38, "MODÈLE · MODEL TEXT", 23, "sans", True, OLIVE)'),
    ('p.text(MX, ky + 26, "RÉPONSES · 全部答案与简析（第 1–8 版）", 26, "sans", True, OLIVE)',
     'p.text(MX, ky + 26, "RÉPONSES · ALL THE ANSWERS WITH NOTES (PAGES 1–8)", 26, "sans", True, OLIVE)'),
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
# R1-1 P1 headline overflow: the EN P1 gloss wrapped to 6 lines (core: 5),
# pushing the dates box into col 2 and the last ex past the flow bottom
# into the row-B image. Shortened gloss re-verified at 5 lines via wrap().
# R1-2 P6-ex head too wide (594px > 434): shortened to the form that fits.
# R1-3 P8 battery heads too wide: W43 FR x EN shipped short forms.
# R1-4 P8 keys flow ended 2570 > 2545: shortened the longest printed notes
# (each saves a wrapped line; keys unchanged).
section(2)
apply_file("content12.py", [
    ('f.gloss("se jouer to be decided, to be played out · une finale a final · une demi-finale a semi-final · un quart de finale a quarter-final · une nocturne a night event · un frisson a thrill · la coquille Saint-Jacques a scallop.")',
     'f.gloss("se jouer to be decided · une finale a final · une demi-finale a semi-final · un quart de finale a quarter-final · une nocturne a night event · un frisson a thrill · la coquille Saint-Jacques scallop.")'),
])
apply_file("content56.py", [
    ('e6.head("LIRE LE CALENDRIER · READING THE SCHEDULE", 25)',
     'e6.head("LIRE LE CALENDRIER · SCHEDULE", 25)'),
])
apply_file("content34.py", [
    ('"on All Saints\' Day the cemeteries are full of chrysanthemums"',
     '"cemeteries full of chrysanthemums"'),
    ('"2 November is the jour des morts, not All Saints\' Day"',
     '"2 November is the jour des morts"'),
    ('"sensitive children get a free monster-repellent badge"',
     '"sensitive children get a free badge"'),
])
apply_file("content56.py", [
    ('"on 23 October the Social Security budget revenue was rejected 115–1"',
     '"23 Oct.: revenue rejected 115–1"'),
    ('"the Culture budget is as important as the Agriculture budget"',
     '"Culture budget = Agriculture budget"'),
])
apply_file("content7.py", [
    ('"Subject-verb agreement: créateurs is plural → rencontrent, not rencontre"',
     '"créateurs is plural → rencontrent"'),
])
apply_file("content8.py", [
    ('bf.head("B · CHOIX MULTIPLE · MULTIPLE CHOICE", 24)',
     'bf.head("B · CHOIX MULTIPLE · MCQ", 24)'),
    ('bf.head("D · PHRASES · SENTENCE BUILDING", 24)',
     'bf.head("D · PHRASES · SENTENCES", 24)'),
    ('bf.head("G · DIALOGUE · DIALOGUE COMPLETION", 24)',
     'bf.head("G · DIALOGUE · COMPLETION", 24)'),
    ('"si + imparfait → conditionnel présent; j\' is je elided before a vowel"',
     '"si + imparfait → conditionnel; j\' = je elided"'),
    ('"on Sunday night early to bed because Monday is school"',
     '"early to bed: Monday is school"'),
    ('"Monday is a school day (a normal Monday after the return)"',
     '"Monday is a school day"'),
])
