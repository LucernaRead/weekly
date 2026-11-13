# D5-REPORT — ru-pt (2026-w47)

- Edition: `2026-w47-ru-pt` (target ru, reader pt, mode latin, `_D5_READER = "latin"`)
- Date: 2026-11-12 (UTC). Builder: W47 D5 ru-family worker.
- Mechanism: `scratch-d5-plan/mechanism/apply_variant.py --target ru --reader pt`
  (per PILOT-REPORT install method; CJK-DECISION.md §1–§3 + brief-d5-rebuild.md read).
- Build interpreter: `tools/venv/bin/python` throughout (Pillow 13.0.0). No system python3.
- Scratch: `hidden_files/w47/scratch-d5-rebuild-ru/scratch-fanout-ru/2026-w47-ru-pt/`
  (baseline/ = pre-fix svg + svglib.py + assets; backup/ = same copy for boxtitle).
- **Build location: IN PLACE in production** (`production/2026-w47/2026-w47-ru-pt/`).
  The only build-copy was the gates' `freeze/` rebuild output, deleted after
  verification. Production SHAs below were re-checked against the production
  files themselves (not a scratch copy).

## Install

- Pre-fix `svglib.py` md5 `27f11789af7c828e47ca14eb00c1dded` (no fix2;
  unkerned run-measurement fix present) → post-install
  `2e87fef862607133a962c0ee981bd0a6` (fix2 added by the installer + D5).
- `assert_routing.py` (latin→news): all assertions pass, fix2 routing preserved.
- Baseline verified clean BEFORE install: pre-fix `run.py` rebuild reproduced the
  delivered 8 SVGs byte-identically (8/8 sha256 OK); pre-fix run.log 0 HEAD TOO WIDE,
  0 FLOW OVERFLOW, TOTAL 150.

## Census (pre → post)

| check | pre | post |
|---|---|---|
| D5 Latin in CJK Sans | 431 | **0** |
| D5 Cyrillic in CJK Sans | 0 | 0 (417 Noto Sans elements, unchanged) |
| curly quotes in CJK Sans | 0 | 0 (2 total, all Newsreader) |
| `census_quotes.py` defective | 0 | **0** |

## Builds

- `run.py` RC=0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE;
  `head_check.py` (run.log vs base-run.log) PASS 0 defects.
- `render.py` RC=0, first pass already normal (20,883,575 B);
  `webpdf.py` RC=0, 58,392 text bytes.
- text.md byte-identical: SHA-256
  `ab21732233d80c5af14a2a579ef611370fb228ba29376d9e2ce9186a7c613a02` (65,116 B).

## New PDFs (verified in production)

- Print `Lucerna-VOL4-ru-pt.pdf`: `9057a1e3…` 21,203,097 B →
  **`eb3c2905d2f870ddcc2273c2384fe3bbc3e1b53df15e6e7bea860e009b68672f` 20,883,576 B**
- Web `Lucerna-VOL4-ru-pt-web.pdf`: `0868cfa4…` 3,381,069 B →
  **`cc52dfb7f87bccce2776cf9f07a5b11f66f0a21187784dbfb596ed546579d66d` 3,337,084 B**
  (< 7 MB; print/web text layers byte-identical, 38,909 chars each)
- Production `svglib.py` contains `_D5_READER` (verified); KIT §5 synced to
  the SHAs above.

## Defects found by D5 (4, in two rounds; text unchanged, font size only)

Round 1 — 3 cream-box title overflows (creambox + boxtitle agree):

1. P1 `СМИ　O QUE DIZEM OS MEDIA` over right +45.4px.
   Fix: `content12.py:73` size 27→23pt (advance 445.8→379.8 vs box inner width
   400.5, ~20.7px margin; 24pt would leave only 4.3px).
2. P6 `ЗА И ПРОТИВ　PRÓS E CONTRAS` over right +14.4px.
   Fix: `content56.py:136` size 24→22pt (advance 413.8→379.3, ~21.2px margin;
   23pt would leave only 3.9px).
3. P7 `СЛОВО　A PALAVRA DA SEMANA` over right +7.4px.
   Fix: `content7.py:88` size 23→22pt (advance 407.4→389.7, ~10.8px margin).

After the round-1 fixes, the gates re-run was green everywhere EXCEPT one
real occlusion flag:

Round 2 — P8 head/subtitle same-baseline collision (occlusion TEXTX,
12.0×19.0px; same class as ru-de's P8 collision — a REAL defect, unrelated
to the voided PILOT-REPORT §5.4 P8 key-row false positive):

4. P8 head `ОТВЕТЫ　RESPOSTAS — ORDENADAS POR PÁGINA; PROCURE O NÚMERO DO
   EXERCÍCIO` ink overlaps the subtitle `Cada resposta com uma breve nota
   em português　✓ = texto modelo` (same baseline y=1302).
   Fix: `content8.py:116` size 25→24pt (advance 1171.4→1124.4; head ends
   ~35.6px before the subtitle starts; subtitle `content8.py:117` untouched).
   Full rebuild + full gates re-run after the fix.

The P1 full-width word head `СЛОВО НЕДЕЛИ　PALAVRA SEMANAL`
(`content12.py:114`, fix1-shortened, 22pt) had no defect and was left alone.
Card crops of all four fixed spots were read visually and confirmed clean
(P8 head and subtitle with a clear gap).

NOT fixed (voided false positive): PILOT-REPORT §5.4 en-ru P8 key-row
"collisions" — voided by CJK-DECISION.md §2 (occlusion_audit.py measured
bare `Noto Sans` runs on the CJK SC face; U+00B7 full-width). No P8 key
row was touched. This edition's P8 key rows ran 0 flags with the fixed tool;
the flag above was the head/subtitle collision, a different element.

## Gates (round-2 rebuild, GATES_OVERALL_FAIL=0)

- D5 census PASS (0/0/0); quotes census 0; `head_check.py` PASS 0 defects.
- `run.py` TOTAL 150; `p8.py extract` 150/150; `p8.py compare` vs core-ru
  CLEAN (keydiff=[137, 138, 139, 140], expected reader-language keys).
- `freeze.py baseline` 8/8 byte-identical; freeze-diff vs pre-fix baseline:
  added CJK chars 0 (added Latin strings 147 = D5 run-splitting).
- `occlusion_audit.py` (fixed version) 0 flags; `boxtitle_check.py` 0 DEFECT
  (57 titles, 683 body lines); `d5_creambox_audit.py` PASS 0 defects
  (P8 lines 228→228, slack_footer 46.5→46.5px; ratios n=398, median 1.040,
  bold median 1.049).
- `spill_sweep.py` 0 SPILL; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR.
- Print/web text layers byte-identical (38,909 chars).
- P8 Morozko SKIPPED by the build's own condition — as before,
  by design, not a defect.

## KIT

- `WEEKLY-KIT.md` §7 appended with the D5 record; §5 PDF SHAs/sizes updated
  to the new values above. History preserved.
- Independent re-proof is the coordinator's job; this report records
  self-check gates only.

## Cleanup

- `freeze/` build-copy deleted after verification. Baseline + logs + JSONs kept.
- No commit, no push, no `lint --write`. No other family touched.
