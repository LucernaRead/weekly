# Micro-fix log — W45 zh-CN × ES (Gate 10 transform-miss cleanup; NOT finalization)

Coordinator decision implemented: clean up the 3 remaining Gate 10 transform
misses so the reproduction chain exits 0. Outcome: **2 of 3 deleted;
1 HELD under the task's STOP rule, so the chain still exits 1.**
This record does NOT declare finalization — a full independent reproof
follows per SOP §8.4.

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER)

- (a) No live worker writing to the ES delivery/build dirs: `ps` at
  snapshot time showed one worker, on zh-cn-NL only; at snapshot-2 time
  no Python workers at all. No process touched the ES dirs.
- (b) Two mtime snapshots of both dirs ~3 minutes apart: `diff` =
  ZERO changes.
- (c) Fix session completed: `FIX-LOG-GATE10.md` filed, status
  "FIX DONE, NOT finalized". Proceeded.

## Pre-cleanup baselines (recorded BEFORE any edit)

Full SHA-256, identical to the FIX-LOG-GATE10 pre-fix section:

```
71d4b608add7f84e0e92bad531409da28d0cb288fee2a0396f0feb1f60e91b52  svg/p1-touiban.svg
8d78f0bb0fe50aa15041bd9012f65215d6cb40e364d691ae17c69f85c2f30c33  svg/p2-shenghuo.svg
091af691031a38e7610cbb34de8dc2da70dd67910b3aad372802e7117cefb912  svg/p3-wenhua.svg
f316e145cefc692ebd85b23c406a93a58309f9e915318d9f823e94521c44a604  svg/p4-tiyu.svg
203d8eae79a87f32d963fdc17040ee538c27f427161f0a40c2af8c0fb494aeef  svg/p5-qingnian.svg
d26244db12294e27a32454b525f7f7cdbda5d055738dade458055b58a681ed73  svg/p6-shendu.svg
1fd7c59999288c37abd0d70ffea0390142bfc5c2486e1866c352697f6ac41394  svg/p7-ciyu.svg
d6c9bb95b56f21b6786cbe64332e63de0ef617ba6b66033e5a4564ab7d887045  svg/p8-ceyan.svg
44df3074de8fba1f68325ca467a440b2a7ef1da5094f8aaece838c3c1f3b9122  cards/p1-touiban.png
5c4e8b73f90613ce8eaac3b812da0c630bbdb556b83730bd268ecea05ed6bba8  cards/p2-shenghuo.png
494c447158acd036cbe053f139c75af55bb882648d5aa94d41ab7bb3324340d4  cards/p3-wenhua.png
6326f43b5a54e869848410a05cc6cfe6117512148d03d53f1e977afa78c273a0  cards/p4-tiyu.png
094f7ad601fe03b71e0872678391019a0dcd1d4d441ab65b938828b4f76da5b6  cards/p5-qingnian.png
84a5c32bb87dcc8c3c718d51389a0f14fe799bb70c9057b9b36a5203f108061d  cards/p6-shendu.png
ec4d9604b2f1cbfa2290348314242fb50d56b3c014aa6f97d45e2839fd71cb99  cards/p7-ciyu.png
605e5da0001fb34424364b4c0d3a8204ea2ec3e0ceeb24a98ed4d953e6aa1366  cards/p8-ceyan.png
e53d52040d1990edbb3c89aa6a3e0fc29d83c9325de75e3f1f65aed911543c46  Lucerna-VOL2-ES.pdf (50,133,157 B)
0ee7547e5d24a835cb349a4037fa94adf279c3350b73a26dacb414609baa573c  Lucerna-VOL2-ES-web.pdf (3,242,033 B)
e408c4825931773811c674e93e3b0474170f3ddca2c9ebae327afd74ee5c0b47  ABSTRACT.txt
```

transform.py pre-edit SHA-256:
`14d1f6b1360413f9a4da8dbdf4beb800e971df84159862580cab9385734bc90d`
(transform.py post-edit SHA-256:
`35dfbb95b88d11b390af1a9b6dc1185680fb26be06ae0381d8c91924e2e42e14`)

## Verification (grep -F, fresh core = hidden_files/weekly-report-w45-zhcn-build, read-only)

The 3 Gate 10 misses from `hidden_files/w45/zh-cn-es-fix/work/gate10-transform.log`
(FAILED list) are byline-level replacements:

1. content12.py `Lucerna editors · Reading level B1` — **0 hits** in fresh
   core content12.py (core bylines: A2 ×2 only, lines 38 and 169).
   VERIFIED STALE → deleted.
2. content56.py `Lucerna editors · Reading level A2` — **0 hits** in fresh
   core content56.py (core bylines: B1 line 16, B2 line 123).
   VERIFIED STALE → deleted.
3. content34.py `Lucerna editors · Reading level A2→B1` — **1 hit** in fresh
   core content34.py line 16:
   `f.byline("Lucerna editors · Reading level A2→B1")`
   (other core byline: B1 line 121). **FAILS the task's literal test
   (must be 0 hits) → HELD, NOT deleted, per the task STOP rule.**

Why #3 still MISSES in the transform run despite the raw-core hit
(mechanism, verified against the Gate 10 log): the loop's A2 replacement
runs before line ~146 and matches the A2→B1 string as a prefix substring
(Gate 10 log: content34 A2 hit x1 = that prefix), converting line 16 to
exactly line ~146's target string
(`Redacción Lucerna · Nivel de lectura A2→B1`). By the time line ~146
runs, its old English string is already gone → MISS. So #3 is a no-op
*in sequence* but is NOT absent from raw core, and the task's STOP rule
is written on raw-core presence. The coordinator must decide: either
accept the 1 remaining miss, or explicitly authorize the sequence-aware
deletion of line ~146 (provably output-identical, since the A2 loop
replacement already produces its exact target string).

## The edit (transform.py in the edition build dir ONLY)

The two stale instances were loop-generated, not standalone lines, so the
shared loop was split — nothing else changed (diff vs the Gate 10
transform copy, whose SHA matched the pre-edit build file exactly, shows
only this hunk plus its comment):

```python
# BEFORE
for f in ["content12.py", "content34.py", "content56.py"]:
    add(f, "Answers on page 8 · 答案见第 8 版", "Respuestas en la página 8 · 答案见第 8 版")
    add(f, "练习 · Exercises", "练习 · Ejercicios")
    add(f, "Lucerna editors · Reading level A2", "Redacción Lucerna · Nivel de lectura A2")
    add(f, "Lucerna editors · Reading level B1", "Redacción Lucerna · Nivel de lectura B1")

# AFTER (micro-fix)
for f in ["content12.py", "content34.py", "content56.py"]:
    add(f, "Answers on page 8 · 答案见第 8 版", "Respuestas en la página 8 · 答案见第 8 版")
    add(f, "练习 · Exercises", "练习 · Ejercicios")
for f in ["content12.py", "content34.py"]:
    add(f, "Lucerna editors · Reading level A2", "Redacción Lucerna · Nivel de lectura A2")
for f in ["content34.py", "content56.py"]:
    add(f, "Lucerna editors · Reading level B1", "Redacción Lucerna · Nivel de lectura B1")
```

Preserved hitting instances: content12 A2 (x2), content34 A2 (x1),
content34 B1 (x1), content56 B1 (x1), content56 B2 (x1, separate line).
`py_compile` OK. No other file in the build or edition dirs was edited.

## Gate 10 re-run (gate10b: fresh core copy + fixed transform alone, one-process driver)

Scratch: `hidden_files/w45/zh-cn-es-fix/work/microfix/gate10b/`
(OUT repointed to `microfix/gate10b-out` in the scratch copies ONLY;
core and edition build OUT lines verified untouched afterwards).
Interpreter: `tools/venv/bin/python`.

- **Transform: 317/318 replacements, exit 1.** Sole FAILED entry:
  `content34.py Lucerna editors · Reading level A2→B1` (the held item).
  The two deleted misses are gone; all byline hits keep their Gate 10
  counts (content12 A2 x2, content34 A2 x1, content34 B1 x1,
  content56 B1 x1, content56 B2 x1).
- **Driver: exit 0, zero `HEAD TOO WIDE` / `FLOW OVERFLOW` warnings,**
  registry TOTAL 150 (A2 56 / B1 69 / B2 25; pages 10/18/18/18/18/18/12/38;
  types 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1;
  writing model 172 chars; P8 keys end y=2411 — all delivered values).
- **SVG comparison: 8/8 byte-identical to the delivered SVGs**
  (cmp, all 8 pages).
- Transform-output content files: byte-identical to the delivered ES
  build content files except the repointed OUT line (line 6);
  bslib4.py identical — same pattern as the original Gate 10.
- **Exit 0 NOT achieved**: the held content34 A2→B1 miss keeps the
  transform at exit 1. This is reported plainly, not papered over.

## Post-cleanup byte-identity (delivered files vs pre-cleanup baselines)

All 18 delivered files byte-identical (SHA-256 diff, 18/18):
8 SVGs, 8 cards, both PDFs (sizes unchanged: 50,133,157 B /
3,242,033 B). Cards/PDFs were hash-verified, NOT regenerated.
`ABSTRACT.txt` SHA unchanged (`e408c482…`). Paper content, furniture,
and `tools/tables.json` untouched. No weekly-git, insert.py, Discord,
main-chat delivery, cron, or subagent activity.

## Status

MICRO-FIX PARTIAL, NOT finalized. 2 stale replacements deleted with
grep evidence; 1 held under the STOP rule with its mechanism documented.
A full independent reproof follows per SOP §8.4; the coordinator's
decision is still owed on the held content34 A2→B1 replacement.

## Micro-fix round 2 (coordinator-authorized single-line deletion; NOT finalization)

Coordinator decision implemented (overriding round 1's STOP rule for
this ONE line only): delete the content34 A2→B1 replacement, on the
documented evidence that (a) the loop A2 replacement runs first and
consumes the A2→B1 string as a prefix, producing exactly the target
string, (b) the A2→B1 replacement therefore always misses in sequence,
(c) deleting it is provably output-identical. Authorization covered
ONLY that one line — nothing else was deleted or changed.

### Pre-flight (coordinator ruling: NO CONCURRENT WRITER)

- (a) No live worker writing to the ES delivery/build dirs: at
  snapshot-1 time the live Python workers were zh-cn-RU webregen,
  zh-cn-IT render, and zh-cn-JA occlusion audit; at snapshot-2 time
  the live workers were zh-cn-JA repro-build and zh-cn-FR reproof
  baseline only. No process touched the ES dirs (cwd + cmdline
  checked; `ps | grep zh-cn-es` = NONE).
- (b) Two mtime snapshots of both dirs ~3 minutes apart: `diff` =
  ZERO changes.
- (c) Micro-fix round 1 completed: `MICROFIX-LOG.md` filed, status
  "MICRO-FIX PARTIAL". Proceeded.

### Pre-round-2 baselines (recorded BEFORE any edit)

All 18 delivered files matched round 1's post-fix baselines exactly
(SHA-256 diff, 18/18; `ABSTRACT.txt` `e408c482…` also matched).
transform.py pre-edit SHA-256 matched round 1's post-edit SHA-256
(`35dfbb95b88d11b390af1a9b6dc1185680fb26be06ae0381d8c91924e2e42e14`)
— no drift since round 1.
Baseline file: `hidden_files/w45/zh-cn-es-fix/work/microfix/gate10c-pre-baselines.txt`.

### The edit (transform.py in the edition build dir ONLY)

Deleted exactly one line (diff vs the round-1 fixed transform copy
shows only `153d152`, nothing else; `py_compile` OK):

```python
# DELETED (was transform.py line 153)
add("content34.py", "Lucerna editors · Reading level A2→B1", "Redacción Lucerna · Nivel de lectura A2→B1")
```

transform.py post-edit SHA-256:
`b2dda203bfcbee83363079557ee4cff770b3a13b071e97d0ae612ea70892d5d3`
NOTE (left untouched per the one-line-only authorization): the
comment block at transform.py lines 28–32 still says the content34
A2→B1 line is "HELD, not deleted … it stays". That comment is now
stale; correcting it was outside the authorized one-line change and
is flagged to the coordinator/parent line, not silently edited.

### Gate 10 re-run (gate10c: fresh core copy + fixed transform alone, one-process driver)

Scratch: `hidden_files/w45/zh-cn-es-fix/work/microfix/gate10c/`
(OUT repointed to `microfix/gate10c-out` in the scratch copies ONLY;
core and edition build OUT lines verified untouched afterwards).
Interpreter: `tools/venv/bin/python`.

- **Transform: 317/317 replacements, EXIT 0, zero MISS / FAILED.**
  Count note, stated plainly: the task text asked for "318/318",
  but that denominator cannot survive the deletion — round 1 had
  318 entries (317 hits + 1 miss); deleting exactly one entry leaves
  317 entries, all hitting. 317/317 + exit 0 is the correct
  expectation, and it is what was measured (317 `ok` lines).
- **Output-identity proof:** gate10c `content34.py` line 16 reads
  `f.byline("Redacción Lucerna · Nivel de lectura A2→B1")` — the
  loop A2 replacement produced exactly the deleted line's target
  string, as predicted. All byline hits keep their counts
  (content12 A2 x2, content34 A2 x1, content34 B1 x1,
  content56 B1 x1, content56 B2 x1).
- **Driver: exit 0, zero `HEAD TOO WIDE` / `FLOW OVERFLOW` warnings,**
  registry TOTAL 150 (A2 56 / B1 69 / B2 25; pages 10/18/18/18/18/18/12/38;
  types 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1;
  writing model 172 chars; P7 teaser ends 2525.1, P7 col3 ends 1679.1,
  P8 keys end y=2411 — all delivered values).
- **SVG comparison: 8/8 byte-identical to the delivered SVGs**
  (cmp, all 8 pages).

### Post-round-2 byte-identity (delivered files vs pre-round-2 baselines)

All 18 delivered files byte-identical (SHA-256 diff, 18/18 + 
`ABSTRACT.txt` unchanged): 8 SVGs, 8 cards, both PDFs (sizes
unchanged: 50,133,157 B / 3,242,033 B). Cards/PDFs were hash-verified,
NOT regenerated. Paper content, furniture, and `ABSTRACT.txt`
untouched. No weekly-git, insert.py, Discord, main-chat delivery,
cron, subagent, or shared-scratch cleanup activity.

### Status

MICRO-FIX ROUND 2 DONE, NOT finalized. The reproduction chain now
exits 0 (transform 317/317 + driver exit 0 + 8/8 SVGs). A full
independent reproof follows per SOP §8.4; this record does not
declare finalization.
