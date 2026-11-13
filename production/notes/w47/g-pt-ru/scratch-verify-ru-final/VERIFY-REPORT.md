# W47 ru 家 §8.4 终态核对报告（终态核对员，接替上一名核对员）

- 核对员：ru 家 §8.4 终态核对员（恢复协调员 #6 派单；与 round-5 校对员 03a5768c、fix4 工人 bd49579f、上一名核对员 5b48f532 均不同人；只读核对，未改任何生产文件）
- 时间：2026-11-13 ~07:15 UTC（2026-11-13 02:15 EST）
- 范围：ru 家 11 版：core-ru（= ru-zh-cn）+ `2026-w47-ru-{de,en,es,fr,it,ja,ko,nl,pt,zh-tw}`
- 依据：SOP §8 全文（已读 `~/workspace/weekly-git/SOP.md` §8）；`scratch-reproof5-w47-ru/PROOF-NOTE-5.md` + `fingerprint.json`；run-log.md；ledger.md；R1 重建 `scratch-ru-rerun-R1/REBUILD-LOG.md`；D5 `scratch-d5-census/D5-CENSUS-130.md` + `scratch-d5-rebuild-ru/scratch-fanout-ru/D5-REPORT-ru-*.md`
- 磁盘：`df -h` 98G 已用 / 52G 可用（`df -k` 101,750,644 KB），未触 100G 停手线（104,857,600 KB）；距停手线约 3G。开工时 97G，核对期间涨至 98G（并行工人在写，本人未渲染、未写生产）

## 全家结论：CLEAN

11 版全部核对有效且为 (a)：最新核对 round-5（校对员 03a5768c）结论 (a) CLEAN、0 findings；
本次实测 11 版印/网/text.md 共 33 个 SHA-256 前 12 位 + 字节数与 PROOF-NOTE-5 指纹逐项一致
（core-ru 两份 text.md 均测，SHA 相同）；
round-5 之后 ru 家 11 个生产目录内 0 个文件改动（`find -newermt "2026-11-12 23:05 UTC"` 0 命中，
放宽到 21:41 UTC 亦 0 命中）。KIT §7 当前值 11/11 与磁盘一致，无 wave-2 SHA 待补项。
第二阶段未触发，无需全新重校。

## 关键时间线（实测）

- ru 家最后一次生产写入：2026-11-12 21:15:44 UTC（core-ru `WEEKLY-KIT.md`）；最后一次交付物写入 21:09:58 UTC（core-ru 网 PDF）。此前：D5 重建 2026-11-12 06:25–11:55 UTC；fix4 重建至 ~21:09 UTC。
- round-5 指纹取于 2026-11-12 21:17:47 UTC（`fingerprint.json` mtime），PROOF-NOTE-5.md 写于 21:41 UTC，协调员验收记入 run-log 2026-11-12 ~23:05 UTC（run-log:4844–4845，独立抽查 SHA 一致：pt 印 de64a14d7ce5、core 印 a114f1d24694、ja 文 465a2e4ebcd8）。
- 简报背景纠正（与上一名核对员结论一致，本人独立复核）：2026-11-11 23:48 UTC 与 2026-11-12 01:27 UTC 两度改 SHA 的是 *-ru 跨家字体路由重建（目标语≠ru、读者=ru，如 en-ru、de-ru），core-ru 明确排除在外；ru 家此后又经历 R1/R2 间距重建（00:38–02:47 UTC 11/12）、D5 重建、fix4 重建，全部早于 round-5 指纹。因此 round-5 晚于 ru 家最后一次重建，结论未被后续工作推翻。
- round-5 之后无 ru 家重建/修复记录：无 `scratch-reproof6-w47-ru`；run-log/ledger 在 2026-11-13 05:01 UTC（上一名核对员完成记录）之后无 ru 家生产改动条目。

## 逐版核对表

“最新核对”均为 round-5（PROOF-NOTE-5.md，结论 (a) CLEAN，0 findings）。磁盘 SHA 为本次实测（2026-11-13 ~07:15 UTC）。

| 版 | 最新核对 + 工号 | 核对 SHA（印 / 网 / 文） | 磁盘 SHA（印 / 网 / 文） | 一致？ | KIT §7 一致？ | 结论 |
|---|---|---|---|---|---|---|
| core-ru | round-5，03a5768c | a114f1d24694 / e37922c048d1 / 2a38d3dab649 | a114f1d24694 / e37922c048d1 / 2a38d3dab649 | 是（字节 24,713,343 / 3,898,280 / 60,953 全符） | 是（§9 L161–162 全值+字节；§7.9 J-6 记文 SHA） | VERIFIED CLEAN |
| ru-de | round-5，03a5768c | 36d4cb6795ae / acc21d4dd4a6 / 31d3eb3eb223 | 36d4cb6795ae / acc21d4dd4a6 / 31d3eb3eb223 | 是（20,880,736 / 3,334,229 / 63,483） | 是（各 2/2/1 处） | VERIFIED CLEAN |
| ru-en | round-5，03a5768c | 7339c020640f / a3148c31c5a9 / 6c6932fb809f | 7339c020640f / a3148c31c5a9 / 6c6932fb809f | 是（20,875,444 / 3,328,923 / 62,785） | 是（各 2/2/2 处） | VERIFIED CLEAN |
| ru-es | round-5，03a5768c | 047ef0fbf75a / 662998dc1e54 / bb298469263f | 047ef0fbf75a / 662998dc1e54 / bb298469263f | 是（20,880,148 / 3,333,651 / 64,176） | 是（§7 L53–54 印/网全值；L88 文 SHA 332c8e4f→bb298469263f 过渡已记） | VERIFIED CLEAN |
| ru-fr | round-5，03a5768c | 0c38972146f9 / b36ecf778e27 / 445daf81541a | 0c38972146f9 / b36ecf778e27 / 445daf81541a | 是（20,880,950 / 3,334,407 / 63,364） | 是（各 2/2/1 处） | VERIFIED CLEAN |
| ru-it | round-5，03a5768c | dc1e47616857 / 6ea69cc772a6 / a46c6da64262 | dc1e47616857 / 6ea69cc772a6 / a46c6da64262 | 是（20,877,136 / 3,330,610 / 63,970） | 是（各 2/2/1 处） | VERIFIED CLEAN |
| ru-ja | round-5，03a5768c | bc7bccfe15ca / dc9f27b03891 / 465a2e4ebcd8 | bc7bccfe15ca / dc9f27b03891 / 465a2e4ebcd8 | 是（27,365,839 / 3,692,713 / 64,504） | 是（各 2/2/1 处） | VERIFIED CLEAN |
| ru-ko | round-5，03a5768c | fece66f1bfec / a6a997780723 / 050d18839631 | fece66f1bfec / a6a997780723 / 050d18839631 | 是（21,975,394 / 3,494,572 / 65,030） | 是（各 2/2/2 处） | VERIFIED CLEAN |
| ru-nl | round-5，03a5768c | 5dedd8ecc30d / 1abee50e0035 / b600944e5e5f | 5dedd8ecc30d / 1abee50e0035 / b600944e5e5f | 是（20,876,260 / 3,329,737 / 64,011） | 是（各 2/2/1 处） | VERIFIED CLEAN |
| ru-pt | round-5，03a5768c | de64a14d7ce5 / a8c1afb03722 / 67ced8562a71 | de64a14d7ce5 / a8c1afb03722 / 67ced8562a71 | 是（20,883,714 / 3,337,256 / 65,102） | 是（各 2/2/1 处） | VERIFIED CLEAN |
| ru-zh-tw | round-5，03a5768c | 0c4bffc78bdc / cc348ad4ae16 / 948538470d3c | 0c4bffc78bdc / cc348ad4ae16 / 948538470d3c | 是（24,763,427 / 3,975,999 / 60,855） | 是（各 2/2/2 处） | VERIFIED CLEAN |

33/33 SHA-12 与字节数与 round-5 指纹逐项一致。KIT 内另有历史 SHA（D5、fix1–fix3、R1 中间值等旧值），均属历史记录行，非当前值；当前值行已逐版核实无误。抽查现值上下文：core-ru §9 L161–162 印/网全值+字节与磁盘逐字一致；ru-es §7 L53–54 印/网全值一致，L88 记文 SHA 由 D5 值 332c8e4f…→现值 bb298469263f…（F-2 附录重导出，字节不变 64,176），与磁盘一致。

## ru-es 17 项间距回归清单（ledger 1398 行）——重建后 census 覆盖确认

- 清单出处：ledger.md:1398，2026-11-11 23:13 UTC，ru-es re-proof (b)，工人 4ae3fffb，17 项全为间距回归（P1 `метеорологическаязима`、P2 `рожденияДеда`/`Профессиональныепраздники`、P5 `маркетплейсахскидки`、P8 Q135/A135 `заказываетподарок`、P8 `Atención:играть` 等；当时印 64cb48f9…/网 526873a8…/文 332c8e4f…）。
- 重建后 census 记录存在：`scratch-ru-rerun-R1/REBUILD-LOG.md` §5（ru-es，2026-11-12 00:38–02:04 UTC 两次构建）+ `census-after-ru-es-1-print.log` / `census-after-ru-es-1-web.log`（印=网）。
- 结论为 **0 真粘连**：census AFTER 为 12 tokens / 15 boundaries（由 BEFORE 170/212 降下），全部为箭头/级别假阳性（`→После`×3、`A2→B1`/`A2→B2`、`→Родительный`、P8 `→выходят/рассказывает/снял/сыграли/играет/победило/работаем` 2.40–2.41pt、`✓Véase` 2.41pt）；日志明记“0 real joins”。17 项逐项裁定在案：`13ноября` 2.47pt、`20ноября` 3.52pt、`19ноября` 3.48pt、`16ноября` 3.68pt、`Atención:играть` → 已分 `Atención: играть`、墨隙 2.36pt（=行常 2.36–2.41pt）；其余 `A.на`/`A.биография`/`результатов+` 等亦均在正常间隙。
- 链路完整性：R1 印 SHA `deb7b08e…` → D5 重建后印 `047ef0fbf75a…`（D5-REPORT-ru-2026-w47-ru-es.md，D5 census 429→0、弯引号 0、CENSUS PASS；D5-CENSUS-130.md L180 ru-es 0/0）→ fix4/F-2 后 round-5 指纹即现值 `047ef0fbf75a…`，与磁盘一致。D5 与 fix4 均未改动正文词串（文 SHA 仅 F-2 附录重导出一处过渡，见上表），间距结论未被后续重建推翻；round-5 另独立重跑 occlusion/boxtitle/spill/edge/D5 census 全绿（PROOF-NOTE-5 机械门禁表）。

## HEADS-NOTE.md 接受项

15 处 HEAD TOO WIDE 全部位于 *-ru 版（de-ru×4、en-ru×2、fr-ru×7、it-ru×1、pt-ru×1），ru 家 0 处；接受的 5 处亦全在他家。ru 家无接受项需要核实 KIT 记录。另：run-log 5159 条 O-R1（zh-cn-ru KIT F8 P7-a2 advance 422.72→426.14）为 *-ru 版观察项，非 ru 家版，不影响本家结论。

## 待修清单

无。11 版全部 VERIFIED CLEAN，无未闭合问题，第二阶段未触发（无 SHA 不符、无核对缺失/过期），无 wave-2 SHA 同步项。

## 方法与只读声明

- 只读：仅 sha256sum 实测、stat/find mtime、grep、读 PROOF-NOTE/fingerprint/KIT/census 日志；未改生产文件、未 commit/push、未跑 lint --write、未跑任何构建/门禁重建、未渲染；未碰 ru 以外任何版。
- 工作目录：`hidden_files/w47/scratch-verify-ru-final/`（本报告 + `disk-sha.txt`）。
- 磁盘停手线复核：开工 `df -k` 101,698,408 KB（97G），收尾 101,750,644 KB（98G），均低于 100G 停手线 104,857,600 KB；第一阶段纯只读已完成，第二阶段未触发故未渲染。
