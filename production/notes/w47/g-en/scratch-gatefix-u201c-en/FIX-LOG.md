# FIX-LOG — W47 U+201C fix2 port (en family: 2026-w47-en-nl + core-en)

Scope: port the core-de fix2 font-routing patch into exactly these 2 editions.
No other edition touched (no de edition — verified 0 defective glyphs there, and
core-de/svglib.py md5 unchanged `e791b279…`), no other file, no commit / push / lint.
Work dir: `hidden_files/w47/scratch-gatefix-u201c-en/` (this dir).

## §0 The port

Source: `production/2026-w47/core-de/svglib.py` lines 75–105 (commit 4ac7192c),
the fix2 block: `if ch == "\u201c"` branch in `_char_font` + the `_QUOTE_CLS` /
`_PATH` rows below it. Ported into the edition's `svglib.py` only — never a
wholesale sync (core-de also carries kinsoku wrap code the en files do not have;
that was NOT ported).

Extension (per task brief, fontTools-verified): the condition covers all three
codepoints — `if ch in ("\u201c", "\u201d", "\u2019")` — because U+201D and
U+2019 are also 1000/1000em in Noto Sans CJK SC/TC. The class is derived, not
spelled, exactly as fix2 does (`_QUOTE_CLS = _char_font("\u201c", "serif", False)`;
no literal `'news'` anywhere — freeze_direct accounts source literals against
tr_<lang>.py). Pre-patch structure verified in both targets before patching:
`_char_font`, `_PATH`, `_NEWS`, `_NEWS_B` all present, same shape as core-de
(the only other core-de/target diff is a stale line-34 comment saying "TC"
where the faces are SC; left untouched — the diff contains ONLY the ported block).

Ported block (identical in both files except the blast-radius comment):

```python
    # fix2 (2026-11-11, proof2 D1/D2 in core-de; ported 2026-11-12 to this
    # edition, extended to three codepoints): U+201C/U+201D/U+2019 are
    # full-width (advance 1000/1000em) in Noto Sans CJK SC/TC — their ink
    # sits at the right edge of the cell, so a sans quote leaves a wide
    # white gap before it. Newsreader's quotes are the narrow glyphs the
    # other pairs already use (~0.44em). Route these three codepoints
    # through the serif branch, which assigns them their Newsreader class:
    # the characters stay the same everywhere (source, text.md, PDF text
    # layers) and only the rendered glyph changes. Blast radius, verified
    # by SVG census on the shipped build: exactly N glyphs in this edition
    # (all P8 ...); no other sans string holds any of the three codepoints.
    # No new string literal is written here on purpose: freeze_direct.py
    # accounts source literals against tr_<lang>.py, and the class name
    # 'news' occurs in no tr literal — a literal 'news' would fail its
    # source level. The class is therefore derived, not spelled.
    if ch in ("\u201c", "\u201d", "\u2019"):
        # italic=False on purpose: the serif branch with italic would pick
        # the "news_i" class, which has no ("sans", ...) _PATH row.
        return _char_font(ch, "serif", bold)
    if cp in _CMAP["sans_b" if bold else "sans"]:
        return "sans"
    return "deja"

# fix2: _PATH entries for the Newsreader class inside sans runs, keyed by the
# derived class name (see _char_font). _pil resolves ("sans", bold, "news")
# to the Newsreader faces, mirroring the ("serif", bold, "news") rows.
_QUOTE_CLS = _char_font("\u201c", "serif", False)
_PATH[("sans", False, _QUOTE_CLS)] = _NEWS
_PATH[("sans", True, _QUOTE_CLS)] = _NEWS_B
```

Verification of the port (both files):
- Pre-patch md5 (both files, byte-identical to each other): `05e25a0212a43d2c2298f85791e3c25d`
  (pristine copies in `pristine/`).
- `py_compile` passes on both.
- `diff` pristine vs patched shows ONLY the two inserted blocks (20 + 6 lines).
- Reverse-patch (strip the inserted lines) reproduces the pre-patch md5 exactly
  for both files (`reverse_check.py`; first version of the strip script added one
  spurious blank line — fixed, then both reversals md5-identical to pristine).
- Functional check (venv python, patched en-nl svglib): `_char_font` returns
  `"news"` for U+201C/U+201D/U+2019 in sans mode, bold and non-bold;
  `_QUOTE_CLS == 'news'`; `("sans", False/True, "news")` rows present in `_PATH`;
  Newsreader U+201C at 20pt measures 8.81px vs Noto Sans CJK SC 20.0px; `_runs`
  splits the D1/D2 quotes into their own `news` runs.
- Post-patch md5: en-nl `b4cb4b20d49cf461461e26faee001da0`,
  core-en `964c4f71be2f83df2374d988cd7d11c1` (re-confirmed after sync).

## §1 2026-w47-en-nl — DONE

- **Census** (`census.py`, per `<text>` font-family; defective = U+201C/U+201D/U+2019
  in Noto Sans CJK SC/TC/HK):
  - BEFORE (production svg/): **4 defective**, all p8-test.svg, all
    `font-family="Noto Sans CJK SC"`: D1 instruction 20pt “…” in
    `Schrijf 80–100 woorden in het Engels: “Mijn maandag 16 november”. …`
    (U+201C ×1 + U+201D ×1) and D2 key note 13.5pt “…” in
    `“Doorbreek de stilte”) · 127. A (Wereldkinderdag is op 20 …`
    (U+201C ×1 + U+201D ×1). No U+2019 anywhere in the edition.
  - AFTER (rebuilt svg/): **0 defective**. The 4 quotes are now lone
    `Newsreader` runs on P8. All other quotes in the edition were already
    Newsreader (serif runs) and are unchanged.
  - SVG change confined to p8-test.svg only (p1–p7 byte-identical to production).
    New p8 sha `6925167b7e93ff0d`.
- **Rebuild** (`tools/run_build.py --steps run,render`, scratch build-copy;
  production integrity re-hashed unchanged, 43 files): run.py exit 0, zero FLOW
  OVERFLOW / HEAD TOO WIDE, TOTAL 150, MODEL 82; render.py exit 0.
- **Gates on build-copy** (logs in `2026-w47-en-nl/`):
  - `freeze.py baseline`: **8/8 byte-identical** (re-render of build-copy source
    vs build-copy SVGs; p8 `6925167b7e93ff0d`).
  - `freeze.py diff` vs core-en: exit 0, TOTAL added CJK 9, all U+3000 (same as
    pre-fix); added Latin strings 344 (was 341 — +3 from the D1/D2 quote runs
    splitting into separate Newsreader runs).
  - `p8.py extract`: noted set 60/150 (same set as core).
  - `p8.py compare` vs core-en: **CLEAN**, missing=[] extra_count=0,
    keydiff=[137, 138, 139, 140, 150] (expected reader-language keys).
  - `occlusion_audit.py`: **0 flags**, selftest OK.
  - `spill_sweep.py`: **0 SPILL**, 124 OBSERVE (32 boxes).
  - `boxtitle_check.py`: **0 DEFECT, 0 OBSERVE, 0 marginal**
    (18 titles, 177 body lines).
  - text.md re-export (`make_textmd_en-nl.py`, copy of the delta exporter with
    paths repointed to the build-copy; original exporter untouched):
    **byte-identical** to production, sha `30bfb6f9…`, 53,565 B.
  - Determinism re-run (`run.py` again in the build copy): SVGs byte-identical.
  - Print/web text layers: `pdftotext -layout` per page — print==web on all 8
    pages, and new print text == old print text on all 8 pages (byte-identical).
- **SHAs** (print / web / text.md):
  - BEFORE: print `626e4c1bbf2c77cb579ac9f6e7511ce7036d6af1bebdb5b7700a729615dc7fee`
    29,341,266 B; web `dd4cee4884e6f3d3af68788b469ac33d4b452c75d4bad91fd68e01dc8e70cf38`
    2,411,532 B; text `30bfb6f93860fae5ae58707c28c4f2e3a18ebcc07e272681e67688451d12c0be`
    53,565 B.
  - AFTER: print `21e13a74e9d938684fcc941e2caca6a8b22ab3e5aa7deb30f2db044405eea4bd`
    29,341,219 B (−47); web `c769e979ee69e4d424e34c32bfcc01f1d7b37d64b2c4f8dd4529b29718bbcf1e`
    2,411,506 B (−26); text unchanged.
- **Sync**: `svg/*.svg` (8) + print PDF + web PDF + `cards/*.png` (8) copied to
  production; re-hashed after copy — print/web SHAs equal the scratch SHAs;
  all 8 SVGs + 8 cards byte-identical after copy. Production `svglib.py` md5
  after patch: `b4cb4b20d49cf461461e26faee001da0`.
- **Post-sync confirmation on production files**: census 0 defective;
  boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal (18 titles, 177 body lines).
- **KIT edits** (`WEEKLY-KIT.md`): §2 print/web bytes + SHAs updated;
  §5 new "U+201C fix2 port" bullet (previous SHAs recorded); §9 Build record
  new "Fix2 port" bullet. History untouched (§3 boxtitle bullet keeps its old
  SHAs as the record of that fix).

## §2 core-en — DONE

- **Census** (same method):
  - BEFORE (production svg/): **2 defective**, both p8-test.svg, both
    `font-family="Noto Sans CJK SC"`: D2 key note 15.5pt “…” in
    `主题“打破沉默”） · 127. A（世界儿童日 11 月 20 日） · …`
    (U+201C ×1 + U+201D ×1). No U+2019 anywhere in the edition.
  - AFTER (rebuilt svg/): **0 defective**. Both quotes now `Newsreader` runs.
  - SVG change confined to p8-test.svg only (p1–p7 byte-identical).
    New p8 sha `ecfff70593d5119a`.
- **Rebuild** (`tools/run_build.py --steps run,render`; production integrity
  re-hashed unchanged, 45 files): run.py exit 0, zero FLOW OVERFLOW / HEAD TOO
  WIDE, TOTAL 150, MODEL 82; render.py exit 0.
- **Gates on build-copy** (logs in `core-en/`):
  - `freeze.py baseline`: **8/8 byte-identical**.
  - `freeze.py diff` vs pre-fix core svg: exit 0, TOTAL added CJK 0, added Latin
    strings 1 (p8 +5/−1 strings: the D2 note string split into runs by the new
    Newsreader quote runs; characters identical).
  - `p8.py extract`: noted set 60/150 (same set as pre-fix).
  - `p8.py compare` vs pre-fix core p8: **CLEAN**, missing=[] extra_count=0,
    keydiff=[].
  - `occlusion_audit.py`: **0 flags**, selftest OK.
  - `spill_sweep.py`: **0 SPILL**, 115 OBSERVE (32 boxes).
  - `boxtitle_check.py`: **0 DEFECT, 0 OBSERVE, 0 marginal**
    (18 titles, 185 body lines).
  - text.md re-export (`make_textmd_core-en.py`, copy of the fix1 exporter with
    paths repointed to the build-copy; original exporter untouched):
    **byte-identical** to production, sha `23855d4b…`, 51,402 B.
  - Determinism re-run: SVGs byte-identical.
  - Print/web text layers: `pdftotext -layout` per page — print==web on all 8
    pages, and new print text == old print text on all 8 pages (byte-identical).
- **SHAs** (print / web / text.md):
  - BEFORE (disk-measured): print `08cbc1e53f2d02d6c64266d1f64ac2422eaa2f8f71e1829f877e94a5627b3213`
    41,407,287 B; web `723c29c574c2692863857b2fabad0078470c6c0efe8104b0bdca7176288a5d1b`
    2,804,275 B; text `23855d4bd60abe4a7fb4db42050cb9343202e85789ffd434634808d299215c69`
    51,402 B. NOTE (pre-existing staleness, not this fix): the KIT §7 line read
    web 2,804,281 B and the Fix 2 bullet reads web `d7927eaa…` — both were already
    stale before this fix (the web PDF was rebuilt once after fix2 without a KIT
    update); measured values are used here, and the Fix 2 bullet's history is
    left as written.
  - AFTER: print `ba7986e6856ebdd1c9c4b2cf76bce3fd56c695aa8b28dd7b4d6f8a1c4b009421`
    41,407,232 B (−55); web `7341c01ea64c80cd0d2bdbdc781381348e9103faf46d908433b5ce6fb1ea9cfa`
    2,804,232 B (−43); text unchanged.
- **Sync**: `svg/*.svg` (8) + print PDF + web PDF + `cards/*.png` (8) copied to
  production; re-hashed after copy — print/web SHAs equal the scratch SHAs;
  all 8 SVGs + 8 cards byte-identical after copy. Production `svglib.py` md5
  after patch: `964c4f71be2f83df2374d988cd7d11c1`.
- **Post-sync confirmation on production files**: census 0 defective;
  boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal (18 titles, 185 body lines);
  spill 0 SPILL (115 OBSERVE).
- **KIT edits** (`WEEKLY-KIT.md`): §7 print/web bytes + SHAs updated; §7 new
  "Fix 3 — U+201C fix2 port" bullet (previous measured SHAs recorded, incl. the
  web-staleness note); §9 new "Fix 3 gates" bullet. History untouched.

## §3 Method notes

- Builds ran through `tools/run_build.py --steps run,render` (scratch build-copy;
  production integrity re-hashed unchanged for both editions). en family uses the
  venv python (Pillow 13); no verify.py exists for en editions — TOTAL/MODEL come
  from run.py + the determinism re-run. p8 compare used explicit `--core-p8` /
  `--edition-p8` paths (`p8_path()` looks for `p8-exercices.svg`, wrong for en).
- `census.py` in this dir is the coordinator's census method re-implemented
  (per `<text>` font-family, codepoints U+201C/U+201D/U+2019, defective families
  Noto Sans CJK SC/TC/HK). BEFORE runs are `census-*-BEFORE.txt`, AFTER runs
  `census-*-AFTER.txt`.
- Freeze build-copies deleted after checks (`*/freeze-baseline/build-copy`,
  50M + 62M); the freeze `svg/` outputs are kept. The main build-copies are kept
  as the audit trail (they duplicate the now-synced production files).
- No `scratch-refanout-it2/backup/` or any other edition touched. No de edition
  touched. No commit / push / lint.

## §4 Disk

- Start (2026-11-12 ~02:56 UTC): 94G used / 56G free (quota cap ~105G).
- End: 90G used / 60G free (other workers cleaned in parallel; this task's own
  footprint is the scratch dir below).
- This scratch dir: 113 MB total after the freeze build-copy deletion.
