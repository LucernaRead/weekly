# FIX REPORT — Lucerna Weekly W46 JA family, Round 1 defects

- Issue: VOL.3, dated Mon 2026-11-09 to Sun 2026-11-15 (9–15 Nov 2026).
- Scope: all 11 JA-target editions — `2026-w46-ja-de, -en, -es, -fr,
  -it, -ko, -nl, -pt, -ru, -zh-cn, -zh-tw`. The directory
  `files/weekly-report-w46-ja-core/` IS the zh-cn edition.
- Authority: the independent proofreader's Round 1 verdict
  (`hidden_files/w46/ja-proofread-gates/proofreader-verdict-round1.md`):
  FAIL for all 11 editions. Blocking defects D-CORE-01, D-CORE-02
  (all 11); D-ZHTW-01, D-ZHTW-02 (zh-tw only).
- Seed record (delivered by the proofreader, not re-derived): VOL.3,
  150 exercises (A2 46 / B1 75 / B2 29).
- Fix worker: 2026-11-02/03. Worked locally only: nothing pushed,
  inserted, or posted; `~/workspace/weekly-git` and `index.json`
  never touched; no rendered SVG/PDF hand-edited; every change went
  through source files and a full re-render; `.text.md` files
  regenerated via `hidden_files/w46/make_textmd.py`, never hand-edited
  or extracted from PDF.
- Status: all four verdict defects fixed at the source, all 11
  editions re-rendered and re-gated on the final artifacts. **A Round 2
  independent proofread is still required; this re-gating does not
  replace it.**

## 1. D-CORE-01 — kinsoku LINE-END violations (BLOCKING, frozen core, all 11)

Source file: `hidden_files/weekly-report-w46-ja-build/svglib.py`,
function `wrap()`.

Root cause: `wrap()` enforced only line-START kinsoku (NO_START
pull-down) and had no line-END rule, so greedy CJK wrapping could
strand an opening bracket at a line end.

Fix (in `wrap()`, after the existing NO_START loop, before the
seam-repair block): a NO_END block with
`NO_END = "（「『〔【《〈([`. For each line except the last, while the
line ends with a NO_END character and has length > 1, the trailing
character is moved to the head of the next line and the shortened line
is rstripped. Pure character move, no width measurement, so the
TC-face plumbing in `hidden_files/w46/gen_ja_zhtw.py` (which patches
`wrap()` by exact strings above/below this block) is unaffected; all
`gen_ja_zhtw.py` anchor strings were verified intact. This wrap-level
fix was chosen over shortening the two stems (both options were
offered by the verdict) because it preserves all visible text
byte-identically except line splits and fixes the defect class.

`svglib.py` md5: `d73e23b365676c3618d7e060b835eb4d` →
`74177544422fe677639d769cd80499fb`. `CANON_SVGLIB_MD5` was updated to
the new value in all 10 guard files: the 9 fan-out `transform.py`
files (`hidden_files/weekly-report-w46-ja-{de,en,es,fr,it,ko,nl,pt,ru}-build/`)
and `hidden_files/w46/gen_ja_zhtw.py` (1 occurrence each, 0 old values
remaining, verified by grep). These transforms copy `svglib.py`
verbatim from the core build and assert the md5; without the update
every fan-out rebuild would have failed.

Before/after (line splits only; the two defect sites):

- P1 quiz item 8 (`p1-hyoushi.svg`, was y=2419.0):
  BEFORE line 1: `七五三の中心の日はいつですか。 A. 9日（`
  BEFORE line 2: `月） · B. 11日（水） · C. 15日（日）`
  AFTER line 1: `七五三の中心の日はいつですか。 A. 9日`
  AFTER line 2: `（月） · B. 11日（水） · C. 15日（日）`
  (`A. 9日（月）` now intact on one line.)
- P3 item 32 (`p3-bunka.svg`, was y=2163.2):
  BEFORE line 1: `二の酉はいつですか。 A. 19日（木） · B. 7日（`
  BEFORE line 2: `土） · C. 15日（日）`
  AFTER line 1: `二の酉はいつですか。 A. 19日（木） · B. 7日`
  AFTER line 2: `（土） · C. 15日（日）`
  (`B. 7日（土）` now intact on one line.)

Isolation verification before rebuilding (tools venv python, `wrap()`
on the exact strings at size 21/19, width 434) produced exactly the
AFTER splits above; P1Q9, which already started its second line with
`（土）`, was unchanged. Core re-render text diff (old `.text.md`
lines vs new SVG `<text>` multiset, before regenerating text.md):
exactly 4 lines changed (the 2 defect sites, 2 lines each), 1302
texts total, count unchanged. No other core text moved.

Line-END kinsoku scan after re-render (proofreader's definitions,
`ja-fix/kinsoku_scan.py` — rebuilt as a verbatim copy of the
proofreader's `kinsoku_orphan_scan.py` with only the output path
changed, verified by diff; output `ja-fix/kinsoku-orphan.json`):

| edition | kinsoku_start | kinsoku_end | orphan |
|---|---|---|---|
| zh-cn | 0 | 0 | 0 |
| de | 0 | 0 | 0 |
| en | 0 | 0 | 0 |
| es | 0 | 0 | 0 |
| fr | 0 | 0 | 0 |
| it | 0 | 0 | 0 |
| ko | 0 | 0 | 0 |
| nl | 0 | 0 | 0 |
| pt | 0 | 0 | 0 |
| ru | 0 | 0 | 0 |
| zh-tw | 0 | 0 | 0 |

No new wrap orphan was introduced. P1 ×11 and P3 ×11 cards were
visually checked at full frame: both rewraps render correctly, no
overflow, no overlap, no tofu.

## 2. D-CORE-02 — ABSTRACT.txt news framing (BLOCKING, all 11)

Source: `ABSTRACT.txt` in each edition folder (no build script
generates these; transforms/generators do not touch them). Edited
directly in the edition folders. Everything before the tail preserved
verbatim; zh-cn/zh-tw tails merged to avoid duplicating the 150 count.
Full before/after texts:
`hidden_files/w46/ja-fix/abstracts-before-after.txt` (BEFORE taken
from the proofreader's `abstracts.txt`, verified byte-identical to the
pre-fix files).

| edition | BEFORE tail (prohibited) | AFTER tail (practice framing) |
|---|---|---|
| zh-cn | 共150道练习，适合想通过读日语新闻学日语的读者。 | 共150道以本周话题为素材的练习。 |
| zh-tw | 共150道練習題，透過真實日本新聞學日語。 | 共150道以本週話題為素材的練習題。 |
| en | 150 exercises for readers learning Japanese through real Japanese news. | 150 exercises built from this week's topics. |
| de | 150 Übungen für alle, die Japanisch durch echte japanische Nachrichten lernen. | 150 Übungen zu den Themen dieser Woche. |
| es | 150 ejercicios para aprender japonés con noticias japonesas reales. | 150 ejercicios construidos a partir de los temas de esta semana. |
| fr | 150 exercices pour apprendre le japonais à travers de vraies nouvelles japonaises. | 150 exercices construits à partir des sujets de cette semaine. |
| it | 150 esercizi per imparare il giapponese con vere notizie giapponesi. | 150 esercizi costruiti sui temi di questa settimana. |
| ko | A2부터 B2까지 150개의 연습 문제를 통해 실제 일본 뉴스로 일본어를 배웁니다. | A2부터 B2까지 이번 주 주제를 소재로 한 150개의 연습 문제가 수록되어 있습니다. |
| nl | 150 oefeningen om Japans te leren met echt Japans nieuws. | 150 oefeningen op basis van de thema's van deze week. |
| pt | 150 exercícios para aprender japonês com notícias japonesas reais. | 150 exercícios construídos a partir dos temas desta semana. |
| ru | 150 упражнений для изучающих японский по настоящим японским новостям. | 150 упражнений, составленных по темам этой недели. |

Post-rewrite verification (final state re-checked 2026-11-03,
`ja-fix/abstract-checks-final.log`): each file is exactly one line
plus trailing newline, contains no ASCII double-quote, contains 150,
A2 and B2, and contains none of the banned news-framing tails — all
11 OK. (A space-before-comma slip introduced in the first ru write,
`упражнений, составленных`, was found and corrected before the final
check; the corrected full text is the one in the table above.)

## 3. D-ZHTW-01 / D-ZHTW-02 and 6 further same-class residue strings (zh-tw only)

Source: `hidden_files/w46/maps/zh-tw.json`. The zh-tw generator
applies the MAP as quoted-literal replacements over the core content
files; the 2 listed strings were simply absent from the MAP (179
entries, neither key present). The MAP grew 179 → 187 entries.

| # | BEFORE (Simplified residue) | AFTER (Traditional) | location |
|---|---|---|---|
| 1 (D-ZHTW-01) | 得到东西的场所用「で」。 | 得到東西的場所用「で」。 | P7 clinic note, `p7-kotoba.svg` (was y=784.04) |
| 2 (D-ZHTW-02) | 在酉の市买熊手 | 在酉の市買熊手 | P8 key 42, `p8-tesuto.svg` (was y=1428.984) |
| 3 | 看的场所用「で」。 | 看的場所用「で」。 | P7 clinic note, sibling of #1 |
| 4 | 场所用「で」 | 場所用「で」 | P8 key 135 note, `content8.py:64` |
| 5 | 2026年没有三の酉 | 2026年沒有三の酉 | P8 key 33 note, `content34.py:73` |
| 6 | 新小结是美ノ海 | 新小結是美ノ海 | P8 key 59 note, `content34.py:195` |
| 7 | 「千歳飴」受欢迎 | 「千歳飴」受歡迎 | P8 key 148 note, `content8.py:94` |
| 8 | 口号是「静かだけど、冒険中。」 | 口號是「静かだけど、冒険中。」 | keys 103 and 128, `content7.py:24` and `content8.py:47` (two rendered occurrences, one source string) |

**Refutation of a verdict claim (flagged for the parent and Round 2):**
the verdict states its full Simplified-only scan found exactly the 2
listed strings and all other core SC strings were converted. That
claim is FALSE on the evidence in the pre-fix artifacts. A full
enumeration of the pre-fix zh-tw SVGs (see §3.1) found the 6
additional strings #3–#8 above. They are the same defect class, same
cause (MAP gap), same fix mechanism. Fixing them was necessary
because the task requires the post-fix full scan to confirm 0
Simplified-only characters remain, which would be false if they were
left. No other changes were made beyond these 8 MAP entries. The
other two mixed clinic notes ("地点＋へ＋动词",
"动词名词化时要加「こと」。") were already in the MAP, which is how
the earlier pass missed the remaining ones.

### 3.1 Simplified-only scan method (corrected)

An initial scan definition (SC-only = OpenCC s2t-differing AND absent
from the core repertoire) was tried and DISCARDED: it reported 0
candidates while residue was present, because the core IS the zh-cn
edition and its repertoire contains Simplified explanation
characters. Do not reuse it. Its output file `sc-scan-BEFORE.json` is
misleading and must not be cited as evidence.

Correct method: enumerate the full universe of characters in the
zh-tw SVGs whose OpenCC `s2t` form differs (OpenCC is available in
`tools/venv/bin/python`; system `python3` has no `opencc` module).
Pre-fix universe: 27 chars, 190 occurrences, dumped in full with
page/y/string for every occurrence to
`hidden_files/w46/ja-fix/sc-occurrences-BEFORE.txt`. Adjudication:
21 chars are legitimate Japanese shinjitai or deliberate keeps
(会内写参号国学寝届峡当数来横浅温点画祷里静 — e.g. 当 in frozen
Japanese `本当の調査`, 号 in `第3号`/`前号`, all 写真/数字/祈祷/横浜
forms); 6 chars occur ONLY in residue strings (东买场欢没结); 号
additionally occurs in the Chinese segment `口号是` (residue) as well
as legitimately in Japanese segments.

Post-fix adjudicated scan (`ja-fix/sc_scan.py`, output
`ja-fix/sc-scan-AFTER.json`, run on the final artifacts):
**VERDICT: 0 Simplified-only characters remain** — residue-char hits
0, residue strings present 0 of 8, all 8 Traditional forms present.
Remaining s2t-differing characters: 21 —
会内写参号国学寝届峡当数来横浅温点画祷里静 (the adjudicated
legitimate set; 号 now occurs only in legitimate Japanese segments).

Post-rebuild spot check: all 8 Traditional forms present in the
rebuilt zh-tw SVGs; grep for the 8 Simplified patterns across all
zh-tw SVG pages returned 0 hits on every page. P7 and P8 zh-tw cards
visually checked at full frame: clinic notes and P8 keys
33/42/59/103/128/135/148 render in Traditional with no overflow,
overlap, or tofu.

## 4. Rebuild and regeneration (all 11)

- Pre-fix snapshot: `hidden_files/w46/ja-fix/before-sha256.txt`
  (132 files: all SVGs, PDFs, text.md files, ABSTRACT.txt files).
- Core rebuild: `run.py` exit 0, TOTAL 150, A2 46 / B1 75 / B2 29,
  by page 10/18/18/18/18/18/12/38, model chars 154, 0 FLOW OVERFLOW
  / HEAD TOO WIDE warnings. `render.py` exit 0, 8 cards, print PDF
  `Lucerna-VOL3.pdf` 24,795,355 bytes. Logs:
  `render-logs/core-run.log`, `render-logs/core-render.log`.
- Fan-out rebuild via `hidden_files/w46/ja-fix/rebuild-fanouts.sh`:
  all 9 `transform.py` runs exit 0, zh-tw `gen_ja_zhtw.py` (plain
  `python3`, per its KIT) exit 0 transforming 9 files, all 10 `run.py`
  runs exit 0 with identical registry counts (TOTAL 150, A2 46 /
  B1 75 / B2 29, by page 10/18/18/18/18/18/12/38, model 154), 0
  overflow warnings in every run log, all 10 `render.py` runs exit 0.
  Full log: `render-logs/rebuild-summary.txt`; per-edition logs in
  `render-logs/`.
- `.text.md` regenerated for all 11 via `make_textmd.py` with week
  label `2026-W46 (9–15 Nov 2026)` and the pre-existing slugs;
  headers verified verbatim (`# <slug>`, blank,
  `Week: 2026-W46 (9–15 Nov 2026)`).
- Web PDFs via `tools/webpdf.py` only, driver
  `hidden_files/w46/ja-fix/build-webpdf.sh`. The background driver
  was aborted by a tool poll during the zh-tw run: 10 of 11 web PDFs
  had completed (exit 0), the zh-tw web PDF was still the pre-fix
  file with a truncated log. The zh-tw web PDF was re-run standalone
  (same command, same tool) and completed exit 0: 2,872,565 bytes,
  44,817 text bytes. The re-run is noted in
  `render-logs/webpdf-summary.txt`; its log is
  `render-logs/webpdf-zh-tw.log`.

## 5. Re-gate results on the FINAL artifacts

Driver: `hidden_files/w46/ja-fix/run_gates.sh` (freeze baseline +
`--strict-cjk` diff, p8 compare, occlusion audit; log
`ja-fix/gates-run.log`). Kinsoku/counts/SC scans: `ja-fix/kinsoku_scan.py`
(verbatim copy of the proofreader's scan, output path only changed),
`ja-fix/counts_checks.py` (output `ja-fix/counts-checks.json`),
`ja-fix/sc_scan.py` (output `ja-fix/sc-scan-AFTER.json`). PDF checks:
`ja-fix/pdf-checks.log`.

- Freeze baseline: 8/8 SVGs byte-identical (`ja-fix/freeze-baseline.json`,
  ok 8). Freeze diff `--strict-cjk`: exit 0 with 0 added CJK for
  zh-cn/de/en/es/fr/it/nl/pt/ru. ko exit 1, adjudicated legitimate:
  308 added distinct chars, set identical to Round 1, ALL Hangul, 0
  new Han, 3,464 added instances. zh-tw exit 1, adjudicated: added
  distinct set identical to Round 1 (158 chars, all Traditional /
  Japanese repertoire, including 將/請/講/輯); total added instances
  849 vs 839 in Round 1, delta exactly +10 = 場+3, 東+1, 歡+1,
  沒+1, 結+1, 號+2, 買+1 — the 8 MAP conversions in §3, no other
  change. (`ja-fix/freeze-<code>.json`.)
- p8 compare: CLEAN 150/150 for all 11 editions, missing/extra/
  uncertain all empty. keydiff: zh-cn []; zh-tw [138];
  de/en/es/fr/it/ko/nl/pt/ru [137, 138] — all adjudicated legitimate
  redirects, identical to Round 1. (`ja-fix/p8compare-<code>.json`;
  core extract `ja-fix/p8extract-core.json`, noted set 150/150.)
- Occlusion audit: 0 flags in all 11 editions; the tool runs its
  synthetic selftest first and refuses to report if it fails.
  (`ja-fix/occlusion-<code>.json`.)
- Kinsoku: 0 / 0 / 0 (start / end / orphan) in all 11 editions (§1).
- Counts (all 11): stems 1–150 complete; P8 keys 1–150 complete;
  level chips raw count A2 44 / B1 74 / B2 27 (145; the run-log
  registry counts A2 46 / B1 75 / B2 29 are the authoritative split,
  identical to the seed record); P6 bars 480/720/780/1020 at x=315
  (= 30×16/24/26/34) with labels 山 34%, 神社 26%, 公園 24%,
  町 16% and the practice-data label, all present; P7 golden phrases
  8, verbatim, exactly 2× each (article + P7 list), present on the
  source page and on P7; keys-flow end-y per edition in §6 notes
  (identical to Round 1 values); badges: core none (badge-less
  subtitle design, adjudicated not a defect), fan-outs correct at
  x=975/y=356.
- PDFs: every web PDF ≤ 7 MB; pdftotext bytes > 0 on every web PDF;
  web-vs-print pdftotext byte-identical for all 11; pdftotext byte
  counts identical to the Round 1 values for every edition.
  (`ja-fix/pdf-checks.log`; sizes in §6.)
- Visual: P1 ×11, P3 ×11, P7 zh-tw, P8 zh-tw checked at full frame —
  all clean (rewraps, clinic notes, P8 keys; no overflow, overlap,
  or tofu). Cosmetic items O-01–O-05 and the W45-promise wording
  were not changed, per the task.

## 6. Final per-edition file inventory

(text.md bytes, web PDF bytes + pdftotext bytes; print PDF bytes;
8 SVGs + 8 cards per edition. Source: `ja-fix/final-inventory.txt`
and `ja-fix/pdf-checks.log`.)

| edition | text.md (B) | web PDF (B) | pdftotext (B) | print PDF (B) | keys-flow end-y | p8 keydiff |
|---|---|---|---|---|---|---|
| zh-cn (core) | 44,213 | 2,496,759 | 44,838 | 24,795,355 | 2514.9 | [] |
| de | 46,348 | 2,365,997 | 46,990 | 29,499,992 | 2535.0 | [137, 138] |
| en | 45,541 | 2,318,036 | 46,148 | 27,837,879 | 2532.0 | [137, 138] |
| es | 47,116 | 2,346,157 | 47,774 | 28,725,836 | 2536.2 | [137, 138] |
| fr | 47,029 | 2,344,131 | 47,669 | 28,745,814 | 2535.0 | [137, 138] |
| it | 46,890 | 2,337,474 | 47,549 | 28,720,416 | 2535.0 | [137, 138] |
| ko | 47,930 | 2,395,644 | 48,521 | 26,585,649 | 2520.4 | [137, 138] |
| nl | 46,151 | 2,340,930 | 46,803 | 28,723,676 | 2537.4 | [137, 138] |
| pt | 46,939 | 2,348,975 | 47,570 | 28,727,053 | 2533.5 | [137, 138] |
| ru | 53,626 | 2,254,296 | 54,264 | 24,646,223 | 2524.0 | [137, 138] |
| zh-tw | 44,192 | 2,872,565 | 44,817 | 27,062,370 | 2514.9 | [138] |

Print PDF filenames: `Lucerna-VOL3.pdf` (core),
`Lucerna-VOL3-{DE,EN,ES,FR,IT,KO,NL,PT,RU}.pdf`,
`Lucerna-VOL3-ZHTW.pdf`; web PDFs are the same names with `-web`
before `.pdf`; text.md files are `<slug>.text.md` (core slug
`2026-w46-ja-zh-cn`). The de print PDF is 5 bytes smaller than the
KIT's pre-fix 29,499,997 — expected, from the SVG line-split changes.

## 7. KIT records

A fix record with defect/fix quotes and re-gate evidence was appended
to all 11 `WEEKLY-KIT.md` files: core §11 (new section); fan-outs
§6 Fix history (en had no §6, so one was added). The records note
that the core build's `svglib.py` was intentionally modified for
D-CORE-01 (new md5) and that the "pristine core build" wording in the
fan-out KITs now refers to the pre-fix state; the zh-tw record notes
the MAP grew to 187 entries. All before/after abstract-tail quotes in
the KIT records were verified programmatically against
`abstracts-before-after.txt` and the current `ABSTRACT.txt` files.

## 8. Not changed / adjudications carried

- The core's badge-less subtitle design (matches shipped W45 JA core
  exactly) — not a defect, unchanged.
- Cosmetic items O-01–O-05 (P8 key-92 spacing variant, IT tight
  numbers-box title, NL keys-flow end-y 1.4-unit difference, P1
  numbers-box wrap, etc.) — unchanged.
- W45-promise wording — unchanged.
- The ko freeze exit-1 — adjudicated legitimate, not churned.
- Nothing else was changed. No fix could not be applied as
  specified, except as flagged: (a) the verdict's "exactly 2" zh-tw
  residue claim was refuted and 6 further same-class strings were
  fixed (§3); (b) D-CORE-01 was fixed at the wrap level instead of by
  shortening the two stems, as the verdict allowed; (c) the first
  SC-scan definition was discarded as unsound (§3.1).

## 9. Evidence index (all under `hidden_files/w46/ja-fix/`)

`FIX-REPORT.md` (this file), `before-sha256.txt`,
`abstracts-before-after.txt`, `abstract-checks-final.log`,
`sc-occurrences-BEFORE.txt`, `sc-scan-AFTER.json`,
`sc_scan.py`, `kinsoku_scan.py`, `kinsoku-orphan.json`,
`counts_checks.py`, `counts-checks.json`, `rebuild-fanouts.sh`,
`build-webpdf.sh`, `run_gates.sh`, `gates-run.log`,
`freeze-baseline.json`, `freeze-<code>.json` (11),
`p8compare-<code>.json` (11), `p8extract-core.json`,
`occlusion-<code>.json` (11), `pdf-checks.log`,
`final-inventory.txt`, `render-logs/` (core/fan-out run+render logs,
`rebuild-summary.txt`, `webpdf-summary.txt`, `webpdf-<code>.log`).
