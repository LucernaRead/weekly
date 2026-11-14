# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　ことば", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　今週の文と間違いクリニック")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "このページはことば特集です：小さなレッスン3つ、今号の文（すべて今号の記事から）、間違いクリニック、そして読者の手紙。", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　DIE UHRZEIT & «WERDEN»", 24)
fa.para("So sagen Sie die Zeit: Es ist halb drei (2.30 Uhr), Viertel vor acht (7.45 Uhr). Mit werden sprechen Sie über die Zukunft: Morgen wird es kalt. Am Sonntag wird die Uhr umgestellt.")
fa.box("BEISPIELE　例文", [("„Es ist Viertel vor acht.“　„Morgen wird es sonnig.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "文の完成", "vor", "7:45 = 8時15分前",
      "Es ist Viertel ___ acht. (7.45 Uhr)", instr="空所補充", size=20, gap=8)
fa.ex("A2", "文の完成", "wird", "wird + Partizip II (受動)",
      "Am Sonntag ___ die Uhr zurückgestellt. (werden)", instr="空所補充", size=20, gap=8)
fa.ex("A2", "文の完成", "wird", "werden + 不定形で未来",
      "Morgen ___ es in Berlin regnen. (werden)", instr="空所補充", size=20, gap=8)
fa.ex("A2", "選択問題", "A", "halb vier = 3:30",
      "„Halb vier“ ist... A. 3.30 Uhr · B. 4.30 Uhr · C. 16.00 Uhr", size=20, gap=8)
fa.end_report()
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1　VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Die Nacht ist länger als sonst. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es regnet — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE　例文", [("„Der Zug ist schneller als das Auto.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "文の完成", "länger", "lang → länger (25時間の夜)",
      "Die Nacht zum Sonntag ist ___ (lang) als andere Nächte.", instr="空所補充", size=20, gap=8)
fb.ex("B1", "文の完成", "weil", "weil は理由を導く",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="空所補充", size=20, gap=8)
fb.ex("B1", "文の書き換え", "Viele reisen, weil Herbstferien sind.", "weil 文では動詞は文末",
      "Viele reisen. Es sind Herbstferien. (weil) → ___", instr="書きかえ", size=20, gap=8)
fb.ex("B1", "選択問題", "A", "比較級 kürzer",
      "Die Tage werden im Herbst... A. kürzer · B. kurz · C. der kürzeste", size=20, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　例文", [("„Meiner Meinung nach bleibt die Umstellung.“　„Niemand weiß, ob sie nächstes Jahr noch gilt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "文の完成", "ob", "ob が間接疑問を導く",
      "Ich weiß nicht, ___ die Umstellung bleibt.", instr="空所補充", size=20, gap=8)
fc.ex("B2", "文の完成", "fraglich", "Es ist fraglich, ob ... = ～かどうか分からない",
      "Es ist ___ , ob die Mitgliedstaaten sich einigen.", instr="空所補充", size=20, gap=8)
fc.ex("B2", "文の書き換え", "Ich finde, dass die Sommerzeit gut ist.", "dass 文では動詞は文末",
      "Ich finde: Die Sommerzeit ist gut. (dass) → ___", instr="書きかえ", size=20, gap=8)
fc.ex("B2", "選択問題", "B", "Meiner Meinung nach = 丁寧な意見の言い方",
      "Höflich eine Meinung sagen: A. „Das ist Quatsch!“ · B. „Meiner Meinung nach ist das zu kompliziert.“ · C. „Du liegst falsch.“", size=20, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word ---
ix = COLX[3]
tb = ["Es ist halb drei. = 2.30 Uhr（3.30ではありません）",
      "eine Stunde länger schlafen = 1時間長く寝る",
      "Von O bis O = 10月から復活祭（タイヤ）",
      "Meiner Meinung nach ... = 私の意見では……",
      "Ich finde, dass ... = 私は～と思います（動詞は文末）",
      "Es ist fraglich, ob ... = ～かどうか不明"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN　道具箱", 21, "sans", True, OLIVE)  # D5 fix run2
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
reader = "„Liebe Lucerna, ich stelle meine Uhren schon am Samstagabend um. Dann ist der Sonntag ganz ruhig. Viele Grüße — ein Leser“"
rh = 62 + 30 + len(wrap("Ein Beispiel der Redaktion — VOL.2 druckt Ihre Briefe!", "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap("Schreiben Sie uns Ihre Sätze von Seite 2, 3 und 5 — und Ihre Texte zur Schreibaufgabe auf Seite 8!", "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap("編集部の例です。次号（VOL.2）で本物の読者の手紙と作文選を載せます。", "sans", False, 19.5, CW - 44)) * 28 + 40
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　読者の手紙", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, "Ein Beispiel der Redaktion — VOL.2 druckt Ihre Briefe!", 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, "Schreiben Sie uns Ihre Sätze von Seite 2, 3 und 5 — und Ihre Texte zur Schreibaufgabe auf Seite 8!", 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, "編集部の例です。次号（VOL.2）で本物の読者の手紙と作文選を載せます。", 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　もう一語", 21, "sans", True, OLIVE)  # D5 fix run2
p.para(ix + 22, wy3 + 78, "«der Klassiker»（Seite 4）: das größte Spiel der Saison — Bayern gegen Dortmund. 伝統の一戦。", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1520
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　今週の文", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "原文の抜粋、今号の記事からそのまま引用　括弧内は出典", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Die Nacht hat dann 25 Stunden, und alle dürfen eine Stunde länger schlafen.", "その夜は25時間あり、みんな1時間長く眠れます。", "Seite 1 · A2"),
    ("Im Frühjahr stellt man die Gartenmöbel VOR das Haus — im Herbst stellt man sie ZURÜCK ins Haus.", "春は庭の家具を家の前に、秋は家の中へ戻します。（覚え方）", "Seite 2 · A2"),
    ("Wer vom 26. bis 29. Oktober einen geschnitzten Kürbis abgibt, bekommt für den 31. Oktober ein Freiticket für ein Kind.", "10月26–29日に彫ったかぼちゃを持って行くと、10月31日の子ども無料券がもらえます。", "Seite 3 · B1"),
    ("Borussia Dortmund gewann am Dienstagabend 2:1 bei Sabah FK in Baku.", "ドルトムントは火曜の夜、バクーでサバフに2:1で勝ちました。", "Seite 4 · B1"),
    ("Man wählt ein Buch, ohne es zu kennen.", "本を選ぶのに、まだその本を知らない。（図書館の「ブラインドデート」）", "Seite 5 · B1"),
    ("84 Prozent von ihnen wollten die Umstellung abschaffen.", "そのうち84%が時刻の切替制度の廃止を望んでいます。", "Seite 6 · B2"),
    ("Die Stunde von 2.00 bis 3.00 Uhr gibt es in dieser Nacht zweimal.", "この夜、2時から3時の1時間が2回現れます。", "Seite 2 · A2"),
    ("Aber die Regierungen der Mitgliedstaaten wurden sich nicht einig — und so blieb alles, wie es ist.", "しかし加盟国の政府は合意できず——すべて今まで通りです。", "Seite 6 · B2"),
]
for i, (q, zh, tag) in enumerate(phrases):
    cx = COLX[i % 4]; cyy = py + 56 + (i // 4) * 204
    quote = "„" + q + "“"
    qlines = len(wrap(quote, "serif", True, 20.5, CW))
    p.para(cx, cyy + 21, quote, 20.5, "serif", True, INK, CW, 1.38)
    t_y = cyy + 21 + (qlines - 1) * 28.3 + 36
    tlines = len(wrap(zh, "sans", False, 19, CW))
    p.para(cx, t_y, zh, 19, "sans", False, GREY, CW, 1.35)
    p.text(cx, t_y + (tlines - 1) * 25.6 + 30, tag, 18, "sans", True, OLIVE)

# --- error clinic ---
ey = 1980
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "FEHLERKLINIK　間違いクリニック", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "学習者がよくする四つの間違い　まず自分で直してから答えを見よう", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Ich habe 25 Jahre alt.", "Ich bin 25 Jahre alt.", "年齢は sein を使い、haben は使いません！"),
    ("Halb drei ist 3.30 Uhr.", "Halb drei ist 2.30 Uhr.", "halb drei = 2時半（drei の前）。"),
    ("Berlin ist größer wie Hamburg.", "Berlin ist größer als Hamburg.", "比較級の後は als を使い、wie は使いません。"),
    ("Ich bleibe zu Hause, weil ich lese ein Buch.", "Ich bleibe zu Hause, weil ich ein Buch lese.", "weil 文では動詞を文末に置きます。"),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　次号予告 (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Samstag, 31. Oktober: Halloween UND Reformationstag UND der Klassiker in Dortmund · Sonntag, 1. November: Allerheiligen · Baden-Württemberg startet in die Herbstferien · dazu Ihre Leserbriefe und die besten Texte von Seite 8!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
