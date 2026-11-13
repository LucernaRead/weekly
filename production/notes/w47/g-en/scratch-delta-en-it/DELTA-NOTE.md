# DELTA-NOTE — Lucerna Weekly 2026-W47 · en-it · Q73 key sync delta

**Edition:** English target × Italian readers (`2026-w47-en-it`), VOL.4, issue week 2026-11-16..22
**Delta:** core-en fix2 sync — Q73 key `"speak"` → `"up"` ONLY
**Date:** 2026-11-11 · **Scratch:** `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-delta-en-it/`
**Conclusion: delta complete, all gates green — ready for proof2.**

## 0. Preconditions (all verified BEFORE any edit)

- Print / web / text SHAs + sizes matched the task AND proof1 PROOF-NOTE exactly
  (see §1 "pre" column). Proof1 (a) conclusion on file in `scratch-proof-en-it1/`.
- Registry Q73 key `'speak'`, text.md line 1151 Q73 `speak`, P8 extract (proof1
  `gates2/p8-extract.json`) Q73 `"speak"`, `content56.py:49` key `"speak"` with stem
  `"Speak ___: tell a teacher."` and note `"speak up = parlare senza paura"` —
  three-source same error, as expected.
- Core-en `content56.py:49` already `"up"` (read-only freeze对照; core never written by
  this delta — see observation in §5).
- Probes: `ls /dev/null` present; `git hash-object -w` OK; scratch write probe OK;
  TMPDIR pointed at scratch `tmp/` throughout; disk 64G free at start.

## 1. SHA table — pre → post (only this edition touched)

| File | Pre (SHA-256 / size) | Post (SHA-256 / size) |
|---|---|---|
| `The-Lucerna-VOL4-en-it.pdf` (print) | `bdfe23784024bb85635eb2984dd3c530c2db63aff1b7c102bc08b78b40d7b61c` / 29,327,190 B | `2db4dad1496e474fbd01315bf3b7f8393358a60155ce103f6a8bae476a5502a0` / 29,327,187 B |
| `The-Lucerna-VOL4-en-it.web.pdf` (web) | `d5e9c1af0880237350b4364d8a4be478673d87d249cd614f334849c969618e58` / 2,408,886 B | `570eef4fb1174edb33e3e46c324d96231dac086140a34e1e7376929a41525239` / 2,408,879 B |
| `2026-w47-en-it.text.md` | `433c2aec5b303a5968e535c83b38e6b30128c1b5a2318fb0fa44466f00dbb15e` / 53,947 B | `a833062570765ad5fea4e1f2a4ac4396afd28f2376bb86dbeb9991eae9e2f464` / 53,944 B |
| `registry.json` | `5d22296d375afbfc5e050de49f505560d0fe3f295e4b9b1f566835ac50758994` / 150 entries | `55b9fe3c6e3d6b12a33da1a21b592dd31f75f62d863b9ebcb46ebe3a02ad07d2` / 150 entries |

Each file is exactly 3 bytes smaller — one `"speak"` → `"up"` occurrence in the
print text layer (P8 answers), one in text.md, one in the web text layer
(web PDF −7 B total is font-subset noise around the same −3 text bytes).
Both PDFs remain 8 pages, 1462.5 × 2025 pts.

## 2. The ONLY source change

`content56.py:49` — one line, key only:

```diff
-f.ex("A2", "Completare le frasi", "speak", "speak up = parlare senza paura",
+f.ex("A2", "Completare le frasi", "up", "speak up = parlare senza paura",
      "Speak ___: tell a teacher.", instr="Completa")
```

- Verified by `diff pre/content56.py` vs edited file: exactly 1 line differs.
- No other source file changed: all other `content*.py`, `bslib4.py`, `svglib.py`,
  `run.py`, `render.py`, `dump_reg.py`, `ABSTRACT.txt` keep their 11 Nov 11:54 mtimes.
- No map/translation file touched (none exists for this delta — the key comes from core).
- Rebuild used the edition's own scripts: `run.py` → `dump_reg_delta.py` (repointed
  copy of `dump_reg.py`, output to this scratch) → `render.py` → `make_textmd_delta.py`
  (repointed copy of `fanout/it/make_textmd_w47.py`, registry from this scratch) →
  `tools/webpdf.py`. No commit, no push.

## 3. Diff evidence (exactly 1 + exactly 1)

- **Registry:** pre vs re-dumped — exactly **1** differing entry:
  `n=73 key 'speak' → 'up'`, note identical, all other fields identical.
  Per-page 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22 (unchanged).
- **text.md:** pre vs re-export — exactly **1** differing line (1151):
  `73. [A2] Completare le frasi — speak (speak up = parlare senza paura)` →
  `73. [A2] Completare le frasi — up (speak up = parlare senza paura)`.
  Re-export: 498 recorded blocks, stub registry 150 = real registry 150.
- **SVG scope (corrected expectation — see §7 note 7):** post-run SHA comparison vs pre —
  ONLY `svg/p8-test.svg` changed (its ANSWERS block prints the key). The other 7 SVGs
  are byte-identical to pre. **P5 unchanged is correct and expected:** the Q73 key
  only ever prints on the P8 answers page; P5 prints only the `Speak ___` blank plus
  the `speak up` note, so the key change cannot touch P5. (en-es delta confirmed the
  same pattern: p8 carries `73. up`, p5 unchanged.) Not an anomaly, no rework.

## 4. Q73 four-source consistency (all `up`)

| Source | Q73 evidence |
|---|---|
| registry (`registry.json`, n=73) | `key: 'up'`, `note: 'speak up = parlare senza paura'` |
| text.md (line 1151) | `73. [A2] Completare le frasi — up (speak up = parlare senza paura)` |
| P8 printed key (fresh `p8.py extract`, `gates/p8-extract.json`) | `"73": "up"`; P8 render shows `73. up` in the ANSWERS — Pagina 5 — block |
| P5 stem + gloss (print p-5.png + SVG) | `73. Speak ___: tell a teacher.` + gloss `to speak up = parlare senza paura` |
| Core对照 (`core-en/registry.json`, n=73) | `key: 'up'`, `note: 'speak up = 大声说出来'` — matches |

## 5. Gate table (all green)

| Gate | Result | Evidence |
|---|---|---|
| `run.py` | RC=0, TOTAL 150, MODEL 82, 0 OVERFLOW / TOO WIDE; P8-keys 2443/2560, all flows within bottoms | `gates/run.log` |
| `render.py` | RC=0, print PDF 29,327,187 B, 8 cards | `gates/render.log` |
| `webpdf.py` | RC=0, WROTE 2,408,879 B, 49,133 text bytes | `gates/webpdf.log` |
| text.md re-export | RC=0, 53,944 B, 498 blocks, stub 150 = real 150 | `gates/textmd.log` |
| Registry re-dump | RC=0, 150 entries, per-page/level counts unchanged | `gates/dump_reg.log`, `registry.json` |
| Occlusion audit (real command, no `--selftest`) | RC=0, **0 flags** (selftest OK: all 6 planted classes fired, clean controls silent) | `gates/occlusion.log`, `gates/occlusion.json` |
| p8 extract (core + edition) | 60/150 noted each, **same set** as core | `gates/p8-extract-core.log`, `gates/p8-extract.log` |
| p8 compare | **CLEAN**, missing=[] extra_count=0 uncertain=[], keydiff=[137, 138, 139, 140, 150] (expected reader-language keys) | `gates/p8-compare.json/.log` |
| keycheck (canonical, repointed copy) | RC=0, registry-vs-p8extract **149/150** exc=[150] mismatch=[]; vs core 145/150 (same 5 expected diffs); Q38–41 [b,a,d,c]; Q125 A; Q46 A; Q52 hosted; Q55 won; Q82/83/84 B/C/A; noted set == core; extract keys 150, none missing | `gates/keycheck.log` |
| keycheck (independent re-run, my re-dump + my extract) | Identical figures: 149 exact excl. [150]; same 5 vs-core diffs; noted set == core extract 60/60 | `gates/keycheck-mine.log`, `gates/keycheck-mine-noted.txt` |
| Freeze baseline (CORRECTED invocation: `--build` = edition dir, `--core-svg` = edition svg dir) | RC=0, tool reports **8/8 SVGs byte-identical**, repointed files: none; produced p8 `ba31ef73…` == shipped post-delta p8; edition shipped SVGs unchanged by the run (re-hashed after) | `gates/freeze-edition.log`, `gates/freeze-edition/` |
| Freeze baseline, core read-only对照 (`--build` = core-en, `--core-svg` = core-en/svg) | RC=0, tool reports **8/8 SVGs byte-identical**, repointed files: none; core integrity re-hash OK | `gates/freeze.log`, `gates/freeze-final/` |
| Freeze direct sha256 | **8/8 MATCH** (re-render vs shipped core SVGs) | `gates/freeze-direct.log` |
| Freeze diff | RC=0, TOTAL added CJK **9, all U+3000** (p1: 2, p2–p8: 1 each) | `gates/freeze-diff.log/.json` |
| Print/web text layers | 47,988 chars each (was 47,991, −3 = the one key), token-multiset diff **0**, per-page byte-identical **8/8** (p8 10,243 B vs pre 10,246 B) | `gates/printweb.log` |
| `check_s11.py it` | RC=0, **ALL §1.1/P8 CHECKS PASS** (colour set core 19 = edition 19; badges A2/B1/B2 present; P8 min SVG font 13.5; Q113–120 [A2] tag; "Levels: 145–149 [A2]"; Q120 chip; WRITING head "H　WRITING　Scrittura [B1]") | `gates/check_s11.log` |
| Boxtitle sweep (source) | RC=0, 12/12 fit; tightest HOW LONG? 384.3px margin +20.2 | `gates/boxtitle.log` |
| Boxtitle sweep (SVG) | RC=0, 18/18 fit, 0 overflows | `gates/boxtitle-svg.log` |
| Creambox (canonical `hidden_files/w47/tools/creambox.py`, 8 SVGs) | RC=0, 32 boxes; **log byte-identical to proof1's** (`diff` RC=0). Min inside-only clearance **+5.0px**, zero inside-only negatives. The single desc-clear −1.0px is the same known P2 AND YOU? false alarm as proof1 (last line "redazione." has no descender; baseline clearance +5.0px inside the cream) | `gates/creambox-all.log` |
| `verify_ed.py it` | RC=0, **VERIFY ALL PASS (23/23)** incl. Q39 a / Q40 d / Q46 A / Q52 hosted / Q55 won / Q125 A, "Arsenal are winning", no stale Ashes phrasing, text.md 150 answers | `gates/verify.log` |
| P8 min font | **10.12 pt ≥ 9.75 pt** (verify_ed, PDF spans) | `gates/verify.log` |
| SVG zero real CJK | PASS (only U+3000 allowed) | `gates/verify.log` |
| 8-page visual | Print p-1…p-8 @110dpi all read: no overlap, no spill, no missing content; footers "Pagina n di 8" all present. Web P1/P8 match print P1/P8 | `render/p-*.png`, `render/w1-1.png`, `render/w8-8.png` |
| D5 fonts (record only, not judged) | Print 41 objects / 7 families — DejaVuSans ×1, Newsreader16pt-Italic ×1, Newsreader16pt-Regular ×16, NotoSansCJKsc-Bold ×8, NotoSansCJKsc-Regular ×8, NotoSerifCJKsc-Regular ×6, UnifrakturMaguntia ×1 (identical counts to proof1). Web 41 objects / 8 Lucerna-renamed families | `gates/fonts-print.txt`, `gates/fonts-web.txt` |

## 6. 150-key stem/adaptation re-check (Q73 lesson: three-source agreement is not enough)

Re-checked **all 70 fill-in/rewrite items** (34 Completare le frasi + 16 Trasformazione
+ 8 Completa il testo + 7 single-word types [Comparativi 1, Passato 2, Futuro 1,
Tempi verbali 1, Subordinate 1, Frasi d'oro 1] + 5 Dialogo) for key-fits-blank:

- 53 literal `f.ex` (key, stem) pairs parsed from `content12/34/56/7.py`, each read
  against its stem — all fit (e.g. Q73 `up` → "Speak up: tell a teacher.";
  Q58 `silence` → "Break the silence: speak up about bullying.";
  Q46 `eight` → "___ singles players play in Turin.").
  Full list in `gates/stem-key-fill.txt`.
- P8 battery Q94–99 (`certify/call/changed/takes/differs/official`) — same stems as
  the P6 items, keys fit.
- Cloze Q112–119 read against the P8 passage + options — all 8 unique fits
  (112 Tuesday / 113 call / 114 continues / 115 will meet / 116 writes /
  117 will certify / 118 wears / 119 will watch).
- Dialogue Q145–149 — all fit (145 row / 146 film / 147 popcorn / 148 show /
  149 Friday, confirmed by the dialogue's own answers "The front row", "Yes, Friday").
- P8 D-block Q133–136 (`will meet/won/more/whether`) — fit their (verb) prompts.
- All other keys unchanged since proof1's full 150/150 three-source hand verification;
  nothing else was re-checked beyond the fill-in/rewrite set above.

**No new defects found.**

## 7. Notes / observations

1. **Creambox invocation:** the tool takes SVG *files*, not a directory (first call
   passed the dir and failed with IsADirectoryError; re-ran with the 8 file paths,
   RC=0). Result log is byte-identical to proof1's.
2. **keycheck reference path:** the canonical `keycheck_ed.py` reads the archived
   noted set from `scratch-fanout-en/core-noted-set.json` (not `scratch-fanout-en2/`,
   as the old `gates.sh` snippet says). My independent re-run first used the wrong
   path and errored only on that line; corrected to compare against my fresh core
   extract — 60/60 identical either way. Figures agree in both runs.
3. **Core-en observation (not touched by this delta):** core-en `content56.py` hash is
   unchanged since my first measurement (`4ed43ff8…`, includes the fix2 Q73 `up`).
   Core-en's shipped PDFs/text.md differ from proof1's reference SHAs (print
   `08cbc1e5…` vs proof1 `b484e007…`, 41,407,287 B; text 51,402 B) with mtimes
   2026-11-11 14:33–14:37 — i.e. the core-en fix2 rebuild, which predates this delta.
   Freeze baseline 8/8 + direct sha 8/8 prove the current core is self-consistent;
   this delta wrote nothing to core-en.
4. **`dump_reg.py` repointing:** the edition's `dump_reg.py` hardcodes its output to
   the fanout scratch; I ran a repointed copy in this scratch (and fixed its
   `os.chdir` to the edition dir — the copy's own dir has no content files) and
   copied the fresh registry into the edition. Same pattern as proof1's repointed
   `make_textmd_proof.py`.
5. **git:** no commit, no push (coordinator's job — 10 editions in parallel). The
   edition dir is untracked (`??`) in the repo, same as at proof1.
7. **Brief correction applied (11 Nov, after the delta):** SVG scope expectation
   corrected — Q73's key only prints on the P8 answers page, so **only p8 changing
   with p5 byte-identical is correct and expected** (P5 prints only the `Speak ___`
   blank + the `speak up` note); not an anomaly, no rework. en-es delta confirmed
   the same pattern. Freeze invocation likewise corrected: baseline `--build` is the
   edition's own build dir (contains `run.py`), core comparison is a separate
   read-only对照 via the core-svg path. Re-run under the corrected invocation:
   edition baseline **8/8** (`gates/freeze-edition.log`) + core baseline **8/8**
   (`gates/freeze.log`) + direct sha **8/8** — all green, conclusion unchanged.
6. **KIT updated:** `WEEKLY-KIT.md` §2 (new SHAs/sizes) + §3 gate header/char count +
   §5 item 6 (delta entry). No other KIT section changed.

## 8. Files in this scratch

- `DELTA-NOTE.md` (this file), `probe.txt`
- `pre/` — pre-change `registry.json`, `2026-w47-en-it.text.md`, `content56.py`,
  `svg-sha256.txt`, `sha256.txt`
- `registry.json` — fresh re-dump (== edition copy, `cmp` verified)
- `dump_reg_delta.py`, `make_textmd_delta.py`, `keycheck_delta.py` — repointed helpers
- `gates/` — `run.log`, `render.log`, `webpdf.log`, `textmd.log`, `dump_reg.log`,
  `occlusion.log/.json`, `p8-extract-core.log/.json`, `p8-extract.log/.json`,
  `p8-compare.log/.json`, `keycheck.log`, `keycheck-mine.log`,
  `keycheck-mine-noted.txt`, `freeze.log`, `freeze-direct.log`,
  `freeze-diff.log/.json`, `freeze-final/`, `freeze-edition.log`,
  `freeze-edition/`, `printweb.log`, `check_s11.log`,
  `boxtitle.log`, `boxtitle-svg.log`, `creambox-all.log`, `creambox-rawneg.txt`,
  `creambox-rawneg-proof1.txt`, `verify.log`, `fonts-print.txt`, `fonts-web.txt`,
  `stem-key-fill.txt`, `svg-sha256-post-run.txt`, `svg-sha256-final.txt`,
  `svg-sha256-post-freeze.txt`,
  `pdftoppm.log`, `pdftoppm-web.log`, `pdftoppm-web1.log`
- `render/` — print `p-1.png`…`p-8.png`, web `w1-1.png`, `w8-8.png` (@110dpi)
- `tmp/` — TMPDIR for the runs
