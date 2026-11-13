# GATE-LOG — 2026-W47 ru-es proof1 机械门实跑证据

版目录：`~/workspace/weekly-git/production/2026-w47/2026-w47-ru-es/`
工具：`~/workspace/weekly-git/tools/venv/bin/python`；正典 creambox `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383` 已验）。
本目录下证据文件：`occlusion.json/.log`、`adjudicate/sheet1–7.png`、`creambox-all.log`、`ink_measure.log`、`triple_check.log`、`p8-compare.json/.log`、`p8-extract.json/.log`、`freeze-diff.json/.log`、`freeze-baseline.log`、`freeze-out/`、`check_core.log`、`keycheck-150.json`、`print.txt`、`web.txt`、`scan1.py`、`svg-before.sha256`。

## §0 身份（磁盘实测）

- `Lucerna-VOL4-ru-es.pdf` SHA `acef924f8742bc78726e73ca84c30ff9097ca4e8b99d1a9715bb834e92a89293`，21,272,810 字节 ✓
- `Lucerna-VOL4-ru-es-web.pdf` SHA `788411a8c3aadd54e64088022d41680b90b8c15762773c594775f3c76d9bee90`，3,348,591 字节 ✓
- `2026-w47-ru-es.text.md` SHA `190e02310e1f29cdd2e0cb4c4735b3a31ba607ddcde59ae7ee018d9b1f350be9`，64,161 字节 ✓
- 三 SHA 与任务一致。`git status`：版目录未入仓（`??`），本次未 commit/push；freeze 运行前后 shipped SVG SHA 未变（`svg-before.sha256` 比对一致）。

## 1. Occlusion 审计（`tools/occlusion_audit.py`）

- 自检：`selftest OK`，6 类 planted 全部触发，clean 对照静默。
- 全版运行：`42 flags {'TEXTX': 42}`，COVER 0 / LINEX 0 / FOOTER 0 / EDGE 0 / BOXTITLE 0，rc=1（仅 TEXTX 有标记）。
- 逐个像素裁定（`adjudicate.py`：按 JSON 坐标从 1950×2700 卡片裁图、2× 放大、红框标墨迹盒，7 张 contact sheet 逐张目视）：
  - P1 #1–#10、P2 #11–#16、P3 #17–#19、P4 #20–#26、P5 #27–#28、P6 #29–#32、P7 #33–#40、P8 #41–#42。
  - 全部 42 项均为 3–8px 的墨迹盒侧边距重叠（相邻标点/词间、引号、带状标题的全角空格分隔段），渲染字形均未相触。**42/42 CLEAR，0 真缺陷**。与 KIT 自查数（42 TEXTX）一致。

## 2. 正典 creambox.py 全版扫描（+45px 窗口 + 逐行 clearance + P7 toolbox）

- 32 个奶油框（P1 4、P2 8、P3 4、P4 2、P5 3、P6 8、P7 3、P8 0）。
- 负窗口余量的 7 框全部为下 +28…+37px 的下一标题假阳性，框内余量 +15.9…+47.7、降部余 ≥ +10.2。
- **P7-TOOLBOX：3 框，最小框内余量 +11.9px，最小降部余量 +5.9px**（通过）。
- 唯一临界：P2 `А ВЫ?` 框（y=795，底 1159.0）末行 `para Ded Moroz.` 启发式 desc-clear −1.0；PIL 真墨迹 + 卡片像素实测：降部最末墨行 y=1158，边界 y=1159，**0px 贴边、0 漫出**（见 PROOF-NOTE O3）。
- 其余 31 框框内余量 ≥ +5.0px；P3/P5 右栏框末行真墨迹余量 ≥ +42.7px（(b) 类未复现）。

## 3. p8 compare（显式 `--core-p8` / `--edition-p8`，core `core-ru/svg/p8-test.svg`）

- `core 150 noted / edition 150 noted / status: CLEAN / missing=[] extra_count=0 uncertain=[] / keydiff=[137, 138, 139, 140]`，rc=0。
- keydiff 逐个裁决：137–140 为 E 节 RU→西语翻译题，印键为西语译文（设计如此）；其余 146 键与 core 字节一致。
- `p8.py extract`：`noted set = 150 of 150`。

## 4. freeze / freeze_direct

- `freeze.py baseline --build <edition> --core-svg <edition>/svg --out scratch/freeze-out`：rc=0，工具报 `8/8 SVGs byte-identical`；**直接 SHA-256 比对 `build-copy/svg/` vs shipped `svg/`：8/8 MATCH**（逐页哈希见 `freeze-baseline.log`）；shipped SVG 运行前后未变。
- `freeze.py diff --core-svg core-ru/svg --edition-svg ru-es/svg`：P1–P8 文本多重集差分如 log 所示（讲解层替换所致）；CJK：edition 每页仅 U+3000（SOP §1.1 全角空格分隔符）+ P1 蛾标 `<title>Lucerna 三色蛾</title>`；新增 CJK 字符仅 U+3000（6 页各 1 个）。无可见中文文本。text.md CJK 0。

## 5. keycheck 150/150（`keycheck-150.json`）

- 逐题手验：题干对正文/表/图表逐项核实；P8 印刷键（p8 extract）与 text.md 答案逐题比对。除 Q150（开放写作，印刷键 `✓`，属设计）外，150/150 一致；**150/150 PASS，0 失败**。
- 表内题：Q54（Крылья—Оренбург 2:0）、Q59（Спартак胜 Акрон 2:1）已对 P4 渲染表（SVG 行重组，8 场全表）逐行核实。范文 97 词（brief 80–100），实测计数。
- 金句：8 条在 SVG 合并文本与 text.md 中各恰出现 2 次（正文 + P7）；`check_core.py`（自跑，rc=0）：`GOLDEN: 8 / golden BAD: 0 / gloss fails: 0`；1 孤儿行首（P7 y553 `”».`）与 1 同基线碰撞（P1 y1712 斜体 `чёрная`）——均与 core 同类、目视干净。

## 6. boxtitle 逐个实测（PIL 真墨迹，不只 advance）

- 全版 32 框标题墨迹右缘 vs 框右缘/页右缘（1862）：全部为正余量；P1 最紧为 `В ЭТОМ НОМЕРЕ　SUMARIO` +65.1px；全版最紧 P6 `ЗА И ПРОТИВ　PROS Y CONTRAS` +8.6px、P7 `ОШИБКИ　CLÍNICA DE ERRORES` +27.4px。
- P1 三法核实（(a) 项）：① PIL 墨迹——`ТУР В ЦИФРАХ　EN CIFRAS` +94.4px、`В ЭТОМ НОМЕРЕ　SUMARIO` +65.1px；② PDF span（PyMuPDF，印 PDF）——`EN CIFRAS` 右缘 867.1px（框 961）、`SUMARIO` 1796.4px（框/页 1862）、`EN BREVE` 1717.7px；③ 200dpi 像素扫描（印 PDF 渲染）——各标题带最右墨点余量 +67.8…+316.9px。**P1 无横向溢出**。
- 全部奶油框末行降部真墨迹：除 O3（0px 贴边）外，余量 ≥ +6.9px（P7 词框 `распродажа = gran venta.`）。

## 7. 印/网文字层比对（(e) 项斜体三联症）

- `pdftotext`：印版 57,731 字节 / 网版 57,780 字节；总字符 38,451 / 38,500；**非空白字符多重集一致，30,774 字符各**（KIT 数字复现）；差异仅为空白（网版 +45 空格 +4 换行），属分割噪声——但以下一项不是噪声：
- **D1（缺陷，见 PROOF-NOTE）**：印版 P1 恰 3 个斜体 span（`NotoSerif-MediumItalic` + `Newsreader16pt-Italic` ×2，本周词 «чёрная пятница»）；**网版斜体 span 0**，对应 span 全部变为 Regular，中间 span 文字层为 `чёрнаяпятница`（丢空格）；`«чёрная пятница»` 印版 8 次 / 网版 7 次，本周词栏抽出为 `«чёрная пятница »`（闭引号脱离）；目视对照 `wow-print.png` vs `wow-web.png` 确认网版正体 + 引号空隙。根因：网 PDF 建于 2026-11-11 03:50 UTC，斜体修复提交 `40963281` 为同日 09:39 UTC（`git log --format=%ad tools/webpdf.py`），**本版网 PDF 用的是修复前工具**。
- **修复验证（scratch 重建，未动 shipped 文件）**：当前 `tools/webpdf.py` 重建 `webpdf-test.pdf`（3,381,724 字节，rc=0，`LucernaNotoSerif-Italic` 54,476 字节已建）：斜体 span 恢复 3 个（bbox 与印版完全一致）、span 文本 `чёрная пятница`、`«чёрная пятница»` 8 次、总字符 38,451 = 印版、空格 5,187 = 印版——修复方案有效。
- 其余印/网一致性：`«` / `»` 各 199 次一致；`чёрная пятница`（无引号）10 次一致。
- P8 最小字号实测（PyMuPDF，印 PDF）：**9.75pt**（SOP §1.1 下限，符合）；全书最小字号亦为 9.75pt（P8）。

## 8. 弯引号 U+201C/U+201D/U+2019 全版扫描（SVG 可见文本 + text.md）

- text.md：U+201C 1、U+201D 1、U+2019 0——仅 P7 `на “чёрной пятнице”` 一对（故意保留）。
- SVG：P1–P6、P8 均为 0；P7 恰 1 对（`“` 起 + `”».` 止，同一元素对）。其余引号均为 « »（U+00AB/U+00BB）。

## 9. §1.1 与读者面扫查（自跑）

- 纸色 `#fbfaf6` 8 页；禁用色 `#f7f1e2` / `#c9a227` / `#8b4513` / `#000000` 均为 0（`gold` 命中 4 处均为内嵌图片 base64 数据子串，非颜色）；徽章 A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f` 俱在；奶油 `#f0eee5` 32 框；页脚 `SEMANARIO RUSO VOL.4` 8 页、`Página N de 8` 1–8 齐全；带标题 46px。
- 对外内容禁内部标签：SVG 可见文本中 `2026-w47` / `ru-es` / `SOP` / `proofread` / `cover` / `W47` 均为 0；text.md 同样 0 命中；VOL.4 9 次（含刊头/页脚）、VOL.3 1 次（P4 更正句，合规）、VOL.5 6 次（下期预告/承诺，合规）。
- E 节 type 标签：`Traducción` 4 题 + `Traducir al español` 4 处，中文 `翻譯`/`翻译`/`中文` 0——(d) 项未复现。
- text.md：838 行，203 块；150 题 + 150 答案行连续 1–150；`— СТРАНИЦА ? —` 与 core-ru `2026-w47-ru-core.text.md:668` 同款（导出器格式，见 PROOF-NOTE O2）。
- 8 页卡片逐页目视：无溢出/重叠/截断/压页脚；P4 八场表与 15 轮赛程完整；P6 图表柱长成比例、38/26/18/18；P7 来信披露（俄+西双语）在框内、与金句线无交；P8 113–150 题 + 全部答案 + 范文完整；P8 «Морозко» 图按设计跳过（键至 col 3，见 KIT）。

## 外部事实来源

- 俄超 14 轮（比分/积分/83 分钟/90+1/20:45）：Forbes `https://www.forbes.ru/sport/571957-zenit-ostupilsa-krasnodar-vydohnul-obzor-14-go-tura-rpl?amp=`；Спорт-Экспресс `https://www.sport-express.net/football/rfpl/news/chempionat-rossii-po-futbolu-turnirnaya-tablica-rpl-8-noyabrya-2026-po-itogam-14-tura-2472636/`；Sports.ru `https://www.sports.ru/football/1117427689-alfa-bank-rpl-lokomotiv-primet-rubin-krasnodar-sygraet-s-czska-v-subbo.html?mainNews-football`；Sportradar 实时赛果（Baltika–Dynamo Makhachkala 0:1、Zenit–Rostov 2:2、Spartak–Akron 2:1、Krylia–Orenburg 2:0、Krasnodar–CSKA 4:2、Akhmat–Rodina 1:0、Fakel–Dynamo 1:2、Lokomotiv–Rubin 0:1）。另 core-ru KIT §3 载明同组来源（sports.ru / Forbes / rusfootball.info）。
- 第 15 轮赛程：Спорт-Экспресс同上（20.11 Rostov–Krylia、21.11 Orenburg–Baltika / Akron–Fakel / Rubin–Zenit / CSKA–Akhmat、22.11 Dynamo–Krasnodar），与 P4 表一致。
- 星期/日期：`date -d`（Europe/Moscow）核验 12 日周四、16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21–22 日周末、27 日周五、29 日周日、30 日周一。
- 其余事实（友谊赛、黑五日期、天气、电影、节日）以 core-ru KIT §3 的已核查来源为准（本版为 fan-out，不改核心事实）。

## 判为非缺陷的项（证据在上）

- 42 TEXTX 全部为测量伪报（像素裁定）；creambox 下标题假阳性；P2 末行降部 0px 贴边（O3）；P1 标语两处 0–1px 词距（O1，核心家具共有）；`— СТРАНИЦА ? —`（O2，导出器共有格式）；Q140 译法（O4）；Q150 印刷键 `✓`（设计）；check_core 孤儿行首/同基线碰撞（与 core 同类）；窄词距类（KIT 已裁定；本版实测词距 3–6px，O1 两处除外）；P8 最小字号 9.75pt（SOP 下限内）；P8 «Морозко» 图跳过（设计）。
- **KIT 记录核对**：occlusion 42 TEXTX、p8 CLEAN/keydiff [137–140]、freeze 8/8、P8 9.75pt、非空白字符 30,774——本次独立实测全部复现；唯 KIT 关于网 PDF 斜体的隐含说法不成立（网 PDF 早于修复提交 40963281 约 6 小时，即 D1）。
