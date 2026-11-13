# FANOUT-REPORT — W47 fr re-fanout #2（从 core-fr fix4 重建 10 读者语版）

重建 run：`r2run1`，2026-11-11。构建与门禁解释器均为 repo 内 `tools/venv/bin/python`（系统 python3 未用）。
网 PDF 一律用已打补丁的 `tools/webpdf.py`（commit 40963281，斜体修复版）生成。**未 commit、未 push。**
工作区：`hidden_files/w47/scratch-refanout-fr2/`；#1 旧版备份：同目录 `backup-old/`（366M，含 #1 全部 10 版 + `OLD-SHA.txt`）。

## 核心定稿（复核一致，开工前验过）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印 `La-Lucerna-VOL4.pdf` | 30,446,975 B | `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d` |
| 网 `La-Lucerna-VOL4-web.pdf` | 2,241,835 B | `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141` |
| 文 `2026-w47-fr-zh-cn.text.md` | 46,471 B | `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df` |

核心 fix4 相对 #1 的变化（逐字节 diff 核实）：`content8.py:170` 键 `devant`→`devant le`；`:176` 题干 `On se retrouve (148)___ du cinéma?`→`On se retrouve (148)___ cinéma?`（删 `du`）；`expl.py:123` `chiffres_note` 删「决赛」二字（387.0px→344.0px，单行，修核心 P4 孤儿 。）。其余全部字节相同。

## 1. 交付：10 版三件 SHA 全表

| 版 | 印刷 PDF（字节 / SHA-256） | 网页 PDF（字节 / SHA-256） | .text.md（字节 / SHA-256） |
|---|---|---|---|
| fr-en（英语） | 17,418,996 / `7210b3e23c97ef4f683bf695ecc7484bc97fda5cf522abb94fb16ce17f675414` | 1,700,436 / `ca7f8ae3a76fdbb70f8af1724f92bdb6269f8bbc48b41348457e3d6ddbf551a2` | 46,191 / `7b658ae24f265d145455798c39f158d504b39e8034022a06b1c809c8bd7a5c4c` |
| fr-de（德语） | 17,424,223 / `77842fe4dc5d162adc7f2b8694ad92e985fe83a1fcd9a49c2c3e3ae2886d8e7b` | 1,706,936 / `df62f6ee61ae8cc6cd57c837a4a2da74187f855b0d71d2c5a07751ebfb9fdf37` | 46,632 / `d3735ef592bc02fcbe9712c3a184c2c2c963fd3fcfaf3311363ccf2baf95bc18` |
| fr-es（西班牙语） | 17,418,347 / `77488ab05a39b269b38f16ebb0da59e500d1c9b8739e77a3ca3a9387712104f4` | 1,701,681 / `2e56003e9353fb3de400b27d9e6700e5ad834007e6be07b0dbe758442efbf0b3` | 46,660 / `096402b410eccd1f3d0cbcdd5cc786ec82815c967eaa0312157cd7b9b49a1d7f` |
| fr-it（意大利语） | 17,415,873 / `2a47495b00bda39a108420b1986bf214946220952b6f9c8b4bd47e842e5632f6` | 1,696,726 / `8957acb69bb9342957c0c20a2f61412f0386beb721cdb076fbfa493bcd58b3ab` | 46,617 / `fac32b0bbf28a1b1a7a7365620de5348501fa49b7295816414522bd85ca25919` |
| fr-pt（葡萄牙语） | 17,420,030 / `420d79e71cc02859a5d9c8fa94c1b09ea7ae4f786c22911a4d8d2a3e7ed95521` | 1,702,371 / `fb88ae09d19a9b66906df2865ec15529c9f09429de22e690fbcc252ac5eff6b1` | 46,536 / `172f28dc192ea023b64bffb3e84f8a7106b4ff46f9db11a6a5d08d0f6b9efbdd` |
| fr-nl（荷兰语） | 17,418,792 / `3b0073cc94bcfb42d9a0ecdd5cd9bbc2b3d7b5846d2f62e82db5be4c9b6957ee` | 1,699,714 / `5217c87ac893a6b0bd89a7066d1c28acf0ff1aa780c4522114fa5360309b18b7` | 46,265 / `d83b5831b235a7b8a9efad5343d996fc85c70d16400eed7250beb4eb4bb5ee28` |
| fr-ru（俄语） | 17,477,429 / `c2976921db3531b69adc9d0a37ab8c5fb59dde8678d6892d6d2a9d72de040229` | 1,760,007 / `a6d94e5f0d54f78d5cd822040b17bff37c04a7a6852ad25fce5388dcdca9a15a` | 50,453 / `a3449fa7e9d90576241371a33fd8f1c25d17a7c723ceee019de9e29d11ccd8f9` |
| fr-ja（日语） | 30,565,630 / `291a514f7980e4a30e0f736d22f3c89c720996f96d83770206d92343e6096f63` | 2,309,603 / `031684fd076ba8e1b3c64ae4f3df17330e10d838650ca2577cd110bc04ab44d3` | 47,532 / `aca654257d25d33d331db2c201724d287e050bdcb288c84057b74c8ef8461498` |
| fr-ko（韩语） | 23,103,425 / `a315cced01b3725d57e17ca5b57015372b4bf2555392033cae618dd38faf3c82` | 2,048,869 / `0862b544eb337d4061cf762a9f40932ae40fc5d0107cfd9bac2bb31e4349ebd5` | 47,323 / `f5474d61eeadf9fdb2fe6a5fb3e2e15ff9088201aa8989e986ed064f46ba5c37` |
| fr-zh-tw（繁体中文） | 30,551,086 / `ccdfc35fb49f41f6ee966f296a0016ccdff6b1d4a865cb79238997c3b42af95b` | 2,552,871 / `ac9f148038dcdb103230d78a319a1d206d3f394a3746dabd819d683852603324` | 45,998 / `6e348b8c9309d1822a3d6cf4482dee9781ea07157002f0239990b5c61ed73ba9` |

注：新网 PDF 均比 #1 大（约 1.66–1.70MB → 1.70–2.55MB），因改用 40963281 斜体修复版 webpdf.py；核心网 PDF 在 fix4 中亦同向变大（2,205,749 → 2,241,835 B）。非缺陷。CJK 三版印刷 PDF 约 23–31MB（CJK 字体嵌入），亦与 #1 同量级。

## 2. 必查清单 8 项（逐项落点与实测值）

### 项 1 — P7 披露框溢出（框 y=1878 h=380，框底 2258.0；#1 末基线 2260.6，+2.6 溢出）

de/es/it/pt/nl/ru 六版 `courrier_disclosure` 删中句（该信息已由 P7 法文示例标注句覆盖），3 行→2 行；en/ja/ko/zh-tw 四版原先 2 行未动。重建后 10 版全部 creambox + PIL 双重实测：

| 版 | 末行内容（末基线前） | 末基线 | creambox 清除 | PIL 真墨末行（svg y） | 2258–2270 间隙墨 |
|---|---|---|---|---|---|
| fr-en | …labelled editorial example; VOL.5 will honou… | 2233.3 | +24.7（desc-clear +18.8） | 2237.3 | 无 |
| fr-de | löst das Versprechen ein, echte Einsendungen zu kommentieren. | 2233.3 | +24.7（desc-clear +18.8） | 2237.8 | 无 |
| fr-es | promesa de comentar envíos reales. | 2233.3 | +24.7（desc-clear +18.8） | 2237.3 | 无 |
| fr-it | manterrà la promessa di commentare invii veri. | 2233.3 | +24.7（desc-clear +18.8） | 2237.3 | 无 |
| fr-pt | promessa de comentar envios reais. | 2233.3 | +24.7（desc-clear +18.8） | 2237.3 | 无 |
| fr-nl | VOL.5 lost de belofte in om echte inzendingen te bespreken. | 2233.3 | +24.7（desc-clear +18.8） | 2237.8 | 无 |
| fr-ru | обещание разобрать настоящие письма. | 2233.3 | +24.7（desc-clear +18.8） | 2237.3 | 无 |
| fr-ja | る。VOL.5で実際の投稿の講評という約束を果たす。 | 2233.3 | +24.7（desc-clear +18.8） | 2234.4 | 无 |
| fr-ko | 투고 평론 약속을 지킨다. | 2233.3 | +24.7（desc-clear +18.8） | 2234.4 | 无 |
| fr-zh-tw | ；VOL.5 將兌現點評真實投稿的承諾。 | 2233.3 | +24.7（desc-clear +18.8） | 2235.4 | 无 |

10 版末基线均为 2233.3，清除 +24.7（旧 -2.6）。PIL 真墨末行距框底 20.2–23.6px，间隙 2258–2270 零墨。目视复核：de P7 全页 + 200 dpi 盒底裁切、es P7 盒底裁切，披露 2 行完整在奶油盒内，下方白纸间隙干净、绿带未被侵入。
各版删句原文（expl.py `courrier_disclosure`）：de `diese Ausgabe druckt ein gekennzeichnetes Redaktionsbeispiel.`；es `este número publica un ejemplo editorial marcado.`；it `questo numero pubblica un esempio editoriale marcato.`；pt `esta edição publica um exemplo editorial marcado.`；nl `dit nummer drukt een gemarkeerd redactievoorbeeld.`；ru `в этом номере печатается помеченный редакционный пример.`。

### 项 2 — fr-en：P8 Q64 注 `Les Braves by Dont` → `Dhont`

落点：`expl.py` `n_photo3`，仅 P8 哈希变（`f310354a`→`e027cc89`）。P5 正文与 Q64 选项 B 原先即为 Lukas Dhont，核对一致。P8 目视复核：答案区 64. B (Les Braves by Dhont) 清晰。

### 项 3 — fr-it：P5 词表 mots_photo 两处冠词

落点：`expl.py:139` `mots_photo`，`"una attrice — attrice"`→`"une actrice — attrice"`；`"una séance — spettacolo"`→`"une séance — spettacolo"`。仅 P5 哈希变（新旧值见 §4 改动表）。P5 目视复核：词表两行已为 `une actrice — attrice`、`une séance — spettacolo`。

⚠ **与任务原文一字之差（请 proof2 确认）**：任务原文写的是 `une attrice`，但 fr-it 复校（D2）与核心正文（`une actrice — 女演员`）均规定 `une actrice`。本轮按核心/复校落为正确法语 `une actrice`（`attrice` 不是法语词）。若任务原文有意，请 proof2 改回。

### 项 4 — fr-ja：3 处孤儿日文句号 。

| 落点 | 改法 | 结果 |
|---|---|---|
| P1 g1 `un vin primeur　le beaujolais ボジョレー 新酒。` | 删 `新酒`（释义仍存于 g2 与 m_p8d/m_primeur2 `primeur = 新酒`） | P1 哈希变，行末 `ボジョレー。` 落行内，目视复核无孤儿 |
| P4 `bridge_comp4` `比較級（plus / moins）で文を完成させよう。` | → `比較級（plus / moins）で文を完成しよう。` | 1 行，P4 哈希变 |
| P6 `bridge_chart` `上のカレンダーを読んで正しい答えを選ぼう。` | → `上のカレンダーを読んで答えを選ぼう。` | 1 行，P6 哈希变 |

重扫：ja 新增孤儿 0（旧版 3 处 。P1 1366.65 / P4 1722.92 / P6 1941.22 已全部消失；旧版数据见本报告 §5 检测器验证）。

### 项 5 — fr-zh-tw：D1 简体残留 + D2 孤儿 。×3

- **D1**：`zoom_note` 与 `n_vf1` 各一处 准（U+51C6）→ 準（U+6E96）；重建后 expl.py 全文 准 0 个、準 2 个。核心本身正确简体，未动核心。
- **D2**：(1) P2 gloss 框 `bridge_valise`：`註｜une virgule 逗號　voter 投票　fêter 慶祝。` 删 `une ` → 1 行，句号落行末（P2 哈希变；目视复核：`註｜virgule 逗號 voter 投票 fêter 慶祝。` 单行完整）；(2) P2 ET VOUS 框 `etvous_note`：删 `話` → `說說你的11月19日：用法語寫兩句寄來。` 1 行（目视复核：单行完整）；(3) P3 ZOOM 框 `zoom_note`：删 `這場約會的` → 2 行，句号落第 2 行行末（目视复核：`1951年獲准提前售酒、1985年定為11月第三個星期四、2026年是75週年。` 两行完整，含 準）。
- **P4 残留（只记录，不修）**：`chiffres_note` 繁体释义 `大師賽決賽結果與杜林名單見本版正文。` 仍 387.0px、折 2 行，句号独行于 P4 y=550.53（该基线仅此一元素，确为视觉孤儿）。核心 fix4 删的是法文注里的「决赛」，读者语释义未同步删「決賽」——fix4 之后此项已不再是“核心继承”，但任务明确 P4“只记录”，故留给 proof2 定夺（修法：释义删「決賽」二字，同核心）。

### 项 6 — Q148 落地（10/10）

每版核对：键 `devant le`、题干 `On se retrouve ___ cinéma ?`（无 `du`）。三重验证：P8 SVG 文本层含 `On se retrouve` + `cinéma ?` 且不含 `du cinéma`；`content8.py` 含 `"devant le"` 与 `On se retrouve ({gnums[3]})___ cinéma ?`；`p8.py extract` 提取键 148 = `devant le`。10 版全部通过。P8 目视复核（en/de）：对话区 `(148)___ cinéma ?`、答案区 `148. devant le` 均正确。

### 项 7 — 每版孤儿标点全扫（新增 0）

检测器 `check_extra.py`（逐 `<text>` 元素，与核心 fix4 扫描同法，见 §5 检测器说明）。10 版新增真孤儿全部为 0：

| 版 | 元素总数 | 新增 | 核心继承（行首 —） | 记录残留 | 字体分拆同基线 |
|---|---|---|---|---|---|
| fr-en | 0 | 0 | 0 | 0 | 0 |
| fr-de | 0 | 0 | 0 | 0 | 0 |
| fr-es | 0 | 0 | 0 | 0 | 0 |
| fr-it | 0 | 0 | 0 | 0 | 0 |
| fr-pt | 0 | 0 | 0 | 0 | 0 |
| fr-nl | 0 | 0 | 0 | 0 | 0 |
| fr-ru | 15 | 0 | 1 | 0 | 14 |
| fr-ja | 1 | 0 | 1 | 0 | 0 |
| fr-ko | 15 | 0 | 2 | 0 | 13 |
| fr-zh-tw | 3 | 0 | 2 | 1 | 0 |

核心继承的 “—” 元素（P4 y=623.13、P6 y=653.69，x=1007.0）为行首破折号，与后文同基线（如 `— 好球！`），非视觉孤儿；各版因法文+释义框折行不同，继承数为 0–2（ja/ko/ru/zh-tw 各有，拉丁六版为 0）。zh-tw 另有 P4 残留 1 处（见项 5）。

### 项 8 — 孤行填空线 Q130 / P3 Q36 / Q37（观察项，非缺陷）

三处在 10 版中全部存在，与核心同位关系如下（核心：P3 Q36/Q37 x=538.5 y=1864.7/1997.4；Q130 x=989.0 y=843.0，P8）：

| 版 | Q130（P8） | P3 Q36（y） | P3 Q37（y） | 与核心关系 |
|---|---|---|---|---|
| fr-en | (989.0, 843.0) 与核心分毫不差 | 1924.1 | 2056.8 | Q36/Q37 下移 +59.5（读者语练习流排版所致，x=538.5 不变） |
| fr-de | (989.0, 843.0) 与核心分毫不差 | 1894.4 | 2027.1 | Q36/Q37 下移 +30（读者语练习流排版所致，x=538.5 不变） |
| fr-es | (989.0, 843.0) 与核心分毫不差 | 1924.1 | 2056.8 | Q36/Q37 下移 +59.5（读者语练习流排版所致，x=538.5 不变） |
| fr-it | (989.0, 843.0) 与核心分毫不差 | 1894.4 | 2027.1 | Q36/Q37 下移 +30（读者语练习流排版所致，x=538.5 不变） |
| fr-pt | (989.0, 843.0) 与核心分毫不差 | 1924.1 | 2056.8 | Q36/Q37 下移 +59.5（读者语练习流排版所致，x=538.5 不变） |
| fr-nl | (989.0, 843.0) 与核心分毫不差 | 1924.1 | 2056.8 | Q36/Q37 下移 +59.5（读者语练习流排版所致，x=538.5 不变） |
| fr-ru | (989.0, 843.0) 与核心分毫不差 | 1894.4 | 2027.1 | Q36/Q37 下移 +30（读者语练习流排版所致，x=538.5 不变） |
| fr-ja | (989.0, 843.0) 与核心分毫不差 | 1864.7 | 1997.4 | Q36/Q37 下移 +0（读者语练习流排版所致，x=538.5 不变） |
| fr-ko | (989.0, 843.0) 与核心分毫不差 | 1864.7 | 1997.4 | Q36/Q37 下移 +0（读者语练习流排版所致，x=538.5 不变） |
| fr-zh-tw | (989.0, 843.0) 与核心分毫不差 | 1864.7 | 1997.4 | Q36/Q37 下移 +0（读者语练习流排版所致，x=538.5 不变） |

Q130 三处坐标 10 版与核心完全相同（989.0, 843.0）；Q36/Q37 x 均为 538.5，y 分三档（+0：ja/ko/zh-tw；+30：de/it/ru；+59.5：en/es/pt/nl），与 #1 旧版核查分毫不差——重建未改变其相对位置。未修核心，未判 (b)。

## 3. 门禁结果（10/10 全部 15/15 PASS）

每版 `run.py` exit 0、TOTAL 150、occlusion 0、p8 compare CLEAN（keydiff `[150]`，仅写作题键）、freeze 8/8、印/网文字层字节一致、P8 最小字号 11.625pt、creambox 0 真墨溢出、boxtitle 0 溢出、keycheck 149/150 仅 Q150 例外。任务原文称 keydiff 预期 `[137,138,139]` 附近——实测 10 版均为 `[150]`，与 #1 一致（137–139 为翻译题键，与核心逐字相同；仅写作题键为读者语说明）。

| 版 | gates | 文字层字节 | 网 PDF | P8 最小字号 | 徽章 | MCQ 体/行 | band_r1 起始 | 终值 P6深读/P6练习/P8答案流/P7金句流 |
|---|---|---|---|---|---|---|---|---|
| fr-en | 15/15 | 105,574 | 1,700,436 B | 11.625pt | 134 | 45/1481 | 1252.1 | 1288/1300/2527/2560/2146/2560/1778/1830 |
| fr-de | 15/15 | 104,632 | 1,706,936 B | 11.625pt | 134 | 45/1485 | 1337.5 | 1288/1300/2527/2560/2126/2560/1806/1830 |
| fr-es | 15/15 | 104,934 | 1,701,681 B | 11.625pt | 134 | 45/1479 | 1299.7 | 1288/1300/2527/2560/2167/2560/1806/1830 |
| fr-it | 15/15 | 106,161 | 1,696,726 B | 11.625pt | 134 | 45/1478 | 1307.6 | 1288/1300/2527/2560/2146/2560/1778/1830 |
| fr-pt | 15/15 | 104,688 | 1,702,371 B | 11.625pt | 134 | 45/1482 | 1270.9 | 1288/1300/2527/2560/2106/2560/1778/1830 |
| fr-nl | 15/15 | 105,229 | 1,699,714 B | 11.625pt | 134 | 45/1480 | 1329.4 | 1288/1300/2527/2560/2126/2560/1718/1830 |
| fr-ru | 15/15 | 107,298 | 1,760,007 B | 11.625pt | 134 | 45/1477 | 1284.4 | 1288/1300/2527/2560/2046/2560/1718/1830 |
| fr-ja | 15/15 | 102,405 | 2,309,603 B | 11.625pt | 134 | 45/1451 | 1380.0 | 1258/1300/2402/2560/2106/2560/1718/1830 |
| fr-ko | 15/15 | 102,735 | 2,048,869 B | 11.625pt | 134 | 45/1449 | 1436.9 | 1258/1300/2402/2560/2086/2560/1718/1830 |
| fr-zh-tw | 15/15 | 101,463 | 2,552,871 B | 11.625pt | 134 | 45/1442 | 1405.0 | 1258/1300/2402/2560/2026/2560/1718/1830 |

各版 gates 全量 JSON 在工作区 `<lang>/gates-r2run1.json`，build 日志 `<lang>/build-r2run1.log`（含单条已知良性 `NOSPACE` 行 `P7 DORE NOSPACE`，gates 已过滤）。precheck 10/10 PASS（g1–g6 ≤5 行；band_r1 起始 ≥1252；band_r2 ≥950；共行对 ≤1757，实测最大 1754.6，最小 872.1）。

## 4. 改动封闭性（新版 SVG vs #1 备份逐页哈希对比）

| 版 | 改动页（#1 哈希 → 新哈希，前 8 位） | 未动页 |
|---|---|---|
| fr-en | P8（f310354a→e027cc89） | P1、P2、P3、P4、P5、P6、P7 |
| fr-de | P7（4bc0ef75→700bee74）、P8（7e3269a2→660522e4） | P1、P2、P3、P4、P5、P6 |
| fr-es | P7（c7fc6d9e→75d2252b）、P8（20df945f→aa084df5） | P1、P2、P3、P4、P5、P6 |
| fr-it | P5（7a7f178e→a91995f1）、P7（d486ba6a→12eb2907）、P8（e95c7ef1→64d1ba48） | P1、P2、P3、P4、P6 |
| fr-pt | P7（ea3d710b→c3419d55）、P8（7d582103→34bf3311） | P1、P2、P3、P4、P5、P6 |
| fr-nl | P7（037b5c49→4eb69452）、P8（6a9750ef→467885cd） | P1、P2、P3、P4、P5、P6 |
| fr-ru | P7（e825ca39→04f6feb7）、P8（3cdf7e52→a92673d4） | P1、P2、P3、P4、P5、P6 |
| fr-ja | P1（8bf58ae5→0111ee1c）、P4（8252ca19→2b64f954）、P6（7fdd8932→11f2a3c3）、P8（66b5fa78→bf40c3c0） | P2、P3、P5、P7 |
| fr-ko | P8（b533645f→fc7999be） | P1、P2、P3、P4、P5、P6、P7 |
| fr-zh-tw | P2（7e372c72→b46154cf）、P3（f3280832→22af3699）、P8（86da3308→7b8c6116） | P1、P4、P5、P6、P7 |

改动页与修复项一一对应：P7 = 披露框缩短（六版），P8 = Q148（十版全有），P5 = it 词表冠词，P1/P4/P6 = ja 三孤儿，P2/P3 = zh-tw D2。无一页多余改动。`ABSTRACT.txt` 10 版均自 #1 备份原样恢复（内容不受 fix4 影响，字节核对一致）；`WEEKLY-KIT.md` 10 版均已重写（§四新实测 + §五 #2 记录在前、#1 史保留在后）。

## 5. 检测器说明与验证（check_extra.py，本轮一次修正）

孤儿检测原为纯逐元素判定：`<text>` 元素去空格后全为标点即记孤儿。ru 初扫报 14 处“新增”（`.`/`:`），逐一核对基线邻居后证实全部是字体分拆的行末标点：西里尔文本行末的拉丁标点因字体切换被渲染器拆成独立 `<text>` 元素，与同行词共享基线（如 P8 Q139 `Итоги ещё неизвестны.` 之句号 x=1677.3 y=533.0，同基线另有 `Итоги`/`ещё`/`неизвестны`；P4 `chiffres_note` 释义 `Итог финала и состав Турина: см. текст на этой странице.` 之 `:`/`.` 亦同）。

修正：加同基线判定——标点元素若与同页任一含实词元素共享基线（|Δy|<1.5），记 `shared_baseline`（非视觉孤儿），不计新增。分类优先级：核心继承 > 记录残留 > 同基线 > 新增。

验证（未放水）：修正后重扫旧版备份——旧 ja 仍检出 3 处真孤儿 。（P1 1366.65 / P4 1722.92 / P6 1941.22）+ 1 继承 —；旧 zh-tw 仍检出 3 处 。（P2 250.22 / P2 1304.18 / P3 1493.6）+ 2 继承 — + P4 残留 550.53，与 proof1 完全一致。ru 修正后重扫：0 新增、14 处 shared_baseline。ko 同类 13 处（`.`/`——`/`）`，亦全部同基线。10 版最终新增真孤儿 0。

## 6. 目视复核（印刷版 PDF，100 dpi 改动页 + P7 盒底 200 dpi 裁切）

- en P8：Q148 对话与答案、`64. B (Les Braves by Dhont)`、Q130 填空线均正常。
- de P7 全页 + 盒底裁切：披露 2 行完整在盒内，下方白纸间隙干净。de P8：Q148 正常。
- it P5：词表 `une actrice — attrice`、`une séance — spettacolo` 正常。
- ja P1：g1 释义行末 `ボジョレー。` 落行内，无孤儿；全页无他问题。
- zh-tw P2：gloss 框与 ET VOUS 框单行完整；P3：ZOOM 框两行完整、含 準。
- es P7 盒底裁切：披露 2 行完整在盒内。
- 其余改动页（pt/nl/ru/ja P4·P6·P8、ko P8、zh-tw P8）凭 creambox+PIL 数值 + 哈希封闭性通过，未逐页目视——改动均为单行文本缩短或单键替换，无版式风险。（pt/nl/ru/it P7 盒底裁切已渲染在工作区 `png/`，数值已验。）

## 7. 过程事件

- **VM 重启中断（2026-11-11 约 15:25）**：ja 首次重建在 render.py 中段被重启杀掉（run.py 已完成 TOTAL 150，PDF 未生成）。已用 `build_edition.py ja r2run1` 全量重跑，rc=0，三件齐全；其余 9 版构建未受影响。另一次重启中断了 nl finish 的回显（`aborted`），但文件已全部落盘，事后核对 KIT/RECORD/PNG 齐全，无需重做。
- **KIT 格式三分**：#1 各版 KIT 格式不一——en/de/es/it/pt 为中文 §一–§六式；nl/ru 为英文 Files/Gates/Fix log/Notes/Visual QA 式；ja/ko/zh-tw 为英文 Build/Pre-build/runN–GATES/Files delivered/Visual QA/Fix log 式。`finish_edition.py` 已按三式分别接线：中文式重写 §四、§五前置 #2 记录；英文两式替换 Files/Gates（或追加 Rebuild #2 — GATES 节）、Fix log 前置 #2 记录、末尾追加 Visual QA — rebuild #2 节；#1 历史全文保留。
- **D5 字体问题**：只记录，不修（按任务）。拉丁讲解层仍渲染于 Noto Sans CJK SC（与 #1 相同）。
- **核心未动**：10 版构建全程只读 core-fr；构建前后核心三件 SHA 复核一致。其他语族未动。未 commit、未 push。

## 8. 待 proof2 定夺（本轮未擅自决定）

1. fr-it `une actrice` vs 任务原文 `une attrice`（见项 3）。
2. fr-zh-tw P4 残留 。（`chiffres_note` 繁体释义删「決賽」二字即可去孤儿；见项 5）。

## 9. 产物与工作区

- 本报告：`hidden_files/w47/scratch-refanout-fr2/FANOUT-REPORT-fr2.md`
- 每版工作区 `<lang>/`：`build-r2run1.log`、`gates-r2run1.json`、`gates-r2run1.log`、`extra-r2run1.json`、`creambox-r2run1.log`、`precheck-r2run1.log`、`mcq-r2run1.log`、`fixes-note.txt`、`EDITION-RECORD.md`、`png/`（改动页 100 dpi + P7 盒底 200 dpi 裁切）。
- 工具（本轮新增/改动）：`check_extra.py`（同基线判定）、`pil_p7.py`（PIL 真墨测量）、`finish_edition.py`（KIT 三格式接线 + ABSTRACT 恢复 + EDITION-RECORD + 目视渲染）、`measure_fixes.py` / `apply_fixes.py` / `check_extra.py`（修复应用与核验）。
- 生产目录：`production/2026-w47/2026-w47-fr-<lang>/` 10 版（每版含 `WEEKLY-KIT.md`、`ABSTRACT.txt`、三件、`svg/`、`cards/` 等全套）。
- #1 备份：`scratch-refanout-fr2/backup-old/`（含 `OLD-SHA.txt`）。
