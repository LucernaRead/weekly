# FIX REPORT — W46 KO family, Round 1 verdict fixes (fix worker, 2026-11-03)

Issue: VOL.3, dated Mon 2026-11-09 – Sun 2026-11-15. Scope: all 11 KO-target editions
(`2026-w46-ko-de, -en, -es, -fr, -it, -ja, -nl, -pt, -ru, -zh-cn, -zh-tw`).
Seed record (from the proofreader, not re-derived): 150 exercises (A2 51 / B1 72 / B2 27);
per-page 10/18/18/18/18/18/12/38.

Authority: `hidden_files/w46/ko-proofread-gates/proofreader-verdict-round1.md`.
This worker fixed ONLY the verdict's defects, at the source, then fully re-rendered and
re-ran all gates. No other content was changed. Observations O1–O8 were left untouched;
W45-promise wording untouched. A Round 2 independent proofread follows; re-gating does
not replace it. Work was local only: nothing pushed, nothing inserted, no Discord post,
no `index.json` edit, no hand-edited SVG/PDF. `.text.md` files were regenerated from the
source manuscripts via `textmd.py`, never hand-edited or extracted from PDF.

## ⚠️ DISCREPANCY FLAG — read before adjudicating D2 (for the coordinator / Round 2 proofreader)

The verdict's D2 evidence states the stem `가늘` occurs nowhere in the issue except the
gloss line itself, having searched `가늘` and the stems `가는, 가늘게, 가느다란, 얇`
(all 0). Pre-fix verification by this worker CONTRADICTED that evidence on one point:
the verdict's stem list does not cover the attributive inflection **`가늰`**, which is a
different syllable at codepoint level and therefore invisible to a `가늘` substring
search (verified by Python codepoint dump 2026-11-03: `가늘` = 가 U+AC00 + 늘 U+B298;
`가늰` = 가 U+AC00 + 늰 U+B2B0; `'가늘' in '가늰'` is `False`).

Pre-fix counts from the rendered SVGs, all 11 editions identically:

| form | per edition | locations |
|---|---|---|
| `가늘` | 1 | P3 gloss line itself |
| `가늰` | 3 | P3 body ×1 (`길고 가늰 과자를 친구와 나누는`, `content34.py:23`); P5 ×2 (`content56.py:32` body paragraph and `:74` exercise stem) |

The core KIT's gloss adjudication (`가늘다 → 가늰` legitimate) and `check_gloss.py`'s stem
logic are consistent with `가늰` being a real occurrence of the headword.

**Decision:** the prescribed deletion was applied exactly as ordered by the parent task,
because the task explicitly ordered it and Round 2 follows. Post-fix, `가늘` = 0 is
achieved in every edition while `가늰` remains 3× per edition. The deletion must NOT be
presented as proof the word never occurred in inflected form. Whether to keep the
deletion or restore the gloss is for the coordinator / Round 2 proofreader to adjudicate.
This flag is recorded in all 11 KITs.

## D2 — BLOCKING, frozen core, all 11 editions: delete the orphan `가늘다` gloss entry

Location: P3 (`p3-munhwa.svg`), gloss box under the "당신은?" prompt.

### Source files edited

The P3 gloss line lives in `content34.py` in each of the 11 build dirs
(`hidden_files/weekly-report-w46-ko-build/` for the core, `hidden_files/weekly-report-w46-ko-<lang>-build/`
for the 10 fan-outs — the fan-out `content*.py` files already contain the translated
explanation layer, so the fix had to be applied in all 11, not only the core).
The same deletion was applied to both sides of the corresponding pair in all 10
`supp_*.py` record files (core-source string and native string; record only, not
executed at build time — verified by grep that nothing imports/applies `supp_*.py` or
`transform-w45.py` at build time). Core `check_core.py`'s P3 hand list had `"가늘"`
removed from `["겹치", "가늘", "감사", …]` so the check mirrors the new gloss set.

### Before / after (one occurrence each; the `가늘다` entry and its native equivalent deleted, nothing else touched)

| edition | before | after |
|---|---|---|
| zh-cn (core) | `译注｜겹치다 重叠 · 가늘다 细 · 감사하다 感谢 · 나누다 区分、分享。` | `译注｜겹치다 重叠 · 감사하다 感谢 · 나누다 区分、分享。` |
| de | `겹치다 = sich überschneiden · 가늘다 = dünn · 감사하다 = danken · 나누다 = unterscheiden, teilen` | `겹치다 = sich überschneiden · 감사하다 = danken · 나누다 = unterscheiden, teilen` |
| en | `겹치다 = to overlap · 가늘다 = thin · 감사하다 = to thank · 나누다 = to tell apart, to share` | `겹치다 = to overlap · 감사하다 = to thank · 나누다 = to tell apart, to share` |
| es | `겹치다 = coincidir, solaparse · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, compartir` | `겹치다 = coincidir, solaparse · 감사하다 = agradecer · 나누다 = distinguir, compartir` |
| fr | `겹치다 = se chevaucher · 가늘다 = fin · 감사하다 = remercier · 나누다 = distinguer, partager` | `겹치다 = se chevaucher · 감사하다 = remercier · 나누다 = distinguer, partager` |
| it | `겹치다 = sovrapporsi · 가늘다 = sottile · 감사하다 = ringraziare · 나누다 = distinguere, condividere` | `겹치다 = sovrapporsi · 감사하다 = ringraziare · 나누다 = distinguere, condividere` |
| ja | `겹치다 = 重なる · 가늘다 = 細い · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う` | `겹치다 = 重なる · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う` |
| nl | `겹치다 = samenvallen · 가늘다 = dun · 감사하다 = bedanken · 나누다 = onderscheiden, delen` | `겹치다 = samenvallen · 감사하다 = bedanken · 나누다 = onderscheiden, delen` |
| pt | `겹치다 = sobrepor-se · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, partilhar` | `겹치다 = sobrepor-se · 감사하다 = agradecer · 나누다 = distinguir, partilhar` |
| ru | `겹치다 = совпадать · 가늘다 = тонкий · 감사하다 = благодарить · 나누다 = различать, делиться` | `겹치다 = совпадать · 감사하다 = благодарить · 나누다 = различать, делиться` |
| zh-tw | `譯注｜겹치다 重疊 · 가늘다 細 · 감사하다 感謝 · 나누다 區分、分享。` | `譯注｜겹치다 重疊 · 감사하다 感謝 · 나누다 區分、分享。` |

No word was added to body text. Post-edit source check: `grep -rn "가늘"` over all
`*.py` in all 11 build dirs returned no matches (an earlier broad grep hit was stale
`__pycache__` bytecode only).

### Verification

- `가늘` = 0 in all 8 SVGs and in the `.text.md` of every edition (11/11).
- Remaining gloss entries intact and correctly punctuated in all 11 (full wrapped
  gloss text extracted from each `p3-munhwa.svg`; e.g. core
  `译注｜겹치다 重叠 · 감사하다 感谢 · 나누다 区分、分享。`,
  zh-tw `譯注｜겹치다 重疊 · 감사하다 感謝 · 나누다 區分、分享。`).
- P3 visually checked at full frame in all 11 editions: shortened gloss inside its box,
  no overflow, overlap, or missing glyphs; the body line `길고 가늰 과자` remains
  visible (consistent with the discrepancy flag above).
- No layout shift: SVG SHA-256 comparison vs `pre-fix-inventory.log` shows ONLY
  `p3-munhwa.svg` changed in 10 editions (zh-tw: P3 + P6). Core P3 vs the Round 1
  freeze-baseline copy: 182 text nodes both, zero moved nodes; only the 2 gloss lines
  re-wrapped at identical coordinates (y=1355.45, y=1385.175).
- `가늰` remains 3× per edition (flagged, not hidden — see § Discrepancy flag).

## D1 — BLOCKING, zh-tw only: Simplified `规` → Traditional `規` on P6

Location: `weekly-report-w46-ko-zh-tw/svg/p6-gipi.svg`, gloss line.

### Source file edited

`hidden_files/weekly-report-w46-ko-zh-tw-build/content56.py:125` (the Simplified gloss
was in the zh-tw source directly; `supp_zh_tw.py` had no entry for that line, and
`transform-w45.py:107` covers a different gloss line, not this one).

- Before: `譯注｜재다 衡量 · 규모 规模 · 섞다 混淆。`
- After: `譯注｜재다 衡量 · 규모 規模 · 섞다 混淆。` (`规` U+89C4 → `規` U+898F,
  verified at codepoint level; `规` = 0 in all 8 zh-tw SVGs post-fix).
- Record entry added to `supp_zh_tw.py` (record only): the before/after pair above,
  with a D1-fix comment. Remaining `规模` occurrences in the zh-tw build are only
  inside record files (`transform-w45.py:107,207` source sides and the new
  `supp_zh_tw.py` source side), not in rendered content.

### Verification — expanded Simplified-only scan (zh-tw)

Method: OpenCC `s2t` (reimplemented `opencc` in the tools venv) over every CJK char
in zh-tw SVG `<text>` elements; script `/tmp/scan_simp.py` (pre-fix log
`pre-fix-zh-tw-simp-scan.log`, post-fix log `post-fix-zh-tw-simp-scan.log`).
Pre-fix: 3 distinct candidates — `准` U+51C6 ×1, `峰` U+5CF0 ×8, `规` U+89C4 ×1.
Post-fix: **2 candidates remain, both adjudicated non-defects** —
`准` U+51C6 ×1 (P8 `准考證`, standard Traditional term) and `峰` U+5CF0 ×8
(e.g. `高峰`, identical in both scripts per the proofreader's adjudication).
**`规` = 0.** No other Simplified-only characters remain anywhere in the zh-tw edition.
P6 visually checked at full frame: gloss box reads
`譯注｜재다 衡量 · 규모 規模 · 섞다 混淆。`, inside the box, no overflow.

## Re-render

Sequential `run.py` → `render.py` → `webpdf.py` (via `tools/webpdf.py` only) for all
11 editions; combined log `render-all.log`, per-edition logs under `render-logs/`.
Every run log: TOTAL 150, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38;
**0 FLOW OVERFLOW / HEAD TOO WIDE warnings** in any log; all exits 0.

`.text.md` regeneration: core `textmd.py` run per edition with the title derived from
each existing header (first line minus one leading `# `), headers byte-identical to
pre-fix (first 4 lines asserted). Item counts unchanged (338, except ja 339, ru/zh-tw
340 — same as Round 1). Diff vs the pre-fix exports is ONLY the fixed gloss line(s):
the P3 gloss line in all 11, plus the P6 gloss line in zh-tw. Backups of the pre-fix
exports: `textmd-backup/`.

## Re-gates (final artifacts)

Gate artefacts: `gates/` (freeze + occlusion + p8 JSONs/logs), `counts/` (proofreader
part1/part2 scripts re-run with the output dir redirected here — outputs byte-identical
to Round 1 where the fix should not change them), `koscan-*.log`.

| gate | result |
|---|---|
| Freeze baseline (core) | 8/8 SVGs byte-identical |
| Freeze diffs | Latin/Cyrillic editions: 0 added CJK/Hangul. ja: +2,662 CJK-range / 0 Hangul (Round 1: 2,664; the −2 is the deleted gloss entry leaving the core multiset — 3 Hangul syllables + 细 — so the ja added-set shrinks by 2; no new Hangul added). zh-tw: +903 CJK / 0 Hangul, unchanged from Round 1 (P6 `規` +1, P3 `細` −1). pt: +8 Hangul = the adjudicated quoted sentence (`어울요에났서만`). |
| p8.py | CLEAN 150/150 in all 11; keydiff `[137, 138]` except zh-tw `[]` — exactly the Round 1 pattern. (First compare invocation used `--target <edition>` and failed with FileNotFoundError; the tool's `--target` is the TARGET language code — re-run with `--target ko`, all exit 0. The failed invocation's logs were overwritten by the correct re-run; the rerun log is `gates/p8-rerun.log`.) |
| Occlusion audit | 0 flags in all 11; selftest OK (all 6 planted classes fired, clean controls silent). |
| Counts re-measured | 150, A2 51 / B1 72 / B2 27, per-page as seed record; `exercise-counts.json` and `exercise-counts-v2.json` byte-identical to Round 1. |
| Kinsoku | 0 in all 11; `kinsoku.json` identical to Round 1. |
| Reader-facing sweep | Identical to Round 1 (`reader-facing-sweep.json` identical; residual hits are the adjudicated classes, e.g. Korean body text / P8 native-language answers). |
| Koscan | TRUE_SPLITS=0, S3=0 in all 11 (CANDIDATES 290–311). **Provenance gap:** the Round 1 koscan script was not preserved (only its logs: core CANDIDATES=289 TRUE_SPLITS=0 S3=0). The reconstruction (`koscan_reconstruct.py`, preserved here) implements the verdict criterion from the logs. Its first version false-flagged 1 candidate per edition (`두산에` + `4대` on P4) by stripping the digit from `4대` and fusing it into `두산에대`; the source is `두산에\n4대 1로 승리` — an explicit wrap point, not a mid-word split. The script was corrected to require pure-Hangul fragments and re-run: 0 true splits. The correction is documented in the script header. |
| Web PDFs | 8 pages each, all ≤ 7 MB, `pdftotext` bytes > 0 (see inventory). Print PDFs 8 pages each. |
| Builder diagnostics (not proofreader gates) | Core `check_core.py` exit 0 (18 gloss-occurrence fails, same stem-match diagnostic class as pre-fix; 0 involving `가늘`). Core `check_gloss.py`: 13 GLOSS-MISS diagnostics (headwords occurring only inflected, e.g. `피곤하다`, `재다`); 0 involving `가늘`. These diagnostics pre-date the fix and were not cited as defects by the proofreader; the fix removed `가늘` from the checked set and created no new fails. |

## Final per-edition file inventory

| edition | `.text.md` bytes (items) | web PDF (bytes / pdftotext bytes) | print PDF bytes |
|---|---|---|---|
| zh-cn (core) | 27,432 (338) | `Lucerna-VOL3-web.pdf` 2,527,990 / 50,748 | 32,010,944 |
| de | 28,107 (338) | `Lucerna-VOL3-web.pdf` 2,317,063 / 53,304 | 32,910,937 |
| en | 27,939 (338) | `Lucerna-VOL3-EN-web.pdf` 2,292,678 / 52,460 | 32,290,628 |
| es | 28,244 (338) | `Lucerna-VOL3-ES-web.pdf` 2,297,481 / 54,053 | 32,467,501 |
| fr | 28,268 (338) | `Lucerna-VOL3-FR-web.pdf` 2,305,526 / 54,157 | 32,498,888 |
| it | 28,219 (338) | `Lucerna-VOL3-IT-web.pdf` 2,288,426 / 53,493 | 32,463,283 |
| ja | 28,230 (339) | `Lucerna-VOL3-web.pdf` 2,661,269 / 53,820 | 36,156,571 |
| nl | 28,089 (338) | `Lucerna-VOL3-NL-web.pdf` 2,290,981 / 53,168 | 32,464,167 |
| pt | 28,247 (338) | `Lucerna-VOL3-web.pdf` 2,300,931 / 53,676 | 32,468,910 |
| ru | 30,314 (340) | `Lucerna-VOL3-RU-web.pdf` 2,243,230 / 61,377 | 30,826,972 |
| zh-tw | 27,513 (340) | `Lucerna-VOL3-ZHTW-web.pdf` 2,654,260 / 50,895 | 32,053,910 |

All web PDFs: 8 pages, ≤ 7 MB. All editions: 8 SVGs + 8 cards + print PDF + web PDF + `.text.md`.

## Fixes NOT applied as specified

None. Both defects were fixed exactly as the verdict specified. The single caveat is
the `가늰` discrepancy flag above: the D2 deletion was applied as ordered, but the
verdict's evidence for it is incomplete (the `가늰` inflection was not covered by its
stem search). Adjudication belongs to Round 2.

## Records

- Fix record appended to all 11 `WEEKLY-KIT.md` files (defect/fix quotes, re-gate
  evidence, discrepancy flag).
- Artefacts under `hidden_files/w46/ko-fix/`: `pre-fix-inventory.log`,
  `pre-fix-zh-tw-simp-scan.log`, `post-fix-zh-tw-simp-scan.log`, `apply_fixes.py`
  (edit script, asserted exact counts), `render-all.log`, `render-logs/`,
  `textmd-regen.log`, `textmd-backup/`, `run-gates.sh`, `gates-run.log`,
  `gates/`, `counts/`, `koscan_reconstruct.py`, `koscan-*.log`, this report.
