# PROOF-NOTE — 2026-W47 ru-fr · proof1 (independent proofread)

**Edition:** `production/2026-w47/2026-w47-ru-fr/` (Russian target × French reader)
**Proofreader:** proof1 (independent; session `a5288292-e5d0-86e7-d3c0-aa7e940828dc`)
**Date:** 2026-11-11
**Scope:** print PDF 8 pages (full visual read at 200 dpi) + `text.md` full read (838 lines) +
150 exercise keys hand-verified + all mechanical gates re-run independently (KIT not trusted).
**Sources:** no source file modified, rebuilt, committed or pushed. All work in
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-fr1/`.

## Identity (verified this round, disk = task)

| File | SHA-256 | Bytes |
|---|---|---|
| `Lucerna-VOL4-ru-fr.pdf` (print) | `b9476fc2d49584d134e61d59f587bd24e76f4da0caf66de03884ba86523f3629` | 21,260,891 |
| `Lucerna-VOL4-ru-fr-web.pdf` (web) | `78a56be6b7094ce1e9dd2435f174e4e8bb563e6c7363b2a2f82815dfd17128fe` | 3,346,639 (< 7 MB ✓) |
| `2026-w47-ru-fr.text.md` | `4be2d24b46e1396219b1b74af4468d27f4b62a38c2f2af539532615bce8675f6` | 63,489 |

**All three SHAs match the task.** Edition dir is untracked (`?? production/2026-w47/2026-w47-ru-fr/`).

## Conclusion: (b) — defects block finalisation

**1 blocking defect, mechanism-attributed** (web PDF, not edition content):
the web PDF loses the italic faces (ru-en D3-class), with all three symptoms
reproduced at span level. The print PDF and the model text are unaffected, and every
other gate passes — the content of this edition is clean — but the web PDF as shipped
is not fit for the site until `tools/webpdf.py` embeds the italic faces and the web
PDF is rebuilt and re-verified.

Whether the coordinator treats a web-PDF-only defect as blocking the whole edition is
their call; the defect is reported plainly with evidence below.

## Defect list

### D1 — Web PDF: italic faces dropped; italic term loses its space and its closing quote detaches [BLOCKING]

- **Severity:** medium (web/site visual fidelity + searchability). Print PDF unaffected.
- **Page / location:** P1, word-of-week term box — «чёрная пятница» (lead term, 16.12 pt).
- **Attribution:** mechanism (`tools/webpdf.py` font subsetting), NOT this edition's content.
  The same word set in upright type is fine; only the italic spans are affected.
- **Evidence (PyMuPDF span level, print vs web, same page/position):**

  | | print `Lucerna-VOL4-ru-fr.pdf` | web `Lucerna-VOL4-ru-fr-web.pdf` |
  |---|---|---|
  | term span | `NotoSerif-MediumItalic` 16.12, text `чёрная пятница` | `LucernaNotoSerif-Regular` 16.12, text **`чёрнаяпятница`** |
  | « / » spans | `Newsreader16pt-Italic` | Regular faces only |
  | italic faces in file | `Newsreader16pt-Italic`, `NotoSerif-MediumItalic` present (pdffonts) | **zero italic faces** (Regular/Bold only) |

  - **Symptom 3 — italic lost:** the web term renders upright instead of italic.
  - **Symptom 1 — space lost:** the stored web span text is `чёрнаяпятница`
    (no internal space); print stores `чёрная пятница`. (pdftotext's layout pass
    re-inserts a space from glyph positions, so a plain `pdftotext | grep` can miss
    this — the span-level text is the ground truth.)
  - **Symptom 2 — closing quote detached:** web text layer has 2× ` »` vs print 1×;
    the extra one is the web P1 `«чёрная пятница »` (print's single ` »` is the
    legitimate French `« Black Friday »` on P5).
  - Related: the upright second occurrence of the same term (P1, 15.75 pt
    `NotoSerif-Medium`) is intact in both PDFs — the defect is specific to italic.
- **Fix:** make `webpdf.py` subset/embed the two italic faces
  (`NotoSerif-MediumItalic`, `Newsreader-Italic`) the print PDF uses; rebuild the
  web PDF; re-verify with a span-level italic/font check (not pdftotext alone) and
  the print-vs-web text comparison.
- **Verification note:** web non-space character multiset equals print (30,708 chars
  each); the only multiset difference is +42 spaces / +6 newlines in web (segmentation
  noise). The italic-term loss is a stored-text difference, not a layout difference.

## Must-check items (a)–(e) — verdicts

- **(a) P1 box-title/subtitle overflow — does NOT reproduce.** PIL true-ink on the
  200 dpi render: head `ТУР В ЦИФРАХ　EN CHIFFRES` ink max-x 895.7 SVG vs box right
  edge 961; Q6 chip (B1 badge rect x=989.0, y=1146.055, `6.` at x=1061) → 93.3 px
  clear. Crop `crop-p1-head.png` visually clean.
- **(b) P3/P5 right-column cream-box descender spill — does NOT reproduce.** PIL ink:
  P3 right boxes ink bottom +68.3/+68.7 px above box bottom; P5 +63.9 px.
  The P2 "А ВЫ?" box (same class, found by creambox) is the tightest in the edition:
  last line `pour le Père Gel.` ink bottom **+1.24 SVG px above the box bottom**
  (PIL, crop `crop-p2-boxbottom.png` shows the descender inside the box) — tight but
  PASS; see observation OBS-1 below.
- **(c) P7 toolbox clearance — PASS.** Canonical creambox P7-TOOLBOX summary:
  3 boxes, min inside clearance +11.9, min desc-clear +5.9.
- **(d) text.md §E type tags — clean French, no Chinese.** Section E tags are
  `[Traduction]` / `[Traduire en français]`; no `翻譯`/`翻译` residue anywhere in
  `text.md` or `ABSTRACT.txt`; 0 CJK in `text.md`/`ABSTRACT.txt` (added CJK in the
  freeze diff is only U+3000, the SOP §1.1 separator).
- **(e) Web-PDF italic triplet — REPRODUCED, all three symptoms.** See D1 above.

## Observations (not defects)

- **OBS-1 — P2 "А ВЫ?" cream box is tight.** Creambox: box (x=1439.5, y=795,
  bottom=1159.0), last line baseline 1154.0, clearance +5.0, **desc-clear −1.0**
  (tool estimate). PIL true-ink measurement: last-line descender bottom is
  **+1.24 SVG px above the box bottom** — inside, not spilled. Recorded as a
  watch item for the next rebuild, not a defect (the tool's box model over-estimates
  the descender; true ink rules).
- **OBS-2 — P3/P5 mid-page whitespace.** Large empty middle band on P3 and P5
  (article ends ~y1150, exercises begin ~y1650). Template whitespace, not a defect.
- **OBS-3 — P7 Pushkin portrait.** Tight centre crop, top of head near the frame
  edge; identifiable. Not a defect.
- **OBS-4 — Q147** (`Проверьте промокод`, G dialogue) is under-contextualised but
  coherent (seller reminding the buyer about the promo code). Not a defect.
- **OBS-5 — Q62** (`15-й тур ___ 20–22 ноября (быть)` → `будет`): acceptable Russian,
  core-frozen wording. Not a fan-out defect.
- **OBS-6 — P1 byline `От редакцииLucerna`.** At page scale it looks joined, but PIL
  column measurement proves the word gap is **4.8 SVG px — identical to the sibling
  word space in the same line (4.8 px)** and the `Уровень|чтения` space (5.3 px).
  Not a defect; downscaled views mislead, pixel measurement rules.

## Open items

- **O1 — P5 core figure not independently verified:** "11 ноября 2025 года, на Ozon
  сделали больше 14,4 миллиона заказов за один день" (P5 article; Q73 key `14,4`).
  Internally consistent (article + Q73 + answer key agree), but no public source was
  checked for the exact figure. Single-source core figure; if the coordinator wants
  it sourced, that is a core-level follow-up, not a fan-out defect.
- **O2 — Russian cinema release dates for the five 19 Nov premieres (P3).**
  International dates verified: *I Play Rocky* (Peter Farrelly, US limited 6 Nov /
  wide 20 Nov 2026), *Paper Tiger* (James Gray, Cannes competition premiere 16 May
  2026), *You Can See Everything* (A24/Nathan Fielder & Lance Oppenheim, US 16 Oct
  2026). The Russian 19 Nov date itself was not independently verified; the
  international dates cluster in the same window, so the claim is plausible.
  Core-level, not a fan-out defect.
- **O3 — OBS-1 watch item:** P2 "А ВЫ?" box descender clearance (+1.24 px true ink).
  Re-check after any rebuild that re-flows the P2 box.

## Verification summary (all gates, own runs)

| Gate | Result |
|---|---|
| Occlusion audit (selftest OK) | 42 flags, all TEXTX, 0 COVER/LINEX/FOOTER/EDGE/BOXTITLE; **42/42 adjudicated CLEAR** (38 by polarity-free raster gap scan, 4 `Краснодар»` by crop visual — tool's ink-box overhang, glyphs do not touch) |
| Creambox (canonical, all 8 SVGs) | PASS except OBS-1 tight box (see above); P7 toolbox +11.9/+5.9; P8 has no cream boxes; P6 "BELOW-WINDOW +28.0" is a next-element false positive |
| p8 compare | core 150/150, edition 150/150, **CLEAN**, missing=[ ], extra=0, keydiff=[137,138,139,140] (E-section keys correctly re-aimed to French; core keys are Chinese) |
| Freeze baseline | **8/8 SVGs byte-identical**; core integrity: shipped core SVGs unchanged |
| Freeze diff | added CJK = U+3000 only (6, one per page except P6/P7); P8 +173/−639 strings = French answer notes vs Russian core |
| Keycheck | **150/150 hand-verified** (`keycheck-150.json`); printed P8 keys = text.md keys 150/150 (Q150 is a representation difference only: printed `✓` vs text.md parenthetical, same meaning); levels A2 50 / B1 76 / B2 24; per page 10/18/18/18/18/18/12/38 |
| P8 min font (PyMuPDF, both PDFs) | **9.75 pt** (385 spans at 9.75; size distribution identical print vs web) — at the SOP §1.1 floor, PASS |
| Print vs web text layer | non-space multiset equal (30,708 chars each); diff is +42 spaces / +6 newlines (segmentation only), except D1 |
| Curly quotes | only 2 in all SVGs: P7 `“`/`”` (Newsreader, around `чёрной пятнице`) = the stated intentional exception; no U+2019 anywhere |
| Content read | print PDF 8 pages + text.md 838 lines read in full; all pages visually clean, no overflow/overlap/clipping; footers `Page N sur 8`; P7 golden sentences 8/8 verbatim with correct page refs; P4 results table all 8 matches verified; matching option letters verified (P2 D, P3 C, P4 C, P5 C, P8 F); G dialogue read in context; model text 97 words (brief 80–100 ✓) |
| Core facts checked (external) | 1946 Prague Students' Day decision ✓; *Paper Tiger* Cannes 2026 ✓; *I Play Rocky* / Farrelly ✓; A24 Holmes documentary ✓; Nov 2026 weekdays/dates ✓ (16 Mon … 22 Sun; 12 Nov Thu; 27 Nov Fri Black Friday; 30 Nov Mon Cyber Monday; 29 Nov Sun Mother's Day; Nov 20 working + 10 non-working days ✓) |
| `vœu` spelling | correct `vœu` (1× P2 SVG, 3× text.md) — KIT's "voeu (no œ)" ruling is wrong |

## KIT claims corrected (for the record)

1. KIT's "voeu (no œ)" — wrong; the text has correct `vœu`.
2. KIT's freeze "0/8 = known redirect limitation" — wrong; the baseline run reports
   8/8 directly.
3. KIT's "ABSTRACT.txt 434 bytes" — measured 435 bytes (trailing newline); trivial.
4. "14- й" in the web PDF — a pdftotext segmentation artefact only: PyMuPDF span
   texts store `14-й тур` 17× in both PDFs, and `search_for('14- й')` finds 0 in web.
   Not a defect.

## Files delivered (scratch)

- `PROOF-NOTE.md` (this file)
- `GATE-LOG.md` (mechanical-gate evidence, external fact sources, non-defect rulings)
- `keycheck-150.json` (150 items: stem, level, type, text.md key, printed P8 key,
  core key, hand verdict, per-item note)
- `logs/` (occlusion, p8 core/edition/compare, freeze diff/baseline, creambox,
  print/web pdftotext), `render/p-1.png`…`p-8.png` (200 dpi),
  `adjudicate4.py` (polarity-free raster adjudication), `ink_check.py`,
  `build_keycheck.py`, `crop-*.png` (adjudication crops)
