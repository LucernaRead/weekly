# GATE-LOG — W47 zh-tw-es proof1 机械门独立重跑记录（重建版）

复校对象：`production/2026-w47/2026-w47-zh-tw-es/`（重 fan-out 重建版，印 PDF `e32c58c4…`）。
驱动：本 scratch 目录 `gates-proof.py`（另有 `keycheck.py`）；工具一律 `~/workspace/weekly-git/tools/venv/bin/python`（VENV，Python 3.12.3），绝未用系统 python3。
输出：`gates/`（`gates.json` + 各门日志 + `print.txt`/`web.txt` + `freeze-base/`）；`gates-old/` 为旧版备份的 PIL creambox 输出。
TMPDIR：本 scratch 下 `tmp/`。

## 0. 第一步：freeze baseline（0/8 即停手的门）

```
$VENV tools/freeze.py baseline --build . --core-svg svg --out <scratch>/gates/freeze-base   # cwd=本版
baseline: 8/8 SVGs byte-identical
core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
```

门禁驱动内再次重跑亦为 8/8；freeze-base SVG 与版内 SVG 逐字节一致（`freeze_diff_vs_edition_svg {}`）。继续全量复校。

## 1. checks.py（本版自带）

```
cd <edition> && $VENV checks.py
PHRASE 2 迪士尼聖誕，從11月17日開始
SIMP_ONLY_HITS []
CHART p4 [90.0, 450.0, 900.0] expect [90.0, 450.0, 900.0]
CHART p6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] expect [188.0, 695.21, 948.82, 1033.36, 1202.43]
CHECKS PASS        # rc=0
```

## 2. 几何遮挡审计 tools/occlusion_audit.py

```
$VENV tools/occlusion_audit.py --selftest
  → rc=0，6 类 planted 全部触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），干净对照静默
$VENV tools/occlusion_audit.py --json gates/occlusion.json <edition>/svg
  → 0 flags，rc=0
```

## 3. P8 tools/p8.py

```
$VENV tools/p8.py extract --p8 <edition>/svg/p8-test.svg --total 150 --json gates/p8-extract.json
  → noted set = 150 of 150
$VENV tools/p8.py compare --core-p8 production/2026-w47/core-zh-tw/svg/p8-test.svg \
    --edition-p8 <edition>/svg/p8-test.svg --total 150 --json gates/p8-compare.json
  → status: CLEAN   missing=[] extra=[] keydiff=[]
```

## 4. canonical creambox 全扫（hidden_files/w47/tools/creambox.py）

```
$VENV hidden_files/w47/tools/creambox.py <edition>/svg/p1-front.svg p2-life.svg p3-culture.svg \
    p4-sport.svg p5-youth.svg p6-deep.svg p7-lang.svg p8-test.svg
boxes: 36；negative inside clearances: []（0 负）
各页最小内距：p1 18.8 / p2 15.8 / p3 15.8 / p4 9.8 / p5 6.4 / p6 19.9 / p7 12.5
P7 工具箱三条：+40.5（"…hora: 12 veces, de 17:30 a 23:00."）/ +12.5（"…más Y. Crea tu propia frase con ella."）/ +14.0（"…abierta."）
rc=0
```

## 5. boxtitle 逐盒实测（gtools/boxtitle.py）

```
$VENV <scratch-refanout-zh-tw>/gtools/boxtitle.py <edition>/svg gates/
boxes measured: 36；title/line overruns past box right edge: 0；min title right margin overall: 9.8 px；rc=0
```

## 6. PIL creambox（gtools/creambox-pil.py）— 新版与旧版备份对照

```
$VENV <scratch-refanout-zh-tw>/gtools/creambox-pil.py <edition>/svg gates/
  → STRADDLE flags: 4；CREAM-COVER flags: 0；P7 最小余隙 8.0；rc=0
  STRADDLE p2-life.svg  耶誕城小檔　Ficha de Christmasland   ink [1461.5,1452.5,1899.0,1476.5] cream [1439.5,1430.0,1862.0,1890.0]
  STRADDLE p3-culture.svg 金馬小表　Ficha de los Golden Horse ink [1461.5,671.8,1902.0,696.1] cream [1439.5,649.6,1862.0,1119.6]
  STRADDLE p3-culture.svg 鋼雕閉幕行程　Último fin de semana    ink [1461.5,1424.3,1898.0,1452.1] cream [1439.5,1405.6,1862.0,1855.6]
  STRADDLE p5-youth.svg  爵士音樂節時間表　Fechas del jazz     ink [1461.5,1863.8,1869.2,1891.3] cream [1439.5,1841.6,1862.0,2271.6]

$VENV <scratch-refanout-zh-tw>/gtools/creambox-pil.py <scratch-refanout-zh-tw>/backup/2026-w47-zh-tw-es/svg gates-old/
  → STRADDLE flags: 5；CREAM-COVER flags: 0；rc=0
  （同上 4 条完全相同，另第 5 条：）
  STRADDLE p4-sport.svg  deporte?   ink [1461.5,1345.9,1545.0,1366.7] cream [1439.5,1128.0,1862.0,1358.0]
  （旧版 P4 D4 盒底穿：墨底 1366.7 超出盒底 1358.0；新版 P4 零 flag —— 已修好，见 PROOF-NOTE §8）
```

## 7. 印/网文字层（pdftotext + 多重集/位置差分）

```
pdftotext -layout Lucerna-VOL4-ES.pdf     gates/print.txt
pdftotext -layout Lucerna-VOL4-ES-web.pdf gates/web.txt
print = web = 108,948 B；字符多重集差 0；diff 907 行全同
计数（两版一致）：本週日 11 / 下週日 0 / BABYMONSTER 0 / 取捨 2 / end point 0 / 小雪 36
```

## 8. PDF 指标（PyMuPDF，VENV 内联脚本）

```
两 PDF 各 8 页，1462.5 × 2025 pt
P8 字号：最小 9.75 pt（164 个 span：答案键 + 词汇注文 + 页眉 "— Página N —"），最大 34.5 pt；题干 10.35 pt
P1 顶部字号：147 / 45 / 27 / 24
print 23,256,381 B；web 2,529,735 B
```

## 9. 150 题三源交叉（keycheck.py v2 → keycheck-150.json）

```
注册表解析：content12→34→56→7→8 构建顺序（.ex() 含 P1 q.ex、.match_set() 4 组配对、裸 reg_ex() 第 150 题）
  vs text.md 题干 + 答案键区 vs P8 注文集 + p8 compare --total
registry 150 / text.md keys 150 / P8 noted 150 / mismatches 0 / missing 0 / keys 1–150 连续
按文件：content12 28 / content34 36 / content56 36 / content7 12 / content8 38
按题型：單選 67 / 完形單選 12 / 完成句子 54 / 配對 16 / 寫作 1
按级别：A2 44 / B1 74 / B2 32
填空键（gtools/check_fillin_keys.py）：54 条，0 缺失
手验结论（已写入 keycheck-150.json）：hand_verdict all_correct，150 题逐题 hand_verified=true；
  Q150 范文 142 字符（120–180 字带内），与 P8 注文 "(142 caracteres)" 一致
```

## 10. 泄漏 / 贴边 / 引号 / 简体（驱动内联脚本）

```
英文泄漏：deny 命中 {}；唯一共用长 ASCII 串 "A. 12:00 · B. 14:00 · C. 19:00"（构造共用）
P6 贴边：18:30 标签墨盒 [906.8,955.8,990.8,977.5] 与 19:00 标签 [991.4,955.8,1075.4,976.2]，间距 0.6 px，无重叠（与核心先例相同）
弯引号：SVG 文本节点（2,932 个）内 ASCII " 或 ' 为 0；text.md 内直引号/直撇 0；弯引号 " " 全版无
简体字：针对性简体专属字表在 text.md + 8 个 SVG 中全清；checks.py SIMP_ONLY_HITS []
E 节 type：完形單選 12 / 單選 67 / 完成句子 54 / 寫作 2（计数与核心一致，全繁体；渲染标签为西语 Completar/Escribir）
```

## 11. 机制表 242 条核对

```
242 ENTRIES es 值 vs 成品 SVG：
  237 条空格连接逐字一致；去空白连接后全部有账，仅 ENTRIES[230] 模板 "— Página {pg} —" 的 8 个渲染形
  （"— Página 1 —" 至 "— Página 8 —"）逐一在版（首轮 4 处"缺失"为 SVG 文本节点中途换行所致假阳性）
D1 本周日：表 L248（P1）、L270（P2）、L325（P4）成品各 1 次命中；"próximo domingo" 表与成品均为 0
冻结 key（非缺陷）：tables.py:245/:267/:322 "next Sunday" 仍英文；核心 content12.py:37/:113、content34.py:127 亦然
  （核心 re-proof #3 结论 (a) 已认证）
```

## 12. 目视（自渲染）

```
印刷 PDF 100 dpi：renders/p-1.png … p-8.png，8 页逐版目视：无溢出、无重叠、无压页脚、照片/图注就位
STRADDLE/P4-D4 200 dpi 对照：crops/new-p2-2.png、new-p3-3.png、new-p4-4.png、new-p5-5.png
  vs old-p2-2.png、old-p3-3.png、old-p4-4.png、old-p5-5.png；裁切 c1–c5（新/旧各一）
  C1–C3 像素全同；C4 同样超出（y 随重排 −62 px）；C5 新版盒底已包住 "deporte?"
```

## 13. 结果汇总

全部 11 类门禁 PASS，缺陷 0。唯一登记项为 PROOF-NOTE §7 的 4 处 STRADDLE（观察，非缺陷）与 §11 的 4 处核心继承观察。
