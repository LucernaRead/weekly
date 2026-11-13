# REBUILD-LOG — W47 2026-w47-ru-es (wave A, spacing rebuild)

Date: 2026-11-11/12. **NOT REBUILT — STOPPED per the wave-A precondition.**

## Why it stopped

The wave-A brief requires md5 of `svglib.py` = `781059e6784b789c1179446e15b8f6ad`
(the Medium / first fix) in each edition before rebuilding; if any
differs, STOP and report — do not rebuild that edition.

When ru-es's turn came (2026-11-12 ~00:20 UTC), its production
`svglib.py` was md5 `ee3211298f274e02ade2d4ca318ce354` — the SECOND spacing
fix ("unkerned run measurement" in `Page.text`, landed by the dedicated
fix worker during this wave). Rebuilding ru-es now would use the second
fix, which is wave B's work, not wave A's. So ru-es was NOT rebuilt:
no SVG, card, PDF or KIT file was touched.

## State (verified, untouched)

- text.md `332c8e4f5478181d21281fe059483f0da4ee2bf5e39fec4464f836049e2bad60`,
  64,176 B (unchanged from the recorded before state)
- print `64cb48f90dea70553a76e70c8cb9bc75ffa571c1ceaa8318c8655b47b80cf7c3`,
  21,278,615 B (unchanged)
- web `526873a863981b82d6d56892508ef635204baf1569746ba4b2d0b70cd96c8123`,
  3,387,494 B (unchanged)
- svglib.py md5 `ee3211298f274e02ade2d4ca318ce354` (second fix),
  SHA-256 `323b4079d91b5cae4eb0a3a7336bf645178c5eb73ab761410630d580e3473c50`

## BEFORE census (fixed census — for the wave-B baseline)

Re-run with the fixed `census.py` (see ru-de log §6 for the blind-spot
fix) on the still-unrebuilt PDFs: **170 tokens / 212 boundaries**
(print = web) — the same count as ru-fr before (170/212).

## Date cases — CONFIRMED JOINS (measured 2026-11-12, unrebuilt PDFs)

The second-fix worker's ruling (2026-11-11, `scratch-it-ru-spacing2/`)
confirms the date cases as joins (narrow vs the ~3.46 pt body median),
not clearable on crop evidence alone. Measured here in the ru-es
BEFORE files — same lines, same gaps as the rebuilt siblings:

| token | page | visual gap (pt) | space char in text layer? | line normal | line |
|---|---|---|---|---|---|
| `19 ноября` | P2 | **2.19** | yes | 3.16 | "День психолога— это... A. 19 ноября · B. 21" |
| `16 ноября` | P5 | **2.32** | yes | 3.68 | "2026 году — это... A. 16 ноября · B. 27" |
| `20ноября` | P4 | **2.18** | no (fused token) | 3.55 | "15-й тур начнётся... A. 20ноября · B. 8" |
| `13ноября` | P8 | **1.50** | no (fused token) | 1.95* | "Когда«чёрная пятница» на Ozon? A. 13ноября – 2 декабря ·" |

\* P8 line's own space-char width is 1.95 pt, but the ruling's P8 median
is 2.36 pt and the body median 3.46 pt — 1.50 is narrow against both.
The `13ноября` line is one shared core line in all 10 ru-* editions
(1.43 pt in rebuilt de/en/fr, 1.50 pt here — the ruling's 1.43–1.50 range).
`19`/`16` carry a space char in the old text layer but the ink gap is
already ~2.2 pt — the Medium rebuild in de/en/fr only exposed them in
the text layer (2.11/2.24 pt there); the ink never changed. This edition
was NOT synced carrying these joins, per the ruling.

Other date-adjacent checks: `A.на` P4 fused, gap 1.67 pt (de/en/fr
1.68); `A.биография` not a standalone token before — hidden inside the
larger fused token `биографияbiopic` (gap 1.51; the Medium rebuild in
fr exposed it as `A.биография` 2.20). `ГЛАГОЛЫИ` is not flagged in any
ru census (before or after) — nothing to correct against the ruling
(2.62 pt, bold-caps bbox artifact, not a join). Arrow tokens
(`→` + Cyrillic) in the rebuilt siblings measure 2.32–2.41 pt, at the
normal median — already adjudicated as extraction-only false positives,
consistent with the ruling.

Checklist from the ru-es proof note (17 instances, in
`hidden_files/w47/scratch-reproof-ru-es1/PROOF-NOTE.md`): P1
`метеорологическаязима`; P2 `рожденияДеда`, `Профессиональныепраздники`,
`поздравитьfelicitar`; P3 `криминальнаяpolicíaca`, `экранизацияadaptación`;
P4 `результатов+`; P5 `календарнаядата`, `маркетплейсахскидки`,
`начинаютсяуже`; P6 `упражнений—`; P7 `Кипренский—`; P8
`заказываетподарок` (Q135 + A135), `negativo:не` (A82), `возвращаютпокупки`
(A100), `Atención:играть` (A139). By analogy with de/en/fr, the expected
wave-B residuals are the second-defect joins: P8 `negativo:не` and
`Atención:играть`, the dates `13/19/20/16ноября`, `A.` letter joins,
`;` junctions, and the punct junctions `результатов+`, `упражнений—`,
`Кипренский—` (the last three are leading/trailing-punct junctions the
fixed census now catches).

## What wave B needs

Rebuild ru-es (and re-rebuild ru-de, ru-en, ru-fr) with the current
second-fix svglib.py (md5 `ee321129…`). The ru-de/ru-en/ru-fr production
files on disk were all built with the first fix and are now stale
relative to the current source. KIT §5/§7 for ru-es is untouched and
still carries the pre-rebuild SHAs.
