# D5 重建报告 — 2026-w43-en-es（西班牙语读者版）

W43 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-es/`
（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表，
`logs/2026-w43-en-es-run1/` 为 run1 日志快照）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w43`
  → `production/2026-w43/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-en-es/svglib.py --target en
  --reader es --week 2026-w43`（先 `--check` dry-run，10 项改动 + mode latin 正确）。
  装后 `_D5_READER = "latin"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（66 PASS）；fix2 块保留。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由
  `scratch-prep-p3b/en_textmd_w43.py` 导出（P3b T5 已验与 issues 已发版字节一致）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 149**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `MANIFEST-W43-D1.md` 逐字节一致（7 行精确一致之一）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF
  **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，
  零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **553**、西里尔 0、弯引号在 CJK **1**（>0，符合装机前提）。
- 基线 P8 口径：noted **62/149**（与 core 同口径；de/fr 两版为 149/149）。

## 三、缺陷与修法（run1 → run2）

run1 共 12 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比
Noto Sans CJK 宽约 5.7%），另有 1 项既有缺陷（P2 spill，基线同值）。修法只动字号，
**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P1 `TRY IT NOW　Practica al momento` | 25pt 宽 439.1px，超栏 16.6（栏宽 422.5） | `content12.py:47` 25→**24**（421.5 ✓，仅余 1.0px——门禁为确定性量测，通过即通过） |
| 2 | head_check | P3 `B　FESTIVAL WORDS　Completa` | 25pt 宽 427.7px，超 5.2 | `content34.py:43` 25→**24**（410.6 ✓） |
| 3 | head_check | P5 `EARNINGS, IN PLAIN ENGLISH` | 26pt 宽 425.1px，超 2.6 | `content56.py:23` 26→**25**（408.8 ✓） |
| 4 | head_check | P7 `THE TOOLBOX　Herramientas` | 27pt 宽 423.9px，超 1.4 | `content7.py:48` 27→**26**（408.2 ✓） |
| 5 | occlusion | P1 暗带标题与副标 `CAMBIA LA HORA` 重叠 | 111.9×20.8px（副标 27pt 左缘 x=1592.6；44pt 标题右缘 1613.6 仍重叠） | `content12.py:25` 暗带标题 46→**42**（右缘 1545.4，advance 空隙 47.2px） |
| 6 | occlusion | P6 PRACTICE DATA 行被 r6 首栏标题下划线穿过 | LINEX：行尾 x=993.2，越过 x=989 起的规则线（y=1507）4.2px | `content56.py:170` PRACTICE DATA 行 18.5→**18**（行尾 x=969.0，距规则线 20px）。**注意：D1 建报时已修过同一问题（KIT Geometry 第 8 项：缩短西语尾句后行尾 x=958）——D5 字体加宽把它重新引出**（CJK 字体下拉丁串更窄，Newsreader 下变宽 35px） |
| 7 | creambox / boxtitle | P1 `THE WEEK IN NUMBERS　En cifras` | +21.5px | `content12.py:43` 加 `tsize=21`（23pt 426.2，22pt 407.7 仍超约 3px，21pt 389.2 ✓） |
| 8 | creambox / boxtitle | P4 `THE WEEK'S FIXTURES　Partidos` | +3.7px | `content34.py:130` 加 `tsize=22`（406.9 ✓） |
| 9 | creambox / boxtitle | P5 `WORDS OF THE SCREEN　Palabras` | +13.9px | `content56.py:76` 加 `tsize=22`（399.8 ✓） |
| 10 | creambox / boxtitle | P6 `HEADLINE LANGUAGE　Titulares` | +3.2px | `content56.py:158` 加 `tsize=22`（390.4 ✓） |
| 11 | spill | P2 `Check your number !` 跌出 DID YOU KNOW 框底 | +12.71px | `content12.py:193` 框高公式尾数 +14→**+34**（框底 +20px；与 core-en 同款既有缺陷，基线同值） |

**修法插曲（已解决，记入教训）**：#6 第一稿曾把 PRACTICE DATA 行改为 16pt，
重建后 text.md 出现 DIFF（新导出缺该行）。原因：导出器 `en_textmd_w43.py`
只收录字号 ≥18 的 `p.text` 行（L240–242），16pt 被过滤。已改为 18pt
（≥18 阈值，仍收录），text.md 恢复 BYTE-IDENTICAL。**教训：改字号前先确认
导出器阈值；凡 <18pt 的改法都会丢 text.md 行。**

P8 变化：195→**192** 行，距页脚线余量 32.7→**32.6 px**（正，无溢出）。

## 四、门禁（run2，全套 17 门 ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 149，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0（2 弯引号全在 Newsreader） |
| 4 render | RC=0，印 PDF 7,499,239 B |
| 5 webpdf | RC=0，网 PDF 1,068,674 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 62/149（与 core 同口径） |
| 8 p8 compare | **CLEAN**（missing=[]，extra_count=0；keydiff=[136, 139, 149]——与 KIT 记载的读者语答案键一致） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 354，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（164 OBSERVE） |
| 12 boxtitle | 0 DEFECT（55 titles，282 body lines；本次以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 195→192，slack 32.7→32.6） |
| 15 文字层 print=web | 字符多重集差 **0** |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | en 家无 gates.py（`audit_en_fr.py`/`audit_en_es.py` 是旧版几何审计前身，不算 gate） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL1-en-es.pdf`，**7,499,239 字节**，
  SHA-256 `1a9e0b68a28526cf116403c79238c4de4fd105247c05d056ac2bf35a46edfd50`
  （D5 前 KIT 记值 8,618,507 字节）。
- 网 PDF：`2026-w43-en-es.web.pdf`，**1,068,674 字节**，
  SHA-256 `d852804361ed382b4d053555cc26228c21e298964c64656681b76cb449c225a4`
  （D5 前 issues 已发版 1,108,851 字节，`164eb07c…`）。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**
  （SHA-256 `ba99650a7595d1b3b6977b414482e5b18f9c4ea688e62205084ebae8c92ebd1a`）。
- 练习总量仍为 **149 题**，答案键仅 #136/#139/#149 与 core 不同（KIT 已登记）。

## 六、KIT

- `production/2026-w43/2026-w43-en-es/WEEKLY-KIT.md`：Deliverables 节追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **D5 rebuild（2026-11-13）** 节
  （装机、基线、缺陷与修法、门禁 ALL-GREEN、新交付物）。
