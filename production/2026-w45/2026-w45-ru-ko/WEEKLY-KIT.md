# WEEKLY-KIT — Lucerna Russian Weekly, VOL.2 · RU × KO (W45)

**Edition:** Russian target text × Korean explanations (target RU × reader-native KO),
for Korean-speaking learners of Russian.
**Week:** Monday 2 – Sunday 8 November 2026 (VOL.2, same issue week as the finalized W45 core).
**Masthead:** **Lucerna** (no article — Russian is article-less).
**Status: FIX-ROUND COMPLETE (2026-10-27, see §17), NOT independently proofread — a fresh full independent proofread is still required (SOP §8.4); this fix round is NOT a finalization.** No Discord post, no chat
card/PDF dump, no repo push, no cron was made from this build. The weekly-git checkout
was not touched. Independent proofread is the parent's next step.

**Source:** the finalized W45 Russian core (`files/weekly-report-w45-ru-core/`, itself the
zh-cn edition). Build copied to `hidden_files/weekly-report-w45-ru-ko-build/`; the core's
own directories were never edited. Method = the W43 RU×KO sibling pattern: rewrite the
explanation layer only, freeze everything Russian. Transform script (exact-literal
replacements, asserted per string): `tools/scratch/transform-w45-ru-ko.py`. The
explanation-layer function follows the W43 RU×KO precedent (`expl()`, 1 definition +
all call sites). The Korean layer is written directly against the Russian original
(headwords, stems, notes); the core's explanation strings serve only as search
patterns inside the transform script, confined there.

---

## 1. Deliverables (measured on disk)

| File | Bytes | SHA-256 |
|---|---|---|
| Lucerna-VOL2-KO.pdf (print, 8 pages) | 15,078,056 | 6f21c3217ac2fdc6b38850c7ffc949d871954007d3ab0bde8b38fddcdb59a878 |
| Lucerna-VOL2-KO-web.pdf (web, 8 pages, < 10 MB) | 3,090,198 | c8d333abeb734480249ae62ac47293f5d3ca04a6391720bb458f8efab0b05016 |
| svg/ × 8 | p1 976,160 · p2 31,459 · p3 25,304 · p4 300,655 · p5 736,803 · p6 28,548 · p7 26,764 · p8 59,928 | full hashes in §15 |
| cards/ × 8 (1950×2700 PNG) | p1 1,109,719 · p2 734,709 · p3 633,531 · p4 760,113 · p5 790,332 · p6 592,680 · p7 605,862 · p8 941,838 | — |
| WEEKLY-KIT.md (this file) | — | — |
| ABSTRACT.txt (one Korean line, no ASCII double quotes) | — | — |

SVG SHA-256: p1 `47ac594e…`, p2 `3629ee6e…`, p3 `a0ae3628…`, p4 `435cd4ee…`,
p5 `5c231576…`, p6 `c7098182…`, p7 `5c3de102…`, p8 `b2df0615…` (full hashes in §15; pre-fix p8 was `ba2093a9…`, see §17).

## 2. Totals (registry-derived, identical to the core)

- **150 exercises** — A2 51 · B1 75 · B2 24; per page 10/18/18/18/18/18/12/38 (same as core).
- Writing model (P8 §H): **exactly 84 words**, unchanged Russian text.
- Registry `type` strings localized to Korean inside this build's registry only
  (문장 완성 54 · 객관식 42 · 단어 짝짓기 20 · 문장 만들기 12 · 문장 바꾸기 4 ·
  빈칸 객관식 13 · 번역 4 · 쓰기 1 — counts identical to the core); type strings never print.
- Exercise instructions localized per the W43 RU×KO pattern
  (빈칸 채우기 / 문장 만들기 / 번역 / 쓰기 / 바꿔 쓰기 / 단어와 뜻 짝짓기 /
  날짜와 사건을 짝짓기 / 팀과 상대를 짝짓기).
- Build log (final one-process run, `hidden_files/weekly-report-w45-ru-ko-build/build-final.log`):
  **zero FLOW OVERFLOW / HEAD TOO WIDE warnings**. A deterministic re-run reproduced
  all 8 SVGs byte-identically (sha256 check 8/8 OK), so the rendered cards/PDFs stand.

## 3. Baseline reproduction (before any edit)

The unmodified copy of the core build regenerated all 8 SVGs **byte-identical** to the
shipped core SVGs (`tools/freeze.py baseline`, `tools/scratch/baseline-w45-ru-ko`):

| Page | Core sha256 (prefix) | Baseline |
|---|---|---|
| p1-pervaya.svg | 8bfcb7e289dc383e | identical |
| p2-zhizn.svg | 5b35f1d7c000759f | identical |
| p3-kultura.svg | 8be9ba7f8d32ad9b | identical |
| p4-sport.svg | 9d699050f467482a | identical |
| p5-molodezh.svg | f49d0ed8b09b4ec7 | identical |
| p6-razbor.svg | 8559d61d890820e0 | identical |
| p7-yazyk.svg | 961119d6a19e617b | identical |
| p8-test.svg | 2738ae046bda8030 | identical |

Core integrity: shipped core SVGs re-hashed after all build work — unchanged (same 8
hashes). All Korean edits were made on top of that proven baseline, executed only
through the build copy's single driver (`run.py` → `render.py`, one process).

## 4. Pairing furniture (W43 RU×KO registry, verbatim; VOL follows this core)

- **Pairing badge (P1, brick red #a4553a, 22pt bold, centred):**
  `러시아어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판` — **INSERTED at (975, 574)**
  per the RU-core family slot (see §5 for the three-way measurement). The core's
  Russian subtitle at y=372 stays untouched.
- **Top strip centre (P1):** `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · 매주 발행 · 러시아가 읽는 러시아어`
  (W43 RU×KO verbatim).
- **Dark band right lines (P1):** `가운데 낀 수요일` / `11월 4일 휴일 · 2, 6면 참조`.
- **Footers (Korean, every page):** left
  `Lucerna · 러시아어 주간지 VOL.2 · 텍스트는 러시아어 · 해설은 한국어` ·
  right `제 N 면 / 총 8 면`.
- **Gloss prefix:** `해설 — ` (bslib4 gloss()).
- **Bilingual section heads** = Russian original · Korean short form (W43 forms):
  ГЛАВНАЯ ТЕМА · 헤드라인 / НЕДЕЛЯ В ЦИФРАХ · 이번 주 숫자 / СЕЙЧАС ВЫ · 지금 연습해요 /
  СМИ · 미디어 화제 / В ЭТОМ НОМЕРЕ · 이번 호 차례 / СЛОВО НЕДЕЛИ · 이번 주 단어 /
  КОРОТКО · 단신 / БЛИЦ-ВИКТОРИНА · 번개 퀴즈 / А ВЫ? · 여러분은요? /
  СЛОВА НЕДЕЛИ · 이번 주 단어 / УПРАЖНЕНИЯ · 제 N면 연습 /
  ЖИЗНЬ · 생활 / КУЛЬТУРА · 문화 / СПОРТ · 스포츠 / МОЛОДЁЖЬ · 청소년 /
  БОЛЬШОЙ РАЗБОР · 심층 / ЯЗЫК · 언어 / ТЕСТ И ОТВЕТЫ · 연습과 답 /
  14-Й ТУР: КАЛЕНДАРЬ · 14라운드 일정 / ЗА И ПРОТИВ · 찬반 /
  НЕДЕЛЯ ДЕНЬ ЗА ДНЁМ · 이번 주 날짜별 달력 / ОШИБКИ · 실수 클리닉 /
  СЛОВО · 이번 주 새 단어 / ФРАЗЫ НЕДЕЛИ · 이번 주 문장 — 이번 호 기사에서 그대로 뽑았어요 /
  СЛЕДУЮЩАЯ НЕДЕЛЯ · 다음 호 예고 (VOL.3).
- **Exercise header right note (P2–P6):** `답은 8면에 · 문제는 급이 섞여 있어요, 번호로 찾으세요`;
  P1 quiz right note: `1면을 읽고 정답을 고르세요 · 답은 8면에`.
- **P8:** header `ОТВЕТЫ · 정답 — 면별로 나누어 실었어요, 번호로 찾으세요`;
  right note `문제마다 한국어 해설 한 줄 · ✓ 표시는 모범 답안 문제예요`;
  separators `— 제 N 면 —`; answer typography is the RU family's dash style
  (`N. key — note`, writing items `N. ✓ note`) at the core's own sizes (13.3/13.0, lh 1.13).
- **Band subtitles** carry a short Korean segment after the frozen Russian one
  (e.g. P2 `짧은 근무일, 11월의 변화와 지난주 소식`, P6 `휴일이 낀 한 주`,
  P7 `세 단계, 세 주제`, P8 `제 8면 · Большой тест недели + все ответы`).
- **Contents-table level tag for page 8 stays `все`** (W43 RU×KO precedent — kept frozen,
  not translated; see §6).
- **Captions and credits stay Russian by design** (as in W43 RU×KO and W45 RU×DE);
  image payloads byte-identical to the core on every page (§10).

## 5. Badge slot — three-way measurement (this edition / W43 shipped / README #20)

| | String | Slot | Size / weight / colour | Ink span (PIL, venv metrics) |
|---|---|---|---|---|
| This edition (W45 RU×KO) | 러시아어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판 | (975, 574) inserted | 22pt / 700 / #a4553a | 716.16–1234.16 (w 517.67; ink-bbox measure, venv PIL + build fonts — corrected from advance-measure 1233.84, see §17) |
| W43 shipped RU×KO | identical string, verbatim | (975, 574) inserted | 22pt / 700 / #a4553a | 716.16–1234.16 (identical; re-measured from the W43 shipped P1 SVG itself with the same ink-bbox measure, see §17) |
| README #20 family case | FR/IT cores whose y=372 is frozen body strapline → badge INSERTED at y=574, 22pt BRICK centred (FR×JA / FR×KO / IT×JA precedents) | 574 inserted | 22pt BRICK | — |

Why not the 372 slot: the W45 core's y=372 row is frozen Russian target text
(`ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ`),
byte-identical in core and edition — using it would delete target-language text.
The RU family already carries both accepted modes (372-slot group: ru-en / ru-fr / ru-it / ru-pt,
where 372 is a replaceable subtitle slot; 574-slot group: ru-de / ru-es, plus W43 RU×KO itself).
This edition follows its own pair's shipped precedent (574), not a generalized #20
description, and deletes no frozen Russian text.
Clearances (measured): dark-band bottom 542 → badge baseline 574; headline-head
baseline 606 (head ink top ≈588). Same-baseline ink scan (§8) 0 flags on P1;
occlusion audit (§8) 0 flags; P1 card visually confirms no collision.

## 6. Freeze verification (rendered SVGs, this edition vs core)

- `tools/freeze.py diff` (`tools/scratch/diff-w45-ru-ko.json`): added CJK characters =
  2,642 total, **all Hangul** (per-page added-with-Han lists are empty on all 8 pages; coordinator KIT-only correction 2026-10-27 per JA precedent: the P8 #99 fix itself reduced P8 added 1090→1087, so the pre-fix 2,645 was stale; paper unchanged, verified by coordinator re-run of `tools/freeze.py diff` TOTAL 2642, per-page 166/265/191/181/174/222/356/1087);
  edition SVGs contain **0 Han characters** on every page.
- **Removed strings without Han:** only the eight P8 separators `— СТРАНИЦА N —`
  (furniture, replaced by `— 제 N 면 —` per the W43 pair registry). Every other removed
  string is an explanation-layer string.
- **Cyrillic token-multiset diff per page (target-language proof):**
  P1 400 = 400, P2 443 = 443, P3 338 = 338, P4 306 = 306, P5 316 = 316, P6 354 = 354,
  P7 397 = 397 (exactly equal); P8 641 → 633, the only difference being
  `СТРАНИЦА ×8` (the separators above). No other Cyrillic token differs anywhere.
  Korean notes use Hangul transliterations for team names (크라스노다르, 스파르타크,
  체스카, 로코모티프, 제니트), adding no Cyrillic citations.
- All 8 P7 golden sentences occur exactly as in the core (Russian quotes byte-identical;
  only their Korean translations are new; page tags stay Russian `Страница N`).

## 7. P8 answers (dash family; generation code byte-identical except the type check)

- `tools/p8.py compare` core vs edition: **CLEAN, 150 noted = 150 noted,
  missing = [], extra = [], uncertain = []**; keydiff = [83, 137, 138, 148].
- **Independent dash-parse of all 150 printed P8 lines** (key = text before the first
  ` — `; writing item handled separately): keys identical for all numbers **except
  137 and 138**; counts 150 = 150, no missing/extra.
- **137, 138 — documented re-aims (W43 translation precedent):** RU→KO items; Russian
  stems kept, instruction `번역`; keys are Korean in this edition
  (137 `11월 4일 수요일은 휴일이에요.` with note `3면 참조`;
  138 `프로모 코드는 할인 코드예요.` with note `5면 참조`).
  139/140 are the reverse direction (Korean prompts, instruction `번역`, keys Russian
  byte-identical: 139 `В субботу «Краснодар» играет с ЦСКА.`,
  140 `Поздравляю с Днём народного единства!`).
  150 is the writing apparatus line (key form `(열린 문제 — 모범 답안은 아래에 있어요)`,
  note `모범 답안은 이 면 H 구역에 있어요 (84단어)`), model text unchanged Russian.
- **83, 148 — p8.py extraction artifacts, NOT key changes (README #13 lesson applied):**
  the tool's paren branch treats a trailing half-width paren group as part of the
  extracted "key", while the core's full-width parens are not. Printed keys are
  identical in both SVGs (83: key `B`; 148: key `A`), verified by the dash-parse above.
  Korean notes use half-width parentheses throughout (W43 RU×KO typography).
- P8 answers flow ends at y=2203 (bottom 2540) — ample clearance (was 2231 before the §17 fix round; the saved line plus the resulting column-boundary shift moved the flow end up 28).

## 8. Geometric audit (mandatory SOP gate — builder run)

- `tools/occlusion_audit.py`: selftest OK (all 6 planted classes fire, clean controls
  silent). **Final run: 0 flags on all 8 pages; core control 0 flags; NEW vs core: 0**
  (`tools/scratch/occlusion-w45-ru-ko.json`, `occlusion-w45-ru-core.json`).
- **Same-baseline ink scan (README #10, PIL advance extents, venv metrics):**
  all pages **0 flags** at < 5 px gaps, including the P1 top band and the badge row.
- **Chart page (P6) element check (README #12):** zero text elements overlapped by any
  later-drawn rect; bars measured **600/494/388/282 px = 34/28/22/16 × 600/34 exactly**,
  the four % labels at bar-end +14 px (x 1299/1193/1087/981, identical to the core),
  zero ink overlap; the practice-data disclaimer keeps the core's Russian sentence
  plus its Korean equivalent.
- **P7 readers' corner geometry (see also §11):** P7 rect multiset **identical to the
  core**; letters-box bottom 1727.58 = core; phrases rule at y=1756, 28.42 clear.
- Cards P1, P2, P7 viewed by the builder after the final render (Korean glyphs render
  throughout, no missing-glyph boxes); P3–P6, P8 covered by the audits + Cyrillic diff.

## 9. Gloss counts (split on `·` itself, README #21)

9 gloss() calls, **26 items** — per-call counts identical to the core:

| Module | Calls | Items |
|---|---|---|
| content12 (P2) | 3 | 3 / 3 / 3 |
| content34 (P3 + P4) | 3 | 3 / 3 / 3 |
| content56 (P5 + P6) | 3 | 3 / 2 / 3 |

No gloss item was added, dropped, or merged in translation. (The P1 explanation line
and the P7 level bridges are expl() lines, not gloss() calls, and are counted
separately; their item/segment counts are likewise preserved.)

## 10. Images & credits (byte-identical payloads; credits identical to the core)

| Page | Image | Credit (as printed, Russian, frozen) |
|---|---|---|
| P1 | November park photo (autumn_path.jpg, reused from W43) | Фото: Toxer427 — лицензия CC0 (Wikimedia Commons) |
| P4 | 1912 football photo (football1912.jpg, reused from W43) | Фото: автор неизвестен, 1912 — общественное достояние (Wikimedia Commons) |
| P5 | Market photo (market.jpg) | Фото: Престон Керес (USDA) — общественное достояние (Wikimedia Commons) |

Image payload SHA-256 (data URIs in the SVGs, identical core vs edition):
P1 `033aa031…`, P4 `b2992510…`, P5 `8c7e1ddf…`; no image payloads on P2/P3/P6/P7/P8.
Image licensing verification is the core's (W45 RU core KIT §4); this edition changes
no image.

## 11. Readers' corner — no fabrication (disclosure + example kept, explanation layer only)

P7 prints the core's editor's example unchanged (Russian,
`— М. (пример от редакции)`) and the core's Russian disclosure unchanged, plus the
Korean disclosure line. No new reader, letter, name, or quote was invented.
The Korean disclosure carries all three facts: no real letters had arrived, no best
P8 writing had arrived, the editor's example stands and the promise carries to VOL.3
(`실제 편지와 우수 작문은 오지 않았어요. 편집부 예시로 싣고, 약속은 VOL.3으로 이어져요.`).
The VOL.3 teaser repeats the call for letters, as in the core.
**Adjudicated, not re-reported (per the brief's ru-en precedent):** the letters-box
bottom is 1727.58 and the disclosure's 2nd line baseline is 1738.28 — i.e. the 2nd
disclosure line sits below the box bottom. This geometry is **identical in the core
and this edition** (P7 rect multiset identical; disclosure line counts equal in both
languages); it is frozen core geometry, not something this edition introduced, and
the box was deliberately NOT resized. The text is fully readable on the P7 card and
clear of the phrases rule at y=1756. Recorded here per the brief; no action taken.

## 12. Facts (identical to the core)

Split week (2–3 Nov work, 4 Nov Wednesday holiday, 3 Nov one hour shorter,
school-holiday tail to 4 Nov), 11.11 sale 22 Oct – 12 Nov (attributed trade-press
note only), RPL round 14 6–8 Nov (Krasnodar–CSKA Sat 19:30 Ozon Arena;
Spartak–Akron Sun 16:15; round-13 closer Mon 2 Nov; pause until 20 Nov), reported
past events only (CSKA–Spartak 2:0 on 25 Oct; first snow forecast failed;
28 Oct Grandparents Day; 31 Oct Halloween). Russian domestic life only; no politics.
The P6 chart is labeled practice data in both languages
(`УЧЕБНЫЕ ДАННЫЕ · 연습 데이터` + the Russian disclaimer sentence plus its Korean
equivalent), bars 34/28/22/16 as the core.

## 13. Builder self-proof — defects found and fixed

Full visual pass over the P1/P2/P7 cards + full gate suite on the rendered SVGs.
Three real explanation-layer defects were found and fixed (each fix in the Korean
wording only, each followed by a one-process re-render and a full gate re-run):

1. P2 readers'-call Korean para wrapped (under the build venv's PIL metrics) as
   `…보내요` / `? 러시아어로…` / `요.` — a line-start orphan `?` plus a lone `요.`
   tail. Reworded to `여러분은요? 11월 4일 수요일은 뭐 할 거예요? 러시아어로 두 문장 보내 주세요.`
   — now 2 clean lines; P2 col3 ends 1155.5, back to the core value.
2. P6 gloss wrapped with a lone `).` line (the parenthetical in `집에서(일해요).`
   stranded its closer). Reworded to `집에서 일해요` — now 2 clean lines; P6 gloss
   box height back to the core value.
3. P5 gloss split a word with a 4-syllable tail (`만|들었어요`). Reworded to
   `불필요한 것 · составили 만들었어요` — now breaks at a word boundary
   (`составили` / `만들었어요.`).
4. P3 gloss split (`산책해|요`, 1-syllable tail — below the gate threshold) was
   nevertheless cleaned to `산책을 해요` for a word-boundary break.
5. Quiz note used a Latin team abbreviation (`CSKA`); changed to the Hangul form
   (`체스카`) for consistency with the edition's transliteration rule (§6).

**Metric lesson for the proofreader (important):** wrap measurements MUST be taken
with the build venv's Python (`tools/venv/bin/python`), not the system Python — the
two Pillow builds measure the same Korean line differently (the A ВЫ line measures
387.58 under system Python but 390.91 under the venv, which is what the build
actually renders). All line-count claims in this KIT were verified against the
rendered SVGs, not against system-Python wrap calls.

## 14. Korean orphan scan (README #16, task definition)

Scan definition (rendered SVG lines, `tools/scratch/orphan-w45-ru-ko.py`):
every final-line text element checked for (a) a final token consisting only of
punctuation in [.!?…)\]»」], (b) a line starting with such punctuation, and
(c) mid-word splits verified against the build's Korean source strings, with the
continuation fragment's syllable count (≥3 flagged).
**Final result: 0 flags.** Remaining candidates, all adjudicated non-defects:
- P2 gloss line pair `지난 호` / `에.` — a 1-syllable tail, below the ≥3 threshold;
  two rewording attempts produced worse breaks (a line-start separator; a split
  inside 더비), so the original wording stands.
- Gloss lines ending with the `·` separator — the separator is not in the task's
  punctuation set, and the same break class occurs in the core's glosses.
- No line begins or ends with lone punctuation anywhere in the edition.

**Fix round 2026-10-27 (see §17):** the scan's consecutive-line step window was
corrected from 15–45 to 10–45 in `tools/scratch/orphan-w45-ru-ko.py` — the old
15 lower bound structurally excluded the P8 answer line step of 14.69 (13.0pt ×
1.13), which is why the P8 item-99 split was missed. Re-scan of all 8 pages with
the corrected window: **0 flags at the ≥3-syllable threshold**; remaining
candidates, both below threshold and unchanged: P2 gloss tail 1, P8 item-139 note
tail 2.

## 15. Notes for the independent proofreader

- Re-derive the P8 keys from the registry (one-process runs in repointed copies;
  the edition copy re-render reproduced the shipped SVGs 8/8 before the fix round).
  Expected key diffs: {137, 138}; stems {139, 140} with Russian keys byte-identical;
  writing apparatus {150}; p8.py artifact diffs {83, 148} disproven by the dash-parse
  in §7 — verify against the printed lines, not the tool's paren branch alone.
- The P8 answer block uses the RU core's own sizes (13.3/13.0, lh 1.13), not any
  other family's sizes — the family rule is "the core's typography, the column's
  language".
- Height-critical Korean lines were pre-measured with the build's own wrap() under
  the venv to the core's line counts (P2 call box, P7 clinic/word/letters boxes);
  the col3 end coordinates on P2 (1155.5) and P7 (1727.58) match the core exactly.
- The two Han characters found by a raw code grep are inside an unrendered icon
  docstring in the shared svglib (a festival name in a line-art docstring) — they
  are not rendered text, and the rendered SVGs contain 0 Han characters (§6).
- Scratch (transform script, gate scripts, occlusion JSONs, diff JSON, baseline
  output) is confined to `tools/scratch/` and the build dir; nothing operative
  references it.
- Full SVG hashes (final build):
  p1-pervaya: `47ac594e37da186b28e228051ac6bc4f6d4df4469413eaa9331240a4f181d628`
  p2-zhizn: `3629ee6e0df6fcd95bb3351c7925d8456c237e9a41edaae9ec5d0342bae5a8ba`
  p3-kultura: `a0ae3628996bf346e205acb2c4f83d984d894578d12fe0d335ecaa7ef039e432`
  p4-sport: `435cd4eea991527618ec9233920fb58e59e63e22d5b868ae00b290ad4f06dca5`
  p5-molodezh: `5c231576f727b161aaf1de21e89a15316935e0f0eab820e0aa464443c47f884d`
  p6-razbor: `c709818224aabb0a6233630c9fbfec2e12d65a7ebc76ae22eab75bdf40f281f5`
  p7-yazyk: `5c3de1023ba716bec0214a678205caab23fd6639f0b27760ca27c9ca12ea3821`
  p8-test: `b2df06159e0c816acecdf875c52a66df1d0f43ce7cca45ef488921f72715cd8f`

## 16. Delivery status

Builder-complete, NOT proofread-finalized, NOT pushed, NOT posted: per the task brief,
repo insertion is done by the parent line (serialized) and independent proofread is
still pending. No git push, no Discord post, no user message, no cron was made from
this build.

## 17. Fix round (2026-10-27, post independent proof — NOT a finalization)

Independent proof (`hidden_files/w45/ru-ko-proof/REPORT.md`) blocked this edition on
2 items. Both were fixed here; per SOP §8.4 a fresh full independent proofread of
the new version is still required, and nothing in this section constitutes
finalization. No Discord post, no chat card/PDF dump, no cron, no weekly-git touch
was made from this fix round. Fix log: `hidden_files/weekly-report-w45-ru-ko-build/build-fix.log`
(one-process `run.py` + `render.py`, zero FLOW OVERFLOW / HEAD TOO WIDE warnings).

### Fix 1 — P8 item-99 note reworded to a single line (was a mid-word split)

- **Before (rendered P8, col x=989, 13.0pt, step 14.69):** line 1 y=1879.94
  `99. ... — а는 대조를 나` / line 2 y=1894.63 `타내요` — the note verb was split
  as `나 | 타내요`, continuation tail 3 syllables, at the README #16 flagged
  threshold. (Note: the note's first character is Cyrillic а, the Russian
  conjunction itself, followed by the Korean particle 는 — it is not Hangul 아.)
- **After:** note reworded to the shorter equivalent `а는 대조예요` (Cyrillic а +
  `는 대조예요`; "а is contrast" for "а expresses contrast" — key, stem, and
  answer fact unchanged; no other entry touched). Operative change is the single
  line in the build copy's `content56.py` (whole-line exact-literal replacement,
  count-asserted: old string 1 → 0, new string 1).
- **Pre-render measurement (build venv PIL + build svglib wrap, 13.0pt serif,
  col width 434):** the old full line wrapped to exactly the reported 2 lines;
  the new full line measures 420.25 ≤ 434 and wraps to **1 line**.
- **After re-render (rendered P8):** item 99 is one line at y=1879.94 (the old
  line-1 baseline), `타내요` occurs 0 times in P8, normal 28.19 spacing to item
  100 at y=1908.13; P8 answers flow ends at y=2203 (was 2231), bottom 2540.
  P8 card re-viewed at the item-99 region: single clean line, no orphan line.
- **Root-cause tool fix:** the builder orphan scan's consecutive-line step window
  was corrected from 15–45 to 10–45 in `tools/scratch/orphan-w45-ru-ko.py`
  (count-asserted: `10 <= step <= 45` present once, `15 <= step` zero times).
  Re-scan of all 8 pages with the corrected window: **0 flags at the ≥3
  threshold** (remaining candidates below threshold: P2 gloss tail 1, P8
  item-139 note tail 2 — both already adjudicated non-defects, unchanged).

### Fix 2 — KIT §5 badge ink span right end corrected (record only, no layout change)

- **Before:** KIT §5 claimed 716.16–1233.84 (w 517.67) — the right end used the
  advance half-width (975 + 517.67/2 = 1233.84) instead of the ink bbox.
- **After:** 716.16–1234.16. Re-measured with venv PIL + build fonts (sans bold
  22pt, centred x=975): advance 517.67, ink bbox (0, 7, 518, 29), span
  716.16–1234.16; the P1 badge element itself is unchanged ((975, 574), same
  string, size, weight, colour) and the W43 shipped badge re-measured from its own
  P1 SVG gives the identical 716.16–1234.16, so both §5 rows were corrected.
  No collision impact (same-baseline scan 0 flags, §8 re-run below).

### Full gate re-run on the fixed version (all numbers re-measured, not carried over)

- `tools/occlusion_audit.py`: selftest OK (all 6 planted classes fire, clean
  controls silent); edition SVG dir **0 flags**.
- Same-baseline ink scan (venv PIL + build fonts, < 5px = flag): edition **0
  flags** on all 8 pages, core control 0 flags.
- `tools/p8.py compare`: **CLEAN, 150 noted = 150 noted, missing = [],
  extra_count = 0, uncertain = [], keydiff = [83, 137, 138, 148]** — identical to
  the pre-fix result; the note rewording changed no key.
- Totals unchanged: 150 exercises (A2 51 / B1 75 / B2 24; per page
  10/18/18/18/18/18/12/38), 84-word writing model, zero build warnings.
- **Per-page byte identity (pre-fix → post-fix SHA-256):** p1 `47ac594e…`
  identical, p2 `3629ee6e…` identical, p3 `a0ae3628…` identical, p4 `435cd4ee…`
  identical, p5 `5c231576…` identical, p6 `c7098182…` identical, p7 `5c3de102…`
  identical — **only p8 changed**: `ba2093a9…` → `b2df0615…` (full hashes in
  §15). Cards p1–p7 byte sizes identical to pre-fix; only p8 card changed
  (946,622 → 941,838 bytes); all 8 cards still 1950×2700.
- **PDFs re-measured (8 pages each):** print 15,078,056 bytes
  `6f21c3217ac2fdc6b38850c7ffc949d871954007d3ab0bde8b38fddcdb59a878`
  (was 15,078,049 / `01681c2b…`); web 3,090,198 bytes
  `c8d333abeb734480249ae62ac47293f5d3ca04a6391720bb458f8efab0b05016`
  (was 3,091,048 / `d23437e0…`). §1 and §15 updated to these values.
