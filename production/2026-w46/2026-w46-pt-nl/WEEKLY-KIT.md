# WEEKLY-KIT — 葡萄牙语周报 VOL.3 · PT × NL（荷兰语讲解层）

- 刊期：2026-W46，2026 年 11 月 9–15 日；仓库 slug：`2026-w46-pt-nl`；目录：`files/weekly-report-w46-pt-nl/`。
- 目标语：葡萄牙语（巴西变体正文，与核心版逐字相同）· 讲解层：荷兰语（由核心版简体中文讲解层经 transform.py 全量替换）。
- 练习 150 道（A2 49 / B1 70 / B2 31；分版与核心版一致）；范文 88 词；金句 8 条与核心版相同（P7 荷兰文译文 + 页码标签）。
- 事实、图片、承诺处理与核心版完全一致，见核心版 KIT（`files/weekly-report-w46-pt-core/WEEKLY-KIT.md`）：Enem 第二天 + 共和国宣言日假期为主线；P4 次回合赛果未印（截稿注 + 顺延 VOL.4 的开放更新位）；读者来信为编辑部示例 + 双语披露（葡语披露原文保留，中文披露译为荷兰文）。

## 家具（本版）

- P1 副标题（330 行，34pt，经实测定宽）：`PORTUGEES WEEKBLAD · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE`（1763px，合框）。
- P1 配对徽章（372 行，19pt，BRICK）：`TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`。
- 页脚：`A Lucerna · PORTUGEES WEEKBLAD VOL.3 · TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS`；页码：`Pagina {n} van 8`。
- Gloss 前缀：`Uitleg — `；P8 分隔符保留葡语 `— PÁGINA {n} —`。
- 印刷版 PDF：`A-Lucerna-VOL3.pdf`；网页版：`A-Lucerna-VOL3-web.pdf`（tools/webpdf.py，真实文本层）。

## 变换与复现

构建目录：`hidden_files/weekly-report-w46-pt-nl-build/`（由定稿核心构建目录复制）。`transform.py` 由核心源稿复现本版源文件（OUT 重定向、家具、INSTR/TYP 标签、全量讲解层替换、disc_cn→disc_nl、版式修正），运行后源文件零 CJK 残留（已验）。复现命令同英文版 KIT（目录换成本版构建目录，transform.py 仅在全新复制的核心目录上运行一次）。

## 门禁记录

- 构建自检 `gates.py`：17/17 PASS（含 P1 徽章、页脚 8/8、零 CJK、金句 2×、披露逐字、P7 金句区 clearance）。
- `tools/occlusion_audit.py`：0 flags（2 轮修正：来信盒底垫 12→22 防擦框；P2 栏头 `PARA NÃO ERRAR · EZELSBRUGGETJE` 超框改 `PARA NÃO ERRAR · EZELSBRUG`——注：该栏头在 content12.py（P2 在 content12 模块），初次补丁误改 content34.py 未生效，已纠正）。
- `tools/p8.py compare` vs 核心版：CLEAN（150/150；keydiff 仅 137/138 两道翻译题，键随读者语重定向，属正常）。
- `tools/freeze.py diff` vs 核心版：仅讲解层 churn，added CJK 0。
- Web PDF：`A-Lucerna-VOL3-web.pdf` 897,875 字节（<7 MB），pdftotext 45,005 字节，含真实文本层（最终 SVG 重建）。
- 印刷版 PDF：`A-Lucerna-VOL3.pdf` 3,527,944 字节，保留于本目录。
- `.text.md`：`2026-w46-pt-nl.text.md`，由核心版 .text.md 经 transform 表 + 头行/示例句替换导出（`hidden_files/w46/derive_textmd.py`），零 CJK，已验。
- ABSTRACT.txt：荷兰文单行，无 ASCII 双引号，含 masthead、目标语、A2–B2、150 题与真实话题。
- 未做 SOP §8 独立第二人校对——仅构建者自检。

## Round 1 校对缺陷修复记录（2026-11-02，fix worker）

- F-1（P8 答案注全角冒号）：10 条注 `conferir：ele` 等（16/17/18/19/20/56/57/58/102/103 项）中的 U+FF1A（：）改为 ASCII `:`，如 `16. confere — conferir：ele → confere` → `16. confere — conferir: ele → confere`。修复位置：分版 transform.py 新增 §5c 块，10 条精确 sub() 替换（核心 register 未动，故 CJK 版保留 ：）。SVG 全量 FF1A=0，P8 10/10 ASCII 冒号已验。
- F-2（P7 诊所第 4 项句尾全角句号）：transform REPL 表新增带 。 的条目（裸条目保留，处理 P2 练习/P8 答案无句号的情形；时刻表条目同法），诊所句 `De feestdag valt op zondag, maandag geen inhaal。` → `De feestdag valt op zondag, maandag geen inhaal.`。SVG 全量 U+3002=0；重导出的 .text.md 仅第 36、371 行变化（。→ .），其余 478 行逐行相同。
- 重建与重门：由核心 build 目录全新复制 + 修复后 transform 重建（`hidden_files/w46/pt-fix/`，日志见该目录 logs/）；构建自检 `gates.py` FAILURES: none，TOTAL 150（A2 49 / B1 70 / B2 31），0 FLOW OVERFLOW / HEAD TOO WIDE。`freeze.py diff` vs 核心版 added CJK 0；`p8.py compare` CLEAN 150/150，keydiff [137,138]（翻译重定向，属正常）；`occlusion_audit.py` 0 flags，selftest OK；P8/P7 全帧目检通过。门禁 JSON/日志见 `hidden_files/w46/pt-fix/gates/`。
- 最终文件：`.text.md` 33126 字节（480 行）；Web PDF 895921 字节（<7 MB），pdftotext 44993 字节；印刷版 PDF 3527841 字节。
- Round 2 独立校对在后，本修复不替代。

## D5 交付物 pin（2026-11-15，run2 实测）

- 印刷版 PDF：`A-Lucerna-VOL3-pt-nl.pdf`，2282512 字节，SHA-256 `e27e087f9a85f9c8ce87d1ee7c8ec7a258a444cf9e3efca593d3e51f8deade8a`。
- 网页版 PDF：`2026-w46-pt-nl.web.pdf`，763880 字节（<7 MB），SHA-256 `32aeb2d93b140cc9bc5e7db903b46aafb1662efd88efec8d6fd09ae61ace9d35`。
- `.text.md`：`2026-w46-pt-nl.text.md`（run2 carry-over，与 `issues/` 已发版 BYTE-IDENTICAL），33121 字节，SHA-256 `c702ef2bcd4fbd456fe401530c65cf7533535ce3bdbe5b5d86d53fdb1abeb471`。
- 网 PDF 非确定性：以上为终轮实测值，closer 拷 builder 原件，勿重跑 webpdf。

## D5 rebuild (2026-11-15, D5-only)

- 装机：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target pt --reader nl --week 2026-w46`（先 `--check` 干跑，全干净）。模式 latin；`_D5_READER = "latin"`（`svglib.py:100`）；`test_d5_routing.py` **FAILURES: 0**；fix2 保留（`_QUOTE_CLS` ×4）。未跑 `--patch-core`（D40：builder 永不写 production；closer 从 `patched/` 同步）。
- 修前 D5 普查（基线）：Latin 500、Cyrillic 0、curly_in_cjk 0（`d5_census`）；修后全 0（G3）。
- 修复（只降字号，探针：SVG 实测墨宽线性缩放、取留 ≥2px 余量的最大适配字号）：
- content12.py:48 `], tsize=20)` → `], tsize=18.5)`（数字盒标题 `A SEMANA EM NÚMEROS　IN CIJFERS`，探针余量 3.2px）
- content12.py:89 `NESTA EDIÇÃO　IN DEZE EDITIE` 24 → 21pt（探针余量 9.5px；D47：`###` 行自导出丢失，见 D5 节）
- content12.py:131 `EM POUCAS PALAVRAS　KORTOM` 24 → 20pt（探针余量 8.0px；D47：`###` 行自导出丢失，见 D5 节）
- content7.py:84 `A PALAVRA　WOORD VAN DE WEEK` 23 → 19pt（探针余量 10.9px）
- content12.py:255 `e.head("C　COMPLETE COM OS NÚMEROS", 25)` → 22.5pt（探针余量 8.6px）
- D47（导出器 24pt `###` 阈值）：2 行：`NESTA EDIÇÃO　IN DEZE EDITIE`（已发版第 38 行 `### Nesta edição`）、`EM POUCAS PALAVRAS　KORTOM`（已发版第 52 行 `### Em poucas palavras`）；标题文字均仍在终轮印 PDF 文字层内，G15a 差 0。按 D47，builder 只记录、不补行；closer 落仓时只核实、不补行（D49）。
- 终轮门禁 run2：计分门 18/18 全绿（G1–G14 + G15a + G16 + D18 + D37；G15b 仅记录，G15c N/A——pt 无原生校验器，carry-over 路线按 PLAN §2.1）。text.md 状态：carry-over，与已发版 BYTE-IDENTICAL。
