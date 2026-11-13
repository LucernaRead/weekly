# PROOF-NOTE-4 — W47 es 家庭第四轮独立重校

- **轮次**：第四轮独立重校（SOP §8/§8.4；校对员与建造者及第一/二/三轮校对员、修复者均不同；只校对、不修复）
- **日期**：2026-11-12（UTC 19:00–19:30 前后；门禁 GATES DONE 19:22:41）
- **范围**：`production/2026-w47/` es 家庭 11 版：core-es（= es-zh-cn）+ `2026-w47-es-{de,en,fr,it,ja,ko,nl,pt,ru,zh-tw}`
- **结论：(b) 有问题 — 1 条 low 发现（I1），无 MAJOR，无 MEDIUM。**
- **核实重点结论**：H1 修复在版（es-ru P1 `Теперь вы`，独立词 ты 为 0，`А вы?` ×4）；G1/G2/G3、F2/F3/F4 全部在版、无回归；其余 10 版指纹与 PROOF-NOTE-3 一致，未被碰。

## §1 指纹 — 33/33 与 FIX-LOG-3 / PROOF-NOTE-3 一致

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| core-es | 4,317,615 / `6089c0fa5420` | 1,162,042 / `f0f6ed1de57a` | 43,782 / `e537146d733d` |
| es-de | （与 PROOF-NOTE-3 一致） | （同左） | （同左） |
| es-en | （与 PROOF-NOTE-3 一致） | （同左） | （同左） |
| es-fr | （与 PROOF-NOTE-3 一致） | （同左） | （同左） |
| es-it | （与 PROOF-NOTE-3 一致） | （同左） | （同左） |
| es-ja | 8,530,586 / `cbb3efedd9a2` | 1,280,143 / `70d46e27721f` | 46,571 / `29961f6fbc19` |
| es-ko | （与 PROOF-NOTE-3 一致） | （同左） | （同左） |
| es-nl | （与 PROOF-NOTE-3 一致） | （同左） | （同左） |
| es-pt | 2,914,243 / `ce89b874dfc0` | 804,705 / `06514f66f69d` | 45,531 / `e308de125b8a` |
| es-ru | **3,213,297 / `538ca756749a`** | **1,061,847 / `8d440e9b52cf`** | **52,347 / `ee9b53f788c8`** |
| es-zh-tw | （与 PROOF-NOTE-3 一致） | （同左） | （同左） |

- 完整 33 个 SHA-12 见工作目录 `fingerprints.txt`（逐项核对，全部命中）。
- es-ru 三值与 FIX-LOG-3 修复后新值逐字符一致；其余 10 版与 PROOF-NOTE-3 §1 一致。es-ru KIT（`WEEKLY-KIT.md`）亦含新 SHA（印 `538ca756749a`、text `ee9b53f788c8` 各 1 处）。
- 11 版网 PDF 均 < 7 MB 且带文字层（`pdftotext -layout` 抽取，印/网均为 8 页、文字逐字节相同）。

## §2 发现

### I1 — low — text.md 专属：两栏拼接处丢空格/换行，文字粘连（新缺陷类）

**性质**：网站正文导出（text.md）在两栏/两块拼接处丢掉空格或换行，相邻两段文字粘成一串。内容全部在场、顺序正确；**印刷 PDF 在全部抽查点均为干净**（见下）。与 G3 同类（text.md 专属）、同级 low。

**（a）分版粘连（7 版，合计 186 处）**—— core/ja/ko/zh-tw 为 0：

| 版 | 数字粘连（答案区，如 `midnight39.`、`Nairobi77.`、`Infinitiv113.`） | 句号→大写（`correo.Este`、`B.B1`） | 非品牌驼峰（`elEs posible`、`a lasEs`、de 另有 `unaKasten`） | 逗号粘连（`5,titular`） | 数字→大写（`9B1`、`15Un`） | **小计** |
|---|---|---|---|---|---|---|
| es-de | 23 | 2 | 3 | 1 | 2 | **31** |
| es-en | 30 | 2 | 2 | 1 | 2 | **37** |
| es-fr | 21 | 2 | 2 | 1 | 2 | **28** |
| es-it | 20 | 2 | 2 | 1 | 2 | **27** |
| es-nl | 22 | 2 | 2 | 1 | 2 | **29** |
| es-pt | 20 | 2 | 2 | 1 | 2 | **27** |
| es-ru | 0 | 2 | 2 | 1 | 2 | **7** |
| core / ja / ko / zh-tw | 0 | 0 | 0 | 0 | 0 | **0** |

**位置（各版相对位置相同，行号以 de/en 为例，其余见下表）**：

| 位置 | 样本 | 行号（de / en / fr / it / nl / pt / ru） |
|---|---|---|
| P1 BREVES 图注 | `…el 29 de noviembre España decide. En la página 5,titular. En la página 6…` | 163 / 167 / 172 / 172 / 167 / 167 / 169 |
| P5 练习 Q75+Q68 | `…del voto por correo.Este año se puede votar…` | 973 / 973 / 977 / 977 / 993 / 979 / 1024 |
| P5 练习 Q65 选项 | `A. el lunes 9B1` | 900 / 900 / 904 / 904 / 920 / 906 / 950 |
| P6 练习 Q87+Q91 | `B. 15Un debate «propuesto» es…` | 1130 / 1130 / 1134 / 1134 / 1150 / 1136 / 1181 |
| P6 练习 Q88+Q93 | `…B. elEs posible que el debate ___ (tener)…` | 1178 / 1178 / 1182 / 1179 / 1201 / 1182 / 1232 |
| P6 练习 Q90+Q94 | `…a lasEs importante que cada dato ___ (ser) claro.` | 1201 / 1201 / 1205 / 1200 / 1220 / 1204 / 1251 |
| P6 练习 Q92（仅 de） | `…C. unaKasten: sondeo · muestra…` | 1150（de） |
| P8 题目 | `El voto por correo se pide hasta el ___. (A. jueves 19 · B.B1` | 1480 / 1479 / 1486 / 1476 / 1499 / 1485 / 1533 |
| P8 答案区（RESPUESTAS，约 L1620–1800） | de L1625 `Infinitiv113.`、L1627 `um39.`、L1631 `berührt78.`；en L1627 `midnight39.`、L1628 `infinitive113.`、L1632 `infinitive114.`；fr L1631 `infinitif113.`、L1633 `minuit39.`；it L1620 `infinito113.`、L1622 `mezzanotte39.`；nl L1653 `infinitief113.`、L1655 `om39.`；pt L1630 `infinitivo113.`、L1633 `infinitivo114.` | 各版 20–30 处（见上表） |

**（b）全家目录粘连（11 版，合计 77 处）**——同一类，在 core 亦在：每版 7 处，`Pág. 2La semana, día a día` … `Pág. 8Ejercicios y respuestas`（Pág. 2/3/4/5/6/7/8 各 1 处）。

**排除项（已核查，非粘连）**：
- `29N` 不是粘连：印 PDF 文字层亦作 `EL CAMINO AL 29N`，为有意缩写（core 印 txt 2 处）。
- 品牌驼峰合法：`laSexta`、`MiDNI`、`LaLiga`；≥20 字符长词扫描只命中真实德/荷长词（`Wahlkampfveranstaltung`、`verkiezingscommissie`）。
- 数字粘连全部位于 RESPUESTAS 区内（区外 0 处）。

**印 PDF 干净证据**：7 版印 txt 在全部抽查点均为 0：`5,titular`、`correo.Este`、`elEs posible`、`lunes 9B1`、`15Un`、`midnight39`、`nfinitiv113` 各 0；P1 目录印 txt 为 `Pág. 2 La semana`（PyMuPDF 框：`Pág. 2` x 1096.1–1142.8，续以带前导空格的 ` La semana, día a día`）；ru P1/P2 目视（见 §8）亦干净。

**严重度 low**：与 G3 同级——text.md 专属、内容齐全有序、读者可辨读，但已发布的网站正文 visibly garbled（如 `midnight39.`、`Nairobi77.`、`infinitivo113.`）。印刷报纸不受影响。

**修复建议**：导出器在栏间拼接处保留空格/换行（根治）；或按 G3/H1 方式对 text.md 做手术式修复（7 版 (a) 类 + 11 版 (b) 类；注意 FIX-LOG-2 已记的导出器陷阱：全量重导 text.md 不可直接落盘，须手术式改）。

## §3 H1 核实 — 在版，无回归

- es-ru text.md L147 = `AHORA TÚ　Теперь вы`（全角空格 U+3000）；词边界正则 `\bты\b` = **0**；`Теперь ты` 0；`Теперь вы` 1；`А вы?` ×4；共 1888 行。
- 印 + 网 PDF 文字层（`pdftotext`，53,420 B，印网逐字节相同）：`Теперь вы` 各 1，`Теперь ты` 0，`А вы?` 各 4。印 txt L208 `Теперь вы`；L331 `пришлите их в редакцию.`；L403 `nunca «en las 21:00».`。
- 目视：ru P1 渲染图，`AHORA TÚ　Теперь вы` 在 LA SEMANA EN CIFRAS 栏下清晰在版。
- 注：PyMuPDF 抽取会丢全角空格（显为 `AHORA TÚТеперьвы`），为抽取 artifact，与 FIX-LOG-3 记述一致，非问题。

## §4 G1/G2/G3、F2/F3/F4 核实 — 全部在版，无回归

- **G1**（es-ja）：text.md「世界遺産」0，「無形文化遺産」1，L1772 `30. Verdadero — ユネスコが2010年にフラメンコを無形文化遺産に登録`；目视 ja P8 答案区同句在版。
- **G2**（es-pt）：text.md `você` 0，`Agora tu` 1，`E tu?` 4；目视 pt P1 `AHORA TÚ　Agora tu` 在版。
- **G3**（es-ru text.md）：L300 `пришлите их в редакцию.`（¿Y TÚ? 框尾，在位）；L327 `nunca «en las 21:00».`（DECIR 尾，在位）；L208 一带为 `La semana, día a día: del`，无孤儿句；DECIR 标题 L321，尾句在其后 6 行内，与其余 10 版一致。
- **F2**（P6 时间线措辞）：11 版 text.md `sin el PSOE confirmado` 各 ×1，旧措辞 `sin el PSOE).` 各 0。
- **F3**（P1 刊头顶行，PyMuPDF 框，日期 x0 固定 1039.4pt）：fr 副标右端 974.1pt，间隙 **65.3pt**（第三轮记 65.4，仅舍入差）；it 970.7pt，间隙 **68.7pt**；de `LIEST` x1=1035.0pt，间隙 **4.4pt**（一尾随空格 span 止于 1039.4，计入会误算为 0.0；真间隙 4.4pt，两词分明、无合并——与前三轮已接受结论一致）。P1 文字中 `ESPAGNOLSSEMANA` / `SPAGNOLISEMANA` 各 0。
- **F4**（es-ru P2 DECIR）：标题 y0=877.7pt；末行 `nunca «en las 21:00».` 位于 (403.9, 1052.9)，同栏、紧贴段后——与第二/三轮数值相同。目视 ru P2：DECIR 整栏完整，¿Y TÚ? 框以 `пришлите их в редакцию.` 收尾。

## §5 机械门禁 — 11 版全绿（`gates_all4.sh`，自第三轮脚本仅换路径；`GATES DONE 19:22:41`，87 条 rc=0，0 条非零）

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

- 注：edge 日志行 `1 touch/near-lines` 为已知计数 artifact（汇总行自身含关键词）；JSON 为真凭：11 版 8 页合计均为 0 TOUCH / 0 NEAR。
- de boxtitle 1 marginal（+0.7px）在容差内，第四轮一致，已接受。
- spill OBSERVE 均为已知词框注记位置，非溢出。
- p8 keydiff [137,138] 为翻译题设计差异（与 core 不同），10 版一致。

## §6 已核查非发现（不重报，仅记已查）

- **F1 首字母下沉**：FIX-LOG 裁定不修，不重报。
- **\*-ru 拉丁标题字体**（Noto Sans vs Newsreader）：已知跨家 D5 系统性问题，另有工人统一修 svglib.py，不重报。
- **PROOF-NOTE-3 §5 记录更正**：其文 "text.md U+201C/U+201D 各 0 次" 与事实不符——文件与第三轮逐字节相同，而 text.md 实际含弯引号：core 5/5、de 3/0、en 3/3、ko 2/2、nl 0/3（合计与本轮 census 一致：core 10、de 3、en 6、ko 4；nl census 为 4，text.md 为 3——第 4 个弯引号只在 SVG 内、不在 text.md 导出中，全部 4 个均在 Newsreader 内，D5 PASS）。不改变任何一版状态；实质门禁（census）历轮均通过。
- **pt P1 顶行副标未被裁切**：目视疑似末字贴边，实测 PyMuPDF 框：整行 x 66.0–1091.1pt，右余 371.4pt，`…LEITORES DE LÍNGUA PORTUGUESA` 完整；其余 9 版同行右余 399–595pt，均无裁切。
- **ko P1 词框 `"토론"`**：ASCII 双引号在源头（`2026-w47-es-ko/content12.py:116`，`"\"토론\": …"`），印版与源头一致，为韩语引号风格选择，非缺陷；其余版用 `« el debate »`。
- **ja "正誤正誤"**：印版 0 处；`正誤` 为正误题型标签，正确。
- **nl `aantonende wijs`**：正确荷兰语直陈式术语，与 `aanvoegende wijs`（虚拟式）对照使用（#96/#111 `creo que` 后），无误。
- **ja/ko 国民党/국민당 = PP**：标准译名，P2 日历注各 1 处。
- **"Cinco claves" 半译**：de/en/fr/it/nl/ru/ja 均在同框内印西班牙语原文全称，为已接受的摘要体例。
- **pt #149 `A que horas fecha?`**：欧葡口语，可接受（与第三轮一致）。
- **CJK 全角括号前无空格**（如 ko `29(선거 13일)`、ja `29（選挙…`、core `29（距…`）：全家 CJK 体例，非粘连。
- **P5 MiDNI 暂停解除 5 Nov**：与前轮一致，本轮未重开。
- **其余第三轮 §6 已接受项**：本轮全部复核，无变化。

## §7 逐版结论

| 版 | H1/G1–G3/F2–F4 | I1(a) 分版粘连 | I1(b) 目录粘连 | 门禁 | 结论 |
|---|---|---|---|---|---|
| core-es | —（基准版；F2 在版） | 0 | 7 | 全绿 | **有问题（low，I1(b)）** |
| es-de | F2/F3 在版 | 31 | 7 | 全绿（boxtitle 1 marginal 已接受） | **有问题（low，I1）** |
| es-en | F2 在版 | 37 | 7 | 全绿 | **有问题（low，I1）** |
| es-fr | F2/F3 在版 | 28 | 7 | 全绿 | **有问题（low，I1）** |
| es-it | F2/F3 在版 | 27 | 7 | 全绿 | **有问题（low，I1）** |
| es-ja | G1 在版 | 0 | 7 | 全绿 | **有问题（low，I1(b)）** |
| es-ko | F2 在版 | 0 | 7 | 全绿 | **有问题（low，I1(b)）** |
| es-nl | F2 在版 | 29 | 7 | 全绿 | **有问题（low，I1）** |
| es-pt | G2 在版 | 27 | 7 | 全绿 | **有问题（low，I1）** |
| es-ru | H1/G3/F2/F4 在版 | 7 | 7 | 全绿 | **有问题（low，I1）** |
| es-zh-tw | F2 在版 | 0 | 7 | 全绿 | **有问题（low，I1(b)）** |

## §8 工作记录

- **全文通读**：core-es text.md 1803 行全文；10 版讲解层 plus-diff 逐行读完（新生成，行数与第三轮相同：de 599、en 643、fr 664、it 603、ja 507、ko 528、nl 710、pt 614、ru 760、zh-tw 322，共 5,950 行）。
- **P8 答案 1–150**：11 版 text.md 全数在场；门禁 p8-extract 150/150、compare CLEAN（keydiff [137,138] 设计差异）。注：en/it/pt 的严格行首正则初查曾误报缺号，系两栏交错导出所致，已逐号 grep 确认全在。
- **日期/星期/算术**：`date -d` 核 13 Nov 2026 Fri、16 Mon、19 Thu、20 Fri、21 Sat、22 Sun、23 Mon、24 Tue、25 Wed、27 Fri、28 Sat、29 Sun，全部与报纸一致；"Faltan 13 días"（29−16=13 ✓）；RTVE 民调 45+45+30+30+15+3×10=**195** ✓；45−30=**15** ✓；民调禁令 24–28 = **5 天** ✓；竞选 13–27 = 15 天 ✓。
- **引文**：8 条 FRASES DE LA SEMANA 逐条核对原文与页码（Página 1/4/2/5/3/6/3/6），全部逐字一致；作文模范文 #150 手数 **97 词**，与宣称一致。
- **欧冠 MD5**：网查 UEFA 赛程页 + NBC Sports 核实——皇马–PSV 周二 24 Nov；Sabah–巴萨 周三 25 Nov 18:45；马竞–Viking 周三 25 Nov，与 P4 一致。西甲第 13 轮（巴萨 33、皇马 30、马竞 28；巴萨客场 1–2 胜马竞）第三轮已自公开来源核实，本轮未重查。
- **ABSTRACT**：11 版全部读过，均为读者母语，事实与正文一致（13 Nov 辩论、29 Nov 大选、邮寄截止 19 日、弗拉门戈 16 日、圣塞西莉亚 22 日、西甲第 13 轮、欧冠）；无 ASCII 双引号；zh-tw 简体独有字 0（初查命中 黑/化 为误报，二者繁简同形）；非 CJK 版 CJK 字 0。
- **目视抽查**（100 dpi 渲染，读后即删）：ru P1（H1 在版）、ru P2（DECIR + ¿Y TÚ? 完整）、ja P8（G1 在版）、pt P1（G2 在版；顶行副标实测无裁切，见 §6）。
- **只读**：未修复、未重建、未 commit、未 push、未跑 lint、未改 SOP、未碰其他家庭/其他周。工具解释器 `~/workspace/weekly-git/tools/venv/bin/python`。
- **磁盘**：开始 95G 已用 / 55G 空闲（150G 盘），结束 95G，未触发 ≥100G 门限。渲染图 4 张已删除；工作目录仅留日志、指纹、diff、txt 抽取。
- **建议下一步**：修复 I1（text.md 专属；导出器根治或手术式修复，见 §2），随后按 SOP §8.4 对被碰版做新一轮独立重校。
