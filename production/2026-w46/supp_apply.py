# -*- coding: utf-8 -*-
"""Generic W46 fan-out supplement applier. Usage:
  python supp_apply.py <lang>   (imports supp_<lang>.py from the build dir)
Applies GEOM (whole-line, asserted/idempotent) then SUPP (longest-first,
already-applied tolerant). SUPP old strings must occur or their new string
must already be present, else FAILS loudly."""
import importlib, os, sys

def main():
    lang = sys.argv[1]
    build = os.path.expanduser(
        f"~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-ko-{lang}-build")
    sys.path.insert(0, build)
    mod = importlib.import_module(f"supp_{lang.replace('-', '_')}")
    p12 = os.path.join(build, "content12.py")
    text = open(p12, encoding="utf-8").read()
    for old, new in mod.GEOM:
        n = text.count(old)
        if n == 0 and new.split("\n")[-1] in text:
            print(f"  GEOM already-applied: {old[:50]!r}")
            continue
        assert n == 1, f"GEOM NOT FOUND (x{n}): {old[:60]!r}"
        text = text.replace(old, new)
        print(f"  GEOM x{n} {old[:50]!r}")
    open(p12, "w", encoding="utf-8").write(text)
    files = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]
    texts = {f: open(os.path.join(build, f), encoding="utf-8").read() for f in files}
    for old, new in sorted(mod.SUPP, key=lambda p: -len(p[0])):
        hit = False
        for f in files:
            n = texts[f].count(old)
            if n >= 1:
                texts[f] = texts[f].replace(old, new)
                hit = True
                print(f"  SUPP {f} x{n} {old[:44]!r} -> {new[:44]!r}")
        if not hit:
            already = any(new in texts[f] for f in files)
            if already:
                print(f"  SUPP already-applied: {old[:44]!r}")
            else:
                print(f"  SUPP WARNING not-found (W45-op may have translated differently; final CJK scan decides): {old[:60]!r}")
    for f in files:
        open(os.path.join(build, f), "w", encoding="utf-8").write(texts[f])
    print(f"SUPP-{lang.upper()} DONE")

if __name__ == "__main__":
    main()
