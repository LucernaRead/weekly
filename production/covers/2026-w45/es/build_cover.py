# -*- coding: utf-8 -*-
"""W45 weekly cover, reader language SPANISH. 8 pages, 1950x2700.
Headlines/excerpts loaded verbatim from cover-backfill/headlines-w45.json
at build time, never retyped. Explanations in Spanish, traceable to
headline+excerpt only (1-2 sentences each, no facts beyond the source).
Cover itself carries NO vol number (COVER mark instead); P8 lists each
core paper's own VOL (FR VOL.3, all others VOL.2, per task and JSON).
Cover-original Spanish text uses ASCII apostrophes only (none needed);
verbatim items are untouched (zh-tw stays Traditional, zh-cn Simplified).
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import Page, wrap, text_w, esc, INK, OLIVE, GOLD, PAPER, BOX, LINE, GREY

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "svg")
os.makedirs(OUT, exist_ok=True)

ITEMS = json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/cover-backfill/headlines-w45.json"))
assert [i["source_lang"] for i in ITEMS] == ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"], "fixed order changed!"
assert all(i["vol"] == (3 if i["source_lang"] == "fr" else 2) for i in ITEMS), "VOL mismatch vs task"
assert all(len(i["excerpt"].split(". ")) <= 4 or i["source_lang"] in ("ja", "ko", "zh-cn", "zh-tw", "ru") for i in ITEMS)

TABLES = json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/tools/tables.json"))
LANGS = TABLES["languages"]

# Spanish-language names for the source languages.
ES_NAME = {"en": "Inglés", "de": "Alemán", "fr": "Francés",
           "es": "Español", "it": "Italiano", "pt": "Portugués",
           "nl": "Neerlandés", "ru": "Ruso", "ja": "Japonés",
           "ko": "Coreano", "zh-cn": "Chino (simplificado)",
           "zh-tw": "Chino (tradicional)"}
FAMILY = {"en": "Noto Serif CJK SC", "de": "Noto Serif CJK SC", "fr": "Noto Serif CJK SC",
          "es": "Noto Serif CJK SC", "it": "Noto Serif CJK SC", "pt": "Noto Serif CJK SC",
          "nl": "Noto Serif CJK SC", "ru": "Noto Serif CJK SC",
          "ja": "Noto Serif CJK JP", "ko": "Noto Serif CJK KR",
          "zh-cn": "Noto Serif CJK SC", "zh-tw": "Noto Serif CJK TC"}

EXPLAIN = {
 "en": "Estados Unidos vota en unas elecciones de medio mandato, en mitad del mandato de cuatro años del presidente. Los 435 escaños de la Cámara de Representantes están en juego, junto con alrededor de un tercio del Senado y gobernaciones en muchos estados.",
 "de": "Una semana llena de fútbol: Liga de Campeones el martes y el miércoles, Liga Europa el jueves, y el viernes empieza la 9.ª jornada de la Bundesliga. Cuatro noches de fútbol y luego un fin de semana entero de liga, con el Bayern en casa del Atlético de Madrid el martes a las 21.00 y el Stuttgart en casa del Galatasaray a las 18.45.",
 "fr": "El lunes 2 de noviembre Francia retoma la actividad: terminan las vacaciones de Todos los Santos, los alumnos vuelven a clase y empieza una gran semana. Termina el fin de semana del 7 y 8 de noviembre con tres finales a la vez, entre ellas las finales del Rolex Paris Masters en Nanterre el domingo 8, el último gran torneo de tenis de la temporada.",
 "es": "España entra en la semana decisiva antes de la campaña: las listas ya están presentadas y ahora los partidos escriben sus programas. El domingo 29 de noviembre España vota en elecciones generales, y según la portada la vivienda decide la campaña.",
 "it": "El lunes 2 de noviembre Italia cambia de cara: llega el primer frío de verdad de la temporada, con lluvias en la vertiente adriática y la primera nieve ligera en montaña, en torno a los 1.300-1.500 metros. Las previsiones hablan de un noviembre más frío de la media, pero es una probabilidad, no una certeza.",
 "pt": "La semana empieza el lunes 2 de noviembre, festivo de Finados, y termina el domingo 8 con el primer día del Enem. Entre un día y otro, todo el país vive la misma semana: descansar, repasar y hacer la prueba, tras un puente que abre el sábado 31 de octubre.",
 "nl": "Del lunes 2 al domingo 8 de noviembre es la Semana del Clima en los Países Bajos: municipios de todo el país organizan acciones como plantar árboles, ahorrar energía y usar la bicicleta en lugar del coche. Cualquiera puede participar.",
 "ru": "Una semana poco habitual en Rusia: el lunes y el martes se trabaja, pero el miércoles es festivo. El miércoles 4 de noviembre cae en medio de la semana laboral.",
 "ja": "El Día de la Cultura es el martes 3 de noviembre, festivo en el que escuelas y empresas cierran y se celebran eventos culturales en todo el país. La portada anuncia también el fin de semana de las hojas de otoño.",
 "ko": "Del lunes 2 al domingo 8 de noviembre, esta es la semana en la que llega el invierno: el sábado 7 de noviembre es el ipdong, el primer término solar del invierno entre los 24. La portada marca también el final de las hojas de otoño y el inicio del kimjang.",
 "zh-cn": "El Doble 11 ya ha empezado: JD empezó a vender productos en stock el 12 de octubre a las 20.00, Taobao y Tmall abrieron las preventas el 15 de octubre a las 20.00, y el pago final y la venta en stock empezaron el 20 de octubre a las 20.00. La venta en stock seguirá hasta el 13 de noviembre, y la portada anuncia también la llegada del invierno.",
 "zh-tw": "La Semana FinTech de Hong Kong x StartmeupHK 2026 abre el lunes 2 de noviembre en Hong Kong y dura cinco días, hasta el viernes 6 de noviembre. Es un evento muy grande: se esperan más de 45.000 participantes, de más de 120 economías, con más de 1.000 ponentes y más de 800 expositores y empresas emergentes.",
}
assert set(EXPLAIN) == {i["source_lang"] for i in ITEMS}
# Cover-original text: no curly apostrophes anywhere in this file's own strings.
for _v in EXPLAIN.values():
    assert "\u2019" not in _v

W, H = 1950, 2700
MX, CW = 130, 1690
FOOT_Y = 2624

def new_page():
    return Page(W, H)

def header(p, label):
    p.text(975, 128, label, 30, "sans", False, GREY, anchor="middle")

def footer(p, num):
    p.hline(MX, MX + CW, 2570, LINE, 1.2)
    p.text(MX, FOOT_Y, "La Lucerna  ·  COVER  ·  2-8 de noviembre de 2026", 28, "sans", False, GREY)
    p.text(MX + CW, FOOT_Y, num, 28, "sans", False, GREY, anchor="end")

def para(p, x, y, s, size, kind, bold, fill, max_w, lh, family=None):
    for ln in wrap(s, kind, bold, size, max_w):
        p.text(x, y, ln, size, kind, bold, fill, family=family)
        y += size * lh
    return y

def tag_of(it):
    lang = it["source_lang"]
    return (ES_NAME[lang] + "  ·  " + LANGS[lang]["label"]).upper()

# ---------------- P1 ----------------
p = new_page()
header(p, "PORTADA SEMANAL  ·  2-8 DE NOVIEMBRE DE 2026")
p.text(975, 330, "La Lucerna", 168, "serif", True, INK, anchor="middle")
bw = text_w("C O V E R", "sans", True, 44) + 90
p.rect(975 - bw / 2, 385, bw, 78, fill=OLIVE, rx=10)
p.text(975, 440, "C O V E R", 44, "sans", True, PAPER, anchor="middle")
p.text(975, 560, "2-8 de noviembre de 2026", 52, "serif", False, OLIVE, anchor="middle")
p.hline(375, 1575, 620, GOLD, 3)
p.text(975, 740, "Doce portadas, una semana", 84, "serif", True, INK, anchor="middle")
y = para(p, 220, 850, "Doce periódicos, doce lenguas, una semana de noviembre: cada titular abre su propia portada, en su propia lengua, con una breve explicación en español sobre lo que dice y por qué llama la atención.", 46, "serif", False, GREY, 1510, 1.45)
y += 40
p.hline(MX, MX + CW, y, GOLD, 2)
y += 55
for it in ITEMS:
    p.text(MX, y, tag_of(it), 28, "sans", True, OLIVE)
    y += 38
    y = para(p, MX, y, it["headline"], 38, "serif", True, INK, CW, 1.28, family=FAMILY[it["source_lang"]])
    y += 14
    assert y < 2520, f"P1 overflow at {it['source_lang']}: y={y}"
footer(p, "1")
p.save(os.path.join(OUT, "p1-cover.svg"))
print(f"P1 ends y={y:.0f}")

# ---------------- P2-P7: two items per page ----------------
PAIRS = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
for pi, (a, b) in enumerate(PAIRS):
    p = new_page()
    header(p, "LA LUCERNA  ·  COVER  ·  2-8 DE NOVIEMBRE DE 2026")
    y = 210
    for idx in (a, b):
        it = ITEMS[idx]
        lang = it["source_lang"]
        p.text(MX, y, tag_of(it), 34, "sans", True, OLIVE)
        y += 64  # DE-build audit fix: tag ink must clear headline ink (TEXTX)
        y = para(p, MX, y, it["headline"], 60, "serif", True, INK, CW, 1.28, family=FAMILY[lang])
        y += 30
        y = para(p, MX, y, it["excerpt"], 44, "serif", False, INK, CW, 1.5, family=FAMILY[lang])
        y += 34
        p.hline(MX, MX + 180, y, GOLD, 2.5)
        y += 48
        p.text(MX, y, "QUÉ SIGNIFICA", 30, "sans", True, OLIVE)
        y += 46
        y = para(p, MX, y, EXPLAIN[lang], 44, "sans", False, GREY, CW, 1.5)
        y += 58
        if idx == a:
            p.hline(MX, MX + CW, y, LINE, 1.5)
            y += 62
        assert y < 2540, f"P{pi+2} overflow at {lang}: y={y}"
    footer(p, str(pi + 2))
    p.save(os.path.join(OUT, f"p{pi+2}-cover.svg"))
    print(f"P{pi+2} ends y={y:.0f}")

# ---------------- P8: twelve cores at a glance ----------------
p = new_page()
header(p, "LA LUCERNA  ·  COVER  ·  2-8 DE NOVIEMBRE DE 2026")
p.text(975, 300, "Los doce periódicos de esta semana", 88, "serif", True, INK, anchor="middle")
p.text(975, 390, "Los doce periódicos centrales detrás de esta portada, en orden.", 44, "serif", False, GREY, anchor="middle")
p.hline(MX, MX + CW, 440, GOLD, 3)
y = 520
for it in ITEMS:
    lang = it["source_lang"]
    vol = it["vol"]
    p.text(MX, y, f"{it['masthead']}  ·  VOL.{vol}", 36, "sans", True, OLIVE)
    y += 50
    y = para(p, MX, y, it["headline"], 44, "serif", True, INK, CW, 1.32, family=FAMILY[lang])
    y += 40
    assert y < 2520, f"P8 overflow at {lang}: y={y}"
footer(p, "8")
p.save(os.path.join(OUT, "p8-cover.svg"))
print(f"P8 ends y={y:.0f}")
print("OK: 8 SVGs in", OUT)
