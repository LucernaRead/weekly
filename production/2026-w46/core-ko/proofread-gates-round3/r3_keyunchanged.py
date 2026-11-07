#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round 3 independent key-unchanged proof.
Runs tools/p8.py extract FRESH (tools venv) for every edition on the CURRENT
P8 SVGs, then compares each edition's full key dict + noted set against the
pre-fix snapshot JSONs in ko-fix-round3/pre-fix/p8keys/ — reading the JSON
contents directly (including each file's own 'p8' path field), not any
summary. Prints every differing number explicitly; exit 1 if any differ."""
import json, os, subprocess, sys
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
R3 = os.path.join(GOAL, "hidden_files", "w46", "ko-proofread-gates-round3")
PRE = os.path.join(GOAL, "hidden_files", "w46", "ko-fix-round3", "pre-fix", "p8keys")
EDITIONS = {"zh-cn": "weekly-report-w46-ko-core", "de": "weekly-report-w46-ko-de",
            "en": "weekly-report-w46-ko-en", "es": "weekly-report-w46-ko-es",
            "fr": "weekly-report-w46-ko-fr", "it": "weekly-report-w46-ko-it",
            "ja": "weekly-report-w46-ko-ja", "nl": "weekly-report-w46-ko-nl",
            "pt": "weekly-report-w46-ko-pt", "ru": "weekly-report-w46-ko-ru",
            "zh-tw": "weekly-report-w46-ko-zh-tw"}
os.makedirs(os.path.join(R3, "p8keys-now"), exist_ok=True)
PY = os.path.join(GOAL, "tools", "venv", "bin", "python")
overall_ok = True
results = {}
for code, d in EDITIONS.items():
    p8 = os.path.join(GOAL, "files", d, "svg", "p8-siheom.svg")
    outj = os.path.join(R3, "p8keys-now", code + ".json")
    r = subprocess.run([PY, "p8.py", "extract", "--p8", p8, "--total", "150",
                        "--json", outj], cwd=os.path.join(GOAL, "tools"),
                       capture_output=True, text=True)
    print(code, "p8 extract exit", r.returncode, r.stdout.strip()[:200], r.stderr.strip()[:200])
    now = json.load(open(outj, encoding="utf-8"))
    pre = json.load(open(os.path.join(PRE, code + ".json"), encoding="utf-8"))
    print("   pre p8 field:", pre["p8"], "| now p8 field:", now["p8"])
    print("   pre total/how:", pre["total"], pre["how"], "| now:", now["total"], now["how"])
    diffs = [n for n in pre["keys"] if pre["keys"][n] != now["keys"].get(n)]
    extra = [n for n in now["keys"] if n not in pre["keys"]]
    set_same = pre["noted_set"] == now["noted_set"]
    print("   keys identical:", not diffs and not extra,
          "| diff numbers:", diffs, "| extra:", extra,
          "| noted_set identical:", set_same,
          "| key54:", now["keys"].get("54"), "| key103:", now["keys"].get("103"))
    results[code] = {"diffs": diffs, "extra": extra, "noted_set_same": set_same,
                     "key54": now["keys"].get("54"), "key103": now["keys"].get("103"),
                     "pre_p8": pre["p8"], "now_p8": now["p8"]}
    if diffs or extra or not set_same:
        overall_ok = False
json.dump(results, open(os.path.join(R3, "key-unchanged.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("KEY-UNCHANGED OVERALL:", "PASS" if overall_ok else "FAIL")
sys.exit(0 if overall_ok else 1)
