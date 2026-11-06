# Lucerna 繁體中文週報 VOL.2 — 法語講解版 (zh-TW × FR) — WEEKLY KIT — W45

- **Pairing**: Traditional Chinese target text (frozen W45 zh-tw core, week of Mon 2026-11-02 – Sun 2026-11-08) + explanations written natively in French. The edition for French-speaking readers.
- **Slug**: 2026-w45-zh-tw-fr. **Masthead**: « Lucerna » (no article — Chinese takes no article, per SOP), kept exactly as shipped in the core.
- **Deliverables** (this dir): `svg/` ×8, `cards/` ×8 (1950×2700), `Lucerna-VOL2-FR.pdf` (print), `Lucerna-VOL2-FR-web.pdf` (web), this KIT, `ABSTRACT.txt`.
- **PDF pins**: print 20,075,140 B, sha256 `6323329f91ee49644957a6736d54e8e604009a184fe5d17dbf85273d5876dc27` (8 pages); web 3,478,378 B (< 10 MB), sha256 `d50c68bbfbca315a9b05504e6261b5c734a292d5441e8defc733678800b12645` (8 pages).
- **Totals (identical to the zh-tw core — read from the core KIT, NOT the zh-cn split)**: 150 exercises — A2 44 · B1 74 · B2 32; pages 10/18/18/18/18/18/12/38; types 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1. Writing model 138 characters (unchanged Chinese).
- **Status**: BUILT by the builder. **NOT finalized** — an independent proofread follows; only a zero-problem proof finalizes it. No Discord post, no `weekly-git` touch, no `insert.py` run, no edition cards/PDFs sent to main chat, no cron created.

## Production method

Fan-out from the Traditional Chinese core only, produced natively for French readers — never converted from, or copied out of, the Simplified edition. Build dir: `hidden_files/weekly-report-w45-zh-tw-fr-build/` (fresh copy of the core build `hidden_files/weekly-report-w45-zhtw-build/`; the core build dir itself was never executed or modified — read-only reference). Only the explanation layer was rewritten (English → French); the Traditional Chinese target text is frozen. All fix-layer edits live in the transform script `transform_fr.py` (main phase + FIX2–FIX5); no direct build-copy edits remain — see Gate 10 below.

**Pre-flight duplicate check** (coordinator ruling, intent = NO CONCURRENT WRITER): delivery and build dirs were created fresh; two mtime snapshots ~3 minutes apart showed ZERO changes except the snapshot files themselves; no process was writing to these dirs (two `run.py` processes visible in `ps` belonged to sibling builders working in other dirs). Pre-flight CLEAR, recorded in `preflight-snap1.txt` / `preflight-snap2.txt` in the build dir.

**Baseline proof**: `tools/freeze.py baseline` on the unmodified core build reproduced all 8 shipped core SVGs **byte-identically** (8/8) before any edit, and re-hashed the shipped core SVGs afterwards to prove them untouched:
p1-front `4672c972763b0eaf`, p2-life `889fb533ef3ff62e`, p3-culture `508703c2b3c313c6`, p4-sport `e04b62ea6211c9ff`, p5-youth `4dfce72d88000fbc`, p6-deep `06ba4c6627cb8165`, p7-lang `00ac7f57125fcc09`, p8-test `e6e97d02595aef3b`.

## Traditional-independence cross-check (HARD GATE — no conversion, no own table)

Method: extracted the Traditional (CJK) character set from the shipped SVG text of three sources — (a) this edition, (b) the W45 zh-tw core, (c) the W43 zh-tw-fr shipped edition — and compared sets directly from those files (script `checks.py` §7 in the build dir; extraction = `<text>` elements of each shipped SVG, CJK ranges U+3400–U+4DBF and U+4E00–U+9FFF). No Simplified→Traditional conversion, no OpenCC, no hand-made mapping table was used anywhere in this build.

Result: edition 766 CJK chars, core 767, W43 784; **characters in this edition outside the union of (core ∪ W43) = 0**. Every Traditional character in this edition already appears in the zh-tw core's own shipped text or in the W43 same-pairing precedent's shipped text. Zero Simplified-only characters introduced. (The one-char shortfall vs the core is the designed furniture change: the core's Chinese pairing badge/footer strings are replaced by French furniture, per the W43 precedent.)

## Three-way furniture table (all slots/sizes/colors MEASURED from shipped SVGs, not assumed)

| Furniture | W45 zh-tw core (measured) | W43 zh-tw-fr precedent (measured) | This edition |
|---|---|---|---|
| P1 pairing badge | y=378, 21pt, OLIVE #3e4c2a, Chinese+English pairing line (subtitle slot EXISTS) | y=378, 21pt, BRICK #a4553a, replaced in place | y=378, 21pt, BRICK #a4553a, same French text: « TEXTES EN CHINOIS TRADITIONNEL · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES » |
| Footer (all 8 pages) | « Lucerna · 繁體中文週報 VOL.2 · 繁體中文正文 · 英語講解 · Traditional Chinese text · English explanations » / « 第 N 版 / 共 8 版 » | « Lucerna · HEBDOMADAIRE CHINOIS VOL.1 · TEXTE EN CHINOIS TRADITIONNEL · EXPLICATIONS EN FRANÇAIS » / « Page N sur 8 » | « Lucerna · HEBDOMADAIRE CHINOIS VOL.2 · TEXTE EN CHINOIS TRADITIONNEL · EXPLICATIONS EN FRANÇAIS » / « Page N sur 8 » |
| Gloss prefix | « Notes｜ » | « Note — » | « Note — » (W43 zh-tw-fr family precedent) |
| P8 separator | « — Page N — » | « — Page N — » | « — Page N — » (unchanged) |
| P8 key style | dash « n. key — note » | dash « n. key — note » | dash, answer-generation code byte-identical (no paren interaction: the family is dash-style, so the CJK-paren conversion issue does not arise) |
| Edition line y=316 / strapline y=410 | frozen Chinese | frozen Chinese | byte-identical to core |
| Section heads | English second parts (Life, Youth, Deep read, Language focus, …) | French second parts (Vie quotidienne, Jeunesse, Lecture approfondie, Focus langue, …) | French second parts throughout, reusing W43 translations where the Chinese head matches (Tout compris ?, Complétez, À vos calculs, Quiz rapide, Mots des titres, Lire le graphique, Vrai ou faux, Le grand quiz, Lisez et répondez, En situation, À vos plumes, Test et corrigés, …) |

## Freeze verification (vs the CORE's shipped SVGs)

`tools/freeze.py diff --strict-cjk`: per-page added/removed text strings are explanation-layer, pairing furniture, or wrap-segmentation artefacts only; **strict-CJK added = 0 on all 8 pages** (p1–p8: 0, 0, 0, 0, 0, 0, 0, 0). One intermediate run showed +6 full-width ， on P7 only: svglib `_fw()` converts an ASCII comma placed directly after a CJK term into full-width ，, and six French P7 sentences had commas after Chinese terms. Fixed in the transform (FIX4) by restructuring those sentences so no punctuation follows a CJK term (e.g. « 集章, c'est… » → « 集章 veut dire… »); the final run reads 0.
Image payloads byte-identical to core on all 8 pages (counts 1/1/0/1/1/0/0/0; P4 hash `18ad8ae0…` = the core's verified Washington baseball-team photo).

## Gates (all green)

- **Registry**: 150 exercises, A2 44 · B1 74 · B2 32, pages 10/18/18/18/18/18/12/38, types 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1 — identical to core. Final render prints **ZERO FLOW OVERFLOW and ZERO HEAD TOO WIDE warnings**.
- **P8**: `tools/p8.py compare --total 150` → **CLEAN 150=150, keydiff[]** (no missing, no extra, no uncertain). Keys byte-identical to core except none: even #150's apparatus key is the frozen Chinese « (開放題，範文如下) »; only its French note changed (« Tâche ouverte — le texte modèle est imprimé dans la section F ci-dessus (138 caractères) »), and the P8 printed key line shows « 150. ✓ … » as in the core.
- **Occlusion**: `tools/occlusion_audit.py --selftest` OK (all 6 planted classes fired, clean controls silent). Final edition run: **0 flags**; `--core` run: **NEW vs core 0**. Four first-pass flags were fixed in the transform, not adjudicated away: P2 你呢 box last line 4.4px past its border (French shortened 3→2 lines); P5 box title 476.5px > 412px box width (« Le programme de Tianmu » → « Le programme », 340.5px); P6 box title 443.4px > 412px (« Comparez attentivement » → « Comparez », 260.8px); P7 letters-box last line past its border (disclosure cut 8→7→6 wrapped lines, then box-height constant +30px once the formula shortfall was confirmed — see fix record).
- **Same-baseline ink collisions** (PIL/TC-font scan, all pages, furniture bands included): **0 flags** (gap < 2px criterion).
- **P6/P4 chart-label element check** (text ink vs later-drawn bar rects): **0 overlaps**. Bar widths unchanged from core: P4 120.0 and 600.0 px (= 1 and 5 runs × 120); P6 600.0, 800.0, 800.0, 800.0 px (= 6, 8, 8, 8 hours × 100).
- **Gloss counts item-identical**: `gloss()` calls core = edition = 12 (P1 2, P2 2, P3 3, P4 2, P5 2, P6 1); `glossline()` calls core = edition = 4 (P7 3, P8 1). No gloss string in this core contains a `·` item separator, so README #21's split-counting case does not arise; every gloss box's French text is present in the render (freeze-diff added strings).
- **P7 golden sentences**: all 8 verbatim from this issue's own articles (bracket-stripped inner text, since articles carry no 「」), **exactly 2 occurrences each** (article + P7), correct page tags (p. 1, 1, 2, 3, 3, 4, 5, 6).
- **Readers' corner**: frozen Traditional disclosure byte-identical in the render (« 延期披露：VOL.1曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。 ») + French disclosure stating no genuine letters exist (« Lettre d'exemple — pas une vraie lettre. Avis de report : … aucun texte publiable n'était arrivé … ») + explicit open invitation in French (« … l'invitation reste ouverte : écrivez-nous ! »).
- **P7 geometry**: col3 ends 1744.86 (core 1745.36), teaser ends 2542.86 (core 2543.36, footer rule at 2580 — clear); A2 column ink max 1551.35 ≤ 1560 design bottom (flow-end 1594 is trailing gap only); B1/B2 flow ends 1529.
- **Residual-Latin adjudication**: every Latin string in the edition SVGs was listed and classified one by one. French explanation layer throughout; frozen target-text citations byte-identical to the core (event theme « Fintech Nexus: Bridging the World, Building the Future », StartmeupHK, ITF, SUPER STAGE, SOLID TIDES, Trick or Treat, JUMP, MVP, TSNA, C.C. Mercedes, Pier-2, Cathay Pacific Taipei-Tokyo, trail transliterations, NT$, VOL.2, level chips, option letters); photo credits verbatim (« Photo: Wilfredor — CC0 (Wikimedia Commons) », « Photo: CorraleH — CC0 (Wikimedia Commons) », « Photo: Bain News Service — Public domain (Wikimedia Commons) », « Photo: Benjamin Balazs — CC0 (Wikimedia Commons) »); W43-precedent « — Page N — » separators and « p. N » tags. **Zero English explanation residue** (marker scan for « Fill in », « Answer keys », « Word of the week », « Over to you », « Did you get it », « in English », « Traditional Chinese text », « English explanations », « Notes｜ », « Staff report », etc.: none present; the single « Vrai ou faux » hit is the French section head itself).
- **Visual QA**: all 8 rendered cards eyeballed page by page — no overflow, no overlap, no footer collision, image/credit placement confirmed. Non-blocking notes: P4 title « 棒球詞卡 · Les mots du baseball » wraps to two lines (clean wrap inside the flow, no overlap, core geometry otherwise unchanged); P7-A2 flow-end 1594 vs 1560 bottom is trailing gap only (ink ends 1551.35).

## Fix record (all folded into `transform_fr.py`, never left as direct build-copy edits)

- Main phase: repoint OUT/BASE core → edition dir; bslib footer + page line + gloss prefix; badge line replaced in place (y=378, 21pt, OLIVE → BRICK); all 150 registry notes, all gloss/glossline prose, all band subs, section heads, box texts, bylines, P7 columns/clinic/frame/letters/phrases/teaser, P8 heads/writing lines/answer head translated to French with exact-count asserted literal replacements.
- FIX2: band titles missed in the main phase (Life → Vie quotidienne, Youth → Jeunesse, Deep read → Lecture approfondie, Language focus → Focus langue); P6 head « 深讀測驗 · Quiz de lecture approfondie » (535.8px > 434) → « Quiz de lecture » (359.2px); P7 col-3 compression (clinic/frame/letters shortenings) and A2/B2 column tightening.
- FIX3: P7 letters disclosure trimmed to 7 wrapped lines (col3_end 1772.86 → 1743.86), but the last line's ink still crossed the box border by 5.9px — the height formula itself runs short, not just the text length.
- FIX4: strict-CJK ， fix (6 comma-after-CJK-term restructurings); P2 你呢 French 3→2 lines; P5/P6 box-title shortenings (above); P7 letters disclosure cut 7→6 wrapped lines (col3_end 1743.86 → 1714.86), yet the last line still crossed by 6.5px, confirming the formula shortfall.
- FIX5: P7 letters-box height constant +26 → +56 (formula shortfall fixed at the source; final col3_end 1744.86, teaser 2542.86 — core parity, ink clear of the border).

## Gate 10 — transform-solo reproducibility (SELF-RUN, PASSES)

Fresh copy of the core build into `hidden_files/w45-zh-tw-fr-gate10/` + `transform_fr.py` ALONE, then the single one-process driver (`run.py`): output **8/8 byte-identical** to the delivered SVGs (verified with `sha256sum -c` against the pre-run snapshot; exit 0 on all 8), **0 FLOW OVERFLOW / HEAD TOO WIDE warnings**, registry identical (150; A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38). Delivered SVG sha256: p1-front `446aa933f1f94d8efda2cfcd6b47a07b84422880bb1ac8769b1360214b356a52`, p2-life `9c69461636c3fb476a220fd5fd9303b8a95a3f7679975dda47e45063c455d339`, p3-culture `4696d0415d094d4373d8e7fa031f5f4e1b3ea5a172a7920e2288f2dc5afd6474`, p4-sport `fe832a7eff464e4c398112ebb450ede4b88c389204530fec4391f5160bf4d120`, p5-youth `335e7c4560c7ed1e0883be4474601d641e4f86a3a6c1b82fa39e0ec2809e43d8`, p6-deep `e12de61199e8a146f6d9dc6399e55e56f008f4eb6120ca109618ffba5ee5177e`, p7-lang `3318776e2513037ca4de8a9119b19df0d0a6c9805e0a73791aaaa14fe4b9b555`, p8-test `3e7908dfab9dfa93611540f0c04e9815ccf61644e5d5b22de897983a55c03d35`.

## Reproduce

```bash
cd hidden_files/weekly-report-w45-zh-tw-fr-build
../../tools/venv/bin/python transform_fr.py   # idempotent; applies main + FIX2-FIX5
../../tools/venv/bin/python run.py            # one-process driver -> svg/ into files/weekly-report-w45-zh-tw-fr/
../../tools/venv/bin/python render.py         # cards + print/web PDFs
../../tools/venv/bin/python checks.py         # builder self-checks (collisions, charts, gloss, phrases, images, corner, CJK union, Latin inventory)
```

Tools evidence files: `tools/scratch/baseline-w45-zhtw` (baseline), `tools/scratch/w45-zh-tw-fr-diff2.json` (freeze diff, strict-CJK 0), `tools/scratch/w45-zh-tw-fr-occlusion3.json` + `w45-zh-tw-fr-occlusion-new3.json` (occlusion 0 / NEW 0), build-dir `render5.log` (final render, 0 warnings), `gate10-run.log` + `gate10-expected.txt` (Gate 10).

## Image licenses (same files as the core, credits verbatim on the pages)

| Page | File | Credit (Commons API Artist field) | License |
|------|------|-------------------------------------|---------|
| P1 | harbour.jpg | Wilfredor | CC0 |
| P2 | rain.jpg | CorraleH | CC0 |
| P4 | baseball.jpg | Bain News Service | Public domain |
| P5 | pumpkin.jpg | Benjamin Balazs | CC0 |

## Delivery note

This builder does not claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, creates no cron, and does not touch `weekly-git` pushes or `insert.py`.
