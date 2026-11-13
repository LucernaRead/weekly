# it-ko — RECORD (build1, 2026-11-11)

## Gates — build1, `ko/gates1.log`, GATES ALL PASS (first attempt)
- run.py rc 0, 150 exercises, zero FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE; flow ends P1-headline col 2/2 y=1311 (bottom 1828), P8-ex col 3/3 y=941 (bottom 1332), P8-keys col 3/3 y=2499 (bottom 2552, 53 px spare), P7 col3 1673.0
- occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff [137,138,139]); freeze fragments 0 unexplained; freeze baseline direct sha256 8/8
- print/web text multiset identical (7,425 words each; chars equal); web < 7 MB; P8 min font 13.0 px = 9.75 pt
- §1.1 scans pass; VOL.5 = 3 legitimate nodes (same as core); textmd validate 0/0; keys match (except 137–139 + writing); notes match translations.py (table_gaps empty)
- P8 chip check: Q113–120, Q145–149, Q150 all B1, = core 1:1 (same coordinates as core except Q150, y=616 vs core y=586 — same as ja; badge present at (1457, 615))
- No strict-CJK check for ko (reader values are themselves CJK)

## Build history — 1 build
- Pre-build measurements (probe svglib built from core-it + KR index patch, `ko/svglib_probe.py` — note: the probe needs `ko/assets/lucerna-moth.svg` copied next to it because svglib resolves the moth asset relative to its own file): match_set instr "단어와 뜻을 연결하세요" 190.3 px (budget 254.5) OK; P4 E TU 2 lines OK; P7 error notes all 1 line (Lazio 326.7, Torrone 326.7, andare 304.2, probabile 339.9); P7 disclosure 4 lines (1202.8 px) → shortened; P7 gloss 2 lines OK; P1 cifre 2+2+3+2 = 9 lines → 2+2+2+2 = 8 (20.45 shortened); P1 bridge 2 lines (784.4 px); FRASI all 1L+1L (slots ~97 px vs 158); P8 estimate (fr→ko mapping, SERIF 13 in 422.5 px) 2 two-liners (44, 134), total 4533.3 px vs 4576 capacity.
- 3 pre-build edits in translations.py (each count-asserted 1×): disclosure → C3 "이것은 편집부의 예시이며 실제 편지가 아닙니다. 실제 편지와 최우수 작문이 도착하지 않았습니다. 약속은 VOL.5로 이어집니다。" (1047.2 px, 3 lines — the minimal C1 form dropping only "이것은" still measured 4 lines at 1142.0 px, 6.5 px over; C3 drops "마감 시점까지" + "8면 " and keeps all three facts); cifre 20.45 → D2 "20.45 — 아탈란타-인터 킥오프, 일요일 11월 22일（20:45）" (533.1 px, 2 lines — the unedited value wrapped to 3 lines at 755.7 px because the closing fullwidth paren spilled onto a third line); P8 44/134 note → "주어 + 동사" (PRE-EMPTIVE, ja lesson — the ja build1 P8-keys ended 2561, 9 px over, from column-break waste the sum-of-advances estimate ignores; the same fix after the fact cost ja a rebuild). translations.py 149,258 → 149,162 bytes, still 239 entries.
- Build1 (~191 s — much faster than ja's ~402 s; the KR svglib wraps faster than the JP one with the kinsoku port): run.py rc 0, 150 exercises, writing_type "쓰기". P8-keys ends 2499/2552 (53 px spare). Gates1: GATES ALL PASS on the first run. No rebuild needed.
- No tool fixes in this shift — the ja-shift fixes carried over (build_edition.py CJK-reader residual check, occlusion_audit.py transform stack, gates.py adjacent-pair rule). The ko build exercised all three and passed first attempt.
- Re-aimed ko keys (from build_edition.py tr() of the Chinese sources): 137 "성모 건강 축일에는 사람들이 서원의 다리를 건넌다." / "원문과 비교하세요"; 138 "일요일 저녁, 아탈란타가 인터와 경기한다." / "si gioca = 경기가 있다"; 139 "토요일, 라치오는 홈에서 레체와 경기한다." / "in casa = 홈에서"; 140 stem "모든 숫자는 분명해야 합니다. → ___" / "dovere = ~해야 한다".

## Visual — 8/8 cards viewed (build1), zero defects
- P1: masthead band starts x=133.2, both margins clean; cifre box 2-line items clean; bridge 2 lines OK; footer "제 1 면 / 총 8 면".
- P2: "단어와 뜻을 연결하세요" instr fits; E TU box reader question fits ("서원의 다리를 건너거나 나무를 심어 본 적이 있나요? 이탈리아어로 두 문장을 써서 편집부에 보내세요.").
- P3: E TU box clean ("토로네와 초콜릿 중 어느 쪽이 더 좋나요? 두 문장을 써서 보내세요."); word box wraps after 'corteo ·' (same as core, second line "rievocazione · tartufo · mandorle").
- P4: E TU box ends flush with the table header at 1140.45 = core ("일요일 저녁에 어느 경기를 볼 건가요? 이탈리아어로 두 문장을 써서 보내세요." 2 lines); match_set instr fits; results table clean.
- P5: clean (structural mid-page whitespace is the core pattern); word list wraps after 'incontro' (second line starts with '·' — same words, different break, as in ja).
- P6: clean — practice bar chart + "연습용 최저 기온 예시" box + Q83–100.
- P7: error notes 1 line each; disclosure 3 lines ends 1673.0, clear of the FRASI hline; LA PAROLA gloss 2 lines ("vetta = 선두. 이번 주 1면과 4면을 보세요: 라치오가 29점으로 선두."); B2 bridge 3 lines, fits; Dante image; FRASI 8 quotes with translations.
- P8: Q113–120 B1 badges; 141–144 "단어와 뜻을 연결하세요" fits, no graze; RISPOSTE 1–150 all present; Q44/134 now 1 line each ("주어 + 동사"); Q137/138/139 wrap to 2 lines each (fit, flow ends 2499/2552); Q135 1 line ("A che ora gioca la Lazio? — 의문어구는 문장 맨 앞에"); Q149/Q150 separate lines; "150. ✓ 모범 답안은 이 면 H 구역에（99단어)".

## Self-read — full .text.md (1317 lines), all 150 keys re-verified
- Korean explanation layer throughout; the only non-Korean CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent, 4 occurrences) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK).
- Spot checks: Q22 A (1630년의 서원); Q29 B; Q32 A "Fate dolci" (curly quotes — the translations.py ko value verbatim, same as nl); Q44/134 note "주어 + 동사"; Q45 note "장소가 먼저, 주어가 뒤에"; Q51 B (일요일 저녁); Q58 "più + bella: 일요일 저녁이 가장 좋다（주관적 평가）"; Q59 meglio; Q66 B (11월 23일); Q81 Vero; Q82 Falso; Q85 B (13−11=2); Q86 A (6+7=13); Q87 "차트 수치는 연습용 자료이며 실제 예보가 아닙니다"; Q92 B (+0.8%); Q120 B (11월 24일); Q135 note "의문어구는 문장 맨 앞에"; Q136 note "주어 + 동사 + 장소"; Q137–140 re-aimed.
- Model text 99 words frozen. Disclosure 3-line version in P7 LETTERE (ko): "이것은 편집부의 예시이며 실제 편지가 아닙니다. 실제 편지와 최우수 작문이 도착하지 않았습니다. 약속은 VOL.5로 이어집니다。"

## Quota stops on this shift: NONE. Core-it untouched.

---

## Re-fan-out (2026-11-11)
- Rebuilt from core-it fix3 (36bdec2e) by build_edition.py, RC=0 first attempt; text.md 57,347 bytes, 1317 lines, 150 exercises.
- Gates: 19/19 PASS, 0 FAIL (`scratch-refanout-it/gates-ko.log`); P8-keys flow ends y=2499 (bottom 2552); freeze baseline re-taken 8/8 (this dir's baseline is the re-fan-out one; first-fan-out baseline preserved in `scratch-refanout-it/prev-fanout/ko/`).
- fix3 9 lines + E labels + table values verified by `scratch-refanout-it/check_refanout.py` (ALL PASS); sim cross-check 0 unexpected changes.
- KIT updated with the new SHAs + §11 (see the edition dir). Full report: `scratch-refanout-it/FANOUT-REPORT-it.md`.
