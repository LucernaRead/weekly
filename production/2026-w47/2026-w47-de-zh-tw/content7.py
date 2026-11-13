# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　語言", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　本週佳句與錯誤診所")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "這一頁全是語言：三堂短課、本週佳句（全部引自本期原文）、錯誤診所 — 以及讀者來信。", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　DATEN SAGEN", 24)
fa.para("So sagen Sie Daten: Am 18. November ist Buß- und Bettag. Am 29. November ist der erste Advent. Mit werden sprechen Sie über das Passiv: Um 20.30 Uhr wird in München gespielt.")
fa.box("BEISPIELE　例句", [("„Am 18. November ist Buß- und Bettag.“　„Um 20.30 Uhr wird in München gespielt.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "填空", "wird", "被動式：wird + 過去分詞",
      "Am Freitag ___ in München gespielt.", instr="填入", size=22, gap=8)
fa.ex("A2", "填空", "werden", "複數：werden",
      "Die Weihnachtsmärkte ___ am Montag geöffnet.", instr="填入", size=22, gap=8)
fa.ex("A2", "填空", "wird", "werden + 不定詞：將來式",
      "Der Adventskalender ___ am 1. Dezember beginnen.", instr="填入", size=22, gap=8)
fa.ex("A2", "選擇題", "A", "被動式",
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
fb.ex("B1", "填空", "stiller", "still → stiller (比十月安靜)",
      "Im November ist es ___ (still) als im Oktober.", instr="填入", size=22, gap=8)
fb.ex("B1", "填空", "weil", "weil：原因",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="填入", size=22, gap=8)
fb.ex("B1", "改寫", "Viele bleiben zu Hause, weil es dunkel ist.", "weil：動詞在最後",
      "Viele bleiben zu Hause. Es ist dunkel. (weil) → ___", instr="改寫", size=22, gap=8)
fb.ex("B1", "選擇題", "A", "stiller als = 比……安靜",
      "„Stiller als sonst“ heißt... A. 比平常安靜 · B. 和平常一樣 · C. 比平常吵", size=22, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　例句", [("„Meiner Meinung nach braucht das Gedenken Stille.“　„Niemand weiß, ob die Einigung gelingt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "填空", "ob", "ob：間接問句",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="填入", size=22, gap=8)
fc.ex("B2", "填空", "fraglich", "fraglich：是否……仍有疑問",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="填入", size=22, gap=8)
fc.ex("B2", "改寫", "Ich finde, dass das Gedenken Stille braucht.", "dass：動詞在最後",
      "Ich finde: Das Gedenken braucht Stille. (dass) → ___", instr="改寫", size=22, gap=8)
fc.ex("B2", "選擇題", "B", "禮貌表達意見",
      "„Das Gedenken braucht Stille“ höflich sagen: A. „Stille, sofort!“ · B. „Meiner Meinung nach braucht das Gedenken Stille.“ · C. „Die Politik macht alles falsch.“", size=22, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["18. November = 11 月 18 日",
      "der Buß- und Bettag = 懺悔祈禱日",
      "vor fast leeren Rängen = 在幾乎空蕩的看台前",
      "Es wird gespielt. = 比賽將舉行（被動式）",
      "Meiner Meinung nach = 依我看",
      "Es ist fraglich, ob ... = 是否……尚未確定"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110  # zh-tw fix1: pad 110 restores core-de value; formula counts n*29.5+6 but real ink advance is 20.5+n*29.11+6 per entry (para first baseline at y+20.5, lines at 20.5*1.42=29.11), so pad 90 under-counted 6*20.5=123 minus 8*0.39 line overestimate -> clearance pad-90.8 (was -0.8, last baseline 754.8 vs bottom 754.0); pad 110 -> +19.2. The old "90 validated by en/fr occlusion 0 flags" claim was void: the audit cannot see text spilling past its own box bottom.
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
chinese = "編輯範例：截稿前尚未收到真正的來信。請將你的習作寄來 VOL.5。"
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　讀者來信", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　再說一句", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«der Adventskalender»（第 5 頁）：聖誕節前 24 個小門的日曆。", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1560
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　本週佳句", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "引自本期原文　出處見括號", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln.", "休整兩週後，拜仁週五晚對科隆。", "Seite 1 · A2"),
    ("Es geht ums Viertelfinale der Nations League.", "這是關於歐國聯八強賽。", "Seite 1 · A2"),
    ("Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag.", "只有薩克森把 Buß- und Bettag 列為假日。", "Seite 2 · A2"),
    ("Die Märkte beginnen fast zwei Wochen früher.", "市集提早近兩週開市。", "Seite 3 · A2"),
    ("Hinter jedem Türchen wartet eine kleine Überraschung.", "每扇小門後都有一個小驚喜。", "Seite 5 · B1"),
    ("Der FC Bayern gewann in Mainz mit 2:1.", "拜仁在美因茲 2-1 獲勝。", "Seite 4 · B1"),
    ("Die stille Woche ist der Übergang: vom November in den Advent.", "寧靜的一週是過渡：從十一月進入將臨期。", "Seite 6 · B2"),
    ("Am Sonntag ist es still im Land.", "週日，全國一片安靜。", "Seite 6 · B2"),
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
p.text(MX, ey + 28, "FEHLERKLINIK　錯誤診所", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "學習者最常見的四個錯誤　先改正，再核對", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Am Mittwoch die Kinder basteln einen Adventskalender.", "Am Mittwoch basteln die Kinder einen Adventskalender.", "動詞第二：即使主語不在首位，動詞仍在第二位。"),
    ("Halb neun ist 9.30 Uhr.", "Halb neun ist 8.30 Uhr.", "halb neun = 八點半（neun 之前）。"),
    ("Die Mannschaft ist nach Berlin gereist am Montag.", "Die Mannschaft ist am Montag nach Berlin gereist.", "Perfekt：分詞在最後"),
    ("Er fragt, ob spielt die Nationalelf am Montag?", "Er fragt, ob die Nationalelf am Montag spielt.", "ob 子句：動詞在最後"),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　下一期（VOL.5）", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Sonntag, 29. November: Der erste Advent beginnt — Kerzen, Lieder und das erste Türchen. Dazu die Ergebnisse der Europapokale (24.–26. November), der 11. Spieltag und die Weihnachtsmärkte in vollem Gang. Und Ihre Briefe: Die besten echten Briefe erscheinen in VOL.5!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
