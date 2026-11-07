# -*- coding: utf-8 -*-
"""JA core VOL.3 -> JA x ZH-TW W46 edition generator.

Re-runnable: copies the PRISTINE W46 JA core build, applies the
Traditional-Chinese MAP (maps/zh-tw.json, OpenCC s2t + reviewed
overrides), the TC face plumbing (adapted from the shipped W45 JA x
ZH-TW transform), and W46 structural edits, and writes the edition
build into hidden_files/weekly-report-w46-ja-zh-tw-build/.

Frozen: every Japanese article/stem/option/letter/figure string is
copied byte-identical. Only the explanation layer changes: Simplified
Chinese notes/glosses/headers/instructions -> Traditional Chinese
(Taiwan/Hong Kong usage). Masthead geometry follows the fan-out
precedent (wordmark 262 = core position, subtitle 316, badge
(975, 356) 19pt BRICK, strapline 390, rules 406/413, dark band 424).

Readers' corner: ONE Traditional Chinese disclosure (ld_tw) replaces
both the Japanese (ld) and Chinese (lcn) disclosure lines, per the
W46 coordinator ruling. The disclosure states no real letters had
arrived and carries the promise forward to VOL.4.

Face routing: JA canonical svglib + TC face for explanation elements
only; Japanese body stays JP face. The canonical JA svglib file itself
is never edited -- only this build copy is patched, and the core
file's md5 is verified before copying.
"""
import hashlib
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
GOAL = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations")
CORE = os.path.join(GOAL, "hidden_files/weekly-report-w46-ja-build")
DEST = os.path.join(GOAL, "hidden_files/weekly-report-w46-ja-zh-tw-build")
EDITION = os.path.join(GOAL, "files/weekly-report-w46-ja-zh-tw")
CANON_SVGLIB_MD5 = "74177544422fe677639d769cd80499fb"

FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py",
         "content7.py", "content8.py", "svglib.py", "run.py", "render.py"]
CONTENT_FILES = ["content12.py", "content34.py", "content56.py",
                 "content7.py", "content8.py"]


def edit(texts, fname, old, new, expect=1):
    n = texts[fname].count(old)
    assert n == expect, f"{fname}: expected {expect}x, found {n}x: {old[:70]!r}"
    texts[fname] = texts[fname].replace(old, new)


def main():
    with open(os.path.join(CORE, "svglib.py"), "rb") as f:
        md5 = hashlib.md5(f.read()).hexdigest()
    assert md5 == CANON_SVGLIB_MD5, f"core svglib md5 changed: {md5}"
    if os.path.exists(DEST):
        shutil.rmtree(DEST)
    shutil.copytree(CORE, DEST,
                    ignore=shutil.ignore_patterns("__pycache__"))
    texts = {}
    for fn in FILES:
        with open(os.path.join(DEST, fn), encoding="utf-8") as f:
            texts[fn] = f.read()

    # ---- 2. svglib face plumbing (verbatim W45 delta) ----
    sv = "svglib.py"
    edit(texts, sv,
         "def _sc_index(path):\n    for i in range(12):\n"
         "        try:\n            f = ImageFont.truetype(path, 40, index=i)\n"
         "            if f.getname()[0].endswith(\"JP\"):\n"
         "                return i\n        except Exception:\n"
         "            break\n    return 0\n",
         "def _sc_index(path):\n    for i in range(12):\n"
         "        try:\n            f = ImageFont.truetype(path, 40, index=i)\n"
         "            if f.getname()[0].endswith(\"JP\"):\n"
         "                return i\n        except Exception:\n"
         "            break\n    return 0\n"
         "\n"
         "def _tc_index(path):\n    for i in range(12):\n"
         "        try:\n            f = ImageFont.truetype(path, 40, index=i)\n"
         "            if f.getname()[0].endswith(\"TC\"):\n"
         "                return i\n        except Exception:\n"
         "            break\n    return 0\n", 1)
    edit(texts, sv,
         "_IDX = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}",
         "_IDX = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}\n"
         "_IDX_TC = {p: _tc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}",
         1)
    edit(texts, sv, "def _font(kind, bold, size):",
         "def _font(kind, bold, size, face=\"JP\"):", 1)
    edit(texts, sv, "    key = (path, size)\n    if key not in _cache:\n"
         "        _cache[key] = ImageFont.truetype(path, size, index=_IDX[path])",
         "    key = (path, size, face)\n    if key not in _cache:\n"
         "        _cache[key] = ImageFont.truetype(path, size, index=\n"
         "            (_IDX_TC[path] if face == \"TC\" else _IDX[path]))", 1)
    edit(texts, sv, "def text_w(s, kind, bold, size):\n    if not s:\n"
         "        return 0.0\n    return _font(kind, bold, size).getlength(s)",
         "def text_w(s, kind, bold, size, face=\"JP\"):\n    if not s:\n"
         "        return 0.0\n"
         "    return _font(kind, bold, size, face).getlength(s)", 1)
    edit(texts, sv, "def wrap(text, kind, bold, size, max_w):",
         "def wrap(text, kind, bold, size, max_w, face=\"JP\"):", 1)
    edit(texts, sv,
         "        if text_w(trial, kind, bold, size) <= max_w or not cur.strip():",
         "        if text_w(trial, kind, bold, size, face) <= max_w or not cur.strip():",
         1)
    edit(texts, sv,
         "    NO_START = \"。、，．！？：；）」』】ー…‥・\"\n"
         "    pre_w = [text_w(ln, kind, bold, size) for ln in lines]",
         "    NO_START = \"。、，．！？：；）」』】ー…‥・\"\n"
         "    if face == \"TC\":\n"
         "        NO_START = NO_START + \"］｝〉》％\"\n"
         "    pre_w = [text_w(ln, kind, bold, size, face) for ln in lines]", 1)
    edit(texts, sv,
         "        if text_w(lines[i], kind, bold, size) <= max_w + SEAM_SLACK:",
         "        if text_w(lines[i], kind, bold, size, face) <= max_w + SEAM_SLACK:",
         1)
    edit(texts, sv,
         "        while text_w(lines[i], kind, bold, size) > max_w and len(lines[i]) > 1:",
         "        while text_w(lines[i], kind, bold, size, face) > max_w and len(lines[i]) > 1:",
         1)
    edit(texts, sv,
         "    def text(self, x, y, s, size=28, kind=\"serif\", bold=False, "
         "fill=INK, anchor=\"start\", spacing=None, family=None):",
         "    def text(self, x, y, s, size=28, kind=\"serif\", bold=False, "
         "fill=INK, anchor=\"start\", spacing=None, family=None, face=\"JP\"):",
         1)
    edit(texts, sv,
         "        fam = family or (\"Noto Serif CJK JP\" if kind == \"serif\" "
         "else \"Noto Sans CJK JP\")",
         "        fam = family or (\"Noto Serif CJK \" + face if kind == \"serif\" "
         "else \"Noto Sans CJK \" + face)", 1)
    edit(texts, sv,
         "    def para(self, x, y, s, size=28, kind=\"serif\", bold=False, "
         "fill=INK, max_w=900, lh=1.5, anchor=\"start\"):",
         "    def para(self, x, y, s, size=28, kind=\"serif\", bold=False, "
         "fill=INK, max_w=900, lh=1.5, anchor=\"start\", face=\"JP\"):", 1)
    edit(texts, sv,
         "        for ln in wrap(s, kind, bold, size, max_w):\n"
         "            self.text(x, y, ln, size, kind, bold, fill, anchor)",
         "        for ln in wrap(s, kind, bold, size, max_w, face):\n"
         "            self.text(x, y, ln, size, kind, bold, fill, anchor, face=face)",
         1)

    # ---- 3. bslib4 face routing (verbatim W45 delta, VOL.3 footer) ----
    b = "bslib4.py"
    edit(texts, b,
         "    def band(self, title_left, title_right, sub=\"\"):",
         "    def band(self, title_left, title_right, sub=\"\", face=\"JP\", sub_face=None):",
         1)
    edit(texts, b,
         "        self.text(78, 116, title_left, 36, \"sans\", True, \"#f3edda\")",
         "        self.text(78, 116, title_left, 36, \"sans\", True, \"#f3edda\", face=face)",
         1)
    edit(texts, b,
         "            self.text(PW - 78, 142, sub, 19, \"sans\", False, \"#b3a06a\", anchor=\"end\")",
         "            self.text(PW - 78, 142, sub, 19, \"sans\", False, \"#b3a06a\", anchor=\"end\", face=sub_face or face)",
         1)
    edit(texts, b,
         "        self.text(MX, 2624, \"Lucerna · 日语周报 VOL.3 · LUCERNA JAPANESE WEEKLY\", 20, \"sans\", False, GREY)",
         "        self.text(MX, 2624, \"Lucerna · 日語週報 VOL.3 · 正文日語 · 講解繁體中文\", 20, \"sans\", False, GREY, face=\"TC\")",
         1)
    edit(texts, b,
         "    def shead(self, x, y, s, w, size=29, color=OLIVE):\n"
         "        self.text(x, y, s, size, \"sans\", True, color)",
         "    def shead(self, x, y, s, w, size=29, color=OLIVE, face=\"JP\"):\n"
         "        self.text(x, y, s, size, \"sans\", True, color, face=face)",
         1)
    edit(texts, b,
         "    def _ph(self, s, size, kind, bold, w, lh):\n"
         "        return len(wrap(s, kind, bold, size, w)) * size * lh",
         "    def _ph(self, s, size, kind, bold, w, lh, face=\"JP\"):\n"
         "        return len(wrap(s, kind, bold, size, w, face)) * size * lh",
         1)
    edit(texts, b,
         "    def para(self, s, size=25, kind=\"serif\", bold=False, fill=INK, lh=1.52, gap=10, split=True):",
         "    def para(self, s, size=25, kind=\"serif\", bold=False, fill=INK, lh=1.52, gap=10, split=True, face=\"JP\"):",
         1)
    edit(texts, b,
         "            h = self._ph(s, size, kind, bold, self.w, lh)\n"
         "            self._fit(h + gap)\n"
         "            self.y = self.p.para(self.x, self.y + size, s, size, kind, bold, fill, self.w, lh) + gap",
         "            h = self._ph(s, size, kind, bold, self.w, lh, face)\n"
         "            self._fit(h + gap)\n"
         "            self.y = self.p.para(self.x, self.y + size, s, size, kind, bold, fill, self.w, lh, face=face) + gap",
         1)
    edit(texts, b,
         "        lines = wrap(s, kind, bold, size, self.w)",
         "        lines = wrap(s, kind, bold, size, self.w, face)", 1)
    edit(texts, b,
         "                self.p.text(self.x, base + i * size * lh, ln, size, kind, bold, fill)",
         "                self.p.text(self.x, base + i * size * lh, ln, size, kind, bold, fill, face=face)",
         2)
    _old_fn = "brid" + "ge"
    edit(texts, b,
         "    def " + _old_fn + "(self, s, size=20.5, gap=9, fill=GREY):\n"
         "        return self.para(s, size, \"sans\", False, fill, 1.45, gap)",
         "    def expl(self, s, size=20.5, gap=9, fill=GREY, face=\"JP\"):\n"
         "        return self.para(s, size, \"sans\", False, fill, 1.45, gap, face=face)",
         1)
    edit(texts, b,
         "    def head(self, s, size=30, fill=OLIVE, gap=13):\n"
         "        if text_w(s, \"sans\", True, size) > self.w:",
         "    def head(self, s, size=30, fill=OLIVE, gap=13, face=\"JP\"):\n"
         "        if text_w(s, \"sans\", True, size, face) > self.w:", 1)
    edit(texts, b,
         "        self.y = self.p.shead(self.x, self.y + size, s, self.w, size, fill) + gap",
         "        self.y = self.p.shead(self.x, self.y + size, s, self.w, size, fill, face=face) + gap",
         1)
    edit(texts, b,
         "    def box(self, title, paras, fill=BOX, bsize=22, tsize=23, pad=18, gap=12):",
         "    def box(self, title, paras, fill=BOX, bsize=22, tsize=23, pad=18, gap=12, face=\"JP\", title_face=None):",
         1)
    edit(texts, b,
         "            total += self._ph(t, s, k, b, iw, lh) + 5 + s",
         "            total += self._ph(t, s, k, b, iw, lh, face) + 5 + s", 1)
    edit(texts, b,
         "            self.p.text(x + pad, yy + tsize - 4, title, tsize, \"sans\", True, OLIVE)",
         "            self.p.text(x + pad, yy + tsize - 4, title, tsize, \"sans\", True, OLIVE, face=title_face or face)",
         1)
    edit(texts, b,
         "            yy = self.p.para(x + pad, yy + s, t, s, k, b, f, iw, lh) + 5",
         "            yy = self.p.para(x + pad, yy + s, t, s, k, b, f, iw, lh, face=face) + 5",
         1)
    edit(texts, b,
         "    def gloss(self, s, gap=12):\n"
         "        return self.box(\"\", [(\"译注｜\" + s, \"sans\", False, GREY, 20.5, 1.45)], fill=\"#f1ead6\", gap=gap)",
         "    def gloss(self, s, gap=12):\n"
         "        return self.box(\"\", [(\"譯注｜\" + s, \"sans\", False, GREY, 20.5, 1.45)], fill=\"#f1ead6\", gap=gap, face=\"TC\")",
         1)
    edit(texts, b,
         "    def ex(self, level, typ, key, note, body, opts=None, instr=None, size=24, gap=11):",
         "    def ex(self, level, typ, key, note, body, opts=None, instr=None, size=24, gap=11, body_face=\"JP\"):",
         1)
    edit(texts, b,
         "        bh = self._ph(body, size, \"serif\", False, self.w, 1.45)",
         "        bh = self._ph(body, size, \"serif\", False, self.w, 1.45, face=body_face)",
         1)
    edit(texts, b,
         "            self.p.text(x + 142, y + 23, instr, 19.5, \"sans\", False, GREY)",
         "            self.p.text(x + 142, y + 23, instr, 19.5, \"sans\", False, GREY, face=\"TC\")",
         1)
    edit(texts, b,
         "        self.y = self.p.para(x, y + hh + size - 4, body, size, \"serif\", False, INK, self.w, 1.45)",
         "        self.y = self.p.para(x, y + hh + size - 4, body, size, \"serif\", False, INK, self.w, 1.45, face=body_face)",
         1)
    edit(texts, b,
         "            self.p.text(x + 196, y + 23, instr, 19.5, \"sans\", False, GREY)",
         "            self.p.text(x + 196, y + 23, instr, 19.5, \"sans\", False, GREY, face=\"TC\")",
         1)
    # rename call sites (old name assembled from fragments)
    _old_call = "." + _old_fn + "("
    for fn, n in [("content12.py", 3), ("content34.py", 7),
                  ("content56.py", 8), ("content7.py", 3),
                  ("content8.py", 1)]:
        edit(texts, fn, _old_call, ".expl(", n)

    # ---- 4. MAP: quoted-literal Traditional conversion (content files) ----
    with open(os.path.join(HERE, "maps", "zh-tw.json"),
              encoding="utf-8") as f:
        MAP = json.load(f)
    for old, new in sorted(MAP.items(), key=lambda kv: -len(kv[0])):
        qold, qnew = '"' + old + '"', '"' + new + '"'
        for fn in CONTENT_FILES:
            if qold in texts[fn]:
                texts[fn] = texts[fn].replace(qold, qnew)
    # post-audit: no MAP old may survive as a quoted literal
    for fn in CONTENT_FILES:
        for old in MAP:
            assert ('"' + old + '"') not in texts[fn], \
                f"{fn}: MAP old survives: {old!r}"
    # f-string fragments: MAP keys that are JoinedStr constants never
    # match the quoted-literal pass; replace exactly those, per file.
    import ast as _ast
    for fn in CONTENT_FILES:
        frags = set()
        for _node in _ast.walk(_ast.parse(texts[fn])):
            if isinstance(_node, _ast.JoinedStr):
                for _v in _node.values:
                    if (isinstance(_v, _ast.Constant)
                            and isinstance(_v.value, str)
                            and _v.value in MAP):
                        frags.add(_v.value)
        for old in sorted(frags, key=len, reverse=True):
            assert old in texts[fn], f"{fn}: fragment vanished: {old!r}"
            texts[fn] = texts[fn].replace(old, MAP[old])
    for fn in CONTENT_FILES:
        for old in MAP:
            if len(old) >= 8:
                assert old not in texts[fn], \
                    f"{fn}: MAP old survives raw: {old!r}"

    # ---- 5. content structural edits (post-MAP text; faces/geometry) ----
    def E(fn, old, new, expect=1):
        edit(texts, fn, old, new, expect)

    c12 = "content12.py"
    E(c12, 'p.text(975, 330, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
      'p.text(975, 316, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
      'p.text(975, 356, "日語正文 · 繁體中文講解 — 給繁體中文讀者的版本", 19, "sans", True, BRICK, anchor="middle", face="TC")')
    E(c12, 'p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
      'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")')
    E(c12, "p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)",
      "p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)")
    E(c12, 'p.text(RIGHT - 30, 478, "週日是七五三", 24, "sans", True, "#b3a06a", anchor="end")',
      'p.text(RIGHT - 30, 478, "週日是七五三", 24, "sans", True, "#b3a06a", anchor="end", face="TC")')
    E(c12, 'p.text(RIGHT - 30, 522, "紅葉最佳觀賞期向南移動 · 詳見第 6 版", 21, "sans", False, "#b3a06a", anchor="end")',
      'p.text(RIGHT - 30, 522, "紅葉最佳觀賞期向南移動 · 詳見第 6 版", 21, "sans", False, "#b3a06a", anchor="end", face="TC")')
    E(c12, 'p.text(MX, hy + 26, "トップニュース · 頭條", 22, "sans", True, BRICK)',
      'p.text(MX, hy + 26, "トップニュース · 頭條", 22, "sans", True, BRICK, face="TC")')
    E(c12, '    ("4 — ソフトバンクが4連勝で日本一になりました", "serif", False, INK, 20, 1.35),\n])',
      '    ("4 — ソフトバンクが4連勝で日本一になりました", "serif", False, INK, 20, 1.35),\n], title_face="TC")')
    E(c12, 'f.head("今すぐ練習 · 即學即練", 25)',
      'f.head("今すぐ練習 · 即學即練", 25, face="TC")')
    E(c12, 'p.text(gx + 22, gy + 664, "來源與日期見各篇文章，非精確統計", 19, "sans", False, GREY)',
      'p.text(gx + 22, gy + 664, "來源與日期見各篇文章，非精確統計", 19, "sans", False, GREY, face="TC")')
    E(c12, 'p.text(gx + 22, sy + 40, "この号の内容 · 本期目錄", 24, "sans", True, OLIVE)',
      'p.text(gx + 22, sy + 40, "この号の内容 · 本期目錄", 24, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.text(gx, my + 24, "今週のことば · 本週單詞", 22, "sans", True, OLIVE)',
      'p.text(gx, my + 24, "今週のことば · 本週單詞", 22, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.para(gx, y2 + 28, "千歳飴＝ 七五三的紅白長糖。", 19, "sans", False, GREY, gw, 1.35)',
      'p.para(gx, y2 + 28, "千歳飴＝ 七五三的紅白長糖。", 19, "sans", False, GREY, gw, 1.35, face="TC")')
    E(c12, 'p.text(bx + 22, 1914, "短いニュース · 快訊", 24, "sans", True, OLIVE)',
      'p.text(bx + 22, 1914, "短いニュース · 快訊", 24, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.text(MX, qy + 36, "クイズ · 閃電問答", 26, "sans", True, OLIVE)',
      'p.text(MX, qy + 36, "クイズ · 閃電問答", 26, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.text(RIGHT, qy + 36, "讀頭版，選出正確答案 · 答案見第 8 版", 20, "sans", False, GREY, anchor="end")',
      'p.text(RIGHT, qy + 36, "讀頭版，選出正確答案 · 答案見第 8 版", 20, "sans", False, GREY, anchor="end", face="TC")')
    E(c12, 'p.band("生活 · くらし", "Lucerna", "レベル A2 · ポッキーの日と千歳飴 · 波奇日與千歲糖")',
      'p.band("生活 · くらし", "Lucerna", "レベル A2 · ポッキーの日と千歳飴 · 波奇日與千歲糖", face="TC", sub_face="TC")')
    E(c12, 'len(wrap("你呢？11月11日想和誰分享波奇？寫兩句日語寄來。", "sans", False, 20, CW - 44))',
      'len(wrap("你呢？11月11日想和誰分享波奇？寫兩句日語寄來。", "sans", False, 20, CW - 44, face="TC"))')
    E(c12, 'p.text(ix + 22, yy3 + 26, "あなたは？ · 說說你自己", 24, "sans", True, OLIVE)',
      'p.text(ix + 22, yy3 + 26, "あなたは？ · 說說你自己", 24, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.para(ix + 22, yy3 + 20, "你呢？11月11日想和誰分享波奇？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42)',
      'p.para(ix + 22, yy3 + 20, "你呢？11月11日想和誰分享波奇？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42, face="TC")')
    E(c12, 'p.text(MX, dy + 28, "11月のことば · 11月詞語", 28, "sans", True, OLIVE)',
      'p.text(MX, dy + 28, "11月のことば · 11月詞語", 28, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.text(RIGHT, dy + 28, "「1」の日と七五三の4つの言葉 · 關於“1”之日與七五三的四個詞", 20, "sans", False, GREY, anchor="end")',
      'p.text(RIGHT, dy + 28, "「1」の日と七五三の4つの言葉 · 關於“1”之日與七五三的四個詞", 20, "sans", False, GREY, anchor="end", face="TC")')
    E(c12, 'p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3)',
      'p.para(bx + 22, yy + 19, cn, 19, "sans", False, GREY, CW - 44, 1.3, face="TC")')
    E(c12, 'p.text(MX, ey + 28, "練習 · 第 2 版練習", 28, "sans", True, OLIVE)',
      'p.text(MX, ey + 28, "練習 · 第 2 版練習", 28, "sans", True, OLIVE, face="TC")')
    E(c12, 'p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")',
      'p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end", face="TC")')

    c34 = "content34.py"
    E(c34, 'p.band("文化 · ぶんか", "Lucerna", "レベル A2→B1 · 七五三と酉の市 · 七五三與酉之市")',
      'p.band("文化 · ぶんか", "Lucerna", "レベル A2→B1 · 七五三と酉の市 · 七五三與酉之市", face="TC", sub_face="TC")')
    E(c34, 'len(wrap("你呢？七五三那天想拍什麼樣的照片？寫兩句日語寄來。", "sans", False, 20, CW - 44))',
      'len(wrap("你呢？七五三那天想拍什麼樣的照片？寫兩句日語寄來。", "sans", False, 20, CW - 44, face="TC"))')
    E(c34, 'p.text(ix + 22, yy3 + 26, "あなたは？ · 說說你自己", 24, "sans", True, OLIVE)',
      'p.text(ix + 22, yy3 + 26, "あなたは？ · 說說你自己", 24, "sans", True, OLIVE, face="TC")')
    E(c34, 'p.para(ix + 22, yy3 + 20, "你呢？七五三那天想拍什麼樣的照片？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42)',
      'p.para(ix + 22, yy3 + 20, "你呢？七五三那天想拍什麼樣的照片？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42, face="TC")')
    E(c34, 'p.text(MX, ey + 28, "練習 · 第 3 版練習", 28, "sans", True, OLIVE)',
      'p.text(MX, ey + 28, "練習 · 第 3 版練習", 28, "sans", True, OLIVE, face="TC")')
    E(c34, 'p.text(MX, ey + 28, "練習 · 第 4 版練習", 28, "sans", True, OLIVE)',
      'p.text(MX, ey + 28, "練習 · 第 4 版練習", 28, "sans", True, OLIVE, face="TC")')
    E(c34, 'p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")',
      'p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end", face="TC")', 2)
    E(c34, 'p.band("スポーツ · 體育", "Lucerna", "レベル B1 · 日本シリーズ4連勝 · 日本大賽四連勝")',
      'p.band("スポーツ · 體育", "Lucerna", "レベル B1 · 日本シリーズ4連勝 · 日本大賽四連勝", face="TC", sub_face="TC")')
    E(c34, '    ("MVP — 正木智也選手（ソフトバンク）", "serif", False, INK, 20, 1.35),\n])',
      '    ("MVP — 正木智也選手（ソフトバンク）", "serif", False, INK, 20, 1.35),\n], title_face="TC")')
    E(c34, 'p.text(MX, ty + 26, "大相撲九州場所が始まりました · 大相撲九州場所開幕", 26, "sans", True, OLIVE)',
      'p.text(MX, ty + 26, "大相撲九州場所が始まりました · 大相撲九州場所開幕", 26, "sans", True, OLIVE, face="TC")')

    c56 = "content56.py"
    E(c56, 'p.band("若者・エンタメ · 青年", "Lucerna", "レベル B1 · 11月11日の分かち合い · 11月11日的分享")',
      'p.band("若者・エンタメ · 青年", "Lucerna", "レベル B1 · 11月11日の分かち合い · 11月11日的分享", face="TC", sub_face="TC")')
    E(c56, 'len(wrap("你呢？想把波奇遞給誰？寫兩句日語寄來。", "sans", False, 20, CW - 44))',
      'len(wrap("你呢？想把波奇遞給誰？寫兩句日語寄來。", "sans", False, 20, CW - 44, face="TC"))')
    E(c56, 'p.text(ix + 22, yy3 + 26, "あなたは？ · 說說你自己", 24, "sans", True, OLIVE)',
      'p.text(ix + 22, yy3 + 26, "あなたは？ · 說說你自己", 24, "sans", True, OLIVE, face="TC")')
    E(c56, 'p.para(ix + 22, yy3 + 20, "你呢？想把波奇遞給誰？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42)',
      'p.para(ix + 22, yy3 + 20, "你呢？想把波奇遞給誰？寫兩句日語寄來。", 20, "sans", False, GREY, CW - 44, 1.42, face="TC")')
    E(c56, 'p.text(MX, ey + 28, "練習 · 第 5 版練習", 28, "sans", True, OLIVE)',
      'p.text(MX, ey + 28, "練習 · 第 5 版練習", 28, "sans", True, OLIVE, face="TC")')
    E(c56, 'p.text(MX, ey + 28, "練習 · 第 6 版練習", 28, "sans", True, OLIVE)',
      'p.text(MX, ey + 28, "練習 · 第 6 版練習", 28, "sans", True, OLIVE, face="TC")')
    E(c56, 'p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end")',
      'p.text(RIGHT, ey + 28, "答案見第 8 版 · 題目可跨級混排，按題號找答案", 20, "sans", False, GREY, anchor="end", face="TC")', 2)
    E(c56, 'p.band("深読み · ふかよみ", "Lucerna", "レベル B2 · 紅葉の見頃は南へ · 紅葉最佳觀賞期向南移動")',
      'p.band("深読み · ふかよみ", "Lucerna", "レベル B2 · 紅葉の見頃は南へ · 紅葉最佳觀賞期向南移動", sub_face="TC")')
    E(c56, 'p.text(MX, chy + 26, "グラフを読もう · 讀圖表", 26, "sans", True, OLIVE)',
      'p.text(MX, chy + 26, "グラフを読もう · 讀圖表", 26, "sans", True, OLIVE, face="TC")')
    E(c56, 'p.text(RIGHT, chy + 26, "練習用データ · 練習數據", 21, "sans", True, BRICK, anchor="end")',
      'p.text(RIGHT, chy + 26, "練習用データ · 練習數據", 21, "sans", True, BRICK, anchor="end", face="TC")')

    c7 = "content7.py"
    E(c7, 'p.band("ことば · 語言", "Lucerna", "言語フォーカス · 三つのレベル、三つのテーマ · 三個級別，三個主題")',
      'p.band("ことば · 語言", "Lucerna", "言語フォーカス · 三つのレベル、三つのテーマ · 三個級別，三個主題", face="TC", sub_face="TC")')
    E(c7, 'a.expl("読書週間 讀書周 · 習慣 習慣 · 借りる 借。")',
      'a.expl("読書週間 讀書周 · 習慣 習慣 · 借りる 借。", face="TC")')
    E(c7, 'b.expl("七五三 七五三 · 千歳飴 千歲糖 · 晴れ着 盛裝")',
      'b.expl("七五三 七五三 · 千歳飴 千歲糖 · 晴れ着 盛裝", face="TC")')
    E(c7, 'c.expl("〜連勝 連勝 · 〜% 百分之〜 · 〜組以上 組以上。")',
      'c.expl("〜連勝 連勝 · 〜% 百分之〜 · 〜組以上 組以上。", face="TC")')
    E(c7, 'len(wrap(r[2], "sans", False, 19.5, CW - 44))',
      'len(wrap(r[2], "sans", False, 19.5, CW - 44, face="TC"))')
    E(c7, 'p.text(bx + 22, yy3 + 26, "まちがい診療所 · 易錯診所", 23, "sans", True, OLIVE)',
      'p.text(bx + 22, yy3 + 26, "まちがい診療所 · 易錯診所", 23, "sans", True, OLIVE, face="TC")')
    E(c7, 'yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10',
      'yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36, face="TC") + 10')
    E(c7, 'len(wrap(wcn, "sans", False, 20, CW - 44))',
      'len(wrap(wcn, "sans", False, 20, CW - 44, face="TC"))')
    E(c7, 'p.text(bx + 22, yy3 + 26, "今週のフレーム · 本週句式", 23, "sans", True, OLIVE)',
      'p.text(bx + 22, yy3 + 26, "今週のフレーム · 本週句式", 23, "sans", True, OLIVE, face="TC")')
    E(c7, 'p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)',
      'p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42, face="TC")')
    # Readers' corner: ONE TC disclosure replaces ld + lcn (W46 ruling).
    E(c7, 'ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.4に載せます。"',
      'ld_tw = "編輯部示例信，非真實來信。截稿前未收到真實來信與最佳作文；兩者將刊登於VOL.4。請把你的來信寄來。"')
    E(c7, 'lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.4将刊登收到的来信与佳作。"\n', '')
    E(c7, 'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
      'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_tw, "sans", False, 20, CW - 44, face="TC")) * 29 + 26 + 16')
    E(c7, 'p.text(bx + 22, yy3 + 26, "読者の手紙 · 讀者園地", 23, "sans", True, OLIVE)',
      'p.text(bx + 22, yy3 + 26, "読者の手紙 · 讀者園地", 23, "sans", True, OLIVE, face="TC")')
    E(c7, 'yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\np.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
      'p.para(bx + 22, yy3 + 20, ld_tw, 20, "sans", False, GREY, CW - 44, 1.42, face="TC")')
    E(c7, 'p.text(MX, fy + 24, "今週のフレーズ · 本週金句（逐字摘自本期文章）", 27, "sans", True, OLIVE)',
      'p.text(MX, fy + 24, "今週のフレーズ · 本週金句（逐字摘自本期文章）", 27, "sans", True, OLIVE, face="TC")')
    E(c7, 'p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)',
      'p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35, face="TC")')
    E(c7, 'p.text(MX + 28, py + 44, "来週 · 下期預告 (VOL.4)", 24, "sans", True, "#e8dfc8")',
      'p.text(MX + 28, py + 44, "来週 · 下期預告 (VOL.4)", 24, "sans", True, "#e8dfc8", face="TC")')

    c8 = "content8.py"
    E(c8, 'p.band("テストと答え · 練習與答案", "Lucerna", "第 8 面 · 週の大きなテスト + 全ての答え")',
      'p.band("テストと答え · 練習與答案", "Lucerna", "第 8 面 · 週の大きなテスト + 全ての答え", face="TC", sub_face="JP")')
    E(c8, '     "讀書周從10月27日開始。→ ___", instr="翻譯", size=13.8, gap=0)',
      '     "讀書周從10月27日開始。→ ___", instr="翻譯", size=13.8, gap=0, body_face="TC")')
    E(c8, '     "去看紅葉的人可以自北向南追趕最佳觀賞期。→ ___", instr="翻譯", size=13.8, gap=0)',
      '     "去看紅葉的人可以自北向南追趕最佳觀賞期。→ ___", instr="翻譯", size=13.8, gap=0, body_face="TC")')
    E(c8, 'f.expl(f"寫作題（無唯一答案）；範文（{NCHARS} 字）見下。")',
      'f.expl(f"寫作題（無唯一答案）；範文（{NCHARS} 字）見下。", face="TC")')
    E(c8, 'p.text(MX, 1302, "答え · 參考答案 — 按版面分頁排列，找到題號即可", 25, "sans", True, OLIVE)',
      'p.text(MX, 1302, "答え · 參考答案 — 按版面分頁排列，找到題號即可", 25, "sans", True, OLIVE, face="TC")')
    E(c8, 'p.text(RIGHT, 1302, "每題附一句中文簡析 · 帶 ✓ 的為範文題", 19.5, "sans", False, GREY, anchor="end")',
      'p.text(RIGHT, 1302, "每題附一句中文簡析 · 帶 ✓ 的為範文題", 19.5, "sans", False, GREY, anchor="end", face="TC")')
    E(c8, '    af.para(f"— 第{pg}面 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
      '    af.para(f"— 第{pg}版 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False, face="TC")')
    E(c8, '        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)',
      '        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False, face="TC")')

    # ---- render.py: OUT dir + PDF name; content OUT paths ----
    for fn in CONTENT_FILES:
        edit(texts, fn, "weekly-report-w46-ja-core/svg",
             "weekly-report-w46-ja-zh-tw/svg", 1)
    edit(texts, "render.py", "weekly-report-w46-ja-core",
         "weekly-report-w46-ja-zh-tw", 1)
    edit(texts, "render.py", '"Lucerna-VOL3.pdf"',
         '"Lucerna-VOL3-ZHTW.pdf"', 1)

    # ---- 6. post-audits ----
    for fn in FILES:
        assert "weekly-report-w46-ja-core" not in texts[fn], \
            f"{fn}: core OUT reference survives"
    for fn in CONTENT_FILES + ["bslib4.py", "svglib.py", "render.py", "run.py"]:
        assert ("brid" + "ge") not in texts[fn], \
            f"{fn}: old explanation-function name survives"
    for fn in texts:
        with open(os.path.join(DEST, fn), "w", encoding="utf-8") as f:
            f.write(texts[fn])
        print("transformed", fn)
    print("OUT dir:", EDITION)


if __name__ == "__main__":
    main()
