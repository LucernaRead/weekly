# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-cn-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Taalfocus", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Drie niveaus, drie onderwerpen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与包裹 · Winkelen", 24)
a.para("Winkelwoorden deze week: 高潮场 (gāocháochǎng, de piekverkoopperiode), 包裹 (bāoguǒ, een pakket), 取件码 (qǔjiànmǎ, een ophaalcode), 快递柜 (kuàidìguì, een pakketkluisje). Veiligheidswoorden: 消防 (xiāofáng, brandpreventie), 疏散 (shūsàn, evacueren), 自救 (zìjiù, zelfredding).", 21.5)
a.glossline("Telwoorden blijven belangrijk: 一个包裹 (een pakket), 一部电影 (een film), 一场演练 (een oefening).")
a.ex("A2", "完成句子", "个", "包裹 neemt het telwoord 个 gè.",
     "我拿了___包裹。", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "单选", "A", "高潮场 betekent de piekverkoopperiode.",
     "「高潮场」是什么意思? A. 最忙的卖货时间 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "消防", "xiāofáng — brandpreventie, 9 nov.",
     "11月9日是全国___日。", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "单选", "A", "Pakketten nemen 个 — niet 只 of 条.",
     "哪个说法对? A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20.5, gap=10)
a.para("Nog één om te oefenen: 「我的包裹到了吗?」 (Is mijn pakket aangekomen?) Als je op een pakket wacht, vraag het eerst en ga dan naar het kluisje.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Tijd & data", 24)
b.para("Het Chinees geeft tijden groot → klein: jaar, maand, dag, weekdag, dagdeel, uur. Voorbeelden uit dit nummer: 「11月9日星期一」 (ma 9 nov.), 「11月10日星期二20点」 (di 10 nov., 20:00), 「11月15日星期日凌晨3点」 (zo 15 nov., 3 uur 's nachts). De grootste eenheid eerst, niets door elkaar.", 21.5)
b.glossline("Zo wordt het Engelse «Monday, Nov 9» 11月9日星期一.")
b.ex("B1", "单选", "B", "凌晨 língchén — de kleine uurtjes na middernacht.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "06:00 is 早上 — niet 's avonds.",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Volgorde groot → klein: 15 nov., zondag, 03:00.",
     "哪个顺序对? A. 11月15日星期日凌晨3点 · B. 凌晨3点星期日11月15日 · C. 星期日凌晨3点11月15日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周一", "9 november is een maandag — 周一.",
     "11月9日是星期一,也可以说___。消防日在这天。", instr="Vul in", size=20.5, gap=10)
b.para("Nog twee woorden: 凌晨 (língchén) zijn de kleine uurtjes na middernacht, vóór de dageraad; 傍晚 (bàngwǎn) is het korte stukje vlak voor het donker.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Nieuws lezen", 24)
c.para("Als een verhaal een bewering (说法) bevat, scheid dan drie soorten zinnen: beweringen (说法), data (数据) en voorspellingen (预报). Pagina 6 is het voorbeeld: 「最大的一波」 is een bewering over 11 november, de veelvouden 1,5 en 2,5 zijn gerapporteerde data, en de temperaturen van de koude lucht zijn een voorspelling — voorspeld, nog geen feit.", 21.5)
c.glossline("Vraag bij elk getal: van wie is het, en wanneer is het gemeten?")
c.ex("B2", "单选", "C", "「最大的一波」 is een bewering, geen gemeten data.",
     "「最大的一波」在第6版里是什么? A. 数据 · B. 预报 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — gemeten getallen, geen beweringen.",
     "买东西以前,先看___,再看广告。", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Data en afrekenpagina eerst, kop het laatst.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — een voorspelling, nog geen feit.",
     "冷空气的温度是___,还没发生。", instr="Vul in", size=20.5, gap=10)
c.para("Probeer het zelf: in de kalender op pagina 1 is 「11月11日」 een datum — data. De woorden in een advertentie zijn beweringen. Kun je ze uit elkaar houden?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) markeert hoe een handeling gebeurt."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) verbindt werkwoord + graad: 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "Volgorde: getal + telwoord + zelfstandig naamwoord."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日,星期日凌晨3点。」", "Tijden gaan groot → klein: weekdag het laatst."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所 · Foutenkliniek", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看取件码,再开柜门。」(Controleer de code en open het kluisje.) De structuur 先…再… geeft de volgorde van de handelingen."
wcn = "Structuur: 先 … 再 … — eerst X, dan Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Zinsstructuur", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在北京。11月9日学校做了消防演练,我学会了走楼梯。双11我买了一本书,包裹两天就到了。周日凌晨,我想看S16总决赛!」"
lcn = "编辑部示例信,不是真实来信。VOL.2曾预告本期刊登真实来信和最佳作文;截至11月2日截稿,仍未收到,本期仍刊示例,继续征集。延期不是取消。Opmerking van de redactie: VOL.2 beloofde echte brieven in VOL.3; er kwam er geen vóór 2 nov. Het voorbeeld blijft staan. Uitgesteld, niet geannuleerd."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · Lezershoek", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · Zinnen van de week (letterlijk, uit de artikelen van dit nummer)", 27, "sans", True, OLIVE)
quotes = [
    ("「双11的正日子」", "De Double 11-dag zelf.", "p. 1"),
    ("「先看结算页,再决定买不买」", "Kijk naar de afrekenpagina en beslis dan.", "p. 2"),
    ("「提高自防自救能力」", "Verhoog het vermogen tot zelfbescherming en zelfredding.", "p. 3"),
    ("「三支队进了八强」", "Drie teams in de kwartfinales.", "p. 4"),
    ("「输了就回家」", "Verlies en je gaat naar huis.", "p. 4"),
    ("「老电影,新画面」", "Een oude film, een nieuw beeld.", "p. 5"),
    ("「快递的高峰分三波」", "De pakketpiek komt in drie golven.", "p. 6"),
    ("「着火了不坐电梯」", "Neem bij brand de lift niet.", "p. 3"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 150
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 150 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期预告 · Volgende week (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16总决赛打完了,谁是冠军?包裹都到了吗?还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
