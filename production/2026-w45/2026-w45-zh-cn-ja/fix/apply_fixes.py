# -*- coding: utf-8 -*-
"""Apply the 3 Gate-10 record fixes to build scratch/transform_ja.py.
All replacement strings are EXTRACTED from the build copy / delivered
files, never re-typed, so identity is character-for-character."""
import re, os

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
B = os.path.join(BASE, "hidden_files/weekly-report-w45-zh-cn-ja-build")
T = os.path.join(B, "scratch/transform_ja.py")
src = open(T, encoding="utf-8").read()
orig = src

# ---- Fix (a): disclosure pair LONG -> SHORT (SHORT from build content7.py:91 tail)
c7 = open(os.path.join(B, "content7.py"), encoding="utf-8").read()
lcn = re.search(r'lcn = "(.*)"', c7).group(1)
SHORT = lcn.split("取消。", 1)[1]
assert SHORT.startswith("編集部注：VOL.1で予告した"), SHORT
OLD_DISC = "Editor's note: VOL.1 promised real letters and the best VOL.1 writing in VOL.2. None have arrived, so this corner still prints an editor's example. Deferred, not cancelled."
# pair spans two source lines: ("OLD",\n "NEW"),
pat = re.compile(r'\(\"' + re.escape(OLD_DISC) + r'\",\n \"(.*?)\"\),', re.DOTALL)
m = pat.search(src)
assert m, "disclosure pair not found"
LONG = m.group(1)
assert LONG.startswith("編集部注：VOL.1では本号"), LONG[:40]
assert LONG != SHORT
src = src[:m.start(1)] + SHORT + src[m.end(1):]
print("fix(a): disclosure LONG -> SHORT, len", len(LONG), "->", len(SHORT))

# ---- Fix (b): basket-B pair after the Basket-A pair
anchor_b = '("Basket A is cut by 50 yuan.", "かごAは50元値引きされる。"),'
assert src.count(anchor_b) == 1
newpair = '\n("199 − 20 = 179 yuan.", "199 − 20 = 179元。"),  # fix 3: basket-B note unit (P8 key 94)'
src = src.replace(anchor_b, anchor_b + newpair)
print("fix(b): basket-B pair inserted")

# ---- Fix (c): svglib NO_START extension step in main()
sv = open(os.path.join(B, "svglib.py"), encoding="utf-8").read().split("\n")
idx = [i for i, ln in enumerate(sv) if "NO_START = " in ln]
assert len(idx) == 1, idx
nostart_line = sv[idx[0]]
ext_lines = sv[idx[0]+1:idx[0]+6]
assert len(ext_lines) == 5, ext_lines
assert ext_lines[0].strip().startswith("# W45 zh-cn x ja: small kana")
assert ext_lines[4].strip().startswith('NO_START += "'), ext_lines[4]
ext_block = "\n" + "\n".join(ext_lines)
anchor_c = ('    for fn in FILES:\n        open(os.path.join(BUILD, fn), "w", encoding="utf-8").write(texts[fn])\n'
            '    # render.py: BASE + PDF names (mirror the nl build\'s naming)')
assert src.count(anchor_c) == 1, "main() anchor not found"
step = ('    for fn in FILES:\n        open(os.path.join(BUILD, fn), "w", encoding="utf-8").write(texts[fn])\n'
        '    # svglib NO_START small-kana extension (fix 2; same 5 lines as the\n'
        '    # build copy\'s svglib diff — small kana must not start a line).\n'
        '    sp = os.path.join(BUILD, "svglib.py")\n'
        '    s = open(sp, encoding="utf-8").read()\n'
        '    anchor = ' + repr(nostart_line) + '\n'
        '    assert s.count(anchor) == 1, "svglib NO_START anchor"\n'
        '    assert "ぁぃぅぇぉゃゅょゎっ" not in s, "svglib extension already present"\n'
        '    s = s.replace(anchor, anchor + ' + repr(ext_block) + ')\n'
        '    open(sp, "w", encoding="utf-8").write(s)\n'
        '    log.append("  1x  svglib NO_START small-kana extension (5 lines)")\n'
        '    # render.py: BASE + PDF names (mirror the nl build\'s naming)')
src = src.replace(anchor_c, step)
print("fix(c): svglib step inserted; ext lines:")
for ln in ext_lines: print("   ", ln)

# ---- Header: stale svglib bullet
old_head = "- svglib.py — core version kept for the first render (see KIT)."
assert src.count(old_head) == 1
src = src.replace(old_head, "- svglib.py — NO_START small-kana extension applied by main() (fix 2).")
print("header: svglib bullet updated")

open(T, "w", encoding="utf-8").write(src)
print("transform_ja.py rewritten; bytes", len(orig), "->", len(src))
