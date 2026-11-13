# W47 disk cleanup log — scratch-cleanup-disk99

Date: 2026-11-12 ~02:10–02:30 UTC (run 2026-11-11 21:18 EST → 02:3x UTC). Operator: cleanup subagent.
Scope: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/` and
`~/workspace/weekly-git/hidden_files/w47/`. Read-only audit first, SHA-verified deletions only.
No build, render, commit, push, or production change of any kind.

## df before / after

| moment | df -h Used | df -k Used |
|---|---|---|
| start of task | 99G | — (only -h taken) |
| mid-task (trash-location check) | 100G | 103,648,400 KB |
| after deletions | 100G | 103,511,732 KB |

**Note on df:** the volume is 150G; the binding line is the ~100–105G quota, not the
filesystem size. `df -h` reached **100G used during the work** (concurrent workers kept
writing while this cleanup ran). Deletions are the remedy for that line, not a risk to it,
so the verified deletions were completed and are reported here; no space-consuming work
was done. Gross freed by verified deletions: **423,316,331 B (403.7 MB)**. Net df change
over the same window was only −136,668 KB (~133 MB) because concurrent workers wrote
~280 MB while the cleanup ran (103,648,400 → 103,511,732 KB).

**Trash:** `gio trash` was checked and NOT used: the Trash location (`~/.local/share/Trash`)
is on the same filesystem (`/dev/mapper/rv`, same as the workspace), so trashing would move
bytes without freeing any quota. Per the task's own fallback, `rm` was used instead, with
every deleted path + size + SHA-256 recorded below and in `deleted-manifest.tsv`.
No `trash`/`trash-put` CLI is installed (only `gio`).

## Result summary

- **Deleted: 172 files, 423,316,331 B (403.7 MB)**, 0 failures/skips (every file re-verified by SHA+size immediately before `rm`).
- **Target ≥2G NOT reached.** Only ~0.4G passed all four rules; the ~9.4G fanout/refanout bulk is audit-only this round (see §5). No deletion was forced.
- No directory was removed. Every deleted file's parent dir still holds kept files (sources, KIT, logs, cards, assets) — except `scratch-ru-rebuild-C/*/backup-before/`, whose 10 files each were all verified duplicates and are now empty dirs (kept, not removed).

| verdict | files | bytes | meaning |
|---|---|---|---|
| DELETE-DUP-KEEP-ONE(freeze) | 12 | 267,395,023 (255.0 MB) | log AFTER print PDF; freeze copy deleted, build/build-copy copy KEPT (one survivor per build) |
| DELETE-DUP-PROD | 146 | 106,626,381 (101.7 MB) | byte-identical (SHA-256) to the same file in production NOW |
| DELETE-SUPERSEDED-R-KEPT | 12 | 41,274,366 (39.4 MB) | log AFTER SHA; newer verified build exists in R1/R2 scratch; same bytes kept in R1/R2 |
| DELETE-SUPERSEDED-R-KEPT(C-web) | 2 | 8,020,561 (7.6 MB) | C-log before.json SHA; superseded; newer build in R1/R2; same bytes kept in R1/R2 |

Key verification facts: production-current print/web SHAs for all 7 wave-A/B editions
(ru-it/ja/nl/pt/de/en/fr) + ru-es + ru-zh-tw + core-ru were confirmed present in R1/R2
scratch (build1/build2) — i.e. the newer verified build exists in R-scratch for every
edition touched. The wave-A/B AFTER web PDFs also survive byte-identical in R1/R2 build2
copies. Production files were NOT modified: spot-checked SHAs after deletion still match
the pre-deletion values (ru-it print `12f897b2…`, ru-it web `6fce91e4…`, ru-ko print `78e4442a…`).

## Deleted files (full list — same as deleted-manifest.tsv)

| path (relative to hidden_files/w47/) | size (B) | SHA-256 (first 12) | verdict |
|---|---|---|---|
| scratch-ru-rebuild-C/core-ru/backup-before/Lucerna-VOL4-web.pdf | 4,025,900 | b5d67aeb059a | DELETE-SUPERSEDED-R-KEPT(C-web) |
| scratch-ru-rebuild-C/core-ru/backup-before/p1-pervaya.svg | 1,071,118 | 409d5c2d5f79 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/core-ru/backup-before/p2-zhizn.svg | 1,104,911 | 370a2470f20d | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/core-ru/backup-before/p3-kultura.svg | 94,897 | 9c0de9072ddf | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/core-ru/backup-before/p4-sport.svg | 394,682 | 3f330829f0f9 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/core-ru/backup-before/p5-molodezh.svg | 816,532 | 2441db435350 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/core-ru/backup-before/p6-razbor.svg | 99,133 | c6f816791724 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/core-ru/backup-before/p7-yazyk.svg | 613,265 | 6679e1aa8369 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/core-ru/backup-before/p8-test.svg | 912,955 | 6ad2c7f1b434 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-ko/backup-before/Lucerna-VOL4-ru-ko-web.pdf | 3,513,245 | 34e1c1db929f | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-ko/backup-before/Lucerna-VOL4-ru-ko.pdf | 22,007,810 | 78e4442af8af | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-ko/backup-before/p1-pervaya.svg | 1,071,177 | 739fd1e9237d | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-ko/backup-before/p2-zhizn.svg | 1,105,145 | 8cea636d1dc4 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-ko/backup-before/p3-kultura.svg | 95,193 | 14169503011c | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-ko/backup-before/p4-sport.svg | 394,656 | 5f7b29992026 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-ko/backup-before/p5-molodezh.svg | 816,592 | c54640eb44a7 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-ko/backup-before/p6-razbor.svg | 99,434 | a0ca511b111d | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-ko/backup-before/p7-yazyk.svg | 613,098 | 13d5371b8069 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-ko/backup-before/p8-test.svg | 331,205 | 72cdd704cf7f | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-zh-tw/backup-before/Lucerna-VOL4-ru-zh-tw-web.pdf | 3,994,661 | eba60ec2f70f | DELETE-SUPERSEDED-R-KEPT(C-web) |
| scratch-ru-rebuild-C/ru-zh-tw/backup-before/p1-pervaya.svg | 1,071,037 | 828a6c0ef57f | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-zh-tw/backup-before/p2-zhizn.svg | 1,104,922 | fa4eb6ad7a9b | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-zh-tw/backup-before/p3-kultura.svg | 94,908 | 09389ff6f123 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-zh-tw/backup-before/p4-sport.svg | 394,693 | 408165ff7982 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-zh-tw/backup-before/p5-molodezh.svg | 816,543 | 02c8ca94f522 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-zh-tw/backup-before/p6-razbor.svg | 99,144 | fe6276d22c64 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-zh-tw/backup-before/p7-yazyk.svg | 613,147 | 6e46558ba2d7 | DELETE-DUP-PROD |
| scratch-ru-rebuild-C/ru-zh-tw/backup-before/p8-test.svg | 912,965 | d1c10d0b911f | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/build/build-copy/svg/p1-pervaya.svg | 1,070,607 | fdaf10db3f5d | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/build/build-copy/svg/p2-zhizn.svg | 1,106,129 | 5ba325695470 | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/build/build-copy/svg/p3-kultura.svg | 94,974 | 533ca6240a6d | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/build/build-copy/svg/p4-sport.svg | 394,749 | 059d90540af9 | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/build/build-copy/svg/p5-molodezh.svg | 816,624 | 9f5c73428031 | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/build/build-copy/svg/p6-razbor.svg | 99,288 | b3d7a1d995cb | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/build/build-copy/svg/p7-yazyk.svg | 612,630 | c29e36046487 | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/build/build-copy/svg/p8-test.svg | 219,518 | 685746183fbc | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze1/build-copy/Lucerna-VOL4-ru-it-web.pdf | 3,382,725 | 37a31f2d6ef2 | DELETE-SUPERSEDED-R-KEPT |
| scratch-ru-rebuild-it/gates/freeze1/build-copy/Lucerna-VOL4-ru-it.pdf | 21,264,469 | 6f123397a03f | DELETE-DUP-KEEP-ONE(freeze) |
| scratch-ru-rebuild-it/gates/freeze1/build-copy/svg/p1-pervaya.svg | 1,070,607 | fdaf10db3f5d | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze1/build-copy/svg/p2-zhizn.svg | 1,106,129 | 5ba325695470 | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze1/build-copy/svg/p3-kultura.svg | 94,974 | 533ca6240a6d | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze1/build-copy/svg/p4-sport.svg | 394,749 | 059d90540af9 | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze1/build-copy/svg/p5-molodezh.svg | 816,624 | 9f5c73428031 | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze1/build-copy/svg/p6-razbor.svg | 99,288 | b3d7a1d995cb | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze1/build-copy/svg/p7-yazyk.svg | 612,630 | c29e36046487 | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze1/build-copy/svg/p8-test.svg | 219,518 | 685746183fbc | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze2/build-copy/Lucerna-VOL4-ru-it-web.pdf | 3,382,725 | 37a31f2d6ef2 | DELETE-SUPERSEDED-R-KEPT |
| scratch-ru-rebuild-it/gates/freeze2/build-copy/Lucerna-VOL4-ru-it.pdf | 21,264,469 | 6f123397a03f | DELETE-DUP-KEEP-ONE(freeze) |
| scratch-ru-rebuild-it/gates/freeze2/build-copy/svg/p1-pervaya.svg | 1,070,607 | fdaf10db3f5d | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze2/build-copy/svg/p2-zhizn.svg | 1,106,129 | 5ba325695470 | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze2/build-copy/svg/p3-kultura.svg | 94,974 | 533ca6240a6d | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze2/build-copy/svg/p4-sport.svg | 394,749 | 059d90540af9 | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze2/build-copy/svg/p5-molodezh.svg | 816,624 | 9f5c73428031 | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze2/build-copy/svg/p6-razbor.svg | 99,288 | b3d7a1d995cb | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze2/build-copy/svg/p7-yazyk.svg | 612,630 | c29e36046487 | DELETE-DUP-PROD |
| scratch-ru-rebuild-it/gates/freeze2/build-copy/svg/p8-test.svg | 219,518 | 685746183fbc | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/build/build-copy/svg/p1-pervaya.svg | 1,070,608 | d36cb640dc52 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/build/build-copy/svg/p2-zhizn.svg | 1,106,137 | a44343f604e6 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/build/build-copy/svg/p3-kultura.svg | 94,952 | f9bfa1ad33ef | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/build/build-copy/svg/p4-sport.svg | 394,412 | a9922c229b7d | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/build/build-copy/svg/p5-molodezh.svg | 816,624 | 88eca8d6dff7 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/build/build-copy/svg/p6-razbor.svg | 99,187 | d9c308195b5c | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/build/build-copy/svg/p7-yazyk.svg | 613,442 | a425edb2845c | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/build/build-copy/svg/p8-test.svg | 267,991 | b5a1d06e129b | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze1/build-copy/Lucerna-VOL4-ru-ja-web.pdf | 3,720,196 | 8b7b38d48753 | DELETE-SUPERSEDED-R-KEPT |
| scratch-ru-rebuild-ja/gates/freeze1/build-copy/Lucerna-VOL4-ru-ja.pdf | 27,408,235 | d681cf978839 | DELETE-DUP-KEEP-ONE(freeze) |
| scratch-ru-rebuild-ja/gates/freeze1/build-copy/svg/p1-pervaya.svg | 1,070,608 | d36cb640dc52 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze1/build-copy/svg/p2-zhizn.svg | 1,106,137 | a44343f604e6 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze1/build-copy/svg/p3-kultura.svg | 94,952 | f9bfa1ad33ef | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze1/build-copy/svg/p4-sport.svg | 394,412 | a9922c229b7d | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze1/build-copy/svg/p5-molodezh.svg | 816,624 | 88eca8d6dff7 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze1/build-copy/svg/p6-razbor.svg | 99,187 | d9c308195b5c | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze1/build-copy/svg/p7-yazyk.svg | 613,442 | a425edb2845c | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze1/build-copy/svg/p8-test.svg | 267,991 | b5a1d06e129b | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze2/build-copy/Lucerna-VOL4-ru-ja-web.pdf | 3,720,196 | 8b7b38d48753 | DELETE-SUPERSEDED-R-KEPT |
| scratch-ru-rebuild-ja/gates/freeze2/build-copy/Lucerna-VOL4-ru-ja.pdf | 27,408,235 | d681cf978839 | DELETE-DUP-KEEP-ONE(freeze) |
| scratch-ru-rebuild-ja/gates/freeze2/build-copy/svg/p1-pervaya.svg | 1,070,608 | d36cb640dc52 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze2/build-copy/svg/p2-zhizn.svg | 1,106,137 | a44343f604e6 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze2/build-copy/svg/p3-kultura.svg | 94,952 | f9bfa1ad33ef | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze2/build-copy/svg/p4-sport.svg | 394,412 | a9922c229b7d | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze2/build-copy/svg/p5-molodezh.svg | 816,624 | 88eca8d6dff7 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze2/build-copy/svg/p6-razbor.svg | 99,187 | d9c308195b5c | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze2/build-copy/svg/p7-yazyk.svg | 613,442 | a425edb2845c | DELETE-DUP-PROD |
| scratch-ru-rebuild-ja/gates/freeze2/build-copy/svg/p8-test.svg | 267,991 | b5a1d06e129b | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/build/build-copy/svg/p1-pervaya.svg | 1,070,495 | c4f4f0cda6cf | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/build/build-copy/svg/p2-zhizn.svg | 1,106,197 | 870e5c5b6811 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/build/build-copy/svg/p3-kultura.svg | 94,893 | af3b4ae2ed02 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/build/build-copy/svg/p4-sport.svg | 394,557 | 67383c6d2292 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/build/build-copy/svg/p5-molodezh.svg | 816,558 | 7537c66f4307 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/build/build-copy/svg/p6-razbor.svg | 99,293 | df9c33cc3e4d | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/build/build-copy/svg/p7-yazyk.svg | 612,393 | 80faea519a35 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/build/build-copy/svg/p8-test.svg | 219,982 | c07cb075072d | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze1/build-copy/Lucerna-VOL4-ru-nl-web.pdf | 3,385,859 | db2f1c4d6bf1 | DELETE-SUPERSEDED-R-KEPT |
| scratch-ru-rebuild-nl/gates/freeze1/build-copy/Lucerna-VOL4-ru-nl.pdf | 21,290,182 | 6579cf5fc3ea | DELETE-DUP-KEEP-ONE(freeze) |
| scratch-ru-rebuild-nl/gates/freeze1/build-copy/svg/p1-pervaya.svg | 1,070,495 | c4f4f0cda6cf | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze1/build-copy/svg/p2-zhizn.svg | 1,106,197 | 870e5c5b6811 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze1/build-copy/svg/p3-kultura.svg | 94,893 | af3b4ae2ed02 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze1/build-copy/svg/p4-sport.svg | 394,557 | 67383c6d2292 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze1/build-copy/svg/p5-molodezh.svg | 816,558 | 7537c66f4307 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze1/build-copy/svg/p6-razbor.svg | 99,293 | df9c33cc3e4d | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze1/build-copy/svg/p7-yazyk.svg | 612,393 | 80faea519a35 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze1/build-copy/svg/p8-test.svg | 219,982 | c07cb075072d | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze2/build-copy/Lucerna-VOL4-ru-nl-web.pdf | 3,385,859 | db2f1c4d6bf1 | DELETE-SUPERSEDED-R-KEPT |
| scratch-ru-rebuild-nl/gates/freeze2/build-copy/Lucerna-VOL4-ru-nl.pdf | 21,290,182 | 6579cf5fc3ea | DELETE-DUP-KEEP-ONE(freeze) |
| scratch-ru-rebuild-nl/gates/freeze2/build-copy/svg/p1-pervaya.svg | 1,070,495 | c4f4f0cda6cf | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze2/build-copy/svg/p2-zhizn.svg | 1,106,197 | 870e5c5b6811 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze2/build-copy/svg/p3-kultura.svg | 94,893 | af3b4ae2ed02 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze2/build-copy/svg/p4-sport.svg | 394,557 | 67383c6d2292 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze2/build-copy/svg/p5-molodezh.svg | 816,558 | 7537c66f4307 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze2/build-copy/svg/p6-razbor.svg | 99,293 | df9c33cc3e4d | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze2/build-copy/svg/p7-yazyk.svg | 612,393 | 80faea519a35 | DELETE-DUP-PROD |
| scratch-ru-rebuild-nl/gates/freeze2/build-copy/svg/p8-test.svg | 219,982 | c07cb075072d | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/build/build-copy/svg/p1-pervaya.svg | 1,070,526 | 9c7a128b5574 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/build/build-copy/svg/p2-zhizn.svg | 1,105,978 | a8757d6cdb7c | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/build/build-copy/svg/p3-kultura.svg | 95,089 | 5183be0d58cc | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/build/build-copy/svg/p4-sport.svg | 394,573 | de015f4c1d97 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/build/build-copy/svg/p5-molodezh.svg | 816,631 | abeefda77383 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/build/build-copy/svg/p6-razbor.svg | 99,278 | fd9e375284d0 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/build/build-copy/svg/p7-yazyk.svg | 612,660 | dd83d6cf3909 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/build/build-copy/svg/p8-test.svg | 219,553 | 64c80d824e3c | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze1/build-copy/Lucerna-VOL4-ru-pt-web.pdf | 3,382,131 | 38b7fa500c5a | DELETE-SUPERSEDED-R-KEPT |
| scratch-ru-rebuild-pt/gates/freeze1/build-copy/Lucerna-VOL4-ru-pt.pdf | 21,204,114 | b4a3fdfebc3f | DELETE-DUP-KEEP-ONE(freeze) |
| scratch-ru-rebuild-pt/gates/freeze1/build-copy/svg/p1-pervaya.svg | 1,070,526 | 9c7a128b5574 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze1/build-copy/svg/p2-zhizn.svg | 1,105,978 | a8757d6cdb7c | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze1/build-copy/svg/p3-kultura.svg | 95,089 | 5183be0d58cc | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze1/build-copy/svg/p4-sport.svg | 394,573 | de015f4c1d97 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze1/build-copy/svg/p5-molodezh.svg | 816,631 | abeefda77383 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze1/build-copy/svg/p6-razbor.svg | 99,278 | fd9e375284d0 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze1/build-copy/svg/p7-yazyk.svg | 612,660 | dd83d6cf3909 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze1/build-copy/svg/p8-test.svg | 219,553 | 64c80d824e3c | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze2/build-copy/Lucerna-VOL4-ru-pt-web.pdf | 3,382,131 | 38b7fa500c5a | DELETE-SUPERSEDED-R-KEPT |
| scratch-ru-rebuild-pt/gates/freeze2/build-copy/Lucerna-VOL4-ru-pt.pdf | 21,204,114 | b4a3fdfebc3f | DELETE-DUP-KEEP-ONE(freeze) |
| scratch-ru-rebuild-pt/gates/freeze2/build-copy/svg/p1-pervaya.svg | 1,070,526 | 9c7a128b5574 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze2/build-copy/svg/p2-zhizn.svg | 1,105,978 | a8757d6cdb7c | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze2/build-copy/svg/p3-kultura.svg | 95,089 | 5183be0d58cc | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze2/build-copy/svg/p4-sport.svg | 394,573 | de015f4c1d97 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze2/build-copy/svg/p5-molodezh.svg | 816,631 | abeefda77383 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze2/build-copy/svg/p6-razbor.svg | 99,278 | fd9e375284d0 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze2/build-copy/svg/p7-yazyk.svg | 612,660 | dd83d6cf3909 | DELETE-DUP-PROD |
| scratch-ru-rebuild-pt/gates/freeze2/build-copy/svg/p8-test.svg | 219,553 | 64c80d824e3c | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-de/build/build-copy/svg/p1-pervaya.svg | 1,070,507 | c496022d6ea8 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-de/build/build-copy/svg/p2-zhizn.svg | 1,105,836 | 4590b41d027c | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-de/build/build-copy/svg/p3-kultura.svg | 94,893 | f1e9f5e36f55 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-de/build/build-copy/svg/p4-sport.svg | 394,760 | db9391e4c21f | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-de/build/build-copy/svg/p5-molodezh.svg | 816,329 | 192aa2e13259 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-de/build/build-copy/svg/p6-razbor.svg | 99,718 | 14ae25471eaf | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-de/build/build-copy/svg/p7-yazyk.svg | 613,118 | 729792f0aa71 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-de/build/build-copy/svg/p8-test.svg | 219,662 | 269905be70aa | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-de/freeze-baseline/build-copy/Lucerna-VOL4-ru-de-web.pdf | 3,384,428 | 05b0a7abf59a | DELETE-SUPERSEDED-R-KEPT |
| scratch-ru-rebuild-ru-de/freeze-baseline/build-copy/Lucerna-VOL4-ru-de.pdf | 21,230,193 | 80024034da68 | DELETE-DUP-KEEP-ONE(freeze) |
| scratch-ru-rebuild-ru-en/build/build-copy/svg/p1-pervaya.svg | 1,070,708 | 5f531b863310 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-en/build/build-copy/svg/p2-zhizn.svg | 1,106,099 | d632cba2af94 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-en/build/build-copy/svg/p3-kultura.svg | 94,895 | 00ff048bbe7c | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-en/build/build-copy/svg/p4-sport.svg | 394,529 | f9abc1a5dcf0 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-en/build/build-copy/svg/p5-molodezh.svg | 816,796 | 3dd2f2b38c9a | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-en/build/build-copy/svg/p6-razbor.svg | 99,270 | 0794684a414d | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-en/build/build-copy/svg/p7-yazyk.svg | 613,192 | 83d715a15a78 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-en/build/build-copy/svg/p8-test.svg | 219,013 | 8bb21fd23e69 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-en/freeze-baseline/build-copy/Lucerna-VOL4-ru-en-web.pdf | 3,379,458 | 7e67d0069ad0 | DELETE-SUPERSEDED-R-KEPT |
| scratch-ru-rebuild-ru-en/freeze-baseline/build-copy/Lucerna-VOL4-ru-en.pdf | 21,249,828 | 1fcc6aa4101b | DELETE-DUP-KEEP-ONE(freeze) |
| scratch-ru-rebuild-ru-fr/build/build-copy/svg/p1-pervaya.svg | 1,070,523 | 0fc838b4ec3a | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-fr/build/build-copy/svg/p2-zhizn.svg | 1,105,948 | 591c647fe2a8 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-fr/build/build-copy/svg/p3-kultura.svg | 94,998 | 0ce42ebe1193 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-fr/build/build-copy/svg/p4-sport.svg | 394,540 | aac7c190b12d | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-fr/build/build-copy/svg/p5-molodezh.svg | 816,533 | b681cfbf578f | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-fr/build/build-copy/svg/p6-razbor.svg | 99,307 | d717bddb1df4 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-fr/build/build-copy/svg/p7-yazyk.svg | 613,859 | da6994a4647f | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-fr/build/build-copy/svg/p8-test.svg | 219,357 | ff1d226901d0 | DELETE-DUP-PROD |
| scratch-ru-rebuild-ru-fr/freeze-baseline/build-copy/Lucerna-VOL4-ru-fr-web.pdf | 3,384,329 | 2eb8062cbb0c | DELETE-SUPERSEDED-R-KEPT |
| scratch-ru-rebuild-ru-fr/freeze-baseline/build-copy/Lucerna-VOL4-ru-fr.pdf | 21,290,501 | 32f2e1688c71 | DELETE-DUP-KEEP-ONE(freeze) |
| scratch-ru-rebuild-ru-fr/freeze-baseline2/build-copy/Lucerna-VOL4-ru-fr-web.pdf | 3,384,329 | 2eb8062cbb0c | DELETE-SUPERSEDED-R-KEPT |
| scratch-ru-rebuild-ru-fr/freeze-baseline2/build-copy/Lucerna-VOL4-ru-fr.pdf | 21,290,501 | 32f2e1688c71 | DELETE-DUP-KEEP-ONE(freeze) |

## Kept survivors (one per superseded AFTER print build)

The build/build-copy print PDF of each wave-A/B rebuild was KEPT as the single surviving
copy of that superseded build (rule (c)); only its freeze copies were deleted:

- `scratch-ru-rebuild-it/build/build-copy/Lucerna-VOL4-ru-it.pdf` (21,264,469 B) — log AFTER SHA, one copy kept; freeze copies deleted.
- `scratch-ru-rebuild-ja/build/build-copy/Lucerna-VOL4-ru-ja.pdf` (27,408,235 B) — log AFTER SHA, one copy kept; freeze copies deleted.
- `scratch-ru-rebuild-nl/build/build-copy/Lucerna-VOL4-ru-nl.pdf` (21,290,182 B) — log AFTER SHA, one copy kept; freeze copies deleted.
- `scratch-ru-rebuild-pt/build/build-copy/Lucerna-VOL4-ru-pt.pdf` (21,204,114 B) — log AFTER SHA, one copy kept; freeze copies deleted.
- `scratch-ru-rebuild-ru-de/build/build-copy/Lucerna-VOL4-ru-de.pdf` (21,230,193 B) — log AFTER SHA, one copy kept; freeze copies deleted.
- `scratch-ru-rebuild-ru-en/build/build-copy/Lucerna-VOL4-ru-en.pdf` (21,249,828 B) — log AFTER SHA, one copy kept; freeze copies deleted.
- `scratch-ru-rebuild-ru-fr/build/build-copy/Lucerna-VOL4-ru-fr.pdf` (21,290,501 B) — log AFTER SHA, one copy kept; freeze copies deleted.

## Candidates KEPT, with reasons

### (1) Single-copy superseded builds — rule (c) fails (only copy on disk)

| file | size | reason |
|---|---|---|
| scratch-ru-rebuild-it/build/build-copy/Lucerna-VOL4-ru-it-web.pdf | 3,384,121 | log BEFORE web PDF; no copy in production or R-scratch; deleting it would destroy the only copy |
| scratch-ru-rebuild-ja/build/build-copy/Lucerna-VOL4-ru-ja-web.pdf | 3,721,620 | log BEFORE web PDF; no copy in production or R-scratch; deleting it would destroy the only copy |
| scratch-ru-rebuild-nl/build/build-copy/Lucerna-VOL4-ru-nl-web.pdf | 3,387,356 | log BEFORE web PDF; no copy in production or R-scratch; deleting it would destroy the only copy |
| scratch-ru-rebuild-pt/build/build-copy/Lucerna-VOL4-ru-pt-web.pdf | 3,383,561 | log BEFORE web PDF; no copy in production or R-scratch; deleting it would destroy the only copy |
| scratch-ru-rebuild-ru-de/build/build-copy/Lucerna-VOL4-ru-de-web.pdf | 3,385,861 | log BEFORE web PDF; no copy in production or R-scratch; deleting it would destroy the only copy |
| scratch-ru-rebuild-ru-en/build/build-copy/Lucerna-VOL4-ru-en-web.pdf | 3,380,920 | log BEFORE web PDF; no copy in production or R-scratch; deleting it would destroy the only copy |
| scratch-ru-rebuild-ru-fr/build/build-copy/Lucerna-VOL4-ru-fr-web.pdf | 3,385,807 | log BEFORE web PDF; no copy in production or R-scratch; deleting it would destroy the only copy |
| scratch-ru-rebuild-C/core-ru/backup-before/Lucerna-VOL4.pdf | 31,429,147 | C backup-before print PDF; production has moved on (R1/R2 build) and no other copy exists anywhere; deleting it would destroy the only copy of the pre-rebuild print |
| scratch-ru-rebuild-C/ru-zh-tw/backup-before/Lucerna-VOL4-ru-zh-tw.pdf | 24,784,332 | C backup-before print PDF; production has moved on (R1/R2 build) and no other copy exists anywhere; deleting it would destroy the only copy of the pre-rebuild print |

### (2) WebPDF freeze builds (italic-fix1 / patch1) — rule (b) cannot be established

Both `scratch-webpdf-italic-fix1/freeze/build-copy/` and `scratch-webpdf-patch1/freeze/build-copy/`
hold a ru-en freeze build (print `7b73070c2c11…`, 21,245,374 B, identical in both dirs;
web `6419f7ad188d…` / `82dfb6eaeff6…`; 8 SVGs each). Their SHAs match NO log BEFORE/AFTER SHA
(ru-en log: BEFORE `d12fa6a6…` / AFTER `1fcc6aa4…`), NO production file, and NO R-scratch file.
Per rule (b) ('if you cannot establish (b) from a log SHA or a production byte-comparison, KEEP'),
all 20 files kept (49.2 MB). The two print PDFs are duplicates of each other, but duplication
alone does not satisfy (b) — neither copy is verified superseded/reproducible.

### (3) Freeze-baseline SVGs (ru-de/ru-en/ru-fr) — 32 files, 17,659,458 B — rule (b) not met as written

These wave-A SVGs differ from production SVGs, but their bytes DO exist in kept R1 scratch
(e.g. `scratch-ru-rerun-R1/ru-de-1/build-copy/svg/p1-pervaya.svg`). They were nevertheless KEPT:
REBUILD-LOG.md records PDF SHAs only, never SVG SHAs, so rule (b) cannot be established 'from a
log SHA or a production byte-comparison' for them. If the rule is clarified to accept 'component
of a log-recorded superseded build whose bytes survive in R-scratch', these 32 files (list in
`verify2.json` under verdict DELETE-SVG-R-KEPT) are the next deletion candidates.

### (4) Everything else kept by class (not in rule (a), or off-limits)

- All `*.md` / `*.tsv` / `*.json` / `*.log` evidence, all `*.py` sources, KIT files, `text.md`,
  `ABSTRACT.txt`, assets (`*.jpg`, `lucerna-moth.svg`), and `cards/*.png` in every rebuild/webpdf/C dir.
  PNG cards are build outputs in the loose sense but are NOT in rule (a)'s enumerated classes
  (PDF, SVG, render-cache); quantified for a possible second round: ~7 MB per build-copy × 3 copies
  × 7 editions ≈ 150 MB in the wave-A/B rebuild dirs alone (verify before any decision).
- `__pycache__/*.pyc` (~200–500 KB/dir): bytecode cache, not a render cache; rule (b) not met; kept.
- `scratch-ru-rebuild-ru-es/` (112 KB): ru-es was NOT rebuilt (wave-A precondition stop); dir holds
  only its REBUILD-LOG.md + evidence. Nothing to delete.
- `scratch-ru-rebuild-C/` in full, except the verified files above: `core-ru/build/`, `ru-ko/build/`,
  `ru-zh-tw/build/` (the Medium builds — ru-ko is the ko-fix worker's 'before' reference), all
  `presync/` dirs, `before.json`/`final.json`/`now.json`, census/gates scripts. `core-ru/p8-baseline.svg` untouched.
- All off-limits dirs untouched (verified by manifest grep): `scratch-ru-rerun-R1/`, `scratch-ru-rerun-R2/`,
  `scratch-runw-rerun-R3/`, `scratch-runw-port/`, `scratch-core-ru-morozko/`, `scratch-new-gates/`,
  `scratch-sync-R2R3/`, `scratch-sync-R1/`, `scratch-runw-ko-fix/`, `scratch-gatefix-*/`, and the whole
  of `scratch-refanout-it2/` including `backup/` (430 files, 312 MB — re-verified intact after the run).
- WebPDF scratch dirs `scratch-webpdf-de-it-pt/`, `scratch-webpdf-en-es-fr/`, `scratch-webpdf-ko-zh/`,
  and weekly-git `scratch-webpdf-nl-ru-ja/` contain logs/scripts/evidence only — no PDFs at all.
  Nothing deletable there.

## Fanout / refanout audit (AUDIT ONLY — nothing deleted)

Per-dir contents by file class (files / MB). These are fanout/refanout edition build-copy trees
(same shape as the verified rebuild dirs) plus evidence. Bulk is build output (PDF/SVG/PNG/JPG);
the small evidence-only dirs hold no build outputs at all.

| dir | size | PDF | PNG | SVG | JPG | other notable |
|---|---|---|---|---|---|---|
| scratch-fanout-de | 5.2M | — | — | — | — | evidence only (json/log/txt/py/md) |
| scratch-fanout-de-rebuild-A | 2.2M | — | — | — | — | evidence only |
| scratch-fanout-de-rebuild-B | 1.9M | — | — | — | — | evidence only |
| scratch-fanout-en | 615M | 20 / 409.4 | 80 / 93.9 | 99 / 60.1 | 99 / 45.1 | evidence ~4 MB |
| scratch-fanout-en2 | 1.1G | 30 / 629.1 | 166 / 185.5 | 189 / 114.9 | 189 / 86.1 | evidence ~8 MB |
| scratch-fanout-es | 204M | 26 / 101.0 | 104 / 83.3 | 117 / 10.1 | 52 / 4.8 |  |
| scratch-fanout-fr | 85M | — | 94 / 76.4 | — | — | txt 63 / 4.5 MB; no PDFs |
| scratch-fanout-it | 347M | 20 / 179.7 | 80 / 67.7 | 173 / 64.5 | 90 / 28.9 |  |
| scratch-fanout-ja | 3.0M | — | — | — | — | evidence only |
| scratch-fanout-ko | 11M | — | 8 / 9.1 | — | — | evidence only otherwise |
| scratch-fanout-ko3 | 96M | — | 80 / 91.8 | — | — | evidence ~2 MB; no PDFs |
| scratch-fanout-nl | 1.2M | — | — | — | — | evidence only |
| scratch-fanout-pt | 443M | 24 / 283.1 | 96 / 83.2 | 108 / 41.2 | 60 / 28.3 |  |
| scratch-fanout-ru | 692M | 34 / 416.9 | 143 / 136.6 | 153 / 72.5 | 136 / 58.4 |  |
| scratch-fanout-zh-cn | 263M | 7 / 133.0 | 73 / 72.9 | 59 / 34.1 | 21 / 11.4 | other 21 / 4.7 MB |
| scratch-fanout-zh-tw | 596M | 36 / 373.3 | 144 / 144.5 | 242 / 50.8 | 108 / 18.7 |  |
| scratch-refanout-es | 313M | 40 / 150.0 | 174 / 128.7 | 180 / 15.7 | 80 / 7.3 |  |
| scratch-refanout-fr2 | 393M | 20 / 214.6 | 108 / 97.6 | 90 / 42.3 | 60 / 29.7 |  |
| scratch-refanout-it | 675M | 40 / 358.9 | 170 / 152.3 | 263 / 96.7 | 180 / 57.8 |  |
| scratch-refanout-it2 | 1.1G | 61 / 539.2 | 254 / 247.8 | 441 / 161.6 | 270 / 86.6 | PROTECTED: backup/ 430 files / 312 MB |
| scratch-refanout-nl | 382M | 20 / 167.5 | 226 / 149.6 | 90 / 31.0 | 100 / 29.7 |  |
| scratch-refanout-pt | 606M | 40 / 323.5 | 182 / 154.2 | 180 / 68.7 | 100 / 47.1 |  |
| scratch-refanout-ru | 858M | 40 / 491.6 | 160 / 160.7 | 191 / 85.8 | 248 / 106.5 |  |
| scratch-refanout-zh-tw | 976M | 58 / 605.8 | 244 / 249.0 | 349 / 72.8 | 174 / 30.1 |  |

**Totals across the 24 fanout/refanout dirs: ~9.4G** (PDF ~4.6G, PNG ~1.9G, SVG ~0.9G, JPG ~0.6G,
evidence/code ~0.2G; remainder is per-dir rounding).

**Reproducibility judgment (for a second round):** the PDF/SVG/PNG/JPG bulk is build output of
the same kind verified in §1 — generated from edition sources by `run_build.py`/`render.py`/
`webpdf.py`. In principle most of it is either byte-identical to production/R-scratch or a
superseded build reproducible from the kept sources. But NO per-file SHA verification was done
on these dirs this round (audit only, per task), so nothing here is cleared for deletion yet.
A second round should run the same SHA method used here (production byte-comparison + log SHA +
R-scratch copy check, keep-one-per-group) file by file; that is the only way to reach the ≥2G
target. Two policy questions for that round: (1) PNG cards — in or out of rule (a)? (~1.9G at
stake here, ~150 MB in the rebuild dirs); (2) SVG components of a log-recorded build whose bytes
survive in R-scratch — in or out of rule (b)? (32 files / 16.8 MB in the rebuild dirs, more here).
`scratch-refanout-it2/` stays protected until its family lands — audit only, no deletion, in any round.

## Files produced by this run

- `deleted-manifest.tsv` — full deletion manifest (path, size, SHA-256, verdict), 172 rows.
- `delete-summary.json` — counts/bytes + failure list (0 failures).
- This file (`CLEANUP-LOG.md`).
- Working verification scripts (not deliverables, in /tmp): `verify_cleanup.py`, `verify2.py`,
  `do_delete.py`, plus `/tmp/verify2.json` (per-file verdicts) and `/tmp/prod_cur.json`
  (production-current SHAs at verification time).

## What was NOT done

- No file under `production/` was read for writing, modified, or deleted (spot-check SHAs unchanged).
- No commit / push / lint. No build / render. No off-limits dir touched.
- The ≥2G target was not reached safely (0.40G freed). The next ~2G+ can only come from the
  fanout/refanout bulk, which needs a second, SHA-verified round (see §5).
