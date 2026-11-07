# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-es-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · 文化", "La Lucerna", "A2 → B1 · La semana pasada: tres noches de otoño · 上週的三個秋夜")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("La semana pasada: memoria, disfraces y flores", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: A2 → B1")
f.para("La semana pasada, España vivió tres noches seguidas de otoño. El jueves 29 de octubre, Valencia recordó a las víctimas de la DANA de 2024, dos años después de la tormenta. Fueron actos sobrios, de memoria y de homenaje, en los pueblos que más sufrieron.")
f.para("El sábado 31 llegó la noche de los disfraces. Halloween llenó las calles de niños y de monstruos de mentira; en Cataluña, la Castanyada puso castañas asadas, boniatos y panellets en la mesa; en Galicia, el Samaín recordó la fiesta más antigua de la noche de los muertos.")
f.para("Tres fiestas, una misma noche de otoño.")
f.para("Y el domingo 1, Día de Todos los Santos, las familias llevaron flores a los cementerios, como cada año. Después de tres noches de fiesta y de memoria, el lunes 2 llegó el puente para unos y el trabajo para otros (página 2).")
f.gloss("sobrio 克制的 · el homenaje 紀念表彰 · el disfraz 服裝（化裝） · el boniato 紅薯 · el cementerio 墓地。")
f.head("LO QUE QUEDA DEL OTOÑO", 25)
f.para("El otoño sigue: las tardes cortas, las castañas en la calle y, en la cocina, los primeros guisos de la temporada. Y en la agenda, una fecha que ya mira toda España: el domingo 29 de noviembre, las elecciones generales (página 6).")
f.end_report()

# col 3: chestnut image + facts + ¿Y tú? (sequential)
ix = COLX[3]
image(p, "castanas.jpg", ix, 200, CW, 430)
cy3 = caption(p, ix, 630, CW, "Castañas asadas, las protagonistas de la Castanyada: en Cataluña, la noche del 31 de octubre huele a castaña caliente y a boniato asado.",
              "Foto: Wikimedia Commons — CC0 (dominio público)")
facts = ["El jueves 29, Valencia recordó a las víctimas de la DANA de 2024, dos años después.",
         "El sábado 31 se juntaron Halloween, la Castanyada y el Samaín en una sola noche.",
         "El domingo 1, las familias llevaron flores a los cementerios."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "TRES NOCHES, UNA SEMANA", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Qué noche te gusta más: la del 29, la del 31 o la del 1? ¿Y qué comiste el 31? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你最喜歡哪一夜：29 日、31 日還是 1 日？31 日你吃了什麼？寫兩句寄來。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ? · 說說你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你最喜歡哪一夜：29 日、31 日還是 1 日？31 日你吃了什麼？寫兩句寄來。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · 第 3 版練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · ¿VERDADERO O FALSO?", 25)
e.expl("讀第 3 版文章，判斷對錯。")
e.ex("A2", "判斷對錯", "Verdadero", "DANA 紀念活動在 10 月 29 日週四",
     "Los actos de memoria de la DANA fueron el jueves 29 de octubre. ¿Verdadero o falso?", instr="判斷", size=20, gap=8)
e.ex("A2", "判斷對錯", "Verdadero", "Castanyada 吃烤栗子、紅薯和 panellets",
     "En la Castanyada se comen castañas asadas y panellets. ¿Verdadero o falso?", instr="判斷", size=20, gap=8)
e.ex("A2", "判斷對錯", "Falso", "Samaín 是加利西亞古節，不是萬聖節譯名",
     "El Samaín es el nombre gallego de Halloween. ¿Verdadero o falso?", instr="判斷", size=20, gap=8)
e.ex("B1", "判斷對錯", "Falso", "諸聖節在 11 月 1 日，不是 10 月 31 日",
     "El Día de Todos los Santos es el 31 de octubre. ¿Verdadero o falso?", instr="判斷", size=20, gap=8)
e.ex("A2", "判斷對錯", "Verdadero", "週日家屬去墓地獻花",
     "El domingo 1, las familias llevaron flores a los cementerios. ¿Verdadero o falso?", instr="判斷", size=20, gap=8)
e.head("B · PALABRAS DEL TEXTO", 25)
e.expl("用方框裡的詞填空。")
e.para("flores · cementerio · castañas · disfraz · memoria", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "完成句子", "flores", "給逝者帶花 flores",
     "Las familias llevan ___ a los cementerios.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "cementerio", "cementerio = 墓地",
     "El 1 de noviembre las familias van al ___.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "castañas", "castañas asadas 烤栗子",
     "En la Castanyada comemos ___ asadas.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "disfraz", "disfraz = 化裝服裝",
     "El 31 de octubre los niños llevan ___.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "memoria", "actos de memoria 紀念活動",
     "El 29 de octubre fueron actos de ___.", instr="填空", size=20, gap=8)
e.head("C · COMPRENSIÓN", 25)
e.expl("選出正確答案。")
e.ex("A2", "單選", "B", "DANA 紀念是 2024 年風暴兩週年",
     "¿Qué se recordó el jueves 29? A. un partido · B. la DANA de 2024 · C. una boda", size=20, gap=8)
e.ex("A2", "單選", "A", "Castanyada 在加泰羅尼亞",
     "¿Dónde se celebra la Castanyada? A. en Cataluña · B. en Galicia · C. en Madrid", size=20, gap=8)
e.ex("B1", "單選", "C", "Samaín 是加利西亞古老節日",
     "¿Qué es el Samaín? A. un dulce · B. un disfraz · C. una fiesta gallega muy antigua", size=20, gap=8)
e.ex("B1", "單選", "B", "三夜之後週一有人連假有人上班",
     "Después de las tres noches, el lunes 2... A. es fiesta en todas partes · B. unos hacen puente y otros trabajan · C. no pasa nada", size=20, gap=8)
e.head("D · CONSTRUIR FRASES", 25)
e.expl("把詞組成正確的句子。")
e.ex("A2", "造句", "Las familias llevan flores al cementerio.", "動詞第二位",
     "las familias / llevan / flores / al cementerio → ___", instr="造句", size=20, gap=8)
e.ex("B1", "造句", "El sábado comemos castañas asadas.", "時間在前，動詞第二",
     "el sábado / comemos / castañas asadas → ___", instr="造句", size=20, gap=8)
e.ex("B1", "造句", "En Galicia celebran el Samaín.", "地點在前，動詞第二",
     "en Galicia / celebran / el Samaín → ___", instr="造句", size=20, gap=8)
e.ex("B1", "句型轉換", "Todos preguntan si el lunes es fiesta.", "間接疑問用 si",
     "«¿El lunes es fiesta?» (todos preguntan) → ___", instr="改寫", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · DEPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("DEPORTE · 體育", "La Lucerna", "NIVEL B1 · Europa primero, el domingo a las 21:00 · 歐戰在先，週日晚九點")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Europa primero, el domingo a las 21:00", 37)
f.byline("De la redacción deportiva de La Lucerna · Nivel de lectura: B1")
f.para("El Madrid ganó 2–1 en el Camp Nou: fue la primera derrota liguera del Barça.")
f.para("El Clásico del domingo 25 ya tiene resultado: Kylian Mbappé marcó dos goles y el Real Madrid ganó 2–1 en Barcelona. El Barça, líder hasta entonces, perdió su primer partido de Liga; el Madrid de José Mourinho recortó la distancia a tres puntos. Ahora, una semana después, el Barça tiene su semana de respuesta: primero Europa, luego el Metropolitano.")
f.para("El martes 3 se juega la jornada 4 de la Champions: el Barça recibe al Aston Villa en el Camp Nou, el Atlético recibe al Bayern de Múnich y el Villarreal recibe al París Saint-Germain. El miércoles 4, a las 18:45, el Real Madrid visita al AEK de Atenas. Y el jueves 5, también a las 18:45, la Real Sociedad recibe al Olympique de Lyon en la Europa League.")
f.para("Y el fin de semana, la jornada 12 de Liga: el viernes 6 abre el Sevilla–Alavés (21:00); el sábado 7, el Valencia–Real Madrid en Mestalla (21:00); y el domingo 8, el Atlético–Barça en el Metropolitano (21:00). Entre medias, el domingo por la tarde, el Bernabéu cambia de deporte: la NFL llega a Madrid (página 5).")
f.gloss("la jornada 輪次 · recortar la distancia 縮小分差 · recibir 主場迎戰 · visitar 客場挑戰 · el Metropolitano 馬競主場。")
f.end_report()

# col 3: Clásico data box + ¿Y tú? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "EL CLÁSICO, UNA SEMANA DESPUÉS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Domingo 25 de octubre, 21:00 · Spotify Camp Nou · Jornada 10 de LaLiga. El Madrid ganó 2–1 con dos goles de Mbappé: primera derrota liguera del Barça. Una semana después, el Barça responde en Europa (martes, Aston Villa) y en el Metropolitano (domingo, Atlético).", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "¿Y tú? El domingo a las 21:00, ¿qué miras: el Atlético–Barça o la NFL? ¿Y quién gana en el Metropolitano? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("週日 21:00 你看哪一場？馬競主場誰贏？寫兩句西班牙語寄來。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "¿Y TÚ? · 說說你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "週日 21:00 你看哪一場？馬競主場誰贏？寫兩句西班牙語寄來。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SEMANA EUROPEA Y LA JORNADA 12 · 歐戰週與聯賽第 12 輪", 26, "sans", True, OLIVE)
rows = [
    ("Mar 3.11.", "Champions · J4", "FC Barcelona – Aston Villa · Atlético – Bayern · Villarreal – PSG"),
    ("Mié 4.11.", "18:45", "AEK Atenas – Real Madrid (Champions)"),
    ("Jue 5.11.", "18:45", "Real Sociedad – Olympique Lyon (Europa League)"),
    ("Vie 6.11.", "21:00", "Sevilla – Alavés (abre la jornada 12)"),
    ("Sáb 7.11.", "14:00–21:00", "Málaga – Racing · Espanyol – Deportivo · Osasuna – Athletic · Valencia – Real Madrid (21:00)"),
    ("Dom 8.11.", "14:00–21:00", "Elche – Betis · Real Sociedad – Rayo · Celta – Levante · Villarreal – Getafe · Atlético – Barça (21:00)"),
    ("Dom 8.11.", "15:30", "NFL EN EL BERNABÉU: Cincinnati Bengals – Atlanta Falcons (página 5)"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Horarios en hora peninsular. La jornada 12 completa, con todos los partidos del domingo, está en la tabla: el domingo 8 se juega también la NFL en el Bernabéu."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · 第 4 版練習", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPRENSIÓN", 25)
e.expl("讀第 4 版文章，選出正確答案。")
e.ex("B1", "單選", "A", "皇馬 2–1 贏下國家德比",
     "¿Cómo terminó el Clásico del 25? A. 2–1 para el Madrid · B. 2–2 · C. 2–1 para el Barça", size=20, gap=8)
e.ex("B1", "單選", "B", "姆巴佩進了兩球",
     "¿Quién marcó los dos goles del Madrid? A. Yamal · B. Mbappé · C. Mourinho", size=20, gap=8)
e.ex("B1", "單選", "C", "週二歐冠三場西甲球隊比賽",
     "El martes 3 juegan en Champions... A. solo el Barça · B. solo el Madrid · C. Barça, Atlético y Villarreal", size=20, gap=8)
e.ex("B1", "單選", "A", "週日 21:00 馬競–巴薩",
     "El Atlético–Barça se juega... A. el domingo a las 21:00 · B. el sábado a las 18:00 · C. el miércoles", size=20, gap=8)
e.ex("B1", "單選", "B", "週日下午還有 NFL 馬德里站",
     "El domingo por la tarde, en el Bernabéu, hay... A. un concierto · B. la NFL · C. una fiesta", size=20, gap=8)
e.head("B · LAS PALABRAS", 25)
e.match_set("B1", "詞彙配對",
            ["la jornada", "recibir", "visitar", "recortar"],
            ["jugar en casa, como local",
             "cada una de las rondas de una liga",
             "reducir una distancia en la tabla",
             "jugar fuera de casa"],
            ["b", "a", "d", "c"],
            ["jornada=輪次 b", "recibir=主場迎戰 a", "visitar=客場挑戰 d", "recortar=縮小分差 c"],
            instr="把詞和釋義配對")
e.head("C · COMPARATIVOS", 25)
e.expl("用括號裡詞的比較級或 -ísimo 形式填空。")
e.ex("B1", "完成句子", "más importante", "más + importante（馬競–巴薩更重要）",
     "El Atlético–Barça es ___ que un partido normal de Liga. (importante)", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "muchísimos", "muchísimos partidos 比賽很多",
     "El domingo hay ___ partidos: ¡toda la jornada 12! (muchos)", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "peor", "malo 的比較級是 peor",
     "El Barça sufrió su ___ (malo) noche de Liga en el Camp Nou.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "mejor", "bueno 的比較級是 mejor",
     "Mbappé firmó su ___ (bueno) noche del año en Barcelona.", instr="填空", size=20, gap=8)
e.head("D · EL PRETÉRITO INDEFINIDO", 25)
e.expl("把句子改成過去時（pretérito indefinido）。")
e.ex("B1", "句型轉換", "El Madrid ganó 2–1 en el Camp Nou.", "ganar → ganó",
     "El Madrid gana 2–1 en el Camp Nou. → ___", instr="改寫", size=20, gap=8)
e.ex("B1", "句型轉換", "Mbappé marcó dos goles.", "marcar → marcó",
     "Mbappé marca dos goles. → ___", instr="改寫", size=20, gap=8)
e.ex("B1", "句型轉換", "El Barça perdió su primer partido.", "perder → perdió",
     "El Barça pierde su primer partido. → ___", instr="改寫", size=20, gap=8)
e.ex("B1", "句型轉換", "Mourinho recortó la distancia.", "recortar → recortó",
     "Mourinho recorta la distancia. → ___", instr="改寫", size=20, gap=8)
e.ex("B1", "句型轉換", "Los aficionados fueron al estadio.", "ir 的過去時是 fueron",
     "Los aficionados van al estadio. → ___", instr="改寫", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-deporte.svg")
print("P4 saved, exercises so far:", len(REG))
