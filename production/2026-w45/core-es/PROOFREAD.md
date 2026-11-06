# W45 ES core — self-proofread record (builder)

Date: 2026-10-26. Method: full text extraction of all 8 SVGs (P1–P8) read end to end + visual review of all 8 rendered PNGs at 1950×2700 + programmatic checks (golden-sentence counts, P8 answer numbering, model word count).

## Defects found and fixed (all re-rendered and re-verified)

1. P8 ex 131 answer key wrong: was C (Ana watches NFL + Atlético–Barça); the P8-C text says Ana watches only the NFL in the afternoon while Pablo watches Atlético–Barça at night. Fixed key to A; note now reads «Ana 只看 NFL；晚上看马竞–巴萨的是 Pablo».
2. P5 plan item 5 fact error: said the campaign was already underway on Mon Nov 9; the campaign starts Fri Nov 13. Fixed to «vuelta a clase y al trabajo; la campaña empieza el viernes 13».
3. P6 overstatement: «Es la primera vez que un tema sube tanto en un solo mes» exceeded the Reuters wording (record level, not record jump). Fixed to «Es una cifra récord, veinte puntos más que en septiembre».
4. Orphan closing paren «）» on its own line: P1 CIFRAS item 3 and P5 plan item 5. Fixed by shortening both Chinese glosses.
5. Earlier build fixes (pre-proofread): P1 headline FLOW OVERFLOW, P7 B1/B2 head too wide, P7 col3 over FRASES rule, 11 occlusion flags (all real, all fixed — see occlusion.json → occlusion2.json).

## Programmatic checks (final state)

- Golden sentences: 8/8 appear exactly 2× across all SVGs.
- P8 answers: 150, continuous 1–150, no gaps/dupes.
- Model text (P8-H): 84 words, inside the stated 80–100 range, printed on the page.
- Build warnings: FLOW OVERFLOW 0, HEAD TOO WIDE 0.
- Occlusion audit final run (occlusion4.json): 0 flags, selftest OK.
- Furniture-band same-baseline ink-spacing scan: visual check of all 8 PNGs — no same-line collisions (P1 top band, masthead band, inner-page bands, footer bands).

## Remaining verification debt (recorded in KIT §6.1, not a defect in the pages)

- Nov 12 Diputación Permanente vote on the housing decrees: sourced only from the trend pool's Hipotecas.me calendar citation; an independent search returned no confirmation. Kept in P6 timeline + P7 preview with the debt recorded; VOL.3 must re-verify and correct if false.
