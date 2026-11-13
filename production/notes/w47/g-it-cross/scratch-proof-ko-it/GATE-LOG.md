# GATE-LOG — 2026-W47 ko-it proof1 (independent)

All gates re-run by the independent proofer on 2026-11-11 from the scratch
work copy in this directory (`work/` = sources copied from the shipped
edition dir, md5-verified identical; `it/p8-it.json` = own extract).
Logs / products in this directory unless noted.

## Probes & SHA verification (before / after)
- `ls /dev/null` present; `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`, rc=0.
- Write probe `probe.txt` in this dir OK before starting.
- Edition SHAs (before AND after proof, identical):
  - print `Lucerna-VOL4-KO-IT.pdf` 45,676,964 B `54e35033…aa4b0` ✓
  - web `Lucerna-VOL4-KO-IT-web.pdf` 4,025,960 B `f6135c50…a4900` ✓
  - text `2026-w47-ko-it.text.md` 35,213 B `247ed6bd…575c` ✓
- Core SHAs (before AND after proof, identical):
  - print 46,232,227 B `53bf14ed…21a2f27` ✓; web 4,232,878 B `9592945a…bc7` ✓;
    text `2026-w47-ko-zh-cn.text.md` 34,606 B `da1d3a32…81a` ✓
- ABSTRACT.txt 364 B `c3e23f5a…37fbe` ✓ (matches FANOUT record).

## Gates

| # | Gate | Command (interpreter) | Log / product | Result |
|---|---|---|---|---|
| 1 | run.py | `/usr/bin/python3 run.py` in `work/` | `run-proof.log`, `rerun-svg.sha` | rc=0, TOTAL 150, 0 overflow; rebuilt SVGs 8/8 SHA-identical to shipped |
| 2 | freeze baseline | `/usr/bin/python3 tools/freeze.py baseline --build work --core-svg <edition>/svg --out <deleted after logging>` | `freeze-proof.log` | rc=0, **8/8 byte-identical**; core SVGs re-hashed unchanged |
| 3 | freeze diff | `/usr/bin/python3 tools/freeze.py diff --core-svg core-ko/svg --edition-svg <edition>/svg --json freeze-diff-proof.json` | `freeze-diff-proof.log`, `freeze-diff-proof.json` | rc=0, added CJK **7, all U+3000** |
| 4 | occlusion audit | `/usr/bin/python3 tools/occlusion_audit.py --core core-ko/svg --json occlusion-proof.json <edition>/svg` | `occlusion-proof.log`, `occlusion-proof.json` | rc=0, **0 flags** (core 0, NEW 0); selftest 6/6 fired |
| 5 | p8 extract | `/usr/bin/python3 tools/p8.py extract --p8 <edition>/svg/p8-siheom.svg --total 150 --json it/p8-it.json` | `p8-extract-proof.log`, `it/p8-it.json` | 150/150 noted |
| 6 | p8 compare | `/usr/bin/python3 tools/p8.py compare --core-p8 core-ko/svg/p8-siheom.svg --edition-p8 <edition>/svg/p8-siheom.svg --total 150 --json p8-compare-proof.json` | `p8-compare-proof.log`, `p8-compare-proof.json` | **CLEAN**, keydiff=[137, 138] |
| 7 | keycheck | `/usr/bin/python3 keycheck-proof.py it` (own REG + own P8 extract) | `keycheck-proof.log` | **150/150** (149 exact + #150 `✓`); per page 10/10, 18/18×5, 12/12, 38/38 |
| 8 | check_core | `/usr/bin/python3 check_core.py` in `work/` | `check-core-proof.log` | rc=0, gloss 0, phrases 8/8, orphan 0, dates verified |
| 9 | check_gloss | `/usr/bin/python3 check_gloss.py` in `work/` | `check-gloss-proof.log` | rc=0, gloss fails 0 |
| 10 | textmd re-export | `/usr/bin/python3 textmd.py . 2026-w47-ko-it textmd-proof.md "<title>"` in `work/` | `textmd-proof.log`, `textmd-proof.md` | 449 items, **byte-identical** to shipped text.md (SHA `247ed6bd…575c`) |
| 11 | text-layer identity | PyMuPDF extraction (venv) + `cmp`; pdftotext extraction + `cmp` | `textlayer-print.txt`, `textlayer-web.txt` (48,319 B each, identical); `/tmp/pdftxt-*.txt` (51,894 B each, identical) | **byte-identical** under both extractors |
| 12 | web re-render | `tools/venv/bin/python tools/webpdf.py svg webproof.pdf` in `work/` (scratch only; file deleted after logging) | `webpdf-proof.log`, `webproof.txt` | rc=0, 8 pages, text layer byte-identical to shipped web; 4,025,961 B, SHA differs as expected (fontTools clock) |
| 13 | P8 min font | PyMuPDF (venv) on shipped print PDF p.8 | computed in run (no separate log file) | **9.975pt**, 359 spans, 166 at-min; PASS ≥9.75pt |
| 14 | boxtitle | `/usr/bin/python3 boxtitle-ko.py work/` | `boxtitle-proof.log` | **8/8 ≤ 386.5px**; tightest 366.7px (margin 19.8px); P5 359.4px (margin 27.1px) |
| 15 | curly sweep | `grep -c` U+201C/U+201D/U+2019 per SVG + text.md | computed in run | **0/0/0** everywhere |
| 16 | hanzi residual | regex `[\u4e00-\u9fff]` over `<text>` elements | computed in run | **0** in `<text>`; 3 chars only in `<title>Lucerna 三色蛾</title>` (core-identical metadata) |
| 17 | lone-punctuation sweep | `<text>` elements starting with closing punctuation | computed in run | 9 hits, all wrapped `· B./· C.` continuations (core has 7 of the same class); orphan scan 0 |
| 18 | §1.1 style audit | paper/VOL.4/VOL.5/`·` counts core vs it per page | computed in run | identical page-by-page except P7 VOL.5 3→2 by design |
| 19 | census | `/usr/bin/python3 census.py <edition>/text.md work/` | `census-proof.log` | 166 ex/match items, **0 missing**; D6 missing 0 |
| 20 | 150-item 3-source check | own `reg150.py` extraction vs record table vs own P8 extract; notes/stems audit | `reg150.py`, `reg150.json`, `reg-proof.json` | 150/150 rows match record; 0 SVG-key mismatches; 25 Hangul notes all headword references by design |
| 21 | visual read | 100dpi PNGs from shipped print PDF (venv PyMuPDF) | `pages/p-1.png` … `pages/p-8.png` (2032×2813) | **8/8, zero issues** |
| 22 | D5 font census (record only) | font-family counts per SVG | computed in run | Noto Sans CJK SC segments: **0**; it Sans KR 620 / Serif KR 881 / UnifrakturMaguntia 1 (core 603/877/1) |
| 23 | "next Sunday" rule | grep core-ko/, edition, tools/tables.py | computed in run | **0 hits** — rule N/A, not applied |

## Not applicable
- Old-version page-by-page comparison: no prior ko-it edition existed.
- No commit / push made. Shipped PDFs untouched (only read + hashed).

## Cleanup
- `freeze-out/` build-copy (11 MB) and scratch `webproof.pdf` (4,025,961 B)
  deleted after their results were logged; shipped web PDF never overwritten.
