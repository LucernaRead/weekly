# FIX-LOG — 2026-W47 ru-de（德语读者版）D1 修复 fix1

- **版**：`production/2026-w47/2026-w47-ru-de/`（目标语俄语 × 读者母语德语，VOL.4），re-fanout 重建版
- **修复员**：fix1；缺陷：proof2 结论 (b) 之 D1（P1 统计框标题溢出奶油盒，#1 D1 原样复现）
- **修法**：(a) 缩短德语副标题 — `Der Spieltag in Zahlen` → `Der Spieltag`（字号/换行不动）
- **时间**：2026-11-11 16:36–17:00 UTC；**未 commit、未 push**；修后由另一位独立校对员 re-proof，本人不自定稿
- **Scratch**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ru-de1/`
  （日志、重建副本、证据全在此；生产目录除本次修复与重建产物外零写入；core-ru 只读）
- **探针**：`echo test | git hash-object -w --stdin` 在 repo 内成功（`9daeafb9…`，`/dev/null` 正常存在）；
  TMPDIR 全程指向本 scratch 的 `tmp/`；解释器 `tools/venv/bin/python`

## §0 修前身份核对（三 SHA，与任务先验全符）

| 文件 | 修前 SHA-256 | 字节数 |
|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-de.pdf` | `26bfbcd169594a07595083f36f7306568eb4387f122ab6f94507c52141eadad2` | 21,231,822 |
| 网 PDF `Lucerna-VOL4-ru-de-web.pdf` | `99173b8cacdde82a5d1147b54d61d254f16a59e9d8858f246c0acd3958bed4ee` | 3,385,962 |
| 文 `2026-w47-ru-de.text.md` | `5ae444c8724da5b8d0c07874c3f4ce2ffc8a6a6f6dd8504ec3b00f49a732a911` | 63,516 |

证据：`evidence/pre-fix-sha.txt`；修前副本：`evidence/content12.py.PRE-FIX`、
`evidence/2026-w47-ru-de.text.md.PRE-FIX`、`evidence/map-de.json.PRE-FIX`、
`evidence/miss-tr-de.json.PRE-FIX`。

## §1 缺陷 D1 实测（修前，本人独立重测，非照抄 proof1）

- **位置**：P1 左中栏统计框，奶油盒 rect `x=538.5 y=1203.735 w=422.5` → 右缘 **961.0**；
  标题 23pt 粗体，基线 y=1240.735，六段 `<text>`，末段 x=726.6
  `　Der Spieltag in Zahlen`（Noto Sans CJK SC）。
- **本人实测**（`measure_title.py`，`OA.ink_box` PIL 真墨，`evidence/pre-fix-title-ink.txt`）：
  各段真墨右缘 600.5 / 620.5 / 722.9 / **997.6**；
  **标题真墨右缘 997.6，超框右缘 +36.6，越过下一栏左缘 989 达 +8.6** — 与 proof1 的 997.6 一致（独立复算，非引用）。
- **来源定位**：俄语主标题 `ТУР В ЦИФРАХ` 来自核心（core-ru `content12.py:48`
  `f.box("ТУР В ЦИФРАХ　数字看本轮", [`，只读，未动）；
  德语副标题来自本版两处 + 翻译表链（见 §2）。全版 `Der Spieltag in Zahlen`
  仅存于此两处原文 + 两张表，无其他版、无 cover、无他处。

## §2 改动源码行前后对照（仅改本版标题字面量，别无他改）

| # | 文件 | 行 | 改前 | 改后 |
|---|---|---|---|---|
| 1 | 版内 `content12.py`（渲染字面量） | 48 | `f.box("ТУР В ЦИФРАХ　Der Spieltag in Zahlen", [` | `f.box("ТУР В ЦИФРАХ　Der Spieltag", [` |
| 2 | 版内 `2026-w47-ru-de.text.md`（导出文本） | 25 | `### ТУР В ЦИФРАХ · Der Spieltag in Zahlen` | `### ТУР В ЦИФРАХ · Der Spieltag` |
| 3 | `scratch-fanout-ru/map-de.json`（编译表） | 96 | `"ТУР В ЦИФРАХ　数字看本轮": "ТУР В ЦИФРАХ　Der Spieltag in Zahlen"` | `"ТУР В ЦИФРАХ　数字看本轮": "ТУР В ЦИФРАХ　Der Spieltag"` |
| 4 | `scratch-fanout-ru/miss-tr-de.json`（表源） | 33 | 同上（`lit` 节） | 同上 |

- **为什么改 4 处**：`ru_textmd.py` 的导出说明证实 text.md 由 `content*.py` 派生
  （`U+3000 → " · "`）；`build_map.py` 证实 `map-de.json` 由 `miss-tr-de.json`（+ tm2）合并生成。
  只改表不改渲染字面量是空修；只改渲染不改表，重 fanout 会复活长式。
  故渲染字面量（#1）+ 导出（#2）+ 表源（#4）+ 编译表（#3）四处同步。
  `KEEP_AS_IS`（`scratch-fix-ru-d1/build_map.py`）不含此串，无旁路。
- **同步核实**：`ru_textmd.py` 重导出到 scratch 临时文件，与手改后的 text.md **0 diff**
  （63,506 B，150 题，277 块，`evidence/regen-textmd.log`）；
  修前/修后 text.md diff **恰 1 行对（L25）**；text.md 63,516 → 63,506 B（−10 B = 删 ` in Zahlen`）。
- **残留检查**：修后版内 `.py/.md/.txt/.svg` 全文 + 两张表，`Spieltag in Zahlen` **0 处**；
  `backup-old` 未动（仍含长式 ×1，作对照基准）；core-ru `content12.py` SHA 修前修后同为
  `1f4c42a91c304d4233f510aaa3ef38a9ff1c58ee121faa5f3b9424ace01d8cd9`。

## §3 重建

- `run.py`：**rc=0，TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE**（`render/run.log`）
- `render.py`：**rc=0**，8 张 cards + 印 PDF 21,231,616 B（`render/render.log`）
- `webpdf.py`：**rc=0**，网 PDF 3,385,828 B，57,837 text bytes（`render/webpdf.log`）

## §4 修后三 SHA（新交付件；网 PDF 的 SHA/字节数不可复现，只比文字层）

| 文件 | 修后 SHA-256 | 字节数 |
|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-de.pdf` | `872b4f1c05d682f4f8a18749b7d63215a09bc2a151c3ca1601ef454de4019ebd` | 21,231,616 |
| 网 PDF `Lucerna-VOL4-ru-de-web.pdf` | `c8c21903a406914f52550810feebd351d7c7fa5a229cce606a59474170e6354d` | 3,385,828 |
| 文 `2026-w47-ru-de.text.md` | `8a5f1a9b75da5ada55ecc82df6dc05c78a5f35f6e5b93381e25d521a8c9ee44d` | 63,506 |

## §5 D1 修后实测（本人独立重测，两法一致 + 目视）

- **OA.ink_box（与修前同法）**：末段 `　Der Spieltag` 真墨右缘 **887.9**，框右缘 961.0，
  **余量 +73.1**（要求 ≤957，即 ≥4px 余量；实余 73.1）→ **PASS**（`evidence/post-fix-title-ink.txt`）
- **400 dpi 印 PDF 光栅复核**（独立第二法，`evidence/post-fix-raster-ink.txt`）：
  P1 标题带 y1215–1250 真墨右缘 **888.0**（SVG 单位），余量 **+73.0** → **PASS**；
  与字体法 887.9 相差 0.1（舍入级一致）。
- **目视**：`crops/d1-p1-subtitle-FIXED.png`（400 dpi）— `ТУР В ЦИФРАХ　Der Spieltag` 词尾完整在奶油盒内，
  盒右缘在词尾之外留有明显奶油余量；P1 整页卡 `cards/p1-pervaya.png` 目视：版式无位移，
  统计框、后续 `СЕЙЧАС ВЫ` 节、测验、照片、页脚均在位。

## §6 全部门禁（自跑；驱动 `run_gates_fix.py`，由 proof2 同名脚本改路径复用）

| 门 | 命令/方法 | 结果 |
|---|---|---|
| run.py | 见 §3 | rc=0，TOTAL 150，0 溢出 |
| Occlusion 真实审计 | `tools/occlusion_audit.py <版>/svg --json gates/occlusion.json`（未加 `--selftest`） | **42 TEXTX / 0 LINEX**（rc=1 为有 flag 即 1，预期内） |
| Occlusion 像素裁决 | `adjudicate_fix.py` Part A v3（1× 网格卡片墨阈值 min-channel < 140） | **33 像素 CLEAR + 9 目视 CLEAR = 42/42 CLEAR，0 真重叠**（`gates/adjudicate2.txt`） |
| 9 项目视 CLEAR | 自制 `crops/flags-contact-sheet-FIXED.png`（3× 放大）逐项目视 | 9 项与 proof2 逐项同框同值（flag 7/8 P1、11/12 P2、20/21 P4、28/30 P6、37 P7），均为词与后随标点/引号分离字形，词间有空隙，无触碰 |
| Occlusion Part B（boxtitle 真墨扫描） | `adjudicate_fix.py` Part B v2 | **零报告**：无过页缘、无过内容缘、无过奶油盒 — **D1 已从 Part B 消失**（修前报 997.6） |
| p8 compare | `tools/p8.py compare`，**直接读 `gates/p8-compare.json` 本体** | **CLEAN，150/150**；`status=CLEAN`，`missing/extra/uncertain=[]`，`keydiff=[137,138,139,140]`；与 core `ru-p8.json` 直接比对 keydiff 亦恰为 `['137','138','139','140']` |
| p8 extract | `tools/p8.py extract --total 150` | 150/150；Q20 键 `желании`（= core 键）；Q150 印 `✓` |
| keycheck 150 | text.md 答案键 vs P8 印出键 | **0 不符 / 149（Q150 除外，开放写作题印 ✓ 属设计）**；即仅 Q150 不同；答案 150 项连续；范文 97 词 |
| check_core | `check_core.py <版>`（cwd=版目录，带参） | **rc=0**；golden BAD **0**、gloss fails **0**；orphan 1（P7 y553 `”».`，核心同类良性）、same-baseline 碰撞 1（P1 y1712 `чёрная`，核心同类）（`gates/check_core.log`） |
| s11_check | `s11_check.py <版>` | **rc=0，`FAILURES: none`**；8 SVG、纸色 `#fbfaf6`、徽章色、VOL.4 家具、左缘 88.0、可视 SVG 零真实 CJK、网 PDF 8 页 < 7 MB 均 PASS |
| freeze 标准口径 | `freeze.py baseline --build <core-ru> --core-svg <core-ru>/svg --out gates/freeze-core` | **8/8 字节一致**，`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)` |
| freeze 补充 | `freeze.py baseline --build <版> --core-svg <版>/svg --out gates/freeze` | 亦 8/8（版内自洽补充，不冒充标准口径） |
| freeze diff | `freeze.py diff --core-svg core-ru/svg --edition-svg <版>/svg` | removed 851（distinct 486）；**西里尔删除恰 15 项，全部在 P8**：`Билибин、Билибина、Зимняя、Иван、Ивана、Иллюстрация、Морозко、год、достояние、иллюстрация、к、можно、ноябрю、общественное、сказка` 各 ×1 = Q46 `можно` + 14 个 Morozko 图注词（图按设计跳过），unexplained 0；新增 CJK 仅 U+3000 ×8 |
| 印/网文字层 | PyMuPDF，非空白字符 multiset | **总体 + 逐页 8/8 全等，31,001 字符**（修前 31,009，−8 = 删 `inZahlen` 8 个非空白字符，一致）；网 PDF 3,385,828 B < 7 MB；印/网各 8 页 |
| D3 斜体 | 印/网斜体跨度 | 印 **3** = 网 **3**：`«` Newsreader Italic、`чёрная пятница` NotoSerif-MediumItalic、`»`；网版为同系 Lucerna 前缀斜体；`пятница»` 印/网各 7 处，脱离式 `пятница »` 0 处 |
| P8 最小字号 | PyMuPDF 实测印 PDF | **9.75 pt**（全刊最小亦 9.75 pt）≥ 9.75 |
| creambox 正典扫描 | `tools/creambox.py`（`hidden_files/w47/tools/`）全版 8 SVG | **框内负余量 0**；BELOW-WINDOW 95 行，全为 +28.0（×25）/+32.0（×41）/+34.0（×4）/+37.0（×25）下一标题类，unclassified 空；vs backup-old diff **仅 2 行**，即标题行本身（−`Der Spieltag in Zahlen` / +`Der Spieltag`，y=1240.7，clearance +343.0） |
| SVG CJK 扫描 | 可见文本 `[\u3400-\u9fff\u3040-\u30ff]` | **零真实 CJK**；U+3000 ×123（家具分隔符） |
| verify_ed.py | ru-de 无此脚本 | 如实记录：现存均为 en-core 系，不适用；等效覆盖由 check_core（rc=0）+ s11（rc=0）+ keycheck（0 不符）+ p8 compare（CLEAN）提供 |

注：门禁驱动初版沿用了 proof2 脚本的无参 `check_core.py` 调用（rc=1，`IndexError: list index out of range`），
此为驱动 bug，非版缺陷 — 已按 proof2 GATE-LOG §8 的同类纠正带参重跑，rc=0；
`gates/gates.json` 的 `check_core_rc` 已更正为 0 并附注，`gates/check_core.log` 为带参重跑日志。
`gates/run.log` 内仍保留原始无参调用痕迹，可与本注对照。

## §7 回归复验（D2 / D3 / D6 / kicker，均存活）

- **D2（Q25 `День студента`）**：text.md 全称 `Международный день студента` ×2（= core ×2）；
  短式 `День студента` ×11；P2 SVG y=2162 行现为短式（SVG 文本集 diff 仅该行 7 键）。
- **D3（网 PDF 斜体 3=3、`»` 紧贴）**：见 §6，斜体印 3 = 网 3；`пятница»` 印/网各 7 处，脱离式 0 处。
- **D6（`желании`）**：text.md ×2；P8 印出键 Q20 = `желании` = core 键；P2 SVG 计 0（预期：P2 只有题干空白，键只印 P8）。
- **Kicker 间隙**：11 token，9 处间隙 **[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]**，最小 **5.9 px ≥ 4**。
- **D1 其余 4 串**：s1 `УЧЕБНЫЕ ДАННЫЕ` text.md L459 ✓、s3 `Три уровня, три темы` L504 ✓、
  s4 `Большой тест недели + все ответы` L596 ✓、s2 免责声明不在 text.md ✓；4 串全在 SVG（p6 s1/s2、p7 s3、p8 s4）✓。
- **`___` 字面**：87 处，与修前同（核心继承的模板缺口，不作本版缺陷）。

## §8 SVG 文本集回归对照（新 vs backup-old，逐键）

| 页 | 变化键数 | 内容（全部在预期区域内） |
|---|---|---|
| p1 | 41 | y=372 kicker 双空格重排 40 键（重建既有）+ **y=1240.7 标题 1 键：本次修复唯一新增变化** |
| p2 | 7 | 全在 y=2162，Q25 选项 b 短式化（D2，既有） |
| p3 / p4 / p5 | 0 | 完全相同 |
| p6 | 24 | y=1552 图表标题 `УЧЕБНЫЕ ДАННЫЕ` + y=1582 俄语免责声明（D1 map fix，既有） |
| p7 | 18 | 全在 y=168，D1 s3 副标题重排（既有） |
| p8 | 23 | y=1937.3 Q20 键 `желание`→`желании`（D6）+ y=168 D1 s4 副标题重排（既有） |

text.md vs backup-old：**14 行（7 对）** = 修前 6 对 + 本次 L25 1 对，别无其他。

## §9 D5 字体（只记录，不判定）

- 印 PDF：按页 `get_fonts` 计 **72 字体引用 / 69 distinct**，含 Newsreader16pt-Italic、
  NotoSerif-MediumItalic、NotoSerifCJKsc-Regular（×4）；网 PDF：**72 引用 / 69 distinct**，
  Lucerna 前缀同系字体，含 LucernaNewsreader-Italic、LucernaNotoSerif-Italic。
  （计数法与 proof2 的 65 引用不同——proof2 未注明口径；此处只记录本次口径下的实测值，不作比较判定。）
  完整清单：`evidence/d5-fonts.txt`。斜体 3=3 的等效性见 §6 D3 行。

## §10 作用域核查（写了什么、没碰什么）

- **改了**：版内 `content12.py:48`、`2026-w47-ru-de.text.md:25`；
  翻译表 `scratch-fanout-ru/map-de.json:96`、`miss-tr-de.json:33`（防重 fanout 复活）；
  重建产物：`svg/*.svg` ×8、`cards/*.png` ×8、印/网 PDF 各 1。
- **没碰**：core-ru（`find -newermt -3h` 零文件；`content12.py` SHA 修前修后一致；
  freeze 标准口径复核 core SVG 未变 8/8）；其他版（`Der Spieltag in Zahlen` 残留 0 处之外，
  本次无任何他版写入）；`backup-old`（对照基准未动）；repo `tools/`（`freeze.py` 等的
  `M` 状态与 mtime 均早于本次会话，为并行他工既有改动，本次未改其中任何文件）；
  `scratch-fanout-ru/map-en.json` 于 16:52:43 的改动为并行他工，本次未碰。
- **git**：HEAD 仍为 `c0382fa7f6c0915057611d714f75949d81a29956`；**无 commit、无 push**。
  （repo 内另有大量并行他工的 tracked 改动，与本次无关。）

## §11 交付与结论

- **新三 SHA**（见 §4）：印 `872b4f1c…9ebd` / 21,231,616 B；
  网 `c8c21903…54d` / 3,385,828 B；文 `8a5f1a9b…44d` / 63,506 B。
- **D1 已修**：修后真墨右缘 887.9（字体法）/ 888.0（400 dpi 光栅法），框内余量 +73.1 / +73.0，
  400 dpi 裁切图目视词尾完整在框内；全部门禁绿灯；D2/D3/D6/kicker 回归全部存活；
  SVG 文本集相对 backup-old 的唯一新增变化即标题本行。
- **未定稿**：按任务，修后由另一位独立校对员 re-proof；本 FIX-LOG 为修复记录，不作定稿结论。
- **证据索引**（本 scratch 内）：
  `FIX-LOG.md`（本文件）、`measure_title.py`、`run_gates_fix.py`、`adjudicate_fix.py`、
  `evidence/`（修前 SHA、修前副本、修前/修后标题真墨、光栅真墨、导出同步日志、D5 字体清单）、
  `gates/`（`gates.json`、`run.log`、`occlusion.json`、`p8-compare.json`、`p8-ed.json`、`p8-core.json`、
  `freeze-diff.json`、`creambox.log`、`creambox-vs-backup.diff`、`check_core.log`、`adjudicate2.txt`）、
  `render/`（`run.log`、`render.log`、`webpdf.log`）、
  `crops/`（`d1-p1-subtitle-FIXED.png`、`flags-contact-sheet-FIXED.png`）、`tmp/`（导出重生成件）。
