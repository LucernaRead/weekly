# INSERT-LOG — W47 ru bundle

- Worker: 恢复协调员 #6 派单，步骤 4，第十家（ru）
- Date: 2026-11-13
- Repo: `~/workspace/weekly-git`
- Start HEAD (verified): `7e8ce057812488a98156155048362b1b37fa114f` (pt bundle commit)
- Disk before: 98G used / 150G (df -h); after: 98G used — no scratch freed (see §Cleanup)
- Method: original `tools/insert.py` `render_md` + `resolve_bundle_dir` imported directly;
  `main_bundle` (c)–(e) reproduced, skipping only the clean-tree check (535 known `??`
  render-product lines must stay on disk, never committed) and the push.
- Commit message (verbatim, as main_bundle builds it): `Add 2026-w47-ru bundle (RU text · 11 natives)`

## Seed excerpt (step b)

No ru edition existed in `issues/2026-w47/`, so seed mode was required.

Precedent verified (W46): `issues/2026-w46/2026-w46-ru-en/2026-w46-ru-en.md` excerpt
equals exactly the first two complete sentences of the P1 headline body paragraph
in `production/2026-w46/core-ru/2026-w46-ru-zh-cn.text.md`:
> Эта неделя в России — обычная. В понедельник, 9 ноября, люди идут на работу и в школу.

W47 seed excerpt (same rule, from `production/2026-w47/core-ru/2026-w47-ru-zh-cn.text.md`
P1 headline body paragraph, first two sentences) — cross-checked verbatim against
`production/covers/2026-w47/cover.json` `stories.ru.excerpt` (identical):

> Все восемь матчей 14-го тура завершены: тур сыграли 6–8 ноября. «Зенит» и «Динамо» набрали по 31 очку и делят первое место в таблице.

- exercises: 150 (all 11 editions)
- ru-zh-cn edition dir resolved via `resolve_bundle_dir` core fallback: `production/2026-w47/core-ru`
- All other 10 natives resolved to `production/2026-w47/2026-w47-ru-<native>/`

## Render pins (step b — measured from the actual web PDFs / .text.md files)

| slug | web PDF bytes | web PDF SHA-256 | text bytes | text SHA-256 |
|---|---|---|---|---|
| 2026-w47-ru-de | 3334229 | acc21d4dd4a69aab6fc60bcf8b5d52263309e9cceea9376528e9303f5a1d0fcc | 63483 | 31d3eb3eb22309d9bc432abb5ab7f755844e43c9de4bdfd8cfd0677a630ea235 |
| 2026-w47-ru-en | 3328923 | a3148c31c5a9e1b95676d4acb5879ab82da70d9720fea33fa552bdd4d0b9037c | 62785 | 6c6932fb809faae84647120cb8a33fabd0fb7f5879963181328a5623e7c5c48f |
| 2026-w47-ru-es | 3333651 | 662998dc1e54f435f8fa08df31af846ddd8cf88990eeb3b97758dd1d5426ab05 | 64176 | bb298469263f40a5c36b1052a347902af791e1847a0425a705ad20ff8a90f0ed |
| 2026-w47-ru-fr | 3334407 | b36ecf778e2707687bc19e48c941297190bb2423f3dd969451388c780aea0f09 | 63364 | 445daf81541af4f0f822d096e664428bd2f1e0dd23386d26809a1dcaa11a8e08 |
| 2026-w47-ru-it | 3330610 | 6ea69cc772a60f6f9a733862f0ce8f2c38836bba2c030208df376f5f5c8f3077 | 63970 | a46c6da6426253c5e52c6124c10976ca5aa955d7f2db438995002b4e933f1434 |
| 2026-w47-ru-ja | 3692713 | dc9f27b03891763b1c986b31a70cca0ef50b77442e632ee63fd600cad9b27c8c | 64504 | 465a2e4ebcd87b0f638609f9af1fc4d7a830e9a1b2a83bbdb7eb73efb7568f4d |
| 2026-w47-ru-ko | 3494572 | a6a997780723540d904e4d86c2203bb9191362bd3a0124e707e3f3a660bedf6d | 65030 | 050d188396312cab8e3a8544614799c1f44377a559a51043dfbfc6818e544b71 |
| 2026-w47-ru-nl | 3329737 | 1abee50e00351cd4d9663bae1f2fd188f45a83a9f0bd1378c883bef97aba9622 | 64011 | b600944e5e5faacf6127e0a892c87519286bd2cd5429bbc070dafaf63fab184b |
| 2026-w47-ru-pt | 3337256 | a8c1afb037223c476adf5fb76a7c6ac942fa852419da2bddb21fab45f989c079 | 65102 | 67ced8562a719470ecce14fc4d19319413754416ee2105212aed2e3e07931e50 |
| 2026-w47-ru-zh-cn | 3898280 | e37922c048d1a46e32fc0e7e13f6e91e236445f43a5937b9d7c67c63f2dfe195 | 60953 | 2a38d3dab649320e9480ef3b6b3a1824f3cdfd35de822594dabd81f34494a353 |
| 2026-w47-ru-zh-tw | 3975999 | cc348ad4ae16b6f3989b6d7c3966e7f543b658838d1ec3a71817793620ecb462 | 60855 | 948538470d3cbfb3b0110300daf89c382ce4f555e08567bd1b961c8fcff52e0e |

Rendered .md files + `pins.json` (full pins incl. edition dirs): this dir (`render_all.py`,
`write_all.py`, `pins.json`, `2026-w47-ru-*.md`).

## Lint (step c)

- `node lint.mjs --write`: OK
- `node lint.mjs --require-pdf`: RC=0 — `OK: 500 editions, index.json is current`
  (489 before + 11 = 500)
- No bundle-slug lint issues. No rollback needed.

## Commit (steps d–e)

- `git add` explicit paths only: `index.json` + 11 × 3 `issues/2026-w47/<slug>/` files = 34 files staged
- Commit SHA: **`c90f63136ab3557bd59dbe8a44632df28b674b13`**
- `git show --stat HEAD`: 34 files changed, 9910 insertions(+), 1 deletion(-)
- `git status --porcelain` after commit: back to the known 535 `??` lines, zero M/D entries
- `git ls-files issues/2026-w47/2026-w47-ru-*`: 33 files ✓
- `git ls-files issues/2026-w47`: 330 files (10 families × 33)
- **No push performed** (no `push_with_verify`, no `git push`, no `ls-remote`).
  Remote is still at the pt bundle commit; the ru bundle commit exists only locally.

## Cleanup (step f) — NOTHING deleted, all retained

Per-dir verification of all 85 ru-family scratch dirs under `hidden_files/w47/`
(ru-target dirs; `*-ru` dirs of other targets, e.g. `scratch-proof-en-ru1`,
`scratch-fix-es-ru2`, `scratch-delta-en-ru`, `scratch-fix-xru-*`, `scratch-sweep-xru-occl-*`,
`scratch-reproof8-w47-esru`, belong to their own families / cross-family sweeps and were not touched).

Scan: every one of the 85 dirs contains ≥1 audit-record `.md` and/or ≥1 unique `.py` script
(zero dirs with md=0 AND py=0). Verified: no ru-family audit file exists in the repo git index
(`git ls-files production/2026-w47 | grep -iE "PROOF-NOTE|GATE-LOG|FIX-LOG|D5-REPORT|FANOUT-REPORT|EDIT-LOG|GATE-REPORT|VERIFY-REPORT|REBUILD-LOG|CHECK-NOTE|SWEEP-LOG|KIT-SYNC" | grep -i ru`
returns nothing — the only two hits are es-ko / core-nl FIX-LOG.md files of other families).
Deleting any of these dirs would destroy the only copy of its audit record / unique script.
Per the task rule ("拿不准的目录留着并上报…审计记录一律保留上报，130 齐后再统一收割归档"),
all 85 are RETAINED, 0 MB freed (total 6.0G).

Retained list (size = du):

| dir | size | why retained (scratch-only content) |
|---|---|---|
| scratch-check-ru-zh-tw1 | 20K | CHECK-NOTE.md (audit record) |
| scratch-core-ru-morozko | 102M | REBUILD-LOG.md + freeze/occlusion probes |
| scratch-d5-rebuild-ru | 178M | D5-REPORT*.md + rebuild scripts |
| scratch-fanout-ru | 412M | FANOUT-REPORT-ru.md + tm_ru.py / tm-*.json |
| scratch-fix-core-ru1 | 135M | fix logs + textmd-fix1.md |
| scratch-fix-ru | 3.4M | FIX-LOG.md + round2 driver/scripts |
| scratch-fix-ru-d1 | 9.3M | FIX-NOTE.md + apply_ru.py / verify scripts |
| scratch-fix-ru-de1 | 92M | FIX-LOG.md + gate/fix scripts |
| scratch-fix-ru-en-kit | 128K | FIX-LOG.md + WEEKLY-KIT.md.before |
| scratch-fix-ru-en1 | 112M | FIX-LOG.md + GATE-LOG.md + verify scripts |
| scratch-fix-ru-en2 | 96M | unique title/ink scripts + pre/post snapshots |
| scratch-fix-ru-ko1 | 384K | unique scripts + .bak-prefixed / .NEW / .FIXED files |
| scratch-fix-ru-nl1 | 61M | unique gap/raster scripts + pre snapshots |
| scratch-fix-ru-nl2 | 36K | FIX-LOG.md + before/after snapshots |
| scratch-fix-ru-pt1 | 87M | unique measure/exp scripts + svg snapshots |
| scratch-fix-ru-pt2 | 252K | FIX-LOG.md + before/after snapshots |
| scratch-fix-ru-textmd-d6 | 1.2M | FIX-LOG.md + GATE-LOG.md + reexport scripts |
| scratch-fix2b-w47-ru | 368K | unique drivers + pre- textmd/svg snapshots |
| scratch-fix2c-w47-ru | 272K | FIX-LOG-2c.md + driver + pre snapshots |
| scratch-fix3-w47-ru | 556K | unique drivers + pre snapshots |
| scratch-fix4-w47-ru | 1.6M | unique drivers + pre snapshots |
| scratch-gatefix-u201c-ru | 204M | cross-family U+201C patch logs + unique patch scripts (spans ru + other targets; retained, not ru-target-only) |
| scratch-invest-ru-kicker | 14M | INVEST-NOTE.md + baseline/patched svg |
| scratch-proof-core-ru1 | 63M | gate logs + check scripts |
| scratch-proof-ru | 69M | PROOF-NOTE.md |
| scratch-proof-ru-de1 | 53M | PROOF-NOTE.md + GATE-LOG.md |
| scratch-proof-ru-de2 | 107M | PROOF-NOTE.md + GATE-LOG.md + gate scripts |
| scratch-proof-ru-en1 | 81M | unique gate scripts + keydiff/occlusion logs |
| scratch-proof-ru-en2 | 140M | PROOF-NOTE.md + GATE-LOG.md + verify scripts |
| scratch-proof-ru-en3 | 49M | unique verify scripts + occlusion logs |
| scratch-proof-ru-es1 | 47M | unique gate scripts + occlusion/p8 logs |
| scratch-proof-ru-es2 | 119M | unique gate scripts + occlusion/p8 logs |
| scratch-proof-ru-fr1 | 58M | unique gate scripts + crops |
| scratch-proof-ru-fr2 | 113M | PROOF-NOTE.md + GATE-LOG.md + gate scripts |
| scratch-proof-ru-it1 | 101M | unique gate scripts + occlusion/p8 logs |
| scratch-proof-ru-it2 | 115M | PROOF-NOTE.md + GATE-LOG.md + gate scripts |
| scratch-proof-ru-ja1 | 53M | unique gate scripts + occlusion/p8 logs |
| scratch-proof-ru-ja2 | 176M | PROOF-NOTE.md + GATE-LOG.md |
| scratch-proof-ru-ko1 | 185M | unique gate scripts + occlusion/p8/freeze logs |
| scratch-proof-ru-nl1 | 61M | unique gate scripts + occlusion/p8 logs |
| scratch-proof-ru-nl2 | 156M | unique gate scripts + occlusion/p8 logs |
| scratch-proof-ru-pt1 | 87M | unique gate scripts + crops |
| scratch-proof-ru-pt2 | 112M | unique gate scripts + freeze/occlusion logs |
| scratch-proof-ru-zh-tw1 | 79M | unique gate scripts + freeze/occlusion logs |
| scratch-refanout-ru | 182M | FANOUT-REPORT-ru.md + fanout scripts |
| scratch-reproof-ru-de1 | 152M | PROOF-NOTE.md + GATE-LOG.md + gate scripts |
| scratch-reproof-ru-en1 | 102M | unique gate scripts (adjudicate_ru.py etc.) |
| scratch-reproof-ru-en2 | 92M | unique gate scripts + snapshots |
| scratch-reproof-ru-es1 | 16K | PROOF-NOTE.md |
| scratch-reproof-ru-fr1 | 12K | PROOF-NOTE.md |
| scratch-reproof-ru-fr2 | 16K | PROOF-NOTE.md |
| scratch-reproof-ru-it1 | 12K | PROOF-NOTE.md |
| scratch-reproof-ru-ja1 | 20K | PROOF-NOTE.md |
| scratch-reproof-ru-ko1 | 140M | unique gate scripts + snapshots |
| scratch-reproof-ru-nl1 | 60M | unique gate scripts + freeze/p8 logs |
| scratch-reproof-ru-pt1 | 123M | unique gate scripts + freeze/p8 logs |
| scratch-reproof-ru-zh-tw1 | 87M | unique gate scripts + p8/freeze logs |
| scratch-reproof-ru-zh-tw2 | 8.0K | PROOF-NOTE.md |
| scratch-reproof-w47-ru | 20K | PROOF-NOTE.md |
| scratch-reproof2-w47-ru | 12M | p8 inventory logs (per-edition gate output) |
| scratch-reproof3-w47-ru | 2.7M | PROOF-NOTE-3.md + gate scripts |
| scratch-reproof4-w47-ru | 2.9M | PROOF-NOTE-4.md + gate scripts |
| scratch-reproof5-w47-ru | 3.0M | PROOF-NOTE-5.md + gate scripts |
| scratch-ru | 1.2M | adjudicate.py (unique script) + probe crops/occlusion |
| scratch-ru-en-proof2 | 41M | PROOF-NOTE.md + GATE-LOG.md + fullscan.py |
| scratch-ru-fix | 248K | FIX-NOTE.md |
| scratch-ru-kit-sync | 16K | KIT-SYNC.md |
| scratch-ru-ko-port-rebuild | 123M | PORT-REBUILD-SYNC-LOG.md + port scripts |
| scratch-ru-rebuild-C | 188M | REBUILD-LOG.md + census/gate scripts |
| scratch-ru-rebuild-it | 59M | census before/after snapshots + build logs |
| scratch-ru-rebuild-ja | 67M | census before/after snapshots + build logs |
| scratch-ru-rebuild-nl | 60M | census before/after snapshots + build logs |
| scratch-ru-rebuild-pt | 60M | census before/after snapshots + build logs |
| scratch-ru-rebuild-ru-de | 48M | census before/after snapshots + gap scripts |
| scratch-ru-rebuild-ru-en | 48M | REBUILD-LOG.md + census snapshots |
| scratch-ru-rebuild-ru-es | 112K | REBUILD-LOG.md + census snapshots |
| scratch-ru-rebuild-ru-fr | 60M | REBUILD-LOG.md + census snapshots |
| scratch-ru-rerun-R1 | 419M | census before logs + unique scripts |
| scratch-ru-rerun-R2 | 501M | REBUILD-LOG.md + driver logs + scripts |
| scratch-ru-tables-sweep | 12K | SWEEP-LOG.md |
| scratch-ru-textmd | 1.4M | unique verify/apply scripts + regen diffs |
| scratch-ru-textmd-apply | 80K | check_appendix9.py (unique script) + p8 jsons |
| scratch-ru-zh-tw-f1 | 380K | unique scripts + .before files + logs |
| scratch-verify-ru | 8.0K | VERIFY-REPORT.md |
| scratch-verify-ru-final | 20K | VERIFY-REPORT.md + disk-sha.txt |

Not ru-target, untouched (for the record): `scratch-proof-<other>-ru*`, `scratch-fix-<other>-ru*`,
`scratch-delta-en-ru`, `scratch-delta-nl-ru`, `scratch-gate-fr-ru-final`, `scratch-gate-pt-ru-final`,
`scratch-gatefix-it-ru`, `scratch-it-ru-spacing(2)`, `scratch-proof2-it-ru1`, `scratch-proof2-zh-tw-ru1`,
`scratch-fix-xru-heads`, `scratch-fix-xru-w47`, `scratch-sweep-xru-occl-1/2`, `scratch-reproof8-w47-esru`,
`scratch-webpdf-nl-ru-ja`, plus `probe-*.txt` files and `run-log.md` (not directories).
`scratch-run-build` / `scratch-runw-*` only match `*ru*` via the substring "run" — not ru family.
