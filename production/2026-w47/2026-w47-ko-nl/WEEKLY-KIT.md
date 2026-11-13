# Lucerna Weekly — W47 Korean, Dutch reader (VOL.4) — WEEKLY KIT

- Slug: `2026-w47-ko-nl` (target ko, reader Dutch)
- Issue week: 2026-11-16 (Mon) – 2026-11-22 (Sun), VOL.4
- Press time: **2026-11-10** (inherited from core-ko run 11). No score or event after Nov 10 is claimed; Nov 16–22 events are presented as scheduled. Nov 19-only measures are dated Nov 19 only.
- Format: 8 pages, 1950×2700, 4 columns, 150 exercises, continuous numbering 1–150, every exercise in the registry.
- Fan-out of the finalized ko core (`core-ko`, run 11 (fix1) + textmd fix2): Korean content frozen; only the explanation layer (glosses, box titles, instructions, "And you?" prompts, P7 letters disclosure, P8 answer notes, furniture) is in Dutch. Build interpreter locked to **/usr/bin/python3** (system PIL 10.2.0) — the venv (PIL 13.0.0) measures the same Korean serif strings ~1.1% wider and flips freeze 0/8 vs 8/8 (core fix #15). render.py / webpdf.py still use the venv (cairosvg/fontTools, no PIL metrics).

## Lead topic

CSAT week: D-3 (Mon Nov 16) → advance assembly D-1 (Wed Nov 18) → D-day (Thu Nov 19), then Kimchi Day (Sun Nov 22). Second lead: Samsung's Korean Series title (4–1 over kt wiz, first since 2014). Third lead: kimjang cost down 9.0% to 199,456 won (aT, Nov 9 basis, announced Nov 10).

## Contents by page

- P1 (A2): lead (CSAT week + KS + kimjang cost), numbers box (3 / 1 / 199,456 / 4–1 / 12), calendar Nov 16–22, contents, word of the week 「예비소집」, autumn photo (Hakkoda file photo, honestly captioned), quiz 7–10.
- P2 (A2): kimjang cost feature, Kimchi Day box, History exam sign-up box (81st, Sat Nov 28, advanced only, 27,000 won), 김장 나눔, 겨울 밥상, shopping list, ssam photo, D-day strip (D-3/D-1/D-데이/김치의 날), ex. 11–28.
- P3 (A2→B1): Kimchi Day + late-foliage wrap-up (forecast vs observation; no observed Naejangsan peak announced at press time — readers sent to Weather Nuri 날씨누리), bukhansan-ui + Cézanne apples photos, ex. 29–46.
- P4 (B1): full Korean Series result (G1–G5 scores, venues, 4 straight wins after 1 loss, 9th title), postseason ladder (wildcard LG 4–1 Doosan, semi-playoff KIA 3–0 LG, playoff Samsung 3–2 KIA), K League box (FC Seoul early champions 33R, 36R Nov 21–22, finals Dec 5–6), ex. 47–64.
- P5 (B1): CSAT week, advance assembly (times/places vary by school), Nov 19-only measures, 수능이 끝나면, Kimchi Day youth ideas (WiKim youth session), 시험 전날의 하루, study photo, ex. 65–82.
- P6 (B2): 「예보에서 결과로」 — forecast→result theme; comparison table (last week vs this week: KS schedule→result Samsung 4–1; foliage forecast dates→passed; kimjang cost Oct 16 price→Nov 9 survey 199,456 won), ex. 83–100.
- P7 (A2→B2): A2 김치의 날의 말, B1 날짜 세는 말 (D-3/D-1/D-데이), B2 예보와 결과 읽는 법; error clinic (김치의날 spacing; 삼성는→삼성은; 담궈요→담가요; 날예요→날이에요); frame 「〜 후에」; readers' corner (editor's example letter + single Dutch disclosure; promise carried to **VOL.5**); P7 photo strip (kimchi-making, Anattadairy CC0); 8 P7 phrases, all verbatim from this issue's own articles; VOL.5 preview (HanNeungGeom Sat Nov 28, post-CSAT stories, Kimchi Day follow-up, letters/best P8 writing). Ex. 101–112.
- P8 (全部): 38 items — A 연표 8, B 일반 8, C mini-reading 4 (test character 민준이/Minjun, 수험생 story), D 造句 4, E 翻译 4 (stems 137/138 in Korean, keys stay Korean; stems 139/140 in Dutch, keys stay Korean), F 词汇配对 4, G dialogue 完形 5, H writing 1 「나의 김치의 날」 (model 169 chars, in 150–200). P8 photo (kimchi-making2, Anattadairy CC0) in col 4 below the H model. Full printed answers 1–150 with one-line Dutch notes.

## Measured exercise counts (final build, run 2 — fan-out #3, new edition from core run 11)

- TOTAL **150**; by page 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38
- By level A2 51 / B1 72 / B2 27
- By type: Invullen 48, Meerkeuze 52, Combineren 16, Omzetten 4, Zinnen bouwen 8, Juist of onjuist 4, Gatentekst 13, Vertalen 4, Schrijven 1
- Model chars (H writing): 169
- No FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build (run 1 overflowed — see Fixes log #1; run 2 is the shipped build).
- **P8 answer font size (measured with PyMuPDF on the final print PDF): min 9.975 pt** (172 spans in the P8 answers region y≥1302/2700, 167 at 9.975pt) — above the SOP §1.1 threshold of 9.75 pt.
- Level badges ("chips"): 138 total, 35 on P8.

## Trend / fact sources

All facts inherited from core-ko run 11, whose KIT documents them with attribution caveats (Korean Series 4–1; Kimchi Day Nov 22; kimjang cost 199,456 won; CSAT Nov 19, 551,864 candidates; foliage forecasts incl. Weatheri Naejangsan Nov 11; fire-precaution period Nov 1–Dec 15; K League FC Seoul champions; HanNeungGeom 81st Nov 28; Hankook Tire kimjang sharing). Nothing after Nov 10 is claimed. No new facts were introduced by this fan-out; Dutch renderings only.

## Images (same 8 as core, all verified public-domain/CC0)

| File | Page | Author | Licence |
|---|---|---|---|
| autumn.jpg | P1 | lumoplank | CC0 |
| ssam.jpg | P2 | wizdata | CC0 |
| bukhansan-ui.jpg | P3 | Udonhan1992 | CC0 |
| apples.jpg | P3 | Paul Cézanne | Public domain |
| baseball.jpg | P4 | Bain News Service | Public domain |
| study.jpg | P5 | Gary Todd | CC0 |
| kimchi-making.jpg | P7 | Anattadairy | CC0 |
| kimchi-making2.jpg | P8 | Anattadairy | CC0 |

Full Commons page URLs and caption honesty notes in core-ko `assets/CREDITS.md`.

## Fan-out mechanism

- Core copied verbatim, then a translation map (`map-nl.json`, 216 keys + 8 instr, generated by `gen-map-nl.py` — generated from `gen-map-en.py` via `mk-lang.py nl` with `nl-replace.json` (en-value→Dutch-value) + `nl-meta.json`) applied by exact quoted-literal replacement, longest first, plus asserted structural edits (`apply-ko.py`).
- `svglib.py` copied verbatim, fonts frozen (md5 `1c94d836d46fcf6fc67e88b0f0febd34`, same as core).
- **Map-source discipline (learned on the it build, applied here):** the map values live in `gen-map-nl.py`'s embedded MAP dict — editing `nl-replace.json` alone does not change `map-nl.json`; `mk-lang.py nl` must regenerate the gen-map script first, then `gen-map-nl.py`, then re-apply. (The P2 gloss shortening went through exactly this chain.)
- Gloss prefix `Uitleg — `; footer `Lucerna　KOREAANS WEEKBLAD VOL.4　Teksten in het Koreaans　Uitleg in het Nederlands`; page line `Pagina {n} van {total}`.
- P7 letters: single Dutch disclosure replaces `lcn`; `lko` and `lcn2` lines + their render lines removed; `lh` formula rebuilt for 2 blocks (W46 ko-en precedent). Disclosure is 281 chars (8 lines in the probe).
- P8 E-group re-aiming (W46 ko-en precedent): keys 137/138 translated to Dutch; stems 139/140 translated, keys stay Korean → `p8.py compare` keydiff `[137, 138]`, status CLEAN.
- P8 page separator `— 제{pg}면 —` stays frozen. H writing note is an f-string (structural edit: `Modeltekst in deel H op deze pagina ({NCHARS} tekens)`); H key is a plain map entry (`(open opdracht — modeltekst hieronder)`).
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style `n. key — note`, satisfied by construction.
- Straight apostrophe U+0027 only; U+2019 scan across all 8 SVGs = 0. Frame line uses 「」 (see Fixes log #2 — the map already carries the 「」 form, no post-apply fix needed).
- P8 answer-note person names checked one by one: the only personal name is 민준 (Minjun, #129 "Minjun gaat woensdag naar de voorbereidende bijeenkomst", #135 note) — standard Revised Romanization, consistent within the edition; team/company names (Samsung, kt wiz, KIA, LG, FC Seoul, Weatheri, KBO) match core's own renderings. The ja-family sumo-romaji defect class does not apply here.
- Dutch renderings follow the W46 ko-nl precedent where noted: CSAT kept; Kimchidag; kimjang kept; voorbereidende bijeenkomst (예비소집); examen geschiedenis (한능검); Bosdienst (Forestry Service); Weatheri kept; Dutch dates `16 nov.` / `22 nov.`; Dutch numbers `54.980 won` / `26,5 %`; score `4-1`. Type names: Invullen / Meerkeuze / Combineren / Omzetten / Zinnen bouwen / Juist of onjuist / Gatentekst / Vertalen / Schrijven. Instr: Invullen / Herschrijven / Zinnen bouwen / Vertalen / Schrijven / Woorden en toelichting / Berg en toelichting / Woord en betekenis.
- Probe-phase shortenings (P8/P7 headroom, all in the map): P7 clinic notes shortened to 1 line each ([169]/[171] → `Na een slotmedeklinker: 「은」.` / `「이에요」.`; [170] → `Nu: 「담그다」 → 「담가요」.`); disclosure shortened to 281 chars; P8 [120]/[121] shortened (`Bewijs ophalen bij de voorbereidende bijeenkomst` / `Bewijs ophalen, examenlocatie controleren`). Probe after the shortenings: P8 end 2486.6 (headroom 53.4, overflows 0), P7 teaser_end 2512.7 (margin 67.3).

## Self-proofread record (full pass over rendered pages + extracted SVG text + text.md)

- **Run 1 (fan-out #3, 2026-11-11):** build overflowed — P2-feature FLOW OVERFLOW (col 2 y=1930 vs bottom 1540, need 390); the `Boodschappen` box was clamped past the frame and overlapped the D-day strip. Discarded; see Fixes log #1.
- **Run 2 (fan-out #3, 2026-11-11, shipped):** build clean (0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150); P2-feature ends 1531, P8-keys ends 2487, P7 teaser 2512.7. boxtitle 8/8. All gates pass (see Mechanical gates). Full visual read of all 8 print pages at 100dpi: zero issues (P1 `Alles` in contents, quiz #10 new sentence; P2 `Boodschappen` box fully inside the feature area, g2 gloss 2 lines, D-day strip clean; P7 Pattern box `Kader: 「na ~」`, phrase #7 new sentence + (1면), Dutch clinic/disclosure; P8 F header `Woord en betekenis`, E 137/138 Dutch stems, H model text correct). Full self-read of `2026-w47-ko-nl.text.md` (449 items): zero issues. All 150 keys re-derived (keycheck 150/150; #150 `✓` expected, identical in core).
- **Independent proofread:** not yet done — to be assigned by the coordinator (proof1 for this edition, separate person). This KIT records the builder's self-check only.

## Fixes log

| # | Found | Fix | Round |
|---|---|---|---|
| 1 | P2-feature FLOW OVERFLOW after apply round 1: flow ended col 2 y=1930 vs bottom 1540 (need 390). The Dutch P2 gloss #2 wrapped to 3 lines vs en's 2 (+29.7px at the 386.5px gloss-box inner width); the shift pushed the 390px `Boodschappen` box past the 361px left in col 2, so `_fit` clamped it past the frame, overlapping the D-day strip | Shortened in the map source (`nl-replace.json`: `geregistreerd worden` → `geregistreerd`), then `mk-lang.py nl` + `gen-map-nl.py` + re-apply; g2 measures 2 lines, P2-feature ends 1531 (same as en, 9px margin), 0 FLOW OVERFLOW. The probe suite does not simulate the P2-feature flow — this defect class is only caught by run.py's own overflow line | run 1 → run 2 |
| 2 | Frame line: no defect — the map already carries the 「」 form (`Kader: 「na ~」. Vraag: 「〜 후에 뭐 해요?」`) | None needed; post-build sweep U+201C = 0, U+201D = 0, U+2019 = 0 across all 8 SVGs + text.md; the 「」 form is visible in the P7 render and in text.md line 761 | run 2 |
| 3 | Independent reproof (2026-11-12): 6 exact-duplicate exercise slots (Q12/Q13/Q22/Q47/Q74/Q102), P1 lead sentence missing "다른 날의", P7 quote 6 translated as imperative | Q12/Q13/Q22/Q47/Q74/Q102 replaced with new questions from same-page article facts (P2 kimjang cost 13.4% below average, 6 kimjang ingredient types, chili powder -1.8%, P4 Samsung 9th title, P5 exam ticket by 8 a.m., P7 Kimchi Day fixed by law Feb 2020); P8 keys + reader notes updated; P1 sentence → "이번 주의 다른 날의 조치가 아니에요"; P7 quote 6 → past tense "De krant vermeldde de uitslagen met de scores.". Rebuilt + re-gated: TOTAL 150, p8 CLEAN, occlusion 0, spill/boxtitle/edge 0, textlayer PASS, text.md 455 items | fix rebuild 2026-11-12 |
| 4 | Independent reproof round 2 (2026-11-12, PROOF-NOTE-2): R2-1 text.md export drops 7 numbered items (P2 D Q26, P4 D Q61–Q63, P8 B Q121/Q126, P8 F Q142) | R2-1: `textmd.py` global `seen` dedup replaced by per-call-site retention for `.ex`/`.match_set` items (plain prose keeps global dedup); text.md re-exported, 8 items restored per edition (7 numbered + P6 table row label `김장비용`, same root cause, verified against the print P6 table); per-page inventory 150/150, match terms 16/16 standalone, whole-book 150/150; PDFs untouched (print/web SHA unchanged); p8 compare CLEAN (keydiff [137, 138]), D5 census PASS (0/0/0, curly 0) | fix rebuild 2, 2026-11-12 |

## Adjudicated (not defects)

- P8 match-item notes end with the option letter repeated: the letter is in the source note literal itself, core's own convention.
- #43/#123/#124 notes "Weatheri-voorspelling" / "Bosdienst voorspelt piek" / "Weatheri voorspelt piek": core's own renderings of the Weatheri (private weather company) and Forestry Service (산림청) forecasts — not typos.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "(open opdracht — modeltekst hieronder)" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (nl): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure).
- text.md 449 items vs core 452: three accounted drops, no content gap — (1) `is_prose` drops the bare Latin word "Alles" (P1 contents 8면 row level; the SVG/PDF render "Alles" correctly, visible on the P1 render); (2) `lcn2` removed by design; (3) `lko` removed by design. Same pattern as en/de/es/fr/it/pt.
- Repeated page citations (1면/2면/4면/6면) appear once in text.md: textmd.py dedupes repeated citation strings — the rendered P7 phrases carry the full per-phrase citations (check_core phrases 8/8 verbatim).
- Freeze diff added CJK 7, all U+3000 (ideographic space, footer): same pattern as de-family Latin editions.
- P8 answer-note stem 10.35pt is the recorded core adjudication — not a defect, not changed.
- `text.md` contains `___` (75 places) — exported from the source literals, where blanks stay as `___`; the SVG/PDF render them as 1.1pt ink underlines. Same as core.

## Occlusion audit

- `tools/occlusion_audit.py` on `svg/`: **0 flags**. Selftest first: planted classes fired {BOXTITLE: 1, COVER: 1, EDGE: 1, FOOTER: 1, LINEX: 1, TEXTX: 1}; clean controls silent. Log at `hidden_files/w47/scratch-fanout-ko3/nl/occlusion-nl.log` (json `occlusion-nl.json`).

## Mechanical gates (final state, run 2)

- `run.py` (build run 2, `/usr/bin/python3`): exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150 (A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2487, P7 teaser 2512.7). Log `hidden_files/w47/scratch-fanout-ko3/nl/build-nl-run2.log`; SVG hashes `nl/sha-nl-run2.txt`. (Run 1 log `nl/build-nl-run1.log` kept as evidence of the overflow fix.)
- `tools/freeze.py baseline` (**/usr/bin/python3**): **8/8 SVGs byte-identical**, tool self-reports 8/8 with per-file OK rows. Log `hidden_files/w47/scratch-fanout-ko3/nl/freeze-nl.log`; rebuild products deleted after the pass (log + json kept).
- `tools/freeze.py diff` (core-ko svg vs edition svg): TOTAL added CJK characters 7, all U+3000 (see Adjudicated). Log `nl/freeze-diff-nl.log`.
- `tools/p8.py extract` on `svg/p8-siheom.svg`: **noted set = 150 of 150** (parse: lines). Log `nl/p8-extract-nl.log`, json `nl/p8-nl.json`. `compare` vs core P8: **CLEAN** (missing=[] extra_count=0 keydiff=[137, 138]). Log `nl/p8-compare-nl.log`.
- `check_core.py` / `check_gloss.py` (scratch copies with ED + gloss prefix patched to the edition): **gloss fails 0, orphan issues 0**, phrases 8/8 verbatim (incl. the new phrase #7 with (1면)); dates all correct. Log `nl/check-nl.log`.
- Text layers: print and web PDFs each extract to **51,630 bytes, byte-identical** (`cmp` rc 0). Extracts `nl/print-nl.txt`, `nl/web-nl.txt`; empty diff `nl/textlayer-diff-nl.txt`.
- P8 min font 9.975pt (PyMuPDF on the print PDF, P8 answers region y≥1302/2700: 172 spans, 167 at 9.975pt), ≥ 9.75pt. Log `nl/p8font-nl.log`.
- 150-key check (`keycheck-ko.py`, REG from edition sources vs keys extracted from P8 SVG): 149 exact + #150 `✓` (expected) = **150/150**. Log `nl/keycheck-nl.log`; full table in `nl/EDITION-RECORD.md`.
- §1.1 grep audit: paper `#fbfaf6` 1×/page (P4/P6 4×, same as core — colour also used in table cells), VOL.4 correct on all pages, VOL.5 0 except P7 (2, by design), `·` counts identical to core page-by-page and only in gloss/option/credit contexts, colour set identical to core page-by-page. Log `nl/style11-nl.log`.
- Census (`census.py`, ex/match stems + D6 segments vs text.md): ex/match 166 items, 0 missing; D6 0 missing. Log `nl/census-nl.log`.
- Visual read: all 8 print pages at 100dpi, zero issues. PNGs in `hidden_files/w47/scratch-fanout-ko3/nl/pages/`.

## Output files + sizes (final render, run 2)

- Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ko-nl/`
- Print PDF: `Lucerna-VOL4-KO-NL.pdf` — **43,748,187 bytes**, 8 pages, SHA-256 `662eb3e3e3f20b337d9b0dc7397e5f72dadf5f6c533a16d5ed0f6436d7c25f8c` (fix rebuild 2026-11-12; D5 value was 43,747,058 bytes / `770e3c23dce4…`)
- Web PDF: `Lucerna-VOL4-KO-NL-web.pdf` — **3,950,671 bytes** (< 7 MB), 8 pages, SHA-256 `5f84566e41ded4b03c2b40ff7c6596c1251db61b82f6c82586e191580b6e279b` (fix rebuild 2026-11-12; D5 value was 3,947,564 bytes / `f0b06c75ca26…`); pdftotext **51,672 bytes, byte-identical to the print PDF**.
- Text export: `2026-w47-ko-nl.text.md` — 35,904 bytes, 8 pages, 463 items, SHA-256 `55abafb3fee843b26e69f67b61bb30973a61b3fc9c128e7951a2d9d2b53ccc4d` (exported from source via the fixed `textmd.py` (md5 `00d8f52d96ecad396cbc03603d98fa9b`), never from PDF; re-exported 2026-11-12 (fix round 2, R2-1: textmd.py dedup fix, 8 items restored, 455→463 items)).
- `ABSTRACT.txt`: 339 bytes, SHA-256 `804a1ec11dc87f4ee3fa66329601e42f4cb14c512aa1a8e61d65b6ab74e1bf6d`. `Lucerna Korean Weekly VOL.4: de CSAT-aftelling op D-3, het examen op 19 november, Kimchidag op 22 november met kimjangkosten van 199.456 won, Samsungs eerste Korean Series-titel in 12 jaar, plus inschrijving voor het examen geschiedenis en late herfstbladeren — Koreaanse tekst met Nederlandse uitleg, niveaus A2 tot B2, 150 oefeningen.`
- `WEEKLY-KIT.md`: this file. Build records: `hidden_files/w47/scratch-fanout-ko3/nl/EDITION-RECORD.md`.

## Open verification debts (carried to the parent line)

- Independent proofread of this edition not yet done — to be assigned by the coordinator (proof1, separate person from the builder).
- Fact debts inherited from core-ko (see core KIT): no observed Naejangsan/Wolchulsan foliage peak announced at Nov 10 press time; HanNeungGeom details (other than date/time/fee) from secondaries; K League 35R scores not verified — not cited; WiKim Festival 2026 time/theme/session not found in an independent source (printed as scheduled).

## D5 rebuild (2026-11-12, SOP §1.1)

- Template: `mechanism/svglib-ko-d5.py` installed as edition `svglib.py` (`_D5_READER = "latin"`, reader nl; diff vs template: 0 lines). Old svglib kept as `svglib.pre-d5` in the edition dir and in `hidden_files/w47/scratch-d5-ko/2026-w47-ko-nl/pre/`.
- Build: `tools/venv/bin/python` throughout. `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE. Base-venv control (old svglib + venv) TOTAL 150 with the known P2 FLOW OVERFLOW warning (core content, also present pre-D5).
- Gates (all in `hidden_files/w47/scratch-d5-ko/2026-w47-ko-nl/`): D5 census PASS (Latin 0 / Cyrillic 0 / curly-in-CJK 0; production baseline was 408 Latin); `census_quotes.py` 0 defective glyphs; `head_check.py` PASS 0 defects; `occlusion_audit.py` 0 flags; `p8.py extract` 150/150, `compare` vs core-ko CLEAN (keydiff=[137, 138], expected reader-language keys); `spill_sweep.py` 0 SPILL (357 OBSERVE); `boxtitle_check.py` 0 DEFECT (73 titles, 965 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` 0 absolute defects (ratios n=398 median 1.007 boldT 1.040 boldF 0.990; P8 245→233 lines, slack 73.8→74.8px); text layer print/web char-multiset diff 0 (23,503 = 23,503, pdftotext 51,471 bytes byte-identical).
- `freeze.py` (system python3 Pillow 10.2.0, coordinator-approved one-off exception): `diff` patched vs base-venv RC=0, added CJK 0 (Latin strings +592 from run splitting, expected). `baseline` 7/8 (P2–P8 OK; P1 differs): adjudicated interpreter artefact, same as core-ko — P1 text multiset identical (0 diff, verified by direct SVG text comparison, 1115 runs each); only the big display "1" (185 vs 183pt) + knock-on x shifts (31 elements, 0 text-content diffs). Production (venv, canonical) is self-consistent.
- No content files changed. No true D5 defects in this edition.
