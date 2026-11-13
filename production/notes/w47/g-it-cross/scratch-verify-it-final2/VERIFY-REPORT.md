# VERIFY-REPORT — W47 it 家 §8.4 终态核对（重派，第二名核对员）

- **核对员**：本轮独立核对员（与建造者、第 1/2/3 轮校对员、修复者、上一名 §8.4 核对员 089e5763 均不同；只核对、不修复、不改生产文件）
- **日期**：2026-11-13 ~07:25 UTC（Fri 2026-11-13 02:25 EST）
- **范围**：it 家 11 版 — `core-it`（= it-zh-cn）+ `2026-w47-it-{de,en,es,fr,ja,ko,nl,pt,ru,zh-tw}`
- **磁盘**：开工 `df -h` 98G 已用 / 150G（`df -k` 101,741,092 KB，< 停手线 104,857,600 KB）；第一阶段纯只读，未渲染
- **工作目录**：`hidden_files/w47/scratch-verify-it-final2/`（本报告；上一名工人的 `scratch-verify-it-final/` 未动，内只有 GATE-STOP.md）
- **方法**：只读核对生产文件；全部 33 个 SHA-256 + 字节数实测；KIT §7 逐版 grep；生产 mtime 全扫；PROOF-NOTE 逐份读原文；未跑 run.py/render.py，未渲染（第一阶段无不符版，不需要第二阶段）
- **注**：SOP 正文 §8 无编号子节 §8.4；此处“§8.4”按 run-log/ledger 通用口径指 §8 第 4 条循环规则——修后须从头全量重校、直至一整轮零问题才算定稿。

## 全家结论：CLEAN

**11/11 CLEAN，零待修项，无需第二阶段重校。**

- 10 版：最新重校为第三轮（PROOF-NOTE-3，工人 08324ae9，2026-11-12 ~20:00 UTC，结论 (a) CLEAN 零问题），其后生产零改动；本人实测 30 个 SHA + 字节数与三轮指纹逐项一致 → **VERIFIED CLEAN**。
- 1 版（it-ru）：三轮后 SHA 变过（fix-xru 重建 → P2 boxtitle 修复 → fix-it-ru2，末次 2026-11-13 01:41–01:43 UTC），由上一名核对员 089e5763 作为不同校对员做了全新全量重校（scratch-verify-it/VERIFY-REPORT.md §3：text.md 1317 行通读、150 题逐题复核、8 页目视、共享工具全部门禁），结论 CLEAN 零发现；本人实测其 3 个 SHA + 字节数与该重校记录逐项一致，且其后生产零改动 → **VERIFIED CLEAN**。
- KIT §7 SHA：11 版全部与磁盘一致（每版印/网/文 SHA-12 在 KIT 内各恰 1 次）→ **wave-2 KIT SHA 清单为空**。
- D5 census（重建后）：三轮 §4 全部 11 版 latin 0 / cyr 0，弯引号全部走 Newsreader；it-ru `noto_sans_elements=777` 为已知跨家系统项（俄语读者正文合法用 Noto Sans，089e5763 复测 713，同类），非缺陷。

## 1. 逐版表

SHA 均为前 12 位；字节数为实测值。核对 SHA = 最新有效重校记录所载；磁盘 SHA = 本人本次实测。

| 版 | 最新核对 + 工号 | 核对 SHA（印 / 网 / 文） | 磁盘 SHA（印 / 网 / 文） | 一致？ | KIT §7 一致？ | 结论 |
|---|---|---|---|---|---|---|
| core-it | 三轮 (a)，08324ae9，2026-11-12 ~20:00 UTC | 7b3034a08180 / 393e65473a1c / 24b37ae72af3（14,839,776 / 1,546,116 / 52,677） | 7b3034a08180 / 393e65473a1c / 24b37ae72af3（14,839,776 / 1,546,116 / 52,677） | 是 | 是 | VERIFIED CLEAN |
| it-de | 三轮 (a)，08324ae9 | 8cf7241a5d60 / 13414d0fbe1b / 27f58fca0f39（13,499,265 / 1,218,051 / 56,634） | 8cf7241a5d60 / 13414d0fbe1b / 27f58fca0f39（13,499,265 / 1,218,051 / 56,634） | 是 | 是 | VERIFIED CLEAN |
| it-en | 三轮 (a)，08324ae9 | aeae0796361c / e071a54f8f30 / a4d863d96180（13,496,925 / 1,215,698 / 55,126） | aeae0796361c / e071a54f8f30 / a4d863d96180（13,496,925 / 1,215,698 / 55,126） | 是 | 是 | VERIFIED CLEAN |
| it-es | 三轮 (a)，08324ae9 | 4393ba30bd49 / c40c7a0067bd / e19cf39d5ef6（13,497,563 / 1,216,301 / 56,214） | 4393ba30bd49 / c40c7a0067bd / e19cf39d5ef6（13,497,563 / 1,216,301 / 56,214） | 是 | 是 | VERIFIED CLEAN |
| it-fr | 三轮 (a)，08324ae9 | ffb20e7b9620 / d08db2eb54b2 / b4d1ec47ff3a（13,497,005 / 1,215,747 / 56,524） | ffb20e7b9620 / d08db2eb54b2 / b4d1ec47ff3a（13,497,005 / 1,215,747 / 56,524） | 是 | 是 | VERIFIED CLEAN |
| it-ja | 三轮 (a)，08324ae9 | 38a236a3d0ca / e035db45098e / 3dafa38c8b40（21,050,187 / 1,697,338 / 58,209） | 38a236a3d0ca / e035db45098e / 3dafa38c8b40（21,050,187 / 1,697,338 / 58,209） | 是 | 是 | VERIFIED CLEAN |
| it-ko | 三轮 (a)，08324ae9 | 66dffb4ebd5c / 7419a5a624e5 / c37668224de7（15,803,899 / 1,484,256 / 57,349） | 66dffb4ebd5c / 7419a5a624e5 / c37668224de7（15,803,899 / 1,484,256 / 57,349） | 是 | 是 | VERIFIED CLEAN |
| it-nl | 三轮 (a)，08324ae9 | b5a24a8f4234 / 8fc2d76c044a / 92ddd5838d6f（13,495,268 / 1,213,994 / 55,535） | b5a24a8f4234 / 8fc2d76c044a / 92ddd5838d6f（13,495,268 / 1,213,994 / 55,535） | 是 | 是 | VERIFIED CLEAN |
| it-pt | 三轮 (a)，08324ae9 | c4d4fe0f005e / a6e7e8365466 / 03cc7389d3ed（13,500,238 / 1,218,997 / 55,736） | c4d4fe0f005e / a6e7e8365466 / 03cc7389d3ed（13,500,238 / 1,218,997 / 55,736） | 是 | 是 | VERIFIED CLEAN |
| it-ru | 全新全量重校 CLEAN，089e5763，2026-11-13 ~04:55–05:30 UTC（§3） | bca811b03470 / ce75a0349c3e / 28e906435b1f（13,644,359 / 1,361,661 / 67,662） | bca811b03470 / ce75a0349c3e / 28e906435b1f（13,644,359 / 1,361,661 / 67,662） | 是 | 是 | VERIFIED CLEAN |
| it-zh-tw | 三轮 (a)，08324ae9 | 3cf43a808c2a / 133b04d123f1 / 1ae5edf7b167（14,907,346 / 1,640,999 / 52,588） | 3cf43a808c2a / 133b04d123f1 / 1ae5edf7b167（14,907,346 / 1,640,999 / 52,588） | 是 | 是 | VERIFIED CLEAN |

## 2. it2 PROOF-NOTE（10 份）——全部过期，已逐一确认，不作定稿依据

10 份均在 `scratch-reproof-it2-<lang>/PROOF-NOTE.md`，mtime 2026-11-11 22:04–22:14 UTC，结论均为 (a)，均早于 D5 重建（it 家生产 PDF 重建于 2026-11-12 15:02–18:35 UTC）。工号（run-log 3331/3399/3407 行 + ledger 1330/1394/1395 行核实）：de **68c75099**（完成 22:12:59 UTC）、ko **3e392347**（完成 22:14:18 UTC）、en 6598fb0f、es d213fda6、fr dc13d9c2、ja 3f0c4d1d、nl f1177bb5、pt 03707ec5、ru 8a8ca74d、zh-tw f0cabc33。

- **未读到旧版**：盘上 it2-de 记录印 `7952f4ff…`/14,037,210、网 `65e26290…`/1,297,238、文 `de0aa214…`/56,662，与 run-log 3399 行协调员盘验值逐字一致；it2-ko 记录印 `3125d4f3…`/19,296,892、网 `67bda0ac…`/1,607,467、文 `d4d0c6c1…`/57,326，与 run-log 3407 行一致。盘上文件即最终版本。
- **过期证据（SHA 已变）**：it2-de 旧印 `7952f4ff…` vs 现盘 `8cf7241a…`；it2-ko 旧印 `3125d4f3…` vs 现盘 `66dffb4e…`；it2-ru 旧印 `966a9d10…`/14,180,915、旧网 `db22fa31…`/1,441,240、旧文 `47c04715…`/67,731 vs 现盘 `bca811b0…`/13,644,359、`ce75a034…`/1,361,661、`28e90643…`/67,662。
- **关于“PROOF-NOTE-it2-ru”**：磁盘上不存在此文件名的文件。it2-ru 的记录是 `scratch-reproof-it2-ru/PROOF-NOTE.md`（2026-11-11 22:04 UTC，工人 8a8ca74d，(a)，已过期，见上）。it-ru 在 D5 重建后的有效全新全量重校记录是上一名核对员 089e5763 的 `scratch-verify-it/VERIFY-REPORT.md` §3（2026-11-13 ~04:55–05:30 UTC，CLEAN，0 发现；含 text.md 1317 行通读、150 题逐题复核、8 页目视、全部门禁表），其 SHA 与现盘逐项一致（见逐版表）。不同人要求满足：089e5763 与三轮校对员 08324ae9、fix-it-ru2 修复者均不同。

## 3. 三轮重校（PROOF-NOTE-3）核实

- 文件：`scratch-reproof3-w47-it/PROOF-NOTE-3.md`，工人 **08324ae9**（run-log 4699 行），日期 2026-11-12，结论 **(a) CLEAN**，MAJOR 0 / MEDIUM 0 / low 0，零问题轮次。
- 内容：it-en text.md 1317 行全文通读 + 其余 10 版逐行 diff；R2-1/R2-2 均核实在版；外部事实（BookCity/Torrone/Eurochocolate/TFF）与 2026-11-12 live 来源一致；机械门 11/11 ALL-GREEN（run.py TOTAL 150、occlusion 0、p8 150/150 CLEAN keydiff [137,138,139]、D5 census latin 0/cyr 0、boxtitle 0 DEFECT、spill 0、edge 0、印/网文字层 nonws diff 0；已知裁定项：it-ja P8-keys 2561 流光标假象、it-ko 印/网 1 空白字符差、it-ru noto_sans 777）。
- 其指纹表 33 项与本人磁盘实测逐项一致（10 版；it-ru 一项除外，见 §4）。

## 4. it-ru：三轮后 SHA 变化链已闭合

- 三轮记录 it-ru：印 `af296c0525ea`/13,752,697、网 `597e400ffcec`/1,465,756、文 `298c2cd79bb8`/67,681。
- 三轮后变化（run-log + 089e5763 报告 §1 核实）：fix-xru 重建（印 `97095d30…`）→ P2 boxtitle 修复（印 `5281accd…`）→ fix-it-ru2（印 `bca811b0…`，2026-11-13 ~01:46 UTC）。
- 现盘：印 `bca811b03470`/13,644,359、网 `ce75a0349c3e`/1,361,661、文 `28e906435b1f`/67,662，与 089e5763 全新全量重校记录逐项一致；其唯一 HEAD TOO WIDE（P6 `LE PAROLE DELLA MANOVRA`）为已接受项 A3，089e5763 独立复核确认墨迹伸入空白边距、无碰撞，不构成新发现。
- 生产 mtime：it-ru 三件 mtime 均为 2026-11-13 01:41 UTC，KIT 01:43 UTC，均在 089e5763 重校之前；重校后无改动（见 §5）。

## 5. 生产 mtime：核对后零改动

- `find` 全扫 11 个版目录：**2026-11-13 05:27 UTC（089e5763 核对完成）之后 0 个文件改动**。
- 各版最新 mtime：10 版为 2026-11-12 18:34–18:42 UTC（svg 页文件；交付三件为 15:02–18:25 UTC，均在三轮 ~20:00 UTC 之前）；it-ru 为 2026-11-13 01:43 UTC（KIT）。
- run-log 05:27 UTC 之后条目（协调员 #6 接手、磁盘单位纠错、de round-4、caption 补丁）无 it 家生产改动。

## 6. KIT §7 SHA 核对（wave-2 清单）

11 版 WEEKLY-KIT.md 逐版 grep 当前 SHA-12：印/网/文各恰 1 次，全部一致。**wave-2 KIT SHA 清单：空。**（it-ru KIT §19 含 fix-it-ru2 记录，新 SHA 为当前值、旧值保留为历史，正确。）

## 7. D5 census 说明

- 重建后普查（三轮 §4，2026-11-12）：11 版全部 latin 0 / cyr 0，弯引号全部走 Newsreader，CENSUS PASS。
- `scratch-d5-census/D5-CENSUS-130.md` 是**重建前诊断普查**（2026-11-12 01:16–02:10 EST），非重建后验证，不作定稿依据；其记的 it-ko P1 2 个弯引号在 Noto Sans CJK KR 元素内一项为重建前状态，三轮重校后 it-ko curly 4/4 走 Newsreader，已清零。

## 8. 第二阶段

**未启动。** 全部 11 版磁盘 SHA 与最新有效核对记录一致、无缺失、无过期，逐版表无 GAPS，故无版需要全新完整重校。未写任何 PROOF-NOTE，未渲染，未动生产。

## 9. 工作产物与合规

- 本报告：`scratch-verify-it-final2/VERIFY-REPORT.md`（唯一写出文件）。
- 未写 `~/workspace/weekly-git/production/2026-w47/` 或 `issues/` 的任何文件；无 commit/push/add/reset/stash；无 `node lint.mjs --write`；无 insert.py；未派 subagent。
- 上一名工人的 `scratch-verify-it-final/GATE-STOP.md` 未动。
