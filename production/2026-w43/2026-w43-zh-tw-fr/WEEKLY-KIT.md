# Lucerna 繁體中文週報 VOL.1 — 法語講解版 (zh-TW × FR) — WEEKLY KIT

- **Pairing**: Traditional Chinese target text (frozen W43 core, week of Mon 2026-10-19 – Sun 2026-10-25) + explanations written natively in French. The edition for French-speaking readers.
- **Masthead**: « Lucerna » (no article — Chinese takes no article, per SOP), kept exactly as shipped in the core.
- **Deliverables** (this dir): `svg/` ×8, `cards/` ×8 (1950×2700), `Lucerna-VOL1-FR.pdf` (print), `Lucerna-VOL1-FR-web.pdf` (web), this KIT.
- **PDF pins**: print 28,988,605 B, sha256 `a10bd0e87c9ac5ad3e83e020fd1579ffaa3b149bf07f1852d9b8b80768be05f6` (D5 rebuild 2026-11-14); web 3,044,240 B (< 10 MB), sha256 `e4cc28f66e543c1882b191648d1abeabbc4275cfa07f7f527eb68166f6f7939d` (D5 rebuild 2026-11-14).
- **Totals**: 150 exercises — A2 56 · B1 65 · B2 29 (identical to core); pages 10/18/18/18/18/18/12/38; types 單選 65 · 完成句子 52 · 配對 20 · 完形單選 12 · 寫作 1. Writing model 134 characters (unchanged Chinese).
- **Proofread**: builder pass complete (below); independent proofread **PENDING**.

## Production method

Fan-out from the Traditional Chinese core only, produced natively for French readers — never converted from, or copied out of, the Simplified edition. Build dir: `hidden_files/weekly-report-zh-tw-fr-build/` (copy of the core build `weekly-report-zhtw-build/`). Only the explanation layer was rewritten (English → French); the Traditional Chinese target text is frozen.

**Baseline proof**: the unmodified copy of the core build reproduced all 8 shipped core SVGs **byte-identically** (sha256, 8/8) before any edit.

## Freeze verification (vs the CORE's shipped SVGs)

- Image payloads byte-identical on all 8 pages.
- Text-element multiset diff per page: every changed element is explanation layer, pairing furniture, or a wrap-segmentation artefact of a mixed-language explanation paragraph (P5 « 1. » segment; P7 « （登高、討糖、星光大道）. » / « （補假）. » segments; P8 « 20. » segment).
- CJK character multiset per page: **zero characters added** on any page; the only removed CJK characters are exactly the two designed furniture strings (P1 pairing badge and the footer line), whose Chinese pairing text is replaced by the French pairing furniture — the same treatment as the shipped DE fan-out.
- Registry diff (`reg-core.json` vs `reg-fr.json`, both in the build dir): page/level/type identical for all 150; all 150 notes now French; **keys identical except #150** (see registry below).

## Key-diff registry (complete)

- **#150** （寫作， P8): apparatus key « (開放題，範文如下) » → « (question ouverte — texte modèle ci-dessous) »; note → « Question ouverte — le texte modèle est imprimé dans la section F ci-dessus (134 caractères) ». (On the printed page only the note shows, as « 150. ✓ … ».)
- This core contains no translation exercises; #137/#138 are 完成句子 items whose keys （品味 / 留友） are Chinese target-text answers and stay byte-identical — only their notes were translated. All other 149 keys byte-identical to the core.

## Pairing furniture

- P1 badge (brick #a4553a, bold, 21 pt): « TEXTES EN CHINOIS TRADITIONNEL · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES » (measured 1215 px ≤ 1820).
- Footers, all 8 pages: « Lucerna · HEBDOMADAIRE CHINOIS VOL.1 · TEXTE EN CHINOIS TRADITIONNEL · EXPLICATIONS EN FRANÇAIS » / « Page N sur 8 ».
- Gloss boxes prefixed « Note — »; instructions « Complétez » (×52), « Associez » (×5), « Écrivez » (×1). Answer keys headed « 答案 · Réponses — dans l'ordre des pages, avec une courte note en français pour chaque exercice »; half-width parentheses, space before each note parenthesis (notes use the core's dash format « n. key — note »).

## Layout adjudications (French wording only; Chinese text and core geometry formulas never touched)

1. Section head « 讀懂了嗎？ · Vous avez compris ? » measured 454 px > 434 column at 28 pt → shortened to « 讀懂了嗎？ · Tout compris ? » (381 px), on P2/P3/P4/P5/P6.
2. P8 keys: first French draft wrapped to 176 printed lines vs the core's 154 and overflowed the last column. 23 notes that wrapped 1→2 lines were tightened back to one printed line each (registry texts in `reg-fr.json`); final keys flow ends col 3 at y=2500 ≤ 2540 with the core typography (13.3 pt, lh 1.16) unchanged.
3. P7 A2/B1/B2 columns: French prose ran +3–4 lines per column (A2 ink reached ~1701, near the phrases rule at 1708). Ten French paragraphs were tightened to their core line counts; final column ends: A2 y=1561 (= core), B1/B2 y=1493 (core 1526). Col-3 boxes at exact core parity (ends 1678.64; teaser ends 2508.64).
4. P2 « 你呢？ » box (fixed 230 px): the French gloss wrapped 3 lines vs the core's 2 and its last line crossed the box's bottom border (audit STRADDLE) → sentence shortened to 2 lines (« Pleuvra-t-il chez vous ? Où partiriez-vous pour un week-end de trois jours ? »).
5. P6 pass-breakdown box (fixed 504 px): the third French paragraph wrapped 3 lines vs 2 and its last line crossed the bottom border (audit STRADDLE) → shortened to 2 lines (« Contenus selon le détail officiel des billets ; économies calculées par nos soins. »). Wine & Dine figures kept exactly: 品味證 HK$258 (contents 400, saves 142), 尊尚 HK$558 (contents 900, saves 342).

## Builder proofread record

- Full read of all 8 rendered cards: French spelling/accents/agreement checked; every gloss verified against the Chinese article it explains; every answer re-checked against the registry (keys = core, #150 excepted).
- Weekday/date claims re-verified against the real 2026 calendar: Oct 17 Sat (Taiwan Series G1, Dragons 3:0, 40,000), Oct 18 Sun （重陽）, Oct 19 Mon (HK 重陽節翌日 holiday), Oct 20 Tue (G3), Oct 21 Wed (G4), Oct 22 Thu, Oct 23 Fri + Oct 24 Sat (Golden Bell 61 programme/drama nights), Oct 25 Sun (G7 if needed; parade 19:00), Oct 29 Thu (Wine & Dine opens). All consistent with the frozen text.
- P7 phrases of the week: all 8 verified programmatically as verbatim contiguous excerpts of this issue's own articles, each on its tagged page (p. 1, 2, 3, 3, 4, 5, 6, 6).
- Chart bars unchanged from the core (SCALE 1.8 px/HK$, drawn from zero); pass arithmetic re-verified (40+200+160=400, 400−258=142; 40+400+260+200=900, 900−558=342; 498×2=996; 798−498=300; 2,380−1,580=800).
- Image credits as printed on the pages (all public domain / CC0, same images as the core): NASA Johnson Space Center (PD), CorraleH (CC0), Masaki Ikeda 池田正樹 (PD), Fumikas Sagisavas (CC0), unknown author (PD), Kurt Kaiser (CC0), Benjamin Balazs (CC0), Wilfredor (CC0), Jon Sullivan (PD).
- Banned intermediary-layer term: 0 occurrences in the paper SVGs, this KIT, and the build code (the core build has no intermediary helper method; nothing to rename). [Proofreader fix, 2026-10-21: this line originally printed the banned English token itself while claiming zero occurrences — the token has been removed; the paper artifacts were not touched.]

## Geometric occlusion audit (builder run)

Script `audit_zh_tw_fr.py` (build dir): paint-order scan, real-font glyph metrics (svglib), ink band −0.88em…+0.30em, line boxes **expanded by half the stroke width**. Synthetic positive controls validated first: COVER, LINEX, FOOTER, STRADDLE, EDGE all fired (SELFTEST PASS). Final run on the shipped SVGs: **1 raw flag** — P1 masthead « Lucerna » (baseline 218, 168 pt) vs the rule at y=268. Pixel-adjudicated on the rendered card (and identically on the core's card): wordmark ink ends at row 221, the rule occupies rows 267–268, 46 empty rows between — the +0.30em band model overestimates a descender-less blackletter wordmark. **Non-defect; geometry is the core's own.** Effective flags: **0**. (The two STRADDLE flags found on the first pass were fixed — see adjudications 4–5 — and the re-run is clean.)

## Reproduce

```bash
cd hidden_files/weekly-report-zh-tw-fr-build
/tmp/wp-venv/bin/python run.py        # writes svg/ into files/weekly-report-zh-tw-fr/
/tmp/wp-venv/bin/python render.py     # cards + print/web PDFs
/tmp/wp-venv/bin/python audit_zh_tw_fr.py --selftest ../../files/weekly-report-zh-tw-fr/svg
/tmp/wp-venv/bin/python dump_reg.py   # reg dump -> /tmp/zhtw-fr-reg.json
```

## Independent proofread record (2026-10-21) — **PASS, zero problems in the paper**

Fresh independent pass over the shipped artifacts (proofreader did not build this edition). One documentation defect was found in this KIT itself and fixed (see item 10); the paper (SVGs / cards / PDFs) needed no change and was not re-rendered. After the KIT fix, the full verification suite was re-run from the top: all checks green.

1. **Freeze diff vs CORE** — Text-element multiset diff per page: every difference is English apparatus → French apparatus, pairing furniture, or documented wrap segmentation (P5/P7/P8 segments). **CJK character multiset per page: zero characters added on all 8 pages**; removals are exactly the two designed furniture strings — P1 −30 chars (badge + footer), P2–P8 −20 chars each (footer + page marker), removed set ⊆ {繁體中文週報/正文/英語講解/第版共}. No Traditional target text changed; nothing imported from the Simplified edition (CJK-added = ∅ proves it globally; Wine & Dine figures spot-verified in FR P6: 品味證 HK$258 contents 400 saves 142; 尊尚 HK$558 contents 900 saves 342 — exact, also read off the rendered card). Writing model: **134 characters, byte-identical** to the core after joining wrapped fragments.
2. **French apparatus completeness** — All 150 P8 notes in French (read in full against the core's English); instructions Complétez (×52+per-page) / Associez / Écrivez; English-remnant scan of the FR text layer: only false positives (French « week-end », « on », « six »; « Match/Matchs » = French for game). Distinctive core-English strings in FR raw SVG bytes: 0 (« Fill in », « Answer keys », « Word of the week », « Over to you », « Work it out », « Did you get it », « in English » all absent).
3. **Answer keys** — Registry diff (reg-core.json vs reg-fr.json): page/level/type identical for all 150; **key diffs exactly one: #150** (apparatus → French). Printed P8 keys parsed from both editions: 149/149 identical apart from #150. #137 品味 / #138 留友 are Chinese target answers, byte-identical. All note arithmetic re-computed (5,000/1,000×100=500; 15−12=3; 498×2=996; 798−498=300; 13+13=26; 400−258=142; 8×25=200; 558−258=300; 2,380−1,580=800; 40+200+160=400; 40+400+260+200=900) — all correct.
4. **Totals** — 150 exercises, numbering 1–150 continuous in registry and in print; A2 56 · B1 65 · B2 29; pages 10/18/18/18/18/18/12/38; types 單選 65 · 完成句子 52 · 配對 20 · 完形單選 12 · 寫作 1 — all identical to core.
5. **P7 phrases** — All 8 Chinese quotes verified programmatically: each occurs **exactly 2×** in the full-issue normalized text (once on its tagged page, once in the P7 box), verbatim and contiguous; tags (p. 1, 2, 3, 3, 4, 5, 6, 6) all correct.
6. **Weekdays/dates** — Re-verified against the real 2026 calendar: Oct 17 Sat (Taiwan Series G1, Dragons 3:0, 40,000), Oct 18 Sun （重陽）, Oct 19 Mon (HK 重陽翌日 holiday), Oct 20 Tue (G3), Oct 21 Wed (G4; sea warning Wed night), Oct 22 Thu, Oct 23 Fri + Oct 24 Sat (Golden Bell 61 programme/drama), Oct 25 Sun (G7/parade 19:00), Oct 29 Thu (Wine & Dine opens). All consistent.
7. **Furniture** — P1 badge exactly « TEXTES EN CHINOIS TRADITIONNEL · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES »; footers with pairing label + « Page N sur 8 » on all 8 pages; masthead « Lucerna », « Le Lucerna » occurrences = 0.
8. **Geometric occlusion audit (proofreader's own script, PIL real-font metrics, TC index 3)** — Synthetic positive controls for COVER / LINEX / FOOTER / EDGE / STRADDLE (incl. box-bottom spill) all fire; a clean synthetic page is silent. FR result: **0 COVER, 0 EDGE, 0 STRADDLE**; FOOTER flags = only the 2 designed footer lines per page (identical on the core); 1 LINEX = the P1 wordmark band [70,268] vs rule [266,270], **pixel-adjudicated on the FR card: wordmark ink rows 93–221 (cols 691–1258), rows 222–266 empty, rule rows 267–268 → non-defect**, geometry is the core's own (my audit run on the core yields the identical 17 flags). The two builder-fixed STRADDLE spots re-verified on the rendered cards: P2 « 你呢？ » box — French gloss exactly 2 lines, clear space to the box border; P6 pass box — final note exactly 2 lines, ends well above the border.
9. **Images / credits / PDFs** — Image payloads byte-identical to the core on all 8 pages (counts 1/1/2/1/2/2/0/0); every credit name sits on the same page(s) as in the core (NASA Johnson, CorraleH, Masaki Ikeda 池田正樹， Fumikas Sagisavas, Kurt Kaiser, Benjamin Balazs, Wilfredor, Jon Sullivan). Web PDF independently measured: **3,608,355 B (< 10 MB), sha256 `137bed3eb52fee9b3ade3e29694958e0d286d811b77e655d3b5f4866dd38b0e1`** — matches the pin. Print PDF 38,796,715 B, sha256 `fa689b20…` also matches its pin.
10. **Banned-term scan + Traditional-only** — Chinese forms: 0 in paper, KIT, build code. English form: 1 hit — **this KIT's builder record quoted the token itself inside the sentence claiming zero occurrences** (documentation layer only; the paper and code were clean). Fixed by the proofreader: the token was removed from that line and the fix annotated in place; no paper artifact touched. Re-scan after the fix: **0 in paper, KIT, and build code**. Traditional-only: the zero-CJK-added multiset proof (item 1) guarantees no Simplified-only form was introduced; the Chinese text is the core's Traditional text throughout.

**Verdict: PASS** — builder's claims verified in full (baseline/key registry/totals/audit adjudication/PDF pins). The edition is clear for repo insert.

## D5 rebuild record (2026-11-14)

D5 font rebuild of this edition (W43 three-week redo, scope B). The installer `apply_variant.py --check` FATALs on this family's face-suffixed engine (`_IDX_TC`, `"sans_TC"`, `face="TC"`), so the D5 install was hand-ported step-by-step (`scripts/d5_port_zhtw.py`, same rep1 exactly-1-match discipline; D5_BLOCK / READER_CONST verbatim; FIX2_BLOCK mechanism verbatim, anchors re-based on this family's census). W47 engine transplant was rejected with evidence (no `_fw()`). Install: `scripts/install_zhtw.sh` (`--check` dry-run first). `_D5_READER = "latin"` (mode latin/TC); routing unit test FAILURES: 0; fix2 markers 5, `_QUOTE_CLS` 4, retained. §1.1 assembly: the port engine (490 lines) was copied into production first (production never held it; 9 `.py` files per edition, SHA-verified vs MANIFEST-W43.md) plus the pilot moth into `assets/` (10 editions).

- **Pre-D5 census** (baseline): D5_latin_in_cjk=430, D5_cyrillic_in_cjk=0, curly_in_cjk=0; post-D5 census all 0 (gate 3).
- **Build pins (D5 rebuild, final):** print `28,988,605 B`, sha256 `a10bd0e87c9ac5ad3e83e020fd1579ffaa3b149bf07f1852d9b8b80768be05f6`; web `3,044,240 B (< 7 MB)`, sha256 `e4cc28f66e543c1882b191648d1abeabbc4275cfa07f7f527eb68166f6f7939d`. Web PDF is the builder original `scratch-2026-w43-zh-tw/patched/2026-w43-zh-tw-fr/2026-w43-zh-tw-fr.web.pdf` — the closer must copy it, never re-run webpdf (web PDFs are byte-nondeterministic across runs). Print PDF `scratch-2026-w43-zh-tw/patched/2026-w43-zh-tw-fr/Lucerna-VOL1-*.pdf`.
- **Step-7 fixes (point sizes only, zero wording changes; full re-render + full gates after each fix):**
  - `content12.py:175` — P2 你呢 question para: 20 -> 19.5; spill 'jours ?' BELOW +4.20px -> 0 [D5-new].
  - `content56.py:195` — P6 票券拆解 closing note para: 19.5 -> 19; spill +7.22px -> +6.56px (last line 's; economies calculees par nos soins.') [pre-existing (+4.67 in baseline), D5-worsened].
  - `content56.py:190` — P6 票券拆解 box height: 504 -> 514; spill +6.56px -> 0 (box bottom 1418 -> 1428; side piece at sy=by+522 untouched, 8px gap remains) [box-grow, DE KIT adjudication-5 precedent (same box grew 504 -> 580 for DE)].
- **P8:** extract 150/150; compare vs baseline en core CLEAN (missing=[], extra=0; [108] present in both core and edition — the zh-cn D28 core-missing-[108] discrepancy does NOT reproduce in this family). P8 lines base -> patched 212 -> 212 (unchanged by all fixes); footer slack 48.9px (>= 40 required).
- **Gates (17 + D18):** 18 GATE PASS, 0 hard FAIL. Gate 15a text.md: REFLOW — D5 reflow moves line breaks only (difflines=38, char-multiset diff 0, native verifier ADOPT all pages); the shipped `.text.md` is the joined patched export (faithful to the delivered PDF); byte-identical vs the baseline export is impossible where reflow moves wraps — REFLOW accepted per D30 (see family report §4). Gate 15a print=web PASS (multiset 0). gate 15b: shared `verify_textmd.py` rc=1 (FAIL, pre-existing verifier calibration gap — the baseline edition fails identically, only-in-MD 2009 tokens baseline vs 2002 patched, only-in-SVG 0 baseline vs 0 patched); accepted per D27 via 15a + native verifier + full read-through. Residuals are furniture the MD legitimately carries (level badges, instruction words, P8 key notes, footer/masthead words) that the verifier drops on the SVG side. Gate 15c native verifier PASS (ADOPT). D18 masthead gap 42.0px PASS. Logs: `scratch-2026-w43-zh-tw/logs/2026-w43-zh-tw-fr/gates.log` + `GATES-SUMMARY.txt`; D5 report: `production/notes/2026-w43/g-zh-tw/scratch-d5-rebuild-zh-tw/D5-REPORT-2026-w43-zh-tw-fr.md`.
- **text.md provenance:** joined patched export `scratch-2026-w43-zh-tw/logs/2026-w43-zh-tw-fr/2026-w43-zh-tw-fr.text.md.new` (D5-aware joiner `scripts/textexp_zh_tw_d5.py`; the naive exporter fragments D5 run-split lines — see family report §4). issues/ holds no `.text.md` for this edition; this file ships new with the bundle (carry-over exception).
