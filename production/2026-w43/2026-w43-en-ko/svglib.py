# -*- coding: utf-8 -*-
"""SVG weekly-paper builder: PIL-measured text layout + line-art illustrations."""
from PIL import ImageFont
import os

FONTS_DIR = "/usr/share/fonts/opentype/noto"
NEWS_DIR = "/home/hatch/.local/share/fonts"
DEJAVU_DIR = "/usr/share/fonts/truetype/dejavu"
NOTO_DIR = "/usr/share/fonts/truetype/noto"

def _kr_index(path):
    for i in range(12):
        try:
            f = ImageFont.truetype(path, 40, index=i)
            if f.getname()[0].endswith("KR"):
                return i
        except Exception:
            break
    return 0

_SERIF = os.path.join(FONTS_DIR, "NotoSerifCJK-Regular.ttc")
_SERIF_B = os.path.join(FONTS_DIR, "NotoSerifCJK-Bold.ttc")
_SANS = os.path.join(FONTS_DIR, "NotoSansCJK-Regular.ttc")
_SANS_B = os.path.join(FONTS_DIR, "NotoSansCJK-Bold.ttc")
_IDX = {p: _kr_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}
_NEWS = os.path.join(NEWS_DIR, "Newsreader-Regular.ttf")
_NEWS_B = os.path.join(NEWS_DIR, "Newsreader-SemiBold.ttf")
_NEWS_I = os.path.join(NEWS_DIR, "Newsreader-Italic.ttf")
_DEJA = os.path.join(DEJAVU_DIR, "DejaVuSans.ttf")
_DEJA_B = os.path.join(DEJAVU_DIR, "DejaVuSans-Bold.ttf")
_SANS_NOTO = os.path.join(NOTO_DIR, "NotoSans-Regular.ttf")
_SANS_NOTO_B = os.path.join(NOTO_DIR, "NotoSans-Bold.ttf")
_SANS_NOTO_I = os.path.join(NOTO_DIR, "NotoSans-Italic.ttf")
_SANS_NOTO_BI = os.path.join(NOTO_DIR, "NotoSans-BoldItalic.ttf")
# D5 measurement (core-ru W47 spacing fix, 2026-11-11): MEASUREMENT must use
# the face the renderer uses. CairoSVG requests weight=100 for normal text
# and fontconfig resolves "Noto Sans" at that weight to the MEDIUM faces
# (fc-match :weight=100 -> NotoSans-Medium.ttf; italic -> MediumItalic;
# bold -> Bold/BoldItalic). PIL measuring Regular/Italic under-measures
# Cyrillic advances by ~2-3%, which collapses the following inter-word
# space in the PDF. (Same rule as core-ru; Newsreader faces need no such
# split: weight 100/200 resolve to Regular/SemiBold, which _PATH already uses.)
_SANS_NOTO_M = os.path.join(NOTO_DIR, "NotoSans-Medium.ttf")
_SANS_NOTO_MI = os.path.join(NOTO_DIR, "NotoSans-MediumItalic.ttf")
_cache = {}

# --- per-character font choice (SOP 1.1) -------------------------------------
# CairoSVG does NOT do per-glyph fallback for a font-family stack (verified:
# "Newsreader, Noto Serif CJK TC" renders CJK as tofu). So each character is
# assigned to the first font (in preference order) whose cmap contains it, and
# text is emitted as one <text> per maximal same-font run with PIL-measured x.
# serif: Newsreader (Latin) -> Noto Serif CJK SC -> DejaVu Sans (symbols only)
# sans:  D5 (SOP 1.1): fix2 quotes -> serif branch (Newsreader); then by
#        _D5_READER: latin/cjk readers — Latin/digits/punct in the Newsreader
#        cmap -> news (400/600 as the SOP 500/700), Cyrillic -> sans_noto
#        (Noto Sans Medium 500 / Bold 700); ru readers — Latin+Cyrillic ->
#        sans_noto; everything else -> Noto Sans CJK <variant> -> DejaVu Sans.
#        Bold uses the 600/700 variants; italic Cyrillic -> sans_noto_i
#        (both modes, core-ru parity).
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
    "sans_noto": _cmap(_SANS_NOTO), "sans_noto_b": _cmap(_SANS_NOTO_B),
    "sans_noto_i": _cmap(_SANS_NOTO_I),
    "deja": _cmap(_DEJA), "deja_b": _cmap(_DEJA_B),
}
_CYR = range(0x0400, 0x0530)  # Cyrillic + Cyrillic Supplement
_FAMILY = {"news": "Newsreader", "news_i": "Newsreader",
           "serif": "Noto Serif CJK KR",
           "sans": "Noto Sans CJK KR", "sans_noto": "Noto Sans",
           "sans_noto_i": "Noto Sans", "deja": "DejaVu Sans"}
_PATH = {
    ("serif", False, "news"): _NEWS, ("serif", True, "news"): _NEWS_B,
    ("serif", False, "news_i"): _NEWS_I, ("serif", True, "news_i"): _NEWS_I,
    ("serif", False, "serif"): _SERIF, ("serif", True, "serif"): _SERIF_B,
    ("serif", False, "deja"): _DEJA, ("serif", True, "deja"): _DEJA_B,
    ("sans", False, "sans"): _SANS, ("sans", True, "sans"): _SANS_B,
    ("sans", False, "sans_noto"): _SANS_NOTO_M, ("sans", True, "sans_noto"): _SANS_NOTO_B,
    ("sans", False, "sans_noto_i"): _SANS_NOTO_MI, ("sans", True, "sans_noto_i"): _SANS_NOTO_BI,
    ("sans", False, "deja"): _DEJA, ("sans", True, "deja"): _DEJA_B,
}
_IDX2 = {("serif", False, "serif"): _IDX[_SERIF], ("serif", True, "serif"): _IDX[_SERIF_B],
         ("sans", False, "sans"): _IDX[_SANS], ("sans", True, "sans"): _IDX[_SANS_B]}

# --- D5 reader routing (SOP 1.1, 2026-11-11) ------------------------------
# _D5_READER is rewritten by this installer (mechanism/apply_variant.py)
# to the edition's READER language: "latin" (de/en/es/fr/it/nl/pt),
# "ru" (ru), or "cjk" (ja/ko/zh-cn/zh-tw). latin/cjk share routing today
# (Latin never sits in a CJK face: SOP "不用思源宋体自带的拉丁字形排西文");
# ru routes Latin+Cyrillic to Noto Sans (Medium 500 / Bold 700 exact).
# The installer is the ONLY writer of this line; nothing else in the file
# branches on reader language.
_D5_READER = "cjk"

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
    # fix2 (2026-11-11, proof2 D1/D2 in core-de; ported 2026-11-12 to this
    # edition, extended to three codepoints): U+201C/U+201D/U+2019 are
    # full-width (advance 1000/1000em) in Noto Sans CJK SC/TC — their ink
    # sits at the right edge of the cell, so a sans quote leaves a wide
    # white gap before it. Newsreader's quotes are the narrow glyphs the
    # other pairs already use (~0.44em). Route these three codepoints
    # through the serif branch, which assigns them their Newsreader class:
    # the characters stay the same everywhere (source, text.md, PDF text
    # layers) and only the rendered glyph changes. Blast radius, verified
    # by SVG census on the shipped build: exactly 2 glyphs in this edition
    # (both P8, D2 key note); no other sans string holds
    # any of the three codepoints.
    # No new string literal is written here on purpose: freeze_direct.py
    # accounts source literals against tr_<lang>.py, and the class name
    # 'news' occurs in no tr literal — a literal 'news' would fail its
    # source level. The class is therefore derived, not spelled.
    if ch in ("\u201c", "\u201d", "\u2019"):
        # italic=False on purpose: the serif branch with italic would pick
        # the "news_i" class, which has no ("sans", ...) _PATH row.
        return _char_font(ch, "serif", bold)
    # D5 (2026-11-11, SOP 1.1; base: pt-fr pilot patch): the sans layer is
    # the explanation layer. Pilot rules, verbatim in the else-branch:
    # Latin/digits/punct in the Newsreader cmap -> "news"; Cyrillic in
    # _CYR and the Noto Sans cmap -> "sans_noto"; everything else keeps
    # the existing CJK path. Order matters: fix2 quotes above stay first;
    # cmap membership (not hand-kept codepoint lists) decides each rule,
    # so uncovered characters fall through to CJK/deja. Two deliberate
    # extensions over the pilot patch (see template banner + MECHANISM.md):
    # (1) _D5_READER == "ru" routes Latin AND Cyrillic to Noto Sans;
    # (2) italic Cyrillic -> "sans_noto_i" in BOTH modes (core-ru parity;
    # the pilot had no italic Cyrillic; the weekly word is serif-italic,
    # so sans-italic is rare, but ru-core already ships this rule and the
    # uniform patch must not regress it for ru-target editions).
    # Class-name literals are spelled here, as core-ru already does in its
    # shipped _char_font ("sans_noto"/"news"); tools/freeze.py (the actual
    # gate) has no source-literal accounting, and no freeze_direct.py
    # exists in the repo (searched 2026-11-11) — the fix2 comment's
    # caution is preserved verbatim for the _QUOTE_CLS derivation below.
    if italic and cp in _CYR and cp in _CMAP["sans_noto_i"]:
        return "sans_noto_i"
    if _D5_READER == "ru":
        if cp in _CMAP["sans_noto_b" if bold else "sans_noto"]:
            return "sans_noto"
    else:
        if cp in _CMAP["news_b" if bold else "news"]:
            return "news"
        if cp in _CYR and cp in _CMAP["sans_noto_b" if bold else "sans_noto"]:
            return "sans_noto"
    if cp in _CMAP["sans_b" if bold else "sans"]:
        return "sans"
    return "deja"

# fix2: _PATH entries for the Newsreader class inside sans runs, keyed by the
# derived class name (see _char_font). _pil resolves ("sans", bold, "news")
# to the Newsreader faces, mirroring the ("serif", bold, "news") rows.
_QUOTE_CLS = _char_font("\u201c", "serif", False)
_PATH[("sans", False, _QUOTE_CLS)] = _NEWS
_PATH[("sans", True, _QUOTE_CLS)] = _NEWS_B

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
    # kinsoku shori — W43 fix (2026-11-10): a wrapped line must not END
    # with an opening bracket or START with closing punctuation.
    # START (oidashi — the JA build's proven pass): pull the previous
    # line's last character down, so the closer is no longer line-initial.
    # END: break before the opener — move a trailing opener down to the
    # next line's head. Seam repair (JA build's proven pass, NO_END-aware):
    # a line that then exceeds max_w sheds tail glyphs forward (a NO_START
    # closer travels with its predecessor; a trailing opener left behind
    # travels with the shed piece), cascading forward; lines within the
    # 28 px gutter slack are left alone. (The W46 word-integrity repair
    # follows this block and rejoins any Latin word these moves split.)
    NO_START = "。、，．！？：；）」』】ー…‥・)]｝〉》％"
    NO_END = "（〔［｛〈《「『【"
    _SEAM_SLACK = 28.0
    _pre_w = [text_w(ln, kind, bold, size, italic) for ln in lines]
    for _ki in range(1, len(lines)):
        while lines[_ki] and lines[_ki][0] in NO_START and len(lines[_ki - 1]) > 1:
            lines[_ki] = lines[_ki - 1][-1] + lines[_ki]
            lines[_ki - 1] = lines[_ki - 1][:-1].rstrip()
    for _ki in range(len(lines) - 1):
        while lines[_ki] and lines[_ki][-1] in NO_END and len(lines[_ki]) > 1:
            _kch = lines[_ki][-1]
            lines[_ki] = lines[_ki][:-1].rstrip()
            lines[_ki + 1] = _kch + lines[_ki + 1]
    _cascade = False
    for _ki in range(len(lines)):
        if text_w(lines[_ki], kind, bold, size, italic) <= max_w + _SEAM_SLACK:
            _cascade = False
            continue
        if not _cascade and _pre_w[_ki] > max_w + _SEAM_SLACK:
            continue  # unbreakable token, already seam-crossing pre-kinsoku
        _cascade = True
        while text_w(lines[_ki], kind, bold, size, italic) > max_w and len(lines[_ki]) > 1:
            if lines[_ki][-1] in NO_START and len(lines[_ki]) > 2:
                _move, lines[_ki] = lines[_ki][-2:], lines[_ki][:-2]
            else:
                _move, lines[_ki] = lines[_ki][-1], lines[_ki][:-1]
            while lines[_ki] and lines[_ki][-1] in NO_END and len(lines[_ki]) > 1:
                _c = lines[_ki][-1]
                lines[_ki] = lines[_ki][:-1]
                _move = _c + _move
            if _ki + 1 < len(lines):
                lines[_ki + 1] = _move + lines[_ki + 1]
            else:
                lines.append(_move)
        lines[_ki] = lines[_ki].rstrip()
    # Word-integrity repair (W46 EN fix, 2026-11-09; adapted from the DE
    # W46 fix of 2026-11-08): the kinsoku passes above move single glyphs
    # and can split a Latin word across two lines with no hyphen (en-ja P8
    # key 139 note "Sunday": oidashi pulled the final "y" down because the
    # next line started with "；", which is NO_START). Rejoin any such
    # split by moving the whole word to the next line; cascade sheds whole
    # words forward so no line exceeds max_w. CJK per-character breaks are
    # unaffected (Latin letters only). Detection is positional, not
    # heuristic: the space-stripped lines must reproduce the input text,
    # and the two letters either side of a line boundary must have been
    # adjacent in the input (no space). NO_END is defined here because
    # this wrap has no kinsoku END pass (only the START/oidashi pass).
    NO_END = "（(［｛〈《「『"
    def _is_latin(_ch):
        return ("a" <= _ch <= "z") or ("A" <= _ch <= "Z")
    _stripped = []
    _adjacent = []  # _adjacent[j]: _stripped[j] and _stripped[j+1] adjacent in text
    _after_space = True
    for _ch in text:
        if _ch == " ":
            _after_space = True
            continue
        if _stripped:
            _adjacent.append(not _after_space)
        _stripped.append(_ch)
        _after_space = False
    if "".join(_ln.replace(" ", "") for _ln in lines) == "".join(_stripped):
        _i = 0
        while _i < len(lines) - 1:
            _pos = sum(len(_ln.replace(" ", "")) for _ln in lines[:_i + 1])
            if (0 < _pos < len(_stripped) and _is_latin(_stripped[_pos - 1])
                    and _is_latin(_stripped[_pos]) and _adjacent[_pos - 1]):
                _s = _pos - 1
                while _s > 0 and _is_latin(_stripped[_s - 1]) and _adjacent[_s - 1]:
                    _s -= 1
                _e = _pos
                while _e + 1 < len(_stripped) and _is_latin(_stripped[_e + 1]) and _adjacent[_e]:
                    _e += 1
                _word = "".join(_stripped[_s:_e + 1])
                _a, _b = lines[_i], lines[_i + 1]
                _frag_m = _re.search(r"[A-Za-z]+$", _a)
                _head_m = _re.match(r"[A-Za-z]+", _b)
                if _frag_m and _head_m and _word.startswith(_frag_m.group(0)):
                    _frag = _frag_m.group(0)
                    _k = len(_word) - len(_frag)
                    if 0 < _k <= len(_head_m.group(0)):
                        _rest = _b[_k:]
                        _space = ""
                        if _e + 1 < len(_stripped) and not _adjacent[_e]:
                            _space = " "
                        _new_a = _a[:-len(_frag)].rstrip()
                        _new_b = _frag + _b[:_k] + _space + _rest
                        while _new_a and _new_a[-1] in NO_END:
                            _ch = _new_a[-1]
                            _new_a = _new_a[:-1].rstrip()
                            _new_b = _ch + _new_b
                        if _new_a:
                            lines[_i] = _new_a
                            lines[_i + 1] = _new_b
                            _j = _i + 1
                            _guard = 0
                            while _j < len(lines) and _guard < 10000:
                                _guard += 1
                                if text_w(lines[_j], kind, bold, size, italic) <= max_w:
                                    _j += 1
                                    continue
                                _ln = lines[_j]
                                _sp = _ln.rfind(" ")
                                if _sp <= 0:
                                    break
                                _piece = _ln[_sp + 1:]
                                _rest2 = _ln[:_sp].rstrip()
                                while _rest2 and _rest2[-1] in NO_END:
                                    _ch = _rest2[-1]
                                    _rest2 = _rest2[:-1].rstrip()
                                    _piece = _ch + _piece
                                if not _rest2:
                                    break
                                lines[_j] = _rest2
                                if _j + 1 < len(lines):
                                    _nx = lines[_j + 1]
                                    # Positional join: the input had a space
                                    # between the piece and the next line's
                                    # head iff the two stripped chars either
                                    # side of the boundary were not adjacent
                                    # in the input (see _adjacent). A
                                    # character-class guess cannot tell
                                    # "灯笼 a" (space) from "gesungen.（"
                                    # (no space); the position can.
                                    _hpos = sum(len(_ln.replace(" ", "")) for _ln in lines[:_j + 1]) + len(_piece)
                                    _sp2 = " " if (0 < _hpos < len(_stripped) and not _adjacent[_hpos - 1]) else ""
                                    lines[_j + 1] = _piece + _sp2 + _nx
                                else:
                                    lines.append(_piece)
                _i += 1
            else:
                _i += 1
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
            it = ' font-style="italic"' if cls in ("news_i", "sans_noto_i") else ""
            # D1 fix (2026-11-09): CairoSVG strips the LEADING whitespace
            # of a <text> element, so a run beginning with a space prints
            # glued to the previous run ("наDouble", "→___"). A space
            # lands at a run head because _char_font classes " " as Latin
            # (Newsreader), while the glyph before it is CJK/symbol class
            # — the run boundary falls BEFORE the space, not after it.
            # Emit the leading space(s) as their own <text> (a space
            # renders no ink; the following run's x already encodes the
            # advance) and start the visible run after it. The cur advance
            # keeps the letter-spacing units the spaces carried (one sp
            # after each space), so total geometry is unchanged for any
            # spacing value. U+3000 is NOT stripped by CairoSVG (probe:
            # "　包裹" ink starts exactly at x + 28.0), so only ASCII
            # space is moved. A run that is only spaces is emitted as
            # the space element alone; its advance still reaches the
            # next run through cur.
            lead = len(t) - len(t.lstrip(" "))
            if lead:
                _lw = _pil(kind, bold, cls, size).getlength(t[:lead])
                self.add(f'<text x="{cur:.1f}" y="{y}" font-family="{_FAMILY[cls]}" font-size="{size}"{wt}{it} fill="{fill}" text-anchor="start"{spattr}>{esc(t[:lead])}</text>')
                cur += _lw + sp * lead
                t = t[lead:]
                w = _pil(kind, bold, cls, size).getlength(t) if t else 0.0
            if t:
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
    """Mountains, sun, two stick climbers, chrysanthemums — for 重阳."""
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
