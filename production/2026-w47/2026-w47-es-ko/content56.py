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
p.band("JUVENTUD　청년", "La Lucerna", "NIVEL B1　Votar por primera vez　처음 투표하기")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Votar por primera vez: el jueves 19 se cierra el plazo", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: B1")
f.para("¿Votas por primera vez el 29 de noviembre? Tienes dos maneras de votar: en persona o por correo.")
f.para("El voto por correo se pide desde la convocatoria y hasta el jueves 19 de noviembre, en cualquier oficina de Correos o por internet, en la web de Correos. La Oficina del Censo Electoral envía la documentación a la dirección indicada a partir del lunes 9 de noviembre. Después, votas en casa, con calma, y envías el sobre.")
f.para("Y si prefieres votar en persona, el domingo 29 los colegios electorales abren de 9:00 a 20:00, con tu documento de identidad. Novedad de este año: también vale identificarse con la aplicación oficial MiDNI en el móvil. La Junta Electoral Central levantó el 5 de noviembre la suspensión de la aplicación.")
f.para("Y el sábado 28, jornada de reflexión, no hay propaganda ni actos de campaña: un día de silencio antes de votar. Y el viernes 27, la otra cita joven de la semana: el Black Friday, con ofertas en las tiendas y en internet. Compra con cabeza: compara precios antes de pagar.")
f.box("EL PLAN DE LA SEMANA　이번 주 계획", [
    ("1. El lunes 16: Día del Flamenco y primer lunes de campaña(월요일: 플라멩코의 날과 선거운동 첫 주 월요일)", "serif", False, INK, 21, 1.36),
    ("2. El jueves 19: último día para pedir el voto por correo(목요일: 우편 투표 신청 마감일)", "serif", False, INK, 21, 1.36),
    ("3. El viernes 20: vuelve la Liga, Athletic–Espanyol, 21:00(금요일 저녁: 리그가 돌아와요)", "serif", False, INK, 21, 1.36),
    ("4. El sábado 21: derbi Sevilla–Betis, 18:30(토요일: 세비야 더비)", "serif", False, INK, 21, 1.36),
    ("5. El domingo 22: Barça–Villarreal, 14:00; Santa Cecilia(일요일: 바르사 대 비야레알; 성녀 체칠리아 축일)", "serif", False, INK, 21, 1.36),
], tsize=20)
f.gloss("el sobre는 봉투예요 · la papeleta는 투표 용지예요 · el censo는 선거인 명부예요 · el plazo는 기한이에요 · la urna는 투표함이에요.")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("우편 투표를 할까요, 직접 가서 투표할까요? 블랙프라이데이에는 무엇을 살 거예요? 실용적인 것, 아니면 충동적인 것? 두 문장을 써서 보내세요.", "sans", False, 19, CW - 44)) * 27 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　당신은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "우편 투표를 할까요, 직접 가서 투표할까요? 블랙프라이데이에는 무엇을 살 거예요? 실용적인 것, 아니면 충동적인 것? 두 문장을 써서 보내세요.", 19, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　5면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "답은 8면에　문제는 급이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　COMPRENSIÓN", 25)
e.bridge("5면 글을 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "B", "우편 투표는 19일까지 신청해야 해요",
     "El voto por correo se pide hasta... A. el lunes 9 · B. el jueves 19 · C. el domingo 29", size=20, gap=8)
e.ex("B1", "객관식", "A", "서류는 11월 9일부터 발송돼요",
     "La documentación del voto por correo llega desde... A. el lunes 9 · B. el viernes 13 · C. el sábado 28", size=20, gap=8)
e.ex("B1", "객관식", "C", "투표소는 9:00부터 20:00까지 열려요",
     "El domingo 29, los colegios abren... A. todo el día · B. de noche · C. de 9:00 a 20:00", size=20, gap=8)
e.ex("B1", "객관식", "B", "MiDNI는 올해 투표할 때 신분을 확인하는 새로운 방법이에요",
     "Para votar en persona, este año también vale... A. un billete · B. la aplicación MiDNI · C. una entrada", size=20, gap=8)
e.ex("B1", "객관식", "A", "블랙프라이데이, 11월 27일 금요일",
     "El Black Friday es el... A. viernes 27 · B. lunes 16 · C. domingo 29", size=20, gap=8)
e.head("B　PALABRAS DEL TEXTO", 25)
e.bridge("네모 안의 단어로 빈칸을 채우세요. 주의: 활용이 필요한 단어가 있어요.")
e.para("sobre · papeleta · censo · identidad · plazo · urna", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "correo", "correo = 우체국 / 우편",
     "Pido el voto por ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "papeleta", "papeleta = 투표용지",
     "En casa, relleno la ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "envío", "enviar 활용 → envío",
     "Después ___(원형: enviar) el sobre.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "identidad", "documento de identidad = 신분증",
     "Para votar en persona llevo mi documento de ___.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "censo", "censo = 유권자 명부",
     "La Oficina del ___ envía la documentación.", instr="빈칸 채우기", size=20, gap=8)
e.ex("B1", "문장 완성", "plazo", "plazo = 기한(19일 마감)",
     "El jueves 19 termina el ___ del voto por correo.", instr="빈칸 채우기", size=20, gap=8)
e.head("C　IR A + INFINITIVO", 25)
e.bridge("ir a + 동사 원형으로 문장을 바꿔 '~할 것'이라는 뜻을 나타내세요.")
e.ex("B1", "문장 바꾸기", "Voy a pedir el voto por correo.", "voy a + 원형",
     "Pido el voto por correo. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 바꾸기", "Vas a votar el domingo 29.", "vas a + 원형",
     "Votas el domingo 29. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 바꾸기", "Va a abrirse la urna a las 9:00.", "va a + 원형",
     "La urna se abre a las 9:00. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 바꾸기", "Van a comparar precios antes de pagar.", "van a + 원형",
     "Comparan precios antes de pagar. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.head("D　¿VERDADERO O FALSO?", 25)
e.ex("B1", "읽기 판단", "Verdadero", "우편 투표는 Correos에서 신청해요",
     "El voto por correo se pide en una oficina de Correos. ¿Verdadero o falso?", instr="참 / 거짓", size=20, gap=8)
e.ex("B1", "읽기 판단", "Falso", "묵상의 날은 토요일 28일이에요, 일요일이 아니에요",
     "La jornada de reflexión es el domingo 29. ¿Verdadero o falso?", instr="참 / 거짓", size=20, gap=8)
e.ex("B1", "읽기 판단", "Verdadero", "올해는 MiDNI로 투표할 수 있어요",
     "Este año se puede votar identificándose con MiDNI. ¿Verdadero o falso?", instr="참 / 거짓", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-juventud.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · A FONDO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("A FONDO　심층", "La Lucerna", "NIVEL B2　Leer la campaña: debates, programas y encuestas　선거운동 읽기: 토론, 공약, 여론조사")

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
p.text(MX, ey + 28, "EJERCICIOS　6면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "답은 8면에　문제는 급이 섞여 있어요, 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEER LOS GRÁFICOS", 25)
e.bridge("위 두 그래프를 보고 정답을 고르세요.")
e.ex("B2", "객관식", "A", "PSOE와 PP에 각각 무료 45분",
     "El PSOE y el PP tienen en RTVE... A. 45 minutos · B. 30 minutos · C. 15 minutos", size=18.5, gap=2)
e.ex("B2", "객관식", "B", "무료 방송 총 195분",
     "La propaganda gratuita en RTVE suma... A. 120 minutos · B. 195 minutos · C. 45 minutos", size=18.5, gap=2)
e.ex("B2", "객관식", "C", "Podemos: 15분",
     "Podemos tiene en RTVE... A. 45 minutos · B. 30 minutos · C. 15 minutos", size=18.5, gap=2)
e.ex("B2", "객관식", "A", "여론조사 발표 금지 5일(11월 24~28일)",
     "Prohibido publicar encuestas durante... A. 5 días · B. 15 días · C. 1 día", size=18.5, gap=2)
e.ex("B2", "객관식", "B", "45 − 30 = 15",
     "Entre el PSOE y Vox hay... A. 30 minutos · B. 15 minutos · C. 45 minutos", size=18.5, gap=2)
e.ex("B2", "객관식", "C", "선거관리위원회가 발표한 무료 방송 시간만 출처와 함께 실어요",
     "La Lucerna publica aquí... A. una media mezclada · B. todos los sondeos · C. solo datos oficiales, con fuente", size=18.5, gap=2)
e.head("B　COMPRENSIÓN", 25)
e.ex("B2", "객관식", "B", "11월 10일 기준으로 확정된 토론은 laSexta 토론뿐이에요",
     "El único debate cerrado es... A. el cara a cara · B. el de laSexta · C. el debate a cuatro", size=18.5, gap=2)
e.ex("B2", "객관식", "A", "laSexta 토론, 11월 13일 금요일 21:30",
     "El debate de portavoces es el... A. viernes 13, a las 21:30 · B. lunes 16 · C. jueves 26", size=18.5, gap=2)
e.ex("B2", "객관식", "C", "“제안된 것”이 “확정된 것”과 같지 않아요",
     "Un debate «propuesto» es... A. cerrado · B. en la tele · C. aún sin confirmar", size=18.5, gap=2)
e.ex("B2", "객관식", "B", "여론조사는 오차 있는 하루의 사진이에요",
     "Según el texto, una encuesta es... A. un resultado final · B. una foto con margen de error · C. una promesa", size=18.5, gap=2)
e.head("C　EL SUBJUNTIVO", 25)
e.ex("B2", "문장 완성", "tenga", "es posible que + 접속법: tenga",
     "Es posible que el debate ___ (tener) cuatro portavoces.", instr="빈칸 채우기", size=18.5, gap=2)
e.ex("B2", "문장 완성", "sea", "es importante que + 접속법: sea",
     "Es importante que cada dato ___ (ser) claro.", instr="빈칸 채우기", size=18.5, gap=2)
e.ex("B2", "문장 완성", "para que", "para que + 접속법 (목적)",
     "Publicamos la fuente ___ todos puedan comprobarla.", instr="빈칸 채우기", size=18.5, gap=2)
e.ex("B2", "문장 완성", "Aunque", "Aunque + 직설법 (이미 아는 사실)",
     "___ los debates difieren, ninguno miente.", instr="빈칸 채우기", size=18.5, gap=2)
e.head("D　PALABRAS DEL DEBATE", 25)
e.bridge("네모 안의 단어로 빈칸을 채우세요: sondeo · muestra · indecisos · margen de error")
e.ex("B2", "문장 완성", "sondeo", "sondeo = 여론조사",
     "Un ___ pregunta a una muestra de ciudadanos.", instr="빈칸 채우기", size=18.5, gap=2)
e.ex("B2", "문장 완성", "muestra", "muestra = 표본",
     "El sondeo preguntó a una ___ de ciudadanos.", instr="빈칸 채우기", size=18.5, gap=2)
e.ex("B2", "문장 완성", "indecisos", "indecisos = 아직 못 정한 사람",
     "Los ___ todavía no saben a quién votar.", instr="빈칸 채우기", size=18.5, gap=2)
e.ex("B2", "문장 완성", "margen de error", "margen de error = 오차 범위",
     "Toda encuesta tiene un ___.", instr="빈칸 채우기", size=18.5, gap=2)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-afondo.svg")
print("P6 saved, exercises so far:", len(REG))
