# PROOF-NOTE-6 — W47 es 家庭第六轮独立重校

- **轮次**：第六轮独立重校（SOP §8/§8.4；校对员与建造者、第五轮修复者 6bb5d3e6、第五轮校对员 1aed0152 均不同；只校对、不修复）
- **日期**：2026-11-12（UTC 约 20:16–20:20；门禁 GATES6 DONE 20:19:27）
- **范围**：`production/2026-w47/` es 家庭 11 版：core-es（= es-zh-cn）+ `2026-w47-es-{de,en,fr,it,ja,ko,nl,pt,ru,zh-tw}`；被 J1 修复碰过的 7 版：de/en/fr/it/nl/pt/ru；未碰版 core/ja/ko/zh-tw 只做指纹一致性抽查
- **结论：(a) CLEAN — 0 findings。**
- **核实重点结论**：J1 修复 13/13 在位，断句与印层一致；I1 修复 312/312 仍在位（全量复核，非抽查）；H1、G1/G2/G3、F2/F3/F4 全部在版、无回归；全家词表差集重扫除已知排除项外无新增粘连；7 版机械门禁全绿；7 版 KIT 新 text.md SHA 各 2 处、印/网 SHA 未动；未碰 4 版指纹与第五轮一致、确认未动。

## §1 指纹 — 33/33 与 FIX-LOG-5 §7 / PROOF-NOTE-5 §1 一致

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| core-es | 4,317,615 / `6089c0fa5420` | 1,162,042 / `f0f6ed1de57a` | 43,789 / `9cc6462f702c` |
| es-de | 2,916,396 / `3fdc2ce60e6a` | 806,895 / `fd7edd4b8415` | 45,370 / `ff0387066ca9` |
| es-en | 2,915,635 / `a7d5aba8bd0f` | 806,124 / `bb690dd25b6c` | 45,046 / `3c2ef9876638` |
| es-fr | 2,914,957 / `fd0e9f83a989` | 805,426 / `960de8cf8d3b` | 45,834 / `ad8bcbcd0c4f` |
| es-it | 2,913,352 / `0cffc84e47c0` | 803,822 / `f533bb1aa133` | 45,211 / `491044bcfaab` |
| es-ja | 8,530,586 / `cbb3efedd9a2` | 1,280,143 / `70d46e27721f` | 46,578 / `bab03d4d6c8a` |
| es-ko | 5,229,281 / `e2ae545b1462` | 1,097,497 / `fad91509e34f` | 47,403 / `8407be401bb7` |
| es-nl | 2,915,320 / `c716ce60992a` | 805,809 / `8be3118b5080` | 45,342 / `d477656f5ef0` |
| es-pt | 2,914,243 / `ce89b874dfc0` | 804,705 / `06514f66f69d` | 45,576 / `7db6b340f4f6` |
| es-ru | 3,213,297 / `538ca756749a` | 1,061,847 / `8d440e9b52cf` | 52,367 / `ac246f8709d3` |
| es-zh-tw | 4,381,575 / `fd3e65ef1840` | 1,265,861 / `8871073245fd` | 43,818 / `d26fdddc0fa6` |

- 完整 33 个 SHA-256 见工作目录 `fingerprints6.json` / `fingerprints.txt`（逐项核对，全部命中）。
- 7 版被碰 text.md：字节数与完整 SHA-256 与 FIX-LOG-5 §7 新值逐字符一致（+1 B/处，fr +3 B）；行数未变。
- 4 版未碰 text.md（core/ja/ko/zh-tw）：字节数与 SHA-12 与 PROOF-NOTE-5 §1 一致——确认未动。
- 22 个印/网 PDF：字节数与 SHA-12 全部与 PROOF-NOTE-5 §1 一致、未动（网 PDF SHA 以盘上实时值为准核对）；11 版网 PDF 均 < 7 MB；11 版印 PDF 均为 8 页（新鲜抽取断言通过）。

## §2 J1 修复核实 — 13/13 在位，断句与印层一致

- **逐条复核**（`fix-report.json` 的 13 条 `applied`，逐版对照盘上 text.md）：4 个旧串全文件计数 **0/13**；13 处新串全部在记录行号上在位（`verify_j1_i1.json`，233 项断言全过）。修复行原文（截前 220 字）：
  - de L1150：`· C. solo datos oficiales, con final · B. una foto con margen de error · C. una Kasten: sondeo · muestra · indecisos ·`
  - en L1150 / fr L1154 / it L1152：`· C. solo datos oficiales, con final · B. una foto con margen de error · C. una sondeo · muestra · indecisos · margen…`
  - nl L1170：`· C. solo datos oficiales, con final · B. una foto con margen de error · C. una· indecisos · margen de error`（`una·` 为既有框分隔符，见 PROOF-NOTE-5 §3 (a)，非新问题）
  - pt L1154 / ru L1201：`· C. solo datos oficiales, con final · B. una foto con margen de error · C. una muestra · indecisos · margen de error`
  - fr L1756：`101. Es — Pour 1 heure, on emploie le singulier Es jueves 19`
- **印层复核**（本轮新鲜 PyMuPDF 抽取 `txt-print6/`，11 版各 8 页，与第四轮 `pdftotext -layout` 抽取交叉核对；PDF 未动，SHA 见 §1）：
  - 4 个粘连旧串在两种抽取、7 版中均为 **0**。
  - `con final`：`-layout` 视觉行 7 版各 1 处；PyMuPDF 阅读序 7 版真短语齐全（`solo datos oficiales, con fuente` + `A. un resultado final`）。
  - `una sondeo`（en/fr/it）：PyMuPDF 阅读序 3 版 `una promesa` + 框 `sondeo` 均在；`-layout` 中 en 同行 1 处，fr/it 分处相邻两行、两词分明。
  - `una muestra`（pt/ru）：PyMuPDF 阅读序 2 版 `una promesa` + `muestra` 均在；`-layout` 中 ru 同行 1 处，pt 分处相邻两行。
  - `Es jueves 19`（fr）：`-layout` 视觉行 1 处；PyMuPDF 阅读序 `singulier Es` ×1，`jueves 19` 原文计数 ×21（与 FIX-LOG-5 §3 一致；注：空白归一化后计为 22，第 22 处系一例跨行断句 `jueves\n19` 在归一化后合并所致，非新增内容——两份独立抽取原文计数均为 21）。
- **结论：13 处断句与印层完全一致，无一处印层亦粘连或无法判定。**

## §3 I1 / H1 / G1–G3 / F2–F4 核实 — 全部在版，无回归

- **I1（全量复核，非抽查）**：`scratch-fix4-w47-es/fix-report.json` 的 312 条 `applied` 逐版对照盘上 text.md——旧串全文件计数 **0/312**，新串全部在记录行号上 **312/312**（core 7、de 47、en 50、fr 41、it 39、ja 7、ko 7、nl 46、pt 43、ru 18、zh-tw 7）。
- **关键行抽查**：de L163 `5, titular`、L900 `lunes 9 B1`、L973 `correo. Este`；en L1627 `midnight 39.`；pt L1698 `21h30 128.`——全部在位；目录 `Pág. 2 La semana` 11 版各 ×1。
- **H1**（es-ru）：text.md L147 `AHORA TÚ　Теперь вы`（全角空格 U+3000）；`\bты\b` = 0；`Теперь ты` 0；`Теперь вы` 1；`А вы?` ×4；共 1889 行。
- **G1**（es-ja）：text.md「世界遺産」0，「無形文化遺産」1（L1772）。
- **G2**（es-pt）：text.md `você` 0，`Agora tu` 1，`E tu?` 4。
- **G3**（es-ru）：L300 `пришлите их в редакцию.`、L327 `nunca «en las 21:00».` 在位。
- **F2**（P6 时间线措辞）：11 版 text.md `sin el PSOE confirmado` 各 ×1，旧措辞 `sin el PSOE).` 各 0。
- **F3**（P1 刊头顶行）：本轮新鲜印层 11 版全文 `ESPAGNOLSSEMANA` / `SPAGNOLISEMANA` 各 0，均为 8 页。
- **F4**（es-ru P2 DECIR）：新鲜印层含 `nunca «en las 21:00».`（空白归一化后）。

## §4 全家同类残留再扫 — 无新增粘连

**方法**（词表差集法，脚本 `rescan6.py`，结果 `rescan6.json` / `rescan6.log`）：每版 text.md 词表（拉丁词 len≥2 + 西里尔词 len≥2，小写化）减印层词表（本轮新鲜 PyMuPDF 抽取 ∪ 第四轮 `-layout` 抽取，两源取并集）。

- **方法自验**：同一差集法跑修复前备份 `scratch-fix5-w47-es/text-pre-es-*.md`——7 版恰好命中 13 处旧串（de `confinal`、en `confinal`+`unasondeo`、fr `confinal`+`unasondeo`+`esjueves`、it `confinal`+`unasondeo`、nl `confinal`、pt `confinal`+`unamuestra`、ru `confinal`+`unamuestra`），与 FIX-LOG-5 §5 一致，证明该法对本类缺陷无漏网。
- **修后结果**：11 版差集候选仅剩两类已知排除项（逐项核实）：
  - `Portada` ×1/版（11 版全有）：text.md L3 导出器自带节标题 `## Portada`，非报纸正文词，不在印层——单字实词，非粘连。
  - 语言代码 artifact（L1 文件头 `# 2026-w47-es-xx` 的 slug 分词）：core `zh`/`cn`、fr `fr`、it `it`、ja `ja`、ko `ko`、nl `nl`、pt `pt`、ru `ru`、zh-tw `zh`/`tw`，各 ×1；`de`/`en`/`es` 未入候选（其本身即印层实词）。非粘连。
- **结论：无新增同类小写粘连残留。**
- **附带复扫**（9 类模式，`rescan6.py` 后半段）：数字粘连/句号→大写/句号→小写/驼峰/逗号/中点/右括号/分号粘连 11 版均为 0，命中仅为已知排除项——`29N`（每版 2 处，有意缩写）、品牌驼峰 `laSexta` ×9 / `LaLiga` ×1 / `MiDNI` ×8、slug `w47` 中的 `w4`（L1 文件头）、pt 时刻 `21h30`/`12h00`/`18h30`/`14h00`（`h3`×5 / `h0`×2 命中为时刻写法本身，合法）。

## §5 机械门禁 — 7 版全绿（`gates6.sh`，GATES6 DONE 20:19:27）

| 版 | p8 extract | p8 compare vs core-es | D5 census（弯引号 in Newsreader） |
|---|---|---|---|
| es-de | 150/150 rc=0 | CLEAN，keydiff [137, 138] | 3/3 PASS |
| es-en | 150/150 rc=0 | CLEAN，keydiff [137, 138] | 6/6 PASS |
| es-fr | 150/150 rc=0 | CLEAN，keydiff [137, 138] | 0/0 PASS |
| es-it | 150/150 rc=0 | CLEAN，keydiff [137, 138] | 0/0 PASS |
| es-nl | 150/150 rc=0 | CLEAN，keydiff [137, 138] | 4/4 PASS |
| es-pt | 150/150 rc=0 | CLEAN，keydiff [137, 138] | 0/0 PASS |
| es-ru | 150/150 rc=0 | CLEAN，keydiff [137, 138] | 0/0 PASS |

- p8 extract 7/7 为 150/150；compare 7/7 CLEAN（keydiff [137, 138] 为已裁定的翻译题设计差异，与第五轮一致）。
- D5 census 7/7 PASS，通过数与 PROOF-NOTE-5 §7 逐版相同（ru `noto_sans_elements=768` 为 PROOF-NOTE-5 §8 已记的跨家已知系统性问题，census 仍 PASS，不重报）。
- 未重渲染 PDF（PDF 未动，印/网 SHA 不变）；未跑 lint，未 commit，未 push，未改 SOP，未碰其他家庭/其他周。

## §6 KIT 抽查 — 7 版全部通过

- 每版新 text.md SHA（完整 SHA-256）在 KIT 中各出现 **2 次**（现行行 + J1 节）；旧 SHA 各出现 2 次（I1 节“文件：”行 + J1 节“改前”；ru 另 +1 次为 H1 行“改前”，共 3 次，符合链式记录）。
- 每版 KIT 末尾 `## 第五轮独立重校修复 J1` 一节各 1 处。
- 每版 KIT 中印/网 PDF 完整 SHA 各 ≥1 处，与盘上实时值一致、未动；新 text.md 字节数（KIT 以 `45,370 B` 逗号格式书写）与 FIX-LOG-5 §7 一致（de 45,370、en 45,046、fr 45,834、it 45,211、nl 45,342、pt 45,576、ru 52,367）。
- 注：本轮首版核验脚本误以无逗号纯数字查 KIT 字节数、并以空白归一化计数查 `jueves 19`，两处期望值写法有误（见 §2 注）；均已更正为 KIT 实际写法与原文计数后重跑，233 项断言全过——盘上文件无误。

## §7 逐版结论

| 版 | H1/G1–G3/F2–F4 | I1 修复 312 处 | J1 修复 13 处 | 门禁 | 结论 |
|---|---|---|---|---|---|
| core-es | —（基准版；F2 在版） | 7/7 在版 | —（未碰，指纹一致） | —（未重跑，本轮范围外） | **干净** |
| es-de | F2/F3 在版 | 47/47 在版 | 1/1 在位 | 全绿 | **干净** |
| es-en | F2 在版 | 50/50 在版 | 2/2 在位 | 全绿 | **干净** |
| es-fr | F2/F3 在版 | 41/41 在版 | 3/3 在位 | 全绿 | **干净** |
| es-it | F2/F3 在版 | 39/39 在版 | 2/2 在位 | 全绿 | **干净** |
| es-ja | G1 在版 | 7/7 在版 | —（未碰，指纹一致） | — | **干净** |
| es-ko | F2 在版 | 7/7 在版 | —（未碰，指纹一致） | — | **干净** |
| es-nl | F2 在版 | 46/46 在版 | 1/1 在位 | 全绿 | **干净** |
| es-pt | G2 在版 | 43/43 在版 | 2/2 在位 | 全绿 | **干净** |
| es-ru | H1/G3/F2/F4 在版 | 18/18 在版 | 2/2 在位 | 全绿 | **干净** |
| es-zh-tw | F2 在版 | 7/7 在版 | —（未碰，指纹一致） | — | **干净** |

## §8 已核查非发现（不重报，仅记已查）

- **F1 首字母下沉**：FIX-LOG 裁定不修，不重报。
- **\*-ru 拉丁标题字体**（Noto Sans vs Newsreader）：已知跨家 D5 系统性问题，另有工人统一修 svglib.py，不重报（本轮 ru census `noto_sans_elements=768`，与第五轮同一量级）。
- **es text.md 页内顺序打散**：跨家审计已裁定延期至 W47 后修导出器，本轮不重报。
- **nl L1170 `una· indecisos`**：`·` 为 D 框分隔符，既有写法（PROOF-NOTE-5 §3 (a) 已记），J1 修复未动此处，不作发现。
- **en 答案 88 注释偏短**：第四/五轮已读过同一文本，不作发现。
- **PROOF-NOTE-5 §8 其余已接受项**：本轮复核范围未变，无变化。

## §9 工作记录

- **只读**：未修复、未重建、未 commit、未 push、未跑 lint、未改 SOP、未碰其他家庭/其他周；除本 scratch 目录外未写任何东西。工具解释器 `~/workspace/weekly-git/tools/venv/bin/python`（系统 python3 未用）。
- **磁盘**：开始 95G 已用 / 55G 空闲（150G 盘），结束 95G，未触发 ≥100G 门限。工作目录 764K，仅留日志、指纹、抽取文本、核查脚本输出。
- **工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof6-w47-es/`：`PROOF-NOTE-6.md`（本文件）、`fingerprints6.py` / `fingerprints6.json` / `fingerprints.txt`、`extract_print6.py` / `txt-print6/`（11 版新鲜印层抽取）、`verify_j1_i1.py` / `verify_j1_i1.log` / `verify_j1_i1.json`（233 项断言）、`rescan6.py` / `rescan6.json` / `rescan6.log`、`gates6.sh` / `gates6.log` / `p8-extract-*.json,log` / `p8-compare-*.json,log` / `census-*.json,log`。
- **建议下一步**：J1 已独立验证通过，es 家庭第六轮无遗留问题；可按既定流程继续 W47 后续步骤（insert / 封面 / 全 lint）。
