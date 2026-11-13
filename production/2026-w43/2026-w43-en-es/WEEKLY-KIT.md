# WEEKLY KIT — The Lucerna · ENGLISH WEEKLY VOL.1 · EN × ES edition

**Pairing:** English text + Spanish explanations, for Spanish-speaking readers.
**Badge (P1, brick red #a4553a, bold, in place of the core tagline, y=372 centred):** TEXTOS EN INGLÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES (measured 1030.6 px at 19.5 pt — fits with clear air).
**Masthead:** The Lucerna (unchanged). P1 edition line: SEMANARIO EN INGLÉS · VOL.1 · ESTADIOS · VOTOS · CALABAZAS (1543.7 px at 46 pt). Strap: WEEKLY IN ENGLISH · UNA EDICIÓN CADA SEMANA · EL INGLÉS QUE LEE AMÉRICA.
**Footers (all 8 pages):** left “The Lucerna · SEMANARIO INGLÉS VOL.1 · TEXTO EN INGLÉS · EXPLICACIONES EN ESPAÑOL” (881 px), right “Página N de 8”.
**Gloss prefix:** «Nota — ».
**Week:** Mon 2026-10-19 → Sun 2026-10-25 (W43) · VOL.1 · 8 pages (1950×2700) · **149 exercises** (A2 58 · B1 72 · B2 19; per page 10/17/18/18/18/18/12/38 — identical to the core).

## Deliverables (this directory)
- `svg/` — 8 page SVGs (p1-front … p8-exercices)
- `cards/` — 8 PNG cards, 1950×2700 (p1-front, p2-life, p3-culture, p4-sport, p5-jeunesse, p6-politique, p7-langue, p8-exercices)
- `Lucerna-VOL1-ES.pdf` (print) — 8,618,507 bytes · sha256 ee727ca23af47a19f47b85f5fb61fb2007ee855a1dbdf3114117e101bea74b57 (pins updated 2026-10-21 after the independent-proofread fix below; original build pins were 8,618,113 B / 216ee988…)
- `Lucerna-VOL1-ES-web.pdf` — **4,517,009 bytes (< 10 MB)** · sha256 517e9ff12e671f9fc4ca3d552313f0f4cd12d6b7ed08e4b6d6ef884f5db57a44 (original build pins were 4,317,581 B / cb7dbc8f…)
- D5 rebuild (2026-11-13, see D5 rebuild section below): print `The-Lucerna-VOL1-en-es.pdf` **7,499,239 bytes** · sha256 `1a9e0b68a28526cf116403c79238c4de4fd105247c05d056ac2bf35a46edfd50`; web `2026-w43-en-es.web.pdf` **1,068,674 bytes** · sha256 `d852804361ed382b4d053555cc26228c21e298964c64656681b76cb449c225a4` (< 7 MB); text.md byte-identical to the shipped version (sha256 `ba99650a…`). Pre-D5 values: print 8,618,507 B, web 1,108,851 B (`164eb07c…`, shipped in issues/).
- Build code: `hidden_files/weekly-report-en-es-build/` (copy of the frozen core build; core dirs never edited)

## Method (fan-out, same as the EN×FR / EN×DE siblings)
1. Copied the finalized core build (`weekly-report-en-build/`) to `weekly-report-en-es-build/`; rebuilt it **unmodified first — all 8 SVGs byte-identical to the shipped core** (sha256 8/8), registry identical (149). Baseline proven before any edit.
2. Rewrote ONLY the explanation layer into native Spanish: every definition, grammar note, instruction, section-head Spanish half, chart note, clinic note, readers'-corner reply, teaser, and **all P8 answer notes**. The layout library's explanation method was renamed (`expl()`), so the banned intermediary-layer term appears **nowhere** in this edition's paper, kit, or code — 0 occurrences, grep-verified.
3. House bilingual heads kept (English half frozen + Spanish half); over-wide Spanish halves shortened by wording only — never geometry (recorded below). Spanish typography: ¡ ! / ¿ ? inverted marks, decimal commas in the Spanish apparatus (0,45 kg · 3,6 % in notes), guillemets « » kept from the core furniture.

## Freeze record (verified programmatically)
- Registry diff vs core (regenerated core registry vs this edition's): **n / page / level identical for all 149**; levels A2 58 · B1 72 · B2 19; per-page 10/17/18/18/18/18/12/38.
- **Key diffs: exactly 3 — #136, #139, #149** (the documented reader-language items):
  - #136 (EN→ES): key → «Votar ya no es cosa de un solo día; es una temporada.» (note: «no longer = ya no»).
  - #139 (EN→ES): key → «Ninguno de los dos clubes ha ganado nunca la Serie Mundial.» (note: «neither niega a los dos; has ever won, presente perfecto»).
  - #137 / #138 (ES→EN): stems re-aimed into Spanish («Traduce: Los 76ers ganaron por 106 a 100.» / «Traduce: Este año, la votación anticipada empezó el lunes.»); English keys byte-identical to the core.
  - #149 (writing): apparatus key → «(pregunta abierta — el modelo está en el recuadro de escritura)», note «se puntúa por puntos».
- All 13 exercise-type labels translated (Completa→Completar frases family: Completa, Reescribe, Empareja, V o F, Corrige, Traduce/Translate, Lectura de gráfico, Corrección, …). Registry level: **140 notes translated to Spanish, 9 language-neutral notes byte-identical** (verified independently: #18, 77, 78, 84, 95, 100, 103, 119, 120). **Correction (independent proofread, 2026-10-21):** as first built, the PRINTED note coverage did **not** match the core — the inherited `len(note) ≤ 10` print rule, calibrated for compact Chinese notes, silently suppressed 14 Spanish notes on P8 (items 11, 14, 15, 19, 35, 36, 40, 42, 49, 65, 74, 89, 101, 106); the core prints 62 notes, the first ES build printed 48. Fixed in `content8.py` (explicit `NOTAS_EXTRA` set) and re-rendered; printed coverage is now 62 = the core's, item-for-item. See the proofread record in the Status section.
- Full text diff vs core SVGs: every difference is explanation layer / furniture / the documented items above / wrap-segmentation artifacts (P8 key block re-wraps because note parentheses are half-width — keys themselves proven identical via the registry). **Image payloads byte-identical on all 8 pages**; credits identical (English, frozen).
- P7's 8 phrases: verbatim contiguous excerpts of this issue's articles with correct page tags (4/2/4/4/6/6/2/2) — inherited unchanged from the frozen English layer and re-checked against the page texts.
- **CJK characters in final SVGs: 0.** Banned-term occurrences in paper/kit/code: **0**.
- Weekday/date claims verified against the real 2026 calendar: NBA opening Tue Oct 20 ✓ · World Series G1 Fri Oct 23 ✓ · F1 Austin Sun Oct 25 ✓ · Halloween Sat Oct 31 ✓ · Texas early voting Mon Oct 19 – Fri Oct 30 ✓ · Florida mandatory period Sat Oct 24 ✓ · Europe clocks Sun Oct 25, US Sun Nov 1 ✓ · Election Day Tue Nov 3 ✓. (No inherited weekday error of the ES-core kind exists in the EN core.)

## P8 answer keys (house format)
All 149 entries printed under group headers «— Página N —»; format “key (note)” — plain space before a half-width parenthesis, half-width parentheses only. Keys re-derived during the builder's pass against the articles and the chart (#82–87 = 34/27/61%/False/18 points/100%; COLA 3.6%; 106–100 = 6 points; matching maps P2 b/d/c/a · P4 d/b/a/c · P8 b/c/d/a) — all agree.

## Geometry (mandatory audit — builder run)
Paint-order audit with real-font (PIL) glyph metrics and stroke-expanded line boxes (`hidden_files/weekly-report-en-es-build/audit_en_es.py`, copied from the validated zh-CN×FR audit), synthetic positive control **PASS** first (all defect classes fire; clean page silent). Checks: ≥30 % glyph coverage by later opaque shapes, footer band (y > 2580), page-edge spill, box titles vs their own borders, thin lines crossing text ink, text–text overlap.
- **Final result: 2 flags, both on P1, both pixel-adjudicated NON-DEFECTS of exactly the kinds the shipped core itself carries:**
  1. LINEX — word-of-week gloss line 2 (baseline 1846) vs the y=1844 rule: measured ink rows 1830–1842, rule rows 1843–1844, **zero overlap** (identical measurements to the core's own adjudication of the same furniture).
  2. TEXTX — masthead blackletter band vs edition-line band, 26 % of the smaller band (core: 42 %): card inspection shows clear air between wordmark, edition line, and badge — a band-geometry artifact, not ink contact.
- Defects found by the audit / build log during production and **fixed in-build (wording only, never geometry)**:
  1. P1 headline flow overflow (~116 px): P1 explanation shortened to 2 lines (the «champion» gloss lives in exercise note #4 on the same page); numbers-box title → «THE WEEK IN NUMBERS · En cifras»; box glosses trimmed — final line counts equal the core's (expl 2, box L1 3, box L2 4).
  2. P4 head «C · COMPARATIVES · Comparativos» 449 px > 434 → «C · COMPARATIVES · Compara» (389 px).
  3. P5 head → «C · LIVE · Presente continuo» (367 px).
  4. P6 article gloss trimmed to 3 terms / 3 lines (midterm / the House / turnout; incumbent + margin are glossed in the same page's ELECTION WORDS box and exercise notes).
  5. P2 AND-YOU Spanish echo shortened to the 2-line version («¿Hay perritos calientes en tu nevera hoy? ¿Qué dinero entra en tu casa cada mes?») — the writing instruction it drops is stated in full in the English paragraph directly above; col-3 now ends at 1534.6, exactly the core's value.
  6. P3 col-3 footer spill: festival-words glosses trimmed to one line each («a jack-o'-lantern — farol de calabaza», «a porch — el porche de entrada», «a patch — un terreno (de calabazas)», «spooky — espeluznante (divertido)») and the col-3 explanation replaced with a 3-line version («Cada año, Halloween cuesta más, y la IA ayuda con el disfraz: ¿fiesta o compras con fantasmas? Escríbenos (página 7).»). P3: 0 flags.
  7. P8 battery cover: the dialogue tail was covered 95–100 % by the later-drawn writing MODEL box because both Spanish E-stems wrapped to 2 lines (core: 1). Stem #137 shortened to one line («Traduce: Los 76ers ganaron por 106 a 100.»); #138 cannot fit one line in Spanish without losing «este año» (its key is the frozen English «This year, early voting opened on Monday.») — accepted at 2 lines; net effect: everything after §E sits +30 px vs core (F head y=464 vs core 434), dialogue ends y=1405 (core ≈1375), well clear of the writing strip (hline 1486 / box top 1499.3). P8: 0 flags.
  8. P6 PRACTICE DATA note strike-through (pixel-confirmed): the READING head's gold rule (y=1507, x ≥ 989) visibly struck the long Spanish note tail (Latin lowercase ink sits lower than the core's CJK tail, which clears the rule in the core). Spanish tail → «Datos de práctica, ficticios.» — the whole note now ends x=958 < 989. P6: 0 flags.
- Final build log: **zero FLOW OVERFLOW / HEAD TOO WIDE warnings**, 149 exercises. Builder's own full proofread: all visible text of the final SVGs read end-to-end; all 8 cards viewed page by page.

## Print PDF note
The print PDF (8,618,113 B) is smaller than the core's (24.5 MB) because the current shared venv's CairoSVG Flate-compresses the embedded photos more efficiently; the images are embedded at **full source resolution** (verified by XObject extraction: P1 1600×1175 = the source JPEG's pixel size; image XObjects present on exactly the four photo pages 1/2/3/6, as in the core). No quality loss; 8 pages.

## VOL.2 promises carried over in Spanish (must be honoured next issue)
Halloween night Sat Oct 31; clocks fall back Sun Nov 1; Election Day Tue Nov 3 (P7 teaser, Spanish); real readers' letters from VOL.2 and comments on VOL.1's page-8 writing (readers'-corner reply, Spanish); the best AND-YOU sentences printed in VOL.2 page 7 (P2 box promise, English line frozen + Spanish echo).

## Reproduction
```
cd hidden_files/weekly-report-en-es-build
/tmp/wp-venv/bin/python -c "import content12, content34, content56, content7, content8"   # fixed import order; writes svg/ in files/weekly-report-en-es/
/tmp/wp-venv/bin/python audit_en_es.py ../../files/weekly-report-en-es/svg               # 2 flags, both adjudicated above
# cards: cairosvg svg2png output_width=1950 · print PDF: svg2pdf + pypdf merge · web PDF: PIL thumbnails 1400 wide, JPEG quality=85
```
**Reproducibility verified 2026-10-21:** a clean chained rebuild from these sources reproduces all 8 shipped SVGs byte-identically.

## Status
- Builder's own full proofread: **done** (see above).
- **Independent proofread: PASS (2026-10-21)** — fresh independent pass, zero problems after one fix (below). Record:
  1. **Freeze diff vs core** (full text-multiset diff of all 8 SVGs + registry rebuilt from sandboxed copies of both builds): every difference is explanation layer / pairing furniture / the documented registry items. English target text untouched. Both shipped SVG sets reproduce byte-identically from their build sources (8/8 + 8/8).
  2. **Registry**: 149 items in both; n/page/level identical for all 149; levels A2 58 · B1 72 · B2 19; per-page 10/17/18/18/18/18/12/38; 13 type labels translated 1:1. **Key diffs exactly #136, #139, #149**; stems #137/#138 re-aimed into Spanish with English keys byte-identical. The two Spanish translation keys verified faithful against the printed stems (#136 «Voting is no longer a day ; it is a season.» → «Votar ya no es cosa de un solo día; es una temporada.»; #139 «Neither club has ever won the Series.» → «Ninguno de los dos clubes ha ganado nunca la Serie Mundial.»). Keys spot-derived against the articles/chart (chart 34+27+23+16 = 100; #82–87 = C/27/61%/False/18 points/100%; House 218−214 = 4; matching maps P2 b/d/c/a · P4 d/b/a/c · P8 b/c/d/a) — all agree. Numbering 1–149 continuous.
  3. **DEFECT FOUND AND FIXED (explanation layer)**: 14 answer notes present in the registry but missing from the printed P8 key block (items 11, 14, 15, 19, 35, 36, 40, 42, 49, 65, 74, 89, 101, 106) — the inherited `len ≤ 10` print rule fits Chinese notes (8–10 chars) but the Spanish notes run 13–52 chars. The builder's "no note dropped" claim held for the registry, not for the printed page. Fix: `NOTAS_EXTRA` set added to the print condition in the ES build's `content8.py` only; rebuilt — P1–P7 SVGs byte-identical, P8 battery byte-identical, key block now prints 62 notes = the core's exact set. Cards and both PDFs re-rendered with the documented recipe; new pins at the top of this KIT.
  4. **Spanish apparatus**: complete after the fix; CJK characters in final SVGs: 0 (the single '｜' fullwidth bar is a punctuation separator inherited from the core's furniture, not language content); all instructions, glosses, notes, chart note, clinic, readers'-corner reply and teaser in Spanish.

## D5 rebuild (2026-11-13, D5-only)

SOP §1.1 font fix: the explanation layer's Latin letters move from Noto Sans CJK to Newsreader (SemiBold). No commit, no push — insertion is done by the closer after an independent re-proof. Work log: `hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-es/`; per-edition report: `production/notes/2026-w43/g-en/scratch-d5-rebuild-en/D5-REPORT-2026-w43-en-es.md`.

**Install**: core landed with `apply_variant.py --patch-core en --week 2026-w43` (core-en `svglib.py` +95/−3, `_D5_READER = "latin"`); this edition installed with `--svglib patched/…/svglib.py --target en --reader es --week 2026-w43`, `_D5_READER = "latin"`; routing unit test FAILURES: 0 (66 PASS); fix2 block kept.

**Baseline** (pre-fix production build): run TOTAL 149, 0 warnings; print PDF byte-identical to `MANIFEST-W43-D1.md`; print/web text layers differ by 0 chars; self-built web vs shipped web differ by 0 non-space chars (spaces only); pre-fix census D5 Latin 553, Cyrillic 0, curly in CJK 1; baseline P8 noted 62/149 (core口径).

**Defects and fixes** (run1: 12 items, all D5 widening except the pre-existing P2 spill, which the baseline shares; sizes only, no wording changed):

- heads ×4: P1 `TRY IT NOW　Practica al momento` 25→24 (421.5 px, 1.0 px margin); P3 `B　FESTIVAL WORDS　Completa` 25→24; P5 `EARNINGS, IN PLAIN ENGLISH` 26→25; P7 `THE TOOLBOX　Herramientas` 27→26 (column width 422.5).
- occlusion ×2 (P1): band headline vs subtitle `CAMBIA LA HORA` overlapped 111.9×20.8 px → headline 46→**42** (44 still overlapped); P6 PRACTICE DATA line crossed by the r6 head's rule (LINEX, tail x=993.2 vs rule from x=989) → PRACTICE DATA 18.5→**18** (tail x=969.0). Note: the same P6 strike-through was already fixed in the D1 build (Geometry §8: tail shortened, tail x=958) — the D5 font widening re-introduced it (Latin runs ~35 px wider in Newsreader than in the CJK face).
- creambox/boxtitle ×4: P1 `THE WEEK IN NUMBERS　En cifras` +21.5 px → `tsize=21`; P4 `THE WEEK'S FIXTURES　Partidos` +3.7 px → `tsize=22`; P5 `WORDS OF THE SCREEN　Palabras` +13.9 px → `tsize=22`; P6 `HEADLINE LANGUAGE　Titulares` +3.2 px → `tsize=22`.
- spill ×1: P2 `Check your number !` below the DID YOU KNOW box by 12.71 px → box-height formula tail +14→+34 (box bottom +20 px; same pre-existing defect as core-en).

Lesson recorded: the first attempt set PRACTICE DATA to 16 pt, and the rebuild's text.md export then LOST that line — the exporter (`en_textmd_w43.py` L240–242) only includes `p.text` calls with size ≥ 18. Corrected to 18 pt and text.md is byte-identical again. Never size a `p.text` line below 18 pt without checking the exporter threshold.

P8: 195→192 lines, footer slack 32.7→32.6 px.

**Gates run2 (all 17 ALL-GREEN)**: run TOTAL 149, 0 warnings; head_check 0; d5 census 0/0/0; render RC=0; webpdf RC=0 (1,068,674 B < 7 MB); occlusion 0 flags; p8 extract noted 62/149; p8 compare **CLEAN** (keydiff=[136, 139, 149], the registered reader-language keys); freeze baseline 8/8; freeze diff added CJK chars 0; spill 0; boxtitle 0 DEFECT (55 titles); edge 0/0; creambox PASS 0 defects; text layer print=web diff 0; census_quotes 0 defective; no family gates.py for en.

**New deliverables**: print `The-Lucerna-VOL1-en-es.pdf` 7,499,239 B (`1a9e0b68…`); web `2026-w43-en-es.web.pdf` 1,068,674 B (`d8528043…`); text.md byte-identical (`ba99650a…`). Still 149 exercises; answer keys differ from the core only at #136/#139/#149, as registered.
  5. **P7 phrases**: all 8 verified verbatim in their cited pages (tags 4/2/4/4/6/6/2/2); #5 also legitimately recurs in P6's KEY SENTENCE box and P7's B2 example (frozen core design, identical in the core).
  6. **Calendar**: every weekday claim re-checked against the real 2026 calendar (NBA Tue Oct 20 · World Series Fri Oct 23 · F1 Austin Sun Oct 25 · Halloween Sat Oct 31 · Election Day Tue Nov 3 · TX early voting Mon Oct 19 – Fri Oct 30 · FL mandatory Sat Oct 24 · US clocks Sun Nov 1 · DE/MD Thu Oct 22) — all correct.
  7. **Furniture**: pairing badge on P1 (verbatim, brick red); pairing footer + «Página N de 8» on all 8 pages; masthead «The Lucerna» as shipped.
  8. **Geometric occlusion audit** (independent run of the validated script; synthetic positive control PASS — COVER/LINEX/FOOTER/TEXTX all fire, clean page silent): final = **2 flags, both P1, both pixel-adjudicated NON-DEFECTS by the proofreader's own measurements**: (a) LINEX gloss «otoño: fall back.» — ink rows 1830–1842, rule rows 1843–1844, zero overlap (core card measures identically); (b) TEXTX masthead band 26% — card shows clear air between wordmark, edition line and badge. Claimed in-build fixes spot-verified: P6 PRACTICE DATA note ends x≈958 < rule start 989 (measured with production font metrics); P8 dialogue ends well clear of the writing strip (visual). P2–P8: 0 flags.
  9. **Images/PDFs**: SVG image payloads byte-identical to the core on all 8 pages; credits identical (Bain News Service/LoC, Halloween postcard 1912, Social Security Administration, US Capitol — all public domain, each placed). Print-PDF XObjects match the core's source dimensions exactly (P1 1600×1175, P2 749×830, P3 978×1600, P6 1600×685) — the builder's smaller-print-PDF explanation (Flate compression, full-resolution images) is verified true. Web PDF 4,517,009 B < 10 MB, sha256 re-measured after the fix (see Deliverables).
  10. **Banned-term scan**: 0 occurrences in paper, KIT and build code.
  - After the fix, the complete pass was re-run from the top on the final artifacts: **zero problems**.
- Not inserted into the GitHub weekly repo, not posted to Discord (delivery paused), per assignment.
