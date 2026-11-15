# D5 重建报告 — 2026-w45-ru-ja（日语读者版）

W45 ru 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans）。施工 2026-11-14 至 2026-11-15；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-ru/logs/2026-w45-ru-ja/`（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表）。门禁总表复本（D29）：`production/notes/2026-w45/g-ru/scratch-d5-rebuild-ru/logs/2026-w45-ru-ja/GATES-SUMMARY.txt`。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core ru --week 2026-w45` → `production/2026-w45/core-ru/svglib.py`，`_D5_READER = "latin"`（D24：core 常量惰性，见§六）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-ru-ja/svglib.py --target ru --reader ja --week 2026-w45`（先 `--check` dry-run，mode cjk 正确）。装后 `_D5_READER = "cjk"`。
- D26 核实：ru 读者版旧分支 `if _D5_READER == "ru":` 存在（count 1），fix-xru 标记 0（fix-xru 仅 W47，不带入三周重修）。本家无 ru 读者版（mode ru ×0），D26 以代码存在性核实。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（4 处）。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `style-port-ru/textexp_ru.py`（AST 路由）导出（第 0 步已核实：试跑 vs issues 已发 `.text.md.new` BYTE-IDENTICAL；fr 家导出器未用）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 KIT 旧 pins 一致性：基线印 PDF 16149279 字节，sha256 `26fccfb16ec3879ce5b296f5fa1f3f59070ede68c4a477edabac82995f6f5c16`（KIT 旧 pins 为 fanout 期旧值，不可作基线——KIT SHA-lag 修正案）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF **非空字符差 0**，仅空格数浮动（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **204**（>0，符合装机前提），西里尔 0，花括号 CJK 0。
- 基线 P8 口径：noted **150/150**；p8 compare CLEAN，keydiff=[137, 138]；P8 199 / 61.4 行/余量。
- 基线既有缺陷：G6 2 TEXTX（P1 斜体行，见§三 F-2）；G11 1 SPILL（既有缺陷，基线同值）；D18 gap 198.3px。

## 三、缺陷与修法（run1 → run2）

run1 全部缺陷均为 D5 字体切换的几何后果（Noto Sans 比 Newsreader 宽）或既有缺陷（基线同值）。修法只动字号与框高，**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | occlusion (G6) | P1 «первая» 斜体行 y=1712 «сокращённый день» | 2 TEXTX（审计误报，见下 F-2） | **不修**：裁定接受（D22 类），run2 同值 |
| 2 | spill (G11) | P7 读者来信框末行 | 框底 BELOW +10.7px（基线同值，既有缺陷） | `content7.py` 盒高公式尾数 +26→**+46**（盒高 +20；盒底 1727.6→1747.6；引言线净空 ≥8.4px） |
| 3 | run (G1) | kinsoku 移植块 | `NameError: face`（core-zh-tw 移植的 `text_w` 带 `face` 参，ru-ja 的无） | patched ja svglib 3 处调用（L248/275/281）去掉 `face` 参；重跑 RC=0 |

**F-2 裁定（G6 TEXTX ×2，全家 11 版相同）**：审计用 REGULAR 字宽量斜体 run，构建用斜体字宽量——
300 dpi 像素证据（`logs/adjudication-g6/`）：«сокращённый» 与 «день» 之间实隙约 2.5 SVG 单位；
«день»→»» 名义触碰 0.15 单位 = 0.016 mm，低于一个光栅像素。字号比与间隙比无关，降字号清不掉。
基线已发版同形同值（既有内容，零 D5 回归）；y=1712 斜体行 11 版基线+run1 逐字节相同（hash `26221892ff4c`）。
D22 类：非 finding，不阻塞 ALL-GREEN。

P8 变化：199 / 61.4 → 199 / 61.4 行/余量（run1 → run2 不变，修复未动 P8）。

## 四、门禁（run2，全套 16 门 + D18 + D37）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、花括号 CJK 0 |
| 4 render | RC=0，印 PDF 16128164 B |
| 5 webpdf | RC=0，网 PDF 2484226 B（< 7 MB） |
| 6 occlusion | 2 TEXTX（裁定接受，见§三 F-2） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**（exit 0，missing=[]，extra=0；keydiff=[137, 138]） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 67，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（Fix A 后 0 SPILL） |
| 12 boxtitle | 0 DEFECT（52 / 741；run1 为 738 行，盒高修复后重计数） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 199 / 61.4 → 199 / 61.4） |
| 15a 文字层 print=web | 字符多重集差 **0**；text.md BYTE-IDENTICAL |
| 16 census_quotes | 0 defective |
| D18 刊头 | gap **190.9px** PASS |
| D37 副刊头 | N/A（本版无副刊头行） |
| 17 家族 gates.py | ru 家无 gates.py |

**OVERALL: 除 G6 裁定项外全部 GREEN。**脚本字面 RESULT 为 NOT-GREEN（G6 计 FAIL=1），家族结论为 ALL-GREEN modulo F-2 adjudication；无进一步修复轮。

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`；网 PDF 跨次字节不确定，closer 须拷 builder 原件，绝不重跑 webpdf）

- 印 PDF：`Lucerna-VOL2-ru-ja.pdf`，**16128164 字节**，
  SHA-256 `183acf2d63291fa0dbc7e4877b1932206b2d929ace6f9b7dff2979ec2ac3c178`
  （D5 前基线 16149279 字节）。
- 网 PDF：`2026-w45-ru-ja.web.pdf`，**2484226 字节**，
  SHA-256 `03d18d52c5b6e15377aaa58b1d8de947ba63326a1108e76a50fb4dd4e6ff6c41`。
- text.md：`2026-w45-ru-ja.text.md`（**新文件**——issues/ 目前无 ru 版 `.text.md`；与 fanout `.text.md.new` **BYTE-IDENTICAL**），53262 字节，SHA-256 `d156bb302c4abf6f6368f08749ab96cee5992ecbe4bc83648d01460ec3a72b1b`。
- 练习总量仍为 **150 题**，与 core 逐题一致。

## 六、KIT

- `production/2026-w45/2026-w45-ru-ja/WEEKLY-KIT.md`：本版 KIT §9 Deliverables & measured pins pins 更新；文末追加 §12 D5 rebuild 节。
- 生产源同步（closer）：patched/ → 2026-w45-ru-ja/：`svglib.py` + `content7.py`（本版有 content7.py 修复）。
