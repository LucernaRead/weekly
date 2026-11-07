#!/usr/bin/env python3
"""Font-coverage sweep for one edition: every char in every SVG <text> node
checked against the cmap of the rendering font face actually used
(family + weight, SC face index 2 of the split TTCs, UnifrakturMaguntia TTF).
Reports chars missing from the used weight's cmap. A char missing from BOTH
weights of its family is a true missing glyph (tofu / blank gap).
Control: U+0161 š must be reported missing from Noto Serif CJK SC.
"""
import json, re, sys
from pathlib import Path
from fontTools.ttLib import TTFont

GOAL = Path.home() / "workspace/goals/lucernaread-social-media-operations"
ED = GOAL / "files/weekly-report-w46-ru-it/svg"

FONTS = {
    ("Noto Sans CJK SC", "regular"): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 2),
    ("Noto Sans CJK SC", "bold"): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 2),
    ("Noto Serif CJK SC", "regular"): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc", 2),
    ("Noto Serif CJK SC", "bold"): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc", 2),
    ("UnifrakturMaguntia", "regular"): (str(Path.home() / ".local/share/fonts/UnifrakturMaguntia.ttf"), 0),
    ("UnifrakturMaguntia", "bold"): (str(Path.home() / ".local/share/fonts/UnifrakturMaguntia.ttf"), 0),
}

cmaps = {}
for key, (path, idx) in FONTS.items():
    font = TTFont(path, fontNumber=idx, lazy=False)
    cmaps[key] = set(font.getBestCmap().keys())
    print(f"cmap {key}: {len(cmaps[key])} chars from {path} face {idx}")

NS = "{http://www.w3.org/2000/svg}"
import xml.etree.ElementTree as ET

used = {}  # (family, weight) -> set(chars)
occurrences = {}  # char -> list of (file, family, weight, text-snippet)
for svg in sorted(ED.glob("*.svg")):
    root = ET.parse(svg).getroot()
    for el in root.iter(NS + "text"):
        fam = el.get("font-family", "")
        fw = el.get("font-weight", "")
        weight = "bold" if str(fw) == "700" else "regular"
        text = "".join(el.itertext())
        for ch in text:
            if ch in " \n\t":
                continue
            used.setdefault((fam, weight), set()).add(ch)
            occurrences.setdefault(ch, []).append((svg.name, fam, weight, text[:60]))

print(f"\nDistinct rendered chars (excl. whitespace): {len(occurrences)}")
for (fam, weight), chars in sorted(used.items()):
    print(f"  {fam} {weight}: {len(chars)} distinct chars")

missing = {}  # char -> set of (family,weight) missing it
for ch, occs in occurrences.items():
    for fam, weight in {(f, w) for _, f, w, _ in occs}:
        cmap = cmaps.get((fam, weight))
        if cmap is None:
            print(f"WARN no cmap for {(fam, weight)}")
            continue
        if ord(ch) not in cmap:
            missing.setdefault(ch, set()).add((fam, weight))

print(f"\nMISSING-GLYPH CHARS: {len(missing)}")
for ch, fams in sorted(missing.items(), key=lambda kv: ord(kv[0])):
    print(f"  U+{ord(ch):04X} {ch!r} missing from {sorted(fams)}; e.g. {occurrences[ch][0]}")
    for occ in occurrences[ch][:5]:
        print(f"      {occ}")

# Control: š must be missing from Serif SC (both weights) — proves the sweep
# would have caught D4 pre-fix.
serif = cmaps[("Noto Serif CJK SC", "regular")] | cmaps[("Noto Serif CJK SC", "bold")]
print(f"\nCONTROL š U+0161 in Serif SC cmap union: {0x161 in serif} (expect False)")
print(f"CONTROL š U+0161 in Sans SC cmap union: {0x161 in (cmaps[('Noto Sans CJK SC','regular')] | cmaps[('Noto Sans CJK SC','bold')])}")
print(f"CONTROL š present in current it SVGs: {chr(0x161) in occurrences}")

out = {
    "distinct_chars": len(occurrences),
    "missing": {f"U+{ord(ch):04X}": sorted([f"{f}/{w}" for f, w in fams]) for ch, fams in missing.items()},
    "control_serif_has_scaron": bool(0x161 in serif),
    "all_chars": sorted(f"U+{ord(c):04X}" for c in occurrences),
}
Path(sys.argv[1] if len(sys.argv) > 1 else "font-coverage.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
print("\nSWEEP RESULT:", "CLEAN — no missing glyphs" if not missing else f"{len(missing)} MISSING")
