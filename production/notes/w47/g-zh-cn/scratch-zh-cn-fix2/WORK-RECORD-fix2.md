# 返修工作记录 — W47 zh-cn 核心版 第二轮返修（Round 2 fix2 builder）

- 工作目录：`~/workspace/weekly-git/production/2026-w47/core-zh-cn/`
- 本记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-zh-cn-fix2/`
- 基线核对（动手前）：印刷版 41,761,724 B / SHA `bc32fa80…507bd3`；网页版 2,629,533 B / SHA `bc985af8…361e`；`.text.md` 49,324 B / SHA `6ef7f4ea…6a7`——与任务书的 run15 终版一致。
- 先读：SOP.md §8/§1.1、AGENTS.md、WEEKLY-KIT.md 全文、第一轮返修记录（scratch-zh-cn-fix/WORK-RECORD.md）。
- 开工探针（硬门禁）：`git hash-object -w`（weekly-git 内）RC 0；新 scratch 目录真实写文件成功。两次都通才动手。
- 不动：tools/p8.py 与 freeze.py；不跑 insert.py / lint --write / git push / add / reset / stash；不提交；不碰 W43/W45/W46、其他目标语；红线（国际政治、中国国内政治）不动；P8 题干 13.12pt 按 adjudication 不动。

## 来源复核结论（动手前，2026-11-11，独立检索）

### D4 “第一次在BO5里打赢T1”：无限定为假，有“全球总决赛”限定为真
- 原文三处（已定位核实）：P4 正文 `content34.py:130`“BLG赢了T1，这是中国队第一次在BO5里打赢T1。”；Q56 题干 `content34.py:211`“BLG是第一次在BO5里打赢___。”；键注 56 “BLG beat T1 for the first time in a BO5.”。三处均缺限定。
- 反证（无限定为假）：BLG 早就在 BO5 里赢过 T1——MSI 2023 败者组 3–1（伦敦，2023-05-20，esports-news.co.uk）；MSI 2024 两次（3–1、3–2）；MSI 2026 又一次 3–2（大田）。
- 限定版为真：T1 在 S3–S15 全球总决赛 BO5 里对 LPL 是 13 战全胜，BLG 的 S16 半决赛 3–1 是第一次打破。
- 来源：
  - Strafe 2026-11-09〈BLG Becomes First LPL Team to Beat T1 in a Bo5 at Worlds〉：“BLG have become the first LPL team to defeat T1 in a best-of-five series at Worlds… The record BLG broke applies only to best-of-five series at Worlds. BLG had already defeated T1 at other international events, including MSI 2023, where they won 3-1, and MSI 2024, where they claimed two series victories, 3-1 and 3-2.” https://www.strafe.com/news/read/blg-becomes-first-lpl-team-to-beat-t1-in-a-bo5-at-worlds/
  - 懂球帝 2026-11-09〈BLG做到了！LPL战队首次在世界赛BO5中战胜T1，此前13场全败〉 https://www.dongqiudi.com/articles/6631972.html
  - esports-news.co.uk 2023-05-20〈BLG beat T1 to set up all-Chinese final at MSI 2023 London〉（BLG 3–1 T1） https://esports-news.co.uk/2023/05/20/blg-beat-t1-reach-final-at-msi-2023-london/
- 修法：三处统一加“全球总决赛”限定（正文、题干中文加“全球总决赛的BO5”，键注英文加“Worlds BO5”）；键仍为 T1。

### D5 “GEN今年一局没输”：不实
- 原文两处（已定位核实）：P1 `content12.py:42`“GEN今年一局没输：瑞士轮3胜0负，八强3比0，半决赛3比0。”；P4 `content34.py:131`“GEN今年一局没输——瑞士轮3胜0负，八强3比0，半决赛3比0。”。另有一处同形表述 P4 事实框 `content34.py:160`“GEN今年 — 淘汰赛一局没输”——**核实为真，保留**（见下）。
- 证伪：GEN 在瑞士轮出线战对 LYON 是 2–1，先丢一小局、再连赢两局。S16 小局战绩截至半决赛为 10 胜 1 负；“3胜0负”只是大场（系列赛）战绩。
- 来源：
  - 懂球帝 2026-11-08〈恐怖如斯，GEN仅丢一个小局晋级S赛决赛〉：“在面对LYON的出线战中，GEN先丢一局，但马上连追两局2-1晋级淘汰赛。进入淘汰赛后，GEN先是3-0横扫LYON，随后半决赛中又3-0横扫iG，本届世界赛小局来到10胜1负。” https://www.dongqiudi.com/articles/6625624.html
  - 新浪体育 2026-11-08：“本届赛事小局战绩达到10胜1负……瑞士轮出线：GEN以3-0从瑞士轮突围，期间与LYON交手一次以2:1取胜” https://k.sina.cn/article_7880068207_1d5b04c6f06801so2c.html?from=sports
  - clip.dor.gg 2026-11-10 BLG–GEN 决赛前瞻表：“S16 瑞士轮 | 3胜0负（1比0胜IG和HLE，2比1胜LYON）” https://clip.dor.gg/zh-CN/blog/geng-vs-blg-worlds-final
- 修法：两处改为“GEN在S16一场没输，只丢了一小局”（大场全胜为真，丢的一小局如实写出；P4 补细节“瑞士轮3胜0负（对LYON 2比1）”）。无习题断言旧说法，故无键改动。
- 保留项：P4 事实框“GEN今年 — 淘汰赛一局没输”——淘汰赛（八强 3–0 LYON + 半决赛 3–0 IG）小局 6–0，属实且另有范围限定（淘汰赛），不动。记录在案，防下一轮复校误当新缺陷。

## 改动清单（源码级，仅 4 处）

### D4（content34.py）
- :130 正文：“这是中国队第一次在BO5里打赢T1。” → “这是中国队第一次在全球总决赛的BO5里打赢T1。”（wrap 预验：仍 6 行，零数字断裂）
- :210–211 Q56：键注 “BLG beat T1 for the first time in a BO5.” → “BLG beat T1 for the first time in a Worlds BO5.”；题干 “BLG是第一次在BO5里打赢___。” → “BLG是第一次在全球总决赛的BO5里打赢___。”（wrap 预验：仍 1 行；键仍 T1）

### D5（content12.py / content34.py）
- content12.py:42（P1）：“GEN今年一局没输：瑞士轮3胜0负，八强3比0，半决赛3比0。” → “GEN在S16一场没输，只丢了一小局：瑞士轮3胜0负，八强3比0，半决赛3比0。”（wrap 预验：5 行→6 行）
- content34.py:131（P4）：“GEN今年一局没输——瑞士轮3胜0负，八强3比0，半决赛3比0。” → “GEN在S16一场没输，只丢了一小局——瑞士轮3胜0负（对LYON 2比1），八强3比0，半决赛3比0。”（wrap 预验：5 行→6 行；“2比1”完整落在一行，“（对”行末悬挂可接受）
- 不改：P4 事实框“淘汰赛一局没输”（见上，属实）；P8 题干 13.12pt（adjudication）。

## 全量自查重读（第二轮复校 6 项观察已丢失，代行全量自查）

- **全文通读**：content12.py / content34.py / content56.py / content7.py / content8.py 五个模块逐行重读（本记录人亲读，非摘要）。
- **150 题键逐题复核**：149 个未改动键与 run15 的逐题验算结论一致（本轮几何证明除 P1-headline、P4-feature 外各流末位置与 run15 完全相同，键内容无变）；改动键 56 逐题验算：题干“BLG是第一次在全球总决赛的BO5里打赢___。”键 T1，注 “BLG beat T1 for the first time in a Worlds BO5.”——与 D4 三源一致；P8 113–150 在 run15 已逐条通读，本轮 P8 未改（SVG 与 run15 的差异仅 P1/P4 两流），p8.py 150/150 + `.text.md` 键区 1–150 连续为准。
- **事实日期**：`date -d`（Asia/Shanghai）复核全部星期：11月4日星期三、5日星期四、6日星期五、7日星期六、8日星期日、9日星期一、11日星期三、12日星期四、13日星期五、14日星期六、15日星期日、16日星期一、21日星期六、22日星期日——与刊内全部断言一致（含 P8 D 段 11月8日星期日/11月11日星期三/11月14日星期六/11月15日星期日，范文 星期一/星期六/星期日 = 11-16/11-21/11-22）。
- **另查一项、核实后保留**：P2“往年是11月11日、12日两天最忙”——通用模式表述，非归因于邮政局的具体数字；检索未找到反证（邮政局通稿不点名 2025 峰值日；中通云仓三波预报与刊内 P6 一致）。无来源可改，不动；不编造。
- **本轮自查新发现**：除 D4、D5 外，零新缺陷（其余观察均为已裁定项：P8 题干 13.12pt、超右版心 span 8 个、习题选项流式折行、单位孤悬、P4“（对”行末——均与 run15 一致，未扩大）。

## 构建与机械门（run16，最终）

- `run.py`（tools venv）：RC 0，**零 FLOW OVERFLOW / HEAD TOO WIDE**；TOTAL 150（A2 56 / B1 69 / B2 25），页 10/18/18/18/18/18/12/38，类型 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1，范文 138 字——与 run15 基线完全一致。几何变化 vs run15：仅 P1-headline 963→1051、P4-feature 734→804（各 +1 行，框底分别为 1828/1180，均在框内）；其余全部流末位置与 run15 完全相同。日志 `run16.log`。
- `render.py`：RC 0，8 cards + 印刷 PDF **41,763,115 B，SHA `c34f5a54e491a085ea3e19a986748938dda79294b90d154a8e746f54a9eb05aa`**。日志 `render16.log`。
- `webpdf.py`：首次调用路径写错（`../../tools/webpdf.py`，RC 2，用法错误；绝对路径后一次通过）。网页 PDF **2,632,446 B，SHA `6b7a12f517749738de2028569556be326aabe00ab556ac3ec8e59cc936a263d9`**，43,693 text bytes，8 页。日志 `webpdf16.log`。
- `export_core.py`（拷入本目录为 `export_core16.py` 运行）：RC 0，recorded strings 1050，`.text.md` **49,435 B，SHA `23fb62bd7763c59392c05ba7e03f64ad8f521352d464d6ac293d2190c4d0bf04`**，registry 150。日志 `export16.log`。

### 机械门（run16，全部通过）
- Occlusion audit：selftest OK（6 类植入全触发，干净对照静默）；终版 SVG **0 flags**。日志 `occl-st16.log` / `occl16.log`。
- p8.py extract：**150/150**（parse: lines）。日志 `p8-16.log`。
- Freeze：工具自报 **8/8 字节一致**，另独立直接 sha256 比对核心 `svg/` 与新鲜 freeze 副本：**8/8 OK**（非 build-copy 冒充——freeze 工具重跑了构建副本再比对）。日志 `freeze16.log`。
- check16.py（`check16.log`）：print/web 非空字符多重集**一致**（各 22,523；web 多 192 空格 + 3 换行 = ReportLab 重排版已知 artifact）；P8 键区最小字号 **9.975pt ≥ 9.75pt**（369 spans），题干 13.12pt 在位（317 spans 12–14pt：13.12/13.5/13.88）；D4/D5 回归：旧表述 “GEN今年一局没输” 0、“第一次在BO5里打赢” 0、“一局没输”全刊仅 1 处（事实框“淘汰赛一局没输”，属实）；新表述 “GEN在S16一场没输” 2、“只丢了一小局” 2、“全球总决赛的BO5” 2、“对LYON 2比1” 1；`.text.md` 键 56 注 “for the first time in a Worlds BO5” 在位、旧注 0；P1/P4 改句行级核对（PDF 行 y=938.9“拿冠军。GEN在S16一场没输，只丢了”、y=731.0/758.4 P4 改句行）；P6 图表 rects (428.0, 529.644, #46581f) / (428.0, 29.526, #37402f) = 139.38×3.8 / 7.77×3.8 ✓；超右版心 span 8 个，与 run15 同集合；§1.1 逐项：纸 #fbfaf6 8×、金色 hex 0（“gold”×3 为 base64 图数据子串，与 run15 同）、砖红/近黑 0、`·` 138（均在正文）、"2003 年" 0、`waitfor` 0、"VOL.3" 2（有意）、"7.6亿件"/"1.4亿件"/"四分之三" 0、"三分之二" 1、"撤档" 3、"139.38" 24、"7.77" 20、8 条本周短语各 2×、繁体独用字 0、政治扫描 0；全刊数字断裂扫描 **0 候选**；合并拉丁词词汇扫描 **0 未知 token**；`.text.md` 键区 150 键 1–150 连续。
- 可视字符（SVG `<text>` 拼接）：22,523 / 25,971（run15：22,477 / 25,923；+46 非空字符 = D4/D5 改句净增）。
- 目视：8 版全图（`view/` 缩放版）+ 两处改句全分辨率裁图（`view/crop-p1-fix.png`、`view/crop-p4-fix.png`）逐版读过：无溢出、无重叠、无压页脚；Q56 新题干在 P4 版上在位；P8 键 56 新注在位（“56. T1 — BLG beat T1 for the first time in a Worlds BO5.”）。

### 测量级记录（非缺陷，保持原状，与 run15 同）
- 超右版心 span 8 个，同集合（6× “答案见第8版” P1–P6；P8 范文行 1398.8pt；P8 “✓= the writing task” 1397.3pt）。
- 习题选项流式折行、单位孤悬（数字完整、月/日/件单独换行）为引擎常态，不动。
- P4 改句“瑞士轮3胜0负（对 / LYON 2比1）”左括号行末悬挂：可接受的换行形态，“2比1”完整，不断数字。

### KIT 更新
- WEEKLY-KIT.md 已同步：Status（fix2 轮次）、P4 内容表（GEN 大场全胜+丢一小局；BLG 首胜仅限全球总决赛）、S16 来源节（GEN 瑞士轮 2–1 LYON、小局 10–1；BLG 首胜口径）、Measured totals（run16 文件大小/SHA、可视字符 22,523/25,971）、新增 “Round 2 (fix2) fixes — D4–D5” 节（来源、修法、验证）。

### 故障记录
- webpdf16 首次调用相对路径错误（RC 2，用法错误，非故障）；改绝对路径一次通过。无配额故障。无其他故障。
