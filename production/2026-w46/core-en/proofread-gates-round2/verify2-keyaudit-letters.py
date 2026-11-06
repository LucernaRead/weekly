#!/usr/bin/env python3
"""Round 2 key audit (supplementary requirement): cross-edition printed-key
comparison (p8.py extract outputs) + independent raw-SVG letter-key parse.
Run: python3 verify2-keyaudit-letters.py  (from the gate dir; paths absolute)
Outputs: stdout summary; also writes verify2-keyaudit-crossedition.log.
Method:
  A. p8.py extract --total 150 per edition (verify2-p8keys-*.json, saved
     separately): compare each edition's printed keys dict value-by-value
     against the core's; compare core printed keys against registry.json.
  B. Independent parse: raw <text> elements of each P8 SVG, answers region
     (y>1850), grouped by x-column, joined; regex (N. LETTER) for the 79
     single-letter keys; compare against core letters. Independent code path
     from p8.py (guards against a shared extraction bug hiding a letter
     transposition identically in all editions).
"""
import re, json, os, glob, sys

G = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
R = os.path.join(G, "hidden_files/w46/en-proofread-gates-round2")

def main():
    print("=== A. p8.py extract comparison (verify2-p8keys-*.json) ===")
    core = json.load(open(os.path.join(R, "verify2-p8keys-core.json")))["keys"]
    reg = json.load(open(os.path.join(G, "hidden_files/w46/en-core/registry.json")))
    regk = {str(e["n"]): e["key"] for e in reg}
    mism = [(n, regk[n], core.get(n)) for n in regk if regk[n] != core.get(n)]
    print(f"core printed keys: {len(core)}; registry-vs-printed mismatches: {len(mism)}")
    for m in mism:
        print("  registry/printed:", m)
    for p in sorted(glob.glob(os.path.join(R, "verify2-p8keys-*.json"))):
        name = os.path.basename(p)
        if "core" in name:
            continue
        k = json.load(open(p))["keys"]
        diffs = [(n, core.get(n), k.get(n)) for n in core if core.get(n) != k.get(n)]
        print(f"{name}: n={len(k)} diffs-vs-core={len(diffs)} {[d[0] for d in diffs]}")
        for n, a, b in diffs:
            print(f"   {n}: core={a!r} ed={b!r}")

    print("=== B. independent raw-SVG letter parse ===")
    def ans_text(eddir):
        s = open(os.path.join(eddir, "svg", "p8-exercices.svg"), encoding="utf-8").read()
        els = re.findall(r'<text x="([^"]+)" y="([^"]+)"[^>]*>([^<]*)</text>', s)
        els = [(float(x), float(y), t) for x, y, t in els if float(y) > 1850]
        cols = {}
        for x, y, t in els:
            cols.setdefault(round(x), []).append((y, t))
        return " ".join(" ".join(t for _, t in sorted(cols[x])) for x in sorted(cols))
    letter_nums = [n for n, v in core.items() if len(v) == 1 and v in "ABCDabcd"]
    pat = re.compile(r"(?<!\d)(\d{1,3})\. ([A-Da-d])(?=[\s·\(\),;。：、！？（]|$)")
    bad = 0
    for name in ["core", "de", "es", "fr", "it", "ja", "ko", "nl", "pt", "ru", "zh-tw"]:
        d = os.path.join(G, "files", "weekly-report-w46-en-core" if name == "core"
                         else f"weekly-report-w46-en-{name}")
        got = {m.group(1): m.group(2) for m in pat.finditer(ans_text(d))}
        for n in letter_nums:
            if got.get(n) != core[n]:
                bad += 1
                print(f"MISMATCH {name} #{n}: expected {core[n]!r} got {got.get(n)!r}")
    print(f"letter keys per edition: {len(letter_nums)}; editions: 11; "
          f"total letter checks: {len(letter_nums)*11}; mismatches: {bad}")

if __name__ == "__main__":
    main()
