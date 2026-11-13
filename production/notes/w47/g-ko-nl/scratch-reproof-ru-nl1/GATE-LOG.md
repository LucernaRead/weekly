# Gate Log — Independent Re-proof, Lucerna Weekly 2026-W47, ru-nl

All gates self-run by the independent re-proofer in `hidden_files/w47/scratch-reproof-ru-nl1/`.
Interpreter: `tools/venv/bin/python` (Pillow 13.0.0, FreeType 2.14.3) unless noted.
Edition: `production/2026-w47/2026-w47-ru-nl/`; core: `production/2026-w47/core-ru/`.
HEAD at start: `c0382fa7f6c0915057611d714f75949d81a29956`.

## G0 — Opening probe + SHA verification (2026-11-11)

- Probe: `echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`; scratch write `probe.txt` (`probe-write-ok 2026-11-11T18:23:31Z`) OK.
- Print PDF `Lucerna-VOL4-ru-nl.pdf`: `5843ae6b80ac7e38298ec33d565b19e49d73dc165e6d18ffeec5bdddd4982fa2` / 21,291,643 B — MATCHES coordinator.
- Web PDF `Lucerna-VOL4-ru-nl-web.pdf`: `d3f016d58cb7b37a35cbf5b05e9a012c49bff6a116baf716db39aca56500b3eb` / 3,387,332 B — MATCHES.
- Text `2026-w47-ru-nl.text.md`: `8ac1336dbc521f510747d2a838a52e763d6452a81f8ea75ee6fc7c7687942423` / 64,051 B — MATCHES.
- Opening snapshot: 42 files (excl. `__pycache__`) in `opening-snapshot.sha256`.

## G1 — run.py rebuild (scratch copy, OUT redirected to scratch)

- Command: edition copied to `run-copy/`; `run.py` run there (OUT is `__file__`-relative, so the copy's own `svg/` is used; production SVG untouched).
- Result: rc=0, **TOTAL 150**; by page P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38; by level A2 50, B1 76, B2 24; by type Voltooi de zin 54, Meerkeuze 55, Woorden koppelen 20, Zinnen bouwen 12, Zinsomvorming 4, Vertaling 4, Schrijven 1; model words 97; zero FLOW OVERFLOW / HEAD TOO WIDE.
- Rebuilt SVGs **8/8 byte-identical** to production `svg/` (run 1 mtimes 18:26:08–18:26:50 UTC 2026-11-11; run 2 in same copy also 8/8 SAME — deterministic).
- P8 keys end col 3 y=2389.29; P8 Morozko image SKIPPED by build's own condition (keys end 2389.29, `img_y+250+90 > 2560`) — by design, same as W46.
- Log: `run-rebuild.log`, `svg-rebuild-compare.log`.

## G2 — freeze.py baseline, core-ru

- Command: `freeze.py --build production/2026-w47/core-ru --core-svg production/2026-w47/core-ru/svg --out scratch/freeze-core`.
- Result: rc=0, **8/8 SVGs byte-identical**, core integrity re-hash clean. Core P7 SVG hash `6679e1aa83699942…` vs edition P7 `527a45ebf28f…` (different, as expected — explanation layer differs).
- Log: `freeze-core.log`, `freeze-core/`.

## G3 — freeze.py diff core→edition

- Result: rc=0; removed distinct **487**, added distinct 321; removed Cyrillic-bearing strings exactly **15**, all on P8: 14 Morozko-caption words (Билибин, Билибина, Зимняя, Иван, Ивана, Иллюстрация, Морозко, год, достояние, иллюстрация, к, ноябрю, общественное, сказка) + Q46 `можно` ×1; **added Cyrillic 0**; added CJK chars 1 per page = U+3000 only (8 total). Matches KIT's re-fanout record exactly.
- Log: `freeze-diff.json`, `freeze-diff.log`, `freeze-diff-analysis.txt`.

## G4 — p8.py

- Result: extract 150/150 core and 150/150 edition; compare **CLEAN**, `keydiff=[137, 138, 139, 140]` (four E-section translation keys, Dutch by design).
- Log: `p8-edition.json`, `p8-core.json`, `p8-compare.json`, `p8-compare.log`, `p8-extract-edition.log`, `p8-extract-core.log`.

## G5 — Print vs web text layer

- Method: `pdftotext` per page, both PDFs.
- Result: all 8 pages **byte-identical** (not just multiset); 57,957 bytes per PDF; U+2019 = 0 in both.
- Files: `pdftext/print-p1..8.txt`, `pdftext/web-p1..8.txt`.

## G6 — check_core.py (read-only against production dir)

- Result: rc=0; GOLDEN 8 sentences ×2, BAD 0; gloss fails 0; P8 SVG text chars 11,138; 1 orphan line-start (P7 y553 `”».` — KIT-known benign, same class as core); 1 same-baseline collision (P1 y1712 italic «чёрная пятница» — KIT-known, same as core).
- Log: `check-core.log`.

## G7 — P8 minimum font (PyMuPDF)

- Result: **9.75 pt** on both print and web PDFs = SOP §1.1 floor. Per-page minima: P1 11.62, P2 11.62, P3 12.75, P4 11.62, P5 11.62, P6 12.75, P7 11.62, P8 9.75.
- Log: `p8-font.log`.

## G8 — Occlusion audit + adjudication

- Audit (`tools/occlusion_audit.py`, edition svg vs `--core` core-ru svg; selftest OK): edition **42 flags {TEXTX: 42}, 0 LINEX**; core also 42; **NEW vs core: 3** (P7 `ЯЗЫК` vs `　TAAL` 3.8×34.0 px; P8 `ОТВЕТЫ` vs `　TEST EN ANTWOORDEN` 8.0×35.5 px; P8 `ОТВЕТЫ` vs `　ANTWOORDEN — PER PAGINA…` 4.5×19.0 px). Tool rc=1 (its exit semantics for NEW flags found).
- Audit systematic error (new finding): `resolve_font` maps `"Noto Serif"` / `"Noto Sans"` to the CJK SC face while the build measures Cyrillic with real Noto Serif / Noto Sans — audit overstates Cyrillic advance ~3% (#1 `Зенит` 171.8 vs build 166.3; #33 `ЯЗЫК` 136.6 vs 133.0; #39 `Кипренского` 128.7 vs 125.3). Upstream `adjudicate_ru.py` SX=1950/1800 is the wrong scale here (SX=1.0); not used.
- Adjudication attempts: v1 column projection (40 OVERLAP / 2 CLEAR — superseded, wrong); v2 components holding all rasters (OOM-killed rc=137 after ~526 s — superseded); v3 components, fringe-inclusive mask + gap formula bug (card 26 CLEAR / 11 NO-SEED / 5 OVERLAP; print/web 22 CLEAR / 15 OVERLAP / 5 NO-SEED — superseded); v4 blank-column profile (card 24 CLEAR / 18 OVERLAP; print/web 28 CLEAR / 14 OVERLAP — superseded, too strict for vertically interleaving glyphs); v5 vector per-char PIL gaps (10 CLEAR / 32 OVERLAP, gaps −1.02..+0.43 — superseded, per-char getbbox overhang disagrees with string getbbox and raster).
- **v6 final** (solid-component, `adjudicate_reproof6.py`, `adjudication.json`): solid ink = RGB distance from modal bg > 190; 8-connected components; sides by component leftmost vs B.x; OVERLAP iff A-side component spans past B.x+3 or B-side ink absent while A-side ink crosses boundary.
  - Card (1×): **30 CLEAR / 12 OVERLAP**. Print (2×): **34 CLEAR / 8 OVERLAP**. Web (2×): **34 CLEAR / 8 OVERLAP**.
  - Print/web CLEAR gaps: 0.62–50.5 SVG px (4× Краснодар 1.08; Кипренского 1.08; ЯЗЫК/TAAL 48.0; ОТВЕТЫ 50.5 / 26.5).
  - The 8 print OVERLAPs (#4, #11, #13, #17, #28, #29, #30, #31) each verified CLEAR on a 6× zoomed print crop (`crop-flagNN-print.png`, all viewed): `пятница»:`, `толерантности.`, `студента.`, `биография:`, `смартфоны,`, `студента,`, `сбивается.`, `Планируйте:` — all legible, mark clearly separate. String-level PIL gaps −0.6..+0.4 SVG px (sub-pixel touch, ≤0.13 mm at print size).
  - The 4 card-only extra OVERLAPs (#7/#21/#22/#25 Краснодар, #8, #38) are print CLEAR (1.08 / 1.0 SVG px).
- **Final: 42/42 CLEAR on the delivered print and web PDFs.**

## G9 — D7 re-measurement

- Source: `content7.py:12` `thema's` (U+0027); U+2019 = 0 in `content7.py` and in `2026-w47-ru-nl.text.md` (L504); U+2019 = 0 on all 8 pages of both PDFs; `text.md` 64,051 B (−2 B vs KIT pre-fix 64,053 B = exact UTF-8 delta).
- PIL (Noto Sans CJK SC 18 px): U+2019 advance 18.00 px / ink bbox (0,5,18,21); U+0027 advance 5.00 px / ink bbox (0,7,5,21); subtitle advance 229.77 → 216.38 (−13.39 px); U+3000 at 23 px = 23.0 px (`d7-pil.log`).
- Band raster rows 148–161: thema → `'s` blank space = **3 SVG px on card, print and web** (card 1816.00→1820.00; print/web 1817.50→1821.00); same-band inter-letter gaps 1–5 px, median 3 (`d7-raster.log`). Crop `crop-d7-themas-print.png` reads `thema's` as one word.
- Intentional keeps: `ABSTRACT.txt` 1× U+2019 (`thema's van de week`); `check_core.py` L94 `CLOSES` constant — both untouched, correctly.

## G10 — D1 / kicker / D2 / D6 survival (ElementTree, rendered SVG)

- P6 kicker y=1552: `ЧЕМ ЗАЙМУТСЯ НА ЭТОЙ НЕДЕЛЕ?　УЧЕБНЫЕ ДАННЫЕ　OEFENGEGEVENS` ✓
- P6 disclaimer y=1582: RU `Это учебный опрос редакции для упражнений — не настоящая статистика.` + NL `Dit is een oefenenquête van de redactie — geen echte statistiek.` ✓; chart 38/26/18/18 = 100%.
- P1 tagline y=372: `ЕЖЕНЕДЕЛЬНАЯ  ГАЗЕТА  ДЛЯ  ИЗУЧАЮЩИХ  РУССКИЙ  ЯЗЫК  —  НАСТОЯЩАЯ  РОССИЯ,  ПО-РУССКИ`, **9 double-space runs, 0 single** ✓ (`content12.py:18`).
- P7 subtitle y=168: `Фокус на язык　Три уровня, три темы　Drie niveaus, drie thema's` ✓
- P8 subtitle y=168: `PAGINA 8　Большой тест недели + все ответы` ✓
- Q20 key: registry `желании` and printed P8 `желании` ✓; Q25 registry `b`, P2 match option `b. День студента` ✓.
- Logs: `d-survival.log`, `d-survival2.log`, `d-survival3.log`, `d-survival4.log`.

## G11 — 150-question hand verification

- Stems dumped from source AST: 130 `.ex()` + 20 `match_set` = 150; 0 mismatches vs `reg.json` (key/level/type, in order).
- Hand-verified Q1–Q150 key vs stem: **0 mismatches**. Anchors re-checked: 21 goals (P4 table sum), 1946 Prague, 16:20 sunset, 83rd-minute equaliser, 20:45 Baltika, 8-match table (`content34.py` `res14`), Masha passage (`text.md` L622) → Q129–132, 14.4M orders (`text.md` L364), 27 Nov 2026 = Friday.
- Registry vs printed P8 keys: 1 apparent mismatch — Q150 placeholder vs printed `✓` (open-task extraction artefact; core also prints `✓`; keydiff only [137–140]).
- Files: `reg.json`, `ex-stems.json`, `ex-stems.txt`, `key-crosscheck.log`, `p8-edition.json`.

## G12 — Visual read of all 8 cards

- P1–P8 all read (cards `production/2026-w47/2026-w47-ru-nl/cards/*.png`): no overflow, overlap, or clipping. P4 8-row results table present with all 8 scores; P6 chart + disclaimer; P7 band + Pushkin/Kiprensky caption; P8 keys Q1–150 + Q150 97-word model text. Details in PROOF-NOTE.md §7.

## G13 — Production zero-write check

- Closing full-edition SHA-256 re-hash vs `opening-snapshot.sha256`: **0 differences** (42 files, `__pycache__` excluded). File: `closing-snapshot.sha256`.
