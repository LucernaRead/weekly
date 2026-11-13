# 校对笔记 — 2026-W47 en-de 第二轮独立复校（叶子）

- 版：`2026-w47-en-de`（英语目标语 × 德语读者版），VOL.4，8 版，150 题
- 校对员：叶子（第二轮独立复校；与 builder、fix1、第一轮复校员不同人）
- 日期：2026-11-11（UTC 约 08:22–09:05）
- 依据：SOP §8 / §1.1 全文、`AGENTS.md`、`hidden_files/w47/briefs/brief-coordinator.md`、本版 `WEEKLY-KIT.md`、第一轮复校笔记 `scratch-proof-en-de1/PROOF-NOTE.md`、fix1 记录 `scratch-fix-en-de1/FIX-LOG.md`、`GATE-LOG.md`（后两者只作参考，全部结论本轮独立重核）
- 只检查、不改任何源码/成品；未碰 core-en、W43–W46、其他目标语家庭、tools/；未跑 insert.py、lint --write，未做任何 git 写操作（无 add/commit/push/reset/stash）。
- 路径说明：任务所给 brief 路径 `~/workspace/weekly-git/hidden_files/w47/briefs/brief-coordinator.md` 在盘上不存在，实际 brief 在 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/briefs/brief-coordinator.md`，已读该份。

## 开工探针（双通，通过）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，成功。
- 笔记目录 `hidden_files/w47/scratch-proof-en-de2/` 真实写盘成功（`.probe`，完工后已删）；`df -h`：`/home/hatch` 可用 46G，无配额问题；全程未遇 EDQUOT。

## 身份核对（先核身份，通过）

| 文件 | 字节 | SHA-256（实测完整串） | 与任务/KIT 登记 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-de.pdf` | 29,330,766 | `6f82363a63477603b9de4b7ad14967bc01d6bc68e7cbd1b961b8530b52d2d5c2` | 一致 |
| `The-Lucerna-VOL4-en-de.web.pdf`（点式命名） | 2,377,894 | `b2b686e4f9064ef4babdf02697671e5aaf73d1a87382015546d483d09b86181a` | 一致 |
| `2026-w47-en-de.text.md` | 51,948 | — | 与 KIT/fix1 一致（修前 51,989） |

两 PDF 均为 8 页、1462.5 × 2025 pt。身份相符后开工。

## 结论：(a) 零问题

本轮全量复校**零缺陷**。第一轮缺陷 D1 已修复并经本轮独立核实（见下）；其余各项全部通过。按 SOP §8.4，本版达到定稿条件。

### D1 修复核实（第一轮唯一缺陷，已修好）

- **印刷 P7**（本轮从印刷 PDF 全新渲染 110 dpi，`render/p-7.png`）目视确认：第 2 栏底部第 8 条金句以 `Senate, and for governor in 36 states.”` 结束，其下紧接 `—— From page 1 of this issue.`；第 3 栏顶部为 `THE DRILLS　Übungen`，其上无孤行。
- **网页 P7**（`render/w-7.png`）同位置一致。
- **SVG 坐标核实**（`svg/p7-lang.svg`）：8 条出处行全部 x=538.5（第 2 栏），y=1397.04 / 1503.51 / 1643.35 / 1783.19 / 1923.03 / 2096.24 / 2269.45 / **2509.40**；金句末行 y=2455.03，出处行紧跟其后。第 3 栏顶部无出处行。
- **fix1 两处改动已在成品中核实**：text.md 第 747 行 `Erklärung | Win ist Gegenwart; won ist Vergangenheit (hat schon gewonnen) — …`（无 `(gewinnt immer wieder)`），第 775 行 `Erklärung | past simple = einfache Vergangenheit; unregelmäßige Verben muss man lernen.`（无 `für Geschehenes`）；两处旧串全文扫描 0 命中。
- **fix1 副作用核查**：P7 第 1 栏底 “Irregular verbs in this issue: win → won, lose → lost, beat → beat, choose” 在第 2 栏顶续 “→ chose, run → ran.”——flow 正常分栏，无断句、无溢出，run.py 零警告，非缺陷。

## 全量复校结果（逐项，均已查）

1. **8 版印刷版逐版目视**（从印刷 PDF 用 pdftoppm 全新渲染 110 dpi，非 builder card 图）：P1–P8 均读完；无溢出、重叠、压页脚、截断、豆腐块。**8 版网页版亦逐版目视**（`render/w-1.png`～`w-8.png`）：与印刷版逐页一致，无差异。
2. **全文重读**（`2026-w47-en-de.text.md` 全文，P1–P8 正文 + 练习题面 + 150 条答案）：英文正文拼写/标点/语法无误；德语讲解层通顺正确；无英文讲解残留、无中文讲解残留；讲解层所注之词均真实出现在正文里（抽查全部 gloss 框词条与正文对照）。
3. **150 题逐题验算**：registry 150 条，字段 `n` 连续 1–150；分版 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；分级 A2 62 / B1 66 / B2 22；与 KIT 登记一致。逐题对照题面/原文/图表验算答案，全部正确（含：Q84 “33 of 35”（20+13=33，2 未公布）；Q87 254+162+19=435；匹配题字母映射逐项核对：P2 24=b/25=c/26=a/27=d；P3 38=b/39=d/40=a/41=c；P4 56=b/57=c/58=d/59=a；P5 74=d/75=a/76=b/77=c；P8 141=b/142=c/143=d/144=a）。与 core-en 比对：key 差异仅 137、138、139、140、150（预期：德语翻译键 + 写作题短标签），级别差异 0。
4. **金句 8 条逐字比对正文**：8 条全部逐字见于本期正文（脚本核对 print 提取文本，8/8 命中），出处页码全部正确（P1×2、P2、P3、P4、P5、P6×2）。
5. **禁词扫描**：提取文本扫描 `W47 / 2026-w47 / 2026-W47 / cover / SOP / proofread / TODO / Lorem / placeholder / en-de / zh-cn / XXXX / TBD`，零命中。内部结构标记（周次、语言代码、仓库链接、“cover”、内部流程词）无。
6. **VOL.4**：P1 刊头 VOL.4；全部 8 页页脚 `Seite {n} von 8` + `ENGLISH WEEKLY VOL.4`（逐页核实 1–8）；提取文本计数 VOL.4 ×12、VOL.5 ×8、VOL.3 ×3，与 proof1/fix1 一致；VOL.5 8 处均为合法下期预告，VOL.3 3 处与 core 一致（“VOL.3 promised real letters…”）；无错印 VOL 号。
7. **徽章逐页计数**：SVG 徽章矩形（60×30，rx=2.7，A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f`）逐页计数，与 core 逐页完全一致：P1 16、P2 15、P3 16、P4 16、P5 16、P6 19、P7 13、P8 23。
8. **P8 最小字号**：`svg/p8-test.svg` 全部 font-size 集合最小值 13.5pt ≥ 9.75pt（SOP §1.1 底线），无需让步。
9. **日期/星期**：全部日期逐个用 `date -d` 核验：11月3日周二、11月8日周日、11月9日周一、11月10日周二、11月16日周一、11月18日周三、11月19日周四、11月20日周五、11月21日周六、11月22日周日、11月26日周四、11月27日周五、12月1日周二，全部与正文一致。佐治亚决胜轮 12月1日（投票后 4 周）正确。
10. **事实**：沿用 proof1 已核实的公开来源结论（密西西比常规选举无决胜轮；Rousseau《Surprised!》1891 年；人名拼写 Joseph Zada / Ralph Fiennes / Suzanne Collins / Henri Rousseau 等），本轮重读全文未发现与之矛盾的新表述；P8 注文人名逐项与 P3/P8 正文一致，无拼错。
11. **翻译层专项（fan-out 特有）**：讲解/界面语言确为德文；freeze diff 新增 CJK 仅 9 个，全部为 U+3000 表意空格（家具分隔符）；可见文本零真实 CJK 字符；唯一 CJK 字符是 P1 非可见 SVG `<title>Lucerna 三色蛾</title>`（与 core 共有，非可见文字）。E 组中文句答案键已译成德文（137–140 译文准确）；150 为开放题短标签（与 core 短标签模式一致）。
12. **U+2019 缺陷类回归**：8 个 SVG 全扫：U+2019 总数 **0**（逐文件均为 0）。目视抽查含撇号的行（P1 “president's four-year term”、P4 “Cummins's place”、P5 “Friday's Words” 等）：无宽字形、无断裂间隙，ASCII 撇号渲染正常。
13. **ABSTRACT.txt**：628 字节，德文单行，零 ASCII 双引号；含刊名、目标语名、A2–B2、题数与本期真实主题词。
14. **text.md**：51,948 字节，与 KIT/fix1 一致；内容与新 PDF 一致（仅两行 fix1 gloss 差异，见上）。

## 机械门全套自跑（结果见 GATE-LOG.md）

- occlusion（tools/venv）：selftest OK，**0 flags**。
- p8 extract：noted set 60/150，与 core 集合相同。
- p8 compare：**CLEAN**，missing=[]、extra_count=0、uncertain=[]；keydiff=[137, 138, 139, 140, 150]，均为预期内（德语翻译键 + 写作题短标签；W46 en-de 同样 keydiff）。
- freeze：瘦复制重跑 + 直接 sha256 比对再生 SVG 与送审 SVG **8/8 MATCH**（run.py exit 0，零 OVERFLOW / TOO WIDE，TOTAL 150，MODEL 82；重跑在笔记目录内进行，未碰送审目录）；freeze diff：新增 CJK 仅 9 个 U+3000。
- print/web 文字层：pdftotext 各 48,018 字节，**逐字节相同**（`cmp` 通过），token 多重集差 0/0；web PDF 2,377,894 字节 < 7 MB。
- P7 坐标 + 双版目视：D1 已修（见上）。

## 观察项（单独列，不计缺陷；与 proof1 的 8 条一致，均未变）

1. **P2 A 组说明 “Ergänze die Sätze nach Datum und Uhrzeit.”**：本周 5 道题全部是日期、无钟点题；“und Uhrzeit”用词偏宽。但这是 core 中文说明 “根据日期与时间” 的忠实翻译，且 W46 en-de 同款写法——属模板通用措辞，非本版新错。
2. **ABSTRACT.txt 两处措辞偏松**（正文无误，仅摘要）：(a) “Die geprüften Ergebnisse der US-Zwischenwahl”——“geprüft”易与“认证结果”混淆，而正文反复强调 AP call 不是认证结果（认证期 11月10日–12月18日，摘要后半句亦写明）；(b) “am Samstag, 21. November, … das ATP-Finale in Turin”——ATP 决赛在周日 11月22日，周六是半决赛；正文 P4/P6 写法正确。
3. **引号方向**：德文引文用 «…»（法式/瑞士式）；标准德语常用 »…« 或 „…“。全版一致，非错（瑞士德语即用 «»）。
4. **“Anmerkung | Erklärung |” 双前缀**：P2/P3/P4/P5/P6/P7 的 Erklärung 框均有双前缀——KIT 已记为已确认的 W46 惯例，本轮核实为有意保留，非缺陷。
5. **P8 印刷答案注为节选**：150 条 registry 注中 83 条未印在 P8 答案区（只印键或短注）；core 同模式，属模板惯例，非缺失；键本身 150/150 齐全。
6. **版面留白**：P3 第 3 栏止于 1619、P4 第 3 栏止于 1713、P5 第 2 栏止于 597、P6 第 3 栏止于 1256——与 core 相同的模板 flow 行为，KIT 已记。
7. **P1-countries flow 余量仅 2pt**（2298/2300）：在底线内，无溢出；仅记一笔。
8. **freeze.py baseline 未能按原样跑**：整树复制涉磁盘配额风险，沿用 proof1/fix1 的等效做法（同一 tools/venv 解释器、同一构建源码的瘦复制 9.8M，在笔记目录内重跑，不碰送审目录）并逐字节比对，8/8 一致。详见 GATE-LOG.md。

## 未核查项

- 无。本任务清单内各项均已核查（身份、8 版印刷目视、8 版网页目视、全文重读、150 题、8 金句、禁词、VOL、徽章、P8 字号、日期/星期、翻译层、U+2019、P8 人名、全部机械门、print/web 一致、run.py 重跑、D1 修复核实）。
