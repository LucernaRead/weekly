# PROOF-NOTE — 2026-W47 ru-ko, independent re-proof (round 2)

Proofer: independent (round 2; proof1's D1a/D1b were fixed by re-fanout, this
round re-verifies them from scratch). Scope: ONLY
`production/2026-w47/2026-w47-ru-ko/` against core `production/2026-w47/core-ru/`.
Nothing in the production tree was written: all rebuilds/renders ran in a
scratch copy; production SHAs re-verified unchanged at the end (see §1).
Scratch: `hidden_files/w47/scratch-proof-ru-ko1/round2/` (logs, JSONs, crops,
renders); proof1's notes are archived in `archive-proof1/`.

## Conclusion: (b) — DEFECTS FOUND, CANNOT FINALIZE

1 defect, minor, confined to `.text.md` (site body text). Print PDF and web
PDF are unaffected. Defect D-1 below; full gate table in §3, GATE-LOG.md
carries every measured value.

## 1. Artifact identity (re-measured, not trusted)

| File | Bytes | SHA-256 (re-measured) | Matches brief |
|---|---|---|---|
| `Lucerna-VOL4-ru-ko.pdf` (print) | 22,007,810 | `78e4442af8af9ec286c407ff66e08bac2029dd79d3ded43d1bfde3d555a6a400` | yes |
| `Lucerna-VOL4-ru-ko-web.pdf` (web) | 3,513,230 | `3bf39ecf4fa4563458c68319ca42171642f9ad0be24650064faa9b7d9bd03195` | yes |
| `2026-w47-ru-ko.text.md` | 65,069 | `d1feb40e417ba058d773a58ada62ad7fd7805b6a943599d8d017510b402d5a3d` | yes |

Core对照 (fix1, unchanged): print
`d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81`
(31,429,147 B), web
`2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197`
(4,025,834 B), text.md
`348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc`
(60,953 B) — all re-measured, identical to FANOUT-REPORT-ru.md.
Production SVG hashes recorded before work (`round2/prod-svg-sha-before.txt`)
and re-verified OK after work (8/8); the three artifact SHAs above were
re-measured at the end and are unchanged.

## 2. Defect list

### D-1 (MINOR, text.md only) — Q150 answer-list line does not use the core's ✓ form
- **Location:** `2026-w47-ru-ko.text.md` L836 (`## Answers`, `### Page 8`).
- **Measured:**
  - Edition L836: `150. (열린 문제 — 모범 답안은 아래에 있어요) — 모범 답안은 이 면의 H란(97 단어)`
  - Core L836: `150. ✓ 范文见本版 H 区（97词）`
  - P8 printed key for 150 is `✓` in BOTH editions
    (`ru-ko-p8.json` key `150` = `✓`; core `ru-p8.json` key `150` = `✓`;
    `p8.py compare` keydiff = `[137, 138, 139, 140]` only).
  - Exercise line is consistent in both: edition L663 key
    `(열린 문제 — 모범 답안은 아래에 있어요)`, core L663 key `（开放题，范文如下）`.
- **Root cause (source lines, verified in both dirs — `ru_textmd.py` is
  byte-identical core vs edition):** the answers appendix has a special case
  for the writing item, `ru_textmd.py:614-619`:
  ```python
  if e["type"] == "写作":
      lines.append("%d. ✓ %s" % (e["n"], e["note"]))
  else:
      lines.append("%d. %s — %s" % (e["n"], e["key"], e["note"]))
  ```
  The check hard-codes the Chinese type name `写作`. This edition's Q150
  type is the Korean `쓰기` (`content8.py:110`, `f.ex("B1", "쓰기", …)`),
  so the special case never fires and the appendix falls through to the
  generic `key — note` format. The P8 renderer does the same job correctly
  (`content8.py:127`, `txt = f"{n}. ✓ {note}"`, no type check) — that is why
  the printed page is right and only the text.md appendix is wrong.
  Attribution: exporter code shared with the core, triggered by the
  fan-out's translated type label — not a content/translator error.
- **Why it is a defect, not a style difference:** the line is redundant
  ("model answer below" said twice in different words) and it breaks the
  rule that the P8 printed key and the registered key agree except for
  designed differences: for the other 149 items the text.md keylist head
  equals the P8 printed key exactly (verified mechanically, keycheck2.py);
  for 150 it does not. It is also inconsistent with the core's own form.
- **Scope:** same defect class is SYSTEMATIC across the ru family —
  spot-checked `ru-en`, `ru-de`, `ru-ja` text.md L836, all three show the
  same long form (e.g. en: `150. (Open task; model text below) — See the
  model text in section H of this page (97 words)`); only the core has the
  `✓` form. This report only concerns ru-ko; the other 9 editions are
  flagged here so the coordinator can decide the family-wide fix.
- **Fix (for the builder, not done by the proofer):** make the
  `ru_textmd.py` special case type-independent (match by exercise number /
  registry flag, or accept the translated writing-type labels); regenerate
  `2026-w47-ru-ko.text.md` (its SHA/size will change — KIT §5 numbers must
  be updated with it); re-proof the regenerated text.md. Print/web PDFs
  need no rebuild (their content is already correct).
- **Render evidence:** P8 delivered-PDF render (`round2/pdf-render/p8.png`,
  bottom right) shows `150. ✓ 모범 답안은 이 면의 H란(97 단어)`; the
  text.md L836 string above is quoted verbatim from the file.

## 3. Gates (all re-run independently; values in round2/gates.json)

| Gate | Result (re-measured) |
|---|---|
| run.py (scratch copy, abs redirect) | rc=0, TOTAL 150 (A2 50 / B1 76 / B2 24; pp. 10/18/18/18/18/18/12/38; model words 97), 0 FLOW OVERFLOW / HEAD TOO WIDE; rebuilt SVGs 8/8 byte-identical to production; re-rendered print PDF SHA = delivered print SHA `78e4442a…` |
| check_core.py | rc=0, golden BAD 0, gloss fails 0, 8 golden sentences ×2; orphan 1 (P7 y553 `”».`), same-baseline collision 1 (P1 y1712 `чёрная`) — both identical to core, benign known class |
| freeze baseline (edition) | 8/8 (`freeze.py baseline --build <edition> --core-svg <edition>/svg`); ALSO core baseline 8/8 (`--build core-ru --core-svg core-ru/svg`, covering the task's parenthetical reading) |
| freeze diff core→edition | removed distinct 361 / count-sum 529; Cyrillic-bearing removed exactly 15 = Q46 `можно` ×1 + 14 Morozko-caption words (P8 caption zone y≥2450; image skipped by design, `Морозко` absent from edition P8); unexplained 0. New CJK: Han (汉字) 0, kana 0, Hangul 2,832 chars (reader explanations — the only new CJK) |
| p8 extract | 150/150 noted; key 20 = `желании` |
| p8 compare | CLEAN, keydiff `[137, 138, 139, 140]`; direct keydiff vs core `ru-p8.json` identical `[137, 138, 139, 140]` |
| occlusion audit | selftest OK (all 6 planted classes fired, clean controls silent); 42 TEXTX, 0 LINEX, 0 COVER/FOOTER/EDGE/BOXTITLE |
| occlusion adjudication | `adjudicate_ru.py` 42/42 CLEAR; PLUS my own PDF-pixel adjudication on the delivered print PDF rendered 1950×2700 (SX=1.0, not the script's 1950/1800): 41/42 CLEAR, flag 38 resolved separately — direct column scan shows a full-background column at x=556 between `Кипренского` ink (ends 555) and the `,` ink (starts 557), and the crop `flag38-crop.png` shows the caption clean; 42/42 CLEAR total |
| print/web text layer | both 8 pages; pdftotext outputs BYTE-IDENTICAL (58,692 B each); fitz char multiset identical overall AND per page, 26,535 chars; web 3,513,230 B < 7 MB |
| P8 min font (§1.1, s11_check) | 9.75 pt, FAILURES: none |
| creambox full scan | 0 negative inside-only clearance; 96 BELOW-WINDOW lines, all classified (offsets +28/+32/+34/+37, +44 ×1 = the P1 quick-quiz header pointer at y=2348.0, by design); vs first-build backup scan: exactly 3 diff lines (the D1a fix — see §4) |
| kicker (P1, PIL whole-run getbbox) | gaps `[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]` px, min 5.9 ≥ 4 |
| box-title / horizontal-overflow sweep | own PIL true-ink sweep over all 5,260 text elements on 8 pages vs page bounds + containing rect: 0 violations. P1 stats title `ТУР В ЦИФРАХ　숫자로 보는 라운드`: PIL ink ends x=931.9 (advance 931.7), box right 961.0 → clearance 29.1 px; delivered-PDF pixels: rightmost ink x=928 inside the box → clearance 33 px. The ru-de/ru-en +36.6/+37.9 defect does NOT reproduce here. Crop: `p1-stats-crop.png` |
| KIT numbers | text.md 65,069 B, print/web SHAs all present and correct in WEEKLY-KIT.md |

## 4. Re-fanout points re-verified (each independently)

- D1: text.md L459 (`УЧЕБНЫЕ ДАННЫЕ`), L504 (`Три уровня, три темы`),
  L596 (`Большой тест недели`) all present; SVG: P6 s1 + full disclaimer,
  P7 s3, P8 s4 all present.
- D2: Q25 option `День студента` (text.md L187; P2 render shows 25. 17
  ноября with options a. День психолога / b. День студента / c. Всемирный
  день ребёнка / d. день рождения Деда Мороза; P8 key 25 = `b`, = core);
  full phrase `Международный день студента` ×2 in edition text.md = ×2 in core.
- D6: Q20 key `желании` (text.md L173 + keylist L694 + P8 printed key 20);
  stem `Дети пишут Деду Морозу о своём ___.` — prepositional `о своём
  желании` is correct Russian (verified by hand).
- D1a/D1b (ko map): `map-ko.json` contains `родина` and `синоптики`;
  text.md L99 (`родина 고향`) and L538 (`синоптики обещают …`) are pure
  Cyrillic; per-element per-token mixed-script sweep over all 8 SVGs:
  0 mixed Cyrillic+Hangul tokens, 0 Han tokens, 0 kana tokens in SVG text;
  0 Han / 0 kana chars in text.md. Creambox vs backup diff is exactly the
  3 D1a lines.
- Q73 hand check: `В прошлом году сделали 14,4 млн ___.` → `заказов`
  (genitive plural after 14,4 млн) — correct; P8 key 73 = `заказов` = core.
- 150-question mechanical check (`keycheck.py`, `keycheck2.py`):
  130 tagged exercise lines in both (matching sets 25–28/39–42/57–60/
  75–78/141–144 are untagged in text.md in core too — same-as-core);
  stems 0 diffs vs core; key HEADS 0 diffs vs core except designed
  137–140 (Korean translation keys) and Q150's appendix form (D-1);
  keylist 150/150 both, no missing; P8 printed keys vs text.md keylist
  heads: only Q150 differs (D-1).
- P1–P8 full-page visual read of the delivered print PDF renders
  (`round2/pdf-render/p1–p8.png`): no overflow, overlap, clipping or
  misplaced element; all footers `Lucerna　러시아어 주간지 VOL.4…`,
  page numbers `제 N 면 / 총 8 면` correct; VOL.3 only in the P4 correction
  sentence.

## 5. Korean-reader review (all 341 distinct Korean segments read)

- Spelling, honorifics, transliteration: no errors found. Consistent
  polite style (`-입니다/-습니다`, `-하세요/-주세요`); standard
  transliterations (데드 모로즈, 스파르타크, 로코모티프, 크릴리야 소베토프,
  마하치칼라, 벨리키 우스튜그, 타슈켄트); weather terms 진눈깨비/얼음비/
  노면 결빙 used consistently (incl. word box + P7 + notes); case terms
  생격/조격/전치격 correct.
- No Chinese or Japanese residue: freeze added-Han = 0 characters,
  kana = 0; the only new CJK is 2,832 Hangul chars (reader explanations).
- `(а는 대조를 나타냅니다)` (text.md L498/499/780/781) — NOT a defect:
  authored map value (`map-ko.json:104`, `"а 表示对比": "а는 대조를 나타냅니다"`);
  Russian word `а` + Korean topic particle `는` is the normal gloss
  convention, matching core `а 表示对比` and en `а marks a contrast`;
  no such token exists in the printed SVG (0 in the sweep).
- Two minor style observations (not defects): P5 gloss fragment
  `подошёл 맞음` (telegraphic gloss, KIT-documented wrap fix) and the
  H-section header `정답이 하나가 아닙니다` (understandable; a native
  phrasing would be `정해진 답이 있는 문제가 아닙니다`). Left as-is.

## 6. D5 (font issue) — recorded, not a defect, per task

Proof1 D5 (web PDF lost the P1 italic phrase) does NOT reproduce in this
build — it was fixed by the re-fanout's patched `webpdf.py` rebuild:
- Web PDF embeds italic fonts: `LucernaNewsreader-Italic`,
  `LucernaNotoSerif-Italic` (pdffonts; same object IDs 50/54 as print).
- PyMuPDF spans for the italic line `«чёрная пятница»` are identical in
  print and web: Newsreader-Italic `«` + NotoSerif-Italic `чёрная пятница`
  + Newsreader-Italic `»`, with the space present at span level in both.
- `pdftotext` outputs are byte-identical (58,692 B each).
Recorded here only; no repair needed or attempted.

## 7. Checked and cleared (not defects)

- `От редакцииLucerna` tight spacing on P1–P4: identical SVG coordinates
  in core (same elements, same x) — core-inherited rendering.
- check_core orphans: P7 y553 `”».` and P1 y1712 `чёрная` collision —
  both present identically in core.
- Literal `___` blanks (87 in text.md): template gap, core-inherited,
  not listed per task.
- KIT §7 note "numbers head ends x=913.9": stale by ~18 px vs measured
  931.7 (advance) / 931.9 (PIL ink) / 928 (PDF pixels); the artifact
  itself is fine (clearance ~29–33 px). KIT nit only.
- Morozko image skipped on P8 by the build's own condition (keys end
  col 3 y≈2231; `img_y+250+90 > 2560`) — same as core design, not a defect.

## 8. What the fix must cover (for the coordinator)

1. Fix `ru_textmd.py` appendix special case (D-1) and regenerate
   `2026-w47-ru-ko.text.md` (+ update KIT §5 SHA/bytes); re-proof the
   regenerated text.md.
2. Decide the family-wide scope: the same D-1 form appears in all 10 ru
   fan-out text.md files (spot-checked en/de/ja L836); the fix belongs in
   the shared exporter, so one fix covers all 10 — but each edition's
   text.md SHA/bytes/KIT must then be refreshed and re-proofed.
3. No print/web PDF rebuild is needed for ru-ko.

## Evidence files (round2/)

`gates.json`, `gates.log`, `run.log`, `check_core.log`, `render.log`,
`ru-ko-p8.json`, `ru-ko-p8-compare.json`, `core-p8.json`,
`ru-ko-occlusion.json`, `adjudicate-pdf.json` (+ `adjudicate-pdf.log`),
`flag38-crop.png`, `freeze-diff.json`, `freeze-ed/` + `freeze-core/`,
`creambox.log`, `creambox-vs-backup.diff`, `keycheck-150.json`,
`keycheck-report.txt`, `keycheck2.json`, `korean-segments.txt`,
`mixed-sweep.txt`, `boxtitle-sweep.json` (+ `.log`),
`boxtitle_sweep.py`, `my_gates.py`, `adjudicate_pdf.py`, `keycheck.py`,
`keycheck2.py`, `pdf-render/p1–p8.png`, `p1-stats-crop.png`,
`italic-print.png`, `italic-web.png`, `prod-svg-sha-before.txt`,
`prod-svg-mtime-before.txt`, `work/` (scratch rebuild copy;
re-rendered print PDF SHA = delivered `78e4442a…`).
