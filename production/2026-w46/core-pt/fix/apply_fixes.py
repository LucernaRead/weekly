# -*- coding: utf-8 -*-
"""Apply Round 1 proofreader fixes F-1/F-2/F-3 to the PT fan-out transform.py
sources (staged copies under hidden_files/w46/pt-fix/stage/). Never edits a
shipped SVG/PDF/.text.md directly. Live build dirs are rebuilt from pristine
core copies + these staged transforms; this script only produces the staged
transforms. Run: tools/venv/bin/python apply_fixes.py ; asserts on every edit.
"""
import ast, os, re, shutil, sys

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HIDDEN = os.path.join(BASE, "hidden_files")
STAGE = os.path.join(HIDDEN, "w46", "pt-fix", "stage")
FW_COLON = "\uff1a"   # ：
FW_STOP = "\u3002"    # 。
CLINIC_OLD = "假日落在周日，周一不补休"
TIMETABLE_OLD = "迟到不得入内：13 点后关门"

F1 = [  # (file, old, new) — 10 pure-Portuguese P8 note strings, Round 1 F-1
    ("content12.py", "conferir：ele → confere", "conferir: ele → confere"),
    ("content12.py", "abrir：ele → abre", "abrir: ele → abre"),
    ("content12.py", "levar：nós → levamos", "levar: nós → levamos"),
    ("content12.py", "começar：ela → começa", "começar: ela → começa"),
    ("content12.py", "terminar：ela → termina", "terminar: ela → termina"),
    ("content34.py", "2 > 0：mais", "2 > 0: mais"),
    ("content34.py", "3 > 2：mais", "3 > 2: mais"),
    ("content34.py", "17 < 18：mais cedo", "17 < 18: mais cedo"),
    ("content7.py", "conferir：você → confere", "conferir: você → confere"),
    ("content7.py", "terminar：ela → termina", "terminar: ela → termina"),
]

F1_BLOCK = '''
# ---------- 5c. FIX F-1 (Round 1 proofread): fullwidth colon in P8 notes ----------
# The 10 note strings below are pure Portuguese (no CJK gloss) inherited from
# the core register with U+FF1A (：). In Latin-script editions they must use
# an ASCII colon, matching neighbouring notes (e.g. item 101). CJK editions
# (ja/zh-cn/zh-tw) legitimately keep ： inside CJK glosses, so this block is
# present ONLY in the 8 Latin-script transforms. Runs after the REPL loop.
for _fn, _old, _new in [
    ("content12.py", "conferir：ele → confere", "conferir: ele → confere"),
    ("content12.py", "abrir：ele → abre", "abrir: ele → abre"),
    ("content12.py", "levar：nós → levamos", "levar: nós → levamos"),
    ("content12.py", "começar：ela → começa", "começar: ela → começa"),
    ("content12.py", "terminar：ela → termina", "terminar: ela → termina"),
    ("content34.py", "2 > 0：mais", "2 > 0: mais"),
    ("content34.py", "3 > 2：mais", "3 > 2: mais"),
    ("content34.py", "17 < 18：mais cedo", "17 < 18: mais cedo"),
    ("content7.py", "conferir：você → confere", "conferir: você → confere"),
    ("content7.py", "terminar：ela → termina", "terminar: ela → termina"),
]:
    _t = load(_fn)
    _t = sub(_t, _old, _new, _fn)
    save(_fn, _t)
'''

CLINIC_NEW = {
    "de": "Der Feiertag fällt auf einen Sonntag, montags gibt es keinen Ausgleich",
    "en": "The holiday falls on a Sunday, with no Monday off",
    "es": "El festivo cae en domingo, el lunes no se recupera",
    "fr": "Le jour férié tombe un dimanche, pas de récupération le lundi",
    "it": "La festa cade di domenica, il lunedì non si recupera",
    "nl": "De feestdag valt op zondag, maandag geen inhaal",
    "ru": "Праздник выпадает на воскресенье, в понедельник выходного нет",
    "ko": "공휴일이 일요일에 겹쳐도 월요일에 쉬지 않아요",
}

LATIN8 = ["de", "en", "es", "fr", "it", "ko", "nl", "ru"]
F2 = ["de", "en", "es", "fr", "it", "nl", "ru"]  # + ko gets clinic-only fix (F-3)


def repl_entries(transform_path):
    tree = ast.parse(open(transform_path, encoding="utf-8").read())
    repl = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "REPL":
            repl.extend(ast.literal_eval(node.value))
        elif isinstance(node, ast.AugAssign) and getattr(node.target, "id", "") == "REPL":
            repl.extend(ast.literal_eval(node.value))
    return repl


def stage_transform(lang):
    src = os.path.join(HIDDEN, f"weekly-report-w46-pt-{lang}-build", "transform.py")
    dst_dir = os.path.join(STAGE, lang)
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, "transform.py")
    shutil.copyfile(src, dst)
    # preserve gates.py alongside for the rebuild
    shutil.copyfile(
        os.path.join(HIDDEN, f"weekly-report-w46-pt-{lang}-build", "gates.py"),
        os.path.join(dst_dir, "gates.py"))
    return dst


def fix_f1(path):
    txt = open(path, encoding="utf-8").read()
    # guard: no REPL old string may already contain an F-1 literal
    for old, _new in repl_entries(path):
        for _fn, lit, _n in F1:
            assert lit not in old, f"REPL collision: {lit!r} inside {old[:60]!r}"
    m = re.search(r"^# -+ 6\..*$", txt, re.M)
    assert m, "section 6 marker not found"
    txt = txt[:m.start()] + F1_BLOCK.lstrip("\n") + "\n" + txt[m.start():]
    open(path, "w", encoding="utf-8").write(txt)
    print(f"F-1 block inserted: {path}")


def fix_clinic(path, lang):
    """ADD a second REPL entry carrying the trailing 。 (F-2/F-3).

    The bare entry MUST stay: the same Chinese gloss (without 。) is also
    the note of the P2 exercise (content12) and its P8 answer (content8),
    where the translation correctly takes no trailing period. The 。-carrying
    entry (longest-first) consumes the 。 only in the P7 clinic tuple
    (content7) and in the .text.md clinic line, emitting translation + '.'.
    Replacing the bare entry instead would leave CJK in content12/content8
    and fail the §6 zero-CJK assert (found during the en rebuild)."""
    lines = open(path, encoding="utf-8").read().split("\n")
    hits = [i for i, ln in enumerate(lines)
            if f"('{CLINIC_OLD}'," in ln and "2026" not in ln and "“假日" not in ln]
    assert len(hits) == 1, f"{lang}: clinic line hits {hits}"
    i = hits[0]
    ln = lines[i]
    mm = re.match(r"^(\s*\('" + CLINIC_OLD + r"', ')(.*)('\s*\),\s*)$", ln)
    assert mm, f"{lang}: clinic line did not parse: {ln!r}"
    assert "'" not in mm.group(2), f"{lang}: apostrophe in clinic translation"
    assert mm.group(2) == CLINIC_NEW[lang], \
        f"{lang}: clinic translation mismatch: {mm.group(2)!r}"
    indent = ln[:len(ln) - len(ln.lstrip())]
    new_line = (indent + "('" + CLINIC_OLD + FW_STOP + "', '"
                + mm.group(2) + ".')" + ",")
    comment = (indent + "# P7-clinic/.text.md variant of the line above: the "
               "source carries a trailing 。 (F-2/F-3).")
    lines[i + 1:i + 1] = [comment, new_line]
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    print(f"F-2/F-3 clinic entry added ({lang}): ...{CLINIC_OLD}{FW_STOP} -> ...{CLINIC_NEW[lang]}.")


def fix_timetable(path, lang):
    """Add a second REPL entry whose old string carries the trailing 。
    (the .text.md source line ends with 。; the SVG source line does not).
    Longest-first REPL order applies the 。-carrying entry in .text.md and
    the bare entry in SVG sources (where the new entry only WARNs)."""
    lines = open(path, encoding="utf-8").read().split("\n")
    hits = [i for i, ln in enumerate(lines) if f"('{TIMETABLE_OLD}'," in ln]
    assert len(hits) == 1, f"{lang}: timetable line hits {hits}"
    i = hits[0]
    indent = lines[i][:len(lines[i]) - len(lines[i].lstrip())]
    new_line = lines[i].replace(f"'{TIMETABLE_OLD}',", f"'{TIMETABLE_OLD}{FW_STOP}',", 1)
    assert new_line != lines[i]
    comment = (indent + "# .text.md variant of the line above: the export source "
               "carries a trailing 。 which the bare entry leaves behind (F-2).")
    lines[i + 1:i + 1] = [comment, new_line]
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    print(f"F-2 timetable .text.md entry added ({lang})")


def main():
    for lang in LATIN8:
        p = stage_transform(lang)
        fix_f1(p)
    for lang in F2 + ["ko"]:
        fix_clinic(os.path.join(STAGE, lang, "transform.py"), lang)
    for lang in F2:
        fix_timetable(os.path.join(STAGE, lang, "transform.py"), lang)
    print("ALL STAGED TRANSFORMS WRITTEN")


if __name__ == "__main__":
    main()
