# GATE-LOG — 2026-W47 ko-ja (proof1)

Independent re-run of every gate by the proofer (2026-11-11). All paths under
`hidden_files/w47/scratch-proof-ko-ja/` unless noted. Interpreters per the
family iron rule: freeze / run.py / check_core / check_gloss / textmd on
**/usr/bin/python3 (Pillow 10.2.0 / FreeType 2.13.2)**; render (PyMuPDF) and
occlusion-venv control on **tools/venv/bin/python (Pillow 13.0.0)**.

## Probes (before work)

| Check | Result |
|---|---|
| `ls /dev/null` | present (`crw-rw-rw-`) |
| `echo test \| git -C ~/workspace/weekly-git hash-object -w --stdin` | `9daeafb9864cf43055ae93beb0afd6c7d144bfa4` (one probe object written to the repo object store; no file/branch/commit/push) |
| write test in goals-side work dir | OK (`.probe`) |
| disk | 66 G free at start of proof |

## SHA verification

| File | Bytes | SHA-256 | Log |
|---|---|---|---|
| print `Lucerna-VOL4-KO-JA.pdf` | 51,357,740 | `7bc95f97…e2cae2d4c` | matches task brief |
| web `Lucerna-VOL4-KO-JA-web.pdf` | 4,388,239 | `9f0567aa…a8a9c0` | matches task brief |
| `2026-w47-ko-ja.text.md` | 35,425 | `635ec8af…d9e97` | matches task brief, 450 items |
| `ABSTRACT.txt` | 342 | `4a9445de…3157a` | matches builder record |
| core print `Lucerna-VOL4.pdf` | 46,232,227 | `53bf14ed…21a2f27` | before = after proof |
| core web `Lucerna-VOL4-web.pdf` | 4,232,878 | `9592945a…bc7` | before = after proof |
| core `2026-w47-ko-zh-cn.text.md` | 34,606 | `da1d3a32…68181a` | before = after proof |

## Gates

| # | Gate | Command / tool | Result | Log |
|---|---|---|---|---|
| 1 | run.py | `/usr/bin/python3 run.py` in scratch copy `work/ed/` | rc=0; 0 FLOW OVERFLOW / HEAD TOO WIDE; TOTAL 150 (A2 51 / B1 72 / B2 27; pages 10/18/18/18/18/18/12/38); P2-feature ends 1531; P8-keys ends 2351; P7 teaser 2454.7; regenerated 8 SVGs byte-identical to shipped | `run-proof.log` |
| 2 | freeze baseline (system) | `/usr/bin/python3 tools/freeze.py baseline --build <edition> --core-svg <edition>/svg --out freeze-base` | **8/8** byte-identical; core SVGs re-hashed unchanged | `freeze-base.log`, `freeze-base.json` |
| 3 | freeze baseline (venv control) | `tools/venv/bin/python tools/freeze.py baseline …` | **ABORT rc=2** (ko family requires Pillow 10; designed control) | `freeze-base-venv.log` |
| 4 | freeze diff | `/usr/bin/python3 tools/freeze.py diff --core-svg core-ko/svg --edition-svg ko-ja/svg` | added CJK **2901** (p1 122, p2 257, p3 204, p4 154, p5 211, p6 121, p7 345, p8 1487); strings +17/−17, +35/−34, +28/−27, +22/−22, +32/−31, +16/−15, +38/−38, +167/−167 | `freeze-diff-proof.json` |
| 5 | freeze-diff adjudication (own verifier) | `/usr/bin/python3 verify-freeze-diff-proof.py freeze-diff-proof.json` | **added unexplained 0/307; removed unexplained 0/303** | `verify-freeze-diff-proof.log`, `verify-freeze-diff-proof.py` |
| 6 | occlusion audit (system) | `/usr/bin/python3 tools/occlusion_audit.py <edition>/svg` | **0 flags**; selftest 6/6 classes fired | `occlusion-proof-sys.log/.json` |
| 7 | occlusion audit (venv) | `tools/venv/bin/python tools/occlusion_audit.py <edition>/svg` | **0 flags**; selftest 6/6 classes fired | `occlusion-proof-venv.log/.json` |
| 8 | p8.py extract | `/usr/bin/python3 tools/p8.py extract --p8 p8-siheom.svg --total 150` | 150/150 noted | `p8-extract-proof.log`, `p8-proof.json` |
| 9 | p8.py compare | `/usr/bin/python3 tools/p8.py compare --core-p8 … --edition-p8 … --total 150` | **CLEAN**; missing=[] extra=0; keydiff=[137, 138] | `p8-compare-proof.log/.json` |
| 10 | keycheck (own parse) | `/usr/bin/python3 keycheck-proof.py keycheck-proof.json` | **150/150** (149 exact + #150 `✓`); 0 diffs vs p8.py's keys; per page 10/10, 18/18, 18/18, 18/18, 18/18, 18/18, 12/12, 38/38 | `keycheck-proof.log/.json`, `keycheck-proof.py` |
| 11 | check_core | `/usr/bin/python3 <ko3>/ja/checks/check_core.py` | rc=0; gloss fails 0; P7 phrases **8/8 verbatim**; orphan 0; dates verified | `checks-proof.log` |
| 12 | check_gloss | `/usr/bin/python3 <ko3>/ja/checks/check_gloss.py` | rc=0; gloss fails 0 | `checks-proof.log` |
| 13 | print/web text layers (PyMuPDF) | venv `fitz`, `get_text("text")` per page | **byte-identical**; 49,499 B each; 8 pages each; SHA `1ddc2d5f…` both | `textlayer-proof.log`, `text-print-proof.txt`, `text-web-proof.txt` |
| 14 | print/web text layers (pdftotext) | `pdftotext -layout` both PDFs + `cmp` | **identical**; 95,759 B each | `text-print-pdftotext.txt`, `text-web-pdftotext.txt` |
| 15 | P8 min font | venv PyMuPDF `page.get_text("dict")` on print PDF p8 | **9.975 pt** (≥ 9.75); 158 spans at min of 351; sizes 9.975–34.5; stem 10.35 pt | `textlayer-proof.log` |
| 16 | boxtitle widths | `/usr/bin/python3 <ko3>/boxtitle-ko.py <edition>` | **8/8** ≤ 386.5 px; P3 fixed title 347.4 px (was 393.4 OVER); min margin 39.1 px | `boxtitle-proof.log` |
| 17 | P8 #81 line | own parse + `svglib.text_w` (serif 13.3) | single `<text>` element; **397.4 px** (old 463.4 px); full line `81. 비행기는 듣기 시간에 뜨지 않아요. — 聴解中は飛行機が飛ばない` | `p8-81.txt`, `keycheck-proof.json` |
| 18 | creambox true-ink | `/usr/bin/python3 creambox-proof.py` (own, transform-aware, PIL getbbox ascender-corrected) | **0 overflows**; 49 cream rects, 223 paired lines; worst clearance **+3.1 px** (P2 あなたは？ last line) | `creambox-proof.log/.py` |
| 19 | creambox adjudication | `/usr/bin/python3 creambox-adjudicate.py` | all 18 v1 flags traced to the v1 ascender bug; no real overflow (see PROOF-NOTE §7.4) | `creambox-adjudicate.log/.py` |
| 20 | isolated-punctuation sweep | `/usr/bin/python3 sweeps-proof.py` | **0** in 8 ja SVGs, 8 core SVGs, ja text.md, core text.md | `sweeps-proof.log/.py` |
| 21 | U+2019 / curly sweep | same | **0** (U+2019/U+201C/U+201D) in 8 SVGs + text.md, ja and core | `sweeps-proof.log` |
| 22 | §1.1 grep audit | `/usr/bin/python3 <ko3>/style11-ko.py ja` | log **byte-identical** to builder's; paper/VOL.4/`·`/colours = core per page; hanzi 62/133/100/76/116/66/154/825; CJK stray 0/276; P7 VOL.5 3→2 by design; U+2019 0 | `style11-proof.log` |
| 23 | text.md re-export | `/usr/bin/python3 textmd.py . 2026-w47-ko-ja <out> "<title>"` | reproduces shipped file **byte-for-byte, SHA identical**; 450 items | `textmd-proof.log/.md` |
| 24 | census ex/match + D6 | `/usr/bin/python3 <ko3>/census.py <textmd-proof> <edition>` | 166 items, **0 missing**; D6 **0 missing** | `census-proof.log` |
| 25 | text.md self-read | full read of shipped text.md | zero issues | PROOF-NOTE §5 (read in full) |
| 26 | 150 items, three-source hand verification | `/usr/bin/python3 items150-proof.py` + full TSV read | **150/150 OK**; core-vs-ja key diffs only #137/#138/#150 (translation); ja-vs-SVG key diffs 0 | `items150-proof.log/.json/.tsv`, `items150-proof.py` |
| 27 | 8-page visual read | venv PyMuPDF, 100 dpi, print PDF → `pages/p1.png`…`p8.png`, read each | **8/8, zero issues** (P3 title one line; P8 #81 one line) | `pages/`, PROOF-NOTE §6 |
| 28 | "next Sunday" freeze rule | `grep -rn "next Sunday" core-ko/ ko-ja/ tools/tables.py` | **0 hits** — no applicable object | (grep rc=1) |
| 29 | D5 font (record only) | font-family census over 8 ja SVGs | **0** Noto Sans CJK SC segments; families: Serif KR 873, Sans KR 611, UnifrakturMaguntia 1; Latin-only spans: Sans KR 278, Serif KR 13, UnifrakturMaguntia 1 | `sweeps-proof.log` |
| 30 | SVG hashes vs run-2 record | `sha256sum svg/*.svg` vs `ko3/ja/sha-ja-run2.txt` | identical | (diff rc=0) |
| 31 | core integrity | core SHAs before proof vs after proof | identical (see SHA table above) | — |

## Notes on method

- The builder's logs/records were treated as claims, not evidence; every number above was produced by a fresh run in this work dir.
- `creambox-proof.py` v1 had a real measurement bug (PIL `getbbox` y is ascender-relative, not baseline-relative); v2 corrects it per the canonical `occlusion_audit.py` formula (`ink top = y − ascent + t`). The 18 v1 flags were all artefacts of that bug; the corrected run gives 0 overflows. Both the v1 bug and the fix are disclosed in PROOF-NOTE §7.4.
- Text-layer byte counts differ by extractor (PyMuPDF 49,499 B; pdftotext-layout 95,759 B; builder 53,212 B) — extraction-mode artefact; print == web under every method.
- `tools/freeze.py` was read but never edited. No commit / push / insert.py / lint --write was run.
