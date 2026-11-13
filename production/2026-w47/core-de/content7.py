# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　语言", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　本周金句与纠错诊所")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　DATEN SAGEN", 24)
fa.para("So sagen Sie Daten: Am 18. November ist Buß- und Bettag. Am 29. November ist der erste Advent. Mit werden sprechen Sie über das Passiv: Um 20.30 Uhr wird in München gespielt.")
fa.box("BEISPIELE　例句", [("„Am 18. November ist Buß- und Bettag.“　„Um 20.30 Uhr wird in München gespielt.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "完成句子", "wird", "被动：wird + Partizip II",
      "Am Freitag ___ in München gespielt.", instr="填空", size=22, gap=8)
fa.ex("A2", "完成句子", "werden", "复数：werden",
      "Die Weihnachtsmärkte ___ am Montag geöffnet.", instr="填空", size=22, gap=8)
fa.ex("A2", "完成句子", "wird", "werden + 原形表将来",
      "Der Adventskalender ___ am 1. Dezember beginnen.", instr="填空", size=22, gap=8)
fa.ex("A2", "单选", "A", "被动语态",
      "„Es wird gespielt“ ist... A. Passiv · B. Perfekt · C. Imperativ", size=22, gap=8)
fa.end_report()
# --- P7 image: reading room, below the A2 column (col 0 free space) ---
iy7 = fa.y + 16
image(p, "lesesaal.jpg", COLX[0], iy7, CW, 145)  # W47 D1: was 150; A2 flow grew with 16.5pt stems, keep caption clear of the 1548 rule
cy7 = caption(p, COLX[0], iy7 + 150, CW,
              "Der große Lesesaal der Library of Congress in Washington.",
              "Foto: Carol M. Highsmith — public domain")
print("P7 image ends", cy7, "(A2 flow ended", fa.y, ")")
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1　VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Der November ist stiller als der Oktober. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es dunkel ist — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE　例句", [("„Der November ist stiller als der Oktober.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "完成句子", "stiller", "still → stiller（十一月比十月安静）",
      "Im November ist es ___ (still) als im Oktober.", instr="填空", size=22, gap=8)
fb.ex("B1", "完成句子", "weil", "weil 引导原因",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="填空", size=22, gap=8)
fb.ex("B1", "句型转换", "Viele bleiben zu Hause, weil es dunkel ist.", "weil 句动词置尾",
      "Viele bleiben zu Hause. Es ist dunkel. (weil) → ___", instr="改写", size=22, gap=8)
fb.ex("B1", "单选", "A", "stiller als = 比……更安静",
      "„Stiller als sonst“ heißt... A. 比平时更安静 · B. 和平时一样 · C. 比平时更吵", size=22, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　例句", [("„Meiner Meinung nach braucht das Gedenken Stille.“　„Niemand weiß, ob die Einigung gelingt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "完成句子", "ob", "ob 引导间接疑问",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="填空", size=22, gap=8)
fc.ex("B2", "完成句子", "fraglich", "Es ist fraglich, ob ... = 是否还难说",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="填空", size=22, gap=8)
fc.ex("B2", "句型转换", "Ich finde, dass das Gedenken Stille braucht.", "dass 句动词置尾",
      "Ich finde: Das Gedenken braucht Stille. (dass) → ___", instr="改写", size=22, gap=8)
fc.ex("B2", "单选", "B", "礼貌表达观点",
      "„Das Gedenken braucht Stille“ höflich sagen: A. „Stille, sofort!“ · B. „Meiner Meinung nach braucht das Gedenken Stille.“ · C. „Die Politik macht alles falsch.“", size=22, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["18. November = 11 月 18 日",
      "der Buß- und Bettag = 忏悔祈祷日",
      "vor fast leeren Rängen = 几乎空场（欧足联处罚，仅儿童与 50 名德国球迷入场）",
      "Es wird gespielt. = 比赛将进行（被动）",
      "Meiner Meinung nach ... = 在我看来……",
      "Es ist fraglich, ob ... = 是否……还难说"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN　工具箱", 23, "sans", True, OLIVE)
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
label = "Ein Beispiel der Redaktion!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.5."
reader = "„Liebe Lucerna, im November bastle ich einen Adventskalender. Am 1. Dezember öffne ich das erste Türchen. Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.5."
chinese = "编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.5。请寄来您的习作，优秀者刊登于 VOL.5。"
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　读者来信", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　再学一词", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«der Adventskalender»（Seite 5）: ein Kalender mit 24 Türchen bis Weihnachten. 降临节日历。", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1560
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　本周金句", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "原文摘录，逐字引自本期文章　括号内为出处", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln.", "停赛两周后，拜仁周五晚对阵科隆。", "Seite 1 · A2"),
    ("Es geht ums Viertelfinale der Nations League.", "事关欧国联四分之一决赛。", "Seite 1 · A2"),
    ("Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag.", "只有在萨克森，忏悔祈祷日才是法定假日。", "Seite 2 · A2"),
    ("Die Märkte beginnen fast zwei Wochen früher.", "市场比将临期早近两周开市。", "Seite 3 · A2"),
    ("Hinter jedem Türchen wartet eine kleine Überraschung.", "每扇小门后都有一个小惊喜。", "Seite 5 · B1"),
    ("Der FC Bayern gewann in Mainz mit 2:1.", "拜仁在美因茨 2:1 获胜。", "Seite 4 · B1"),
    ("Die stille Woche ist der Übergang: vom November in den Advent.", "安静的一周是过渡：从十一月走向将临期。", "Seite 6 · B2"),
    ("Am Sonntag ist es still im Land.", "周日，全国一片安静。", "Seite 6 · B2"),
]
for i, (q, zh, tag) in enumerate(phrases):
    cx = COLX[i % 4]; cyy = py + 56 + (i // 4) * 190
    quote = "„" + q + "“"
    qlines = len(wrap(quote, "serif", True, 20.5, CW))
    p.para(cx, cyy + 21, quote, 20.5, "serif", True, INK, CW, 1.38)
    t_y = cyy + 21 + (qlines - 1) * 28.3 + 36
    tlines = len(wrap(zh, "sans", False, 19, CW))
    p.para(cx, t_y, zh, 19, "sans", False, GREY, CW, 1.35)
    p.text(cx, t_y + (tlines - 1) * 25.6 + 30, tag, 18, "sans", True, OLIVE)

# --- error clinic ---
ey = 2020
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "FEHLERKLINIK　纠错诊所", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "学习者最常犯的四个错　先自己改，再看答案", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Am Mittwoch die Kinder basteln einen Adventskalender.", "Am Mittwoch basteln die Kinder einen Adventskalender.", "动词第二位：主语不在句首时，动词仍居第二。"),
    ("Halb neun ist 9.30 Uhr.", "Halb neun ist 8.30 Uhr.", "halb neun = 八点半（neun 之前）。"),
    ("Die Mannschaft ist nach Berlin gereist am Montag.", "Die Mannschaft ist am Montag nach Berlin gereist.", "Perfekt 中 Partizip II 放句末。"),
    ("Er fragt, ob spielt die Nationalelf am Montag?", "Er fragt, ob die Nationalelf am Montag spielt.", "ob 从句动词放句末。"),
]
for i, (wrong, right, note) in enumerate(clinic):
    cx = COLX[i]
    p.text(cx, ey + 84, "FALSCH", 19, "sans", True, OLIVE)
    yy = p.para(cx, ey + 112, wrong, 20.5, "serif", False, INK, CW, 1.38)
    p.text(cx, yy + 28, "RICHTIG", 19, "sans", True, OLIVE)
    yy = p.para(cx, yy + 56, right, 20.5, "serif", True, INK, CW, 1.38)
    p.para(cx, yy + 26, note, 19, "sans", False, GREY, CW, 1.35)

# --- next issue teaser ---
ty = 2400
p.rect(MX, ty, RIGHT - MX, 130, fill=CLOTH)
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　下期预告 (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Sonntag, 29. November: Der erste Advent beginnt — Kerzen, Lieder und das erste Türchen. Dazu die Ergebnisse der Europapokale (24.–26. November), der 11. Spieltag und die Weihnachtsmärkte in vollem Gang. Und Ihre Briefe: Die besten echten Briefe erscheinen in VOL.5!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
