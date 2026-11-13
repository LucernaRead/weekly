# DELTA-NOTE — 2026-W47 en-es · Q73 speak → up (core-en fix2 sync)

- Edition: `production/2026-w47/2026-w47-en-es/` (only this edition touched; no commit/push — coordinator handles git)
- Scratch (all logs/evidence): `hidden_files/w47/scratch-delta-en-es/`
- Date: 11 Nov 2026. Fix: core-en fix2, re-proof (a) passed.
- Scope note: the ONLY source change is `content56.py:49`, Q73 key `"speak"` → `"up"`. Stem `Speak ___: tell a teacher.` and note `speak up = hablar sin miedo` untouched. No map/translation file, no ABSTRACT.txt, no other source line touched. Core-en read-only (verified `content56.py:49` = `up`; `registry.json[72].key` = `up`).

## 0. Pre-change verification (all matched before any edit — else stop)

| Item | Pre-change SHA-256 | Size | Source |
|---|---|---|---|
| Print `The-Lucerna-VOL4-en-es.pdf` | `6341e239942338c547cfff31d96b4d6b0ad5b4ad811164380995959ea210b4a5` | 29,331,231 B | proof1 PROOF-NOTE, `scratch-proof-en-es1/` |
| Web `The-Lucerna-VOL4-en-es.web.pdf` | `73356781d8c02970f18e592ef60189891db128eb38cabb04442e1919ee725b97` | 2,414,448 B | proof1 PROOF-NOTE |
| `2026-w47-en-es.text.md` | `2539179917d985e6da78c36be288946865af6b8aa8599c3e532e44e262921e2d` | 54,388 B | proof1 PROOF-NOTE |
| Registry Q73 | `{'n': 73, 'page': 5, 'level': 'A2', 'type': 'Completar frases', 'key': 'speak', 'note': 'speak up = hablar sin miedo'}` | — | `registry.json[72]` |
| text.md line 1151 | `73. [A2] Completar frases — speak (speak up = hablar sin miedo)` | — | `2026-w47-en-es.text.md` |
| P8 printed key | `73. speak` (pdftotext p8; proof1 `p8-extract.json` `"73": "speak"`) | — | print PDF p8 |

Probes before work: `/dev/null` present, `git hash-object -w` OK, scratch write OK (`probe.txt`).

## 1. Post-change SHAs

| Item | Post-change SHA-256 | Size |
|---|---|---|
| Print `The-Lucerna-VOL4-en-es.pdf` | `6a249cc98f0dea9aa24d6b0af1db9480d9b030164f6ad083e4ff4f01249a70cb` | 29,331,230 B (−1) |
| Web `The-Lucerna-VOL4-en-es.web.pdf` | `2bc163a375007387e0e09c0ef2395459688dd2d19aea2f6946ced68c5c1eb79c` | 2,414,439 B (−9) |
| `2026-w47-en-es.text.md` | `314b32a3c3f236bec94ad6f1426664eb180cc8f96053cc886beed3eaacf217ca` | 54,385 B (−3) |

## 2. Diff evidence (verbatim; full files: `registry.diff`, `text.diff`)

Registry diff — exactly 1 line:
```
583c583
<   "key": "speak",
---
>   "key": "up",
```

text.md diff — exactly 1 line:
```
1151c1151
< 73. [A2] Completar frases — speak (speak up = hablar sin miedo)
---
> 73. [A2] Completar frases — up (speak up = hablar sin miedo)
```

## 3. Q73 four-source consistency (all `up` after rebuild)

| Source | Evidence |
|---|---|
| registry.json[72] | `key: 'up'`, `note: 'speak up = hablar sin miedo'` |
| text.md answer line 1151 | `73. [A2] Completar frases — up (speak up = hablar sin miedo)` |
| P8 printed key | `p8-extract.json` `"73": "up"`; print-PDF p8 text `73. up`; P8 render shows `73. up` in ANSWERS — Página 5 — |
| P5 stem + `to speak up` gloss | P5 SVG + render: `Speak ___: tell a teacher.` (Q73, A2 Completa); Nota box `to speak up = hablar sin miedo`; box title `SPEAK UP　Alza la voz`; match set `75. to speak up`; Q79 `Children (speak) up this week.` — all coherent with key `up` |

Cross-check vs core: registry keys vs core-en registry differ ONLY in the 5 known reader-language keys (137–140, 150). Q73 now `up` = core `up`. (`q73-four-source.log`)

## 4. Rebuild log

- `run.py` rc=0 (`run.log`): TOTAL exercises 150, MODEL words 82, 0 OVERFLOW / TOO WIDE, all flows end within bottom (P8-keys y=2443/bottom 2560).
- `render.py` rc=0 (`render.log`): 8 cards + print PDF 29,331,230 B, 8 pages, 1462.5 × 2025 pts.
- `dump_reg.py` rc=0 (`dump_reg.log`): registry 150 (by page 1:10, 2:17, 3:18, 4:18, 5:18, 6:18, 7:12, 8:39); copied scratch output → edition `registry.json`.
- `make_textmd_w47.py` rc=0 (`make_textmd.log`): stub registry 150 = real registry 150; wrote text.md 54,385 B.
- `webpdf.py` rc=0 (`webpdf.log`): wrote web PDF 2,414,439 B, 49,552 text bytes (< 7 MB).

## 5. Gate table (all re-run fresh; full log `gates-run1.log`)

| Gate | Result |
|---|---|
| run.py | rc=0, TOTAL 150, MODEL 82, 0 overflow, all flows within bottom |
| occlusion (REAL audit, no `--selftest`) | rc=0, **0 flags** (edition 0, core 0, NEW vs core 0) — `occlusion.log` / `occlusion.json` |
| p8 extract (core + edition) | noted set 60/150 each, identical sets (parse: joined) |
| p8 compare | **CLEAN**, missing=[] extra_count=0 uncertain=[]; keydiff=[137, 138, 139, 140, 150] (expected reader-language keys) — `p8-compare.json` read directly |
| keycheck | extract keys 150, registry 150, missing none; key mismatches p8-vs-registry: only #150 short-label exception (known); text.md 150 answer lines, 1–150 continuous, 0 mismatches — `keycheck.log` |
| freeze baseline (edition rebuild in copy) | **8/8 SVGs byte-identical** — `freeze.log` |
| freeze baseline (core-en rebuild in copy, read-only) | **8/8 SVGs byte-identical**; core integrity: shipped core SVGs unchanged — `freeze-core.log` |
| freeze diff vs core | TOTAL added CJK 9, all U+3000 — `freeze-diff.log` / `freeze-diff.json` |
| print/web text layer | 48,255 chars each, token-multiset diff 0/0, per-page byte-identical 8/8 — `printweb.log` |
| check_s11 (§1.1/P8) | **ALL PASS**; P8 min SVG font-size 13.5 — `check_s11.log` |
| source boxtitle sweep | 12/12 fit, 0 over budget — `boxtitle.log` |
| SVG boxtitle sweep | 18/18 fit, 0 overflows — `boxtitle-svg.log` |
| creambox canonical (PIL true ink) | **NO OVERFLOW**; all inside-only clearances positive (min +5.0, P2 AND YOU? box) — `creambox-check.log` |
| verify_ed | **VERIFY ALL PASS** (Q39/Q40/Q46/Q52/Q55/Q125 fix1 checks still pass; text.md 150 answers; P8 min PDF font **10.12 pt ≥ 10 pt**; SVG zero real CJK) — `verify.log` |
| P8 min font | SVG 13.5 pt; PDF 10.12 pt — both ≥ 10 pt threshold |
| 8-page visual | All 8 web-PDF pages rendered (`visual/web-p-*.png`, 100 dpi) and read: no overflow, no overlap, no defect. P5 Q73 stem + gloss + SPEAK UP box verified by eye; P8 ANSWERS `73. up` verified by eye |
| SVG change scope | ONLY `p8-test.svg` changed vs pre-delta (`svg-pre.sha256` vs `svg-post.sha256`); other 7 SVGs byte-identical |
| 150-key fill/rewrite audit | All 50 Completar frases (34) + Reescribir (16) keys checked against their stems — all fit their blanks (incl. Q73 `up` in `Speak ___`; cross-checks Q70 `silence` / Q79 `speak → are speaking` / Q133–136) — `key-stem-check.txt` |

## 6. D5 — count only, no judgement, no fix

No definition of "D5 字体" found (same as proof1). Recorded only: print-PDF `pdffonts` = **41 rows / 35 distinct font names** (`pdffonts-print.txt`, `pdffonts-distinct.txt`). Not judged, not repaired.

## 7. Notes / deviations (for the coordinator)

1. **SVG scope is p8 only, not p5+p8.** The task expected p5/p8 to change, but P5 renders only the stem (`Speak ___`), not the key — the stem is byte-identical, so `p5-youth.svg` is correctly unchanged. Only the answer page (p8) carries the key. Verified: pre/post sha256 of p5 identical (`5aab5f16…`), p8 changed (`e565acaf…` → `1c7f8051…` in freeze reproduction).
2. **Freeze baseline `--build` semantics.** `tools/freeze.py baseline` requires `--build` = a directory containing `run.py` (it copies it and rebuilds) and `--core-svg` = the SVG dir to match. Pointing `--build` at the core svg dir (`core-en/svg`) cannot work — there is no `run.py` there. I ran the meaningful checks both ways: edition baseline `--build <edition> --core-svg <edition>/svg` = 8/8, AND core-en baseline `--build core-en --core-svg core-en/svg` = 8/8 (read-only; core integrity line confirms core SVGs unchanged). If the coordinator intended a different invocation, the tool as written does not support it.
3. **Occlusion log line.** The `occlusion.log` contains a `selftest OK: planted classes fired …` line printed by the tool itself on the real-audit run; I did NOT invoke `--selftest` (per task). The real audit result is `0 flags`.
4. **Runtime restart during visual rendering.** The first `pdftoppm` run was interrupted by a VM/runtime restart, leaving `web-p-8.png` truncated (PIL load failed). Re-rendered p8 only (`-f 8 -l 8`); all 8 PNGs re-verified loadable at 2032×2813 before the visual check.
5. **Scope hygiene.** `git status --porcelain -- production/` shows 457 `M` entries, all under W43 (other parallel agents' redesign work) — none under `production/2026-w47/`. My writes were confined to the untracked `production/2026-w47/2026-w47-en-es/` dir, my scratch dir, and `dump_reg.py`'s designed output `scratch-fanout-en2/fanout/es/registry.json` (regenerated in place, now also `up`). Core-en untouched (`git status` shows it still as untracked `??`, no modifications; freeze-core integrity line agrees).
6. **WEEKLY-KIT.md updated** (in-edition): new print/web/text SHAs + sizes (see §1) and a Delta Q73 entry in §9. No commit/push (coordinator's job).

## 8. Conclusion — ready for proof2: YES

Single-key delta only, registry/text diffs exactly 1 line each, Q73 consistent across all four sources and with fixed core-en, every gate green (occlusion 0, p8 CLEAN, freeze 8/8 ×2, keycheck 150/150 with only the known #150 exception, print/web 8/8 identical, P8 min font 10.12 pt, 8 pages visually clean, 50/50 fill-in/rewrite keys sane). Nothing outstanding except the proof2 read itself.
