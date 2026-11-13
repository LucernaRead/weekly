# GATE-LOG.md — 2026-W47 it-ru (round 2 proofread, re-fan-out), mechanical gates self-run

Independent proof2, 2026-11-11. All commands run with `TMPDIR=<scratch>/tmp`, `PYTHONDONTWRITEBYTECODE=1`, tools venv python (`~/workspace/weekly-git/tools/venv/bin/python`, Pillow 13.0.0, freetype 2.14.3). Production read-only throughout; final re-verification at the end confirms production untouched (SHAs in §1 identical before/after).

## 0. Hard-gate probes (pre-work, 2026-11-11 ~20:38 UTC)

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2…`, RC=0.
- Real file written to scratch `probe.txt`. Scratch dir verified fresh (only my own `probe.txt` + `tmp/` at creation).
- System /tmp (512M) never used.

## 1. Identity (KIT §1 three SHA)

| File | Size | SHA-256 | Task value |
|---|---|---|---|
| Print PDF `La-Lucerna-VOL4-RU.pdf` | 14,180,887 B | `f74bd65735550718a9927adb47047547d6cd3972f9ccfa4164bd467bf257c3fd` | match |
| Web PDF `La-Lucerna-VOL4-RU-web.pdf` | 1,441,225 B | `c35f390b39e3fe0ef6e95f9a9a292ab94cc356a3955decdcd2dbcd4cf357d1f5` | match |
| Text `2026-w47-it-ru.text.md` | 67,687 B / 1317 lines | `d1b6ddb1e691f74f7a7ce2960077774987dfd36b99712c8b3b49bb254a8361e2` | match |

Shipped SVG SHAs recorded in `shipped-svg.sha256` (p1 `dcbe4b97…`, p2 `462eb58b…`, p3 `87c35bf2…`, p4 `8c4910d6…`, p5 `needfe6a…`, p6 `050fe442…`, p7 `31372b24…`, p8 `69f26e6c…`). End-of-work re-check: `sha256sum -c shipped-svg.sha256` = 8/8 OK; three deliverable SHAs + sizes identical to the table above.
Production state note: the edition directory is untracked in git (`?? production/2026-w47/2026-w47-it-ru/`, no commit touches it yet) — insertion has not happened; I changed nothing there.

## 2. Build interpreter

- `~/workspace/weekly-git/tools/venv/bin/python`, Pillow 13.0.0, freetype 2.14.3 (from `freeze-diff.json` runtime block).
- Core verified as true core before freeze: core-it content md5s match KIT §11 (content8 `629b5b0a…`, content12 `91cdfbb9…`, content34 `18926942…`); core content files have 0 Cyrillic chars and 561/586/637/364/461 CJK chars; ru edition content files have 1982/2131/2382/1248/1806 Cyrillic and 0 CJK.

## 3. run.py re-run (in a scratch copy) — RC=0, TOTAL 150, 0 overflow

- Re-run in scratch copy (`rerun/edition/`, OUT patched to scratch absolute path — production `content*.py` OUT hardcodes the production svg dir, so patching the copy FIRST was mandatory; production OUT untouched, verified by `sha256sum -c shipped-svg.sha256` = 8/8 OK). Log: `rerun/run.log`.
- RC=0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE.
- Levels: A2 47 / B1 70 / B2 33. Pages: 10/18/18/18/18/18/12/38.
- By type: Дополните предложение 61, Выберите ответ 48, Подберите слова 12, Составьте предложения 7, Преобразуйте предложения 1, Верно или неверно 3, Вставьте слово 13, Переведите 4, Письмо 1.
- Model words 99. P1-headline ends 1362; P4 col3 ends 1140.45; P7 col3 ends 1673.0; P8-keys flow ends col 3 y=2529 (bottom 2552). `ALL DONE`.

## 4. SVG rebuild 8/8 + print PDF re-render byte-identical

- **SVG rebuild 8/8 byte-identical** to shipped SVGs (`cmp`).
- **Print PDF re-render byte-identical** to delivered (`rerender.py` in scratch, cairosvg svg2pdf + pypdf merge, reading shipped SVGs read-only): 14,180,887 B, sha256 `f74bd65…3fd`. Log: `rerender.log`; output `rerender-print.pdf`.

## 5. Freeze (canonical tool)

- **freeze.py baseline** (`--build core-it --core-svg core-it/svg --out scratch/freeze-baseline`): RC=0, **8/8 byte-identical**; core integrity unchanged (8 files re-hashed); build-copy verified as core (0 Cyrillic, CJK counts identical to production core). NOT self-compared. Log: `freeze-baseline.log`.
- **freeze.py diff** core vs edition: RC=0; strict-CJK RC=1 with added CJK = 8 × U+3000 only (exempt furniture separators); gates.py fragment check: 0 unexplained add/rem (P1–P7). JSON: `freeze-diff.json`.

## 6. Occlusion audit (canonical tool)

- Selftest OK (all 6 classes fire: BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX; clean controls silent). Log: `occlusion-selftest.log`.
- **0 flags** on 8 shipped SVGs. Log: `occlusion.log`.
- Caveat carried from the task: `occlusion_audit.py`'s `resolve_font` maps Noto Serif/Sans to CJK SC, overestimating Cyrillic advance ≈3%. Ink verdicts in this proof do not rest on tool values alone — the two flagged title bands were re-measured with real NotoSans-Bold (PIL) and with pixel measurement on the delivered PDF renders (see §7 / PROOF-NOTE O-1, O-2).

## 7. Cream-box PIL true-ink scan + spill scan + orphan scan (my script)

Script `cream_spill_orphan.py` (adapted from it-en proof2 scratch; footer-band exclusion added at baseline y≥2596 since ru svglib splits footer into per-word nodes). Log: `cream-spill-orphan.log`.
- 29 cream rects total (P1 4, P2 4, P3 3, P4 6, P5 4, P6 5, P7 3, P8 0); text nodes P1 301, P2 278, P3 264, P4 251, P5 288, P6 275, P7 331, P8 1100.
- **5 flags**: 1 CREAM-X (P2 «ЗАПОМНИТЕ», ink 872.1..1019.4 vs box 538.5..961.0 — adjudicated PROOF-NOTE O-2, observation per STRADDLE); 0 CREAM-Y; 0 SPILL-PAGE; 0 SPILL-FOOTER; 4 ORPHAN? candidates (P5 ««», P6 «18.», P8 «due», P8 «___» — all adjudicated PROOF-NOTE O-5, not defects).
- Title-band union scan (all 29 cream rects, OA ink): only P1/P2 flag. Two apparent flags were scan artifacts from adjacent side-by-side boxes: P4 NOTE box (y=463) catching the classifica title of the neighbouring box (fits its own box, −29 px); P6 chart box (y=1594) catching «PROPOSTA ≠ LEGGE» of the neighbouring box (fits its own box). All other cream titles fit (overhangs −21 to −267 px).
- P1/P2 pixel evidence (delivered print PDF, 96 dpi): P1 cream ends x=960, ink to x=1065 (overhang 104 px); P2 cream ends x=960, ink to x=1020 (overhang 59 px). Web P2 re-measured fresh this session (`web_p2_title_px.py`, render `pages/webp2-2.png`): cream right=960, ink right=1020 — identical to print; column profile 0 dark px at x=960–961 (cream edge in the gap after «М»). P7 fits (−110.7 px). Crops: `pages/crop-p1-cifre.png`, `pages/crop-p2-frase.png`, `pages/crop-p7-errori.png`.
- Word-gap measurement (scripts `gap_measure*.py`, 200 dpi renders `pages/hi1/hi2/hi3/hi5/hi7--*.png`): Russian word-to-word white gaps 4.3–7.7 SVG px; letter gaps within words max 2.9 px; no two space-separated words touch. The 96 dpi «joined» appearance is a downsampling artifact (PROOF-NOTE O-4).

## 8. Text-layer consistency (print vs web PDF)

- `gates.py`: print/web text multiset identical — print_words=7587, web_words=7587, chars_equal=True, word_diff=[].
- Per-page check run by me this session (`textcmp/`, `pdftotext -f N -l N` on both PDFs, sorted-token diff): all 8 pages empty diff. Word counts per page (print = web): P1 725, P2 772, P3 632, P4 673, P5 597, P6 732, P7 573, P8 1410.
- Web PDF 1,441,225 B < 7 MB (gate).

## 9. p8.py extract + compare (canonical tool)

- Extract: 150/150, RC=0. Log: `p8-extract.log`; JSON: `p8-extract.json`.
- Compare vs core: status **CLEAN**, missing [] / extra [] / uncertain [], keydiff **[137, 138, 139]** (expected re-aimed reader-sentence keys). Log: `p8-compare.log`; JSON: `p8-compare.json`.
- Three-way 150-key check (REG vs text.md vs P8 printed keys, `rerun/REG.json` via `dump_reg.py`, comparison in `threeway.json`): **149/150 exact matches**. Only Q150 differs by design (writing item): REG key «(Открытое задание — образец текста ниже)», text.md «150. ✓ Образец текста в разделе H ниже (99 слов)», P8 prints «✓» — the documented writing-item format; gates.py skips it too. Q140 key is the Italian sentence «Ogni cifra deve essere chiara.» in REG, text.md, P8, and core alike — no keydiff is correct behaviour (Q140 translates INTO Italian), not an omission.

## 10. gates.py copy re-run (20/20 PASS)

Copy from `scratch-fanout-it/`, repointed SCRATCH to my dir. Log: `gates-ru.log`. Output JSONs in `ru/`.
- Honest note: the first run showed 3 FAILs only because the output dir `ru/` did not exist — after `mkdir -p ru/`, re-run: **20 PASS, 0 FAIL — GATES ALL PASS**.
- The 20 PASS lines: occlusion 0 flags; p8 extract noted count 150 rc=0; p8 compare CLEAN keydiffs=[137, 138, 139]; freeze diff fragments explained by translations/furniture (P1–7), unexplained_add=[] unexplained_rem=[]; freeze diff report present (pages 1–8); freeze strict-cjk (no added CJK except U+3000), rc=1 added_cjk={'\u3000': 8} non_space={}; print/web text multiset identical; web PDF < 7MB (1441225 bytes); print PDF size sane (14180887 bytes); P8 min font >= 13px (9.75pt), min=13.0; paper #fbfaf6 present; no gold/brick/near-black, hits=[]; no VOL.5 in furniture (only preview/disclosure), VOL.5 text nodes=3; VOL.4 present, count=9; badge colours A2/B1/B2; no double outer frame, full-page rects=0; textmd validate forward-miss: 0 reverse-miss: 0; answers count 150 (edition=150 core=150); keys 1–150 match core (except 137–139 re-aimed, writing), mismatches=[]; notes match translations.py (except 137–140 + writing), mismatches=[] table_gaps=[].
- One INFO line: '·' total occurrences in SVGs: 148 (core had them only in options/gloss lists).

## 11. §1.1 scans (from gates.py + proofer's own)

- P8 min font 13.0 px = 9.75 pt — exactly at the SOP §1.1 floor, not below (PROOF-NOTE O-16).
- Paper #fbfaf6 present; no gold/brick/near-black; VOL.5 in exactly 3 legitimate nodes; VOL.4 ×9; badge colours present; 0 full-page rects.
- No tofu observed in any of the 8 print-page renders or the web P1/P2/P8 renders (§14).

## 12. Character scans

- text.md: CJK ideographs 0; U+3000 ×101; U+FF1A ×14; U+2019 0; banned terms Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu all 0; «Translate» 0; «Переведите» 8 (Q137–140 ×2: exercise labels + P8 section-E labels).
- Fullwidth colon ： in 7 frozen P8 notes (16–20, 60–61) — core-inherited (PROOF-NOTE O-10).

## 13. Title count (measured, not assumed)

- Definition: stripped line all-uppercase, len>3. text.md: **98 all-caps lines** (en edition measured 85 under the same rule — difference is Russian all-caps gloss lines).
- Headlines **6/6 present**. String «56» occurs 2× (exercise 56 stem + key). «56 titles» is a phantom number; no element of this edition counts 56 (PROOF-NOTE O-15).

## 14. Visual read (fresh renders, proofer's own)

- Print PDF, fresh 96 dpi renders `pages/p--1.png` … `pages/p--8.png`, all 8 viewed. P1: clean except P1 cifre title overflow (observation per STRADDLE). P2: clean except P2 frase title (observation). P3: clean (core-pattern mid-page whitespace). P4: clean (E TU box 2 lines + gloss, flush with table; results table clean). P5: clean (core-pattern whitespace). P6: clean except inherited «18.» orphan line. P7: LETTERE disclosure 3 lines, clear of FRASI hline; errori title fits. P8: dense but legible, «Переведите на русский/итальянский» labels correct, model text present, keys flow ends 2529/2552, no footer intrusion. No overflow, overlap, footer intrusion, or tofu other than the two title observations.
- Web PDF: `pages/web-p1--1.png` and `pages/web-p8--8.png` viewed; P2 rendered fresh this session (`pages/webp2-2.png`, pdftoppm -r 96) and viewed. Web P1/P2/P8 identical in layout to print; no tofu; the P1/P2 title overflows appear identically in web. Defect D-1 visually confirmed in web P8: key 100 «scaglione = налоговая ставка», key 144 «scaglione = налоговая ставка, a».

## 15. Fact verification (web, 2026-11-11)

- **Manovra 2027**: hearings Nov 9–12, joint Camera/Senato Budget committees, Giorgetti Thu Nov 12 (Bankitalia, UPB, Giorgetti); amendments deadline Tue Nov 17 18:00; bill C. 3174-bis; final approval by Dec 31, 2026; ~26 miliardi; approved by Council of Ministers Oct 28 — confirmed by multiple Italian news sources.
- **DPB**: approved CdM Oct 13, sent to EU/Parliament Oct 15; growth +1.0% 2026, +0.8% 2027; deficit 2.9% 2026, 3.4% 2027 (with NEC clause), 3.2% 2028 — confirmed (doppiominimo.com, dirittobancario.it, sienapost.it).
- **BookCity Milano 2026**: 15th edition Nov 23–29; theme «Il senno sulla Luna»; 1,360 events / 2,487 protagonists / 1,164 books / 443 venues; opening Mon Nov 23 20:00 Teatro Dal Verme with Colson Whitehead (two Pulitzers); preview Sun Nov 22 16:00 Fondazione Luigi Rovati with Edmund de Waal («Come cominciare», Bollati Boringhieri, introduced by Giovanna Forlanelli) — confirmed, incl. official press release (bookcitymilano.it) and edmunddewaal.com.
- **Torino Film Festival**: 44th edition, Tue 24 Nov – Wed 2 Dec 2026, nine days — confirmed from the official regulation: «Il 44° Torino Film Festival si svolgerà da martedì 24 novembre a mercoledì 2 dicembre 2026, per la durata di nove giorni.» (torinofilmfest.org).
- **Eurochocolate 32nd edition / Festa del Torrone 29th edition**: rest on it-en proof2's 2026-11-11 verification (not re-litigated).
- **Dates/weekdays** verified with `date -d` (Europe/Rome): Nov 6 Fri, 7 Sat, 8 Sun, 9 Mon, 12 Thu, 15 Sun, 16 Mon, 17 Tue, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 23 Mon, 24 Tue, Dec 2 Wed, Dec 31 Thu, Oct 15 Thu, Oct 28 Wed — all match the paper.
- **Arithmetic** re-done by hand: MD11 goals 3+1+2+3+3+2+3+1+2+4 = 24 in 10 matches ✓; Q85 13−11=2 ✓; Q86 6+7=13 ✓; classifica Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 / Udinese 5 (20th) consistent across P1, P4 table, keys ✓; Torrone Nov 7–22 = 16 days / 3 weekends ✓; Torino Film Festival Nov 24–Dec 2 = 9 days ✓; BookCity Nov 23–29 = 7 days ✓.
- **Golden sentences 8/8 at exactly 2× each** (article + P7 FRASI): «La Lazio resta in vetta», «ventiquattro gol in dieci partite», «il ponte votivo sul Canal Grande», «oltre centocinquanta figuranti in costumi rinascimentali», «la squadra di Gattuso è ancora imbattuta dopo 11 giornate», «sette giorni di libri, ragioni e follie», «il testo può ancora cambiare», «approvato dal governo non vuol dire già legge».
