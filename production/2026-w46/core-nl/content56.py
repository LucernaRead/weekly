# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-nl-core/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JONGEREN (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JONGEREN · 青年", "De Lucerna", "NIVEAU B1 · Robinson, de schoen en het verlanglijstje · 荒岛节目、鞋子与愿望单")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Robinson op zondag — en de schoen staat klaar", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: B1")
f.para("Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4. Negentien bekende Nederlanders en Vlamingen leven 34 dagen op een onbewoond eiland in Maleisië. Nicolette Kluijver en Edson da Graça presenteren het programma, Camille Vanuxem is de verslaggever.")
f.para("De kandidaten slapen buiten en moeten alles zelf doen: vuur maken, eten zoeken, proeven winnen. Wie een proef verliest, kan naar huis worden gestemd. Wie het langst blijft, wint de expeditie. Het seizoen begon op zondag 1 november — en elke week wordt het spel harder.")
f.para("Deze week is zondag 15 november een drukke dag: overdag de intocht in Amsterdam, 's avonds een nieuwe aflevering van Robinson. En na de intocht mag de schoen. Ook jongeren zetten hun schoen — met een verlanglijstje erin, in plaats van alleen een tekening.")
f.para("Een verlanglijstje schrijven is ook Nederlands oefenen: schrijf in het Nederlands wat je wilt, waarom je het wilt en voor wie je het nog meer opschrijft. Sinterklaas leest Nederlands, zeggen kinderen — en de redactie ook.")
f.head("JONGEREN EN DE SCHOEN", 25)
f.para("De schoen zetten is niet alleen voor kleine kinderen. Jongeren zetten hun schoen met een wortel voor het paard, een tekening — of een verlanglijstje met drie wensen. Klein of groot, een wens op papier is het begin van Sinterklaas.")
f.box("ZO KIJK JE ROBINSON", [
    ("1. Kijk zondag om 20:00 uur op RTL 4（周日晚 20:00 在 RTL 4 收看）", "serif", False, INK, 21, 1.36),
    ("2. Let op de proeven: daar worden de punten verdeeld（注意比赛项目：分数在那里决出）", "serif", False, INK, 21, 1.36),
    ("3. Raad met vrienden wie het langst blijft（和朋友猜谁能留到最后）", "serif", False, INK, 21, 1.36),
    ("4. Zet daarna je schoen: met een verlanglijstje erin（然后放好鞋子：里面放一张愿望单）", "serif", False, INK, 21, 1.36),
])
f.gloss("het verlanglijstje 愿望单 · de verslaggever 记者、报道员 · de proef 比赛项目、考验 · stemmen 投票 · de aflevering （一）集。")
f.end_report()

# col 3: facts + en jij (sequential, measured; no photo this page)
ix = COLX[3]
facts = ["Expeditie Robinson: 19 kandidaten; elke zondag 20:00 uur, RTL 4.",
         "34 dagen op een onbewoond eiland in Maleisië; presentatie: Nicolette Kluijver en Edson da Graça.",
         "Na de intocht (15 november) mag de schoen, met een wortel en een verlanglijstje."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 64
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "JONGEREN IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Kijk jij zondag naar Expeditie Robinson, of zet je liever je schoen met een verlanglijstje? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("周日你看《荒岛远征》，还是更爱放鞋子加愿望单？写两句荷兰语寄来。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ? · 说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "周日你看《荒岛远征》，还是更爱放鞋子加愿望单？写两句荷兰语寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "OEFENINGEN · 第 5 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · BEGRIJPEN", 25)
e.bridge("读第 5 版文章，选出正确答案。")
e.ex("B1", "单选", "B", "Robinson 每周日 20:00 在 RTL 4 播出",
     "Expeditie Robinson is elke zondag om... A. 18:00 uur · B. 20:00 uur · C. 12:00 uur", size=20, gap=8)
e.ex("B1", "单选", "A", "19 位参赛者",
     "Expeditie Robinson heeft ___ kandidaten. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "单选", "C", "节目在马来西亚的荒岛上拍摄",
     "De kandidaten leven op een eiland in... A. Spanje · B. Grave · C. Maleisië", size=20, gap=8)
e.ex("B1", "单选", "B", "参赛者在岛上待 34 天",
     "De kandidaten blijven ___ dagen op het eiland. A. 19 · B. 34 · C. 88", size=20, gap=8)
e.ex("B1", "单选", "A", "鞋子里放愿望单",
     "Jongeren zetten hun schoen met... A. een verlanglijstje · B. een boek · C. een lampion", size=20, gap=8)
e.head("B · WOORDEN UIT DE TEKST", 25)
e.bridge("用方框里的词填空。")
e.para("verlanglijstje · verslaggever · proef · stemmen · aflevering · kandidaat", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "verlanglijstje", "verlanglijstje = 愿望单（het）",
     "In mijn schoen zit een ___ met drie wensen.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "verslaggever", "verslaggever = 记者（de）",
     "Camille Vanuxem is de ___ van het programma.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "proef", "proef = 比赛项目、考验（de）",
     "Wie een ___ verliest, kan naar huis gaan.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "stemmen", "stemmen = 投票",
     "De kandidaten ___ wie naar huis moet.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "aflevering", "aflevering = （一）集",
     "Zondag is er een nieuwe ___ van Robinson.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "kandidaten", "kandidaat 复数：kandidaten",
     "Er zijn 19 ___ op het eiland.", instr="填空", size=20, gap=8)
e.head("C · DE TOEKOMST MET GAAN", 25)
e.bridge("用 gaan + 不定式说将来。")
e.ex("B1", "完成句子", "gaat winnen", "gaat winnen = 会赢（只是猜测）",
     "Wie ___ (winnen) Expeditie Robinson, denk je?", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaan kijken", "wij → gaan + 不定式 kijken",
     "Wij ___ (kijken) zondag naar de nieuwe aflevering.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaat zetten", "hij → gaat zetten",
     "Hij ___ (zetten) zondagavond zijn schoen.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaan schrijven", "zij (复数) → gaan schrijven",
     "De kinderen ___ (schrijven) een verlanglijstje.", instr="填空", size=20, gap=8)
e.head("D · WAAR OF NIET WAAR?", 25)
e.ex("B1", "判断对错", "Waar", "对：节目 11 月 1 日开始",
     "Expeditie Robinson begon op 1 november. Waar of niet waar?", instr="判断", size=20, gap=8)
e.ex("B1", "判断对错", "Niet waar", "错：节目在马来西亚拍摄",
     "Expeditie Robinson speelt in Spanje. Waar of niet waar?", instr="判断", size=20, gap=8)
e.ex("B2", "判断对错", "Niet waar", "错：鞋子里放胡萝卜是给马的",
     "De wortel in de schoen is voor Sinterklaas. Waar of niet waar?", instr="判断", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jongeren.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · VERDIEPING (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERDIEPING · 深读", "De Lucerna", "NIVEAU B2 · Sint-Maarten of Halloween? · 圣马丁节还是万圣节？")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P6-main")
f.title("Sint-Maarten of Halloween: moet je kiezen?", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: B2")
f.para("Sint-Maarten is een oude traditie in Nederland. Kinderen lopen al meer dan honderd jaar met lampionnen langs de deuren. Halloween is nieuwer in Nederland — en het groeit: volgens onderzoeksbureau Motivaction vierde in 2025 26 procent van de Nederlanders Halloween, tegenover 21 procent een jaar eerder.")
f.para("Maar let op de cijfers: de onderzoeken gebruiken verschillende definities en zijn daarom niet rechtstreeks vergelijkbaar. En een lege stoep betekent niet automatisch dat Sint-Maarten verdwijnt. In sommige plaatsen verplaatst de viering zich naar winkelcentra en georganiseerde optochten, waar kinderen samen langs deelnemende winkels lopen.")
f.para("Deskundigen zien Sint-Maarten niet verdwijnen. Antropoloog Irene Stengs van het Meertens Instituut zei in 2025 dat de belangstelling voor Sint-Maarten is toegenomen. Traditiedeskundige Ineke Strouken ziet geen duidelijke landelijke achteruitgang. Het feest verandert, zeggen zij — het verdwijnt niet.")
f.para("De twee feesten zijn ook anders. Halloween draait om griezelen en verkleden; Sint-Maarten draait om delen en aandacht voor anderen. Veel kinderen doen allebei: griezelen op 31 oktober, zingen op 11 november. Kiezen hoeft niet — het zijn twee feesten, in twee weken, met twee soorten licht.")
f.para("Een traditie leeft als mensen haar blijven vieren. Op straat, in het winkelcentrum of allebei: de lampion gaat aan als het donker wordt, en het liedje klinkt bij elke deur.")
f.head("VOOR OF TEGEN KIEZEN?", 25)
f.para("Voorstanders van kiezen zeggen: één feest is genoeg, anders wordt november één lange verkleedweek. Tegenstanders zeggen: feesten groeien naast elkaar, zoals talen naast elkaar groeien. De krant kiest niet: vier wat je viert — maar zing op 11 november in ieder geval één liedje.")
f.gloss("de traditie 传统 · griezelen 吓人 · de belangstelling 兴趣· de achteruitgang 衰退 · de deskundige 专家。")
f.end_report()

# col 3: OEFENDATA chart + pro/contra box (sequential, measured)
ix = COLX[3]
rows = [
    ("Ik loop met een lampion", "40", 160),
    ("Ik vier Halloween", "25", 100),
    ("Ik doe allebei", "20", 80),
    ("Ik blijf thuis", "15", 60),
]
cap = "OEFENDATA — verzonnen cijfers om mee te oefenen, geen echte enquête. Vraag: wat doe jij rond 11 november? (100 jongeren)"
capcn = "练习数据：虚构数字，仅供练习，非真实调查。问题：11 月 11 日前后你会做什么？（100 名年轻人）"
ch = 62 + len(rows) * 58 + 14 + len(wrap(cap, "serif", False, 19, CW - 44)) * 27 + 6 + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
p.rect(ix, 200, CW, ch, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DE GRAFIEK · 图表（练习数据）", 24, "sans", True, OLIVE)
yy3 += 58
for lab, val, bw in rows:
    p.text(ix + 22, yy3 + 20, lab, 19.5, "serif", True, INK)
    p.text(ix + CW - 22, yy3 + 20, val, 19.5, "sans", True, BRICK, anchor="end")
    p.rect(ix + 22, yy3 + 30, bw, 18, fill=OLIVE)
    yy3 += 58
yy3 += 14
yy3 = p.para(ix + 22, yy3 + 19, cap, 19, "serif", False, GREY, CW - 44, 1.36)
yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, CW - 44, 1.32) + 6
print("P6 chart ends", 200 + ch, "content to", yy3)
by6 = 200 + ch + 26
bt = [
    ("Voor kiezen: één feest is genoeg in november.", "serif", False, INK, 21, 1.4),
    ("Tegen kiezen: feesten groeien naast elkaar, zoals talen.", "serif", False, INK, 21, 1.4),
    ("De krant kiest niet: vier wat je viert. En zing op 11 november één liedje. En jij?", "serif", False, INK, 21, 1.4),
]
bh = 62 + sum(len(wrap(t, "serif", False, 21, CW - 44)) * 29.5 + 8 for t, *_ in bt) + 16 + 30
p.rect(ix, by6, CW, bh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = by6 + 16
p.text(ix + 22, yy3 + 26, "VOOR OF TEGEN? · 正方还是反方", 21, "sans", True, OLIVE)
yy3 += 52
for t, k, b, fl, s, lh in bt:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.4) + 8
print("P6 col3 ends", by6 + bh)

# ---- P6 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "OEFENINGEN · 第 6 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LEES DE GRAFIEK", 25)
e.bridge("看第 6 版图表（练习数据）回答。")
e.ex("B2", "完成句子", "40", "40 名年轻人提灯笼",
     "___ van de 100 jongeren lopen met een lampion.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "25", "25 人过万圣节",
     "___ jongeren vieren Halloween.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "60", "40 + 20 = 60",
     "Lampion lopen en allebei samen: ___ jongeren.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "15", "15 人待在家里",
     "___ jongeren blijven thuis.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "100", "图表共 100 人：40+25+20+15",
     "De grafiek telt in totaal ___ jongeren.", instr="填空", size=21.5, gap=9)
e.head("B · BEGRIJPEN", 25)
e.bridge("读第 6 版文章，选出正确答案。")
e.ex("B2", "单选", "B", "2025 年 26% 的荷兰人过万圣节",
     "Volgens Motivaction vierde in 2025 ___ procent Halloween. A. 21 · B. 26 · C. 11", size=21.5, gap=9)
e.ex("B2", "单选", "B", "两项调查定义不同，不能直接比较",
     "De onderzoeken zijn... A. precies hetzelfde · B. niet rechtstreeks vergelijkbaar · C. allebei fout", size=21.5, gap=9)
e.ex("B2", "单选", "C", "圣马丁节的关注度增加了（Stengs，2025）",
     "Irene Stengs zei in 2025 dat de belangstelling voor Sint-Maarten... A. verdween · B. gelijk bleef · C. is toegenomen", size=21.5, gap=9)
e.ex("B2", "单选", "A", "万圣节重扮鬼，圣马丁节重分享",
     "Halloween draait om griezelen; Sint-Maarten draait om... A. delen · B. voetbal · C. boeken", size=21.5, gap=9)
e.ex("B2", "单选", "B", "传统靠人们继续庆祝而活着",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=21.5, gap=9)
e.head("C · WOORDEN", 25)
e.bridge("用方框里的词填空。")
e.para("traditie · griezelen · belangstelling · achteruitgang", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B2", "完成句子", "traditie", "traditie = 传统（de）",
     "Sint-Maarten is een oude ___.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "griezelen", "griezelen = 扮鬼吓人",
     "Met Halloween gaan kinderen ___ en zich verkleden.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "belangstelling", "belangstelling = 关注（de）",
     "De ___ voor Sint-Maarten is toegenomen.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "achteruitgang", "achteruitgang = 衰退（de）",
     "Strouken ziet geen duidelijke landelijke ___.", instr="填空", size=21.5, gap=9)
e.head("D · MAAK DE ZINNEN", 25)
e.bridge("把词组成正确的句子。")
e.ex("B2", "造句", "Sint-Maarten is een oude traditie in Nederland.", "主语 + 动词 + 表语 + 地点",
     "sint-maarten / is / een oude traditie / in nederland → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "De kinderen lopen met lampionnen langs de deuren.", "主语 + 动词 + 方式 + 地点",
     "de kinderen / lopen / met lampionnen / langs de deuren → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "Een traditie leeft als mensen haar blijven vieren.", "als 从句在句末",
     "een traditie / leeft / als mensen haar blijven vieren → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "Kiezen hoeft niet: het zijn twee feesten.", "kiezen + hoeft niet + 解释",
     "kiezen / hoeft niet / het zijn twee feesten → ___", instr="造句", size=21.5, gap=9)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-verdieping.svg")
print("P6 saved, exercises so far:", len(REG))
