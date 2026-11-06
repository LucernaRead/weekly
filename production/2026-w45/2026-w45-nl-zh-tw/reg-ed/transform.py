# -*- coding: utf-8 -*-
"""NL x ZH-TW (W45, VOL.2) fan-out transform.

Runs ONCE on a pristine copy of the W45 NL core build
(hidden_files/weekly-report-w45-nl-build). Re-running on an already
transformed copy is refused by the OUT assertion below; fix rounds
re-copy the core, edit this file, and re-run from scratch, so the
shipped edition is always reproducible from core + this script.

Method (W43 NL x ZH-TW precedent, same column):
  1. Base script conversion of the explanation layer with OpenCC
     s2twp (tools venv ships opencc_python_reimplemented). The
     converter only touches CJK characters, so Dutch text, numbers
     and code structure are provably untouched (asserted: the
     non-CJK character stream is identical before/after).
  2. Explicit Taiwan-native fixups (phrase table below, counts
     asserted). This is the step that makes the edition a native
     Traditional text rather than a raw conversion: week words take
     週 (s2twp leaves 周), statistical data takes 數據 (s2twp gives
     資料), and every converted line is then read in full (see the
     build log) with wording corrected where Taiwan usage differs.
  3. Column furniture per the W43 NL x ZH-TW KIT §3 (badge in the
     y=372 subtitle slot, footer, P8 header/separator, gloss
     prefix, quote style, bridge -> expl rename, TC svglib face).
"""
import re
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

CORE_OUT = "workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-core/svg"
ED_OUT = "workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-zh-tw/svg"
CORE_BASE = "workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-core"
ED_BASE = "workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-zh-tw"

CONTENT = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]


def replace(path, old, new, expect=None):
    txt = open(path, encoding="utf-8").read()
    n = txt.count(old)
    if expect is not None:
        assert n == expect, f"{path}: {old!r} found {n}, expected {expect}"
    assert n >= 1, f"{path}: {old!r} not found"
    open(path, "w", encoding="utf-8").write(txt.replace(old, new))
    return n


def main():
    from opencc import OpenCC
    cc = OpenCC("s2twp")
    cjk = re.compile(r"[\u4e00-\u9fff]")

    for fn in CONTENT:
        path = os.path.join(HERE, fn)
        txt = open(path, encoding="utf-8").read()
        # Refuse to run on an already-transformed copy.
        assert CORE_OUT in txt, f"{fn} is not a pristine core copy (OUT already repointed)"
        before_noncjk = "".join(ch for ch in txt if not cjk.match(ch))
        conv = cc.convert(txt)
        after_noncjk = "".join(ch for ch in conv if not cjk.match(ch))
        assert before_noncjk == after_noncjk, f"{fn}: non-CJK stream changed by conversion"
        open(path, "w", encoding="utf-8").write(conv)
        print(f"converted {fn}")

    # ---- Taiwan-native fixups (post-conversion forms; counts asserted) ----
    # Week words take 週. s2twp leaves 周; 周圍 (surroundings) must keep 周.
    week_pairs = [
        ("周一", "週一"), ("周二", "週二"), ("周三", "週三"), ("周四", "週四"),
        ("周五", "週五"), ("周六", "週六"), ("周日", "週日"),
        ("本周", "本週"), ("下周", "下週"),
        ("氣候周", "氣候週"), ("設計周", "設計週"), ("歐戰周", "歐戰週"),
    ]
    for fn in CONTENT:
        path = os.path.join(HERE, fn)
        txt = open(path, encoding="utf-8").read()
        for old, new in week_pairs:
            if old in txt:
                print(f"  week {fn}: {old} x{txt.count(old)} -> {new}")
                txt = txt.replace(old, new)
        open(path, "w", encoding="utf-8").write(txt)
    # After the phrase fixups, the only remaining 周 must be 周圍
    # (surroundings) or the spaced P1 nameplate (fixed by furniture below).
    for fn in CONTENT:
        txt = open(os.path.join(HERE, fn), encoding="utf-8").read()
        rest = [m.start() for m in re.finditer("周", txt)]
        for pos in rest:
            assert txt[pos:pos + 2] == "周圍" or txt[pos:pos + 3] == "周 報", f"{fn}: unexpected remaining 周 at {pos}: {txt[max(0,pos-10):pos+10]!r}"
        print(f"  week residue {fn}: {len(rest)} (all 周圍 / nameplate)")

    # Statistical data takes 數據, not s2twp's 資料 (3 chart sites).
    for fn in ["content56.py"]:
        n = replace(os.path.join(HERE, fn), "練習資料", "練習數據", expect=3)
        print(f"  data fixup content56.py: {n}")

    # s2twp phrase over-corrections, found on full-diff review (2026-10-27).
    # Every 代码 here is a KNMI colour code, never software code.
    phrase_fixups = [
        ("程式碼", "代碼", 5),      # colour codes: P2 instr + 2 notes, P6 note, P7 golden gloss
        ("比賽專案", "比賽項目", 3),  # contest trials: P5 box + gloss + note
        ("報道", "報導", 1),        # Taiwan media usage: P5 box
        ("集市", "市集", 2),        # flea market: P3 gloss + note
        ("把片語成正確的句子", "把詞組成正確的句子", 1),  # s2twp mangled 把词组 + 成
    ]
    for old, new, expect in phrase_fixups:
        found = 0
        for fn in CONTENT:
            path = os.path.join(HERE, fn)
            txt = open(path, encoding="utf-8").read()
            c = txt.count(old)
            if c:
                open(path, "w", encoding="utf-8").write(txt.replace(old, new))
                print(f"  phrase {fn}: {old} x{c} -> {new}")
                found += c
        assert found == expect, f"phrase fixup {old}: found {found}, expected {expect}"

    # ---- OUT repoint (expanduser form, README #11) ----
    for fn in CONTENT:
        replace(os.path.join(HERE, fn),
                f"os.path.expanduser(\"~/{CORE_OUT}\")",
                f"os.path.expanduser(\"~/{ED_OUT}\")", expect=1)
    rp = os.path.join(HERE, "render.py")
    replace(rp, f"os.path.expanduser(\"~/{CORE_BASE}\")",
            f"os.path.expanduser(\"~/{ED_BASE}\")", expect=1)
    replace(rp, "\"De-Lucerna-VOL2.pdf\"", "\"De-Lucerna-VOL2-ZHTW.pdf\"", expect=1)
    replace(rp, "\"De-Lucerna-VOL2-web.pdf\"", "\"De-Lucerna-VOL2-ZHTW-web.pdf\"", expect=1)

    # ---- bslib4: footer, bridge -> expl, gloss prefix ----
    bp = os.path.join(HERE, "bslib4.py")
    # bslib4 is NOT OpenCC-converted (only the content modules are), so
    # its old strings are still in Simplified form here.
    replace(bp, "De Lucerna · 荷兰语周报 VOL.2 · LUCERNA DUTCH WEEKLY",
            "De Lucerna · 荷語週報 VOL.2 · 正文荷語 · 講解繁體中文", expect=1)
    replace(bp, "def bridge(self, s, size=20.5, gap=9, fill=GREY):",
            "def expl(self, s, size=20.5, gap=9, fill=GREY):", expect=1)
    replace(bp, "译注｜", "譯注｜", expect=1)
    txt = open(bp, encoding="utf-8").read()
    assert txt.count("譯注｜") == 1, "gloss prefix count != 1"
    assert "bridge" not in txt, "bslib4 still mentions bridge"

    # ---- content call sites: .bridge( -> .expl( (22 sites) ----
    total = 0
    for fn in CONTENT:
        path = os.path.join(HERE, fn)
        txt = open(path, encoding="utf-8").read()
        n = txt.count(".bridge(")
        total += n
        open(path, "w", encoding="utf-8").write(txt.replace(".bridge(", ".expl("))
        print(f"  expl rename {fn}: {n}")
    assert total == 22, f".bridge( call sites = {total}, expected 22"

    # ---- P1 furniture (W43 NL x ZH-TW §3, NL family subtitle-slot case) ----
    c12 = os.path.join(HERE, "content12.py")
    # Note: the spaced nameplate's 周 is NOT touched by the week fixups
    # (it is followed by a space, not a weekday character), so the old
    # form here still carries 周.
    replace(c12, "荷 蘭 語 周 報 · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12",
            "荷 語 週 報 · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12", expect=1)
    replace(c12,
            'p.text(975, 372, "DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS", 19, "sans", False, GREY, anchor="middle")',
            'p.text(975, 372, "荷語正文 · 繁體中文講解 — 給繁體中文讀者的版本", 19.5, "sans", True, BRICK, anchor="middle")',
            expect=1)

    # ---- Quote style: explanation-layer “” -> 「」 (1 site, P1 word box) ----
    n = 0
    for fn in CONTENT:
        path = os.path.join(HERE, fn)
        txt = open(path, encoding="utf-8").read()
        n += txt.count("“") + txt.count("”")
    assert n == 2, f"curly-quote chars = {n}, expected 2 (one pair)"
    replace(c12, "“氣候”", "「氣候」", expect=1)

    # ---- P8 furniture (W43 column precedent) ----
    c8 = os.path.join(HERE, "content8.py")
    replace(c8, "ANTWOORDEN · 參考答案 — 按版面分頁排列，找到題號即可",
            "ANTWOORDEN · 全部答案與簡析（第 1–8 版）", expect=1)
    replace(c8, 'af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
            'af.para(f"— 第 {pg} 版 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
            expect=1)

    # ---- svglib: the 4 TC-face lines (W43 / EN x ZH-TW §2) ----
    sp = os.path.join(HERE, "svglib.py")
    replace(sp, "def _sc_index(path):", "def _tc_index(path):", expect=1)
    replace(sp, 'if f.getname()[0].endswith("SC"):', 'if f.getname()[0].endswith("TC"):', expect=1)
    replace(sp, "_IDX = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}",
            "_IDX = {p: _tc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}", expect=1)
    replace(sp, 'fam = family or ("Noto Serif CJK SC" if kind == "serif" else "Noto Sans CJK SC")',
            'fam = family or ("Noto Serif CJK TC" if kind == "serif" else "Noto Sans CJK TC")', expect=1)

    # ---- Final guards ----
    for fn in CONTENT + ["bslib4.py", "svglib.py"]:
        txt = open(os.path.join(HERE, fn), encoding="utf-8").read()
        assert ".bridge(" not in txt and "bridge" not in txt, f"{fn} still has bridge"
        assert "桥接" not in txt, f"{fn} has 桥接"
    print("transform OK")


if __name__ == "__main__":
    main()
