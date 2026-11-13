# Lessons from fr (2026-11-11) — apply to es / it / pt / nl / ja / ko / zh-tw

## 1. Apostrophes: use straight ' everywhere (Latin langs)
- U+2019 (curly ’) renders FULL-WIDTH (20.5 px at 20.5 px font) in Noto Sans CJK SC, the font Latin runs are set in. Every `l'`, `d'`, `C'` gets a 9–10 px gap — wider than a word space, reads as a typo (`C' est`, `l' année`).
- W46 TMs carry curly values (fr: 31). Fix at MAP level after build_map: replace ’ → ' in all lit/type/instr/key values + meta except meta.abstract (plain-text file, keep curly there). 0 curly must remain in the map; verify with grep on the applied content*.py/bslib4.py.
- Author miss-tr files with straight ' from the start. (en already used straight '; fr miss had 21 curly.)
- Note: build_map.py map buckets are `lit, type, instr, key, meta` — there is NO `note` bucket (notes live in `lit`). A script iterating `m['note']` crashes with KeyError and leaves the map unmodified — check the structure first.

## 2. P1 numbers-box head width vs the Q6 chip (all langs)
- The head is 23 px bold, starts x=556.5; the French run starts x≈726.6; the B1 Q6 chip rect starts x=989. The translation must end ≤ ~975 (≥14 px gap; en/de have 55 px).
- fr's `La journée en chiffres` ended ≈989 → 0 px contact with the chip, a real defect, fixed to the W46 pattern `EN CHIFFRES`.
- Measure each language's head with `svglib.text_w(' <translation>','sans',True,23)` from the core dir BEFORE building: end = 726.6 + w. If end > 975, shorten the translation (W46 pattern: short caps form).
- Same check applies to any long band-sub/head translation that could reach a flow column: measure, don't guess.

## 3. Width-measurement reminder (unchanged)
- P1 gloss 19 px sans ≤422.5 px; P7 errs 19.5 px sans ≤378.5 px; P7 word gloss/disc 20 px sans ≤378.5 px; A-bridges 20.5 px sans ≤422.5 px. Measure before building; apostrophe replacement shortens strings (~15 px per ’), so post-fix fits only improve.
