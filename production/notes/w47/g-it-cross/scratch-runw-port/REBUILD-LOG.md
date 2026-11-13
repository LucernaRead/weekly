# REBUILD-LOG — W47 `_run_w` port to the ru family + 3 *-ru editions; probe on ru-de GREEN

Date: 2026-11-11 ~23:59–2026-11-12 ~00:15 UTC. Worker: ru-family `_run_w` port + ru-de probe.
Probe edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-de/`
(svglib source: `2026-w47-it-ru/svglib.py`, md5 `ee3211298f274e02ade2d4ca318ce354`.)
Scratch dir (this log's home):
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-runw-port/`

## VERDICT: PROBE GREEN — GO for the rebuild waves

The `_run_w` fix (sum of cached single-char advances, used ONLY inside
`Page.text`) was ported byte-identically into all 14 target svglib.py
files. The ru-de probe build clears **all 15 real joins** the Medium
fix left (12 in the Medium log's §3a table + the 3 punctuation-junction
joins `результатов+`, `—скидка`, `—поздравляю` that were in the Medium
census JSON but not in its prose table). Probe census: **12 tokens /
15 boundaries, print AND web — all 15 are the previously-cleared false
positives** (ARROW cases at normal gaps, `A2→B1/B2` diagram connectors,
`✓Mustertext` at the normal median). Gates all pass, freeze 8/8, SVG
text content byte-identical to the Medium build. Production PDFs
untouched throughout (SHAs re-verified after every step).
No production PDF was rebuilt; no commit/push/lint; no other edition
touched.

## 1. The port — 14 files

Source `_run_w` block taken verbatim from it-ru (comment block +
`_adv_cache`/`_adv`/`_run_w`, lines 162–188 of the source), inserted
after `text_w`; the same 4 `Page.text` call sites repointed
(`total`, per-run `w`, leading-space `_lw`, re-measured `w`).
`text_w`/`wrap` untouched in every file. `py_compile` passes on all 14.

| File | Before md5 | After md5 | Bytes |
|---|---|---|---|
| `core-ru/svglib.py` | 781059e6784b789c1179446e15b8f6ad | ee3211298f274e02ade2d4ca318ce354 | 21569 → 22924 |
| `2026-w47-ru-de/svglib.py` | 781059e6784b789c1179446e15b8f6ad | ee3211298f274e02ade2d4ca318ce354 | 21569 → 22924 |
| `2026-w47-ru-en/svglib.py` | 781059e6784b789c1179446e15b8f6ad | ee3211298f274e02ade2d4ca318ce354 | 21569 → 22924 |
| `2026-w47-ru-es/svglib.py` | 781059e6784b789c1179446e15b8f6ad | ee3211298f274e02ade2d4ca318ce354 | 21569 → 22924 |
| `2026-w47-ru-fr/svglib.py` | 781059e6784b789c1179446e15b8f6ad | ee3211298f274e02ade2d4ca318ce354 | 21569 → 22924 |
| `2026-w47-ru-it/svglib.py` | 781059e6784b789c1179446e15b8f6ad | ee3211298f274e02ade2d4ca318ce354 | 21569 → 22924 |
| `2026-w47-ru-ja/svglib.py` | 781059e6784b789c1179446e15b8f6ad | ee3211298f274e02ade2d4ca318ce354 | 21569 → 22924 |
| `2026-w47-ru-ko/svglib.py` | 781059e6784b789c1179446e15b8f6ad | ee3211298f274e02ade2d4ca318ce354 | 21569 → 22924 |
| `2026-w47-ru-nl/svglib.py` | 781059e6784b789c1179446e15b8f6ad | ee3211298f274e02ade2d4ca318ce354 | 21569 → 22924 |
| `2026-w47-ru-pt/svglib.py` | 781059e6784b789c1179446e15b8f6ad | ee3211298f274e02ade2d4ca318ce354 | 21569 → 22924 |
| `2026-w47-ru-zh-tw/svglib.py` | 781059e6784b789c1179446e15b8f6ad | ee3211298f274e02ade2d4ca318ce354 | 21569 → 22924 |
| `2026-w47-nl-ru/svglib.py` | 78fdfbb037538b1f8a738434ea90a782 | 8630b52f57bc4be209ef6ff4e51797a8 | 18114 → 19469 |
| `2026-w47-pt-ru/svglib.py` | 4228b7e7fc52caaec9d690f614755b4a | f1e0895cebf46c98b864657073004c6c | 18104 → 19459 |
| `2026-w47-zh-cn-ru/svglib.py` | a6fd6f1d41339fc0688f287e83273dfc | ce693ad4ff1d7ca6e8765c111c524ae0 | 29686 → 31041 |

Verification of "only the fix changed" (no pre-patch copies were saved,
so this was proved by reversal):
- All 11 ru copies are now **byte-identical to the it-ru fixed source**
  (md5 `ee3211298f…`); the pre-patch `diff core-ru it-ru` showed exactly
  the block insert + the 4 repoints, so the change is exactly the fix.
- For the 3 *-ru files (and 2 ru files as cross-checks), reverse-patching
  the current file (drop the block, restore the 4 `getlength` lines)
  reproduces the recorded before-md5 **exactly**
  (`patch_svglib.py` + the reverse check in this dir). The block itself
  is byte-identical to the source block in all 14 files.
- One patch-script bug caught during the run: my first slice of the
  source block omitted the blank line after `_run_w`'s return, so the
  first pass left the 11 ru files 1 byte short of it-ru; fixed by
  inserting the blank line, after which all 11 match it-ru exactly.
  A second bug: a substring `count()` double-counted the `w = …`
  repoint line inside the `… if t else 0.0` line — replaced with
  exact-line matching (each repoint line asserted to occur exactly once).

## 2. BEFORE state (ru-de production, Medium fix — wave A rebuild)

Recorded before the probe; the brief's proof-note SHAs
(print `872b4f1c…`, web `9aad0067…`) are the PRE-Medium values — wave A
had since rebuilt ru-de with the Medium fix, so the on-disk values
below are the true before-state and were re-verified unchanged after
every probe step.

| File | Bytes | SHA-256 |
|---|---|---|
| `2026-w47-ru-de.text.md` | 63,471 | `d0f9b48c8fab4df8bb39acfdfebfbc6ad6cf0f09e75891449d13a0f1ce2dcc0f` |
| `Lucerna-VOL4-ru-de.pdf` (print) | 21,230,193 | `80024034da684b62db63a3671866f85fc4c913f56ebcb48ebca1603aa4cc31e3` |
| `Lucerna-VOL4-ru-de-web.pdf` (web) | 3,384,428 | `05b0a7abf59aa3617e5e75e94361460a692a144fb883017ba64bdf2198319992` |
| `svglib.py` (Medium fix) | 21,569 | md5 `781059e6784b789c1179446e15b8f6ad` — VERIFIED first, matches task |

BEFORE census (reproduced exactly with the Medium worker's
`census.py`, same method): **27 distinct tokens / 30 boundaries**,
print = web. (The Medium log's prose says "24 tokens / 27 boundaries",
but its own `census-print-after.json` says 27/30 — the JSON is
authoritative and my run reproduces it row for row. The 3 extra tokens
are the punctuation-junction joins `результатов+`, `—скидка`,
`—поздравляю`, which the prose table omitted.) The 15 real joins are
the 12 in the Medium log §3a plus those 3; the other 15 boundaries are
the cleared false positives listed in §3b.

## 3. Probe build (scratch only)

- `tools/venv/bin/python tools/run_build.py --build
  production/2026-w47/2026-w47-ru-de --out
  <this-dir>/ru-de-probe --steps run,render` → RC=0 (~3 min),
  print PDF 21,229,165 B; wrapper integrity: "production unchanged
  (42 files re-hashed)".
- `tools/webpdf.py <probe>/build-copy/svg
  <probe>/build-copy/Lucerna-VOL4-ru-de-web.pdf` → 3,383,424 B,
  57,908 text bytes, RC=0.
- Probe SHAs: print
  `1920da86eb76624b300a6c76f6acc3a0bfbb2921aab37ad111cd434e238e396c`,
  web
  `254eb45f9c07b263b332ef61bd4d9a2908d90a1616d1a4507ea54607436ec1c9`.
- Production SHAs re-verified immediately after the probe and again at
  end of work: identical to §2 (print `80024034…`, web `05b0a7ab…`;
  text.md `d0f9b48c…` unchanged).
- Second independent rebuild (`--out <this-dir>/ru-de-probe2`) → **8/8
  SVG SHA match** vs the first probe build; the two print PDFs are also
  byte-identical (same SHA `1920da86…`). Its run-build log also shows
  TOTAL 150 and "production unchanged (42 files re-hashed)". (Its
  build-copy web PDF is the stale copied production file, not a fresh
  build — only its SVGs/print PDF were used for the freeze check, same
  caveat as the it-ru probe.)

## 4. Census + gaps on the probe build (print AND web identical)

Census (`census.py`, the Medium worker's tool, text.md vocabulary):

| | BEFORE (production) | THIS probe |
|---|---|---|
| distinct join tokens | 27 | **12** |
| total join boundaries | 30 | **15** |

The 12 remaining tokens / 15 boundaries are exactly the previously
cleared false positives — **0 real joins**:

| Token | Pages | Gap (pt) | Verdict |
|---|---|---|---|
| `→После` ×3 | P7 | 3.75 | FP (normal; space-only-run extraction artifact) |
| `→Родительный` ×1 | P7 | 3.75 | FP (normal) |
| `A2→B1` (2 bounds), `A2→B2` (1 bound) | P1 | 0.0 | FP — deliberate diagram connectors, read as designed |
| P8 `→выходят/рассказывает/снял/сыграли/играет/победило/работаем` | P8 | 2.40–2.41 | FP — at the normal median (2.36 pt at 9.8 pt); NOT joins per task |
| `✓Mustertext` | P8 | 2.41 | FP (normal 2.37–2.38 on the line) |

All 15 real joins are GONE from both PDFs (none appears in either
census). Separated ink gaps (`gap_rude.py`, PyMuPDF rawdict), print =
web on every measurement:

| Split | BEFORE gap | PROBE gap | Normal on line | Verdict |
|---|---|---|---|---|
| P8 `Imperativ:` \| `не` | 0.55 pt | **2.35 pt** | 2.37 | separate |
| P8 `13` \| `ноября` | 1.43 pt | **2.47 pt** | ~2.5 | separate; text layer now `13 ноября`, fused form absent |
| P4 `20` \| `ноября` | 2.18 pt | **3.52 pt** | ~3.55 | separate; text layer `20 ноября` |
| P2 `19` \| `ноября` | 2.11 pt | **3.48 pt** | 3.48 | separate; text layer `19 ноября` |
| P5 `16` \| `ноября` | 2.24 pt | **3.68 pt** | 3.66 | separate; text layer `16 ноября` |
| P4 `A.` \| `на` | 1.68 pt | **3.48 pt** | ~3.5 | separate |
| P3 `A.` \| `биография` | 2.20 pt | **3.63 pt** | 3.62–3.71 | separate |
| P7 `A.` \| `снег` | 2.28 pt | **3.71 pt** | 3.69–3.78 | separate |
| P7 `A.` \| `цена` | 2.29 pt | **3.72 pt** | 3.75 | separate |
| P7 `A.` \| `точно` | 2.29 pt | **3.71 pt** | 3.44–3.75 | separate |
| P7 `Tauwetter;` \| `мокрый` | 1.86 pt | **3.43 pt** | 3.14–3.44 | separate |
| P7 `Rabattcode;` \| `возврат` | 1.97 pt | **3.47 pt** | ~3.1–3.4 | separate |
| P4 `результатов` \| `+` | 1.96 pt | **3.01 pt** | ~2.8–3.5 | separate |
| P8 `—` \| `скидка` | 1.44 pt | **2.41 pt** | 2.42 (sibling line) | separate |
| P8 `—` \| `поздравляю` | 0.46 pt | **2.41 pt** | ~2.4 | separate |

The DATE gaps now land essentially exactly on the normal for their
lines (19ноября 3.48 vs normal 3.48; 20ноября 3.52 vs ~3.55; 16ноября
3.68 vs 3.66) — the predicted kern correction, not an overshoot.

Byline (must stay ~2.89 pt): **unchanged** — P1/P2/P3/P5/P6 2.89 pt,
P4 ("От спортивной редакции Lucerna") 2.82 pt, print = web. The
Cyrillic byline runs carry ~zero kern, so `_run_w` leaves them alone,
as predicted.

Visual crops (200 dpi from the probe print PDF, this dir):
`p8-13noyabrya-probe.png` — "Когда «чёрная пятница» на Ozon?
A. 13 ноября – 2 декабря ·" visibly separated;
`p8-imperativ-probe.png` — "82. Не спешите с покупкой. —
Verneinter Imperativ: не спешите" visibly separated.

## 5. Gates on the probe build — ALL PASS

- `run.py` TOTAL **150** (both probe builds; zero overflow — from
  run-build.log).
- p8 extract **150/150** (`ru-de/p8-extract.json`).
- p8 compare vs core-ru: **CLEAN**, keydiff **[137, 138, 139, 140]**
  (`ru-de/p8-compare.json`).
- Occlusion audit on probe SVGs: **0 flags** (selftest OK).
- Freeze reproducibility: **8/8 SVG SHA match** between the two
  independent probe builds; print PDFs byte-identical.
- Print/web text layers: **identical per page** on all 8 pages
  (37,532 chars each; Medium was 37,514 — the +18 is the reappearing
  space chars at the 15 fixed boundaries plus tokenization splits).
- SVG text content: **byte-identical to the Medium build** — text-node
  multisets identical on all 8 pages (966/920/753/915/836/790/970/1669
  nodes); only `x` positions moved (456/379/325/401/364/329/524/1047
  nodes per page). No reflow: node counts identical, line-breaking
  untouched by construction (`text_w`/`wrap` verified unchanged by the
  reverse-patch md5 check).
- Web PDF 3,383,424 B < 7 MB; print PDF 21,229,165 B sane.
- `ГЛАГОЛЫИ` (bold-caps bbox artifact): does not appear in this
  census; not flagged, per task.

Not run (not in the task's gate list): `check_core.py` (the Medium
gates ran it; it operates on the edition dir and was not needed to
decide this probe — the p8/occlusion/freeze/census gates above are the
specified set).

## 6. Go / no-go for the rebuild waves

**GO.** The probe passes every gate in the task, print AND web.
The rebuild waves may proceed per edition:
run_build (scratch) + webpdf, with the same before/after census and
gate checks per edition. Notes for the waves:

- The 3 *-ru editions (nl-ru, pt-ru, zh-cn-ru) carry their own patched
  svglib copies (after-md5s in §1); their P8 LAT→CYR joins from the
  it-ru sweep (`aankomenтребует` 1.44 pt, `vencerпрошедшее` 0.77 pt,
  `IGобыграла` 1.32 pt, `GENвышла` 1.45 pt) are the same defect class
  and should clear the same way — verify per edition, do not assume.
- The other 10 ru-family editions share the ru core, so the shared
  `13ноября` line (and the P2/P4/P5 DATE lines, same core lines) should
  clear identically; still verify each edition's census, since each has
  its own native-language layers.
- Wave-C note (from the it-ru log §9, unchanged by this probe):
  core-ru's P8 Morozko image + caption are LOST in the Medium-fix
  rebuild (keys flow grew, tripping the `content8.py:131–140`
  conditional) — the core-ru re-rebuild is expected to need that
  separate layout fix; this probe does not cover it.
- `webpdf.py` font subsetting is non-deterministic across processes
  (it-ru log §7: 5-byte subset-stream difference); probe-vs-production
  web SHAs will differ in subset bytes only even for identical content.

## 7. Files in this scratch dir

- `REBUILD-LOG.md` (this file), `patch_svglib.py` (the port script),
  `census.py` + `line_gaps.py` (copied from
  `scratch-ru-rebuild-ru-de/` — the Medium worker's tools, unmodified),
  `gap_rude.py` (fixed-join/byline/arrow gap measurement + text-layer
  check + P8 crops), `census-before-print.json`,
  `census-probe-print.json`, `census-probe-web.json`,
  `p8-13noyabrya-probe.png`, `p8-imperativ-probe.png`,
  `ru-de/` (p8-extract.json, p8-compare.json),
  `ru-de-probe/` + `ru-de-probe2/` (run_build scratch: `build-copy`,
  `run-build.log`), `probe2.log`.
- Only files written outside production svglib.py files + this scratch
  dir: none.

## 8. Incidental notes (not gating)

- `~/AGENTS.md` changed on disk mid-task (a push-loop lesson added by
  another worker, 2026-11-11: background-exec loops vs nohup sleep
  death). Unrelated to this task; noted only because the runtime
  flagged the injected copy as stale.
- The Medium log's prose census count ("24 tokens / 27 boundaries")
  disagrees with its own JSON (27/30); the JSON is authoritative and
  was reproduced exactly. The 3 tokens the prose omitted are real
  joins of the same defect class, and all 3 cleared in this probe.

## CORRECTION (coordinator, 2026-11-12 02:47 UTC)
The size column in the table above ("21569 → 22924") is wrong by 87 B on the
post-`_run_w` figure. Measured on disk by the ru-ko port worker (2026-11-12
02:44 UTC): the `_run_w` file (md5 `ee321129…`, verified pre-patch backup in
`scratch-ru-ko-port-rebuild/pre-patch/`) is **23,011 B**, and after the Hangul
fix it is **24,488 B** (delta +1,477 B, the same 24-line insertion, uniform
across all 15 copies). The md5s in the table are the binding check and are
unaffected — they match exactly. Only the byte counts were mis-recorded.
