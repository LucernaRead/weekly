# GATE-LOG — 2026-W47 it-de 独立复校（core D-2 fix 后重扩散）

复校日期：2026-11-11。venv：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0，FreeType 2.14.3）。生产目录只读；全部构建输出重定向至本 scratch；`PYTHONDONTWRITEBYTECODE=1`；TMPDIR 指向本 scratch 下 `tmp/`。开工探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` RC=0 + scratch 内真实写文件通过。

## 0. SHA 硬规则（开工核对 + 完工复核，两次全对）

| 件 | 字节数 | SHA-256 | 结果 |
|---|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-DE.pdf` | 14,037,210 | `7952f4ff3b957ecbbbdd8be5701237b2fe43824160575ee8bc217baedfa5c7b8` | ✓ |
| 网页 PDF `La-Lucerna-VOL4-DE-web.pdf` | 1,297,238 | `65e262903bd0ee8fa82fa2d575f6225ec01c815c5551451ec964ee448c9a1ac0` | ✓ |
| text.md `2026-w47-it-de.text.md` | 56,662（1317 行） | `de0aa214818e4ce2c25952323cd8cac781d72d89419130b2ffb96308dd2798c9` | ✓ |

源核心三 SHA 与 FANOUT-REPORT-it2 §2 逐字一致（印 `e1f89922…` / 网 `09f2ef66…` / 文 `9eb9ee06…`）；备份三 SHA 与 `shas-pre.txt` 逐字一致（印 `527b38ce…` / 网 `f9f4343b…` / 文 `36a11a8f…`）。

## A. D-2 回归（`verify` 自写检查，见正文 §2；日志见各小节行内）

- text.md diff（`diff backup text.md production text.md`）：恰 :775/:777 两行 replace；56,683→56,662（−21 B）。
- SVG/cards：p1–p6/p8 逐字节一致，仅 p7 不同（sha256 逐一比对）；content diff 仅 `content7.py:17/:18` 两行。
- p7 SVG 位置级文本节点 diff：仅两句换行碎片有变（节点索引 20–49 区间）。
- PDF 文字层（PyMuPDF，空白 + `→` 归一化后计数）：印/网 P7 新串 L17/L18 各 ×1、旧串各 ×0；全文档亦各 ×1/×0。旧串全版 live 文件 grep 0（仅 KIT §13 历史行各 1 次）。
- 全树 `diff -rq backup production`：恰 7 个文件不同（text.md、两 PDF、WEEKLY-KIT.md、cards/p7、content7.py、svg/p7）。

## B. fix1 回归（`verify_triple.py` + `scan_box_titles.py`，`verify-triple-prod.log` / `scan_box_titles_prod.log`）

| 缺陷 | PIL 真墨 | 96dpi 渲染像素 | 文字层 bbox（印/网） | 最紧值 |
|---|---|---|---|---|
| D1 P1 | +25.0（墨 936.0） | +28（固实 933；fix1 称 932，1px 阈值差） | +24.9（702.1pt → 936.1px） | **+24.9** |
| D2 P2 | +9.5（墨 951.5） | +11（固实 950） | +8.1（714.7pt → 952.9px） | **+8.1** |

- 旧串 0 次：`DIE WOCHE IN ZAHLEN`、`MERKSATZ` 在 svg + text.md + content12.py 均为 0；content12.py:44/:177 为新标题；translations.py de 值 L94/L563 已核。
- 29 奶油盒标题重扫：0 flags；最紧 D2 +9.5、P7 ERRORI TIPICI +13.8、P3 HINWEIS +19.2、D1 +25.0。
- 全节点奶油盒扫描（`creambox_allnode.py`，`out/creambox-allnode.log`）：29 盒 0 flags；全版最紧 P1 副标题 +5.8。

## C. P7 语义核查（独立检索，非引述 fix 员结论）

检索 `Italian futuro semplice andare irregular stem andr- leggerò regular future tense`（browser.search，2026-11-11）：LibreTexts《Indicativo futuro》不规则词干表列 andare → andr-，并以 leggere 作规则 -ere 动词例（io leggerò）；Dante Learning 规则表 parlare/leggere/dormire，andare 列入元音脱落不规则组（*anderò* 为错形）；FluentU：-ciare/-giare 动词丢 i 加未来时词尾，andare → andrò 列入不规则；FlexiClasses：andare → andrò 不规则。结论：L17 删 andare 规则例 ✓；L18 leggere 标 regolare ✓；assaggiare → assaggerò、guardare → guarderò 规则形 ✓。全版 `regolar`/`irregolare` 仅两行。

## 1. 重建（自写 `rebuild.py`：生产副本 → scratch `rebuild/`，OUT/BASE 重定向；`out/run.log`）

- run.py rc=0，TOTAL 150（A2 47 / B1 70 / B2 33）；页 10/18/18/18/18/18/12/38；范文 99 词；FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE = 0（grep 计数 0）。P4 col3 1140.45、P7 col3 1673.0、P8-ex col3 y=870、P8-keys col3 y=2514（底 2552）——与 KIT §8 逐项一致。
- render.py rc=0；SVG 8/8 字节一致。
- 重渲印 PDF 与交付件逐字节相同（SHA `7952f4ff…`，14,037,210 B）。

## 2. webpdf 重建

- 首次调用误传 print PDF 路径（`no SVGs in ...pdf`，rc=2）——用法错误，已纠正：`webpdf.py <svg_dir> <out_pdf>`。
- 纠正后 rc=0，1,297,244 B（与交付 1,297,238 B 差 6 B，符合“不可复现”预期）。
- 文字层印/网/重建三方原始文本逐字节相同（sha256 `538fe962f535d58ba288cbb3413130fdad5b03bcde28b4e62a0ca64410bb9476`，46,089 B）。

## 3. text.md 复导出（自写 `reexport_textmd.py`，`out/reexport.log`）

- 字节一致：56,662 B、1317 行、150 题，SHA `de0aa214…` 与交付一致。

## 4. freeze baseline + freeze diff（`out/freeze-baseline.log` / `out/freeze-diff.log` / `out/freeze-diff.json`）

- 首次调用误把 `--build` 指到 it-de 版（0/8，预期内：建的是版、比的是核心）——已纠正为 `--build <core-it>`。
- 纠正后 baseline：**8/8 字节一致 rc=0**；Pillow 13 守卫通过；core 完整性复核通过（core-it SVG 运行前后重哈希无变化）。build-copy 身份核实：含 `2026-w47-it-zh-cn.text.md`、`La-Lucerna-VOL4.pdf`（无 -DE 后缀），content12.py 中 `2026-w47-it-de` 出现 0 次——确为 core-it 自身，非版目录冒充。
- diff rc=0：P1 +30/−46、P2 +36/−29、P3 +35/−30、P4 +29/−26、P5 +44/−41、P6 +31/−25、P7 +43/−40、P8 +164/−629（与重扩散前逐项一致；纯拉丁 D-2 改动对 freeze diff 不可见，见 §A 的文字层检查）；新增 CJK 仅 13× U+3000（家具分隔符，豁免）。

## 5. occlusion audit（`out/occlusion-selftest.log` / `out/occlusion.log` / `out/occlusion.json`）

- selftest OK（6 类阳性对照全触发、干净对照静默）；生产 8 页 **0 flags**，rc=0。

## 6. p8 compare（`out/p8/`）

- extract 150/150 rc=0（版与核心各 150）。
- compare `--core-dir/--edition-dir --target it --total 150` rc=0，**CLEAN**，missing=[]、extra=0、keydiff=[137,138,139]。

## 7. gates.py 20/20（`out/gates.log`；`gates.py` 拷自 scratch-fanout-it，SCRATCH 重指本目录；`translations.py` 与 `validate_edition_textmd.py` 拷自 scratch-fanout-it，SHA 逐一核对一致）

- 首跑：19 PASS + 1 FAIL（`textmd validate`——本 scratch 当时缺 `validate_edition_textmd.py` 辅助脚本，工具缺失，非内容失败）；补拷验证器（SHA `ab2b0a78…` 与源头一致）后重跑：**GATES ALL PASS，20/20**。逐项见 `out/gates.log`（occlusion、p8、freeze diff 解释、strict-CJK、文字层多重集一致 7781 词、web <7MB、印 PDF 尺寸、P8 字号、纸色、无金/砖/近黑、VOL.5 ×3、VOL.4 ×9、徽章色、无双层外框、textmd validate 0/0、答案 150、键 1–150 除 137–139 外一致、notes 除 137–140 外一致）。
- 词数口径注记：gates 脚本（Python）计 7781 词；本轮 Python `split()` 计 7782（差 1，为计数器尾 token 处理差）；`wc -w`（POSIX locale）计 7276——C locale 下 wc 对多字节 UTF-8 词的计数 artifact。三方 pdftotext 输出字节逐字节相同（§2），词数差非内容差。

## 8. text.md 校验（`validate_textmd_v4.py`，`out/textmd-validate-v4.log`）

- 该脚本原样输出为 Counter 多重性差（358/909），非集合差——方法注记，不可直接引用。
- 本轮另算**集合差**：text.md 有、SVG 为 0 次的词恰 **10 个**——`key`（导出器标记）、`Aufgabe`/`Offene`（导出器注）、`attraversare:i`、`portare:i`、`piantare:noi`、`pregare:la`、`mangiare:la`、`vincere:ha`、`pareggiare:ha`（全角冒号无空格连接，SVG 中为拆分词）。**0 个新内容词。**
- SVG 有、text.md 为 0 次的词 133 个：裸数字题号、家具词、`[...]` 指令词（Einsetzen/Ins/übersetzen/Schreiben/Richtig/bilden）、冒号连接词的拆分侧。全部已解释。
- text.md 汉字 0 个、U+3000 ×106、全角冒号 ×14；禁词 Ucraina/Russia/Putin 0；“next Sunday”在 text.md 中 0 次。

## 9. 150 键核对（`out/keys-3way.log` / `out/keys-p8-vs-textmd.log`）

- 练习键 vs Risposte：0 实 mismatch（12 处表观差为配对题 `key-c` vs `c` 归一化 artifact；Q150 设计差）。
- Risposte vs core：147 逐字相同，仅 137–139 不同（德语重定向）。
- P8 印刷键 vs Risposte：0 mismatch，150/150。
- 8 金句：逐字在 core 与本版正文各 ×1（全文各 ×2），页码标注逐项核实。

## 10. 渲染像素验证（交付印 PDF，96dpi + 200dpi，`pages/`）

- 全页最右固实墨（96dpi）：P1 1861、P2 1862（y=1586）、P3 1861、P4 1861、P5 1862（y=602）、P6 1861、P7 1861、P8 1864（y=1375）——**与备份旧版逐页逐值相同**，无回归。
- P2/P5 最右行经 SVG 节点确认与 core 同值同构造（P2 y=1594 `Una festa, una giornata verde`；P5 y=603 Corot 图注），恰在边距，非缺陷。
- P8 家具行：PIL 1862.0；96dpi 渲染 1864；200dpi 渲染 1864.3（`crop-p8-furniture-wide.png`：末字 `e` 完整，红线贴其右缘）。
- P7 LETTERE 底：盒底 1673.0；PIL 真墨底 1672.92（+0.08px）；96dpi 渲染盒内最低固实墨行 1672（+1.0px；上一轮 1671/+2.0，1px 栅格阈值差，LETTERE 节点与备份逐字节一致）；y=1686 墨线为通栏分隔线（x 88..1861），非文字。
- P1 副标题：PIL +5.8，渲染最右 1855（+7）。

## 11. P8 字号（SOP §1.1，下限 9.75pt）

- 最小 13.0px = **9.75pt**（185 节点，即 RISPOSTE 键）；其余各页最小 15.5px（P6 17px）。达标。

## 12. §1.1 扫描（`out/style-scan.log`）

- 纸色 #fbfaf6 ×10；无金/砖/近黑（“gold”×3 全在 base64 图片串内）；VOL.4 ×9；VOL.5 ×3 全合法（P2 交叉引用、LETTERE 说明、VOL.5 预告栏）；徽章色 #5c6e30 ×44、#46581f ×380、#37402f ×39；“全页 rect”×8 均为无描边纸底；描边全页框 0 个。

## 13. 孤儿扫描（`out/orphan-scan.log`）

- 单字节点 470 个：**0 孤儿**。全部为结构项（徽章/题号/Einsetzen/kicker/日期标题）、栏中换行末词、或已接受项 P3-main 末行 `costruzioni.`（core 同节点同栏）。新增仅 D-2 换行碎片（P7 `assaggiare`/`→`/`guarderò.`，段内），非栏顶/栏底孤儿。

## 14. 目视检查（交付印 PDF 200dpi 全页 + 6 张标注裁图，`pages/`）

- 8 页全页图逐页目视：无溢出、无重叠、无裁切、无乱码（P1–P8 逐页要点见 PROOF-NOTE §8）。
- 标注裁图（红线=盒/页缘）：`crop-d1-title.png`、`crop-d2-title.png`、`crop-p7-a2.png`（D-2 两句逐字完整）、`crop-p7-lettere-bottom.png`（末行下行字母完整在盒内）、`crop-p8-furniture-wide.png`（末字 `e` 完整）、`crop-p1-subtitle.png`（末端与红线有空隙）。

## 15. 内容抽查（全文通读 text.md 1317 行 + 直播源）

- 意甲 11 轮 10 场比分与直播源 10/10 一致；24 球重算一致；积分表与报道一致。
- 星期核验（`TZ=Europe/Rome date -d`）：21 个日期与文中全部星期表述一致。
- BookCity 15 届/23–29日/主题/Whitehead/1360/2487/1164/443 与官方节目册逐项一致。
- Q83–86 算术正确（13−11=2、6+7=13）；范文 99 词（实数）；Q137–140 翻译逐句核对通过。

## 16. STRADDLE 裁决

- 29 盒标题 + 全节点扫描 0 flags；8 页最右墨与备份逐页相同；STRADDLE 不触发，无回归。

## 结论

**0 缺陷。结论 (a)：干净，可定稿。**
观察项 3 项（P8 家具行贴边、P7 LETTERE 盒底 +0.08px PIL、P1 副标题 +5.8px）：均在盒内/页内，字形完整，无裁切、无重叠。

## 工具局限 / 方法注记（本轮实录）

1. `tools/freeze.py diff` 与 `tools/p8.py compare` 对纯拉丁改动不可见（fix3 §6 已记，本轮复现）——D-2 靠文字层检查 + 导出 diff + 位置级 SVG 节点 diff 覆盖。
2. `validate_textmd_v4.py` 输出为 Counter 多重性差（358/909），须另算集合差（恰 10 个已解释词）才可作证据。
3. `wc -w` 在 POSIX locale 下对 UTF-8 文本少计约 500 词（7276 vs Python 7782）；词数以 Python 计数 + 字节哈希为准。
4. 首跑 freeze baseline 与 gates 各有一次本轮操作失误（`--build` 错指版目录；gates 缺辅助脚本），均已纠正重跑，终值以纠正后为准；失误均未写生产。
