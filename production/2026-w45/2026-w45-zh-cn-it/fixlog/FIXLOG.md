# FIX LOG — W45 ZH-CN × IT (independent proof round, verdict NOT PASS → fix)

Fix agent run 2026-10-28. NOT a finalization: a full independent reproof follows (SOP §8.4).
Proof report: `hidden_files/w45/zh-cn-it-proof/REPORT.md`. Only the two blocking items
below were touched; all settled proof items were left alone; `tools/tables.json` untouched;
`~/workspace/weekly-git`, `insert.py`, Discord, main-chat delivery, crons, shared scratch
dirs untouched. No subagent spawned. All commands with `tools/venv/bin/python`.
No content module was ever imported inside the core build dir.

## Pre-flight (coordinator ruling: intent = NO CONCURRENT WRITER)

- (a) No live worker/process writing to the delivery/build dirs (only unrelated
  zh-cn-es / zh-cn-de / zh-cn-nl workers running; none touch the it dirs).
- (b) mtime snapshots of both dirs a few minutes apart (snap1 ~08:00 UTC, snap2
  08:03 UTC, fixlog itself excluded): ZERO changes.
- (c) Proof session completed: REPORT.md filed before this fix started.
- Pre-fix hashes recorded in `fixlog/prefix-hashes.txt` BEFORE any change (table below).

## B1 — P8 key 135 note was English, now Italian

- OLD (delivered P8 SVG + card, verbatim):
  `135. 数字 (shùzì — the AI film's characters are digital images.)`
- NEW (delivered P8 SVG, verbatim):
  `135. 数字 (shùzì — i personaggi del film AI sono immagini digitali.)`
- Mirror evidence (ex 70, P5): build `content56.py:81` and the delivered P5
  exercise read `shùzì — i personaggi del film sono immagini digitali.`; the
  proof report confirms the same. The B1 form inserts `AI` after `film`
  (the AI variant of the same clause) and keeps the paren style
  `数字 (shùzì — [Italian clause])`, the confirmed zh-cn×IT P8 family style.
- Root cause as diagnosed by the proof: `scratch/transform.py` mapped only the
  P5 form (`the film's characters…`, ex 70) and missed the P8-key `AI` variant
  (`content8.py:62` in the pre-fix build).
- The fix is a mapping INSIDE `scratch/transform.py` (phase 1, right after the
  ex-70 mapping), NOT a post-hoc direct edit — Gate 10 below proves it.
- Fit: final render log shows ZERO FLOW OVERFLOW / HEAD TOO WIDE warnings.
  P8 text-node diff pre-fix → post-fix: 330 nodes both, exactly ONE changed
  node (key 135). Key 135 y = 2059.70 in both; neighbours 134 (2030.47) and 136
  (2088.93) unchanged — zero reflow. Last key line unchanged (key 150 ends
  y = 2528.98, footer rule 2580, ~45 px clear per the proof's card adjudication).

## B2 — Gate 10: fix layer folded into scratch/transform.py

The diff of the proof's transform-solo repro build vs the it-build was
enumerated FIRST and matched the proof's itemization exactly — no MORE edits
than the proof listed, so folding proceeded (per the task's stop condition):

- Phase 2a, 11 short-form literals (4 box-title shortenings + 5 band re-titles
  + P6 head shortening + P7 disclosure rewrite):
  - `数字看本周 · I numeri di questa settimana` → `数字看本周 · Numeri della settimana`
  - `本周生活小日历 · Le date di questa settimana` → `本周生活小日历 · Date settimanali`
  - `生活 · Life` → `生活 · Vita`
  - `文化 · Culture` → `文化 · Cultura`
  - `看比赛的中文 · Parole per la partita` → `看比赛的中文 · Parole per la gara`
  - `这一周的高频词 · Parole della settimana` → `这一周的高频词 · Parole settimanali`
  - `青年 · Youth` → `青年 · Giovani`
  - `深读 · Deep read` → `深读 · Lettura approfondita`
  - `C · 练习篮子算一算 · Calcoli con i cesti` → `C · 练习篮子算一算 · Calcoli`
  - `词语 · Language focus` → `词语 · Focus sulla lingua`
  - P7 disclosure (long Chinese + short-Italian-note form) → full Italian
    disclosure ending `…mandateci le vostre lettere in cinese, le pubblicheremo!`
- Phase 2b, 34 pinyin-discipline literals copied verbatim (bare literals) from
  `scratch/pinyin_fix.py` (Han citations → pinyin-only inside P8 notes).
  Verification: applying 11 + 34 to the proof's repro-build copy left a diff
  vs the it-build of ONLY the OUT path line (see `fixlog/foldcheck/`).
- Why two phases: phase-2 old strings are phase-1 OUTPUTS (Italian text with
  Han citations), so they cannot live in phase 1 — a single longest-first list
  would zero-match-abort on them (e.g. the pinyin old `I vestiti vogliono 件,
  non 个 o 条.` is longer than, and only exists after, its phase-1 source).
  `main()` therefore runs phase 1, then 2a, then 2b, all in memory, each with
  the same zero-match abort; files are written only on APPLY. All splices are
  exact unique literals (tools README #17); no AST byte-offset splicing, no
  repr literals (#18). `scratch/pinyin_fix.py` is retained for history but is
  no longer needed for reproduction.
- The it-build content files were re-synced from the fixed-transform output
  (OUT repointed to the delivery dir), so `run.py` in the it-build now
  reproduces the NEW delivered SVGs as well.

## Change set (verified exactly)

- P1–P7 SVGs and cards: BYTE-IDENTICAL to pre-fix (hashes in the table below).
- P8 SVG + P8 card + both PDFs: differ ONLY via the key 135 note change
  (zero reflow, see B1). Nothing else differs — any other difference would
  have meant a wrong fold; none occurred.
- ABSTRACT.txt and all furniture strings unchanged.

## Gate 10 re-run (fresh core copy + fixed scratch/transform.py alone)

- Fresh copy of `hidden_files/weekly-report-w45-zhcn-build/` + fixed
  `scratch/transform.py` at `<copy>/scratch/transform.py`, work in
  `fixlog/gate10/` + `fixlog/gate10-out/svg/`. Core build dir never imported
  or executed in place.
- Exit codes, all honest: transform count-only exit 0; transform apply exit 0;
  single-process `run.py` exit 0.
- Counts: phase 1 = 276 mappings / 423 replacements (proof's old apply total
  was 422; +1 = the new B1 mapping); phase 2a = 11 entries / 11 replacements;
  phase 2b = 34 entries / 39 replacements (multi-hit entries: jiǎozǐ ×3,
  bǔdōng / Le famiglie / 直降-significa ×2 each); TOTAL 473.
  (Count mode now reports true sequential counts, not the old double-counted
  434: the old count-only pass did not apply replacements in memory, so
  substring-overlapping olds were counted twice.)
- Result: gate10-out SVGs 8/8 byte-identical to the NEW delivered SVGs,
  ZERO HEAD TOO WIDE / FLOW OVERFLOW warnings (registry TOTAL 150,
  A2 56 / B1 69 / B2 25, pages 10/18/18/18/18/18/12/38, writing model 172 chars).
- The delivery render itself (it-build `run.py` → delivery dir) also exited 0
  with registry 150 and 0 warnings, and produced the same P8 hash as gate10-out.

## Mechanical gates re-run on the new render

- Occlusion audit: `--selftest` OK (all 6 planted classes fire, clean controls
  silent); edition 0 flags; core 0 flags; NEW vs core 0 (`fixlog/occlusion.json`).
- `p8.py compare` vs core: core 150 noted, edition 150 noted, status CLEAN,
  missing=[] extra_count=0 uncertain=[] keydiff=[] (`fixlog/p8.json`).
- Gloss counts (split on `·`): core 10 calls / 33 items = it-build 10 calls /
  33 items.
- Registry (final render log `fixlog/final-run.log`): TOTAL 150, 0 warnings.
- P8 header claim "Tutte le note in italiano" now true: pre-fix → post-fix P8
  text-node diff = only key 135 changed; the proof's scope check established
  every other note as Italian (only #94, pure maths `199 − 20 = 179 yuan.`,
  was identical to the core besides #135); the new #135 note is Italian; a
  distinctive-English-word scan over the joined text of all 8 new SVGs
  returns NONE on every page, and the old English #135 string is absent.

## Hash tables (SHA-256)

### Pre-fix (from fixlog/prefix-hashes.txt, recorded before any change)

| file | SHA-256 | size |
|---|---|---|
| svg/p1-touiban.svg | 83cd4e7fb40b27add191e7b524b706a6672c55224dd4f2bc02415ddced799834 | |
| svg/p2-shenghuo.svg | 58a9dedb927f54c9553c574e390bb10f35c1dc16708ab046fbd12d115283956d | |
| svg/p3-wenhua.svg | b7ac0f6c075771422fb1f6330d987a7c626ce8909b8c0f5f4da51bc60c211954 | |
| svg/p4-tiyu.svg | add1a18620a466d5a3d11c548943b8927cde69fce691136828b6341802312bc9 | |
| svg/p5-qingnian.svg | 4940dcfe13a0b857c570ae1aaf3a416cf02eedca8e804abf1f3d3abba8fee716 | |
| svg/p6-shendu.svg | d3867195bf16f47843a8c202063e7d3a21b6d0ae846475214c585efdea7e3604 | |
| svg/p7-ciyu.svg | 4dace51163554551b8c5fbd955da6276cf616695bc1554eb11b99c9b25806e3a | |
| svg/p8-ceyan.svg | d4f4cb95ca3f33b1b5f5b13cc8cc578467747de8755facf3210685ab6297e3d3 | |
| cards/p1-touiban.png | 687cc28af01d9e4e0dbbecf18c6913d7897e962e7a4ad40c771aaf8497cb6720 | |
| cards/p2-shenghuo.png | 45779f78d954f7792723c4bd46a963ea4bd407ffcfd724ecfadb390cdb0ee7d6 | |
| cards/p3-wenhua.png | b9b43b26569127910b3619e7e96742801fbd00abed38bac6bcd186a0bc520ccf | |
| cards/p4-tiyu.png | 99ea285a73e0f3e2bae1d2d0ba290e863ba5ee09a28bee1fac10625d6e68e7b7 | |
| cards/p5-qingnian.png | 4ca40afa6c33bc633a138e0aae01d66db7df0ab70651a8c75102f0f0a57eef1c | |
| cards/p6-shendu.png | e7e6fed523ae1bb929e1be3299363e32be38b1c1ddecc8ecbf8906f8d4f93c7a | |
| cards/p7-ciyu.png | 82ecf71324310a802a958c460cca8e68d9776f317e6ea33c14002f83dda3c8cc | |
| cards/p8-ceyan.png | 23bda4c561e7dbc234790ffce403cdd1f088c8d98d4c06b5fd3baa467bf491b7 | |
| Lucerna-VOL2.pdf (print) | 799d95f49840fe69fa7d89f6eef8bde0313d7aaeab91111c2ab4a43e3c1777cc | 46,262,380 B |
| Lucerna-VOL2-web.pdf (web) | 93e8056d1a6ce7d839fcf8915cf84c1127ee980e45dcad475e982bd269527d66 | 3,262,614 B |

### Post-fix (from fixlog/postfix-hashes.txt)

P1–P7 SVGs and P1–P7 cards: identical to pre-fix (same hashes as above).
Changed files only:

| file | SHA-256 | size |
|---|---|---|
| svg/p8-ceyan.svg | 70e28a68cd1266ddbb3786f2a0520bad20edfb17c4f66334762b2ede8e774d58 | |
| cards/p8-ceyan.png | 54c826e360a687eba8ea1bf30a0749c1cbb918cd659374a766686fa8e76f95dd | |
| Lucerna-VOL2.pdf (print) | 612959385fedcfd660f0892efe6964007b2aa8a14a5dffafa137b743f05a4efa | 46,262,363 B |
| Lucerna-VOL2-web.pdf (web) | 742c01caaa149105addc903dd08739b3c143a6314c973471a0c934c4bed4b621 | 3,262,810 B |

## Evidence files

- `fixlog/prefix-hashes.txt`, `fixlog/postfix-hashes.txt` (full hash tables)
- `fixlog/snap1.txt`, `fixlog/snap2.txt` (pre-flight mtime snapshots)
- `fixlog/gate10-count.log`, `fixlog/gate10-apply.log`, `fixlog/gate10-run.log`
  (Gate 10 run), `fixlog/gate10-out/svg/` (Gate 10 SVGs, 8/8 = delivered)
- `fixlog/final-run.log`, `fixlog/final-render.log` (delivery render)
- `fixlog/occlusion.json`, `fixlog/p8.json` (mechanical gates)
- `fixlog/foldcheck/` (fold-coverage proof copy: 11 + 34 applied to the proof's
  repro build = it-build except the OUT line)
