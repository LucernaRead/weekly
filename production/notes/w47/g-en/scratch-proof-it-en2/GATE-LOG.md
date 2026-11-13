p1: +32 strings / -46 strings; CJK core 197 -> edition 20; added CJK chars: 1 {'\u3000': 1}
p2: +33 strings / -29 strings; CJK core 191 -> edition 17; added CJK chars: 2 {'\u3000': 2}
p3: +33 strings / -30 strings; CJK core 180 -> edition 15; added CJK chars: 2 {'\u3000': 2}
p4: +29 strings / -26 strings; CJK core 162 -> edition 18; added CJK chars: 2 {'\u3000': 2}
p5: +40 strings / -41 strings; CJK core 227 -> edition 15; added CJK chars: 2 {'\u3000': 2}
p6: +27 strings / -25 strings; CJK core 167 -> edition 17; added CJK chars: 2 {'\u3000': 2}
p7: +42 strings / -40 strings; CJK core 304 -> edition 13; added CJK chars: 1 {'\u3000': 1}
p8: +164 strings / -629 strings; CJK core 1015 -> edition 22; added CJK chars: 1 {'\u3000': 1}
TOTAL added CJK characters: 13
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
production/2026-w47/2026-w47-it-en/svg: 0 flags 
2026-w47-it-en forward-miss: 0 reverse-miss: 0
# GATE LOG — 2026-W47 it-en, proof2 (2026-11-11)

## Identity
- print La-Lucerna-VOL4-EN.pdf 14,032,990 B sha256 d41e7255d7da8ea63cf07560911a518b2e55a4a7d8a9eb8b0f3c1ae6d3129e2f
- web La-Lucerna-VOL4-EN-web.pdf 1,259,104 B sha256 32a6727966cfa130618c64356cd9db9812f04cbc96e961ff1534b143580e5903
- text 2026-w47-it-en.text.md 55,274 B sha256 7160560555042d9992fda8cb8b21b3067eb8374a6279a50b19abdc3443e69c30
  All match the task statement. Re-checked at end of round: identical.

## Regression (fix1 D-1)
- CJK ideographs U+4E00-9FFF in .text.md: 0 (verified in the pre-read scan; the 12144 figure in an earlier draft of this log was a regex-escaping error in the logging snippet, not a measurement)
- '翻译' count: 0; 'Translate]' count: 4
- U+3000: 106; U+FF1A: 14; U+2019: 0
- Lines 969/971/973/975: Q137 [A2 · Translate], Q138 [B1 · Translate], Q139 [B1 · Translate], Q140 [B2 · Translate] — all English, correct.

## Gates run by me (tools/venv/bin/python unless noted)
- p8 extract: 150/150 noted (p8-extract.json)
- p8 compare vs core-it: CLEAN, missing=[], extra_count=0, uncertain=[], keydiff=[137,138,139] (p8-compare.json)
- freeze baseline: 8/8 SVGs byte-identical; core integrity OK (freeze-baseline.log)
- freeze diff: added CJK 13 x U+3000 only (p1 1, p2 2, p3 2, p4 2, p5 2, p6 2, p7 1, p8 1); P8 +164/-629 strings (freeze-diff.json/log)
- occlusion_audit: selftest OK (all 6 classes fired); 0 flags (occlusion.log)
- textmd validator (validate_edition_textmd.py): forward-miss 0 / reverse-miss 0, rc 0 (textmd-validate.log)
- U+2019 full scan (8 SVGs): 0; U+2018: 0
- print/web pdftotext multiset: 7,945 words each, 0 diff both directions; 109,893 bytes each; web PDF < 7 MB, real text layer
- VOL in print text: VOL.4 x9, VOL.5 x3 (P2 cross-ref; P7 LETTERE disclosure; P7 next-week preview)
- badge rects 60x30 with in-rect labels: P1 9/1, P2 14/1, P3 8/10, P4 13/2, P5 15/3, P6 0/0/18, P7 4/4/4, P8 9/23/3 = 141 total
- P8 min font-size in SVG: 13.0 px = 9.75 pt (SOP floor)
- banned terms (Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu): 0
- model text: 99 words; golden sentences 8/8 at exactly 2x; keys numbering 150/150 continuous; levels A2 47/B1 70/B2 33; pages 10/18/18/18/18/18/12/38
- visual: 8 print pages (110 dpi, pages/p-*.png) + web P1/P8 viewed; no overflow/overlap/footer intrusion/clipping/tofu
- core<->en .text.md difflib: 401 changed blocks, 1317 lines each; only Italian-prose change = 4 P1 cifre heads (O-1)

## Notes
- Probe: git hash-object -w OK; real file write into hidden_files/w47/scratch-proof-it-en2/ OK (probe.txt removed).
- O-11: freeze baseline core-SVG hashes differ from fix1 log values (e.g. p1 c213a7b0 vs cea71083); both runs 8/8 self-consistent; no impact (see PROOF-NOTE.md O-11).
- No source/finished file was modified; work confined to the edition dir (read-only) and this scratch dir.
