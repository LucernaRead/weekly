# PROOF-NOTE-5 — W47 es 家庭第五轮独立重校

- **轮次**：第五轮独立重校（SOP §8/§8.4；校对员与建造者及第一/二/三/四轮校对员、修复者均不同；只校对、不修复）
- **日期**：2026-11-12（UTC 19:40–20:06 前后；门禁 GATES DONE 20:05:56）
- **范围**：`production/2026-w47/` es 家庭 11 版：core-es（= es-zh-cn）+ `2026-w47-es-{de,en,fr,it,ja,ko,nl,pt,ru,zh-tw}`
- **结论：(b) 有问题 — 1 条 low 新发现（J1，I1 同类残留，13 处），无 MAJOR，无 MEDIUM。**
- **核实重点结论**：I1 修复 312/312 在版，多修 49 处逐条印层复核全部正确、无一误修；H1、G1/G2/G3、F2/F3/F4 全部在版、无回归；排除项未被误改；core/ja/ko/zh-tw 4 版本轮干净。

## §1 指纹 — 33/33 与 FIX-LOG-4 §7 / PROOF-NOTE-4 §1 一致

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| core-es | 4,317,615 / `6089c0fa5420` | 1,162,042 / `f0f6ed1de57a` | 43,789 / `9cc6462f702c` |
| es-de | 2,916,396 / `3fdc2ce60e6a` | 806,895 / `fd7edd4b8415` | 45,369 / `92013d149576` |
| es-en | 2,915,635 / `a7d5aba8bd0f` | 806,124 / `bb690dd25b6c` | 45,044 / `dd34d3a3cd48` |
| es-fr | 2,914,957 / `fd0e9f83a989` | 805,426 / `960de8cf8d3b` | 45,831 / `0086ceee4c72` |
| es-it | 2,913,352 / `0cffc84e47c0` | 803,822 / `f533bb1aa133` | 45,209 / `f9d0cf98767b` |
| es-ja | 8,530,586 / `cbb3efedd9a2` | 1,280,143 / `70d46e27721f` | 46,578 / `bab03d4d6c8a` |
| es-ko | 5,229,281 / `e2ae545b1462` | 1,097,497 / `fad91509e34f` | 47,403 / `8407be401bb7` |
| es-nl | 2,915,320 / `c716ce60992a` | 805,809 / `8be3118b5080` | 45,341 / `2afcdcf2c309` |
| es-pt | 2,914,243 / `ce89b874dfc0` | 804,705 / `06514f66f69d` | 45,574 / `7c7ad36c3eb9` |
| es-ru | 3,213,297 / `538ca756749a` | 1,061,847 / `8d440e9b52cf` | 52,365 / `6f89a108c8fd` |
| es-zh-tw | 4,381,575 / `fd3e65ef1840` | 1,265,861 / `8871073245fd` | 43,818 / `d26fdddc0fa6` |

- 完整 33 个 SHA-12 见工作目录 `fingerprints.txt`（逐项核对，全部命中）。
- 11 版 text.md 新 SHA 与 FIX-LOG-4 §7 逐字符一致；11 版印/网 PDF 与 PROOF-NOTE-4 §1 一致、未动。
- 11 版网 PDF 均 < 7 MB 且带文字层（PyMuPDF 抽取，印/网均为 8 页、文字逐字节相同）。
- 11 版 KIT 均含新 text.md SHA（各 2 处：现行行 + I1 小节）与「第四轮独立重校修复 I1」小节（各 1 处）。

## §2 I1 修复核实 — 312/312 在版，多修 49 处全部正确

- **逐条复核**（`fix-report.json` 的 312 条 `applied`，逐版对照盘上 text.md）：旧串全文件计数 **0/312**，新串全部在位且在记录行号上 **312/312**（`verify312.json`）。
- **印层复核**（逐条对照第四轮印 PDF 文字层 `scratch-reproof4-w47-es/txt/*-print.txt`，空白归一化）：300 处新串在印层连续出现；其余 12 处适用 FIX-LOG-4 §4 的或准则（`题号. 后续文字` 在印层连续出现），逐条验过——
  - `los dos 141.` ×4（de L1540、en L1539、fr L1546、pt L1545）：印层均有 `141. el sondeo`，旧串 0；
  - 答案 67/68/69/71 ×8（de L1774/1776/1777/1779、nl L1803/1808/1810/1812）：印层均有 `67. C — …`、`68. B — …`、`69. A — …`、`71. papeleta — …` 全句，旧串 0。
  - 其余多修项（`mezclada Según` ×7、`MiDNI · El` ×7、`) C` ×8、`C. la campaña` ×7、`21h30 128.` / `12h00 71.`）均在 300 处严格通过之列。
- **结论：多修 49 处判断全部正确，无一误修，无发现。**FIX-LOG-4 §3 对漏计原因的说明（P8 题目区 4 处 + RESPUESTAS 末尾 67/68/69/71）与盘上实测一致。
- **残留重扫**（9 类模式 + 补充模式，全家）：目录/逗号/句号→大写/句号→小写/驼峰（非品牌）/数字粘连/中点/右括号/`,[A-Z]`/`;[A-Za-z]`/`»[A-Za-z]`/`[A-Za-z]«`/西里尔数字粘连 均为 **0**；数字→大写残留仅 `29N`（排除项，见 §6）。英序数 `19th/13th/27th/28th`（en 9 处）、法序数 `13e/5e`（fr 7 处）、葡/法时刻 `21h30/12h00/18h30/14h00`（pt 7 处）均完好。

## §3 发现

### J1 — low — text.md 专属：小写词与小写词拼接粘连（I1 同类残留，第四轮与修复轮均漏检）

**性质**：与 I1 同一缺陷类（两栏拼接丢空格），但发生在两个**小写词**之间，故第四轮的 9 类模式扫描与修复轮的重扫均未覆盖（其模式只抓数字/大写/句号/逗号/中点/右括号）。内容全部在场、顺序正确；**印刷 PDF 在全部 13 处均为干净**（见下）。与 I1/G3 同级 low。

**（a）`confinal`（`con` + `final`）×7**—— P6 Q88 选项 C 尾 `con` 与 Q92 选项 A 尾 `final` 拼接：

| 版 | 行号 | 行内实测 |
|---|---|---|
| es-de | L1150 | `· C. solo datos oficiales, confinal · B. una foto con margen de error · C. una Kasten: …` |
| es-en | L1150 | `· C. solo datos oficiales, confinal · B. una foto con margen de error · C. unasondeo · …` |
| es-fr | L1154 | 同上（`C. unasondeo`） |
| es-it | L1152 | 同上（`C. unasondeo`） |
| es-nl | L1170 | `· C. solo datos oficiales, confinal · B. una foto con margen de error · C. una· indecisos · …` |
| es-pt | L1154 | 同上（`C. unamuestra`） |
| es-ru | L1201 | 同上（`C. unamuestra`） |

**（b）`unasondeo`（`una` + `sondeo`）×3**—— P6 Q92 选项 C 首词 `una` 与 D 框首词 `sondeo` 拼接：en L1150、fr L1154、it L1152（与 (a) 同行）。

**（c）`unamuestra`（`una` + `muestra`）×2**—— 同上，D 框次词 `muestra`：pt L1154、ru L1201（与 (a) 同行）。

**（d）`Esjueves`（`Es` + `jueves`）×1**—— P8 答案区：fr L1756 `101. Es — Pour 1 heure, on emploie le singulier Esjueves 19`（答案 101 注释尾 `Es` 与答案 139 残片 `jueves 19` 拼接；其相邻行 L1761 的 `Son140.` 已在第四轮修复中修好）。

**印层干净证据**：7 版印 txt 中 `confinal` / `unasondeo` / `unamuestra` 各为 **0**；fr 印 txt 中 `Esjueves` 为 **0**，而 `jueves 19` ×21、`singulier Es` ×1 均在版。源头（`core-es/content56.py:210`）Q88 C 全文为 `solo datos oficiales, con fuente`，Q92 A 为 `un resultado final`，Q92 C 为 `una promesa`——印版 SVG 词序与源头一致。

**13 处均系修复前已存在**：逐条核对修复前备份 `scratch-fix4-w47-es/text-pre-*.md`，`confinal` 7 版各 1、`unasondeo` 3 版各 1、`unamuestra` 2 版各 1、`Esjueves` fr 1，全部在备份中——非修复引入，是第四轮表列与修复轮扫描共同漏计。

**严重度 low**：与 I1/G3 同级——text.md 专属、内容齐全有序、印刷报纸不受影响；但网站正文在 P6 练习区 visibly garbled（如 `confinal`、`unasondeo`）。

**修复建议**：按 I1 同款手术式修复（拼接处插 1 空格：`con final`、`una sondeo`、`una muestra`、`Es jueves 19`）；注：两片分属不同题/框（`con` 属 Q88 C、其续 `fuente` 在孤行；`final` 属 Q92 A；`una` 属 Q92 C、其续 `promesa` 在孤行），插空格后的断句与 312 处已接受修复（如 `los dos 141.`）同一惯例。**根治建议**：导出器修好栏间拼接后，须补一类扫描——text.md 词表对印层词表的差集（本轮即以此法发现 J1：拉丁词 len≥2 全家仅剩这 4 个粘连词 + 语言代码 artifact），否则小写粘连仍会漏网。

## §4 H1 核实 — 在版，无回归

- es-ru text.md L147 = `AHORA TÚ　Теперь вы`（全角空格 U+3000）；词边界正则 `\bты\b` = **0**；`Теперь ты` 0；`Теперь вы` 1；`А вы?` ×4；共 1889 行。
- 印 PDF 文字层：P1 `Теперь вы` 1、`Теперь ты` 0；全册 `А вы?` ×4、`Теперь вы` ×1、`Теперь ты` 0。
- 目视：ru P1 渲染图（100 dpi，读后已删），`AHORA TÚ　Теперь вы` 在 LA SEMANA EN CIFRAS 栏下清晰在版，版面无重叠。

## §5 G1/G2/G3、F2/F3/F4 核实 — 全部在版，无回归

- **G1**（es-ja）：text.md「世界遺産」0，「無形文化遺産」1，L1772 `30. Verdadero — ユネスコが2010年にフラメンコを無形文化遺産に登録`。
- **G2**（es-pt）：text.md `você` 0，`Agora tu` 1，`E tu?` 4。
- **G3**（es-ru text.md）：L300 `пришлите их в редакцию.`（在位）；L327 `nunca «en las 21:00».`（在位）；L208 一带为 `La semana, día a día: del`，无孤儿句；DECIR 标题 L321，尾句在其后 6 行内。
- **F2**（P6 时间线措辞）：11 版 text.md `sin el PSOE confirmado` 各 ×1，旧措辞 `sin el PSOE).` 各 0。
- **F3**（P1 刊头顶行，PyMuPDF 框，日期 x0 固定 1039.4pt）：fr 副标右端 974.1pt，间隙 **65.3pt**；it 970.7pt，间隙 **68.7pt**；de `LIEST` x1=1035.0pt，间隙 **4.4pt**（一尾随空格 span 止于 1039.4，计入会误算为 0.0；真间隙 4.4pt，两词分明——与前四轮已接受结论一致）。11 版印 PDF 全文 `ESPAGNOLSSEMANA` / `SPAGNOLISEMANA` 各 0，均为 8 页。
- **F4**（es-ru P2 DECIR）：标题 y0=877.7pt；末行 `nunca «en las 21:00».` 位于 (403.9, 1052.9)，同栏、紧贴段后——与第二/三/四轮数值相同。

## §6 排除项未被误改

- `29N`：11 版各 2 处（印层亦作 `29N`，有意缩写）。
- 品牌驼峰：`laSexta` 11 版各 9 处、`MiDNI` 各 8 处、`LaLiga` 各 1 处，与修复前一致。
- 德/荷长词真实存在（`Wahlkampfveranstaltung`、`verkiezingscommissie` 等）；CJK 全角括号前无空格为全家体例（core/ja/zh-tw ` digit+（` 各 6–7 处，ko `digit+(` 7 处）。
- 数字→小写扫描：en 序数 `19th/13th/27th/28th`、pt 时刻 `18h30/21h30/14h00/12h00` 均为合法，无新粘连。

## §7 机械门禁 — 11 版全绿（`gates_all5.sh`，自第四轮脚本仅换路径；`GATES DONE 20:05:56`，87 条 rc=0，0 条非零）

| 版 | freeze 8/8 | occlusion | p8 extract 150/150 | p8 compare | boxtitle（标题/正文行/DEFECT/OBSERVE/marginal） | spill | edge（JSON 合计，8 页） | D5 census（弯引号 in Newsreader） |
|---|---|---|---|---|---|---|---|---|
| core-es | ✓ | 0 | ✓ | —（基准） | 30 / 330 / 0 / 0 / 0 | 0 SPILL，85 OBSERVE | 0 TOUCH / 0 NEAR | 10/10 PASS |
| es-de | ✓ | 0 | ✓ | CLEAN，keydiff [137,138] | 24 / 264 / 0 / 0 / **1** | 0 / 67 | 0 / 0 | 3/3 PASS |
| es-en | ✓ | 0 | ✓ | CLEAN，keydiff [137,138] | 26 / 261 / 0 / 0 / 0 | 0 / 70 | 0 / 0 | 6/6 PASS |
| es-fr | ✓ | 0 | ✓ | CLEAN，keydiff [137,138] | 24 / 269 / 0 / 0 / 0 | 0 / 71 | 0 / 0 | 0/0 PASS |
| es-it | ✓ | 0 | ✓ | CLEAN，keydiff [137,138] | 22 / 266 / 0 / 0 / 0 | 0 / 71 | 0 / 0 | 0/0 PASS |
| es-ja | ✓ | 0 | ✓ | CLEAN，keydiff [137,138] | 26 / 346 / 0 / 0 / 0 | 0 / 84 | 0 / 0 | 0/0 PASS |
| es-ko | ✓ | 0 | ✓ | CLEAN，keydiff [137,138] | 38 / 604 / 0 / 0 / 0 | 0 / 149 | 0 / 0 | 4/4 PASS |
| es-nl | ✓ | 0 | ✓ | CLEAN，keydiff [137,138] | 26 / 264 / 0 / 0 / 0 | 0 / 71 | 0 / 0 | 4/4 PASS |
| es-pt | ✓ | 0 | ✓ | CLEAN，keydiff [137,138] | 24 / 266 / 0 / 0 / 0 | 0 / 69 | 0 / 0 | 0/0 PASS |
| es-ru | ✓ | 0 | ✓ | CLEAN，keydiff [137,138] | 30 / 372 / 0 / 0 / 0 | 0 / 72 | 0 / 0 | 0/0 PASS |
| es-zh-tw | ✓ | 0 | ✓ | CLEAN，keydiff [137,138] | 26 / 328 / 0 / 0 / 0 | 0 / 82 | 0 / 0 | 0/0 PASS |

- 注：edge 日志行 `1 touch/near-lines` 为已知计数 artifact（汇总行自身含关键词）；JSON 为真凭：11 版 8 页合计均为 0 TOUCH / 0 NEAR（status ok）。
- de boxtitle 1 marginal（+0.7px）在容差内，第四轮一致，已接受。
- spill OBSERVE 数与第四轮逐版相同（core 85、de 67、en 70、fr 71、it 71、ja 84、ko 149、nl 71、pt 69、ru 72、zh-tw 82），均为已知词框注记位置，非溢出。
- p8 keydiff [137,138] 为翻译题设计差异（与 core 不同），10 版一致。

## §8 已核查非发现（不重报，仅记已查）

- **F1 首字母下沉**：FIX-LOG 裁定不修，不重报。
- **\*-ru 拉丁标题字体**（Noto Sans vs Newsreader）：已知跨家 D5 系统性问题，另有工人统一修 svglib.py，不重报。
- **es text.md 页内顺序打散**：跨家审计已裁定延期至 W47 后修导出器，本轮不重报。本轮仅记一处与之相关的核查：P6 Q88 C 尾 `fuente` 与 Q92 C 尾 `promesa` 在 text.md 中为孤行（L1152–1154 一带），源头与印版 SVG 词序正确——属已知顺序问题，无新内容缺失。
- **PROOF-NOTE-4 §5 记录更正沿用**：其文 "text.md U+201C/U+201D 各 0 次" 与事实不符一事，第四轮已记；本轮 census 与之相符，无变化。
- **en 答案 88 注释偏短**（`88. C — Only the published free-airtime figures`，未写「选管会公布、注明来源」；de/fr/it/ja/ko/nl/pt/ru 均写全）：注释为简析而非答案本身，字母 C 正确、事实无矛盾，第四轮已读过同一文本——不作发现，仅记。
- **pt P1 顶行副标、ko P1 词框 `"토론"`、ja "正誤"、nl `aantonende wijs`、ja/ko 国民党/국민당 = PP、"Cinco claves" 半译、pt #149 `A que horas fecha?`、P5 MiDNI 暂停解除 5 Nov**：与第四轮 §6 一致，本轮全部复核，无变化。
- **第四轮 §6 其余已接受项**：本轮全部复核，无变化。

## §9 逐版结论

| 版 | H1/G1–G3/F2–F4 | I1 修复 312 处 | J1 新发现 | 门禁 | 结论 |
|---|---|---|---|---|---|
| core-es | —（基准版；F2 在版） | 7/7 在版 | 0 | 全绿 | **干净** |
| es-de | F2/F3 在版 | 47/47 在版 | 1（`confinal`） | 全绿（boxtitle 1 marginal 已接受） | **有问题（low，J1）** |
| es-en | F2 在版 | 50/50 在版 | 2（`confinal`、`unasondeo`） | 全绿 | **有问题（low，J1）** |
| es-fr | F2/F3 在版 | 41/41 在版 | 3（`confinal`、`unasondeo`、`Esjueves`） | 全绿 | **有问题（low，J1）** |
| es-it | F2/F3 在版 | 39/39 在版 | 2（`confinal`、`unasondeo`） | 全绿 | **有问题（low，J1）** |
| es-ja | G1 在版 | 7/7 在版 | 0 | 全绿 | **干净** |
| es-ko | F2 在版 | 7/7 在版 | 0 | 全绿 | **干净** |
| es-nl | F2 在版 | 46/46 在版 | 1（`confinal`） | 全绿 | **有问题（low，J1）** |
| es-pt | G2 在版 | 43/43 在版 | 2（`confinal`、`unamuestra`） | 全绿 | **有问题（low，J1）** |
| es-ru | H1/G3/F2/F4 在版 | 18/18 在版 | 2（`confinal`、`unamuestra`） | 全绿 | **有问题（low，J1）** |
| es-zh-tw | F2 在版 | 7/7 在版 | 0 | 全绿 | **干净** |

## §10 工作记录

- **全文通读**：core-es text.md 1803 行全文；10 版讲解层 plus-diff 逐行读完（plain `diff` 的 `>` 行，行数与第四轮相同：de 599、en 643、fr 664、it 603、ja 507、ko 528、nl 710、pt 614、ru 760、zh-tw 322，共 5,950 行）。
- **P8 答案 1–150**：11 版 text.md 全数在场（逐号正则核查，无缺号）；门禁 p8-extract 150/150、compare CLEAN（keydiff [137,138] 设计差异）。
- **日期/星期/算术**：`date -d` 核 13 Nov 2026 Fri、16 Mon、17 Tue、18 Wed、19 Thu、20 Fri、21 Sat、22 Sun、23 Mon、24 Tue、25 Wed、26 Thu、27 Fri、28 Sat、29 Sun，全部与报纸一致；"Faltan 13 días"（29−16=13 ✓）；RTVE 民调 45+45+30+30+15+3×10=**195** ✓；45−30=**15** ✓；民调禁令 24–28 = **5 天** ✓；竞选 13–27 = 15 天 ✓。
- **引文**：8 条 FRASES DE LA SEMANA 逐条核对——源头 `content7.py` 逐字一致，且在 text.md 中按词序全数在场（栏间交错致跨度拉长，属已知顺序问题）；页码标注 Página 1/4/2/5/3/6/3/6 与正文一致。作文模范文 #150 手数 **97 词**，与宣称一致（源头 `content8.py` 模型文本去引号连接符后计 97 词）。
- **欧冠/西甲**：第四轮已自公开来源核实，本轮未重查；文本与第四轮逐字相同（指纹一致）。
- **ABSTRACT**：11 版全部读过，均为读者母语，事实与正文一致（13 Nov 辩论、29 Nov 大选、邮寄截止 19 日、弗拉门戈 16 日、圣塞西莉亚 22 日、西甲第 13 轮、欧冠）；单行、无 ASCII 双引号；zh-tw 简体独有字 0（全文亦 0，繁体字在版：說/讀/請/語/見/與/間/還）；非 CJK 版 CJK 字 0（ja 汉字为日文汉字，ko 0）；core 全文繁体独有字 0。
- **目视抽查**（100 dpi 渲染，读后即删）：ru P1（H1 `AHORA TÚ　Теперь вы` 在版，版面干净）。
- **只读**：未修复、未重建、未 commit、未 push、未跑 lint、未改 SOP、未碰其他家庭/其他周。工具解释器 `~/workspace/weekly-git/tools/venv/bin/python`。
- **磁盘**：开始 95G 已用 / 55G 空闲（150G 盘），结束 95G，未触发 ≥100G 门限。渲染图 1 张已删除；工作目录 1.5M，仅留日志、指纹、diff、核查脚本输出。
- **建议下一步**：修复 J1（13 处，text.md 专属手术式修复，见 §3），随后按 SOP §8.4 对被碰 7 版做新一轮独立重校；导出器根治时补词表差集扫描（见 §3）。
