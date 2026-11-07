# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-es-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · PORTADA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2 · SEGUNDA EDICIÓN", 23, "sans", True, OLIVE)
p.text(975, 92, "CADA SEMANA EN ESPAÑOL · 毎週一号 · スペイン人が読んでいるスペイン語を読む", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "SEMANA DEL 2 AL 8 DE NOVIEMBRE DE 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "La Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "ス ペ イ ン 語 週 刊 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL", 46, "serif", True, INK, anchor="middle")
p.text(975, 372, "スペイン語テキスト · 日本語の解説 — 日本語読者のための版", 19.5, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "¡LA VIVIENDA DECIDE LA CAMPAÑA!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Faltan 27 días para el 29-N: las listas están cerradas y los programas, en marcha.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "29-Nまであと27日 · 住宅が選挙戦を決める", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "今号のトップ · 詳しくは2・6ページ", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "LA NOTICIA · トップ記事", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "La cuenta atrás del 29-N: la vivienda decide la campaña", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "De la redacción de La Lucerna · Nivel de lectura: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("España entra en la semana decisiva antes de la campaña. Las listas ya están presentadas: ahora los partidos escriben sus programas.")
f.para("El domingo 29 de noviembre, España vota en elecciones generales. El presidente Pedro Sánchez disolvió las Cortes el 5 de octubre, después de que el Congreso rechazara dos decretos de vivienda el 2 de octubre. Entre el 21 y el 26 de octubre, los partidos presentaron sus candidaturas.")
f.para("¿Por qué la vivienda decide la campaña? Porque, según el barómetro de octubre del CIS, más de la mitad de los españoles la cita como el primer problema del país. Ningún otro tema llega tan alto (página 6).")
f.para("Y esta semana empieza con un descanso largo para millones de españoles: el lunes 2 es fiesta en nueve comunidades (página 2).")
f.para("El domingo 8, Madrid tiene dos citas: la NFL a las 15:30 y el Atlético–Barça a las 21:00.")
f.para("Esta es la segunda edición de La Lucerna en español: cada semana, la España real contigo. ¡Bienvenidos!")
f.expl("解説 — la cuenta atrás カウントダウン · disolver las Cortes 議会を解散する · el decreto 政令 · la candidatura 候補者リスト。")
f.box("LA SEMANA EN CIFRAS · 今週の数字", [
    ("27 — días faltan el lunes 2 para las elecciones del domingo 29（29日の選挙まで27日）", "serif", False, INK, 20.5, 1.35),
    ("9 — comunidades donde el lunes 2 de noviembre es fiesta（11月2日に休みの自治州）", "serif", False, INK, 20.5, 1.35),
    ("55,7 — % que cita la vivienda como el principal problema, según el CIS de octubre（10月のCISデータ）", "serif", False, INK, 20.5, 1.35),
])
f.head("AHORA TÚ · すぐ練習", 25)
f.ex("A2", "文の完成", "programas", "las listas ya están presentadas; ahora se escriben los programas",
     "Las listas ya están presentadas: ahora los partidos escriben sus ___.", size=20.5)
f.ex("A2", "文の完成", "29", "選挙は11月29日（日）",
     "España vota en elecciones generales el domingo ___ de noviembre.", size=20.5)
f.ex("A2", "文の完成", "vivienda", "住宅が選挙戦の決定的な争点",
     "La ___ decide la campaña del 29-N.", size=20.5)
f.ex("A2", "文の完成", "nueve", "月曜に休みの自治州は9つ",
     "El lunes 2 es fiesta en ___ comunidades.", size=20.5)
f.ex("B1", "文の完成", "21:00", "アトレティコ–バルサは日曜21:00キックオフ",
     "El Atlético–Barça del domingo se juega a las ___.", size=20.5)
f.ex("B1", "文の完成", "15:30", "NFLマドリード戦は日曜15:30キックオフ",
     "La NFL llega al Bernabéu el domingo a las ___.", size=20.5)
f.end_report()

# ---- claves de la semana (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "CINCO", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "CLAVES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "五大見どころ · Para entender la semana", 19, "sans", False, GREY)
gt = [
    ("La precampaña del 29-N", 250),
    ("El puente del lunes 2", 226),
    ("La semana europea", 196),
    ("Atlético–Barça, el domingo", 158),
    ("La NFL en el Bernabéu", 122),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE if i == 0 else GOLD)
    byy += 92
p.text(gx + 22, byy + 16, "Cinco claves, sin números", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "inventados: todo está explicado", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 68, "en esta edición.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 102, "五大見どころ：数字は作らず今号で説明。", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "EN ESTA EDICIÓN · 今号の目次", 24, "sans", True, OLIVE)
som = [
    ("Pág. 2", "El puente del lunes 2", "A2"),
    ("Pág. 3", "Tres noches de otoño", "A2→B1"),
    ("Pág. 4", "Europa y el domingo", "B1"),
    ("Pág. 5", "La NFL en Madrid", "B1"),
    ("Pág. 6", "La vivienda decide", "B2"),
    ("Pág. 7", "Fechas y promesas", "A2→B2"),
    ("Pág. 8", "Ejercicios y respuestas", "todos"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "LA PALABRA DE LA SEMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "« la precampaña » : los partidos cierran listas y escriben programas.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, "「プレキャンペーン」：正式選挙戦の前数週間。", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
p.rect(ix, iy, iw, 320, fill=BOX, stroke=LINE, sw=1.4)
illus_houses(p, ix + 188, iy + 30, s=2.2)
caption(p, ix, iy + 320, iw,
        "Casas, pisos y alquileres: la vivienda es el tema que decide la campaña del 29-N. En la página 6, los datos del CIS y el calendario completo hacia el 29 de noviembre. (Ilustración de la redacción, no una fotografía)",
        "Ilustración: La Lucerna")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-otono")
f2.head("UNA SEMANA, DOS ESPAÑAS", 25)
f2.para("El lunes, unos de puente y otros, a trabajar. El domingo, Madrid con dos citas a la vez. Entre medias, Europa y las listas: esta semana España vive a la vez su descanso y su campaña.", 22.5)
f2.para("Nuestro consejo para esta semana: lee el programa, no solo el titular. En la página 6 te enseñamos cómo.", 22.5)
f2.end_report()
# col 3 BREVES
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "BREVES · 短報", 24, "sans", True, OLIVE)
brefs = [
    ("EL PUENTE", "El lunes 2 es fiesta en 9 comunidades de 17. La lista completa, en la página 2."),
    ("EUROPA", "Champions el martes: Barça–Aston Villa, Atlético–Bayern y Villarreal–PSG. (Página 4)"),
    ("EL DOMINGO", "La NFL en el Bernabéu por la tarde y el Atlético–Barça por la noche. (Páginas 4 y 5)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "QUIZ RELÁMPAGO · クイズ", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "トップ記事を読んで、正しい答えを選ぼう · 答えは8ページ", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "選択問題", "C", "選挙は11月29日",
      "Las elecciones generales son el... A. 2 de noviembre · B. 13 de noviembre · C. 29 de noviembre", size=21)
qf.ex("A2", "選択問題", "B", "月曜に休みの自治州は9つ",
      "El lunes 2 es fiesta en... A. todas las comunidades · B. nueve comunidades · C. ninguna", size=21)
qf.ex("A2", "選択問題", "A", "NFLマドリード戦は日曜午後",
      "La NFL llega al Bernabéu el... A. domingo 8 · B. lunes 2 · C. viernes 6", size=21)
qf.ex("A2", "選択問題", "B", "アトレティコ–バルサは日曜21:00",
      "El Atlético–Barça se juega el domingo a las... A. 15:30 · B. 21:00 · C. 18:30", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-portada.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VIDA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIDA · 暮らし", "La Lucerna", "NIVEL A2 · El puente del lunes 2 · 11月2日の連休")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("El puente del lunes 2: tres días para unos, lunes normal para otros", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: A2")
f.para("El lunes 2 de noviembre es festivo en nueve comunidades — y día de trabajo en las demás.")
f.para("Las nueve son: Andalucía, Aragón, Asturias, Canarias, Castilla-La Mancha, Castilla y León, Extremadura, Madrid y Navarra. Allí, el fin de semana dura tres días: del sábado 31 de octubre al lunes 2 de noviembre. En las demás — Baleares, Cantabria, Cataluña, Galicia, Murcia, el País Vasco, La Rioja, la Comunitat Valenciana, Ceuta y Melilla — el lunes 2 es un día de trabajo normal.")
f.para("¿Por qué pasa esto? Porque el Día de Todos los Santos, el 1 de noviembre, cayó en domingo. Cuando una fiesta cae en domingo, algunas comunidades pasan el día libre al lunes. Por eso todos preguntan lo mismo: «¿El lunes es fiesta en mi comunidad?»")
f.para("Es la segunda semana con horario de invierno: anochece pronto y las tardes se hacen cortas. El puente, entonces, sabe mejor: tres días para descansar, leer y ver a la familia antes de una semana llena de fútbol y de precampaña.")
f.box("EL CALENDARIO · 今週のカレンダー", [
    ("Lunes 2 — puente en nueve comunidades; las candidaturas proclamadas llegan al BOE el martes 3（月曜は9州で連休；火曜に官報で正式候補を発表）", "serif", False, INK, 21, 1.36),
    ("Martes 3 — Champions: Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG（火曜はCLでスペイン勢3試合）", "serif", False, INK, 21, 1.36),
    ("Miércoles 4 — Champions: AEK–Real Madrid, 18:45（水曜はレアルがアテネでAEKと対戦）", "serif", False, INK, 21, 1.36),
    ("Jueves 5 — Europa League: Real Sociedad–Lyon, 18:45（木曜はレアル・ソシエダがELでリヨンと対戦）", "serif", False, INK, 21, 1.36),
    ("Viernes 6 — Liga, jornada 12: Sevilla–Alavés, 21:00（金曜はリーグ第12節が開幕）", "serif", False, INK, 21, 1.36),
    ("Sábado 7 — Valencia–Real Madrid, 21:00, en Mestalla（土曜はバレンシア対レアル）", "serif", False, INK, 21, 1.36),
    ("Domingo 8 — NFL en el Bernabéu, 15:30; Atlético–Barça, 21:00（日曜はNFLマドリード戦＋アトレティコ–バルサ）", "serif", False, INK, 21, 1.36),
])
f.head("DECIR LA FECHA", 25)
f.para("En español, la fecha se dice así: «el lunes 2 de noviembre». Primero el día de la semana, luego el número y luego el mes. Los días y los meses van en minúscula: lunes, noviembre. Y ojo: el primero del mes no es «el primero», es «el uno»: el 1 de noviembre.", 23)
f.gloss("festivo 休みの · el puente 連休 · la comunidad 自治州 · anochecer 日暮れ · el horario de invierno 冬時間。")
f.end_report()

# col 3: facts + ¿Y tú? (sequential, measured)
ix = COLX[3]
facts = ["El lunes 2 es festivo en 9 comunidades — y día de trabajo en las demás.",
         "Todos los Santos cayó en domingo 1: por eso algunas comunidades pasan la fiesta al lunes.",
         "Es la segunda semana con horario de invierno: anochece pronto."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "¿SABÍAS QUE…?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿El lunes 2 es fiesta en tu comunidad? ¿Qué haces con el puente: viajas, descansas o ves fútbol? Escribe dos frases en español y envíalas a la redacción: las mejores salen en la página 7, «Cartas de los lectores»."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("11月2日、あなたの地域は休みですか？連休は何をしますか：旅行、休養、それともサッカー観戦？スペイン語で2文書いて編集部に送ってください。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ? · あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "11月2日、あなたの地域は休みですか？連休は何をしますか：旅行、休養、それともサッカー観戦？スペイン語で2文書いて編集部に送ってください。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Decir la fecha wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "LOS DÍAS DE LA SEMANA · 日付の言い方", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "lunes 2 – domingo 8 de noviembre · 11月2日（月）～8日（日）", 20, "sans", False, GREY, anchor="end")
lx = MX
ly = dy + 58
for d, t in [
    ("lunes 2", "el lunes 2 — festivo en nueve comunidades"),
    ("martes 3", "el martes 3 — Champions y BOE"),
    ("miércoles 4", "el miércoles 4 — AEK–Real Madrid, 18:45"),
    ("jueves 5", "el jueves 5 — Real Sociedad–Lyon, 18:45"),
]:
    p.text(lx, ly + 24, d, 24, "serif", True, OLIVE)
    p.text(lx + 240, ly + 24, t, 21, "sans", False, GREY)
    ly += 36
ly = dy + 58
rx = MX + 910
for d, t in [
    ("viernes 6", "el viernes 6 — Sevilla–Alavés, 21:00"),
    ("sábado 7", "el sábado 7 — Valencia–Real Madrid, 21:00"),
    ("domingo 8", "el domingo 8 — NFL, 15:30; Atlético–Barça, 21:00"),
]:
    p.text(rx, ly + 24, d, 24, "serif", True, OLIVE)
    p.text(rx + 240, ly + 24, t, 21, "sans", False, GREY)
    ly += 36
p.para(lx, dy + 226, "Ojo: los días de la semana y los meses van en minúscula en español — lunes, noviembre — y el 1 del mes es «el uno», no «el primero».", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · 2ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ · レベル混合の問題もあります。番号で探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · LAS FECHAS", 25)
e.expl("正しい日付の形で文を完成させてください。")
e.ex("A2", "文の完成", "2", "11月2日（月）",
     "El puente es el lunes ___ de noviembre.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "8", "11月8日（日）",
     "El Atlético–Barça se juega el domingo ___ de noviembre.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "29", "選挙は11月29日",
     "Las elecciones generales son el ___ de noviembre.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "uno", "毎月1日は el uno と言う",
     "El Día de Todos los Santos es el ___ de noviembre.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "noviembre", "月は小文字",
     "El lunes 2 de ___ es festivo en nueve comunidades.", instr="空所補充", size=20, gap=8)
e.head("B · EL PRESENTE", 25)
e.expl("動詞の現在形を補ってください。")
e.ex("A2", "文の完成", "es", "el lunes → es（単数）",
     "El lunes 2 ___ festivo en Madrid.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "preguntan", "todos → preguntan",
     "Todos ___ lo mismo: «¿El lunes es fiesta?»", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "anochece", "anochecer → anochece",
     "En noviembre ___ pronto.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "descansamos", "nosotros → descansamos",
     "Con el puente, ___ tres días.", instr="空所補充", size=20, gap=8)
e.ex("A2", "文の完成", "dura", "el fin de semana → dura",
     "El fin de semana ___ tres días en Madrid.", instr="空所補充", size=20, gap=8)
e.head("C · COMPRENSIÓN", 25)
e.expl("2ページの記事を読んで、正しい答えを選んでください。")
e.ex("A2", "選択問題", "B", "月曜に休みの自治州は9つ",
     "¿En cuántas comunidades es festivo el lunes 2? A. en todas · B. en nueve · C. en ninguna", size=20, gap=8)
e.ex("A2", "選択問題", "A", "諸聖人の日11月1日は日曜",
     "Todos los Santos cayó en... A. domingo · B. lunes · C. sábado", size=20, gap=8)
e.ex("A2", "選択問題", "C", "カタルーニャでは月曜は平日",
     "El lunes 2, en Cataluña... A. es fiesta · B. hay puente · C. se trabaja", size=20, gap=8)
e.ex("B1", "選択問題", "B", "冬時間2週目、日暮れが早い",
     "Es la segunda semana con... A. horario de verano · B. horario de invierno · C. vacaciones", size=20, gap=8)
e.head("D · LAS PALABRAS", 25)
e.match_set("A2", "単語のペア",
            ["el puente", "festivo", "anochecer", "la comunidad"],
            ["día de fiesta, sin trabajo",
             "descanso largo de tres días",
             "hacerse de noche",
             "una región con gobierno propio"],
            ["b", "a", "c", "d"],
            ["puente=三日間の連休 b", "festivo=休みの a", "anochecer=日暮れ c", "comunidad=自治州 d"],
            instr="語と意味を結ぶ")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vida.svg")
print("P2 saved, exercises so far:", len(REG))
