# W47 ru-ko CJK regression fix — `_run_w` Hangul predicate + probe rebuild

Date: 2026-11-12 UTC (probe build 02:11–02:17 UTC). Worker: ko-fix probe.
Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-runw-ko-fix/`
Production dir: `~/workspace/weekly-git/production/2026-w47/` (main only, no branch).
**Scratch only — no production file touched, no commit/push/lint.**

## VERDICT: GO — port the exact diff (§3) to all 14 `_run_w` copies

The ru-ko probe build passes **every gate** (census 0 real joins print AND web;
occlusion 0 flags; check_core collisions 0; freeze 8/8; print/web text layers
identical per page; text.md byte-identical), and the portability sweep proves
the diff changes **nothing** for any other font class or edition: 90,419 runs
swept across the other 13 editions, **0 differ**; ru-ko 164/8,698 differ, all
Hangul runs, all positive deltas. The 5 GREEN R2 editions' SHAs stand (their
`_run_w` behaviour is provably unchanged); ru-ko must be rebuilt from the
patched production copy at sync time and its print SHA re-verified (§7).

## 0. Context (verified by R2, not re-litigated)

- The `_run_w` spacing fix (unkerned run measurement in `svglib.py`
  `Page.text`) is probe-green on ru-de and 13/14 re-rebuild editions are
  GREEN in scratch (R2 log `scratch-ru-rerun-R2/REBUILD-LOG.md` §5–§7).
- The ONE exception is ru-ko, BLOCKED: `_run_w` under-measures CJK runs
  with inter-word spaces (~1.09 units per space at 19.5 pt), so 8 P7
  `Страница` page references overlap the preceding Korean sentence's ink
  (3.1–5.5 px) and check_core collisions go 0→10. Verified NOT pre-existing
  (wave-C Medium build and production both 0 flags / 0 collisions).
- The ko CJK token (P8, 2.34–2.44 pt) is unchanged vs BEFORE, not a join,
  not in `_run_w` scope.
- Why only ko: Japanese/Chinese running text has NO inter-word spaces;
  Latin runs are kerned fonts where `_run_w` is the correct measurement;
  Cyrillic kern is 0.00. Korean is the only ru-edition native language
  that combines a CJK script WITH inter-word spaces.
- R2's ko scratch build exists (print `2fd2389c…`, 22,005,216 B; web
  `9403c38c…`, 3,510,639 B) — NOT synced, used here only as the
  regression reference.

## 1. BEFORE state (production ru-ko, verified 2026-11-12 ~02:05 UTC)

| File | Bytes | SHA-256 |
|---|---|---|
| `2026-w47-ru-ko.text.md` | 65,012 | `5e9bd67201fd232aff598e0bbb487ba45821878e533392bc6e749444b090bffe` |
| `Lucerna-VOL4-ru-ko.pdf` (print) | 22,007,810 | `78e4442af8af9ec286c407ff66e08bac2029dd79d3ded43d1bfde3d555a6a400` |
| `Lucerna-VOL4-ru-ko-web.pdf` (web) | 3,513,245 | `34e1c1db929faf24a5a173170a8fab939dfd5503ff88a56a0ce56b07a2bb8ce6` |
| `svglib.py` | 22,924 | md5 `ee3211298f274e02ade2d4ca318ce354` (same as all 11 ru copies) |

BEFORE census (R2, probe method, print = web): **239 tokens / 416
boundaries** — the full Medium-class join set (pre-Medium production
build) plus the second-class 12. R2 AFTER (the regressed build):
**95 / 223**, 0 real joins, but occlusion 8 TEXTX + collisions 10.

Disk at start: 98G used / 150G (below the 100G stop line); at end 99G.
Memory gate as in R2 (wait while available < 1000 MB, max 600 s).

## 2. Mechanism — measured, not guessed (`measure.py`, `measure2.py`)

### 2.1 The 8 overlaps ARE exactly the under-measurement

For each of the 10 check_core collision lines (8 `Страница` + P1 `в` +
P7 `с`), the wave-C-vs-R2 x-shift of the following run equals
`getlength(run) − _run_w(run)` of the Korean run to ≤0.09u (SVG x is
rounded to 0.1). P7 Hangul runs are `sans` kind: the whole Korean
sentence — Hangul + digits + spaces + `(` — is ONE `sans` run in
NotoSansCJK (in `serif` kind the same string splits into 11 runs, with
spaces classed `news`; see §2.2 — this is why only `sans`-kind Korean
lines regress).

| Line | Size | Spaces | getlength | `_run_w` | Delta | R2→waveC shift | shift−delta |
|---|---|---|---|---|---|---|---|
| P7 y1953 `제14라운드의 여덟 경기가 모두 끝났습니다. (` | 19.5 | 5 | 364.80 | 360.48 | **4.31** | 4.3 | −0.01 |
| P7 y1953 `휴식기 후 리그는 11월 20일에 돌아옵니다. (` | 19.5 | 6 | 353.88 | 350.64 | **3.23** | 3.3 | +0.07 |
| P7 y2093 `이것이 2026년 국가대표의 마지막 경기입니다. (` | 19.5 | 5 | 385.38 | 382.14 | **3.23** | 3.3 | +0.07 |
| P7 y2093 `똑똑한 구매자는 서두르지 않는다. (` | 19.5 | 4 | 283.88 | 280.64 | **3.23** | 3.3 | +0.07 |
| P7 y2233 `직업 기념일은 휴일이 아니다. (` | 19.5 | 4 | 248.00 | 244.77 | **3.23** | 3.2 | −0.03 |
| P7 y2233 `이런 주는 일 년에 가장 흔합니다. (` | 19.5 | 6 | 276.84 | 271.45 | **5.39** | 5.3 | −0.09 |
| P7 y2373 `11월의 밤은 어둡고 길다. (` | 19.5 | 4 | 215.84 | 212.61 | **3.23** | 3.2 | −0.03 |
| P7 y2373 `11월에는 근무일 20일과 휴일 10일이 있다. (` | 19.5 | 6 | 357.59 | 354.36 | **3.23** | 3.2 | −0.03 |
| P1 y1206 `고 마감 시점 · ` | 20.5 | 4 | 135.45 | 133.17 | **2.28** | 2.3 | +0.02 |
| P7 y968 `는 출발점으로 생격: ` | 19.5 | 3 | 164.20 | 162.05 | **2.16** | 2.1 | −0.06 |

### 2.2 The exact flank rule — it is NOT "per space"

R2's "~1.09 units per space" is line 1's average (4.31/4). The
decomposition (NotoSansCJK, 19.5 pt, delta = getlength − sum):

| Probe | Delta |
|---|---|
| `가 나` (Hangul–space–Hangul) | **+1.08** |
| `가 나 다` (2 such spaces) | **+2.16** |
| `가  나` (double space) | +0.00 |
| `가. 나` / `가, 나` / `가: 나` / `가; 나` (punct-adjacent) | +0.00 |
| `가 1` / `1 나` / `1 2` (digit-adjacent) | +0.00 |
| `가 A` / `A 나` / `A B` (Latin-adjacent) | +0.00 |
| `가　나` (U+3000) / `가 \u3000나` / `가\u3000 나` | +0.00 |
| `中 文` / `中文 测试` (Han–space–Han) | +0.00 |
| `あ う` / `あいう うえ` (Kana–space–Kana) | +0.00 |
| `가\u00a0나` (NBSP between Hangul) | **+1.08** |
| `나. (` / `가 (나` / `가) 나` | +0.00 |

So the delta is **exactly +1.08u at 19.5 pt per SINGLE ASCII space (or
NBSP) flanked by Hangul syllables on BOTH sides** — and zero otherwise.
Counting lines confirms it: line 2 has 6 spaces but only 3 are
Hangul–Hangul (the others are Hangul–digit or punct), delta 3.23 =
3×1.08; line 6 has 6 spaces, 5 qualify, delta 5.39 = 5×1.08. The
effect is Hangul-specific (Han/Kana spaces: 0.00) and face-independent
(NotoSerifCJK `가 나`: +1.06; bold sans +1.03, bold serif +1.17).
Cross-size, first flagged line (4 qualifying spaces): 17 pt 3.81,
18 pt 4.06, 19.5 pt 4.31, 20 pt 4.44, 20.5 pt 4.56, 23 pt 5.12,
24 pt 5.38, 27 pt 6.06, 46 pt 10.31 — delta/pt ≈ 0.221–0.225, linear.
Per-space delta across ALL spaced Hangul runs on P7 (19.5 pt, 21 runs):
0.00–1.08, mean 0.78 (the spread is the flank mix, not noise).

Consequences for the fix shape (decided by these numbers, not preference):
- A flat per-space correction (+1.09/space) is WRONG: it would
  over-correct every line whose spaces are not all Hangul-flanked
  (line 2: +6.48 instead of +3.23).
- A flank-counting correction would reproduce getlength only
  approximately (rounding, NBSP, mixed runs). Whole-string getlength
  IS the measurement wave-C used and verified (0 flags / 0 collisions),
  so it is exact by construction.
- The branch must be on run CONTENT (Hangul present), not on font
  class — see §2.3.

### 2.3 Why the class branch (`serif`/`sans` → getlength) is REJECTED

| Run | getlength | `_run_w` | Delta |
|---|---|---|---|
| `Tauwetter; ` — sans-kind LATIN run, cls `sans` | 101.77 | 103.80 | **−2.03** |
| `Lucerna` in NotoSerifCJK, cls `serif` | 78.28 | 78.84 | **−0.56** |
| ru-ja P8 `\u3000解答 — ページごとに…` (spaced CJK) | — | — | **−5.75** |
| ru-zh-tw P1 `: Toxer427 — ` (spaced CJK) | — | — | **−1.73** |

In `sans` kind, Latin text is rendered in Noto Sans CJK SC and it
KERNS (Newsreader-style). The class branch would revert the `_run_w`
fix for every sans-kind Latin run — reintroducing the exact defect
`_run_w` was built to fix (the ru-de probe: `Tauwetter; | мокрый`
1.86 → 3.43 pt on-normal only because `_run_w` measures the sum).
Latin-in-CJK runs kern NEGATIVE, Hangul-space runs measure POSITIVE:
the two effects have opposite signs, so no class branch can serve both.

### 2.4 The Hangul predicate — and what it leaves untouched

- All 680 Hangul-containing runs in the R2 ru-ko build:
  delta (getlength − sum) **+0.00…+8.62, zero negative**. So the
  getlength path can only move following runs RIGHT, never left.
  164 of the 680 have a nonzero delta (the other 516 have no
  qualifying space and measure identically either way).
  Hangul+Latin mixed runs (10): delta +0.98…+2.08, all positive.
- Serif-kind CJK runs containing a space: **0** in the ru-ko build
  (spaces are `news`-class in serif kind, so a serif CJK run can never
  contain an ASCII space) — but the predicate covers them anyway if
  one ever arises (serif CJK shows the same +1.06 effect).
- ru-ja / ru-zh-tw: **0 Hangul runs** in all 8,196 / 8,273 runs
  swept; their spaceless CJK runs measure getlength == sum, so the
  predicate leaves them byte-identical.

## 3. The fix — EXACT unified diff (vs production `2026-w47-ru-ko/svglib.py`)

File `svglib.diff` in this dir. The patched file
(`src-edition/2026-w47-ru-ko/svglib.py`) is md5
`27f11789af7c828e47ca14eb00c1dded` (production `ee3211298f274e02ade2d4ca318ce354`).

```diff
--- /home/hatch/workspace/weekly-git/production/2026-w47/2026-w47-ru-ko/svglib.py
+++ /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-runw-ko-fix/src-edition/2026-w47-ru-ko/svglib.py
@@ -184,8 +184,32 @@
     return w
 
 def _run_w(kind, bold, cls, size, t):
+    # Hangul-containing runs take the whole-string getlength instead of
+    # the sum of single-char advances (ru-ko CJK fix, 2026-11-12):
+    # in Noto Sans/Serif CJK, ONE ASCII space (or NBSP) between two
+    # Hangul syllables measures +1.08u MORE in whole-string getlength
+    # than in the sum at 19.5pt ('가 나' +1.08, '가 나 다' +2.16, same in
+    # both CJK faces and bold; scales linearly, +0.22u/pt/space), while
+    # digit/Latin/punctuation-adjacent spaces, double spaces, U+3000,
+    # Han-space-Han and Kana-space-Kana all measure +0.00. Pango renders
+    # the whole-string advance, so the sum under-measured every spaced
+    # Korean run and placed the following run too far left (ru-ko P7:
+    # 8 'Страница' overlaps, check_core collisions 0->10; the wave-C
+    # x-shift equals the measured delta to <=0.09u on all 10 lines).
+    # Latin/Cyrillic runs keep the unkerned sum (Pango renders them
+    # unkerned, e.g. Newsreader -3.19u at 13pt); Japanese/Chinese runs
+    # contain no Hangul, so they keep the sum and are unaffected.
+    # For every Hangul-containing run measured in ru-ko, getlength >=
+    # sum (680 runs, delta +0.00..+8.62, zero negative), so this path
+    # can only move following runs right, never left.
+    if any(_is_hangul(ch) for ch in t):
+        return _pil(kind, bold, cls, size).getlength(t)
     return sum(_adv(kind, bold, cls, size, ch) for ch in t)
 
+def _is_hangul(ch):
+    cp = ord(ch)
+    return 0xAC00 <= cp <= 0xD7A3 or 0x1100 <= cp <= 0x11FF or 0x3130 <= cp <= 0x318F
+
 def _breakable(ch):
     return ch == " "
```

Design notes:
- Only `_run_w` changes; `text_w`/`wrap` are untouched, so
  line-breaking is byte-identical to the shipped layout (no reflow
  anywhere) and the only geometry change is run-boundary x moving
  right on Hangul runs — exactly the overrun.
- The predicate is Hangul syllables + jamo (U+AC00–U+D7A3,
  U+1100–U+11FF, U+3130–U+318F). The `getlength` call reuses the
  same `_pil` face the sum path uses — no new font, no new cache.
- `py_compile` passes. The `_run_w` block occurs exactly once in
  every one of the 14 target files (asserted by the sweep script).

## 4. Portability — the diff changes NOTHING outside Hangul runs (`portability.py`)

Method: the exact edit from §3 applied to scratch copies of all 14
production `svglib.py` files; old vs new `_run_w` compared over (a) a
fixed 24-string corpus (Latin kern cases, Cyrillic, CJK, mixed) and
(b) every run of every text node in each edition's SVG set (R2 build1
SVGs where they exist, else production SVGs). All 14 compile.

| Edition | SVG runs swept | Runs differing old-vs-new | Worst \|diff\| |
|---|---|---|---|
| core-ru | 8,285 | 0 | 0.00 |
| 2026-w47-ru-de | 7,819 | 0 | 0.00 |
| 2026-w47-ru-en | 7,820 | 0 | 0.00 |
| 2026-w47-ru-es | 7,831 | 0 | 0.00 |
| 2026-w47-ru-fr | 7,818 | 0 | 0.00 |
| 2026-w47-ru-it | 7,818 | 0 | 0.00 |
| 2026-w47-ru-ja | 8,196 | 0 | 0.00 |
| **2026-w47-ru-ko** | **8,698** | **164** | **8.62** |
| 2026-w47-ru-nl | 7,814 | 0 | 0.00 |
| 2026-w47-ru-pt | 7,815 | 0 | 0.00 |
| 2026-w47-ru-zh-tw | 8,273 | 0 | 0.00 |
| 2026-w47-nl-ru | 2,817 | 0 | 0.00 |
| 2026-w47-pt-ru | 2,886 | 0 | 0.00 |
| 2026-w47-zh-cn-ru | 5,227 | 0 | 0.00 |

- **90,419 runs across the other 13 editions: 0 differ.** The corpus
  shows 5 differing runs in every edition — those are the 5 Hangul
  probes in the corpus itself (expected); no Latin/Cyrillic/CJK probe
  differs anywhere.
- Only ru-ko among the 14 has Hangul in its text.md (4,112 chars).
  The other `*-ko` / `ko-*` editions' svglib copies do NOT contain
  `_run_w` at all (grep: `_run_w` exists in exactly 15 files — the 14
  targets + `2026-w47-it-ru`, the fix's source), so they never had
  this regression and need nothing.
- `2026-w47-it-ru` (the 15th `_run_w` carrier, byte-identical file)
  was swept separately: 3,893 runs, **0 differ**, compiles OK. It
  should take the same diff at sync time so the family stays
  byte-identical — a sync-step note, not a probe finding.

## 5. Probe build (scratch only)

Source: a full copy of the production edition at
`src-edition/2026-w47-ru-ko/` with ONLY `svglib.py` patched (§3);
built via `tools/run_build.py --build <scratch source> --out
ru-ko/build{1,2} --steps run,render` (the wrapper's repoint +
copy discipline applies; the production edition was hashed before
and after — §7). `webpdf.py` regenerated unconditionally on build1.
Driver: `run_ko.sh` (R2's driver adapted: same memgate, same
completion-marker reuse rule, same gate invocations).

- build1: `run_build` rc=0, "done: outputs (19 svg/png/pdf files)"
  02:11:08 UTC; build2 rc=0, 02:14:15 UTC.
- run.py TOTAL **150** both builds (ALL DONE, no OVERFLOW mentions);
  P8 keys end col 3 y **2231.27** (unchanged); Morozko SKIPPED as
  before (ko never had it — out of scope, not a loss).
- New SHAs (for the sync step — NOT applied):
  - print `62538d215e2ef0cbe440faa23cb4e147dc78e9116e1b6db02fc07ca704635b27`,
    22,005,230 B (R2's was `2fd2389c…`, 22,005,216 B)
  - web `da80b1730f33dd03e935a911fed6578457fab71543a8da4c220e432b575e7cb5`,
    3,510,692 B, 58,756 text bytes (R2's `9403c38c…`, 3,510,639 B,
    58,744 — the +12 in webpdf's counter; extracted text differs by
    exactly the +8 P7 spaces, §6)
  - text.md `5e9bd672…` UNCHANGED (byte-identical in build-copy).

## 6. Gates on the probe build — ALL PASS

- Census AFTER (probe method, print = web): **95 tokens / 223
  boundaries** — the same counts as R2's AFTER (95/223). Cyrillic-bearing
  rows: only 11, ALL previously-cleared false positives, **0 real joins**:
  `→После` ×3, `→Родительный` (3.75 pt), `뒤에는골:` (gap None, same
  as BEFORE), P8 arrows ×7 (2.40–2.41 pt, NOT joins),
  `аное대조를나타냅니다` P8, **2.34–2.44 pt — unchanged vs BEFORE
  (2.35–2.43) and vs R2 AFTER, reported as before**. The other 84
  tokens are Korean CJK rows (e.g. `빈칸채우기` ×48 at 3.28 pt — real
  spaces between Korean words, extraction artifacts). GONE: all 4 DATE
  cases, the entire Medium-class join set, `результатов+`, `—скидка`,
  `—поздравляю`.
- Gaps AFTER (ink, print = web): `13ноября` 1.50 → **2.47 pt**,
  `20ноября` 2.18 → **3.52**, `19ноября` 2.11 → **3.48**,
  `16ноября` 2.24 → **3.68**, `A.на` 1.68 → **3.48**,
  `A.биография` 2.20 → **3.63**, `A.снег` 2.28 → **3.71**,
  `A.цена` 2.29 → **3.72**, `A.точно` 2.29 → **3.71**,
  `результатов+` −0.14 → **3.01**, `—скидка` 1.44 → **2.41**,
  `—поздравляю` → **2.37**. Byline 1.10 pt → **2.89/2.82 pt with
  space char**. Text layer: all four spaced date forms present, all
  fused forms absent. Values are IDENTICAL to R2's AFTER on every
  measured pair (Latin kerning correction fully preserved) except one
  rounding-level 0.01 pt difference on a non-target P5 occurrence
  (`'ёрная пятница»: скидки с 16 ноября'`: 3.02 vs R2's 3.01; the
  target `A. 16 ноября` line is 3.68 in both).
- p8 extract **150/150**; p8 compare vs production core-ru **CLEAN,
  missing=[] extra_count=0 uncertain=[], keydiff [137, 138, 139, 140]**
  (expected).
- check_core rc=0, golden BAD 0, gloss fails 0, orphans 1 (P7 y553
  `”».`, same benign class as KIT), **collisions 0** (was 10 in R2).
- Occlusion audit: **0 flags** (was 8 TEXTX in R2; selftest OK).
- Freeze: **8/8 SVG SHA match** between the two independent builds;
  print PDFs byte-identical (`62538d21…`).
- Print/web text layers: **identical per page** (per-page
  byte-identical; 26,535 non-ws chars each).
- Morozko: keys end 2231.27, SKIPPED as before (§5).

### 6.1 The fix restores wave-C geometry exactly where it matters

Next-run x on the 10 collision lines, fixed build vs wave-C Medium
build vs R2 build (SVG units):

| Line | Fixed | wave-C | Fixed−waveC | R2 | Fixed−R2 |
|---|---|---|---|---|---|
| P7 `제14…끝났습니다. (` | 452.8 | 452.8 | +0.0 | 448.5 | +4.3 |
| P7 `휴식기…돌아옵니다. (` | 1342.9 | 1342.9 | +0.0 | 1339.6 | +3.3 |
| P7 `이것이…경기입니다. (` | 473.4 | 473.4 | +0.0 | 470.1 | +3.3 |
| P7 `똑똑한…않는다. (` | 1272.9 | 1272.9 | +0.0 | 1269.6 | +3.3 |
| P7 `직업…아니다. (` | 336.0 | 336.0 | +0.0 | 332.8 | +3.2 |
| P7 `이런…흔합니다. (` | 1265.8 | 1265.8 | +0.0 | 1260.5 | +5.3 |
| P7 `11월의 밤은…길다. (` | 303.8 | 303.8 | +0.0 | 300.6 | +3.2 |
| P7 `11월에는…있다. (` | 1346.6 | 1346.6 | +0.0 | 1343.4 | +3.2 |
| P1 `고 마감 시점 · ` | 674.0 | 674.0 | +0.0 | 671.7 | +2.3 |
| P7 `는 출발점으로 생격: ` | 1639.6 | 1639.6 | +0.0 | 1637.5 | +2.1 |

**Fixed − wave-C = +0.0 on all 10 lines.** The fix restores the
verified-correct geometry exactly; the fixed−R2 column reproduces
the measured deltas of §2.1.

### 6.2 Extracted-text diff (fixed vs R2 build, print AND web)

Identical on P1–P6 and P8; P7 differs by exactly **8 inserted single
spaces** — one at each of the 8 `Страница` junctions, nothing else.
In the rendered PDFs the Korean span is byte-identical in both builds
(same ink, same bbox); the `Страница` span sits ~4.3 SVG units
further right in the fixed build. Visual check (300 dpi crops):
`ru-ko-p7-junction-FIXED.png` shows `. ( Страница 1)` with a clear
space; `ru-ko-p7-junction-R2.png` shows `. (Страница 1)` jammed.

## 7. Summary + disposition (for the sync step — NOT applied here)

| Item | Value |
|---|---|
| ru-ko probe | **GREEN — all gates pass, 0 real joins** |
| Occlusion | 8 TEXTX → **0 flags** |
| check_core collisions | 10 → **0** (rc=0, BAD 0, gloss 0) |
| Census | 239/416 (BEFORE) → **95/223** (AFTER, print = web) |
| Freeze | **8/8 SVG SHA**, print PDFs byte-identical |
| New print SHA | `62538d21…` (22,005,230 B) |
| New web SHA | `da80b173…` (3,510,692 B) |
| Portability | **GO for all 14 copies** (§4); also safe for it-ru (0/3,893) |

- **GO.** Port the §3 diff to all 14 production `svglib.py` copies
  (and to `2026-w47-it-ru/svglib.py`, the 15th carrier, so the family
  stays byte-identical). The 5 GREEN R2 editions (ru-it/pt/nl/ja/zh-tw)
  need NO rebuild: the sweep proves the diff cannot change their
  geometry (0 differing runs over 90,419 swept), so their R2 SHAs stand.
- ru-ko MUST be rebuilt after the port (not synced from this scratch
  build): rebuild from the patched production copy and re-verify the
  print SHA is `62538d215e2ef0cbe440faa23cb4e147dc78e9116e1b6db02fc07ca704635b27`
  plus occlusion 0 / collisions 0 — the freeze check (8/8 within
  scratch) makes a mismatch unlikely, but the sync step should confirm
  it rather than assume it.
- **Production integrity (final check, 2026-11-12 ~02:18 UTC): all 3
  production files (text.md + print + web) re-hashed — 0 mismatches
  vs the BEFORE SHAs in §1.** Production untouched throughout; no
  commit/push/lint; no KIT file edited. Disk at end: 99G used (below
  the 100G stop line).

## 8. Files in this scratch dir

- `REBUILD-LOG.md` (this file), `svglib.diff` (the exact §3 diff),
  `measure.py` + `measure.log` (§2.1, §2.3–2.4), `measure2.py` +
  `measure2.log` (§2.2 flank rule, Q3–Q5), `portability.py` +
  `portability.log` (§4 sweep), `run_ko.sh` (the driver),
  `driver-run.out`, `src-edition/2026-w47-ru-ko/` (the patched
  source edition — only `svglib.py` differs from production),
  `port/<edition>/svglib.py` (the §3 edit applied to all 14 + it-ru;
  `assets` symlinked for import).
- Per-edition `ru-ko/`: `before-sha.txt`, `after-sha.txt`,
  `after-prod-sha.txt`, `run_build{1,2}.log`, `webpdf1.log`,
  `driver.log`, `census-AFTER-{print,web}.txt/.json`,
  `gaps-AFTER.txt` (+ `gaps-AFTER-web.txt`), `crops/`,
  `gates/` (`p8-ed.json`, `p8-compare.json`, `p8-extract.log`,
  `p8-compare.log`, `check_core.log`, `occlusion.json`,
  `occlusion.log`, `freeze.log`, `textlayer.log`, `morozko.log`),
  `build1/` + `build2/` (full run_build scratch outputs).
- Visual evidence: `ru-ko-p7-junction-FIXED.png` (300 dpi crop,
  `. ( Страница` with clear space) and `ru-ko-p7-junction-R2.png`
  (same clip from R2's build, jammed).
