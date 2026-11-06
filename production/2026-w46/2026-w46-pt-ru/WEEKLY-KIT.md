# WEEKLY-KIT — 葡萄牙语周报 VOL.3 · PT × RU（俄语讲解层）

- 刊期：2026-W46，2026 年 11 月 9–15 日；仓库 slug：`2026-w46-pt-ru`；目录：`files/weekly-report-w46-pt-ru/`。
- 目标语：葡萄牙语（巴西变体正文，与核心版逐字相同）· 讲解层：俄语（由核心版简体中文讲解层经 transform.py 全量替换）。
- 练习 150 道（A2 49 / B1 70 / B2 31；分版与核心版一致）；范文 88 词；金句 8 条与核心版相同（P7 俄文译文 + 页码标签）。
- 事实、图片、承诺处理与核心版完全一致，见核心版 KIT（`files/weekly-report-w46-pt-core/WEEKLY-KIT.md`）：Enem 第二天 + 共和国宣言日假期为主线；P4 次回合赛果未印（截稿注 + 顺延 VOL.4 的开放更新位）；读者来信为编辑部示例 + 双语披露（葡语披露原文保留，中文披露译为俄文）。

## 家具（本版）

- P1 副标题（330 行，30pt）：`ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE`（1757px，合框）。
- P1 配对徽章（372 行，19pt，GREY 非粗体——W45 俄版先例）：`ТЕКСТЫ НА ПОРТУГАЛЬСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ`。
- 页脚：`A Lucerna · ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА ПОРТУГАЛЬСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ`；页码：`Страница {n} из 8`。
- Gloss 前缀：`Пояснение — `；P8 分隔符保留葡语 `— PÁGINA {n} —`。
- 印刷版 PDF：`A-Lucerna-VOL3.pdf`；网页版：`A-Lucerna-VOL3-web.pdf`（tools/webpdf.py，真实文本层）。

## 变换与复现

构建目录：`hidden_files/weekly-report-w46-pt-ru-build/`（由定稿核心构建目录复制）。`transform.py` 由核心源稿复现本版源文件（OUT 重定向、家具、INSTR/TYP 标签、全量讲解层替换、disc_cn→disc_ru、P8 答案 13pt、词盒垫 +30、P7 几何 gap 14/spacing 88/垫 22），运行后源文件零 CJK 残留（已验）。复现命令同英文版 KIT（目录换成本版构建目录，transform.py 仅在全新复制的核心目录上运行一次）。

## 门禁记录

- 构建自检 `gates.py`：17/17 PASS（含 P1 徽章、页脚 8/8、零 CJK、金句 2×、披露逐字、P7 金句区 clearance）。
- `tools/occlusion_audit.py`：0 flags（1 轮修正：P1 顶条俄文过长与右侧日期行同基线相撞 52.1px，顶条改短为 `TODA SEMANA EM PORTUGUÊS · ТО, ЧТО ЧИТАЕТ БРАЗИЛИЯ`，614px）。
- `tools/p8.py compare` vs 核心版：CLEAN（150/150；keydiff 仅 137/138 两道翻译题，键随读者语重定向，属正常）。
- `tools/freeze.py diff` vs 核心版：仅讲解层 churn，added CJK 0。
- Web PDF：`A-Lucerna-VOL3-web.pdf` 924,653 字节（<7 MB），pdftotext 53,270 字节，含真实文本层。
- 印刷版 PDF：`A-Lucerna-VOL3.pdf` 3,291,569 字节，保留于本目录。
- `.text.md`：`2026-w46-pt-ru.text.md`，由核心版 .text.md 经 transform 表 + 头行/示例句替换导出（`hidden_files/w46/derive_textmd.py`），零 CJK，已验。
- ABSTRACT.txt：俄文单行，无 ASCII 双引号，含 masthead、目标语、A2–B2、150 题与真实话题。
- 未做 SOP §8 独立第二人校对——仅构建者自检。

## Round 1 校对缺陷修复记录（2026-11-02，fix worker）

- F-1（P8 答案注全角冒号）：10 条注 `conferir：ele` 等（16/17/18/19/20/56/57/58/102/103 项）中的 U+FF1A（：）改为 ASCII `:`，如 `16. confere — conferir：ele → confere` → `16. confere — conferir: ele → confere`。修复位置：分版 transform.py 新增 §5c 块，10 条精确 sub() 替换（核心 register 未动，故 CJK 版保留 ：）。SVG 全量 FF1A=0，P8 10/10 ASCII 冒号已验。
- F-2（P7 诊所第 4 项句尾全角句号）：transform REPL 表新增带 。 的条目（裸条目保留，处理 P2 练习/P8 答案无句号的情形；时刻表条目同法），诊所句 `Праздник выпадает на воскресенье, в понедельник выходного нет。` → `Праздник выпадает на воскресенье, в понедельник выходного нет.`。SVG 全量 U+3002=0；重导出的 .text.md 仅第 36、371 行变化（。→ .），其余 478 行逐行相同。
- 重建与重门：由核心 build 目录全新复制 + 修复后 transform 重建（`hidden_files/w46/pt-fix/`，日志见该目录 logs/）；构建自检 `gates.py` FAILURES: none，TOTAL 150（A2 49 / B1 70 / B2 31），0 FLOW OVERFLOW / HEAD TOO WIDE。`freeze.py diff` vs 核心版 added CJK 0；`p8.py compare` CLEAN 150/150，keydiff [137,138]（翻译重定向，属正常）；`occlusion_audit.py` 0 flags，selftest OK；P8/P7 全帧目检通过。门禁 JSON/日志见 `hidden_files/w46/pt-fix/gates/`。
- 最终文件：`.text.md` 34946 字节（480 行）；Web PDF 923066 字节（<7 MB），pdftotext 53258 字节；印刷版 PDF 3291447 字节。
- Round 2 独立校对在后，本修复不替代。
