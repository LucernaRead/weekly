# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ja-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · テストと答え =================
CURPAGE[0] = 8
p = BSPage4()
p.band("テストと答え · Test y respuestas", "Lucerna", "第 8 面 · 週の大きなテスト + 全ての答え")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 週のクロニクル", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "La Semana de la Lectura termina el 9 de noviembre (lunes)",
     "読書週間は、11月9日（___）で終わります。(A. 月よう日 · B. 日よう日)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "El día de Pocky es el 11 de noviembre (miércoles)",
     "ポッキーの日は、11月11日（___）です。(A. 水よう日 · B. 金よう日)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "El partido 3 de las Japan Series fue el 27 de octubre (martes)",
     "日本シリーズの第3戦は、10月27日（___）でした。(A. 火よう日 · B. 水よう日)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Partido 4: SoftBank ganó 4-2",
     "第4戦は、ソフトバンクが ___ 対2で勝ちました。(A. 4 · B. 2)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "Shichi-Go-San se centra el 15 de noviembre (domingo)",
     "七五三の中心の日は、11月 ___ 日（日）です。(A. 9 · B. 15)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Las hojas del monte Takao culminan desde el 13 de noviembre (viernes)",
     "高尾山の見頃は、11月 ___ 日ごろからです。(A. 13 · B. 23)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "El día de Pocky empezó en 1999",
     "『ポッキー＆プリッツの日』は、___ 年に始まりました。(A. 1999 · B. 1989)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "El Ni-no-tori de Tori-no-ichi es el 19 de noviembre (jueves)",
     "二の酉は、11月 ___ 日です。(A. 19 · B. 7)", size=13.8, gap=0)
f.head("B · 一般問題", 21, OLIVE, 5)
f.ex("A2", "opción múltiple", "A", "Shichi-Go-San celebra a los niños de 3, 5 y 7 años",
     "七五三は、だれのお祝いですか。 A. 3歳・5歳・7歳の子ども · B. 大人 · C. お年寄り", size=13.8, gap=0)
f.ex("B1", "opción múltiple", "B", "Las visitas culminan a principios de noviembre (26 %), dice la encuesta",
     "調査では、お参りがいちばん多いのはいつですか。 A. 11月15日 · B. 11月上旬 · C. 12月", size=13.8, gap=0)
f.ex("B1", "opción múltiple", "A", "El MVP de la serie es Masaki Tomoya",
     "日本シリーズのMVPはだれですか。 A. 正木選手 · B. 山川選手 · C. 筒香選手", size=13.8, gap=0)
f.ex("B1", "opción múltiple", "A", "El 13.º título de SoftBank",
     "ソフトバンクは、何度目の日本一ですか。 A. 13度目 · B. 3度目 · C. 1度目", size=13.8, gap=0)
f.ex("A2", "opción múltiple", "A", "Chitose-ame es un caramelo largo rojo y blanco",
     "千歳飴は、どんな飴ですか。 A. 赤と白の長い飴 · B. 黒い丸い飴 · C. 緑の四角い飴", size=13.8, gap=0)
f.ex("B2", "opción múltiple", "A", "Las fechas previstas marcan el inicio de la mejor temporada",
     "紅葉の予報の日にちは、何ですか。 A. 見頃が始まる目安 · B. いちばん美しい日 · C. 落葉の日", size=13.8, gap=0)
f.ex("B2", "opción múltiple", "A", "El 74 % de las familias se hace fotos en un estudio, dice la encuesta",
     "写真館で撮る家庭は何%ですか。 A. 74% · B. 71% · C. 26%", size=13.8, gap=0)
f.ex("A2", "opción múltiple", "A", "El lema es 「静かだけど、冒険中。」",
     "読書週間のスローガンは？ A. 静かだけど、冒険中。 · B. 本の秋 · C. 紅葉の秋", size=13.8, gap=0)
f.head("C · 読んで答えましょう", 21, OLIVE, 5)
f.para("ユウは中学生です。今週の月よう日は、読書週間の最後の日です。ユウは図書館で借りた本を読みます。水よう日には、友達とポッキーを分けます。金よう日には、高尾山へ紅葉を見に行くつもりです。日よう日には、妹の七五三で神社へ行きます。", 15, lh=1.3, split=False)
f.ex("A2", "opción múltiple", "B", "El lunes lee un libro de la biblioteca",
     "ユウは月よう日に何をしますか。 A. 神社へ行く · B. 図書館で借りた本を読む · C. ポッキーを買う", size=13.8, gap=0)
f.ex("A2", "opción múltiple", "B", "El miércoles comparte Pocky con amigos",
     "水よう日に何をしますか。 A. 高尾山へ行く · B. 友達とポッキーを分ける · C. 神社へ行く", size=13.8, gap=0)
f.ex("A2", "opción múltiple", "A", "El viernes va al monte Takao a ver las hojas",
     "金よう日にどこへ行きますか。 A. 高尾山 · B. 神社 · C. 図書館", size=13.8, gap=0)
f.ex("B1", "opción múltiple", "B", "El domingo va a un santuario por el Shichi-Go-San de su hermana",
     "日よう日にどこへ行きますか。 A. 高尾山 · B. 神社 · C. 浅草", size=13.8, gap=0)
f.head("D · 文を作りましょう", 21, OLIVE, 5)
f.ex("A2", "construcción de frases", "私は水よう日に友達とポッキーを分けます。", "sujeto + tiempo + objeto + verbo",
     "私は / 水よう日に / 友達とポッキーを分けます → ___", instr="Construye una frase", size=13.8, gap=0)
f.ex("A2", "construcción de frases", "七五三は子どものお祝いです。", "七五三 = una celebración para niños",
     "七五三は / 子どもの / お祝いです → ___", instr="Construye una frase", size=13.8, gap=0)
f.ex("B1", "construcción de frases", "神社で千歳飴をもらいます。", "Usa 「で」 para el lugar",
     "神社で / 千歳飴を / もらいます → ___", instr="Construye una frase", size=13.8, gap=0)
f.ex("B1", "construcción de frases", "ソフトバンクは4連勝で日本一になりました。", "Cuatro victorias seguidas dieron el título",
     "ソフトバンクは / 4連勝で / 日本一になりました → ___", instr="Construye una frase", size=13.8, gap=0)
f.head("E · 翻訳しましょう", 21, OLIVE, 5)
f.ex("A2", "traducción", "Shichi-Go-San es el 15 de noviembre.", "Ver página 3",
     "七五三は11月15日です。 → ___", instr="Traduce", size=13.8, gap=0)
f.ex("B1", "traducción", "El día de Pocky empezó en 1999.", "Ver página 2",
     "『ポッキー＆プリッツの日』は1999年に始まりました。 → ___", instr="Traduce", size=13.8, gap=0)
f.ex("B1", "traducción", "読書週間は10月27日から始まります。", "Ver página 7",
     "La Semana de la Lectura empieza el 27 de octubre. → ___", instr="Traduce", size=13.8, gap=0)
f.ex("B2", "traducción", "紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。", "Ver página 6 (tras la mejor temporada)",
     "Quienes van a ver las hojas pueden ir tras la mejor temporada del norte al sur. → ___", instr="Traduce", size=13.8, gap=0)
f.head("F · 今週のことば", 21, OLIVE, 5)
f.match_set("B2", "relacionar",
            ["七五三", "千歳飴", "落葉", "見頃"],
            ["木から落ちた葉",
             "3歳・5歳・7歳の子どものお祝い",
             "紅葉がいちばん美しい時",
             "赤と白の長い飴"],
            ["b", "d", "a", "c"],
            ["七五三 = una celebración para niños de 3, 5 y 7 años b", "千歳飴 = caramelo largo rojo y blanco d", "落葉 = hojas caídas a", "見頃 = la mejor temporada c"],
            instr="Une palabras y sentidos")
f.head("G · 神社で", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "お参りします = ir a rezar",
     "— 七五三ですね。— はい、神社へ ___ ます。(A. お参りに行き · B. お参りに行か)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "撮ります = hacer una foto",
     "— 写真を ___ か。 (A. 撮ります · B. 撮った)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Shichi-Go-San se centra el 15 de noviembre (página 3)",
     "— 七五三はいつですか。— 11月 ___ 日です。(A. 15 · B. 9)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "千歳飴 es popular",
     "— おすすめはありますか。— 『___ 』が人気です。(A. 千歳飴 · B. ポッキー)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "どういたしまして = de nada",
     "— ありがとうございました。— ___ 。(A. どういたしまして · B. さようなら)", size=13.8, gap=0)
f.head("H · 書いてみましょう", 21, OLIVE, 5)
MODELO = ("私の11月の1週間は、本と秋の1週間です。"
          "月よう日は、読書週間の最後の日です。図書館で借りた本を読みます。"
          "水よう日は、友達とポッキーを分けます。1が4つ並ぶ日です。"
          "金よう日は、高尾山へ紅葉を見に行きます。"
          "日よう日は、妹の七五三です。神社へ行って、写真を撮ります。"
          "11月は短いですが、楽しいことが多い季節です。")
NCHARS = len(MODELO.replace(" ", ""))
f.bridge(f"Tarea de redacción (sin una única respuesta correcta); el texto modelo ({NCHARS} caracteres) está abajo.")
f.ex("B1", "redacción", "(tarea abierta: texto modelo abajo)", f"Texto modelo en la sección H de esta página ({NCHARS} caracteres)",
     "『私の11月の1週間』について、150〜200字で書いてください。読書、七五三、紅葉の中から一つ選んでください。", instr="Redacción", size=13.8, gap=0)
f.para("例： " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 答え =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答え · Respuestas: agrupadas por página; solo busca tu número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Una breve nota en español con cada respuesta · ✓ = el ejercicio con texto modelo", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 12.9, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "redacción":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 12.9, lh=1.13, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-tesuto.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model chars:", NCHARS)
