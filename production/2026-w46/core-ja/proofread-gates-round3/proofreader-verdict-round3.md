# Proofreader verdict — Round 3, Lucerna Weekly W46, JA family

Issue: VOL.3, dated Mon 2026-11-09 – Sun 2026-11-15. Target language: Japanese.
Scope: all 11 JA-target editions (one per reader-native language).
Proofreader: independent; did not build or fix these editions. No edition file
was edited, re-rendered, pushed, inserted, or posted by the proofreader.
Gate dir: `hidden_files/w46/ja-proofread-gates-round3/` (fresh; earlier gate
dirs not reused). All gate JSONs/logs cited below live in that dir.

Round 2 verdict: FAIL on ONE defect, D-KEY-42 (all 11 editions). This round
re-verified the fix and re-ran the FULL round because the fix touched the
frozen core registry.

## Per-edition verdict

| Edition | Verdict |
|---|---|
| 2026-w46-ja-zh-cn (core) | PASS |
| 2026-w46-ja-de | PASS |
| 2026-w46-ja-en | PASS |
| 2026-w46-ja-es | PASS |
| 2026-w46-ja-fr | PASS |
| 2026-w46-ja-it | PASS |
| 2026-w46-ja-ko | PASS |
| 2026-w46-ja-nl | PASS |
| 2026-w46-ja-pt | PASS |
| 2026-w46-ja-ru | PASS |
| 2026-w46-ja-zh-tw | PASS |

## §1 Fix verification — D-KEY-42: CONFIRMED fixed in all 11 editions

Defect: P8 key 42 omitted the stem piece `酉の市で`; correct key
`酉の市で熊手を買います。`.

Rendered P8 key-42 line (full line incl. reader-language note, from
`p8-tesuto.svg`), all at x=527:

| Ed. | Rendered key-42 line | y |
|---|---|---|
| zh-cn | `42. 酉の市で熊手を買います。 — 在酉の市买熊手` | 1428.984 |
| de | `42. 酉の市で熊手を買います。 — Einen Kumade auf dem Tori-no-ichi` + wrap line `kaufen` (see DE ruling) | 1368.877 / 1383.454 |
| en | `42. 酉の市で熊手を買います。 — Buying a kumade at Tori-no-ichi` | 1428.984 |
| es | `42. 酉の市で熊手を買います。 — Comprar un kumade en Tori-no-ichi` | 1396.854 |
| fr | `42. 酉の市で熊手を買います。 — Acheter un kumade à Tori-no-ichi` | 1368.877 |
| it | `42. 酉の市で熊手を買います。 — Comprare un kumade a Tori-no-ichi` | 1368.877 |
| ko | `42. 酉の市で熊手を買います。 — 도리노이치에서 구마데 사기` | 1368.877 |
| nl | `42. 酉の市で熊手を買います。 — Een kumade kopen op Tori-no-ichi` | 1424.831 |
| pt | `42. 酉の市で熊手を買います。 — Comprar um kumade em Tori-no-ichi` | 1424.831 |
| ru | `42. 酉の市で熊手を買います。 — Покупка кумадэ на Тори-но-ити` | 1424.831 |
| zh-tw | `42. 酉の市で熊手を買います。 — 在酉の市買熊手` | 1428.984 |

- Old form `42. 熊手を買います。` (without `酉の市で`): 0 occurrences in all
  SVGs and all `.text.md` exports (grep exit 1). In PDF text layers each web
  PDF contains the new key-42 form exactly once; the only other
  `熊手を買います` line is the legitimate P3 article sentence
  `酉の市では、熊手を買います。` (with stem-piece context `酉の市では` + `、`),
  not the old key form. `.text.md` key-42 lines correct in all 11 (DE carries
  the faithful `kaufen` continuation line). Print PDFs show key 42 correct
  in all 11.
- Notes UNCHANGED: byte-identical to the pre-fix notes retained in
  `hidden_files/w46/ja-fix-round3/key42-before.json` for all 11 editions.
- Sibling 造句 keys 39/40/41/133/134/135/136 unchanged and complete in all
  11 (core: 39 `七五三は子どものお祝いです。`, 40 `神社へお参りに行きます。`,
  41 `千歳飴をもらいます。`, 133 `私は水よう日に友達とポッキーを分けます。`,
  134 `七五三は子どものお祝いです。`, 135 `神社で千歳飴をもらいます。`,
  136 `ソフトバンクは4連勝で日本一になりました。`; notes differ per reader
  language as designed).
- Source level: `content34.py:95` in all 11 build copies carries the new key
  with unchanged notes; old exact-quoted key `"熊手を買います。"` = 0 in all
  11 build dirs. Source-hash check vs `ja-fix-round3/before-source-sha256.txt`
  (30 entries): exactly the 11 `content34.py` files CHANGED; `bslib4.py`,
  `content12/56/7/8.py`, `run.py`, `render.py`, `svglib.py`, all 10
  `transform.py`, `gen_ja_zhtw.py`, and MAP `hidden_files/w46/maps/zh-tw.json`
  (187 entries) all SAME / hash-identical.

### DE wrap adjudication — RULING: ACCEPTABLE (not a defect)

Evidence (measured independently with the build's own `svglib.text_w` /
`wrap`, tools venv; font sizes read from the elements themselves: DE 12.9,
zh-cn/en/zh-tw 13.3; log: `de-wrap-measurements.log`):

- Unwrapped DE full line `42. 酉の市で熊手を買います。 — Einen Kumade auf dem
  Tori-no-ichi kaufen` = 466.1px at 12.9pt vs the 434px column (over by 32.1).
- `wrap(..., 434)` returns exactly
  `['42. 酉の市で熊手を買います。 — Einen Kumade auf dem Tori-no-ichi', 'kaufen']`.
  Rendered line 1 = 419.0px, right edge x=946.0 < column end 961, next column
  at 989 — no overflow into the next column. Line 2 `kaufen` = 43.8px at
  x=527, y=1383.454 (14.577 below line 1). The break is at a space before
  `kaufen`; no word, bracket, or punctuation split.
- All other editions' key-42 lines fit one line at their native sizes:
  zh-cn/zh-tw 292.8, en 407.9, es 421.2, fr 405.8, it 419.7, ko 351.0,
  nl 411.3, pt 429.3, ru 406.7 (all ≤ 434).
- Precedent in the same DE P8: key 68 wraps onto single-word second line
  `Schrein` (y 2169.810 → 2184.387) and key 97 onto `(Donnerstag)`
  (y 1890.894 → 1905.471) — the same single-word-continuation pattern.
- Keys-flow end-y unchanged: DE max non-footer text y = 2535.011 (Round 2:
  2535.0). Kinsoku/orphan scans 0 in DE; canonical occlusion audit 0 flags
  in DE. Visual check of the DE P8 card: the wrap renders tidily with no
  overlap (see `visual-review-round3.md`).

Ruling: the DE two-line wrap is a clean space-break wrap of the same class
as keys 68/97 in the same edition, with no overflow, orphan, or overlap.
ACCEPTABLE. No fix required.

### Whole-tree old-md5 grep — Round 2 caveat COMPLETED

Old md5 `d73e23b365676c3618d7e060b835eb4d`; new md5
`74177544422fe677639d769cd80499fb` (core `svglib.py` md5 verified by
`md5sum`; NO_END block present at lines 78–82).

- Whole-tree grep: `timeout 600 grep -r -I -n --exclude-dir=venv <old-md5> .`
  from the goal dir (26G, 71,145 files) COMPLETED in ~423s, before the
  timeout. 173 hit lines in 145 distinct files (log: `md5-grep-old.log`;
  `.err` holds only grep's "input file is also the output" warning for the
  log file itself, which sits inside the scanned tree; the log holds no
  self-hit). Scope note: `-I` skips binary files and `venv` was excluded;
  the string is a source-code guard value, and edition SVG/.text.md text was
  verified separately by extraction.
- Classification (full list in `md5-grep-classification.txt`): ZERO hits in
  any live W46 build source — no hits in any
  `hidden_files/weekly-report-w46-ja*-build/` dir, `hidden_files/w46/maps/`,
  `hidden_files/w46/gen_ja_zhtw.py`, the canonical toolkit, or any edition
  SVG/`.text.md`/PDF-text/ABSTRACT. Every hit is a historical record or
  backup:
  - 52 `WEEKLY-KIT.md` record files (11 W46 + 41 older issues): each quotes
    the old md5 inside a dated fix-history/provenance record of the form
    `OLD → NEW` (W46: the Round 1 wrap-level fix record; e.g. core KIT
    lines 182–184). Records, not sources.
  - 68 files under `hidden_files/w45/*` (proof REPORTs, LEDGER, scratch
    build copies) + 22 under `hidden_files/weekly-report-w45-*-build/`:
    W45-cycle historical snapshots/records (the W45 es-ja `svglib.py`
    itself md5s to a different value; the old md5 appears only in a comment).
  - `hidden_files/ja-p7-overprint-correction.md`: record.
  - `hidden_files/w46/ja-fix/FIX-REPORT.md:46`: record quoting `OLD → NEW`.
  - 2 files `tools/scratch/rerun-ja-ru/{gen_transform.py,transform.py}`:
    2026-10-28 VOL.2/W45-era rerun scratch ("reads the PRISTINE W45 JA core
    build"), not referenced by any W46 build dir; the live W46 RU guard
    carries the NEW md5 (verified directly below).
- Guard files verified directly: `CANON_SVGLIB_MD5` = new value in all 10
  guard files (9 fan-out `transform.py` + `gen_ja_zhtw.py`), each with an
  md5 assert; 0 occurrences of the old md5 in those files or core
  `svglib.py`. A targeted grep over all 11 W46 build dirs + tools + all 11
  edition dirs returned only the KIT record quotes and the 2 scratch files
  above (log: `md5-grep-live-sources.log`).
- Round 1 fixes survive: kinsoku 0/0/0 (see §3), abstracts hash-identical
  to the recorded AFTER text, zh-tw MAP 187 entries hash-identical with all
  8 Traditional conversions intact + SC scan clean (see §3), svglib md5
  unchanged (new value).

### Fix-claim adjudication

| Claim (FIX-REPORT.md + WEEKLY-KIT §12/§6 records) | Adjudication |
|---|---|
| One-line source change, core `content34.py:95`, key arg `熊手を買います。` → `酉の市で熊手を買います。` | CONFIRMED |
| Propagated to all 10 fan-outs by regeneration at each `content34.py:95` | CONFIRMED |
| Stem/notes/article/everything else untouched | CONFIRMED |
| No `transform.py` or MAP edited | CONFIRMED |
| Old form 0 everywhere (SVG/.text.md/PDF) | CONFIRMED |
| Notes unchanged in all 11 | CONFIRMED |
| Siblings 39/40/41/133/134/135/136 unchanged and complete | CONFIRMED |
| DE line-fit exception flagged; wrap as described | CONFIRMED as described; ruled ACCEPTABLE (above) |
| Re-gates clean | CONFIRMED (own re-gates, §3) |
| Change isolation exactly 44 files (4/edition) | CONFIRMED (§4) |
| Round 1 fixes survive (svglib md5, MAP 187, abstracts) | CONFIRMED |
| WEEKLY-KIT fix records appended to all 11 KITs | CONFIRMED — `D-KEY-42` record present in all 11 KITs (core §12, fan-outs §6 Fix history); core record quotes before/after lines verified against the rendered SVG lines; earlier sections untouched (append-only; record sits in its own §12 section) |

## §2 Full key-letter verification — 150/150 CONFIRMED in all 11 editions

Method: (a) read the full core `.text.md` (1329 lines) and verified every key
1–150 semantically against stems, articles, and grammar; (b) extracted the
P8 key value of every edition from its `.text.md` (joining wrap
continuations) and diffed all 150 values against the core
(log: `key-compare.log`); (c) `p8.py extract` 150/150 noted set per edition;
(d) verified matching-block stems/options strings present in every edition's
SVGs; (e) `p8.py compare` CLEAN per edition (§3).

Result: keys 1–150 are semantically correct in the core, and every edition's
rendered P8 keys are identical to the core's except the adjudicated 137/138
redirects (and the key-150 footer-pointer wording, an extraction join
artifact — the footer text itself differs by reader language as designed).
No wrong key letter in any edition. The ru key-137 full SVG line was
verified directly: `137. Сити-Го-Сан — 15 ноября. — См. страницу 3`
(x=1451, y=1958.748); the truncated form in the text-diff is an extractor
artifact of splitting on ` — `.

### Matching blocks (stem + options + key), verified in all 11 editions

Block 25–28 (P2, word↔meaning). Stems: 25 ポッキー, 26 プリッツ,
27 千歳飴, 28 熊手. Options: a. red-white long candy / b. lucky rake /
c. salty thin biscuit / d. chocolate thin biscuit.
Keys: 25→d, 26→c, 27→a, 28→b — identical in all 11 editions.

Block 43–46 (P3, word↔meaning). Stems: 43 七五三, 44 千歳飴, 45 熊手,
46 酉の市. Options: a. 11月の酉の日に開くお祭り / b. 3歳・5歳・7歳の子どものお祝い /
c. 商売繁盛の縁起物 / d. 赤と白の長い飴.
Keys: 43→b, 44→d, 45→c, 46→a — identical in all 11 editions.

Block 141–144 (P8, word↔meaning). Stems: 141 七五三, 142 千歳飴,
143 落葉, 144 見頃. Options: a. 木から落ちた葉 / b. 3歳・5歳・7歳の子どものお祝い /
c. 紅葉がいちばん美しい時 / d. 赤と白の長い飴.
Keys: 141→b, 142→d, 143→a, 144→c — identical in all 11 editions.

### Redirect keys 137/138 (adjudicated legitimate, carried from Round 2)

| Ed. | 137 | 138 |
|---|---|---|
| zh-cn | 七五三是11月15日。 | 波奇日从1999年开始。 |
| de | Shichi-Go-San ist der 15. November. | Der Pocky-Tag begann 1999. |
| en | Shichi-Go-San is November 15. | Pocky Day started in 1999. |
| es | Shichi-Go-San es el 15 de noviembre. | El día de Pocky empezó en 1999. |
| fr | Shichi-Go-San, c'est le 15 novembre. | Le jour des Pocky a commencé en 1999. |
| it | Shichi-Go-San è il 15 novembre. | Il giorno dei Pocky è iniziato nel 1999. |
| ko | 시치고상은 11월 15일이다. | 포키데이는 1999년에 시작됐다. |
| nl | Shichi-Go-San is 15 november. | Pocky-dag begon in 1999. |
| pt | O Shichi-Go-San é 15 de novembro. | O dia do Pocky começou em 1999. |
| ru | Сити-Го-Сан — 15 ноября. (see full line above) | День Pocky начался в 1999 году. |
| zh-tw | 七五三是11月15日。 | 波奇日從1999年開始。 |

Keys 139/140 identical to core in all editions (139 `読書週間は10月27日から始まります。`,
140 `紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。`).
Option-order swaps handled correctly (Q87 key B vs Q126 key A, both 目安;
Q103 key B vs Q128 key A, both slogan).

### Arithmetic / numerical keys (recomputed)

Q91 34−26=8 ✓; Q92 34+26=60 ✓; Q93 34+26+24+16=100 ✓; Q13/Q22 six `1`s in
平成11年11月11日 ✓; Q23 four sticks in `1111` ✓; Q54 10 ✓; Q55 13 ✓;
Q56 3 ✓. Model text: 154 non-space characters excluding the `例：` label
(joined SVG lines at x=1451, y 464.4–558.6 total 156 incl. the 2-char label).

### Weekday/date claims (calendar-checked with `date -d`, America/Toronto)

2026-10-24 Sat, 10-25 Sun, 10-26 Mon, 10-27 Tue, 10-28 Wed, 10-29 Thu,
11-07 Sat, 11-09 Mon, 11-11 Wed, 11-13 Fri, 11-15 Sun, 11-19 Thu, 11-21 Sat,
11-22 Sun, 11-23 Mon, 11-29 Sun, 12-04 Fri — all correct as printed.
Issue dates 11-09–11-15 correct.

## §3 Full re-gate (independent, on the final artifacts)

Canonical gates run independently in the Round 3 dir (`run_gates.sh`,
`gates-run.log`, GATES-DONE). All values match Round 2 except the key-42
change itself.

- Freeze baseline: exit 0, 8/8 byte-identical per edition. Freeze diff
  `--strict-cjk`: exit 0 with 0 added CJK for zh-cn/de/en/es/fr/it/nl/pt/ru;
  exit 1 for ko and zh-tw only, adjudicated legitimate — added sets AND
  totals byte-identical to Round 2 (ko 308 distinct / 3464 instances, all
  Hangul; zh-tw 158 distinct / 849 instances). Freeze-JSON R2→R3 comparison
  (`freeze-r2r3-compare.log`): the ONLY string differences in any edition
  are the P8 key-42 added/removed strings (+ DE `kaufen`); P8 CJK totals +4
  in every edition (the 4 added chars 酉の市で); zh-cn self-diff shows only
  the +4 total, no string diffs.
- `p8.py compare`: CLEAN 150/150 for all 11; missing/extra/uncertain empty;
  keydiffs zh-cn `[]`, zh-tw `[138]`, other 9 `[137, 138]` — adjudicated
  legitimate redirects (§2).
- Canonical occlusion audit: 0 flags in all 11 editions (JSONs
  `occlusion-<code>.json`, each `{'flags': []}`; tool selftest runs first
  per SOP).
- Own checks (exit 0; logs/JSONs in gate dir): kinsoku 0/0/0
  (start/end/orphan) ×11; abstracts all PASS (single line + trailing
  newline, 0 ASCII double-quotes, contains 150/A2/B2, equals recorded AFTER
  text, no banned news-framing tail, long common prefix vs BEFORE); counts:
  stems 150, keys 150, raw chips A2 44/B1 74/B2 27, nearest-badge split
  A2 46/B1 75/B2 29, 0 unpaired, per-page distribution
  10/18/18/18/18/18/12/38; P6 bars 480/720/780/1020 at x=315 with labels
  山 34% / 神社 26% / 公園 24% / 町 16% + practice-data label; P7 golden
  phrases 8 × exactly 2 each, verbatim contiguous excerpts; keys-flow end-y
  identical to Round 2 per edition (zh-cn 2514.9, de 2535.0, en 2532.0,
  es 2536.2, fr 2535.0, it 2535.0, ko 2520.4, nl 2537.4, pt 2533.5,
  ru 2524.0, zh-tw 2514.9); pairing badges present at x=975/y=356 in all 10
  fan-outs with correct native-language text (core badge-less by W45 JA
  precedent, not a defect); masthead pixel bands byte-identical to Round 2
  (wordmark ends 265; subtitle 282–319; badge ~338–359; strapline 374–390;
  merged inter-band gaps ≥13); ABSTRACT.txt valid ×11.
- PDFs: all 11 web PDFs ≤ 7 MB, 8 pages, `pdftotext` bytes > 0, web
  extraction byte-identical to print (web bytes / text bytes:
  zh-cn 2,496,765/44,850; de 2,366,010/47,006; en 2,318,038/46,160;
  es 2,346,165/47,786; fr 2,344,131/47,681; it 2,337,476/47,561;
  ko 2,395,657/48,533; nl 2,340,934/46,815; pt 2,348,982/47,582;
  ru 2,254,305/54,276; zh-tw 2,872,569/44,829 — print byte sizes in
  `pdf-round3.log`).
- Sweeps: 0 Hangul outside ko, 0 Cyrillic outside ru; 0 Chinese-prose
  marker hits in the 9 non-Chinese editions; reader-facing sweep clean
  except the known EN false positive (`covered` in
  `74. 200 — The survey covered 200 Shichi-Go-San families`, 2 hits, same
  line); all 3 image credits present in all 11 (P1 maple Poliphilo CC0,
  P3 Hiroshige III 1876 print public domain, P4 stadium Syced CC0, all
  Wikimedia Commons).
- SC scan (zh-tw): 21 s2t-differing chars, 126 instances, 0 residue
  chars/strings; all 8 Traditional conversions present at the Round 2
  locations (incl. key-42 note `在酉の市買熊手`, y=1429.0).
- Core integrity after gates: `core-svg-sha256-before.txt` vs
  `core-svg-sha256-after.txt` IDENTICAL — the freeze-baseline run left core
  SVGs untouched.

## §4 Change isolation — CONFIRMED

Own hash + multiset-diff vs the Round 2 state (retained pre-fix copies in
`ja-fix-round3/`: `before-sha256.txt` 132 files, `baseline-svg-text/`,
`textmd-before/`; log: `change-isolation.log`): exactly 44 files changed,
4 per edition (P8 SVG + print PDF + web PDF + `.text.md`); 88 files
unchanged (all P1–P7 SVGs, all ABSTRACT.txt). SVG text-multiset diff: in
10 editions exactly ONE text changed (the key-42 line); in DE the same one
changed text plus the `kaufen` wrap-continuation element (1329→1330 texts).
`.text.md` diffs: ONLY the key-42 lines (+ DE `kaufen` line). This matches
the fix report's claim exactly.

## §5 Native-language correctness

Every explanation, gloss, note, abstract, and footer is in the reader's
native language; no untranslated strings; no wrong-script residue beyond
adjudicated Japanese keeps (target-language text, P7 excerpts, slogans);
register consistent. Pairing badges visibly carried in all 10 fan-outs
(W45 precedent; badge-less core subtitle NOT re-raised). Reader-facing
sweep clean (§3). Cosmetics O-01–O-05 stay as adjudicated in Round 2
(not re-raised).

## §6 Cards (visual review)

Viewed the shipped post-fix `cards/` PNGs at full frame: P1, P3, and P8 of
every edition, plus P7 zh-tw (34 cards; notes in
`visual-review-round3.md`). No overflow, overlap, missing glyphs/tofu, or
missing image credits. P1 item-8 and P3 item-32 rewrap sites correct in all
11. DE P8 wrap renders tidily. P7 zh-tw renders cleanly with Traditional
forms throughout.

## Residual / new defects

NONE. No new defect and no residual defect was found in this round. The
single Round 2 blocking defect D-KEY-42 is fixed and verified in all 11
editions; the DE wrap is ruled ACCEPTABLE with evidence; the Round 2
whole-tree-grep caveat is completed with classification above. Adjudicated
non-defects were not re-raised (badge-less core subtitle, O-01–O-05).

## Final verdict

ROUND 3 PASS (all 11 shippable)
