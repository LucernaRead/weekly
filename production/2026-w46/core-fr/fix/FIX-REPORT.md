# W46 FR-family fix report (Round 1 defects D1–D3) — local only, 2026-11-03

Worker: FR-family fix worker. No git, no inserts, no pushes, no Discord, no chat dumps.
Verdict fixed: `hidden_files/w46/fr-proofread-gates/proofreader-verdict-round1.md` (FAIL all 11, D1–D3 + flag F-MAIL).
F-MAIL was NOT touched: reader-letter disclosure wording verified still present in all 12 dirs (P7); mailbox verification remains the coordinator's pre-insert check.

## Source changes (all at source level; no rendered SVG/PDF hand-edits)

Build dirs: `hidden_files/weekly-report-w46-fr-build/` (core/zh-cn source) + `hidden_files/weekly-report-w46-fr-<native>-build/` for de/en/es/it/ja/ko/nl/pt/ru/zh-cn/zh-tw.
Content files were verified byte-identical across all 12 build dirs except the OUT path, so each fix was applied identically in all 12 copies. Scripts: `fr-fix/apply_fixes.py`, `fr-fix/shorten_d2.py`.

### D1 — all 11 editions + core (P3 item 37)
- `content34.py` (all 12 copies): key `La foire n'est plus à Paris.` → `La foire n'est pas à Paris.`; stem `(plus) La foire est à Paris. → ___` → `(pas) La foire est à Paris. → ___`.
- `expl.py` (all 12): `bridge_neg` lost ` / ne...plus` (now lists only `ne...jamais / ne...pas`); `n_neg3` set to each edition's own `n_neg2` `ne...pas` gloss (was `ne...plus` = no-longer). `ne...plus` occurred nowhere else in the family sources (verified by grep before editing), so no grammar column depended on it.
- Verified: no `n'est plus` / `(plus)` / `ne...plus` remains in any final SVG or `.text.md`.

### D2 — item 135, fr-it / fr-nl / fr-pt / fr-ru / fr-ja / fr-ko only (key unchanged)
- `expl.py` `stem_e1` in the 6 editions; the other 5 editions' accepted stems (de/en/es/zh-cn/zh-tw) untouched — verified still present.
- First attempt used longer déjà-faithful stems; all 6 pushed the P8 battery flow end from y=1502 to y=1552 and `occlusion_audit.py` flagged COVER on `Merci !` (71% covered by the writing-strip box; confirmed on the IT P8 card). Final single-line stems (same omission of déjà as the accepted EN/DE/ES stems), flow end back to y=1502, 0 flags:

| edition | old stem (wrong: "a programme explains France") | final stem |
|---|---|---|
| fr-it | `Un programma spiega la Francia.` | `Leggere un programma è capire la Francia.` |
| fr-nl | `Een programma legt Frankrijk uit.` | `Een programma lezen is Frankrijk kennen.` |
| fr-pt | `Um programa explica a França.` | `Ler um programa é compreender a França.` |
| fr-ru | `Программа объясняет Францию.` | `Читая программу, понимаешь Францию.` |
| fr-ja | `番組がフランスを説明する。` | `番組表を読むとフランスが分かる。` |
| fr-ko | `프로그램이 프랑스를 설명한다.` | `프로그램표를 읽으면 프랑스를 이해한다.` |

- NL needed a second shortening (`…Frankrijk begrijpen.` still wrapped → `…Frankrijk kennen.`, mirroring accepted DE `Frankreich kennen`).

### D3 — P4 `familier` gloss, fr-ja / fr-ko / fr-ru / fr-zh-tw only
- `expl.py` `bridge_treve`: JA `familier くだけた` → `familier なじみのある`; KO `familier 구어체` → `familier 친숙한`; RU `familier разговорное` → `familier знакомый`; ZH-TW `familier 口語` → `familier 熟悉的`. Correct editions (DE/EN/ES/IT/NL/PT/zh-cn) untouched.

## Re-render + finish (all 12 dirs)
- One-process driver per build dir (`import content12, content34, content56, content7, content8`), 150 exercises each, 0 FLOW OVERFLOW / HEAD TOO WIDE. Logs: `fr-fix/render-*.log`, `render2-*.log`, `render3-nl.log`.
- Finish (`fr-fix/finish_all.py`, sequential): 8 PNG cards + print PDF + web PDF (`tools/webpdf.py`) + `.text.md` regenerated from the source manuscript via `hidden_files/w46/text-export/export.py` (existing per-edition header preserved verbatim). ABSTRACT.txt untouched in all dirs (byte sizes identical to pre-fix; spot-checked core/de/ja still name Senate 9 Nov, Armistice 11 Nov, Dieppe fair 14–15 Nov, 150 exercises, A2–B2).
- Final numbers (print bytes / web bytes / pdftotext bytes print=web / `.text.md` bytes) — full log: `fr-fix/finish-all.log` + `fr-fix/finish-d2-round2.log`:
  - core: 23643162 / 2057423 / 46177 / 45506 · de: 9847768 / 1354604 / 46640 / 45812 · en: 9842783 / 1347395 / 45928 / 45250 · es: 9804515 / 1348845 / 46530 / 45769 · it: 9801621 / 1341501 / 46258 / 45503 · ja: 23705891 / 2107641 / 47153 / 46175 · ko: 15503892 / 1715537 / 46526 / 45689 · nl: 9805028 / 1346343 / 46302 / 45547 · pt: 9806086 / 1350380 / 46380 / 45570 · ru: 9808194 / 1393328 / 51372 / 50050 · zh-cn: 23643162 / 2057424 / 46177 / 45503 · zh-tw: 23654837 / 2400946 / 44997 / 44327. All web PDFs < 7 MB, all 8 pages, web text bytes = print text bytes.

## Gates re-run by the fix worker on FINAL artifacts (`fr-fix/gates-final/`)
- `freeze.py diff` vs core: PASS as adjudicated for all 11. P1–P7 removed strings contain CJK except punctuation-only `。` / `）。` (no French body text removed). P8 removed fragments are re-wrapped answer-key lines, settled by the p8 compare. Added CJK = 0 (de/en/es/it/nl/pt/ru); JA +2,281 / KO +2,460 = native explanation layers; ZH-TW +1,010 = traditional forms. fr-zh-cn: 0 differences on all 8 pages. Residue scans: 0 Han chars in Latin/RU/KO editions; ZH-TW simplified-only scan empty; JA Han list is standard shinjitai only.
- `p8.py compare`: CLEAN for all 11 — core and edition both 121 noted, missing=[], extra=0, uncertain=[], keydiff=[150] (zh-cn keydiff=[]). Identical to the proofreader's Round 1 result except the fixed key 37 now reads `pas`.
- `occlusion_audit.py`: 0 flags for core + all 11; selftest OK on every run. (The intermediate D2-overflow flags above were found and fixed during this work; final SVGs are clean.)
- Changed-page proofread by the worker: full SVG-text extraction of P3 (negation block + bridge + key 37) in all 12 dirs, P8 item 135 + dialogue in all 6 D2 editions, P4 gloss + surrounding paragraph in all 4 D3 editions; card visual check: P8 ×7 (6 D2 + EN control), P3 ×2 (core, RU), P4 ×4 (JA/KO/RU/ZH-TW). No new defect found.

## KITs
Fix record appended to all 12 `WEEKLY-KIT.md` (11 edition dirs + core dir): `files/weekly-report-w46-fr-*/WEEKLY-KIT.md`, section "补记：独立校对 Round 1 缺陷修复（2026-11-03…）", with defect/fix quotes, re-render numbers and re-gate evidence.

## Open item for coordinator (not this worker's scope)
- F-MAIL: mailbox verification before insert; replace the labelled editorial example/disclosure if real reader letters exist. Wording untouched and present in all editions.
- Round 2 independent proofread still required before shipping (SOP §8 loop rule).
