# DELTA-NOTE — 2026-W47 en-zh-tw · Q73 key sync (`speak` → `up`)

- Edition: `production/2026-w47/2026-w47-en-zh-tw/` (English target, Traditional Chinese reader)
- Trigger: core-en fix2 (Q73 key "speak" → "up"; stem "Speak ___: tell a teacher.",
  note "speak up = 大聲說出來" unchanged); re-proof (a) passed.
- Scope: **this edition only, one key only** (`content56.py:49`). No commit, no push.
- Scratch: `hidden_files/w47/scratch-delta-en-zh-tw/` (logs in `gates/`, pre-state in `pre/`,
  visual thumbnails in `visual/`).

## 1. Pre-rebuild verification (all matched the task pins before any edit)

| File | SHA-256 | Size |
|---|---|---|
| Print PDF `The-Lucerna-VOL4-en-zh-tw.pdf` | `7641031186c77653ac1263056a968ba7ce2ffb9383716c5a35cfad798e0fc334` | 38,152,350 B |
| Web PDF `The-Lucerna-VOL4-en-zh-tw.web.pdf` | `e07e5dd048dad9ab1ed42daa6d33c2e9f0dea129538b957c06afe25627e0d177` | 2,965,191 B |
| `2026-w47-en-zh-tw.text.md` | `57cb886738e8e23d79abe531e1f03ee7372560c5020ff02d4d6997ea117651b3` | 51,147 B |
| `ABSTRACT.txt` (MUST-PRESERVE) | `47750881038ea49c33d1a562346d13a23bb0b058f6e487e3dd35a985ecc80f16` | — |
| `registry.json` | `156b499d65968bde9f7e2e64ae03fe635900bfef7bfcb223a11f2e0f8b689c65` | — |
| `content56.py` | `d2881cddd4c0e8b978ff09c0b0dfab066be180132253ea4227842f8020cd7c98` | — |

- Registry Q73 (pre): `{"n": 73, "page": 5, "level": "A2", "type": "完成句子", "key": "speak", "note": "speak up = 大聲說出來"}`.
- text.md L1151 (pre): `73. [A2] 完成句子 — speak (speak up = 大聲說出來)`.
- P8 SVG (pre): `73. speak · 74. d · 75. a · 76. b (right = 權利 b) · 77. c · 78. Schools …`.
- P5 SVG (pre): stem `Speak ___: tell a teacher.` + gloss `to speak up = 大聲說出來`.
- Core对照 (read-only): `core-en/content56.py:49` = `f.ex("A2", "完成句子", "up", "speak up = 大声说出来",` — already `up` ✓.
- ABSTRACT.txt (pre): first line starts `…已宣佈結果`, `宣布` 0× ✓.

## 2. The one edit

`content56.py:49` only:

```diff
-f.ex("A2", "完成句子", "speak", "speak up = 大聲說出來",
+f.ex("A2", "完成句子", "up", "speak up = 大聲說出來",
      "Speak ___: tell a teacher.", instr="填空")
```

Note and stem untouched (one byte-for-byte verified edit; no other `speak`-key remains:
`grep '"speak", "speak up'` → no match after the edit). Rebuild sequence (tools venv python):
`run.py` → adapted `dump_reg_delta.py` (registry → edition's own `registry.json`) →
adapted `make_textmd_delta.py` (copy of the fanout exporter, `REG_PATH` repointed to the
edition registry; the originals hardcode fanout-scratch paths and were NOT overwritten) →
`render.py` → `tools/webpdf.py svg/ The-Lucerna-VOL4-en-zh-tw.web.pdf`.

## 3. Post-rebuild SHAs

| File | SHA-256 | Size |
|---|---|---|
| Print PDF | `854d0943264c0821842da52d75585a5eeaaf537b371e0148d22bfab7a1853468` | 38,152,349 B |
| Web PDF | `e6e9f8596f14d431c7805b0ad630c91669317b2a99f3d4557ac08903526a41bb` | 2,965,206 B |
| text.md | `cf12ebfe88d7804ccef05d2fb62d8e94dc68ed081a20577cb8adac2ae6386e2b` | 51,144 B |
| `ABSTRACT.txt` | `47750881038ea49c33d1a562346d13a23bb0b058f6e487e3dd35a985ecc80f16` (**unchanged**) | — |
| `registry.json` | `ee44f57db25c51848ec30e1912731437b1ffb2a1046ddc87ed245e9bc5e3df3c` | — |

## 4. Diff evidence (exactly 1 line each)

Registry diff (`gates/registry.diff`):
```diff
583c583
<   "key": "speak",
---
>   "key": "up",
```

text.md diff (`gates/text.diff`):
```diff
1151c1151
< 73. [A2] 完成句子 — speak (speak up = 大聲說出來)
---
> 73. [A2] 完成句子 — up (speak up = 大聲說出來)
```

SVG bytes vs pre-rebuild (`gates/post-svg-sha.txt`, `gates/final-svg-sha.txt`):
p1/p2/p3/p4/p5/p6/p7 SAME, **only p8-test.svg CHANGED — and that is the correct,
expected scope, not an anomaly**: the Q73 key appears only on the P8 answers page;
P5 prints only the `Speak ___` blank + the `speak up` gloss, the key itself never
goes on P5. The en-es delta confirmed the same pattern (p8 carries `73. up`, p5
byte-identical). No rework is warranted on this point.

## 5. Q73 four-source consistency (all `up`)

1. registry.json: `{"n": 73, "page": 5, "level": "A2", "type": "完成句子", "key": "up", "note": "speak up = 大聲說出來"}`.
2. text.md L1151: `73. [A2] 完成句子 — up (speak up = 大聲說出來)`.
3. P8 SVG: `73. up · 74. d · 75. a · 76. b (right = 權利 b) · 77. c · 78. Schools …`.
4. P5 SVG: stem `Speak ___: tell a teacher.` + gloss `to speak up = 大聲說出來`
   (gloss line `譯注｜bullying = 欺凌 · to speak up = 大…`, p5 byte-identical to pre).
   Full evidence: `gates/q73-four-source.txt`.

## 6. ABSTRACT.txt preservation

- SHA before = SHA after = `47750881038ea49c33d1a562346d13a23bb0b058f6e487e3dd35a985ecc80f16`.
- `宣布` 0× before and after; first sentence `…已宣佈結果…` intact.
- KIT §5 item 4 correction note preserved (KIT untouched except §2 SHAs, §3 header/text-layer
  line, §5 item 5 membership correction + item 6 delta entry).

## 7. OpenCC s2t self-check (`gates/s2t.log`, venv `OpenCC('s2t')`)

ABSTRACT.txt / registry.json / text.md / 8 SVGs: **0 diffs each, total 0** ✓.

## 8. Gate table (all green; logs in `gates/`)

| Gate | Result | Evidence |
|---|---|---|
| run.py | rc=0, TOTAL 150, 0 FLOW OVERFLOW, P8-keys 2137/2560, P2-ex 2532/2560 | `run.log` |
| freeze baseline, edition (`--build` = this edition's own build dir, `--core-svg` = its shipped `svg/`) | 8/8 SVGs byte-identical; shipped edition SVGs unchanged by the run | `freeze-baseline-edition.log` |
| freeze baseline, core read-only对照 (`--build` = core-en, `--core-svg` = core-en/svg) | 8/8 SVGs byte-identical; shipped core SVGs unchanged by the run | `freeze-baseline.log` |
| freeze diff core-vs-edition | TOTAL added CJK 775 (same as pre-delta); only p8 differs from the pre-delta diff (+82/-90 → +81/-89) | `freeze-diff.log`, `freeze-diff-pre.log` |
| occlusion audit (real run, no --selftest flag) | 0 flags | `occlusion.log`, `occlusion.json` |
| p8 extract | noted 60/150 (same set as core) | `p8-extract.log`, `p8-extract.json` |
| p8 compare (read `p8-compare.json` body) | CLEAN, missing=[], extra=0, keydiff [137, 138, 139, 150] | `p8-compare.log`, `p8-compare.json` |
| keycheck | registry-vs-P8 149/150 exact + n=150 exception, mismatch=[]; extract keys 150/150, missing none; registry-vs-core 146/150, diff only {137, 138, 139, 150} (Q73 now matches core); Q38–41 b/a/d/c | `keycheck.log` (`keycheck_delta.py`) |
| print/web text layers | per-page byte-identical 8/8 (11657/12448/10671/11698/10138/10592/12250/19489 chars), token-multiset diff 0, plain `pdftotext` 47,829 chars each | `textlayer.log` (`textlayer_compare.py`) |
| check_s11.py zh-tw | ALL §1.1/P8 CHECKS PASS; P8 min font 13.5 SVG units | `check_s11.log` |
| P8 min font (PDF, PyMuPDF) | 10.125 pt ≥ 10 pt (P8 spans 269; doc min 10.125 pt) | `p8-minfont.log` |
| creambox true-ink (B-group ink-box script, adapted to this edition) | 32 boxes, STRADDLE 0, CREAM-COVER 0; min ink bottom clearance +2.5 px (P2 box, pre-existing — P2 byte-identical) | `creambox-ink.log`, `creambox.json` |
| creambox canonical (+45 px window) | 32 boxes, 0 inside-only negatives (min clearance +4.5); P7 summary 7 boxes, min inside +47.7, min desc-clear +41.6 | `creambox.log` |
| 8 pages visual | all clean (cards re-rendered by render.py; thumbnails in `visual/`) | §9 |
| 150-key/stem fit review | all fit (see §10) | `gates/exercises.json`, `gates/fillins.txt`, `gates/keyfit.log` |
| D5 fonts | recorded only: print 43 font objects, web 43 font objects, all embedded+subset | `gates/pdffonts-print.txt`, `gates/pdffonts-web.txt` |

## 9. Visual check (8/8, from re-rendered `cards/`)

- P1: masthead, headline, Capitol photo, SEARCHES / IN THIS ISSUE / WORD OF THE WEEK boxes — clean.
- P2: calendar, turkey photo, SAY IT, exercises 11–19 + 20–27 — clean. Q19's blank sits
  tight at the bottom (P2-ex 2532/2560, as before; P2 byte-identical to pre-delta).
- P3: Rousseau tiger, Haymitch, B/C/D sections — clean.
- P4: W. G. Grace photo, Ashes, ATP — clean.
- P5: Q73 `Speak ___: tell a teacher.` renders; gloss `to speak up = 大聲說出來`;
  `SPEAK UP · 大聲說出來` box; Lawrence children photo — clean.
- P6: map/ballot/chart, B2 items — clean.
- P7: toolbox, readers' corner, example letter, Johnson portrait — clean.
- P8: cloze/dialogue/writing/model + ANSWERS block shows `73. up · 74. d · 75. a · 76. b …` — clean.

## 10. 150-key/stem fit review (Q73 lesson: three-source agreement is not enough)

Method: stub-execution extraction of all 150 (n, level, type, key, note, body, opts) pairs
(`extract_pairs.py`, adapted from the fanout text.md exporter) — keys+types match
registry.json 150/150 (`gates/extract_pairs.log`).

- **78 fill-in/rewrite/translation/dialogue/cloze**: each key read against its stem — all fit.
  Incl. Q73 `up` in "Speak ___: tell a teacher." (note "speak up = 大聲說出來" = the
  phrasal verb the blank completes); cloze 112–119 verified against the P8 passage verbatim
  (Tuesday / call / continues / will meet / writes / will certify / wears / will watch);
  dialogue 145–149 verified against the dialogue verbatim (row / film / popcorn / show / Friday);
  translations 137–140 + corrections 108–111 verified (keys are the corrected sentences).
- **51 MCQ** (單選/閱讀理解/圖表讀數): mechanical check — every key letter is among the
  options in its body; 0 fails (`gates/keyfit.log`).
- **20 match** (詞彙配對): every key a–d, note ends with the same letter; 0 fails.
- **Q150 寫作**: open item, no key to fit.
- Observation (not a defect, out of delta scope — **not changed**): 3 duplicate stems,
  all core-identical P6 revisits with fitting keys: Q2/Q95, Q5/Q96 (content12.py +
  content56.py), Q6/Q12 (content12.py ×2). Inherited core design, Q73-style mismatch: none.

## 11. Notes / corrections found along the way (recorded, not expanded in scope)

1. **KIT §5 item 5 membership error (corrected in KIT):** it claimed the pre-delta
   registry-vs-core diff was "the 5 reader-language keys 137–140, 150". Measured from
   both registry files, the pre-delta diff was {Q73, 137, 138, 139, 150} — Q140
   "打破沉默。" is byte-identical in core and edition. Count 145/150 was right.
2. **KIT "42,852 chars" text-layer figure (corrected in KIT §2/§3/§5):** not reproducible
   by plain `pdftotext` (47,829) or `-layout` (103,931) on the rebuilt PDFs; the method
   was never recorded. KIT now quotes the reproducible plain-`pdftotext` count, 47,829
   each, identical print/web.
3. **Canonical creambox desc-clear −1.5 px** (P2 box, last line `句英語寄給編輯部。`,
   clearance +4.5): a 0.30×fontsize descender *estimate* on a CJK line whose final `。`
   has no descender; true-ink bottom clearance is +2.5 px and the true-ink audit +
   occlusion audit both report 0 flags. Pre-existing (P2 byte-identical). No action.
4. `tools/occlusion_audit.py` prints its internal detector selftest on every real run
   ("selftest OK: planted classes fired …"); the audit itself ran without `--selftest`.
5. Two parallel exec calls in this session were aborted by the runtime; all affected
   steps were re-run sequentially with the same results (s2t, p8 — no data lost).
6. No other edition, week, or tool file was touched. No commit/push (coordinator's job).
   KIT updated: §2 new SHAs/sizes, §3 header + text-layer line, §5 item 5 correction +
   item 6 delta entry (ABSTRACT §5 item 4 note untouched).

## 12. Conclusion

**Delta complete, all gates green. Q73 is `up` in all four sources; ABSTRACT.txt preserved
byte-for-byte; only p8 changed (correct and expected — the key lives only on P8, never
on P5); the only changed lines are the Q73 key in registry.json and text.md. Freeze
baseline: edition rebuild 8/8 + core read-only对照 8/8. Ready for proof2.**
