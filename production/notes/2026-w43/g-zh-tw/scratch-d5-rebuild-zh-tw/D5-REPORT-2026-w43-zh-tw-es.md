# D5-REPORT — 2026-w43-zh-tw-es (W43 zh-tw, D5 rebuild 2026-11-14)

- Reader: es (mode latin/TC); `_D5_READER = "latin"`. Core: `2026-w43-zh-tw-en` (built from `production/2026-w43/core-zh-tw/`).
- Install: hand-ported `d5_port_zhtw.py` (installer FATALs on the face= engine) + `install_zhtw.sh` (`--check` first). Routing unit test FAILURES: 0. fix2 markers 5, `_QUOTE_CLS` 4, retained.
- §1.1 assembly: port engine (490 lines) copied into production (SHA-verified vs MANIFEST-W43.md) + pilot moth into `assets/` (production never held the port engine).
- Baseline (10/10 CLEAN family-wide): TOTAL 150, 0 warnings; print PDF bytes/SHA == MANIFEST; web < 7 MB; print-vs-web pdfdiff IDENTICAL; web-vs-issued pdfdiff IDENTICAL; p8 extract 150/150; pre-D5 census D5_latin_in_cjk=427, D5_cyrillic_in_cjk=0, curly_in_cjk=0.
- Rebuild: run TOTAL 150, 0 warnings; render RC=0; webpdf RC=0; print 28,987,001 B sha256 `7e4a2fae46d0e081148e1a747c48ce08c0c3c3d728d1431f7b83ea7c77f00003`; web 3,042,374 B sha256 `d4df3c6b31847887bafc569cbecf14dac2889238fb8e2ce0edbb14dc0ba579f6`.
- Fixes: none.
- P8: extract 150/150; compare CLEAN (missing=[], extra=0; [108] present in both core and edition — no D28 discrepancy in this family). Lines 194 -> 194 (unchanged); footer slack 44.0px.
- Gates: 18 GATE PASS, 0 hard FAIL, 1 REFLOW (gate 15a text.md: D5 reflow moves line breaks only, difflines=54, char-multiset diff 0, native verifier ADOPT; coordinator adjudication requested). Gate 15a print=web PASS (multiset 0). Gate 15b rc=1 (see KIT D5 record for the D27 acceptance / pt tool gap). Gate 15c native verifier PASS (ADOPT). D18 masthead gap 42.0px PASS.
- text.md: joined patched export `logs/2026-w43-zh-tw-es/2026-w43-zh-tw-es.text.md.new` (joiner `scripts/textexp_zh_tw_d5.py`); ships new with the bundle (issues/ holds no `.text.md`).
- Logs: `scratch-2026-w43-zh-tw/logs/2026-w43-zh-tw-es/` (`gates.log`, `GATES-SUMMARY.txt`, `run-patched.log`, `render-patched.log`, `rebuild-patched.log`).
