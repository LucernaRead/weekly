# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P3 San Martín / P4 Nations League. Fresh text, structure mirrors W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · 문화", "La Lucerna", "A2 → B1 · San Martín, castañas y vino nuevo · 성 마르틴, 밤과 새 포도주")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("San Martín: la capa, las castañas y el veranillo", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: A2 → B1")
f.para("El miércoles 11 de noviembre es San Martín, y en muchos pueblos de España es día de fiesta, de castañas y de vino nuevo.")
f.para("Cuenta la leyenda que Martín, soldado romano, partió su capa en dos con la espada para cubrir a un mendigo que moría de frío. Y el cielo le regaló unos días de sol: el veranillo de San Martín, ese calor suave que llega a mitad del otoño, justo antes de que el frío se instale de verdad.")
f.para("En Moreda de Aller, en Asturias, la Fiesta de San Martín o de los Humanitarios empieza con una misa cantada al son de las gaitas. Después llega la puya del ramu, la subasta del pan de escanda bendecido, y un desfile de carrozas con bandas de gaitas y trajes tradicionales.")
f.para("Y en la mesa, la comida de San Martín: fabada, casadiellas y panchón. En Galicia y en Castilla y León, el magosto pone castañas asadas y vino nuevo en la mesa. Tres fiestas, una misma tarde de otoño.")
f.gloss("la capa는 망토예요 · el mendigo는 거지예요 · el veranillo는 늦가을 따뜻한 날, la gaita는 백파이프 · el magosto는 밤 축제.")
f.head("LO QUE QUEDA DEL OTOÑO", 25)
f.para("El otoño sigue: las tardes cortas, las castañas en la calle y, en la cocina, los primeros guisos de la temporada. Y en la agenda, una fecha que ya mira toda España: el domingo 29 de noviembre, las elecciones generales (página 6).")
f.end_report()

# col 3: chestnut image + facts + ¿Y tú? (sequential)
ix = COLX[3]
image(p, "castanas.jpg", ix, 200, CW, 430)
cy3 = caption(p, ix, 630, CW, "Castañas asadas, las protagonistas del magosto: en noviembre, la noche huele a castaña caliente y a vino nuevo, de Galicia a Castilla y León.",
              "Foto: Wikimedia Commons — CC0 (dominio público)")
facts = ["El miércoles 11 es San Martín: fiesta, castañas y vino nuevo en muchos pueblos.",
         "En Moreda de Aller, la fiesta empieza con misa cantada y gaitas, y sigue con la puya del ramu.",
         "El veranillo de San Martín trae unos días de sol suave a mitad del otoño."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SAN MARTÍN, EN TRES DATOS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Has probado las castañas asadas? ¿Conoces el veranillo de San Martín en tu país? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("군밤을 먹어 본 적이 있나요? 여러분 나라에도 veranillo 같은 늦가을 따뜻한 날이 있나요? 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ? · 당신은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "군밤을 먹어 본 적이 있나요? 여러분 나라에도 veranillo 같은 늦가을 따뜻한 날이 있나요? 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · 3면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "답은 8면에 · 문제는 급이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · ¿VERDADERO O FALSO?", 25)
e.bridge("3면 글을 읽고 맞는지 틀린지 판단하세요.")
e.ex("A2", "읽기 판단", "Verdadero", "성 마르틴 축일은 11월 11일 수요일이에요",
     "San Martín se celebra el miércoles 11 de noviembre. ¿Verdadero o falso?", instr="참 / 거짓", size=20, gap=8)
e.ex("A2", "읽기 판단", "Verdadero", "마르틴은 망토를 거지와 나눴어요",
     "Martín partió su capa para cubrir a un mendigo. ¿Verdadero o falso?", instr="참 / 거짓", size=20, gap=8)
e.ex("A2", "읽기 판단", "Falso", "우마니타리오스 축제는 아스투리아스에서 열려요, 갈리시아가 아니에요",
     "La Fiesta de los Humanitarios se celebra en Galicia. ¿Verdadero o falso?", instr="참 / 거짓", size=20, gap=8)
e.ex("B1", "읽기 판단", "Falso", "베라니요는 가을의 따뜻한 며칠이에요, 여름이 아니에요",
     "El veranillo de San Martín es el verano. ¿Verdadero o falso?", instr="참 / 거짓", size=20, gap=8)
e.ex("A2", "읽기 판단", "Verdadero", "성 마르틴 식사에는 fabada, casadiellas, panchón이 나와요",
     "La comida de San Martín incluye fabada y casadiellas. ¿Verdadero o falso?", instr="참 / 거짓", size=20, gap=8)
e.head("B · PALABRAS DEL TEXTO", 25)
e.bridge("네모 안의 단어로 빈칸을 채우세요.")
e.para("capa · mendigo · castañas · gaita · veranillo", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "문장 완성", "capa", "마르틴은 자기 망토(capa)를 나눴어요",
     "Martín partió su ___ en dos.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "mendigo", "mendigo = 거지",
     "El ___ moría de frío junto a la puerta.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "castañas", "castañas asadas = 군밤",
     "En el magosto comemos ___ asadas.", instr="빈칸 채우기", size=20, gap=8)
e.ex("A2", "문장 완성", "gaita", "gaita = 백파이프",
     "La misa de San Martín suena al son de la ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "veranillo", "veranillo de San Martín = 성 마르틴의 늦가을 따뜻함",
     "En noviembre llega el ___ de San Martín.", instr="빈칸 채우기", size=20, gap=8)
e.head("C · COMPRENSIÓN", 25)
e.bridge("정답을 고르세요.")
e.ex("A2", "객관식", "B", "우마니타리오스 축제는 Moreda de Aller에서 열려요",
     "¿Dónde se celebra la Fiesta de los Humanitarios? A. en Galicia · B. en Moreda de Aller · C. en Madrid", size=20, gap=8)
e.ex("A2", "객관식", "A", "puya del ramu는 축복받은 빵 경매예요",
     "¿Qué es la puya del ramu? A. la subasta del pan bendecido · B. un baile · C. un dulce", size=20, gap=8)
e.ex("B1", "객관식", "C", "베라니요는 가을의 며칠간 따뜻한 날씨예요",
     "¿Qué es el veranillo de San Martín? A. una fiesta · B. un plato · C. unos días de sol suave en otoño", size=20, gap=8)
e.ex("B1", "객관식", "B", "성 마르틴 축일 후에 총선거는 11월 29일이에요",
     "Después de San Martín, la próxima gran fecha es... A. el puente · B. las elecciones del 29 · C. la Navidad", size=20, gap=8)
e.head("D · CONSTRUIR FRASES", 25)
e.bridge("단어를 모아 올바른 문장을 만드세요.")
e.ex("A2", "문장 만들기", "Martín parte su capa en dos.", "동사는 두 번째 자리예요",
     "Martín / parte / su capa / en dos → ___", instr="문장 만들기", size=20, gap=8)
e.ex("B1", "문장 만들기", "En noviembre comemos castañas asadas.", "시간이 앞에, 동사는 두 번째예요",
     "en noviembre / comemos / castañas asadas → ___", instr="문장 만들기", size=20, gap=8)
e.ex("B1", "문장 만들기", "En Moreda celebran San Martín.", "장소가 앞에, 동사는 두 번째",
     "en Moreda / celebran / San Martín → ___", instr="문장 만들기", size=20, gap=8)
e.ex("B1", "문장 바꾸기", "Todos preguntan si hay veranillo.", "간접 의문문에는 si를 써요",
     "«¿Hay veranillo?» (todos preguntan) → ___", instr="바꿔 쓰기", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · DEPORTE (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("DEPORTE · 스포츠", "La Lucerna", "NIVEL B1 · Praga el jueves, Inglaterra el domingo · 목요일은 프라하, 일요일은 잉글랜드")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Praga el jueves, Inglaterra el domingo", 37)
f.byline("De la redacción deportiva de La Lucerna · Nivel de lectura: B1")
f.para("La Liga se para y juega la selección: dos partidos de la Liga de Naciones deciden el grupo A3.")
f.para("España, vigente campeona del mundo y de Europa, juega en el grupo A3 con Croacia, Inglaterra y la República Checa. La fase de grupos se cierra esta semana: el jueves 12, a las 20:45, la Roja visita a Chequia en el estadio Letná de Praga; el domingo 15, a las 20:45, recibe a Inglaterra en el Metropolitano de Madrid.")
f.para("El seleccionador Luis de la Fuente dio la lista el viernes 6 de noviembre, y los convocados se concentran el lunes 9 en la Ciudad del Fútbol de Las Rozas. El domingo 15 puede decidir el primer puesto del grupo y la plaza en la fase final de la Liga de Naciones.")
f.para("Y el viernes 13, a las 19:00, la selección sub-21 juega un amistoso contra Japón en Almendralejo (Badajoz). Entre la Roja y la sub-21, esta semana el fútbol español no se para: cambia de camiseta.")
f.gloss("la fase de grupos는 조별 리그예요 · el seleccionador는 국가대표 감독이에요 · la lista는 소집 명단이에요 · la plaza는 자리예요 · el amistoso는 친선 경기예요.")
f.end_report()

# col 3: last-Sunday box + ¿Y tú? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 376, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "EL DOMINGO 8, DOS CITAS", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "El domingo 8, Madrid tuvo dos citas: por la tarde, la NFL en el Bernabéu, y por la noche, el Atlético–Barça en el Metropolitano. Al cierre de esta edición, los resultados no estaban disponibles: esta página no inventa marcadores.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 602
etvous = "¿Y tú? El domingo a las 20:45, ¿qué miras: la Roja o la tele? ¿Quién gana el grupo A3: España o Inglaterra? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("일요일 20:45에 어떤 경기를 보세요? 스페인 대 잉글랜드, 누가 이길까요? 답을 스페인어로 두 문장 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "¿Y TÚ? · 당신은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "일요일 20:45에 어떤 경기를 보세요? 스페인 대 잉글랜드, 누가 이길까요? 답을 스페인어로 두 문장 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA LIGA DE NACIONES · GRUPO A3 · 네이션스리그 A3조 일정", 26, "sans", True, OLIVE)
rows = [
    ("J1 · 26.09", "20:45", "Inglaterra – España (en Londres, abre la fase)"),
    ("J2 · 29.09", "20:45", "España – Croacia (estreno ante la afición)"),
    ("J3 · 03.10", "20:45", "España – República Checa (en casa)"),
    ("J4 · 06.10", "20:45", "Croacia – España (a domicilio)"),
    ("J5 · 12.11", "20:45", "República Checa – España (Letná, Praga)"),
    ("J6 · 15.11", "20:45", "España – Inglaterra (Metropolitano, Madrid)"),
    ("SUB-21 · 13.11", "19:00", "España – Japón, amistoso en Almendralejo (Badajoz)"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Horarios en hora peninsular. La fase de grupos se cierra el domingo 15: el partido contra Inglaterra puede decidir el primer puesto del grupo A3."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · 4면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "답은 8면에 · 문제는 급이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPRENSIÓN", 25)
e.bridge("4면 글을 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "A", "스페인은 A3조에 있어요",
     "España juega en el grupo... A. A3 · B. A1 · C. B3", size=20, gap=8)
e.ex("B1", "객관식", "B", "목요일은 체코전, 일요일은 잉글랜드전이에요",
     "Esta semana, la Roja juega... A. dos partidos en casa · B. en Praga y en Madrid · C. solo en Praga", size=20, gap=8)
e.ex("B1", "객관식", "C", "두 경기 모두 20:45에 시작해요",
     "Los dos partidos de la Roja son a las... A. 18:45 · B. 21:00 · C. 20:45", size=20, gap=8)
e.ex("B1", "객관식", "A", "일요일 경기는 메트로폴리타노에서 열려요",
     "El España–Inglaterra se juega en... A. el Metropolitano · B. el Bernabéu · C. Las Rozas", size=20, gap=8)
e.ex("B1", "객관식", "B", "U21은 금요일에 일본과 경기해요",
     "La sub-21 juega el viernes contra... A. Inglaterra · B. Japón · C. Croacia", size=20, gap=8)
e.head("B · LAS PALABRAS", 25)
e.match_set("B1", "단어 짝짓기",
            ["la fase de grupos", "el seleccionador", "la lista", "el amistoso"],
            ["un partido sin puntos en juego",
             "la primera parte de un torneo, en grupos",
             "quien elige a los jugadores de la selección",
             "los jugadores convocados para un partido"],
            ["b", "c", "d", "a"],
            ["fase de grupos=조별 리그 b", "seleccionador=국가대표 감독 c", "lista=소집 명단 d", "amistoso=친선 경기 a"],
            instr="단어와 뜻 짝짓기")
e.head("C · COMPARATIVOS", 25)
e.bridge("빈칸을 채우세요. 괄호 안 단어의 비교급이나 -ísimo 형태를 쓰세요.")
e.ex("B1", "문장 완성", "más importante", "más + importante (조 1위가 더 중요해요)",
     "El partido del domingo es ___ que un amistoso. (importante)", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "muchísimos", "muchísimos aficionados = 아주 많은 팬",
     "El Metropolitano espera a ___ aficionados. (muchos)", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "peor", "malo의 비교급은 peor예요",
     "Perder en Praga sería la ___ (malo) noticia de la semana.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "mejor", "bueno의 비교급은 mejor예요",
     "Ganar el grupo sería la ___ (bueno) noticia del otoño.", instr="빈칸 채우기", size=20, gap=8)
e.head("D · EL PRETÉRITO INDEFINIDO", 25)
e.bridge("문장을 과거형으로 바꾸세요.")
e.ex("B1", "문장 바꾸기", "De la Fuente dio la lista el viernes.", "dar → dio",
     "De la Fuente da la lista el viernes. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 바꾸기", "La Roja abrió la fase en Londres.", "abrir → abrió",
     "La Roja abre la fase en Londres. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 바꾸기", "España jugó en Praga el jueves.", "jugar → jugó",
     "España juega en Praga el jueves. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 바꾸기", "Los convocados fueron a Las Rozas.", "ir의 과거형은 fueron",
     "Los convocados van a Las Rozas. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 바꾸기", "El grupo cerró la fase el domingo.", "cerrar → cerró",
     "El grupo cierra la fase el domingo. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-deporte.svg")
print("P4 saved, exercises so far:", len(REG))
