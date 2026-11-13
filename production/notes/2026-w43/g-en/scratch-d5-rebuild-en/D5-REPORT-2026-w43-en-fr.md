# D5 重建报告 — 2026-w43-en-fr（法语读者版）

W43 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-fr/`
（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表，
`logs/2026-w43-en-fr-run1/` 为 run1 日志快照）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w43`
  → `production/2026-w43/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-en-fr/svglib.py --target en
  --reader fr --week 2026-w43`（先 `--check` dry-run，10 项改动 + mode latin 正确）。
  装后 `_D5_READER = "latin"`；装后 svglib md5 与生产 core-en 装后相同
  （`3b0d9729c69e`；core-en svglib docstring 含 "— for 重阳" 一行，fanout 版无此行，
  属既有差异）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（66 PASS）；fix2 块保留。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由
  `scratch-prep-p3b/en_textmd_w43.py` 导出（P3b T5 已验与 issues 已发版字节一致；
  本版导出器试跑即以 `2026-w43-en-fr` 为样本，47,780 B，与已发版 BYTE-IDENTICAL）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 149**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `MANIFEST-W43-D1.md` 逐字节一致（7 行精确一致之一）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF
  **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，
  零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **598**、西里尔 0、弯引号在 CJK **59**（>0，符合装机前提；
  法语 « » 弯引号多，全家最高）。
- 基线 P8 口径：noted **149/149**（fanout 全量口径；core 为 62/149）。

## 三、缺陷与修法（run1 → run2）

run1 共 12 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比
Noto Sans CJK 宽约 5.7%），另有 1 项既有缺陷（P2 spill，基线同值）。修法只动字号，
**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P3 `A　TRUE OR FALSE ?　Vrai / faux` | 25pt 宽 429.6px，超栏 7.1（栏宽 422.5） | `content34.py:31` 25→**24**（412.4 ✓） |
| 2 | head_check | P4 `C　COMPARATIVES　Comparatifs` | 25pt 宽 442.8px，超 20.3 | `content34.py:158` 25→**23**（407.3 ✓；24pt 425.0 仍超 2.5） |
| 3 | head_check | P5 `EARNINGS, IN PLAIN ENGLISH` | 26pt 宽 425.1px，超 2.6 | `content56.py:23` 26→**25**（408.8 ✓） |
| 4 | head_check | P5 `D　TRUE OR FALSE ?　Vrai / faux` | 25pt 宽 429.9px，超 7.4 | `content56.py:64` 25→**24**（412.7 ✓） |
| 5 | head_check | P6 `READING THE CHART　Graphique` | 24pt 宽 433.1px，超 10.6 | `content56.py:188` 24→**23**（415.0 ✓） |
| 6 | head_check | P8 `D　SENTENCES　Phrases à former` | 24pt 宽 423.7px，超 1.2 | `content8.py:70` 24→**23**（406.0 ✓） |
| 7 | occlusion | P1 暗带标题与副标 `L'EUROPE RECULE` 重叠 | 121.2×20.8px（副标 27pt 左缘 x=1583.3；44pt 标题右缘 1613.6 仍重叠） | `content12.py:25` 暗带标题 46→**42**（右缘 1545.4，advance 空隙 37.9px） |
| 8 | creambox / boxtitle | P1 `THE WEEK IN NUMBERS　Chiffres` | +12.5px | `content12.py:43` 加 `tsize=22`（398.6 ✓） |
| 9 | creambox / boxtitle | P2 `DO THE MATHS　À vous de calculer` | +14.7px | `content12.py:174` 加 `tsize=22`（400.6 ✓） |
| 10 | creambox / boxtitle | P3 `FESTIVAL WORDS　Mots de la fête` | +5.1px | `content34.py:80` 加 `tsize=22`（391.8 ✓） |
| 11 | creambox / boxtitle | P6 `HEADLINE LANGUAGE　Les titres` | +6.2px | `content56.py:158` 加 `tsize=22`（392.7 ✓） |
| 12 | spill | P2 `Check your number !` 跌出 DID YOU KNOW 框底 | +12.71px | `content12.py:193` 框高公式尾数 +14→**+34**（框底 +20px；与 core-en 同款既有缺陷，基线同值） |

P8 变化：221→**221** 行，距页脚线余量 34.9→**34.9 px**（正，无溢出）。

## 四、门禁（run2，全套 17 门 ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 149，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0 |
| 4 render | RC=0，印 PDF 7,502,963 B |
| 5 webpdf | RC=0，网 PDF 1,072,352 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 149/149 |
| 8 p8 compare | **EXTRA_ONLY**（core 62 noted vs 本版 149 noted，extra_count=87，裁定接受；keydiff=[136, 139, 149]——与 KIT 记载的读者语答案键一致） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（170 OBSERVE） |
| 12 boxtitle | 0 DEFECT（57 titles，287 body lines；本次以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 221→221，slack 34.9→34.9） |
| 15 文字层 print=web | 字符多重集差 **0** |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | en 家无 gates.py（`audit_en_fr.py`/`audit_en_es.py` 是旧版几何审计前身，不算 gate） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL1-en-fr.pdf`，**7,502,963 字节**，
  SHA-256 `44b551420d6b91b17f5e19b16986e3f1a1ed65758b9c8f71f39c0d7e987351b7`
  （D5 前 KIT 记值 8,623,199 字节——该值为 D1 前旧值，已过期，以此为准）。
- 网 PDF：`2026-w43-en-fr.web.pdf`，**1,072,352 字节**，
  SHA-256 `cb02ed902f319f610fdf1e206cc48a5501940ce55cb51f9985c3534e24a70275`
  （D5 前 issues 已发版 1,113,337 字节，`b2dfb4f5…`）。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**
  （SHA-256 `2b25e2aab4f09d5b29fa3694eac375a9def8214ae1296ecb34c263ce03a482bf`）。
- 练习总量仍为 **149 题**，答案键仅 #136/#139/#149 与 core 不同（KIT 已登记）。

## 六、KIT

- `production/2026-w43/2026-w43-en-fr/WEEKLY-KIT.md`：Deliverables 节追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **D5 rebuild（2026-11-13）** 节
  （装机、基线、缺陷与修法、门禁 ALL-GREEN、新交付物）。
