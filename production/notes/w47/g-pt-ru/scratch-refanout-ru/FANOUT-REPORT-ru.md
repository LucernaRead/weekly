# ru re-fanout — FANOUT-REPORT-ru.md (2026-11-11)

Rebuilt all 10 reader-language editions of `2026-w47-ru-*` from finalized
core-ru (fix1 `f11854bf`), with the D1 map fix. **No commit, no push.**
Per-language records: `records/<lang>/RECORD.md` (artifacts, gates, logs).
Old editions backed up whole-dir (44 files each) to
`hidden_files/w47/scratch-refanout-ru/backup-old/`.

## Core (verified before the first build and after the last gate — unchanged)

| File | Bytes | SHA-256 |
|---|---|---|
| `core-ru/Lucerna-VOL4.pdf` (print) | 31,429,147 | `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81` |
| `core-ru/Lucerna-VOL4-web.pdf` (web) | 4,025,834 | `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197` |
| `core-ru/2026-w47-ru-core.text.md` | 60,953 | `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` |

Core = fix1 `f11854bf` (ancestor of repo HEAD). No core file modified; git
shows no tracked modification under `production/2026-w47/core-ru/`.

## Rebuilt editions — artifacts

| Lang | Print PDF bytes | Print SHA-256 | Web PDF bytes | Web SHA-256 | `.text.md` bytes | `.text.md` SHA-256 |
|---|---|---|---|---|---|---|
| en | 21,251,190 | `b244c56b7575f425e52902f19823f740d46cdafea2afcb1b86cdde24df863406` | 3,380,786 | `d306b3f365c5b4a04022f2a900faee904eb3f838c2f530fe5b4ce667c62d14a9` | 62,829 | `1e06ec55e8ba694224e244e37d81e6bfdfc3c3299e6aeb925308fd08e0b0e2ea` |
| de | 21,231,822 | `26bfbcd169594a07595083f36f7306568eb4387f122ab6f94507c52141eadad2` | 3,385,962 | `99173b8cacdde82a5d1147b54d61d254f16a59e9d8858f246c0acd3958bed4ee` | 63,516 | `5ae444c8724da5b8d0c07874c3f4ce2ffc8a6a6f6dd8504ec3b00f49a732a911` |
| fr | 21,291,969 | `8f09a2703081f12b76ace75331a79b5c4507282894b119298e68b7ce77c83562` | 3,385,758 | `45f6401dc1e20dfc12d596d4d31e49e4803f6a41c442d9e757940ef15d823929` | 63,543 | `7a402199542afaf125a8648fe7fd4bcc67766718e0e70b2351e35418b18522ec` |
| es | 21,278,615 | `64cb48f90dea70553a76e70c8cb9bc75ffa571c1ceaa8318c8655b47b80cf7c3` | 3,387,465 | `7af50086c326e1d5bcd78afa746663e3a0d1c5b5b35735a719a17006b694b051` | 64,215 | `a4044bf0b7570abb58eaf7c0e53c71870f7182c3b375991bdb6eac721502ef1b` |
| it | 21,265,865 | `c69b7bdf3165ed24f05be8004559e0102c0c8e38f15e395bc32360094628359b` | 3,384,095 | `91028029155a32dab67c77d4fa0d69e6373ce790730f296cfd3a29d46ae60afd` | 64,014 | `ac9636b971959d9f9c25e253aff6ff35f575512b5be70088240f365fb3ac10d1` |
| pt | 21,205,597 | `59f01012f5c64fdddb73e1b73a50b448e21b8d2c68f59b740b4927a6f1444cdd` | 3,383,529 | `485a27b6be196e7f7d95c3b2d2e218ba3969ebe8fe084668ec20eea4f7bcff70` | 65,155 | `54d8a766e18daf5f256e91c76765c9e71fefb48c9435e83d28e103bba603d60e` |
| nl | 21,315,805 | `8982ce29eaf2bc57661a089b9bf0bd8021444130e2e0c9aa505f9176de4a1e17` | 3,387,072 | `abc3ec69f695129c9e248dae36880da1754f6af5ef32b62f5438435458512593` | 64,053 | `96dc93598dec047b87a168c2332bc30b611b8a42250d22e65c7e1da2920ac694` |
| ja | 27,409,704 | `150f970828142d50cc10ba157182dd282c22dd74d82de5f7c932141d86cda0a3` | 3,721,635 | `57cf6b07ba4fc83404848cd43f2dc1c08304255ef94dae0e3ec359203bc7b67d` | 64,514 | `c17ff1877155c5155e55ea43eec43dee516d133ec456817bb7549c23d17ea840` |
| ko | 22,007,810 | `78e4442af8af9ec286c407ff66e08bac2029dd79d3ded43d1bfde3d555a6a400` | 3,513,230 | `3bf39ecf4fa4563458c68319ca42171642f9ad0be24650064faa9b7d9bd03195` | 65,069 | `d1feb40e417ba058d773a58ada62ad7fd7805b6a943599d8d017510b402d5a3d` |
| zh-tw | 24,784,766 | `2d19ad648194eeceeb03ddf9dd313326a51dd5f077ce9e9b0ae65753caeb42b4` | 3,995,314 | `991b22ab217eaf925aee4c444e71b9c423c5dfa09b6471a8de8459637671d52d` | 60,887 | `bc9c425f1c887d4ad70b7f2369671b3d36979b33d40713967977a4febd4a62c4` |

All 10: print + web PDFs 8 pages each; `.text.md` 150 exercises / 277 blocks;
`ABSTRACT.txt` restored from the backup (identical to the map meta abstract);
ja print 27,409,704 bytes with 72 distinct font xrefs (clean — the bad-merge
figure is ~6,485); web PDFs all < 7 MB, built with the patched `webpdf.py`
(commit `40963281`).

## D1 / D2 / D6 / kicker — per-language verification

Map route: surgical — old `map-<lang>.json` + 4 KEEP_AS_IS values from
`scratch-fix-ru-d1/build_map.py`. Verified byte-identical to the regenerated
`scratch-fix-ru-d1/maps/map-<lang>.json` for en/de/es/pt/ko/zh-tw; for fr/it/nl/ja
the surgical route additionally preserves the hand fixes that live only in the
old maps (fr 49, it 13, nl 3 × `’`→`'`; ja 3 wording fixes).
`rebuild-ru-zh-tw/` is validation-only, not a deliverable.

| Lang | D1 text.md L459 / L504 / L596 | D1 disclaimer SVG-only | D1 all 4 in SVG | D2 `День студента` | D2 full phrase ×2 | D6 `желании` ×2 in text.md | D6 p8 key 20 | Kicker min gap |
|---|---|---|---|---|---|---|---|---|
| en | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 5.9 px |
| de | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 5.9 px |
| fr | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 5.9 px |
| es | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 5.9 px |
| it | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 5.9 px |
| pt | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 5.9 px |
| nl | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 5.9 px |
| ja | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 5.9 px |
| ko | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 5.9 px |
| zh-tw | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 5.9 px |

Kicker gaps (all 10, PIL ink-box per SVG font family, INVEST-NOTE method 1):
`[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]` — exactly the INVEST-NOTE
Table 1 values, min 5.9 px ≥ 4. P1 kicker row identical to core in all 10.

`.text.md` diff old→new: exactly **6 line pairs** in 9 editions (L173 D6 key,
L187 D2 option, L459/L504/L596 D1 titles, L694 D6 key list) and nothing else;
**ko has 8** (the same 6 + L99 D1a + L538 D1b, see below).
Old→new text.md bytes: en 62,769→62,829; de 63,452→63,516; fr 63,489→63,543;
es 64,161→64,215; it 63,962→64,014; pt 65,098→65,155; nl 63,984→64,053;
ja 64,451→64,514; ko 65,002→65,069 (+67: D1/D2/D6 + D1a/D1b);
zh-tw 60,815→60,887.

## Gates summary (all 10 PASS)

| Gate | Result (all 10 unless noted) |
|---|---|
| `run.py` exit 0 / TOTAL 150 / 0 overflow | PASS |
| `check_core.py` exit 0, golden BAD 0, gloss fails 0 | PASS; orphans 1 (P7 y553 `”».`, known benign) except ja (4: + P7 `。`×2, `：`×1) and zh-tw (5: + P7 `。`×3, `：`×1) — same CJK class as core/ja; same-baseline collision 1 (P1 y1712 `чёрная`, same as core) |
| `p8.py extract` 150/150 + `compare` CLEAN | PASS; keydiff `[137, 138, 139, 140]`; direct keydiff vs core `ru-p8.json` identical |
| Occlusion audit | 42 TEXTX, 0 LINEX; adjudicated 42/42 CLEAR |
| Freeze baseline | 8/8 byte-identical |
| Freeze diff Cyrillic-bearing removed | 9 langs: exactly 15 = Q46 `можно` ×1 + 14 Morozko-caption words (image skipped by design); zh-tw: exactly 1 = `можно` (Morozko image PRESENT, no caption removed); unexplained 0 in all 10 |
| Print/web text layer | multiset identical overall and per page (en 30,363; de 31,009; fr 30,771; es 30,838; it 30,923; pt 31,107; nl 31,087; ja 26,630; ko 26,535; zh-tw 25,845 chars) |
| P8 min font (§1.1 `s11_check.py`) | 9.75 pt, FAILURES: none, all 10 |
| Creambox full 8-page scan | no negative inside-only clearance; BELOW-WINDOW 95 lines (8 langs) / 96 (ko, zh-tw — the extra +44.0 line is the P1 quick-quiz header pointer, see below); scan byte-identical to the first build's scan in 9 langs; ko differs in exactly 3 lines (the D1a fix, see below) |
| `apply_ru.py` | rc=1 Latin langs (only the known D6 fix-comment CJK in `content12.py:261`, comment-only, no unmapped literals); rc=0 ja/ko/zh-tw ("apply OK") |

Freeze diff totals (distinct / count-sum): en 484/850, de 486/851, fr 484/850,
es 484/848, it 482/848, pt 484/848, nl 487/854, ja 349/536, ko 361/529,
zh-tw 253/308. The totals vary by language (translation length); the
Cyrillic-bearing removed list is the invariant, and it is clean in all 10.

## Corrections found and fixed during this run

1. **ko D1a/D1b (proof1 DEFECTS, fixed — not deferred).** The ko map's `lit`
   bucket carried two translator typos that ko proof1 had already flagged as
   defects (PROOF-NOTE.md conclusion (b) — DEFECTS FOUND, CANNOT FINALIZE):
   - D1a (P2 gloss, `content12.py:172`): `родина` rendered as Cyrillic `роди`
     + Hangul 나 (U+B098) — `роди나`.
   - D1b (P7 B2 bridge, `content7.py:48`): `синоптики` rendered as Hangul 시
     (U+C2DC) + Cyrillic `ноптики`.
   Fix: corrected the 2 map values in `maps/map-ko.json` (same KEEP mechanism
   as the 4 D1 strings; pre-fix copy `maps/map-ko.json.bak-pre-d1ab`, diff =
   exactly those 2 lines); rebuilt ko whole. Verified: P7 y=660 single
   Cyrillic run `синоптики`, P2 y=382 `родина`, text.md L99/L538 clean, zero
   mixed-script tokens remain; ko freeze diff's Cyrillic list is now the
   standard 15. The ko creambox scan now differs from the first build's scan
   in exactly 3 lines (`-'роди' -'나' +'родина'`), everything else identical.
2. **zh-tw freeze reference number corrected (256 → 253).** The task brief's
   "removed 256" is the FIX-NOTE's number, computed when the core SVG still
   lacked the fix1 kicker double spaces. With the kicker landed in the
   edition (required by this same task), the 3 P1 kicker runs (`'  '` ×7,
   `',  '` ×1, `'—  '` ×1) are no longer removed: distinct 253 / count-sum 308.
   Decomposed the two freeze-diff JSONs — the ONLY delta is those 3 kicker
   strings; the Cyrillic conclusion (only Q46 `можно`) is identical. The gate
   assertion was updated to 253/308 with this note (`gate_lang.py`).
3. **Creambox classifier: P1 quick-quiz header row.** ko and zh-tw have 96
   BELOW-WINDOW lines (not 95): the extra line is the P1 quick-quiz header
   pointer (`1면을 읽고 정답을 고르세요　정답은 8면` / `…Answers on page 8`)
   at y=2348.0, below the brief-news box by design — the same element sits at
   y=2348.0 in en too (offset +37 there, +44 in ko/zh-tw because their
   brief-news boxes are shorter). The gate now classifies the y=2348.0 row
   (≤ +44) as by-design instead of failing it (`gate_lang.py`).
4. **Stale KIT numbers corrected.** Every KIT's "56,600–58,994 bytes / 203
   blocks" for `.text.md` was stale — the shipped files were already
   60,815–65,002 bytes / 277 blocks (re-running `ru_textmd.py` on the
   pre-refanout sources reproduces them byte-identically; verified for en and
   zh-tw explicitly, block-counted for all 10). KITs now carry the true
   numbers; en's §5 fix-1 note was corrected the same way.

## Gate-script bugs found and fixed during this run (all in `gate_lang.py`)

- D1 check searched whole KEEP values (with U+3000) in text.md, but the
  exporter renders ` · ` separators — now checks the Russian segments
  (L459/504/596) + SVG presence.
- Freeze-diff check summed counts and demanded Cyrillic == [`можно`] — now
  reports distinct + count-sum, with the allowance {`можно`} ∪ {core P8
  caption-zone (y≥2450) runs} when the Morozko image is absent; zh-tw
  distinct 253 is enforced (see correction 2).
- Kicker measurement used per-char advance accumulation (ignores kerning) and
  counted the attached comma as a word gap — now element-level whole-run
  `getbbox` (trailing spaces stripped: they inflate the right edge) with
  INVEST-NOTE tokenization (10 tokens, 9 gaps). The result now reproduces
  INVEST-NOTE Table 1 exactly.
- Creambox-vs-backup comparison added (normalized path diff); en's
  `gates.json` was patched with the same method retroactively (0 diff lines).

## KIT updates

Every edition's `WEEKLY-KIT.md` got §5 (new print/web SHA+bytes, re-fanout
build line, true text.md bytes/blocks) and a **Re-fanout (2026-11-11)** bullet
in the self-proofread record with the D1/D2/D6/kicker evidence and the gate
summary. The 9 Latin/CJK KITs share the layout (updated by `update_kit.py`);
zh-tw's table-style KIT was updated by hand (§1 table, §2 build chain, §3 gate
table, new §9). en's KIT additionally corrects the stale "map still has curly
quotes" claim (the map now carries the straight quotes for
`content56.py:12` directly; the fix1 comment is kept in the source) and the
stale fix-1 text.md numbers.

## Tools / scripts (in this workdir)

- `build_lang.py` — per lang: apply → restore ABSTRACT.txt + WEEKLY-KIT.md
  from backup-old → run.py → render.py → webpdf.py → ru_textmd.py → check_core.py.
- `gate_lang.py` — per lang: p8 extract/compare + direct keydiff vs core
  `ru-p8.json` → occlusion + adjudication → freeze baseline + diff →
  print/web text multiset → s11_check → creambox (+ vs-backup diff) → kicker
  PIL gaps → D1/D2/D6 checks. Writes `records/<lang>/gates.json`.
- `make_maps.py` — surgical maps (old map + 4 KEEP values).
- `fix_maps_ko.py` — the 2 ko D1a/D1b map corrections.
- `update_kit.py`, `record_lang.py` — KIT + RECORD generation from gates.json.

## Backup location

`hidden_files/w47/scratch-refanout-ru/backup-old/2026-w47-ru-{en,de,fr,es,it,pt,nl,ja,ko,zh-tw}/`
— whole-directory copies (44 files each) of the first-build editions, taken
before any rebuild. 407 MB total.

## Verdict

**All 10 editions rebuilt, re-gated, zero issues. Ready for independent
re-proofread** (ru-en's re-proofread is a separate assignment; the other 9
await their proofread rounds). No commit, no push performed.
