# GATE-LOG — 2026-W47 it-de 独立复校（fix1 后第二轮全量复校）

复校日期：2026-11-11。venv：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0，FreeType 2.14.3；freeze guard 通过，非 ko 版）。
生产目录只读；全部构建输出重定向至本 scratch；`PYTHONDONTWRITEBYTECODE=1`；TMPDIR 指向本 scratch 下 `tmp/`。

## 0. SHA 硬规则（开工核对 + 完工复核，两次全对）

| 件 | 字节数 | SHA-256 | 结果 |
|---|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-DE.pdf` | 14,037,237 | `527b38ce33f20765b211d7191623d76c6fbb3a56f3a19aa5167d7a0f32211457` | ✓ |
| 网页 PDF `La-Lucerna-VOL4-DE-web.pdf` | 1,297,272 | `f9f4343bdcec894854e3362a9f46b6c17d3b992076096c9970b13e1cc27a4d3a` | ✓ |
| text.md `2026-w47-it-de.text.md` | 56,683（1317 行） | `36a11a8f2b58452374b7211434b78e4526c2f584f21764f98a4c2ca9fc302ed4` | ✓ |

开工探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` RC=0 + scratch 内真实写文件通过。

## 1. 重建（自写 `rebuild.py`：生产副本 → scratch `rebuild/`，OUT/BASE 重定向）

- run.py rc=0，TOTAL 150（A2 47 / B1 70 / B2 33）；页 10/18/18/18/18/18/12/38；范文 99 词；FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE = 0。
- render.py rc=0；SVG 8/8 字节一致。
- 重渲印 PDF 与交付件逐字节相同（SHA `527b38ce…`）。

## 2. webpdf 重建

- rc=0，1,297,258 B（与交付 1,297,272 B 差 14 B，符合“不可复现”预期）。
- 文字层印/网/重建三方原始文本逐字节相同，多重集哈希均为 `dd0f5b6337e37872b92965691be02ba0c4ceaf967afe9684cb0a9751c4236e94`。
- 词计数 7785（fix1 称 7784——计数口径差异，非缺陷，已记录）。

## 3. text.md 复导出（自写 `reexport_textmd.py`，用 `production/2026-w46/core-it/finish` 的 `export_it_textmd`）

- 字节一致：56,683 B、1317 行、150 题，SHA `36a11a8f…` 与交付一致。

## 4. freeze baseline + freeze diff

- baseline：8/8 字节一致 rc=0；Pillow 13 守卫通过；core 完整性复核通过（core-it SVG 在 `core-it/svg/`）。
- diff rc=0：P1 +30/−46、P2 +36/−29、P3 +35/−30、P4 +29/−26、P5 +44/−41、P6 +31/−25、P7 +43/−40、P8 +164/−629；新增 CJK 仅 13× U+3000（家具分隔符，豁免）。
- 逐条分类：未解释的 added 仅 2 条（均为 P8 “Subjekt + Verb”复合节点，意语句 + 德语注，可解释）；removed 139 条全为 core P8 答案行换行碎片，键本身由 p8 compare CLEAN 证同。
- 注意：自写 `classify_freeze.py` 的节点级意文拼接比较法被证明不可靠（difflib 对重复句错位，误报假差异——已用 grep 证实 `IL PRESENTE`、`COMPRENSIONE`、`QUARTA EDIZIONE`、`VOL. 4` 在 core 与本版 SVG 中各 1×；不要再引用该脚本的 mismatch 输出作证据）。

## 5. occlusion audit

- rc=0，**0 flags**。selftest 6 类阳性对照全触发、干净对照静默。

## 6. p8 compare

- extract 150/150 rc=0。
- compare `--core-dir/--edition-dir --target it --total 150` rc=0，**CLEAN**，missing=[]、extra=0、keydiff=[137,138,139]。（首试未加 `--total` 报错 rc=2，p8.py compare 必须带 `--total`。）

## 7. 源码级复现 fanout（自写 `replicate_fanout.py`，独立复写 fanout 变换）

- 计数失配 0，6 个文件残留 CJK 0 行；复现件与生产件 **10/10 文件逐字节一致**（content12/34/56/7/8、bslib4、render、run、svglib、ABSTRACT.txt）。
- 结论：本版与 core 的差异仅来自已记录的翻译变换，意大利目标语未动。bslib4 与 core 的 diff 仅页脚/页码行/注前缀三处翻译；render.py diff 仅 BASE 路径 + 输出文件名。

## 8. D1/D2 回归（盒右缘 961px；接受下限 +5px）

| 缺陷 | PIL 真墨 | 96dpi 渲染像素 | 文字层 bbox | 最紧值 | 结论 |
|---|---|---|---|---|---|
| D1 P1 `LA SETTIMANA IN CIFRE　ZAHLEN` | +25.0（墨 936.0） | +29（固实 932；AA 933/+28） | +24.9（702.05pt → 936.1px） | **+24.9** | 通过 |
| D2 P2 `LA FRASE PER RICORDARE　MERKE` | +9.5（墨 951.5） | +11（固实 950） | +8.1（714.7pt → 952.9px；网同值） | **+8.1** | 通过 |

- 盒缘 961 得证：P1 y=1450 行灰度 @955/@960=238、@965/@1000=250。
- 旧串 0 次：`DIE WOCHE IN ZAHLEN`、`MERKSATZ`（作标题 gloss）在 svg + text.md + content12.py 均为 0；仅 `WEEKLY-KIT.md` §12 修史记录（L94–95、L99）还提及旧串，属历史记录可接受。
- 全版 29 奶油盒标题重扫（PIL 真墨 + 全节点扫描）：横向 0 flags；最紧 D2 +9.5、P7 ERRORI TIPICI +13.8、P3 HINWEIS +19.2、D1 +25.0。
- 全节点最紧：P1 LA SETTIMANA 副标题 `Die Woche　Cosa succede, giorno per giorno` 墨 1856.2 vs 盒 1862 → +5.8（proof1-D1 副标题，proof2 测 +5.5）；cifre 盒最宽行 +20.8。
- 纵向最紧：P7 LETTERE spareV +0.1（PIL）；渲染最低固实墨行 1671 vs 盒底 1673.0 → +2.0。

## 9. 渲染像素验证（交付印 PDF，96dpi + 200dpi，`pages/`）

- 全页最右固实墨：P1 1861（−1）、P2 1862（0，y=1585–1588）、P3 1861、P4 1861、P5 1862（0，y=600–603）、P6 1861、P7 1861、P8 1864（+2，y=1374–1376）。
- P2/P5 最右行经 SVG 节点确认：P2 y=1594 `Una festa, una giornata verde`（PIL 1862.0，与 core 同值）；P5 y=603 `Foto: Jean-Baptiste-Camille Corot — Wikimedia Commons,`（PIL 1862.0，与 core 同值）。恰在边距，非缺陷。
- P8 y=1382 家具行 `Jede Antwort hat eine einzeilige Notiz auf Deutsch　✓ = Modelltext-Aufgabe`（PIL 1862.0，渲染 1864）；core 对应行（`每题附一句中文简析　带 ✓ 的为范文题`，同 y=1382）同一构造。观察项，非缺陷。

## 10. P8 字号（SOP §1.1，下限 9.75pt）

- 最小 13.0px = **9.75pt**（185 节点，即 RISPOSTE 键）；其余各页最小 15.5px（P6 17px）。达标。

## 11. §1.1 扫描

- 纸色 #fbfaf6 ×10；无金/砖/近黑（“gold”×3 命中全在 base64 图片串内，非颜色）；VOL.4 ×9；VOL.5 ×3 且全为合法节点（P2 交叉引用、LETTERE 说明、VOL.5 预告栏）；徽章色 #5c6e30 ×44、#46581f ×380、#37402f ×39；“全页 rect”×8 均为无描边的纸底 `<rect width="1950" height="2700" fill="#fbfaf6"/>`（每页 1 个），描边全页框 0 个。

## 12. text.md 校验（v2/v3/v4，`validate_textmd*.py`）

- forward：**0 miss**（合理语义；v1 朴素整行子串法的 29/160 条为方法 artifact：导出器按设计不导出的家具 + 选项碎片 + 正则 bug）。
- reverse v4（去标点集合差，`out/textmd-validate-v4.log`）：text.md 有、SVG 为 0 次的词仅 10 个——`key`（导出器标记）、`Aufgabe`/`Offene`（导出器注）、`attraversare:i`、`portare:i`、`piantare:noi`、`pregare:la`、`mangiare:la`、`vincere:ha`、`pareggiare:ha`（全角冒号无空格连接，SVG 中为拆分词）。**0 个新内容词。**
- SVG 有、text.md 为 0 次的词 133 个：裸数字题号、家具词、不导出的 `[...]` 指令词、冒号连接词的拆分侧。全部已解释。
- text.md 汉字 0 个、U+3000 ×106、全角冒号 ×14；禁词 Ucraina/Russia/Putin 0；“next Sunday”在 text.md 中 0 次。

## 13. 150 键核对（text.md 层 vs core-it text.md）

- 两版答案各 150 条，题号 1–150 全齐；keydiff [137, 138, 139, 150]（137–139 重定向翻译键，与 p8 一致；150 为写作题注德语译文）。
- 逐字相同答案行：16–20、60–61、85–86，共 9 行。
- 练习行键 vs Risposte 键：仅 Q150 表述差异（设计），无不一致。

## 14. 孤儿扫描

- 单字节点全版扫描：**0 孤儿**。全部为结构项（徽章/`Einsetzen`/kicker/日期标题）、栏中换行末词、或已接受项 P3-main 末行 `costruzioni.`（core 同节点同栏：core (538.5, 1202.94)，本版 (538.5, 1232.665)；y 移位为德语层重排）。
- y<400 的单字节点仅 P1 页眉 kicker（36pt）与 P2 大标题末词 `novembre`（37pt），均为标题结构。

## 15. 目视检查（交付印 PDF 200dpi 全页 + 5 张标注裁图）

- 8 页全页图逐页目视：无溢出、无重叠、无裁切、无乱码（P1–P8 逐页要点见 PROOF-NOTE §9）。
- 标注裁图（红线=盒/页缘，`pages/crop-*.png`）：
  - `crop-d1-title.png`：标题完整在盒内，与红线有明显空隙。
  - `crop-d2-title.png`：标题完整在盒内，与红线有明显空隙。
  - `crop-p7-lettere-bottom.png`：末行下行字母完整在盒内，红线（盒底 1673）位于其下。
  - `crop-p8-furniture.png`：末字 `Aufgabe` 的 `e` 字形完整、无裁切，红线（1862）仅贴其右缘。
  - `crop-p1-subtitle.png`：`giorno per giorno` 末端与红线有明显空隙。

## 16. 内容抽查（全文通读 text.md 1317 行）

- 意甲 11 轮 10 场、24 球（逐场加总 3+1+2+3+3+2+3+1+2+4=24）；Lazio 29、Inter 28、Roma 27、Milan 24、Como 23、Udinese 5。
- Q137–140 翻译正确；Q83–86 算术正确（13−11=2、6+7=13）；P7 FRASI 8 条页码抽查无误；150 题键与题面逐项一致。
- 星期核验（`TZ=Europe/Rome date -d`）：11月6日周五、7日周六、8日周日、9日周一、12日周四、13日周五、14日周六、15日周日、16日周一、17日周二、19日周四、20日周五、21日周六、22日周日、23日周一、24日周二、12月2日周三、12月6日周日、12月31日周四、10月15日周四、10月28日周三——与文中全部星期表述一致。

## 17. STRADDLE 裁决

- 全版 29 奶油盒标题 + 全节点扫描：无任何标题越过奶油盒右缘，STRADDLE 不触发；备份旧版对照无需跑（无 straddle、无新缺陷）。
- D1/D2 旧串在备份旧版中本就存在（非回归），本次只验 fix1 后新版在盒内——已通过。

## 结论

**0 缺陷。结论 (a)：干净，可定稿。**
观察项 3 项（P8 家具行贴边 +2px 渲染、P7 LETTERE 盒底 +2.0px 渲染、P1 副标题 +5.8px PIL）：均在盒内/页内，字形完整，无裁切、无重叠。
