# PROOF-NOTE — W47 fr-ko (法语核心 × 读者韩语) 独立复校 proof1

- 复校员：独立复校（与构建者不同人），2026-11-11 12:48–13:10 EST
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-ko1/`
- 结论：**(a) 零缺陷，定稿** — 本版无缺陷。另 2 项记录（不计入本版缺陷）：1 项核心继承问题（Q148，需 core 轨道修）、1 项全周级已知待定项（D5 字体）。
- 生产文件只读：复校期间未改任何生产文件，未 commit、未 push。确定性重建在沙盒副本中进行（副本已删，哈希记录在 GATE-LOG）。`git status` 上该版目录与 core-fr 均为未提交新目录（builder 工作状态，复校未动）。

## 身份核对（开工前实测，与任务书完全一致）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4-fr-ko.pdf`（印刷） | 23,103,417 | `4106a1bd80bce5b45a67eb3f6e2b81daeb646ca97f8cdb01b5f09ffdc378e34b` |
| `La-Lucerna-VOL4-fr-ko-web.pdf`（网页） | 2,048,862 | `4b2ca968db5e5d1a0368eb14fb7b28c5badcabb5a908220b763830a6d97469c5` |
| `2026-w47-fr-ko.text.md` | 47,323 | `b069a041bf5765eef046e8e1b47d5bfb51e6256e38510268473c1d2cbc0fcd8a` |

核心 core-fr 三件对照（盘上实测，复核前后各测一次，未变；注意盘上文件名为 `La-Lucerna-VOL4.pdf` / `La-Lucerna-VOL4-web.pdf` / `2026-w47-fr-zh-cn.text.md`，非任务书所写的 `-fr` 名）：

| 文件 | SHA-256（复核前 = 复核后） |
|---|---|
| `La-Lucerna-VOL4.pdf`（印刷，30,446,982 B） | `db3f2a71206f256b9ee0136afd8a2af663e0b3a33df8924c251a064611f135e7` |
| `La-Lucerna-VOL4-web.pdf`（网页，2,205,749 B） | `26593a39c258fd721e11548f0ea8f7e8eb3cd47195c3d87003481aaf5fe17823` |
| `2026-w47-fr-zh-cn.text.md`（46,477 B） | `2b50c88d6af4c3a9907e61cb71d67d9c9e2bb8992d41fd10bec7d10ca660737e` |

核心 core-fr 已定稿（fix3 build，proof4 (a)）。Builder 本版 run1，门禁 15/15。

## 缺陷清单

**零项。** 本版无 ko 引入缺陷。

## 特别核查 — P7 读者园地奶油盒（自测裁定，不采信跨版目测）

- 位置：P7 右下 `LE COURRIER DES LECTEURS　독자 편지` 奶油盒（`p7-langue.svg`：`x=989.0 y=1878 w=873.0 h=380`，盒底 `y=2258.0`）。
- 内容：`courier_disclosure` 韩文段 2 行（基线 2206.0 / 2233.3）："편집부 알림: 마감 시점에 VOL.4 투고가 도착하지 않아, 명시한 편집부 예문을 싣는다. VOL.5에서 실제 투고 평론 약속을 지킨다."——与核心中文版同为 2 行（德文版为 3 行溢出，ko 不是）。
- 自测（非采信 fr-de 复校员目测）：
  - creambox 规范扫描（`creambox-proof1.log`）：该盒 naive clearance **+24.7**（正值），inside-only 末基线 2233.3，desc-clear **+18.8**；P7-TOOLBOX 汇总：4 盒，最小 inside clearance +24.7，最小 desc-clear +18.8。
  - PIL 真墨测量（印刷 PDF 300 dpi，`p7_measure.py` / `p7_measure2.py`）：奶油 rect 经 PDF 绘图实测 `svg-y 1878.0..2258.0, x 989.0..1862.0`；末行字形真墨最末行 svg y≈2234.4，盒底 2258.0，**真墨清除 +23.6px**；2234.4 至 2269.6 之间零墨；深绿带绘图实测起于 svg y=2270.0（盒底之下 12px 白纸）。300 dpi 裁切（`png/p7-box-crop.png`）目视：两行韩文完整在奶油内，盒底奶油边干净，字形无一触边。
  - 结论：**干净，无溢出。** fr-de 复校员"ko 版 inside-only +24.7"的说法与本次自测一致，但本裁定完全基于上述自测数据。
- 全版 creambox 另有 7 条 naive `clearance -` 行（+24.0/+37.0），逐一核对均为**下一标题误报**（`LE MOT DE LA SEMAINE`、`LA SEMAINE EN CHIFFRES`、`À VOUS !　당신 차례!` ×3、`IL EST PRÉVU QUE + SUBJONCTIF`、`LE DÉBAT　토론`），各盒 inside-only 清除均为正（最小 +47.7）。详见 GATE-LOG。

## 记录项（不计入本版 (a) 判定）

### R1 — Q148 错法语（核心继承，10 版共有，需 core 轨道修）

- 印法：P8 对话 "— On se retrouve (148)___ du cinéma ? — Oui, à 19 h 30."，答案键 `devant`（本版 `p8-proof1.json` / 核心 `final-fr-p8.json` / text.md 答案区 `148. devant（영화관 앞）` 三源一致）。
- 问题：填入后成 "On se retrouve **devant du cinéma** ?"——介词 `devant` 后不接 `du`，正确应为 "devant **le** cinéma"。
- 定性：核心冻结源 `core-fr/content8.py:176` 与 ko 版 `content8.py:176` 字节相同（source_freeze 门已验），核心键亦为 `devant`；属核心原文缺陷，非 ko fan-out 引入，fan-out 按 freeze 规则不得擅自偏离核心。故只记录，报请转 core 轨道修复（修核心后 10 版同受影响，须重验）。

### R2 — D5 字体（全周级已知待定项，如实记录，不判 (b)、不擅自修）

- 实测（8 页 SVG 字体普查，精确分类）：
  - ko 版：`Newsreader` 983 段、`Noto Sans CJK SC` 661 段、`Noto Serif CJK SC` 155 段、`DejaVu Sans` 4 段（P7 ✗ 标记，合理）、`UnifrakturMaguntia` 1 段（刊头黑体）。
  - CJK 字体段共 816：含 CJK 字符 452 段、纯拉丁字母 222 段、纯数字/标点 125 段、纯标点/空格 17 段。
  - 核心对照：CJK 字体段共 776（415 / 219 / 125 / 17）。ko 版仅比核心多 **3 段**纯拉丁字母段（222 vs 219），其余 125+17 两段数与核心完全相同——即 D5 现象基本是核心继承的常量，非 ko 讲解层新引入。纯拉丁字母段多为双语结构标题（如 `SEMAINE DU 16 AU 22 NOVEMBRE 2026`、`LE JOURNAL DES APPRENANTS…`、`ALCARAZ GAGNE PARIS…`），核心原文即如此。
- 按任务书指示：仅记录实测段数，待用户定夺 scope。

### R3 — 任务书所称冻结英文 "next Sunday"（核查说明，非缺陷）

- 任务书称该英文冻结于核心 gloss `content12.py:37/:113`、`content34.py:127`。盘上实测：该三行现为法文头条 `"Alcaraz, roi de Paris : le Sénat tranche mercredi"`、`« trancher »` 词条与 MCQ 代码，不含该英文串；全仓 grep "next Sunday" 仅命中 W46 zh-tw 文件（味全龙游行旧文，与 W47 无关），**core-fr 与 fr-ko 两目录内 "Sunday" 出现 0 次**。
- 结论：本版内不存在该英文串，无可裁定的内容；行号与盘上现状不符，已如实记录（可能为旧版行号）。不影响 (a) 判定。

## 其余手验（150 题逐题核对，无问题）

- `.text.md` 全文 1,087 行通读：150 题题干/选项/答案/注记逐题核对题干事实与文章内容，韩语注记逐条核对语法与译义。结论：除 R1 外，150 键全部正确。
  - 三源交叉（版 P8 keys / text.md 答案区 / 核心 P8 keys，`triple-check.json`）：text.md 答案区 150/150 解析，**唯一差异为 Q150**（写作键：核心 `开放题` → ko `自由 작문`，预期翻译）；其余 149 键三源完全一致。
  - 抽查示例：Q26 注记 "Vrai (1951년부터 조기 판매)" 与 P3 ZOOM "1951 : le droit de vendre plus tôt" 同事实；Q53 "plus vite"、Q54 "plus grand"、Q55 "moins longue" 比较级答案正确；Q64 "Lukas Dhont" 拼写已在 P5 文章与题干双重核对无误；Q80 "458–0" 与 P6 日历一致；Q84 "26 nov." 与 "Fin du délai de 50 jours" 一致；Q113 "propose"（主语 Le cinéma 单数）、Q114 "aimé"（avoir 无配合）注记正确；Q113–116 过去分词配合注记正确；Q135–139 韩→法翻译答案与韩语提示准确对应；Q140–144 配对键 a/b/c/d/e 与词表一致。
  - 细项（非缺陷，仅备查）：P2 "참고 | une virgule 쉼표 voter 투표하다 fêter 축하하다." 无溢出；P4 解说员短语 `『』`韩式引号（U+300E/U+300F）为讲解层原文标点，见 CJK 分类；P5 "LE CINÉMA DU MERCREDI" 韩注 "신작은 11월 18일 수요일 개봉, 16편" 与文章一致；P7 读者来信韩注 "샤오모의 해설" 为 ko 版讲解层署名，无中文残留；"DATES À RETENIR" 韩注 "주의: 누보는 19일 목요일 출시. 축제는 18일 밤부터." 与文章一致。
- 8 页逐页目视（印刷 PDF 150 dpi，`png/p1.png`–`p8.png`；另抽查网页 PDF P1/P7，100 dpi）：零问题——P1 band_r1（法文标题止 1236.9，韩文带起 1436.9，净空 200.0）无重叠；各页无溢出、无遮挡、无截断；Atget / Moreau / Méliès / Doré / Hiroshige 图注完整；P8 42 题答案流完整，Hiroshige 图在位。
- 徽章 134（10/12/18/15/14/15/12/38），与 builder 一致；P8 最小字号 11.625pt；U+2019=0、U+00B7=0；印/网文字层逐字节一致（102,735 B）；卷号 VOL.4 各处一致；无中文残留。

## 参考

- 构建报告：`hidden_files/w47/scratch-fanout-fr/FANOUT-REPORT-fr.md`（ko 版 run1）与 `hidden_files/w47/scratch-fanout-fr/ko/EDITION-RECORD.md`
- 门禁明细：同目录 `GATE-LOG.md`、`gates-proof1.json`
- 证据图：同目录 `png/`（p1–p8 印刷版、`p7-box-crop.png` 盒底裁切、`p7-300dpi.png`、`web-p1.png`、`web-p7.png`）
