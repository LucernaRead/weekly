# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1　表紙 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL.4　第4号", 23, "sans", True, OLIVE)
p.text(975, 92, "毎週、日本語で　Semanal　日本人が読んでいる日本語を読む", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "2026年11月16日（月）〜22日（日）", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, OLIVE, 1.6)
p.text(975, 262, "Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "日本語版　VOL.4　酉の市　新酒　相撲　紅葉", 40, "serif", True, INK, anchor="middle")
p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "木よう日は二の酉！", 36, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "11月19日（木）は酉の市・二の酉とボジョレー解禁です。", 23, "serif", False, ONCLOTH)
p.text(RIGHT - 30, 524, "Jueves es Ni-no-tori", 24, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "Los dos yokozuna van 2–1　Ver página 4", 21, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "トップニュース　Titular", 22, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "二の酉と新酒、19日の木よう日", 56, "serif", True, INK, 1388, 1.06)
p.text(MX, hy + 30, "夜の浅草と、秋のワイン — 日本の11月の真ん中です", 25, "serif", False, GREY)
hy += 46
p.text(MX, hy + 28, "Lucerna編集部　読むレベル：A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("19日（木よう日）は、酉の市・二の酉です。浅草の鷲神社では、午前0時の一番太鼓から、24時まで市が開きます。熊手を買う人の夜です。")
f.para("同じ19日（木よう日）は、ボジョレー・ヌーヴォーの解禁日です。フランスのボジョレー地方の新酒です。日本は、時差で、世界で最も早く新酒を飲むことができる国だそうです。")
f.para("大相撲の九州場所は、3日目まで終わりました。大の里も豊昇龍も、2勝1敗です。場所は、22日（日よう日）の千秋楽まで続きます。優勝は、まだ決まっていません。")
f.para("紅葉の見頃は、京都へ移っています。ウェザーニューズの10月29日の予報では、京都の嵐山は23日（月よう日）ごろから見頃だそうです。")
f.para("『Lucerna』日本語版の第4号です。今週も、本物の日本のニュースを、やさしい日本語でお届けします。どうぞ楽しんでください！")
f.gloss("解禁 la puesta a la venta　一番太鼓 el primer tambor　千秋楽 el último día　見頃 la mejor época.")
f.box("数字で見る今週　La semana en cifras", [
    ("19 — 二の酉と新酒の解禁日は11月19日（木）です", "serif", False, INK, 20, 1.35),
    ("22 — 相撲の千秋楽は11月22日（日）です", "serif", False, INK, 20, 1.35),
    ("23 — 嵐山の見頃は11月23日ごろです", "serif", False, INK, 20, 1.35),
    ("30 — 流行語のノミネートは30語です", "serif", False, INK, 20, 1.35),
])
f.head("今すぐ練習　Practica ahora", 25)
f.ex("A2", "completa", "19", "Ni-no-tori y Beaujolais: jue. 19 nov.",
     "二の酉は11月 ___ 日（木よう日）です。", size=19.5, gap=6)
f.ex("A2", "completa", "22", "La final del sumo es el 22 de noviembre (domingo)",
     "相撲の千秋楽は11月 ___ 日（日よう日）です。", size=19.5, gap=6)
f.ex("A2", "completa", "23", "Arashiyama: hojas desde el lun. 23 nov.",
     "嵐山は ___ 日（月）ごろから見頃だそうです。", size=19.5, gap=6)
f.ex("A2", "completa", "2", "Los dos yokozuna van 2–1 tras el día 3",
     "3日目まで、大の里も豊昇龍も ___ 勝1敗です。", size=19.5, gap=6)
f.ex("A2", "completa", "19", "Beaujolais Nouveau: jueves 19 de noviembre",
     "ボジョレー・ヌーヴォーの解禁日は、11月 ___ 日です。", size=19.5, gap=6)
f.ex("A2", "completa", "熊手", "Un kumade es el amuleto comprado en Tori-no-ichi",
     "酉の市では、___ を買います。", size=19.5, gap=6)
f.end_report()

# ---- trend box (col 3) ----
gx, gw = COLX[3], CW
gy = 590
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "今週のトレンド", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "日本の「今、熱い話題」", 24, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "発表と予報の日付つきでお届けします", 19, "sans", False, GREY)
topics = [
    "相撲九州場所 — 3日目まで両横綱2勝1敗",
    "酉の市・二の酉 — 19日（木）",
    "ボジョレー解禁 — 19日（木）",
    "紅葉の見頃 — 嵐山は23日ごろ",
]
byy = gy + 150
for i, t in enumerate(topics):
    yy_t = p.para(gx + 22, byy + 22, f"{i+1}. {t}", 20, "serif", True, INK, gw - 44, 1.32)
    byy = yy_t + 26
yy_n = p.para(gx + 22, byy + 24, "相撲の結果は、スポニチとサンスポの報道（11月8日〜10日）です。", 19, "serif", False, GREY, gw - 44, 1.35)
yy_n2 = p.para(gx + 22, yy_n + 24, "紅葉の予報は、ウェザーニューズの発表（10月29日）です。", 19, "serif", False, GREY, gw - 44, 1.35)
p.text(gx + 22, gy + 636, "出典：各発表・予報の日付は記事の中にあります", 17, "sans", False, GREY)
p.text(gx + 22, gy + 664, "Fuentes y fechas en los artículos", 19, "sans", False, GREY)

# ---- contents (col 3) ----
sy = 1306
p.rect(gx, sy, gw, 330, fill=BOX)
p.text(gx + 22, sy + 40, "この号の内容　En este número", 24, "sans", True, OLIVE)
som = [
    ("2面", "酉の市と熊手", "A2"),
    ("3面", "ボジョレーと秋の味", "A2→B1"),
    ("4面", "相撲3日目まで", "B1"),
    ("5面", "流行語30と紅葉の写真", "B1"),
    ("6面", "紅葉は京都へ", "B2"),
    ("7面", "酉の市と流行語のことば", "A2→B2"),
    ("8面", "テストと答え", "Todos los niveles"),
]
yy = sy + 82
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 108, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 37

# ---- word of the week (col 3) ----
my = 1646
p.text(gx, my + 24, "今週のことば　Palabra de la semana", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
y2 = p.para(gx, my + 76, "「熊手（くまで）」 — 酉の市で買う商売繁盛の縁起物です。福をかき込むと言います。", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "熊手 = el rastrillo de bambú de Tori-no-ichi, amuleto para negocios prósperos.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1884, LINE, 1.2)
iy = 1908
ix, iw = span_x(0, 2)
image(p, "maple.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "秋のカエデの葉。今週、見頃は京都へ移ります。（6面）",
        "Foto: Poliphilo — CC0 (Wikimedia Commons)")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1908, 2290, tag="P1-ryukougo")
f2.head("流行語のノミネート", 25)
f2.para("「新語・流行語大賞」のノミネート30語が、5日（木よう日）に発表されました。『りくりゅう』『ちいかわ』『酷暑日』などが入っています。トップテンは、12月1日（火よう日）に発表されます。（5面）", 22.5)
f2.end_report()
# col 3 brief box
bx = COLX[3]
p.rect(bx, 1908, CW, 430, fill=BOX)
p.text(bx + 22, 1938, "短いニュース　En breve", 24, "sans", True, OLIVE)
brefs = [
    ("相撲", "3日目まで、両横綱は2勝1敗です。（4面）"),
    ("小雪", "22日（日）は二十四節気の小雪です。"),
    ("勤労感謝の日", "23日（月）は祝日、勤労感謝の日です。（2面）"),
]
byy = 1968
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2346
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "クイズ　Quiz relámpago", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lee la primera página y elige la respuesta correcta　Respuestas en la página 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "opción múltiple", "B", "Ni-no-tori es el 19 de noviembre (jueves)",
      "二の酉はいつですか。 A. 7日（土）　B. 19日（木）　C. 22日（日）", size=21)
qf.ex("A2", "opción múltiple", "A", "Beaujolais Nouveau: jueves 19 de noviembre",
      "新酒の解禁日はいつですか。 A. 19日（木）　B. 22日（日）　C. 23日（月）", size=21)
qf.ex("A2", "opción múltiple", "B", "Tras el día 3, los dos yokozuna van 2–1",
      "3日目まで、両横綱は何勝何敗ですか。 A. 3勝0敗　B. 2勝1敗　C. 1勝2敗", size=21)
qf.ex("A2", "opción múltiple", "C", "Arashiyama: hojas desde el lun. 23 nov.",
      "嵐山の見頃はいつごろからですか。 A. 13日（金）　B. 21日（土）　C. 23日（月）", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-hyoushi.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2　生活 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("生活　くらし", "Lucerna", "レベル A2　酉の市と熊手　Tori-no-ichi y kumade")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("19日 — 夜通しの酉の市", 37)
f.byline("Lucerna編集部　読むレベル：A2")
f.para("酉の市は、11月の酉の日に開くお祭りです。2026年は、一の酉が7日（土よう日）、二の酉が19日（木よう日）です。三の酉はありません。")
f.para("浅草の鷲神社では、午前0時の一番太鼓から、24時まで市が開きます。となりには、酉の寺の長國寺もあります。熊手店は150店ほど、露店は750店ほどあります。熊手を売る店が、たくさん並びます。")
f.para("熊手は、商売繁盛の縁起物です。金運や福をかき込む、と言います。熊手を買うと、店の人が威勢よく手締めを打ちます。屋台の食べ物も楽しめます。")
f.gloss("夜通し toda la noche　露店 los puestos　威勢よく a voz en grito y con alegría　かき込む recoger.")
f.head("小雪と勤労感謝の日", 25)
f.para("22日（日よう日）は、二十四節気の小雪です。雪が少し降り始めるころ、という意味です。23日（月よう日）は、勤労感謝の日です。祝日です。働く人に、ありがとう、と言う日です。")
f.para("11月の後半は、年末へ向かう季節です。酉の市の夜、紅葉、勤労感謝の日。秋の終わりを、楽しみましょう。")
f.gloss("二十四節気 las 24 estaciones　働く trabajar　年末 el fin de año.")
f.end_report()

# col 3: numbers box + words box + あなた (sequential, measured)
ix = COLX[3]
nums = ["7日 — 一の酉は11月7日（土）でした",
        "19日 — 二の酉は11月19日（木）",
        "24時 — 午前0時から24時まで開きます",
        "2回 — 2026年の酉の市は2回です"]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in nums) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "酉の市の数字", 24, "sans", True, OLIVE)
yy3 += 52
for t in nums:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
fc = ["熊手 — 商売繁盛の縁起物",
      "手締め — 買った時に打つ拍手",
      "一番太鼓 — 午前0時の太鼓"]
fy3 = sy3 + sh + 26
fh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in fc) + 32
p.rect(ix, fy3, CW, fh, fill=BOX)
yy3 = fy3 + 16
p.text(ix + 22, yy3 + 26, "酉の市のことば", 24, "sans", True, OLIVE)
yy3 += 52
for t in fc:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = fy3 + fh + 26
etvous = "あなたは？二の酉で、どんな熊手を買いたいですか。日本語で2文、書いて、送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("¿Qué kumade te gustaría comprar en Ni-no-tori? Escribe dos frases en japonés y envíanoslas.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？　Ahora tú", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "¿Qué kumade te gustaría comprar en Ni-no-tori? Escribe dos frases en japonés y envíanoslas.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- season words strip ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "11月のことば　Palabras de noviembre", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "酉の市と秋の4つの言葉　Cuatro palabras sobre Tori-no-ichi y el otoño", 20, "sans", False, GREY, anchor="end")
words = [
    ("熊手（くまで）", "商売繁盛の縁起物", "rastrillo de bambú para la prosperidad"),
    ("手締め（てじめ）", "拍手で祝うこと", "celebrar con aplausos"),
    ("解禁（かいきん）", "売り始める日", "el día en que empiezan las ventas"),
    ("小雪（しょうせつ）", "雪が少し降るころ", "cuando empieza a caer un poco de nieve"),
]
for i, (t, lab, cn) in enumerate(words):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 106, t, 34, "serif", True, OLIVE)
    yy = p.para(bx + 22, dy + 140, lab, 20.5, "serif", False, INK, CW - 44, 1.32)
    p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)
p.para(MX, dy + 234, "文で覚えましょう：『19日に、浅草で熊手を買います。』", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 250
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "練習　Ejercicios página 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8　Los niveles están mezclados — busca tu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　理解", 25)
e.bridge("第2版の文章を読んで、正しい答えを選んでください。")
e.ex("A2", "opción múltiple", "B", "Ni-no-tori es el 19 de noviembre (jueves)",
     "二の酉はいつですか。 A. 7日（土）　B. 19日（木）　C. 22日（日）", size=19, gap=6)
e.ex("A2", "opción múltiple", "B", "En 2026 hay dos fiestas de Tori-no-ichi",
     "2026年の酉の市は、何回ですか。 A. 1回　B. 2回　C. 3回", size=19, gap=6)
e.ex("A2", "opción múltiple", "A", "Tori-no-ichi dura de medianoche a medianoche",
     "酉の市は、何時から何時までですか。 A. 0〜24時　B. 9〜17時　C. 18〜20時", size=19, gap=6)
e.ex("A2", "opción múltiple", "B", "Un kumade es un amuleto de buena suerte para negocios prósperos",
     "熊手は、何ですか。 A. 食べ物　B. 商売繁盛の縁起物　C. 服", size=19, gap=6)
e.ex("A2", "opción múltiple", "B", "Shōsetsu es el 22 de noviembre (domingo)",
     "小雪はいつですか。 A. 19日　B. 22日　C. 23日", size=19, gap=6)
e.head("B　ことば", 25)
e.bridge("言葉や数字を入れてください。")
e.ex("A2", "completa", "熊手", "熊手 = un rastrillo de bambú para la prosperidad",
     "商売繁盛の縁起物を「___」と言います。", instr="Completa", size=19, gap=6)
e.ex("A2", "completa", "手締め", "手締め = los aplausos al comprar un kumade",
     "熊手を買うと、店の人が「___」を打ちます。", instr="Completa", size=19, gap=6)
e.ex("A2", "completa", "19", "Ni-no-tori es el 19 de noviembre (jueves)",
     "二の酉は11月 ___ 日（木）です。", instr="Completa", size=19, gap=6)
e.ex("A2", "completa", "7", "Ichi-no-tori fue el 7 de noviembre (sábado)",
     "一の酉は11月 ___ 日（土）でした。", instr="Completa", size=19, gap=6)
e.ex("A2", "completa", "勤労感謝の日", "Lun. 23 nov.: Día de Acción de Gracias por el Trabajo",
     "23日（月）は「___」の日です。", instr="Completa", size=19, gap=6)
e.head("C　数字と日付", 25)
e.bridge("第2版の数字と日付で答えてください。")
e.ex("A2", "completa", "0", "Tori-no-ichi empieza a medianoche",
     "酉の市は午前 ___ 時から始まります。", instr="Completa", size=19, gap=6)
e.ex("A2", "completa", "24", "Tori-no-ichi dura hasta medianoche",
     "酉の市は ___ 時まで開きます。", instr="Completa", size=19, gap=6)
e.ex("A2", "completa", "2", "En 2026 hay dos fiestas de Tori-no-ichi",
     "2026年の酉の市は ___ 回です。", instr="Completa", size=19, gap=6)
e.ex("A2", "completa", "22", "Shōsetsu es el 22 de noviembre (domingo)",
     "小雪は11月 ___ 日（日）です。", instr="Completa", size=19, gap=6)
e.head("D　ペアにしましょう", 25)
e.match_set("A2", "relacionar",
            ["熊手", "手締め", "一番太鼓", "小雪"],
            ["雪が少し降り始めるころ",
             "商売繁盛の縁起物",
             "午前0時の太鼓",
             "熊手を買った時に打つ拍手"],
            ["b", "d", "c", "a"],
            ["熊手 = un rastrillo de bambú para la prosperidad b", "手締め = los aplausos al comprar un kumade d", "一番太鼓 = el tambor de medianoche c", "小雪 = cuando empieza a caer un poco de nieve a"],
            instr="Relacionar")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-kurashi.svg")
print("P2 saved, exercises so far:", len(REG))
