# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-nl-reproof/work/freeze-full/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Taal in de kijker", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Drie niveaus, drie thema's")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与冬天 · Winkelen", 24)
a.para("Winkelwoorden voor deze week: 现货 (xiànhuò, op voorraad), 直降 (zhíjiàng, een directe verlaging), 立减 (lìjiǎn, af bij het afrekenen), 结算页 (jiésuàn yè, de afrekenpagina). Winterwoorden: 立冬 (lìdōng, Begin van de winter), 补冬 (bǔdōng, goed eten vóór de winter), 厚衣服 (hòu yīfu, warme kleren).", 21.5)
a.glossline("Maatwoorden blijven belangrijk: 一件毛衣 (een trui), 一条围巾 (een sjaal), 一部电影 (een film).")
a.ex("A2", "完成句子", "件", "毛衣 neemt het maatwoord 件 jiàn.",
     "我想买一___毛衣。", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "单选", "A", "直降 betekent dat de prijs zelf daalt.",
     "「直降」是什么意思? A. 价格直接变低 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "立冬", "lìdōng — Begin van de winter, 7 nov.",
     "11月7日是___。", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "单选", "A", "Kleren nemen 件, niet 个 of 条.",
     "哪个说法对? A. 一件毛衣 · B. 一个毛衣 · C. 一条毛衣", size=20.5, gap=10)
a.para("Nog één om te oefenen: 「这件毛衣多少钱?」 (Hoeveel kost deze trui?) Vraag in de winkel eerst de prijs, betaal daarna.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Tijd en data", 24)
b.para("Het Chinees geeft tijden van groot naar klein: jaar, maand, dag, weekdag, dagdeel, uur. Voorbeelden uit dit nummer: 「11月7日星期六17点52分」 (za 7 nov., 17.52 u.), 「11月10日星期二20点」 (di 10 nov., 20.00 u.), 「11月15日凌晨3点」 (15 nov., 3 u. 's nachts). De grootste eenheid eerst, niets uit volgorde.", 21.5)
b.glossline("Zo wordt het Nederlandse «zaterdagavond 7 november» in het Chinees 11月7日星期六晚上.")
b.ex("B1", "单选", "B", "凌晨 língchén — de kleine uurtjes na middernacht.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "06.00 u. is 早上 (ochtend), geen avond.",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Volgorde groot → klein: 7 nov., zaterdag, 17.52 u.",
     "哪个顺序对? A. 11月7日星期六17点52分 · B. 17点52分星期六11月7日 · C. 星期六17点52分11月7日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周六", "7 nov. is een zaterdag — 周六.",
     "11月7日是星期六,也可以说___。立冬在这天。", instr="Vul in", size=20.5, gap=10)
b.para("Nog twee woorden: 凌晨 (língchén) zijn de kleine uurtjes na middernacht, vóór de dageraad; 傍晚 (bàngwǎn) is het korte stukje vlak vóór het donker wordt.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Het nieuws lezen", 24)
c.para("Als een verhaal een bewering (说法) bevat, onderscheid dan drie soorten zinnen: beweringen (说法), data (数据) en advertenties (广告). Pagina 6 is het voorbeeld: 「最低价」 is een bewering, de 270 yuan van de oefenmandjes zijn oefendata, en de afrekenpagina laat zien wat je echt betaalt.", 21.5)
c.glossline("Vraag bij elke prijs: van wie is dit cijfer, en waar staat het geschreven?")
c.ex("B2", "单选", "C", "「最低价」 is een reclamebewering, geen gemeten data.",
     "「最低价」在第6版里是什么? A. 数据 · B. 声明 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — gemeten cijfers, geen beweringen.",
     "买东西以前,先看___,再看广告。", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Eerst de data en de afrekenpagina, de kop het laatst.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "结算", "jiésuàn — de afrekenpagina toont de echte prijs.",
     "真正要付的钱,看___页的价格。", instr="Vul in", size=20.5, gap=10)
c.para("Probeer het zelf: in het kalenderkader op pagina 1 is 「11月7日」 een datum — data. De woorden in een advertentie zijn beweringen. Kun jij ze uit elkaar houden?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de) markeert de manier van handelen."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de): werkwoord + graad, bijv. 跑得快."),
    ("「我买了三只毛衣个」", "→ 「我买了三件毛衣。」", "Volgorde: getal + maatwoord + zelfstandig naamwoord. De laatste 个 is er één te veel; truien nemen 件."),
    ("「立冬在星期六十一月七日」", "→ 「立冬在11月7日,星期六。」", "Tijden: groot → klein, weekdag het laatst."),
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
wt = "「先看评价,再下单。」(Eerst beoordelingen checken, dan bestellen.) 先…再… geeft de volgorde aan. Meer: 「先看天气,再出门。」"
wcn = "Patroon: 先 … 再 … — eerst X, dan Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Zinspatroon", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在上海。立冬那天,我吃了饺子,也给妈妈打了电话。双11,我买了一件毛衣,现货第二天就到了。」"
lcn = "编辑部示例信,不是真实来信。编辑部说明:VOL.1曾预告本期(VOL.2)刊登真实读者来信和VOL.1第8版最佳作文;至今没有收到真实来信,也没有可刊登的投稿,所以本期仍刊登编辑部示例,并继续征集。延期不是取消。Redactie: VOL.1 beloofde echte brieven in VOL.2. Die zijn er nog niet, dus een voorbeeldbrief. Uitgesteld, niet afgesteld — stuur ons je eigen brief in het Chinees!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
# NOTE: the disclosure above mixes Chinese and English in one string; the
# sans wrap measures CJK and Latin with the same SC face, so the height
# formula above (sans, 20pt) matches the render path. Verified in the build log.
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
    ("「不用等11月11日」", "Je hoeft niet te wachten tot 11 nov.", "p. 1"),
    ("「下单就能发货」", "Bestel het en het wordt verstuurd.", "p. 2"),
    ("「先看结算页,再付款」", "Controleer de afrekenpagina en betaal dan.", "p. 2"),
    ("「水开始结冰」", "Het water begint te bevriezen.", "p. 3"),
    ("「三场都输了」", "Alle drie de series verloren.", "p. 4"),
    ("「小局一场没赢」", "Geen enkele game gewonnen.", "p. 4"),
    ("「故事够不够好」", "Maar is het verhaal wel goed genoeg?", "p. 5"),
    ("「别以后,就现在」", "Niet later — nu.", "p. 5"),
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
p.text(MX + 28, py + 44, "下期预告 · Volgende week (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "双11当天11月11日星期三,包裹到了吗?S16淘汰赛打完了,谁进了决赛?总决赛北京时间11月15日凌晨3点。还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
