# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 头版 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1 · 第 1 号", 23, "sans", True, OLIVE)
p.text(975, 92, "每周读中文 · Читайте настоящий китайский — каждую неделю", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "2026年10月19日（周一）— 25日（周日）", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "简体中文版 · VOL.1 · 双11 · 大闸蟹 · 霜降", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "给学中文的人的周报 — Настоящий Китай — по-китайски", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)
# pairing badge: which text, which explanation language, which reader
p.text(975, 434, "ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", 19.5, "sans", True, BRICK, anchor="middle")

# band
p.rect(MX, 458, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 512, "双11到了「付尾款周」!周二晚 8 点,天猫付尾款", 36, "sans", True, "#f3edda")
p.text(MX + 30, 556, "京东已经开卖;现货一直卖到 11 月 13 日,这一周就能买。", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 512, "付尾款周", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 556, "Неделя остатка · ключевые сроки — страница 2", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "头条 · Главная тема", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "双11到了「付尾款」的这一周", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 30, "周二 20:00,天猫付尾款、现货开售——今年的购物季来得更早,也更长", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "Редакция Lucerna · Уровень чтения A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("今年的双11来得早。京东10月12日晚上8点就开始卖现货,10月20日晚上8点还有「开门红」。", size=24)
f.para("淘宝和天猫10月15日晚上8点开始预售。预售,就是先付一点定金,把看好的东西先订下来。", size=24)
f.para("10月20日晚上8点,是今年双11最重要的时间:大家付尾款,现货也同时开售。付完尾款,快递就开始送货了。", size=24)
f.para("现货会一直卖到11月13日。所以这一周,不用等11月11日,双11已经开始了。", size=24)
f.para("这一周,手机上最常见的话是:定金、尾款、满减、凑单、红包口令。第2版有双11日历和买东西的办法。", size=24)
f.para("这是《Lucerna》简体中文版第1号。每周,我们用简单的中文,带你读真正的中国新闻。欢迎你!", size=24)
f.gloss("yùshòu 预售 — предпродажа: заказ до дня продаж · dìngjīn 定金 — задаток · wěikuǎn 尾款 — остаток, платят позже · xiànhuò 现货 — товар в наличии, готов к отправке.")
f.box("数字看本周 · Неделя в цифрах", [
    ("20 октября, 20:00 — Tmall: доплата остатка; начинаются продажи со склада", "serif", False, INK, 20, 1.35),
    ("13 ноября — последний день продаж со склада", "serif", False, INK, 20, 1.35),
    ("15 октября — день старта предпродаж Taobao и Tmall", "serif", False, INK, 20, 1.35),
    ("№ 8 — место темы «大闸蟹价格» в снимке горячих поисков (правая колонка)", "serif", False, INK, 20, 1.35),
])
f.head("即学即练 · Сразу к практике", 25)
f.ex("A2", "完成句子", "12", "JD.com начал продажи со склада 12 октября.",
     "京东10月___日开始卖现货。", instr="Впишите слово", size=19.5, gap=6)
f.ex("A2", "完成句子", "10", "Предпродажа Tmall началась в месяце 10 (октябрь).",
     "天猫预售___月15日开始。", instr="Впишите слово", size=19.5, gap=6)
f.ex("A2", "完成句子", "8", "Доплата остатка открылась в 20:00.",
     "付尾款的时间是10月20日晚上___点。", instr="Впишите слово", size=19.5, gap=6)
f.ex("A2", "完成句子", "定金", "При предпродаже сначала платят задаток.",
     "预售的时候先付___。", instr="Впишите слово", size=19.5, gap=6)
f.ex("A2", "完成句子", "13", "Продажи со склада идут до 13 ноября.",
     "现货一直卖到11月___日。", instr="Впишите слово", size=19.5, gap=6)
f.ex("A2", "完成句子", "尾款", "После оплаты остатка начинается доставка.",
     "付完___,快递就开始送货了。", instr="Впишите слово", size=19.5, gap=6)
f.end_report()

# ---- search heat box (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "本周热搜 · Горячие поиски", 25, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "大家在搜什么 · Что ищут все", 22, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Снимок зеркала горячих поисков Weibo", 19, "sans", False, GREY)
topics = [
    "大闸蟹价格争议 — 第 8 位",
    "NBA 新赛季 — 第 9 位(热度约 34.9 万)",
    "中国体操男队世锦赛铜牌 — 第 19 位",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 10
p.para(gx + 22, byy + 12, "Рейтинги и цифры популярности взяты из снимка стороннего зеркала от 21 октября, 00:30. Цифры приблизительные — это лишь ориентир. Все три темы есть в этом номере.", 18.5, "sans", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 636, "Источник: зеркало горячих поисков (rddh.cn)", 18.5, "sans", False, GREY)
p.text(gx + 22, gy + 664, "Снимок: 21.10.2026, 00:30", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1296
p.rect(gx, sy, gw, 330, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "本期目录 · Содержание", 24, "sans", True, OLIVE)
som = [
    ("2版", "双11日历与本周生活", "A2"),
    ("3版", "重阳刚过,霜降要来", "A2→B1"),
    ("4版", "体操摘铜,NBA 开赛", "B1"),
    ("5版", "电竞 S16 与维密秀", "B1"),
    ("6版", "大闸蟹「价格崩盘」是真的吗", "B2"),
    ("7版", "词语精讲", "A2→B2"),
    ("8版", "测验与答案", "全部"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

# ---- word of the week (col 3) ----
my = 1636
p.text(gx, my + 24, "本周词 · Слово недели", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
p.para(gx, my + 76, "「尾款」 wěikuǎn — остаток: последняя часть цены, которую вы платите. 先付定金,后付尾款 (сначала задаток, потом остаток). Пример: 「尾款付完,快递就来了。」", 21.5, "serif", False, INK, gw, 1.4)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "locker.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "快递柜(资料图)。付完尾款,这一周,包裹会陆续送到你手里。",
        "Фото: Map hobby — CC0 (Wikimedia Commons)")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-week")
f2.head("忙碌的一周", 25)
f2.para("这一周又买东西,又过节气:周五是霜降,秋天快要过完了。周六凌晨还有电竞比赛。先看好日历,再安排周末吧。", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "快讯 · Коротко", 24, "sans", True, OLIVE)
brefs = [
    ("霜降", "周五霜降:吃柿子,加衣服,看红叶。(第 3 版)"),
    ("体操", "中国体操男队在世锦赛拿到铜牌。(第 4 版)"),
    ("S16", "周六凌晨 1 点,S16 瑞士轮开打。(第 5 版)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "闪电问答 · Быстрый опрос", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Прочитайте страницу 1 и выберите · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "单选", "A", "Доплата остатка открылась 20 октября.",
      "天猫付尾款是哪一天? A. 10月20日 · B. 11月11日 · C. 10月15日", size=21)
qf.ex("A2", "单选", "B", "При предпродаже сначала платят задаток.",
      "预售的时候先付什么? A. 尾款 · B. 定金 · C. 快递费", size=21)
qf.ex("A2", "单选", "C", "Тема крабов заняла № 8 в снимке.",
      "「大闸蟹价格」在热搜快照里是第几位? A. 第 9 位 · B. 第 19 位 · C. 第 8 位", size=21)
qf.ex("A2", "单选", "A", "Продажи со склада идут до 13 ноября.",
      "现货一直卖到哪一天? A. 11月13日 · B. 11月11日 · C. 10月31日", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-touiban.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 生活 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("生活 · Жизнь", "Lucerna", "Уровень A2 · 双11日历 · 霜降生活 · Календарь и жизнь поздней осени")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("双11日历:哪天付钱,哪天收货", 37)
f.byline("Редакция Lucerna · Уровень чтения A2")
f.para("双11不是一天,是一段时间。今年从10月中旬就开始了。先记住三个日子:10月15日、10月20日、11月13日。")
f.para("10月15日晚上8点,淘宝、天猫开始预售。预售时先付定金,把喜欢的东西订下来。定金不多,但付了定金,就要记得付尾款。")
f.para("10月20日晚上8点付尾款。尾款就是总价减去定金。付完尾款,商家就发货。京东10月20日晚上8点还有「开门红」,很多现货直接开卖。")
f.para("从10月20日到11月13日是现货期。不想等预售的人,可以在这段时间直接买。这一周包裹很多,收货可能比平时慢一点。")
f.gloss("zǒngjià 总价 — полная цена · fāhuò 发货 — отправить товар · shāngjiā 商家 — продавец, магазин.")
f.head("满减怎么玩 · Как работает 满减", 25)
f.para("Магазины часто устраивают акции вроде «满300减50» (потрать 300 юаней — сэкономь 50). Это и есть 满减 (mǎnjiǎn) — «потрать и сэкономь». Если в корзине не хватает до 300, добавляют одну мелкую вещь и добирают сумму — это называется 凑单 (còudān). Разобранный пример ниже использует учебные цифры.")
f.box("Разобранный пример · 练习例子", [
    ("一件外套 260 元,一条围巾 60 元,一起 320 元。", "serif", False, INK, 20, 1.35),
    ("满 300 减 50,实付 270 元。先付定金 30 元,尾款是 270 − 30 = 240 元。", "serif", False, INK, 20, 1.35),
])
f.head("周五霜降:秋天的最后一个节气", 25)
f.para("10月23日,星期五,是霜降。霜降是二十四节气里的第十八个,也是秋天的最后一个节气。霜降以后,11月7日就是立冬,冬天要来了。")
f.para("霜降的时候,早上的草地上会有白白的霜。天气一天比一天冷,要记得加衣服。老话说:「补冬不如补霜降。」霜降时吃得好一点,冬天身体才好。")
f.para("霜降吃柿子。还有一句话:「霜降吃柿子,嘴唇不会裂。」这个周末,去看看红叶、吃一个柿子,就是很好的安排。")
f.gloss("jiéqì 节气 — 24 солнечных срока, делящих год · shuāng 霜 — иней · lìdōng 立冬 — начало зимы (7 ноября).")
f.box("本周生活小日历 · Даты этой недели", [
    ("周二 20:00 — 天猫付尾款,京东「开门红」", "serif", False, INK, 20, 1.35),
    ("周五 — 霜降:吃柿子,赏红叶,加衣服", "serif", False, INK, 20, 1.35),
    ("周六 01:00 — S16 瑞士轮开打(第 5 版)", "serif", False, INK, 20, 1.35),
])
f.end_report()

# col 3: valley image + facts + 你呢 (sequential, measured)
ix = COLX[3]
image(p, "valley.jpg", ix, 200, CW, 230)
cy3 = caption(p, ix, 430, CW, "秋天的山谷,红叶正当时。霜降前后,是看红叶的好时候。",
              "Фото: Paul Gilmore — CC0 (Wikimedia Commons)")
facts = ["霜降是二十四节气里的第 18 个。",
         "霜降以后是立冬,今年在 11 月 7 日。",
         "上周日(10 月 18 日)是重阳节,故事在第 3 版。"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "你知道吗 · А вы знали?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "你呢?你住的地方,霜降的时候冷不冷?这个双11,你想买什么?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("А вы? Холодно ли там, где вы живёте? Что вы хотите купить на этом 双11? Напишите две фразы по-китайски.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · А вы?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "А вы? Холодно ли там, где вы живёте? Что вы хотите купить на этом 双11? Напишите две фразы по-китайски.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- word strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "购物词语卡 · Слова для покупок", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Четыре слова из любого торгового приложения", 20, "sans", False, GREY, anchor="end")
words = [
    ("定金", "dìngjīn · задаток", "небольшая часть цены, платят первой"),
    ("尾款", "wěikuǎn · остаток", "последняя часть цены"),
    ("满减", "mǎnjiǎn · потрать и сэкономь", "потрать достаточно — цена снизится"),
    ("红包", "hóngbāo · красный конверт", "деньги в красном конверте, на удачу"),
]
for i, (t, lab, en) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX, stroke=LINE, sw=1.4)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, en, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 234, "Запомните фразу: 「先付定金,后付尾款,买满三百还能减五十。」", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Упражнения", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Ответы на странице 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · 读一读选一选 · Выбор ответа", 25)
e.glossline("Прочитайте страницу 2 и выберите лучший ответ.")
e.ex("A2", "单选", "A", "Первая важная дата сезона покупок — 15 октября.",
     "双11第一个要记的日子是哪天? A. 10月15日 · B. 11月11日 · C. 11月13日", size=19, gap=6)
e.ex("A2", "单选", "B", "При предпродаже сначала платят задаток.",
     "预售的时候先付什么? A. 尾款 · B. 定金 · C. 全款", size=19, gap=6)
e.ex("A2", "单选", "A", "После оплаты остатка продавец отправляет товар.",
     "付完尾款以后,商家做什么? A. 发货 · B. 退定金 · C. 关门", size=19, gap=6)
e.ex("A2", "单选", "B", "Shuāngjiàng — 18-й солнечный срок.",
     "霜降是第几个节气? A. 第16个 · B. 第18个 · C. 第24个", size=19, gap=6)
e.ex("A2", "单选", "A", "Lìdōng (начало зимы) идёт после Shuāngjiàng.",
     "霜降以后是哪个节气? A. 立冬 · B. 冬至 · C. 寒露", size=19, gap=6)
e.head("B · 词语填空 · Впишите слово", 25)
e.glossline("Впишите в каждый пропуск верное слово.")
e.ex("A2", "完成句子", "定金", "dìngjīn — задаток при предпродаже.",
     "预售时先付___。", instr="Впишите", size=19, gap=6)
e.ex("A2", "完成句子", "尾款", "wěikuǎn — остаток: итог минус задаток.",
     "总价减去定金,就是___。", instr="Впишите", size=19, gap=6)
e.ex("A2", "完成句子", "满减", "mǎnjiǎn — потрать 300, сэкономь 50.",
     "买满300元便宜50元,这叫___。", instr="Впишите", size=19, gap=6)
e.ex("A2", "完成句子", "霜", "shuāng — белый иней на траве.",
     "霜降的早上,草地上有白白的___。", instr="Впишите", size=19, gap=6)
e.ex("B1", "完成句子", "节气", "jiéqì — Shuāngjiàng, последний срок осени.",
     "二十四___里,霜降是秋天的最后一个。", instr="Впишите", size=19, gap=6)
e.head("C · 数字与日期 · Числа и даты", 25)
e.glossline("Используйте разобранный пример на этой странице.")
e.ex("A2", "完成句子", "260", "Пальто в примере стоит 260 юаней.",
     "练习例子里,外套___元。", instr="Впишите", size=19, gap=6)
e.ex("A2", "完成句子", "320", "260 + 60 = 320 юаней вместе.",
     "外套和围巾一起___元。", instr="Впишите", size=19, gap=6)
e.ex("B1", "完成句子", "270", "320 − 50 = 270 юаней после скидки.",
     "满减以后实付___元。", instr="Впишите", size=19, gap=6)
e.ex("B1", "完成句子", "240", "Остаток: 270 − 30 = 240 юаней.",
     "练习例子里的尾款是___元。", instr="Впишите", size=19, gap=6)
e.head("D · 词语配对 · Сопоставьте пары", 25)
e.match_set("A2", "词汇配对",
            ["定金", "尾款", "满减", "节气"],
            ["划分一年的 24 个时间点",
             "先付的一小部分钱",
             "买满多少,便宜多少",
             "最后付的那部分钱"],
            ["b", "d", "c", "a"],
            ["dìngjīn = платят первым, b", "wěikuǎn = платят последним, d", "mǎnjiǎn = потрать и сэкономь, c", "jiéqì = 24 срока, a"],
            instr="Сопоставьте")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-shenghuo.svg")
print("P2 saved, exercises so far:", len(REG))
