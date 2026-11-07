# COVER-KIT — W43 Weekly Cover, reader language KOREAN (ko)

## Spec
- SOP 附则五 (weekly cover): 8 pages, 1950×2700, weekly visual system
  (warm ivory #f7f1e2, deep olive #3e4c2a accents, serif).
- Reader language: Korean. All cover-original writing (title, intro,
  explanations, labels) is in Korean, 해요체 (polite informal style).
  Headlines and excerpts stay in their ORIGINAL languages, verbatim.
- Masthead: `Lucerna` with NO article (tables.json `languages.ko`:
  `article: null`, `masthead: "Lucerna"`). NO VOL number anywhere on
  P1–P7; the cover is marked COVER (olive COVER badge under the
  masthead on P1, plus `Lucerna · COVER` footers on every page).
- Week label: 2026년 10월 19일~25일 (W43, October 19–25, 2026).

## Sources (the 12 items, FIXED order)
Taken verbatim from the shared source
`hidden_files/cover-backfill/headlines-w43.json` (and .md).
`build.py` loads that JSON at build time, so headlines/excerpts are
inserted programmatically, never re-typed — no transcription drift is
possible by construction. No discrepancy between the JSON and the
material used was encountered; no re-extraction from the cores was
performed (per the task brief).

| # | Lang | Core dir | Masthead | VOL (P8 only) | Headline (verbatim) |
|---|------|----------|----------|---------------|---------------------|
| 1 | en | weekly-report-en-vol1 | The Lucerna | VOL.1 | First Votes, First Games : America's Biggest Week of the Autumn |
| 2 | de | weekly-report-de-vol1 | Die Lucerna | VOL.1 | Eine Stunde geschenkt: Deutschland stellt die Uhren zurück — und elf Länder haben Ferien |
| 3 | fr | weekly-report-vol4 | Le Lucerna | VOL.2 | Présidentielle 2027 : les Français regardent déjà les sondages |
| 4 | es | weekly-report-es-vol1 | La Lucerna | VOL.1 | Este domingo: dormimos una hora más… ¡y se juega el Clásico! |
| 5 | it | weekly-report-it-vol1 | La Lucerna | VOL.1 | Un'ora in più di sonno: domenica torna l'ora solare |
| 6 | pt | weekly-report-pt-vol1 | A Lucerna | VOL.1 | Domingo é dia de decisão: o Brasil volta às urnas |
| 7 | nl | weekly-report-nl-vol1 | De Lucerna | VOL.1 | Een volle week: vakantie, design, dance — en een uur extra slaap |
| 8 | ru | weekly-report-ru-vol1 | Lucerna | VOL.1 | Первый снег — уже на этой неделе! |
| 9 | ja | weekly-report-ja-vol1 | Lucerna | VOL.1 | 土よう日、日本シリーズが始まる！ |
| 10 | ko | weekly-report-ko-vol1 | Lucerna | VOL.1 | 태풍 참피가 오고 있어요 |
| 11 | zh-cn | weekly-report-zhcn-vol1 | Lucerna | VOL.1 | 双11到了「付尾款」的这一周 |
| 12 | zh-tw | weekly-report-zhtw-vol1 | Lucerna | VOL.1 | 強颱薔琵壓境！週五、週六風雨最大 |

Excerpts are the same JSON `excerpt` fields (≤4 sentences each), used
verbatim on P2–P7. W43 VOLs on P8: FR VOL.2, all others VOL.1.

## Layout (8 pages)
- P1: masthead `Lucerna` + olive COVER badge + week label
  (2026년 10월 19일~25일) + cover title `열두 개의 언어로 읽는 한 주`
  + 2-sentence generic framing intro (no new facts) + 12 headline
  teasers in fixed order (source-language code + Korean language name +
  verbatim headline).
- P2: EN, DE. P3: FR, ES. P4: IT, PT. P5: NL, RU. P6: JA, KO.
  P7: zh-cn, zh-tw. Each item: source-language tag, verbatim headline,
  verbatim excerpt, then a 1–2 sentence explanation in Korean
  (해요체) stating what happened + why it matters. Every explanation
  claim is traceable to that item's headline + excerpt only; no facts
  beyond the source article. Terms quoted in their original form
  (e.g. 「开门红」, 「共伴效應」) rather than transliterated.
- P8: the week's 12 core papers at a glance, fixed order: per core,
  masthead + VOL + verbatim headline (same extracted material only,
  nothing invented).

## Build
- Build dir: `hidden_files/cover-w43-ko-build/` — `build.py`,
  `svglib.py` (COPIED from the KO core build dir
  `hidden_files/weekly-report-ko-build/`; no core content module was
  imported), `orphan_scan.py`, `svg/`, `png/` (eyeball renders).
- Fonts: Noto Serif/Sans CJK (KR face for measurement; SC face for
  zh-cn, TC for zh-tw, JP for ja headlines/excerpts so each script
  renders in its own variant).
- PDF built ONLY with:
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>`
  (text-layer web PDF).

## Verification outputs
- Occlusion audit:
  `tools/venv/bin/python tools/occlusion_audit.py svg`
  → selftest OK (all 6 planted classes fired), `svg: 0 flags`, exit 0.
- Orphan scan (`orphan_scan.py`, REVISED 2026-10-28 — see "Issues
  found + fixed" #5): Korean prose = the 12 Korean explanations.
  A Korean prose paragraph fails iff its final line, after stripping
  trailing punctuation, holds exactly ONE whitespace token (1-token
  rule). Headlines and source-language excerpts are reported
  separately, never counted as Korean-prose flags (headline
  single-word wraps are headline wraps; CJK excerpts have no
  whitespace tokens, so a token count is meaningless for them).
  → `KOREAN PROSE ORPHAN FLAGS (1-token rule): 0`, exit 0.
  The pre-2026-10-28 ≤3-character rule is retired: it wrongly passed
  the 4-character 1-token finals `시작해요.` and `만이에요.`.
- Eyeball: all 8 pages rendered to PNG (CairoSVG) and visually
  inspected — no overflow, no cut-off text, no overlapping elements,
  no tofu/missing glyphs; all 12 scripts render (Latin, Cyrillic,
  Japanese, Korean, Simplified + Traditional Chinese).
- PDF text layer: `pdftotext` returns 9,880 bytes (non-empty).
  Whitespace-insensitive check: ALL 12 headlines AND ALL 12 excerpts
  extract from the PDF. (A naive whitespace-normalised check initially
  flagged the zh-tw excerpt only because a CJK line break becomes a
  space in pdftotext output; the whitespace-stripped check passes for
  all 12 excerpts.)
- VOL check: `VOL` occurs exactly 12 times in the PDF text, all on P8;
  SVGs p1–p7 contain zero `VOL` strings.
- File: `cover-w43-ko.pdf`, 662,649 bytes (< 7 MB target), 8 pages
  (rebuild after the 2026-10-28 orphan fix below; text bytes 9,893 —
  unchanged character count, only line breaks moved).
- PDF text-layer re-verification after the final rebuild: all 12
  headlines + all 12 excerpts extract (whitespace-insensitive);
  VOL count 12, P8 only.

## Typhoon-name alert check (coordinator verification, 2026-10-28)
Grep of all 8 SVGs AND of the final PDF text:
- `Chanpi`, `Changpi`, `Fung-wong`, Latin `Champi`, Latin `Jangmi`,
  Korean `장미`: ZERO occurrences anywhere.
- KO-item explanation names the storm ONLY as Korean `참피`
  (Champi): `제30호 태풍 참피가 북상하고 있어요. “참피”는 라오스가 낸
  꽃 이름이고, 기상청은 21일 아침에 아주 강한 태풍이라고 했어요.`
- ZH-TW-item explanation names the storm with the native characters
  `薔琵` and no Latin name (the explicitly acceptable alternative):
  `강력한 태풍 「薔琵」가 대만 동쪽 해상을 향해 다가오고 있어요. …`
  (the name comes from the zh-tw excerpt itself, so it introduces no
  new fact). The first draft of this explanation named no storm at
  all; it was revised to name `薔琵` so the explanation complies with
  the alert's naming requirement, then fully re-verified (occlusion
  0 flags, orphan 0 flags, P7 re-eyeballed clean, PDF rebuilt).
- Verbatim headlines/excerpts were NOT altered by this fix.

## Issues found + fixed
1. EN excerpt orphan (real defect): at 46 pt the EN excerpt's final
   line was the lone word `too.` — caught by the orphan scan. Fixed
   by rendering the EN excerpt only at 45 pt, which pulls the full
   clause (`— and in Alaska, Arkansas, Connecticut and Colorado too.`)
   onto the final line. Excerpt text itself untouched (verbatim).
2. First draft P2–P7 ended at y≈1300–1400 (pages half empty). Fixed by
   enlarging body type (headline 58 pt, excerpt/explanation 46 pt,
   1.7 line height) and spreading the two items down the page;
   final content ends at y≈1760–2080, inside the footer rule.
3. No other defects: occlusion audit clean on first run; no
   discrepancies between the JSON source and the built material.
4. Typhoon-name alert (see section above): ZH-TW explanation revised
   to name the storm as native `薔琵` (no Latin name); KO explanation
   already named only `참피`. No wrong names were ever present
   (grep: zero `Chanpi` / `Changpi` / `Fung-wong` / Latin `Champi` /
   Latin `Jangmi` / `장미` in SVGs or PDF text).
5. Korean orphan final lines, 2026-10-28 (layout only, wording
   untouched): P5 NL explanation and P6 JA explanation each ended
   on a 1-token final line at 46 pt — `시작해요.` and `만이에요.`
   respectively. The old ≤3-character orphan rule had passed both
   (both finals are 4 characters stripped) and is therefore retired
   for Korean prose. Fix (in `build.py`, so the build stays
   reproducible — same pattern as the earlier EN-excerpt 45 pt fix):
   NL + JA explanations render at 45 pt only; all other explanations
   stay at 46 pt; wrap width unchanged (1650). Each reflows 3 → 2
   lines; P5 end y 1918.4, P6 end y 1680.8 (both inside the footer
   rule; build asserts pass). `orphan_scan.py` rewritten to the
   1-token rule for all 12 Korean explanations (scanned at their
   built sizes) and re-run: `KOREAN PROSE ORPHAN FLAGS: 0`, exit 0.
   New final lines (verbatim from the rebuilt SVGs + PDF text):
   NL — `북부 지역은 지난주에 쉬었고 이번 주 월요일부터 학교가 다시
   시작해요.` (10 tokens); JA — `요코하마 DeNA 베이스타즈와 후쿠오카
   소프트뱅크 호크스의 대결은 2년 만이에요.` (9 tokens).
   No-wording proof: joining each page's SVG text with spaces gives
   byte-identical wording on all 8 pages vs the pre-fix SVGs, and
   each fixed paragraph's lines joined with spaces equal the original
   explanation string exactly. Re-verification after rebuild:
   occlusion audit `files/cover-w43-ko/svg: 0 flags`, exit 0
   (selftest OK); PDF rebuilt ONLY via
   `tools/venv/bin/python tools/webpdf.py` → 662,649 bytes, 8 pages,
   pdftotext 9,893 bytes, all 12 headlines + all 12 excerpts extract
   (whitespace-insensitive), VOL count 12 (P8 only). Storm-name
   re-grep on the new SVGs: zero `Chanpi` / `Changpi` /
   `Fung-wong` / Latin `Champi` / Latin `Jangmi` / `장미`;
   `참피` only for ko, `薔琵` only for zh-tw. No headline, excerpt,
   or other explanation touched (P1–P4, P7, P8 SVGs byte-identical
   to pre-fix).
6. P2 DE explanation, sentence 2 — wrong entity, second fix round,
   2026-10-28 (wording fix, sentence 1 untouched): the DE headline's
   "elf Länder" was rendered as countries, but the DE core's own
   continuation ("Elf Bundesländer haben in dieser Woche gleichzeitig
   Herbstferien") disambiguates it as eleven German federal states
   — the same mistranslation class already fixed in the W43 English
   cover to "eleven German states". Fix in `build.py` EXPL["de"]
   only (build stays reproducible):
   OLD: "헤드라인은 열한 나라가 휴가 중이라는 소식도 함께 전해요."
   NEW: "헤드라인은 독일의 열한 개 주가 휴가 중이라는 소식도 함께 전해요."
   Sentence 1 ("독일에서는 일요일 새벽에 서머타임이 끝나고 시계가
   3시에서 2시로 한 시간 뒤로 돌아가요.") verified unchanged (joined
   P2 SVG text contains sentence 1 + NEW exactly once). The reworded
   DE explanation still wraps to 2 lines at 46 pt; its final line
   (y=1801.5) and the P2 page end (y=1919.7) are inside the footer
   rule; the 45 pt NL/JA gating is untouched
   (`expl_size = 45 if lang in ("nl", "ja") else 46`).
   TOOLCHAIN NOTE: rebuilding with `tools/venv/bin/python` (Pillow
   13.0.0) does NOT reproduce the verified first-round state — it
   measures the JA explanation's 45 pt first line at 1652.8 pt
   (> 1650 wrap width), reflowing JA to 3 lines with a 1-token final
   "만이에요." and flagging the orphan scan. System `python3`
   (Pillow 10.2.0) measures the same line at 1638.2 pt and reproduces
   the verified 2-line JA exactly. This fix was therefore built and
   orphan-scanned with system `python3`; `webpdf.py` and
   `occlusion_audit.py` were run with `tools/venv/bin/python` as
   specified. Future rebuilds of this cover must use system `python3`
   for `build.py`/`orphan_scan.py` until the Pillow drift is resolved.
   Re-verification after rebuild:
   - OLD sentence: 0 occurrences in all 8 edition SVGs and in the
     PDF text layer; NEW sentence: present in the P2 SVG (1×) and
     in the PDF text (1×, joined-space check).
   - Orphan scan (1-token rule, retired ≤3-character rule NOT used):
     `orphan_scan.py` (system python3) → `KOREAN PROSE ORPHAN FLAGS
     (1-token rule): 0`, exit 0 — 12 explanations at built sizes
     (NL/JA 45 pt, others 46 pt); supplementary same-rule scan of
     P1 title (66 pt) / intro (38 pt) / footnote (30 pt) and P8
     title (60 pt) / intro (36 pt) → 0 flags. Reflowed P2 DE final
     line: "돌아가요. 헤드라인은 독일의 열한 개 주가 휴가 중이라는
     소식도 함께 전해요." (11 tokens).
   - Occlusion audit (`tools/venv/bin/python
     tools/occlusion_audit.py files/cover-w43-ko/svg`): selftest OK,
     `svg: 0 flags`, exit 0.
   - PDF rebuilt ONLY via `tools/venv/bin/python tools/webpdf.py
     files/cover-w43-ko/svg files/cover-w43-ko/cover-w43-ko.pdf` →
     662,651 bytes (< 7 MB), 8 pages, pdftotext 9,904 bytes
     (non-empty); all 12 headlines AND all 12 excerpts extract
     (whitespace-insensitive); VOL count 12 (P8 only).
   - Only-content-difference check vs the pre-fix snapshot: P2 SVG
     differs; P1, P3–P8 SVGs byte-identical (P5 NL and P6 JA 45 pt
     reflows exactly as before). No headline, excerpt, or other
     explanation touched; storm names re-grepped in PDF text: zero
     `Chanpi` / `Changpi` / `Fung-wong` / Latin `Champi` /
     Latin `Jangmi` / `장미`; `참피` only for ko, `薔琵` only for
     zh-tw. New PDF SHA-256:
     5b4ec13c8ed5056ca745ddec3d41fd49f42ec1f45f9dd4b16252f1213da8ea2b
     (pre-fix: e90c42c2c5a2d9314217f2c73362f7b4d1c7f507ed946ed4b5df775ac5a7db51,
     662,649 bytes, 9,893 pdftotext bytes).
