# -*- coding: utf-8 -*-
"""SVG weekly-paper builder: PIL-measured text layout + line-art illustrations."""
from PIL import ImageFont
import os

FONTS_DIR = "/usr/share/fonts/opentype/noto"
NEWS_DIR = "/home/hatch/.local/share/fonts"
DEJAVU_DIR = "/usr/share/fonts/truetype/dejavu"
NOTO_DIR = "/usr/share/fonts/truetype/noto"

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
_IDX_SC = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}
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
# split: weight 100/200 resolve to Regular/SemiBold, which _FONT_FILE already uses.)
_SANS_NOTO_M = os.path.join(NOTO_DIR, "NotoSans-Medium.ttf")
_SANS_NOTO_MI = os.path.join(NOTO_DIR, "NotoSans-MediumItalic.ttf")
_cache = {}

import re as _re
_CJK = r'[\u3000-\u303f\u3400-\u9fff\uf900-\ufaff]'
def _fw(s):
    """Full-width punctuation where it touches a CJK character (Chinese
    typesetting); Latin/digit contexts (20:00, English glosses) untouched.
    Preserved verbatim from the old zh-cn engine."""
    if not _re.search(_CJK, s):
        return s
    s = _re.sub(r'(?<=' + _CJK + r'),', '，', s)
    s = _re.sub(r',(?=' + _CJK + r')', '，', s)
    s = _re.sub(r'(?<=' + _CJK + r');', '；', s)
    s = _re.sub(r';(?=' + _CJK + r')', '；', s)
    s = _re.sub(r'(?<=' + _CJK + r'):', '：', s)
    s = _re.sub(r':(?=' + _CJK + r')', '：', s)
    s = _re.sub(r'(?<=' + _CJK + r')\?', '？', s)
    s = _re.sub(r'(?<=' + _CJK + r')!', '！', s)
    # parentheses: convert the PAIR when the enclosed text contains any CJK
    def _pair(m):
        inner = m.group(1)
        if _re.search(_CJK, inner):
            return '（' + inner + '）'
        return m.group(0)
    s = _re.sub(r'\(([^()]*)\)', _pair, s)
    return s

# --- per-character font choice (SOP 1.1) -------------------------------------
# CairoSVG does NOT do per-glyph fallback for a font-family stack (verified:
# "Newsreader, Noto Serif CJK SC" renders CJK as tofu). So each character is
# assigned to the first font (in preference order) whose cmap contains it, and
# text is emitted as one <text> per maximal same-font run with PIL-measured x.
# serif: Newsreader (Latin) -> Noto Serif CJK SC -> DejaVu Sans (symbols)
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
# face="SC" is the default (Simplified-Chinese target text).
# NOTE: Newsreader's cmap lacks the pinyin caron vowels ǎ/ǒ/ǔ
# (U+01CE/U+01D2/U+01D4), so they fall through to the SC face upright;
# Noto Serif CJK SC contains them (verified by cmap check).
from fontTools.ttLib import TTFont as _TTFont
def _cmap(path, index=0):
    return _TTFont(path, fontNumber=index).getBestCmap()
_CMAP = {
    "news": _cmap(_NEWS), "news_b": _cmap(_NEWS_B), "news_i": _cmap(_NEWS_I),
    "serif_SC": _cmap(_SERIF, _IDX_SC[_SERIF]), "serif_b_SC": _cmap(_SERIF_B, _IDX_SC[_SERIF_B]),
    "sans_SC": _cmap(_SANS, _IDX_SC[_SANS]), "sans_b_SC": _cmap(_SANS_B, _IDX_SC[_SANS_B]),
    "sans_noto": _cmap(_SANS_NOTO), "sans_noto_b": _cmap(_SANS_NOTO_B),
    "sans_noto_i": _cmap(_SANS_NOTO_I),
    "deja": _cmap(_DEJA), "deja_b": _cmap(_DEJA_B),
}
_CYR = range(0x0400, 0x0530)  # Cyrillic + Cyrillic Supplement
_FAMILY = {"news": "Newsreader", "news_i": "Newsreader",
           "serif_SC": "Noto Serif CJK SC",
           "sans_SC": "Noto Sans CJK SC", "sans_noto": "Noto Sans",
           "sans_noto_i": "Noto Sans", "deja": "DejaVu Sans"}
_FONT_FILE = {
    ("serif", False, "news"): _NEWS, ("serif", True, "news"): _NEWS_B,
    ("serif", False, "news_i"): _NEWS_I, ("serif", True, "news_i"): _NEWS_I,
    ("serif", False, "serif_SC"): _SERIF, ("serif", True, "serif_SC"): _SERIF_B,
    ("serif", False, "deja"): _DEJA, ("serif", True, "deja"): _DEJA_B,
    ("sans", False, "sans_SC"): _SANS, ("sans", True, "sans_SC"): _SANS_B,
    ("sans", False, "sans_noto"): _SANS_NOTO_M, ("sans", True, "sans_noto"): _SANS_NOTO_B,
    ("sans", False, "sans_noto_i"): _SANS_NOTO_MI, ("sans", True, "sans_noto_i"): _SANS_NOTO_BI,
    ("sans", False, "deja"): _DEJA, ("sans", True, "deja"): _DEJA_B,
}
_FONT_IDX = {
    ("serif", False, "serif_SC"): _IDX_SC[_SERIF], ("serif", True, "serif_SC"): _IDX_SC[_SERIF_B],
    ("sans", False, "sans_SC"): _IDX_SC[_SANS], ("sans", True, "sans_SC"): _IDX_SC[_SANS_B],
}

# --- D5 reader routing (SOP 1.1, 2026-11-11) ------------------------------
# _D5_READER is rewritten by this installer (mechanism/apply_variant.py)
# to the edition's READER language: "latin" (de/en/es/fr/it/nl/pt),
# "ru" (ru), or "cjk" (ja/ko/zh-cn/zh-tw). latin/cjk share routing today
# (Latin never sits in a CJK face: SOP "不用思源宋体自带的拉丁字形排西文");
# ru routes Latin+Cyrillic to Noto Sans (Medium 500 / Bold 700 exact).
# The installer is the ONLY writer of this line; nothing else in the file
# branches on reader language.
_D5_READER = "latin"

def _char_font(ch, kind, bold, italic=False, face="SC"):
    cp = ord(ch)
    if kind == "serif":
        if italic and cp in _CMAP["news_i"]:
            return "news_i"
        if cp in _CMAP["news_b" if bold else "news"]:
            return "news"
        if cp in _CMAP[("serif_b_" if bold else "serif_") + face]:
            return "serif_" + face
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
    if cp in _CMAP[("sans_b_" if bold else "sans_") + face]:
        return "sans_" + face
    return "deja"

# fix2: _FONT_FILE entries for the Newsreader class inside sans runs, keyed by the
# derived class name (see _char_font). _pil resolves ("sans", bold, "news")
# to the Newsreader faces, mirroring the ("serif", bold, "news") rows.
_QUOTE_CLS = _char_font("\u201c", "serif", False)
_FONT_FILE[("sans", False, _QUOTE_CLS)] = _NEWS
_FONT_FILE[("sans", True, _QUOTE_CLS)] = _NEWS_B

def _pil(kind, bold, cls, size):
    key = (kind, bold, cls, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(_FONT_FILE[(kind, bold, cls)], size,
                                         index=_FONT_IDX.get((kind, bold, cls), 0))
    return _cache[key]

def _runs(s, kind, bold, italic=False, face="SC"):
    """Split s into maximal runs sharing one font. Returns [(text, cls)]."""
    runs, cur, curcls = [], "", None
    for ch in s:
        cls = _char_font(ch, kind, bold, italic, face)
        if cls == curcls:
            cur += ch
        else:
            if cur:
                runs.append((cur, curcls))
            cur, curcls = ch, cls
    if cur:
        runs.append((cur, curcls))
    return runs

def text_w(s, kind, bold, size, face="SC", italic=False):
    if not s:
        return 0.0
    return sum(_pil(kind, bold, cls, size).getlength(t) for t, cls in _runs(_fw(s), kind, bold, italic, face))

def _run_span(t, cls, kind, bold, size):
    """Advance one <text> run occupies: max(advance, ink right edge).
    Italic glyphs slant past their advance (Newsreader-Italic 'u'
    overhangs its advance), so the next run must start after the ink,
    not the advance -- else the following run's ink touches it. For
    upright runs ink <= advance, so the span is unchanged. (This does
    NOT clear the audit's italic flag: the audit measures italic runs
    with the Regular font, which is wider still -- see BUILD-REPORT.)"""
    if not t.strip():
        return _pil(kind, bold, cls, size).getlength(t)
    f = _pil(kind, bold, cls, size)
    return max(f.getlength(t), f.getbbox(t)[2])

def _breakable(ch):
    return ch == " "

def wrap(text, kind, bold, size, max_w, face="SC", italic=False):
    """Greedy wrap: Latin words kept whole where possible, CJK per char."""
    text = _fw(text)
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
    # Closing punctuation (kinsoku NO_START minus the small kana, which
    # are letters, not punctuation): a line must not START with one.
    # Used by the two guards below; the oidashi loop reuses the same set
    # via NO_START (which adds the kana).
    _CLOSING_PUNCT = "。、，．！？：；）」』】％ー…‥・)]}〉》.,!?%:;"
    # skip_next: set when the space-before-closing-punct guard below has
    # already consumed the next (punct) token into cur.
    skip_next = False
    for _ti, tok in enumerate(tokens):
        if skip_next:
            skip_next = False
            continue
        trial = cur + tok
        if text_w(trial, kind, bold, size, face, italic) <= max_w or not cur.strip():
            cur = trial
        elif len(tok) == 1 and tok in _CLOSING_PUNCT and text_w(cur, kind, bold, size, face, italic) <= max_w:
            # Closing punctuation belongs to the word before it: never
            # break before it. Keep it on the line even if it runs a few
            # px over max_w (well inside SEAM_SLACK 28); breaking here
            # leaves the next line starting with it, and oidashi then
            # pulls the last glyph of the previous line down -- splitting
            # a Latin word mid-word (W46 fr P6: "coli"/"s?" for "colis ?").
            cur = trial
        else:
            # Orphan-word slack (W45 it P2): never strand the final word
            # of a paragraph on its own line over a few px. If this token
            # is the last word and the line overruns max_w by at most 8px
            # (well inside the 22px card padding and SEAM_SLACK 28), keep
            # it on the line: the alternative is an extra line that can
            # collide with fixed-position furniture below (it: "calcoli",
            # 381.5px vs max_w 378.5).
            if tok.strip() and all(not t.strip() for t in tokens[_ti + 1:]):
                if text_w(trial, kind, bold, size, face, italic) <= max_w + 8:
                    cur = trial
                    continue
            # KO build: prefer a word-boundary (space) break when the fragment
            # after the last space is short; otherwise break by syllable.
            sp = cur.rfind(" ")
            if sp > 0 and tok != " ":
                tail = cur[sp + 1:]
                # ... but never break at a space whose tail is pure closing
                # punctuation: that strands the punctuation at the head of
                # the next line and oidashi splits the word before it.
                if tail and not all(ch in _CLOSING_PUNCT for ch in tail) and text_w(tail, kind, bold, size, face, italic) <= max_w * 0.45:
                    lines.append(cur[:sp].rstrip())
                    cur = tail + tok
                    continue
            # Space before closing punctuation (W43 fr P7: the space before
            # ':' did not fit, so the break dropped it and ':' started the
            # next line; oidashi then pulled the 's' off 'phrases' to join
            # it -- 'phrase'/'s:'). The punctuation belongs to the word
            # just completed: keep the space + punct on this line when the
            # overrun stays inside SEAM_SLACK (28px, the same allowance
            # the closing-punct guard above already relies on). The punct
            # token is consumed here and skipped on the next iteration.
            if (tok == " " and _ti + 1 < len(tokens)
                    and len(tokens[_ti + 1]) == 1
                    and tokens[_ti + 1] in _CLOSING_PUNCT
                    and text_w(cur + " " + tokens[_ti + 1], kind, bold, size, face, italic) <= max_w + 28):
                cur = cur + " " + tokens[_ti + 1]
                skip_next = True
                continue
            lines.append(cur.rstrip())
            cur = tok.lstrip() if tok == " " else tok
    if cur.strip():
        lines.append(cur.rstrip())
    # kinsoku shori (ZH-CN build): a line must not START with closing punctuation --
    # pull the previous line's last character down (oidashi). Line count unchanged.
    # A line must not END with opening punctuation either -- push it to the next line.
    # Small kana added (zh-cn-ja W46: sutegana must not start a line).
    NO_START = "。、，．！？：；）」』】％ー…‥・)]}〉》.,!?%:;ぁぃぅぇぉゃゅょゎっァィゥェォャュョヮッ"
    NO_END = "（「『〔【《〈([{"
    # pre_w MUST be measured BEFORE kinsoku (ja precedent): the seam
    # repair below tells an oidashi-grown line (pre_w <= max_w +
    # SEAM_SLACK) from an unbreakable token that was already over-wide.
    # Measured after kinsoku, an oidashi-grown line looks "already
    # over-wide" and is skipped, leaving it seam-crossing into the next
    # column (W46 core P7: '」 (Has my parcel arrived?) When you wait'
    # at 463.9px vs max_w 422.5, overprinting the B1 column's '11').
    # Word chars for the no-split guard below: Latin letters incl.
    # diacritics (pinyin carons U+01CE/U+01D0/U+01D2/U+01D4, acute/grave/umlaut vowels),
    # digits, and ":" / "." inside times and decimals ("19:30", "3.5").
    # (Same _WORD as the W45 engine, which introduced this guard.)
    _WORD = r"[A-Za-z0-9\u00c0-\u00ff\u0100-\u024f\u1e00-\u1eff:.,]+"
    pre_w = [text_w(ln, kind, bold, size, face, italic) for ln in lines]
    for i in range(1, len(lines)):
        guard = 0
        while lines[i] and lines[i][0] in NO_START and len(lines[i - 1]) > 1 and guard < 8:
            # Never split a Latin/digit word by pulling one char of it:
            # if the previous line ends in a word, pull the WHOLE word
            # down (W43 fr P7: one-char pulls cut "phrases" to "phrase"/"s:"
            # for a stranded ':'; W45 ja P2 precedent: "zhìjiàng" cut to
            # "zhìjiàn"/"g"). If the previous line IS a single word, leave
            # the line starting with the closing punctuation rather than
            # splitting the word.
            _wm = _re.search(_WORD + r"$", lines[i - 1])
            if _wm and _wm.start() > 0:
                _mv = lines[i - 1][_wm.start():]
                lines[i] = _mv + lines[i]
                lines[i - 1] = lines[i - 1][:_wm.start()].rstrip()
            elif _wm:
                break
            else:
                lines[i] = lines[i - 1][-1] + lines[i]
                lines[i - 1] = lines[i - 1][:-1].rstrip()
            guard += 1
    for i in range(len(lines) - 1):
        guard = 0
        while lines[i] and lines[i][-1] in NO_END and len(lines[i]) > 1 and guard < 8:
            lines[i + 1] = lines[i][-1] + lines[i + 1]
            lines[i] = lines[i][:-1].rstrip()
            guard += 1
    # Seam repair (2026-10-21 core patch -- JA P7 glyph overprint): oidashi
    # never re-measures the receiving line, and a line starting with a
    # NO_START chain (e.g. 』!。) pulls one glyph per pass, so the receiving
    # line can end far past max_w. A wrapped line may legitimately sit in
    # the gutter (SEAM_SLACK: the 4-column grid's pitch minus column width),
    # but once its ink crosses the pitch it overprints the neighbouring
    # column's first glyph. Repair ONLY such seam-crossing lines that
    # oidashi itself grew (pre_w <= max_w + SEAM_SLACK): shed trailing
    # glyphs to the head of the next line until the line fits max_w again,
    # cascading forward. A NO_START glyph is shed together with the glyph
    # before it, so the next line never starts with one.
    SEAM_SLACK = 28
    cascade = False
    for i in range(len(lines)):
        if text_w(lines[i], kind, bold, size, face, italic) <= max_w + SEAM_SLACK:
            cascade = False
            continue
        if not cascade and pre_w[i] > max_w + SEAM_SLACK:
            continue  # unbreakable token, already seam-crossing pre-kinsoku
        cascade = True
        while text_w(lines[i], kind, bold, size, face, italic) > max_w and len(lines[i]) > 1:
            # Never split a trailing Latin word: shed it whole. The
            # oidashi-grown tail is often Latin ("...When you wait"), and
            # single-glyph shedding would cut "you" to "yo"/"u" across
            # the break. A shed lone space is dropped, not carried over.
            m = _re.search(r"[A-Za-z]+$", lines[i])
            if m and m.start() > 0:
                move, lines[i] = lines[i][m.start():], lines[i][:m.start()]
            elif lines[i][-1] in NO_START and len(lines[i]) > 2:
                move, lines[i] = lines[i][-2:], lines[i][:-2]
            else:
                move, lines[i] = lines[i][-1], lines[i][:-1]
            if move.strip():
                if i + 1 < len(lines):
                    lines[i + 1] = move + lines[i + 1]
                else:
                    lines.append(move)
        lines[i] = lines[i].rstrip()
    return lines

# --- three-colour moth (brand mark) on the masthead rule ----------------------
# Inner XML of assets/lucerna-moth.svg (design sample), inlined so the build
# does not depend on the design worktree. viewBox 64 120 384 284 (384x284).
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

    def text(self, x, y, s, size=28, kind="serif", bold=False, fill=INK, anchor="start", spacing=None, family=None, face="SC", italic=False):
        # Explicit single family (e.g. the UnifrakturMaguntia masthead): one
        # element; CairoSVG anchors single-font text correctly.
        # (italic is ignored here: no italic face exists for a fixed family.)
        if family is not None:
            s = _fw(s)
            sp = f' letter-spacing="{spacing}"' if spacing else ""
            wt = ' font-weight="700"' if bold else ""
            self.add(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}"{wt} fill="{fill}" text-anchor="{anchor}"{sp}>{esc(s)}</text>')
            return y
        if not s:
            return y
        s = _fw(s)
        # Mixed text: one <text> per same-font run, x positions measured with
        # PIL (CairoSVG mis-measures text-anchor on multi-font <tspan> runs).
        runs = _runs(s, kind, bold, italic, face)
        sp = spacing or 0
        total = sum(_run_span(t, cls, kind, bold, size) for t, cls in runs) + sp * (len(s) - 1)
        if anchor == "middle":
            cur = x - total / 2.0
        elif anchor == "end":
            cur = x - total
        else:
            cur = x
        wt = ' font-weight="700"' if bold else ""
        spattr = f' letter-spacing="{spacing}"' if spacing else ""
        for i, (t, cls) in enumerate(runs):
            w = _run_span(t, cls, kind, bold, size)
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
            # (Variant 056a957d5366 per D1-FIX-PATCH.md §2b: this file uses
            # _run_span, not _pil(...).getlength, for run widths.)
            lead = len(t) - len(t.lstrip(" "))
            if lead:
                _lw = _run_span(t[:lead], cls, kind, bold, size)
                self.add(f'<text x="{cur:.1f}" y="{y}" font-family="{_FAMILY[cls]}" font-size="{size}"{wt}{it} fill="{fill}" text-anchor="start"{spattr}>{esc(t[:lead])}</text>')
                cur += _lw + sp * lead
                t = t[lead:]
                w = _run_span(t, cls, kind, bold, size) if t else 0.0
            if t:
                self.add(f'<text x="{cur:.1f}" y="{y}" font-family="{_FAMILY[cls]}" font-size="{size}"{wt}{it} fill="{fill}" text-anchor="start"{spattr}>{esc(t)}</text>')
            # next run starts after this run's rendered span (incl. its
            # trailing letter-spacing) plus one boundary spacing unit.
            cur += w + (sp * len(t) if i < len(runs) - 1 else 0)
        return y

    def para(self, x, y, s, size=28, kind="serif", bold=False, fill=INK, max_w=900, lh=1.5, anchor="start", face="SC", italic=False):
        for ln in wrap(s, kind, bold, size, max_w, face, italic):
            self.text(x, y, ln, size, kind, bold, fill, anchor, face=face, italic=italic)
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
