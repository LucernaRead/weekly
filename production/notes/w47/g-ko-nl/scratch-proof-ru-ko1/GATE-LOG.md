# GATE-LOG — 2026-W47 ru-ko, independent re-proof round 2 (all gates re-run)

Edition: `production/2026-w47/2026-w47-ru-ko/` · VOL.4 · 2026-11-11.
Python: `~/workspace/weekly-git/tools/venv/bin/python` (tools/venv).
My driver: `round2/my_gates.py` (fresh code; same shared-tool invocations as
the re-fanout `gate_lang.py`, every number below re-measured here).
All outputs under `scratch-proof-ru-ko1/round2/`. Nothing in the production
tree was written: rebuilds/renders ran in `round2/work/` (scratch copy);
absolute paths used for every redirect; production SVG SHA-256 recorded
before work and re-verified 8/8 OK after work; the three artifact SHAs
re-measured at the end and unchanged. No commit, no push.

## §0 Identity (re-measured)

- Print PDF 22,007,810 B, SHA-256
  `78e4442af8af9ec286c407ff66e08bac2029dd79d3ded43d1bfde3d555a6a400` — matches brief.
- Web PDF 3,513,230 B, SHA-256
  `3bf39ecf4fa4563458c68319ca42171642f9ad0be24650064faa9b7d9bd03195` — matches brief.
- text.md 65,069 B, SHA-256
  `d1feb40e417ba058d773a58ada62ad7fd7805b6a943599d8d017510b402d5a3d` — matches brief.
- Core (fix1, re-measured, unchanged): print 31,429,147 B
  `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81`;
  web 4,025,834 B
  `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197`;
  text.md 60,953 B
  `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc`.
- Edition dir is untracked in git (`?? production/2026-w47/2026-w47-ru-ko/`);
  `git status` shows no modifications in the edition or core dirs.

## §1 run.py — rc=0, TOTAL 150, SVG 8/8 byte-identical

- Command: `cd round2/work && tools/venv/bin/python run.py > round2/run.log` (absolute redirect).
- rc=0. TOTAL 150; by level A2 50 / B1 76 / B2 24; by page
  1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38; by type 문장 완성 54 /
  객관식 55 / 단어 짝짓기 20 / 문장 만들기 12 / 문장 바꾸기 4 / 번역 4 / 쓰기 1;
  model words 97. `grep -c "FLOW OVERFLOW|HEAD TOO WIDE" run.log` = 0.
- Rebuilt `work/svg/*.svg` vs production `svg/*.svg`: 8/8 MATCH (sha256).
- `render.py` in the scratch copy, rc=0: 8 cards + print PDF 22,007,810 B,
  SHA-256 `78e4442af8af9ec286c407ff66e08bac2029dd79d3ded43d1bfde3d555a6a400`
  = the delivered print PDF SHA (byte-identical reproduction).

## §2 check_core.py — rc=0

- `check_core.py round2/work`, rc=0. GOLDEN: 8, all ×2 (P1×2, P2×1, P3×1,
  P4×1, P5×1, P6×2 — full list in `round2/check_core.log`); golden BAD 0;
  gloss fails 0; P8 svg text chars 8740; orphan line-starts 1
  (P7 y553 `”».`); same-baseline collisions 1 (P1 y1712 `чёрная`). Both
  singletons are identical to core (same class, benign).

## §3 freeze — baseline 8/8 (edition AND core), diff clean

- `freeze.py baseline --build <edition> --core-svg <edition>/svg --out
  round2/freeze-ed` rc=0 → baseline 8/8. (The task's parenthetical reads
  `--build` as the core dir; that run was ALSO done:
  `freeze.py baseline --build core-ru --core-svg core-ru/svg --out
  round2/freeze-core` rc=0 → baseline 8/8. Both readings green.)
- `freeze.py diff --core-svg core-ru/svg --edition-svg <edition>/svg`
  rc=0 → `round2/freeze-diff.json`: removed distinct 361 / count-sum 529.
- Cyrillic-bearing removed (15 items, count-sum 15, all P8): Билибин,
  Билибина, Зимняя, Иван, Ивана, Иллюстрация, Морозко, год, достояние,
  иллюстрация, к, можно, ноябрю, общественное, сказка — i.e. exactly Q46
  `можно` ×1 + the 14 Morozko-caption words (core P8 caption zone y≥2450;
  edition skips the image by design, `Морозко` absent from edition P8).
  Unexplained: none.
- Added CJK (freeze `cjk_added_total`): Han ideographs 0, kana 0,
  Hangul total 2,832 (reader explanations only). No Chinese/Japanese residue.

## §4 p8 — extract 150/150, compare CLEAN, keydiff [137,138,139,140]

- `p8.py extract` core P8 → 150 noted; edition P8 → 150 noted
  (`round2/core-p8.json`, `round2/ru-ko-p8.json`).
- `p8.py compare --core-p8 … --edition-p8 … --total 150` rc=0:
  `status: CLEAN  missing=[] extra_count=0 uncertain=[]
  keydiff=[137, 138, 139, 140]` (`round2/ru-ko-p8-compare.json`).
- Direct keydiff vs core `ru-p8.json` (150 keys): `[137, 138, 139, 140]`.
  Key 20 = `желании`; keys 25/26/27/28 = `b/d/c/a`; key 73 = `заказов`;
  key 150 = `✓` (both). Keys 137–140 are the designed Korean translations.
- NOTE (my driver bug, corrected): my first regex looked for `verdict:`
  in compare stdout; the tool prints `status: CLEAN`. Corrected value is
  CLEAN per stdout + JSON (see `gates.json` `fails_corrected`).

## §5 occlusion — 42 TEXTX, 0 LINEX, adjudicated 42/42 CLEAR

- `occlusion_audit.py --selftest` rc=0: planted classes fired
  {BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX} ×1 each; clean controls silent.
- Audit on edition `svg/`: 42 flags, all TEXTX; 0 LINEX/COVER/FOOTER/EDGE/
  BOXTITLE. Per page: P1 10, P7 8, P4 7, P2 6, P6 4, P3 3, P5 2, P8 2
  (`round2/ru-ko-occlusion.json`).
- `adjudicate_ru.py <json> <edition>`: `Counter({'CLEAR': 42})`, rc=0.
- PLUS independent PDF-pixel adjudication (`round2/adjudicate_pdf.py`) on
  the DELIVERED print PDF rendered at 1950×2700 (SVG coords 1:1, SX=1.0 —
  the script's hardcoded 1950/1800 is wrong for this 1950-wide SVG and was
  NOT relied on): 41/42 CLEAR by gap-column scan. Flag 38 (P7,
  `Кипренского` vs `, 1827`, claimed 3.5 px) was resolved by direct column
  measurement: column x=556 is fully background (min pixel 249 over the
  band) between `Кипренского` ink (ends 555) and `,` ink (starts 557);
  the crop `round2/flag38-crop.png` (delivered-PDF pixels) shows the
  caption `портрет Ореста Кипренского, 1827 год.` clean. My adjudicator's
  dark-background polarity misfired there (it sampled the portrait image
  above the caption). Final: 42/42 CLEAR.

## §6 print/web text layer — multiset identical, pdftotext byte-identical

- Both PDFs 8 pages. Print 22,007,810 B; web 3,513,230 B (< 7 MB).
- PyMuPDF (fitz) non-whitespace char multiset: identical overall AND on
  each of the 8 pages; 26,535 chars each.
- `pdftotext` on both PDFs: 58,692 B each, outputs BYTE-IDENTICAL
  (`cmp` clean). (KIT §5's "58,554" is stale vs the current files; the
  authoritative multiset gate above is green.)

## §7 s11 / §1.1 — FAILURES: none, P8 min font 9.75 pt

- `s11_check.py <edition>` rc=0, `FAILURES: none`; P8 min font 9.75 pt
  (SOP §1.1 floor, at the allowed minimum — not a defect).
  Checks passed: 8 SVG, paper `#fbfaf6`, no `#f7f1e2`/`#c9a227`/`#8b4513`/
  `#000000`, badges A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f`, foot VOL.4 +
  full-width space, VOL.3 only in P4 correction, masthead 196 px, band
  46 px, left margin ≥ 87. Full stdout in `round2/gates.log`.

## §8 creambox — 0 negative, 96 BELOW-WINDOW all classified, vs-backup diff 3

- `creambox.py` (hidden_files/w47/tools/, the canonical consolidated scan)
  on all 8 SVGs: inside-only negative clearance [] (0); BELOW-WINDOW 96
  lines: +28.0 ×25, +32.0 ×41, +34.0 ×4, +37.0 ×25, +44.0 ×1 — all within
  the classified ranges (next-block lines +24..+37; the +44.0 line is the
  P1 quick-quiz header pointer `1면을 읽고 정답을 고르세요　정답은 8면` at
  y=2348.0, by design). Unclassified: [] (`round2/creambox.log`).
- Vs first-build backup scan (`scratch-refanout-ru/backup-old/…/svg`):
  exactly 3 content diff lines, all the D1a fix
  (`-'роди' -'나' +'роди나'`), everything else identical
  (`round2/creambox-vs-backup.diff`).

## §9 kicker — min gap 5.9 px ≥ 4

- P1 kicker row (y=372), PIL whole-run `getbbox`, INVEST-NOTE tokenization
  (11 tokens incl. detached `,`): gaps
  `[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]` px; min 5.9 ≥ 4.
  Full string: `ЕЖЕНЕДЕЛЬНАЯ  ГАЗЕТА  ДЛЯ  ИЗУЧАЮЩИХ  РУССКИЙ  ЯЗЫК  —
  НАСТОЯЩАЯ  РОССИЯ,  ПО-РУССКИ` (9 double spaces landed).

## §10 box-title sweep (own code) — 0 violations; P1 stats box clear

- `round2/boxtitle_sweep.py`: PIL true-ink box (`occlusion_audit.ink_box`,
  same fonts) for all 5,260 text elements across 8 pages vs page bounds
  and smallest containing rect (tolerance 1.0 px): 0 violations of any
  kind (PAGE-BOUNDS / LEFT- / RIGHT- / BOTTOM-OVERFLOW).
- P1 stats box (cream rect x=538.5 y=1174.01 w=422.5 h=380 → right 961.0):
  title row y=1211.01 runs `ТУР` (556.5) + `В` (604.7) + `ЦИФРАХ` (625.4)
  + `　숫자로 보는 라운드` (726.6): PIL ink right 931.9, advance right
  931.7 → clearance 29.1 px; delivered-PDF pixels: rightmost ink inside
  the box in the title band x=928 → clearance 33 px. The sibling
  ru-de/ru-en +36.6/+37.9 overflows do NOT reproduce. Crop:
  `round2/p1-stats-crop.png`.

## §11 D1 / D2 / D6 / map-ko (re-verified)

- D1: text.md L459 `УЧЕБНЫЕ ДАННЫЕ`, L504 `Три уровня, три темы`, L596
  `Большой тест недели`; SVG P6 (s1 + disclaimer), P7 (s3), P8 (s4) — all present.
- D2: text.md `Международный день студента` ×2 (edition) = ×2 (core);
  `День студента` ×11 in edition text.md; Q25 option is the short form
  (text.md L187; P2 render; P8 key 25 = `b`).
- D6: text.md `желании` ×2 (L173 exercise + L694 keylist); P8 key 20 = `желании`.
- map-ko: `map-ko.json` contains `родина` and `синоптики`; text.md L99
  (`роди나` → `родина`) and L538 (`си놉틱스` → `синоптики`) clean.
- Mixed-script sweep (corrected — first attempt concatenated all SVG text
  into one string and produced cross-element false positives; corrected
  method is per-element, per-whitespace-token): 0 mixed Cyrillic+Hangul
  tokens, 0 Han tokens, 0 kana tokens in SVG text; 0 Han / 0 kana chars
  in text.md (`round2/mixed-sweep.txt`). The 4 mixed tokens found in
  text.md are the gloss "(a + Korean topic particle)" at L498/499/780/781
  — Cyrillic A U+0430 followed directly by Hangul NEUN U+B294, i.e. the
  authored map value for "a + indicates contrast", consistent with
  core "a + indicates contrast" and en "a marks a contrast"; not a defect
  (see PROOF-NOTE section 5).

## §12 150-question check (keycheck.py / keycheck2.py)

- 130 tagged exercise lines in edition AND core (matching sets
  25–28/39–42/57–60/75–78/141–144 untagged in both — same-as-core).
- Stems: 0 diffs vs core. Key heads: 0 diffs vs core except designed
  137–140 (Korean translation keys) and Q150's appendix form (D-1).
  Note-only diffs (head same, explanation language differs): 138 — all
  Chinese → Korean, by design.
- Keylist (`## Answers`): 150/150 both, no missing. P8 printed keys vs
  text.md keylist heads: only Q150 differs (D-1).
- Hand-verified: Q20 (`о своём желании`, prepositional — correct), Q25
  matching set (keys b/d/c/a, options verified on the P2 render), Q73
  (`14,4 млн заказов`, genitive plural — correct).

## §13 Korean review + D5 (recorded)

- All 341 distinct Korean segments in text.md read (`round2/korean-segments.txt`):
  no spelling/honorific/transliteration errors; no Chinese/Japanese residue
  (freeze added-Han 0, kana 0; new CJK = 2,832 Hangul chars only).
- D5 (proof1: web PDF lost the P1 italic phrase) does NOT reproduce:
  web embeds `LucernaNewsreader-Italic` + `LucernaNotoSerif-Italic`
  (pdffonts, objects 50/54); PyMuPDF spans for `«чёрная пятница»` are
  identical in print and web (Newsreader-Italic `«` + NotoSerif-Italic
  `чёрная пятница` + Newsreader-Italic `»`, space present at span level);
  pdftotext byte-identical (58,692 B). Crops: `round2/italic-print.png`,
  `round2/italic-web.png`. Recorded only; no repair.

## §14 Visual — P1–P8 full-page read (delivered print PDF renders)

- `round2/pdf-render/p1–p8.png` (fitz, 1950×2700, 1:1 with SVG): read in
  full. No overflow, overlap, clipping or misplaced element on any page;
  footers and `제 N 면 / 총 8 면` correct on all 8; P8 key list complete
  to Q150 (`150. ✓ 모범 답안은 이 면의 H란(97 단어)`).

## §15 KIT numbers

- text.md 65,069 B, print/web SHAs present and correct in WEEKLY-KIT.md.
  Two KIT nits (not defects): §5 "pdftotext bytes 58,554" vs measured
  58,692 (both PDFs, byte-identical outputs); §7 "numbers head ends
  x=913.9" vs measured 931.7 (advance) / 931.9 (PIL ink) / 928 (PDF
  pixels) — artifact is fine in both cases.

## §16 Result

- Gates: all green EXCEPT the one content defect D-1 (text.md L836 Q150
  appendix form — see PROOF-NOTE §2). Conclusion: (b) — DEFECTS FOUND,
  CANNOT FINALIZE. Fix is exporter-side (`ru_textmd.py:616`); after the
  fix, only text.md (+ KIT numbers) needs regeneration and re-proof;
  print/web PDFs need no rebuild.
