# PROOF-NOTE — Lucerna Weekly 2026-W47 en-es · proof1 (independent)

- Edition: `production/2026-w47/2026-w47-en-es/` (VOL.4, issue week Mon 2026-11-16–Sun 2026-11-22)
- Proofreader: proof1 (independent; not the builder). No source file was modified, rebuilt, committed or pushed.
- Objects verified (full SHA-256, prefixes match task): print `The-Lucerna-VOL4-en-es.pdf` 29,330,745 B `e668bc5f40f8c6e3ddc7a1d705cc39bcd004a615a2d9f2f62a0cad68304bc719`; web `The-Lucerna-VOL4-en-es.web.pdf` 2,377,727 B `a0a2f9d6d3035e4df1e05f5cf8c73c3a7fea1e35f1440b4b18e52ca85e68bcd8`; `2026-w47-en-es.text.md` 53,837 B `850fee7a0f45942896d5f2fbe91a58f4878626d2b2636266c2a7faa0288ab9db`. Both PDFs 8 pages.

## Conclusion: (b) — defects found, listed below

Three defects. One is a wrong answer key (high), two are box-title ink overflows (one core-level, one es-only). None is a build failure; all other gates pass.

## Defect D1 — HIGH, core-level: P3 matching keys Q39/Q40 swapped

- Location: P3 exercise C (matching 38–41), `registry.json` n=39/40, text.md answer lines, and the printed ANSWERS block on P8 (both print and web PDFs).
- Printed definitions (verified in both en-es and core-en P3 SVGs, same letter order):
  - a = "a person who teaches and guides you" (= a mentor)
  - b = "a person chosen to take part in the Games" (= a tribute)
  - c = "a person who lives with you in the jungle camp" (= a campmate)
  - d = "the place where the Games are fought" (= the arena)
- Keys as printed: 38 → b ✓, **39 → d (WRONG, correct is a)**, **40 → a (WRONG, correct is d)**, 41 → c ✓.
- Root is in core-en: `content34.py` line 61 has keys `["b", "d", "a", "c"]`, identical in core-en and en-es; core-en registry has the identical wrong keys (39=d, 40=a) and identical P3 SVG layout. Frozen-core defect — affects the core and all en fan-outs. Fix belongs to the coordinator/core, never to this edition.
- Secondary inconsistency inside the same defect: registry Q40 note says "arena = el estadio a" while the printed P3 gloss says "the arena = la arena" (estadio = stadium; la arena is correct). The note is wrong as well.
- All other 148 keys verified semantically correct against their stems (incl. P6 chart arithmetic 254+162+19=435, P8 cloze 112–119, dialogue 145–149, translations 137–140, and the other matching sets P2 D 24–27, P4 C 56–59, P5 C 74–77, P8 F 141–144).

## Defect D2 — MEDIUM, core-level: P2 box title overflows its cream box

- Location: P2, "THE SENATE, IN NUMBERS　El Senado" (Noto Sans CJK SC 700, 23pt), cream box x=538.5–961.0, title baseline y=562.84.
- Measurement (edition's own `svglib.text_w`): title starts x=556.5, advance width 429.5 → ends 986.0, **25.0 px past the box right edge (961.0)**. Visually confirmed on the print card: "Senado" runs off the cream onto the white page background.
- Root is in core-en: core title "THE SENATE, IN NUMBERS　参议院数字" ends 989.1 → **28.1 px past the same box edge**, visually confirmed on the core card (last Chinese character half outside the cream). Frozen-core defect — every fan-out inherits the too-long English head; the gloss width only modulates the amount.
- Note: the box is at capacity by design — core P1 title fits by only 1.5 px and core P4 by only 0.7 px (advance), so any wider gloss in a fan-out risks the same overflow class.

## Defect D3 — LOW–MEDIUM, es-only: P6 box title overflows its cream box

- Location: P6, "HOW LONG?　Duración del mandato" (Noto Sans CJK SC 700, 23pt), cream box x=1439.5–1862.0, title baseline y=703.
- Measurement (`text_w`): title starts x=1457.5, advance width 410.2 → ends 1867.7, **5.7 px past the box right edge (1862.0)**. Pixel check on the print card: green ink reaches x=1867; the final "o" of "mandato" straddles the cream edge. Small but visible.
- Es-only: core-en title "HOW LONG?　任期多长？" ends 1732.5, fitting by 129.5 px. The Spanish gloss ("Duración del mandato") is what overflows. Fixable in the es layer alone (shorten the Spanish head); no core touch needed.

## Observations (non-blocking, no action required from proof1)

- O1 — P5 bridge line "Cada niño tiene derechos | Every child has rights = Cada niño tiene derechos." reads redundantly (Spanish twice). Same construction is frozen in core ("每个孩子都有权利｜Every child has rights = 每个孩子都有权利。") — core pattern, cosmetic, not an es defect.
- O2 — P7 NEXT WEEK teaser "The Ashes, second week in Perth": loose wording (the Perth Test ends Nov 25, inside VOL.5's week; the 2nd Test is Brisbane, Dec 4). Core text, frozen; not treated as a factual defect.
- O3 — Three minor claims could not be source-verified (not asserted false, just unverified): P4 "Day one is already sold out"; Ashes first ball "10:20 a.m. local — 2:20 a.m. in London" (the Perth UTC+8 → London GMT arithmetic is consistent; the start time itself was not source-checked); ATP singles final "not before 6 p.m. local time". Every other external fact was verified against live sources (see GATE-LOG.md).
- O4 — Template flow, same as core: section heads occasionally sit at the bottom of one column with their items at the top of the next (e.g. P4 "B SENTENCES", P5 "D PRESENT CONTINUOUS"). Not a defect.
- O5 — The P2 "SAY IT" phrase boxes and the P7 toolbox were the creambox-sensitive areas: visually confirmed clean (toolbox clearance +48.5 px; "¡Feliz Día de Acción de Gracias!" fits inside its box).

## What passed (summary; numbers in GATE-LOG.md)

- Full text.md read; 150/150 answer lines match registry; 149/150 semantically correct (D1 is the exception).
- occlusion audit 0 flags (selftest OK) — but note its BOXTITLE class only covers bordered (stroke / #2c2822) boxes, NOT cream boxes; D2/D3 were caught by the explicit `text_w` boxtitle measurement + visual crops, not by the audit.
- p8 extract 150/150; p8 compare CLEAN (keydiff [137–140, 150] = translations + open task, expected).
- freeze 8/8 SVGs byte-identical; freeze diff vs core: no English article text changed; added CJK 9 chars, all U+3000.
- creambox refined check: NO OVERFLOW, 32 cream boxes, inside clearance +5.0 to +92.4 px.
- boxtitle widths measured for all 17 cream-box titles: 15 fit (tightest fits P4 +7.5, P1 +20.4); D2 −25.0, D3 −5.7.
- P8 minimum font 13.5 pt (≥ SOP §1.1 floor 9.75 pt); other pages 15.5 pt.
- Print vs web PDF text layers identical (token-multiset diff 0/0).
- All 8 print cards + web P1/P8 viewed: no other overflow, overlap, or footer intrusion; images/captions correct; masthead, footers, page numbers correct.
- Curly quotes balanced (text.md 81/81; SVG 82/82); straight apostrophe is the frozen core convention (43 es vs 45 core; curly ’ = 0 both). Banned/internal strings 0 in visible SVG text. VOL.4 ×12; VOL.5 ×8 (teasers); VOL.3 ×3 (legitimate). Real CJK in visible es text 0.
- All dates/weekdays in the paper correct (checked against `date`, America/Toronto).
- P7 golden sentences: all 8 verbatim in the issue body with correct page attributions. Model text "My Monday, November 16" = 82 words (matches KIT).
