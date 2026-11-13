# es-ja — Per-edition record (2026-11-11)

Status: **COMPLETE — self-check zero issues; awaiting independent proofreading.**

First CJK-reader edition. Japanese is compact: build 1 already had
0 overflow and P8-keys ending 2521 — no P8-note tightening was needed
at all (only 5 multi-line P8 items vs ru's 33).

## Coverage pre-check

- ja-missing 135 items; ja-conflicts 0 lines; ja-fallback-skipped 0 lines;
  ja.json 250 keys.
- All covered by MANUAL + harvest/ja.json + special handling.

## Apply

- `apply_fanout.py ja`: 485 total literal replacements; 2 manual-over-
  harvest overrides (VIDA　暮らし → VIDA　生活; "muchísimos aficionados
  球迷很多" harvest "muchísimos aficionados = ものすごく多くのファン"
  → manual "muchísimos aficionados＝とても多くのファン").
- Leftover zh keys: **2 entries, both false positives** (key==value):
  "VIDA　生活" (content12.py) and "CULTURA　文化" (content34.py) —
  the Chinese source and the correct Japanese rendering are the same
  shared kanji; the apply report shows each replaced 1×. Band titles
  verified: VIDA　生活, CULTURA　文化, JUVENTUD　若者.
- CJK in .py is EXPECTED for a Japanese edition (the script only
  reports it, does not fail on it).
- P8 writing type: 作文 (content8.py:134 — the ✓ form).

## Pre-build fixes (all wrap-measured before build)

1. P1 gloss (sans 19, gw): "「討論」：2人以上が公開で話し合い、順番に発言し
   質問する。" (2 lines) → "「討論」：人々が公開で話し合う。" (302.9, 1 line).
   Measured in sans at gw from the start (nl lesson).
2. P7 word-box gloss: already 2 lines @20 — kept as harvested.
3. P7 F-MAIL editor's note: 5 lines @20/@19 → "編集部より：締め切りまでに
   本物の手紙も最優秀作文も届かなかったため、今号は編集部の見本の手紙を
   掲載します。約束は VOL.5 に持ち越しです。" (4 lines @19 at CW-44;
   drops "お便りをお待ちしています！"). ldcn wrap 20→19, *29→*27, para 20→19.
4. P7 ERRORES notes: all 4 are 1 line at 19.5 units at CW-44 — no fix needed
   (unlike fr/nl/ru).
5. P5 your-turn: 4 lines @20 AND @19 — kept full text, rendered at 19
   (eh wrap 20→19, *29→*27, para 20→19); P5 col3 1601.55, 6.45px above
   divider, adjudicated like ru.
6. P3 your-turn: 3 lines @20 AND @19 — rendered at 19 for the 13px margin.
   P4 your-turn (4 lines @20, box 964.5) and P2 your-turn (6 lines @20,
   col3 1022.0) need no fix.
7. P2 C-intro: "2ページの記事を読んで、正しい答えを選ぼう。" (2 lines,
   line 2 a lone "。") → "記事を読んで正しい答えを選ぼう。" (1 line @20.5).
8. P5 B-bridge: already 2 lines @20.5, kept as harvested.
9. P6 band: "選挙戦の読み方" → "選挙戦を読む：討論・政策・世論調査"
   (full sub 831.7 units in sans 18, limit 1684).
10. P8 header: right note 427.2 units wide @19.5 → header 1302→1337,
    keys flow 1328→1363.
11. Letter parens full-width → half-width "(ejemplo, escrito por la
    redacción)".
12. Box titles measured against their boxes — no pt-§6.13 overflow
    (widest "LA SEMANA EN CIFRAS　今週の数字" 415.7/422.5). The RTVE
    title's Spanish gloss "minutos de propaganda por partido" is core's
    own subtitle, identical in core-es, not a harvest gap.
- P7 col3 budget: gloss 2 lines (Δ0) + ed note 4 lines @19 (Δ+21) → 1865.51.
- All 14 substitutions applied in one pass with count assertions.

## Builds

- **Build 1:** run rc=0, 0 OVERFLOW/TOO WIDE, TOTAL 150; P2 col3 1022.0,
  P3 1594.75, P4 964.5, P5 1601.55, P7 1865.51, P8-keys y=2521 (39px spare).
  Render rc=0 (print 17,295,670 B; web 1,504,797 B). Occlusion 0 flags;
  sweeps 0/0; p8 150/150 CLEAN, keydiff=[137, 138]; freeze 8/8;
  pdftotext identical.
- **Build 2** (4 bridge-widow fixes: P4 A, P5 A, P5 C, P6 A): run rc=0,
  0 overflow, TOTAL 150; same col numbers. Render rc=0 (print
  17,294,880 B; web 1,503,887 B). Occlusion 0; sweeps 0/0; new widow
  check found 2 MORE widows (P4 C, P4 D).
- **Build 3 (final)** (P4 C, P4 D fixes): run rc=0, 0 overflow, TOTAL 150;
  P8-keys y=2521. Render rc=0 (print 17,294,297 B; web 1,503,253 B).
  Occlusion 0 flags; sweeps 0/0/0 (box-vs-hline 0, orphans 0, widows 0
  over 20 bridges); p8 150/150 CLEAN, keydiff=[137, 138] adjudicated;
  freeze tool 8 OK + direct sha256 8/8; pdftotext print = web, 47,054 B
  byte-identical; P8 min font 10.125pt.

## P8 diagnostic (build 1)

Only 5 multi-line items vs core's 2: #31, #44 (core-consistent), #88,
#139 (core-consistent), #140. #137/#138 and #1 are 1 line each in
Japanese. No tightening needed — the flow fits with 39px spare.
Writing type 作文 (the ✓ form). #150 note "模範文はこのページのHを参照
（97語）" matches the W46 es-ja ruling ("模範文はこのページのH区
（84語）"); the modelo section H is on P8 itself.

## Gates (build 3)

- §1.1: paper #fbfaf6 ×8, VOL.4 ×9, VOL.5 ×3, chips A2 11 / B1 21 /
  B2 3 = 35 (+1 #37402f header band rect, same as core), Q113–150 all
  badged; masthead 196; P8 min font 10.125pt.
- Full-width: Japanese 。、：（）＝ inside Japanese text is correct
  Japanese usage, not a defect; Spanish letter parens half-width.
- CJK: Japanese text by design; no Simplified-Chinese residue (leftover
  check: only the 2 key==value false positives, §6.1).
- Gloss tokens, per page (core §8.1): P1 reflexión 2; P2 mitin 2 /
  cartel 2 / escaño 2; P3 cante 5 / toque 6 / baile 9 / compás 4 /
  duende 5; P4 parón 2 / liderato 3; P5 papeleta 3 / censo 2 / plazo 4.
- No "12 de noviembre".

## Visual (8 PNGs)

- Build 1 full pass: P1 gloss 1 line clear of divider; P2 title fits,
  Note box clear, C-intro 1 line; P3 ¿Y TÚ? box above divider;
  P4 ¿Y TÚ? box above fixture table; P5 ¿Y TÚ? box above divider,
  B-bridge 2 lines together; P6 band subtitle full; P7 word-box gloss
  2 lines, letter half-width parens, ed note 4 lines inside box,
  banner well above footer, ERRORES 1 line each; P8 header + note clear
  of swan caption, keys end well above footer, #150 ✓ form.
- Defect class found visually: lone-"。" bridge widows — P4 A, P5 A,
  P5 C, P6 A (build 1); P4 C, P4 D caught by the new sweep check
  (build 2). All 7 fixed to 1 line; P4/P5/P6 re-inspected after build 3.
- Note: #44's note wraps "時間が先、動詞は2" / "番目" — the renderer's
  character-level CJK break of "2番目"; the wrap itself is
  core-consistent, the split point is a rendering detail (see §6.14
  of the KIT).

## 150-key verification

Full REG dump read (`es-ja-keys.txt`, 150 lines); matching sets verified
letter-by-letter: 25–28 (debate=討論 c, mitin=集会 b, cartel=ポスター d,
escaño=議席 a), 52–55 (jornada=節 c, derbi=ダービー b, liderato=首位 a,
fase liga=リーグ戦 d), 141–144 (sondeo=世論調査 c, muestra=標本 d,
margen de error=誤差の範囲 b, junta electoral=選挙管理委員会 a).
#57 "muchísimos aficionados＝とても多くのファン" (manual override landed).
#137/#138 Japanese-sentence keys ("月曜日は国際フラメンコの日。 —
原文と比べよう。" / "土曜日にセビージャ・ダービーを見る。 — 原文と比べよう。").

## `.text.md`

1,803 lines (build 3 re-export; v1 read end-to-end, 1,830 lines).
Exporter fix (KIT §6.16): build-1 export showed #82 as "282." —
the extractor's flat 9 px/char model glued a digit orphaned from #44's
note onto the next column's key. Fixed the scratch extractor copy
(CJK-aware width + column-boundary split) and re-exported: "282." →
"82.", all 150 keys present; the v1→v3 diff is re-flow only (character
multiset identical ignoring whitespace). Build-3 export differs from
v3 only by the 6 fixed bridge strings (verified: new forms present,
old forms gone, keys 1–150 all present).

## es-ja deliverables (all in `~/workspace/weekly-git/production/2026-w47/2026-w47-es-ja/`)

- `La-Lucerna-VOL4-es-ja.pdf` — 17,294,297 B,
  SHA-256 `de40fa29ee957b64cba37f7afb5affe9e8b18abc15b5bf823cefbdf15f8545cf`
- `La-Lucerna-VOL4-es-ja-web.pdf` — 1,503,253 B,
  SHA-256 `859b4421086697dab0148b050bfaaf68fd3cd34c1f9dd08c22124d620f9ab1d7`
- `2026-w47-es-ja.text.md` (1,803 lines)
- `ABSTRACT.txt` (Japanese, one line, no ASCII double quotes, 447 bytes)
- `WEEKLY-KIT.md` (adjudications §6.1–§6.16; 3-round self-proofread
  record; final round zero findings)
- 8 SVG in `svg/`, 8 PNG in `cards/`

**Self-check conclusion: zero known defects; awaiting independent proofreading.**

## Records

`scratch-fanout-es/es-ja.md` (this file), `es-ja-build1/2/3.log`,
`es-ja-render1/2/3.log`, `es-ja-freeze.log`, `es-ja-freeze3.log`,
`freeze-es-ja-1/`, `freeze-es-ja-3/`, `es-ja-keys.txt`,
`es-ja-p8-extract.json`, `es-ja-p8-compare.json`,
`es-ja-p8-extract3.json`, `es-ja-p8-compare3.json`,
`extract_text_es_ja.py` (fixed copy: CJK-aware width + column split),
`2026-w47-es-ja-apply.json`; `sweep_de.py` extended with the bridge-widow
check (3rd check, shared across editions); `FANOUT-REPORT-es.md` updated
(es-ja line added, checklist checked).

## Incidents

- Duplicate dispatch of the build-3 gate command (same exec sent twice)
  caused a service restart mid-run; the first call aborted. Recovered
  by verifying the edition dir + PDFs intact, then re-running the gates
  once. No data loss (the /tmp copy of the v1 .text.md was lost in the
  restart, as /tmp is ephemeral — the shipped .text.md was unaffected).
