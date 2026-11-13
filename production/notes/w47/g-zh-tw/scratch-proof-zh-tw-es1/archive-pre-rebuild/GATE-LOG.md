# GATE-LOG — W47 zh-tw-es proof1 机械门独立重跑记录

复校对象：`production/2026-w47/2026-w47-zh-tw-es/`；工具一律 `~/workspace/weekly-git/tools/venv/bin/python`；中间大文件放 /tmp/proof-es1，笔记目录只留本文档与 PROOF-NOTE.md。

## 1. 文件身份

- `sha256sum`：print `5f77b922a5f954fbe84b59ea6a1bcce7a21f663dd27d69e4067f34d655dea9cf`（23,256,393 B）；web `c625ae1d85f220af088c6f3c95189b31442cbb970079067e5f3364310060b7b8`（2,513,310 B）；text.md `4e7bd1ae9b864a43b65b3edb882b82de9be9535e3d930035176fce902c47aa08`（52,272 B）。与任务所给一致。
- PyMuPDF（tools venv）：两 PDF 各 8 页，`Rect(0, 0, 1462.5, 2025.0)`。P8 字号集合两 PDF 相同，最小 9.75pt（其次 10.35pt）。

## 2. 文字层一致（pdftotext）

- print 48,652 字节；web 48,654 字节。字符多重集差 = 2：web 多 1 个 `\n` + 1 个空格，无字符缺失（行边界空白 artifact，与 KIT 所述一致）。
- 兩次提取曾写入笔记目录的 print.txt/web.txt，后因 EDQUOT 事件删除（可复现，数字已记于此）。

## 3. checks.py（本版自带）

```
PHRASE 2 × 8（封王遊行從天母棒球場出發／夜間遊行晚上7點…／小雪之後…／主燈秀每半小時一次…／頒獎典禮晚上6點30分開始／保險箱裡…／穿上紅色衣服…／迪士尼聖誕，從11月17日開始）
SIMP_ONLY_HITS []
CHART p4 [90.0, 450.0, 900.0] expect [90.0, 450.0, 900.0]
CHART p6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]
CHECKS PASS
```

## 4. 几何遮挡审计 tools/occlusion_audit.py

- 自检：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`
- 本版：`0 flags`。

## 5. P8 tools/p8.py

- `extract --p8 svg/p8-test.svg --total 150`：`noted set = 150 of 150`。
- `compare --core-p8 production/2026-w47/core-zh-tw/svg/p8-test.svg --edition-p8 …/2026-w47-zh-tw-es/svg/p8-test.svg --total 150`：
  `core 150 noted / edition 150 noted / status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[]`。
- 事故：首次带 `--json <笔记目录>/p8-compare.json` 运行时，`json.dump` 抛 `OSError: [Errno 122] Disk quota exceeded`；按任务指令停手、删自己笔记目录内可复现中间件（print.txt、web.txt）后重试一次，不带 `--json`，得上述 CLEAN 结论。
- P8 徽章（SVG 节点配对实测）：38 个 level chip 与 113–150 号一一配对，无缺失；A2 8 · B1 20 · B2 10。

## 6. freeze.py

- `baseline --build <本版目录> --core-svg <本版 svg> --out /tmp/proof-es1/freeze`：`baseline: 8/8 SVGs byte-identical`，8 个 sha256 全 MATCH；`core integrity: shipped core SVGs unchanged`。`git status` 确认未改动版内文件。
- `diff --core-svg core-zh-tw/svg --edition-svg <本版 svg>`：每页 +/− 字符串均为讲解层 EN→ES 改写与家具翻译；**新增 CJK 字符总数仅 27 = 「西班牙」×9**（P1 徽章+页脚 2 次，P2–P8 页脚各 1 次）。其余增减 CJK 均为同一中文串的 EN/ES 对照（家具「英語講解」→「西班牙語講解」、「第N版／共8版」→「Página N de 8」）与节点拆分差异；唯一中文释义句替换为 P1 词卡「拿下總冠軍，叫封王。」→ 西班牙语释义「campeonato es 封王.」，属讲解层重写，无新增目标语文本。

## 7. 弯撇/弯引號全扫

- U+2019、U+201C、U+201D、U+2018 在 `svg/*.svg`、text.md、content*.py、ABSTRACT.txt 中：**0**。
- SVG 文本节点中 ASCII `'`：0。`·` 共 59 处：P5 12（列表点 + 人名间隔号）、P6 4（时间轴图例）、P8 42（选项分隔），另 P1–P3、P7 为 0；均在允许语境。

## 8. 英文残留扫描（与 core 逐串比对）

- 与 core-zh-tw 完全相同的字符串共 1044 条；其中像英文 prose 的仅 4 条，皆为合法共有项：`A. 12:00 · B. 14:00 · C. 19:00`（数字选项）、`SUPER SAFE`、`SUPER STAGE`（活动英文名）、`香港11月節目　Hong Kong`（栏目标题，Hong Kong 为专名）。
- 英文常用词扫描：唯一命中为节目标题专名 `The Awakening of the Wendigo`。**英文 prose 泄漏 0**。

## 9. text.md 一致性

- SVG 全部文本节点（去空白后长度 ≥2）逐一查 text.md：**0 缺失**。
- text.md 与 SVG 字符多重集差 148，全部由导出器标题（`#`、H1 及 8 个 "## Page N — …" 英文页标题）与 SVG 刊头 "Lucerna" 家具之差解释，无内容字符缺失。

## 10. 编号与表

- 编号节点：1–150 齐全，无缺失；重复仅为配对题 25–28、43–46、61–64、79–82 在题面与 P8 答案各出现一次（166 节点 = 150 + 16）。
- fan-out 表 `scratch-fanout-zh-tw/tables.py`：`ENTRIES` 238 条，`LANGS` 9 语（de fr es it pt nl ru ja ko）。
- 写作范文 F（P8 SVG 重建）：非空字符 142，落在 120–180 字带内，与 KIT 及 P8 注文 "150. ✓ … (142 caracteres)" 一致。

## 11. §1.1 实测

- 纸色 #fbfaf6（8 页）；徽章色 A2 #5c6e30、B1 #46581f、B2 #37402f 齐全；无双线外框；页脚 `Lucerna　繁體中文週報 VOL.4　繁體中文正文　西班牙語講解`，页码行 `Página N de 8`。
- `VOL.` 出现：VOL.4 ×10、VOL.5 ×1（仅 P7 下期预告头）、VOL.3 ×2（P7 延期披露中/西两文，正确）。
- 非色板颜色（#D7B257、#EDD17F、#F1E8D4、#34483A、#7898CD、#4D72B4、#84A283、#4F765D）仅在 P1 刊头线中央三色蛾标志（`<title>Lucerna 三色蛾</title>`）内，属 SOP §1.1 规定的标志，非正文用色。
- 图片 6 张（P2/P3/P4/P5/P7/P8）均在渲染图上确认位置与出处署名。

## 12. 目视

- 印刷 PDF 8 页（100dpi，/tmp/proof-es1/png/p-1..p-8.png）逐版目视：无溢出、无重叠、无压页脚。
- 网页 PDF P1、P8（web-p1-1.png、web-p8-8.png）渲染与印刷版一致，无豆腐块；web PDF 字体全部嵌入子集（含 LucernaNotoSansCJKTC / LucernaNotoSerifCJKTC / Newsreader / UnifrakturMaguntia）。
