# GATE-LOG — 2026-W47 pt-it re-proof（fix1 后独立复校）

- Proofreader: independent re-proof（subagent reproof-pt-it1），2026-11-11（UTC）
- Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-pt-it1/`
- Tooling: `~/workspace/weekly-git/tools/venv/bin/python` 全程；`TMPDIR` = 本 scratch `tmp/`。
- 交付三 SHA（开工与收工两次核对一致）：印 `75fd3847bc5c4f0a8cab338e2e78a632463bc8f4e19e838c00026c34cf9ff67c` / 12,930,798；网 `a0ccd14c0c51411b37d0733bb21b14f143ad84c04d7212d15319e560f8a670fd` / 1,137,048；text.md `37c1980caacc6cef28d9df50133b09b45a51a8d4f17296e34412b2cd88285209` / 37,419。
- Creambox canonical：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`。

## §1 机械门实跑证据（全部自己跑，生产目录零写入）

| 门 | 命令 / 口径 | 结果 | 日志 |
|---|---|---|---|
| run.py（scratch build-copy） | `python -u run.py`（副本内，源与生产目录同文件） | **rc=0，TOTAL 150**（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38；范文 88 词）；0 OVERFLOW / 0 TOO WIDE | `run-copy.log` |
| 重建 SVG 比对 | 重建 8 张 SVG sha256 vs 交付 SVG | **8/8 逐字节一致** | `svg-rebuild.sha` |
| gates.py（build-copy） | `python -u gates.py` | **16/16 PASS，FAILURES: none**（`[PASS]` 16 行，`[FAIL]` 0 行） | `gates.log` |
| occlusion 真实审计 | `tools/occlusion_audit.py production/2026-w47/2026-w47-pt-it/svg --json occlusion.json` | **0 flags**（`flag_count: 0`；工具内置自检 `selftest OK: planted classes fired {BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX}` 6 类全触发，干净对照静默） | `occlusion.log`、`occlusion.json` |
| p8 extract（版） | `tools/p8.py extract --p8 .../2026-w47-pt-it/svg/p8-avaliacao.svg --total 150 --json p8-extract.json` | **150/150 noted** | `p8-extract.log`、`p8-extract.json` |
| p8 extract（核心） | 同上，core-pt P8 | **150/150 noted** | `p8-extract-core.log`、`p8-extract-core.json` |
| p8 compare | `tools/p8.py compare --core-p8 ../core-pt/svg/p8-avaliacao.svg --edition-p8 svg/p8-avaliacao.svg --total 150` | **CLEAN**（missing=[] extra_count=0 uncertain=[] **keydiff=[137, 138]**） | `p8-compare.log` |
| freeze baseline（核心） | `tools/freeze.py baseline --build production/2026-w47/core-pt --core-svg production/2026-w47/core-pt/svg --out freeze-core` | **8/8 SVGs byte-identical**（repointed: none；core 完整性：8 文件复哈希未变） | `freeze-core.log` |
| freeze baseline（版内自比对） | `... baseline --build production/2026-w47/2026-w47-pt-it --core-svg .../2026-w47-pt-it/svg --out freeze-ed` | **8/8 SVGs byte-identical**（repointed: none） | `freeze-ed.log` |
| freeze diff | `tools/freeze.py diff --core-svg ../core-pt/svg --edition-svg svg --json freeze-diff.json` | rc=0；新增 CJK 字符仅 **U+3000，共 9 个**（P1 2 个、其余每页 1 个） | `freeze-diff.log`、`freeze-diff.json` |
| 印/网文字层 | `pdftotext -layout` 两版 + `cmp` | 各 **110,388 字节，逐字节相同**（`cmp` 无差异） | `print.txt`、`web.txt` |
| P8 最小字号（PDF） | PyMuPDF 取印/网 P8 全部 span | **9.75pt**（P8 390 spans；全文档最小亦 9.75pt），印/网一致；**= SOP §1.1 下限**（任务口径 ≥9.75pt 一致） | `p8-fontsize.log` |
| check_s11（pt 改编版） | 自 scratch 的 `check_s11_pt.py`（en 原件未动） | **ALL §1.1/P8 CHECKS PASS**（rc=0）：8 页纸底 `#fbfaf6` 齐全；色集 core=edition=21 色，extra/missing 皆无；VOL.4/VOL.5 逐页计数与 core 一致；徽章 8 页逐页同数同色（10/15/18/15/18/18/12/35 = 141 枚）；P8 SVG 最小字号 13.0（= 9.75pt）；P8 题号 113–150 齐全；H 头 `ESCREVA VOCÊ`、`Scrittura`、`✓` 齐全 | `check_s11.log`、`check_s11_pt.py` |
| creambox 全版扫描 | canonical `creambox.py svg/*.svg` | 31 盒；除已裁决假阳性外 **0 真溢出**（见 §4；日志与 fix1 版逐字节相同） | `creambox.log` |
| boxtitle 真墨（31 盒全量） | `boxtitle_ink.py`（PIL，自身字号，26 粗体标题）+ `nota_ink.py`（本轮新写，5 个无粗体标题的 Nota 盒顶行）+ 交付 PDF 300dpi 像素复验（印/网） | **0 溢出**；D6 +83.5（PIL）/+82.6（PDF）；最紧 P1「EM POUCAS PALAVRAS」+3.5；全部 31 项见 §2 | `boxtitle-ink.log`、`nota-ink.log`、`pixel_boxtitle.log`、`pixel_boxtitle_web.log` |
| 溢出横扫 | `sweep_all.py`（每奶油盒 × 盒列 ±60px 窗口内全部文本，真墨迹量横/纵向） | 盒内 H-OVER **0 处**；其余旗标皆为盒外章节标题/正文（见 §4，与 fix1 同值同裁决） | `sweep-all.log` |
| 150 题手验 | `keycheck.py`：印刷键 × 核心键 × text.md 行内答案 × Respostas 汇总 四源比对 + 逐题读题干配对 | **机械 0 不符**；逐题手验 **149/150 PASS + Q150 开放写作 ✓** | `keycheck.log`、`keycheck-150.txt`、`keycheck-150.json` |
| 引号/CJK/禁词 | `sweep_text.py`：SVG 文本节点 + text.md + 印/网 pdftotext | 弯引号成对（« » 40/40；U+201C/U+201D 各 2；U+2019 仅 P1 徽标 1 处）；CJK 仅 U+3000；渲染文本禁词 0；简体残留 0；非省略号 `..` 0 | `sweep-text.log` |
| text.md 散文覆盖 | `text_coverage2.py`（本轮新写）：散文段标志词 vs 其对应页 SVG 词袋 | 除 2 行 text.md 独有行（见 PROOF-NOTE §4 O-NEW）外全部 >90% 覆盖 | `text-coverage2.log` |
| 逐页看图 | 交付印 PDF 110dpi 全页 P1–P8 + P2 D6 盒 300dpi 裁图 | 8 页无溢出/重叠/压页脚；D6 标题已收进框内（`crop-p2-PARA-NAO-ERRAR.png`）；P1 顶栏原标语在位 | `view-p1.png`–`view-p8.png`、`crop-p2-PARA-NAO-ERRAR.png` |

## §2 31 框标题 clear 全表（PIL 真墨，自身字号；框右为 clear 基准）

26 个粗体盒标题（`boxtitle-ink.log`）+ 5 个 Nota 盒顶行（`nota-ink.log`，fs=20.5，sans）；全部 clear > 0，无溢出。

| # | 页 | 框标题 / 盒顶行 | fs | 框右 | 墨右 | clear |
|---|---|---|---|---|---|---|
| 1 | P1 | A SEMANA EM NÚMEROS　In cifre | 23 | 1411.5 | 1383.0 | +28.5 |
| 2 | P1 | A SEMANA, DIA A DIA | 27 | 1862.0 | 1732.5 | +129.5 |
| 3 | P1 | NESTA EDIÇÃO　Questo numero（D5） | 24 | 1862.0 | 1838.5 | +23.5 |
| 4 | P1 | EM POUCAS PALAVRAS　IN BREVE（全版最紧） | 24 | 1862.0 | 1858.5 | +3.5 |
| 5 | P2 | **PARA NÃO ERRAR　La regola（D6，已修）** | 23 | 961.0 | 877.5 | **+83.5** |
| 6 | P2 | VOCÊ SABIA? | 24 | 1862.0 | 1611.5 | +250.5 |
| 7 | P2 | E VOCÊ?　Parla di te | 24 | 1862.0 | 1700.5 | +161.5 |
| 8 | P2 | SEX 20 | 32 | 510.5 | 228.0 | +282.5 |
| 9 | P2 | SÁB 21 | 32 | 961.0 | 678.5 | +282.5 |
| 10 | P2 | DOM 22 | 32 | 1411.5 | 1147.0 | +264.5 |
| 11 | P2 | SEG 23 | 32 | 1862.0 | 1579.5 | +282.5 |
| 12 | P2 | Nota — o feriadão…（Nota 盒顶行，非粗体） | 20.5 | 961.0 | 932.5 | +28.5 |
| 13 | P3 | A SEMANA, DIA A DIA | 24 | 1862.0 | 1702.5 | +159.5 |
| 14 | P3 | E VOCÊ?　Parla di te | 24 | 1862.0 | 1700.5 | +161.5 |
| 15 | P3 | PALAVRAS DA MEMÓRIA | 22 | 1862.0 | 1716.5 | +145.5 |
| 16 | P3 | Nota — o quilombo…（Nota 盒顶行，非粗体） | 20.5 | 961.0 | 877.5 | +83.5 |
| 17 | P4 | OS FINALISTAS | 23 | 1862.0 | 1628.5 | +233.5 |
| 18 | P4 | E VOCÊ?　Parla di te | 24 | 1862.0 | 1700.5 | +161.5 |
| 19 | P4 | Nota — o agregado…（Nota 盒顶行，非粗体） | 20.5 | 1411.5 | 1305.0 | +106.5 |
| 20 | P5 | O PLANO DA ESPERA | 23 | 961.0 | 787.5 | +173.5 |
| 21 | P5 | OS JOVENS EM NÚMEROS | 24 | 1862.0 | 1761.5 | +100.5 |
| 22 | P5 | E VOCÊ?　Parla di te | 24 | 1862.0 | 1700.5 | +161.5 |
| 23 | P5 | Nota — o gabarito…（Nota 盒顶行，非粗体） | 20.5 | 961.0 | 933.5 | +27.5 |
| 24 | P6 | O CAMINHO ATÉ O GABARITO | 22 | 1862.0 | 1770.5 | +91.5 |
| 25 | P6 | LER OS NÚMEROS | 24 | 1862.0 | 1671.5 | +190.5 |
| 26 | P6 | A CONTAGEM　do dia 16 ao dia 30 | 21 | 961.0 | 456.0 | +505.0 |
| 27 | P6 | DOIS GABARITOS　um exame | 21 | 1862.0 | 1314.0 | +548.0 |
| 28 | P6 | Nota — o prazo…（Nota 盒顶行，非粗体） | 20.5 | 961.0 | 928.5 | +32.5 |
| 29 | P7 | ERROS COMUNS　Errori frequenti | 23 | 1862.0 | 1844.5 | +17.5 |
| 30 | P7 | A PALAVRA　La parola（D4） | 23 | 1862.0 | 1710.5 | +151.5 |
| 31 | P7 | CARTAS DOS LEITORES | 23 | 1862.0 | 1718.5 | +143.5 |

PDF 300dpi 像素复验（印 = 网，同值；`pixel_boxtitle.log` / `pixel_boxtitle_web.log`；除路径外与 fix1 日志逐值相同）：

| 标题 | PIL clear | PDF 像素 clear | 结论 |
|---|---|---|---|
| D6 P2 PARA NÃO ERRAR | +83.5 | +82.6 | 已修 ✓（≥ +5） |
| D5 P1 NESTA EDIÇÃO（fs=24） | +23.5 | +21.7 | 存活 ✓ |
| D4 P7 A PALAVRA（fs=23） | +151.5 | +151.0 | 存活 ✓ |
| P1 EM POUCAS PALAVRAS | +3.5 | +3.1 | 在框内 ✓ |
| P7 ERROS COMUNS | +17.5 | +18.5 | 在框内 ✓ |

## §3 D1–D5 存活复测（与 proof1/fix1 实测值逐字一致）

| 项 | 本轮实测（自 creambox/boxtitle/pixel 日志） | 结论 |
|---|---|---|
| D1 P1「EM POUCAS PALAVRAS」框 | 框底 **2348.0**，末行「em Brasília. (Página 4)」基线 2327.6，clearance **+20.4**，desc-clear +14.4 | 已修存活 ✓ |
| D2 P3「A SEMANA, DIA A DIA」框 | 框底 **551.0**，末条「16h30.」基线 540.6，clearance **+10.4**，desc-clear +3.9 | 已修存活 ✓ |
| D3 P6「O CAMINHO ATÉ O GABARITO」框 | 框底 **854.0**，末行「Página do Participante.」基线 840.8，clearance **+13.2**，desc-clear +6.9 | 已修存活 ✓ |
| D4 P7「A PALAVRA」标题 | 「A PALAVRA　La parola」（fs=23）；PIL 真墨 clear **+151.5**，印/网 PDF 像素 **+151.0** | 修复存活 ✓ |
| D5 P1「NESTA EDIÇÃO」标题 | 「NESTA EDIÇÃO　Questo numero」（fs=24）；PIL 真墨 clear **+23.5**，印/网 PDF 像素 **+21.7** | 修复存活 ✓ |

## §4 creambox / sweep-all 逐项裁决（除 D6 已修外，0 真溢出）

creambox（31 盒，`creambox.log` 与 fix1 版逐字节相同）：
- 5 处 BELOW-WINDOW（皆盒外章节标题/家具行，假阳性）：P1 numbers 框 +37.0「AGORA VOCÊ」；P2 日程框 +32.0「Atenção: …」；P3 Nota 框 +37.0「UM DIA, DOIS SENTIDOS」；P6 图表框 +42.0「EXERCÍCIOS」与「Risposte a pagina 8 …」（同一盒两行）。
- 6 处 desc-clear 负值（行内无降部字母，proof1 已真墨迹复验余量 +4.5~+5.4；本轮值与 proof1/fix1 逐字相同）：P2 −1.0「Scrivi due frasi e inviale.」；P3 −0.9「frasi e inviale.」；P4 −1.5「due frasi e inviale.」；P5 −1.1「2027.」；P5 −0.9「inviale.」；P7 −1.5「memoria della lotta e della cultura.」。

sweep-all（`sweep-all.log`）：盒内 H-OVER 0 处。旗标 6 组皆为盒外（与 fix1 同值同裁决）：
- L-OVER −1.0 两处（P1「AGORA VOCÊ」墨左 988.0 vs 盒左 989.0；「A PALAVRA DA SEMANA」1438.5 vs 1439.5）：两行基线皆在盒底之下，属盒外标题，1px 为字形侧轴承，非缺陷。
- H-OVER 4 处皆为盒外章节标题/家具行：P2「O FERIADÃO, DIA A DIA」y=1594 在盒 y=1618 之上；P2「Atenção: …」BELOW；P2「Três dias, uma semana…」y=1594 在盒 y=1618 之上（家具行，墨右 1862.4 贴版心）；P6「O FIM DE NOVEMBRO EM NÚMEROS」y=1576 在盒 y=1594 之上。
- V-OVER：0 处。P2 D6 盒（box0 [538,605-961,846]）在 sweep 中仅余 Nota BELOW 行，无盒内旗标。

## §5 150 题手验（keycheck 149/150 + Q150 ✓）

- 机械四源比对：印刷键 = 核心键（仅 137/138 例外）= text.md 行内答案 = Respostas 汇总，**0 不符**（Q150 除外：印刷键 `✓`，行内为开放写作注，Respostas 为 `✓ + 范文指引`）。
- 逐题读题干配对（`keycheck-150.txt` 全表 750 行已逐行读完）：**149/150 PASS**。Q73「Depois da prova, começa a ___.」→ `espera` 与题干配对正确（与 Q70「começa a espera pelo ___」→ `gabarito` 各配各题）；Q137「Venerdì 20 novembre è festa nazionale.」与 Q138「Il Palmeiras ha vinto 5–4 ai rigori.」皆为正确意大利语译文（与核心键的差异为预期的读者语渲染）；Q139/Q140 意葡互译正确；Q146/Q147 与 P4 正文一致（Grêmio 第六冠、Palmeiras 第五冠）。
- 范文 88 词（`len(split())`=88，独立重数与 gates 一致），在 80–100 范围内。

## §6 引号 / CJK / 禁词（sweep-text.log）

- 弯引号：U+201C/U+201D 全版仅 P8 各 2/2；U+2019 仅 P1 徽标「L'EDIZIONE」1 处；ASCII 双引号 0；« » 全版平衡（P7 33/33；text.md 40/40；印/网 pdftotext 40/40）。
- CJK：SVG 文本节点仅 U+3000（每页 13–20 个）；text.md 0；印/网 pdftotext 0；freeze diff 新增 CJK 仅 U+3000（9 个）。
- 禁词（渲染文本节点 + text.md）：国际政治/内部标签 0（裸 grep 全 SVG 文件时 SOP/XXX/EUA 有命中，上下文皆为内嵌图片 base64，非渲染文本，与 proof1/fix1 同结论；print.txt/web.txt 中 0 命中）。
- 简体残留 0；`翻译`/`中文` 0；非省略号 `..` 0（45 处 `..` 皆在 `...` 内）；`?Scrivi` 合并 0；双空格 0。

## §7 D7 与注记（只记录、不判缺陷）

1. **D7 已撤销**：P1 顶栏标语「Il portoghese che legge il Brasile」未改动——`tables_it.py:201` 与 `content12.py:15` 均为原句；P1 SVG 与修前逐字节相同（`38041cab…`）；P1 整页目视图中顶栏标语为原句。**绝不列为缺陷。**
2. **P8 最小字号 9.75pt**：= SOP §1.1 下限，判 PASS（任务口径 ≥9.75pt 与 SOP 一致）。
3. **P8 注行墨右 +0.4**（proof1 实测，0.5 边际带内）：已知非缺陷，不复述为新发现。
4. **D6 以外 SVG 零意外变化**：除 p2 外 7 页与 proof1 修前逐字节相同（§2 另见 PROOF-NOTE §2 全表）。
5. 本轮未改动核心：freeze 核心基线 8/8 且 core SVG 复哈希未变；生产目录零写入（全部重渲染在 scratch build-copy）；NO commit、NO push。
6. 观察项 O-NEW（text.md 两行无渲染对应，全 pt 族系统性共有）见 PROOF-NOTE §4，不阻塞定稿。
