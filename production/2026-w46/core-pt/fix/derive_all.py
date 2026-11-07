# -*- coding: utf-8 -*-
"""Regenerate all 9 fixed PT editions' .text.md from the core .text.md via
hidden_files/w46/derive_textmd.py + the rebuilt build-dir transform REPL
tables. Extras (gloss prefix + 2 example sentences) are extracted from the
PRE-FIX shipped .text.md files and frozen in derive-args.json, so the run is
reproducible after the files are overwritten. F-5: zh-cn header_new is the
new Simplified-Chinese header line (all other header/sub lines are the
shipped pre-fix values, byte-preserved).

Usage: tools/venv/bin/python derive_all.py [--extract-only]
"""
import json, os, subprocess, sys

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HIDDEN = os.path.join(BASE, "hidden_files")
FIX = os.path.join(HIDDEN, "w46", "pt-fix")
ARGS_JSON = os.path.join(FIX, "derive-args.json")

HEADER_OLD = ("Semana de 9 a 15 de novembro de 2026 · Textos em português · "
              "Explicações em chinês simplificado · Níveis A2–B2 · 150 exercícios")
SUB_OLD = "# A Lucerna · 葡萄牙语周报 VOL.3"
ZH_CN_HEADER_NEW = ("2026 年 11 月 9–15 日 · 正文葡萄牙语 · 讲解简体中文 · "
                    "级别 A2–B2 · 150 道练习题")
LANGS = ["de", "en", "es", "fr", "it", "ko", "nl", "ru", "zh-cn"]


def shipped(lang):
    p = os.path.join(BASE, "files", f"weekly-report-w46-pt-{lang}",
                     f"2026-w46-pt-{lang}.text.md")
    return open(p, encoding="utf-8").read().splitlines()


def extract():
    args = {}
    for lang in LANGS:
        ls = shipped(lang)
        header_new = ZH_CN_HEADER_NEW if lang == "zh-cn" else ls[2]
        extras = []
        if lang != "zh-cn":
            # gloss prefix: shipped L98 "*<prefix>a proclamação..."
            l98 = ls[97]
            assert l98.startswith("*") and "a proclamação" in l98, (lang, l98[:60])
            prefix = l98[1:].split("a proclamação")[0]
            assert prefix != "译注｜", lang
            extras.append(["译注｜", prefix])
            # example sentences 139/140: native part before " → "
            l461, l462 = ls[460], ls[461]
            assert l461.startswith("139. ") and " → " in l461, (lang, l461[:60])
            assert l462.startswith("140. ") and " → " in l462, (lang, l462[:60])
            extras.append(["“假日落在周日。”", l461[5:].split(" → ")[0]])
            extras.append(["你到达时，请出示带照片的证件。",
                           l462[5:].split(" → ")[0]])
        args[lang] = {
            "header_new": header_new,
            "sub_new": ls[0],
            "allow_cjk": "1" if lang in ("ko", "zh-cn") else "0",
            "extras": extras,
        }
    with open(ARGS_JSON, "w", encoding="utf-8") as f:
        json.dump(args, f, ensure_ascii=False, indent=1)
    print("wrote", ARGS_JSON)
    return args


def run(args):
    core_text = os.path.join(BASE, "files", "weekly-report-w46-pt-core",
                             "2026-w46-pt-zh-cn.text.md")
    for lang in LANGS:
        a = args[lang]
        cmd = [os.path.join(BASE, "tools", "venv", "bin", "python"),
               os.path.join(HIDDEN, "w46", "derive_textmd.py"),
               os.path.join(HIDDEN, f"weekly-report-w46-pt-{lang}-build", "transform.py"),
               core_text,
               os.path.join(BASE, "files", f"weekly-report-w46-pt-{lang}",
                            f"2026-w46-pt-{lang}.text.md"),
               HEADER_OLD, a["header_new"], SUB_OLD, a["sub_new"],
               a["allow_cjk"]]
        for old, new in a["extras"]:
            cmd += [old, new]
        print("=== derive", lang, "===")
        r = subprocess.run(cmd, capture_output=True, text=True)
        print(r.stdout, end="")
        print(r.stderr, end="")
        assert r.returncode == 0, f"derive failed for {lang}"
        print("derive OK:", lang)


if __name__ == "__main__":
    if "--extract-only" in sys.argv:
        extract()
    else:
        if not os.path.exists(ARGS_JSON):
            extract()
        else:
            print("using existing", ARGS_JSON)
        run(json.load(open(ARGS_JSON, encoding="utf-8")))
