# WEEKLY-KIT — 葡萄牙语周报 VOL.3 · PT × JA（日语讲解层）

- 刊期：2026-W46，2026 年 11 月 9–15 日；仓库 slug：`2026-w46-pt-ja`；目录：`files/weekly-report-w46-pt-ja/`。
- 目标语：葡萄牙语（巴西变体正文，与核心版逐字相同）· 讲解层：日语（由核心版简体中文讲解层经 transform.py 全量替换；CJK 文字为合法讲解文本）。
- 练习 150 道（A2 49 / B1 70 / B2 31；分版与核心版一致）；范文 88 词；金句 8 条与核心版相同（P7 日文译文 + 页码标签）。
- 事实、图片、承诺处理与核心版完全一致，见核心版 KIT（`files/weekly-report-w46-pt-core/WEEKLY-KIT.md`）：Enem 第二天 + 共和国宣言日假期为主线；P4 次回合赛果未印（截稿注 + 顺延 VOL.4 的开放更新位）；读者来信为编辑部示例 + 双语披露（葡语披露原文保留，中文披露译为日文）。

## 家具（本版）

- P1 副标题（330 行，36pt）：`ポ ル ト ガ ル 語 週 刊 · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE`（1765px，合框）。
- P1 配对徽章（372 行，19.5pt，BRICK）：`ポルトガル語テキスト · 日本語の解説 — 日本語読者のための版`。
- 页脚：`A Lucerna · ポルトガル語週刊 VOL.3 · 本文はポルトガル語 · 解説は日本語`；页码：`{n} ページ（全 8 ページ）`。
- Gloss 前缀：`解説 — `；P8 分隔符为日语 `— {n} ページ —`（W45 日版先例）。
- svglib：由 W45 pt-ja 构建目录复制（JP 字体 + kinsoku NO_START/接缝修复），与核心版 svglib 差异仅字体面与 kinsoku 块。
- 印刷版 PDF：`A-Lucerna-VOL3-JA.pdf`；网页版：`A-Lucerna-VOL3-JA-web.pdf`（tools/webpdf.py，真实文本层）。

## 变换与复现

构建目录：`hidden_files/weekly-report-w46-pt-ja-build/`（由定稿核心构建目录复制）。`transform.py` 由核心源稿复现本版源文件（OUT 重定向、家具、INSTR/TYP 标签、全量讲解层替换、disc_cn→disc_ja、词盒垫 +30），运行后以 REPL 穷尽检查验明无中文源字面残留（同形/前缀译文除外，已逐项裁定）。P7 几何沿用核心值（gap 44/spacing 108/垫 35），P8 答案沿用核心 13.5pt。复现命令同英文版 KIT（目录换成本版构建目录，transform.py 仅在全新复制的核心目录上运行一次）。

## 门禁记录

- 构建自检 `gates.py`：17/17 PASS（由 `hidden_files/w46/adapt_gates.py` 生成，cjk-mode skip；注：适配器初版把 `{total}` 写入 f-string 致 NameError，已修适配器并重写本版 gates.py 为字面 `8`）。
- `tools/occlusion_audit.py`：0 flags。
- `tools/p8.py compare` vs 核心版：CLEAN（150/150；keydiff 仅 137/138 两道翻译题，键随读者语重定向，属正常）。
- `tools/freeze.py diff` vs 核心版：仅讲解层 churn（320 删/335 增字串，0 条葡语正文改动；新增 CJK 为合法日文）。
- Kinsoku 行首检查：0 违规（无行首禁则符号）。
- Web PDF：`A-Lucerna-VOL3-JA-web.pdf` 1,497,357 字节（<7 MB），pdftotext 45,872 字节，含真实文本层。
- 印刷版 PDF：`A-Lucerna-VOL3-JA.pdf` 15,687,617 字节，保留于本目录（JP 字体嵌入所致，核心版印刷版 14.7 MB 同量级）。
- `.text.md`：`2026-w46-pt-ja.text.md`，由核心版 .text.md 经 transform 表 + 头行/示例句替换导出（`hidden_files/w46/derive_textmd.py`，allow_cjk=1），已验无简体中文残留行。
- ABSTRACT.txt：日文单行，无 ASCII 双引号，含 masthead、目标语、A2–B2、150 题与真实话题。
- 未做 SOP §8 独立第二人校对——仅构建者自检。

## Round 1 校对后未改动验证记录（2026-11-02）

- 本版 Round 1 PASS，未重渲染、未修改。修复工 hash 复核：全部制品与修复前快照一致；核心 build 目录未动。
- 合法 CJK 标点保留已验：P8 10 条答案注 10/10 全角冒号 ：；SVG 全量 FF1A=54、U+3002=70（含 P8 42 处 ：），.text.md FF1A=8、U+3002=49。未重跑三门禁（制品未变）。
