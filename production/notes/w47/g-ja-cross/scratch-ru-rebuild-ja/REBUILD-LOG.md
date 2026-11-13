# REBUILD LOG — 2026-w47-ru-ja (wave B, ru word-spacing rebuild)

- Edition: `production/2026-w47/2026-w47-ru-ja/` (Russian target × Japanese reader, VOL.4)
- Date: 2026-11-11 23:43–23:56 UTC. No commit, no push, no lint.
- Scratch: `hidden_files/w47/scratch-ru-rebuild-ja/` (this log, `census.py`, `run_build.log`, `webpdf.log`, `gates/`, `census-*.txt/.json`, `textlayer.log`, `pre-snapshot.txt`). Build copy under `build/`.
- Root cause (per brief): PIL measured Cyrillic with Regular faces while CairoSVG renders Medium faces (weight=100 → Medium), so rendered ink overran the space. Fix at source: `svglib.py` `_PATH` entries for `("serif",False,"noto"/"noto_i")` and `("sans",False,"sans_noto"/"sans_noto_i")` now point at NotoSerif-Medium/MediumItalic and NotoSans-Medium/MediumItalic.
- svglib.py md5 verified BEFORE the rebuild: `781059e6784b789c1179446e15b8f6ad` ✓.

## §0 BEFORE state

| file | SHA-256 | bytes |
|---|---|---|
| `2026-w47-ru-ja.text.md` | `07824474bb88439bea67fb4d1dc3ede956f33b006a32e8203e5b52081c1090da` | 64,477 |
| `Lucerna-VOL4-ru-ja.pdf` (print) | `150f970828142d50cc10ba157182dd282c22dd74d82de5f7c932141d86cda0a3` | 27,409,704 |
| `Lucerna-VOL4-ru-ja-web.pdf` (web) | `ea1a9d7381f02e18ab24c3d20c36efec1b9b58cf3494b3e2478a27a1851a6743` | 3,721,620 |

## §1 Rebuild

- `tools/run_build.py --build production/2026-w47/2026-w47-ru-ja --out <scratch>/build --steps run,render`: rc=0. run.py TOTAL 150; render.py exit 0.
- Promoted from the scratch build copy into production: `svg/*.svg` ×8 + `Lucerna-VOL4-ru-ja.pdf` only (cards NOT re-copied — footprint per brief).
- `tools/webpdf.py svg Lucerna-VOL4-ru-ja-web.pdf`: rc=0, 3,720,196 B, 58,610 text bytes.
- `text.md` SHA after: `07824474…` — UNCHANGED ✓.

## §2 AFTER state

| file | SHA-256 | bytes / mtime (UTC) |
|---|---|---|
| `2026-w47-ru-ja.text.md` | `07824474bb88439bea67fb4d1dc3ede956f33b006a32e8203e5b52081c1090da` | 64,477 (unchanged) |
| `Lucerna-VOL4-ru-ja.pdf` (print) | `d681cf9788392b44b271fbe76e0ef48fbe7913563c94c1e2335a04b7b9f26a61` | 27,408,235, 2026-11-11 23:46:14 |
| `Lucerna-VOL4-ru-ja-web.pdf` (web) | `8b7b38d48753247dc90ed8913120dfcbee7c3d9e0b07fcebce72c5ce49fb2254` | 3,720,196, 2026-11-11 23:48:09 |

Final on-disk web SHA re-verified at end of work: still `8b7b38d4…`.

## §3 Gates (all green)

| gate | result |
|---|---|
| run.py | exit 0, TOTAL 150 |
| render.py | exit 0 |
| p8.py extract | 150/150 |
| p8.py compare vs core-ru | CLEAN, keydiff [137, 138, 139, 140] |
| check_core.py | exit 0; golden BAD 0, gloss fails 0; orphan 4 (P7 y553 `”».` + P7 y784 `：`/`。` + P7 y968 `。` — exactly the 4 inline-punctuation false positives the KIT already records); same-baseline collisions 0 |
| occlusion_audit.py | 0 flags (selftest OK; was 42 TEXTX before) |
| freeze baseline | 8/8, run twice (8/8 both — reproducibility verified) |
| freeze diff vs core-ru | informational only (added Latin strings 22 — Japanese edition, no CJK added) |
| print/web text layers | multiset identical overall + per page 8/8 (26,630 non-ws chars each; byte-identical) |

## §4 Census (word joins; `census.py` token-split + char-gap method)

- BEFORE: 123 join candidates in print, 123 in web.
- AFTER: 8 naive candidates in print, 8 in web — ALL cleared as false positives:
  - 2× `A2→B1` / `A2→B2` (P1 kicker): level-range arrows.
  - 4× date options `19ноября` (P2), `20ноября` (P4), `16ноября` (P5), `13ноября` (P8): trailing-space spans whose layout gap is real and visibly spaced (same mechanism as ru-it, verified there with 300 dpi crops).
  - 1× P7 `21の後はгол` (error-clinic gloss `«забили 21 гол»`): Japanese note + Russian quote; junction char-bbox gap 3.26 pt (wider than a normal space); 300 dpi crop viewed — clearly spaced (`21の後は гол： забили 21 гол。`).
  - 1× P8 `土曜の注目カード：クラスノダール4:2` (answer 48 B): Japanese note + score; junction char-bbox gap 1.20 pt; 300 dpi crop viewed — daylight between `ル` and `4`. Normal Japanese mixed-text CJK↔digit setting with no space char by design — the same class the round-2 proof note explicitly excluded as not a defect — and the token is unchanged vs the BEFORE build.
- **Real joins: 0 in print, 0 in web.**
- Proof-note checklist: all ~90 round-2 sites gone (byline `От редакцииLucerna`, `Главныетемынеделив`, `Профессиональныепраздники`, `КонстантинЮон`, `Промокоддействует`, P8 `заказываетподарок` / `поздравляетдруга-студента` / `начинается16` — none remains a candidate).
- Second-defect-class check (P8 Latin-run trailing-space overrun, per the it-ru probe heads-up): NO P8 Latin→Cyrillic joins present — the only P8 candidates are the `13 ноября` date option and the Japanese-note score above, neither a Latin run. This edition is NOT blocked by the second fix.
- Byline `От редакции Lucerna`: real space char, gap 2.89 pt on P1–P3/P5/P6, 2.82 pt on P4 (`От спортивной редакции Lucerna`), vs 1.10 pt with no space char before. `Профессиональные праздники` spaced.

## §5 KIT updated

- §5: print SHA/bytes, web SHA/bytes, pdftotext bytes 58,411 → 58,610, char count 26,540 → 26,630.
- §7: Fix 2 record appended; §7 print/web text-layer line updated to 26,630. No other KIT content altered.

## §6 Production integrity

- Pre/post snapshot diff: exactly 11 files changed — `svg/*.svg` ×8, print PDF, web PDF, `WEEKLY-KIT.md`. No other edition touched by this worker (other-edition files changing during this window are parallel workers' — e.g. the it-ru probe — with mtimes outside this rebuild's file set; this worker's writes went only to its 4 edition dirs and its 4 scratch dirs).
- No commit / push / lint. Core-ru untouched.
