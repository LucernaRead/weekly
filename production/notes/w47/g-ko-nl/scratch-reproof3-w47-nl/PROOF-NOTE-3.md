# PROOF-NOTE-3 — W47 nl 家庭第三轮独立重校

- 校对员：第三轮独立重校员（与建造者、第一轮校对员、第一轮修复者、第二轮校对员、第二轮修复者均不同）
- 依据：SOP §8 / §8.4 proofread-until-zero；只校对、不修复、不重建、不 commit、不 push、不跑 lint
- 校对时间：2026-11-12 18:34–18:50 UTC 左右（门禁串行跑完 18:44:48，extras 跑完 18:50:19）
- 磁盘：开工 95G/150G，收尾 95G/150G，未触 ≥100G 停手门限
- 工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`（全程；未用系统 python3）
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof3-w47-nl/`（`mech/` 含 gates.py、run-gates.sh/out、gates-\<lang\>.log/.json、diff-core-vs-\<lang\>.txt、expl-\<lang\>.txt、run-extras.sh、extras.log、d5-census.log、boxtitle/、spill/、edge/；渲染图 pages/ 已读完即清；gates 临时 repro-* 已清）

## 总体结论：(a) 干净 — 零问题轮次

**新发现：0 条**（MAJOR 0、MEDIUM 0、low 0、trivial 0）。

- 第二轮 3 项修复全部核实在版（text.md + 印 PDF + 目视渲染三重核实，见下节）。
- 指纹 33/33 与修复记录一致；KIT 新 SHA 在版，旧 SHA 仅见于 KIT 历史修复记录行（见「附注」）。
- core-nl text.md 全文通读 + 10 版讲解层 diff 2,410 行（`>` 行）逐行读完 + P8 答案 1–150 逐题复核：无新问题。
- 机械门禁全绿：gates 10/10 `OVERALL: ALL PASS`；boxtitle 11 版 0 DEFECT；spill 11 版 0 SPILL；edge 11 版 ok（touch 0、near 0）；core occlusion 0 flags；core p8 extract 150/150；D5 census 11 版 PASS；全家 ASCII 直引号 0。
- 三处修复页目视干净（de P7、es P8、en P1 渲染图已读）。

## 发现表

无。无 MAJOR、MEDIUM、low、trivial 发现。

## 逐版结论

| 版 | 结论 |
|---|---|
| core-nl（nl-zh-cn） | 干净。text.md 431 行全文通读无新问题；P8 答案 113–150 逐题复核无误；ABSTRACT 齐全。 |
| nl-de | 干净。修复 1 在版；gates ALL PASS；目视 P7 干净。 |
| nl-en | 干净。修复 3 在版；gates ALL PASS；目视 P1 干净。 |
| nl-es | 干净。修复 2 在版；gates ALL PASS；目视 P8 干净。 |
| nl-fr | 干净。gates ALL PASS。 |
| nl-it | 干净。gates ALL PASS；boxtitle 唯一 marginal 为已知残留（见「不重报项」）。 |
| nl-ja | 干净。gates ALL PASS。 |
| nl-ko | 干净。gates ALL PASS。 |
| nl-pt | 干净。gates ALL PASS。 |
| nl-ru | 干净（内容）。gates ALL PASS；拉丁标题字体为已知跨家 D5 系统性问题，另有跨家工人统一修，不重报。 |
| nl-zh-tw | 干净。gates ALL PASS。 |

## 3 项第二轮修复核实（全部在版）

### 1. nl-de P7「besten P8-Texte」✓
- text.md L366：`Keine echten Briefe oder besten P8-Texte — Beispiel; Versprechen für VOL.5.` ✓
- 印 PDF 全文含该句（pdftotext 命中 1 次，"besten" 行后折行）。
- 目视（印 PDF P7，100 dpi 渲染）：BRIEVEN VAN LEZERS 奶油盒内三行呈现 `Keine echten Briefe oder besten / P8-Texte — Beispiel; Versprechen für / VOL.5.`，无溢出、无压线；盒下分隔线与 `Beispielbrief der Redaktion…` 正常。
- gates de：P7 token 893/893（第二轮 890/890，多 3 个 token，系新增句所致，预期内）。

### 2. nl-es Q140 `Hago un surprise` ✓
- text.md L415：`140. [B2 · Traducción] Hago un surprise con un poema corto. → ___ — Respuesta: Ik maak een surprise met een kort gedicht.（surprise: expresión fija; corto = kort） [Traducir al neerlandés]` ✓
- 旧形 `Hago una sorpresa` 全版 0 处 ✓；印 PDF 含新形、旧形 0 处 ✓。
- 目视（印 PDF P8）：Q140 题干 `Hago un surprise con un poema corto. → ___`；答案区 140. `Ik maak een surprise met een kort gedicht. – surprise: expresión fija; corto = kort`；答案区 1–150 编号齐全、无溢出。
- 附带核实：de Q140 源句为德语 `Ich mache eine Surprise mit einem kurzen Gedicht.`；pt Q140 `Faço uma surprise com um poema curto.`；fr Q140 `Je fais une surprise avec un petit poème.`（法语词形与荷兰语借词相同）——均与修复方向一致，无问题。

### 3. nl-en P1 `“Group win”` 弯引号 ✓
- text.md L45：`“Group win”: first in the group.`（弯引号）✓
- 印 PDF P1 含 `“Group win”: first in the group.` ✓；D5 census：en 弯引号总数 2，全部在 Newsreader 内 ✓。
- 目视（印 PDF P1）：HET WOORD 盒内 `“Group win”: first in the group.`，弯引号清晰；整页无重叠、无溢出。
- 全家 11 版 text.md ASCII 直引号 `"` 全部为 0 处 ✓（en 的一对为全家仅有，现已清零）。
- 另：en 印 PDF 另有一处无引号的 `Group win means finishing first in the group`（Q103 附注），无引号，正常。

## 内容重校摘要（从头全量）

- **core-nl text.md 全文通读（431 行，P1–P8）**：日期/星期经 `date -d`（Europe/Amsterdam）逐一核验（2026-11-01 周日、11-11 周三 Sint-Maarten、11-13 周五、11-14 周六、11-15 周日、11-16 周一、11-21 周六、11-22 周日、11-24 周二、11-29 周日、12-05 周六）与文中全部星期标注一致。算术复核：16 Nov→5 Dec=19 天；14→15 Nov=1 天；12:00–16:00=4 小时；2009→2026=17 年；22 Nov→5 Dec=13 天；荷兰进球 7–5（四场 1+2+2+2=7，对手 1+1+2+1=5）；图表 35+30+20+15=100、35+30=65；Eredivisie 积分与赛果一致。题号：编号行 142 条（1–150 缺 25–28 与 141–144 两组），加两组共 8 题 = 150 题 ✓；本地化答案标记 142 条 ✓；裸 `VOL.4` 行 0 ✓。范文词数按词计 81 词（PROOF-NOTE-2 的 81 正确；"NEC – PSV" 中的 en-dash 不是词）。P7 金句 8 条逐字出自本期文章且页码标注正确（P1×2、P2、P3、P4、P5、P6×2）。P8 答案 113–150 逐题复核无误。
- **10 版讲解层 diff 逐行读完**（每版 616 行 diff，241 行 `>` 行，共 2,410 行）：de、en、es、fr、it、ja、ko、pt、ru、zh-tw 全部读完。各版答案键、数字、日期、译名均与 core 一致。已核实点：ja パッケスアーフォント统一、ko 팍예스아폰트统一、zh-tw 收禮夜/主詞/受詞统一、it/pt `[B1 · Cloze]` 已本地化（Testo con lacune / Texto com lacunas 各 13 处）、ru P1 数字框完整、pt kicker/刊名本地化、it P2 标题/NOTA 盒已修。逐版答案标记数均为 142 条；编号行均为 142 条，缺的仅为分组题 25–28、141–144；非 CJK 版中文 "答案" 残留 0 处；裸 VOL.4 行 0 处。
- **引号普查**：ASCII 直引号全家 0；弯引号 “/”：core 1 对（“小组头名”）、de 1 个 “（„Gruppensieg“ 用 „…“，开引号为 U+201E）、en 1 对；«» 开引号数：各版 35–36，ru 46（即 «» 合计约 70–72，ru 92，与 PROOF-NOTE-2 一致）。
- **ABSTRACT 11 版齐全**：全部单行、无 ASCII 双引号、读者母语撰写、含刊名 + 目标语名 + A2–B2 + 150 练习 + 真实话题（Sinterklaas/Pakjesavond、Oranje 对德国、Expeditie Robinson、传统变迁）。ja 用 パッケスアーフォント、ko 用 팍예스아폰트。
- **KIT SHA 抽查**：de/es/en/fr/it 五版 KIT 含当前新 SHA（de `9032021929da…`、es `06f0e2e00aec…`、en `7e35b073ade0…`、fr `08f57ec27d86…`、it `dc91af0aa78d…`）。de/es/en KIT 内旧 SHA 各出现 1 次，均为 KIT 内历史修复记录行（D5 重建 / 第一轮修复记录）所引的旧值，非当前交付值（见「附注」）。

## 逐版门禁结果表（gates.py，10/10 ALL PASS）

每版：occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiffs=[137,138]（翻译题读者母语键，预期）；freeze 8/8；印/网文字 posdiff 0、msdiff 0（8 页）；P8 答案区最小 10.12pt；chips = core {A2:8, B1:24, B2:3}；s11_svg 干净（off-palette={}，gold/old=False，paper_fills=8）。

| 版 | OVERALL | pdftotext 印=网 (B) | P8 token（印/网） | 备注 |
|---|---|---|---|---|
| nl-de | ALL PASS | 46,678 | 2258/2258 | P7 893/893（+3，新增句，预期内） |
| nl-en | ALL PASS | 45,371 | 2324/2324 | |
| nl-es | ALL PASS | 46,703 | 2405/2405 | |
| nl-fr | ALL PASS | 46,769 | 2438/2438 | |
| nl-it | ALL PASS | 46,365 | 2347/2347 | |
| nl-ja | ALL PASS | 47,840 | 1595/1595 | |
| nl-ko | ALL PASS | 47,512 | 1636/1636 | |
| nl-pt | ALL PASS | 46,588 | 2375/2375 | |
| nl-ru | ALL PASS | 55,025 | 2194/2194 | |
| nl-zh-tw | ALL PASS | 44,242 | 1689/1689 | |

日志：`mech/gates-<lang>.log` / `.json`；串行运行记录 `mech/run-gates.out`（ALL GATES DONE 18:44:48）。

## 其余机械门禁（extras，rc=0 全绿）

- **boxtitle_check.py**（11 版）：0 DEFECT、0 OBSERVE；唯一 marginal：it P6 `DATI INVENTATI` 超出 0.6px，容差 1.0px 内（已知残留，见「不重报项」）。core 25 titles / 316 body lines；zh-tw 25/312；ja 21/333；ko 39/492；de 21/245；en 19/241；es 19/240；fr 15/247；it 25/235；pt 21/238；ru 25/300。
- **spill_sweep.py**（11 版）：0 SPILL。OBSERVE 数：core 58、de 38、en 37、es 39、fr 38、it 39、ja 67、ko 123、pt 39、ru 36、zh-tw 55（与第二轮一致）。
- **pdf_edge_scan.py**（11 版）：全部 status ok，touch 0、near 0；各页最小边距 ≥53.6pt。
- **core occlusion_audit.py**：自检 OK（6 类 planted flags 全部触发，clean 对照静默）；core-nl/svg 0 flags。
- **core p8.py extract --total 150**：noted set = 150/150（1–150 全集）。
- **D5 census**（`scratch-d5-plan/mechanism/d5_census.py`，逐版运行，日志 `mech/d5-census.log`）：11 版全部 CENSUS PASS。D5_latin_in_cjk=0、D5_cyrillic_in_cjk=0、curly_in_cjk=0、noto_sans_elements=0（ru 除外）。弯引号：core 总数 2、de 总数 1、en 总数 2，全部在 Newsreader 内；其余版 0。ru noto_sans_elements=780（该工具口径；与第一轮 338 / 第二轮 329 / 第二轮修复 census 478 的方法口径差异——后者把纯标点/数字节点也计入），属已知跨家 D5 系统性问题，不修、不重报。

## 文件指纹表（33/33 与修复记录一致）

SHA-256 前 12 位 + 字节数；印 PDF 均为 8 页。nl-de/nl-es/nl-en 三值为第二轮修复后新值；其余 8 版与 PROOF-NOTE-2 一致、未变。

| 版 | 印 PDF（SHA-12 / 字节） | 网 PDF（SHA-12 / 字节） | text.md（SHA-12 / 字节） |
|---|---|---|---|
| core-nl | `0c5d63b942d2` / 13,830,540 | `2b6f223eaff9` / 1,874,709 | `aa1f470353f9` / 44,087 |
| nl-de | `9032021929da` / 12,104,245 | `fbf0c25a503a` / 1,536,368 | `6825c35db04c` / 46,247 |
| nl-en | `7e35b073ade0` / 12,102,396 | `c7ffd6676cfa` / 1,534,493 | `e3273f300f42` / 45,136 |
| nl-es | `06f0e2e00aec` / 12,107,932 | `7025ce05d975` / 1,540,051 | `672bd4c0080c` / 47,648 |
| nl-fr | `08f57ec27d86` / 12,106,421 | `1b429a3ff61e` / 1,538,511 | `f1d1154442c4` / 47,744 |
| nl-it | `dc91af0aa78d` / 12,102,273 | `9eff96cf487a` / 1,534,364 | `e9880da2da99` / 47,194 |
| nl-ja | `b886a483f641` / 18,803,540 | `2b38c2547606` / 1,967,732 | `b7e5f5dc8b48` / 47,804 |
| nl-ko | `e7fa69a263fe` / 13,871,386 | `218aebe12b4b` / 1,791,786 | `e13db87160d1` / 47,576 |
| nl-pt | `e2fe3b3a9568` / 12,110,707 | `40c51869695b` / 1,542,854 | `67516e2163c8` / 47,365 |
| nl-ru | `bb407a7b067e` / 12,368,148 | `1c13bb4f7311` / 1,780,327 | `dd1c0c087c46` / 57,909 |
| nl-zh-tw | `3fd293bfef56` / 13,887,537 | `542c6f1bc8e2` / 1,976,266 | `bf1f627d1bbf` / 44,308 |

## 不重报项（任务明确规定）

- FIX-LOG 裁定不修项：18/19/20（正余量偏紧：pt P2 余 2.0pt、es P7 余 2.6pt、pt P6 余 2.4pt）、21（观察项）、ko 括号习惯（ko 括号前缺空格的系统性习惯）。
- 第一轮/第二轮已接受残留：core ABSTRACT 未写明 "16–22日" 周次（仅写 "11 月 16 日周一" 等具体日期，第二轮已记的观察项）；it P6 `DATI INVENTATI` 0.6px marginal（工具容差 1.0px 内，本轮 boxtitle 仍报 MARGINAL，状态未变）；ru "башмак" vs "ботинок" 同义词、ru Q139 "(88-й)"、Q140 "(surprise (фикс.))" 简略、fr Q136 缺 "+ manner"、pt Q122 保留荷兰语河名 "Maas"、it Q134 "(S + V + C + luogo)"、de Q31 "legt um 10:15 Uhr in De Omval ab" 略别扭、en "de intocht arrival"、P3 图注 "voer"、P5 全角括号、fr Q139 "L'arrivée à Amsterdam"、P4 词库跨栏断行、fr 刊名短名/全名、ru P1/P2 疑似粘连（测量假象）、es/pt P2 间隙 0.0（尾随空格假象）、CJK/俄语版碰撞扫描假象、ja P1 kicker 间隙 4.5pt、P8 keydiff 137/138（翻译题答案本就应用读者母语，非失败）。
- nl-ru 拉丁标题字体问题（已知跨家 D5 系统性问题，另有跨家工人统一修 svglib.py；本轮 nl-ru 内容照常校对，无新问题）。

## 附注

- KIT 内旧 SHA：de/es/en 三版 KIT 各含 1 处旧 SHA（de L252、es L251、en L125），均为 KIT 内历史修复记录行所引的旧值（D5 重建记录 / 第一轮修复记录），非当前交付值；当前交付值（上表）已在 KIT 内新 SHA 条目中核实。
- 本轮未发现任何须修复项；按 SOP §8.4，本轮为零问题轮次。
