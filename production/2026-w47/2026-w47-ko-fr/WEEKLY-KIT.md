# Lucerna Weekly — W47 Korean, French reader (VOL.4) — WEEKLY KIT

- Slug: `2026-w47-ko-fr` (target ko, reader French)
- Issue week: 2026-11-16 (Mon) – 2026-11-22 (Sun), VOL.4
- Press time: **2026-11-10** (inherited from core-ko run 11). No score or event after Nov 10 is claimed; Nov 16–22 events are presented as scheduled. Nov 19-only measures are dated Nov 19 only.
- Format: 8 pages, 1950×2700, 4 columns, 150 exercises, continuous numbering 1–150, every exercise in the registry.
- Fan-out of the finalized ko core (`core-ko`, run 11 (fix1) + textmd fix2): Korean content frozen; only the explanation layer (glosses, box titles, instructions, "And you?" prompts, P7 letters disclosure, P8 answer notes, furniture) is in French. Build interpreter locked to **/usr/bin/python3** (system PIL 10.2.0) — the venv (PIL 13.0.0) measures the same Korean serif strings ~1.1% wider and flips freeze 0/8 vs 8/8 (core fix #15). render.py / webpdf.py still use the venv (cairosvg/fontTools, no PIL metrics).
- **Note on this KIT file:** the original KIT (fan-out #2) was backed up to ko3 scratch (`fr/ko-fr-WEEKLY-KIT-pre-ko3.md`, SHA `329c7a0b…`) before the ko3 apply wiped the edition directory (the apply does a full `rmtree` and does not preserve the KIT); this file is that backup restored plus the ko3 rebuild sections below.

## Lead topic

CSAT week: D-3 (Mon Nov 16) → advance assembly D-1 (Wed Nov 18) → D-day (Thu Nov 19), then Kimchi Day (Sun Nov 22). Second lead: Samsung's Korean Series title (4–1 over kt wiz, first since 2014). Third lead: kimjang cost down 9.0% to 199,456 won (aT, Nov 9 basis, announced Nov 10).

## Contents by page

- P1 (A2): lead (CSAT week + KS + kimjang cost), numbers box (3 / 1 / 199,456 / 4–1 / 12), calendar Nov 16–22, contents, word of the week 「예비소집」, autumn photo (Hakkoda file photo, honestly captioned), quiz 7–10.
- P2 (A2): kimjang cost feature, Kimchi Day box, History exam sign-up box (81st, Sat Nov 28, advanced only, 27,000 won), 김장 나눔, 겨울 밥상, shopping list, ssam photo, D-day strip (D-3/D-1/D-데이/김치의 날), ex. 11–28.
- P3 (A2→B1): Kimchi Day + late-foliage wrap-up (forecast vs observation; no observed Naejangsan peak announced at press time — readers sent to Weather Nuri 날씨누리), bukhansan-ui + Cézanne apples photos, ex. 29–46.
- P4 (B1): full Korean Series result (G1–G5 scores, venues, 4 straight wins after 1 loss, 9th title), postseason ladder (wildcard LG 4–1 Doosan, semi-playoff KIA 3–0 LG, playoff Samsung 3–2 KIA), K League box (FC Seoul early champions 33R, 36R Nov 21–22, finals Dec 5–6), ex. 47–64.
- P5 (B1): CSAT week, advance assembly (times/places vary by school), Nov 19-only measures, 수능이 끝나면, Kimchi Day youth ideas (WiKim youth session), 시험 전날의 하루, study photo, ex. 65–82.
- P6 (B2): 「예보에서 결과로」 — forecast→result theme; comparison table (last week vs this week: KS schedule→result Samsung 4–1; foliage forecast dates→passed; kimjang cost Oct 16 price→Nov 9 survey 199,456 won), ex. 83–100.
- P7 (A2→B2): A2 김치의 날의 말, B1 날짜 세는 말 (D-3/D-1/D-데이), B2 예보와 결과 읽는 법; error clinic (김치의날 spacing; 삼성는→삼성은; 담궈요→담가요; 날예요→날이에요); frame 「〜 후에」; readers' corner (editor's example letter + single French disclosure; promise carried to **VOL.5**); P7 photo strip (kimchi-making, Anattadairy CC0); 8 P7 phrases, all verbatim from this issue's own articles; VOL.5 preview (HanNeungGeom Sat Nov 28, post-CSAT stories, Kimchi Day follow-up, letters/best P8 writing). Ex. 101–112.
- P8 (全部): 38 items — A 연표 8, B 일반 8, C mini-reading 4 (test character 민준이/Minjun, 수험생 story), D 造句 4, E 翻译 4 (stems 137/138 in French, keys stay Korean; stems 139/140 in French, keys stay Korean), F 词汇配对 4, G dialogue 完形 5, H writing 1 「나의 김치의 날」 (model 169 chars, in 150–200). P8 photo (kimchi-making2, Anattadairy CC0) in col 4 below the H model. Full printed answers 1–150 with one-line French notes.

## Measured exercise counts (final build, run 1 — fan-out #3 rebuild from core run 11)

- TOTAL **150**; by page 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38
- By level A2 51 / B1 72 / B2 27
- By type: Compléter 48, Choix multiple 52, Apparier 16, Transformer 4, Faire des phrases 8, Vrai ou faux 4, Texte à trous 13, Traduire 4, Écrire 1
- Model chars (H writing): 169
- No FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build.
- **P8 answer font size (measured with PyMuPDF on the final print PDF): min 9.975 pt** (170 spans in the P8 answers region y≥1302/2700, 165 at 9.975pt) — above the SOP §1.1 threshold of 9.75 pt.
- Level badges ("chips"): 138 total, 35 on P8.

## Trend / fact sources

All facts inherited from core-ko run 11, whose KIT documents them with attribution caveats (Korean Series 4–1; Kimchi Day Nov 22; kimjang cost 199,456 won; CSAT Nov 19, 551,864 candidates; foliage forecasts incl. Weatheri Naejangsan Nov 11; fire-precaution period Nov 1–Dec 15; K League FC Seoul champions; HanNeungGeom 81st Nov 28; Hankook Tire kimjang sharing). Nothing after Nov 10 is claimed. No new facts were introduced by this fan-out; French renderings only.

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

- Core copied verbatim, then a translation map (`map-fr.json`, 216 keys + 8 instr, generated by `gen-map-fr.py` — itself derived from `gen-map-en.py` via the generic `mk-lang.py` + `fr-replace.json` / `fr-meta.json`) applied by exact quoted-literal replacement, longest first, plus asserted structural edits (`apply-ko.py`).
- `svglib.py` copied verbatim, fonts frozen (md5 `1c94d836d46fcf6fc67e88b0f0febd34`, same as core).
- Gloss prefix `Note — `; footer `Lucerna　HEBDOMADAIRE CORÉEN VOL.4　Texte coréen　Explications en français`; page line `Page {n} sur {total}`.
- P7 letters: single French disclosure replaces `lcn`; `lko` and `lcn2` lines + their render lines removed; `lh` formula rebuilt for 2 blocks (W46 ko-fr precedent).
- P8 E-group re-aiming (W46 ko-fr precedent): keys 137/138 translated to French; stems 139/140 translated, keys stay Korean → `p8.py compare` keydiff `[137, 138]`, status CLEAN.
- P8 page separator `— 제{pg}면 —` stays frozen. H writing note is an f-string (structural edit: `Texte modèle dans la partie H de cette page ({NCHARS} caractères)`); H key is a plain map entry (`(tâche libre — texte modèle ci-dessous)`).
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style `n. key — note`, satisfied by construction.
- Straight apostrophe U+0027 only (no U+2019 anywhere in French values); U+2019 scan across all 8 SVGs = 0.
- P8 answer-note person names checked one by one: the only personal name is 민준 (Minjun, #129 "Minjun va à la convocation préalable mercredi", #135 note) — standard Revised Romanization, consistent within the edition; team/company names (Samsung, kt wiz, KIA, LG, FC Seoul, Weatheri, KBO) match core's own renderings. The ja-family sumo-romaji defect class does not apply here.
- French renderings (W46 ko-fr precedent where noted): CSAT kept; Jour du kimchi; kimjang; convocation préalable (예비소집); examen d'histoire (한능검); Office des forêts (Forestry Service); Weatheri kept; French dates `18 nov.`; French numbers `199 456 wons` / `9,0 %`; score `4-1`; D-1/D-3/D-day kept as the taught terms from the Korean text. Type names: Compléter / Choix multiple / Associer les mots aux notes / Transformer / Vrai ou faux / Texte à trous / Faire des phrases / Traduire / Écrire. Instr: Compléter / Reformuler / Faire des phrases / Traduire / Écrire / Associer les mots aux notes / Associer la montagne à sa note / Associer le mot à son sens.

## Self-proofread record (full pass over rendered pages + extracted SVG text + text.md)

- **Probe (pre-build):** P8-keys sim end col 3 y=2426.5 (headroom 113.5, 0 overflows, 7 two-line entries); P7 sim col3 ends 1768.2, teaser 2510.2, disclosure 7 lines; P2/P3/P5 "And you?" boxes end 1227.0 / 1537.7 / 853.0, all inside limits. Log `hidden_files/w47/scratch-fanout-ko/fr/probe-fr.log`.
- **Apply round 1:** OK, but `boxtitle-ko.py` 7/8 — P7 frame title `이번 주의 틀　Structure de la semaine` 406.8px > 386.5px inner width. Fix: shortened to `La structure` (275.9px). Re-applied (round 2); boxtitle 8/8. No render was running during the re-apply.
- **Run 1 (fan-out #3 rebuild, 2026-11-11):** build clean (0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150); P2-feature ends 1531, P8-keys ends 2426, P7 teaser 2510.22. boxtitle 8/8 (no shortening needed — the #2 shortening is in the map). All gates pass (see Mechanical gates). Full visual read of all 8 print pages at 100dpi: zero issues. Full self-read of `2026-w47-ko-fr.text.md` (449 items): zero issues. All 150 keys re-derived (keycheck 150/150; #150 `✓` expected, identical in core). SVG change footprint vs #2 run 1: **exactly P1/P4/P7 changed** (the core D2/D3/D4 fixes + the Frame 「」 fix); P2/P3/P5/P6/P8 byte-identical — the old fr was built from the pre-08:40 core (run 10) and was stale on p1/p4/p7; this rebuild brings it to the finalized core.
- **Independent proofread:** not yet done — to be assigned by the coordinator (proof1 for this edition, separate person). This KIT records the builder's self-check only.

## Fixes log

| # | Found | Fix | Round |
|---|---|---|---|
| 1 | boxtitle check after apply round 1: P7 frame title `Structure de la semaine` 406.8px over the 386.5px inner width | Shortened to `La structure` (275.9px); re-applied, boxtitle 8/8 before the build | #2, 2 (apply) |
| 2 | `p8.py compare` first call failed (arg error: compare needs `--total`) | Re-ran with `--total 150` → CLEAN, keydiff `[137, 138]` | #2 |
| 3 | ko3: the map reproduces curly double quotes U+201C/U+201D in `content7.py:81` (`Cadre : “après ~”. Demandez : “〜 후에 뭐 해요?”`) — the on-disk #2 P7 SVG carried the same defect | Re-applied the core-style 「」 form `Cadre : 「après ~」. Demandez : 「〜 후에 뭐 해요?」` post-apply, before building. Post-build sweep: U+201C = 0, U+201D = 0, U+2019 = 0 across all 8 SVGs + text.md; the 「」 form is visible in the P7 render and in text.md line 761 | ko3 run 1 |
| 4 | ko3: the #2 fr was built from the PRE-08:40 core (run 10) — stale on p1/p4/p7 | Rebuilt from the finalized core run 11: P1 quiz #10 `어느 팀이에요`, P4 #47 `어느 팀이에요` + #48 without the duplicated `시리즈`, P7 frame example + phrase #7 now the new sentence `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요` (1면). Verified in the renders and in check_core phrases 8/8 verbatim | ko3 run 1 |
| 5 | Independent reproof (2026-11-12): 6 exact-duplicate exercise slots (Q12/Q13/Q22/Q47/Q74/Q102), P1 lead sentence missing "다른 날의", P7 quote 6 translated as imperative | Q12/Q13/Q22/Q47/Q74/Q102 replaced with new questions from same-page article facts (P2 kimjang cost 13.4% below average, 6 kimjang ingredient types, chili powder -1.8%, P4 Samsung 9th title, P5 exam ticket by 8 a.m., P7 Kimchi Day fixed by law Feb 2020); P8 keys + reader notes updated; P1 sentence → "이번 주의 다른 날의 조치가 아니에요"; P7 quote 6 → past tense "Il a rapporté les résultats avec les scores.". Rebuilt + re-gated: TOTAL 150, p8 CLEAN, occlusion 0, spill/boxtitle/edge 0, textlayer PASS, text.md 455 items | fix rebuild 2026-11-12 |
| 6 | Independent reproof round 2 (2026-11-12, PROOF-NOTE-2): R2-1 text.md export drops 7 numbered items (P2 D Q26, P4 D Q61–Q63, P8 B Q121/Q126, P8 F Q142) | R2-1: `textmd.py` global `seen` dedup replaced by per-call-site retention for `.ex`/`.match_set` items (plain prose keeps global dedup); text.md re-exported, 8 items restored per edition (7 numbered + P6 table row label `김장비용`, same root cause, verified against the print P6 table); per-page inventory 150/150, match terms 16/16 standalone, whole-book 150/150; PDFs untouched (print/web SHA unchanged); p8 compare CLEAN (keydiff [137, 138]), D5 census PASS (0/0/0, curly 0) | fix rebuild 2, 2026-11-12 |

## Adjudicated (not defects)

- P8 match-item notes end with the option letter repeated (`25. d — … 199 456 wons d`): the letter is in the source note literal itself, core's own convention (`김장비용=四口之家199,456韩元 d` in core-ko); the fr map translated the note text and kept the letter.
- #43/#123/#124 note "prévisions Weatheri": core's own rendering of 웨더아이 (private weather company, corrected in core run 4) — not a typo.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "(tâche libre — texte modèle ci-dessous)" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (fr): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure).
- text.md 449 items vs core 452: three accounted drops, no content gap — (1) `is_prose` drops the bare 3-letter Latin word "Tout" (P1 contents 8면 row level; the SVG/PDF render "Tout" correctly, visible on the P1 render); (2) `lcn2` removed by design; (3) `lko` removed by design. Same pattern as en/de/es. (The #2 KIT recorded 332 vs 333 under the old textmd.py; the fixed re-export is 449 vs 452.)
- Freeze diff added CJK 7, all U+3000 (ideographic space, footer): same pattern as de-family Latin editions.
- P8 answer-note stem 10.35pt is the recorded core adjudication — not a defect, not changed.
- `text.md` contains `___` (23 places) — exported from the source literals, where blanks stay as `___`; the SVG/PDF render them as 1.1pt ink underlines. Same as core.

## Occlusion audit

- `tools/occlusion_audit.py` on `svg/` (ko3 run 1): **0 flags**. Selftest first: planted classes fired {BOXTITLE: 1, COVER: 1, EDGE: 1, FOOTER: 1, LINEX: 1, TEXTX: 1}; clean controls silent. Log at `hidden_files/w47/scratch-fanout-ko3/fr/occlusion-fr.log` (json `occlusion-fr.json`).

## Mechanical gates (final state, ko3 run 1)

- `run.py` (build run 1, `/usr/bin/python3`): exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150 (A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2426, P7 teaser 2510.22). Log `hidden_files/w47/scratch-fanout-ko3/fr/build-fr-run1.log`; SVG hashes `fr/sha-fr-run1.txt` (exactly P1/P4/P7 changed vs #2 run 1 — the core D2/D3/D4 fixes + the Frame 「」 fix; the other 5 SVGs byte-identical).
- `tools/freeze.py baseline` (**/usr/bin/python3**): **8/8 SVGs byte-identical**, tool self-reports 8/8 with per-file OK rows. Log `hidden_files/w47/scratch-fanout-ko3/fr/freeze-fr.log`; rebuild products deleted after the pass (log + json kept).
- `tools/freeze.py diff` (core-ko svg vs edition svg): TOTAL added CJK characters 7, all U+3000 (see Adjudicated). Log `fr/freeze-diff-fr.log`.
- `tools/p8.py extract` on `svg/p8-siheom.svg`: **noted set = 150 of 150** (parse: lines). Log `fr/p8-extract-fr.log`, json `fr/p8-fr.json`. `compare` vs core P8: **CLEAN** (missing=[] extra_count=0 keydiff=[137, 138]). Log `fr/p8-compare-fr.log`.
- `check_core.py` / `check_gloss.py` (scratch copies with ED + gloss prefix patched to the edition): **gloss fails 0, orphan issues 0**, phrases 8/8 verbatim (incl. the new phrase #7 with (1면)); dates all correct. Log `fr/check-fr.log`.
- Text layers: print and web PDFs each extract to **52,304 bytes, byte-identical** (`cmp` rc 0). Extracts `fr/print-fr.txt`, `fr/web-fr.txt`.
- P8 min font 9.975pt (PyMuPDF on the print PDF, P8 answers region y≥1302/2700: 170 spans, 165 at 9.975pt), ≥ 9.75pt. Log `fr/p8font-fr.log`.
- 150-key check (`keycheck-ko.py`, REG from edition sources vs keys extracted from P8 SVG): 149 exact + #150 `✓` (expected) = **150/150**. Log `fr/keycheck-fr.log`; full table in `fr/EDITION-RECORD.md`.
- §1.1 grep audit: paper `#fbfaf6` 1×/page (P4/P6 4×, same as core — colour also used in table cells), VOL.4 correct on all pages, VOL.5 0 except P7 (2, by design), `·` counts identical to core page-by-page and only in gloss/option/credit contexts, colour set identical to core page-by-page. Log `fr/style11-fr.log`.
- Census (`census.py`, ex/match stems + D6 segments vs text.md): ex/match 166 items, 0 missing; D6 0 missing. Log `fr/census-fr.log`.
- Visual read: all 8 print pages at 100dpi, zero issues. PNGs in `hidden_files/w47/scratch-fanout-ko3/fr/pages/`.

## Output files + sizes (final render, ko3 run 1)

- Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ko-fr/`
- Print PDF: `Lucerna-VOL4-KO-FR.pdf` — **43,751,522 bytes**, 8 pages, SHA-256 `1f6add20c07db17f556b1c2d3303d5e2f99a03de7be1604e2250219ae3480da1` (fix rebuild 2026-11-12; D5 value was 43,750,452 bytes / `dedad96d3ee2…`)
- Web PDF: `Lucerna-VOL4-KO-FR-web.pdf` — **3,954,158 bytes** (< 7 MB), 8 pages, SHA-256 `dc933cc18cfee50111b035d95c9ffecc3547b9a1b85f1b56b01853ad5179bbe1` (fix rebuild 2026-11-12; D5 value was 3,951,154 bytes / `eea62fb6f68e…`); pdftotext **52,326 bytes, byte-identical to the print PDF**.
- Text export: `2026-w47-ko-fr.text.md` — 36,131 bytes, 8 pages, 463 items, SHA-256 `661b391e24d370bc54b2c9dd615f3e0c661a99dfc2b4539db05c615f871570de` (exported from source via the fixed `textmd.py` (md5 `00d8f52d96ecad396cbc03603d98fa9b`), never from PDF; old #2: 26,727 B / 332 items, `fabcc1c3…` — the fixed re-export; re-exported 2026-11-12 (fix round 2, R2-1: textmd.py dedup fix, 8 items restored, 455→463 items))
- `ABSTRACT.txt`: one line, French, no ASCII double quotes, 378 bytes, SHA-256 `d34aecc9380d252bd3f669b6306e47e85bcdccbd1b0971bbf6297b1d055b5054` (unchanged from #2). `Lucerna Korean Weekly VOL.4 : le compte à rebours du CSAT à J-3, l'examen le 19 novembre, le Jour du kimchi le 22 novembre avec un kimjang à 199 456 wons, le premier titre de Samsung en Korean Series depuis 12 ans, plus l'inscription à l'examen d'histoire et les feuillages de fin d'automne — texte coréen avec explications en français, niveaux A2 à B2, 150 exercices.`
- `WEEKLY-KIT.md`: this file. Build records: `hidden_files/w47/scratch-fanout-ko3/fr/EDITION-RECORD.md`.

## Open verification debts (carried to the parent line)

- Independent proofread of this edition not yet done — to be assigned by the coordinator (proof1, separate person from the builder).
- Fact debts inherited from core-ko (see core KIT): no observed Naejangsan/Wolchulsan foliage peak announced at Nov 10 press time; HanNeungGeom details (other than date/time/fee) from secondaries; K League 35R scores not verified — not cited; WiKim Festival 2026 time/theme/session not found in an independent source (printed as scheduled).

## D5 rebuild (2026-11-12, SOP §1.1)

- Template: `mechanism/svglib-ko-d5.py` installed as edition `svglib.py` (`_D5_READER = "latin"`, reader fr; diff vs template: 0 lines). Old svglib kept as `svglib.pre-d5` in the edition dir and in `hidden_files/w47/scratch-d5-ko/2026-w47-ko-fr/pre/`.
- Build: `tools/venv/bin/python` throughout. `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Gates (all in `hidden_files/w47/scratch-d5-ko/2026-w47-ko-fr/`): D5 census PASS (Latin 0 / Cyrillic 0 / curly-in-CJK 0); `census_quotes.py` 0 defective glyphs; `head_check.py` PASS 0 defects; `occlusion_audit.py` 0 flags; `p8.py extract` 150/150, `compare` vs core-ko CLEAN (keydiff=[137, 138], expected reader-language keys); `spill_sweep.py` 0 SPILL (360 OBSERVE); `boxtitle_check.py` 0 DEFECT (73 titles, 964 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` 0 absolute defects (ratios n=398 median 1.007 boldT 1.040 boldF 0.989; P8 234→217 lines, slack 60.0→75.5px); text layer print/web char-multiset diff 0 (23,641 = 23,641, pdftotext 52,167 bytes byte-identical).
- `freeze.py` (system python3 Pillow 10.2.0, coordinator-approved one-off exception): `diff` patched vs base-venv RC=0, added CJK 0 (Latin strings +591 from run splitting, expected). `baseline` 7/8 (P2–P8 OK; P1 differs): adjudicated interpreter artefact, same as core-ko — P1 text multiset identical (0 diff); only the big display "1" (185 vs 183pt) + knock-on x shifts. Production (venv, canonical) is self-consistent.
- Creambox "spill" flag adjudicated FALSE POSITIVE (not a defect, no content change made): the tool's spill check compares the patched line's y against the BASELINE box position, but the P6 gloss box moved down with the reflowed column (base box bottom 502.9 → patched box bottom 575.95); the gloss line (y 528.2) sits inside the patched box. Same defect class as ko-ru/ko-en, verified by SVG geometry (patched box x=989 y=460 h=115.95; line inside) and by the absolute check (patched lines vs patched boxes) at 0 defects.
- No content files changed. No true D5 defects in this edition.
