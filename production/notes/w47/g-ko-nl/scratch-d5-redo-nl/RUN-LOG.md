# RUN-LOG — W47 D5 nl-family REDO (second worker, 2026-11-12)

Task: rebuild the nl family in TOP-LEVEL production
(`production/2026-w47/2026-w47-nl-<reader>/`). The first worker rebuilt the
`fanout-nl/` COPY and deleted its build-copy, so production still held pre-D5
PDFs; its D5-REPORT SHAs describe the copy, not production. This run redoes
all 7 Latin/Russian fan-outs + 3 CJK reader editions in place, reusing the
first worker's fix conclusions (extracted by diffing top-level vs copy content
files; only `# D5:`-marked hunks applied — newer production drift such as
delta D7/D8/D10 width-scans, fix1 NOTE_RIGHT anchors, build-11 content8 text
changes and the bslib4 `w` mechanism is KEPT, never overwritten from the copy).

Scratch: `hidden_files/w47/scratch-d5-redo-nl/` (scripts + per-edition dirs).
Builds run in place in production; only baseline SVG snapshots + logs live in
scratch. No commit, no push, no `lint.mjs --write`.

## nl-en — DONE (2026-11-12 ~09:44 UTC)
- Phase A: prerun svg == snapshot YES; TOTAL 150; census FAIL 498 Latin; occlusion 0; spill 0 (D11 already fixed in production); boxtitle 0; edge 0.
- Fixes applied (6, from first worker, re-verified): P2 head 25→23pt; P1 DE WEEK IN CIJFERS tsize 20; Agenda 19→18; IN DEZE EDITIE 24→23; P2 ZO ONTHOUD tsize 20; P6 VOOR OF TEGEN 21→19; P7 HET WOORD 23→20.
- Gates: all green (see D5-REPORT-nl-nl-en.md). Notable: p8 compare CLEAN keydiff=[137,138] (140 now matches core after build-11 Q140 fix); freeze diff vs baseline added CJK 0.
- Production SHAs (verified): print `d87a5242afec…` 12,102,271 B; web `c43bccdd7899…` 1,534,345 B; text.md unchanged `9596c4acbb27…` 45,115 B.
- KIT synced (§6 sizes + new §12; §10/§11 untouched).

## nl-de — DONE (2026-11-12 ~10:00 UTC)
- Phase A: prerun svg == snapshot YES (fix2 in production svglib changes no output); TOTAL 150; census FAIL 501 Latin; occlusion 0; spill 0 (D11 already fixed in production); boxtitle 0; edge 0.
- Fixes applied (6, from first worker, re-verified): P2 head 25→23pt; P1 DE WEEK IN CIJFERS tsize 21; Agenda 19→17; IN HET KORT 24→22; P2 ZO ONTHOUD tsize 22; P6 VOOR OF TEGEN 21→19; P7 HET WOORD 23→21.
- Gates: all green (see D5-REPORT-nl-nl-de.md). Freeze diff vs baseline added CJK 0.
- Production SHAs (verified): print `97420549c81e…` 12,104,230 B; web `15a65413c7f7…` 1,536,343 B; text.md unchanged `c1342c3fe20d…` 46,226 B.
- KIT synced (Files delivered + new D5 rebuild section; history preserved).

## nl-es — DONE (2026-11-12 ~10:20 UTC)
- Phase A: prerun svg == snapshot YES; TOTAL 150; census FAIL 497 Latin; occlusion 0; spill 0 (D11 already fixed in production); boxtitle 0 (copy-era pre-existing P6 +1.5px defect already fixed in production by fix1 D1); edge 0.
- Fixes applied (6, from first worker, re-verified): P2 head 25→23pt; P1 DE WEEK IN CIJFERS tsize 22; IN DEZE EDITIE 24→22; P2 ZO ONTHOUD tsize 21; P6 DE GRAFIEK 23→20; P7 HET WOORD 23→21; P2 PAKJESAVOND head 28→27 (TEXTX).
- Gates: all green (see D5-REPORT-nl-nl-es.md). Freeze diff vs baseline added CJK 0.
- Production SHAs (verified): print `2da02d5b3081…` 12,107,937 B; web `ac5498117a56…` 1,540,064 B; text.md unchanged `44fc3d5c4287…` 47,649 B.
- KIT synced (Files delivered + new D5 rebuild section; history preserved).
- Process note: nl-en's combined `rebuild-1.log` was overwritten by the nl-de run (both wrote to the scratch root); per-gate logs for nl-en survive in its edition dir, and its KIT §12 log list was corrected to name only the preserved logs. All later rebuilds write to per-edition `rebuild-1.log`.

## nl-fr — DONE (2026-11-12 ~10:40 UTC)
- Phase A: prerun svg == snapshot YES; TOTAL 150; census FAIL 500 Latin; occlusion 0; spill 0 (D11 already fixed in production); boxtitle 0; edge 0.
- Fixes applied (7, from first worker, re-verified): P2 head 25→23pt; P1 DE WEEK IN CIJFERS tsize 20 (+TEXTX fix); P2 ZO ONTHOUD tsize 21; P6 DE GRAFIEK 24→21; P6 VOOR OF TEGEN 21→19; P7 PAS OP 23→21; P7 HET WOORD 23→20.
- Gates: all green (see D5-REPORT-nl-nl-fr.md). Freeze diff vs baseline added CJK 0.
- Production SHAs (verified): print `08f57ec27d86…` 12,106,421 B; web `7e2f0989d641…` 1,538,515 B; text.md unchanged `f1d1154442c4…` 47,744 B.
- KIT synced (Files delivered + new D5 rebuild section; history preserved).

## nl-it — DONE (2026-11-12 ~11:00 UTC)
- Phase A: prerun svg == snapshot YES; TOTAL 150; census FAIL 495 Latin; occlusion 0; spill 0 (D11 already fixed in production); boxtitle 0; edge 0.
- Fixes applied (3, from first worker, re-verified): P2 head 25→23pt; P6 VOOR OF TEGEN 21→20; P7 PAS OP 23→22.
- Gates: all green (see D5-REPORT-nl-nl-it.md). Boxtitle 0 DEFECT, 1 marginal (P2 `RICORDA` 0.8px, ink inside — same as copy build). Freeze diff vs baseline added CJK 0.
- Production SHAs (verified): print `675f2bf33c42…` 12,102,402 B; web `f042c93a0522…` 1,534,505 B; text.md unchanged `f1d9e3f58b82…` 47,060 B.
- KIT synced (Files delivered + new D5 rebuild section; history preserved).

## nl-pt — DONE (2026-11-12 ~11:20 UTC)
- Phase A: prerun svg == snapshot YES; TOTAL 150; census FAIL 497 Latin; occlusion 0; spill 0 (D11 already fixed in production); boxtitle 0; edge 0.
- Fixes applied (8, from first worker, re-verified): P2 head 25→23pt; P1 DE WEEK IN CIJFERS tsize 22; IN DEZE EDITIE 24→22; P2 ZO ONTHOUD tsize 21; P2 PAKJESAVOND head 28→27 (TEXTX); P6 DE GRAFIEK 24→22; P6 VOOR OF TEGEN 21→19; P7 HET WOORD 23→19.
- Gates: all green (see D5-REPORT-nl-nl-pt.md). Freeze diff vs baseline added CJK 0.
- Production SHAs (verified): print `dc43c521becb…` 12,110,806 B; web `a5c9fd908314…` 1,542,942 B; text.md unchanged `7e6b0c54dcb2…` 47,209 B.
- KIT synced (Files delivered + new D5 rebuild section; history preserved).

## nl-ru — DONE (2026-11-12 ~11:35 UTC)
- Phase A: prerun svg == snapshot YES (production svglib carries unkerned-run patch); TOTAL 150; census FAIL 612 (Latin 346 + Cyrillic 266); occlusion 0; spill 0 (D11 already fixed in production); boxtitle 0; edge 0.
- Fixes applied (1, from first worker, re-verified): P2 head 25→23pt only. Zero D5-caused defects otherwise; no en-ru-style P8 false-positive collisions (tool fixed).
- Gates: all green (see D5-REPORT-nl-nl-ru.md). Freeze diff vs baseline added CJK 0.
- Production SHAs (verified): print `8fa079cbd094…` 12,367,658 B; web `e025daa39ff5…` 1,779,860 B (larger — Cyrillic Noto Sans now embedded); text.md unchanged `f23da475ff54…` 57,870 B.
- KIT synced (Files delivered + new D5 rebuild section; history preserved).

## Status: 7/7 Latin/Russian fan-outs DONE (en, de, es, fr, it, pt, ru) + core-nl. Remaining: 3 CJK reader editions (ja, ko, zh-tw).

## nl-ja — DONE (2026-11-12 ~12:15 UTC)
- Phase A: prerun svg == snapshot YES; TOTAL 150; census FAIL 336 Latin; occlusion 0; spill 0 (D11 already fixed in production); boxtitle 1 DEFECT pre-existing (P6 +2.5px); edge 0.
- Fixes applied (3, fresh discovery): P2 head 25→23pt; P2 ZO ONTHOUD tsize 21; P6 DE GRAFIEK 24→21 (over grew +2.5→+25.6px after D5 install).
- Gates: all green on rebuild-2 (see D5-REPORT-nl-nl-ja.md). Freeze diff vs baseline added CJK 0; vs core-nl added CJK 3315 (JP text).
- Production SHAs (verified): print `67aeebb40b58…` 18,803,852 B; web `6840df0c1e61…` 1,968,009 B; text.md unchanged `060bfdea2434…` 47,801 B.
- KIT synced (Files delivered + new D5 rebuild section; history preserved).

## nl-ko — Phase A DONE (2026-11-12 ~12:20 UTC)
- Prerun svg == snapshot YES; TOTAL 150; census FAIL 333 Latin; occlusion 0; spill 0; boxtitle 0; edge 0.

## nl-ko — DONE (2026-11-12 ~12:40 UTC)
- Fixes applied (1, fresh discovery): P2 head 25→23pt only. No box-title defect (39 titles all fit).
- Gates: all green on rebuild-2 (see D5-REPORT-nl-nl-ko.md). Freeze ran under venv, RC=0 — system-python3 fallback NOT needed. Freeze diff vs baseline added CJK 0; vs core-nl added CJK 3447 (KR text).
- Production SHAs (verified): print `fd8daad8ba7e…` 13,871,308 B; web `7dd70f00993a…` 1,791,909 B; text.md unchanged `75fbaa3004d0…` 47,585 B.
- KIT synced (Files delivered + new D5 rebuild section; history preserved).

## nl-zh-tw — Phase A DONE (2026-11-12 ~12:45 UTC)
- Prerun svg == snapshot YES; TOTAL 150; census FAIL 333 Latin; occlusion 0; spill 0; boxtitle 0; edge 0.

## nl-zh-tw — DONE (third worker, 2026-11-12)
- Install + rebuild-1 were already done by the second worker (svglib md5 `d8266612…` → `83c4820e…`, routing FAILURES 0); it was interrupted during `render.py` of rebuild-1 (0-byte `render.log`). Rebuild-1 found exactly one defect: HEAD TOO WIDE [P2-feature] `DRIE DINGEN VOOR 5 DECEMBER`.
- Fix applied (third worker): P2 head 25 → 23pt (`content12.py:175`; core-nl D5 defect, same line). No box-title defect (25 titles all fit).
- Gates: all green on rebuild-2 (see D5-REPORT-nl-nl-zh-tw.md). Freeze diff vs baseline added CJK 0; vs core-nl added CJK 1051 (TC reader text).
- Production SHAs (verified): print `90710eae78ae…` 13,888,370 B; web `1a923a7a42c6…` 1,976,962 B; text.md unchanged `30af89dfbfe2…` 44,320 B.
- KIT synced (Files delivered + new D5 rebuild section; history preserved).

## Status: 10/10 nl-family editions DONE (7 Latin/Russian fan-outs + 3 CJK reader editions) + core-nl. Third-worker independent verification of the 9 earlier editions: see `verify-3rd/` (re-run of the read-only gates on current top-level production) and the third worker's RUN-LOG in `scratch-d5-rebuild-nl/RUN-LOG-3rd-worker.md`.

## Render reproducibility check + web-SHA re-sync (third worker, 2026-11-12)
- Re-ran `render.py` + `webpdf.py` in place in all 10 top-level production dirs (logs: `verify-3rd/repro/<slug>.log`, pre/post SHAs in `<slug>.pre-sha` / `<slug>.post-sha`).
- Print PDFs: 10/10 reproduced BYTE-IDENTICALLY (all print SHAs above unchanged).
- Web PDFs: 10/10 got a NEW SHA on re-run (known toolchain property — KIT build-7 note already says web SHA/size are not reproducible run to run, only the text layer is compared). Stream-level diff (nl-de, `/tmp` scratch, deleted): skeleton identical; 18/126 streams differ, 70 bytes total, all inside embedded TTF `head`-table checksums; pdftotext bytes identical per edition.
- `textlayer.py` re-run vs the NEW web PDFs: RC 0, word multiset diff 0, char streams equal, orphan (a)/(b) 0 — all 10 (logs: `verify-3rd/<slug>/textlayer-repro.log`).
- New web SHAs (current production truth, KIT "Files delivered" re-synced, script `verify-3rd/resync-web-sha.py`, RESYNC-OK): de `2361bedfd4d5…` 1,536,341 B; en `db7a9ace064a…` 1,534,348 B; es `249fda66604b…` 1,540,062 B; fr `1b429a3ff61e…` 1,538,511 B; it `81a3ffaf8e8e…` 1,534,500 B; pt `b9e2c0d5b7f2…` 1,542,946 B; ru `69678fdcdd00…` 1,779,868 B; ja `9a4b3dbd5dad…` 1,968,007 B; ko `694720afc0cc…` 1,791,910 B; zh-tw `42b892b5c065…` 1,976,958 B. The per-edition "Production SHAs" lines above keep the rebuild's original web SHAs as history; the new values are recorded in each KIT (Files delivered + dated repro note in the D5 section) and each D5-REPORT (web line updated + repro note). Print + text.md SHAs unchanged everywhere.
