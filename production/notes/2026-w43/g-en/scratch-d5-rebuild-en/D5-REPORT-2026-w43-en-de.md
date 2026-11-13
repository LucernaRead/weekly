# D5 重建报告 — 2026-w43-en-de（德语读者版）

W43 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-de/`
（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表，
`logs/2026-w43-en-de-run1/` 为 run1 日志快照）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w43`
  → `production/2026-w43/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-en-de/svglib.py --target en
  --reader de --week 2026-w43`（先 `--check` dry-run，10 项改动 + mode latin 正确）。
  装后 `_D5_READER = "latin"`；装后 svglib md5 与 de/it/nl/pt 四版全同
  （`6c3596c1e919`）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（66 PASS）；fix2 块保留。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由
  `scratch-prep-p3b/en_textmd_w43.py` 导出（P3b T5 已验与 issues 已发版字节一致）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 149**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `MANIFEST-W43-D1.md` 逐字节一致（7 行精确一致之一）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF
  **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，
  零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **592**、西里尔 0、弯引号在 CJK **1**（>0，符合装机前提）。
- 基线 P8 口径：noted **149/149**（fanout 全量口径；core 为 62/149）。

## 三、缺陷与修法（run1 → run2）

run1 共 11 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比
Noto Sans CJK 宽约 5.7%），另有 1 项既有缺陷（P2 spill，基线同值）。修法只动字号，
**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P4 `D　VERB FORMS　Vergangenheit` | 25pt 宽 428.0px，超栏 5.5（栏宽 422.5） | `content34.py:167` 25→**24**（410.9 ✓） |
| 2 | head_check | P5 `EARNINGS, IN PLAIN ENGLISH` | 26pt 宽 425.1px，超 2.6 | `content56.py:23` 26→**25**（408.8 ✓） |
| 3 | head_check | P5 `C　THIS WEEK, LIVE　-ing-Form` | 25pt 宽 423.5px，超 1.0 | `content56.py:54` 25→**24**（406.5 ✓） |
| 4 | head_check | P6 `READING THE CHART　Diagramm` | 24pt 宽 432.3px，超 9.8 | `content56.py:188` 24→**23**（414.2 ✓） |
| 5 | head_check | P7 `THE TOOLBOX　Werkzeugkiste` | 27pt 宽 438.0px，超 15.5 | `content7.py:48` 27→**25**（405.6 ✓；26pt 仅余 0.7px，不取） |
| 6 | head_check | P7 `THE ERROR CLINIC　Fehlerklinik` | 25pt 宽 436.1px，超 13.6 | `content7.py:99` 25→**24**（418.7 ✓） |
| 7 | occlusion | P1 暗带标题与副标 `EUROPA STELLT UM` 重叠 | **145.2×20.8px**（全家最大——德语副标 27pt 宽 295.7px，左缘 x=1559.3；46pt 标题右缘 1681.3，44pt 仍重叠 54px，故不能只降两档） | `content12.py:25` 暗带标题 46→**42**（右缘 1545.4， advance 空隙 13.9px）+ `content12.py:27` 副标 27→**25**（左缘移至 1581.2，advance 空隙 35.8px，墨水空隙约 15px） |
| 8 | creambox / boxtitle | P4 `THE WEEK'S FIXTURES　Spielplan` | +13.7px | `content34.py:130` 加 `tsize=22`（23pt 436.0，22pt 417.0 ✓） |
| 9 | creambox / boxtitle | P5 `WORDS OF THE SCREEN　Wortliste` | +22.9px | `content56.py:76` 加 `tsize=21`（23pt 427.7，22pt 409.1 仍超约 4px，21pt 390.5 ✓） |
| 10 | spill | P2 `Check your number !` 跌出 DID YOU KNOW 框底 | +12.71px | `content12.py:193` 框高公式尾数 +14→**+34**（框底 +20px；与 core-en 同款既有缺陷，基线同值） |

P8 变化：225→**216** 行，距页脚线余量 34.9→**46.7 px**（正，无溢出）。

## 四、门禁（run2，全套 17 门 ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 149，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0（3 弯引号全在 Newsreader） |
| 4 render | RC=0，印 PDF 7,500,351 B |
| 5 webpdf | RC=0，网 PDF 1,069,759 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 149/149 |
| 8 p8 compare | **EXTRA_ONLY**（core 62 noted vs 本版 149 noted，extra_count=87，裁定接受；keydiff=[136, 139, 149]——与 KIT 记载的读者语答案键 #136/#139/#149 一致） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 383，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（170 OBSERVE） |
| 12 boxtitle | 0 DEFECT（55 titles，284 body lines；本次以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 225→216，slack 34.9→46.7） |
| 15 文字层 print=web | 字符多重集差 **0** |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | en 家无 gates.py（`audit_en_fr.py`/`audit_en_es.py` 是旧版几何审计前身，不算 gate） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL1-en-de.pdf`，**7,500,351 字节**，
  SHA-256 `fa012bcb406c23c749ab34f65b17381686405346fdb1f015a94c69ed8d77f37c`
  （D5 前 KIT §一值 8,623,563 字节）。
- 网 PDF：`2026-w43-en-de.web.pdf`，**1,069,759 字节**，
  SHA-256 `b0c18a07aba2cd5df11a586607121369baac1820508f713f3e1bd3840d182fe3`
  （D5 前 issues 已发版 1,114,484 字节，`e086bc0c…`）。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**
  （SHA-256 `eb6a1179cdf3621a06746c2b74b56cb04a0e5a997200775b09221a12487380db`）。
- 练习总量仍为 **149 题**，与 core 逐题一致（KIT §三/§四未变）。

## 六、KIT

- `production/2026-w43/2026-w43-en-de/WEEKLY-KIT.md`：§一追加 D5 交付物行（新 SHA +
  字节数，注明 D5 前值）；文末追加 **§十一、D5 重建记录（2026-11-13）**（装机、基线、
  缺陷与修法、门禁 ALL-GREEN、新交付物）。
