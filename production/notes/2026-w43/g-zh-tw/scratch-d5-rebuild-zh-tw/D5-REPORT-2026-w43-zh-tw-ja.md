# D5-REPORT — 2026-w43-zh-tw-ja (W43 zh-tw, D5 rebuild 2026-11-14)

- Reader: ja (mode cjk/JP); `_D5_READER = "cjk"`. Core: `2026-w43-zh-tw-en` (built from `production/2026-w43/core-zh-tw/`).
- Install: hand-ported `d5_port_zhtw.py` (installer FATALs on the face= engine) + `install_zhtw.sh` (`--check` first). Routing unit test FAILURES: 0. fix2 markers 5, `_QUOTE_CLS` 4, retained.
- §1.1 assembly: port engine (490 lines) copied into production (SHA-verified vs MANIFEST-W43.md) + pilot moth into `assets/` (production never held the port engine).
- Baseline (10/10 CLEAN family-wide): TOTAL 150, 0 warnings; print PDF bytes/SHA == MANIFEST; web < 7 MB; print-vs-web pdfdiff IDENTICAL; web-vs-issued pdfdiff IDENTICAL; p8 extract 150/150; pre-D5 census D5_latin_in_cjk=198, D5_cyrillic_in_cjk=0, curly_in_cjk=0.
- Rebuild: run TOTAL 150, 0 warnings; render RC=0; webpdf RC=0; print 34,628,026 B sha256 `66c352fb5f734b31f550cc70a01d41599f5bebf0527549582cfa075552b3fef1`; web 3,742,362 B sha256 `327ba94f410b6bb9ee0d18df960617733a4628ad5ef1f422d49d0d09522344b6`.
- Fixes (point sizes only, zero wording changes; full re-render + full gates after each):
  - `bslib4.py gloss()` — gloss() gains optional size param: default 20.5 (no effect elsewhere); helper only; enables the local fix below [D5-new].
  - `content56.py:18` — P5 金鐘賞 gloss: size=20 (was default 20.5); body line '部門にノミネー' right overflow +2.8px -> 0 (boxtitle + creambox) [D5-new].
- P8: extract 150/150; compare CLEAN (missing=[], extra=0; [108] present in both core and edition — no D28 discrepancy in this family). Lines 185 -> 185 (unchanged); footer slack 48.9px.
- Gates: 18 GATE PASS, 0 hard FAIL, 1 REFLOW (gate 15a text.md: D5 reflow moves line breaks only, difflines=24, char-multiset diff 0, native verifier ADOPT; coordinator adjudication requested). Gate 15a print=web PASS (multiset 0). Gate 15b rc=1 (see KIT D5 record for the D27 acceptance / pt tool gap). Gate 15c native verifier PASS (ADOPT). D18 masthead gap 42.0px PASS.
- text.md: joined patched export `logs/2026-w43-zh-tw-ja/2026-w43-zh-tw-ja.text.md.new` (joiner `scripts/textexp_zh_tw_d5.py`); ships new with the bundle (issues/ holds no `.text.md`).
- Logs: `scratch-2026-w43-zh-tw/logs/2026-w43-zh-tw-ja/` (`gates.log`, `GATES-SUMMARY.txt`, `run-patched.log`, `render-patched.log`, `rebuild-patched.log`).
