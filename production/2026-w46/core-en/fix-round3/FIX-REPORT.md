# FIX-REPORT — Lucerna Weekly W46, EN family, Round 3 proofread fixes (R-B6 + R-M4)

- Issue: VOL.3, Mon 2026-11-09 – Sun 2026-11-15. Target English, 3 editions fixed: 2026-w46-en-zh-tw, 2026-w46-en-es, 2026-w46-en-fr.
- Authority: `hidden_files/w46/en-proofread-gates-round2/proofreader-verdict-round2.md` (Round 2 FAIL, 3 editions blocked; §4 R-M4, §5 R-B6, §10 Round 3 fix list, §11 answer-key audit). SOP: `files/weekly-report-SOP.md`.
- Worker: fix worker (subagent), 2026-11-03 UTC. No proofreading was done; only the verdict's two listed residual defects were fixed, at the source, with full re-renders. The other 8 editions (core, de, it, ja, ko, nl, pt, ru) PASSED Round 2 and were NOT touched. A Round 3 independent proofread follows — this report's re-gating does not replace it.
- Method: every change went through a build source file (`hidden_files/weekly-report-w46-en-<native>-build/`). No rendered SVG/PDF was hand-edited. The three editions were fully re-rendered from source, sequentially, one at a time (`build_one_en_r3.sh`, mirroring Round 1's `build_one_en.sh` with logs redirected here: run.py → render.py → tools/webpdf.py → canonical `hidden_files/w46/en_textmd.py`). All gate tools are the shared toolkit under `tools/`; no hand-rolled equivalents for the gates. Simulation/measurement scripts in this directory use each build's own `svglib` font metrics.
- Evidence in this directory (`hidden_files/w46/en-fix-round3/`): per-edition build logs (`<ed>-{run,render,webpdf,textmd}.log`, `<ed>-build-driver.log`), `sim_bridge_pre.py` + `sim_bridge_pre.log` + `sim_bridge_post.log` (bridge wrap, real wrap function), `measure_titles_round3_pre.py/.log` + `measure_titles_round3_post.py/.log` (title-slot measurement), freeze JSONs/logs (`freeze-<ed>.json/.log`), P8 JSONs/logs (`p8-<ed>.json/.log`), occlusion JSONs/logs (`occlusion-<ed>.json/.log`), rowcheck logs (`rowcheck-<ed>.log`), `verify_round3_texts.py` + `r2r3-multiset-diff.log` (Round 2 → Round 3 SVG-text multiset diff + text.md Answers counts), `regcheck_dump.py` + `registry-recheck.json/.log` (registry recount from a scratch copy of the core build), `pdf_checks.log`, visual crops (`crops/`), PASS-edition hash snapshot + verification (`pass-editions-before.sha256`, `pass-editions-after-check.log`), target-edition hash snapshot + changed-file list (`target-editions-before.sha256`, `target-changed-files.txt`), KIT section sources (`kit-section-<ed>.md`).

## 1. Fixes applied (before → after, with source)

### R-B6 — zh-tw only (BLOCKING). P2 `B · WILL` bridge, punctuation-only final line.

- Source: `hidden_files/weekly-report-w46-en-zh-tw-build/content12.py:256`, `e.expl(...)` (bridge: 20.5pt sans, 434px column — `expl()` → `para()`, `bslib4.py` CW=434).
- Before (Round 1 fix, as rendered in Round 2): `用 will + 動詞原形來改寫（承諾與將要發生的事）。`
  Rendered, 2 lines: `[p2-life#160 x=527 y=2037.5] 用 will + 動詞原形來改寫（承諾與將要發生的事` + `[p2-life#161 x=527 y=2067.225] ）。` — the second line contained only `）。` at the left margin.
- After (verdict's 1-line text; the 2-line alternative was NOT used): `用 will + 動詞原形改寫，承諾與將要發生的事。`
  Keeps the praised `動詞原形` clarification and the full meaning; drops only `來` and the parentheses.
- Simulation (real wrap, zh-tw build's TC svglib, `sim_bridge_pre.py`/`sim_bridge_post.log`): the current text reproduces EXACTLY as 2 lines (line 1: 427.9px `用 will + 動詞原形來改寫（承諾與將要發生的事`; line 2: 41.0px `）。`); the core bridge control wraps as 1 line (407.4px); the new text wraps as 1 line, 427.9px in the 434px box (6.1px spare). The verdict's alternative (`用 will + 動詞原形來改寫，表達承諾與將要發生的事。`) simulates as 2 lines ending `的事。` (61.5px) and was not needed. All other candidates in the verdict's `verify2-bridge-cands.log` reproduce identically under the same wrap (c 366.4px 1 line; d 407.4px 1 line; f 366.4px 1 line).
- Verification: rendered as a single `<text x="527" y="2037.5" font-size="20.5">用 will + 動詞原形改寫，承諾與將要發生的事。</text>` element; no lone-`）。` element remains on P2. Visually confirmed at full frame on the P2 card and in a 2× crop of the bridge (`crops/r3-b6-zh-tw-p2-bridge.png`): one bridge line ending `。`, exercise 16 directly below, no second line.
- KIT correction: the zh-tw `WEEKLY-KIT.md` Round 1 B6 line said the bridge "now ends `）。`" — that misdescribed the render (as printed, `）。` was a standalone second line, not a line ending). The line is corrected in place (CORRECTION note citing the Round 2 element coordinates) and the Round 3 record below it states the correction again. The misreading is not repeated anywhere in this report.

### R-M4 — es + fr (BLOCKING). P3 box titles lack the English head.

- Source: `content34.py:81` (`v3.box(...)`, same slot as all P3 titles) in each fan-out build dir. No layout change was made or permitted.
- es before: `LA NOCHE DE SCROOGE` (`[p3-culture#160]`) → after: `SCROOGE'S NIGHT · La noche`. Same pattern as the fixed nl/pt titles.
- fr before: `LA NUIT DE SCROOGE` (`[p3-culture#159]`) → after: `SCROOGE'S NIGHT · La nuit`. Same pattern as the fixed nl/pt titles.
- Measurement (each edition's own svglib, sans bold 23pt, slot 416.0px = box x=1451 w=434, title x=1469; pre-fix `measure_titles_round3_pre.log`, post-fix rendered-SVG `measure_titles_round3_post.log`): es new title 345.9px, fits (spare 70.1px), rendered ink right edge 1815.0px vs box edge 1885; fr new title 322.7px, fits (spare 93.3px), ink right edge 1792.0px. Fuller forms overflow and were not used (es full mixed 476.2px; fr full mixed 452.9px). Shipped nl/pt controls reproduce exactly (nl 409.8px, pt 323.2px).
- Verification: each title renders as a single `<text x="1469" y="873" font-size="23" font-weight="700">` element. Visually confirmed at full frame on both P3 cards: titles inside their boxes with clearance. Occlusion audit BOXTITLE class silent (0 flags overall).
- KIT records: the es/fr KITs did not record the P3-title defect (their Round 1 records carried only an out-of-scope OBSERVATION). Round 3 fix records are appended to both KITs (see §4); the OBSERVATION bullets are left as Round 1 history.

## 2. Deliberately NOT changed

- Answer keys: no registry change, no key work (Round 2 §11: 150/150 semantically correct, letters identical in all 11 editions; the defect class is absent from the EN family). P8 keydiff `[137, 138, 139, 140, 150]` remains the legitimate translation/pointer set in all three editions.
- The B1-shortened-forms and M4-short-glosses deviations (ACCEPTABLE as printed, Round 2 §3).
- The FR masthead at 42pt.
- The ko P2 bridge sub-S3 break (observation O-R2-2, NOT a defect, NOT a fix item) — ko untouched in any case.
- The core/de `.text.md` exporter format (documented, accurate).
- Anything in the 8 PASS editions (see §5).

## 3. Build log summary (3 editions: 0 warnings, TOTAL 150)

| Edition | run.py | render.py (print PDF bytes) | webpdf.py (bytes / text bytes) | text.md (150 ex.) |
|---|---|---|---|---|
| zh-tw | exit 0, 0 overflow, TOTAL 150 | exit 0, 8 cards, print 24,611,412 | 2,204,231 / 44,900 | 43,589 bytes (stat) |
| es | exit 0, 0 overflow, TOTAL 150 | exit 0, 8 cards, print 15,187,863 | 1,552,611 / 46,205 | 45,881 bytes (stat) |
| fr | exit 0, 0 overflow, TOTAL 150 | exit 0, 8 cards, print 15,263,495 | 1,557,939 / 49,197 | 45,884 bytes (stat) |

Text.md regeneration: canonical `hidden_files/w46/en_textmd.py` from each edition's own build source (never hand-edited, never extracted from PDF); headers preserved verbatim (first 6 lines identical across editions, reader label per edition). The exporter's own "bytes" figure is a character count; the sizes above are `stat` bytes. Each text.md Answers section: 150 entries, numbers 1–150 unique and complete (`r2r3-multiset-diff.log`).

## 4. Re-gate results on the FINAL artifacts (3 editions)

Gate JSONs/logs live in this directory. Freeze/p8/occlusion were re-run with the canonical tools; rowcheck is the supplementary `hidden_files/w46/rowcheck46.py` used in Rounds 1–2.

| Edition | freeze diff vs core (exit 0) | p8 compare --target en --total 150 (exit 0) | occlusion (selftest OK) | rowcheck (COLLIDE / MISMATCH / GRAZE) |
|---|---|---|---|---|
| es | TOTAL added CJK 0 | CLEAN 70→70, missing [], uncertain [], keydiff [137,138,139,140,150] | 0 flags | 0 / 0 / 0.0% |
| fr | TOTAL added CJK 0 | EXTRA_ONLY 70→150, extra 80 (adjudicated list, identical to Round 2), missing [], uncertain [], keydiff [137,138,139,140,150] | 0 flags | 0 / 0 / 0.0% |
| zh-tw | TOTAL added CJK 680 (unchanged from Round 2; all Traditional Han explanation layer) | CLEAN 70→70, missing [], uncertain [], keydiff [137,138,139,140,150] | 0 flags | 0 / 0 / 0.0% |

Notes:
- P8: the first invocation without `--target` failed with a usage error (rc=2, no JSON written); the authoritative invocation is `--target en --total 150` (the default `--target en` alone uses the stale total 149 — see verdict §7). The re-run results above are from the correct invocation and match Round 2 exactly per edition (es CLEAN, fr EXTRA_ONLY, zh-tw CLEAN).
- Counts re-measured: registry re-dumped from a scratch copy of the untouched core build (SVGs redirected to `regcheck-svg/`, registry to `registry-recheck.json`; the shipped `hidden_files/w46/en-core/registry.json` was NOT overwritten): 150 exercises, numbers 1–150 unique, no missing/dup, all keyed; per-page 10/17/18/18/18/18/12/39; levels A2 60 / B1 69 / B2 21; byte-identical to the shipped registry snapshot. Seed record confirmed, not re-derived.
- Change confinement (Round 2 → Round 3 SVG-text multiset diff, page + text, positions ignored; `r2r3-multiset-diff.log`): es exactly 1 string changed (P3 title); fr exactly 1 string changed (P3 title); zh-tw exactly 2 lines → 1 line (the P2 bridge). No other string changed in any page of any edition.
- PDF checks (`pdf_checks.log`): every web PDF 8 pages (`pdfinfo`), ≤ 7 MB, `pdftotext` bytes > 0 and EQUAL to the print-PDF extraction per edition (es 46,205; fr 49,197; zh-tw 44,900). Real text layer confirmed.
- Visual checks: every changed page at full frame — zh-tw P2 (bridge single line, no punctuation-only line), es P3 and fr P3 (new titles inside their boxes) — plus P1/P8 spot checks at full frame for all three editions (mastheads, Searches bars, footers, P8 answers blocks, FR 42pt masthead + M1 tail intact). No overflow, overlap, clipping, or orphan line seen. Crop evidence: `crops/`.

## 5. Final per-edition file inventory + untouched confirmation

Sizes in bytes (`stat`). "pdftotext bytes" = `pdftotext` stdout byte count, same method for web and print PDFs, equal for both per edition. Each edition dir holds 8 SVGs (`svg/`) and 8 cards (`cards/`), all re-rendered from source, plus `ABSTRACT.txt` (untouched in Round 3) and `WEEKLY-KIT.md` (Round 3 record appended).

| Edition | text.md | web PDF | print PDF | pdftotext bytes (web = print) |
|---|---|---|---|---|
| zh-tw `2026-w46-en-zh-tw` | 43,589 | 2,204,231 | 24,611,412 | 44,900 |
| es `2026-w46-en-es` | 45,881 | 1,552,611 | 15,187,863 | 46,205 |
| fr `2026-w46-en-fr` | 45,884 | 1,557,939 | 15,263,495 | 49,197 |

- 8 PASS editions untouched: SHA-256 snapshot of all 168 files in core/de/it/ja/ko/nl/pt/ru taken BEFORE any edit (`pass-editions-before.sha256`); re-verification after all work: 168/168 OK, 0 failures (`pass-editions-after-check.log`, `sha256sum -c` rc=0).
- Target-edition change confinement: vs the pre-fix snapshot, exactly 6 files changed per edition — the changed page's SVG + card, both PDFs, text.md, and WEEKLY-KIT.md (`target-changed-files.txt`). All other 7 pages' SVGs/cards are byte-identical after the full re-render.
- Build-source confinement: the only build files modified after the task-start marker (excluding `__pycache__`) are the three intended ones: `weekly-report-w46-en-zh-tw-build/content12.py`, `weekly-report-w46-en-es-build/content34.py`, `weekly-report-w46-en-fr-build/content34.py`.
- Nothing else was changed: `~/workspace/weekly-git` untouched (read-only status check: no changes), `index.json` untouched, no push, no insert, no Discord post, no chat dump. No subagents were spawned.

## 6. Files changed

Build sources (one exact-string edit each, occurrence-count asserted):
- zh-tw: `weekly-report-w46-en-zh-tw-build/content12.py:256` (R-B6).
- es: `weekly-report-w46-en-es-build/content34.py:81` (R-M4).
- fr: `weekly-report-w46-en-fr-build/content34.py:81` (R-M4).
- Edition files: all SVGs/cards/PDFs re-rendered (only the changed page differs per edition, §5); all 3 `<slug>.text.md` regenerated via the canonical exporter; all 3 `WEEKLY-KIT.md` (zh-tw B6 line corrected + Round 3 record appended; es/fr Round 3 R-M4 records appended). `ABSTRACT.txt` files untouched.
- Nothing else. No fix could not be applied: both verdict-specified fixes were applied exactly as specified (1-line bridge text; measured title swaps, no layout change).

## 7. Handoff to Round 3 proofread

- R-B6 and R-M4 are fixed at source and re-gated as above; the Round 3 proofread need only re-verify the three fixed items + the change-confinement diff. The other 8 editions' PASS stands (byte-verified untouched).
- The zh-tw KIT B6 misdescription is corrected; the es/fr KITs now record the P3-title defect and its fix.
- No new strings were introduced except the three fix strings, all measured/simulated and visually confirmed.
