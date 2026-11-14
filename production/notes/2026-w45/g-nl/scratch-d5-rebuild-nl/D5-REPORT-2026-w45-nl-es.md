# D5 重建报告 — 2026-w45-nl-es（西班牙语读者版）

W45 nl 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK）。施工 2026-11-14（v1 11:27–13:23 UTC 被 restart drain 中断于 ru 网 PDF 步；v2 接替补建 ru + zh-tw，全量重跑门禁）；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-nl/logs/2026-w45-nl-es/`（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表）。门禁总表复本（D29）：`production/notes/2026-w45/g-nl/scratch-d5-rebuild-nl/logs/2026-w45-nl-es/GATES-SUMMARY.txt`。

## 一、装机

- Core 落盘（全家共用一次，v1 执行）：`apply_variant.py --patch-core nl --week 2026-w45` → `production/2026-w45/core-nl/svglib.py` +95/−3 行，`_D5_READER = "latin"`（D24：按 patched 原样同步，不特殊处理）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-nl-es/svglib.py --target nl --reader es --week 2026-w45`（先 `--check` dry-run，mode=latin 正确）。装后 `_D5_READER = "latin"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（svglib.py 含 fix2 标记 13 处，安装器日志 "added fix2 block"）。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `scratch-2026-w45-nl/export_text_w45nl.py` 导出（第 0 步已核实：AST 导出器，无 hardcode，标题由参数传入；scratch 试跑 vs issues 已发版 BYTE-IDENTICAL）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 7,526,083 字节；印/网文字层 vs issues 已发 web PDF 字符多重集差 **0**（自验 11/11 全绿）。
- 修前普查 `d5_census.py`：D5 违规 **拉丁 494**（>0，符合装机前提）。
- KIT §11 旧 pin 与基线实测不符（de 例：KIT 印 7,918,211 B，基线实测 7,526,971 B）——KIT SHA 滞后（PLAN 修正案：基线永不以 KIT SHA 为准），本次以实测发运值订正。
- 基线 P8 口径：noted **150/150**。

## 三、缺陷与修法（run1 → run2）

run1 缺陷：3 处 HEAD TOO WIDE（P2 DRIE ACTIES VOOR DEZE WEEK、P3 TWEEDEHANDS IS OOK CULTUUR、P7 B1　SCHEIDBARE WERKWOORDEN）；occlusion 1 处 TEXTX（P7 'SCHEIDBARE WERKWOORDEN' 与 'B2' 重叠 5.2×17.8px）；boxtitle/creambox 5 处；ru 另有 spill 1 处。全部为 D5 字体加宽引起（拉丁粗体在 Noto Sans CJK 下比 Newsreader 宽）。修法只动字号，**未动任何文字内容**（共 8 处）。

| 位置 | 内容 | 实测 | 修法 |
|---|---|---|---|
| content12.py:49 | 奶油框标题 DE WEEK IN CIJFERS　EN CIFRAS | 宽 415.0px，超框 10.2px；修后 396.9px，余量 5.9px | tsize — → **tsize=22** |
| content12.py:180 | 奶油框标题 ZO ONTHOUD JE HET　EL TRUCO | 宽 412.8px，超框 8.0px；修后 394.8px，余量 8.0px | tsize — → **tsize=22** |
| content56.py:162 | p.text VOOR OF TEGEN?　PROS Y CONTRAS | 宽 415.7px，超 15.1px；修后 395.9px，余量 2.7px | 21 → **20** |
| content7.py:73 | p.text PAS OP!　ERRORES FRECUENTES | 宽 410.7px，超 10.1px；修后 392.8px，余量 5.8px | 23 → **22** |
| content7.py:84 | p.text HET WOORD　PALABRA SEMANAL | 宽 432.1px，超 32.1px；修后 394.5px，余量 3.5px | 23 → **21** |
| content12.py:176 | 栏头 DRIE ACTIES VOOR DEZE WEEK | 宽 425.0px；修后 408.0px | 25 → **24** |
| content34.py:21 | 栏头 TWEEDEHANDS IS OOK CULTUUR | 宽 456.7px；修后 420.1px | 25 → **23** |
| content7.py:32 | 栏头 B1　SCHEIDBARE WERKWOORDEN | 宽 455.7px；修后 417.8px | 24 → **22** |

P8 变化：232 → 232 行（content8.py 未动），距页脚线余量 36.9px（正，无溢出）。

## 四、门禁（run2，全套 16 门 + D18）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、花括号 CJK 0 |
| 4 render | RC=0，印 PDF 6,941,183 B |
| 5 webpdf | RC=0，网 PDF 1,019,584 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**（missing=[] extra=0，keydiff=[137, 138]——137/138 为读者语重定向真重 aim，已裁定，非缺陷） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 466，D5 run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（1 OBSERVE） |
| 12 boxtitle | 0 DEFECT |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 232 → 232，slack 36.9px） |
| 15a 文字层 print=web | 字符多重集差 **0**（34,543 字符）；text.md BYTE-IDENTICAL |
| 15b carryover（补充，诊断性） | 共享 `verify_textmd.py` 对 nl 家未标定，patched 与基线同态 FAIL——D27 类已知工具口径差，非 D5 回归，不计入 verdict（见 §四末） |
| 16 census_quotes | 0 defective |
| D18 刊头 | gap **89.7px** PASS |
| 17 家族 gates.py | nl 家无 gates.py |

**OVERALL: ALL-GREEN.**

补充（G15b）：`verify_textmd.py --reader es` 在 patched 与基线（修前生产版）上同态 FAIL（de 例：SVG-only 711 / MD-only 1119，基线 711 / 1121；ru、zh-cn 基线与 patched 残差完全相同；pt 无读者表 rc=2）。根因为共享校验器的表按 pt 目标语格式标定，nl 家格式不在其标定范围内；内容不变的证据以门 15（AST 导出器 BYTE-IDENTICAL + print=web 差 0 + 基线印 PDF vs 已发 web PDF 差 0）为准。

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`；网 PDF 跨次字节不确定，closer 须拷 builder 原件，绝不重跑 webpdf）

- 印 PDF：`De-Lucerna-VOL2-nl-es.pdf`，**6,941,183 字节**，
  SHA-256 `9976e67b8a809e58d1f1f4e799657dd0421881af849e2d46c9a424b79fc37d28`
  （D5 前基线 7,526,083 字节）。
- 网 PDF：`2026-w45-nl-es.web.pdf`，**1,019,584 字节**，
  SHA-256 `708b9f5fbd2e6b203aedfc23a649fd5a144c38fb66d55831cd48d27bd972112d`。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**（39,823 字节，SHA-256 `229b307b1b559f92f88f328058b2b48c0babab53f4522235d26474ae8edd2ad0`）。
- 练习总量仍为 **150 题**，与 core 逐题一致。

## 六、KIT

- `patched/2026-w45-nl-es/WEEKLY-KIT.md`（closer 同步入 production）：§11 pin 更新为本次实测发运值（印/网/SVG 全量 SHA）；文末追加 D5 rebuild 节。
