# -*- coding: utf-8 -*-
# W47 ES core (VOL.4) — P5 first vote / P6 deep read. Fresh text, structure mirrors W46.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JUVENTUD (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUVENTUD　若者", "La Lucerna", "NIVEL B1　Votar por primera vez　初めての投票")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Votar por primera vez: el jueves 19 se cierra el plazo", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: B1")
f.para("¿Votas por primera vez el 29 de noviembre? Tienes dos maneras de votar: en persona o por correo.")
f.para("El voto por correo se pide desde la convocatoria y hasta el jueves 19 de noviembre, en cualquier oficina de Correos o por internet, en la web de Correos. La Oficina del Censo Electoral envía la documentación a la dirección indicada a partir del lunes 9 de noviembre. Después, votas en casa, con calma, y envías el sobre.")
f.para("Y si prefieres votar en persona, el domingo 29 los colegios electorales abren de 9:00 a 20:00, con tu documento de identidad. Novedad de este año: también vale identificarse con la aplicación oficial MiDNI en el móvil. La Junta Electoral Central levantó el 5 de noviembre la suspensión de la aplicación.")
f.para("Y el sábado 28, jornada de reflexión, no hay propaganda ni actos de campaña: un día de silencio antes de votar. Y el viernes 27, la otra cita joven de la semana: el Black Friday, con ofertas en las tiendas y en internet. Compra con cabeza: compara precios antes de pagar.")
f.box("EL PLAN DE LA SEMANA　今週の計画", [
    ("1. El lunes 16: Día del Flamenco y primer lunes de campaña（月曜：フラメンコの日と選挙戦最初の月曜）", "serif", False, INK, 21, 1.36),
    ("2. El jueves 19: último día para pedir el voto por correo（木曜：郵便投票の申請締め切り）", "serif", False, INK, 21, 1.36),
    ("3. El viernes 20: vuelve la Liga, Athletic–Espanyol, 21:00（金曜夜：リーガ再開）", "serif", False, INK, 21, 1.36),
    ("4. El sábado 21: derbi Sevilla–Betis, 18:30（土曜：セビージャ・ダービー）", "serif", False, INK, 21, 1.36),
    ("5. El domingo 22: Barça–Villarreal, 14:00; Santa Cecilia（日曜：バルサ対ビジャレアル；聖セシリアの日）", "serif", False, INK, 21, 1.36),
], tsize=20)
f.gloss("el sobre＝封筒 · la papeleta＝投票用紙 · el censo＝選挙人名簿 · el plazo＝期限 · la urna＝投票箱。")
f.end_report()

# col 3: ballot-box photo + facts + ¿Y tú?
ix = COLX[3]
image(p, "urna_small.jpg", ix, 200, CW, 520)
cy3 = caption(p, ix, 720, CW, "Una urna de votación en bronce, con la inscripción «Suffrage universel» (sufragio universal). Tu voto va a una urna como esta: por correo llega en un sobre y en persona la echas tú mismo el domingo 29, de 9:00 a 20:00.",
              "Foto: Jebulon — CC0 (dominio público, Wikimedia Commons)")
facts = ["El voto por correo se pide hasta el jueves 19: en Correos o por internet.",
         "Para votar en persona vale el DNI y también la aplicación oficial MiDNI.",
         "El Black Friday es el viernes 27: compara precios antes de pagar."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "VOTAR POR PRIMERA VEZ", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Votarías por correo o en persona? ¿Qué comprarías en el Black Friday: algo útil o un capricho? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("郵便投票にする？　それとも直接行く？　ブラックフライデーでは何を買う？　実用的なもの、それとも衝動買い？　2文書いて送ろう。", "sans", False, 19, CW - 44)) * 27 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　あなたは？", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "郵便投票にする？　それとも直接行く？　ブラックフライデーでは何を買う？　実用的なもの、それとも衝動買い？　2文書いて送ろう。", 19, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　5ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベル混合の問題もあります。番号で探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　COMPRENSIÓN", 25)
e.bridge("記事を読んで正しい答えを選ぼう。")
e.ex("B1", "選択問題", "B", "郵便投票は19日までに申請する",
     "El voto por correo se pide hasta... A. el lunes 9 · B. el jueves 19 · C. el domingo 29", size=20, gap=8)
e.ex("B1", "選択問題", "A", "書類は11月9日から届く",
     "La documentación del voto por correo llega desde... A. el lunes 9 · B. el viernes 13 · C. el sábado 28", size=20, gap=8)
e.ex("B1", "選択問題", "C", "投票所は9:00から20:00まで開いている",
     "El domingo 29, los colegios abren... A. todo el día · B. de noche · C. de 9:00 a 20:00", size=20, gap=8)
e.ex("B1", "選択問題", "B", "MiDNIは今年から投票時の身分証明に使える新しい方法",
     "Para votar en persona, este año también vale... A. un billete · B. la aplicación MiDNI · C. una entrada", size=20, gap=8)
e.ex("B1", "選択問題", "A", "ブラックフライデー、11月27日（金）",
     "El Black Friday es el... A. viernes 27 · B. lunes 16 · C. domingo 29", size=20, gap=8)
e.head("B　PALABRAS DEL TEXTO", 25)
e.bridge("枠の中の言葉で空所を補おう。注意：活用が必要な言葉もある。")
e.para("sobre · papeleta · censo · identidad · plazo · urna", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "文の完成", "correo", "correo = 郵便局／郵便の",
     "Pido el voto por ___.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "papeleta", "papeleta = 投票用紙",
     "En casa, relleno la ___.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "envío", "enviar の活用 → envío",
     "Después ___（不定形：enviar）el sobre.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "identidad", "documento de identidad = 身分証明書",
     "Para votar en persona llevo mi documento de ___.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "censo", "censo = 選挙人名簿",
     "La Oficina del ___ envía la documentación.", instr="空所補充", size=20, gap=8)
e.ex("B1", "文の完成", "plazo", "plazo＝期限（19日締め切り）",
     "El jueves 19 termina el ___ del voto por correo.", instr="空所補充", size=20, gap=8)
e.head("C　IR A + INFINITIVO", 25)
e.bridge("ir a + 不定詞で書きかえよう。")
e.ex("B1", "文の書き換え", "Voy a pedir el voto por correo.", "voy a＋不定形",
     "Pido el voto por correo. → ___", instr="書きかえ", size=20, gap=8)
e.ex("B1", "文の書き換え", "Vas a votar el domingo 29.", "vas a＋不定形",
     "Votas el domingo 29. → ___", instr="書きかえ", size=20, gap=8)
e.ex("B1", "文の書き換え", "Va a abrirse la urna a las 9:00.", "va a＋不定形",
     "La urna se abre a las 9:00. → ___", instr="書きかえ", size=20, gap=8)
e.ex("B1", "文の書き換え", "Van a comparar precios antes de pagar.", "van a＋不定形",
     "Comparan precios antes de pagar. → ___", instr="書きかえ", size=20, gap=8)
e.head("D　¿VERDADERO O FALSO?", 25)
e.ex("B1", "正誤正誤", "Verdadero", "郵便投票は Correos で申請する",
     "El voto por correo se pide en una oficina de Correos. ¿Verdadero o falso?", instr="正誤", size=20, gap=8)
e.ex("B1", "正誤正誤", "Falso", "静粛日は土曜28日で、日曜ではない",
     "La jornada de reflexión es el domingo 29. ¿Verdadero o falso?", instr="正誤", size=20, gap=8)
e.ex("B1", "正誤正誤", "Verdadero", "今年はMiDNIで身分確認して投票できる",
     "Este año se puede votar identificándose con MiDNI. ¿Verdadero o falso?", instr="正誤", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-juventud.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · A FONDO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("A FONDO　深掘り", "La Lucerna", "NIVEL B2　Leer la campaña: debates, programas y encuestas　選挙戦を読む：討論・政策・世論調査")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P6-main")
f.title("Leer la campaña: debates, programas y encuestas", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: B2　La política nacional española")
f.para("En campaña, no todo lo que se anuncia está cerrado.")
f.para("Al cierre de esta edición, el 10 de noviembre, solo hay un debate cerrado: el de portavoces de laSexta, el viernes 13 a las 21:30, con Ana Pastor. Van Carlos Cuerpo (PSOE), Juan Bravo (PP), Pablo Bustinduy (Frente Amplio) y José María Figaredo (Vox), a hablar de economía, con público en el plató.")
f.para("El debate de vivienda en la Cadena SER, el miércoles 18, ya está acordado (Rodríguez–Bravo), pero no se había publicado la hora al cierre de esta edición: acordado no es cerrado. El PP propone un cara a cara entre Sánchez y Feijóo para el lunes 16, y un debate a cuatro para el jueves 26; el lunes 9, PSOE y PP acuerdan que la Academia de Televisión organice los dos debates, pero las fechas, las horas y los participantes siguen sin cerrarse. Atresmedia convoca su propio debate a cuatro para el lunes 23, sin el PSOE confirmado. RTVE propone un debate a ocho, con los portavoces de los ocho grupos, para el lunes 23. Un debate «propuesto» no es un debate «cerrado»: la primera lección de esta página es leer el verbo.")
f.para("Una encuesta es una foto con margen de error, tomada en un día concreto.")
f.para("Y ojo con el calendario: del martes 24 al sábado 28 no se pueden publicar encuestas, y el sábado 28 es la jornada de reflexión. Hay poco tiempo de campaña y poco tiempo de silencio: el domingo 29, la única encuesta que no admite error: la votación, con papeletas de verdad.")
f.para("Leer un debate es fácil si preguntas tres cosas: ¿quién habla, de qué tema y con qué datos? El que promete sin datos promete humo.")
f.end_report()

# col 3: timeline + poll-reading box (sequential, measured)
bx = COLX[3]
steps = [
    "13 NOV. — Empieza la campaña; debate de portavoces en laSexta, 21:30.",
    "16 NOV. — El PP propone el cara a cara Sánchez–Feijóo (sin confirmar).",
    "18 NOV. — Debate sobre vivienda en la Cadena SER (Rodríguez–Bravo).",
    "19 NOV. — Termina el plazo para pedir el voto por correo.",
    "23 NOV. — Atresmedia convoca un debate a cuatro (sin el PSOE confirmado).",
    "23 NOV. — RTVE propone un debate a ocho, con los portavoces de los ocho grupos.",
    "24–28 NOV. — Prohibido publicar encuestas.",
    "26 NOV. — El PP propone un debate a cuatro de la Academia (sin fecha pactada).",
    "27 NOV. — Termina la campaña; el 28, jornada de reflexión.",
    "29 NOV. — España vota, de 9:00 a 20:00.",
]
tl_h = 68 + sum(len(wrap(t, "serif", False, 19, CW - 44)) * 19 * 1.35 + 29 for t in steps) + 20
p.rect(bx, 200, CW, tl_h, fill=BOX)
yy3 = 200 + 16
p.text(bx + 22, yy3 + 26, "EL CAMINO AL 29N", 24, "sans", True, OLIVE)
yy3 += 52
for t in steps:
    yy3 = p.para(bx + 22, yy3 + 19, t, 19, "serif", False, INK, CW - 44, 1.35) + 10
tl_end = 200 + tl_h
by3 = tl_end + 26
bb = ("Para leer cualquier debate, pregunta tres cosas: ¿quién habla? "
      "¿De qué tema? ¿Con qué datos? "
      "Sin esas tres respuestas, una promesa no dice casi nada.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f0eee5")
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LEER UN DEBATE", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh, "timeline box height", tl_h)

# ---- bar charts (RTVE free slots, JEC — honestly captioned) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, OLIVE, 2)
p.text(MX, gy + 10, "LOS MINUTOS GRATIS EN RTVE　minutos de propaganda por partido", 26, "sans", True, OLIVE)
rtve = [("PSOE", 45), ("PP", 45), ("Vox", 30), ("Frente Amplio", 30), ("Podemos", 15)]
bx1, bw_, bhh = MX, 2 * CW + GUT, 322
p.rect(bx1, gy + 28, bw_, bhh, fill=BOX)
p.text(bx1 + 22, gy + 68, "PROPAGANDA GRATIS EN RTVE　minutos", 21, "sans", True, INK)
yy = gy + 96
for lab, v in rtve:
    p.text(bx1 + 22, yy + 24, lab, 21, "serif", True, INK)
    p.rect(bx1 + 430, yy + 6, v * 6.4, 22, fill=OLIVE)
    p.text(bx1 + 448 + v * 6.4, yy + 24, f"{v} min", 20.5, "serif", False, INK)
    yy += 31
p.para(bx1 + 22, gy + bhh - 30, "Acuerdo de la Junta Electoral Central del 4 de noviembre: 195 minutos en total, del 13 al 27 de noviembre. Tres formaciones más tienen 10 minutos cada una: Frente Obrero, PCTE y SALF.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right column: the poll ban
rx = COLX[2]
p.rect(rx, gy + 28, 2 * CW + GUT, bhh, fill="#f0eee5")
p.text(rx + 22, gy + 68, "¿POR QUÉ NO HAY ENCUESTAS?", 21, "sans", True, INK)
yy = gy + 96
for lab, v in [("Prohibido publicar encuestas", 5), ("Días de campaña en total", 15), ("Días de silencio (reflexión)", 1)]:
    p.text(rx + 22, yy + 24, lab, 21, "serif", True, INK)
    p.rect(rx + 430, yy + 6, v * 6.4, 22, fill=OLIVE)
    p.text(rx + 448 + v * 6.4, yy + 24, f"{v}", 20.5, "serif", False, INK)
    yy += 31
p.para(rx + 22, gy + bhh - 30, "Del martes 24 al sábado 28 de noviembre no se pueden publicar encuestas. El sábado 28 es la jornada de reflexión: sin propaganda ni actos de campaña.", 17.5, "sans", False, GREY, 2 * CW + GUT - 44, 1.3)

# ---- P6 exercises ----
ey = 1940
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　6ページの練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答えは8ページ　レベル混合の問題もあります。番号で探してください", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEER LOS GRÁFICOS", 25)
e.bridge("グラフを見て正しい答えを選ぼう。")
e.ex("B2", "選択問題", "A", "PSOEとPPに無料45分ずつ",
     "El PSOE y el PP tienen en RTVE... A. 45 minutos · B. 30 minutos · C. 15 minutos", size=18.5, gap=2)
e.ex("B2", "選択問題", "B", "無料放送は合計195分",
     "La propaganda gratuita en RTVE suma... A. 120 minutos · B. 195 minutos · C. 45 minutos", size=18.5, gap=2)
e.ex("B2", "選択問題", "C", "Podemos：15分",
     "Podemos tiene en RTVE... A. 45 minutos · B. 30 minutos · C. 15 minutos", size=18.5, gap=2)
e.ex("B2", "選択問題", "A", "世論調査の発表禁止は5日間（11月24〜28日）",
     "Prohibido publicar encuestas durante... A. 5 días · B. 15 días · C. 1 día", size=18.5, gap=2)
e.ex("B2", "選択問題", "B", "45 − 30 = 15",
     "Entre el PSOE y Vox hay... A. 30 minutos · B. 15 minutos · C. 45 minutos", size=18.5, gap=2)
e.ex("B2", "選択問題", "C", "選挙管理委員会が公表した無料放送時間だけを出典付きで載せる",
     "La Lucerna publica aquí... A. una media mezclada · B. todos los sondeos · C. solo datos oficiales, con fuente", size=18.5, gap=2)
e.head("B　COMPRENSIÓN", 25)
e.ex("B2", "選択問題", "B", "11月10日時点で確定しているのは laSexta の討論だけ",
     "El único debate cerrado es... A. el cara a cara · B. el de laSexta · C. el debate a cuatro", size=18.5, gap=2)
e.ex("B2", "選択問題", "A", "laSextaの討論、11月13日（金）21:30",
     "El debate de portavoces es el... A. viernes 13, a las 21:30 · B. lunes 16 · C. jueves 26", size=18.5, gap=2)
e.ex("B2", "選択問題", "C", "「提案された」は「確定した」とは違う",
     "Un debate «propuesto» es... A. cerrado · B. en la tele · C. aún sin confirmar", size=18.5, gap=2)
e.ex("B2", "選択問題", "B", "世論調査は誤差のある写真で、ある一日に撮られたもの",
     "Según el texto, una encuesta es... A. un resultado final · B. una foto con margen de error · C. una promesa", size=18.5, gap=2)
e.head("C　EL SUBJUNTIVO", 25)
e.ex("B2", "文の完成", "tenga", "es posible que + 接続法：tenga",
     "Es posible que el debate ___ (tener) cuatro portavoces.", instr="空所補充", size=18.5, gap=2)
e.ex("B2", "文の完成", "sea", "es importante que + 接続法：sea",
     "Es importante que cada dato ___ (ser) claro.", instr="空所補充", size=18.5, gap=2)
e.ex("B2", "文の完成", "para que", "para que + 接続法（目的）",
     "Publicamos la fuente ___ todos puedan comprobarla.", instr="空所補充", size=18.5, gap=2)
e.ex("B2", "文の完成", "Aunque", "Aunque + 直説法（知っている事実）",
     "___ los debates difieren, ninguno miente.", instr="空所補充", size=18.5, gap=2)
e.head("D　PALABRAS DEL DEBATE", 25)
e.bridge("枠の中の言葉で補おう：sondeo · muestra · indecisos · margen de error")
e.ex("B2", "文の完成", "sondeo", "sondeo = 世論調査",
     "Un ___ pregunta a una muestra de ciudadanos.", instr="空所補充", size=18.5, gap=2)
e.ex("B2", "文の完成", "muestra", "muestra＝標本",
     "El sondeo preguntó a una ___ de ciudadanos.", instr="空所補充", size=18.5, gap=2)
e.ex("B2", "文の完成", "indecisos", "indecisos = 未定の人",
     "Los ___ todavía no saben a quién votar.", instr="空所補充", size=18.5, gap=2)
e.ex("B2", "文の完成", "margen de error", "margen de error = 誤差の範囲",
     "Toda encuesta tiene un ___.", instr="空所補充", size=18.5, gap=2)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-afondo.svg")
print("P6 saved, exercises so far:", len(REG))
