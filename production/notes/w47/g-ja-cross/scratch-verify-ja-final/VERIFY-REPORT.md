# W47 ja 家庭 §8.4 终态核对报告（第二轮核对，恢复协调员 #6 派单）

- **核对员**：W47 ja 家 §8.4 终态核对员（恢复协调员 #6 派单；与建造者、第一至四轮校对员/修复工人、#4 轮核对员均不同人）
- **日期**：2026-11-13，磁盘核对时点 07:12–07:17 UTC（02:12–02:17 EST）
- **范围**：ja 家 11 版（core-ja = ja-zh-cn + 10 个 fan-out：ja-de/ja-en/ja-es/ja-fr/ja-it/ja-ko/ja-nl/ja-pt/ja-ru/ja-zh-tw）
- **工作目录**：`hidden_files/w47/scratch-verify-ja-final/`（本报告、磁盘 SHA 实测 `disk-sha-now.txt`、#4 轮附录 A 摘录 `verify-appendix-a.txt`）
- **约束遵守**：纯只读核对，未改任何生产文件，未 commit/push/add/reset/stash，未跑 lint（无 `--write`），未碰 insert.py，未碰 ja 以外任何版。未渲染（第二阶段未触发，无需渲染）。磁盘 `df -h` 97G（`df -k` 101,699,760 KB），低于 100G 停手线（104,857,600 KB），距配额上限约 105G 尚有约 8G。

## 全家结论：CLEAN

**ja 家 11/11 最终状态仍然成立：10 版 VERIFIED CLEAN + ja-ru 第五轮重校 CLEAN。**全部 33 个磁盘 SHA 与最新核对记录逐字节一致，无一版触发第二阶段全新重校。待修内容清单：无。仅 1 项 KIT 文字同步记入 wave-2 清单（见 §3，非内容缺陷、非核对缺口）。

## 1. 逐版核对表

| 版 | 最新核对 + 工号 | 核对 SHA（印 / 网 / text.md，SHA-12） | 磁盘 SHA（本轮实测） | 一致？ | KIT §7 一致？ | 结论 |
|---|---|---|---|---|---|---|
| core-ja（zh-cn） | 第四轮 aa94c0d9，(a) CLEAN，`scratch-reproof4-w47-ja/PROOF-NOTE-4.md` §1 | `0ce5e4b872ae` / `0f9098ff3bf0` / `55c570f1bd0e` | 相同（25,973,509 / 4,654,731 / 44,432 B） | 是（3/3） | 是（各 1 处） | **VERIFIED CLEAN** |
| ja-de | 第四轮 aa94c0d9，(a) | `4283e8a74ff9` / `c24dfb09d7d0` / `0d8d1de78a06` | 相同（25,813,856 / 4,387,416 / 46,520 B） | 是（3/3） | 是（印/网各 2 处，文 1 处） | **VERIFIED CLEAN** |
| ja-en | 第四轮 aa94c0d9，(a) | `c6a15edb8a6c` / `0560f0e4ea85` / `fb5a4700d3c9` | 相同（25,806,211 / 4,379,966 / 45,706 B） | 是（3/3） | 是（印/网各 2 处，文 1 处） | **VERIFIED CLEAN** |
| ja-es | 第四轮 aa94c0d9，(a) | `74066b869920` / `43a26e56278f` / `d8e0c3018361` | 相同（25,814,013 / 4,387,651 / 46,702 B） | 是（3/3） | 是（印/网各 2 处，文 1 处） | **VERIFIED CLEAN** |
| ja-fr | 第四轮 aa94c0d9，(a) | `9d4c6114fb31` / `ef073db3df37` / `badb0a6e7d00` | 相同（25,812,296 / 4,386,312 / 46,882 B） | 是（3/3） | 是（印/网各 2 处，文 1 处） | **VERIFIED CLEAN** |
| ja-it | 第四轮 aa94c0d9，(a) | `e44a8fcba1ba` / `3cb1e9559b3a` / `91224d88a55d` | 相同（25,807,665 / 4,381,291 / 46,692 B） | 是（3/3） | 是（印/网各 2 处，文 1 处） | **VERIFIED CLEAN** |
| ja-ko | 第四轮 aa94c0d9，(a) | `b78a3f6d5a39` / `bdf5074b3698` / `b1736ccf46f8` | 相同（28,141,037 / 4,552,025 / 47,722 B） | 是（3/3） | 是（印/网各 2 处，文 1 处） | **VERIFIED CLEAN** |
| ja-nl | 第四轮 aa94c0d9，(a) | `d6f14754f22c` / `97ee26ba1616` / `7f8f6638e635` | 相同（25,805,479 / 4,379,026 / 45,627 B） | 是（3/3） | 是（印/网各 2 处，文 1 处） | **VERIFIED CLEAN** |
| ja-pt | 第四轮 aa94c0d9，(a) | `3cca426dcbec` / `a573debf0755` / `9c9609378189` | 相同（25,814,751 / 4,388,490 / 46,696 B） | 是（3/3） | 是（印/网各 2 处，文 1 处） | **VERIFIED CLEAN** |
| ja-ru | **第五轮**（#4 轮核对员，(a) CLEAN，`scratch-verify-ja/VERIFY-REPORT.md` §4；见 §2） | `44d884ac6b54` / `d130ae325fed` / `f934bcf1d9f4` | 相同（25,898,158 / 4,469,712 / 53,004 B） | 是（3/3） | 是（现值各 1 处，§12 fix-xru；§8 主段落仍为旧值，见 §3） | **VERIFIED CLEAN** |
| ja-zh-tw | 第四轮 aa94c0d9，(a) | `4b09db1088b8` / `649ac196e81a` / `77fb0f36c75b` | 相同（25,988,418 / 4,789,292 / 44,361 B） | 是（3/3） | 是（印/网各 2 处，文 2 处） | **VERIFIED CLEAN** |

## 2. 核对链与时效证据（机械化比对，非目视）

1. **版数**：生产目录 `production/2026-w47/` 下 `2026-w47-ja-*` 共 10 个 + `core-ja` = **11 版**，与 run-log、PROOF-NOTE-4、#4 轮 VERIFY-REPORT 所称 11 版一致，无出入。注：无独立的 `2026-w47-ja-zh-cn` 目录——core-ja 即 ja-zh-cn 版（其 text.md 名为 `2026-w47-ja-zh-cn.text.md`），三方记录一致。
2. **磁盘 SHA vs #4 轮附录 A**：`diff verify-appendix-a.txt disk-sha-now.txt` → **IDENTICAL，33/33**。#4 轮核对员 2026-11-13 04:57 UTC 的磁盘快照与本轮 07:12 UTC 实测逐字节相同（全量 SHA-256 + 文件名）。
3. **磁盘 SHA vs 第四轮指纹表**（PROOF-NOTE-4 §1，程序逐项比对字节数 + SHA-12）：10 版 30/30 OK；ja-ru 仅印/网 MISMATCH、text.md OK——系第四轮后 *-ru 重建（见下），非未记录变动。
4. **ja-ru 的第五轮记录**：第四轮后，跨家 *-ru 修复（Latin 标题误入 Noto Sans）重建了 ja-ru：工人 fec69813，2026-11-12 23:50–23:51 UTC，印 `44d884ac…`/25,898,158 B、网 `d130ae325fed…`/4,469,712 B，text.md 未变。#4 轮核对员随即对 ja-ru 做了**全新全量重校（第五轮）**，结论 (a) CLEAN，记录在 `scratch-verify-ja/VERIFY-REPORT.md` §4（150 题、日期/星期、事实/算术、8 页看图、7 门禁全绿、xru 探针复核均在案）。本轮磁盘 SHA 与该轮记录的 3 个值逐字节一致，故第五轮结论仍然成立。
5. **D5 重建时序**：D5 重建 ja 家 11 版完成于 2026-11-12 白天（`scratch-d5-ja/RUN-LOG.md`；生产 PDF mtime 14:09–20:06 UTC；门禁全绿、freeze 8/8、census PASS），**早于**第四轮重校（2026-11-12 ~22:40 UTC）。第四轮指纹即 D5 后状态，本轮 30/30 一致证明 D5 后无再改动。任务简报所称“其后 D5 重建可能改过 SHA”——就 ja 家而言，D5 重建发生在第四轮之前，已被第四轮覆盖；第四轮之后只有 ja-ru 一次 *-ru 重建，已被第五轮覆盖。
6. **mtime 核查**：`find core-ja 2026-w47-ja-* -newermt "2026-11-13 05:00 UTC"`（#4 轮核对时点）→ **无结果**。11 版全部生产文件 mtime ≤ 2026-11-12 23:52 UTC（ja-ru KIT），核对后零改动。
7. **run-log / ledger 复核**：2026-11-13 05:00 UTC 之后 run-log 无任何 ja 家生产变动记录（05:00 后条目为 es-ru F1 修复、de round-3/round-4、协调员 #5/#6 交接）。05:00 之前最后一条 ja 相关记录为 01:15 UTC *-ru 扫查：工人 09cda9c4 报 ja-ru occlusion + boxtitle 双门 PASS（与第五轮结论一致）。ledger 尾部无 ja 家新增条目。
8. **KIT §7 核对**：11 版 KIT 内当前磁盘印/网/text.md SHA-12 均在位（core-ja 各 1 处；其余 9 版印/网各 2 处、文 1 处；ja-zh-tw 文 2 处；ja-ru 现值各 1 处）。见 §3 的唯一例外。

## 3. KIT 文字同步（wave-2 清单，非核对缺口）

- **ja-ru KIT §8 主段落仍以重建前的值为交付值**（印 25,970,343 B `04b2f315e267…`、网 4,540,808 B `0726eda64903…`），未同步到 fix-xru 后的现值；但 KIT §12 fix-xru 节含当前值（印 `44d884ac…`/25,898,158 B、网 `d130ae325fed…`/4,469,712 B、text 未变），与磁盘一致。与 #4 轮报告 §5、COVER-REPORT 待办所述为同一项。**只记录，不改 KIT。**按任务书：这是 KIT 文字待 wave-2 更新，不是核对缺口（磁盘 SHA 与核对记录一致）。
- 其余 KIT 内的旧 SHA 均为有标注的历史构建记录（D5 各轮、fix1 等），不列入清单。

## 4. 第二阶段：未触发

无一版磁盘 SHA 与核对记录不符，无一版核对缺失，故**未做全新重校**，未写 PROOF-NOTE，未渲染（磁盘零新增占用，仅本报告与两份 SHA 清单文本文件）。

## 附录：当前磁盘全量 SHA-256（2026-11-13 07:12 UTC 实测）

```
core-ja/Lucerna-VOL4.pdf 0ce5e4b872ae4d53fc639bff0ae2df3cf2bfd91149bd08b04400920e21adc214
core-ja/Lucerna-VOL4-web.pdf 0f9098ff3bf0836c279960beffdb1ff619c1cdb01fceef699046c0a77be1e9ef
core-ja/2026-w47-ja-zh-cn.text.md 55c570f1bd0e9ea4d907960fe0fc472fe69440bacf67a83af40d0d48b977e1aa
2026-w47-ja-de/Lucerna-VOL4-JA-DE.pdf 4283e8a74ff969a5d6d565e5cc03cd0618648ed827e6cd8843ce5ec85326c7a5
2026-w47-ja-de/Lucerna-VOL4-JA-DE-web.pdf c24dfb09d7d0c54333c6f43aafdf697a08e99a178c5be5b762bc571c90086d4c
2026-w47-ja-de/2026-w47-ja-de.text.md 0d8d1de78a06d4df371b88425cb66f330222e6ca1a200632fdcdc48c8c95bd22
2026-w47-ja-en/Lucerna-VOL4-JA-EN.pdf c6a15edb8a6c9e2954cb844b38b36a27f19d404ede7ad5084c3d3389db3410cf
2026-w47-ja-en/Lucerna-VOL4-JA-EN-web.pdf 0560f0e4ea8520899c0b7054ded812d2a16fba6cec0f9e55cfc3bec8b99c1d8d
2026-w47-ja-en/2026-w47-ja-en.text.md fb5a4700d3c94cd17039d8b69d2626e35ed115812fdcb5ca34f17294f8860c3f
2026-w47-ja-es/Lucerna-VOL4-JA-ES.pdf 74066b86992080d5de346594ec437f0686932daa2b68d2acc176925d1933bd53
2026-w47-ja-es/Lucerna-VOL4-JA-ES-web.pdf 43a26e56278f7b7cca4219c18ce508bdc2fe1662e99e2f91584e4ebcb71f09f2
2026-w47-ja-es/2026-w47-ja-es.text.md d8e0c3018361cdce75084706e6857e642822992ecab8ac55f5865b861091ebb0
2026-w47-ja-fr/Lucerna-VOL4-JA-FR.pdf 9d4c6114fb31cca2a912c2313f756667277748f048b4c0041aba10bc051e4507
2026-w47-ja-fr/Lucerna-VOL4-JA-FR-web.pdf ef073db3df3789ef4326440df33cea387675e0ed1b5dacc17161220bf0622c5a
2026-w47-ja-fr/2026-w47-ja-fr.text.md badb0a6e7d00858afda9e6d1e158a915e93bd1ee41478e23bf3857cf23c72563
2026-w47-ja-it/Lucerna-VOL4-JA-IT.pdf e44a8fcba1ba429a2ad6c463cca8f4e33559d1a65139e46fa27d367f4242cf6c
2026-w47-ja-it/Lucerna-VOL4-JA-IT-web.pdf 3cb1e9559b3a6e7763858cbaeae56eee9a61e54a083e8ade9c5c950e513a62fb
2026-w47-ja-it/2026-w47-ja-it.text.md 91224d88a55d5dc7ae8c3411e62d4199fe32d4028293223ba5373bd3a21125aa
2026-w47-ja-ko/Lucerna-VOL4-JA-KO.pdf b78a3f6d5a39da219b61d8ae179c397622259484dfe3a4804f2027a7be51d0d2
2026-w47-ja-ko/Lucerna-VOL4-JA-KO-web.pdf bdf5074b36981cf6bcf913a8d732a604dd37d4be9a65398c6c6a43b79f4c3f73
2026-w47-ja-ko/2026-w47-ja-ko.text.md b1736ccf46f8cd2cc7646038c5163849e306210884d4b15fbb3f388a82535517
2026-w47-ja-nl/Lucerna-VOL4-JA-NL.pdf d6f14754f22c8ee43d343a59d77e6cf0df271465d9dfcbe3b094a5368da2246d
2026-w47-ja-nl/Lucerna-VOL4-JA-NL-web.pdf 97ee26ba16163696bd9a1ff30968bd71e8eab18af4cc75fcf9f2e04ded95f338
2026-w47-ja-nl/2026-w47-ja-nl.text.md 7f8f6638e6352eb8ba9c1a2b3283f0e2436ea65613cf15c109ae3f067f69af4d
2026-w47-ja-pt/Lucerna-VOL4-JA-PT.pdf 3cca426dcbec961b4a1ddb54248e05f1d1771f9661fd9df5ed70d10773749dbf
2026-w47-ja-pt/Lucerna-VOL4-JA-PT-web.pdf a573debf07556431b5d8b20d95f088d9f8f098c84935380f9a7fb3635ab5a81e
2026-w47-ja-pt/2026-w47-ja-pt.text.md 9c9609378189a5b32b894b5c26adbdf4e8e1b23bbbe7b923f7a6198c4c62564a
2026-w47-ja-ru/Lucerna-VOL4-JA-RU.pdf 44d884ac6b543a6be3f4186ffe8ce22899a5ba90bc1f951539e0a3176af822a4
2026-w47-ja-ru/Lucerna-VOL4-JA-RU-web.pdf d130ae325fedb8325a724aef3ee3889b1db01c9ee0d5091b74644a9ab388dbd5
2026-w47-ja-ru/2026-w47-ja-ru.text.md f934bcf1d9f4611d094ed6f55a1f76fc8da74663cfe647c9fed17025af3d4eec
2026-w47-ja-zh-tw/Lucerna-VOL4-JA-ZH-TW.pdf 4b09db1088b81f4a56bfd5ee7126088cb2762e2348279f402032c1749bd76c8c
2026-w47-ja-zh-tw/Lucerna-VOL4-JA-ZH-TW-web.pdf 649ac196e81abf1a99524847e89ca4d5104080f12b644aa234aee0b94819b5cc
2026-w47-ja-zh-tw/2026-w47-ja-zh-tw.text.md 77fb0f36c75bb4713873b33793d63fc243f27fee3d4450c1d1e8f5da94ed416f
```
