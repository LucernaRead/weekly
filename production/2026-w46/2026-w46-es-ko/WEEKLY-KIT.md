# WEEKLY-KIT · 2026-w46-es-ko — La Lucerna, Spanish Weekly VOL.3, explanations in Korean

Slug: `2026-w46-es-ko`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: Korean (해요체), written natively, no intermediate language.
Build dir: `hidden_files/weekly-report-w46-es-ko-build/` (copy of the W46 core build; transform tables `hidden_files/w46/t_ko.py` + `t_ko2.py`, applied by `hidden_files/w46/build_one.py`). SC face unchanged (W45 ES×KO precedent).

## 1. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-KO.pdf` 9,348,939 B (CJK font embedding); web PDF `La-Lucerna-VOL3-KO-web.pdf` 853,808 B (<7 MB), text layer 48,417 B via `pdftotext`, byte-identical to the print PDF's text.
`.text.md` exported from this edition's own SVG text layer (never from PDF).

## 2. Furniture (W45 ES×KO KIT §§4–5, VOL.1→VOL.3 only)

- Badge INSERTED at y=574, 22pt (tagline y=372 frozen Spanish): `스페인어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판`.
- Edition line: `스페인어 주간지 · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA`.
- Top strip: `CADA SEMANA EN ESPAÑOL · 매주 발행 · 스페인이 읽는 스페인어`.
- Band right: `29-N까지 20일 · 주택이 선거전을 결정해요` / `이번 호 헤드라인 · 2, 6면 참조`.
- Footer: `La Lucerna · 스페인어 주간지 VOL.3 · 텍스트는 스페인어 · 해설은 한국어` / `제 {n} 면 / 총 8 면`.
- Gloss prefix `해설 — `; `bridge()` kept.
- Bands: VIDA · 생활 / CULTURA · 문화 / DEPORTE · 스포츠 / JUVENTUD · 청소년 / A FONDO · 심층 / LENGUA · 언어 / EJERCICIOS Y RESPUESTAS · 연습과 답.
- Box titles: LA NOTICIA · 헤드라인, LA SEMANA EN CIFRAS · 이번 주 숫자, AHORA TÚ · 바로 연습해요, EN ESTA EDICIÓN · 이번 호 차례, BREVES · 단신, QUIZ RELÁMPAGO · 번개 퀴즈, EL CALENDARIO · 이번 주 일정, LOS DÍAS DE LA SEMANA · 날짜 말하기, EL PLAN DE LA SEMANA · 이번 주 계획 (tsize=20), ERRORES TÍPICOS · 자주 하는 실수 (20pt), LA PALABRA · 이번 주 단어, FRASES DE LA SEMANA · 이번 주 문장 (이번 호 글에서 그대로 뽑았어요), LA PRÓXIMA SEMANA · 다음 호 예고 (VOL.4).
- P8 header: `RESPUESTAS · 정답 — 면별로 나누어 실었어요, 번호로 찾으세요` + `문제마다 한국어 해설 한 줄 · ✓ 표시는 모범 답안 문제예요`; separator `— 제 {n} 면 —`; exercise right note `답은 8면에 · 문제는 급이 섞여 있어요, 번호로 찾으세요`.
- Type mapping 1:1: 문장 완성 48 · 객관식 47 · 빈칸 채우기 13 · 단어 짝짓기 12 · 문장 바꾸기 10 · 읽기 판단 8 · 문장 만들기 7 · 번역 4 · 쓰기 1. P8 check `== "쓰기"`.
- Instr: 填空→빈칸 채우기, 判断→참 / 거짓, 造句→문장 만들기, 改写→바꿔 쓰기, 翻译→번역, 写作→쓰기, 把词和释义配对→단어와 뜻 짝짓기; `原形` → `원형` (verified in the W45 KO build).
- Disclosure: `편집부 알림: 실제 편지와 8면 최고 글이 없어서 예시 편지를 실어요. 약속은 다음 호로 이어져요.` (shortened for fit — see §5; all facts kept).
- P8 re-aiming (W45 KO §4): keys 137/138 → Korean; notes 139/140 → Korean; key 150 note → `(열린 문제 — 모범 답안은 아래에 있어요)`, note → `모범 답안은 이 면 H 구역에 있어요 (84단어)`.

## 3. Registry verification & key-diff adjudication

`p8.py compare` vs core P8: CLEAN, 150/150, keydiff=[137, 138] (the two translation keys re-aimed to Korean; 150's note change is not visible to `p8.py compare` because writing items print `N. ✓ note`). `freeze.py diff` vs core SVGs: added CJK is all Hangul syllables (U+AC00–U+D7A3), Hanzi = 0, full-width parens = 0 (one known W45 adjudication pattern: an NFL token count shift from a P8 note rewrite does not affect the Spanish body).

## 4. Gates (final render)

- Builder self-check: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises; `p8.py extract` 150/150.
- `tools/occlusion_audit.py`: 0 flags (`hidden_files/w46/es-ko-occlusion.json`, selftest passed).
- Same-baseline furniture scan + chart GRAZE element-check (`hidden_files/w46/checks.py`): 7 rowcheck reports, all P1 contents-list 4.0px gaps — the core pattern, no overlap; chart 0 overlaps.
- Korean orphan scan (`hidden_files/w46/es_ko_orphan.py`, new for W46 — see §5): 0 reports; document-order and x-grouped implementations agree.
- Web PDF text layer: 48,417 B, identical to print text; <7 MB.
- Visual: P1, P7 inspected — badge clear of the band, top strip clear of the date line, A2 bridge wraps cleanly, letters box with disclosure inside, preview band clear of the footer rule.

## 5. Orphan scan + fixups (Korean apparatus only; core geometry and Spanish text untouched)

1. Orphan scan (S1 line-initial orphan punctuation/particle, S2 ≤2-syllable residue lines), implemented fresh for this family in `hidden_files/w46/es_ko_orphan.py` — no dedicated ES×KO scan script survives from W45, so the W45 dual-method scan was NOT reused; the new script implements both groupings (document-order runs vs x-grouped continuation detection, measurements with tools/venv PIL) and requires them to agree. First scan: 11 reports, all adjudicated real wrap defects (mid-word splits and lone-syllable tails produced by the wrapper's seam breaking). Fixes, all verified offline with the build's `wrap()` at the true draw widths before applying: P2 calendar parenthetical → `(자정 시작)`; P3 gloss reordered/shortened (veranillo gloss uses a comma, gaita/magosto glosses drop `예요`); P4 ¿Y TÚ? reworded; P4 bridge shortened (parenthetical dropped); P5 gloss shortened (`유권자 명부` → `명부`, jornada gloss shortened); P7 A2 bridge restructured twice (final: `요일과 월은 소문자로 써요. 날짜는 el miércoles 11 de noviembre, 1일은 el uno예요.`); P7 B2 bridge restructured with em-dash breaks; disclosure shortened (D1 form, §2); P8 notes for items 38/45/63/135 shortened (drop lone-syllable tails). Second scan after rebuild: 1 report (A2 bridge `은` orphan — the renderer's effective width runs ~10px over the offline 434px estimate, confirmed by ink measurement on the rendered card); fixed by the V4 restructure above. Final scan: 0 reports, groupings agree.
2. No P6/P8 size reductions were pre-applied for KO; none were needed (no overflows).
3. Core letters-box fix inherited via rebuild from the fixed core build.

## 6. Promises, sources, credits

As in the core: 13 Nov campaign start and 29 Nov vote lead the issue; the unverified 12 Nov decree date was NOT reintroduced; reader letters: labelled editor's example (Ana) + bilingual disclosure, promise carried to VOL.4, no reader fabricated. Sources, image credits and the full article record: see the core KIT `files/weekly-report-w46-es-core/WEEKLY-KIT.md`.

## 7. Reproduction

`python3 hidden_files/w46/build_one.py ko t_ko` (copies the fixed core build, applies `t_ko.py` + `t_ko2.py`, runs `run.py`, renders via `tools/venv`, gates freeze/p8/occlusion), then `tools/venv/bin/python hidden_files/w46/es_ko_orphan.py files/weekly-report-w46-es-ko/svg` (must print 0 reports). Gate outputs: `hidden_files/w46/es-ko-diff.json`, `es-ko-p8-compare.json`, `es-ko-occlusion.json`, `es-ko-build.log`; gate record in `hidden_files/w46/es-gates.log`. Independent proofread (§8.4 SOP) still outstanding — do not claim finalisation.

## 8. Fix record — Round 1 proofread defects D-2–D-5 (fix worker, 2026-11-02/03)

Four mid-word splits under the binding tools README #16 orphan standard (window 10–45, mid-word splits with ≥3-syllable tails, every prose column). All fixed AT THE SOURCE in the KO transform tables (no SVG/PDF hand-edit); the builder's narrower `es_ko_orphan.py` S1/S2 scan is NOT a complete orphan gate (Round 1 verdict) and was re-run only as a supplement.

- D-2 (P1 cifras box, `총|파업`): source `hidden_files/w46/t_ko.py` (cifras pair, content12.py). Before: `24 — horas dura la huelga general del miércoles 11 de noviembre (11월 11일 총파업은 24시간이에요)`. After: `24 — horas dura la huelga general del miércoles 11 de noviembre (11월 11일, 총파업 24시간이에요)`. Date (11월 11일), strike and 24 hours all preserved; the break now falls at the space after the comma and `총파업` stands whole on the last line. Verified visually on the KO P1 card.
- D-3 (P2 calendar, `세|스타오`): source `hidden_files/w46/t_ko.py` (calendar pair, content12.py). Before: `(토요일 세스타오에서 연방컵 결승)`. After: `(토요일에 세스타오에서 열리는 연방컵 결승)`. Saturday, Sestao and the Federation Cup final all preserved; `세스타오` stands whole at the start of the last line. Verified visually on the KO P2 card.
- D-4 (P4 exercise instruction, `채|우세요`): source `hidden_files/w46/t_ko.py` (content34.py bridge). Before: `괄호 안 단어의 비교급이나 -ísimo 형태로 빈칸을 채우세요.` After: `빈칸을 채우세요. 괄호 안 단어의 비교급이나 -ísimo 형태를 쓰세요.` Same instruction semantics in two sentences (fill the blanks; use the comparative / -ísimo form of the parenthesised word). Verified visually on the KO P4 card.
- D-5 (P5 exercise instruction, `나타|내세요`): source `hidden_files/w46/t_ko2.py` (content56.py bridge). Before: `ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’을 나타내세요.` After: `ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’이라는 뜻을 나타내세요.` All instruction elements preserved (ir a + infinitive, rewrite the sentences, express '~will'). Verified visually on the KO P5 card.
- Rewording method: candidate wordings were wrap-simulated offline with a verbatim copy of the build `svglib.py` wrap/measurement code (`hidden_files/w46/es-fix/sim_wrap.py`, `sim_candidates*.py`) and chosen so the wrap break falls at a space with the at-risk word whole; the rendered SVGs were then verified directly (line dumps + full-frame cards).
- Re-render: full rebuild via `python3 hidden_files/w46/build_one.py ko t_ko` from the fixed core build; 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises (A2 50 / B1 72 / B2 28; per page 10/18/18/18/18/18/12/38). SVG change isolation: only P1/P2/P4/P5 changed (sha256 changed); P3/P6/P7/P8 byte-identical to the pre-fix render.
- Re-gates (final artifacts): `tools/freeze.py diff` — added CJK all Hangul (3,506 chars), Hanzi 0; `tools/p8.py compare` — CLEAN, 150/150, keydiff=[137, 138] (adjudicated re-aiming, unchanged); `tools/occlusion_audit.py` — 0 flags, selftest OK; P6 re-wrap = reflow only (KO P6 removed set contains no Spanish exercise fragments; non-CJK word-multiset lost = only the replaced footer words); counts re-measured from SVGs 150 with the Round 1 stem sequences; same-baseline scan 0 reports.
- Full README #16 orphan scan (independent implementation, window 10–45, ≥3-syllable tails, all pages): 9 candidates, 0 TRUE splits. The 8 Round 1 false positives recur byte-identically (word-boundary breaks, adjudicated as such in Round 1 — see FIX-REPORT.md for the full list) plus 1 new candidate at the fixed D-3 site (`(토요일에` → `세스타오에서…`), adjudicated FALSE POSITIVE: the break falls at the space between the complete words `토요일에` and `세스타오에서` in the source string, i.e. a word-boundary wrap, not a mid-word split. Builder `es_ko_orphan.py`: 0 reports, groupings agree.
- PDFs: print `La-Lucerna-VOL3-KO.pdf` 9,349,457 B; web `La-Lucerna-VOL3-KO-web.pdf` 854,202 B (<7 MB) via `tools/webpdf.py`; `pdftotext` 48,448 B, byte-identical web vs print (`cmp` passed). `.text.md` regenerated with `hidden_files/w46/es_textmd.py` from the edition's own SVG text layer (48,561 B; diff vs pre-fix = exactly the 4 fixed passages; headers preserved verbatim).
- Gate outputs + build log + orphan scans: `hidden_files/w46/es-fix/`; fix report: `hidden_files/w46/es-fix/FIX-REPORT.md`. Round 2 independent proofread still outstanding — this record does not replace it. M-1 (KO P3 gloss separator) untouched per the fix brief. No other edition touched.
