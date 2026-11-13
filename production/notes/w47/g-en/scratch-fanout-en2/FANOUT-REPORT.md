# FANOUT-REPORT — W47 English family re-fan-out (2026-11-11)

**Scope:** rebuild all 10 English-target reader editions (`2026-w47-en-{de,es,fr,it,ja,ko,nl,pt,ru,zh-tw}`)
from the fixed core-en, apply each edition's fix1 (proof1 edition-level defects), run all gates, update
each KIT. **No commit, no push.** Core-en was not touched (fixed core: print 41,407,278 B
`b484e007…`, web 2,804,271 B `7277e32a…`, text.md 51,405 B `e368828a…`, re-proof (a) passed).

**Scratch:** `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-en2/`
(`fanout/` = patched maps + `apply.py` + per-lang dirs + build-gates logs; `backup/` = the 10 old
edition dirs, 518M; `abstracts/` = 10 new ABSTRACTs). Backups of the old editions are in `backup/`.

**Mechanism (verified before use, not guessed):** `fanout/apply.py` (from the old `scratch-fanout-en/`
round, SCR repointed) copies core-en py files + assets + registry.json into the edition dir, then
rewrites the explanation layer from `map-<lang>.json` (AST role-aware literal replacement). It
`shutil.rmtree`s the edition dir first — KIT.md, ABSTRACT.txt, text.md, PDFs, SVGs, cards are deleted
and restored/rebuilt after each apply. `build_lang.sh <lang>` runs run.py → render.py → dump_reg.py →
occlusion_audit → p8 extract (core + edition) → p8 compare → keycheck_ed → freeze baseline → freeze
diff → webpdf → print/web text diff → make_textmd → check_s11 → boxtitle sweep (source) → svg
boxtitle sweep → creambox → verify_ed. `sweep_svg_titles.py` was hardened in this round: a box title
must start within 60px of its rect's left edge; a word starting at/after the rect's right edge is not
a title (the it SAY IT glossary false positive). Full mechanism notes + per-lang gate logs:
`scratch-fanout-en2/fanout/<lang>/build-gates.log`.

**Core fix1 (9 items, in `hidden_files/w47/scratch-fix-core-en1/FIX-LOG.md`, carried by the rebuild
into every edition and verified per edition — not assumed):** Q39→a, Q40→d (keys `["b","a","d","c"]`,
notes mentor=a, arena=d); P1 SEARCHES box 92→86px; P2 DID YOU KNOW offset 62→89; `已确认`→`已宣布`
everywhere; Ashes P4 fully rewritten as 2025–26 retrospective (Australia won 4–1; 1st Test Fri 21 Nov
2025 Perth; next Ashes England 18 Jun–2 Aug 2027; Q46 new stem/key A; Q52 hosts→hosted; Q55 sold→won;
Q125 key A "4–1"; "Perth is winning!"→"Arsenal are winning!"); P7 NEXT WEEK rewritten; box titles
SENATE→"SENATE IN NUMBERS", SATURDAY→"SATURDAY, NOV 21"; SAY IT middle panel widened to w=380.
**Registry is hand-maintained, not transform-derived** — each edition needed its own fix1 + registry
re-dump; the core fix did not propagate.

**Map patch (`fanout/patch_maps.py`, 11 Nov):** 14 real new literals per lang (Q39/Q40 keys + notes,
Q46/Q52/Q55/Q125 notes, SATURDAY/SENATE titles, P1 strip, Q7/Q82/Q83/Q84 notes, P6 bridge; Q46/Q125
notes fresh per-lang translations; `已宣布` word swaps; es arena fixed "arena = la arena d"; it arena
fixed "l'arena d"). Edition-level map fixes folded in: fr B2 "encore" removed; ko ODD gloss → "숫자로";
ja HAYMITCH → "ヘイミッチ戦", ODD → "数字で", D6 instruction → "現在進行形で書きかえよう。";
es HOW LONG? gloss → "Duración"; ru HAYMITCH → "Игры"; nl 4 guillemet values « »→" "; de two proof2
strings (remove "(gewinnt immer wieder)" from the Win gloss; remove "für Geschehenes" from the
past-simple gloss — these live only in the on-disk edition files). Nested map structure: patches must
use nested key access (`m['lit'][k]`), flat iteration silently matches nothing (learned on the it map).

**ABSTRACTs:** all 10 rewritten to the full form (announced results; certification 10 Nov–18 Dec;
16 Nov Anti-Bullying/Odd Socks; 20 Nov Children's Day + Hunger Games; 21 Nov Premier League back +
Turin ATP final + Ashes 4–1 look-back; reader language; A2–B2; 150), no ASCII double quotes. it/nl/pt/
ru/zh-tw old ABSTRACTs were short-form (§9-class violations their proof1s had not flagged) — fixed
consistently with ja D4 / ko D3.

**Gate invariants (all 10 editions, final build):** run.py exit 0, 0 OVERFLOW / TOO WIDE, TOTAL 150,
MODEL 82; occlusion 0 flags; p8 extract noted set 60/150 = core; p8 compare CLEAN, keydiff =
[137, 138, 139, 140, 150] except zh-tw [137, 138, 139, 150] (key 140 "打破沉默。" is script-identical
in Simplified/Traditional, so it does not differ from core — by identity, not error); keycheck
registry-vs-p8extract 149/150 exact + n=150 short-label exception; registry keys vs core 145/150
(diffs only 137–140, 150); freeze baseline 8/8 byte-identical; freeze diff TOTAL added CJK 9 for
Latin/Cyrillic editions (all U+3000); print/web token-multiset diff 0, per-page byte-identical 8/8;
check_s11 ALL PASS; source boxtitle sweep 12/12; SVG boxtitle sweep 18/18; creambox all inside-only
clearances positive; P8 min PDF font 10.12pt ≥ 9.75pt; SVG zero real CJK (Latin/Cyrillic).
`verify_ed.py` per edition: Q39/40 keys + notes (incl. estadio/stadio check), Q46/52/55/125 keys +
notes, no stale Ashes phrasing in registry, text.md answer checks, SAY IT panel widths, P8 min font,
zero real CJK in SVGs. No `FAIL` line in any of the 10 build-gates logs.

## New SHAs (print / web / text.md)

| lang | print SHA-256 (bytes) | web SHA-256 (bytes) | text.md SHA-256 (bytes) | chars |
|---|---|---|---|---|
| de | `fe02ab1d9ba41e7a22651be02bda3612b66b54f2c521e12ab0ab5ca6797be5e1` (29,331,212) | `19e166e03f28e813a8418189f20c1ddd31635f6621fbb182268e552c5302e6e5` (2,414,462) | `0aad0d2c8118bd6dab2f08170425f8ada595b5a397ba0d77511cffdd12c1e5e1` (52,568) | 47,406 |
| fr | `76b4522c53a2fcad0a92f9b02180ff353dc73845ce57080cb7c1d2b0d263dd2f` (29,330,979) | `dd68f929b86af917626769bb52cad6ba34a0b6fe4e959a43279de4e319f83266` (2,413,670) | `2d832a170a229817af36c1c5378db7ef2030abd54bec54ab5cf019a6f0364855` (53,809) | 48,076 |
| es | `6341e239942338c547cfff31d96b4d6b0ad5b4ad811164380995959ea210b4a5` (29,331,231) | `73356781d8c02970f18e592ef60189891db128eb38cabb04442e1919ee725b97` (2,414,448) | `2539179917d985e6da78c36be288946865af6b8aa8599c3e532e44e262921e2d` (54,388) | 48,258 |
| it | `bdfe23784024bb85635eb2984dd3c530c2db63aff1b7c102bc08b78b40d7b61c` (29,327,190) | `d5e9c1af0880237350b4364d8a4be478673d87d249cd614f334849c969618e58` (2,408,886) | `433c2aec5b303a5968e535c83b38e6b30128c1b5a2318fb0fa44466f00dbb15e` (53,947) | 47,991 |
| pt | `3f6b415fa35195ca49605414b5a756a01f0457032cc5c6acc75075e49c221dad` (29,345,708) | `0252edc42a4981413c25067e8ed60bb5069994f86c10a4d25a0b8483e0846629` (2,418,233) | `12b04ff13b12db5232d3114816f287c2d72a69df164e0273269409ef3148d545` (54,123) | 47,926 |
| nl | `a5957d64e727662c0d4763596af517f0eae324471b93a4bd9dadb304c03bc136` (29,341,272) | `ee3d98baba20febe72c297ccb2591055991d4ed9b341b1429b6c7748b3371193` (2,411,538) | `baecaf6e92ff837857e3d6d7dd7ae28f2b1fbb15b8be78bec9428a83c13be459` (53,568) | 48,044 |
| ru | `daf81d35cdf44e66dffaed2f2ab68da66251742a1be02cb1af95f8daeed9cdaf` (29,241,701) | `3fb58ae2e80f16460e7da5f5973cc5eb9ffc2687579b6fd88fb2d9eef41674fe` (2,452,739) | `d59c98c0676f74352ce81557598641b91d4d17a4d033dbdd22e775199f0bbcf7` (62,395) | 47,655 |
| ja | `9f9faaea18807551394977ef536d142da65cfda78b73aa91d807063c0c4b0428` (41,509,391) | `25645767641d06f1bfdc25f9437eb5c7f3ce0c319612eaabc9e912353f756f49` (2,883,877) | `219ce22d549887f0ca6895a928206ac18b255686e8f50f07296c54cd33d48aa9` (53,588) | 43,475 |
| ko | `ecad215eb3f5ab98e6d50a7fd5ea5b383902c8f1ea0aadd3bff1fb28822072cd` (32,386,301) | `5115ad3f586bbb94226ad841bbfeedd31fa80eecc7ee6cf4a9296d43ccc9ca9e` (2,629,426) | `e5633ac3569d216ce5e7f0578af3ab0c920fa964c77636fd2c7954a3a05484ac` (53,590) | 43,897 |
| zh-tw | `7641031186c77653ac1263056a968ba7ce2ffb9383716c5a35cfad798e0fc334` (38,152,350) | `e07e5dd048dad9ab1ed42daa6d33c2e9f0dea129538b957c06afe25627e0d177` (2,965,191) | `57cb886738e8e23d79abe531e1f03ee7372560c5020ff02d4d6997ea117651b3` (51,147) | 42,852 |

Freeze added CJK: de/fr/es/it/pt/nl/ru 9 (all U+3000); ja 2,084; ko 2,323 (Hangul 2,309/2,323 = 99.4%,
U+3000 9); zh-tw 775.

## Per-edition fix1 completion

- **de (2 builds) — DONE.** Proof2 (a) voided by Q39/40 + Ashes staleness; rebuilt + fix1. KIT §2/§3/§4/§5/§8/§9
  updated. New defect found by this round (pre-existing, de proof rounds missed it): P3 HAYMITCH title
  "HAYMITCH'S GAMES　Haymitchs Spiele" 443.6px, −39.1px (identical in backup SVG) → map "Spiele"
  (317.5, +87.0). Second build was interrupted by a VM restart during webpdf — recovered by verifying
  completed steps from logs/artifacts and resuming webpdf-onward only, no step repeated blindly.
  Tight-but-passing: P2 AND YOU? box last line baseline clearance +5.0px; the 0.30×size descender
  heuristic flags −1.0px, but the rendered card crop shows the line (incl. its `g` descender) fully
  inside the cream — heuristic false alarm, no fix. Visual: P3/P4 cards clean; P1 SEARCHES last
  baseline +12.0, P2 DID YOU KNOW +14.3.
- **fr — DONE.** D5 "encore" removed (0 hits in rebuilt source; B2 now "Personne ne sait si le
  décompte va changer."). D1–D4 core-level resolved by rebuild. Visual: P7 toolbox + NEXT WEEK clean.
  KIT §8 line 91's old-title history kept as history.
- **es — DONE.** D3 HOW LONG? → "Duración" (262.2px). Q40 registry note corrected "arena = la arena d"
  (fixes the estadio=stadium error — same error class as it). Visual: P6 crop "HOW LONG?　Duración"
  fits inside the cream box.
- **it (2 builds) — DONE.** D1–D2 core-level. First fix attempt — widening SAY IT box3 panel to w=340 —
  put the panel's right edge at x=1370, exactly where the SAY IT glossary column starts
  (`lx = 1370` in content12.py), so glossary words sat flush against the cream with 0px gutter (caught
  on the P2 card crop; the SVG title sweep also flagged it as an apparent −106.6px overflow, which
  exposed the crowding). Not a title overflow — a real layout collision. **Fix chosen: shorten the
  sub, not the panel** — map value `感恩节快乐！` → "Buon Ringraziamento!" (208.2px, 35.9px/side in
  the default 280 panel); the w=340 edit was reverted by the re-apply (apply.py re-copies content12.py
  from core). Second build all green; P2 card re-checked clean. The sweep was hardened the same way
  (see Mechanism). The it arena note was the same error class as es (`lo stadio` wrong) → `l'arena d`.
- **pt (2 builds) — DONE.** D1–D2 core-level. New defect found by the sweep (pre-existing, pt proof1
  missed it): P5 ODD SOCKS title "ODD SOCKS, IN NUMBERS　Números" 414.7px, −10.2px (identical in
  backup; the old KIT's claimed 397.2 was mis-measured) → "N.º" (346.2px, +58.2; standard Portuguese
  abbreviation); only `svg/p5-youth.svg` changed vs the first build. Tightest: HOW LONG? +8.9 advance,
  +8.5 true ink. Visual: P5 crop clean.
- **nl — DONE.** D4 fixed in the map: 0 « in rebuilt content*.py, registry.json, text.md, all 8 SVGs;
  the 4 spots now read e.g. Q65 `Het thema dit jaar is "Doorbreek de stilte"`, Q126
  `Thema van de Week tegen Pesten: "Doorbreek de stilte"`. Note: the core fix changed the SENATE title
  to "SENATE IN NUMBERS" (the old nl §5 "THE SENATE, IN NUMBERS　De Senaat" fix is superseded); rebuilt
  title "SENATE IN NUMBERS　Senaat".
- **ru — DONE.** D4 fixed by post-apply code edit in `content12.py` — `phrase_panel(299, …, w=420)`
  (panel 89–509; 51px gap to middle panel at 560 is empty margin at that y). RU line1 "Подсчёт голосов
  всё ещё продолжается." 394.5px now fits; RU line2 360.6px fits the core-widened w=380 middle panel.
  Verified on the P2 card: all three Russian subs inside their panels; glossary gutter intact (panel 3
  ends 1340). D5 fixed in the map: P3 HAYMITCH → "Игры" (309.6px, +94.9); P4 SATURDAY fixed by
  core's shorter "SATURDAY, NOV 21" — rebuilt "SATURDAY, NOV 21　Суббота" 328.9px (+75.6).
- **ja (2 builds) — DONE.** D4 ABSTRACT rewritten to full form; D5 HAYMITCH → "ヘイミッチ戦" (385.4px,
  +19.1); D6 instruction → "現在進行形で書きかえよう。" (single line on rebuilt P5 SVG, baseline
  y=2543.95, above footer rule). Two NEW defects found by the sweep (pre-existing, ja proof1 missed
  them, same class as ko D3): P5 ODD SOCKS "数字で見る" 426.9px, −22.4 → "数字で" (≈357.9px); P6
  "A PRACTICE BALLOT　練習用投票用紙" 407.9px advance, −3.4 (true ink −3.5px — a real overflow, not
  rounding) → "投票用紙" (338.9px, +65.6). Both fixed in `map-ja.json`, full rebuild + re-gate.
  Tightest: THE WEEK IN NUMBERS +1.5 advance, +1.5 true ink — genuinely tight but inside, recorded,
  no fix. **KIT §3 freeze corrected to re-measured 2,084** (old KIT's 2,096 was the pre-rebuild count;
  2,092 was the first build of this round before the A PRACTICE BALLOT title fix; new histogram top-5:
  の 81, は 74, い 59, を 55, で 52). No leftover Simplified Chinese re-verified on rebuilt text.md: 0
  hits for 中期选举/众议院/民主党赢下/参议院/星期五/金句/范文 etc.
- **ko — DONE.** D3 ODD SOCKS → "숫자로" (375.4px, +29.1). Old ABSTRACT short-form rewritten to full
  form. Tight-but-passing recorded: P3 HAYMITCH "헤이미치의 경기" 401.9px (+2.6 advance, +2.5 true
  ink) — genuinely tight but inside, no fix. The §5 item 1 P2-ex bridge fix
  ("will + 동사로 바꿔 쓰세요(약속)。") survives the rebuild (lives in the map) — P2-ex ends 2532/2560
  as before.
- **zh-tw (2 builds) — DONE.** All 9 defects core-level, zero edition-level. Diff vs backup `<` lines
  all expected old versions (old P1 strip, Q7/Q46/Q82–84 已確認 forms, P6 bridge "已確認數").
  **New issue found and fixed by this round's OpenCC s2t self-check (first build):** the 6 new 已宣布
  literals came through the map as 已宣布 with 布 — s2t flagged 4 diffs in registry.json, 6 in
  text.md, 5 in the SVGs, every one 布→佈 in 已宣布. 布 is not a Simplified leak in the strict sense
  (宣布 is standard Traditional too), but this edition's own precedent (KIT §5 item 2) writes 宣佈
  with 佈, and the §3 script gate requires 0 s2t differences — so the 6 map values were patched
  宣布→宣佈 (P1 strip, Q7/Q82/Q83/Q84 notes, P6 bridge), full rebuild + re-gate. Re-check after the
  rebuild: registry.json, text.md and all 8 SVGs convert to themselves with **0 differences**; 宣佈
  13× in text.md, 9× in registry.json; 宣布 0× anywhere. (The `opencc` CLI binary is not installed on
  this VM; the check used the Python `opencc` package in the repo venv, `OpenCC('s2t')`.)
  Visual: P1 card clean — strip "期中選舉　已宣佈結果　詳見第6版"; IN BRIEF "ASHES — A year ago:
  Australia beat England 4–1 in the 2025–26 Ashes. (p. 4)"; SEARCHES box contents inside the cream.
  KIT §5 items 4–5 added (§2 SHAs/sizes, §3 freeze 775 + script gate, §4 SENATE/SATURDAY titles,
  §6 P4 Ashes note, §8 map path → `scratch-fanout-en2/fanout/map-zh-tw.json`, §9 build record →
  `scratch-fanout-en2/fanout/zh-tw/`).

## New defects found by this round (not in any proof1)

1. **de P3 HAYMITCH title −39.1px** (pre-existing; de proof rounds missed it) → "Spiele".
2. **pt P5 ODD SOCKS title −10.2px** (pre-existing; pt proof1 missed it; old KIT's 397.2px was
   mis-measured) → "N.º".
3. **ja P5 ODD SOCKS title −22.4px** (pre-existing; ja proof1 missed it) → "数字で".
4. **ja P6 A PRACTICE BALLOT title −3.4px** (pre-existing; true ink −3.5px, a real overflow, not
   rounding) → "投票用紙".
5. **it SAY IT box3 layout collision** (w=340 panel vs glossary at x=1370, 0px gutter — caught on the
   P2 card, not by the sweep's number) → shorten the sub to "Buon Ringraziamento!"; sweep hardened
   (title must start within 60px of its rect's left edge; a word at/after the rect's right edge is not
   a title).
6. **es + it Q40 arena notes** (estadio/stadio = stadium, wrong) → "la arena d" / "l'arena d".
7. **Short-form ABSTRACTs** in it/nl/pt/ru/zh-tw (SOP §9-class, proof1s didn't flag them) → all 10
   rewritten to full form.
8. **zh-tw 已宣布 vs 宣佈** (s2t self-check, first build) → 6 map values patched to 宣佈; re-check 0
   differences.

## Tight-but-passing (genuinely tight, inside, recorded no-fix)

- de P3 HAYMITCH "Haymitchs Spiele" after fix: +87.0 (was −39.1). de P2 AND YOU? last line: baseline
  clearance +5.0px; descender heuristic −1.0px false alarm (card crop verifies the `g` descender fully
  inside the cream).
- ja P3 HAYMITCH "ヘイミッチ戦": +19.1. ja THE WEEK IN NUMBERS: +1.5 advance / +1.5 true ink.
- ko P3 HAYMITCH "헤이미치의 경기": +2.6 advance / +2.5 true ink.
- pt HOW LONG?: +8.9 advance / +8.5 true ink.

## Mechanism / process notes

- `map-de2.json` is a flat lit-only extract with OLD values — ignore it; the maps are NESTED
  (`{"lit": {...}, ...}`).
- The `de` second build was interrupted by a VM restart during webpdf; recovery = verify completed
  steps from logs/artifacts, resume webpdf-onward only — no step repeated blindly.
- When a KIT updater script's `rep()` assert fails, nothing is written (write happens at the end) —
  re-run the whole updater with the corrected string; check exact line wraps with grep first.
- `TMPDIR` = scratch `.../scratch-fanout-en2/tmp` throughout (`/tmp` is 512M and often full).
- No commits, no pushes made in this round. The `en` website-cover entry (cover.json does not exist
  yet) must use the Ashes retrospective wording.
