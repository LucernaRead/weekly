# DELTA-NOTE — Lucerna Weekly 2026-W47, edition en-nl (Q73 speak→up delta)

- **Edition:** English target, Dutch reader (`production/2026-w47/2026-w47-en-nl/`)
- **Date:** 2026-11-11 (Toronto, America/Toronto)
- **Scope:** one-key sync only. core-en fix2 changed Q73 key `"speak"` → `"up"`
  (stem "Speak ___: tell a teacher.", note `speak up = …` unchanged). This edition synced
  the same key in `content56.py:49` only, then rebuilt + fully re-gated.
- **No commit / no push** (10 editions in parallel; git ops by the coordinator).

## 1. Pre-change verification (all matched the task values — work proceeded)

| file | size (B) | SHA-256 |
|---|---|---|
| print `The-Lucerna-VOL4-en-nl.pdf` | 29,341,272 | `a5957d64e727662c0d4763596af517f0eae324471b93a4bd9dadb304c03bc136` |
| web `The-Lucerna-VOL4-en-nl.web.pdf` | 2,411,538 | `ee3d98baba20febe72c297ccb2591055991d4ed9b341b1429b6c7748b3371193` |
| `2026-w47-en-nl.text.md` | 53,568 | `baecaf6e92ff837857e3d6d7dd7ae28f2b1fbb15b8be78bec9428a83c13be459` |

All three equal the full SHAs in proof1's PROOF-NOTE (`scratch-proof-en-nl1/`).
Probes before any work: `/dev/null` present, `git hash-object -w` OK, probe file written
in this scratch dir.
Three-source pre-state confirmed (expected: all three still wrong together):
- registry.json Q73: `{'n': 73, 'page': 5, 'level': 'A2', 'type': 'Zinnen aanvullen', 'key': 'speak', 'note': 'speak up = je uitspreken'}`
- text.md line 1151: `73. [A2] Zinnen aanvullen — speak (speak up = je uitspreken)`
- P8 extracted from the print PDF: `… 73. speak · 74. d …`
- core-en `content56.py:49` (read-only): key `"up"` — core fix2 already in place, untouched.

## 2. The only change

`content56.py:49` — one token:
```diff
-f.ex("A2", "Zinnen aanvullen", "speak", "speak up = je uitspreken",
+f.ex("A2", "Zinnen aanvullen", "up", "speak up = je uitspreken",
      "Speak ___: tell a teacher.", instr="Vul in")
```
Note and stem untouched. No other source line changed (only `content56.py` has a new
mtime among `content*.py`/`bslib4.py`/`svglib.py`; no map/translation/ABSTRACT/KIT
file touched except the KIT SHA+delta entry in §2/§5/§9, see §7).
Rebuild: edition's own `run.py` → `render.py` → registry re-dump → `make_textmd_delta.py`
(text.md) → `tools/webpdf.py` (web PDF). Logs: `delta-build.stdout.log`.

## 3. Post-change file identity

| file | size (B) | SHA-256 |
|---|---|---|
| print `The-Lucerna-VOL4-en-nl.pdf` | 29,341,267 | `f1e1e511bd780243878f767c73d92f22ff6407718fbde7dbe209068938e87dca` |
| web `The-Lucerna-VOL4-en-nl.web.pdf` | 2,411,546 | `c1a0828865d9a293b7e2be1e3f6cec674f7b1f1ca8193049c2c43906e1c509a8` |
| `2026-w47-en-nl.text.md` | 53,565 | `30bfb6f93860fae5ae58707c28c4f2e3a18ebcc07e272681e67688451d12c0be` |

Both PDFs 8 pages, 1462.5 × 2025 pts.

## 4. Diff evidence (exactly 1 change each)

- **registry diff: exactly 1 entry** — n=73 `key: 'speak'` → `'up'`; all other 149 entries
  byte-identical; total still 150 (pages 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22).
- **text.md diff: exactly 1 line** — line 1151:
  `73. [A2] Zinnen aanvullen — speak (speak up = je uitspreken)` →
  `73. [A2] Zinnen aanvullen — up (speak up = je uitspreken)`.
- **SVG scope: only p8-test.svg changed.** SHA-256: p1–p7 byte-identical to pre-change;
  p8 `530c9d35…` → `ee35fc68…`. The single differing region (stripped-text bytes
  34413–34944) is exactly `73. speak` → `73. up` plus the reflow of the same answer
  words onto the following lines (`76. b …`, `socks today.`, `We are …` — no word added,
  removed, or altered). All 8 embedded images identical (hashes unchanged).
  P5 is byte-identical to pre-change **by design, and this is the correct expectation**
  (brief correction, confirmed by the en-es delta): the Q73 key only ever prints on the
  P8 answers page; P5 prints only the stem `Speak ___` and the `speak up` note, never
  the key itself. p8-only change is correct — p5-unchanged is NOT an anomaly and needs
  no rework.

## 5. Q73 four-source evidence (all `up`)

| source | evidence |
|---|---|
| registry.json | Q73 `key: 'up'`, note `speak up = je uitspreken` |
| text.md (line 1151) | `73. [A2] Zinnen aanvullen — up (speak up = je uitspreken)` |
| P8 printed key (SVG + print PDF + web PDF text layer) | `… 72. rights (right = een recht) · 73. up · 74. d · 75. a · 76. …`; `73. speak` absent from P8 SVG |
| P5 stem + note (p5-youth.svg) | stem `Speak ___: tell a teacher.` present; gloss `to speak up = je uitspreken` present (split across two `<text>` elements: `… to speak up` / `= je uitspreken · …`); `73. speak` as a key absent |

Registry vs text.md appendix: **0 mismatches / 150**. Registry vs P8-extracted keys:
150/150 extracted, **1 diff — n=150 only**, the known extractor truncation of the
open-question long label (registry `Open vraag — punten in het schrijfblok; …` vs
extracted `Open vraag`), same as proof1.

## 6. Gates (all re-run fresh on the new build; logs in `gates/`)

| gate | result |
|---|---|
| run.py | RC=0; TOTAL 150; MODEL 82 words; **0 OVERFLOW / TOO WIDE**; all Flow ends ≤ bottom (P8-keys 2375/2560) |
| render.py / webpdf.py | RC=0 / RC=0 |
| occlusion audit (real command, not --selftest) | selftest OK (all 6 classes fired, clean controls silent); **0 flags** |
| p8 extract (core + edition) | edition 150 keys; noted set 60/150, **identical to core's set** |
| p8 compare (`p8-compare.json` read in full) | **status CLEAN**; missing=[]; extra=[]; keydiff=[137, 138, 139, 140, 150] (reader-language translation keys + writing key — expected) |
| keycheck.py | RC=0; REG 150, p8extract 150, exact match **149/150** (only n=150, known exception) |
| freeze baseline (edition build) | `--build` = edition dir (contains run.py), `--core-svg` = edition svg: **8/8 SVGs byte-identical** (scratch-copy rebuild reproduces all 8 shipped SVGs, incl. new p8 `ee35fc68…`); shipped edition SVGs unchanged by the run. Log: `gates/freeze-edition.log`, JSON `gates/freeze-edition.json` |
| freeze baseline (core, read-only) | `--build` = core-en, `--core-svg` = core-en/svg: **8/8 SVGs byte-identical**; direct sha256 re-render vs shipped core SVGs **8/8 MATCH**; core integrity unchanged by the run |
| freeze diff | added CJK = **9× U+3000 only** (same as proof1) |
| print/web text layer | 48,041 chars each (was 48,044: −3 for speak→up); token-multiset diff **0/0**; per-page pdftotext **byte-identical p1–p8** |
| check_s11.py (nl) | RC=0, **ALL §1.1 / P8 CHECKS PASS**; colour set core 19 = edition 19; badges A2/B1/B2 present; P8 min font **13.5 pt** (≥10 required) |
| boxtitle sweep (source) | 12/12 fit; tightest HOW LONG? +20.3, ODD SOCKS +20.6 |
| boxtitle sweep (SVG) | 18/18 fit; overflows 0 |
| creambox raw | 0 OVERFLOW |
| creambox inside-only (strict, own content) | all 32 `#f0eee5` boxes POSITIVE clearance (+5.0 to +92.4); tightest P2 y=1211 +5.0 — same as proof1 (P2 byte-identical). The en-ja script's descender heuristic flags that one box at −1.0; baseline clearance is +5.0, unchanged from the proof1 PASS |
| D5 fonts (count only, not judged) | Newsreader 1023, Noto Sans CJK SC 663, Noto Serif CJK SC 27, DejaVu Sans 4, UnifrakturMaguntia 1 — identical to proof1 |

## 7. Fill-in / rewrite key-fit review (Q73 lesson: three-source agreement is not enough)

All 50 "Zinnen aanvullen" (34) + "Zinnen omvormen" (16) entries re-checked stem-by-stem
against their source `ex()` calls (AST parse of content*.py + the `d_items` loop in
content8.py for Q133–136); full table in `fillin-rewrite-check.txt`. **50/50 fit.**
Spot highlights: Q73 `up` in "Speak ___: tell a teacher." (speak up = tell a teacher —
correct phrasal verb); Q70 `silence` / "Break the ___: speak up about bullying.";
Q79 `Children are speaking up this week.` (speak → are speaking); Q133 `will meet`,
Q134 `won`, Q135 `more` ("254 is ___ than 218."), Q136 `whether`; Q107 `win`
('"Democrats ___ the House" is a headline.' — headline present tense, correct).
Pre-existing duplicates carried over unchanged from proof1 (a) and not flagged:
Q6/Q12 share the stem "The new Congress meets in ___ 2027."; Q2/Q95 share key `call`;
Q5/Q96 share key `changed` (different pages/levels).

## 8. Visual check (fresh 100-DPI renders from the new print PDF, `render/`)

All 8 pages viewed: no overflow, overlap, clipping, or cut-off text; footers
"Pagina N van 8" on all pages. Old-vs-new pixel diff (threshold >30):
**P1–P7 0.00% (pixel-identical)**, **P8 0.14%** (confined to the Q73 answer reflow).
Web-vs-print pixel diff is identical to the old build (P1 0.443%, P8 0.152% — pre-existing
font-subsetting rendering artifact, unchanged by this delta); text layers are
byte-identical per page. P5: Q73 stem + gloss clean; the widowed "D PRESENT CONTINUOUS"
head at the bottom of column 2 is the carried-over proof1 observation (P5 pixel-identical).
P8: ANSWERS block prints "73. up" and ends well above the footer; MODEL box clean.

## 9. Core integrity

core-en was NOT touched by this agent (read-only). Its fix2 SHAs measured after the
delta differ from proof1's values by design (fix2 rebuild):
print `08cbc1e5…` 41,407,287 B (was `b484e007…` 41,407,278 B);
web `d7927ead…` 2,804,281 B (was `7277e32a…` 2,804,271 B);
text `23855d4b…` 51,402 B (was `e368828a…` 51,405 B; −3 = speak→up).
core-en `content56.py:49` verified key `"up"` before the delta.

## 10. KIT + conclusion

- `WEEKLY-KIT.md` updated: §2 new SHAs/sizes, §5 delta entry (Q73 speak→up, only change),
  §9 delta log pointer. No other repo-side file was written.
- **Conclusion: delta complete, all gates green — ready for proof2.**
  Single-key change, verified in all four sources, rebuild confined to one SVG page,
  no other edition/core/tool touched.
