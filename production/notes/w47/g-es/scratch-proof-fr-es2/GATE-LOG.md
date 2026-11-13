# GATE-LOG — W47 fr-es proof2 独立门禁重跑日志

复校：2026-11-11，proof2。解释器一律 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。
`gates-proof.py` 为 builder `gates.py` 的副本，仅改输出目录到本 scratch（`SCR` 指向本目录；门 7 在 scratch
副本 `rerun/` 中重跑，生产目录零写入；`LOGD = SCR`，故门禁 JSON/日志落在本目录根部）。
本日志所引全部命令均为本人执行；他人并行写入本目录的文件（见 PROOF-NOTE §7）未用作证据。

工作区 `S/` = `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-es2/`
生产目录 `ED` = `~/workspace/weekly-git/production/2026-w47/2026-w47-fr-es/`
核心目录 `CORE` = `~/workspace/weekly-git/production/2026-w47/core-fr/`

## 0. 探针与身份核对

```
$ ls -la /dev/null -> crw-rw-rw- 1 root root 1, 3 Nov 11 16:04 /dev/null（存在，未重建）
$ echo probe-ok > S/tmp/probe.txt; git hash-object -w S/tmp/probe.txt
da0c4eb8d9a48d171a33574b380752e183286751（探针成功）
$ sha256sum La-Lucerna-VOL4-fr-es.pdf La-Lucerna-VOL4-fr-es-web.pdf 2026-w47-fr-es.text.md
77488ab05a39b269b38f16ebb0da59e500d1c9b8739e77a3ca3a9387712104f4  La-Lucerna-VOL4-fr-es.pdf
2e56003e9353fb3de400b27d9e6700e5ad834007e6be07b0dbe758442efbf0b3  La-Lucerna-VOL4-fr-es-web.pdf
096402b410eccd1f3d0cbcdd5cc786ec82815c967eaa0312157cd7b9b49a1d7f  2026-w47-fr-es.text.md
17,418,347 B / 1,701,681 B / 46,660 B —— 与任务书逐值一致，先核对再开工。
核心三件复核：a30af667…25a9d / 30,446,975 B；56f50ca8…58e141 / 2,241,835 B；52024e02…63df / 46,471 B —— 与任务书一致。
收尾时三件 SHA 再次逐值复核一致（生产目录未动）。
```

## 1. 独立重建（scratch 副本，`S/rerun/`）

```
$ cp ED/*.py S/rerun/; ln -s ED/assets S/rerun/assets
$ tools/venv/bin/python run.py > S/es/build-proof2.log 2>&1; echo rc=$?
rc=0
P8 saved, TOTAL exercises: 150
TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
by type {'完成句子': 49, '单选': 26, '句型转换': 7, '词汇配对': 21, '阅读判断': 5, '图表读数': 6, '跟练': 8, '改错': 4, '完形填空': 8, '阅读理解': 5, '翻译': 5, '对话补全': 5, '写作': 1}
ALL DONE
grep -c FLOW OVERFLOW|HEAD TOO WIDE|NOSPACE S/es/build-proof2.log -> 0
SVG sha 重建 vs 生产：bd6a40f0 220dd45e 1b39fa5b dd5ec45e 51b18d6f c3f18dcd 75d2252b aa084df5 = 8/8 相同
```

## 2. gates 15/15（独立重跑，exit 0）

```
$ tools/venv/bin/python S/gates-proof.py es proof2 2>&1 | tee S/es/gates-proof2.log
PASS run: exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
PASS occlusion: 0 flags, selftest OK
PASS p8_extract: keys 150/150, printed notes 121/150
PASS p8_compare: CLEAN, keydiff [150] (writing key only)
PASS source_freeze: content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
PASS string_freeze: all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
PASS freeze_direct: two builds sha256 8/8 identical: ['bd6a40f0', '220dd45e', '1b39fa5b', 'dd5ec45e', '51b18d6f', 'c3f18dcd', '75d2252b', 'aa084df5']
PASS text_layer: print/web pdftotext byte-equal (104934 B); web 1701681 B < 7MB; print 17418347 B
PASS p8_font: P8 min font 11.625pt >= 9.75pt
PASS scans: U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
PASS chips: 134 total [10, 12, 18, 15, 14, 15, 12, 38]
PASS keycheck: 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
PASS mcq: bodies: 45  rendered lines: 1479
PASS widths: 31 single-line strings all within budget
PASS band_spans: FR title ends 1236.9, band_r1 starts 1299.7, FR sub ends 837.2, band_r2 starts 1450.1
GATES 15/15 PASS
完整 JSON：S/gates-proof2.json
```

注：门 1 读取的 scratch 根目录 `build-proof2.log` 为并行进程放置的 builder 日志副本
（见 PROOF-NOTE §7）；本人独立构建日志 `S/es/build-proof2.log`（§1）与之结论一致
（rc=0、TOTAL 150、零溢出 token）。门 7 的做法：生产 SVG 只做哈希取样（只读），
在 scratch 副本 `S/rerun/` 内完整重建一次并比对 8/8 SHA——生产目录未写入。
（§1 的 `S/rerun` 与门 7 使用的为同一副本目录，门 7 重建前会先清空重建；两轮构建结果一致。）

## 3. freeze baseline + diff（`tools/freeze.py`，标准口径）

```
$ tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/core-fr \
    --core-svg production/2026-w47/core-fr/svg --out S/freeze > S/freeze/freeze-baseline.log
baseline_rc=0
baseline: 8/8 SVGs byte-identical (repointed files: render.py)
  OK p1 6aad8b4bcdfb975c / p2 5709e000bbd7b4d1 / p3 7828cfe331187278 / p4 7e46e630eb6b75aa / p5 fff2a8d3d7acdaab / p6 7af7cf3c240f222b / p7 75237d672f20f44b / p8 5bee4d4473bfc8a7（每页 produced 值与 core 值逐位相同）
core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)

$ tools/venv/bin/python tools/freeze.py diff --core-svg CORE/svg --edition-svg ED/svg \
    --json S/freeze/freeze-diff.json > S/freeze/freeze-diff.log
diff_rc=0
p1: +25 strings / -23 strings; CJK core 224 -> edition 35; added CJK chars: 0
p2: +38 strings / -33 strings; CJK core 283 -> edition 28; added CJK chars: 0
p3: +35 strings / -44 strings; CJK core 194 -> edition 20; added CJK chars: 1 {'\u3000': 1}
p4: +45 strings / -49 strings; CJK core 236 -> edition 27; added CJK chars: 0
p5: +37 strings / -42 strings; CJK core 244 -> edition 22; added CJK chars: 0
p6: +29 strings / -30 strings; CJK core 226 -> edition 25; added CJK chars: 1 {'\u3000': 1}
p7: +42 strings / -34 strings; CJK core 411 -> edition 15; added CJK chars: 0
p8: +124 strings / -122 strings; CJK core 1220 -> edition 190; added CJK chars: 8 {'\u3000': 8}
TOTAL added CJK characters: 10
```

新增 CJK 全部为 U+3000 全角空格（两段式导读条分隔符，本家庭通用结构）；无新增汉字/假名/韩文。
逐页 U+3000 计数（edition 文本元素层 vs core）：p1 35/35、p2 28/33、p3 20/19、p4 27/29、p5 22/23、
p6 25/24、p7 15/15、p8 190/182——净增 10，与 freeze diff 一致（与 #1 计数相同）。
（p4 -49 vs #1 的 -50、p7 +42 vs #1 的 +43：核心 fix4 改动 `chiffres_note` 与披露句删除所致，方向一致。）

## 4. occlusion audit（真实命令，无 --selftest）

```
$ tools/venv/bin/python tools/occlusion_audit.py --json S/occlusion.json ED/svg/ > S/occlusion.log
occl_rc=0
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
.../2026-w47-fr-es/svg/: 0 flags
```

## 5. creambox（canonical，8 页）

```
$ tools/venv/bin/python hidden_files/w47/tools/creambox.py ED/svg/*.svg > S/creambox.log
creambox_rc=0
BELOW-WINDOW（7 条，全为下一栏目标题假阳性）：
  +24.0 y=1676.0 'LE MOT DE LA SEMAINE' / +37.0 y=1127.8 'LA SEMAINE EN CHIFFRES'
  +37.0 y=412.4 'À VOUS !　¡TE TOCA!' / +37.0 y=442.1 'À VOUS !　¡TE TOCA!'
  +37.0 y=2394.7 'À VOUS !　¡TE TOCA!' / +37.0 y=826.8 'IL EST PRÉVU QUE + SUBJONCTIF'
  +37.0 y=1693.7 'LE DÉBAT　DEBATE'
P7-TOOLBOX summary: 4 boxes, min inside clearance +24.7, min desc-clear +18.8
  inside-only [P7-TOOLBOX]: last baseline 2233.3 clearance +24.7 desc-clear +18.8 | 'promesa de comentar envíos reales.'
```

P7 PIL 真墨（印刷版 PDF，200 dpi）：

```
$ tools/venv/bin/python scratch-refanout-fr2/pil_p7.py es
es last disclosure-grey ink svg y: 2237.3
es grey ink in gap 2258..2270: NONE (clean)
自写全色扫描：last dark-ink row svg y: 2279.5（绿带本体填充，非文字墨；2258–2270 间隙全色深墨亦为 NONE）
裁切：S/png/crop-p7-boxbottom.png（200 dpi，盒底目视干净，见 PROOF-NOTE §6）
```

## 6. spill sweep（本人 PIL 真墨扫，`S/sweep_spill.py`）

覆盖 creambox + occlusion BOXTITLE 的盲区：无描边奶油框的墨边穿越（EDGE-*）、
基线在盒内但横向溢出（HSPILL）、墨触盒而基线在盒外（TOUCH-OUT）。
字墨盒用 `tools/occlusion_audit.py::ink_box`（与 canonical 审计同字体映射）。

```
$ tools/venv/bin/python S/sweep_spill.py ED/svg/ > S/spill.log
p1: 5 cream boxes, 182 texts, 0 flags / p2: 3, 188, 0 / p3: 4, 190, 0 / p4: 6, 200, 0
p5: 6, 187, 0 / p6: 4, 207, 0 / p7: 4, 193, 0 / p8: 1, 310, 0
TOTAL FLAGS: 0
核心对照：$ tools/venv/bin/python S/sweep_spill.py CORE/svg/ > S/spill-core.log -> TOTAL FLAGS: 0
阳性对照（#1 备份旧 P7，S/oldp7/）：2 flags
  ('EDGE-B', 1013.0, 2260.6, 'envíos reales.', 'box y+h=2258.0 ink 2243.6..2260.9')
  ('TOUCH-OUT', 1013.0, 2260.6, 'envíos reales.', 'box y 1878.0..2258.0')
——扫法能检出旧缺陷，新版 0 flags 不是空转。初版 HSPILL 误判（同 y 带不同栏文本）已修正：
仅当墨与盒横向重叠且越边才计旗；修正后重跑 edition/core 均为 0。
```

## 7. check_extra / Q148 / 孤行填空线

```
$ tools/venv/bin/python S/check_extra.py es proof2 > S/extra.log   （修正后版，本人 scratch 副本）
extra_rc=0
orphan elements: total=0 new=0 inherited=0 remnant=0 shared_baseline=0
blank lines core: [{'page': 'p3', 'y': 1864.7, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 1997.4, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}]
blank lines es:   [{'page': 'p3', 'y': 1924.1, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 2056.8, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}] ok=True
Q148: stem_ok=True key_in_content8=True extracted='devant le'
EXTRA PASS        （S/es/extra-proof2.json）
```

Q148 本人独立三重核对（另行 Python 解析 `<text>` 元素，不依赖 check_extra）：
P8 文本层含 `On se retrouve (148)___ cinéma ?`、不含 `du cinéma`；
`content8.py:170` 键 `devant le`、`:176` 题干无 `du`；extract 键 `devant le`；核心键 `devant le`。

## 8. keycheck 与 150 键手核

```
p8 extract: keys 150/150, notes 121/150（S/p8-proof2.json）；compare CLEAN, keydiff [150]（S/p8compare-proof2.json）
REG（S/regdump/ 重跑导出 S/reg.json）vs P8 提取 vs 核心 final-fr-p8.json：仅 Q150 不同（REG 全句 vs P8 短键 'Pregunta abierta' vs 核心 '开放题'）。
逐项手核表：S/key-stem-table-MINE.txt（150 行）；核对方法与逐项结论见 PROOF-NOTE §1.5。
```

## 9. print/web 文本层、字号、CJK

```
pdftotext -layout print/web（gates 门 8，S/print-proof2.txt、S/web-proof2.txt）：byte-equal，104,934 B；web 1,701,681 B < 7 MB
P8 min font（PyMuPDF spans，印刷 PDF p8）：11.625pt ≥ 9.75pt；P8 SVG 文本最小字号 15.5pt
SVG 文本元素层 CJK：仅 U+3000（362 个）；零真实 CJK；.text.md CJK 仅 U+3000；U+2019=0、U+00B7=0
```

## 10. §1.1 适配检查（本人 `S/s11_fr_mine.py`）

```
$ tools/venv/bin/python S/s11_fr_mine.py es > S/s11.log
s11_rc=0
  VOL note p6-politique.svg: VOL.5 core=0 ed=1 -- adjudicated in PROOF-NOTE (P6 calendar note:
     es E value 'Calendario previsto; ... en el VOL.5.' vs core '本页日程为计划安排，18 日投票结果下期跟进。'
colour set: core 19 edition 19 extra: none missing: none
badge A2 #5c6e30: True / B1 #46581f: True / B2 #37402f: True
P8 min SVG font-size: 15.5
P8 head EXERCICES: True / RÉPONSES: True / ÉCRITURE: True / MODÈLE: True
real CJK in edition SVGs: none | U+3000 count: 362
ALL S11-FR (MINE) CHECKS PASS
```

初版两 FAIL 均系脚本口径，已逐一裁定并修正脚本后重跑全过：
(a) VOL.5 计数差：实为 `chart_note` 翻译（核心「下期」→ es「en el VOL.5」，`expl.py:128` vs 核心 `:129`），
属合法翻译，gates string_freeze 亦计为 1 例外；(b) 「真实 CJK」初版把 `<title>Lucerna 三色蛾</title>`
（P1 嵌套 moth 品牌 SVG 内，核心版亦同，非渲染文本元素）计入，改按 `<text>` 元素层扫描后为 none；
另修正 U+3000 落在 `\u2e80–\u31ef` 数值区间的误判（U+3000 为允许项）。

### check_s11.py / verify_ed.py（任务书所列）

全仓检索：`find hidden_files/w47 -name check_s11.py / verify_ed.py` 检出的全部副本均为 **en 族**
（core-en 路径、`p8-test.svg` 页名、`registry.json`），fr 族不存在此二工具，无法在 fr-es 上运行。
其检查意图由 gates 15 门（§1.1 scans/chips/widths/band_spans/p8_font）+ 本人 `s11_fr_mine.py` 全面覆盖，
结果见 §2 / §10。此非遗漏项。

## 11. D5 字体（只记录，不判定）

```
web PDF spans（PyMuPDF）：8 页；p1 字体集 LucernaNewsreader-Bold/Italic/Regula、LucernaNotoSansCJKSC-Bol/Reg、LucernaUnifrakturMagunti
'Votación del Senado' -> LucernaNotoSansCJKSC-Reg 14.25pt p1
'envíos reales' -> LucernaNotoSansCJKSC-Reg 14.62pt p7
'EXPLICACIONES EN ESPAÑOL' -> LucernaNotoSansCJKSC-Reg 12.75pt p1
'ALCARAZ GAGNE PARIS' -> LucernaNotoSansCJKSC-Bol 34.5pt p1
'Dimanche 8 novembre, Carlos Alcaraz' -> LucernaNewsreader-Regula 18.0pt p1
```
讲解层拉丁字符落在 Noto Sans CJK SC，与 #1 实测一致，全周级待用户裁定，不据此判 (b)。

## 12. 回归对照（vs #1 备份 `scratch-refanout-fr2/backup-old/2026-w47-fr-es/`）

```
SVG sha：p1 SAME bd6a40f0 / p2 SAME 220dd45e / p3 SAME 1b39fa5b / p4 SAME dd5ec45e
         p5 SAME 51b18d6f / p6 SAME c3f18dcd / p7 CHANGED c7fc6d9e -> 75d2252b / p8 CHANGED 20df945f -> aa084df5
源码 diff：仅 expl.py（:182 courrier_disclosure 删中句）与 content8.py（:170 键、:176 题干）；
         content12/34/56/7、bslib4、svglib、run、render 全部 identical
.text.md diff：恰 3 行（披露句、Q148 题干、Q148 答案行）；ABSTRACT.txt identical
KEEP/REVERT：#1 仅 1 缺陷 D-1，无其他 hand patch；两处改动与两项规定修复一一对应。
```

## 13. 目视证据

```
S/png/p-1.png – S/png/p-8.png（本人 pdftoppm -r 100 自 verified SHA 印刷 PDF 渲染）
S/png/p7-200.png、S/png/crop-p7-boxbottom.png（200 dpi 盒底裁切）
逐页结论见 PROOF-NOTE §6：8 页全部干净。
```

## 14. 生产目录完整性

```
复校全程未写 production 下任何文件，未 commit、未 push。
收尾 sha256sum：print 77488ab0…2104f4 / web 2e56003e…fbf0b3 / text 096402b4…a1d7f，与开工前逐值一致。
git status --porcelain -- production/2026-w47/2026-w47-fr-es/ production/2026-w47/core-fr/
  -> 仅 '??'（两目录为未入仓新内容），无修改记录。
```
