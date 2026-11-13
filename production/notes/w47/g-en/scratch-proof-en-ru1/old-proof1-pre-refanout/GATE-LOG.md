# GATE-LOG — Lucerna Weekly 2026-W47 en-ru, proof1

- **Edition:** en-ru, VOL.4
- **Date:** 2026-11-11
- **Probe:** `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`; probe file written in scratch dir. `/tmp` was 2% used at probe time (not 100% as brief warned); all intermediates placed in scratch with `TMPDIR=<scratch>/tmp`. Nothing written to /tmp; no other agent's files touched.

## Object SHAs (verified on disk, re-checked 2026-11-11)

| File | Size | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-ru.pdf` (print) | 29,241,566 B | `788cd0c08ec9b72fd52c8a65b4aadacb05e27980369295d7df0b726eb82efd70` |
| `The-Lucerna-VOL4-en-ru.web.pdf` (web) | 2,417,491 B | `da80486218d001cc6dc09e4107391cf81b15d1dde7f5c3b6d8e0aeb5f2ffe77a` |
| `2026-w47-en-ru.text.md` | 61,835 B | `5e8f7bf4f8e4b9d8c70c275f92e178fa03ee5b48b58da690f248415ab289dacb` |

All three match the brief exactly. Both PDFs 8 pages, 1462.5×2025 pt. KIT `WEEKLY-KIT.md` read in full (builder claims all gates green; 150 exercises, per-page 10/17/18/18/18/18/12/39, A2 62 / B1 66 / B2 22, MODEL words 82) — claims re-verified independently below, not taken on trust.

## Gate results

### 1. Full-text read — PASS (with 2 findings, see PROOF-NOTE.md Defects 1–2)
- text.md read completely (~1,306 lines).
- 150 keys hand-verified against stems: **148/150 correct**. Wrong: Q39 mentor→d (must be a), Q40 arena→a (must be d). All other matching blocks verified: Q24–27, Q56–59, Q74–77, Q141–144 (mechanical log: `gates/matching-check.log`).
- Q108 correction drops "in 2026" from the error sentence — grammatical, not a defect.
- Minor nit: P5 "У каждого ребёнка есть права | Every child has rights = У каждого ребёнка есть права." — redundant Russian repeated; core-rooted.

### 2. Occlusion audit — PASS, 0 flags
- `tools/occlusion_audit.py` on `svg/` → RC=0, selftest OK (all 6 classes fired), **0 flags**.
- Files: `gates/occlusion.json`, `gates/occlusion.log`.

### 3. P8 extract + compare — PASS (CLEAN, expected keydiff)
- Core 60/150 noted, edition 60/150 noted, same set; **compare CLEAN**, missing=[] extra=0.
- **keydiff [137,138,139,140,150]** — all expected per KIT (137–140 RU translation keys, 150 writing key).
- Extract keys 150/150 vs registry, missing none.
- Files: `gates/p8-extract.json/.log`, `gates/p8-extract-core.json/.log`, `gates/p8-compare.json/.log`.
- Note: `keycheck.py` was copied to `gates/` but NOT run — it compares REG vs P8-extract and cannot catch a wrong key inside REG itself (the Q39/40 swap is in REG); stem-vs-key check was done by hand + mechanically for all 5 matching blocks instead.

### 4. Freeze — PASS, 8/8
- Baseline 8/8 byte-identical; direct sha256 re-render vs shipped core SVGs 8/8 MATCH.
- Diff added CJK = 9× U+3000 only (2+1+1+1+1+1+1+1 per page).
- Files: `gates/freeze.log`, `gates/freeze-diff.json/.log`, `gates/freeze-final/`.

### 5. check_s11.py (ru) — PASS
- ALL §1.1/P8 CHECKS PASS: colour set core 19 = edition 19; badges A2 #5c6e30 / B1 #46581f / B2 #37402f; P8 min SVG font 13.5; Q113–120 [A2] tags; "Levels: 145–149 [A2]"; "H WRITING Письмо [B1]".
- Files: `gates/check_s11.py`, `gates/check_s11.log`.

### 6. Print / web text identity — PASS
- pdftotext both: 47,093 chars, 2,523 distinct tokens, token-multiset diff 0.
- Web PDF text layer present (2,417,491 B).
- File: `gates/printweb-diff.log`.

### 7. P8 min font — PASS
- PyMuPDF on print PDF: answers render at **10.12 pt** (13.5 SVG px × 3/4); ≥9.75 pt SOP §1.1 floor → PASS.
- KIT's "13.5 pt" label conflates SVG px with pt — wording nit only. Photo credit 11.62 pt. P1 min 11.62 pt.

### 8. Quotes / apostrophes / banned words — PASS
- text.md U+201C 81 / U+201D 81 (balanced); SVGs per page 201C=201D (2/1/10/3/11/2/29/24 = 82 total); U+2019 = 0 everywhere (apostrophes are ASCII ', 40 in text.md); U+2018 = 0.
- **0 Cyrillic-adjacent curly quotes in all 8 SVGs** → no full-width quote misuse.
- The brief's P7 "чёрной пятнице" exception does NOT occur in this edition (lowercase "чёрной" appears nowhere; only capital "Чёрная пятница" unquoted in P2) — nothing to judge.
- Banned-word scan (桥接/SOP/proofread/cover/TODO/FIXME/XXX/lorem/占位) = 0 hits.
- File: `gates/quote-diff.log` (naive strip-tags comparison is noisy due to lost spaces; raw counts above are authoritative).

### 9. Creambox (mandatory P7 toolbox scan) — PASS for P7; defects found on P2 (see below)
- Raw `creambox.py` shows many −35.5/−37.0 "clearances" — **proven to be a tool artifact**: identical pattern in core-en control (same boxes, same last-baseline texts). The tool takes max() within bottom+45px, i.e. it reports the next block's first line below the box.
- Corrected computation (last baseline INSIDE each box): all boxes' own last lines sit inside with padding +4.5 to +92.4 (mostly +47.7/+48.1). P7 visual confirms toolbox contents fully inside cream.
- Files: `gates/creambox.log`, `gates/creambox-core.log`, `gates/creambox-true.log`.

### 10. Horizontal / vertical containment (PyMuPDF on print PDF) — 3 DEFECTS
- The +6.0/+13.7 "V-SPILL" entries are next-block headings/body text below boxes (design spacing), NOT defects.
- **D1 — P2 DID YOU KNOW? box:** last line "November 3." straddles the box bottom edge (rect bottom 868.8 pt; span top 866.5, baseline 882.6; 663 ink px below bottom; zoom crop confirms cream edge cuts through the line). **Identical in core-en (same 663 px) → core-level.**
- **D2 — P2 SAY IT mini-boxes 1–2:** Russian translation lines overflow the 280 px cream boxes horizontally. RU line 1 ink x 103–490 vs box [159,439] (56 px left, 51 px right); RU line 2 ink x 571–924 vs box [610,890] (39 px left, 34 px right); EN line 2 "The new Congress meets in January." ink x 574–931 vs box [610,890]. **EN line 2 overflow identical in core-en → core-level**; RU lines 1–2 overflow is en-ru-specific (core Chinese lines fit: widths ~126–166 px vs Russian ~350 px; texts centred on box centres so spill is symmetric). Box 3 fits. Visual crop confirms Russian text on white outside cream.
- **D3 — P3/P4 col-3 box titles overflow cream-box right edge (boxtitle widths, PDF spans):** P3 "HAYMITCH'S GAMES　Игры Хеймитча" 323.8 pt vs budget 303.4 pt → **OVER by 20.4 pt (~27 px)**; P4 "SATURDAY, NOVEMBER 21　Суббота" 311.5 vs 303.4 → **OVER by 8.1 pt (~11 px)**. Other 8 col-3 titles pass (8 pass / 2 over). Core comparison: core P3 title 290.2 pt PASSES (P3 is en-ru-specific); core P4 title 307.0 pt OVER by 3.6 pt (P4 overflow exists in core, worse in ru). Titles stay within column/page, legible. Full-width crop of P3/P4 confirms the gloss tails sit on white past the cream edge.
- Files: `gates/h-containment.log`, `gates/boxtitle-ru.log`, `gates/boxtitle.py`; renders `render/p2-didyouknow.png`, `render/p2-sayit.png`.

### 11. Visual checks — PASS (except D1–D3 above)
- Print cards P1–P8 all viewed; web P1 + P8 rendered via pdftoppm (`render/web-p1-1.png`, `render/web-p8-8.png`) and viewed — web matches print. P7 viewed first (toolbox clean).
- No other overflow/overlap/truncation/footer-intrusion on P1, P3, P4, P5, P6, P8. Footers "Страница N из 8" present all pages; masthead/edition line/badge correct.

### 12. External-fact verification — PASS except Defect 2 (Ashes)
- All verified 2026-11-11 via web search; see PROOF-NOTE.md "Verified clean" for the item-by-item list.
- **Midterms:** AP Nov 8 count Dem 254 / GOP 162 / 19 uncalled; Senate 20–13, 2 uncalled (Alaska, Mississippi); 7 flips; 5 governors; 218–214 / 53–47 going-in; new Congress Jan 3, 2027; House GOP leadership elections Nov 10; Johnson will not run (NBC/AP Nov 4); House Dems Nov 18–19; Georgia majority rule, runoff would be Dec 1 (conditional phrasing accurate; Ossoff won outright Nov 3).
- **Anti-Bullying Week, I'm a Celebrity, Hunger Games (film + soundtrack album Nov 13), ATP Finals, NFL Week 11, Premier League** — all exact as printed.
- **ASHES — FAIL (Defect 2):** 2025–26 Ashes first Test was Nov 21, 2025 at Perth (Australia won by 8 wickets in 2 days); no Ashes Nov 2026.
- Calendar arithmetic verified via `date` (America/Toronto): Nov 3 Tue, Nov 8 Sun, Nov 9 Mon, Nov 10 Tue, Nov 15 Sun, Nov 16 Mon, Nov 18 Wed, Nov 19 Thu, Nov 20 Fri, Nov 21 Sat, Nov 22 Sun, Nov 26 Thu (Thanksgiving), Dec 1 Tue. 254+162+19=435 ✓; 20+13+2=35 ✓.
- Not separately verified (minor/hedged, no contradiction found): certification window Nov 10–Dec 18; "Patriots, after Munich"; W.G. Grace credit; Rousseau "Surprised!" 1891; Lawrence children photo Feb 19, 1912; Samuel Johnson portrait (Reynolds, 1772); LOC Reading Room photo (Highsmith).

## Standing rules honored
- SOP §8.4 proof loop: a full round with zero findings is required to call an edition final; defects found → verdict (b).
- Core-level defects reported to the coordinator, core never touched.
- No source files modified, no rebuild, no commit/push; webpdf.py NOT re-run (would rewrite shipped web PDF); dump_reg.py NOT run (would write into edition dir); freeze baseline wrote only into scratch.
