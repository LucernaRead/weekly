# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 青年 (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("青年　Juventud", "Lucerna", "Level B1　新电影《试探》　11月片单　Una película nueva y las de noviembre")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-feature")
f.title("新电影《试探》，你去看吗？", 32)
f.byline("Redacción Lucerna　Nivel de lectura B1")
f.para("11月21日星期六，一部新电影要上映了：《试探》。这是悬疑惊悚片，主演是冯绍峰、李梦、陈雨锶。故事讲的是：一个钢琴家，女友失踪了；一个陌生女子走进山间别墅，怪事一件一件地来。")
f.para("看之前，先看简介，再决定要不要买票。悬疑片最怕剧透：别先看别人的影评，别先问看过的人。自己走进电影院，跟着故事猜一猜，才有意思。")
f.para("11月还有别的电影：《白衣逆行者》原定11月6日上映，刘德华主演，讲的是真实事件里的普通人，可是上映前撤档了，没有上映。11月6日，《珠穆朗玛：云中彼岸》在艺联专线上映，讲的是雪山攀登。11月7日，《我们仅有一次的人生》上映，宋佳、文淇主演，讲的是两个孤独的人在寒冬里互相取暖。")
f.para("冬天看电影也很好：外面冷，电影院里暖和。看一部电影，两个小时，故事讲完了，心里也暖了。")
f.para("读书月还在继续：11月7日国际美术馆日，在艺术品中间读书；11月14日文化馆之夜，亲手摸古籍、抄经典。看完电影，也可以去读书月走一走。")
f.gloss("xuányí 悬疑 — suspense, un misterio · shīzōng 失踪 — desaparecido, perdido · biéshù 别墅 — una villa, una casa en las colinas · qǔnuǎn 取暖 — entrar en calor (el uno con el otro).")
f.head("11月片单，怎么选", 25)
f.para("新片很多，先看简介，再看时间：11月6日一部，11月7日一部，11月21日《试探》。选一部你最想看的，再买票。")
f.box("这一周的高频词　Palabras de la semana", [
    ("试探 — 试着问一问，看对方怎么说。", "serif", False, INK, 20, 1.35),
    ("悬疑片最怕剧透，自己走进电影院看。", "serif", False, INK, 20, 1.35),
], tsize=21)  # fix1 D-3: title 23->21, ink 989.5->951.5, box right 961.0
f.end_report()

# col 3: popcorn + film dates + 你呢
ix = COLX[3]
image(p, "popcorn.jpg", ix, 200, CW, 220)
cy3 = caption(p, ix, 420, CW, "电影院的爆米花（资料图）。看电影的时候，很多人喜欢买一桶爆米花。",
              "Foto: Based5290 — Dominio público (Wikimedia Commons)")
facts = ["11月21日 — 《试探》上映",
         "11月6日 — 《珠穆朗玛》",
         "原定11月6日 — 《白衣逆行者》撤档",
         "11月7日 — 《我们仅有一次的人生》",
         "11月14日 — 读书月文化馆之夜"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "电影小日历　Fechas de cine", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "你呢？你会去看《试探》吗？这个月，你在读什么书？写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("¿Y tú? ¿Verías 《试探》? ¿Qué estás leyendo este mes? Escribe dos frases en chino.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己　¿Y tú?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "¿Y tú? ¿Verías 《试探》? ¿Qué estás leyendo este mes? Escribe dos frases en chino.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "练习　Ejercicios", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8　答案见第8版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P5-ex")
e.head("A　读一读选一选　Leer y elegir", 25)
e.glossline("Lee la página 5 y elige la mejor respuesta.")
e.ex("B1", "单选", "A", "《试探》 es una película de suspense.",
     "《试探》是哪种电影？ A. 悬疑惊悚片 · B. 动画片 · C. 纪录片", size=20, gap=6)
e.ex("B1", "单选", "A", "《试探》 se estrena el 21 nov.",
     "《试探》在哪天上映？ A. 11月21日 · B. 11月13日 · C. 11月7日", size=20, gap=6)
e.ex("B1", "单选", "A", "La historia trata de un pianista.",
     "《试探》讲的是谁？ A. 钢琴家 · B. 船长 · C. 画家", size=20, gap=6)
e.ex("B1", "单选", "A", "《白衣逆行者》 se retiró antes de su estreno del 6 nov.",
     "《白衣逆行者》上映了吗？ A. 没有，上映前撤档了 · B. 上映了，11月6日 · C. 上映了，11月7日", size=20, gap=6)
e.ex("B1", "单选", "A", "《我们仅有一次的人生》, con Song Jia y Wen Qi.",
     "《我们仅有一次的人生》主演是谁？ A. 宋佳、文淇 · B. 刘德华 · C. 冯绍峰", size=20, gap=6)
e.head("B　词语填空　Huecos de palabras", 25)
e.glossline("Rellena cada hueco con la palabra correcta.")
e.ex("B1", "完成句子", "悬疑", "xuányí — 《试探》 es una película de suspense.",
     "《试探》是___惊悚片，11月21日上映。", instr="Completa", size=20, gap=6)
e.ex("B1", "完成句子", "失踪", "shīzōng — la novia del pianista ha desaparecido.",
     "钢琴家的女友___了。", instr="Completa", size=20, gap=6)
e.ex("B1", "完成句子", "别墅", "biéshù — una villa en las colinas.",
     "陌生女子走进山间___。", instr="Completa", size=20, gap=6)
e.ex("B1", "完成句子", "真实", "zhēnshí — 《白衣逆行者》 se basa en hechos reales.",
     "《白衣逆行者》讲的是___事件里的普通人。", instr="Completa", size=20, gap=6)
e.ex("A2", "完成句子", "七", "Siete sedes en el Mes de la Lectura.",
     "读书月有___个场馆一起参加。", instr="Completa", size=20, gap=6)
e.head("C　时间与数字　Horas y números", 25)
e.glossline("Responde con fechas y números de la Página 5.")
e.ex("B1", "完成句子", "21", "《试探》 se estrena el 21 nov.",
     "《试探》在11月___日上映。", instr="Completa", size=20, gap=6)
e.ex("B1", "完成句子", "6", "《珠穆朗玛：云中彼岸》 se estrena el 6 nov.",
     "《珠穆朗玛：云中彼岸》在11月___日上映。", instr="Completa", size=20, gap=6)
e.ex("B1", "完成句子", "7", "《我们仅有一次的人生》 se estrena el 7 nov.",
     "《我们仅有一次的人生》在11月___日上映。", instr="Completa", size=20, gap=6)
e.ex("B1", "完成句子", "14", "Noche cultural: 14 de noviembre.",
     "文化馆之夜在11月___日。", instr="Completa", size=20, gap=6)
e.head("D　词语配对　Emparejar", 25)
e.match_set("B1", "词汇配对",
            ["试探", "悬疑", "失踪", "别墅"],
            ["山里的独栋房子",
             "让人猜不透，心里发紧的故事",
             "试着问一问，看对方怎么说",
             "人不见了，不知道去了哪里"],
            ["c", "b", "d", "a"],
            ["试探 = tantear el terreno, c", "悬疑 = suspense, b", "失踪 = desaparecido, d", "别墅 = una villa, a"],
            instr="Empareja las palabras")
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-qingnian.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 深读 (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("深读　Lectura profunda", "Lucerna", "Level B2　包裹深读　Por qué no hubo una explosión de paquetes")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P6-feature")
f.title("今年的包裹，为什么没有爆掉？", 32)
f.byline("Redacción Lucerna　Nivel de lectura B2")
f.para("今年的双11，快递没有爆掉。往年是11月11日、12日两天最忙，今年是“无高峰，全高峰”：没有一天突然爆掉，但每一天都很忙。")
f.para("为什么会这样？因为卖东西的办法变了：预售前置、现货补量、返场加购、分期发货。货不是一天发完的，是分好几批发的。第一波在10月20日到21日，第二波在10月31日，第三波在11月11日。中通云仓预计，第三波是最高峰。")
f.para("再看邮政局的数字：去年双11（10月21日到11月11日，22天），全行业一共揽收139.38亿件；单日最高7.77亿件。注意：139.38亿件是22天的总数，7.77亿件是一天的最高量——两个数字不是一回事，不能直接比大小。")
f.para("湖南顺丰说，配送高峰在11月12日到15日，人力和运力比平时多了约20%。铁路也帮忙：高铁急送覆盖196个主要城市，最快4小时门到门。")
f.para("可是，没有爆掉，不等于都准时到。天气、路况、网点的人手，都会影响速度。包裹到了以后，先打开看一看，再确认收货。")
f.para("结论：双11的包裹没有爆掉，是因为活动分三段，人也分三批下单。知道这一点，等包裹的时候，就不用天天着急了。")
f.gloss("dǎsàn 打散 — repartir, romper un pico · fǎnchǎng 返场 — una reventa, una venta extra · fēnqī 分期 — a plazos, en tandas · zǒngshù 总数 — un total, la suma.")
f.para("读图的时候，先问：这根柱子是什么？是总数，还是一天的量？先看数据，再看广告，高峰来了也不慌。")
f.gloss("yùjì 预计 — una estimación, lo que se espera, aún no contado.")
f.end_report()

# ---- postal-bureau chart (cols 0-2) ----
ly = 1210
p.text(MX, ly + 26, "快递量：22天总数和一天最高量　Cifras de la administración postal, Double 11 2025", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ly + 40, OLIVE, 2)
rows = [("22天总数", 139.38, "139.38亿件"), ("最高一天", 7.77, "7.77亿件")]
SCALE = 3.8
BARX = MX + 340
by0 = ly + 60
for i, (name, val, lab) in enumerate(rows):
    yy = by0 + i * 50
    p.text(MX, yy + 30, name, 24, "sans", True, INK)
    bw_ = val * SCALE
    p.rect(BARX, yy + 4, bw_, 30, fill=OLIVE if i == 0 else CLOTH)
    p.text(BARX + bw_ + 16, yy + 30, lab, 24, "serif", True, INK)
p.para(MX, by0 + 2 * 50 + 12, "Barras desde 0. Las dos barras son medidas diferentes: la primera es un total de 22 días, la segunda el volumen más alto de un solo día. No las compares como tendencia. Cifras: 国家邮政局 (administración postal) — balance final del Double 11 2025 (21 oct.–11 nov., 22 días). Solo para practicar la lectura.", 20.5, "serif", False, GREY, 1323, 1.4)

# col 3: key points + three questions + 你呢
ix = COLX[3]
facts = ["三波高峰 — 10月20日，10月31日，11月11日",
         "22天总数 — 139.38亿件",
         "单日最高 — 7.77亿件",
         "先看数据，再确认收货"]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "深读要点　Ideas clave", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
qs = ["1. 这是说法，还是数据？",
      "2. 数据是谁量的？哪一天？",
      "3. 预报和事实，分得清吗？"]
qh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 14 for t in qs) + 30
p.rect(ix, ay3, CW, qh, fill=BOX)
yy3 = ay3 + 16
p.text(ix + 22, yy3 + 26, "读新闻三问　Tres preguntas", 24, "sans", True, OLIVE)
yy3 += 52
for t in qs:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 8
ey3 = ay3 + qh + 26
etvous = "你呢？你的包裹等了几天？你会先打开看一看吗？写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("¿Y tú? ¿Cuántos días tardó tu paquete? ¿Lo abres y lo revisas primero? Escribe dos frases en chino.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己　¿Y tú?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "¿Y tú? ¿Cuántos días tardó tu paquete? ¿Lo abres y lo revisas primero? Escribe dos frases en chino.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", ey3 + eh)

# ---- P6 exercises ----
ey = 1560
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "练习　Ejercicios", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8　答案见第8版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P6-ex")
e.head("A　读一读选一选　Leer y elegir", 25)
e.glossline("Lee la página 6 y elige la mejor respuesta.")
e.ex("B2", "单选", "A", "Ningún día explotó; todos los días fueron a tope.",
     "今年的双11快递怎么样？ A. 没有一天爆掉 · B. 11月11日一天爆掉 · C. 快递都停了", size=20, gap=6)
e.ex("B2", "单选", "A", "El total de 22 días es de 139,38 mil millones de artículos.",
     "22天总数是多少？ A. 139.38亿件 · B. 7.77亿件 · C. 6.34亿件", size=20, gap=6)
e.ex("B2", "单选", "A", "El mejor día llegó a 777 millones de artículos.",
     "单日最高是多少？ A. 7.77亿件 · B. 139.38亿件 · C. 6.34亿件", size=20, gap=6)
e.ex("B2", "单选", "A", "El pico de entregas es del 12 al 15 nov.",
     "配送高峰在哪几天？ A. 11月12日到15日 · B. 11月9日到11日 · C. 10月20日到21日", size=20, gap=6)
e.ex("B2", "单选", "B", "Abre el paquete y revisa antes de confirmar.",
     "包裹到了以后，先做什么？ A. 直接确认收货 · B. 先打开看一看 · C. 先放一个月", size=20, gap=6)
e.head("B　词语填空　Huecos de palabras", 25)
e.glossline("Rellena cada hueco con la palabra correcta.")
e.ex("B2", "完成句子", "打散", "dǎsàn — el pico se repartió, no fue un solo día.",
     "快递量被___了，没有一天突然爆掉。", instr="Completa", size=20, gap=6)
e.ex("B2", "完成句子", "批", "pī — las mercancías se envían en varias tandas.",
     "货是分好几___发的。", instr="Completa", size=20, gap=6)
e.ex("B2", "完成句子", "二十二", "139.38亿件 es el total de 22 días.",
     "139.38亿件是___天的总数。", instr="Completa", size=20, gap=6)
e.ex("B2", "完成句子", "亿", "yì — 100 millones; 7.77亿件 en un día.",
     "单日最高是7.77___件。", instr="Completa", size=20, gap=6)
e.ex("B2", "完成句子", "4", "Exprés de alta velocidad: 4 horas de puerta a puerta.",
     "高铁急送最快___小时门到门。", instr="Completa", size=20, gap=6)
e.head("C　图表读数　Leer el gráfico", 25)
e.glossline("Lee el gráfico de la página 6.")
e.ex("B2", "完成句子", "139.38", "El total de 22 días es 139.38亿件.",
     "22天总数是___亿件。", instr="Completa", size=20, gap=6)
e.ex("B2", "完成句子", "7.77", "El mejor día llegó a 7.77亿件.",
     "单日最高是___亿件。", instr="Completa", size=20, gap=6)
e.ex("B2", "完成句子", "一天", "Una barra es un total de 22 días, la otra el pico de un día.",
     "图里两根柱子，一个是22天总数，一个是___最高量。", instr="Completa", size=20, gap=6)
e.ex("B2", "完成句子", "数据", "shùjù — números medidos, no afirmaciones.",
     "139.38亿件和7.77亿件，都是邮政局的___，不是广告词。", instr="Completa", size=20, gap=6)
e.head("D　词语配对　Emparejar", 25)
e.match_set("B2", "词汇配对",
            ["说法", "数据", "预报", "预计"],
            ["还没发生的事，先猜一猜",
             "大概的数字，还没最后数完",
             "别人说的话，不一定是真的",
             "量出来的数字"],
            ["c", "d", "a", "b"],
            ["说法 = una afirmación, c", "数据 = números medidos, d", "预报 = un pronóstico, a", "预计 = una estimación, b"],
            instr="Empareja las palabras")
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-shendu.svg")
print("P6 saved, exercises so far:", len(REG))
