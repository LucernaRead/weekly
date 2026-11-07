# COVER-KIT — W43 Weekly Cover, Japanese readers (cover-w43-ja)

## Spec
- SOP 附则五 (weekly cover): 8 pages, 1950×2700, weekly visual system
  (warm ivory #f7f1e2, deep olive accents, serif), COVER mark, no VOL
  number for the cover issue itself.
- Reader language: JAPANESE. All cover-original writing (cover title,
  intro, labels, explanations, P8 heading/intro, footers) is in
  Japanese. Headlines and excerpts stay in their ORIGINAL languages,
  verbatim.
- Masthead: "Lucerna" with NO article (Japanese takes no article —
  confirmed from tables.json: ja entry has `"article": null`,
  `"masthead": "Lucerna"`). Week label: 2026年10月19日～25日.
- VOL note: the cover issue itself carries NO VOL number (P1–P7 have
  zero occurrences of "VOL"; footers read "COVER"). P8 lists each core
  paper's own masthead + VOL, as the task's P8 layout requires — that
  is source metadata about the 12 cores, not a volume number for this
  cover. P8 VOL count verified: 12 (FR VOL.2, all others VOL.1).

## Sources (no re-extraction; used exactly as given)
Shared backfill file:
`hidden_files/cover-backfill/headlines-w43.json` (and `.md`), 12 items
in FIXED order: en, de, fr, es, it, pt, nl, ru, ja, ko, zh-cn, zh-tw.
The builder loads this JSON directly — headlines and excerpts are never
hand-typed, so they are character-for-character identical by
construction. Cross-check: all 12 headlines appear verbatim in the .md
as well; no JSON-vs-.md discrepancy was found. No core SVG was re-read,
and nothing was silently fixed.

| # | Lang | Core dir | Masthead | VOL | Headline (verbatim) |
|---|------|----------|----------|-----|--------------------|
| 01 | en | weekly-report-en-vol1 | The Lucerna | 1 | First Votes, First Games : America's Biggest Week of the Autumn |
| 02 | de | weekly-report-de-vol1 | Die Lucerna | 1 | Eine Stunde geschenkt: Deutschland stellt die Uhren zurück — und elf Länder haben Ferien |
| 03 | fr | weekly-report-vol4 | Le Lucerna | 2 | Présidentielle 2027 : les Français regardent déjà les sondages |
| 04 | es | weekly-report-es-vol1 | La Lucerna | 1 | Este domingo: dormimos una hora más… ¡y se juega el Clásico! |
| 05 | it | weekly-report-it-vol1 | La Lucerna | 1 | Un'ora in più di sonno: domenica torna l'ora solare |
| 06 | pt | weekly-report-pt-vol1 | A Lucerna | 1 | Domingo é dia de decisão: o Brasil volta às urnas |
| 07 | nl | weekly-report-nl-vol1 | De Lucerna | 1 | Een volle week: vakantie, design, dance — en een uur extra slaap |
| 08 | ru | weekly-report-ru-vol1 | Lucerna | 1 | Первый снег — уже на этой неделе! |
| 09 | ja | weekly-report-ja-vol1 | Lucerna | 1 | 土よう日、日本シリーズが始まる！ |
| 10 | ko | weekly-report-ko-vol1 | Lucerna | 1 | 태풍 참피가 오고 있어요 |
| 11 | zh-cn | weekly-report-zhcn-vol1 | Lucerna | 1 | 双11到了「付尾款」的这一周 |
| 12 | zh-tw | weekly-report-zhtw-vol1 | Lucerna | 1 | 強颱薔琵壓境！週五、週六風雨最大 |

Excerpts: each item's P1 article-opening sentences, verbatim from the
same JSON (≤4 sentences each). Full texts are in the JSON, not
re-typed here.

## Layout (8 pages)
- P1: masthead "Lucerna" + olive COVER badge + week label
  (2026年10月19日～25日 · 日本語読者のための週間カバー) + cover title
  「今週の十二の見出し」 + 2-sentence generic framing intro (no new
  facts) + 12 numbered headline teasers in fixed order (left column
  01–06, right column 07–12; Japanese source-language label + verbatim
  headline).
- P2–P7: 2 items per page in fixed order (P2 EN/DE, P3 FR/ES, P4 IT/PT,
  P5 NL/RU, P6 JA/KO, P7 zh-cn/zh-tw). Each item: Japanese
  source-language tag + core masthead, verbatim headline (serif bold),
  verbatim excerpt, then a 「解説」 box with a 1–2 sentence explanation
  in Japanese. Every explanation claim traces to that item's headline +
  excerpt ONLY; the only gloss is zh-cn 「付尾款」 rendered as
  「残りの代金を支払うこと」 (a gloss of the headline's own words, no
  new fact). The two blocks are vertically centred in the content area
  (final block ends ~y=1930–2020).
- P8: 「今週の十二の正刊——一覧」: per core, masthead + VOL + verbatim
  headline, in fixed order, with a Japanese language label prefix.
- Fonts per shipped-core convention (tables.json faces): Latin/Cyrillic
  items in Noto Serif/Sans CJK SC; Japanese in JP; Korean in KR;
  Simplified Chinese in SC; Traditional Chinese in TC; all
  reader-language (Japanese) furniture in JP. This is what lets
  webpdf.py subset and embed the right faces.

## Build
- Build dir: `hidden_files/cover-w43-ja-build/` — `build.py`
  (self-contained; layout patterns copied from the sibling cover-w43-en
  build, never imported) + `svglib_ja_core.py` (the JA core's PATCHED
  svglib, copied verbatim — md5 d73e23b365676c3618d7e060b835eb4d,
  matching the canonical file; never edited, never imported) + `svg/` +
  `png/` (CairoSVG eyeball renders).
- Wrap: `build.py`'s `wrap()` copies the JA core svglib's kinsoku
  mechanism (NO_START oidashi + seam repair with SEAM_SLACK=28 that
  RE-MEASURES final line widths), adapted only in that the width
  function is parameterized per font family (the core measures JP face
  only; this cover sets 12 source languages in their shipped-core
  faces), and the NO_START set is extended with the ASCII closer set
  per tools/README rule 19 (KO×JA precedent). The builder additionally
  asserts on every wrapped line: width ≤ max_w + SEAM_SLACK, any line
  over max_w is a single unbreakable token, and no line after the first
  starts with a NO_START closer — all asserts passed on the first build.
- Edition dir: `files/cover-w43-ja/` — `svg/` (same 8 SVGs) +
  `cover-w43-ja.pdf` + this KIT.
- No git touched. No subagents spawned. Pre-flight: the build dir did
  not exist, so no other worker was active on this edition.

## Verification outputs
- Occlusion audit: `tools/venv/bin/python tools/occlusion_audit.py
  hidden_files/cover-w43-ja-build/svg` → selftest OK (all 6 planted
  classes fired exactly once; clean controls silent), **0 flags**.
- Visual eyeball: all 8 pages rendered with CairoSVG at 975 px wide
  and inspected — no overflow, no cut-off text, no tofu/missing
  glyphs (Latin, Cyrillic, Japanese, Korean, Simplified + Traditional
  Chinese all render), no overlapping elements.
- P1 VOL check: 0 occurrences of "VOL" on P1 (and on P2–P7); COVER
  badge present on P1.
- Final PDF built ONLY with:
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>`
  → 646,598 bytes (< 7 MB target), 8 pages, 9,910 text bytes
  (pdftotext non-empty).
- Headline check: all 12 headlines extract from the PDF
  (whitespace-normalized comparison: 12/12). Excerpts: 12/12 on the
  same comparison. SVG-side verbatim check (text nodes concatenated in
  paint order, whitespace-stripped to allow for wrap line splits):
  12/12 headlines + 12/12 excerpts present on their item pages.
- PDF SHA-256: 27f868caf51eaed047de4192de88f6dd99db9776526f50fe84e7e268d12f19bf

## Issues found + fixed
1. None in content or layout: the first build passed all width/kinsoku
   asserts, the audit came back clean on the first run, and all 8
   eyeball renders were clean — no rebuild was needed.
2. Method note (not a defect): a naive full-string verbatim check of
   excerpts against the raw SVG files "missed" (wrapping splits text
   across <text> nodes, so the contiguous string is not in the file).
   Resolved by concatenating text nodes in paint order and comparing
   whitespace-stripped — 12/12 headlines + 12/12 excerpts confirmed.
   The builder itself loads the JSON directly, so verbatimness holds
   by construction regardless.
3. Process note (not a defect): webpdf.py took ~4.5 minutes (10 font
   subsets: JP/KR/SC/TC serif + bold, JP sans) and backgrounded
   mid-run; it completed with exit 0 and the expected output line.
4. Typographic note (not a defect): the P1 Japanese intro wraps
   mid-word (言葉 split across lines) — normal Japanese per-character
   wrapping, kinsoku-clean (no line starts with a closer).

## Fixes 2026-10-28 (independent proofread, exactly 2 problems — both fixed, nothing else changed)

Build source changed only: `hidden_files/cover-w43-ja-build/build.py`
(`EXPL["de"]` sentence 1 + kinsoku handling in `wrap()`). No headline,
excerpt, or other explanation was touched. No git touched. No Discord
post. No PDF dumped into chat. Storm names untouched by construction
(only P2/P4 SVGs changed — see §5 below): ko item チャンピー and
zh-tw item 薔琵 extract from the new PDF exactly as before.

### Fix 1 — P4, PT item explanation: kinsoku violation, small-kana line start (rewrap ONLY, no wording change)
- Problem: the explanation wrapped 「フラヴィオ」 so line 1 ended
  「…フラヴ」 and line 2 started with small kana
  「ィオ・ボルソナロ氏の2人だけである。」 Small kana (sutegana)
  must not start a line under Japanese kinsoku (JIS X 4051).
- Fix (rewrap only): ィ pulled back to line 1. New lines, full text
  otherwise unchanged:
  - Line 1: 「10月25日（日）8時から17時（ブラジリア時間）に、ブラジル人は大統領選挙の決選投票に向かう。候補はルラ氏とフラヴィ」
  - Line 2: 「オ・ボルソナロ氏の2人だけである。」
  - Full PT explanation (unchanged wording):
    「10月25日（日）8時から17時（ブラジリア時間）に、ブラジル人は大統領選挙の決選投票に向かう。候補はルラ氏とフラヴィオ・ボルソナロ氏の2人だけである。」
- Builder change: `NO_START` extended with small kana
  「ぁぃぅぇぉっゃゅょァィゥェォッャュョ」, handled by a dedicated
  pull-UP pass in `wrap()` (not the generic closer oidashi, which pulls
  the previous line's last char down and would have produced
  「…フラ」 / 「ヴィオ…」 instead of the required rewrap). The
  pulled-up P4 line 1 measures 1784.2 px against max_w 1764 px — over
  by 20.2 px, inside SEAM_SLACK 28 (cap 1792 px), so the builder's
  final-width assert passes; line 2 measures 529.5 px. The final
  kinsoku assert now covers sutegana via the extended `NO_START`.
- Full-edition scan (all 8 pages, all SVG text nodes): line-initial
  small kana 0 violations; line-initial long-vowel/iteration marks
  (ー, ゝ, ゞ, ヽ, ヾ, 々) 0 violations; line-initial closers 0
  violations. No other sutegana instance existed pre-fix (the P4 ィ
  was the only one), so no other rewrap was needed and none was made.
  If a future rewrap alone could not fix such an instance, it would
  be reported, not word-changed — not triggered here.

### Fix 2 — P2, DE item explanation sentence 1: wrong night
- OLD (exact): 「日曜日の夜、ドイツは時計を1時間戻して夏時間を終える。」
- NEW (exact): 「土曜から日曜にかけての夜、ドイツは時計を1時間戻して夏時間を終える。」
- Reason: the DE excerpt says the change happens "In der Nacht von
  Samstag auf Sonntag" — the night from Saturday to Sunday.
  「日曜日の夜」 reads as Sunday night, a day late.
- Second sentence UNCHANGED: 「見出しによれば、11か国が休暇中である。」
  Full new DE explanation:
  「土曜から日曜にかけての夜、ドイツは時計を1時間戻して夏時間を終える。見出しによれば、11か国が休暇中である。」
  (single wrapped line, 1683.1 px ≤ 1764 px, so P2 layout/coordinates
  are unchanged — only that one text node changed.)

### Re-verification (supersedes the PDF line in "Verification outputs" above)
1. P4 SVG line inspection + PDF text: line 1 ends 「…フラヴィ」,
   line 2 begins 「オ・ボルソナロ氏の2人だけである。」; no PDF text
   line starts with ィ or any other small kana. Full-edition
   small-kana line-start scan: 0 violations. Kinsoku scan otherwise:
   0 violations (closers 0, iteration marks 0).
2. New DE sentence present in the P2 SVG and in the PDF text (both raw
   and whitespace-stripped checks); old DE sentence absent from all 8
   SVGs and from the PDF text (both raw and whitespace-stripped
   checks).
3. Occlusion audit re-run on the edition SVGs:
   `tools/venv/bin/python tools/occlusion_audit.py files/cover-w43-ja/svg`
   → selftest OK (all 6 planted classes fired exactly once; clean
   controls silent), **0 flags, exit 0**.
4. PDF rebuilt ONLY with:
   `tools/venv/bin/python tools/webpdf.py files/cover-w43-ja/svg files/cover-w43-ja/cover-w43-ja.pdf`
   → 8 pages, **646,929 bytes** (< 7 MB), pdftotext **9,931 bytes**
   (non-empty), all 12 headlines extract (whitespace-normalized:
   12/12). Previous PDF was 646,598 bytes / 9,910 pdftotext bytes.
5. Only P2 and P4 SVGs differ from the pre-fix set. P1, P3, P5, P6, P7,
   P8 are byte-identical (hashes unchanged). P2 differs in exactly
   one text node (the DE explanation, same coordinates); P4 differs
   in exactly two text nodes (the PT explanation lines, same
   coordinates). New edition SVG SHA-256:
   P2 dfe48ebfd976895dce3131916b3fe633d00db5f45c2c1027bfb4e993049a068b,
   P4 e4612cb8af929b5e85aa462de129d8206776a51cbac8570682b436e33419fe27.
6. New PDF SHA-256: dc1bbf0dc05322912536dab990c71a31347605c13b034b353d3f10b1e5a9e94e
   (previous: 27f868caf51eaed047de4192de88f6dd99db9776526f50fe84e7e268d12f19bf).

### Fix 3 — P2, DE item explanation sentence 2: wrong unit (countries instead of German federal states)
- OLD (exact): 「見出しによれば、11か国が休暇中である。」
- NEW (exact): 「見出しによれば、11の州が休暇中である。」
- Reason: the DE headline says "elf Länder haben Ferien", but the DE
  core's own P1 states "Elf Bundesländer haben in dieser Woche
  gleichzeitig Ferien" — Länder/Bundesländer are German federal
  states, not countries. Same mistranslation previously fixed in the
  W43 English cover ("eleven countries" → "eleven German states").
- Sentence 1 UNCHANGED:
  「土曜から日曜にかけての夜、ドイツは時計を1時間戻して夏時間を終える。」
  Full new DE explanation:
  「土曜から日曜にかけての夜、ドイツは時計を1時間戻して夏時間を終える。見出しによれば、11の州が休暇中である。」
  (single wrapped line, same node coordinates x=93 y=1976.5 as before —
  same character count, so P2 layout/coordinates are unchanged.)
- Builder change: one string in `hidden_files/cover-w43-ja-build/build.py`
  (`EXPL["de"]`), sentence 2 only. No headline, excerpt, or other
  explanation touched. Storm names untouched (チャンピー, 薔琵 as-is).
  First-round fixes untouched: P4 kinsoku rewrap and P2 sentence 1
  night fix both verified intact below.

### Re-verification (Fix 3, supersedes the PDF line in "Re-verification" above)
1. Old sentence 「見出しによれば、11か国が休暇中である。」 occurs
   0 times in all 8 edition SVGs and 0 times in the PDF text layer
   (raw and whitespace-stripped checks). New sentence
   「見出しによれば、11の州が休暇中である。」 present in the P2 SVG
   (single node, x=93 y=1976.5) and in the PDF text (raw and
   whitespace-stripped checks).
2. Kinsoku scan of all SVG text lines (all 8 pages): line-start
   small kana 0, line-start closers 0, line-end openers 0,
   line-start long-vowel/iteration marks (ー, ゝ, ゞ, ヽ, ヾ, 々) 0.
   P4 rewrap intact: line 1 still ends 「…フラヴィ」 and line 2
   still begins 「オ・ボルソナロ氏の2人だけである。」.
3. Occlusion audit re-run on the edition SVGs:
   `tools/venv/bin/python tools/occlusion_audit.py files/cover-w43-ja/svg`
   → selftest OK (all 6 planted classes fired exactly once; clean
   controls silent), **0 flags, exit 0**.
4. PDF rebuilt ONLY with:
   `tools/venv/bin/python tools/webpdf.py files/cover-w43-ja/svg files/cover-w43-ja/cover-w43-ja.pdf`
   → **8 pages, 647,532 bytes** (< 7 MB), pdftotext **9,931 bytes**
   (non-empty; same byte count as before because OLD and NEW have
   the same character count), all 12 headlines extract
   (whitespace-normalized: 12/12).
5. Only the P2 SVG differs in content from the pre-fix set. P1, P3,
   P4, P5, P6, P7, P8 are byte-identical (hashes unchanged). New
   edition SVG SHA-256:
   P2 eb1db94a1868317983113e95ff450a7669977856ff172fd146edd3d60a28daa7
   (pre-fix: dfe48ebfd976895dce3131916b3fe633d00db5f45c2c1027bfb4e993049a068b).
6. New PDF SHA-256: 1f671155d42ed9152d692029ba2c5436c369e5c425b42e287ecc87adbf3a76e9
   (previous: dc1bbf0dc05322912536dab990c71a31347605c13b034b353d3f10b1e5a9e94e).
