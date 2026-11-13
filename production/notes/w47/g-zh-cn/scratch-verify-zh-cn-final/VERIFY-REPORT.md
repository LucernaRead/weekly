# W47 zh-cn 家 §8.4 终态核对报告（第二轮核对 / final）

- 核对员：本轮终态核对员（新派工人，与第二轮重校员 90628111、#5 核对员 ab814a87、建造者、第一轮校对员、修复者、*-ru 重建者均不同）
- 核对时间：2026-11-13 ~07:15 UTC（02:15 EST）
- 磁盘：`df -h` 97G 已用 / 150G（`df -k` 101,696,028 KB；配额上限约 105G，余约 8G）；未触 100G（GiB）停手线。全程只读核对，未渲染、未改任何生产文件，未 commit/push/lint --write，未跑 run.py/render.py。
- 依据：`~/workspace/weekly-git/SOP.md` §8 全文已读（校对闭环 §8.1–§8.6、附则一几何审计、附则二工具化）。
- 工作目录：`hidden_files/w47/scratch-verify-zh-cn-final/`（本报告；无第二阶段重校，故无 PROOF-NOTE）
- 上轮核对：#5 轮（工人 ab814a87，2026-11-13 05:27 UTC），`scratch-verify-zh-cn/VERIFY-REPORT.md`，结论 10/10 CLEAN。

## 版数澄清（11 个目录，10 版）

磁盘上有 11 个目录：10 个 fan-out（`2026-w47-zh-cn-{de,en,es,fr,it,ja,ko,nl,pt,ru}`）+ `core-zh-cn`。
法定版数为 **10 版**（读者语 de/en/es/fr/it/ja/ko/nl/pt/ru）。`core-zh-cn` 是构建源，不单独算一版：

- core 的 `2026-w47-zh-cn-en.text.md` 与 fan-out `zh-cn-en` 的同名文件逐字节相同（SHA `2aaf8992bbc2…`，49,447 B）；
- core 印 PDF `Lucerna-VOL4.pdf` 与 fan-out 印 PDF `Lucerna-VOL4-EN.pdf` 逐字节相同（SHA `566554e0ebc8…`，33,521,858 B）；
- en 版有自己独立的 fan-out 目录与 EN 命名 PDF，实际存放处是 fan-out 目录，不是 core（不符合 W46 core 兜底模式的第 11 版证据）。
- 无第 11 版证据。以下按 10 版核对（core 只作交叉核对行）。

## 结论总览：CLEAN

| 版 | 最新核对 + 工号 | 结论 | 核对 SHA（印/网/文） | 磁盘 SHA | 一致？ | KIT §7 一致？ | 本轮结论 |
|---|---|---|---|---|---|---|---|
| zh-cn-de | 第二轮 PROOF-NOTE-2，90628111，(a) | (a) 干净 | 印 `b104a8b7b81b` / 网 `31fffc7ff93c` / 文 `e11d4f915226` | 相同 | 是 3/3 | 是（Artifacts final + Post-proof fix 各记一次） | **VERIFIED CLEAN** |
| zh-cn-en | 第二轮 PROOF-NOTE-2，90628111，(a) | (a) 干净 | 印 `566554e0ebc8` / 网 `2579a61027eb` / 文 `2aaf8992bbc2` | 相同 | 是 3/3 | 是（Post-proof fix 节记一次） | **VERIFIED CLEAN** |
| zh-cn-es | 第二轮 PROOF-NOTE-2，90628111，(a) | (a) 干净 | 印 `91c8a84ce10b` / 网 `86df4f212879` / 文 `b5bf366bad5f` | 相同 | 是 3/3 | 是（Artifacts final + Post-proof fix 各记一次） | **VERIFIED CLEAN** |
| zh-cn-fr | 第二轮 PROOF-NOTE-2，90628111，(a) | (a) 干净 | 印 `30ea0661e5c7` / 网 `638e9293509b` / 文 `4cf31ce982f6` | 相同 | 是 3/3 | 是（Artifacts final + Post-proof fix 各记一次） | **VERIFIED CLEAN** |
| zh-cn-it | 第二轮 PROOF-NOTE-2，90628111，(a) | (a) 干净 | 印 `0649d5e84bdd` / 网 `9aef40aa18ad` / 文 `808250dde250` | 相同 | 是 3/3 | 是（Artifacts final + Post-proof fix 各记一次） | **VERIFIED CLEAN** |
| zh-cn-ja | 第二轮 PROOF-NOTE-2，90628111，(a) | (a) 干净 | 印 `1e4e8510174c` / 网 `21f0e9ba278c` / 文 `b0fa1af51e9f` | 相同 | 是 3/3 | 是（Artifacts final + Post-proof fix 各记一次） | **VERIFIED CLEAN** |
| zh-cn-ko | 第二轮 PROOF-NOTE-2，90628111，(a) | (a) 干净 | 印 `93cae6913685` / 网 `68597c56beb0` / 文 `9f58f841635d` | 相同 | 是 3/3 | 是（Artifacts final — fix round 1 + Post-proof fix 各记一次） | **VERIFIED CLEAN** |
| zh-cn-nl | 第二轮 PROOF-NOTE-2，90628111，(a) | (a) 干净 | 印 `8ac769437ff6` / 网 `fad4d6c11db0` / 文 `79666191a8b5` | 相同 | 是 3/3 | 是（Artifacts final, after fix1 + Post-proof fix 各记一次） | **VERIFIED CLEAN** |
| zh-cn-pt | 第二轮 PROOF-NOTE-2，90628111，(a) | (a) 干净 | 印 `fa6c12699c41` / 网 `bfc1a6e4b6bd` / 文 `0c9d9d5b97ac` | 相同 | 是 3/3 | 是（Artifacts final + Post-proof fix 各记一次） | **VERIFIED CLEAN** |
| zh-cn-ru | #5 轮全新全量重校，ab814a87，(a) | (a) 干净 | 印 `52aa381ae7dd` / 网 `3e47f038c53b` / 文 `1f11029b4e83` | 相同 | 是 3/3 | 是（Artifacts final 已更新为新 SHA + `## fix-xru` 节记新 SHA；文另见 Post-proof fix 节） | **VERIFIED CLEAN** |
| core-zh-cn（交叉核对，非独立版） | 第二轮 PROOF-NOTE-2，90628111 | (a) | 印 `566554e0ebc8` / 网 `6c258be74dac` / 文 `2aaf8992bbc2` | 相同 | 是 3/3 | 是（Post-proof fix 节记一次） | 交叉核对一致（见下） |

- 10 版全部 VERIFIED CLEAN：最新一轮重校结论均为 (a)，其后磁盘三 SHA 逐字节未变，KIT 记录值亦一致。
- ru 版说明：第二轮指纹里的 ru 印/网旧值（`fd6977bff8b0` / `e5ce689b3811`）在第二轮之后由 *-ru 字体路由重建（2026-11-12 23:49–23:50 UTC）改写；#5 核对员已对新 SHA 做全新全量重校，结论 (a)，本轮磁盘实测与 #5 记录的新 SHA 逐字节一致，故 ru 版核对仍然有效，无需再做第二阶段重校。

## 磁盘实测 SHA-256 全表（2026-11-13 ~07:15 UTC）

| 版 | text.md（字节 / SHA-256） | 印 PDF（字节 / SHA-256） | 网 PDF（字节 / SHA-256） |
|---|---|---|---|
| core-zh-cn | 49,447 / `2aaf8992bbc20ebf1a0d7e652514ff0f345efd9e99e83e756779b777fd880521` | 33,521,858 / `566554e0ebc82c9fc5a6d9f89a96306be0f789337a6e49158b9872b376cc000d` | 2,434,907 / `6c258be74dac28cbbf5a6cd827117cdb75f1a95155ab2c875e26d04a9271968f` |
| zh-cn-en | 49,447 / `2aaf8992bbc20ebf1a0d7e652514ff0f345efd9e99e83e756779b777fd880521` | 33,521,858 / `566554e0ebc82c9fc5a6d9f89a96306be0f789337a6e49158b9872b376cc000d` | 2,434,914 / `2579a61027eb7b8be480e9d32353798a143a066b5fc5ae6bd625d50f9b5e8a07` |
| zh-cn-de | 50,640 / `e11d4f915226d3a252696c60641a1bfd4d0285ec464110858e599756d25d4b13` | 33,519,503 / `b104a8b7b81bb9eb666c3da7914d33d02f982c743c7bd6ef10bbb139f05fd1fd` | 2,433,265 / `31fffc7ff93c1436a44ad32761a8cfcd3c3275bb6c83b7f76480a164326475f5` |
| zh-cn-fr | 51,785 / `4cf31ce982f657d7c648b20c80b6eb7dfae9d53e2fe7edeadc38a51a16c6bc5d` | 33,513,599 / `30ea0661e5c764b9c04d29a0d3746fb823d97719385fd27ecffe2fa4a68007dd` | 2,427,467 / `638e9293509b75fdf19046c44726caea6789c1753197f4f326706e1606a295ac` |
| zh-cn-es | 51,137 / `b5bf366bad5f769616fdda577ee402cf2aa63e621b43e10669e97d690be9f7e7` | 33,515,603 / `91c8a84ce10bc86fdbb963b35532e8997c040bb4e90d1709af666640d0912582` | 2,428,933 / `86df4f21287966b1f1b2a8566bbc6be081d96f16a0b7cc67e148b4aeda9e0717` |
| zh-cn-it | 50,924 / `808250dde25028d7d34d76c0bd6a4c657df28d8713d86829d463d881874390f4` | 33,509,858 / `0649d5e84bdd6d07ed780a5f4aaa0737ebff4a1b632e06d26e7ca593ceafc739` | 2,423,711 / `9aef40aa18ad7d1bb53db3bd5c3033d587c3a112f667e0f39a332419bcefea0a` |
| zh-cn-pt | 50,798 / `0c9d9d5b97aca7aec7c76fa436f4df9feb0bde02414dbda4a4634616e63f6a49` | 33,516,115 / `fa6c12699c410f25d85604c518df7b1b603e2f1b49be435f4421e97e06fcd2c6` | 2,430,061 / `bfc1a6e4b6bdd37dcb17272e319eb0f459e2fe9c00fececc066273650c962d09` |
| zh-cn-nl | 50,025 / `79666191a8b5435549c244616133d62dbc12f1052e9de9bf642405ccb89a64c0` | 33,512,271 / `8ac769437ff6ae0f0ed81ef57961d6b4d48e9c3a032f614a0652b9379e25ab07` | 2,426,029 / `fad4d6c11db0d2657864faecb5d098e9a66bda383644cea37bd5cd256ff95545` |
| zh-cn-ru | 60,498 / `1f11029b4e83fed3e52a9fa84c380836bca7da34632a30ab210faafe2536036d` | 33,644,459 / `52aa381ae7dd22cd30cb06fa0a40c7e3db065d941d46fa71e732f14d1f45840a` | 2,557,060 / `3e47f038c53b5b5f082f7f367fecd0bf3aa8eec1a174b2026689a3068292808c` |
| zh-cn-ja | 52,408 / `b0fa1af51e9f841d7309070f6d9290de0c9590bac5739b5237ec38e9c4ae7883` | 35,542,435 / `1e4e8510174ce0cb97ae0238fe4c0ed3c0b969d07317ca6a459ad8af3ba5a72b` | 2,826,131 / `21f0e9ba278cea69e2862ab7acd5a6f7781f0040160253ebd5c00ea75c3691bb` |
| zh-cn-ko | 52,695 / `9f58f841635d07f2825a7ceeaf63494f98a11a8423dd81c1e882a4c8bb3dc0cf` | 36,955,671 / `93cae6913685c01f74d8a524f3bcde4eef7af642387090576f381edb2882cd22` | 2,807,966 / `68597c56beb09b01a243217b73fd7afbf065271e2106674fac414cd67273b656` |

- 与第二轮指纹（`scratch-reproof2-w47-zh-cn/fingerprints.txt`）逐项核对：除 ru 版印/网（已由 #5 重校覆盖）外，全部 30 个值字节与 SHA 均一致。
- 与 #5 报告 SHA-12 表逐项核对：33/33（含 core）字节与 SHA-12 均一致。

## 时效核对（证明后无改动）

- 生产 mtime：全部 10 版 fan-out 的印/网/text.md 最后修改均为 2026-11-12（15:59–17:14 UTC；ru 印/网 23:49–23:50 UTC），KIT 最后修改 2026-11-12 17:27–17:28（ru KIT 23:51）。
- `find … -newermt '2026-11-13 05:27:00 UTC'`（#5 核对时刻）：11 个目录内 **0 个文件**有更新。即 #5 核对之后生产树零改动。
- run-log 复核：#5 核对（05:27 UTC）之后至本轮的 run-log 条目（it 家核对、封面 caption 补丁、es-ru F1 修复、de round-3/round-4、协调员 #6 接手 07:10 UTC）均未触及 zh-cn 家生产目录；caption 补丁只动 `production/covers/` 的 cover.json 与封面块。
- 时序链完整：D5 重建（11-12 下午）→ 第二轮重校 PROOF-NOTE-2（11-12 ~18:18，工人 90628111）→ ru *-ru 重建（11-12 23:49–23:50）→ #5 全新全量重校 ru（11-13 05:27，工人 ab814a87，结论 (a)）→ 本轮时效核对（11-13 ~07:15）。无一版的核对在其后被生产改动推翻。

## KIT §7 核对（逐节定位，本轮独立重跑）

方法：对每版用完整 SHA-256 在其 KIT 内定位出现行，并确认所属章节为终态记录节（Artifacts (final) / Post-proof fix / fix-xru），而非仅历史旧值。

- de/es/fr/it/ja/pt：当前 3 SHA 各在 `## Artifacts (final)` 与 `## Post-proof fix — independent reproof F4–F9` 两节各出现一次。✓
- ko：当前 3 SHA 在 `## Artifacts (final — fix round 1, 2026-11-11)` 与 Post-proof fix 节各一次。✓
- nl：当前 3 SHA 在 `## Artifacts (final, after fix1 2026-11-11)` 与 Post-proof fix 节各一次。✓
- en（fan-out 目录 KIT）：当前 3 SHA 在 Post-proof fix 节（L768–L770）记一次；core KIT 同值在 Post-proof fix 节（L801–L803）记一次。✓
- ru：当前 3 SHA 在 `## Artifacts (final)`（L186–L192）与 `## fix-xru`（L278）记新值；text.md 另见 Post-proof fix 节（L267）。旧值 `fd6977bff8b0` / `e5ce689b3811` 仍在 KIT 历史记录中出现，属重建前旧值留存，非不一致。✓
- 结论：KIT §7 与磁盘一致，**wave-2 KIT 清单中无 SHA 更正项**。

## core-zh-cn 交叉核对

- core 印 PDF 与 zh-cn-en 印 PDF 逐字节相同（SHA `566554e0ebc8`，33,521,858 B）；core text.md 与 en text.md 逐字节相同（SHA `2aaf8992bbc2`，49,447 B）。
- core 网 PDF（`6c258be74dac`，2,434,907 B）与 en 网 PDF（`2579a61027eb`，2,434,914 B）差 7 字节：两份 KIT 各自记录了自己正确的值（core KIT 记 `6c258be74dac`，en KIT 记 `2579a61027eb`）；第二轮重校与 #5 核对均已记录此差异，提取文本逐字节相同，属非内容差异（元数据/字体子集化）。**不作缺陷，不入 wave-2。**

## 第二阶段：无需重校

- 磁盘 SHA 与核对记录不符的版：0；核对缺失的版：0。故按任务书第二阶段触发条件，**本轮不做任何全新全量重校**，未写任何 PROOF-NOTE，未渲染。
- O-R1（ru 版 KIT F8 advance 422.72→426.14）：已接受项，非缺陷；磁盘 SHA 与 #5 测量时一致，数值未变，无需重测。本轮沿用 #5 裁定：KIT F8 数值更新（422.7 → 426.1）列入 wave-2 记项，或由协调员另行裁定。
- zh-tw-ru KIT L35 笔误：KIT 文字问题，待 wave-2，不构成核对缺口（与本家无关，仅按任务书记录）。
- O4（ru 目录 `svglib.py.orig` 杂文件）：已处理——本轮复核生产树 11 个目录内 `*.orig` / `*.bak` 文件为 **0 个**（run-log 05:27 条：3 个 .orig 已移出生产树至 `scratch-fix-xru-heads/orig-backups/` 保存）。

## 全家结论：CLEAN

zh-cn 家 10 版 §8.4 定稿状态仍然成立：最新一轮重校结论全部为 (a)，核对后生产零改动，KIT §7 与磁盘一致，无 GAPS、无待修项（wave-2 记项仅 O-R1 的 KIT F8 数值更新一事）。

## 附：证据位置

- 第二轮重校：`hidden_files/w47/scratch-reproof2-w47-zh-cn/PROOF-NOTE-2.md` + `fingerprints.txt`（工人 90628111，2026-11-12 ~18:18，结论 (a) 零新发现）。
- #5 轮核对 + ru 全新全量重校：`hidden_files/w47/scratch-verify-zh-cn/VERIFY-REPORT.md`（工人 ab814a87，2026-11-13 05:27 UTC）；ru 重校日志 `scratch-verify-zh-cn/ru/logs/`、提取文本 `ru/print.txt` / `ru/web.txt`、P7 放大裁图 `ru/p7-head-zoom.png`。
- run-log / ledger：`hidden_files/w47/run-log.md`（#5 核对条 05:27 UTC；其后无 zh-cn 生产改动）、`hidden_files/w47/ledger.md`（L1136 架构澄清：core-zh-cn = zh-cn-en；L1267 zh-cn 家 10/10）。
- 本轮未动生产文件：全程只读（sha256sum、mtime、KIT grep）；未跑任何构建/渲染/门禁脚本（无 SHA 不符触发第二阶段，故无需重跑）。
