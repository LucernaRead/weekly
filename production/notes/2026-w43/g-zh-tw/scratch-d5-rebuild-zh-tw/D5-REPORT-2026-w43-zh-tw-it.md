# D5-REPORT — 2026-w43-zh-tw-it (W43 zh-tw, D5 rebuild 2026-11-14)

- Reader: it (mode latin/TC); `_D5_READER = "latin"`. Core: `2026-w43-zh-tw-en` (built from `production/2026-w43/core-zh-tw/`).
- Install: hand-ported `d5_port_zhtw.py` (installer FATALs on the face= engine) + `install_zhtw.sh` (`--check` first). Routing unit test FAILURES: 0. fix2 markers 5, `_QUOTE_CLS` 4, retained.
- §1.1 assembly: port engine (490 lines) copied into production (SHA-verified vs MANIFEST-W43.md) + pilot moth into `assets/` (production never held the port engine).
- Baseline (10/10 CLEAN family-wide): TOTAL 150, 0 warnings; print PDF bytes/SHA == MANIFEST; web < 7 MB; print-vs-web pdfdiff IDENTICAL; web-vs-issued pdfdiff IDENTICAL; p8 extract 150/150; pre-D5 census D5_latin_in_cjk=425, D5_cyrillic_in_cjk=0, curly_in_cjk=0.
- Rebuild: run TOTAL 150, 0 warnings; render RC=0; webpdf RC=0; print 28,980,352 B sha256 `011636d3392127a2b554e1f1e08b422f117413d8a442da9750789e48dc4a6932`; web 3,037,376 B sha256 `7a20bc32cc31f23de7a4a5734cf8cbf1b3858309b581a96e7875af7d31e14b1b`.
- Fixes (point sizes only, zero wording changes; full re-render + full gates after each):
  - `content12.py:175` — P2 你呢 question para: 20 -> 19.5; spill 'giorni?' BELOW +4.20px -> 0 [pre-existing, identical in baseline].
- P8: extract 150/150; compare CLEAN (missing=[], extra=0; [108] present in both core and edition — no D28 discrepancy in this family). Lines 214 -> 214 (unchanged); footer slack 56.6px.
- Gates: 18 GATE PASS, 0 hard FAIL, 1 REFLOW (gate 15a text.md: D5 reflow moves line breaks only, difflines=50, char-multiset diff 0, native verifier ADOPT; coordinator adjudication requested). Gate 15a print=web PASS (multiset 0). Gate 15b rc=1 (see KIT D5 record for the D27 acceptance / pt tool gap). Gate 15c native verifier PASS (ADOPT). D18 masthead gap 42.0px PASS.
- text.md: joined patched export `logs/2026-w43-zh-tw-it/2026-w43-zh-tw-it.text.md.new` (joiner `scripts/textexp_zh_tw_d5.py`); ships new with the bundle (issues/ holds no `.text.md`).
- Logs: `scratch-2026-w43-zh-tw/logs/2026-w43-zh-tw-it/` (`gates.log`, `GATES-SUMMARY.txt`, `run-patched.log`, `render-patched.log`, `rebuild-patched.log`).
