# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JONGEREN (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JONGEREN　青年", "De Lucerna", "NIVEAU B1　Robinson, de surprise en het gedicht　荒岛节目、伪装礼物与小诗")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Robinson op zondag — en de surprises", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4. Negentien bekende Nederlanders en Vlamingen leven 34 dagen op een onbewoond eiland in Maleisië. Nicolette Kluijver en Edson da Graça presenteren het programma, Camille Vanuxem is de verslaggever.")
f.para("De kandidaten slapen buiten en moeten alles zelf doen: vuur maken, eten zoeken, proeven winnen. Wie een proef verliest, kan naar huis worden gestemd. Wie het langst blijft, wint de expeditie. Het seizoen begon op zondag 1 november — en elke week wordt het spel harder. Zondag 22 november is er een nieuwe aflevering.")
f.para("Zondagavond is ook de avond van de surprises: over dertien dagen is het pakjesavond, op zaterdag 5 december. Jongeren maken een surprise voor een vriend of vriendin: een cadeau in een gekke verpakking, met een gedicht erbij. Een surprise maken is ook Nederlands oefenen: schrijf het gedicht in het Nederlands.")
f.para("Een gedicht hoeft niet lang te zijn: vier regels zijn genoeg. Vertel in het gedicht wie het cadeau krijgt, waarom juist die persoon, en wat erin zit — maar verklap de surprise niet te snel. Sinterklaas leest Nederlands, zeggen kinderen — en de redactie ook.")
f.head("JONGEREN EN DE SURPRISE", 25)
f.para("Een surprise is niet alleen voor kleine kinderen. Jongeren maken surprises met een wortel voor het paard, een tekening — of een gedicht van vier regels. Klein of groot, een gedicht op papier is het begin van pakjesavond.")
f.box("ZO KIJK JE ROBINSON", [
    ("1. Kijk zondag om 20:00 uur op RTL 4（周日晚 20:00 在 RTL 4 收看）", "serif", False, INK, 21, 1.36),
    ("2. Let op de proeven: daar worden de punten verdeeld（注意比赛项目：分数在那里决出）", "serif", False, INK, 21, 1.36),
    ("3. Raad met vrienden wie het langst blijft（和朋友猜谁能留到最后）", "serif", False, INK, 21, 1.36),
    ("4. Schrijf daarna een gedicht voor je surprise（然后为你的伪装礼物写首诗）", "serif", False, INK, 21, 1.36),
])
f.gloss("de surprise 伪装礼物 · het gedicht 诗 · de verslaggever 记者、报道员 · de proef 比赛项目、考验 · de aflevering （一）集。")
f.end_report()

# col 3: facts + en jij + photo (sequential, measured)
ix = COLX[3]
facts = ["Expeditie Robinson: 19 kandidaten; elke zondag 20:00 uur, RTL 4.",
         "34 dagen op een onbewoond eiland in Maleisië; presentatie: Nicolette Kluijver en Edson da Graça.",
         "Pakjesavond is op zaterdag 5 december — nog 13 dagen vanaf zondag 22 november."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 64
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "JONGEREN IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Kijk jij zondag naar Expeditie Robinson, of maak je liever een surprise met een gedicht? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("周日你看《荒岛远征》，还是更爱做伪装礼物加小诗？写两句荷兰语寄来。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ?　说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "周日你看《荒岛远征》，还是更爱做伪装礼物加小诗？写两句荷兰语寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 boxes end", ey3 + eh)
iy5 = ey3 + eh + 26
image(p, "strand.jpg", ix, iy5, CW, 250)
cy5 = caption(p, ix, iy5 + 250, CW, "Een tropische baai met palmen — net als het eiland in Maleisië waar Expeditie Robinson wordt opgenomen.",
              "Foto: Elise Iovenko / Unsplash — CC0")
print("P5 col3 ends", cy5)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　第5版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("读第 5 版文章，选出正确答案。")
e.ex("B1", "单选", "B", "Robinson 每周日 20:00 在 RTL 4 播出",
     "Expeditie Robinson is elke zondag om... A. 18:00 uur · B. 20:00 uur · C. 12:00 uur", size=20, gap=8)
e.ex("B1", "单选", "A", "19 位参赛者",
     "Expeditie Robinson heeft ___ kandidaten. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "单选", "C", "节目在马来西亚的荒岛上拍摄",
     "De kandidaten leven op een eiland in... A. Spanje · B. Grave · C. Maleisië", size=20, gap=8)
e.ex("B1", "单选", "B", "参赛者在岛上待 34 天",
     "De kandidaten blijven ___ dagen op het eiland. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "单选", "A", "surprise 里有诗",
     "Bij een surprise hoort... A. een gedicht · B. een boek · C. een lampion", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("用方框里的词填空。")
e.para("surprise · gedicht · verslaggever · proef · aflevering · kandidaat", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "surprise", "surprise = 伪装礼物（de）",
     "Ik maak een ___ voor mijn vriendin.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "verslaggever", "verslaggever = 记者（de）",
     "Camille Vanuxem is de ___ van het programma.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "proef", "proef = 比赛项目、考验（de）",
     "Wie een ___ verliest, kan naar huis gaan.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gedicht", "gedicht = 诗（het）",
     "In vier regels schrijf ik een ___.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "aflevering", "aflevering = （一）集",
     "Zondag is er een nieuwe ___ van Robinson.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "kandidaten", "kandidaat 复数：kandidaten",
     "Er zijn 19 ___ op het eiland.", instr="填空", size=20, gap=8)
e.head("C　DE TOEKOMST MET GAAN", 25)
e.bridge("用 gaan + 不定式说将来。")
e.ex("B1", "完成句子", "gaat winnen", "gaat winnen = 会赢（只是猜测）",
     "Wie ___ (winnen) Expeditie Robinson, denk je?", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaan kijken", "wij → gaan + 不定式 kijken",
     "Wij ___ (kijken) zondag naar de nieuwe aflevering.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaat maken", "zij → gaat maken",
     "Zij ___ (maken) zondag een surprise voor pakjesavond.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaan schrijven", "zij (复数) → gaan schrijven",
     "De kinderen ___ (schrijven) een gedicht van vier regels.", instr="填空", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "判断对错", "Waar", "对：节目 11 月 1 日开始",
     "Expeditie Robinson begon op 1 november. Waar of niet waar?", instr="判断", size=20, gap=8)
e.ex("B1", "判断对错", "Niet waar", "错：节目在马来西亚拍摄",
     "Expeditie Robinson speelt in Spanje. Waar of niet waar?", instr="判断", size=20, gap=8)
e.ex("B2", "判断对错", "Niet waar", "错：四行诗就够了",
     "Een gedicht voor een surprise moet minstens twintig regels hebben. Waar of niet waar?", instr="判断", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jongeren.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · VERDIEPING (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERDIEPING　深读", "De Lucerna", "NIVEAU B2　Sinterklaas: oud feest, nieuwe wensen　圣诞老人节：古老的节日，新的愿望")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P6-main")
f.title("Sinterklaas: oud feest, nieuwe wensen", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B2")
f.para("Sinterklaas is een oud feest in Nederland. Kinderen zetten al meer dan honderd jaar hun schoen bij de deur. Maar het feest verandert: vroeger zat er een tekening in de schoen, nu steeds vaker een verlanglijstje — soms op papier, soms op een telefoon.")
f.para("Ook pakjesavond verandert. Vroeger kreeg je een cadeau in een doos; nu maken veel families een surprise: het cadeau zit verstopt in iets geks, met een gedicht erbij. Het gedicht is vaak het leukste van de avond — grappig, lief of een beetje plagend.")
f.para("Deskundigen zien het feest niet verdwijnen. Het Sinterklaasjournaal is elke dag om 18:00 uur op televisie en de landelijke intocht in Grave was live op NPO 3 te zien. Het feest verandert, zeggen zij — het verdwijnt niet.")
f.para("De twee weken rond Sinterklaas zijn ook anders dan vroeger. Sint-Maarten was vorige week woensdag: kinderen liepen met lampionnen langs de deuren. Nu staat de schoen klaar. Twee feesten van licht en geven, in twee weken — met twee soorten wensen: een wortel voor het paard, een lijstje voor de Sint.")
f.para("Een traditie leeft als mensen haar blijven vieren. Op straat, in de huiskamer of allebei: de schoen staat klaar als het donker wordt, en het gedicht klinkt op pakjesavond bij elk cadeau.")
f.head("VOOR OF TEGEN EEN LIJSTJE?", 25)
f.para("Voorstanders van het lijstje zeggen: zo krijgt iedereen wat hij echt wil. Tegenstanders zeggen: een verrassing is leuker dan een lijstje. De krant kiest niet: schrijf wat je wilt — maar schrijf het in het Nederlands.")
f.gloss("het verlanglijstje 愿望单 · de surprise 伪装礼物 · het gedicht 诗 · veranderen 改变 · de traditie 传统。")
f.end_report()

# col 3: OEFENDATA chart + pro/contra box (sequential, measured)
ix = COLX[3]
rows = [
    ("Een wortel en een tekening", "35", 140),
    ("Een verlanglijstje", "30", 120),
    ("Een gedicht", "20", 80),
    ("Nog niets", "15", 60),
]
cap = "OEFENDATA — verzonnen cijfers om mee te oefenen, geen echte enquête. Vraag: wat zet jij in je schoen? (100 jongeren)"
capcn = "练习数据：虚构数字，仅供练习，非真实调查。问题：你在鞋里放什么？（100 名年轻人）"
# fix4 D8: capcn wrap width CW-25 (397.5). Width scan (sans 18.5):
# 378.5 (CW-44) wraps 。 onto line 2 start; band 388.5-406.5 wraps to the
# same 2 lines with 。 at end of line 1; 397.5 is the band middle (9px from
# each edge). Narrowing (fix3-style) cannot keep 2 lines here — every width
# that clears the orphan forces 3 lines (+26px box growth, downstream shift);
# widening keeps 2 lines, box height unchanged, zero y shift. Line 1 ends at
# ix+22+388.5 = 1850.0, 12px inside the box right edge (1862.0).
capcn_w = CW - 25
ch = 62 + len(rows) * 58 + 14 + len(wrap(cap, "serif", False, 19, CW - 44)) * 27 + 6 + len(wrap(capcn, "sans", False, 18.5, capcn_w)) * 26 + 18
p.rect(ix, 200, CW, ch, fill=BOX)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DE GRAFIEK　图表（练习数据）", 24, "sans", True, OLIVE)
yy3 += 58
for lab, val, bw in rows:
    p.text(ix + 22, yy3 + 20, lab, 19.5, "serif", True, INK)
    p.text(ix + CW - 22, yy3 + 20, val, 19.5, "sans", True, OLIVE, anchor="end")
    p.rect(ix + 22, yy3 + 30, bw, 18, fill=OLIVE)
    yy3 += 58
yy3 += 14
yy3 = p.para(ix + 22, yy3 + 19, cap, 19, "serif", False, GREY, CW - 44, 1.36)
yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, capcn_w, 1.32) + 6  # fix4 D8: capcn_w, see above
print("P6 chart ends", 200 + ch, "content to", yy3)
by6 = 200 + ch + 26
bt = [
    ("Voor een lijstje: zo krijgt iedereen wat hij echt wil.", "serif", False, INK, 21, 1.4),
    ("Tegen een lijstje: een verrassing is leuker dan een lijstje.", "serif", False, INK, 21, 1.4),
    ("De krant kiest niet: schrijf wat je wilt. En jij?", "serif", False, INK, 21, 1.4),
]
bh = 62 + sum(len(wrap(t, "serif", False, 21, CW - 44)) * 29.5 + 8 for t, *_ in bt) + 16 + 30
p.rect(ix, by6, CW, bh, fill="#f0eee5")
yy3 = by6 + 16
p.text(ix + 22, yy3 + 26, "VOOR OF TEGEN?　正方还是反方", 21, "sans", True, OLIVE)
yy3 += 52
for t, k, b, fl, s, lh in bt:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.4) + 8
print("P6 col3 ends", by6 + bh)

# ---- P6 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　第6版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEES DE GRAFIEK", 25)
e.bridge("看第 6 版图表（练习数据）回答。")
e.ex("B2", "完成句子", "35", "35 名年轻人放胡萝卜和图画",
     "___ van de 100 jongeren zetten een wortel en een tekening in hun schoen.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "30", "30 人放愿望单",
     "___ jongeren zetten een verlanglijstje in hun schoen.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "65", "35 + 30 = 65",
     "Wortel en verlanglijstje samen: ___ jongeren.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "15", "15 人什么都没放",
     "___ jongeren zetten nog niets in hun schoen.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "100", "图表共 100 人：35+30+20+15",
     "De grafiek telt in totaal ___ jongeren.", instr="填空", size=21.5, gap=9)
e.head("B　BEGRIJPEN", 25)
e.bridge("读第 6 版文章，选出正确答案。")
e.ex("B2", "单选", "B", "以前鞋里放图画，现在常放愿望单",
     "Vroeger zat er een tekening in de schoen; nu steeds vaker... A. een lampion · B. een verlanglijstje · C. een boek", size=21.5, gap=9)
e.ex("B2", "单选", "B", "surprise 是藏在古怪包装里的礼物",
     "Een surprise is een cadeau... A. in een doos van de winkel · B. verstopt in iets geks · C. zonder gedicht", size=21.5, gap=9)
e.ex("B2", "单选", "C", "圣诞老人新闻每天 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 12:00 uur · B. 20:00 uur · C. 18:00 uur", size=21.5, gap=9)
e.ex("B2", "单选", "A", "传统靠人们继续庆祝而活着",
     "Een traditie leeft als... A. mensen haar blijven vieren · B. ze oud is · C. ze op televisie is", size=21.5, gap=9)
e.ex("B2", "单选", "B", "圣马丁节在上周三",
     "Sint-Maarten was... A. gisteren · B. vorige week woensdag · C. volgende week", size=21.5, gap=9)
e.head("C　WOORDEN", 25)
e.bridge("用方框里的词填空。")
e.para("verlanglijstje · surprise · gedicht · veranderen", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B2", "完成句子", "verlanglijstje", "verlanglijstje = 愿望单（het）",
     "Op het ___ staan drie wensen.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "surprise", "surprise = 伪装礼物（de）",
     "Het cadeau zit verstopt in een ___.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "gedicht", "gedicht = 诗（het）",
     "Bij het cadeau hoort een ___ van vier regels.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "verandert", "veranderen → verandert（单数）",
     "Het feest ___ elk jaar een beetje.", instr="填空", size=21.5, gap=9)
e.head("D　MAAK DE ZINNEN", 25)
e.bridge("把词组成正确的句子。")
e.ex("B2", "造句", "Sinterklaas is een oud feest in Nederland.", "主语 + 动词 + 表语 + 地点",
     "sinterklaas / is / een oud feest / in nederland → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "De kinderen zetten hun schoen bij de deur.", "主语 + 动词 + 宾语 + 地点",
     "de kinderen / zetten / hun schoen / bij de deur → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "Een traditie leeft als mensen haar blijven vieren.", "als 从句在句末",
     "een traditie / leeft / als mensen haar blijven vieren → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "Het feest verandert, maar het verdwijnt niet.", "veranderen + maar + 否定",
     "het feest / verandert / maar het verdwijnt niet → ___", instr="造句", size=21.5, gap=9)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-verdieping.svg")
print("P6 saved, exercises so far:", len(REG))
