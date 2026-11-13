# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语　Sprachfokus", "Lucerna", "语言聚焦　三个级别，三个主题　Drei Stufen, drei Themen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　决赛与包裹　Finale & Pakete", 24)
a.para("Wörter der Woche: 决赛 (juésài, das Finale), 冠军 (guànjūn, der Meister), 半决赛 (bànjuésài, das Halbfinale), 到货 (dàohuò, angekommen), 退换货 (tuìhuànhuò, Rückgabe und Umtausch), 价保 (jiàbǎo, Preisschutz).", 21.5)
a.glossline("Zählwörter sind weiter wichtig: 一个包裹 (ein Paket), 一部电影 (ein Film), 一场演练 (eine Übung).")
a.ex("A2", "完成句子", "个", "包裹 nimmt das Zählwort 个 gè.",
     "我拿了___包裹。", instr="Ergänzen", size=20, gap=10)
a.ex("A2", "单选", "A", "决赛 heißt das Finale, das letzte Spiel.",
     "「决赛」是什么意思？ A. 最后一场比赛 · B. 第一场比赛 · C. 练习赛", size=20, gap=10)
a.ex("A2", "完成句子", "决赛", "juésài — das Finale; BLG gegen GEN am 15. Nov.",
     "11月15日凌晨3点，BLG和GEN打___。", instr="Ergänzen", size=20, gap=10)
a.ex("A2", "单选", "A", "Pakete nehmen 个 — nicht 只 oder 条.",
     "哪个说法对？ A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20, gap=10)
a.para("Noch eins zum Üben: 「我的包裹到了吗？」 (Ist mein Paket da?) Wenn du auf ein Paket wartest, frag erst nach und geh dann zum Fach.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　时间与日期　Zeit & Daten", 24)
b.para("Chinesische Zeiten gehen vom Großen zum Kleinen: Jahr, Monat, Tag, Wochentag, Tageszeit, Stunde. Beispiele aus dieser Ausgabe: 「11月15日星期日凌晨3点」 (So, 15. Nov., 3 Uhr morgens), 「11月22日星期日」 (So, 22. Nov.), 「11月21日星期六」 (Sa, 21. Nov.). Die größte Einheit zuerst, nichts durcheinander.", 21.5)
b.glossline("So wird aus dem englischen «Sunday, Nov 22» 11月22日星期日.")
b.ex("B1", "单选", "B", "凌晨 língchén — die frühen Stunden nach Mitternacht.",
     "「凌晨3点」是什么时候？ A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20, gap=10)
b.ex("B1", "完成句子", "早上", "06:00 Uhr ist 早上 — nicht abends.",
     "半决赛在北京时间11月8日___6点开始。（不是晚上）", instr="Ergänzen", size=20, gap=10)
b.ex("B1", "单选", "A", "Groß-zu-klein-Reihenfolge: 22. Nov., Sonntag.",
     "哪个顺序对？ A. 11月22日星期日 · B. 星期日11月22日 · C. 星期日小雪11月22日", size=20, gap=10)
b.ex("B1", "完成句子", "周日", "Der 22. Nov. ist ein Sonntag — 周日.",
     "11月22日是星期日，也可以说___。小雪在这天。", instr="Ergänzen", size=20, gap=10)
b.para("Noch zwei Wörter: 凌晨 (língchén) sind die frühen Stunden nach Mitternacht, vor der Morgendämmerung; 傍晚 (bàngwǎn) ist die kurze Zeit kurz vor Einbruch der Dunkelheit.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　读新闻　Nachrichten lesen", 24)
c.para("Wenn eine Geschichte eine Behauptung (说法) enthält, trenne drei Arten von Sätzen: Behauptungen (说法), Daten (数据) und Prognosen (预报). Seite 6 ist das Beispiel: 「没有爆掉」 ist eine Behauptung über die Pakete dieses Jahres, die Summe 139.38亿件 ist gemeldete Daten — schon gezählt, kein Raten — und 「第三波是最高峰」 ist eine Prognose von 中通云仓: erwartet, noch nicht gezählt.", 21.5)
c.glossline("Frag bei jeder Zahl: Wessen Zahl ist das, und wann wurde sie gemessen?")
c.ex("B2", "单选", "A", "「139.38亿件」 ist eine endgültige Zahl der Postbehörde, schon gezählt.",
     "「139.38亿件」在第6版里是什么？ A. 已经数完的事实 · B. 邮政局的预计 · C. 广告词", size=20, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — gemessene Zahlen, keine Behauptungen.",
     "买东西以前，先看___，再看广告。", instr="Ergänzen", size=20, gap=10)
c.ex("B2", "单选", "B", "Daten und Kassenseite zuerst, Schlagzeile zuletzt.",
     "读新闻时，哪个做法最好？ A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — eine Vorhersage, noch keine Tatsache.",
     "「第三波是最高峰」是___，还没发生。", instr="Ergänzen", size=20, gap=10)
c.para("Probier es selbst: Im Kalenderkasten auf Seite 1 ist 「11月22日」 ein Datum — Daten. Die Wörter in einer Werbung sind Behauptungen. Kannst du sie unterscheiden?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters + image ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) zeigt, wie eine Handlung ausgeführt wird."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) verbindet Verb + Grad: 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "Reihenfolge: Zahl + Zählwort + Substantiv."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日，星期日凌晨3点。」", "Zeiten gehen groß → klein: Wochentag zuletzt."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所　Fehlerklinik", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看预报，再决定穿什么。」Die Struktur 先…再… gibt die Reihenfolge der Handlungen an."
wcn = "Rahmen: 先 … 再 … — erst X, dann Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式　Satzmuster", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好！我住在上海。11月9日半决赛，我看了BLG打T1，3比1，真好看！双11我买了一件外套，包裹两天就到了。你们呢？」"
lcn = "编辑部示例信，不是真实来信。VOL.3曾预告本期刊登真实来信和最佳作文；截至11月10日截稿，仍未收到，继续征集。延期不是取消。Anmerkung der Redaktion: VOL.3 versprach echte Briefe in VOL.4; bis zum 10. Nov. kam keiner an. Verschoben, nicht abgesagt."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地　Leserecke", 23, "sans", True, OLIVE)
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
p.text(MX, fy + 24, "本周金句　Sätze der Woche (wörtlich, aus den Artikeln dieser Ausgabe)", 27, "sans", True, OLIVE)
quotes = [
    ("「决赛对阵GEN」", "Das Finale: BLG gegen GEN.", "S. 1"),
    ("「包裹都到了吗」", "Sind alle Pakete da?", "S. 2"),
    ("「小雪气寒而将雪矣」", "Kleiner Schnee: Die Luft wird kalt, Schnee kommt.", "S. 3"),
    ("「两支中国队进了四强」", "Zwei chinesische Teams erreichten die Halbfinals.", "S. 4"),
    ("「先看简介，再决定」", "Lies erst die Inhaltsangabe, dann entscheide.", "S. 5"),
    ("「无高峰，全高峰」", "Kein einzelner Gipfel — jeder Tag ist ein Gipfel.", "S. 6"),
    ("「先打开看一看，再确认收货」", "Erst öffnen und prüfen, dann den Empfang bestätigen.", "S. 6"),
    ("「悦读深圳」", "Freudiges Lesen in Shenzhen — das Motto des Shenzhen-Lesemonats.", "S. 3"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 112
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
# Pitch 112 (not core's 120): de col-3 runs ~49px taller than core, so
# fy lands 49px lower; at pitch 120 the teaser band ended 2615.3, crossing
# the footer rule (2596) and the footer text. 112 saves 32px -> band ends
# ~2583, clear of the footer. Quote rows need ~76px, so 112 keeps slack.
py = fy + 66 + 4 * 112 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "下期预告　Nächste Woche (VOL.5)", 24, "sans", True, GOOSE)
p.para(MX + 28, py + 84, "S16总决赛打完了，谁是冠军？小雪之后，冬天怎么过？还有你们的来信和第8版最佳作文。下周见！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
