# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Taal in de kijker", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Drie niveaus, drie thema's")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 购物与量词 · Maatwoorden", 24)
a.para("Als je winkelt, gebruikt het Chinees maatwoorden (量词): 一件外套 (een jas), 一条围巾 (een sjaal), 一斤蟹 (een halve kilo krab), 一只蟹 (één krab). Het patroon is: getal + maatwoord + zelfstandig naamwoord (数词 + 量词 + 名词).", 21.5)
a.glossline("Het Nederlands telt vrij losjes; het Chinees kiest bij elke soort ding een eigen maatwoord — geen meervoud, geen -s.")
a.ex("A2", "完成句子", "件", "wàitào neemt het maatwoord jiàn.",
     "我想买一___外套。", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "单选", "B", "wéijīn neemt tiáo, voor lange, zachte dingen.",
     "「一条」可以说什么? A. 一条外套 · B. 一条围巾 · C. 一条大闸蟹", size=20.5, gap=10)
a.ex("A2", "完成句子", "斤", "jīn — een halve kilo; marktprijzen zijn per jīn.",
     "大闸蟹多少钱一___?", instr="Vul in", size=20.5, gap=10)
a.ex("A2", "单选", "A", "Kleding neemt jiàn, niet gè of tiáo.",
     "哪个说法对? A. 一件衣服 · B. 一个衣服 · C. 一条衣服", size=20.5, gap=10)
a.para("Nog een om te oefenen: 「这件外套多少钱?」 (Hoeveel kost deze jas?) Vraag in de winkel eerst de prijs, betaal daarna.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Tijd en data", 24)
b.para("Het Chinees geeft tijden van groot naar klein: jaar, maand, dag, weekdag, dagdeel, uur. Voorbeeld: 20 okt., 20 u. wordt 「10月20日晚上8点」 — de grootste eenheid eerst, niets uit volgorde.", 21.5)
b.glossline("Zo wordt het Nederlandse «vrijdagavond 23 oktober» in het Chinees 10月23日星期五晚上.")
b.ex("B1", "单选", "B", "língchén — de kleine uurtjes na middernacht.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "上午", "De NBA opende 's ochtends, Pekingtijd.",
     "NBA 在北京时间10月21日___开打。(不是晚上)", instr="Vul in", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Volgorde groot naar klein: 20 okt., avond, 20 u.",
     "哪个顺序对? A. 10月20日晚上8点 · B. 8点晚上10月20日 · C. 晚上8点10月20日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周五", "23 okt. is een vrijdag — zhōuwǔ.",
     "10月23日是星期五,也可以说___。霜降在这天。", instr="Vul in", size=20.5, gap=10)
b.para("Nog twee woorden: 凌晨 (língchén) zijn de kleine uurtjes na middernacht, vóór de dageraad; 傍晚 (bàngwǎn) is het korte stukje vlak vóór het donker wordt.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Het nieuws lezen", 24)
c.para("Als een verhaal een geschil (争议) bevat, scheid dan drie soorten zinnen: online beweringen (说法), officiële verklaringen (声明) en marktgegevens (数据). Beweringen kunnen overdrijven; gegevens moeten hun bron en datum behouden. Pagina 6 is het voorbeeld: 「暴跌40%」 is een bewering, 77,5 元 en 57,5 元 zijn gegevens, 「崩盘不实」 is een verklaring.", 21.5)
c.glossline("Vraag bij elk cijfer: wie heeft het gemeten, en wanneer?") 
c.ex("B2", "单选", "C", "De daling van 40 procent was een online bewering.",
     "「暴跌超过40%」在第6版里是什么? A. 数据 · B. 声明 · C. 网上的说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "声明", "shēngmíng — de officiële verklaring van de vereniging.",
     "协会10月19日发表___,说「崩盘」不是真的。", instr="Vul in", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Gegevens en bron eerst; de kop het laatst.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和出处 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "25.8", "De echte, berekende daling op pagina 6 is 25,8%.",
     "第6版真正算出的数据降幅是___%。", instr="Vul in", size=20.5, gap=10)
c.para("Probeer het zelf: in het zoektrends-kader op pagina 1 is 「第 8 位」 een rangorde — een gegeven. De woorden in een kop zijn beweringen. Kun jij ze uit elkaar houden?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de) markeert hoe een handeling wordt gedaan; het staat vóór het werkwoord."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de) verbindt een werkwoord met een graadcomplement: 跑得快."),
    ("「我买了三只大闸蟹个」", "→ 「我买了三只大闸蟹。」", "Volgorde: getal + maatwoord + zelfstandig naamwoord. De laatste 个 is er één te veel; krabben nemen zhī, 只."),
    ("「霜降在星期五十月二十三日」", "→ 「霜降在10月23日,星期五。」", "Tijden gaan van groot naar klein: eerst maand en dag, de weekdag het laatst."),
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
wt = "「先付定金,后付尾款。」(Eerst de aanbetaling, dan het restbedrag.) Het patroon 先…后/再… geeft de volgorde van handelingen. Meer: 「先看天气,再出门。」「先洗手,再吃饭。」"
wcn = "Patroon: 先 … 后/再 … — eerst X, dan Y. Maak je eigen zin."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Zinspatroon", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在多伦多。霜降那天,我吃了柿子,也给妈妈打了电话。我的购物车里有一件外套,还在等付尾款。」"
lcn = "Een voorbeeldbrief van de redactie — geen echte. In VOL.2 staan echte lezersbrieven en de beste schrijfopdracht van pagina 8!"
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
    ("「今年的双11来得早」", "De 双11 van dit jaar kwam vroeg.", "p. 1"),
    ("「付完尾款，快递就开始送货了」", "Zodra het restbedrag is betaald, begint de bezorging.", "p. 1"),
    ("「付完尾款，商家就发货」", "Zodra je het restbedrag betaalt, verstuurt de verkoper.", "p. 2"),
    ("「遥知兄弟登高处，遍插茱萸少一人」", "Wang Wei's beroemde regel over Chóngyáng, uit zijn gedicht.", "p. 3"),
    ("「两个分数只差2.735分」", "De twee scores verschillen slechts 2.735 punten.", "p. 4"),
    ("「最大的看点是詹姆斯」", "De grootste trekpleister is LeBron.", "p. 4"),
    ("「看S16，要通宵了」", "S16 kijken betekent de hele nacht opblijven.", "p. 5"),
    ("「先看数据，再看标题」", "Gegevens eerst, kop het laatst, de regel van pagina 6.", "p. 6"),
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
p.text(MX + 28, py + 44, "下期预告 · Volgende week (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16 瑞士轮打完了:LPL 的四支队打得怎么样?双11 的包裹都到了吗?我们追踪报道。11月7日是立冬,冬天要来了。还有你们的来信和第 8 版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
