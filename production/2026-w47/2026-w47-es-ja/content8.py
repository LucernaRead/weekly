# -*- coding: utf-8 -*-
# W47 ES core (VOL.4) — P8: 38 exercises + registry-generated answers. Dash style, as W46.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS　練習と答え", "La Lucerna", "8ページ　La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "A", "el flamenco suena＝フラメンコが鳴る",
     "El lunes, el flamenco ___ en la calle. (A. suena · B. duerme)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "empieza la campaña = 選挙戦が始まる",
     "La campaña ___ el viernes 13. (A. termina · B. empieza)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "laSextaの討論 21:30",
     "El debate de laSexta fue a las ___. (A. 21:30 · B. 9:00)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "el voto por correo se pide hasta el jueves 19",
     "El voto por correo se pide hasta el ___. (A. jueves 19 · B. lunes 16)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "la Liga vuelve＝リーガが再開",
     "La Liga ___ el viernes 20. (A. vuelve · B. para)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "B", "セビージャ・ダービーは土曜日",
     "El derbi Sevilla–Betis es el ___. (A. domingo · B. sábado)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "Santa Cecilia＝音楽の守護聖人",
     "Santa Cecilia es la patrona de los ___. (A. músicos · B. futbolistas)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "スペインが投票する29日（日）",
     "El domingo 29, España ___. (A. vota · B. duerme)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "選択問題", "A", "選挙戦は11月13日（金）に始まる",
     "La campaña electoral empieza el... A. viernes 13 · B. lunes 16 · C. domingo 29", size=15.5, gap=1)
f.ex("A2", "選択問題", "B", "国際フラメンコの日、11月16日",
     "El Día del Flamenco es el... A. domingo 22 · B. lunes 16 · C. viernes 20", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "郵便投票は19日までに申請する",
     "El voto por correo se pide hasta... A. jueves 19 · B. viernes 20 · C. sábado 28", size=15.5, gap=1)
f.ex("B1", "選択問題", "C", "セビージャ・ダービー、土曜18:30",
     "El derbi Sevilla–Betis es el sábado a las... A. 14:00 · B. 21:00 · C. 18:30", size=15.5, gap=1)
f.ex("B1", "選択問題", "B", "ブラックフライデー、11月27日（金）",
     "El Black Friday es el... A. domingo 29 · B. viernes 27 · C. lunes 16", size=15.5, gap=1)
f.ex("B1", "選択問題", "C", "MiDNIは公式の身分確認アプリ",
     "MiDNI es... A. un billete · B. una entrada · C. una aplicación oficial", size=15.5, gap=1)
f.ex("B2", "選択問題", "B", "11月24〜28日は世論調査の発表なし",
     "No se publican encuestas del... A. 16 al 19 · B. 24 al 28 · C. 13 al 15", size=15.5, gap=1)
f.ex("B1", "選択問題", "C", "チャンピオンズリーグ第5節、11月24〜25日",
     "La jornada 5 de la Champions es el... A. 20–21 · B. 29–30 · C. 24–25", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Lucía vive en Sevilla: el sábado 21 ve el derbi Sevilla–Betis en el Sánchez-Pizjuán. Diego vive en Madrid: el sábado ve el Real Madrid–Celta en el Bernabéu. Los dos escuchan flamenco el lunes 16 y leen los programas antes de votar el 29.", 16.5, lh=1.3, split=False)
f.ex("A2", "選択問題", "A", "ルシアは土曜にセビージャでダービーを見る",
     "¿Quién ve el derbi en Sevilla? A. Lucía · B. Diego · C. los dos", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "ディエゴは土曜にレアル・マドリー対セルタを見る",
     "El sábado, Diego... A. ve el Madrid–Celta · B. ve el derbi · C. duerme", size=15.5, gap=1)
f.ex("A2", "選択問題", "A", "2人とも綱領を読んでから投票する",
     "Antes de votar, los dos... A. leen los programas · B. ven «Infamia» · C. viajan a Praga", size=15.5, gap=1)
f.ex("A2", "選択問題", "B", "タイトルは2つの都市と1つの土曜日をまとめる",
     "El mejor título es... A. «Una tormenta» · B. «Dos ciudades, un sábado» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "文を作る", "El lunes suena el flamenco.", "時間が先、動詞は2番目",
     "el lunes / suena / el flamenco → ___", instr="文を作る", size=15.5, gap=1)
f.ex("A2", "文を作る", "El sábado vemos el derbi.", "時間が先",
     "el sábado / vemos / el derbi → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "La campaña dura quince días.", "主語＋動詞＋時間",
     "la campaña / dura / quince días → ___", instr="文を作る", size=15.5, gap=1)
f.ex("B1", "文を作る", "¿A qué hora empieza el debate?", "疑問詞は文頭に",
     "¿ / a qué hora / empieza / el debate / ? → ___", instr="文を作る", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "翻訳", "月曜日は国際フラメンコの日。", "原文と比べよう。",
     "El lunes es el Día del Flamenco. → ___", instr="翻訳", size=15.5, gap=1)
f.ex("A2", "翻訳", "土曜日にセビージャ・ダービーを見る。", "原文と比べよう。",
     "El sábado vemos el derbi Sevilla–Betis. → ___", instr="翻訳", size=15.5, gap=1)
f.ex("B1", "翻訳", "El voto por correo se pide hasta el jueves 19.", "pedir hasta el jueves 19",
     "郵便投票は木曜19日までに申請しなければならない。→ ___", instr="翻訳", size=15.5, gap=1)
f.ex("B2", "翻訳", "Cada promesa tiene que llevar datos.", "tener que = 〜しなければならない",
     "約束はすべてデータに裏づけられなければならない。→ ___", instr="翻訳", size=15.5, gap=1)
f.head("F　LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "単語のペア",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo=世論調査 c", "muestra=標本 d", "margen de error=誤差の範囲 b", "junta electoral=選挙管理委員会 a"],
            instr="語と意味を結ぶ")
f.head("G　DIÁLOGO EN EL COLEGIO", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "A", "vengo a votar＝投票しに来た",
     "— Buenos días, vengo a ___. (A. votar · B. cantar)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "documento de identidad＝身分証明書",
     "— ¿Tiene su documento de ___? (A. identidad · B. puente)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "¿dónde está la urna? 投票箱はどこ？",
     "— ¿Dónde está la ___? (A. urna · B. guitarra)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "la papeleta va en el sobre＝投票用紙は封筒に入れる",
     "— La papeleta va en el ___. (A. sobre · B. derbi)", size=15.5, gap=1)
f.ex("B1", "穴埋め選択", "A", "¿a qué hora cierra el colegio? 投票所は何時に閉まる？",
     "— ¿A qué hora ___ el colegio? (A. cierra · B. canta)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.bridge("作文問題（正解は一つではない）。模範文（97語）は下。")
f.ex("B1", "作文", "（自由な問題。模範文は下）", "模範文はこのページのHを参照（97語）",
     "«¿Qué harías tú en la primera semana de campaña?» Escribe 80–100 palabras: tu lunes 16, tu viernes 20 y tu voto del 29.", instr="作文", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y el lunes 16 escucho flamenco en la calle: cante, toque y baile, la música de la semana. "
          "El viernes 13 empezó la campaña, y el domingo 29 voto por primera vez: pido el voto por correo hasta el jueves 19. "
          "El viernes 20 vuelve la Liga, y el sábado veo el derbi Sevilla–Betis con mi familia. "
          "El domingo 22 escucho a la banda de Santa Cecilia. "
          "Mis amigos de Barcelona no tienen duende en su barrio: el lunes trabajan. Yo, en cambio, leo los programas con calma y preparo mi voto. "
          "¡Qué semana!")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()
print("P8-ex flow ended y=", f.y)

# ---- P8 image: swan pen, in the free space of the last exercise column ----
iy8 = f.y + 24
ih8 = 240
image(p, "swan_pen.jpg", COLX[3], iy8, CW, ih8)
caption(p, COLX[3], iy8 + ih8, CW,
        "La pluma del escritor: esta página es para escribir. El texto modelo de arriba tiene 97 palabras: tu texto, entre 80 y 100.",
        "Pluma de cisne — dominio público (Wikimedia Commons)")
print("P8 image bottom approx", iy8 + ih8 + 90)

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1337, "RESPUESTAS　全解答と解説（1–8ページ）", 25, "sans", True, OLIVE)
p.text(RIGHT, 1337, "各問に日本語の解説つき　✓ は模範文のある問題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1363, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
print("MODELO words:", len(MODELO.split()))
