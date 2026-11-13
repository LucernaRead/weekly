# Independent Re-proof Note — Lucerna Weekly 2026-W47, ru-nl

**Re-proofer:** independent (not fix1 repairer, not proof1). **Scope:** `production/2026-w47/2026-w47-ru-nl/` only, against finalized core `production/2026-w47/core-ru/`. **No production file modified, no commit, no push.** All work in `hidden_files/w47/scratch-reproof-ru-nl1/`.

## Verdict: (a) ZERO DEFECTS

Every fix1 claim re-measured independently; every mechanical gate re-run; all 150 questions hand-verified key-vs-stem; all 8 cards read visually; all 42 occlusion flags adjudicated on the delivered PDF raster + zoomed crops.

## 1. Opening verification — three SHAs

All three match the coordinator's 18:39 UTC values exactly:

| Artifact | SHA-256 | Size |
|---|---|---|
| Print PDF `Lucerna-VOL4-ru-nl.pdf` | `5843ae6b80ac7e38298ec33d565b19e49d73dc165e6d18ffeec5bdddd4982fa2` | 21,291,643 B |
| Web PDF `Lucerna-VOL4-ru-nl-web.pdf` | `d3f016d58cb7b37a35cbf5b05e9a012c49bff6a116baf716db39aca56500b3eb` | 3,387,332 B |
| Text `2026-w47-ru-nl.text.md` | `8ac1336dbc521f510747d2a838a52e763d6452a81f8ea75ee6fc7c7687942423` | 64,051 B |

HEAD at start: `c0382fa7f6c0915057611d714f75949d81a29956`. Opening snapshot: 42 files hashed in `opening-snapshot.sha256`. Closing snapshot vs opening: **zero changes** (see §9).

## 2. D7 (the only claimed defect) — verified fixed

`content7.py:12` P7 band subtitle reads `p.band("ЯЗЫК　TAAL", "Lucerna", "Фокус на язык　Три уровня, три темы　Drie niveaus, drie thema's")` — U+0027 `'`; U+2019 count = 0 in `content7.py` and 0 in `2026-w47-ru-nl.text.md` (L504 same `thema's`). Both PDFs: U+2019 = 0 on all 8 pages (print and web). `text.md` is 64,051 B vs the KIT-recorded pre-fix 64,053 B = −2 B, exactly the UTF-8 `’` (3 B) → `'` (1 B) delta.

**PIL true-ink** (Noto Sans CJK SC 18 px, `d7-pil.log`): U+2019 advance 18.00 px, ink bbox (0,5,18,21); U+0027 advance 5.00 px, ink bbox (0,7,5,21); full subtitle advance 229.77 → 216.38, delta 13.39 px.

**Band raster** (rows 148–161, `d7-raster.log`): thema → `'s` blank space = **3 SVG px on all three rasters** — card: last solid col 1816.00 → first solid col 1820.00; print/web (2×): 1817.50 → 1821.00. Same-band neighbourhood check (card, 27 solid-ink groups): inter-letter gaps 1–5 px, median 3 — the fixed 3 px gap is exactly the median, inside the normal range. Zoomed print crop `crop-d7-themas-print.png` reads `thema's` as one word, no longer `thema' s`.

**Intentional keeps verified:** `ABSTRACT.txt` has 1× U+2019 in a different sentence (`thema's van de week`); `check_core.py` L94 `CLOSES` set constant contains `’` — both non-D7, correctly untouched. Core P7 SVG contains no `thema` (the Dutch tail is a fan-out addition); freeze-diff shows P7 **added** `"　Drie niveaus, drie thema's"` with no removed counterpart.

## 3. Earlier defects survive (D1 / kicker / D2 / D6)

All verified in the **rendered** SVG (ElementTree, line-joined by baseline) — not just in source:

- **D1, P6 kicker:** y=1552 line `ЧЕМ ЗАЙМУТСЯ НА ЭТОЙ НЕДЕЛЕ?　УЧЕБНЫЕ ДАННЫЕ　OEFENGEGEVENS`.
- **D1, P6 disclaimer:** y=1582 line `Это учебный опрос редакции для упражнений — не настоящая статистика. Dit is een oefenenquête van de redactie — geen echte statistiek.` (RU + NL both present); bar chart 38/26/18/18 = 100%.
- **D2 kicker, P1 tagline:** y=372 `ЕЖЕНЕДЕЛЬНАЯ  ГАЗЕТА  ДЛЯ  ИЗУЧАЮЩИХ  РУССКИЙ  ЯЗЫК  —  НАСТОЯЩАЯ  РОССИЯ,  ПО-РУССКИ` with **9 double-space runs, 0 single-space runs** (`content12.py:18`, D2 fix intact in the render).
- **D2, P7 subtitle:** y=168 `Фокус на язык　Три уровня, три темы　Drie niveaus, drie thema's`.
- **D2, P8 subtitle:** y=168 `PAGINA 8　Большой тест недели + все ответы`.
- **D6, Q20 key:** registry `желании` (`желание = een wens`) and printed P8 key `желании`.
- **Q25:** match set on P2 (`b. День студента`, options a. День психолога / b. День студента / c. Всемирный день ребёнка / d. день рождения Деда Мороза); registry key `b`; mapping 17 Nov→b, 18 Nov→d, 20 Nov→c, 22 Nov→a.

## 4. Mechanical gates (all self-run; full table in GATE-LOG.md)

| Gate | Result |
|---|---|
| `run.py` rebuild (scratch copy) | rc=0, **TOTAL 150** (P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38); A2 50 / B1 76 / B2 24; 0 FLOW OVERFLOW / HEAD TOO WIDE; rebuilt SVGs **8/8 byte-identical** to production (twice, deterministic) |
| `freeze.py` baseline, core-ru | rc=0, **8/8 SVGs byte-identical** |
| `freeze.py` diff core→edition | rc=0; removed distinct 487, added 321; removed Cyrillic **15, all on P8** (14 Morozko-caption words + Q46 `можно`); **added Cyrillic 0**; added CJK 8 = U+3000 only |
| `p8.py` | extract 150/150 core and edition; compare **CLEAN**, keydiff `[137, 138, 139, 140]` (Dutch E-section by design) |
| Print vs web text layer | all 8 pages **byte-identical**, 57,957 B per PDF; U+2019 = 0 both |
| `check_core.py` | rc=0; GOLDEN 8×2, BAD 0, gloss fails 0; P8 SVG text chars 11,138; 1 orphan line-start (P7 y553 `”».`, KIT-known benign); 1 same-baseline collision (P1 y1712 italic «чёрная пятница», same as core) |
| P8 minimum font | **9.75 pt** both PDFs = SOP §1.1 floor (P1 11.62, P2 11.62, P3 12.75, P4 11.62, P5 11.62, P6 12.75, P7 11.62, P8 9.75) |

## 5. 150-question hand verification — 0 mismatches

Dumped all stems from the source AST (130 `.ex()` + 20 `match_set` = 150); 0 mismatches vs `reg.json`. Hand-verified Q1–Q150 key vs stem (not just three-source agreement). Spot anchors re-checked against article text: **21 goals** in round 14 (P4 table sums 1+3+1+6+2+3+4+1); 1946 Prague decision; 16:20 Moscow sunset; 83rd-minute Rostov equaliser; 20:45 Baltika kickoff; full 8-match table in `content34.py` (`res14`); Masha passage (`text.md` L622) anchors Q129–Q132 verbatim; 14.4M orders at `text.md` L364; 27 Nov 2026 is a Friday. Registry vs printed P8 keys: exactly 1 apparent mismatch — Q150, registry placeholder `(Open opdracht, modeltekst hieronder)` vs printed `✓`; core also prints `✓`, core-vs-edition keydiff is only [137–140], so this is the open-task extraction artefact, not a defect.

## 6. Occlusion adjudication — 42/42 CLEAR on the delivered PDFs

Audit: **42 flags {TEXTX: 42}, 0 LINEX**; core also 42; NEW vs core: 3 (P7 `ЯЗЫК` vs `　TAAL` 3.8×34.0 px; P8 `ОТВЕТЫ` vs `　TEST EN ANTWOORDEN` 8.0×35.5 px; P8 `ОТВЕТЫ` vs `　ANTWOORDEN — PER PAGINA…` 4.5×19.0 px).

**Audit systematic error (found by this re-proof):** `tools/occlusion_audit.py` `resolve_font` maps `"Noto Serif"` / `"Noto Sans"` to the CJK SC face, while the build (`svglib.py`) measures Cyrillic with real Noto Serif / Noto Sans. The audit therefore overstates Cyrillic advance ~3% (e.g. flag #1 `Зенит`: audit advance 171.8 vs build 166.3, diff 5.5 px = the flagged overlap; #33 `ЯЗЫК`: 136.6 vs 133.0; #39 `Кипренского`: 128.7 vs 125.3). The 42 TEXTX flags are largely audit mis-measurement. Upstream `adjudicate_ru.py` hardcodes SX=1950/1800 (~1.0833), the wrong scale here (SVG px == card px, SX=1.0); do not use it.

**Adjudication path (v1–v5 all documented as superseded in the scratch dir):**
- v1 column projection split at B.x: false OVERLAPs (last glyph overhangs B.x).
- v2 8-connected components, all rasters held: OOM-killed rc=137.
- v3 components on fringe-inclusive mask: AA fringe bridges hairline gaps; also subtracted 1 SVG px instead of 1 raster px.
- v4 blank-column profile: too strict — glyphs interleave vertically (chevron arm tips dip into rows where the bowl is indented), so no single column is blank across the whole band even though every ROW has a gap.
- v5 vector per-char PIL gaps: −0.02..−1.02 for 32/42 — per-char `getbbox` overhang disagrees with both the string `getbbox` (+0.4 for #7) and the raster; sub-pixel hinting makes the vector edge unreliable at this scale.

**v6 (final, solid-component, `adjudicate_reproof6.py` + `adjudication.json`):** solid ink = RGB distance from modal bg > 190; 8-connected components in the y-overlap band; sides attributed by component leftmost pixel vs boundary B.x; OVERLAP iff an A-side component spans past B.x+3 or B-side ink is absent while A-side ink crosses the boundary; otherwise CLEAR with gap = (min centre distance − 1 raster px) / scale.

- Card (1×): 30 CLEAR / 12 OVERLAP. Print (2×): **34 CLEAR / 8 OVERLAP**. Web (2×): **34 CLEAR / 8 OVERLAP**.
- The 34 print/web CLEARs have solid-component gaps **0.62–50.5 SVG px** (4× Краснодар 1.08; Кипренского 1.08; ЯЗЫК/TAAL 48.0; ОТВЕТЫ 50.5 / 26.5).
- The 8 print OVERLAPs (#4, #11, #13, #17, #28, #29, #30, #31) were each inspected on a 6× zoomed crop of the print PDF (`crop-flagNN-print.png`, all viewed): every one reads cleanly — `пятница»:`, `толерантности.`, `студента.`, `биография:`, `смартфоны,`, `студента,`, `сбивается.`, `Планируйте:` — the mark is clearly separate and legible. Their string-level PIL gaps are −0.6..+0.4 SVG px: a sub-pixel layout touch (≤0.13 mm at print size), invisible at reading distance. The v6 raster touch is a quantisation artefact: a 0.4 px vector gap cannot form a full blank raster column, and diagonal 8-connectivity bridges the corner pixel (proven exactly for #7: `р` solid ends col 231, `»` solid starts col 232, with only AA fringe (lum 146–246) in between).
- The 4 card-only extra OVERLAPs are the same phenomenon at 1× (#7/#21/#22/#25 Краснодар: print CLEAR 1.08; #8, #38: print CLEAR 1.0). The card is a 1× preview raster of the same vector content; the delivered PDFs are the authoritative artifact.
- **Final true value: 42/42 CLEAR on the delivered print and web PDFs**, with the 8 sub-pixel cases recorded honestly (visually CLEAR, PIL string gap −0.6..+0.4 SVG px — a tooling-tolerance note, not a content defect).

## 7. Visual read of all 8 cards — clean

- **P1:** masthead, VOL.4, tagline, lead `14-й тур: «Зенит» и «Динамо» — по 31 очку`, `ТУР В ЦИФРАХ` box, Q1–6, November-park photo (Toxer427, CC0), `СНЕГ БУДЕТ?`, `КОРОТКО`, contents, word of the week, blitz quiz Q7–10. No overflow/overlap.
- **P2:** `ЖИЗНЬ` band, student/Ded Moroz story, `ПРАЗДНИКИ НЕДЕЛИ` rail (16–22 Nov), `А ВЫ?` box, Yuon `«Зима. Ростов»` painting with caption, 4 words of the week, Q11–28 incl. Q25 match set. No overflow/overlap.
- **P3:** `КУЛЬТУРА` band, 19 Nov cinema story, rails, Q29–46. No overflow/overlap.
- **P4:** `СПОРТ` band; **the 8-row results table is present and fully legible** (Lokomotiv–Rubin 0:1, Fakel–Dynamo 1:2, Akhmat–Rodina 1:0, Krasnodar–CSKA 4:2, Krylia–Orenburg 2:0, Spartak–Akron 2:1, Zenit–Rostov 2:2, Baltika–Dynamo Mkh 0:1 — all scores consistent with Q52–Q64); 15th-round fixtures table; 1912 Olympic team photo; `ТАБЛИЦА: ТОП-5`; Q47–64. No overflow/overlap.
- **P5:** `МОЛОДЁЖЬ` band, Black Friday story (14.4M orders, 27 Nov Friday, Cyber Monday 30 Nov), corn photo, `ЧЁРНАЯ ПЯТНИЦА: ДАТЫ` rail, Q65–82. No overflow/overlap.
- **P6:** `БОЛЬШОЙ РАЗБОР` band, week article, day-by-day calendar strip (16–22), `УЧЕБНЫЕ ДАННЫЕ` + bilingual disclaimer line, bar chart 38/26/18/18, Q83–100. No overflow/overlap.
- **P7:** `ЯЗЫК TAAL` band + subtitle `…Drie niveaus, drie thema's` (reads as one word), 3 language columns, `ОШИБКИ` rail, Pushkin portrait by Kiprensky 1827 with full caption, word of the week, readers' letters, 8 phrases of the week, next-week band. No overflow/overlap.
- **P8:** `ТЕСТ И ОТВОРЕНЫ` band + subtitle, sections A–H (Q113–150), Masha passage, Q150 model text (97 words), full answer key Q1–150 with Dutch explanations. Keys end col 3 y=2389.29; Morozko image skipped by the build's own condition (by design, same as W46). No overflow/overlap/clipping.

## 8. Non-defect notes (for the parent, not defects in this edition)

- **Documentation drift:** `WEEKLY-KIT.md` §5 still lists pre-fix1 numbers — print PDF SHA `8982ce29…` / 21,315,805 B, web SHA `abc3ec69…` / 3,387,072 B, text.md 64,053 B — stale vs the delivered files. KIT should be re-issued.
- **Missing references (cleaned/missing, not defects):** the brief `hidden_files/w47/briefs/brief-coordinator.md` named in the task does not exist; `adjudicate_ru.py` has no copy anywhere in the repo (only a W45 proof log references it); `hidden_files/w47/scratch-fanout-ru/` is gone. The edition dir is untracked in git (`?? production/2026-w47/2026-w47-ru-nl/`), so the pre-fix1 state cannot be diffed from git.
- **Audit tool finding:** `tools/occlusion_audit.py` `resolve_font` uses the CJK SC face for `"Noto Serif"` / `"Noto Sans"`, overstating Cyrillic advance ~3% and generating the 42 TEXTX flags; the flags are box-overlap, not ink-overlap. Worth fixing in the tool (out of scope for this re-proof; no production files touched).
- **1× card raster quantisation:** at 1×, 12 flags show solid-ink diagonal touches for vector gaps ≤0.5 px; at 2× print/web they separate or read clean. Not a defect.

## 9. Production zero-write check

Closing full-edition SHA-256 re-hash vs `opening-snapshot.sha256` (42 files, `__pycache__` excluded): **0 differences**. No production file was modified by this re-proof. `run.py` rebuilds ran only in `scratch-reproof-ru-nl1/run-copy/` with OUT redirected to scratch; renders only in scratch copies; the production web PDF was never overwritten (text layer compared only).

## Evidence index (all under `hidden_files/w47/scratch-reproof-ru-nl1/`)

`opening-snapshot.sha256`, `closing-snapshot.sha256`, `run-copy/`, `run-rebuild.log`, `svg-rebuild-compare.log`, `freeze-core/` + `freeze-core.log`, `freeze-diff.json` / `freeze-diff.log` / `freeze-diff-analysis.txt`, `p8-edition.json`, `p8-core.json`, `p8-compare.json` / `.log`, `pdftext/print-p1..8.txt` + `web-p1..8.txt`, `check-core.log`, `p8-font.log`, `occlusion.json` / `occlusion.log`, `adjudicate_reproof.py` + `adjudication-v1-superseded.json`, `adjudicate_reproof2.py`, `adjudicate_reproof3.py`, `adjudicate_reproof4.py` + `adjudication4.log`, `adjudicate_reproof6.py` + `adjudication6.log` + `adjudication.json` (v6 final), `adjudicate_vector.py` + `adjudication-vector.log` + `adjudication-vector.json` (v5), `reg.json`, `ex-stems.json` / `ex-stems.txt`, `key-crosscheck.log`, `d7-pil.log`, `d7-raster.log`, `d-survival.log`, `d-survival2.log`, `d-survival3.log`, `d-survival4.log`, `debug-flag7.txt`, `debug-flag7-cc.txt`, `debug-flag7-grid.txt`, `debug-flag10.txt`, `debug-geometry.txt`, `crop-flag7-line.png`, `crop-flag7-tight.png`, `crop-flag10.png`, `crop-flag10-print.png`, `crop-flag04-print.png`, `crop-flag11-print.png`, `crop-flag13-print.png`, `crop-flag17-print.png`, `crop-flag28-print.png`, `crop-flag29-print.png`, `crop-flag30-print.png`, `crop-flag31-print.png`, `crop-d7-themas-print.png`.


---

# Re-proof (independent) — 2026-w47-ru-nl — Fix 1 round (text.md L836)

- **Edition:** 2026-w47-ru-nl (Russian target × Dutch reader, VOL.4)
- **Proofer:** independent re-proof agent (did not build this edition; fresh round
  for the Fix 1 text.md change — the note above is the earlier D7 round)
- **Date:** 2026-11-11
- **Scope:** the text.md Fix 1 (L836 Q150 appendix line) plus a full independent
  read of the edition as delivered: all 8 pages of the print PDF (authoritative
  rendering, read visually page by page at 100 dpi), the full text.md
  (840 lines), and the web PDF (text layer + P8 render).
- **Verdict: (a) ZERO FINDINGS**

## SHAs (start and end of read — identical, nothing changed mid-read)

| File | SHA-256 | Size |
|---|---|---|
| `2026-w47-ru-nl.text.md` (start + end) | `849015f1e920f15c8a0040157a477aab5efb75200f27ef8bcac43160e544e9b0` | 64,013 B |
| `Lucerna-VOL4-ru-nl.pdf` print (start + end) | `5843ae6b80ac7e38298ec33d565b19e49d73dc165e6d18ffeec5bdddd4982fa2` | 21,291,643 B |
| `Lucerna-VOL4-ru-nl-web.pdf` web (start + end) | `f317713abb247128035ec1a2643213301face29828782320fb4b6dc2de74ce05` | 3,387,356 B |

- text.md SHA matches the brief's required hash exactly; size 64,013 B as specified.
  The fix is confirmed in place before any reading began.
- Print SHA matches KIT §5 exactly (`5843ae6b…`). Print was NOT rebuilt by the fix.
- Web SHA differs from KIT §5 (`d3f016d5…`, 3,387,332 B) — **known KIT drift, not a defect**:
  the concurrent web-PDF rebuild rewrote all 9 ru web PDFs (KIT §7 Fix 1 note
  already records this; coordinator to reconcile in the KIT-sync wave).
  The web PDF was stable across this whole read (same SHA at start and end),
  8 pages, and its extracted text is byte-identical to the print PDF's
  (SHA `6e4620ae…` for both extractions, 110,893 bytes each).
- The web-PDF check is NOT deferred: the web file was stable and P8 was
  rendered and read visually from the final file.

## The fix under re-proof (L836)

- text.md L836 reads exactly: `150. ✓ Zie de modeltekst in deel H van deze pagina (97 woorden)`
- The printed P8 key 150 reads exactly the same line (verified visually on the
  print render, on the web render, in the print/web text layers, and in the
  P8 SVG via `tools/p8.py extract`: key `✓`, segment
  `✓ Zie de modeltekst in deel H van deze pagina (97 woorden)`).
- The note text is the same as before the fix; only the redundant
  parenthesised key prefix `(Open opdracht, modeltekst hieronder) —` was dropped.
- No other text.md line changed: the L836 change is the only difference vs the
  pre-fix file per the KIT record, and the full text.md read found nothing
  else inconsistent with the print.

## Key verification (programmatic + visual)

- `tools/p8.py extract --p8 svg/p8-test.svg --total 150`: **noted set = 150 of 150**.
- text.md appendix vs printed P8 keys (segment-by-segment comparison of the
  p8.py extraction against the text.md appendix): **150/150 match**.
  The single apparent diff in the raw comparison (Q150) is a parser artifact:
  the extractor's tail sweep appends the page footer
  (`Lucerna RUSSISCH WEEKBLAD VOL.4 … Pagina 8 van 8`) after the last key;
  the Q150 segment itself is byte-identical to text.md L836.
- text.md stems: 130 individually numbered stems + 5 matching groups of 4
  (25–28, 39–42, 57–60, 75–78, 141–144) = 150, contiguous 1–150.
  Per-page counts: P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38 — match KIT.
- Type counts: Meerkeuze 55, Voltooi de zin 54, Woorden koppelen 20 (5 groups),
  Zinnen bouwen 12, Zinsomvorming 4, Vertaling 4, Schrijven 1 — match KIT.
- Model writing text («Моя неделя 16–22 ноября»): 97 whitespace tokens
  (96 excluding the standalone em-dash token) — matches the printed
  “(97 woorden)” under the builder's token convention (run.py: 97).
  The full model text is present on print P8 §H and identical in text.md.
- E-section translation keys 137–140 are in Dutch by design
  (Dinsdag 17 november, Studentendag. / Een pakket moet gevolgd, opgehaald en
  gecontroleerd worden. / Op dinsdag speelt Rusland tegen Venezuela. /
  Fijne Studentendag allemaal!) — as KIT §7 records.

## Page-by-page notes (print PDF, read visually in full)

- **P1 — Первая (lead, round 14).** Masthead, headline, lead article,
  numbers box (8 / 21 / 31 / 20), media box, contents, word of the week
  «чёрная пятница», November-park photo + caption + credit, «СНЕГ БУДЕТ?»
  box, blitz quiz ex. 1–10. All present, no overflow/overlap/clipping.
  Facts consistent: Zenit/Dynamo 31 pts, Spartak 29, Krasnodar/CSKA 26;
  Krasnodar–CSKA 4:2, Lokomotiv–Rubin 0:1; Uzbekistan 12 Nov (result unknown
  at press time, to VOL.5), Venezuela 17 Nov 19:00, Black Friday from 16 Nov,
  round 15 from 20 Nov.
- **P2 — Жизнь (A2).** Students' Day 17 Nov (Prague 1946; Russia's main day
  25 Jan), Ded Moroz's birthday 18 Nov in Veliky Ustyug, holidays-of-the-week
  box (16–22 Nov), «А ВЫ?» letter call, Yuon «Зима. Ростов» painting +
  caption, weather words (оттепель / мокрый снег / ледяной дождь /
  гололедица), ex. 11–28. All present. Q22 key 16:20 matches the article's
  “Солнце садится около 16:20”. No defects.
- **P3 — Культура (A2→B1).** Five premieres 19 Nov (Рокки, Бумажный тигр,
  Увидеть всё, Дедмобиль, Колотун), Hunger Games 26 Nov, «Лиля»/«Лес» from
  12 Nov, ex. 29–46. Gloss fix verified on the render:
  `криминальная crimineel · сказочное sprookjesachtig.` — full words, no
  truncated hyphens. No defects.
- **P4 — Спорт (B1).** Full round-14 results table: all 8 matches present
  (Lokomotiv–Rubin 0:1, Fakel–Dinamo 1:2, Akhmat–Rodina 1:0,
  Krasnodar–CSKA 4:2, Krylya Sovetov–Orenburg 2:0, Spartak–Akron 2:1,
  Zenit–Rostov 2:2, Baltika–Dinamo Mkh 0:1, incl. the 20:45 kickoff);
  top-5 table; VOL.3 correction box (the eighth match) present; national-team
  note (Tashkent 12 Nov, Krasnodar 17 Nov); round-15 fixtures 20–22 Nov
  (8 fixtures); 1912 football photo + caption; ex. 47–64. Table scores agree
  with the article and with the P8 keys (Q52 0:1, Q53 2:2, Q54 2:0, Q55 0:1).
  No defects.
- **P5 — Молодёжь (B1).** Black Friday dates: calendar 27 Nov, Ozon
  13 Nov–2 Dec, Wildberries 16–30 Nov, M.Video from 12 Nov, Yandex Market
  25–27 Nov (provisional), Lamoda 27–30 Nov, Cyber Monday 30 Nov; 11.11
  (22 Oct–12 Nov; 14.4m orders 11 Nov 2025); returns peak 11–30 Nov;
  4–7-day promo codes; market photo + honest caption; dates box; ex. 65–82.
  Dates box agrees with the article and the keys. No defects.
- **P6 — Разбор (B2).** Week-of-16–22-Nov analysis; day strip
  16 пн–20 пт (light) / 21 сб–22 вс (yellow); ЗА/ПРОТИВ box; chart
  (Работа и учёба 38, Покупки и скидки 26, Кино и книги 18, Спорт и прогулки
  18 — sums to 100%, bars proportional); practice-data disclaimer in Russian
  + Dutch; D1 fix verified (`УЧЕБНЫЕ ДАННЫЕ` + `OEFENGEGEVENS`); ex. 83–100.
  No defects.
- **P7 — Язык.** Three level columns (weather / shopping / attribution),
  4-item error clinic (с Днём студента / на «чёрной пятнице» /
  забили 21 гол / с 19 ноября), word box «распродажа», readers' corner with
  the editor's example AND the on-page disclosure in Russian and Dutch
  (`Geen brieven of teksten: voorbeeld van de redactie, beloofd voor VOL.5.`),
  Pushkin portrait + caption, 8 golden sentences with page refs
  (P1×2, P2×1, P3×1, P4×1, P5×1, P6×2) — each verified to occur in its cited
  article (P1: “Все восемь матчей 14-го тура завершены”,
  “Это последний матч сборной в 2026 году”; P2: “Профессиональные праздники
  не дают выходных”; P3: “В ноябре вечера тёмные и долгие”; P4: “После паузы
  чемпионат возвращается 20 ноября”; P5: “Умный покупатель не спешит”;
  P6: “Такие недели — самые частые в году”, “В ноябре 20 рабочих дней
  и 10 выходных”) — VOL.5 teaser; ex. 101–112. No defects.
- **P8 — Тест.** Sections A–H, ex. 113–150, full 150-key answer list, model
  text, footer `Pagina 8 van 8`. Stems spot-checked against text.md
  (Q113–120, Q127–128, Q133–140, Q141–149, H) — all match. No overflow;
  key list runs to Q150 at the bottom of the third column, clear of the footer.
  No defects.

## Dutch (reader language) and Russian source text

- All explanation, glosses, instructions, section furniture and footers read
  in correct Dutch; Russian article text, stems and keys are correct and
  consistent with the numbers/dates in the articles. No tofu, no clipped or
  overlapping text found on any page. No CJK in visible content.

## Observation (NOT a finding)

- **Narrow word spaces at some Cyrillic→Latin and Cyrillic→Cyrillic joins**
  (e.g. P1 «метеорологическаязима», «От редакцииLucerna»,
  «зона вылетаdegradatiezone», P2 «Профессиональныепраздники»,
  «напечатаемв VOL.5», P7 «забили21 гол»). Investigation: the space character
  IS present in the layout — in the P1 SVG the space between
  «метеорологическая» (x=1088.0) and «зима» (x=1316.4) is a separate
  `<text>` element at x=1310.9, a 5.5 px advance, i.e. the normal word-space
  width for that size (body-text spaces measure 5.8–5.9 px; the KIT-ruled
  range is 4–6 px). The ink gap measures ~2 px at 100 dpi only because the
  'я'/'з' glyphs extend to their advance edges — the same systemic
  per-word-`<text>`-element rendering as the whole edition (254 space
  elements with advance < 6.5 px on P1 alone). It is byte-identical in
  core-ru (same SVG coordinates, same pdftotext extraction
  «метеорологическаязима»), i.e. frozen-core rendering, and the same class
  the KIT already rules as normal (“narrow (4–6 px) word spaces … are
  normal, same class as core”). Not flagged: the space exists, its advance
  is in the ruled range, the class is systemic and core-identical, and the
  prior independent re-proof accepted this unchanged print PDF with zero
  findings. Recorded here only so the observation is on the record.

## Notes for the coordinator

- KIT drift to reconcile in the KIT-sync wave: web PDF SHA on disk
  `f317713a…` (3,387,356 B) vs KIT §5 `d3f016d5…` (3,387,332 B).
  Print SHA matches KIT §5. text.md SHA matches the Fix 1 record.
- No production files were modified; no lint run; no commit/push.
  Read-only checks used: `pdftotext`, `pdftoppm` renders (in /tmp, deleted
  after the read), `tools/p8.py extract` (read-only, no --json output).
- Temp renders and extracted text files were deleted after the read.
