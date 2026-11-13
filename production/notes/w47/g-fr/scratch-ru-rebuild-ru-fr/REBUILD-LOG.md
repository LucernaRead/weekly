# REBUILD-LOG — W47 2026-w47-ru-fr (wave A, spacing rebuild)

Date: 2026-11-11 23:52–00:15 UTC. Fix: svglib Medium (first fix), md5
`781059e6784b789c1179446e15b8f6ad` (verified in the build-copy; see note
below — the second fix has since landed in production svglib.py).

## Verdict: DONE, BLOCKED BY SECOND FIX

All 131→14 joins cleared except the 14 real joins of the second defect
class (Latin/symbol run + trailing space + Cyrillic). All KIT §5 gates
green. Needs a wave-B rebuild with the second-fix svglib (see below).

## BEFORE (recorded 2026-11-11)

- text.md `e4cc50fd4195ed1adb7051c684c894c5a3b3091aa643cf3bab96690178e22a46`, 63,361 B
- print `cdde6a829ba09283d7f815c960570cd1aec0771a41b3f03bead08cb47d530f79`, 21,291,969 B
- web `7a3af1e2de8b57517e9c2e7b4933e35495107f5e2c4a9b72dfcefdb5fc0e79c5`, 3,385,807 B
- Census (fixed census, old web PDF as before proxy): 170 tokens / 212 boundaries.

## BUILD

- `tools/run_build.py --build production/2026-w47/2026-w47-ru-fr --out
  scratch-ru-rebuild-ru-fr/build --steps run,render`
  (background session proc_a71532fbd0ab; the session's exit 1 is the
  trailing `grep -c` finding 0 overflow matches — the build itself:
  run.py exit 0, TOTAL 150, render.py exit 0, integrity clean, 0 overflow).
- Synced svg/*.svg + cards/*.png + print PDF into production; web PDF
  built with `tools/webpdf.py svg Lucerna-VOL4-ru-fr-web.pdf` (58,036 text bytes).
- text.md SHA UNCHANGED.

## AFTER

- print `32f2e1688c71212688aa47239530508fac1177d3b7dab278b7814763468a439f`,
  21,290,501 B, mtime 2026-11-11 23:58:01 UTC
- web `2eb8062cbb0cd2ed714ed680f9c59b381d0389ccb07e38bd0c73a31a32c06139`,
  3,384,329 B, mtime 2026-11-11 23:59:04 UTC
  (re-verified after all gates — still the file built here)
- Footprint: 19 files changed vs before (8 svg + 8 cards + print + web +
  svglib.py by the second-fix worker, see below). text.md unchanged.

## GATES

- run.py exit 0 / TOTAL 150 / zero overflow; render.py exit 0.
- p8 extract 150/150 (core + edition); compare vs core-ru CLEAN,
  keydiff [137, 138, 139, 140] (direct JSON keydiff identical); key 20 = желании.
- check_core.py rc 0, golden BAD 0, gloss fails 0, orphan P7 y579 `”».`
  (benign, same class as core), same-baseline collisions 0.
- occlusion_audit.py 0 flags (selftest OK).
- Freeze: baseline tool self-reports 0/8 — explained: production SVGs
  were built with first-fix svglib (md5 781059e6); the re-run used the
  second-fix svglib that landed mid-wave. Two independent baseline
  re-runs are byte-identical to each other (8/8); structured comparison
  vs production: identical element counts/strings/y, only run-boundary x
  shifted (per-line random walk, up to ~7 units) = the unkerned-measurement
  change. Build is deterministic given one svglib.
- Print/web text layers byte-identical per page (fitz non-whitespace
  30,770 chars each; raw 37,488 each).
- Byline "От редакции Lucerna": space char present P1–P6, ink gap 2.89 pt
  (P4 "От спортивной редакции Lucerna" 2.82 pt). "Профессиональные
  праздники" spaced P2/P6.

## CENSUS (fixed census.py — see "Census blind spot" below)

After: **28 tokens / 31 boundaries** (print = web), before 170 / 212.

REAL remaining joins (14 tokens / 14 boundaries) — second defect class:
| token | page | gap (pt) | note |
|---|---|---|---|
| `:пять` | P8 | −0.22 | glyphs overlap |
| `:играть` | P8 | −0.52 | glyphs overlap (key 139 "Attention :играть") |
| `—скидка` | P8 | 1.44 | unchanged before→after |
| `—поздравляю` | P8 | 1.33 | key 140, unchanged before→after |
| `результатов+` | P4 | 1.96 | was −0.14 (overlap) before; improved, still ~2.3 pt short of ~4.3 normal |
| `13ноября` | P8 | 1.43 | |
| `19ноября` | P2 | 2.11 | line "День психолога — это... A. 19ноября · B. 21" |
| `20ноября` | P4 | 2.18 | line "15-й тур начнётся... A. 20ноября · B. 8" |
| `16ноября` | P5 | 2.24 | line "2026 году — это... A. 16ноября · B. 27" |
| `A.на` | P4 | 1.68 | line "«Ростов» сравнял счёт с «Зенитом»... A.на" |
| `A.биография` | P3 | 2.20 | normal 3.62–3.71 |
| `A.снег` | P7 | 2.28 | normal ~3.7 |
| `A.цена` | P7 | 2.29 | normal ~3.7 |
| `A.точно` | P7 | 2.29 | normal ~3.7 |

Date/letter gaps identical in de/en/fr (same Russian body lines).
The date/letter joins are newly visible in the *text layer* only — ink
gaps identical before/after (old PDF carried a space char there, new one
does not; not a visual regression). No P8 colon joins of the
de/en form: fr key 82 "Impératif négatif : не спешите" is SPACED
(the French " :" + space survives); key 139 is the `:играть` join above.

Cleared as false positives (14 tokens / 17 boundaries): `→После` ×3,
`A2→B1` (2 bnd), `A2→B2` (0.0 pt — deliberate diagram connector),
`→Родительный`, P8 `→выходят/рассказывает/снял/сыграли/играет/победило/работаем`
(2.32–2.41 vs normal 2.15–2.38 at 9.8 pt), `✓Voir` (2.33 vs 2.37),
`Ozon:` / `Wildberries:` P5 (source L376/378 has no space before ':';
the census hit came from the key lines' French "Ozon :" form; measured
0.00 gap before ':' with a 4.0 pt space after, matching the source).

## Census blind spot (found + fixed during this wave)

The shared census (`scratch-ru-rebuild-ru-de/census.py`) stripped
leading/trailing punctuation from each word before analysis, so
leading/trailing punct junctions (`—поздравляю`, `:играть`,
`результатов+`) were invisible — the first after-census run missed them.
Fixed: analyse the RAW word and only skip outright when the raw word
IS a vocab word with no surrounding punctuation. The before/after
counts above are from the fixed census (re-run on all three completed
editions; see their updated logs). ru-de/ru-en KIT records and logs
were corrected to the fixed counts (de 27 tok/30 bnd, 15 real;
en 29/32, 17 real).

## Second fix landed mid-wave

During this wave the dedicated fix worker landed the second spacing fix
in production `svglib.py` (all 4 editions): md5
`ee3211298f274e02ade2d4ca318ce354`, SHA-256
`323b4079d91b5cae4eb0a3a7336bf645178c5eb73ab761410630d580e3473c50` —
"unkerned run measurement" in `Page.text` (sums single-char advances so
the next run's x matches what Pango renders). This edition was built
with the FIRST fix only, as briefed; a wave-B rebuild with the second-fix
svglib is needed to clear the 14 remaining joins.

## KIT

§5 SHAs/bytes + build line + web text bytes updated; §7 "Spacing
rebuild" record appended (blocked status). No commit/push/lint.

## Ruling confirmation (2026-11-12)

The it-ru ruling (`hidden_files/w47/scratch-it-ru-spacing2/REBUILD-LOG.md`)
confirms every adjudication in this log: the DATE cases (`19ноября` 2.11,
`20ноября` 2.18, `16ноября` 2.24, `13ноября` 1.43 pt) are CONFIRMED
JOINS, narrow against the ~3.46 pt body / 2.36 pt P8 medians — this
edition was correctly NOT synced carrying them. The ARROW cases
(`→` + Cyrillic, 2.32–2.41 pt, at the normal median) are NOT joins —
extraction-only signal, already cleared as false positives. `ГЛАГОЛЫИ`
(2.62 pt, bold-caps bbox artifact) is not flagged anywhere in this
edition's censuses. No numbers in this log change.
