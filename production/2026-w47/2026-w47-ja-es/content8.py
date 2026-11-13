# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8　テストと答え =================
CURPAGE[0] = 8
p = BSPage4()
p.band("テストと答え　Ejercicios y respuestas", "Lucerna", "第8面　週の大きなテスト + 全ての答え")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　週のクロニクル", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "Ni-no-tori es el 19 de noviembre (jueves)",
     "酉の市・二の酉は、11月19日（___）です。(A. 木　B. 金)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Beaujolais Nouveau: jueves 19 de noviembre",
     "ボジョレー・ヌーヴォーの解禁日は、11月19日（___）です。(A. 木　B. 土)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Ōnosato perdió contra Yoshinofuji el día 1",
     "大の里は初日、義ノ富士に（___）ました。(A. 負け　B. 勝ち)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Hōshōryū perdió contra Fujiryōga el día 3",
     "豊昇龍は3日目、藤凌駕に（___）ました。(A. 負け　B. 勝ち)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Arashiyama: hojas desde el lun. 23 nov.",
     "嵐山の見頃は、11月23日（___）ごろからです。(A. 月　B. 日)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Shōsetsu es el 22 de noviembre (domingo)",
     "小雪は、11月22日（___）です。(A. 日　B. 月)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Nominaciones: jue. 5 de noviembre",
     "流行語のノミネートは、11月5日（___）に発表されました。(A. 木　B. 金)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "La final del sumo es el 22 de noviembre (domingo)",
     "相撲の千秋楽は、11月22日（___）です。(A. 日　B. 月)", size=13.8, gap=0)
f.head("B　一般問題", 21, OLIVE, 5)
f.ex("A2", "opción múltiple", "A", "Tori-no-ichi se celebra los días del gallo de noviembre",
     "酉の市は、何の日に開きますか。 A. 酉　B. 卯　C. 辰", size=13.8, gap=0)
f.ex("B1", "opción múltiple", "B", "En 2026 hay dos fiestas de Tori-no-ichi",
     "2026年の酉の市は、何回ですか。 A. 1回　B. 2回　C. 3回", size=13.8, gap=0)
f.ex("B1", "opción múltiple", "A", "Las uvas del vino nuevo se cosechan hacia septiembre",
     "新酒のぶどうは、いつ収穫しますか。 A. 9月　B. 12月　C. 2月", size=13.8, gap=0)
f.ex("B1", "opción múltiple", "A", "Tras tres días, los dos yokozuna van 2–1",
     "3日目までの星取は？ A. 2勝1敗　B. 3勝0敗　C. 1勝2敗", size=13.8, gap=0)
f.ex("A2", "opción múltiple", "B", "Un kumade es un amuleto de buena suerte para negocios prósperos",
     "熊手は、何ですか。 A. 赤い飴　B. 商売繁盛の縁起物　C. 緑のお菓子", size=13.8, gap=0)
f.ex("B2", "opción múltiple", "A", "Pronósticos distintos: definiciones distintas",
     "予想が会社によってちがうのは、どうしてですか。 A. 見頃の決め方がちがうから　B. 嵐山が2つあるから　C. 測る機械が壊れたから", size=13.8, gap=0)
f.ex("B2", "opción múltiple", "A", "Arashiyama: hojas desde el 12 dic. aprox.",
     "嵐山の落葉はじめはいつごろからですか。 A. 12月12日ごろ　B. 11月23日　C. 11月13日", size=13.8, gap=0)
f.ex("A2", "opción múltiple", "A", "Chiikawa es un manga de gran éxito",
     "「ちいかわ」は、何ですか。 A. 大ヒットした漫画　B. 相撲　C. お酒", size=13.8, gap=0)
f.head("C　読んで答えましょう", 21, OLIVE, 5)
f.para("ユウは中学生です。今週の木よう日は、酉の市・二の酉です。ユウは夜、家族と浅草へ行って、熊手を見ます。金よう日には、友達と紅葉の写真を上げます。日よう日には、テレビで相撲の千秋楽を見ます。月よう日は、勤労感謝の日で学校が休みです。", 15, lh=1.3, split=False)
f.ex("A2", "opción múltiple", "A", "Jueves: ir a Asakusa en familia",
     "木よう日に何をする？ A. 家族と浅草へ　B. 学校へ　C. 図書館で読む", size=13.8, gap=0)
f.ex("A2", "opción múltiple", "A", "Viernes: subir fotos de hojas",
     "金よう日に何をする？ A. 写真を上げる　B. 神社へ　C. 熊手を買う", size=13.8, gap=0)
f.ex("A2", "opción múltiple", "B", "Domingo: ver la final de sumo",
     "日よう日に何を見ますか。 A. 映画　B. 相撲の千秋楽　C. 野球", size=13.8, gap=0)
f.ex("B1", "opción múltiple", "A", "Lunes sin clase: Día de Acción de Gracias por el Trabajo",
     "月よう日は、どうして学校が休みですか。 A. 勤労感謝の日だから　B. 小雪だから　C. 日よう日だから", size=13.8, gap=0)
f.head("D　文を作りましょう", 21, OLIVE, 5)
f.ex("A2", "construye una frase", "私は木よう日に浅草へ行きます。", "sujeto + tiempo + lugar + verbo",
     "私は / 木よう日に / 浅草へ行きます → ___", instr="Construye una frase", size=13.8, gap=0)
f.ex("A2", "construye una frase", "酉の市は11月の酉の日に開きます。", "sujeto + tiempo + verbo",
     "酉の市は / 11月の酉の日に / 開きます → ___", instr="Construye una frase", size=13.8, gap=0)
f.ex("B1", "construye una frase", "新酒は11月19日から売られます。", "tiempo + verbo",
     "新酒は / 11月19日から / 売られます → ___", instr="Construye una frase", size=13.8, gap=0)
f.ex("B1", "construye una frase", "大の里は3日目まで2勝1敗です。", "2–1 después de tres días",
     "大の里は / 3日目まで / 2勝1敗です → ___", instr="Construye una frase", size=13.8, gap=0)
f.head("E　翻訳しましょう", 21, OLIVE, 5)
f.ex("A2", "Traduce", "Ni-no-tori es el 19 de noviembre.", "Ver página 2",
     "二の酉は11月19日です。 → ___", instr="Traduce", size=13.8, gap=0)
f.ex("B1", "Traduce", "El vino nuevo sale el 19 de noviembre.", "Ver página 3",
     "新酒は11月19日に解禁されます。 → ___", instr="Traduce", size=13.8, gap=0)
f.ex("B1", "Traduce", "Nominaciones: 5 de noviembre.", "Ver página 5",
     "流行語のノミネートは、11月5日に発表されました。 → ___", instr="Traduce", size=13.8, gap=0)
f.ex("B2", "Traduce", "Quien quiera ver las hojas debe comprobar las fechas del pronóstico y la situación actual.", "Ver página 6",
     "紅葉を見に行く人は、予報の日付と今の様子を確かめましょう。→ ___", instr="Traduce", size=13.8, gap=0)
f.head("F　今週のことば", 21, OLIVE, 5)
f.match_set("B2", "relacionar",
            ["熊手", "解禁", "金星", "見頃"],
            ["新酒を売り始める日",
             "紅葉がいちばん美しい時",
             "商売繁盛の縁起物",
             "前頭の力士が横綱に勝つこと"],
            ["c", "a", "d", "b"],
            ["熊手 = un rastrillo de bambú para la prosperidad c", "解禁 = el día en que empiezan las ventas a", "金星 = un luchador de bajo rango vence a un yokozuna d", "見頃 = la mejor época b"],
            instr="Relacionar")
f.head("G　酉の市で", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "Ir a Asakusa",
     "— 酉の市ですね。— はい、浅草へ ___ ます。(A. 行き　B. 行か)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Comprar un kumade",
     "— 熊手を ___ か。 (A. 買います　B. 買った)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Ni-no-tori es el 19 de noviembre (ver página 2)",
     "— 二の酉はいつですか。— 11月 ___ 日です。(A. 19　B. 7)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Recomendar un kumade",
     "— おすすめはありますか。— 『___ 』が人気です。(A. 熊手　B. ポッキー)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "De nada",
     "— ありがとう。— ___ 。(A. どういたしまして　B. さようなら)", size=13.8, gap=0)
f.head("H　書いてみましょう", 21, OLIVE, 5)
MODELO = ("私の11月の1週間は、秋の楽しみが多い1週間です。"
          "木よう日は、酉の市・二の酉です。家族と浅草へ行って、熊手を見ます。"
          "夜の浅草は、明るくにぎやかです。"
          "金よう日は、友達と紅葉の写真を上げます。"
          "日よう日は、テレビで相撲の千秋楽を見ます。"
          "月よう日は、勤労感謝の日で学校が休みです。"
          "11月は短いですが、楽しい季節です。")
NCHARS = len(MODELO.replace(" ", ""))
f.bridge(f"Tarea de redacción (sin una única respuesta correcta); el texto modelo ({NCHARS} caracteres) está abajo.")
f.ex("B1", "Redacción", "(tarea abierta — texto modelo abajo)", f"Texto modelo en la sección H ({NCHARS} caracteres)",
     "『私の11月の1週間』について、150〜200字で書いてください。酉の市、相撲、紅葉の中から一つ選んでください。", instr="Redacción", size=13.8, gap=0)
f.para("例： " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ---- arashiyama image (col 3 slack below the exercises) ----
ix8 = COLX[3]
image(p, "arashiyama-temple.jpg", ix8, 710, CW, 290)
caption(p, ix8, 1000, CW,
        "京都・嵐山、天龍寺の紅葉。見頃は23日ごろからです。",
        "Foto: lumoplank — CC0 (Wikimedia Commons)")

# ================= 答え =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "答え　Respuestas: agrupadas por página; solo busca tu número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Una breve nota en español con cada respuesta　✓ = el ejercicio con texto modelo", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Redacción":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-tesuto.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model chars:", NCHARS)
