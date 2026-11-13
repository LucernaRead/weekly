# GATE-LOG — W47 es-nl proof1 (independent proofread)

- Edition: `production/2026-w47/2026-w47-es-nl/` (Spanish target × Dutch reader)
- Proofreader: proof1 subagent, 2026-11-11
- Scratch: `hidden_files/w47/scratch-proof-es-nl1/`
- TMPDIR: scratch `tmp/` throughout (/tmp was full at task start)

## Identity (measured on disk, all match KIT §7 / task)

| File | Bytes | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4-es-nl.pdf` | 3,502,220 | `f88a21414c77508b8eb1a26af763e027fb5a1eed657b6fb576097ede8171dab1` |
| `La-Lucerna-VOL4-es-nl-web.pdf` | 850,386 | `85240de829be675577d03467f8697e8bf2f7814fb1de022a20f2290da9a4bcb3` |
| `2026-w47-es-nl.text.md` | 44,788 | `8801edefd46f58ea78beb576bb3a90e9babeb3c9e710def96ffef3578bcb0283` |

Both PDFs 8 pages, 1462.5 × 2025 pts. Git probe `echo test | git -C ~/workspace/weekly-git
hash-object -w --stdin` OK. `git status` showed pre-existing modified `issues/2026-w43/`
files — not mine; no source file was modified (SVG SHA before/after freeze identical).

## Mechanical gates (all actually run; KIT numbers not trusted)

| Gate | Tool / evidence | Result |
|---|---|---|
| Occlusion audit | `tools/occlusion_audit.py` (formal run, no `--selftest`) | exit 0, selftest OK (6 planted classes fired), **0 flags**; core 0; NEW vs core 0 |
| p8 extract | `tools/p8.py` | 150/150 |
| p8 compare | `tools/p8.py` | CLEAN, missing=[], extra=0, keydiff=[137, 138] (adjudicated in KIT §6.1) |
| Freeze diff | `tools/freeze.py diff` | added CJK = 1 char (U+3000, P1); core/es-nl both 118 U+3000, all title separators |
| Freeze baseline | `tools/freeze.py baseline` | **8/8 SVGs byte-identical**; shipped core SVGs unchanged (SHA before = after). Note: `freeze.py` has no `direct` subcommand (only `baseline`/`diff`); the baseline run is the freeze check. |
| Print/web text layer | `pdftotext` default / -layout / -raw | default 45,724 B both, byte-identical; -layout 108,639 B both; -raw 44,761 B both; whitespace-normalized raw identical; word multiset identical; per-page words identical (862/930/714/795/798/823/892/2056) |
| P8 min font | PyMuPDF, both PDFs | **10.125 pt** (≥ 9.75 pt floor); other pages min 11.625 / 12.75 pt |
| Keycheck (formal) | REG keys (`scratch-fanout-es/es-nl-keys.txt`, 150 lines) vs `p8extract.json` keys | **150/150 present; 149/150 exact** — only Q150 differs in form (REG "Open vraag — voorbeeldtekst hieronder op deze pagina" vs extract "✓", same content). See `keycheck-150.json` / `keycheck.log` |
| Level counts | REG dump | A2 50 / B1 72 / B2 28 ✓ (KIT) |
| Per-page counts | P8 SVG answer sections | 10/18/18/18/18/18/12/38 ✓ (P8 113–150; the "150." line is a split text element, counted by hand) |
| Cream-box ink sweep | `creambox.py` + true PIL ink boxes (`creambox-ink.log`) | 27 cream rects; **1 spill**: P5 ¿Y TÚ? +3.1 (see D3). Tightest inside: P2 "ley." −0.3, P5 "compara precios…" −0.4, P4 −1.3, P3 −1.9. P7 toolbox clearance +9.4 ✓. P1 "empty" rects (y=1874, y=1999) are the urn-illustration area (one is the lid `<path>`, not a text box). |
| Boxtitle text_w | `svglib.text_w`, right-edge rule, all 27 boxes (`boxtitle.log`) | **2 overruns**: P5 "EL PLAN DE LA SEMANA Het weekplan" −36.8 (D4); P7 "ERRORES TÍPICOS Typische fouten" −6.5 (D5). All other titles fit (tightest inside: P7 "LA PALABRA Woord van de week" +0.1, P1 "EN ESTA EDICIÓN In dit nummer" +6.0 — both visually confirmed on cream). Every body line inside every box also checked (right-margin < 3 flagged: only the two titles). |
| Curly quotes | U+201C/U+201D/U+2019 in SVG `<text>` per page | U+201C = 0 everywhere. U+201D: P1 ×1 ("„Debat”" Dutch gloss), P8 ×2 (key 91 "„Voorgesteld”/„bevestigd”") — all Dutch-style Latin typography, no CJK text in this edition (only U+3000 separators). U+2019 ×1: P6 "programma's". No CJK-context curly quotes. |
| §1.1 font/color audit | SVG font-family / fill census (`quotes-colors.log`) | Fonts: Newsreader 959, Noto Sans CJK SC 637, Noto Serif CJK SC 43, UnifrakturMaguntia 1 (masthead) ✓. UI/text colors exactly the spec set (paper #fbfaf6, book-green #37402f, olive #46581f, badge A2 #5c6e30); no gold/red-brown. Extra fills (#f6e08e ×10, #D7B257/#EDD17F, blues #4D72B4/#7898CD, greens #4F765D/#84A283) are inside the inline urn/moth illustrations only. P8 chips: 35 rx=2.7 rects = A2 11 / B1 21 / B2 3 ✓ (KIT). |
| VOL counts | SVG text | VOL.4 ×9, VOL.5 ×3 ✓ (KIT) |
| ABSTRACT.txt | file read | Single line, Dutch, 455 B, no ASCII `"` ✓ |
| Gloss tokens (§8.1, case-sensitive) | SVG text counts | P1 reflexión 2 ✓; P2 mitin/cartel/escaño 2 each ✓; P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 6 ✓; P4 parón 2 / liderato 3 ✓; P5 papeleta 2 / censo 2 / plazo 3 ✓ (case-insensitive censo=3 only because of proper noun "Censo Electoral") |
| P7 col3 / banner (KIT §6.6) | SVG coords + PIL ink + 150 dpi crop | Banner text ink bottom ≈2582.5 < footer rule 2596 ✓, BUT banner rect (y 2493.5–2611.5) is 29 units lower than core (2464.5–2582.5) and overlaps footer text ink top (2611.0) by 0.5 — footer cap-tops visibly sliced (see D6, `crop-p7-footer.png`). |
| Dates/weekdays | `date -d` (Europe/Madrid) | 13 Fri, 16 Mon, 17 Tue, 18 Wed, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 23 Mon, 24 Tue, 27 Fri, 28 Sat, 29 Sun; 10 Tue, 9 Mon, 5 Thu — all as printed ✓ |

## Visual inspection (own 150 dpi renders, `render/print-*.png` + `render/web-*.png`)

- All 8 print pages + web P1/P8 read in full. Crops (3×): P5 ¿Y TÚ? box bottom
  (`crop-p5-youtu-boxbottom.png` — descenders cross the cream edge), P3 box bottom
  (clean), P5 "EL PLAN DE LA SEMANA" title (`crop-p5-plantitle.png` — "weekplan" off
  the cream), P7 "ERRORES TÍPICOS" title (`crop-p7-errorestitle.png` — final "n" off
  the cream), P1 "EN ESTA EDICIÓN" title (fits), P7 bottom banner + footer
  (`crop-p7-bottom.png`, `crop-p7-footer.png` — footer caps sliced).
- P7 "FRASES DE LA SEMANA": all 8 quoted sentences verified verbatim against P1–P6
  articles, with correct Dutch translations and page tags.
- Sargent image: asset `flamenco_sargent.jpg` is 793×1132, exactly Commons file
  "Sargent John Singer Spanish Dancer.jpg"; the work is *Spanish Dancer* (1880–81,
  private collection) per Invaluable auction record + Google Arts & Culture — the
  caption "(1880–81)" is CORRECT. (es.wikipedia's "1879–82" describes the study
  series, not this work.)

## Verdict

**NOT zero defects — conclusion (b).** 6 defects (D1–D6) + 1 observation (O1).
See PROOF-NOTE.md for the numbered list.
