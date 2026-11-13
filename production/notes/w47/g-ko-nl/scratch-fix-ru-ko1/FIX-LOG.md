# FIX-LOG — 2026-W47 ru-ko fix1 (proof1 D-1, exporter bug)

 fixer: subagent ru-ko fix1 · 2026-11-11 ~18:27–18:55 UTC
 scope: `production/2026-w47/2026-w47-ru-ko/` + its `ru_textmd.py` only.
   No commit, no push. run.py / render.py / webpdf.py NOT run (PDFs untouched).
   Core-ru and the other 9 ru fan-outs NOT touched.
 work dir (all scripts/logs/outputs): `hidden_files/w47/scratch-fix-ru-ko1/`

## 0. Pre-flight

- Probe (required): `echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`, rc 0.
  Scratch write probe (`hidden_files/w47/scratch-fix-ru-ko1/.probe`) OK.
- NOTE — brief file missing: the task cites
  `hidden_files/w47/briefs/brief-coordinator.md`, but there is no `briefs/`
  directory under `hidden_files/w47/` (verified `ls` + `find`). Work proceeded
  from the task text itself + repo-root `SOP.md` (§1.1, §8.4) + repo `AGENTS.md`,
  both read before touching anything.
- SOP/AGENTS rules honoured: production via shared tools only (tools/p8.py,
  tools/freeze.py, tools/venv python); text.md exported from source, never
  from PDF; no hand-edit of generated artefacts.

## 1. Opening SHA verification (all three match the brief — proceed)

| artefact | SHA-256 (opening) | bytes |
|---|---|---|
| `Lucerna-VOL4-ru-ko.pdf` (print) | `78e4442af8af9ec286c407ff66e08bac2029dd79d3ded43d1bfde3d555a6a400` | 22,007,810 |
| `Lucerna-VOL4-ru-ko-web.pdf` (web) | `3bf39ecf4fa4563458c68319ca42171642f9ad0be24650064faa9b7d9bd03195` | 3,513,230 |
| `2026-w47-ru-ko.text.md` | `d1feb40e417ba058d773a58ada62ad7fd7805b6a943599d8d017510b402d5a3d` | 65,069 |

- Pre-fix snapshot: `snapshot-prefixed-sha256.txt` (42 files, `__pycache__` excluded).
- Backup of pre-fix text.md: `2026-w47-ru-ko.text.md.bak-prefixed`
  (SHA `d1feb40e…`, verified equal to opening value).
- Backup of pre-fix exporter: `ru_textmd.py.bak-prefixed`
  (SHA-256 of file `28a51c7e…` per snapshot; md5 `0d42818e5fcdb88764411f9ae5f70942`).

## 2. Defect confirmation (D-1, text.md only)

- New text.md (pre-fix) L836:
  `150. (열린 문제 — 모범 답안은 아래에 있어요) — 모범 답안은 이 면의 H란(97 단어)`
- Core `2026-w47-ru-core.text.md` L836:
  `150. ✓ 范文见本版 H 区（97词）`
- Print P8 (pdftotext, print PDF p.8, verified §6) already prints the ✓ form:
  `150. ✓ 모범 답안은 이 면의 H란(97 단어)` — so only text.md was wrong.
- Root cause confirmed in source:
  - `ru_textmd.py:616` (pre-fix): `if e["type"] == "写作":`
  - `content8.py:110` (ru-ko): `f.ex("B1", "쓰기", "(열린 문제 — 모범 답안은 아래에 있어요)", …)`
  - `content8.py:110` (core): `f.ex("B1", "写作", "（开放题，范文如下）", …)`
  - `content8.py:126-127` (ru-ko P8 render): `if e_["type"] == "쓰기": txt = f"{e_['n']}. ✓ {e_['note']}"`
    → P8 render checks the translated label (correct per edition);
    the exporter hardcoded the Chinese label only.
  - `bslib4.py:23-25` (`reg_ex`): REG entries carry only
    `{n, page, level, type, key, note}` — `instr` is NOT stored, so the
    `instr="쓰기"` argument (content8.py:111) cannot be used as the signal.

## 3. Exporter: which copy is the "shared" one?

- `md5sum` of `ru_textmd.py` in core-ru + all 10 ru fan-outs: ALL identical,
  `0d42818e5fcdb88764411f9ae5f70942`. There is NO separate shared source file;
  each edition dir carries its own copy, and the build invokes the copy in
  its own dir (KIT §5: `ru_textmd.py . 2026-w47-ru-ko.text.md "VOL.4 · …"`,
  run with cwd = the edition dir — `sys.path[0]` is the script dir, which is
  how `import bslib4` resolves in `get_reg()`; confirmed: running the
  exporter from scratch fails with `ModuleNotFoundError: No module named
  'bslib4'` unless `PYTHONPATH=<build-dir>`).
- Decision (scope-preserving): fix ONLY the ru-ko copy — the copy this
  edition's build actually calls. Editing the other 10 copies would violate
  "绝不碰其他版". The fix is written type-agnostic, so the coordinator's
  batch item can apply the identical patch to the other 9 fan-out copies.
- Systemic evidence gathered for that batch item (live-registry replay,
  `dump_reg.py`, save() patched to no-op, one subprocess per edition):
  in EVERY one of the 11 editions (core + 10 fan-outs) there is exactly ONE
  REG entry whose key starts with `(` or `（`, always n=150, page 8, B1,
  the writing exercise:

| edition | n=150 type | n=150 key (first chars) |
|---|---|---|
| core-ru | `写作` | `（开放题，范文如下）` |
| ru-de | `Schreiben` | `(Offene Aufgabe, …` |
| ru-en | `writing` | `(Open task; …` |
| ru-es | `Redacción` | `(Pregunta abierta, …` |
| ru-fr | `Rédaction` | `(Question ouverte, …` |
| ru-it | `Composizione` | `(Domanda aperta, …` |
| ru-ja | `作文` | `（自由記述、模範文は下）` |
| ru-ko | `쓰기` | `(열린 문제 — 모범 답안은 아래에 있어요)` |
| ru-nl | `Schrijven` | `(Open opdracht, …` |
| ru-pt | `Escrita` | `(Pergunta aberta, …` |
| ru-zh-tw | `寫作` | `（開放題，範文如下）` |

  Each replay: TOTAL 150, PAREN_KEYS 1. No other exercise in any edition
  has a parenthesised key (match_set keys are letters; all other f.ex keys
  are answers).

## 4. The fix (only change to shared logic)

 File: `production/2026-w47/2026-w47-ru-ko/ru_textmd.py`
 Location: `Exporter.do_appendix()`, old line 616.

 BEFORE (lines 615-619):
 ```python
             for e in by_page[pg]:
                 if e["type"] == "写作":
                     lines.append("%d. ✓ %s" % (e["n"], e["note"]))
                 else:
                     lines.append("%d. %s — %s" % (e["n"], e["key"], e["note"]))
 ```

 AFTER (lines 615-628):
 ```python
             for e in by_page[pg]:
                 # Writing exercise: its "key" is not an answer but the
                 # parenthesised open-task note, e.g. core "(开放题…)" /
                 # ko "(열린 문제 …)". The type label is translated per
                 # reader language (写作/쓰기/writing/…) so it cannot be
                 # matched here — this exporter is shared by all of them.
                 # The parenthesised key is unique in the registry
                 # (verified: exactly 1 of 150 in core + all 10 fan-outs,
                 # always the writing exercise, n=150, page 8).
                 if e["key"].startswith(("(", "（")):
                     lines.append("%d. ✓ %s" % (e["n"], e["note"]))
                 else:
                     lines.append("%d. %s — %s" % (e["n"], e["key"], e["note"]))
 ```

 Docstring updated (lines ~74-78): the appendix rule now reads
 "(writing exercise: "{n}. ✓ {note}"; detected by its parenthesised key,
 not by the translated type label — see do_appendix)."
 No other line of the exporter changed. The body emitter (`ex_line`,
 line 238) was already type-agnostic and needed no change.
 Why the key rule, not a label list: it is language-independent, needs no
 per-language maintenance, and matches the P8 renderer's semantics
 (the writing exercise has no answer key — its "key" is the open-task note).
 The hardcoded `写作` check was removed entirely, not kept as an OR.

## 5. Regeneration (scratch first, then write-back)

 Command (KIT §5 form, run from the repo root; build dir = edition dir):
 `tools/venv/bin/python production/2026-w47/2026-w47-ru-ko/ru_textmd.py
  production/2026-w47/2026-w47-ru-ko <out> "VOL.4 · Russian text · Korean explanations"`
 - Scratch output `2026-w47-ru-ko.text.md.NEW`:
   `wrote … (65012 bytes, 150 exercises, 277 blocks)` — same 150/277 as before.
 - `diff` scratch-NEW vs pre-fix backup: EXACTLY ONE line:
   ```
   836c836
   < 150. (열린 문제 — 모범 답안은 아래에 있어요) — 모범 답안은 이 면의 H란(97 단어)
   ---
   > 150. ✓ 모범 답안은 이 면의 H란(97 단어)
   ```
 - Write-back: copied scratch-NEW over
   `production/2026-w47/2026-w47-ru-ko/2026-w47-ru-ko.text.md` (pre-fix
   backup already in scratch).

## 6. Post-fix three SHAs

| artefact | SHA-256 (post-fix) | bytes | vs opening |
|---|---|---|---|
| `Lucerna-VOL4-ru-ko.pdf` (print) | `78e4442af8af9ec286c407ff66e08bac2029dd79d3ded43d1bfde3d555a6a400` | 22,007,810 | UNCHANGED ✓ |
| `Lucerna-VOL4-ru-ko-web.pdf` (web) | `3bf39ecf4fa4563458c68319ca42171642f9ad0be24650064faa9b7d9bd03195` | 3,513,230 | UNCHANGED ✓ |
| `2026-w47-ru-ko.text.md` | `5e9bd67201fd232aff598e0bbb487ba45821878e533392bc6e749444b090bffe` | 65,012 | CHANGED (−57 B, L836 only) ✓ |

 New text.md L836 (production file, verified after write-back):
 `150. ✓ 모범 답안은 이 면의 H란(97 단어)`

## 7. Guard: core regeneration byte-identical (core NOT touched)

 Fixed exporter (scratch copy `ru_textmd.py.FIXED`, run with
 `PYTHONPATH=production/2026-w47/core-ru` — needed only because the script
 was invoked from scratch, not from the build dir) on the core build dir:
 `wrote … (60953 bytes, 150 exercises, 277 blocks)`
 `cmp` vs shipped `production/2026-w47/core-ru/2026-w47-ru-core.text.md`:
 BYTE-IDENTICAL. SHA both
 `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc`.
 Core L836 from the guard output: `150. ✓ 范文见本版 H 区（97词）` (unchanged).
 Core files: zero writes (core text.md SHA re-verified after all work, §8).

## 8. KIT §5 update

 `WEEKLY-KIT.md` §5, line 57:
 - BEFORE: `.text.md` exported from the source manuscript (65,069 bytes, 150 exercises, 277 blocks).
 - AFTER: `.text.md` exported from the source manuscript (65,012 bytes, SHA-256 `5e9bd67201fd232aff598e0bbb487ba45821878e533392bc6e749444b090bffe`, 150 exercises, 277 blocks; fix1 2026-11-11: was 65,069 bytes, see §7).
 §7: new "Fix 1 (2026-11-11, proof1 D-1, exporter bug …)" bullet appended
 after the re-fanout bullet, summarising root cause, patch, SHAs and gates.
 Print/web PDF lines in §5 (SHAs/sizes) needed NO change — values identical.

## 9. Production zero-write verification

 Post-fix snapshot `snapshot-postfix-sha256.txt` vs pre-fix snapshot:
 diff shows EXACTLY 3 files changed, nothing else:
 - `2026-w47-ru-ko.text.md`: `d1feb40e…` → `5e9bd672…`
 - `WEEKLY-KIT.md`: `622f2c8f…` → `a84402fb…`
 - `ru_textmd.py`: `28a51c7e…` → `1b88b7f5…`
 File list identical (42 files, no adds/deletes).
 `__pycache__/*.pyc` in the edition dir pre-date this session
 (2026-11-11 15:28 UTC; session started 18:27 UTC) — not written by this fix.
 No other edition, core, tools/, or repo file touched. No commit, no push.

## 10. Handover / open items (for the coordinator)

- This fix is DONE and self-verified; it still needs the independent
  re-proof that the task requires (not done by this fixer).
- Batch item for the coordinator (NOT done here, out of scope): the same
  one-line patch applies to the other 9 ru fan-out copies of `ru_textmd.py`
  (ru-en/ru-de/ru-ja + the rest, whose L836 are the same long form per the
  brief). Evidence in §3 above proves the patch is correct for all of them;
  each must still be regenerated + guard-checked individually after patching.
- Nothing else in ru-ko changed; the edition is otherwise exactly as the
  re-fanout left it (all prior gates' numbers reproduced, see GATE-LOG.md).
