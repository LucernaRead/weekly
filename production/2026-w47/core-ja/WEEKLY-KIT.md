# WEEKLY-KIT — Lucerna 日本語版 VOL.4 (W47, 16–22 Nov 2026)

Slug: `2026-w47-ja-zh-cn`. Target language: Japanese. Reader language:
Simplified Chinese (the core edition IS the zh-cn edition, as in W46:
no separate `weekly-report-w47-ja-zh-cn` build dir exists).

## §1 Specification — SOP §1.1 visual system (rebuilt 2026-11-10, Round 5)

- 8 pages, 1950×2700, 4 columns. Paper `#fbfaf6`, ink `#302c28`,
  body `#3a3631`, caption `#6f675d`, fine line `#d8d2c4`, book-green
  cloth `#37402f`, olive `#46581f`, goose-yellow `#f6e08e`,
  on-cloth text `#f4efe1`. Level badges: A2 `#5c6e30`, B1 `#46581f`,
  B2 `#37402f`, white text. No gold, no brick-red, no near-black
  backgrounds; no double outer frame. The W46 warm-ivory system
  (`#f7f1e2`, double frame, `#b3a06a`/`#a4553a`/`#2c2822`) was
  removed in Round 5 per the coordinator's ruling that W47 must be
  built to §1.1 (KIT disclosure ≠ compliance).
- Footer every page: `Lucerna　日语周报 VOL.4　LUCERNA JAPANESE WEEKLY`
  (full-width spaces), page line `第 N 版／共 8 版` (full-width ／).
  Top strip: `VOL.4　第4号` / `毎週、日本語で　每周一期　日本人が読んでいる日本語を読む` /
  `2026年11月16日（月）〜22日（日）`.
- Masthead `Lucerna` (tables.json: no article for Japanese).
  P1 masthead rule: olive line at y=420 with the tricolor moth
  (`assets/lucerna-moth.svg`, same as core-en) centred on the line;
  band below is cloth-green with cream title + goose-yellow subtitle.
- P1 badge (same geometry as W46): `日本語版　VOL.4　酉の市　新酒　相撲　紅葉`.
- Section bands are cloth-green with cream text; side boxes have a
  light fill (`#f0eee5`) and no stroke; captions in GREY; section
  rules olive.
- P1 lead headline (15 chars whitespace-stripped, cover.mjs LIMITS
  headline for CJK is 30): 「二の酉と新酒、19日の木よう日」.
- Explanation layer: Japanese articles (です・ます, full weekday forms,
  no ruby) + small grey Simplified Chinese glosses/notes/answer notes.
- Exercises: 150 total, continuous numbering 1–150, registry-generated
  P8 answers. Measured: A2 48 · B1 73 · B2 29. By page:
  10/18/18/18/18/18/12/38. By type: 完成句子 50 · 单选 51 ·
  完形单选 13 · 词汇配对 12 · 判断对错 11 · 造句 8 · 翻译 4 · 写作 1.
- P8 model text 154 characters (printed range 150–200).
- Furniture: `tools/tables.py furniture zh-cn --target ja --week
  2026-W47` errors (`no established furniture column for native
  'zh-cn'`; established: de, es, fr, it, nl, pt) — the W46-established
  furniture strings were reused with VOL.4. No furniture string was
  invented.
- `svglib.py` carries the W46 D-CORE-01 fix (NO_START + NO_END kinsoku
  in `wrap()`), md5 `74177544422fe677639d769cd80499fb`, unchanged.

## §2 Lead and page contents

- P1 front, A2 — lead: Ni-no-tori + Beaujolais Nouveau解禁 share
  Thu 19 Nov. Numbers box 19/22/23/30; trend box (4 topics, dated
  sources); contents; word of the week 熊手; maple photo; buzzword
  nominees mini-feature; briefs (sumo / 小雪 / 勤労感謝の日);
  lightning quiz ex 7–10. Lead fill-ins ex 1–6.
- P2 life, A2 — 酉の市と熊手 + 小雪 / 勤労感謝の日; words strip
  熊手/手締め/解禁/小雪. No photo. Ex. 11–28.
- P3 culture, A2→B1 — Beaujolais + 酉の市屋台; beaujolais photo;
  culture calendar box. Ex. 29–46.
- P4 sport, B1 — Sumo Kyushu basho days 1–3 + star-record box +
  full-width closing strip (champion undecided, final result promised
  in VOL.5). No photo (see §6). Ex. 47–64.
- P5 youth, B1 — Buzzword award 30 nominees + Arashiyama photo.
  Ex. 65–82.
- P6 deep read, B2 — Foliage moving to Kyoto + labelled practice-data
  chart (京都 38 / 浅草 24 / 高尾山 22 / 家 16 = 100%, bar widths
  1140/720/660/480, labelled as practice data, not a real survey).
  Ex. 83–100.
- P7 language focus, A2/B1/B2 — Language columns (酉の市 words;
  buzzwords; sumo numbers), error clinic ×4, frame 「福をかき込む」,
  readers' corner (editor's example + disclosure, see §4), 8 golden
  phrases, VOL.5 teaser. Tori photo (2025, captioned as such).
  Ex. 101–112.
- P8 assessment + writing + all keys — A chronicle cloze 8, B MC 8,
  C reading about ユウ 4 (Thu 19 酉の市, Fri 20 紅葉 photos, Sun 22
  sumo final on TV, Mon 23 holiday), D sentence building 4,
  E translation JA→ZH 4 (unified direction), F matching 4,
  G shrine-dialogue cloze 5, H writing 『私の11月の1週間』
  (150–200字). Ex. 113–150.

## §3 Trend sources (all facts sourced, 10 Nov 2026 research)

- Sumo Kyushu basho: Fukuoka Kokusai Center, opened Sun 8 Nov,
  closes Sun 22 Nov. Day 1 (8 Nov): Ōnosato lost to Yoshinofuji
  (tsukiotoshi); Hōshōryū beat Umi-no-umi (oshidashi); Kirishima beat
  Ura; Kotosakura lost to Fujiryūga; Aonishiki lost to Asanoyama.
  Day 2 (9 Nov): Ōnosato beat Fujiryūga (yorikiri), first win;
  Hōshōryū and Kirishima 2nd straight wins; both yokozuna + all 3
  ōzeki won. Day 3 (10 Nov): Hōshōryū lost to Fujiryūga (oshitaoshi)
  — Fujiryūga's first kinboshi, 11 basho from debut, 7th fastest
  since the 1958 six-basho system; Ōnosato 2nd win. After day 3 both
  yokozuna are 2–1. Ōnosato aiming for 2nd straight title, 7th
  overall; Hōshōryū returning after 3 straight absences, right-knee
  surgery late July. Sources: Sponichi, Sanspo, Daily, Excite /
  SportsHochi. Kotosakura is written 琴櫻 (official kanji).
- Tori-no-ichi 2026: Ichi-no-tori Sat 7 Nov; **Ni-no-tori Thu 19 Nov**;
  no San-no-tori; Asakusa Ōtori Shrine + Chōkoku-ji; 0:00–24:00 from
  the first drum; **~150 kumade shops, ~750 food stalls** (Ōtori
  Shrine official 「酉の市豆知識」, via multiple secondary sources
  2026-11-10: everynews.tokyo, lifestyle.assist-all.co.jp,
  matsuri.group, ikokajapan.com; Time Out gives 800–900 stalls
  in a typical year). The Round-5 fix replaced the wrong "~80 stalls".
  Kumade; tejime; washi-mai.
- Foliage: Weathernews 3rd forecast 29 Oct 2026: Takao ~13 Nov,
  Miyajima ~21 Nov, **Arashiyama ~23 Nov**, Kōrankei ~23 Nov, Akizuki
  ~28 Nov; mid-Nov onward slightly later than average. Arashiyama
  spot page (Weathernews, read 8 Nov 2026 via the secondary reading
  at yuuekiinfo.com/archives/6450, updated 8 Nov 19:01): ~20%
  coloured, **peak from ~26 Nov, leaf-fall start ~12 Dec**. The
  25 Oct reading was peak ~24 Nov, leaf-fall ~10 Dec; the 8 Nov
  reading supersedes it, and the issue attributes the figures to
  "11月8日の時点". A table at ikokajapan.com cites a 3–5 Nov
  snapshot of the spot page (~22 Nov / ~8 Dec) — spot values move
  with the update date, so the issue uses the 8 Nov reading. **23 Nov
  is the 29 Oct 3rd-forecast value (P6 para 1), NOT the spot-page
  reading** — P6 para 2 previously misattributed it; fixed in
  Round 5 (12 Dec replaces the wrong 9 Dec in P6 para 2, the P6
  numbers box, ex 85 and P8 ex 127; keys unchanged). Japan
  Meteorological Corporation 1st forecast 2 Sep: Tokyo ~29 Nov,
  Osaka ~4 Dec. tenki.jp differs (Arashiyama from 13 Nov) —
  forecasts differ by definition; the issue attributes each figure
  to its forecaster.
- Beaujolais Nouveau 2026: release **Thu 19 Nov** (3rd Thursday,
  0:00), Burgundy Beaujolais; Japan earliest worldwide due to time
  difference; Hanshin Umeda ~40 kinds.
- Buzzword award: 2026 新語・流行語大賞 nominees 30 announced
  **Thu 5 Nov** (ORICON / Sponichi): りくりゅう (Miura Riku / Kihara
  Ryuichi figure-skating pair), ちいかわ（現象）, 酷暑日, NISA貧乏,
  ボンボンドロップシール（ボンドロ）, 好きすぎて滅！ (M!LK song),
  パンチくん, AI暴走; top 10 + grand prize **Tue 1 Dec 14:00**,
  Tokyo Kaikan.
- Calendar: 小雪 Sun 22 Nov (24 solar terms); 勤労感謝の日 Mon 23 Nov
  (public holiday, just after the issue week). Dates verified with
  `date -d` (Asia/Tokyo).

## §4 Promises honoured (from W46 JA VOL.3, KIT §10)

1. Sumo Kyushu basho results — reported on P4 for days 1–3 only,
   verified from the sources in §3. **Honesty caveat: the final
   champion cannot be known before the Mon 16 Nov deadline (basho
   ends Sun 22 Nov).** P4 states the champion is undecided and
   promises the final result in VOL.5. No result was fabricated.
2. Tori-no-ichi Ni-no-tori, Thu 19 Nov 2026 — P1 lead + P2 + P7.
3. Foliage continuation as the peak moves to Kyoto (Arashiyama
   ~23 Nov) — P1 + P5 + P6.
4. Real readers' letters + best P8 writing (W46 topic
   『私の11月の1週間』): NO real letters or texts are known to have
   arrived (nothing in the task or files evidences any arrival). No
   fabricated readers/letters/names/quotes. P7 prints a clearly
   labelled editor's example PLUS on-page disclosure in Japanese and
   Simplified Chinese stating no real letters had arrived by the
   deadline, promise carried forward to VOL.5. The writing topic
   『私の11月の1週間』 is carried forward unchanged.

## §5 Golden phrases (each exactly 2× in the whitespace-stripped text)

1. 「19日（木よう日）は、酉の市・二の酉です。」(P1)
2. 「同じ19日（木よう日）は、ボジョレー・ヌーヴォーの解禁日です。」(P1)
3. 「熊手は、商売繁盛の縁起物です。」(P2)
4. 「ボジョレー・ヌーヴォーは、フランスのボジョレー地方の新酒です。」(P3)
5. 「3日目まで、大の里も豊昇龍も2勝1敗です。」(P4)
6. 「『りくりゅう』は、フィギュアスケートのペアです。」(P7 B1)
7. 「紅葉の見頃は、京都へ移っています。」(P1)
8. 「酉の市は、11月の酉の日に開くお祭りです。」(P2)
Recount after final render: 8× exactly 2 — bare-sentence recount on
the whitespace-stripped `2026-w47-ja-zh-cn.text.md` (and on the final
SVGs). Counting note: the bare sentence is what occurs twice (article
+ P7 golden-phrases box). The `ja-core-checks.py` quote list includes
the 「」 brackets, so it counts 1× (P7 box only) — that is the same
counting convention as W46, not a missing occurrence. Near-duplicate
traps were avoided in source: P7 A2 uses 『熊手』/『酉の市』 quoted
forms; P1 para 3 uses different punctuation for phrase 5; P8 E stems
use different sentences.

## §6 Images

Five images, all PD/CC0, verified against the Wikimedia Commons API
on 2026-11-10 (byte sizes match the downloaded originals). Full
credits in `assets/CREDITS.md`. P1 maple.jpg (Poliphilo, CC0);
P3 beaujolais.jpg (Alainauzas, public domain); P5 arashiyama-pond.jpg
(Tenryū-ji Sōgenchi pond, lumoplank, CC0); P7 tori.jpg (Hanazono
Shrine, Mozzucu, CC0 — 2025 photo, captioned as such); P8
arashiyama-temple.jpg (lumoplank, CC0). P4 carries no photo: the PD
1936/1909 dohyo photos found were too low-res (433×321 / 478×295)
and were rejected. P2 and P6 carry no photo (P6 carries the
practice-data chart). No CC-BY/CC-BY-SA image used. The two unused
W46 files (hiroshige.jpg, stadium.jpg) were removed from this dir's
`assets/` copy; the originals remain in the W46 core dir.

## §7 Proofread record

- Builder self-check: no FLOW OVERFLOW / HEAD TOO WIDE warnings.
- Kinsoku line-start hits: 0. Orphan-line scan over the full text
  dump (lines starting with `·）)」、。，．！？：；ー…‥・` or ≤2 chars,
  excluding structural elements): 0 hits after final fixes.
- P6 chart: labels end x≤154, bars start x=338 — clear.
  `ja-core-bandscan.py`: band collisions ok; chart labels
  京都/浅草/高尾山/家 ink ends 132/132/154/110, all < bar start 338.
- Full text dump proofread (1345 dump lines, P1–P8) + all 8 card PNGs
  visually checked, in 5 rounds (see §11). All dates/weekdays,
  sumo facts vs sources, chart arithmetic (91: 38−24=14; 92: 38+24=62;
  93: 100), all 150 keys vs stems re-verified against the printed
  P8 answers (registry dump vs dump: 0 mismatches, numbering 1–150
  continuous, page grouping correct), E section unified to JA→ZH —
  verified in round 3 and re-verified in round 5.
- Feature-column whitespace on P2/P3/P4/P6 follows the W46 pattern
  (short feature columns); disclosed, not a defect. Line starts with
  particles (が, etc.) are kinsoku-clean; accepted, not defects.
  Wrapped option lines may start with a full-width space (the
  "　B." / "　C." continuation) — same wrap pattern as W46,
  accepted, not a defect.
- P1 layout (Round 5): headline flow ends col 2 y=915 (bottom 1828);
  after Round 6 (masthead 196px / headline 56px) it ends y=921.
  row B (photo / buzzwords / briefs) starts y≈1908 after the +24
  shift; quiz ends y=2525 (bottom 2540). P7 layout: col3 ends
  1768.58; teaser ends 2542.58 (footer 2580);
  tori image spans cols 0–2 at y=1180, h=220, caption y=1400. P8:
  exercise flow ends col 3 y=531 (bottom 1252); arashiyama-temple
  image in col 3 at y=710, h=290, caption y=1000; keys flow ends
  col 3 y=2351 (bottom 2540). P5: col3 ends 1506.45 (exercises
  start 1580).

## §8 Gates (all recorded in ja-gates.log)

- Occlusion audit: `tools/occlusion_audit.py` — 0 flags
  (`ja-core-occlusion.json`; selftest OK, all 6 classes fired on
  planted controls, clean controls silent). Round 5 caught 2 flags
  on the first re-render (P1 LINEX: the word-of-the-week gloss
  "进来。" struck by the row-B divider; P1 BOXTITLE: source line
  18.5 px ink ran past the trend-box edge at 1862.0) — fixed by
  shifting row B +24 and shrinking the source line to 17 px
  (ink ends 1835.5, 26.5 px clear), re-audit 0 flags.
- P8 extract: `tools/p8.py extract --total 150` — noted set 150/150
  (`ja-core-p8.json`).
- Freeze baseline: `tools/freeze.py baseline` — 8/8 SVGs
  byte-identical, run twice with identical sha256; core integrity
  unchanged by the runs. Re-confirmed after the Round-5 registry
  dump rebuild (sha256 of all 8 SVGs unchanged).
- Web PDF: `tools/webpdf.py` — `Lucerna-VOL4-web.pdf`, 4,654,731
  bytes (< 7 MB), 44,763 pdftotext raw bytes, byte-identical to the
  print PDF text (character multiset, whitespace aside). Print PDF kept:
  `Lucerna-VOL4.pdf` (25,973,509 bytes, 8 pages).
- Text: `2026-w47-ja-zh-cn.text.md`, 44,432 bytes, 1356 lines,
  1329 text lines.
- P8 minimum font size: 9.975 pt (answers, 13.3 SVG px; Tm-matrix
  measurement of print PDF p.8; next size 10.35 pt = 13.8 px
  exercises).
- Strict-CJK: not applicable to the core (Japanese text is native).
- Fix 1 re-gate (2026-11-11, core typo key 47, see §11): occlusion 0
  flags; p8 extract 150/150, noted set and keys identical to the
  pre-fix extract (0 key diffs); freeze 8/8 with
  `tools/venv/bin/python`; print/web text layers byte-identical
  (44,818 raw bytes each; web 85,061 -layout bytes). New artifacts:
  print `Lucerna-VOL4.pdf` 26,018,019 bytes, SHA-256
  `20b9d50469fbb6ca6470c17becb2790a30f69191d9083520a9270ea7ebbe9ab4`;
  web `Lucerna-VOL4-web.pdf` 4,652,763 bytes, SHA-256
  `8722bdfbcec0478a7a60fc86ab0ee7cc9333f957253959476d4f608eed82d5b0`;
  text.md 44,432 bytes, SHA-256
  `bcfa667da57e2f477b9d825200b98db454ade3c1dde6ec92ea3d446b0bf9926a`.
  Only `svg/p8-tesuto.svg` changed
  (`9db7294a…` → `f7118644ac8b31a4be2f04c7044afd0a9043592bfd89d1b45c1b0526c08798a2`);
  P1–P7 SVGs byte-identical to pre-fix. Evidence in
  `hidden_files/w47/scratch-ja-fix-core1/` (FIX-LOG.md, GATE-LOG.md).
- D5 rebuild (2026-11-12, SOP §1.1; `svglib-ja-d5.py` lands as the core
  template per CJK-DECISION §4.2 — `apply_variant.py --patch-core` refuses
  old-style core-ja svglib, as designed): Latin explanation layer 207 →
  0 in Noto Sans CJK (D5 census PASS; curly quotes 0, total 0).
  Full gates, all green: run.py TOTAL 150, 0 FLOW OVERFLOW / 0 HEAD TOO
  WIDE (head_check PASS); occlusion 0 flags (selftest 6/6); p8 extract
  150/150, compare vs pre-D5 base CLEAN keydiff=[]; freeze baseline 8/8
  byte-identical; freeze diff vs base: added CJK 2 (both U+3000, run-split
  whitespace artifact — SVG char multiset differs only in space/U+3000,
  no content char differs); spill 0; boxtitle 0 DEFECT (29 titles,
  459 body lines, real pre-D5 backup); edge 0 TOUCH / 0 NEAR; creambox
  PASS 0 defects (ratios n=361 median 1.012 boldT 1.040 boldF 1.002;
  P8 lines 206→206, slack 78.1 px unchanged); print/web text layers
  character-multiset identical, and identical to the delivered text
  (44,763 raw bytes each). New artifacts: print `Lucerna-VOL4.pdf`
  25,973,499 bytes, SHA-256
  `e5b8a65dcf658d7303dc93b814cd43faf69ac9d32f65bdac93c1d002abcd32c6`;
  web `Lucerna-VOL4-web.pdf` 4,654,724 bytes, SHA-256
  `a1f1a21c267fbbbeb8c9c0837dac16b0d097c9d089568e70de9e3ee4c8949059`;
  text.md unchanged (44,432 bytes, SHA-256
  `bcfa667da57e2f477b9d825200b98db454ade3c1dde6ec92ea3d446b0bf9926a`).
  Post-sync verification on the production dir: freeze baseline 8/8,
  D5 census PASS, quotes census 0. Evidence in
  `hidden_files/w47/scratch-d5-ja/core-ja/` (RUN-LOG.md, gate logs + JSONs).
  NOTE: core-ja/render.py hardcodes BASE to the production dir (W46-era
  file); a first scratch render overwrote the delivered print PDF with a
  pre-D5 re-render (25,973,499 B vs delivered 26,018,019 B, SHA
  `20b9d504…`) — pre-D5 SVG/svglib preserved, delivered web PDF intact,
  final D5 artifacts unaffected; scratch builds now rewrite BASE to the
  build dir (production render.py untouched).

### Fix round — D1 romaji fix (2026-11-12; independent reproof PROOF-NOTE.md)

- D1 (all 11 ja editions): `りくりゅう` romaji `ryuuryuu` → `rikuryuu` (5× per edition: P7 gloss + P8 answers 66/77/80/105). Sources: `content7.py` (2×) + `content56.py` (3×). Japanese core text `りくりゅう` untouched; answer letters untouched. (This KIT's §1 carries no romaji spec line, so no §1 change applies here; the fan-out KITs' §1 lines were updated.)
- Changed SVGs vs pre-fix: p7-kotoba.svg, p8-tesuto.svg; unchanged: p1-hyoushi.svg, p2-kurashi.svg, p3-bunka.svg, p4-supotsu.svg, p5-wakamono.svg, p6-fukayomi.svg.
- Print PDF `Lucerna-VOL4.pdf`: 25,973,509 bytes, sha256 `0ce5e4b872ae4d53fc639bff0ae2df3cf2bfd91149bd08b04400920e21adc214`.
- Web PDF `Lucerna-VOL4-web.pdf`: 4,654,731 bytes, sha256 `0f9098ff3bf0836c279960beffdb1ff619c1cdb01fceef699046c0a77be1e9ef`.
- Text `2026-w47-ja-zh-cn.text.md`: 44,432 bytes, sha256 `55c570f1bd0e9ea4d907960fe0fc472fe69440bacf67a83af40d0d48b977e1aa` (surgical replacement, exactly 5 lines changed, each only by the fix substitution).
- Full re-gates (all green):
  - run.py: TOTAL 150
  - head_check: HEAD CHECK PASS 0 defects
  - D5 census: CENSUS PASS
  - quotes: GRAND TOTAL defective: 0
  - occlusion: 0 flags
  - p8 extract: noted set = 150 of 150
  - p8 compare: status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[]
  - freeze baseline: 8/8 byte-identical (core integrity unchanged)
  - freeze diff vs pre-fix base: TOTAL added CJK characters: 0; TOTAL added Latin strings: 5 (the 5 substitutions: p7 +1/-1, p8 +4/-4; p1–p6 +0/-0)
  - spill: 0 SPILL
  - boxtitle: 0 DEFECT (29 titles, 459 body lines)
  - edge: 0 TOUCH, 0 NEAR
  - creambox: CREAMBOX PASS 0 defects
  - text layer: print-vs-web multiset diff: +0 -0 IDENTICAL; patched-vs-delivered +10 -10 (the 5 substitutions)
  - PDF text: print+web `ryuuryuu` 0×, `rikuryuu` 5×
- Post-sync verification on the production dir: freeze baseline 8/8, D5 census PASS, quotes census 0; production svg/text.md `ryuuryuu` 0×, `rikuryuu` 5×.
  Evidence in `hidden_files/w47/scratch-fix-ja/core-ja/` (fix log + gate logs + JSONs).
  Note: the previous fix worker's `update_kit.py` failed on this KIT
  (its §8 has no `###` subsections, so two historical print-size lines
  fell in its "head" match); this subsection and the §11 entry were
  written by the replacement worker with the same content the script
  would have produced.

## §9 Reproduction

Build dir: `production/2026-w47/core-ja/` (copied from the W46 JA
build; W46 dirs never edited). One-process driver:
`tools/venv/bin/python run.py` (content12→34→56→7→8, shared bslib4
registry), then `tools/venv/bin/python render.py` (cards PNG + print
PDF). Web PDF via `tools/webpdf.py` only. Text export via
`hidden_files/w47/scratch-ja/export-textmd.py` (reads the
ja-core-checks.py dump, writes the W46-format .text.md). NOTE
(2026-11-11, Fix 1): that exporter path no longer exists in this
clone; the exporter was reconstructed as
`hidden_files/w47/scratch-ja-fix-core1/export-textmd-core.py`
(SVG `<text>` elements in document order, modelled on the validated
fanout-ja-en exporter) and proven byte-identical against the pre-fix
.text.md from the pre-fix SVGs before use. Never run a
build module standalone; never import a content module inside a build
dir. Scratch (crops, dumps, exporter) lives in
`hidden_files/w47/scratch-ja/`.

## §10 VOL.5 promises registered

- Sumo Kyushu basho FINAL result (basho closes Sun 22 Nov; W47 P4
  promises it).
- Buzzword award top 10 + grand prize, Tue 1 Dec 14:00, Tokyo Kaikan.
- Readers' letters + best P8 writing (W47 topic
  『私の11月の1週間』) — carried forward; print only real arrivals,
  else the disclosure again.
- Foliage continuation as the peak moves to Tokyo (~29 Nov) and
  Osaka (~4 Dec).

## §11 Fix record — proofread rounds (builder, 2026-11-10)

Round 1 (visual, all 8 cards): 14 wrap orphans / short-line defects.
Fixed titles (P2 「19日 — 夜通しの酉の市」, P3 「新酒の夜 —
19日の0時」, P6 「見頃を追いかけて京都へ」), P1 ex 8 stem, P2 ex
13/15/17, P4 ex 57, P5 words box / ex 65/66, P6 facts box,
P7 ex 103/107.

Round 2 (orphan scan, 17 hits → 18 edits): P1 para-2 ending, P1
numbers-box 23, P1 words box, P1 小雪 brief (dropped （2面）), P2
last para + facts box, P3 ex 37, P4 ex 55/57, P5 gloss reorder +
facts box, P6 para-1, P5 ex 66 stem, P7 ex 107 + B1 bridge,
P8 C129/C130 stems, P8 model text, P8 C-passage (dropped "SNSに" so
the passage's final "す。" pulls up).

Round 3 (full text read of all 1331 dump lines, P1–P8): verified all
dates/weekdays, sumo facts vs sources, chart arithmetic, all 150
keys vs stems, numbering 1–150 continuous, E section unified to
JA→ZH (E139/E140 stems/keys swapped: keys now Chinese). Found 4
further issues, all fixed: (a) P4 record box 琴桜 → 琴櫻 (official
kanji for Kotosakura; only occurrence); (b) P7 B1 bridge split
"ノミネート" → split into two `bridge()` calls ("りくりゅう 双人滑 ·
ちいかわ 吉伊卡哇" / "ノミネート 提名"); (c) P7 ex 107 split "候補" →
A option "優勝する" → "優勝"; (d) P8 key 130 note "周五把红叶照片上传
到SNS" → "周五把红叶照片上传" (passage no longer mentions SNS).

Round 4 (visual verification of round-3 fixes): P4 record box shows
琴櫻; P7 bridge two clean lines; P7 ex 107 now breaks after particle
に ("C. 候補に" / "選ばれること") — grammatically clean, accepted;
orphan scan 0 hits; phrases 2×; kinsoku clean. No further defects
found; edition re-gated on the final artifacts (§8).

Round 5 (independent proofreader round + builder rework, 2026-11-10):
independent proofreader found 4 defects, all fixed at source and the
whole issue re-rendered + re-checked from scratch:
- D1 (§1.1 visual system): rebuilt to SOP §1.1 — paper `#fbfaf6`,
  ink `#302c28` (body text also renders in ink `#302c28`; `#3a3631`
  is the §1.1 table value for body text but is not used anywhere in
  the build — same as core-en), caption `#6f675d`, line `#d8d2c4`,
  cloth `#37402f`, olive `#46581f`, goose `#f6e08e`, on-cloth
  `#f4efe1`; badges A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f`;
  double outer frame removed; gold/brick/near-black removed;
  "·" → full-width space, ASCII `/` → full-width ／ in footer and
  page lines; P1 olive rule y=420 with tricolor moth; side boxes
  borderless. Changed files: `svglib.py`, `bslib4.py`, all 5 content
  files; moth SVG copied from core-en. SVG grep audit after the
  rebuild: `#fbfaf6` 1×/page, old `#f7f1e2` 0×, banned colours 0×,
  "·" 0×, `第N版／共8版` 1×/page, double-frame rects 0×.
- D2 (P2 stalls): "80軒近くの露店" → 「熊手店は150店ほど、露店は
  750店ほどあります」 (Ōtori Shrine official 「酉の市豆知識」,
  §3).
- D3 (P6 Arashiyama): spot-page reading re-verified by the builder
  against the 8 Nov 2026 secondary reading (yuuekiinfo.com,
  updated 8 Nov 19:01): ~20% coloured, peak ~26 Nov, leaf-fall
  ~12 Dec; 23 Nov is the 29 Oct 3rd-forecast value. Fixed P6 para 2
  (11/26, 12/12), P6 numbers box ("12 — …12月12日ごろ"), ex 85
  (B=12月12日ごろ) and P8 ex 127 (A=12月12日ごろ); keys unchanged.
  The two 12月9日 distractors (ex 83 C, ex 86 C) kept — wrong
  options only.
- D4 (ちいかわ): "大ヒット映画" → "大ヒットした漫画" in 7 places
  (P5 article + words box, ex 67, P7 B1, ex 106, P8 ex 128); keys
  unchanged.
- Re-render + full re-check: run.py exit 0, zero FLOW OVERFLOW /
  HEAD TOO WIDE; full text read of all 1345 dump lines; registry
  vs printed P8 answers 150/150, 0 mismatches; all 8 cards visually
  checked; occlusion audit 0 flags after fixing the 2 mid-round
  flags (see §8); p8 150/150; freeze 8/8; P8 min font 9.975 pt.
  No further defects found in the re-check round. Edition re-gated
  on the final artifacts (§8) and returned for a fresh independent
  proofread.

Round 6 (§1.1 type-scale alignment, 2026-11-10): coordinator-ordered
  alignment of the three §1.1 deviations in the Round-5 proof note,
  observation (1). Masthead 168px → 196px (147pt) and P1 headline
  44px → 56px (42pt, lh 1.2 → 1.06) landed cleanly — P1 headline flow
  ends col 2 y=921 (bottom 1828), no overflow, masthead clear of the
  top rule and subtitle. P8 stems 13.8px (10.35pt) → 20.5px (15.375pt)
  was tried and ROLLED BACK per the rollback clause: the build produced
  4× FLOW OVERFLOW (P8-ex ends col 3 y=1390, bottom 1252) and the
  occlusion audit flagged 62 markers, all on P8 (G-section ex 145–147
  100% covered by the temple image, H head + ex 149–150 struck by the
  answers rule, exercise text overlapping the caption and keys 113–117).
  The P8 exercise flow has only ~179px of slack above the col-3 image
  (ends y=531, image at y=710) and the 20.5px stems need ~+850px of
  column height; no clean fix exists without layout surgery, so the
  stems stay at 13.8px / 10.35pt (answers still 9.975pt, ≥ 9.75pt floor).
  Note: the ko P8 precedent cited in the task does not exist on disk —
  ko content8.py still uses size=13.8 (10.35pt, confirmed in ko's print
  PDF: 60 spans at 10.35pt); the verified 20.5 precedent is de, whose P8
  layout was extended for it (battery bottom 1505 → 1555). Margins were
  already compliant (MX=88px = 66pt both sides; band rects x=88 w=1774
  on all 8 pages) — untouched. KIT §11 D1 wording corrected (body text
  renders in ink `#302c28`, `#3a3631` is the table value, not used).
  Final artifacts re-gated in `hidden_files/w47/scratch-ja-fix2/`:
  occlusion 0 flags, p8 150/150, freeze 8/8, print/web text layers
  byte-identical, 150 keys re-verified with 0 mismatches.

Fix 1 (core typo key 47, 2026-11-11): the de-fr first-round proof
  (observation O1) and the ja-de fix-1 check jointly found one core
  typo — `content34.py:186`, P8 key 47 Chinese note
  "首日战胜大之里的是一之富士". Verified before touching: (1) the
  Japanese text reads 義ノ富士 (`content34.py:120` P4 article,
  `:187` key 47 stem, `content8.py:21` ex 115 stem); (2) keys 47 and
  115 name the same person (both: Ōnosato lost day 1 to Yoshinofuji;
  key 115 note `content8.py:20` already correctly reads "义之富士");
  (3) full-core grep: 一之富士 occurred exactly once
  (`content34.py:186`, text.md:1247, p8 SVG 1×); 义之富士 once
  (`content8.py:20`, text.md:1319, p8 SVG 1×); no other Chinese note
  mentioning 義ノ富士 confuses 一/义 ("一之酉" in `content12.py:261`
  is Ichi-no-tori, correct, untouched). Fix: one character 一→义 at
  `content34.py:186`, nothing else. Whole issue re-rendered
  (`run.py` ×2, `render.py`, `webpdf.py`, text.md re-exported) and
  re-gated in `hidden_files/w47/scratch-ja-fix-core1/`: run.py exit 0
  zero overflow both runs, registry 150 (A2 48 / B1 73 / B2 29);
  freeze 8/8; occlusion 0 flags; p8 extract 150/150; print/web text
  layers byte-identical; P8 min font 9.98 pt (≥ 9.75 pt floor,
  Round-5 Tm-matrix value 9.975 pt); U+2019 full sweep 0; 150 keys
  re-verified against the registry (145 exact-line matches; the 5
  remaining are the frozen F-section stem+key display format and the
  writing-item ✓ display, all byte-identical to pre-fix); 8 pages
  visually checked, P8 answers area magnified (key 47 reads
  "义之富士"). Post-fix grep: 一之富士 0 everywhere (source, text.md,
  SVG); 义之富士 2× in each (pre-fix 1 + 1, as expected). The
  text.md exporter (`hidden_files/w47/scratch-ja/export-textmd.py`)
  no longer exists in this clone, so it was reconstructed in the fix
  scratch (`export-textmd-core.py`, modelled on the validated
  fanout-ja-en exporter) and proven byte-identical against the
  pre-fix text.md from the pre-fix SVGs before use. NOTE: the first
  `webpdf.py` attempt failed mid-run (RC=120, log stops after the
  first subset font) and the text.md write then failed with EDQUOT
  (disk quota exceeded, 45 GB free on df) — both transient under
  parallel load; small-write probe passed minutes later and the
  webpdf retry (fresh TMPDIR) succeeded RC=0. Out of scope, untouched:
  the fan-out editions (their P8 notes are reader-language
  translations; de already verified correct as Yoshinofuji) and the
  §3 trend-narrative romanizations (Umi-no-umi, Fujiryūga — separate
  record issue). Awaiting a fresh full independent proofread
  (coordinator to assign).

- Fix round (2026-11-12, D1 romaji fix; see §8 fix subsection for gates + SHAs): D1 `ryuuryuu` → `rikuryuu` in `content7.py` + `content56.py` (5×, P7 gloss + P8 answers 66/77/80/105). Full rebuild + re-gates; print/web/text.md re-synced with new SHAs recorded in §8.
