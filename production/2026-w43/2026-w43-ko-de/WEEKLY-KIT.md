# Lucerna Korean Weekly VOL.1 — KO × DE Edition （한국어 본문 + 독일어 해설）

**Edition:** Korean text + **German** explanations, for German-speaking readers.
**Week:** Mon 2026-10-19 – Sun 2026-10-25 · VOL.1 · 8 pages · 150 exercises.
**Source:** the finalized, P2-patched Korean core (`files/weekly-report-ko-vol1/`, Korean + Chinese explanations). This edition copies that build and rewrites ONLY the explanation layer into German, following the DE-column sibling pattern (FR×DE / RU×DE / KO×EN conventions).
**Build dir:** `hidden_files/weekly-report-ko-de-build/` (the core's build dir was never edited).
**Status: BUILDER-COMPLETE — pending independent proofread. NOT posted to Discord.**

## 1. Pairing furniture (as mandated)

- Masthead: **Lucerna** (no article — Korean takes none).
- P1 pairing badge, brick red (#a4553a), 20pt bold, under the tagline:
  **„KOREANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER"** (measured 971.9px ≤ 1820, centred).
  Inserted exactly as in KO×EN: tagline 372→366, badge at y=394, rules at 412/421, black band 424→433, band texts +9.
- Footers (all 8 pages): „Lucerna · KOREANISCHE WOCHENZEITUNG VOL.1 · TEXT AUF KOREANISCH · ERKLÄRUNGEN AUF DEUTSCH" / „Seite N von 8" (footer-left measured 998.7px at 20pt, no collision with the right footer).
- Date line, edition line, Korean article text, Korean exercise stems/options: unchanged from the core.

## 2. Baseline proof (before any edit)

The unmodified copy in `hidden_files/weekly-report-ko-de-build/`, rebuilt with output redirected, reproduced **all 8 shipped core SVGs byte-identical**, and the registry dump was identical to the core's (150 entries; writing model 162 characters). Build environment: `/tmp/wp-venv` (cairosvg / Pillow / pypdf).

## 3. What changed — the explanation layer, in full German

Every Chinese apparatus string was replaced by a German one, by asserted-count patches (each replacement's occurrence count verified before writing):

- All article glosses (P1–P6 HINWEIS boxes; prefix „HINWEIS · " as in RU×DE), grammar/vocab lines on P7, the P7 pattern note and readers'-corner note, all chart/bracket glosses, all section-header German halves (bilingual heads kept: Korean + German), all exercise instructions and per-item type labels, the P2 D-Day strip glosses, the P8 section instructions, and **all 150 P8 answer notes**.
- German type labels: Ausfüllen 49 · Ankreuzen 51 · Zuordnen 16 · Lückentext 13 · Sätze bilden 8 · Umformen 4 · Richtig/Falsch 4 · Übersetzen 4 · Schreiben 1 (sums to 150; same items as the core).
- Conventions: „Suneung" for 수능 (as RU×DE uses „Suneung"); „Forstbehörde" for 산림청; „Wetterbehörde" for 기상청; German number formats kept consistent with the printed Korean facts (551,864 / 75,000 with comma thousands as printed in the paper; „1,5 Millionen" decimal comma in prose notes; „50 %" with space). Note-hygiene: half-width space before every note parenthesis, zero full-width characters in keys/notes (programmatically checked).
- Three box/section titles were shortened so the bilingual head fits its measure (house style, recorded): „숫자로 보는 이번 주 · Zahlen" (P1), „「D-데이」 사용법 · D-Day zählen" (P2), „이번 주 청년 숫자 · Zahlen" (P5). The P1 search-box source line reads „KoreaTrendBoard (10월 21일) · Zahlen gerundet" at 17pt (ends x≈1848, inside the box).
- Chinese apparatus remnants: **zero** — the rendered DE SVGs contain 0 Han-character text elements; the build code contains no Han outside frozen Korean-content strings that merely sit next to apparatus (credits/captions stay Korean, as in the core). The banned intermediary term appears nowhere (paper, this KIT, code).
- Frozen Korean-only furniture kept Korean-only exactly as the core: P3 calendar box, P4 calendar box, P6 예보 읽는 법 sidebar, P8 band sub-line.

## 4. Freeze verification

- Build-source diff vs the core is confined to the explanation layer (line counts: bslib4 6, svglib 2, content12 153, content34 144, content56 156, content7 84, content8 120, render.py 6 — same magnitudes as the KO×EN sibling diff).
- Pure-Korean lines that changed are exactly: the P1 tagline and the two black-band lines (text identical, only y shifted +9 for the badge insertion), the Korean instruction glosslines on P2–P6 (reader-language apparatus; German in this edition, per the KO×EN precedent), the P8 writing glossline, and the P8 key group-heading line (restructured by the keep-with-next block, §6). Nothing else.
- Registry diff (DE vs core, all 150): pages and levels identical for every item (A2 57 · B1 66 · B2 27; pages 10/18/18/18/18/18/12/38). **Keys differ in exactly 3 items** — the documented translation re-aims (§5). All other keys byte-identical and all 150 found verbatim in the rendered P8 (whitespace-insensitive), #150 as its ✓ apparatus line.
- Image payloads byte-identical per page (counts 1/1/2/1/2/1/0/0); credits identical (Korean).
- Facts unchanged: Typhoon Champi stays an OPEN forecast (the paper never states a decided landfall; #137's key is the German translation of the open-forecast sentence); the foliage dispute stays two-peaks/two-criteria as printed.
- Writing model: exactly 162 characters, byte-identical. P7's 8 phrases: occurrence counts across the issue identical to the core (4/2/2/4/2/2/2/2 — phrases 1 and 4 recur legitimately in the deck/stems, as documented in the core KIT), Korean page tags （1면…6면) kept.

## 5. Re-aimed items (the only permitted key/stem changes)

| # | Core | This edition |
|---|---|---|
| 137 | KO stem → Chinese key | same KO stem → key „Die Zugbahn des Taifuns kann sich noch ändern." · note „Siehe Seite 1" |
| 138 | KO stem → Chinese key | same KO stem → key „Bis zur Prüfung sind es noch 29 Tage." · note „Siehe Seite 2" |
| 139 | Chinese stem → KO key | stem „Bitte prüfen Sie am Wochenende das neueste Wetter. → ___" → KO key byte-identical · note „Siehe Seite 1" |
| 140 | Chinese stem → KO key | stem „Am Freitag gehe ich in den Haneul-Park, um das Silbergras zu sehen. → ___" → KO key byte-identical · note „Siehe Seite 3" |
| 150 | registry line „(开放题——范文见下方）" | „(offene Aufgabe — Mustertext unten)" · note „Mustertext in Abschnitt H auf dieser Seite (162 Zeichen)" |

## 6. P8 keep-with-next (applied from the start, per the KO×EN precedent)

The key-flow block from KO×EN's proofread fix was built into this edition's content8.py before first render: before each „— 제N면 —" group heading, if fewer than ~2 item lines of room remain in the column, the heading moves to the next column. Result: all 8 headings head their groups (— 제8면 — tops column 4 at y=1341.3); lowest key baselines per column 2516.5 / 2516.7 / 2530.5 / 2499.7 — worst clearance to the footer rule (2580) is 49.5px.

## 7. Geometry — audit, and three defects found & fixed in-build

**Audit** (`audit_ko_de.py`, sibling paint-order tool): coverage ≥30% by later opaque shapes, footer band y>2580, page edges, thin-line crossings — **0 flags on all 8 pages** (core control also 0). One tooling fix was needed: the copied script measured `<line>` elements with a zero-height box, blind to exactly the rule-crossing class it must catch; line boxes are now expanded by half the stroke width. Validated both ways: injected cover rect → 4 COVER flags; injected line across a key baseline → LINEX flag. A supplementary text–text overlap scan was also run: the only pair is the P1 wordmark vs edition line (17.6px by the glyph-box metric) — decorative, geometry identical to the core; adjudicated false positive by the card render.

**Defects the audit/QA caught in this build (all German-layer only, all fixed):**

1. **P1 word-of-the-week gloss strike.** The 2-line German gloss „…nach Norden ziehen, nordwärts ziehen." put its second line's ink band across the full-width rule at y=1844 (pixel proof: rule rows carry the „ziehen." glyph fringe; crop viewed). Fixed by compressing to one line: „북상하다 = nach Norden/nordwärts ziehen." (369.5px ≤ 434, both synonyms kept). Re-rendered: gloss ink now ends at row 1832, rule clear.
2. **P1 search-box overlap.** The German sentence under the Korean themes line wrapped to 2 lines (49 chars) and overprinted the fixed source line below. Fixed by shortening to one line: „Vier Wörter – die Themen dieser Ausgabe." (sidebar crop re-verified clean).
3. **P8 §F instr overrun.** „Wort und Bedeutung zuordnen" (ends x=1464.9) overprinted column 4's model text (starts x=1451); crop showed the collision. Fixed: „Wort–Bedeutung zuordnen" (ends x=1430.2, 20.8px clear; registry type „Zuordnen" unchanged).
4. **P7 flow repair (pre-emptive, German wording only).** Three P7 notes wrapped longer than the Chinese and pushed column 3 to end at 1759.28, which would have put the VOL.2 teaser band across the footer rule. Shortened: clinic note 4 → „Pro Text nur ein Sprachstil."; readers'-corner note → „Beispiel der Redaktion, kein echter Brief. In VOL.2: echte Briefe und beste Texte von Seite 8!"; the pattern note kept in full. Column 3 now ends 1703.76, teaser band bottom 2549.76 — identical geometry to KO×EN's shipped P7.

**Core P2 patch geometry kept:** in the DE P2 SVG the memorise-sentence first-line baseline is y=1794 and the rule sits at y=1804 (post-patch positions, unchanged).

## 8. Re-solve record (builder)

- All 16 matching items: the letter in each German note equals the item's key letter (16/16, programmatic).
- All 150 key–note pairs read through against the issue's printed facts: every German note correctly justifies its key (spot anchors: #32 Cheongsong on-site from Nov 4; #84 50 % criterion; #97 X with „50 %, nicht 80 %"; #123 59 m/s; #127 Weatheri Oct 25; #146/147 exam-day transport facts).
- The 4 re-aimed items solved directly: #137/#138 German keys are faithful translations of the frozen Korean stems; #139/#140 German stems faithfully render the core's Chinese stems, keys byte-identical Korean.
- Build runs with zero FLOW OVERFLOW / HEAD TOO WIDE warnings; totals TOTAL 150.

## 9. Character totals (visible text of the SVGs; no-space / with-space)

| page | DE | core |
|---|---|---|
| P1 | 2,283 / 2,809 | 1,877 / 2,343 |
| P2 | 2,308 / 2,801 | 1,751 / 2,160 |
| P3 | 2,000 / 2,404 | 1,560 / 1,900 |
| P4 | 1,792 / 2,140 | 1,451 / 1,761 |
| P5 | 1,950 / 2,366 | 1,501 / 1,866 |
| P6 | 1,966 / 2,451 | 1,613 / 2,043 |
| P7 | 2,370 / 2,891 | 1,731 / 2,123 |
| P8 | 7,981 / 9,805 | 4,443 / 5,449 |
| **total** | **22,650 / 27,667** | 15,927 / 19,645 |

(The extraction method reproduces the core's published totals exactly; the increase is the fuller German apparatus, as in the other DE siblings.)

## 10. Files delivered (`files/weekly-report-ko-de/`)

- `svg/` — 8 page SVGs (1950×2700).
- `cards/` — 8 PNG cards (1950×2700); **all 8 viewed by the builder after the final render** — badge, German apparatus, both P1 fixes, the §F fix, P7 band clearance and all footers confirmed on the renders.
- `Lucerna-VOL1-DE.pdf` — print PDF, 8 pages, 34,666,674 B.
- `Lucerna-VOL1-DE-web.pdf` — web PDF, 8 pages, **3,138,794 B** (< 10 MB Discord limit).
- `WEEKLY-KIT.md` — this file.

**Status: BUILDER-COMPLETE.** Next step per SOP: independent proofread of this edition (fresh eyes, full pass), then repo insert + Discord delivery to the 한국어 thread by the parent flow. Not posted by the builder.

## 11. 독립 교정 기록 — INDEPENDENT PROOFREAD (2026-10-21, fresh eyes, not the builder)

**Verdict: PASS — one complete independent pass found ZERO problems in the paper. No fixes were needed; nothing in the build sources was changed.**

What was verified independently (own extraction, own registry dump, own audit code — builder tools not trusted):

- **Core integrity (full visible-text diff, all 8 pages, both editions):** every Korean sentence/stem/option/key unchanged. The only key-text differences anywhere are the documented four: #137/#138 German keys, #139/#140 German stems with Korean keys byte-identical, #150 German apparatus line. Registry: 150 = 150 items, levels A2 57 · B1 66 · B2 27 identical, per-page counts 10/18/18/18/18/18/12/38 identical, type counts identical (Ausfüllen 49 · Ankreuzen 51 · Zuordnen 16 · Lückentext 13 · Sätze bilden 8 · Umformen 4 · Richtig/Falsch 4 · Übersetzen 4 · Schreiben 1).
- **Han characters in DE rendered text: 0.** Chinese apparatus remnants: 0 — every removed core text element is Chinese apparatus or a documented item; every added element is German apparatus or a bilingual head whose Korean half is byte-identical to the core's.
- **Keys & re-solving:** all 149 real registry keys found verbatim in the rendered P8 (whitespace-insensitive); #150 apparatus line matches the registry in both editions. All P8 assessment items (#113–150) re-solved directly from the rendered stems — all keys correct. Items 1–112 carry byte-identical Korean stems+keys from the core (itself fully proofread independently), with all 150 German notes read against the core notes for faithfulness — natural and complete. All four matching sets re-solved from the renders (25–28 b/d/c/a; 43–46 b/c/d/a; 61–64 b/c/a/d; 141–144 b/c/d/a); every matching note's letter agrees with its key. Writing model byte-identical to the core, exactly **162 characters** (no-space) in both editions.
- **Re-aimed items:** #137 key „Die Zugbahn des Taifuns kann sich noch ändern." — OPEN forecast preserved, no landing claim. #138 „Bis zur Prüfung sind es noch 29 Tage." ✓ #139/#140 German stems faithful to the core stems; their Korean keys byte-identical.
- **Geometry (own audit, PIL metrics on the production fonts, line boxes expanded by half stroke width):** 0 COVER / 0 FOOTER / 0 EDGE / 0 LINEX / 0 text–text flags on all 8 pages, except the single masthead wordmark-vs-edition-line glyph-box pair, which appears identically in the frozen core (decorative furniture artefact, confirmed on the render). Audit sensitivity validated on a synthetic positive control (injected cover rect flagged at 100%; injected rule flagged on both crossed lines). Core run through the same audit as a control: identical single flag.
- **The builder's four in-build fixes re-verified in the shipped renders:** (a) P1 word-of-week gloss one line „북상하다 = nach Norden/nordwärts ziehen." — pixel scan of the shipped card: ink ends at row 1832, zero ink on the y=1844 rule rows; compression loses nothing vs the core gloss (both synonyms of 向北移动、北上 preserved). (b) P1 search-box line „Vier Wörter – die Themen dieser Ausgabe." — source line intact below it, faithful. (c) P8 §F instruction „Wort–Bedeutung zuordnen" measured end x=1430.2, exactly **20.8 px** clear of column 4's model text (x=1451). (d) P7: readers'-corner rail last baseline 1692.68 (ink bottom 1698.68) above the phrases rule at 1733.8; VOL.2 teaser band bottom = 2431.76 + 118 = **2549.76** exact, footer rule at 2580 clear. P8 group headings all head their groups (— 제8면 — sits atop column 4); per-column lowest key baselines 2516.5 / 2516.7 / 2530.5 / 2499.7 → worst footer clearance **49.5 px**, as claimed.
- **Core P2 patch kept:** memorise-sentence baseline 1794, rule 1804; pixel scan of the shipped DE P2 card shows ink ending at row 1795, zero ink on the rule rows.
- **Pairing & furniture:** brick-red badge (#a4553a, 700, 20 pt) on P1 y=394; pairing footers + „Seite N von 8" on all 8 pages; standalone "Lucerna" wordmark (no article) on all 8 pages; images per page 1/1/2/1/2/1/0/0, payloads byte-identical to the core; credit/caption elements identical per page; P4 ladder paths pure translations; P5 Melon bars byte-identical geometry (143 : 21). P7 phrases: 8 phrases, occurrence counts 4/2/2/4/2/2/2/2 in both editions, page tags correct, German translations faithful. Facts identical (Champi OPEN forecast only; foliage two-criteria dispute as printed). Note-parenthesis hygiene: every German note parenthesis has a preceding space, half-width only (the only no-space hits are frozen Korean date/name parentheticals, identical in the core). Kinsoku line-start scan: 0 hits. All 8 cards viewed by the proofreader.

**Two documentation nits in this KIT (not paper defects, recorded for accuracy):** §9's char totals for DE P1 (2283/2809) and P8 (7981/9805) do not reproduce under the stated extraction — independent measurement gives P1 2275/2801 and P8 7979/9801; the core totals DO reproduce exactly with the same method, so the DE figures appear to predate the §7 fixes. §5 quotes the core #150 registry answer approximately; the actual registry line is '(开放题，范文如下)'. Neither affects the paper.

**Status after independent proofread: FINAL (proofread gate passed).** Web PDF 3,138,794 B < 10 MB. Not posted by the proofreader; repo insert + Discord delivery are the parent flow's steps.
