# D5-REPORT — 2026-w43-zh-tw-pt (W43 zh-tw, D5 rebuild 2026-11-14)

- Reader: pt (mode latin/TC); `_D5_READER = "latin"`. Core: `2026-w43-zh-tw-en` (built from `production/2026-w43/core-zh-tw/`).
- Install: hand-ported `d5_port_zhtw.py` (installer FATALs on the face= engine) + `install_zhtw.sh` (`--check` first). Routing unit test FAILURES: 0. fix2 markers 5, `_QUOTE_CLS` 4, retained.
- §1.1 assembly: port engine (490 lines) copied into production (SHA-verified vs MANIFEST-W43.md) + pilot moth into `assets/` (production never held the port engine).
- Baseline (10/10 CLEAN family-wide): TOTAL 150, 0 warnings; print PDF bytes/SHA == MANIFEST; web < 7 MB; print-vs-web pdfdiff IDENTICAL; web-vs-issued pdfdiff IDENTICAL; p8 extract 150/150; pre-D5 census D5_latin_in_cjk=429, D5_cyrillic_in_cjk=0, curly_in_cjk=0.
- Rebuild: run TOTAL 150, 0 warnings; render RC=0; webpdf RC=0; print 28,989,983 B sha256 `e4320d2adfeb83ad6f3119799aec17247bd40de91c86ba807b50c7cfca003c2f`; web 3,047,164 B sha256 `3631765ddf7418d7dd24ceb82fe63e717aa6493b893fbc1eba29c22bc523cb65`.
- Fixes (point sizes only, zero wording changes; full re-render + full gates after each):
  - `content56.py:195` — P6 票券拆解 closing note para: 19.5 -> 19; spill +7.22px -> +6.56px (last line 'economias sao contas nossas.') [pre-existing (+7.22 in baseline), D5-worsened].
  - `content56.py:190` — P6 票券拆解 box height: 504 -> 514; spill +6.56px -> 0 (same geometry as fr fix) [box-grow, DE KIT adjudication-5 precedent].
- P8: extract 150/150; compare CLEAN (missing=[], extra=0; [108] present in both core and edition — no D28 discrepancy in this family). Lines 203 -> 203 (unchanged); footer slack 42.6px.
- Gates: 18 GATE PASS, 0 hard FAIL, 1 REFLOW (gate 15a text.md: D5 reflow moves line breaks only, difflines=44, char-multiset diff 0, native verifier ADOPT; coordinator adjudication requested). Gate 15a print=web PASS (multiset 0). Gate 15b rc=2 (see KIT D5 record for the D27 acceptance / pt tool gap). Gate 15c native verifier PASS (ADOPT). D18 masthead gap 42.0px PASS.
- text.md: joined patched export `logs/2026-w43-zh-tw-pt/2026-w43-zh-tw-pt.text.md.new` (joiner `scripts/textexp_zh_tw_d5.py`); ships new with the bundle (issues/ holds no `.text.md`).
- Logs: `scratch-2026-w43-zh-tw/logs/2026-w43-zh-tw-pt/` (`gates.log`, `GATES-SUMMARY.txt`, `run-patched.log`, `render-patched.log`, `rebuild-patched.log`).
