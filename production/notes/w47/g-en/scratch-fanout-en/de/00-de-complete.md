# en-de fan-out — builder record (successor to d132d807, 11 Nov 2026)

## Handover audit (discs did not match the report)

- d132d807 reported en-de complete, zero issues. On-disk state at takeover (11 Nov ~01:30 EST):
  `production/2026-w47/2026-w47-en-de/` held 8 SVGs + 8 card PNGs only — NO print PDF, NO web PDF,
  NO WEEKLY-KIT.md, NO .text.md, NO ABSTRACT.txt. `de/build.log` was 0 bytes.
  Gate JSONs predated the last SVG render (occlusion.log 00:51, p8-extract/compare 00:55,
  freeze-diff 00:55 vs SVGs 01:01–01:02) — all stale, none re-runnable as evidence.
- Verdict recorded at the time: en-de treated as NOT complete. Rebuilt and re-gated from scratch below.

## What was reusable from the previous builder

- `apply.py` (AST role-aware fan-out applier) + `map-de.json` (lit 234 = 62 TM hits + 172 fresh
  translations of the 205 misses; 33 misses are English-only strings carrying U+3000, need no map)
  + `tm-de.json` + `miss-de.json` + `inventory.py/tm_build.py`: sound, reused as-is.
- `de/repro/` (freeze baseline copy, 01:03–01:04): discardable; fresh freeze re-run instead.
- The edition source dir itself (content*.py already German-mapped): kept, one string fixed below.
- The old occlusion flag (P1 'Senatssitze.' 52% COVER, log 00:51) was already fixed by the previous
  builder's re-render — confirmed by a FRESH occlusion run: 0 flags. The old log is not evidence.

## The one fix made in this round

- D-de1 (translation): P2 "SAY IT: IN JANUARY 2027" box title read "So sagt man die Uhrzeit"
  (how to say the clock time), inherited verbatim from the W46 TM where the box taught
  "eleven o'clock". In W47 the box teaches the date "In January 2027".
  Fixed to "So sagt man das Datum" in `content12.py:219` and in `map-de.json` lit entry
  "SAY IT: IN JANUARY 2027　这样说时间" (same string). Full rebuild + re-render + all gates re-run.
- Checked and retained: P1 numbers box / P2 calendar gloss lines in German (W46 en-de precedent:
  "Nov 11, 11:00 — Stille · 1918 — Waffenstillstand"); "Fünf Sätze | who, where, was geschah,
  die Wende, das Ende" verbatim W46 en-de; doubled gloss prefix "Anmerkung | Erklärung |" (W46
  convention); moth `<title>Lucerna 三色蛾</title>` is a non-visible SVG title shared with core;
  P8 key 150 short label "Offene Aufgabe" (same pattern as core "开放题").

## Final gates (all re-run fresh after the fix, 11 Nov 01:35–01:51 EST)

- run.py exit 0, 0 overflow warnings; TOTAL 150; MODEL words 82.
- render.py exit 0; print PDF 29,330,795 bytes, SHA-256
  6d91162fac10c81e59ec811362136cd69e4e535a5b7ad04b4b98c94d530d95ba.
- dump_reg.py: 150 (10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22).
- occlusion_audit.py: 0 flags, selftest OK.
- p8.py extract: noted 60/150 (same set as core). compare: CLEAN, missing=[] extra=0,
  keydiff=[137,138,139,140,150] (reader-language keys, expected; W46 en-de same).
  P8 extract vs registry: 150/150 (Q150 short-label pattern shared with core).
- freeze.py baseline: tool 8/8 + direct sha256 8/8 MATCH.
- freeze.py diff: added = German only; removed = Chinese layer / gloss-box lines /
  re-chunked P8 key lines / furniture; visible text zero real CJK (only U+3000 separators).
- webpdf.py: 2,377,924 bytes (< 7 MB), text 48,076 bytes; print/web token-multiset diff 0/0.
  SHA-256 e8c6746167d7351e0cda55427ec191da98af9112e94f281cf390e5488f28d751.
- P8 min font-size 13.5 pt (≥ 9.75); badge-rect counts = core on all 8 pages
  (16/15/16/16/16/19/13/23); Q113–120 tags, Q145–149 "Levels: 145–149 [A2]",
  H WRITING "Schreiben [B1]" all present.
- text.md 51,989 bytes (stub registry 150 = real registry 150); full self-read done
  (P1–P2 in full; P3–P8 German-bearing lines + answers 118–150); 0 CJK chars in text.md.
- 8 cards visually checked one by one: no overflow / overlap / footer intrusion / tofu.
- §1.1: paper #fbfaf6 ×8; colour set identical to core; badge colours A2 #5c6e30 / B1 #46581f /
  B2 #37402f; VOL.4 everywhere (VOL.5 counts match core per page — teasers only).

## Deliverables (all in production/2026-w47/2026-w47-en-de/)

- 8 SVG + 8 card PNG + The-Lucerna-VOL4-en-de.pdf (print) + The-Lucerna-VOL4-en-de.web.pdf
- 2026-w47-en-de.text.md + ABSTRACT.txt (German, one line, no ASCII ") + WEEKLY-KIT.md
- ABSTRACT: "The Lucerna Englisch-Wochenblatt VOL.4: Die geprüften Ergebnisse der
  US-Zwischenwahl vom Dienstag, 3. November — … 150 Übungen, für Deutschsprachige, die mit
  Nachrichten aus der englischsprachigen Welt Englisch lernen."
