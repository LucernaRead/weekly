# PROOF NOTE — 2026-W47 ru-en, Round-1 Independent Proofread

- Edition: `2026-w47-ru-en` (Russian target × English reader), Lucerna Weekly VOL.4, issue 16–22 November 2026
- Proofer: round-1 independent (leaf); check only, no source/finished-product modification
- Date: 2026-11-11
- Work dir: `~/workspace/weekly-git` (clone, main); notes: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-en1/`
- Read first: `SOP.md` §8 + §1.1 (full), `AGENTS.md`, `production/2026-w47/2026-w47-ru-en/WEEKLY-KIT.md` (full), `scratch-fanout-ru/FANOUT-REPORT-ru.md`

## Verdict: NOT zero-issue — 2 minor defects (D1, D2)

Both are cosmetic/spacing, text remains legible and correct. No content, key, level, badge, or layout defect found. See GATE-LOG.md for the full mechanical-gate record.

## Identity recheck (self-computed, matches KIT exactly)

- Print PDF `Lucerna-VOL4-ru-en.pdf`: 21,245,420 bytes, SHA-256 `023d9fd12bdca276751400fb13f7f399d645c267a09ba1897eb0e598d52f2e3a`, 8 pages
- Web PDF `Lucerna-VOL4-ru-en-web.pdf`: 3,341,934 bytes, SHA-256 `fab0fc44736ecb169a1cc3932a8e85db2504f694f02e84d45f3063435327493d`, 8 pages, < 7 MB
- Edition dir contains `svg/` (8 SVGs), `cards/` (8 PNGs), both PDFs, `WEEKLY-KIT.md`, `ABSTRACT.txt`, `2026-w47-ru-en.text.md` (56,604 bytes per KIT)
- Startup probes passed: `git hash-object -w` probe + real write probe file in scratch dir

## Defect D1 — minor: P5 band subtitle curly double quotes render full-width (CJK font)

- Location: P5 (`svg/p5-molodezh.svg`), band subtitle node, font `Noto Sans CJK SC`, 18 px SVG / 13.5 pt print
- Original (rendered): `“Black Friday”: sales from 16 November` — visible gap between `”` and `:`, reading as `” :`
- Should be: same string with normal quote spacing, e.g. straight quotes `"Black Friday"` (the fix the fr family applied to the same defect class: curly ’ → straight ' in 52 map values) or a Latin font for the English gloss
- Evidence:
  (a) Char-level measurement on the print PDF (PyMuPDF rawdict): `“` advance 13.50 pt and `”` advance 13.50 pt — exactly 1 em at 13.5 pt, i.e. full-width; a normal word space in the same line is 3.02 pt; the widest Latin letter `m` is 12.50 pt.
  (b) Pixel measurement on a 3× zoom crop: ink gap ≈ 9.8 pt between `”` ink and `:` ink (≈ 3.2× a word space).
  (c) Source is the fan-out layer: `scratch-fanout-ru/map-en.json` line 109 maps `…“Black Friday”: sales from 16 November` from a W46 TM value whose Chinese source used full-width `“黑色星期五”` (correct in Chinese typography); the English translation kept curly quotes, which render full-width in the CJK font. Straight apostrophes in the same font are fine (3.75 pt advance, P2 band verified). The P7 `“чёрной пятнице”` pair is in Newsreader (proportional) and renders fine.
- Scope: affects BOTH PDFs (the defect is in the SVG itself, in the CJK font).
- Severity: minor — text fully legible and correct; only spacing is wrong. Same mechanism as the U+2019 defect class the program treats as a defect, in fan-out-added text, so it is a defect, not an observation.

## Defect D2 — minor: web PDF only — "14-й" hyphen-split spans open a spurious gap ("14- й")

- Location: web PDF `Lucerna-VOL4-ru-en-web.pdf` only. Print PDF is clean at every instance.
- Original (web, rendered): P1 headline reads `14- й тур: «Зенит» и «Динамо» — по 31 очку` (gap between `-` and `й`); P4 section heading reads `14- й тур: все восемь…`
- Should be: `14-й тур…` tight, as in the print PDF.
- Evidence (span-box measurement, PyMuPDF `get_text('dict')`, same span in both PDFs):
  - P1 headline, 39.8 pt: `14-` span box ends x=128.6 (web) vs 133.0 (print); next span `й тур` starts x=133.0 in both → 4.4 pt box gap; ink gap 2.75 pt at 4× zoom. Confirmed visually in `crops/crop-headline-web.png` vs `crops/crop-headline-print.png`.
  - P4 section heading, 24 pt: `14-` ends x=103.8 (web) vs 106.5 (print) → 2.6 pt gap. Confirmed visually in `crops/crop-p4head-web.png` vs `crops/crop-p4head-print.png`.
  - Full abutting-pair scan over all 8 pages (1,349 consecutive abutting span pairs, same line, same span count): gaps > 0.5 pt in web at only 7 spots — P4 24 pt `14-`|`й тур` 2.6 pt; P1 15 pt `1. 14-`|`й тур` (contents item 1) 2.2 pt; P4 13.5 pt ` все восемь результа`|`+` 1.9 pt; P1 15 pt `3. «`|`Чёрная пятница` (contents item 3) 1.1 pt; P5 24 pt `«`|`Чёрная пятница` (band title) 0.9 pt; P7 16.12 pt `«`|… 0.6 pt ×2. All other 1,342 pairs ≤ 0.5 pt (mostly 0.0–0.1 pt). The P1 39.8 pt headline pair was measured directly (its two spans have different bbox y0, so the line scan did not pair them).
  - Mechanism: the web font subsetting renders the run before a span break slightly narrower than the print font while the following span keeps its absolute SVG x, so a gap opens exactly at hyphen/quote span boundaries. Web-only; the SVGs and print PDF are unaffected.
- Severity: minor — text remains legible; the worst instance (P1 headline, 4.4 pt) is plainly visible on the web front page. Tool-level fix (webpdf.py font subsetting), not an edition-content fix.

## Observations (not defects)

- O1: P7 `check_core` orphan flag (p7 y553 `”».`): false positive. The node is the last node of the complete line `«на “чёрной пятнице”».` at y=552.6 (verified in SVG nodes + 3× crop) — visually complete, same benign class as core per KIT §7.
- O2: P1 same-baseline collision (y1712 italic «чёрная пятница»): same as core per KIT §7; visually fine.
- O3: "·" (U+00B7) separators used systematically — MCQ options (`A. 31 · B. 29 · C. 26`), gloss lists in Note boxes, top strip — counts P1 10, P2 13, P3 13, P4 12, P5 13, P6 10, P7 6, P8 37. Core-identical content punctuation (present in `.text.md` stems); the §1.1 no-`·` rule targets masthead/footer/page furniture, which comply (footer uses U+3000 full-width spaces). Extending the rule to options/glosses would be a program-level decision, not a per-edition defect.
- O4: Key 139 "On Tuesday Russia play Venezuela." uses British-English plural agreement for a national team; key 51's note uses the same form ("The national team play in Krasnodar…"). Internally consistent with the edition's British date format ("17 November"); standard BBC-style sports usage. Not flagged.
- O5: Key 140 "Happy Students' Day to everyone!" adds "to everyone" to the Russian "Поздравляю с Днём студента!" — standard English greeting equivalent; not flagged.
- O6: P5 dates box omits "предварительно" for Yandex Market 25–27 Nov (article says "предварительно с 25 по 27 ноября"); a summary-box compression, not flagged.
- O7: "Дедмобиль" release date: edition says 19 Nov per the latest Karo Premier/Mosfilm announcement (23 Oct 2026); older sources say 20 or 26 Nov. Not flagged.
- O8: KIT known rulings reconfirmed, not re-flagged: P8 stem 10.35 pt keeps core value; P8 «Морозко» image skipped by design (keys end col 3 y≈2288, condition `img_y+250+90=2652 > 2560`); `.text.md` "— СТРАНИЦА? —" separator and trailing «Морозко» credit line match core exporter format; narrow (4–6 px) word spaces where a Cyrillic run meets a Latin gloss are normal (same class as core); no drop cap.
- O9: Masthead "Lucerna" wordmark checked: masthead ink width print 1330.7 pt vs web 1330.0 pt — identical; the 8.3 pt span-bbox difference in the text layer is not a visible defect (the wordmark is drawn as paths, not a text span).
- O10: During this proofread the system file-watcher reported an external change to `~/MEMORY.md` (unrelated to this task): cover-motion secondary conversions reached 113/144 in repo with 31 cells staying still (4 policy refusals + 27 merit: 18 size-floor, 5 frame-merge, 4 off-by-one), 0 remaining; W45 fr-1 succeeded; W46 zh-tw-1 orphan re-converted and passed. No action taken.

## What was verified clean (summary; detail in GATE-LOG.md)

- Visual: all 8 pages re-rendered from SVG by me (CairoSVG via `tools/venv/bin/python`, 975×1350, did not trust builder's `cards/`) and read in full; web P1/P8 rendered from the web PDF at 150 dpi and read in full. No overflow, overlap, clipping, or missing content (except D1/D2 spacing).
- 150 questions: all stems/options/keys rechecked against the articles; printed key lines verified verbatim (whitespace-insensitive) 150/150 + 8/8 page separators; registry distribution matches KIT (by page 10/18/18/18/18/18/12/38; A2 50/B1 76/B2 24; fill-in 54, MCQ 42, matching 20, sentence building 12, rewrite 4, cloze 13, translation 4, writing 1); model text 97 words.
- Golden sentences: 8/8 verified verbatim ×2 (source page + P7 list), page refs correct (P1×2, P2×1, P3×1, P4×1, P5×1, P6×2).
- Translation layer: explanation/interface English throughout; E keys 137–140 in English (verified values); 0 CJK chars in visible SVG text (only `三色蛾` inside the moth `<title>` metadata, same as core); no Chinese residue; all CJK-derived literals correctly transliterated (Ded Moroz, Veliky Ustyug, Krylia Sovetov, Dynamo Makhachkala).
- Badges: 130 individual chips + 5 group chips (P2 25–28 A2, P3 39–42 B1, P4 57–60 B1, P5 75–78 B1, P8 141–144 B2), all levels match registry, 0 mismatches. Fills A2 `#5c6e30`, B1 `#46581f`, B2 `#37402f`.
- U+2019: 0 across all 8 SVGs; U+2018: 0; straight apostrophes render normally (3.75 pt advance).
- Ban-word scan (43,371 visible chars): 0 hits. VOL inventory: VOL.4 ×9 (masthead + 8 footers), VOL.3 ×1 (P4 correction sentence — expected), VOL.5 ×6 (teasers/disclosure — expected). Footer verified (U+3000 separators, "Page N of 8").
- ABSTRACT.txt: one English line, 355 bytes, no ASCII double quotes, names real topics + VOL.4 + A2–B2 + 150 exercises.
- P8 min font 9.75 pt (387 spans at 9.75 pt) — meets ≥9.75 pt.
- P8 note person names verified against public sources: Stallone ✓ (key 30), Elizabeth Holmes ✓ (key 32), Peter Farrelly ✓ (stem 44, Russian "Питер Фаррелли"). "Masha" is the fictional reading character; "Ded Moroz" is folklore. No sumo-wrestler-type romanization issue exists in this edition.
- Facts spot-checked vs public sources (2026-11-11): RPL round 14 — all 8 scores, 21 goals total (0:1, 1:2, 1:0, 4:2, 2:0, 2:1, 2:2, 0:1), Zenit & Dynamo 31 pts joint first, Spartak 29, Krasnodar & CSKA 26, Komarov 83' equalizer, Dynamo's 90+1' winner vs Fakel, Baltika–Dynamo Mkh 0:1 on 8 Nov, round 15 starts 20 Nov (Rostov–Krylia Sovetov) — all confirmed (Forbes, Sports.ru, Sport-Express, 8–11 Nov 2026). Film slate — I Play Rocky / Farrelly / Stallone biopic ✓; Paper Tiger / James Gray / Cannes 2026 competition ✓; You Can See Everything / A24 / Elizabeth Holmes ✓; Дедмобиль / Yuri Stoyanov, dir. Vladimir Kott, 19 Nov per latest distributor announcement ✓; Колотун и Волшебное королевство / 19 Nov 2026 ✓; Лес / Svetlana Tyulbasheva adaptation / 12 Nov ✓; Лиля / Lili Brik biopic, dir. Vera Storozheva / 12 Nov ✓. Weekdays verified (6 Nov Fri, 7 Sat, 8 Sun, 12 Thu, 16 Mon, 17 Tue, 18 Wed, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 27 Fri, 29 Sun, 30 Mon); November working days 20 (21 weekdays − 4 Nov Unity Day) ✓; practice chart 38/26/18/18 sums to 100% ✓.

## Evidence files (scratch-proof-ru-en1/)

`PROBE.txt`, `fresh/` (8 self-rendered PNGs + `web-p1.png`, `web-p8.png` + `-small` versions), `text/`, `golden-check.txt`, `golden-check2.txt`, `fonts-badges.txt`, `badges-check.txt`, `p8-extract.json`, `p8-compare.json`, `keydiff-md.txt`, `keynotes-diff*.txt`, `occlusion.json`, `adjudicate-mine.txt`, `crops/` (16 zoom crops incl. `crop-headline-print.png`, `crop-headline-web.png`, `crop-p4head-print.png`, `crop-p4head-web.png`), `freeze/` + `freeze.json`, `print.txt`, `web.txt`, `rerun/` + `rerun-log.txt`, `banwords.txt`, `PROOF-NOTE.md` (this file), `GATE-LOG.md`.
