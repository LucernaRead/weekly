# D5 重建报告 — 2026-w43-en-it（意大利语读者版）

W43 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-it/`
（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表，
`logs/2026-w43-en-it-run1/` 为 run1 日志快照）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w43`
  → `production/2026-w43/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-en-it/svglib.py --target en
  --reader it --week 2026-w43`（先 `--check` dry-run，10 项改动 + mode latin 正确）。
  装后 `_D5_READER = "latin"`；装后 svglib md5 与 de/es/fr/nl/pt 全同
  （`6c3596c1e919`）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（66 PASS）；fix2 块保留。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由
  `scratch-prep-p3b/en_textmd_w43.py` 导出（P3b T5 已验与 issues 已发版字节一致）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 149**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `MANIFEST-W43-D1.md` 差 −79 B（元数据浮动，同批 4 版之一）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF
  **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，
  零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **550**、西里尔 0、弯引号在 CJK **1**（>0，符合装机前提）。
- 基线 P8 口径：noted **62/149**（与 core 同口径；de/fr 两版为 149/149）。

## 三、缺陷与修法（run1 → run2）

run1 共 6 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比
Noto Sans CJK 宽约 5.7%），另有 1 项既有缺陷（P2 spill，基线同值）。修法只动字号，
**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P4 `C　COMPARATIVES　Comparativi` | 25pt 宽 444.0px，超栏 21.5（栏宽 422.5） | `content34.py:158` 25→**23**（408.5 ✓；24pt 426.2 仍超 3.7） |
| 2 | head_check | P5 `EARNINGS, IN PLAIN ENGLISH` | 26pt 宽 425.1px，超 2.6 | `content56.py:23` 26→**25**（408.8 ✓） |
| 3 | occlusion | P1 暗带标题与副标 `SPOSTA L'ORA` 重叠 | 55.5×20.8px（副标 27pt 左缘 x=1649.0，全家最窄副标） | `content12.py:25` 暗带标题 46→**44**（右缘 1613.6，advance 空隙 35.4px；44 即够，无需降到 42） |
| 4 | creambox / boxtitle | P1 `THE WEEK IN NUMBERS　In cifre` | +3.5px | `content12.py:43` 加 `tsize=22`（389.9 ✓） |
| 5 | boxtitle | P1 `IN THIS ISSUE　In questo numero`（目录框眉，非 box() 标题，是裸 `p.text` 24pt） | +11.1px | `content12.py:88` 24→**22**（宽约 411.6→377.3，余量约 −23px） |
| 6 | spill | P2 `Check your number !` 跌出 DID YOU KNOW 框底 | +12.71px | `content12.py:193` 框高公式尾数 +14→**+34**（框底 +20px；与 core-en 同款既有缺陷，基线同值） |

P8 变化：193→**189** 行，距页脚线余量 32.7→**52.8 px**（正，无溢出）。

## 四、门禁（run2，全套 17 门 ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 149，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0 |
| 4 render | RC=0，印 PDF 7,493,650 B |
| 5 webpdf | RC=0，网 PDF 1,063,082 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 62/149（与 core 同口径） |
| 8 p8 compare | **CLEAN**（missing=[]，extra_count=0；keydiff=[136, 139, 149]——与 KIT 记载的读者语答案键一致） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（168 OBSERVE） |
| 12 boxtitle | 0 DEFECT（57 titles，275 body lines；本次以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 193→189，slack 32.7→52.8） |
| 15 文字层 print=web | 字符多重集差 **0** |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | en 家无 gates.py（`audit_en_fr.py`/`audit_en_es.py` 是旧版几何审计前身，不算 gate） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL1-en-it.pdf`，**7,493,650 字节**，
  SHA-256 `d54137e00e209de5bdc1cbc1eb4aa46c8025de56c8c184af3b37636363ce592e`
  （D5 前 KIT 记值 8,615,022 字节）。
- 网 PDF：`2026-w43-en-it.web.pdf`，**1,063,082 字节**，
  SHA-256 `6416281b07a3362325c86e1a4fa4206a1b9578815923b0fb880e3b0504180d0a`
  （D5 前 issues 已发版 1,103,724 字节，`32aaebd8…`）。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**
  （SHA-256 `dbc0c91d5d3dc47692126dbc91f00a2c084e758c05cf2ed538124d6520108829`）。
- 练习总量仍为 **149 题**。

## 六、KIT

- `production/2026-w43/2026-w43-en-it/WEEKLY-KIT.md`：交付物 pin 行追加 D5 交付物
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **D5 rebuild（2026-11-13）** 节
  （装机、基线、缺陷与修法、门禁 ALL-GREEN、新交付物）。
