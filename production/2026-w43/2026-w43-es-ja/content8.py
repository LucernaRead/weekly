# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-es-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS · 練習と答え", "La Lucerna", "8ページ · La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "B", "abrir el marcador = 先制点を決める",
     "Doué ___ el marcador en París. (A. cerró · B. abrió)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "poner el 1–1 = 同点ゴールを決める",
     "Espart ___ el 1–1 para el Barça. (A. perdió · B. puso)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "de cabeza = ヘディング",
     "Lucas Hernández marcó el 2–1 de ___. (A. cabeza · B. penalti)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "volver a + 原形 = もう一度…",
     "Yamal ___ a empatar: 2–2. (A. salió · B. volvió)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "cerrar el partido = 試合を決める",
     "Vitinha y Fabián Ruiz ___ el 4–2 al final. (A. abrieron · B. cerraron)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "derrota = 敗北",
     "Fue la primera ___ del Barça este año. (A. victoria · B. derrota)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "日曜にクラシコ開催",
     "El domingo se juega el ___ en el Camp Nou. (A. Clásico · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "camiseta = ユニフォーム",
     "El Barça lleva una ___ de GOLF WANG. (A. camiseta · B. bufanda)", size=15.5, gap=1)
f.head("B · PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "選択問題", "B", "日曜未明、03:00 が 02:00 に",
     "El cambio: a las... A. 02→03 · B. 03→02 · C. 00→01", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "カナリアは1時間少ない",
     "¿Dónde hay una hora menos? A. Canarias · B. Madrid · C. Barcelona", size=15.5, gap=1)
f.ex("A2", "選択問題", "C", "クラシコと F1 がどちらも21:00",
     "El domingo, 21:00: hay... A. solo fútbol · B. solo coches · C. los dos", size=15.5, gap=1)
f.ex("B1", "選択問題", "B", "Castanyada では panellets を食べる",
     "¿Qué dulce es de la Castanyada? A. flan · B. panellets · C. chocolate", size=15.5, gap=1)
f.ex("B1", "選択問題", "A", "Halloween は10月31日の土曜",
     "Halloween es... A. sáb. 31.10 · B. dom. 1.11 · C. lun. 2.11", size=15.5, gap=1)
f.ex("B1", "選択問題", "C", "総選挙は11月29日",
     "Las elecciones generales son el... A. 29.10 · B. 1.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "選択問題", "B", "二つの世論調査は混ぜてはならない",
     "¿Por qué no mezclamos las series? A. son secretas · B. métodos distintos · C. son viejas", size=15.5, gap=1)
f.ex("B1", "選択問題", "A", "DANA Adam は今季初の名前つきの嵐",
     "La DANA Adam es... A. la primera tormenta con nombre · B. una fiesta gallega · C. un equipo", size=15.5, gap=1)
f.head("C · LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Lucía vive en Sevilla: el lunes 2 es festivo en Andalucía y hace puente. Marta vive en Barcelona: en Cataluña el lunes 2 es laborable y trabaja. El sábado por la noche, Marta celebra la Castanyada con sus amigos: castañas y panellets.", 16.5, lh=1.3, split=False)
f.ex("A2", "選択問題", "B", "アンダルシアは祝日の名簿に入っている",
     "¿Quién hace puente? A. Marta · B. Lucía · C. las dos", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "カタルーニャでは月曜は仕事の日",
     "El lunes 2, Marta... A. trabaja · B. viaja · C. duerme", size=15.5, gap=1)
f.ex("A2", "選択問題", "C", "Castanyada では栗と panellets を食べる",
     "¿Qué comen Marta y sus amigos? A. flores · B. dulces de Halloween · C. castañas y panellets", size=15.5, gap=1)
f.ex("A2", "選択問題", "B", "タイトルが二つの土地の対比をまとめている",
     "El mejor título es... A. «Una tormenta» · B. «Dos lunes» · C. «El Clásico»", size=15.5, gap=1)
f.head("D · CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "文を作る", "El domingo dormimos una hora más.", "時刻が先に来る",
     "el domingo / dormimos / una hora más → ___", instr="文を作る", size=15.5, gap=1)
f.ex("A2", "文を作る", "El lunes es festivo en Madrid.", "主語 + 動詞 + 場所",
     "el lunes / es festivo / en Madrid → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "El Clásico empieza a las nueve.", "a las nueve = 9時に",
     "el Clásico / empieza / a las nueve → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "¿A qué hora empieza el partido?", "疑問詞は文頭に来る",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="文を作る", size=15.5, gap=1)
f.head("E · TRADUCE", 22, OLIVE, 5)
f.ex("A2", "翻訳", "日曜日は1時間長く眠れます。", "原文と照らし合わせる",
     "El domingo dormimos una hora más. → ___", instr="翻訳", size=15.5, gap=1)
f.ex("A2", "翻訳", "月曜日は9つの自治州で祝日です。", "原文と照らし合わせる",
     "El lunes es festivo en nueve comunidades. → ___", instr="翻訳", size=15.5, gap=1)
f.ex("B1", "翻訳", "El Clásico se juega el domingo a las nueve de la noche.", "se juega = 行われる／キックオフ",
     "クラシコは日曜の夜9時にキックオフ。→ ___", instr="翻訳", size=15.5, gap=1)
f.ex("B2", "翻訳", "Cada gráfico tiene que llevar su fuente.", "tener que = 〜しなければならない",
     "どのグラフにも出典を明記しなければなりません。→ ___", instr="翻訳", size=15.5, gap=1)
f.head("F · LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "単語のペア",
            ["el sondeo", "el indeciso", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "quien aún no sabe a quién votar"],
            ["c", "d", "b", "a"],
            ["sondeo=世論調査 c", "indeciso=未定の人 d", "margen de error=誤差の範囲 b", "junta electoral=選挙管理委員会 a"],
            instr="語と意味を結ぶ")
f.head("G · DIÁLOGO EN LA TIENDA", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "A", "disfraz = 仮装の衣装",
     "— Busco un ___ para mi hija. (A. disfraz · B. paraguas)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "Monster High は子どもに人気",
     "— Le encanta ___. (A. Monster High · B. el Samaín)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "¿cuánto cuesta? いくらですか",
     "— ¿Cuánto ___? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "pagar = 支払う",
     "— ¿Cómo va a ___: con tarjeta o en efectivo? (A. pagar · B. votar)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "ハロウィンは土曜日",
     "— Con tarjeta. La fiesta es el ___. (A. sábado · B. lunes)", size=15.5, gap=1)
f.head("H · ESCRIBE TÚ", 22, OLIVE, 5)
f.expl("作文問題（決まった答えはありません）。模範文（82語）は以下です。")
f.ex("B1", "作文", "（自由記述 — 模範文は以下）", "模範文はこのページの H 欄（82語）",
     "«¿El lunes 2 es festivo en tu comunidad?» Escribe 80–100 palabras: dónde vives, tu plan del 31 y del 1, y tu lunes.", instr="作文", size=15.5, gap=1)
MODELO = ("Vivo en Valencia, y aquí el lunes 2 de noviembre no es festivo: trabajo como un lunes normal. "
          "Mis amigos de Madrid sí hacen puente, ¡qué suerte! El sábado 31 celebro Halloween con mi familia, "
          "y el domingo llevamos flores al cementerio, como cada año. Por la tarde leo un libro en el sofá "
          "y preparo la semana con calma. El lunes, mientras Madrid descansa, yo abro la tienda a las nueve. "
          "No es justo… pero en diciembre, seguro, llega mi puente.")
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
