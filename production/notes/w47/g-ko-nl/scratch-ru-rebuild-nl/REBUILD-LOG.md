# REBUILD LOG — 2026-w47-ru-nl (wave B, ru word-spacing rebuild)

- Edition: `production/2026-w47/2026-w47-ru-nl/` (Russian target × Dutch reader, VOL.4)
- Date: 2026-11-11 23:35–23:55 UTC. No commit, no push, no lint.
- Scratch: `hidden_files/w47/scratch-ru-rebuild-nl/` (this log, `census.py`, `run_build.log`, `webpdf.log`, `gates/`, `census-*.txt/.json`, `textlayer.log`, `pre-snapshot.txt`). Build copy under `build/`.
- Root cause (per brief): PIL measured Cyrillic with Regular faces while CairoSVG renders Medium faces (weight=100 → Medium), so rendered ink overran the space. Fix at source: `svglib.py` `_PATH` entries for `("serif",False,"noto"/"noto_i")` and `("sans",False,"sans_noto"/"sans_noto_i")` now point at NotoSerif-Medium/MediumItalic and NotoSans-Medium/MediumItalic.
- svglib.py md5 verified BEFORE the rebuild: `781059e6784b789c1179446e15b8f6ad` ✓.

## §0 BEFORE state

| file | SHA-256 | bytes |
|---|---|---|
| `2026-w47-ru-nl.text.md` | `849015f1e920f15c8a0040157a477aab5efb75200f27ef8bcac43160e544e9b0` | 64,013 |
| `Lucerna-VOL4-ru-nl.pdf` (print) | `5843ae6b80ac7e38298ec33d565b19e49d73dc165e6d18ffeec5bdddd4982fa2` | 21,291,643 |
| `Lucerna-VOL4-ru-nl-web.pdf` (web) | `f317713abb247128035ec1a2643213301face29828782320fb4b6dc2de74ce05` | 3,387,356 |

## §1 Rebuild

- `tools/run_build.py --build production/2026-w47/2026-w47-ru-nl --out <scratch>/build --steps run,render`: rc=0. run.py TOTAL 150; render.py exit 0.
- Promoted from the scratch build copy into production: `svg/*.svg` ×8 + `Lucerna-VOL4-ru-nl.pdf` only (cards NOT re-copied — footprint per brief).
- `tools/webpdf.py svg Lucerna-VOL4-ru-nl-web.pdf`: rc=0, 3,385,859 B, 58,009 text bytes.
- `text.md` SHA after: `849015f1…` — UNCHANGED ✓.

## §2 AFTER state

| file | SHA-256 | bytes / mtime (UTC) |
|---|---|---|
| `2026-w47-ru-nl.text.md` | `849015f1e920f15c8a0040157a477aab5efb75200f27ef8bcac43160e544e9b0` | 64,013 (unchanged) |
| `Lucerna-VOL4-ru-nl.pdf` (print) | `6579cf5fc3ea1fb0137e48d37f4f975fe15648a14cbd86378102aa3c914ae08a` | 21,290,182, 2026-11-11 23:38:28 |
| `Lucerna-VOL4-ru-nl-web.pdf` (web) | `db2f1c4d6bf1fc28e801856718680f571366249873e6cd1fa70e11bbb7be3575` | 3,385,859, 2026-11-11 23:40:24 |

Final on-disk web SHA re-verified at end of work: still `db2f1c4d…`.

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
| print/web text layers | multiset identical overall + per page 8/8 (31,087 non-ws chars each; byte-identical) |

## §4 Census (word joins; `census.py` token-split + char-gap method)

- BEFORE: 136 join candidates in print, 136 in web.
- AFTER: 13 naive candidates in print, 13 in web — ALL cleared as false positives:
  - 2× `A2→B1` / `A2→B2` (P1 kicker): level-range arrows.
  - 4× date options `19ноября` (P2), `20ноября` (P4), `16ноября` (P5), `13ноября` (P8): trailing-space spans whose layout gap is real and visibly spaced (same mechanism as ru-it, verified there with 300 dpi crops).
  - 6× `Antwoorden` (P1–P6): the genuine Dutch word for "answers" (answer-key header, SVG-only, 0× in text.md — absent from the census known-word set); the Antwoord+en split is coincidental.
  - 1× `novemberweer` (P2): a genuine Dutch compound, "November weather" (SVG-only gloss word, 0× in text.md).
- **Real joins: 0 in print, 0 in web.**
- Second-defect-class check (P8 Latin-run trailing-space overrun, per the it-ru probe heads-up): NO P8 Latin→Cyrillic joins present — the only P8 candidate is the `13 ноября` date option. This edition is NOT blocked by the second fix.
- Byline `От редакции Lucerna`: real space char, gap 2.89 pt on P1–P3/P5/P6, 2.82 pt on P4 (`От спортивной редакции Lucerna`), vs 1.10 pt with no space char before. `Профессиональные праздники` spaced.

## §5 KIT updated

- §5: print SHA/bytes, web SHA/bytes, pdftotext bytes 57,822 → 58,009, char count 31,014 → 31,087.
- §7: Fix 2 record appended; §7 print/web text-layer line updated to 31,087. No other KIT content altered.

## §6 Production integrity

- Pre/post snapshot diff: exactly 11 files changed — `svg/*.svg` ×8, print PDF, web PDF, `WEEKLY-KIT.md`. No other edition touched.
- No commit / push / lint. Core-ru untouched.
