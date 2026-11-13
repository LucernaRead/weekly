# GATE-LOG — W47 zh-tw × ru proof1（机械门输出留档）

复校对象 `~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-ru/`，工具一律 `~/workspace/weekly-git/tools/venv/bin/python`，输出存于本目录。

## 0. 对象核验 + 探针（2026-11-11 09:21 UTC）

```
echo test | git -C ~/workspace/weekly-git hash-object -w --stdin
# -> 9daeafb9864cf43055ae93beb0afd6c7d144bfa4（写盘探针成功）
sha256sum Lucerna-VOL4-RU.pdf Lucerna-VOL4-RU-web.pdf 2026-w47-zh-tw-ru.text.md
# e1f3c46a9e22a3b03c9b8a6c9fc450b86bb254ccbec223169b682c2447c2ff76  Lucerna-VOL4-RU.pdf
# 385e4b265347bb5d87442934b60f9b2c1bac88b48bfc20ca98033bc54d6a0719  Lucerna-VOL4-RU-web.pdf
# 41da5432e31c1f9819a6508d8fc91933a64ac6cd8b0a0794e32f0d10e0319f09  2026-w47-zh-tw-ru.text.md
# 字节：print 12896270 / web 1993092 / text.md 62485 —— 与任务给定全符
```

## 1. occlusion 审计 — 0 flags

```
tools/venv/bin/python tools/occlusion_audit.py <edition>/svg --json occlusion.json
# rc=0
# selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
# <edition>/svg: 0 flags
```
输出：`occlusion.json`、`occlusion.log`。

## 2. p8 extract — 150/150；p8 compare — CLEAN

```
tools/venv/bin/python tools/p8.py extract --p8 <edition>/svg/p8-test.svg --total 150 --json p8-extract.json
# rc=0；noted set = 150 of 150 (parse: lines)；set: [1..150]
tools/venv/bin/python tools/p8.py compare --core-p8 <core>/svg/p8-test.svg --edition-p8 <edition>/svg/p8-test.svg --total 150 --json p8-compare.json
# rc=0
# core 150 noted；edition 150 noted
# status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[]
```
输出：`p8-extract.json`、`p8-extract.log`、`p8-compare.json`、`p8-compare.log`。**keydiff 为空，无逐项差异可列。**

## 3. freeze baseline — 8/8；freeze diff --strict-cjk — FAIL rc=1（+36 字，已定位）

```
tools/venv/bin/python tools/freeze.py baseline --build <edition> --core-svg <edition>/svg --out freeze
# rc=0
# baseline: 8/8 SVGs byte-identical (repointed files: content12.py, content34.py, content56.py, content7.py, content8.py)
#   OK p1-front 3e5b9d5270f1e3d3 / p2-life ff50565c150562d3 / p3-culture 53b8e8c831c5bfc3 / p4-sport 23ecd7132275a7be
#   OK p5-youth d2f6511b8097fcbc / p6-deep b6d1b537 / p7-lang c0e4e11bd3de662c / p8-test c8f4c218865ee023
# core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
tools/venv/bin/python tools/freeze.py diff --core-svg <core>/svg --edition-svg <edition>/svg --strict-cjk --json freeze-diff.json
# rc=1
# STRICT-CJK FAIL: edition adds CJK characters the core does not have
# p1: +28/-28 strings; added CJK: 4 {'俄': 2, '下': 2}
# p2: +43/-40; added: 2 {'下': 1, '俄': 1}
# p3: +55/-50; added: 3 {'下': 2, '俄': 1}
# p4: +46/-43; added: 4 {'下': 3, '俄': 1}
# p5: +62/-47; added: 17 {'月': 1, '日': 1, '、': 1, '演': 1, '台': 2, '：': 1, '會': 1, '唱': 1, '巨': 1, '北': 2}
# p6: +37/-33; added: 1 {'俄': 1}
# p7: +356/-107; added: 2 {'下': 1, '俄': 1}
# p8: +202/-188; added: 3 {'下': 1, '。': 1, '俄': 1}
# TOTAL added CJK characters: 36
```

独立复算（SVG 文本去空白后 CJK 多重集差）与工具一致；成因定位见 PROOF-NOTE §1/§2：
`俄` = 家具 `英語講解`→`俄語講解`；`下` = D1（核心已改 `本週日`）；P5 余字 = N3 BABYMONSTER 行；P8 `。` = N5 key 134 句尾。无其他新增中文内容。
输出：`freeze-baseline.log`、`freeze-diff.log`、`freeze-diff.json`、`freeze/`（重跑副本目录）。

## 4. 印/网文字层比对 — 多重集差 0

```
pdftotext Lucerna-VOL4-RU.pdf print.txt       # 58526 bytes
pdftotext Lucerna-VOL4-RU-web.pdf web.txt     # 58528 bytes
# 字符多重集（去空白）：print 24955 / web 24955；only in print {}；only in web {}；diff total 0
```
输出：`print.txt`、`web.txt`。

## 5. P8 最小字号（PyMuPDF，tools/venv）

```
# Lucerna-VOL4-RU.pdf：8 页，1462.5 x 2025.0 pt
#   P8 sizes: 9.75pt: 6786 字；10.35pt: 1083；11.25: 103；11.62: 48；12.0: 158；12.75: 43；13.5: 44；14.25: 91；14.62: 151；15.0: 54；15.75: 113；18.0: 152；18.75: 65；34.5: 25
#   P8 min size: 9.75
# Lucerna-VOL4-RU-web.pdf：同上，P8 min size 9.75（字体为子集改名版 LucernaNewsreader-Regula / LucernaNotoSansCJKTC-* / LucernaNotoSerifCJKTC-Re）
```
结论：双 PDF 均为 9.75pt，恰达 SOP §1.1 下限。

## 6. 弯引号 / 简体字 / 编号（自写核查脚本，SVG 文本层）

```
# ASCII " : 0；ASCII ' : 0；U+201C: 5（均为 „…" 内层闭合引号）；U+201D: 0；U+2019: 0；«: 27；»: 27
# 半角 : 只出现在俄语句内与 HH:MM 时间写法；全角 ： 90 处（中文标号）
# 简体专用字：0 命中
# text.md 编号 1–150 全齐，无缺无重；配对组 25–28. / 43–46. / 61–64. / 79–82. 俱在
# 金句 8/8 各恰 2 次（去空白后 SVG 文本检索）：P1×2、P2×2、P3×2、P4×2、P5×2（正文页 + P7）
# 范文 142 字（120–180 内）
```

## 7. 机制层核查（tables.py vs 版内 SVG）

```
# tables.py ENTRIES: 238；"ru" 值 238 条；逐字比对版内 SVG（去空白）：237/238 命中
# 唯一未命中：— Страница {pg} —（带 {pg} 占位符的模板串，非缺陷）
# D1 俄语串在表内：L252 / L274 / L329（"следующее воскресенье"）
# N1 语法错在表内：L2070（"Выучите их раз"）
# N2 缺口：grep "Тайбэйском музыкальном центре" / "Сяосюэ — 22 ноября" / "Четыре больших события" / "Накапливать баллы" —— 0 命中
# N6/N7 在表内：[31]/[148] "гигантский шар-Пикачу"；[138]/[165] "Рождество в Диснее"
```
辅助文件：`/tmp/ru_entries.txt`（238 条 ru 值转储，仅作核查用，不入档）。

## 8. 渲染卡逐版目视（cards/*.png，8/8）

P1、P2、P3、P4、P5、P6、P7、P8 全部看过：无溢出、无重叠、无压页脚。另渲染网页 PDF P1/P7（`web-p1.png`、`web-p7.png`，72dpi）与印刷卡比对：版式/字重一致，网页工具层 0 发现。
