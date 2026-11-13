# W47 ko 家 §8.4 终态核对报告（VERIFY-REPORT，最终轮）

- 核对员：本任务 subagent（与建造者、各轮校对员、修复工人均不同人；本次只做只读核对，未做第二阶段重校——无版需要）
- 核对时间：2026-11-13 ~02:12–02:20 UTC（Fri 2026-11-13）
- 范围：ko 家 11 版（core-ko = ko-zh-cn 版 + 2026-w47-ko-{de,en,es,fr,it,ja,nl,pt,ru,zh-tw}）
- 只读核对：未改任何生产文件，未 commit/push/add/reset/stash，未跑 lint --write，未跑 insert.py，未渲染（第一阶段纯只读，无需渲染）
- 磁盘：`df -h` 97G 已用 / 52G 可用（停手线为 df -h 100G，即 df -k ≥ 104,857,600 KB；当前 df -k 约 101,696,000 KB，未到线。配额上限约 105G df -h 口径，余约 8G）
- SOP：`~/workspace/weekly-git/SOP.md` §8 全文已读；`weekly-git/AGENTS.md` 已读
- 工具：`sha256sum` / `stat` / `find -newermt` / python3（只读比对）；未动用仓内构建工具（无需重建）

## 1. 枚举核对

盘上 `production/2026-w47/` 内 ko 家目录共 11 个，与任务清单一致，无多无少：

- `core-ko`（内含 `2026-w47-ko-zh-cn.text.md`，即 ko-zh-cn 版；无独立 `2026-w47-ko-zh-cn` 目录，与 #4 轮一致）
- `2026-w47-ko-de`、`2026-w47-ko-en`、`2026-w47-ko-es`、`2026-w47-ko-fr`、`2026-w47-ko-it`、`2026-w47-ko-ja`、`2026-w47-ko-nl`、`2026-w47-ko-pt`、`2026-w47-ko-ru`、`2026-w47-ko-zh-tw`

每版均含印 PDF、网 PDF、`.text.md` 三件（全量 sha256 实测见 §3）。`issues/2026-w47/` 本地尚不存在（W47 未开始插仓，与 run-log 一致；本次核对只涉生产侧）。

## 2. 最新核对记录（逐版）

ko 家最新全量重校为**第三轮独立重校**，工人 `2f24fef8`（工号见 run-log 与 #4 报告；PROOF-NOTE-3 正文未署工号），产出 `hidden_files/w47/scratch-reproof3-w47-ko/PROOF-NOTE-3.md`，run-log 记于 2026-11-12 ~20:15 UTC。结论 **(a) 干净，0 发现**（R2-1/R2-2/R2-3 与 F1–F5 全部核实通过，87 门机械门禁 RC=0，按页 inventory 11 版全部 150/150）。

其后唯一改动 ko 家生产文件的事件是跨家 `*-ru` 修复（fix-xru，2026-11-12 23:53 UTC，工人 fec69813）：仅 ko-ru 的印/网 PDF 重建（`svglib.py` 拉丁字体路由改道，text.md 未变）。ko-ru 的新 SHA 已由 **#4 轮核对员（工人 `08aafa41`，2026-11-13 ~05:00 UTC，`scratch-verify-ko/VERIFY-REPORT.md` §3.2）亲自全新全量重校**，结论 **(a) 干净，0 发现**（text.md 947 行通读、印/网文本层逐字节一致、p8 CLEAN、D5 census PASS、遮挡 0、8 页逐页目视）。

#4 轮之后的新记录排查：`find` 全 hidden_files/w47 下 mtime 晚于 2026-11-13 05:00 UTC 的 `PROOF-NOTE*.md`，仅命中 `scratch-reproof-de-round3/2026-w47-de-ko/PROOF-NOTE.md`——那是 **de 家** round-3 的 de-ko 版（德语目标 × 韩语读者），不属 ko 家，不影响 ko 家结论。ko 家无更新的重校记录。

run-log / ledger 在 #4 轮之后的 ko 相关条目：de 家 round-3（R3-F1/F2，只动 de 家 11 版，其中 de-ko 亦属 de 家）、ko 头条图与 ko-2 次图重制 + caption/alt 补丁（只动 `production/covers/2026-w47/`，不动生产版目录）。均经下节 mtime 审计证实未碰 ko 家生产文件。

## 3. SHA 对照表（核对记录 SHA vs 当前磁盘实测）

磁盘实测为本次 `sha256sum` 全值（下表列前 12 位 + 字节数；全值见 §6 附录）。

| 版 | 最新核对 + 工号 | 核对记录 SHA（印 / 网 / 文，SHA-12） | 磁盘 SHA（印 / 网 / 文，SHA-12） | 一致？ | KIT §7 一致？ | 结论 |
|---|---|---|---|---|---|---|
| ko-zh-cn（core-ko） | PROOF-NOTE-3，2f24fef8，(a) | 印 `7248314a5ae2` / 45,181,315；网 `ac97b284fe16` / 4,226,882；文 `044001ac2f14` / 35,456 | 印 `7248314a5ae2` / 45,181,315；网 `ac97b284fe16` / 4,226,882；文 `044001ac2f14` / 35,456 | 是 | 是（三 SHA 各出现 1 次） | VERIFIED CLEAN |
| ko-de | PROOF-NOTE-3，2f24fef8，(a) | 印 `8d217beb86ae` / 43,754,319；网 `4b1a54ce3040` / 3,956,937；文 `4f6945d36115` / 36,012 | 相同 | 是 | 是 | VERIFIED CLEAN |
| ko-en | PROOF-NOTE-3，2f24fef8，(a) | 印 `f10c5065bb5b` / 43,748,448；网 `59bb38b0bc77` / 3,951,102；文 `f5e5bb278704` / 35,781 | 相同 | 是 | 是 | VERIFIED CLEAN |
| ko-es | PROOF-NOTE-3，2f24fef8，(a) | 印 `637bcb1b1b22` / 43,752,821；网 `e1ae9fcc033b` / 3,955,583；文 `a24bd9ffaa09` / 36,065 | 相同 | 是 | 是 | VERIFIED CLEAN |
| ko-fr | PROOF-NOTE-3，2f24fef8，(a) | 印 `1f6add20c07d` / 43,751,522；网 `dc933cc18cfe` / 3,954,158；文 `661b391e24d3` / 36,131 | 相同 | 是 | 是 | VERIFIED CLEAN |
| ko-it | PROOF-NOTE-3，2f24fef8，(a) | 印 `edfda4420e46` / 43,746,645；网 `f0efba8a29ab` / 3,949,052；文 `4e7926e4ffa7` / 36,068 | 相同 | 是 | 是 | VERIFIED CLEAN |
| ko-ja | PROOF-NOTE-3，2f24fef8，(a) | 印 `f8c7508f9be8` / 50,279,548；网 `f9bb1d3a3929` / 4,373,107；文 `be048d7d4164` / 36,275 | 相同 | 是 | 是 | VERIFIED CLEAN |
| ko-nl | PROOF-NOTE-3，2f24fef8，(a) | 印 `662eb3e3e3f2` / 43,748,187；网 `5f84566e41de` / 3,950,671；文 `55abafb3fee8` / 35,904 | 相同 | 是 | 是 | VERIFIED CLEAN |
| ko-pt | PROOF-NOTE-3，2f24fef8，(a) | 印 `70047cd27b8d` / 43,753,908；网 `e4028beb886a` / 3,956,638；文 `059743986a52` / 35,935 | 相同 | 是 | 是 | VERIFIED CLEAN |
| ko-ru | #4 全新重校，08aafa41，(a) | 印 `9bf5c43082b6` / 43,846,114；网 `5fc509995df1` / 4,047,903；文 `e439f6a60a13` / 38,039 | 相同 | 是 | 否——见 §4（已知 wave-2 KIT 文字项） | VERIFIED CLEAN |
| ko-zh-tw | PROOF-NOTE-3，2f24fef8，(a) | 印 `65118aabee9f` / 45,219,886；网 `189fde45fc9e` / 4,323,857；文 `841a26658cb7` / 35,487 | 相同 | 是 | 是 | VERIFIED CLEAN |

比对方式：除逐项目视比对外，另以脚本程序化解析 PROOF-NOTE-3 指纹表 11 行并与磁盘重算逐版比对——10 版 MATCH；ko-ru 仅印/网与第三轮不符（fix-xru 重建所致，text.md MATCH），而其印/网新值与 #4 全新重校记录逐位一致。另与 #4 VERIFY-REPORT §2 所载 33 项磁盘实测逐项一致（SHA-12 + 字节数全等）。

## 4. mtime 审计（证明后无改动）

`find` 11 个版目录全部文件，mtime 晚于 2026-11-13 05:00 UTC（#4 核对时间）者：**0 个**。各目录最新 mtime：

- core-ko / ko-de / ko-en：KIT 2026-11-12 18:45 UTC；其余 7 版 KIT 2026-11-12 18:46 UTC
- ko-ru：KIT 2026-11-12 23:54 UTC（fix-xru 后）；印 PDF 23:53:27、网 PDF 23:53:48
- 全部印/网 PDF 与 text.md 的 mtime 均在 2026-11-12 13:55–23:53 UTC 之间，早于 #4 核对

即：自 #4 轮核对以来，ko 家生产目录**零文件**被改动。

## 5. KIT §7（Output files + sizes 节）核对

以脚本逐版统计磁盘实测三组完整 SHA-256 在各版 `WEEKLY-KIT.md` 中的出现次数：

| 版 | 印 SHA 在 KIT 中次数 | 网 SHA 在 KIT 中次数 | 文 SHA 在 KIT 中次数 | 结论 |
|---|---|---|---|---|
| core-ko、ko-de、ko-en、ko-es、ko-fr、ko-it、ko-ja、ko-nl、ko-pt、ko-zh-tw | 1 | 1 | 1 | 一致 |
| ko-ru | 1（fix-xru 节 L142） | 1（fix-xru 节 L143） | 2（§7 L117 + fix-xru 节） | §7 节本身仍载重建前值——已知 wave-2 项，见下 |

ko-ru KIT 的 “Output files + sizes” 节（L115–116）仍载重建前 SHA（印 `4c0c80b6b6bf…` / 43,926,367 B；网 `ee36501822d1…` / 4,126,934 B）；新 SHA 只在 fix-xru 节（L141–144）出现，该节并注明 “this build supersedes the ‘Output files + sizes’ deliverables”。与 #4 轮结论完全相同，**自 #4 以来无变化**。此为 KIT 文字待 wave-2 更新项，不是核对缺口，不动成品，不阻塞内容定稿。

## 6. 第二阶段——无需重校

磁盘 SHA 与核对记录逐版一致、核对无缺失：11 版中 0 版触发第二阶段条件，故本次**未做**全新全量重校，无新 PROOF-NOTE 产出。#4 轮的结论（10 版直接 VERIFIED CLEAN + ko-ru 全新重校 (a)）在当前磁盘上仍然成立。

## 7. 待办清单（只记录，不修复）

**内容待修：无。** 11 版全部 CLEAN，0 条新发现。

**wave-2 清单（KIT 文字，不动成品，与 #4 轮第 5 节第 1 项相同，未变）：**

1. **ko-ru KIT “Output files + sizes” 节 SHA 已过期**（KIT-only 修正，不重建、不重校）：印 PDF 改为 `9bf5c43082b6d4e36c8cc7c62a9507fc3ff588616f4fe3e048ae2ce5019d1c48` / 43,846,114 B；网 PDF 改为 `5fc509995df17bee4d98e9483a1861157efebece886c535f3a031b9131cbd2fa` / 4,047,903 B；text.md 不变 `e439f6a60a13d26bfdc3ac17d502cef1592063e6fe8fecf1e15c8f52109e6841` / 38,039 B。旧值保留备查（fix-xru 节已有新旧对照）。

## 8. 全家结论

**CLEAN** —— 11/11 版核对有效且为 (a)：10 版 SHA 与第三轮 CLEAN 重校（工人 2f24fef8，(a)）逐项一致；ko-ru 新 SHA 与 #4 全新全量重校（工人 08aafa41，(a)）逐项一致；mtime 审计证实 #4 轮后零改动；KIT §7 除 ko-ru 一处已知 wave-2 文字项外全部一致。ko 家 proofread-until-zero 成立，内容定稿态未被其后任何工作破坏。

## 附录：磁盘实测完整 SHA-256（本次 `sha256sum`）

| 版 | 文件 | 字节 | SHA-256 |
|---|---|---|---|
| ko-zh-cn（core-ko） | `2026-w47-ko-zh-cn.text.md` | 35,456 | `044001ac2f14e76620a3c5109ecd85a29d6875d05401fd11f071070e91c5d3f3` |
| ko-zh-cn（core-ko） | `Lucerna-VOL4-web.pdf` | 4,226,882 | `ac97b284fe160de403d637b5e5a6d05f3aa6a3574cae5d28022feadfab6a8373` |
| ko-zh-cn（core-ko） | `Lucerna-VOL4.pdf` | 45,181,315 | `7248314a5ae2d3b053d6a818af2dcbd9c62c109c3ee732b5020a97abed95f256` |
| ko-de | `2026-w47-ko-de.text.md` | 36,012 | `4f6945d3611552aa90fc1fea66d4270f63ae939fb3196f616cee86215f68c16a` |
| ko-de | `Lucerna-VOL4-KO-DE-web.pdf` | 3,956,937 | `4b1a54ce3040982076796965e45135e00ac057848315e6d3374235b6ec9212e4` |
| ko-de | `Lucerna-VOL4-KO-DE.pdf` | 43,754,319 | `8d217beb86ae25f72ddd5413bd59011fe7051adc30965e0bb09cf2298e47c3d2` |
| ko-en | `2026-w47-ko-en.text.md` | 35,781 | `f5e5bb278704c676b8904b23b47a46b7444fc1529c5c43ff6e10760da54fa7e5` |
| ko-en | `Lucerna-VOL4-KO-EN-web.pdf` | 3,951,102 | `59bb38b0bc771cb8eb1c89b65c828e419780317db80573369bbfacddc189b3c7` |
| ko-en | `Lucerna-VOL4-KO-EN.pdf` | 43,748,448 | `f10c5065bb5b90f753b2452055c2276a47861cd5eab88c6e4ebd941629884ee1` |
| ko-es | `2026-w47-ko-es.text.md` | 36,065 | `a24bd9ffaa097d529f6fc81b98748126ad1a471d44b9323ba3de15c8313f2b06` |
| ko-es | `Lucerna-VOL4-KO-ES-web.pdf` | 3,955,583 | `e1ae9fcc033b58266bc9652b653ae27cbb56f396c477186a18d594c1cf9e09c9` |
| ko-es | `Lucerna-VOL4-KO-ES.pdf` | 43,752,821 | `637bcb1b1b22a57f7167bdd9516c86dab89440a356f2187faf0e4ca5bbacd5d3` |
| ko-fr | `2026-w47-ko-fr.text.md` | 36,131 | `661b391e24d370bc54b2c9dd615f3e0c661a99dfc2b4539db05c615f871570de` |
| ko-fr | `Lucerna-VOL4-KO-FR-web.pdf` | 3,954,158 | `dc933cc18cfee50111b035d95c9ffecc3547b9a1b85f1b56b01853ad5179bbe1` |
| ko-fr | `Lucerna-VOL4-KO-FR.pdf` | 43,751,522 | `1f6add20c07db17f556b1c2d3303d5e2f99a03de7be1604e2250219ae3480da1` |
| ko-it | `2026-w47-ko-it.text.md` | 36,068 | `4e7926e4ffa795fd12055bdf4f959711b4f78037fc6c5a05dc9f890b52155ecc` |
| ko-it | `Lucerna-VOL4-KO-IT-web.pdf` | 3,949,052 | `f0efba8a29ab51061e10c2d5fe854f47aad29bb9cf381043243b51a16ad11aeb` |
| ko-it | `Lucerna-VOL4-KO-IT.pdf` | 43,746,645 | `edfda4420e4699d9b8a344a82a10b396c43eb409a5017d9bd90da024d9766f0f` |
| ko-ja | `2026-w47-ko-ja.text.md` | 36,275 | `be048d7d4164ed8466642665f18bdf765174ccfff62342642a489327f6d71a9e` |
| ko-ja | `Lucerna-VOL4-KO-JA-web.pdf` | 4,373,107 | `f9bb1d3a392996ba8344083be0aac90ed30873ddb2ab8f296516de656c65b7f8` |
| ko-ja | `Lucerna-VOL4-KO-JA.pdf` | 50,279,548 | `f8c7508f9be83c8fd83ffca7041864df83609ea394972132c93f5e79e64c8a6d` |
| ko-nl | `2026-w47-ko-nl.text.md` | 35,904 | `55abafb3fee843b26e69f67b61bb30973a61b3fc9c128e7951a2d9d2b53ccc4d` |
| ko-nl | `Lucerna-VOL4-KO-NL-web.pdf` | 3,950,671 | `5f84566e41ded4b03c2b40ff7c6596c1251db61b82f6c82586e191580b6e279b` |
| ko-nl | `Lucerna-VOL4-KO-NL.pdf` | 43,748,187 | `662eb3e3e3f20b337d9b0dc7397e5f72dadf5f6c533a16d5ed0f6436d7c25f8c` |
| ko-pt | `2026-w47-ko-pt.text.md` | 35,935 | `059743986a5214459fdd66f777cc64991bedb20da7273b8cda457c47a11dc388` |
| ko-pt | `Lucerna-VOL4-KO-PT-web.pdf` | 3,956,638 | `e4028beb886a1ff0be9cf753983d11e30d8c751132df27c0cfd5395ea018a418` |
| ko-pt | `Lucerna-VOL4-KO-PT.pdf` | 43,753,908 | `70047cd27b8de7d867f9af3cea8d25fe09e3ace678b43948c9564e8632140f92` |
| ko-ru | `2026-w47-ko-ru.text.md` | 38,039 | `e439f6a60a13d26bfdc3ac17d502cef1592063e6fe8fecf1e15c8f52109e6841` |
| ko-ru | `Lucerna-VOL4-KO-RU-web.pdf` | 4,047,903 | `5fc509995df17bee4d98e9483a1861157efebece886c535f3a031b9131cbd2fa` |
| ko-ru | `Lucerna-VOL4-KO-RU.pdf` | 43,846,114 | `9bf5c43082b6d4e36c8cc7c62a9507fc3ff588616f4fe3e048ae2ce5019d1c48` |
| ko-zh-tw | `2026-w47-ko-zh-tw.text.md` | 35,487 | `841a26658cb7dcff9d3489e95caedd5558165a73efc9e37bbb262c75693b0203` |
| ko-zh-tw | `Lucerna-VOL4-KO-ZH-TW-web.pdf` | 4,323,857 | `189fde45fc9e7b747611f4beb0285db17ce34f77aefff372bf16e868b82110f1` |
| ko-zh-tw | `Lucerna-VOL4-KO-ZH-TW.pdf` | 45,219,886 | `65118aabee9f7494c50071139ea74dbff6e16f00c2c0f357902564ac06402936` |
