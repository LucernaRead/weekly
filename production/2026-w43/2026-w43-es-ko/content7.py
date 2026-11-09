# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LENGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LENGUA　언어", "La Lucerna", "언어 집중　Tres niveles, tres herramientas　세 단계, 세 가지 도구")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　DECIR LA HORA Y EL PRESENTE", 24)
a.para("Para decir la hora: «Es la una», pero «Son las dos, las tres…». «Y media» es +30 minutos (2:30); «menos cuarto», −15 (2:45).", 21.5)
a.para("Y ojo con dormir: el presente cambia la vocal — duermo, duermes, duerme… pero dormimos, dormís. Despertarse es reflexivo: me despierto, se despierta.", 21.5)
a.expl('시간을 말할 때 ‘1시’만 es를 써요. dormir는 불규칙 활용이고 despertarse는 재귀동사예요.')
a.ex("A2", '문장 완성', "Son", '10시는 Son을 써요 (la una만 Es를 써요)',
     "___ las diez de la noche. Empieza la película.", instr='빈칸 채우기', size=20.5, gap=10)
a.ex("A2", '문장 완성', "duerme", "dormir: él → duerme（o→ue）",
     "Mi hermano ___ (dormir) hasta las once el domingo.", instr='빈칸 채우기', size=20.5, gap=10)
a.ex("A2", '문장 완성', "se despierta", "despertarse: ella → se despierta",
     "Ella ___ (despertarse) a las ocho.", instr='빈칸 채우기', size=20.5, gap=10)
a.ex("A2", '객관식', "B", 'y media = 30분',
     "«Son las dos y media» son las... A. 2:15 · B. 2:30 · C. 2:45", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　COMPARATIVOS Y PASADO", 24)
b.para("Para comparar: más / menos + adjetivo + que. Dos irregulares para recordar: bueno → mejor, malo → peor.", 21.5)
b.para("Para contar el martes de Champions usamos el pretérito indefinido: ganó, marcó, perdió, cortó. Es el tiempo de los resultados y de las crónicas.", 21.5)
b.expl('비교급은 más…que예요. bueno→mejor, malo→peor는 불규칙이에요. 경기 결과는 indefinido 과거로 말해요.')
b.ex("B1", '문장 완성', "más importante", 'más + 형용사 (비교)',
     "El Clásico es ___ que un partido normal. (importante)", instr='빈칸 채우기', size=20.5, gap=10)
b.ex("B1", '문장 완성', "peor", 'malo의 비교급은 peor예요',
     "Fue la ___ (malo) noche del Barça esta temporada.", instr='빈칸 채우기', size=20.5, gap=10)
b.ex("B1", '문장 완성', "marcó", 'marcar의 indefinido: marcó',
     "Doué ___ (marcar) el primer gol en París.", instr='빈칸 채우기', size=20.5, gap=10)
b.ex("B1", '객관식', "B", '비야레알이 4–3으로 졌어요',
     "El Villarreal en Liverpool... A. ganó 4–3 · B. perdió 4–3 · C. empató 0–0", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　CREO QUE… / NO CREO QUE…", 24)
c.para("Con «creo que» afirmamos: va el indicativo — «Creo que el Clásico es el domingo». Con «no creo que», con dudas y con «es importante que» va el subjuntivo: tenga (tener), sea (ser), llueva (llover).", 21.5)
c.para("Es la gramática de la página 6: opinar sobre encuestas sin afirmar más de lo que sabemos.", 21.5)
c.expl('creo que 뒤에는 직설법, no creo que와 es importante que 뒤에는 접속법 (tenga/sea/llueva)이 와요.')
c.ex("B2", '문장 완성', "es", 'creo que + 직설법: es',
     "Creo que el Clásico ___ (ser) el domingo.", instr='빈칸 채우기', size=20.5, gap=10)
c.ex("B2", '문장 완성', "sea", 'no creo que + 접속법: sea',
     "No creo que el gráfico ___ (ser) completo sin la fuente.", instr='빈칸 채우기', size=20.5, gap=10)
c.ex("B2", '문장 완성', "tenga", 'es importante que + 접속법: tenga',
     "Es importante que cada encuesta ___ (tener) su fecha.", instr='빈칸 채우기', size=20.5, gap=10)
c.ex("B2", '객관식', "B", 'es posible que + 접속법 llueva',
     "«Es posible que el domingo...» A. llueve · B. llueva · C. llover", size=20.5, gap=10)
c.end_report()

# ---- col 3: errores típicos + palabra + lectores ----
bx = COLX[3]
errs = [
    ("«Es las tres.»", "→ «Son las tres.» Solo «la una» usa es; las demás horas usan son.", '‘1시’만 es를 쓰고 나머지 시간은 son을 써요.'),
    ("«Hoy soy muy aburrido.»", "→ «Hoy estoy muy aburrido.» Estado de hoy: estar. Ser aburrido = ser una persona aburrida.", '오늘 상태는 estar, 성격은 ser예요.'),
    ("«Me gusta los libros.»", "→ «Me gustan los libros.» Gustar cambia con la cosa: gusta / gustan.", 'gustar는 단수 gusta, 복수 gustan.'),
    ("«La gente son felices.»", "→ «La gente es feliz.» Gente es singular, como un solo grupo.", 'gente는 단수 집합명사라 동사도 단수예요.'),
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
p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS　자주 하는 실수", 23, "sans", True, OLIVE)
yy3 += 44
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 17, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 17, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 16, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 4
wy = 200 + eh + 16
wt = "« empatar » es terminar igual: en un partido, no ganar ni perder. Esta semana la palabra vive dos veces: el Atlético empató en Stuttgart — ¡y Alonso y Sainz llegan empatados a Austin, con los mismos puntos!"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap('empatar = 비기다. 이번 주 두 번 나와요: 아틀레티코 무승부, 알론소·사인스 동점.', "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PALABRA　이번 주 단어", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "empatar = 비기다. 이번 주 두 번 나와요: 아틀레티코 무승부, 알론소·사인스 동점.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 16
lt = "«¡Hola! Soy Mei y estudio español en Pekín. El domingo voy a ver el Clásico con mis amigos — y antes, a dormir una hora más. ¡Gracias por el periódico!» — Mei （carta de ejemplo, escrita por la redacción）"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap('편집부가 쓴 예시 편지예요. VOL.2에는 실제 편지와 8면 최고 글을 실어요!', "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DE LOS LECTORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "편집부가 쓴 예시 편지예요. VOL.2에는 실제 편지와 8면 최고 글을 실어요!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases de la semana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 4, OLIVE, 2)  # ko W43: rule 1686->1696, clears CARTAS gloss tail (was LINEX)
p.text(MX, fy + 24, "FRASES DE LA SEMANA　이번 주 문장 (이번 호 글에서 그대로 뽑았어요)", 27, "sans", True, OLIVE)
quotes = [
    ("«La noche tiene 25 horas y dormimos una hora más.»", '이 밤은 25시간이고, 우리는 한 시간 더 자요.', "Página 1"),
    ("«En Canarias hay una hora menos que en la Península»", '카나리아는 본토보다 한 시간 적어요.', "Página 2"),
    ("«El sistema sigue — si la ley europea no cambia.»", '유럽 법이 바뀌지 않으면 제도는 그대로예요.', "Página 2"),
    ("«El PSG ganó 4–2 en París: fue la primera derrota azulgrana de la temporada.»", '파리 생제르맹이 파리에서 4–2로 이겼어요. 바르사의 이번 시즌 첫 패배예요.', "Página 4"),
    ("«España se divide en dos: unos hacen puente y otros, no.»", '스페인은 둘로 나뉘어요. 연휴인 곳과 아닌 곳이에요.', "Página 3"),
    ("«En Cataluña, la Castanyada: castañas asadas, boniatos y panellets, unos dulces pequeños de mazapán.»", '카탈루냐의 Castanyada에는 군밤, 군고구마, 그리고 아몬드 반죽으로 만든 작은 과자 panellets를 먹어요.', "Página 3"),
    ("«La camiseta se estrena primero con el equipo femenino, el sábado 24»", '이 유니폼은 토요일 24일 여자 팀이 먼저 선보여요.', "Página 5"),
    ("«Publicamos las dos series con su fuente y su fecha, una junto a otra — y no las mezclamos nunca en un solo número.»", '두 시리즈를 출처와 날짜와 함께 나란히 싣고, 절대로 하나의 숫자로 섞지 않아요.', "Página 6"),
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
p.text(MX + 28, py + 44, "LA PRÓXIMA SEMANA　다음 호 예고 (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "El jueves 29: los actos de memoria de la DANA en Valencia. El sábado 31: Halloween, la Castanyada y el Samaín. El domingo 1: Todos los Santos — y el lunes 2, el puente en nueve comunidades. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lengua.svg")
print("P7 saved, exercises so far:", len(REG))
