# ru-nl fix1 — GATE-LOG（门禁逐项实测）

版目录：`production/2026-w47/2026-w47-ru-nl/`；核心对照：`production/2026-w47/core-ru/`（fix1，未动）。
工具：`~/workspace/weekly-git/tools/venv/bin/python`；共享工具 `tools/{freeze,p8,occlusion_audit,webpdf}.py`。
完整原始输出：`gates.log`（run_gates.sh），`run.log` / `render.log` / `webpdf.log` / `textmd.log`。

## 重建

| 步 | 命令 | rc | 实测值 |
|---|---|---|---|
| run.py | `tools/venv/bin/python run.py` | 0 | TOTAL 150（A2 50 / B1 76 / B2 24；分页面 10/18/18/18/18/18/12/38）；FLOW OVERFLOW 0，HEAD TOO WIDE 0；`P8 morozko SKIPPED: no room`（与改前一致，设计使然） |
| render.py | `tools/venv/bin/python render.py` | 0 | 8 cards；印 PDF 21,291,643 B |
| webpdf.py | `tools/venv/bin/python tools/webpdf.py svg Lucerna-VOL4-ru-nl-web.pdf` | 0 | 网 PDF 3,387,332 B，57,957 text bytes |
| ru_textmd.py | `ru_textmd.py . 2026-w47-ru-nl.text.md "VOL.4 · Russian text · Dutch explanations"` | 0 | text.md 64,051 B，150 exercises，277 blocks |

## 门禁

### g1 check_core.py — rc=0 PASS
- golden BAD: 0；gloss fails: 0；P8 svg text chars: 11,138。
- orphan line-starts 1 项：`('p7-yazyk.svg', 553, '”».')`——与改前构建完全相同（良性类，见 KIT）。
- same-baseline collisions 1 项：`('p1-pervaya.svg', 1712, 'чёрная', ' ')` total 1——与改前构建完全相同。

### g2/g3 p8.py extract — rc=0 PASS
- core `core-ru/svg/p8-test.svg`：noted set = 150 of 150（parse: lines）。
- edition `2026-w47-ru-nl/svg/p8-test.svg`：noted set = 150 of 150（parse: lines）。

### g4 p8.py compare — rc=0 PASS
- `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]`（150/150，双侧）。
- 直接 JSON keydiff（新 `ru-nl-p8.json` keys vs 新 `core-p8.json` keys）：`[137, 138, 139, 140]`——与改前构建一致；其余 146 键与核心逐字相同。

### g5 occlusion_audit.py 真实审计（无 --selftest 标志；工具内部先过合成自检）— 42 flags
- 审计命令：`tools/occlusion_audit.py <版>/svg --core <core-ru>/svg --json ru-nl-occlusion.json`。
- 内部自检：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`。
- 结果：`42 flags {'TEXTX': 42}`，LINEX 0，COVER/FOOTER/EDGE/BOXTITLE 0；审计 rc=1（有 flags 时的预期退出码）。
- 旗标集合与改前构建的 `ru-nl-occlusion.json` **逐项完全相同**（42/42，page/class/text/detail 全等）——本次改动未引入新旗标。
- `--core` 附带输出：`core: 42 flags; NEW vs core: 3`（系 core 与 fan-out 的固有差异，与改前一致，非本次引入；旗标集合本身与改前构建相同）。

### g5b 遮挡裁决（交付 PDF 实测为准）— 42/42 CLEAR
- 工具债（已证实）：上游 `adjudicate_ru.py` 硬编码 `SX = 1950/1800`（假设 PNG 宽 1800）；本族 cards 为 1950 宽（render.py output_width=1950），正确 SX 应为 1.0。本 scratch 内已打补丁的副本 `adjudicate_ru_fix1.py`（SX=1950/1950，另加 `ADJ_CARD_DIR` 覆盖）。
- 三种裁决对照（同一 42 旗标）：
  - 上游 SX（1950/1800）× cards：42 CLEAR（与改前构建报数一致——该数是错标尺下的结果，仅作交叉对照）。
  - 修正 SX=1.0 × cards：38 CLEAR / 4 OVERLAP（p1 Краснодар ×1，p4 Краснодар ×3，均为 J=231 或 1172）。
  - 修正 SX=1.0 × **交付印 PDF 光栅**（fitz 1950×2700 逐页渲染，`pdf-pages/`）：41 CLEAR / 1 OVERLAP（p7 Кипренского J=565 darkbg）。
- 5 个争议旗标逐个交付 PDF 实测（`adj-*.png` 裁图 + 列墨计数）：
  - p1/p4 Краснодар ×4：交付 PDF 在 J 列确有 1px 全背景列（J 列墨像素 0，两侧墨列 9px/4px），另有 7–14px 宽背景段；裁图见 `adj-p1-pervaya-231.png`、`adj-p4-sport-231.png`、`adj-p4-sport-1172.png`——“р»” 间隙肉眼清晰。**CLEAR（gap=1px，紧但真实）**。cards 上判 OVERLAP 是 CairoSVG 抗锯齿在该 1px 列留下 ≥2 墨像素所致——渲染器差异，非真实重叠。
  - p7 Кипренского ×1：交付 PDF 裁图 `adj-p7-yazyk-565.png` 显示“Кипренского, 1827”干净、间距正常。OVERLAP 是裁决器背景误判：`bg_dark()` 采样行落进图注上方的深色照片（median 105 → 判 dark），把白纸底（亮像素 >160）全算成墨。改用正确浅底逻辑（墨 = v<180）重测图注行 rows 1490..1508：逗号墨右缘 x568 → “1”墨左缘 x577，**8 空白列**，邻间隙 1–3 列。**CLEAR**。
- **结论：交付 PDF 实测 42/42 CLEAR，无真实重叠。**

### g6 freeze baseline — rc=0 PASS，8/8
- 命令：`tools/freeze.py baseline --build <core-ru 版目录> --core-svg <core-ru>/svg --out <scratch>/freeze --json freeze-baseline.json`。
- `baseline: 8/8 SVGs byte-identical (repointed files: none)`；8 页逐一 OK；core integrity：shipped core SVGs unchanged by the run（8 files re-hashed）。

### g7 freeze diff core→edition — rc=0，无回归
- 逐页 +/− 串数与改前构建完全相同：p1 +19/−22，p2 +36/−37，p3 +26/−28，p4 +28/−28，p5 +27/−27，p6 +34/−33，p7 +47/−50，p8 +178/−629；TOTAL added CJK 8（每页 `\u3000` ×1）。
- removed total：487 条（全局去重 460），改前改后相同。
- 全 diff 唯一变化（p7 added_strings）**：旧 `"\u3000Drie niveaus, drie thema’s"` → 新 `"\u3000Drie niveaus, drie thema's"`——恰为 D7 本句，diff 如实捕获。其余 7 页 added/removed 集合完全相同。

### g8 s11_check.py（§1.1）— rc=0 PASS，FAILURES: none
- 8 SVG；paper #fbfaf6；禁色 #f7f1e2/#c9a227/#8b4513/#000000 均无；徽章 A2 #5c6e30 / B1 #46581f / B2 #37402f；foot 含 VOL.4 + 全角空格；拉丁读者版无 CJK 可见字；masthead 196px；band title 46px；左 margin ≥87（88.0）。
- 网 PDF 8 页 <7MB（3,387,332 B）；web text > 0；印 PDF 8 页。
- **P8 min font 9.75pt ≥ §1.1 下限 9.75pt**（s11_check 与 g10 fitz 双法一致）。

### g9 印/网文字层逐页一致 — rc=0 PASS
- pdftotext 字节：印 110,893 = 网 110,893；fitz 全文字符 multiset 一致：37,531 vs 37,531。
- 逐页 multiset 一致：`[True ×8]`（P1–P8 全过）。
- （注：改前构建 RECORD 记 31,087 字符，系 pdftotext multiset 口径；本轮用 fitz 全文口径 37,531，两侧同口径一致即过门。）

### g10 P8 最小字号（fitz，双 PDF）— PASS
- 印 PDF P8 min font：**9.75pt**（908 spans）；网 PDF P8 min font：**9.75pt**（908 spans）。

## 未改动项复核（D1/kicker/D2/D6 存活）

- D1：P6 `УЧЕБНЫЕ ДАННЫЕ` + full 俄语 disclaimer（`Это учебный опрос редакции для упражнений — не настоящая статистика`，content56.py 原句亦在）存活；P7 副标 `Три уровня, три темы` 存活（SVG 按词分 `<text>`，逗号独立成元—— joined 文本为 "Три уровня , три темы"，归一化后匹配）；P8 副标 `Большой тест недели + все ответы` 存活；text.md 含 D1 诸标记。
- D2：Q25 选项 `День студента` 存活（P8 joined 文本）；`Международный день студента` 全句在 text.md 中 ×2。
- D6：Q20 key `желании` 存活（P8 SVG 内；p8 extract key 20 = `желании` = core `ru-p8.json` key 20）。
- Kicker：content12.py:18 双空格存活（`ЕЖЕНЕДЕЛЬНАЯ  ГАЗЕТА  ДЛЯ  ИЗУЧАЮЩИХ  РУСС…`）。
- SVG 变化清单：仅 `svg/p7-yazyk.svg` 变化，其余 7 页 SHA-256 与改前完全相同（`svg-before.sha256` vs `svg-after.sha256` diff 仅 1 行）。
