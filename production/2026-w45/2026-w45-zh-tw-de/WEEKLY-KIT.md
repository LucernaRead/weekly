# Lucerna Weekly — W45 zh-tw × de (Traditional Chinese target · German reader) — WEEKLY KIT

## Edition identity

- **Pairing:** zh-tw × de — Traditional Chinese text, explanations in German, for German-speaking readers.
- **Slug:** 2026-w45-zh-tw-de. **Issue week:** Mon 2026-11-02 to Sun 2026-11-08 (magazine model).
- **Masthead:** Lucerna (no article — Chinese is article-less).
- **Pairing badge (P1, y=378, 21pt bold, brick #a4553a):** CHINESISCHER TEXT (TRADITIONELL) · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER
- **Footers (all 8 pages):** Lucerna · CHINESISCHE WOCHENZEITUNG VOL.2 · TEXT AUF CHINESISCH (TRADITIONELL) · ERKLÄRUNGEN AUF DEUTSCH / Seite N von 8
- **Derived from:** the W45 zh-tw core (files/weekly-report-w45-zhtw-core/, Traditional Chinese text + English explanations, VOL.2). Every Traditional Chinese article sentence/stem/option/key is byte-identical to the core; ONLY the explanation layer was rewritten (English → German).
- **Build dir:** hidden_files/weekly-report-w45-zh-tw-de-build/ (run.py → svg/, render.py → cards/ + PDFs). **Transform:** transform.py in the same dir — every explanation-layer change lives there (see §7).
- **Deliverables (this dir):** svg/ (8), cards/ (8 PNGs 1950×2700), Lucerna-VOL2-DE.pdf (print), Lucerna-VOL2-DE-web.pdf (web).
- **Exercises:** 150, identical registry (A2 44 · B1 74 · B2 32; pages 10/18/18/18/18/18/12/38; types 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1). These are the zh-tw core's TRUE counts from its KIT — not the zh-cn core's 56/69/25 split.
- **Delivery:** NOT finalized by the builder (independent proofread follows); NOT posted to Discord, NOT sent into the main chat, no cron created, weekly-git untouched, insert.py NOT run.

## 0. Pre-flight duplicate check (coordinator ruling: NO CONCURRENT WRITER)

- Delivery dir files/weekly-report-w45-zh-tw-de/ and build dir hidden_files/weekly-report-w45-zh-tw-de-build/ did not exist at task start (fresh dirs, created by this build).
- Two mtime snapshots 120 seconds apart showed ZERO changes except the snapshot files themselves (self-referential); no live worker/process was writing to these dirs (the one running render.py at the time belonged to an unrelated zh-cn-es reproof in different dirs).
- Verdict: CLEAR to proceed; no concurrent writer.

## 1. Baseline first

- `tools/freeze.py baseline` on the core build: **8/8 SVGs byte-identical** (p1 4672c972…, p2 889fb533…, p3 508703c2…, p4 e04b62ea…, p5 4dfce72d…, p6 06ba4c66…, p7 00ac7f57…, p8 e6e97d02…), shipped core SVGs re-hashed unchanged afterwards.
- The unmodified copy in this edition's build dir reproduced the same 8 core SVGs byte-identically (cmp clean on all 8) before any explanation change. Only then was transform.py applied.

## 2. Traditional independence — HARD GATE (no conversion, ever)

- The edition's Traditional text comes ONLY from the zh-tw core (frozen) plus the W43 zh-tw-de precedent for furniture. No Simplified→Traditional conversion, no OpenCC, no character mapping table of my own was used anywhere in this build.
- **Cross-check (method):** text nodes were extracted from the shipped SVG files themselves — (a) W43 zh-tw-de SVGs, (b) W45 zh-tw core SVGs — and their CJK character sets unioned (1024 chars). Every CJK character in this edition's SVGs was checked against that union.
- **Result: edition CJK set 766 chars, outside the union: NONE (empty list).** The edition introduces zero new CJK characters beyond the union; its Traditional text is a subset of the core's own characters.
- **Simplified-only spot scan:** a list of Simplified-only forms (邮 说 国 龙 马 发 观 欢 对 让 认 识 语 学 读 书 报 纸 电 话 车 门 问 间 见 风 云 气 头) was checked against the edition's CJK set: **zero hits**. Any such hit would have been a build failure; there is none.
- Note for the proofreader: the core's own Simplified-character audit (OpenCC s2t, Taiwan variants only) is inherited unchanged because the target text is byte-identical to the core.

## 3. Furniture three-way table (core · W43 zh-tw-de · this edition)

Measured from the shipped P1 SVGs themselves (not assumed):

| Element | W45 zh-tw core | W43 zh-tw-de (shipped) | This edition (W45 zh-tw-de) |
|---|---|---|---|
| P1 edition line (y=316, 27pt sans, grey) | 繁體中文版 · VOL.2 · 2026年11月2日(一)至11月8日(日) · 台灣 / 香港 | 繁體中文版 · VOL.1 · 2026年10月19日(一)至10月25日(日) · 台灣 / 香港 | Identical to core (frozen) |
| P1 badge line (y=378, 21pt bold, centered) | 繁體中文正文 · 英語講解 — Traditional Chinese text · Explanations in English · the edition for English-speaking readers (OLIVE) | CHINESISCHER TEXT (TRADITIONELL) · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER (BRICK #a4553a) | Same slot, size, color and text as W43 zh-tw-de (BRICK) |
| P1 strapline (y=410, 30pt bold BRICK) | 金融科技週 · 台北旅展 · 味全龍封王——本週台港最熱的三件事 | 颱風 · 連假 · 金鐘獎 · 台灣大賽——本週最忙的一週 | Identical to core (frozen content) |
| Badge slot ruling | — | — | **In-place replacement at y=378, 21pt bold BRICK** — the ZH-TW core family precedent. This is NOT the zh-cn family's (975,434) slot: the zh-tw core family carries its badge on the y=378 line, and W43 zh-tw-de proves the same geometry. Badge width measured 1193.7px (≤1820). |
| Footers | Lucerna · 繁體中文週報 VOL.2 · 繁體中文正文 · 英語講解 · Traditional Chinese text · English explanations / 第 N 版 / 共 8 版 | Lucerna · CHINESISCHE WOCHENZEITUNG VOL.1 · TEXT AUF CHINESISCH (TRADITIONELL) · ERKLÄRUNGEN AUF DEUTSCH / Seite N von 8 | Lucerna · CHINESISCHE WOCHENZEITUNG VOL.2 · TEXT AUF CHINESISCH (TRADITIONELL) · ERKLÄRUNGEN AUF DEUTSCH / Seite N von 8 (VOL.2 adapted; width 1165.9px) |
| Gloss prefix (bslib4.gloss) | Notes｜ | Hinweis · (family's own shipped build code) | Hinweis · (W43 zh-tw-de code, NOT tables.json's HINWEIS uppercase — README #14: family code wins) |
| P8 separator | — Page N — | — Seite N — | — Seite N — |
| P8 key style | N. key — note (dash style), 12.8pt, lh 1.12 | N. key — note (dash style), 13.3pt, lh 1.16 (W43 core's geometry) | **Core's dash style and geometry kept byte-identical (12.8/1.12)** — README #8: a fan-out keeps its core's answer-generation code unchanged. W43's 13.3/1.16 belonged to the W43 core, not to this family rule. |
| P8 note brackets | dash separator, no brackets | dash separator, no brackets | dash separator, no brackets (no paren conversion question arises) |
| Band titles (Chinese half frozen + German half) | 生活 · Life / 文化 · Culture / 體育 · Sport / 青年 · Youth / 深讀 · Deep read / 語言 · Language focus / 測驗與答案 · Test & keys | 生活 · Leben / 文化 · Kultur / 體育 · Sport / 青年 · Jugend / 深讀 · Vertiefung / 語言 · Sprachfokus / 測驗與答案 · Test & Lösungen | Leben / Kultur / Sport / Jugend / Vertiefung / Sprachfokus / Test & Lösungen (same German halves as W43) |
| Instruction words | Fill in / Match / Writing | Ausfüllen / Zuordnen / Schreiben | Ausfüllen / Zuordnen / Schreiben |
| P7 phrase head / tags | 本週金句 · Phrases of the week — word for word from this issue's articles / (p. N) | 本週金句 · Sätze der Woche — Wort für Wort aus den Artikeln dieser Ausgabe / (S. N) | Sätze der Woche form + (S. N) tags, distribution S.1×2, S.2, S.3×2, S.4, S.5, S.6 |
| Readers' corner head | 讀者園地 · Readers' corner | 讀者園地 · Leserecke | 讀者園地 · Leserecke |

## 4. What is German now (the full explanation layer)

All 12 Hinweis gloss boxes; every bilingual section head (Chinese half kept, German half per §3); all band subtitles (Chinese part kept + German tail); both P1/P4/P6 bylines (Redaktionsbericht · Quelle: …); the P1 word-of-the-week gloss; both practice-example arithmetic lines (German number style: NT$2.400 + NT$1.600 = NT$4.000; NT$6.200 − NT$1.200 = NT$5.000); the P4 chart title + note; the P6 chart title + source line + compare-box paragraph; all four Over-to-you questions; all P7 column lead/body/closing paragraphs, all 3 glosslines, all 3 clinic notes, the sentence-frame texts, the readers'-corner disclosure (German), all 8 phrase translations; the VOL.3 teaser head (下期預告 · Nächste Woche (VOL.3) — the Chinese teaser text is frozen content, kept); P8 section heads A–F, the §F glossline, the Mustertext: label, the keys header + right note, all 8 group separators, and **all 150 P8 answer notes in German**. Credit lines remain byte-identical to the core (source attributions, not apparatus).

## 5. Gates (all green before BUILT)

- **Freeze baseline:** 8/8 byte-identical (see §1).
- **Freeze diff --strict-cjk (final render):** per page +24/−22, +37/−34, +42/−38, +34/−32, +43/−40, +42/−37, +89/−87, +199/−191 strings; **added CJK = 0 on all 8 pages, TOTAL 0**. Intermediate note: the first German draft added 3 CJK punctuation chars by the typesetter's own _fw() rule (svglib converts ASCII , : ; ? ! touching a CJK char to fullwidth: clinic note 完勝:/完封: → ：×2 on P7; key-109 note 打卡, → ，×1 on P8). These were NOT kept as adjudications — the two strings were reworded to avoid the adjacency (clinic note now ends its terms with space/period; key 109 now reads "Auf einem Fest postet man mit 打卡 ein Foto und zeigt: Ich war da."), and the final diff reads 0. The _fw() rule itself is the frozen core typesetter, unchanged.
- **p8.py compare (explicit P8 SVGs, total 150):** core 150 noted, edition 150 noted, **status CLEAN, missing=[], extra_count=0, keydiff=[]**. The single intentional apparatus change is item 150's writing line: key "(開放題,範文如下)" → "(offene Aufgabe — Mustertext unten)" and its note → "Offene Aufgabe — der Mustertext steht oben in Abschnitt F (138 Zeichen)" (same class as W43's #150; the tool's printed-key extraction reports the writing item via its ✓ line, hence keydiff[]).
- **Occlusion audit (tools/occlusion_audit.py):** selftest OK (all 6 planted classes fired, clean controls silent); edition **0 flags**; core 0 flags; **NEW vs core 0**. Two NEW BOXTITLE flags on the first German render were fixed in the transform (not adjudicated away): P2 Over-to-you box 230→250 with the Champion-deals box shifted +20 (audit: ink 1326.4 > border 1322.0); P7 readers-box height formula +14px (audit: ink 1749.8 > border 1743.9). Final audit after re-render: 0 flags.
- **Same-baseline ink-collision scan (build-dir audit_extra.py, PIL + TC font, ascent-corrected):** edition **0 flags**; core control 0 flags; W43 zh-tw-de shipped control 0 flags. (Instrument note: the first version of this scan mis-measured vertical ink (PIL getbbox anchor "la" needs the ascent subtracted) and did not unescape &amp;, producing 9 false chart flags and 1 false core flag; both bugs were fixed in the script and all three runs then read 0.)
- **Chart-label element check (same script, P4/P6, text ink vs any later-drawn rect):** edition **0 flags**; core 0 flags. P4 bars measured 120.0px (1 run) and 600.0px (5 runs); P6 bars 600.0/800.0/800.0/800.0px (6/8/8/8 hours) — identical to the core's chart geometry.
- **Gloss counts (item-identical to core):** gloss() boxes **12 = 12** (rendered "Hinweis · " boxes: 12; "Notes" boxes: 0); glossline() **4 = 4** (P7 ×3 + P8 §F ×1); match_set note items **16 = 16** (4 sets × 4). Counting method per README #21: gloss() call strings and match-set note lists counted item by item from the build sources, then verified in the render. (The "33" figure from another family's core does not apply here; the zh-tw core's true counts are 12/4/16.)
- **Registry:** 150, ZERO FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build log (build4.log). Final flow ends: P1-lead 1871 (bottom 1935), P1-quiz 2225, P2-main 1264, P3-main 1677, P4-main 366 (bottom 1020), P4-ex 2513, P5-main 1391, P6-main 663 (bottom 860), P6-ex 2189, P7-a2 1529 / b1 1496 / b2 1496 (bottom 1560), P7 col3 1757.86, P7 teaser 2555.86 (footer rule 2580 — clear), P8-ex col 3/3 y=299 (reflow vs core's col 2/3 y=1250: the German §F glossline wraps one line longer, pushing the writing item + model into the 4th column; the keys header at fixed y=1264 stays clear and the top area renders balanced — verified on the P8 card), P8-keys col 3/3 y=2257 (bottom 2540).
- **P7 golden sentences:** all 8 verbatim from this issue's own articles, **exactly 2× each** issue-wide (article + P7; core also 2×8), each 1× on P7 itself, with correct page tags (S.1×2, S.2, S.3×2, S.4, S.5, S.6).
- **Images:** per-page <image> payloads **byte-identical to the core** (counts 1/1/0/1/1/0/0/0); all 4 Commons Artist credits verbatim (Wilfredor CC0; CorraleH CC0; Bain News Service Public domain; Benjamin Balazs CC0).
- **Readers' corner:** frozen Traditional disclosure intact (延期披露…你的來信,下一期見。) + German disclosure stating no genuine letters exist + explicit open invitation in German ("Beispielbrief der Redaktion — kein echter Brief. … bis Redaktionsschluss kam nichts Veröffentlichbares — das Beispiel bleibt, und die Einladung bleibt offen: Schicken Sie uns Ihren Brief!"). The frozen example letter itself (台北小讀者) is untouched target text.
- **Residual-Latin adjudication:** full English-apparatus remnant scan over the rendered text: ZERO (checked strings include "Explanations in English", "This week", "Word of the week", "Quick quiz", "Did you get it", "Fill in", "Over to you", "Work it out", "Practice example", "All notes in English", "Model answer", "Open task", "Notes", "p. N", "Answer keys", "Language focus", "Deep read", "Test & keys", "Readers' corner", "Phrases of the week", "Next week" — no hits). Every remaining Latin token in the 772-token inventory adjudicates to one of: (i) German word or standard German loanword (Test, Quiz, Team, Shows, Code, Scan, live, online, per, pro); (ii) frozen target-text proper noun/theme/title (Fintech Nexus: Bridging the World, Building the Future; SUPER STAGE; SOLID TIDES; JUMP; Trick or Treat; Taiwan Series; Hong Kong FinTech Week; venue/event names; film titles Jurassic World / Shrek / Kung Fu Panda / Back to the Future); (iii) verbatim Commons credit (Photo: … — CC0 / Public domain (Wikimedia Commons)); (iv) masthead/footer/label (Lucerna, VOL.2, Seite N von 8, NT$ currency code, FAQ source name, exercise letters A–D and S. tags); or (v) the regex artifact "amp" from SVG "&amp;" escaping (rendered glyph is "&"). No English explanation residue remains.
- **Cards eyeballed:** all 8 cards viewed page by page — no overflow, no overlap, no footer collision, badge/footers/gloss boxes/fixed boxes/chart labels/keys all clean. P8 keys end well above the footer rule; P7 teaser band ends 2555.86, clear of the 2580 rule.

## 6. Layout adjudications (wording/geometry only; Chinese text never touched)

1. **P7 B1 head** — full German "B1 · 球賽與節氣 · Spiele & Jahreszeiten" measured 473.5px > 434 box (HEAD TOO WIDE) → "B1 · 球賽與節氣 · Spiele, Jahreszeit" (429.2px, fits; no content lost — the column still covers games and the season).
2. **P7 columns condensed** — German lead/body/closing paragraphs run longer than English: A2 tightened to end 1529 (= core), B2 tightened to end 1496 (= core), B1 ends 1496 (≤1560). No facts dropped; Chinese terms all kept.
3. **P7 col3 (clinic + frame + readers)** — first German draft pushed col3 to 1918.38 and the teaser to 2716.38 (into the footer). Condensed in the transform (clinic notes, frame texts, readers disclosure) to col3 1743.86, then the readers-box formula +14px (see §5) → col3 1757.86, teaser 2555.86, clear of the footer rule.
4. **P2 Over-to-you box** — German question needs 3 lines where English needed 2; box grew 230→250 and the Champion-deals box shifted +20 (ends 1820 < 2540). Same grow-the-box precedent as W43 DE's P2 box. Scoped to content12.py only: content34.py's P4 box carries an identical rect literal but is clean and was NOT moved.
5. **P8 §F glossline + writing apparatus** — German glossline ("Schreiben — es gibt keine einzige richtige Antwort. Es folgt ein Mustertext mit 138 Zeichen.") wraps longer than the English, reflowing P8-ex into a 4th column (see §5); no type change, no content change, keys header unaffected.
6. **fw-avoidance rewordings** — clinic note 1 and key-109 note reworded to avoid _fw() fullwidth-punctuation adjacencies (see §5 strict-CJK note); meaning unchanged.

## 7. Reproducible build (transform-first discipline)

Every fix-layer edit above (title shortening, disclosure rewrite, box grows, formula padding, fw-avoidance rewordings) was folded into transform.py AS IT WAS MADE — no direct build-copy edit survives. The transform (259 literal pairs, each asserting its total occurrence count across the target files before replacing; whole-string/line splicing only, never AST byte offsets; f-string fragments replaced with bare text, never repr literals) runs on a fresh copy of the core build:

```
cd hidden_files/weekly-report-w45-zh-tw-de-build
python3 transform.py <build_dir> <edition_base_path>   # 259 pairs, all counts asserted
python3 run.py      # one-process driver: content12 -> 34 -> 56 -> 7 -> 8
python3 render.py   # cards + print/web PDFs
```

**Gate 10 (transform-solo replay, self-run before BUILT):** fresh core copy in hidden_files/w45-zh-tw-de-gate10-build/ + transform.py ALONE (output to hidden_files/w45-zh-tw-de-gate10-out/) → run.py exit 0, render.py exit 0, **0 warnings, registry identical, 8/8 SVGs byte-identical to the delivered SVGs** (cmp clean on all 8; gate10 PDFs also byte-size-identical: print 20850433, web 3440559). The build is NOT done at 7/8 — it is 8/8.

## 8. PDF pins (delivered files)

- Print: Lucerna-VOL2-DE.pdf — 8 pages, 20,850,433 bytes, SHA-256 c8ba558624659bd70c68cd9ddc86a06ac89ecaf88e21e9f730f51d2d3bdda3e2
- Web: Lucerna-VOL2-DE-web.pdf — 8 pages, 3,440,559 bytes (< 10 MB), SHA-256 25d5ebb196b4e16c3d349aa18ff77510465352f860e9b1c7f202fba3cc577e16
- Cards: 8 PNGs, each 1950×2700 RGB.

## 9. Facts as finalized in the core — unchanged

Hong Kong FinTech Week x StartmeupHK 2026 (Nov 2–6, main conference Nov 2–3, 45,000+ / 120+ economies / 1,000+ speakers / 800+ exhibitors); ITF Taipei travel fair (Nov 6–9, 123 countries/cities, 1,600 booths); Wei Chuan Dragons Taiwan Series champions 4–2 (Game 6 Oct 26, 6–0 shutout, MVP C.C. Mercedes); Lidong Nov 7; Kaohsiung Steel Sculpture Festival (Oct 23–Nov 22, SUPER STAGE, SOLID TIDES); Fulong sand festival closing Oct 26 (19th, 151 days); Tianmu Halloween Oct 25–26 (250 shops, 4,500 buckets); Double 11 preview only (Nov 11, not reported as done). Zero politics. All arithmetic re-derived in German notes (2.400+1.600=4.000; 6.200−1.200=5.000; 6+8+8+8=30; 1+5=6; 151/31 days; 4.100/8.200 coupon set; 138-character model).

## 10. Builder proofread note (self-check, before independent proofread)

- Extracted text of all 8 pages read against the core's English notes: every German note faithful to its English source and to its question/article/chart; every Chinese term quoted in a German gloss confirmed present on its own page; every date/weekday/arithmetic total re-checked (German number style 45.000/1.600/4.100 applies to German prose only; Chinese text untouched).
- This builder does NOT claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, creates no cron, and does not touch weekly-git pushes or insert.py.
