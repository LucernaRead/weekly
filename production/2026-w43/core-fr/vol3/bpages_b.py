# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-vol3/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 阅读文化版 =================
p = BSPage()
y = p.band("第 三 版", "阅读 · 文化 · 趣味", "READING · CULTURE · FUN")

x, w = span_x(0, 2)
ay = p.shead(x, y + 30, "阅读 A · 节日", w) + 42
ay = p.para(x, ay, "« La fête du Double Neuf »", 34, "serif", True, INK, w, 1.2) + 8
ay = p.para(x, ay, "Le 18 octobre, la Chine fête le Double Neuf, la fête des aînés. Ce jour-là, on monte sur les montagnes, on regarde les chrysanthèmes et on pense aux personnes âgées. En France, il y a une autre fête pour les morts et les souvenirs : la Toussaint, le 1er novembre. Ce jour-là, les familles vont au cimetière et mettent des chrysanthèmes sur les tombes. Deux pays, deux fêtes, mais la même idée : ne pas oublier les aînés. En Chine comme en France, le chrysanthème est la fleur de l'automne et du souvenir.", 23.5, "serif", False, INK, w, 1.48) + 10
ay = p.para(x, ay, "注释｜la fête 节日 · aîné 长辈 · monter 登上 · chrysanthème 菊花 · cimetière 墓地 · tombe 坟墓 · souvenir 回忆", 21, "serif", False, GREY, w, 1.42) + 8
aqs = [
    "1. La fête du Double Neuf est le…  A. 1er novembre  B. 18 octobre  C. 23 octobre",
    "2. Ce jour-là, on monte sur les montagnes et on regarde…  A. les feuilles  B. la lune  C. les chrysanthèmes",
    "3. La fête française pour les morts s'appelle…  A. la Toussaint  B. la rentrée  C. le Double Neuf",
    "4. Dans les deux pays, le chrysanthème est la fleur…  A. du printemps  B. de l'été  C. de l'automne et du souvenir",
]
for q in aqs:
    ay = p.para(x, ay, q, 22.5, "serif", False, INK, w, 1.42) + 4
print("P3 reading A ends", ay)

cx = COLX[2]
cy = y + 16
cy = p.shead(cx, cy + 30, "趣 味 角", CW) + 40
cy = p.para(cx, cy, "绕口令｜« Un chasseur sachant chasser doit savoir chasser sans son chien. » 一个会打猎的猎人,要学会不带猎狗打猎——练 s 音的好材料。", 22.5, "serif", False, INK, CW, 1.48) + 12
cy = p.para(cx, cy, "冷笑话｜— Pourquoi les plongeurs plongent-ils toujours en arrière ? — Parce que sinon, ils tombent dans le bateau ! (为什么潜水员总向后跳水?因为向前跳会掉进船里!)", 22.5, "serif", False, INK, CW, 1.48) + 12
cy = p.para(cx, cy, "谚语｜« Après la pluie, le beau temps. » 雨过天晴——和中文一个说法。本周谁的天气转晴了?", 22.5, "serif", False, INK, CW, 1.48)
print("P3 fun ends", cy)

# Row 2: B (col 0) | C (col 1) | 完形 (col 2)
ry = 866
bx = COLX[0]
by = p.shead(bx, ry + 30, "阅读 B · 人物", CW) + 42
by = p.para(bx, by, "« Hugo, l'homme des jardins »", 30, "serif", True, INK, CW, 1.2) + 8
by = p.para(bx, by, "Victor Hugo (1802–1885) est le plus grand écrivain français. Il a écrit « Les Misérables » et « Notre-Dame de Paris ». Mais Hugo aimait aussi les jardins. Pour lui, il n'y a pas de mauvaises herbes : il y a seulement de mauvais cultivateurs. Dans sa maison de Guernesey, il regardait la mer et il écrivait debout, chaque matin. Quand il est mort, deux millions de personnes ont suivi son cercueil dans les rues de Paris. Aujourd'hui encore, on lit Hugo dans le monde entier — et cette semaine, dans ce journal.", 23, "serif", False, INK, CW, 1.46) + 10
bqs = [
    "1. Hugo a vécu au…  A. XVIIe siècle  B. XIXe siècle  C. XXe siècle",
    "2. Il écrivait…  A. la nuit  B. debout, le matin  C. dans les cafés",
    "3. Sa maison de Guernesey regardait…  A. la mer  B. Paris  C. un jardin",
    "4. Pour Hugo, les « mauvaises herbes »…  A. existent  B. n'existent pas  C. sont rares",
    "5. Combien de personnes à ses funérailles ?  A. deux mille  B. deux cent mille  C. deux millions",
]
for q in bqs:
    by = p.para(bx, by, q, 21.5, "serif", False, INK, CW, 1.4) + 3
print("P3 reading B ends", by)

cx2 = COLX[1]
cy2 = p.shead(cx2, ry + 30, "阅读 C · 时事", CW) + 42
cy2 = p.para(cx2, cy2, "« La France pense déjà à 2027 »", 30, "serif", True, INK, CW, 1.2) + 8
cy2 = p.para(cx2, cy2, "Les Français voteront pour un nouveau président en 2027. Mais déjà, les sondages occupent la télévision et les journaux : cette semaine, « élection présidentielle 2027, sondages » est la recherche numéro un en France sur Google. Les candidats ne sont pas encore officiels, mais les débats ont commencé. Pour les jeunes Français, les grandes questions sont le climat, le travail et le prix de la vie. La campagne sera longue — et ce journal la suivra, une phrase à la fois.", 23, "serif", False, INK, CW, 1.46) + 10
cqs = [
    "Vrai ou faux ?  1. Les Français voteront en 2026.   2. Les sondages sont déjà à la télévision.   3. Tous les candidats sont officiels.",
    "词条｜voter 投票 · un sondage 民调 · un candidat 候选人 · le prix de la vie 生活成本 · une campagne 竞选运动",
]
for q in cqs:
    cy2 = p.para(cx2, cy2, q, 22, "serif", False, INK, CW, 1.45) + 3
print("P3 reading C ends", cy2)

kx = COLX[2]
ky = p.shead(kx, ry + 30, "完形填空", CW) + 42
ky = p.para(kx, ky, "« Le matin de la Toussaint »", 30, "serif", True, INK, CW, 1.2) + 8
ky = p.para(kx, ky, "Le 1er novembre, Madame Leroy se lève ___ (1). Elle prend un café, puis elle va au marché. Elle achète des ___ (2) blancs et jaunes. Ensuite, elle va au ___ (3) avec sa fille. Là, elles nettoient la tombe de la grand-mère et parlent d'elle. Le soir, Madame Leroy est fatiguée, mais elle est ___ (4) : les souvenirs sont une ___ (5) de vivre encore ensemble. Elle dit : « On n'oublie ___ (6) les gens qu'on aime. »", 23.5, "serif", False, INK, CW, 1.5) + 10
kopts = [
    "1. A. tard  B. tôt  C. vite",
    "2. A. chrysanthèmes  B. livres  C. poissons",
    "3. A. jardin  B. cimetière  C. marché",
    "4. A. heureuse  B. malade  C. en colère",
    "5. A. façon  B. saison  C. maison",
    "6. A. jamais  B. toujours  C. souvent",
]
for o in kopts:
    ky = p.para(kx, ky, o, 22, "serif", False, INK, CW, 1.4) + 3
print("P3 cloze ends", ky)

# 冷知识 strip (社交热议 moved to P5)
sy = 1880
p.hline(MX, RIGHT, sy - 16, INK, 1.6)
sy = p.shead(MX, sy + 28, "法 语 冷 知 识", RIGHT - MX) + 38
cold = [
    "« Chrysanthème »(菊花)来自希腊语:chrysos(金)+ anthemon(花)——金色的花。秋天开金花,正应景。",
    "《悲惨世界》有多长?初版近 1 900 页,是 19 世纪最长的小说之一。本周,你已读完它最有名的一句。",
]
for i, t in enumerate(cold):
    p.para(MX + i * 744, sy, t, 21.5, "serif", False, INK, 700, 1.42)
print("P3 cold strip ~ends", sy + 70)
p.foot(3)
p.save(f"{OUT}/b3-reading.svg")
print("P3 saved")

# ================= P4 · 练习版 =================
p = BSPage()
y = p.band("第 四 版", "练习专版", "EXERCISES · DO THE WORK")

mcq = [
    "1. Ce que tu dis ___ vrai.  A. est  B. es  C. sont",
    "2. Je pense, donc je ___.  A. suis  B. es  C. suit",
    "3. Petit poisson ___ grand.  A. devient  B. deviendra  C. devenait",
    "4. ___ et espérez !  A. Attendez  B. Attendre  C. Attendons",
    "5. Il ___ lire Hugo.  A. faut  B. falloir  C. faut de",
    "6. Je ne lis ___ des romans français.  A. pas  B. que  C. plus",
    "7. Elles ___ levées tôt hier.  A. ont  B. sont  C. se",
    "8. « Ne … que » veut dire…  A. seulement  B. jamais  C. toujours",
    "9. Elle ne boit ___ de l'eau.  A. pas  B. plus  C. que",
    "10. Longtemps, je me ___ couché tôt.  A. ai  B. suis  C. me",
    "11. Demain, nous ___ au jardin.  A. allons  B. irons  C. allions",
    "12. Le contraire de « tôt » est…  A. tard  B. vite  C. lentement",
    "13. Il n'y a ___ de mauvais cultivateurs.  A. que  B. pas  C. ni",
    "14. Vous ___ responsables de vos plantes.  A. êtes  B. sont  C. es",
    "15. Pour apprendre, il faut ___ chaque jour.  A. répéter  B. répètes  C. répété",
]
col_y = [y + 16, y + 16, y + 16]
col_head = ["单 选 题 · 一", "单 选 题 · 二", "单 选 题 · 三"]
for c in range(3):
    col_y[c] = p.shead(COLX[c], col_y[c] + 30, col_head[c], CW) + 40
for i, q in enumerate(mcq):
    c = i // 5
    col_y[c] = p.para(COLX[c], col_y[c], q, 22.5, "serif", False, INK, CW, 1.42) + 10
print("P4 mcq ends", col_y)

gy = max(col_y) + 10
p.hline(MX, RIGHT, gy - 12, LINE, 1)
x, w = span_x(0, 2)
gyh = p.shead(x, gy + 30, "完 成 句 子 · 用括号词完成", w) + 42
comp = [
    "1. Je ne mange ______ (que / pas) du pain le matin.",
    "2. Il ______ (falloir) imaginer Sisyphe heureux.",
    "3. Demain, elle ______ (devenir) grande.",
    "4. Nous nous ______ (se lever) tôt hier.",
    "5. Tu es ______ (responsable) de ce que tu apprivoises.",
    "6. ______ (attendre) et espérez !",
    "7. Petit à petit, l'oiseau ______ (faire) son nid.",
    "8. Elle ne boit que de ______ (le / l') eau.",
]
for i, s in enumerate(comp):
    xx = x + (i % 2) * (w // 2 + 16)
    ww = w // 2 - 16
    yy = gyh + (i // 2) * 74
    p.para(xx, yy, s, 22, "serif", False, INK, ww, 1.4)
gy = gyh + 4 * 74 + 6
gy3 = p.shead(COLX[2], gy - 4 * 74 - 6 + 30, "句 型 转 换", CW) + 42
trans = [
    "1. Je bois de l'eau. (改成「只喝水」)",
    "2. Il mange du pain. (改成否定句)",
    "3. Vous attendez. (改成祈使句)",
    "4. Elle deviendra grande. (改成过去时)",
]
for i, s in enumerate(trans):
    gy3 = p.para(COLX[2], gy3, s, 22, "serif", False, INK, CW, 1.4) + 10
print("P4 complete ends", gy, "transform ends", gy3)

ey = max(gy, gy3) + 8
p.hline(MX, RIGHT, ey - 12, LINE, 1)
x, w = span_x(0, 2)
eyh = p.shead(x, ey + 30, "短 文 改 错 · 每行一处", w) + 42
errs2 = [
    "1. Il faut à lire ce livre.  ______",
    "2. Je suis me couché de bonne heure.  ______",
    "3. Elle ne boit pas que de l'eau.  ______",
    "4. Nous deviendrons grands hier.  ______",
]
for i, s in enumerate(errs2):
    xx = x + (i % 2) * (w // 2 + 16)
    yy = eyh + (i // 2) * 74
    p.para(xx, yy, s, 22, "serif", False, INK, w // 2 - 16, 1.4)
ey = eyh + 2 * 74 + 6
ty = p.shead(COLX[2], ey - 2 * 74 - 6 + 30, "翻 译 · 汉译法", CW) + 42
p.para(COLX[2], ty, "见下方五句,先遮住第五版的参考译法,自己写一遍再对照。", 21, "serif", False, GREY, CW, 1.45)
print("P4 mid ends", ey)

ty2 = ey + 6
p.hline(MX, RIGHT, ty2 - 10, LINE, 1)
ty2 = p.shead(MX, ty2 + 30, "翻 译 题 · 五句", RIGHT - MX) + 42
trs = [
    "1. 我只喝水。", "2. 应该早点睡。", "3. 没有坏草,只有不会耕种的人。",
    "4. 秋天是冬天的春天。", "5. 她每天读一点法语。",
]
for i, s in enumerate(trs):
    xx = MX + (i % 3) * 492
    yy = ty2 + (i // 3) * 70
    p.para(xx, yy, s, 23, "serif", False, INK, 452, 1.4)
ty2 = ty2 + 2 * 70 + 6

wy = ty2
p.hline(MX, RIGHT, wy - 8, LINE, 1)
wy = p.shead(MX, wy + 28, "写 作 题", RIGHT - MX) + 38
wy = p.para(MX, wy, "题目:《 Mon automne 我的秋天 》。写 5–6 句法语:你的城市现在是什么季节?你读什么书?用上本周的 il faut 和 ne … que 各一次。范文与点评在第五版——先写,再看。", 23, "serif", False, INK, RIGHT - MX, 1.48) + 6
wy = p.para(MX, wy, "投稿:把作文发到评论区,小墨挑三篇在下期「读者园地」点评。写错不丢人——« Il n'y a que de mauvais cultivateurs »,没有坏学生,只有还没练够的句子。", 22, "serif", False, GREY, RIGHT - MX, 1.45)
print("P4 writing ends", wy)

# 挑战题 strip
chy = 1840
p.hline(MX, RIGHT, chy - 16, LINE, 1)
chy = p.shead(MX, chy + 28, "挑 战 题 · 加分项(答案在第五版)", RIGHT - MX) + 38
chal = [
    "1. « Après la pluie, ___ beau temps. »  A. le  B. la  C. un",
    "2. Le chrysanthème est la fleur de ___.  A. l'été  B. l'automne  C. l'hiver",
    "3. On fête la Toussaint le ___.  A. 18 octobre  B. 1er novembre  C. 23 octobre",
]
for i, s in enumerate(chal):
    p.para(MX + i * 492, chy, s, 21.5, "serif", False, INK, 452, 1.42)
chy = chy + 78
p.para(MX, chy, "朗读打卡｜把第三版完形短文读出声来,录下来发到评论区——开口,才是这周真正的最后一题。", 21.5, "serif", False, OLIVE, RIGHT - MX, 1.42)
print("P4 bottom ends", chy + 40)
p.foot(4)
p.save(f"{OUT}/b4-exercises.svg")
print("P4 saved")

# ================= P5 · 答案版 =================
p = BSPage()
y = p.band("第 五 版", "答案 · 范文 · 预告", "KEY · MODEL ESSAY · NEXT WEEK")

x, w3 = span_x(0, 2)
ay = p.shead(x, y + 30, "参 考 答 案 · 单选与完形", w3) + 40
keys1 = [
    "单选(第四版):1 A  2 A  3 B  4 A  5 A  6 B  7 B  8 A  9 C  10 B  11 B  12 A  13 A  14 A  15 A",
    "简析:第 5 题 il faut + 原形,无 de;第 6、9、13 题都是 ne … que「只有」;第 7、10 题自反动词用 être;第 11 题 aller 将来时词干 ir-。",
    "完形(第三版):1 B(tôt,呼应 No.006)  2 A(菊花)  3 B(墓地)  4 A(幸福)  5 A(façon 方式)  6 A(jamais 从不)",
    "阅读 A:1 B  2 C  3 A  4 C。阅读 B:1 B  2 B  3 A  4 B  5 C。",
    "阅读 C 判断:1 Faux(2027 年)  2 Vrai  3 Faux(候选人尚未官宣)。",
    "挑战题(第四版):1 A(谚语原文 le beau temps)  2 B(菊花属秋)  3 B(诸圣节 11 月 1 日)。",
]
for k in keys1:
    ay = p.para(x, ay, k, 22, "serif", False, INK, w3, 1.45) + 4
ay2 = p.shead(x, ay + 20, "答 案 · 完成句子 / 转换 / 改错 / 翻译", w3) + 38
keys2 = [
    "完成句子:1 que  2 faut  3 deviendra  4 sommes levés(女:levées)  5 responsable  6 Attendez  7 fait  8 l'",
    "句型转换:1 Je ne bois que de l'eau.  2 Il ne mange pas de pain.  3 Attendez !  4 Elle est devenue grande.",
    "改错:1 删 à → Il faut lire…  2 Je me suis couché…(me 提前,助动词 suis)  3 删 pas → Elle ne boit que de l'eau.  4 hier → demain,或改 est devenue",
    "翻译参考:1 Je ne bois que de l'eau.  2 Il faut se coucher de bonne heure.  3 Il n'y a pas de mauvaises herbes, il n'y a que de mauvais cultivateurs.  4 L'automne est le printemps de l'hiver.  5 Elle lit un peu de français chaque jour.",
]
for k in keys2:
    ay2 = p.para(x, ay2, k, 22, "serif", False, INK, w3, 1.45) + 4
print("P5 keys end", ay2)

cx = COLX[2]
cy = y + 16 + 30
cy = p.shead(cx, cy, "本 周 复 盘", CW) + 40
cy = p.para(cx, cy, "这一周你拿下了:ce que、donc、简单将来时、祈使句、il faut、复合过去时、ne … que——七个语法点,七位作家。卡住的地方,回到第二版再读一遍原句:语法在句子里,比在表格里记得牢。", 22, "serif", False, INK, CW, 1.48) + 12
cy = p.para(cx, cy, "自测:合上报纸,默写 No.007 的两句,再口头造一个 ne … que 的句子。能做到,本周毕业。", 22, "serif", False, OLIVE, CW, 1.48)
print("P5 recap ends", cy)

my = max(ay2, cy) + 14
p.hline(MX, RIGHT, my - 10, INK, 1.6)
x, w = span_x(0, 2)
myh = p.shead(x, my + 28, "写 作 范 文 · 《 Mon automne 》", w) + 40
my2 = p.para(x, myh, "« Mon automne est doux. Les feuilles tombent lentement dans ma ville. Le soir, je ne lis que des classiques français : Hugo, Camus, Saint-Exupéry. Il faut lire une page chaque jour, même une petite page. Petit lecteur deviendra grand lecteur. »", 24, "serif", False, INK, w, 1.5) + 6
my2 = p.para(x, my2, "点评｜五句里藏了四个本周点:ne … que、il faut、lentement(慢慢地)、deviendra 的词形变化。短,但句句是本周的句子——这才是范文的意义。", 22, "serif", False, GREY, w, 1.45)
my3 = myh
my3 = p.para(COLX[2], my3, "编者的话", 26, "serif", True, OLIVE, CW, 1.3) + 6
my3 = p.para(COLX[2], my3, "第一期做得慢,因为每一句都读了原文。慢,正是这份报纸的快。——小墨", 22, "serif", False, INK, CW, 1.48)
my = max(my2, my3) + 16
print("P5 model ends", my)

p.hline(MX, RIGHT, my - 8, LINE, 1)
x, w = span_x(0, 2)
by = p.shead(x, my + 28, "秋 日 书 单 · 从易到难(社交热议延伸)", w) + 40
books = [
    ("A2 《苏菲的烦恼》 Les Malheurs de Sophie", "19 世纪儿童文学,句子短、情节稠,适合第一本原著。"),
    ("B1 莫里哀《无病呻吟》Le médecin malgré lui", "对白体喜剧,口语感强,读出声来最好玩。"),
    ("进阶 《改变花的水》 Changer l'eau des fleurs", "当代畅销小说,守墓人的故事,语言现代,秋天读最配。"),
]
for t, d in books:
    by = p.para(x, by, t, 23, "serif", True, INK, w, 1.35) + 2
    by = p.para(x, by, d, 21.5, "serif", False, GREY, w, 1.42) + 8
print("P5 books end", by)

ny = my
ny = p.shead(COLX[2], ny + 28, "下 周 预 告 · VOL.2", CW) + 40
ny = p.para(COLX[2], ny, "主题「深秋与节日」:诸圣节 la Toussaint 专题阅读、万圣夜的前世今生、法语里的「死亡」委婉说法;每日一句继续文学:波德莱尔的秋、里尔克的《秋日》法译。不见不散。", 22.5, "serif", False, INK, CW, 1.48) + 12
ny = p.para(COLX[2], ny, "读者互动｜今日打卡:在评论区写下你的《Mon automne》第一句。点赞最高的一句,登下期头版。", 22.5, "serif", False, OLIVE, CW, 1.48)
print("P5 next ends", ny)

fy = max(by, ny) + 16

# 社交热议 (moved from P3)
p.hline(MX, RIGHT, fy - 8, LINE, 1)
hy5 = p.shead(MX, fy + 28, "本 周 社 交 热 议 · TRENDING", RIGHT - MX) + 38
hot = [
    ("拟人化短剧走红", "博主 @bonjour.mate(61 万粉)把「你心里的法语」演成一个被冷落的角色:当年天天背单词,到了巴黎面包房却只说得出 Bonjour。评论区全是「这就是我」。"),
    ("「能读法语原著」成氛围感顶流", "Ins 上一条帖子火了:烛光下翻杜拉斯《情人》原著,配文「能读法语,有点时髦」。读书的仪式感,正成为语言学习的新动力——本报也只读原著。"),
    ("法语分级书单刷屏", "从 A2 的《苏菲的烦恼》到 B1 的莫里哀,法语老师们这周都在晒书单。左边「秋日书单」就是给你的三本台阶。"),
]
for i, (h, b) in enumerate(hot):
    xx = MX + i * 492
    yy = p.para(xx, hy5, h, 24, "serif", True, OLIVE, 452, 1.3) + 4
    p.para(xx, yy, b, 21.5, "serif", False, INK, 452, 1.45)
fy = hy5 + 186
print("P5 hot ends", fy)

p.rect(MX, fy, RIGHT - MX, 86, fill=DARK)
p.text(780, fy + 54, "读 真 书 , 读 原 文 · LUCERNA — READ BOOKS IN ANY LANGUAGE", 25, "sans", True, "#f3edda", anchor="middle")
print("P5 bottom ends", fy + 86)
p.foot(5)
p.save(f"{OUT}/b5-key.svg")
print("P5 saved")
