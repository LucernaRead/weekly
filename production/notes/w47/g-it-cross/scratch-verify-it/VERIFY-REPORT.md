# VERIFY-REPORT — W47 it 家 §8.4 状态核对

- **核对员**：本轮独立核对员（与建造者及第 1/2/3 轮校对员、修复者均不同；只核对、不修复、不改生产文件）
- **日期**：2026-11-13（UTC 约 04:55–05:30）
- **范围**：it 家 11 版 — `core-it`（= it-zh-cn）+ `2026-w47-it-{de,en,es,fr,ja,ko,nl,pt,ru,zh-tw}`
- **磁盘**：开工/收工均为 96G 已用 / 150G（< 100G 停线）
- **方法**：只读核对生产文件；`run.py` 在 scratch 副本内重跑；机械门禁全部用仓内共享工具 + `tools/venv/bin/python`；印 PDF 8 页逐页目视
- **工作目录**：`hidden_files/w47/scratch-verify-it/`（`VERIFY-REPORT.md` 本文件；`runs/2026-w47-it-ru/` 重建副本；`logs/`；`gates/`；`pages/` 8 页 100dpi 渲染；`gates-it-ru.sh`；`freeze-baseline/`）

## 总结论

**11/11 CLEAN，零待修项。**

- 10 版：最后重校（三轮，PROOF-NOTE-3，2026-11-12 ~20:00 UTC，结论 (a) CLEAN 零问题）之后 SHA 未变，磁盘三 SHA 与重校记录逐项一致 → **VERIFIED CLEAN**。
- 1 版（it-ru）：三轮重校后 SHA 变过（fix-xru 重建 → P2 boxtitle 修复 → fix-it-ru2），本人作为不同校对员做了**全新全量重校**（SOP §8：text.md 1317 行通读、印/网文本层逐字节一致、P8 150 题逐题复核、8 页逐页看图、共享工具机械门禁）→ **CLEAN，零发现**。
- KIT §7 SHA：11 版全部与磁盘一致（完整 64 位均在 KIT 内）→ **wave-2 KIT SHA 清单为空**。
- 跨家新缺陷类复查（es 四轮发现的 text.md 两栏拼接粘连 I1/J1）：11 版 it text.md 全部扫描，**0 处粘连**，it 家不受影响。

## 1. 最后重校记录（逐版）

最后一次全量重校均为**第三轮**（`scratch-reproof3-w47-it/PROOF-NOTE-3.md`，2026-11-12 ~20:00 UTC，结论 (a) CLEAN，MAJOR 0 / MEDIUM 0 / low 0；门禁 11/11 ALL-GREEN）。此前轮次：第一轮重校 (a)（it-ko 2026-11-11 22:14 UTC，工人 3e392347）、第二轮发现 2 low（R2-1/R2-2，已由 fix2 修完并经三轮核实在版）。

| 版 | 最后重校结论 | 当时 SHA-12（印 / 网 / 文） |
|---|---|---|
| core-it | (a) CLEAN | 7b3034a08180 / 393e65473a1c / 24b37ae72af3 |
| it-de | (a) CLEAN | 8cf7241a5d60 / 13414d0fbe1b / 27f58fca0f39 |
| it-en | (a) CLEAN | aeae0796361c / e071a54f8f30 / a4d863d96180 |
| it-es | (a) CLEAN | 4393ba30bd49 / c40c7a0067bd / e19cf39d5ef6 |
| it-fr | (a) CLEAN | ffb20e7b9620 / d08db2eb54b2 / b4d1ec47ff3a |
| it-ja | (a) CLEAN | 38a236a3d0ca / e035db45098e / 3dafa38c8b40 |
| it-ko | (a) CLEAN | 66dffb4ebd5c / 7419a5a624e5 / c37668224de7 |
| it-nl | (a) CLEAN | b5a24a8f4234 / 8fc2d76c044a / 92ddd5838d6f |
| it-pt | (a) CLEAN | c4d4fe0f005e / a6e7e8365466 / 03cc7389d3ed |
| it-ru | (a) CLEAN | af296c0525ea / 597e400ffcec / 298c2cd79bb8 |
| it-zh-tw | (a) CLEAN | 3cf43a808c2a / 133b04d123f1 / 1ae5edf7b167 |

三轮重校后 it 家的改动（run-log 核实）：it-ru fix-xru 重建（印 97095d30…）、it-ru P2 boxtitle 修复（印 5281accd…）、it-ru fix-it-ru2（印 bca811b0…，2026-11-13 ~01:46 UTC）。其余 10 版三轮后无改动。

## 2. 当前磁盘 SHA-12 表（两次实测一致，开工与收工）

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） | 对照三轮 | 结论 |
|---|---|---|---|---|---|
| core-it | 14,839,776 / 7b3034a08180 | 1,546,116 / 393e65473a1c | 52,677 / 24b37ae72af3 | 一致 | VERIFIED CLEAN |
| it-de | 13,499,265 / 8cf7241a5d60 | 1,218,051 / 13414d0fbe1b | 56,634 / 27f58fca0f39 | 一致 | VERIFIED CLEAN |
| it-en | 13,496,925 / aeae0796361c | 1,215,698 / e071a54f8f30 | 55,126 / a4d863d96180 | 一致 | VERIFIED CLEAN |
| it-es | 13,497,563 / 4393ba30bd49 | 1,216,301 / c40c7a0067bd | 56,214 / e19cf39d5ef6 | 一致 | VERIFIED CLEAN |
| it-fr | 13,497,005 / ffb20e7b9620 | 1,215,747 / d08db2eb54b2 | 56,524 / b4d1ec47ff3a | 一致 | VERIFIED CLEAN |
| it-ja | 21,050,187 / 38a236a3d0ca | 1,697,338 / e035db45098e | 58,209 / 3dafa38c8b40 | 一致 | VERIFIED CLEAN |
| it-ko | 15,803,899 / 66dffb4ebd5c | 1,484,256 / 7419a5a624e5 | 57,349 / c37668224de7 | 一致 | VERIFIED CLEAN |
| it-nl | 13,495,268 / b5a24a8f4234 | 1,213,994 / 8fc2d76c044a | 55,535 / 92ddd5838d6f | 一致 | VERIFIED CLEAN |
| it-pt | 13,500,238 / c4d4fe0f005e | 1,218,997 / a6e7e8365466 | 55,736 / 03cc7389d3ed | 一致 | VERIFIED CLEAN |
| it-ru | 13,644,359 / bca811b03470 | 1,361,661 / ce75a0349c3e | 67,662 / 28e906435b1f | **变过** | 本轮全新重校 → CLEAN（见 §3） |
| it-zh-tw | 14,907,346 / 3cf43a808c2a | 1,640,999 / 133b04d123f1 | 52,588 / 1ae5edf7b167 | 一致 | VERIFIED CLEAN |

## 3. it-ru 全新全量重校（本轮，独立重校员）

### 3.1 内容通读（text.md 1317 行，全读）

- 题干 1–150 齐全、无缺重；答案区 1–150 齐全、无缺重；答案逐题与题面/原文/图表复核一致。
- 范文 99 词（实测 99，与标注一致）；Q44/Q134 均带“主语+动词+地点+日期”注；Q136 带地点注。
- 日期/星期用 `date -d`（Europe/Rome）全验：11月6日周五、7日周六、8日周日、12日周四、15日周日、16日周一、21日周六、22日周日、23日周一，全部与版面一致。
- 算术重算：P4 赛果 10 场进球 3+1+2+3+3+2+3+1+2+4=24；Q85 13−11=2；Q86 6+7=13；全部正确。
- 8 条金句逐条与 P1–P6 原文逐字一致；D-2 修正句在版（`assaggiare → assaggerò, guardare → guarderò`；`leggere, regolare al futuro: leggerò`）。
- 俄语讲解层逐项对照正文（注释词均真实出现在正文里）；意大利语题干与三轮核实的 it-en 版逐字比对：除 Q140（按设计用读者语出题：俄语 vs 英语）外，137 条题干意大利语部分逐字节一致。
- ASCII 直引号 0、U+FFFD 0、全角冒号 0；`настоящее` 0（fix-it-ru2 的删除在版）；L861 披露句为修复后 3 行版（`Пример от редакции, а не письмо. Писем и лучших сочинений нет; обещание переносится на VOL.5.`）。
- 既往修复在版：F-1 副标 `КАЖДУЮ НЕДЕЛЮ ПО-ИТАЛЬЯНСКИ`（印层 L9，`ПО - ИТАЛЬЯНСКИ` 为 pdftotext 连字符抽取 artifact，P1 渲染图目视在版）；F-2 `NOV. Scade` 印层 1 次；F-3 全角冒号 0；F-4 `LA FRASE PER RICORDARE` 在版；F-5 Q44/Q134 注完整；R-1 P8-keys 终值 2543 ≤ 2552。
- ABSTRACT.txt 已读：俄语原生、VOL.4、真实主题（拉齐奥 29 分、托罗内/ Eurochocolate 闭幕、圣母敬礼与植树日、BookCity/都灵电影节、预算案）、A2–B2、150 题。

### 3.2 机械门禁（共享工具，`tools/venv/bin/python`，生产只读）

| 门 | 结果 |
|---|---|
| run.py（scratch 副本重跑） | TOTAL 150，0 FLOW OVERFLOW；HEAD TOO WIDE 仅已接受的 1 条（P6-ex，见 §3.4） |
| SVG 重建比对 | 8/8 与生产 SVG 逐字节一致 |
| occlusion_audit.py | 0 flags（selftest 通过） |
| p8.py extract | 150/150 |
| p8.py compare vs core-it | CLEAN，missing=[] extra=0，keydiff=[137,138,139]（读者语翻译答案，预期） |
| D5 census | D5_latin_in_cjk=0，D5_cyrillic_in_cjk=0，curly_total=0，CENSUS PASS（noto_sans_elements=713 为俄语读者正文合法用 Noto Sans，三轮记为 777 的已知系统项，非缺陷） |
| boxtitle_check.py | 0 DEFECT / 0 OBSERVE / 0 marginal（34 titles，500 body lines） |
| spill_sweep.py | 0 SPILL（29 boxes，170 candidates 均为 OBSERVE——盒边邻接文字，8 页目视确认无溢入；与三轮同签名） |
| pdf_edge_scan.py | 0 TOUCH / 0 NEAR（8 页；P8 最小边距 53.6pt） |
| 印/网文本层 | 44,253 字符各，multiset_diff=0，nonws_diff=0（逐字节一致） |
| freeze.py baseline（core-it） | 8/8 byte-identical，core 完整性通过 |
| freeze.py diff vs core-it | added CJK chars=0（Latin added 145 为 fan-out 预期量，与 fix-it-ru2 记录一致） |
| head_check.py | 报告 1 条 HEAD TOO WIDE（即 §3.4 已接受项；工具按设计见一条即报 FAIL，见 §3.4 独立复核） |

### 3.3 8 页逐页目视（印 PDF，100dpi 渲染，`pages/p1-1.png` … `p8-8.png`）

P1–P8 全部干净：无溢出、无重叠、无压页脚、无豆腐块、页脚完整。重点复核页：
- P1：`LA SETTIMANA IN CIFRE В ЦИФРАХ` 盒标题在盒内；Q7–Q10 齐全。
- P2：`LA FRASE PER RICORDARE ЗАПОМНИТЕ` 盒标题在盒内（修复 #4）；练习 A–D 齐全。
- P4：`I RISULTATI DELL'11ª GIORNATA ИТОГИ 11-ГО ТУРА (6–8 ноября)` 标题在盒内（修复 #5）；赛果表 10 场齐全。
- P7：LETTERE DEI LETTORI 披露句 3 行，`VOL.5.` 基线 y=1667.92，分隔线 y=1686，净空约 13px（与 FIX-LOG 像素复核一致），无穿字；FRASI DELLA SETTIMANA 8 句齐全；LA PROSSIMA SETTIMANA 栏完整。
- P8：练习 113–150 + 答案 1–150 齐全，范文在版，页脚完整，最小字 9.75pt。

### 3.4 唯一 HEAD TOO WIDE（已接受项，独立复核）

- `run.py` 报告：`HEAD TOO WIDE [P6-ex]: D　LE PAROLE DELLA MANOVRA`。
- 独立实测（`bslib4.text_w`，与构建同一算法）：advance 446.0 vs 栏宽 422.5，超 23.5px；墨迹右缘 x=1885（SVG 实测），内容右缘 1862，超规则线约 23px，但距页边（1950）仍有 65px，且该栏为最右栏、右侧为空白边距，无碰撞、无越栏。
- P6 渲染图目视：标题完整、无碰撞、无截断。与协调员裁定（run-log 2026-11-12：接受，须记 KIT）一致。**不构成新发现，不重报为缺陷。**

## 4. KIT §7 SHA 核对（wave-2 清单）

11 版 KIT 的 §7/追加节均含当前磁盘三 SHA（完整 64 位逐项核对一致，含字节数）。**wave-2 KIT SHA 清单：空，无一处不一致。**
（it-ru KIT §19 含 fix-it-ru2 记录，新 SHA 为当前值、旧值保留为历史，正确。）

## 5. 跨家新缺陷类复查：text.md 两栏拼接粘连（I1/J1）

背景：es 家四轮重校（PROOF-NOTE-4，2026-11-12 19:00–19:30 UTC）发现 text.md 导出在两栏拼接处丢空格的新缺陷类 I1（数字粘连/句号→大写/驼峰/逗号粘连/数字→大写/目录粘连）及后续 J1（小写粘连，如 `confinal`），es 家已修复；该类为 text.md 专属、印 PDF 不受影响。
本轮对 it 家 11 版 text.md 全部扫描：
- I1 五类正则：数字粘连 0、句号→大写 0、逗号粘连 0、数字→大写 0、目录粘连（`Pag. 2…`）0；驼峰类唯一命中为品牌名 `BookCity`（18–29 次，各版均有），非粘连。
- J1 小写粘连：text.md 词 vs 8 张 SVG 词表拆分测试，11 版**可拆分候选 0**；仅剩的 text-only 词为 markdown 章节名（`Prima/Lingua/Sport/Cultura/...`），系 text.md 结构标题，非粘连。
- **结论：I1/J1 类在 it 家 11 版中 0 处，it 家不受影响。**

## 6. U+201C 说明（非发现）

U+201C 修复工人（FIX-LOG，2026-11-12 03:22 UTC）记录的 5 版新 SHA（core-it `c45fbe9f…` 等）与当前磁盘不符——其后 D5 重建重渲了 it 家各版，SHA 随之改变。当前生产 SVG 实测：5 版弯引号元素全部走 Newsreader、Noto Sans CJK 缺陷 0 处（core-it 2/2、it-de 2/2、it-en 2/2、it-nl 1/1、it-zh-tw 2/2），修复效果在版（经由 D5 路由）。三轮重校的 D5 census 同为 0 缺陷。**不构成问题，仅记此说明。**

## 7. 观察项（不计缺陷，不阻塞）

- O1（it-ru，轻微）：P5 本周计划第 1 条把活动名缩写为 «I tesori della Calabria»，全名 «I tesori della Calabria Straordinaria» 见 P1 日历。摘要列表内的缩写，事件与日期正确，非事实错误。
- O2（跨家已知，协调员已裁定本轮不修）：M1–M5（run-log 2026-11-12）。其中 M1 范文“84”标签与 83 词实测不符不适用于 it-ru（本版标注 99 词、实测 99 词）；其余为跨家措辞观察项，本轮不重报、不修。

## 8. 待修清单

**无。** 11 版全部 CLEAN；KIT SHA 全部一致；I1/J1 扫描 0 处。

## 9. 工作产物

- 本报告：`scratch-verify-it/VERIFY-REPORT.md`
- 门禁脚本：`scratch-verify-it/gates-it-ru.sh`；日志：`scratch-verify-it/logs/`（run-it-ru.log、gates-*.log、freeze-*.log）
- 门禁 JSON：`scratch-verify-it/gates/2026-w47-it-ru/`（occlusion/p8-extract/p8-compare/boxtitle/spill/edge/freeze-baseline/freeze-diff）
- 重建副本：`scratch-verify-it/runs/2026-w47-it-ru/`（8 SVG 与生产逐字节一致）；freeze 基线：`scratch-verify-it/freeze-baseline/`
- 8 页渲染：`scratch-verify-it/pages/p1-1.png` … `p8-8.png`
- 生产文件零改动：无 commit、无 push、无 lint、无 reset/stash/add。
