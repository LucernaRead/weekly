# WEEKLY-KIT — 葡萄牙语周报 VOL.3 · PT × ZH-CN（简体中文讲解层，家具版）

- 刊期：2026-W46，2026 年 11 月 9–15 日；仓库 slug：`2026-w46-pt-zh-cn`；目录：`files/weekly-report-w46-pt-zh-cn/`。
- 本版与核心版（`files/weekly-report-w46-pt-core/`）内容完全相同：核心版即简体中文讲解版（W45 先例：核心版以 slug `2026-w46-pt-zh-cn` 入库）。本版仅家具不同（页脚配对说明 + P1 配对徽章），讲解层、正文、练习、答案逐字相同。
- 练习 150 道（A2 49 / B1 70 / B2 31）；范文 88 词；金句 8 条。
- 事实、图片、承诺处理与核心版完全一致，见核心版 KIT（`files/weekly-report-w46-pt-core/WEEKLY-KIT.md`）。

## 家具（本版，与核心版的仅有两处差别）

- P1 副标题（330 行，38pt，沿用核心版）：`葡 萄 牙 语 周 报 · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE`。
- P1 配对徽章（372 行，19.5pt，BRICK，ZH-TW 版式之简体镜像）：`葡萄牙语正文 · 简体中文讲解 — 给简体中文读者的版本`（核心版此行为通用标语）。
- 页脚：`A Lucerna · 葡萄牙语周报 VOL.3 · 正文葡萄牙语 · 讲解简体中文`（核心版页脚为 `A Lucerna · 葡萄牙语周报 VOL.3 · LUCERNA PORTUGUESE WEEKLY`）。
- 页码、Gloss 前缀（`译注｜`）、P7 几何、P8 答案字号、P8 分隔符均沿用核心版。
- 印刷版 PDF：`A-Lucerna-VOL3.pdf`；网页版：`A-Lucerna-VOL3-web.pdf`（tools/webpdf.py，真实文本层）。

## 变换与复现

构建目录：`hidden_files/weekly-report-w46-pt-zh-cn-build/`（由定稿核心构建目录复制）。`transform.py` 仅做 OUT 重定向 + 上述两处家具替换（家具外零改动）。复现命令同英文版 KIT（目录换成本版构建目录，transform.py 仅在全新复制的核心目录上运行一次）。

## 门禁记录

- 构建自检 `gates.py`：17/17 PASS（由 `hidden_files/w46/adapt_gates.py` 生成，cjk-mode skip；注：本版 gates.py 亦有与繁体版相同的手工修正——词表 headword 检查改为去空格比较，因中文按字断行；原 `=` 切分假设不适用于中文词表格式）。
- `tools/occlusion_audit.py`：0 flags。
- `tools/p8.py compare` vs 核心版：CLEAN（150/150；keydiff 为空——家具外零改动）。
- `tools/freeze.py diff` vs 核心版：+1/−1 字串（仅徽章 + 页脚）。
- Web PDF：`A-Lucerna-VOL3-web.pdf` 1,367,192 字节（<7 MB），pdftotext 43,025 字节，含真实文本层。
- 印刷版 PDF：`A-Lucerna-VOL3.pdf` 14,775,653 字节，保留于本目录。
- `.text.md`：`2026-w46-pt-zh-cn.text.md`，与核心版同名文件逐字节相同（内容相同，头行已是简体中文配对说明）。
- ABSTRACT.txt：与核心版逐字节相同（同一内容、同一读者语）。
- 未做 SOP §8 独立第二人校对——仅构建者自检。

## Round 1 校对缺陷修复记录（2026-11-02，fix worker）

- F-4（ABSTRACT.txt 新闻框架）：尾句 `，150 道练习，适合学葡萄牙语的读者通过巴西新闻学葡萄牙语。` → `，以本周话题为素材的 150 道练习。`（练习框架，简体中文）。单行、无 ASCII 双引号、无尾换行（与修复前字节形态一致），含 masthead、A2–B2、150。
- F-5（.text.md 头行）：第 3 行葡萄牙语头行 `Semana de 9 a 15 de novembro de 2026 · Textos em português · Explicações em chinês simplificado · Níveis A2–B2 · 150 exercícios` 经导出参数改为简体中文 `2026 年 11 月 9–15 日 · 正文葡萄牙语 · 讲解简体中文 · 级别 A2–B2 · 150 道练习题`；.text.md 仅此 1 行变化。SVG 8/8 与修复前逐字节相同（hash 已验），未重渲染内容。
- 注意：本版 KIT 原称 .text.md / ABSTRACT.txt 与核心版逐字节相同——F-4/F-5 修复后不再相同（核心版文件为冻结参照与导出源，保留修复前形态，未动）。
- 重建与重门：由核心 build 目录全新复制 + 修复后 transform 重建（`hidden_files/w46/pt-fix/`，日志见该目录 logs/）；构建自检 `gates.py` FAILURES: none，TOTAL 150（A2 49 / B1 70 / B2 31），0 FLOW OVERFLOW / HEAD TOO WIDE。`freeze.py diff` vs 核心版 added CJK 118（仅每页页脚/徽章家具字串，+1/−1）；`p8.py compare` CLEAN 150/150，keydiff 为空；`occlusion_audit.py` 0 flags，selftest OK；P8/P7 全帧目检通过。门禁 JSON/日志见 `hidden_files/w46/pt-fix/gates/`。
- 最终文件：`.text.md` 32515 字节（480 行）；Web PDF 1367191 字节（<7 MB），pdftotext 43025 字节；印刷版 PDF 14775653 字节。
- Round 2 独立校对在后，本修复不替代。
