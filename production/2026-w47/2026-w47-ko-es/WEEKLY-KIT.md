# Lucerna Weekly — W47 Korean, Spanish reader (VOL.4) — WEEKLY KIT

- Slug: `2026-w47-ko-es` (target ko, reader Spanish)
- Issue week: 2026-11-16 (Mon) – 2026-11-22 (Sun), VOL.4
- Press time: **2026-11-10** (inherited from core-ko run 11). No score or event after Nov 10 is claimed; Nov 16–22 events are presented as scheduled. Nov 19-only measures are dated Nov 19 only.
- Format: 8 pages, 1950×2700, 4 columns, 150 exercises, continuous numbering 1–150, every exercise in the registry.
- Fan-out of the finalized ko core (`core-ko`, run 11 (fix1) + textmd fix2): Korean content frozen; only the explanation layer (glosses, box titles, instructions, "And you?" prompts, P7 letters disclosure, P8 answer notes, furniture) is in Spanish. Build interpreter locked to **/usr/bin/python3** (system PIL 10.2.0) — the venv (PIL 13.0.0) measures the same Korean serif strings ~1.1% wider and flips freeze 0/8 vs 8/8 (core fix #15). render.py / webpdf.py still use the venv (cairosvg/fontTools, no PIL metrics).
- **Note on this KIT file:** the original KIT (fan-out #2) was backed up to ko3 scratch (`es/ko-es-WEEKLY-KIT-pre-ko3.md`, SHA `a7dd2fa1…`) before the ko3 apply wiped the edition directory (the apply does a full `rmtree` and does not preserve the KIT); this file is that backup restored plus the ko3 rebuild sections below. The "Core moved" and "Disk-quota incidents" notes from #2 are now closed history (see below).

## Core moved during fan-out #2 (closed history)

- At **2026-11-11 08:40:30 UTC**, while the fr edition was being papered over, `core-ko/content12.py`, `content34.py`, `content7.py` were modified and the core SVGs rebuilt (08:40:40–08:41:03). Core KIT still said "run 10" (mtime 02:16) — no run-11 record existed yet.
- Changed pages: p1 (`c47bc434…` → `00227ca1…`), p4 (`4b18a1d9…` → `d997631e…`), p7 (`e6908156…` → `14b7cf13…`); p2/p3/p5/p6/p8 byte-identical. Verified content changes (Korean strings): P1 quiz stem `한국시리즈에서 우승한 팀은 어디예요?` → `…어느 팀이에요?` and option list gained the `A.` prefix; P4 `한국시리즈 시리즈 전적은…` → `한국시리즈 전적은…` (duplicated 시리즈 dropped); P7 frame example `수능 후에 김치의 날이 와요` → `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요`, and the letters disclosure reworded.
- Consequence at the time: **ko-fr (and #1's ko-en/ko-de) were built from the pre-08:40 core and were then stale on p1/p4/p7. ko-es was applied at 08:44 from the new core and matched it (freeze baseline 8/8, freeze diff +7 CJK only).**
- **Closed in ko3 (2026-11-11):** the core was finalized as run 11 (fix1) + textmd fix2, and ALL 10 fan-out editions were rebuilt from it in fan-out #3 — ko-en, ko-de, ko-es included. The coordinator's decision was the rebuild itself; this edition's ko3 run 1 (below) stands on the finalized core.

## Lead topic

CSAT week: D-3 (Mon Nov 16) → advance assembly D-1 (Wed Nov 18) → D-day (Thu Nov 19), then Kimchi Day (Sun Nov 22). Second lead: Samsung's Korean Series title (4–1 over kt wiz, first since 2014). Third lead: kimjang cost down 9.0% to 199,456 won (aT, Nov 9 basis, announced Nov 10).

## Contents by page

- P1 (A2): lead (CSAT week + KS + kimjang cost), numbers box (3 / 1 / 199,456 / 4–1 / 12), calendar Nov 16–22, contents, word of the week 「예비소집」, autumn photo (Hakkoda file photo, honestly captioned), quiz 7–10.
- P2 (A2): kimjang cost feature, Kimchi Day box, History exam sign-up box (81st, Sat Nov 28, advanced only, 27,000 won), 김장 나눔, 겨울 밥상, shopping list, ssam photo, D-day strip (D-3/D-1/D-데이/김치의 날), ex. 11–28.
- P3 (A2→B1): Kimchi Day + late-foliage wrap-up (forecast vs observation; no observed Naejangsan peak announced at press time — readers sent to Weather Nuri 날씨누리), bukhansan-ui + Cézanne apples photos, ex. 29–46.
- P4 (B1): full Korean Series result (G1–G5 scores, venues, 4 straight wins after 1 loss, 9th title), postseason ladder (wildcard LG 4–1 Doosan, semi-playoff KIA 3–0 LG, playoff Samsung 3–2 KIA), K League box (FC Seoul early champions 33R, 36R Nov 21–22, finals Dec 5–6), ex. 47–64.
- P5 (B1): CSAT week, advance assembly (times/places vary by school), Nov 19-only measures, 수능이 끝나면, Kimchi Day youth ideas (WiKim youth session), 시험 전날의 하루, study photo, ex. 65–82.
- P6 (B2): 「예보에서 결과로」 — forecast→result theme; comparison table (last week vs this week: KS schedule→result Samsung 4–1; foliage forecast dates→passed; kimjang cost Oct 16 price→Nov 9 survey 199,456 won), ex. 83–100.
- P7 (A2→B2): A2 김치의 날의 말, B1 날짜 세는 말 (D-3/D-1/D-데이), B2 예보와 결과 읽는 법; error clinic (김치의날 spacing; 삼성는→삼성은; 담궈요→담가요; 날예요→날이에요); frame 「〜 후에」; readers' corner (editor's example letter + single Spanish disclosure; promise carried to **VOL.5**); P7 photo strip (kimchi-making, Anattadairy CC0); 8 P7 phrases, all verbatim from this issue's own articles; VOL.5 preview (HanNeungGeom Sat Nov 28, post-CSAT stories, Kimchi Day follow-up, letters/best P8 writing). Ex. 101–112.
- P8 (全部): 38 items — A 연표 8, B 일반 8, C mini-reading 4 (test character 민준이/Minjun, 수험생 story), D 造句 4, E 翻译 4 (stems 137/138 in Spanish, keys stay Korean; stems 139/140 in Spanish, keys stay Korean), F 词汇配对 4, G dialogue 完形 5, H writing 1 「나의 김치의 날」 (model 169 chars, in 150–200). P8 photo (kimchi-making2, Anattadairy CC0) in col 4 below the H model. Full printed answers 1–150 with one-line Spanish notes.

## Measured exercise counts (final build, run 1 — fan-out #3 rebuild from core run 11)

- TOTAL **150**; by page 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38
- By level A2 51 / B1 72 / B2 27
- By type: Completar 48, Opción múltiple 52, Relacionar 16, Transformar 4, Formar frases 8, Verdadero o falso 4, Texto con huecos 13, Traducir 4, Escribir 1
- Model chars (H writing): 169
- No FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build.
- **P8 answer font size (measured with PyMuPDF on the final print PDF): min 9.975 pt** (172 spans in the P8 answers region y≥1302/2700, 167 at 9.975pt) — above the SOP §1.1 threshold of 9.75 pt.
- Level badges ("chips"): 138 total, 35 on P8.

## Trend / fact sources

All facts inherited from core-ko run 11, whose KIT documents them with attribution caveats (Korean Series 4–1; Kimchi Day Nov 22; kimjang cost 199,456 won; CSAT Nov 19, 551,864 candidates; foliage forecasts incl. Weatheri Naejangsan Nov 11; fire-precaution period Nov 1–Dec 15; K League FC Seoul champions; HanNeungGeom 81st Nov 28; Hankook Tire kimjang sharing). Nothing after Nov 10 is claimed. No new facts were introduced by this fan-out; Spanish renderings only.

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

- Core copied verbatim, then a translation map (`map-es.json`, 216 keys + 8 instr, generated by `gen-map-es.py` — itself derived from `gen-map-en.py` via the generic `mk-lang.py` + `es-replace.json` / `es-meta.json`) applied by exact quoted-literal replacement, longest first, plus asserted structural edits (`apply-ko.py`).
- `svglib.py` copied verbatim, fonts frozen (md5 `1c94d836d46fcf6fc67e88b0f0febd34`, same as core).
- Gloss prefix `Nota — `; footer `Lucerna　SEMANARIO COREANO VOL.4　Texto en coreano　Explicaciones en español`; page line `Página {n} de {total}`.
- P7 letters: single Spanish disclosure replaces `lcn`; `lko` and `lcn2` lines + their render lines removed; `lh` formula rebuilt for 2 blocks (W46 ko-es precedent).
- P8 E-group re-aiming (W46 ko-es precedent): keys 137/138 translated to Spanish; stems 139/140 translated, keys stay Korean → `p8.py compare` keydiff `[137, 138]`, status CLEAN.
- P8 page separator `— 제{pg}면 —` stays frozen. H writing note is an f-string (structural edit: `Texto modelo en la sección H de esta página ({NCHARS} caracteres)`); H key is a plain map entry (`(tarea abierta — texto modelo abajo)`).
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style `n. key — note`, satisfied by construction.
- Straight apostrophe U+0027 only (no U+2019 anywhere in Spanish values); U+2019 scan across all 8 SVGs = 0.
- P8 answer-note person names checked one by one: the only personal name is 민준 (Minjun, #129 "Minjun va a la convocatoria previa el miércoles", #135 note) — standard Revised Romanization, consistent within the edition; team/company names (Samsung, kt wiz, KIA, LG, FC Seoul, Weatheri, KBO) match core's own renderings. The ja-family sumo-romaji defect class does not apply here.
- Spanish renderings (W46 ko-es precedent where noted): CSAT kept; Día del Kimchi; kimjang; convocatoria previa (예비소집); examen de historia (한능검); Servicio Forestal (Forestry Service); Weatheri kept; Spanish dates `18 nov.`; Spanish numbers `199 456 wones` / `9,0 %`; score `4-1`; D-1/D-3/D-day kept as the taught terms from the Korean text. Type names: Completar / Opción múltiple / Relacionar / Transformar / Formar frases / Verdadero o falso / Texto con huecos / Traducir / Escribir. Instr: Completar / Reformular / Formar frases / Traducir / Escribir / Relacionar palabras y notas / Relacionar la montaña con su nota / Palabra y significado.

## Self-proofread record (full pass over rendered pages + extracted SVG text + text.md)

- **Probe (pre-build):** P8-keys sim end col 3 y=2457.3 (headroom 82.7, 0 overflows, 9 two-line entries); P7 sim col3 ends 1741.7, teaser 2483.7, disclosure 7 lines; P2/P3/P5 "And you?" boxes end 1198.0 / 1508.7 / 824.0, all inside limits. Log `hidden_files/w47/scratch-fanout-ko/es/probe-es.log`.
- **Apply round 1:** OK, but `boxtitle-ko.py` 7/8 — P3 `김치의 날에 알아 둘 것　Conviene saber` 408.6px > 386.5px inner width. Fix: shortened to `A saber` (317.4px). Re-applied (round 2); boxtitle 8/8. P2 shopping `Lista de la compra` 385.8px passes by 0.7px — kept, measured.
- **Run 1 (build):** exit 0, 0 warnings, TOTAL 150. But occlusion audit found **3 flags**: P2 EDGE — matching instr `Relacionar las palabras con las notas` past the page edge by 17.75px; P8 TEXTX ×2 — F-section instr `Relacionar la palabra con su significado` overlapping the F option lines. Fix (run 2): P2 instr → `Relacionar palabras y notas`; F instr → `Relacionar palabra y significado`. Run 2: EDGE gone, but TEXTX persisted (overlap 103.5px → 34.2px). Root cause measured from the SVG: the F header sits at x=1185.0 while the option text starts at x=1439.5 — a 254.5px budget, i.e. ≈21 chars (the en edition uses `Match word to meaning`). Fix (run 3): F instr → `Palabra y significado` (21 chars). Run 3: occlusion **0 flags**. All other gates pass (see Mechanical gates). Full visual read of all 8 print pages at 100dpi: zero issues. Full self-read of `2026-w47-ko-es.text.md` (332 items): zero issues. All 150 keys re-derived (keycheck 150/150; #150 `✓` expected, identical in core).
- **Run 1 (fan-out #3 rebuild, 2026-11-11):** build clean (0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150); P2-feature ends 1531, P8-keys ends 2457, P7 teaser 2483.7. boxtitle 8/8 (no shortening needed — the #2 shortenings and instr fixes are in the map). All gates pass (see Mechanical gates). Full visual read of all 8 print pages at 100dpi: zero issues. Full self-read of `2026-w47-ko-es.text.md` (449 items): zero issues. All 150 keys re-derived (keycheck 150/150; #150 `✓` expected, identical in core). SVG change footprint vs #2 run 3: **only P7 changed** (the Frame 「」 fix); P1/P2/P3/P4/P5/P6/P8 byte-identical.
- **Disk-quota incidents (process, not content — closed):** in fan-out #2 the VM disk quota (EDQUOT) blocked freeze baseline, webpdf, textmd and check-edition; gates were verified in `/tmp/es-gates/` but the web PDF, text.md, gate logs, KIT and record were not yet landed. **Closed in ko3:** the quota state recovered (74G used / 75G free at build time), all three files + record + KIT are landed in the edition/scratch dirs by this rebuild; the /tmp copies are stale and not needed.
- **Independent proofread:** not yet done — to be assigned by the coordinator (proof1 for this edition, separate person). This KIT records the builder's self-check only.

## Fixes log

| # | Found | Fix | Round |
|---|---|---|---|
| 1 | boxtitle check after apply round 1: P3 title `Conviene saber` 408.6px over the 386.5px inner width | Shortened to `A saber` (317.4px); re-applied, boxtitle 8/8 before the build | #2, 2 (apply) |
| 2 | occlusion audit on run-1 build: P2 matching instr past the page edge (+17.75px); P8 F instr overlapping option lines | P2 instr → `Relacionar palabras y notas`; F instr → `Relacionar palabra y significado` | #2, 2 (build) |
| 3 | occlusion audit on run-2 build: P8 TEXTX persisted (overlap 34.2px) — F-header budget is only 254.5px (x=1185.0 → option text at x=1439.5) | F instr → `Palabra y significado` (21 chars, same length class as en `Match word to meaning`); run 3 occlusion 0 flags | #2, 3 (build) |
| 4 | ko3: the map reproduces curly double quotes U+201C/U+201D in `content7.py:81` (`Marco: “después de ~”. Pregunta: “〜 후에 뭐 해요?”`) — the on-disk #2 P7 SVG carried the same defect | Re-applied the core-style 「」 form `Marco: 「después de ~」. Pregunta: 「〜 후에 뭐 해요?」` post-apply, before building. Post-build sweep: U+201C = 0, U+201D = 0, U+2019 = 0 across all 8 SVGs + text.md; the 「」 form is visible in the P7 render and in text.md line 761. Only P7 changed vs #2 run 3 | ko3 run 1 |
| 5 | Independent reproof (2026-11-12): 6 exact-duplicate exercise slots (Q12/Q13/Q22/Q47/Q74/Q102), P1 lead sentence missing "다른 날의", P7 quote 6 translated as imperative, P1 top-strip slogan replaced | Q12/Q13/Q22/Q47/Q74/Q102 replaced with new questions from same-page article facts (P2 kimjang cost 13.4% below average, 6 kimjang ingredient types, chili powder -1.8%, P4 Samsung 9th title, P5 exam ticket by 8 a.m., P7 Kimchi Day fixed by law Feb 2020); P8 keys + reader notes updated; P1 sentence → "이번 주의 다른 날의 조치가 아니에요"; P7 quote 6 → past tense "Informó los resultados con los marcadores."; P1 top strip → "매주 한국어로 Un número cada semana 한국 사람이 읽는 한국어를 읽어요". Rebuilt + re-gated: TOTAL 150, p8 CLEAN, occlusion 0, spill/boxtitle/edge 0, textlayer PASS, text.md 455 items | fix rebuild 2026-11-12 |
| 6 | Independent reproof round 2 (2026-11-12, PROOF-NOTE-2): R2-1 text.md export drops 7 numbered items (P2 D Q26, P4 D Q61–Q63, P8 B Q121/Q126, P8 F Q142); R2-3 P2 band title `김장비용, 김치의 날` (comma) vs `김장비용과 김치의 날` (과) in the other 10 editions | R2-1: `textmd.py` global `seen` dedup replaced by per-call-site retention for `.ex`/`.match_set` items (plain prose keeps global dedup); text.md re-exported, 8 items restored per edition (7 numbered + P6 table row label `김장비용`, same root cause, verified against the print P6 table); per-page inventory 150/150, match terms 16/16 standalone, whole-book 150/150 R2-3: P2 band `김장비용, 김치의 날` → `김장비용과 김치의 날` (content12.py:166); rebuilt + re-gated: TOTAL 150, p8 CLEAN (keydiff [137, 138]), occlusion 0, spill 0 (358 OBSERVE), boxtitle 0 DEFECT (73 titles), edge 0/0, census PASS, quotes 0, textlayer PASS, print/web 8 pages each, P8 keys 150/150; P2 band now matches core; freeze baseline 7/8 (known P1 artefact, as round 1), freeze diff CJK +0, Latin 597 | fix rebuild 2, 2026-11-12 |

## Adjudicated (not defects)

- P8 match-item notes end with the option letter repeated (`25. d — … 199 456 wones d`): the letter is in the source note literal itself, core's own convention (`김장비용=四口之家199,456韩元 d` in core-ko); the es map translated the note text and kept the letter.
- #43/#123/#124 note "previsión de Weatheri": core's own rendering of 웨더아이 (private weather company, corrected in core run 4) — not a typo.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "(tarea abierta — texto modelo abajo)" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (es): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure).
- text.md 449 items vs core 452: three accounted drops, no content gap — (1) `is_prose` drops the bare 3-letter Latin word "Todo" (P1 contents 8면 row level; the SVG/PDF render "Todo" correctly, visible on the P1 render); (2) `lcn2` removed by design; (3) `lko` removed by design. Same pattern as en/de. (The #2 KIT recorded 332 vs 333 under the old textmd.py; the fixed re-export is 449 vs 452.)
- Freeze diff added CJK 7, all U+3000 (ideographic space, footer): same pattern as de-family Latin editions.
- P8 answer-note stem 10.35pt is the recorded core adjudication — not a defect, not changed.
- `text.md` contains `___` (23 places) — exported from the source literals, where blanks stay as `___`; the SVG/PDF render them as 1.1pt ink underlines. Same as core.
- P2 shopping box title `Lista de la compra` (385.8px) passes the 386.5px inner width by 0.7px — measured, kept; a future core change to that box would need re-measurement.

## Occlusion audit

- `tools/occlusion_audit.py` on `svg/` (ko3 run 1): **0 flags**. Selftest first: planted classes fired {BOXTITLE: 1, COVER: 1, EDGE: 1, FOOTER: 1, LINEX: 1, TEXTX: 1}; clean controls silent. Log at `hidden_files/w47/scratch-fanout-ko3/es/occlusion-es.log` (json `occlusion-es.json`).

## Mechanical gates (final state, ko3 run 1)

- `run.py` (build run 1, `/usr/bin/python3`): exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150 (A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2457, P7 teaser 2483.7). Log `hidden_files/w47/scratch-fanout-ko3/es/build-es-run1.log`; SVG hashes `es/sha-es-run1.txt` (only P7 changed vs #2 run 3 — the Frame 「」 fix; the other 7 SVGs byte-identical).
- `tools/freeze.py baseline` (**/usr/bin/python3**): **8/8 SVGs byte-identical**, tool self-reports 8/8 with per-file OK rows. Log `hidden_files/w47/scratch-fanout-ko3/es/freeze-es.log`; rebuild products deleted after the pass (log + json kept).
- `tools/freeze.py diff` (core-ko svg vs edition svg): TOTAL added CJK characters 7, all U+3000 (see Adjudicated). Log `es/freeze-diff-es.log`.
- `tools/p8.py extract` on `svg/p8-siheom.svg`: **noted set = 150 of 150** (parse: lines). Log `es/p8-extract-es.log`, json `es/p8-es.json`. `compare` vs core P8: **CLEAN** (missing=[] extra_count=0 keydiff=[137, 138]). Log `es/p8-compare-es.log`.
- `check_core.py` / `check_gloss.py` (scratch copies with ED + gloss prefix patched to the edition): **gloss fails 0, orphan issues 0**, phrases 8/8 verbatim (incl. the new phrase #7 with (1면)); dates all correct. Log `es/check-es.log`.
- Text layers: print and web PDFs each extract to **52,007 bytes, byte-identical** (`cmp` rc 0). Extracts `es/print-es.txt`, `es/web-es.txt`.
- P8 min font 9.975pt (PyMuPDF on the print PDF, P8 answers region y≥1302/2700: 172 spans, 167 at 9.975pt), ≥ 9.75pt. Log `es/p8font-es.log`.
- 150-key check (`keycheck-ko.py`, REG from edition sources vs keys extracted from P8 SVG): 149 exact + #150 `✓` (expected) = **150/150**. Log `es/keycheck-es.log`; full table in `es/EDITION-RECORD.md`.
- §1.1 grep audit: paper `#fbfaf6` 1×/page (P4/P6 4×, same as core — colour also used in table cells), VOL.4 correct on all pages, VOL.5 0 except P7 (2, by design), `·` counts identical to core page-by-page and only in gloss/option/credit contexts, colour set identical to core page-by-page. Log `es/style11-es.log`.
- Census (`census.py`, ex/match stems + D6 segments vs text.md): ex/match 166 items, 0 missing; D6 0 missing. Log `es/census-es.log`.
- Visual read: all 8 print pages at 100dpi, zero issues. PNGs in `hidden_files/w47/scratch-fanout-ko3/es/pages/`.

## Output files + sizes (final render, ko3 run 1)

- Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ko-es/`
- Print PDF: `Lucerna-VOL4-KO-ES.pdf` — **43,752,821 bytes**, 8 pages, SHA-256 `637bcb1b1b22a57f7167bdd9516c86dab89440a356f2187faf0e4ca5bbacd5d3` (fix rebuild 2026-11-12; fix rebuild 2, 2026-11-12; fix-1 value was 43,752,798 bytes / `709b794a694f…`; D5 value was 43,751,757 bytes / `8672ef924611…`)
- Web PDF: `Lucerna-VOL4-KO-ES-web.pdf` — **3,955,583 bytes** (< 7 MB), 8 pages, SHA-256 `e1ae9fcc033b58266bc9652b653ae27cbb56f396c477186a18d594c1cf9e09c9` (fix rebuild 2026-11-12; fix rebuild 2, 2026-11-12; fix-1 value was 3,955,564 bytes / `cb2f55019eee…`; D5 value was 3,952,529 bytes / `105856e3608c…`); pdftotext **52,070 bytes, byte-identical to the print PDF**.
- Text export: `2026-w47-ko-es.text.md` — 36,065 bytes, 8 pages, 463 items, SHA-256 `a24bd9ffaa097d529f6fc81b98748126ad1a471d44b9323ba3de15c8313f2b06` (exported from source via the fixed `textmd.py` (md5 `00d8f52d96ecad396cbc03603d98fa9b`), never from PDF; old #2: 26,696 B / 332 items, `ebac600a…` — the fixed re-export; re-exported 2026-11-12 (fix round 2, R2-1: textmd.py dedup fix, 8 items restored, 455→463 items))
- `ABSTRACT.txt`: one line, Spanish, no ASCII double quotes, 384 bytes, SHA-256 `383ccd7f7751d1701585eb271d507b5dd626173dca241d74c7bc8c81fb2c8cdf` (unchanged from #2). `Lucerna Korean Weekly VOL.4: la cuenta atrás del CSAT en D-3, el examen el 19 de noviembre, el Día del Kimchi el 22 de noviembre con un kimjang de 199 456 wones, el primer título de Samsung en la Serie Coreana en 12 años, más la inscripción al examen de historia y las hojas de finales de otoño — texto coreano con explicaciones en español, niveles A2 a B2, 150 ejercicios.`
- `WEEKLY-KIT.md`: this file. Build records: `hidden_files/w47/scratch-fanout-ko3/es/EDITION-RECORD.md`.

## Open verification debts (carried to the parent line)

- Independent proofread of this edition not yet done — to be assigned by the coordinator (proof1, separate person from the builder).
- Fact debts inherited from core-ko (see core KIT): no observed Naejangsan/Wolchulsan foliage peak announced at Nov 10 press time; HanNeungGeom details (other than date/time/fee) from secondaries; K League 35R scores not verified — not cited; WiKim Festival 2026 time/theme/session not found in an independent source (printed as scheduled).

## D5 rebuild (2026-11-12, SOP §1.1)

- Template: `mechanism/svglib-ko-d5.py` installed as edition `svglib.py` (`_D5_READER = "latin"`, reader es; diff vs template: 0 lines). Old svglib kept as `svglib.pre-d5` in the edition dir and in `hidden_files/w47/scratch-d5-ko/2026-w47-ko-es/pre/`.
- Build: `tools/venv/bin/python` throughout. `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Gates (all in `hidden_files/w47/scratch-d5-ko/2026-w47-ko-es/`): D5 census PASS (Latin 0 / Cyrillic 0 / curly-in-CJK 0); `census_quotes.py` 0 defective glyphs; `head_check.py` PASS 0 defects; `occlusion_audit.py` 0 flags; `p8.py extract` 150/150, `compare` vs core-ko CLEAN (keydiff=[137, 138], expected reader-language keys); `spill_sweep.py` 0 SPILL (358 OBSERVE); `boxtitle_check.py` 0 DEFECT (73 titles, 963 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` 0 absolute defects (ratios n=396 median 1.007 boldT 1.040 boldF 0.989; P8 218→217 lines, slack 60.0→75.5px); text layer print/web char-multiset diff 0 (23,556 = 23,556, pdftotext 51,910 bytes byte-identical).
- `freeze.py` (system python3 Pillow 10.2.0, coordinator-approved one-off exception): `diff` patched vs base-venv RC=0, added CJK 0 (Latin strings +598 from run splitting, expected). `baseline` 7/8 (P2–P8 OK; P1 differs): adjudicated interpreter artefact, same as core-ko — P1 text multiset identical (0 diff); only the big display "1" (185 vs 183pt) + knock-on x shifts. Production (venv, canonical) is self-consistent.
- Creambox "spill" flag adjudicated FALSE POSITIVE (not a defect, no content change made): the tool's spill check compares the patched line's y against the BASELINE box position, but the P6 gloss box moved down with the reflowed column (base box bottom 502.9 → patched box bottom 575.95); the gloss line (y 528.2) sits inside the patched box. Same defect class as ko-ru/ko-en, verified by SVG geometry (patched box x=989 y=460 h=115.95; line inside) and by the absolute check (patched lines vs patched boxes) at 0 defects.
- No content files changed. No true D5 defects in this edition.
