# Lucerna Weekly — W46 Korean core (VOL.3) — WEEKLY KIT

- Issue week: Mon Nov 9 – Sun Nov 15, 2026. Issue dated Mon Nov 9, 2026.
- Target language: 한국어 (Korean). Masthead: Lucerna with NO article (Korean takes no article, per tools/tables.json).
- Explanation layer convention (same as the W43/W45 KO cores): **Chinese** — small gray glosses, notes, answer explanations, and section labels are in Simplified Chinese; the articles and exercises are in Korean. For repo/abstract purposes this core IS the zh-cn edition.
- Page spec: 1950×2700, 4 columns, warm ivory paper, dark olive-green accents (same pipeline as W45 KO core: Python → SVG → CairoSVG → PNG/PDF).
- Build dir: `hidden_files/weekly-report-w46-ko-build/` (content12/34/56/7/8.py, bslib4.py, svglib.py, run.py, render.py, check_core.py, check_gloss.py, textmd.py). Edition dir: `files/weekly-report-w46-ko-core/` (svg/, cards/, Lucerna-VOL3.pdf, Lucerna-VOL3-web.pdf, this KIT, ABSTRACT.txt, 2026-w46-ko-zh-cn.text.md).
- Build commands (from the build dir):
  - `~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py` (writes the 8 SVGs, prints flow ends + TOTAL)
  - `~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py` (writes cards/ PNGs + print PDF only; web PDF is built separately with tools/webpdf.py)
  - `cd ~/workspace/goals/lucernaread-social-media-operations/tools && ./venv/bin/python webpdf.py ../files/weekly-report-w46-ko-core/svg ../files/weekly-report-w46-ko-core/Lucerna-VOL3-web.pdf`
  - `cd ~/workspace/goals/lucernaread-social-media-operations/tools && ./venv/bin/python occlusion_audit.py ../files/weekly-report-w46-ko-core`
  - `cd ~/workspace/goals/lucernaread-social-media-operations/tools && ./venv/bin/python p8.py extract --p8 ../files/weekly-report-w46-ko-core/svg/p8-siheom.svg --total 150`
  - `~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python textmd.py . 2026-w46-ko-zh-cn ../files/weekly-report-w46-ko-core/2026-w46-ko-zh-cn.text.md "<title>"` (exports the text manuscript from source literals; answer keys/notes excluded by construction)

## Lead topic

「김장 한창, 수능 D-7 — 11월 11일은 세 가지 이름의 날」— the week the W45 VOL.3 preview promised: kimjang in full swing (verified prices + Seoul discount), one week to the CSAT (D-10 on Nov 9 → D-4 on Nov 15, D-7 on Thu Nov 12), HanNeungGeom registration closing, the verified playoff result + announced (shifted) Korean Series schedule, and the readers'-corner carry. CSAT-day measures are dated Nov 19 ONLY throughout the issue, never presented as applying this week. Korean Series games of Nov 3–8 had NOT been played at the Nov 2 press time — no scores for them are printed anywhere in the issue.

## Promises honoured (W45 → W46)

- W45-promises extractor file (`hidden_files/w46/w45-promises.md`) states the W45 KO KIT enumerates no VOL.3 teaser topics and lists only the readers'-corner carry. Cross-checked against the primary source the KIT summarises: the shipped W45 build source `hidden_files/weekly-report-w45-ko-build/content7.py` prints a VOL.3 teaser verbatim ("다음 주에는 김장이 한창이에요. 수능까지 일주일이 남았어요. 한능검 시험이 가까워져요. 플레이오프와 한국시리즈 소식도 전해요. 여러분의 편지와 8면 쓰기 우수작도 실어요. 기대해 주세요!"). The KIT records the preview's existence without enumerating topics — no direct contradiction. Per SOP §10 a printed next-issue preview must be honoured: all five items are honoured in W46 (kimjang / one week to CSAT / HanNeungGeom approaching / playoff + Korean Series news / letters + best P8 writing). This KIT-vs-printed-source discrepancy is recorded here, per the follow-up handoff's KIT-wins rule (no change to the teaser list resulted, there being no KIT contradiction).
- The extractor found NO additional KO handover items (no KO results-reporting handover, no extra KO calendar nodes). Other targets' handovers in that file were not imported. The Nov 9 (Firefighters' Day) and Nov 11 calendar nodes come from independent Korean-ecosystem research.
- W43→W45 KO promises (foliage verdict, playoffs, Champi track, Oct 31 Halloween, letters) were reported honoured in W45 per its KIT; the letters promise was carried to VOL.3 and is carried again to VOL.4 here (see readers' corner below).
- Readers' corner: NO real reader letters or best P8 texts had arrived by press time (nothing in the record says any arrived). P7 prints a clearly labelled editor's example letter PLUS the required on-page disclosure in Korean and Chinese stating no real letters/best P8 texts had arrived, the example stands, and the promise carries to VOL.4. No fabricated readers, letters, names, or quotes anywhere. The P8 지민이 story is a test passage, not presented as a real person.

## Contents by page

- P1 표지 (A2) — lead 「김장 한창, 수능 D-7 — 11월 11일은 세 가지 이름의 날」: kimjang price split (cabbage down, shrimp jeot up), CSAT countdown D-10/D-7 with Nov 19 measures explicitly NOT this week's measures, foliage two-forecast framing, Nov 11 three names, playoff result (Samsung 3–2 KIA) + KS "발표된" schedule with press-time note, HanNeungGeom window; numbers box (10 / 7 / 3 / 17 / 5,557); week calendar box (Nov 9 Firefighters' Day + Wolchulsan forecast, Nov 10 HanNeungGeom close 17:00, Nov 11 three names, Nov 12 D-7, Nov 15 KS G7 if needed; wildfire-caution note from Nov 1); contents box; word of the week 「한창」; row-B briefs; 6 drills + 4 quiz = 10 exercises.
- P2 생활 (A2) — 김장 가격 feature (aT/KAMIS Oct 16 retail prices: cabbage 5,557 won/head −10.3% YoY, shrimp jeot 20,269 won/kg +32.5% YoY; autumn cabbage output 1.222M tonnes +19%; Seoul 5–11 Nov discount at 18 Hanaro Mart stores), 소방의 날 Nov 9 feature, 한능검 box (windows incl. Seoul/Gangwon/Jeju Nov 6 10:00–12:00 only + 13:00 nationwide nuance, 27,000 won fee, Nov 17 refund deadline, Nov 11–13 cancelled-seat window with dates only — start times conflict across secondaries), 김장하는 날 + 겨울 밥상 sections, shopping-list box, facts box, D-day strip (D-10 Nov 9 / D-7 Nov 12 / D-4 Nov 15 / D-데이 Nov 19 — calendar arithmetic, labeled as such); 18 exercises.
- P3 문화 (A2→B1) — 「단풍 예보와 11월 11일의 세 이름」: agency-by-agency foliage verdicts (Forest Service/Arboretum Sep 22 maple forecast: Naejangsan Nov 4, Hallasan 1100 Road Nov 6, Wolchulsan Nov 9, Duryunsan Nov 11; National Park Service/Weatheri whole-mountain: Bukhansan Nov 4, Naejangsan Nov 11; KMA observation: Seoraksan actual peak Oct 16; NO observed peak announced for Naejangsan/Wolchulsan at press time — stated, with a Weather Nuri pointer), Naejangsan vehicle control Oct 30–Nov 15 + free shuttle, Nov 11 three names (Pepero Day / Farmers' Day / Garaetteok Day with origins), 단풍 구경 advice (대중교통, 옷차림 + 준비물 box); 18 exercises.
- P4 스포츠 (B1) — 「삼성이 KIA를 꺾고 한국시리즈에 올랐어요」: full verified playoff result (G1 Oct 26 Daegu KIA 5–1; G2 Oct 27 Daegu Samsung 8–3; G3 Oct 29 Gwangju Samsung 6–4; G4 Oct 30 Gwangju KIA 4–2; G5 Nov 1 Daegu Samsung 6–1), shifted KS schedule as announced (G1 Nov 3 18:30 Suwon … G7 Nov 11 18:30 Suwon, G5–G7 if needed) + shift reason (Oct 25 rainout, 5-game playoff, travel day) + explicit press-time note (paper closed Nov 2; G1–G5 results unknown; check the KBO website; G6/G7 conditional), drawn postseason ladder, 응원 + 결과 없는 경기 honesty section; 18 exercises.
- P5 청년 (B1) — 「수능까지 딱 일주일이 남아요」: CSAT D-7-week youth feature (551,864 candidates, 1,312 sites carried from W45), preliminary assembly Nov 18 + entry 08:10 + Nov 19 measures dated explicitly as Nov 19 only, Pepero Day youth section, 시험 전날의 하루 + 합격 기원 음식 sections; 18 exercises.
- P6 깊이 읽기 (B2) — 「예보와 발표를 읽는 법」: date vs criterion vs result analysis, comparison table (이번 주 11월 9–15일: 예보/접수 마감, 아직 결과 없어요 / 시험 날 11월 19일: D-데이, 특별 조치 있어요), source lines citing the announcing bodies, 결과를 모를 때 + 날짜를 세는 법 sections; 18 exercises.
- P7 말 공부 (A2→B2) — A2 김장의 말, B1 날짜 세는 말 (D-10/D-7/D-4/D-데이), B2 예보와 발표 읽는 법 (기준·예상·관측); error clinic ×4 (each deliberate error framed as the error with its correction; all four are new and distinct from W45); frame 「〜 전에」; readers' corner with the editor's example letter + Korean/Chinese disclosure (promise carries to VOL.4); 8 phrases of the week, each verified as a contiguous excerpt of this issue's articles with page tags; VOL.4 preview (CSAT day Nov 18–19, HanNeungGeom preparation, Nov 22 Kimchi Day, letters/best P8 writing); 12 exercises.
- P8 시험과 답 (全部) — 38 items (A 연표 完形单选 8, B 일반 문제 单选 8, C mini-reading (지민이 story) + 单选 4, D 造句 4, E 翻译 4 both directions, F 词汇配对 4, G dialogue 完形单选 5, H writing 1 on 『나의 11월 11일』); all keys registry-generated with one-line Chinese notes; writing model 158 chars (inside its printed 150–200자 instruction).

## Measured exercise counts (final build)

- TOTAL 150. By page: 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38.
- By level: A2 51 / B1 72 / B2 27.
- By type: 完成句子 48, 单选 52, 词汇配对 16, 完形单选 13, 造句 8, 句型转换 4, 判断 4, 翻译 4, 写作 1.
- P7 phrases of the week (all verified verbatim, whitespace-insensitive, against the tagged article pages): 「배추 값은 내렸는데 새우젓 값은 올랐어요」(1면), 「11월 11일은 이름이 세 개인 날이에요」(1면), 「김장이 한창이에요」(2면), 「수능까지 7일 남았어요. 오늘이 D-7예요」(2면), 「예보 날짜와 실제 관측 날짜는 달라요」(3면), 「결과는 KBO 홈페이지에서 확인하세요」(4면), 「수능까지 딱 일주일이 남아요」(5면), 「날짜와 기준과 결과를 나누면」(6면).

## Trend / fact sources (with attribution caveats)

- Research cutoff Mon Nov 2, 2026 (browser.search, Korean ecosystem). Press time is stated on P4 as Nov 2: Korean Series games of Nov 3–8 had not been played; no scores for them are printed.
- KBO 2026 postseason (multiple Nov 1, 2026 reports incl. Yonhap via sportschosun/bbs/munhwa + KBO schedule summaries): playoff Samsung 3–2 KIA (G1 Oct 26 Daegu KIA 5–1; G2 Oct 27 Daegu Samsung 8–3; G3 Oct 29 Gwangju Samsung 6–4; G4 Oct 30 Gwangju KIA 4–2; G5 Nov 1 Daegu Samsung 6–1). Semi-playoff background (re-verified): KIA beat LG 3–0 (5–1, 6–3, 13–1); wildcard LG beat Doosan 4–1 on Oct 14. Korean Series (kt wiz, regular-season 1st, vs Samsung), shifted schedule as announced: G1 Tue Nov 3 18:30 Suwon; G2 Wed Nov 4 18:30 Suwon; travel day Thu Nov 5; G3 Fri Nov 6 18:30 Daegu; G4 Sat Nov 7 14:00 Daegu; G5 Sun Nov 8 14:00 Daegu (if needed); G6 Tue Nov 10 18:30 Suwon (if needed); G7 Wed Nov 11 18:30 Suwon (if needed). Original plan G1 Mon Nov 2; shift because playoff G1 was rained out Oct 25, the playoff went to 5 games, and a travel/moving day is needed (KBO statements reported Oct 30–31). KS tickets from Mon Nov 2 11:00; media day Mon Nov 2.
- Foliage — attribute by agency, never blend: Korea Forest Service / National Arboretum forecast of Sep 22, 2026 (maple, ≥50% of leaves coloured): Naejangsan Nov 4, Hallasan 1100 Road Nov 6, Wolchulsan Nov 9, Duryunsan Nov 11. National Park Service / Weatheri forecast (whole-mountain basis): Bukhansan Nov 4, Naejangsan Nov 11. KMA observation (whole mountain ~80%): Seoraksan actual peak Oct 16, 2026 (one day earlier than average Oct 17); as of Oct 24 Naejangsan had not yet reached first foliage; Jirisan peak observed Oct 22, Deogyusan Oct 20. Jeongeup city outlook: Naejangsan peak around Nov 7–8. Naejangsan vehicle control Oct 30–Nov 15, free shuttle from Naejang Reservoir car park. At press time NO observed peak had been announced for Naejangsan or Wolchulsan — the issue says so and points readers to Weather Nuri (날씨누리).
- Kimjang prices: aT (Korea Agro-Fisheries & Food Trade Corp) KAMIS retail prices, Oct 16, 2026: cabbage 5,557 won/head, down 10.3% year-on-year; shrimp jeot 20,269 won/kg, up 32.5%; radish, green onion, garlic, ginger also down. Autumn cabbage production estimate 1.222M tonnes (KREI), +19% year-on-year. Seoul discount: Nov 5–11, 6 kimjang items (peeled garlic, altari radish, soil green onion, ginger, carrot, pear) up to half price at 18 Hanaro Mart stores (Seoul announcement Nov 1, 2026). Ministry of Oceans and Fisheries "Korea Seafood Grand Sale" Oct 28–Nov 29, 2026 covering shrimp jeot/sea salt (secondarily sourced; phrased with attribution in the issue).
- HanNeungGeom (Korean History exam) 81st: exam Sat Nov 28, 2026, 10:00, advanced (심화) only; fee 27,000 won; regular registration Nov 3 10:00 – Nov 10 17:00 with region-specific first days (Incheon/Gyeonggi Nov 3; Seoul/Gangwon/Jeju Nov 6 10:00–12:00 only; nationwide for remaining seats from Nov 6 13:00 to Nov 10 17:00); full-refund cancellation by Nov 17 17:00; cancelled-seat registration Nov 11–13 (start TIME conflicts across secondaries — 10:00 vs 13:00 — so the issue prints dates only plus "check the website for times"); photo registration from Nov 11 10:00; tickets from Nov 24 10:00; results Dec 11 10:00. Sources: secondaries citing the National Institute of Korean History notice dated Oct 19, 2026 (primary notice not directly retrieved — same caveat as W45).
- Nov 11, 2026 (Wed) — three names, one date: Pepero Day (11/11 = four 1s like four sticks; Pepero launched by Lotte 1983; schoolgirl-custom origin treated as folklore; reported in press 1996, Lotte marketing from 1997); Farmers' Day / 농업인의 날, legal memorial day since 1996 (the character 土 decomposes into 十 + 一); Garaetteok Day since 2006 (Ministry of Agriculture, Food and Rural Affairs; share rice garaetteok made from Korean rice). Nov 9, 2026 (Mon) is Firefighters' Day (소방의 날, from emergency number 119).
- CSAT (수능): Thu Nov 19, 2026; 551,864 candidates; 1,312 test sites (carried from W45, re-confirmed in research); D-counts: Mon Nov 9 D-10, Tue Nov 10 D-9, Wed Nov 11 D-8, Thu Nov 12 D-7 (exactly one week left), Fri Nov 13 D-6, Sat Nov 14 D-5, Sun Nov 15 D-4; D-1 Wed Nov 18, D-day Thu Nov 19. Preliminary assembly (예비소집) Wed Nov 18: tickets handed out, test site confirmed; exam-day entry by 08:10. Nov 19-only measures (10:00 work start, extra subway runs, English listening 13:10–13:35 flight ban, 200 m traffic control) dated Nov 19 only throughout, never as this week's measures.
- VOL.4 teaser facts (verified): Kimchi Day (김치의 날) Nov 22 every year, legal memorial day designated Feb 2020 under the Kimchi Industry Promotion Act (11 = ingredients one by one, 22 = 22 benefits). CSAT + preliminary assembly dates above.
- Calendar/weekday checks (Asia/Seoul, `date -d`, 2026): Nov 9 Mon, Nov 10 Tue, Nov 11 Wed, Nov 12 Thu, Nov 13 Fri, Nov 14 Sat, Nov 15 Sun, Nov 19 Thu, Nov 28 Sat, Nov 22 Sun. Wildfire caution period Nov 1–Dec 15, fine up to 300,000 won (W45). Cheongsong Apple Festival on-site event Nov 4–8 ended before this issue week (just-passed background only, no new claims).

## Images (all verified public-domain/CC0; no CC BY-SA used)

- P1 autumn.jpg — W43 file photo: Hakkoda valley, Artist lumoplank, CC0 (Wikimedia Commons). Captioned as a file photo, NOT a Korean foliage shot or any W46 event.
- P2 ssam.jpg — ssam vegetables with ssamjang, Artist wizdata, CC0. Captioned explicitly as ssam vegetables, NOT a kimjang photo.
- P3 bukhansan-ui.jpg — Bukhansan Ui station platform, Artist Udonhan1992, CC0. P3 apples.jpg — W43 file: Cézanne still life, public domain (autumn fruit).
- P4 baseball.jpg — W43 file: Bain News Service early-1900s US team, public domain, captioned as file photo.
- P5 study.jpg — W43 file: Gary Todd, CC0, students studying, captioned as file photo.
- P6/P7/P8 carry no photos (P6 uses two boxes + comparison table instead).
- Shortfall disclosed (same as W45): no verified PD/CC0 kimjang-making or Korean foliage shot was available from Commons file pages; the verified W45 file set is reused with honest captions.

## Self-proofread record (full pass over rendered pages + extracted SVG text)

- Read all 8 rendered cards visually (P1 + P7 twice — P7 re-checked after the disclosure fix) and all extracted SVG text node-by-node via check scripts (`check_core.py`, `check_gloss.py` in the build dir).
- All 150 answer keys re-derived against stems/articles/tables: P8 extract noted set 150/150; P7 phrases verified verbatim whitespace-insensitively against tagged pages (8/8, script output in the gate log).
- Every glossed word verified to occur on its own page (script `check_gloss.py` parses the actual gloss() strings from source): 14 apparent misses are all dictionary-form vs inflected-form pairs (집계하다→집계한, 좌우하다→좌우한다고, 막히다→막혀/막힐, 버무리다→버무려요, 아삭하다→아삭해요, 가늘다→가늰, 밀리다→밀렸어요, 하나가 되다→하나가 돼요, 끈끈하다→끈끈한, 피곤하다→피곤해져요, 졸리다→졸려요, 재다→잰, 정직하다→정직해요) — adjudicated legitimate; no true gloss orphans remain. Three gloss fixes applied while writing (젓갈→새우젓 on P1; 나누다 consolidated on P3; 날씬하다→날씬해지다 on P5).
- All date/weekday pairs checked against the real 2026 calendar; all arithmetic re-checked (D-10/D-7/D-4/D-1/D-데이; 5,557/20,269; −10.3%/+32.5%; 5–1/8–3/6–4/4–2/6–1; 551,864; 1,312; 27,000).
- Korean 띄어쓰기/particles/endings and 해요체 consistency checked page by page; the error clinic's 4 deliberate mistakes are each framed as the error with its correction, never presented as correct usage.
- No banned wording, no international-politics items, no anniversary framing. No fabricated reader, letter, name, or quote anywhere; the P7 letter is labeled as an editor's example with the on-page disclosure, and the P8 지민이 story is a test passage, not presented as a real person.
- Image captions checked for honesty (file photos labeled as such, never presented as the event itself).
- Line-start kinsoku: no lines begin with closing punctuation except the adjudicated opening-quote starts (wrap policy); verified via SVG text scan.
- ×KO orphan scan (window 10–45, ≥3-syllable-tail criterion, parenthesised fragments + line-start orphan punctuation included): 3 initial hits — P2 lone verb tail 「들어가요.」 (fixed by narrowing that paragraph's wrap width), P7 lone verb tail 「이어져요.」 (fixed by shortening the disclosure sentence so the wrap ends on a full clause), P4 parenthesised clause tail 「신문에 나온 일이에요.)」 (adjudicated non-defect: a complete clause, not a lone fragment like `(6면)`). Final scan: 1 adjudicated hit only.
- P8 F matching set re-derived (initial draft had 한창 with no matching right; rebuilt as 절정/김장/예보/관측 with keys b/a/d/c).
- Furniture-band check (manual, per tools README lesson): P1 top band and all section bars show no same-baseline ink collisions; P6 comparison-table labels checked manually — no grazed labels. Occlusion audit (which includes LINEX + same-baseline furniture scan + chart GRAZE element-check) returned 0 flags.

## Occlusion audit

- Selftest first: `selftest OK`, all 6 planted classes fire, clean controls silent.
- First audit on finished SVGs: 2 TEXTX flags — P1 calendar-box backbone lines overprinted the fixed source lines. TRUE defects: the two decorative backbone lines were removed (facts repeated in the calendar topics themselves).
- Final audit after all fixes: **0 flags**.
- Adjudicated residual (same class as W45): feature flows end partway down the third column (P2 75%, P3 88%, P4 81%, P5 52%, P6 85% of their feature regions by flow-end log) — a quiet band, not an empty column. P1 headline ends col 2 by design (row B below); P7 columns end ~1090–1124 (bottom 1560) by design (phrases section below, right rail ends y=1776.7); P8 exercise flow ends col 3 y=531 (bottom 1252) by design (keys section below at fixed y).

## Fixes log

- P2 FLOW OVERFLOW (feature exceeded 3 columns by ~128 px): trimmed by whole paragraphs/sections only — removed one sentence from 「김장하는 날」 para 1, removed the whole 「시장에서 김장 준비」 section in a second round (its content repeats W45). Final: feature ends col 2 y=1206 (bottom 1540), zero warnings.
- P7 teaser overflow (ended y=2568.7, past the 2540 limit): shortened the Korean disclosure, reduced the phrases-row pitch 132→124, shortened the frame text. Teaser then ended y=2507.7; after the letters-box fix below it ends y=2518.7 (inside the limit).
- P1 TEXTX ×2 (above): removed the two backbone lines.
- P2/P7 orphan tails (above): wrap-width narrowing + disclosure shortening.
- P7 disclosure spill (found on visual proofread: the Chinese disclosure's third line printed below the readers'-corner box, crossing the golden-phrases rule): the first shortening did NOT fix it — re-check on 2026-11-02 (during the es P7 visual review) showed the disclosure still wrapped to 3 lines with the third line outside the box, a defect the occlusion audit does not catch (it misses text escaping the bottom of this box). Real fix: `lcn2` shortened to the 37-char 2-line form `郑重说明：截稿前未收到真实来信与 8 版优秀作文，仍刊示例，顺延至 VOL.4。` AND the letters-box height formula trailing +26→+66 (the draw code's fixed gaps exceed the formula's by ~1 line). Re-rendered and visually verified: disclosure inside the box (margin +8px by rect measurement), audit 0 flags, teaser 2518.7. The same defect class was then measured and fixed in de/es/pt/it (see their KITs); en/fr/ja/nl/ru/zh-tw measured +8/+9px and needed no change.
- P8 matching-set bug (above): rebuilt F set.
- No FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build log.

## Output files + sizes (final render)

- `svg/` — 8 SVGs (p1-pyoji, p2-saenghwal, p3-munhwa, p4-seupocheu, p5-cheongnyeon, p6-gipi, p7-mal, p8-siheom).
- `cards/` — 8 page PNGs.
- `Lucerna-VOL3.pdf` — print PDF, 32,011,288 bytes. SHA-256: `05169e63026083cf2a26ede85b6730f8fe5e6a65f32c6e0c81d14a3965149999`.
- `Lucerna-VOL3-web.pdf` — web PDF (tools/webpdf.py, real text layer), 2,528,379 bytes (< 7 MB). SHA-256: `b1a0b2b4610a08e4c702766262b0f9d76ec59ea9c13a07c153241ae13f6a350e`. pdftotext: 50,765 bytes; 「김장이 한창이에요」 found 7 times; print PDF text layer consistent. 8 pages.
- `ABSTRACT.txt` — one line, Simplified Chinese, no ASCII double quotes.
- `2026-w46-ko-zh-cn.text.md` — 338 items, 8 pages, exported from the source manuscript via `textmd.py` (AST literal extraction; answer keys and key-notes excluded by construction; no PDF/SVG extraction).
- Exactly one `*web*.pdf` in the edition dir.

## Open verification debts (NOT resolved by invention — carried to the parent line)

- Korean Series G1–G5 results unknown at the Nov 2, 2026 press time; G6/G7 (Nov 10–11) conditional on the series lasting that long. The issue prints the announced schedule + press-time note only.
- No observed foliage peak announced for Naejangsan/Wolchulsan at press time; only forecasts/outlooks cited, attributed by agency.
- HanNeungGeom details from secondaries citing the Oct 19, 2026 notice (primary page not directly retrieved); cancelled-seat start time conflicts across secondaries (dates only printed).
- Image shortfall: no verified PD/CC0 kimjang-making or Korean foliage photo; only the verified W45 file set is reused with honest captions.
- This KIT declares the CORE build only. Fan-out editions (en/de/fr/es/it/pt/nl/ru/ja/zh-cn/zh-tw) are built and gated separately; their KITs carry their own gate outputs. No independent reproof round has been run on this core.

## Fix record — Round 1 proofreader verdict (fix worker, 2026-11-03)

Source-only fixes for the independent proofreader's Round 1 defects (verdict: `hidden_files/w46/ko-proofread-gates/proofreader-verdict-round1.md`); full re-render from source, no hand-edited SVG/PDF. Observations O1–O8 untouched. A Round 2 independent proofread follows; re-gating does not replace it.

- D2 (BLOCKING, frozen core, all 11 editions): P3 gloss line under the "당신은?" prompt. The `가늘다` entry was DELETED from the gloss line in `content34.py` (and mirrored in the `supp_*.py` record pair; core `check_core.py` hand list updated the same way). Before: `겹치다 重叠 · 가늘다 细 · 감사하다 感谢 · 나누다 区分、分享。` After: `겹치다 重叠 · 감사하다 感谢 · 나누다 区分、分享。` Post-fix verification: `가늘` occurs 0 times in all 8 SVGs and in `2026-w46-ko-zh-cn.text.md` of every edition; remaining gloss entries intact and correctly punctuated; P3 visually checked at full frame in all 11 editions (shortened gloss inside its box, no overflow/overlap). SVG hash comparison vs the pre-fix inventory: only `p3-munhwa.svg` changed in this edition (zh-tw: P3 + P6).
- ⚠️ DISCREPANCY FLAG for the coordinator / Round 2 proofreader (do not treat the D2 deletion as proof the stem never occurs): pre-fix verification found the attributive inflection `가늰` (가 U+AC00 + 늰 U+B2B0; `'가늘' in '가늰'` is False at codepoint level) 3× per edition — P3 body `길고 가늰 과자를 친구와 나누는` and P5 ×2 (body + exercise stem) — which the verdict's stem list (가는, 가늘게, 가느다란, 얇) did not cover. The prescribed deletion was applied exactly as ordered; post-fix `가늰` remains 3× per edition. Adjudication of keep-vs-restore belongs to Round 2.

Re-gates on the final artifacts (all 11 editions; full logs/JSONs under `hidden_files/w46/ko-fix/`):
- Freeze: core baseline 8/8 SVGs byte-identical; this edition added CJK/Hangul characters vs core: n/a (core) (ja 2,662 vs Round 1's 2,664 — the −2 is the deleted gloss entry leaving the core multiset: 3 Hangul syllables + 细; pt +8 Hangul = the adjudicated quoted sentence; zh-tw 903 unchanged: P6 `規` +1, P3 `細` −1).
- p8.py: CLEAN 150/150, keydiff [137, 138]. Occlusion audit: 0 flags, selftest OK. Counts re-measured: 150 exercises, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38 (identical to Round 1). Kinsoku: 0. Koscan reconstruction: CANDIDATES=311 TRUE_SPLITS=0 S3=0 (reconstruction script preserved at `hidden_files/w46/ko-fix/koscan_reconstruct.py`; the Round 1 koscan script itself was not preserved, only its logs).
- Render: 0 FLOW OVERFLOW / HEAD TOO WIDE. `Lucerna-VOL3-web.pdf` 2527990 bytes (< 7 MB), 8 pages, pdftotext 50748 bytes. `Lucerna-VOL3.pdf` 32010944 bytes, 8 pages. `2026-w46-ko-zh-cn.text.md` regenerated from the source manuscript via `textmd.py` (headers byte-identical to pre-fix, 338 items, 27432 bytes; diff vs pre-fix export is only the fixed gloss line(s)).

## Fix record — Round 3 (2026-11-03; Round 2 verdict FAIL — three frozen-core defects)

Round 2 proofreader verdict (2026-11-03): all 11 editions FAIL on three blocking frozen-core defects; D1 confirmed; keys 150/150 confirmed; gates clean. Round 3 fixed ONLY the three defects below, at the build sources (no SVG/PDF patches), full re-render of all 11 editions. D1 was NOT disturbed. No other family touched. Nothing pushed/inserted/posted. Full report: `hidden_files/w46/ko-fix-round3/FIX-REPORT.md`.

- R-GLOSS — RESTORE the `가늘다` gloss entry in the P3 gloss line, exactly as pre-fix (reverses the Round 1 D2 deletion, whose "occurs nowhere" premise Round 2 refuted: `가늰` occurs 3× per edition — P3 body, P5 body, P5 exercise 69 option A, key 69 = A — and `가늘다 → 가늰` is a ㄹ-irregular attributive). Restored in `content34.py`, both sides of the `supp_*.py` record pair, and the core `check_core.py` hand list.
  - Before (Round 1 form): `译注｜겹치다 重叠 · 감사하다 感谢 · 나누다 区分、分享。`
  - After (restored, verified verbatim from the rendered P3 SVG gloss band): `译注｜겹치다 重叠 · 가늘다 细 · 감사하다 感谢 · 나누다 区分、分享。`
  - This resolves the Round 1 discrepancy flag in this KIT: the stem DOES occur (as inflected `가늰`); the entry is restored, not deleted.
- D3 — item 54 (P4), stem fix at the core source, key UNCHANGED (`밀렸어요`).
  - Before: `한국시리즈 시작이 하루 ___어요.` → reconstructed `하루 밀렸어요어요` (doubled ending).
  - After: `한국시리즈 시작이 하루 ___.` → reconstructed `한국시리즈 시작이 하루 밀렸어요.` (verified in all 11 renderings).
- D4 — item 103 (P7), stem fix at the core source, key UNCHANGED (`절임배추`).
  - Before: `미리 소금에 절인 배추를 ___이라고 해요.` (ungrammatical: `배추` is vowel-final, quotative must be `라고`).
  - After: `미리 소금에 절인 배추를 ___라고 해요.` → reconstructed `미리 소금에 절인 배추를 절임배추라고 해요.` (verified in all 11 renderings; contrast item 101 `김장이라고`, batchim-final, unchanged).
- Same-class sweep (AST text-read of the build sources, `sweep.py`): all 77 fill-in stems scanned for stem+key doubling — exactly 1 candidate (item 54); all quotative `이라고/라고` usages scanned for final-syllable mismatch — exactly 1 mismatch (item 103) among 3 quotative stems, plus 4 correct prose usages and 1 non-applicable (`'D-7'이라고`, non-Hangul token) reported unscanned-as-defect for Round 3 adjudication. No further candidates; nothing else fixed.
- Keys UNCHANGED: p8.py compare CLEAN 150/150, keydiff [137, 138]; per-edition key-extraction JSONs byte-identical pre-fix vs post-fix (all 150 keys, noted sets identical; keys 54 `밀렸어요` and 103 `절임배추` unchanged everywhere).

Re-gates on the final artifacts (all 11 editions; full logs/JSONs under `hidden_files/w46/ko-fix-round3/gates/`):
- Freeze: core baseline 8/8 SVGs byte-identical; this edition added CJK/Hangul characters vs core: n/a (core baseline). No U+FFFD.
- p8.py: CLEAN 150/150, keydiff [137, 138]. Occlusion audit: 0 flags in all 88 pages, selftest OK. Counts re-measured: 150 exercises, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38. Kinsoku: 0. Koscan reconstruction: CANDIDATES=360 TRUE_SPLITS=0 S3=0 (script preserved at `hidden_files/w46/ko-fix-round3/koscan-round3.py`).
- P3 gloss-box geometry: gloss lines inside their box (top margin 38.5, bottom margin 47.725); occlusion 0. Visual: P3 full frame checked (restored gloss inside its box, no overflow); P4 item 54 / P7 item 103 checked at full frame in the core + spot checks (de P4, ja P7).
- Core `check_core.py` re-run on the final artifacts: exit 0; P7 phrases all verbatim; dates all True; gloss-occurrence diagnostics 19 (was 18 after Round 1) — the +1 is the restored `가늘` hand-list entry, a known naive-substring diagnostic of the same class as the other 18 (dictionary form vs inflected prose form, e.g. `막히`/`막혀`, `가늘`/`가늰`); the KIT adjudication of the `가늘다 → 가늰` pair stands.
- Render: 0 FLOW OVERFLOW / HEAD TOO WIDE. `Lucerna-VOL3-web.pdf` 2528382 bytes (< 7 MB), 8 pages, pdftotext 50756 bytes. `Lucerna-VOL3.pdf` 32011292 bytes, 8 pages, pdftotext 50756 bytes. `2026-w46-ko-zh-cn.text.md` regenerated via `textmd.py` (headers byte-identical to pre-fix, 338 items, 27449 bytes; diff vs pre-fix export is only the restored P3 gloss line).
- Change isolation: hash diff vs the pre-fix snapshot — exactly 9 files changed in this edition (svg/p3, svg/p4, svg/p7, cards p3/p4/p7, print PDF, web PDF, `.text.md`); SVG-text multiset diff — the ONLY string changes are the three fixes (P3 gloss wrap lines, P4 item-54 stem, P7 item-103 stem). No other string changed anywhere.
