# D5 重建报告 — 2026-w43-en-pt（葡萄牙语读者版）

W43 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-pt/`
（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表，
`logs/2026-w43-en-pt-run1/` 为 run1 日志快照）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w43`
  → `production/2026-w43/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-en-pt/svglib.py --target en
  --reader pt --week 2026-w43`（先 `--check` dry-run，10 项改动 + mode latin 正确）。
  装后 `_D5_READER = "latin"`；装后 svglib md5 与 de/it/nl 全同（`6c3596c1e919`）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（66 PASS）；fix2 块保留。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由
  `scratch-prep-p3b/en_textmd_w43.py` 导出（P3b T5 已验与 issues 已发版字节一致）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 149**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `MANIFEST-W43-D1.md` 逐字节一致（7 行精确一致之一）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF
  **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，
  零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **549**、西里尔 0、弯引号在 CJK **1**（>0，符合装机前提）。
- 基线 P8 口径：noted **62/149**（与 core 同口径；de/fr 两版为 149/149）。

## 三、缺陷与修法（run1 → run2）

run1 共 7 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比
Noto Sans CJK 宽约 5.7%），另有 1 项既有缺陷（P2 spill，基线同值）。修法只动字号，
**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P4 `C　COMPARATIVES　Comparação` | 25pt 宽 442.6px，超栏 20.1（栏宽 422.5） | `content34.py:158` 25→**23**（407.1 ✓；24pt 424.9 仍超 2.4） |
| 2 | head_check | P5 `EARNINGS, IN PLAIN ENGLISH` | 26pt 宽 425.1px，超 2.6 | `content56.py:23` 26→**25**（408.8 ✓） |
| 3 | occlusion | P1 暗带标题与副标 `ATRASA O RELÓGIO` 重叠 | 138.0×25.5px（副标 27pt 左缘 x=1566.5；44pt 标题右缘 1613.6 仍重叠 47px；单降标题到 42 仅余 21.1px advance 空隙，墨水约 −2px，不够） | `content12.py:25` 暗带标题 46→**42**（右缘 1545.4）+ `content12.py:27` 副标 27→**25**（左缘移至 1587.9，advance 空隙 42.5px） |
| 4 | creambox / boxtitle | P1 `THE WEEK IN NUMBERS　Semana` | +10.5px | `content12.py:43` 加 `tsize=22`（396.8 ✓） |
| 5 | creambox / boxtitle | P6 `HOW TO FOLLOW IT　Como seguir` | +8.3px | `content56.py:138` 加 `tsize=22`（394.2 ✓） |
| 6 | creambox / boxtitle | P6 `HEADLINE LANGUAGE　Manchete` | +14.2px | `content56.py:158` 加 `tsize=22`（400.4 ✓） |
| 7 | spill | P2 `Check your number !` 跌出 DID YOU KNOW 框底 | +12.71px | `content12.py:193` 框高公式尾数 +14→**+34**（框底 +20px；与 core-en 同款既有缺陷，基线同值） |

P8 变化：191→**187** 行，距页脚线余量 32.7→**32.7 px**（正，无溢出）。

## 四、门禁（run2，全套 17 门 ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 149，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0 |
| 4 render | RC=0，印 PDF 7,501,769 B |
| 5 webpdf | RC=0，网 PDF 1,071,178 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 62/149（与 core 同口径） |
| 8 p8 compare | **CLEAN**（missing=[]，extra_count=0；keydiff=[136, 139, 149]——与 KIT 记载的读者语答案键一致） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（169 OBSERVE） |
| 12 boxtitle | 0 DEFECT（57 titles，281 body lines；本次以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 191→187，slack 32.7→32.7） |
| 15 文字层 print=web | 字符多重集差 **0** |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | en 家无 gates.py（`audit_en_fr.py`/`audit_en_es.py` 是旧版几何审计前身，不算 gate） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL1-en-pt.pdf`，**7,501,769 字节**，
  SHA-256 `2a4b70efddefe66aff04d84a836af6182d8d017cc0649fcef4f063c0f70b302d`
  （D5 前 KIT §11 记值 8,622,488 字节）。
- 网 PDF：`2026-w43-en-pt.web.pdf`，**1,071,178 字节**，
  SHA-256 `d4e426be7208255020a05a2c85e16cf82d1639f55707473d205d915ca4f74cce`
  （D5 前 issues 已发版 1,113,944 字节，`1ed9ae29…`）。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**
  （SHA-256 `1ab0f9c629e625f0d6ab7fcf7c26dfc90b1ce70792536a136da557e93a7c7cb6`）。
- 练习总量仍为 **149 题**。

## 六、KIT

- `production/2026-w43/2026-w43-en-pt/WEEKLY-KIT.md`：§11 Deliverables 追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **§13. D5 rebuild（2026-11-13）**
  （装机、基线、缺陷与修法、门禁 ALL-GREEN、新交付物）。
