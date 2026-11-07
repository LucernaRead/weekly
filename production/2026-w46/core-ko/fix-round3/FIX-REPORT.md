# FIX-REPORT — W46 KO family, Round 3 (fix worker)

- **Issue:** Lucerna Weekly VOL.3, dated Mon 2026-11-09 to Sun 2026-11-15.
- **Family / scope:** KO-target only — all 11 editions (reader-native de, en, es, fr, it, ja, nl, pt, ru, zh-cn, zh-tw; NO ko-ko edition exists). No other family touched.
- **Date of work:** 2026-11-03 (all times UTC in the preserved logs).
- **Trigger:** Round 2 independent proofread verdict (`hidden_files/w46/ko-proofread-gates-round2/proofreader-verdict-round2.md`): ROUND 2 FAIL, all 11 editions. D1 CONFIRMED. Keys 150/150 CONFIRMED. Gates clean. Three blocking frozen-core defects (R-GLOSS, D3, D4), all minor. This round fixes ONLY those three.
- **Work directory:** `hidden_files/w46/ko-fix-round3/` (this report, scripts, logs, gate outputs, pre-fix snapshot).
- **What was NOT done:** nothing was pushed, inserted, posted to Discord, or dumped into chat. `~/workspace/weekly-git` untouched; `index.json` untouched; the SOP untouched. A Round 3 independent proofread follows — the re-gating in §6 does not replace it.

## 1. The three defects and their fixes

All fixes were applied at the core/build sources (never SVG/PDF patches), then all 11 editions were fully re-rendered (`run.py` → `render.py` → `tools/webpdf.py`, sequential, one edition at a time; `.text.md` regenerated via the family's `textmd.py`). Fix script: `apply_fixes.py` — 43 edits, each with an exact-count (count==1) assertion; all passed. `__pycache__` cleared in all build dirs before re-render.

### R-GLOSS — restore the `가늘다` gloss entry in the P3 gloss line (all 11 editions)

Round 1's D2 deletion (based on the claim `가늘다` "occurs nowhere") is PARTLY REVERSED on the Round 2 proofreader's RESTORE ruling. The claim is refuted: `가늰` occurs exactly 3× per edition — P3 body `길고 가늰 과자를 친구와 나누는`, P5 body `길고 가늰 과자 한 상자를 건네며`, P5 exercise 69 option A `빼빼로데이에는 무엇을 나눠 줘요? A. 길고 가늰 과자` (P8 key 69 = A — item 69 TESTS the word). Codepoint fact: `가늘` (늘 U+B298) vs `가늰` (늰 U+B2B0); `'가늘' in '가늰'` is False, so a substring search misses it. `가늘다 → 가늰` is a ㄹ-irregular attributive an A2–B1 reader cannot derive by rule. The entry already fit pre-fix. This also resolves the Round 1 discrepancy flag recorded in the KITs (the stem DOES occur, as inflected `가늰`).

Sources changed (per edition): `content34.py` (the `f.gloss()` argument, without the prefix) + both sides of the `supp_*.py` record pair (core has no `supp` file) + the core `check_core.py` P3 hand list (`"겹치", "감사"` → `"겹치", "가늘", "감사"`, line 30). The D1 fix (Round 1) was NOT disturbed.

Restored gloss lines, verbatim as rendered (prefix + argument; verified byte-equal from the P3 SVG gloss band — see §4):

| Edition | Before (Round 1 form) | After (restored) |
|---|---|---|
| zh-cn (core) | `译注｜겹치다 重叠 · 감사하다 感谢 · 나누다 区分、分享。` | `译注｜겹치다 重叠 · 가늘다 细 · 감사하다 感谢 · 나누다 区分、分享。` |
| de | `HINWEIS · 겹치다 = sich überschneiden · 감사하다 = danken · 나누다 = unterscheiden, teilen` | `HINWEIS · 겹치다 = sich überschneiden · 가늘다 = dünn · 감사하다 = danken · 나누다 = unterscheiden, teilen` |
| en | `Note — 겹치다 = to overlap · 감사하다 = to thank · 나누다 = to tell apart, to share` | `Note — 겹치다 = to overlap · 가늘다 = thin · 감사하다 = to thank · 나누다 = to tell apart, to share` |
| es | `Nota — 겹치다 = coincidir, solaparse · 감사하다 = agradecer · 나누다 = distinguir, compartir` | `Nota — 겹치다 = coincidir, solaparse · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, compartir` |
| fr | `Note — 겹치다 = se chevaucher · 감사하다 = remercier · 나누다 = distinguer, partager` | `Note — 겹치다 = se chevaucher · 가늘다 = fin · 감사하다 = remercier · 나누다 = distinguer, partager` |
| it | `Nota — 겹치다 = sovrapporsi · 감사하다 = ringraziare · 나누다 = distinguere, condividere` | `Nota — 겹치다 = sovrapporsi · 가늘다 = sottile · 감사하다 = ringraziare · 나누다 = distinguere, condividere` |
| ja | `解説 — 겹치다 = 重なる · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う` | `解説 — 겹치다 = 重なる · 가늘다 = 細い · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う` |
| nl | `Uitleg — 겹치다 = samenvallen · 감사하다 = bedanken · 나누다 = onderscheiden, delen` | `Uitleg — 겹치다 = samenvallen · 가늘다 = dun · 감사하다 = bedanken · 나누다 = onderscheiden, delen` |
| pt | `Nota — 겹치다 = sobrepor-se · 감사하다 = agradecer · 나누다 = distinguir, partilhar` | `Nota — 겹치다 = sobrepor-se · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, partilhar` |
| ru | `Пояснение — 겹치다 = совпадать · 감사하다 = благодарить · 나누다 = различать, делиться` | `Пояснение — 겹치다 = совпадать · 가늘다 = тонкий · 감사하다 = благодарить · 나누다 = различать, делиться` |
| zh-tw | `譯注｜겹치다 重疊 · 감사하다 感謝 · 나누다 區分、分享。` | `譯注｜겹치다 重疊 · 가늘다 細 · 감사하다 感謝 · 나누다 區分、分享。` |

Occurrence counts after the fix (rendered SVGs, all 11 editions): `가늘` = 1 (the gloss entry only), `가늰` = 3 (unchanged body/stem occurrences). No other `가늘` occurrence exists anywhere in the rendered text.

### D3 — item 54 (P4): stem+key doubling

- Source: core `content34.py` line 219 (fan-outs inherit the identical Korean stem; fixed in all 11 build dirs). Key UNCHANGED.
- Before: stem `한국시리즈 시작이 하루 ___어요.` + key `밀렸어요` → reconstructs `하루 밀렸어요어요` (doubled ending; the sole fill item where the key ends with the stem's suffix).
- After: stem `한국시리즈 시작이 하루 ___.` + key `밀렸어요` → reconstructs `한국시리즈 시작이 하루 밀렸어요.` — verified correct in all 11 editions' rendered P4 extraction (see §4). The alternative (key → `밀렸`) was NOT used, per the proofreader's specified fix.

### D4 — item 103 (P7): quotative mismatch

- Source: core `content7.py` line 25 (fan-outs inherit the identical Korean stem; fixed in all 11 build dirs). Key UNCHANGED.
- Before: stem `미리 소금에 절인 배추를 ___이라고 해요.` + key `절임배추`. `배추` is vowel-final (추, no batchim), so the quotative must be `라고`; contrast item 101 `김장이라고` (장 is batchim-final, correct).
- After: stem `미리 소금에 절인 배추를 ___라고 해요.` + key `절임배추` → reconstructs `미리 소금에 절인 배추를 절임배추라고 해요.` — verified correct in all 11 editions' rendered P7 extraction (see §4).

## 2. Same-class sweep (mandatory)

Method (`sweep.py`, preserved in this directory; AST text-read of the build sources — content modules were never imported/executed standalone):

- (a) D3 class: every `.ex()` stem containing `___` (77 stems per edition; 0 multi-blank). Attached suffix = the Hangul run immediately after `___`. Flag iff the item's key endswith that suffix. Reconstruction verified for the flagged item.
- (b) D4 class: every quotative `이라고/라고` in exercise stems, reconstructed with the item's key and checked by the final syllable's batchim (jongseong = (ord − 0xAC00) % 28 ≠ 0 → `이라고`; vowel-final → `라고`). Longest-match handling: `이라고` preferred over `라고` (substring) to avoid double-counting. Plus ALL string literals containing `이라고/라고` in `content*.py`, checked against the preceding token. Stem identity across editions also checked (127 exercise stems per edition; Korean stems byte-identical across all 11 build dirs except the expected translation re-aims for items 137/138 and the item-150 writing-model note variants).

Complete candidate list (pre-fix run `sweep-pre.json`/`sweep-pre.log`; post-fix run `sweep-post.json`/`sweep-post.log`):

- **D3 doubling: exactly 1 candidate — item 54 only** (`content34.py:218`, key `밀렸어요`, suffix `어요`, reconstruction `하루 밀렸어요어요`). All other 76 blank stems: a suffix is present but the key does not end with it (e.g. item 19 `조심`+`하세요`, item 20 `좌우`+`한다고`). **Zero further candidates.**
- **D4 quotative stems: 3 total, exactly 1 mismatch — item 103 only** (`절임배추이라고`, 추 vowel-final). The other two are correct: item 34 `절정이라고` (정 batchim), item 101 `김장이라고` (장 batchim).
- **Quotative literals in prose: 7 total** = the 3 stems above (blank preceding token) + 4 prose usages, all correct or non-applicable:
  - `김장이라고` (`content7.py:17` body) — correct (장 batchim).
  - `예보 날짜라고` (`content12.py:41`) — correct (짜 vowel-final).
  - `'〜 전에 뭐 해요?'라고` (`content7.py:80`) — correct (ends 요, vowel-final).
  - `'D-7'이라고` (`content12.py:40`) — preceding token is non-Hangul `D-7`; the batchim rule is not directly applicable. NOT flagged as a defect; recorded here for Round 3 adjudication. NOT fixed in this round, per the task instruction to fix only D3/D4 and report further candidates without silently fixing them.
- **Zero further genuine candidates in either class.** Post-fix sweep: doubling flags 0; quotative stems 3, all correct; item 54 reconstructs `한국시리즈 시작이 하루 밀렸어요.`; item 103 reconstructs `미리 소금에 절인 배추를 절임배추라고 해요.`

## 3. Keys unchanged — proof

- `tools/p8.py compare --target ko`: CLEAN 150/150 in all 11 editions; keydiff `[137, 138]` in all fan-outs, `[]` in zh-tw (see §6).
- Per-edition key extraction (`tools/p8.py extract --total 150`) diffed pre-fix vs post-fix: **all 150 keys byte-identical in every edition** (identical key-dict hashes; noted sets identical; zero differing numbers). Keys 54 = `밀렸어요` and 103 = `절임배추` in all 11 editions, before and after. Evidence: `keydiff.py` / `keydiff.log`. (An earlier truncated console print made the JSON `p8` path fields look uniform; direct re-inspection confirmed each JSON carries its own edition's path and its own edition-specific keys 137/138.)

## 4. Rendered-text verification of the fixes

- **P3 gloss lines:** reconstructed from the P3 SVG gloss band (document-order nodes at the gloss anchor x, space-joined at wrap points) and verified byte-equal to the §1 table in all 11 editions (`gloss_check.py` / `gloss-check.log`: 11/11 MATCH). Wrap lines per edition are quoted in that log.
- **Items 54 / 103 / 69 from the rendered-SVG exercise extraction** (`gates/counts/exercises-all.json`, via `keydiff.py` output): in every edition, item 54 = `한국시리즈 시작이 하루 ___.` (P4), item 103 = `미리 소금에 절인 배추를 ___라고 해요.` (P7), item 69 unchanged with option A `길고 가늰 과자` (P5, key A). `___어요` is absent from all P4 renderings; `___라고` is present on all P7 renderings (item 101 legitimately uses `___이라고` on the same page).
- **P3 gloss-box geometry** (`gates/checks.json`): gloss lines inside their box in all 11 editions — core/zh-tw box y=1316.95 h=115.95, 2 lines; de/en/es/fr/it/ja/nl/pt box y=1346.675 h=145.675, 3 lines; ru y=1376.4 h=145.675, 3 lines; top margin 38.5, bottom margin 47.725 in all 11; occlusion 0.
- **D1 survives:** zh-tw `规` = 0; core retains `规` = 2 (expected). Expanded OpenCC s2t Simplified-only scan re-run on the final zh-tw SVGs (`zh_tw_simp_scan.py` / `zh-tw-simp-scan.log`): exactly 2 distinct candidates, both adjudicated non-defects — `峰` U+5CF0 ×8, `准` U+51C6 ×1. Zh-tw P6 gloss `譯注｜재다 衡量 · 규모 規模 · 섞다 混淆。` intact.
- **Core self-check:** `check_core.py` re-run on the final artifacts: exit 0; P7 phrases all verbatim; dates all True; gloss-occurrence diagnostics 19 (was 18 after Round 1) — the +1 is the restored `가늘` hand-list entry, a known naive-substring diagnostic of the same class as the other 18 (dictionary form vs inflected prose form, e.g. `막히`/`막혀`, `가늘`/`가늰`); the KIT adjudication of the `가늘다 → 가늰` pair stands. Log: `check_core-post.log`.
- **Visual:** P3 ×11 at full frame (restored gloss inside its box, no overflow/overlap, body line `길고 가늰 과자` visible); P4 (item 54) and P7 (item 103) at full frame in the core, plus spot checks de P4 and ja P7 (items 101/103 contrast visible). All clean.

## 5. Change isolation

- **Hash diff vs the pre-fix snapshot** (`pre-fix/inventory.log` vs `post-fix-inventory.log`): in EVERY edition exactly 9 files changed — `svg/p3-munhwa.svg`, `svg/p4-seupocheu.svg`, `svg/p7-mal.svg`, `cards/p3-munhwa.png`, `cards/p4-seupocheu.png`, `cards/p7-mal.png`, the print PDF, the web PDF, and the `.text.md`. All other SVGs/cards byte-identical.
- **SVG-text multiset diff** (`svg_multiset_diff.py` / `svg-multiset-diff.log`, pre-fix node extraction vs current SVGs): P1/P2/P5/P6/P8 identical in all 11 editions; the ONLY changed strings are the P3 gloss wrap lines (restored entry + wrap reflow), the P4 item-54 stem line, and the P7 item-103 stem line. Total +51/−47 nodes across 11 editions (wrap reflow only). **No other string changed anywhere.**
- **`.text.md` diffs:** exactly ONE line per edition vs the pre-fix export — the P3 gloss line (line 277, or 279 ja / 281 ru/zh-tw), restored entry only. Headers byte-identical; item counts unchanged (338 ×8 editions, 339 ja, 340 ru/zh-tw — same as pre-fix). Exercise stems do not appear in `.text.md`, so D3/D4 correctly produce no `.text.md` diff. Byte counts returned to pre-Round-1 values.
- **Source diff vs the pre-fix source snapshot** (`pre-fix/sources/`): only the expected lines changed — core 4 lines (gloss line 26 in `content34.py`, stem 54 line 219 in `content34.py`, stem 103 line 25 in `content7.py`, hand list line 30 in `check_core.py`); fan-outs = gloss + 2 stems + `supp` pair lines.

## 6. Re-gates on the final artifacts

All gates run on the final artifacts (script `run-gates.sh`, log `gates-run.log`; outputs under `gates/`). Render: 33/33 steps exit 0, all 11 editions TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE warnings (`render-all.log`, `render-logs/`).

| Gate | Result (all 11 editions unless noted) |
|---|---|
| Freeze (`tools/freeze_check.py`) | Core baseline 8/8 SVGs byte-identical, exit 0. Added CJK/Hangul vs core: Latin/Cyrillic editions 0; ja 2,664 (Round 2: 2,662; +2 = restored `細`, Hangul added 0); pt 8 Hangul (unchanged adjudicated quoted `서울에서 만났어요`); zh-tw 904 (Round 2: 903; +1 = restored `細`, Hangul added 0). No U+FFFD. |
| p8.py compare (`--target ko`) | CLEAN 150/150 in all 11; keydiff `[137, 138]` in all fan-outs, `[]` in zh-tw; core extract 150/150. |
| Occlusion audit (`tools/occlusion_audit.py`) | 0 flags in all 11 editions, all 88 pages; selftest OK (all 6 planted classes fired, clean controls silent). |
| Counts (`extract_exercises-round3.py`) | 138 blocks = 150 items, missing `[]`; TOTAL 150, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38 — identical in all 11. |
| Kinsoku | 0 in all 11. U+FFFD = 0 everywhere. |
| Koscan (`koscan-round3.py`, verbatim Round 2 script, tools/README standards: window 10–45px, same-column x within 30px, pure-Hangul fragments, source-word attestation) | TRUE_SPLITS=0, S3≥3=0, S3≤3=0, LINESTART=0 in all 11. CANDIDATES 357–362 (zh-cn 360, de 357, en 358, es 357, fr 361, it 359, ja 360, nl 358, pt 358, ru 362, zh-tw 361). ORPHANshort 10–11 per edition, identical adjudicated set as Round 2 (complete words/labels: P1 brief heads `예보/김장/단풍/야구`, P2 `필수`, P3 `물/간식`, P4 `삼성`, P6 `구분`, P7 `해요`, + zh-tw credit-wrap `사진`). |
| P6/P7 checks (`round3-checks.py`) | P6 comparison table 12/12 cells in all 11; P7 phrases 8/8 verified verbatim in articles AND on P7 in all 11; reader-facing sweep hits only adjudicated false-positive substrings (`core` in `coreano`, `encore`, `Score`); ABSTRACTs all single-line, no ASCII double quote, reader-native. |
| PDFs | All web PDFs 8 pages, ≤7 MB, pdftotext bytes > 0 and equal to the print-PDF pdftotext bytes (text layer present). See §7. |

## 7. Final inventory

| Edition | `.text.md` (bytes / items) | Web PDF (bytes / pdftotext) | Print PDF (bytes / pdftotext) |
|---|---|---|---|
| zh-cn (core) | 27,449 / 338 | `Lucerna-VOL3-web.pdf` 2,528,382 / 50,756 | 32,011,292 / 50,756 |
| de | 28,128 / 338 | `Lucerna-VOL3-web.pdf` 2,317,186 / 53,316 | 32,911,089 / 53,316 |
| en | 27,959 / 338 | `Lucerna-VOL3-EN-web.pdf` 2,292,773 / 52,452 | 32,290,743 / 52,452 |
| es | 28,264 / 338 | `Lucerna-VOL3-ES-web.pdf` 2,297,594 / 54,064 | 32,467,650 / 54,064 |
| fr | 28,287 / 338 | `Lucerna-VOL3-FR-web.pdf` 2,305,618 / 54,155 | 32,499,010 / 54,155 |
| it | 28,242 / 338 | `Lucerna-VOL3-IT-web.pdf` 2,288,549 / 53,507 | 32,463,409 / 53,507 |
| ja | 28,252 / 339 | `Lucerna-VOL3-web.pdf` 2,661,599 / 53,821 | 36,156,863 / 53,821 |
| nl | 28,108 / 338 | `Lucerna-VOL3-NL-web.pdf` 2,291,086 / 53,178 | 32,464,313 / 53,178 |
| pt | 28,267 / 338 | `Lucerna-VOL3-web.pdf` 2,301,018 / 53,675 | 32,469,019 / 53,675 |
| ru | 30,342 / 340 | `Lucerna-VOL3-RU-web.pdf` 2,243,389 / 61,396 | 30,827,141 / 61,396 |
| zh-tw | 27,530 / 340 | `Lucerna-VOL3-ZHTW-web.pdf` 2,654,630 / 50,903 | 32,054,373 / 50,903 |

All web PDFs 8 pages; all print PDFs 8 pages. Web PDFs built ONLY via `tools/webpdf.py`.

## 8. KIT records

A Round 3 fix record (defect/fix quotes, re-gate evidence, discrepancy-note resolution) was appended to all 11 `WEEKLY-KIT.md` files (append only; earlier sections untouched). Script preserved: `append_kit_records.py`.

## 9. Anything not applied / open for Round 3 adjudication

- **Nothing among the three assigned defects was left unapplied.** R-GLOSS, D3, D4 are all applied, re-rendered, and re-gated in all 11 editions.
- **One scanned usage reported, not fixed** (per instructions): the prose quotative `'D-7'이라고` (`content12.py:40`) — non-Hangul preceding token, batchim rule not directly applicable; listed in §2 for Round 3 adjudication. It is not counted as a defect candidate.
- **No other candidate** was found by the same-class sweep in either class, and no other string was changed. Any further judgement (including whether the restored gloss entry and the two stem fixes read correctly in context) belongs to the Round 3 independent proofread that follows.

## 10. Evidence index (all under `hidden_files/w46/ko-fix-round3/`)

`FIX-REPORT.md` (this file) · `apply_fixes.py` · `sweep.py`, `sweep-pre.json/.log`, `sweep-post.json/.log` · `extract_svg_text.py` · `render-all.sh`, `render-all.log`, `render-logs/` · `regen-textmd.sh`, `textmd-regen.log` · `run-gates.sh`, `gates-run.log`, `gates/` (freeze, occlusion, p8 JSONs/logs, `checks.json`, `counts/`, `koscan/`, `p8keys-post-*.json`) · `round3-checks.py` · `svg_multiset_diff.py`, `svg-multiset-diff.log` · `koscan-round3.py` · `extract_exercises-round3.py` · `gloss_check.py`, `gloss-check.log` · `keydiff.py`, `keydiff.log` · `freeze_summary.py`, `freeze-summary.log` · `zh_tw_simp_scan.py`, `zh-tw-simp-scan.log` · `check_core-post.log` · `append_kit_records.py` · `post-fix-inventory.log` · `pre-fix/` (snapshot: `inventory.log`, `sources/`, `textmd-backup/`, `svg-text/`, `p8keys/`).
