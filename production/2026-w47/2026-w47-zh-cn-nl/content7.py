# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语　Taalfocus", "Lucerna", "语言聚焦　三个级别，三个主题　Drie niveaus, drie onderwerpen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　决赛与包裹　Finale pakketten", 24)
a.para("Woorden van de week: 决赛 (juésài, de finale), 冠军 (guànjūn, de kampioen), 半决赛 (bànjuésài, de halve finale), 到货 (dàohuò, aangekomen), 退换货 (tuìhuànhuò, retour en ruil), 价保 (jiàbǎo, prijsbescherming).", 21.5)
a.glossline("Telwoorden blijven belangrijk: 一个包裹 (een pakket), 一部电影 (een film), 一场演练 (een oefening).")
a.ex("A2", "完成句子", "个", "包裹 neemt het telwoord 个 gè.",
     "我拿了___包裹。", instr="Vul in", size=20, gap=10)
a.ex("A2", "单选", "A", "决赛 betekent de finale, de laatste wedstrijd.",
     "「决赛」是什么意思？ A. 最后一场比赛 · B. 第一场比赛 · C. 练习赛", size=20, gap=10)
a.ex("A2", "完成句子", "决赛", "juésài — de finale; BLG tegen GEN op 15 nov.",
     "11月15日凌晨3点，BLG和GEN打___。", instr="Vul in", size=20, gap=10)
a.ex("A2", "单选", "A", "Pakketten nemen 个 — niet 只 of 条.",
     "哪个说法对？ A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20, gap=10)
a.para("Nog een om te oefenen: 「我的包裹到了吗？」 (Is mijn pakket er?) Als je op een pakket wacht, vraag het eerst en ga dan naar de kluis.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　时间与日期　Tijd & data", 24)
b.para("Chinees zet tijden van groot naar klein: jaar, maand, dag, weekdag, dagdeel, uur. Voorbeelden uit dit nummer: 「11月15日星期日凌晨3点」 (zo 15 nov., 3 uur 's nachts), 「11月22日星期日」 (zo 22 nov.), 「11月21日星期六」 (za 21 nov.). De grootste eenheid eerst, niets door elkaar.", 21.5)
b.glossline("Zo wordt het Engelse «Sunday, Nov 22» 11月22日星期日.")
b.ex("B1", "单选", "B", "凌晨 língchén — de kleine uurtjes na middernacht.",
     "「凌晨3点」是什么时候？ A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20, gap=10)
b.ex("B1", "完成句子", "早上", "06:00 is 早上 — niet 's avonds.",
     "半决赛在北京时间11月8日___6点开始。（不是晚上）", instr="Vul in", size=20, gap=10)
b.ex("B1", "单选", "A", "Volgorde van groot naar klein: 22 nov., zondag.",
     "哪个顺序对？ A. 11月22日星期日 · B. 星期日11月22日 · C. 星期日小雪11月22日", size=20, gap=10)
b.ex("B1", "完成句子", "周日", "22 nov. is een zondag — 周日.",
     "11月22日是星期日，也可以说___。小雪在这天。", instr="Vul in", size=20, gap=10)
b.para("Nog twee woorden: 凌晨 (língchén) zijn de kleine uurtjes na middernacht, vóór de dageraad; 傍晚 (bàngwǎn) is het korte stukje vlak voor het donker.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　读新闻　Nieuws lezen", 24)
c.para("Als een verhaal een bewering (说法) bevat, scheid dan drie soorten zinnen: beweringen (说法), gegevens (数据) en voorspellingen (预报). Pagina 6 is het voorbeeld: 「没有爆掉」 is een bewering over de pakketten van dit jaar, het totaal 139.38亿件 zijn gerapporteerde gegevens — al geteld, geen gok — en 「第三波是最高峰」 is een voorspelling van 中通云仓: verwacht, nog niet geteld.", 21.5)
c.glossline("Vraag bij elk getal: van wie is het, en wanneer is het gemeten?")
c.ex("B2", "单选", "A", "「139.38亿件」 is een definitieve telling van de postdienst, al geteld.",
     "「139.38亿件」在第6版里是什么？ A. 已经数完的事实 · B. 邮政局的预计 · C. 广告词", size=20, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — gemeten getallen, geen beweringen.",
     "买东西以前，先看___，再看广告。", instr="Vul in", size=20, gap=10)
c.ex("B2", "单选", "B", "Data en afrekenpagina eerst, kop het laatst.",
     "读新闻时，哪个做法最好？ A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — een voorspelling, nog geen feit.",
     "「第三波是最高峰」是___，还没发生。", instr="Vul in", size=20, gap=10)
c.para("Probeer het zelf: in het kalenderkader op pagina 1 is 「11月22日」 een datum — een gegeven. De woorden in een advertentie zijn beweringen. Kun jij ze onderscheiden?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters + image ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) markeert hoe een handeling gebeurt."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) verbindt werkwoord + graad: 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "Volgorde: getal + telwoord + naamwoord."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日，星期日凌晨3点。」", "Tijden gaan groot → klein: weekdag het laatst."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所　Foutenkliniek", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看预报，再决定穿什么。」Het patroon 先…再… geeft de volgorde van de handelingen."
wcn = "Structuur: 先 … 再 … — eerst X, dan Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式　Zinspatroon", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好！我住在上海。11月9日半决赛，我看了BLG打T1，3比1，真好看！双11我买了一件外套，包裹两天就到了。你们呢？」"
lcn = "编辑部示例信，不是真实来信。VOL.3曾预告本期刊登真实来信和最佳作文；截至11月10日截稿，仍未收到，继续征集。延期不是取消。Noot van de redactie: VOL.3 beloofde echte brieven; tot 10 nov. kwam er geen. Uitgesteld, niet afgelast."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地　Lezershoek", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- P7 image (brush) below the letters box ----
iy7 = col3_end + 12
image(p, "brush.jpg", bx, iy7, CW, 130)
cy7 = caption(p, bx, iy7 + 130, CW, "毛笔（资料图）。写中文，先从一笔一画开始。",
              "Foto: Mx. Granger — CC0 (Wikimedia Commons)")
img_end = cy7
print("P7 image ends", img_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, img_end + 44)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "本周金句　Zinnen van de week (letterlijk, uit de artikelen van dit nummer)", 27, "sans", True, OLIVE)
quotes = [
    ("「决赛对阵GEN」", "De finale: BLG tegen GEN.", "p. 1"),
    ("「包裹都到了吗」", "Zijn alle pakketten er?", "p. 2"),
    ("「小雪气寒而将雪矣」", "Kleine Sneeuw: de lucht wordt koud, de sneeuw komt eraan.", "p. 3"),
    ("「两支中国队进了四强」", "Twee Chinese teams haalden de halve finales.", "p. 4"),
    ("「先看简介，再决定」", "Lees eerst de samenvatting en beslis dan.", "p. 5"),
    ("「无高峰，全高峰」", "Geen enkele piek — elke dag is een piek.", "p. 6"),
    ("「先打开看一看，再确认收货」", "Open en controleer eerst, bevestig dan de ontvangst.", "p. 6"),
    ("「悦读深圳」", "Vrolijk lezen in Shenzhen — het thema van de Shenzhen-Leesmaand.", "p. 3"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 120
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 120 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "下期预告　Volgende week (VOL.5)", 24, "sans", True, GOOSE)
p.para(MX + 28, py + 84, "S16总决赛打完了，谁是冠军？小雪之后，冬天怎么过？还有你们的来信和第8版最佳作文。下周见！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
