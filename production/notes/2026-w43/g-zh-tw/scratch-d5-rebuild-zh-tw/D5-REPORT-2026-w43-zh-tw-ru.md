# D5-REPORT — 2026-w43-zh-tw-ru (W43 zh-tw, D5 rebuild 2026-11-14)

- Reader: ru (mode ru/TC); `_D5_READER = "ru"`. Core: `2026-w43-zh-tw-en` (built from `production/2026-w43/core-zh-tw/`).
- Install: hand-ported `d5_port_zhtw.py` (installer FATALs on the face= engine) + `install_zhtw.sh` (`--check` first). Routing unit test FAILURES: 0. fix2 markers 5, `_QUOTE_CLS` 4, retained.
- §1.1 assembly: port engine (490 lines) copied into production (SHA-verified vs MANIFEST-W43.md) + pilot moth into `assets/` (production never held the port engine).
- Baseline (10/10 CLEAN family-wide): TOTAL 150, 0 warnings; print PDF bytes/SHA == MANIFEST; web < 7 MB; print-vs-web pdfdiff IDENTICAL; web-vs-issued pdfdiff IDENTICAL; p8 extract 150/150; pre-D5 census D5_latin_in_cjk=196, D5_cyrillic_in_cjk=283, curly_in_cjk=0.
- Rebuild: run TOTAL 150, 0 warnings; render RC=0; webpdf RC=0; print 29,575,205 B sha256 `86e3c27ead7415a3a8d7a79271cbe5e00b73cc15db57e58fdf28cda88e9b81d1`; web 3,286,327 B sha256 `7517b2ed87b3c1c24eab0b897744858f50fe25e7bd0d0d56f58da3bc842f512c`.
- Fixes (point sizes only, zero wording changes; full re-render + full gates after each):
  - `content12.py:112` — P2 f.box title '練習例子　Пример для тренировки': tsize=22 (was default 23); title right overflow +8.5px -> 0 (boxtitle + creambox) [D5-new].
- P8: extract 150/150; compare CLEAN (missing=[], extra=0; [108] present in both core and edition — no D28 discrepancy in this family). Lines 206 -> 206 (unchanged); footer slack 46.1px.
- Gates: 18 GATE PASS, 0 hard FAIL, 1 REFLOW (gate 15a text.md: D5 reflow moves line breaks only, difflines=150, char-multiset diff 0, native verifier ADOPT; coordinator adjudication requested). Gate 15a print=web PASS (multiset 0). Gate 15b rc=1 (see KIT D5 record for the D27 acceptance / pt tool gap). Gate 15c native verifier PASS (ADOPT). D18 masthead gap 42.0px PASS.
- text.md: joined patched export `logs/2026-w43-zh-tw-ru/2026-w43-zh-tw-ru.text.md.new` (joiner `scripts/textexp_zh_tw_d5.py`); ships new with the bundle (issues/ holds no `.text.md`).
- Logs: `scratch-2026-w43-zh-tw/logs/2026-w43-zh-tw-ru/` (`gates.log`, `GATES-SUMMARY.txt`, `run-patched.log`, `render-patched.log`, `rebuild-patched.log`).
