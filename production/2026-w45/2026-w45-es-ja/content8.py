# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-es-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS · 練習と答え", "La Lucerna", "8ページ · La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "B", "ganó 2–1 = 2–1で勝利",
     "El Madrid ___ 2–1 en el Camp Nou. (A. perdió · B. ganó)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "marcar dos goles = 2得点する",
     "Mbappé ___ dos goles en Barcelona. (A. paró · B. marcó)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "primera derrota liguera = リーグ初黒星",
     "Fue la primera ___ del Barça en la Liga. (A. derrota · B. victoria)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "recortar = 点差を縮める",
     "El Madrid ___ la distancia a tres puntos. (A. aumentó · B. recortó)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "acoger = 開催する（ベルナベウでのNFL開催）",
     "El Bernabéu ___ un partido de la NFL. (A. acoge · B. cierra)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "el emparrillado = アメフト場",
     "El Bernabéu cambia el césped por el ___. (A. puente · B. emparrillado)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "日曜はアトレティコ–バルサ戦",
     "El domingo se juega el ___ en el Metropolitano. (A. Atlético–Barça · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "himno = 国歌",
     "Antes del partido suenan dos ___: el de España y el de EE. UU. (A. himnos · B. puentes)", size=15.5, gap=1)
f.head("B · PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "選択問題", "B", "月曜に休みの自治州は9つ",
     "El lunes 2 es fiesta en... A. todas · B. nueve comunidades · C. ninguna", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "諸聖人の日11月1日",
     "Todos los Santos es el... A. 1 de noviembre · B. 2 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "選択問題", "C", "アトレティコ–バルサもNFLも日曜",
     "El domingo 8 hay... A. solo fútbol · B. solo NFL · C. la NFL y el Atlético–Barça", size=15.5, gap=1)
f.ex("B1", "選択問題", "B", "Castanyadaではpanelletsを食べる",
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", "選択問題", "A", "DANA追悼行事は10月29日（木）",
     "Los actos de memoria de la DANA fueron el... A. jueves 29 de octubre · B. sábado 31 · C. lunes 2", size=15.5, gap=1)
f.ex("B1", "選択問題", "C", "選挙は11月29日",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "選択問題", "B", "CIS10月調査：住宅55,7%",
     "Según el CIS de octubre, la vivienda es el principal problema para el... A. 20,9 % · B. 55,7 % · C. 17,1 %", size=15.5, gap=1)
f.ex("B1", "選択問題", "A", "選挙戦は11月13日に始まる",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C · LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el lunes 2 es festivo en su comunidad y hace puente. Ana vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El domingo por la tarde, Ana ve la NFL en televisión; por la noche, Pablo ve el Atlético–Barça.", 16.5, lh=1.3, split=False)
f.ex("A2", "選択問題", "B", "マドリードは休みのリストに入っている",
     "¿Quién hace puente? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "カタルーニャでは月曜は平日",
     "El lunes 2, Ana... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "AnaはNFLだけを見る；夜にアトレティコ–バルサを見るのはPablo",
     "El domingo, Ana ve... A. solo la NFL · B. solo el Barça · C. la NFL y, por la noche, el Atlético–Barça", size=15.5, gap=1)
f.ex("A2", "選択問題", "B", "見出しは二つの地域の対比をまとめる",
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D · CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "文を作る", "El lunes es festivo en Madrid.", "主語 + 動詞 + 場所",
     "el lunes / es festivo / en Madrid → ___", instr="文を作る", size=15.5, gap=1)
f.ex("A2", "文を作る", "El domingo vemos la NFL en el Bernabéu.", "時間が前",
     "el domingo / vemos / la NFL / en el Bernabéu → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "El Atlético–Barça empieza a las nueve.", "a las nueve = 9時に",
     "el Atlético–Barça / empieza / a las nueve → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "¿A qué hora empieza el partido?", "疑問詞は文頭に",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="文を作る", size=15.5, gap=1)
f.head("E · TRADUCE", 22, OLIVE, 5)
f.ex("A2", "翻訳", "月曜日は9つの自治州で祝日です。", "原文を参照",
     "El lunes es festivo en nueve comunidades. → ___", instr="翻訳", size=15.5, gap=1)
f.ex("A2", "翻訳", "日曜日はNFLとアトレティコ–バルサを見ます。", "原文を参照",
     "El domingo vemos la NFL y el Atlético–Barça. → ___", instr="翻訳", size=15.5, gap=1)
f.ex("B1", "翻訳", "El Bernabéu acoge un partido de la NFL.", "acoger = 開催する",
     "ベルナベウはNFLの試合を開催する。→ ___", instr="翻訳", size=15.5, gap=1)
f.ex("B2", "翻訳", "Cada gráfico tiene que llevar su fuente.", "tener que = ～しなければならない",
     "どのグラフにも出典を明記しなければならない。→ ___", instr="翻訳", size=15.5, gap=1)
f.head("F · LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "単語のペア",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo=世論調査 c", "muestra=標本 d", "margen de error=誤差範囲 b", "junta electoral=選挙管理委員会 a"],
            instr="語と意味を結ぶ")
f.head("G · DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "A", "alquiler = 家賃",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "tres habitaciones = 3部屋",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "¿cuánto cuesta? いくらですか",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "firmar = 署名する（契約に）",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "mudanza = 引っ越し",
     "— La ___ es el lunes 2, que es fiesta. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H · ESCRIBE TÚ", 22, OLIVE, 5)
f.expl("作文問題（決まった答えはありません）。模範文（84語）は以下です。")
f.ex("B1", "作文", "（自由記述 — 模範文は以下）", "模範文はこのページの H 欄（84語）",
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del puente y tu domingo 8.", instr="作文", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y aquí el lunes 2 de noviembre sí es festivo: hago puente con mi familia. "
          "El sábado 7 vemos el Valencia–Real Madrid en televisión, y el domingo 8 tenemos dos citas: por la tarde, la NFL en el Bernabéu, y por la noche, el Atlético–Barça. "
          "Mis amigos de Barcelona no tienen puente: el lunes trabajan. Yo, en cambio, descanso un día más y preparo la semana con calma. "
          "El viernes 13 empieza la campaña, y el 29 votamos todos. ¡Qué mes!")
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
