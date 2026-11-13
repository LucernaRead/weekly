# GATE-LOG — W47 zh-tw-es proof2（重扩散新版）

- 版：`2026-w47-zh-tw-es`；校对：2026-11-11 ~19:30–20:35 UTC
- 探针：`git hash-object -w /dev/null` rc=0；scratch 真实写文件 rc=0；`TMPDIR=<scratch>/tmp`；`PYTHONDONTWRITEBYTECODE=1` 全程
- 驱动：本 scratch 内 `gates.py`（自重扩散 `gates.py` 复制，M 路径改向本 scratch；并修其已知 bug：p8 `extra` 改读 compare JSON 的 `extra` 键，不再读不存在的 `extra_count`）
- 日志：`gates/es-proof2/`；重建日志：`rebuild/run.log`、`rebuild/render.log`

## 门禁汇总（全部通过；freeze diff --strict-cjk 见末行说明）

| # | 门 | 结果 |
|---|---|---|
| 1 | run.py RC / 题量 / 0 溢出 | RC=0；150 题；A2 44 / B1 74 / B2 32；分页 10/18/18/18/18/18/12/38；类型 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1；0 FLOW OVERFLOW；日志无 WARNING/TOO WIDE/ERROR。P7 col3 1823.3 / teaser 2577.3 |
| 2 | SVG 重建 8/8 字节一致 | run.py 重建后 `sha256sum -c snapshot-before.sha256`：19/19 OK（含 8 SVG + 8 cards + 印/网 PDF + text.md） |
| 3 | 重渲印 PDF 与交付逐字节相同 | render.py RC=0；重渲 `Lucerna-VOL4-ES.pdf` 23,256,381 B，SHA `e32c58c4…54a2c` 与交付一致；cards 8 张亦字节一致 |
| 4 | freeze 核心 baseline 8/8 | `freeze.py baseline` 8/8 SVGs byte-identical；核心完整性 OK（核心 8 个 SVG 重哈希未变） |
| 5 | freeze diff（core vs edition） | 文字多重集 diff：讲解层 EN→ES 一一对应替换，中文正文零增删。`--strict-cjk` 字面 FAIL（见观察 2）：新增 CJK 仅 西/班/牙 ×9，全部位于家具「西班牙語講解」（页脚×8 + P1 badge×1）；非缺陷 |
| 6 | occlusion | selftest rc=0（6 类 planted 全触发）；audit flags **0** |
| 7 | 奶油盒 canonical 扫描 | 36 盒；负内清除 0；分页最小内清除 P1 18.8 / P2 15.8 / P3 15.8 / P4 9.8 / P5 6.4 / P6 19.9 / P7 12.5；P7 工具盒 +40.5 / +12.5 / +14.0 |
| 8 | 奶油盒 PIL 真墨扫 | STRADDLE **4**（见 PROOF-NOTE 观察 1；旧版 5，新版 4，修好 1，引入 0）；CREAM-COVER **0**；P7 最小清除 8.0 |
| 9 | boxtitle | 36 盒；超框 **0**；最小标题右余 9.8px |
| 10 | spill 扫（页界） | occlusion_audit 解析 3399 元素，0 出界（1950×2700） |
| 11 | 孤儿扫 | 被注词 21 项正文出现 2–70 次；P8 填空键 32/32 出自 P1–P7 正文；孤儿 **0** |
| 12 | p8 extract 150/150 | `p8.py extract --total 150` noted_set = 150 |
| 13 | p8 compare | vs 核心 `--core-p8/--edition-p8`：**CLEAN**；missing=[]、extra=[]（本轮驱动已修取键 bug，实测 []）、keydiff=[] |
| 14 | P8 最小字号 ≥9.75pt | 印/网均为 **9.75pt**（恰 SOP §1.1 下限）；最大 34.5pt；P1 顶部字号 [147.0, 45.0, 27.0, 24.0] |
| 15 | §1.1 | 纸 #fbfaf6 8 处；金色/砖色类 fill 0；VOL.5 恰 1 处（P7 下期预告）；VOL.4 10 处；徽章色 #5c6e30/#46581f/#37402f 齐全；页脚 `Página N de 8` 8/8 |
| 16 | 日期星期全验 | 14 个日期 `date -d` 核对，与正文星期全部相符（见 PROOF-NOTE） |
| 17 | checks.py | **PASS**：8 句各 2 次；SIMP_ONLY_HITS []；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] |
| 18 | 印/网文字层比对 | pdftotext -layout 印/网各 108,948 B、字节相等，字符多重集差 0；本週日 11/11、下週日 0/0、BABYMONSTER 0/0、取捨 2/2、end point 0、小雪 36/36 |
| 19 | keycheck | 填空键 54/54 出自正文，无缺失；答案键 1–150 连续（150/150） |
| 20 | leak 扫 | deny 命中 0；唯一共享长 ASCII 串为 Q140 选项行「A. 12:00 · B. 14:00 · C. 19:00」（构造共享，非泄漏） |
| 21 | abutting | P6 18:30「頒獎典禮」墨右缘 990.8 与 19:00「夜間遊行」墨左缘 991.4，缝 **0.6px**（与核心先例一致；渲染裁切目视有发丝间隔、无重叠） |
| 22 | KIT §1 三 SHA 与盘上一致 | 印/网/text.md 三 SHA 在 KIT 内各命中 1 处，与盘上实测一致 |
| 23 | 标题实测数 | **77 条**（规则见 PROOF-NOTE；分頁 9/11/11/9/12/8/9/8）；“56 titles”非本版数 |
| 24 | 目视 | 8 页联络表 `contact-8pages.png` 全部看过：无溢出、无重叠、无页脚碰撞；4 处 STRADDLE 与 P6 发丝缝均有 200dpi 交付 PDF 裁切为证 |

## 备注

- web PDF 未重渲染（字节不可复现，只比文字层——门 18）。
- KIT K6/K7 是另派的文档收尾，不属本轮。
- 本轮驱动相对重扩散驱动的唯一改动：p8 `extra` 取键 bug 修复（`extra_count` → `extra`），其余逻辑、阈值未动；门 13 的 `extra: []` 为实测值。
