# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JUVENTUD (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUVENTUD　청소년", "La Lucerna", "NIVEL B1　Disfraces, camisetas y pantallas　의상　유니폼　화면")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Pantallas y disfraces: así se prepara España para Halloween", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: B1")
f.para("Faltan diez días para Halloween, y España ya busca su disfraz. Según los datos de idealo.es de principios de octubre, los adultos buscan sobre todo disfraces de La Catrina, de Pennywise, de los años 70 y 80, de Michael Myers y de Maléfica. Para los niños, lo más buscado es Monster High y el éxito del año: K-Pop Demon Hunters.")
f.para("El susto también viene en pantalla grande. Este otoño, las salas de cine estrenan películas de terror para todos los gustos — y el sábado 31, mucha gente va a celebrar Halloween en el cine o en casa, con amigos.")
f.para("El fútbol también tiene su fiesta de Halloween: la camiseta del Clásico. Para el partido del domingo, el Barça lleva en el pecho el logo GOLF WANG, de Tyler, the Creator. La camiseta se estrena primero con el equipo femenino, el sábado 24, y en el juego eFootball se puede jugar con ella desde el viernes 23. Un cantante en la camiseta del partido más grande: la música y el fútbol se cruzan otra vez.")
f.para("Y no todo es pantalla: el viernes pasado se estrenó en los cines El mal hijo, el primer largometraje de Jaime Lorente, un drama rural rodado entre Murcia y Canarias. Una historia de familia, lejos de los disfraces: el cine español también tiene su otoño serio.")
f.para("Halloween se junta este año con las fiestas propias de España — la Castanyada y el Samaín (página 3). Cada lector elige su noche: ¿disfraz, castañas o las dos?")
f.box("EL PLAN DEL SÁBADO 31", [
    ('1. Por la mañana: compra el disfraz en la tienda (오전에 가게에서 의상을 사요)', "serif", False, INK, 21, 1.36),
    ('2. Por la tarde: cine de terror con amigos (오후에 친구와 공포 영화를 봐요)', "serif", False, INK, 21, 1.36),
    ('3. Por la noche: fiesta de Halloween (밤에 Halloween 파티에 가요)', "serif", False, INK, 21, 1.36),
    ('4. O la opción tranquila: castañas asadas en casa (아니면 조용히 집에서 군밤을 먹어요)', "serif", False, INK, 21, 1.36),
    ('5. El domingo 1: flores y familia, el Día de Todos los Santos (일요일 1일은 모든 성인의 날: 꽃과 가족)', "serif", False, INK, 21, 1.36),
])
f.gloss('el disfraz (변장) 의상 · el susto 깜짝 놀람 · estrenar 처음 선보이다 · el largometraje 장편 영화 · rodado 촬영된.')
f.end_report()

# col 3: halloween image + facts + ¿Y tú?
ix = COLX[3]
image(p, "halloween1910.jpg", ix, 200, CW, 290)
cy3 = caption(p, ix, 490, CW, "Una postal de Halloween de hacia 1909: la fiesta ya repartía sustos hace más de cien años. Este año, España busca disfraces de Catrina, de Pennywise y de Monster High.",
              "Fuente: Wikimedia Commons — dominio público")
facts = ["Según idealo.es, para los niños lo más buscado es Monster High y K-Pop Demon Hunters.",
         "La camiseta del Clásico lleva el logo GOLF WANG, de Tyler, the Creator.",
         "El mal hijo es el primer largometraje de Jaime Lorente, rodado entre Murcia y Canarias."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DISFRACES 2026", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿De qué te disfrazas este Halloween — o prefieres las castañas de la Castanyada? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap('올해 Halloween에는 무엇으로 변장해요? 아니면 군밤이 더 좋아요? 두 문장 써서 보내 주세요.', "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "올해 Halloween에는 무엇으로 변장해요? 아니면 군밤이 더 좋아요? 두 문장 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　5면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "답은 8면에　문제는 급이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　COMPRENSIÓN", 25)
e.expl('5면 글을 읽고 정답을 고르세요.')
e.ex("B1", '객관식', "B", '아이는 Monster High를 가장 많이 찾아요',
     "Según idealo.es, para los niños lo más buscado es... A. Pennywise · B. Monster High · C. Maléfica", size=20, gap=8)
e.ex("B1", '객관식', "A", 'Catrina는 어른에게 인기 있는 의상이에요',
     "¿Qué disfraz buscan los adultos? A. La Catrina · B. K-Pop Demon Hunters · C. Monster High", size=20, gap=8)
e.ex("B1", '객관식', "C", 'GOLF WANG은 Tyler, the Creator의 로고예요',
     "¿De quién es el logo GOLF WANG? A. de LaLiga · B. de un equipo · C. de Tyler, the Creator", size=20, gap=8)
e.ex("B1", '객관식', "B", '새 유니폼은 토요일 여자 팀이 먼저 선보여요',
     "La camiseta se estrena primero... A. el domingo con los hombres · B. el sábado con el equipo femenino · C. en noviembre", size=20, gap=8)
e.ex("B1", '객관식', "A", 'El mal hijo는 그의 장편 데뷔작이에요',
     "El mal hijo es... A. el primer largometraje de Jaime Lorente · B. una serie de televisión · C. un videojuego", size=20, gap=8)
e.head("B　PALABRAS DEL TEXTO", 25)
e.expl('상자 속 단어로 빈칸을 채우세요. 주의: 활용해야 하는 단어도 있어요.')
e.para("disfraz · buscar · estrenar · sala · miedo · postre", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", '문장 완성', "disfraz", 'disfraz = 변장 의상',
     "Para Halloween compro un ___.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "busca", 'buscar 활용 él → busca',
     'La gente ___ (원형 buscar) el disfraz en internet.', instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "estrena", 'estrenar 활용 → estrena',
     'El equipo femenino ___ (원형 estrenar) la camiseta el sábado.', instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "salas", 'salas de cine 영화관 (복수로 써요)',
     "Las ___ de cine estrenan películas de terror.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "miedo", 'dar miedo 무섭게 하다',
     "Las películas de terror dan ___.", instr='빈칸 채우기', size=20, gap=8)
e.ex("B1", '문장 완성', "postre", 'postre = 디저트 (3면: panellets)',
     "Los panellets son un ___ de mazapán.", instr='빈칸 채우기', size=20, gap=8)
e.head("C　IR A + INFINITIVO", 25)
e.expl('ir a + 동사 원형으로 ‘~할 것’을 나타내세요.')
e.ex("B1", '문장 바꾸기', "Vamos a comprar los disfraces el sábado.", 'vamos a + 원형',
     "Compramos los disfraces el sábado. → ___", instr='바꿔 쓰기', size=20, gap=8)
e.ex("B1", '문장 바꾸기', "Va a ver una película de terror.", 'va a + 동사 원형',
     "Ve una película de terror. → ___", instr='바꿔 쓰기', size=20, gap=8)
e.ex("B1", '문장 바꾸기', "Vas a jugar con la camiseta nueva en eFootball.", 'vas a + 원형',
     "Juegas con la camiseta nueva en eFootball. → ___", instr='바꿔 쓰기', size=20, gap=8)
e.ex("B1", '문장 바꾸기', "Van a comer castañas asadas en casa.", 'van a + 동사 원형',
     "Comen castañas asadas en casa. → ___", instr='바꿔 쓰기', size=20, gap=8)
e.head("D　¿VERDADERO O FALSO?", 25)
e.ex("B1", '읽기 판단', "Verdadero", 'eFootball은 10월 23일부터예요',
     "En eFootball se puede jugar con la camiseta desde el 23 de octubre. ¿Verdadero o falso?", instr='참 / 거짓', size=20, gap=8)
e.ex("B1", '읽기 판단', "Falso", '촬영지는 무르시아와 카나리아예요',
     "El mal hijo se rodó en Madrid. ¿Verdadero o falso?", instr='참 / 거짓', size=20, gap=8)
e.ex("B1", '읽기 판단', "Verdadero", 'idealo.es 자료는 10월 초 것이에요',
     "Los datos de idealo.es son de principios de octubre. ¿Verdadero o falso?", instr='참 / 거짓', size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-juventud.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · A FONDO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("A FONDO　심층", "La Lucerna", "NIVEL B2　Rumbo al 29N　11월 29일 총선을 향해")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P6-main")
f.title("Rumbo al 29N: leer las encuestas sin perder la calma", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: B2　La política nacional española")
f.para("El domingo 29 de noviembre, España vota en elecciones generales. La legislatura se ha cerrado sin presupuestos nuevos: los presupuestos de 2023 siguen prorrogados, algo que los medios españoles describen como una primera vez. Esta semana, los partidos presentan sus listas ante las juntas electorales provinciales — el papeleo silencioso que pone en marcha la campaña.")
f.para("Con la fecha fijada, las encuestas mandan en los titulares. Pero hay un problema que todo lector debería conocer: las encuestas no se ponen de acuerdo entre sí. Y la diferencia no es pequeña.")
f.para("La media de encuestas que publica el diario Demócrata — una media de entre 15 y 16 institutos, con datos del 20 y 21 de octubre — da ventaja al PP con ≈31,7 %, seguido del PSOE con ≈26,8 %, Vox con 18,7 %, Sumar con 6,3 % y Podemos con 3,1 %.")
f.para("El barómetro de octubre del CIS, el instituto público de encuestas, cuenta otra historia: PSOE 34 %, PP 22,2 % y Vox 17,1 %. En una serie, el PP va primero; en la otra, el PSOE saca casi doce puntos de ventaja.")
f.para("¿Quién miente? Probablemente nadie. Las encuestas difieren por el método: cuándo se pregunta, a cuántas personas, cómo se reparte a los indecisos y cómo se cocina el voto bruto. Una encuesta no es un resultado: es una foto con margen de error, tomada en un día concreto.")
f.para("Nuestro consejo de lectura es simple: mira siempre quién publica, cuándo y con qué método; compara series, no titulares sueltos; y desconfía de quien mezcle dos encuestas en un solo número. Publicamos las dos series con su fuente y su fecha, una junto a otra — y no las mezclamos nunca en un solo número.")
f.para("Las próximas semanas traerán el programa de cada partido, los debates y, al final, la única encuesta que no admite error: la del 29 de noviembre, con papeletas de verdad.")
f.end_report()

# col 3: timeline + poll-reading box (sequential, measured)
bx = COLX[3]
p.rect(bx, 200, CW, 590, fill=BOX)
p.text(bx + 22, 240, "EL CAMINO AL 29N", 24, "sans", True, OLIVE)
steps = [
    ("OCTUBRE", "La legislatura se cierra sin presupuestos nuevos: siguen los de 2023."),
    ("19–25 OCT.", "Los partidos presentan sus listas ante las juntas electorales provinciales."),
    ("OCTUBRE", "Las encuestas ocupan los titulares: dos series, dos fotos distintas."),
    ("29 NOV.", "Elecciones generales: España vota."),
]
sy3 = 282
for w, t in steps:
    p.text(bx + 22, sy3 + 21, w, 20, "sans", True, OLIVE)
    sy3 = p.para(bx + 164, sy3 + 21, t, 21, "serif", False, INK, CW - 186, 1.4) + 16
by3 = 816
bb = ("Para leer cualquier encuesta, pregunta tres cosas: ¿quién la publica? "
      "¿Cuándo se hizo el trabajo de campo? ¿Qué margen de error tiene? "
      "Sin esas tres respuestas, un porcentaje no dice casi nada.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f0eee5")
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LEER UNA ENCUESTA", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh)

# ---- bar charts (two separate sets, honestly captioned) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, OLIVE, 2)
p.text(MX, gy + 10, "DOS SERIES, DOS FOTOS　두 개의 시리즈, 두 장의 사진 (no se pueden mezclar　섞으면 안 돼요)", 26, "sans", True, OLIVE)
dem = [("PP", 31.7), ("PSOE", 26.8), ("Vox", 18.7), ("Sumar", 6.3), ("Podemos", 3.1)]
cis = [("PSOE", 34.0), ("PP", 22.2), ("Vox", 17.1), ("Sumar", None), ("Podemos", None)]
bx1, bx2, bw_, bhh = MX, COLX[2], 2 * CW + GUT, 322
for (x0, title, data, cap) in [
    (bx1, "MEDIA DEMÓCRATA · estimación de voto, %", dem,
     "Media de 15–16 institutos · datos del 20–21 de octubre de 2026."),
    (bx2, "BARÓMETRO CIS (OCTUBRE) · estimación de voto, %", cis,
     "Instituto público CIS · Aquí solo se muestran los tres partidos publicados en nuestra fuente."),
]:
    p.rect(x0, gy + 28, bw_, bhh, fill=BOX)
    p.text(x0 + 22, gy + 68, title, 21, "sans", True, INK)
    yy = gy + 96
    for lab, v in data:
        p.text(x0 + 22, yy + 24, lab, 21, "serif", True, INK)
        if v is not None:
            p.rect(x0 + 150, yy + 6, v * 12, 22, fill=OLIVE)
            p.text(x0 + 168 + v * 12, yy + 24, f"{v:.1f}".replace(".", ",") + " %", 20.5, "serif", False, INK)
        else:
            p.text(x0 + 150, yy + 24, "— no publicado en la fuente —", 19.5, "sans", False, GREY)
        yy += 31
    p.para(x0 + 22, gy + bhh - 30, cap, 17.5, "sans", False, GREY, bw_ - 44, 1.3)

# ---- P6 exercises ----
ey = 1940
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　6면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "답은 8면에　문제는 급이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEER LOS GRÁFICOS", 25)
e.expl('위 두 그래프를 보고 정답을 고르세요.')
e.ex("B2", '객관식', "A", 'Demócrata 평균에서는 PP가 1위예요 (31,7%)',
     "En la media de Demócrata, primero va... A. el PP · B. el PSOE · C. Vox", size=19, gap=3)
e.ex("B2", '객관식', "B", 'CIS에서는 PSOE가 34%예요',
     "En el barómetro del CIS, el PSOE tiene... A. 26,8 % · B. 34 % · C. 31,7 %", size=19, gap=3)
e.ex("B2", '객관식', "C", '두 시리즈 모두 Vox가 3위예요',
     "¿Qué es verdad en las DOS series? A. Sumar primero · B. Podemos gana a Vox · C. Vox, tercero", size=19, gap=3)
e.ex("B2", '객관식', "A", '평균은 15–16개 기관을 모은 것이에요',
     "La media de Demócrata reúne... A. 15–16 institutos · B. un instituto · C. ninguno", size=19, gap=3)
e.ex("B2", '객관식', "B", "31,7 + 26,8 + 18,7 = 77,2",
     "PP + PSOE + Vox en la media suman... A. 50 % · B. 77,2 % · C. 100 %", size=19, gap=3)
e.ex("B2", '객관식', "C", '우리 출처에는 CIS의 Sumar/Podemos가 실리지 않았어요',
     "En el CIS no aparecen Sumar y Podemos porque... A. tienen 0 % · B. van primeros · C. la fuente no los publicó", size=19, gap=3)
e.head("B　COMPRENSIÓN", 25)
e.ex("B2", '객관식', "B", '의회는 새 예산 없이 끝났고 2023년 예산이 연장됐어요',
     "La legislatura se cerró... A. con presupuestos nuevos · B. sin presupuestos nuevos · C. sin elecciones", size=19, gap=3)
e.ex("B2", '객관식', "A", '이번 주 각 당이 후보 명단을 제출해요',
     "Esta semana, los partidos presentan... A. sus listas · B. los resultados · C. el nuevo gobierno", size=19, gap=3)
e.ex("B2", '객관식', "C", '여론조사는 오차가 있는, 특정한 날의 사진이에요',
     "Según el texto, una encuesta es... A. un resultado final · B. una promesa · C. una foto con margen de error", size=19, gap=3)
e.ex("B2", '객관식', "B", '두 시리즈는 나누어 싣고 출처와 날짜를 밝혀요',
     "La Lucerna publica las dos series... A. mezcladas en un número · B. separadas, con fuente y fecha · C. sin fecha", size=19, gap=3)
e.head("C　EL SUBJUNTIVO", 25)
e.ex("B2", '문장 완성', "tenga", 'es posible que + 접속법 tenga',
     "Es posible que el CIS ___ (tener) otro método.", instr='빈칸 채우기', size=19, gap=3)
e.ex("B2", '문장 완성', "sea", 'es importante que + 접속법 sea',
     "Es importante que cada gráfico ___ (ser) claro.", instr='빈칸 채우기', size=19, gap=3)
e.ex("B2", '문장 완성', "para que", 'para que + 접속법 (목적)',
     "Publicamos la fuente ___ todos puedan comprobarla.", instr='빈칸 채우기', size=19, gap=3)
e.ex("B2", '문장 완성', "Aunque", 'Aunque 뒤에는 직설법이 와요 (이미 아는 사실)',
     "___ las encuestas difieren, ninguna miente.", instr='빈칸 채우기', size=19, gap=3)
e.head("D　PALABRAS DEL DEBATE", 25)
e.expl('상자 속 단어로 빈칸을 채우세요: sondeo · media · indecisos · margen de error')
e.ex("B2", '문장 완성', "sondeo", 'sondeo = 여론조사',
     "Un ___ pregunta a una muestra de ciudadanos.", instr='빈칸 채우기', size=19, gap=3)
e.ex("B2", '문장 완성', "media", 'media = 여러 결과의 평균',
     "La ___ de Demócrata reúne 15–16 institutos.", instr='빈칸 채우기', size=19, gap=3)
e.ex("B2", '문장 완성', "indecisos", 'indecisos = 아직 정하지 않은 사람들',
     "Los ___ todavía no saben a quién votar.", instr='빈칸 채우기', size=19, gap=3)
e.ex("B2", '문장 완성', "margen de error", 'margen de error = 오차 범위',
     "Toda encuesta tiene un ___.", instr='빈칸 채우기', size=19, gap=3)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-afondo.svg")
print("P6 saved, exercises so far:", len(REG))
