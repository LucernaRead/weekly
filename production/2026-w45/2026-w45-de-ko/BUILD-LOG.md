# BUILD-LOG — W45 DE × KO (builder log, consolidated)

Source core (read-only): `files/weekly-report-w45-de-core/` (VOL.2, 150 exercises).
Core build (read-only, copied): `hidden_files/weekly-report-w45-de-build/`.
This build: `hidden_files/weekly-report-w45-de-ko-build/`
(content12/34/56/7/8.py, bslib4.py, svglib.py, run.py, render.py, scratch/).
Delivery: `files/weekly-report-w45-de-ko/` (svg×8, cards×8, print PDF, web PDF,
WEEKLY-KIT.md, ABSTRACT.txt).

## 0. Pre-flight
- No `files/weekly-report-w45-de-ko/` or `hidden_files/weekly-report-w45-de-ko-build/`
  existed; no rendering processes running — proceeded normally.
- `tools/freeze.py baseline` on the core build: 8/8 SVGs byte-identical to shipped core.
- Core SVG SHA-256 recorded before any edit: `scratch/core-svg-hashes-before.txt`
  (p1 6cbd48022b5f863d… p2 9362256dca74f8… p3 3e8a8d16136a46… p4 b787f592599cc4d…
  p5 4dcbeb97c566f4d… p6 01b75ad49a54c803… p7 fbaf8cdd8a90f299… p8 299524bd2ad25ec4d…).
- Re-hash at close: 8/8 OK — core never written.

## 1. Copy + transform
- Copied core build tree; repointed OUT in all five content modules to
  `weekly-report-w45-de-ko` (incl. the `os.path.expanduser("~/…")` spelling).
- `scratch/transform_ko.py`: line-literal replacements only, each asserting ≥1 hit,
  plus residual check. Translates the full Chinese explanation layer to Korean
  (해요체): furniture, section heads, bridges, glosses, box texts, UND SIE
  paragraphs, toolbox, phrase translations, clinic notes, all 150 exercise notes,
  P8 prompts/keys where re-aimed, readers-corner Korean line.
  Final: `RESIDUAL: Han=0, .bridge(=0, forbidden-term=0`.
- Fixes during the transform run: two redundant pairs deleted after failing on
  already-covered identical strings; bare `选出正确答案。` pair moved after all
  page-specific pairs; one missed P7 B1 MC options string added.
- bslib4.py: `bridge` → `expl`; gloss prefix `译注｜` → `해설 — `;
  footer → `Die Lucerna · 독일어 주간지 VOL.2 · 텍스트는 독일어 · 해설은 한국어`
  + `제 {n} 면 / 총 {total} 면`.
- content8.py: P8 note parens full-width → half-width ` ({note})`;
  separator `— 第 {pg} 版 —` → `— 제 {pg} 면 —`;
  answers head → `ANTWORTEN · 모든 정답과 해설 (1–8면)`;
  keys paragraph 14.5/1.3 → 13.0/1.26 (W43 DE×KO precedent).
- content7.py: variable `chinese` → `korean` (3 occurrences).
- render.py copied from core build; PDFs renamed to W45 family convention:
  `Die-Lucerna-VOL2-KO.pdf` (print), `Die-Lucerna-VOL2-KO-web.pdf` (web).

## 2. Build rounds (each re-render preceded by full SVG SHA-256 baseline)
- build1 (scratch/build1.log): 150 exercises, no FLOW OVERFLOW / HEAD TOO WIDE,
  but P7 rail 1595.5 > phrases hline 1508; P8 keys 2670 > 2560;
  P2/P3/P4 col-3 boxes each +29px over fixed elements.
- build2–4 (build2/3/4.log): UND SIE Korean paragraphs shortened to 2 wrapped lines
  each (final P2 `운전하세요? 여러분 나라 기름값은 얼마예요? 독일어로 두 문장 보내 주세요.`;
  P3 `가을에는 여름보다 더 읽나요? 침대 옆에는 무슨 책이 있나요? 독일어로 두 문장 보내 주세요.`;
  P4 `이번 주 응원 팀은 어디예요? 토요일 빅매치 승자는 누구예요? 독일어로 두 문장 보내 주세요.`);
  4 toolbox items shortened to 1 line each; readers-corner Korean line to 3 lines;
  P8 keys font 13.0/1.26. Final geometry: P2 box4 1550.66, P3 TIPP 1583.66,
  P4 col-3 1135.25 (= core values); P7 rail 1449.5; P8 keys 2156.
- build5 (build5.log): P1 Fragen bottom Korean line shortened
  (`독일에서 이번 주 화제가 된 다섯 가지 질문이에요.`) after an occlusion flag
  (ink 1905.5 > box border 1885.0); occlusion re-run 0 flags.
- build6 (build6.log): koscan S3=7 → round-6 note rewordings (7 strings, see KIT §7
  history in scratch) → S3=3.
- build7 (build7.log): round-7 rewordings (3 strings) → S3=1 (`베|를린전이` tail 4).
- build8 (build8.log): round-8 rewordings (3 strings: `모든 성인의 날은 11월 1일` →
  `모든 성인의 날 11월 1일`; `목요일 유로파리그 호펜하임전은 18:45에 시작해요` →
  `목요일 유로파리그 호펜하임전 18:45예요`; `일요일 17:30에 프라이부르크–우니온 베를린전이 시작해요` →
  `일요일 17:30 프라이부르크–우니온전`) → S3=0; also fixes two stranded lone `)` line starts.
- Round baselines: scratch/round2–8-baseline.sha256 (round-8 baseline p8 f968569195c38f…);
  final baseline scratch/final-baseline.sha256 (final p8 b26cf6a1bf11d70f…).

## 3. Final render + final gates (all on build-8 SVGs)
- render-final.log: cards 8× PNG 1950×2700; print PDF 9,590,386 bytes;
  web PDF 4,011,071 bytes (<10 MB); each 8 pages (pypdf).
- freeze-diff-final: added CJK 3,782, Han added 0; German main text frozen except
  adjudicated furniture/explanation items (KIT §1).
- p8-final.txt: CLEAN 150=150, keydiff [137, 138, 139, 150].
- occlusion-final: edition 0, core 0, NEW 0 (selftest passed, 6 classes).
- rowcheck-final.txt: 0 same-baseline pairs <2px; P6 chart-label coverage 0.0%.
- koscan-final.txt: 40 true splits, all tails ≤2, S3=0; line-start closers 1
  (frozen core P6 `%` line); line-start `·` 0; block-final ≤2: 6 (adjudicated).
- gates-final.txt: gloss 25=25; P7 verbatim 2× all 8 + tags; readers corner
  (whitespace-normalized re-check after wrap-line false negatives); furniture vs W43
  measured; images identical (P1 690d06733105c2a7, P4 a08dd48e7fa4071d);
  credits present; 桥接 0; Han 0; VOL.1 0; footer 8/8; PDFs/cards dimensions PASS.
- Interpreter: tools/venv/bin/python, Python 3.12.3, PIL 13.0.0 (run.py and render.py);
  cairosvg 2.9.1; system python3 lacks cairosvg (import fails) — render.py must use
  tools/venv/bin/python.

## 4. Known non-blockers (carried, not defects of this edition)

- Three lone tail-≤2 final lines (`요.` / `아요.`) pass the S3 standard; left as-is
  deliberately (ES×KO precedent treats tail-1/2 as non-issues).
- Core verification debt carries over unchanged: Pflege numbers attributed to ARD
  "Hart aber fair" 26 October (not independently re-verified); B2 count light at
  14/150; 2 photos, not 4.
- If any further P8 note change is needed, keys reflow downstream: re-run koscan,
  p8 compare, and occlusion audit after it — do not assume a local note edit is
  consequence-free.

## 5. Fix round — 独立校对阻塞问题（门 5 S3=6）修复

- 开工查重：files/ 与 build/ 树 90 秒窗口零新写盘（最后写盘为已完成交付），
  无进行中渲染（同期另有一 nl-fr 版 rowcheck 在跑，与本版无关），正常开工。
- 修复前基线：重渲染前现版 8 页 SVG、8 张卡片、双 PDF 完整 sha256 记入
  scratch/fixround-baseline.sha256（p8 b26cf6a1…、印刷 PDF 9,590,386 B /
  b9aa7e30…、网页 PDF 4,011,071 B / c164647a…）。
- 候选措辞先在 /tmp 沙盒副本中模拟验证（沙盒复现与基线逐字节一致；模拟扫描
  复现独立实测 50 处/S3=6），定稿方案落到真实构建树；Q80 曾试“이번 주”前置
  仍 S3，改为上游重排自然归位后原文不动。
- 改动（仅 P8 注文措辞；键全部不动；transform_ko.py 5 条映射同步修正）：
  Q5 `9라운드는 총 9경기예요` → `이번 9라운드는 9경기예요`；
  Q30 `바이에른은 이번 주에도 방학 중이에요` → `이번 주도 바이에른은 방학 중이에요`；
  Q39/Q124 `바덴뷔르템베르크는 방학이 끝났어요` → `이번 주 바덴뷔르템베르크는 방학이 끝났어요`；
  Q74 `크리스마스 공연의 첫 연습` → `올해 크리스마스 공연의 첫 연습`；
  Q80 原文不动（重排后整词落行）；重排新生 S3：Q76 `weil 절에서는 동사가 끝에 와요` →
  `weil 절은 동사가 끝에 와요`。未改德语正文、P7 金句、读者园地、徽章等其他内容；
  未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43。
- 单进程重渲染：run.py → render.py，均为 tools/venv/bin/python（Python 3.12.3，
  PIL 13.0.0；render.py 另 cairosvg 2.9.1），日志 scratch/fixround-render.log，
  零 FLOW OVERFLOW / HEAD TOO WIDE；P8 电池区终点 y=1500、答案流终点 y=2107（≤2560）。
- 改动范围：仅 P8 SVG（db0e2529…）、P8 卡片、双 PDF 变化；P1–P7 SVG 与卡片
  逐字节不变（对照 scratch/fixround-baseline.sha256 vs fixround-after.sha256）。
- 修复后门禁重跑（原始输出见 scratch/ fixround 系列文件）：
  韩语全量扫描（窗口 10–45）真切分 44 处、S3=0（修复前独立实测 50 处/S3=6；
  构建员原“40 处/S3=0”记录订正为 50→44、6→0）；
  p8 compare CLEAN 150=150、keydiff [137, 138, 139, 150]；
  occlusion 分版 0／核心 0／NEW 0（selftest 6 类全触发）；
  freeze 核心 8/8 未变、新增 CJK 3788 全韩文音节、汉字新增 0、removed 字符串集合与终版相同；
  rowcheck 0 旗、P6 图表覆盖 0.0%；gloss 25=25；P7 金句 8×2；8 张卡面目视通过；
  双 PDF 各 8 页（印刷 9,590,456 B / 3e80dce1…、网页 4,011,381 B / 2c855421…）。
- 状态：修复轮完成、仍未定稿、待独立全量复校（SOP §8.4：渲染变化后须另派独立复校）。
