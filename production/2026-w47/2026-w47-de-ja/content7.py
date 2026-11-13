# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE　言語", "Die Lucerna", "A2 → B2　Sätze der Woche & Fehlerklinik　今週の文と間違いクリニック")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "このページは言葉のページ：3つの短いレッスン、今週の文（今号からの引用）、間違いクリニック — そして読者の手紙。", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2　DATEN SAGEN", 24)
fa.para("So sagen Sie Daten: Am 18. November ist Buß- und Bettag. Am 29. November ist der erste Advent. Mit werden sprechen Sie über das Passiv: Um 20.30 Uhr wird in München gespielt.")
fa.box("BEISPIELE　例", [("„Am 18. November ist Buß- und Bettag.“　„Um 20.30 Uhr wird in München gespielt.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "穴埋め", "wird", "受動態：wird + 過去分詞",
      "Am Freitag ___ in München gespielt.", instr="入れよう", size=22, gap=8)
fa.ex("A2", "穴埋め", "werden", "複数形：werden",
      "Die Weihnachtsmärkte ___ am Montag geöffnet.", instr="入れよう", size=22, gap=8)
fa.ex("A2", "穴埋め", "wird", "werden + 不定詞：未来",
      "Der Adventskalender ___ am 1. Dezember beginnen.", instr="入れよう", size=22, gap=8)
fa.ex("A2", "選択問題", "A", "受動態",
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
fb.box("BEISPIELE　例", [("„Der November ist stiller als der Oktober.“　„Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "穴埋め", "stiller", "still → stiller (10月より静か)",
      "Im November ist es ___ (still) als im Oktober.", instr="入れよう", size=22, gap=8)
fb.ex("B1", "穴埋め", "weil", "weil：理由",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="入れよう", size=22, gap=8)
fb.ex("B1", "書き換え", "Viele bleiben zu Hause, weil es dunkel ist.", "weil：動詞は最後",
      "Viele bleiben zu Hause. Es ist dunkel. (weil) → ___", instr="書き換えよう", size=22, gap=8)
fb.ex("B1", "選択問題", "A", "stiller als = いつもより静か …",
      "„Stiller als sonst“ heißt... A. いつもより静か · B. いつもと同じ · C. いつもよりうるさい", size=22, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2　MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE　例", [("„Meiner Meinung nach braucht das Gedenken Stille.“　„Niemand weiß, ob die Einigung gelingt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "穴埋め", "ob", "ob：間接疑問文",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="入れよう", size=22, gap=8)
fc.ex("B2", "穴埋め", "fraglich", "fraglich：まだ疑わしい",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="入れよう", size=22, gap=8)
fc.ex("B2", "書き換え", "Ich finde, dass das Gedenken Stille braucht.", "dass：動詞は最後",
      "Ich finde: Das Gedenken braucht Stille. (dass) → ___", instr="書き換えよう", size=22, gap=8)
fc.ex("B2", "選択問題", "B", "丁寧な意見",
      "„Das Gedenken braucht Stille“ höflich sagen: A. „Stille, sofort!“ · B. „Meiner Meinung nach braucht das Gedenken Stille.“ · C. „Die Politik macht alles falsch.“", size=22, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["18. November = 11月18日",
      "der Buß- und Bettag = 悔い改めと祈り",
      "vor fast leeren Rängen = ほぼ空席の観客席の前で",
      "Es wird gespielt. = 試合が行われる（受動態）",
      "Meiner Meinung nach = 私の意見では",
      "Es ist fraglich, ob ... = まだ不明"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110  # fix1 D1: pad 90 -> 110 (= core-de value). Formula misses the +20.5/entry p.para offset (6 entries = +123), only partly offset by the 29.5 vs 29.11 line-height gap: clearance = pad - 90.8 for ja (8 lines), so 90 gave -0.8 (last baseline 754.8 vs box bottom 754.0, 'fraglich' descender ~4.7 below the box). 110 gives clearance +19.2 (bottom 774.0), same class as core +18.8. Boxes below shift +20 (LESERBRIEFE y 790, NOCH EIN WORT ends 1508.5, far before the 1548 Satze rule). Occlusion audit cannot see this defect class (text drawn after its own box, nothing covers it) -- the old "validated by occlusion 0 flags" claim was false. Edition-local fix only; shared helper untouched.
p.rect(ix, CTOP, CW, tbh, fill=BOX)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN　道具箱", 23, "sans", True, OLIVE)
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
label = "Ein Beispiel der Redaktion!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.5."
reader = "„Liebe Lucerna, im November bastle ich einen Adventskalender. Am 1. Dezember öffne ich das erste Türchen. Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.5."
chinese = "編集部の例：締め切りまでに本物の手紙は届かなかった。VOL.5 にあなたの文章を送ってください。"
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16
p.rect(ix, ry, CW, rh, fill="#f0eee5")
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE　読者の手紙", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, OLIVE, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT　もう一言", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«der Adventskalender»（5ページ）：クリスマスまでの24の小窓のカレンダー。", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1560
p.hline(MX, RIGHT, py - 12, OLIVE, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE　今週の文", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "今号からの引用　出典はかっこ内", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln.", "2週間の休み明け、バイエルンは金曜夜にケルンと対戦。", "Seite 1 · A2"),
    ("Es geht ums Viertelfinale der Nations League.", "ネーションズリーグ準々決勝の話。", "Seite 1 · A2"),
    ("Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag.", "Buß- und Bettag が祝日なのはザクセン州だけ。", "Seite 2 · A2"),
    ("Die Märkte beginnen fast zwei Wochen früher.", "市はほぼ2週間早く始まる。", "Seite 3 · A2"),
    ("Hinter jedem Türchen wartet eine kleine Überraschung.", "小窓の裏には小さな驚きが待つ。", "Seite 5 · B1"),
    ("Der FC Bayern gewann in Mainz mit 2:1.", "バイエルンはマインツで2-1勝利。", "Seite 4 · B1"),
    ("Die stille Woche ist der Übergang: vom November in den Advent.", "静かな一週間は移行期：11月から待降節へ。", "Seite 6 · B2"),
    ("Am Sonntag ist es still im Land.", "日曜日、国中が静かになる。", "Seite 6 · B2"),
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
p.text(MX, ey + 28, "FEHLERKLINIK　間違いクリニック", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "学習者によくある4つの間違い　まず直して、次に確認", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Am Mittwoch die Kinder basteln einen Adventskalender.", "Am Mittwoch basteln die Kinder einen Adventskalender.", "動詞は2番目：主語が最初でなくても、動詞は2番目。"),
    ("Halb neun ist 9.30 Uhr.", "Halb neun ist 8.30 Uhr.", "halb neun = 8時半（neun の前）。"),
    ("Die Mannschaft ist nach Berlin gereist am Montag.", "Die Mannschaft ist am Montag nach Berlin gereist.", "Perfekt：分詞は最後"),
    ("Er fragt, ob spielt die Nationalelf am Montag?", "Er fragt, ob die Nationalelf am Montag spielt.", "ob の文：動詞は最後"),
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
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE　次号（VOL.5）", 24, "sans", True, ONCLOTH)
p.para(MX + 26, ty + 82, "Sonntag, 29. November: Der erste Advent beginnt — Kerzen, Lieder und das erste Türchen. Dazu die Ergebnisse der Europapokale (24.–26. November), der 11. Spieltag und die Weihnachtsmärkte in vollem Gang. Und Ihre Briefe: Die besten echten Briefe erscheinen in VOL.5!", 21, "serif", False, "#cac8ba", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
