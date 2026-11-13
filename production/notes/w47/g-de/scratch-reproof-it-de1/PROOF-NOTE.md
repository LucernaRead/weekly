# PROOF-NOTE — 2026-W47 it-de 独立复校（fix1 后第二轮全量复校）

**结论 (a)：干净，可定稿。0 缺陷。观察项 3 项（均在盒内/页内，无裁切、无重叠，见 §5）。**

- 版次：2026-w47-it-de（意大利语目标语 × 德语读者，VOL.4）
- 复校员：独立复校 subagent；fix1 后第二轮全量复校（SOP §8.4）
- 复校日期：2026-11-11
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it-de1/`

## 1. SHA 硬规则（完工复核，三件全对）

| 件 | 字节数 | SHA-256（实测） | 结果 |
|---|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-DE.pdf` | 14,037,237 | `527b38ce33f20765b211d7191623d76c6fbb3a56f3a19aa5167d7a0f32211457` | ✓ 一致 |
| 网页 PDF `La-Lucerna-VOL4-DE-web.pdf` | 1,297,272 | `f9f4343bdcec894854e3362a9f46b6c17d3b992076096c9970b13e1cc27a4d3a` | ✓ 一致 |
| text.md `2026-w47-it-de.text.md` | 56,683（1317 行） | `36a11a8f2b58452374b7211434b78e4526c2f584f21764f98a4c2ca9fc302ed4` | ✓ 一致 |

## 2. D1/D2 回归（fix1 修后重测，三法取最紧者，接受下限 +5px）

旧串 `DIE WOCHE IN ZAHLEN`、`MERKSATZ`（作标题 gloss 时）在 SVG + text.md + content12.py 中均为 **0 次**；content12.py:44 = `LA SETTIMANA IN CIFRE　ZAHLEN`，:177 = `LA FRASE PER RICORDARE　MERKE`（translations.py de 值 L94、L563 已核）。

| 缺陷 | 标题（fix1 后） | PIL 真墨 | 96dpi 渲染像素 | 文字层 bbox | 最紧值 | 结论 |
|---|---|---|---|---|---|---|
| D1 P1 cifre | `LA SETTIMANA IN CIFRE　ZAHLEN` | +25.0（墨 936.0，盒缘 961） | +29（固实墨 932；AA 933/+28） | +24.9（xMax 702.05pt → 936.1px） | **+24.9** | 通过 |
| D2 P2 frase | `LA FRASE PER RICORDARE　MERKE` | +9.5（墨 951.5） | +11（固实墨 950） | +8.1（xMax 714.7pt → 952.9px；网页 PDF 同值） | **+8.1** | 通过 |

- 盒右缘 961px 得证：P1 y=1450 行灰度 @955/@960=238、@965/@1000=250。
- 29 个奶油盒标题全版重扫（PIL 真墨 + 全节点扫描）：横向 0 flags；最紧依次为 D2 +9.5、P7 ERRORI TIPICI +13.8、P3 HINWEIS +19.2、D1 +25.0。
- 标注裁图目视（200dpi，红线=盒缘 961）：D1/D2 标题墨迹完整、与红线有明显空隙。**D1/D2 回归通过。**

## 3. 门禁汇总（详见 GATE-LOG.md）

| 门禁 | 结果 |
|---|---|
| 重建（run.py + render.py，OUT/BASE 重定向至 scratch） | rc=0；TOTAL 150（A2 47 / B1 70 / B2 33）；页 10/18/18/18/18/18/12/38；范文 99 词；FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE = 0；SVG 8/8 字节一致；重渲印 PDF 与交付件逐字节相同 |
| webpdf 重建 | rc=0；1,297,258 B（与交付差 14 B，符合“不可复现”预期）；印/网/重建三方文字层原始文本逐字节相同，多重集哈希一致 |
| text.md 复导出 | 字节一致（56,683 B、1317 行、150 题） |
| freeze baseline / freeze diff | 8/8 字节一致 rc=0；diff 仅已解释项（P8 +164/−629 为答案行换行碎片；新增 CJK 仅 13× U+3000 家具分隔符，豁免） |
| occlusion audit | rc=0，**0 flags**；selftest 6 类阳性对照全触发、干净对照静默 |
| p8 compare `--total 150` | rc=0，**CLEAN**；missing=[]、extra=0、keydiff=[137,138,139] |
| 源码级复现 fanout（独立复写变换） | 复现件与生产件 **10/10 文件逐字节一致**；与 core 的差异仅来自已记录的翻译变换，意大利目标语未动 |
| §1.1 扫描 | 纸色 #fbfaf6 ×10；无金/砖/近黑（“gold”×3 全在 base64 图片串内）；VOL.4 ×9；VOL.5 ×3 全合法；徽章色 #5c6e30 ×44、#46581f ×380、#37402f ×39；“全页 rect”×8 均为无描边纸底；描边全页框 0 个 |
| P8 字号 | 最小 13.0px = **9.75pt**（185 节点，即 RISPOSTE 键），达 SOP §1.1 下限 |

## 4. text.md ↔ SVG 一致性（本轮收尾，v4 集合差）

- forward：**0 miss**（合理语义；v1 的 29 条为导出器按设计不导出的家具/选项碎片）。
- reverse（v4：去标点集合差）：text.md 有、SVG 为 0 次的词仅 **10 个**，全部已解释：`key`（导出器标记）、`Aufgabe`/`Offene`（`(Offene Aufgabe — Modelltext unten)` 导出器注）、`attraversare:i`、`portare:i`、`piantare:noi`、`pregare:la`、`mangiare:la`、`vincere:ha`、`pareggiare:ha`（7 个全角冒号无空格连接的动词+代词，SVG 中为拆分的两个词；词本身在 SVG 中存在）。**0 个新内容词。**
- SVG 有、text.md 为 0 次的词 133 个：裸数字（题号，text.md 中为 `113.` 附着形式或被去编号正则剥离）、家具词（AUF/TEXT/PAGINA/…，不导出）、`[...]` 指令词（`Einsetzen`、`Ins`、`übersetzen`、`Schreiben`、`Richtig`、`bilden`，在 text.md 的方括号标签内）、以及上述冒号连接词的拆分侧。全部已解释。
- 决定性交叉证据：字节一致的复导出（§3）+ 三方文字层哈希一致。
- 其他：text.md 汉字 0 个、U+3000 ×106、全角冒号 ×14；禁词 Ucraina/Russia/Putin 0；“next Sunday”在 text.md 中 0 次（冻结核心，非缺陷）；范文 99 词。

## 5. 150 键核对（text.md 层，vs core-it text.md）

- 两版答案各 150 条，题号 1–150 全齐。
- keydiff：**[137, 138, 139, 150]** —— 137–139 为重定向的读者句翻译键（与 p8 keydiff [137,138,139] 一致；150 的“键”是写作题注的德语译文，p8 按写作项处理故不在 keydiff 内）。
- 逐字相同的答案行：16–20、60–61（冻结动词范式）+ 85–86（算术），共 9 行。
- 练习行键 vs Risposte 键：仅 Q150 有表述差异（练习行为 `(Offene Aufgabe — Modelltext unten)`，Risposte 为 `✓ Modelltext in Abschnitt H unten (99 Wörter)`），属设计，无不一致。
- 内容抽查：意甲 11 轮 10 场、24 球（逐场加总 3+1+2+3+3+2+3+1+2+4=24）；Lazio 29、Inter 28、Roma 27、Milan 24、Como 23、Udinese 5；Q83–86 算术正确（13−11=2、6+7=13）；P7 FRASI 8 条页码抽查无误；星期核验（`TZ=Europe/Rome date -d`）与文中全部星期表述一致。

## 6. 最右墨迹行裁决（PIL + 渲染像素 + 节点确认）

| 位置 | 行 | PIL 墨右 | 渲染像素 | 裁决 |
|---|---|---|---|---|
| P8 y=1382 家具行 | `Jede Antwort hat eine einzeilige Notiz auf Deutsch　✓ = Modelltext-Aufgabe` | 1862.0（恰在边距） | 1864（+2） | 观察项（§7 之一） |
| P2 y=1594 | `Una festa, una giornata verde` | 1862.0（恰在边距） | 1862（0） | 非缺陷 |
| P5 y=603 | `Foto: Jean-Baptiste-Camille Corot — Wikimedia Commons,` | 1862.0（恰在边距） | 1862（0） | 非缺陷 |

- P2/P5 两行与 core 同节点同值（core P2/P5 墨右亦为 1862.0），继承构造。
- P8 家具行的 core 对应行（`每题附一句中文简析　带 ✓ 的为范文题`，同 y=1382）为同一构造；无裁切、无重叠（occlusion 0 flags）、距页缘 1950 尚有 88px。
- 全页最右固实墨：P1 1861、P2 1862、P3 1861、P4 1861、P5 1862、P6 1861、P7 1861、P8 1864。

## 7. 观察项（非缺陷，不影响定稿）

1. **P8 家具行贴边**：见 §6。PIL 恰在边距 1862.0，96dpi 渲染读 1864（+2px，栅格化）；200dpi 裁图目视：末字 `Aufgabe` 的 `e` 字形完整、无裁切，红线（1862）仅贴其右缘。无边框、无他物重叠，不触发 STRADDLE。
2. **P7 LETTERE 盒底极紧**：纵向余量 PIL +0.1px、渲染 +2.0px（最低固实墨行 1671 vs 盒底 1673.0）。200dpi 裁图目视：末行 `Aufsätze; das Versprechen gilt für VOL.5.` 下行字母（`p`、`g`）完整在盒内，红线（盒底 1673）位于其下。在盒内，但为全版最紧纵向余量。
3. **P1 副标题最紧**：`Die Woche　Cosa succede, giorno per giorno` 墨 1855.0–1856.2 vs 盒 1862 → +5.8（PIL）/+7（渲染）。在盒内。

## 8. 孤儿扫描

- 单字节点全版扫描（29 盒外）：0 孤儿。全部单字节点为 (a) 结构项（级别徽章 A2/B1/B2、`Einsetzen` 指令、页眉 kicker、日期标题），(b) 栏中换行末词（文章/练习行中部换行），(c) 已接受项 P3-main 末行 `costruzioni.`（core 同节点同栏：core (538.5, 1202.94)，本版 (538.5, 1232.665)，y 移位为德语层重排所致；栏中段，非栏断孤儿）。
- 无单字节点位于栏顶/栏底（y<400 者仅 P1 页眉 kicker 36pt 与 P2 大标题末词 `novembre` 37pt，均为标题结构）。

## 9. 目视检查（交付印 PDF 200dpi 全页 + 标注裁图）

- 8 页全页图逐页目视：版式、图片、图注、表格、练习区、答案区均干净，无溢出、无重叠、无裁切、无乱码。
  - P1：D1 cifre 盒、头条、球场照、QUIZ LAMPO 均正常。
  - P2：D2 frase 盒正常；中栏 `E LA SETTIMANA SCORSA?` 下留白为 core 固有栏流。
  - P3：Torrazzo 照、IL WEEKEND DOLCE、E TU? 均正常；中栏留白为 core 固有模式。
  - P4：赛果表、LA CLASSIFICA 均正常。
  - P5：Corot 画、IL PIANO DELLA SETTIMANA 均正常。
  - P6：MINIME DI ESEMPIO 柱状图、PROPOSTA ≠ LEGGE 均正常。
  - P7：Dante 像、ERRORI TIPICI、LETTERE、FRASI 页码均正常。
  - P8：150 题 + 150 答案行全齐，Q137–139 德语翻译键、Q150 范文注均正常。
- 标注裁图 5 张（红线=盒/页缘）：D1 标题、D2 标题、P7 LETTERE 底、P8 家具行、P1 副标题——字形均完整（见 §2、§6、§7）。

## 10. STRADDLE 裁决

- 全版 29 奶油盒标题 + 全节点扫描：**无任何标题越过奶油盒右缘**，STRADDLE 裁决不触发；备份旧版对照（`scratch-refanout-it/backup/2026-w47-it-de/`）无需跑（无 straddle、无新缺陷）。
- D1/D2 的旧串在备份旧版中本就存在（非回归），本次只验 fix1 后新版在盒内——已验通过。

## 11. 缺陷清单

**无。0 缺陷。**

---

*证据文件：`GATE-LOG.md`（本 scratch）、`pages/p200-1..8.png`、`pages/crop-d1-title.png`、`pages/crop-d2-title.png`、`pages/crop-p7-lettere-bottom.png`、`pages/crop-p8-furniture.png`、`pages/crop-p1-subtitle.png`、`out/textmd-validate-v4.log`。*
