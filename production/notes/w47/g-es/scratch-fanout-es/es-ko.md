# es-ko — Per-edition record (2026-11-11)

Status: **COMPLETE — self-check zero issues; awaiting independent proofreading.**

Second CJK-reader edition. Like ja, Korean is compact — but unlike ja,
build 1's P8-keys ended at 2554 (6px spare), so 4 notes were tightened.

## Coverage pre-check

- ko-missing 129 items; ko-conflicts 0 lines; ko-fallback-skipped 84 lines;
  ko.json 257 keys.
- All covered by MANUAL + harvest/ko.json + special handling.

## Apply

- `apply_fanout.py ko`: 476 literal replacements; 3 manual-over-harvest
  overrides ("Después ___ (원형 enviar) el sobre." → "Después ___(원형:
  enviar) el sobre." — manual drops the space before "("; "JUVENTUD
  청소년" → "JUVENTUD　청년"; "muchísimos aficionados = 아주 많은 팬" →
  "= 아주 많은 팬들").
- Leftover zh keys NONE; CJK in .py NONE (hangul is outside the script's
  CJK U+4E00–U+9FFF scan range).
- Band titles: VIDA　생활, CULTURA　문화, JUVENTUD　청년.
  "EL CALENDARIO　이번 주 일정" 271.5/422.5 — fits.
- P8 writing type: 쓰기 (content8.py — the ✓ form).

## Pre-build fixes (all wrap-measured before build)

1. P1 gloss (sans 19, gw): "“토론”: 두 사람 이상이 차례대로 공개 토론하고
   질문해요." (2 lines) → "“토론”: 사람들이 공개적으로 토론해요."
   (325.7, 1 line). **Incident:** the first substitution failed (count 0)
   because the file ends the gloss with ASCII "." not "。" — Korean
   harvest mixes "." (glosses) and "。" (bridges). Fixed by matching the
   file's ".".
2. P7 word-box gloss: already 2 lines @20 — kept as harvested.
3. P7 F-MAIL editor's note: 4 lines @20 AND @19 — no shortening; wrap
   20→19, *29→*27, para 20→19 for the col3 math. The "Write us!" closer
   ("편지를 보내 주세요!") is KEPT — it fits in 4 lines (unlike ja/pt).
4. P7 ERRORES notes: all 4 are 1 line at 19.5 units at CW-44 — no fix.
   **Caution:** my first measurement used retyped strings, not the file's
   — the file's actual notes differ ("1시는 단수라서 동사는 es를 써요."
   etc.) and briefly suggested a phantom 2-line ERR2. Always extract
   strings from the file.
5. P5 your-turn: 4 lines @20, **3 lines @19** — rendered at 19
   (eh wrap 20→19, *29→*27, para 20→19); P5 col3 1574.55 (clean value).
6. P3 your-turn: 3 lines @20 AND @19 — rendered at 19 for the 13px margin.
   P4 your-turn (4 lines @20, box 964.5) and P2 your-turn (4 lines @20,
   col3 993.0) need no fix.
7. Bridges: ALL already 1 line (P2 C "2면 글을 읽고 정답을 고르세요."
   266.3; P5 A 266.3; P6 A "위 두 그래프를 보고 정답을 고르세요." 317.3)
   or 2 lines with content on both lines — no bridge shortening needed
   at all for ko (unlike ja's 7).
8. P6 band: "선거운동 읽기" → "선거운동 읽기: 토론, 공약, 여론조사"
   (full sub 789.7 units in sans 18, limit 1684).
9. P8 header: right note 470.0 units wide @19.5; title 681.5 at 25 —
   no collision; header 1302→1337, keys flow 1328→1363 (uniform).
10. Letter parens full-width → half-width "(ejemplo, escrito por la
    redacción)".

## Builds

- **Build 1:** run rc=0, 0 OVERFLOW/TOO WIDE, TOTAL 150; P2 col3 993.0,
  P3 1594.75, P4 964.5, P5 1574.55, P7 1865.51; **P8-keys y=2554**
  (6px spare). P8 diagnostic: only 6 multi-line items (#32, #44, #82,
  #92, #139, #140).
- **Build 2 (final):** 4 notes tightened to 1 line each (wrap-verified):
  #32 "성 체칠리아 축일은 11월 22일이에요.", #82 "올해는 MiDNI로 투표할
  수 있어요", #92 "여론조사는 오차 있는 하루의 사진이에요",
  #140 "tener que = ~해야 해요" (each replaced only in its DEFINING
  file — #92 also occurs in the P7 FRASES quote, which keeps the long
  form). Run rc=0, 0 overflow, TOTAL 150, P8-keys y=2506 (54px spare).

## Gates (build 2)

- Render rc=0 (print 8,874,275 B; web 1,199,171 B). Occlusion 0 flags;
  sweeps 0/0/0 (box-vs-hline 0, orphans 0, widows 0 over 20 bridges);
  p8 extract 150/150, compare CLEAN, keydiff=[137, 138] adjudicated;
  freeze tool 8 OK + direct sha256 8/8; pdftotext print = web, 47,790 B
  byte-identical; P8 min font 10.125pt.
- §1.1: paper #fbfaf6 ×8, VOL.4 ×9, VOL.5 ×3, chips A2 11 / B1 21 /
  B2 3 = 35 (+1 #37402f header band rect, same as core), Q113–150 all
  badged; masthead 196; no "12 de noviembre"; 0 CJK ideographs in the
  Korean text (hangul only).
- Gloss tokens, per page (core §8.1): P1 reflexión 2; P2 mitin 2 /
  cartel 2 / escaño 2; P3 cante 5 / toque 6 / baile 9 / compás 4 /
  duende 5; P4 parón 2 / liderato 3; P5 papeleta 3 / censo 2 / plazo 4.

## Visual (8 PNGs, all clean)

- P1 gloss 1 line clear of divider; P2 title fits, Note box clear,
  C-intro 1 line; P3 ¿Y TÚ? box above divider; P4 ¿Y TÚ? box above
  fixture table; P5 ¿Y TÚ? box above divider (3 lines), B-bridge 2
  lines together; P6 band subtitle full; P7 word-box gloss 2 lines,
  letter half-width parens, ed note 4 lines inside box (closer kept),
  ERRORES 1 line each, banner well above footer, FRASES long #92 form
  intact; P8 header + note clear of swan caption, keys end well above
  footer, #44/#139 2 lines (core-consistent), #137/#138 1 line each,
  #150 ✓ form.

## 150-key verification

Full REG dump read (`es-ko-keys.txt`, 150 lines); matching sets verified
letter-by-letter: 25–28 (debate=토론 c, mitin=유세 b, cartel=포스터 d,
escaño=의회 의석 a), 52–55 (jornada=라운드 c, derbi=더비 b, liderato=1위 a,
fase liga=리그 단계 d), 141–144 (sondeo=여론조사 c, muestra=표본 d,
margen de error=오차 범위 b, junta electoral=선거관리위원회 a).

## `.text.md`

1,800 lines, read end-to-end (Korean layer line by line; Spanish frozen
as in core); numbers 1–150 all present; 0 CJK ideographs; no
"12 de noviembre". Exported with `extract_text_es_ko.py` (copied from
the FIXED ja extractor + hangul ranges U+AC00–U+D7AF / U+1100–U+11FF
added to `run_w`). Keys 1–150 verified in the export.

## es-ko deliverables (all in `~/workspace/weekly-git/production/2026-w47/2026-w47-es-ko/`)

- `La-Lucerna-VOL4-es-ko.pdf` — 8,874,275 B,
  SHA-256 `ba1a6e0a23a404c53ba1ad8cdfd9a2c83a3810242c08539715d24aed14949b5e`
- `La-Lucerna-VOL4-es-ko-web.pdf` — 1,199,171 B,
  SHA-256 `9117f3c186ee3aeca2a8e92208f590d0c0c4d8eaaeede6d83be5abee99725417`
- `2026-w47-es-ko.text.md` (1,800 lines)
- `ABSTRACT.txt` (Korean, one line, no ASCII double quotes, 423 bytes)
- `WEEKLY-KIT.md` (adjudications §6.1–§6.14; 2-round self-proofread
  record; final round zero findings)
- 8 SVG in `svg/`, 8 PNG in `cards/`

**Self-check conclusion: zero known defects; awaiting independent proofreading.**

## Records

`scratch-fanout-es/es-ko.md` (this file), `es-ko-build1/2.log`,
`es-ko-render2.log`, `es-ko-freeze.log`, `freeze-es-ko-2/`,
`es-ko-keys.txt`, `es-ko-p8-extract.json`, `es-ko-p8-compare.json`,
`extract_text_es_ko.py`, `2026-w47-es-ko-apply.json`;
`sweep_de.py` PUNCT set extended with ASCII ".?!" (and fixed a
SyntaxError from the unescaped `"` in the set literal);
`FANOUT-REPORT-es.md` updated (es-ko line added, checklist checked).
