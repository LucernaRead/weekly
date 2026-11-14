# D5 重建报告 — 2026-w45-en-pt（葡萄牙语读者版）

W45 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-en/logs/2026-w45-en-pt/`（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表）。门禁总表复本（D29）：`production/notes/2026-w45/g-en/scratch-d5-rebuild-en/logs/2026-w45-en-pt/GATES-SUMMARY.txt`。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w45` → `production/2026-w45/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-en-pt/svglib.py --target en --reader pt --week 2026-w45`（先 `--check` dry-run，mode latin 正确）。装后 `_D5_READER = "latin"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（9 处）。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `scratch-prep-p3b/en_textmd_w45.py` 导出（第 0 步已核实：hardcode 仅 W45 刊头 1 行；scratch 试跑 vs issues 已发版 BYTE-IDENTICAL）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `style-port-en/MANIFEST-W45-D1.md` 逐字节一致（16773031 字节，sha256 `b130e143…`）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF **非空字符差 0**，仅空格数浮动（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，零词字符丢失）。
- 修前普查 `d5_census.py`：D5 违规 **521**（>0，符合装机前提）。
- 基线 P8 口径：noted **78/150**（CLEAN；R1 落盘后重跑，D32；落盘前为 SHORT missing=[150] 抽取器盲区，见 §四）。

## 三、缺陷与修法（run1 → run2）

run1 共 5 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Noto Sans CJK 下比 Newsreader 宽），另有 P2 框溢出 1 项为既有缺陷（基线同值）。修法只动字号与框高，**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | `content56.py:109` “READ THE CHART　Leia o gráfico” | 25pt 宽 432.6px，超栏 10.1 | 25→**24**（415.3） |
| 2 | occlusion | P1 暗带标题与副标 “Terça de eleições” | 重叠 67.5px | 暗带标题 46→**42**（44pt 单独仅余 +0.3px；副标保持 27pt，修复后 gap +68.4px） |
| 3 | spill | P2 DID YOU KNOW 框 “bags.” | 框底 BELOW +12.74px（既有缺陷，基线同值） | `content12.py:193` 框高公式尾数 +14→**+34** |
| 4 | boxtitle / creambox | “THE WEEK IN NUMBERS　Números” | 右溢 +23.5px | tsize 23→**21** |
| 5 | boxtitle / creambox | “SUNDAY, NOVEMBER 8　Domingo” | 右溢 +2.9px | tsize 23→**21** |

P8 变化：199 → 200 行，距页脚线余量 32.7 → 32.7 px（正，无溢出）。

## 四、门禁（run2，全套 16 门 + D18）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、花括号 CJK 0 |
| 4 render | RC=0，印 PDF 16275116 B |
| 5 webpdf | RC=0，网 PDF 1961710 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 78/150（R1 落盘后重跑，D32） |
| 8 p8 compare | **PASS（R1 landed, D32；extract core 78 / ed 78，compare CLEAN，exit 0，keydiff=[137, 138, 139, 140, 150]）** |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 337，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（91 OBSERVE） |
| 12 boxtitle | 0 DEFECT（34 titles, 165 body lines；以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 199 → 200，slack 32.7 → 32.7） |
| 15a 文字层 print=web | 字符多重集差 **0**；text.md BYTE-IDENTICAL |
| 16 census_quotes | 0 defective |
| D18 刊头 | gap **133.2px** PASS |
| 17 家族 gates.py | en 家无 gates.py |

**OVERALL: 16/16 ALL-GREEN + D18 PASS（g8 经 R1 落盘后重跑 PASS，D32）。**

g8 p8 compare PASS（R1 landed, D32；extract core 78 / ed 78，compare CLEAN，exit 0，keydiff=[137, 138, 139, 140, 150]；patched 与基线重跑均为 CLEAN）。落盘前为 FAIL RC=1，SHORT missing=[150]：150 号注释在 SVG 与文字层中全文印出（“150. Questão aberta: veja os pontos no quadro de redação; o modelo está no quadro desta página (Pontua-se por pontos)”），为冒号式，`tools/p8.py` `detect_note()` 落盘前只认括号式 `key (note)` 与破折号式 `key — note`；R1 冒号式规则（D32）落盘后 [150] 以 `method='colon'` 检出。已发基线重跑同样 CLEAN，印 PDF 与清单字节精确一致。未改内容迁就抽取器；D31 adjudication 已转为真 PASS。

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`；网 PDF 跨次字节不确定，closer 须拷 builder 原件，绝不重跑 webpdf）

- 印 PDF：`The-Lucerna-VOL2-en-pt.pdf`，**16275116 字节**，
  SHA-256 `09fdfabcf8d1c83a35306f7dd426d16647eba2fe251344a6472d0379292a1414`
  （D5 前基线 16773031 字节）。
- 网 PDF：`2026-w45-en-pt.web.pdf`，**1961710 字节**，
  SHA-256 `c2eeeb10b858e8ae1ce62a397f0e0b077ae22f4c696fbb73abff1ad0b17ca9a8`。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**（43565 字节，SHA-256 `22b7494163cb612342fde1f39501938b8e29a6d820918192866715e5ee63af40`）。
- 练习总量仍为 **150 题**，与 core 逐题一致。

## 六、KIT

- `production/2026-w45/2026-w45-en-pt/WEEKLY-KIT.md`：§7 “Final files” pin 更新；文末追加 §11。