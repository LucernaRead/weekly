# D5 重建报告 — 2026-w43-en-ru（俄语读者版）

W43 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader；俄语版西里尔字母由 Noto Sans CJK 改走 Noto Sans（regular 面））。
施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-ru/`
（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表，
`logs/2026-w43-en-ru-run1/` 为 run1 日志快照）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w43`
  → `production/2026-w43/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-en-ru/svglib.py --target en
  --reader ru --week 2026-w43`（先 `--check` dry-run，10 项改动 + mode ru 正确）。
  装后 `_D5_READER = "ru"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（66 PASS）；fix2 块保留。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由
  `scratch-prep-p3b/en_textmd_w43.py` 导出（P3b T5 已验与 issues 已发版字节一致）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 149**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `MANIFEST-W43-D1.md` 逐字节一致（7 行精确一致之一）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF
  **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，
  零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **422**、西里尔 **323**（全家唯一西里尔 >0 的版）、
  弯引号在 CJK **1**（>0，符合装机前提）。
- 基线 P8 口径：noted **62/149**（与 core 同口径；de/fr 两版为 149/149）。
- 基线另有一处已知测量误报：P8 ×3 "互撞"（`p8.py` 逐字/逐行比对的已知误报，
  D5-METHOD §4.5），**不修**。

## 三、缺陷与修法（run1 → run2）

run1 仅 2 门红（全家最少：head 0 缺陷、boxtitle 0 DEFECT、creambox PASS），
其余 15 门全绿。修法只动字号，**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | occlusion | P2 AND YOU 框末行 `приходит в семью?` 压在 TELLING THE TIME 横线 y=1558 上（`content12.py:213 p.hline(MX, RIGHT, dy-12)`，dy=1570 固定） | LINEX：末行基线 y=1559，框底已达 1563.6。根因：俄语 AND YOU 框比他版高——俄语回译行 20pt 下绕 3 行；框高公式 `content12.py:202`：62 + 英文 7 行×30.5 + 12 + 俄文 3 行×29 + 20 = 394.5 | **两处同修**：① `content12.py:193` DID YOU KNOW 框高公式尾数 +14→**+34**（全家通用修法，框底 +20px）；② `content12.py:202` 与 `:208` 俄语回译行 20→**19pt**（19pt 下绕 2 行，框高 −29px）。净效果：框底 1563.6+20−29 = **1554.6**（与修后 core-en 同值），末行基线约 1550，距横线 8px。备选（未采用）：etvous 英文段 21.5→19.5pt（7→6 行，省 30.5px），视觉改动更大。注意：只加 +34 不动 AND YOU 框会把框底推到 1583.6，撞上 TELLING THE TIME 右栏标题墨顶（约 1580.4） |
| 2 | spill | P2 `Check your number !` 跌出 DID YOU KNOW 框底 | +12.71px | 即上表第 1 项之 ①（全家通用修法；与 core-en 同款既有缺陷，基线同值） |

P8 变化：196→**197** 行，距页脚线余量 32.7→**32.7 px**（正，无溢出）。

## 四、门禁（run2，全套 17 门 ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 149，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0（noto_sans_elements=862，西里尔正常面） |
| 4 render | RC=0，印 PDF 7,808,348 B |
| 5 webpdf | RC=0，网 PDF 1,331,580 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 62/149（与 core 同口径） |
| 8 p8 compare | **CLEAN**（missing=[]，extra_count=0；keydiff=[136, 139, 149]——与 KIT 记载的读者语答案键一致） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（186 OBSERVE） |
| 12 boxtitle | 0 DEFECT（57 titles，439 body lines；本次以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 196→197，slack 32.7→32.7） |
| 15 文字层 print=web | 字符多重集差 **0** |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | en 家无 gates.py（`audit_en_fr.py`/`audit_en_es.py` 是旧版几何审计前身，不算 gate） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL1-en-ru.pdf`，**7,808,348 字节**，
  SHA-256 `5df67b262bd16578404db288f18421f96da5dc50f36241b7e78c28a8403699c8`
  （D5 前 KIT §9 记值 8,574,128 字节）。
- 网 PDF：`2026-w43-en-ru.web.pdf`，**1,331,580 字节**，
  SHA-256 `7edf2365247e1af5244e502f88bb70095761ca6e30322fedfdba1810589ad2a3`
  （D5 前 issues 已发版 1,170,319 字节，`7885361d…`）。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**
  （SHA-256 `de0fbf3d9285cf697934a5374f8a81d7a4515ca9bfc6078525f7d025c55f981d`）。
- 练习总量仍为 **149 题**。

## 六、KIT

- `production/2026-w43/2026-w43-en-ru/WEEKLY-KIT.md`：§9 Deliverables 追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **§12. D5 rebuild（2026-11-13）**
  （装机、基线、缺陷与修法、门禁 ALL-GREEN、新交付物）。
