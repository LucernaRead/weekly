# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P8: 38 exercises + registry-generated answers. Dash style, as W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS · 練習と答え", "La Lucerna", "8ページ · La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "B", "visita a Chequia = チェコへの遠征",
     "El jueves, la Roja ___ a Chequia en Praga. (A. recibe · B. visita)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "recibir a Inglaterra = イングランドをホームに迎える",
     "El domingo, España ___ a Inglaterra en Madrid. (A. visita · B. recibe)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "la lista = 招集リスト",
     "De la Fuente dio ___ el viernes 6. (A. la lista · B. la huelga)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "la huelga dura 24 horas = ストは24時間続く",
     "La huelga del miércoles ___ 24 horas. (A. empieza · B. dura)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "empieza la campaña = 選挙戦が始まる",
     "El viernes 13 ___ la campaña electoral. (A. empieza · B. termina)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "el sobre = 封筒",
     "El voto por correo llega en un ___. (A. puente · B. sobre)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "日曜はスペイン対イングランド",
     "El domingo se juega el ___ en el Metropolitano. (A. España–Inglaterra · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "veranillo = 小春日和",
     "En noviembre llega el ___ de San Martín. (A. veranillo · B. puente)", size=15.5, gap=1)
f.head("B · PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "選択問題", "B", "ゼネストは11月11日（水）",
     "La huelga general es el... A. lunes 9 · B. miércoles 11 · C. viernes 13", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "聖マルティンの日、11月11日",
     "San Martín es el... A. 11 de noviembre · B. 12 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "選択問題", "C", "スペイン対イングランドもストも今週",
     "Esta semana hay... A. solo fútbol · B. solo huelga · C. la huelga y el España–Inglaterra", size=15.5, gap=1)
f.ex("B1", "選択問題", "B", "マゴストでは焼き栗を食べる",
     "¿Qué se come en el magosto? A. flan · B. castañas asadas · C. chocolate", size=15.5, gap=1)
f.ex("B1", "選択問題", "A", "ストのスローガン：給料・住まい・物価",
     "El lema de la huelga es... A. «Salarios, vivienda y precios» · B. «Fútbol y fiesta» · C. «Cine y series»", size=15.5, gap=1)
f.ex("B1", "選択問題", "C", "総選挙は11月29日",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "選択問題", "B", "CIS住宅調査：住宅を心配する人は86.9%",
     "Según el CIS de vivienda, está preocupado el... A. 13,5 % · B. 86,9 % · C. 79 %", size=15.5, gap=1)
f.ex("B1", "選択問題", "A", "選挙戦は11月13日に始まる",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C · LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el miércoles 11 sigue la huelga en las noticias y el domingo ve el España–Inglaterra en el Metropolitano. Ana vive en Barcelona: el miércoles 11 trabaja, y el domingo ve el partido por televisión. Los dos leen los programas antes de votar el 29.", 16.5, lh=1.3, split=False)
f.ex("A2", "選択問題", "B", "パブロは日曜にメトロポリターノへ行く",
     "¿Quién ve el partido en el Metropolitano? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "アナは水曜に働く",
     "El miércoles 11, Ana... A. trabaja · B. va a la huelga · C. duerme", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "2人とも綱領を読んでから投票する",
     "Antes de votar, los dos... A. leen los programas · B. ven «Infamia» · C. viajan a Praga", size=15.5, gap=1)
f.ex("A2", "選択問題", "B", "見出しは2つの場所の対比をまとめる",
     "El mejor título es... A. «Una tormenta» · B. «Dos miércoles» · C. «El Clásico»", size=15.5, gap=1)
f.head("D · CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "文を作る", "El miércoles hay huelga general.", "主語 + 動詞 + 場所",
     "el miércoles / hay / huelga general → ___", instr="文を作る", size=15.5, gap=1)
f.ex("A2", "文を作る", "El domingo vemos el España–Inglaterra.", "時間が先",
     "el domingo / vemos / el España–Inglaterra → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "La campaña empieza a las cero horas.", "a las cero horas = 0時に",
     "la campaña / empieza / a las cero horas → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "¿A qué hora empieza el partido?", "疑問詞は文頭に",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="文を作る", size=15.5, gap=1)
f.head("E · TRADUCE", 22, OLIVE, 5)
f.ex("A2", "翻訳", "水曜、スペイン全土でゼネスト。", "原文と比べよう。",
     "El miércoles hay huelga general en toda España. → ___", instr="翻訳", size=15.5, gap=1)
f.ex("A2", "翻訳", "日曜、私たちはスペイン対イングランドを見る。", "原文と比べよう。",
     "El domingo vemos el España–Inglaterra. → ___", instr="翻訳", size=15.5, gap=1)
f.ex("B1", "翻訳", "El voto por correo llega a casa.", "llegar a casa = 家に届く",
     "郵便投票が家に届く。→ ___", instr="翻訳", size=15.5, gap=1)
f.ex("B2", "翻訳", "Cada gráfico tiene que llevar su fuente.", "tener que = 〜しなければならない",
     "すべてのグラフに出典を明記しなければならない。→ ___", instr="翻訳", size=15.5, gap=1)
f.head("F · LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "単語のペア",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo=世論調査 c", "muestra=標本 d", "margen de error=誤差の範囲 b", "junta electoral=選挙管理委員会 a"],
            instr="語と意味を結ぶ")
f.head("G · DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "A", "alquiler = 家賃",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "tres habitaciones = 3部屋",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "¿cuánto cuesta? = いくらですか",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "firmar = 署名する（契約書に）",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "mudanza = 引っ越し",
     "— La ___ es el miércoles 11, día de huelga. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H · ESCRIBE TÚ", 22, OLIVE, 5)
f.expl("作文問題（答えは一つではない）。模範文（84語）は下。")
f.ex("B1", "作文", "（自由な問題。模範文は下）", "模範文はこのページのH区（84語）",
     "«¿Qué harías tú por la vivienda?» Escribe 80–100 palabras: tu plan del miércoles 11, tu domingo 15 y tu voto del 29.", instr="作文", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y el miércoles 11 sigo la huelga en las noticias: salarios, vivienda y precios, los tres temas de la semana. "
          "El viernes 13 empieza la campaña, y el domingo 15 veo el España–Inglaterra con mi familia. "
          "El jueves 12 veo el Chequia–España en Praga por televisión, a las 20:45. "
          "Mis amigos de Barcelona no tienen huelga en su empresa: el miércoles trabajan. Yo, en cambio, leo los programas con calma y preparo mi voto por correo. "
          "El 29 votamos. ¡Qué semana!")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPUESTAS · 全解答と解説（1–8ページ）", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "各問に日本語の解説つき · ✓ は模範文のある問題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— {pg} ページ —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "作文":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
