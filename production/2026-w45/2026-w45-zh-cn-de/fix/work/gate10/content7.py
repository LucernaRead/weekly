# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-de-fix/work/gate10/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Sprachfokus", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Drei Niveaus, drei Themen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与冬天 · Einkaufen", 24)
a.para("Einkaufswörter dieser Woche: 现货 (xiànhuò, auf Lager), 直降 (zhíjiàng, eine direkte Senkung), 立减 (lìjiǎn, Abzug an der Kasse), 结算页 (jiésuàn yè, die Kassenseite). Winterwörter: 立冬 (lìdōng, Winteranfang), 补冬 (bǔdōng, vor dem Winter gut essen), 厚衣服 (hòu yīfu, warme Kleidung).", 21.5)
a.glossline("Zählwörter zählen weiterhin: 一件毛衣 (ein Pullover), 一条围巾 (ein Schal), 一部电影 (ein Film).")
a.ex("A2", "完成句子", "件", "毛衣 nimmt das Zählwort 件 jiàn.",
     "我想买一___毛衣。", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "单选", "A", "直降 heißt: Der Preis selbst sinkt.",
     "「直降」是什么意思? A. 价格直接变低 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "立冬", "lìdōng — Winteranfang, 7. Nov.",
     "11月7日是___。", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "单选", "A", "Kleidung nimmt 件, nicht 个 oder 条.",
     "哪个说法对? A. 一件毛衣 · B. 一个毛衣 · C. 一条毛衣", size=20.5, gap=10)
a.para("Noch eins zum Üben: 「这件毛衣多少钱?」 (Wie viel kostet dieser Pullover?) Fragen Sie beim Einkaufen erst nach dem Preis, dann zahlen Sie.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Zeit & Daten", 24)
b.para("Chinesisch ordnet Zeiten groß → klein: Jahr, Monat, Tag, Wochentag, Tageszeit, Stunde. Beispiele aus dieser Ausgabe: 「11月7日星期六17点52分」 (Sa., 7. Nov., 17:52 Uhr), 「11月10日星期二20点」 (Di., 10. Nov., 20:00 Uhr), 「11月15日凌晨3点」 (15. Nov., 3 Uhr nachts). Die größte Einheit zuerst, nichts in falscher Reihenfolge.", 21.5)
b.glossline("So wird aus „Samstagabend, 7. November“ 11月7日星期六晚上.")
b.ex("B1", "单选", "B", "凌晨 língchén — die kleinen Stunden nach Mitternacht.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "06:00 Uhr ist 早上 (morgens), nicht abends.",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Reihenfolge groß → klein: 7. Nov., Samstag, 17:52 Uhr.",
     "哪个顺序对? A. 11月7日星期六17点52分 · B. 17点52分星期六11月7日 · C. 星期六17点52分11月7日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周六", "Der 7. Nov. ist ein Samstag — 周六.",
     "11月7日是星期六,也可以说___。立冬在这天。", instr="Ausfüllen", size=20.5, gap=10)
b.para("Noch zwei Wörter: 凌晨 (língchén) sind die kleinen Stunden nach Mitternacht, vor der Morgendämmerung; 傍晚 (bàngwǎn) ist die kurze Zeit kurz vor Einbruch der Dunkelheit.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Nachrichten lesen", 24)
c.para("Wenn eine Geschichte eine Behauptung (说法) enthält, trennen Sie drei Arten von Sätzen: Behauptungen (说法), Daten (数据) und Werbung (广告). Seite 6 ist das Beispiel: 「最低价」 ist eine Behauptung, die 270元 der Übungskörbe sind Übungsdaten, und die Kassenseite zeigt, was Sie wirklich zahlen.", 21.5)
c.glossline("Fragen Sie bei jedem Preis: Wessen Zahl ist das, und wo steht sie?")
c.ex("B2", "单选", "C", "「最低价」 ist Werbung, keine gemessenen Daten.",
     "「最低价」在第6版里是什么? A. 数据 · B. 声明 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — gemessene Zahlen, keine Behauptungen.",
     "买东西以前,先看___,再看广告。", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Erst Daten und Kassenseite, die Schlagzeile zuletzt.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "结算", "jiésuàn — die Kassenseite zeigt den echten Preis.",
     "真正要付的钱,看___页的价格。", instr="Ausfüllen", size=20.5, gap=10)
c.para("Probieren Sie es selbst: Im Kalenderkasten auf Seite 1 ist 「11月7日」 ein Datum — Daten. Die Wörter in einer Werbung sind Behauptungen. Können Sie sie unterscheiden?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de) gibt an, wie etwas getan wird."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de) verbindet Verb + Grad: 跑得快."),
    ("「我买了三只毛衣个」", "→ 「我买了三件毛衣。」", "Reihenfolge: Zahl + Zählwort + Nomen. Das 个 am Ende ist eins zu viel; Pullover nehmen 件."),
    ("「立冬在星期六十一月七日」", "→ 「立冬在11月7日,星期六。」", "Zeiten: groß → klein, Wochentag zuletzt."),
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
wt = "「先看评价,再下单。」(Erst prüfen, dann bestellen.) 先…再… gibt die Reihenfolge an. Mehr: 「先看天气,再出门。」"
wcn = "Muster: 先 … 再 … — erst X, dann Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Satzmuster", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在上海。立冬那天,我吃了饺子,也给妈妈打了电话。双11,我买了一件毛衣,现货第二天就到了。」"
lcn = "编辑部示例信,不是真实来信。编辑部说明:VOL.1曾预告本期(VOL.2)刊登真实读者来信和VOL.1第8版最佳作文;至今没有收到真实来信,也没有可刊登的投稿,所以本期仍刊登编辑部示例,并继续征集。延期不是取消。Redaktionsbeispiel — kein echter Brief. VOL.1 versprach echte Briefe in VOL.2; keiner kam an. Aufgeschoben, nicht aufgehoben — schreiben Sie uns Ihren Brief auf Chinesisch!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
# NOTE: the disclosure above mixes Chinese and English in one string; the
# sans wrap measures CJK and Latin with the same SC face, so the height
# formula above (sans, 20pt) matches the render path. Verified in the build log.
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
p.text(MX, fy + 24, "本周金句 · Sätze der Woche (wörtlich, aus den Artikeln dieser Ausgabe)", 27, "sans", True, OLIVE)
quotes = [
    ("「不用等11月11日」", "Man muss nicht bis zum 11. Nov. warten.", "S. 1"),
    ("「下单就能发货」", "Bestellen — und es wird versandt.", "S. 2"),
    ("「先看结算页,再付款」", "Erst die Kassenseite prüfen, dann zahlen.", "S. 2"),
    ("「水开始结冰」", "Das Wasser beginnt zu gefrieren.", "S. 3"),
    ("「三场都输了」", "Alle drei Serien verloren.", "S. 4"),
    ("「小局一场没赢」", "Kein einziges Spiel gewonnen.", "S. 4"),
    ("「故事够不够好」", "Aber ist die Geschichte gut genug?", "S. 5"),
    ("「别以后,就现在」", "Nicht später — jetzt.", "S. 5"),
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
p.text(MX + 28, py + 44, "下期预告 · Nächste Woche (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "双11当天11月11日星期三,包裹到了吗?S16淘汰赛打完了,谁进了决赛?总决赛北京时间11月15日凌晨3点。还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
