# WEEKLY-KIT — ES×JA（スペイン語正文 · 日本語解説）W45 VOL.2

- **Pairing:** Spanish target text (frozen W45 core, `files/weekly-report-w45-es-core/`,
  VOL.2, week Mon 2 – Sun 8 Nov 2026) + explanation layer written natively in
  **Japanese**, for Japanese readers. Every explanation was written directly
  from the Spanish text; no intermediary language was used anywhere in the
  production chain, and the banned intermediary term occurs **0 times** in the
  paper, this KIT, and the build code.
- **Status: fix round complete; independent re-proof: PENDING**
  (a separate proofreader must still re-verify the fixed edition per SOP
  §8.4; no final-edition claim is made here). The first independent
  proofread (hidden_files/w45/es-ja-proof/REPORT.md) blocked on 2 items,
  both fixed and recorded in §9.1–§9.2; the independent re-proof
  (hidden_files/w45/es-ja-reproof/REPORT.md) then blocked on 1 further
  item (P7 readers'-letter invitation), fixed in this second fix round
  and recorded in §9.4. No Discord post, no main-chat card/PDF dump,
  no cron was created, and the core build dir, the core edition dir,
  and the W43 edition dir were never written. No subagent was spawned.
- **Build dir:** `hidden_files/weekly-report-w45-es-ja-build/` (copy of the W45
  core build `hidden_files/weekly-report-w45-es-build/`).
- **Transform:** `hidden_files/w45-es-ja-transform.py` — exact-string /
  whole-line replacements only, each asserting its hit count, abort on
  mismatch; longer strings before their substrings; type names before
  instr substrings containing them. No AST byte-offset splicing, no repr
  literals in value maps. All content modules render in the single-process
  driver `run.py` (shared exercise registry); no content module was ever
  imported inside the core build dir.
- **Deliverables (this dir):** `svg/` ×8, `cards/` ×8 (1950×2700 PNG),
  `La-Lucerna-VOL2-JA.pdf` (print, 8 pp., 21,775,658 B,
  sha256 `7ebbf37e2514197c71c3cdb612875a1e219e1eeacb97880beac4f62c0abd680b`),
  `La-Lucerna-VOL2-JA-web.pdf` (web, 8 pp., 3,639,992 B < 10 MB,
  sha256 `56ed27fd1b6ff17b6f9d4741ef9652756f25f6daa83170406c8d5dded64cc35d`),
  `WEEKLY-KIT.md`, `ABSTRACT.txt` (Japanese, one line, no ASCII double quotes).
- **SVG sha256 (full):**
  p1 `098de92d91f15c2e…` · p2 `d5bbf5d10f1d4ae7…` · p3 `b8cd0e6a4c83bf20…` ·
  p4 `196e97a39a91453d…` · p5 `1534eea1f9121ac9…` · p6 `481ffa7a0bb32fdf…` ·
  p7 `20f1a1dcdf9acebf…` · p8 `dac6d639a5d6b582…`
  (full hashes recorded in the fix-round build logs
  `hidden_files/w45-es-ja-build4.log` (fix round 1) and
  `hidden_files/w45-es-ja-build5.log` (fix round 2 — this round's
  pre-fix baseline, recorded before any re-render, plus post-fix
  hashes). Fix round 1 changed only p5 (pre-fix p5 `1cd8a67fd126a4f5…`,
  pre-fix PDFs print 21,775,534 B sha256
  `e20412982cd45a173bca3ea5156595c614bff5a564ee6b134a3794e14013a6d8`
  and web 3,638,986 B sha256
  `56984875b7e6a1e8ec2e6091e87fe1a806fb73bc3bb185b58f454f302b9ba3e7`);
  fix round 2 changed only p7 (pre-fix p7 `a09489eaca3c89f7…`,
  pre-fix PDFs print 21,775,534 B sha256
  `ad19ec708b70ab5dbdca73588d495d1e00703ebf7d47e1337a2789c43dcea8a3`
  and web 3,639,060 B sha256
  `5d75623cfb9851b233d7393c426540be7b79da1efb42f7b16ee37090067934a9`) —
  see §9.4 for the round-2 per-page byte-identity table.)

## §1 Baseline proof (freeze)

- Before any edit, `tools/freeze.py baseline` on the W45 core build reproduced
  all 8 shipped core SVGs byte-identically (p1 `a1b3010296ad129e`,
  p2 `10e78c2e6cb29519`, p3 `5986ba9e318c985e`, p4 `1894836e06be824b`,
  p5 `cd15c68b5f8db752`, p6 `fcfccf8267e10cc7`, p7 `b1774024b6a17353`,
  p8 `d1c46fa439ac505d`); the shipped core SVGs re-hashed unchanged afterwards.
- **Frozen-text accounting** (`tools/freeze.py diff`, core vs this edition):
  added CJK total **3,007** characters — the expected figure for a Japanese-
  native edition of a non-CJK target (W43 ES×JA: 3,005 on its own week);
  every added character is Japanese explanation-layer text, adjudicated by
  the itemization below, not by the strict-CJK flag (which is the
  Japanese-native-edition expectation, as in W43 §4).
- **Spanish token multiset (strongest freeze check):** Latin-script tokens
  core **5,437** vs edition **5,397** (CORRECTED in the fix round — the
  first-issue figures 5,430 / 5,390 matched no reproducible tokenizer;
  see §9.2 for the full correction note). Tokenizer, stated so the
  figures reproduce exactly: `tools/freeze.py` `<text>` extraction
  (same as `load_texts`) + Spanish-alphabet token regex
  `[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+`. Quirk of that tokenizer, verified by
  recount: the Catalan `ç` falls outside the Spanish-alphabet set, so
  each of the 42 `Barça` tokens in either edition counts as two
  (`Bar` + `a`) — that is the entire +42 vs a Latin-extended count.
  Cross-check with Latin-extended regex `[A-Za-zÀ-ÖØ-öø-ÿ]+`: core
  5,395 vs edition 5,355 — same difference (40), same only-in-core /
  only-in-edition multisets. Only-in-core tokens are exactly the declared
  furniture: the P1 tagline words (EL PERIÓDICO SEMANAL PARA APRENDER — LA
  VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA, 11 tokens), the footer English line
  (LUCERNA + SPANISH + WEEKLY, 8 pages each), and the P8 separators
  (PÁGINA ×8). Only-in-edition Latin tokens are `N` ×1 (from the Japanese
  band line `29-Nまで…`) and `CL` ×2 (the standard Japanese sports-press
  abbreviation inside two Japanese notes) — Japanese-layer abbreviations,
  not Spanish body text. **No Spanish token was lost or added.**
- Removed non-CJK strings, itemized: P1 tagline ×1 (→ badge, §2); P2
  `AEK）` + `）` (re-wrap fragments of the frozen calendar line — the token
  AEK survives in the edition); P6 ×4 (re-wrap fragments of frozen Spanish
  paragraphs — every word survives; the breaks moved because the JP face
  measures Latin glyphs marginally differently from the SC face); P7
  `mejor。` (wrap fragment — the word mejor survives); P8 separators ×8
  (→ Japanese separators, §2). Removed-side non-explanation items = 0.

## §2 Furniture (verbatim from the shipped W43 ES×JA edition, VOL.1→VOL.2 only)

Source of every string: the shipped W43 SVGs in `files/weekly-report-es-ja/svg/`
(+ that edition's KIT §3). Checked against tools README #20: for the ES
family the shipped form and the README agree (ES cores carry a native
subtitle slot at y=372, so the badge replaces it in place at 19.5pt) — no
shipped-wins override was needed; had they conflicted, the shipped form
would have won and the override would be recorded here.

- Masthead: **La Lucerna**
- P1 badge (brick #a4553a, 19.5pt bold, subtitle slot y=372, replaces the
  core tagline line): `スペイン語テキスト · 日本語の解説 — 日本語読者のための版`
- P1 edition line (46pt): `ス ペ イ ン 語 週 刊 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL`
- P1 top strip: `CADA SEMANA EN ESPAÑOL · 毎週一号 · スペイン人が読んでいるスペイン語を読む`
- P1 band right lines: `29-Nまであと27日 · 住宅が選挙戦を決める` /
  `今号のトップ · 詳しくは2・6ページ`
- Footer, all 8 pages: `La Lucerna · スペイン語週刊 VOL.2 · 本文はスペイン語 · 解説は日本語`
  + page line `N ページ（全 8 ページ）` (1–8 verified per page)
- Section heads: `VIDA · 暮らし` / `CULTURA · 文化` (shared kanji, as in W43) /
  `DEPORTE · スポーツ` / `JUVENTUD · 若者` / `A FONDO · 深掘り` /
  `LENGUA · ことば` / `EJERCICIOS Y RESPUESTAS · 練習と答え`
- Box/section second halves (W43 verbatim): `LA NOTICIA · トップ記事`,
  `LA SEMANA EN CIFRAS · 今週の数字`, `AHORA TÚ · すぐ練習`,
  `五大見どころ · Para entender la semana`, `EN ESTA EDICIÓN · 今号の目次`,
  `BREVES · 短報`, `QUIZ RELÁMPAGO · クイズ`,
  `EJERCICIOS · Nページの練習`, exercise right note
  `答えは8ページ · レベル混合の問題もあります。番号で探してください`,
  `¿Y TÚ? · あなたは？`, `ERRORES TÍPICOS · よくある間違い`,
  `LA PALABRA · 今週の単語`,
  `FRASES DE LA SEMANA · 今週の文（今号の記事から一字一句そのまま）`,
  `LA PRÓXIMA SEMANA · 次号予告 (VOL.3)`
- Gloss prefix: `解説 — ` (bslib `gloss()`); explanation calls renamed
  `bridge()` → `expl()` exactly as in W43 (def ×1 + call sites ×20).
- P8 header: `RESPUESTAS · 全解答と解説（1–8ページ）`; right note
  `各問に日本語の解説つき · ✓ は模範文のある問題`; separators
  `— N ページ —` ×8 (Japanese form, W43 precedent).
- Type labels (W43 1:1 mapping): 完成句子→文の完成, 单选→選択問題,
  词汇配对→単語のペア, 判断对错→正誤判断, 造句→文を作る,
  句型转换→文の書き換え, 完形单选→穴埋め選択, 翻译→翻訳, 写作→作文.
  Instr labels: 填空→空所補充, 判断→正誤, 把词和释义配对→語と意味を結ぶ
  (造句/改写/翻译/写作 share their type's Japanese form).
- Declared unchanged shared-kanji items (W43 §6 precedent): `文化`,
  `el cementerio 墓地`, `cementerio = 墓地`, `himno = 国歌`, `原形`
  (in `vamos a + 原形` etc. and `(原形 acoger)`), and the P7 letter's
  full-width attribution `（ejemplo, escrito por la redacción）` with the
  frozen Spanish letter body (Ana, Shanghái).

## §3 Registry & P8 gate

- **150 exercises — A2 50 · B1 72 · B2 28; per page 10/18/18/18/18/18/12/38;
  page/level/type identical to the core for all 150.** Build warnings:
  **FLOW OVERFLOW 0 · HEAD TOO WIDE 0** (final build).
- Type counts: 文の完成 48 · 選択問題 47 · 単語のペア 12 · 正誤判断 8 ·
  文を作る 7 · 文の書き換え 10 · 穴埋め選択 13 · 翻訳 4 · 作文 1.
- `tools/p8.py compare` (explicit `--core-p8/--edition-p8`, total 150):
  **CLEAN, 150 = 150, missing = [], extra = 0**, keydiff list of 15.
  First-dash adjudication (key = text before the first ` — `, byte-compared):
  - **13 of 15 are tool extraction artifacts** (README #13 class): the
    first-dash keys are byte-identical to the core; `p8.py`'s paren branch
    diverted because the Japanese note ends in a full-width paren group
    (#2, #11, #12, #29, #125: key + note-head swallowed up to the paren) or
    contains one (#83, #85, #95, #96, #98, #107, #117, #148). True keys
    verified identical item by item against the printed lines.
  - **Exactly 2 true key changes, the W43 precedent (translation items
    re-aimed ES→reader language):**
    - **#137** key core `周一在九个自治区是假日。` →
      `月曜日は9つの自治州で祝日です。` (note `原文を参照`)
    - **#138** key core `周日我们看 NFL 和马竞–巴萨。` →
      `日曜日はNFLとアトレティコ–バルサを見ます。` (note `原文を参照`)
  - **#139/#140** (reverse direction): stems re-aimed at Japanese
    (`ベルナベウはNFLの試合を開催する。→ ___`,
    `どのグラフにも出典を明記しなければならない。→ ___`); **Spanish keys
    byte-identical to the core** — same pairing as W43 §3.
  - **#150** (作文, apparatus line): renders
    `150. ✓ 模範文はこのページの H 欄（84語）` (W43 wording with the W45
    word count 84, not 82).
  - One language-neutral note kept identical to the core: P6 §A
    `34 + 22,2 + 17,1 = 73,3` (digits only); the P1 #1 note is frozen
    Spanish (`las listas ya están presentadas; ahora se escriben los
    programas`), as in the core.

## §4 Geometry gates

- `tools/occlusion_audit.py` (selftest passed first): **this edition 0 flags;
  core 0 flags; NEW vs core 0** (fix-round run
  `hidden_files/w45-es-ja-occlusion4.json`; the pre-fix run
  `hidden_files/w45-es-ja-occlusion3.json` read the same).
  Two earlier self-found flags were real, Japanese-length defects, both
  fixed by shortening Japanese text only (§6) — the final 0 is not an
  inheritance claim.
- **Same-baseline ink scan** (own implementation, true-ink boxes via PIL at
  4× supersampling, furniture bands included): **0 collisions** on all 8 pages.
- **P6 chart element check:** all 34 `<rect>` elements byte-identical to the
  core; chart value labels identical (CIS PSOE 34,0 / PP 22,2 / Vox 17,1 /
  Sumar 6,1 / Podemos 3,1; problem chart 55,7 / 20,9 / 20,3); no second data
  series printed.
- **P6 Inmigración graze — frozen core geometry, non-blocking known defect
  (NOT fixed, per ruling):** the chart label `Inmigración` (baseline y=1717,
  ink box x 1011.0–1144.2, y 1723.2–1746.8) is overlapped by the later-drawn
  bar rect (x=1139.0, y=1730.0, w=152.25, h=22.0) by **5.2 px horizontally**
  (16.8 px vertically). Measured **identical in core and edition**
  (same ink box, same rect, same 5.2 px overlap) — the edition's P6 geometry
  is byte-identical to the core here, and the core chart was not touched.
  It is below the audit's 30% COVER threshold, which is why the audit reads
  0 flags on both; it is recorded here, not repaired, because the ruling
  freezes core geometry.

## §5 Content gates

- **Gloss, split on `·` itself (README #21):** content12 (P2) 5 ·
  content34 (P3) 5 + (P4) 5 · content56 (P5) 4 = **19, equal to the core's
  19 item by item** (Spanish headwords in the same order).
- **Image payloads:** per-page `<image>` counts and SHA-256 identical to the
  core (P1/P2/P4/P6/P7/P8: 0; P3: 1; P5: 1 — the W43-verified CC0/USDA photos;
  the P1 houses are vector paths from the frozen `illus_houses()` function,
  not a photo).
- **P7 golden sentences:** all 8 Spanish quotes verbatim from this issue's
  articles; each occurs **exactly 2 times** across the 8 SVGs (article + P7
  table, whitespace-normalized programmatic count); page tags
  (Página 1..6) = 1:2, 2:1, 3:1, 4:1, 5:1, 6:2, identical to the core.
- **Readers' letters (no invented readers/letters/quotes):** P7 carries the
  core's labelled editors' example letter (Ana, frozen Spanish, attribution
  intact) + the FIX1 disclosure in Spanish (frozen) and Japanese. The
  Japanese disclosure states all three facts: no real readers' letters had
  arrived, no best P8 texts had arrived, the example is printed and the
  promise carries to VOL.3 — **plus, since fix round 2 (§9.4), the explicit
  public invitation `手紙をお待ちしています。`** (label trimmed
  `編集部より：` → `編集部：` to hold the original 3 lines; the three
  fact clauses are byte-identical — the trim is disclosed in §9.4 for
  the next independent proofreader's own acceptability judgment).
- **Japanese typography:** canonical JA svglib kinsoku + SEAM_SLACK=28 (see
  §7); post-kinsoku line-start orphan scan = **0** (full-width closers,
  small kana `ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮ`, long vowel mark `ー`,
  AND ASCII closers `)]}.,!?%:;"'` all covered — CORRECTED in the fix
  round: the first-issue scan set contained NO small kana, so its
  "small kana covered, scan 0" claim was false and it missed the P5
  orphan; the set was extended in both the build-copy svglib NO_START
  and the self-audit scan, and the full 8-page rescan reads 0 — see
  §9.1 for the evidence);
  row-end width re-check after kinsoku: no line exceeds its column (audit
  0 flags + same-baseline scan 0); kanji-only nodes adjudicated one by one
  — all legitimate Japanese (type/instr labels, shared terms in §2, wrapped
  fragments); Simplified-only blocklist scan = **0 hits** (no residual
  Chinese explanation text).

## §6 Self-found defects & fixes (Japanese side only, never core geometry)

1. **P1 word-of-week note crossed the 1844 rule (LINEX, real):** the Japanese
   note wrapped to 2 lines with the orphan line `間。` at baseline 1841.85,
   its ink crossing the row-B rule. Fixed by shortening to one line:
   `「プレキャンペーン」：正式選挙戦の前数週間。` (verified 1-line wrap at
   19pt in 434px). Audit flag cleared.
2. **P7 preview box pushed onto the footer (TEXTX, then FOOTER/LINEX, real):**
   the Japanese word-box note wrapped to 4 lines (core Chinese: 3) and the
   Japanese disclosure to 4–5 lines (core: 3), shifting the preview box
   from the core's y=2440.08 down to 2527.08, where its body text overprinted
   the footer. Fixed by shortening both Japanese strings to the core's line
   counts — word note to 3 lines
   (`precampaña = プレキャンペーン：選挙戦前の数週間。今号は precampaña；選挙戦は13日（金）に始まる。`,
   applied identically to the height-formula copy and the printed copy) and
   disclosure to 3 lines
   (`編集部より：本物の手紙も最優秀作文も届かなかったため、見本の手紙を掲載します。約束はVOL.3へ。`).
   Preview rect returned to **y=2440.08, exactly the core's position**; final
   audit 0 flags. The invitation sentence was dropped from the disclosure to
   hold 3 lines; the three required facts are all present. (That dropped
   invitation was the re-proof blocker; it was restored in fix round 2 —
   see §9.4 — without adding a line.)
3. **P1 band-right and badge widths:** checked by the same-baseline scan (0)
   and card目检 — no collisions with the left band text.

## §7 svglib & reproducibility

- The canonical JA svglib file (`hidden_files/weekly-report-ja-build/svglib.py`,
  md5 `d73e23b365676c3618d7e060b835eb4d`) was **never edited** — re-verified
  byte-identical after the fix-round build. The build copy's svglib is the
  canonical file **plus exactly two deltas** (diff-verified, no other
  line differs): (1) the verbatim append of the core build's
  `illus_houses()` function (frozen P1 houses illustration, 2,209 chars),
  without which P1 cannot render; (2) FIX-W45-ESJA-1: the `NO_START`
  line extended with the small kana
  `ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮ` (long vowel `ー` was already
  in the set). The extension follows the tools README #19 pattern
  (build COPY extends NO_START, canonical never edited; the
  proofreader must diff the two files and confirm the change is
  exactly that line plus the append). Mechanism, JP face selection, and
  SEAM_SLACK=28 all come from the canonical file itself. The W43 ES×JA
  precedent used the canonical set unmodified; this edition cannot,
  because its Japanese explanation layer wraps a word (`アトレティコ`)
  across a line break in a way the unmodified set does not guard —
  see §9.1.
- **Reproducibility verified:** a fresh copy of the core build + canonical
  svglib + the same `illus_houses()` append + the same transform script +
  `run.py` reproduces all 8 delivered SVGs **byte-for-byte** (hashes in §0
  header). The transform script in `hidden_files/` is the final, corrected
  version (it already contains the §6 shortenings).
- Card目检: P1, P6, P7 rendered cards inspected at full size — badge,
  band lines, word note clearance, P6 charts, P7 letter/disclosure/quotes/
  preview clearance all as specified; no overflow, overlap, or truncation
  seen.

## §8 Known items (carried, not defects introduced here)

- P6 Inmigración 5.2 px graze (§4): frozen core geometry, recorded, not repaired.
- The core's FIX1/FIX2 history stands as recorded in the core KIT (11月12日
  date removed in FIX1; P8 #57 note corrected in FIX2); this edition inherits
  the fixed core text byte-for-byte.
- W45 core KIT §6.3's illustration note stands: the P1 houses are an
  editors' program-drawn illustration, captioned as such on the page, not a
  photograph.

## §9 Fix round (independent proofread blockers 1–2, hidden_files/w45/es-ja-proof/REPORT.md)

Fix method: single-process re-render only — `run.py` (one driver process
for content12 → 34 → 56 → 7 → 8, shared registry) then `render.py`
(tools venv python, for cairosvg/pypdf); no content module was imported
inside the core build dir; no rewording of any Spanish body text; the
only source edits are the two NO_START extensions below, each applied
as an exact unique literal with a count assertion (count == 1).

### §9.1 P5 line-start small-kana orphan (kinsoku) — FIXED

- **Before:** P5 `EL PLAN DEL PUENTE` item 4, SVG (x=545, y=851.16) →
  (x=545, y=879.72): upper `en el Metropolitano（日曜夜：アトレテ`,
  lower `ィコ対バルサ）` — `アトレティコ` cut mid-word,捨て仮名 `ィ`
  stranded at line start. Root cause, confirmed: the builder
  self-audit script's NO_START set
  (`。、，．！？：；）」』】ー…‥・)]}.,!?%:;"'`) contained no small
  kana at all, so the first-issue §5 claim of small-kana coverage was
  false; the canonical JA svglib NO_START has the same gap.
- **Fix (no rewording, no Spanish change):** the build-copy svglib
  NO_START line extended with
  `ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮ` (README #19 pattern;
  canonical file untouched, md5 re-verified). The kinsoku oidashi then
  pulls `テ` down with its small kana, preserving line count and every
  character. The self-audit script's scan set was extended identically
  (`SMALL_KANA` + original set = 48 members).
- **After (new line break, same coordinates, same wording):**
  upper `en el Metropolitano（日曜夜：アトレ`, lower
  `ティコ対バルサ）` — the second line now starts with full-size `テ`
  followed by `ィ`; the word `アトレティコ` is intact across the break.
  P5 card目检: item 4 reads `en el Metropolitano（日曜夜：アトレ /
  ティコ対バルサ）`, neighbours (items 3, 5) unchanged, no overflow.
- **Rescan evidence (full 8 pages, 0):** builder self-audit
  (`hidden_files/w45-es-ja-audit.py`, extended set) — same-baseline ink
  scan 0, orphan line-starts **0**; independent rescan (extended set,
  raw + lstrip + strip variants × 8 pages) — **0**. Only p5 changed
  (see byte table below), so no other page could have gained an orphan.

### §9.2 KIT §1 Latin token totals — CORRECTED

- **Before:** core 5,430 / edition 5,390. **After:** core **5,437** /
  edition **5,397**. The freeze conclusion is unchanged and still true
  (no Spanish token lost or added): difference 40 both before and after,
  only-in-core 43 (P1 tagline 11 + footer English line 24 + P8
  separators 8), only-in-edition 3 (`N` ×1 + `CL` ×2).
- **Why the old numbers were wrong:** they reproduce under neither
  tokenizer. Recount method (freeze.py `<text>` extraction):
  Spanish-alphabet regex `[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+` gives exactly
  5,437 / 5,397; the +42 vs Latin-extended
  (`[A-Za-zÀ-ÖØ-öø-ÿ]+` → 5,395 / 5,355) is fully explained — the
  Catalan `ç` is outside the Spanish-alphabet set, so all 42 `Barça`
  tokens count as two each (`Bar` + `a`) in both editions. The §1
  figures now state this tokenizer so they are reproducible.

### §9.3 Fix-round re-verification (all gates re-run on the fixed files)

- `tools/occlusion_audit.py` selftest passed; edition **0 flags**,
  core 0 flags, NEW vs core **0**
  (`hidden_files/w45-es-ja-occlusion4.json`).
- Same-baseline ink scan (self-audit): **0 collisions**, all 8 pages.
- `tools/p8.py compare` (explicit core/edition P8): **CLEAN,
  150 = 150, missing = [], extra = 0**, keydiff unchanged
  `[2, 11, 12, 29, 83, 85, 95, 96, 98, 107, 117, 125, 137, 138, 148]`.
- Registry (single-process run): **150; A2 50 / B1 72 / B2 28;
  per page 10/18/18/18/18/18/12/38**; FLOW OVERFLOW 0 / HEAD TOO WIDE 0.
- `tools/freeze.py diff`: added CJK total still **3,007** (the P5 fix
  moves one kana across a line break; no character added or removed).
- Cards 1950×2700 ×8; PDFs 8 pages each — print 21,775,534 B
  (same byte size as pre-fix by coincidence; SHA changed with the P5
  page), web 3,639,060 B (< 10 MB).
- Per-page SVG byte identity vs pre-fix (sha256, full hashes in the
  header; truncated here): p1 `098de92d…` IDENTICAL · p2 `d5bbf5d1…`
  IDENTICAL · p3 `b8cd0e6a…` IDENTICAL · p4 `196e97a3…` IDENTICAL ·
  p5 `1cd8a67f…` → `1534eea1…` **CHANGED (only page)** · p6
  `481ffa7a…` IDENTICAL · p7 `a09489ea…` IDENTICAL · p8 `dac6d639…`
  IDENTICAL. Cards: only `p5-juventud.png` changed
  (`32b7655b…` → `47b2a820…`); the other 7 PNGs are byte-identical.
- **This fix round is NOT a final edition:** per SOP §8.4 it must pass
  a fresh independent full re-proof before any final claim.

### §9.4 P7 readers'-letter invitation restored (re-proof blocker, hidden_files/w45/es-ja-reproof/REPORT.md problem 1) — FIXED

- **Before (3 lines, no invitation):**
  `編集部より：本物の手紙も最優秀作文も届かなかったため、見本の手紙を掲載します。約束はVOL.3へ。`
  — three facts only (no real letters, no best P8 texts, example printed +
  promise to VOL.3); the frozen Spanish note likewise had no invitation,
  and the core Chinese note's closing `欢迎来信！` was the one explicit
  invitation, dropped in this edition to hold 3 lines (§6.2). The P7
  preview line `tus cartas` is a contents preview (Spanish only) and the
  other pages' ¿Y TÚ? lines are exercise prompts — neither counts as a
  readers'-column invitation, per the es-ru / ru-nl rulings on the
  identical defect.
- **After (still 3 lines, invitation restored):**
  `編集部：本物の手紙も最優秀作文も届かなかったため、見本の手紙を掲載します。約束はVOL.3へ。手紙をお待ちしています。`
- **What was kept byte-identical:** all three fact clauses
  (`本物の手紙も最優秀作文も届かなかったため` /
  `見本の手紙を掲載します` / `約束はVOL.3へ`), the frozen Spanish note,
  the Ana example letter and its full-width attribution
  `（ejemplo, escrito por la redacción）`. No reader, letter, or quote
  was invented — only the invitation clause was added.
- **Label trim, stated plainly for the next proofreader's independent
  judgment (NOT pre-judged acceptable here):** the attribution label
  was shortened by one word, `編集部より：` → `編集部：` (dropped `より`,
  2 characters; "from the editorial department" → "editorial
  department"). This is the es-ru fix precedent exactly (es-ru:
  `Примечание редакции:` → `Примечание:` to fit `Ждём писем!` in
  3 lines, independently judged acceptable in es-ru-reproof).
  The trim was a necessity, not a preference — measured with the
  build's own `wrap()` (sans 20pt, width 390, i.e. CW−44):
  old label + invitation = **4 lines** (4th line a lone `す。`);
  trimmed label + invitation = **3 lines**; a plain-verb variant
  (`手紙を待っています。`) also fits in 3 lines with the old label,
  but the polite `手紙をお待ちしています。` form was chosen per the
  task wording, with the label trim as the es-ru-precedented cost.
  The next independent proofreader must judge the trim acceptable or
  not on its own merits; this KIT records it, it does not bless it.
- **Line-count math (why no 4th line is possible):** pre-fix P7
  geometry — disclosure baselines y=1775.89 / 1804.29 / 1832.69,
  FRASES hline y=1841.08, preview rect y=2440.08 h=118 (bottom 2558.08),
  footer line y=2580 (margin 21.92). One extra disclosure line adds
  29px to the readers' box height, pushing the preview bottom to
  2587.08 — past the footer line. Hence the invitation had to fit in
  the original 3 lines.
- **Method:** whole-line replacement of `ldcn` in
  `hidden_files/weekly-report-w45-es-ja-build/content7.py:100` by exact
  unique literal, count assertion 1×; then single-process re-render
  (`run.py` content12→34→56→7→8, shared registry) + tools-venv
  `render.py` (cards + both PDFs). No content module was imported
  inside the core build dir. Pre-fix baseline (full sha256 of 8 SVGs,
  8 cards, both PDFs) was written to
  `hidden_files/w45-es-ja-build5.log` BEFORE the re-render, after a
  start-of-work concurrency check (no render process running; 70s
  recheck with zero new writes) — so the byte table below is
  checkable, unlike the round-1 gap the re-proof flagged.
- **Geometry after (measured from the delivered p7-lengua.svg):**
  disclosure STILL 3 lines at UNCHANGED baselines y=1775.89 /
  1804.29 / 1832.69 (L1 `編集部：本物の手紙も最優秀作文も届かな` /
  L2 `かったため、見本の手紙を掲載します。約` /
  L3 `束はVOL.3へ。手紙をお待ちしています。`); readers' box end
  (P7 col3) 1820.08, unchanged; ES note baselines unchanged
  (1632.29 / 1660.69 / 1689.09 / 1717.49); Ana letter baselines
  unchanged (1388.58–1571.76); FRASES hline y=1841.08 and header
  y=1879.08 unchanged; preview rect y=2440.08 h=118 unchanged;
  total `<text>` elements 155.
- **Re-verification on the fixed files:**
  - `tools/occlusion_audit.py` selftest passed; edition **0 flags**,
    core 0 flags, NEW vs core **0**
    (`hidden_files/w45-es-ja-occlusion5.json`).
  - `tools/p8.py compare` (explicit core/edition P8): **CLEAN,
    150 = 150, missing = [], extra = 0**, keydiff unchanged
    `[2, 11, 12, 29, 83, 85, 95, 96, 98, 107, 117, 125, 137, 138, 148]`
    (`hidden_files/w45-es-ja-p8-5.json`).
  - Registry: **150; A2 50 / B1 72 / B2 28;
    per page 10/18/18/18/18/18/12/38**; FLOW OVERFLOW 0 / HEAD TOO WIDE 0.
  - Builder self-audit orphan rescan: **0** (P5 small-kana fix intact);
    the only remaining known item is the frozen-core P6 Inmigración
    5.2px graze, unchanged.
  - P7 card目检 (full size): disclosure 3 lines fully readable inside
    the readers' box, invitation on the last line, no overflow,
    overlap, or truncation; FRASES, preview box, and footer all clear.
  - Canonical JA svglib md5 re-verified
    `d73e23b365676c3618d7e060b835eb4d` (never edited).
- **Per-page byte identity vs this round's pre-fix baseline
  (build5.log):** SVG p1–p6, p8 IDENTICAL; only p7 CHANGED
  (`a09489ea…` → `20f1a1dc…`). Cards p1–p6, p8 IDENTICAL; only p7
  CHANGED (`ffbaecae…` → `551e0cc6…`). Both PDFs changed (P7
  embedded): print 21,775,534 B → **21,775,658 B**
  (sha256 `7ebbf37e…`), web 3,639,060 B → **3,639,992 B**
  (sha256 `56ed27fd…`).
- **This fix round is NOT a final edition:** per SOP §8.4 it must pass
  a fresh independent re-proof (at minimum the P7 invitation point,
  the label-trim acceptability judgment, the audit-0 result, and the
  P7 card) before any final claim.

