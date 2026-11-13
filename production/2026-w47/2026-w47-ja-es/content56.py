# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5　若者・エンタメ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("若者・エンタメ　青年", "Lucerna", "レベル B1　流行語30と紅葉の写真　30 palabras de moda y hojas de otoño")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P5-feature")
f.title("今年のことば、30語", 37)
f.byline("Lucerna編集部　読むレベル：B1")
f.para("「新語・流行語大賞」のノミネート30語が、5日（木よう日）に発表されました。今年の世の中を映すことばが、30語選ばれました。トップテンと大賞は、12月1日（火よう日）に発表されます。")
f.para("ノミネートには、『りくりゅう』があります。フィギュアスケートのペア、三浦璃来選手と木原龍一選手のことです。大ヒットした漫画『ちいかわ』も入っています。暑い日を表す『酷暑日』もあります。")
f.para("『好きすぎて滅！』は、M!LKの楽曲の名前です。『ボンボンドロップシール（ボンドロ）』は、シールの名前です。『AI暴走』や『NISA貧乏』など、暮らしを映すことばもあります。")
f.gloss("暮らし la vida　映す reflejar　世の中 la sociedad　楽曲 una canción.")
f.head("紅葉の写真", 25)
f.para("秋は、写真の季節でもあります。京都の嵐山では、23日ごろから紅葉が見頃になります。赤いカエデの写真を、SNSに上げる人も多いです。")
f.para("ことばと写真で、今年の秋を楽しみましょう。あなたの好きな今年のことばは、何ですか。")
f.gloss("上げる subir　季節 la estación.")
f.end_report()

# col 3: arashiyama image + words + numbers + あなた
ix = COLX[3]
image(p, "arashiyama-pond.jpg", ix, 200, CW, 290)
cy3 = caption(p, ix, 490, CW, "京都・嵐山、天龍寺の曹源池。紅葉の見頃は23日ごろからです。",
              "Foto: lumoplank — CC0 (Wikimedia Commons)")
words5 = ["りくりゅう — 三浦・木原のペア",
          "ちいかわ — 大ヒットした漫画の名前",
          "酷暑日 — とても暑い日のこと"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in words5) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "流行語のことば", 24, "sans", True, OLIVE)
yy3 += 52
for t in words5:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
nums5 = ["30 — ノミネートは30語です",
         "5 — ノミネートの発表は11月5日です",
         "1 — トップテンの発表は12月1日です"]
ny3 = sy3 + sh + 26
nh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in nums5) + 32
p.rect(ix, ny3, CW, nh, fill=BOX)
yy3 = ny3 + 16
p.text(ix + 22, yy3 + 26, "流行語の数字", 24, "sans", True, OLIVE)
yy3 += 52
for t in nums5:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = ny3 + nh + 26
etvous = "あなたは？今年のことば30語の中で、いちばん好きなことばはどれですか。日本語で2文、書いて、送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("¿Cuál de las 30 palabras de este año te gusta más? Escribe dos frases en japonés y envíanoslas.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？　Ahora tú", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "¿Cuál de las 30 palabras de este año te gusta más? Escribe dos frases en japonés y envíanoslas.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "練習　Ejercicios página 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8　Los niveles están mezclados — busca tu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　理解", 25)
e.bridge("第5版の文章を読んで、正しい答えを選んでください。")
e.ex("B1", "opción múltiple", "A", "30 nominaciones el jueves 5 de noviembre",
     "ノミネート30語が発表されたのはいつですか。 A. 11月5日　B. 11月19日　C. 12月1日", size=19, gap=6)
e.ex("B1", "opción múltiple", "A", "rikuryuu es una pareja de patinaje artístico",
     "りくりゅうは、何ですか。 A. スケートのペア　B. 映画の名前　C. シールの名前", size=19, gap=6)
e.ex("B1", "opción múltiple", "A", "Chiikawa es un manga de gran éxito",
     "「ちいかわ」は、何ですか。 A. 大ヒットした漫画　B. 相撲の技　C. お酒の名前", size=19, gap=6)
e.ex("B1", "opción múltiple", "C", "Top 10 y gran premio: 1 de diciembre",
     "トップテンと大賞はいつ発表されますか。 A. 11月5日　B. 11月19日　C. 12月1日", size=19, gap=6)
e.ex("B1", "opción múltiple", "B", "Las hojas de Arashiyama desde el 23 aproximadamente",
     "嵐山の見頃はいつごろからですか。 A. 19日　B. 23日ごろ　C. 12月1日", size=19, gap=6)
e.head("B　数字", 25)
e.bridge("第5版の数字を入れてください。")
e.ex("B1", "completa", "30", "Se nominaron 30 palabras",
     "ノミネートは ___ 語です。", instr="Completa", size=19, gap=6)
e.ex("B1", "completa", "5", "Las nominaciones se anunciaron el 5 de noviembre",
     "ノミネートは11月 ___ 日に発表されました。", instr="Completa", size=19, gap=6)
e.ex("B1", "completa", "1", "Top 10 el 1 de diciembre",
     "トップテンは12月 ___ 日に発表されます。", instr="Completa", size=19, gap=6)
e.ex("B1", "completa", "23", "Arashiyama: hojas desde el 23 nov.",
     "嵐山の見頃は11月 ___ 日ごろからです。", instr="Completa", size=19, gap=6)
e.ex("B1", "completa", "暑い", "酷暑日 = un día muy caluroso",
     "『酷暑日』は、とても ___ 日のことです。", instr="Completa", size=19, gap=6)
e.head("C　正しい・正しくない", 25)
e.bridge("正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "verdadero o falso", "○", "Se nominaron 30 palabras",
     "ノミネートは30語です。", instr="¿Verdadero o falso?", size=19, gap=6)
e.ex("B1", "verdadero o falso", "×", "El Top 10 aún no ha salido",
     "トップテンは、もう発表されました。", instr="¿Verdadero o falso?", size=19, gap=6)
e.ex("B1", "verdadero o falso", "×", "rikuryuu no es un título de película",
     "『りくりゅう』は、映画の名前です。", instr="¿Verdadero o falso?", size=19, gap=6)
e.ex("B1", "verdadero o falso", "○", "Las hojas de Arashiyama desde el 23 aproximadamente",
     "嵐山の見頃は、23日ごろからです。", instr="¿Verdadero o falso?", size=19, gap=6)
e.head("D　文を完成しましょう", 25)
e.bridge("第5版の文を完成してください。")
e.ex("B1", "completa", "選ばれ", "30 palabras reflejan la sociedad de este año",
     "今年の世の中を映すことばが、30語 ___ ました。", instr="Completa", size=19, gap=6)
e.ex("B1", "completa", "ペア", "rikuryuu es la pareja Miura Riku y Kihara Ryuichi",
     "『りくりゅう』は、三浦璃来選手と木原龍一選手の ___ です。", instr="Completa", size=19, gap=6)
e.ex("B1", "completa", "上げる", "Muchos suben fotos de arces rojos a las redes",
     "赤いカエデの写真を、SNSに ___ 人も多いです。", instr="Completa", size=19, gap=6)
e.ex("B1", "completa", "発表", "Top 10 el 1 de diciembre",
     "トップテンは、12月1日に ___ されます。", instr="Completa", size=19, gap=6)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-wakamono.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6　深読み (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("深読み　ふかよみ", "Lucerna", "レベル B2　紅葉は京都へ　Las hojas se van a Kioto")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P6-feature")
f.title("見頃を追いかけて京都へ", 37)
f.byline("Lucerna編集部　読むレベル：B2")
f.para("紅葉の見頃は、北から南へ、平地へ移っています。ウェザーニューズの10月29日の「第3回紅葉見頃予想」では、東京の高尾山は11月13日ごろ、広島の宮島は11月21日ごろ、京都の嵐山は11月23日ごろから見頃だそうです。")
f.para("嵐山の今の様子は、11月8日の時点で、全体の2割が色づき始めたところだそうです。ウェザーニューズの嵐山のページでは、見頃は11月26日ごろから、落葉はじめは12月12日ごろからと書かれています。")
f.para("日本気象株式会社の9月2日の予想では、東京の紅葉は11月29日ごろ、大阪は12月4日ごろです。どちらも、平年並みの予想です。予報の日にちは、見頃が始まる目安です。")
f.para("ただし、予想は会社によってちがいます。日本気象協会の予想では、嵐山の見頃は11月13日からです。見頃の決め方がちがうからです。日にちだけを見て、決めつけないようにしましょう。")
f.para("紅葉を見に行く人は、予報の日付と今の様子を、両方確かめましょう。京都の11月下旬は、朝晩が冷えます。暖かい服の準備も大切です。")
f.gloss("平地 la llanura　落葉はじめ las primeras hojas que caen　決めつける afirmar　確かめる comprobar.")
f.end_report()

# col 3: facts + words
ix = COLX[3]
facts6 = ["13 — 高尾山は11月13日ごろから見頃",
          "21 — 宮島は11月21日ごろから見頃",
          "23 — 嵐山は11月23日ごろから見頃",
          "12 — 嵐山の落葉はじめは12月12日ごろ"]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts6) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "今週の数字", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts6:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
words6 = ["追いかける — 後を追って行くこと",
          "見頃 — いちばん美しい時",
          "色づく — 葉の色が変わること"]
wy3 = sy3 + sh + 26
wh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in words6) + 32
p.rect(ix, wy3, CW, wh, fill=BOX)
yy3 = wy3 + 16
p.text(ix + 22, yy3 + 26, "紅葉のことば", 24, "sans", True, OLIVE)
yy3 += 52
for t in words6:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", wy3 + wh)

# ---- practice chart (full width) ----
chy = 1500
p.text(MX, chy + 26, "グラフを読もう　Leer el gráfico", 26, "sans", True, OLIVE)
p.text(RIGHT, chy + 26, "練習用データ　Datos de práctica", 21, "sans", True, OLIVE, anchor="end")
p.hline(MX, RIGHT, chy + 40, OLIVE, 2)
p.text(MX, chy + 78, "秋の休みに、どこへ行きたいですか（練習用データ — 実際の調査ではありません）", 22, "serif", True, INK)
chart = [("京都", 38), ("浅草", 24), ("高尾山", 22), ("家", 16)]
byy = chy + 104
for name, val in chart:
    p.text(MX, byy + 26, name, 22, "serif", False, INK)
    p.rect(MX + 250, byy, val * 30, 34, fill=OLIVE)
    p.text(MX + 250 + val * 30 + 16, byy + 26, f"{val}%", 22, "sans", True, INK)
    byy += 56
p.para(MX, byy + 22, "このグラフは練習用データです。数字は全部で100%になります。", 19.5, "serif", False, GREY, RIGHT - MX, 1.4)

# ---- P6 exercises ----
ey = 1900
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "練習　Ejercicios página 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respuestas en la página 8　Los niveles están mezclados — busca tu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　理解", 25)
e.bridge("第6版の文章を読んで、正しい答えを選んでください。")
e.ex("B2", "opción múltiple", "B", "Miyajima: hojas desde el 21 nov.",
     "宮島の見頃はいつごろからですか。 A. 11月13日　B. 11月21日ごろ　C. 12月9日", size=19, gap=6)
e.ex("B2", "opción múltiple", "B", "20 % de Arashiyama en color el 8 nov.",
     "嵐山の今の様子は、11月8日の時点でどうですか。 A. 全体が真っ赤です　B. 2割が色づき始めました　C. もう落葉しています", size=19, gap=6)
e.ex("B2", "opción múltiple", "B", "Arashiyama: hojas desde el 12 dic. aprox.",
     "嵐山の落葉はじめはいつごろからですか。 A. 11月23日　B. 12月12日ごろ　C. 12月4日", size=19, gap=6)
e.ex("B2", "opción múltiple", "A", "Asoc. Meteorológica de Japón: Arashiyama desde el 13 nov.",
     "日本気象協会の予想では、嵐山の見頃はいつからですか。 A. 11月13日から　B. 11月23日から　C. 12月9日から", size=19, gap=6)
e.ex("B2", "opción múltiple", "A", "Pronósticos distintos: definiciones distintas",
     "予想が会社によってちがうのは、どうしてですか。 A. 見頃の決め方がちがうから　B. 嵐山が2つあるから　C. 測る機械が壊れたから", size=19, gap=6)
e.head("B　グラフ", 25)
e.bridge("練習用データのグラフを見て答えてください。")
e.ex("B2", "completa", "京都", "Kioto encabeza el gráfico",
     "「行きたい場所」で1位は ___ です。", instr="Completa", size=19, gap=6)
e.ex("B2", "completa", "38", "El 38 % quiere ir a Kioto",
     "京都と答えた人は ___ %です。", instr="Completa", size=19, gap=6)
e.ex("B2", "completa", "24", "Asakusa: 24 %",
     "浅草は ___ %です。", instr="Completa", size=19, gap=6)
e.ex("B2", "completa", "14", "Kioto menos Asakusa: 14 %",
     "京都と浅草の差は ___ %です。", instr="Completa", size=19, gap=6)
e.ex("B2", "completa", "62", "38+24=62",
     "京都と浅草を合わせると ___ %です。", instr="Completa", size=19, gap=6)
e.ex("B2", "completa", "100", "Las cuatro suman: 100 %",
     "4つの数字を全部足すと ___ %になります。", instr="Completa", size=19, gap=6)
e.head("C　数字と事実", 25)
e.bridge("第6版の数字を入れてください。")
e.ex("B2", "completa", "13", "Monte Takao: desde el 13 nov.",
     "高尾山は11月 ___ 日ごろから見頃です。", instr="Completa", size=19, gap=6)
e.ex("B2", "completa", "29", "Las hojas de Tokio hacia el 29 de noviembre",
     "東京の紅葉は11月 ___ 日ごろです。", instr="Completa", size=19, gap=6)
e.ex("B2", "completa", "4", "Las hojas de Osaka hacia el 4 de diciembre",
     "大阪の紅葉は12月 ___ 日ごろです。", instr="Completa", size=19, gap=6)
e.ex("B2", "completa", "29", "El pronóstico de Weathernews era del 29 de octubre",
     "ウェザーニューズの予報は10月 ___ 日でした。", instr="Completa", size=19, gap=6)
e.head("D　正しい・正しくない", 25)
e.bridge("正しければ○、正しくなければ×を書いてください。")
e.ex("B2", "verdadero o falso", "○", "La temporada de hojas va del norte al sur",
     "紅葉の見頃は、北から南へ移ります。", instr="¿Verdadero o falso?", size=19, gap=6)
e.ex("B2", "verdadero o falso", "×", "El gráfico es un ejercicio, no una encuesta real",
     "グラフの数字は、本当の調査の結果です。", instr="¿Verdadero o falso?", size=19, gap=6)
e.ex("B2", "verdadero o falso", "×", "Pronósticos de Arashiyama: no coinciden",
     "嵐山の見頃の日にちは、どの会社も同じです。", instr="¿Verdadero o falso?", size=19, gap=6)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-fukayomi.svg")
print("P6 saved, exercises so far:", len(REG))
