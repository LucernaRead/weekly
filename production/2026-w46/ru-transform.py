# -*- coding: utf-8 -*-
"""RU fan-out transform: copy the W46 RU core build, rewrite ONLY the explanation
layer (Simplified Chinese -> reader language) via an ordered substring map,
repoint OUT/render paths, apply per-language furniture + badge + P8 separator,
optionally swap svglib (JA/TC faces). Never run inside the core build dir.

Usage: ru-transform.py <native>   (maps live in ru_maps.py next to this file)
"""
import sys, os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE_BUILD = os.path.join(GOAL, "hidden_files/weekly-report-w46-ru-build")
sys.path.insert(0, HERE)
import ru_maps as maps

CJK = re.compile(r"[\u2e80-\u9fff\uac00-\ud7a3\u3040-\u30ff]")
CYR = re.compile(r"[А-Яа-яЁё]+")

def cyr_seqs(s):
    return sorted(CYR.findall(s))

def main():
    native = sys.argv[1]
    spec = maps.SPECS[native]
    dest = os.path.join(GOAL, f"hidden_files/weekly-report-w46-ru-{native}-build")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(CORE_BUILD, dest, ignore=shutil.ignore_patterns("__pycache__", "dump_cjk.py", "check_core.py"))
    if spec.get("svglib_from"):
        src = os.path.join(GOAL, f"hidden_files/{spec['svglib_from']}/svglib.py")
        shutil.copyfile(src, os.path.join(dest, "svglib.py"))
        print("svglib copied from", spec["svglib_from"])

    files = ["bslib4.py", "content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "render.py"]
    before = {}
    for fn in files:
        p = os.path.join(dest, fn)
        before[fn] = open(p, encoding="utf-8").read()

    ed_dir = f"weekly-report-w46-ru-{native}"
    for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        p = os.path.join(dest, fn)
        t = open(p, encoding="utf-8").read()
        t = t.replace("files/weekly-report-w46-ru-core/svg", f"files/{ed_dir}/svg")
        assert "w46-ru-core" not in t, fn
        open(p, "w", encoding="utf-8").write(t)
        before[fn] = t
    rp = os.path.join(dest, "render.py")
    t = open(rp, encoding="utf-8").read()
    t = t.replace("files/weekly-report-w46-ru-core", f"files/{ed_dir}")
    t = t.replace("Lucerna-VOL3.pdf", f"Lucerna-VOL3-{spec['suffix']}.pdf")
    open(rp, "w", encoding="utf-8").write(t)

    bp = os.path.join(dest, "bslib4.py")
    t = open(bp, encoding="utf-8").read()
    old_foot_l = '        self.text(MX, 2624, "Lucerna · 俄语周报 VOL.3 · LUCERNA RUSSIAN WEEKLY", 20, "sans", False, GREY)'
    assert old_foot_l in t
    t = t.replace(old_foot_l, f'        self.text(MX, 2624, "{spec["footer"]}", 20, "sans", False, GREY)')
    old_foot_r = '        self.text(RIGHT, 2624, f"第 {n} 版 / 共 {total} 版", 20, "sans", False, GREY, anchor="end")'
    assert old_foot_r in t
    t = t.replace(old_foot_r, f'        self.text(RIGHT, 2624, f"{spec["page_line"]}", 20, "sans", False, GREY, anchor="end")')
    assert '"译注｜" + s' in t
    t = t.replace('"译注｜" + s', f'"{spec["gloss_prefix"]}" + s')
    open(bp, "w", encoding="utf-8").write(t)
    before["bslib4.py"] = t

    cp = os.path.join(dest, "content12.py")
    t = open(cp, encoding="utf-8").read()
    sub_line = 'p.text(975, 372, "ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ", 19, "sans", False, GREY, anchor="middle")'
    assert sub_line in t
    if spec["badge_mode"] == "replace":
        t = t.replace(sub_line, f'p.text(975, 372, "{spec["badge"]}", {spec["badge_size"]}, "sans", True, {spec["badge_color"]}, anchor="middle")')
    else:
        badge_line = (f'# W45 shipped same-pairing badge slot (975, 574), 22pt BRICK\n'
                      f'p.text(975, 574, "{spec["badge"]}", 22, "sans", True, BRICK, anchor="middle")')
        t = t.replace(sub_line, sub_line + "\n" + badge_line)
    open(cp, "w", encoding="utf-8").write(t)

    c8 = os.path.join(dest, "content8.py")
    t = open(c8, encoding="utf-8").read()
    old_sep = 'af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)'
    assert old_sep in t
    if spec.get("p8_separator"):
        t = t.replace(old_sep, f'af.para(f"{spec["p8_separator"]}", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)')
    open(c8, "w", encoding="utf-8").write(t)

    cmap = sorted(spec["map"], key=lambda e: -len(e[0]))
    stats = {}
    seen = set()
    for entry in cmap:
        old = entry[0]
        if old in seen and len(entry) != 3:
            continue
        seen.add(old)
        if len(entry) == 2 and entry[0] == entry[1]:
            continue  # identity entry (same glyphs in both scripts): no-op by design
        if len(entry) == 3:
            new_list, only_file = entry[1], entry[2]
            p = os.path.join(dest, only_file)
            t = open(p, encoding="utf-8").read()
            parts = t.split(old)
            assert len(parts) - 1 == len(new_list), (only_file, old, len(parts) - 1, len(new_list))
            out = parts[0]
            for new, part in zip(new_list, parts[1:]):
                out += new + part
            open(p, "w", encoding="utf-8").write(out)
            stats[old] = len(new_list)
            continue
        new = entry[1]
        total = 0
        for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:
            p = os.path.join(dest, fn)
            t = open(p, encoding="utf-8").read()
            n = t.count(old)
            if n:
                t = t.replace(old, new)
                open(p, "w", encoding="utf-8").write(t)
                total += n
        assert total >= 1, f"MAP KEY NEVER FOUND: {old!r}"
        stats[old] = total
    print(f"map: {len(cmap)} keys, {sum(stats.values())} replacements")

    for fn in files:
        p = os.path.join(dest, fn)
        t = open(p, encoding="utf-8").read()
        for entry in cmap:
            if len(entry) == 2 and entry[0] == entry[1]:
                continue
            assert entry[0] not in t, (fn, entry[0])

    # Cyrillic preservation: a changed line may only gain/lose Cyrillic
    # sequences that occur inside a map key / replacement (mixed gloss notes
    # like "можно + 不定式" legitimately translate the Russian word too).
    from collections import Counter
    allowed_removed, allowed_added = set(), set()
    for entry in cmap:
        allowed_removed.update(cyr_seqs(entry[0]))
        if len(entry) == 2:
            allowed_added.update(cyr_seqs(entry[1]))
        else:
            for nv in entry[1]:
                allowed_added.update(cyr_seqs(nv))
    def whitelisted(line):
        return ("2624" in line or "975, 372" in line or "975, 574" in line
                or "СТРАНИЦА" in line or "Pagina" in line or "ページ" in line
                or "p.band(" in line
                or ("af.para" in line and ("제 " in line or "第 " in line)))
    for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:
        old_lines = before[fn].splitlines()
        new_lines = open(os.path.join(dest, fn), encoding="utf-8").read().splitlines()
        if fn == "content12.py" and spec["badge_mode"] == "insert":
            new_lines = [ln for ln in new_lines
                         if not ln.startswith("# W45 shipped same-pairing badge slot")
                         and "975, 574" not in ln]
        assert len(old_lines) == len(new_lines), (fn, len(old_lines), len(new_lines))
        for o, n in zip(old_lines, new_lines):
            if o == n:
                continue
            if whitelisted(o) or whitelisted(n):
                continue
            removed = Counter(cyr_seqs(o)) - Counter(cyr_seqs(n))
            added = Counter(cyr_seqs(n)) - Counter(cyr_seqs(o))
            assert set(removed) <= allowed_removed, (fn, o, "||", n, dict(removed))
            assert set(added) <= allowed_added, (fn, o, "||", n, dict(added))

    if spec.get("no_cjk"):
        for fn in files:
            t = open(os.path.join(dest, fn), encoding="utf-8").read()
            m = CJK.search(t)
            assert not m, (fn, t[max(0, m.start() - 40):m.start() + 40])
        print("no-CJK check: clean")

    os.makedirs(os.path.join(GOAL, f"files/{ed_dir}/svg"), exist_ok=True)
    print("BUILD DIR READY:", dest)
    print("EDITION DIR:", os.path.join(GOAL, f"files/{ed_dir}"))

if __name__ == "__main__":
    main()
