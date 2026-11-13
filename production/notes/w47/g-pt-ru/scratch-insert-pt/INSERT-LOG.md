# INSERT-LOG — W47 pt bundle

- Worker: 恢复协调员 #6 派单，步骤 4，第九家（pt）
- Date: 2026-11-13
- Repo: `~/workspace/weekly-git`
- Start HEAD (verified): `797e8460c6f63bac034208d2848f8114534ce600` (nl bundle commit)
- Disk before: 98G used / 150G (df -h); after: 98G used — no scratch freed (see §Cleanup)
- Method: original `tools/insert.py` `render_md` + `resolve_bundle_dir` imported directly;
  `main_bundle` (c)–(e) reproduced, skipping only the clean-tree check (535 known `??`
  render-product lines must stay on disk, never committed) and the push.
- Commit message (verbatim, as main_bundle builds it): `Add 2026-w47-pt bundle (PT text · 11 natives)`

## Seed excerpt (step b)

No pt edition existed in `issues/2026-w47/`, so seed mode was required.

Precedent verified (W46): `issues/2026-w46/2026-w46-pt-en/2026-w46-pt-en.md` excerpt
equals exactly the first two complete sentences of the P1 headline body paragraph
in `production/2026-w46/core-pt/2026-w46-pt-zh-cn.text.md`:
"Domingo, 15 de novembro, é o segundo dia do Enem 2026 — e é também o feriado da
Proclamação da República. A prova e o feriado chegam no mesmo dia: de manhã, o país
acorda para a história; à tarde, mais de 5 milhões de estudantes fazem Ciências da
Natureza e Matemática."

W47 seed excerpt (same rule, from `production/2026-w47/core-pt/2026-w47-pt-zh-cn.text.md`
P1 headline body paragraph, first two sentences) — cross-checked verbatim against
`production/covers/2026-w47/cover.json` `stories.pt.excerpt` (identical):

> Sexta, 20 de novembro, é feriado nacional: o Dia Nacional de Zumbi e da Consciência Negra. A data lembra a morte de Zumbi dos Palmares, em 1695, líder do Quilombo dos Palmares.

- exercises: 150 (all 11 editions)
- pt-zh-cn edition dir resolved via `resolve_bundle_dir` core fallback: `production/2026-w47/core-pt`
- All other 10 natives resolved to `production/2026-w47/2026-w47-pt-<native>/`

## Render pins (step b — measured from the actual web PDFs / .text.md files)

| slug | web PDF bytes | web PDF SHA-256 | text bytes | text SHA-256 |
|---|---|---|---|---|
| 2026-w47-pt-de | 1063957 | 11a2581bb4d3cdfa3749c8110617f43c0111f7efdd6c1bce83b7d363359863ea | 37908 | 5bea955b4bb628060ea5e4449dc0514883ecacc3c18c011206b1fb976345883b |
| 2026-w47-pt-en | 1058709 | 71ebd11901ed216fdeb44cdd10443bc0f41c9815476f7390385f542bc55ccc2a | 37332 | 59a54ecfebab367e713f4dcce98370694e0e88cbd163883fa70cc3343fde18fc |
| 2026-w47-pt-es | 1058816 | f60aee6774f28fe688eda5c4f0fd32547d30d32711557558ae363334286d754d | 37468 | f23feb96f80a99b1b451e9aca33510e058c38f61608c9e6e300ccbb31913e1a0 |
| 2026-w47-pt-fr | 1059870 | 0b41560bc4b8aa894fda0d2a18de667c4da8b7c7a5d406736b2a521a7a962b7c | 37702 | 790267a7bfe5739c557e943a4a3ec1dabbe6a622a0e6bccb064f0df5c7f80542 |
| 2026-w47-pt-it | 1056189 | 89ec1f93ca908f5061b8497333eb4fe08a75b0604ccb87c9bd98d0f0693f817d | 37422 | d55da797bfe6eb2185c27a207e48d0395a3df98ecd26e26ecd227d5e4c5e93c5 |
| 2026-w47-pt-ja | 1433879 | a9b4a30929c18cbd949062d1cf79425eb0d1943363251a7f7fbb578da280862b | 37915 | 90dcdcca7821049a9af8735653d7059e4a111eeaae6dfebf1ea1467941ec9830 |
| 2026-w47-pt-ko | 1307288 | 797ad196553e64af5b9a992905dda169cd49ba776b945fe0d420aaf73f354744 | 37804 | 3eb35dfb9070565c1b168d3e79b8319c4867434b53e0819e8f77cd8ca467cb4c |
| 2026-w47-pt-nl | 1060458 | 0d7be4afdc71763420bf99b829998c1c4f9b70d01d6b9c51fb3bd72911712387 | 37571 | 34a38b8851359c1f9850dad2d10b418f2d65629d29ee959fd2878492d899eaca |
| 2026-w47-pt-ru | 1202092 | 15c0ddf67c2c2118f91d58c89e482b4183cd008bceb5d5ddf75db199a9421916 | 39736 | 87871659c0101a9d8c2f7bc415946653ea80257032332cda8b1208e6288184c8 |
| 2026-w47-pt-zh-cn | 1389823 | ca9f7722ecb261e023a2600cde21639bb57c507da29e51fd14522b4e8f29ed34 | 36886 | 352f509798a6cea00543885d7c64332c78e55d9f0e643c3f3c931d37127b13c5 |
| 2026-w47-pt-zh-tw | 1463493 | 2d0e80af74d7d33eaa1cc4e669b9b6471f004649a8d1440400a02db30554e85a | 36875 | 5cd5c7270e6a3dc0bfe2f5c0c644f782189bffff9df5be2d10d9e07fd49a2888 |

Rendered .md files + `pins.json` (full pins incl. edition dirs): this dir (`render_all.py`,
`write_all.py`, `pins.json`, `2026-w47-pt-*.md`).

## Lint (step c)

- `node lint.mjs --write`: OK
- `node lint.mjs --require-pdf`: RC=0 — `OK: 489 editions, index.json is current`
  (478 before + 11 = 489)
- No bundle-slug lint issues. No rollback needed.

## Commit (steps d–e)

- `git add` explicit paths only: `index.json` + 11 × 3 `issues/2026-w47/<slug>/` files = 34 files staged
- Commit SHA: **`7e8ce057812488a98156155048362b1b37fa114f`**
- `git show --stat HEAD`: 34 files changed, 6568 insertions(+), 1 deletion(-)
- `git status --porcelain` after commit: back to the known 535 `??` lines, zero M/D entries
- `git ls-files issues/2026-w47/2026-w47-pt-*`: 33 files ✓
- `git ls-files issues/2026-w47`: 297 files (9 families × 33)
- **No push performed** (no `push_with_verify`, no `git push`, no `ls-remote`).
  Remote is still at the nl bundle commit; the pt bundle commit exists only locally.

## Cleanup (step f) — NOTHING deleted, all retained

Per-dir verification of all 49 pt-family scratch dirs under
`hidden_files/w47/` (target pt only; `*-pt` dirs of other targets, e.g.
`scratch-proof-en-pt1`, `scratch-delta-en-pt`, `scratch-fix-ru-pt1`, belong to
their own families and were not touched):

Every one of the 49 dirs contains scratch-only audit records and/or unique
scripts that do NOT exist in the repo git index (verified:
`git ls-files production/2026-w47 | grep -iE "PROOF-NOTE|GATE-LOG|FIX-LOG|D5-REPORT|FANOUT-REPORT|EDIT-LOG|GATE-REPORT|VERIFY"`
returns no W47 pt audit files — only unrelated `verify.py` in de-* dirs).
Deleting any of these dirs would destroy the only copy of its audit record.
Per the task rule ("拿不准的目录留着并上报…审计记录一律保留上报，130 齐后再统一收割归档"),
all 49 are RETAINED, 0 MB freed.

Retained list (size = du, rounded):

| dir | size | why retained (scratch-only content) |
|---|---|---|
| scratch-proof-pt | 57M | PROOF-NOTES-PT.md |
| scratch-proof-pt2 | 53M | PROOF-NOTE.md + freeze/gates/occlusion logs |
| scratch-proof-pt-de1 | 53M | PROOF-NOTE.md, GATE-LOG.md, make_keycheck.py |
| scratch-proof-pt-de2 | 121M | PROOF-NOTE.md, GATE-LOG.md, boxtitle_ink.py + probes |
| scratch-proof-pt-en1 | 64M | PROOF-NOTE.md, GATE-LOG.md, check_final_proof.py |
| scratch-proof-pt-en2 | 170M | PROOF-NOTE.md, GATE-LOG.md, check_final_proof.py, classify_pt.py, creambox*.py |
| scratch-proof-pt-es1 | 37M | PROOF-NOTE.md, GATE-LOG.md, ink_line.py, ink_probe.py, make_keycheck.py |
| scratch-proof-pt-es2 | 105M | PROOF-NOTE.md, GATE-LOG.md, card_probe*.py, resp_compare*.py |
| scratch-proof-pt-fr1 | 27M | PROOF-NOTE.md, GATE-LOG.md, measure_ink.py |
| scratch-proof-pt-fr2 | 93M | PROOF-NOTE.md, GATE-LOG.md, check_s11_pt.py, measure_ink.py |
| scratch-proof-pt-it1 | 32M | PROOF-NOTE.md, GATE-LOG.md |
| scratch-proof-pt-it2 | 86M | PROOF-NOTE.md, GATE-LOG.md, boxtitle_ink.py, sweep_*.py |
| scratch-proof-pt-ja1 | 55M | PROOF-NOTE.md, GATE-LOG.md, hscan.py, ink.py |
| scratch-proof-pt-ko1 | 48M | PROOF-NOTE.md, GATE-LOG.md, ink_measure*.py, pixelscan.py |
| scratch-proof-pt-ko2 | 121M | PROOF-NOTE.md, GATE-LOG.md, qtable.md, keycheck-mine.py |
| scratch-proof-pt-nl1 | 34M | PROOF-NOTE.md, GATE-LOG.md, build_keycheck.py |
| scratch-proof-pt-ru1 | 27M | PROOF-NOTE.md, GATE-LOG.md, inkprobe.py |
| scratch-proof-pt-zh-tw1 | 159M | PROOF-NOTE.md, GATE-LOG.md, gloss_pixels.py, reg_dump.py, pixel-sweep.py |
| scratch-proof-core-pt1 | 39M | PROOF-NOTE.md, GATE-LOG.md, keycheck.py, pil_*.py |
| scratch-proof-core-pt2 | 47M | PROOF-NOTE.md, GATE-LOG.md, keycheck2.py, pil_re2.py |
| scratch-fix-pt | 76M | FIX-LOG.md |
| scratch-fix-pt-de1 | 76M | FIX-LOG.md, GATE-LOG.md, verify_ed_pt.py + probes |
| scratch-fix-pt-en1 | 78M | FIX-LOG.md, GATE-LOG.md, verify_ed-pt.py, old-textmd.md |
| scratch-fix-pt-es1 | 140M | FIX-LOG.md, GATE-LOG.md, d7_*.py, resp_compare_fix*.py |
| scratch-fix-pt-it1 | 74M | FIX-LOG.md, GATE-LOG.md, pixel_boxtitle_web.py, premeasure.py |
| scratch-fix-pt-ja1 | 78M | FIX-LOG.md, GATE-LOG.md, gates_pt.py, measure_topstrip.py |
| scratch-fix-pt-ko1 | 209M | FIX-LOG.md, GATE-LOG.md, *-mine.py, probe_wrap*.py, scan_lines*.py |
| scratch-fix-pt-ru2 | 90M | FIX-LOG-2.md, textmd-pre-backup.md |
| scratch-fix-pt-minor1 | 199M | FIX-LOG.md, make_textmd_pt.py, text-pre-zh-cn.md |
| scratch-d5-rebuild-pt | 285M | D5-REPORT-*.md (11) + RUN-LOG.md, diag*.py, textlayer.py |
| scratch-reproof-pt-de1 | 102M | PROOF-NOTE.md, GATE-LOG.md, verify_ed_pt.py, sweep_overflow.py |
| scratch-reproof-pt-en1 | 110M | PROOF-NOTE.md, GATE-LOG.md, verify_ed-pt.py, my_trueink.py |
| scratch-reproof-pt-es1 | 111M | PROOF-NOTE.md, GATE-LOG.md, d7_*.py, resp_compare_fix.py |
| scratch-reproof-pt-it1 | 86M | PROOF-NOTE.md, GATE-LOG.md, nota_ink.py, text_coverage*.py |
| scratch-reproof-pt-ja1 | 109M | PROOF-NOTE.md, GATE-LOG.md, check_s11_ptja.py, dcheck.py, pixcheck.py |
| scratch-reproof-pt-ja2 | 74M | PROOF-NOTE.md, GATE-LOG.md |
| scratch-reproof-pt-ko1 | 134M | PROOF-NOTE.md, GATE-LOG.md, verify_ed_ptko.py, xcheck150.py, probe*.py |
| scratch-reproof-pt-nl1 | 9M | PROOF-NOTE.md, GATE-LOG.md, build_keycheck.py, ink_measure.py, pixel_measure.py |
| scratch-reproof-pt-ru1 | 72M | PROOF-NOTE.md, GATE-LOG.md, check_final_ptru.py, keycheck_ptru.py, sweep_ptru.py |
| scratch-reproof-w47-pt | 0M | PROOF-NOTE.md + toolout logs |
| scratch-reproof2-w47-pt | 1M | PROOF-NOTE-2.md, census.py, p8_vs_textmd.py |
| scratch-kit-edit-pt | 0M | EDIT-LOG.md (KIT edit audit record — explicitly retain per task) |
| scratch-fanout-pt | 55M | FANOUT-REPORT-pt.md, README-BLOCKER.md, build_one.sh, check_final.py |
| scratch-refanout-pt | 110M | FANOUT-REPORT-pt.md, apply_fixes.py, boxtitle_core.py, creambox*.py, classify_pt.py |
| scratch-pt | 78M | round3-check.py, freeze logs, p2/p6/p7 chart PNGs |
| scratch-pt-en-fix1 | 38M | FIX-LOG.md, GATE-LOG.md, old-textmd.md |
| scratch-pt-fix2 | 49M | round4-log.md, round4-check.py |
| scratch-pt-furniture-backwrite | 0M | NOTE.md |
| scratch-gate-pt-ru-final | 3M | GATE-REPORT.md + gate-run/identity/inkprobe logs |

Total retained: 49 dirs, ~3.9G. Deleted: none (0 MB freed).
Also retained: this dir `scratch-insert-pt` (holds this log + pins.json + rendered .md),
same as the other eight families' `scratch-insert-*` dirs.
Not touched: other families' `*-pt` dirs (en-pt, de-pt, …), `probe-*.txt`, `Reports-preinsert/`.

Note for the 130-complete harvest: the audit records above (PROOF-NOTE/GATE-LOG/FIX-LOG/
D5-REPORT/FANOUT-REPORT/EDIT-LOG/GATE-REPORT) exist only in these scratch dirs; harvest
them into the repo (e.g. `production/notes/`) before any future deletion. The `.py`
build-copies inside are duplicates of tracked `production/2026-w47/` code and the
rendered PDFs/PNGs are reproducible from it — only the audit .md/.log files and the
top-level unique probe/verify scripts are irreplaceable.
