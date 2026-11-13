# -*- coding: utf-8 -*-
# W47 ES core (VOL.4) — P3 flamenco & Santa Cecilia / P4 LaLiga J13. Fresh text, structure mirrors W46.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　文化", "La Lucerna", "A2 → B1　Flamenco y Santa Cecilia　フラメンコと聖セシリア")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("El flamenco cumple: del 16 de noviembre a Santa Cecilia", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: A2 → B1")
f.para("El lunes 16 de noviembre es el Día Internacional del Flamenco, y en España suena la guitarra en todos los rincones.")
f.para("La fecha recuerda el 16 de noviembre de 2010, cuando la UNESCO, en Nairobi, inscribió el flamenco en su Lista del Patrimonio Cultural Inmaterial de la Humanidad. No es solo un baile: es cante, toque y baile, con palmas, taconeo y compás.")
f.para("El flamenco nació del encuentro de muchas culturas en Andalucía: gitanos, andaluces, árabes, judíos. Y su palabra mágica es el duende: ese momento en que la música te toca por dentro y no sabes explicarlo.")
f.para("Y la música sigue: el domingo 22 es Santa Cecilia, la patrona de los músicos. Las bandas municipales y las sociedades musicales dan en noviembre su concierto del año: en Bilbao, la Banda Municipal toca el domingo 22 a las 12:00 en el Palacio Euskalduna. Noviembre es el mes de las bandas.")
f.gloss("el cante＝歌 · el toque＝ギター演奏 · el baile＝踊り · el compás＝リズム · el duende＝フラメンコの魂。")
f.head("LO QUE QUEDA DE NOVIEMBRE", 24)
f.para("El otoño sigue: las tardes cortas, la música en la calle y, en la agenda, una fecha que ya mira toda España: el domingo 29 de noviembre, las elecciones generales (página 6).")
f.end_report()

# col 3: flamenco image + facts + ¿Y tú? (sequential)
ix = COLX[3]
image(p, "flamenco_sargent.jpg", ix, 200, CW, 500)
cy3 = caption(p, ix, 700, CW, "«Bailaora española», cuadro de John Singer Sargent (1880–81): una bailaora con su mantón, el gesto que el mundo reconoce como flamenco.",
              "Cuadro: John Singer Sargent — dominio público (Wikimedia Commons)")
facts = ["El 16 de noviembre de 2010, la UNESCO declaró el flamenco Patrimonio Inmaterial de la Humanidad.",
         "El flamenco es cante, toque y baile, con palmas, taconeo y compás.",
         "El 22 de noviembre es Santa Cecilia: noviembre es el mes de las bandas de música."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "EL FLAMENCO, EN TRES DATOS", 23, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Has escuchado flamenco alguna vez? ¿Conoces la música de tu país que tiene duende? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("フラメンコを聞いたことがある？　あなたの国の音楽で、魂を感じるものは？　2文書いて送ろう。", "sans", False, 19, CW - 44)) * 27 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "フラメンコを聞いたことがある？　あなたの国の音楽で、魂を感じるものは？　2文書いて送ろう。", 19, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　3ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベル混合の問題もあります。番号で探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　¿VERDADERO O FALSO?", 25)
e.bridge("3ページの記事を読んで、正しいか間違いか正誤しよう。")
e.ex("A2", "正誤正誤", "Verdadero", "国際フラメンコの日、11月16日（月）",
     "El Día Internacional del Flamenco es el lunes 16 de noviembre. ¿Verdadero o falso?", instr="正誤", size=20, gap=8)
e.ex("A2", "正誤正誤", "Verdadero", "ユネスコが2010年にフラメンコを無形文化遺産に登録",
     "La UNESCO declaró el flamenco Patrimonio Inmaterial en 2010. ¿Verdadero o falso?", instr="正誤", size=20, gap=8)
e.ex("A2", "正誤正誤", "Falso", "フラメンコは踊りだけじゃない。歌とギターと踊りの三位一体。",
     "El flamenco es solo un baile. ¿Verdadero o falso?", instr="正誤", size=20, gap=8)
e.ex("B1", "正誤正誤", "Falso", "聖セシリアの日は11月22日。音楽の守護聖人。",
     "Santa Cecilia, patrona de la música, es el 16 de noviembre. ¿Verdadero o falso?", instr="正誤", size=20, gap=8)
e.ex("A2", "正誤正誤", "Verdadero", "ビルバオ市立楽団は22日（日）12:00に演奏",
     "La Banda Municipal de Bilbao toca el domingo 22 a las 12:00. ¿Verdadero o falso?", instr="正誤", size=20, gap=8)
e.head("B　PALABRAS DEL TEXTO", 25)
e.bridge("枠の中の言葉で空所を補おう。")
e.para("cante · baile · guitarra · palmas · compás", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "文の完成", "cante", "cante＝歌",
     "El flamenco es ___, toque y baile.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "baile", "baile＝踊り",
     "La bailaora mueve los brazos en el ___.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "guitarra", "guitarra＝ギター",
     "El toque es la ___ del flamenco.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "palmas", "palmas＝手拍子",
     "El público marca el ritmo con las ___.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "compás", "compás＝リズム",
     "Sin ___ no hay flamenco.", instr="空所補充", size=20, gap=8)
e.head("C　COMPRENSIÓN", 25)
e.bridge("正しい答えを選ぼう。")
e.ex("A2", "選択問題", "B", "ユネスコが2010年にナイロビで宣言",
     "¿Dónde declaró la UNESCO el flamenco Patrimonio? A. en Madrid · B. en Nairobi · C. en Sevilla", size=20, gap=8)
e.ex("A2", "選択問題", "A", "duendeは音楽が心に響く瞬間",
     "¿Qué es el duende? A. el momento en que la música te toca · B. un instrumento · C. un baile", size=20, gap=8)
e.ex("B1", "選択問題", "C", "フラメンコはアンダルシアの多文化の出会いから生まれた",
     "El flamenco nació del encuentro de culturas en... A. Madrid · B. Bilbao · C. Andalucía", size=20, gap=8)
e.ex("B1", "選択問題", "B", "フラメンコの日の次は11月29日の選挙",
     "Después del Día del Flamenco, la próxima gran fecha es... A. el puente · B. las elecciones del 29 · C. la Navidad", size=20, gap=8)
e.head("D　CONSTRUIR FRASES", 25)
e.bridge("言葉を並べて正しい文を作ろう。")
e.ex("A2", "文を作る", "El flamenco es cante, toque y baile.", "主語＋動詞＋叙述",
     "el flamenco / es / cante, toque y baile → ___", instr="文を作る", size=20, gap=8)
e.ex("B1", "文を作る", "En noviembre suena la guitarra en España.", "時間が先、動詞は2番目",
     "en noviembre / suena / la guitarra / en España → ___", instr="文を作る", size=20, gap=8)
e.ex("B1", "文を作る", "En Bilbao toca la banda el domingo.", "場所が先、動詞は2番目",
     "en Bilbao / toca / la banda / el domingo → ___", instr="文を作る", size=20, gap=8)
e.ex("B1", "文の書き換え", "Todos preguntan si hay duende.", "間接疑問文には si",
     "«¿Hay duende?» (todos preguntan) → ___", instr="書きかえ", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · DEPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("DEPORTE　スポーツ", "La Lucerna", "NIVEL B1　Vuelve la Liga: la jornada 13　リーガ再開：第13節")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Vuelve la Liga: la jornada 13, del viernes al lunes", 32)
f.byline("De la redacción deportiva de La Lucerna　Nivel de lectura: B1")
f.para("La Liga se para y vuelve: después del parón de selecciones, la jornada 13 se juega del viernes 20 al lunes 23 de noviembre.")
f.para("El Barça llega líder, con 33 puntos, después de ganar 1–2 al Atlético en el Metropolitano. El Real Madrid es segundo, con 30, y el Atlético tercero, con 28. La jornada 13 puede mover el liderato: el Barça recibe al Villarreal el domingo a las 14:00, y el Madrid recibe al Celta el sábado a las 21:00.")
f.para("El partido grande del sábado es el derbi sevillano, a las 18:30: Sevilla–Betis, un clásico de barrio que se juega con el corazón. Y el domingo a las 21:00, el Getafe recibe al Atlético en el Coliseum.")
f.para("Y la semana que viene vuelve Europa: la jornada 5 de la Champions, el martes 24 y el miércoles 25. El Madrid recibe al PSV el martes a las 21:00; el Barça visita al Sabah el miércoles a las 18:45 y el Atlético recibe al Viking a las 21:00. En la jornada 4, el Barça ganó 3–0 al Aston Villa, el Madrid 3–2 al AEK y el Atlético perdió 0–2 con el Bayern.")
f.gloss("la jornada＝節 · el derbi＝ダービー · el liderato＝首位 · el parón＝中断期間 · la fase liga＝リーグ戦。")
f.end_report()

# col 3: champions box + ¿Y tú? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX)
p.text(bx + 22, 240, "LA CHAMPIONS VUELVE", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "La semana que viene, la jornada 5: martes 24, Real Madrid–PSV, 21:00; miércoles 25, Sabah–Barça, 18:45, y Atlético–Viking, 21:00. También juegan el Villarreal y el Betis. En la jornada 4, el Barça ganó 3–0 y el Madrid 3–2; el Atlético perdió 0–2.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "¿Y tú? El sábado a las 18:30, ¿qué miras: el derbi sevillano o el Madrid–Celta? ¿Quién gana la Liga: el Barça o el Madrid? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("土曜18:30はどの試合を見る？　セビージャ・ダービーとレアル・マドリー対セルタ。リーガ優勝はバルサとレアル、どちら？　スペイン語で2文書いて送ろう。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "¿Y TÚ?　あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "土曜18:30はどの試合を見る？　セビージャ・ダービーとレアル・マドリー対セルタ。リーガ優勝はバルサとレアル、どちら？　スペイン語で2文書いて送ろう。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA JORNADA 13　LOS SEIS PARTIDOS DE LA SEMANA　第13節の6試合", 26, "sans", True, OLIVE)
rows = [
    ("VIE 20 · 21:00", "Athletic – Espanyol (abre la jornada, en San Mamés)"),
    ("SÁB 21 · 18:30", "Sevilla – Betis (el derbi sevillano)"),
    ("SÁB 21 · 21:00", "Real Madrid – Celta (en el Bernabéu)"),
    ("DOM 22 · 14:00", "Barcelona – Villarreal (el líder recibe al submarino)"),
    ("DOM 22 · 21:00", "Getafe – Atlético (el Atlético visita el Coliseum)"),
    ("LUN 23 · 21:00", "Levante – Elche (cierra la jornada 13)"),
]
yy = ty + 16
for i, (d, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Horarios en hora peninsular. La jornada 13 se juega del viernes 20 al lunes 23: estos son sus seis partidos clave; el resto de la jornada, en la web de LaLiga."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　4ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベル混合の問題もあります。番号で探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPRENSIÓN", 25)
e.bridge("記事を読んで正しい答えを選ぼう。")
e.ex("B1", "選択問題", "A", "バルサが33ポイントで首位",
     "El líder de la Liga es el... A. Barça, con 33 puntos · B. Real Madrid, con 33 · C. Atlético, con 28", size=20, gap=8)
e.ex("B1", "選択問題", "B", "第13節、11月20〜23日",
     "La jornada 13 se juega... A. el fin de semana del 8 · B. del viernes 20 al lunes 23 · C. en diciembre", size=20, gap=8)
e.ex("B1", "選択問題", "C", "セビージャ・ダービー、土曜18:30",
     "El derbi Sevilla–Betis es el sábado a las... A. 14:00 · B. 21:00 · C. 18:30", size=20, gap=8)
e.ex("B1", "選択問題", "A", "バルサ対ビジャレアル、日曜14:00",
     "El Barça–Villarreal se juega el domingo a las... A. 14:00 · B. 18:30 · C. 21:00", size=20, gap=8)
e.ex("B1", "選択問題", "B", "チャンピオンズリーグ第5節、11月24〜25日",
     "La jornada 5 de la Champions es... A. el 20–21 · B. el 24–25 · C. el 29–30", size=20, gap=8)
e.head("B　LAS PALABRAS", 25)
e.match_set("B1", "単語のペア",
            ["la jornada", "el derbi", "el liderato", "la fase liga"],
            ["el primer puesto de la clasificación",
             "un partido entre dos rivales de la misma ciudad",
             "una fecha del campeonato, con diez partidos",
             "la primera parte de la Champions, en formato liga"],
            ["c", "b", "a", "d"],
            ["jornada＝節 c", "derbi＝ダービー b", "liderato＝首位 a", "fase liga＝リーグ戦 d"],
            instr="語と意味を結ぶ")
e.head("C　COMPARATIVOS", 25)
e.bridge("比較級か -ísimo 形で補おう。")
e.ex("B1", "文の完成", "más importante", "más + importante（首位争いがより重要）",
     "El Barça–Villarreal es ___ que un amistoso. (importante)", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "muchísimos", "muchísimos aficionados＝とても多くのファン",
     "El Bernabéu espera a ___ aficionados. (muchos)", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "peor", "malo の比較級は peor",
     "Perder el derbi sería la ___ (malo) noticia de la semana.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "mejor", "bueno の比較級は mejor",
     "Ganar la jornada sería la ___ (bueno) noticia del otoño.", instr="空所補充", size=20, gap=8)
e.head("D　EL PRETÉRITO INDEFINIDO", 25)
e.bridge("過去形（pretérito indefinido）に直そう。")
e.ex("B1", "文の書き換え", "El Barça ganó 1–2 al Atlético.", "ganar → ganó",
     "El Barça gana 1–2 al Atlético. → ___", instr="書きかえ", size=20, gap=8)
e.ex("B1", "文の書き換え", "El Madrid recibió al Celta el sábado.", "recibir → recibió",
     "El Madrid recibe al Celta el sábado. → ___", instr="書きかえ", size=20, gap=8)
e.ex("B1", "文の書き換え", "El Atlético perdió 0–2 con el Bayern.", "perder → perdió",
     "El Atlético pierde 0–2 con el Bayern. → ___", instr="書きかえ", size=20, gap=8)
e.ex("B1", "文の書き換え", "La Liga volvió el viernes 20.", "volver → volvió",
     "La Liga vuelve el viernes 20. → ___", instr="書きかえ", size=20, gap=8)
e.ex("B1", "文の書き換え", "La jornada cerró el lunes 23.", "cerrar → cerró",
     "La jornada cierra el lunes 23. → ___", instr="書きかえ", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-deporte.svg")
print("P4 saved, exercises so far:", len(REG))
