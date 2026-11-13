# W47 ko 家 §8.4 状态核对报告（VERIFY-REPORT）

- 核对员：本任务 subagent（与建造者、第一/二/三轮校对员、修复工人均不同人）
- 核对时间：2026-11-13 ~05:00 UTC（Fri 2026-11-13）
- 范围：ko 家 11 版（core-ko = ko-zh-cn 版 + 2026-w47-ko-{de,en,es,fr,it,ja,nl,pt,ru,zh-tw}）
- 只读核对：未改任何生产文件，未 commit/push，未跑 lint --write，未 reset/stash
- 磁盘：96G 已用 / 54G 可用（< 100G 门限，未触发停手）
- SOP：`~/workspace/weekly-git/SOP.md` 全文已读（重点 §8 校对闭环）；`weekly-git/AGENTS.md` 已读
- 工具：`tools/venv/bin/python`（仓内共享工具）；pdftotext / pdftoppm（系统）

## 1. 最后重校记录（run-log + PROOF-NOTE-3）

ko 家最后一次全量重校为**第三轮独立重校**，工人 `2f24fef8`，产出
`hidden_files/w47/scratch-reproof3-w47-ko/PROOF-NOTE-3.md`，run-log 记于
2026-11-12 ~20:15 UTC。结论 **(a) 干净，0 发现**（R2-1/R2-2/R2-3 与 F1–F5
全部核实通过，87 门机械门禁 RC=0，按页 inventory 11 版全部 150/150）。
ko-ja 补做（D5 重建线微任务，工人 74b1c7df，2026-11-12 ~12:10 UTC 验收）
**早于**第三轮重校，已包含在第三轮重校的核对范围内。

## 2. SHA 对照表（最后重校 SHA vs 当前磁盘实测）

| 版 | text.md（字节 / SHA-12） | web PDF（字节 / SHA-12） | print PDF（字节 / SHA-12） | 对照 |
|---|---|---|---|---|
| ko-zh-cn（core-ko） | 35,456 / `044001ac2f14` | 4,226,882 / `ac97b284fe16` | 45,181,315 / `7248314a5ae2` | 一致 |
| ko-de | 36,012 / `4f6945d36115` | 3,956,937 / `4b1a54ce3040` | 43,754,319 / `8d217beb86ae` | 一致 |
| ko-en | 35,781 / `f5e5bb278704` | 3,951,102 / `59bb38b0bc77` | 43,748,448 / `f10c5065bb5b` | 一致 |
| ko-es | 36,065 / `a24bd9ffaa09` | 3,955,583 / `e1ae9fcc033b` | 43,752,821 / `637bcb1b1b22` | 一致 |
| ko-fr | 36,131 / `661b391e24d3` | 3,954,158 / `dc933cc18cfe` | 43,751,522 / `1f6add20c07d` | 一致 |
| ko-it | 36,068 / `4e7926e4ffa7` | 3,949,052 / `f0efba8a29ab` | 43,746,645 / `edfda4420e46` | 一致 |
| ko-ja | 36,275 / `be048d7d4164` | 4,373,107 / `f9bb1d3a3929` | 50,279,548 / `f8c7508f9be8` | 一致 |
| ko-nl | 35,904 / `55abafb3fee8` | 3,950,671 / `5f84566e41de` | 43,748,187 / `662eb3e3e3f2` | 一致 |
| ko-pt | 35,935 / `059743986a52` | 3,956,638 / `e4028beb886a` | 43,753,908 / `70047cd27b8d` | 一致 |
| ko-ru | 38,039 / `e439f6a60a13` | **4,047,903 / `5fc509995df1`** | **43,846,114 / `9bf5c43082b6`** | **印/网已变** |
| ko-zh-tw | 35,487 / `841a26658cb7` | 4,323,857 / `189fde45fc9e` | 45,219,886 / `65118aabee9f` | 一致 |

上表 SHA-12 与字节数均为本次磁盘实测（`sha256sum` 全值前 12 位）。
除 ko-ru 外 10 版与 PROOF-NOTE-3 指纹表逐版一致；另经 mtime 审计，
该 10 版在 2026-11-12 20:30 UTC 之后**零文件**被改动（PDF mtime
13:55–18:39 UTC，全部早于第三轮重校 20:15 UTC 的定稿态）。

ko-ru 变化原因（已查实，非未知改动）：跨家 `*-ru` 修复（fix-xru，
2026-11-12 23:53 UTC，工人 fec69813）：`svglib.py` 中 `_D5_READER == "ru"`
分支被删，拉丁文改走 Newsreader（原误走 Noto Sans CJK），西里尔文仍走
Noto Sans。重建文件集恰为 8 SVG + 8 cards PNG + 印/网 PDF + KIT +
svglib.py（mtime 审计一致，无其他文件被碰）。text.md 未变
（`e439f6a60a13`，与第三轮一致）。
重校前 SHA：印 `4c0c80b6b6bf` / 43,926,367 B；网 `ee36501822d1` / 4,126,934 B。

## 3. 逐版结论

### 3.1 VERIFIED CLEAN（10 版：SHA 与最后 CLEAN 重校一致）

core-ko（ko-zh-cn）、ko-de、ko-en、ko-es、ko-fr、ko-it、ko-ja、ko-nl、
ko-pt、ko-zh-tw。结论依据：最后重校 (a) CLEAN + 三 SHA 与磁盘逐版一致 +
mtime 审计零改动。ko-ja 的 D5 补做已含在第三轮重校内，不再单列。

### 3.2 ko-ru：SHA 已变 → 本人全新全量重校（SOP §8），结论 CLEAN，0 发现

本人作为不同校对员对 ko-ru（新印/网 SHA）从头全量重校：

**文本通读**：`2026-w47-ko-ru.text.md` 全文 947 行已读（P1–P8）。
韩文核心层与 core 一致；俄语讲解层逐项通读，拼写/性数/人称一致
（А вы? / вы 体全版统一）；R2-2 `조사하다 = обследовать` 两处在版、
`опрашивать` 0 处；R2-3 P2 band 行 `과` 式在版；F1 六道新题键
（Q12 A / Q13 A / Q22 1.8 / Q47 A / Q74 8 / Q102 A）与同页文章事实逐题
复核全对；F3/F4/F5 均在版无回归；P7 金句 8 条均逐字出自本期文章；
日期/星期逐日核验一致（11/16 周一、11/18 周三、11/19 周四、11/20 周五、
11/22 周日、11/28 周六、12/11 周五）；算术复核（199,456 vs 219,071
降 8.95%→9.0%；54,980 vs 74,800 降 26.5%；551,864 + 2,310）全对；
五场比分（8-7 / 3-2 / 5-1 / 10-5 / 12-1）跨页一致；P2/P3/P4/P8
四组配对题配对关系逐组核对全对；ABSTRACT.txt 俄语单行 500 B，
含 150 题、A2–B2 与真实主题，无 ASCII 双引号。

**印/网文本层**：pdftotext 提取逐字节一致（layout 108,229 B；
plain 59,170 B；两版均 > 0）。

**与 CLEAN 态内容同一性**：现印版 plain 文本层 vs 第三轮重校存档的
印版文本层（`scratch-reproof3-w47-ko/pdftext/2026-w47-ko-ru-print.txt`）：
非空字符多重集 **23,540 = 23,540**，差异仅 8 个空白字符
（3 空格 + 5 换行，pdftotext 抽取顺序/空白所致），**零内容字符差异**。
与 KIT fix-xru 节所载多重集门结论（23,540）一致。证实 fix-xru 只改了
字体路由，未改任何内容。

**P8 150 题**：`p8.py extract` 150/150；`p8.py compare` vs core-ko
**CLEAN**，missing=[]，extra=0，keydiff=[137, 138]（已知翻译重定向项，
与第三轮一致；P8 印版 137/138 键带“См. страницу N”注，属正常渲染）。
抽查键：Q121 A、Q125 B、Q126 A 与第三轮一致。

**机械门禁**（全部用仓内共享工具重跑，日志见 `mech/`）：
- D5 census：PASS（Latin-in-CJK 0、Cyrillic-in-CJK 0；curly 0 defective）
- 引号普查：0 defective
- 几何遮挡 `occlusion_audit.py`：**0 flags**（自检 6 类 planted 全触发）
- spill：**0 SPILL**（410 OBSERVE 均为阈值下候选，逐页目视裁定无溢出；
  与第三轮 spill 0 一致）
- boxtitle：**0 DEFECT**，0 OBSERVE，0 marginal（85 titles / 1209 body lines；
  与 01:10 UTC 扫查工人结论一致，本次为独立重跑）
- edge：8 页 **0 TOUCH，0 NEAR**
- 构建日志：fix-xru 重建 run.py rc=0 TOTAL 150，0 FLOW OVERFLOW /
  0 HEAD TOO WIDE（`scratch-fix-xru-w47/logs/ko-run.log` 核实）

**按页 inventory**（复用第三轮同款脚本 `inventory_textmd.py` /
`inventory_textmd2.py` / `inventory_match.py`，只读）：
全书 150/150、按页 150/150、配对词独立行 16/16，0 缺失。
R2-1 四块（P2 D 块 김치의 날、P4 D 块 준플레이오프/플레이오프/한국시리즈、
P8 B 块 Q121/Q126、P8 F 块 김치의 날 + P6 行标签 김장비용）逐项在版。

**8 页逐页看图**：印 PDF 经 pdftoppm 100 dpi 渲染（`pages/p-1..p-8.png`），
逐页目视：P1–P8 无溢出、无重叠、无压页脚、无豆腐块、无截断句；
页脚均为「Страница N из 8」；P8 答案键 1–150 齐全（含 150. ✓ 范文标记）。

**ko-ru 结论：(a) 干净，0 发现。** 新印/网 SHA 下的 ko-ru 达到定稿条件。

## 4. KIT §7（Output files + sizes 节）核对

逐版将 KIT “Output files + sizes” 节所载印/网/text SHA 与磁盘实测比对：

| 版 | KIT §7 与磁盘一致 |
|---|---|
| core-ko、ko-de、ko-en、ko-es、ko-fr、ko-it、ko-ja、ko-nl、ko-pt、ko-zh-tw | 是（三 SHA 各在 §7 出现 1 次） |
| **ko-ru** | **否 — 见 wave-2 清单第 1 项** |

ko-ru KIT 的 “Output files + sizes” 节（L115–117）仍载重建前 SHA
（印 `4c0c80b6b6bf` / 网 `ee36501822d1`）；新 SHA 只在 fix-xru 节
（L141–144）出现 1 次，该节并注明“this build supersedes the
‘Output files + sizes’ deliverables”。text SHA 在 §7 一致
（`e439f6a60a13`，出现 2 次：§7 + fix-xru 节）。

## 5. 待修清单（只记录，不擅自改源码）

**内容待修：无。** 11 版全部 CLEAN，0 条新发现。

**wave-2 清单（KIT 文字，不动成品）：**

1. **ko-ru KIT “Output files + sizes” 节 SHA 已过期**（KIT-only 修正，
   不重建、不重校）：印 PDF 改为 `9bf5c43082b6d4e36c8cc7c62a9507fc3ff588616f4fe3e048ae2ce5019d1c48`
   / 43,846,114 B；网 PDF 改为 `5fc509995df17bee4d98e9483a1861157efebece886c535f3a031b9131cbd2fa`
   / 4,047,903 B；text.md 不变 `e439f6a60a13d26bfdc3ac17d502cef1592063e6fe8fecf1e15c8f52109e6841`
   / 38,039 B。旧值保留备查（fix-xru 节已有新旧对照）。

## 6. 证据文件（本工作目录）

`hidden_files/w47/scratch-verify-ko/`：
- `VERIFY-REPORT.md`（本文件）
- `mech/`：p8extract / p8compare（含 JSON）、census、quotes、occl、
  spill、boxtitle、edge、inventory / inventory2 / inventory-match 日志
- `pdftext/`：print.txt / web.txt（layout）与 print-plain.txt /
  web-plain.txt（plain，逐字节一致）
- `pages/`：p-1..p-8.png（印 PDF 100 dpi 渲染，目视依据）

## 7. 总结

- 11 版逐版结论：**11/11 CLEAN**（10 版 SHA 与第三轮 CLEAN 重校一致，
  直接 VERIFIED CLEAN；ko-ru 因 fix-xru 重建改 SHA，已由本人全新全量
  重校，0 发现，CLEAN）。
- ko 家 proofread-until-zero 成立，内容定稿态未被 fix-xru 破坏。
- 唯一待办：ko-ru KIT §7 两处 SHA 的 wave-2 文字更新（上文第 5 节第 1 项），
  不阻塞内容定稿。
