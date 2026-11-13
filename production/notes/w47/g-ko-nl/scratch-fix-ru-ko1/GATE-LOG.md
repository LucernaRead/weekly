# GATE-LOG — 2026-W47 ru-ko fix1 (proof1 D-1)

 fixer: subagent ru-ko fix1 · 2026-11-11 ~18:27–18:55 UTC
 All commands run from repo root `~/workspace/weekly-git` unless noted.
 Python: `tools/venv/bin/python`. No run.py / render.py / webpdf.py run.
 Artefacts (this dir): `p8-ru-ko.json`, `p8-compare.json`, `freeze-diff.json`,
 `check_appendix.py`, `dump_reg.py`, snapshots, backups, `.text.md.NEW`,
 `.text.md.GUARD`, `ru_textmd.py.FIXED`.
 Verdict column: PASS = gate green on the FINAL production text.md.

## G1. Opening SHA check — PASS
 `sha256sum` print/web/text.md at start:
 print `78e4442af8af9ec286c407ff66e08bac2029dd79d3ded43d1bfde3d555a6a400` (22,007,810 B)
 web   `3bf39ecf4fa4563458c68319ca42171642f9ad0be24650064faa9b7d9bd03195` (3,513,230 B)
 text  `d1feb40e417ba058d773a58ada62ad7fd7805b6a943599d8d017510b402d5a3d` (65,069 B)
 All three equal the brief's values — work proceeded.

## G2. Exporter regeneration (scratch) — PASS
 Fixed exporter → scratch `2026-w47-ru-ko.text.md.NEW`:
 `wrote … (65012 bytes, 150 exercises, 277 blocks)`.
 `diff` vs pre-fix backup: exactly 1 line (L836, long form → ✓ form).
 New L836: `150. ✓ 모범 답안은 이 면의 H란(97 단어)`.

## G3. Core guard (fixed exporter must reproduce core byte-identically) — PASS
 Fixed exporter on core-ru build dir → `2026-w47-ru-core.text.md.GUARD`
 (60,953 bytes, 150 exercises, 277 blocks).
 `cmp` vs shipped core text.md: BYTE-IDENTICAL.
 SHA both `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc`.
 Guard L836: `150. ✓ 范文见本版 H 区（97词）`.
 (First attempt failed with `ModuleNotFoundError: No module named 'bslib4'`
 because the script was invoked from scratch; re-ran with
 `PYTHONPATH=production/2026-w47/core-ru`. This is an invocation artefact
 of running from scratch, not a defect — the normal KIT invocation runs the
 script from inside the build dir. No core file was touched either way.)

## G4. P8 extract (tools/p8.py, printed P8 SVG) — PASS
 `tools/p8.py extract --p8 production/2026-w47/2026-w47-ru-ko/svg/p8-test.svg
  --total 150 --json p8-ru-ko.json`
 → `noted set = 150 of 150 (parse: lines)`.
 Q150 extracted key: `✓`; Q149: `B`; Q1: `8` (spot values).

## G5. P8 compare core vs ru-ko (tools/p8.py) — PASS
 `tools/p8.py compare --core-dir production/2026-w47/core-ru
  --edition-dir production/2026-w47/2026-w47-ru-ko --target ru --total 150`
 → `core 150 noted / edition 150 noted / status: CLEAN
     missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]`
 Identical status/keydiff to the pre-fix re-fanout gate (SVG untouched, as expected).

## G6. Appendix vs printed P8 keys, mechanical 150/150 (check_appendix.py) — PASS
 New production text.md appendix parsed (150 lines, contiguous 1–150;
 per-page counts P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38 —
 identical to core).
 For n=1..149: each appendix line starts with the P8-extracted key + ` — `.
 Q150: appendix line exactly `✓ 모범 답안은 이 면의 H란(97 단어)`,
 matching the P8-extracted key `✓`.
 Keys 1–149 identical to core appendix except the recorded translated
 sentence keys [137, 138, 139, 140] (same keydiff as G5, pre-existing).
 Q150 is ✓ form in BOTH ko and core appendices.
 Script exit 0: `ALL 150 APPENDIX LINES MATCH PRINTED P8 KEYS; …`
 (First run of the checker flagged Q137–140 as mismatches vs core; that was
 a checker error — those four keys are sentence answers translated into the
 reader language, the known keydiff. Checker corrected to allow exactly
 [137–140]; re-run exit 0.)

## G7. text.md vs print PDF P8 (pdftotext) — PASS
 `pdftotext -f 8 -l 8 -layout Lucerna-VOL4-ru-ko.pdf -`:
 contains `150. ✓ 모범 답안은 이 면의 H란(97 단어)` (1 hit, p.8 line 144).
 The print PDF already carried the ✓ form; the new text.md now agrees with it.
 (The P8 exercise stem `150. 쓰기` on the same page is the exercise itself,
 not an answer line — not a mismatch.)

## G8. Freeze diff core → ru-ko (tools/freeze.py, SVG text) — PASS (unchanged)
 `tools/freeze.py diff --core-svg production/2026-w47/core-ru/svg
  --edition-svg production/2026-w47/2026-w47-ru-ko/svg --json freeze-diff.json`
 Per-page +/− strings match the pre-fix re-fanout gate; totals:
 distinct added 451 / distinct removed 361.
 Cyrillic-bearing removed: 15 = Q46 `можно` ×1 (known legal) + 14
 Morozko-caption words (image skipped by design) — identical to the KIT
 re-fanout record, unexplained 0. (freeze diff has no text.md input; it is
 re-run here to confirm the SVG layer — and therefore the PDFs — is
 untouched. Added CJK 2,851 chars is the expected Korean explanation layer.)

## G9. PDFs unchanged — PASS
 Post-fix `sha256sum`:
 print `78e4442af8af9ec286c407ff66e08bac2029dd79d3ded43d1bfde3d555a6a400` (22,007,810 B)
 web   `3bf39ecf4fa4563458c68319ca42171642f9ad0be24650064faa9b7d9bd03195` (3,513,230 B)
 Both equal the opening values. Not rebuilt (no render/webpdf run).

## G10. Core untouched — PASS
 Core text.md SHA after all work:
 `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc`
 (equals the G3 guard value and the pre-work value).

## G11. Production zero-write (except text.md + KIT) — PASS
 42-file SHA snapshot, pre-fix vs post-fix: exactly 3 files differ:
 `2026-w47-ru-ko.text.md` (`d1feb40e…` → `5e9bd672…`),
 `WEEKLY-KIT.md` (`622f2c8f…` → `a84402fb…`),
 `ru_textmd.py` (`28a51c7e…` → `1b88b7f5…`).
 File list identical (no adds/deletes). No other edition/core/tools file touched.
 No commit, no push.

## G12. KIT §5 updated — PASS
 `WEEKLY-KIT.md` §5 line 57 now reads 65,012 bytes + SHA-256
 `5e9bd67201fd232aff598e0bbb487ba45821878e533392bc6e749444b090bffe`,
 150 exercises, 277 blocks, with fix1 pointer to §7; §7 carries the Fix 1
 bullet. PDF SHA/size lines in §5 unchanged (values still correct).

## Overall
 G1–G12 all PASS. Remaining step (out of this fixer's scope): independent
 re-proof of the fixed edition, to be dispatched separately.
