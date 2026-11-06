# -*- coding: utf-8 -*-
"""Generate a W46 DE fan-out transform.py from the EN pair table + a
per-language translation dict keyed by the EN new-string.
Usage: gen_transform.py <lang-code>  (reads tr-<code>.py in this dir)
Emits: transform-<code>.py in this dir.
"""
import ast, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = sys.argv[1]
pairs = json.load(open(os.path.join(HERE, "en-pairs.json"), encoding="utf-8"))
# pairs: [listname, old, en_new]
ns = {}
exec(open(os.path.join(HERE, f"tr-{CODE}.py"), encoding="utf-8").read(), ns)
TR = ns["TR"]
CFG = ns["CFG"]

missing = sorted({en for _, _, en in pairs if en not in TR})
assert not missing, f"missing translations for {CODE}: {missing[:10]} ({len(missing)})"
extra = sorted(set(TR) - {en for _, _, en in pairs})
assert not extra, f"extra dict keys for {CODE}: {extra[:10]}"

lists = {}
for name, old, en in pairs:
    lists.setdefault(name, []).append((old, TR[en]))

def fmt_pairs(plist):
    out = []
    for old, new in plist:
        out.append(f"    ({old!r}, {new!r}),")
    return "\n".join(out)

body = []
body.append('# -*- coding: utf-8 -*-')
body.append(f'"""DE x {CODE.upper()} fan-out transform for W46 DE core build copy.')
body.append('Generated from the EN pair table + tr-%s.py. German body text is' % CODE)
body.append('NEVER touched: every `old` is a Chinese explanation-layer string,')
body.append('a bilingual furniture string, or a generic type/instr token.')
body.append('Run once from the build dir copy."""')
body.append("import os")
body.append("")
body.append("BASE = os.path.dirname(os.path.abspath(__file__))")
body.append("LOG = []")
body.append("")
body.append("def rep(fname, old, new, expect=None):")
body.append("    p = os.path.join(BASE, fname)")
body.append('    s = open(p, encoding="utf-8").read()')
body.append("    n = s.count(old)")
body.append("    if expect is not None:")
body.append('        assert n == expect, f"{fname}: {old!r} count {n} != {expect}"')
body.append("    else:")
body.append('        assert n >= 1, f"{fname}: {old!r} not found"')
body.append('    LOG.append(f"{fname}: {n}x {old[:60]!r} -> {new[:60]!r}")')
body.append('    open(p, "w", encoding="utf-8").write(s.replace(old, new))')
body.append("")
body.append("def rep_all(fname, pairs):")
body.append("    seen = set()")
body.append("    for old, new in pairs:")
body.append('        assert old not in seen, f"duplicate old in {fname}: {old!r}"')
body.append("        seen.add(old)")
body.append("    for old, new in sorted(pairs, key=lambda t: -len(t[0])):")
body.append("        rep(fname, old, new)")
body.append("")
body.append("# ---------- OUT repoint (1 per content file) ----------")
body.append('for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:')
body.append(f'    rep(f, "weekly-report-w46-de-core", "weekly-report-w46-de-{CODE}", 1)')
body.append("")
body.append("# ---------- svglib docstring comment only (not rendered) ----------")
body.append("pth = os.path.join(BASE, \"svglib.py\")")
body.append('s = open(pth, encoding="utf-8").read()')
body.append('if "for \\u91cd\\u9633." in s:')
body.append('    rep("svglib.py", "for \\u91cd\\u9633.", "for Double Ninth.", 1)')
body.append("else:")
body.append('    LOG.append("svglib.py: no Double Ninth comment (already adapted), skipped")')
body.append("")
body.append("# ---------- bslib4: furniture + gloss prefix ----------")
body.append("rep(\"bslib4.py\",")
body.append('    \'"Die Lucerna · \\u5fb7\\u8bed\\u5468\\u62a5 VOL.3 · LUCERNA GERMAN WEEKLY"\',')
body.append(f"    {CFG['footer']!r}, 1)")
body.append(f"rep(\"bslib4.py\", 'f\"\\u7b2c {{n}} \\u7248 / \\u5171 {{total}} \\u7248\"', {CFG['pageline']!r}, 1)")
body.append(f"rep(\"bslib4.py\", '\"\\u8bd1\\u6ce8\\uff5c\" + s', {CFG['gloss_prefix']!r}, 1)")
body.append("")
for name in ["C12", "C34", "C56", "C7", "C8"]:
    fname = {"C12": "content12.py", "C34": "content34.py", "C56": "content56.py",
             "C7": "content7.py", "C8": "content8.py"}[name]
    body.append(f"# ================= {fname} =================")
    body.append(f"{name} = [")
    body.append(fmt_pairs(lists[name]))
    body.append("]")
    body.append(f'rep_all("{fname}", {name})')
    body.append("")
body.append("# ---------- P8 keys ----------")
if CFG.get("separator") is not None:
    body.append("rep(\"content8.py\", 'kf.para(f\"— \\u7b2c {pg} \\u7248 —\", 17, \"sans\", True, OLIVE, 1.28, 3)',")
    body.append(f"    'kf.para(f\"{CFG['separator']}\", 17, \"sans\", True, OLIVE, 1.28, 3)', 1)")
bracket_new = CFG["bracket"]
bracket_code = 's += f"' + bracket_new + '"'
body.append("rep(\"content8.py\", 's += f\"\\uff08{e[\\'note\\']}\\uff09\"',")
body.append(f"    {bracket_code!r}, 1)")
if CFG.get("keys_size") is not None:
    size, lh = CFG["keys_size"]
    body.append("rep(\"content8.py\", 'kf.para(\" · \".join(parts), 14.5, \"sans\", False, INK, 1.3, 9)',")
    body.append(f"    'kf.para(\" · \".join(parts), {size}, \"sans\", False, INK, {lh}, 9)', 1)")
body.append("")
body.append("# ---------- generic value maps ----------")
body.append(f"TYPEMAP = {CFG['typemap']!r}")
body.append(f"INSTRMAP = {CFG['instrmap']!r}")
body.append('for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:')
body.append("    for old, new in INSTRMAP + TYPEMAP:")
body.append("        pth = os.path.join(BASE, f)")
body.append('        n = open(pth, encoding="utf-8").read().count(old)')
body.append("        if n == 0:")
body.append('            LOG.append(f"{f}: 0x {old!r} (absent, skipped)")')
body.append("        else:")
body.append("            rep(f, old, new)")
body.append("")
body.append("# ---------- leak check: no original Chinese literal may remain ----------")
body.append("import re")
if CFG.get("cjk_scan"):
    body.append("CJK = re.compile(r\"[\\u2e80-\\u9fff\\u3040-\\u30ff\\uac00-\\ud7af\\uff00-\\uffef]\")")
    body.append("leaks = {}")
    body.append('for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:')
    body.append("    for i, line in enumerate(open(os.path.join(BASE, f), encoding=\"utf-8\"), 1):")
    body.append("        if CJK.search(line):")
    body.append("            leaks.setdefault(f, []).append((i, line.strip()[:80]))")
    body.append('print("CJK leaks:", leaks if leaks else "NONE")')
    body.append("assert not leaks, \"CJK strings remain after transform\"")
else:
    body.append("olds = [old for _, old, _ in " + repr([(n, o, e) for n, o, e in pairs]) + "]")
    body.append("exempt = " + repr(sorted(set(CFG.get("leftover_exempt", [])) | {o for _, o, e in pairs if TR[e] == o})))
    body.append("olds = [o for o in olds if o not in exempt]")
    body.append("left = {}")
    body.append('for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:')
    body.append('    s = open(os.path.join(BASE, f), encoding="utf-8").read()')
    body.append("    for old in olds:")
    body.append("        if old in s:")
    body.append("            left.setdefault(f, []).append(old)")
    body.append('print("leftover original literals:", left if left else "NONE")')
    body.append("assert not left, \"original literals remain after transform\"")
body.append("")
body.append('print("\\n".join(LOG))')
body.append('print(f"TOTAL replacements: {len(LOG)}")')
body.append("")

out = os.path.join(HERE, f"transform-{CODE}.py")
open(out, "w", encoding="utf-8").write("\n".join(body))
print("wrote", out)
