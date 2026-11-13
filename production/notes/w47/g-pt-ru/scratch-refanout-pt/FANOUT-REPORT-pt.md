# FANOUT-REPORT-pt — W47 pt 全族重建 (core-pt fix2)

**Rebuild date:** 2026-11-11. **Core:** `~/workspace/weekly-git/production/2026-w47/core-pt/`
at fix2 (`d2b0e182`). **Driver home:** `scratch-refanout-pt/` (this directory).
**No commit, no push.** All ten editions rebuilt from scratch in
`~/workspace/weekly-git/production/2026-w47/2026-w47-pt-<lang>/`; the first-round
editions were backed up first (`backup-old/`, 293 MB, SHA list `backup-sha.txt`).

**Interpreter (every step, all 10 editions):**
`~/workspace/weekly-git/tools/venv/bin/python` — Python 3.12.3, Pillow 13.0.0,
FreeType 2.14.3 (bundled `pillow.libs/libfreetype-57f805ba.so.6.20.6`),
HarfBuzz bundled, raqm 0.11.0. System python3 was NOT used anywhere.
Tools: `build_edition.sh <lang>` (build) + `gates_pt.py <lang> --skip-render`
(gates) + `classify_pt.py <lang>` (hand-patch inventory) + `gloss_probe.py`
(P4 gloss PIL measurement) + manual contact-sheet review of all 8 pages per edition.

## 1. New files — full SHA-256 + bytes (30)

| Edition | File | Bytes | SHA-256 |
|---|---|---|---|
| pt-de | `A-Lucerna-VOL4.pdf` | 12938914 | `77243c72c38a14232ea443f03856ccf0a88f3d4b2c0c89e75aa87cf658e6284a` |
| pt-de | `A-Lucerna-VOL4-web.pdf` | 1147629 | `56eb92d0251d691956e8dac6cccab0e9bf2a4bbadd9dc662c55632eb1b13b84b` |
| pt-de | `2026-w47-pt-de.text.md` | 37907 | `519ab0dedbae110dba11eeffe3cd8517db41141020061e9a66c5dd252d784305` |
| pt-en | `A-Lucerna-VOL4.pdf` | 12932439 | `782e7cb9d9109f4282667fd6dde71ab981933fa5290a9cd4882aaa49322cca6d` |
| pt-en | `A-Lucerna-VOL4-web.pdf` | 1139921 | `e02cf58cbee4cf5daac47fccc9319faf8158b6b31523ba220794f415a5e9bb61` |
| pt-en | `2026-w47-pt-en.text.md` | 37333 | `513326ffa497ca2b6714c1016eadbfaa2ac3447269b782749c968022e0e118ed` |
| pt-es | `A-Lucerna-VOL4.pdf` | 12933062 | `f1b4fc207a3575391868aeb9c8f7d0f34659c434ecf3a13c85c8cba19362a0d4` |
| pt-es | `A-Lucerna-VOL4-web.pdf` | 1140276 | `d00e8f5420750496b7cb7551eab51e7207a123b1c3f0a55896aead83dac4ae7c` |
| pt-es | `2026-w47-pt-es.text.md` | 37467 | `96d6f11a5616ab97291115bb9da0577bce8049031f14988576f6cced77b29e27` |
| pt-fr | `A-Lucerna-VOL4.pdf` | 12934630 | `4b9f41475eb5ec7ec7e81cb372c50a58b6d7516c17a21fd1e2745ff7189f7653` |
| pt-fr | `A-Lucerna-VOL4-web.pdf` | 1141286 | `1f5cc5adc131bf16bd4a1f3a796e3470a399293f7f99e15f61f0ccfdb5080fb3` |
| pt-fr | `2026-w47-pt-fr.text.md` | 37699 | `39d06879d21b37ecca7b42ddb55214391bcb3c1aa6215cbcb39b184176e0a8e2` |
| pt-it | `A-Lucerna-VOL4.pdf` | 12930828 | `6c8a5f3db220dcdfba6e0904b12ec66e37062f0007cfaeb9aed71b208e9911ce` |
| pt-it | `A-Lucerna-VOL4-web.pdf` | 1137080 | `5ebf28b436f60fe0b59dcff89a4f1bf62dc0aa93bf4a4e2e7da9a2e965114e89` |
| pt-it | `2026-w47-pt-it.text.md` | 37419 | `37c1980caacc6cef28d9df50133b09b45a51a8d4f17296e34412b2cd88285209` |
| pt-ja | `A-Lucerna-VOL4.pdf` | 24991049 | `e45f4a9471d59a78e615cfd010679b7aff4dd963f092ab7457f6d8214fda8a08` |
| pt-ja | `A-Lucerna-VOL4-web.pdf` | 1680796 | `ff67441e1c61e58b002b0a9c40711732512d089bde84aeadc57ff774778281e8` |
| pt-ja | `2026-w47-pt-ja.text.md` | 37915 | `90dcdcca7821049a9af8735653d7059e4a111eeaae6dfebf1ea1467941ec9830` |
| pt-ko | `A-Lucerna-VOL4.pdf` | 17185806 | `ac839d227acb506f71ccfd05a1b63915a22cca91c6bcb0cec0cecd025c2de6e1` |
| pt-ko | `A-Lucerna-VOL4-web.pdf` | 1431508 | `f505a301e3cb22645aba7131fb61d2f6f445d41ff670bfb3aa63dcebb071c38f` |
| pt-ko | `2026-w47-pt-ko.text.md` | 37823 | `fe14281fdd24abcfc527d359d707aef97b6d92bc9d602cd38ce1a4fbf6c791c4` |
| pt-nl | `A-Lucerna-VOL4.pdf` | 12935296 | `7404001d519ac57d932fb99a7f73d59c0036a5de8d4ef35c276a8a9bca335029` |
| pt-nl | `A-Lucerna-VOL4-web.pdf` | 1142955 | `f8119356b8032f6720de25567367a53911958fe51c194d2e1d366130bcca9be3` |
| pt-nl | `2026-w47-pt-nl.text.md` | 37559 | `6f8d4d5960326b69f7ad639dbedc3a15ec8972780e292b2e2c3625001b5532cd` |
| pt-ru | `A-Lucerna-VOL4.pdf` | 12916388 | `86447421b5a5abff48690ed8ab8e4cd51ce9808e5adcaf24f0d8e30004a0d2f2` |
| pt-ru | `A-Lucerna-VOL4-web.pdf` | 1188615 | `acd86e86bc20562c2080952bec2c89071c85c1733d2cb5183f4dc6d90253b779` |
| pt-ru | `2026-w47-pt-ru.text.md` | 39736 | `87871659c0101a9d8c2f7bc415946653ea80257032332cda8b1208e6288184c8` |
| pt-zh-tw | `A-Lucerna-VOL4.pdf` | 24130648 | `42d7d4de02fadf02f82007e7230cc84ed75fb6181a90c0d65702a257bb7d9b11` |
| pt-zh-tw | `A-Lucerna-VOL4-web.pdf` | 1820203 | `bf86bcc80642b13d164c523cd683b1cd6f41578a67bd9f8664226ba8153b7512` |
| pt-zh-tw | `2026-w47-pt-zh-tw.text.md` | 36875 | `5cd5c7270e6a3dc0bfe2f5c0c644f782189bffff9df5be2d10d9e07fd49a2888` |

Old (first-round) files are listed with full SHA in `backup-sha.txt`.
Note: en `text.md` is byte-identical to its first-round file (same SHA
`513326ffa497ca2b6714c1016eadbfaa2ac3447269b782749c968022e0e118ed`).

## 2. Gates per edition

All editions: edition `gates.py` 16/16; p8 extract 150/150; p8 compare CLEAN
(keydiff [137, 138] — expected, Q137/138 keys re-aim at the reader language);
freeze baseline 8/8; creambox 0 spill; keycheck 149/150 (Q150 = open writing task,
extracted as `✓`) unless noted; sweep 1 bridge widow (proof1 F1 — the '0' originally written here was wrong); italic spans print 1 = web 1;
check_final word multiset diff 0 (print == web).

| Edition | run/occl | p8 | freeze | creambox | boxtitle | keycheck | print/web text | P8 min | multiset |
|---|---|---|---|---|---|---|---|---|---|
| pt-de | 0/0 | 150/150 CLEAN | 8/8 | 0 | clear | 149/150 | byte-identical (111,362) | 9.75pt | 0 (8,436) |
| pt-en | 0/0 | 150/150 CLEAN | 8/8 | 0 | clear | 149/150 | byte-identical (110,367) | 9.75pt | 0 (8,507) |
| pt-es | 0/0 | 150/150 CLEAN | 8/8 | 0 | clear | 149/150 | byte-identical (109,231) | 9.75pt | 0 (8,576) |
| pt-fr | 0/0 | 150/150 CLEAN | 8/8 | 0 | clear | 149/150 | byte-identical (110,813) | 9.75pt | 0 (8,629) |
| pt-it | 0/0 | 150/150 CLEAN | 8/8 | 0 | clear | 149/150 | byte-identical (110,388) | 9.75pt | 0 (8,457) |
| pt-ja | 0/0 | 150/150 CLEAN | 8/8 | 0 | clear | 149/150 | byte-identical (107,708) | 10.125pt | 0 (6,896) |
| pt-ko | 0/0 | 150/150 CLEAN | 8/8 | 0 | clear | 149/150 | byte-identical (105,505) | 10.125pt | 0 (7,052) |
| pt-nl | 0/0 | 150/150 CLEAN | 8/8 | 0 | clear | 149/150 | byte-identical (111,218) | 9.75pt | 0 (8,557) |
| pt-ru | 0/0 | 150/150 CLEAN | 8/8 | 0 | clear | 148/150 * | P8 spacing only * | 9.75pt | 0 (8,093) |
| pt-zh-tw | 0/0 | 150/150 CLEAN | 8/8 | 0 | clear | 149/150 | byte-identical (103,995) | 10.125pt | 0 (7,011) |

\* ru two known deviations (both pre-existing in the first-round edition, NOT
regressions from this rebuild — see §6): (1) keycheck 148/150, exit 1 by design:
Q137 extracts truncated (`Пятница, 20 ноября,` — em-dash parse artifact in the
extractor, already adjudicated a non-defect in proof1) plus the expected Q150 `✓`.
The tool exits 0 only when every mismatch is Q150-with-`✓`, so ru necessarily exits
1. (2) print/web `pdftotext -layout` differ on P8 only (40 lines, single-space
column shifts around question numbers); the word multiset is identical (diff 0),
and the first-round backup's print/web pair differs the same way — verified by direct
comparison. `pdftotext -layout` spacing artifact on the web PDF subset-font layout;
text layers themselves identical.

Visual: every edition got a contact sheet of all 8 pages (2×4, `visual/<lang>-contact.png`)
plus full-resolution crops of change points; all reviewed clean. The P4 gloss box was
PIL-measured per edition (see §3).

## 3. D5 gloss — nine-edition disambiguation check

Core fix2 changed P4 gloss `o título 冠军` → `o título 冠军头衔` (content34.py:134 +
text.md:215). Each reader edition got the same disambiguation via a new SEG key
`冠军头衔` (longest-match wins over `冠军`); the old `冠军` mapping is untouched.

| Edition | New gloss value | Rendered in P4 gloss box | PIL lines / right clear / bottom clear | Overflow |
|---|---|---|---|---|
| pt-de | `Titel` | `o título Titel` | 4 / +101.5 / +42.7 | no |
| pt-en | *(already disambiguated)* | `o título title` | 4 / +190.5 / +42.7 | no |
| pt-es | `título` | `o título título` | 4 / +86.5 / +42.7 | no |
| pt-fr | `le titre` | `o título le titre` | 4 / +68.5 / +42.7 | no |
| pt-it | `titolo` | `o título titolo` | **5** / +340.5 / +47.7 | no |
| pt-ja | `優勝/タイトル` | `o título 優勝/タイトル` | 4 / +236.5 / +42.7 | no |
| pt-ko | `우승/타이틀` | `o título 우승/타이틀` | 4 / +280.5 / +42.7 | no |
| pt-nl | `titel` | `o título titel` | 4 / +197.5 / +42.7 | no |
| pt-ru | `титул` | `o título титул` | 4 / +99.5 / +42.7 | no |
| pt-zh-tw | `冠軍頭銜` | `o título 冠軍頭銜` | 4 / +383.5 / +45.7 | no |

**en:** the en gloss already read `o título title` — `冠军` was mapped to
`title`, not to the bare `champion`, so there was no ambiguity to remove.
Only the new SEG key was added to the en table (no rendering change); en
`text.md` is byte-identical to its first-round file and the rendered gloss is
unchanged. (it takes 5 lines because Italian is the longest rendering; still
inside the box with +47.7px bottom clear — no box height was changed anywhere.)

For reference, the core-pt fix2 gloss box is 3 lines, last line +3.1px, bottom
+47.7px; reader editions are 4 lines because the extra reader-language gloss
prefix (`Note |`, `解説 —`, `譯注｜`, …) plus the longer headword wraps one more line.
All fit with ≥ +42.7px bottom clear.

## 4. pt-ko rebase

pt-ko was rebuilt in full under the venv interpreter, NOT patched. The first-round
ko edition was actually built with system python3 even though its KIT said venv —
the venv-vs-system measurement difference (Korean space +1.11px) moved line breaks
in 4 places (P2/P3/P4/P7 gloss, proof1 O1). This rebuild's **freeze baseline 8/8 and
p8 extract 150/150 + CLEAN against the venv-built core** is the rebase proof.

The 4 line-break moves are layout changes, so per SOP §8.4 this edition needs a
full re-proof by a separate proofer — NOT self-certified final by this agent; this
is recorded in the ko KIT §9. Verified in the rebuild: SÁB 21 renders
`토요일 16:30, 파우메이라스 대 플라멩구`; Q65 reads
`65. B — 2일 차는 자연과학과 수학, 13:30–18:30`; D6 colons (24 spots, e.g.
`3 > 1: mais`, `채워요: prazo`) and D8 commas all correct. text.md diff vs the
first-round file is 5 lines (L215 D5, L280/L363/L393 D6 colons, L433 verbatim).
Word count print/web 7,052/7,052 — the +22 vs the first-round count comes from the
D6 `: ` insertions splitting tokens, not from content changes.

## 5. KIT build-command correction

The ko KIT recorded a venv build command while the build actually used system
python3. Every edition's KIT now carries a `Re-fanout (2026-11-11, core-pt fix2)`
appendix (appended after §8/§9, never rewriting the old sections) stating the actual
command used (`build_edition.sh <lang>` + `gates_pt.py <lang> --skip-render`), the
interpreter (venv python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3 / HarfBuzz bundled
/ raqm 0.11.0), the new SHA-256 + bytes, the gate results, the D5 gloss value with
PIL measurement, the proof1 fixes carried in, and the hand-patch inventory.
Es note (retained): the backup PDF has only fix1 tables, no fix1 geometry, so the
new-vs-old print-PDF text-layer difference is reflow only.

## 6. Edition notes (proof1 fixes carried in, per-edition)

| Edition | Proof1 fixes (verified by true-ink measurement where noted) |
|---|---|
| pt-de | None at edition level (D1–D3 all core). |
| pt-en | None (en was already disambiguated — see §3). |
| pt-es | D4 `口诀` → `La regla` (+97.3); D5 `常见错误` → `Errores` (+111.6); D6 `本周生词` → `La palabra` (+138.0). |
| pt-fr | D1 `数字` → `Chiffres` (+18.7); D2 `口诀` → `À retenir` (+89.7); D3 `常见错误` → `Erreurs` (+111.2); D4 kicker `sub330_size` 32→30, masthead x=139.5–1810.5 inside the 88–1862 frame (old 32pt started at x=83.7, ~4.4px over the left edge). |
| pt-it | D4 `本周生词` → `La parola` (+151.6); D5 `本期目录` → `Questo numero` (+23.3, fs=24; was +2.5px overflow). |
| pt-ja | D4 `数字` → `数字` (single character); D5 SÁB 21 whole-sentence key → `土曜日16:30、パルメイラス対フラメンゴ`; Q65 whole-sentence key (proof1 miss, same class) → `2日目は自然科学と数学、13:30–18:30`. Fragment keys `周六 16` / `至 18` deleted. Kinsoku svglib restored from backup (md5 `f61efb1bdac0e1c0a38fc60b300f238e` ≠ core `4228b7e7…`) — build driver copies it over the core's file before transform; verified post-build. |
| pt-ko | D6 colon rules + D8 comma rules (see §4); fragment keys `周六 16` / `至 18` deleted; SÁB 21 → `토요일 16:30, 파우메이라스 대 플라멩구`; Q65 → `2일 차는 자연과학과 수학, 13:30–18:30`. |
| pt-nl | D5 `口诀` → `Ezelsbruggetje` (+19.5; was +24.5px overflow); D6 `常见错误` → `Fouten` (+115.0); D4 E2 reworded `bewustzijn, geweten: de memorie aan verzet en cultuur` — last line `memorie aan verzet en cultuur.` has ink bottom exactly on the baseline (by1=0.00, no descenders) with last-line bottom clear +4.48px; the earlier +0.5px marginal overflow is gone. If a future venv rebuild still shows +0.5px, record it marginal per the ru O3 ruling — do not twist the translation again. |
| pt-ru | D1 `常见错误` → `Ошибки` (+97.5); D2 `数字` → `Цифры` (+20.2); SÁB 21 whole-sentence key (proof1 miss, same class) → `суббота, 16:30, дерби Палмейрас–Фламенго`. Ru O3 (P7 A PALAVRA last line, 0.5px zero margin) already adjudicated a non-defect in proof1; untouched. ru keycheck 148/150 and print/web pdftotext P8 spacing difference: pre-existing, see §2. |
| pt-zh-tw | D5 core gloss value `冠軍頭銜`. ABSTRACT.txt lacked the masthead (SOP §9), so the build driver prepended `A Lucerna 葡萄牙語週報 VOL.4：` to the copied-back file; the rest is unchanged. |

text.md diff vs first-round file (only L215 D5 gloss + L433 verbatim, unless noted):
de 2 lines; en 0 lines (byte-identical); es 2; fr 2; it 2; ja 2; ko 5 (D6 colons);
nl 3 (D4 E2 reword + D5 + verbatim); ru 2; zh-tw 2.

## 7. Hand-patch inventory (classify_pt.py)

`classify_pt.py <lang>` diffed the 9 build-source `.py` files (bslib4, content12/34/56/7/8,
gates, render, run, svglib) of each rebuilt edition against the backed-up first-round
edition and labelled every diff KEEP / REVERT / MERGE / INSERT / DELETE. Note on
direction: the backups all predate core fix1, so every fix1 line (P1 flash box 436→474,
P3 +26, P6 640→654, P8 `max_w=395`, bslib4 pipe rule) is KEEP, not a lost patch.

| Edition | KEEP | REVERT | MERGE | INSERT | DELETE |
|---|---|---|---|---|---|
| pt-de | 24 | 0 | 0 | 0 | 0 |
| pt-en | 23 | 0 | 0 | 0 | 0 |
| pt-es | 27 | 0 | 0 | 0 | 0 |
| pt-fr | 28 | 0 | 0 | 0 | 0 |
| pt-it | 26 | 0 | 0 | 0 | 0 |
| pt-ja | 29 | 0 | 0 | 0 | 0 |
| pt-ko | 52 | 0 | 0 | 0 | 0 |
| pt-nl | 28 | 0 | 0 | 0 | 0 |
| pt-ru | 27 | 0 | 0 | 0 | 0 |
| pt-zh-tw | 24 | 0 | 0 | 0 | 0 |

Total: 288 KEEP, **0 REVERT, 0 lost hand patches** across all 10 editions. Every
diff is core-fix1 lines, the proof1 boxtitle shortenings, the whole-sentence keys,
the ko punctuation-mechanical lines (24), and the D5 gloss lines. (ja `svglib.py`
shows no diff: backup and rebuild carry the same kinsoku file.)

## 8. Mechanism fixes applied during this rebuild (apply_fixes.py, assertions passed)

1. D5 gloss key `冠军头衔` added to all 10 tables (values in §3; longest-match priority).
2. Newly found `墨底` key: a core-fix1 comment (content12.py:131, `# old bottom 2310;
   pt-es PIL ink run reaches 2342 (墨底 +33, …`) broke transform step 6's CJK-0 assertion
   for every Latin edition (the comment did not exist in the first round). A SEG key
   `墨底` was added to all 10 tables (de `Tintenunterkante`, en `ink bottom`, es
   `borde inferior de tinta`, fr `bas de l'encre`, it `base dell'inchiostro`, ja
   `インク下端`, ko `잉크 하단`, nl `inktonderkant`, ru `нижний край чернил`, zh-tw
   `墨底` identity). All 10 tables now hold 222 SEG keys.
3. Proof1 edition fixes listed in §6 (tables + FURN[fr] `sub330_size` 32→30).
4. ko punctuation in transform.py + textmd.py: `re.sub(r'：(?=\S)', ': ', t)` + `，→,`.
5. `verbatim` (textmd_extra, 9 languages; en untouched): de `(wörtlich aus dieser
   Ausgabe)`, es `(citadas palabra por palabra de este número)`, fr `(extraites mot
   pour mot de ce numéro)`, it `(citate parola per parola da questo numero)`, ja
   `（本号の記事から一字一句）`, ko `（이 호 기사에서 한 자 한 자）`, nl `(letterlijk uit
   dit nummer)`, ru `(дословно из этого номера)`, zh-tw `（逐字摘自本期文章）`.
   All 10 text.md files carry `(verbatim from this issue)` ×1 at line 433 before the
   replacement and the translated line after.
6. en fix1 values asserted through (D1 slogan, D2 `o título title`, D3 colon OVR).

Tool fixes during the rebuild:
- `gates_pt.py` / `classify_pt.py`: the edition slug for zh_tw must be hyphenated
  (`2026-w47-pt-zh-tw`, not `zh_tw`); the first zh_tw gates run hit the wrong path and
  was discarded and re-run after the fix (final run: all rc 0).
- `gloss_probe.py`: rect regex accepts `rx="0"` attributes; GLOSS detection uses the
  per-edition prefix (`Note |`, `해설 —`, `HINWEIS ·`, `Note —`, `Nota —`, `Uitleg —`,
  `Пояснение —`, `解説 —`, `譯注｜`); 'inside' requires x inside the box too.
- ru gates first run: `print_web_text_equal: false` and `keycheck_rc: 1` — both
  investigated and adjudicated pre-existing (§2), not re-run to hide them.

## 9. Core-inherited defects (all 10 editions, core is finalised — do not touch, record only)

- P1 EM POUCAS PALAVRAS box: last line `em Brasília. (Página 4)` overflows the box
  bottom by +17.6px.
- P3 schedule box: last line `16h30.` by +15.6px.
- P6 timeline box: last line `Página do Participante.` descenders by ~+5px.
- es D7 / P8 model text: 2–3 lines past the right frame edge by +2/+14px.
- de (b) P3/P5 descender note did not reproduce.

## 10. Out-of-scope observations (record only, do not fix)

- Other Latin editions' P8-note colons lack a space (fr verified `3 > 1:mais`); all
  proof1s left them unnamed — per the respective PROOF-NOTE.md, do not widen the fix.
- nl D4 marginal note: see §6 (ru O3 ruling applies if +0.5px recurs).
- ru keycheck / pdftotext deviations: pre-existing, adjudicated in §2.
- Tiny count note: word counts via check_final (fitz) differ by 2 from the independent
  recount during the ru investigation (8,095 vs 8,093) — a counting-method artifact,
  identical on both sides; the multiset diff is 0 in both methods.

## 11. Files in this directory

- `FANOUT-REPORT-pt.md` (this file), `backup-sha.txt` (old files, full SHA).
- `backup-old/` — the 10 first-round editions, full copies (293 MB).
- `build_edition.sh`, `gates_pt.py`, `classify_pt.py`, `gloss_probe.py`,
  `apply_fixes.py`, `transform.py`, `tables_*.py`, `furniture.py`, `make_gates.py`,
  `textmd.py`, `check_final.py`, `creambox.py`, `creambox_diag.py`, `boxtitle_core.py`,
  `keycheck_core.py`, `minfont.py`, `sweep_de.py`, `check_p8keys.py`.
- `<lang>-gates.json`, `<lang>-classify.json`, `<lang>-build.log`, `<lang>-*.log`,
  `<lang>-textdiff.json`, `<lang>-p8size.json` (fresh, this rebuild; the stale
  first-round files with the same names live in `scratch-fanout-pt/`).
- `visual/<lang>-contact.png` (all 8 pages) + change-point crops.
