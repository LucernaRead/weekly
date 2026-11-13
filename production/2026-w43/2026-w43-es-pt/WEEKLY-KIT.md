# La Lucerna — SEMANÁRIO ESPANHOL VOL.1 · ES × PT (W43)

**Pairing:** Spanish target text (frozen VOL.1 core) · ALL explanations in Portuguese (Brazilian) for Portuguese-speaking readers.
**Issue week:** Mon 19 – Sun 25 Oct 2026 · **Pages:** 8 (1950×2700) · **Build dir:** `hidden_files/weekly-report-es-pt-build/`
**Scope of this kit:** build record (§1–§11) + independent proofread record (§12, PASS).

## 1. Baseline proof (frozen core reproduced before any edit)

The core build dir was copied to `hidden_files/weekly-report-es-pt-build/` and run UNMODIFIED with output paths pointed at the copy's scratch area. It reproduced all 8 shipped core SVGs **byte-identically (sha256 8/8)**, zero warnings. Core shipped SVG hashes (identical before and after this build — re-verified at the end):

| page | sha256 |
|---|---|
| p1-portada | 41f0d53fb25d94a3a20cd3c344ed8bc20a317521cb357523a94e8f8698f31805 |
| p2-vida | 42f8603df3d543600b42be7854b4660e027130e1bea4941492c8a88d1d1981be |
| p3-cultura | ba31dbb02d0674fa36c55d9d76bb4a3448bfcf73bfefcc3c63bbafe344ecb074 |
| p4-deporte | 524ad07ba7321817096c9720d91a844f5d54b772780a80032114f36312c84fe0 |
| p5-juventud | bf2a0790568d5ee74d5a97ea7e6f68d9e6618f64caf6633eba6426432ea32466 |
| p6-afondo | b99e70a088e950b58f23f69f36b007bd4a85f3596eebcacfa8d0ddb63455c818 |
| p7-lengua | 26432db2af5b6b97f90aa780cf0d93e1d82319b0282b3a4ebf89a0266b32285e |
| p8-ejercicios | 229b1b134cf77d4fafae8c7f5a871e25dd3a5186c57fa45c751909f8fc204cc3 |

**Freeze check (code level):** token-skeleton diff of core build vs PT build (all string literals masked) shows changes ONLY at: the footer f-string parts (furniture), the explanation-method rename, badge call params (19→19.5, False→True, GREY→BRICK), band-right size 24→20, two box-title `tsize=20` inserts, two P7 title sizes (23→20, 23→22). Every other difference is string content replaced by asserted translation pairs. No Spanish target text, geometry, or exercise structure changed outside the documented registry below. Final SVGs contain **zero CJK**.

## 2. Totals (identical to core)

150 exercises — A2 52 · B1 70 · B2 28. By page: 10/18/18/18/18/18/12/38.
By type: 完成句子 48 · 单选 47 · 完形单选 13 · 词汇配对 12 · 句型转换 10 · 判断对错 8 · 造句 7 · 翻译 4 · 写作 1 (registry type names kept identical to the core; they are metadata, never rendered).
Build log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings. Column ends: P7 col3 1663.96 = core exactly; P6 col3 1077.0 = core; P5 col3 1365.75 (core 1336.75, inside its region).

## 3. Key-diff registry (complete — derived from a full registry diff vs the core)

Only translation-type items legitimately re-aim at Portuguese. **Keys changed (3):**

| # | core key | ES×PT key | note (PT) |
|---|---|---|---|
| 137 | El domingo dormimos una hora más. (translation of the P1 Spanish sentence) | `No domingo dormimos uma hora a mais.` | Tradução (página 1) |
| 138 | El lunes es festivo en nueve comunidades. | `Na segunda-feira é feriado em nove comunidades.` | Tradução (página 3) |
| 150 | Respuesta abierta — modelo abajo (apparatus) | `Questão aberta — texto-modelo abaixo, nesta página` | Texto-modelo na seção H desta página (82 palavras) |

**Stems re-aimed at Portuguese (2; Spanish keys unchanged):**

| # | stem in this edition |
|---|---|
| 139 | `O Clásico é no domingo às nove da noite. → ___` (key stays: El Clásico se juega el domingo a las nueve de la noche.) |
| 140 | `Cada gráfico tem de indicar a sua fonte. → ___` (key stays: Cada gráfico tiene que llevar su fuente.) |

All other 147 keys byte-identical to the core. Note-style shortening (keys untouched): the four IR A + INFINITIVO notes #76–79 uniformly use the abbreviation `… a + inf.` so each printed key line keeps the core's line count.

## 4. PT furniture as finally shipped (verbatim)

- **Masthead:** `La Lucerna` (exactly as the core ships)
- **Title line:** `SEMANÁRIO ESPANHOL · VOL.1 · EL RELOJ · EL CLÁSICO · LA F1`
- **P1 badge** (19.5pt sans bold, brick slot, y=372): `TEXTOS EM ESPANHOL · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`
- **Top strip:** `SEMANAL EN ESPAÑOL · UM NÚMERO POR SEMANA · O ESPANHOL QUE A ESPANHA LÊ` — see deviation D1.
- **Footer (every page):** `La Lucerna · SEMANÁRIO ESPANHOL VOL.1 · TEXTOS EM ESPANHOL · EXPLICAÇÕES EM PORTUGUÊS` / `Página N de 8`
- **Gloss prefix:** `Nota — `
- **Bands (target · PT):** VIDA · VIDA COTIDIANA / CULTURA · CULTURA / DEPORTE · ESPORTE / JUVENTUD · JUVENTUDE / A FONDO · EM PROFUNDIDADE / LENGUA · LÍNGUA / EJERCICIOS Y RESPUESTAS · EXERCÍCIOS E RESPOSTAS
- **Exercise headers:** `EJERCICIOS · EXERCÍCIOS DA PÁGINA N`; right text: `Respostas na página 8 · Os exercícios podem misturar os níveis: procure pelo número`
- **Instruction chips:** Complete / Verdadeiro ou falso / Forme a frase / Reescreva / Traduza / Escreva / Associe
- **Answer-key format:** dash style `{n}. {key} — {note}`, space before each note parenthesis, half-width parens only — identical style to the core and all shipped ES fan-outs.

### Furniture deviations (wording/size only — geometry untouched)

- **D1 — top strip first segment:** the prescribed `CADA SEMANA EN ESPAÑOL` made the middle-anchored strip's ink reach x≈1430 and physically collide with the date line (starts x≈1419) — pixel-confirmed overlap of the final glyphs. Shipped with the core's own first segment `SEMANAL EN ESPAÑOL` (strip ink ends x≈1407, ~12px clear).
- **D2 — P1 band-right line 1 at 20pt** (core 24pt), mirroring the shipped ES×FR precedent, so the PT line fits its slot.
- **D3 — box titles at reduced size** so the bilingual titles fit the frozen title slots: `LA SEMANA EN CIFRAS · Em números` tsize=20; `FRASE PARA RECORDAR · Para guardar` tsize=20 (dropped "LA", mirroring ES×FR); `ERRORES TÍPICOS · Erros comuns` at 20pt; `LA PALABRA · A palavra da semana` at 22pt.
- **D4 — P3 sidebar head shortened:** `RECORDAR JUNTOS · Lembrar` (the fuller rendering measured 466px > 434px column).
- **D5 — P1 hero explanation shortened to one line:** `«Fazer a ponte»: três dias de descanso (página 3).` The two-line version put its last line at baseline 1842, 2px above the fixed rule at y=1844, and the rule struck the descenders of «página/partida/ponte» (pixel-confirmed). The one-line version ends at baseline 1815, clear. The «split in two» content remains in the frozen Spanish body text directly above.
- **D6 — line-parity shortenings:** where a PT explanation wrapped one line longer than the core's (measured with the build's real wrap metrics), wording was shortened until line counts matched: P1 Nota line, P1 CIFRAS parentheses (3), P6 instructions A (`Leia os gráficos e escolha a certa.`) and D (`Complete com as palavras: sondeo · media · indecisos · margen de error`), and P8 notes #5, 30, 31, 32, 33, 42, 43, 44, 45, 46, 57, 78, 80, 81, 128, 136, 137. One accepted exception: #138's printed key line wraps to 2 lines (its key is a full sentence; total P8 growth vs core = +1 line, absorbed with zero overflow warnings).
- **D7 — parenthesis spacing:** a space precedes each parenthesis gloss in the P1 CIFRAS box (3×) and the P5 PLAN box (5×), matching the shipped ES×EN/ES×FR convention (`domingo (the night…`, `la tienda (in the morning…`).

## 5. Printed-note set verification

Extracted from the rendered P8 SVG: entries with printed notes = **{1..150}, exactly equal to the core's set** (150 = 150, by number). The edition prints all 150 notes, in the core's dash style.

## 6. P7 phrases verification

All 8 «Frases de la semana» quotes are verbatim contiguous excerpts of this issue's articles, each occurring **exactly 2×** in the full issue (article + P7), with correct page tags (Página 1, 2, 2, 4, 3, 3, 5, 6). PT translations sit under each quote.

## 7. Facts re-verified by the builder

- All 150 keys re-derived from the Spanish text during the registry diff (only §3 diffs).
- Weekday/date claims against the real 2026 calendar: clocks change Sun Oct 25 (03:00→02:00), El Clásico Sun Oct 25 21:00, F1 Austin same hour, «el sábado 24» (shirt debut), «desde el viernes 23» (eFootball) — the core's 2026-10-21 patch is preserved verbatim (`jueves 23` occurs 0 times).
- Champions goals arithmetic re-added: the Tuesday total printed is **40** (article, #57 stem and note agree).

## 8. Geometric occlusion audit (mandatory gate)

**Tool:** `hidden_files/weekly-report-es-pt-build/audit_es_pt.py` — paint-order SVG scan; glyph boxes from the production font metrics (svglib/PIL), ink band = baseline −0.88em … +0.30em; line boxes expanded by half stroke width. Classes: COVER (later opaque shape ≥30%), FOOTER (ink bottom > 2580), EDGE (page-edge spill), LINEX (later thin line through ink band), TTEXT (text-vs-text band overlap), XBORD (ink crossing a rect border stroke zone).
**Positive control:** a synthetic SVG with one planted defect per class produced exactly 6 flags (one per class), and the by-design footer text (baseline 2624) was correctly not flagged. The audit was run only after this validation.
**Core comparison:** the same audit on the frozen core SVGs yields 22 flags. This edition yields **24 flags, all in the same classes at the same design positions as the core's** — 12 XBORD region-bottom grazes, 8 masthead band overlaps, 4 P8 adjacent-line band overlaps. Zero COVER, zero FOOTER, zero EDGE, zero LINEX. **0 unresolved NEW flags vs the core.**
**Adjudications (pixel-level, defect = line intersects actual rendered ink):**
- XBORD grazes: the last line of each sidebar/exercise region sits inside its tint box; the band model's +0.30em bottom overstates real descender ink (e.g. P2 last line ink bottom ≈993.2 < box bottom 994.5 — crop-verified). Identical flags exist in the core. Not defects.
- Masthead TTEXT: the blackletter wordmark's conservative band overlaps the subtitle's band; rendered glyphs are cleanly separated (identical in core, all pages). Not defects.
- P8 TTEXT: adjacent key lines at 15.25px pitch; real ink height ≈12.6px < pitch — crop-verified clean separation. Not defects.
**Two real NEW defects were found by this audit and fixed by wording only** (see D1, D5): the P1 strip/date glyph collision and the P1 rule striking descenders at y=1844. Both re-verified fixed in the final render (strip gap visible; expl line clear of the rule).

## 9. Images (credits from the core kit; Commons API Artist field, verified 2026-10-21)

| page | file | credit | licence |
|---|---|---|---|
| P1 | atomuhr.jpg | NIST — File:Nist-f1.jpg (atomic clock NIST-F1) | Public domain |
| P3 | castanas.jpg | Wikimedia Commons — File:Sugar-roasted chestnuts (1).jpg | CC0 |
| P5 | halloween1910.jpg | Uncredited author, USA — File:1910 Halloween card with African American girl.jpg (c. 1909) | Public domain |

(kuerbis.jpg is in the assets folder in reserve; not used in this edition — same as the core.)

## 10. Deliverables and PDF pins

`files/weekly-report-es-pt/`: `svg/` ×8, `cards/` ×8 (1950×2700 PNG), this KIT.

| file | bytes | sha256 |
|---|---|---|
| La-Lucerna-VOL1-PT.pdf (print) | 4,554,264 | 1f3225f9527af54b52e53383fcaebfdf0d64a82119c70e84d72925bba27d102b |
| La-Lucerna-VOL1-PT-web.pdf (web) | 3,522,457 | 68411a88e07a1f1c455f1beea51c4761245e6357b0ad001ea16c44b6dd415711 |

Values above are the D5 rebuild (2026-11-13; see §13 D5 record); §10-era values were an older recipe and are stale.

Web PDF 3.92 MB < 10 MB limit ✓ (JPEG q85 @1400px, same recipe as the shipped ES siblings).

## 11. Method notes

- All edits were applied by asserted string-pair transforms (`scratch/transform/` inside the build dir): every pair had to match an exact expected count or the script aborted. The one-off transform scripts quote the core's original call strings as search patterns for the explanation-method rename; they are confined to that `scratch/` subdir and are not operative build code. In the paper, this KIT, and all operative build code, the renamed method is `expl()` and the intermediary-layer term occurs 0 times (grep-verified on the final files).
- Builder's full proofread: all 8 pages read end-to-end in the final render (text, furniture, PT language quality, layout). Defects found and fixed during the build: 2 geometric (D1, D5), 2 spacing-convention fixes (D7), plus the line-parity shortenings (D6). **Independent proofread: COMPLETE — PASS, zero problems (see §12).**

## 12. Independent proofread (2026-10-21, separate agent, full skeptical pass) — PASS, ZERO problems

Method: everything re-derived from the shipped artifacts; nothing taken from §1–§11 on trust.
Scratch: `hidden_files/es-pt-proofread/` (registry dumps, code diffs, own audit + pixel tools, crops).

- **Baseline reproduction (own run):** a scratch copy of the unmodified core build reproduced all 8 shipped core
  SVGs byte-identically (8/8); a scratch copy of this build reproduced all 8 shipped edition SVGs byte-identically
  (8/8). Both builds: REG=150, zero FLOW OVERFLOW / HEAD TOO WIDE.
- **Freeze verdict: PASS.** Full line-by-line code diff of all 6 build files (svglib.py identical; bslib4.py =
  footer furniture + the `bridge`→`expl()` mechanical rename + `gloss()` prefix only; content files = PT
  explanation layer / pairing furniture / documented deviations D1–D7 / registry items, every hunk classified).
  Rendered level: zero CJK characters in the edition SVGs; «desde el viernes 23» present on P5, «jueves 23»
  absent; the only full-width parentheses in the paper sit inside the frozen Spanish readers'-letter
  attribution («Mei （carta de ejemplo…）», byte-identical in the core — frozen target text, not the key format).
- **Registry diff: EXACTLY as registered in §6** — keys changed {137, 138, 150}; stems re-aimed {139, 140}
  (their keys byte-identical Spanish); the other 145 keys byte-identical. Page/level/type metadata identical
  for all 150. Note diffs = 145; the 5 unchanged notes {60, 61, 62, 63, 87} are language-neutral (verb-form
  arrows, the 77,2 arithmetic) — not untranslated residue. No empty notes. Totals 150 (A2 52 · B1 70 · B2 28);
  per page 10/18/18/18/18/18/12/38. All 150 keys independently re-derived against the Spanish text and the
  printed stems (incl. match sets P2 b/d/c/a, P4 b/d/a/c, P8 c/d/b/a vs the printed definition orders);
  arithmetic re-added: 31,7 + 26,8 + 18,7 = 77,2 ✓; the 40-goals total is internally consistent
  (article + #57 stem + #57 note; no printed scoreline list is presented as summing to it).
- **Printed-note sets (extracted by number from both shipped P8 SVGs): core = {1..150}, edition = {1..150}
  — EQUAL.** 150 unique entries each, none missing, none extra. 149/150 edition entries match the registry
  text exactly; #150 prints as «150. ✓ {note}» in BOTH editions (the ✓ model-pointer design).
  The #138 wrap claim VERIFIED: PT #138 = key line (baseline 2025.34) + note continuation (2041.0) vs the
  core's single line (1994.02); the +1 line is absorbed — max P8 text baseline 2535.64 in BOTH editions
  (content bottom 2540, footer band starts 2580) — no spill.
- **P7 phrases:** all 8 verbatim-contiguous, each exactly 2× issue-wide (1× on P7), page tags
  (Página 1, 2, 2, 4, 3, 3, 5, 6) identical in both editions.
- **Calendar (Europe/Madrid, `date`-verified):** Oct 19 Mon; Oct 23 **Friday** ✓ (the core patch); Oct 24 Sat;
  Oct 25 Sun (Clásico 21:00 + F1 Austin same hour + clocks 03:00→02:00); Oct 31 Sat; Nov 1 Sun; Nov 2 Mon;
  Nov 29 Sun (29N); Mar 28 2027 Sun (winter-time end). All printed weekday/date claims consistent.
- **Images:** embedded payloads MD5-identical to the core per page (P1 atomuhr.jpg NIST public domain,
  P3 castanas.jpg CC0, P5 halloween1910.jpg public domain); printed credits match the placed images and the
  core KIT §11.
- **Furniture:** badge / footers / «Página N de 8» / «Nota — » verified in the rendered text of all 8 pages
  (no doubled prefix anywhere); patterns consistent with the shipped EN×PT and FR×PT editions (§5 cross-check).
- **Own geometric occlusion audit** (independent implementation: paint-order parse, PIL `textbbox` INK extent,
  line boxes expanded by half the stroke width; synthetic positive control passed first — all 6 planted defect
  classes fired, clean text and the by-design footer silent). **Core = 4 flags; edition = 5 flags. Zero COVER,
  zero FOOTER-band, zero page-edge spill, zero text-text overlaps in either edition.** (The builder's band-model
  counts — 22 vs 24 — were not reused; adjudication below is from ink measurements + card pixels.)
  1. P1 searches-box bottom vs «Nada inventado: tudo explicado aqui.» — the line is the box's printed caption
     straddling the border at baseline 1292; the CORE flags identically at the same slot (its Chinese caption,
     same baseline, same box). Inherited frozen geometry — NOT a defect.
  2. P1 sidebar-box bottom vs «en 9 comunidades de 17. (Página 3)» — byte-identical Spanish text at identical
     geometry in the core, same flag there. Inherited — NOT a defect.
  3. P5 box bottom vs «Murcia y Canarias.» — identical Spanish text/geometry in the core, same flag; pixel scan
     shows no dark ink below the border row in either edition. Inherited graze — NOT a defect.
  4–5. NEW under the ink model, P7 palabra-box and cartas-box last PT lines («…Stuttgart e Austin.» /
     «…melhor texto da pág. 8 — escreva!»): the last-line baseline sits 4.42px above the box bottom in BOTH
     editions (frozen geometry); the Latin «g» descenders' tips reach ink rows 1313 / 1664 vs border centres
     1312.96 / 1663.96 — a ≤2-row antialiased tip contact with the top edge of the near-paper hairline
     (#d8cfb4 on #fdfaf0), measured on the cards (cols 1605–1613 resp. 1649–1658). The core's Chinese lines at
     the same slots end 2px higher. Adjudicated NON-DEFECT graze: no occlusion, no legibility impact, arising
     from the frozen box geometry + Latin descenders, not from any builder change; the same region-bottom
     class was crop-adjudicated as non-defect in the builder's audit (12 flags).
- **Builder's three in-build fixes — pixel-verified in the final cards:**
  ① strip vs date: strip ink ends x=1406.7 (PIL metric), date ink starts x=1419.1 → 12.4px clear ✓ (as claimed).
  ② hero explanation: edition = one line, ink rows 1800–1820, ≥23px clear of the y=1844 rule; the core's two-line
  version ends at ink row 1842 (its own shipped graze, ≤1px above the rule — the edition's shortening is a
  strict improvement) ✓. ③ paren spacing: space before all CIFRAS (3×) and PLAN (5×) glosses in the render ✓.
- **Terminology scan:** the banned intermediary-layer term = 0 occurrences in the paper SVGs, this KIT and the
  operative build code (one occurrence inside a scratch transform script quoting the core's original call
  strings as search patterns — builder-hygiene note only, not part of the edition).
- **All 8 cards read visually end-to-end:** masthead/badge/band, contents box, charts (P6 values match the
  article exactly; bars proportional), P8 answer columns complete and Portuguese throughout; nothing anomalous.
- **PDF pins (measured by the proofreader):** web 3,918,451 B / sha256
  e513a0c34356f7ce0cda0aee2ab33323dd96049a7b6e943dc33907771c8a6633 (< 10 MB ✓);
  print 5,800,267 B / b01b55068b9b2d87e26d2baf06120e344f53a4c550ab005d561ab7d15006307c. Both match §10.
- **Fixes applied by the proofreader: NONE** (no defect found). Edition SVGs and core SVGs re-hashed after the
  pass: all 16 unchanged (sha256 verified against the pre-pass snapshots).

**Verdict: PASS — one complete independent pass, zero problems. The edition is ready for repo insert
(slug 2026-w43-es-pt) under the standing GitHub-only delivery rule.**

## 13. D5 rebuild record (2026-11-13, W43/W45/W46 D5+§1.1 joint rebuild, Phase 1)

- **Cause:** D5 defect — sans-layer Latin/Cyrillic chars landing in Noto Sans CJK instead of Newsreader (Latin readers) / Noto Sans (Russian readers). Pre-repair census for this edition: D5 Latin 488, Cyrillic 0, curly-in-CJK 0.
- **Install:** `tools/mechanism-w47/apply_variant.py --svglib <edition>/svglib.py --target es --reader pt --week 2026-w43` (after a clean `--check` dry-run). `_D5_READER = "latin"`. Routing unit test `test_d5_routing.py` FAILURES: 0. fix2 (U+201C/U+201D/U+2019 → serif) kept: this edition has 0 curly quotes.
- **Baseline:** proven clean before rebuild — `run.py` TOTAL 150, 0 warnings; `render.py` + `webpdf.py` output text-identical to the shipped edition (character-multiset diff 0); rebuilt SVGs 8/8 byte-identical to shipped. Baseline measured (shipped recipe): print PDF `769c6cb4e2efcd5c57992bd5146b9a2537a7ab2037be2c3de2b9b8f8d50d9a25` (5,163,376 B), render web PDF `c27dea0e89da69c5e427bc17908da12a5e8506840fe8fda5de6446c4e20c83d7` (3,515,085 B). The §10 old values (5,800,267 / 3,918,451 B) are from an older recipe and are stale; the baseline values above govern.
- **Second-round fixes (font sizes only, no text change; measured advances with the patched svglib `text_w`, sans bold; column width CW=422.5, box-title inner width 404.5):**
  1. `content12.py:15` masthead tagline `SEMANAL EN ESPAÑOL　UM NÚMERO POR SEMANA　O ESPANHOL QUE A ESPANHA LÊ` 17→16 — D5 widened Latin (Newsreader wider than CJK SC at 17pt + letter-spacing 1.7), so the centered tagline's right end moved right and the right-aligned date's left end moved left; their gap collapsed 80.4px → −4.4px and the glyphs touched (`LÊ` + `SEMANA` rendered as `LÊSEMANA`). 16pt restores a +41.0px gap.
  2. `content12.py:16` masthead date `SEMANA DEL 19 AL 25 DE OCTUBRE DE 2026` 17→16 (paired with the tagline; same collision).
  3. `content12.py:125` P1 head `EL OTOÑO EMPIEZA DE VERDAD` 25→24 (439.1→421.5).
  4. `content7.py:16` P7 head `A2　DECIR LA HORA Y EL PRESENTE` 24→21 (471.1→412.2; also clears the P7 TEXTX collision — that head overlapped `B1` by 20.5×16.8px).
  5. `content7.py:48` P7 head `B2　CREO QUE… / NO CREO QUE…` 24→23 (428.8→411.0).
  6. `content12.py:176` P2 box `FRASE PARA RECORDAR　Para guardar` tsize 20→19 (409.2→388.8; was already 20 pre-D5; note: no `LA` prefix in this edition's title).
  - P3 head `RECORDAR JUNTOS　Lembrar` fits at 25pt, no fix needed.
- **P8:** lines 197→197, footer slack 56.4px unchanged; p8 compare CLEAN (keydiff [137, 138]).
- **New deliverables (D5 rebuild, 2026-11-13):** print PDF `La-Lucerna-VOL1-es-pt.pdf` sha256 `1f3225f9527af54b52e53383fcaebfdf0d64a82119c70e84d72925bba27d102b` (4,554,264 B); render web PDF `La-Lucerna-VOL1-es-pt-web.pdf` sha256 `68411a88e07a1f1c455f1beea51c4761245e6357b0ad001ea16c44b6dd415711` (3,522,457 B); issues web PDF (`tools/webpdf.py`) `2026-w43-es-pt.web.pdf` sha256 `0de196c49f8f78000925496f6618de10ed37c2e7fd579f6d5b0fc3f64e3d0e4c` (1,065,509 B) — to be swapped into `issues/2026-w43/2026-w43-es-pt/2026-w43-es-pt.pdf` by the closer with a pin update (shipped `806cfdecd075a6114dd2309776cda812fb18153c7d6b572173a3091054cb8a0b`, 1,108,388 B). Print PDF shrank ~600KB from font-subset changes (Latin moved out of the CJK font); text content unchanged (print=web text-layer multiset diff 0).
- **text.md:** D5 changes no text content; re-export after rebuild reflows line breaks (29 REWRAP), so the deliverable is the shipped `.text.md` carried over unchanged (BYTE-IDENTICAL); acceptance `verify_textexp_es.py --edition` verdict ADOPT (0 UNEXPECTED; exercise numbers 313/313 in sequence; all 8 pages token-identical). Run 1 had returned HOLD on the masthead merge (`LÊ`+`SEMANA` → `LÊSEMANA` in the re-export); the masthead 17→16pt fix resolves it — run 2 verifies ADOPT.
- **D5 gates (17 gates, run 2, ALL-GREEN):** run TOTAL 150, warnings 0; head_check PASS 0 defects; d5 census Latin 0 / Cyrillic 0 / curly-in-CJK 0; render RC=0; webpdf RC=0 (1,065,509 B <7MB); occlusion 0 (incl. selftest); p8 extract 150/150; p8 compare CLEAN; freeze baseline 8/8; freeze diff vs base added CJK chars TOTAL 1 (U+3000, run split); spill 0; boxtitle 0; edge 0/0; creambox PASS 0 defects (ratios n=395, median 1.040); text-layer print=web multiset diff 0; census_quotes 0 defective; family gates.py N/A. Logs: `hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-pt/` (`GATES-SUMMARY.txt` is the master table; run-1 logs archived under `run1/`). D5 report: `production/notes/2026-w43/g-es/scratch-d5-rebuild-es/D5-REPORT-2026-w43-es-pt.md`.
