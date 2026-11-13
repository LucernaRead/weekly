# W47 fan-out 建版盘点 — en / es / it / pt / ru / nl

- 盘点员：家庭建版盘点员（只调查、不建版、不修、不 commit、不 push、不派 subagent）
- 实测时间：2026-11-11 09:30–09:45 UTC（探针 09:27 UTC 通过）
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 成功（`9daeafb9…`）+ `hidden_files/w47/probe-inventory-families.txt` 真实写盘成功
- 先读：SOP.md §8 / §1.1 全文、`AGENTS.md`、协调员 brief、ledger.md 全文、run-log.md 尾部（`iconv` 绕过一处无效 UTF-8 字节后读）
- 方法：全量实测，不信任任何回报——每版印刷 PDF / 网页 PDF / text.md 逐个 `sha256sum` + 字节数；`pdfinfo` 核 8 页；`pdftotext` 核文字层；`find -size 0` 扫零字节；PROOF-NOTE.md 逐份读结论并把其记录的 SHA 与盘上 SHA 逐字比对；FANOUT-REPORT-{fam}.md 逐份把记录的 SHA 与盘上 SHA 交叉比对

## 范围说明

- 六个家庭各 10 版，共 60 版。核心版（`core-{fam}/`）即该目标语的 **zh-cn 读者版**（如 core-en 内是 `The-Lucerna-VOL4-en-zh-cn.pdf`），所以每家庭 fan-out 为除 zh-cn 外的 10 个读者语：de、en、fr、es、it、pt、nl、ru、ja、ko、zh-tw（各家庭缺哪一个读者见总表注）。
- en/es/it/pt/ru 五家庭版目录在 `production/2026-w47/2026-w47-{fam}-{reader}/`；**nl 家庭 10 版全在 `production/2026-w47/fanout-nl/2026-w47-nl-{reader}/`**（不在 production 根目录，见 §4 第 3 项）。

## 1. 总表（家庭 × 读者语）

图例：建成 = 目录在 + 印刷/网页 PDF + text.md + KIT + ABSTRACT 全在（另经 `pdfinfo` 8 页 + 文字层 >0 + 零字节文件 0 个，见 §1.1）；
proof1 状态：`✅(a)` = 独立复校 (a) 零问题且其记录 SHA 与盘上一致（可定稿）；`(b)→P2✅` = proof1 (b) → fix1 → proof2 (a) 且 SHA 与盘上一致；
`(b)→P3跑` = proof1/2 均为 (b)，proof3 在跑；`—` = 盘上无任何 PROOF-NOTE（proof1 从未出结论）。

### en 家庭（10/10 建成）

| 读者 | 建版状态 | 三件齐否 | proof1 状态 |
|---|---|---|---|
| de | 建成 | 齐（印 29,330,766 / 网 2,377,894 / 文 51,948） | (b)→P2✅ 定稿（P1(b) D1 P7 金句#8孤行；fix1 后 P2(a) 08:29） |
| es | 建成 | 齐 | — 待派 |
| fr | 建成 | 齐 | — 待派 |
| it | 建成 | 齐 | — 待派 |
| ja | 建成 | 齐 | — 待派 |
| ko | 建成 | 齐 | — 待派 |
| nl | 建成 | 齐 | — 待派 |
| pt | 建成 | 齐 | — 待派 |
| ru | 建成 | 齐 | — 待派 |
| zh-tw | 建成 | 齐 | — 待派 |

### es 家庭（10/10 建成）

| 读者 | 建版状态 | 三件齐否 | proof1 状态 |
|---|---|---|---|
| en | 建成 | 齐（印 3,500,745 / 网 849,020 / 文 44,386） | ✅(a) 定稿（P1(a) 07:40，SHA 与盘上一致） |
| de | 建成 | 齐（印 3,503,020 / 网 852,182 / 文 44,739） | (b)→P2✅ 定稿（P1(b) D1/D2 P1 版式；fix1 后 P2(a) 08:37） |
| fr | 建成 | 齐 | — 待派 |
| it | 建成 | 齐 | — 待派 |
| ja | 建成 | 齐 | — 待派 |
| ko | 建成 | 齐 | — 待派 |
| nl | 建成 | 齐 | — 待派 |
| pt | 建成 | 齐 | — 待派 |
| ru | 建成 | 齐 | — 待派 |
| zh-tw | 建成 | 齐 | — 待派 |

### it 家庭（10/10 建成）

| 读者 | 建版状态 | 三件齐否 | proof1 状态 |
|---|---|---|---|
| en | 建成 | 齐（印 14,032,990 / 网 1,259,104 / 文 55,274） | (b)→P2✅ 定稿（P1(b) D-1 text.md「翻译」×4；fix1 只改 text.md，P2(a) 08:15） |
| de | 建成 | 齐 | — 待派 |
| es | 建成 | 齐 | — 待派 |
| fr | 建成 | 齐 | — 待派 |
| ja | 建成 | 齐 | — 待派 |
| ko | 建成 | 齐 | — 待派 |
| nl | 建成 | 齐 | — 待派 |
| pt | 建成 | 齐 | — 待派 |
| ru | 建成 | 齐 | — 待派 |
| zh-tw | 建成 | 齐 | — 待派 |

### pt 家庭（10/10 建成）

| 读者 | 建版状态 | 三件齐否 | proof1 状态 |
|---|---|---|---|
| en | 建成 | 齐（印 12,932,451 / 网 1,102,777 / 文 37,333） | (b)→P2✅ 定稿（P1(b) 3 类轻微；fix1 6 处后 P2(a) 08:18） |
| de | 建成 | 齐 | — 待派 |
| es | 建成 | 齐 | — 待派 |
| fr | 建成 | 齐 | — 待派 |
| it | 建成 | 齐 | — 待派 |
| ja | 建成 | 齐 | — 待派 |
| ko | 建成 | 齐 | — 待派 |
| nl | 建成 | 齐 | — 待派 |
| ru | 建成 | 齐 | — 待派 |
| zh-tw | 建成 | 齐 | — 待派 |

### ru 家庭（10/10 建成）

| 读者 | 建版状态 | 三件齐否 | proof1 状态 |
|---|---|---|---|
| en | 建成 | 齐（印 21,245,374 / 网 3,375,060 / 文 56,600） | (b)→P3跑（P1(b) D1/D2；fix1 后 P2(b) D3 网页独有；webpdf 斜体补丁重建后 P3 在跑，见 §1.2） |
| de | 建成 | 齐 | — 待派 |
| es | 建成 | 齐 | — 待派 |
| fr | 建成 | 齐 | — 待派 |
| it | 建成 | 齐 | — 待派 |
| ja | 建成 | 齐 | — 待派 |
| ko | 建成 | 齐 | — 待派 |
| nl | 建成 | 齐 | — 待派 |
| pt | 建成 | 齐 | — 待派 |
| zh-tw | 建成 | 齐 | — 待派 |

### nl 家庭（10/10 建成，位置在 fanout-nl/）

| 读者 | 建版状态 | 三件齐否 | proof1 状态 |
|---|---|---|---|
| en | 建成 | 齐（印 12,665,899 / 网 1,574,228 / 文 45,074） | (b)→P2✅ 定稿（P1(b) D1 U+2019 弯撇号；fix1 后 P2(a) 08:24） |
| de | 建成 | 齐 | — 待派 |
| es | 建成 | 齐 | — 待派 |
| fr | 建成 | 齐 | — 待派 |
| it | 建成 | 齐 | — 待派 |
| ja | 建成 | 齐 | — 待派 |
| ko | 建成 | 齐 | — 待派 |
| pt | 建成 | 齐 | — 待派 |
| ru | 建成 | 齐 | — 待派 |
| zh-tw | 建成 | 齐 | — 待派 |

### §1.1 三件齐全的实测口径（60 版全部通过）

- 印刷 PDF 与网页 PDF 均为 8 页（`pdfinfo` 逐版核，60/60）；网页 PDF 文字层 44,142–58,554 字节，全部 >0；印刷文字层与网页文字层基本一致（差值 0–110 字节，见 §5 末尾说明）。
- 60 个版目录树内零字节文件 0 个；每版 `svg/` 均为 8 个文件；每版 `ABSTRACT.txt` 在；每版 `WEEKLY-KIT.md` 在。
- **EDITION-RECORD.md：60/60 缺失**（版目录内无，各家庭 scratch 目录内亦无；de/ko/fr/ja 四家庭有，en/es/it/pt/ru/nl 六家庭全无——见 §4 第 1 项）。

### §1.2 ru-en proof3 在跑的盘上证据

`hidden_files/w47/scratch-proof-ru-en3/` 有工作文件（`verify3*.py/json`、`freeze-diff.json`、`occlusion.json`、`p8-compare.json`，mtime 09:23–09:29 UTC），**无 PROOF-NOTE.md**（09:30 UTC 实测）。其前序：P1(b) D1 P5 弯双引号全宽 + D2 网页 "14-й" 假空隙；fix1 后 P2(b) D3 网页独有（空格丢失/闭引号脱开 3.354pt/斜体丢失，工具层）；webpdf 斜体补丁已落地，网版已重建为 `6419f7ad…`（盘上 3,375,060 字节，与 KIT §7 一致），P3 复核中。

## 2. en 家庭专项说明（d132d807 回报未送达，只认盘上实测）

**结论：en 家庭 10/10 实测完整，无半成品残留。** 第一棒（d132d807）报告的“完成”与盘面不符的状态，已被第二棒全部重建，证据在盘上，不依赖任何人口头回报：

1. **半成品原状（第二棒接手时，记于 en-de KIT §8，盘上可验）**：第一棒报 en-de 完成零问题，但盘上只有 8 张 SVG + 8 张卡片 PNG，**无 PDF、无 WEEKLY-KIT.md、无 .text.md、无 ABSTRACT.txt**；`de/build.log` 为 0 字节空文件；`occlusion.log`、`p8-compare.json`、`p8-extract.json`、`freeze-diff.json` 全部早于最后一次 SVG 渲染（00:51–00:55 vs SVG 01:01–01:02），即门禁全是过期快照。
2. **重建结果（实测）**：10 版全部三件齐全 + KIT + ABSTRACT + 8 SVG；`pdfinfo` 全部 8 页；文字层印/网基本一致（en 家庭 10 版差值 0–2 字节）；60 版范围零字节文件 0 个；各版 KIT 均引述 freeze-diff 结论（英文正文未动，见 §5）。
3. **en-de 的复校链已闭合**：P1(b) D1（P7 金句#8 出处行孤悬第 3 栏顶）→ fix1（只改 `content7.py` 两处德语 gloss 行 + 只 `p7-lang.svg` 变）→ P2(a) 零问题（`scratch-proof-en-de2/PROOF-NOTE.md`，08:29 UTC），其记录的印/网 SHA（`6f82363a…`/`b2b686e4…`）与盘上逐字一致。**en-de 是 en 家庭唯一已定稿版。**
4. **其余 9 版（es/fr/it/ja/ko/nl/pt/ru/zh-tw）**：建版完成、自查据 KIT/报告称零问题，但**无任何 proof1 记录**，在 §3 待派清单内。FANOUT-REPORT-en.md 的 9 版印/网 SHA 与盘上逐字一致，仅 en-de 一行过期（报告写于 06:01 UTC，fix1 之前——预期内，见 §4 第 4 项）。

## 3. proof1 待派清单（53 版：已建成、三件齐全、无 proof1 结论）

优先级按任务口径“先有 KIT 的、再无 KIT 的”——**60 版全部有 KIT，故本清单 53 版全部属于“有 KIT”一档，无“无 KIT”一档**；以下按家庭排序，家庭内按读者语字母序。每版位置：en/es/it/pt/ru 在 `production/2026-w47/2026-w47-{fam}-{reader}/`，nl 在 `production/2026-w47/fanout-nl/2026-w47-nl-{reader}/`。

- **en（9 版）**：en-es、en-fr、en-it、en-ja、en-ko、en-nl、en-pt、en-ru、en-zh-tw
- **es（8 版）**：es-fr、es-it、es-ja、es-ko、es-nl、es-pt、es-ru、es-zh-tw
- **it（9 版）**：it-de、it-es、it-fr、it-ja、it-ko、it-nl、it-pt、it-ru、it-zh-tw
- **pt（9 版）**：pt-de、pt-es、pt-fr、pt-it、pt-ja、pt-ko、pt-nl、pt-ru、pt-zh-tw
- **ru（9 版）**：ru-de、ru-es、ru-fr、ru-it、ru-ja、ru-ko、ru-nl、ru-pt、ru-zh-tw
- **nl（9 版）**：nl-de、nl-es、nl-fr、nl-it、nl-ja、nl-ko、nl-pt、nl-ru、nl-zh-tw

不在本清单的 7 版：已定稿 6 版（en-de、es-en、es-de、it-en、pt-en、nl-en，见 §1）+ ru-en（proof3 在跑，见 §1.2）。另注意：ledger/run-log 记载的 proof1 派单只覆盖过 *-en 与 *-de 版；除上述 7 版外，盘上（`hidden_files/w47/scratch-proof-*` 全量 + `/tmp` 扫查）无其他任何一版的 PROOF-NOTE。

## 4. 阻塞清单

**按任务定义（缺件 / 半成品 / 无 KIT 的版）：0 版。** 60 版无一缺件、无一半成品、无一无 KIT。

以下是不阻塞建版、但须协调员知晓/处置的缺口（只记录，不裁定）：

1. **EDITION-RECORD.md 全缺（60/60）**：六家庭的版目录与 scratch 目录内均无 EDITION-RECORD.md（de/ko/fr/ja 家庭有此文件）。各版 KIT 在，可作替代准源；是否补写由协调员定。
2. **FANOUT-REPORT-it.md 缺失**：全仓（`hidden_files/w47` + `production/2026-w47`）无此文件。it 家庭只有 `scratch-fanout-it/STATUS.md`，其尾部内容已过期——描述的是第一棒 EDQUOT 停工态（it-en 未完成、其余 9 版未开始），与盘面矛盾（10 版全建成、it-en 已 proof2(a)）。接替棒（7e0db518）完成了建版但未留合并报告；it 各版 KIT 在盘，可作准源。
3. **nl 家庭版目录位置**：10 版全在 `production/2026-w47/fanout-nl/`，不在 production 根目录。FANOUT-REPORT-nl.md 自述“(not moved; coordinator decides later)”——是否移入根目录待协调员定。insert 阶段须注意此路径。
4. **各家庭报告的 *-en 行 SHA 过期（预期内，非盘面问题）**：en/es/pt/ru/nl 五份 FANOUT-REPORT 与盘上逐版比对——每份恰好只有 *-en 版的印/网 SHA 与盘上不符，因为报告写于 fix1 之前（en 06:01、es 06:08、pt 06:07、ru 06:47、nl 05:24 UTC 末次修改）；其余 9 版/份全部逐字一致。准源为各版 KIT + 复校笔记，不以报告尾部 SHA 为准（与 de 家庭的教训一致）。
5. **ru-en proof3 未出结论**（见 §1.2），在跑中，非阻塞。
6. **印/网文字层微差（工具层已知项，非逐版阻塞）**：除 ru-en（57,149/57,149 逐字节一致）外，多数版印/网文字层差 1–110 字节（最大 it-ru 110 字节、ru-ja 64 字节）；与已知 webpdf weight/italic 工具差异同类，协调员已有 pre-insert 全量网页 PDF 重建计划，此处只记录。

## 5. KIT 核心 SHA / 建版时间记录（只记录，不裁定是否重建）

1. **无一版 KIT 登记核心 SHA**：60 份 fan-out KIT 全量 grep——没有任何一份写有核心版 PDF/SVG 的 SHA-256 值。KIT 登记的是来源表述（“copied whole from `core-{fam}/`”）+ freeze 基线 8/8 + freeze-diff 摘要（新增 = 本读者语讲解层，移除 = 核心中文讲解层；en 家庭 10 版均另写“英文正文未动”）。
2. **六核心当前盘上 SHA（实测，供核对各版是否建自当前核心）**：

| 核心（= zh-cn 读者版） | 印刷 PDF（字节 / SHA-256 前 16） | 网页 PDF（字节 / SHA-256 前 16） | PDF mtime (UTC) |
|---|---|---|---|
| core-en | 41,407,278 / `ca1ab6c02906a39f` | 2,765,419 / `2ee5391f00d1b532` | 11-10 21:57 / 22:02 |
| core-es | 17,212,236 / `4787e5c8243426fa` | 1,372,318 / `6e8fb9c8fbb0aeb6` | 11-10 21:39 / 21:40 |
| core-it | 27,726,384 / `fc5e952d08c00092` | 1,758,563 / `4381cdf740fc6d9a` | 11-10 21:59 / 22:01 |
| core-pt | 25,311,662 / `f1ca8a2a65c2d10c` | 1,571,251 / `520bebfd720e4464` | 11-10 22:16 / 22:19 |
| core-ru | 31,429,156 / `4b56429722dbbf45` | 3,992,881 / `8a2649263171727e` | 11-11 00:10 / 00:13 |
| core-nl | 25,955,551 / `d661b63830be6b44` | 2,067,793 / `9b583aa9f9ca42cc` | 11-10 21:59 / 22:03 |

3. **核心 PDF 全部早于 fan-out 建版**：六核心印刷/网页 PDF 的 mtime 为 11-10 21:39 至 11-11 00:13 UTC；六家庭最早的 fan-out 网页 PDF mtime 为 en 02:51、es 02:03、it 01:39、pt 02:45、ru 02:35、nl 03:13（均为 11-11 UTC）。其后 ledger 未记这六核心有任何重建（de/ja/ko/zh-tw/zh-cn 核心的重修均不在本次六家庭内）。
4. **一项须留意的异常（只记录）**：`core-en/svg/` 内 8 个文件 mtime 为 **2026-11-11 02:06–02:07 UTC**，晚于核心印刷 PDF（11-10 21:57），且正在 en 家庭拷贝/建版窗口内（en-de 目录建于 01:54 UTC）。但 10 份 en KIT 引述的 freeze-diff 均只含讲解层增减（de 版 fix1 重跑 08:05、es/fr diff 跑于 02:49/03:26、it/ja/ko/nl/pt/ru/zh-tw diff 跑于 03:48–05:55，全部晚于 02:07），未见冻结正文漂移的记录；是否须重跑 freeze 核对，由协调员裁定，本盘点不裁定。
5. **另记**：nl 家庭报告称核心 slug 为 `2026-w47-nl-zh-cn`，与实测 core-nl 内文件一致；其报告中“Source: frozen core … (slug 2026-w47-nl-zh-cn …)”一句无误。es-en KIT 自述 fan-out 源为“定稿 core `core-es/`（zh-cn reader edition）”，与实测一致。

## 附录 A：60 版三件套全量 SHA-256 实测（字节数 / SHA 前 16 位；完整 SHA 见各版 KIT §7 或盘上 `sha256sum`）

| 版 | 印刷 PDF | 网页 PDF | text.md |
|---|---|---|---|
| 2026-w47-en-de | 29330766 / `6f82363a63477603` | 2377894 / `b2b686e4f9064ef4` | 51948 / `0243670305ae1926` |
| 2026-w47-en-es | 29330745 / `e668bc5f40f8c6e3` | 2377727 / `a0a2f9d6d3035e4d` | 53837 / `850fee7a0f459428` |
| 2026-w47-en-fr | 29330444 / `14da9810fa348a57` | 2376712 / `0f188504a65e1348` | 53239 / `b882d0e9f348bcee` |
| 2026-w47-en-it | 29326709 / `195e155228e63515` | 2372517 / `995339d48612cc93` | 53373 / `a9cbd2f18c6ecfee` |
| 2026-w47-en-ja | 41509526 / `5cfb282caa800c34` | 2843624 / `f20c1affd5a53ab2` | 52982 / `1fcc919c1d72958c` |
| 2026-w47-en-ko | 32386030 / `983ad19cbd400836` | 2594367 / `e2439e78fc3d5515` | 52965 / `9020d107dc95860e` |
| 2026-w47-en-nl | 29340703 / `5b2a364b60fb5537` | 2375438 / `f1d2b8f43600e39a` | 52965 / `3e21e424fbc2237a` |
| 2026-w47-en-pt | 29345286 / `50484ca9c0ef2323` | 2381728 / `c150c65509fa722e` | 53549 / `329a027375eda3fe` |
| 2026-w47-en-ru | 29241566 / `788cd0c08ec9b72f` | 2417491 / `da80486218d001cc` | 61835 / `5e8f7bf4f8e4b9d8` |
| 2026-w47-en-zh-tw | 38152082 / `d2e919473d70463a` | 2927283 / `df41f1fc1a6786b8` | 50505 / `6ecf354e4e614c77` |
| 2026-w47-es-de | 3503020 / `e97c5acc601179bc` | 852182 / `7760133bec9f34b9` | 44739 / `9b6d61cac662ec91` |
| 2026-w47-es-en | 3500745 / `e881ebb9c50efe59` | 849020 / `8ab8c66cc9c4e642` | 44386 / `886b6af5e84dde8f` |
| 2026-w47-es-fr | 3499799 / `c1c3ecdc326da7d9` | 846204 / `e6e5abbf4f923e4d` | 45272 / `94476219c438fc47` |
| 2026-w47-es-it | 3498408 / `d4eaaf2fd3f955c1` | 845673 / `24bd25008151e3dd` | 44644 / `a2c3606482b56d17` |
| 2026-w47-es-ja | 17294297 / `de40fa29ee957b64` | 1503253 / `859b4421086697da` | 46018 / `e1486c4686b7a0d2` |
| 2026-w47-es-ko | 8874275 / `ba1a6e0a23a404c5` | 1199171 / `9117f3c186ee3aec` | 46843 / `ddf077f538a34bb9` |
| 2026-w47-es-nl | 3502220 / `f88a21414c77508b` | 850386 / `85240de829be6755` | 44788 / `8801edefd46f58ea` |
| 2026-w47-es-pt | 3500787 / `4793edeb87c2d6cd` | 847463 / `d7429fcb83d70735` | 44990 / `d3e4bd818b51f19b` |
| 2026-w47-es-ru | 3593674 / `1e727ff1d28dfcba` | 904435 / `b88bfd2ce822603c` | 51957 / `cee6c798e8ae7ea1` |
| 2026-w47-es-zh-tw | 17262202 / `23926bd9729a0411` | 1686124 / `3e96ea85cb5bfe3c` | 43246 / `0e6a0fbb89c1a686` |
| 2026-w47-it-de | 14037296 / `6903d98b3adb07c1` | 1265110 / `a62a094705fabd79` | 56734 / `851ac7af017672d3` |
| 2026-w47-it-en | 14032990 / `d41e7255d7da8ea6` | 1259104 / `32a6727966cfa130` | 55274 / `7160560555042d99` |
| 2026-w47-it-es | 14033685 / `9c7ee019b041a748` | 1259244 / `d05e956d056c76f8` | 56259 / `01791ae188a99e91` |
| 2026-w47-it-fr | 14034268 / `5445d1a62f631bb7` | 1258939 / `416b11053b82475a` | 56616 / `b3d5c147bb68d58c` |
| 2026-w47-it-ja | 28221078 / `f0fb8a83671a4d7b` | 1869651 / `b6660f12a4d57833` | 58239 / `87d1ec4e54d7dcae` |
| 2026-w47-it-ko | 19296953 / `522008ebdfed5295` | 1575451 / `a9bdc956ca19be6f` | 57376 / `10fdd97935a99a88` |
| 2026-w47-it-nl | 14034647 / `9322290029fa8175` | 1259635 / `6c546925c847f034` | 55590 / `49a5e6ead7d9b254` |
| 2026-w47-it-pt | 14036807 / `4492665b04a7a631` | 1262226 / `164492f8ab7b69f1` | 55820 / `438656e1f9b8317c` |
| 2026-w47-it-ru | 14181162 / `b70e7b62da565b7f` | 1407790 / `1c93b80d57de5e76` | 67722 / `7d3679679bccbaba` |
| 2026-w47-it-zh-tw | 27779760 / `6171fea645bd67e0` | 2042022 / `57e29e6ff725a3c0` | 52568 / `53c3ca77e2a365ed` |
| 2026-w47-pt-de | 12938940 / `a1b7bfc28e2a74b3` | 1110425 / `26647474dbeb7442` | 37905 / `f33307b8413e34a3` |
| 2026-w47-pt-en | 12932451 / `0146a4202b015f44` | 1102777 / `a974ef7ccf7c879f` | 37333 / `513326ffa497ca2b` |
| 2026-w47-pt-es | 12933122 / `faf2f098043d4126` | 1103156 / `8ef5e4200eef8d5c` | 37449 / `337bb77b771583be` |
| 2026-w47-pt-fr | 12934799 / `fe02b4fbb3a5869c` | 1104302 / `96190bcacb57c530` | 37687 / `f3cb6a085b203dc4` |
| 2026-w47-pt-it | 12930920 / `ea4e4fd80e9aa3f9` | 1100022 / `4c0d5069ba440d21` | 37404 / `178b5bb2dff8452c` |
| 2026-w47-pt-ja | 24992044 / `04f284ed6596a1b0` | 1644666 / `339d2b0517e4977f` | 37892 / `893e8574b6e1b6ce` |
| 2026-w47-pt-ko | 17185929 / `10c758cf1bab7444` | 1394979 / `b1b609fdf3437cd1` | 37797 / `fb9248014654f2b7` |
| 2026-w47-pt-nl | 12935390 / `5a58050b684893bb` | 1105901 / `30db8b9ca8a3331c` | 37571 / `c2ff3429ed601e7b` |
| 2026-w47-pt-ru | 12916544 / `d2822ae0ea1c50d1` | 1151627 / `a6a5f25f93265a89` | 39719 / `3d7597d949cf279f` |
| 2026-w47-pt-zh-tw | 24130201 / `ddc35d9b4c71d4c5` | 1781773 / `fff6b33550f85e71` | 36865 / `d3e70bf967f966fb` |
| 2026-w47-ru-de | 21226139 / `31fab92b7b1b392f` | 3347223 / `1a67d6b46352c3ae` | 57310 / `be89c4be9bc36eed` |
| 2026-w47-ru-en | 21245374 / `7b73070c2c11313a` | 3375060 / `6419f7ad188d0e6a` | 56600 / `2bf57f6808763372` |
| 2026-w47-ru-es | 21272810 / `acef924f8742bc78` | 3348591 / `788411a8c3aadd54` | 58041 / `734b7324c2cda3bf` |
| 2026-w47-ru-fr | 21260891 / `b9476fc2d49584d1` | 3346639 / `78a56be6b7094ce1` | 57356 / `0f1299e1c18e7d93` |
| 2026-w47-ru-it | 21260017 / `a3e17e19cca04a96` | 3345188 / `04fa800929cbf87e` | 57852 / `43327f39df9afd7c` |
| 2026-w47-ru-ja | 27404856 / `929a5c4786f256cb` | 3683942 / `fbfb35d3d34e7e19` | 58308 / `9242e2624663bfe5` |
| 2026-w47-ru-ko | 22002774 / `4e450e65c7c5dfb5` | 3474892 / `797af4e6e622d16a` | 58811 / `d67d7f495af15de8` |
| 2026-w47-ru-nl | 21285839 / `59d16202fb04c4b9` | 3348435 / `1c860fc77a9a1b2a` | 57863 / `76a4490691891228` |
| 2026-w47-ru-pt | 21199772 / `e6171dabf8d87161` | 3344677 / `cc8fea68fcf0c829` | 58994 / `3d0bb5bfd59b6c20` |
| 2026-w47-ru-zh-tw | 24785168 / `69239a09d74a478e` | 3963820 / `543ce70dd628ee47` | 54642 / `989f01b7d5ff3775` |
| 2026-w47-nl-de | 12669843 / `0df8e6146159d459` | 1581124 / `8859e18a23b46d84` | 46161 / `1531c25ee6ec4844` |
| 2026-w47-nl-en | 12665899 / `2cc431f2572abad8` | 1574228 / `0fc6232bbe2bd8d3` | 45074 / `1d69f5edc43e217b` |
| 2026-w47-nl-es | 12669477 / `47f15cc8cb137a22` | 1579768 / `4b416858f1412e22` | 47276 / `86837159583a2dcf` |
| 2026-w47-nl-fr | 12704394 / `e6db69e3cb07c805` | 1577894 / `d26a0b571ddb268c` | 47536 / `bc9c9f0056d9c1b5` |
| 2026-w47-nl-it | 12715556 / `a05cc4be4048cc23` | 1575654 / `072c7f2e808ad6c9` | 46851 / `7652632d685a4001` |
| 2026-w47-nl-ja | 26049268 / `af010c1f2d2f0d39` | 2119188 / `07243a6bc87aee40` | 47592 / `6685d681c585eca2` |
| 2026-w47-nl-ko | 17281555 / `d72e53eb31c222fb` | 1884427 / `a5b50f5985fa7da5` | 47383 / `bbca93462db80962` |
| 2026-w47-nl-pt | 12671956 / `d70937d8fb72c5a6` | 1582075 / `05faf02640908dd0` | 46025 / `5b353380d17479bd` |
| 2026-w47-nl-ru | 12718342 / `d60da2784c30d283` | 1625792 / `22ac256f24bc3585` | 57044 / `2355c998b9964a3a` |
| 2026-w47-nl-zh-tw | 25995622 / `a2a8652111933af1` | 2343866 / `daab1ef20d80cf58` | 44126 / `9a049708c485af0d` |

注：印刷 PDF 文件名各家庭不同（en 用 `The-Lucerna-VOL4-en-{reader}.pdf`；es `La-Lucerna-VOL4-es-{reader}.pdf`；
it `La-Lucerna-VOL4-{READER}.pdf`；pt `A-Lucerna-VOL4.pdf`；ru `Lucerna-VOL4-ru-{reader}.pdf`；
nl `De-Lucerna-VOL4-nl-{reader}.pdf`）；网页 PDF：en 用 `.web.pdf`（带点），其余五家庭用 `-web.pdf`（连字符）——insert 阶段须兼容两种命名。

## 附录 B：复校笔记逐份核对（结论 + 其记录 SHA 与盘上比对）

| 版 | 笔记目录 | 结论 | 记录 SHA vs 盘上 |
|---|---|---|---|
| en-de | `scratch-proof-en-de1/` (07:57) | (b)：D1 P7 金句#8 出处行孤悬第 3 栏顶（轻微） | 记录印/网 `6d91162f…`/`e8c67461…` ≠ 盘上（旧 build，已 superseded） |
| en-de | `scratch-proof-en-de2/` (08:29) | **(a) 零问题**，fix1 已核 | `6f82363a…`/`b2b686e4…` = 盘上 ✅ |
| es-en | `scratch-proof-es-en1/` (07:40) | **(a) 零问题，可定稿** | GATE-LOG 印/网 `e881ebb9…`/`8ab8c66c…` = 盘上 ✅ |
| es-de | `scratch-proof-es-de1/` (08:05) | (b)：D1/D2 P1 版式（中） | 记录 `4919afbc…`/`69a3ae61…` ≠ 盘上（旧 build，已 superseded） |
| es-de | `scratch-proof-es-de2/` (08:37) | **(a) 零问题**，D1/D2 已修 | `e97c5acc…`/`7760133b…` = 盘上 ✅ |
| it-en | `scratch-proof-it-en1/` (07:47) | (b)：D-1 text.md Q137–140「翻译」×4（轻微） | `d41e7255…`/`32a67279…` = 盘上（PDF 未动） ✅ |
| it-en | `scratch-proof-it-en2/` (08:15) | **(a) 零问题** | 同上 PDF + 新 text.md `71605605…` = 盘上 ✅ |
| pt-en | `scratch-proof-pt-en1/` (07:41) | (b)：3 类轻微（D1 刊头标语歧义、D2 champion 错译、D3 P8 冒号后缺空格×4） | 记录 `40bc2f44…`/`8d2b5815…` ≠ 盘上（旧 build，已 superseded） |
| pt-en | `scratch-proof-pt-en2/` (08:18) | **(a) 缺陷 0 项**，fix1 6 处已核 | `0146a420…`/`a974ef7c…` = 盘上 ✅ |
| nl-en | `scratch-proof-nl-en1/` (07:53) | (b)：D1 P7 BRIEVEN 框 U+2019 渲染成 "Editor' s"（中） | 记录 `0b4dc8c0…`/`477dd85d…` ≠ 盘上（旧 build，已 superseded） |
| nl-en | `scratch-proof-nl-en2/` (08:24) | **(a) 零问题** | `2cc431f2…`/`0fc6232b…` + 文 `1d69f5ed…` = 盘上 ✅ |
| ru-en | `scratch-proof-ru-en1/` (07:57) | (b)：D1 P5 弯双引号全宽、D2 网页 "14-й" 假空隙 | 记录 `023d9fd1…`/`fab0fc44…` ≠ 盘上（旧 build，已 superseded） |
| ru-en | `scratch-ru-en-proof2/` (09:03) | **(b)：D3 仅网页**（空格丢失/闭引号脱开/斜体丢失） | 印 `7b73070c…` = 盘上；网 `82dfb6ea…` ≠ 盘上（斜体补丁后重建为 `6419f7ad…`） |
| ru-en | `scratch-proof-ru-en3/` | proof3 在跑，**无 PROOF-NOTE.md**（09:30 UTC 实测） | — |

盘上无其他任何一版的 PROOF-NOTE（`scratch-proof-*` 全量 + `/tmp` 扫查；`scratch-proof-es2/it2/pt2/nl2/en2/en3/ru` 等为核心版复校，非 fan-out）。
