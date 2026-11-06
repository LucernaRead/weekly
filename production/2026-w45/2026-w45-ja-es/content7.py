# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ja-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · ことば (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ことば · Lengua", "Lucerna", "言語フォーカス · 三つのレベル、三つのテーマ · Tres niveles, tres temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 本と読書のことば", 24)
a.para("読書週間は、今週も続いています。10月27日（火よう日）に始まり、11月9日（月よう日）までです。今年のスローガンは『静かだけど、冒険中。』です。秋は『読書の秋』。本を読む季節です。", 21.5)
a.para("図書館では、読書週間のイベントがあります。本の紹介や読み聞かせです。静かな場所で、本の世界へ出かけましょう。", 21.5)
a.bridge("読書週間 Semana de la Lectura · 紹介 presentación · 読み聞かせ lectura en voz alta.")
a.ex("A2", "Completar", "27", "La Semana de la Lectura empezó el 27 de octubre (martes)",
     "読書週間は10月 ___ 日（火）から始まりました。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Completar", "9", "La Semana de la Lectura dura hasta el 9 de noviembre",
     "読書週間は11月 ___ 日までです。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Opción múltiple", "B", "El lema es 「静かだけど、冒険中。」",
     "今年のスローガンは？ A. 本の秋 · B. 静かだけど、冒険中。 · C. 紅葉の秋", size=20.5, gap=10)
a.ex("A2", "Opción múltiple", "A", "El evento de la biblioteca es la presentación de libros",
     "図書館のイベントは何ですか。 A. 本の紹介 · B. 野球の試合 · C. 鍋の料理", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 紅葉のことば", 24)
b.para("紅葉の季節のことばを覚えましょう。『見頃』は、紅葉がいちばん美しい時です。『紅葉狩り』は、紅葉を見に行くことです。『ライトアップ』は、夜に光で照らすことです。", 21.5)
b.para("『落葉』は、木から落ちた葉です。見頃が過ぎると、落葉の季節になります。北から南へ、紅葉の見頃は移っていきます。", 21.5)
b.bridge("見頃 mejor época para ver las hojas · 紅葉狩り salir a ver las hojas · 落葉 hojas caídas")
b.ex("B1", "Opción múltiple", "B", "見頃 = cuando las hojas se ven más bonitas",
     "『見頃』の意味は？ A. 葉が落ちる時 · B. 紅葉がいちばん美しい時 · C. 夜の光", size=20.5, gap=10)
b.ex("B1", "Completar", "紅葉狩り", "紅葉狩り = salir a ver las hojas",
     "紅葉を見に行くことを「___」と言います。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Opción múltiple", "C", "ライトアップ = iluminar de noche",
     "『ライトアップ』とは？ A. 葉が落ちること · B. 朝の光 · C. 夜に光で照らすこと", size=20.5, gap=10)
b.ex("B1", "Completar", "落葉", "落葉 = hojas caídas",
     "木から落ちた葉を「___」と言います。", instr="Completa", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 数字を読む", 24)
c.para("数字の読み方を練習しましょう。『1.5倍』は、去年の1倍に、半分（0.5倍）を足した数です。つまり、去年より50%多い、という意味です。", 21.5)
c.para("『73%』は、100人のうち73人、という意味です。4人のうち3人ぐらい、と考えると分かりやすいです。『1,300万食』は、1,300万回食べられた、という数です。", 21.5)
c.bridge("〜倍 veces · 〜% por ciento · 〜万食 decenas de millar de raciones.")
c.ex("B2", "Opción múltiple", "B", "1.5倍 = 50% más que el año pasado",
     "『1.5倍』の意味は？ A. 去年と同じ · B. 去年より50%多い · C. 去年の半分", size=20.5, gap=10)
c.ex("B2", "Opción múltiple", "A", "73% ≈ 3 de cada 4",
     "『73%』は、4人のうち何人ぐらいですか。 A. 3人ぐらい · B. 1人ぐらい · C. 4人全部", size=20.5, gap=10)
c.ex("B2", "Completar", "1.5", "Las cenas de olla son 1,5 veces las del año pasado",
     "鍋の食卓は、去年の ___ 倍になりました。（2面）", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Completar", "1,300", "サクサクdeコパン llegó a 13 millones de raciones",
     "『サクサクdeコパン』は ___ 万食を超えました。（2面）", instr="Completa", size=20.5, gap=10)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「昨日、友達と鍋を食べます」", "→ 『昨日』があるので過去形：『鍋を食べました』。", "Con 「昨日」, usa el pasado."),
    ("「私の趣味は鍋を食べるです」", "→ 『こと』が必要です：『鍋を食べることです』。", "Añade 「こと」 para sustantivar."),
    ("「ライトアップを三本見ました」", "→ 場所の数え方は「か所」です：『三か所見ました』。", "Cuenta los lugares con 「か所」."),
    ("「金沢に紅葉を見ます」", "→ 場所は『で』：『金沢で紅葉を見ます』。", "Usa 「で」 para el lugar de la acción."),
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
wt = "『ゆるく整える』 — ゆるく（無理をしないで）＋整える（体と心をよくする）。忙しい人でも、ゆっくり体を整える、という意味です。"
wcn = "Desglose: poner el cuerpo y la mente en orden con calma."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "今週のフレーム · Frase semanal", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「こんにちは。私は中学生です。読書週間には、図書館で本を2冊読みたいです。文化の日には、家族と金沢へ行きたいです。」— 読者の手紙の例"
ld_es = "Ejemplo de la redacción, no una carta real. Hasta la fecha límite no habían llegado cartas reales ni los mejores textos de la página 8; ambos aparecerán en el VOL.3. ¡Envíanos tu carta en japonés! Las seleccionadas saldrán en el VOL.3."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_es, "sans", False, 20, CW - 44)) * 29 + 26 + 16
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "読者の手紙 · Cartas de lectores", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, ld_es, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "今週のフレーズ · Frases de la semana (citas textuales de este número)", 27, "sans", True, OLIVE)
quotes = [
    ("「文化の日は、11月3日（火よう日）です。」", "El Día de la Cultura es el 3 de noviembre, martes.", "Página 1"),
    ("「ゆっくり、ゆるく整える日本の11月です。」", "Es un noviembre japonés lento y relajado, en orden.", "Página 1"),
    ("「『ゆる』は、無理をしない、ゆっくり、という意味です。」", "«Yuru» significa no forzarse, ir despacio.", "Página 2"),
    ("「鍋の材料が1か月早く並び始めました。」", "Los ingredientes para la olla aparecieron en las tiendas un mes antes.", "Página 2"),
    ("「伝統工芸と紅葉と光を、いっしょに楽しむことができます。」", "Se pueden disfrutar juntos la artesanía tradicional, las hojas de otoño y las luces.", "Página 3"),
    ("「ソフトバンクが2連勝でスタートしました。」", "SoftBank empezó con dos victorias seguidas.", "Página 4"),
    ("「ルールを守って、楽しいハロウィンにしましょう。」", "Respetemos las reglas y pasemos un Halloween divertido.", "Página 5"),
    ("「紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。」", "Quienes van a ver las hojas pueden seguir la mejor época de norte a sur.", "Página 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 132
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 132 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "来週 · Próximo número (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "読書週間が終わります（9日・月）。日本シリーズの最終結果も総括します。紅葉の見頃の続きと、読者の手紙と第8版の作文の優秀作も載せます。お楽しみに！", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-kotoba.svg")
print("P7 saved, exercises so far:", len(REG))
