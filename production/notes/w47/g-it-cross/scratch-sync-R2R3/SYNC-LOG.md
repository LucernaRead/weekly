# SYNC-LOG — W47 `_run_w` re-rebuild sync: R2's 5 + R3's 3 (8 editions)

Date: 2026-11-12 (UTC). Sync worker: R2+R3 sync.
Sources: R2 log `hidden_files/w47/scratch-ru-rerun-R2/REBUILD-LOG.md`,
R3 log `hidden_files/w47/scratch-runw-rerun-R3/REBUILD-LOG.md`.
Production: `~/workspace/weekly-git/production/2026-w47/` (main only, no branch).
**No commit / push / lint.** ru-ko NOT synced (BLOCKED — `_run_w` CJK regression,
fix worker on it). R1's editions (core-ru, ru-de/en/fr/es) NOT touched.
No other family, no W43/W45/W46 covers/motions, no weekly-design, no little-stage.

## 0. Pre-flight

- Disk at start: 98G used / 150G (66%), below the 100G stop line. Disk at end of copy: 98G.
- Production BEFORE SHAs re-hashed before any copy: all 24 files (8 editions ×
  text.md + print + web) match the BEFORE values recorded in the R2 log §2 and
  the R3 log §1 — 0 mismatches. (Full table in §1 below: the "BEFORE" columns.)

## 1. Scratch verification (BEFORE copy) + before→after table

Every scratch file was hashed on disk and compared with its recorded SHA
**before** copying. 15/16 matched outright. The one exception was resolved
with evidence, not overridden — see §1a.

| Edition | File | BEFORE SHA-256 (production) | BEFORE bytes | AFTER SHA-256 (synced) | AFTER bytes |
|---|---|---|---|---|---|
| ru-it | `2026-w47-ru-it.text.md` | `0bb5739a9e2a1215074b8d5cba566736e88cd84d45f3bc28eb0fe5a8966f5989` | 63,972 | `0bb5739a9e2a1215074b8d5cba566736e88cd84d45f3bc28eb0fe5a8966f5989` (unchanged) | 63,972 |
| ru-it | `Lucerna-VOL4-ru-it.pdf` (print) | `6f123397a03f32610a14c1ea23f23a80ba442c6b976fa08f9f52275822561331` | 21,264,469 | `12f897b2f27cbc8e50c08c497c36e41c72f894be6403a63654c498eea69e07db` | 21,263,401 |
| ru-it | `Lucerna-VOL4-ru-it-web.pdf` (web) | `37a31f2d6ef22f4300fd01275b778612929d3e5b95eac8dacd1cd20a571ac396` | 3,382,725 | `6fce91e40ee95c736ed07ef71e838147318591be2d09c7696195f64bb7a42cd1` | 3,381,661 |
| ru-pt | `2026-w47-ru-pt.text.md` | `ab21732233d80c5af14a2a579ef611370fb228ba29376d9e2ce9186a7c613a02` | 65,116 | unchanged | 65,116 |
| ru-pt | `Lucerna-VOL4-ru-pt.pdf` (print) | `b4a3fdfebc3fa5c23786f496ed1a2416698f8aa5eb5687a9213d3f7c3118a3f9` | 21,204,114 | `9057a1e3e3f4f74fe0a451a6d744d4e19f7c645489c24eacf67e6a0b51f2fb38` | 21,203,097 |
| ru-pt | `Lucerna-VOL4-ru-pt-web.pdf` (web) | `38b7fa500c5a28f5a83919ae4327b017d30fbb81fa732a95947e624e463488fa` | 3,382,131 | `0868cfa46eb7c0058eb047c5ae21d2a8635dbb8858ee7676b2c35557e0d8836b` | 3,381,069 |
| ru-nl | `2026-w47-ru-nl.text.md` | `849015f1e920f15c8a0040157a477aab5efb75200f27ef8bcac43160e544e9b0` | 64,013 | unchanged | 64,013 |
| ru-nl | `Lucerna-VOL4-ru-nl.pdf` (print) | `6579cf5fc3ea1fb0137e48d37f4f975fe15648a14cbd86378102aa3c914ae08a` | 21,290,182 | `2bd4e0f2aa0f18794efd393e2e3e5499619729fd25bc82e36e475d2a37a702ff` | 21,289,183 |
| ru-nl | `Lucerna-VOL4-ru-nl-web.pdf` (web) | `db2f1c4d6bf1fc28e801856718680f571366249873e6cd1fa70e11bbb7be3575` | 3,385,859 | `390d4050e03f0aa4f6392009f333d09465c907ab45dddb2c8ec4d580ce5f7d48` | 3,384,838 |
| ru-ja | `2026-w47-ru-ja.text.md` | `07824474bb88439bea67fb4d1dc3ede956f33b006a32e8203e5b52081c1090da` | 64,477 | unchanged | 64,477 |
| ru-ja | `Lucerna-VOL4-ru-ja.pdf` (print) | `d681cf9788392b44b271fbe76e0ef48fbe7913563c94c1e2335a04b7b9f26a61` | 27,408,235 | `38a6efb07df58c7cffba459ffe2e65c28a98fbb92c1bc2ccf5bf93ccd7ee878c` | 27,407,117 |
| ru-ja | `Lucerna-VOL4-ru-ja-web.pdf` (web) | `8b7b38d48753247dc90ed8913120dfcbee7c3d9e0b07fcebce72c5ce49fb2254` | 3,720,196 | `89973dd75d8242d03880dcb0b509f02bb6a070b86fdef3e4b11e5e171f97e880` | 3,719,047 |
| ru-zh-tw | `2026-w47-ru-zh-tw.text.md` | `277a24f8a1674c970a367bf4fc8cccdd85d3f88941f85d633713a0e525ee6c83` | 60,850 | unchanged | 60,850 |
| ru-zh-tw | `Lucerna-VOL4-ru-zh-tw.pdf` (print) | `094b6a3b17cb34d7b0760a2bc1775cd9e59aadedb5f906ce51e103254ad537ca` | 24,784,332 | `dbd7a52a0f8e532f094ff8f9e276d7ca523ec52987316e2e2576f841850828d6` | 24,781,766 |
| ru-zh-tw | `Lucerna-VOL4-ru-zh-tw-web.pdf` (web) | `eba60ec2f70f220cecf42d633976ce146c1276603000b046c1f23ff0dd07c3c2` | 3,994,661 | `d7787a5e49e98ab2eb6a774e64730cc33587b18c9612434b8434ef6c29e85184` | 3,992,096 |
| nl-ru | `2026-w47-nl-ru.text.md` | `f23da475ff54bcfe86bbe6794473eafc65b42dbd5f015766924ce3e83cefb984` | — | unchanged | — |
| nl-ru | `De-Lucerna-VOL4-nl-ru.pdf` (print) | `21b7adf007a15e195756d49b22c824e828f854e11e02a10c916426997c468cc8` | 12,718,418 | `b9847bb26eac3011660c767b4ae17857ddeb39014fe8b9ffa7b9ec90b0404933` | 12,718,074 |
| nl-ru | `De-Lucerna-VOL4-nl-ru-web.pdf` (web) | `df6c3a7cb16cad0fc2b26bd90a8bdc8065c1197598d4f28b8944f705b0b95b6c` | 1,661,395 | `cbaac2df7c7acd38f35c9cd9eaba04b3416c290b72e676057f68dccb47b6c7ca` | 1,661,043 |
| pt-ru | `2026-w47-pt-ru.text.md` | `87871659c0101a9d8c2f7bc415946653ea80257032332cda8b1208e6288184c8` | — | unchanged | — |
| pt-ru | `A-Lucerna-VOL4.pdf` (print) | `86447421b5a5abff48690ed8ab8e4cd51ce9808e5adcaf24f0d8e30004a0d2f2` | 12,916,388 | `a3b022bc3dd5097e4c9217e3285d51d634a39672d7a6b6c4a6ee95725da85fee` | 12,916,087 |
| pt-ru | `A-Lucerna-VOL4-web.pdf` (web) | `c7017796abe91579d6429ae8f571401ef6aab0cd321e1acc593e66014f16c181` | 1,188,611 | `0cdf71671e02c7263c3883b5c1d0d324cc24c84c3a380625935c9fdd22849d77` | 1,188,302 |
| zh-cn-ru | `2026-w47-zh-cn-ru.text.md` | `de12db587c41005301b221cce52ae0d088ec52f9eaccf2338aa94382f00e8094` | — | unchanged | — |
| zh-cn-ru | `Lucerna-VOL4-RU.pdf` (print) | `bcfc550ff96ae87ce46fe1199592f5c7a690b91325dd3d5a410b11d95061305b` | 33,572,610 | `f1b2162dc91900e5d5a328d66e325a8d6bcf130f28d61d4ac0404e1e6b6189fe` | 33,572,048 |
| zh-cn-ru | `Lucerna-VOL4-RU-web.pdf` (web) | `a281456fc27d9036e753cd210d01938a98a7aaf18da604c2b80f46e49553e979` | 2,486,429 | `dbf960ab1c55eb1e4e14ef25db3a034b43254d6673373a02030f80915d414ee1` | 2,485,880 |

Copy result: all 16 PDFs copied; production copies re-hashed after copy and
match the scratch SHAs exactly (16/16 OK). text.md files were NOT copied and
are byte-identical before/after (spacing-only rebuilds). Only the 8 in-scope
edition dirs were touched.

### §1a. ru-it web SHA discrepancy — RESOLVED with evidence (file synced)

The R2 REBUILD-LOG.md §5.1/§7 records ru-it web SHA `9408886d…` (3,381,671 B),
but the scratch file on disk hashed to `6fce91e4…` (3,381,661 B). Investigation
(`ru-it/driver.log`, `ru-it/after-sha.txt`, `ru-it/gates/`):

- The R2 driver ran webpdf TWICE for ru-it build1. Run 1 (00:20 UTC) wrote
  3,381,671 B (`9408886d…`); the driver then re-ran webpdf unconditionally
  (the stale-web fix from incident §6.1) at 00:28 UTC, writing 3,381,661 B
  (`6fce91e4…`). Both runs report **57,869 text bytes**.
- The 10-byte difference is webpdf's documented non-deterministic
  font-subset bytes — the same class the R2 log itself notes for ru-ja
  (23 B between runs, "not content").
- The SECOND driver pass (00:27–00:29) re-ran **all** gates on the final
  `6fce91e4…` file: census print 13/23 AND web 13/23, p8 extract 150/150,
  p8 compare CLEAN keydiff [137–140], check_core rc=0, occlusion 0 flags,
  freeze 8/8, text layer per-page byte-identical (30,923 chars)
  — all in `ru-it/gates/` (timestamps 00:28–00:29) and `census-AFTER-web.json`
  (00:28). `ru-it/after-sha.txt` (the driver's final record) lists `6fce91e4…`.
- So the REBUILD-LOG.md value is stale (transcribed from the superseded
  00:20 run); the file on disk IS the fully-gated file. Synced as
  `6fce91e4…` (3,381,661 B) and the KIT updated to that SHA — using the stale
  log value in the KIT would have made the KIT disagree with the production
  file. **Parent action: correct the R2 log's ru-it web SHA to `6fce91e4…`
  (3,381,661 B) so the record matches the shipped file.**

Also noted (pre-existing KIT drift, now resolved by this sync):
- nl-ru KIT web line was stale vs BEFORE (`1a174743…`, 1,661,392 B vs the
  production BEFORE file `df6c3a7c…`, 1,661,395 B — web rebuilt 23:10–23:58 Nov 11
  without a KIT update, per the R3 log §1).
- pt-ru KIT §6 line was stale vs BEFORE (print 12,916,544 B `d2822ae0…` vs
  production BEFORE 12,916,388 B `86447421…`; web 1,151,627 B `a6a5f25f…` vs
  production BEFORE 1,188,611 B `c7017796…`).
- zh-cn-ru KIT Artifacts web line was stale vs BEFORE (2,486,423 B `8d3f72d3…`
  vs production BEFORE 2,486,429 B `a281456f…`).

## 2. KIT §5+§7 updates (print/web SHA + size only)

Only the lines stating the CURRENT build's print/web SHA-256, file bytes, and
web pdftotext bytes were changed. No other section touched; no historical Fix
record rewritten; D5 items frozen. (Note: in the ru-* KITs §7 holds only
historical Fix records and the previous build's gate lines — no current-state
print/web SHA/size lines existed there to update. For the other four KITs the
current-state lines live in their own equivalent sections: ru-zh-tw §1
Deliverables table, nl-ru "Files delivered", pt-ru §6 Gate record,
zh-cn-ru "Artifacts (final)".)

pdftotext bytes were measured on the synced files with webpdf.py's own method
(`pdftotext <pdf> - | wc -c`); print = web for all 8, confirming the text-layer
identity the R2/R3 logs record.

| Edition | KIT lines changed | New values |
|---|---|---|
| ru-it | §5 L53–54 (print/web SHA+bytes), L56 (pdftotext bytes) | print 21,263,401 B `12f897b2…`; web 3,381,661 B `6fce91e4…`; pdftotext 57,869 (was 57,843) |
| ru-pt | §5 L53–54, L56 | print 21,203,097 B `9057a1e3…`; web 3,381,069 B `0868cfa4…`; pdftotext 58,433 (was 58,390) |
| ru-nl | §5 L53–54, L56 | print 21,289,183 B `2bd4e0f2…`; web 3,384,838 B `390d4050…`; pdftotext 58,046 (was 58,009) |
| ru-ja | §5 L53–54, L56 | print 27,407,117 B `38a6efb0…`; web 3,719,047 B `89973dd7…`; pdftotext 58,627 (was 58,610) |
| ru-zh-tw | §1 Deliverables table, print + web rows | print 24,781,766 B `dbd7a52a…`; web 3,992,096 B `d7787a5e…` |
| nl-ru | "Files delivered", print + web lines | print 12,718,074 B `b9847bb2…`; web 1,661,043 B `cbaac2df…`; pdftotext 55,022 (was 55,000) |
| pt-ru | §6 Gate record line 50 | print 12,916,087 B `a3b022bc…`; web 1,188,302 B `0cdf7167…`; text bytes 55,001 (was 54,994) |
| zh-cn-ru | "Artifacts (final)", print + web lines | print 33,572,048 B `f1b2162d…`; web 2,485,880 B `dbf960ab…` |

Verification after edit: each new SHA appears exactly once in its KIT; the
old current-state SHAs are gone from the §5/current-state lines (they remain
only inside the §7/§9 historical Fix records, which is correct history).
The 8 edition dirs are untracked in git (`??`), so no `git diff` baseline
exists; verification was by direct grep/read of the edited lines.
pdftotext bytes measured on synced files: ru-it 57,869; ru-pt 58,433;
ru-nl 58,046; ru-ja 58,627; ru-zh-tw 56,176; nl-ru 55,022; pt-ru 55,001;
zh-cn-ru 52,559. (ru-it/ru-ja/nl-ru/pt-ru/zh-cn-ru match the R2/R3 log values;
ru-pt, ru-nl, ru-zh-tw were not given in the logs and are measured here.)

## 3. Freeze re-baseline (on the synced files)

Method (per the wave-C note + `scratch-ru-rebuild-C/gates.py`): for each
edition, `tools/venv/bin/python tools/freeze.py baseline --build
production/2026-w47/2026-w47-<ed> --core-svg production/2026-w47/2026-w47-<ed>/svg
--out <this dir>/freeze-<ed>`, then a direct SHA-256 comparison of the freeze
rebuild's SVGs against the scratch build1 SVGs that produced the synced PDFs,
plus a check that the freeze rebuild's print PDF is byte-identical to the
synced print PDF.

Scope note: this sync copies PDFs only (per task); the production `svg/` dirs
still hold the PRE-`_run_w` build's SVGs (verified 0/8 vs the scratch rebuilds
for all 8 editions before the copy). Therefore the tool's own baseline number
(rebuild vs the shipped `svg/`) is EXPECTED to be 0/8 — the SVGs genuinely
changed, that is the point of the rebuild. The reproducibility proof is the
direct comparison against the scratch build1 SVGs. The KIT §7 freeze lines
still describe the previous build's gate (they were not rewritten — they are
historical records); the production `svg/` refresh is out of this task's scope.

Results (runs 2026-11-12 ~02:05–02:20 UTC; `freeze-<ed>.log` + `freeze-results-batch*.json`,
`freeze-direct-fixed.json` in this dir):

| Edition | Tool baseline vs shipped `svg/` | Direct: freeze-regenerated SVGs vs scratch build1 SVGs | Fresh SVGs landed in |
|---|---|---|---|
| ru-it | 0/8 (rc=1) | **8/8** | build-copy/svg |
| ru-pt | 0/8 (rc=1) | **8/8** | build-copy/svg |
| ru-nl | 0/8 (rc=1) | **8/8** | build-copy/svg |
| ru-ja | 0/8 (rc=1) | **8/8** | build-copy/svg |
| ru-zh-tw | 0/8 (rc=1) | **8/8** | build-copy/svg |
| nl-ru | 0/8 (rc=1) | **8/8** | build-copy/svg |
| pt-ru | 0/8 (rc=1) | **8/8** | build-copy/svg |
| zh-cn-ru | 0/8 (rc=1) | **8/8** | `<out>/svg` (repointed) |

- Tool baseline 0/8 is the expected consequence of the stale shipped `svg/`
  (see scope note), not a reproducibility failure: the tool's own log shows the
  "produced" hashes are the NEW SVGs (e.g. zh-cn-ru p1 produced `0f06f1ec…` =
  scratch build1), differing from the shipped ones by design. The tool also
  confirms "shipped core SVGs unchanged by the run (8 files re-hashed)".
- **zh-cn-ru 0/8 scare — my script's bug, corrected, NOT a real failure.** The
  first direct-compare script overwrote the fresh `<out>/svg` entries with the
  stale `build-copy/svg` entries (same basenames) because zh-cn-ru is the one
  edition whose run outputs are repointed out of the copy (freeze log:
  "repointed files: render.py, content56/7/12/34/8.py"; the other 7 say
  "repointed files: none" and regenerate in place). Re-run with freeze.py's
  own collection rule (`<out>/svg` wins over `build-copy/svg`):
  **zh-cn-ru 8/8** (`freeze-direct-fixed.json`). All 8 editions are 8/8.
- **Print-PDF check in the freeze driver: VOID, withdrawn.** The driver's
  "freeze print PDF == synced: True" compared the build-copy PDF, but
  `freeze.py baseline` only runs `run.py`, never `render.py` — the build-copy
  PDF is just the copied synced file (mtime preserved from the scratch build),
  so the match proves nothing. It is NOT claimed as evidence here. PDF
  reproducibility evidence remains the R2/R3 workers' own build1-vs-build2
  byte-identical print PDFs (freeze 8/8 in their logs). The freeze re-baseline
  proves SVG-level reproducibility from the synced sources: 8/8 for all 8.
- Freeze outputs: the bulky `freeze-<ed>/build-copy/` dirs (~325 MB total)
  were deleted after the check (reproducible intermediates); logs + result
  JSONs kept in this dir.

## 4. Final production-integrity check

Re-hashed text.md + print + web for all 8 editions after the freeze runs
(2026-11-12 ~02:21 UTC): **24/24 OK, 0 mismatches.**

- text.md: byte-identical to the recorded BEFORE SHAs for all 8 editions
  (spacing-only rebuilds — no text.md was copied or modified).
- print/web: equal to the scratch SHAs for all 8 editions (ru-it web against
  `6fce91e4…`, the gated file — see §1a).
- KIT new SHAs verified to match the production files (spot-checked ru-it +
  zh-cn-ru; all 16 new SHAs were verified present exactly once in their KITs
  at edit time, §2).
- Disk at end: 99G used / 150G (the 100G stop line was never crossed; the
  freeze build-copy cleanup freed ~325 MB).

## 5. Files in this scratch dir

- `SYNC-LOG.md` (this file), `freeze_run.py` + `freeze_run2.py` (freeze drivers,
  batches 1–2), `freeze-<ed>.log` + `freeze-results-batch1.json` /
  `freeze-results-batch2.json` + `freeze-direct-fixed.json` (per-edition freeze
  runs; the corrected direct comparison), `freeze-<ed>/` (now empty dirs —
  the bulky build-copy outputs were deleted after the check; logs kept).
- Copy record: `/tmp/sync_copy_record.json` (per-file before/after SHA+size).
- Verification scripts used: `/tmp/verify_scratch.py`, `/tmp/sync_copy.py`,
  `/tmp/cmp_svg.py`, `/tmp/freeze_direct_fix.py`, `/tmp/final_integrity.py`
  (ephemeral; results recorded in this log).
