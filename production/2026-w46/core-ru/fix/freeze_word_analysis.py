# -*- coding: utf-8 -*-
"""Word-level freeze analysis (proofreader-style): per-page Cyrillic-word
multiset diff core vs edition (ADD must be empty), CJK char totals in the
edition, added-script breakdown, Simplified/Traditional-only checks via
opencc, and core Han nodes surviving verbatim. Reads SVG text only."""
import re, sys, os, glob
from collections import Counter

TEXT_RE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)
CYR = re.compile(r"[А-Яа-яЁё]+")
HAN = re.compile(r"[\u2e80-\u9fff]")
KANA = re.compile(r"[\u3040-\u30ff]")
HANGUL = re.compile(r"[\uac00-\ud7a3]")

def texts(svgdir):
    out = {}
    for f in sorted(glob.glob(os.path.join(svgdir, "*.svg"))):
        t = open(f, encoding="utf-8").read()
        out[os.path.basename(f)] = [re.sub(r"<[^>]+>", "", m.group(1)) for m in TEXT_RE.finditer(t)]
    return out

def main():
    core_dir, ed_dir, label = sys.argv[1], sys.argv[2], sys.argv[3]
    core, ed = texts(core_dir), texts(ed_dir)
    try:
        import opencc
        s2t = opencc.OpenCC("s2t"); t2s = opencc.OpenCC("t2s")
    except Exception as e:
        s2t = t2s = None
        print(f"opencc unavailable: {e}")
    total_add, total_rem = Counter(), Counter()
    ed_chars = Counter()
    for fn in sorted(core):
        c = Counter(w for s in core[fn] for w in CYR.findall(s))
        e = Counter(w for s in ed[fn] for w in CYR.findall(s))
        add, rem = e - c, c - e
        total_add.update(add); total_rem.update(rem)
        print(f"{fn} CYR-WORD ADD: {dict(add)}")
        print(f"{fn} CYR-WORD REM: {dict(rem)}")
    for fn in sorted(ed):
        for s in ed[fn]:
            ed_chars.update(s)
    han = sum(v for k, v in ed_chars.items() if HAN.match(k))
    kana = sum(v for k, v in ed_chars.items() if KANA.match(k))
    hangul = sum(v for k, v in ed_chars.items() if HANGUL.match(k))
    cyr = sum(v for k, v in ed_chars.items() if CYR.match(k))
    print(f"TOTAL ADD: {dict(total_add)}")
    print(f"TOTAL REM: {dict(total_rem)}")
    print(f"CHAR TOTALS cyr={cyr} han={han} kana={kana} hangul={hangul}")
    # core Han nodes surviving verbatim in edition
    core_han = [s for fn in core for s in core[fn] if HAN.search(s)]
    ed_set = Counter(s for fn in ed for s in ed[fn])
    surv = [s for s in core_han if ed_set.get(s, 0) > 0]
    print(f"CORE HAN NODES SURVIVING VERBATIM: {len(surv)}")
    for s in surv[:5]:
        print(f"  SURV: {s!r}")
    if s2t and t2s:
        # Added CJK chars: chars in edition strings not present in core at all
        core_chars = set("".join(s for fn in core for s in core[fn]))
        ed_added_chars = sorted({ch for fn in ed for s in ed[fn] for ch in s if HAN.match(ch) and ch not in core_chars})
        simp_only = [ch for ch in ed_added_chars if s2t.convert(ch) != ch]
        trad_only = [ch for ch in ed_added_chars if t2s.convert(ch) != ch]
        print(f"ADDED HAN CHARS (not in core): {''.join(ed_added_chars)}")
        print(f"SIMPLIFIED-ONLY among added: {''.join(simp_only)}")
        print(f"TRADITIONAL-ONLY among added: {''.join(trad_only)}")
    return 1 if total_add else 0

if __name__ == "__main__":
    sys.exit(main())
