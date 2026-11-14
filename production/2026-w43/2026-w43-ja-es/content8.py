# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · テストと答え =================
CURPAGE[0] = 8
p = BSPage4()
p.band("テストと答え　Test y respuestas", "Lucerna", "第8面　週の大きなテスト + 全ての答え")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　週のクロニクル", 21, OLIVE, 5)
f.ex("B1", "Texto con huecos", "A", "El partido 1 es el sábado 24 de octubre",
     "日本シリーズの第1戦は、10月24日（___）です。(A. 土よう日 · B. 日よう日)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "A", "El último día de los Juegos Para Asiáticos también es el 24",
     "アジアパラ競技大会の最終日も、___ 日です。(A. 24 · B. 25)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "A", "El Jidai Matsuri fue el jueves 22 de octubre",
     "時代祭は、10月 ___ 日（木）でした。(A. 22 · B. 24)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "La venta general empezó el día 22 a las 12:00",
     "日本シリーズのチケットの一般発売は、___ 日12時でした。(A. 20 · B. 22)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "A", "Irohazaka: época ideal desde el viernes 23",
     "日光のいろは坂の見頃は、___ 日（金）からです。(A. 23 · B. 15)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "Geraldon sumó 1.342 puntos",
     "ジェラードンの合計点は、___ 点でした。(A. 671 · B. 1,342)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "A", "La Semana de la Lectura empieza el martes 27 de octubre",
     "読書週間は、10月 ___ 日（火）からです。(A. 27 · B. 31)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "B", "Halloween es el sábado 31 de octubre",
     "ハロウィンは、10月 ___ 日（土）です。(A. 30 · B. 31)", size=13.8, gap=0)
f.head("B　一般問題", 21, OLIVE, 5)
f.ex("A2", "Opción múltiple", "B", "45 países y regiones",
     "アジアパラ競技大会に参加した国と地域は？ A. 18 · B. 45 · C. 282", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "A", "282 deportistas japoneses",
     "日本の選手は何人でしたか。 A. 282人 · B. 120人 · C. 17人", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Tōyō: 10 h 31 min 30 s",
     "予選会で1位の東洋大学のタイムは？ A. 10時間31分30秒 · B. 1分46秒 · C. 9時間31分", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "1 min 46 s = 106 segundos",
     "法政大学は国士舘大学より何秒速かったですか。 A. 33秒 · B. 106秒 · C. 46秒", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "C", "Las reseñas de «餅» subieron un 168 %",
     "『餅』の口コミは何%増えましたか。 A. 82% · B. 84% · C. 168%", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "A", "Multa por tirar basura: 2.000 yenes",
     "渋谷でゴミを捨てた時の罰金は？ A. 2,000円 · B. 1,000万円 · C. 900円", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "La exposición del Shōsōin, hasta el 9 de noviembre",
     "正倉院展はいつまでですか。 A. 11月1日 · B. 11月9日 · C. 10月31日", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "C", "SoftBank: 91 victorias en la temporada",
     "ソフトバンクのレギュラーシーズンの勝ち数は？ A. 71 · B. 49 · C. 91", size=13.8, gap=0)
f.head("C　読んで答えましょう", 21, OLIVE, 5)
f.para("ケンは大学生です。今週の土よう日、横浜スタジアムで日本シリーズの第1戦があります。ケンはチケットを買うことができませんでしたから、テレビで応援します。日よう日は、奈良の正倉院展へ行くつもりです。来週の読書週間には、図書館で本を3冊借りたいと思っています。", 15, lh=1.3, split=False)
f.ex("A2", "Opción múltiple", "B", "Ken anima el sábado desde casa ante el televisor",
     "ケンは土よう日に何をしますか。 A. スタジアムへ行く · B. テレビで応援する · C. 奈良へ行く", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "B", "Porque no pudo comprar entradas",
     "ケンはなぜスタジアムへ行きませんか。 A. 時間がない · B. チケットが買えなかった · C. 雨だった", size=13.8, gap=0)
f.ex("A2", "Opción múltiple", "A", "El domingo va a la exposición del Shōsōin",
     "日よう日の予定は？ A. 正倉院展 · B. 図書館 · C. ハロウィン", size=13.8, gap=0)
f.ex("B1", "Opción múltiple", "B", "Quiere tomar prestados 3 libros",
     "読書週間に借りたい本は？ A. 2冊 · B. 3冊 · C. 9冊", size=13.8, gap=0)
f.head("D　文を作りましょう", 21, OLIVE, 5)
f.ex("A2", "Formar una frase", "私は土よう日に試合を見ます。", "Sujeto + tiempo + objeto + verbo",
     "私は / 土よう日に / 試合を見ます → ___", instr="Forma una frase", size=13.8, gap=0)
f.ex("A2", "Formar una frase", "紅葉は今週末が見頃です。", "見頃 = época ideal",
     "紅葉は / 今週末が / 見頃です → ___", instr="Forma una frase", size=13.8, gap=0)
f.ex("B1", "Formar una frase", "図書館で本を借ります。", "El lugar de la acción lleva «で»",
     "図書館で / 本を / 借ります → ___", instr="Forma una frase", size=13.8, gap=0)
f.ex("B1", "Formar una frase", "ジェラードンは1,342点で優勝しました。", "Puntos + で + 優勝",
     "ジェラードンは / 1,342点で / 優勝しました → ___", instr="Forma una frase", size=13.8, gap=0)
f.head("E　翻訳しましょう", 21, OLIVE, 5)
f.ex("A2", "Traducción", "La procesión sale del jardín imperial de Kioto a las 12.", "Ver página 3",
     "行列は京都御苑を12時に出発します。 → ___", instr="Traduce", size=13.8, gap=0)
f.ex("B1", "Traducción", "Tirar basura cuesta una multa de 2.000 yenes.", "Ver página 5",
     "ゴミを捨てると、2,000円の罰金です。 → ___", instr="Traduce", size=13.8, gap=0)
f.ex("B1", "Traducción", "読書週間は来週の火よう日から始まります。", "Ver página 7",
     "La Semana de la Lectura empieza el martes que viene. → ___", instr="Traduce", size=13.8, gap=0)
f.ex("B2", "Traducción", "私は池袋のハロウィンのイベントに行きたいです。", "Ver página 5 (el evento de Ikebukuro)",
     "Quiero ir al evento de Halloween de Ikebukuro. → ___", instr="Traduce", size=13.8, gap=0)
f.head("F　今週のことば", 21, OLIVE, 5)
f.match_set("B2", "Emparejar",
            ["見頃", "福袋", "行列", "勝率"],
            ["勝った割合（.650など）",
             "花や紅葉がいちばん美しい時",
             "中身が見えない本のセット",
             "昔の服を着た人の列"],
            ["b", "c", "d", "a"],
            ["見頃 = época ideal, b", "福袋 = bolsa sorpresa, c", "行列 = procesión, d", "勝率 = porcentaje de victorias, a"],
            instr="Une palabra y definición")
f.head("G　図書館で", 21, OLIVE, 5)
f.ex("B1", "Texto con huecos", "A", "見せてください = muéstremela, por favor",
     "— 本を借りたいです。— はい、カードを ___ ください。(A. 見せて · B. 見て)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "A", "借りられます = poder tomar prestado (forma potencial)",
     "— 3冊、___ か。 (A. 借りられます · B. 借りますた)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "A", "La Semana de la Lectura empieza el martes (página 7)",
     "— いつ返しますか。— 読書週間が始まる ___ に返します。(A. 火よう日 · B. 土よう日)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "A", "La bolsa sorpresa de libros es lo más popular",
     "— おすすめはありますか。— 『本の ___ 』が人気です。(A. 福袋 · B. 行列)", size=13.8, gap=0)
f.ex("B1", "Texto con huecos", "A", "どういたしまして = de nada",
     "— ありがとうございました。— ___ 。(A. どういたしまして · B. さようなら)", size=13.8, gap=0)
f.head("H　書いてみましょう", 21, OLIVE, 5)
MODELO = ("私の秋の週末は、スポーツと読書の週末です。"
          "土よう日は、友達と家で日本シリーズを見ます。私はDeNAを応援します。"
          "試合の後は、近くの公園へ紅葉を見に行きます。"
          "日よう日は、図書館で借りた本を読みます。"
          "読書週間も始まりますから、静かな場所で大きな冒険をしたいです。"
          "秋は短いですが、楽しいことが多い季節です。")
NCHARS = len(MODELO.replace(" ", ""))
f.expl(f"Ejercicio de redacción (sin respuesta única); el modelo ({NCHARS} caracteres) va a continuación.")
f.ex("B1", "Redacción", "(pregunta abierta — modelo a continuación)", f"El modelo está en la sección H de esta página ({NCHARS} caracteres)",
     "『私の秋の週末』について、150〜200字で書いてください。スポーツ、紅葉、読書の中から一つ選んでください。", instr="Redacción", size=13.8, gap=0)
f.para("例： " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 答え =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "答え　Respuestas — ordenadas por página, busca el número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Una breve explicación en español por respuesta　✓ = ejercicio con modelo", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Página {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
