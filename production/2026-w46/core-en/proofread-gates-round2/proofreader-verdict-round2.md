# Proofreader verdict — Round 2 (completion) — Lucerna Weekly W46, EN family

- Issue week: Mon 2026-11-09 – Sun 2026-11-15. VOL.3.
- Scope: all 11 EN-target editions (reader-native de, es, fr, it, ja, ko, nl, pt, ru, zh-cn = core, zh-tw).
- Proofreader: independent Round 2 completion agent. This agent did NOT build or fix these editions. A previous Round 2 proofreader completed nearly all mechanical gate work and ended without a verdict; this verdict rests ONLY on evidence this agent verified or re-ran (see §6 for the verification record, including what was reused and its freshness basis).
- Gate dir: `hidden_files/w46/en-proofread-gates-round2/` (all `verify2-*` files cited below live there unless stated otherwise; edition dirs are `files/weekly-report-w46-en-*/`).
- Date of verdict: 2026-11-03 (UTC). Hard shipping gate: proofread-until-zero.

## Correction addendum (2026-11-03, after delivery of the first verdict text)

The §6.4 "koscan script not preserved" paragraph in the original text below was WRONG and is corrected in place (§6.4). The canonical koscan script DOES exist, at `hidden_files/w46/koscan.py` (copied from the W45 NL-KO build per `hidden_files/w46/gates.sh:27`). The original search missed it because the two broad greps over `hidden_files/w46/` were killed before completing, and the script lives outside the three locations searched (Round 1 gate dir, Round 2 gate dir, `en-fix/`). After the error was found (via the completed background grep), this agent re-ran the CANONICAL script itself against the correct inputs — ko SVGs (`files/weekly-report-w46-en-ko/svg`) + the EN-family ko build dir (`hidden_files/weekly-report-w46-en-ko-build`, per FIX-REPORT §method) — and the output (`verify2-koscan-canonical.log`) is BYTE-IDENTICAL to the fix worker's `en-fix/koscan-ko2.log`: CANDIDATES=28, TRUE_SPLITS=13, S3=0, orphans 0, LEAD 1. B3 therefore rests on the canonical re-run, not on the reconstruction. Two earlier attempts against wrong build dirs (`weekly-report-ko-en-build`, `weekly-report-ko-build` — other families' sources; logs `verify2-koscan-canonical-ko-enbuild.log` / `verify2-koscan-canonical-ko-build.log`, TRUE_SPLITS=2 with most candidates UNRESOLVED) are SUPERSEDED and must not be cited. The verdict itself is UNCHANGED: B3 CONFIRMED, S3=0; ROUND 2 FAIL stands as written.

## Addendum 2 — supplementary requirement: answer-key semantic audit (2026-11-03)

After the verdict text above was written, a supplementary requirement was added: verify EVERY answer-key letter 1–150 in the EN core semantically (matching blocks option-by-option, cloze/fill keys against grammar and article facts, arithmetic keys recomputed), and verify each edition's P8 printed keys match the core's — because a sibling family (ZH-CN) was found to carry frozen-core LETTER transpositions that p8.py set-equality cannot catch, and RU had the same defect class in Round 1. The audit was performed and is recorded in full in §11. Result: **150/150 semantically correct; zero wrong key letters; zero transpositions; the defect class is ABSENT from the EN family.** No new blocking defect. The verdict remains ROUND 2 FAIL on R-B6 + R-M4 only.

## Final verdict

**ROUND 2 FAIL — 3 editions blocked: zh-tw (R-B6), es (R-M4), fr (R-M4). The other 8 editions PASS and are shippable as printed.**

Per-edition verdicts (§1) and the complete residual defect list (§5) are the authoritative record. Nothing else blocks shipment.

## 1. Per-edition PASS / FAIL

| Edition | Verdict | Reason |
|---|---|---|
| core (zh-cn) | **PASS** | B4, B5 confirmed fixed; no residual defect. |
| de | **PASS** | B4, M1, M3 confirmed fixed; no residual defect. |
| es | **FAIL** | R-M4: P3 title lacks the English head (§4, §5). |
| fr | **FAIL** | R-M4: P3 title lacks the English head (§4, §5). |
| it | **PASS** | B4 confirmed fixed; no residual defect. |
| ja | **PASS** | B4 confirmed fixed; O-R2-1 is not a defect (§9). |
| ko | **PASS** | B2, B3, M2 confirmed fixed; gloss regression clean; O-R2-2 is not a defect (§9). |
| nl | **PASS** | B4, M4 (short-gloss deviation ACCEPTED, §3b) confirmed. |
| pt | **PASS** | B1 (shortened-form deviation ACCEPTED, §3a), B4, M4 (short-gloss deviation ACCEPTED, §3b) confirmed. |
| ru | **PASS** | B1 (shortened-form deviation ACCEPTED, §3a), B4 confirmed. |
| zh-tw | **FAIL** | R-B6: P2 bridge still wraps to a punctuation-only line (§5). B4, B5, M2 confirmed fixed. |

## 2. Fix-verification table (Round 1 defects B1–B6, M1–M4)

Adjudications: CONFIRMED = fix present as claimed and correct; PARTIAL = the specific defect is gone but the same defect class remains; REFUTED = claim contradicted by the artifacts. Evidence is quoted from the SVG text elements (element IDs from `texts/*.txt` extraction, cross-checked by a second direct-SVG parse) and from the visual pass (`visual/verify2-*.png`).

### B1 — HOW LONG noun-phrase glosses (es/pt/ru P6) — CONFIRMED present as shortened question forms

Shipped titles (P6, x=1469, y=703, all three): es `HOW LONG? · ¿Cuánto dura?`, pt `HOW LONG? · Quanto dura?`, ru `HOW LONG? · Каков срок?` (elements P6 #182/183). The other 8 editions are unchanged and carry correct questions (incl. de `Wie lange im Amt?`, fr `Quelle durée?`, it `Quanto dura?`). Visually confirmed fitting inside their boxes (crops `verify2-b1-{es,pt,ru}-p6.png`; full frames `verify2-full-{es,pt,ru}-p6.png`). Whether the shortened forms are ACCEPTABLE is adjudicated in §3a: **ACCEPTABLE**. The fix claim (question forms present) is CONFIRMED; the deviation from the verdict's proposed full strings is accepted, not a defect.

### B2 — ko ABSTRACT typo — CONFIRMED fixed

`ABSTRACT.txt` (ko) now reads `NFL 뮌헨 경기` (U+BB8C `뮌` present, U+B326 `댦` absent), 479 bytes, single line + trailing newline, no ASCII double-quote. All 11 ABSTRACTs verified: single line, no ASCII double-quote, contain `150`, `Lucerna`, and A2–B2; reader-native; real topics named.

### B3 — ko P8 syllable splits — CONFIRMED fixed (S3 = 0)

- `솔퍼드` intact on one P8 line: `…는 솔퍼드에서 생방송돼요)`, y=1982.06. `묵념해요` intact (3 occurrences incl. P8 line-start `묵념해요)`, y=2163.41). Visually confirmed in crop `verify2-b3-ko-p8.png` (keys 68 and 130).
- Prior `koscan-ko.log` reports CANDIDATES=28, TRUE_SPLITS=13, S3=0, orphans 0, LEAD 1. This agent re-ran the CANONICAL script itself (`hidden_files/w46/koscan.py`, ko SVGs + `hidden_files/weekly-report-w46-en-ko-build`); the output (`verify2-koscan-canonical.log`) is BYTE-IDENTICAL to the fix worker's `en-fix/koscan-ko2.log` — CANDIDATES=28, TRUE_SPLITS=13, S3=0, orphans 0, LEAD 1 (see Correction addendum). The 13 confirmed true splits have max tail 2 syllables. The 5 candidates with tail ≥3 syllables are none of them confirmed true splits: 4 are confirmed spaced/word-boundary in the sources (`그리고`/`여러분의`, `금요일에`/`무엇을`, `시간이`/`걸려요`, `동안`/`묵념해요`), and the 5th (`항목대로`/`채점해요)`) is UNRESOLVED by the script's source check (trailing-paren artifact) but is semantically two words — no true mid-word split has tail ≥3. An independent same-x window reconstruction (`verify2-koscan.py` / `verify2-koscan.log`) had reproduced CANDIDATES=28 before the canonical script was located; it agrees. Orphan final lines 0; line-start orphan punctuation 1 (the frozen P8 `! See you on…` convention, Round 1 O2, unchanged). The remaining `갈라쇼`|`는` split has a 1-syllable tail, within the accepted S3 standard. The canonical SPLIT list also confirms O-R2-2's P2 `일`|`어날` split (tail 2, sub-S3) and the P3 `않`|`은` re-break (tail 1).
- Regression sweep (§2, M2 below): ko P3/P4 gloss boxes have no orphan lines — final lines P3 `은 것.`, P4 `스타선수.` (visually confirmed, crops `verify2-koregr-ko-p3.png` / `verify2-koregr-ko-p4.png`; P3 final line breaks `않`|`은`, a 1-syllable tail within the accepted precedent, exactly as the KIT regression note describes).

### B4 — lone `»`, all 11 (P7 toolbox) — CONFIRMED fixed

Zero lone-`»` elements in either parse path, all 11 editions. Every P7 carries `B1 — « Dickens wrote the story in` (y=443.1) + `1843.»` (y=477.3, element #66). Visually confirmed in all 11 B4 crops (`verify2-b4-*-p7.png`) and all 11 P7 full frames. The distinct line-32 example sentence `« Dickens wrote the story in 1843. » —` (P7 #41) keeps its spaced form deliberately — not a defect.

### B5 — lone `。`, P7 editor's note (core + zh-tw) — CONFIRMED fixed

Zero lone-`。` elements anywhere, either parse path. Both notes now read as 2 lines with `。` attached: core `投稿，故本期如实说明、不虚构来信；请把来信与写作寄来，VOL.4 起刊登收到的真实来信。` and the Traditional equivalent (zh-tw). The `你的` deletion preserves meaning ("please send [your] letters and writing" — possessor implied, natural Chinese) and was surgical: `你的` remains in 3 legitimate places per edition (P2 header, P2 question, P7 next-issue line). Visually confirmed (crops `verify2-b5-{core,zh-tw}-p7.png`; P7 full frames).

### B6 — lone `。`, P2 bridge (zh-tw) — PARTIAL → residual defect R-B6 (§5)

The specific lone-`。` element is gone, but the bridge still wraps to a punctuation-only final line (see §5 for full evidence). The fix worker's claim ("bridge now ends `）。`") misreads its own simulation: line 2 IS `）。`, not a line ending in it. Core bridge is a single clean line; de/fr bridges end with content-bearing lines.

### M1 — de/fr FINAL TEST untranslated tail — CONFIRMED fixed

de: `… · Die Antworten stehen am Ende dieser Seite`; fr: `… · Les réponses sont en bas de cette page`. All 11 editions now carry English + native tail (ja tail still glued with no separator — Round 1 O11, pre-existing, not counted). Visually confirmed in the P8 header band (crops `verify2-m1-{de,fr}-p8.png`).

### M2 — doubled gloss prefixes (fr/ko/zh-tw) — CONFIRMED fixed

Zero doubled prefixes anywhere (extraction + SVG paths). fr 5× single `Note |`, ko 5× single `해설 —`, zh-tw 5× distinct pair `譯注｜講解｜`; de 5× distinct pair `Anmerkung | Erklärung |` untouched; core 5× `译注｜讲解｜`. Visually confirmed: P2 gloss crops `verify2-m2-{fr,ko,zh-tw}-p2.png` — 3-line boxes, substantial final lines (shortest zh-tw P3 `來的。`, 2 content chars). A generic short-text scan found no other punctuation-only tails except R-B6 and the ja 1-kana tails (O-R2-1).

### M3 — de `call a race` gloss — CONFIRMED fixed

Old wording count 0. `das Ergebnis verkünden` ×2 exactly: P6 gloss line (P6 #74, `das Ergebnis verkünden · to certify =`) and P8 note 95 (P8 #247). Visually confirmed (crops `verify2-m3-de-p6.png`, `verify2-m3-de-p8.png`).

### M4 — nl/pt P3 titles — CONFIRMED present as short glosses; deviation ACCEPTABLE (§3b)

nl `SCROOGE'S NIGHT · Scrooge-nacht`, pt `SCROOGE'S NIGHT · A noite` (both P3, x=1469, y=873). Visually confirmed fitting in their boxes (crops `verify2-m4-{nl,pt}-p3.png`; full frames). Adjudicated ACCEPTABLE in §3b.

## 3. Deviation adjudications

Both deviations were measured by this agent with the build library's own metrics (sans bold 23pt, advance ≈ ink; `verify2-measure.py` / `verify2-measure.log`). The slot width SLOT = 416.0px was independently derived from SVG geometry, not accepted on faith: for all 22 title slots (P6 + P3 × 11 editions), box rect x=1451 width=434 (right edge 1885), title x=1469 start-anchored 23pt bold → 1885−1469 = 416.0px. Font: Noto Sans CJK SC (JP for ja, TC for zh-tw). The prior `measure_titles.py` re-run by this agent is byte-identical to `measure_titles.log` (`verify2-measure_titles-rerun.log`).

### 3a. B1 shortened forms — ACCEPTABLE

- Full verdict-proposed forms overflow the 416.0px slot: es `¿Cuánto dura el mandato?` 468.9px (+52.9), pt `Quanto dura o mandato?` 455.6px (+39.6), ru `Каков срок полномочий?` 473.0px (+57.0). Even the shorter alternative es `¿Cuánto dura el cargo?` overflows (429.6px, +13.6); dropping the question mark still overflows. Shipped forms fit with 80–97px spare (es 335.7, pt 328.7, ru 318.8).
- The shortened forms are correct, complete questions: es/pt `¿Cuánto dura?` / `Quanto dura?` ("How long does it last?") with the term referent supplied by the English head, the box body listing House/Senate/President/Governor term lengths directly below, and the P6 election-counting context; ru `Каков срок?` is lexically stronger since `срок` itself denotes a term/period.
- The IT precedent is decisive for consistency: Round 1 adjudicated it `Quanto dura?` (328.7px, identical construction) a correct question for this same box — es/pt cannot be failed for the identical form.
- Requiring the full forms would need a layout change (wider box / smaller font) disproportionate for a gloss whose referent is recoverable in situ. No fitting fuller correct form exists at 23pt among those tested.
- **Verdict: ACCEPTABLE. No Round 3 action for B1.**

### 3b. M4 short glosses — ACCEPTABLE

- Fuller forms all overflow: nl full mixed `De nacht van Scrooge` 487.5px (+71.5), no-article `Nacht van Scrooge` 455.0px (+39.0), full-caps 526.2px; pt full `A noite de Scrooge` 453.5px (+37.5), no-article `Noite de Scrooge` 436.0px (+20.0), full-caps 487.7px. Shipped: nl `Scrooge-nacht` 409.8px (spare only 6.2px, but fits; occlusion BOXTITLE silent) — a complete compound translation of "Scrooge's night," parallel to de `Scrooge-Nacht`; pt `A noite` 323.2px ("The night") — the English head supplies "Scrooge," the gloss supplies the head noun, exactly parallel to it `La notte` (336.8px), which Round 1 passed without criticism among the keepers.
- Short glosses adequately convey the header; no fitting fuller form exists.
- **Verdict: ACCEPTABLE. No Round 3 action for M4 (nl/pt).**

## 4. ES/FR observation verdict — DEFECTIVE as printed (R-M4)

- **Confirmed:** es P3 title is `LA NOCHE DE SCROOGE` and fr P3 title is `LA NUIT DE SCROOGE` (both x=1469, y=873, same slot as all other P3 titles), with NO English head. The fix worker's claim is correct; Round 1's M4 statement that "the other 9 editions keep" the pattern was wrong in count — only 7 editions keep it (core, de, it, ja, ko, ru, zh-tw); the droppers are nl, pt, es, fr (4). Visually confirmed (crops `verify2-m4-{es,fr}-p3.png`; P3 full frames).
- The translations themselves are correct. The defect is the lost English article title in the header, inconsistent with 9 of 11 editions after the nl/pt fix (7 keepers + 2 fixed).
- **Fixable WITHOUT layout change:** short mixed-case candidates fit comfortably — es `SCROOGE'S NIGHT · La noche` 345.9px (spare 70.1), fr `SCROOGE'S NIGHT · La nuit` 322.7px (spare 93.3), exactly parallel to pt `A noite` / it `La notte`. Fuller forms overflow (es full-mixed 476.2px, fr 452.9px; no-article es 446.6px, fr 423.3px — fr no-article overflows by only 7.3px, still overflow).
- **Classification — BLOCKING for es/fr.** Reasoning: (1) Round 1 already established this exact pattern as a defect requiring fix (M4, nl/pt); the fix round fixed 2 of the 4 instances of the same defect class, leaving 2. Shipping 2 editions carrying a defect class already judged defective in this same round would be inconsistent — the standard cannot depend on which editions the fixer happened to touch. (2) Proofread-until-zero is a hard shipping gate; a known defective header is not zero. (3) M4's "minor" label in Round 1 described severity inside a verdict that already failed every edition on blocking items; it was never adjudicated as shippable-with-defect, and no precedent in this process permits shipping an edition with a known Round-1-class defect. (4) The fix is a measured string swap with no layout change, so FAIL costs one small fix round, not a rebuild. The counter-argument (minor = shippable) is considered and rejected for reasons (1)–(3).
- **Verdict: R-M4 is a Round 3 fix item for es + fr. Both editions FAIL Round 2.**

## 5. Residual / new defects (complete list)

No other residual defects are established. The visual pass found nothing beyond these two items. Nothing else may be added to this list without quoted evidence.

### R-B6 (BLOCKING, zh-tw only) — P2 `B · WILL` bridge, punctuation-only final line

- Wrong text (rendered, 2 lines): `[p2-life#160 x=527 y=2037.5] 用 will + 動詞原形來改寫（承諾與將要發生的事` + `[p2-life#161 x=527 y=2067.225] ）。`. Visually confirmed: the second line contains only `）。` at the left margin (crop `verify2-b6-zh-tw-p2.png`; full frame `verify2-full-zh-tw-p2.png`). Same defect class as B6 (punctuation alone on a line). B6 adjudication: PARTIAL.
- Correct text (simulation-validated, 1 line, 427.9px at the bridge's 20.5pt sans in a 434px box — the CJK greedy-wrap simulator reproduces the core 1-line bridge and the current zh-tw 2-line `）。` tail exactly, validating the prediction): `用 will + 動詞原形改寫，承諾與將要發生的事。` — keeps `動詞原形` and the full meaning; drops only `來` and the parentheses. Alternative (2 lines ending `的事。`): `用 will + 動詞原形來改寫，表達承諾與將要發生的事。` (see `verify2-bridge-cands.log` for all candidates).
- Round 3 instruction: apply the 1-line text (or the alternative), RE-SIMULATE with the real wrap, re-render, and VISUALLY CONFIRM at full frame that no punctuation-only line remains. Also correct the zh-tw WEEKLY-KIT.md fix-record line, which currently misdescribes the render ("bridge now ends `）。`") — as printed, `）。` is a standalone line, not a line ending. Do not repeat the fix worker's misreading.
- Note: the fix worker's rewording kept the praised `動詞原形` clarification; the residual is purely the wrap, not the wording choice.

### R-M4 (BLOCKING, es + fr) — P3 box titles lack the English head

- Wrong text: es `[p3-culture#160] LA NOCHE DE SCROOGE`; fr `[p3-culture#159] LA NUIT DE SCROOGE`.
- Correct text: es `SCROOGE'S NIGHT · La noche` (345.9px, fits); fr `SCROOGE'S NIGHT · La nuit` (322.7px, fits). Same slot, same pattern as the fixed nl/pt titles.
- Round 3 instruction: swap the two title strings at build source, re-render P3 for es/fr, re-run the title-slot measurement + occlusion check, and visually confirm at full frame. No layout change is needed or permitted for this fix.

## 6. Gate-verification record (re-run vs reused)

### 6.1 Freshness — gate outputs are NOT stale

No edition file changed after the gate outputs were produced. Edition SVG/card max mtimes 02:20–02:57 UTC 2026-11-03; web PDFs/text.md 02:24–02:57 UTC; `WEEKLY-KIT.md` newest 03:04:28 UTC in every edition; gate outputs 03:07:19–03:13:54 UTC 2026-11-03. The fix worker finished ~03:04 UTC as stated in the task. Reuse of prior outputs below rests on this freshness, plus the spot re-runs in §6.2.

### 6.2 Spot re-runs by THIS agent — byte-identical

Freeze + p8 (`--total 150`) + occlusion re-run for ko, zh-tw, and one Latin edition (de). All exits 0; all JSONs and logs byte-identical to the prior agent's outputs (saved as `verify2-freeze-{ko,zh-tw,de}.json/.log`, `verify2-p8-*.json/.log`, `verify2-occlusion-*.json/.log`). Freeze totals: de 0, ko 2375, zh-tw 680. P8: de EXTRA_ONLY 70→150, extra 80, keydiff `[137,138,139,140,150]`; ko/zh-tw CLEAN 70→70, same keydiff, missing=[] uncertain=[]. Occlusion: 0 flags, selftest OK, all three. `measure_titles.py` re-run byte-identical to `measure_titles.log` (`verify2-measure_titles-rerun.log`). No spot check disagreed, so no full-gate re-run was required.

### 6.3 Reused after verification (prior agent's outputs, freshness + spot-check basis)

Rowcheck logs (all 11 read in full — 80 CLEAN, 0 COLLIDE, P6 chart-label GRAZE 0.0% everywhere, gloss counts OK; the rowcheck script itself was not re-run); R1→R2 multiset diff (read in full — changes confined to claimed fix lines plus reflow lines in fr/ko/zh-tw gloss boxes and ko P8 reflow; no unexpected string churn); freeze/p8/occlusion outputs for the other 8 editions (freshness + identical spot re-runs for 3 editions, incl. both CJK editions).

### 6.4 Provenance gaps and corrections (stated honestly)

- **Koscan script — CORRECTED (see addendum).** The canonical script exists at `hidden_files/w46/koscan.py` and was re-run by this agent against the correct inputs (ko SVGs + `hidden_files/weekly-report-w46-en-ko-build`); output `verify2-koscan-canonical.log` is byte-identical to the fix worker's `en-fix/koscan-ko2.log` (CANDIDATES=28, TRUE_SPLITS=13, S3=0, orphans 0, LEAD 1). B3 rests on this canonical re-run. The original "script not preserved" claim was wrong: the script lives outside the three locations first searched, and the broad greps meant to find it were killed before completing. Two runs against wrong (other-family) build dirs are preserved as superseded attempts and must not be cited.
- **Masthead scan corrected.** A first masthead pixel scan (`verify2-masthead-bars.log`) was contaminated by rule lines and reported a uniform 65–1884 range — DISCARDED, do not cite. The row-filtered scan (`verify2-masthead2.log`, glyph rows only) supersedes it and reproduces Round 1 exactly for the tight fits (FR 89–1861, IT 65–1885; see §7). One immaterial variance: ko right edge 1384px (this scan) vs 1369px (Round 1) — different band/threshold, ~500px clearance either way, FITS.
- **Wrap-simulation limitation.** The CJK greedy-wrap simulator (sans 20.5pt, width 434) reproduces the core 1-line bridge and the zh-tw current 2-line `）。` tail exactly. The same approach with serif 22.5pt did NOT reproduce the B4 toolbox word-wrap (Latin text wraps at word boundaries, not char-by-char); B4 rests on extraction + visual evidence, not on that simulation.
- **SC-residue / provenance literal scans — decision.** The broader simplified-residue scan for zh-tw and the source-literal provenance scan (ko new-Han literals / zh-tw identical-to-core literals) were verified in Round 1 and were NOT independently re-run by this agent. DECISION: the claim rests on Round 1 + freeze evidence + this agent's script scan (ko Hangul 2375 only, 0 Han, matching freeze total; zh-tw Han 1728 only; Latin editions 0 non-Latin chars; ru Cyrillic 5437 only; ja Han 1160 + Hiragana 928 + Katakana 402 — matching the fix-report script scan exactly), because no zh-tw/ko string changed in the fix round except the verified items (M2 prefix pair, both Traditional; B4/B5 lines; ko P8 reflows, pure Hangul — freeze delta pure Hangul, ko 2381→2375; zh-tw 679→680, +1 is the M2 `講解` pair, all Traditional Han). This limitation is stated explicitly; it is not silently assumed.

## 7. Gate outputs summary (verified)

- **Freeze:** added CJK 0 for all Latin editions (P8 residual 2 = U+FF1B fullwidth semicolons inside frozen key strings, not a defect); ja 2188, ko 2375, zh-tw 680 — matching KIT claims as amended by the fix record.
- **P8 (`--total 150`, authoritative; the default `--target en` uses stale total 149):** core 70 noted; CLEAN es/it/ja/ko/pt/ru/zh-tw 70→70; EXTRA_ONLY de/fr/nl 70→150, identical extra lists (80 numbers), keydiff `[137,138,139,140,150]` in all 10 fan-outs — legitimate (137–140 translation keys re-aimed per reader language; 150 open writing pointer). Missing=[], uncertain=[] everywhere.
- **Occlusion:** 0 flags in all 11 (prior outputs + spot re-runs identical, selftest OK every run).
- **Rowcheck:** 80 CLEAN, 0 COLLIDE (all 11 logs read); P6 GRAZE 0.0% everywhere.
- **Counts re-measured:** registry `hidden_files/w46/en-core/registry.json` — 150 entries, numbers 1–150 unique, no missing/dup, all keyed; per-page 10/17/18/18/18/18/12/39; levels A2 60 / B1 69 / B2 21. Every `.text.md` Answers section: 150 entries, 150 unique. Confirms KIT.
- **P1 Searches bars (SVG rects, this agent):** all 11 editions identical widths 250/218/186/140/108 px, strictly decreasing in label order 1–5, olive `#3e4c2a` first, tan `#b3a06a` rest, labelled as relative snapshots. **P6 chart:** no bar-like rects in any edition (26 rects total per P6 SVG: frames/boxes/badges only) — the P6 "chart" is text rows, consistent with GRAZE 0.0% and the core KIT.
- **P7 golden phrases:** 88/88 verified verbatim (joined per-page text, this agent's check) in all 11 editions — the 8 Round 1 sentences, same wording. (The prior `golden-bars.log` reading "MISSING" on all 88 lines is an uninterpretable leftover — no producing script was preserved — and is NOT treated as a failure; the phrases were independently re-verified 88/88 from SVG texts.)
- **Masthead pixel clearance (glyph rows only, `verify2-masthead2.log`):** FR at 42pt ink 89–1861, clearance 24/24 — FITS, reduction confirmed necessary and sufficient. IT at 46pt ink 65–1885, clearance 0/0 — FITS, marginal/flush, no clipping (Round 1 O1). Others: core 561–1387 (496/498), de 134–1815 (69/70), es 154–1795 (89/90), ja 476–1473 (411/412), ko 580–1384 (515/501), nl 226–1722 (161/163), pt 123–1826 (58/59), ru 136–1814 (71/71), zh-tw 561–1387 (496/498). Masthead sizes from SVG: FR 42pt, all others 46pt. Visually confirmed on all 11 P1 full frames.
- **Badge/footer:** P1 badge/tagline element (#5) present in all 11 (native pairing line, e.g. de `ENGLISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — …`; core carries the frozen tagline `THE LEARNERS' WEEKLY — …` in that slot, adjudicated not a defect in Round 1). Footer at y=2624 on all 8 pages in every edition. Pairing badge visibly in P1 masthead area and footer labels — confirmed via extraction + P1 full frames.
- **Image credits:** all 5 present in SVG texts of all 11 editions (Claude Monet, Horace Nicholls, John Leech, Frank R. Snyder, Kenneth C. Zirkel); visually confirmed on the pages viewed.
- **PDFs (this agent):** every web PDF 8 pages, ≤7 MB (1,547,039–2,204,469 bytes), `pdftotext` bytes > 0 and EQUAL to print-PDF extraction per edition (core 45003, de 48519, es 46197, fr 49189, it 45896, ja 47288, ko 47052, nl 48518, pt 46077, ru 50959, zh-tw 44908). Real text layer confirmed.
- **ABSTRACTs:** all valid (§2/B2); reader-native, real topics + masthead + levels + 150.
- **W45 promises honoured as disclosed:** the unchanged disclosure lines were seen in extraction and on the viewed pages — P1 IN BRIEF election line ("Nov 3: Americans voted. Press time Nov 2: no results, none invented. (p. 6)"), P6 patience/results sentences ("When the verified results are in, VOL.4 will report them… Patience is part of the system, not a failure of it."), P7 editor's note (VOL.2 promise, no real letters received, honest disclosure, real letters from VOL.4 conditional on receipt), P6/P7 next-week lines (verified midterm results; NFL Munich Sun Nov 15). No fix-round change affects them.

## 8. Visual pass record

Full record: `visual/verify2-visual-pass.log`. 45 full-frame views (P1×11, P8×11, P7×11, P6×4, P2×3, P3×5, P4×1) + 30 full-resolution element crops, all viewed by this agent, all saved under `visual/` with `verify2-` prefixes (78 files total). Findings: no overflow, overlap, missing glyphs/tofu, or missing image credits anywhere viewed — EXCEPT the two residual defects R-B6 (zh-tw P2, §5) and R-M4 (es/fr P3, §4), each confirmed at full frame and in crop. The prior agent left `visual/` empty; this pass is this agent's own work. No edition file was re-rendered or edited for this pass (shipped cards only).

## 9. Other verifications and observations

- **Native-language correctness:** no new native-language strings were introduced except the fix strings, all verified in §2. Round 1's full diff read stands. Every explanation/gloss/note/abstract/footer is in the reader's native language; no untranslated strings found (ja FINAL TEST tail glued with no separator is the pre-existing Round 1 O11, not counted).
- **KIT fix records:** spot-read in all 11 editions. The fix record sections match FIX-REPORT.md claims, including the ko regression note (matches the rendered gloss boxes exactly) and the FR masthead history (46→44→42pt, consistent with Round 1). TWO KIT inaccuracies to correct in Round 3: (a) the zh-tw KIT B6 line misdescribes the render ("bridge now ends `）。`" — see §5/R-B6); (b) the es/fr KITs do not record the P3-title defect — Round 3 must add the R-M4 fix record. The core/de text.md format-change documentation in the KITs (canonical `en_textmd.py`, old files under `en-fix/old-textmd/`) is accurate.
- **Text.md format change (core/de) — ACCEPTABLE, indeed more faithful.** For 9 editions (es/fr/it/ja/ko/nl/pt/ru/zh-tw) the new-vs-old diffs are fix-lines only (with the pre-existing exporter prefix convention: gloss lines in text.md show the source call string without/with partial furniture prefix, while rendered SVGs carry the full prefix — a convention, not a mismatch). For core/de the format change is larger (old exporter emitted `serif`/`sans` font tags, `MATCH:` blocks, `({...})` placeholders; new exporter emits joined headings, `EXERCISE:` lines, resolved numbers). First 6 header lines identical; Answers 150/150 both; the only Answers content diffs in core are stems 17–19, where the NEW export matches the rendered P8 keys exactly (`17. She will wear a poppy. · 18. We will stand still. · 19. Will they watch the ceremony?`, P8 #176–177) while the OLD export had longer stems; de new export resolves all `({...})` placeholders and its only Answers diff is the M3 line. Totals and changed lines verified. Record the prefix-convention caveat.
- **O-R2-1 (observation, NOT a defect):** Japanese 1-kana + `。` final lines (ja P2 `う。`, P3 `い。`, P6 `う。`, P7 `く。`) — content mora + period, normal Japanese wrap, unchanged since Round 1 (ja R1→R2 diff shows only B4 lines changed), not flagged by Round 1's full read. Explicitly distinguished from zh-tw `）。` (zero content characters, punctuation alone). No new defect class is invented for them.
- **O-R2-2 (observation, NOT a defect):** ko P2 `B · WILL` bridge breaks `일어나다` as `일` | `어날` (elements P2 #160/161: `will + 동사원형으로 바꿔 쓰세요(약속과 앞으로 일` / `어날 일).`). Mid-word break, 2-syllable tail — BELOW the S3 (tail ≥3) blocking bar, pre-existing since Round 1 (absent from the R1→R2 diff), outside the B3 P8 scope. Recorded for the record only; it does not change any verdict and is not a Round 3 fix item. (For scale: the accepted `갈라쇼`|`는` precedent is a 1-syllable tail; this is the same class, one syllable longer, still sub-S3.)
- **No international politics / English-news preference:** unchanged since Round 1; the issue's P6 subject is US domestic election administration (target-country domestic politics of the English-speaking world, carried with the plain no-results disclosure) and the P1 lead is UK/Commonwealth remembrance — no new content was introduced in the fix round.

## 10. Round 3 fix list (for the fixer — proofreader does not fix)

1. zh-tw: R-B6 — replace the P2 bridge text per §5, re-simulate, re-render, visually confirm; correct the KIT B6 line.
2. es: R-M4 — P3 title → `SCROOGE'S NIGHT · La noche`; re-render P3; re-measure + occlusion; visually confirm.
3. fr: R-M4 — P3 title → `SCROOGE'S NIGHT · La nuit`; re-render P3; re-measure + occlusion; visually confirm.
4. Re-gate the three fixed editions (freeze/p8/occlusion for the touched pages at minimum; full gate preferred since re-renders are cheap), re-run the R1→R2-style multiset diff to confirm no other string changed, and add fix records to the three KITs. Round 3 proofread need only re-verify the three fixed items + the diff — the other 8 editions' PASS stands.

## 11. Answer-key semantic audit (supplementary requirement — see Addendum 2)

### 11.1 Method

- **Source of truth for stems/options/facts:** the core manuscript export (`files/weekly-report-w46-en-core/2026-w46-en-zh-cn.text.md`, read in full: all article paragraphs, all EXERCISE stems with options, all MATCH word/definition lists) + the rendered SVGs (cloze option lists 112–119 and the P3 COMING SOON box date for #33 confirmed directly from SVG text elements). Every key below was checked against meaning, grammar, or article fact — not against another key list.
- **Registry vs printed:** core registry (`hidden_files/w46/en-core/registry.json`, 150 entries) compared with the printed P8 keys extracted by `p8.py extract --total 150` from the core P8 SVG (re-run by this agent, byte-identical to `p8-core.json`).
- **Cross-edition:** `p8.py extract --total 150` run by this agent for EACH of the 10 fan-out editions (`verify2-p8keys-{ed}.json/.log`); every printed key value compared against the core's, number by number.
- **Independent letter check:** a second, independent parse of the raw P8 SVG `<text>` elements (answers region y>1850, grouped by x-column, joined; regex `N. LETTER`) for the 79 single-letter keys in all 11 editions (`verify2-keyaudit-letters.py`, output `verify2-keyaudit-crossedition.log`). This guards against a shared extraction bug hiding an identical transposition in every edition. (First attempt with a y>1930 cutoff missed column tops starting at y≈1917 and was corrected; the corrected run is the result cited.)
- **Arithmetic recomputed** from the article's own dates, not copied from the key (see §11.4).

### 11.2 Cross-edition printed-key result — 150/150 present, letters identical

- All 150 keys are present in the printed P8 answers of all 11 editions.
- The ONLY value differences vs the core in any edition are the 5 legitimate translation items, identical in kind across all 10 fan-outs: **137, 138, 139, 140** (the four translation sentences re-aimed into the reader's native language — same sentences, correctly translated; verified by reading) and **150** (the open-task pointer in the reader's language). This is exactly the `keydiff [137,138,139,140,150]` already adjudicated legitimate in the p8 gate.
- Every LETTER key is identical in all 11 editions: independent parse, 79 letters × 11 editions = **869 checks, 0 mismatches** (0 wrong letters, 0 missing).
- Registry vs printed core keys: 1 difference, immaterial — #150 only (registry carries the full pointer text `开放题 — 要点见写作框，范文在第 8 版写作框内`; the printed key is the short form `开放题`). #150 is open-ended with no letter key; no transposition risk.
- Note on RU 137: the extract value reads `Терпение` ("Patience") alone. This is a dash-split extraction artifact, NOT a truncation in print — the raw SVG shows the full sentence printed across wrapped elements (`137. Терпение — часть…`, continuing on following lines). Verified in the raw SVG; not a defect.

### 11.3 Matching-block table — every block matched option-by-option

Each word was matched to its definition on meaning; every alternative pairing is semantically excluded. Each block uses each letter exactly once (permutation intact — the transposition pattern would break meaning, and meaning was checked independently of the permutation).

| Block | Word → definition (verified) | Keys |
|---|---|---|
| P2 D·THE WORDS (24–27) | 24 a poppy → **a.** a red flower worn in November · 25 an armistice → **b.** an agreement to stop fighting · 26 a veteran → **c.** a person who served in the forces · 27 a ceremony → **d.** a formal public event | a, b, c, d |
| P3 C·THE WORDS (38–41) | 38 a miser → **b.** a person who loves money and hates spending it · 39 a ghost → **c.** the spirit of a dead person · 40 a heist → **d.** a robbery, usually of a bank · 41 a catchphrase → **a.** a line everybody repeats | b, c, d, a |
| P4 C·THE WORDS (56–59) | 56 a fixture → **b.** a game in a season's schedule · 57 a group → **d.** a small set of players who play each other · 58 a finale → **c.** the last event of a season · 59 a star → **a.** a famous player, loved by the fans | b, d, c, a |
| P5 C·THE WORDS (74–77) | 74 an appeal → **c.** a public call for help and money · 75 a challenge → **d.** a hard task you take on · 76 kindness → **a.** being kind to other people · 77 a marathon → **b.** a race of about 26 miles | c, d, a, b |
| P8 F·WORDS (141–144) | 141 a silence → **b.** a quiet time with no speaking · 142 an armistice → **c.** an agreement to stop fighting · 143 a runoff → **a.** the second vote, when no one wins a majority · 144 a miser → **d.** a person who loves money and hates spending it | b, c, a, d |

Spot-exclusions (why no swap is possible): a poppy is not an agreement, a person, or an event; an armistice is not a flower, a person, or an event; a runoff is not a quiet time, an agreement, or a person; a marathon is not a call for help, a task, or kindness. All 20 pairings forced by meaning. **20/20 correct.**

### 11.4 Semantic verification by type — 150/150

- **MCQ letters (7–10, 20–23, 28–33, 46–51, 64–69, 82–93, 120–132):** each checked against the article facts and the printed options. All correct — including the distractors' exclusion (e.g. #7 B Wednesday Nov 11, not Nov 13/15; #21 C 1920, not 1918/1919; #47 C 3:30 p.m. local, not 9:30 a.m. Munich time; #50 C North Macedonia, not Spain/Croatia; #91 B Alaska and Maine, not Texas/Florida or Ohio/Georgia).
- **Chart/arithmetic (82–87), recomputed:** Election Day 2022 = Tue Nov 3. Senate decided Saturday after = Nov 7 → **4 days** (#82 B ✓). House decided Wednesday after = Nov 11 → **8 days** (#83 C ✓). Difference 8−4 = **4 days** (#87 C ✓). #84 A (Nov 10–Dec 18), #85 B (Dec 1), #86 A (history, not a prediction) verbatim from the article ✓.
- **Cloze/fill word keys (1–6, 11–15, 34–37, 52–55, 70–73, 94–99, 112–119):** grammar + article facts. All correct — including #53 `begin` (plural subject "The ATP Finals"), #55 `eight` ("The eight best singles players"), #97 `takes` (singular "Counting"), #98 `differs` (singular "The rule"), #112 B Wednesday (Nov 11, 2026 is a Wednesday; issue week Mon Nov 9–Sun Nov 15), #115 B Eleven, #117 C will, #118 B going, #119 A still.
- **Transformations (16–19, 42–45, 60–63, 78–81, 100–107, 133–136):** tense/agreement/construction. All correct — will-future (#16–19), past simple (#42–45, #60–63, #134), present continuous (#78–81), third-person -s (#100, #102, #104), `were` (#107), `Whether`-fronting (#136).
- **Error correction (108–111):** `doesn't` (#108), `fell` (#109), `bigger` without `more` (#110), `will watch` (#111). All correct.
- **Dialogue (145–149):** ticket / line / scarf / anthem / Sunday — each forced by the following line (show it; five minutes; wear it with pride; two anthems; the game is Sunday Nov 15). All correct.
- **Translations (137–140):** Chinese renderings faithful to the English sentences (patience/system/failure; Wednesday Nov 11, 11 a.m., two minutes; Sunday/NFL/Munich; not-every-country/same-name). All correct.
- **Open writing (150):** no letter key; pointer only. Not applicable to the transposition class.
- **Adjacent-swap sweep:** the specific ZH-CN/RU defect pattern (neighbouring key letters transposed) was checked by meaning at every adjacent pair, not just by permutation: no adjacent pair in any block or MCQ run is meaning-swapped. **Total: 150/150 semantically correct; 0 wrong key letters; 0 transpositions.**

### 11.5 Conclusion

The frozen-core LETTER-transposition defect class found in the ZH-CN sibling (and in RU in Round 1) is **ABSENT from the EN family**: core keys are semantically right, and all 11 editions print the same letters. No new blocking defect arises from this audit. The Round 3 fix list in §10 is unchanged (R-B6, R-M4 only); no registry change and no re-render is required for keys.

---

**ROUND 2 FAIL — blocking defects: R-B6 (zh-tw, P2 bridge punctuation-only line) and R-M4 (es + fr, P3 titles lacking the English head). 8 editions PASS (core, de, it, ja, ko, nl, pt, ru). Deviations B1-shortened-forms and M4-short-glosses ACCEPTABLE. Answer-key audit: 150/150 semantically correct, letters identical in all 11 editions — no additional defect.**
