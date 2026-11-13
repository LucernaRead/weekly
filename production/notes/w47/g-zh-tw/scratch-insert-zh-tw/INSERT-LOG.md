# INSERT-LOG — W47 zh-tw bundle (last family, 130/130)

- Worker: W47 zh-tw insert (recovery coordinator #6, step 4, 12th/last family)
- Date: 2026-11-13 (Fri) ~07:25–08:00 EST
- Repo: ~/workspace/weekly-git; pre-insert HEAD verified: `26466e69` (zh-cn bundle)
- Disk before: 98G used / 52G avail (150G); after: 98G used / 52G avail — no change (nothing deleted, see §5)
- Method: imported tools/insert.py, reproduced main_bundle (b)–(e) with original render_md; skipped only the clean-tree check (535 known `??` render products must stay on disk, never committed) and all pushes. `git add` explicit paths only; no `git add -A`, no reset/stash, no push/ls-remote.

## Seed excerpt (first-in-week target, no in-week sibling)

- Precedent checked (W46): `issues/2026-w46/2026-w46-zh-tw-en/2026-w46-zh-tw-en.md` excerpt = core-zh-tw P1 headline paragraph, first two complete sentences (joined with a space after 。). Verified against W46 core-zh-tw text.md P1.
- W47 core-zh-tw P1 first two sentences: 「味全龍拿下隊史第6座總冠軍，封王遊行訂在本週日（11月22日）下午2點。封王遊行從天母棒球場出發，終點是台北大巨蛋松菸大道。」
- W47 cover.json `stories.zh-tw.excerpt` is exactly these two sentences (same wording, no space after 。). Substantively identical → adopted.
- Seed excerpt used (W46 spacing convention, space after 。):
  > 味全龍拿下隊史第6座總冠軍，封王遊行訂在本週日（11月22日）下午2點。 封王遊行從天母棒球場出發，終點是台北大巨蛋松菸大道。
- exercises=150, publishedAt=2026-11-16, vol=4, pages=8 (all 10 editions).

## Rendered editions (step b — all 10 fail-fast, sibling=(seed))

| slug | web PDF bytes | web PDF SHA-256 | text.md bytes | text.md SHA-256 | edition dir |
|---|---|---|---|---|---|
| 2026-w47-zh-tw-de | 1903630 | `a67ffad9183562624bbef7deb112b85d33c1d9717fca95a9c5bcaed7ecf4a838` | 51820 | `8187f61963262e57627f2ff371e5c7ddb8d5b974fc44763ca4555eb57c1ab83f` | `production/2026-w47/2026-w47-zh-tw-de` |
| 2026-w47-zh-tw-en | 1898131 | `45d0760038014de266aaab5390898ae33f2110a6a14f98aeae8131301ddaba06` | 49804 | `9b8b5295ddd822afc020a8c439a55e35cb5259b5d18afa25f4e4d4cacd376905` | `production/2026-w47/core-zh-tw` |
| 2026-w47-zh-tw-es | 1902298 | `f8c0086a1a66cad8b084bb142b9cf420ff468baf53f8d2d7985ffbcf460d9679` | 52252 | `e8a36b7996f61c812d04d916b30171371c70b0dddf9b01a648fb6067fab97b70` | `production/2026-w47/2026-w47-zh-tw-es` |
| 2026-w47-zh-tw-fr | 1899287 | `233658513953a1b4b3f5aea84fa9f42b230326c41e60f8edc440524e958e9038` | 52476 | `a2df8892d632ab081dd05b05c4df62be33a5ed91a3749cca27ed02db7e3c3fcf` | `production/2026-w47/2026-w47-zh-tw-fr` |
| 2026-w47-zh-tw-it | 1895728 | `3ed32974c27d4cd6271a0d2788f76e7df8f7160f1f2ee13dcde867f56eb6a212` | 51691 | `788ed6f6600cf0ae84b2e03ad466f420c19ac095bdbb3ab471152132692f6f24` | `production/2026-w47/2026-w47-zh-tw-it` |
| 2026-w47-zh-tw-ja | 2447388 | `660f93940fe899ab40bc82def399a0cb1b85a0d2d161826c42e97f184fd29b9e` | 53759 | `6e5b4b81e13159fbcf37b0dc22668f056f69775c021fc7428a67f50fe2c42c51` | `production/2026-w47/2026-w47-zh-tw-ja` |
| 2026-w47-zh-tw-ko | 2134244 | `7419fee9eedf78144254784ef343de449782d7b7e86880b6dfdaa65dc056c0fc` | 53922 | `0215bc2cf6a69c7cbc9fb999f595b4d2539e1087a413653a61f8cff3192b681b` | `production/2026-w47/2026-w47-zh-tw-ko` |
| 2026-w47-zh-tw-nl | 1898763 | `d28897aea142e157ac3710ad5eb923642097f362c5d9de1bdc77cb30b1284550` | 50602 | `487127dd7d72bbe9bc803b921b65d919b7fc53fedf3a70920579c05ec23a57a0` | `production/2026-w47/2026-w47-zh-tw-nl` |
| 2026-w47-zh-tw-pt | 1907201 | `90caf45fab413515c62b35f35fc58fecd1ec56eca056e82d527b878e0f81d784` | 51498 | `542bfae121e5e50a9d68fdddeb3d5b55a1b43d9a4b1f8b4630c4a5b086f46c37` | `production/2026-w47/2026-w47-zh-tw-pt` |
| 2026-w47-zh-tw-ru | 1997666 | `04606730a740e008fe427e69859c1e90a911f2872ec6079b8df75a135421afa1` | 62498 | `ea9c1514df967cd8e8a324d2037c6c15460a33b451318bc07b09d7e764a81c32` | `production/2026-w47/2026-w47-zh-tw-ru` |

Notes: zh-tw-en resolved via core-zh-tw fallback (`resolve_bundle_dir`, `core-zh-tw/2026-w47-zh-tw-en.text.md` present). Other 9 via `production/2026-w47/<slug>/`. `bundle_natives(zh-tw)` = en, de, fr, es, it, pt, nl, ru, ja, ko (10; zh-cn excluded).

## Write + lint (step c)

- Wrote 10 × {`.md`, `.text.md`, `.pdf`} under `issues/2026-w47/`; `node lint.mjs --write` RC=0 → "index.json written: 520 editions".
- `node lint.mjs --require-pdf` RC=0 → "OK: 520 editions, index.json is current" (full output in `require-pdf.txt`).
- No rollback needed.

## Commit (step d, NO push — step e)

- Message: `Add 2026-w47-zh-tw bundle (ZH-TW text · 10 natives)`
- Commit SHA: `75c8c097477d82b37b07b383a424c3ae2ccfc6ca`
- `git show --stat HEAD`: 31 files (30 issues/ files + index.json), 61687 insertions(+), 1 deletion(-).
- Post-commit `git status --porcelain`: 535 lines, all `??`, zero other entries (same known render products as before).
- `git ls-files issues/2026-w47/2026-w47-zh-tw-*`: 30 files in index; `git ls-files issues/2026-w47`: 390 files = 130 editions × 3 → **W47 is 130/130 locally** (index.json 520 editions total).
- No push performed: no `push_with_verify`, no `git push`, no `ls-remote`. Remote still at zh-cn bundle until the coordinator pushes.

## Scratch cleanup (step f)

Rule applied per directory: delete only if every file is either byte-identical to a git-index blob or a reproducible render/log; keep any directory holding sole-copy audit records or sole-copy scripts (to be harvested into the repo, e.g. `production/notes/`, after 130/130).

Verification performed (evidence in `scratch-audit.json`, `scratch-classify.json`, `unique-scripts.json`, `novel-top-scripts.json`):
- Enumerated 80 zh-tw scratch directories under `hidden_files/w47/` (excluding this `scratch-insert-zh-tw/` workdir), total 4,957 MB.
- Repo `production/notes/` holds only 7 files, none zh-tw: no audit record has been harvested yet.
- Top-level audit .md files (PROOF-NOTE / GATE-LOG / FIX-LOG / VERIFY-REPORT / EDIT-LOG / FANOUT-REPORT / DELTA-NOTE / RUN-LOG / CHECK-NOTE / KIT-SYNC …): 160 files, **0 byte-identical to any tracked blob** (checked against all 16,630 tracked blobs). 79/80 dirs hold ≥1 such sole-copy record.
- The remaining dir, `scratch-zh-tw` (373.7 MB), holds sole-copy scripts `punct_dryrun.py` / `punct_apply.py` plus decision/search JSONs (`picked.json`, `hk-picked.json`, `*-search.json`, `occlusion*.json`) — keep per the unique-script rule. Its build-copy snapshots are stale variants of repo-tracked production code (verified by diff: repo `core-zh-tw/content12.py` is newer/final), but the dir cannot be deleted whole without destroying the sole-copy scripts.
- Build-copy / freeze / tmp/fakehome snapshots elsewhere are likewise stale variants of repo-tracked production code, but each of those dirs also holds a sole-copy audit .md, so no dir qualifies for whole-directory deletion.

### Deleted: (none)

### Kept: all 80 directories (4,957 MB) — delete 0 MB, disk unchanged at 98G used

- `scratch-check-ru-zh-tw1` — 0.0 MB, 2 files — KEEP: audit .md: CHECK-NOTE.md
- `scratch-d5-zh-tw` — 262.2 MB, 978 files — KEEP: audit .md: RUN-LOG.md; sole-copy script/json: stage2_gates.sh, stage0_baseline.sh, stage1_build_gates.sh…
- `scratch-delta-en-zh-tw` — 133.1 MB, 174 files — KEEP: audit .md: DELTA-NOTE.md; sole-copy script/json: dump_reg_delta.py, make_textmd_delta.py, s2t_check.py…
- `scratch-delta-nl-zh-tw` — 42.4 MB, 97 files — KEEP: audit .md: DELTA-LOG.md, freeze-core/build-copy/FIX-LOG.md; sole-copy script/json: orphan_sweep_pre.py, dump_reg_delta.py, check_creambox_delta.py…
- `scratch-fanout-zh-tw` — 35.4 MB, 634 files — KEEP: audit .md: 00-BLOCKED-disk-quota.md, 01-BLOCKED-disk-quota-again.md, FANOUT-REPORT-zh-tw.md…; sole-copy script/json: p8-keys-de.json, tmp/run-before/tables.py, tmp/run-after/tables.py…
- `scratch-fix-core-zh-tw2` — 33.8 MB, 69 files — KEEP: audit .md: FIX-LOG.md, GATE-LOG.md
- `scratch-fix-core-zh-tw3` — 33.9 MB, 72 files — KEEP: audit .md: FIX-LOG.md, GATE-LOG.md
- `scratch-fix-core-zh-tw4` — 34.1 MB, 81 files — KEEP: audit .md: text-md-before.md, WEEKLY-KIT-before.md, FIX-LOG.md…; sole-copy script/json: content7.py, content12.py
- `scratch-fix-core-zh-tw5` — 34.1 MB, 81 files — KEEP: audit .md: text-md-before.md, WEEKLY-KIT-before.md, FIX-LOG.md; sole-copy script/json: creambox.py, boxtitle.py, content34-before.py
- `scratch-fix-de-zh-tw-toolbox` — 2.6 MB, 55 files — KEEP: audit .md: FIX-LOG.md, GATE-LOG.md; sole-copy script/json: measure.py, get_gloss.py, d2scan-zh-tw.py
- `scratch-fix-en-zh-tw` — 0.0 MB, 8 files — KEEP: audit .md: FIX-NOTE.md; sole-copy script/json: check_s2t.py, fix_abstract.py
- `scratch-fix-fr-zh-tw1` — 46.9 MB, 89 files — KEEP: audit .md: FIX-LOG.md; sole-copy script/json: d3-verify-fix1.py, gates-fix1.py, check_extra-fix1.py…
- `scratch-fix-ja-zh-tw2` — 0.0 MB, 20 files — KEEP: audit .md: FIX-LOG.md, GATE-LOG.md; sole-copy script/json: key-compare-fix2.py
- `scratch-fix-zh-tw` — 290.5 MB, 1019 files — KEEP: audit .md: FIX-LOG.md, logs/core-zh-tw/textmd-fresh-post.md, logs/core-zh-tw/textmd-fresh-pre.md…; sole-copy script/json: fix_build_gates.sh, run_all.sh, run_rest.sh…
- `scratch-fix-zh-tw-core1` — 33.8 MB, 64 files — KEEP: audit .md: FIX-LOG.md, GATE-LOG.md
- `scratch-fix-zh-tw-fr1` — 0.1 MB, 5 files — KEEP: audit .md: FIX-LOG.md, GATE-LOG.md
- `scratch-fix-zh-tw-it1` — 0.3 MB, 14 files — KEEP: audit .md: FIX-LOG.md, GATE-LOG.md
- `scratch-fix-zh-tw-ja-time` — 286.7 MB, 363 files — KEEP: audit .md: FIX-LOG.md
- `scratch-fix-zh-tw-ja1` — 0.7 MB, 20 files — KEEP: audit .md: FIX-LOG.md
- `scratch-fix-zh-tw-ko1` — 70.5 MB, 150 files — KEEP: audit .md: FIX-LOG.md, GATE-LOG.md; sole-copy script/json: gates.py, keycheck.py, gates/ko-fix1/gates.json
- `scratch-fix-zh-tw-ko2` — 128.9 MB, 228 files — KEEP: audit .md: FIX-LOG.md, GATE-LOG.md; sole-copy script/json: gates.py, keycheck.py, work/transform.py…
- `scratch-fix-zh-tw-ru-kit` — 0.0 MB, 1 files — KEEP: audit .md: FIX-NOTE.md
- `scratch-fix-zh-tw-ru1` — 0.8 MB, 24 files — KEEP: audit .md: FIX-LOG.md, GATE-LOG.md
- `scratch-ja-zh-tw-fix1` — 0.0 MB, 20 files — KEEP: audit .md: FIX-LOG.md, GATE-LOG.md
- `scratch-kit-edit-zh-tw` — 0.0 MB, 1 files — KEEP: audit .md: EDIT-LOG.md
- `scratch-proof-core-zh-tw-reproof` — 0.2 MB, 15 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md
- `scratch-proof-de-zh-tw2` — 20.9 MB, 71 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: gates/p8extract.json, gates/freeze-diff.json, gates/spots-p8.json…
- `scratch-proof-en-zh-tw` — 104.7 MB, 107 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: occlusion.json, measure3.py
- `scratch-proof-en-zh-tw1` — 66.1 MB, 76 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: freeze.json, freeze-diff.json, measure3.py…
- `scratch-proof-en-zh-tw2` — 131.6 MB, 136 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: p8-extract.json, keycheck.py, freeze-diff.json…
- `scratch-proof-es-zh-tw1` — 20.3 MB, 39 files — KEEP: audit .md: PROOF-NOTE.md; sole-copy script/json: keys137.py, svgtext.py, freeze-diff.json…
- `scratch-proof-es-zh-tw2` — 78.3 MB, 136 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: scan_cjk.py
- `scratch-proof-fr-zh-tw1` — 17.6 MB, 42 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: freeze-diff.json, classify_cjk.py, cjk-added-classification.json…
- `scratch-proof-fr-zh-tw2` — 17.1 MB, 47 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: proof_gates.py, check_extra.py, verify_ed_fr.py…
- `scratch-proof-it-zh-tw1` — 51.9 MB, 90 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: freeze-diff.json, sweep.py, sweep2.py…
- `scratch-proof-ja-zh-tw1` — 4.0 MB, 42 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md, freeze-proof1/build-copy/EDITION-RECORD.md; sole-copy script/json: freeze-diff-proof1.json
- `scratch-proof-ja-zh-tw2` — 0.4 MB, 25 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: work/checks1.py, work/checks2.py, work/checks3.py…
- `scratch-proof-ko-zh-tw` — 30.0 MB, 91 files — KEEP: audit .md: textmd-proof1.md, PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: freeze-diff-proof1.json, trace-freeze-diff-proof1.py, occlusion-proof1.json…
- `scratch-proof-nl-zh-tw1` — 112.2 MB, 152 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md, freeze-core-proof1/build-copy/FIX-LOG.md; sole-copy script/json: occlusion.json, freeze-diff.json, measure2.py…
- `scratch-proof-pt-zh-tw1` — 159.2 MB, 228 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md, round1-first-edition/PROOF-NOTE.md…; sole-copy script/json: inkprobe.json, inkprobe-core.json, gloss_probe.py…
- `scratch-proof-ru-zh-tw1` — 78.1 MB, 115 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: freeze-diff.json, occlusion.json, occlusion-core.json…
- `scratch-proof-zh-tw` — 43.3 MB, 66 files — KEEP: audit .md: PROOF-NOTE.md
- `scratch-proof-zh-tw-de1` — 78.6 MB, 146 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md, text-export-rerun.md…; sole-copy script/json: keycheck-150.json
- `scratch-proof-zh-tw-es1` — 67.8 MB, 108 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md, archive-pre-rebuild/PROOF-NOTE.md…; sole-copy script/json: gates-proof.py, keycheck.py, keycheck-150.json…
- `scratch-proof-zh-tw-fr1` — 43.7 MB, 114 files — KEEP: audit .md: PROOF-NOTE-old-build-0841.md, GATE-LOG-old-build-0841.md, PROOF-NOTE.md…; sole-copy script/json: keycheck150.py, keycheck-150.json, work/p8-extract.json…
- `scratch-proof-zh-tw-it1` — 78.1 MB, 166 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md, prev-proof1-old-build/PROOF-NOTE.md…; sole-copy script/json: d2scan-core.py, d2scan-it.py, gates-proof1.py…
- `scratch-proof-zh-tw-ja1` — 41.2 MB, 103 files — KEEP: audit .md: PROOF-NOTE-old-pre-refanout.md, GATE-LOG-old-pre-refanout.md, PROOF-NOTE.md…; sole-copy script/json: gates-ja.py, keycheck-raw.json, keycheck-150.json…
- `scratch-proof-zh-tw-ko1` — 70.8 MB, 145 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md, proof1-old-build/PROOF-NOTE.md…; sole-copy script/json: keycheck.py, proof1-old-build/gates/freeze-diff.json, gates/freeze-diff.json
- `scratch-proof-zh-tw-ko2` — 84.2 MB, 151 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: keycheck.py, gates/freeze-diff.json
- `scratch-proof-zh-tw-nl1` — 114.0 MB, 195 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md, proof1-old-build/PROOF-NOTE.md…; sole-copy script/json: gates.py, keycheck.py, keycheck-150.json…
- `scratch-proof-zh-tw-pt1` — 43.7 MB, 95 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md, PROOF-NOTE-old-pre-refanout.md…; sole-copy script/json: gates-pt.py, keycheck-raw.json, keycheck-150.json…
- `scratch-proof-zh-tw-ru1` — 109.6 MB, 214 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md, archive-old-edition/PROOF-NOTE.md…; sole-copy script/json: gates-proof1.py, keycheck-150.json, gates/freeze-diff.json…
- `scratch-proof-zh-tw2` — 8.8 MB, 13 files — KEEP: audit .md: PROOF-NOTE-2.md; sole-copy script/json: work/freeze.json
- `scratch-proof2-it-zh-tw1` — 96.8 MB, 148 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: freeze-baseline.json, sweep.py, sweep2.py…
- `scratch-proof2-zh-tw-de1` — 112.9 MB, 192 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md, out/text-export-rerun.md; sole-copy script/json: gates-proof2.py, keycheck.py, geometry.py…
- `scratch-proof2-zh-tw-es1` — 39.8 MB, 91 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: gates.py, gates/es-proof2/gates.json, gates/es-proof2/freeze-diff.json
- `scratch-proof2-zh-tw-fr1` — 73.9 MB, 136 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: keycheck150.py, gates-proof2.py, keycheck-150.json…
- `scratch-proof2-zh-tw-it1` — 71.0 MB, 143 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: gates-driver.py, gates/freeze-diff.json, gates/it-proof2/gates.json
- `scratch-proof2-zh-tw-ja1` — 103.4 MB, 192 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: creambox_scan.py, out/p8-extract.json, out/creambox.json…
- `scratch-proof2-zh-tw-ko1` — 0.0 MB, 3 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md
- `scratch-proof2-zh-tw-ko2` — 40.8 MB, 102 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: gates.py, keycheck.py, gates/ko-proof2/gates.json
- `scratch-proof2-zh-tw-nl1` — 80.7 MB, 161 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: run-copy/build/content12.py, run-copy/build/content34.py, run-copy/build/content56.py…
- `scratch-proof2-zh-tw-pt1` — 40.1 MB, 94 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: gates.py, gates/pt-proof2/gates.json, gates/pt-proof2/freeze-diff.json…
- `scratch-proof2-zh-tw-ru1` — 32.0 MB, 107 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: gates.py, gates/ru-proof2/gates.json
- `scratch-refanout-zh-tw` — 236.9 MB, 1143 files — KEEP: audit .md: FANOUT-REPORT-zh-tw.md; sole-copy script/json: audit-tables.py, patch-tables-d1.py, backup/2026-w47-zh-tw-de/content12.py…
- `scratch-rekey-zh-tw-memory` — 0.0 MB, 1 files — KEEP: audit .md: FIX-LOG.md
- `scratch-reproof-core-zh-tw2` — 37.5 MB, 86 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: analyze.py
- `scratch-reproof-core-zh-tw3` — 34.2 MB, 74 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md
- `scratch-reproof-fr-zh-tw1` — 108.0 MB, 147 files — KEEP: audit .md: GATE-LOG.md, PROOF-NOTE.md; sole-copy script/json: check_extra.py, spill_sweep.py, proof_gates.py…
- `scratch-reproof-it2-zh-tw` — 112.6 MB, 148 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: sweep.py, sweep2.py, rerun/content12.py…
- `scratch-reproof-ru-zh-tw1` — 86.1 MB, 202 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: occlusion.json, adjudicate.py, adjudication.json…
- `scratch-reproof-ru-zh-tw2` — 0.0 MB, 1 files — KEEP: audit .md: PROOF-NOTE.md
- `scratch-reproof-w47-zh-tw` — 0.7 MB, 97 files — KEEP: audit .md: PROOF-NOTE.md
- `scratch-reproof-zh-tw-ko2` — 83.0 MB, 153 files — KEEP: audit .md: PROOF-NOTE.md, GATE-LOG.md; sole-copy script/json: gates.py, keycheck.py, gates/freeze-diff.json…
- `scratch-reproof2-w47-zh-tw` — 2.2 MB, 221 files — KEEP: audit .md: PROOF-NOTE-2.md; sole-copy script/json: reproof2_gates.sh, gates/core-zh-tw/occlusion.json, gates/core-zh-tw/core-zh-tw.json…
- `scratch-ru-zh-tw-f1` — 0.3 MB, 14 files — KEEP: audit .md: FIX-LOG.md; sole-copy script/json: freeze-diff.json
- `scratch-verify-zh-tw` — 8.6 MB, 27 files — KEEP: audit .md: VERIFY-REPORT.md; sole-copy script/json: run_gates_ru.sh, gates/zh-tw-ru/2026-w47-zh-tw-ru.json, gates/zh-tw-ru/census.json
- `scratch-zh-tw` — 373.7 MB, 4904 files — KEEP: audit .md: measure-venv/lib/python3.12/site-packages/numpy/random/LICENSE.md, measure-venv/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md, measure-venv/lib/python3.12/site-packages/numpy-2.5.4.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md…; sole-copy script/json: snow-search.json, jazz-search.json, moon-search.json…
- `scratch-zh-tw-fix` — 34.5 MB, 98 files — KEEP: audit .md: FIX-LOG.md; sole-copy script/json: occlusion13.json, build12-src-backup/content12.py, build12-src-backup/content34.py…
- `scratch-zh-tw-kit-sync` — 0.0 MB, 4 files — KEEP: audit .md: KIT-SYNC.md, KIT-SYNC-2.md

Probe files (`probe-*zh-tw*.txt`, coordinator logs, KB-size) left untouched — not scratch directories.

## Files in this workdir

- `render_bundle.py` — insert driver (import insert.py, reproduce main_bundle b–e, no push)
- `rendered.json` — per-edition pins (PDF/text bytes + SHA, edition dir, sibling)
- `require-pdf.txt` — full lint --require-pdf output (RC=0)
- `scratch-audit.json` / `scratch-classify.json` / `unique-scripts.json` / `novel-top-scripts.json` — cleanup evidence
- `INSERT-LOG.md` — this file
