# -*- coding: utf-8 -*-
"""Add kinsoku post-processing to wrap() in the CJK build svglib copies
(core, zh-cn, zh-tw, ko) and extend the existing JA kinsoku with an
END pass. Modeled verbatim on the JA build's proven START+seam code.
No other svglib behaviour changes; font-index handling untouched.
Run once. Assertions fail loudly if anchors differ."""
import os

ROOT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HB = os.path.join(ROOT, "hidden_files")

NO_START_CJK = "\u3002\u3001\uff0c\uff0e\uff01\uff1f\uff1a\uff1b\uff09\u300d\u300f\u3011})"
NO_START_KO = NO_START_CJK + ",.:;!?"
NO_END = "\uff08(\uff3b\uff5b\u3008\u300a\u300c\u300e"

def end_pass(no_start):
    return '''
    # kinsoku END pass (W46 DE Round 1 fix, M-5): no line may END with an
    # opening bracket — push it to the head of the next line, shedding
    # trailing glyphs forward (NO_START pairs together) if the receiving
    # line then exceeds max_w. Line count unchanged except a possible
    # appended line when the last line overflows.
    NO_START = "{NS}"
    NO_END = "{NE}"
    for _i in range(len(lines) - 1):
        while len(lines[_i]) > 1 and lines[_i][-1] in NO_END:
            _ch = lines[_i][-1]
            lines[_i] = lines[_i][:-1].rstrip()
            lines[_i + 1] = _ch + lines[_i + 1]
            _j = _i + 1
            while text_w(lines[_j], kind, bold, size) > max_w and len(lines[_j]) > 1:
                if _j + 1 < len(lines):
                    if lines[_j][-1] in NO_START and len(lines[_j]) > 2:
                        _move, lines[_j] = lines[_j][-2:], lines[_j][:-2]
                    else:
                        _move, lines[_j] = lines[_j][-1], lines[_j][:-1]
                    lines[_j + 1] = _move + lines[_j + 1]
                    _j += 1
                else:
                    lines.append(lines[_j][-1])
                    lines[_j] = lines[_j][:-1]
                    break
'''.format(NS=no_start, NE=NO_END)

def start_seam(no_start):
    return '''
    # kinsoku shori: a line must not START with closing punctuation —
    # pull the previous line's last character down (oidashi). Line count unchanged.
    NO_START = "{NS}"
    pre_w = [text_w(ln, kind, bold, size) for ln in lines]
    for i in range(1, len(lines)):
        while lines[i] and lines[i][0] in NO_START and len(lines[i - 1]) > 1:
            lines[i] = lines[i - 1][-1] + lines[i]
            lines[i - 1] = lines[i - 1][:-1].rstrip()
    # Seam repair (2026-10-21 core patch — JA P7 glyph overprint): oidashi
    # never re-measures the receiving line, and a line starting with a
    # NO_START chain (e.g. \u300f!.) pulls one glyph per pass, so the receiving
    # line can end far past max_w. A wrapped line may legitimately sit in
    # the gutter (SEAM_SLACK: the 4-column grid's pitch minus column width),
    # but once its ink crosses the pitch it overprints the neighbouring
    # column's first glyph. Repair ONLY such seam-crossing lines that
    # oidashi itself grew (pre_w <= max_w + SEAM_SLACK): shed trailing
    # glyphs to the head of the next line until the line fits max_w again,
    # cascading forward. A NO_START glyph is shed together with the glyph
    # before it, so the next line never starts with one.
    cascade = False
    for i in range(len(lines)):
        if text_w(lines[i], kind, bold, size) <= max_w + SEAM_SLACK:
            cascade = False
            continue
        if not cascade and pre_w[i] > max_w + SEAM_SLACK:
            continue  # unbreakable token, already seam-crossing pre-kinsoku
        cascade = True
        while text_w(lines[i], kind, bold, size) > max_w and len(lines[i]) > 1:
            if lines[i][-1] in NO_START and len(lines[i]) > 2:
                move, lines[i] = lines[i][-2:], lines[i][:-2]
            else:
                move, lines[i] = lines[i][-1], lines[i][:-1]
            if i + 1 < len(lines):
                lines[i + 1] = move + lines[i + 1]
            else:
                lines.append(move)
        lines[i] = lines[i].rstrip()
    return lines'''.format(NS=no_start)

TAIL = '    if cur.strip():\n        lines.append(cur.rstrip())\n    return lines\n'

def patch_full(build, no_start):
    p = os.path.join(HB, build, "svglib.py")
    s = open(p, encoding="utf-8").read()
    assert "NO_END" not in s, (build, "already patched")
    assert s.count(TAIL) == 1, (build, s.count(TAIL))
    block = ('    if cur.strip():\n        lines.append(cur.rstrip())\n'
             + end_pass(no_start)
             + start_seam(no_start) + '\n')
    s = s.replace(TAIL, block)
    assert s.count("def esc(s):") == 1, build
    assert "SEAM_SLACK = 28" not in s, build
    s = s.replace("def esc(s):", "SEAM_SLACK = 28\n\n\ndef esc(s):", 1)
    open(p, "w", encoding="utf-8").write(s)
    print("OK full kinsoku:", build)

def patch_ja(build):
    p = os.path.join(HB, build, "svglib.py")
    s = open(p, encoding="utf-8").read()
    anchor = '    NO_START = "\u3002\u3001\uff0c\uff0e\uff01\uff1f\uff1a\uff1b\uff09\u300d\u300f\u3011\u30fc\u2026\u2025\u30fb\u3041\u3043\u3045\u3047\u3049\u308e\u3063\u3083\u3085\u3087\u30a1\u30a3\u30a5\u30a7\u30a9\u30ee\u30c3\u30e3\u30e5\u30e7"'
    assert s.count(anchor) == 1, ("ja anchor", s.count(anchor))
    assert "NO_END" not in s, "ja already patched"
    ja_no_start = "\u3002\u3001\uff0c\uff0e\uff01\uff1f\uff1a\uff1b\uff09\u300d\u300f\u3011\u30fc\u2026\u2025\u30fb\u3041\u3043\u3045\u3047\u3049\u308e\u3063\u3083\u3085\u3087\u30a1\u30a3\u30a5\u30a7\u30a9\u30ee\u30c3\u30e3\u30e5\u30e7"
    # END pass goes after the NO_START def, before pre_w; it re-defines
    # NO_START with the identical JA set (harmless) and adds NO_END.
    insert = anchor + '\n    NO_END = "' + NO_END + '"' + '''
    for _i in range(len(lines) - 1):
        while len(lines[_i]) > 1 and lines[_i][-1] in NO_END:
            _ch = lines[_i][-1]
            lines[_i] = lines[_i][:-1].rstrip()
            lines[_i + 1] = _ch + lines[_i + 1]
            _j = _i + 1
            while text_w(lines[_j], kind, bold, size) > max_w and len(lines[_j]) > 1:
                if _j + 1 < len(lines):
                    if lines[_j][-1] in NO_START and len(lines[_j]) > 2:
                        _move, lines[_j] = lines[_j][-2:], lines[_j][:-2]
                    else:
                        _move, lines[_j] = lines[_j][-1], lines[_j][:-1]
                    lines[_j + 1] = _move + lines[_j + 1]
                    _j += 1
                else:
                    lines.append(lines[_j][-1])
                    lines[_j] = lines[_j][:-1]
                    break
'''
    s = s.replace(anchor, insert, 1)
    open(p, "w", encoding="utf-8").write(s)
    print("OK JA END pass:", build)

patch_full("weekly-report-w46-de-build", NO_START_CJK)
patch_full("weekly-report-w46-de-zh-cn-build", NO_START_CJK)
patch_full("weekly-report-w46-de-zh-tw-build", NO_START_CJK)
patch_full("weekly-report-w46-de-ko-build", NO_START_KO)
patch_ja("weekly-report-w46-de-ja-build")
print("ALL KINSOKU PATCHES APPLIED")
