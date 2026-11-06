# -*- coding: utf-8 -*-
"""DE x FR fan-out transform for W46 DE core build copy.
Generated from the EN pair table + tr-fr.py. German body text is
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
    rep(f, "weekly-report-w46-de-core", "weekly-report-w46-de-fr", 1)

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
    '"Die Lucerna · HEBDOMADAIRE ALLEMAND VOL.3 · TEXTE EN ALLEMAND · EXPLICATIONS EN FRANÇAIS"', 1)
rep("bslib4.py", 'f"\u7b2c {n} \u7248 / \u5171 {total} \u7248"', 'f"Page {n} sur {total}"', 1)
rep("bslib4.py", '"\u8bd1\u6ce8\uff5c" + s', '"Note — " + s', 1)

# ================= content12.py =================
C12 = [
    ('WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语', "WÖCHENTLICH AUF DEUTSCH · CHAQUE SEMAINE · L'ALLEMAND QUE LISENT LES ALLEMANDS"),
    ('德 语 周 报 · VOL.3 · 国 家 队 · 圣 马 丁 · NFL', 'JOURNAL ALLEMAND · VOL.3 · ÉQUIPE NATIONALE · SAINT-MARTIN · NFL'),
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")', 'p.text(975, 372, "TEXTE EN ALLEMAND · EXPLICATIONS EN FRANÇAIS — L\'ÉDITION POUR LES LECTEURS FRANCOPHONES", 20, "sans", True, BRICK, anchor="middle")'),
    ('本周国家队周 · 圣马丁节与 NFL', 'SEMAINE INTERNATIONALE · SAINT-MARTIN & NFL'),
    ('详见第 4 版 · Seite 4', 'Voir page 4'),
    ('DIE TOPMELDUNG · 头条', 'DIE TOPMELDUNG · À la une'),
    ('讲解｜die Länderspielpause 国家队比赛间歇期 · das Viertelfinale 四分之一决赛 · ausverkauft 售罄。', 'Notes — die Länderspielpause = trêve internationale · das Viertelfinale = quart de finale · ausverkauft = complet.'),
    ('DIE WOCHE IN ZAHLEN · 数字看本周', 'DIE WOCHE IN ZAHLEN · En chiffres'),
    ('5 — Punkte hat Deutschland nach vier Spielen in der Nations League（四轮过后德国队 5 分）', "5 — Punkte hat Deutschland nach vier Spielen in der Nations League (l'Allemagne a 5 points après quatre matches)"),
    ('11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（11 点 11 分狂欢季开幕）', '11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln (le carnaval commence à 11 h 11)'),
    ('15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（周日 15 点 30 分 NFL 开球）', '15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München (le match NFL commence dimanche à 15 h 30)'),
    ('JETZT ÜBEN · 即学即练', 'JETZT ÜBEN · À toi de jouer'),
    ('国家队比赛周', 'semaine de trêve internationale'),
    ('塞尔维亚首都', 'capitale de la Serbie'),
    ('狂欢季 11 点 11 分开幕', 'le carnaval commence à 11 h 11'),
    ('NFL 在慕尼黑', 'la NFL à Munich'),
    ('四轮 5 分', '5 points après quatre matches'),
    ('周日是纪念日', 'dimanche, jour du souvenir'),
    ('圣马丁节 11 月 11 日', "la Saint-Martin, c'est le 11 novembre"),
    ('11 月 11 日是星期三', 'le 11 novembre est un mercredi'),
    ('本周大问题 · Die Fragen der Woche', 'Grandes questions · Die Fragen der Woche'),
    ('德国本周最热议的五个问题。', "Les cinq questions qui agitent l'Allemagne."),
    ('IN DIESER AUSGABE · 本期目录', 'IN DIESER AUSGABE · Sommaire'),
    ('空场比赛（无观众）。详见第 4 版。', 'Un match sans spectateurs. Voir page 4.'),
    ('KURZ & GUT · 快讯', 'KURZ & GUT · En bref'),
    ('BLITZQUIZ · 闪电问答', 'BLITZQUIZ · Quiz éclair'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Lis la une, choisis la bonne réponse · Réponses page 8'),
    ('周五客战塞尔维亚', "à l'extérieur en Serbie vendredi"),
    ('NFL 下午 3 点半开球', "coup d'envoi NFL à 15 h 30"),
    ('纪念日在周日', "le jour du souvenir, c'est dimanche"),
    ('LEBEN · 生活', 'LEBEN · La vie'),
    ('LEVEL A2 · Der 11. November & der Alltag · 11 月 11 日与日常生活', 'LEVEL A2 · Der 11. November & der Alltag · Le 11 novembre et le quotidien'),
    ('der Jeck 狂欢者（科隆方言） · die fünfte Jahreszeit 第五个季节（狂欢季） · die Laterne 灯笼 · der Weckmann 面人面包 · die Martinsgans 圣马丁鹅。', 'der Jeck = fou du carnaval (dialecte de Cologne) · die fünfte Jahreszeit = la cinquième saison (carnaval) · die Laterne = lanterne · der Weckmann = bonhomme brioché · die Martinsgans = oie de la Saint-Martin.'),
    ('DER 11. NOVEMBER · 11 月 11 日', 'DER 11. NOVEMBER'),
    ('你过狂欢节还是圣马丁节？写两句德语寄来。', 'Karneval ou Saint-Martin ? Écris deux phrases en allemand !'),
    ('UND SIE? · 说说你自己', 'UND SIE? · Et toi ?'),
    ('MARTIN IN KÜRZE · 圣马丁简讯', 'MARTIN IN KÜRZE · En bref'),
    ('RECHNEN WIR MAL · 算一算', 'RECHNEN WIR MAL · Calculons'),
    ('Die Uhrzeiten der Woche · 本周时刻', 'Die Uhrzeiten der Woche · Les heures de la semaine'),
    ('注意：11 月 11 日是工作日。去科隆要早到：老城很挤，晚上街道属于提灯笼的孩子们。', 'Note : le 11 novembre est un jour travaillé. Arrive tôt à Cologne : la vieille ville est bondée, et le soir les rues sont aux enfants et à leurs lanternes.'),
    ('ÜBUNGEN · 第 2 版练习', 'ÜBUNGEN · Exercices page 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Réponses page 8 · Les niveaux se mélangent — retrouve chaque réponse par son numéro'),
    ('看第 2 版文章，用时间填空。', "Lis l'article page 2 et complète les heures."),
    ('WDR 10 点半直播', 'la WDR en direct dès 10 h 30'),
    ('Weckmann 是面人面包', 'un Weckmann est un bonhomme brioché'),
    ('11 月 11 日不是法定假日', "le 11 novembre n'est pas férié"),
    ('圣马丁鹅配红甘蓝和丸子', "l'oie de la Saint-Martin, chou rouge et quenelles"),
    ('改成 Perfekt 现在完成时。', 'Réécris au Perfekt (passé composé).'),
    ('读第 2 版文章，选出正确答案。', "Lis l'article page 2 et choisis la bonne réponse."),
    ('Jeck=狂欢者 c', 'Jeck=fou du carnaval c'),
    ('Laterne=灯笼 a', 'Laterne=lanterne a'),
    ('Weckmann=面人面包 b', 'Weckmann=bonhomme brioché b'),
    ('Martinsgans=圣马丁鹅 d', 'Martinsgans=oie de la Saint-Martin d'),
]
rep_all("content12.py", C12)

# ================= content34.py =================
C34 = [
    ('KULTUR · 文化', 'KULTUR · Culture'),
    ('A2 → B1 · St. Martin, Karneval & Rückblick · 圣马丁、狂欢节与回顾', 'A2 → B1 · St. Martin, Karneval & Rückblick · Saint-Martin, carnaval et retour en arrière'),
    ('der Bettler 乞丐 · der Mantel 斗篷 · das Geschnatter 鹅叫声 · der Gänsestall 鹅棚 · das Dreigestirn 狂欢节三人组。', 'der Bettler = mendiant · der Mantel = manteau · das Geschnatter = caquètement · der Gänsestall = étable des oies · das Dreigestirn = triumvirat du carnaval.'),
    ('ST. MARTIN · 圣马丁', 'ST. MARTIN · Saint-Martin'),
    ('die Laterne — 灯笼', 'die Laterne — lanterne'),
    ('der Mantel — 斗篷', 'der Mantel — manteau'),
    ('die Gans — 鹅', 'die Gans — oie'),
    ('der Weckmann — 面人面包', 'der Weckmann — bonhomme brioché'),
    ('das Martinsfeuer — 圣马丁篝火', 'das Martinsfeuer — feu de la Saint-Martin'),
    ('das Kostüm — 服装', 'das Kostüm — costume'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · Saint-Martin'),
    ('UND SIE? · 说说你自己', 'UND SIE? · Et toi ?'),
    ('你做过灯笼吗？你们国家的孩子唱什么歌？写两句德语寄来。', 'Tu as fait une lanterne ? Écris deux phrases en allemand !'),
    ('DER TIPP · 编辑部建议', 'DER TIPP · Conseil'),
    ('ÜBUNGEN · 第 3 版练习', 'ÜBUNGEN · Exercices page 3'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Réponses page 8 · Les niveaux se mélangent — retrouve chaque réponse par son numéro'),
    ('读第 3 版文章，判断对错。', "Lis l'article page 3. Vrai ou faux ?"),
    ('传说马丁是罗马士兵', 'la légende dit que Martin était soldat romain'),
    ('传说鹅叫声暴露了他', "la légende dit que les oies l'ont trahi"),
    ('纪念日 11 月 11 日', "le jour du souvenir, c'est le 11 novembre"),
    ('截稿时 11 月 3–8 日结果未知', 'résultats du 3 au 8 novembre inconnus au bouclage'),
    ('狂欢季 11 点 11 分开幕', 'le carnaval commence à 11 h 11'),
    ('用方框里的词填空。', "Complète avec les mots de l'encadré."),
    ('斗篷分给乞丐', 'le manteau partagé avec le mendiant'),
    ('纸灯笼', 'une lanterne en papier'),
    ('圣马丁鹅', "l'oie de la Saint-Martin"),
    ('圣马丁鹅配红甘蓝和丸子', "l'oie de la Saint-Martin, chou rouge et quenelles"),
    ('狂欢节服装', 'un costume de carnaval'),
    ('游行在篝火处结束', 'le cortège finit au feu de joie'),
    ('选出正确答案。', 'Choisis la bonne réponse.'),
    ('马丁后来成为图尔主教', 'Martin devient plus tard évêque de Tours'),
    ('灯笼游行常在前后晚上举行', 'les cortèges aux lanternes ont souvent lieu les soirs voisins'),
    ('VOL.4 报道 11 月 3–8 日结果', 'VOL.4 racontera les résultats du 3 au 8 novembre'),
    ('把词组成正确的句子。', 'Remets les mots dans une phrase correcte.'),
    ('主谓宾顺序', 'ordre sujet–verbe–objet'),
    ('时间状语开头，动词第二位', "le temps d'abord, le verbe en deuxième"),
    ('地点开头，动词第二位', "le lieu d'abord, le verbe en deuxième"),
    ('SPORT · 体育', 'SPORT · Sport'),
    ('LEVEL B1 · Nationalelf & NFL · 国家队与 NFL', 'LEVEL B1 · Nationalelf & NFL · Équipe nationale et NFL'),
    ('das Geisterspiel 空场比赛 · das Hinspiel 首回合 · ausverkauft 售罄 · der Star 明星 · gewinnen 获胜。', 'das Geisterspiel = match fantôme · das Hinspiel = match aller · ausverkauft = complet · der Star = star · gewinnen = gagner.'),
    ('你更爱看足球还是美式橄榄球？贝尔格莱德谁赢？写两句德语寄来。', 'Foot ou foot US ? Qui gagne ? Deux phrases en allemand !'),
    ('DER SPIELPLAN · 本周与下周赛程', 'DER SPIELPLAN · Cette semaine et la suivante'),
    ('ÜBUNGEN · 第 4 版练习', 'ÜBUNGEN · Exercices page 4'),
    ('读第 4 版文章，选出正确答案。', "Lis l'article page 4 et choisis la bonne réponse."),
    ('德国 5 分，荷兰希腊各 8 分', "l'Allemagne 5 points, les Pays-Bas et la Grèce 8 chacun"),
    ('主教练 11 月 5 日公布名单', 'le sélectionneur annonce sa liste le 5 novembre'),
    ('贝尔格莱德空场', 'stade vide à Belgrade'),
    ('首回合德国 2:0 胜塞尔维亚', "l'Allemagne a gagné l'aller 2-0 contre la Serbie"),
    ('NFL 慕尼黑赛售罄', 'le match NFL de Munich est complet'),
    ('Geisterspiel=空场比赛 b', 'Geisterspiel=match fantôme b'),
    ('Hinspiel=首回合 a', 'Hinspiel=match aller a'),
    ('Ausrüster=装备赞助商 c', 'Ausrüster=équipementier c'),
    ('ausverkauft=售罄 d', 'ausverkauft=complet d'),
    ('用比较级完成句子（括号里是原级）。', 'Complète au comparatif (le mot entre parenthèses est au positif).'),
    ('viel → mehr（荷兰 8 分多于德国 5 分）', "viel → mehr (les Pays-Bas ont 8 points, plus que les 5 de l'Allemagne)"),
    ('spät → später（15:30 晚于 11:11）', 'spät → später (15 h 30 est plus tard que 11 h 11)'),
    ('leise → leiser（空场比主场安静）', "leise → leiser (un stade vide est plus silencieux qu'un match à domicile)"),
    ('früh → früher（11 月 5 日早于 11 月 13 日）', 'früh → früher (le 5 novembre est plus tôt que le 13 novembre)'),
    ('看上面的赛程表，选出正确答案。', 'Regarde le calendrier ci-dessus et choisis la bonne réponse.'),
    ('塞尔维亚–德国周五 20:45', 'Serbie–Allemagne vendredi à 20 h 45'),
    ('NFL 周日 15:30', 'NFL dimanche à 15 h 30'),
    ('德国–荷兰周一 20:45', 'Allemagne–Pays-Bas lundi à 20 h 45'),
    ('拜仁–科隆周五 20:30', 'Bayern–Köln vendredi à 20 h 30'),
    ('沙尔克–斯图加特周六 17:30', 'Schalke–Stuttgart samedi à 17 h 30'),
]
rep_all("content34.py", C34)

# ================= content56.py =================
C56 = [
    ('JUGEND · 青年', 'JUGEND · Jeunesse'),
    ('LEVEL B1 · Laternen, Lieder & Schule · 灯笼、歌曲与学校', 'LEVEL B1 · Laternen, Lieder & Schule · Lanternes, chansons et école'),
    ('basteln 制作 · der Pausenhof 课间操场 · sich verkleiden 乔装打扮 · die Stimmung 气氛 · der Pirat 海盗。', 'basteln = bricoler · der Pausenhof = cour de récré · sich verkleiden = se déguiser · die Stimmung = ambiance · der Pirat = pirate.'),
    ('SCHULWOCHE · 开学周', 'SCHULWOCHE · La rentrée'),
    ('die Laterne — 灯笼', 'die Laterne — lanterne'),
    ('basteln — 制作', 'basteln — bricoler'),
    ('das Lied — 歌曲', 'das Lied — chanson'),
    ('das Kostüm — 服装', 'das Kostüm — costume'),
    ('der Umzug — 游行', 'der Umzug — cortège'),
    ('der Stern — 星星', 'der Stern — étoile'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · Saint-Martin'),
    ('UND SIE? · 说说你自己', 'UND SIE? · Et toi ?'),
    ('你小时候做过灯笼吗？11 月你唱哪首歌？写两句德语寄来。', 'Une lanterne enfant ? Ta chanson ? Deux phrases en allemand !'),
    ('DER WOCHENPLAN DER REDAKTION · 编辑部一周计划', 'DER WOCHENPLAN DER REDAKTION · La semaine de la rédaction'),
    ('ÜBUNGEN · 第 5 版练习', 'ÜBUNGEN · Exercices page 5'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Réponses page 8 · Les niveaux se mélangent — retrouve chaque réponse par son numéro'),
    ('读第 5 版文章，选出正确答案。', "Lis l'article page 5 et choisis la bonne réponse."),
    ('11 月 9 日全德复课', 'la rentrée partout le 9 novembre'),
    ('孩子们做纸灯笼', 'les enfants fabriquent des lanternes en papier'),
    ('纸灯笼', 'une lanterne en papier'),
    ('上午狂欢，下午圣马丁', "carnaval le matin, Saint-Martin l'après-midi"),
    ('NFL 周日在电视上', 'la NFL à la télé dimanche'),
    ('周五看国家队比赛', "regarder l'équipe nationale vendredi"),
    ('用方框里的词填空。', "Complète avec les mots de l'encadré."),
    ('做灯笼', 'fabriquer des lanternes'),
    ('唱圣马丁歌曲', 'chanter les chansons de la Saint-Martin'),
    ('狂欢节服装', 'un costume de carnaval'),
    ('灯笼游行', 'un cortège aux lanternes'),
    ('灯笼上的星星', "l'étoile sur la lanterne"),
    ('用 weil 连接两个句子（动词放句末）。', 'Relie les deux phrases avec weil (le verbe va à la fin).'),
    ('weil 句动词置尾', 'dans une subordonnée en weil, le verbe va à la fin'),
    ('ist 置尾', 'ist va à la fin'),
    ('will 置尾', 'will va à la fin'),
    ('beginnt 置尾', 'beginnt va à la fin'),
    ('判断对错。', 'Vrai ou faux ?'),
    ('11 月 9 日巴伐利亚也复课', 'la Bavière aussi de retour le 9 novembre'),
    ('灯笼游行在晚上', 'le cortège aux lanternes a lieu le soir'),
    ('孩子们唱圣马丁歌曲', 'les enfants chantent les chansons de la Saint-Martin'),
    ('VERTIEFUNG · 深读', 'VERTIEFUNG · Approfondissement'),
    ('LEVEL B2 · Volkstrauertag & Stromsteuer · 纪念日与电力税', "LEVEL B2 · Volkstrauertag & Stromsteuer · Jour du souvenir et taxe sur l'électricité"),
    ('gedenken 纪念 · die Kranzniederlegung 献花圈 · der stille Tag 安静日 · die Verbundenheit 联系 · die Versöhnung 和解。', 'gedenken = commémorer · Kranzniederlegung = gerbe · stille Tag = jour de silence · Verbundenheit = lien · Versöhnung = réconciliation.'),
    ('DIE ZAHLEN · 本周数字', 'DIE ZAHLEN · Les chiffres'),
    ('纪念日：纪念需要安静——对此几乎人人赞同。电力税：降多少尚未确定。两者都关系到几乎每个家庭。', "Jour du souvenir : se souvenir demande du silence — presque tout le monde est d'accord. Taxe sur l'électricité : la baisse reste ouverte. Les deux touchent presque chaque foyer."),
    ('ZWEI SONNTAGE IM NOVEMBER · 十一月的两个周日', 'ZWEI SONNTAGE IM NOVEMBER · Deux dimanches de novembre'),
    ('WAS INTERESSIERT DIE LESER? · 读者最关心什么？', "WAS INTERESSIERT DIE LESER? · Qu'est-ce qui intéresse les lecteurs ?"),
    ('("Nations League und NFL", 46, "足球")', '("Nations League und NFL", 46, "football")'),
    ('("St. Martin und Karneval", 34, "节日")', '("St. Martin und Karneval", 34, "fêtes")'),
    ('("Volkstrauertag und Gedenken", 20, "纪念")', '("Volkstrauertag und Gedenken", 20, "mémoire")'),
    ('ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）', "ÜBUNGSDATEN · Données d'exercice — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Données d'exercice, pas un vrai sondage.)"),
    ('ÜBUNGEN · 第 6 版练习', 'ÜBUNGEN · Exercices page 6'),
    ('看上面的练习图表，选出正确答案。', "Utilise le graphique d'exercice ci-dessus."),
    ('46% 足球最受关注', 'le football en tête avec 46 %'),
    ('节日 34% 第二', 'les fêtes deuxièmes avec 34 %'),
    ('纪念 20% 最小', 'le souvenir le plus petit avec 20 %'),
    ('纪念 20%', 'le souvenir 20 %'),
    ('读第 6 版深读文章，选出正确答案。', "Lis l'article page 6."),
    ('11 月 15 日纪念日', "le jour du souvenir, c'est le 15 novembre"),
    ('ZDF 13 点半直播纪念仪式', 'la ZDF en direct dès 13 h 30'),
    ('家庭电力税 2.05 欧分', 'la taxe des foyers est de 2,05 centimes'),
    ('2027 年预算 11 月 27 日表决', 'vote du budget 2027 le 27 novembre'),
    ('用括号里的形式填空。', 'Complète avec la forme entre parenthèses.'),
    ('被动：wird + Partizip II', 'passif : wird + participe passé'),
    ('ob 引导间接疑问句', 'ob introduit une question indirecte'),
    ('献花圈仪式', 'une cérémonie de dépôt de gerbe'),
    ('为和平与和解', 'pour la paix et la réconciliation'),
    ('德奥联系', 'le lien germano-autrichien'),
    ('纪念受害者', 'se souvenir des victimes'),
]
rep_all("content56.py", C56)

# ================= content7.py =================
C7 = [
    ('SPRACHE · 语言', 'SPRACHE · La langue'),
    ('A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所', 'A2 → B2 · Sätze der Woche & Fehlerklinik · Phrases de la semaine et clinique des erreurs'),
    ('本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。', 'Cette page est consacrée à la langue : trois petites leçons, les phrases de la semaine (citées mot pour mot dans les articles de ce numéro), la clinique des erreurs et le courrier des lecteurs.'),
    ('BEISPIELE · 例句', 'BEISPIELE · Exemples'),
    ('被动：wird + Partizip II', 'passif : wird + participe passé'),
    ('复数：werden', 'pluriel : werden'),
    ('werden + 原形表将来', 'werden + infinitif pour le futur'),
    ('被动语态', 'voix passive'),
    ('lang → länger（夜晚比白天长）', 'lang → länger (la nuit est plus longue que le jour)'),
    ('weil 引导原因', 'weil introduit une raison'),
    ('weil 句动词置尾', 'dans une subordonnée en weil, le verbe va à la fin'),
    ('länger als = 比……更长', 'länger als = plus long que'),
    ('„Länger als sonst“ heißt... A. 比平时更长 · B. 和平时一样 · C. 比平时更短', "„Länger als sonst“ veut dire... A. plus long que d'habitude · B. comme d'habitude · C. plus court que d'habitude"),
    ('ob 引导间接疑问', 'ob introduit une question indirecte'),
    ('Es ist fraglich, ob ... = 是否还难说', 'Es ist fraglich, ob ... = il est douteux que ...'),
    ('dass 句动词置尾', 'dans une subordonnée en dass, le verbe va à la fin'),
    ('礼貌表达观点', 'une façon polie de donner son avis'),
    ('11.11 Uhr = 11 点 11 分', '11.11 Uhr = 11 h 11'),
    ('vor leeren Rängen = 空场，没有观众', 'vor leeren Rängen = stade vide'),
    ('Es wird gespielt. = 比赛将进行（被动）', 'Es wird gespielt. = Il sera joué'),
    ('Meiner Meinung nach ... = 在我看来……', 'Meiner Meinung nach = à mon avis'),
    ('Ich finde, dass ... = 我觉得……', 'Ich finde, dass = je trouve que'),
    ('Es ist fraglich, ob ... = 是否……还难说', 'Es ist fraglich, ob ... = on doute que'),
    ('DER WERKZEUGKASTEN · 工具箱', 'DER WERKZEUGKASTEN'),
    ('label = "Ein Beispiel der Redaktion!"', 'label = "Un exemple de la rédaction !"'),
    ('编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.4。请寄来您的习作，优秀者刊登于 VOL.4。', "Exemple de la rédaction, pas une vraie lettre : aucune vraie lettre n'était arrivée au bouclage. Envoyez-nous les vôtres pour VOL.4 !"),
    ('LESERBRIEFE · 读者来信', 'LESERBRIEFE · Courrier'),
    ('NOCH EIN WORT · 再学一词', 'NOCH EIN WORT · Encore un mot'),
    ('«das Geisterspiel»（Seite 4）: ein Spiel ohne Zuschauer im Stadion. 空场比赛。', '«das Geisterspiel» (Seite 4) : ein Spiel ohne Zuschauer im Stadion. Un match fantôme : un match sans spectateurs.'),
    ('SÄTZE DER WOCHE · 本周金句', 'SÄTZE DER WOCHE · Phrases de la semaine'),
    ('原文摘录，逐字引自本期文章 · 括号内为出处', 'Cité mot pour mot dans les articles de ce numéro · source entre crochets'),
    ('德甲休战——但国家队要比赛。', "La Bundesliga s'arrête — mais l'équipe nationale joue."),
    ('11 点 11 分，科隆新一季狂欢季开幕。', 'À 11 h 11, la nouvelle session du carnaval commence à Cologne.'),
    ('他的纪念日是 11 月 11 日。', "Son jour du souvenir, c'est le 11 novembre."),
    ('书包收拾好了，操场上又热闹起来。', 'Les cartables sont prêts, les cours de récré bruissent à nouveau.'),
    ('十一月黑暗，但并不安静：它歌唱、发光、庆祝。', 'Novembre est sombre, mais pas silencieux : il chante, brille et fête.'),
    ('比赛售罄，RTL 现场直播。', 'Le match est complet ; RTL diffuse en direct.'),
    ('这里的纪念意味着：停下来、记住——并为和平与和解挺身而出。', "Ici, se souvenir veut dire : s'arrêter, se rappeler — et défendre la paix et la réconciliation."),
    ('周日，全国一片安静。', 'Dimanche, le pays est silencieux.'),
    ('FEHLERKLINIK · 纠错诊所', 'FEHLERKLINIK · La clinique des erreurs'),
    ('学习者最常犯的四个错 · 先自己改，再看答案', "Quatre erreurs fréquentes des apprenants · corrige d'abord, puis vérifie"),
    ('动词第二位：主语不在句首时，动词仍居第二。', "Verbe en deuxième : même si le sujet n'est pas premier, le verbe reste deuxième."),
    ('halb zwölf = 十一点半（zwölf 之前）。', 'halb zwölf = 11 h 30, une demi-heure avant zwölf.'),
    ('Perfekt 中 Partizip II 放句末。', 'Au Perfekt, le participe passé va à la fin.'),
    ('ob 从句动词放句末。', 'Dans une subordonnée en ob, le verbe va à la fin.'),
    ('IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.4)', 'IN DER NÄCHSTEN AUSGABE · Prochain numéro (VOL.4)'),
]
rep_all("content7.py", C7)

# ================= content8.py =================
C8 = [
    ('ÜBUNGEN & ANTWORTEN · 练习与答案', 'ÜBUNGEN & ANTWORTEN · Exercices & réponses'),
    ('SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方', 'SCHLUSSTEST · Test final · Alle Antworten unten auf dieser Seite — toutes les réponses en bas de cette page'),
    ('beginnt（第三人称单数）', 'beginnt (3e personne du singulier)'),
    ('bastelt（第三人称单数）', 'bastelt (3e personne du singulier)'),
    ('geht（第三人称单数）', 'geht (3e personne du singulier)'),
    ('singt（第三人称单数）', 'singt (3e personne du singulier)'),
    ('schaut（第三人称单数）', 'schaut (3e personne du singulier)'),
    ('sieht（第三人称单数）', 'sieht (3e personne du singulier)'),
    ('erzählt（第三人称单数）', 'erzählt (3e personne du singulier)'),
    ('A · LÜCKENTEXT · 完形填空', 'A · LÜCKENTEXT · Texte à trous'),
    ('选项：', 'Options :'),
    ('B · WISSENSFRAGEN · 综合问答', 'B · WISSENSFRAGEN · Quiz'),
    ('狂欢季 11 点 11 分开幕', 'le carnaval commence à 11 h 11'),
    ('周五客战塞尔维亚', "à l'extérieur en Serbie vendredi"),
    ('NFL 周日 15:30', 'NFL dimanche à 15 h 30'),
    ('纪念日 11 月 15 日', "le jour du souvenir, c'est le 15 novembre"),
    ('家庭电力税 2.05 欧分', 'la taxe des foyers est de 2,05 centimes'),
    ('主教练 11 月 5 日公布名单', 'le sélectionneur annonce sa liste le 5 novembre'),
    ('ZDF 13 点半直播纪念仪式', 'la ZDF en direct dès 13 h 30'),
    ('亡灵主日 11 月 22 日', "Totensonntag, c'est le 22 novembre"),
    ('C · LESEVERSTEHEN · 阅读理解', 'C · LESEVERSTEHEN · Lecture'),
    ('周三做灯笼', 'fabriquer une lanterne mercredi'),
    ('周五看德国队', "regarder l'Allemagne vendredi"),
    ('D · SÄTZE BAUEN · 造句', 'D · SÄTZE BAUEN · Phrases'),
    ('时间状语，动词第二位', 'le temps, le verbe en deuxième'),
    ('主谓宾顺序', 'ordre sujet–verbe–objet'),
    ('时间状语开头，动词第二位', "le temps d'abord, le verbe en deuxième"),
    ('地点时间开头，动词第二位', "lieu et temps d'abord, verbe en deuxième"),
    ('E · ÜBERSETZEN · 翻译', 'E · ÜBERSETZEN · Traduction'),
    ('狂欢节 11 点 11 分在科隆开幕。', 'Le carnaval commence à 11 h 11 à Cologne.'),
    ('beginnen = 开始', 'beginnen = commencer'),
    ('Der Karneval beginnt um 11.11 Uhr in Köln.（译成中文）', 'Der Karneval beginnt um 11.11 Uhr in Köln. (traduire en français)'),
    ('我周三做一个灯笼。', 'Je fabrique une lanterne mercredi.'),
    ('basteln = 制作', 'basteln = bricoler'),
    ('Ich bastle am Mittwoch eine Laterne.（译成中文）', 'Ich bastle am Mittwoch eine Laterne. (traduire en français)'),
    ('学校 11 月 9 日又开学了。', "L'école a recommencé le 9 novembre."),
    ('wieder begonnen = 又开始', 'wieder begonnen = recommencé'),
    ('Die Schule hat am 9. November wieder begonnen.（译成中文）', 'Die Schule hat am 9. November wieder begonnen. (traduire en français)'),
    ('看比赛 = das Spiel schauen', 'regarder un match = das Spiel schauen'),
    ('"我周日看 NFL 比赛。（译成德语）", instr="翻译"', '"Je regarde le match NFL dimanche. (traduire en allemand)", instr="Traduire en allemand"'),
    ('F · WÖRTER PAAREN · 词汇配对', 'F · WÖRTER PAAREN · Paires'),
    ('Mantel=斗篷 b', 'Mantel=manteau b'),
    ('Laterne=灯笼 a', 'Laterne=lanterne a'),
    ('Geisterspiel=空场比赛 d', 'Geisterspiel=match fantôme d'),
    ('Versöhnung=和解 c', 'Versöhnung=réconciliation c'),
    ('singst（第二人称单数）', 'singst (2e personne du singulier)'),
    ('macht（第二人称复数）', 'macht (2e personne du pluriel)'),
    ('essen（第一人称复数）', 'essen (1re personne du pluriel)'),
    ('machst（第二人称单数）', 'machst (2e personne du singulier)'),
    ('schaue（第一人称单数）', 'schaue (1re personne du singulier)'),
    ('G · DIALOG · 对话补全', 'G · DIALOG · Dialogue'),
    ('开放题 — 要点见写作框，范文在第 8 版写作框内', "Tâche ouverte — suis les points de l'encadré ; le texte modèle est dans l'encadré de cette page"),
    ('按要点给分', 'Noté selon les points listés'),
    ('H · SCHREIBEN · 写作', 'H · SCHREIBEN · Rédaction'),
    ('用德语写 80–100 词：《我的十一月的一周》。写清做什么手工、看哪几场比赛、和谁一起，并写一句关于圣马丁节或纪念日的话。', 'Écris en allemand, 80–100 mots : « Ma semaine de novembre ». Dis ce que tu fabriques, quels matches tu regardes et avec qui — et ajoute une phrase sur la Saint-Martin ou le jour du souvenir.'),
    ('MUSTER · 范文（84 Wörter）', 'MUSTER · Texte modèle (84 mots)'),
    ('ANTWORTEN · 全部答案与简析（第 1–8 版）', 'ANTWORTEN · Toutes les réponses avec notes (pages 1–8)'),
]
rep_all("content8.py", C8)

# ---------- P8 keys ----------
rep("content8.py", 'kf.para(f"— \u7b2c {pg} \u7248 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— Page {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"\uff08{e[\'note\']}\uff09"',
    's += f"({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)', 1)

# ---------- generic value maps ----------
TYPEMAP = [('完成句子', 'à compléter'), ('单选', 'QCM'), ('句型转换', 'transformation'), ('词汇配对', 'appariement'), ('判断对错', 'vrai/faux'), ('完形填空', 'texte à trous'), ('造句', 'construction de phrase'), ('对话补全', 'dialogue à compléter'), ('翻译', 'traduction'), ('写作', 'rédaction')]
INSTRMAP = [('instr="填空"', 'instr="Compléter"'), ('instr="改写"', 'instr="Réécrire"'), ('instr="判断"', 'instr="Vrai ou faux ?"'), ('instr="造句"', 'instr="Former une phrase"'), ('instr="翻译"', 'instr="Traduire en français"'), ('instr="把词和释义配对"', 'instr="Relier les paires"')]
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
