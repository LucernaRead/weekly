# -*- coding: utf-8 -*-
"""SVG weekly builder: PIL-measured text layout + line-art illustrations."""
from PIL import ImageFont
import os

FONTS_DIR = "/usr/share/fonts/opentype/noto"

def _tc_index(path):
    for i in range(12):
        try:
            f = ImageFont.truetype(path, 40, index=i)
            if f.getname()[0].endswith("TC"):
                return i
        except Exception:
            break
    return 0

_SERIF = os.path.join(FONTS_DIR, "NotoSerifCJK-Regular.ttc")
_SERIF_B = os.path.join(FONTS_DIR, "NotoSerifCJK-Bold.ttc")
_SANS = os.path.join(FONTS_DIR, "NotoSansCJK-Regular.ttc")
_SANS_B = os.path.join(FONTS_DIR, "NotoSansCJK-Bold.ttc")
_IDX = {p: _tc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}
_cache = {}

def _font(kind, bold, size):
    path = {"serif": _SERIF_B if bold else _SERIF,
            "sans": _SANS_B if bold else _SANS}[kind]
    key = (path, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, size, index=_IDX[path])
    return _cache[key]

def text_w(s, kind, bold, size):
    if not s:
        return 0.0
    return _font(kind, bold, size).getlength(s)

def _breakable(ch):
    return ch == " "

def wrap(text, kind, bold, size, max_w):
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
        if text_w(trial, kind, bold, size) <= max_w or not cur.strip():
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
BOX = "#fdfaf0"; LINE = "#d8cfb4"; GREY = "#57523f"; BRICK = "#a4553a"; DARK = "#2c2822"

class Page:
    def __init__(self, w=1080, h=1440):
        self.w, self.h = w, h
        self.parts = []
        self.add(f'<rect width="{w}" height="{h}" fill="{PAPER}"/>')
        self.add(f'<rect x="26" y="26" width="{w-52}" height="{h-52}" fill="none" stroke="{INK}" stroke-width="3"/>')
        self.add(f'<rect x="37" y="37" width="{w-74}" height="{h-74}" fill="none" stroke="{INK}" stroke-width="1.2"/>')

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, size=28, kind="serif", bold=False, fill=INK, anchor="start", spacing=None, family=None):
        fam = family or ("Noto Serif CJK TC" if kind == "serif" else "Noto Sans CJK TC")
        sp = f' letter-spacing="{spacing}"' if spacing else ""
        wt = ' font-weight="700"' if bold else ""
        self.add(f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}"{wt} fill="{fill}" text-anchor="{anchor}"{sp}>{esc(s)}</text>')
        return y

    def para(self, x, y, s, size=28, kind="serif", bold=False, fill=INK, max_w=900, lh=1.5, anchor="start"):
        for ln in wrap(s, kind, bold, size, max_w):
            self.text(x, y, ln, size, kind, bold, fill, anchor)
            y += size * lh
        return y

    def hline(self, x1, x2, y, color=LINE, wdt=1.2):
        self.add(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{color}" stroke-width="{wdt}"/>')

    def rect(self, x, y, w, h, fill="none", stroke=None, sw=1.2, rx=0):
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st}/>')

    def section_head(self, x, y, s, size=31, color=OLIVE, rule_to=1016):
        self.text(x, y, s, size, "sans", True, color)
        self.hline(x, rule_to, y + 14, GOLD, 2)
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
    """Mountains, sun, two stick climbers, chrysanthemums — for 重阳."""
    st = f'stroke="{INK}" stroke-width="{3.2*s}" stroke-linecap="round" stroke-linejoin="round"'
    _g(p, f'''
    <circle cx="{x+150*s}" cy="{y+26*s}" r="{17*s}" fill="{GOLD}" {st}/>
    <path d="M{x} {y+120*s} L{x+70*s} {y+52*s} L{x+118*s} {y+96*s} L{x+168*s} {y+40*s} L{x+238*s} {y+120*s}" {st}/>
    <path d="M{x+30*s} {y+120*s} L{x+92*s} {y+74*s} L{x+128*s} {y+120*s}" {st}/>
    <circle cx="{x+98*s}" cy="{y+66*s}" r="{6.5*s}" fill="{INK}"/>
    <path d="M{x+98*s} {y+73*s} L{x+96*s} {y+90*s} L{x+86*s} {y+104*s} M{x+96*s} {y+90*s} L{x+108*s} {y+100*s} M{x+97*s} {y+78*s} L{x+110*s} {y+70*s}" {st}/>
    <circle cx="{x+128*s}" cy="{y+84*s}" r="{6*s}" fill="{INK}"/>
    <path d="M{x+128*s} {y+90*s} L{x+130*s} {y+104*s} L{x+121*s} {y+114*s} M{x+130*s} {y+104*s} L{x+140*s} {y+110*s}" {st}/>
    <g fill="{BRICK}">
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
      fill="{BRICK}" stroke="{INK}" stroke-width="{2.4*s}"/>''')

def illus_fox(p, x, y, s=1.0):
    st = f'stroke="{INK}" stroke-width="{3*s}" stroke-linejoin="round"'
    _g(p, f'''
    <path d="M{x+8*s} {y+6*s} L{x+34*s} {y+30*s} L{x+62*s} {y+6*s} L{x+66*s} {y+44*s} L{x+35*s} {y+78*s} L{x+4*s} {y+44*s} Z" {st} fill="{BOX}"/>
    <path d="M{x+8*s} {y+6*s} L{x+22*s} {y+26*s} M{x+62*s} {y+6*s} L{x+48*s} {y+26*s}" {st}/>
    <circle cx="{x+24*s}" cy="{y+42*s}" r="{3.2*s}" fill="{INK}"/>
    <circle cx="{x+46*s}" cy="{y+42*s}" r="{3.2*s}" fill="{INK}"/>
    <path d="M{x+30*s} {y+56*s} L{x+40*s} {y+56*s} L{x+35*s} {y+63*s} Z" fill="{BRICK}"/>''')

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
    <circle cx="{x+116*s}" cy="{y+18*s}" r="{12*s}" fill="{GOLD}" {st}/>
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
    <path d="M{x+52*s} {y+6*s} A30 30 0 1 0 {x+52*s} {y+58*s} A24 24 0 1 1 {x+52*s} {y+6*s} Z" fill="{GOLD}" {st}/>
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
    <circle cx="{x+84*s}" cy="{y+16*s}" r="{9*s}" fill="{GOLD}" {st}/>''')

def illus_book(p, x, y, s=1.0):
    st = f'stroke="{INK}" stroke-width="{3*s}" stroke-linejoin="round"'
    _g(p, f'''
    <path d="M{x+35*s} {y+14*s} Q{x+18*s} {y+4*s}, {x+4*s} {y+10*s} L{x+4*s} {y+56*s} Q{x+18*s} {y+50*s}, {x+35*s} {y+60*s} Q{x+52*s} {y+50*s}, {x+66*s} {y+56*s} L{x+66*s} {y+10*s} Q{x+52*s} {y+4*s}, {x+35*s} {y+14*s} Z" {st} fill="{BOX}"/>
    <line x1="{x+35*s}" y1="{y+14*s}" x2="{x+35*s}" y2="{y+60*s}" {st}/>
    <path d="M{x+35*s} {y+30*s} Q{x+44*s} {y+18*s}, {x+54*s} {y+24*s} Q{x+46*s} {y+34*s}, {x+35*s} {y+30*s}" fill="{OLIVE}"/>''')
