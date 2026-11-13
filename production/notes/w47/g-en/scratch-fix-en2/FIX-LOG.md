# FIX-LOG — W47 core-en fix 2: Q73 answer key (2026-11-11)

Fixer: core-en subagent (fix2). Scope: `production/2026-w47/core-en/` ONLY.
One source line changed; no fan-out edits, no `tools/` edits, no commit, no push.
Work log + scripts: `hidden_files/w47/scratch-fix-en2/`
(`sweep_ink.py`, `sweep_sayit.py`, `dump_reg_fix2.py`, `make_textmd_fix2.py`,
`keycheck_fix2.py`, `dump_keyverify_fix2.py`, `audit_110_fix2.py`, `tmp/`).
Scripts are the fix1 scripts re-derived with paths repointed to this scratch dir.

## 0. Probes (before any work)

- `ls /dev/null` present (char device, no `touch` needed).
- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4` ✓
- Real write in goals hidden_files: `hidden_files/w47/probe-fix-en2.txt` ✓

## 1. Baselines (pre-fix, disk-measured — all three matched the task's SHAs)

| artifact | sha256 | bytes |
|---|---|---|
| print PDF `The-Lucerna-VOL4-en-zh-cn.pdf` | `b484e007e6e0e29a78ea3f81c412e9c27c45a7c2b317a9a6081a2f63eb416566` | 41,407,278 |
| web PDF `The-Lucerna-VOL4-en-zh-cn.web.pdf` | `7277e32a96f26974efd68d5e27978e0f1570dd15222f29a060ecdf7dbd89d3f8` | 2,804,271 |
| `2026-w47-en-zh-cn.text.md` | `e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b` | 51,405 |

## 2. The defect (verified in all three sources before touching anything)

- `content56.py:49–50`: `f.ex("A2", "完成句子", "speak", "speak up = 大声说出来", "Speak ___: tell a teacher.", instr="填空")`.
  Stem `Speak ___: tell a teacher.` + key `speak` reads "Speak speak: tell a teacher." — ungrammatical.
  The taught phrasal verb is **speak up** (same-page C-group 75. `to speak up`,
  match-set 4 Q75 `to speak up → a`, D-group Q79 "Children are speaking up this week.",
  note "speak up = 大声说出来"). The only key that fits the blank is **`up`**.
  Same-group control: Q70 "Break the ___" → silence, Q71 "wear odd ___" → socks,
  Q72 "Every child has ___" → rights — every key is the word that fills the blank.
- Three sources agreed on the error: registry n=73 key `'speak'`,
  text.md:1151 `73. [A2] 完成句子 — speak (speak up = 大声说出来)`, P8 key `73. speak`.
- All 10 en-* reader editions carry the same wrong key (their own registries;
  core fix does NOT propagate — each en-* fix must sync Q73 in its own files,
  same hand-maintained-registry conclusion as fix1 §2 item 1).

## 3. The fix (exactly one line)

`content56.py:49` — key `"speak"` → `"up"`; note `speak up = 大声说出来` unchanged; stem unchanged.

```diff
-f.ex("A2", "完成句子", "speak", "speak up = 大声说出来",
+f.ex("A2", "完成句子", "up", "speak up = 大声说出来",
      "Speak ___: tell a teacher.", instr="填空")
```

Registry diff pre → post: **exactly 1 entry changed** (n=73 `speak` → `up`,
note unchanged). Q70–Q72 (`silence`/`socks`/`rights`) and Q79
("Children are speaking up this week.") re-verified unchanged.
text.md diff pre → post: **exactly 1 line** (`:1151`, Q73 answer `speak` → `up`).

## 4. Rebuild

- `run.py`: rc=0, **TOTAL exercises: 150**, 0 × FLOW OVERFLOW / HEAD TOO WIDE.
  MODEL words: 82. P8 keys flow ends y=2548 (bottom 2560), P8 battery y=1418.
- `render.py`: rc=0, print PDF regenerated.
- `dump_reg_fix2.py`: registry 150; by page P1 10 / P2 17 / P3 18 / P4 18 / P5 18 /
  P6 18 / P7 12 / P8 39; A2 62 / B1 66 / B2 22 (identical distribution to baseline).
- `make_textmd_fix2.py`: re-exported text.md, 51,402 B (see §3 for the 1-line diff).
- SVG identity vs fix1 KIT §9 hashes: **p1–p4, p6, p7 byte-identical**;
  only p5 (`a6a515cd5f734d0d…`, Q73 stem page) and p8 (`1066c475da8afe7e…`,
  answer-key page) changed — exactly the two pages the fix touches.
- Note: the on-disk `build-en.log` in core-en was NOT refreshed by this build
  (it still shows fix1-era flow numbers, e.g. P4-main y=1675 vs this run's 2045);
  the SVG hashes above are authoritative — P4 SVG is byte-identical to fix1,
  so the stale log's numbers predate fix1's final rebuild. Live build logs are
  in `tmp/build-run-fix2.log` / `tmp/build-render-fix2.log`.
- Note: `cards/*.png` byte sizes shifted on re-render on pages whose SVGs are
  identical (p1 +3,134 B, p4 +88,920 B) — render-time PNG variance in the
  preview cards only; the print PDF grew by just 9 B and freeze is 8/8, so no
  content change. Not investigated further.

## 5. Gates (all re-run after the rebuild)

| gate | result |
|---|---|
| `run.py` rc / TOTAL | rc=0 / 150 |
| `freeze.py baseline` | **8/8 SVGs byte-identical** (see §4; `tmp/freeze-fix2.log`) |
| `occlusion_audit.py` | **0 flags**, selftest OK (all 6 planted classes fired) |
| `p8.py extract --total 150` | **150/150**, noted set 60/150 (same set as fix1 baseline) |
| `p8.py compare` (independent re-run, `tmp/p8-compare-fix2.json`) | **CLEAN** — missing=[] extra_count=0 uncertain=[] keydiff=[] |
| `keycheck` registry-vs-P8 | **149/150 exact**, #150 the known full-text writing exception, 0 mismatches — PASS |
| print/web text layer (`pdftotext` per page) | **byte-identical on all 8 pages** (P1 12,475 B; P2 13,046 B; P3 11,043 B; P4 12,060 B; P5 10,585 B; P6 10,960 B; P7 13,476 B; P8 19,642 B) |
| P8 min font size (svg `font-size` attrs) | **15.5 pt** (255 spans, none < 9.75 pt) — floor 9.75 pt, no concession |
| creambox ink sweep (`sweep_ink.py`, 1950 px PNGs) | **0 OVERFLOW** on all 8 pages; tightest box-bottom clearance +2.9 px (pre-existing P2 AND YOU?, passing), next +11.0 px (P1 SEARCHES) |
| boxtitle ink sweep (same run) | **0 OVERFLOW**; tightest title edge clearance +5.5 px |
| SAY IT sweep (`sweep_sayit.py`, P2 PNG) | all panels inside (middle label ink −11.0 px/side); vocab list ≤ −25.0 px; note para line 3 ink ends 1861 vs RIGHT 1862 (−1.0 px, same as baseline) |
| web PDF | 2,804,281 B (< 7 MB), text layer 48,135 B (−3 B vs baseline: `speak`→`up`) |
| 150 keys, three-source hand check (`tmp/key-verify-fix2.txt`, 165 lines) | **150/150 PASS** — every stem/key/note read; match sets 1–5 (n=24–27, 38–41, 56–59, 74–77, 141–144) all correct, incl. fix1's Q39 mentor→a / Q40 arena→d intact; cloze 112–119 unique-key re-verified (Tuesday/call/continues/will meet/writes/will certify/wears/will watch) |
| D5 fonts | record only, not fixed: Newsreader / Noto Sans CJK SC / Noto Serif CJK SC / UnifrakturMaguntia on all pages; DejaVu Sans only on P6 (the four ☐ ballot checkboxes) — unchanged from fix1 (`tmp/fonts-d5-fix2.txt`) |

## 6. Q73 four-source consistency (post-fix)

- registry n=73: `{key: 'up', note: 'speak up = 大声说出来'}` ✓
- text.md:1151: `73. [A2] 完成句子 — up (speak up = 大声说出来)` ✓
- P8 print text layer: `73. up` ✓ (p8 extract key `73: up`)
- P5 print text layer: stem `Speak ___: tell a teacher.` unchanged; P5 gloss
  `to speak up` present ✓ — "Speak up: tell a teacher." now reads correctly.

## 7. New SHAs (post-fix, disk-measured)

| artifact | sha256 | bytes |
|---|---|---|
| print PDF `The-Lucerna-VOL4-en-zh-cn.pdf` | `08cbc1e53f2d02d6c64266d1f64ac2422eaa2f8f71e1829f877e94a5627b3213` | 41,407,287 |
| web PDF `The-Lucerna-VOL4-en-zh-cn.web.pdf` | `d7927eaad14531a9aee71331d4e27abbf951a296f6b6ee5fb1c770f8c7f7e444` | 2,804,281 |
| `2026-w47-en-zh-cn.text.md` | `23855d4bd60abe4a7fb4db42050cb9343202e85789ffd434634808d299215c69` | 51,402 |

## 8. Scope hygiene

- Only `production/2026-w47/core-en/` touched (1 source line + regenerated
  artifacts: `registry.json`, `svg/p5-youth.svg`, `svg/p8-test.svg`,
  `2026-w47-en-zh-cn.text.md`, both PDFs, `cards/*.png`).
- No en-* edition dir touched by this agent. (`core-nl/` files show fresh
  mtimes from a concurrent parallel agent's own fix — not this work.)
- No commit, no push. `git status` unchanged in kind: core-en still untracked
  (`?? production/2026-w47/core-en/`); the `M issues/2026-w43/...` entries are
  pre-existing work by other agents, untouched here.
- Handoff for the coordinator: the same Q73 key error (`'speak'`) sits in all
  10 en-* registries and must be synced per edition (key → `up`, note/stem
  unchanged) in each en-* fix pass, with that edition's own rebuild + gates.
