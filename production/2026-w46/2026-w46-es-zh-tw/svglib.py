# -*- coding: utf-8 -*-
"""SVG weekly-paper builder: PIL-measured text layout + line-art illustrations."""
from PIL import ImageFont
import os

FONTS_DIR = "/usr/share/fonts/opentype/noto"
NEWS_DIR = "/home/hatch/.local/share/fonts"
DEJAVU_DIR = "/usr/share/fonts/truetype/dejavu"

def _sc_index(path):
    for i in range(12):
        try:
            f = ImageFont.truetype(path, 40, index=i)
            if f.getname()[0].endswith("SC"):
                return i
        except Exception:
            break
    return 0

_SERIF = os.path.join(FONTS_DIR, "NotoSerifCJK-Regular.ttc")
_SERIF_B = os.path.join(FONTS_DIR, "NotoSerifCJK-Bold.ttc")
_SANS = os.path.join(FONTS_DIR, "NotoSansCJK-Regular.ttc")
_SANS_B = os.path.join(FONTS_DIR, "NotoSansCJK-Bold.ttc")
_IDX = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}
_NEWS = os.path.join(NEWS_DIR, "Newsreader-Regular.ttf")
_NEWS_B = os.path.join(NEWS_DIR, "Newsreader-SemiBold.ttf")
_NEWS_I = os.path.join(NEWS_DIR, "Newsreader-Italic.ttf")
_DEJA = os.path.join(DEJAVU_DIR, "DejaVuSans.ttf")
_DEJA_B = os.path.join(DEJAVU_DIR, "DejaVuSans-Bold.ttf")
_cache = {}

# --- per-character font choice (SOP 1.1) -------------------------------------
# CairoSVG does NOT do per-glyph fallback for a font-family stack (verified:
# "Newsreader, Noto Serif CJK SC" renders CJK as tofu). So each character is
# assigned to the first font (in preference order) whose cmap contains it, and
# text is emitted as one <text> per maximal same-font run with PIL-measured x.
# serif: Newsreader (Latin) -> Noto Serif CJK SC -> DejaVu Sans (symbols only)
# sans:  Noto Sans CJK SC -> DejaVu Sans. Bold uses the 600/700 variants.
# Italic (SOP 1.1: the weekly word): Latin chars in an italic run use
# Newsreader-Italic; CJK/symbols stay upright (no italic CJK face exists).
# Bold+italic falls back to regular italic (no bold-italic face shipped).
from fontTools.ttLib import TTFont as _TTFont
def _cmap(path, index=0):
    return _TTFont(path, fontNumber=index).getBestCmap()
_CMAP = {
    "news": _cmap(_NEWS), "news_b": _cmap(_NEWS_B), "news_i": _cmap(_NEWS_I),
    "serif": _cmap(_SERIF, _IDX[_SERIF]), "serif_b": _cmap(_SERIF_B, _IDX[_SERIF_B]),
    "sans": _cmap(_SANS, _IDX[_SANS]), "sans_b": _cmap(_SANS_B, _IDX[_SANS_B]),
    "deja": _cmap(_DEJA), "deja_b": _cmap(_DEJA_B),
}
_FAMILY = {"news": "Newsreader", "news_i": "Newsreader",
           "serif": "Noto Serif CJK SC",
           "sans": "Noto Sans CJK SC", "deja": "DejaVu Sans"}
_PATH = {
    ("serif", False, "news"): _NEWS, ("serif", True, "news"): _NEWS_B,
    ("serif", False, "news_i"): _NEWS_I, ("serif", True, "news_i"): _NEWS_I,
    ("serif", False, "serif"): _SERIF, ("serif", True, "serif"): _SERIF_B,
    ("serif", False, "deja"): _DEJA, ("serif", True, "deja"): _DEJA_B,
    ("sans", False, "sans"): _SANS, ("sans", True, "sans"): _SANS_B,
    ("sans", False, "deja"): _DEJA, ("sans", True, "deja"): _DEJA_B,
}
_IDX2 = {("serif", False, "serif"): _IDX[_SERIF], ("serif", True, "serif"): _IDX[_SERIF_B],
         ("sans", False, "sans"): _IDX[_SANS], ("sans", True, "sans"): _IDX[_SANS_B]}

def _char_font(ch, kind, bold, italic=False):
    cp = ord(ch)
    if kind == "serif":
        if italic and cp in _CMAP["news_i"]:
            return "news_i"
        if cp in _CMAP["news_b" if bold else "news"]:
            return "news"
        if cp in _CMAP["serif_b" if bold else "serif"]:
            return "serif"
        return "deja"
    if cp in _CMAP["sans_b" if bold else "sans"]:
        return "sans"
    return "deja"

def _pil(kind, bold, cls, size):
    key = (kind, bold, cls, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(_PATH[(kind, bold, cls)], size,
                                         index=_IDX2.get((kind, bold, cls), 0))
    return _cache[key]

def _runs(s, kind, bold, italic=False):
    """Split s into maximal runs sharing one font. Returns [(text, cls)]."""
    runs, cur, curcls = [], "", None
    for ch in s:
        cls = _char_font(ch, kind, bold, italic)
        if cls == curcls:
            cur += ch
        else:
            if cur:
                runs.append((cur, curcls))
            cur, curcls = ch, cls
    if cur:
        runs.append((cur, curcls))
    return runs

def text_w(s, kind, bold, size, italic=False):
    if not s:
        return 0.0
    return sum(_pil(kind, bold, cls, size).getlength(t) for t, cls in _runs(s, kind, bold, italic))

def _breakable(ch):
    return ch == " "

def wrap(text, kind, bold, size, max_w, italic=False):
    """Greedy wrap: Latin words kept whole where possible, CJK per char."""
    lines, cur = [], ""
    tokens = []
    buf = ""
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
        if text_w(trial, kind, bold, size, italic) <= max_w or not cur.strip():
            cur = trial
        else:
            lines.append(cur.rstrip())
            cur = tok.lstrip() if tok == " " else tok
    if cur.strip():
        lines.append(cur.rstrip())
    return lines

# --- three-colour moth (brand mark) on the masthead rule ----------------------
# Inner XML of assets/lucerna-moth.svg (design sample), inlined so the build
# does not depend on the design worktree. viewBox 64 120 384 284 (384x284).
import re as _re
_MOTH_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "lucerna-moth.svg")
with open(_MOTH_PATH, encoding="utf-8") as _f:
    _MOTH_SVG = _re.sub(r"^<svg[^>]*>|</svg>\s*$", "", _f.read().strip())

def moth(p, cx, y, w=96):
    """Draw the moth centred on (cx, y): w px wide, aspect 384:284."""
    h = w * 284 / 384.0
    p.add(f'<svg x="{cx - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w}" height="{h:.1f}" '
          f'viewBox="64 120 384 284">{_MOTH_SVG}</svg>')

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

INK = "#302c28"; OLIVE = "#46581f"; PAPER = "#fbfaf6"
CLOTH = "#37402f"; GOOSE = "#f6e08e"; ONCLOTH = "#f4efe1"
BOX = "#f0eee5"; LINE = "#d8d2c4"; GREY = "#6f675d"

class Page:
    def __init__(self, w=1080, h=1440):
        self.w, self.h = w, h
        self.parts = []
        self.add(f'<rect width="{w}" height="{h}" fill="{PAPER}"/>')

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, size=28, kind="serif", bold=False, fill=INK, anchor="start", spacing=None, family=None, italic=False):
        # Explicit single family (e.g. the UnifrakturMaguntia masthead): one
        # element; CairoSVG anchors single-font text correctly.
        # (italic is ignored here: no italic face exists for a fixed family.)
        if family is not None:
            sp = f' letter-spacing="{spacing}"' if spacing else ""
            wt = ' font-weight="700"' if bold else ""
            self.add(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}"{wt} fill="{fill}" text-anchor="{anchor}"{sp}>{esc(s)}</text>')
            return y
        if not s:
            return y
        # Mixed text: one <text> per same-font run, x positions measured with
        # PIL (CairoSVG mis-measures text-anchor on multi-font <tspan> runs).
        runs = _runs(s, kind, bold, italic)
        sp = spacing or 0
        total = sum(_pil(kind, bold, cls, size).getlength(t) for t, cls in runs) + sp * (len(s) - 1)
        if anchor == "middle":
            cur = x - total / 2.0
        elif anchor == "end":
            cur = x - total
        else:
            cur = x
        wt = ' font-weight="700"' if bold else ""
        spattr = f' letter-spacing="{spacing}"' if spacing else ""
        for i, (t, cls) in enumerate(runs):
            w = _pil(kind, bold, cls, size).getlength(t)
            it = ' font-style="italic"' if cls == "news_i" else ""
            self.add(f'<text x="{cur:.1f}" y="{y}" font-family="{_FAMILY[cls]}" font-size="{size}"{wt}{it} fill="{fill}" text-anchor="start"{spattr}>{esc(t)}</text>')
            # next run starts after this run's rendered span (incl. its
            # trailing letter-spacing) plus one boundary spacing unit.
            cur += w + (sp * len(t) if i < len(runs) - 1 else 0)
        return y

    def para(self, x, y, s, size=28, kind="serif", bold=False, fill=INK, max_w=900, lh=1.5, anchor="start", italic=False):
        for ln in wrap(s, kind, bold, size, max_w, italic):
            self.text(x, y, ln, size, kind, bold, fill, anchor, italic=italic)
            y += size * lh
        return y

    def hline(self, x1, x2, y, color=LINE, wdt=1.2):
        self.add(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="{wdt}"/>')

    def rect(self, x, y, w, h, fill="none", stroke=None, sw=1.2, rx=0):
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st}/>')

    def section_head(self, x, y, s, size=31, color=OLIVE, rule_to=1016):
        self.text(x, y, s, size, "sans", True, color)
        self.hline(x, rule_to, y + 14, OLIVE, 2)
        return y + 14

    def save(self, path):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
               f'viewBox="0 0 {self.w} {self.h}">' + "".join(self.parts) + "</svg>")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        return path

# ---------------- line-art illustrations (stroke style) ----------------
def _g(p, inner):
    p.add(f'<g fill="none">{inner}</g>')

def illus_climb(p, x, y, s=1.0):
    """Mountains, sun, two stick climbers, chrysanthemums — for 重陽."""
    st = f'stroke="{INK}" stroke-width="{3.2*s}" stroke-linecap="round" stroke-linejoin="round"'
    _g(p, f'''
    <circle cx="{x+150*s}" cy="{y+26*s}" r="{17*s}" fill="{GOOSE}" {st}/>
    <path d="M{x} {y+120*s} L{x+70*s} {y+52*s} L{x+118*s} {y+96*s} L{x+168*s} {y+40*s} L{x+238*s} {y+120*s}" {st}/>
    <path d="M{x+30*s} {y+120*s} L{x+92*s} {y+74*s} L{x+128*s} {y+120*s}" {st}/>
    <circle cx="{x+98*s}" cy="{y+66*s}" r="{6.5*s}" fill="{INK}"/>
    <path d="M{x+98*s} {y+73*s} L{x+96*s} {y+90*s} L{x+86*s} {y+104*s} M{x+96*s} {y+90*s} L{x+108*s} {y+100*s} M{x+97*s} {y+78*s} L{x+110*s} {y+70*s}" {st}/>
    <circle cx="{x+128*s}" cy="{y+84*s}" r="{6*s}" fill="{INK}"/>
    <path d="M{x+128*s} {y+90*s} L{x+130*s} {y+104*s} L{x+121*s} {y+114*s} M{x+130*s} {y+104*s} L{x+140*s} {y+110*s}" {st}/>
    <g fill="{OLIVE}">
      <circle cx="{x+196*s}" cy="{y+112*s}" r="{5*s}"/><circle cx="{x+208*s}" cy="{y+104*s}" r="{6*s}"/>
      <circle cx="{x+218*s}" cy="{y+114*s}" r="{5*s}"/><circle cx="{x+206*s}" cy="{y+118*s}" r="{4.4*s}"/>
    </g>
    <path d="M{x+206*s} {y+120*s} L{x+206*s} {y+132*s}" {st}/>''')

def illus_frost(p, x, y, s=1.0):
    st = f'stroke="{OLIVE}" stroke-width="{3*s}" stroke-linecap="round"'
    cx, cy, r = x + 34*s, y + 34*s, 30*s
    _g(p, f'''
    <g {st}>
      <line x1="{cx-r}" y1="{cy}" x2="{cx+r}" y2="{cy}"/>
      <line x1="{cx-r*0.5}" y1="{cy-r*0.87}" x2="{cx+r*0.5}" y2="{cy+r*0.87}"/>
      <line x1="{cx+r*0.5}" y1="{cy-r*0.87}" x2="{cx-r*0.5}" y2="{cy+r*0.87}"/>
      <path d="M{cx-r} {cy} l{10*s} {-7*s} M{cx-r} {cy} l{10*s} {7*s} M{cx+r} {cy} l{-10*s} {-7*s} M{cx+r} {cy} l{-10*s} {7*s}"/>
      <circle cx="{cx}" cy="{cy}" r="{5*s}"/>
    </g>''')

def illus_flame(p, x, y, s=1.0):
    _g(p, f'''<path d="M{x+18*s} {y+2*s} C {x+30*s} {y+16*s}, {x+34*s} {y+22*s}, {x+34*s} {y+32*s}
      a16 {16*s} 16 0 1 1 -32 0 C {x+2*s} {y+24*s}, {x+8*s} {y+18*s}, {x+12*s} {y+12*s}
      C {x+13*s} {y+18*s}, {x+15*s} {y+20*s}, {x+17*s} {y+21*s} C {x+16*s} {y+12*s}, {x+16*s} {y+7*s}, {x+18*s} {y+2*s} Z"
      fill="{OLIVE}" stroke="{INK}" stroke-width="{2.4*s}"/>''')

def illus_fox(p, x, y, s=1.0):
    st = f'stroke="{INK}" stroke-width="{3*s}" stroke-linejoin="round"'
    _g(p, f'''
    <path d="M{x+8*s} {y+6*s} L{x+34*s} {y+30*s} L{x+62*s} {y+6*s} L{x+66*s} {y+44*s} L{x+35*s} {y+78*s} L{x+4*s} {y+44*s} Z" {st} fill="{BOX}"/>
    <path d="M{x+8*s} {y+6*s} L{x+22*s} {y+26*s} M{x+62*s} {y+6*s} L{x+48*s} {y+26*s}" {st}/>
    <circle cx="{x+24*s}" cy="{y+42*s}" r="{3.2*s}" fill="{INK}"/>
    <circle cx="{x+46*s}" cy="{y+42*s}" r="{3.2*s}" fill="{INK}"/>
    <path d="M{x+30*s} {y+56*s} L{x+40*s} {y+56*s} L{x+35*s} {y+63*s} Z" fill="{OLIVE}"/>''')

def illus_thinker(p, x, y, s=1.0):
    st = f'stroke="{INK}" stroke-width="{3*s}" stroke-linecap="round"'
    _g(p, f'''
    <circle cx="{x+35*s}" cy="{y+32*s}" r="{26*s}" {st}/>
    <path d="M{x+35*s} {y+32*s} m{-12*s} 0 a12 12 0 1 1 12 12 a8 8 0 1 0 -8 -8 a5 5 0 1 1 5 5" {st}/>
    <path d="M{x+35*s} {y+58*s} L{x+35*s} {y+72*s} M{x+20*s} {y+78*s} L{x+50*s} {y+78*s}" {st}/>''')

def illus_fish(p, x, y, s=1.0):
    st = f'stroke="{INK}" stroke-width="{3*s}" stroke-linejoin="round"'
    _g(p, f'''
    <path d="M{x+2*s} {y+30*s} Q{x+16*s} {y+16*s}, {x+32*s} {y+30*s} Q{x+16*s} {y+44*s}, {x+2*s} {y+30*s} Z" {st} fill="{BOX}"/>
    <path d="M{x+32*s} {y+30*s} L{x+42*s} {y+20*s} L{x+42*s} {y+40*s} Z" {st}/>
    <circle cx="{x+11*s}" cy="{y+27*s}" r="{2.6*s}" fill="{INK}"/>
    <path d="M{x+52*s} {y+30*s} L{x+70*s} {y+30*s} M{x+64*s} {y+23*s} L{x+71*s} {y+30*s} L{x+64*s} {y+37*s}" {st}/>
    <path d="M{x+82*s} {y+26*s} Q{x+104*s} {y+4*s}, {x+128*s} {y+26*s} Q{x+104*s} {y+50*s}, {x+82*s} {y+26*s} Z" {st} fill="{BOX}"/>
    <path d="M{x+128*s} {y+26*s} L{x+142*s} {y+12*s} L{x+142*s} {y+40*s} Z" {st}/>
    <circle cx="{x+94*s}" cy="{y+22*s}" r="{3*s}" fill="{INK}"/>''')

def illus_island(p, x, y, s=1.0):
    st = f'stroke="{INK}" stroke-width="{3*s}" stroke-linecap="round" stroke-linejoin="round"'
    _g(p, f'''
    <circle cx="{x+116*s}" cy="{y+18*s}" r="{12*s}" fill="{GOOSE}" {st}/>
    <path d="M{x+6*s} {y+62*s} Q{x+40*s} {y+38*s}, {x+76*s} {y+62*s}" {st}/>
    <path d="M{x+52*s} {y+50*s} L{x+52*s} {y+30*s} L{x+70*s} {y+40*s} L{x+52*s} {y+40*s}" {st}/>
    <path d="M{x+0*s} {y+74*s} q{10*s} {-8*s} {20*s} 0 t{20*s} 0 t{20*s} 0 t{20*s} 0 t{20*s} 0 t{20*s} 0" {st}/>
    <path d="M{x+10*s} {y+88*s} q{10*s} {-8*s} {20*s} 0 t{20*s} 0 t{20*s} 0 t{20*s} 0" {st}/>''')

def illus_sisyphus(p, x, y, s=1.0):
    st = f'stroke="{INK}" stroke-width="{3.4*s}" stroke-linecap="round"'
    _g(p, f'''
    <path d="M{x} {y+104*s} L{x+150*s} {y+30*s}" {st}/>
    <circle cx="{x+96*s}" cy="{y+38*s}" r="{21*s}" fill="{BOX}" {st}/>
    <circle cx="{x+52*s}" cy="{y+52*s}" r="{7*s}" fill="{INK}"/>
    <path d="M{x+54*s} {y+59*s} L{x+66*s} {y+74*s} L{x+56*s} {y+92*s} M{x+66*s} {y+74*s} L{x+82*s} {y+80*s} M{x+56*s} {y+64*s} L{x+78*s} {y+52*s}" {st}/>''')

def illus_moon(p, x, y, s=1.0):
    st = f'stroke="{INK}" stroke-width="{3*s}" stroke-linejoin="round"'
    _g(p, f'''
    <path d="M{x+52*s} {y+6*s} A30 30 0 1 0 {x+52*s} {y+58*s} A24 24 0 1 1 {x+52*s} {y+6*s} Z" fill="{GOOSE}" {st}/>
    <path d="M{x+6*s} {y+84*s} L{x+96*s} {y+84*s} M{x+12*s} {y+84*s} L{x+12*s} {y+70*s} L{x+40*s} {y+70*s} L{x+40*s} {y+84*s}" {st}/>
    <path d="M{x+46*s} {y+76*s} L{x+92*s} {y+76*s} L{x+92*s} {y+84*s}" {st}/>
    <path d="M{x+104*s} {y+66*s} q{10*s} {-12*s} {20*s} 0 q{-4*s} {10*s} {-10*s} {12*s} q{-6*s} {-2*s} {-10*s} {-12*s} Z" fill="{BOX}" {st}/>''')

def illus_sprout(p, x, y, s=1.0):
    st = f'stroke="{INK}" stroke-width="{3*s}" stroke-linecap="round"'
    _g(p, f'''
    <path d="M{x+50*s} {y+78*s} L{x+50*s} {y+44*s}" {st}/>
    <path d="M{x+50*s} {y+52*s} Q{x+28*s} {y+50*s}, {x+24*s} {y+30*s} Q{x+44*s} {y+30*s}, {x+50*s} {y+44*s}" fill="{OLIVE}"/>
    <path d="M{x+50*s} {y+46*s} Q{x+72*s} {y+44*s}, {x+76*s} {y+24*s} Q{x+56*s} {y+24*s}, {x+50*s} {y+38*s}" fill="{OLIVE}"/>
    <path d="M{x+8*s} {y+86*s} Q{x+30*s} {y+68*s}, {x+50*s} {y+84*s} Q{x+70*s} {y+68*s}, {x+92*s} {y+86*s}" {st}/>
    <circle cx="{x+84*s}" cy="{y+16*s}" r="{9*s}" fill="{GOOSE}" {st}/>''')

def illus_book(p, x, y, s=1.0):
    st = f'stroke="{INK}" stroke-width="{3*s}" stroke-linejoin="round"'
    _g(p, f'''
    <path d="M{x+35*s} {y+14*s} Q{x+18*s} {y+4*s}, {x+4*s} {y+10*s} L{x+4*s} {y+56*s} Q{x+18*s} {y+50*s}, {x+35*s} {y+60*s} Q{x+52*s} {y+50*s}, {x+66*s} {y+56*s} L{x+66*s} {y+10*s} Q{x+52*s} {y+4*s}, {x+35*s} {y+14*s} Z" {st} fill="{BOX}"/>
    <line x1="{x+35*s}" y1="{y+14*s}" x2="{x+35*s}" y2="{y+60*s}" {st}/>
    <path d="M{x+35*s} {y+30*s} Q{x+44*s} {y+18*s}, {x+54*s} {y+24*s} Q{x+46*s} {y+34*s}, {x+35*s} {y+30*s}" fill="{OLIVE}"/>''')

def illus_voto(p, x, y, s=1.0):
    """Ballot box with envelope and pencil — line art for the campaign / postal-vote lead."""
    st = 'stroke="' + INK + '" stroke-width="' + str(3*s) + '" stroke-linecap="round" stroke-linejoin="round"'
    inner = (
        '<rect x="' + str(x+20*s) + '" y="' + str(y+56*s) + '" width="' + str(150*s) + '" height="' + str(84*s) + '" fill="' + BOX + '" ' + st + '/>'
        '<rect x="' + str(x+8*s) + '" y="' + str(y+44*s) + '" width="' + str(174*s) + '" height="' + str(16*s) + '" fill="' + GOOSE + '" ' + st + '/>'
        '<rect x="' + str(x+74*s) + '" y="' + str(y+48*s) + '" width="' + str(42*s) + '" height="' + str(8*s) + '" fill="' + INK + '"/>'
        '<path d="M' + str(x+62*s) + ' ' + str(y+44*s) + ' L' + str(x+82*s) + ' ' + str(y+8*s) + ' L' + str(x+118*s) + ' ' + str(y+8*s) + ' L' + str(x+138*s) + ' ' + str(y+44*s) + '" fill="' + BOX + '" ' + st + '/>'
        '<path d="M' + str(x+82*s) + ' ' + str(y+8*s) + ' L' + str(x+100*s) + ' ' + str(y+30*s) + ' L' + str(x+118*s) + ' ' + str(y+8*s) + '" fill="none" ' + st + '/>'
        '<path d="M' + str(x+196*s) + ' ' + str(y+110*s) + ' L' + str(x+226*s) + ' ' + str(y+58*s) + '" ' + st + '/>'
        '<path d="M' + str(x+226*s) + ' ' + str(y+58*s) + ' L' + str(x+234*s) + ' ' + str(y+48*s) + ' L' + str(x+242*s) + ' ' + str(y+58*s) + ' L' + str(x+234*s) + ' ' + str(y+110*s) + ' Z" fill="' + OLIVE + '" ' + st + '/>'
        '<path d="M' + str(x) + ' ' + str(y+148*s) + ' L' + str(x+250*s) + ' ' + str(y+148*s) + '" ' + st + '/>'
    )
    _g(p, inner)

def illus_houses(p, x, y, s=1.0):
    """Row of simple houses with windows and doors — line art for the housing lead."""
    st = 'stroke="' + INK + '" stroke-width="' + str(3*s) + '" stroke-linecap="round" stroke-linejoin="round"'
    inner = (
        '<path d="M' + str(x) + ' ' + str(y+110*s) + ' L' + str(x) + ' ' + str(y+52*s) + ' L' + str(x+42*s) + ' ' + str(y+14*s) + ' L' + str(x+84*s) + ' ' + str(y+52*s) + ' L' + str(x+84*s) + ' ' + str(y+110*s) + '" ' + st + ' fill="' + BOX + '"/>'
        '<rect x="' + str(x+30*s) + '" y="' + str(y+76*s) + '" width="' + str(22*s) + '" height="' + str(34*s) + '" fill="' + GOOSE + '" ' + st + '/>'
        '<rect x="' + str(x+12*s) + '" y="' + str(y+62*s) + '" width="' + str(16*s) + '" height="' + str(16*s) + '" fill="' + BOX + '" ' + st + '/>'
        '<rect x="' + str(x+56*s) + '" y="' + str(y+62*s) + '" width="' + str(16*s) + '" height="' + str(16*s) + '" fill="' + BOX + '" ' + st + '/>'
        '<path d="M' + str(x+104*s) + ' ' + str(y+110*s) + ' L' + str(x+104*s) + ' ' + str(y+66*s) + ' L' + str(x+136*s) + ' ' + str(y+34*s) + ' L' + str(x+168*s) + ' ' + str(y+66*s) + ' L' + str(x+168*s) + ' ' + str(y+110*s) + '" ' + st + ' fill="' + BOX + '"/>'
        '<rect x="' + str(x+128*s) + '" y="' + str(y+82*s) + '" width="' + str(18*s) + '" height="' + str(28*s) + '" fill="' + GOOSE + '" ' + st + '/>'
        '<rect x="' + str(x+112*s) + '" y="' + str(y+70*s) + '" width="' + str(14*s) + '" height="' + str(14*s) + '" fill="' + BOX + '" ' + st + '/>'
        '<rect x="' + str(x+146*s) + '" y="' + str(y+70*s) + '" width="' + str(14*s) + '" height="' + str(14*s) + '" fill="' + BOX + '" ' + st + '/>'
        '<path d="M' + str(x+188*s) + ' ' + str(y+110*s) + ' L' + str(x+188*s) + ' ' + str(y+80*s) + ' L' + str(x+212*s) + ' ' + str(y+52*s) + ' L' + str(x+236*s) + ' ' + str(y+80*s) + ' L' + str(x+236*s) + ' ' + str(y+110*s) + '" ' + st + ' fill="' + BOX + '"/>'
        '<rect x="' + str(x+204*s) + '" y="' + str(y+88*s) + '" width="' + str(16*s) + '" height="' + str(22*s) + '" fill="' + GOOSE + '" ' + st + '/>'
        '<path d="M' + str(x) + ' ' + str(y+118*s) + ' L' + str(x+236*s) + ' ' + str(y+118*s) + '" ' + st + '/>'
    )
    _g(p, inner)
