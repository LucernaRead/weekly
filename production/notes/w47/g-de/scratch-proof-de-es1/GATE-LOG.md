# GATE-LOG — de-es proof1 (2026-11-11)
Probe: `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` RC=0 (9daeafb9…); probe file written hidden_files/w47/probe-de-es-proof1.txt.
SHA verify (2026-11-11 09:05 UTC):
- print Die-Lucerna-VOL4-de-es.pdf 10,968,803 B sha256 7bc39e1f58b9bb44… MATCH
- web   Die-Lucerna-VOL4-de-es-web.pdf 1,558,821 B sha256 cd453143111bfad4… MATCH
- text  2026-w47-de-es.text.md 50,124 B sha256 5f5ea69b69a578dd… MATCH
PROBE-OK 2026-11-11T09:16:14Z
PROBE-OK 2026-11-11T09:21:10Z
## Gates re-run by proofer (all outputs in this dir unless noted)
- sha256sum print/web/text.md: MATCH all three (7bc39e1f… / cd453143… / 5f5ea69b…); sizes 10,968,803 / 1,558,821 / 50,124 B.
- pdftotext -layout print/web: 114,654 / 114,737 B; 8 pages each; per-page word multiset identical P1-P8.
- pdftotext default: print 51,012 B / web 51,013 B, word multiset identical (8,088). -raw normalised: identical 49,812 B.
- Q34 counts (grep): new 1x / old 0x in content34.py, .text.md, svg/p3-kultur.svg, print txt, web txt.
- Curly quotes: U+201C 33 / U+201D 0 / U+2019 0 in SVGs+text.md; all 201C paired with 201E (33) in German strings; tr_es.py 2x 201C/201E inside German stem only.
- text.md vs core-de text.md diff: 951/1,186 lines identical; stem check 137 numbered, 14 diffs all explanation-layer/expected.
- MUSTER token count: 84 (python split).
- occlusion_audit.py svg --json occlusion.json --selftest: RC=0 BUT --selftest runs selftest ONLY (no audit) — caught on review; re-run WITHOUT --selftest: RC=0, selftest OK, "0 flags", occlusion.json flag_count=0.
- p8.py extract --p8 svg/p8-uebungen.svg --total 150 --json p8extract.json: RC=0, noted 150/150.
- p8.py compare --core-p8 core/svg/p8-uebungen.svg --edition-p8 svg/p8-uebungen.svg --total 150 --json p8compare.json: RC=0, CLEAN, keydiff=[137,138,139,150].
- freeze.py diff --core-svg core/svg --edition-svg svg --json freeze.json: RC=0, TOTAL added CJK 7 (all U+3000, P2-P8 x1).
- freeze_direct.py es <ED> <S>: RC=0, source PASS (0 unaccounted), rendered 8/8, sha 083e2a2a/689045ad/fc88f676/df1bebf7/86fa4421/2bbe05f9/b7aa0771/57e118e7.
- keycheck.py es <ED> <S> (needs p8extract.json in S): RC=0, 149/150 exact, only Q150 extractor truncation.
- boxtitle.py es (from scratch-fanout-de-rebuild-A): RC=0, 7/7 fit.
- d2scan-de-es.py (this dir): 58 print-abutting pairs, 0 web gaps >0.5pt; extended delta check all 81 pairs max |delta| 0.0pt.
- creambox.py (this dir): all cream boxes clearance +10.4..+47.7 EXCEPT P7 toolbox -0.4 (box bottom 783.5, last baseline 783.9); de-en P7 identical -0.4 (same geometry); core-de toolbox +18.8.
- chips rx="2.7": 10/15/18/15/18/12/35 TOTAL 141. P8 min span (PyMuPDF): 9.94pt. ABSTRACT.txt 426B, 0 ASCII ".
- Pixel diff print-vs-web (100dpi renders): mean |d| P1 2.096, P2 0.521, P3 0.572, P4 0.673, P5 0.679, P6 0.585, P7 1.467, P8 0.188.
- Visual: print P1-P8 viewed; web W1-W8 viewed; zoom p7-toolbox-zoom.png (render crop, /tmp/proof-de-es1/) confirms D1.
- No disk-quota errors encountered; probes passed before every write (git hash-object RC=0 each time).
