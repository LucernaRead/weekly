# FANOUT-REPORT-en — W47 English family (core-en → 10 reader editions)

Core: `production/2026-w47/core-en/` (en-zh-cn, VOL.4, 150 exercises, fixed).
Order: de → fr → es → it → pt → nl → ru → ja → ko → zh-tw. One edition finished
and self-checked before the next starts; no batching.

## de — COMPLETE, self-check zero issues

- Edition: `production/2026-w47/2026-w47-en-de/` (slug `2026-w47-en-de`)
- Print PDF: `The-Lucerna-VOL4-en-de.pdf`, 29,330,795 bytes,
  SHA-256 `6d91162fac10c81e59ec811362136cd69e4e535a5b7ad04b4b98c94d530d95ba`
- Web PDF: `The-Lucerna-VOL4-en-de.web.pdf`, 2,377,924 bytes,
  SHA-256 `e8c6746167d7351e0cda55427ec191da98af9112e94f281cf390e5488f28d751`
- Gates: run exit 0, 0 overflow; occlusion 0 flags; p8 extract 60/150, compare CLEAN
  (keydiff only 137–140, 150, expected); freeze direct sha256 8/8; print/web text diff 0/0;
  P8 min font 13.5 pt; badges = core on all 8 pages; text.md 51,989 bytes, 150/150 keys;
  8 cards visually checked, zero issues.
- Handover note: previous builder d132d807 reported complete, but on-disk state had no PDF /
  KIT / text.md / ABSTRACT and all gate JSONs were stale (predated the last render). Treated
  as incomplete; rebuilt + re-gated from scratch. One fix in this round: P2 SAY IT title
  "So sagt man die Uhrzeit" → "So sagt man das Datum" (W46 TM reuse error; the box teaches
  a date, not a clock time). Full record: `scratch-fanout-en/de/00-de-complete.md`.

## fr — COMPLETE, self-check zero issues

- Edition: `production/2026-w47/2026-w47-en-fr/` (slug `2026-w47-en-fr`)
- Print PDF: `The-Lucerna-VOL4-en-fr.pdf`, 29,330,444 bytes,
  SHA-256 `14da9810fa348a577d16927d90c7c2c05e67c537c533266ff81860486b7c11a5`
- Web PDF: `The-Lucerna-VOL4-en-fr.web.pdf`, 2,376,712 bytes,
  SHA-256 `0f188504a65e13488a5e07c2591c9ea9fa6f2adb0b5c0b2c3719797b8d7e22c3`
- Gates: run exit 0, 0 overflow; occlusion 0 flags; p8 extract 60/150, compare CLEAN
  (keydiff only 137–140, 150, expected); freeze direct sha256 8/8; print/web text diff 0/0;
  P8 min font 13.5 pt; badges = core on all 8 pages; text.md 53,239 bytes, 150/150 keys;
  8 cards visually checked after the final render, zero issues.
- Fixes in this round (each → rebuild + re-render + full re-gate): (1) P7 HEAD TOO WIDE ×3 —
  ERROR CLINIC / READERS' CORNER / AN EXAMPLE LETTER French subs shortened; (2) P2 FLOW
  OVERFLOW ×2 — calendar box → full-French short form, bridges A/B shortened;
  (3) occlusion 5 flags (P1 COVER midterm para, P2 LINEX SENATE title, P4 EDGE SATURDAY,
  P5 TEXTX ODD SOCKS, P6 EDGE HOW LONG) + 3 proactive box-title shortenings;
  (4) "Note | Note |" doubling 11× in gloss boxes — prefix stripped from the 11 gloss
  translations (kept on the P1 bridge, which uses f.bridge); (5) U+2019 full-width gap —
  SC sans face gives U+2019 a 1.0em advance, so every French elision rendered with a ~19 px
  gap; core uses ASCII apostrophe only (0× U+2019), so build_map.py now normalizes
  U+2019 → ' for all editions (fr content now 0× U+2019; P3 bridge gaps re-measured 8–10 px).
- Full record: `scratch-fanout-en/fr/00-fr-complete.md` (and the edition WEEKLY-KIT.md §8).
- Tools built this round (reusable for es–zh-tw): `build_map.py` (TM + miss-tr + fresh +
  meta → map, with poison rejection and U+2019 normalization), `fr/gates.sh`,
  `check_s11.py` (§1.1 + P8 checks, also re-validated de RC=0), `fr/make_textmd_w47.py`.

## es — COMPLETE, self-check zero issues

- Edition: `production/2026-w47/2026-w47-en-es/` (slug `2026-w47-en-es`)
- Print PDF: `The-Lucerna-VOL4-en-es.pdf`, 29,330,745 bytes,
  SHA-256 `e668bc5f40f8c6e3ddc7a1d705cc39bcd004a615a2d9f2f62a0cad68304bc719`
- Web PDF: `The-Lucerna-VOL4-en-es.web.pdf`, 2,377,727 bytes,
  SHA-256 `a0a2f9d6d3035e4df1e05f5cf8c73c3a7fea1e35f1440b4b18e52ca85e68bcd8`
- Gates: run exit 0, 0 overflow (all 17 flows within bottom); occlusion 0 flags; p8 extract
  60/150, compare CLEAN (keydiff 137–140, 150, expected); freeze direct sha256 8/8;
  print/web text diff 0/0; P8 min font 13.5 pt; badges = core on all 8 pages; text.md
  53,837 bytes, 150/150 keys; 8 cards visually checked after the final render, zero issues.
- Fixes in this round (each → rebuild + re-render + full re-gate): (1) P1 COVER — word-of-week
  bridge wrapped to 3 lines into IN BRIEF (57%) → shortened to "Elecciones de medio mandato:
  toda la Cámara y un tercio del Senado."; (2) P8-keys FLOW OVERFLOW — answers block ran to
  y=2907 (bottom 2560), 13 occlusion flags, compare SHORT missing 150 → W46-extracted P8 key
  size 15.5/1.3 too big for W47 Spanish notes (87 answers lines vs fr 73) → key_size 13.5,
  key_lh 1.26 (fr/nl/de values), P8-keys now ends 2443/2560; (3) p8 extract still missed 150
  after the geometry fix — W46 TM Q150 key uses a colon ("Pregunta abierta: …") while core/fr/de
  use dash style, and p8.py detect_note needs " — " before the trailing paren note → lit_override
  to dash form; (4) text.md exporter SCRATCH path still pointed at fr/ (sed miss) → fixed to es/;
  (5) VM restart SIGTERM'd the gates run during webpdf — completed steps verified fresh from logs,
  only webpdf + diff + text.md re-run.
- Run-gate lesson: Flow's end_report prints "ended col N/N y=NNNN (bottom MMMM)" WITHOUT the
  word OVERFLOW — the old TOO WIDE|OVERFLOW grep missed the P8-keys overflow on the first es run.
  The run gate must check every flow's end y against its bottom. fr/de build.logs re-checked the
  same way: all flows within bottom.
- Tool note (NOT fixed — p8.py off-limits): FOOTER_RE `LUCERNA|...` doesn't match the mixed-case
  "The Lucerna" footer, so the footer leaks into the last answer segment (key 150) for every
  edition; masked when key 150 is dash-style, bites when paren-style. Full note in the edition
  WEEKLY-KIT.md §10.
- Full record: `scratch-fanout-en/es/00-es-complete.md` (and the edition WEEKLY-KIT.md §8).

## it — COMPLETE, self-check zero issues

- Edition: `production/2026-w47/2026-w47-en-it/` (slug `2026-w47-en-it`)
- Print PDF: `The-Lucerna-VOL4-en-it.pdf`, 29,326,709 bytes,
  SHA-256 `195e155228e63515d3133a32cebbbee71c3dccf973387d4c1c2f614670e3da26`
- Web PDF: `The-Lucerna-VOL4-en-it.web.pdf`, 2,372,517 bytes,
  SHA-256 `995339d48612cc9344a5213e38026a9cda9a1de910efb268308fa9e877064a46`
- Gates: run exit 0, 0 overflow (all flows within bottom; P8-keys 2443/2560); occlusion 0 flags;
  p8 extract 60/150, compare CLEAN (keydiff 137–140, 150, expected); freeze direct sha256 8/8;
  print/web text diff 0/0; P8 min font 13.5 pt; badges = core on all 8 pages; text.md
  53,373 bytes, 150/150 keys; 8 cards visually checked after the final render, zero issues.
- Fixes in this round (each → rebuild + re-render + full re-gate): (1) P1 bridge size patch
  missed — my #189 used "Nota — " but apply.py's patch looks for the W46 it bridge label
  "Spiegazione | " → bridge would render at default 20.5pt instead of 19.5 → fixed #189 to
  the W46 it convention "Spiegazione | a midterm = …"; (2) text.md exporter SCRATCH path still
  pointed at es/ (same trailing-slash sed trap as es) → fixed, re-ran RC=0; (3) P8 key size
  pre-set to 13.5/1.26 on the es lesson (15.5/1.3 overflows for long-note Romance languages).
- Standing lesson for nl/ru/ja/ko/zh-tw: the P1-bridge label need NOT equal the gloss prefix —
  check the W46 P1-bridge label per language (it "Spiegazione | ", de "Erklärung | ");
  verify the bridge-size patch applied (no WARN in apply output) on the first build.
- Full record: `scratch-fanout-en/it/00-it-complete.md` (and the edition WEEKLY-KIT.md §5).

## pt — COMPLETE, self-check zero issues

- Edition: `production/2026-w47/2026-w47-en-pt/` (slug `2026-w47-en-pt`)
- Print PDF: `The-Lucerna-VOL4-en-pt.pdf`, 29,345,286 bytes,
  SHA-256 `50484ca9c0ef23231977066164281455491180ef7843efc8d266805cdcc5ce0e`
- Web PDF: `The-Lucerna-VOL4-en-pt.web.pdf`, 2,381,728 bytes,
  SHA-256 `c150c65509fa722ef17d54f0c823878c7f958fcca6aaaae879e10c36e7430071`
- Gates: run exit 0, 0 overflow (all flows within bottom; P8-keys 2443/2560); occlusion 0 flags;
  p8 extract 60/150, compare CLEAN (keydiff 137–140, 150, expected); freeze direct sha256 8/8;
  print/web text diff 0/0; P8 min font 13.5 pt; badges = core on all 8 pages; text.md
  53,549 bytes, 150/150 keys; 8 cards visually checked after the final render, zero issues.
- Fixes in this round: (1) Q150 colon → dash via lit_overrides (caught before the first build —
  the W46 pt TM value uses a colon, the es Q150 trap); (2) P8 key size pre-set to 13.5/1.26
  (es/it lesson); (3) SCRATCH path fixed at sed time (it lesson) — no text.md failure.
- Notes kept: "SPORT · Desporto" is the shipped W46 pt head (content34.py:96), not a defect;
  Q13 TM note "Segunda volta a 1 de dezembro" (European form) coexists with fresh "segundo turno"
  (Q21) — two source literals, both correct, kept like the fr/es Q136/Q105 pattern.
- Full record: `scratch-fanout-en/pt/00-pt-complete.md` (and the edition WEEKLY-KIT.md §5).

## nl — COMPLETE, self-check zero issues

- Edition: `production/2026-w47/2026-w47-en-nl/` (slug `2026-w47-en-nl`)
- Print PDF: `The-Lucerna-VOL4-en-nl.pdf`, 29,340,703 bytes,
  SHA-256 `5b2a364b60fb55372e2ceada5e19b48cbdaa6e14b3ef8872d6e75322eff18e05`
- Web PDF: `The-Lucerna-VOL4-en-nl.web.pdf`, 2,375,438 bytes,
  SHA-256 `f1d2b8f43600e39af4aa1677db61f84820bef07ee9b826828e28704c55a9d94c`
- Gates: run exit 0, 0 overflow (all flows within bottom; P8-keys 2375/2560); occlusion 0 flags;
  p8 extract 60/150, compare CLEAN (keydiff 137–140, 150, expected); freeze direct sha256 8/8;
  print/web text diff 0/0; P8 min font 13.5 pt; badges = core on all 8 pages; text.md
  52,965 bytes, 150/150 keys; 8 cards visually checked after the final render, zero issues.
- Fix in this round (→ rebuild + re-render + full re-gate): P2 SENATE box title
  "THE SENATE, IN NUMBERS　De Senaat" (text_w 413.0) overflowed its box and ended 6pt from the
  column-3 line "Second story of the week" — the occlusion audit does NOT flag title-to-neighbour
  text collisions (0 flags throughout). Shortened to "…　Senaat" (gap now 39pt, pixel-verified).
  Standing lesson: text_w under-measures U+3000 titles by ~15pt (true ink 428.5 vs text_w 413.0);
  pixel-check any title facing live text in the next column; shorten pre-emptively.
  Note: es's SENATE title (411.4pt) has the same ~6pt tightness and was left as "tight but no
  collision" — flagged here for the parent, not re-opened (es is complete).
- Full record: `scratch-fanout-en/nl/00-nl-complete.md` (and the edition WEEKLY-KIT.md §5).

## ru — COMPLETE, self-check zero issues

- Edition: `production/2026-w47/2026-w47-en-ru/` (slug `2026-w47-en-ru`)
- Print PDF: `The-Lucerna-VOL4-en-ru.pdf`, 29,241,566 bytes,
  SHA-256 `788cd0c08ec9b72fd52c8a65b4aadacb05e27980369295d7df0b726eb82efd70`
- Web PDF: `The-Lucerna-VOL4-en-ru.web.pdf`, 2,417,491 bytes,
  SHA-256 `da80486218d001cc6dc09e4107391cf81b15d1dde7f5c3b6d8e0aeb5f2ffe77a`
- Gates: run exit 0, 0 overflow (all flows within bottom; P8-keys 2460/2560); occlusion 0 flags;
  p8 extract 60/150, compare CLEAN (keydiff 137–140, 150, expected); freeze direct sha256 8/8;
  print/web text diff 0/0; P8 min font 13.5 pt; badges = core on all 8 pages; text.md
  61,835 bytes, 150/150 keys; 8 cards visually checked after the final render, zero issues.
- Fixes in this round (all pre-emptive, caught before the first build): (1) Q150 colon → dash via
  lit_overrides (es/pt lesson — W46 ru TM value uses a colon); (2) P8 key size pre-set to
  13.5/1.26 (es/it lesson); (3) SENATE title pre-shortened to "Сенат" (nl lesson); (4) SCRATCH
  path verified at sed time (it/nl lesson). No rebuild was needed after the first gates.
- Note kept: "H　WRITING　Письмо [B1]" is the shipped W46 ru head (content8.py:131) — kept as-is.
- Full record: `scratch-fanout-en/ru/00-ru-complete.md` (and the edition WEEKLY-KIT.md §5).

## ja — COMPLETE, self-check zero issues

- Edition: `production/2026-w47/2026-w47-en-ja/` (slug `2026-w47-en-ja`)
- Print PDF: `The-Lucerna-VOL4-en-ja.pdf`, 41,509,526 bytes,
  SHA-256 `5cfb282caa800c343435639ee1b54a325f7d902e4fa6a3c53f2bc4e1374aa63c`
- Web PDF: `The-Lucerna-VOL4-en-ja.web.pdf`, 2,843,624 bytes,
  SHA-256 `f20c1affd5a53ab23dd8619715dfa86f72c3c6322c0faf5f8daf4c0b4cc7eabb`
- Gates: run exit 0, 0 overflow (all flows within bottom; P8-keys 2205/2560); occlusion 0 flags;
  p8 extract 60/150, compare CLEAN (keydiff 137–140, 150, expected); freeze direct sha256 8/8;
  print/web text diff 0/0; P8 min font 13.5 pt; badges = core on all 8 pages; text.md
  52,982 bytes, 150/150 keys; 8 cards visually checked after the final render, zero issues.
- Print PDF 41.5 MB is the CJK-font-embedding scale (core-en print PDF is 41.4 MB); web PDF
  2.84 MB < 7 MB. Freeze added CJK 2,096 chars = the Japanese layer itself (hiragana-heavy);
  0 leftover Simplified Chinese strings verified in the SVGs.
- Fix in this round (→ rebuild + re-render + full re-gate): P4 gloss used full-width colons
  ("a Test：…") while every other gloss uses "=" — fixed to "=". Anchor typo also caught by
  build_map at the start (Japanese 勝/輪 in the anchor instead of source 胜/轮) — anchors must be
  copied character-for-character from the source literal.
- Full record: `scratch-fanout-en/ja/00-ja-complete.md` (and the edition WEEKLY-KIT.md §5).

## ko — COMPLETE, self-check zero issues

- Edition: `production/2026-w47/2026-w47-en-ko/` (slug `2026-w47-en-ko`)
- Print PDF: `The-Lucerna-VOL4-en-ko.pdf`, 32,386,030 bytes,
  SHA-256 `983ad19cbd400836a465b9592d9a866597d5476b39a0a36a3c8e6ea9e6834c18`
- Web PDF: `The-Lucerna-VOL4-en-ko.web.pdf`, 2,594,367 bytes,
  SHA-256 `e2439e78fc3d551503b7222ed740f2868eba415bddaa960a1fd47d06a126907a`
- Gates: run exit 0, 0 overflow after the P2 fix (all flows within bottom; P8-keys 2205/2560;
  P2-ex 2532/2560); occlusion 0 flags; p8 extract 60/150, compare CLEAN (keydiff 137–140, 150,
  expected); freeze direct sha256 8/8; print/web text diff 0/0; P8 min font 13.5 pt; badges =
  core on all 8 pages; text.md 52,965 bytes, 150/150 keys; 8 cards visually checked after the
  final render, zero issues.
- Fix in this round (→ rebuild + re-render + full re-gate): P2-ex FLOW OVERFLOW (y=2946/2560)
  on the first run — the only overflow in the whole fan-out. Root cause: the W46 TM B bridge
  wrapped to 2 lines; one early extra line cascaded through the 4-column flow packing and
  `match_set`'s keep-together _fit(362) clamped the D block to the page bottom (333pt dead gap).
  Fixed via lit_overrides → 1-line bridge; re-run P2-ex ends 2532/2560 (same as ja).
- Incident: VM restart SIGTERM'd the gates run at ~05:25 (text.md step never ran, /tmp log wiped).
  Recovered the es way: completed steps verified from artifacts; re-ran only direct-sha (8/8),
  print/web diff (0/0), print SHA/size, text.md (RC=0, 150/150).
- Standing lesson for zh-tw: verify every reused TM bridge fits on ONE line — a 1-line excess
  early in a 4-column flow cascades; check the P2-ex flow end on the first run.
- Full record: `scratch-fanout-en/ko/00-ko-complete.md` (and the edition WEEKLY-KIT.md §5).

## zh-tw — COMPLETE, self-check zero issues

- Edition: `production/2026-w47/2026-w47-en-zh-tw/` (slug `2026-w47-en-zh-tw`)
- Print PDF: `The-Lucerna-VOL4-en-zh-tw.pdf`, 38,152,082 bytes,
  SHA-256 `d2e919473d70463a00b3be10129bfecbd3c1a9137b0ae4ab0cf8ca2bdea78e07`
- Web PDF: `The-Lucerna-VOL4-en-zh-tw.web.pdf`, 2,927,283 bytes,
  SHA-256 `df41f1fc1a6786b839c63fdd53ecec1fdecba57a19ddf7c274a679762f421545`
- Gates: run exit 0, 0 overflow after the P2 fix (all flows within bottom; P8-keys 2137/2560;
  P2-feature 1528/1540, 12pt spare, visually clean; P2-ex 2532/2560); occlusion 0 flags;
  p8 extract 60/150, compare CLEAN (keydiff [137, 138, 139, 150] — 140 is script-identical,
  expected); freeze direct sha256 8/8; print/web text diff 0/0; P8 min font 13.5 pt; badges =
  core on all 8 pages; text.md 50,505 bytes, 150/150 keys; 8 cards visually checked after the
  final render, zero issues.
- OpenCC s2t gate (this edition only): registry.json + text.md convert to themselves with
  0 differences — zero Simplified characters in the deliverables.
- Fixes in this round (each → rebuild + re-render + full re-gate): (1) P2-ex FLOW OVERFLOW
  (y=2946/2560, same as ko's first run) — W46 TM B bridge wrapped to 2 lines; fixed via
  lit_overrides → 1-line bridge; (2) Simplified 布 in the Q2/Q95 registry notes
  ("宣布競選結果", a W46 TM conversion gap) — fixed via lit_overrides → "宣佈競選結果";
  OpenCC re-check clean. Process slip: the first override edit replaced the lit_overrides
  dict instead of merging, dropping the B-bridge fix — the re-run overflowed again (2946) and
  caught it; both overrides verified present in map-zh-tw.json before the final apply.
- zh-tw mechanics: 216 misses (11 more than the other languages — 8 script-identical lit +
  3 script-identical type/instr, all needing identity mappings because the TM stores differing
  pairs only); calendar/numbers box follow the W46 zh-tw English+Traditional-gloss pattern.
- Full record: `scratch-fanout-en/zh-tw/00-zh-tw-complete.md` (and the edition WEEKLY-KIT.md §5).
