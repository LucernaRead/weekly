# Lucerna Weekly — W47 Korean, German reader (VOL.4) — WEEKLY KIT

- Slug: `2026-w47-ko-de` (target ko, reader German)
- Issue week: 2026-11-16 (Mon) – 2026-11-22 (Sun), VOL.4
- Press time: **2026-11-10** (inherited from core-ko run 11). No score or event after Nov 10 is claimed; Nov 16–22 events are presented as scheduled. Nov 19-only measures are dated Nov 19 only.
- Format: 8 pages, 1950×2700, 4 columns, 150 exercises, continuous numbering 1–150, every exercise in the registry.
- Fan-out of the finalized ko core (`core-ko`, run 11 (fix1) + textmd fix2): Korean content frozen; only the explanation layer (glosses, box titles, instructions, "Und du?" prompts, P7 letters disclosure, P8 answer notes, furniture) is in German. Build interpreter locked to **/usr/bin/python3** (system PIL 10.2.0) — the venv (PIL 13.0.0) measures the same Korean serif strings ~1.1% wider and flips freeze 0/8 vs 8/8 (core fix #15). render.py / webpdf.py still use the venv (cairosvg/fontTools, no PIL metrics).
- **Note on this KIT file:** the previous KIT (written in fan-out #2) was lost when `apply-ko.py` wiped the edition directory during the ko3 rebuild (the apply does a full `rmtree` and does not preserve the KIT). This file was rewritten in full in ko3 run 1, reconstructing the #2/fix1 history from the #2 EDITION-RECORD (`scratch-fanout-ko/de/EDITION-RECORD.md`) and the fix1 FIX-LOG (`scratch-fix-ko-de1/FIX-LOG.md`); the ko3 run-1 sections below are primary. The es/fr KITs were backed up to ko3 scratch before their applies for the same reason.

## Lead topic

CSAT week: D-3 (Mon Nov 16) → advance assembly D-1 (Wed Nov 18) → D-day (Thu Nov 19), then Kimchi Day (Sun Nov 22). Second lead: Samsung's Korean Series title (4–1 over kt wiz, first since 2014). Third lead: kimjang cost down 9.0% to 199,456 won (aT, Nov 9 basis, announced Nov 10).

## Contents by page

- P1 (A2): lead (CSAT week + KS + kimjang cost), numbers box (3 / 1 / 199,456 / 4–1 / 12), calendar Nov 16–22, contents, word of the week 「예비소집」, autumn photo (Hakkoda file photo, honestly captioned), quiz 7–10.
- P2 (A2): kimjang cost feature, Kimchi Day box, History exam sign-up box (81st, Sat Nov 28, advanced only, 27,000 won), 김장 나눔, 겨울 밥상, shopping list, ssam photo, D-day strip (D-3/D-1/D-데이/김치의 날), ex. 11–28.
- P3 (A2→B1): Kimchi Day + late-foliage wrap-up (forecast vs observation; no observed Naejangsan peak announced at press time — readers sent to Weather Nuri 날씨누리), bukhansan-ui + Cézanne apples photos, ex. 29–46.
- P4 (B1): full Korean Series result (G1–G5 scores, venues, 4 straight wins after 1 loss, 9th title), postseason ladder (wildcard LG 4–1 Doosan, semi-playoff KIA 3–0 LG, playoff Samsung 3–2 KIA), K League box (FC Seoul early champions 33R, 36R Nov 21–22, finals Dec 5–6), ex. 47–64.
- P5 (B1): CSAT week, advance assembly (times/places vary by school), Nov 19-only measures, 수능이 끝나면, Kimchi Day youth ideas (WiKim youth session), 시험 전날의 하루, study photo, ex. 65–82.
- P6 (B2): 「예보에서 결과로」 — forecast→result theme; comparison table (last week vs this week: KS schedule→result Samsung 4–1; foliage forecast dates→passed; kimjang cost Oct 16 price→Nov 9 survey 199,456 won), ex. 83–100.
- P7 (A2→B2): A2 김치의 날의 말, B1 날짜 세는 말 (D-3/D-1/D-데이), B2 예보와 결과 읽는 법; error clinic (김치의날 spacing; 삼성는→삼성은; 담궈요→담가요; 날예요→날이에요); frame 「〜 후에」; readers' corner (editor's example letter + single German disclosure; promise carried to **VOL.5**); P7 photo strip (kimchi-making, Anattadairy CC0); 8 P7 phrases, all verbatim from this issue's own articles; VOL.5 preview (HanNeungGeom Sat Nov 28, post-CSAT stories, Kimchi Day follow-up, letters/best P8 writing). Ex. 101–112.
- P8 (全部): 38 items — A 연표 8, B 일반 8, C mini-reading 4 (test character 민준이/Minjun, 수험생 story), D 造句 4, E 翻译 4 (stems 137/138 in Korean, keys in German; stems 139/140 in German, keys stay Korean — verified from the P8 SVG key nodes + content8.py:70/72; now agrees with :60), F 词汇配对 4, G dialogue 完形 5, H writing 1 「나의 김치의 날」 (model 169 chars, in 150–200). P8 photo (kimchi-making2, Anattadairy CC0) in col 4 below the H model. Full printed answers 1–150 with one-line German notes.

## Measured exercise counts (final build, run 1 — fan-out #3 rebuild from core run 11)

- TOTAL **150**; by page 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38
- By level A2 51 / B1 72 / B2 27
- By type: Satz ergänzen 48, Auswahl 52, Paare zuordnen 16, Umformen 4, Sätze bilden 8, Richtig oder falsch 4, Lückentext 13, Übersetzen 4, Schreiben 1
- Model chars (H writing): 169
- No FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build.
- **P8 answer font size (measured with PyMuPDF on the final print PDF): min 9.975 pt** (173 spans in the P8 answers region y≥1302/2700, 168 at 9.975pt) — above the SOP §1.1 threshold of 9.75 pt.
- Level badges ("chips"): 138 total, 35 on P8.

## Trend / fact sources

All facts inherited from core-ko run 11, whose KIT documents them with attribution caveats (Korean Series 4–1; Kimchi Day Nov 22; kimjang cost 199,456 won; CSAT Nov 19, 551,864 candidates; foliage forecasts incl. Weatheri Naejangsan Nov 11; fire-precaution period Nov 1–Dec 15; K League FC Seoul champions; HanNeungGeom 81st Nov 28; Hankook Tire kimjang sharing). Nothing after Nov 10 is claimed. No new facts were introduced by this fan-out; German renderings only.

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

- Core copied verbatim, then a translation map (`map-de.json`, 216 keys + 8 instr, generated by `gen-map-de.py` — hand-authored; META/INSTR live inside `gen-map-de.py`, so `mk-lang.py` cannot be used for de) applied by exact quoted-literal replacement, longest first, plus asserted structural edits (`apply-ko.py`).
- `svglib.py` copied verbatim, fonts frozen (md5 `1c94d836d46fcf6fc67e88b0f0febd34`, same as core).
- Gloss prefix `Hinweis — `; footer `Lucerna　KOREANISCHE WOCHENZEITUNG VOL.4　Koreanischer Text　Erklärungen auf Deutsch`; page line `Seite {n} von {total}`.
- P7 letters: single German disclosure replaces `lcn`; `lko` and `lcn2` lines + their render lines removed; `lh` formula rebuilt for 2 blocks (W46 ko-de precedent).
- P8 E-group re-aiming (W46 ko-de precedent): keys 137/138 translated to German; stems 139/140 translated, keys stay Korean → `p8.py compare` keydiff `[137, 138]`, status CLEAN.
- P8 page separator `— 제{pg}면 —` stays frozen. H writing note is an f-string (structural edit: `Mustertext in Abschnitt H auf dieser Seite ({NCHARS} Zeichen)`); H key is a plain map entry (`(offene Aufgabe — Mustertext unten)`).
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style `n. key — note`, satisfied by construction.
- Straight apostrophe U+0027 only; U+2019 scan across all 8 SVGs = 0. The P7 frame line uses 「」 (core-style) — see Fixes log #1.
- P8 answer-note person names checked one by one: the only personal name is 민준 (Minjun, #129 "Minjun geht am Mittwoch zur Vorversammlung", #135 note) — standard Revised Romanization, consistent within the edition; no sumo-style romaji issue (ja-family class does not apply here). Team/company names (Samsung, kt wiz, KIA, LG, FC Seoul, Weatheri, KBO) match core's own renderings.
- German renderings (W46 ko-de precedent where noted): CSAT kept; Kimchi-Tag; Kimjang-Kosten; Vorversammlung (예비소집); Geschichtsprüfung (한능검); Forstbehörde (Forestry Service); Weatheri kept; German dates `18. Nov.`; German numbers `199.456 Won` / `9,0 %`; score `4:1`. Type names: Satz ergänzen / Auswahl / Paare zuordnen / Umformen / Sätze bilden / Richtig oder falsch / Lückentext / Übersetzen / Schreiben. Instr: Ausfüllen / Paare zuordnen / Wort-Bedeutung zuordnen / Sätze bilden / Übersetzen / Schreiben. P7 teaser headroom is 40.8px (footer 2580 − teaser 2539.2) — tighter than core (32.3px) but inside limits; do not lengthen the P7 disclosure.

## Self-proofread record (full pass over rendered pages + extracted SVG text + text.md)

- **Run 1 (fan-out #3 rebuild, 2026-11-11):** build clean (0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150); P2-feature ends 1531, P8-keys ends 2457, P7 teaser 2539.22. boxtitle 8/8 (no shortening needed — the #2 shortenings are in the map). All gates pass (see Mechanical gates). Full visual read of all 8 print pages at 100dpi: zero issues. All 150 keys re-derived (keycheck 150/150; #150 `✓` expected, identical in core). Map hygiene: 0 double-space / edge-space issues in 216 values.
- **History (fan-out #2 + fix1, superseded by this rebuild):** #2 run 1 found a P2-feature FLOW OVERFLOW (the shopping-list box covering the D-day strip; occlusion 7 flags) caused by the German 봉사활동 gloss wrapping to 3 lines — gloss shortened to `봉사활동 = Ehrenamt · 이웃 = Nachbar · 따뜻하다 = warm` (2 lines), run 2 clean, ALL GATES PASS (print 45,682,479 B, SHA `bcf8f141…`). #2 run 1 also found 2 box titles over 386.5px (P3 `Gut zu wissen` 389.4px, P5 `Zahlen der Jugend` 396.8px) → shortened to `Wichtig` (319.6px) / `Jugendzahlen` (345.7px). fix1 (proof1 D1+D5) changed only `content7.py:81` (「」 Frame) and `content12.py:174` (Ernteaussichten) — both re-applied post-apply in this rebuild (see Fixes log). The old fix1 print (45,682,367 B, SHA `c19fe6c1…`), web (4,035,061 B, SHA `375f0cf79e6c4592edc504cdafcca469aff402ee79393aa694a5cb4cc3dd0878`), and text.md (26,603 B, SHA `a76413749471ee248e5f6bf4c83d1047a63e3134104f9fd63098c148196ca0d1`) are superseded (web/text values from fix1 FIX-LOG :41/:42, verified by grep). Fix1 provenance note (from its FIX-LOG): the brief path given in the fix1 task (`~/workspace/weekly-git/hidden_files/w47/briefs/brief-coordinator.md`) does not exist on disk; the brief actually read was the goals-side copy at `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/briefs/brief-coordinator.md`.
- **Lesson from #2 (family-wide):** always measure gloss wraps WITH the reader-language gloss prefix — the prefix alone can cost a line.
- **Independent proofread:** not yet done — to be assigned by the coordinator (proof2 for this edition, separate person). This KIT records the builder's self-check only.

## Fixes log

| # | Found | Fix | Round |
|---|---|---|---|
| 1 | D1 carry-forward: the map reproduces curly double quotes U+201C/U+201D in `content7.py:81` (`Rahmen: “nach ~”. Frag: “〜 후에 뭐 해요?”`) | Re-applied the fix1 form `Rahmen: 「nach ~」. Frag: 「〜 후에 뭐 해요?」` (core-style 「」 wrap) post-apply, before building. Post-build sweep: U+201C = 0, U+201D = 0, U+2019 = 0 across all 8 SVGs + text.md; the 「」 form is visible in the P7 render and in text.md line 761 | ko3 run 1 |
| 2 | D5 carry-forward: the map reproduces `작황 = die Ernte` in `content12.py:174` | Re-applied `작황 = Ernteaussichten` (covers 收成 + 长势; the idiomatic German for 「작황이 좋다」) post-apply, before building. Verified in the P2 render and in text.md | ko3 run 1 |
| 3 | Core D2/D3/D4 flow through the rebuild: P1 quiz #10 + P4 #47 `어느 팀이에요`; P4 #48 without the duplicated `시리즈`; P7 frame example + phrase #7 now the new sentence `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요` (1면) | Via apply from core run 11; verified in the renders (P1, P4, P7) and in check_core phrases 8/8 verbatim | ko3 run 1 |
| 4 | #2 run 1: P2-feature FLOW OVERFLOW — shopping-list box (390px) did not fit, was clamped and painted OVER the D-day strip (occlusion 7 flags: 3 COVER on shopping-list lines, 4 TEXTX vs strip/exercise header) | Root cause: the German 봉사활동 gloss wrapped to 3 lines (`ehrenamtliche Arbeit …`, +1 line = +29.7px vs en), pushing the box past the bottom (en ended at 1531 with only 9px spare). Gloss shortened to `봉사활동 = Ehrenamt · 이웃 = Nachbar · 따뜻하다 = warm` (2 lines, verified with core `svglib.wrap`, prefix included). All other P2 glosses measured: 효능 2, 아삭하다 2, 조사하다 3 in both en and de (identical y-coords). Rebuilt as run 2: P2-feature ends 1531, 0 warnings, occlusion 0 flags. The shortened gloss is in the map, so the ko3 rebuild inherits it | #2 run 2 |
| 5 | #2 run 1: 2 box titles over the 386.5px inner width (P3 `김치의 날에 알아 둘 것　Gut zu wissen` 389.4px, P5 `이번 주 청년 숫자　Zahlen der Jugend` 396.8px) | Shortened in the map: P3 → `Wichtig` (319.6px), P5 → `Jugendzahlen` (345.7px); others kept (P1 `In Zahlen` 312.9, P2 hanneung `Anmeldung` 264.2, P2 shopping `Einkaufsliste` 326.7, P7 clinic `Fehlerklinik` 248.3, P7 frame `Muster der Woche` 341.3, P7 letters `Leserecke` 246.9). `boxtitle-ko.py` 8/8 after re-apply; inherited by ko3 | #2 run 2 |
| 6 | #2: map generation pitfall | `de-replace.json` had a stray `{` at the start of the second block (JSON error, fixed) and the Frame-entry value in the en source is a literal backslash escape `“` (not a real “ char), so the replace table needed a separate backslash-form key to match. `gen-map-de.py` initially wrote `map-en.json` / printed `GEN-MAP-EN`; fixed in `mk-de.py` and the current file | #2 |
| 7 | Independent reproof (2026-11-12): 6 exact-duplicate exercise slots (Q12/Q13/Q22/Q47/Q74/Q102), P1 lead sentence missing "다른 날의" | Q12/Q13/Q22/Q47/Q74/Q102 replaced with new questions from same-page article facts (P2 kimjang cost 13.4% below average, 6 kimjang ingredient types, chili powder -1.8%, P4 Samsung 9th title, P5 exam ticket by 8 a.m., P7 Kimchi Day fixed by law Feb 2020); P8 keys + reader notes updated; P1 sentence → "이번 주의 다른 날의 조치가 아니에요". Rebuilt + re-gated: TOTAL 150, p8 CLEAN, occlusion 0, spill/boxtitle/edge 0, textlayer PASS, text.md 455 items | fix rebuild 2026-11-12 |
| 8 | Independent reproof round 2 (2026-11-12, PROOF-NOTE-2): R2-1 text.md export drops 7 numbered items (P2 D Q26, P4 D Q61–Q63, P8 B Q121/Q126, P8 F Q142) | R2-1: `textmd.py` global `seen` dedup replaced by per-call-site retention for `.ex`/`.match_set` items (plain prose keeps global dedup); text.md re-exported, 8 items restored per edition (7 numbered + P6 table row label `김장비용`, same root cause, verified against the print P6 table); per-page inventory 150/150, match terms 16/16 standalone, whole-book 150/150; PDFs untouched (print/web SHA unchanged); p8 compare CLEAN (keydiff [137, 138]), D5 census PASS (0/0/0, curly 0) | fix rebuild 2, 2026-11-12 |

## Adjudicated (not defects)

- P8 match-item notes end with the option letter repeated (`25. d — … 199.456 Won d`, `26. a — … 22. Nov. a`): the letter is in the source note literal itself, core's own convention (`김장비용=四口之家199,456韩元 d` in core-ko); the de map translated the note text and kept the letter.
- #40/#123/#124 note "Weatheri-Prognose": core's own rendering of 웨더아이 (private weather company, corrected in core run 4) — not a typo.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "(offene Aufgabe — Mustertext unten)" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (de): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure).
- text.md 449 items vs core 452: three accounted drops, no content gap — (1) `is_prose` drops the bare 3-letter Latin word "Alle" (P1 contents 8면 row level; the SVG/PDF render "Alle" correctly, visible on the P1 render); (2) `lcn2` removed by design; (3) `lko` removed by design. Same pattern as en.
- Freeze diff added CJK 7, all U+3000 (ideographic space, footer): back to 7 from the fix1 16 (the 9 extra chars were core-side stem drift vs the then-current core; the rebuild from the fixed core resolves it).
- The P2 shopping-list box sits entirely above the D-day strip with no overlap (the #2 fix verified again in the ko3 P2 render).
- The German #7 phrase note stays the short map form `Nach der CSAT kommt der Kimchi-Tag.` — no fix1 long-note existed for de; the Korean sentence + (1면) citation self-healed from the new core.
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style `n. key — note`, satisfied by construction.
- P8 answer-note stem 10.35pt is the recorded core adjudication — not a defect, not changed.
- `text.md` contains `___` (23 places) — exported from the source literals, where blanks stay as `___`; the SVG/PDF render them as 1.1pt ink underlines. Same as core.

## Occlusion audit

- `tools/occlusion_audit.py` on `svg/`: **0 flags**. Selftest first: planted classes fired {BOXTITLE: 1, COVER: 1, EDGE: 1, FOOTER: 1, LINEX: 1, TEXTX: 1}; clean controls silent. Log at `hidden_files/w47/scratch-fanout-ko3/de/occlusion-de.log` (json `occlusion-de.json`).

## Mechanical gates (final state, run 1)

- `run.py` (build run 1, `/usr/bin/python3`): exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150 (A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2457, P7 teaser 2539.22). Log `hidden_files/w47/scratch-fanout-ko3/de/build-de-run1.log`; SVG hashes `de/sha-de-run1.txt` (vs #2 run 2, P1/P2/P4/P7 changed — P2 is the fix1 D5 change, content12.py:174, P2 SVG 92390ad4…→cfab7ef1…; P3/P5/P6/P8 byte-identical to #2 run 2. "Only P1/P4/P7 changed" holds only vs the fix1-after SVGs baseline, where the P1/P4/P7 deltas are the core D2/D3/D4 fixes).
- `tools/freeze.py baseline` (**/usr/bin/python3**): **8/8 SVGs byte-identical**, tool self-reports 8/8 with per-file OK rows. Log `hidden_files/w47/scratch-fanout-ko3/de/freeze-de.log`; rebuild products deleted after the pass (log + json kept).
- `tools/freeze.py diff` (core-ko svg vs edition svg): TOTAL added CJK characters 7, all U+3000 (see Adjudicated). Log `de/freeze-diff-de.log`.
- `tools/p8.py extract` on `svg/p8-siheom.svg`: **noted set = 150 of 150** (parse: lines). Log `de/p8-extract-de.log`, json `de/p8-de.json`. `compare` vs core P8: **CLEAN** (missing=[] extra_count=0 keydiff=[137, 138]). Log `de/p8-compare-de.log`.
- `check_core.py` / `check_gloss.py` (scratch copies with ED + gloss prefix patched to the edition): **gloss fails 0, orphan issues 0**, phrases 8/8 verbatim (incl. the new phrase #7 with (1면)); dates all correct. Log `de/check-de.log`.
- Text layers: print and web PDFs each extract to **52,078 bytes, byte-identical** (`cmp` rc 0). Log `de/textlayer-diff-de.txt` (empty diff).
- P8 min font 9.975pt (PyMuPDF on the print PDF, P8 answers region y≥1302/2700: 173 spans, 168 at 9.975pt), ≥ 9.75pt. Log `de/p8font-de.log`.
- 150-key check (`keycheck-ko.py`, REG from edition sources vs keys extracted from P8 SVG): 149 exact + #150 `✓` (expected) = **150/150**. Log `de/keycheck-de.log`; full table in `de/EDITION-RECORD.md`.
- §1.1 grep audit: paper `#fbfaf6` 1×/page (P4/P6 4×, same as core — colour also used in table cells), VOL.4 correct on all pages, VOL.5 0 except P7 (2, by design), `·` counts identical to core page-by-page and only in gloss/option/credit contexts, colour set identical to core page-by-page. Log `de/style11-de.log`.
- Census (`census.py`, ex/match stems + D6 segments vs text.md): ex/match 166 items, 0 missing; D6 0 missing. Log `de/census-de.log`.
- Visual read: all 8 print pages at 100dpi, zero issues. PNGs in `hidden_files/w47/scratch-fanout-ko3/de/pages/`.

## Output files + sizes (final render, run 1)

- Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ko-de/`
- Print PDF: `Lucerna-VOL4-KO-DE.pdf` — **43,754,319 bytes**, 8 pages, SHA-256 `8d217beb86ae25f72ddd5413bd59011fe7051adc30965e0bb09cf2298e47c3d2` (fix rebuild 2026-11-12; D5 value was 43,753,274 bytes / `01c8a283684b…`)
- Web PDF: `Lucerna-VOL4-KO-DE-web.pdf` — **3,956,937 bytes** (< 7 MB), 8 pages, SHA-256 `4b1a54ce3040982076796965e45135e00ac057848315e6d3374235b6ec9212e4` (fix rebuild 2026-11-12; D5 value was 3,953,949 bytes / `b0ee1af9d6ed…`); pdftotext **52,066 bytes, byte-identical to the print PDF**.
- Text export: `2026-w47-ko-de.text.md` — 36,012 bytes, 8 pages, 463 items, SHA-256 `4f6945d3611552aa90fc1fea66d4270f63ae939fb3196f616cee86215f68c16a` (exported from source via the fixed `textmd.py` (md5 `00d8f52d96ecad396cbc03603d98fa9b`), never from PDF; re-exported 2026-11-12 (fix round 2, R2-1: textmd.py dedup fix, 8 items restored, 455→463 items)).
- `ABSTRACT.txt`: 350 bytes, SHA-256 `2d7ba827b0d051ff1647668c108883dfca05deb7fd5e7f51174a5135a3f9a7c6`. `Lucerna Korean Weekly VOL.4: die CSAT-Woche — Countdown D-3, Prüfung am 19. Nov., Kimchi-Tag am 22. Nov., Kimjang-Kosten bei 199.456 Won, Samsungs erster Korean-Series-Titel seit 12 Jahren, dazu Anmeldung zur Geschichtsprüfung und Spätherbstlaub — koreanischer Text mit deutschen Erklärungen, Stufen A2 bis B2, 150 Übungen.`
- `WEEKLY-KIT.md`: this file. Build records: `hidden_files/w47/scratch-fanout-ko3/de/EDITION-RECORD.md`.

## Open verification debts (carried to the parent line)

- Independent proofread of this edition not yet done — to be assigned by the coordinator (proof2, separate person from the builder).
- Fact debts inherited from core-ko (see core KIT): no observed Naejangsan/Wolchulsan foliage peak announced at Nov 10 press time; HanNeungGeom details (other than date/time/fee) from secondaries; K League 35R scores not verified — not cited; WiKim Festival 2026 time/theme/session not found in an independent source (printed as scheduled).

## D5 rebuild (2026-11-12, SOP §1.1)

- Template: `mechanism/svglib-ko-d5.py` installed as edition `svglib.py` (`_D5_READER = "latin"`, reader de; diff vs template: 0 lines). Old svglib kept as `svglib.pre-d5` in the edition dir and in `hidden_files/w47/scratch-d5-ko/2026-w47-ko-de/pre/`.
- Build: `tools/venv/bin/python` throughout. `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Gates (all in `hidden_files/w47/scratch-d5-ko/2026-w47-ko-de/`): D5 census PASS (Latin 0 / Cyrillic 0 / curly-in-CJK 0); `census_quotes.py` 0 defective glyphs; `head_check.py` PASS 0 defects; `occlusion_audit.py` 0 flags; `p8.py extract` 150/150, `compare` vs core-ko CLEAN (keydiff=[137, 138], expected reader-language keys); `spill_sweep.py` 0 SPILL (358 OBSERVE); `boxtitle_check.py` 0 DEFECT (73 titles, 968 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` 0 absolute defects (ratios n=402 median 1.009 boldT 1.040 boldF 0.994; P8 231→215 lines, slack 60.0→61.0px); text layer print/web char-multiset diff 0 (23,803 = 23,803, pdftotext 51,926 bytes byte-identical).
- `freeze.py` (system python3 Pillow 10.2.0, coordinator-approved one-off exception): `diff` patched vs base-venv RC=0, added CJK 0 (Latin strings +590 from run splitting, expected). `baseline` 7/8 (P2–P8 OK; P1 differs): adjudicated interpreter artefact, same as core-ko — P1 text multiset identical (0 diff); only the big display "1" (185 vs 183pt) + knock-on x shifts. Production (venv, canonical) is self-consistent.
- Creambox "spill" flag adjudicated FALSE POSITIVE (not a defect, no content change made): the tool's spill check compares the patched line's y against the BASELINE box position, but the P6 gloss box moved down with the reflowed column (base box bottom 502.9 → patched box bottom 575.95); the gloss line (y 528.2) sits inside the patched box. Same defect class as ko-ru/ko-en, verified by SVG geometry (patched box x=989 y=460 h=115.95; line inside) and by the absolute check (patched lines vs patched boxes) at 0 defects.
- No content files changed. No true D5 defects in this edition.
