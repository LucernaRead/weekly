# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE FOCUS =================
CURPAGE[0] = 7
p = BSPage4()
p.band("SPRACHE · 言語", "Die Lucerna", "A2 → B2 · Sätze der Woche & Fehlerklinik · 今週の文と間違いクリニック")

p.para(MX, 226, "Diese Seite gehört der Sprache: drei kleine Lektionen, die Sätze der Woche aus dieser Ausgabe, unsere Fehlerklinik — und Ihre Briefe.", 23, "serif", False, INK, RIGHT - MX, 1.4)
p.para(MX, 262, "このページは言語が専門です。三つの小さなレッスン、今週の文（すべて今号の記事原文からの引用）、間違いクリニック、読者の手紙があります。", 20, "sans", False, GREY, RIGHT - MX, 1.4)

CTOP, CBOT = 330, 1480
# --- col A2 ---
fa = Flow(p, [(COLX[0], CW)], CTOP, CBOT, tag="P7-A2")
fa.head("A2 · DIE ZAHLEN & «WERDEN»", 24)
fa.para("So sagen Sie die Zahlen: 14,04 Cent pro Liter, rund 8,35 Euro für 50 Liter. Mit werden sprechen Sie über die Zukunft und das Passiv: Am Freitag wird gespielt. Der Tankrabatt wird bis Dezember gelten.")
fa.box("BEISPIELE · 例文", [("„Am Freitag wird gespielt.“ · „Der Tankrabatt gilt bis Dezember.“", "serif", False, INK, 21, 1.4)])
fa.ex("A2", "文完成", "wird", "受動態：wird + Partizip II",
      "Am Freitag ___ gespielt: Hamburg gegen Gladbach.", instr="空所補充", size=20, gap=8)
fa.ex("A2", "文完成", "werden", "複数：werden",
      "Am Sonntag ___ drei Spiele gespielt.", instr="空所補充", size=20, gap=8)
fa.ex("A2", "文完成", "wird", "werden + 不定詞で未来を表す",
      "Der Tankrabatt ___ bis Dezember gelten.", instr="空所補充", size=20, gap=8)
fa.ex("A2", "選択肢", "A", "受動態",
      "„Es wird gespielt“ ist... A. Passiv · B. Perfekt · C. Imperativ", size=20, gap=8)
fa.end_report()
# --- col B1 ---
fb = Flow(p, [(COLX[1], CW)], CTOP, CBOT, tag="P7-B1")
fb.head("B1 · VERGLEICHE & GRÜNDE", 24)
fb.para("Vergleichen geht mit dem Komparativ: Der Abend ist länger als sonst. Gründe geben Sie mit weil: Ich bleibe zu Hause, weil es kalt ist — das Verb steht am Ende des Satzes.")
fb.box("BEISPIELE · 例文", [("„Das Spiel ist später als sonst.“ · „Ich lese, weil das Buch spannend ist.“", "serif", False, INK, 21, 1.4)])
fb.ex("B1", "文完成", "später", "spät → später（19:30が最も遅い）",
      "Das Spiel Hoffenheim–Schalke ist ___ (spät) als die anderen Sonntagsspiele.", instr="空所補充", size=20, gap=8)
fb.ex("B1", "文完成", "weil", "weil が理由を導く",
      "Es wird früher dunkel, ___ die Tage kürzer werden.", instr="空所補充", size=20, gap=8)
fb.ex("B1", "文の書き換え", "Viele bleiben zu Hause, weil es kalt ist.", "weil の文では動詞が文末へ",
      "Viele bleiben zu Hause. Es ist kalt. (weil) → ___", instr="書きかえ", size=20, gap=8)
fb.ex("B1", "選択肢", "A", "länger als = ……より長い",
      "„Länger als sonst“ heißt... A. いつもより長い · B. いつもと同じ · C. いつもより短い", size=20, gap=8)
fb.end_report()
# --- col B2 ---
fc = Flow(p, [(COLX[2], CW)], CTOP, CBOT, tag="P7-B2")
fc.head("B2 · MEINUNG SAGEN", 24)
fc.para("Eine Meinung sagen Sie höflich so: Meiner Meinung nach ... Oder: Ich finde, dass ... — bei dass steht das Verb am Ende! Nicht sicher? Dann: Es ist fraglich, ob ...")
fc.box("BEISPIELE · 例文", [("„Meiner Meinung nach braucht die Pflege mehr Geld.“ · „Niemand weiß, ob die Steuer sinkt.“", "serif", False, INK, 21, 1.4)])
fc.ex("B2", "文完成", "ob", "ob が間接疑問を導く",
      "Ich weiß nicht, ___ die Stromsteuer sinkt.", instr="空所補充", size=20, gap=8)
fc.ex("B2", "文完成", "fraglich", "Es ist fraglich, ob ... = ……か疑わしい",
      "Es ist ___ , ob sich Union und SPD einigen.", instr="空所補充", size=20, gap=8)
fc.ex("B2", "文の書き換え", "Ich finde, dass die Pflege mehr Hilfe braucht.", "dass の文では動詞が文末へ",
      "Ich finde: Die Pflege braucht mehr Hilfe. (dass) → ___", instr="書きかえ", size=20, gap=8)
fc.ex("B2", "選択肢", "B", "丁寧な意見の言い方",
      "„Die Pflege braucht mehr Geld“ höflich sagen: A. „Mehr Geld, sofort!“ · B. „Meiner Meinung nach braucht die Pflege mehr Geld.“ · C. „Die Politik macht alles falsch.“", size=20, gap=8)
fc.end_report()

# --- col 3 rail: toolbox + readers + word (post-patch geometry: gap 6, pad 110) ---
ix = COLX[3]
tb = ["14,04 Cent = 1リットル14.04セント",
      "rund 8,35 Euro = 約8.35ユーロ節約",
      "Es wird gespielt. = 試合が行われる",
      "Meiner Meinung nach = 私の意見では",
      "Ich finde, dass = 私は……と思う",
      "Es ist fraglich, ob = ……か疑わしい"]
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110
p.rect(ix, CTOP, CW, tbh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = CTOP + 16
p.text(ix + 22, yy3 + 26, "DER WERKZEUGKASTEN · 道具箱", 23, "sans", True, OLIVE)
yy3 += 52
for t in tb:
    yy3 = p.para(ix + 22, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 44, 1.42) + 6
ry = CTOP + tbh + 16
label = "Ein Beispiel der Redaktion!"
defer = "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3."
reader = "„Liebe Lucerna, am Dienstag schaue ich Bayern bei Atlético. Die Fußballwoche ist toll! Viele Grüße — die Redaktion“"
invite = "Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.3."
note_ja = "編集部の例です。本物のお便りも第8ページの最優秀作文も届きませんでした。"
invite_ja = "お便りと第8ページの作文を送ってください！優秀作はVOL.3に掲載します。"
rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \
    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \
    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \
    + len(wrap(note_ja, "sans", False, 19.5, CW - 44)) * 28 + 8 \
    + len(wrap(invite_ja, "serif", False, 20.5, CW - 44)) * 29.5 + 40 + 32
# NOTE (JA fan-out): 6 paras in the readers box (label, defer, reader,
# invite, note_ja, invite_ja); trailing +32 follows the DE x EN final
# form (core fix1 +16, plus +16 for the added sixth para).
p.rect(ix, ry, CW, rh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ry + 16
p.text(ix + 22, yy3 + 26, "LESERBRIEFE · 読者の手紙", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 20, label, 20, "sans", True, BRICK, CW - 44, 1.42)
yy3 = p.para(ix + 22, yy3 + 20.5, defer, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 21, reader, 21, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 20.5, invite, 20.5, "serif", False, INK, CW - 44, 1.42) + 8
yy3 = p.para(ix + 22, yy3 + 19.5, note_ja, 19.5, "sans", False, GREY, CW - 44, 1.42) + 8
p.para(ix + 22, yy3 + 20.5, invite_ja, 20.5, "serif", False, INK, CW - 44, 1.42)
wy3 = ry + rh + 16
p.rect(ix, wy3, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, wy3 + 40, "NOCH EIN WORT · もう一語", 22, "sans", True, OLIVE)
p.para(ix + 22, wy3 + 78, "«der Tankrabatt»（Seite 2）: die gesenkte Steuer auf Benzin und Diesel. 燃料割引。", 20.5, "serif", False, INK, CW - 44, 1.42)
print("P7 col3 ends", wy3 + 150)

# --- phrases of the week (verbatim from this issue) ---
py = 1520
p.hline(MX, RIGHT, py - 12, GOLD, 2)
p.text(MX, py + 28, "SÄTZE DER WOCHE · 今週の文", 28, "sans", True, OLIVE)
p.text(RIGHT, py + 28, "今号の記事からの一字一句の引用 · かっこ内は出典", 20, "sans", False, GREY, anchor="end")
phrases = [
    ("Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.", "四夜連続のサッカー、そして週末いっぱいのリーグ戦。", "Seite 4 · B1"),
    ("Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.", "ガソリンとディーゼルのエネルギー税が1リットルあたり14.04セント下がります。", "Seite 2 · A2"),
    ("Wer 50 Liter tankt, spart rund 8,35 Euro.", "50リットル給油すると、約8.35ユーロ節約できます。", "Seite 2 · A2"),
    ("Die Schule hat nach den Herbstferien wieder begonnen.", "秋休みの後、学校がまた始まりました。", "Seite 5 · B1"),
    ("Die Tage sind kurz, die Abende lang.", "日は短く、夜は長い。", "Seite 3 · A2"),
    ("Zwei schwere Auswärtsspiele für die deutschen Teams.", "ドイツのチームの二つの厳しいアウェー戦。", "Seite 4 · B1"),
    ("Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.", "ドイツ経済はゆっくりと停滞から抜け出しつつありますが、回復はまだ自立していません。", "Seite 6 · B2"),
    ("Es geht langsam aufwärts — aber von allein geht es nicht.", "ゆっくりと上向いている——しかし、ひとりでに良くなるわけではありません。", "Seite 6 · B2"),
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
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "FEHLERKLINIK · 間違いクリニック", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "学習者が最もよくする四つの間違い · まず自分で直してから答えを見よう", 20, "sans", False, GREY, anchor="end")
clinic = [
    ("Die Schule beginnt wieder in Baden-Württemberg am Montag.", "In Baden-Württemberg beginnt die Schule am Montag wieder.", "動詞第二位：主語が文頭になくても、動詞は二番目に置きます。"),
    ("Halb acht ist 8.30 Uhr.", "Halb acht ist 7.30 Uhr.", "halb acht = 7時半（acht の30分前）。"),
    ("Die Preise sind gefallen um 14 Cent.", "Die Preise sind um 14 Cent gefallen.", "Perfekt では Partizip II を文末に置きます。"),
    ("Er fragt, ob kommt der Bus?", "Er fragt, ob der Bus kommt.", "ob の従属文では動詞を文末に置きます。"),
]
for i, (wrong, right, note) in enumerate(clinic):
    cx = COLX[i]
    p.text(cx, ey + 84, "FALSCH", 19, "sans", True, BRICK)
    yy = p.para(cx, ey + 112, wrong, 20.5, "serif", False, INK, CW, 1.38)
    p.text(cx, yy + 28, "RICHTIG", 19, "sans", True, OLIVE)
    yy = p.para(cx, yy + 56, right, 20.5, "serif", True, INK, CW, 1.38)
    p.para(cx, yy + 26, note, 19, "sans", False, GREY, CW, 1.35)

# --- next issue teaser ---
ty = 2400
p.rect(MX, ty, RIGHT - MX, 130, fill=DARK)
p.text(MX + 26, ty + 46, "IN DER NÄCHSTEN AUSGABE · 次号予告 (VOL.3)", 24, "sans", True, "#f3edda")
p.para(MX + 26, ty + 82, "Sonntag, 15. November: Volkstrauertag und NFL in München — American Football in der Allianz Arena · dazu St. Martin am 11. November, die Europapokal-Rückspiele und Ihre Briefe: Schreiben Sie uns! Die besten echten Briefe erscheinen in VOL.3!", 21, "serif", False, "#e8dfc8", RIGHT - MX - 52, 1.4)
p.foot(7)
p.save(f"{OUT}/p7-sprache.svg")
print("P7 saved, exercises so far:", len(REG))
