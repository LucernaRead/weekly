# SYNC-LOG — W47 `_run_w` re-rebuild sync: R1's 5 editions
(ru-de / ru-en / ru-fr / ru-es / core-ru)

Date: 2026-11-12 (UTC, ~02:19–02:35). Sync worker: R1 sync.
Source: R1 log `hidden_files/w47/scratch-ru-rerun-R1/REBUILD-LOG.md` (§7 values).
Production: `~/workspace/weekly-git/production/2026-w47/` (main only, no branch).
**No commit / push / lint.** ru-ko NOT synced (BLOCKED). R2's/R3's editions NOT
touched (a separate sync worker owns them). No other family, no W43/W45/W46
covers/motions, no weekly-design, no little-stage.

## 0. Pre-flight

- Disk at start: 99G used / 150G (67%), below the 100G stop line. Disk at end
  of copy: 99G (the sync only overwrites existing files, net ~0).
- R1 log §7 read first. Production BEFORE SHAs re-hashed before any copy: all
  16 files (6 text.md + 5 print + 5 web) match the BEFORE values recorded in
  the R1 log §1/`before.sha256` — 0 mismatches. (Full table in §1: "BEFORE".)
- `core-ru/content8.py:133` verified `img_h = 200` before the copy (the
  Morozko layout fix was already in production; `content8.py` not touched).

## 1. Scratch verification (BEFORE copy) + before→after table

Every scratch build-1 file was hashed on disk and compared with its recorded
SHA **before** copying. **10/10 PDFs + 6/6 text.md files matched outright,
sizes included — 0 exceptions** (unlike the R2 sync, no stale-log discrepancy
here). Production copies were re-hashed after the copy and match the scratch
SHAs exactly (10/10). text.md files were NOT copied and are byte-identical
before/after (spacing-only rebuilds).

| Edition | File | BEFORE SHA-256 (production) | BEFORE bytes | AFTER SHA-256 (synced) | AFTER bytes |
|---|---|---|---|---|---|
| ru-de | `2026-w47-ru-de.text.md` | `d0f9b48c8fab4df8bb39acfdfebfbc6ad6cf0f09e75891449d13a0f1ce2dcc0f` | 63,471 | unchanged | 63,471 |
| ru-de | `Lucerna-VOL4-ru-de.pdf` (print) | `80024034da684b62db63a3671866f85fc4c913f56ebcb48ebca1603aa4cc31e3` | 21,230,193 | `1920da86eb76624b300a6c76f6acc3a0bfbb2921aab37ad111cd434e238e396c` | 21,229,165 |
| ru-de | `Lucerna-VOL4-ru-de-web.pdf` (web) | `05b0a7abf59aa3617e5e75e94361460a692a144fb883017ba64bdf2198319992` | 3,384,428 | `8366d304e95ba1a906b762f884dbcb636b1b321d47f1cdfe9c833f8b94ca9197` | 3,383,411 |
| ru-en | `2026-w47-ru-en.text.md` | `5dba645578989ed58673b060b6c67e6df844335f82a1ba351012f66e5c9404df` | 62,786 | unchanged | 62,786 |
| ru-en | `Lucerna-VOL4-ru-en.pdf` (print) | `1fcc6aa4101b07a89f17cab7d52a974c3acdfdc49712a96f043f66909d468831` | 21,249,828 | `e29ba5fae4a3886d19867a6c995786deec7afe307f48d79d301d6be5ae0fc81b` | 21,248,719 |
| ru-en | `Lucerna-VOL4-ru-en-web.pdf` (web) | `7e67d0069ad0bb8ee4d1951a4ebc9cdc30d416a635241468bb0fce0df877b09f` | 3,379,458 | `7a3f635116c948b2c9605be4111859f212a117b5cc4240c20fadbd3321174f5b` | 3,378,370 |
| ru-fr | `2026-w47-ru-fr.text.md` | `e4cc50fd4195ed1adb7051c684c894c5a3b3091aa643cf3bab96690178e22a46` | 63,361 | unchanged | 63,361 |
| ru-fr | `Lucerna-VOL4-ru-fr.pdf` (print) | `32f2e1688c71212688aa47239530508fac1177d3b7dab278b7814763468a439f` | 21,290,501 | `c29251ebecb6125edbf7e9d4f66c6ff3371f164651563412a3db142d876ff6b5` | 21,289,489 |
| ru-fr | `Lucerna-VOL4-ru-fr-web.pdf` (web) | `2eb8062cbb0cd2ed714ed680f9c59b381d0389ccb07e38bd0c73a31a32c06139` | 3,384,329 | `d17fc2255b1b6c7b15286ce6b111c8d8f9c3079b210dd372e144e6ca9918c4d6` | 3,383,322 |
| ru-es | `2026-w47-ru-es.text.md` | `332c8e4f5478181d21281fe059483f0da4ee2bf5e39fec4464f836049e2bad60` | 64,176 | unchanged | 64,176 |
| ru-es | `Lucerna-VOL4-ru-es.pdf` (print) | `64cb48f90dea70553a76e70c8cb9bc75ffa571c1ceaa8318c8655b47b80cf7c3` | 21,278,615 | `deb7b08e1697793a0412cf5c06c85fbc737393e50a6407fa83864b5ccb2ad31e` | 21,276,149 |
| ru-es | `Lucerna-VOL4-ru-es-web.pdf` (web) | `526873a863981b82d6d56892508ef635204baf1569746ba4b2d0b70cd96c8123` | 3,387,494 | `8c1bb27e7bf3bc3bb79a5cc1fe534b7499719158f7532dd90b18b10719f401d4` | 3,385,029 |
| core-ru | `2026-w47-ru-core.text.md` | `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` | 60,953 | unchanged | 60,953 |
| core-ru | `2026-w47-ru-zh-cn.text.md` | `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` | 60,953 | unchanged | 60,953 |
| core-ru | `Lucerna-VOL4.pdf` (print) | `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81` | 31,429,147 | `c2fd743e16fec66c13cf1f610445c5b1c35f209279d6e5cdfdc0d2deec7202a2` | 31,426,561 |
| core-ru | `Lucerna-VOL4-web.pdf` (web) | `b5d67aeb059a8baf4edbf4a5909a6c765327a9fdaf9a0c0db1e2d33c1bc1a7ba` | 4,025,900 | `a4f4bbd61deb3574a9e66acaf4d7d0e2cd613cfadf6f235bf007555555c81c7f` | 4,023,304 |

Only the 5 in-scope edition dirs were touched. Copy result: all 10 PDFs
copied; production copies re-hashed after copy and match the scratch SHAs
exactly (10/10 OK).

## 2. KIT §5+§7 updates (print/web SHA + size only)

Only the lines stating the CURRENT build's print/web SHA-256, file bytes, and
text-layer bytes were changed. No other section touched; no historical Fix
record rewritten; D5 items frozen. (Section-number note: in the ru-de KIT the
Build section is §4, not §5 — §4 L37–38/40 were updated, the §5-equivalent
lines; core-ru's current-state line lives in §7.3. In the ru-* KITs §7 holds
only historical Fix records and the previous build's gate lines — no
current-state print/web SHA/size lines existed there to update, per the R2/R3
sync precedent.)

pdftotext bytes were measured on the synced files (`pdftotext <pdf> - | wc -c`);
print = web for all 5, `cmp` of the two pdftotext outputs is diff 0 for all 5.
PyMuPDF `get_text` char totals were also measured on the synced files and match
the R1 log values exactly, print = web per page 8/8 for all 5.

| Edition | KIT lines changed | New values |
|---|---|---|
| ru-de | §4 L37–38 (print/web SHA+bytes), L40 (text-layer bytes/chars) | print 21,229,165 B `1920da86…`; web 3,383,411 B `8366d304…`; pdftotext 57,908 (was 57,915), 37,532 chars each (was 37,514) |
| ru-en | §5 L52–53, L56 (pdftotext bytes) | print 21,248,719 B `e29ba5fa…`; web 3,378,370 B `7a3f6351…`; pdftotext 57,366 (was 57,316); non-whitespace chars 30,352 unchanged |
| ru-fr | §5 L53–54, L56 (pdftotext bytes) | print 21,289,489 B `c29251eb…`; web 3,383,322 B `d17fc225…`; pdftotext 58,056 (was 58,036); non-whitespace chars 30,770 unchanged |
| ru-es | §5 L53–54, L56 (pdftotext bytes/chars) | print 21,276,149 B `deb7b08e…`; web 3,385,029 B `8c1bb27e…`; pdftotext 57,978 (was 57,780); non-whitespace chars 30,838 (was 30,774); text layers now byte-identical per page (37,577 chars each) — the old "segmentation noise" clause no longer applies and was dropped |
| core-ru | §7.3 L105 (实测文件 line; label fix1 → _run_w 2026-11-12) | print 31,426,561 B `c2fd743e…`; web 4,023,304 B `a4f4bbd6…`; fix1 values moved into the 旧值 clause |

Verification after edit: each new SHA appears exactly once in its KIT; the
old current-state SHAs are gone from the current-state lines. They remain only
inside the §6/§7 historical Fix records, which is correct history (ru-fr's
old full SHAs survive only in §7 L92, the Spacing-rebuild record's
"SHAs old → new" line; ru-de/ru-en old SHAs survive only as truncated `…`
forms in their §6/§7 records). The 5 edition dirs are untracked in git (`??`)
except core-ru's `WEEKLY-KIT.md` (tracked); verification was by direct
grep/read of the edited lines.

Measured text-layer figures on the synced files (for the record):
ru-de pdftotext 57,908, get_text 37,532 chars, non-whitespace 31,001;
ru-en 57,366 / 37,122 / 30,352; ru-fr 58,056 / 37,505 / 30,770;
ru-es 57,978 / 37,577 / 30,838; core-ru 56,073 / 31,504 / 25,934.
(core-ru's fix1 KIT line recorded 56,024 pdftotext bytes; the new build
measures 56,073 — the §7.4 fix1 line is historical and was left untouched.)

Pre-existing KIT drift resolved by this sync (noted, not introduced here):
- ru-es KIT §5 web line was stale vs BEFORE (3,387,465 B `7af50086…` vs the
  production BEFORE file 3,387,494 B `526873a8…` — web rebuilt 22:21 Nov 11
  without a KIT update, per the KIT's own Fix 1 note).
- core-ru KIT §7.3 web line was likewise stale vs BEFORE (4,025,834 B
  `2f995f1d…` vs the production BEFORE file 4,025,900 B `b5d67aeb…`).

Note on ru-en: the §5 "Web PDF built" line (L56, updated to 57,366) and the
Spacing-rebuild record line (L58, 57,367 bytes / 37,102 chars) were already
layered figures from different builds before this sync; L58 is left as that
build's historical record, as in the R2/R3 precedent.

## 3. Freeze re-baseline (on the synced files)

Method (per the R2/R3 sync + `tools/freeze.py`): for each edition,
`tools/venv/bin/python tools/freeze.py baseline --build
production/2026-w47/<ed-dir> --core-svg production/2026-w47/<ed-dir>/svg
--out <this dir>/freeze-<ed>` (driver `freeze_run.py`, log `freeze_run.log`,
per-edition logs `freeze-<ed>.log`, results `freeze-results.json`), then a
direct SHA-256 comparison of the freeze rebuild's SVGs against the scratch
build-1 SVGs that produced the synced PDFs.

| Edition | Tool baseline vs shipped `svg/` | Direct vs scratch build-1 SVGs | Per-page |
|---|---|---|---|
| ru-de | 0/8 (rc=1) | **8/8** | all 8 true |
| ru-en | 0/8 (rc=1) | **8/8** | all 8 true |
| ru-fr | 0/8 (rc=1) | **8/8** | all 8 true |
| ru-es | 0/8 (rc=1) | **8/8** | all 8 true |
| core-ru | 0/8 (rc=1) | **8/8** | all 8 true |

Scope note: this sync copies PDFs only (per task); the production `svg/` dirs
still hold the PRE-`_run_w` build's SVGs. Therefore the tool's own baseline
number (rebuild vs the shipped `svg/`) is EXPECTED to be 0/8 — the SVGs
genuinely changed, that is the point of the rebuild. The reproducibility proof
is the direct comparison against the scratch build-1 SVGs: 8/8 for all 5.
All 5 freeze logs also record "core integrity: shipped core SVGs unchanged by
the run (8 files re-hashed)" — the freeze runs did not modify production.
`freeze.py` runs `run.py` only (no `render.py`), so there is no freeze-rebuild
print PDF to compare; print-PDF byte-identity between R1's two independent
builds was already verified in the R1 log (build 1 vs build 2, same SHA).
The KIT freeze lines still describe the previous build's gate (they were not
rewritten — they are historical records); the production `svg/` refresh is out
of this task's scope.

## 4. Final production-integrity check

Re-hashed text.md + print + web for all 5 editions AFTER the freeze runs
(16 files): text.md files byte-identical to the recorded BEFORE SHAs
(`d0f9b48c…` / `5dba6455…` / `e4cc50fd…` / `332c8e4f…` / `348511e0…` ×2);
print/web equal the scratch SHAs (see §1 AFTER column). **0 mismatches.**

core-ru extras:
- `content8.py:133` still reads `img_h = 200`; `git diff` on that file shows
  exactly the one authorized line (`img_h = 250` → `img_h = 200`). The
  `ru_textmd.py` / `svglib.py` diffs predate this task (per the R1 log §0b/§7).
- Morozko image + caption PRESENT on P8 of the synced print PDF: images per
  page [1,1,0,1,1,0,1,1], total 6, P8 = 1; caption
  "«Морозко»: иллюстрация Ивана Билибина, 1932 год. Зимняя сказка — к ноябрю."
  and credit "Иллюстрация: Иван Билибин — общественное достояние
  (Wikimedia Commons)" both present in the P8 text layer.
- Tracked-file footprint in scope (`git status`): only
  `M core-ru/WEEKLY-KIT.md` (this sync) plus the pre-existing
  `M core-ru/content8.py`, `M core-ru/ru_textmd.py`, `M core-ru/svglib.py`.
  No other tracked file changed; no commit/push/lint performed.

## 5. Disk note

99G at start → 99G at end of copy. Disk briefly touched **100G during the
freeze runs** (freeze build-copies ~209M + concurrent workers' writes); the
five `freeze-*/build-copy/` dirs were deleted immediately after the check
(logs + `freeze-results.json` kept), bringing the disk back to 99G. This sync
dir is now 32K. No edition was blocked.

## 6. Files in this scratch dir

- `SYNC-LOG.md` (this file), `freeze_run.py` (freeze driver),
  `freeze_run.log` (driver log), `freeze-results.json` (per-edition freeze
  results), `freeze-<ed>.log` (per-edition freeze tool output),
  `freeze-<ed>/svg/` (empty placeholder dirs; the rebuilt SVGs were collected
  from the deleted `build-copy/svg/` copies — the per-page SHA evidence is in
  `freeze-results.json` and the `DIFF`/`core integrity` lines of the logs).
