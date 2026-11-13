# PROOF-NOTE — W47 fr-ru proof1（独立复校）

- 版：`production/2026-w47/2026-w47-fr-ru/`（法语核心 × 俄语读者版，fr fan-out #1，未 commit 未 push）
- 时间：2026-11-11 12:48–13:10 EST；解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR：goals 侧 `hidden_files/w47/scratch-proof-fr-ru1/tmp`（未用 /tmp）。
- 探针：开工前 `ls /dev/null` 存在（普通文件 0 B）、`git hash-object -w` 通（`9daeafb9…`）、goals 侧写文件探针通。注：复核末尾 `/dev/null` 再次缺失（git 报 `could not open '/dev/null'`），已 `touch /dev/null` 垫回并重验 hash-object 通——垫回后复测与开工前一致，非配额问题。
- 只读生产文件：未改任何生产文件、不 commit、不 push。复核前后 SHA 均未变（见 §1）。

## 结论：(b) 不定稿

机械门 14/14 + freeze 8/8 + 确定性重建 8/8 + 目视/手验均通过，**唯一未过项为 D1（P7 读者园地奶油盒溢出，真墨约 5 px 出盒）**。与 fr-de 复校 D1 同缺陷类、同 −2.6 基线，按同一标准判定。

## 1. 身份核对（SHA，复核前后各测一次，均未变）

| 件 | 大小 | SHA-256（复核前 = 复核后） |
|---|---|---|
| 印 `La-Lucerna-VOL4-fr-ru.pdf` | 17,477,487 B | `96aa5eb73b02cf756ec0a4fefd1dafcd36a024c4e87d78343c84ff93f285cd86` |
| 网 `La-Lucerna-VOL4-fr-ru-web.pdf` | 1,760,059 B | `f25ad674cfdc40a2e5aa3d85ab185e67e640554aa55ac7a1d646709cb62d45f8` |
| text `2026-w47-fr-ru.text.md` | 50,537 B | `cfb2cf442b447e7da93faab9de857b723109997f5b3a6bb1cd03ffac1de73740` |

与任务书三件完全一致。核心 core-fr（`production/2026-w47/core-fr/`，文件名为 `La-Lucerna-VOL4.pdf` / `La-Lucerna-VOL4-web.pdf` / `2026-w47-fr-zh-cn.text.md`）复核前 = 复核后：

| 件 | 大小 | SHA-256 前缀 |
|---|---|---|
| 印 `La-Lucerna-VOL4.pdf` | 30,446,982 B | `db3f2a71…` 全 `db3f2a71206f256b9ee0136afd8a2af663e0b3a33df8924c251a064611f135e7` |
| 网 `La-Lucerna-VOL4-web.pdf` | 2,205,749 B | `26593a39…` 全 `26593a39c258fd721e11548f0ea8f7e8eb3cd47195c3d87003481aaf5fe17823` |
| text `2026-w47-fr-zh-cn.text.md` | 46,477 B | `2b50c88d…` 全 `2b50c88d6af4c3a9907e61cb71d67d9c9e2bb8992d41fd10bec7d10ca660737e` |

## 2. 缺陷清单

### D1（唯一缺陷，判定 (b) 的依据）— P7 读者园地奶油盒溢出

- 位置：`svg/p7-langue.svg`，奶油盒 `x=989.0 y=1878 w=873.0 h=380`，盒底 2258.0（渲染实测底边 svg y=2257.47）。
- 溢出行：俄语 `courier_disclosure` 第 3 行 `«письма.»`，`x=1013.0`，基线 svg y=2260.6（盒底 −2.6），字号 19.5pt。
- 同段 3 行（同 x=1013、同 19.5pt、行距 27.3，段内连续）：
  - y=2206.0 `Заметка редакции: к сдаче номера текстов VOL.4 не поступило, поэтому печатаем`
  - y=2233.3 `помеченный пример редакции; VOL.5 выполнит обещание разобрать настоящие`（盒内末行，clearance +24.7）
  - y=2260.6 `письма.`（盒外）
- **本复校员独立实测（非采信 fr-de 目测）**：
  - creambox 规范扫描（`hidden_files/w47/tools/creambox.py`）：naive `last baseline 2260.6 clearance -2.6`；inside-only 末基线 2233.3（+24.7，desc-clear +18.8）；BELOW-WINDOW +2.6 为同段续行，非下一标题（P7-TOOLBOX 汇总：4 盒，最小 inside clearance +24.7、最小 desc-clear +18.8）。
  - PIL 真墨（印刷 PDF 300 dpi，裁剪渲染防 OOM）：`#6f675d` 墨色在 `письма.` 列（svg x 1013–1125）自 svg y≈2249.8 起，末行真墨至 **svg y≈2262.5，即盒底之下约 5 px**；墨列 svg x 1015.2–1086.6，与 `письма.` 字形吻合。深绿带顶 svg y=2270.08，真墨未及绿带（余约 7.5 px）。
  - 网页 PDF 同法复测：同一真墨范围（svg y 至 2262.5），印/网同缺陷。
  - 目视（150 dpi 印刷 P7、100 dpi 网页 P7）：`письма.` 一行贴在奶油盒底边外、绿带之上，肉眼可见出盒。
- 核心对照：core-fr 同盒同段仅 2 行，末基线 2233.3（+24.7），无溢出。故为 ru 版俄语 disclosure 3 行化引入的本版缺陷，非核心继承。
- 修复方向（供协调员）：缩短俄语 disclosure 至 2 行（或上移该段），重跑全套门禁 + P7 重验。

### R1（记录，不计入判定）— Q148 核心继承问题

- 题干（P8 G 对话）：`— On se retrouve (148)___ du cinéma ? — Oui, à 19 h 30.` 键 `devant`。
- 问题：`devant` 后接 `du cinéma` 成 `devant du cinéma`，法语不成立（应为 `devant le cinéma`）。核心出处 `core-fr/content8.py:170`（`("A2", "devant", E["n_g4"])`）及 `:176` 题干行，10 版共有，核心轨道另修。本版三源一致（P8 键 / text.md 答案区 `148. devant (У кинотеатра)` / 核心 P8 键均为 devant），只记录。

### R2（记录，不计入判定）— D5 字体（全周级已知待定项）

- 实测（Noto Sans CJK SC 段数，8 页 SVG 全扫）：ru 版共 688 段，其中西里尔文 303、纯拉丁文 231、混合/纯 CJK 154。
- 核心对照：core-fr 共 661 段，纯拉丁文 221。ru 版纯拉丁文段数与核心基本持平（231 vs 221，+10 为徽章/编号类），拉丁讲解层落 CJK 字体为全周既有状态，非本版新引入。只记录实测段数，不以此判 (b)。

## 3. 其余核查（全部通过）

- **freeze 首检 8/8**（`tools/freeze.py diff`，`freeze-diff.log`）：p1 +30/−23 新增 CJK 0；p2 +39/−33 新增 0；p3 +35/−34 新增 1（U+3000）；p4 +73/−41 新增 0；p5 +58/−34 新增 0；p6 +46/−28 新增 0；p7 +39/−34 新增 0；p8 +155/−122 新增 14（U+3000）。新增 CJK 合计 15，**全部为结构全角空格 U+3000，无新增 CJK 文字**。
- **机械门 14/14 PASS**（`proof_gates.py` → `gates-proof1.json`，详见 GATE-LOG）：run / occlusion 0 flags / p8_extract 150/150（notes 121/150）/ p8_compare CLEAN keydiff [150] / source_freeze / string_freeze（1 串因翻译 E 值豁免）/ text_layer 印网逐字节一致 107,479 B / p8_font 11.625pt / scans / chips 134 [10,12,18,15,14,15,12,38] / keycheck 仅 Q150 不同 / mcq 45 bodies 1,478 lines 0 defects / widths / band_spans（FR title ends 1236.9，band_r1 starts 1284.4，gap 47.5）。
- **确定性**：版目录沙盒副本重建（`rebuild-run.log`，副本已删），删 svg 后 `run.py` rc=0、TOTAL 150（分布与 builder 一致），8 个 SVG sha256 与 builder `freeze_direct` 记录逐一相同 8/8：`45d7ade2 / e805be98 / 8bc49b18 / c9dc8270 / b7577f84 / 69a1f37e / e825ca39 / 3cdf7e52`。
- **creambox 全版扫描**（33 盒，`creambox-proof1.log`）：除 D1 外，7 条 naive 负值行全部为下一标题误报（BELOW-WINDOW +24.0/+37.0，inside-only 全部 ≥ +47.7）；右缘扫描（`text_w` 实测 33 盒全部文字）：零越盒右缘。
- **150 题逐题手验**：三源交叉——P8 抽取键 vs text.md 答案区 150/150 一致（0 偏差）；P8 抽取键 vs 核心 P8 键仅 Q150 不同（写作题，预期）；text.md 全文 1,088 行通读，题干与答案逐题核对无误（Q64 « Les Braves » → Lukas Dhont 已核；Q109–116 Théo 完形、Q120 si+imparfait→irais、Q131 si+imparfait 例句等均核）。
- **8 页逐页目视**（印刷 PDF 150 dpi，`png/p1.png`–`p8.png`）：除 D1 外零问题；P1 band 无重叠（FR title ends 1236.9，band_r1 starts 1284.4）；各页无溢出/遮挡/截断。网页 PDF 抽查（`png/web-p1.png`、`web-p7.png`，100 dpi）：与印刷版布局一致；P7 溢出在网页版同样存在。
- **P3 ZOOM 盒下半空白**：与核心对照——同盒几何完全相同（x=1439.5 y=1137.6 w=422.5 h=476.0，底 1613.6），核心盒内末行 y=1493.6、ru 版 1465.6，空白为核心继承版式，非本版回归，不计缺陷。
- **双语小文件标题越奶油盒右缘**（已裁决规则）：33 盒全部文字 `text_w` 实测，零越右缘；无字形被裁、无墨叠他元素，故无此缺陷。

## 4. 门禁产物

`PROOF-NOTE.md`、`GATE-LOG.md`、`proof_gates.py`、`gates-proof1.json`、`freeze-diff.log`、`occlusion-proof1.json`、`p8-proof1.json`、`p8compare-proof1.json`、`mcq-proof1.log`、`print-proof1.txt`、`web-proof1.txt`、`creambox-proof1.log`、`p7_ink.py`、`p7_ink2.py`、`rebuild-run.log`、`png/`（p1–p8、web-p1、web-p7）。

## 5. 修复后重验要求

修 D1（俄语 disclosure 压回 2 行）后重跑全套门禁 + P7 真墨重测 + 目视；其余门禁与内容无需重验（但重建后 freeze/determinism 须随新版重跑）。
