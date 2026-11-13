# REBUILD LOG — 2026-w47-ru-pt (wave B, ru word-spacing rebuild)

- Edition: `production/2026-w47/2026-w47-ru-pt/` (Russian target × Portuguese reader, VOL.4)
- Date: 2026-11-11 23:25–23:45 UTC. No commit, no push, no lint.
- Scratch: `hidden_files/w47/scratch-ru-rebuild-pt/` (this log, `census.py`, `run_build.log`, `webpdf.log`, `gates/`, `census-*.txt/.json`, `textlayer.log`, `pre-snapshot.txt`). Build copy under `build/`.
- Root cause (per brief): PIL measured Cyrillic with Regular faces while CairoSVG renders Medium faces (weight=100 → Medium), so rendered ink overran the space. Fix at source: `svglib.py` `_PATH` entries for `("serif",False,"noto"/"noto_i")` and `("sans",False,"sans_noto"/"sans_noto_i")` now point at NotoSerif-Medium/MediumItalic and NotoSans-Medium/MediumItalic.
- svglib.py md5 verified BEFORE the rebuild: `781059e6784b789c1179446e15b8f6ad` ✓.

## §0 BEFORE state

| file | SHA-256 | bytes |
|---|---|---|
| `2026-w47-ru-pt.text.md` | `ab21732233d80c5af14a2a579ef611370fb228ba29376d9e2ce9186a7c613a02` | 65,116 |
| `Lucerna-VOL4-ru-pt.pdf` (print) | `4d726d922b33b6c38ab93e7ed1c47c8913817a5fa4e3bbc59988ff232bec61ed` | 21,205,591 |
| `Lucerna-VOL4-ru-pt-web.pdf` (web) | `6f197ab96c9735caf94a98c97e716b594a120870a661b7b998238f63e264d20f` | 3,383,561 |

## §1 Rebuild

- `tools/run_build.py --build production/2026-w47/2026-w47-ru-pt --out <scratch>/build --steps run,render`: rc=0. run.py TOTAL 150; render.py exit 0.
- Promoted from the scratch build copy into production: `svg/*.svg` ×8 + `Lucerna-VOL4-ru-pt.pdf` only (cards NOT re-copied — footprint per brief).
- `tools/webpdf.py svg Lucerna-VOL4-ru-pt-web.pdf`: rc=0, 3,382,131 B, 58,390 text bytes.
- `text.md` SHA after: `ab217322…` — UNCHANGED ✓.

## §2 AFTER state

| file | SHA-256 | bytes / mtime (UTC) |
|---|---|---|
| `2026-w47-ru-pt.text.md` | `ab21732233d80c5af14a2a579ef611370fb228ba29376d9e2ce9186a7c613a02` | 65,116 (unchanged) |
| `Lucerna-VOL4-ru-pt.pdf` (print) | `b4a3fdfebc3fa5c23786f496ed1a2416698f8aa5eb5687a9213d3f7c3118a3f9` | 21,204,114, 2026-11-11 23:28:50 |
| `Lucerna-VOL4-ru-pt-web.pdf` (web) | `38b7fa500c5a28f5a83919ae4327b017d30fbb81fa732a95947e624e463488fa` | 3,382,131, 2026-11-11 23:30:39 |

Final on-disk web SHA re-verified at end of work: still `38b7fa50…`.

## §3 Gates (all green)

| gate | result |
|---|---|
| run.py | exit 0, TOTAL 150 |
| render.py | exit 0 |
| p8.py extract | 150/150 |
| p8.py compare vs core-ru | CLEAN, keydiff [137, 138, 139, 140] |
| check_core.py | exit 0; golden BAD 0, gloss fails 0; orphan 1 (P7 y553 `”».`, same benign class as before); same-baseline collisions 0 |
| occlusion_audit.py | 0 flags (selftest OK; was 42 TEXTX before) |
| freeze baseline | 8/8, run twice (8/8 both — reproducibility verified) |
| freeze diff vs core-ru | informational only |
| print/web text layers | multiset identical overall + per page 8/8 (31,105 non-ws chars each; byte-identical) |

## §4 Census (word joins; `census.py` token-split + char-gap method)

- BEFORE: 132 join candidates in print, 132 in web.
- AFTER: 6 naive candidates in print, 6 in web — ALL cleared as false positives:
  - 2× `A2→B1` / `A2→B2` (P1 kicker): level-range arrows.
  - 4× date options `19ноября` (P2), `20ноября` (P4), `16ноября` (P5), `13ноября` (P8): trailing-space spans whose layout gap is real and visibly spaced (same mechanism as ru-it, where 300 dpi crops were viewed).
- **Real joins: 0 in print, 0 in web.**
- Second-defect-class check (P8 Latin-run trailing-space overrun, per the it-ru probe heads-up): NO P8 Latin→Cyrillic joins present — the only P8 candidate is the `13 ноября` date option. This edition is NOT blocked by the second fix.
- Byline `От редакции Lucerna`: real space char, gap 2.89 pt on P1–P3/P5/P6, 2.82 pt on P4 (`От спортивной редакции Lucerna`), vs 1.10 pt with no space char before. `Профессиональные праздники` spaced.

## §5 KIT updated

- §5: print SHA/bytes, web SHA/bytes, pdftotext bytes 58,327 → 58,390 (char count 31,105 unchanged, matches this rebuild's measurement).
- §7: Fix 2 record appended. No other KIT content altered.

## §6 Production integrity

- Pre/post snapshot diff: exactly 11 files changed — `svg/*.svg` ×8, print PDF, web PDF, `WEEKLY-KIT.md`. No other edition touched.
- No commit / push / lint. Core-ru untouched.
