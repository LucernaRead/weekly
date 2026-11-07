# WEEKLY-KIT — Lucerna Weekly VOL.2, KO×DE (Korean target × German reader)

**Status: builder-complete only — NOT finalized. Pending independent proofread.**
**Issue week: Mon Nov 2 – Sun Nov 8, 2026. Masthead: `Lucerna` with no article (Korean takes none).**
**Delivery: `files/weekly-report-w45-ko-de/` — svg×8, cards×8, print PDF, web PDF, this KIT, ABSTRACT.txt.**
**Build tree: `hidden_files/weekly-report-w45-ko-de-build/` — `transform.py` (all fixes live here),
`orig/` (pristine core copies), `baselines/` (per-round pre/post sha256, never reset),
`audit_extra.py`, `spy_wrap.py`, `spy/` (wrap-spy scratch run), `scratch2/` (reproduction scratch run).**

## 1. Delivery files

| file | bytes | sha256 |
|---|---|---|
| Lucerna-VOL2.pdf (print, 8 pages) | 32,997,603 | `d60a7de2dca8c8e6a49f93095d7c4fc8a928b21ea79a5c9cecb0de0a0a5811c5` |
| Lucerna-VOL2-web.pdf (web, 8 pages, < 10 MB SOP target) | 3,546,997 | `2cbdd6355b613829af47f91118db89e2843bcdc3f3d7e91a01e606c65d316652` |

SVG sha256 (final, round 4):

| page | sha256 |
|---|---|
| p1-pyoji.svg | `46a6f85db8e52298d48afbee7d5bded45ab4080fd089ec7e578e1716cb45fa89` |
| p2-saenghwal.svg | `ffc3ec71b1c93a3f41aac4675ff5d9a97d3366a16cb4443b33c9d0959a79cb54` |
| p3-munhwa.svg | `377d4aef66f97a75384296b5b4d4505377a133c2e713f543bd8f58b543e534fd` |
| p4-seupocheu.svg | `6e6e192709883fbf232ecaf17ffcf9d7a178df9a57bcb873d5141dabb89c0c00` |
| p5-cheongnyeon.svg | `4f3962784e164e3ff8aedce8d08492191f0399acbb8c4a4ed97ffab082a02e33` |
| p6-gipi.svg | `7b02e35a604826b53be875df80ecc5e16f57058dd90633bb70971634bfdb469b` |
| p7-mal.svg | `a59318bd4f4ada2c2db090c0b11703420002d5f79cdc5ad26934311ee99cae90` |
| p8-siheom.svg | `c7e9bc4598c62b89cf732651e37354c714f944541634a06944cdc281bf918994` |

Card PNG sha256 (final): p1 `2144b1eddb96049b3813d3eef8e74c8502f56818573b177e9241bba4735a6102`,
p2 `534c496ebaea1e5030d1f83f125cab95c4dea6013dc8bc5a76e44622d12fb82d`,
p3 `251069b1c7986af70df5fa08769513708509fd04e8b9525722db6098c03bc76a`,
p4 `ee50cdf3228e5d8226d172185bb2197b7a6a5b479e0147301df6473eeef41912`,
p5 `75f261f717ce97baeeb732f24ec38da260eb3cdb39c6b6cb5fdf8af3d57b7d2f`,
p6 `32bbbc8107b7ebaf5b40285a8ebcf00cb0b069b6a029a1b35485cc3821444bee`,
p7 `2fe71c6957c27f5e79a0d666d52a91690cf153ec13ff9e320f7c39f47a9c2694`,
p8 `a6e707bdaa08f12d7cfaf325c27513c3577498d45e8371ecce0e88bfb67e7773`.

## 2. Toolchain (both interpreters recorded; audit measurements use the venv)

- `run.py`: tools venv Python 3.12.3, PIL 13.0.0. Verified: a scratch copy of the build tree
  (OUT redirected to scratch) run with the venv reproduces all 8 delivery SVGs byte-identically.
- `render.py`: tools venv Python 3.12.3, PIL 13.0.0, cairosvg 2.9.1 (system python3 has no
  cairosvg and was NOT used for rendering; system python3 is 3.12.3 with PIL 10.2.0).
- Canonical tools used: `freeze.py`, `p8.py`, `occlusion_audit.py`, plus the supplementary
  `audit_extra.py` (this build tree) for the advance-edge, frame-line, same-baseline,
  P6-label-coverage and Korean-orphan scans the canonical audit does not cover.

## 3. Core measured numbers (measured from the KO core on disk/render, never copied)

- VOL.2; page spec 1950×2700, 4 columns; masthead `Lucerna`, no article.
- Lead theme: Ipdong week — last foliage weekend, kimjang/winter-prep opening, CSAT countdown
  (D-17 on Nov 2 → D-12 on Nov 7; CSAT-day measures dated Nov 19 only, never this week).
- TOTAL 150 exercises; by page 10/18/18/18/18/18/12/38; by level A2 51 / B1 72 / B2 27;
  by type: sentence completion 48, multiple choice 52, vocabulary matching 16, cloze choice 13,
  sentence building 8, sentence transformation 4, true/false 4, translation 4, writing 1.
- P8: 38 items (A 8, B 8, C 4, D 4, E 4, F 4, G 5, H 1); P8 printed-note set 150/150;
  dash style `N. key — note`; group headings in Korean, `— 제N면 —`.
- Writing model: 157 characters with spaces excluded, printed instruction 150–200자.
  Model text begins `나의 겨울 준비는 김장부터 시작해요.` and is frozen verbatim.
- P7 structure: A2 입동의 말 / B1 날짜 세는 말 / B2 예보 읽는 법 columns (4 exercises each,
  12 total); error clinic ×4; frame `〜부터 〜까지` (산불조심기간 example); readers' corner with
  an editor's example letter plus disclosure; 8 phrases of the week, each verified verbatim
  against its tagged article page; VOL.3 teaser band.
- P7 phrase occurrence counts across the whole issue (including P7 itself):
  5 / 2 / 4 / 2 / 2 / 2 / 2 / 2 (see §8 for the phrases).
- Gloss inventory (rendered `gloss()`/`glossline()` strings split on `·`, tools README #21):
  content12 24, content34 26, content56 28, content7 6 — total 84 items.
- Footers (core, all 8 pages): left `Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY`,
  right `제 N 면 / 총 8 면`, baseline y=2624.
- Images per page (payload sha256 prefixes of base64): P1 1 (`535fff46b7ce`), P2 1
  (`e66d2b455ec6`), P3 2 (`e266b6ee1a87`, `5bea45d1f81e`), P4 1 (`1a7e7d6d5ffc`),
  P5 1 (`6a1bab177d54`), P6 0, P7 0, P8 0.
- svglib line-break rules (unchanged — target language unchanged): `NO_START` includes the KO
  core's own ASCII closer set, `NO_END = "「『（【〈《([{"`; greedy wrap, Latin words kept
  whole where possible, CJK per character, word-boundary preference when the fragment after
  the last space fits within 45% of max width, plus kinsoku oidashi (max 8 moves).
- Core SVG sha256 (verified unchanged after every round; final re-check §11):
  p1 `f1e6913d5fbcc0985fcf34f481814bb5756f3efc2aae29c1040ad9c85a1f9b5e`,
  p2 `839dcdd0ae4d603ff6ef4b786c6496f0f8f9263a061ccd2387d86f5e6b6509c1`,
  p3 `7437117949a3da0aad1d3084b6efed963687be1b8379ee93f27fd8991a899b34`,
  p4 `7f0aed9bec64dbb3f6596e1a20e7e815212706f417f565463624f2b9caad0902`,
  p5 `68e6ead94a42ec478633b1499889d8d71a28f03aca54b04264098bc561785ce9`,
  p6 `e7f53e421500d0a3a199b290c97b8fdd6ee7d425e92b1ebdfd8adb85af7ba39`,
  p7 `ddb4e76cf4e978156e04eb0ca86db7c4c237f3dd07feee36996314ec01db6594`,
  p8 `17031514098198758075ee9654f5cf179fa1767902002c1698c4b95a8b646401`.

## 4. Trend-first check (core theme is living seasonal/calendar heat, not commemoration)

Corroborated by public sources (Oct 2026): 산림청/국립수목원 Sep 22, 2026 forecast
(내장산 Nov 4, 월출산 Nov 9), Seoraksan actual observation Oct 16, and the 수능 Nov 19, 2026
plan released Oct 20 (10:00 work start, English listening 13:10–13:35). The core KIT's own
trend pool is `hidden_files/w45/trend-batch-C.md` (KO section) and its promises register is
`hidden_files/w45/w43-promises.md`.

## 5. Build method

Copy of the core build to the ko-de build tree; `transform.py` regenerates all build files from
`orig/` (pristine core copies) every round, repoints OUT/BASE to the DE edition directory, then
applies assertion-checked exact-literal replacements. All fixes go only into `transform.py`;
re-render is always single-process `run.py` followed by venv `render.py`. Registry `type`
arguments stay byte-identical (internal keys, W45 ES×DE precedent); only rendered strings
(instr, notes, heads, boxes, gloss, band lines) change. P8 answer-generation code is untouched.
Line-based/exact-literal splicing only (never AST byte offsets); f-string fragments get bare
text, never repr literals. No build-tree script was ever run in a way that writes back to the
delivery or core directories; registry-expansion re-runs were copied to scratch with OUT
redirected (see `spy/`, `scratch2/`).

## 6. Furniture three-way comparison (W45 core / W43 ko-de / this edition)

W43 same-pairing measurements win over README #20 generalization wherever they differ.
All W43 values below were measured from the shipped W43 ko-de files.

| slot | W45 core | W43 ko-de | this edition |
|---|---|---|---|
| subtitle y | 372 | 366 | 366 |
| badge | — | INSERTED y=394, 20pt bold BRICK `#a4553a`, advance 971.9 px | y=394, 20pt, weight 700, `#a4553a`, advance 971.90625 px — string verbatim from W43 |
| rules y | 392 / 401 | 412 / 421 | 412 / 421 |
| dark band rect y | 424 | 433 | 433 |
| band texts y | 478 / 522 | 487 / 531 | 487 / 531 |
| everything below y=606 | — | unmoved | unmoved |
| top strip German segment | — | `Jede Woche eine neue Ausgabe` | identical |
| footer | `Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY` | VOL.1 form | `Lucerna · KOREANISCHE WOCHENZEITUNG VOL.2 · TEXT AUF KOREANISCH · ERKLÄRUNGEN AUF DEUTSCH` |
| page line | `제 N 면 / 총 8 면` | `Seite N von 8` | `Seite N von 8` (all 8 pages, baseline 2624) |
| gloss prefix | — | `HINWEIS · ` | `HINWEIS · ` |
| band titles | 생활 / 문화 / 스포츠 / 청년 / 깊이 읽기 / 말 공부 / 시험과 답 | 생활 · Leben etc. | 생활 · Leben, 문화 · Kultur, 스포츠 · Sport, 청년 · Jugend, 깊이 읽기 · Vertiefung, 말 공부 · Sprache, 시험과 답 · Test und Antworten |
| exercise heads | 연습 | `연습 · Übungen Seite N` | `연습 · Übungen Seite N` |
| exercise right line | — | `Antworten auf Seite 8 · Niveaus können gemischt sein; nach Nummer suchen` | identical |
| P1 quiz right line | — | `Lesen Sie die Titelseite und wählen Sie die richtige Antwort · Antworten auf Seite 8` | identical |
| P8 header | 답 | `답 · Lösungen — nach Seiten geordnet; einfach die Nummer suchen` | identical |
| P8 header right line | — | `Jede Aufgabe mit kurzer Anmerkung · ✓ = Schreibaufgabe mit Mustertext` | identical |
| P8 band sub-line | `제8면 · 이번 주의 큰 시험 + 모든 답` | Korean-only | Korean-only (unchanged) |
| contents P8 level | 全部 | Alle | Alle |
| P7 band sub | — | `Drei Niveaus, drei Themen` | identical |
| P7 glossline format | — | `=` separator | `=` separator (e.g. `남다 = übrig bleiben · 바로 = genau, eben`) |
| German number formats | — | thousands with commas (551,864 / 1,312 / 3,271 / 27,000); decimal comma in prose (415,5 mm); `50 %` with a space | identical convention |
| instr labels | 填空 / 造句 / 翻译 / 写作 / 改写 / 把词和释义配对 / 把词和说明配对 / 把山和说明配对 | Ausfüllen / Sätze bilden / Übersetzen / Schreiben / Umformen / Wort–Bedeutung zuordnen / Paare zuordnen | identical mapping |

Badge string (verbatim, W43 ko-de):
`KOREANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`

## 7. Gates — measured values (final outputs)

### Freeze (core → edition, final run)
P1 +20/−19 strings, CJK 1462→1339; P2 +42/−39, 1612→1360; P3 +33/−31, 1524→1346;
P4 +27/−25, 1232→1074; P5 +36/−35, 1433→1234; P6 +21/−19, 1276→1136; P7 +39/−40, 1365→1037;
P8 +176/−169, 2496→1238. **TOTAL added CJK characters: 0 on every page.**
Baseline proof: `freeze.py baseline` on the unmodified core build reproduced all 8 core SVGs
byte-identically (8/8); the shipped core was re-hashed after every round and is unchanged (§11).

### P8 compare (explicit dual paths, `--total 150`)
Core 150 noted, edition 150 noted, status CLEAN, missing=[], extra_count=0,
keydiff=[109, 137, 138]. Adjudication of every keydiff item against the printed line:
- **137**: genuine E-redirect German key — printed `137. Der 7. November ist Ipdong.`,
  note `Siehe Seite 1`.
- **138**: genuine E-redirect German key — printed `138. Bis zur Suneung sind es noch 12 Tage.`,
  note `Siehe Seite 5`.
- **109**: documented `p8.py` paren-group artifact, FALSE POSITIVE — printed keys are
  byte-identical (`109. 기준` in both; core note `日期不同因标准不同（3版）`,
  edition note `Andere Daten, andere Kriterien (Seite 3)`); the trailing ASCII paren group
  `(Seite 3)` in the German note is pulled into the tool's key candidates, exactly as in the
  NL×DE precedent. Not a real key difference.
- #139/#140: no keydiff (Korean keys byte-identical); #150: apparatus line, not a keydiff.

### P8 note-completeness comparison (core vs edition numbered key lines 1–150)
- Identical numbered lines: **0**. Every core note is localized to German; no untranslated
  note survives.
- Identical non-numbered lines: only the 8 frozen Korean group headings (`— 제N면 —`) and
  frozen Korean stems/keys (including #139/#140 keys) — adjudicated individually, all frozen
  target-language text, not notes.
- Edition P8 key lines containing Han: 0 (Han in rendered DE text is 0 on ALL 8 pages).
- Core P8 notes are 150/150 with zero Korean note lines; core notes that mix a Korean headword
  with a gloss (e.g. `김장=腌过冬泡菜 a`, `이기다的过去式이겼어요`) keep the Korean headword
  with the gloss localized (e.g. `김장=Kimchi für den Winter a`, `이기다过去形이겼어요` →
  German gloss form). No separate Korean-note adjudication is needed beyond this rule.
- P8 top-section diff (y<1252, multiset) contains ONLY expected changes: band title German
  half, instr labels (造句×4→Sätze bilden, 翻译×4→Übersetzen, 写作→Schreiben,
  把词和释义配对→Wort–Bedeutung zuordnen), E stems 139/140 (German; #140 wraps to 2 lines),
  H glossline (German). No Korean stem changed.

### Canonical occlusion audit (`occlusion_audit.py`, path-parsing fix verified)
Selftest OK (all 6 planted classes fired, clean controls silent).
**Edition 0 flags; core 0 flags; NEW vs core 0.**

### Supplementary scans (`audit_extra.py`, venv PIL, 4× supersampled baseline-anchored ink)
- ADVANCE right-edge scan (inner frame x=1910): **0 flags**.
- Frame-line scan (every text ink box vs every rect border and line element; footer rule
  y=2580 vs footer baseline 2624 exempt by design): **0 flags**.
- Same-baseline scan (0.6 px tolerance, ink-interval overlap): **0 flags**.
- P6 table-label coverage vs later-drawn rects (true ink, gate <30%): all 12 labels **0.0%**,
  worst 0.0%.
- Korean orphan scan (wrap-spy log, 535 unique wrap records, 422 Korean-containing,
  818 lines, 396 junctions): line-start NO_START **0**, mid-word splits with ≥3-syllable tails
  **0**, mid-word splits with 1–2-syllable tails (info) **0** — all 396 junctions are
  word-boundary breaks; 0 walks broken. The wrap-spy ran ONLY in a scratch copy
  (`spy/`, OUT redirected); it never ran in the real build directory. Coverage includes
  reflowed Korean text (German gloss boxes shift subsequent Korean paragraphs between
  columns) and every Korean furniture string; the German explanation layer is not subject to
  the Korean scan. Note: this edition adds no new Korean furniture strings.
- P1 brief `(6면)` fragment check: renders on the sentence line
  (`11월 2일은 D-17, 7일은 D-12예요. (6면)`, y=2218.8) — the core round-2 fix is preserved.

### Geometry / flow (final run log)
Zero FLOW OVERFLOW / HEAD TOO WIDE (grep count 0). Flow ends: P1-headline 1413/1828,
P1-weekend 2094/2290, P1-quiz 2521/2540, P2-feature 1417/1540, P2-ex 2258/2580,
P3-feature 1290/1560, P3-ex 2095/2580, P4-feature 1022/1180, P4-ex 2002/2580,
P5-feature 1268/1560, P5-ex 2226/2580, P6-feature 1119/1180, P6-ex 2165/2580,
P7 columns 1062/1029/1059 (bottom 1560), P7 col3 ends 1709.94, **P7 teaser ends 2483.94
(< 2540)**, P8-ex 492/1252, **P8 key-flow ends col 3 y=2396 (< 2540)**; P8 key max baselines
per column 2514.9 / 2530.5 / 2530.3 / 2379.7 (all < 2540).

### Counts / images / phrases / gloss survival
- TOTAL 150; levels A2 51 / B1 72 / B2 27; pages 10/18/18/18/18/18/12/38; model 157 chars — all
  = core.
- Image payloads per page = core exactly (1/1/2/1/1/0/0/0 with matching hashes, §3).
- Phrase frequencies = core exactly (5/2/4/2/2/2/2/2).
- Gloss headwords: every Korean headword survives in the render (distinct-headword check
  80/80, 0 missing; occurrence count 84 by the split-on-`·` method).
- Banned intermediary term: **0 hits** in the rendered SVGs, the build code, ABSTRACT.txt,
  and this KIT (grep-verified after writing).

### Visual inspection
All 8 final cards viewed in full (p1–p8), not a subset. No overlaps, no cut-off text, no
misplaced boxes found. P7 readers'-corner solicitation sits inside its box with clear space
to the phrases rule below; P8 answer columns read cleanly to the footer rule.

## 8. P7 phrases and German translations

| Korean phrase (frozen) | German translation | tag |
|---|---|---|
| 11월 7일은 입동이에요 | Der 7. November ist Ipdong. | 1면 |
| 절정에 가까운 주말이라고만 말할 수 있어요 | Man kann nur sagen: ein Wochenende nahe dem Höhepunkt. | 1면 |
| 김장은 겨울 내내 먹는 김치를 담그는 일이에요 | Kimjang ist das Einlegen von Kimchi für den Winter. | 1면 |
| 수능까지 17일 남았어요. 오늘이 D-17예요 | Bis zur Suneung sind es noch 17 Tage. Heute ist D-17. | 2면 |
| 낮은 길은 더 늦게 물들어요 | Die tieferen Wege färben sich später. | 3면 |
| KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요 | Die KIA Tigers schlagen die LG Twins mit drei Siegen in Folge. | 4면 |
| 온 나라가 수험생을 응원해요 | Das ganze Land feuert die Prüflinge an. | 5면 |
| 날짜를 먼저 보세요 | Schau zuerst auf das Datum. | 6면 |

P7 target-language definition prose stays Korean verbatim; only the explanation layer is
localized (glosslines, clinic notes, frame note, letters notes, phrase translations).
P7 word-box definition sentences are NOT localized (DE-family freeze rule: DE×NL/DE×PT
established that localizing a P7 word-box definition sentence is a blocking freeze failure;
DE×EN/DE×ES/DE×IT keep the definition sentences verbatim — this edition does the same for
the Korean definition sentences). Korean instruction glosslines on P2–P6/P8 are reader-language
apparatus and become German (W43 ko-de / KO×EN precedent).

## 9. P7 readers' corner — ruling

- Korean example letter frozen verbatim (begins `안녕하세요. 저는 대학생이에요.`); no invented
  names, letters, or quotations.
- Disclosure apparatus replaced by German blocks (W43 ko-de precedent: disclosure apparatus
  replaced with German notes; forced by geometry — the core teaser ends at 2512.94 with only
  27.06 px headroom under 2540, so keeping the Korean disclosure plus a German one would push
  the teaser past 2540).
- Short note: `Beispiel der Redaktion, kein echter Brief.`
- Disclosure (contains all 3 facts + the VOL.3 promise):
  `Bis Redaktionsschluss kamen keine echten Briefe und keine besten Texte von Seite 8 an.
  Darum steht hier das Beispiel; unser Versprechen aus dem letzten Heft gilt für VOL.3.`
- Solicitation (imperative, verbatim):
  `Schreiben Sie uns Ihren Brief — und Ihren besten Text von Seite 8!`
- Scope ruling: the solicitation literally covers BOTH letters and best P8 texts, which
  exceeds the PT-family combination precedent (letters-only solicitation + deferring
  disclosure + teaser naming best p.8 texts ruled sufficient). The teaser line itself is NOT
  counted as a solicitation; the frozen Korean teaser body says
  `여러분의 편지와 8면 쓰기 우수작도 실어요` (your letters and the p.8 writing best works).
- Teaser title: `다음 주 · Nächste Woche (VOL.3)`; teaser body stays Korean.

## 10. P8 E-zone redirect (core KO↔ZH → this edition KO↔DE)

| # | stem | key | note |
|---|---|---|---|
| 137 | Korean (frozen) `11월 7일은 입동이에요. → ___` | German `Der 7. November ist Ipdong.` | `Siehe Seite 1` |
| 138 | Korean (frozen) `수능까지 12일 남았어요. → ___` | German `Bis zur Suneung sind es noch 12 Tage.` | `Siehe Seite 5` |
| 139 | German `Besondere Maßnahmen gelten nur am 19. November. → ___` | Korean byte-identical | `Siehe Seite 6` |
| 140 | German `Am Samstag fahre ich nach Naejangsan, um das Herbstlaub zu sehen. → ___` | Korean byte-identical | `Siehe Seite 3` |
| 150 | writing prompt (frozen) | `(offene Aufgabe — Mustertext unten)` | `Mustertext in Abschnitt H auf dieser Seite (157 Zeichen)` |

## 11. Rounds 1–4 fix log (baselines archived per round, never reset)

- Round 1 (initial render): print PDF 33,391,853 bytes; web PDF 3,546,501 bytes. The
  transform's final Han check then caught one missed literal (the short P8 variant
  `内藏山公团预报峰值11月11日`, distinct from the longer P3 variant with 公园）.
- Round 1 → 2 diff: ONLY p8 SVG, p8 card, both PDFs changed (the P8 note fix). Round 2 exposed
  `!! FLOW OVERFLOW [P1-headline] col 2 y=1743 need 99 bottom 1828`: the German P1 gloss box
  wrapped to 4 lines (core: 3), pushing the numbers box from column 1 to column 2 and driving
  the drills past the headline bottom into the row-B zone.
- Round 2 → 3 diff: ONLY p1 SVG, p1 card, both PDFs changed. Fix: P1 gloss shortened to
  exactly 3 wrap lines at 20.5pt/398px (verified with the build's own `wrap()`):
  `입동 = Ipdong, Winterbeginn · 절정 = Höhepunkt · 김장 = Winter-Kimchi · 상륙하다 = landen
  · 온대저기압 = Sturmtief.` P1-headline flow then ended col 2 y=1413, exactly the core value;
  zero FLOW OVERFLOW / HEAD TOO WIDE. Round 3 occlusion audit found 1 NEW flag: TEXTX on P1,
  `Ausgabe.` (second line of the German calendar line
  `Diese fünf Daten sind das Gerüst dieser Ausgabe.`) overprinting the fixed source line at
  gy+636 by 78.2×19.2 px — a real defect, since the core line fit on one line.
- Round 3 → 4 diff: ONLY p1 SVG, p1 card, both PDFs changed. Fix: calendar line shortened to
  one line at 18.5pt/390px, `Diese fünf Daten sind das Gerüst.` (the box context carries the
  rest; the Korean line above states it fully). Round 4: all gates in §7 pass.
- Baselines: `baselines/round-1-post.sha256`, `round-2-pre.sha256` (= round-1-post),
  `round-2-post.sha256`, `round-3-pre.sha256` (= round-2-post), `round-3-post.sha256`,
  `round-4-pre.sha256` (= round-3-post), `round-4-post.sha256`. Each round's pre-fix baseline
  was recorded in full (SVG + card + PDF sha256) before the fix.
- Core untouched: final core SVG hashes match the §3 record exactly (all 8 pages).
- Two transform pitfalls found and fixed (do not re-introduce): (a) Korean glosslines end
  with ASCII `.`, not `。` (14 literals corrected); the P7 lines with `。` are genuine and were
  left alone. (b) Korean `답` (U+B2F5) vs the look-alike character in the P8 header literal —
  the source uses Korean `답`. (c) Substring-order hazards in shared note pairs: the longer
  `特别…` form before the bare `措施…` form, the longer `KIA三连胜晋级` before bare `三连胜晋级`,
  and the parenthesized `日期不同因标准不同（3版）` before bare `日期不同因标准不同`; the
  transform asserts against the corresponding corruption patterns.

## 12. Image credits (Wikimedia Commons API Artist field, every image actually placed)

- P1 autumn.jpg — lumoplank, CC0 (file photo, not Seoraksan). Caption notes it is a file photo.
- P2 ssam.jpg — wizdata, CC0 (ssam vegetables, not a kimjang photo). Caption notes it is not
  a kimjang photo.
- P3 bukhansan-ui.jpg — Udonhan1992, CC0; apples.jpg — Cézanne, public domain.
- P4 baseball.jpg — Bain News Service, public domain (file photo).
- P5 study.jpg — Gary Todd, CC0 (file photo).
- P6/P7/P8 carry no photos. All captions carry the `자료 사진` (file photo) note where the
  image is a file photo.

## 13. Deviations from W43 ko-de (itemized)

1. VOL.1 → VOL.2 everywhere (footer, top strip, contents, P8 header context).
2. Issue week, dates, theme, phrases, model text, and image set are the W45 Ipdong week,
   not W43's week (all values in §3 are W45 measurements).
3. E-redirect item numbers and key wording are this issue's (137/138 German keys, §10);
   the redirect pattern itself is identical to W43 ko-de.
4. P8 keydiff includes #109, a paren-group artifact of the tool (false positive, §7);
   W43's run did not surface this item.
5. P1 calendar line shortened to one German line (round-4 fix, §11); W43 ko-de's calendar
   line needed no such fix.
6. P7 readers'-corner solicitation is a single imperative covering letters AND best P8 texts
   (§9); W43 ko-de replaced the disclosure apparatus with German notes without that combined
   imperative.
7. P1 gloss box is 3 lines in German (round-3 fix, §11); the W43 gloss box needed no
   re-shortening.
8. NOT deviations (verified identical to W43 ko-de): badge string and geometry, subtitle/rules/
   band geometry, footer/page-line wording pattern, gloss prefix, band-title pattern, exercise
   heads and right lines, P8 header and right line, contents P8 level `Alle`, P7 band sub,
   P7 glossline `=` format, German number formats, instr-label mapping, P8 band sub-line
   kept Korean-only.

## 14. Open items (for the parent line, not this builder)

- Independent proofread has not happened; this edition is builder-complete only.
- Repo insertion is the parent line's serialized step (blocked behind an unrelated push outage
  per the core KIT at build time); this builder did not insert, push, or post to Discord.
- Nothing was sent into the main chat; no cron was created; `weekly-git` was not touched.
