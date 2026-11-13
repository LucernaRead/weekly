# PORT-REBUILD-SYNC-LOG — W47 ru-ko Hangul fix: port to 15 svglib.py copies, rebuild ru-ko, sync

Date: 2026-11-12 (UTC). Worker: ru-ko port + rebuild + sync.
Task: port the ko-fix `_run_w` Hangul diff to all 15 production `svglib.py`
copies, rebuild ru-ko from the patched production copy, verify, sync ru-ko only.
Production: `~/workspace/weekly-git/production/2026-w47/` (main only, no branch).
**No commit / push / lint. No other edition rebuilt or touched.**
Sources: ko-fix probe log `hidden_files/w47/scratch-runw-ko-fix/REBUILD-LOG.md`,
diff `hidden_files/w47/scratch-runw-ko-fix/svglib.diff`, portability sweep
`hidden_files/w47/scratch-runw-ko-fix/portability.log` (all under
`~/workspace/goals/lucernaread-social-media-operations/` — the task's bare
`hidden_files/w47/...` path is goal-relative, not repo-relative).
Scratch (this log's home):
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ru-ko-port-rebuild/`

## 0. Pre-flight

- Disk at start: 99G used / 150G (66%), below the 100G stop line. Disk at end: 99G.
- Memory gate 1500 MB available (per task): build1 start waited 240 s for
  available to rise 1418 → 1694 MB; all later gates passed without waiting.
- Production ru-ko BEFORE SHAs re-hashed before any copy — match the ko-fix
  log §1 exactly (text.md `5e9bd672…`, print `78e4442a…` 22,007,810 B, web
  `34e1c1db…` 3,513,245 B).
- Note (pre-existing KIT drift, same class as the R2R3 sync log §1a): the
  ru-ko KIT §5 web line said 3,513,230 B / `3bf39ecf…`, but the actual BEFORE
  web file was 3,513,245 B / `34e1c1db…` (web rebuilt without a KIT update).
  The §5 line now carries the new synced values (§3); the true BEFORE values
  are recorded here.

## 1. Port — all 15 `svglib.py` copies (exact diff, `patch --fuzz=0`)

Method: pre-patch md5 verified against the expected value for every file
BEFORE patching (all 15 matched); dry-run `patch` on all 15 (15/15 OK); then
patched + `py_compile` each. Pre-patch copies saved in `pre-patch/`.

| File | Before md5 | After md5 | Bytes |
|---|---|---|---|
| `core-ru/svglib.py` | `ee3211298f274e02ade2d4ca318ce354` | `27f11789af7c828e47ca14eb00c1dded` | 23,011 → 24,488 |
| `2026-w47-ru-de/svglib.py` | `ee321129…` | `27f11789…` | 23,011 → 24,488 |
| `2026-w47-ru-en/svglib.py` | `ee321129…` | `27f11789…` | 23,011 → 24,488 |
| `2026-w47-ru-es/svglib.py` | `ee321129…` | `27f11789…` | 23,011 → 24,488 |
| `2026-w47-ru-fr/svglib.py` | `ee321129…` | `27f11789…` | 23,011 → 24,488 |
| `2026-w47-ru-it/svglib.py` | `ee321129…` | `27f11789…` | 23,011 → 24,488 |
| `2026-w47-ru-ja/svglib.py` | `ee321129…` | `27f11789…` | 23,011 → 24,488 |
| `2026-w47-ru-ko/svglib.py` | `ee321129…` | `27f11789…` | 23,011 → 24,488 |
| `2026-w47-ru-nl/svglib.py` | `ee321129…` | `27f11789…` | 23,011 → 24,488 |
| `2026-w47-ru-pt/svglib.py` | `ee321129…` | `27f11789…` | 23,011 → 24,488 |
| `2026-w47-ru-zh-tw/svglib.py` | `ee321129…` | `27f11789…` | 23,011 → 24,488 |
| `2026-w47-nl-ru/svglib.py` | `8630b52f57bc4be209ef6ff4e51797a8` | `9b2531b76693a62a959d5927afb96c1c` | 19,514 → 20,991 |
| `2026-w47-pt-ru/svglib.py` | `f1e0895cebf46c98b864657073004c6c` | `c52139e5a6357742a944f9651071f6b6` | 19,508 → 20,985 |
| `2026-w47-zh-cn-ru/svglib.py` | `ce693ad4ff1d7ca6e8765c111c524ae0` | `13e7fa7045b5c46bb5a9fecc47518c99` | 31,170 → 32,647 |
| `2026-w47-it-ru/svglib.py` | `ee321129…` | `27f11789…` | 23,011 → 24,488 |

(All 15 deltas are +1,477 bytes — the same 24-line insertion. Sizes measured
on disk; the 22,924 B figure in the earlier port/ko-fix logs does not match
the files as they stand — the md5s, which are the binding check, match
exactly.)

Verification (all pass):
- The 11 ru copies + it-ru are byte-identical after patching, md5
  `27f11789af7c828e47ca14eb00c1dded` — exactly the ko-fix worker's patched md5.
- The 3 `*-ru` copies each differ from pre-patch ONLY by this diff:
  `diff` pre→post is 24 added lines, 0 removed lines; reverse-patching the
  patched file reproduces the recorded pre-patch md5 exactly (nl-ru
  `8630b52f…`, pt-ru `f1e0895c…`, zh-cn-ru `ce693ad4…`). Ru-ko reverse-patch
  also reproduces `ee321129…`.
- `py_compile` passes on all 15. The diff is a pure insertion (comment +
  Hangul branch in `_run_w`, `_is_hangul` helper); no other line changed.
- No other production file was modified by the port (only the 15 `svglib.py`;
  `__pycache__` refreshed by `py_compile`, content-neutral).

## 2. Rebuild ru-ko from the patched production copy (scratch only)

Source: full copy of the production edition at
`src-edition/2026-w47-ru-ko/` (verified byte-identical to production,
`svglib.py` md5 `27f11789…`); built via `tools/run_build.py --build
<scratch source> --out ru-ko/build{1,2} --steps run,render` (driver
`run_port.sh`, same memgate/gates as the ko-fix `run_ko.sh`); `webpdf.py`
regenerated unconditionally on build1. Builds 02:28–02:36 UTC.

- build1 rc=0, build2 rc=0; run.py TOTAL **150** both builds (ALL DONE, no
  OVERFLOW); P8 keys end col 3 y **2231.27** (unchanged); Morozko SKIPPED as
  before (ko never had it — out of scope, not a loss).
- text.md byte-identical to production (`5e9bd672…`, 65,012 B).

| File | SHA-256 | Bytes |
|---|---|---|
| print `Lucerna-VOL4-ru-ko.pdf` | `62538d215e2ef0cbe440faa23cb4e147dc78e9116e1b6db02fc07ca704635b27` | 22,005,230 |
| web `Lucerna-VOL4-ru-ko-web.pdf` | `e996c1f3826b6606c88b3ed05143de8299faaaba9f3e7a736f6cc4170ff6f350` | 3,510,669 |

- **Print SHA is EXACTLY the probe's `62538d21…` (22,005,230 B)** — the
  required gate, passed.
- Web SHA differs from the probe's `da80b173…` (3,510,692 B) — expected
  webpdf font-subset nondeterminism (same class as the R2R3 sync log §1a:
  10 B for ru-it, 23 B for ru-ja between runs). Verified by text-identity +
  gates on the synced file, not overridden: same 58,756 pdftotext bytes as
  the probe web, print/web text layers identical per page (26,535 non-ws
  chars each), census identical (§2a).

### 2a. Gates on the rebuild — ALL PASS

- Census AFTER (probe method, print = web): **95 tokens / 223 boundaries**.
  Census JSON `rows` are byte-identical to the probe's AFTER census (only
  the `pdf` path field differs) — the same known-FP set, **0 real joins**:
  the 11 Cyrillic-bearing rows are the previously-cleared false positives
  (`→После` ×3, `→Родительный`, `뒤에는골:`, P8 arrows ×7, `аное대조를나타냅니다`
  P8 2.34–2.44 pt unchanged vs BEFORE); the other 84 tokens are Korean CJK
  rows (e.g. `빈칸채우기` ×48 at 3.28 pt — real spaces between Korean words,
  extraction artifacts). GONE: all 4 DATE cases, the entire Medium-class
  join set, `результатов+`, `—скидка`, `—поздравляю`. Gaps AFTER: spaced
  `13/20/16 ноября` present, fused forms absent (same as probe §6).
- p8 extract **150/150**; p8 compare vs production core-ru **CLEAN,
  missing=[] extra_count=0 uncertain=[], keydiff [137, 138, 139, 140]**
  (expected — the four E translation keys).
- check_core rc=0, golden BAD 0, gloss fails 0, orphan 1 (P7 y553 `”».`,
  same benign class as KIT), **collisions 0** (was 10 in R2).
- Occlusion audit: **0 flags** (was 8 TEXTX in R2; selftest OK).
- Freeze: **8/8 SVG SHA match** between the two independent builds; print
  PDFs byte-identical (`62538d21…`).
- Print/web text layers: **identical per page** (per-page byte-identical;
  26,535 non-ws chars each).
- Morozko: keys end 2231.27, SKIPPED as before (§2).

## 3. Sync ru-ko ONLY

Copy: verified scratch build1 print + web PDFs → production
`2026-w47-ru-ko/` (02:41 UTC); production copies re-hashed after copy.

| File | BEFORE (production) | AFTER (synced) |
|---|---|---|
| `2026-w47-ru-ko.text.md` | `5e9bd672…` (65,012 B) | `5e9bd672…` unchanged (65,012 B) |
| `Lucerna-VOL4-ru-ko.pdf` (print) | `78e4442a…` (22,007,810 B) | `62538d21…` (22,005,230 B) |
| `Lucerna-VOL4-ru-ko-web.pdf` (web) | `34e1c1db…` (3,513,245 B) | `e996c1f3…` (3,510,669 B) |

pdftotext bytes on the synced files (webpdf method): print 58,756, web
58,756 (print = web). P7 `Страница` junctions verified on the synced print
PDF: **8× `( Страница N` with the space, 0× jammed `(Страница`**.

### 3a. KIT §5+§7 updates (`WEEKLY-KIT.md` in the edition dir)

- §5 L53–54: print line → 22,005,230 B `62538d21…`; web line → 3,510,669 B
  `e996c1f3…`.
- §5 L56: pdftotext bytes 58,554 → **58,756**; char count 26,441 → **26,535**
  (the 26,441 was stale since the 2026-11-11 re-fanout, whose record already
  says 26,535).
- §7: appended a dated **Rebuild (2026-11-12, `_run_w` Hangul fix)** record
  (new SHAs/sizes + gates + freeze re-baseline outcome). No historical Fix
  record rewritten; the pre-fix SHAs remain in §7 only as history.
- Verification after edit: each new SHA appears exactly twice in the KIT
  (§5 current-state + §7 record); old SHAs are gone from §5 (0 hits in
  §5 for `78e4442a` / `3bf39ecf`).

### 3b. Freeze re-baseline on the synced files

Method (per the R2R3 sync log §3): `tools/venv/bin/python tools/freeze.py
baseline --build production/2026-w47/2026-w47-ru-ko --core-svg
production/2026-w47/2026-w47-ru-ko/svg --out <this dir>/freeze-ru-ko`
(driver `freeze_run.py`; `2026-w47-ru-ko` is not a ko-family path for
freeze.py's Pillow guard — ko is the reader language, not the target — so
the venv/Pillow-13 stack is correct, as the probe builds already proved).
Run 02:44 UTC, rc=1.

- Tool baseline vs shipped `svg/`: **0/8 (expected)** — production `svg/`
  still holds the PRE-fix build's SVGs (sync copies PDFs only; the `svg/`
  refresh is out of scope, same as the R2R3 sync). The tool log shows the
  produced hashes are the NEW SVGs, differing from the shipped ones by
  design. "repointed files: none" (fresh SVGs regenerate in place).
- Direct comparison (freeze.py's own collection rule, `<out>/svg` wins over
  `build-copy/svg`): freeze-regenerated SVGs vs scratch build1 SVGs
  **8/8** (p1–p8, all True; `freeze-result.json`).
- "shipped core SVGs unchanged by the run (8 files re-hashed)" — the tool's
  own integrity line.
- The freeze print-PDF check is VOID by construction (freeze.py only runs
  `run.py`, never `render.py`) and is NOT claimed; PDF reproducibility
  evidence is the two independent builds' byte-identical print PDFs (§2a).
- The bulky `freeze-ru-ko/build-copy/` (41 MB) was deleted after the check;
  `freeze-ru-ko.log` + `freeze-result.json` kept.

### 3c. Final production-integrity check (after the freeze run)

Re-hashed text.md + print + web in production: **3/3 OK, 0 mismatches.**
text.md byte-identical to BEFORE (`5e9bd672…`); print `62538d21…`; web
`e996c1f3…`; production `svglib.py` md5 `27f11789…`. P7 junctions
re-checked on the synced print: 8 spaced / 0 jammed. Only ru-ko files were
touched in production: the 2 PDFs, `WEEKLY-KIT.md`, `svglib.py`
(`__pycache__` refreshed by `py_compile` only).

## 4. Scope notes / open items

- No other edition was rebuilt: the portability sweep proves the diff
  changes 0 runs in the other 13 editions' 90,419 swept runs, so their
  R1/R2/R3 scratch builds stand. No sibling PDF, no other edition dir, no
  other family's file was touched.
- The two concurrent sync workers (R2R3, R1) and their editions/scratch
  dirs were not touched. (Observed, not mine: `core-ru/WEEKLY-KIT.md`,
  `content8.py`, `ru_textmd.py` show modified in git status — the R1 sync
  worker's in-progress files; left alone.)
- Production `svg/` dirs still hold the pre-`_run_w` build's SVGs for all 15
  patched editions (sync copies PDFs only). That is the known, accepted
  state from the R2R3 sync; a `svg/` refresh is out of this task's scope.
- No commit / push / lint (per task; the 2026-w47 edition dirs are untracked
  in git, `??`, so no `git diff` baseline exists — verification was by
  direct hash/read of the edited lines).
- Disk at end: 99G used / 150G; the 100G stop line was never crossed.

## 5. Files in this scratch dir

- `PORT-REBUILD-SYNC-LOG.md` (this file), `run_port.sh` (rebuild driver),
  `freeze_run.py` (freeze re-baseline driver), `census.py`, `checks.py`,
  `gap_rude.py` (gate scripts copied from the ko-fix scratch),
  `pre-patch/` (the 15 pre-patch `svglib.py` copies) + `pre-patch-md5s.txt`,
  `src-edition/2026-w47-ru-ko/` (patched production copy — the build source),
  `ru-ko/` (`driver.log`, `run_build{1,2}.log`, `webpdf1.log`,
  `after-sha.txt`, `census-AFTER-{print,web}.txt/.json`, `gaps-AFTER*.txt`,
  `crops/`, `gates/` (p8-extract/​compare, check_core, occlusion, freeze,
  textlayer, morozko), `build1/` + `build2/` (full run_build outputs)),
  `freeze-ru-ko.log` + `freeze-result.json` (freeze re-baseline; the
  `freeze-ru-ko/` build-copy was deleted after the check, its `svg/` is an
  empty placeholder dir).
