# PROOF-NOTE — Lucerna Weekly 2026-W47 en-ru, proof2 (Q73 delta rebuild)

- **Edition:** English target, Russian reader (en-ru), VOL.4, 8 pages, 150 exercises
- **Proofreader:** independent proof2 (SOP §8.4), not the delta builder, not fix1
- **Date:** 2026-11-11
- **Object:** the Q73 delta rebuild (fix2). SHAs verified on disk **before and after**
  this round — unchanged by my work (I wrote nothing into production; all
  re-renders ran only in this scratch dir).

| File | Bytes | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-ru.pdf` (print) | 29,241,520 | `a42edc0e0bd0b7bbcac0163ad70639a1b400cb2cf6df4584db4f544f76c5d594` |
| `The-Lucerna-VOL4-en-ru.web.pdf` (web) | 2,452,562 | `9e636240016e11c0b3738f9389d66f7b6f6729f1385c2cb0a379fe9f3f873a09` |
| `2026-w47-en-ru.text.md` | 62,381 | `78c1b137e66571faf5bc51366f05edebfde152e0b30d717b926d1c92505794a4` |

All three match the brief exactly. Both PDFs 8 pages, 1462.5 × 2025 pt.
Core-en (control) SHAs unchanged by this round: freeze baseline re-hashed the
shipped core SVGs before AND after (`core integrity: shipped core SVGs unchanged`,
8 files), first hashes p1 `a9a8deaf76e61cb2…`, p2 `979747160de01d67…`,
p3 `efb83ce76688554b…` — identical to the delta record.

## Verdict: (a) — zero findings. en-ru is final.

No defect found. proof1's (b) D1 is fixed and retained through the delta rebuild;
the delta's Q73 key is correct in all four sources and fits its stem; every
mechanical gate re-run independently is green; the full text (1,305 lines) was
read and all 150 keys were hand-verified stem-by-stem.

## 1. Q73 — four-source consistency (the delta's whole point)

| Source | Value |
|---|---|
| `content56.py:49` | key `"up"`, note `"speak up = говорить открыто"`, stem `"Speak ___: tell a teacher."` |
| registry n=73 | key `up`, note `speak up = говорить открыто` |
| text.md:1151 | `73. [A2] Дополнить предложения — up (speak up = говорить открыто)` |
| P8 printed key | extract key 73 = `up`; SVG answer segment `73. up · 74. d · 75. a ·`; rendered P8 answers strip (zoom crop `render/p8-p5top-zoom.png`) reads `72. rights (right = право) · 73. up · 74. d · 75. a` |
| P5 stem + gloss | `Speak ___: tell a teacher.` in place; gloss `speak up = говорить открыто` in place; P5 contains no `73. up` (correct — the key is never printed on P5) |
| core-en control | `content56.py:49` key `up` (note `speak up = 大声说出来` — reader-language note, expected difference); core registry Q73 = `up` |

Diff scope — exactly minimal, re-measured from the delta's own snapshots:
- Registry diff (`registry-pre.json` vs `registry-new.json`): **exactly 1 entry**,
  n=73, `key: "speak"` → `"up"`, note unchanged; other 149 entries byte-identical.
- text.md diff (`text-pre.md` vs shipped): **exactly 1 line**, 1151,
  `— speak (…)` → `— up (…)`; −3 bytes (62,384 → 62,381).
- SVG diff (pre-delta `svg-pre.sha256` vs shipped): **only `p8-test.svg` changed**
  (`9cd7c8da…` → `873e92fe…`); p1–p7 byte-identical to pre-delta. Correct and
  expected: the key is printed only on the P8 answers page, never on P5.

## 2. D1 regression — fix1's P1 SEARCHES gloss, retained (triple re-measured)

| Place | Repaired value (verified) |
|---|---|
| `content12.py:85` | `p.text(gx + 22, byy + 76, "Относительный интерес, не точные.", 19, "sans", False, GREY)` |
| `scratch-fanout-en/map-ru.json:228` | `"相对热度示意，非精确搜索量。": "Относительный интерес, не точные."` |
| P1 SVG | gloss `Относительный интерес, не точные.` in place; old string `не точные цифры` **0×** in `content12.py`, P1 SVG (and 0× in map-ru.json value) |

Three independent measurements, all inside (fix1's numbers reproduced exactly):
1. **SVG advance** (`svglib.text_w`, same function the sweeps use): new gloss
   339.4 px, starts x=1461.5, ends 1800.9 → **margin +61.1 px** (box right edge
   1862.0). Old gloss re-measured 409.0 px → −8.5 px (the proof1 defect).
2. **Print-PDF ink** (PyMuPDF spans): span x[1096.1, 1351.3] pt vs box
   x[1079.6, 1396.5] pt → **right margin +45.2 pt**.
3. **Rendered pixels** (150 dpi print render, `render/print-p-1.png`): rightmost
   ink pixel 1349.3 pt → **margin +47.2 pt**. P1 viewed: the gloss sits inside
   the cream box with clear space to the right.
   H-SPILL total for the whole issue is now **0** (was 1, this gloss, in proof1).

## 3. 150 keys — hand-verified stem-by-stem (Q73 lesson: consistency is not enough)

- Full text.md read, lines 1–1305. Mechanical 3-source cross-check
  (registry vs P8-extract vs text.md answers): **150/150**, with only the known
  n=150 short-label exception (P8 extract truncates the open-writing key to
  `Открытый вопрос`; registry and text.md carry the full string — same
  exception as proof1/fix1, adjudicated in keycheck as `exc=[150]`).
- Stub re-run of the content sources (`keyfit2.py`, my copy): stub items 150 =
  registry 150, **key mismatches: NONE**. All **57 blank/rewrite items**
  hand-checked key-into-stem: Q1 midterm, Q2 call, Q3 seats, Q4 majority,
  Q5 changed, Q6 January, Q11 November, Q12 January, Q13 1, Q14 Thursday,
  Q15 27, Q16–19 will-forms, Q34 opens, Q35 mentor, Q36 twice, Q37 jungle,
  Q42–45 past-simple rewrites, Q52 hosted, Q53 lasts, Q54 eight, Q55 won,
  Q60–63 past-simple rewrites, Q70 silence, Q71 socks, Q72 rights,
  **Q73 up ("Speak up: tell a teacher.")**, Q78–81 present-continuous rewrites,
  Q94 certify, Q95 call, Q96 changed, Q97 takes, Q98 differs, Q99 official,
  Q100 won, Q101 more, Q102 lost, Q103 will, Q104 published, Q105 whether,
  Q106 chose, Q107 win, Q133 will meet, Q134 won, Q135 more, Q136 whether —
  **all form grammatical, correct sentences; 0 mismatches**.
- All **14 direct-reg items** hand-checked: Q112 Tuesday, Q113 call,
  Q114 continues, Q115 will meet, Q116 writes, Q117 will certify, Q118 wears,
  Q119 will watch (P8 cloze passage, internally consistent); Q145 row,
  Q146 film, Q147 popcorn, Q148 show, Q149 Friday (dialogue; film opens
  Friday, November 20); Q150 open writing. **0 mismatches.**
- All matching blocks in definition order: Q24–27 b/c/a/d, Q38–41 b/a/d/c,
  Q56–59 b/c/d/a, Q74–77 d/a/b/c, Q141–144 b/c/d/a.
- Weekdays re-verified with `date -d` (America/Toronto): Nov 3 Tuesday,
  Nov 16 Monday, Nov 20 Friday, Nov 21 Saturday, Nov 26 Thursday
  (Thanksgiving), Nov 27 Friday (Black Friday).
- Arithmetic re-checked: 254+162+19=435 ✓; 20+13=33 of 35 ✓; 254−218=36 ✓
  (P7 "254 is 36 more than the majority"); Q87 key C (435) ✓.
- P8 MODEL text is 82 words (counted), inside the 80–100 prompt range.
- Content facts: no new English content vs proof1 (freeze diff: only
  re-segmentation of identical English strings + Russian additions + Chinese
  removals). The issue's announced-results premise (254/162/19, 7 flips,
  5 governors, certification Nov 10–Dec 18) is internally consistent across
  P1/P2/P6 and the chart; Ashes/sport/film facts are those proof1 verified
  against live sources the same day.

## 4. Verified clean (summary — per-gate evidence in GATE-LOG.md)

- **run.py** (scratch copy, full rebuild): rc=0, TOTAL exercises 150,
  MODEL words 82, OVERFLOW/TOO WIDE 0. Fresh SVGs **8/8 byte-identical** to shipped.
- **render.py** (scratch copy): rc=0, 8 pages, 1462.5×2025 pt. Third run
  reproduced the shipped print PDF **byte-for-byte** (SHA `a42edc0e…`,
  29,241,520 B) — see observation below on run-to-run byte variance.
- **freeze baseline, standard** (`--build` core-en, `--core-svg` core-en/svg):
  **8/8** byte-identical; core integrity confirmed. **Supplement**
  (`--build` edition, `--core-svg` edition/svg): **8/8**, p8 `873e92fe…`.
- **freeze diff**: TOTAL added CJK **9, all U+3000** (2+1+1+1+1+1+1+1).
- **occlusion audit** (real audit, no `--selftest`): **0 flags**; selftest OK
  (6 planted classes fired, clean controls silent); `occlusion.json` flags `[]`.
- **p8 extract + compare**: 150/150 extracted; noted 60/150 both core and
  edition, same set; compare **CLEAN**, missing=[] extra=[] uncertain=[],
  keydiff **[137, 138, 139, 140, 150]** (expected: reader-language translation
  keys + writing short label).
- **keycheck**: registry-vs-P8extract **149/150 + exc=[150]**, mismatch=[];
  registry-vs-core **145/150**, diff only 137–140, 150 — **Q73 now matches
  core** (fix1 was 144/150 with Q73 differing); noted set == core noted True;
  Q38–41 `['b','a','d','c']`, Q125 A, Q46 A, Q52 hosted, Q55 won, Q82/83/84 B C A.
- **Print/web text identity**: pdftotext both 54,726 chars each; per-page
  byte-identical **8/8** (5556/6621/5756/6182/5175/6110/7379/11947 B);
  token-multiset diff **0/0**. Scratch re-rendered print and re-rendered web
  PDFs are also per-page byte-identical to the shipped pair (8/8 each).
- **webpdf** (scratch only, never over the shipped file): rc=0, 8 pages,
  2,452,554 B (shipped web 2,452,562 B — SHA/bytes float per run as briefed;
  only the text layer is compared, and it is identical).
- **P8 min font**: **10.12 pt** ≥ 9.75 pt floor (PyMuPDF, independently
  measured); P1 min 11.62 pt; all pages min ≥ 10.12 pt.
- **creambox** (canonical PIL true-ink scan): rc=0; inside-only baseline
  clearances all positive (min +5.0 px, P2 AND YOU? box); P7 toolbox 7 boxes,
  min inside clearance +47.7, min desc-clear +41.6. See tight item below.
- **h-containment**: **H-SPILL total 0**; V-SPILLs 28, all +6.0/+13.7
  next-block headings below boxes (design spacing, same pattern as proof1).
- **boxtitle**: source sweep 12/12 fit (tightest ODD SOCKS 398.3, +6.2);
  SVG sweep 18/18 fit, 0 overflows.
- **check_s11**: ALL §1.1/P8 CHECKS PASS. **verify_ed**: VERIFY ALL PASS
  (Q39 a / Q40 d / Q125 A; P8 min 10.12 pt; SVG zero real CJK).
- **Quotes/banned/orphans**: text.md U+201C 81 / U+201D 81 (balanced),
  SVGs 82/82, U+2019 = 0, U+2018 = 0; 0 Cyrillic-adjacent curly quotes;
  banned-word scan 0; **orphan visual-line scan 0**.
- **ABSTRACT**: full form, 1 line, 659 chars, Russian, 0 ASCII double quotes.
- **"next Sunday"**: 0 hits (no applicable object, as proof1).
- **Registry counts**: pages 10/17/18/18/18/18/12/39; levels A2 62 / B1 66 /
  B2 22; total 150.
- **Visual**: print P1–P8 all viewed at 150 dpi; web P1 + P8 rendered and
  viewed, identical to print. No overflow/overlap/truncation/footer-intrusion
  on any page. Footers "Страница N из 8" on all pages.

## 5. Tight-but-passing (genuinely tight, inside, recorded no-fix)

- **P2 AND YOU? box, last line "по-английски для редакции."** — baseline
  clearance +5.0 px; DESC=0.30 estimate gives desc-clear −1.0 px, but that
  estimate overstates this line's real descender: rendered-pixel measurement
  (150 dpi, text-ink only) puts the lowest ink at 1157.8 pt vs box bottom
  1158.7 pt → **+0.9 pt inside**. Same adjudication as proof1 (+0.0 px
  true-ink-bottom there, +0.9 pt rendered-pixel here — both inside, not
  crossing). The olive full-width divider below the box is a design rule,
  not a spill.
- **P5 ODD SOCKS, IN NUMBERS　Цифры** — advance margin +6.2 px, true-ink
  margin +6.5 px (source + SVG sweeps agree). Inside; tightest title.
- **P1 SEARCHES gloss vertical** — baseline clearance +12.0 px, true-ink
  +7.0 px (only its horizontal margin changed in fix1; vertical unchanged).

## 6. Minor nits (not defects — carried from proof1)

- P5 line "У каждого ребёнка есть права | Every child has rights = У каждого
  ребёнка есть права." — the Russian is repeated redundantly. Stylistic nit,
  core-rooted (same as proof1).
- Q108 correction drops "in 2026" from the error sentence — grammatical,
  not flagged (same as proof1).
- KIT §3 "P8 min font 13.5 pt" conflates SVG px with pt (same wording nit as
  proof1): the real rendered size is 10.12 pt, still above the ≥9.75 pt floor.

## 7. Observation (not a defect): render.py byte variance run-to-run

`render.py` output bytes are not fully stable across runs: three runs on the
same byte-identical SVGs produced 29,241,520 B (run 1), 43,372,505 B (run 2),
29,241,520 B (run 3). Runs 1 and 3 hash to the shipped print SHA exactly
(`a42edc0e…`); run 2's text layer is byte-identical to the shipped PDF on all
8 pages (pdftotext comparison). The variance is in font embedding, not content,
and the shipped file is the reproducible canonical output. Recorded so a future
byte-size mismatch on a re-render is not mistaken for a content defect.

## 8. D5 font inventory (recorded only, not judged — per brief)

1,798 `<text>` elements across the 8 SVGs; 26 distinct `font-size` values (px):
13.5×75, 15.5×13, 16×1, 17×34, 18×15, 18.5×2, 19×162, 19.5×71, 20×53, 20.5×166,
21×21, 21.5×183, 22×167, 22.5×9, 23×147, 23.5×131, 24×465, 25×34, 26×2, 27×3,
28×11, 32×11, 36×5, 46×15, 53×1, 196×1 (masthead). Identical to the
proof1/fix1/delta records, item for item. No judgement made.

## 9. Standing rules honored

- No source files modified, no rebuild into production, no commit/push;
  webpdf.py re-run only in scratch (`webpdf/out.web.pdf`); dump_reg.py NOT run;
  make_textmd NOT run; freeze baselines wrote only into scratch.
- The one run.py failure seen mid-round was my own scratch-copy mistake
  (missing `assets/` in the first copy — `FileNotFoundError:
  lucerna-moth.svg`); the copy was fixed and the valid run is the one
  reported above (rc=0, TOTAL 150, fresh SVGs 8/8 identical).
- Core-en was read-only throughout (hashes re-verified after the round).

## Evidence paths (this scratch dir)

`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-ru2/`
- `PROOF-NOTE.md` (this file), `GATE-LOG.md`
- `gates/` — occlusion.json/.log, p8-extract*.json/.log, p8-compare.json/.log,
  keycheck.py/.log, keyfit2.py/.log, freeze.log, freeze-edition.log,
  freeze-diff.json/.log, printweb.log, webpdf.log, run-copy.log,
  run-copy-sha.txt, render-copy.log, render-copy2.log, check_s11.log,
  boxtitle.log, boxtitle-svg.log, creambox.log, h-containment.py/.log,
  verify.log, verify_proof2.py/.log, pixel.log
- `render/` — print-p-1..8.png (150 dpi), web-p1-1.png, web-p8-8.png,
  p8-answers-zoom.png, p8-p5-answers-zoom.png, p8-p5top-zoom.png (73. up)
- `freeze-core/`, `freeze-final/` — freeze baseline re-renders (core + edition)
- `run-copy/` — scratch rebuild copy (run.py + render.py outputs; 3rd render
  reproduces the shipped print SHA byte-for-byte)
- `webpdf/` — scratch-only web-PDF re-render (text-identical to shipped web)
- `textcmp/` — pdftotext per-page outputs for the four-way text comparison
- `.probe`
