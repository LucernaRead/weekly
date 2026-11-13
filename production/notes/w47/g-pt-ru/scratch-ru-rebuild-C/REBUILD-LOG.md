# W47 ru rebuild — wave C (core-ru, ru-ko, ru-zh-tw) — REBUILD LOG

Date: 2026-11-11 (UTC). Fix: svglib.py Medium measurement
(`781059e6784b789c1179446e15b8f6ad` verified on all 3 editions before any
build). Method: `tools/run_build.py --steps run,render` (scratch copy) +
`tools/webpdf.py`, then census (token-split vs text.md vocab, PyMuPDF char
gaps) + KIT §5 gates. No commit/push/lint. Production untouched except where
an edition is explicitly synced below.

## 0. BEFORE state (all 3 editions, recorded 2026-11-11 ~23:18 UTC)

| Edition | text.md (SHA, bytes) | print PDF (SHA, bytes) | web PDF (SHA, bytes) |
|---|---|---|---|
| core-ru | `348511e0…` 60,953 (`2026-w47-ru-core.text.md` = `2026-w47-ru-zh-cn.text.md`, byte-identical) | `d60fbd6c…` 31,429,147 | `b5d67aeb…` 4,025,900 (mismatch vs KIT `2f995f1d…`/4,025,834 — concurrent web-rebuild drift, pre-existing) |
| ru-ko | `5e9bd672…` 65,012 | `78e4442a…` 22,007,810 | `34e1c1db…` 3,513,245 (mismatch vs KIT `3bf39ecf…`/3,513,230 — same drift) |
| ru-zh-tw | `277a24f8…` 60,850 | `094b6a3b…` 24,784,332 | `eba60ec2…` 3,994,661 (matches task brief + KIT) |

Full 129-file SHA snapshot: `before.json` in this dir.

## 0b. BEFORE census (naive token-split, all 3 editions, print = web)

- core-ru: 231 candidates → **148 TRUE JOINs (123 types)**; cleared 70 extraction
  (CJK/Latin segmentation), 8 intra-word (`Вс`×7 P4, `вс`×1 P6, gap 0.0 — same
  FP class as the ru-de probe), 5 real-space (`→После`×3, `→Родительный`,
  `后面用гол：забили21`, gaps 3.29–3.75pt). Byline 1.10pt, no space char, P1–P6.
  `Профессиональные праздники` fused P2×2 (1.55/1.30pt), P6×1 (1.35), P7×1 (1.40).
  JOIN gap band 0.63–2.68pt, median 2.04 — same band as the ru-de proof.
- ru-ko: 391 candidates → **167 TRUE JOINs (140 types)**; cleared 211 extraction,
  8 intra-word, 5 real-space. Byline/prof identical to core.
- ru-zh-tw: 231 candidates → **148 TRUE JOINs (123 types)**; cleared as core.
  Byline/prof identical to core.
- Note: the 148/167 counts include one known artifact each, `ГЛАГОЛЫИ` P3
  (bold Cyrillic caps head; probe: bold already matched, 2.62pt is a PyMuPDF
  glyph-bbox artifact, true visual gap is a full space). Net true joins
  excl. artifact: core 147, ko 166, zh-tw 147.

## 1. core-ru — BLOCKED (do NOT sync; production untouched)

Build: `run_build.py` rc=0, run.py exit 0, TOTAL 150, render.py exit 0,
integrity "production unchanged (45 files)". Scratch print 28,720,800 B,
web 3,705,986 B.

### 1a. Medium fix WORKS
- Byline P1–P6: 1.10pt, no space → **2.89pt (×5), 2.82pt (P4), space char
  present** — exactly the probe's numbers.
- `Профессиональные праздники`: 1.55/1.30/1.35/1.40pt fused → **4.39/3.48/
  3.67/3.95pt, space chars present** — exactly the probe's numbers.
- Census 148 → **12 JOIN verdicts** (print = web).
- p8 extract 150/150; compare vs old baseline **CLEAN, keydiff []**.
- check_core rc=0: golden BAD 0, gloss 0, orphans 5 (same P7 set as KIT),
  collisions **0** (was 1, P1 y1712 — gone). P8 SVG text chars 8047 (was 8191;
  see §1c — the Morozko caption accounts for 144 of the drop).
- occlusion **0 flags** (was 42 TEXTX — the false-positive class is gone).
- print/web text layer: multiset identical overall + per page (25,807 chars),
  raw text byte-identical.

### 1b. BLOCKER 1 — 11 remaining joins are the SECOND defect class
Heads-up (parent, 2026-11-11): it-ru probe found a second class — a Newsreader
(Latin) run renders wider than PIL measures it, so its TRAILING space overruns
and the following Cyrillic word fuses. A dedicated fix worker is on it.
Core-ru's 11 remaining joins (excl. `ГЛАГОЛЫИ` artifact, unchanged 2.62pt)
are exactly this pattern, gaps essentially UNCHANGED by the Medium fix
(Δ ≤ 0.08pt, old vs new on the same boundaries):

| Token | Page | Old gap | New gap | Run structure (new SVG) |
|---|---|---|---|---|
| `19ноября` | P2 | 2.19pt (spaced in extraction) | 2.11pt | Newsreader run `': 19 '` + Noto Serif `ноября` |
| `20ноября` | P4 | 2.18pt | 2.18pt | Newsreader digits + Cyrillic |
| `16ноября` | P5 | 2.32pt (spaced in extraction) | 2.24pt | Newsreader digits + Cyrillic |
| `13ноября` | P8 | 1.50pt | 1.43pt | Newsreader digits + Cyrillic |
| `→выходят` | P8 | 2.40pt | 2.33pt | CJK SC run `→` + Newsreader ` ` + Noto Serif `выходят` |
| `→рассказывает` | P8 | 2.32pt | 2.32pt | same pattern |
| `→снял` | P8 | 2.40pt | 2.40pt | same pattern |
| `→сыграли` | P8 | 2.41pt | 2.41pt | same pattern |
| `→играет` | P8 | 2.40pt | 2.40pt | same pattern |
| `→победило` | P8 | 2.40pt | 2.40pt | same pattern |
| `→работаем` | P8 | 2.40pt | 2.40pt | same pattern |

Notes: `19ноября`/`16ноября` were already narrow-gap (2.19/2.32pt) before —
below the normal 2.78–4.36pt band — just above PyMuPDF's space-detection
threshold, so the old census tokenised them as spaced; the defect was already
there. The 6 `→` cases were the second boundary of 3-part before-tokens
(`выходить→выходят` etc.); the Medium fix fixed the first (Cyrillic-side)
boundary and left the second (arrow-side) untouched. The P5 before-token
`промокод→` (Cyrillic-side boundary) is gone after the fix, confirming the
split. Per the heads-up: 0-joins bar NOT waived, no renderer fix attempted,
edition reported blocked-by-second-fix.

### 1c. BLOCKER 2 — P8 Morozko image + caption LOST to the conditional skip
- New print PDF: 5 image xrefs (P1/P2/P4/P5/P7); old: 6 (incl. P8 Morozko
  906×1129). New P8 SVG: ZERO `Морозко`/`Билибин` hits (old: present).
- Text multiset old−new: 127 chars OLD-only, 0 NEW-only — exactly the P8
  caption + credit (`«Морозко»: иллюстрация Ивана Билибина, 1932 год.
  Зимняя сказка — к ноябрю. Иллюстрация: Иван Билибин — общественное
  достояние (Wikimedia Commons)`).
- Freeze diff old-SVG → new-SVG: P1–P7 only space/punctuation
  re-segmentation from re-wrapping (no word lost); P8 removed 27 distinct /
  37 count — the Morozko caption words + re-segmentation; added Latin
  `B. ` is re-segmentation, not new content.
- Mechanism (`content8.py:131–140`): image placed only if keys end in col 3
  AND `img_y + 250 + 90 < 2560` (i.e. keys end y < 2196). Old: `P8 keys end
  col 3 y 2188.39` → placed, `morozko ends 2579.99`. New: `P8 keys end col 3
  y 2216.58` (+28.19 — wider Cyrillic re-wrapped the key lines into ~2 more
  lines) → `P8 morozko SKIPPED: no room`. A layout decision (shrink image /
  tighten keys) is needed; not a rebuild's call. Do NOT sync a P8 that loses
  the illustration + caption.
- Print size drop 31,429,147 → 28,720,800 B and web 4,025,900 → 3,705,986 B is
  fully explained by the dropped Morozko image (same font inventory, 69
  distinct fonts both sides, 0 NEW-only chars).

### 1d. Core-ru disposition
- **NOT synced. Production files untouched** (verified: `before.json` hashes
  still hold for core-ru; the only writes were to this scratch dir).
- text.md files: two `.text.md` in build-copy byte-identical to production
  (verified by presync).
- KIT NOT updated (no shippable build to record).
- Scratch build kept at `core-ru/build/` as evidence for the second-fix
  worker and the layout decision. Backup of pre-rebuild files:
  `core-ru/backup-before/` (8 SVG + print + web). Baseline p8:
  `core-ru/p8-baseline.svg`.

## 2. ru-ko — BLOCKED-by-second-fix (do NOT sync; production untouched)

Build: `run_build.py` rc=0, run.py exit 0, TOTAL 150, render.py exit 0,
integrity "production unchanged (42 files)". Scratch print 22,006,276 B
(old 22,007,810, −1,534), web 3,511,719 B (old 3,513,245, −1,526).
`P8 keys end col 3 y 2231.27`, `P8 morozko SKIPPED` — same as the old build;
ko never had the Morozko image (0 hits in old P8 SVG), so nothing is lost.

### 2a. Medium fix WORKS (same numbers as core)
- Byline P1–P6: 2.89/2.89/2.89/2.82/2.89/2.89pt, space chars present.
- `Профессиональные праздники`: 4.39/3.48/3.67/3.95pt, spaced.
- Census 167 → **13 JOIN verdicts** (print = web).
- p8 extract 150/150; compare vs production core-ru **CLEAN, keydiff
  [137, 138, 139, 140]** — exactly as expected.
- check_core rc=0: golden BAD 0, gloss 0, orphans 1 (P7 y553 `”».`, same as
  KIT), collisions **0** (KIT: 1, P1 y1712 — gone). P8 SVG text chars 8740.
- occlusion **0 flags** (KIT re-fanout: 42 TEXTX — gone).
- print/web text layer: multiset identical overall + per page (26,535 chars —
  same as the KIT re-fanout count), raw text byte-identical.
- Content conservation: images 5 old = 5 new; text multiset OLD-only 0 /
  NEW-only 0; freeze diff old→new: only space/punct re-segmentation, ZERO
  Cyrillic-bearing removed strings.

### 2b. BLOCKER — 12 second-class joins (same 11 as core-ru + 1 Korean)
Identical gaps to core-ru for the shared 11 (dates 2.11/2.18/2.24/1.43pt;
arrows 2.33/2.32/2.40/2.41/2.40/2.40/2.40pt; all pre-existing, Δ ≤ 0.08pt
vs old). Plus one ko-only P8 token:
- `а는대조를나타냅니다` P8, gap 2.44pt (old 2.43pt, Δ0.01). SVG line:
  `… выходные. — а` (Noto Serif) + `는` (Noto Serif CJK SC) + Newsreader
  ` ` + `대조를` (CJK SC) + ` ` + `나타냅니다` (CJK SC). The fused boundary
  is the CJK SC run `는` + trailing space + CJK SC `대조를` — same mechanism
  family (trailing space after a non-Cyrillic run overruns; gap unchanged
  by the Medium fix), in P8 answer keys, pre-existing. Flagged explicitly
  because it is CJK-SC→CJK rather than Latin→Cyrillic — the fix worker to
  confirm it is in scope.
- `ГЛАГОЛЫИ` P3 2.62pt: the known bold-caps artifact, unchanged.

### 2c. Calibration note (for the fix worker — applies to all 3 editions)
Known-good spaces in the NEW ko print PDF (space char present in the text
layer), by font/size: NotoSerif-Medium 9.8pt (P8-key size) median 2.36pt;
Newsreader16pt 9.8pt median 2.37pt; NotoSerif-Medium 14.2pt median 3.46pt;
18.0pt median 4.37pt. Against this:
- Date cases are unambiguously narrow: 1.43pt at 9.75pt (normal 2.36);
  2.11/2.18/2.24pt at body size (normal ~3.4–3.7).
- Arrow/CJK cases sit AT the normal median for their size (2.32–2.44pt at
  9.75pt vs 2.36–2.37 normal): the missing space char in extraction is the
  only signal — they are the mild end of the class, vs it-ru's 0.03–1.39pt.
  Reported as blocked per the heads-up (pattern + unchanged gap), not waived;
  severity is for the fix worker to judge.
- As with core-ru, two date tokens (`19ноября` 2.19→2.11, `16ноября`
  2.32→2.24) were already narrow before, just above PyMuPDF's
  space-detection threshold.

### 2d. ru-ko disposition
- **NOT synced. Production files untouched.**
- text.md in build-copy byte-identical to production (verified by presync).
- KIT NOT updated (no shippable build to record).
- Scratch build kept at `ru-ko/build/`; backup at `ru-ko/backup-before/`.

## 3. ru-zh-tw — BLOCKED-by-second-fix (do NOT sync; production untouched)

Build: `run_build.py` rc=0, run.py exit 0, TOTAL 150, render.py exit 0,
integrity "production unchanged (42 files)". Scratch print 24,782,811 B
(old 24,784,332, −1,521), web 3,993,152 B (old 3,994,661, −1,509).
`P8 keys end col 3 y 2188.39`, `P8 morozko ends 2579.99` — IDENTICAL to the
old (F1) build (verified in `scratch-ru-zh-tw-f1/run_build.log`, same two
lines); the keys flow did NOT grow, so the Morozko image SURVIVES. The
round-2 re-proof (a) verdict stands on content: this rebuild is
measurement-only (text.md byte-identical, see below).

### 3a. Medium fix WORKS (same numbers as core/ko)
- Byline P1–P6: 2.89/2.89/2.89/2.82/2.89/2.89pt, space chars present.
- `Профессиональные праздники`: 4.39/3.48/3.67/3.95pt, spaced.
- Census 148 → **12 JOIN verdicts** (print = web) — byte-for-byte the same
  12 as core-ru, identical gaps.
- p8 extract 150/150; compare vs production core-ru **CLEAN, keydiff
  [137, 138, 139, 140]** — exactly as expected.
- check_core rc=0: golden BAD 0, gloss 0, orphans 5 (same P7 set as
  KIT/core), collisions **0** (KIT: 1, P1 y1712 — gone). P8 SVG text chars 8178.
- occlusion **0 flags** (KIT: 42 TEXTX — gone).
- print/web text layer: multiset identical overall + per page (25,844 chars),
  raw text byte-identical.
- Content conservation: images 6 old = 6 new; text multiset OLD-only 0 /
  NEW-only 0; freeze diff old→new: only space/punct re-segmentation, ZERO
  Cyrillic-bearing removed strings. F1 fix survives: text.md SHA still
  `277a24f8…` (60,850 B), unchanged (see §4).

### 3b. BLOCKER — the same 11 second-class joins as core-ru
4 Newsreader-digit dates (2.11/2.18/2.24/1.43pt) + 7 CJK-SC-arrow P8 keys
(2.33/2.32/2.40/2.41/2.40/2.40/2.40pt) + the `ГЛАГОЛЫИ` P3 2.62pt artifact
(unchanged). All pre-existing, gaps Δ ≤ 0.08pt vs old. No Morozko issue,
no other issue. Blocked solely on the second class.

### 3c. ru-zh-tw disposition
- **NOT synced. Production files untouched.**
- text.md in build-copy byte-identical to production (verified by presync).
- KIT NOT updated (no shippable build to record).
- Scratch build kept at `ru-zh-tw/build/`; backup at `ru-zh-tw/backup-before/`.

## 4. Wave summary (all 3 editions BLOCKED, none synced)

| Edition | Medium fix | Gates (excl. census) | Census before → after | Blockers |
|---|---|---|---|---|
| core-ru | byline 2.89/2.82, prof 4.39/3.48/3.67/3.95 | p8 150/150 CLEAN [] / check_core 0 / occlusion 0 / text layers identical | 148 → 12 (11 2nd-class + `ГЛАГОЛЫИ`) | second class + **P8 Morozko lost** (keys y 2188.39→2216.58, image+caption dropped, 127 chars) |
| ru-ko | same | p8 150/150 CLEAN [137–140] / check_core 0 / occlusion 0 / text layers identical | 167 → 13 (12 2nd-class + `ГЛАГОЛЫИ`) | second class (+1 ko-only `а는대조를나타냅니다` P8, CJK→CJK); no image loss (never had it) |
| ru-zh-tw | same | p8 150/150 CLEAN [137–140] / check_core 0 / occlusion 0 / text layers identical | 148 → 12 (11 2nd-class + `ГЛАГОЛЫИ`) | second class only; Morozko survives |

- **Production integrity: 129 files hashed before (`before.json`) and after
  (`final.json`) — ZERO files changed.** No sync, no KIT edit, no commit/
  push/lint. The concurrent web-rebuild job did not rewrite any production
  web PDF during this wave (final snapshot = before snapshot).
- **text.md unchanged everywhere** (verified start and end): core both files
  `348511e0…` 60,953 B; ko `5e9bd672…` 65,012 B; zh-tw `277a24f8…` 60,850 B.
- **Scratch-built (blocked, NOT in production) PDFs:**
  - core-ru: print `07d01abe…` 28,720,800 B (2026-11-11 23:26:30 UTC);
    web `0e1c08db…` 3,705,986 B (23:27:28 UTC).
  - ru-ko: print `84263d68…` 22,006,276 B (23:38:14 UTC);
    web `48ca1aa4…` 3,511,719 B (23:40:31 UTC).
  - ru-zh-tw: print `8a118804…` 24,782,811 B (23:47:59 UTC);
    web `02cd58da…` 3,993,152 B (23:50:13 UTC).
- **What unblocks the wave:** (1) the dedicated second-fix worker's renderer
  fix, followed by a re-census (expect 0 joins + the `ГЛАГОЛЫИ` artifact
  unchanged at ~2.62pt); (2) for core-ru only, a layout decision on the P8
  Morozko conditional (`content8.py:131–140`: keys end y 2216.58 vs the
  <2196 threshold — shrink image 250→~230, tighten the +90 caption
  allowance, or accept the skip; NOT a rebuild's call). After both, the
  three scratch builds must be REBUILT (not just synced — the second fix
  changes measurement again) and re-gated.
- **Census-method note:** the naive token-split census clears non-Cyrillic
  tokens as extraction artifacts (ko: 211→219 clears, mostly Hangul+Latin
  adjacency at P8). One ko-only Cyrillic-bearing token,
  `а는대조를나타냅니다`, is reported under the second class but is CJK→CJK,
  not Latin→Cyrillic — the second-fix worker to confirm scope.
- **Freeze note:** the `freeze.py baseline` re-baseline step was not run as a
  production gate because no edition was synced (nothing to baseline
  against). The scratch builds were verified reproducible in the sense that
  `run_build.py` integrity re-hash passed and `freeze.py diff` old→new shows
  only re-segmentation (plus the core-ru Morozko loss). When the wave
  re-runs after the second fix, run `freeze.py baseline --build <ed>
  --core-svg <ed>/svg` on the SYNCED files as the KIT gate.

## Tools in this dir
- `snapshot.py` — 129-file SHA snapshot of the 3 edition dirs.
- `census.py` — naive token-split census (v3, line-token based) + byline +
  `Профессиональные праздники` probes.
- `presync.py` — scratch-output checks before sync (text.md identical,
  census, p8, check_core, occlusion, text layers).
- `gates.py` — production gates after sync (p8, check_core, occlusion,
  freeze re-baseline, text layers).
- `gapcheck.py` — OLD vs NEW ink gap at given token boundaries.
