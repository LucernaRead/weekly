# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LENGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LENGUA　ことば", "La Lucerna", "ことば特集　Tres niveles, tres herramientas　三つのレベル、三つの道具")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　DECIR LA HORA Y EL PRESENTE", 24)
a.para("Para decir la hora: «Es la una», pero «Son las dos, las tres…». «Y media» es +30 minutos (2:30); «menos cuarto», −15 (2:45).", 21.5)
a.para("Y ojo con dormir: el presente cambia la vocal — duermo, duermes, duerme… pero dormimos, dormís. Despertarse es reflexivo: me despierto, se despierta.", 21.5)
a.expl("時刻で「1時」だけ es を使う。dormir は不規則活用、despertarse は再帰動詞。")
a.ex("A2", "文の完成", "Son", "10時は Son（la una だけ Es）",
     "___ las diez de la noche. Empieza la película.", instr="空所補充", size=20.5, gap=10)
a.ex("A2", "文の完成", "duerme", "dormir: él → duerme（o→ue）",
     "Mi hermano ___ (dormir) hasta las once el domingo.", instr="空所補充", size=20.5, gap=10)
a.ex("A2", "文の完成", "se despierta", "despertarse: ella → se despierta",
     "Ella ___ (despertarse) a las ocho.", instr="空所補充", size=20.5, gap=10)
a.ex("A2", "選択問題", "B", "y media = 30分",
     "«Son las dos y media» son las... A. 2:15 · B. 2:30 · C. 2:45", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　COMPARATIVOS Y PASADO", 24)
b.para("Para comparar: más / menos + adjetivo + que. Dos irregulares para recordar: bueno → mejor, malo → peor.", 21.5)
b.para("Para contar el martes de Champions usamos el pretérito indefinido: ganó, marcó, perdió, cortó. Es el tiempo de los resultados y de las crónicas.", 21.5)
b.expl("比較級 más…que。bueno→mejor、malo→peor は不規則。試合結果は過去形 indefinido で言う。")
b.ex("B1", "文の完成", "más importante", "más + 形容詞（比較）",
     "El Clásico es ___ que un partido normal. (importante)", instr="空所補充", size=20.5, gap=10)
b.ex("B1", "文の完成", "peor", "malo の比較級は peor",
     "Fue la ___ (malo) noche del Barça esta temporada.", instr="空所補充", size=20.5, gap=10)
b.ex("B1", "文の完成", "marcó", "marcar の indefinido：marcó",
     "Doué ___ (marcar) el primer gol en París.", instr="空所補充", size=20.5, gap=10)
b.ex("B1", "選択問題", "B", "ビジャレアルが4–3で敗れる",
     "El Villarreal en Liverpool... A. ganó 4–3 · B. perdió 4–3 · C. empató 0–0", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　CREO QUE… / NO CREO QUE…", 24)
c.para("Con «creo que» afirmamos: va el indicativo — «Creo que el Clásico es el domingo». Con «no creo que», con dudas y con «es importante que» va el subjuntivo: tenga (tener), sea (ser), llueva (llover).", 21.5)
c.para("Es la gramática de la página 6: opinar sobre encuestas sin afirmar más de lo que sabemos.", 21.5)
c.expl("creo que の後は直説法。no creo que、es importante que の後は接続法（tenga/sea/llueva）。")
c.ex("B2", "文の完成", "es", "creo que + 直説法：es",
     "Creo que el Clásico ___ (ser) el domingo.", instr="空所補充", size=20.5, gap=10)
c.ex("B2", "文の完成", "sea", "no creo que + 接続法：sea",
     "No creo que el gráfico ___ (ser) completo sin la fuente.", instr="空所補充", size=20.5, gap=10)
c.ex("B2", "文の完成", "tenga", "es importante que + 接続法：tenga",
     "Es importante que cada encuesta ___ (tener) su fecha.", instr="空所補充", size=20.5, gap=10)
c.ex("B2", "選択問題", "B", "es posible que + 接続法 llueva",
     "«Es posible que el domingo...» A. llueve · B. llueva · C. llover", size=20.5, gap=10)
c.end_report()

# ---- col 3: errores típicos + palabra + lectores ----
bx = COLX[3]
errs = [
    ("«Es las tres.»", "→ «Son las tres.» Solo «la una» usa es; las demás horas usan son.", "「1時」だけ es、ほかの時刻は son。"),
    ("«Hoy soy muy aburrido.»", "→ «Hoy estoy muy aburrido.» Estado de hoy: estar. Ser aburrido = ser una persona aburrida.", "今日の状態には estar。ser は（人が）退屈という意味。"),
    ("«Me gusta los libros.»", "→ «Me gustan los libros.» Gustar cambia con la cosa: gusta / gustan.", "gustar は対象で決まる：単数は gusta、複数は gustan。"),
    ("«La gente son felices.»", "→ «La gente es feliz.» Gente es singular, como un solo grupo.", "gente は単数の集合名詞で、動詞も単数。"),
]
# 盒高 = 绘制循环精确模拟（2026-10-21 回补：原平均行高公式系统性低估 206.5，第四条被下方盒覆盖；修法与 ES×EN 版一致）
_sim = 216 + 44
for _w, _r, _n in errs:
    _sim += 17 + len(wrap(_w, "serif", True, 21.5, CW - 44)) * 21.5 * 1.36 \
          + 17 + len(wrap(_r, "serif", False, 20.5, CW - 44)) * 20.5 * 1.36 \
          + 16 + len(wrap(_n, "sans", False, 19.5, CW - 44)) * 19.5 * 1.36 + 4
eh = _sim - 200 + 12
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS　よくある間違い", 23, "sans", True, OLIVE)
yy3 += 44
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 17, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 17, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 16, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 4
wy = 200 + eh + 16
wt = "« empatar » es terminar igual: en un partido, no ganar ni perder. Esta semana la palabra vive dos veces: el Atlético empató en Stuttgart — ¡y Alonso y Sainz llegan empatados a Austin, con los mismos puntos!"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("empatar = 引き分け。今週二度登場：アトレティコがシュトゥットガルトと引き分け、アロンソとサインツが同点。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PALABRA　今週の単語", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "empatar = 引き分け。今週二度登場：アトレティコがシュトゥットガルトと引き分け、アロンソとサインツが同点。", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 16
lt = "«¡Hola! Soy Mei y estudio español en Pekín. El domingo voy a ver el Clásico con mis amigos — y antes, a dormir una hora más. ¡Gracias por el periódico!» — Mei （carta de ejemplo, escrita por la redacción）"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("見本の手紙で、本物ではありません。VOL.2 に本物の手紙と最優秀作文を掲載。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DE LOS LECTORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "見本の手紙で、本物ではありません。VOL.2 に本物の手紙と最優秀作文を掲載。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases de la semana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "FRASES DE LA SEMANA　今週の文（今号の記事から一字一句そのまま）", 27, "sans", True, OLIVE)
quotes = [
    ("«La noche tiene 25 horas y dormimos una hora más.»", "この夜は25時間あり、私たちは1時間長く眠れます。", "Página 1"),
    ("«En Canarias hay una hora menos que en la Península»", "カナリアは半島より1時間少ない。", "Página 2"),
    ("«El sistema sigue — si la ley europea no cambia.»", "制度はこれまで通り——ヨーロッパの法律が変わらないかぎり。", "Página 2"),
    ("«El PSG ganó 4–2 en París: fue la primera derrota azulgrana de la temporada.»", "パリ・サンジェルマンがパリで4–2で勝った：バルサの今季初黒星だ。", "Página 4"),
    ("«España se divide en dos: unos hacen puente y otros, no.»", "スペインは真っ二つ：半分は連休、もう半分は連休ではない。", "Página 3"),
    ("«En Cataluña, la Castanyada: castañas asadas, boniatos y panellets, unos dulces pequeños de mazapán.»", "カタルーニャでは Castanyada に焼き栗、焼き芋、panellets（アーモンドの小さなお菓子）を食べる。", "Página 3"),
    ("«La camiseta se estrena primero con el equipo femenino, el sábado 24»", "このユニフォームは、まず女子チームが土曜24日に初披露する。", "Página 5"),
    ("«Publicamos las dos series con su fuente y su fecha, una junto a otra — y no las mezclamos nunca en un solo número.»", "私たちは二つのデータを出典と日付と並べて載せ、決して一つの数字に混ぜません。", "Página 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "LA PRÓXIMA SEMANA　次号予告 (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "El jueves 29: los actos de memoria de la DANA en Valencia. El sábado 31: Halloween, la Castanyada y el Samaín. El domingo 1: Todos los Santos — y el lunes 2, el puente en nueve comunidades. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lengua.svg")
print("P7 saved, exercises so far:", len(REG))
