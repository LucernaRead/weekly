# GATE-LOG — 2026-W47 pt–fr proof1 (independent, re-fanout rebuild)

Proofreader: pt-fr2, 2026-11-11. All gates re-run by the proofreader; KIT numbers not trusted, only re-run results below. All commands run with `TMPDIR=<scratch>/tmp` (system /tmp never used). Edition dir untouched (final SHA re-check identical to task values; `git status` still only `??` untracked dir). All Python via `~/workspace/weekly-git/tools/venv/bin/python` (3.12.3, Pillow 13.0.0, FreeType 2.14.3).

Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-fr2/`
Edition: `~/workspace/weekly-git/production/2026-w47/2026-w47-pt-fr/` (ED)
Core: `~/workspace/weekly-git/production/2026-w47/core-pt/` (read-only)

## §0 Identity (disk is authoritative)

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`, rc=0 (probe OK; /dev/null present)
- Print PDF `A-Lucerna-VOL4.pdf`: sha256 `4b9f41475eb5ec7ec7e81cb372c50a58b6d7516c17a21fd1e2745ff7189f7653`, 12,934,630 bytes — matches task
- Web PDF `A-Lucerna-VOL4-web.pdf`: sha256 `1f5cc5adc131bf16bd4a1f3a796e3470a399293f7f99e15f61f0ccfdb5080fb3`, 1,141,286 bytes — matches task
- text.md `2026-w47-pt-fr.text.md`: sha256 `39d06879d21b37ecca7b42ddb55214391bcb3c1aa6215cbcb39b184176e0a8e2`, 37,699 bytes — matches task

## §1 Mechanical gates (all re-run)

| Gate | Command / method | Result |
|---|---|---|
| run.py (scratch copy) | `python run.py` in `build-copy/` | **rc=0, TOTAL 150** (A2 48 / B1 71 / B2 31; pages 10/18/18/18/18/18/12/38; model 88 words), **0 overflow** (`run.log`) |
| Rebuilt SVG identity | `cmp` scratch `build-copy/svg/*.svg` vs shipped `svg/*.svg` | **8/8 byte-identical** |
| Builder gates | `python gates.py` (read-only, shipped SVGs) | **16/16 PASS**, `FAILURES: none` (`gates.log`); P7 quote-region max baseline 2380.17 < 2404 |
| Freeze baseline (core, required) | `tools/freeze.py baseline --build production/2026-w47/core-pt --core-svg production/2026-w47/core-pt/svg --out freeze-core --json freeze-core.json` | **rc=0, 8/8 SVGs byte-identical**, repointed: none; core integrity: shipped core SVGs unchanged by the run (`freeze-core.log/.json`) |
| Freeze baseline (edition, supplement) | `tools/freeze.py baseline --build <edition> --core-svg <edition>/svg --out freeze-ed` | **rc=0, 8/8** (`freeze-ed.log/.json`) |
| Freeze diff | `tools/freeze.py diff --core-svg core-pt/svg --edition-svg <edition>/svg` | **added CJK only U+3000 ×9** (P1: 2, other pages: 1 each); per-page +25..+52 / −22..−48 strings, P8 +191/−753 (`freeze-diff.log/.json`) |
| Occlusion audit (real) | `tools/occlusion_audit.py <edition-dir> --json occlusion.json` | **rc=0, 0 flags**; self-test OK, all 6 planted classes fired (BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX); clean controls silent (`occlusion.log/.json`) |
| p8 extract | `tools/p8.py extract --p8 svg/p8-avaliacao.svg --total 150` | **150/150 noted** (`p8-extract.log/.json`) |
| p8 compare (JSON body read directly) | `tools/p8.py compare --core-p8 core-pt/svg/p8-avaliacao.svg --edition-p8 svg/p8-avaliacao.svg --total 150` | **status CLEAN** (`p8-compare.json`: missing=[], extra=[], uncertain=[], **keydiff=[137, 138]**); core 150 noted, edition 150 noted (`p8-compare.log/.json`) |
| keycheck | `keycheck_core.py <scratch build-copy> <p8-extract.json>` (script copied into own scratch so its output lands here, not in the refanout scratch) | **rc=0, exact match 149/150**; sole mismatch Q150 (REG key `(exercice ouvert — texte modèle ci-dessous)` vs extracted `✓` — known open-task exception) (`keycheck.log`, `keycheck-150.json`) |
| Print/web text layers | `check_final.py` (PyMuPDF word multiset) + `pdftotext -layout` byte compare + per-page token counts | **8 pages each, 8,629 words each, multiset-diff 0; per-page diff 0** (993/825/761/931/811/859/883/2566); **pdftotext bytes identical, 110,813** (`check-final.log`, `print.txt`, `web.txt`) |
| Web re-render (scratch only) | `tools/webpdf.py <scratch svg> web-rerender.pdf` | rc=0, 1,141,272 bytes (shipped 1,141,286; 14-byte delta = fontTools timestamps, SHA/size not reproducible by design); **re-render text layer byte-identical to shipped web** (110,813) (`webpdf.log`, `web-rerender.pdf/.txt`) |
| Scratch print re-render | `render.py` in `build-copy/` | rc=0; **re-rendered print PDF SHA identical to shipped** `4b9f4147…f7653`, 12,934,630 bytes (`render.log`) |
| P8 min font (effective) | `minfont.py` (pypdf visitor, print PDF p.8) | **min 9.75pt** (n=374 runs), **0 below 9.75pt**; distinct sizes 9.75–34.5pt; texts at min are P8 answer lines (`minfont.log`) |
| P8 min font (spans) | `check_final.py` answer region y∈[948,1950)pt, web PDF | **min span 9.75pt**, 186 spans, sizes [9.75, 10.5, 14.625, 18.75]; word bbox min 9.75 / median 9.75 (`fr-p8size.json`) |
| Italic spans | fitz span scan, print vs web | **print 1 = web 1** (`« consciência »`) (`italic.log`) |
| check_s11 (§1.1 + P8 font + badges) | **pt-adapted copy** `check_s11_pt.py` (adapted from `scratch-fanout-en/check_s11.py`, which is en-specific: core-en page names, en cloze tokens, registry.json; pt version uses core-pt, pt page names, P8 chips per exercise from keycheck-150.json levels) | **rc=0, ALL §1.1/P8 CHECKS PASS**: paper rect 8/8; VOL.4 counts core=ed per page (2/1/1/1/1/1/1/1), VOL.5 (0/0/0/0/0/0/3/0); chip rect counts core=ed per page (10/15/18/15/18/18/12/35); colour set core 21 = edition 21, extra/missing none; badge colours A2/B1/B2 present; P8 min SVG font 13.0 units (= 9.75pt; core 13.5 — fr answers run at 13 units by design, p8_keys_small, KIT §6; gate is the SOP §1.1 floor, not core equality); **P8 exercise chips Q113–120 + Q145–150: 14/14 OK** (same-row chip of REG level colour); ESCREVA VOCÊ head present (`check-s11.log`, `check_s11_pt.py`) |
| Sweep (gates_pt step 11) | `sweep_de.py <edition-dir>` | **rc=0: box-vs-hline 0, bridges 20, bridge orphans 0, bridge widows 0** (`sweep.log`) |
| Boxtitle true ink (23pt) | `boxtitle_core.py <edition>/svg` | **rc=0; all 31 box titles clear, min +12.0px** (P1 EM POUCAS PALAVRAS); D1 +18.7, D2 +89.7, D3 +111.2 (`boxtitle.log`) |
| Full-page true-ink scan | `measure_ink.py` (copy of pt-fr1 method, canonical `occlusion_audit.ink_box`, paths repointed to own scratch) | **right_margin 1** (P8 header ink_r exactly 1862.0, over 0.0); **right_edge 0; box_right 0; box_left 0; box_bottom 0**; left_margin 10 × 0.2px glyph-bearing noise only (`ink.log/.json`) |
| Creambox canonical | `creambox.py <edition>/svg/*.svg` | 5 negative "last baseline" entries, all below-window headings (see §2) (`creambox.log`) |
| Creambox diag | `creambox_diag.py <edition>/svg/*.svg` | all negatives adjudicated owner-rect=NONE; min true-ink bottom clearance **+0.3px** (P2/P3/P4 E VOCÊ), +0.4px (P5 E VOCÊ), +4.2px (P7 word box) (`creambox-diag.log`) |
| Curly quotes / CJK / banned | `scan8.py` + `scan8b.py` (own scripts) | straight `"` 0; `“”` balanced 2/2 (SVG + text.md); no Han/kana/hangul; only U+FF5C `｜` (house separator, core-present, see §4); `verbatim`/`SOP`/`proofread`/`TODO`/`FIXME`/`lorem`/`cover`/`?Écrivez`/`?Write` absent; `..` only inside `...` (45 = 45 both files); VOL.3 only in P7 disclosure (allowed); 150/150 stems found in their SVG pages (`scan8.log`, `scan8b.log`) |
| 150-key hand check | full text.md read + 8-page visual + mechanical cross-checks | **150/150 OK** (`keycheck-hand.json`, `verify150.log`): Respostas parsed 150 (1–150 complete); Respostas vs REG keys 0 diffs; Respostas vs P8-extracted 0 diffs (both excl. Q150); model text 88 words; 8 phrases each exactly 2×; exercise numbers 150/150 |
| Weekdays | `date -d` (America/Toronto) | Sat 11-07, Sun 11-08, Sat 11-14, Sun 11-15, Mon 11-16, Tue 11-17, Wed 11-18, Thu 11-19, Fri 11-20, Sat 11-21, Sun 11-22, Mon 11-23, Fri 11-27, Mon 11-30, Sun 12-06 — all match the issue |
| D1–D4 pixel strips | PIL dark-pixel strips on scratch-rendered cards | D1 gap x1412–1440: **0** (dark px at x≥1463 are the neighbour box's own body text); D2 beyond box right: **0**; D3 beyond box right: **0**; D4 beyond margins: **0/0**; D4 inside band: 10,547 |

## §2 Creambox adjudication (all 5 negatives are false positives)

- P1 box y=786 bottom=1220.2, "last baseline" 1257.2 clearance −37.0 → below-window line `AGORA VOCÊ　À vous de jouer`, owner-rect=NONE; OWN last baseline 1175.2, ink bottom 1177.9, ink-clearance **+42.2**.
- P2 box y=1618 bottom=1768.0, "last baseline" 1800.0 clearance −32.0 → below-window line `Atenção: o feriado é nacional…`, owner-rect=NONE; OWN last baseline 1731.9, ink-clearance **+35.8**.
- P3 box y=200 bottom=405.1, "last baseline" 442.1 clearance −37.0 → below-window line `UM DIA, DOIS SENTIDOS`, owner-rect=NONE; OWN last baseline 357.4, ink-clearance **+47.5**.
- P6 boxes y=1594 bottom=1916.0, "last baseline" 1958.0 clearance −42.0 (×2) → below-window exercise-band headers `EXERCÍCIOS　EXERCICES DE LA PAGE 6` / `Réponses page 8…`, owner-rect=NONE; OWN last baselines 1876.0 / 1854.0, ink-clearances **+36.0 / +57.8**.
- Tightest true-ink bottom clearances (all positive, ink inside box): P2/P3/P4 E VOCÊ **+0.3px**, P5 E VOCÊ **+0.4px**, P7 word box **+4.2px**, P2 schedule cells `Palmeiras–Flamengo` **+2.1px**.

## §3 §1.1 spot values (from check_s11 run)

- Paper `#fbfaf6` ×8; colour set core 21 = edition 21 (extra/missing none); badge colours all three present; VOL.4 counts per page core=edition (P1 2, others 1); VOL.5 P7 3 = core 3 (disclosure + next-week text, allowed).
- ABSTRACT.txt: single line, 673 bytes, French, no ASCII double quotes; real topics (Consciência Negra 20 Nov, Zumbi/Palmares, Copa final Grêmio × Palmeiras 6 Dec Mané Garrincha, Enem corrigé/TRI, Palmeiras × Flamengo 21 Nov) + VOL.4 + A2–B2 + 150 exercices.

## §4 CJK accounting detail

- Freeze diff: added CJK only U+3000 ×9. The only other U+FF00–UFFEF-range character is `｜` U+FF5C (fullwidth vertical line, a punctuation separator, not a Han character): core has 1 per page on P1–P6, edition keeps 1 on P1 (`Mots-clés｜`) and uses `Note —` on P2–P6; text.md uses `Note｜` (6×). No Han/kana/hangul characters anywhere (0 in all 8 SVGs, text.md, ABSTRACT.txt). The SVG-vs-text.md separator difference (`—` vs `｜`) is a pre-existing export quirk, content-identical, not a defect.

## §5 Flagged threshold conflict (not a defect — needs coordinator ruling)

- Task gate 4 states "P8 最小 PDF 字号 ≥10pt"; measured **9.75pt** by three independent methods (minfont.py effective 9.75pt, 0 below; check_final.py answer-region min span 9.75pt; check_s11_pt.py SVG min 13.0 units × 0.75). SOP §1.1 sets the floor at 9.75pt ("答案字号降到不低于 9.75pt（W46 现行众数）"), KIT §6 records 9.75pt, round-1 proof accepted it. Judged per SOP: not a defect. Coordinator to rule if the task's ≥10pt is a hard requirement.

## §6 Files produced (scratch)

- `PROOF-NOTE.md`, `GATE-LOG.md` (this file), `keycheck-hand.json`, `keycheck-150.json`
- Evidence: `run.log`, `gates.log`, `freeze-core.log/.json`, `freeze-ed.log/.json`, `freeze-diff.log/.json`, `occlusion.log/.json`, `p8-extract.log/.json`, `p8-extract-core.log/.json`, `p8-compare.log/.json`, `keycheck.log`, `check-final.log`, `fr-textdiff.json`, `fr-p8size.json`, `minfont.log`, `italic.log`, `check-s11.log`, `check_s11_pt.py`, `sweep.log`, `boxtitle.log`, `ink.log/.json`, `measure_ink.py`, `creambox.log`, `creambox-diag.log`, `scan8.log`, `scan8b.log`, `verify150.log`, `render.log`, `webpdf.log`, `print.txt`, `web.txt`, `web-rerender.pdf`, `web-rerender.txt`
- Scratch rebuild copy: `build-copy/` (edition copy + rebuilt SVGs + re-rendered cards/print PDF; proves reproducibility without touching production)
- No source files modified; no commit; no push.

## §7 Supplementary checks (triggered by the pt-it re-proof; measured and judged independently)

### S1 — P2 "PARA NÃO ERRAR" box title: PASS, no overflow
- Targeted PIL re-measurement (`occlusion_audit.ink_box`, independent repeat of the boxtitle run): title ink L=556.5, **R=871.5** vs box right 961.0 → clear **+89.5px** (boxtitle: R=871.3 / +89.7; 0.2px inter-method difference); left clear 18.0px. Source `tables_fr.py:57`.
- PDF pixel cross-check (scratch card `p2-vida.png`, title band y620–650): dark pixels beyond box right (x961–1020) = **0**; dark x-range in band 559–874, all inside the box.
- Visual: `crop-p2-paranao.png` shows the title ending far from the box's right edge. The pt-it overflow (−59.5px, gloss `La regola da ricordare`) does not transfer: the French gloss `À retenir` is ~150px shorter. **Not a defect.**

### S2 — P1 top-strip slogan "Le portugais que lit le Brésil": grammatically correct, NOT a defect
- Source `tables_fr.py:200`; rendered in the P1 top strip (17pt).
- Independent French-grammar judgment (**against the coordinator's preliminary reading**): relative `que` is invariably the direct object (COD), never the subject; the subject relative pronoun is `qui` (three grammar references agree: live-french.net, monfrancais.fr, sandrineescoffier.com — `qui` = sujet + verb; `que` = COD + subject + verb, e.g. `le livre que je lis`). Parsing: `que` = COD = `le portugais`; the clause subject is the postposed `le Brésil` (standard nominal-subject inversion, e.g. `le livre que lit Marie`). The sentence means "the Portuguese that Brazil reads" = 「巴西人正在读的葡萄牙语」 — no inversion. Had `le portugais` been the subject, the pronoun would have to be `qui` (`Le portugais qui lit le Brésil`). Italian `che` is ambiguous (subject or object), so the pt-it case differs; French `que` is unambiguous.
- Widths (17pt true ink): current full strip line 600.9–1231.7 (630.8px), clearances 512.9 / 630.3px inside margins 88–1862; hypothetical SVO reordering `Le portugais que le Brésil lit` measures **identical** (630.8px; segment 218.0px both ways) — no layout risk either way; no change needed.
- Premise correction: the task's "17pt centered at x=975" is inaccurate — the element is `text-anchor="start"` at x=600.9 (ink centre 916.3); in any case the line sits far inside the margins.
- Visual: `crop-p1-strip.png`. **Not a defect.** S1/S2 do not change conclusion (a) zero defects.
