# W47 en 家 §8.4 终态核对报告（VERIFY-REPORT）

- 核对员：全新核对员（与建造者、二轮重校员 2f96abe3、#4 核对员 30e69a22、en-ru fix2 修复者 ff34ff71 均不同人）
- 时间：2026-11-13 07:13–07:17 UTC（02:13–02:17 EST）
- 范围：目标语 en，11 版：core-en（= 2026-w47-en-zh-cn）+ 2026-w47-en-{de,es,fr,it,ja,ko,nl,pt,ru,zh-tw}
- 方式：只读核对。未改任何生产文件，未 commit/push，未跑 lint --write/reset/stash/add -A；未碰 en 以外任何版；未派 subagent。
- 磁盘：开工 `df -k` 已用 101,696,028 KB = `df -h` 97G，未到 100G（GiB，即 104,857,600 KB）停手线；配额上限约 105G，余约 8G。本轮纯只读，未渲染（无此需要）。
- 工作目录：`hidden_files/w47/scratch-verify-en-final/`（本报告）

## 结论总览

**en 家 11/11 VERIFIED CLEAN，可定稿。**

- 10 版（core-en/en-zh-cn、de、es、fr、it、ja、ko、nl、pt、zh-tw）：最后重校（二轮，工人 2f96abe3，2026-11-12 ~18:30 UTC，`scratch-reproof2-w47-en/PROOF-NOTE-2.md`）结论 (a) CLEAN，且印/网/text.md 三 SHA + 字节数与本次磁盘实测逐版一致 → VERIFIED CLEAN，无需重校。
- 1 版（en-ru）：二轮后因 boxtitle fix2 重建改过印/网 SHA，#4 核对员 30e69a22（2026-11-13 04:56–05:10 UTC，`scratch-verify-en/VERIFY-REPORT.md`）已按 SOP §8 对当前磁盘态做过全新全量重校，结论 (a) CLEAN；本次实测三 SHA 与该重校记录逐项一致 → VERIFIED CLEAN，无需重校。
- KIT SHA 核对：11 版 KIT 内记录的印/网/text.md 完整 SHA-256（64 位）均与磁盘一致（33/33），wave-2 清单无待修项。
- 核对后零改动：en 家 11 个目录内 2026-11-13 05:10 UTC（#4 核对结束）之后无任何文件 mtime 变动；run-log / ledger 在 05:11 UTC 之后无任何 en 相关条目；不存在比 #4 更新的 en 家 PROOF-NOTE。
- 待修清单：无阻塞项、无须修复项。仅 1 项非缺陷观察（Q109，#4 报告 O1，已记 polish，不拦定稿，不修）。

## 数量核对

- 枚举：`2026-w47-en-*` 目录 10 个（de/es/fr/it/ja/ko/nl/pt/ru/zh-tw）+ `core-en` 1 个 = **11 版**，与任务书“10 或 11 版”相符，与 run-log 架构口径一致（core-en 即 en-zh-cn 读者版，无缺版）。

## 第一阶段——逐版时效核对

### 最新核对记录（每版）

| 版 | 最新核对 | 工号 | 结论 | 记录时间 |
|---|---|---|---|---|
| en-zh-cn（core-en） | 二轮全量重校 PROOF-NOTE-2 | 2f96abe3 | (a) CLEAN | 2026-11-12 ~18:30 UTC |
| en-de | 二轮全量重校 PROOF-NOTE-2 | 2f96abe3 | (a) CLEAN | 2026-11-12 ~18:30 UTC |
| en-es | 二轮全量重校 PROOF-NOTE-2 | 2f96abe3 | (a) CLEAN | 2026-11-12 ~18:30 UTC |
| en-fr | 二轮全量重校 PROOF-NOTE-2 | 2f96abe3 | (a) CLEAN | 2026-11-12 ~18:30 UTC |
| en-it | 二轮全量重校 PROOF-NOTE-2 | 2f96abe3 | (a) CLEAN | 2026-11-12 ~18:30 UTC |
| en-ja | 二轮全量重校 PROOF-NOTE-2 | 2f96abe3 | (a) CLEAN | 2026-11-12 ~18:30 UTC |
| en-ko | 二轮全量重校 PROOF-NOTE-2 | 2f96abe3 | (a) CLEAN | 2026-11-12 ~18:30 UTC |
| en-nl | 二轮全量重校 PROOF-NOTE-2 | 2f96abe3 | (a) CLEAN | 2026-11-12 ~18:30 UTC |
| en-pt | 二轮全量重校 PROOF-NOTE-2 | 2f96abe3 | (a) CLEAN | 2026-11-12 ~18:30 UTC |
| en-ru | #4 全新全量重校（scratch-verify-en/VERIFY-REPORT.md §en-ru） | 30e69a22 | (a) CLEAN | 2026-11-13 04:56–05:10 UTC |
| en-zh-tw | 二轮全量重校 PROOF-NOTE-2 | 2f96abe3 | (a) CLEAN | 2026-11-12 ~18:30 UTC |

注：PROOF-NOTE-2 §1 所记 en-ru 印/网 SHA（印 `9e503c053878`/29,097,780 B、网 `8875c5599472`/2,573,323 B）是 fix2 重建前的值，已被 #4 重校的新值取代；其 text.md SHA（`13e0e75ce382`）未变，与磁盘一致。

### SHA-12 对照表（核对记录值 vs 本次磁盘实测，2026-11-13 07:13 UTC）

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） | 对照 |
|---|---|---|---|---|
| en-zh-cn（core-en） | 30,110,585 / `5e9789d5f873` | 2,605,509 / `9283d6e6baab` | 51,573 / `e271f6cbfc44` | 一致 |
| en-de | 28,845,594 / `80e0746afc89` | 2,334,821 / `86438c44ceb8` | 52,736 / `2b2af27cc59b` | 一致 |
| en-es | 28,847,830 / `81e1cfb9f3b0` | 2,337,042 / `452a9d0f891a` | 54,556 / `cb334ba784ac` | 一致 |
| en-fr | 28,847,125 / `f18c64ee8913` | 2,336,319 / `18523f7b6177` | 53,974 / `cbe3b588d970` | 一致 |
| en-it | 28,841,732 / `0062f3d9b875` | 2,330,932 / `24ad7443e932` | 54,115 / `3d6c872ff631` | 一致 |
| en-ja | 35,187,926 / `068e2d9da3e5` | 2,713,215 / `e0ead68adf7a` | 53,756 / `2ccd31bee63d` | 一致 |
| en-ko | 30,159,302 / `dacad9cca89b` | 2,535,257 / `7c486f7d60aa` | 53,758 / `b5592fecb7af` | 一致 |
| en-nl | 28,842,162 / `eb6be63a6686` | 2,331,372 / `32e8baa51bf9` | 53,736 / `cbd9a008c530` | 一致 |
| en-pt | 28,850,391 / `eb347a545c8e` | 2,339,582 / `adc0a7e864db` | 54,291 / `1b3ee4558a75` | 一致 |
| en-ru | 28,991,765 / `7336fdd65c17` | 2,468,694 / `8ded0e80780b` | 62,552 / `13e0e75ce382` | 一致 |
| en-zh-tw | 30,215,637 / `58112dca9caf` | 2,701,637 / `cd585a52bc57` | 51,321 / `63c7651e06e9` | 一致 |

（磁盘值由本次实测 `sha256sum` + `stat` 得出，完整 64 位 SHA 见下节 KIT 核对程序输出。33/33 一致，字节数 33/33 一致。）

### 生产 mtime（证明核对后无改动）

- 10 版印/网/text.md 全部建于 2026-11-12 12:51–15:05 UTC，KIT 建于 2026-11-12 15:23–15:28 UTC——均在二轮重校（18:30 UTC）之前、#4 核对（11-13 04:56 UTC）之前。
- en-ru 印/网建于 2026-11-13 01:22 UTC（boxtitle fix2 重建），text.md 建于 01:22 UTC——均在 #4 重校之前。
- `find core-en 2026-w47-en-* -newermt '2026-11-13 05:10:00 UTC'`：**0 个文件**。#4 核对结束后 en 家生产目录零改动。
- run-log.md：05:11 UTC “en 家 §8.4 核对完成”条目之后（至 07:00 UTC）无任何 en 相关条目；其后条目只涉 es-ru F1、de round-3/4、封面。
- 无更新的 en 家 PROOF-NOTE：`scratch-reproof2-w47-en/`（2026-11-12 18:05）为最新 en 重校目录；`scratch-verify-en/`（2026-11-13 05:10）为最新 en 核对目录；其后无新建的 en 家 reproof/verify/fix scratch。

### KIT §7/§2 SHA 核对（完整 64 位）

逐版以程序提取 KIT 内全部 64 位 SHA-256，与磁盘实测全值比对：

| 版 | KIT 印 SHA | KIT 网 SHA | KIT 文 SHA |
|---|---|---|---|
| en-zh-cn | OK | OK | OK |
| en-de | OK | OK | OK |
| en-es | OK | OK | OK |
| en-fr | OK | OK | OK |
| en-it | OK | OK | OK |
| en-ja | OK | OK | OK |
| en-ko | OK | OK | OK |
| en-nl | OK | OK | OK |
| en-pt | OK | OK | OK |
| en-ru | OK | OK | OK |
| en-zh-tw | OK | OK | OK |

**33/33 一致。**（各版 KIT 章节编号不统一：core-en/de/es/fr 的 SHA 表在 §7，余版在 §2；均已逐版定位核对——与 #4 报告的章节分布一致。）

磁盘完整 SHA（本次实测，供复核）：

| 版 | 印 PDF SHA-256 | 网 PDF SHA-256 | text.md SHA-256 |
|---|---|---|---|
| en-zh-cn | `5e9789d5f873559c29ecc53fcf41b7ede5ad53ed38cba856f9612051ad44d356` | `9283d6e6baab5d276710362e88d4875228cfa1b47ae30e020ce6942dd11491c6` | `e271f6cbfc446ab4dd5580ea1f1222c34beac27a8eba95ee40ac9eca97fce24e` |
| en-de | `80e0746afc89949c16250144b2a0108568b6ab6be070960c4da9ed1045b87992` | `86438c44ceb8c499de88e64d0d0f70c6435134a55d85433dcb30b24d332f0ff4` | `2b2af27cc59ba25382bfacf11398fce8a330c2235c6097c22fe0cc624cd7c0ee` |
| en-es | `81e1cfb9f3b073362a61dec36c15bafbbf995c8f4d1a5b1dd547fce4ca233a57` | `452a9d0f891ac24a6a06a127b04414bbe5fec94eb08ffbf50cad911b93f3c829` | `cb334ba784acf059ea86dfa143f960f728870a8a321eb81645f7108005376d0a` |
| en-fr | `f18c64ee89131942807a864d331f12eafbf674905e16b1b6047d7c572b6135c3` | `18523f7b61779902091cb6d494b2118134fa68598b4f03e7603f88e3c682f362` | `cbe3b588d970f172b131ee5642f44ca16822b299be2de68fc64de539d22bf227` |
| en-it | `0062f3d9b875c63abc96e0211f980bb2d2162b7a49f5a26db156a15f4bd680f7` | `24ad7443e932c63624c050d9c9c6e3e79c4947180993449833e32d441fd2896e` | `3d6c872ff631d267f202e0b9ecc56ded477a63068c4e492f8747099e5c3790a0` |
| en-ja | `068e2d9da3e50d70dde8f3525faa73e4d703d29adcdad4d18c80cbfe13e698b1` | `e0ead68adf7a5be76c2b26c8fb6b2662732ac5b19b27f788c9f377795186b911` | `2ccd31bee63d5abc4b50f35a4a77923922bfd4bb63e0b2f168211f46f04c3f4e` |
| en-ko | `dacad9cca89b724500adf7c4eb1990ea3aadaf6f22bd65f4c315ea580e7233a0` | `7c486f7d60aac42e310f7d9ad7120e1a6385d65aaceca1757ce9b4151d462e4a` | `b5592fecb7afb30f1e22f865fe0a416dfd7dd9cc8b70319a7f6ad89cce6638bc` |
| en-nl | `eb6be63a66868ef1cbcfafe9a85b462ff58f8fc574b66be2267a77fd3b0e1db5` | `32e8baa51bf9260999812e6155113630717b2a4512430aef49d8465b758dc9c5` | `cbd9a008c530e127d6a446910443047e1df60092ed9e54ba0479b7a480696fe4` |
| en-pt | `eb347a545c8ec0239433ba3d7f7cf6d4c643f4aca05639f471fb2726bb6cba10` | `adc0a7e864dbd52c44273229b5cf804ac0e8282446b120a728aaeb01353bcdb6` | `1b3ee4558a758ae55e2faf84daee3ad9a12bd912ff0cce5dfcef5db2e6da05c0` |
| en-ru | `7336fdd65c17baa107ecb7ef3871c696499c52176d131573214c08ec7195bbc3` | `8ded0e80780b33981cb31bf438c9ceb1ac804cc226f6aa985ae94507dbcca0ad` | `13e0e75ce382f9ed9ae4d390f95026febd92ed08d1689347302c623fa34351f5` |
| en-zh-tw | `58112dca9cafc639314ebab97273aa5622bc323cc084bb88a11b1ab6aaa025b7` | `cd585a52bc5772230d975bd4a305119563e3f07ebc0ccd80404f73c027e242de` | `63c7651e06e925927a2bcc97939418209657855c0073b8e0aac445f2bede8009` |

## 第二阶段——全新完整重校

**无需执行。** 磁盘 SHA 与核对记录不符的版：0；核对缺失的版：0。11 版全部核对有效且为 (a)，无一版触发第二阶段条件，故未写新的 PROOF-NOTE，未渲染任何页面（磁盘亦余约 8G 至配额上限，无渲染消耗）。

## 逐版结论表

| 版名 | 最新核对 + 工号 | 核对 SHA | 磁盘 SHA | 一致？ | KIT §7 一致？ | 结论 |
|---|---|---|---|---|---|---|
| en-zh-cn（core-en） | 二轮 (a)，2f96abe3 | 印 `5e9789d5f873` / 网 `9283d6e6baab` / 文 `e271f6cbfc44` | 相同 | 是 | 是 | VERIFIED CLEAN |
| en-de | 二轮 (a)，2f96abe3 | 印 `80e0746afc89` / 网 `86438c44ceb8` / 文 `2b2af27cc59b` | 相同 | 是 | 是 | VERIFIED CLEAN |
| en-es | 二轮 (a)，2f96abe3 | 印 `81e1cfb9f3b0` / 网 `452a9d0f891a` / 文 `cb334ba784ac` | 相同 | 是 | 是 | VERIFIED CLEAN |
| en-fr | 二轮 (a)，2f96abe3 | 印 `f18c64ee8913` / 网 `18523f7b6177` / 文 `cbe3b588d970` | 相同 | 是 | 是 | VERIFIED CLEAN |
| en-it | 二轮 (a)，2f96abe3 | 印 `0062f3d9b875` / 网 `24ad7443e932` / 文 `3d6c872ff631` | 相同 | 是 | 是 | VERIFIED CLEAN |
| en-ja | 二轮 (a)，2f96abe3 | 印 `068e2d9da3e5` / 网 `e0ead68adf7a` / 文 `2ccd31bee63d` | 相同 | 是 | 是 | VERIFIED CLEAN |
| en-ko | 二轮 (a)，2f96abe3 | 印 `dacad9cca89b` / 网 `7c486f7d60aa` / 文 `b5592fecb7af` | 相同 | 是 | 是 | VERIFIED CLEAN |
| en-nl | 二轮 (a)，2f96abe3 | 印 `eb6be63a6686` / 网 `32e8baa51bf9` / 文 `cbd9a008c530` | 相同 | 是 | 是 | VERIFIED CLEAN |
| en-pt | 二轮 (a)，2f96abe3 | 印 `eb347a545c8e` / 网 `adc0a7e864db` / 文 `1b3ee4558a75` | 相同 | 是 | 是 | VERIFIED CLEAN |
| en-ru | #4 全新重校 (a)，30e69a22 | 印 `7336fdd65c17` / 网 `8ded0e80780b` / 文 `13e0e75ce382` | 相同 | 是 | 是 | VERIFIED CLEAN |
| en-zh-tw | 二轮 (a)，2f96abe3 | 印 `58112dca9caf` / 网 `cd585a52bc57` / 文 `63c7651e06e9` | 相同 | 是 | 是 | VERIFIED CLEAN |

## 全家结论

**CLEAN。** 11/11 版核对有效且为 (a)，磁盘 SHA、字节数、KIT SHA 全部一致，核对后零改动，无第二阶段重校需要。

## 待修清单

无。仅 1 项非缺陷观察（承接 #4 报告 O1）：en-ru Q109 答案键 `The count continued after the vote.` 语法成立，但按正文口径 `continues` 更自然；两轮前序重校均未列为问题，不修、不拦定稿，交协调员裁定是否记为 polish 项。

## 附：SOP §8 已读

已读 `~/workspace/weekly-git/SOP.md` §8 全文（§8.1–§8.6 + 附则一/二几何审计与工具化）及 `~/workspace/weekly-git/AGENTS.md`（只读核对合规：未写生产、未 commit/push、未跑 lint --write、未跑 insert.py）。
