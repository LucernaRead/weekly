# GATE-LOG — Lucerna Weekly 2026-W47 en-es · proof2 (Q73 delta rebuild)

Scratch: `hidden_files/w47/scratch-proof-en-es2/`. Runner: `run_gates.sh` → `gates-run1.log`. All runs in scratch copies; production untouched (final re-hash = task SHAs).

## 0. Probes & identity

- `/dev/null` present (`crw-rw-rw-` 1,3); `git hash-object -w --stdin` OK (`ce013625…`); scratch write OK (`probe.txt`).
- Print `6a249cc98f0dea9aa24d6b0af1db9480d9b030164f6ad083e4ff4f01249a70cb` / 29,331,230 B ✓
- Web `2bc163a375007387e0e09c0ef2395459688dd2d19aea2f6946ced68c5c1eb79c` / 2,414,439 B ✓
- text.md `314b32a3c3f236bec94ad6f1426664eb180cc8f96053cc886beed3eaacf217ca` / 54,385 B ✓
- Re-verified at end of round: identical SHAs/sizes.

## 1. Delta scope

| Check | Source | Value |
|---|---|---|
| Registry diff | `diff registry-pre.json registry.json` | exactly 1 line: `583c583` `"key": "speak"` → `"key": "up"` |
| text.md diff | `diff text-pre.md 2026-w47-en-es.text.md` | exactly 1 line: `1151c1151` `speak` → `up` |
| SVG scope | `svg-pre.sha256` vs `svg-now.sha256` | only `p8-test.svg` changed (`e565acaf…` → `1c7f8051…`); p1–p7 byte-identical |
| Source | `content56.py:49` | `f.ex("A2", "Completar frases", "up", "speak up = hablar sin miedo",` |

## 2. Q73 four-source

| Source | Value |
|---|---|
| registry.json[72] | key `up`, note `speak up = hablar sin miedo` |
| text.md:1151 | `73. [A2] Completar frases — up (speak up = hablar sin miedo)` |
| print PDF p8 / web PDF p8 | `73. up` (in `72. rights … · 73. up · 74. d`) |
| `p8-extract.json` | `"73": "up"` |
| P5 SVG | stem `Speak ___: tell a teacher.`; Nota `to speak up = hablar sin miedo`; box title `SPEAK UP　Alza la voz`; `75. to speak up`; Q79 `Children (speak) up this week.` |
| core-en registry[72] | key `up`; registry-vs-core keydiff = exactly 137–140, 150 (reader-language keys) |

## 3. Gates (each independently re-run; full output in `gates-run1.log`)

| Gate | Log | Result |
|---|---|---|
| run.py (runcopy rebuild) | `run.log` | rc=0; TOTAL exercises 150; MODEL words 82; OVERFLOW 0 matches; TOO WIDE 0; ALL DONE; P8-keys y=2443/bottom 2560 |
| freeze baseline (edition) | `freeze.log` | **8/8 SVGs byte-identical**; core integrity: shipped SVGs unchanged |
| freeze baseline (core-en, read-only) | `freeze-core.log` | **8/8 SVGs byte-identical**; core integrity unchanged |
| freeze diff vs core | `freeze-diff.log/json` | TOTAL added CJK 9, all U+3000 (p1:2, p2–p8:1 each); file byte-identical to delta's |
| occlusion (REAL audit, no `--selftest`) | `occlusion.log/json` | rc=0; **0 flags** (edition 0, core 0, NEW vs core 0); json identical to delta's |
| p8 extract core | `p8-extract-core.log/json` | noted set 60/150 (parse: joined) |
| p8 extract edition | `p8-extract.log/json` | noted set 60/150 (parse: joined); identical set to core |
| p8 compare | `p8-compare.log/json` (read directly) | **CLEAN**; missing=[] extra=[] uncertain=[]; keydiff=[137, 138, 139, 140, 150]; file byte-identical to delta's |
| check_s11 | `check_s11.log` | **ALL §1.1/P8 CHECKS PASS**; P8 min SVG font 13.5; colour set 19/19, extra none, missing none |
| boxtitle source | `boxtitle.log` | 12 measured, 0 over budget; tightest P1 +20.4 |
| boxtitle SVG | `boxtitle-svg.log` | 18 checked, 0 overflows; P2 SENATE +33.6, P6 HOW LONG +142.3 |
| creambox (PIL true ink) | `creambox-check.log` | **NO OVERFLOW**; 32 boxes; clearance +5.0 to +92.4 px (tightest P2 y=1211 +5.0) |
| verify_ed | `verify.log` | **VERIFY ALL PASS**; P8 min PDF font **10.12 pt ≥ 10 pt**; SVG zero real CJK |
| keycheck | `keycheck.log` | extract 150, registry 150, missing none; only mismatch #150 short-label exception (known); text.md 150 lines, 1–150 continuous, 0 mismatches |
| print/web text layer | `printweb.log` | print 48,255 chars / web 48,255 chars; token-multiset diff 0/0; per-page 8/8 byte-identical (P1 4956B, P2 5890B, P3 5309B, P4 5786B, P5 4694B, P6 5653B, P7 6051B, P8 9916B) |
| orphan punctuation | `orphan.log` | SVG 8 pages: start-closer 0, end-opener 0; text.md: 0 / 0; curly “ ” 81/81; SOP/proofread/TODO/PLACEHOLDER/Lorem/XXX/estadio/stadio = 0 |
| dates | `date` (America/Toronto) | Nov 3 2026 Tue, Nov 8 Sun, Nov 9 Mon, Nov 16 Mon, Nov 20 Fri, Nov 26 Thu, Nov 27 Fri, Nov 21 2025 Fri, Jan 8 2026 Thu |
| MODEL words | independent count | 82 (alphanumeric tokens) |
| ABSTRACT.txt | file | 1 line Spanish, 807 B |
| D5 fonts (count only) | `pdffonts-print.txt` / `pdffonts-distinct.txt` | pdffonts 43 lines (41 font rows + 2 header); **35 distinct font names**; no judgement, no fix |

## 4. 150-question hand verification

- text.md 1305 lines read in full (P1–P8 body + all 150 answer lines); every key checked against its stem.
- Matching-block SVG letter orders re-extracted and verified: P2 D 24→b, 25→c, 26→a, 27→d; P3 C 38→b, 39→a, 40→d, 41→c; P4 C 56→b, 57→c, 58→d, 59→a; P5 C 74→d, 75→a, 76→b, 77→c; P8 F 141→b, 142→c, 143→d, 144→a. Numbered terms in SVG match registry numbering.
- Arithmetic: 254+162+19=435 (Q87→C); 254−218=36. Q73 `up` verified (see §2); Q70/Q79 cross-checks verified.
- Result: **150/150 PASS**, zero defects. Known accepted items carried over from proof1: Q108/Q109 clinic corrections, P5 D-header column split (O3), P2 SAY IT Feliz edge (O4, pixel-clean).

## 5. Visual (8 pages, web PDF, 100 dpi, `visual/web-p-*.png`, 2032×2813)

| Page | Result |
|---|---|
| P1 | Clean |
| P2 | Clean (O4 Feliz edge only, accepted) |
| P3 | Clean |
| P4 | Clean |
| P5 | Clean — Q73 stem + Nota box + SPEAK UP box eye-verified |
| P6 | Clean |
| P7 | Clean — 8 golden sentences + page attributions eye-verified |
| P8 | Clean — `73. up` in ANSWERS eye-verified |

## 6. Verdict

**(a) — 定稿，零缺陷。** en-es 可定稿。No defects; observations O1–O7 are non-blocking (see PROOF-NOTE.md).
