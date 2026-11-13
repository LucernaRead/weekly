# WEEKLY-KIT — Lucerna 日本語版 VOL.4, Italian-reader edition (W47, 16–22 Nov 2026)

Slug: `2026-w47-ja-it`. Target language: Japanese. Reader language:
Italian. Built by fan-out from the re-settled core `2026-w47-ja-zh-cn`
(core-ja, frozen; only the explanation layer was rewritten).

## §1 Specification — SOP §1.1 visual system

- 8 pages, 1950×2700, 4 columns. Paper `#fbfaf6`, ink `#302c28`,
  caption `#6f675d`, fine line `#d8d2c4`, book-green cloth `#37402f`,
  olive `#46581f`, goose-yellow `#f6e08e`, on-cloth `#f4efe1`.
  Level badges: A2 `#5c6e30`, B1 `#46581f`, B2 `#37402f`, white text.
  No gold, no brick-red, no near-black backgrounds; no double outer
  frame; no `·` separator anywhere (8/8 SVGs: `·` 0×, `#fbfaf6`
  1×/page, old `#f7f1e2` 0×).
- Masthead `Lucerna` (no article for Japanese; UnifrakturMaguntia
  196px = 147pt). P1 headline 56px = 42pt. Margins MX=88px = 66pt.
  Footer every page: `Lucerna　SETTIMANALE GIAPPONESE VOL.4　Testi
  in giapponese　Spiegazioni in italiano`, page line `Pagina N di 8`
  (Italian, per reader language). VOL.4 everywhere it is an issue
  number; VOL.5 appears 3× (P4 previous-issue note, P7 disclosure
  merged single mention, P7 next-issue teaser — same pattern as de).
- Exercises: 150 total, continuous numbering 1–150, registry-generated
  P8 answers. Measured: A2 48 · B1 73 · B2 29. By page:
  10/18/18/18/18/18/12/38. By type (registry): completamento 50 ·
  scelta multipla 51 · abbinamento 12 · costruzione di frasi 8 ·
  vero o falso 11 · cloze 13 · traduzione 4 · Scrittura 1. P8 model
  text 154 characters.
- Practice section heads stay in Japanese, frozen (A　理解,
  B　ことば, C　数字と日付, C　文を作りましょう,
  D　ペアにしましょう, D　正しい・正しくない, B　グラフ,
  C　数字と事実, D　文を完成しましょう, B　一般問題,
  スポーツ　体育); exercise-type labels are Italian (Completa,
  scelta multipla, cloze, Abbinare, Costruisci una frase,
  Vero o falso?, Traduci, Scrittura). `match_set` instruction is
  `Abbinare`.
- `りくりゅう`: romaji `rikuryuu` in the P7 gloss and P8 answers.
  `ちいかわ`: `Chiikawa` (never the Chinese name 吉伊卡哇).
- Trend-box source line (P1): `Fonti e date negli articoli`
  (fits the 400px box, one line). P7 disclosure (readers' corner)
  is Italian, 5 lines: "Esempio della redazione, non una lettera
  vera. Entro la scadenza non sono arrivate lettere né i migliori
  testi di pagina 8; entrambi usciranno nel VOL.5. Mandaci la tua
  lettera in giapponese!" No real letters were fabricated; nothing
  was fetched from any mailbox.

## §2 Lead and page contents

Same as the core (frozen Japanese text, facts, dates, pictures).
P1 lead: Ni-no-tori + Beaujolais Nouveau release, Thu 19 Nov.
P2 life (Tori-no-ichi + kumade). P3 culture (Beaujolais + stalls).
P4 sport (sumo Kyushu basho days 1–3, champion undecided, final
result promised in VOL.5). P5 youth (30 buzzword nominees +
Arashiyama photo). P6 deep read (foliage moving to Kyoto + labelled
practice-data chart, 38/24/22/16 = 100%). P7 language focus
(A2/B1/B2 columns + error clinic ×4 + frame 「福をかき込む」 +
readers' corner + 8 golden phrases + VOL.5 teaser). P8 assessment
+ writing + all keys.

## §3 Trend sources

Unchanged from the core — see `core-ja/WEEKLY-KIT.md` §3 (sumo
day 1–3 results, Tori-no-ichi, Weathernews foliage forecast,
Beaujolais Nouveau 19 Nov, buzzword nominees 5 Nov, calendar).
No new research was done for the fan-out; no fact was changed.

## §4 Promises honoured

Same as the core (KIT §4): sumo final in VOL.5, buzzword top 10 +
grand prize 1 Dec, readers' letters + best P8 writing carried
forward (disclosure re-printed in Italian), foliage continuation.

## §5 Golden phrases

The core's 8 phrases, verbatim Japanese + Italian glosses on P7
(Italian glosses translated from the core's Chinese glosses; the
Japanese sentences are byte-identical to the core).

## §6 Images

Same five PD/CC0 images as the core (P1 maple, P3 beaujolais,
P5 Arashiyama pond, P7 tori 2025, P8 Arashiyama temple). Credits
in `assets/CREDITS.md` (copied from the core). Italian captions
are the translated map values (e.g. `Foto: Poliphilo — CC0
(Wikimedia Commons)`).

## §7 Proofread record (builder self-check, this edition)

- Full text read: `2026-w47-ja-it.text.md` (1378 lines) +
  all 8 card PNGs visually checked. No overflow, overlap, footer
  strike or tofu found in the final artifacts.
- Simplified-Chinese residue scan over the text dump and the SVGs:
  0 hits (`吉伊卡哇` 0×, `参考答案` 0×, `酉之市` 0×, `提名` 0×).
  `ryuuryuu` / `Chiikawa` as specified.
- 150 keys re-verified key-by-key against the core extract:
  only [137, 138, 139, 140] differ — the E-group translation
  answers, translated JA→IT as ruled: 137 `Ni-no-tori è il
  19 novembre.`, 138 `Il vino nuovo esce il 19 novembre.`,
  139 `Le nomination delle parole di moda sono state annunciate
  il 5 novembre.`, 140 `Chi va a vedere le foglie dovrebbe
  controllare le date previste e la situazione attuale.` All
  other 146 keys byte-identical to the core.
- P7 teaser ends 2528.1 (footer 2580, 52px clear); P7 col3 ends
  1754.1. P8 exercise flow ends col 3 y=561 (bottom 1252); P8-keys
  flow ends col 3 y=2442 (bottom 2540, 98px slack). Fix-1 re-verified
  identical (runA/runB logs): same end positions, zero overflow.

## §7a Fix-1 re-verification (builder, 2026-11-11)

- 150 P8 answer notes re-read in full from the rebuilt text.md;
  all keys byte-identical to the pre-fix `p8.py` extract (keys
  untouched); only the 6 note strings in §11 F4 changed.
  Full text.md old-vs-new diff = exactly those 6 lines.
- Person-name romaji re-checked one by one in the notes:
  Ōnosato, Hōshōryū, Yoshinofuji, Chura-no-umi, Fujiryōga,
  Miura Riku, Kihara Ryuichi, Miyajima, Shōsetsu, ryuuryuu,
  Chiikawa — all correct, no further same-class residue.
  Long-vowel (macron) convention: this edition already writes
  `Hōshōryū` / `Ōnosato` / `Shōsetsu` with macrons for long
  vowels; `Fujiryōga` (りょう = ryō) follows exactly the same
  convention. `Chura-no-umi` takes the hyphenated form used by
  the fr/es/pt editions (en uses `Churanōmi`, de uses
  `Churanoumi` — each edition's own choice, not adopted here).

- Fix round 2 (2026-11-12, new standing gates `boxtitle_check.py`/`spill_sweep.py`, commit 45ca73fc): 2 boxtitle defect(s) — P1 `数字で見る今週　La settimana in cifre` +8.5px; P7 `今週のフレーム　Struttura della settimana` +68.5px (worst of the nine) — fixed by layout only, no words changed (see §11 F5). P7 col3 ends 1781.1, teaser ends 2541.1 (footer 2580); P8-keys flow ends col 3 y=2442 (bottom 2540).
## §8 Gates (all recorded in scratch-fanout-ja/)

- run.py exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE
  (`build-it-run2.log`; run1 had 2 P8-keys overflows + P7 teaser
  over the footer, fixed — see §11; run3 is the identical re-run
  for the freeze check).
- Occlusion audit: `tools/occlusion_audit.py` — 0 flags
  (`it-occlusion.json`; selftest OK, all 6 classes fired on
  planted controls, clean controls silent).
- P8 extract: `tools/p8.py extract --total 150` — noted set 150/150
  (`it-p8.json`).
- P8 compare: `tools/p8.py compare` vs the core — status CLEAN,
  missing=[] extra_count=0 uncertain=[], keydiff=[137, 138, 139, 140]
  (`it-p8compare.json`).
- Freeze: direct sha256 of the 8 SVGs, two consecutive builds
  (fix-1 runA vs runB, same `tools/venv/bin/python`) — 8/8
  byte-identical; pre-fix vs post-fix SVG diff = only
  `p8-tesuto.svg`. Fix-1 gate files live in
  `hidden_files/w47/scratch-ja-it-fix1/` under the goals dir
  (see §11 F4); the `it-*.json` / `build-it-run*.log` files
  named in the original §8 were already absent at first-round
  proof (proof O1) and were re-run from scratch for fix-1.
- Web PDF: `tools/webpdf.py` — `Lucerna-VOL4-JA-IT-web.pdf`,
  4,381,291 bytes (< 7 MB), 46,922 text bytes, text
  byte-identical to the print PDF.
  Print PDF: `Lucerna-VOL4-JA-IT.pdf`, 25,807,665 bytes, 8 pages.
  Print sha256:
  `e44a8fcba1ba429a2ad6c463cca8f4e33559d1a65139e46fa27d367f4242cf6c`.
  Web sha256:
  `3cb1e9559b3a6e7763858cbaeae56eee9a61e54a083e8ade9c5c950e513a62fb`.
  (Fix-1 rebuild, 2026-11-11; pre-fix values were print 29,099,162 /
  `75986cd7…200fd`, web 4,476,984 / `b3ea6d18…353f0`, 47,000 text
  bytes — see §11 F4.)
- Text: `2026-w47-ja-it.text.md`, 46,692 bytes, 1378 lines,
  exported from the final SVGs (`export-textmd-it.py`).
- P8 minimum font size: 9.975pt (answers, 13.3 SVG px; PyMuPDF
  measurement of print PDF p.8; next size 10.35pt = exercises).
  P8 stems stay at 13.8px / 10.35pt per the core (Round 6 rollback).
- §1.1 grep audit on the final SVGs: paper `#fbfaf6` 1×/page,
  old `#f7f1e2` 0×, banned colours 0×, `·` 0×, badges A2 `#5c6e30`
  / B1 `#46581f` / B2 `#37402f`, masthead 196px on P1, page line
  `Pagina N di 8` 1×/page, VOL.4 as the issue number.

### Fix round 2 re-gates (2026-11-12; logs in `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-gatefix-ja-koit/`)

- `boxtitle_check.py` on the fixed edition: 0 DEFECT / 0 OBSERVE (was 2 DEFECT); `spill_sweep.py`: 0 SPILL. No new defects vs the 130-wide aggregate baseline for this edition.
- `run.py` twice (fix1 run+render, fix2 run-only; `tools/venv/bin/python`): both exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE; TOTAL 150 (A2 48 / B1 73 / B2 29; by page 10/18/18/18/18/18/12/38; types unchanged). P1-headline flow ends col 2 y=921 (bottom 1828, unchanged).
- Freeze: fix1 vs fix2 SVG sha256 — 8/8 byte-identical. SVG diff vs pre-fix build: p1 + p7 only (p2–p6, p8 byte-identical).
- Occlusion audit: 0 flags (selftest OK, all 6 classes fired); 0 NEW vs core.
- P8 extract 150/150; compare vs core CLEAN, keydiff still exactly [137, 138, 139, 140].
- Print PDF `Lucerna-VOL4-JA-IT.pdf`: 29,099,202 bytes, sha256 `58c74118ae3f79beab02458c9bb1d459048b88567b75dfc6b8b232cba79ec10f`.
- Web PDF `Lucerna-VOL4-JA-IT-web.pdf`: 4,477,024 bytes (< 7 MB), sha256 `ff47d54a9af1bd5dfa449eb4a2e4b8c3304d49466c18d8d1715256572f725431`, 47,004 text bytes.
- Text layers: `pdftotext -layout` print vs web byte-identical (106,305 bytes each, `cmp` clean); plain `pdftotext` likewise identical.
- Visual check of the fixed titles on the render cards (crops in the scratch dir): two-line titles sit inside their cream boxes with clean spacing; no overflow, overlap, or footer intrusion.

### D5 rebuild (2026-11-12; evidence in `hidden_files/w47/scratch-d5-ja/ja-it/`)

- Production svglib.py replaced verbatim with the ja D5 template (`svglib-ja-d5.py`, `_D5_READER = "latin"`, 0 lines diff vs template); old svglib md5 `b8bca01f…`, new `abfd29ed…`. U+201C fix2 routing preserved; quotes census 0 defective.
- Production census before → after: Latin 407 → 0, Cyrillic 0, curly-in-CJK 0 (RC=0).
- Gates (all green): `run.py` TOTAL 150, 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; `head_check.py` PASS; occlusion 0 flags; p8 extract 150/150, compare vs core-ja CLEAN, keydiff=[137, 138, 139, 140]; freeze baseline 8/8 byte-identical; freeze diff vs base added CJK 2 (all U+3000); spill 0; boxtitle 36 titles, 502 body lines, 0 DEFECT; edge 0 TOUCH / 0 NEAR; creambox PASS 0 defects (n=381 median 1.012 boldT 1.040 boldF 0.998; P8 238→242 lines, slack 60.0→60.0 px); text layers print/web/delivered multiset-identical (27,380 chars vs delivered 27,462 raw).
- Print PDF `Lucerna-VOL4-JA-IT.pdf`: 25,807,650 bytes, sha256 `4e47887337909b20c89db2be0925e711bdc9b57422f856479e64ecc6a55f4974`.
- Web PDF `Lucerna-VOL4-JA-IT-web.pdf`: 4,381,274 bytes, sha256 `0a97c94a09c28ca8ae765012e57b827badaef0401b748964b92588d71691074f`.
- text.md unchanged (46,678 bytes, sha `71a2d7d2…`); synced to production and re-verified there (freeze baseline 8/8, census 0, quotes 0).

### Fix round — D1 romaji fix (2026-11-12; independent reproof PROOF-NOTE.md)

- D1 (all 11 ja editions): `りくりゅう` romaji `ryuuryuu` → `rikuryuu` (5× per edition: P7 gloss + P8 answers 66/77/80/105). Sources: `content7.py` (2×) + `content56.py` (3×). Japanese core text `りくりゅう` untouched; answer letters untouched.
- Changed SVGs vs pre-fix: p7-kotoba.svg, p8-tesuto.svg; unchanged: p1-hyoushi.svg, p2-kurashi.svg, p3-bunka.svg, p4-supotsu.svg, p5-wakamono.svg, p6-fukayomi.svg.
- Print PDF `Lucerna-VOL4-JA-IT.pdf`: 25,807,661 bytes, sha256 `1bfe0610763411cd1172e61c8b3a3a1e0afce0dc081789cf815cab2bb0ad87b6`.
- Web PDF `Lucerna-VOL4-JA-IT-web.pdf`: 4,381,297 bytes, sha256 `db031afe2252b7e40b2bc00819f35f4708004cf3c7b4364e51125a2e00dca3fe`.
- Text `2026-w47-ja-it.text.md`: 46,678 bytes, sha256 `9b677d40100d2c9dfbde67932f6e46113a56ac7cea87ded22a674957a24f02b8` (surgical replacement, exactly 5 lines changed, each only by the fix substitution).
- Full re-gates (all green):
  - run.py: P8 saved, TOTAL exercises: 150
  - head_check: HEAD CHECK PASS 0 defects
  - D5 census: CENSUS PASS
  - quotes: GRAND TOTAL defective: 0
  - occlusion: /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-it/2026-w47-ja-it/svg: 0 flags 
  - p8 extract:   set: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
  - p8 compare: status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140] {'status': 'CLEAN', 'total': 150, 'how': 'lines', 'ref_how': 'lines', 'core_count': 150, 'edition_count': 150, 'core_set': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 4
  - freeze baseline: core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
  - freeze diff vs pre-fix base: p8: +4 strings / -4 strings; CJK core 1422 -> edition 1422; added CJK chars: 0 ; added Latin strings: 4 (unexpected 4) | TOTAL added CJK characters: 0 | TOTAL added Latin strings: 5 (unexpected 5)
  - spill: SPILL_SWEEP 2026-w47-ja-it: 35 boxes, 83 candidates, 0 SPILL, 83 OBSERVE
  - boxtitle: BOXTITLE 2026-w47-ja-it: 36 titles, 502 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal
  - edge: EDGE_SCAN 2026-w47-ja-it: 8 pages, 0 TOUCH, 0 NEAR
  - creambox: CREAMBOX PASS 0 defects
  - text layer: print-vs-web multiset diff: +0 -0 IDENTICAL
  - PDF text: /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-it/2026-w47-ja-it/Lucerna-VOL4-JA-IT.pdf ryuuryuu: 0; /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-it/2026-w47-ja-it/Lucerna-VOL4-JA-IT.pdf rikuryuu: 5; /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-it/2026-w47-ja-it/Lucerna-VOL4-JA-IT-web.pdf ryuuryuu: 0; /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-it/2026-w47-ja-it/Lucerna-VOL4-JA-IT-web.pdf rikuryuu: 5; 
- Post-sync verification on the production dir: freeze baseline 8/8, D5 census PASS, quotes census 0; production svg/text.md `ryuuryuu` 0×, `rikuryuu` 5×.
  Evidence in `hidden_files/w47/scratch-fix-ja/ja-it/` (fix log + gate logs + JSONs).

### Fix round 3 — L4 holiday-name wording (2026-11-12; third independent reproof PROOF-NOTE-3.md)

- L4 (ja-it): P8 answer 132 `月よう日は、どうして学校が休みですか。` — `Lunedì niente scuola: Festa del ringraziamento` → `Lunedì niente scuola: Festa del ringraziamento per il lavoro`. The short form is the Italian name for the US Thanksgiving and is confusable with Japan’s 勤労感謝の日 (same defect class as fix round 2 L2 in ja-es); the full form matches answer 20 in the same edition. Source: `content8.py:57`.
- Untouched on purpose: answer 20 `23 nov. (lun.): ringraziamento per il lavoro` (`content12.py:263`) already used the literal form. §11 F1’s quoted #132 note (`Lunedì niente scuola: Festa del ringraziamento`) is kept verbatim as history, as with the Fujiryōga quote in F4. Answer letters / keys untouched.
- Changed SVGs vs pre-fix: p8-tesuto.svg; unchanged: p1-hyoushi.svg, p2-kurashi.svg, p3-bunka.svg, p4-supotsu.svg, p5-wakamono.svg, p6-fukayomi.svg, p7-kotoba.svg.
- Print PDF `Lucerna-VOL4-JA-IT.pdf`: 25,807,665 bytes, sha256 `e44a8fcba1ba429a2ad6c463cca8f4e33559d1a65139e46fa27d367f4242cf6c`.
- Web PDF `Lucerna-VOL4-JA-IT-web.pdf`: 4,381,291 bytes, sha256 `3cb1e9559b3a6e7763858cbaeae56eee9a61e54a083e8ade9c5c950e513a62fb`.
- Text `2026-w47-ja-it.text.md`: 46,692 bytes, sha256 `91224d88a55d5dc7ae8c3411e62d4199fe32d4028293223ba5373bd3a21125aa` (re-exported from the patched SVGs + fragmented lines restored verbatim, exactly 1 line(s) changed, each only by the fix substitution; see FIX-LOG-3.md for the re-export verification).
- Full re-gates (all green):
  - run.py: P8 saved, TOTAL exercises: 150
  - head_check: HEAD CHECK PASS 0 defects
  - D5 census: CENSUS PASS
  - quotes: GRAND TOTAL defective: 0
  - occlusion: /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix3-w47-ja/ja-it/2026-w47-ja-it/svg: 0 flags 
  - p8 extract:   set: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
  - p8 compare: status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140] {'status': 'CLEAN', 'total': 150, 'how': 'lines', 'ref_how': 'lines', 'core_count': 150, 'edition_count': 150, 'core_set': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 4
  - freeze baseline: core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
  - freeze diff vs pre-fix base: p8: +1 strings / -1 strings; CJK core 1422 -> edition 1422; added CJK chars: 0 ; added Latin strings: 1 (unexpected 1) | TOTAL added CJK characters: 0 | TOTAL added Latin strings: 1 (unexpected 1)
  - spill: SPILL_SWEEP 2026-w47-ja-it: 35 boxes, 83 candidates, 0 SPILL, 83 OBSERVE
  - boxtitle: BOXTITLE 2026-w47-ja-it: 36 titles, 502 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal
  - edge: EDGE_SCAN 2026-w47-ja-it: 8 pages, 0 TOUCH, 0 NEAR
  - creambox: CREAMBOX PASS 0 defects
  - text layer: print-vs-web multiset diff: +0 -0 IDENTICAL
  - text layer bytes: BYTE-IDENTICAL print-vs-web pdftotext (46936 vs 46936 bytes)
  - pages: PAGES+SIZE OK
  - P8 min fontsize: P8 min fontsize: 9.975pt
  - U+201C/U+201D: U+201C/U+201D census: 0
  - final check: FINAL-CHECK OK ja-it
  - PDF text: /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix3-w47-ja/ja-it/2026-w47-ja-it/Lucerna-VOL4-JA-IT.pdf full-form occurrences: 1; /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix3-w47-ja/ja-it/2026-w47-ja-it/Lucerna-VOL4-JA-IT.pdf short-string occurrences: 1; /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix3-w47-ja/ja-it/2026-w47-ja-it/Lucerna-VOL4-JA-IT-web.pdf full-form occurrences: 1; /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix3-w47-ja/ja-it/2026-w47-ja-it/Lucerna-VOL4-JA-IT-web.pdf short-string occurrences: 1; 
- Post-sync verification on the production dir: freeze baseline 8/8, D5 census PASS, quotes census 0; production text.md `Festa del ringraziamento` only as the full form, 1× (L1355); `ringraziamento per il lavoro` 2× (answer 20 + Q132).
  Evidence in `hidden_files/w47/scratch-fix3-w47-ja/ja-it/` (fix log + gate logs + JSONs).

## §9 Reproduction

Build dir:
`production/2026-w47/fanout-ja/2026-w47-ja-it/` (copied from
`core-ja/` by `scratch-fanout-ja/apply.py it`, map
`scratch-fanout-ja/map-it.json`, 221 map keys + 6 instr + meta).
`tools/venv/bin/python run.py`, then `render.py` (cards PNG +
print PDF), then `tools/webpdf.py svg Lucerna-VOL4-JA-IT-web.pdf`,
then `export-textmd-it.py`. Never run a build module standalone;
never import a content module inside a build dir. Scratch (logs,
probes, gate JSONs, maps) lives in
`hidden_files/w47/scratch-fanout-ja/`.

## §10 VOL.5 promises registered

Same as the core (KIT §10).

## §11 Fix record — fan-out fixes (builder, 2026-11-11)

- F1 (P8-keys overflow, run1): keys flow ended col 3 y=2585
  (bottom 2540), 2 FLOW OVERFLOW lines; simulation
  (`probe-p8sim.py it`) listed 19 two-line entries. Fix (SOP §1.1
  step 2, notes only — keys untouched): shortened 11 distinct
  answer notes in `map-it.json` (verified one line each with
  `svglib.wrap()` before editing: #20 `23 nov. (lun.):
  ringraziamento per il lavoro`, #54/#111 `Kinboshi di
  Fujiryūga: 11° torneo dal debutto` (this quoted note itself
  carried the D1 misspelling — corrected to `Fujiryōga` in F4
  below; the quote is kept verbatim as history), #60 `Hōshōryū
  torna dopo
  tre tornei di assenza`, #68 `Top 10 e gran premio: 1°
  dicembre`, #73 `Foglie di Arashiyama al culmine ~23 nov.`,
  #83 `Foglie di Miyajima al culmine ~21 nov.`, #85/#127
  `Foglie di Arashiyama cadono ~12 dic.`, #86 `Previsione meteo
  giapponese: Arashiyama 13 nov.`, #87/#126 `Previsioni diverse:
  definizioni del culmine`, #94 `Foglie del monte Takao al
  culmine ~13 nov.`, #132 `Lunedì niente scuola: Festa del
  ringraziamento`), plus the `writing_note` meta (`Testo modello
  in sezione H (154 caratteri)`). 15 entries affected
  (20, 54, 60, 68, 73, 83, 85, 86, 87, 94, 111, 126, 127, 132,
  150). Result: keys flow ends y=2442, zero overflow. E-keys
  #139/#140 stay two lines (keys themselves untouched, as in fr).
  #39 stays two lines (long Japanese stem, as in de).
- F2 (P7 teaser over the footer, run1): teaser ended 2583.62
  (footer 2580). Root cause: the Italian disclosure wrapped to
  6 lines and the clinic notes one line longer than en. Fix:
  disclosure shortened to 5 lines (191 chars, wrap-verified:
  6→5 lines; single VOL.5 mention, as in de). Result: teaser
  ends 2528.1.
- F3 (render race, no content impact): the first `render.py`
  invocation was executed twice by the runtime (two processes
  8 s apart writing the same PDF); the merged print PDF came
  out 108,387,170 bytes with 37,537 xrefs (en: 197) — same 8
  pages and images, but bloated. The duplicate was killed, the
  bloated PDF deleted, and `render.py` re-run once cleanly
  (`render-it2.log`): 29,099,162 bytes. Lesson recorded: never
  run two renders into one edition dir; check `ps` before
  re-running render.
- Map accounting: `map-it.json` 221 map keys + 6 instr + meta;
  same 221-key set as map-en (verified key-for-key identical).

- Fix round (2026-11-12, D1 romaji fix; see §8 fix subsection for gates + SHAs): D1 `ryuuryuu` → `rikuryuu` in `content7.py` + `content56.py` (5×, P7 gloss + P8 answers 66/77/80/105). Full rebuild + re-gates; print/web/text.md re-synced with new SHAs recorded in §8.

- Fix round 3 (2026-11-12, L4 holiday-name wording; see §8 fix subsection for gates + SHAs): P8 answer 132 `Lunedì niente scuola: Festa del ringraziamento` → `Lunedì niente scuola: Festa del ringraziamento per il lavoro` in `content8.py:57` (short form is the US Thanksgiving name; answer 20 already used the literal form). §11 F1's quoted #132 note kept verbatim as history. Full rebuild + re-gates; print/web/text.md re-synced with new SHAs recorded in §8.

## §11a Fix record — fix round 1 (builder, 2026-11-11)

- F4 (D1/D2, first-round proof defect — the round-1 (a) is void;
  a second full proof round must follow). P8 answer notes
  misspelled two sumo wrestlers' romaji — `Umi-no-umi` (key 48)
  and `Fujiryūga` (keys 49, 54, 63, 111, 116). Found by the
  ja-es fix-1 builder's cross-edition grep; round-1 proof had
  missed this class (its note list records the names only as
  `Fujiryūga`/`Hōshōryū` without checking the readings).
  Readings verified independently against public sources before
  editing: 藤凌駕 = ふじりょうが (Fujiryōga) — ozumo.jp
  «藤凌駕は「ふじりょうが まさはる」と読む» (citing the Japan
  Sumo Association official profile); Nikkan Sports 2025-10-01
  «藤凌駕（ふじりょうが、22＝藤島）»; 美ノ海 = ちゅらのうみ
  (Chura-no-umi) — Nikkan Sports 2018-05-30
  «美ノ海（ちゅらのうみ）»; ibid. «木崎改め美ノ海
  （ちゅらのうみ、25＝木瀬）».
  Fix: 6 note strings in the sources only —
  `content34.py:188` (key 48) `Umi-no-umi …` →
  `Chura-no-umi ha perso contro Hōshōryū il giorno 1`;
  `:190` (49) `Fujiryūga ha battuto …` → `Fujiryōga …`;
  `:202` (54) `Kinboshi di Fujiryūga: …` →
  `Kinboshi di Fujiryōga: 11° torneo dal debutto`;
  `:224` (63) `Fujiryūga ha vinto un kinboshi il giorno 3` →
  `Fujiryōga …`; `content7.py:57` (111) same kinboshi note →
  `Fujiryōga …`; `content8.py:22` (116)
  `Hōshōryū ha perso contro Fujiryūga il giorno 3` →
  `… contro Fujiryōga …`. Answer keys (B/A/11/○) untouched;
  question stems (kanji 藤凌駕 / 美ノ海) untouched.
  Pre-fix full-edition grep: `Fujiryūga` 5× + `Umi-no-umi` 1×
  in .py sources, text.md and the P8 SVG (all 6 = the 6 notes,
  no residue elsewhere); post-fix: wrong spellings 0× in .py +
  SVG text nodes + text.md (the only remaining `Fujiryūga`
  strings are the quoted old forms inside this KIT's fix
  records (§11 F1/F4, kept as history with the old→new
  mapping)); correct `Fujiryōga` 5× +
  `Chura-no-umi` 1× per layer (py / SVG / text.md).
  Whole issue rebuilt (runA/runB, render, webpdf) + full gate
  suite re-run, all green (see §8 and §7a); P8 notes old-vs-new
  diff = exactly those 6 lines; the only SVG that changed
  pre-→post-fix is `p8-tesuto.svg`.
  Upstream note (NOT fixed here — out of scope, core-ja is
  read-only for this task): the same two misspellings sit in
  `production/2026-w47/core-ja/WEEKLY-KIT.md` §3 lines 83–88
  (`Umi-no-umi` 1×, `Fujiryūga` 4×) — the likeliest source the
  fan-out builders copied. No shared romaji table file exists
  (no map-*.json at all in `hidden_files/w47/scratch-fanout-ja/`
  — the O1 gap stands), so the defect lives in each edition's
  own note strings + the core KIT narrative. Other editions NOT
  touched, state report only: de/en/es/fr/pt already fixed
  (en `Churanōmi`, de `Churanoumi`, fr/es/pt `Chura-no-umi`);
  ja-nl still carries `Fujiryūga` 5× + `Umi-no-umi` 1× in its
  .py sources. Also new in this fix: `export-textmd-it.py`
  created in the edition dir (modelled on en's — the original
  was absent); validated byte-identical reproduction of the
  pre-fix text.md from the pre-fix SVGs before the fix.
  Fix-1 logs: `hidden_files/w47/scratch-ja-it-fix1/` under the
  goals dir (FIX-LOG.md, GATE-LOG.md, build/render/webpdf
  logs, gate JSONs, pre/post SHA lists).
  Incident during the fix (no content impact): the first
  `webpdf.py` run exited rc=120 mid font-subsetting and the
  text.md export then failed with disk-quota-exceeded (EDQUOT;
  df showed 45 GB free) while other agents rendered in
  parallel; deleting my own 33 MB pre-fix PDF snapshots from
  the fix-1 scratch dir restored writability (their bytes/SHA
  are recorded here and in FIX-LOG.md), and webpdf re-ran clean
  with an isolated TMPDIR (`/tmp/webpdf-it-fix1`, rc=0).

- F5 (fix round 2, 2026-11-12 — new standing gates, 130-wide run 2026-11-12 01:54 UTC). Defects: P1 `数字で見る今週　La settimana in cifre` +8.5px; P7 `今週のフレーム　Struttura della settimana` +68.5px (worst of the nine). Shared cause (all 9 ja boxtitle defects): `Flow.box` and the P7 col-3 box titles render the bilingual `JP　gloss` title as ONE 23pt line in a 422.5px box whose inner width is 386.5px; the core's short Chinese gloss (386.5px exactly) fits, but the DE/ES/FR/IT/NL glosses run 405–469px. P1 numbers box: `Flow.box` in `bslib4.py` now splits an over-wide bilingual title onto two lines (JP title 23pt / gloss 19pt) only when the single line exceeds the inner width; P7 frame box: title split the same way in `content7.py` (box +27px, `fy` gap 44→30 so the teaser keeps 38.9px clear of the footer). No words added, removed, or substituted — layout only — so no re-proof was needed and `text.md` is untouched (its title strings are word-identical; a future re-export would render them on two lines). P7 slack was the binding constraint (teaser 22.9–25.4px from the footer in de/es/fr/nl): the +27px frame box is offset by reclaiming 14px from the col-3→phrases gap (`fy = max(1712, col3_end + 30)`), net +13px; fr's clinic (only +9.5px) was shrunk to 21pt instead of a second two-line box, which would have needed +54px. Verified: re-run gates 0/0, freeze 8/8, p8/occlusion clean (see §8b); production files re-gated after sync (boxtitle 0 DEFECT, spill 0 SPILL).
