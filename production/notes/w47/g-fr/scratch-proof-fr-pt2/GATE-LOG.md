# GATE-LOG — W47 fr-pt 独立校对 proof1（re-fanout #2）

复校员：独立校对（与重建者不同人）。日期：2026-11-11。
目标：`production/2026-w47/2026-w47-fr-pt/`（re-fanout #2 重建版，VOL.4）。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-pt2/`。
生产目录零写入；core-fr 只读；全部重建在 scratch 副本（`pt/rerun/`、`build-copy/`、`freeze-baseline/build-copy/`）中进行；全部 venv python 运行均加 `PYTHONDONTWRITEBYTECODE=1`；TMPDIR 为本 scratch 下 `tmp/`。

## 0. 探针与身份核对

- `ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 通（`9daeafb9…`）。
- 磁盘 SHA（实测，与任务书逐一核对一致）：
  - 印刷 PDF `La-Lucerna-VOL4-fr-pt.pdf`：17,420,030 B，`420d79e71cc02859a5d9c8fa94c1b09ea7ae4f786c22911a4d8d2a3e7ed95521`
  - 网页 PDF `La-Lucerna-VOL4-fr-pt-web.pdf`：1,702,371 B，`fb88ae09d19a9b66906df2865ec15529c9f09429de22e690fbcc252ac5eff6b1`
  - `2026-w47-fr-pt.text.md`：46,536 B（1,088 行），`172f28dc192ea023b64bffb3e84f8a7106b4ff46f9db11a6a5d08d0f6b9efbdd`

## 1. run.py 确定性重建（门禁 1）

- scratch 副本 `pt/rerun/` 运行 run.py：rc=0，TOTAL 150；by level A2 53 / B1 75 / B2 22；by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42}；零 `FLOW OVERFLOW` / `HEAD TOO WIDE` / `NOSPACE`（`build-proof2.log`）。
- 重建 SVG 与现盘 8/8 字节一致：`a8ca67ea, 1c7f056e, 13a8fe0a, d9b6af38, 2a66a9f0, 5ef9766c, c3419d55, 34bf3311`（另一次独立重建于 `build-copy/`，gates 门 freeze_direct 亦 8/8，见下）。

## 2. freeze（门禁 2）

- 标准核心比对（`tools/freeze.py baseline --build . --core-svg svg`，在 `core-fr` 目录内运行，`--out` 指本 scratch 的 `freeze-baseline/`）：rc=0，**8/8** 字节相同；核心 SVG 跑后重哈希未变（`freeze-baseline.json`、`freeze-baseline.log`）。`--build` 指核心目录本身（core-fr），`--core-svg` 指核心 svg 目录——路径正确，证据有效。
- `freeze.py diff`（核心 svg vs 本版 svg）：8/8 页；新增 CJK 合计 11，全部为 U+3000（p2 ×1、p8 ×10，其余 0；结构分隔符，无汉字/假名/韩文）。逐页：p1 +25/−23、p2 +38/−33、p3 +36/−44、p4 +45/−49、p5 +41/−42、p6 +30/−30、p7 +41/−34、p8 +123/−123（`freeze-diff.json`、`freeze-diff.log`）。freeze 只做 CJK 核算，纯拉丁改动另由 string_freeze 门覆盖（见 §3）。
- 相对首轮（fr-pt1）的源码 diff：`expl.py` 恰 1 行（披露框中间句删除）、`content8.py` 恰 2 行（Q148 键与题干），其余源码全部相同；SVG 逐字节：仅 P7（`c3419d55`）与 P8（`34bf3311`）变化，其余 6 页与首轮相同。

## 3. 机械门禁 15/15 PASS（gates.py，`pt proof2`，rc=0）

`pt/gates-proof2.json`，`pt/gates-proof2.log`：

| 门 | 结果 |
|---|---|
| run | PASS — exit 0，零 overflow/wide；TOTAL 150；by level A2 53 / B1 75 / B2 22；by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42} |
| occlusion | PASS — 0 flags，selftest OK（真实审计命令，非 `--selftest`；`pt/occlusion-proof2.json` 本体：`flag_count: 0`，`flags: []`） |
| p8_extract | PASS — keys 150/150，printed notes 121/150 |
| p8_compare | PASS — CLEAN，keydiff [150]（仅写作题键）。直接读 `pt/p8compare-proof2.json` 本体：`status: CLEAN`，`keydiff: [150]`，core/edition note 集各 121 枚且相同，missing/extra/uncertain 均为 [] |
| source_freeze | PASS — content/bslib/svglib/run 与核心字节相同；render.py 仅 BASE+PDF 名不同 |
| string_freeze | PASS — 核心非 CJK 串逐页存活；0 核心 E 残留；0 未入账 CJK；1 条翻译豁免（核心 `stem_e1` 前缀 `Traduisez : `） |
| freeze_direct | PASS — `build-copy/` 独立重建，8/8 SVG SHA 全同：`a8ca67ea, 1c7f056e, 13a8fe0a, d9b6af38, 2a66a9f0, 5ef9766c, c3419d55, 34bf3311` |
| text_layer | PASS — 印/网 pdftotext 逐字节一致（104,688 B）；网 1,702,371 B < 7MB；印 17,420,030 B |
| p8_font | PASS — P8 最小字号 **11.625pt** ≥ 10pt（任务门限；SOP 门限 9.75pt 亦过） |
| scans | PASS — U+2019=0，U+00B7=0，gold=0，旧纸色=0，#fbfaf6 ×8 |
| chips | PASS — 134 枚 [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck | PASS — 150 键对核心 `final-fr-p8.json`，仅 Q150 不同（`Pergunta aberta`） |
| mcq | PASS — bodies: 45，rendered lines: 1482，0 缺陷 |
| widths | PASS — 31 条单行串全部在预算内 |
| band_spans | PASS — 法文标题止 1236.9，band_r1 起 1270.9，法文副标题止 837.2，band_r2 起 1489.2 |

## 4. creambox（规范版，8 页）与溢出横扫（门禁 7）

`hidden_files/w47/tools/creambox.py` 扫 8 个 SVG（`creambox-proof2.log`；核心版对照 `creambox-core.log`），7 条 BELOW-WINDOW，逐条裁定：

| # | 盒 | BELOW-WINDOW | 裁定 |
|---|---|---|---|
| 1 | P1 y=1280 bottom=1652.0 | +24.0 `LE MOT DE LA SEMAINE` | 假阳性——下一栏目标题；盒内末行 clearance +48.0 |
| 2 | P2 y=886 bottom=1090.8 | +37.0 `LA SEMAINE EN CHIFFRES` | 假阳性——下一栏目标题；盒内 +47.7 |
| 3 | P3 y=200 bottom=375.4 | +37.0 `À VOUS !　A TUA VEZ!` | 假阳性——下一框标题；盒内 +47.7 |
| 4 | P4 y=200 bottom=405.1 | +37.0 `À VOUS !　A TUA VEZ!` | 假阳性——下一框标题；盒内 +47.7 |
| 5 | P5 y=2182 bottom=2387.4 | +37.0 `À VOUS !　A TUA VEZ!` | 假阳性——下一框标题；盒内 +47.7 |
| 6 | P6 y=463 bottom=820.3 | +37.0 `IL EST PRÉVU QUE + SUBJONCTIF` | 假阳性——下一栏目标题；盒内 +48.5 |
| 7 | P6 y=1330 bottom=1656.7 | +37.0 `LE DÉBAT　DEBATE` | 假阳性——下一栏目标题；盒内 +48.5 |

- **P7 披露框（首轮 D-1 修复复验）**：盒 y=1878 bottom=2258.0，末基线 **2233.3**，inside-only clearance **+24.7**，desc-clear +18.8——与核心版同盒逐值相同，溢出已修净（首轮为 BELOW-WINDOW +2.6）。
- P2 `ET VOUS ?` 盒（y=974 bottom=1308.6）：末行基线 1304.2，clearance +4.4，desc-clear −1.6；核心版同盒 desc-clear −2.2（更紧）——核心继承，不列缺陷。
- P1 agenda 盒（y=588 bottom=1256.0）：末行 clearance +8.0，desc-clear +2.3，与核心版逐值相同。
- 注：首轮 PROOF-NOTE §4 称 P5 盒 bottom=2357.7 为笔误；首轮 `creambox.log` 第 216 行实为 bottom=2387.4，与本轮一致。

## 5. P7 PIL 真墨测量（门禁 6 的一部分，250 dpi）

`pil_p7.py` / `pil_p7b.py`，日志 `pil-p7-proof2.log`（印刷版 PDF P7，clip pt (740,1400,1400,1710)）：

- 校准：垂直扫描 x_svg=1250：奶油 render 色 (239,237,228)（SVG #f0eee5 经 PDF 转换差 1），纸白 (251,249,246)；奶油末行 svg **2258.3** ≈ 盒底 2258.0。
- 披露末行真墨末行：svg **2237.6**（任务复验要点约 2237.3，差 0.3，250 dpi 像素量化内）。
- 间隙 2258–2269：**零墨**；2258.3 起为纸白；svg 2270.0 起为下一栏深绿带（`LA SEMAINE PROCHAINE` 矩形顶，y=2270，墨色 (132,137,126) 为带边抗锯齿）——非溢出。
- 目视：`png/crop-p7-mailbox-300dpi.png`（300 dpi），末行 `promessa de comentar envios reais.` 完整在盒内，盒下留白干净。

## 6. spill / boxtitle 真墨扫描（门禁 6）

`spill_boxtitle.py`（`spill-boxtitle-proof2.log`）：33 盒；盒底 +60 px 内盒外行 11 行全为粗体标题（HEADING），正文续行溢出 **0**；33 盒标题 PIL 真墨溢出 **0**（28 盒有粗体标题行，全部水平/垂直在盒内）。**SPILL/BOXTITLE PASS**（已排除整页纸底 rect，避免空转）。

## 7. check_extra：孤儿 / 填空行 / Q148（门禁 3、5、8）

`check_extra.py pt proof2`（`pt/extra-proof2.log`、`pt/extra-proof2.json`），rc=0，**EXTRA PASS**：

- 孤儿标点元素：total=0，new=0，inherited=0，remnant=0，shared_baseline=0（共享基线规则已启用；旧真孤儿 0，本版无新增）。
- 填空行：3 条，与核心同构——P8 (989.0, 843.0) 与核心一致；P3 两行 x=538.5，y=1924.1 / 2056.8，核心 y=1864.7 / 1997.4（+59.4/+59.4，约 +59.5 档，只记录不判）。
- Q148：stem_ok（P8 SVG 有 `On se retrouve` 与 `cinéma ?`，无 `du cinéma`）；key_in_content8（`content8.py:170` `"devant le"` + 题干 `On se retrouve ({gnums[3]})___ cinéma ?`）；extracted=`devant le`。

## 8. check_s11（门禁 4）

`check_s11_pt.py`（fr 改编版；`check-s11-proof2.log`）：**36 项 PASS**，含 8 页纸色 rect、VOL.4、徽章 rect 数与色集、色集与核心一致（无新增 fill）、无金/旧纸色、P8 最小字号 11.625pt。**CHECK_S11 PASS**。

## 9. verify_ed（重建版专属复验）

`verify_ed_pt.py`（`verify-ed-proof2.log`）：**25 项 PASS**，rc=0。**VERIFY_ED PASS**：

- D1：披露中间句 `por isso publicamos um exemplo da redação claramente indicado` 已从 expl.py 与 SVG 消失；披露为 2 行式（`o VOL.5 cumprirá a promessa de comentar envios reais.`）；P7 披露盒末基线 2233.3。
  - 注：首版脚本用整句跨行子串匹配 SVG，误报 1 项 FAIL（句子在 SVG 中分两行 `o VOL.5 cumprirá a` / `promessa de comentar envios reais.`）；已修正为两分片分别匹配后重跑，全 PASS——属检测器伪影，非版面问题。
- D2/D3（pt 词表）：`une actrice — atriz` / `une séance — sessão` 在 expl.py、P5 SVG、text.md、印刷文字层四处皆有；`uma actrice` / `uma séance` 三处皆无。
- Q148：registry、`content8.py`、P8 extract 三重均为 `devant le`；P8 SVG 题干无 `du cinéma`。
- text.md：答案块解析 150 键；除 Q150（散文键）外与 registry 逐项一致；Q148 答案 `devant le`；Q150 答案以 `Pergunta aberta` 开头；CJK 0；U+2019=0；U+00B7=0。

## 10. 150 题逐题手验（门禁 5）

`key-stem-check.txt`（registry 键/注记 + text.md 题干逐题对照；配对题另取 `content*.py` 的 `match_set` 左右列；对话题取 P8 SVG 对话全文）：**150/150 适配**。要点：Q83=C 三重核对（核心键 C、P8 印出 `83. C (Votação solene 9 dez.)`、P6 日历 `9 déc. Vote solennel : le budget de l'État`）；Q130–139 翻译/改写五组逐句验（Q137 `depuis lundi`、Q138 `préparer nos affaires`、Q139 `On ne connaît pas encore les résultats` 均与葡语题干语义一致）；Q140–144 配对 a–e 逐对验；Q145–149 对话逐句验（Q148 填入后为 `On se retrouve devant le cinéma ?`，语法成立）；Q150 写作题例外。详见 PROOF-NOTE §6。

## 11. 文本扫描（门禁 8）

- text.md（1,088 行，46,536 B）：`«` 74 / `»` 74，成对，零不平衡段落；直引号 `"` 0；U+2019=0；U+00B7=0；CJK 0；`Dont` 0；禁查词（乌克兰/俄乌/战争/台湾/简体/繁体）0。
- ABSTRACT.txt：233 B，一行葡萄牙语，内容准确（Alcaraz / Senado / Beaujolais 75 周年 / 150 题 / 16–22 nov.）。
- MODÈLE：96 词（80–100 要求内）。
- P7 八句金句：8/8 逐字出自 P1–P6 正文（脚本核对）。
- D5 字体普查（只记录，不判）：SVG 8 页 Newsreader 947 / Noto Sans CJK SC 691 / Noto Serif CJK SC 74（57 段仅为空白分隔符）/ DejaVu Sans 4 / UnifrakturMaguntia 1；Noto Sans CJK SC 段中 565 段含拉丁字母且无 CJK 表意/假名/韩文——葡语讲解层落在 Noto Sans CJK SC，全周级待定项，见 PROOF-NOTE R2。

## 12. 目视

- 印刷版 PDF 100 dpi 全页 `png/p1.png`–`png/p8.png`：除记录项外零问题（见 PROOF-NOTE §5）。
- 网页版抽查：`png/web-p1.png`、`png/web-p7.png`——与印刷版同版式，P7 邮箱盒同样修复。
- 裁图：`png/crop-p7-mailbox-300dpi.png`（300 dpi，D-1 修复处）。

## 13. 结论

**(a) 零缺陷可定稿。** 记录项 R1–R4（见 PROOF-NOTE §7）均不计入 (a) 判定：R1、R3、R4 为核心继承（首轮既有观察类），R2 为全周级待定项。
