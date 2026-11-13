# GATE-LOG.md — 2026-W47 it-ru D-1 fix round, mechanical gates self-run

Fix round for proof2 (b) defect D-1 (`scaglione` → «ступень налоговой шкалы»). All commands run with `TMPDIR=<scratch>/tmp`, `PYTHONDONTWRITEBYTECODE=1`, tools venv python (`~/workspace/weekly-git/tools/venv/bin/python`, Pillow 13.0.0, freetype 2.14.3). Production read-only during rebuild; copy-back only after the rebuild gates passed; production gates re-run after copy-back. No commit, no push.

## 0. Hard-gate probes (pre-work, 2026-11-11 ~21:07 UTC)

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2…`, RC=0.
- Real file written to scratch `probe.txt` (`fix-probe-20261111-210747`).
- System /tmp (512M) never used for work files (one accidental fragment `cp … /tmp/nonexistent` immediately removed; see FIX-LOG §7).
- Pre-fix three SHA verified exact before any edit: print 14,180,887 B `f74bd65735550718a9927adb47047547d6cd3972f9ccfa4164bd467bf257c3fd`; web 1,441,225 B `c35f390b39e3fe0ef6e95f9a9a292ab94cc356a3955decdcd2dbcd4cf357d1f5`; text 67,687 B `d1b6ddb1e691f74f7a7ce2960077774987dfd36b99712c8b3b49bb254a8361e2`.

## 1. Identity (new three SHA — production, after copy-back)

| File | Size | SHA-256 | Previous (re-fan-out) |
|---|---|---|---|
| Print PDF `La-Lucerna-VOL4-RU.pdf` | 14,180,929 B | `af980e26fcb124773e0e3a5824e3ff742e6a72f8da50c8e53ab017418adf6200` | 14,180,887 B `f74bd657…57c3fd` |
| Web PDF `La-Lucerna-VOL4-RU-web.pdf` | 1,441,248 B | `3e10d785bd1eab5318ef175a52bdebef89649622d1a7f53ea891b54b4f652cc9` | 1,441,225 B `c35f390b…57d1f5` |
| Text `2026-w47-it-ru.text.md` | 67,752 B / 1317 lines | `8a49ce37cc7df3ba92569243cd28b0286bee6651547f526c8cacdf112c5c895c` | 67,687 B `d1b6ddb1…361e2` |

New SVG SHAs: p6 `a36aa3ce1eeab8f1f30412f149dbea22b1cff0f5c499a8751a912fd518f425e2`, p8 `6faa486ae94a6a512e530235b78e51bba977a2596e907552c420bd134c4a4165`; other 6 SVGs unchanged (verified against `shipped-svg.sha256`: p1 `dcbe4b97…`, p2 `462eb58b…`, p3 `87c35bf2…`, p4 `8c4910d6…`, p5 `needfe6a…`, p7 `31372b24…` all OK).

## 2. Build interpreter

- `~/workspace/weekly-git/tools/venv/bin/python`, Pillow 13.0.0, freetype 2.14.3.
- Core untouched: freeze baseline (see §5) re-verified core-it reproduces 8/8 and core SVGs unchanged.

## 3. run.py re-run (scratch rebuild) — RC=0, TOTAL 150, 0 overflow

- Rebuild via `rebuild.py` (copy of `build_edition.py`, EDROOT/OUT/BASE repointed to scratch; imports the fixed `translations.py` from `scratch-fanout-it`). Log: `rebuild-logs/build1.log`.
- RC=0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE. `ALL DONE`.
- Flow ends (changed only where expected): P6-main 1379/1520 (was 1349; +30 px = one extra NOTE-gloss line); P8-keys 2529/2552 (unchanged); all other flows identical to the proof2 rerun log.
- Levels: A2 47 / B1 70 / B2 33. Pages: 10/18/18/18/18/18/12/38. Model words 99.

## 4. Rebuild-vs-production diff (before copy-back)

- SVGs: only p6/p8 differ; p1–p5, p7 byte-identical (`cmp`).
- Cards: only p6/p8 differ; other 6 byte-identical.
- text.md diff: exactly 5 lines (663/763/987/1217/1305).
- content files: diff vs rebuild copies is only the OUT/BASE path line, plus the 3 fixed strings (content56.py:126/:229, content8.py:85).

## 5. Freeze (canonical tool)

- **freeze.py baseline** (`--build core-it --core-svg core-it/svg --out scratch/freeze-baseline`): RC=0, **8/8 byte-identical**; core integrity unchanged (8 files re-hashed). Log: `freeze-baseline.log`. Core verified as true core, not self-compared.
- **freeze.py diff** core vs fixed edition (run inside gates.py, both runs): 0 unexplained add/rem (P1–P7); strict-CJK added = 8 × U+3000 only (exempt furniture separators). JSON: `ru/freeze-diff.json` (rebuild run) / `ru-prod/freeze-diff.json` (production run).

## 6. Occlusion audit (canonical tool)

- Run inside gates.py on the 8 rebuilt SVGs and again on the 8 production SVGs: **0 flags** both times. (Selftest was run by proof2 on the same tool version and passed; the tool is unchanged since.)

## 7. Width verification (D-1 renderings, pre-build + post-build)

- Pre-build `measure_widths.py` (edition's own ru svglib `wrap()`): P8 key 100 single line 344.7/422.5 px; P8 key 144 single line 308.6/422.5 px; P6 NOTE gloss 6 → 7 lines (P6-main spare 171 px).
- Post-build node + PIL measurement on rebuilt SVGs: key 100 last run «шкалы» x=1287.4, right edge 1333.6 vs column right 1411.5 (77.9 px spare); key 144 last run «шкалы, a» x=1689.0, right edge 1749.2 vs 1862.0 (112.8 px spare). PIL full-line widths 353.0 / 316.7 px agree with `wrap()` within ~2.5%.
- Visual: rebuilt print P6 (`pages/fix-p6-6.png`) and P8 (`pages/fix-p8-8.png`) viewed at 96 dpi; crops `pages/crop-key100.png`, `pages/crop-key144.png` viewed — both keys single-line, legible, clear margins; NOTE gloss 7 lines inside its box, last line «процедура.» in-box, clean gap to the chart below. Q144 stem («un livello di reddito del sistema fiscale») vs note («ступень налоговой шкалы») no longer contradictory.

## 8. Text-layer consistency (print vs web PDF)

- `gates.py`, both runs: print/web text multiset identical — print_words=7590, web_words=7590, chars_equal=True, word_diff=[].
- Old form «налоговая ставка»: 0 in SVG flat text, 0 in text.md, 0 in web PDF text layer, 0 in print PDF text layer. New form «ступень налоговой шкалы»: SVG flat p6=1, p8=2; text.md 5× (lines 663/763/987/1217/1305); web + print PDF text layers 3× each.
- Web PDF 1,441,248 B < 7 MB.

## 9. p8.py extract + compare (canonical tool, `--total 150`)

- Extract: 150/150, RC=0 (both runs). JSONs: `ru/p8-extract.json`, `ru-prod/p8-extract.json`.
- Compare vs core: status **CLEAN**, missing [] / extra [] / uncertain [], keydiff **[137, 138, 139]** (expected re-aimed reader-sentence keys). JSONs: `ru/p8-compare.json`, `ru-prod/p8-compare.json`.

## 10. gates.py (20/20 PASS, twice)

Gates script: proof2's `gates.py` copied to this scratch, repointed (EDROOT→rebuild dir for the first run; `gates-prod.py` with EDROOT→production for the second). Logs: `gates-fix.log` (rebuild), `gates-prod.log` (production). Both identical verdicts:

```
PASS occlusion 0 flags
PASS p8 extract noted count | noted=150 rc=0
PASS p8 compare vs core | verdict=CLEAN keydiffs=[137, 138, 139]
PASS freeze diff fragments explained by translations/furniture (P1-7) | unexplained_add=[] unexplained_rem=[]
PASS freeze diff report present | pages=['1', '2', '3', '4', '5', '6', '7', '8']
PASS freeze strict-cjk (no added CJK except U+3000) | rc=1 added_cjk={'\u3000': 8} non_space={}
PASS print/web text multiset identical | print_words=7590 web_words=7590 chars_equal=True word_diff=[] []
PASS web PDF < 7MB | 1441248 bytes
PASS print PDF size sane | 14180929 bytes
PASS P8 min font >= 13px (9.75pt) | min=13.0
PASS paper #fbfaf6 present
PASS no gold/brick/near-black | hits=[]
PASS no VOL.5 in furniture (only preview/disclosure) | VOL.5 text nodes=3
PASS VOL.4 present | count=9
PASS badge colours A2/B1/B2
PASS no double outer frame | full-page rects=0
INFO '·' total occurrences in SVGs: 148 (core had them only in options/gloss lists)
PASS textmd validate | 2026-w47-it-ru forward-miss: 0 reverse-miss: 0
PASS answers count 150 | edition=150 core=150
PASS keys 1-150 match core (except 137-139 re-aimed, writing) | mismatches=[]
PASS notes match translations.py (except 137-140 + writing) | mismatches=[] table_gaps=[]
GATES ALL PASS
```

## 11. §1.1 scans (from gates.py)

- P8 min font 13.0 px = 9.75 pt — exactly at the SOP §1.1 floor, not below.
- Paper #fbfaf6 present; no gold/brick/near-black; VOL.5 in exactly 3 legitimate nodes; VOL.4 ×9; badge colours present; 0 full-page rects.

## 12. Untouched items (explicitly not changed, per task)

- P1/P2 bilingual box titles: text.md:45 (`LA SETTIMANA IN CIFRE　НЕДЕЛЯ В ЦИФРАХ`) and :205 (`LA FRASE PER RICORDARE　ЗАПОМНИТЕ`) byte-identical to the pre-fix version; p1/p2 SVGs byte-identical. STRADDLE observations O-1/O-2 stand as observations.
- Q140 key: still the Italian sentence «Ogni cifra deve essere chiara.» in REG, text.md, P8 and core alike — correct behaviour, not changed.
- Other 8 languages' `scaglione` values in translations.py: untouched (diff vs pre-fix backup is exactly the 3 ru lines).
- Core-it: untouched (freeze baseline §5). No commit, no push.
