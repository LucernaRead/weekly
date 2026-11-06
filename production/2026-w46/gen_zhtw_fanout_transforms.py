#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate W46 zh-tw x {ja,ko,ru} transform scripts from the NL pair order
plus zhtw-translations{,-b,-c,-d}.json. Furniture per W45 precedent.
Re-run after editing translations; then re-copy the core build, apply,
run.py, render.py."""
import importlib.util, json, os

G = "/home/hatch/workspace/goals/lucernaread-social-media-operations"

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.PAIRS

nl = load("t_nl", f"{G}/hidden_files/w46-zh-tw-nl-transform.py")[:254]
tr = {}
for f in ["zhtw-translations.json", "zhtw-translations-b.json",
          "zhtw-translations-c.json", "zhtw-translations-d.json",
          "zhtw-translations-e.json"]:
    tr.update(json.load(open(f"{G}/hidden_files/w46/{f}", encoding="utf-8")))
FURN = {
 "ja": {"footer": "Lucerna · 中国語（繁体字）週刊 VOL.3 · 本文は中国語（繁体字） · 解説は日本語",
        "pageline": "{n} ページ（全 {total} ページ）", "gloss": "解説 — ",
        "badge": "中国語（繁体字）テキスト · 日本語の解説 — 日本語読者のための版",
        "sep": "— {pg} ページ —", "suffix": "JA"},
 "ko": {"footer": "Lucerna · 중국어 번체 주간지 VOL.3 · 텍스트는 중국어 번체 · 해설은 한국어",
        "pageline": "제 {n} 면 / 총 {total} 면", "gloss": "해설 — ",
        "badge": "중국어 번체 텍스트 · 한국어 해설 — 한국어 독자를 위한 판",
        "sep": "— 제 {pg} 면 —", "suffix": "KO"},
 "ru": {"footer": "Lucerna · КИТАЙСКИЙ (ТРАДИЦИОННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА КИТАЙСКОМ (ТРАДИЦИОННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ",
        "pageline": "Страница {n} из {total}", "gloss": "Пояснение — ",
        "badge": "ТЕКСТЫ НА КИТАЙСКОМ (ТРАДИЦИОННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ",
        "sep": "— СТРАНИЦА {pg} —", "suffix": "RU"},
}
CORE = "weekly-report-w46-zhtw-core"
for lang in ["ja", "ko", "ru"]:
    ed = f"weekly-report-w46-zh-tw-{lang}"
    f = FURN[lang]; suf = f["suffix"]
    pairs = []
    for i, (old, new) in enumerate(nl):
        if i == 0:
            pairs.append((f"~/workspace/goals/lucernaread-social-media-operations/files/{CORE}/svg",
                          f"~/workspace/goals/lucernaread-social-media-operations/files/{ed}/svg"))
        elif i == 1:
            pairs.append((f"~/workspace/goals/lucernaread-social-media-operations/files/{CORE}\"",
                          f"~/workspace/goals/lucernaread-social-media-operations/files/{ed}\""))
        elif i == 2:
            pairs.append(("Lucerna-VOL3.pdf", f"Lucerna-VOL3-{suf}.pdf"))
        elif i == 3:
            pairs.append(("Lucerna-VOL3-web.pdf", f"Lucerna-VOL3-{suf}-web.pdf"))
        elif i == 4:
            pairs.append((old, f["footer"]))
        elif i == 5:
            pairs.append((old, f["pageline"]))
        elif i == 6:
            pairs.append((old, f["gloss"]))
        elif i == 7:
            pairs.append((old, f["badge"]))
        elif i == 252:
            pairs.append((old, f["sep"]))
        elif i == 253:
            pairs.append((old, new))
        else:
            pairs.append((old, tr[str(i)][lang]))
    assert len(pairs) == 254, len(pairs)
    # fix 1: P5 practice-numbers glossline missed by every W46 zh-tw transform
    pairs.append(("Practice numbers: NT$450 + NT$1,550 = NT$2,000, exactly his budget.",
                  tr["254"][lang]))
    assert len(pairs) == 255, len(pairs)
    out = ["# -*- coding: utf-8 -*-",
           f'"""Transform W46 zh-tw CORE (English explanations) -> zh-tw x {lang.upper()} fan-out.',
           "Whole-string literal pairs only, in the W46 zh-tw x NL pair order (long/specific",
           "strings before their substrings: heads/glosslines before bare instr words).",
           "DASH family: core P8 answer-generation code unchanged. Furniture strings follow",
           "the W45 zh-tw x " + lang + " precedent (badge y=378, 21pt, OLIVE, in-place).",
           "Geometry pair (letters-box padding +14) pre-applied per the DE lesson.",
           f'Run from the fan-out build dir: python3 ../w46-zh-tw-{lang}-transform.py"""',
           "import glob, sys", "", f'ED = "{ed}"', f'CORE = "{CORE}"',
           'ROOT = "~/workspace/goals/lucernaread-social-media-operations/files/"', "", "PAIRS = ["]
    for o, n in pairs:
        out.append(f"    ({o!r}, {n!r}),")
    out += ["]", "",
            "def main():",
            '    files = sorted(glob.glob("*.py"))',
            "    missed = []",
            "    for old, new in PAIRS:",
            "        total = 0",
            "        for f in files:",
            '            s = open(f, encoding="utf-8").read()',
            "            n = s.count(old)",
            "            if n:",
            "                total += n",
            '                open(f, "w", encoding="utf-8").write(s.replace(old, new))',
            "        if total == 0:",
            "            missed.append(old)",
            "        else:",
            '            print(f"{total:3d}  {old[:70]!r}")',
            "    if missed:",
            '        print("\\nMISSED PAIRS (0 matches) — TRANSFORM FAILED:")',
            "        for m in missed:",
            '            print("  ", repr(m))',
            "        sys.exit(1)",
            '    print("\\nTRANSFORM OK:", len(PAIRS), "pairs applied")',
            "", 'if __name__ == "__main__":', "    main()", ""]
    open(f"{G}/hidden_files/w46-zh-tw-{lang}-transform.py", "w", encoding="utf-8").write("\n".join(out))
    print(lang, "wrote", len(pairs))
