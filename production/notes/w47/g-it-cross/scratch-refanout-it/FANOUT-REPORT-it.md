# FANOUT-REPORT-it — W47 Italian-target family, re-fan-out (2026-11-11)

10 editions rebuilt from finalized core fix3 (commit `36bdec2e`, re-proof (a) zero issues),
after the table fix + hand-patch inventory. **Build only — no commit, no push.**
All builds with `tools/venv/bin/python` (Pillow 13.0.0); TMPDIR = goals-side scratch tmp.

- Source core: `production/2026-w47/core-it/` (md5s verified against 36bdec2e before building:
  content8.py `629b5b0a088c492ed720a5474a8150b0`, content12.py `91cdfbb95425db7de5cc0e65dbf3ac1a`,
  content34.py `189269425b298e676c354f262b7eff19`).
- Mechanism: `hidden_files/w47/scratch-fanout-it/` (`build_edition.py`, `gates.py`, `translations.py`).
- Logs/reports: `hidden_files/w47/scratch-refanout-it/` (this report, `gates-<lang>.log`,
  `check-<lang>.json`, `freeze-verify.txt`, `shas.txt`, `sheets/sheet-<lang>.png`).

## 1. Deliverables (10/10, each print PDF + web PDF + .text.md, 1317 lines, 150 exercises)

| edition | print SHA-256 | print bytes | web SHA-256 | web bytes | text.md SHA-256 | text.md bytes | gates | words (print=web) | P8-keys end (bottom 2552) |
|---|---|---|---|---|---|---|---|---|---|
| it-de | `ee5a962f1f3b59a8a225acbf949ee542b7d81f99451cc1dc591babb0a3c3234f` | 14,037,260 | `e6d3df844c9fa4fd3ef5e39dcf6cd80d740dfbd7cc5208384763efc6ee89eb84` | 1,297,292 | `8660fc02b2510cce831e5c3e57b0020949dc4c05e5d4b1bd30db4e667b4cc222` | 56,699 | 20/20 | 7787 | 2514 |
| it-en | `3b6b2d2c9067aa88e22914a83ef4ca6ddf37ce2e98e154c80bd9ca7fb79190fd` | 14,032,945 | `03bb1ff239dc46d408130d8c828417e004a9a0b488ba50e8594f5a8122dd5e2f` | 1,291,182 | `f12950aa8561371585da7ada54b15eb83df595ccb0fe51cfa513650dffd6a984` | 55,221 | 20/20 | 7934 | 2514 |
| it-es | `8b7547d315a50de4858d6971483f79951c2d497ef28e4f71dc66942bc405411b` | 14,033,641 | `efc1404b8797a8b133fdafe911c1886a9a2be24158a2e49a4dcaeb657cdb9266` | 1,291,428 | `64a8ac2fce4e7063c7bebfcbb5b6cde2f8fe1fbde4f265a510e6abf83d007031` | 56,214 | 20/20 | 8001 | 2529 |
| it-fr | `6e393b3d385c606443c82b7813ddfae2623b9ee2fff128690247f1f2f0fcf00f` | 14,034,074 | `7276c70ff46caf931ba761ec3ca36f7b8ee467c1c1d22931f460eaa81596b77f` | 1,290,987 | `a634057bfdf97f0c29492ba769c96213a6540ef15f8a1cbf17bc88ed51dc92f7` | 56,538 | 20/20 | 8012 | 2514 |
| it-ja | `279962b7b3ae203049e1646d81c737228309aff0b864fef94079f4cc81ddb319` | 28,221,039 | `4df33c6917da1b4452d8f8aa7574eb47d70161a074c0b30424cbb684ab007a7b` | 1,901,688 | `bf64b304305e5d6e0679a9816c6b95576709c47e30dd69aa4cc6b24bf6def634` | 58,186 | 19/19 | 6749 | 2546 |
| it-ko | `d5698327bbb331d0270e5ca86c531068fe8425f0ff11251747fc4ddd9768b7a3` | 19,296,912 | `85722a84c68bb1e03b2bde56462d23ffc0855405ae4e4911d71e04adc819086e` | 1,607,490 | `e9dbe37172028913924567df9445604a4bd79584fe910de4c487662b8ab45614` | 57,347 | 19/19 | 7414 | 2499 |
| it-nl | `2091448cb9155812311ae298e0c2f349d0b2d83ac6fa94f26f79f10b4c4c5a7f` | 14,034,409 | `039ee0bb9cc55f4faeceba85d5e11752abbb6fd2843de2e082c9c4cdf2b88b8f` | 1,291,738 | `0a044d4b87da3cf281a18dad08cecef6d2842a99f4cb44da36276e35f902f4dd` | 55,509 | 20/20 | 7888 | 2529 |
| it-pt | `6f74ee92c72d4ca545fb763c268231b05b6970a5e170b943cdc2882a3ce4a477` | 14,036,628 | `f28a563544bcac8998097fc418c94b47f92a650b351518339c9be864a1ada1c4` | 1,294,408 | `2ce7bfe9bb1f58d72b6249c4a2d2cd2bf5d97e028e10d2e3acfc480797627cb8` | 55,739 | 20/20 | 7965 | 2529 |
| it-ru | `f74bd65735550718a9927adb47047547d6cd3972f9ccfa4164bd467bf257c3fd` | 14,180,887 | `c35f390b39e3fe0ef6e95f9a9a292ab94cc356a3955decdcd2dbcd4cf357d1f5` | 1,441,225 | `d1b6ddb1e691f74f7a7ce2960077774987dfd36b99712c8b3b49bb254a8361e2` | 67,687 | 20/20 | 7587 | 2529 |
| it-zh-tw | `79e51c537d9bcafb7612a056358cb9597c998ec84db1e16b183099ca98e5cfe8` | 27,779,719 | `a809a3a53ca7c0b6a462803bc7fd2cf65f5f99621a3d08b7b872ce6f49edaf79` | 2,074,068 | `681dff470eeb01dae8883e5c34773599290711c724e0ec741b59b82da8933e45` | 52,515 | 19/19 | 6832 | 2484 |

Web PDFs all < 7 MB (largest zh-tw 2,074,068 B). Print PDFs 14.0–28.2 MB. All 10 builds
RC=0 on the first attempt (batch 1: en/de/es; batch 2: fr/pt/nl; batch 3: ru/ja/ko; batch 4: zh-tw).
No FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE in any build log.

## 2. Gates (10/10 ALL PASS, 0 FAIL)

Per edition (`scratch-refanout-it/gates-<lang>.log`): Latin/Cyrillic editions 20/20,
CJK editions (ja/ko/zh-tw) 19/19 — the strict-CJK gate does not apply to CJK readers.
Every edition: occlusion **0 flags**; p8 extract **150/150**, compare **CLEAN** (keydiffs
only [137, 138, 139], the re-aimed reader-sentence keys, expected); freeze diff **0 unexplained**
fragments; print/web text multiset identical (word counts above, chars equal); web PDF < 7 MB;
P8 min font **13.0 px = 9.75 pt** (SOP §1.1 floor); §1.1 scans pass; text.md validate **0/0**;
keys + notes match. Freeze baseline re-taken per edition: **8/8 sha256** (`freeze-verify.txt`;
new baselines in `scratch-fanout-it/<lang>/freeze-baseline/`, first-fan-out baselines preserved
in `scratch-refanout-it/prev-fanout/`).

## 3. Mechanism checks (3/3, verified before and after building)

### 3.1 Table fix — 17 values, all in place, all measured
`translations.py` holds 240 entries; all 17 new values verified present exactly once before
building (spot: it-de D1 `Die Woche　Cosa succede, giorno per giorno`, U+3000 separator).
PIL true-ink clearance measured on the rebuilt SVGs (`scratch-refanout-it/measure_built.py`,
ALL PASS) — measured equals the table-fix prediction in every case:

| edition | boxes | measured clearance (px) |
|---|---|---|
| de | D1 | +5.5 |
| fr | D1 / D2 / D3 / D4 | +4.5 / +5.5 / +8.5 / +111.5 |
| pt | D2 / D3 / D4 / D5 | +15.5 / +36.5 / +26.5 / +140.5 |
| nl | D1 / D2 / D3 | +22.5 / +30.5 / +63.5 |
| ru | D2 / D3 / D4 | +30.3 / +24.9 / +107.2 |

**fr D1 +4.5 px** is below the nominal +5 px gate but equals the prediction, and TABLE-FIX-LOG §3
records `CHIFFRES` as already the shortest French form with no shorter alternative; the task names
+4.5 as the expected value. The gate was treated as a regression tripwire (stop only if measured
< predicted) — it did not trip. de D1 measured +5.5 px as predicted. Gates occlusion 0 (independent
4× method) confirms both fit.

### 3.2 Exporter 「翻譯」 fix — labels localized in all 10 editions
`translations.py` carries the 「翻譯」 map (en Translate, de Übersetzen, fr Traduire, es Traducir,
pt Traduzir, nl Vertalen, ru Переведите, ja 翻訳, ko 번역하기, zh-tw 翻譯);
`build_edition.py` asserts `consumed "翻译": 4` + zero-tolerance residual-CJK check.
Verified per edition by `check_refanout.py` (ALL PASS): content8.py:69/71/73/75 E labels +
text.md L969/971/973/975.
- **it-en / it-es byte comparison (task-required):** the 4 label lines L969/971/973/975 are
  **byte-identical** to the hand-fixed backup versions (4/4 lines, both editions; 1317 lines each).
  The mechanism now generates exactly what the hand fix produced.
- The first fan-out's residual 「翻譯」 on Q137–140 is gone in all 10 rebuilt editions
  (the es fix1 text.md-only patch is superseded by the mechanism).

### 3.3 Hand-patch inventory — exactly 1 real hand patch, re-applied
`PATCH-INVENTORY.md`: only it-nl `content12.py:18` masthead spacing 11.5 → 11.0 is outside the
mechanism. All other reported "patches" are fix3 content (9 lines/edition: D1, P2 b/d, D11, P4 b/c,
P8 F), carried automatically — grep-verified in place exactly once each per edition, old wording
absent (`check_refanout.py` ALL PASS).

**it-nl spacing re-apply (done 2026-11-11):** `spacing 11.5 → 11.0` on `2026-w47-it-nl/content12.py:18`
only (asserted count==1); 0 occurrences of `spacing=11.5` remain in the file. Re-ran step-wise:
run.py RC=0, render.py RC=0, webpdf.py RC=0 (logs `nl-rerun-{run,render,webpdf}.log`).
SHA check: print PDF changed, web PDF changed, **text.md UNCHANGED**; p1 SVG changed.
Masthead band measured with `tools/occlusion_audit.py::ink_box` (4× method) on the rebuilt
`svg/p1-prima.svg`: band left **10.5**, right **1873.7**, width 1863.2, page 1950 — inside,
left spare 10.5, right spare 76.3. (At 11.5 it would be 26.5 px wider → left −2.75, matching the
original build1 failure ink x=−2.7.) Core-it line 18 stays 11.5 (correct for the Chinese masthead);
the nl rule was NOT merged back into core-it.

**content8.py:80–82 adjudication:** the backup's longer glosses ("la parte del sistema fiscale,
un livello di reddito" etc.) are the PRE-fix3 core wording; fix3 deliberately shortened them
(P8 F matching options protruding into the column gap — `PATCH-INVENTORY.md` §4 B-7/B-8/B-9).
The rebuild correctly carries the fix3 short forms. The earlier coordination note warning that a
re-fan-out would "lose" those patches is superseded by that adjudication.

## 4. Sim cross-check — 0 unexpected changes

Rebuilt-vs-backup changed lines (content12 / content34 / content56 / content7 / content8),
compared against the table-fix simulation (`scratch-fix-it-table/sim-NEW-<lang>-content*.py.txt`):

| edition | changed lines |
|---|---|
| de | 8/6/0/0/14 |
| en | 6/6/0/0/14 |
| es | 6/6/0/0/14 |
| fr | 12/6/0/2/14 |
| ja | 6/6/0/0/14 |
| ko | 6/6/0/0/14 |
| nl | 12/8/2/2/14 (content12.py 10 after the spacing re-apply) |
| pt | 12/6/0/2/14 |
| ru | 10/6/0/2/14 |
| zh-tw | 6/6/0/0/14 |

Line-set equality holds for every file (same changed lines, no extras). The E-label change
(4 lines in content8.py) + fix3 (9 lines) + table values account for all of them.

## 5. Visual check — 8/8 per edition, 0 defects

- 10 contact sheets (`scratch-refanout-it/sheets/sheet-<lang>.png`, 8 pages each, 80 pages total):
  no overflow, overlap, clipping, or tofu in any edition.
- Full-size spot checks of the highest-risk pages: P1 for de/nl/fr/pt/ru (D1 subtitles, cifre
  boxes, mastheads — incl. nl masthead at spacing 11.0 and pt/es-style flush-left mastheads,
  both fully rendered with no glyph clipped) and P7 for nl/fr/pt/ru (ERRORI TIPICI titles fit their
  cream boxes; 3-line disclosures end clear of the FRASI rule).
- Known core-pattern traits carried over unchanged (not defects): P3/P5 structural whitespace;
  ko/ja P5 word-list wrap-after differences; ru tight word gaps in P7 FRASI glosses.

## 6. KIT updates

Each edition's `WEEKLY-KIT.md` was rebuilt from the first-fan-out KIT (preserved verbatim in
`scratch-refanout-it/backup/2026-w47-it-<lang>/WEEKLY-KIT.md`): new print/web SHA + bytes and
text.md bytes in §7 (translations.py now 240 entries), fresh gates record in §8, new **§11
Re-fan-out** section. Verified by independent grep: new print/web SHA present ×1 per KIT,
old print/web/text.md SHA **0 occurrences** in every KIT (es §7/§9 fix1 SHAs replaced with
superseded-notes). Per-edition `RECORD.md` in `scratch-fanout-it/<lang>/` carries a re-fan-out
note; `scratch-fanout-it/STATUS.md` carries a family-level note.

## 7. Backup

`scratch-refanout-it/backup/` — 10 old edition dirs, **430 files, 312 MB**, per-file SHA-256
verified (`backup/source.sha256` vs `backup/backup.sha256`, diff clean). **Do NOT delete before
the new bundle is in the repo.** First-fan-out scratch (logs/RECORDs/freeze baselines) preserved
at `scratch-refanout-it/prev-fanout/` (346 MB) because `build_edition.py`/`gates.py` overwrite
their logs in `scratch-fanout-it/<lang>/`.

## 8. Discrepancies recorded (not defects)

1. **Edition list:** the task's list read `it-{de,en,es,fr,it,ja,ko,nl,pt,ru}` ("it 版在
   production 根目录下平铺"), but **no `2026-w47-it-it` edition exists** anywhere: the grid's
   10 non-core it editions are de/en/es/fr/ja/ko/nl/pt/ru/**zh-tw**, and the mechanism
   (`build_edition.py` LANGS, `translations.py`) supports exactly those 10. Built zh-tw as the
   10th; did NOT invent an it-it edition.
2. **Exporter-fix commit hash:** the task cited `fe1cb048`, which **does not exist** in this repo
   (`git log --all` has no such revision). The fix lives goals-side
   (`scratch-fix-export-it1/FIX-LOG.md`) and was verified by content (240-entry map, harness
   byte-identical re-export), not by hash.
3. **fr D1 +4.5 px:** below the nominal +5 px gate, exactly as predicted — see §3.1.
4. **Environment quirk:** `/dev/null` in this sandbox is a regular file (50–216 bytes), not a
   character device; it broke `git show | md5sum` and Python `subprocess.DEVNULL` at different
   times. Workaround used throughout: write to real files under the scratch tmp dir.
5. **Repo house rules:** `~/workspace/weekly-git/AGENTS.md` was read during this run (runtime
   instruction). Nothing in it contradicts this work: the it edition dirs are untracked (0 files
   in `git ls-files`); only core-it's 5 source files are tracked (fix3 commit); no committed
   edition was touched; no commit, no push.

## 9. Scope

Work confined to `production/2026-w47/2026-w47-it-*/` and `hidden_files/w47/` (scratch-refanout-it,
scratch-fanout-it). No other week touched. No commit, no push — the re-fan-out bundle is built
and gated, awaiting the coordinator's bundle commit step.
