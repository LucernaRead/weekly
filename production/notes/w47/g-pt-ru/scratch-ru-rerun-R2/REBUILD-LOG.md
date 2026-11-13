# W47 ru re-rebuild R2 — ru-it / ru-pt / ru-nl / ru-ja / ru-ko / ru-zh-tw (with the `_run_w` fix)

Date: 2026-11-12 UTC. Worker: consolidated R2 (6 editions).
Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ru-rerun-R2/`
Production dir: `~/workspace/weekly-git/production/2026-w47/` (main only, no branch).
**DO NOT SYNC — build + verify in scratch ONLY. No production file touched, no commit/push/lint.**

## 0. Context (verified, not re-litigated)

- The second spacing fix (`_run_w`: unkerned run measurement in `svglib.py`
  `Page.text`) is ported to all 11 ru copies, md5
  `ee3211298f274e02ade2d4ca318ce354`, byte-identical to the it-ru fixed source.
  PROBE-GREEN on ru-de (worker f50d7c58,
  `scratch-runw-port/REBUILD-LOG.md`): census 27 tokens/30 boundaries → 12/15,
  0 real joins; `13ноября` 1.43 → 2.47 pt, text layer now reading `13 ноября`;
  gates all pass.
- The first fix (Cyrillic Medium faces) is already in those copies.
- Wave B (ru-it/pt/nl/ja) was synced with the Medium fix and reported "0 real
  joins" — that verdict is SUPERSEDED for the date cases (the shared
  `13ноября` line at 1.43–1.50 pt is a confirmed join). All 4 need this
  re-rebuild regardless.
- Wave C (core-ru/ru-ko/ru-zh-tw) was BLOCKED (11–12 second-class joins each +
  core-ru Morozko loss) and never synced. ru-ko/ru-zh-tw are here; core-ru is
  another worker's (R1). Wave C log:
  `scratch-ru-rebuild-C/REBUILD-LOG.md`.
- Severity rules (decided): DATE cases (19/20/16/13 ноября, 1.43–2.24 pt) are
  CONFIRMED JOINS — they must be gone; P8 ARROW cases (~2.36–2.44 pt, at the
  normal median) are NOT joins; the `ГЛАГОЛЫИ` bold-caps bbox artifact is not
  a join; the ko CJK token (`аное대조를나타냅니다`, P8, 2.43–2.44 pt, CJK→CJK)
  is not a visual join and not in `_run_w` scope — report as before, do not
  chase it. Target: 0 real joins, print AND web.
- ru-zh-tw ONLY: verify Morozko SURVIVES — its keys end was 2188.39 with
  margin +7.61, and the Medium fix did not grow it (delta +0.00).
- ru-ko: never had Morozko (keys end 2231.27, already skipped in the finalized
  build) — do NOT try to restore it; out of scope.

## 1. Pre-flight verification (all 6, before any build)

| Edition | svglib.py md5 | Expected |
|---|---|---|
| ru-it | `ee3211298f274e02ade2d4ca318ce354` | ✓ match |
| ru-pt | `ee3211298f274e02ade2d4ca318ce354` | ✓ match |
| ru-nl | `ee3211298f274e02ade2d4ca318ce354` | ✓ match |
| ru-ja | `ee3211298f274e02ade2d4ca318ce354` | ✓ match |
| ru-ko | `ee3211298f274e02ade2d4ca318ce354` | ✓ match |
| ru-zh-tw | `ee3211298f274e02ade2d4ca318ce354` | ✓ match |

Disk at start: 97G used / 150G (65%), below the 100G stop line. Memory gate in
the driver: wait while available < 1000 MB, max 600 s per build, then proceed
and log memory at build start (shared box runs ~16 workers; available hovered
~1000–1280 MB).

## 2. BEFORE state (production PDFs, recorded 2026-11-12 ~00:05–00:15 UTC)

Note the split: ru-it/pt/nl/ja production PDFs are the wave-B **Medium**
builds (byline already 2.89 pt); ru-ko/ru-zh-tw production PDFs are the
**original pre-Medium** builds (byline still 1.10 pt, no space char) because
wave C never synced. The R2 rebuild therefore fixes both defect classes at
once for ko/zh-tw, and only the second class for it/pt/nl/ja.

| Edition | text.md SHA-256 (bytes) | print PDF SHA-256 (bytes) | web PDF SHA-256 (bytes) |
|---|---|---|---|
| ru-it | `0bb5739a9e2a1215074b8d5cba566736e88cd84d45f3bc28eb0fe5a8966f5989` (63,972) | `6f123397a03f32610a14c1ea23f23a80ba442c6b976fa08f9f52275822561331` (21,264,469) | `37a31f2d6ef22f4300fd01275b778612929d3e5b95eac8dacd1cd20a571ac396` (3,382,725) |
| ru-pt | `ab21732233d80c5af14a2a579ef611370fb228ba29376d9e2ce9186a7c613a02` (65,116) | `b4a3fdfebc3fa5c23786f496ed1a2416698f8aa5eb5687a9213d3f7c3118a3f9` (21,204,114) | `38b7fa500c5a28f5a83919ae4327b017d30fbb81fa732a95947e624e463488fa` (3,382,131) |
| ru-nl | `849015f1e920f15c8a0040157a477aab5efb75200f27ef8bcac43160e544e9b0` (64,013) | `6579cf5fc3ea1fb0137e48d37f4f975fe15648a14cbd86378102aa3c914ae08a` (21,290,182) | `db2f1c4d6bf1fc28e801856718680f571366249873e6cd1fa70e11bbb7be3575` (3,385,859) |
| ru-ja | `07824474bb88439bea67fb4d1dc3ede956f33b006a32e8203e5b52081c1090da` (64,477) | `d681cf9788392b44b271fbe76e0ef48fbe7913563c94c1e2335a04b7b9f26a61` (27,408,235) | `8b7b38d48753247dc90ed8913120dfcbee7c3d9e0b07fcebce72c5ce49fb2254` (3,720,196) |
| ru-ko | `5e9bd67201fd232aff598e0bbb487ba45821878e533392bc6e749444b090bffe` (65,012) | `78e4442af8af9ec286c407ff66e08bac2029dd79d3ded43d1bfde3d555a6a400` (22,007,810) | `34e1c1db929faf24a5a173170a8fab939dfd5503ff88a56a0ce56b07a2bb8ce6` (3,513,245) |
| ru-zh-tw | `277a24f8a1674c970a367bf4fc8cccdd85d3f88941f85d633713a0e525ee6c83` (60,850) | `094b6a3b17cb34d7b0760a2bc1775cd9e59aadedb5f906ce51e103254ad537ca` (24,784,332) | `eba60ec2f70f220cecf42d633976ce146c1276603000b046c1f23ff0dd07c3c2` (3,994,661) |

Per-edition files: `<slug>/before-sha.txt` (full SHAs + md5).

## 3. BEFORE census (probe method: `census.py` from `scratch-runw-port/`, print = web on all 6)

| Edition | Distinct join tokens | Total join boundaries |
|---|---|---|
| ru-it | 29 | 39 |
| ru-pt | 25 | 28 |
| ru-nl | 27 | 35 |
| ru-ja | 43 | 58 |
| ru-ko | 239 | 416 |
| ru-zh-tw | 188 | 262 |

The ko/zh-tw/ja counts are inflated by CJK/native-language tokens (CJK runs
with no spaces, `譯注｜…` glosses, Japanese date lines) that the probe census
lists as candidates; adjudication filters to Cyrillic-bearing boundaries (see
per-edition sections). The shared real-join core in every BEFORE census:
`19ноября` P2, `20ноября` P4, `16ноября` P5, `13ноября` P8 (1.43–1.50 pt),
`A.биография` P3 (2.20), `A.на` P4 (1.68), `A.снег/цена/точно` P7
(2.28–2.29), `результатов+` P4 (1.96), `—скидка` P8 (1.44); plus the
`→выходят/рассказывает/снял/сыграли/играет/победило/работаем` P8 arrow
tokens (2.32–2.41 pt, NOT joins per the severity rules) and `→После` ×3 /
`→Родительный` P7 (3.75 pt, real spaces).

Per-edition BEFORE details:

- **ru-it**: 29/39. Extra P8 native junctions (not in the core list):
  `negativo:не` 1.14 pt, `fila:пять` 0.85 pt, `Attenzione:играть` −0.19 pt
  (Latin word + colon + Cyrillic, space after colon — same class as
  `—поздравляю`); `✓Vedi` 2.33 pt; `·повод` P2 2.23 pt, `·кинозрителя` P3
  2.21 pt. `SETTIMANALE` ×8 (footer, intra-word split, FP).
  Byline already 2.89/2.82 pt (Medium build). `13ноября` 1.43 pt, text layer
  fused (`13 ноября` absent on P8; `19/20/16 ноября` present elsewhere in the
  text layer but the fused option forms also present).
- **ru-pt**: 25/28. Same core; extra P8: `negativo:не` 1.14 pt, `✓Ver`
  2.33 pt; `·повод` P2 2.21 pt. No `fila:пять` / `Attenzione:играть`
  equivalents (different P8 key glosses).
- **ru-nl**: 27/35. Same core; extra P8: `elkaar:пять` 0.85 pt,
  `op:играть` 0.66 pt, `✓Zie` 2.33 pt. `Antwoorden` ×6 (intra-word split,
  FP), `novemberweer` (Dutch intra-word split, FP).
- **ru-ja**: 43/58. Same core; CJK rows are extraction artifacts (Japanese
  runs with no spaces, gaps 1.43–1.44 pt at the leading `—` of Japanese
  answer lines, 3.44 pt at `·` separators, 0.0 pt on `8.11./7.11./6.11.`
  score fragments); `21の後はгол：забили` P7 is the shared multi-boundary
  token. `降格圏内·` etc. 3.44–3.46 pt are real spaces.
- **ru-ko**: 239/416. Pre-Medium build: the full Medium-class join set is
  still present (byline `редакцииLucerna` 1.10 pt ×5, `Профессиональные
  праздники` 1.35–1.55 pt, P1 `метеорологическаязима`, `результатэтого`
  1.84 pt, P8 `заказываетподарок` 1.13 pt, `Сначаласоставьтесписок` 1.33 pt,
  etc. — gaps 0.63–2.68 pt across P1–P8) on top of the second-class 12
  (11 shared + ko-only CJK token `аное대조를나타냅니다` P8, 2.35–2.43 pt).
  `13ноября` 1.50 pt here.
- **ru-zh-tw**: 188/262. Pre-Medium build: same full Medium-class set as ko
  (byline 1.10 pt ×5, same P1–P8 joins), plus the second-class 11
  (`13ноября` 1.50 pt). CJK `譯注｜…` gloss rows are extraction artifacts.

Full BEFORE rows: `<slug>/census-BEFORE-print.txt` (+ `.json`, web twins).
Gap measurements on the 15 probe pairs + byline + arrows:
`<slug>/gaps-BEFORE.txt`.

## 4. Build method (per edition, serial, scratch only)

Driver: `run_r2.sh` in this dir. Per edition, in order ru-it, ru-pt, ru-nl,
ru-ja, ru-ko, ru-zh-tw:
1. `tools/venv/bin/python tools/run_build.py --build
   production/2026-w47/2026-w47-<slug> --out <slug>/build1 --steps run,render`
2. `tools/venv/bin/python tools/webpdf.py <slug>/build1/build-copy/svg
   <slug>/build1/build-copy/Lucerna-VOL4-<slug>-web.pdf` — ALWAYS regenerated:
   the build-copy initially holds the STALE production web PDF, so a
   reuse-if-present check would silently poison the web census/text layer.
   (Caught on the first driver run: it skipped webpdf for ru-it build1;
   driver killed, script fixed, partial build2 deleted, driver restarted.
   Lost work: ~90 s of ru-it build2 render.)
3. Second independent build to `<slug>/build2` (run,render) for the freeze
   check (8/8 SVG SHA match + print PDFs byte-identical).
4. Gates on build1: run.py TOTAL (expect 150, zero overflow); p8 extract
   150/150; p8 compare vs production core-ru CLEAN with missing/extra/
   uncertain empty (keydiff [137,138,139,140] EXPECTED); check_core.py
   (cwd = build-copy); occlusion audit 0 flags; freeze 8/8; print/web text
   layers identical per page; census AFTER print + web; gap re-measurement
   on the 15 probe pairs + byline + arrows; text.md byte-identical.

## 5. Per-edition results

### 5.1 ru-it — GREEN (all gates pass; 0 real joins)

- Build: run_build rc=0 both builds; run.py TOTAL 150, zero overflow;
  integrity "production unchanged (42 files re-hashed)" both builds.
  P8 keys end col 3 y 2331.72 (unchanged vs wave B); Morozko skipped as
  before (ru-it never carried it — keys end far above the 2196 threshold;
  not a loss, out of scope).
- New SHAs (§5+§7 values for the sync step — NOT applied, production
  untouched):
  - print `12f897b2f27cbc8e50c08c497c36e41c72f894be6403a63654c498eea69e07db`,
    21,263,401 B
  - web `9408886dc006a8a9780c9f019c75b3e8ff543b0baa6a3982b8fb670c0d3b2ed3`,
    3,381,671 B, 57,869 text bytes (production web was 3,382,725 B /
    57,843 — the +26 text bytes are the reappearing space chars)
  - text.md `0bb5739a…` UNCHANGED (byte-identical in build-copy, verified).
- Census AFTER (probe method, print = web): **29 tokens / 39 boundaries →
  13 / 23**. All 13 remaining tokens are previously-cleared false
  positives, 0 real joins:
  `SETTIMANALE` ×8 (footer intra-word split), `→После` ×3 + `→Родительный`
  (3.75 pt real spaces), `A2→B1`/`A2→B2` (diagram connectors), P8 arrows
  `→выходят/рассказывает/снял/сыграли/играет/победило/работаем`
  (2.40–2.41 pt, at the normal median — NOT joins), `✓Vedi` 2.41 pt.
  GONE: all 4 DATE cases, `A.биография/на/снег/цена/точно`,
  `результатов+`, `—скидка`, `—поздравляю`, the P8 colon junctions
  `negativo:не` (1.14), `fila:пять` (0.85), `Attenzione:играть` (−0.19),
  and `·повод` / `·кинозрителя`.
- Gaps AFTER (ink, print = web): `13ноября` 1.43 → **2.47 pt**,
  `20ноября` 2.18 → **3.52**, `19ноября` 2.11 → **3.48**,
  `16ноября` 2.24 → **3.68**, `A.на` 1.68 → **3.48**, `A.биография`
  2.20 → **3.63**, `A.снег` 2.28 → **3.71**, `A.цена` 2.29 → **3.72**,
  `A.точно` 2.29 → **3.71**, `результатов+` 1.96 → **3.01**,
  `—скидка` 1.44 → **2.41**, `—поздравляю` → **2.38**. Byline unchanged
  2.89/2.82 pt. Text layer: `13/19/20/16 ноября` all present as spaced
  forms, all fused forms absent. P8 crops in `ru-it/crops/` show
  `A. 13 ноября` separated. (Identical numbers to the ru-de probe —
  the shared core lines clear identically, as predicted.)
- Gates: p8 extract **150/150**; p8 compare vs production core-ru **CLEAN,
  keydiff [137, 138, 139, 140]** (expected); check_core rc=0, golden BAD 0,
  gloss fails 0, orphans 1 (P7 y553 `”».`, same benign class as KIT),
  collisions 0, P8 SVG text chars 11122; occlusion **0 flags** (selftest OK,
  real audit — the corrected invocation, re-run 00:29 UTC); freeze **8/8
  SVG SHA match** between the two independent builds,
  print PDFs byte-identical (`12f897b2…`); print/web text layers
  **identical per page** (30,923 non-ws chars each).

### 5.2 ru-pt — GREEN (all gates pass; 0 real joins)

- Build: run_build rc=0 both builds; run.py TOTAL 150, zero overflow;
  integrity "production unchanged (42 files re-hashed)" both builds.
  P8 keys end col 3 y 2317.03.
- New SHAs (§5+§7 values for the sync step — NOT applied):
  - print `9057a1e3e3f4f74fe0a451a6d744d4e19f7c645489c24eacf67e6a0b51f2fb38`,
    21,203,097 B
  - web `0868cfa46eb7c0058eb047c5ae21d2a8635dbb8858ee7676b2c35557e0d8836b`,
    3,381,069 B
  - text.md `ab217322…` UNCHANGED (byte-identical in build-copy, verified).
- Census AFTER (probe method, print = web): **25 tokens / 28 boundaries →
  12 / 15** — the exact probe pattern (ru-de probe: 12/15). All 12
  remaining tokens are previously-cleared false positives, 0 real joins:
  `→После` ×3, `→Родительный` (3.75 pt), `A2→B1`/`A2→B2` (diagram),
  P8 arrows ×7 (2.40–2.41 pt, NOT joins), `✓Ver` 2.41 pt.
  GONE: all 4 DATE cases, `A.биография/на/снег/цена/точно`,
  `результатов+`, `—скидка`, `—поздравляю`, `negativo:не`, `·повод`.
- Gaps AFTER (ink, print = web): `13ноября` 1.43 → **2.47 pt**,
  `20ноября` 2.18 → **3.52**, `19ноября` 2.11 → **3.48**,
  `16ноября` 2.24 → **3.68**, `A.на` 1.68 → **3.48**, `A.биография`
  2.20 → **3.63**, `A.снег` 2.28 → **3.71**, `A.цена` 2.29 → **3.72**,
  `A.точно` 2.29 → **3.71**, `результатов+` 1.96 → **3.01**,
  `—скидка` 1.44 → **2.41**, `—поздравляю` → **2.41**. Byline unchanged
  2.89/2.82 pt. Text layer: all four spaced date forms present, all
  fused forms absent.
- Gates: p8 extract **150/150**; p8 compare vs production core-ru **CLEAN,
  keydiff [137, 138, 139, 140]** (expected); check_core rc=0, golden BAD 0,
  gloss fails 0, orphans 1 (P7 y553 `”».`), collisions 0, P8 SVG text
  chars 11081; occlusion **0 flags** (selftest OK); freeze **8/8 SVG SHA
  match**, print PDFs byte-identical; print/web text layers **identical
  per page** (31,105 non-ws chars each).

### 5.3 ru-nl — GREEN (all gates pass; 0 real joins)

- Build: run_build rc=0 both builds; run.py TOTAL 150, zero overflow;
  integrity "production unchanged (42 files re-hashed)" both builds.
  P8 keys end col 3 y 2389.29.
- New SHAs (§5+§7 values for the sync step — NOT applied):
  - print `2bd4e0f2aa0f18794efd393e2e3e5499619729fd25bc82e36e475d2a37a702ff`,
    21,289,183 B
  - web `390d4050e03f0aa4f6392009f333d09465c907ab45dddb2c8ec4d580ce5f7d48`,
    3,384,838 B
  - text.md `849015f1…` UNCHANGED (byte-identical in build-copy, verified).
- Census AFTER (probe method, print = web): **27 tokens / 35 boundaries →
  14 / 22**. All 14 remaining tokens are previously-cleared false
  positives, 0 real joins: `Antwoorden` ×6 (Dutch intra-word split),
  `novemberweer` (intra-word), `→После` ×3, `→Родительный` (3.75 pt),
  `A2→B1`/`A2→B2` (diagram), P8 arrows ×7 (2.40–2.41 pt, NOT joins),
  `✓Zie` 2.41 pt. GONE: all 4 DATE cases, `A.биография/на/снег/цена/точно`,
  `результатов+`, `—скидка`, `—поздравляю`, the P8 colon junctions
  `elkaar:пять` (0.85), `op:играть` (0.66).
- Gaps AFTER (ink, print = web): `13ноября` 1.43 → **2.47 pt**,
  `20ноября` 2.18 → **3.52**, `19ноября` 2.11 → **3.48**,
  `16ноября` 2.24 → **3.68**, `A.на` 1.68 → **3.48**, `A.биография`
  2.20 → **3.63**, `A.снег` 2.28 → **3.71**, `A.цена` 2.29 → **3.72**,
  `A.точно` 2.29 → **3.71**, `результатов+` 1.97 → **3.09**,
  `—скидка` 1.44 → **2.41**, `—поздравляю` → **2.36**. Byline unchanged
  2.89/2.82 pt. Text layer: all four spaced date forms present, all
  fused forms absent.
- Gates: p8 extract **150/150**; p8 compare vs production core-ru **CLEAN,
  keydiff [137, 138, 139, 140]** (expected); check_core rc=0, golden BAD 0,
  gloss fails 0, orphans 1 (P7 y553 `”».`), collisions 0, P8 SVG text
  chars 11138; occlusion **0 flags** (selftest OK); freeze **8/8 SVG SHA
  match**, print PDFs byte-identical; print/web text layers **identical
  per page** (31,087 non-ws chars each).

### 5.4 ru-ja — GREEN (all gates pass; 0 real joins)

- Build: run_build rc=0 both builds; run.py TOTAL 150, zero overflow;
  integrity "production unchanged (42 files re-hashed)" both builds.
  P8 keys end col 3 y 2203.08. Images: 5 total, per-page [1,1,0,1,1,0,1,0]
  — identical to production (P8 never carried an image here; no loss).
- New SHAs (§5+§7 values for the sync step — NOT applied):
  - print `38a6efb07df58c7cffba459ffe2e65c28a98fbb92c1bc2ccf5bf93ccd7ee878c`,
    27,407,117 B
  - web `89973dd75d8242d03880dcb0b509f02bb6a070b86fdef3e4b11e5e171f97e880`,
    3,719,047 B, 58,627 text bytes (pre-restart webpdf produced
    3,719,070 B — the 23 B difference is webpdf's known non-deterministic
    font-subset bytes, not content)
  - text.md `07824474…` UNCHANGED (byte-identical in build-copy, verified).
- Census AFTER (probe method, print = web): **43 tokens / 58 boundaries →
  25 / 38**. All 25 remaining tokens are previously-cleared false
  positives / CJK extraction artifacts, 0 real joins: Japanese date lines
  `11月17日—` ×5, `11月18日—` ×2, `11月22日—`, `11月19日—` (2.32–2.40 pt,
  unchanged vs BEFORE — CJK lines, no spaces by design), Japanese
  `·`-separator lines at 3.44–3.46 pt (real spaces), score fragments
  `8.11.` ×4 / `7.11.` ×3 / `6.11.` (0.0 pt, intra-word),
  `21の後はгол：забили` (gap None, same as BEFORE — wave C cleared this
  P7 token as real-space), `→После` ×3, `→Родительный` (3.75 pt),
  `A2→B1`/`A2→B2` (diagram), P8 arrows ×7 (2.40–2.41 pt, NOT joins).
  GONE: all 4 DATE cases, `A.биография/на/снег/цена/точно`,
  `результатов+`, `—скидка`, `—поздравляю`, AND the nine Japanese
  `—…` P8 lines that read 1.43–1.44 pt in BEFORE (they no longer appear
  as candidates — the dash run now measures with a space char, same
  mechanism as the Cyrillic dash joins).
- Gaps AFTER (ink, print = web): `13ноября` 1.43 → **2.47 pt**,
  `20ноября` 2.18 → **3.52**, `19ноября` 2.11 → **3.48**,
  `16ноября` 2.24 → **3.68**, `A.на` 1.68 → **3.48**, `A.биография`
  2.20 → **3.63**, `A.снег` 2.28 → **3.71**, `A.цена` 2.29 → **3.72**,
  `A.точно` 2.29 → **3.71**, `результатов+` 1.88 → **3.01**,
  `—скидка` 1.44 → **2.41**, `—поздравляю` → **2.34**. Byline unchanged
  2.89/2.82 pt. Text layer: all four spaced date forms present, all
  fused forms absent.
- Gates: p8 extract **150/150**; p8 compare vs production core-ru **CLEAN,
  keydiff [137, 138, 139, 140]** (expected); check_core rc=0, golden BAD 0,
  gloss fails 0, orphans 1 (P7 y553 `”».`), collisions 0, P8 SVG text
  chars 8475; occlusion **0 flags** (selftest OK); freeze **8/8 SVG SHA
  match**, print PDFs byte-identical; print/web text layers **identical
  per page** (26,630 non-ws chars each).

### 5.5 ru-ko — BLOCKED (occlusion gate FAILS: 8 TEXTX flags introduced by `_run_w`; do NOT sync)

- Build: run_build rc=0 both builds; run.py TOTAL 150, zero overflow;
  integrity "production unchanged (42 files re-hashed)" both builds.
  P8 keys end col 3 y 2231.27 — identical to the finalized build; Morozko
  SKIPPED as before (ko never had it; out of scope, not a loss).
- New SHAs (for the record only — NOT shippable, do NOT apply):
  - print `2fd2389ccc1e48a55f76b44826470d735ee47a9e5058969cfe1d0ef862c66573`,
    22,005,216 B
  - web `9403c38c8dcc349672508ea520534b2c24591f05b59189df87be67fa763be44f`,
    3,510,639 B, 58,744 text bytes
  - text.md `5e9bd672…` UNCHANGED (byte-identical in build-copy, verified).
- Census AFTER (probe method, print = web): **239 tokens / 416 boundaries →
  95 / 223**. Cyrillic-bearing rows: only 11, ALL previously-cleared false
  positives, **0 real joins**: `→После` ×3, `→Родительный` (3.75 pt),
  `뒤에는гол:` (gap None, same as BEFORE — wave C cleared this P7 token as
  real-space), P8 arrows ×7 (2.40–2.41 pt, NOT joins),
  `аное대조를나타냅니다` P8, 2.34–2.44 pt (the known ko CJK token — not a
  visual join, not in `_run_w` scope; gap essentially unchanged vs BEFORE
  2.35–2.43, reported as before). The other 84 remaining tokens are Korean
  CJK rows (e.g. `빈칸채우기` ×48 at 3.28 pt — real spaces between Korean
  words, extraction artifacts). GONE: all 4 DATE cases, the entire
  Medium-class join set (byline, `Профессиональные праздники`, P1–P8
  joins), `результатов+`, `—скидка`, `—поздравляю`.
- Gaps AFTER (the fixed pairs — same probe-identical numbers as ru-it):
  `13ноября` 1.50 → **2.47 pt**, `20ноября` 2.18 → **3.52**,
  `19ноября` 2.11 → **3.48**, `16ноября` 2.24 → **3.68**,
  `A.на` 1.68 → **3.48**, `A.биография` 2.20 → **3.63**,
  `A.снег` 2.28 → **3.71**, `A.цена` 2.29 → **3.72**,
  `A.точно` 2.29 → **3.71**, `результатов+` −0.14 → **3.01**,
  `—скидка` 1.44 → **2.41**, `—поздравляю` → **2.37**. Byline
  1.10 pt (no space) → **2.89/2.82 pt with space char**. Text layer: all
  four spaced date forms present, all fused forms absent.
- Other gates: p8 extract **150/150**; p8 compare vs production core-ru
  **CLEAN, keydiff [137, 138, 139, 140]** (expected); freeze **8/8 SVG SHA
  match**, print PDFs byte-identical; print/web text layers **identical
  per page**.
- **BLOCKER — occlusion audit: 8 TEXTX flags (rc=1).** All on P7, all the
  same pattern — a Korean sentence ending in ` (` followed by the Russian
  page reference `Страница`:
  `제14라운드의 여덟 경기가 모두 끝났습니다. (` → `Страница` (overlap
  4.5×18.2 px), `휴식기 후 리그는 11월 20일에 돌아옵니다. (` → 3.4 px,
  `이것이 2026년 국가대표의 마지막 경기입니다. (` → 3.4 px,
  `똑똑한 구매자는 서두르지 않는다. (` → 3.4 px,
  `이런 주는 일 년에 가장 흔합니다. (` → 5.5 px,
  `직업 기념일은 휴일이 아니다. (` → 3.2 px,
  `11월의 밤은 어둡고 길다. (` → 3.4 px,
  `11월에는 근무일 20일과 휴일 10일이 있다. (` → 3.1 px.
  check_core agrees: same-baseline collisions **0 → 10** (the same 8
  `Страница` lines + P1 y1206 `고 마감 시점 · ` vs `в` and P7 y968
  `는 출발점으로 생격: ` vs `с`). check_core itself exits rc=0 (golden
  BAD 0, gloss 0, orphans 1, P8 chars 8740), but the collision jump is
  part of the same defect.
- **Verified NOT pre-existing.** Same tools, same invocation, on the
  wave-C Medium scratch build: occlusion **0 flags**, collisions **0**.
  On production ko (pre-Medium): occlusion **0 flags**. The R2 build is
  the only one that flags — the regression is `_run_w` itself.
- **Mechanism (measured, not guessed).** In the R2 SVG the first flagged
  line is `x=88.0 … '제14라운드의 여덟 경기가 모두 끝났습니다. ('` with
  `Страница` at `x=448.5`; in the wave-C SVG the identical text sits at
  `x=88.0` with `Страница` at `x=452.8`. So `_run_w` measured the Korean
  run as 360.5 units vs `getlength`'s 364.8 — **4.3 units short** at
  font-size 19.5. Direct PIL check on NotoSansCJK-Regular (the audit's
  font): whole-string `getlength` = 673.66 vs sum-of-single-char advances
  = 665.59 at 36 px (diff 8.06, ×19.5/36 = 4.37 units — the observed
  4.3). Substring tests isolate it: a space between two Hangul words
  measures **2.02 units MORE in whole-string getlength than the sum of
  its single-char advances** at 36 px (`가 나` diff 2.02; `여덟 경기가
  모두` 4.03 for 2 spaces; the full string's 4 inter-Hangul-word spaces
  account for the whole 8.06). No diff for `. (`, `다.`, digits, or
  Hangul with no space. So `_run_w` under-measures every CJK run by
  ~1.09 units per inter-word space at 19.5 pt, placing the following run
  that far too far left — 4 spaces → ~4.4 units ≈ 1.3 pt of ink overlap,
  exactly the audit's 3.1–5.5 px. Visual check (300 dpi crops
  `ru-ko-p7-junction-R2.png` vs `...-PROD.png`, same clip): production
  shows `. ( Страница` with a clear space; R2 shows `. (Страница` with
  the space eaten and the glyphs jammed together. This also explains why
  ru-ja passed (Japanese has no inter-word spaces, so sum == whole) and
  why the Latin/Cyrillic editions passed.
- **What unblocks ko:** a CJK-aware `_run_w` (e.g. whole-string
  `getlength` for runs containing Hangul/CJK, or a per-space correction
  for CJK runs) — a renderer-fix decision, NOT a rebuild's call. The
  scratch builds must be REBUILT after that fix (not just synced).
  The ko CJK token `аное대조를나타냅니다` is unaffected and stays
  reported as before.

### 5.6 ru-zh-tw — GREEN (all gates pass; 0 real joins; Morozko SURVIVES)

- Build: run_build rc=0 both builds; run.py TOTAL 150, zero overflow;
  integrity "production unchanged (42 files re-hashed)" both builds.
- **Morozko SURVIVES (the §5 check).** P8 keys end col 3 y **2188.39** —
  identical to the finalized build (delta +0.00, margin +7.61 under the
  2196 threshold); run log: `P8 morozko ends 2579.99` in BOTH builds (no
  SKIP). Images: **6 total**, per-page [1,1,0,1,1,0,1,1] — P8 carries its
  image. P8 SVG: `Морозко` ×1, `Билибин` ×2, P8 SVG text chars 8178
  (identical to the wave-C Medium build's 8178). Print size 24,781,766 B
  vs production 24,784,332 B — no ~2.7 MB drop, confirming nothing was
  lost (contrast core-ru's Medium build, which lost the image and shrank
  by ~2.7 MB).
- New SHAs (§5+§7 values for the sync step — NOT applied):
  - print `dbd7a52a0f8e532f094ff8f9e276d7ca523ec52987316e2e2576f841850828d6`,
    24,781,766 B
  - web `d7787a5e49e98ab2eb6a774e64730cc33587b18c9612434b8434ef6c29e85184`,
    3,992,096 B
  - text.md `277a24f8…` UNCHANGED (byte-identical in build-copy, verified).
- Census AFTER (probe method, print = web): **188 tokens / 262 boundaries →
  41 / 57**. Cyrillic-bearing rows: only 10, ALL previously-cleared false
  positives, **0 real joins**: `→После` ×3, `→Родительный` (3.75 pt),
  `後面用гол：забили` (gap None, same as BEFORE — wave C cleared this P7
  token as real-space), P8 arrows ×7 (2.40–2.41 pt, NOT joins). The other
  31 rows are Chinese CJK lines (P8 answer lines at 2.32–2.40 pt,
  unchanged vs BEFORE — CJK, no spaces by design), score fragments
  `8.11.` ×4 / `7.11.` ×3 (0.0 pt, intra-word), `A2→B1`/`A2→B2`
  (diagram), and `·` lines at 3.44 pt (real spaces). GONE: all 4 DATE
  cases, the entire Medium-class join set (byline, `Профессиональные
  праздники`, P1–P8 joins), `результатов+`, `—скидка`, `—поздравляю`.
- Gaps AFTER (ink, print = web): `13ноября` 1.50 → **2.47 pt**,
  `20ноября` 2.18 → **3.52**, `19ноября` 2.11 → **3.48**,
  `16ноября` 2.24 → **3.68**, `A.на` 1.68 → **3.48**, `A.биография`
  2.20 → **3.63**, `A.снег` 2.28 → **3.71**, `A.цена` 2.29 → **3.72**,
  `A.точно` 2.29 → **3.71**, `результатов+` −0.14 → **3.01**,
  `—скидка` 1.44 → **2.41**, `—поздравляю` → **2.34**. Byline
  1.10 pt (no space) → **2.89/2.82 pt with space char**. Text layer: all
  four spaced date forms present, all fused forms absent.
- Gates: p8 extract **150/150**; p8 compare vs production core-ru **CLEAN,
  keydiff [137, 138, 139, 140]** (expected); check_core rc=0, golden BAD 0,
  gloss fails 0, orphans 5 (P7 y417 `。`, y553 `”».`, y784 `：`+`。`,
  y968 `。` — the same P7 set as KIT/core), collisions **0**, P8 SVG text
  chars 8178; occlusion **0 flags** (selftest OK); freeze **8/8 SVG SHA
  match**, print PDFs byte-identical; print/web text layers **identical
  per page** (25,844 non-ws chars each — same count as wave C's record).

## 6. Driver incidents (fixed during the run; no production impact)

1. **Stale web PDF reuse (run 1).** `run_build.py` copies the production
   edition into `build-copy`, so a fresh build-copy already contains the
   OLD web PDF; `render.py` does not regenerate it (the probe log §3 notes
   the same trap). The first driver checked "web PDF exists → skip
   webpdf" and would have censused the stale file. Caught after ru-it
   build1: driver killed, webpdf made unconditional, partial ru-it build2
   deleted, driver restarted. Lost work ~90 s.
2. **Stale print PDF reuse (run 2).** Same trap for the build-reuse check:
   ru-pt build1 was killed mid-render but its build-copy already held the
   stale production print PDF, so "print exists → reuse" would have
   blessed an incomplete build. Fixed: reuse requires
   `run_buildN.log` to contain "done: outputs"; otherwise the build dir
   is deleted and rebuilt. Partial ru-pt/build1 deleted before restart.
3. **check_core invocation (run 2).** `check_core.py` takes the edition dir
   as `argv[1]`; called with no arg it dies with `IndexError` (rc=1).
   Correct form (cwd = build-copy): `check_core.py .` → rc=0. Verified
   manually for ru-it build1 before fixing the driver.
4. **occlusion `--selftest` short-circuit (run 2).** In
   `tools/occlusion_audit.py`, `--selftest` means "run ONLY the synthetic
   selftest" and returns 0 before touching the svgdir. The driver passed
   it, so run 2's "occlusion rc=0" was vacuous — selftest only, no audit.
   Correct form: no `--selftest` (the selftest always runs first
   anyway). Wave B's logs show both lines because they ran it without
   the flag. Driver fixed; the re-run confirmed ru-it occlusion 0 flags
   (00:29 UTC) and every later edition ran the corrected invocation.

5. **Runtime restart mid-run (00:42 UTC).** The VM/runtime restarted while
   ru-ja build2 was rendering; the driver session died with no confirmed
   result. Recovery: verified from the logs that ru-it/pt/nl were fully
   done and ru-ja build1 was complete (`run_build1.log` contains
   "done: outputs", rc=0, webpdf rc=0, fresh web PDF 3,719,070 B) while
   ru-ja build2 was partial (stale production print PDF, no completion
   marker) and ru-ko/ru-zh-tw unstarted. No process survived the restart.
   Driver relaunched for `ru-ja ru-ko ru-zh-tw` only; its completion-marker
   reuse rule reuses ru-ja build1 and rebuilds build2 from scratch.
   Disk at relaunch: 98G used (still below the 100G stop line).

   Disk at relaunch: 98G used (still below the 100G stop line).

## 7. Summary + disposition (for the sync step — NOT applied here)

| Edition | Census before → after (tokens/boundaries) | Real joins after | Gates | Disposition |
|---|---|---|---|---|
| ru-it | 29/39 → 13/23 | 0 | all pass | GREEN — sync-ready |
| ru-pt | 25/28 → 12/15 | 0 | all pass | GREEN — sync-ready |
| ru-nl | 27/35 → 14/22 | 0 | all pass | GREEN — sync-ready |
| ru-ja | 43/58 → 25/38 | 0 | all pass | GREEN — sync-ready |
| ru-ko | 239/416 → 95/223 | 0 | **occlusion FAIL (8 TEXTX)**; collisions 0→10 | **BLOCKED — do NOT sync** |
| ru-zh-tw | 188/262 → 41/57 | 0 | all pass; Morozko survives | GREEN — sync-ready |

- **5 of 6 GREEN.** ru-it/pt/nl/ja/zh-tw pass every gate: run.py TOTAL 150,
  p8 150/150 CLEAN keydiff [137–140], check_core rc=0 (BAD 0, gloss 0,
  collisions 0), occlusion 0 flags, freeze 8/8 + print byte-identical,
  print/web text layers identical per page, text.md byte-identical,
  0 real joins print AND web. The DATE cases clear with exactly the
  probe's numbers in every edition (13ноября 1.43–1.50 → 2.47 pt etc.).
  ru-zh-tw's Morozko survives with keys end unchanged at 2188.39.
- **ru-ko BLOCKED.** The spacing fix itself regresses ko: `_run_w`
  under-measures CJK runs with inter-word spaces (~1.09 units per space
  at 19.5 pt), so 8 P7 `Страница` page references overlap the preceding
  Korean sentence's ink (3.1–5.5 px) and check_core collisions go 0→10.
  Verified NOT pre-existing (wave-C Medium build and production both
  0 flags / 0 collisions with the same tools). Needs a CJK-aware renderer
  fix, then a full rebuild — do not sync the ko scratch build.
- The ko CJK token `аное대조를나타냅니다` (P8, 2.34–2.44 pt) is unchanged
  vs BEFORE, reported as before, not a join, not in `_run_w` scope.
- **Production integrity (final check, 2026-11-12 ~01:05 UTC): all 18
  production files (6 editions × text.md + print + web) re-hashed —
  0 mismatches vs the BEFORE SHAs in §2.** Production untouched
  throughout; no commit/push/lint; no KIT file edited. Disk at end:
  98G used (below the 100G stop line).
- KIT §5+§7 values for the sync step (the 5 GREEN editions only):
  - ru-it: print `12f897b2f27cbc8e50c08c497c36e41c72f894be6403a63654c498eea69e07db`
    (21,263,401 B); web `9408886dc006a8a9780c9f019c75b3e8ff543b0baa6a3982b8fb670c0d3b2ed3`
    (3,381,671 B, 57,869 text bytes)
  - ru-pt: print `9057a1e3e3f4f74fe0a451a6d744d4e19f7c645489c24eacf67e6a0b51f2fb38`
    (21,203,097 B); web `0868cfa46eb7c0058eb047c5ae21d2a8635dbb8858ee7676b2c35557e0d8836b`
    (3,381,069 B)
  - ru-nl: print `2bd4e0f2aa0f18794efd393e2e3e5499619729fd25bc82e36e475d2a37a702ff`
    (21,289,183 B); web `390d4050e03f0aa4f6392009f333d09465c907ab45dddb2c8ec4d580ce5f7d48`
    (3,384,838 B)
  - ru-ja: print `38a6efb07df58c7cffba459ffe2e65c28a98fbb92c1bc2ccf5bf93ccd7ee878c`
    (27,407,117 B); web `89973dd75d8242d03880dcb0b509f02bb6a070b86fdef3e4b11e5e171f97e880`
    (3,719,047 B, 58,627 text bytes)
  - ru-zh-tw: print `dbd7a52a0f8e532f094ff8f9e276d7ca523ec52987316e2e2576f841850828d6`
    (24,781,766 B); web `d7787a5e49e98ab2eb6a774e64730cc33587b18c9612434b8434ef6c29e85184`
    (3,992,096 B)
  - ru-ko (BLOCKED, record only): print
    `2fd2389ccc1e48a55f76b44826470d735ee47a9e5058969cfe1d0ef862c66573`
    (22,005,216 B); web `9403c38c8dcc349672508ea520534b2c24591f05b59189df87be67fa763be44f`
    (3,510,639 B, 58,744 text bytes)

## 8. Files in this scratch dir

- `REBUILD-LOG.md` (this file), `run_r2.sh` (the driver),
  `driver-all.log` + `driver-all-2.log` (driver runs 1–3, incl. the two
  killed runs), `census.py` + `gap_rude.py` (copied unmodified from
  `scratch-runw-port/`), `checks.py` (textlayer / freeze / morozko
  helpers).
- Per edition `<slug>/`: `before-sha.txt`, `census-BEFORE-{print,web}.txt/.json`,
  `gaps-BEFORE.txt`, `run_build{1,2}.log`, `webpdf1.log`, `driver.log`,
  `after-sha.txt`, `census-AFTER-{print,web}.txt/.json`, `gaps-AFTER.txt`
  (+ `gaps-AFTER-web.txt`), `crops/` (P8 13-ноября + Imperativ crops),
  `gates/` (`p8-ed.json`, `p8-compare.json`, `p8-extract.log`,
  `p8-compare.log`, `check_core.log`, `occlusion.json`, `occlusion.log`,
  `freeze.log`, `textlayer.log`, `morozko.log`),
  `build1/` + `build2/` (full run_build scratch outputs: `build-copy`
  with svg/*.svg ×8, print + web PDFs, cards).
- ru-ko evidence: `ru-ko-p7-stranitsa.png` (full P7 strip),
  `ru-ko-p7-junction-R2.png` + `ru-ko-p7-junction-PROD.png` (300 dpi
  tight crops of the `(Страница` junction, R2 vs production).


## CORRECTION (2026-11-12, coordinator-verified) — ru-it web SHA in §7 is STALE
- §7 records ru-it web as `9408886dc006a8a9780c9f019c75b3e8ff543b0baa6a3982b8fb670c0d3b2ed3` (3,381,671 B). The CORRECT value is **`6fce91e40ee95c736ed07ef71e838147318591be2d09c7696195f64bb7a42cd1` (3,381,661 B)**.
- Cause (found by the R2R3 sync worker, verified by the coordinator on disk): the R2 driver ran webpdf twice — 00:20 wrote 3,381,671 B (`9408886d…`), then re-ran it unconditionally at 00:28, writing 3,381,661 B (`6fce91e4…`); §7 transcribed the superseded 00:20 value. The 10 B is webpdf's documented non-deterministic font-subset bytes (same class as ru-ja's 23 B). Both runs report 57,869 text bytes, and the second pass re-ran ALL gates on the final file (census 13/23 print+web, p8 150/150 CLEAN, check_core rc=0, occlusion 0, freeze 8/8, text layer per-page byte-identical).
- Production file and WEEKLY-KIT.md (line 54) now hold the CORRECT value `6fce91e4…` (3,381,661 B) — the sync worker synced the actual scratch file and updated the KIT to it. The §7 line above stands as the historical record of the mistake; this note is the correction. No other §7 value is affected (the sync worker verified the other 15 PDFs against their recorded SHAs).
