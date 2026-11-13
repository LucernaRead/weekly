# D5 重建报告 — 2026-w43-en-nl（荷兰语读者版）

W43 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-nl/`
（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表，
`logs/2026-w43-en-nl-run1/` 为 run1 日志快照）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w43`
  → `production/2026-w43/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-en-nl/svglib.py --target en
  --reader nl --week 2026-w43`（先 `--check` dry-run，10 项改动 + mode latin 正确）。
  装后 `_D5_READER = "latin"`；装后 svglib md5 与 de/it/pt 全同（`6c3596c1e919`）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（66 PASS）；fix2 块保留。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由
  `scratch-prep-p3b/en_textmd_w43.py` 导出（P3b T5 已验与 issues 已发版字节一致）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 149**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `MANIFEST-W43-D1.md` 逐字节一致（7 行精确一致之一）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF
  **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，
  零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **556**、西里尔 0、弯引号在 CJK **1**（>0，符合装机前提）。
- 基线 P8 口径：noted **62/149**（与 core 同口径；de/fr 两版为 149/149）。

## 三、缺陷与修法（run1 → run2）

run1 共 8 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比
Noto Sans CJK 宽约 5.7%），另有 1 项既有缺陷（P2 spill，基线同值）。修法只动字号，
**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P4 `C　COMPARATIVES　Vergelijking` | 25pt 宽 438.2px，超栏 15.7（栏宽 422.5） | `content34.py:158` 25→**24**（420.6 ✓，仅余 1.9px——门禁为确定性量测，通过即通过） |
| 2 | head_check | P5 `EARNINGS, IN PLAIN ENGLISH` | 26pt 宽 425.1px，超 2.6 | `content56.py:23` 26→**25**（408.8 ✓） |
| 3 | head_check | P8 `B　MULTIPLE CHOICE　Meerkeuze` | 24pt 宽 441.1px，超 18.6 | `content8.py:43` 24→**22**（404.4 ✓；23pt 422.7 仍超 0.2px） |
| 4 | occlusion | P1 暗带标题与副标 `DE KLOK TERUG` 重叠 | 89.9×20.8px（副标 27pt 左缘 x=1614.6；44pt 标题右缘 1613.6 仅余约 1px advance，不够） | `content12.py:25` 暗带标题 46→**42**（右缘 1545.4，advance 空隙 69.2px） |
| 5 | occlusion | P6 PRACTICE DATA 行被 r6 首栏标题下划线穿过 | LINEX：行尾越过 x=989 起的规则线（y=1507） | `content56.py:170` PRACTICE DATA 行 18.5→**18**（与 es 同款：荷兰语尾句 `Oefengegevens, verzonnen.` 使行尾越线；18pt 后行尾收至规则线左，≥18 导出器阈值不受影响，text.md 仍字节一致） |
| 6 | creambox / boxtitle | P3 `SAY IT ON THE NIGHT　Zeg het zo` | +2.6px | `content34.py:25` 加 `tsize=22`（389.2 ✓） |
| 7 | creambox / boxtitle | P5 `WORDS OF THE SCREEN　Scherm` | +2.9px | `content56.py:76` 加 `tsize=22`（389.5 ✓） |
| 8 | creambox / boxtitle | P6 `HOW TO FOLLOW IT　Zo volg je ze` | +2.3px | `content56.py:138` 加 `tsize=22`（389.4 ✓） |
| 9 | spill | P2 `Check your number !` 跌出 DID YOU KNOW 框底 | +12.71px | `content12.py:193` 框高公式尾数 +14→**+34**（框底 +20px；与 core-en 同款既有缺陷，基线同值） |

P8 变化：197→**193** 行，距页脚线余量 32.7→**51.6 px**（正，无溢出）。

## 四、门禁（run2，全套 17 门 ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 149，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0 |
| 4 render | RC=0，印 PDF 7,494,138 B |
| 5 webpdf | RC=0，网 PDF 1,063,554 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 62/149（与 core 同口径） |
| 8 p8 compare | **CLEAN**（missing=[]，extra_count=0；keydiff=[136, 139, 149]——与 KIT 记载的读者语答案键一致） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（167 OBSERVE） |
| 12 boxtitle | 0 DEFECT（57 titles，282 body lines；本次以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 197→193，slack 32.7→51.6） |
| 15 文字层 print=web | 字符多重集差 **0** |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | en 家无 gates.py（`audit_en_fr.py`/`audit_en_es.py` 是旧版几何审计前身，不算 gate） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL1-en-nl.pdf`，**7,494,138 字节**，
  SHA-256 `3875d10bc3aa7a5267c4e5599358254bd20475011441385a7dc78d8fec4b85ae`
  （D5 前 KIT §9 记值 8,617,312 字节）。
- 网 PDF：`2026-w43-en-nl.web.pdf`，**1,063,554 字节**，
  SHA-256 `5107ac33829e6f78cac8642da9e70a450dcf506ebbe2963a72f3cf35d4e87e5d`
  （D5 前 issues 已发版 1,105,489 字节，`4e244251…`）。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**
  （SHA-256 `72de521951fd70f1e69076ecd28cb38a245130f6a935fa54b3f8f59b439f7ce0`）。
- 练习总量仍为 **149 题**。

## 六、KIT

- `production/2026-w43/2026-w43-en-nl/WEEKLY-KIT.md`：§9 Deliverables 追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **§11. D5 rebuild（2026-11-13）**
  （装机、基线、缺陷与修法、门禁 ALL-GREEN、新交付物）。
