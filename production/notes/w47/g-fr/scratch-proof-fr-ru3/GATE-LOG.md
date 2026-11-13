# GATE-LOG — W47 fr-ru 独立校对 proof3（全部门禁逐项实测值）

- 版：`production/2026-w47/2026-w47-fr-ru/`；核心：`production/2026-w47/core-fr/`（fix4）
- 解释器：`tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3，freeze.py 自报）
- scratch：`hidden_files/w47/scratch-proof-fr-ru3/`（全部中间件、脚本、日志在此；生产目录零写入）
- 结论：**b — 1 项缺陷 D1（见 PROOF-NOTE.md §2）**；其余门全绿。

## 0. 开工 SHA 核对（实测，与任务一致）

```
La-Lucerna-VOL4-fr-ru.pdf      17477429 B  c2976921db3531b69adc9d0a37ab8c5fb59dde8678d6892d6d2a9d72de040229
La-Lucerna-VOL4-fr-ru-web.pdf   1760007 B  a6d94e5f0d54f78d5cd822040b17bff37c04a7a6852ad25fce5388dcdca9a15a
2026-w47-fr-ru.text.md           50453 B  a3449fa7e9d90576241371a33fd8f1c25d17a7c723ceee019de9e29d11ccd8f9
```

## 1. run.py（scratch 副本重建）— PASS

- 命令：复制版目录（仅 .py + svg/ + cards/ + assets/）至 `scratch-proof-fr-ru3/rebuild/` 后跑 `run.py`；日志 `logs-rebuild.txt`。
- rc=0；TOTAL **150**（A2 53 / B1 75 / B2 22；按页 1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42；
  按型：完成句子 49、单选 26、词汇配对 21、阅读理解 5、阅读判断 5、完形填空 8、图表读数 6、翻译 5、
  对话补全 5、句型转换 7、改错 4、跟练 8、写作 1）。
- `FLOW OVERFLOW` / `HEAD TOO WIDE` / `NOSPACE` 出现 0 次（日志 grep 计数 0）。
- 重建 SVG 与交付 SVG **8/8 字节一致**（`svg-rebuild.sha` vs `svg-source-start.sha`，diff 空）；
  生产 SVG 始末哈希一致（`svg-source-after.sha` = 始值），生产目录未动。

## 2. freeze baseline + diff — PASS

- `freeze.py baseline --build production/2026-w47/core-fr --core-svg production/2026-w47/core-fr/svg --out freeze-core`：
  rc=0，**8/8** byte-identical（p1–p8 全 OK），`core integrity: shipped core SVGs unchanged`。日志 `freeze-core.log`。
- `freeze.py baseline --build production/2026-w47/2026-w47-fr-ru --core-svg production/2026-w47/2026-w47-fr-ru/svg --out freeze-ed`：
  rc=0，**8/8** byte-identical；`core integrity` 同样确认。日志 `freeze-ed.log`。
- `freeze.py diff --core-svg core-fr/svg --edition-svg 2026-w47-fr-ru/svg`：rc=0；
  p1 +30/−23，p2 +39/−33，p3 +35/−34，p4 +73/−40，p5 +58/−34，p6 +46/−28，p7 +38/−34，p8 +155/−122
  （增减均为讲解层替换）；新增 CJK 字符合计 15，**全部为 U+3000**（p3 1 处、p8 14 处；法/俄分隔符，SOP §1.1 所定），
  真实 CJK 字符 0。JSON `freeze-diff.json`。

## 3. occlusion 几何审计 — PASS（0 flags；盲区由 §7 补）

- 命令：`tools/occlusion_audit.py --json occlusion.json production/2026-w47/2026-w47-fr-ru/svg`。
- rc=0；自检 `selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；
  **flag_count = 0**。日志 `occlusion.log`，JSON `occlusion.json`。
- 盲区说明：occlusion 只查后绘元素覆盖/线穿字/页脚/出边，不查文本越出自家背景盒底——D1 由 §7 的 PIL + 交付 PDF 像素检出。

## 4. p8 extract / compare — PASS

- `p8.py extract --p8 svg/p8-exercices.svg --total 150`：rc=0；键 **150/150**，注记集 **121/150**（Q148 键 `devant le`）。
  日志 `p8-extract.log`，JSON `p8-extract.json`。
- `p8.py compare --core-p8 core-fr/svg/p8-exercices.svg --edition-p8 … --total 150`：rc=0；
  core 121 noted / edition 121 noted；**status CLEAN**，missing=[] extra=[] uncertain=[]，**keydiff=[150]**。
  JSON `p8-compare.json`。

## 5. 印/网文字层 — PASS

- `pdftotext -layout`：印版 107,298 B，网版 107,298 B，**逐字节一致**（`cmp` 无差异；`print.txt` / `web.txt`）。
- 网 PDF 1,760,007 B < 7 MB。

## 6. P8 最小字号 — PASS

- PyMuPDF 取印版 P8 全部 span：最小 **11.625pt** ≥ 9.75pt（SOP §1.1 下限）；全 8 页最小亦为 11.625pt。
- SVG 属性最小字号：P8 15.5pt（`check_s11_ru.log`）。

## 7. 盒标题 / 全文本 PIL 真墨 + 交付 PDF 像素 — 1 项越边（D1）

- 脚本 `verify_ed_ru.py`（自写；字体与字号取 SVG 元素本身，墨盒 `anchor="ls"` 基线相对）：
  8 页全部 `<text>` 逐一实测，入盒文本 **517 个**，越边 **1 个**：
  `p3-culture.svg — BOX #f0eee5 x1440 y1640 w422 h330，墨 1461.5–1675.5 × 1952.2–1971.2，文本 'вечером в среду 18-го.'`
  （盒底 1970.0，墨底 1971.2，越边 1.2 svg px）。其余 516 个全在盒内；页边越界 0。
- 交付 PDF 像素裁定（`La-Lucerna-VOL4-fr-ru.pdf` P3）：
  盒底矢量边 1477.199pt；600dpi 扫描暗墨延续至约 1477.92–1478.04pt（≥0.7pt 出盒）；
  300dpi 裁切 `crop-p3-boxbottom.png` 目视：3–4 处下行笔画尖出盒底。→ **D1，见 PROOF-NOTE.md §2**。
- 交付 PDF 8 页外沿 3px（150dpi）非纸色像素：**全 0**。
- P7 披露框间隙：200dpi 扫描 svg y 2258.5–2269.5 行暗像素 **0**（首版误含 y=2270 绿条首行得 1846，已修正行范围；
  绿条顶边恰为 svg y=2270，见 SVG `<rect x="989.0" y="2270" width="873.0" height="290" fill="#37402f"/>`）。
  披露末行 PIL 真墨自测：`<text x="1013.0" y="2233.3" font-size="19.5">обещание разобрать настоящие письма.</text>`，
  墨盒 y −17…+5 → 墨底 2238.3，盒底 2258.0，余量 19.7px。
- 补充：P1 band 左右栏（`Turin commence dimanche…` / `БОЖОЛЕ НУВО В ЧЕТВЕРГ СМ. С. 3, 6`）在 PIL 入盒检查内，无越边；目视 P1 无重叠。

## 8. 150 题逐题手验 — PASS（D1 除外）

- REG 转储（`dump_reg.py` 在 scratch 副本跑 content12/34/56/7/8；`reg-core.json` / `reg-ed.json`）：
  各 150 题；页/级/型 **0 差异**；键仅 **Q150** 异（核心 `开放题 — 要点见写作框，范文在第 8 版写作框内` →
  版 `Открытый вопрос — баллы в рамке; образец в рамке на с. 8`，读者语写作键，设计内差异）；
  Q148 键 `devant le`、注 `У кинотеатра`。
- 注 143 处中→俄：逐条读过，同事实；数字/日期归一化核对（中文数词 + 俄月份名转数字；
  `Лига 1` 专名剔除）0 差异；7 处注完全相同者均为法语语法注（Q16/17/18/35/97/103/138）。
  （Q124 注曾现终端显示乱码，字节核实为干净 UTF-8 `Нуво 19-го`，`expl.py:232` 与 `content8.py:316` 一致。）
- text.md（`ВСЕ ОТВЕТЫ` 块解析）：答案 **150 条**，键与 REG **150/150 全等**，注 **121 条**与 REG 全等，
  Q148 `devant le` ✓。
- 题干 vs 核心：string-freeze（`verify_ed_ru.py` §7）：缺失 0、豁免（已译 E 值）1、
  核心讲解残留 0、未说明 CJK 0。
- MCQ 选项完整性（`check_mcq.py`，45 体、1477 行）：**DEFECTS: 0，UNLOCATED: 0**。日志 `mcq.log`。
- 宽度预算（31 单行 + 4 对，`text_w`）：**0 超出**。
- Q148 题干：`(148)___ cinéma ?` 版/核逐字一致；P8 `du cinéma` 0 次。
- Q130：P8 `(989.0, 843.0)` 元素 `___`，版/核一致。Q36/Q37：P3 x=538.5 列 29 要素偏移全 +29.7（+30 档）。
- 目视 P1–P8：题干、选项、键、答案页逐题读过（PROOF-NOTE.md §6），键题契合；仅 D1 一处版式问题。

## 9. §1.1 / 杂项扫描 — PASS（`check_s11_ru.py`，日志 `check_s11_ru.log`）

- 纸色 `#fbfaf6` 矩形 8/8 页；颜色集版/核 19 色**完全一致**（无增无减）；
  VOL.4 / VOL.5 计数逐页与核相等；徽章 rect 逐页相等（[10, 12, 18, 15, 14, 15, 12, 38]，合计 134），
  颜色多重集逐页相等；A2/B1/B2 徽章色全在版内。
- U+2019 0、U+00B7 0、金色 `#b49a4a` 0、旧纸色 `#f7f1e2` 0；真实 CJK 字符 0（U+3000 共 369 处，均为分隔符）。
- "next Sunday" 版 SVG 全文 0 命中。

## 10. 孤儿扫描 — PASS（0 新增）

- 自写检测器（基线分组 ±1.5px + x 间隔 >400px 分栏；同基线分拆 <text> 合并）：
  版与核：标点独行基线 **0 处**、单字母独行基线 **0 处**；**0 新增**。
- 对照试验：合成孤儿 `。` 检出；同基线 `Итоги ещё неизвестны` + `.` 分拆不误报。
  （旧版检测器误报源于跨行拼接与同基线分拆——本检测器已修，见 PROOF-NOTE.md §7。）

## 11. 全页目视（P1–P8，印版 110dpi 渲染）— 除 D1 外通过

- 渲染件 `render/p1.png` … `render/p8.png`（交付印版 PDF 渲染）；另 `render/p7-boxbottom.png`（P7 盒底 300dpi 裁切）。
- P1：报头/头条/快讯/Q1–Q10 无溢出；Atget 图小白方块与核心同图（O3）。
- P2：日期表星期正确（16 周一…22 周日）；Q11–Q25 全契合。
- P3：Q26–Q43 全契合；**D1 位于 DATES 盒**（见 §7）；其余无问题。
- P4：Q44–Q61、数字盒、网球词表全契合；D5 只记录（见 PROOF-NOTE.md §5 O2）。
- P5：Q62–Q78 全契合；`Lukas Dhont` 拼写正确；Méliès 图注完整。
- P6：Q79–Q96、日历（23/10、4/11、9–17/11、18/11、20/11、26/11、9/12）与正文内部一致。
- P7：语法栏/金句/诊所 Q97–Q108 全契合；披露框 2 行在盒内（像素 + 裁切双证）；下期预告日期星期正确（23 日周一、27 日周五）。
- P8：Q109–Q150 全契合；Q130 空白行与核心一致（O1）；Q148 题干无 `du`；答案区 150 条与注齐全；Hiroshige 图注完整。

## 12. 未做 / 边界

- 未 commit、未 push、未改生产目录任何文件；重渲染只在 `scratch-proof-fr-ru3/rebuild/` 与 freeze out 目录做。
- D1 修复与重渲染由 builder 做；修后须整期重渲染 + 从头再做一轮全量校对（SOP §8.4）。
