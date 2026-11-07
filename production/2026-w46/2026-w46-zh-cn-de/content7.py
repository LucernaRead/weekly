# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-cn-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Sprachfokus", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Drei Stufen, drei Themen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与包裹 · Einkaufen", 24)
a.para("Einkaufswörter für diese Woche: 高潮场 (gāocháochǎng, die Hauptverkaufszeit), 包裹 (bāoguǒ, ein Paket), 取件码 (qǔjiànmǎ, ein Abholcode), 快递柜 (kuàidìguì, ein Paketfach). Sicherheitswörter: 消防 (xiāofáng, Brandschutz), 疏散 (shūsàn, evakuieren), 自救 (zìjiù, Selbstrettung).", 21.5)
a.glossline("Zählwörter sind weiter wichtig: 一个包裹 (ein Paket), 一部电影 (ein Film), 一场演练 (eine Übung).")
a.ex("A2", "完成句子", "个", "包裹 nimmt das Zählwort 个 gè.",
     "我拿了___包裹。", instr="Ergänzen", size=20.5, gap=10)
a.ex("A2", "单选", "A", "高潮场 bedeutet die Hauptverkaufszeit.",
     "「高潮场」是什么意思? A. 最忙的卖货时间 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "消防", "xiāofáng — Brandschutz, 9. Nov.",
     "11月9日是全国___日。", instr="Ergänzen", size=20.5, gap=10)
a.ex("A2", "单选", "A", "Pakete nehmen 个 — nicht 只 oder 条.",
     "哪个说法对? A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20.5, gap=10)
a.para("Noch eins zum Üben: 「我的包裹到了吗?」 (Ist mein Paket schon da?) Wenn du auf ein Paket wartest, frag zuerst, dann geh zum Fach.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Zeit und Daten", 24)
b.para("Chinesisch gibt Zeiten groß → klein an: Jahr, Monat, Tag, Wochentag, Tageszeit, Stunde. Beispiele aus dieser Ausgabe: 「11月9日星期一」 (Mo., 9. Nov.), 「11月10日星期二20点」 (Di., 10. Nov., 20:00 Uhr), 「11月15日星期日凌晨3点」 (So., 15. Nov., 3 Uhr morgens). Die größte Einheit zuerst, nichts durcheinander.", 21.5)
b.glossline("So wird aus dem englischen «Monday, Nov 9» 11月9日星期一.")
b.ex("B1", "单选", "B", "凌晨 língchén — die frühen Stunden nach Mitternacht.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "06:00 Uhr ist 早上 — nicht abends.",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="Ergänzen", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Reihenfolge groß → klein: 15. Nov., Sonntag, 03:00 Uhr.",
     "哪个顺序对? A. 11月15日星期日凌晨3点 · B. 凌晨3点星期日11月15日 · C. 星期日凌晨3点11月15日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周一", "Der 9. November ist ein Montag — 周一.",
     "11月9日是星期一,也可以说___。消防日在这天。", instr="Ergänzen", size=20.5, gap=10)
b.para("Noch zwei Wörter: 凌晨 (língchén) sind die frühen Stunden nach Mitternacht, vor der Morgendämmerung; 傍晚 (bàngwǎn) ist die kurze Zeit kurz vor Einbruch der Dunkelheit.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Nachrichten lesen", 24)
c.para("Wenn eine Geschichte eine Behauptung (说法) enthält, trenne drei Arten von Sätzen: Behauptungen (说法), Daten (数据) und Vorhersagen (预报). Seite 6 ist das Beispiel: 「最大的一波」 ist eine Behauptung über den 11. November, die Vielfachen 1,5 und 2,5 sind gemeldete Daten, und die Kaltlufttemperaturen sind eine Vorhersage — vorhergesagt, noch keine Tatsache.", 21.5)
c.glossline("Frag bei jeder Zahl: Wessen Zahl ist das, und wann wurde sie gemessen?")
c.ex("B2", "单选", "C", "「最大的一波」 ist eine Behauptung, keine gemessenen Daten.",
     "「最大的一波」在第6版里是什么? A. 数据 · B. 预报 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — gemessene Zahlen, keine Behauptungen.",
     "买东西以前,先看___,再看广告。", instr="Ergänzen", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Daten und Kassenseite zuerst, Schlagzeile zuletzt.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — eine Vorhersage, noch keine Tatsache.",
     "冷空气的温度是___,还没发生。", instr="Ergänzen", size=20.5, gap=10)
c.para("Probier es selbst: Im Kalenderkasten auf Seite 1 ist 「11月11日」 ein Datum — Daten. Die Wörter in einer Werbung sind Behauptungen. Kannst du sie unterscheiden?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) zeigt, wie eine Handlung ausgeführt wird."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) verbindet Verb + Grad: 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "Reihenfolge: Zahl + Zählwort + Substantiv."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日,星期日凌晨3点。」", "Zeiten gehen groß → klein: Wochentag zuletzt."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所 · Fehlerklinik", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看取件码,再开柜门。」(Prüfe den Code, dann öffne das Fach.) Der Rahmen 先…再… gibt die Reihenfolge der Handlungen an."
wcn = "Rahmen: 先 … 再 … — erst X, dann Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Satzrahmen", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在北京。11月9日学校做了消防演练,我学会了走楼梯。双11我买了一本书,包裹两天就到了。周日凌晨,我想看S16总决赛!」"
lcn = "编辑部示例信,不是真实来信。VOL.2曾预告本期刊登真实来信和最佳作文;截至11月2日截稿,仍未收到,本期仍刊示例,继续征集。延期不是取消。Anmerkung der Redaktion: VOL.2 versprach echte Leserbriefe in VOL.3; bis zum 2. Nov. kam keiner an. Das Beispiel bleibt stehen. Verschoben, nicht abgesagt."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · Leserecke", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · Sätze der Woche (wörtlich, aus den eigenen Artikeln dieser Ausgabe)", 27, "sans", True, OLIVE)
quotes = [
    ("「双11的正日子」", "Der Double-11-Tag selbst.", "S. 1"),
    ("「先看结算页,再决定买不买」", "Prüfe die Kassenseite, dann entscheide.", "S. 2"),
    ("「提高自防自救能力」", "Die Fähigkeit zu Selbstschutz und Selbstrettung stärken.", "S. 3"),
    ("「三支队进了八强」", "Drei Teams im Viertelfinale.", "S. 4"),
    ("「输了就回家」", "Verlieren und nach Hause fahren.", "S. 4"),
    ("「老电影,新画面」", "Ein alter Film, ein neues Bild.", "S. 5"),
    ("「快递的高峰分三波」", "Die Paketwelle kommt in drei Wellen.", "S. 6"),
    ("「着火了不坐电梯」", "Bei einem Brand nimm nicht den Aufzug.", "S. 3"),
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
p.text(MX + 28, py + 44, "下期预告 · Nächste Woche (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16总决赛打完了,谁是冠军?包裹都到了吗?还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
