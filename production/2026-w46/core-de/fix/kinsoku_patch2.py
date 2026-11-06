# -*- coding: utf-8 -*-
"""Kinsoku patch v2 (W46 DE Round 1 fix follow-up).

Round 1 follow-up findings (verified on rebuilt SVGs + wrap simulation):
 1. The END-pass shedding loop shed a single "." off "76.", splitting the
    token into a line ending "· 76" and a line starting ".Die Kinder"
    (core/zh-cn P8 keys paragraph). Shedding must move a whole trailing
    Latin token when the last glyph is ASCII punctuation, and restore the
    space the raw wrap consumed at that break.
 2. The seam repair runs AFTER the END pass and sheds trailing glyphs
    until the line fits — it can stop exactly on an opening bracket
    (JA P1 Fragen line ending "（"). A final START-then-END polish sweep
    after seam closes both violation types.
 3. ASCII closing punctuation (.,:;!?) was missing from the CJK NO_START
    sets (KO already had it), so a stranded ASCII period survived the
    START repair. Added to core/zh-cn/zh-tw/JA sets.

Applies to the 5 CJK build svglib.py copies only. Latin/Cyrillic builds
untouched. Assertions fail loudly if anchors differ.
"""
import os

ROOT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HB = os.path.join(ROOT, "hidden_files")
BUILDS = ["weekly-report-w46-de-build", "weekly-report-w46-de-zh-cn-build",
          "weekly-report-w46-de-zh-tw-build", "weekly-report-w46-de-ko-build",
          "weekly-report-w46-de-ja-build"]

HELPERS = '''
def _kinsoku_shed_piece(_ln, _ns):
    """Piece to shed off the end of _ln. A NO_START glyph goes with the
    glyph before it; a trailing ASCII-punctuated Latin token goes whole
    (never split "76." into "76" + "."); anything else sheds one glyph."""
    if _ln[-1] in ".,:;!?":
        _k = _ln.rfind(" ")
        if _k > 0:
            return _ln[_k + 1:]
    if len(_ln) > 2 and _ln[-1] in _ns:
        return _ln[-2:]
    return _ln[-1:]


def _kinsoku_join_piece(_piece, _nxt):
    """Prepend _piece to _nxt, restoring the space the raw wrap consumed
    at the break when a punctuated Latin token rejoins Latin text."""
    if (_piece and _piece[-1] in ".,:;!?" and _nxt
            and ord(_nxt[0]) < 0x2E80 and _nxt[0].isalnum()):
        return _piece + " " + _nxt
    return _piece + _nxt

'''

OLD_NO_START_CJK = '    NO_START = "。、，．！？：；）」』】})"'
NEW_NO_START_CJK = '    NO_START = "。、，．！？：；）」』】}),.:;!?"'
JA_NO_START_OLD = '    NO_START = "。、，．！？：；）」』】ー…‥・ぁぃぅぇぉゎっゃゅょァィゥェォヮッャュョ"'
JA_NO_START_NEW = '    NO_START = "。、，．！？：；）」』】ー…‥・ぁぃぅぇぉゎっゃゅょァィゥェォヮッャュョ,.:;!?"'

END_SHED_OLD = """                    if lines[_j][-1] in NO_START and len(lines[_j]) > 2:
                        _move, lines[_j] = lines[_j][-2:], lines[_j][:-2]
                    else:
                        _move, lines[_j] = lines[_j][-1], lines[_j][:-1]
                    lines[_j + 1] = _move + lines[_j + 1]"""
END_SHED_NEW = """                    _move = _kinsoku_shed_piece(lines[_j], NO_START)
                    if len(lines[_j]) - len(_move) < 1:
                        _move = lines[_j][-1:]
                    lines[_j] = lines[_j][:-len(_move)].rstrip()
                    lines[_j + 1] = _kinsoku_join_piece(_move, lines[_j + 1])"""

END_ELSE_OLD = """                else:
                    lines.append(lines[_j][-1])
                    lines[_j] = lines[_j][:-1]
                    break"""
END_ELSE_NEW = """                else:
                    _move = _kinsoku_shed_piece(lines[_j], NO_START)
                    if len(lines[_j]) - len(_move) < 1:
                        _move = lines[_j][-1:]
                    lines.append(_move)
                    lines[_j] = lines[_j][:-len(_move)].rstrip()
                    break"""

SEAM_SHED_OLD = """            if lines[i][-1] in NO_START and len(lines[i]) > 2:
                move, lines[i] = lines[i][-2:], lines[i][:-2]
            else:
                move, lines[i] = lines[i][-1], lines[i][:-1]
            if i + 1 < len(lines):
                lines[i + 1] = move + lines[i + 1]
            else:
                lines.append(move)"""
SEAM_SHED_NEW = """            move = _kinsoku_shed_piece(lines[i], NO_START)
            if len(lines[i]) - len(move) < 1:
                move = lines[i][-1:]
            lines[i] = lines[i][:-len(move)].rstrip()
            if i + 1 < len(lines):
                lines[i + 1] = _kinsoku_join_piece(move, lines[i + 1])
            else:
                lines.append(move)"""

POLISH = """    # Final polish (W46 DE Round 1 fix follow-up): seam shedding can stop
    # exactly on an opening bracket, and the START repair runs before seam,
    # so one last START-then-END sweep closes both violation types. Moves
    # are single glyphs; receiving lines stay within max_w + SEAM_SLACK
    # (verified by the occlusion audit on rendered SVGs).
    for _i in range(1, len(lines)):
        while lines[_i] and lines[_i][0] in NO_START and len(lines[_i - 1]) > 1:
            lines[_i] = lines[_i - 1][-1] + lines[_i]
            lines[_i - 1] = lines[_i - 1][:-1].rstrip()
    for _i in range(len(lines) - 1):
        while len(lines[_i]) > 1 and lines[_i][-1] in NO_END:
            _ch = lines[_i][-1]
            lines[_i] = lines[_i][:-1].rstrip()
            lines[_i + 1] = _ch + lines[_i + 1]
"""

for build in BUILDS:
    p = os.path.join(HB, build, "svglib.py")
    s = open(p, encoding="utf-8").read()
    assert "_kinsoku_shed_piece" not in s, (build, "already patched v2")
    # helpers before wrap()
    anchor = "def wrap(text, kind, bold, size, max_w):"
    assert s.count(anchor) == 1, (build, "wrap anchor", s.count(anchor))
    s = s.replace(anchor, HELPERS.lstrip("\n") + anchor, 1)
    # NO_START sets
    if "de-ja-build" in build:
        assert s.count(JA_NO_START_OLD) == 1, (build, "JA NO_START")
        s = s.replace(JA_NO_START_OLD, JA_NO_START_NEW, 1)
    elif "de-ko-build" in build:
        # KO already carries ",.:;!?" in both NO_START defs (v1 patch).
        assert s.count(NEW_NO_START_CJK) == 2, (build, "KO NO_START", s.count(NEW_NO_START_CJK))
    else:
        assert s.count(OLD_NO_START_CJK) == 2, (build, "NO_START count", s.count(OLD_NO_START_CJK))
        s = s.replace(OLD_NO_START_CJK, NEW_NO_START_CJK)
    # shedding loops
    assert s.count(END_SHED_OLD) == 1, (build, "END shed")
    s = s.replace(END_SHED_OLD, END_SHED_NEW, 1)
    assert s.count(END_ELSE_OLD) == 1, (build, "END else")
    s = s.replace(END_ELSE_OLD, END_ELSE_NEW, 1)
    assert s.count(SEAM_SHED_OLD) == 1, (build, "seam shed")
    s = s.replace(SEAM_SHED_OLD, SEAM_SHED_NEW, 1)
    # polish before wrap()'s return
    tail = "        lines[i] = lines[i].rstrip()\n    return lines\n"
    assert s.count(tail) == 1, (build, "return tail", s.count(tail))
    s = s.replace(tail, "        lines[i] = lines[i].rstrip()\n" + POLISH + "    return lines\n", 1)
    open(p, "w", encoding="utf-8").write(s)
    print("OK kinsoku v2:", build)
print("ALL KINSOKU V2 PATCHES APPLIED")
