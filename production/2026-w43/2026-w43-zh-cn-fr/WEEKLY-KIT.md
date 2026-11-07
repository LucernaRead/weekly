# WEEKLY-KIT — Lucerna VOL.1 · zh-CN × FR (Simplified Chinese text · French explanations)

Week 2026-10-19 → 2026-10-25 (W43) · 8 pages · 1950×2700 · 4 columns · ivory #f7f1e2
Build: `hidden_files/weekly-report-zhcn-fr-build/` · Output: `files/weekly-report-zhcn-fr/`
Status: built, builder-proofread (see PROOFREAD RECORD), geometric audit adjudicated clean.
**Independent proofread: PENDING** (separate step, not part of this build).
Not inserted into the repo, not posted to Discord (delivery paused).

## IDENTITY

- Edition: the Simplified Chinese weekly VOL.1 re-aimed at **French-speaking
  readers** — every Chinese article, stem, option and key is the frozen core's
  （简体正文 + 英语讲解， `files/weekly-report-zhcn-vol1/`); the entire explanation
  layer (glosses, grammar notes, instructions, section glosses, chart notes,
  P7 clinic/readers' notes, all 150 P8 answer notes) is rewritten natively in French.
- Masthead: **Lucerna** (unchanged, no article — Chinese is article-less).
- Pairing badge, P1, brick red #a4553a bold, directly under the masthead rules:
  « TEXTES EN CHINOIS SIMPLIFIÉ · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES
  LECTEURS FRANCOPHONES » (19.5 pt sans bold, measured 1079.7 px — fits the
  1820 px measure on one line; the prescribed text needed no shortening).
- P1 edition line (KO×FR pattern): « HEBDOMADAIRE CHINOIS · VOL.1 · 双11 · 大闸蟹 ·
  霜降 » at 40 pt serif bold, measured 1078.6 px — the HEBDOMADAIRE variant fits,
  so the JOURNAL-style fallback was not needed.
- Footers on all 8 pages: « Lucerna · HEBDOMADAIRE CHINOIS VOL.1 · TEXTE EN
  CHINOIS SIMPLIFIÉ · EXPLICATIONS EN FRANÇAIS » (measured 991.3 px) /
  « Page N sur 8 ».
- Gloss prefix: « Note — » everywhere (house style of the ×FR editions); the
  layout library's instruction-line method is named `expl()` in this build.
- Instruction words: Complétez / Associez / Écrivez.
- Bilingual section heads (Chinese head + French second half) throughout,
  e.g. « 满减怎么玩 · Le principe du 满减 », « 练习 · Exercices »,
  « 答案 · Réponses — par page, avec une note pour chaque réponse »,
  key group headers « — Page N — ».
- French number style in the apparatus prose: decimal comma (57,5),
  thousands space (10 100), percent with space (25,8 %). Chinese text, printed
  data and answer keys keep the core's forms.
- P8 answer keys print as « key (note) » — a space before a half-width
  parenthesis. All 150 registry notes are written without CJK characters and
  without internal parentheses (pinyin is used for Chinese terms), so the
  typesetter's CJK-pair rule never widens a note parenthesis: all 150 printed
  key lines verified half-width (the only full-width parentheses on P8 sit
  inside frozen Chinese exercise stems, byte-identical to the core).

## METHOD

1. Copied the core's finalized build (`hidden_files/weekly-report-zhcn-build/`,
   post-rework, post-proofread) to `weekly-report-zhcn-fr-build/`. The core's
   directories were never edited.
2. **Baseline proof before any edit:** the unmodified copy, with output paths
   first patched to a /tmp dump dir, rebuilt SVGs **byte-identical to the
   shipped core on all 8 pages**, registry identical (150; A2 56 · B1 65 ·
   B2 29; pages 10/18/18/18/18/18/12/38; writing model 148 chars).
3. Rewrote only the explanation layer, file by file (content12/34/56/7/8,
   bslib4 gloss prefix + footers + badge), via exact-match replacements with
   asserted occurrence counts (318 substitutions). Output paths →
   `files/weekly-report-zhcn-fr/`; PDFs renamed `Lucerna-VOL1-FR.pdf` /
   `Lucerna-VOL1-FR-web.pdf`.
4. The banned intermediary term appears nowhere — paper, this KIT, and code
   (grep over build sources + final SVGs = 0 hits, either language form).

## TOTALS (measured on the final build)

- Exercises: **150** — A2 56 · B1 65 · B2 29; per page 10/18/18/18/18/18/12/38.
- Types (registry): 完成句子 68 · 单选 50 · 词汇配对 20 · 完形单选 11 · 写作 1
  — identical to the core, item for item.
- Writing model 《我的双11购物车》: 148 characters, Chinese, byte-identical
  (verified by joining the wrapped fragments in both editions).
- Visible text: 24,866 characters no-space (concatenated SVG text nodes;
  the core measures 22,853 by the same method — the French apparatus runs longer).
- Build log: zero FLOW OVERFLOW, zero HEAD TOO WIDE on the final build
  (one initial warning — the 满减 head at 437.2 px vs the 434 px column —
  fixed by shortening, see below).

## FREEZE VERIFICATION

- Registry diff vs the core registry: **n / page / level / type identical
  for all 150**; key diffs **exactly 1**, the documented reader-language item:
  - #150 key → « (question ouverte — modèle ci-dessous) » (the writing item's
    registry apparatus line, was the core's Chinese apparatus line);
    its note → « Question ouverte — le modèle est dans la section F de
    cette page, 148 caractères ».
  - The core contains no zh↔EN translation exercises (types are
    完成句子/单选/词汇配对/完形单选/写作 only), so no other key could re-aim;
    all 149 other keys are byte-identical (verified by parsing both editions'
    printed P8 key lines), and all 150 notes are new French.
- Full text-node multiset diff vs the core SVGs, per page: every differing
  node classifies as French apparatus / badge / footer. The only pure-Chinese
  deltas are (a) the footer page markers （第 N 版 / 共 8 版 → « Page N sur 8 »),
  (b) wrap-point fragments of mixed paragraphs whose Chinese segments are
  unchanged (P7 B1 explanation line, P8 model-answer paragraph — the model
  text itself verified byte-identical after joining). The FR CJK character
  set is a subset of the core's (only 解， from the core's 英语讲解 furniture,
  is absent) — no Chinese character was introduced or altered.
- P7 phrases: the 8 Chinese quotes + page tags verified — each quote occurs
  exactly 2× in the issue (source + P7, reading-order-joined count, identical
  counts in core and FR), byte-verbatim Simplified excerpts; only their
  translations are new (French), tags stay « (p. N) ».
- Images: embedded payloads byte-identical to the core on every page
  (counts per page 1/1/2/2/1/2/0/0); credits identical in substance — the
  « Photo : » label is French style and the 1896 credit's « unknown author »
  is rendered « auteur inconnu »; artist names and licenses unchanged
  (Map hobby; Paul Gilmore; PushpaKhan; Gerda Arendt; noahsilliman; Syced;
  Fumikas Sagisavas ×2 — all CC0 / public domain).
- Facts unchanged, re-verified against the 2026 calendar: 双11付尾款周 lead
  (Tmall tail payments Tue Oct 20, 20:00); hairy-crab figures (Xinfadi ~3两
  females ¥77.5/斤 → ¥57.5/斤 Oct 6, −25.8 % labeled as computed); 重阳 2026
  retrospective Sun Oct 18; 霜降 Fri Oct 23. Zero politics, as the core.
- Traditional-character audit: OpenCC t2s over all visible text — **zero**
  traditional forms (the Chinese is Simplified only, as in the core).
- English-apparatus remnants: **zero**. All 150 registry notes are French
  prose with no CJK and no English function words (programmatic scan); every
  remaining Latin string on the pages classifies as French apparatus, pinyin,
  or a proper noun (Lucerna, Tmall, JD.com, NBA, S16, LPL, Weibo, Xinfadi,
  Sina Finance, The Beijing News, Wikimedia Commons, CC0, team/person names).

## LAYOUT ADJUDICATIONS (French fitted to core geometry; wording only)

- **Shortened bilingual heads / box titles** where real-font measurement
  required it (column measure 434 px; box inner width 398 px):
  « 满减怎么玩 · Le principe du 满减 » (391.0 px; the literal « Comment marche
  满减 » measured 437.2 and tripped HEAD TOO WIDE),
  « 本周生活小日历 · Les dates » (299.3 px; « Les dates de la semaine » 459.6
  would have spilled the box — the core's own history had a 14 px spill at
  this very title; not repeated),
  « 节日小日历 · Calendrier des fêtes » (389.3 px; « Petit calendrier des
  fêtes » 448.0 spilled), « 体育小日历 · Calendrier sportif » (364.0 px;
  « Petit calendrier sportif » 422.6 + 22 offset spilled),
  « 大家在搜什么 · Ce que l'on cherche » (374.9 px; « Ce que tout le monde
  cherche » 485.1 spilled the hot-search box),
  « 蟹的小知识 · Le crabe en bref » (342.4 px),
  « C · 读图与换算 · Le graphique » (374.4 px), « C · 时间换算 · Fuseaux
  horaires » (397.8 px). Worst surviving case: « 这一周的高频词 · Mots de la
  semaine » ends 7 px inside its box border, verified in the render.
- **P8 keys:** French notes are longer than the core's English; they still
  fit the core geometry unchanged — the keys flow ends col 3/3 at y=2502,
  ≈74 px clear of the 2580 footer rule (build log + audit). No note needed
  tightening; no size or leading change.
- **P7 columns** end at y=1220 / 1217 / 1353 (core: 1187 / 1184 / 1255) and
  the teaser box ends at 2519.2 (core: 2514) — all clear of the footer band.

## GEOMETRIC OCCLUSION AUDIT RECORD (SOP addendum + thin-line supplement)

- Script: `hidden_files/weekly-report-zhcn-fr-build/audit_zh_fr.py` (kept with
  the build). Paint-order scan of the shipped SVG stream; ink band = baseline
  −0.88 em … +0.30 em; widths from the production font metrics; shape boxes
  expanded by half the stroke width. Checks: (a) later opaque shape covering
  ≥30 % of a text ink band, (b) text ink intruding into the footer band
  (below y=2580), (c) text ink past a page edge, (d) any later-drawn thin line
  crossing a text ink band, (e) text–text ink-band overlap (>4 % of the
  smaller), (f) box-title spill (a text starting inside a filled box must end
  inside the smallest containing box).
- **Validation:** synthetic positive control fires all defect classes
  (COVER, LINEX, FOOTER, TEXTX, BOXTITLE each confirmed); a clean synthetic
  page is silent.
- **Result on the shipped SVGs: 2 flags, both adjudicated non-defects:**
  1. P1 TEXTX — masthead wordmark « Lucerna » (168 pt) vs the edition line
     below it: a measurement-band artifact of the blackletter's tall ink
     band; the rendered page shows clear air between the wordmark and the
     HEBDOMADAIRE line (crop-verified). Same geometry as the shipped core,
     which carries the identical adjudicated pair.
  2. P2 LINEX — the gold rule at y=1804 vs the conservative ink band of
     « Retenez la phrase : … » (baseline 1800, band bottom 1806.2).
     Pixel adjudication on the rendered card: the lowest actual text ink
     (the descender of « p » in « phrase ») ends at y=1802 and the rule
     occupies y=1803–1804 — **1 px of clear air, no contact, nothing struck
     through**. Left as the core's geometry.
- Zero coverage, zero footer-band intrusions, zero edge spills, zero
  box-title spills on all 8 pages. Kinsoku line-start scan on the final text
  nodes: 0 lines begin with closing punctuation.
- All 8 card PNGs viewed page by page: no covered, clipped or struck-through
  text; badge, footers, boxes and the P8 key columns all sit as designed.

## PROOFREAD RECORD (builder's full pass, completed before handoff)

- Full read-through of all 8 rendered pages + extracted text: every French
  gloss, instruction, grammar note, clinic rule, chart note and readers'-
  corner line read against the Chinese it explains; all 150 P8 notes read
  against their stems and articles (incl. chart arithmetic 251.928 −
  249.193 = 2.735; crab drop 20 ÷ 77.5 ≈ 25.8 %; practice-example and
  writing-model arithmetic 260+60+40=360, −50 → 310, deposit 30 → balance 280).
- French checked for spelling, accents, agreement and punctuation
  (’ apostrophes, « » guillemets, space before % and two-part punctuation,
  decimal commas in apparatus prose).
- Dates/weekdays re-checked against the 2026 calendar (Oct 19 Mon …
  Oct 25 Sun; 重阳 Sun Oct 18; 霜降 Fri Oct 23; 立冬 Nov 7; S16 Beijing
  conversions Oct 24 01:00 / Nov 15 03:00; NBA Beijing Oct 21; women's
  final Oct 22 01:30).
- Reproducibility: a scratch rebuild from the build sources reproduces all
  8 shipped SVGs byte-identically.
- **Independent proofread: PENDING** — to be completed by a fresh reviewer;
  this edition is not final until that pass finds zero problems (SOP §8).

## VOL.2 promises carried over in French (must be honoured next issue)

S16 Swiss-stage results for the four LPL teams (AL / BLG / TES / IG);
双11 delivery follow-up — did the parcels arrive?; 立冬 (Nov 7) preview;
real readers' letters + the best P8 writing (《我的双11购物车》), replacing
the labeled editor's example in the readers' corner (P7 note, French).

## DELIVERABLES (this directory)

- `svg/` — 8 page SVGs (p1-touiban … p8-ceyan) · `cards/` — 8 PNGs (1950×2700)
- `Lucerna-VOL1-FR.pdf` — print PDF, 67,691,279 bytes ·
  sha256 8a5ec2f72b98a84ed0161665c03bc46021eaa0c3f2109bb05929d0957af642cf
- `Lucerna-VOL1-FR-web.pdf` — web PDF (JPEG pages q85 @1400px),
  **3,252,490 bytes (< 10 MB)** ·
  sha256 37631ed7f213f830393aabd53d8b7800001f02ed9ed5d339cfc7667e728ad19a

## REPRODUCTION

```bash
cd hidden_files/weekly-report-zhcn-fr-build
/tmp/wp-venv/bin/python run.py        # -> files/weekly-report-zhcn-fr/svg/ (registry = 150)
/tmp/wp-venv/bin/python render.py     # -> cards/ + Lucerna-VOL1-FR.pdf + Lucerna-VOL1-FR-web.pdf
/tmp/wp-venv/bin/python audit_zh_fr.py --selftest   # positive control must pass
/tmp/wp-venv/bin/python audit_zh_fr.py ../../files/weekly-report-zhcn-fr/svg
```
Venv `/tmp/wp-venv` (cairosvg, pillow, pypdf, opencc). Never use
/opt/meta-chromium (hangs in this VM).
