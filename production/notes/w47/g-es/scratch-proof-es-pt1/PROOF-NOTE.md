# PROOF-NOTE — W47 es-pt (Spanish target × Portuguese reader), proof1

- **Proofreader:** proof1 (independent), 2026-11-11
- **Object:** `production/2026-w47/2026-w47-es-pt/` (build 4, per WEEKLY-KIT.md §8)
- **Verdict: (b) — NOT ready. Two light defects, both in the fan-out (this edition) layer.**
  Per SOP §8.4, D1 + D2 require fix + full re-render + a fresh full proofread round before 定稿.

## Object verified (SHA-256, re-checked immediately before writing this note)

| File | Bytes | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4-es-pt.pdf` (print) | 3,500,787 | `4793edeb87c2d6cd138906bbdeb0c2fc47088c91a11d99e75582b71daafde4e0` |
| `La-Lucerna-VOL4-es-pt-web.pdf` (web) | 847,463 | `d7429fcb83d70735f38587527d0fcc1032389d891e94b12b7dba4ad4ee4776ef` |
| `2026-w47-es-pt.text.md` | 44,990 (1,797 lines) | `d3e4bd818b51f19bbea2c52dd1f5664bd342ea497d96f6180ae05b3f350b7a2f` |

All three match the task brief and KIT §7. Probe OK before starting:
`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` →
`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`; scratch write OK. `/tmp` was full;
`TMPDIR` pointed at this scratch's `tmp/` throughout. `/tmp` showed 503M free at probe
time; disk 76G free on /home. `git status` showed unrelated W43 modified files
(other work in progress — not touched).

Sources read in full: `SOP.md` §1.1 + §8, repo `AGENTS.md`, edition `WEEKLY-KIT.md`.
Methodology template: `scratch-proof-es-fr1/` PROOF-NOTE.md + GATE-LOG.md.

---

## Defects

### D1 — LIGHT, this edition (fan-out layer) — P1 box-title overflow

**Location:** P1, middle column, cream box `LA SEMANA EN CIFRAS　Em números`
(box x=538..961, y=1288; title x=556.5, baseline y=1324.7, fs=23 bold Noto Sans CJK SC).

**Evidence (measured, not estimated):**

- PIL advance-width of the title with its real font/weight: right edge **971.9**,
  i.e. **+10.9 past the box edge (961)**.
- PNG ink measurement: rightmost ink x=**968** at y=1322, i.e. **+7 px** past the edge.
- Cream edge confirmed at x=961 by row scan (cream spans 540..960 at y=1330).
- Visually confirmed in crops `crop-p1-title-row.png`, `crop-p1-title-right.png` and in
  the full P1 render: the final `s` of `números` sits on white paper.
- No collision with the next column (its text starts x=989; 21 px clearance), so this
  is a box-edge overrun, not a text-on-text overlap.

**Root cause:** the Portuguese gloss `Em números` is too long for the box; the core's
Chinese gloss fits. Fix suggestion (builder's call): shorten the gloss to `Números`
(as in en) or reduce the title size.

**Same defect class elsewhere:** es-fr has the same overflow (advance right 977.8,
+16.8) — missed by its proof, which relied on the occlusion audit. The occlusion
audit's BOXTITLE class only checks rects with a stroke or fill `#2c2822`; cream boxes
(`#f0eee5`, no stroke) are excluded — which is why the boxtitle gate was run explicitly.
es-de / en / it fit.

### D2 — LIGHT, this edition (fan-out layer) — P8 answer notes mix Brazilian Portuguese into a European-Portuguese edition

Four instances, one root cause — the KIT §6.4 note-tightening pass (build 2 → 4).
All four confirmed as printed in `p8-ejercicios.svg` and in the P8 render:

| # | As printed | European-PT form | Note |
|---|---|---|---|
| 67 | `As seções abrem das 9:00 às 20:00` | `As secções abrem…` | #150 itself uses `secção` |
| 71 | `papeleta = cédula` | `papeleta = boletim de voto` | the edition's own P5 Note and #148 say `boletim`; in EU-PT `cédula` chiefly means banknote |
| 74 | `censo = cadastro eleitoral` | `censo = recenseamento eleitoral` | P5 Note says `o caderno eleitoral` |
| 96 | `fato conhecido` | `facto conhecido` | |

**The edition norm is unambiguously EU-PT:** tu-forms (`vais`, `ouviste`, `Votarias`,
`comprarias`), `até ao fecho`, `secção`, `adeptos` over `torcedores` (KIT §7 manual
override), `bilhete de identidade` (#146). Fix: align the four notes to EU forms.

---

## Observations (not defects)

- **O1:** P2 `ley.` ink +0.07 and P5 VOTAR box `compara precios antes de pagar.` +0.05 —
  at the edge but not over; Spanish frozen text, identical in core. Same as es-fr1 O1.
- **O2:** #56 note `más + importante (a luta pelo título)` is a surplus interpretation
  (the stem has nothing to do with the title race); the fact is not wrong (Barça does lead).

## Core-level candidates (report to coordinator; NOT es-pt defects)

- **C1 — Nov 13 laSexta debate theme (frozen core).** The paper says economy only;
  quadratin.com 2026-11-10 and diarioenpositivo.com 2026-11-06 describe Nov 13 as
  economy + housing (`economía, vivienda y actualidad` / `debate sobre vivienda y
  economía`). Core KIT §6.10 already adjudicated economy-only citing
  diariodesantiago.es 2026-11-06. Insufficient to overturn, but the coordinator may
  re-check before VOL.5. Same as es-fr1's C1.
- **C2 — RTVE free-minutes split presented as JEC-settled (frozen core, P6).**
  The paper prints, with a bar chart: PSOE 45 / PP 45 / Vox 30 / Frente Amplio 30 /
  Podemos 15 min, plus Frente Obrero / PCTE / SALF 10 each — "Junta Electoral
  Central: 195 minutos en total, del 13 al 27 de noviembre". The arithmetic is
  internally consistent (45+45+30+30+15+10×3 = 195), and P8 keys #83–85 faithfully
  carry the same numbers. But live reporting (diariodia.es, 2026-11-01, updated
  2026-11-09) shows the split is **actively disputed before the JEC**: Frente Amplio
  and Podemos are contesting the inheritance of Sumar's 2023 electoral rights; the
  JEC commission's first meeting was Nov 4, and the RTVE propaganda-slot proposal had
  not yet been presented at that date. Core KIT §5.3 cites queproponen.es as its
  source; I could not retrieve that page in search to independently confirm the split.
  **Not verified as settled fact as of 2026-11-11; recommend the coordinator re-check
  before the issue's publication window (Nov 16–22).** If the JEC decides otherwise
  (e.g. Podemos 10 not 15, or the Sumar share split), the P6 item and P8 keys #83–85
  must be corrected. This is a core matter — the fan-out did not introduce it.

## Mechanism-level observation (report; not a blocking defect for this edition)

- SOP §1.1 says Latin-reader explanation layers use Newsreader, but every W47 Latin
  fan-out renders them in **Noto Sans CJK SC** (verified in es-pt, es-fr/de/en/it,
  en-pt), and the shipped W46 es-fr web PDF embeds `LucernaNotoSansCJKSC` — i.e.
  uniform across production, previously proof-passed and shipped, fixable only by a
  mechanism change, not at edition level. Same for body text using `#302c28` instead
  of SOP's `#3a3631` (0 occurrences of `#3a3631` in both core and edition).

---

## Gates summary (all actually run — see GATE-LOG.md for commands and full tables)

| Gate | Result |
|---|---|
| Occlusion audit (formal, no --selftest) | **0 flags**; selftest all six classes fired (BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX) |
| p8 extract | **150/150** |
| p8 compare vs core-es | CLEAN; missing=[] extra=0; keydiff=[137, 138] (adjudicated translation items, W45/W46 ruling) |
| Freeze baseline | **8/8 byte-identical** (first run 0/8 was my own `--core-svg` error — see GATE-LOG) |
| Freeze diff | added CJK = 0 total |
| keycheck (REG vs P8-extracted) | REG 150; A2 50 / B1 72 / B2 28; per page P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38; MODELO 97 words; **149/150 exact** — only #150 differs by its adjudicated rendered form (REG key `Questão aberta — texto modelo abaixo, nesta página`, extracted `✓`; script exits RC=1 only because its `expected_only` predicate expects a prefix match). Not a defect. |
| creambox.py full scan + PIL ink measurement | All 22 cream boxes inside. Tightest ink clearances: P5 VOTAR `compara precios antes de pagar.` **+0.05**; P2 `ley.` **+0.07**; P7 CARTAS +1.45; P2 ¿Y TÚ? `envia-as à redação.` +1.54; P5 ¿Y TÚ? `frases e envia-as.` +1.62; P3 ¿Y TÚ? `envia-as.` +1.72; P4 ¿Y TÚ? +1.75. P7 toolbox: ERRORES ink +38.01 (baseline +42.5); LA PALABRA +21.22; CARTAS +1.45. Six negative baseline clearances are false positives (below-box headings/notes, same coordinates as core — verified via diag). |
| Print/web text layer | `pdftotext` both 45,996 B, byte-identical (`cmp` clean); both PDFs 8 pages |
| P8 minimum font (PyMuPDF spans, print = web) | **10.125 pt** — KIT's claim verified correct this time; other pages 11.62–12.75 pt; ≥ 9.75 pt floor ✓ |
| boxtitle text_w (all 27 titles, real font/weight) | **One overflow — D1.** All other 26 positive (minimum +9.0, P7 LA PALABRA) |
| Curly quotes U+201C/U+201D/U+2019 | 0 in all SVG text and in text.md (the "P7 Newsreader italic pair" exception is moot — none exist); guillemets « » balanced 56/56; 0 ASCII apostrophes/straight double quotes in text.md |
| §1.1 fonts/colors | paper `#fbfaf6` ×8; masthead UnifrakturMaguntia 196 units ×1; VOL.4 ×9, VOL.5 ×3 (legitimate forward refs); P8 chip rects 35 (A2 `#5c6e30` 11 / B1 `#46581f` 21 / B2 `#37402f` 3); no gold/brick-red (moth yellows `#D7B257`/`#EDD17F` only, as in core); CJK in SVG `<text>` = 0 on all pages; U+3000 total 118; moth `<title>Lucerna 三色蛾</title>` present (non-rendered, as in core). Fill census vs core-es: no new colors introduced by the fan-out. |
| Dates (`date -d`, Europe/Madrid) | 2026-11-13 Fri, 11-16 Mon, 11-19 Thu, 11-20 Fri, 11-22 Sun, 11-24 Tue, 11-25 Wed, 11-26 Thu, 11-27 Fri, 11-28 Sat, 11-29 Sun — all match the paper's weekday claims |

**Methodology warning for whoever continues:** text.md interleaves columns row-wise,
so naive linear reading misassigns stems to numbers (this nearly misjudged P6 Q83–100);
the SVG column-major (COLX ≈ [88, 538.5, 989, 1439.5]) + y-order layout is authoritative
(`extract_items.py` → `items-150.txt`).

## 150 answer keys — semantic verification (all hand-checked against the stems as laid out in the SVGs)

- All 138 items extracted by layout + the 12 matching items (25–28 / 52–55 / 141–144)
  verified separately: **all correct**.
- Matching: 25=c, 26=b, 27=d, 28=a; 52=c, 53=b, 54=a, 55=d; 141=c, 142=d, 143=b, 144=a.
- Golden sentences 8/8, each exactly 2× (original + P7 quote); page refs
  P1/P4/P2/P5/P3/P6/P3/P6 all correct.
- Model text counted 97 words ✓.
- Per-page Note-word counts match KIT exactly (P1 reflexión 2; P2 mitin/cartel/escaño 2;
  P3 cante 5/toque 6/baile 9/compás 4/duende 6; P4 parón 2/liderato 3; P5 papeleta 2/
  censo 3/plazo 3). P8 answer notes (Portuguese) read fully.

## External facts verified online (2026-11-11)

| Fact | Verdict | Source |
|---|---|---|
| Election calendar: RD 806/2026 (BOE 2026-10-06); vote Sun 2026-11-29 9:00–20:00; campaign Fri Nov 13 00:00–Fri Nov 27 24:00 (15 days); reflection Sat Nov 28; no polls Tue Nov 24–Sat Nov 28 (LOREG art. 69.7) | ✓ | BOE / JEC calendar |
| UNESCO flamenco declared 2026-11-16, 2010, Nairobi | ✓ | UNESCO |
| LaLiga MD13: all six fixtures/times (Athletic–Espanyol Fri 21:00 San Mamés; Sevilla–Betis Sat 18:30; Real Madrid–Celta Sat 21:00; Barça–Villarreal Sun 14:00; Getafe–Atlético Sun 21:00 Coliseum; Levante–Elche Mon 21:00; round Fri 20–Mon 23); standings Barça 33, Madrid 30, Atlético 28, Betis 26; Atlético–Barça 1–2 Sun 2026-11-08 at Metropolitano (Fermín brace) | ✓ | LaLiga / match reports |
| UCL MD4: Barça 3–0 Aston Villa Nov 3; Atlético 0–2 Bayern Nov 3; AEK 2–3 Real Madrid Nov 4. MD5: Real Madrid–PSV Tue Nov 24 21:00; Sabah–Barça Wed Nov 25 18:45; Atlético–Viking Wed Nov 25 21:00; Villarreal and Betis also play MD5 | ✓ | UEFA |
| MiDNI: JEC Acuerdo 342/2026, session 2026-11-05, lifts MiDNI suspension (MiDGT stays suspended) | ✓ | JEC |
| Debates: laSexta Nov 13 21:30, Ana Pastor moderating, Cuerpo (PSOE) / Bravo (PP) / Bustinduy (Frente Amplio) / Figaredo (Vox) confirmed; SER debate Nov 18 on vivienda, Bravo vs Isabel Rodríguez; Atresmedia debate-a-cuatro moved to Mon Nov 23 (Feijóo, Abascal, Colau confirmed; PSOE invited, unconfirmed); RTVE debate-a-cuatro Nov 26; PP proposes cara a cara Sánchez–Feijóo Mon Nov 16 (Mediaset) | ✓ | laSexta / SER / Atresmedia / RTVE reporting |
| Frente Amplio is a real 2026 Spanish formation (Bustinduy minister; Colau its candidate) | ✓ | press |
| Bilbao Municipal Band: Sun Nov 22, 12:00, Palacio Euskalduna | ✓ | teoriamusical.com.es, checked against official source |
| Sargent `«Bailaora española»` (1880–81) | ✓ | Google Arts & Culture: *Spanish Dancer* (1880–1881, private collection), the rediscovered full-size preliminary painting for *El Jaleo* |
| Postal vote: documentation dispatched from Mon Nov 9; application deadline Thu Nov 19 (inclusive); deposit by Wed Nov 25; scrutiny Fri Dec 4 | ✓ | Correos official note 2026-11-10; LOREG art. 72 |
| RTVE free-minutes split (PSOE 45 / PP 45 / Vox 30 / FA 30 / Podemos 15 + 3×10 = 195), presented as JEC-settled | **unverifiable as settled — see C2** | diariodia.es 2026-11-01 (upd. 2026-11-09): FA vs Podemos dispute pending before JEC; RTVE proposal not yet presented |
| Nov 13 laSexta debate theme: economy only | **contested — see C1** | quadratin.com 2026-11-10, diarioenpositivo.com 2026-11-06: economy + housing; core KIT §6.10 adjudicated economy-only (diariodesantiago.es 2026-11-06) |

## Visual check of the 8 rendered PNGs (`cards/p1-portada.png` … `p8-ejercicios.png`)

- **P1:** only D1 visible (final `s` of `números` past the cream edge). Banner, CINCO
  CLAVES bars, ballot-box illustration, quiz strip, footer all clean.
- **P2:** clean. ¿Y TÚ? last line `envia-as à redação.` inside its box. `D LAS PALABRAS`
  header at the bottom of column 3 with items in column 4 — layout as frozen, not a defect.
- **P3:** clean. Sargent image matches its caption; ¿Y TÚ? last line `envia-as.` inside.
- **P4:** clean. MD13 table and LA CHAMPIONS VUELVE box match the verified fixtures/results.
- **P5:** clean. VOTAR box last line `compara precios antes de pagar.` inside; ¿Y TÚ?
  `frases e envia-as.` inside. Bronze ballot-box photo matches its caption
  (`SUFFRAGE UNIVERSEL`).
- **P6:** clean. RTVE bar chart renders correctly (bars aligned, no overflow); EL CAMINO
  AL 29N and ¿POR QUÉ NO HAY ENCUESTAS? boxes fine. (The chart's *numbers* are C2.)
- **P7:** clean. ERRORES TÍPICOS / LA PALABRA / CARTAS boxes all inside their cream;
  medieval book-of-hours image matches its caption; golden sentences + page refs correct.
- **P8:** clean. All 150 keys legible; the four D2 Brazilianisms confirmed in print
  (#67 `seções`, #71 `cédula`, #74 `cadastro eleitoral`, #96 `fato`); #150 uses the
  adjudicated `✓` form with `secção`. Plume image matches its caption.

No new visual defects beyond D1. No overlap, no footer intrusion, no image-caption
mismatch on any page.

## Conclusion

**(b) — Two light defects, both in this edition's fan-out layer:**

1. **D1 (light): P1 box-title overflow** — `LA SEMANA EN CIFRAS　Em números`, ink +7 px
   past the cream-box edge (advance +10.9).
2. **D2 (light): P8 answer notes, 4 Brazilian-Portuguese forms in an EU-PT edition**
   — #67 `seções`, #71 `cédula`, #74 `cadastro eleitoral`, #96 `fato`.

**Escalations for the coordinator (not es-pt defects):** C1 (Nov 13 debate theme,
economy-only vs economy+housing) and C2 (RTVE minutes split presented as JEC-settled
while the FA/Podemos inheritance dispute is pending before the JEC).
**Mechanism observation:** explanation layers render in Noto Sans CJK SC, not
SOP §1.1 Newsreader; body `#302c28` not `#3a3631` — uniform across production,
mechanism-level only.

**Fix + full re-render + fresh full proofread round required before 定稿 (SOP §8.4).**
No source files were modified, rebuilt, committed, or pushed by this proof.
