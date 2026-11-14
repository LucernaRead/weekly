# D5-REPORT — 2026-w43-zh-tw-nl (W43 zh-tw, D5 rebuild 2026-11-14)

- Reader: nl (mode latin/TC); `_D5_READER = "latin"`. Core: `2026-w43-zh-tw-en` (built from `production/2026-w43/core-zh-tw/`).
- Install: hand-ported `d5_port_zhtw.py` (installer FATALs on the face= engine) + `install_zhtw.sh` (`--check` first). Routing unit test FAILURES: 0. fix2 markers 5, `_QUOTE_CLS` 4, retained.
- §1.1 assembly: port engine (490 lines) copied into production (SHA-verified vs MANIFEST-W43.md) + pilot moth into `assets/` (production never held the port engine).
- Baseline (10/10 CLEAN family-wide): TOTAL 150, 0 warnings; print PDF bytes/SHA == MANIFEST; web < 7 MB; print-vs-web pdfdiff IDENTICAL; web-vs-issued pdfdiff IDENTICAL; p8 extract 150/150; pre-D5 census D5_latin_in_cjk=426, D5_cyrillic_in_cjk=0, curly_in_cjk=0.
- Rebuild: run TOTAL 150, 0 warnings; render RC=0; webpdf RC=0; print 28,978,377 B sha256 `4fe7944674d99be6e6e9013c1213301b470ccc0da21148171fe58abdd7315ca5`; web 3,035,350 B sha256 `28f65e9130db203b87f9939158f65534b210723c602a8e51772e18b64a614e4a`.
- Cold cache: print PDF cold-cache explosion in fix1 render: 98,845,804 B; warmed fc-cache and re-rendered from the same source -> 28,978,377 B; full gates re-run after.
- Fixes (point sizes only, zero wording changes; full re-render + full gates after each):
  - `content56.py:195` — P6 票券拆解 closing note para: 19.5 -> 19; spill 'berekening.' BELOW +4.67px -> 0 [pre-existing, identical in baseline].
- P8: extract 150/150; compare CLEAN (missing=[], extra=0; [108] present in both core and edition — no D28 discrepancy in this family). Lines 201 -> 201 (unchanged); footer slack 46.2px.
- Gates: 18 GATE PASS, 0 hard FAIL, 1 REFLOW (gate 15a text.md: D5 reflow moves line breaks only, difflines=38, char-multiset diff 0, native verifier ADOPT; coordinator adjudication requested). Gate 15a print=web PASS (multiset 0). Gate 15b rc=1 (see KIT D5 record for the D27 acceptance / pt tool gap). Gate 15c native verifier PASS (ADOPT). D18 masthead gap 42.0px PASS.
- text.md: joined patched export `logs/2026-w43-zh-tw-nl/2026-w43-zh-tw-nl.text.md.new` (joiner `scripts/textexp_zh_tw_d5.py`); ships new with the bundle (issues/ holds no `.text.md`).
- Logs: `scratch-2026-w43-zh-tw/logs/2026-w43-zh-tw-nl/` (`gates.log`, `GATES-SUMMARY.txt`, `run-patched.log`, `render-patched.log`, `rebuild-patched.log`).
