# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JUVENTUD (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUVENTUD　JUVENTUDE", "La Lucerna", "NIVEL B1　Disfraces, camisetas y pantallas　FANTASIAS, CAMISAS E TELAS")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Pantallas y disfraces: así se prepara España para Halloween", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: B1")
f.para("Faltan diez días para Halloween, y España ya busca su disfraz. Según los datos de idealo.es de principios de octubre, los adultos buscan sobre todo disfraces de La Catrina, de Pennywise, de los años 70 y 80, de Michael Myers y de Maléfica. Para los niños, lo más buscado es Monster High y el éxito del año: K-Pop Demon Hunters.")
f.para("El susto también viene en pantalla grande. Este otoño, las salas de cine estrenan películas de terror para todos los gustos — y el sábado 31, mucha gente va a celebrar Halloween en el cine o en casa, con amigos.")
f.para("El fútbol también tiene su fiesta de Halloween: la camiseta del Clásico. Para el partido del domingo, el Barça lleva en el pecho el logo GOLF WANG, de Tyler, the Creator. La camiseta se estrena primero con el equipo femenino, el sábado 24, y en el juego eFootball se puede jugar con ella desde el viernes 23. Un cantante en la camiseta del partido más grande: la música y el fútbol se cruzan otra vez.")
f.para("Y no todo es pantalla: el viernes pasado se estrenó en los cines El mal hijo, el primer largometraje de Jaime Lorente, un drama rural rodado entre Murcia y Canarias. Una historia de familia, lejos de los disfraces: el cine español también tiene su otoño serio.")
f.para("Halloween se junta este año con las fiestas propias de España — la Castanyada y el Samaín (página 3). Cada lector elige su noche: ¿disfraz, castañas o las dos?")
f.box("EL PLAN DEL SÁBADO 31", [
    ("1. Por la mañana: compra el disfraz en la tienda (de manhã: compra a fantasia na loja)", "serif", False, INK, 21, 1.36),
    ("2. Por la tarde: cine de terror con amigos (à tarde: cinema de terror com os amigos)", "serif", False, INK, 21, 1.36),
    ("3. Por la noche: fiesta de Halloween (à noite: festa de Halloween)", "serif", False, INK, 21, 1.36),
    ("4. O la opción tranquila: castañas asadas en casa (ou a opção tranquila: castanhas assadas em casa)", "serif", False, INK, 21, 1.36),
    ("5. El domingo 1: flores y familia, el Día de Todos los Santos (domingo, dia 1: flores e família, o Dia de Todos os Santos)", "serif", False, INK, 21, 1.36),
])
f.gloss("el disfraz, a fantasia · el susto, o susto · estrenar, estrear · el largometraje, o longa-metragem · rodado, filmado.")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("De que você se fantasia neste Halloween — ou prefere as castanhas da Castanyada? Escreva duas frases.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　E você?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "De que você se fantasia neste Halloween — ou prefere as castanhas da Castanyada? Escreva duas frases.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　EXERCÍCIOS DA PÁGINA 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8　Os exercícios podem misturar os níveis: procure pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　COMPRENSIÓN", 25)
e.expl("Leia o artigo da página 5 e escolha a resposta certa.")
e.ex("B1", "单选", "B", "para as crianças, o mais buscado é Monster High",
     "Según idealo.es, para los niños lo más buscado es... A. Pennywise · B. Monster High · C. Maléfica", size=20, gap=8)
e.ex("B1", "单选", "A", "La Catrina é fantasia de adulto",
     "¿Qué disfraz buscan los adultos? A. La Catrina · B. K-Pop Demon Hunters · C. Monster High", size=20, gap=8)
e.ex("B1", "单选", "C", "o logo GOLF WANG é de Tyler, the Creator",
     "¿De quién es el logo GOLF WANG? A. de LaLiga · B. de un equipo · C. de Tyler, the Creator", size=20, gap=8)
e.ex("B1", "单选", "B", "a camisa estreia primeiro no sábado, com o time feminino",
     "La camiseta se estrena primero... A. el domingo con los hombres · B. el sábado con el equipo femenino · C. en noviembre", size=20, gap=8)
e.ex("B1", "单选", "A", "El mal hijo é o primeiro longa-metragem de Jaime Lorente",
     "El mal hijo es... A. el primer largometraje de Jaime Lorente · B. una serie de televisión · C. un videojuego", size=20, gap=8)
e.head("B　PALABRAS DEL TEXTO", 25)
e.expl("Complete com as palavras do quadro. Atenção: alguns verbos mudam de forma.")
e.para("disfraz · buscar · estrenar · sala · miedo · postre", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "disfraz", "disfraz = a fantasia",
     "Para Halloween compro un ___.", instr="Complete", size=20, gap=8)
e.ex("B1", "完成句子", "busca", "buscar, com ele: busca",
     "La gente ___ (infinitivo: buscar) el disfraz en internet.", instr="Complete", size=20, gap=8)
e.ex("B1", "完成句子", "estrena", "estrenar, com ele: estrena",
     "El equipo femenino ___ (infinitivo: estrenar) la camiseta el sábado.", instr="Complete", size=20, gap=8)
e.ex("B1", "完成句子", "salas", "salas de cine = salas de cinema (no plural)",
     "Las ___ de cine estrenan películas de terror.", instr="Complete", size=20, gap=8)
e.ex("B1", "完成句子", "miedo", "dar miedo = dar medo",
     "Las películas de terror dan ___.", instr="Complete", size=20, gap=8)
e.ex("B1", "完成句子", "postre", "postre = a sobremesa (página 3: panellets)",
     "Los panellets son un ___ de mazapán.", instr="Complete", size=20, gap=8)
e.head("C　IR A + INFINITIVO", 25)
e.expl("Reescreva com ir a + infinitivo, para falar do futuro.")
e.ex("B1", "句型转换", "Vamos a comprar los disfraces el sábado.", "vamos a + inf.",
     "Compramos los disfraces el sábado. → ___", instr="Reescreva", size=20, gap=8)
e.ex("B1", "句型转换", "Va a ver una película de terror.", "va a + inf.",
     "Ve una película de terror. → ___", instr="Reescreva", size=20, gap=8)
e.ex("B1", "句型转换", "Vas a jugar con la camiseta nueva en eFootball.", "vas a + inf.",
     "Juegas con la camiseta nueva en eFootball. → ___", instr="Reescreva", size=20, gap=8)
e.ex("B1", "句型转换", "Van a comer castañas asadas en casa.", "van a + inf.",
     "Comen castañas asadas en casa. → ___", instr="Reescreva", size=20, gap=8)
e.head("D　¿VERDADERO O FALSO?", 25)
e.ex("B1", "判断对错", "Verdadero", "no eFootball, a camisa desde 23 de outubro",
     "En eFootball se puede jugar con la camiseta desde el 23 de octubre. ¿Verdadero o falso?", instr="Verdadeiro ou falso", size=20, gap=8)
e.ex("B1", "判断对错", "Falso", "rodado entre Múrcia e Canárias, não Madri",
     "El mal hijo se rodó en Madrid. ¿Verdadero o falso?", instr="Verdadeiro ou falso", size=20, gap=8)
e.ex("B1", "判断对错", "Verdadero", "os dados do idealo.es são do começo de outubro",
     "Los datos de idealo.es son de principios de octubre. ¿Verdadero o falso?", instr="Verdadeiro ou falso", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-juventud.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · A FONDO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("A FONDO　EM PROFUNDIDADE", "La Lucerna", "NIVEL B2　Rumbo al 29N　RUMO AO 29N")

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
p.text(MX, gy + 10, "DOS SERIES, DOS FOTOS　Duas séries, duas fotos (no se pueden mezclar　não misturar)", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "EJERCICIOS　EXERCÍCIOS DA PÁGINA 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8　Os exercícios podem misturar os níveis: procure pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEER LOS GRÁFICOS", 25)
e.expl("Leia os gráficos e escolha a certa.")
e.ex("B2", "单选", "A", "na média do Demócrata, o PP é o primeiro (31,7%)",
     "En la media de Demócrata, primero va... A. el PP · B. el PSOE · C. Vox", size=19, gap=3)
e.ex("B2", "单选", "B", "no CIS, o PSOE tem 34%",
     "En el barómetro del CIS, el PSOE tiene... A. 26,8 % · B. 34 % · C. 31,7 %", size=19, gap=3)
e.ex("B2", "单选", "C", "nas duas séries, o Vox é o terceiro",
     "¿Qué es verdad en las DOS series? A. Sumar primero · B. Podemos gana a Vox · C. Vox, tercero", size=19, gap=3)
e.ex("B2", "单选", "A", "a média reúne 15–16 institutos",
     "La media de Demócrata reúne... A. 15–16 institutos · B. un instituto · C. ninguno", size=19, gap=3)
e.ex("B2", "单选", "B", "31,7 + 26,8 + 18,7 = 77,2",
     "PP + PSOE + Vox en la media suman... A. 50 % · B. 77,2 % · C. 100 %", size=19, gap=3)
e.ex("B2", "单选", "C", "a nossa fonte não publicou Sumar e Podemos no CIS",
     "En el CIS no aparecen Sumar y Podemos porque... A. tienen 0 % · B. van primeros · C. la fuente no los publicó", size=19, gap=3)
e.head("B　COMPRENSIÓN", 25)
e.ex("B2", "单选", "B", "a legislatura fechou sem orçamento novo; segue o de 2023",
     "La legislatura se cerró... A. con presupuestos nuevos · B. sin presupuestos nuevos · C. sin elecciones", size=19, gap=3)
e.ex("B2", "单选", "A", "esta semana os partidos apresentam as suas listas",
     "Esta semana, los partidos presentan... A. sus listas · B. los resultados · C. el nuevo gobierno", size=19, gap=3)
e.ex("B2", "单选", "C", "uma pesquisa é uma foto de um dia, com margem de erro",
     "Según el texto, una encuesta es... A. un resultado final · B. una promesa · C. una foto con margen de error", size=19, gap=3)
e.ex("B2", "单选", "B", "as duas séries saem separadas, com fonte e data",
     "La Lucerna publica las dos series... A. mezcladas en un número · B. separadas, con fuente y fecha · C. sin fecha", size=19, gap=3)
e.head("C　EL SUBJUNTIVO", 25)
e.ex("B2", "完成句子", "tenga", "es posible que + subjuntivo: tenga",
     "Es posible que el CIS ___ (tener) otro método.", instr="Complete", size=19, gap=3)
e.ex("B2", "完成句子", "sea", "es importante que + subjuntivo: sea",
     "Es importante que cada gráfico ___ (ser) claro.", instr="Complete", size=19, gap=3)
e.ex("B2", "完成句子", "para que", "para que + subjuntivo (finalidade)",
     "Publicamos la fuente ___ todos puedan comprobarla.", instr="Complete", size=19, gap=3)
e.ex("B2", "完成句子", "Aunque", "Aunque + indicativo (fato conhecido)",
     "___ las encuestas difieren, ninguna miente.", instr="Complete", size=19, gap=3)
e.head("D　PALABRAS DEL DEBATE", 25)
e.expl("Complete com as palavras: sondeo · media · indecisos · margen de error")
e.ex("B2", "完成句子", "sondeo", "sondeo = a pesquisa de opinião",
     "Un ___ pregunta a una muestra de ciudadanos.", instr="Complete", size=19, gap=3)
e.ex("B2", "完成句子", "media", "media = a média de vários institutos",
     "La ___ de Demócrata reúne 15–16 institutos.", instr="Complete", size=19, gap=3)
e.ex("B2", "完成句子", "indecisos", "indecisos = os indecisos",
     "Los ___ todavía no saben a quién votar.", instr="Complete", size=19, gap=3)
e.ex("B2", "完成句子", "margen de error", "margen de error = a margem de erro",
     "Toda encuesta tiene un ___.", instr="Complete", size=19, gap=3)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-afondo.svg")
print("P6 saved, exercises so far:", len(REG))
