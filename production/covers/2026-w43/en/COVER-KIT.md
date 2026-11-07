# COVER-KIT — W43 Weekly Cover, English readers (cover-w43-en)

## Spec
- SOP 附则五 (weekly cover): 8 pages, 1950×2700, weekly visual system
  (warm ivory #f7f1e2, deep olive accents, serif), COVER mark, no VOL
  number for the cover issue itself.
- Reader language: ENGLISH. All cover-original writing (cover title,
  intro, explanations, P8 intro) is in English. Headlines and excerpts
  stay in their ORIGINAL languages, verbatim.
- Masthead: "The Lucerna" (English article convention). Week label:
  October 19–25, 2026.
- VOL note: the cover issue itself carries NO VOL number (P1 has zero
  occurrences of "VOL"; footers read "COVER"). P8 lists each core
  paper's own masthead + VOL, as the task's P8 layout requires — that
  is source metadata about the 12 cores, not a volume number for this
  cover.

## Sources (no re-extraction; used exactly as given)
Shared backfill file:
`hidden_files/cover-backfill/headlines-w43.json` (and `.md`), 12 items
in FIXED order: en, de, fr, es, it, pt, nl, ru, ja, ko, zh-cn, zh-tw.
The builder loads this JSON directly — headlines and excerpts are never
hand-typed, so they are character-for-character identical by
construction. No discrepancy between the JSON and the .md was found;
no core SVG was re-read, and nothing was silently fixed.

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
- P1: masthead "The Lucerna" + olive COVER badge + week label +
  cover title "The Week in Twelve Headlines" + 2-sentence generic
  framing intro (no new facts) + 12 numbered headline teasers in
  fixed order (left column 01–06, right column 07–12; source-language
  label + verbatim headline).
- P2–P7: 2 items per page in fixed order (P2 EN/DE, P3 FR/ES, P4 IT/PT,
  P5 NL/RU, P6 JA/KO, P7 zh-cn/zh-tw). Each item: source-language tag
  + core masthead, verbatim headline (serif bold), verbatim excerpt,
  then an "IN ENGLISH" box with a 1–2 sentence explanation. Every
  explanation claim traces to that item's headline + excerpt ONLY;
  the only gloss is zh-cn 「付尾款」 rendered as "paying final
  balances" (a gloss of the headline's own words, no new fact).
- P8: "The Week's Twelve Core Papers — At a Glance": per core,
  masthead + VOL + verbatim headline, in fixed order.
- Fonts per shipped-core convention (tables.json faces): Latin/Cyrillic
  items in Noto Serif/Sans CJK SC; Japanese in JP; Korean in KR;
  Simplified Chinese in SC; Traditional Chinese in TC. This is what
  lets webpdf.py subset and embed the right faces.

## Build
- Build dir: `hidden_files/cover-w43-en-build/` — `build.py` (self-
  contained; svglib/bslib4 patterns COPIED, never imported, per the
  no-import rule for core build dirs) + `svg/` + `png/` (CairoSVG
  eyeball renders).
- Edition dir: `files/cover-w43-en/` — `svg/` (same 8 SVGs) +
  `cover-w43-en.pdf` + this KIT.
- No git touched. No subagents spawned. Pre-flight: the build dir did
  not exist, so no other worker was active on this edition.

## Verification outputs
- Occlusion audit: `tools/venv/bin/python tools/occlusion_audit.py svg`
  → selftest OK, **0 flags** (final run after the type-size bump;
  the pre-bump run was also 0 flags).
- Visual eyeball: all 8 pages rendered with CairoSVG at 975 px wide
  and inspected — no overflow, no cut-off text, no tofu/missing
  glyphs (Latin, Cyrillic, Japanese, Korean, Simplified + Traditional
  Chinese all render), no overlapping elements.
- Final PDF built ONLY with:
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>`
  → 404,985 bytes (< 7 MB target), 8 pages, 9,197 text bytes
  (pdftotext non-empty).
- Headline check: all 12 headlines extract from the PDF (whitespace-
  normalized comparison: 12/12). Excerpts: 12/12 on a whitespace-
  stripped comparison; the 4 CJK excerpts only "miss" on the naive
  comparison because pdftotext inserts a space at CJK line breaks
  where the original has none — the characters themselves are all
  present in order (verified).
- PDF SHA-256: e3a6f339e387c5bbc4cf539e91f14f2800cc515a7759d9ac801bd9c3837b174a

## Issues found + fixed
1. First build left P2–P7 half-empty (content ended ~y=1200 of 2540).
   Fixed: headline 48→60 pt, excerpt 32→37 pt, explanation 29→32 pt,
   and the two blocks are vertically centred in the content area
   (final block ends ~y=1940–2040). Re-audited clean after the change.
2. CairoSVG flag mistake on first render attempt (`-w` is not a flag;
   `--output-width` is). No SVG change; renders regenerated.
3. P1 teaser order ambiguity (2-column layout): resolved by numbering
   teasers 01–12 in fixed order, left column 01–06, right 07–12.
4. P7 zh-tw English explanation named the wrong typhoon (2026-10-28
   fix): "Fung-wong" → "Jangmi". See "Fix 2026-10-28" below.

## Fix 2026-10-28 — P7 zh-tw English explanation, typhoon name only
- OLD (wrong): "Strong Typhoon Fung-wong is approaching the seas east
  of Taiwan, with the heaviest wind and rain expected on Friday"
- NEW (correct): "Strong Typhoon Jangmi is approaching the seas east
  of Taiwan, with the heaviest wind and rain expected on Friday"
- Authority: the zh-tw core's own P1 SVG
  (`files/weekly-report-zhtw-vol1/svg/p1-front.svg`) names the storm
  "Jangmi" (1 occurrence) and contains zero "Fung-wong". Fung-wong is
  a different typhoon name and was wrong here.
- Scope: EXACTLY this one string. Changed in the build source
  (`hidden_files/cover-w43-en-build/build.py`, EXPL["zh-tw"], line
  160), all 8 SVGs regenerated, copied to the edition dir. The
  explanation's second line ("and Saturday, and a combined effect
  with the northeast monsoon set to make the rain heavier and
  longer-lasting.") is unchanged. No headline, excerpt, or other
  explanation was touched; the verbatim zh-tw headline/excerpt
  (Traditional characters) are unchanged.
- Nothing-else-changed proof: regenerated build SVGs match the
  pre-fix set on 7/8 pages (SHA-256 identical); only p7-items.svg
  differs, and old→new is identical except "Fung-wong"→"Jangmi"
  (byte length 3902→3899, the 3-character name shortening). Zero
  "Fung-wong" remains in build.py, the build SVGs, or the edition SVGs.
- Re-verification (same procedure as the original build):
  - Occlusion audit: `tools/venv/bin/python tools/occlusion_audit.py
    files/cover-w43-en/svg` → selftest OK, **0 flags**.
  - Final PDF rebuilt ONLY with `tools/venv/bin/python
    tools/webpdf.py files/cover-w43-en/svg
    files/cover-w43-en/cover-w43-en.pdf` → **404,984 bytes**
    (< 7 MB), **8 pages**, **9,194 text bytes** (pdftotext
    non-empty; old PDF was 404,985 bytes / 9,197 text bytes — the
    −1 PDF byte / −3 text bytes is exactly the name shortening).
  - pdftotext: "Jangmi" 1 occurrence, "Fung-wong" 0; new first line
    present, second line unchanged; all 12 headlines extract
    (12/12); zh-tw headline verbatim.
  - New PDF SHA-256:
    0737bc927c088fd435a9c1da0eb87f962e6261dd5b3dddea92878fc91904c996
    (supersedes the pre-fix SHA in "Verification outputs" above).

## Fix 2026-10-28 (second) — P2 German item English explanation, two factual mistranslations in one sentence only
- OLD (wrong): "Germany turns its clocks back one hour on Sunday night, ending summer time, while eleven countries are on holiday."
- NEW (correct): "Germany turns its clocks back one hour in the early hours of Sunday, ending summer time, while eleven German states are on holiday."
- Authority: (1) the headline's "elf Länder" is shorthand for German
  federal states — the same DE core article's own continuation reads
  "Elf Bundesländer haben in dieser Woche gleichzeitig Herbstferien"
  (eleven federal states with autumn holidays simultaneously), not
  eleven sovereign countries. (2) The excerpt says the change happens
  "In der Nacht von Samstag auf Sonntag" at 3.00 — the night from
  Saturday to Sunday, i.e. the early hours of Sunday; "Sunday night"
  ordinarily means the night following Sunday daytime.
- Scope: EXACTLY this one string. Changed in the build source
  (`hidden_files/cover-w43-en-build/build.py`, EXPL["de"], line
  150), all 8 SVGs regenerated, copied to the edition dir. No
  headline, excerpt, or other explanation was touched — including
  the P7 zh-tw explanation, which still correctly reads "Strong
  Typhoon Jangmi…" (unchanged).
- Nothing-else-changed proof: regenerated build SVGs match the
  pre-fix set on 7/8 pages (SHA-256 identical); only p2-items.svg
  differs (pre-fix d1976fafc528cb1a08b132230ca3ef26b20bebd0c10114b6bbc8b4e361a1934d
  → new fd531498c11fb63eeb6ad718ed54e19df85108046df195fb1413d3486c9a8e2c),
  and p7-items.svg is byte-identical to pre-fix (the previous round's
  Jangmi fix untouched). Edition SVGs are byte-identical to the
  build SVGs on all 8 pages. Zero occurrences of the old sentence
  ("eleven countries", "on Sunday night" in this explanation) remain
  in build.py, the build SVGs, or the edition SVGs.
- Re-verification (same procedure as the original build):
  - Occlusion audit: `tools/venv/bin/python tools/occlusion_audit.py
    files/cover-w43-en/svg` → selftest OK, **0 flags**.
  - Final PDF rebuilt ONLY with `tools/venv/bin/python
    tools/webpdf.py files/cover-w43-en/svg
    files/cover-w43-en/cover-w43-en.pdf` → **404,990 bytes**
    (< 7 MB), **8 pages**, **9,211 text bytes** (pdftotext
    non-empty; pre-fix PDF was 404,984 bytes / 9,194 text bytes —
    the +17 text bytes is exactly the new sentence's +17 characters).
  - pdftotext: new sentence present (whitespace-normalized), old
    sentence absent; "eleven countries" 0, "Sunday night" 0;
    "Jangmi" 1, "Fung-wong" 0; all 12 headlines extract (12/12).
  - New PDF SHA-256:
    6e0770a64032c5b8a2653601a3a0eac602cc4f37477db51c395439ce523efa32
    (supersedes the pre-fix SHA in "Fix 2026-10-28" above).
