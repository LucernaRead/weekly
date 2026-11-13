# W47 ru 家 §8.4 状态核对报告

- 核对员：ru 家 §8.4 状态核对员（与 round-5 校对员 03a5768c、fix4 工人 bd49579f 均不同人；只读核对，未改任何生产文件）
- 时间：2026-11-13 ~04:59 UTC（2026-11-12 23:59 EST）
- 范围：ru 家 11 版：core-ru（= ru-zh-cn）+ `2026-w47-ru-{de,en,es,fr,it,ja,ko,nl,pt,zh-tw}`
- 依据：SOP §8 / §8.4；`scratch-reproof5-w47-ru/PROOF-NOTE-5.md` + `fingerprint.json`；run-log.md；`scratch-fix-xru-heads/HEADS-NOTE.md`
- 磁盘：96G 已用 / 54G 可用，未触 100G 停线

## 总结论：round-5 结论仍成立，11/11 VERIFIED CLEAN，无需重校

round-5（校对员 03a5768c，2026-11-12 ~23:05 UTC）结论为 (a) CLEAN、0 findings。
本次实测：ru 家 11 版印/网/text.md 共 33 个 SHA-256 前 12 位 + 字节数，与 PROOF-NOTE-5 指纹逐项一致，
且 `find -newermt "2026-11-12 23:05 UTC"` 在 ru 家 11 个生产目录内命中 **0 个文件**——
round-5 之后没有任何人/工人动过 ru 家的任何生产文件。

## 关键时间线纠正（任务简报背景有误）

任务简报称“*-ru 跨家修复重建 11/11 于 2026-11-12 ~18:58 EST 完成（ru 家多版重建改 SHA）”。
实测纠正：**该重建改的是 *-ru 版（目标语≠ru、读者=ru，如 en-ru、de-ru……），不是 ru 家版。**
证据：
- *-ru 重建工人 A/B/C 的 11 版清单（en/de/es/fr/nl/pt/zh-cn/zh-tw/it/ja/ko + -ru）全为他家版；run-log 明确写
  “core-ru 明确排除”；
- ru 家 11 版 svglib.py 的 `_D5_READER` 均为 `latin`（ru-de/en/es/fr/it/nl/pt）或 `cjk`（core-ru/ru-ja/ru-ko/ru-zh-tw），
  从无 `"ru"`；`_D5_READER == "ru"` 分支虽在代码里，但对 ru 家是死分支，未被触发、未被修；
- 其后 HEAD TOO WIDE 裁定 15 处（de-ru×4、en-ru×2、fr-ru×7、it-ru×1、pt-ru×1）与 28 处改道回归修复，
  全部位于 *-ru 版，不含任何 ru 家版；
- 其后 de/fr/pt 三家重校与修复亦只动他家版。
因此 round-5 的 SHA 晚于 ru 家最后一次重建（fix4，~23:00 UTC），round-5 结论未被后续工作推翻。

## 逐版核对

“最后重校”均为 round-5（PROOF-NOTE-5.md，2026-11-12 ~23:05 UTC，结论 CLEAN 0 findings）。
磁盘 SHA 为本次实测（2026-11-13 ~04:59 UTC）。

| 版 | 最后重校结论 | 当前印 PDF SHA-12 / 字节 | 当前网 PDF SHA-12 / 字节 | 当前 text.md SHA-12 / 字节 | 结论 |
|---|---|---|---|---|---|
| core-ru | CLEAN | a114f1d24694 / 24,713,343 | e37922c048d1 / 3,898,280 | 2a38d3dab649 / 60,953 | VERIFIED CLEAN |
| ru-en | CLEAN | 7339c020640f / 20,875,444 | a3148c31c5a9 / 3,328,923 | 6c6932fb809f / 62,785 | VERIFIED CLEAN |
| ru-de | CLEAN | 36d4cb6795ae / 20,880,736 | acc21d4dd4a6 / 3,334,229 | 31d3eb3eb223 / 63,483 | VERIFIED CLEAN |
| ru-es | CLEAN | 047ef0fbf75a / 20,880,148 | 662998dc1e54 / 3,333,651 | bb298469263f / 64,176 | VERIFIED CLEAN |
| ru-fr | CLEAN | 0c38972146f9 / 20,880,950 | b36ecf778e27 / 3,334,407 | 445daf81541a / 63,364 | VERIFIED CLEAN |
| ru-it | CLEAN | dc1e47616857 / 20,877,136 | 6ea69cc772a6 / 3,330,610 | a46c6da64262 / 63,970 | VERIFIED CLEAN |
| ru-pt | CLEAN | de64a14d7ce5 / 20,883,714 | a8c1afb03722 / 3,337,256 | 67ced8562a71 / 65,102 | VERIFIED CLEAN |
| ru-nl | CLEAN | 5dedd8ecc30d / 20,876,260 | 1abee50e0035 / 3,329,737 | b600944e5e5f / 64,011 | VERIFIED CLEAN |
| ru-ja | CLEAN | bc7bccfe15ca / 27,365,839 | dc9f27b03891 / 3,692,713 | 465a2e4ebcd8 / 64,504 | VERIFIED CLEAN |
| ru-ko | CLEAN | fece66f1bfec / 21,975,394 | a6a997780723 / 3,494,572 | 050d18839631 / 65,030 | VERIFIED CLEAN |
| ru-zh-tw | CLEAN | 0c4bffc78bdc / 24,763,427 | cc348ad4ae16 / 3,975,999 | 948538470d3c / 60,855 | VERIFIED CLEAN |

33/33 SHA-12 与字节数与 round-5 指纹逐项一致（core-ru 两份 text.md 字节一致，取 `2026-w47-ru-zh-cn.text.md`）。

## KIT §7 SHA 核对（step 4）

11/11 一致，无 wave-2 清单项：
- core-ru：KIT §9 交付行明记印 `a114f1d24694…`（24,713,343 B）与网 `e37922c048d1…`（3,898,280 B），
  §7.9（J-6 补修 4）记 text `2a38d3dab649`——与磁盘一致。
- 10 版 fan-out：KIT §7“Outputs/实测文件”行（ru-en L52–54 等）明记三 SHA 全值与字节数，与磁盘一致；
  各版 §7 末条 fix-4 记录亦含同一组 SHA。
- ru-zh-tw：KIT §1 文件表三 SHA 全值与字节数与磁盘一致。
- 注意：KIT 内另有大量历史 SHA（D5、fix1–fix3 等旧值），均属历史记录行，非当前值；当前值行已逐版核实无误。

## HEADS-NOTE.md 接受项核对

15 处 HEAD TOO WIDE 全部位于 *-ru 版（de-ru、en-ru、fr-ru、it-ru、pt-ru），**ru 家 0 处**；
接受的 5 处（en-ru A1/A2、it-ru A3、fr-ru A4、de-ru A5）亦全在他家。
ru 家无接受项需要核实 KIT 记录，不重报、不新增。
附带：ru 家 KIT 中 head_check 均为 PASS 0 defects（ru-zh-tw J-6 条明记），无待处理警告。

## 待修清单

无。11 版全部 VERIFIED CLEAN，无未闭合问题，无需全新重校（step 3 未触发），无 wave-2 SHA 同步项。

## 方法与只读声明

- 只读：仅 sha256 实测、grep、find -newermt、KIT 文本核对；未改生产文件、未 commit/push、未跑 lint --write、
  未跑任何构建/门禁重建；未碰 ru 以外任何版。
- 工作目录：`hidden_files/w47/scratch-verify-ru/`（本报告 1 文件）。
- 备注：网 PDF SHA 非确定性（run-log 04:08 条已有记录），但本次 11 版网 SHA 与 round-5 实测值逐字节一致，
  且无任何文件 mtime 变化，故不存在“同内容不同 SHA”的歧义。
