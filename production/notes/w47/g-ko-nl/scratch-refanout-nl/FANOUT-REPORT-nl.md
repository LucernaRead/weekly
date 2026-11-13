# FANOUT-REPORT-nl — W47 Dutch-target family re-fanout (core fix2)

- **Date:** 2026-11-11. **Scope:** 10 reader editions (de, en, es, fr, it, ja, ko,
  pt, ru, zh-tw) under `production/2026-w47/fanout-nl/2026-w47-nl-<reader>/`.
  (The task brief lists `{de,en,es,fr,it,ja,ko,nl,pt,ru}` but no `nl-nl`
  edition exists; the real 10th edition is zh-tw. Core is `core-nl/`,
  slug `2026-w47-nl-zh-cn`, zh-cn reader.)
- **Core HEAD built against:** fix2 **`5de7492f`** ("W47 core-nl fix2: D3 match
  overflow + D4 answer-marker localization + D5 Eredivisie standings",
  2026-11-11 11:58 UTC). Verified again after the first coordinator follow-up.
- **Build only — no commit, no push.** Work only in `production/2026-w47/` and
  `hidden_files/w47/`.
- **Method:** surgical, not full re-gen. `gen_fanout.py` copies core sources and
  translates only CJK literals — there is no separate fan-out facts list
  (verified by grep: no "Speelronde 12"/"Eredivisie na 12" in the mechanism
  dir), so the facts live in `content34.py` itself and a surgical insert into
  each edition's `content34.py` is mechanism-equivalent to a re-gen for D5
  (same logic for D3). A full re-gen would have lost the many per-edition
  manual fixes recorded in each `<lang>.md`; instead the core deltas + proved
  edition fixes were applied as string edits, then each edition was rebuilt
  (`run.py` → `render.py` → `export_fanout.py` → `tools/webpdf.py` →
  `gates.py`). All builds with `tools/venv/bin/python` (Pillow 13.0.0); one
  edition at a time, in order en → de → fr → es → it → pt → ru → ja → ko →
  zh-tw. it was rebuilt a second time (build 5) for the late proof1 handoff
  (see §5).
- **Environment quirk (2026-11-11 ~12:05 EST):** `/dev/null` did not exist in
  this VM at task start, so `git` failed; it later appeared as a regular file
  (probably touched by a concurrent agent). Mitigation: truncate `/dev/null`
  (`: > /dev/null`) at the start of each build step, since a regular file
  accumulates writes instead of discarding them. Probe-first rule was honored
  (`git hash-object -w` + real goals-side file write before starting).

## Deliverables (SHA-256 + bytes, re-verified from disk 2026-11-11)

| edition | build | print PDF (bytes) | web PDF (bytes) | text.md (bytes) |
|---|---|---|---|---|
| de | 6 | `f87d3f4d6518a10a42e9ebbc05d55eda09cb1b2ce2786aa695c4fb183341ab59` (12,669,890) | `44d1550835408e1df9bd414608ad7f507557f49f438ca61c5141ab7a7e0f3ab6` (1,617,821) | `7d6eee03b87a09d9319a999a1842e6252c7bb1959d6f57f6d40b431e967fd873` (46,214) |
| en | 9 | `3352492cf30e965d8249c55638f0ed73d4e07c0a4a97d61f4c9aa55c696a693c` (12,665,902) | `2589cac4102d70f9041138f3c67a0176eff726a770cc89034ebd9c8905e39a06` (1,610,568) | `05513522b585be936b4bd28654e911c278595afa9ec8a8713e1504ab364623dd` (45,106) |
| es | 3 | `0388d59c7e7085bbd4a733f235081f26dac901489ebe1f10ee121f391306b771` (12,669,541) | `5b4f81621c77233cf9d89fa44eb6a1a249fb943f39d64ca96749e70f39cd7a21` (1,616,172) | `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` (47,649) |
| fr | 5 | `50d9182b11a9b587f6cb4dd726cb1379387d7c5c7b52a2b36903a6c627aca544` (12,656,012) | `9e90d0ab053b8fef4c8c1534294060bb0110aa5e5a395c1d11c572a9881084e4` (1,612,638) | `21888192450ff4f8350ed5c0fd091e4de44e4425fd593103b35358cdef43e7c9` (47,739) |
| it | **5** | `2520e5ad82096ef3c860e46b15934849faf2962ed8d61f885dc17151d2089826` (12,667,197) | `609dc9a534f109e61d86a4a58d42b9dd4a2ef1673b2a78fb7abb5b668cf97f0c` (1,610,232) | `62142f938c6a814297b5b4602a5a95ea0d7df38b1c4f86df5402a9a8dad629e8` (47,049) |
| ja | 2 | `40e58eb248ea12da5d52e592f582e44bbf35246a17df05c8d27240d492446e49` (26,049,308) | `3c60dddbd2f917d99c82a447d9964a3f72a42ca8c9243465949eba9e65f4ae49` (2,155,388) | `e890ba135c8c5ad2873d41bbf9133a23ece29bdf08f7a1f6686765e9beb0dcf6` (47,796) |
| ko | 2 | `aaeeba2cb7f59bb0e8d50d6614b09f3831c4ade3be3cff52f03d8f71e25113bd` (17,281,343) | `ed38e32febf217635830d3d6a7d7fa4b0c52f5db37493f78ce4bb8a0204065d5` (1,919,763) | `1d103d29fcbde556646bf5106d812cb358a9f0b3cc14b6b0b9f31030c31fe408` (47,580) |
| pt | 3 | `e85aa1a01bea9c7894546e9e33f45f2c519f202f3404103dff59265f5daac834` (12,672,018) | `a0c8c87bd941fc87d945eac257053a482de7b1f1fc8a088070f3d66351146d85` (1,618,472) | `865e659fc2d4a9b1639c3513cd8e3326536feac8ae5fed14dca411d0cc137efc` (47,204) |
| ru | 5 | `f945029d3a736dd3d139c555a4693283dc3aa9feba732edc91805b556ff889c2` (12,718,382) | `e5e3d5d3fd36b767858c96cafce0b4bf317f7ed2fd62a605aaa7eed327352724` (1,661,354) | `558786fc6247329c319fd1cf965e458ec32cea1daf3d7ae534f02c9804829273` (57,848) |
| zh-tw | 2 | `3a81e9cf00ff56378f692af8e951a4d306d0c68eae113332c8bede67d477eb9b` (25,993,150) | `aedb0d6e80fdb95f3279dea8523b09e2130309f82e26fcf940559405cd1cced7` (2,369,193) | `54d20ccd80af265c3ec62d2db0a08cbd1e7ecc559ea1bdc24557b449d293539e` (44,315) |

it build 5: print PDF and text.md are byte-identical to build 4 (same SHAs);
web PDF differs by 7 bytes (1,610,232 vs 1,610,225 — webpdf font-subset
nondeterminism; text layer identical, 46,500 B both, gates green).

## Gate table (per edition — all gates ALL PASS in every edition)

Common to all 10: `run.py` TOTAL 150, zero OVERFLOW / TOO WIDE; occlusion 0;
p8 extract 150/150; p8 compare CLEAN, 0 key diffs; freeze 8/8 (venv);
print/web text posdiff 0, msdiff 0 on all 8 pages; P8 answer-zone font
min = median 10.12pt; chips core = edition {A2:8, B1:24, B2:3}; §1.1 clean;
`check_one.py` ALL PASS; creambox 0 true overflow (all flags pixel-probed
0 dark pixels in the 7px strip below the box bottom — descent-allowance
artifacts on descender-free last lines); horizontal box-title true-ink check
56 titles, 0 FAIL; 8/8 pages + key crops viewed clean.

| edition | print/web tokens (P1–P8) | pdftotext print=web | P8 spans | creambox flags → true | titles_h tightest | visual |
|---|---|---|---|---|---|---|
| de (b6) | 832/813/719/720/795/729/890/2255 | 46,734 B | 187 | 2 → 0 | P6 DAFÜR / DAGEGEN +17 | 8/8 clean |
| en (b9) | 790/828/738/735/807/748/915/2318 | 45,429 B | 187 | 2 → 0 | P7 WORD OF THE WEEK +13 | 8/8 clean |
| es (b3) | 812/820/727/731/794/743/913/2403 | 46,814 B | 184 | 3 → 0 | P6 chart head +0 (adjudicated, see §6) | 8/8 clean |
| fr (b5) | 819/824/722/725/799/739/944/2436 | 46,862 B | 187 | 3 → 0 | P6 DONNÉES FICTIVES +13 | 8/8 clean |
| it (b5) | 809/817/722/726/793/735/915/2344 | 46,500 B | 185 | 2 → 0 | P7 PAROLA +148 | 8/8 clean |
| ja (b2) | 745/706/665/661/683/647/734/1600 | 47,919 B | 561 | 6 → 0 | P2 こう覚えよう +13 | 8/8 clean |
| ko (b2) | 733/713/668/667/695/657/754/1639 | 47,613 B | 613 | 3 → 0 | (no title < +20) | 8/8 clean |
| pt (b3) | 815/817/721/728/792/741/913/2372 | 46,693 B | 188 | 4 → 0 | P7 PALAVRA DA SEMANA +1 | 8/8 clean |
| ru (b5) | 797/802/722/727/783/730/885/2149 | 54,978 B | 598 | 3 → 0 | P6 УЧЕБНЫЕ ДАННЫЕ +10 | 8/8 clean |
| zh-tw (b2) | 749/705/664/658/685/648/733/1676 | 44,323 B | 565 | 3 → 0 | P1 numbers title +11 | 8/8 clean* |

\* zh-tw visual clean except the two known orphan-。 items (see §7): P3 lone
`。` (fix3 D6, inherited) and P6 caption gloss `。` at line start (new finding).

text.md diff vs backup (pre-rebuild) classification — every changed line is
D3 (1 line-pair) + D5 (1 line) + documented per-edition extras, nothing else:
en 5, de 9, fr 19, es 9, it 11, pt 293 (144 type-label line-pairs), ru 3, ja 3,
ko 5, zh-tw 289 (142 D4-spacing pairs + term lines; see §1).

## §1 D4 — answer-marker localization (exporter, verified in place)

- `scratch-fanout-nl/export_fanout.py` contains the `ANSWER_MARK` table
  (lines 60–71), verified before building: de `— Antwort:`/Antwort,
  en `— Correct:`/Correct, es `— Respuesta:`/Respuesta, fr `— Réponse:`/
  Réponse, it `— Risposta:`/Risposta, ja `— 答え：`/答え, ko `— 정답：`/정답,
  pt `— Resposta:`/Resposta, ru `— Ответ：`/Ответ; match items use the bare
  word; core-nl and nl-zh-tw keep Chinese `— 答案：`.
- Per edition, text.md: **142 ex-markers + 8 match words**, exactly as
  specified; `答案` residual 0 in all 9 non-Chinese editions.
- zh-tw keeps Chinese markers: 142 `— 答案：` + 8 `(答案 x)` = 150. Total
  `答案` in zh-tw text.md is 168 — the extra 18 are legitimate
  instruction/header text (選出正確答案 / 答案見第8版 / 按題號找答案 /
  無唯一答案), identical in the pre-fix2 build. `check_one.py` originally
  asserted total `答案` == 150 and failed on this; the check was corrected
  (2026-11-11) to count markers, and re-runs ALL PASS. The fixed exporter
  writes `— 答案： B` (marker + space + answer, uniform with the other
  editions' `— Correct: B`); the pre-fix2 export had no space after `：`.
  That spacing accounts for zh-tw's 289-line diff (142 spacing pairs + term
  lines) — all D4/D3/D5, no other content change.
- Web-PDF italic loss (de D5 / en D2 / fr D3 / es D7 / it D2 / ja D1 / ko D5 /
  pt D5 / zh-tw D2 — mechanism, `tools/webpdf.py`): the current
  `tools/webpdf.py` already contains the italic fix (commit 40963281,
  `fc_match:slant=italic` → Newsreader-Italic.ttf). Rebuilding the web PDFs
  fixed it for free; verified italic span count print == web == 1 in every
  edition. `webpdf.py` was NOT edited.

## §2 Type-label localization (nl-pt proof1 D4)

- Root cause: `scratch-fanout-nl/trans_table.py` TYPES row for pt was copied
  from en (all English). Fixed the row AND all English type tokens in nl-pt
  content files (145 tokens: 144 `typ` args + 1 `e_["type"] == "writing"`
  comparison in `content8.py:142`, which must match the new 寫作 value or the
  P8 answers loop breaks).
- Final pt TYPES row (aligned to it-pt text.md + it-family
  `scratch-fanout-it/translations.py`): 完成句子 → `Completa a frase`,
  单选 → `Escolha múltipla`, 完形单选 → `Cloze`, 词汇配对 →
  `Relaciona as palavras`, 判断对错 → `Verdadeiro ou falso` (no `?`; the `?`
  belongs to the separate instr form only), 造句 → `Forma frases`,
  翻译 → `Traduzir`, 写作 → `Escrita` (proof's `Escreva` rejected — that is
  the instr form, not the type word). Replacement order matters: `cloze
  choice` before `choice` (substring).
- Verified: 0 English type tokens left in nl-pt content files; type brackets
  in text.md all Portuguese (Completa a frase 65, Escolha múltipla 44,
  Cloze 13, Relaciona as palavras 2, Verdadeiro ou falso 7, Forma frases 8,
  Traduzir 4, Escrita 1); English instr phrases 0 in the print PDF.
- **`Complete` ×59 adjudication:** the pt check first FAILED on this because
  `Complete` ×59 remains in text.md and the print PDF. Investigation proved
  it is NOT leftover English: it is the Portuguese você-imperative of
  *completar*, deliberately mapped in `trans_table.py` INSTRS pt row
  (`'instr="填空"': 'instr="Complete"'`, parallel to es `Completar`, it
  `Completa`, fr `Compléter`, en `Fill in`). It renders as the per-item
  instruction label, while the TYPE brackets are all Portuguese. Count is
  exact: 59 = 65 complete-type items − 6 P1 NU JIJ items with no instr;
  structural parallel of es `[Completar]` ×59 and it-pt `[Completa]` ×56.
  Portuguese instrs all present (Complete 59, Forme a frase 8, Verdadeiro ou
  falso 7, Traduzir 4, Escreva 1, Ligue palavra 1). `check_one.py` was
  corrected to scope pt-types checks to type brackets only (text.md) and
  English instr phrases only (print PDF); re-run ALL PASS. The old pt
  proof's "print `Complete` ×59" counted instr renderings, not type labels.

## §3 Terminology pinned (nl-zh-tw proof1 D3)

- Sinterklaasjournaal unified to `聖誕老人新聞` (3 `辛特克拉斯新聞` fixed);
  Expeditie Robinson unified to `《荒島遠征》` (2 `《魯濱遜遠征》` fixed;
  core uses `《荒岛远征》`, Traditional renders `《荒島遠征》`).
- Verified post-build: old terms 0 residual in zh-tw text.md/SVG (and 0 in
  all 10 editions by grep); zh-tw text.md counts 聖誕老人新聞 8
  (5 pre-existing + 3 converted), 《荒島遠征》 3.

## §4 nl-pt P6 box title (proof1 D1)

- `VOOR OF TEGEN?　A FAVOR OU CONTRA?` overflowed +21.5px → shortened to
  `A FAVOR / CONTRA` (task suggestion, delete words only, no additions).
- Advance-based clearance +11.5px; PIL true-ink re-measure (build 3):
  ink right 1850 vs box right 1862, clearance **+12px** (≥+5 required).

## §5 nl-ko P2 EN JIJ box (proof1 D7)

- Korean gloss reflowed by dropping `함께`; now 3 lines, last line ends
  `...편집부에 보내세요.` with the period attached — no orphan period.
  Verified with ko svglib `wrap()` and visually on the P2 card crop.

## §6 Horizontal box-title true-ink check (NEW — added per nl-it proof1 D1 handoff)

- Tool gap found by the it proof: occlusion BOXTITLE only covers stroked /
  `#2c2822` boxes (cream `#f0eee5` not included) and creambox measures
  horizontal only via advance width, not true ink — so a +65.9px box-title
  overflow passed all gates. New tool `check_titles_h.py`: every BOLD (or
  ≥23pt) text inside a cream rect, PIL true-ink rightmost dark pixel on the
  rendered card vs the rect's own right edge.
- Results: **10 editions × 56 titles, 0 FAIL, ALL PASS.** Tightest real
  clearances: es P6 `DE GRAFIEK　DATOS DE PRÁCTICA` +0, pt P7
  `HET WOORD　PALAVRA DA SEMANA` +1, ru P6 +10, en P7 / fr P6 / ja P2 +13.
- es P6 +0 adjudication: solid ink (lum<90) rightmost 1861, i.e. 1px INSIDE
  the box; only a 1px antialiased fringe (lum 90–200) touches the 1862 edge
  line — confirmed by threshold sweep (90 → 1861, 150/200 → 1862) and a 3×
  zoom crop (`it-d1-d3-before-after/es-p6-charthead-zoom.png`): the final `A`
  does not land on newsprint. Same as the build-3 adjudication; no fix.
  (First version of the script misattributed sibling ink on shared baselines
  — P2 4-column table headers, P1 numbers title vs the right-column body —
  and reported 3–4 false FAILs per edition; fixed to probe each text's own
  advance span (anchor-aware, +3px outer margin), re-run 0 FAIL.)
- it P7 D1 re-measure (the handoff's explicit ask): `HET WOORD　PAROLA`
  true-ink right **1714**, box right 1862, clearance **+148px**.

## Per-edition fixes beyond the core deltas (all with proof sources)

- **en (build 9):** proof2 (en1) D1 — P1 HET WOORD English note shortened to
  one line `"Group win": first in the group.` (was 2 lines, cut by the y=1853
  full-width rule; pixel-scan evidence). Note: the second proof2 run (en2)
  reported zero defects and did not mention this line — conflict recorded;
  en1's evidence is strong and the fix is the proof's own suggestion.
- **de (build 6):** proof1 D1 P1 `IN DEZE EDITIE　IN DIESER AUSGABE` +33.5 →
  `...　AUSGABE` (+89.5); D2 P6 `VOOR OF TEGEN?　DAFÜR ODER DAGEGEN?` +47.5 →
  `DAFÜR / DAGEGEN` (+13.5); O2 P2 `ZO ONTHOUD JE HET　MERK ES DIR` +0.5 →
  `MERK DIR` (+32.5).
- **fr (build 5):** proof1 D1 P7 `HET WOORD　LE MOT DE LA SEMAINE` +21.6 →
  `MOT DE LA SEMAINE` (+10.5, chosen over the proof's `LE MOT` to preserve
  meaning); D2 P6 `VOOR OF TEGEN?　POUR OU CONTRE?` +0.8 → `POUR OU CONTRE`
  (+14.5); D4 8× U+2019 → U+0027 (content7.py 4, content8.py 4); post-build
  sweep U+2018/U+2019/U+201C/U+201D = 0 in content, svg, text.md, both PDF
  text layers.
- **es (build 3):** proof1 D1 P6 `VOOR OF TEGEN?　¿A FAVOR O EN CONTRA?` +47.8
  → `¿SÍ O NO?` (+103.5); D2 P7 `HET WOORD　PALABRA DE LA SEMANA` +34 →
  `PALABRA SEMANAL` (+21.5); D6 Q140 key missing `corto` — fixed (see §7);
  O2 EN JIJ boxes (P2 content12.py, P5 content56.py) bottom pad +20 → +22
  (proof-recommended hardening). O1 adjudication: Q78 `Zij ___ (maken)` key
  `gaat maken` unchanged — singular zij is the exercise convention, key
  defensible; stem and key untouched (verified text.md:262).
- **it (builds 4 + 5):** proof1 D1 P7 `HET WOORD　PAROLA DELLA SETTIMANA`
  +65.5 → `PAROLA` (+147.5); D3 4× U+2019 → U+0027 (content7.py:122 golden,
  content8.py:43 #126, :75 #140, :133 P8 header); build 5 added the
  mechanism-level fixes — `trans_table.py` it HET WOORD value → `PAROLA`
  and the 4 U+2019 table sources → U+0027 (table U+2019 15 → 11; remaining
  11 are fr 7 / en 1 / it dead entry 1436 `c’erano`, not in this edition,
  untouched). Before/after renders kept in
  `it-d1-d3-before-after/` (+ `BEFORE-AFTER-NOTE.md`).
- **pt (build 3):** proof1 D1 P6 (see §4); D4 type labels (see §2); O1 P2
  EN JIJ pad +20 → +22.
- **ru (build 5):** no proof dir exists (unproofed); core fixes only.
- **ja (build 2):** core fixes only. ABSTRACT `De` (proof1 D2) deliberately
  NOT fixed — see §7.
- **ko (build 2):** proof1 D7 (see §5). P4 B-section word list flows with
  `• interland • stand` at the top of col 2 — same flow mechanism as other
  editions, all words present; not a defect.
- **zh-tw (build 2):** proof1 D3 terms (see §3); D3/D5 core deltas. P3 lone
  `。` + P6 leading `。` — see §7.

## §7 Coordinator follow-ups and open items

- **Follow-up 1 (core-nl re-proof post-fix2, conclusion (b)):** 2 new core
  defects D6/D7 — P3 and P7 each have a Chinese full stop `。` orphaned
  alone on its own line (fix-round leftover, proof1 missed; fix2 D3/D4/D5
  all pass regression). Core fix3 was assigned to another agent. **This
  rebuild continued the fix2 core to completion and did NOT rebuild for
  fix3**, per instruction.
- **Core fix3 has since landed:** `f567bcea` ("W47 core-nl fix3: D6/D7 orphan
  。 (proof2 rounds)") is now the repo HEAD and core-nl's last commit. It is
  NOT included in any edition in this report. A separate incremental rebuild
  is pending (coordinator to assign).
- **Fix3 incremental-rebuild scope, measured 2026-11-11 (family-wide
  orphan-。 sweep, all 10 editions × 8 pages):** only **zh-tw** carries
  orphan-。 lines (2); the other 9 editions have **0**. So the fix3
  incremental rebuild touches zh-tw only — except for the new item below.
  - zh-tw P3 lone `。` (x=538, y=2280.22, under the C HET PERFECTUM
    instruction) — core fix3 D6 inherited; visually confirmed on the P3 crop.
  - zh-tw P7: **no** orphan `。` — fix3 D7 did not reproduce in this edition's
    wrap.
- **NEW finding — P6 chart-caption gloss `。` at line start (not in fix3's
  scope):** `。問題：你在鞋裡放什麼？（100 名年輕人）` (zh-tw, x=1462,
  y=659.44) — the line-breaker split before `。`, detaching it from
  `...非真實調查。` at the end of the previous line. Same defect class as
  fix3 D6/D7, but **still present in the current core itself** (`f567bcea`,
  Simplified `。问题：你在鞋里放什么？`, same coordinates). fix3 fixed D6/D7
  (P3/P7) but did not cover P6 — the re-proof listed only P3/P7. **Needs a
  coordinator decision:** a core fix (D8?) + incremental rebuild of core +
  zh-tw (the only two editions carrying the Chinese gloss). Visually
  confirmed on the P6 caption crop. Not fixed here — out of fix2 scope.
- **Follow-up 2 (nl-es proof1 handoff, 3 items — all done, es-only):**
  1. Q140 `corto` fixed in es (`content8.py:75-76` key →
     `Ik maak een surprise met een kort gedicht.`, note → `surprise:
     expresión fija; corto = kort`; source sentence untouched). Key source
     is the **core** — the key is copied verbatim from core-nl
     `content8.py:75`; the core's own source sentence carries 小诗, so the
     defect originates in the core. Verified post-build in text.md:415 and
     on printed P8 answer 140; p8 compare still CLEAN (translation items
     137–140 are legitimately re-aim, exempt from key compare). Recorded in
     `es-proof-handoff-note.md`.
  2. es D1/D2 titles re-measured from built SVGs: P6 `¿SÍ O NO?` +103.5,
     P7 `PALABRA SEMANAL` +21.5 — both fit, no further shortening.
  3. O1 adjudication (no change): Q78 singular zij accepted.
  **Same Q140 key-vs-source mismatch exists in 6 other editions + core,
  recorded only, NOT fixed** (coordinator scope: es only). en `... with a
  little poem.`, fr `... avec un petit poème.`, ja `小さな詩つきのプレゼント…`,
  ko `작은 시가 담긴…`, pt `... com um poema curto.`, zh-tw
  `我做一個帶小詩的偽裝禮物。` — all keys lack `kort`. de `... mit einem
  Gedicht.` / it `... con una poesia.` / ru `... со стихотворением.` have no
  qualifier, keys match, no defect. A core-level fix (add `kort` to the
  core key) would correct all 7 at once — flagged for the coordinator.
- **ja ABSTRACT `De` (proof1 D2) — NOT fixed, flagged:** across all 101 W47
  ABSTRACT.txt files only core-nl has "De Lucerna"; all fan-out abstracts use
  bare "Lucerna". SOP §9 says "含刊名" but the pt proof explicitly
  adjudicated bare "Lucerna VOL.4" as the family convention, not a defect;
  the it proof also passed its ABSTRACT. One prover's strict reading vs
  family convention + another prover's ruling — left unchanged. Lint has no
  abstract-masthead gate, so it cannot block insert.
- **en proof conflict (recorded):** proof2 run en1 found P1-note D1
  (pixel-scan evidence); run en2 reported zero defects and did not mention
  it. Fixed per en1's evidence.
- **it / es-it curly-quote direction conflict (recorded):** nl-it D3 goes
  straight→curly is wrong here — U+2019 renders with a full-width gap in
  Noto Sans CJK SC (visually verified), so nl-it changed 4× U+2019 →
  U+0027; es-it fix1 went the opposite direction. Root cause is Latin text
  in the CJK SC font. nl-it follows rendering evidence only, es-it
  untouched; conflict recorded in `it-d1-d3-before-after/BEFORE-AFTER-NOTE.md`
  for the coordinator to escalate.
- **Mechanism files changed (goals-side, not in the repo):**
  `scratch-fanout-nl/trans_table.py` — pt TYPES row fixed; it HET WOORD
  value → `PAROLA`; 4 it U+2019 sources → U+0027. These take effect on the
  next `gen_fanout.py` run; the built editions already carry the fixes.
  `export_fanout.py` was NOT edited (ANSWER_MARK table already correct).
  `tools/webpdf.py` was NOT edited (italic fix already in, commit 40963281).

## Backup

- 10 old edition dirs (303 MB, 442 files) copied to
  `scratch-refanout-nl/backup/` before any edit; SHA-256 manifest
  `SHA256-orig.txt` vs `SHA256-backup.txt` identical (`BACKUP_SHA_MATCH`).
- **The backup must NOT be deleted before the new bundle is in the repo.**
- Pre-rebuild deliverable SHAs were recorded from the backup manifest and
  match the earlier FANOUT-REPORT-nl.md / FIX-LOG values.

## Files and logs

- This report: `scratch-refanout-nl/FANOUT-REPORT-nl.md`
- Mechanism: `scratch-fanout-nl/` — `export_fanout.py` (D4 ANSWER_MARK),
  `gen_fanout.py`, `trans_table.py` (pt TYPES + it HET WOORD + it U+2019
  sources fixed), `gates.py`, per-edition records `<lang>.md` (all updated),
  previous `FANOUT-REPORT-nl.md`.
- Rebuild scratch: `scratch-refanout-nl/` — `backup/` (+SHA256 manifests),
  `measure_titles.py/.log`, `apply_fixes.py/.log`, `apply_fixes2.log`,
  `build_one.sh`, `check_one.py` (pt-types checks corrected; zh-tw D4 check
  corrected 2026-11-11), `check_titles_h.py` (new horizontal true-ink
  check), `review_images.py`, `es-proof-handoff-note.md`,
  `<r>-{build,render,export,webpdf,gates,check,creambox,titles_h}.log`,
  `<r>-review/` (all 10 editions), `it-d1-d3-before-after/` (D1/D3
  before-after renders + note + es P6 chart-head zoom),
  `zh-tw-review/` (incl. `crop-p3-lone-period.png`, `crop-p6-caption.png`).
- Proof reports: `scratch-proof-nl-{de,en1,en2,es,fr,it,ja,ko,pt,zh-tw}1/
  PROOF-NOTE.md` (no ru proof dir). Creambox tool:
  `scratch-fix-core-nl1/check_creambox.py`. Core FIX-LOG:
  `production/2026-w47/core-nl/FIX-LOG.md`.
- Per-edition KITs updated (Files delivered + Fixes + Re-fanout §; it KIT also
  has the build-5 follow-up §; zh-tw KIT has the known-issues §).
