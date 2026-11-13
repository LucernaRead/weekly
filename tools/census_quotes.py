# -*- coding: utf-8 -*-
"""U+201C/U+201D/U+2019 SVG census (coordinator's method).

Per <text> element font-family: count the three quote codepoints in
defective families (Noto Sans CJK SC/TC/HK — full-width 1.000em advance).
Quotes in Newsreader (or any other family) are NOT defective.
Usage: census_quotes.py <svg-dir> [svg-dir ...]
Prints per-file rows + a total; exit 0 iff 0 defective glyphs.
"""
import sys, os
import xml.etree.ElementTree as ET

CPS = {"\u201c": "U+201C", "\u201d": "U+201D", "\u2019": "U+2019"}
DEFECTIVE = {"Noto Sans CJK SC", "Noto Sans CJK TC", "Noto Sans CJK HK"}
NS = "{http://www.w3.org/2000/svg}"

def census_dir(svgdir):
    rows = []
    total_def = 0
    total_by_family = {}
    for fn in sorted(os.listdir(svgdir)):
        if not fn.endswith(".svg"):
            continue
        path = os.path.join(svgdir, fn)
        root = ET.parse(path).getroot()
        defect = 0
        by_family = {}
        for el in root.iter(NS + "text"):
            fam = el.get("font-family", "")
            txt = "".join(el.itertext())
            for cp, name in CPS.items():
                n = txt.count(cp)
                if n:
                    by_family.setdefault(fam, {}).setdefault(name, 0)
                    by_family[fam][name] += n
                    if fam in DEFECTIVE:
                        defect += n
        total_def += defect
        for fam, d in by_family.items():
            for name, n in d.items():
                total_by_family.setdefault(fam, {}).setdefault(name, 0)
                total_by_family[fam][name] += n
        rows.append((fn, defect, by_family))
    return rows, total_def, total_by_family

def main():
    grand = 0
    for svgdir in sys.argv[1:]:
        rows, total_def, total_by_family = census_dir(svgdir)
        print(f"== {svgdir} ==")
        for fn, defect, by_family in rows:
            detail = "; ".join(
                f"{fam}: " + ",".join(f"{k}x{v}" for k, v in sorted(d.items()))
                for fam, d in sorted(by_family.items()))
            print(f"  {fn}: defective={defect}" + (f"  [{detail}]" if detail else ""))
        print(f"  TOTAL defective: {total_def}")
        for fam, d in sorted(total_by_family.items()):
            tag = "DEFECTIVE" if fam in DEFECTIVE else "ok"
            print(f"    {fam} ({tag}): " + ",".join(f"{k}x{v}" for k, v in sorted(d.items())))
        grand += total_def
    print(f"GRAND TOTAL defective: {grand}")
    return 0 if grand == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
