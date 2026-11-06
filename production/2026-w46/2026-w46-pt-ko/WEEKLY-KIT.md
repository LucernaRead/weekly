# WEEKLY-KIT — 葡萄牙语周报 VOL.3 · PT × KO（韩语讲解层）

- 刊期：2026-W46，2026 年 11 月 9–15 日；仓库 slug：`2026-w46-pt-ko`；目录：`files/weekly-report-w46-pt-ko/`。
- 目标语：葡萄牙语（巴西变体正文，与核心版逐字相同）· 讲解层：韩语（由核心版简体中文讲解层经 transform.py 全量替换；Hangul 为合法讲解文本）。
- 练习 150 道（A2 49 / B1 70 / B2 31；分版与核心版一致）；范文 88 词；金句 8 条与核心版相同（P7 韩文译文 + 页码标签）。
- 事实、图片、承诺处理与核心版完全一致，见核心版 KIT（`files/weekly-report-w46-pt-core/WEEKLY-KIT.md`）：Enem 第二天 + 共和国宣言日假期为主线；P4 次回合赛果未印（截稿注 + 顺延 VOL.4 的开放更新位）；读者来信为编辑部示例 + 双语披露（葡语披露原文保留，中文披露译为韩文）。

## 家具（本版）

- P1 副标题（330 行，38pt）：`포르투갈어 주간지 · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE`（1798px，合框）。
- P1 配对徽章（372 行，19.5pt，BRICK）：`포르투갈어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판`。
- 页脚：`A Lucerna · 포르투갈어 주간지 VOL.3 · 텍스트는 포르투갈어 · 해설은 한국어`；页码：`제 {n} 면 / 총 8 면`。
- Gloss 前缀：`해설 — `；P8 分隔符保留葡语 `— PÁGINA {n} —`。
- svglib 与核心版相同（SC 字体面）。
- 印刷版 PDF：`Lucerna-VOL3-KO.pdf`（无 `A-` 前缀，W45 韩版先例）；网页版：`Lucerna-VOL3-KO-web.pdf`（tools/webpdf.py，真实文本层）。

## 变换与复现

构建目录：`hidden_files/weekly-report-w46-pt-ko-build/`（由定稿核心构建目录复制）。`transform.py` 由核心源稿复现本版源文件（OUT 重定向、家具、INSTR/TYP 标签、全量讲解层替换、disc_cn→disc_ko、词盒垫 +30、P7 几何 gap 30/spacing 94、P6 词表内 `·` 改 `/` 防枚举误切），运行后以 REPL 穷尽检查验明无中文源字面残留。P8 答案沿用核心 13.5pt。复现命令同英文版 KIT（目录换成本版构建目录，transform.py 仅在全新复制的核心目录上运行一次）。

## 门禁记录

- 构建自检 `gates.py`：17/17 PASS（由 `hidden_files/w46/adapt_gates.py` 生成，cjk-mode skip；适配器 `{total}`→`8` 修正已入适配器）。
- `tools/occlusion_audit.py`：0 flags（2 轮修正：P7 金句区溢入预告盒，几何 gap 44→30、spacing 108→94；P6 词表内点号致枚举多计，改 `/`）。
- `tools/p8.py compare` vs 核心版：CLEAN（150/150；keydiff 仅 137/138 两道翻译题，键随读者语重定向，属正常）。
- `tools/freeze.py diff` vs 核心版：仅讲解层 churn（0 条葡语正文改动；新增 CJK 为合法韩文）。
- KO orphan 扫描（窗口 10–45，含括号内片段与行首孤标点，≥3 音节尾判据）：0 缺陷。扫描中发现并修正 3 处：P4 提示句尾 `주세요.`、P5 计划项括号尾、P7 诊所句 `시간|이에요` 3 音节中切；两轮改写曾使断行更差（`주|세요`、`준|비`），已回退/改用更短措辞并重验。残留 1 音节余部（`벼락치|기`、`끝나|고`）与 2 音节余部（`최|고의`）低于 ≥3 音节判据，予以接受并记录。
- Web PDF：`Lucerna-VOL3-KO-web.pdf` 1,173,009 字节（<7 MB），pdftotext 45,676 字节，含真实文本层（最终 SVG 重建）。
- 印刷版 PDF：`Lucerna-VOL3-KO.pdf` 7,072,555 字节，保留于本目录。
- `.text.md`：`2026-w46-pt-ko.text.md`，由核心版 .text.md 经 transform 表 + 头行/示例句替换导出（`hidden_files/w46/derive_textmd.py`，allow_cjk=1），已验无汉字残留行。
- ABSTRACT.txt：韩文单行，无 ASCII 双引号，含 masthead、目标语、A2–B2、150 题与真实话题。
- 未做 SOP §8 独立第二人校对——仅构建者自检。

## Round 1 校对缺陷修复记录（2026-11-02，fix worker）

- F-1（P8 答案注全角冒号）：10 条注 `conferir：ele` 等（16/17/18/19/20/56/57/58/102/103 项）中的 U+FF1A（：）改为 ASCII `:`，如 `16. confere — conferir：ele → confere` → `16. confere — conferir: ele → confere`。修复位置：分版 transform.py 新增 §5c 块，10 条精确 sub() 替换（核心 register 未动，故 CJK 版保留 ：）。SVG 全量 FF1A=0，P8 10/10 ASCII 冒号已验。
- F-3（P7 孤立 。 节点）：删除 P7 诊所句后的独立 。 文本节点，句末改 ASCII `.`：`공휴일이 일요일에 겹쳐도 월요일에 쉬지 않아요。`（+ 孤节点）→ 单节点 `공휴일이 일요일에 겹쳐도 월요일에 쉬지 않아요.`。修复位置：分版 transform.py 新增带 。 的诊所 REPL 条目 + §5d 几何块（仅诊所 gloss 的 wrap/para 由 CW−44 放宽至 CW−40，右 margin 22px→18px，仍在框内；其余三条 gloss 断行经模拟验证不变）。重建后 P7 U+3002=0（P1 保留 1 处合法 gloss `proclamação = 선포（공화국 선포）。`）；.text.md 。 3→2（仅第 371 行变化）。
- 重建与重门：由核心 build 目录全新复制 + 修复后 transform 重建（`hidden_files/w46/pt-fix/`，日志见该目录 logs/）；构建自检 `gates.py` FAILURES: none，TOTAL 150（A2 49 / B1 70 / B2 31），0 FLOW OVERFLOW / HEAD TOO WIDE。`freeze.py diff` vs 核心版 added CJK 3140（合法韩文讲解层）；`p8.py compare` CLEAN 150/150，keydiff [137,138]（翻译重定向，属正常）；`occlusion_audit.py` 0 flags，selftest OK；P8/P7 全帧目检通过。门禁 JSON/日志见 `hidden_files/w46/pt-fix/gates/`。
- 最终文件：`.text.md` 33281 字节（480 行）；Web PDF 1172271 字节（<7 MB），pdftotext 45663 字节；印刷版 PDF 7072429 字节。
- Round 2 独立校对在后，本修复不替代。
