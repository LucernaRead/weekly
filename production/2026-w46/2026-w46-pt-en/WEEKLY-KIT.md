# WEEKLY-KIT — 葡萄牙语周报 VOL.3 · PT × EN（英语讲解层）

- 刊期：2026-W46，2026 年 11 月 9–15 日；仓库 slug：`2026-w46-pt-en`；目录：`files/weekly-report-w46-pt-en/`。
- 目标语：葡萄牙语（巴西变体正文，与核心版逐字相同）· 讲解层：英语（由核心版简体中文讲解层经 transform.py 全量替换）。
- 练习 150 道（A2 49 / B1 70 / B2 31；分版与核心版一致）；范文 88 词；金句 8 条与核心版相同（P7 英文译文 + 页码标签）。
- 事实、图片、承诺处理与核心版完全一致，见核心版 KIT（`files/weekly-report-w46-pt-core/WEEKLY-KIT.md`）：Enem 第二天 + 共和国宣言日假期为主线；P4 次回合赛果未印（截稿注 + 顺延 VOL.4 的开放更新位）；读者来信为编辑部示例 + 双语披露（葡语披露原文保留，中文披露译为英文）。

## 家具（本版）

- P1 副标题（330 行，35pt，经实测定宽）：`PORTUGUESE WEEKLY · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE`（38pt 会溢出页框，实测 1939px → 改 35pt，1786px）。
- P1 配对徽章（372 行，19pt，OLIVE）：`TEXT IN PORTUGUESE · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS`。
- 页脚：`A Lucerna · VOL.3 · Text in Portuguese · Explanations in English`；页码：`Page {n} of 8`。
- Gloss 前缀：`Note | `；P8 分隔符保留葡语 `— PÁGINA {n} —`。
- 印刷版 PDF：`A-Lucerna-VOL3.pdf`；网页版：`A-Lucerna-VOL3-web.pdf`（tools/webpdf.py，真实文本层）。

## 变换与复现

构建目录：`hidden_files/weekly-report-w46-pt-en-build/`（由定稿核心构建目录复制）。`transform.py` 由核心源稿复现本版源文件（OUT 重定向、家具、INSTR/TYP 标签、全量讲解层替换、disc_cn→disc_en、版式修正），运行后源文件零 CJK 残留（已验）。复现：

```
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-pt-en-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python transform.py  # 仅在全新复制的核心目录上运行一次
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python gates.py
```

注：transform.py 含两处事后补丁（已并入 transform，复现时自动生效）：补 2 条漏译 literal（第 2 天在 11 月 15 日；确认卡是高考的文件）；§5b 版式修正（见下）。

## 门禁记录

- 构建自检 `gates.py`：17/17 PASS（含 P1 徽章、页脚 8/8、零 CJK、金句 2×、披露逐字、P7 金句区 clearance）。
- `tools/occlusion_audit.py`：0 flags（初版 8 flags 已修：P1 数字盒标题改 tsize=20；P7 来信盒加高致金句撞预告框——缩短示例标签、盒底垫 35→22、fy 间隙 44→30、金句间距 108→94，复查 0 flags）。
- `tools/p8.py compare` vs 核心版：CLEAN（150/150；keydiff 仅 137/138 两道翻译题，键随读者语重定向，属正常）。
- `tools/freeze.py diff` vs 核心版：仅讲解层 churn，added CJK 0。
- Web PDF：`A-Lucerna-VOL3-web.pdf` 893,279 字节（<7 MB），pdftotext 44,326 字节，含真实文本层。
- 印刷版 PDF：`A-Lucerna-VOL3.pdf` 3,489,960 字节，保留于本目录。
- `.text.md`：`2026-w46-pt-en.text.md`，由核心版 .text.md 经 transform 表 + 头行/示例句替换导出（`hidden_files/w46/derive_textmd.py`），零 CJK，已验。
- ABSTRACT.txt：英文单行，无 ASCII 双引号，含 masthead、目标语、A2–B2、150 题与真实话题。
- 未做 SOP §8 独立第二人校对——仅构建者自检。

## Round 1 校对缺陷修复记录（2026-11-02，fix worker）

- F-1（P8 答案注全角冒号）：10 条注 `conferir：ele` 等（16/17/18/19/20/56/57/58/102/103 项）中的 U+FF1A（：）改为 ASCII `:`，如 `16. confere — conferir：ele → confere` → `16. confere — conferir: ele → confere`。修复位置：分版 transform.py 新增 §5c 块，10 条精确 sub() 替换（核心 register 未动，故 CJK 版保留 ：）。SVG 全量 FF1A=0，P8 10/10 ASCII 冒号已验。
- F-2（P7 诊所第 4 项句尾全角句号）：transform REPL 表新增带 。 的条目（裸条目保留，处理 P2 练习/P8 答案无句号的情形；时刻表条目同法），诊所句 `The holiday falls on a Sunday, with no Monday off。` → `The holiday falls on a Sunday, with no Monday off.`。SVG 全量 U+3002=0；重导出的 .text.md 仅第 36、371 行变化（。→ .），其余 478 行逐行相同。
- 构建器复现缺陷（非内容改动）：分版 transform.py §5b 断言要求长版编辑示例标签出现 2 次，但 REPL 表已输出短版标签，计数恒为 0，新推导永不过。暂存版 transform 将该断言放宽为 `in (0, 2)`，替换本身为 no-op，§5b 几何编辑照常执行。
- 重建与重门：由核心 build 目录全新复制 + 修复后 transform 重建（`hidden_files/w46/pt-fix/`，日志见该目录 logs/）；构建自检 `gates.py` FAILURES: none，TOTAL 150（A2 49 / B1 70 / B2 31），0 FLOW OVERFLOW / HEAD TOO WIDE。`freeze.py diff` vs 核心版 added CJK 0；`p8.py compare` CLEAN 150/150，keydiff [137,138]（翻译重定向，属正常）；`occlusion_audit.py` 0 flags，selftest OK；P8/P7 全帧目检通过。门禁 JSON/日志见 `hidden_files/w46/pt-fix/gates/`。
- 最终文件：`.text.md` 33031 字节（480 行）；Web PDF 891340 字节（<7 MB），pdftotext 44314 字节；印刷版 PDF 3489843 字节。
- Round 2 独立校对在后，本修复不替代。
