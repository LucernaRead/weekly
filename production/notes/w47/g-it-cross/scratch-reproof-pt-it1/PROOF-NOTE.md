# PROOF-NOTE — 2026-W47 pt-it（葡萄牙语目标、意大利语读者版）— re-proof（fix1 后独立复校）

- Proofreader: independent re-proof（subagent reproof-pt-it1）
- Date: 2026-11-11（UTC；任务 12:28 EST 下达）
- Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-pt-it1/`
- Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-pt-it/`（生产目录零写入；全部重渲染只在 scratch 内 build-copy；NO commit、NO push）
- 对照：proof1（`scratch-proof-pt-it2/PROOF-NOTE.md`，D1–D6）与 fix1（`scratch-fix-pt-it1/FIX-LOG.md`、`GATE-LOG.md`，仅 D6）
- 工具：`tools/venv/bin/python` 全程；TMPDIR 指本 scratch `tmp/`；pt 适配脚本（`check_s11_pt.py`、`boxtitle_ink.py`、`pixel_boxtitle.py`、`keycheck.py`、`sweep_all.py`、`sweep_text.py`）自本 scratch 内新写/复核，en 族原版未动；`nota_ink.py`、`text_coverage.py`、`text_coverage2.py` 为本轮新写；creambox 用 canonical `hidden_files/w47/tools/creambox.py`。

## §0 身份核对（磁盘为准，开工与收工两次核对一致）

| 文件 | 磁盘 SHA-256 | 字节 | 与任务一致 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | `75fd3847bc5c4f0a8cab338e2e78a632463bc8f4e19e838c00026c34cf9ff67c` | 12,930,798 | ✓ |
| `A-Lucerna-VOL4-web.pdf`（网） | `a0ccd14c0c51411b37d0733bb21b14f143ad84c04d7212d15319e560f8a670fd` | 1,137,048 | ✓ |
| `2026-w47-pt-it.text.md` | `37c1980caacc6cef28d9df50133b09b45a51a8d4f17296e34412b2cd88285209` | 37,419 | ✓ |

三文件 SHA 与任务完全一致；收工复验未变。生产目录 `git status` 仅见整目录未入库（`??`），无任何已跟踪文件修改。

## 结论：(a) 零缺陷，可定稿

- **D6 已修并通过双重验证**（见下 §1）：PIL 真墨 clear **+83.5**，交付印/网 PDF 300dpi 像素 clear **+82.6**，均 ≥ +5px 标准；300dpi 裁图目视标题整行收进奶油框内。
- **其余 7 页 SVG 与 proof1 修前逐字节相同**（仅 p2 变化 `dbbb6bcc…` → `1ccd77e4…`；P1 哈希 `38041cab…` 与 FIX-LOG 宣称的修前值一致，零改动）。
- **全部门禁独立重跑全绿**（详见 GATE-LOG）：run.py rc=0 TOTAL 150；重建 SVG 8/8 字节一致；gates 16/16；occlusion 0 flags（阳性自检 6 类全触发）；p8 extract 150/150、compare CLEAN（keydiff [137,138]）；印/网文字层各 110,388 字节逐字节相同；freeze 核心基线 8/8 + 版内自比对 8/8，新增 CJK 仅 U+3000 ×9；P8 最小字号 9.75pt（= SOP §1.1 下限）；31 盒标题真墨全在框内（最紧 +3.5）；150 题逐题手验 149/150 PASS + Q150 开放写作 ✓。
- **D1–D5 全部存活**（见 §3，实测值与 proof1/fix1 逐字一致）。
- **D7（已撤销）未列为缺陷**：`tables_it.py:201` 与 `content12.py:15` 仍为原标语「Il portoghese che legge il Brasile」（P1 顶栏目视确认），符合协调员裁定。
- 观察项 O-NEW（见 §4）：两处 text.md 独有行，全 pt 族 11 版系统性共有、proof1 已有、非 fix1 引入、交付 PDF 本体无问题——记观察、不阻塞定稿。

## §1 D6 复测（P2「PARA NÃO ERRAR」框标题）

- 定位：P2 第二栏奶油框 `x[538.5,961.0] y[605.02,846.02]`；标题「PARA NÃO ERRAR　La regola」基线 y=642.02，fs=23 粗体，x=556.5。
- 源码行：`content12.py:183`（`f.box("PARA NÃO ERRAR　La regola", [`）；gloss 源 `tables_it.py:58`（`"口诀": "La regola"`）——两处均为修后值。
- 实测（双法一致；另见 GATE-LOG §2/§5）：
  1. PIL 真墨（`boxtitle_ink.py`，svglib `_pil`/`_runs`，fs=23 自身字号）：墨右 **877.5**，框右 961.0，clear **+83.5**（修前 −59.5）。
  2. 交付**印 PDF** 300dpi 像素（`pixel_boxtitle.py`，PyMuPDF）：墨右 **878.4**，clear **+82.6**；交付**网 PDF**同法同值 +82.6。
  3. 目视：300dpi 原生裁图 `crop-p2-PARA-NAO-ERRAR.png`——「PARA NÃO ERRAR　La regola」整行收进奶油框内，右缘余量肉眼清晰；P2 整页图 `view-p2.png` 同处无漫出。
- 结论：修后标准（PDF 渲染像素离盒边 ≥ +5px）达成，余量 +82.6。**D6 已修 ✓。**

## §2 其余 7 页 SVG 逐字节比对（vs fix1 `svg-pre.sha`，即 proof1 交付态）

| 页 | 修前（proof1） | 现盘 | 结论 |
|---|---|---|---|
| p1-capa | `38041cab…` | `38041cab…` | 相同 ✓ |
| p2-vida | `dbbb6bcc…` | `1ccd77e4…` | 唯一变化页（D6） ✓ |
| p3-cultura | `c8b0998f…` | `c8b0998f…` | 相同 ✓ |
| p4-esporte | `aa12aac5…` | `aa12aac5…` | 相同 ✓ |
| p5-jovens | `c2be1a20…` | `c2be1a20…` | 相同 ✓ |
| p6-aprofundamento | `3a39cddd…` | `3a39cddd…` | 相同 ✓ |
| p7-lingua | `d60e6a2f…` | `d60e6a2f…` | 相同 ✓ |
| p8-avaliacao | `f0038894…` | `f0038894…` | 相同 ✓ |

与 FIX-LOG 宣称一致：仅 `svg/p2-vida.svg` 变化，其余 7 页字节不变，无意外改动。另：scratch 内重建 8 张 SVG 与交付 SVG 逐字节一致 8/8（`svg-rebuild.sha`）。

## §3 proof1 缺陷复验（D1–D5 全部存活，未被 fix1 误伤）

| 项 | 本轮实测（自交付 SVG / 交付 PDF） | 结论 |
|---|---|---|
| D1 P1「EM POUCAS PALAVRAS」框 | 框底 **2348.0**，末行「em Brasília. (Página 4)」基线 2327.6，clearance **+20.4**，desc-clear +14.4；全页目视末行在奶油底上 | 存活 ✓ |
| D2 P3「A SEMANA, DIA A DIA」框 | 框底 **551.0**，末条「16h30.」基线 540.6，clearance **+10.4**，desc-clear +3.9 | 存活 ✓ |
| D3 P6「O CAMINHO ATÉ O GABARITO」框 | 框底 **854.0**，末行「Página do Participante.」基线 840.8，clearance **+13.2**，desc-clear +6.9；全页目视末行在框内 | 存活 ✓ |
| D4 P7「A PALAVRA」标题 | 「A PALAVRA　La parola」（fs=23）；PIL 真墨 clear **+151.5**，印/网 PDF 像素 **+151.0** | 存活 ✓ |
| D5 P1「NESTA EDIÇÃO」标题 | 「NESTA EDIÇÃO　Questo numero」（fs=24）；PIL 真墨 clear **+23.5**，印/网 PDF 像素 **+21.7** | 存活 ✓ |

## §4 观察项（不计缺陷，不阻塞定稿）

### O-NEW — text.md 两行在渲染 SVG 中无对应（全 pt 族系统性共有，proof1 已有）

- **L11**：text.md 第 11 行「O JORNAL SEMANAL PARA APRENDER — O BRASIL DE VERDADE, EM PORTUGUÊS, DO BRASIL」不在 it 版 P1 SVG 的任何文本节点中（core-pt P1 SVG 有此行，x=633.7 y=372 fs=16；fan-out 时该槽位被读者语行「TESTI IN PORTOGHESE　SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI」取代）。核查：pt-fr/pt-es/pt-de/pt-nl/pt-ru 五版 text.md 皆含此行各 1 次、P1 SVG 皆无——11 版同 pattern。属 text.md 导出层系统性残留，非本版独有、非 fix1 引入；交付 PDF 本体无此问题（该行是报纸自身的葡语标语，印在网站正文里亦无事实错误）。
- **L3**：text.md 第 3 行副标题「Settimana dal 16 al 22 novembre 2026 · Testi in portoghese · Spiegazioni in italiano · Livelli A2–B2 · 150 esercizi」中「Livelli」「esercizi」两词不在 P1 SVG 中——此为 text.md 题头元数据行（刊期/语种/级别/题数汇总），非正文段落，渲染版以徽章与分版标注呈现同信息。
- 裁定：两处皆为 program 级 text.md 导出口径问题，应由协调员在全族层面定夺是否改导出逻辑；不作为本版缺陷，不修本版。本轮以 `text_coverage2.py`（散文段逐词袋检验）核实：除上述两行外，text.md 全部散文段的标志词均在其对应页 SVG 中（>90% 覆盖）。
- 注：初版粗查 `text_coverage.py`（全文展平词序比对）报 188 行缺失，系方法伪报——pdftotext 跨栏打乱词序 + 填空线/选项标点所致，已废弃，不作证据。

### O-OLD（proof1 已记录，本轮只确认、不判）

- **拉丁解释层字体**（Noto Sans CJK SC）：已知待用户裁定，不判缺陷。
- **P8 注行墨右 +0.4**（0.5 边际带内，proof1 实测）：非缺陷。
- **P3 中段留白、P5 中段留白**：核心固有排版（正文栏短于版面），非本版引入。

## §5 核实摘要（本轮独立实测，非复述 KIT/FIX-LOG）

- 全文通读：印 PDF 8 页逐版看图（`view-p1.png`–`view-p8.png`，110dpi）+ text.md 534 行逐行读；除 §4 观察项外无文字、事实、日期、编号、级别问题。星期核验（`date -d`）：2026-11-07 周六、11-20 周五、12-06 周日，与文中「sábado 7」「sexta 20」「6 de dezembro」一致；11-16..22 为周一..周日；工作日算术复核无误（16–30 共 15 天 = 10 工作日 + 5 周末/假日；第 10 个工作日 = 11 月 30 日）。
- 150 题：机械四源 0 不符（`keycheck.log`）；逐题手验（`keycheck-150.txt` 750 行逐行读完）**149/150 PASS + Q150 开放写作 ✓**；Q73「espera」与 Q70「gabarito」各配各题无误；Q137/Q138 为设计内读者语差异（意大利语译文正确）；Q139/Q140 意葡互译正确；Q146/Q147（Grêmio 争第六冠、Palmeiras 争第五冠）与 P4 正文一致；范文 88 词（`len(split())`=88，80–100 范围内）。
- P7 八句本周短语逐字出自本期正文（P1 标题/导语、P3、P4、P5、P6、P2 各句），意译 + 页码标注齐全；读者来信披露（VOL.3 未到、顺延 VOL.5）意译 3 行齐全；P1 头条 41 非空字符 ≤56。
- 31 盒标题逐一真墨检查：26 粗体标题（`boxtitle-ink.log`）+ 5 Nota 盒顶行（`nota_ink.py` 新写独立量测）全部 clear > 0；最紧为 P1「EM POUCAS PALAVRAS」+3.5（PIL）/+3.1（PDF 像素），在框内。
- creambox：31 盒；5 处 BELOW-WINDOW 负值皆为盒外章节标题/家具行（与 proof1/fix1 同值同裁决，`creambox.log` 与 fix1 版逐字节相同）；6 处 desc-clear 负值（−0.9~−1.5，行内无降部字母，proof1 已真墨迹复验余量 +4.5~+5.4）；sweep-all 盒内 H-OVER 0 处，6 组旗标皆盒外（与 fix1 同值同裁决）。
- 引号/CJK/禁词（`sweep-text.log`）：弯引号成对（« » 40/40；U+201C/U+201D 各 2；U+2019 仅 P1 徽标 1 处）；CJK 仅 U+3000；渲染文本（print.txt/web.txt）禁词 0、简体残留 0。
- D7 标语验证：`tables_it.py:201` 与 `content12.py:15` 均为原句「Il portoghese che legge il Brasile」；P1 顶栏目视确认原句在位；**绝不列为缺陷**（协调员已裁定语法正确）。
