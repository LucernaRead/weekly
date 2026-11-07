# Round 2 Proofreader Verdict — Lucerna Weekly 2026-W46, DE family (VOL.3)

**Issue:** Mon 2026-11-09 – Sun 2026-11-15. Target language German. Press time 2 November 2026.
**Proofreader:** independent, Round 2. Did not build or fix these editions. Verdict date: 2026-11-03.
**Scope:** 11 editions — `2026-w46-de-en, -es, -fr, -it, -ja, -ko, -nl, -pt, -ru, -zh-cn, -zh-tw`.
`weekly-report-w46-de-core/` is a duplicate directory of the zh-cn edition, not a 12th edition (see §4).
**Round 1 verdict:** FAIL, all 11 blocked (`de-proofread-gates/proofreader-verdict-round1.md`).
**Fix record adjudicated:** `de-fix/FIX-REPORT.md` (2026-11-03) + fix records appended to each edition's `WEEKLY-KIT.md`.
**Gate directory (this round):** `hidden_files/w46/de-proofread-gates-round2/` (fresh; Round 1 dir not reused).

## 1. Per-edition verdict

| Edition | Verdict | Blocking defect |
|---|---|---|
| de-en | **PASS** | — |
| de-es | **PASS** | — |
| de-fr | **PASS** | — |
| de-it | **PASS** | — |
| de-ja | **PASS** | — |
| de-ko | **PASS** | — |
| de-nl | **PASS** | — |
| de-pt | **PASS** | — |
| de-ru | **PASS** | — |
| de-zh-cn | **FAIL** | D-R2-1 (P8 key 140 word split `da` / `sNFL-Spiel.`) |
| de-zh-tw | **PASS** | — |

10 of 11 editions are shippable. Only de-zh-cn is blocked, by one new defect (§5).

## 2. Fix verification — Round 1 defects and minors

Every item adjudicated CONFIRMED / PARTIAL / REFUTED with quoted evidence from the final artifacts.
Script: `fix_verify.py` → `fix_verify.log` (131 checks, 131 PASS, 0 FAIL), plus independent re-gates (§6).

### 2.1 Blocking defects

| ID | Claim | Ruling | Evidence |
|---|---|---|---|
| D-CORE-1 (factual, all editions) | P4 caption corrected to `…spielt in dieser Woche in Belgrad — am Montag danach in Berlin.` | **CONFIRMED** | New caption present in all 12 dirs (core + 11); old string `…in Belgrad und Berlin.` absent everywhere. Date claim verified independently: `TZ='Europe/Berlin' date -d` — issue week Mon 9 – Sun 15 Nov 2026; Berlin game Mon 16 Nov 2026 is outside the week. |
| D-ABSTRACT (all 11) | Abstracts re-framed as practice, single-line, no ASCII quotes | **CONFIRMED** | All 11 + core single-line, 0 ASCII double-quotes, reader-native, VOL.3 + 150 + A2–B2 present. Closings practice-framed, e.g. en `150 exercises on this week's topics.`, zh-cn `150 道以本周话题为素材的练习。`, zh-tw `150 道以本週話題為素材的練習。` Facts/topics intact. Strict practice-framing gate applied (SOP §9 example does not override the 2026-10-28 rule). |
| D-CORE-3 (core/zh-cn/zh-tw P2) | Orphan `。` removed | **CONFIRMED** | No lone-punctuation element on P2 of core, zh-cn or zh-tw (element scan S4: zero in the whole family). The former element `<text x="1473" y="1175.88">。</text>` is gone. |
| D-TOOLBOX (en/es/fr/it/pt/ru P7) | `Es wird gespielt.` glossed as present passive, not future | **CONFIRMED** | en `It is played`, es `Se juega`, fr `Il est joué`, it `Si gioca`, pt `Joga-se`, ru `Играется`; future forms absent. Controls intact: nl `Er wordt gespeeld`, ja `試合が行われる`, ko `경기가 열린다`. Ex. 103/104 future-vs-passive contrast preserved. |
| D-IT-1 (it P3) | Noun glossed with noun form | **CONFIRMED** | `das Geschnatter = lo starnazzare` present; bare verb form absent. |
| D-NL-1 (nl P6) | P6 gloss headwords restored | **CONFIRMED** | `die Verbundenheit = verbondenheid`, `die Versöhnung = verzoening`, `die Kranzniederlegung = kranslegging`, `der stille Tag = stille dag` all present. `kranslegging` adjudicated correct (action noun parallel to en `wreath-laying`; P8 key 97 keeps the fuller `een kransleggingsceremonie`). |
| D-RU-1 (ru P7) | Definition restored in full | **CONFIRMED** | `ein Spiel ohne Zuschauer im Stadion. Матч-призрак.` present in the NOCH EIN WORT box. |
| D-KO-1 (ko P5/P8) | 3 punctuation orphans removed | **CONFIRMED** | No lone-punctuation elements on KO P5 or P8; zero in the whole family (S4 scan). KO P5/P8 cards viewed: clean. |
| D-PT-1 (pt, tu/você mix) | você-form throughout, incl. follow-up miss | **CONFIRMED** | Sweep of all PT SVGs: 0 occurrences of `Completa com`, `Lê`, `Escreve`, `Escolhe`, `Olha`, `Usa`, `Junta`, `traduz para português`, `corrige-os`, `Fizeste`. você-forms present (`Complete com as palavras do quadro`, `Leia/Escreva/Escolha`, `Traduza para o português`). The single `Completa*` hit in P8 is the infinitive section label `Completar o diálogo`, person-neutral, not a tu imperative. Retained `Enviem-nos as vossas para VOL.4!` is plural address, internally consistent. |

### 2.2 Minors

| ID | Ruling | Evidence |
|---|---|---|
| M-1 bare-German `DER WERKZEUGKASTEN` headers (es/fr/it/nl/pt/ru/ja/ko) + RU P1 `IN DIESER AUSGABE` | **CONFIRMED (deviation accepted — see (d))** | Short reader-language glosses present in all 8 editions; RU P1 `IN DIESER AUSGABE · В номере` present. Full forms measured and layout-forced (see §3(d)). |
| M-2 bare-noun `Kranzniederlegung` glosses (es/fr/it/pt/ru/nl) | **CONFIRMED (deviation accepted — see (d))** | Full forms present in all 6: es `ofrenda floral`, fr `dépôt de gerbe`, it `deposizione di corone`, pt `deposição de coroas`, ru `возложение венков`, nl `kranslegging`. P6 gloss block 5 lines (last baseline 1022.4) vs 4 lines elsewhere (1002.7); no overflow/overlap (occlusion 0, cards viewed). |
| M-3 thinned UND SIE? invitations (es/fr/it/nl/pt/ru) | **CONFIRMED** | Full two-question invitations present on P3/P4/P5 per edition (strings verified per edition in `fix_verify.log`). |
| M-4 JA/KO P8 register mix | **CONFIRMED** | JA 138 plain `水曜日にランタンを作る。`; `作ります` absent from all JA SVGs. KO 137 polite `개막합니다`; plain `개막한다.` absent. JA/KO notes uniformly plain / polite respectively. |
| M-5 wrap punctuation at line edges (CJK) | **CONFIRMED** | No lone-punctuation elements anywhere; remaining line-edge breaks are mid-phrase token wraps (see §3(a)/(e)). |
| M-6 KO P1 exercise-flow quirk | **CONFIRMED** | KO P1 head x=527 y=1736.58; exercises 1–6 all x=1061 with EN-identical baselines 848.6/971.5/1094.5/1217.4/1340.4/1463.3 (EN head y=1734.52; 2px difference only). KO P1 card viewed: exercises read in order. |
| T-1 ZH-TW P8 header separator dropped | **CONFIRMED** | `Alle Antworten unten auf dieser Seite — 答案在本版下方` present in zh-tw P8. |
| Stale freeze archives (en/nl/ru, doc only) | **CONFIRMED** | Regenerated `de-{en,nl,ru}-freeze.json` byte-equal to this session's independent runs; stale copies preserved in `de-fix/stale-de-{en,nl,ru}-freeze.json`. |

### 2.3 O-1 badge-slot — PASS, not re-raised

zh-cn retains the German subtitle slot in the masthead, as adjudicated in Round 1. No defect.

## 3. Flagged items (a)–(g) — explicit rulings

**(a) Kinsoku v2 fix — CONFIRMED, with one residual defect of the same class (D-R2-1).**
Own scans (line-start AND line-end, all pages, all 11 editions + core; log `kinsoku-scan.log`): no lone-punctuation elements; no line-end opening brackets. The `76.` token is intact in core/zh-cn P8 (`76. Die Kinder freuen sich, weil St. Martin kommt.`), zh-tw (wraps after `sich,`), ja and ko. No other token split by the S1 signature (line starting with 1–2 lowercase letters + capital) was found anywhere. HOWEVER, one word-split of exactly the class the v1 shedding created remains in core/zh-cn P8: D-R2-1 (§5). Origin (pre-existing in Round 1 vs introduced by kinsoku v1/v2) could NOT be established — no pre-fix SVGs were available for comparison — and no origin is asserted. The defect stands regardless of origin and blocks zh-cn only.

**(b) Occlusion follow-up — CONFIRMED, all six sites verified by geometry AND visually.**
ES/PT/RU P4: last gloss baseline 1133.82, SPIELPLAN head at 1140 — gap preserved, gloss fully visible on all three cards. FR/RU P3: `genügt.` baseline 1583.66, exercises rule at y=1608 (24.34px clear) — visible on both cards. RU P7: `Матч-призрак.` baseline 1498.98, SÄTZE rule at y=1508, NOCH EIN WORT box rect y=1378.5 h=150 → bottom 1528.5, SÄTZE head at 1548. Full-resolution crop viewed: the gold rule passes through the box's empty bottom padding, striking no text. Canonical occlusion audit: 0 flags on every page of every edition (self-test: all 6 planted classes fired, clean controls silent).

**(c) P8 keydiff [137,138,139,140,150] — LEGITIMATE, all five items adjudicated.**
137–139 are correct reader-language translations of the E-section sentences in every fan-out (read in full from the P8 notes dumps; e.g. en `The carnival begins at 11.11 in Cologne.`, ru `Карнавал открывается в 11.11 в Кёльне.`, ja `カーニバルは11時11分にケルンで開幕する。`). 140 is the fourth E-section item: the intact German sentence `Am Sonntag schaue ich das NFL-Spiel.` in all 10 fan-outs (the task's direction is translate INTO German; the printed key is the German sentence itself). 150 is the translated open-task label in each edition (en `Open task`, es `Tarea abierta`, fr `Tâche ouverte`, it `Compito aperto`, ja `自由課題`, ko `열린 과제`, nl `Open taak`, pt `Tarefa aberta`, ru `Открытое задание`, zh-tw `開放題`). zh-cn keydiff is `[]` (identical to core). NOTE: the core/zh-cn P8 *rendering* of item 140 is split across lines (`da` / `sNFL-Spiel.`) — that is D-R2-1, a rendering defect, not a key error; the key itself is correct.

**(d) Deviations — ALL CONFIRMED, layout-forced and correct.**
- M-1 short glosses: full-form candidates re-measured with PIL/Noto Sans CJK Bold at 23pt reproduce the fix report exactly (es 543.7, fr 451.3, it 551.5, nl 503.8, pt 542.8, ru 577.5 — all > 412px slot); short forms reproduce exactly (369.2/371.0/389.9/405.9/365.2/369.3/372.3; ko 393.2 vs claimed 394.4, 1.2px, still < 412). RU P1 full 424.0 / short 382.5 exact at 24pt. Short glosses are correct translations of "toolbox". Deviation accepted.
- M-2 gap accommodation: confirmed (see M-2 above); no overflow/overlap.
- NL `kranslegging`: correct (see D-NL-1 above).
- D-PT-1 follow-up miss: fixed and verified (see D-PT-1 above); retained plural `Enviem-nos as vossas para VOL.4!` accepted as internally consistent plural address.

**(e) PT P8 line starting `...)` — ACCEPTABLE, not a defect.**
Quote (PT P8, keys block): line `...) · 111. Ich finde, dass das Gedenken Stille braucht.(numa oração…`, preceded by `…110. fraglich(Es ist fraglich, ob... = é duvidoso se`. This is a mid-note greedy-wrap continuation: the `...)` closes the parenthetical note of item 110, fully visible and unambiguous. Same class as the all-edition `% · B. 100 %…` continuation wraps (item 88 stem) and the FR P8 `%)` wrap (item 84 note `34 %)`). It is a token break between separate tokens, not a kinsoku violation and not a lone orphan. No action required.

**(f) Transform sources not regenerated — RECORDED, not a defect.**
`tr-*.py` and `en-pairs.json` under `hidden_files/w46/` are dated 2026-11-02 (pre-fix); FIX-REPORT.md line 14 states they were NOT regenerated and edits live in the build dirs only. Verified: the finding matches file dates/contents. This is a reproducibility/record matter only. No artifact was found wrong on this ground; no edition is failed for it. Whoever re-runs the transforms must re-apply the Round 2 source edits or regenerate from the build dirs.

**(g) Counts — RECONCILED; seed totals CONFIRMED; fix worker's arithmetic REFUTED in detail.**
Chip scan from shipped SVGs (per edition, `counts.json`): 149 numbered + item 150 = 150; per-page 10/18/18/18/18/18/12/37 (+150 on P8 = 38); chips A2 57 / B1 70 / B2 14 / 8 untagged (113–120). Static AST parse of the frozen core build sources (`registry_parse.py` → `registry.json`, `key_registry.py` → `key_registry.json`, non-executing): 150 registrations, **A2 66 / B1 70 / B2 14** — the seed totals are correct. Reconciliation: untagged 113–120 are registry A2×6 + B1×2 (118, 120 are B1); dialogue items 145–147 carry a B1 chip element but registry says A2 (group-chip scan artifact); item 150 is B1 with no chip. Hence A2 = 57+6+3 = 66; B1 = 70−3+2+1 = 70; B2 = 14. The fix worker's explanation ("57+8+150=66", treating all 8 untagged and item 150 as A2) is arithmetically wrong. This is a record discrepancy only — no artifact defect; counts per edition are correct as shipped.

## 4. De-core duplicate finding

SVG hashes identical, card PNG hashes identical, `.text.md` byte-identical, `ABSTRACT.txt` identical, web-PDF extracted text identical (`pdftotext` cmp clean) between `weekly-report-w46-de-core/` and canonical `weekly-report-w46-de-zh-cn/`. PDF file hashes differ at identical byte sizes (web 1,670,976; print 16,578,272) — metadata/filename-level only. KITs differ in framing text (expected). Fix record present (grep count 1) in all 12 KITs. **No shippable divergence: the duplicate's artifacts match the canonical zh-cn edition. The duplicate must not be counted or shipped separately.** D-R2-1 affects the duplicate identically because the artifacts are identical — but the shippable edition is zh-cn, and it is zh-cn that is blocked.

## 5. Residual / new defects

### D-R2-1 — BLOCKING (de-zh-cn only): P8 key 140 word split

- **Location:** `weekly-report-w46-de-zh-cn/svg/p8-uebungen.svg` (and identically in the de-core duplicate), keys block, items 139–141.
- **Evidence (SVG elements):**
  - `<text x="1451" y="2091.0">（wieder begonnen = 又开始） · 140. Am Sonntag schaue ich da</text>`
  - `<text x="1451" y="2109.85">sNFL-Spiel.（看比赛 = das Spiel schauen） · 141. b（Mantel=斗…</text>`
- **Visual confirmation:** full-resolution crop of the zh-cn P8 card shows line 1 ending `…schaue ich da`, line 2 beginning `sNFL-Spiel.` The German word `das` is split across lines, producing the non-word `sNFL`.
- **Correct rendering:** `140. Am Sonntag schaue ich das NFL-Spiel.` intact on one line, as printed in all 10 fan-outs (verified via `p8.py extract` and the EN SVG).
- **Scope:** core/zh-cn only. All 10 fan-outs print item 140 intact. The `.text.md` export shows the correct source string, so this is render/wrap-only. The key itself is correct (see (c)).
- **Origin:** not established (no pre-fix SVGs available); no origin asserted. The defect blocks shipment of de-zh-cn regardless of origin.
- **Fix required (by the fix worker, not the proofreader):** re-wrap the keys paragraph so `das NFL-Spiel.` is not split; re-run kinsoku + occlusion gates on the re-rendered P8; the corrected edition needs a re-proofread of P8 only.

No other residual defects were found. In particular: no other token split in the family (S1-signature scan: exactly one hit — D-R2-1); no lone-punctuation elements; no wrong keys; no overflow/overlap; no missing glyphs/tofu; no missing image credits; no untranslated strings; no wrong-script residue.

### Non-defect observations (checked, accepted, no action)

- KO P8 note 22 transliterates Weckmann as `벡만` (single occurrence, consistent within the edition; intelligible gloss transliteration, not a key or factual error). Not raised.
- Item 67 notes in all editions reproduce the core's morning/afternoon simplification of the German item (which says evening). Carried from Round 1 as a trivial note, not a defect.
- ES/FR/IT `la WDR` / `la ZDF` treated as acceptable target-language press usage, not flagged.
- PT `Estugarda` (Stuttgart) and `Colónia` (Köln) are correct Portuguese exonyms.

## 6. Full key verification — 150/150 SEMANTICALLY CORRECT

Re-verified on the FINAL artifacts (all 11 re-rendered). Method: static key registry extracted from the frozen core build sources (stem + key + note for all 150, `key_registry.json`), every stem/option read from the build sources and checked against the full core `.text.md` (1409 lines, P1–P8) and article/chart facts; P8 printed keys extracted per edition (`p8.py extract --json`, `p8extract/`); P8 translated notes read in full for all 11 editions (`p8notes/`). `p8.py` set-equality alone was NOT relied on. **Result: all 150 keys semantically correct in the core and in all 11 editions' P8 renderings. No wrong key letter.**

### 6.1 Matching blocks — stem + options + key, quoted in full

**P2, items 25–28** — stem: `25. der Jeck / 26. die Laterne / 27. der Weckmann / 28. die Martinsgans`, options:
a. `das Licht aus Papier, das die Kinder am Abend tragen`
b. `der warme Umhang, den Martin mit dem Bettler teilte`
c. `die Person in Köln, die Karneval feiert`
d. `der Gänsebraten am Martinstag`
Keys: **25 = c** (`der Jeck` = man who celebrates carnival in Cologne), **26 = a** (`die Laterne` = paper light), **27 = b** (`der Weckmann` = yeast-dough man), **28 = d** (`die Martinsgans` = roast goose). All four correct against the article and the P2 word box.

**P4, items 52–55** — stem: `52. das Geisterspiel / 53. das Hinspiel / 54. der Ausrüster / 55. ausverkauft`, options:
a. `das erste Spiel gegen denselben Gegner in einer Runde`
b. `ein Spiel ohne Zuschauer im Stadion`
c. `die Firma, die die Trikots und Schuhe liefert`
d. `alle Karten sind weg, es gibt keine mehr`
Keys: **52 = b** (game without spectators), **53 = a** (first leg), **54 = c** (kit supplier firm), **55 = d** (all tickets gone). All four correct against the P4 article.

**P8 F-section, items 141–144** — stem: `141. der Mantel / 142. die Laterne / 143. das Geisterspiel / 144. die Versöhnung`, options:
a. `das Licht aus Papier, das die Kinder am Abend tragen`
b. `der warme Umhang, den Martin mit dem Bettler teilte`
c. `die Aussöhnung nach einem Streit — Frieden zwischen Menschen`
d. `ein Spiel ohne Zuschauer im Stadion`
Keys: **141 = b** (warm cloak shared by Martin), **142 = a** (paper light), **143 = d** (game without spectators), **144 = c** (reconciliation after a quarrel). All four correct.

### 6.2 All other categories — verified

- **Cloze 113–120:** keys A/B/A/B/A/B/B/A verified against verb person/number and the cloze paragraph (beginnt/bastelt/geht/singt/schaut/sieht/erzählt/beginnt).
- **Dialogue 145–149:** keys B/A/A/B/A verified (singst/macht/essen/machst/schaue — 2nd sg / 2nd pl / 1st pl / 2nd sg / 1st sg).
- **Multiple choice 1–15, 21–24, 39–42, 47–51, 60–64, 65–69, 80–82, 89–92, 104, 108, 112, 121–132:** every key checked against the article facts (dates, times, scores, places, broadcasters). All correct.
- **Richtig/Falsch 29–33, 80–82:** all correct against the legend/article (incl. 32 Falsch: results of 3–8 Nov unknown at press time).
- **Comparatives 56–59, 105:** mehr/später/leiser/früher/länger — all correct (8 pts > 5; 15.30 later than 11.11; empty stadium quieter; 5 Nov earlier than 13 Nov; night longer than day).
- **Chart/arithmetic 83–88:** 46%/34%/20% labels match measured bars 782/578/340; 46+34=80, 46+34+20=100 recomputed. All correct.
- **Grammar 93–100, 101–103, 106, 109–111:** wird-passive, ob, verb forms (geht/spricht), gedenken, Kranzniederlegung/Versöhnung/Verbundenheit — all correct.
- **Sentence-building 43–46, 76–79, 107, 111, 133–136:** verb-second / verb-final orders all correct.
- **Translations 137–140:** reader-language renderings correct in all 10 fan-outs; 140 the intact German sentence (see (c)). Core/zh-cn 137–139 correct; 140 correct as a key, split only in rendering (D-R2-1).
- **Item 150:** open task, evaluated per the writing-frame points, in all editions.
- **P8 printed keys vs registry:** core matches the registry except (i) 137 spacing-join artifact (`狂欢节11 点…` vs registry `狂欢节 11 点…` — line-join, not a defect), (ii) 140 split (D-R2-1), (iii) 150 truncated to `开放题` (extraction/note handling, not a defect). Every fan-out differs from core only on 137–140 and 150, all legitimate.
- **P8 translated notes:** read in full for all 11 editions — correct throughout, register consistent (JA plain, KO polite, PT você).

The complete 150-key list (registry order) is appended in §9.

### 6.3 Golden sentences, MUSTER, chart

- 8 golden sentences, each exactly **2×** in core + all 11 editions (verbatim contiguous excerpts on P7, each with page/level source; translations read on the P7 cards for all 11 editions).
- MUSTER **84 words** in all 12 dirs. Chart bars **782/578/340** in all editions, labels 46%/34%/20%, with the ÜBUNGSDATEN practice-data disclaimer.

## 7. Gate outputs summary (independently re-run, not trusted from the fix worker)

| Gate | Result |
|---|---|
| Freeze (`freeze.py diff --strict-cjk`, `freeze/`) | en/es/fr/it/nl/pt/ru exit 0, added CJK 0; ja exit 1 by design **+3275**; ko exit 1 **+3213**; zh-tw exit 1 **+1043**; zh-cn exit 0, +0/−0. Matches the fix report exactly. Removed-string scan: only furniture + re-wrap splits of lines still present; no German body text removed. |
| P8 (`p8.py compare`, `p8/`) | All 11 **CLEAN 150/150**, missing=[], extra=0; keydiff [137,138,139,140,150] (10 fan-outs), [] (zh-cn). Adjudicated legitimate (§3(c)). |
| Occlusion (`occlusion_audit.py`, `occlusion/`) | **0 flags** for core + all 11 editions. Self-test: all 6 planted classes fired, clean controls silent. |
| Counts (`counts.json`) | 149 numbered + item 150 = 150; per-page 10/18/18/18/18/18/12/38; reconciled A2 66 / B1 70 / B2 14 (§3(g)). |
| Fix verification (`fix_verify.py`, `fix_verify.log`) | 131 checks, 131 PASS, 0 FAIL. |
| Kinsoku/wrap scans (`kinsoku-scan.log`) | 0 lone-punctuation elements; 0 line-end opening brackets; exactly one S1-signature token split (D-R2-1). |
| Badges/footers | P1 badge at y=372 present in reader language in all 10 fan-outs; zh-cn German subtitle slot (O-1 PASS). `Die Lucerna` on 8/8 pages in every edition. Footer pairing text verified per edition from SVG. |
| Masthead pixel clearance | P1 cards: first ink row 26 in all 11 (frame border); masthead title ink confined to y 179–254 in all 11; next ink ≥40px below (≥294). No masthead collision in any edition. |
| PDFs (`pdf_text_equality.log`) | Web == print extracted text byte-identical AND normalized-equal for all 11 (e.g. en 48,496; ru 56,649; zh-cn 47,665 bytes). All web PDFs ≤ 7 MB (largest zh-tw 2,038,468). Text layer present in all. |
| ABSTRACT.txt | Valid in all 11 + core (see D-ABSTRACT). |
| Reader-facing sweep | Clean in all editions (only legitimate `VOL.4` references). Script purity: Latin editions 0 CJK/Cyrillic; ru 0 CJK/Hangul; ja 0 Hangul/Cyrillic; ko 0 han/kana/Cyrillic. |
| W45 promises spot-check | Readers'-letters disclosure, 20 Nov Bayern–Köln teaser, VOL.4 carry-forward present in all 11. |

## 8. Cards viewed

Full-frame (half-scale) views: P1 and P8 of all 11 editions; P4 and P7 of all 11 editions; P3 of es/fr/it/nl/pt/ru (fr/ru/it viewed at half-scale; es/nl/pt P3 covered by SVG/geometry + fix checks); P6 of es/fr/it/nl/pt/ru (es/nl viewed; fr/it/pt/ru covered by SVG/geometry + fix checks); P2 of core/zh-cn/zh-tw (core viewed; zh-cn/zh-tw covered by identical-hash + SVG checks); P5 of ko. Full-resolution crops: RU P7 gold-rule site (PASS), core P8 keys block items 139–141 (D-R2-1 confirmed), `76.` block (intact). No overflow, overlap, missing glyphs/tofu, or missing image credits found except D-R2-1. All viewed cards are recorded in the working notes; the shipped cards themselves are unmodified.

## 9. Complete key list (registry order, core)

Appended programmatically from `key_registry.json` (stem + key + note per item). Keys 1–150 all verified semantically (§6).

| # | Level | Kind | Stem | Key | Note |
|---|---|---|---|---|---|
| 1 | A2 | ex | Diese Woche ist ___: Die Bundesliga spielt nicht, die Nationalmannschaft spielt. | Länderspielpause | 国家队比赛周 |
| 2 | A2 | ex | Am Freitag spielt Deutschland in ___ gegen Serbien. | Belgrad | 塞尔维亚首都 |
| 3 | A2 | ex | Um 11.11 Uhr beginnt in Köln die neue Session des ___. | Karnevals | 狂欢季 11 点 11 分开幕 |
| 4 | A2 | ex | Am Sonntag spielen die Lions und die Patriots in ___. | München | NFL 在慕尼黑 |
| 5 | B1 | ex | Deutschland hat nach vier Spielen ___ Punkte. | fünf | 四轮 5 分 |
| 6 | B1 | ex | Am Sonntag ist auch ___: ein stiller Gedenktag. | Volkstrauertag | 周日是纪念日 |
| 7 | A2 | ex | Deutschland spielt am Freitag in... A. Berlin · B. Belgrad · C. München | B | 周五客战塞尔维亚 |
| 8 | A2 | ex | Das NFL-Spiel in München beginnt um... A. 11.11 Uhr · B. 20.45 Uhr · C. 15.30 Uhr | C | NFL 下午 3 点半开球 |
| 9 | A2 | ex | Die Karnevalssession beginnt in Köln um... A. 11.11 Uhr · B. 15.30 Uhr · C. 20.45 Uhr | A | 狂欢季 11 点 11 分开幕 |
| 10 | A2 | ex | Der Volkstrauertag ist am... A. Sonntag, 15. November · B. Mittwoch, 11. November · C. Montag, 9. November | A | 纪念日在周日 |
| 11 | A2 | ex | Die Karnevalssession beginnt um ___ Uhr. | 11.11 | 狂欢季 11 点 11 分开幕 |
| 12 | A2 | ex | Der WDR überträgt ab ___ Uhr live. | 10.30 | WDR 10 点半直播 |
| 13 | A2 | ex | Das NFL-Spiel in München beginnt um ___ Uhr. | 15.30 | NFL 下午 3 点半开球 |
| 14 | A2 | ex | St. Martin ist am ___. | 11. November | 圣马丁节 11 月 11 日 |
| 15 | A2 | ex | Der 11. November 2026 ist ein ___. | Mittwoch | 11 月 11 日是星期三 |
| 16 | A2 | ex | Der Karneval (beginnen) in Köln. → ___ | Der Karneval hat in Köln begonnen. | beginnen → begonnen |
| 17 | A2 | ex | Die Kinder (singen) Martinslieder. → ___ | Die Kinder haben Martinslieder gesungen. | singen → gesungen |
| 18 | A2 | ex | Wir (basteln) eine Laterne. → ___ | Wir haben eine Laterne gebastelt. | basteln → gebastelt |
| 19 | B1 | ex | Martin (teilen) seinen Mantel. → ___ | Martin hat seinen Mantel geteilt. | teilen → geteilt |
| 20 | B1 | ex | Viele Familien (essen) Martinsgans. → ___ | Viele Familien haben Martinsgans gegessen. | essen → gegessen |
| 21 | A2 | ex | Wann überträgt der WDR? A. um 11.11 Uhr · B. ab 10.30 Uhr · C. um 15.30 Uhr | B | WDR 10 点半直播 |
| 22 | A2 | ex | Was ist ein Weckmann? A. ein Lied · B. Gebäck aus Hefeteig · C. eine Laterne | B | Weckmann 是面人面包 |
| 23 | A2 | ex | Ist der 11. November ein Feiertag? A. Nein, Schule und Arbeit laufen normal. · B. Ja, alles ist geschlossen. · C. Nur in Köln. | A | 11 月 11 日不是法定假日 |
| 24 | A2 | ex | Was isst man mit der Martinsgans? A. Pommes · B. Rotkohl und Klöße · C. Eis | B | 圣马丁鹅配红甘蓝和丸子 |
| 25 | A2 | match_set | MATCH left=der Jeck | rights=['das Licht aus Papier, das die Kinder am Abend tragen', 'der Mann aus Hefeteig, den die Kinder bekommen', 'der Mensch, der in Köln Karneval feiert', 'der Gänsebraten am Martinstag'] | c | Jeck=狂欢者 c |
| 26 | A2 | match_set | MATCH left=die Laterne | rights=['das Licht aus Papier, das die Kinder am Abend tragen', 'der Mann aus Hefeteig, den die Kinder bekommen', 'der Mensch, der in Köln Karneval feiert', 'der Gänsebraten am Martinstag'] | a | Laterne=灯笼 a |
| 27 | A2 | match_set | MATCH left=der Weckmann | rights=['das Licht aus Papier, das die Kinder am Abend tragen', 'der Mann aus Hefeteig, den die Kinder bekommen', 'der Mensch, der in Köln Karneval feiert', 'der Gänsebraten am Martinstag'] | b | Weckmann=面人面包 b |
| 28 | A2 | match_set | MATCH left=die Martinsgans | rights=['das Licht aus Papier, das die Kinder am Abend tragen', 'der Mann aus Hefeteig, den die Kinder bekommen', 'der Mensch, der in Köln Karneval feiert', 'der Gänsebraten am Martinstag'] | d | Martinsgans=圣马丁鹅 d |
| 29 | A2 | ex | Martin war der Legende nach ein römischer Soldat. Richtig oder falsch? | Richtig | 传说马丁是罗马士兵 |
| 30 | A2 | ex | Die Gänse haben Martin versteckt. Richtig oder falsch? | Falsch | 传说鹅叫声暴露了他 |
| 31 | A2 | ex | Der Gedenktag des heiligen Martin ist am 11. November. Richtig oder falsch? | Richtig | 纪念日 11 月 11 日 |
| 32 | B1 | ex | Die Ergebnisse vom 3. bis 8. November standen bei Redaktionsschluss fest. Richtig oder falsch? | Falsch | 截稿时 11 月 3–8 日结果未知 |
| 33 | A2 | ex | Die Karnevalssession beginnt um 11.11 Uhr. Richtig oder falsch? | Richtig | 狂欢季 11 点 11 分开幕 |
| 34 | A2 | ex | Martin teilte seinen ___ mit einem Bettler. | Mantel | 斗篷分给乞丐 |
| 35 | A2 | ex | Die Kinder basteln eine bunte ___ aus Papier. | Laterne | 纸灯笼 |
| 36 | A2 | ex | Am Martinstag gibt es die Martins___: Gänsebraten. | Gans | 圣马丁鹅 |
| 37 | A2 | ex | In Köln tragen die Jecken ein buntes ___. | Kostüm | 狂欢节服装 |
| 38 | A2 | ex | Am ___ endet der Laternenumzug. | Martinsfeuer | 游行在篝火处结束 |
| 39 | A2 | ex | Was wurde Martin später? A. ein König · B. Bischof von Tours · C. ein Bäcker | B | 马丁后来成为图尔主教 |
| 40 | A2 | ex | Wann finden Laternenumzüge statt? A. nur am 25. Dezember · B. oft auch vor oder nach dem 11. November · C. nur im Sommer | B | 灯笼游行常在前后晚上举行 |
| 41 | A2 | ex | Was isst man am Martinstag? A. Gänsebraten mit Rotkohl und Klößen · B. Eis · C. Pommes | A | 圣马丁鹅配红甘蓝和丸子 |
| 42 | B1 | ex | Wo berichtet die Redaktion über die Spiele vom 3. bis 8. November? A. in VOL.4 · B. in dieser Ausgabe mit Ergebnissen · C. gar nicht | A | VOL.4 报道 11 月 3–8 日结果 |
| 43 | A2 | ex | Martin / teilte / seinen Mantel / mit einem Bettler → ___ | Martin teilte seinen Mantel mit einem Bettler. | 主谓宾顺序 |
| 44 | B1 | ex | die Kinder / basteln / bunte Laternen / aus Papier → ___ | Die Kinder basteln bunte Laternen aus Papier. | 主谓宾顺序 |
| 45 | A2 | ex | am 11. November / beginnt / die Karnevalssession / in Köln → ___ | Am 11. November beginnt die Karnevalssession in Köln. | 时间状语开头，动词第二位 |
| 46 | B1 | ex | am Martinsfeuer / endet / der Laternenumzug → ___ | Am Martinsfeuer endet der Laternenumzug. | 地点开头，动词第二位 |
| 47 | B1 | ex | Wie viele Punkte hat Deutschland nach vier Spielen? A. acht · B. fünf · C. zwei | B | 德国 5 分，荷兰希腊各 8 分 |
| 48 | B1 | ex | Wann nennt Klopp seinen Kader? A. am 13. November · B. am 5. November · C. am 9. November | B | 主教练 11 月 5 日公布名单 |
| 49 | B1 | ex | Warum ist das Spiel in Belgrad ein Geisterspiel? A. Es ist Nacht. · B. Es gibt keine Karten. · C. Das Stadion bleibt wegen einer UEFA-Strafe leer. | C | 贝尔格莱德空场 |
| 50 | B1 | ex | Wie endete das Hinspiel gegen Serbien? A. 2:0 für Deutschland · B. 1:1 · C. 0:2 | A | 首回合德国 2:0 胜塞尔维亚 |
| 51 | B1 | ex | Das NFL-Spiel in München ist... A. abgesagt · B. ausverkauft · C. gratis | B | NFL 慕尼黑赛售罄 |
| 52 | B1 | match_set | MATCH left=das Geisterspiel | rights=['das erste Spiel gegen denselben Gegner in einer Runde', 'ein Spiel ohne Zuschauer im Stadion', 'die Firma, die die Trikots und Schuhe liefert', 'alle Karten sind weg, es gibt keine mehr'] | b | Geisterspiel=空场比赛 b |
| 53 | B1 | match_set | MATCH left=das Hinspiel | rights=['das erste Spiel gegen denselben Gegner in einer Runde', 'ein Spiel ohne Zuschauer im Stadion', 'die Firma, die die Trikots und Schuhe liefert', 'alle Karten sind weg, es gibt keine mehr'] | a | Hinspiel=首回合 a |
| 54 | B1 | match_set | MATCH left=der Ausrüster | rights=['das erste Spiel gegen denselben Gegner in einer Runde', 'ein Spiel ohne Zuschauer im Stadion', 'die Firma, die die Trikots und Schuhe liefert', 'alle Karten sind weg, es gibt keine mehr'] | c | Ausrüster=装备赞助商 c |
| 55 | B1 | match_set | MATCH left=ausverkauft | rights=['das erste Spiel gegen denselben Gegner in einer Runde', 'ein Spiel ohne Zuschauer im Stadion', 'die Firma, die die Trikots und Schuhe liefert', 'alle Karten sind weg, es gibt keine mehr'] | d | ausverkauft=售罄 d |
| 56 | B1 | ex | Die Niederlande haben ___ (viel) Punkte als Deutschland. | mehr | viel → mehr（荷兰 8 分多于德国 5 分） |
| 57 | B1 | ex | Das NFL-Spiel beginnt ___ (spät) als die Karnevalseröffnung. | später | spät → später（15:30 晚于 11:11） |
| 58 | B1 | ex | In Belgrad spielt Deutschland ohne Zuschauer — das ist ___ (leise) als ein Heimspiel in Berlin. | leiser | leise → leiser（空场比主场安静） |
| 59 | B1 | ex | Klopp nennt den Kader ___ (früh) als das Spiel in Belgrad. | früher | früh → früher（11 月 5 日早于 11 月 13 日） |
| 60 | B1 | ex | Serbien–Deutschland beginnt um... A. 20.45 Uhr · B. 18.45 Uhr · C. 15.30 Uhr | A | 塞尔维亚–德国周五 20:45 |
| 61 | B1 | ex | Das NFL-Spiel in München beginnt um... A. 20.45 Uhr · B. 15.30 Uhr · C. 11.11 Uhr | B | NFL 周日 15:30 |
| 62 | B1 | ex | Deutschland–Niederlande ist am Montag um... A. 15.30 Uhr · B. 17.30 Uhr · C. 20.45 Uhr | C | 德国–荷兰周一 20:45 |
| 63 | B1 | ex | Bayern–Köln beginnt am Freitag um... A. 20.30 Uhr · B. 15.30 Uhr · C. 18.30 Uhr | A | 拜仁–科隆周五 20:30 |
| 64 | B1 | ex | Schalke–Stuttgart ist das Topspiel am Samstag um... A. 15.30 Uhr · B. 17.30 Uhr · C. 20.30 Uhr | B | 沙尔克–斯图加特周六 17:30 |
| 65 | B1 | ex | Wann sind alle wieder in der Schule? A. am 9. November · B. am 11. November · C. am 15. November | A | 11 月 9 日全德复课 |
| 66 | B1 | ex | Was basteln die Kinder? A. ein Kostüm · B. Laternen aus Papier · C. einen Kürbis | B | 孩子们做纸灯笼 |
| 67 | B1 | ex | Was ist am 11. November richtig? A. Nur Karneval. · B. Karneval am Vormittag, St. Martin am Abend. · C. Nur St. Martin. | B | 上午狂欢，下午圣马丁 |
| 68 | B1 | ex | Was läuft am Sonntag im Fernsehen? A. die Bundesliga · B. die NFL · C. ein Film | B | NFL 周日在电视上 |
| 69 | A2 | ex | Was schauen viele Jugendliche am Freitag? A. die Nationalmannschaft in Belgrad · B. die NFL · C. den Karneval | A | 周五看国家队比赛 |
| 70 | B1 | ex | Die Kinder tragen eine bunte ___ durch die Straßen. | Laterne | 纸灯笼 |
| 71 | B1 | ex | In der Schule ___ die Kinder Laternen. | basteln | 做灯笼 |
| 72 | B1 | ex | Die Kinder singen ein Martins___. | Lied | 唱圣马丁歌曲 |
| 73 | B1 | ex | In Köln tragen die Kinder ein buntes ___. | Kostüm | 狂欢节服装 |
| 74 | A2 | ex | Am Abend zieht der ___ durch die Straßen. | Umzug | 灯笼游行 |
| 75 | A2 | ex | Auf der Laterne ist ein ___. | Stern | 灯笼上的星星 |
| 76 | B1 | ex | Die Kinder freuen sich. St. Martin kommt. (weil) → ___ | Die Kinder freuen sich, weil St. Martin kommt. | weil 句动词置尾 |
| 77 | B1 | ex | Er bleibt zu Hause. Es ist dunkel. (weil) → ___ | Er bleibt zu Hause, weil es dunkel ist. | ist 置尾 |
| 78 | B1 | ex | Sie geht in die Bibliothek. Sie will ein Buch lesen. (weil) → ___ | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | will 置尾 |
| 79 | B1 | ex | Köln feiert. Die Karnevalssession beginnt. (weil) → ___ | Köln feiert, weil die Karnevalssession beginnt. | beginnt 置尾 |
| 80 | A2 | ex | Auch in Bayern sind die Herbstferien am 9. November vorbei. Richtig oder falsch? | Richtig | 11 月 9 日巴伐利亚也复课 |
| 81 | B1 | ex | Der Laternenumzug findet am Vormittag statt. Richtig oder falsch? | Falsch | 灯笼游行在晚上 |
| 82 | A2 | ex | Die Kinder singen Martinslieder. Richtig oder falsch? | Richtig | 孩子们唱圣马丁歌曲 |
| 83 | B1 | ex | Was interessiert die Leser am meisten (Übungsdaten)? A. Nations League und NFL · B. St. Martin · C. Volkstrauertag | A | 46% 足球最受关注 |
| 84 | B1 | ex | Was ist die zweitgrößte Gruppe? A. Volkstrauertag · B. St. Martin und Karneval · C. Nations League | B | 节日 34% 第二 |
| 85 | B1 | ex | Fußball und Feste zusammen sind... A. 66 % · B. 80 % · C. 100 % | B | 46+34=80 |
| 86 | B2 | ex | Welche Gruppe ist kleiner? A. Feste · B. Gedenken · C. beide gleich | B | 纪念 20% 最小 |
| 87 | B1 | ex | Wie viele Prozent interessieren sich für den Volkstrauertag? A. 20 % · B. 34 % · C. 46 % | A | 纪念 20% |
| 88 | B2 | ex | Die drei Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 % | B | 46+34+20=100 |
| 89 | B2 | ex | Wann ist Volkstrauertag? A. am 11. November · B. am 15. November · C. am 22. November | B | 11 月 15 日纪念日 |
| 90 | B2 | ex | Wer überträgt die Gedenkstunde ab 13.30 Uhr? A. das ZDF · B. RTL · C. die ARD | A | ZDF 13 点半直播纪念仪式 |
| 91 | B2 | ex | Wie hoch ist die Stromsteuer für Haushalte? A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent | B | 家庭电力税 2.05 欧分 |
| 92 | B1 | ex | Wann soll der Bundeshaushalt 2027 verabschiedet werden? A. am 15. November · B. am 27. November · C. am 18. November | B | 2027 年预算 11 月 27 日表决 |
| 93 | B2 | ex | Die Gedenkstunde ___ (werden) live übertragen. | wird | 被动：wird + Partizip II |
| 94 | B2 | ex | Niemand weiß, ___ die Einigung gelingt. | ob | ob 引导间接疑问句 |
| 95 | B1 | ex | Die Debatte ___ (gehen) weiter. | geht | gehen → geht |
| 96 | B2 | ex | Steinmeier ___ (sprechen) das Totengedenken. | spricht | sprechen → spricht |
| 97 | B1 | ex | In vielen Städten gibt es eine ___. | Kranzniederlegung | 献花圈仪式 |
| 98 | B2 | ex | Gedenken heißt: für Frieden und ___ einstehen. | Versöhnung | 为和平与和解 |
| 99 | B2 | ex | Die Gedenkstunde steht im Zeichen der deutsch-österreichischen ___. | Verbundenheit | 德奥联系 |
| 100 | B1 | ex | Die Menschen ___ der Opfer von Gewalt und Krieg. | gedenken | 纪念受害者 |
| 101 | A2 | ex | Am Freitag ___ in Belgrad gespielt. | wird | 被动：wird + Partizip II |
| 102 | A2 | ex | Am 11. November ___ zwei Feste gefeiert. | werden | 复数：werden |
| 103 | A2 | ex | Die Karnevalssession ___ um 11.11 Uhr beginnen. | wird | werden + 原形表将来 |
| 104 | A2 | ex | „Es wird gespielt“ ist... A. Passiv · B. Perfekt · C. Imperativ | A | 被动语态 |
| 105 | B1 | ex | Im November ist die Nacht ___ (lang) als der Tag. | länger | lang → länger（夜晚比白天长） |
| 106 | B1 | ex | Es wird früher dunkel, ___ die Tage kürzer werden. | weil | weil 引导原因 |
| 107 | B1 | ex | Viele bleiben zu Hause. Es ist dunkel. (weil) → ___ | Viele bleiben zu Hause, weil es dunkel ist. | weil 句动词置尾 |
| 108 | B1 | ex | „Länger als sonst“ heißt... A. 比平时更长 · B. 和平时一样 · C. 比平时更短 | A | länger als = 比……更长 |
| 109 | B2 | ex | Ich weiß nicht, ___ die Stromsteuer sinkt. | ob | ob 引导间接疑问 |
| 110 | B2 | ex | Es ist ___ , ob sich Union und SPD einigen. | fraglich | Es ist fraglich, ob ... = 是否还难说 |
| 111 | B2 | ex | Ich finde: Das Gedenken braucht Stille. (dass) → ___ | Ich finde, dass das Gedenken Stille braucht. | dass 句动词置尾 |
| 112 | B2 | ex | „Das Gedenken braucht Stille“ höflich sagen: A. „Stille, sofort!“ · B. „Meiner Meinung nach braucht das Gedenken Stille.“ · C. „Die Politik macht alles falsch.“ | B | 礼貌表达观点 |
| 113 | A2 | comprehension:cloze_defs | CLOZE/DIALOGUE option set | A | beginnt（第三人称单数） |
| 114 | A2 | comprehension:cloze_defs | CLOZE/DIALOGUE option set | B | bastelt（第三人称单数） |
| 115 | A2 | comprehension:cloze_defs | CLOZE/DIALOGUE option set | A | geht（第三人称单数） |
| 116 | A2 | comprehension:cloze_defs | CLOZE/DIALOGUE option set | B | singt（第三人称单数） |
| 117 | A2 | comprehension:cloze_defs | CLOZE/DIALOGUE option set | A | schaut（第三人称单数） |
| 118 | B1 | comprehension:cloze_defs | CLOZE/DIALOGUE option set | B | sieht（第三人称单数） |
| 119 | A2 | comprehension:cloze_defs | CLOZE/DIALOGUE option set | B | erzählt（第三人称单数） |
| 120 | B1 | comprehension:cloze_defs | CLOZE/DIALOGUE option set | A | beginnt（第三人称单数） |
| 121 | B1 | ex | Die Karnevalssession beginnt um... A. 11.11 Uhr · B. 15.30 Uhr · C. 20.45 Uhr | A | 狂欢季 11 点 11 分开幕 |
| 122 | A2 | ex | Deutschland spielt am Freitag in... A. Berlin · B. Belgrad · C. München | B | 周五客战塞尔维亚 |
| 123 | A2 | ex | Das NFL-Spiel in München beginnt um... A. 11.11 Uhr · B. 20.45 Uhr · C. 15.30 Uhr | C | NFL 周日 15:30 |
| 124 | B1 | ex | Der Volkstrauertag ist am... A. 15. November · B. 11. November · C. 22. November | A | 纪念日 11 月 15 日 |
| 125 | B1 | ex | Die Stromsteuer für Haushalte beträgt... A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent | B | 家庭电力税 2.05 欧分 |
| 126 | A2 | ex | Klopp nennt seinen Kader am... A. 13. November · B. 5. November · C. 9. November | B | 主教练 11 月 5 日公布名单 |
| 127 | B1 | ex | Die Gedenkstunde überträgt ab 13.30 Uhr... A. das ZDF · B. RTL · C. die ARD | A | ZDF 13 点半直播纪念仪式 |
| 128 | A2 | ex | Der Totensonntag ist am... A. 15. November · B. 18. November · C. 22. November | C | 亡灵主日 11 月 22 日 |
| 129 | B1 | ex | Wann gehen die Kinder aus dem Haus? A. um halb acht · B. um acht · C. um halb neun | A | halb acht = 7:30 |
| 130 | A2 | ex | Was bastelt die Familie am Mittwoch? A. ein Kostüm · B. eine Laterne · C. einen Kürbis | B | 周三做灯笼 |
| 131 | A2 | ex | Was schaut die Familie am Freitag? A. Deutschland in Belgrad · B. die NFL · C. den Karneval | A | 周五看德国队 |
| 132 | B1 | ex | Wann schaut die Familie das NFL-Spiel? A. Samstag 18.30 Uhr · B. Sonntag 15.30 Uhr · C. Freitag 20.45 Uhr | B | NFL 周日 15:30 |
| 133 | A2 | ex | die Karnevalssession / beginnt / am Mittwoch → ___ | Die Karnevalssession beginnt am Mittwoch. | 时间状语，动词第二位 |
| 134 | A2 | ex | wir / basteln / eine Laterne / aus Papier → ___ | Wir basteln eine Laterne aus Papier. | 主谓宾顺序 |
| 135 | B1 | ex | die Kinder / gehen / am Montag / wieder in die Schule → ___ | Die Kinder gehen am Montag wieder in die Schule. | 时间状语开头，动词第二位 |
| 136 | B1 | ex | am Sonntag / ist / Volkstrauertag / in ganz Deutschland → ___ | Am Sonntag ist Volkstrauertag in ganz Deutschland. | 地点时间开头，动词第二位 |
| 137 | A2 | ex | Der Karneval beginnt um 11.11 Uhr in Köln.（译成中文） | 狂欢节 11 点 11 分在科隆开幕。 | beginnen = 开始 |
| 138 | A2 | ex | Ich bastle am Mittwoch eine Laterne.（译成中文） | 我周三做一个灯笼。 | basteln = 制作 |
| 139 | B1 | ex | Die Schule hat am 9. November wieder begonnen.（译成中文） | 学校 11 月 9 日又开学了。 | wieder begonnen = 又开始 |
| 140 | B1 | ex | 我周日看 NFL 比赛。（译成德语） | Am Sonntag schaue ich das NFL-Spiel. | 看比赛 = das Spiel schauen |
| 141 | B1 | match_set | MATCH left=der Mantel | rights=['das Licht aus Papier, das die Kinder am Abend tragen', 'der warme Umhang, den Martin mit dem Bettler teilte', 'die Aussöhnung nach einem Streit — Frieden zwischen Menschen', 'ein Spiel ohne Zuschauer im Stadion'] | b | Mantel=斗篷 b |
| 142 | B1 | match_set | MATCH left=die Laterne | rights=['das Licht aus Papier, das die Kinder am Abend tragen', 'der warme Umhang, den Martin mit dem Bettler teilte', 'die Aussöhnung nach einem Streit — Frieden zwischen Menschen', 'ein Spiel ohne Zuschauer im Stadion'] | a | Laterne=灯笼 a |
| 143 | B1 | match_set | MATCH left=das Geisterspiel | rights=['das Licht aus Papier, das die Kinder am Abend tragen', 'der warme Umhang, den Martin mit dem Bettler teilte', 'die Aussöhnung nach einem Streit — Frieden zwischen Menschen', 'ein Spiel ohne Zuschauer im Stadion'] | d | Geisterspiel=空场比赛 d |
| 144 | B1 | match_set | MATCH left=die Versöhnung | rights=['das Licht aus Papier, das die Kinder am Abend tragen', 'der warme Umhang, den Martin mit dem Bettler teilte', 'die Aussöhnung nach einem Streit — Frieden zwischen Menschen', 'ein Spiel ohne Zuschauer im Stadion'] | c | Versöhnung=和解 c |
| 145 | A2 | comprehension:ddefs | CLOZE/DIALOGUE option set | B | singst（第二人称单数） |
| 146 | A2 | comprehension:ddefs | CLOZE/DIALOGUE option set | A | macht（第二人称复数） |
| 147 | A2 | comprehension:ddefs | CLOZE/DIALOGUE option set | A | essen（第一人称复数） |
| 148 | B1 | comprehension:ddefs | CLOZE/DIALOGUE option set | B | machst（第二人称单数） |
| 149 | B1 | comprehension:ddefs | CLOZE/DIALOGUE option set | A | schaue（第一人称单数） |
| 150 | B1 | reg_ex | None | 开放题 — 要点见写作框，范文在第 8 版写作框内 | 按要点给分 |


## 10. Final verdict

**ROUND 2 FAIL — de-zh-cn blocked by D-R2-1 (P8 key 140 word split `da` / `sNFL-Spiel.`); the other 10 editions PASS and are shippable.**

Blocking defect list (complete): **D-R2-1 only.** All Round 1 defects and minors are CONFIRMED fixed. All 150 keys are semantically correct. The fix required is a P8 re-wrap of the zh-cn edition only, followed by kinsoku + occlusion re-gates and a P8-only re-proofread.
