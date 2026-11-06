## Fix sync B-1 (2026-10-28, transform.py + this KIT only — paper unchanged)

CORRECTION to the Method claim above and to the fix2/fix3 headers below: the claim
that every fix-round change had been appended to transform.py was FALSE for fix2/fix3.
Independent proof (hidden_files/w45/ko-ru-proof/REPORT.md §11/B-1) ran the shipped
transform.py alone on a fresh core copy (257 replacements passed) and found 19 fix2/fix3
short forms absent from transform.py (count 0 each), the delivered build files still in
their long forms, and a re-render in the overflow state (P1-headline overflow, P5-feature
overflow, P8-keys 2569 > 2540, P7 teaser 2695.46, p1/p5/p7/p8 SVGs differing). fix1 WAS
appended (REPL.update in transform.py); fix2/fix3 were not, until this sync.

This sync appends all 19 fix2/fix3 mappings verbatim to transform.py as a separate
second phase (FIX2FIX3), AFTER the main REPL phase: their sources are the RU long forms
that the main phase itself produces, so merging them into REPL would sort some of them
before their producer and assert-fail. Main REPL entries: 257, unchanged. FIX2FIX3: 19.
Idempotency (ko-it precedent): an entry whose source is absent but whose destination —
or, for a chained entry, its final form after later entries in the same pass (e.g. a f.ex
line whose dst still carries type "翻译", later rewritten to "Переведите") — or, for a
superseded main-phase entry, its fix short form — is already present is SKIPPED, not
failed. An entry with neither source nor destination/final/superseding form still FAILS
(verified by two negative controls: a corrupted P1 short gloss and a corrupted chained
E-item final form each make transform.py exit non-zero). No paper file, no build content
file, and nothing under tools/ was changed by this sync; the delivered SVGs/cards/PDFs
were NOT re-rendered.

### Synced entries (long → short, verbatim from fix2.py / fix3.py)

fix2 (12):
- fix2-1: `정리 = приводить в порядок, повторять · 끈끈하다 = липкий · 합격 = успешная сдача.` → `정리 = повторение · 끈끈하다 = липкий · 합격 = сдача.`
- fix2-2: `중점 = приоритетный · 배치하다 = размещать · 통제하다 = перекрывать, контролировать.` → `중점 = главный · 배치하다 = разместить · 통제하다 = перекрывать.`
- fix2-3: `챙기다 = приготовить заранее · 졸리다 = хотеть спать · 평소 = обычно.` → `챙기다 = приготовить · 졸리다 = сонливость · 평소 = обычно.`
- fix2-4: `비다 = молиться, желать · 피하다 = избегать · 미끄럽다 = скользкий.` → `비다 = молиться · 피하다 = избегать · 미끄럽다 = скользкий.`
- fix2-5: `Пик по прогнозу лесной службы по Нэчжансану — 4 ноября` → `Пик по лесной службе, Нэчжансан — 4 ноября`
- fix2-6: `Пик по прогнозу парковой корпорации по Нэчжансану — 11 ноября` → `Пик по парковой корпорации, Нэчжансан — 11 ноября`
- fix2-7: `Прогноз парковой корпорации по Нэчжансану — 11-е число` → `Прогноз парковой корпорации, Нэчжансан — 11-е`
- fix2-8: `С 13 часов 6 ноября — запись по всей стране на оставшиеся места` → `С 13 часов 6 ноября — запись на оставшиеся места`
- fix2-9: `Пик по прогнозу лесной службы по Вольчхульсану — 9 ноября` → `Пик по лесной службе, Вольчхульсан — 9 ноября`
- fix2-10: `К моменту сдачи в печать настоящих писем читателей и лучшего сочинения со стр. 8 не поступило: пример остаётся, а обещание переносится в VOL.3. Присылайте нам свои письма и свои тексты со стр. 8!` → `Настоящих писем и лучшего сочинения со стр. 8 к сдаче номера не поступило: пример остаётся, обещание — в VOL.3. Присылайте письма и тексты со стр. 8!`
- fix2-11: `cyq = fy + 66 + (i % 4) * 132` → `cyq = fy + 66 + (i % 4) * 102`
- fix2-12: `py = fy + 66 + 4 * 132 + 18` → `py = fy + 66 + 4 * 102 + 18`

fix3 (7):
- fix3-1: `입동 = ипдон, начало зимы · 절정 = пик, апогей · 김장 = заготовка кимчи на зиму · 상륙하다 = выйти на берег · 온대저기압 = внетропический циклон.` → `입동 = ипдон · 절정 = пик · 김장 = кимчжан · 상륙하다 = выйти на берег · 온대저기압 = циклон.`
- fix3-2: `Во время аудирования самолёты не взлетают и не садятся` → `Во время аудирования самолёты не летают`
- fix3-3: `Сотрудников безопасности в Сеуле на Хэллоуин — 3 271 человек` → `Безопасность в Сеуле на Хэллоуин — 3 271 человек`
- fix3-4: `С пожеланием успешной сдачи дарят тток из клейкого риса и ёт` → `С пожеланием сдачи дарят тток и ёт`
- fix3-5: `В день экзамена учреждения начинают работу в 10 часов` → `В день экзамена учреждения работают с 10 часов`
- fix3-6: `Во время аудирования в день экзамена самолёты ограничены` → `Самолёты ограничены во время аудирования`
- fix3-7: `На следующей неделе готовится к экзамену по истории Кореи` → `На следующей неделе — экзамен по истории Кореи`

### Repro validation (scratch only, tools venv python, OUT repointed to scratch)

- Fresh core copy + new transform.py alone: 276 ok (257 REPL + 19 FIX2FIX3), 0 skip, 0 fail.
- 6 content files: OUT-normalized identical to the delivered build files, and byte-identical
  after restoring the delivered OUT line (bslib4 has no OUT line; strict identical).
- 8 SVGs: byte-identical to the delivered SVGs (p1 d188d1c7…, p2 c8ce33ac…, p3 de57bfbe…,
  p4 8ce74068…, p5 ebbea645…, p6 56eff22f…, p7 e57f374e…, p8 8fa66246…; full hashes in
  the fix scratch deliverables-snapshot files).
- Run log: ZERO FLOW OVERFLOW; P1-headline ends 1413, P5-feature ends 1268, P7 teaser ends
  2517.46 (< 2540), P8-keys ends 2456 (< 2540); TOTAL 150 — exactly the shipped round-3 values.
- Re-run on a delivered-build copy: 276 skip (258 already-applied + 18 superseded-by-fix),
  0 ok, files byte-unchanged — transform.py is now idempotent on the shipped tree.
- transform.py sha256 before this sync: 2895b6616ed4691864d06041edd9d185dd05767d030b6d519d7ef8aaf75475cd;
  after: cc72648708f7192a0aab53dc1a013e3f8afcaff5dcc003c060575e8e033b84b8 (final, with the
  chained-final-form skip logic; the intermediate sync hash was
  973d62f7268a7e1b890d48f39220d28ee716c67157667f14d3643f584cdaef76, superseded in the same
  session by the idempotency hardening — fresh repro was re-run against the final hash).
- Deliverable hash proof: svg×8 + cards×8 + both PDFs re-hashed after this KIT edit and found
  identical to the pre-fix snapshot (print PDF 30,916,571 B, sha256
  b4756358b2b821495d18ec66b6db56c3cedba7c964957df252941a52a5907070; web PDF 3,622,912 B,
  sha256 76e8b5032d0378b53f228e4d6a69d81f48d63987b63ab004bf9282dad81ffb01). KIT/ABSTRACT are
  not render inputs, so a KIT-only edit cannot change the PDFs; the re-hash confirms it.
- This sync does NOT finalize the edition: independent re-verification (repro re-check) and
  coordinator sign-off are still required before any listing.
