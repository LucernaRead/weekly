# GATE-LOG — 2026-W47 core-ja 修复后全量复校（第二轮，re-proof）

- 对象：`production/2026-w47/core-ja/`（2026-w47-ja-zh-cn，VOL.4）
- 解释器：全部 Python 门均用 `~/workspace/weekly-git/tools/venv/bin/python`
  （与构建同一解释器）；text.md 重导出用系统 python3（纯标准库）。
- 成品（实测，与任务给定一致）：
  印刷 `Lucerna-VOL4.pdf` 26,018,019 B /
  `20b9d50469fbb6ca6470c17becb2790a30f69191d9083520a9270ea7ebbe9ab4`；
  网页 `Lucerna-VOL4-web.pdf` 4,652,763 B /
  `8722bdfbcec0478a7a60fc86ab0ee7cc9333f957253959476d4f608eed82d5b0`；
  text.md 44,432 B /
  `bcfa667da57e2f477b9d825200b98db454ade3c1dde6ec92ea3d446b0bf9926a`。

## 1. 身份与探针

| 检查 | 结果 |
|---|---|
| git hash-object 探针 | 通过（`da0c4eb8…`，RC=0） |
| scratch 真实写盘探针 | 通过（`scratch-proof-ja-core2/.probe`） |
| 三份成品字节 + SHA-256 | 通过，与任务给定一致 |
| 修前 text.md 副本 diff（`scratch-ja-fix-core1/textmd-prefixed.md`） | 仅 1247 行一处差异（一→义），其余 1355 行逐字一致 |

## 2. 回归核查

| 串 | py | text.md | svg | 印刷 PDF 文字层 | 网页 PDF 文字层 |
|---|---|---|---|---|---|
| `一之富士` | 0 | 0 | 0 | 0 | 0 |
| `义之富士` | 2 | 2 | 2 | 2 | 2 |
| `義ノ富士`（日文） | 4（:120/:187/:189/content8:21） | 2 整串（:449、:1048；key 47 题干在 :509–510 跨行拆分，已核实） | 2 整串（P4 1、P8 key 47 题干 1；key 115 题干跨 <text> 换行） | 题干完整呈现 | 题干完整呈现 |
| `義之富士`（繁体形） | 0 | 0 | 0 | — | — |
| `一之酉`（正确，应保留） | 1（content12.py:261） | 1（:1217） | 1 | — | — |

- key 47 与 key 115 同一人核实：两题干均指「初日大の里败给義ノ富士」，
  简析分别为 content34.py:186 与 content8.py:20，键均为 A。
  公开来源（スポニチ/サンスポ/デイリー/報知/読売）确认初日结果无误。

## 3. 机械门

| 门 | 结果 |
|---|---|
| freeze baseline 第 1 次 | 8/8 SVGs byte-identical；core integrity：运行前后重哈希一致 |
| freeze baseline 第 2 次（同一解释器重跑） | 8/8，哈希与第 1 次逐个一致；p8 `f7118644ac8b31a4…` 与 fix1 声称一致；P1–P7 哈希与 fix1 记录的修前值一致 |
| occlusion（`tools/occlusion_audit.py`） | 自检通过（6 类 planted 全触发，clean 对照静默）；0 flags |
| p8 extract（`tools/p8.py extract --total 150`） | noted set 150/150（`p8-extract.json`） |
| p8 compare（core-vs-core） | status CLEAN；missing=[]、extra_count=0、uncertain=[]、**keydiff=[]**（注：[137,138,139,140] 是 fan-out vs 核心的预期，核心自比正确预期为空；E 组键 137–140 在核心本就是中文句，已逐条核对无误） |
| p8 extract vs 修前 extract（`ja-core-p8.json`） | noted 集相等，keys 150/150，0 key diffs |
| print/web 文字层（raw） | 各 44,818 B，`cmp` 逐字节一致 |
| print/web 文字层（-layout） | 各 85,061 B，`cmp` 逐字节一致 |
| text.md validator（SVG 重导出比对） | 重导出与交付 text.md 逐字节一致（1356 行） |
| U+2019 全扫 | SVG + text.md + content\*.py 合计 0 |
| VOL.4 核对 | P1 3×、其余各版 1× |
| 徽章计数 | P1–P7 112 题、P8 38 题逐题映射，缺徽 0、错徽 0（组徽章 25–28/43–46/141–144 共用 1 徽，W46 同版式）；P1 目录 4 个版级徽与 §4 版级一致 |
| P8 最小字号（PyMuPDF，印刷 PDF） | 全期各版最小 11.62/12.75pt；P8 最小 **9.98pt**（≥9.75pt 门槛）；P8 题干 10.35pt（79 处） |
| §1.1 grep 审计 | 旧纸色 `#f7f1e2` 0×；禁用金 `#c9a227` 0×；`·`（除图片 base64 外）0×；`第N版／共8版` 1×/版；纸色 `#fbfaf6` 1×/版 |
| 金句 8× 各 2× | 去空白全文计数，8 条裸句各恰为 2 |
| 禁忌行首扫描 | 0 hits |

## 4. 150 键逐题复核（登记 vs 印刷 P8 答案行）

- 登记 dump（freeze build-copy 内重跑，`registry-proof2.json`）：TOTAL 150，
  n 1–150 连续，级别 A2 48 / B1 73 / B2 29，分版 10/18/18/18/18/18/12/38，
  题型与 KIT 一致，范文 154 字。
- 登记键 vs p8 extract 键：仅 150 题一处差异（登记「（开放题，范文如下）」
  vs 印刷「✓」），W46 既定冻结版式，与修前逐字节一致。
- 登记「`{n}. {key} — {note}`」vs text.md 答案行：149/150 逐字一致；
  仅 150 题同上冻结版式差异。
- 人工逐题核对键值与题干/正文：P4 47–64、P6 图表 88–93
  （38−24=14、38+24=62、合计 100）、P6 日期 94–97、P8 A–G 组 113–149
  全部复算无误。

## 5. 8 版目视（自运印刷 PDF 100 dpi；网页版 P8 同分辨率；P8 key 47 区 300 dpi 放大）

| 版 | 结果 |
|---|---|
| P1 | 干净；头条、趋势栏、目录、快讯、闪电问答、页脚均清晰，无溢出重叠 |
| P2 | 干净（特征栏中段空白为 KIT §7 已披露的 W46 冻结版式） |
| P3 | 干净；葡萄园图 + 图注 + 文化日历正常 |
| P4 | 干净；ex 47 题干「義ノ富士」正确；记录盒「琴櫻」正确；收尾横条正常 |
| P5 | 干净；岚山图 + 流行语栏正常 |
| P6 | 干净；图表标签与柱条分离（京都/浅草/高尾山/家），练习区正常 |
| P7 | 干净；诊所栏、金句栏、鸟居图 + 图注（2025年11月24日）、读者园地披露、VOL.5 预告正常 |
| P8 | 干净；练习流、范文（154 字）、寺图、答案区完整，答案流未压页脚；300 dpi 放大确认 key 47「47. A — 首日战胜大之里的是义之富士」字形清晰；网页版 P8 版式与印刷版一致，key 47 行相同 |

## 6. 事实抽查（公开来源，见 PROOF-NOTE §5）

相扑初日～3 日目（スポニチ/サンスポ/デイリー/報知/読売）、酉の市 2026
（鷲神社官网引述二次来源）、博若莱 2026（阪急阪神 PR/サントリー）、
流行语大赏 2026（ORICON/モデルプレス）、红叶三家预报与嵐山 11月8日
实况（Weathernews 官方/共同 PR、yuuekiinfo.com、日本気象株式会社）、
全部日期/星期（`date -d`，Asia/Tokyo）——均与文中一致，无事实错误。

## 7. 结论

**(a) 零问题**（SOP §8.4）。fix1 的 1 处改对；观察项 3 条（O1 りくりゅう罗马字
译注口径、O2 ex 103 选项平行、O3 露店 750 店异口径已披露）不计缺陷；
另案 R1（KIT §3 罗马字 Umi-no-umi/Fujiryūga 仅存于 KIT 内部记录，
读者可见交付物为 0）按任务要求只报告、不列为本轮缺陷。

## 8. 未跑 / 未动

- 未跑 insert.py、lint --write；未 git add/commit/push/reset/stash
  （除开工探针 `git hash-object -w`）。
- 未碰 W43–W46、其他目标语家庭、tools/、issues/；未改任何源码/成品。
