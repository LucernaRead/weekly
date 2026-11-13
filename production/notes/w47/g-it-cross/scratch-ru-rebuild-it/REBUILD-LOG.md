# REBUILD LOG — 2026-w47-ru-it (wave B, ru word-spacing rebuild)

- Edition: `production/2026-w47/2026-w47-ru-it/` (Russian target × Italian reader, VOL.4)
- Date: 2026-11-11 23:17–23:30 UTC. No commit, no push, no lint.
- Scratch: `hidden_files/w47/scratch-ru-rebuild-it/` (this log, `census.py`, `run_build.log`, `webpdf.log`, `gates/`, `census-*.txt/.json`, `textlayer.log`, `pre-snapshot.txt`). Build copy under `build/` (kept for audit; production was never built in place).
- Root cause (per brief): PIL measured Cyrillic with Regular faces while CairoSVG renders Medium faces (weight=100 → Medium), so rendered ink overran the space. Fix at source: `svglib.py` `_PATH` entries for `("serif",False,"noto"/"noto_i")` and `("sans",False,"sans_noto"/"sans_noto_i")` now point at NotoSerif-Medium/MediumItalic and NotoSans-Medium/MediumItalic.
- svglib.py md5 verified BEFORE the rebuild: `781059e6784b789c1179446e15b8f6ad` ✓ (expected value).

## §0 BEFORE state (23:17 UTC)

| file | SHA-256 | bytes |
|---|---|---|
| `2026-w47-ru-it.text.md` | `0bb5739a9e2a1215074b8d5cba566736e88cd84d45f3bc28eb0fe5a8966f5989` | 63,972 |
| `Lucerna-VOL4-ru-it.pdf` (print) | `c69b7bdf3165ed24f05be8004559e0102c0c8e38f15e395bc32360094628359b` | 21,265,865 |
| `Lucerna-VOL4-ru-it-web.pdf` (web) | `b994d11ff9c219c7900b53b2eca377a345e49a45f97e9ea691fc51712bd1ac14` | 3,384,121 |

## §1 Rebuild

- `tools/run_build.py --build production/2026-w47/2026-w47-ru-it --out <scratch>/build --steps run,render`: rc=0. run.py TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE (per run-build log); render.py exit 0.
- Promoted from the scratch build copy into production: `svg/*.svg` ×8 + `Lucerna-VOL4-ru-it.pdf` only (cards NOT re-copied — footprint per brief: svg + print + web + KIT).
- `tools/webpdf.py svg Lucerna-VOL4-ru-it-web.pdf`: rc=0, 3,382,725 B, 57,843 text bytes.
- `text.md` SHA after: `0bb5739a…` — UNCHANGED ✓ (also byte-identical in the build copy before promotion).

## §2 AFTER state

| file | SHA-256 | bytes / mtime (UTC) |
|---|---|---|
| `2026-w47-ru-it.text.md` | `0bb5739a9e2a1215074b8d5cba566736e88cd84d45f3bc28eb0fe5a8966f5989` | 63,972 (unchanged) |
| `Lucerna-VOL4-ru-it.pdf` (print) | `6f123397a03f32610a14c1ea23f23a80ba442c6b976fa08f9f52275822561331` | 21,264,469, 2026-11-11 23:22:32 |
| `Lucerna-VOL4-ru-it-web.pdf` (web) | `37a31f2d6ef22f4300fd01275b778612929d3e5b95eac8dacd1cd20a571ac396` | 3,382,725, 2026-11-11 23:23:09 |

Final on-disk web SHA re-verified at end of work: still `37a31f2d…` (the file built here; no concurrent rewrite observed).

## §3 Gates (all green)

| gate | result |
|---|---|
| run.py | exit 0, TOTAL 150 |
| render.py | exit 0 |
| p8.py extract | 150/150 |
| p8.py compare vs core-ru | CLEAN, keydiff [137, 138, 139, 140] |
| check_core.py | exit 0; golden BAD 0, gloss fails 0; orphan 1 (P7 y553 `”».`, same benign class as KIT); same-baseline collisions 0 (the P1 y1712 italic collision from the re-fanout record is gone with the wider spacing) |
| occlusion_audit.py | 0 flags (selftest OK; was 42 TEXTX before — the Regular-vs-Medium false-positive class vanished) |
| freeze baseline | 8/8, run twice (freeze1 + freeze2, both 8/8 — reproducibility verified); core integrity: shipped core SVGs unchanged |
| freeze diff vs core-ru | informational only (translation adds Latin wholesale; --strict-latin not applicable core-vs-edition) |
| print/web text layers | multiset identical overall + per page 8/8 (30,923 non-ws chars each; pdftotext-equivalent byte-identical) |

## §4 Census (word joins; `census.py` token-split + char-gap method)

- BEFORE: 138 join candidates in print, 138 in web.
- AFTER: 14 naive candidates in print, 14 in web — ALL cleared as false positives:
  - 8× `SETTIMANALE` (footer, every page): a single Italian word that splits as SETTIMANA+LE. Not a join.
  - 2× `A2→B1` / `A2→B2` (P1 kicker): level-range arrows. Not a join.
  - 4× date options `19ноября` (P2), `20ноября` (P4), `16ноября` (P5), `13ноября` (P8): the option strings are spans like `... A. 19 ` + `ноября` (trailing space inside the number span). The space char is dropped from the PDF text layer by CairoSVG, so PyMuPDF merges the token — but the layout gap is real and visibly spaced: 300 dpi crops viewed for P2 (`A. 19 ноября`) and P8 (`A. 13 ноября`); char-bbox gaps 2.11 / 2.18 / 2.24 / 1.43 pt. Words do not run together.
- **Real joins: 0 in print, 0 in web.**
- Proof-note checklist: all 6 round-2 findings gone (P1 `Главные темы` / `российских СМИ`, P1 `метеорологическая зима`, P4 `результатов +`, P4 `достояние (`, P8 keys 92/139); `Профессиональные праздники` spaced (no longer a candidate).
- Byline `От редакции Lucerna`: now a real space char on P1–P3/P5/P6, gap 2.89 pt; P4 `От спортивной редакции Lucerna` 2.82 pt. Before: no space char, 1.10 pt (matches the ru-de probe's 1.10→2.89 pt exactly).
- Census caveat: the script's `max_internal_gap` returns 0.0 when its char filter finds no chars (multi-baseline tokens) — the 0.0 values in the AFTER list are unmeasured, not zero gaps; the date tokens were re-measured precisely (junction char-pair gaps above) and visually confirmed.

## §5 KIT updated

- §5: print SHA/bytes, web SHA/bytes, pdftotext bytes 57,648 → 57,843, char count 30,862 → 30,923.
- §7: Fix 2 record appended (this rebuild). No other KIT content altered.

## §6 Production integrity

- Pre/post snapshot diff of the edition dir: exactly 11 files changed — `svg/*.svg` ×8, print PDF, web PDF, `WEEKLY-KIT.md`. No other edition touched; no other file in this edition changed.
- No commit / push / lint. Core-ru untouched (freeze core-integrity check: 8 shipped core SVGs unchanged).
