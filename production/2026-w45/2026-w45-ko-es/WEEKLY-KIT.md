# WEEKLY-KIT — Lucerna Weekly VOL.2 · Korean target × Spanish readers (KO×ES)

**Status: builder-complete, NOT finalized.** Finalization is the independent proofreader's decision. This edition has NOT been posted to Discord, NOT sent to the main chat, and NOT inserted into the LucernaRead/weekly repo (repo insertion is the parent line's serialized step).

## 1. Edition identity

- Issue week: Monday Nov 2 – Sunday Nov 8, 2026; dated Monday Nov 2, 2026; VOL.2.
- Pairing: target language Korean × reader native language Spanish. Masthead `Lucerna` with NO article (Korean takes no article).
- Theme (frozen from the KO core): Ipdong week — last foliage weekend, kimjang / winter-prep season opening, CSAT countdown (D-17 on Nov 2 → D-12 on Nov 7; CSAT-day measures dated Nov 19 only, never this week).
- Delivery directory: `files/weekly-report-w45-ko-es/` — `svg/` ×8, `cards/` ×8, `Lucerna-VOL2-ES.pdf`, `Lucerna-VOL2-ES-web.pdf`, `WEEKLY-KIT.md` (this file), `ABSTRACT.txt`.
- Build tree: `hidden_files/weekly-report-w45-ko-es-build/` — `transform.py` (single source of all fixes), `orig/` (pristine core copies), `baselines/`, `run.py`, `render.py`, `audit_extra.py`, `occlusion.json`, `freeze-diff.json`, round logs, `spy/` (wrap-spy scratch, build-tree-local only).

## 2. Core numbers (measured from the W45 KO core on disk/render, 2026-10-27)

- TOTAL **150**; by page **10/18/18/18/18/18/12/38**; by level **A2 51 / B1 72 / B2 27**.
- By type: sentence completion 48, multiple choice 52, vocabulary matching 16, cloze choice 13, sentence building 8, sentence transformation 4, true/false 4, translation 4, writing 1.
- P8: 38 items — A timeline cloze 8, B general multiple choice 8, C mini-reading (Jimin story) + multiple choice 4, D sentence building 4, E translation 4 (both directions), F vocabulary matching 4, G dialogue cloze 5, H writing 1 on `나의 겨울 준비`; dash style (`N. key — note`); printed-note set 150/150 (core and edition).
- Writing model: **157 characters excluding spaces** (printed instruction 150–200자), frozen verbatim, begins `나의 겨울 준비는 김장부터 시작해요.`
- P7 structure: A2 `입동의 말`, B1 `날짜 세는 말`, B2 `예보 읽는 법`; error clinic ×4; frame `〜부터 〜까지` (fire-prevention-period example); readers' corner with editor's example letter + Korean+Spanish on-page disclosure; 8 phrases of the week; VOL.3 preview (teaser).
- Gloss: 84 `·`-split items (content12 24 / content34 26 / content56 28 / content7 6), plus 1 f-string writing glossline in content8 (no `·`) = 85 counted strings; edition = core exactly, per file.
- Images per page: **1/1/2/1/1/0/0/0** (see §8).
- Core SVG SHA-256 (verified unchanged after every round, final re-hash 2026-10-27): p1 `f1e6913d5fbcc0985fcf34f481814bb5756f3efc2aae29c1040ad9c85a1f9b5e`, p2 `839dcdd0ae4d603ff6ef4b786c6496f0f8f9263a061ccd2387d86f5e6b6509c1`, p3 `7437117949a3da0aad1d3084b6efed963687be1b8379ee93f27fd8991a899b34`, p4 `7f0aed9bec64dbb3f6596e1a20e7e815212706f417f565463624f2b9caad0902`, p5 `68e6ead94a42ec478633b1499889d8d71a28f03aca54b04264098bc561785ce9`, p6 `e7f53e421500d0a3a199b290c97b8fdd6ee7d425e92b1ebdfd8adb85af7ba39a`, p7 `ddb4e76cf4e978156e04eb0ca86db7c4c237f3dd07feee36996314ec01db6594`, p8 `17031514098198758075ee9654f5cf179fa1767902002c1698c4b95a8b646401`. Core print PDF 33,125,291 bytes, web PDF 3,366,637 bytes. No writes were made to the core dir, W43 dirs, `weekly-git`, or shared scratch.

## 3. Build method + interpreters

- Single-process re-render through the build's driver (tools README #7): `tools/venv/bin/python run.py` then `tools/venv/bin/python render.py`. Content modules were never imported inside the core build directory (#11); comparisons were made only via copies with OUT repointed, and the wrap-spy run used a scratch copy inside the build tree only.
- `transform.py` is the single source: 258 MAP entries, all applied with count > 0. Every fix-round edit went into it; a full pre-fix SHA-256 baseline of SVG/cards/PDFs was saved before each round (`baselines/round1-post`, `round2-pre/post`, `round3-pre/post`, `round4-pre`, `round5-pre`, `round6-pre`, `round7-pre`, `final-sha256.txt`).
- Interpreters (2026-10-27): venv Python **3.12.3, PIL 13.0.0, cairosvg 2.9.1** — used for both `run.py` and `render.py`; audit measurements use venv PIL. System python3 (3.12.3, PIL 10.2.0, no cairosvg) was never used for rendering.
- SVG output is deterministic across runs (verified: two consecutive `run.py` runs produce identical SVG hashes; `final-sha256.txt` matches the delivered files).

## 4. Furniture — three-way table (W45 core / W43 ko-es / this edition)

| Item | W45 core | W43 ko-es (measured from shipped files) | This edition (measured from render) |
|---|---|---|---|
| Badge (P1 masthead) | none (Korean-only masthead) | `TEXTOS EN COREANO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`, y=394, 20pt, weight-700, BRICK `#a4553a`, centered x=975 | identical string, y=394, 20pt, BRICK, x=975 |
| Subtitle / rules / dark band / band lines | subtitle y=372, rules 392/401, band y=424, band lines 478/522 | subtitle 366, rules 412/421, band 433, band lines 487/531 (subtitle −6, rules +20, band +9, band lines +9) | same as W43 ko-es (subtitle −6, rules +20, band +9, band lines +9); headline block and everything below y=606 unmoved |
| Footer (all 8 pages, baseline 2624) | Korean form | `Lucerna · SEMANARIO COREANO VOL.1 · TEXTO EN COREANO · EXPLICACIONES EN ESPAÑOL` | `Lucerna · SEMANARIO COREANO VOL.2 · TEXTO EN COREANO · EXPLICACIONES EN ESPAÑOL` (1 per page, all 8 pages) |
| Page line (baseline 2624, right) | `제 N 면 / 총 8 면` | `Página N de 8` | `Página N de 8` (all 8 pages; this was caught late — see §10, round 7) |
| P1 edition line | Korean | `SEMANARIO COREANO · VOL.1 · …` | `SEMANARIO COREANO · VOL.2 · 입동 · 단풍 · 김장` |
| Top strip | Korean | `매주 한국어로 · Cada semana · 한국 사람이 읽는 한국어를 읽어요` | identical |
| Band titles | Korean only | 생활·Vida cotidiana, 문화·Cultura, 스포츠·Deportes, 청년·Juventud, 깊이 읽기·Lectura profunda, 말 공부·Lengua, 시험과 답·Test y respuestas; P8 band subtitle stays Korean-only | identical |
| Exercise heads | Korean | `연습 · Ejercicios pág. N`; right line `Respuestas en la pág. 8 · Los ejercicios mezclan niveles: busca por número`; section heads stay Korean; glossline instruction lines in Spanish | identical |
| Type labels | Korean | Completar, Opción múltiple, Emparejar, Texto con huecos, Formar una frase, Transformación, Verdadero o falso, Traducción, Redacción | identical |
| Instr labels | Korean | Completa, Forma la frase, Traduce, Escribe, Reescribe, Relaciona | identical |
| P8 header | Korean | `답 · Respuestas — ordenadas por página, busca el número`; right line `Cada respuesta con una nota breve en español · ✓ = ejercicio con modelo`; separators stay Korean (`— 제N면 —`); contents P8 level `Todos` | identical |
| P7 titles | Korean | `실수 병원 · La clínica de errores`, `이번 주의 틀 · La frase modelo`, `독자의 편지 · Cartas de los lectores`, `이번 주의 문장 · Frases de la semana (textuales, de este número)`, teaser title `다음 주 · La semana que viene (VOL.3)` with teaser body staying Korean | identical |
| Gloss prefix | `译注｜` | `Nota — ` (method names kept as `gloss()`/`glossline()` in this build; rendered output is what matters) | identical |
| Image captions/credits | Korean | stay Korean (e.g. `사진: … — CC0 (Wikimedia Commons) · 자료 사진`) | identical |
| Bylines / VOL line / dates | Korean | stay Korean (`Lucerna 편집부 · 읽기 레벨: A2`, `VOL. 1 · 제1호`, Korean date range) | stay Korean (VOL.2 form) |

## 5. Gate measurements (final render, round 7)

- **Counts**: TOTAL 150; page distribution 10/18/18/18/18/18/12/38 = core; levels A2 51 / B1 72 / B2 27 = core; types = core; model essay verbatim = core (157 chars excl. spaces).
- **Flow ends** (run log, all inside bottoms): P1-headline 1413/1828, P1-weekend 2094/2290, P1-quiz 2521/2540, P2-feature 1417/1540, P2-ex 2258/2580, P3-feature 1290/1560, P3-ex 2234/2580, P4-feature 1022/1180, P4-ex 2002/2580, P5-feature 1268/1560, P5-ex 2226/2580, P6-feature 1119/1180, P6-ex 2283/2580, P7 columns 1092/1029/1059 (bottom 1560), P7 teaser **2522.94** (<2540, 17.06px headroom), P8-ex 463/1252, P8-keys 2382/2540; P8 keys max baseline 2514.92 (<2540).
- **Canonical occlusion audit** (`tools/occlusion_audit.py`): selftest OK (all 6 planted classes fire, clean controls silent); edition **0 flags**, core **0 flags**, NEW vs core **0**.
- **Supplementary audit** (`build/audit_extra.py`, venv PIL): full-page right-edge scan (inner frame x=1910) **0** on all 8 pages, edition and core; full-page frame-line scan **0** on all 8 pages, edition and core; same-baseline ink collisions **0** on all 8 pages, edition and core (0.6px tolerance, ink-interval overlap). P6 chart-label baseline-anchored ink coverage (getmetrics method): **0.0% for all 12 labels**, edition and core — gate <30% passed.
- **Korean orphan scan** (wrap-spy run in a build-tree-local scratch copy, 535 unique wrap records): definition — window 10–45 with the ≥3-syllable-tail standard applied to ALL prose columns (calendar, plan, ¿Y TÚ?, cifras boxes, etc.; the retired "first segment ≤ 1 syllable" criterion was not used); checks: line-start characters in `NO_START` (including ASCII closers `)]}〉》.,!?%:;"`), line-start orphan punctuation (mirror defect), mid-word splits whose continuation tail has ≥3 Hangul syllables (source eojeol vocabulary from the build source, Spanish explanation layer excluded, Korean furniture strings included), and parenthesised final-line fragments. Result: **line-start NO_START 0, mid-word splits ≥3-syllable tail 0, 1–2-syllable tail 0**; one lone parenthesised fragment `1,620명)` adjudicated NON-defect — it is the frozen P5 cifras-box line `3,271명 — 서울시 할로윈 안전 인력 (이태원 1,620명)` wrapping at a natural break, at identical coordinates (y=1398.55) in core and edition, a complete parenthesised number token (1-syllable tail by the ≥3 rule), not a split word.
- **Freeze diff** (`tools/freeze.py diff`, core vs edition): p1 +20/−19, p2 +43/−38, p3 +33/−30, p4 +27/−24, p5 +36/−34, p6 +23/−18, p7 +35/−35, p8 +171/−168 strings; added CJK characters **0 on p1–p7, 1 on p8** — the single added Hangul syllable `절` is the headword citation in item 104's note (`절기 = las 24 divisiones del año`, core note was Chinese-only `节气＝一年24个时节`); legitimate per the ko-target adjudication class, not new target text.
- **P8** (`tools/p8.py`, OLD version — see §6): `extract --total 150` gives noted set **150/150** for both core and edition; `compare` with explicit dual paths (`--core-p8 …/ko-core/svg/p8-siheom.svg --edition-p8 …/ko-es/svg/p8-siheom.svg --total 150`): **CLEAN, missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]**. Item 109 adjudicated from its printed line: keys byte-identical (`기준`), note localized (`Las fechas difieren porque los criterios difieren (pág. 3)`) — no 109-style artefact in this edition. P8 notes are purely Spanish (cross-family residue is a blocking item; none found). Edition P8 key lines contain no Han characters (rendered Han = 0 across all 8 pages).
- **Rendered-text checks**: Han (U+4E00–U+9FFF) in text nodes **0** on all 8 pages (Hangul is expected and is not Han); ASCII double-quote characters **0**; banned intermediary term **0** in SVGs, build code (`transform.py`, `bslib4.py`, all `content*.py`, `run.py`, `render.py`, `svglib.py`), `ABSTRACT.txt`, and this KIT — checked in Chinese, English, and Spanish forms.
- **Gloss verification**: per-file rendered `·`-split counts edition = core (24/26/28/6, total 84); every edition gloss string present in its rendered page text (spaceless substring check, **0 missing**).
- **Phrase verification**: all 8 P7 phrases verbatim contiguous against their tagged article pages in this edition; whole-issue frequencies edition = core = **5/2/4/2/2/2/2/2**; all 8 Spanish translations present on P7 with Korean tags kept (e.g. `(1면)`).
- **E-zone** (verified from the core's content8 order: A 113–120, B 121–128, C 129–132, D 133–136, E 137–140, F 141–144, G 145–149, H 150): 137 stem Korean frozen → key `El 7 de noviembre es Ipdong.`, note `Compara con la pág. 1`; 138 stem Korean frozen → key `Quedan 12 días para el examen.`, note `Compara con la pág. 5`; 139 stem → Spanish `Las medidas especiales solo se aplican el 19 de noviembre. → ___`, key Korean byte-identical, note `Compara con la pág. 6`; 140 stem → Spanish `El sábado voy a Naejangsan a ver el follaje. → ___`, key Korean byte-identical, note `Compara con la pág. 3`; 150 key `(pregunta abierta — modelo a continuación)` replaced by the shorter `✓ El modelo está en la sección H (157 caracteres)` to save one P8 key line (rendered key line: `150. ✓ El modelo está en la sección H (157 caracteres)`).
- **P7 readers' corner**: labelled editor's example (`Ejemplo editorial, no una carta real.`); Korean disclosure frozen; Spanish disclosure + imperative: `Sin cartas reales ni mejores textos de la pág. 8, la promesa pasa al VOL.3. ¡Envíanos tu carta · tu texto destacado!` — covers no real letters, no best P8 texts, VOL.3 promise, and an imperative covering both letters and P8 writing. Teaser lines, content-preview lines, and other-page exercise prompts were NOT counted as solicitation. VOL.3 preview and readers'-corner promises must be kept for next issue.
- **Visual**: all 8 final cards (p1–p8) viewed; **zero defects** (no overlaps, no clipped text, no missing images, footers/page lines correct on every page).
- **PDFs**: print `Lucerna-VOL2-ES.pdf` **32,555,388 bytes, 8 pages**, SHA-256 `d8ccaea5ff50559b060d79c27bf2d8d26a63103fb613eb0c78f5b0597040c8fe`; web `Lucerna-VOL2-ES-web.pdf` **3,579,175 bytes, 8 pages (<10 MB)**, SHA-256 `8eea982b0ec3a86db23afc252edb71a82a380f6a9bb6fc6eacbe2919068242eb`. Full SHA-256 of final `svg/`×8, `cards/`×8, and both PDFs: `build/baselines/final-sha256.txt` (18 lines, verified to match the delivered files).

## 6. Tool versions

- `tools/p8.py` is the **verified OLD version**, SHA-256 `67df05f1bc7234eeb48d25fff2cb85a406e8bfcd6b211b9fdc76231b6296c132` (recorded 2026-10-27). Its old keydiff may contain 109-style parenthesis/dash artefacts, so every keydiff was adjudicated from the printed lines, never from tool output alone. The newer file `hidden_files/w45/p8-dash-fix-verify/p8.py.new` (SHA-256 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b274627003d8226815046eccc0ca9`, verified TRUSTED) was NOT adopted — adoption is deferred; `tools/` was not replaced.
- Canonical `tools/occlusion_audit.py` (selftest OK, see §5). Supplementary scans: `build/audit_extra.py` (venv PIL).

## 7. Translation decisions of note

- Spanish number style follows W43: thousands with `.` (551.864, 1.312, 3.271, 27.000), decimal comma in prose (415,5 mm).
- P1 band right lines: `IPDONG` / `Ipdong, el 7 de noviembre · comienza la temporada de kimjang`. P1 practice head: `지금 바로 연습 · Práctica inmediata` (no HEAD TOO WIDE warning).
- P1 gloss: `kimchi de invierno` → `kimchi invernal` (see §10, round 3) so the gloss fits 3 lines including the `Nota — ` prefix while keeping full `ciclón extratropical`.
- P7 phrases' Spanish translations: `El 7 de noviembre es Ipdong.` / `Solo puede decirse: un fin de semana cercano al apogeo.` / `Kimjang es hacer el kimchi de todo el invierno.` / `Quedan 17 días para el examen; hoy es D-17.` / `Los caminos bajos se tiñen más tarde.` / `KIA Tigers venció a LG Twins por tres victorias seguidas.` / `Todo el país anima a los candidatos.` / `Mira primero la fecha.` (tags kept Korean).
- Clinic example spelling: the correct past form is `담갔어요` (final entry: `El pasado de «담그다» es «담갔어요».`).

## 8. Images (only clearly public-domain/CC0; credit lines verbatim from the Wikimedia Commons API Artist field)

| Page | File / credit (as printed) | Payload SHA-256 (base64 text) | Decoded-JPEG SHA-256 |
|---|---|---|---|
| P1 | autumn.jpg — lumoplank, CC0 | `535fff46b7ce…` | `6f7f33ed8f40…` |
| P2 | ssam.jpg — wizdata, CC0 (ssam vegetables, explicitly not a kimjang photo; captioned honestly) | `e66d2b455ec6…` | `96a6a19b612a…` |
| P3 | bukhansan-ui.jpg — Udonhan1992, CC0 | `e266b6ee1a87…` | `158ea3a0e81f…` |
| P3 | apples.jpg — Cézanne, public domain | `5bea45d1f81e…` | `214cc390ac7c…` |
| P4 | baseball.jpg — Bain News Service, public domain | `1a7e7d6d5ffc…` | `18ad8ae06fac…` |
| P5 | study.jpg — Gary Todd, CC0 | `6a1bab177d54…` | `35e7dc69d417…` |
| P6/P7/P8 | none | — | — |

Payload hashes are identical between edition and core for every page, in both calibres (base64 text vs decoded JPEG); pattern 1/1/2/1/1/0/0/0 = core. Every credited image is verified as actually placed.

## 9. W43 deviations (this edition vs W43 ko-es, itemized)

1. VOL.2 throughout (footer, edition line) vs W43's VOL.1 — required by the issue, not a defect.
2. Page line fixed in round 7: the first six rounds shipped Korean page lines (`제 N 면 / 총 8 면`) because the f-string was not in the MAP; final render has `Página N de 8` on all 8 pages, matching W43.
3. `이번 주의 말` subtitle: this edition `Palabra de la semana` vs W43 `La palabra de la semana` — a wording variant (both grammatical Spanish), not a furniture-measurement deviation.
4. Method-name difference (no rendered effect): this build keeps `gloss()`/`glossline()` names; W43 renamed them to `expl()`. Rendered output (prefix `Nota — `) is identical.
5. Letters-box `lh` slack +39 over the original formula (see §10, round 6) — a Spanish-descender accommodation, not present in W43 (W43's disclosure text did not end on a `¡` line).
6. P8 key 150 shortened to `✓ El modelo está en la sección H (157 caracteres)` (W43's form was longer) — saves one P8 key line.
7. E-zone re-aim item numbers are 137/138, verified from this edition's core render (they happen to match ko-en/ko-de, but were not copied from them).

## 10. Round-by-round fix log

- **Round 1**: TOTAL 150, levels/pages/types = core, but three overflows: P1-headline FLOW OVERFLOW (ends col 2 y=1942 vs bottom 1828), P7 teaser ends 2655.46 (>2540), P8-keys overflow (ends 2585). PDFs: print 32,557,462 bytes, web 3,584,151 bytes. Baseline `baselines/round1-post.sha256` (= `round2-pre.sha256`).
- **Round 2**: 26 edits — P7 clinic/frame/short-note/disclosure shortenings + P8 key-note shortenings (each verified to 1 rendered line with its printed prefix). Result: P7 teaser 2512.94, P8-keys end 2382, but P1-headline overflow unchanged (identical y=1743/need 99).
- **Round 3**: root cause found — the P1 gloss wrapped to 4 lines **including the `Nota — ` prefix** (the prefix-free test had shown 3 lines). Changed `kimchi de invierno` → `kimchi invernal`, giving 3 lines with prefix while keeping full `ciclón extratropical`. Result: **zero FLOW OVERFLOW / HEAD TOO WIDE**; P1-headline ends col 2 y=1413 = core value exactly. Baseline `baselines/round3-post.sha256`.
- **Round 3 audit**: canonical audit selftest OK but edition had **2 NEW flags**, both P7 letters box: LINEX (phrases-section gold rule crossing the disclosure's last-line ink) and BOXTITLE (disclosure line-3 ink bottom 1740.2 > box border 1738.9).
- **Rounds 4–5**: disclosure shortened 4→3 lines, clinic item 3 → `El número va separado.`, frame note → `«desde ~ hasta ~»: «〜부터 〜까지예요?»` (1 line), short note → `Ejemplo editorial, no una carta real.` (1 line), letters-box `lh` slack +29 (formula trailing +26 → +55), solicitation comma → `·`. Result: LINEX cleared, but **1 BOXTITLE remained** (last-line ink bottom 1740.0 > border 1738.9, identical after the comma change — proving the comma was not the cause).
- **Diagnosis**: PIL measurement at size 80 with NotoSansCJK-Regular.ttc KR face: the glyph `¡` itself has bbox bottom 110 vs baseline ≈93–94, i.e. it dips **17px at size 80 = 4.3px at 20pt** below the baseline (1735.7 + 4.3 = 1740.0). Any last line containing `¡` therefore straddles a border sitting only 3.24px below its baseline.
- **Round 6**: letters-box slack +55 → **+65** (i.e. +39 over the original formula's +26). Result: canonical audit 0 flags edition, 0 core, 0 NEW; P7 teaser 2522.94; box-to-phrases-rule gap stays 30px as in the core. PDFs: print 32,557,288 bytes, web 3,579,500 bytes.
- **Round 7 (final)**: page-line mapping added (`제 {n} 면 / 총 {total} 면` → `Página {n} de {total}`) after the footer audit caught Korean page lines on all 8 pages. All gates re-run on the final render: canonical audit 0/0/0, supplementary scans 0, flow ends unchanged from round 6, PDFs as in §5. Baseline `baselines/round7-pre.sha256` (pre-fix state); `baselines/final-sha256.txt` refreshed to the final files.

## 11. Transform pitfalls found and fixed (do not re-introduce)

- Substring-order hazards (fixed by longest-first ordering or quoted-context replacements): P3 note `现场庆典11月4日起` is a substring of P8 note `青松现场庆典11月4日起` (quoted-context P3 entry); P6 judgment note `特别措施只适用于11月19日` vs the P8 E stem `特别措施只适用于11月19日。→ ___` (stem first, then bare long form, then short form `措施只适用于11月19日`); P7 note `日期不同因标准不同（3版）` before P8 short form `日期不同因标准不同`, while P3's distinct form is `日期不同因为标准不同`; P8 short variants distinct from longer forms (ko-de KIT §11 pitfall class): `内藏山公团预报峰值11月11日` (no 公园）, `月出山林业厅预报峰值11月9日`, `首尔报名窗口10点至12点` (no date, 至 form); `KIA三连胜晋级` before bare `三连胜晋级`.
- A round-2 edit that shortened the P6 judgment note also matched inside the E-stem translation string (×2 occurrence); fixed with a restore entry that returns the E stem to its full sentence form after the note shortening.
- A generated STRUCT block for content7 broke transform.py syntax (nested double quotes + a placeholder collision producing `+ 26_NEW`); rewritten with a single-quoted short anchor on the `lcn2` wrap fragment. Transform.py syntax is verified OK and the run passes.
- Value-map replacements on f-string fragments use bare text, never repr literals, and per-page stray-quote counts were asserted after AST transforms (tools README #18); transforms splice on whole lines or exact unique literals with assertions, never AST byte offsets into UTF-8 source (#17).

## 12. Open items for the parent line

- **Independent proofread has not happened.** This KIT certifies builder-complete only; the proofread-until-zero-problems gate is the proofreader's, not the builder's.
- **Repo insertion is the parent line's serialized step** — not attempted here.
- **Inherited core verification debts** (from the core KIT, not re-verified by this builder): Korean Series Nov 2 start may shift after the playoff rain delay (issue uses `발표된` wording + press-time note); playoff G1 (Oct 26) result unknown at the Oct 26 research cutoff (no score printed); Champi "latest warning record" formal status unconfirmed (claim omitted); Ipdong Nov 7 / Soseol Nov 22 from calendar-blog sources, KASI official page not retrieved; Han History exam details from secondaries citing the Oct 19, 2026 notice, primary page not directly retrieved; Commons image shortfall (no verified PD/CC0 Korean foliage, kimjang-making, or Korean-student-studying shot; ssam photo captioned honestly as ssam, not kimjang).
- No international politics in this edition; Korean domestic politics (CSAT measures, exam administration) is within the standing rule.
