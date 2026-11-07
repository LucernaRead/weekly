# -*- coding: utf-8 -*-
"""Lucerna weekly COVER, W43 (19-25 Oct 2026), reader language SPANISH.

Source material: cover-backfill/headlines-w43.json ONLY (headlines + excerpts
verbatim, fixed order). Explanations in Spanish restate headline+excerpt only.
No VOL number on P1 (COVER badge instead); P8 carries masthead + VOL.
Page size 1950x2700, weekly visual system (ivory #f7f1e2, olive, serif).
Font faces per language so PIL measurement matches the audit's face_index:
  Latin + RU -> SC (2), JA -> JP (0), KO -> KR (1), zh-cn -> SC (2), zh-tw -> TC (3)
"""
import json, os
from PIL import ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/cover-backfill/headlines-w43.json")
OUT = os.path.join(BASE, "svg")
os.makedirs(OUT, exist_ok=True)

with open(SRC, encoding="utf-8") as f:
    ITEMS = json.load(f)
assert len(ITEMS) == 12, len(ITEMS)
ORDER = ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"]
assert [i["source_lang"] for i in ITEMS] == ORDER

# Spanish reader-language labels for the source languages
LABEL = {
    "en": "Inglés", "de": "Alemán", "fr": "Francés", "es": "Español",
    "it": "Italiano", "pt": "Portugués", "nl": "Neerlandés", "ru": "Ruso",
    "ja": "Japonés", "ko": "Coreano", "zh-cn": "Chino simplificado",
    "zh-tw": "Chino tradicional",
}
FACE = {"ja": 0, "ko": 1, "zh-tw": 3}  # default SC = 2
SUFFIX = {"ja": "JP", "ko": "KR", "zh-tw": "TC"}  # default SC

FONTS_DIR = "/usr/share/fonts/opentype/noto"
SERIF = os.path.join(FONTS_DIR, "NotoSerifCJK-Regular.ttc")
SERIF_B = os.path.join(FONTS_DIR, "NotoSerifCJK-Bold.ttc")
SANS = os.path.join(FONTS_DIR, "NotoSansCJK-Regular.ttc")
SANS_B = os.path.join(FONTS_DIR, "NotoSansCJK-Bold.ttc")
_cache = {}

def font(kind, bold, size, lang):
    idx = FACE.get(lang, 2)
    path = (SERIF_B if bold else SERIF) if kind == "serif" else (SANS_B if bold else SANS)
    key = (path, size, idx)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, size, index=idx)
    return _cache[key]

def text_w(s, kind, bold, size, lang):
    return font(kind, bold, size, lang).getlength(s) if s else 0.0

def wrap(text, kind, bold, size, max_w, lang):
    """Greedy wrap: Latin words whole, CJK chars individually."""
    lines, cur, buf, tokens = [], "", "", []
    for ch in text:
        if ord(ch) < 0x2E80 and ch != " ":
            buf += ch
        else:
            if buf:
                tokens.append(buf); buf = ""
            tokens.append(ch)
    if buf:
        tokens.append(buf)
    for tok in tokens:
        trial = cur + tok
        if text_w(trial, kind, bold, size, lang) <= max_w or not cur.strip():
            cur = trial
        else:
            lines.append(cur.rstrip())
            cur = tok.lstrip() if tok == " " else tok
    if cur.strip():
        lines.append(cur.rstrip())
    return lines

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

INK = "#28251d"; OLIVE = "#3e4c2a"; GOLD = "#b3a06a"; PAPER = "#f7f1e2"
BOX = "#fdfaf0"; LINE = "#d8cfb4"; GREY = "#57523f"; BRICK = "#a4553a"
W, H = 1950, 2700
MX = 110            # side margin (inside frame)
CW = W - 2 * MX     # content width 1730

def fam(kind, lang):
    suf = SUFFIX.get(lang, "SC")
    return ("Noto Serif CJK " + suf) if kind == "serif" else ("Noto Sans CJK " + suf)

class Page:
    def __init__(self):
        self.parts = [
            f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
            f'<rect x="26" y="26" width="{W-52}" height="{H-52}" fill="none" stroke="{INK}" stroke-width="3"/>',
            f'<rect x="37" y="37" width="{W-74}" height="{H-74}" fill="none" stroke="{INK}" stroke-width="1.2"/>',
        ]
    def add(self, s):
        self.parts.append(s)
    def text(self, x, y, s, size=28, kind="serif", bold=False, fill=INK, anchor="start", lang="es"):
        wt = ' font-weight="700"' if bold else ""
        self.add(f'<text x="{x}" y="{y}" font-family="{fam(kind, lang)}" font-size="{size}"{wt} fill="{fill}" text-anchor="{anchor}">{esc(s)}</text>')
        return y
    def para(self, x, y, s, size=28, kind="serif", bold=False, fill=INK, max_w=CW, lh=1.5, lang="es"):
        for ln in wrap(s, kind, bold, size, max_w, lang):
            self.text(x, y, ln, size, kind, bold, fill, lang=lang)
            y += size * lh
        return y
    def para_h(self, s, size, kind, bold, max_w, lh, lang):
        return len(wrap(s, kind, bold, size, max_w, lang)) * size * lh
    def hline(self, x1, x2, y, color=LINE, wdt=1.2):
        self.add(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="{wdt}"/>')
    def rect(self, x, y, w, h, fill="none", stroke=None, sw=1.2):
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"{st}/>')
    def footer(self, n):
        self.text(W // 2, 2624, f"La Lucerna · Portada semanal · Página {n} de 8", 28, "sans", False, GREY, anchor="middle", lang="es")
    def save(self, name):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
               f'viewBox="0 0 {W} {H}">' + "".join(self.parts) + "</svg>")
        path = os.path.join(OUT, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        return path

def masthead(p, y=210):
    p.text(W // 2, y, "La Lucerna", 150, "serif", True, INK, anchor="middle", lang="es")
    return y

def cover_badge(p):
    # Top-right COVER badge, clear of the masthead block.
    p.rect(1630, 78, 210, 64, fill=OLIVE)
    p.text(1735, 124, "COVER", 34, "sans", True, "#f7f1e2", anchor="middle", lang="es")

# --- Spanish explanations: restatements of headline + excerpt ONLY ---
EXPL = {
    "en": "En Estados Unidos la votación ya ha empezado: la votación anticipada se abrió el lunes 19 de octubre en Texas y en otros estados, antes del día de las elecciones, el 3 de noviembre.",
    "de": "Alemania retrasa los relojes en la noche del sábado al domingo: a las 3:00 el reloj vuelve a las 2:00, y once países tienen vacaciones esa semana.",
    "fr": "Aunque la elección presidencial es en 2027, los franceses ya hablan de ella: esta semana la búsqueda número uno en Google en Francia es sobre las encuestas de la presidencial de 2027.",
    "es": "Este domingo coinciden dos cosas en España: de madrugada cambia la hora y se duerme una hora más, y además se juega el Clásico.",
    "it": "En la noche del sábado 24 al domingo 25 de octubre, Italia vuelve a la hora solar: a las 03:00 el reloj retrocede a las 02:00, tras siete meses de horario de verano.",
    "pt": "El domingo 25 de octubre, de las 8:00 a las 17:00, hora de Brasilia, los brasileños vuelven a las urnas para la segunda vuelta de las elecciones a la Presidencia.",
    "nl": "Es una semana completa en los Países Bajos: las regiones Centro y Sur tienen vacaciones de otoño del 17 al 25 de octubre, el Norte vuelve a clase el lunes, y hay diseño, danza y una hora extra de sueño.",
    "ru": "Los meteorólogos esperan los primeros copos entre el miércoles y el viernes, del 21 al 23 de octubre, con temperaturas en torno a los cero grados.",
    "ja": "El primer partido de la Serie de Japón es el sábado 24 de octubre a las 18:30 en el estadio de Yokohama, entre los BayStars de DeNA y los Hawks de SoftBank, un duelo que no se veía desde hace dos años.",
    "ko": "El tifón número 30, Champi — un nombre aportado por Laos que significa flor — avanza hacia el norte, y la agencia meteorológica advirtió el 21 por la mañana de que es un tifón muy fuerte.",
    "zh-cn": "El Doble 11 llega temprano este año: JD empezó a vender productos en stock el 12 de octubre a las 20:00 y tiene su gran inicio el 20 a la misma hora, mientras Taobao y Tmall abrieron la preventa el 15 a las 20:00.",
    "zh-tw": "El fuerte tifón Jangmi se acerca al mar al este de Taiwán: el martes 20 por la noche su centro estaba a unos 1.390 kilómetros al este-sureste de Eluanbi, con vientos máximos de unos 60 metros por segundo, y el monzón del noreste hará que la lluvia sea mayor y más duradera.",
}

def build_p1():
    p = Page()
    cover_badge(p)
    masthead(p)
    p.text(W // 2, 300, "Semana del 19 al 25 de octubre de 2026", 40, "sans", False, GREY, anchor="middle", lang="es")
    p.hline(MX, W - MX, 340, GOLD, 3)
    y = 470
    y = p.text(W // 2, y, "Doce idiomas, una semana", 88, "serif", True, OLIVE, anchor="middle", lang="es")
    y += 70
    intro = ("Doce titulares, doce idiomas: esta portada reúne las noticias que abren la semana "
             "en cada edición de Lucerna, para leer el mundo en la lengua que estás aprendiendo.")
    y = p.para(MX, y, intro, 40, "serif", False, INK, max_w=CW, lh=1.5, lang="es")
    y += 45
    p.hline(MX, W - MX, y, GOLD, 2)
    y += 70
    _heights = []
    for _it in ITEMS:
        _hl = p.para_h(_it["headline"], 37, "serif", True, CW, 1.35, _it["source_lang"])
        _heights.append(42 + _hl)
    _gap = max(18, int((2500 - y - sum(_heights)) // 12))
    for it in ITEMS:
        lang = it["source_lang"]
        y = p.text(MX, y, LABEL[lang].upper() + "  ·  " + it["masthead"], 27, "sans", True, OLIVE, lang="es")
        y += 42
        y = p.para(MX, y, it["headline"], 37, "serif", True, INK, max_w=CW, lh=1.35, lang=lang)
        y += _gap
    assert y < 2560, f"P1 overflow: ends at {y}"
    p.footer(1)
    p.save("p1-cover.svg")

def build_item_pages():
    pairs = [(ITEMS[i], ITEMS[i + 1]) for i in range(0, 12, 2)]
    for pi, (a, b) in enumerate(pairs):
        p = Page()
        p.text(MX, 150, "La Lucerna · Portada semanal", 34, "sans", True, OLIVE, lang="es")
        p.text(W - MX, 150, "19–25 de octubre de 2026", 34, "sans", False, GREY, anchor="end", lang="es")
        p.hline(MX, W - MX, 185, GOLD, 2)
        y = 270
        for it in (a, b):
            lang = it["source_lang"]
            y = p.text(MX, y, LABEL[lang].upper() + "  ·  " + it["masthead"], 30, "sans", True, OLIVE, lang="es")
            y += 50
            y = p.para(MX, y, it["headline"], 50, "serif", True, INK, max_w=CW, lh=1.35, lang=lang)
            y += 28
            y = p.para(MX, y, it["excerpt"], 42, "serif", False, INK, max_w=CW, lh=1.5, lang=lang)
            y += 30
            y = p.text(MX, y, "EN ESPAÑOL", 27, "sans", True, BRICK, lang="es")
            y += 48
            y = p.para(MX, y, EXPL[lang], 42, "serif", False, GREY, max_w=CW, lh=1.5, lang="es")
            y += 55
            if it is a:
                p.hline(MX, W - MX, y, LINE, 1.5)
                y += 70
        assert y < 2560, f"P{pi+2} overflow: ends at {y}"
        p.footer(pi + 2)
        p.save(f"p{pi+2}-cover.svg")

def build_p8():
    p = Page()
    p.text(W // 2, 150, "La Lucerna", 110, "serif", True, INK, anchor="middle", lang="es")
    p.text(W // 2, 235, "Los 12 periódicos de la semana, de un vistazo", 44, "serif", False, OLIVE, anchor="middle", lang="es")
    p.text(W // 2, 300, "Semana del 19 al 25 de octubre de 2026", 36, "sans", False, GREY, anchor="middle", lang="es")
    p.hline(MX, W - MX, 340, GOLD, 3)
    y = 450
    _heights = []
    for _it in ITEMS:
        _hl = p.para_h(_it["headline"], 37, "serif", True, CW, 1.35, _it["source_lang"])
        _heights.append(42 + _hl)
    _gap = max(18, int((2500 - y - sum(_heights)) // 12))
    for it in ITEMS:
        lang = it["source_lang"]
        y = p.text(MX, y, f'{it["masthead"]} · VOL. {it["vol"]}  ·  {LABEL[lang]}', 28, "sans", True, OLIVE, lang="es")
        y += 42
        y = p.para(MX, y, it["headline"], 37, "serif", True, INK, max_w=CW, lh=1.35, lang=lang)
        y += _gap
    assert y < 2560, f"P8 overflow: ends at {y}"
    p.footer(8)
    p.save("p8-cover.svg")

build_p1()
build_item_pages()
build_p8()
print("SVGs written to", OUT)
for n in sorted(os.listdir(OUT)):
    print(" ", n, os.path.getsize(os.path.join(OUT, n)), "bytes")
