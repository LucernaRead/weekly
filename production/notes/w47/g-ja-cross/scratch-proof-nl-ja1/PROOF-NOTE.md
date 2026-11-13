# PROOF-NOTE — 2026-W47 nl → ja（日语读者版）· proof1（独立复校，build-6）

- 版目录：`production/2026-w47/2026-w47-nl-ja/`（规范路径）
- 复校员：独立复校（proof1）· 2026-11-11（America/Toronto）
- 对象：delta build-6（core-nl fix3+fix4+fix5 同步）。机械门完整证据见同目录 `GATE-LOG.md`；150 题逐题手验见 `b6-keycheck-table.txt` / `b6-keycheck.json`
- 源文件未改动、未重建生产文件、未 commit、未 push。生产目录只读验证：开工/收工 42 文件哈希快照逐项一致，零写入
- 前置 delta 记录（`scratch-delta-nl-ja/DELTA-LOG.md` / `GATE-LOG.md`）仅作参阅；以下全部结论均为本次自跑自测

## §0 身份核对（磁盘实测，开工与收工两次一致）

| 文件 | 磁盘 SHA-256 | 磁盘字节 | 与任务一致 |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-ja.pdf`（印） | `f78ffe324aaf24d39fa71cc815b96d6c163cf2747c27a10d7633e94cb41943b0` | 26,049,309 | ✓ |
| `De-Lucerna-VOL4-nl-ja-web.pdf`（网） | `b4d4501b8665d0adee4b8484a66a8bd17031ee4953f397e7c0142b7b0ee4762b` | 2,155,389 | ✓ |
| `2026-w47-nl-ja.text.md`（文） | `060bfdea243483edb1a30691ff26291eac1a90bc69f2ea4c38fe97eac05bb93a` | 47,801 | ✓ |

探针：`git hash-object -w /dev/null` 成功（`e69de29b…`）；goals 侧 scratch 真实写文件成功；`df` 可用 54G。TMPDIR 全程用自有 scratch。

## 结论：(b) 有缺陷，不能定稿

共 **1 项缺陷（低）**，系 build-5 旧缺陷遗留、非 delta 引入；修复只需改 `ABSTRACT.txt` 2 字符，不动三件交付物。Delta 六处（D6–D11）全部复核通过，全部机械门通过，150 题三方手验通过。

| # | 严重度 | 页 | 缺陷 | 归属 |
|---|---|---|---|---|
| D2' | 低 | ABSTRACT.txt | 摘要缺完整刊名 `De Lucerna`，只写裸 `Lucerna VOL.4`，违反 SOP §9（含刊名） | 本版（build-5 旧 proof1 D2 遗留，delta 未动 ABSTRACT.txt） |

## 缺陷清单

### D2' — ABSTRACT.txt 缺完整刊名 `De Lucerna`（旧 proof1 D2 遗留，未消除）
- **定位**：`ABSTRACT.txt` 全文（单行）：
  > `オランダ語週刊 Lucerna VOL.4（2026年11月16日〜22日）：シンタクラースとパッケスアーフォント、ネーションズリーグのオランダ対ドイツ、エクスペディティ・ロビンソンとシンタクラースの伝統の変化——オランダ語の読解と150の練習問題、レベルA2〜B2、日本語の解説付き。`
- **实测证据**：`grep -c "De Lucerna" ABSTRACT.txt` = **0**；`Lucerna` 出现 1 次。SOP §9 要求摘要“并含刊名”；完整刊名是 `De Lucerna`（本版 text.md 标题 `# De Lucerna · オランダ語週刊 VOL.4 · 2026-W47`、核心 ABSTRACT `De Lucerna 荷兰语周报 VOL.4：…`、P1 报头均为 `De Lucerna`）。摘要其余要素齐全：目标语名（オランダ語）、A2〜B2、150 题、真实主题词、日期 11月16日〜22日。
- **修复建议**：改为 `オランダ語週刊 De Lucerna VOL.4（2026年11月16日〜22日）：…`（只加 `De ` 两字符，其余不动）；修后只需重核摘要本身（不改印/网/text.md 三件 SHA）。旧 proof 亦记：nl 家庭其余 8 版摘要同为裸 `Lucerna`（模板共性），宜统改，此处只裁本版。
- **不属缺陷说明**：旧 proof 的 O1（Q78 `Zij` 单复数）仍为观察非缺陷——P8 答案注已消歧（78 无标记=单数 `gaat maken`；79 注 `（複数）`=复数 `gaan schrijven`），与核心逐字一致，本版不动。

## 旧缺陷复核（build-5 proof1，两项）
- **旧 D1（中）— 网 PDF 丢失 P1 斜体 `«de groepswinst»`：已消除。** 本次 PyMuPDF span 实测交付网 PDF：斜体 span **1 个**——P1 `LucernaNewsreader-Italic 16.12pt '«de groepswinst»'`，与印 PDF（`Newsreader16pt-Italic 16.12pt`，同词）一致。网 PDF 全书斜体 span 总数 = 1 = 印 PDF。证据：`b6-textlayer.log` / `b6-textlayer.json`。
- **旧 D2（低）— ABSTRACT 缺 `De`：未消除**，见上（D2'）。

## Delta D6–D11 逐项复核（全部自测，非照抄）

| 点 | 自测值 | 结论 |
|---|---|---|
| D6 | 本版 `wrap()` 0.1px 扫描：带 **412.8–430.0**，中点 421.4，选中 421.4 在带内且为中点；断行 2 行与修前逐字同：`現在完了形で補おう。助動詞hebben／zijnに` (y=2303.5) / `注意。` (y=2333.22)；p3 SVG 与 staging 字节一致，下游 y 无位移；200dpi 裁图目检 `。` 在行末 | ✓ 结构同步属实，修前即无缺陷 |
| D7 | 带 **414.9–430.0**，中点 422.45，选中 422.45；3 行逐字同：`de wedstrijd 試合；de groepswinst グループ` / `優勝；de kwartfinale 準々決勝；scoren 得点` / `する。` (y=725.66/755.39/785.11)；p7 SVG 字节一致；裁图目检 | ✓ |
| D8 | 带 **369.5–387.7**，中点 378.6，选中 capcn_w=378.6；3 行逐字同，基线 635.02/659.44/683.86 全不变；`P6 chart ends 691` 与修前同；p6 SVG 字节一致 | ✓ |
| D9 | 三源一致：`content8.py:75` + `text.md:415` + P8 节点 (y=2175.3) 均为 `Ik maak een surprise met een kort gedicht.`；题干 `小さな詩つきのプレゼントを作ります。` 含“小”= kort，语义搭配正确；其余 149 键未动；P8 裁图目检印出 `kort`；修前 keydiff [137,138,140] → 修后 [137,138] | ✓ 真修 |
| D10 | 带 **378.0–397.9**，中点 387.95，选中 dt_zh_w=387.95；2 行逐字同：`締め切り時、手紙も最優秀作文も届かず。` (1783.77) / `見本掲載。約束は VOL.5 へ。` (1812.17)；`P7 col3 ends 1927.5` 与修前同；p7 SVG 字节一致 | ✓ |
| D11 | 盒 `<rect x=1439.5 y=591.6 h=638.0>` 底 **1229.6**；末行 `18:45 uur.` 基线 **1209.49**，基线余量 **+20.11px**；事实句 wrap 3/3/3/2/3=14 行，顶留公式 62→89，sh 611.0→638.0；PIL 真墨（卡片 1×，纸/奶油双底色）：末行最低墨行 y=1209，余量 +20.6px；交付印 PDF 150dpi：最低墨行 svg-y 1209.53，余量 +20.07px；盒底下 7px 条带卡片 0 / 印 PDF 0 非纸像素；`P4 col3 ends 1229.6`；与习题线 y=1608 间隔 378.40px；裁图目检末行在盒内、下有明显留白 | ✓ 真修 |
| 注 | D11 卡片 y=1228/1229 两行各 423 非纸像素是盒底行本身的奶油填色（盒宽 422.5px；y=1229 像素为 (244,243,235)，系 1229.6 分数底边的奶油/纸张混色，非文字墨）；严格取完全在盒底之下的行 y=1230–1236 后为 0，与印 PDF 一致 | — |

- **SVG 变化范围**：与 staging（build-5）逐页 SHA 比对，**仅 p4-sport.svg（D11）与 p8-toets.svg（D9）变化**，其余 6 页字节一致。
- **D6/D7/D8/D10“不存在”核实**：修前 SVG 断行与盒内余量本次重测干净（上表逐行基线 + 孤儿横扫 0/0 + spill 0 + creambox 与修前逐项相同），属结构同步，非漏检。

## 核实摘要（全部通过，详见 GATE-LOG）

- **全文通读**：`text.md` 431 行全文通读 + 150 题表逐题手验 + 交付印 PDF 裁图目检（D6/D7/D9/D11/P6 标题/P4 图注）；无溢出、无遮挡、无错字、无内部标签（`SOP/proofread/cover/TODO` 零命中；`VOL.5` 出现均为正文下期预告与读者来信承诺）。
- **150 题手验**：registry vs text.md vs P8 三方 **149/149 MATCH**（仅 Q150 开放写作为例外：P8 印 `✓`，text.md 载 81 词 Tekstmodel，实数 81 词在 80–100 范围内）。题干–键语义逐题手验 150/150 通过：含 Q73（`In vier regels schrijf ik een ___.` → `gedicht`，四行诗搭配正确）、Q78 单数/Q79 复数消歧、配对键 25–28 = d/c/a/b 与 P2 印出选项逐项核对一致、141–144 = b/c/d/a 与 P8 F 区印出选项逐项核对一致、图表题 35+30+20+15=100 与 P6 图表原文一致。分级 A2 46 / B1 73 / B2 31；按页 10/18/18/18/18/18/12/38；题号 1–150 无缺无重。
- **机械门**：见 GATE-LOG——run.py rc=0 TOTAL 150 零溢出；重建 SVG 8/8、text.md 与印 PDF 重建均字节一致；occlusion 0 flags；p8 extract 150/150、compare CLEAN（keydiff [137,138] 为翻译题键即读者语，按设计）；freeze 核心基线 8/8；印/网文字层 msdiff 0，posdiff 仅 P1 报头 1 个 token（`De Lucerna` dx=−0.20pt，属已知字体子集化微移，与核心 fix5 同类）；P8 最小字号 10.12pt（≥ SOP §1.1 下限 9.75pt）；§1.1 风格门全过；孤儿标点 (a) 0 / (b) 0；spill 0；creambox 6 flags 与修前逐项相同（均为已知假阳性，P4 0 flags）；盒标题横向真墨全量扫描（2015 个文本，PIL + 交付印 PDF 300dpi 裁决 30 个近边项）0 越边。
- **56 标题口径说明**：任务所称“56 标题”在本版可枚举的集合中未能复现（奶油盒首行 26、双语标题 ≥20pt 60、双语标题全部 82）；本次改为全量扫描 2015 个 `<text>`（含全部盒标题与栏目标题），PIL 初筛 + 交付 PDF 300dpi 逐项裁决，0 越边——该超集覆盖任何 56 标题子集。请协调员确认 56 的枚举口径。
- **D5 字体（只记录，不作门、不修）**：印 PDF 字体计数 NotoSansCJKsc-Bold 463 / Regular 312、NotoSerifCJKsc-Regular 297 / Bold 1、Newsreader16pt-Regular 1072 / Italic 1、UnifrakturMaguntia 1；网 PDF 同结构（LucernaNewsreader-Bold 40 为子集化拆分，Italic 1 在位）。CJK 字体上的纯拉丁 span 378（span 口径；与核心 fix5 的 245 分段口径不同，不可直接比）。
- **日期/星期核验**：11/14 六、11/15 日、11/16 一、11/21 六、11/22 日、11/24 二、11/29 日均与正文一致（`日:` 零命中）。
- **KIT 声明复核**：基本属实。两处说明：① KIT 未提 ABSTRACT 缺 `De`（本次 D2'）；② D11 卡片初报 422 像素确为盒底填色，已订正为 0（见上表注）。

## 未决 / 备注
- D2' 修复后只需重核 ABSTRACT.txt（改 2 字符，不动三件 SHA），建议修复后由协调员直核，不必重走全量 proof。
- 旧 proof 的 P1/P2/P6 假阳性裁定（ZO ONTHOUD JE HET 右缘内 5.4px、P6 图表头真墨在框内）本次以交付 PDF 300dpi 重测确认：P6 标题真墨最右 1848.88（内 13.12px）、P2 栏目标题 `Wat hoort bij pakjesavond?…` 真墨最右 1853.36（内 8.64px）。与 nl-de 同题越框不同，本版两处均在内。
