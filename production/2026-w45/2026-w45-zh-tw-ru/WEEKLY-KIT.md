# Lucerna Weekly — W45 zh-tw × ru (Traditional Chinese target · Russian reader) — WEEKLY KIT

## Edition identity

- **Pairing:** zh-tw × ru — Traditional Chinese text, explanations in Russian, for Russian-speaking readers.
- **Slug:** 2026-w45-zh-tw-ru. **Issue week:** Mon 2026-11-02 to Sun 2026-11-08 (magazine model).
- **Masthead:** Lucerna (no article — Chinese is article-less).
- **Pairing badge (P1, y=378, 21pt bold, OLIVE #3e4c2a, centered, measured width 1287.4 px):** ТЕКСТЫ НА КИТАЙСКОМ (ТРАДИЦИОННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ
- **Footers (all 8 pages):** Lucerna · КИТАЙСКИЙ (ТРАДИЦИОННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА КИТАЙСКОМ (ТРАДИЦИОННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ / Страница N из 8
- **Derived from:** the W45 zh-tw core (files/weekly-report-w45-zhtw-core/, Traditional Chinese text + English explanations, VOL.2). Every Traditional Chinese article sentence/stem/option/key is byte-identical to the core; ONLY the explanation layer was rewritten (English → Russian).
- **Build dir:** hidden_files/weekly-report-w45-zh-tw-ru-build/ (run.py → svg/, render.py → cards/ + PDFs). **Transform:** transform.py in the same dir — every explanation-layer change lives there (see §7).
- **Deliverables (this dir):** svg/ (8), cards/ (8 PNGs 1950×2700 RGB), Lucerna-VOL2-RU.pdf (print), Lucerna-VOL2-RU-web.pdf (web), ABSTRACT.txt.
- **Exercises:** 150, identical registry (A2 44 · B1 74 · B2 32; pages 10/18/18/18/18/18/12/38; types 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1). These are the zh-tw core's TRUE counts from its KIT — not the zh-cn core's 56/69/25 split.
- **Delivery:** NOT finalized by the builder (independent proofread follows); NOT posted to Discord, NOT sent into the main chat, no cron created, weekly-git untouched, insert.py NOT run.

## 0. Pre-flight duplicate check (coordinator ruling: NO CONCURRENT WRITER)

- Delivery dir files/weekly-report-w45-zh-tw-ru/ and build dir hidden_files/weekly-report-w45-zh-tw-ru-build/ did not exist at task start (fresh dirs, created by this build).
- Two mtime snapshots 120 seconds apart showed ZERO changes; no live worker/process was writing to these dirs (other workers visible at the time belonged to unrelated zh-tw-nl / zh-tw-es builds in different dirs).
- Verdict: CLEAR to proceed; no concurrent writer.

## 1. Baseline first

- `tools/freeze.py baseline` on the core build: **8/8 SVGs byte-identical** (p1 4672c972…, p2 889fb533…, p3 508703c2…, p4 e04b62ea…, p5 4dfce72d…, p6 06ba4c66…, p7 00ac7f57…, p8 e6e97d02…), shipped core SVGs re-hashed unchanged afterwards.
- The unmodified copy in this edition's build dir reproduced the same 8 core SVGs byte-identically (sha256-identical on all 8) before any explanation change. Only then was transform.py applied.

## 2. Traditional independence — HARD GATE (no conversion, ever)

- The edition's Traditional text comes ONLY from the zh-tw core (frozen) plus the W43 zh-tw-ru precedent for furniture. No Simplified→Traditional conversion, no OpenCC, no character mapping table of my own was used anywhere in this build.
- **Cross-check (method):** text nodes were extracted from the shipped SVG files themselves — (a) W43 zh-tw-ru SVGs, (b) W45 zh-tw core SVGs — and their CJK character sets unioned (1040 chars). Every CJK character in this edition's SVGs was checked against that union.
- **Result: edition CJK set 780 chars, outside the union: NONE (empty list).** The edition introduces zero new CJK characters beyond the union; its Traditional text is a subset of the core's own characters.
- **Simplified-only spot scan:** a list of Simplified-only forms (邮 说 国 龙 马 发 观 欢 对 让 认 识 语 学 读 书 报 纸 电 话 车 门 问 间 见 风 云 气 头) was checked against the edition's CJK set: **zero hits**. Any such hit would have been a build failure; there is none.
- Note for the proofreader: the core's own Simplified-character audit (OpenCC s2t, Taiwan variants only) is inherited unchanged because the target text is byte-identical to the core.

## 3. Furniture three-way table (core · W43 zh-tw-ru · this edition)

Measured from the shipped P1 SVGs themselves (not assumed):

| Element | W45 zh-tw core | W43 zh-tw-ru (shipped) | This edition (W45 zh-tw-ru) |
|---|---|---|---|
| P1 edition line (y=316, 27pt sans, grey) | 繁體中文版 · VOL.2 · 2026年11月2日(一)至11月8日(日) · 台灣 / 香港 | 繁體中文版 · VOL.1 · 2026年10月19日(一)至10月25日(日) · 台灣 / 香港 | Identical to core (frozen) |
| P1 badge line (y=378, 21pt bold, centered) | 繁體中文正文 · 英語講解 — Traditional Chinese text · Explanations in English · the edition for English-speaking readers (OLIVE #3e4c2a) | ТЕКСТЫ НА КИТАЙСКОМ (ТРАДИЦИОННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ (OLIVE #3e4c2a) | Same slot, size, color and text as W43 zh-tw-ru (OLIVE — NOT the zh-tw-de build's BRICK variant; the zh-tw-ru family precedent is OLIVE, measured in both the core and W43 zh-tw-ru P1 SVGs). Badge width 1287.4 px (≤1820) |
| P1 strapline (y=410, 30pt bold BRICK) | 金融科技週 · 台北旅展 · 味全龍封王——本週台港最熱的三件事 | 颱風 · 連假 · 金鐘獎 · 台灣大賽——本週最忙的一週 | Identical to core (frozen content) |
| Badge slot ruling | — | — | **In-place replacement at y=378, 21pt bold OLIVE** — the ZH-TW core family precedent (same slot as zh-tw-de's y=378/21pt finding, different color: OLIVE per the zh-tw-ru family's own shipped P1). This is NOT the zh-cn family's (975,434) slot. |
| Footers | Lucerna · 繁體中文週報 VOL.2 · 繁體中文正文 · 英語講解 · Traditional Chinese text · English explanations / 第 N 版 / 共 8 版 | Lucerna · КИТАЙСКИЙ (ТРАДИЦИОННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.1 · ТЕКСТЫ НА КИТАЙСКОМ (ТРАДИЦИОННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ / Страница N из 8 | Lucerna · КИТАЙСКИЙ (ТРАДИЦИОННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА КИТАЙСКОМ (ТРАДИЦИОННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ / Страница N из 8 (VOL.2 adapted) |
| Gloss prefix (bslib4.gloss) | Notes｜ | Пояснение — (family's own shipped build code, bslib4.py line 197) | Пояснение — (W43 zh-tw-ru code, NOT an invented form — README #14: family code wins) |
| P8 separator | — Page N — | — СТРАНИЦА N — | — СТРАНИЦА N — |
| P8 key style | N. key — note (dash style), 12.8pt, lh 1.12 | N. key — note (dash style) | **Core's dash style and geometry kept byte-identical (12.8/1.12)** — README #8: a fan-out keeps its core's answer-generation code unchanged. |
| P8 note brackets | dash separator, no brackets | dash separator, no brackets | dash separator, no brackets (writing item 150 printed as "150. ✓ note"; its Russian note uses the W43 bracket form "(Открытое задание — образец выше, в разделе F (138 знаков))") |
| Band titles (Chinese half frozen + Russian half) | 生活 · Life / 文化 · Culture / 體育 · Sport / 青年 · Youth / 深讀 · Deep read / 語言 · Language focus / 測驗與答案 · Test & keys | 生活 · Жизнь / 文化 · Культура / 體育 · Спорт / 青年 · Молодёжь / 深讀 · Глубокое чтение / 語言 · Языковой фокус / 測驗與答案 · Тест и ответы | Same Russian halves as W43 zh-tw-ru |
| Instruction words | Fill in / Match / Writing | Заполните / Сопоставьте / Напишите | Заполните / Сопоставьте / Напишите (section head F uses the noun Письмо; the F glossline and instr use Напишите) |
| P7 phrase head / tags | 本週金句 · Phrases of the week — word for word from this issue's articles / (p. N) | 本週金句 · Фразы недели / (Страница N) | Фразы недели — слово в слово из статей этого номера + (Страница N) tags, distribution Страница 1×2, 2, 3×2, 4, 5, 6 (= core distribution) |
| Readers' corner head | 讀者園地 · Readers' corner | 讀者園地 · Уголок читателя | 讀者園地 · Уголок читателя |

## 4. What is Russian now (the full explanation layer)

All 12 Пояснение gloss boxes; every bilingual section head (Chinese half kept, Russian half per §3); all band subtitles (Chinese part kept + Russian tail); both P1/P6 bylines (Сообщение редакции · Источник: …) and the P4 TSNA byline; the P1 word-of-the-week gloss; both practice-example arithmetic lines (Russian number style: NT$2 400 + NT$1 600 = NT$4 000; NT$6 200 − NT$1 200 = NT$5 000); the P4 chart title + note; the P6 chart title + source line + compare-box paragraph; all four Over-to-you questions; all P7 column lead/body/closing paragraphs, all 3 glosslines, all 3 clinic notes, the sentence-frame texts, the readers'-corner disclosure (Russian), all 8 phrase translations; the VOL.3 teaser head (下期預告 · На следующей неделе (VOL.3) — the Chinese teaser text is frozen content, kept); P8 section heads A–F, the §F glossline, the Образец ответа: label, the keys header + right note, all 8 group separators, and **all 150 P8 answer notes in Russian**. Credit lines remain byte-identical to the core (source attributions, not apparatus).
Two separate AI strings were both translated (the zh-cn content8:62 AI-variant trap analogue): P6 note "AI helps read data, spot risks and answer clients." → "ИИ помогает читать данные, замечать риски и отвечать клиентам." AND P8 note "AI inside finance is 人工智慧＋." → "ИИ в финансах — это 人工智慧＋."

## 5. Gates (all green before BUILT)

- **Freeze baseline:** 8/8 byte-identical (see §1).
- **Freeze diff --strict-cjk (final render):** per page +24/−22, +40/−35, +46/−38, +38/−33, +44/−40, +43/−37, +93/−90, +198/−187 strings; **added CJK = 0 on all 8 pages, TOTAL 0**. Intermediate note: the first Russian draft added 1 CJK punctuation char by the typesetter's own _fw() rule (P7 memory line "сначала 封王, затем…" — comma directly after a CJK char converted to ，). This was NOT kept as an adjudication — the line was reworded to "сначала 封王 — затем…" and the final diff reads 0. The _fw() rule itself is the frozen core typesetter, unchanged. Russian strings otherwise keep the core English string's CJK characters at the same positions/counts, or drop them; no new CJK character was introduced.
- **p8.py compare (explicit P8 SVGs, total 150):** core 150 noted, edition 150 noted, **status CLEAN, missing=[], extra_count=0, keydiff=[]**. The single intentional apparatus change is item 150's writing line: note → "(Открытое задание — образец выше, в разделе F (138 знаков))" (same class as W43's #150; the key itself is untouched Chinese "(開放題,範文如下)" and the tool's printed-key extraction reports the writing item via its ✓ line, hence keydiff[]).
- **Occlusion audit (tools/occlusion_audit.py):** selftest OK (all 6 planted classes fired, clean controls silent); edition **0 flags**; core 0 flags; **NEW vs core 0**. Five NEW flags on the first Russian render were fixed in the transform (not adjudicated away): P2 Over-to-you box 230→250 with the Champion-deals box shifted +20 (audit: ink 1326.4 > border 1322.0); P5 stage-shows box title shortened ("Выступления на сцене" → "Выступления", audit: right ink 1900.0 > border 1885.0); P6 compare box title shortened ("Сравнивайте внимательно" → "Сравнивайте цены", audit: right ink 1953.8 > border 1885.0 and past the 1950 page edge); P7 readers-box height formula tail +26→+36 (audit: ink 1751.9 > border 1745.4). Final audit after re-render: 0 flags.
- **Same-baseline ink-collision scan (build-dir audit_extra.py, PIL + TC font, ascent-corrected):** edition **0 flags**; core control 0 flags.
- **Chart-label element check (same script, P4/P6, text ink vs any later-drawn rect):** edition **0 flags**; core 0 flags. P4 bars measured 120.0 px (1 run) and 600.0 px (5 runs); P6 bars 600.0/800.0/800.0/800.0 px (6/8/8/8 hours) — identical to the core's chart geometry.
- **Gloss counts (item-identical to core):** gloss() boxes **12 = 12** (rendered "Пояснение — " boxes: 12; "Notes" boxes: 0); glossline() **4 = 4** (P7 ×3 + P8 §F ×1); match_set note items **16 = 16** (4 sets × 4). Counting method per README #21: gloss() call strings and match-set note lists counted item by item from the build sources, then verified in the render. (The "33" figure from another family's core does not apply here; the zh-tw core's true counts are 12/4/16.)
- **Registry:** 150, ZERO FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build log (build5.log: 0 matches). Final flow ends: P1-lead 1900 (bottom 1935), P1-quiz 2225, P2-main 1264, P3-main 1677, P4-main 439 (bottom 1020), P4-ex 2513, P5-main 1391, P6-main 663 (bottom 860), P6-ex 2189, P7-a2 1529 / b1 1529 / b2 1496 (bottom 1560), P7 col3 1755.36, P7 teaser 2553.36 (footer rule 2580 — clear), P8-ex col 2/3 y=1250 (bottom 1252, as core), P8-keys col 3/3 y=2341 (bottom 2540).
- **P7 golden sentences:** all 8 verbatim from this issue's own articles, **exactly 2× each** issue-wide (article + P7; core also 2×8), each 1× on P7 itself, with correct page tags (Страница 1×2, 2, 3×2, 4, 5, 6).
- **Images:** per-page <image> payloads **byte-identical to the core** (counts 1/1/0/1/1/0/0/0; placements identical); all 4 Commons Artist credits verbatim (Wilfredor CC0; CorraleH CC0; Bain News Service Public domain; Benjamin Balazs CC0).
- **Readers' corner:** frozen Traditional disclosure intact (延期披露…你的來信,下一期見。) + Russian disclosure stating no genuine letters exist + explicit open invitation in Russian ("Пример от редакции — не настоящее письмо. VOL.1 обещал настоящие письма и лучшие сочинения с 8-й страницы с этого номера, но пригодного не поступило: пример остаётся — пишите нам!"). The frozen example letter itself (台北小讀者) is untouched target text.
- **Residual-Latin adjudication:** full Latin-token inventory over the rendered text (50 distinct tokens): every remaining Latin token adjudicates to one of: (i) exercise/section letters (A–F, a–d) and frame variables (X, Y); (ii) frozen target-text proper noun/theme/title (Fintech Nexus: Bridging the World, Building the Future; SUPER STAGE; SOLID TIDES; JUMP; Trick or Treat; CTBC; TSNA; MVP; ITF; StartmeupHK; the "x" in "FinTech Week x StartmeupHK"); (iii) verbatim Commons credit (Photo: … — CC0 / Public domain (Wikimedia Commons)); (iv) masthead/footer/label (Lucerna, VOL.2, Страница N из 8, NT$ currency code, FAQ source name). No English explanation residue remains (checked strings include "Explanations in English", "This week", "Word of the week", "Quick quiz", "Did you get it", "Fill in", "Over to you", "Work it out", "Practice example", "All notes in English", "Model answer", "Open task", "Notes", "Answer keys", "Language focus", "Deep read", "Test & keys", "Readers' corner", "Phrases of the week", "Next week" — no hits).
- **Cards eyeballed:** all 8 cards viewed page by page — no overflow, no overlap, no footer collision, badge/footers/gloss boxes/fixed boxes/chart labels/keys all clean. P8 keys end well above the footer rule; P7 teaser band ends 2553.36, clear of the 2580 rule. Non-blocking note: P7 B1 glossline/paragraph show the core typesetter's own fullwidth-paren spacing (e.g. "（封王/完封） ," — the identical pattern renders in the core's English strings too); inherited behavior, not a defect introduced by this build.

## 6. Coordinator additional check (2026-10-28, rendered-output sweep + Gate 10 repoint)

- **Rendered-output sweep (the zh-tw-pt/es 算一算 miss):** every text node of all 8 delivered SVGs was swept against a 60+ item English-head checklist (including "Work it out"). Result: **0 hits**. The 算一算 head is Russian on all three pages that carry it: P2, P3 and P5 each render exactly "算一算 · Посчитайте" (P3 card re-verified visually). Russian-head positive control: Посчитайте 3, Поняли? 4, А вы? 4, Заполните 60 (= 54 instr + 6 section heads), Сопоставьте 4, Читаем график 2, and every other Russian head ≥1 — except "Бейсбольные слова", which counts 0 only because the P4 word-card title wraps across two text nodes ("棒球詞卡 · Бейсбольные" + "слова"); both fragments are present and "Baseball words" is 0. No head was missed; no transform change was needed.
- **Gate 10 repoint (the es template issue):** this build did NOT inherit the es Gate 10 template. Its transform repoints by whole directory-name replacement (weekly-report-w45-zhtw-core → weekly-report-w45-zh-tw-ru) and the Gate 10 replay repointed the whole "files/weekly-report-w45-zh-tw-ru" segment to the sibling dir hidden_files/w45-zh-tw-ru-gate10-out — never splicing an absolute temp dir inside the ~/workspace/… prefix. Verified: no stray nested tree remains — files/ contains no gate10 dir (an early mis-pointed files/w45-zh-tw-ru-gate10-out created during the replay setup was removed the same session); the delivery dir contains only svg/, cards/, the two PDFs and ABSTRACT.txt (+ this KIT); the gate10-build dir is flat (py files + assets + logs only); the gate10-out dir holds only svg/, cards/ and the two PDFs.

## 7. Reproducible build (transform-first discipline)

Every fix-layer edit above (title shortenings, disclosure rewrites, box grows, formula padding, fw-avoidance rewording, P7 column condensations) was folded into transform.py AS IT WAS MADE — no direct build-copy edit survives. The transform (281 literal pairs, each asserting its old string is found before replacing; whole-string/line splicing only, never AST byte offsets; f-string fragments replaced with bare text, never repr literals; plus the two scoped layout fixes in _layout_fixes()) runs on a fresh copy of the core build:

```
cd hidden_files/weekly-report-w45-zh-tw-ru-build
python3 transform.py <build_dir> <edition_base_path>   # 281 pairs, all found
python3 run.py      # one-process driver: content12 -> 34 -> 56 -> 7 -> 8
python3 render.py   # cards + print/web PDFs
```

**Gate 10 (transform-solo replay, self-run before BUILT):** fresh core copy in hidden_files/w45-zh-tw-ru-gate10-build/ + transform.py ALONE (output to hidden_files/w45-zh-tw-ru-gate10-out/, repointed as a whole path segment, see §6) → run.py exit 0, render.py exit 0, **0 warnings, registry identical, 8/8 SVGs byte-identical to the delivered SVGs** (cmp clean on all 8; gate10 PDFs also byte-size-identical: print 13595492, web 3479333). The build is NOT done at 7/8 — it is 8/8.

## 8. PDF pins (delivered files)

- Print: Lucerna-VOL2-RU.pdf — 8 pages, 13,595,492 bytes, SHA-256 829aa69964ead07542de1471b93cc26a386dd03673918d215613416524a1edaf
- Web: Lucerna-VOL2-RU-web.pdf — 8 pages, 3,479,333 bytes (< 10 MB), SHA-256 18977332a09cff97bbc0f2869951bb3cb5a632a2be076f259d555d7fb9b21138
- Cards: 8 PNGs, each 1950×2700 RGB.

## 9. Facts as finalized in the core — unchanged

Hong Kong FinTech Week x StartmeupHK 2026 (Nov 2–6, main conference Nov 2–3, 45,000+ / 120+ economies / 1,000+ speakers / 800+ exhibitors); ITF Taipei travel fair (Nov 6–9, 123 countries/cities, 1,600 booths); Wei Chuan Dragons Taiwan Series champions 4–2 (Game 6 Oct 26, 6–0 shutout, MVP C.C. Mercedes); Lidong Nov 7; Kaohsiung Steel Sculpture Festival (Oct 23–Nov 22, SUPER STAGE, SOLID TIDES); Fulong sand festival closing Oct 26 (19th, 151 days); Tianmu Halloween Oct 25–26 (250 shops, 4,500 buckets); Double 11 preview only (Nov 11, not reported as done). Zero politics. All arithmetic re-derived in Russian notes (2 400+1 600=4 000; 6 200−1 200=5 000; 6+8+8+8=30; 1+5=6; 151/31 days; 4 100/8 200 coupon set; 138-character model).

## 10. Builder proofread note (self-check, before independent proofread)

- Extracted text of all 8 pages read against the core's English notes: every Russian note faithful to its English source and to its question/article/chart; every Chinese term quoted in a Russian gloss confirmed present on its own page; every date/weekday/arithmetic total re-checked (Russian number style with space thousands separators applies to Russian prose only; Chinese text untouched).
- This builder does NOT claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, creates no cron, and does not touch weekly-git pushes or insert.py.
