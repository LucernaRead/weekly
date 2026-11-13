# DELTA-LOG — 2026-W47 nl-it (Italian readers), core fix3+fix4+fix5 sync

Date: 2026-11-11. Agent: delta rebuild (nl-it). Scope: sync core-nl fix
rounds 3–5 (D6–D11) into `2026-w47-nl-it`. No commit, no push.
Work dir: `hidden_files/w47/scratch-delta-nl-it/` (exclusive, new).
Canonical dir: `production/2026-w47/2026-w47-nl-it/`.
Staging (pre-delta对照, untouched): `production/2026-w47/fanout-nl/2026-w47-nl-it/`
(build 5, re-fanout).

## 0. Source-material gap (recorded, worked around)

The task named three pilot references that do NOT exist in this clone:

- `hidden_files/w47/briefs/brief-coordinator.md` — no `briefs/` dir at all.
- `hidden_files/w47/scratch-delta-nl-de/`, `-nl-es/`, `-nl-fr/` and their
  `DELTA-LOG.md` — none exist (a repo-wide `find` for `*DELTA*` /
  `*delta*` returns nothing; the nl-de/nl-es/nl-fr scratch dirs are gone,
  presumably cleaned after their inserts).
- `hidden_files/w47/scratch-fanout-nl/export_fanout.py` (the fan-out
  text.md exporter) — also gone; likewise the core fix-round scratch dirs
  (`scratch-fix-nl4/`, `scratch-fix-nl5b/`, `scratch-proof-core-nl2/`).

What WAS available and used as the operation template instead:

- `production/2026-w47/core-nl/FIX-LOG.md` — full fix3 (D6/D7) + fix4
  (D8/D9/D10) + fix5 (D11) records: mechanisms, width-scan method, gates.
- The finished nl-de canonical dir `production/2026-w47/2026-w47-nl-de/`
  vs its staging: a complete `diff -rq` + per-file `diff` gave the exact
  delta shape (bslib4 `w` hunk, `w=` call sites, `capcn_w`/`dt_zh_w`,
  D11 `62 → 89`, D9 key line), and its KIT `## Delta` section gave the
  doc template (its referenced scratch dir is gone too, but the KIT
  section survived in the canonical dir).
- The task text itself (staging SHAs, D9 two-piece, acceptance list).

Consequence for text.md: with no exporter in the clone, the D9 text.md
change was made as a direct single-line edit of line 415 (see §4). It is
fully determined by `content8.py:75`'s `f.ex` arguments, and the diff vs
staging is exactly that one line; the three-way gate (§6) confirms
registry = text.md:415 = P8 node. A re-export would produce the same line.

## 1. Probes (before any edit)

- `echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4` OK.
- Scratch write probe `hidden_files/w47/scratch-delta-nl-it/probe.txt` OK.
- Staging SHAs verified against the task (coordinator 18:05 UTC disk check):
  print `2520e5ad82096ef3c860e46b15934849faf2962ed8d61f885dc17151d2089826` /
  12,667,197 B; web `609dc9a534f109e61d86a4a58d42b9dd4a2ef1673b2a78fb7abb5b668cf97f0c` /
  1,610,232 B; text.md `62142f938c6a814297b5b4602a5a95ea0d7df38b1c4f86df5402a9a8dad629e8` /
  47,049 B — all three matched disk exactly.

## 2. Canonical dir creation

`cp -a production/2026-w47/fanout-nl/2026-w47-nl-it production/2026-w47/2026-w47-nl-it`
(`cp` reported `failed to preserve ownership` for two dirs — ownership
preservation is not permitted in this VM; content is unaffected), then
`diff -r` staging vs canonical: rc 0, byte-identical; the three SHAs
re-checked identical. Staging copy retained untouched as the pre-delta
对照. Pre-delta SVG baseline recorded in `svg-hashes-before.txt`.

## 3. Pre-delta findings (build-5 SVGs, before any edit)

- D6 P3 bridge: 2 lines, ends `agli ausiliari hebben/zijn.` — clean.
- D7 P7 gloss bridge: 3 lines, ends `scoren segnare.` — clean.
- D8 P6 caption: 4 lines, ends `(100 giovani)` — clean.
- D10 P7 letters: 2 lines, ends `esempio; promessa passata a VOL.5.` — clean.
- D11 P4 HET PROGRAMMA box: bottom 1202.6, last baseline `18:45 uur.`
  1209.49 → **−6.89px, real defect**, same as core (facts 3/3/3/2/3 = 14).
- D9 text.md:415: old key `Ik maak een surprise met een gedicht.` + stem
  `Faccio una surprise con una poesia.` — **real defect, two-piece**.

So D6/D7/D8/D10 are structural syncs (mechanism + locally scanned widths
reproducing the current clean wraps exactly); D9 and D11 are real fixes.

## 4. Width rescans (this edition's own text, own wrap(), 0.1px steps)

Script: `width-scan.py` (0.1px scan, 200–430px) + `width-scan-analytic.py`.
The 200–430 scan truncated three bands at its 430 ceiling, so the true
upper edges were derived analytically: for greedy `wrap()`, the current
split holds iff for every line i, `w ≥ width(line_i)` and
`w < width(line_i + " " + first-word-of-line_{i+1})`; upper grid edge =
that minimum − 0.1px. Lower edges from the scan matched the analytic
`max(line widths)` to 0.06px. Each midpoint was verified with a direct
`wrap()` call to reproduce the current lines exactly.

| site | text (kind/size) | band (px) | mid | result |
|---|---|---|---|---|
| D6 P3 bridge (sans 20.5) | `Completa al passato prossimo. … hebben/zijn.` | 399.9–438.9 | **419.4** | 2 lines, unchanged |
| D7 P7 gloss bridge (sans 20.5) | `de wedstrijd partita; … scoren segnare.` | 415.5–449.9 | **432.7** | 3 lines, unchanged |
| D8 P6 capcn (sans 18.5) | `Dati per l'esercizio: … (100 giovani)` | 367.4–388.0 | **377.7** | 4 lines, unchanged |
| D10 P7 dt_zh (sans 20) | `Nessuna vera lettera … VOL.5.` | 343.7–433.7 | **388.7** | 2 lines, unchanged |

Method notes:

- The D7 band sits above the column width (422.5px); the widest rendered
  line is 415.5px, so `w=432.7` (a wrap width only) causes no overflow.
- No core numbers were copied: core D6 was `CW−40` (382.5), D7 `CW−35`
  (387.5), D8 `CW−25` (397.5), D10 `CW−32` (390.5) — all different from
  the values above, as expected for different reader text.
- Two `python - <<EOF` heredoc attempts blocked forever on stdin (the
  heredoc binds to `tee`, not to `python -` when piped) — killed, redone
  as script files. `width-scan2.log` / `width-scan3.log` are the stale
  artifacts of those two attempts; the authoritative logs are
  `width-scan.log` and `width-scan-analytic.log`.

## 5. Edits (canonical dir only; full diff in §9)

- `bslib4.py`: `Flow.para` / `Flow.bridge` gain optional `w` (mechanism
  copied from core fix3 / nl-de canonical hunk, verbatim).
- `content34.py:78`: D6 bridge `w=419.4`. `content34.py:130`: D11
  `sh = 89 + …` (was 62; comment records 89 = 16+52+21).
- `content7.py:19`: D7 bridge `w=432.7`. `content7.py:92,100`: D10
  `dt_zh_w = 388.7`, used in `lh` and the `p.para` call.
- `content56.py:144,156`: D8 `capcn_w = 377.7`, used in `ch` and the
  `p.para` call.
- `content8.py:75–76`: D9 key → `Ik maak een surprise met een kort gedicht.`,
  stem → `Faccio una surprise con una breve poesia. → ___`.
- `2026-w47-nl-it.text.md:415`: same two substitutions, the only changed
  line (diff vs staging is exactly line 415, +11 bytes, 47,049 → 47,060).
  The build-4 KIT note («it Q140 has no defect») is superseded by the
  coordinator's 2026-11-11 two-piece instruction — recorded in the KIT
  Delta section.

## 6. Rebuild (scratch OUT)

Rebuild copy: `scratch-delta-nl-it/rebuild/2026-w47-nl-it/` (full `cp -a`
of the edited canonical dir; `diff -r` clean; OUT path verified inside
scratch with `readlink -f` before running). The staging web PDF was never
overwritten — only its text layer was compared.

- `run.py` rc=0, TOTAL 150, by page 10/18/18/18/18/18/12/38,
  A2 46 / B1 73 / B2 31; zero FLOW OVERFLOW / HEAD TOO WIDE.
- `render.py` rc=0 (cards + print PDF 12,667,201 B).
- `webpdf.py` rc=0 (1,610,237 B < 7 MB, 46,510 text bytes).
- SVG hashes vs build 5: **only `p4-sport.svg` (D11) and `p8-toets.svg`
  (D9) changed**; the other 6 byte-identical.
- D11 re-measurement on rebuilt SVG: box bottom 1229.6, last baseline
  1209.49, margin **+20.11px**.

## 7. Promotion

After all gates passed: `svg/*.svg`, `cards/*.png`, print PDF, web PDF
copied from the scratch rebuild into the canonical dir. Verified:
canonical SHAs equal rebuild SHAs; `diff -r` svg/ and cards/ identical;
staging three SHAs re-verified unchanged (print `2520e5ad…`, web
`609dc9a5…`, text.md `62142f93…`).

## 8. New SHAs (build 6, lowercase)

- Print PDF `De-Lucerna-VOL4-nl-it.pdf`:
  `4d297162d9e9f2ac99896ab2cf41865af0588d0d060ad76b89b3a7dabe44da15`
  (12,667,201 B; was `2520e5ad82096ef3c860e46b15934849faf2962ed8d61f885dc17151d2089826`, 12,667,197 B)
- Web PDF `De-Lucerna-VOL4-nl-it-web.pdf`:
  `15d1b6480e5d3456b527f8f5f2e70b0afd6fa7d90e0b17e9e5ea145ddfe410f6`
  (1,610,237 B; was `609dc9a534f109e61d86a4a58d42b9dd4a2ef1673b2a78fb7abb5b668cf97f0c`, 1,610,232 B)
- text.md `2026-w47-nl-it.text.md`:
  `f1d9e3f58b82e1bc0f9f51c52a1c7e14ac8bb69c87dd60a3d54df44bb44b781b`
  (47,060 B; was `62142f938c6a814297b5b4602a5a95ea0d7df38b1c4f86df5402a9a8dad629e8`, 47,049 B)
- Web PDF SHA/size are not reproducible run to run (fontTools subset
  nondeterminism) — only its text layer is compared (identical, §6 GATE-LOG).

## 9. Source diff (canonical vs staging, complete)

```
bslib4.py:   Flow.para/Flow.bridge + w=None mechanism (core fix3)
content34.py:78  bridge(..., w=419.4)            # D6
content34.py:130 sh = 89 + ...                   # D11 (was 62)
content56.py:144 capcn_w = 377.7; ch uses capcn_w   # D8
content56.py:156 p.para(..., capcn_w, ...)       # D8
content7.py:19   bridge(..., w=432.7)            # D7
content7.py:92   dt_zh_w = 388.7; lh uses dt_zh_w    # D10
content7.py:100  p.para(..., dt_zh_w, ...)       # D10
content8.py:75-76 key +kort, stem +breve         # D9
2026-w47-nl-it.text.md:415  same two substitutions  # D9
WEEKLY-KIT.md: Files delivered (new SHAs) + ## Delta section
```

No other file changed in the canonical dir. No commit, no push.
Gate evidence: `GATE-LOG.md` + `gates/` in this scratch dir.
