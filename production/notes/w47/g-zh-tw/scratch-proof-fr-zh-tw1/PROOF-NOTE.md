# PROOF-NOTE — W47 fr-zh-tw (法语核心 × 繁中读者版) 独立复校 proof1

- 复校员：独立复校（与构建者不同人），2026-11-11 12:48–14:20 EST
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-zh-tw1/`
- 结论：**(b) 有缺陷，不定稿** — 2 项缺陷（D1 简体残留 1 字 + D2 行首孤字 。3 处），见下。另 2 项记录（不计入本版缺陷）：1 项核心继承缺陷（Q148，需 core 轨道修）、1 项全周级已知待定项（D5 字体）。
- 生产文件只读：复校期间未改任何生产文件，未 commit、未 push。确定性重建在沙盒副本中进行（副本已删，哈希记录在 GATE-LOG）。`git status` 上该版目录为未提交新目录（`?? production/2026-w47/2026-w47-fr-zh-tw/`，builder 工作状态，复校未动）。复核前后三件 SHA 逐一相同。

## 身份核对（开工前与收工后两次实测，一致）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4-fr-zh-tw.pdf`（印刷） | 30,551,968 | `9f48e43e4a32a53b8bec0c8fe2504d6447bc95c55606e2540564f935b39d88da` |
| `La-Lucerna-VOL4-fr-zh-tw-web.pdf`（网页） | 2,558,076 | `5ab101b975166b10b3dba4fdb839abb74698c6bcee026bb9455a6244b8b87cef` |
| `2026-w47-fr-zh-tw.text.md` | 46,020 | `1da457a80d0d02ada1e76ce6525a83493bcb14cc4650098a7cab76f858a36ba0` |

核心 core-fr 对照 SHA（复核前后各测一次，未变）：
- 印 `La-Lucerna-VOL4.pdf`：`db3f2a71206f256b9ee0136afd8a2af663e0b3a33df8924c251a064611f135e7`
- 网 `La-Lucerna-VOL4-web.pdf`：`26593a39c258fd721e11548f0ea8f7e8eb3cd47195c3d87003481aaf5fe17823`
- 文 `2026-w47-fr-zh-cn.text.md`：`2b50c88d6af4c3a9907e61cb71d67d9c9e2bb8992d41fd10bec7d10ca660737e`

构建报告：`hidden_files/w47/scratch-fanout-fr/FANOUT-REPORT-fr.md`（zh-tw 版 run2，门禁 15/15）。

## 缺陷清单

### D1 — 简体残留「准」（须修后重校）

- 位置：`expl.py:120`（`zoom_note`）与 `expl.py:230`（`n_vf1`），同一词「獲准」。
- 内容：正體應為「**獲準**」（`準`才是繁體形，`准`為簡化字）。本版為繁體中文版，全版自稱「講解繁體中文」，出现简体字即为错字。
- 出现处（全版共 4 文件）：
  - `expl.py:120`：`1951年獲准提前售酒、1985年定為11月第三個星期四、2026年是這場約會的75週年。`
  - `expl.py:230`：`1951年獲准提前售酒`
  - `svg/p3-culture.svg`：P3 ZOOM 框中文译注（同句）
  - `svg/p8-exercices.svg`：P8 第 26 题注记（同句）
  - `2026-w47-fr-zh-tw.text.md:419`（P3 ZOOM）与 `:1063`（RÉPONSES 第 26 题注记）
- 实测方法：全版 CJK 逐字 opencc `s2t` 扫描（SVG 8 页 + `expl.py` + `.text.md`），唯一简体字即 `准`；其余 255 个新增异体字全部为繁体或两岸同形字（见 GATE-LOG §1）。`准`未进 freeze「新增 CJK」集——因核心（简体）已有 3 处，本版 2 处，属**核心简体字被原样带入繁体译文**，string_freeze 的整串比对拦不住，只有逐字简繁扫描能发现。Builder 的启发式简体集未含 `准`，故漏网。
- 修复方向（供 builder，不由复校改）：`expl.py` 两处 `准`→`準`，仅改值；P3/P8 SVG 哈希变，PDF 与 `.text.md` 随之变；修后重跑 gates 全套 + 本复校重验（P3、P8、text.md 三处）。

### D2 — 行首孤字「。」（轻微，3 处，均新于核心）

CJK 禁则：句号不得置于行首。以下三处「。」单独成行，150 dpi 目视清晰可见：

| 位置 | 上行（末行） | 孤字行（SVG 坐标） |
|---|---|---|
| P2 译注框 | `註｜une virgule 逗號　voter 投票　fêter 慶祝` | `p2-vie.svg` y=250.225 x=989.0，`。` |
| P2 ET VOUS 框 | `說說你的11月19日：用法語寫兩句話寄來` | `p2-vie.svg` y=1304.18 x=1461.5，`。` |
| P3 ZOOM 框 | `1951年獲准提前售酒、1985年定為11月第三個星期四、2026年是這場約會的75週年`（同 D1 句） | `p3-culture.svg` y=1493.6 x=1461.5，`。` |

- 定性：文字完整、无裁切、无重叠，属轻微排版缺陷；三处核心均无（核心 P2 注记换行在「祝。」、ET VOUS 单行、P3 无孤字），是繁体译文换行引入的新问题。
- 修复方向：将上行缩短至少 1 字，使「。」回到上行末（或等效改写）；仅改值，修后重验三处。
- 不计入项：P4 同形孤字 `。`（`p4-sport.svg` y=550.53，「大師賽決賽結果與杜林名單見本版正文」/「。」）与核心逐字节同位（核心「大师赛决赛结果与都灵名单见本版正文」/「。」），属核心继承版式，只记录、不计入本版缺陷（见观察 O1）。

## P7 读者园地奶油盒——独立实测裁定（干净）

任务要求不得直接采信跨版目测（fr-de 复校员称 zh-tw 版 inside-only +24.7），本复校**自己实测**：

- SVG：`p7-langue.svg` 盒 `x=989.0 y=1878 w=873.0 h=380`，盒底 2258.0；`courrier_disclosure`（`expl.py:182`）繁体段「編輯部說明：截至付印，編輯部尚未收到 VOL.4 的投稿作文，故本期登載標示明確的編輯部示例；VOL.5 將兌現點評真實投稿的承諾。」排成 **2 行**，基线 2206.0 / 2233.3。
- canonical creambox（`hidden_files/w47/tools/creambox.py`）：该盒 inside-only 末基线 2233.3，clearance **+24.7**，desc-clear **+18.8**；无 BELOW-WINDOW 行（无第 3 行）。
- PIL 真墨测量（印刷 PDF 300 dpi，**真 SVG 坐标**——SVG 为 1950×2700，见 GATE-LOG §7 校准）：奶油底边实测 svg y≈2257.5（与盒底 2258.0 一致）；末行真墨最末行 svg y≈2235，**盒内余白约 23px**；其下 12px 白纸，再接深绿带（起于 svg y=2270.0）；300 dpi 裁切（`png/p7-box-crop.png`）目视：末行完整在奶油内，边下干净。
- 裁定：**P7 无溢出，干净**；与核心同盒（末基线 2233.3，+24.7）一致。与 de 版同盒 -2.6 溢出不同构。

## 其余手验（150 题逐题核对，无问题）

- `.text.md` 全文 1,087 行通读：150 题题干/选项/答案/注记逐题核对题干事实与文章内容，繁体注记逐条核对语法与译义。结论：除 D1、R1 外，150 键全部正确。
  - 三源交叉（P8 抽取键 / text.md 答案区 / 核心 P8 键）：150/150 一致，仅 Q150 不同（写作键 `開放題` vs 核心 `开放题`）；text.md 答案区 150 条全解析、0 缺失、0 实 mismatch（8 处为解析器把注记内全角空格切断所致，键字母本身均一致）；带注记答案 121 条，与 P8 抽取注记数 121/150 一致。
  - 抽查示例：Q26 注记与 P3 ZOOM 同事实（除 D1 的 `准` 字外）；Q53 `plus vite`、Q113 `propose`（Le cinéma 单数）、Q114 `aimé`（avoir 无配合）、Q120 `irais`、Q121 `semble`、Q122 `reçoit`、Q135–139 漢→法翻译答案与注记均正确；Q64 `Lukas Dhont`（text.md 3 处，`Dont` 全版 0 次）；Q148 除外（R1）。
  - 人名逐一核对法文原文：東特（Dhont）、梅諾謝（Ménochet）、菲斯（Fils）、海米奇（Haymitch）、勞倫斯（Lawrence）、斯米亞（Smia）、梅杜爾（Meddour）、史考特·湯瑪斯（Scott Thomas）、吉茲（Guiz）、梅里愛（Méliès）、多雷（Doré）、廣重（Hiroshige）、阿特熱（Atget）、莫羅（Moreau）；台湾用法杜林、薄酒萊、藍軍。
- 8 页逐页目视（印刷 PDF 150 dpi；另抽查网页 PDF P1/P7，100 dpi）：除 D1、D2 外零问题——P1 band_r1（法文标题止 1236.9、读者带起 1405.0，净空 168.1，1920 单位；真 SVG 单位则为 1256.2 / 1427.0，净空 170.7）无重叠；各页无溢出、无遮挡、无截断；Atget、Châtillon、Moreau、Méliès、Doré、Hiroshige 图注完整；P8 42 题答案流完整。
- 奶油盒右缘扫描（已裁决规则）：全版 33 盒，中心落在盒内、字形越右缘的 span 为 **0**；无缺陷、无观察项。
- 丢空格扫描（ru 教训类）：同基线相邻 span 对 678 组，字-字紧邻（间隙 <2 svg 单位）为 **0**；61 组间隙 <5 均为设计使然（箭头 `→`、`___`、前导空格 span 的 bbox 修边），SVG 坐标与核心同位逐一相同，无丢空格。
- 徽章 134（10/12/18/15/14/15/12/38），与 builder 一致；P8 最小字号 11.625pt；U+2019=0、U+00B7=0；印/网文字层逐字节一致（101,806 B）；卷号 VOL.4 各处一致；页脚 8 页均为「講解繁體中文」，P1 徽章「法語正文　繁體中文講解 — 給繁體中文讀者的版本」。
- 「next Sunday」核查：本版与核心盘上全文搜 0 次（`content12.py`/`content34.py`/`expl.py`/SVG/text.md），任务书记载的行号已过期；无此项可判，不影响结论。

## 记录项（不计入本版 (b) 判定）

### R1 — Q148 错法语（核心继承，10 版共有，需 core 轨道修）

- 印法：P8 对话「— On se retrouve (148)___ du cinéma ? — Oui, à 19 h 30.」，答案键 `devant`（`p8-proof1.json` / 核心 `final-fr-p8.json` / text.md 答案区 `148. devant（電影院門口）` 三源一致）。
- 问题：填入后成「On se retrouve **devant du cinéma** ?」——介词 `devant` 后不接 `du`，正确应为「devant **le** cinéma」。
- 定性：核心冻结源 `core-fr/content8.py:176` 与本版 `content8.py:176` 字节相同，核心键亦为 `devant`；属核心原文缺陷，非 zh-tw fan-out 引入，fan-out 按 freeze 规则不得擅自偏离核心。故不计入本版缺陷，报请转 core 轨道修复（修核心后 10 版同受影响，须重验）。

### R2 — D5 字体（全周级已知待定项，如实记录，不判 (b)、不擅自修）

- 实测：8 页 SVG 字体普查——`Newsreader` 931 段、`Noto Sans CJK SC` 657 段、`Noto Serif CJK SC` 62 段、`DejaVu Sans` 4 段（P7 ✗ 标记，合理）、`UnifrakturMaguntia` 1 段（刊头黑体）。
- 其中 719 段 CJK 字体中 **362 段为纯拉丁文**（核心对照：723 段中 361 段）。本版仅比核心多 1 段：`CLINIQUE DES ERREURS`——系双语标题「CLINIQUE DES ERREURS　易错诊所」按字体拆 run 所致（核心为同一 `<text>` 元素、含 CJK 故不计），非新增内容；其余 361 段与核心同文（刊头、法文家具、级别标、题号等法文结构层落在 CJK 字体，属继承结构）。
- 按任务书指示：仅记录，待用户定夺 scope。

## 观察项（非缺陷，仅备查）

- O1：P4 孤字 `。`（y=550.53）与核心同位同文，核心继承版式，不计入本版。
- O2：P7 披露行 2 行首为 `；`、P8 答案流续行行首为 `）`，均与核心同位同文，核心继承断行，不计入本版。
- O3：P3 头「BEAUJOLAIS　薄酒萊小測」宽度门已过；P1「sam. 21　Turin : demies　SERD」中 SERD 为欧洲减废周（源文件即如此）。
- O4：band_spans 门所用 1920 单位系历史口径（见 GATE-LOG §7）：SVG 实为 1950×2700，真值 = 读数 ×1.015625；净空真值更大，结论不变。

## 参考

- 构建报告：`hidden_files/w47/scratch-fanout-fr/FANOUT-REPORT-fr.md`（zh-tw 版 run2）
- 门禁明细：同目录 `GATE-LOG.md`、`gates-proof1.json`
- 证据图：同目录 `png/`（p1–p8 印刷版、`p7-300.png`、`p7-box-crop.png` 300 dpi 盒底裁切、`web-p1.png`、`web-p7.png`）
