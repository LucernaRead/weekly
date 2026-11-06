# W45 KOxRU B-1 fix summary (2026-10-28, depth-2 fixer)
- Pre-fix snapshot: hidden_files/w45/ko-ru-fix/deliverables-snapshot-before.txt
- Post-fix snapshots: deliverables-snapshot-after.txt / after2.txt (identical hashes)
- Baseline repro (old transform): hidden_files/w45/ko-ru-fix/baseline-repro/ + baseline-diff.txt
- Fixed repro (final transform): hidden_files/w45/ko-ru-fix/fixed-repro2/ + fixed2-transform-out.txt + fixed2-run-out.txt
- Idempotent repro: hidden_files/w45/ko-ru-fix/idempotent-repro2/ + idempotent2-out.txt (276 skip, files unchanged)
- Negative controls: neg1 (corrupted P1 short gloss -> exit 1), neg2b (corrupted chained E-item final form in content8 -> exit 1)
- transform.py: before 2895b661... , final cc726487... ; REPL 257 unchanged, FIX2FIX3 19 added as second phase.
- KIT: files/weekly-report-w45-ko-ru/WEEKLY-KIT.md, section "Fix sync B-1" at line 106, plus Method correction and fix2/fix3 header corrections.
- NOT done (by design, coordinator's call): no finalization, no listing, no Discord, no weekly-git, no cron, no re-render of paper.
