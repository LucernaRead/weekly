# FIX-LOG — 2026-W47 de-pt · fix1（D1 返修，重建版）

- Edition: `2026-w47-de-pt`（德语正文，葡萄牙语讲解），VOL.4，刊期 2026-11-16–22
- Builder: fix1（重派；上一棒 5d246196 因服务重启在探针后即失败，未动任何源文件）
- 时间：2026-11-11（UTC）
- 缺陷来源：proof1 PROOF-NOTE.md 结论 (b)，唯一缺陷 D1
- 范围：只修 D1，不扩大；不碰 de-es 版任何文件；不碰 tools/；不 commit、不 push、不派 subagent

## 0. 探针（开工及每次写盘前重探，均通过，无 EDQUOT）

`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`
+ 在本 scratch 目录真实写文件（`.probe` / 本日志 / 各门日志）。

## 1. 改了什么（逐文件逐行）

### 唯一源码改动

| 文件 | 行 | 改前 | 改后 |
|---|---|---|---|
| `production/2026-w47/2026-w47-de-pt/content8.py` | 75 | `("A2", "A", "ist (3.ª pers. sg.)"),` | `("A2", "A", "ist (3.ª pess. sg.)"),` |

- 改动性质：答案键 Q120 注释缩写一字之误（`pers.` → `pess.`，补一个 `s`）。
  葡萄牙语 pessoa 的标准缩写是 `pess.`；`pers.` 是西班牙语 persona 的缩写，属从 de-es 版跨语言复制残留。
- 其余 12 处同类注释（Q113–119、Q145–149）本来就是 `pess.`，未动。
- 改后全版源码核查：`grep -rn "pers\." content*.py bslib4.py verify.py svglib.py render.py run.py` → **0 处**；
  `content8.py` 内 `pess.` 出现 **13 次**（Q113–120 八处 + Q145–149 五处）。

### 未动的文件（明确记录）

- `de-es` 版任何文件：未读未写（只在 tr_pt/tr_es 检查时以 grep 只读核对了 tr_es.py 的 `pers.` 行，见 §4）。
- `tools/`：未动。`tr_pt.py`（机制层）：**只查未改**（见 §4）。
- 未跑 `transform.py`：重建只跑 run.py → render.py → webpdf → verify → 各门禁（驱动
  `scratch-fix-de-pt1/build_fix1.py`，与 fan-out 驱动同步骤同门槛，唯独不含 transform 步——
  transform 会从 tr_pt.py 重新生成 content8.py，把已修的 `pess.` 盖回 `pers.`）。

### 重建产物（源自改后源码）

只 P8 相关产物随改动变化；P1–P7 源码未动，build.log 各页 flow end 与 KIT rebuild-3 逐值一致
（P1-headline 1554、P3-main 916、P8-battery 1409.445、P8-keys 2457 等），freeze 各页 +/− 计数与 rebuild-3 逐值一致。

## 2. 成品 SHA（重建前 → 重建后，实测）

| 文件 | 重建前（旧） | 重建后（新） |
|---|---|---|
| 印刷 `Die-Lucerna-VOL4-de-pt.pdf` | 10,968,908 B · `33e2dc7d5fe62549c605a622d61d59ade0dd5fa4e54aa3a7901dbbc486d260aa` | **10,968,903 B · `5f2bc3d4590fca0e6509fda53ddafe6a4b1cc618a5c23e78f5181e177143c2aa`** |
| 网页 `Die-Lucerna-VOL4-de-pt-web.pdf` | 1,599,432 B · `a251196e6d411c09f3b4ccef54876da6fcacd96fd899198154b9836118b877bb` | **1,602,461 B · `62371d80a399779aded2e9dbcd3ea303f46f338d7c9d9241dc929e4a1a0e7adb`** |
| `2026-w47-de-pt.text.md` | 49,812 B · `4257920750577d5ad5f0e58ca8959dcb8ef4779cafd1a932a170405c24790dbf` | **49,812 B · `e2ee96ebd9dca775598431f87c511f53ed04dec2547896586d46a2c57a800928`** |

- 两份 PDF 均为 8 页，`pdfinfo` 页尺寸 1462.5 × 2025 pt 一致。
- text.md 字节数不变（`pers.` 与 `pess.` 同为 5 字符）；印版小 5 B、网版大 3,029 B，
  属 PDF 流重压/字体子集差异（见 §5 T1 说明），内容层见门禁表一致。
- 旧 SHA 与任务简报/PROOF-NOTE 核对全符（重建前实测，见开工核对）。

## 3. D1 五重核验（改后全部为 `pess.`，`pers.` 归零）

| 位置 | `pers.` | `pess.` | Q120 原文 |
|---|---|---|---|
| content8.py | 0 | 13 | `("A2", "A", "ist (3.ª pess. sg.)")` |
| svg/p8-uebungen.svg | 0 | 13 | — |
| 2026-w47-de-pt.text.md | 0 | 13 | `120. A (ist (3.ª pess. sg.))` |
| 印版文字层（pdftotext P8） | 0 | 13 | `120. A (ist (3.ª pess. sg.))` |
| 网版文字层（pdftotext P8） | 0 | 13 | `120. A (ist (3.ª pess. sg.))` |

13 = Q113–120（8 处）+ Q145–149（5 处），与复校笔记的同类注释分布一致。

## 4. 机制层 tr_pt.py 检查结论（只查未改）

**有同一 `pers.` 串。位置（两份副本一致）：**

- `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-de/tr_pt.py:243`
  `'ist（第三人称单数）': 'ist (3.ª pers. sg.)',` —— 全文唯一 1 处 `pers.`；
  其余同类映射 L236–242、L274–277 均为正确的 `pess.`。
- 同一串亦在 `scratch-fanout-de-rebuild-A/tr_pt.py:243`（freeze_direct.py 读的是这份副本）。

**建议（机制层改动由协调员另派，fix1 不擅自改）：** 将 tr_pt.py:243 的值改为
`'ist (3.ª pess. sg.)'`（与 L236–242、L274–277 一致）。此后任何从该机制表重新 transform
的 de-pt 版都不会再引入 D1。

**对照（只读核对，未碰）：** de-es 的 `tr_es.py` L236 起全部用 `pers.`，在西班牙语里正确，
de-es 版不碰、不改。

**直接后果（已实测，见 §5 freeze_direct 行）：** 因 tr_pt.py:243 仍为旧值，freeze_direct 源码层
报 1 条未入账新增字面量 `'ist (3.ª pess. sg.)'`，源码层 FAIL；渲染层 8/8 全部通过、
各页 frozen 计数与 sha8 与 rebuild-3 逐值一致。待机制层修正后，源码层应恢复 0 未入账、PASS。
此 FAIL 是 edition-only 修复的预期机械后果，不是重建错误。

## 5. 门禁结果（全部重跑，日志在本目录）

| 门 | 命令要点 | 结果 |
|---|---|---|
| build 驱动 | `build_fix1.py`（run → render → webpdf → verify → occlusion → p8 → freeze → pdftotext → chips → export → P8 字号） | **ALL GATES PASS**，DRIVER_RC=0 |
| run.py | build.log | exit 0；零 FLOW OVERFLOW / HEAD TOO WIDE；TOTAL 150；P8-battery 1409.445；P8-keys 2457 |
| render.py | render.log | exit 0；印版 10,968,903 B |
| webpdf.py | webpdf.log | exit 0；网版 1,602,461 B（< 7 MB）；50,684 text bytes |
| verify.py | verify.log | exit 0；TOTAL 150；编号连续；SVG 重跑字节一致；**SOP 1.1 style audit True**；verbatim OK；P8 floor True；17 项禁词全空 |
| occlusion 审计 | `tools/occlusion_audit.py ED --json occlusion.json`（**正式审计，未带 --selftest**） | RC 0；selftest OK（6 类 planted 全触发，clean 对照静默）；**0 flags** |
| p8 extract | `tools/p8.py extract --total 150` | RC 0；**150/150**（`noted set = 150 of 150`） |
| p8 compare | `tools/p8.py compare` vs core-de | RC 0；**CLEAN**，missing=[]，extra=0，**keydiff=[137, 138, 139, 150]**（预期） |
| freeze diff | `tools/freeze.py diff` | RC 0；各页 +31/−44、+33/−31、+45/−46、+24/−21、+40/−44、+36/−32、+59/−77、+143/−137；**TOTAL added CJK = 7**（每页 1 个 U+3000，P2–P8，P1 为 0） |
| freeze_direct | `freeze_direct.py pt`（rebuild-A） | 渲染层 **8/8**：147/163/195/166/173/175/150/186，sha8 `083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7`（与 rebuild-3 一致）；源码层 **FAIL：1 条未入账** `'ist (3.ª pess. sg.)'`（见 §4，待机制层修正） |
| keycheck 150 | `keycheck.py pt` | **149/150 精确**；唯一非精确 Q150（抽取器截断，预期内，已在 keydiff 集内） |
| boxtitle 7/7 | `boxtitle.py pt`（预算 400.5px） | **7/7 fit**（356.5 / 386.0 / 378.5 / 333.9 / 386.1 / 384.8 / 388.1px） |
| measure | `measure.py pt` | RC 0；**24/24 PASS，0 FAIL** |
| 印/网文字层 | pdftotext（default + -raw） | 印版 50,684 B / 网版 50,684 B，**词多重集一致**；-raw 归一化后完全一致（各 49,500 B）；网版有真实完整文字层 |
| chips | SVG `rx="2.7"` 统计 | 每页 {1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35}，**TOTAL 141**；P8 A2 22 / B1 13 / B2 0 |
| P8 最小字号 | PyMuPDF 实测（印版+网版） | P8 最小 span **9.94pt**（349 spans，两版一致），高于 9.75pt 下限 |
| abutting | 印版 vs 网版 span 几何逐页比对（容差 0.5pt） | **无问题**；P1 最大偏差 0.22pt（'Die Lucerna'），P2–P8 均为 0.00pt |
| 网版词内字符间隙 | PyMuPDF rawdict 扫描（>0.5pt 计） | **0 处** |
| §1.1 grep | SVG 颜色/文字层扫描 + verify.py style audit | **通过**：旧式色值 `#f7f1e2/#c9a227/#d4af37/#8b6914` 计 0；文字节点含 gold/brown 计 0；fill/stroke 全部落在 §1.1 调色板内（另含 P6 图表/图片固有色 `#4f765d/#84a283/#4d72b4/#7898cd/#d7b257/#edd17f` 等，继承自核心，未动）；`·` 仅见于既有位置（选项分隔 `A. … · B. …`、术语表分隔、P1 家具行、P8 答案键分隔），与 rebuild-3 一致；verify.py SOP 1.1 style audit True |

## 6. 附注（非缺陷，复校已知项的变化）

- **T1 已随工具变化而消失（旧工具层项，非本版内容问题）：** 本次重建的网版 `pdffonts`
  含 `LucernaNewsreader-Italic` 子集（rebuild-3 时网版无 Italic）；P1 每周一词
  `« der Adventskalender »` 在网版中现为斜体跨，与印版一致；abutting P1 最大偏差由
  rebuild-3 的 9.69pt 降至 0.22pt。属当前 `tools/webpdf.py` 的行为，非 fix1 改动所致，
  供协调员知悉。
- 网版字节 +3,029 B（1,599,432 → 1,602,461），即上述 Italic 子集嵌入所致；文字层与印版一致，< 7 MB，有效交付物。
- 其余 proof1 工具层项（T2 已并入 T1 说明）与复校范围外非问题均未变；P8 字号、题量、冻结点均与 rebuild-3 一致。

## 7. 交付状态

- 未 commit、未 push（按任务指令）。重建后的成品在
  `production/2026-w47/2026-w47-de-pt/`：印版 / 网版 / text.md 三项新 SHA 见 §2。
- 待协调员：(1) 派机制层修正 tr_pt.py:243（§4），随后 freeze_direct 源码层应恢复 PASS；
  (2) 安排 fix1 后的 D1 定点重校（按 SOP §8 循环规则，修后须重校 D1 所在处）。
