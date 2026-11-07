#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Same-class sweep for W46 KO Round 3 (run PRE-fix on core sources; stems
verified byte-identical across all 11 build dirs separately).

(a) D3 class: fill-in stems where the key ends with the stem's own attached
    suffix (text immediately after '___' up to first space/punctuation).
(b) D4 class: quotative particles 이라고/라고 in exercise stems (reconstructed
    with the key) and in all other Korean string literals (preceding word in
    the same literal), checked against the final syllable's batchim
    (jongseong): batchim-final -> 이라고; vowel-final -> 라고.

Sources are read as TEXT via ast and never imported/executed.
"""
import ast, glob, os, re, sys, json

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
BUILDS = {
 "zh-cn": "weekly-report-w46-ko-build", "de": "weekly-report-w46-ko-de-build",
 "en": "weekly-report-w46-ko-en-build", "es": "weekly-report-w46-ko-es-build",
 "fr": "weekly-report-w46-ko-fr-build", "it": "weekly-report-w46-ko-it-build",
 "ja": "weekly-report-w46-ko-ja-build", "nl": "weekly-report-w46-ko-nl-build",
 "pt": "weekly-report-w46-ko-pt-build", "ru": "weekly-report-w46-ko-ru-build",
 "zh-tw": "weekly-report-w46-ko-zh-tw-build",
}
HANG = re.compile(r"[\uac00-\ud7a3]")

def batchim(ch):
    """True if Hangul syllable ch has a final consonant (jongseong)."""
    o = ord(ch) - 0xAC00
    if o < 0 or o > 11171:
        return None
    return (o % 28) != 0

def last_hangul(word):
    for ch in reversed(word):
        if HANG.match(ch):
            return ch
    return None

def const_str(node):
    return node.value if isinstance(node, ast.Constant) and isinstance(node.value, str) else None

def collect_ex_calls(build_dir):
    """Return list of (file, lineno, key, stem, kind) for .ex() calls with a
    positional stem at index 4, plus (file, lineno, key, body) for body= kwargs."""
    out = []
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        path = os.path.join(build_dir, fname)
        tree = ast.parse(open(path, encoding="utf-8").read(), filename=fname)
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            if not (isinstance(node.func, ast.Attribute) and node.func.attr == "ex"):
                continue
            args = [const_str(a) for a in node.args]
            key = args[2] if len(args) > 2 else None
            stem = args[4] if len(args) > 4 else None
            if stem is not None and key is not None:
                out.append((fname, node.lineno, key, stem, "ex-stem"))
            for kw in node.keywords:
                if kw.arg in ("body",):
                    v = const_str(kw.value)
                    if v is not None:
                        out.append((fname, node.lineno, key, v, "ex-body"))
                if kw.arg in ("opts",):
                    if isinstance(kw.value, (ast.List, ast.Tuple)):
                        for el in kw.value.elts:
                            v = const_str(el)
                            if v is not None:
                                out.append((fname, node.lineno, key, v, "ex-opt"))
    return out

def sweep_doubling(calls):
    cands = []
    for fname, ln, key, stem, kind in calls:
        if "___" not in stem:
            continue
        # multiple blanks?
        nblank = stem.count("___")
        after = stem.split("___", 1)[1]
        # attached suffix: Hangul run immediately after ___ (no space)
        m = re.match(r"([\uac00-\ud7a3]+)", after)
        suffix = m.group(1) if m else ""
        flag = bool(suffix) and key.endswith(suffix)
        cands.append({"file": fname, "line": ln, "kind": kind, "key": key,
                      "stem": stem, "nblank": nblank, "suffix": suffix,
                      "doubling": flag,
                      "reconstructed": stem.replace("___", key, 1) if nblank else stem})
    return cands

def sweep_quotative_stems(calls):
    cands = []
    for fname, ln, key, stem, kind in calls:
        if "___" not in stem:
            continue
        # Find the quotative particle AFTER the blank; prefer the longer
        # '이라고' ('라고' is a substring of '이라고' — never double-count).
        idx = stem.find("___")
        tail = stem[idx:]
        if "이라고" in tail:
            part, pidx = "이라고", stem.find("이라고", idx)
        elif "라고" in tail:
            part, pidx = "라고", stem.find("라고", idx)
        else:
            continue
        words = re.findall(r"[\uac00-\ud7a3]+", key)
        qw = words[-1] if words else ""
        lh = last_hangul(qw)
        b = batchim(lh) if lh else None
        correct = "이라고" if b else "라고"
        cands.append({"file": fname, "line": ln, "kind": kind, "key": key,
                      "stem": stem, "particle": part,
                      "quoted_word": qw, "last_syllable": lh,
                      "batchim": b, "correct_particle": correct,
                      "mismatch": part != correct,
                      "reconstructed": stem.replace("___", key, 1)})
    return cands

def sweep_quotative_literals(build_dir):
    """All string literals containing 이라고/라고, preceding word checked.
    Excludes the exercise stems already covered (tagged separately)."""
    cands = []
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        path = os.path.join(build_dir, fname)
        tree = ast.parse(open(path, encoding="utf-8").read(), filename=fname)
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                s = node.value
                # Prefer the longer '이라고' at each position (라고 is a
                # substring of 이라고). Scan left to right.
                pos = 0
                while True:
                    i1 = s.find("이라고", pos)
                    i2 = s.find("라고", pos)
                    if i1 < 0 and i2 < 0:
                        break
                    if i1 >= 0 and (i2 < 0 or i1 <= i2):
                        part, mstart = "이라고", i1
                    else:
                        part, mstart = "라고", i2
                    pos = mstart + len(part)
                    before = s[:mstart]
                    # Preceding token: last whitespace-delimited token,
                    # quotes stripped; last Hangul syllable decides.
                    toks = before.split()
                    raw_tok = toks[-1].strip("'\"‘’“”「」『』") if toks else ""
                    lh = last_hangul(raw_tok)
                    b = batchim(lh) if lh else None
                    correct = "이라고" if b else ("라고" if lh else None)
                    cands.append({"file": fname, "line": node.lineno,
                                  "literal": s, "particle": part,
                                  "preceding_token": raw_tok,
                                  "last_syllable": lh,
                                  "batchim": b, "correct_particle": correct,
                                  "mismatch": (correct is not None and part != correct),
                                  "non_hangul_token": lh is None})
    return cands

def main():
    core_dir = os.path.join(GOAL, "hidden_files", BUILDS["zh-cn"])
    calls = collect_ex_calls(core_dir)
    print(f"ex-call stems collected (core): {len(calls)}")
    dbl = sweep_doubling(calls)
    print(f"stems with ___: {sum(1 for d in dbl if d['nblank'])}; "
          f"multi-blank: {[d for d in dbl if d['nblank'] > 1]}")
    flags = [d for d in dbl if d["doubling"]]
    print(f"D3-CLASS DOUBLING CANDIDATES: {len(flags)}")
    for d in flags:
        print(json.dumps(d, ensure_ascii=False))
    print("--- all attached-suffix stems (suffix non-empty) ---")
    for d in dbl:
        if d["suffix"]:
            print(json.dumps(d, ensure_ascii=False))
    q = sweep_quotative_stems(calls)
    print(f"QUOTATIVE STEMS: {len(q)}")
    for d in q:
        print(json.dumps(d, ensure_ascii=False))
    lits = sweep_quotative_literals(core_dir)
    print(f"QUOTATIVE LITERALS (all, incl. stems/notes/prose): {len(lits)}")
    for d in lits:
        print(json.dumps(d, ensure_ascii=False))
    # stem identity across editions
    print("--- stem identity core vs fan-outs ---")
    def stemset(code):
        cs = collect_ex_calls(os.path.join(GOAL, "hidden_files", BUILDS[code]))
        return {(c[2], c[3]) for c in cs if c[4] == "ex-stem"}
    core_stems = stemset("zh-cn")
    print(f"core ex-stems: {len(core_stems)}")
    for code in BUILDS:
        if code == "zh-cn":
            continue
        s = stemset(code)
        print(code, "n=", len(s), "diff-vs-core:", sorted(s ^ core_stems)[:10] if s != core_stems else "IDENTICAL")
    out = {"doubling_all": dbl, "doubling_flags": flags,
           "quotative_stems": q, "quotative_literals": lits}
    outpath = sys.argv[1] if len(sys.argv) > 1 else None
    if outpath:
        with open(outpath, "w", encoding="utf-8") as fh:
            json.dump(out, fh, ensure_ascii=False, indent=1)
        print("wrote", outpath)

if __name__ == "__main__":
    main()
