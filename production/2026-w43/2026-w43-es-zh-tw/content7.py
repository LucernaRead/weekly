# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-es-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LENGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LENGUA · 語言", "La Lucerna", "語言聚焦 · Tres niveles, tres herramientas · 三個級別，三件工具")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · DECIR LA HORA Y EL PRESENTE", 24)
a.para("Para decir la hora: «Es la una», pero «Son las dos, las tres…». «Y media» es +30 minutos (2:30); «menos cuarto», −15 (2:45).", 21.5)
a.para("Y ojo con dormir: el presente cambia la vocal — duermo, duermes, duerme… pero dormimos, dormís. Despertarse es reflexivo: me despierto, se despierta.", 21.5)
a.expl("報時僅「一點」用 es；dormir 是不規則變位；despertarse 是反身動詞。")
a.ex("A2", "完成句子", "Son", "十點鐘用 Son（只有 la una 用 Es）",
     "___ las diez de la noche. Empieza la película.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "duerme", "dormir: él → duerme（o→ue）",
     "Mi hermano ___ (dormir) hasta las once el domingo.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "se despierta", "despertarse: ella → se despierta",
     "Ella ___ (despertarse) a las ocho.", instr="填空", size=20.5, gap=10)
a.ex("A2", "單選", "B", "y media = 30 分鐘",
     "«Son las dos y media» son las... A. 2:15 · B. 2:30 · C. 2:45", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · COMPARATIVOS Y PASADO", 24)
b.para("Para comparar: más / menos + adjetivo + que. Dos irregulares para recordar: bueno → mejor, malo → peor.", 21.5)
b.para("Para contar el martes de Champions usamos el pretérito indefinido: ganó, marcó, perdió, cortó. Es el tiempo de los resultados y de las crónicas.", 21.5)
b.expl("比較級 más…que；bueno→mejor、malo→peor 不規則；講賽果用過去式 indefinido。")
b.ex("B1", "完成句子", "más importante", "más + 形容詞（比較）",
     "El Clásico es ___ que un partido normal. (importante)", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "peor", "malo 的比較級是 peor",
     "Fue la ___ (malo) noche del Barça esta temporada.", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "marcó", "marcar 的 indefinido：marcó",
     "Doué ___ (marcar) el primer gol en París.", instr="填空", size=20.5, gap=10)
b.ex("B1", "單選", "B", "比利亞雷亞爾 4–3 落敗",
     "El Villarreal en Liverpool... A. ganó 4–3 · B. perdió 4–3 · C. empató 0–0", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · CREO QUE… / NO CREO QUE…", 24)
c.para("Con «creo que» afirmamos: va el indicativo — «Creo que el Clásico es el domingo». Con «no creo que», con dudas y con «es importante que» va el subjuntivo: tenga (tener), sea (ser), llueva (llover).", 21.5)
c.para("Es la gramática de la página 6: opinar sobre encuestas sin afirmar más de lo que sabemos.", 21.5)
c.expl("creo que 後用陳述式；no creo que、es importante que 後用虛擬式：tenga、sea、llueva。")
c.ex("B2", "完成句子", "es", "creo que + 陳述式：es",
     "Creo que el Clásico ___ (ser) el domingo.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "sea", "no creo que + 虛擬式：sea",
     "No creo que el gráfico ___ (ser) completo sin la fuente.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "tenga", "es importante que + 虛擬式：tenga",
     "Es importante que cada encuesta ___ (tener) su fecha.", instr="填空", size=20.5, gap=10)
c.ex("B2", "單選", "B", "es posible que + 虛擬式 llueva",
     "«Es posible que el domingo...» A. llueve · B. llueva · C. llover", size=20.5, gap=10)
c.end_report()

# ---- col 3: errores típicos + palabra + lectores ----
bx = COLX[3]
errs = [
    ("«Es las tres.»", "→ «Son las tres.» Solo «la una» usa es; las demás horas usan son.", "只有「一點」用 es，其餘鐘點用 son。"),
    ("«Hoy soy muy aburrido.»", "→ «Hoy estoy muy aburrido.» Estado de hoy: estar. Ser aburrido = ser una persona aburrida.", "今天的狀態用 estar；ser 指人無趣。"),
    ("«Me gusta los libros.»", "→ «Me gustan los libros.» Gustar cambia con la cosa: gusta / gustan.", "gustar 看對象：單數 gusta，複數 gustan。"),
    ("«La gente son felices.»", "→ «La gente es feliz.» Gente es singular, como un solo grupo.", "gente 是單數集合名詞，動詞用單數。"),
]
# 盒高 = 繪製循環精確模擬（2026-10-21 回補：原平均行高公式系統性低估 206.5，第四條被下方盒覆蓋；修法與 ES×EN 版一致）
_sim = 216 + 44
for _w, _r, _n in errs:
    _sim += 17 + len(wrap(_w, "serif", True, 21.5, CW - 44)) * 21.5 * 1.36 \
          + 17 + len(wrap(_r, "serif", False, 20.5, CW - 44)) * 20.5 * 1.36 \
          + 16 + len(wrap(_n, "sans", False, 19.5, CW - 44)) * 19.5 * 1.36 + 4
eh = _sim - 200 + 12
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS · 常見錯誤", 23, "sans", True, OLIVE)
yy3 += 44
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 17, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 17, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 16, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 4
wy = 200 + eh + 16
wt = "« empatar » es terminar igual: en un partido, no ganar ni perder. Esta semana la palabra vive dos veces: el Atlético empató en Stuttgart — ¡y Alonso y Sainz llegan empatados a Austin, con los mismos puntos!"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("empatar = 打平。本週出現兩次：馬競戰平史圖加特，阿隆索塞恩斯同分。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PALABRA · 本週生詞", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "empatar = 打平。本週出現兩次：馬競戰平史圖加特，阿隆索塞恩斯同分。", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 16
lt = "«¡Hola! Soy Mei y estudio español en Pekín. El domingo voy a ver el Clásico con mis amigos — y antes, a dormir una hora más. ¡Gracias por el periódico!» — Mei （carta de ejemplo, escrita por la redacción）"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("編輯部示例信，非真實來信。VOL.2 刊真實來信與第 8 版最佳作文——寫信來吧！", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DE LOS LECTORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "編輯部示例信，非真實來信。VOL.2 刊真實來信與第 8 版最佳作文——寫信來吧！", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases de la semana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASES DE LA SEMANA · 本週金句（逐字摘自本期文章）", 27, "sans", True, OLIVE)
quotes = [
    ("«La noche tiene 25 horas y dormimos una hora más.»", "這一夜有 25 個小時，我們多睡一小時。", "Página 1"),
    ("«En Canarias hay una hora menos que en la Península»", "加那利比半島少一個小時。", "Página 2"),
    ("«El sistema sigue — si la ley europea no cambia.»", "制度照舊——除非歐洲法律改變。", "Página 2"),
    ("«El PSG ganó 4–2 en París: fue la primera derrota azulgrana de la temporada.»", "巴黎聖日耳曼在巴黎 4–2 獲勝：這是巴薩本賽季首敗。", "Página 4"),
    ("«España se divide en dos: unos hacen puente y otros, no.»", "西班牙分成兩半：一半放連假，另一半沒有。", "Página 3"),
    ("«En Cataluña, la Castanyada: castañas asadas, boniatos y panellets, unos dulces pequeños de mazapán.»", "在加泰羅尼亞，Castanyada 節吃烤栗子、烤紅薯和 panellets——一種杏仁糖小甜點。", "Página 3"),
    ("«La camiseta se estrena primero con el equipo femenino, el sábado 24»", "這件球衣先由女足在週六 24 日首秀。", "Página 5"),
    ("«Publicamos las dos series con su fuente y su fecha, una junto a otra — y no las mezclamos nunca en un solo número.»", "我們把兩組數據連同來源和日期並排刊登，永不混成一個數字。", "Página 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "LA PRÓXIMA SEMANA · 下期預告 (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "El jueves 29: los actos de memoria de la DANA en Valencia. El sábado 31: Halloween, la Castanyada y el Samaín. El domingo 1: Todos los Santos — y el lunes 2, el puente en nueve comunidades. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lengua.svg")
print("P7 saved, exercises so far:", len(REG))
