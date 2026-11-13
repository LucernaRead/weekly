# GATE LOG — webpdf italic fix (D3), 2026-W47 ru-en

All gates self-run by the executor on the REBUILT web PDF (SHA `6419f7ad…`)
vs the untouched print PDF (SHA `7b73070c…`, 21,245,374 B, verified before AND
after the rebuild).
Interpreter: `~/workspace/weekly-git/tools/venv/bin/python` (PyMuPDF 2.1).
Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-en/`.
Core dir: `~/workspace/weekly-git/production/2026-w47/core-ru/`.
Scratch dir: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-webpdf-italic-fix1/`
(`PYTHONDONTWRITEBYTECODE=1` on all tool runs).

## 0. Startup probes — PASSED (no EDQUOT)

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`, RC=0 — re-run before every write step (start, patch, rebuild, KIT, logs).
- Real-write probe in this scratch dir OK each time. No `Disk quota exceeded`
  during this task.

## 1. Identity — SHA-256 verified (print UNTOUCHED)

- Before rebuild: print 21,245,374 B `7b73070c2c11313a7b7cd6ec714174bffc105fe5f595d99ef32c434e76d2885e`;
  web 3,367,620 B `82dfb6eaeff6eaa7d9851c723404dc27536fd41225804921d2071e522bae65ec`.
- After rebuild: print SAME bytes + SAME SHA; web **3,375,060 B,
  `6419f7ad188d0e6aca09ae76abc739e954d0d6e1d5249171c34376e6b61360b6`**, 8 pages
  (`pdfinfo`: 8 pages, 1462.5 x 2025 pts, PDF 1.7, producer pypdf).
- Build: `tools/venv/bin/python tools/webpdf.py svg Lucerna-VOL4-ru-en-web.pdf` → RC=0,
  `WROTE … 3375060 bytes, 57149 text bytes` (full log: `webpdf-build.log`).

## 2. D3 — all three facets GREEN (direct measurement, `verify.py` + `verify-out.json`)

| Facet | Before (proof 2) | After | Gate |
|---|---|---|---|
| (a) space | web `'чёрнаяпятница'`, 35,197 chars | web line `'«чёрная пятница»'`, space present, joined form 0 occurrences (grep: `'чёрная пятница'` ×10 in web pdftotext, `'чёрнаяпятница'` ×0); web space bbox [1145.576, 1266.762, 1148.108, 1288.725] **identical to print**; font LucernaNotoSerif-Italic | PASS |
| (b) closing » gap | x1 deficit 3.354 pt, gap +1.161 pt | last-`а` x1 print 1222.815 = web 1222.815, deficit **0.00 pt**; gap −2.193 pt in BOTH (italic overhang restored); » x0 1220.622 both | PASS (≤ 0.5 pt) |
| (c) italic | web LucernaNotoSerif-Regular, 0 italic chars | web embeds LucernaNotoSerif-Italic + LucernaNewsreader-Italic (`pdffonts`); italic census print 16 chars (NotoSerif-MediumItalic 14 + Newsreader16pt-Italic 2) = web 16 (LucernaNotoSerif-Italic 14 + LucernaNewsreader-Italic 2); D3 span font web = LucernaNotoSerif-Italic | PASS |

- 3× visual crops (`p1-teaser-print.png` / `p1-teaser-web.png`, clip x1040–1420,
  y1240–1330, P1, 3×): **pixel-identical** — SHA-256 equal
  (`97822ec606d54e0bd30d11878c50d99b2bac0d91221a2e6bb6300190313d0b70`),
  0 / 307,800 pixels differing. Read by eye: «чёрная пятница» italic, two words
  with a clear space, closing » tight on `а`.

## 3. D2 — all 7 original spots still 0.00 pt (direct lookup, pinned by expected print x1)

Command: ad-hoc char-sequence lookup, occurrences pinned by (page, text, print x1)
against proof 2's values (`verify.py` first pass + pinned re-check; all RC=0).

| Spot | Print x1 | Web x1 | Deficit (was) |
|---|---|---|---|
| P1 headline `14-` 39.75 pt | 133.02 | 133.02 | **0.00** (was 4.33) |
| P4 heading `14-` 24 pt | 106.46 | 106.46 | **0.00** (was 2.62) |
| P1 contents `1. 14-` 15 pt | 1138.69 | 1138.69 | **0.00** (was 2.20) |
| P4 band-sub ` все восемь результатов` 13.5 pt | 1008.74 | 1008.74 | **0.00** (was 1.94) |
| P1 contents `3. «` 15 pt | 1122.22 | 1122.22 | **0.00** (was 1.17) |
| P5 title `«` 24 pt | 80.11 | 80.11 | **0.00** (was 0.91) |
| P7 `«` 16.12 pt ×2 (x0=1096.12) | 1105.61 / 1105.61 | 1105.61 / 1105.61 | **0.00 / 0.00** (was 0.58) |

No regression. (Note: the first-pass char-sequence scan also matched every OTHER
`«`/`14-` occurrence on those pages — all deficits 0.00 as well; the table above
is the pinned 7.)

## 4. Full independent scan — proof 2's method, re-run (`fullscan.py`, copy of proof 2's file, unmodified)

- `tools/venv/bin/python -W ignore <scratch>/fullscan.py` (cwd = edition dir) → RC=0.
  Output: `scan.json`, `scan-out.txt`.
- Span-text diffs: **0** (was 1, D3(a)). Abutting pairs (web−print gap) > 0.5 pt: **0**
  (was 1, D3(b) +3.354). Intra-span char-pair gap diffs > 0.5 pt: **0** (was 1).
  Per-page char multiset: all 8 pages `{}` (empty — was P1 off by one space).
- Extended sweep in `verify.py` (SAME pairing: line y + order, advance-box gap,
  but reporting the MAX over ALL pairs, not just flagged ones): **2,644 pairs,
  max diff 0.00 pt, 0 pairs > 0.5 pt.** The D2-round 1,704-pair scan is NOT reused —
  its line-key matcher dropped the D3 pair (proof 2's finding); this sweep uses
  proof 2's line-y + order pairing and additionally re-measures every D2 spot by
  direct lookup (§3), so it is not subject to that matcher gap.
- Note on method: `verify.py`'s first version matched spans by exact text and failed
  on the D3 line because PyMuPDF merges `чёрная` + space + `пятница` into one span;
  it was rewritten to char-level matching. The pinned re-check then confirmed §2–§3.

## 5. Text layers — byte-identical

- `pdftotext Lucerna-VOL4-ru-en.pdf` → **57,149 B**; `pdftotext …-web.pdf` → **57,149 B**.
- `diff` of the two texts → **RC=0, zero differing lines** (was exactly one differing
  line, P1 line 207, pre-fix). Texts saved at `/tmp/italfix-print.txt` / `/tmp/italfix-web.txt`
  (ephemeral; the byte counts are recorded here and in the KIT).

## 6. `check_core.py` — GOLDEN 8, BAD 0, RC=0

- `PYTHONDONTWRITEBYTECODE=1 …/venv/bin/python check_core.py .`
- golden BAD: 0; gloss fails: 0; P8 svg text chars: 10,571.
- 1 orphan line-start (P7 y553 `”».`, known benign); 1 same-baseline collision
  (P1 y1712 `чёрная` + ` `, the D3 line — same as core/proof 2).

## 7. p8 extract + compare — 150/150, CLEAN, RC=0

- `tools/p8.py extract --p8 svg/p8-test.svg --total 150 --json <scratch>/p8-extract.json`
  → noted set = 150 of 150, RC=0.
- `tools/p8.py compare --core-p8 <core-ru>/svg/p8-test.svg --edition-p8 svg/p8-test.svg
  --total 150 --json <scratch>/p8-compare.json`
  → `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]`, RC=0
  (the four E translation keys, as expected).

## 8. freeze — baseline 8/8, diff −0 removed, RC=0

- `tools/freeze.py baseline --build . --core-svg svg --out <scratch>/freeze`
  → `baseline: 8/8 SVGs byte-identical (repointed files: none)`, RC=0
  (p5 hash `ae19aec96bc1d5ba…` matches the KIT record; full log: `freeze.log`).
  Core integrity OK (8 shipped core SVGs unchanged).
- `tools/freeze.py diff --core-svg <core-ru> --edition-svg svg --json <scratch>/freeze-diff.json`
  → per page **−0 strings removed** (P1–P8); added CJK only U+3000 (121 total), RC=0.

## 9. Occlusion audit — 42 TEXTX, flag set IDENTICAL to pre-patch runs

- `tools/occlusion_audit.py --selftest` → OK (planted classes fired, clean controls silent), RC=0.
- `tools/occlusion_audit.py --json <scratch>/occlusion.json svg` → **42 TEXTX,
  0 LINEX, 0 COVER, 0 FOOTER, 0 EDGE, 0 BOXTITLE**.
  Flag-set comparison (byte-identical JSON) vs the weight-patch run
  (`scratch-webpdf-patch1/occlusion.json`) AND proof 2's run
  (`scratch-ru-en-proof2/occlusion.json`): **IDENTICAL — no new flag**.
  Round-1 pixel adjudication (42/42 CLEAR, systematic false-positive class) still applies.
- Exit-code note: the tool returns **RC=1 whenever any flag exists**
  (`occlusion_audit.py: exit_code = 1 if flags else 0`) — that is its by-design
  "flags present" signal, not a failure of this run. (Proof 2's "RC=0" for the same
  42-flag run was a pipeline artifact: they captured `tail`'s RC. The substantive
  gate — flag set identical, no new flag — passes.)
- Extra `--core` run (`--core <core-ru>`, `--json <scratch>/occlusion-vs-core.json`):
  core 42 flags; NEW vs core: 4 — all four involve edition-only English strings
  (`PRACTICE DATA`, `LANGUAGE`, `TEST AND ANSWERS`, `ANSWER KEY…`), i.e. pre-existing
  edition-vs-core differences, none introduced by this patch (flag set byte-identical
  to the pre-patch runs proves that).

## 10. KIT — updated (§5 + §7, ru-en only)

- §5: new web PDF 3,375,060 B / SHA `6419f7ad…`; pdftotext 57,149 = print, `diff` 0;
  italic-patch paragraph added; multiset line corrected to 35,198 chars each.
- §7: "Print/web text layer" line corrected (old "multiset identical (30,293 chars
  each)" was wrong pre-fix — off by exactly one U+0020; true only after this fix);
  1,704-pair scan claim corrected (its matcher missed the D3 pair); new
  "Webpdf italic patch APPLIED" record with fix, mechanism correction, and gates.
- No other KIT touched; no `lint --write`, no index.json touch.

## 11. NOT done (per the brief)

- No source edits, no rebuilds of any other edition, no print re-render.
- No git write operations of any kind (no add/commit/push/stash/reset, no
  `insert.py`, no `lint --write`). Patch commit left to the coordinator.
- No files left behind in the repo: `scan.json` written by the fullscan run into the
  edition dir was copied to scratch and removed; `__pycache__` suppressed
  (`PYTHONDONTWRITEBYTECODE=1` on every run). `git status` after the work shows only
  `M tools/webpdf.py` as mine (plus pre-existing dirty state from other agents:
  `M tools/freeze.py`, `M tools/occlusion_audit.py`, `M tools/p8.py`, `issues/2026-w43/…`
  — mtimes predate this session; untouched).
