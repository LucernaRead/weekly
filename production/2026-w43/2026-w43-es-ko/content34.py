# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　문화", "La Lucerna", "A2 → B1　Las fiestas del otoño　가을 축제")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Fiestas de otoño: un puente partido en dos Españas", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: A2 → B1")
f.para("El domingo 1 de noviembre es el Día de Todos los Santos, una de las fiestas más queridas de España. Las familias van al cementerio, llevan flores a sus muertos y comen dulces de la temporada. Este año la fiesta cae en domingo — y ahí empieza el problema.")
f.para("Cuando una fiesta cae en domingo, algunas comunidades pasan el día libre al lunes. Este año, el lunes 2 de noviembre es festivo solo en nueve comunidades: Andalucía, Aragón, Asturias, Canarias, Castilla-La Mancha, Castilla y León, Extremadura, Madrid y Navarra. Allí, el fin de semana dura tres días: del 31 de octubre al 2 de noviembre.")
f.para("En las demás — Baleares, Cantabria, Cataluña, Galicia, Murcia, el País Vasco, La Rioja, la Comunitat Valenciana, Ceuta y Melilla — el lunes 2 es un día de trabajo normal. España se divide en dos: unos hacen puente y otros, no. Por eso estos días todos preguntan lo mismo: «¿El lunes es fiesta en mi comunidad?»")
f.para("La noche anterior, el sábado 31 de octubre, llega Halloween — una fiesta que viene de fuera, pero que ya es parte del otoño español, sobre todo para los niños. En la página 5 contamos qué disfraces busca España este año.")
f.para("Pero España también tiene sus fiestas propias para estas fechas. En Cataluña, la Castanyada: castañas asadas, boniatos y panellets, unos dulces pequeños de mazapán. En Galicia, el Samaín, una fiesta muy antigua de la noche de los muertos. Tres fiestas, una misma noche de otoño.")
f.gloss('el cementerio 묘지 · el dulce 단것 · festivo 쉬는 날 · el homenaje 추모 행사 · el mazapán 마지팬 (아몬드 반죽).')
f.head("RECORDAR JUNTOS　함께 기억해요", 24)  # D5 fix run1: head 25->24 (adv 436.8->419.3 vs CW 422.5)
f.para("El jueves 29 de octubre se cumplen dos años de la DANA de Valencia de 2024, la tormenta que dejó 233 muertos, según la cifra de las asociaciones de víctimas.")
f.para("Esta semana, Catarroja homenajeó a los servicios de emergencia y a los voluntarios de aquellos días, con unas 1.300 distinciones. Los representantes de las entidades locales han pedido que el día 29 no haya plenos en los ayuntamientos, para facilitar los actos de memoria. Desde La Lucerna, nos sumamos al recuerdo.")
f.end_report()

# col 3: chestnut image + facts + ¿Y tú? (sequential)
ix = COLX[3]
image(p, "castanas.jpg", ix, 200, CW, 430)
cy3 = caption(p, ix, 630, CW, "Castañas asadas, las protagonistas de la Castanyada: en Cataluña, la noche del 31 de octubre huele a castaña caliente y a boniato asado.",
              "Foto: Wikimedia Commons — CC0 (dominio público)")
facts = ["El lunes 2 de noviembre es festivo en 9 comunidades — y día de trabajo en las demás.",
         "En la Castanyada se comen castañas asadas, boniatos y panellets, dulces de mazapán.",
         "El Samaín gallego es una fiesta muy antigua: la noche de los muertos."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "TRES FIESTAS, UNA NOCHE", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Qué fiesta te gusta más: Halloween, la Castanyada o el Samaín? ¿Y qué comes ese día? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap('가장 좋아하는 축제는 뭐예요? 그날 무엇을 먹어요? 스페인어로 두 문장 써서 보내 주세요.', "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "가장 좋아하는 축제는 뭐예요? 그날 무엇을 먹어요? 스페인어로 두 문장 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　3면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "답은 8면에　문제는 급이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　¿VERDADERO O FALSO?", 25)
e.expl('3면 글을 읽고 참인지 거짓인지 판단하세요.')
e.ex("A2", '읽기 판단', "Verdadero", '모든 성인의 날은 11월 1일이에요',
     "El Día de Todos los Santos es el 1 de noviembre. ¿Verdadero o falso?", instr='참 / 거짓', size=20, gap=8)
e.ex("A2", '읽기 판단', "Falso", '월요일에 쉬는 자치주는 9곳뿐, 스페인 전역이 아니에요',
     "El lunes 2 de noviembre es festivo en toda España. ¿Verdadero o falso?", instr='참 / 거짓', size=20, gap=8)
e.ex("A2", '읽기 판단', "Verdadero", 'Castanyada에는 군밤과 panellets를 먹어요',
     "En la Castanyada se comen castañas asadas y panellets. ¿Verdadero o falso?", instr='참 / 거짓', size=20, gap=8)
e.ex("B1", '읽기 판단', "Falso", 'Samaín은 갈리시아의 오랜 축제예요',
     "El Samaín es el nombre gallego de Halloween. ¿Verdadero o falso?", instr='참 / 거짓', size=20, gap=8)
e.ex("A2", '읽기 판단', "Verdadero", '마드리드는 9개 자치주에 들어가고 주말이 사흘이에요',
     "En Madrid, el fin de semana del 31 al 2 dura tres días. ¿Verdadero o falso?", instr='참 / 거짓', size=20, gap=8)
e.head("B　PALABRAS DEL TEXTO", 25)
e.expl('상자 속 단어로 빈칸을 채우세요.')
e.para("flores · cementerio · festivo · castañas · puente", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", '문장 완성', "flores", '고인에게 가져가는 꽃 flores',
     "Las familias llevan ___ al cementerio.", instr='빈칸 채우기', size=20, gap=8)
e.ex("A2", '문장 완성', "cementerio", 'cementerio = 묘지',
     "El 1 de noviembre las familias van al ___.", instr='빈칸 채우기', size=20, gap=8)
e.ex("A2", '문장 완성', "festivo", 'festivo = 쉬는 날',
     "El lunes 2 es ___ en nueve comunidades.", instr='빈칸 채우기', size=20, gap=8)
e.ex("A2", '문장 완성', "castañas", 'castañas asadas 군밤',
     "En la Castanyada comemos ___ asadas.", instr='빈칸 채우기', size=20, gap=8)
e.ex("A2", '문장 완성', "puente", 'hacer puente 연휴를 만들다',
     "Con tres días libres, hacemos ___.", instr='빈칸 채우기', size=20, gap=8)
e.head("C　COMPRENSIÓN", 25)
e.expl('정답을 고르세요.')
e.ex("A2", '객관식', "B", '모든 성인의 날은 11월 1일이에요',
     "¿Cuándo es Todos los Santos? A. el 31 de octubre · B. el 1 de noviembre · C. el 2 de noviembre", size=20, gap=8)
e.ex("A2", '객관식', "A", '자치주 9곳이에요',
     "¿En cuántas comunidades es festivo el lunes 2? A. en nueve · B. en todas · C. en ninguna", size=20, gap=8)
e.ex("B1", '객관식', "B", 'Samaín은 갈리시아의 오래된 축제예요',
     "¿Qué es el Samaín? A. un dulce de mazapán · B. una fiesta gallega muy antigua · C. un disfraz", size=20, gap=8)
e.ex("B1", '객관식', "C", 'Catarroja는 이번 주 구조대와 자원봉사자를 표창했어요',
     "¿Qué pasó en Catarroja esta semana? A. un partido · B. una fiesta de Halloween · C. un homenaje a emergencias y voluntarios", size=20, gap=8)
e.head("D　CONSTRUIR FRASES", 25)
e.expl('단어를 바른 문장으로 만드세요.')
e.ex("A2", '문장 만들기', "Las familias llevan flores al cementerio.", '동사가 두 번째예요',
     "las familias / llevan / flores / al cementerio → ___", instr='문장 만들기', size=20, gap=8)
e.ex("B1", '문장 만들기', "El lunes es festivo en nueve comunidades.", '장소는 문장 끝에',
     "el lunes / es festivo / en nueve comunidades → ___", instr='문장 만들기', size=20, gap=8)
e.ex("B1", '문장 만들기', "En Cataluña comemos castañas asadas.", '장소가 앞에 와요',
     "en Cataluña / comemos / castañas asadas → ___", instr='문장 만들기', size=20, gap=8)
e.ex("B1", '문장 바꾸기', "Todos preguntan si el lunes es fiesta.", '간접 의문문은 si예요',
     "«¿El lunes es fiesta?» (todos preguntan) → ___", instr='바꿔 쓰기', size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · DEPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("DEPORTE　스포츠", "La Lucerna", "NIVEL B1　La semana del Clásico　엘 클라시코의 주")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("La semana del Clásico: Europa primero, el domingo a las 21:00", 32)
f.byline("De la redacción deportiva de La Lucerna　Nivel de lectura: B1")
f.para("¡Qué semana de fútbol! El martes y el miércoles se juega la jornada 3 de la Champions, y el domingo llega el partido más grande: el primer Clásico de la temporada, en el Camp Nou, a las 21:00.")
f.para("El martes fue una noche de 40 goles en Europa — y de malas noticias para el Barça. El PSG ganó 4–2 en París: fue la primera derrota azulgrana de la temporada. Doué marcó el primero; Espart empató; Lucas Hernández puso el 2–1 de cabeza; Yamal empató otra vez; y al final, Vitinha y Fabián Ruiz cerraron el 4–2.")
f.para("Los otros dos equipos españoles jugaron también el martes: el Liverpool ganó 4–3 al Villarreal en un partido loco, y el Atlético empató 1–1 en Stuttgart. El gol rojiblanco fue de Julián Álvarez, que cortó así una sequía de casi medio año sin marcar.")
f.para("Esta noche (21:00) juegan los otros dos equipos españoles: el Real Madrid recibe al RB Leipzig en el Bernabéu — la última prueba antes del Clásico — y el Real Betis recibe al Feyenoord en La Cartuja. Los resultados llegan después del cierre de esta edición: los contamos la próxima semana.")
f.para("Y el domingo, la gran pregunta no es solo quién gana. A las 21:00 empieza también la carrera de Fórmula 1 en Austin: Alonso y Sainz, empatados a siete puntos, corren a la misma hora que el Clásico. Este domingo, España elige: ¿fútbol o coches?")
f.gloss('la jornada 라운드 · el marcador 스코어 · empatar 비기다 · la sequía 골 가뭄 · cerrar el partido 경기를 마무리 짓다.')
f.end_report()

# col 3: Clásico data box + ¿Y tú? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX)
p.text(bx + 22, 240, "EL CLÁSICO EN DATOS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Domingo 25 de octubre, 21:00 · Spotify Camp Nou · Jornada 10 de LaLiga. El Barça llega líder, sin perder en la Liga. El Madrid de Mourinho llega a seis puntos, después de perder el derbi. El partido está declarado de alto riesgo, y LaLiga prepara una semana especial: «El 25 de octubre los astros se alinean».", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "¿Y tú? El domingo a las 21:00, ¿qué miras: el Clásico o la Fórmula 1? ¿Y quién gana el Clásico? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap('일요일 21:00에 어느 경기를 봐요? 엘 클라시코는 누가 이길까요? 스페인어로 두 문장 써서 보내 주세요.', "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "¿Y TÚ?　여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "일요일 21:00에 어느 경기를 봐요? 엘 클라시코는 누가 이길까요? 스페인어로 두 문장 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SEMANA EUROPEA Y EL GRAN DOMINGO　유럽 경기 주간과 대일요일", 26, "sans", True, OLIVE)
rows = [
    ("Mar 20.10.", "Champions · J3", "PSG 4–2 FC Barcelona — primera derrota azulgrana de la temporada"),
    ("Mar 20.10.", "Champions · J3", "Liverpool FC 4–3 Villarreal CF — un partido loco"),
    ("Mar 20.10.", "Champions · J3", "VfB Stuttgart 1–1 Atlético de Madrid (gol de Julián Álvarez)"),
    ("Mié 21.10.", "21:00", "Real Madrid – RB Leipzig (Bernabéu) · Real Betis – Feyenoord (La Cartuja)"),
    ("Vie–Dom", "F1 · Austin", "Entrenamientos el viernes · clasificación el sábado (23:00, hora peninsular)"),
    ("Dom 25.10.", "21:00", "EL CLÁSICO: FC Barcelona – Real Madrid (Camp Nou) + la carrera de F1 en Austin"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Atención: los partidos del miércoles terminan después del cierre de esta edición — por eso aquí son previa, sin resultados."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　4면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "답은 8면에　문제는 급이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　COMPRENSIÓN", 25)
e.expl('4면 글을 읽고 정답을 고르세요.')
e.ex("B1", '객관식', "A", '파리 생제르맹이 4–2로 이겼어요',
     "¿Cómo terminó el PSG – Barça? A. 4–2 para el PSG · B. 2–2 · C. 4–2 para el Barça", size=20, gap=8)
e.ex("B1", '객관식', "B", '훌리안 알바레스가 골을 넣었어요',
     "¿Quién marcó el gol del Atlético en Stuttgart? A. Vitinha · B. Julián Álvarez · C. Lamine Yamal", size=20, gap=8)
e.ex("B1", '객관식', "C", '비야레알이 리버풀에 4–3으로 졌어요',
     "El Villarreal perdió... A. 0–1 en casa · B. 2–2 · C. 4–3 en Liverpool", size=20, gap=8)
e.ex("B1", '객관식', "A", '일요일 21:00 엘 클라시코예요',
     "El Clásico se juega... A. el domingo a las 21:00 · B. el sábado a las 18:00 · C. el miércoles", size=20, gap=8)
e.ex("B1", '객관식', "B", '같은 시각에 F1 오스틴 레이스도 있어요',
     "El domingo a las 21:00 también hay... A. un concierto · B. la carrera de F1 en Austin · C. una fiesta", size=20, gap=8)
e.head("B　LAS PALABRAS", 25)
e.match_set("B1", '단어 짝짓기',
            ["el marcador", "la jornada", "el banquillo", "empatar"],
            ["el sitio del entrenador junto al campo",
             "el resultado de un partido, con los goles",
             "terminar un partido con el mismo resultado",
             "cada una de las rondas de una liga"],
            ["b", "d", "a", "c"],
            ['marcador=스코어 b', 'jornada=라운드 d', 'banquillo=벤치 a', 'empatar=비기다 c'],
            instr='단어와 뜻 짝짓기')
e.head("C　COMPARATIVOS", 25)
e.expl('괄호 속 단어의 비교급이나 -ísimo 형태로 빈칸을 채우세요.')
e.ex("B1", '문장 완성', "más grande", 'más + grande (엘 클라시코가 더 중요해요)',
     "El Clásico es ___ que un partido normal de Liga. (grande)", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "muchísimos", '골이 아주 많아요 (화요일 40골)',
     "El martes hubo ___ goles: ¡40 en toda Europa! (muchos)", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "peor", 'malo의 비교급은 peor예요',
     "El Barça tuvo su ___ (malo) noche de la temporada en París.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "mejor", 'bueno의 비교급은 mejor예요',
     "Alonso quiere su ___ (bueno) resultado del año en Austin.", instr='빈칸 채우기', size=20, gap=8)
e.head("D　EL PRETÉRITO INDEFINIDO", 25)
e.expl('문장을 과거형 (indefinido)으로 바꾸세요.')
e.ex("B1", '문장 바꾸기', "El PSG ganó 4–2 en París.", "ganar → ganó",
     "El PSG gana 4–2 en París. → ___", instr='바꿔 쓰기', size=20, gap=8)
e.ex("B1", '문장 바꾸기', "Lamine Yamal marcó el 2–2.", "marcar → marcó",
     "Lamine Yamal marca el 2–2. → ___", instr='바꿔 쓰기', size=20, gap=8)
e.ex("B1", '문장 바꾸기', "El Villarreal perdió 4–3 en Liverpool.", "perder → perdió",
     "El Villarreal pierde 4–3 en Liverpool. → ___", instr='바꿔 쓰기', size=20, gap=8)
e.ex("B1", '문장 바꾸기', "Julián Álvarez cortó su sequía.", "cortar → cortó",
     "Julián Álvarez corta su sequía. → ___", instr='바꿔 쓰기', size=20, gap=8)
e.ex("B1", '문장 바꾸기', "Los aficionados fueron al estadio.", 'ir의 과거형은 fueron이에요',
     "Los aficionados van al estadio. → ___", instr='바꿔 쓰기', size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-deporte.svg")
print("P4 saved, exercises so far:", len(REG))
