# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ja-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ことば (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ことば · Lengua", "Lucerna", "言語フォーカス · 三つのレベル、三つのテーマ · Tres niveles, tres temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 本と読書のことば", 24)
a.para("来週の火よう日（27日）から、『第80回読書週間』が始まります。11月9日までです。今年のスローガンは『静かだけど、冒険中。』です。秋は『読書の秋』。本を読む季節です。", 21.5)
a.para("町田市の図書館では、子どものための『本の福袋』が発表されました（20日）。中身が見えない、3冊の本のセットです。開ける時の楽しみも、読書の楽しみです。", 21.5)
a.expl("読書週間 semana de la lectura · 福袋 bolsa sorpresa (sin ver el contenido) · 中身 el contenido。")
a.ex("A2", "Completar", "27", "La Semana de la Lectura empieza el martes 27",
     "読書週間は ___ 日（火）から始まります。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Completar", "9", "Dura hasta el 9 de noviembre",
     "読書週間は11月 ___ 日までです。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Completar", "80", "Este año es la 80.ª edición",
     "今年は第 ___ 回の読書週間です。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Opción múltiple", "B", "La bolsa sorpresa lleva 3 libros",
     "『本の福袋』の中には、本が何冊ありますか。 A. 2冊 · B. 3冊 · C. 9冊", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 応援のことば", 24)
b.para("スポーツの応援では、こんな言葉を使います。『頑張れ！』『勝つぞ！』『負けるな！』。日本シリーズでは、横浜スタジアムで大きな声が聞こえます。", 21.5)
b.para("応援する時は、チームの名前を呼びます。『DeNA、頑張れ！』。勝った時は『勝った！』、負けた時は『次、頑張ろう』と言います。", 21.5)
b.expl("頑張れ ¡ánimo! · 勝つぞ ¡a ganar! · 負けるな ¡no te rindas!")
b.ex("B1", "Opción múltiple", "B", "頑張れ = ¡ánimo!",
     "応援の言葉はどれですか。 A. おはよう · B. 頑張れ · C. さようなら", size=20.5, gap=10)
b.ex("B1", "Completar", "勝つ", "勝つぞ = ¡a ganar!",
     "勝ちたい気持ちの言葉：『___ ぞ！』", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Opción múltiple", "B", "Al perder se dice «次、頑張ろう»",
     "負けた時に言う言葉は？ A. 勝った！ · B. 次、頑張ろう · C. お帰り", size=20.5, gap=10)
b.ex("B1", "Completar", "応援", "応援する = animar",
     "大きな声でチームを助けることを「___ する」と言います。", instr="Completa", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · パーセントを読む", 24)
c.para("数字の読み方を練習しましょう。『168%増えました』は、前の年の約2.7倍になった、という意味です。100%増えると2倍、50%増えると1.5倍です。", 21.5)
c.para("野球の勝率『.650』は、『6割5分』と読みます。割合の言葉は、ニュースによく出ます。『過去最多』『約〜』『〜以上』も、大切な言葉です。", 21.5)
c.expl("〜倍 veces · 割 décimas (1割 = 10 %) · 過去最多 récord histórico。")
c.ex("B2", "Opción múltiple", "B", "Subir un 100 % es duplicarse",
     "100%増えると、何倍になりますか。 A. 1倍 · B. 2倍 · C. 10倍", size=20.5, gap=10)
c.ex("B2", "Opción múltiple", "A", "El .650 se lee «6割5分»",
     "勝率『.650』の読み方は？ A. 6割5分 · B. 65割 · C. 6分5割", size=20.5, gap=10)
c.ex("B2", "Completar", "1.5", "Subir un 50 % es multiplicarse por 1,5",
     "50%増えると、___ 倍になります。", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Completar", "168", "Página 2: las reseñas de «餅» subieron un 168 %",
     "『餅』の口コミは、前の年より ___ %増えました。（2面）", instr="Completa", size=20.5, gap=10)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「本を三本買いました」", "→ 本の数え方は「冊」です：『本を三冊買いました』。", "Los libros se cuentan con «冊», no con «本»."),
    ("「昨日、図書館へ行きます」", "→ 『昨日』があるので過去形：『図書館へ行きました』。", "Con «昨日» (ayer) el verbo va en pasado."),
    ("「趣味は本を読むです」", "→ 『こと』が必要です：『本を読むことです』。", "Para sustantivar el verbo hace falta «こと»."),
    ("「図書館に本を借ります」", "→ 場所は『で』：『図書館で本を借ります』。", "El lugar de la acción lleva «で»."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "まちがい診療所 · Clínica de errores", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "『静かだけど、冒険中。』 — 静かだ＋けど（でも）＋冒険中（〜の最中）。本を読む人は、静かな場所で、大きな冒険をしています。"
wcn = "El eslogan, por partes: tranquilo, pero en plena aventura."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "今週のフレーム · Frase semanal", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「こんにちは。私は高校生です。読書週間には、図書館で借りた本を3冊読みたいです。静かだけど、冒険中！」— 読者の手紙の例"
lcn = "Carta de ejemplo de la redacción; no es una carta real. ¡En el VOL.2 publicaremos cartas de verdad y la mejor redacción de la página 8!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "読者の手紙 · Cartas de lectores", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "今週のフレーズ · Frases de la semana (citas textuales de este número)", 27, "sans", True, OLIVE)
quotes = [
    ("「この対決は2年ぶりです」", "Este duelo llega dos años después.", "Página 1"),
    ("「スポーツが熱い週末になります」", "Será un fin de semana de deporte intenso.", "Página 1"),
    ("「紅葉前線は北から南へ下りています」", "El frente de las hojas baja de norte a sur.", "Página 2"),
    ("「秋は、食の季節でもあります」", "El otoño también es la estación del buen comer.", "Página 2"),
    ("「歩きながら、日本の長い歴史を見ることができます」", "Se puede ver la larga historia de Japón caminando.", "Página 3"),
    ("「結果は来週の新聞でお知らせします」", "El resultado saldrá la semana que viene en este periódico.", "Página 4"),
    ("「テレビの前で笑った人も多い週末でした」", "Fue un fin de semana de risas ante el televisor.", "Página 5"),
    ("「障害のある人もない人も、同じ場所で同じ試合を見ます」", "Con o sin discapacidad, todos ven el mismo partido en el mismo lugar.", "Página 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 150
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 150 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "来週 · La semana que viene (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "読書週間が始まります（27日・火〜11月9日）。ハロウィンは31日（土）！日本シリーズの結果もお知らせします。あなたの手紙と、第8版の作文の優秀作も載せます。お楽しみに！", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-kotoba.svg")
print("P7 saved, exercises so far:", len(REG))
