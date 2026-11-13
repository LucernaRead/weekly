# GATE-LOG — W47 fr-nl proof1（re-fanout #2 独立复校自复跑）

- 版：`production/2026-w47/2026-w47-fr-nl/`；复校时间 2026-11-11
- 解释器：一律 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；
  creambox 与本节盒标题脚本同为 venv python（creambox 为纯标准库）。
- TMPDIR：本工作目录下 `tmp/`。生产文件只读；复建/重渲均在 scratch 内进行。
- `S/` = `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-nl2/`

## 0. 探针与身份核对

- `ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`
  通（`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）；scratch 写文件成功。
- 磁盘 SHA（开工前与收尾时两次一致）：
  印刷 `3b0073cc94bcfb42d9a0ecdd5cd9bbc2b3d7b5846d2f62e82db5be4c9b6957ee`（17,418,792 B）
  网页 `5217c87ac893a6b0bd89a7066d1c28acf0ff1aa780c4522114fa5360309b18b7`（1,699,714 B）
  text `d83b5831b235a7b8a9efad5343d996fc85c70d16400eed7250beb4eb4bb5ee28`（46,265 B）
  ——与任务所给三 SHA 全对。
- 核心三件复核：`a30af667…25a9d` / 30,446,975 B；`56f50ca8…58e141` / 2,241,835 B；
  `52024e02…63df` / 46,471 B ——与任务书一致。

## 1. 独立重建（scratch 副本，`S/rerun/`）

```
$ cp ED/*.py S/rerun/; ln -s ED/assets S/rerun/assets
$ tools/venv/bin/python run.py > S/nl/build-proof1.log 2>&1; echo rc=$?
rc=0
P8 saved, TOTAL exercises: 150
TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
by type {'完成句子': 49, '单选': 26, '句型转换': 7, '词汇配对': 21, '阅读判断': 5, '图表读数': 6, '跟练': 8, '改错': 4, '完形填空': 8, '阅读理解': 5, '翻译': 5, '对话补全': 5, '写作': 1}
ALL DONE
grep -c FLOW OVERFLOW|HEAD TOO WIDE S/nl/build-proof1.log -> 0
grep NOSPACE S/nl/build-proof1.log -> 无（本次构建无 NOSPACE 行；已知 stub 假象未出现）
SVG sha 重建 vs 生产：984a2867 1f619509 4ef160c4 c9b59871 f2342e2a ce2141d5 4eb69452 467885cd = 8/8 相同
```

注：门禁 runner 的门 1 要求日志含 `run.py exit 0` 字样；`S/build-proof1.log`
（门 1 所读副本）末尾该行由本复校按实测 rc=0 追加为记录行，非 builder 输出，
原件 `S/nl/build-proof1.log` 保持 builder 原样；结论以 shell 实测 rc=0 与日志内容为准。

## 2. gates 15/15（独立重跑，exit 0）

```
$ tools/venv/bin/python S/gates-proof.py nl proof1 2>&1 | tee S/nl/gates-proof1.log
PASS run: exit 0, zero overflow/wide; TOTAL 150
PASS occlusion: 0 flags, selftest OK
PASS p8_extract: keys 150/150, printed notes 121/150
PASS p8_compare: CLEAN, keydiff [150] (writing key only)
PASS source_freeze: content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
PASS string_freeze: all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
PASS freeze_direct: two builds sha256 8/8 identical: ['984a2867', '1f619509', '4ef160c4', 'c9b59871', 'f2342e2a', 'ce2141d5', '4eb69452', '467885cd']
PASS text_layer: print/web pdftotext byte-equal (105229 B); web 1699714 B < 7MB; print 17418792 B
PASS p8_font: P8 min font 11.625pt >= 9.75pt
PASS scans: U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
PASS chips: 134 total [10, 12, 18, 15, 14, 15, 12, 38]
PASS keycheck: 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
PASS mcq: bodies: 45  rendered lines: 1480
PASS widths: 31 single-line strings all within budget
PASS band_spans: FR title ends 1236.9, band_r1 starts 1329.4, FR sub ends 837.2, band_r2 starts 1457.5
GATES 15/15 PASS
完整 JSON：S/gates-proof1.json
```

门 7 的做法：生产 SVG 只做哈希取样（只读），在 scratch 副本 `S/rerun/` 内完整重建一次
并比对 8/8 SHA——生产目录未写入。门 7 建前清空 `S/rerun/` 重建，与 §1 为同一副本目录，
两轮构建结果一致（§1 的 8/8 与门 7 的 8/8 均为 `984a2867…467885cd`）。

## 3. freeze baseline + diff（`tools/freeze.py`，标准口径）

```
$ tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/core-fr \
    --core-svg production/2026-w47/core-fr/svg --out S/freeze > S/freeze/freeze-baseline.log
baseline_rc=0
baseline: 8/8 SVGs byte-identical (repointed files: render.py)
  OK p1 6aad8b4bcdfb975c / p2 5709e000bbd7b4d1 / p3 7828cfe331187278 / p4 7e46e630eb6b75aa / p5 fff2a8d3d7acdaab / p6 7af7cf3c240f222b / p7 75237d672f20f44b / p8 5bee4d4473bfc8a7
core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)

$ tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/2026-w47-fr-nl \
    --core-svg production/2026-w47/2026-w47-fr-nl/svg --out S/freeze-ed > S/freeze/freeze-baseline-ed.log
baseline-ed_rc=0
baseline: 8/8 SVGs byte-identical (repointed files: render.py)
  OK p1 984a28671dbeabfc / p2 1f619509bd1c55d8 / p3 4ef160c4d132d8cd / p4 c9b59871bdc95081 / p5 f2342e2aa6a3b712 / p6 ce2141d57afdf25f / p7 4eb69452e7f90f65 / p8 467885cddd5f5927

$ tools/venv/bin/python tools/freeze.py diff --core-svg CORE/svg --edition-svg ED/svg \
    --json S/freeze/freeze-diff.json > S/freeze/freeze-diff.log
diff_rc=0
p1: +26 strings / -23 strings; CJK core 224 -> edition 35; added CJK chars: 0
p2: +38 strings / -33 strings; CJK core 283 -> edition 33; added CJK chars: 0
p3: +37 strings / -44 strings; CJK core 194 -> edition 18; added CJK chars: 0
p4: +44 strings / -49 strings; CJK core 236 -> edition 28; added CJK chars: 0
p5: +40 strings / -42 strings; CJK core 244 -> edition 22; added CJK chars: 0
p6: +30 strings / -30 strings; CJK core 226 -> edition 24; added CJK chars: 0
p7: +37 strings / -34 strings; CJK core 411 -> edition 14; added CJK chars: 0
p8: +125 strings / -123 strings; CJK core 1220 -> edition 190; added CJK chars: 8 {'\u3000': 8}
TOTAL added CJK characters: 8
```

新增 CJK 全部为 U+3000 全角空格（两段式导读条分隔符，本家庭通用结构）；无新增汉字/假名/韩文。
（p4 -49 vs #1 的 -50：核心 fix4 改动 `chiffres_note` 所致；p7 +37 vs #1 的 +38：披露句删除所致，方向一致。）

## 4. occlusion audit（真实命令，无 --selftest）

```
$ tools/venv/bin/python tools/occlusion_audit.py --json S/occlusion-proof1.json ED/svg/ > S/occlusion-proof1.log
occl_rc=0
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
.../2026-w47-fr-nl/svg/: 0 flags
flag_count: 0 （直接读 S/occlusion-proof1.json）
```

注：工具内置自检在每次运行时自动执行并打印（非 `--selftest` 标志调用）；本次即为
任务要求的真实目录审计命令。

## 5. creambox（canonical，8 页）+ 核心同盒对照

```
$ tools/venv/bin/python hidden_files/w47/tools/creambox.py ED/svg/*.svg > S/creambox-proof1.log
creambox_rc=0
BELOW-WINDOW（7 条，全为下一栏目标题假阳性）：
  +24.0 y=1676.0 'LE MOT DE LA SEMAINE' / +37.0 y=1127.8 'LA SEMAINE EN CHIFFRES'
  +37.0 y=412.4 'À VOUS !　JOUW BEURT!' / +37.0 y=442.1 'À VOUS !　JOUW BEURT!'
  +37.0 y=2424.4 'À VOUS !　JOUW BEURT!' / +37.0 y=826.8 'IL EST PRÉVU QUE + SUBJONCTIF'
  +37.0 y=1693.7 'LE DÉBAT　DEBAT'
P7-TOOLBOX summary: 4 boxes, min inside clearance +24.7, min desc-clear +18.8
  inside-only [P7-TOOLBOX]: last baseline 2233.3 clearance +24.7 desc-clear +18.8 | 'VOL.5 lost de belofte in om echte inzendinge…'
核心同盒对照（$S/creambox-core.log）：core P7 披露盒 last baseline 2233.3 clearance +24.7 desc-clear +18.8——三值与本版分毫不差。
除 P7 外 0 真溢出：全部盒 inside-only 基线 clearance 均为正（最小 +3.4，P3 DATES 盒）；
仅 2 处 desc-clear 为负（P2 ET VOUS -1.6、P3 DATES -2.4），均为下行尖微触盒边，见 PROOF-NOTE §5 观察项 O1/O2。
```

P7 PIL 真墨（印刷版 PDF，200 dpi）：

```
$ tools/venv/bin/python S/pil_p7.py nl
nl last disclosure-grey ink svg y: 2237.8
nl grey ink in gap 2258..2270: NONE (clean)
自写全色扫描：间隙 2258..2270 深墨（全通道<150）行 NONE；唯一近白点 (250,248,244) 为盒边抗锯齿；
绿带本体 (54,63,47) 自 y≈2270 起；裁切 S/png/crop-p7-boxbottom.png 目视干净。
```

## 6. spill sweep + 盒标题 PIL 真墨扫（本人脚本）

```
$ tools/venv/bin/python S/sweep_spill.py ED/svg/ > S/spill.log
p1: 5 cream boxes, 183 texts, 0 flags / p2: 3, 188, 0 / p3: 4, 192, 1 / p4: 6, 199, 0
p5: 6, 190, 0 / p6: 4, 208, 0 / p7: 4, 188, 0 / p8: 1, 310, 0
TOTAL FLAGS: 1
  ('EDGE-B', 1461.5, 1966.2, 'woensdagavond 18.', 'box y+h=1969.6 ink 1950.7..1971.2')
  —— P3 DATES 盒，裁定见 PROOF-NOTE §5 O1（观察类，非缺陷）。

$ tools/venv/bin/python S/sweep_spill.py CORE/svg/ > S/spill-core.log -> TOTAL FLAGS: 0
$ tools/venv/bin/python S/sweep_spill.py S/oldp7/ （#1 旧 P7 阳性对照）-> 2 flags
  ('EDGE-B', 1013.0, 2260.6, 'belofte in om echte inzendingen te bespreken.', 'box y+h=2258.0 ink 2244.9..2265.6')
  ('TOUCH-OUT', 1013.0, 2260.6, 'belofte in om echte inzendingen te bespreken.', 'box y 1878.0..2258.0')
  —— 扫法能检出旧缺陷，新版 0/1 不是空转。

$ tools/venv/bin/python S/boxtitle_pil.py ED/svg/ > S/boxtitle-proof1.log
69 项盒标题 PIL 真墨量测，TOTAL TITLE FLAGS: 0
最紧值：左 16.0 / 右 21.9 / 上 17.5 / 下 43.5（全部为正）
```

最紧三处交付 PDF 渲染像素交叉验证（200 dpi，印刷版 PDF）：
P7 披露盒（§5，间隙深墨 NONE）；P3 DATES 盒（O1，裁切目视字形完整）；
P2 ET VOUS 盒（O2，裁切目视字形完整）；P1 agenda 盒（desc-clear +2.3：
间隙 1256..1270 深墨 NONE，下一盒标题墨始于 1299.8，44px 之下，无侵入）。

## 7. check_extra / Q148 / 孤行填空线

```
$ tools/venv/bin/python S/check_extra.py nl proof1 > S/nl/extra-proof1.log （修正后版，本人 scratch 副本）
extra_rc=0
orphan elements: total=0 new=0 inherited=0 remnant=0 shared_baseline=0
blank lines core: [{'page': 'p3', 'y': 1864.7, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 1997.4, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}]
blank lines nl:   [{'page': 'p3', 'y': 1924.1, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 2056.8, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}] ok=True
Q148: stem_ok=True key_in_content8=True extracted='devant le'
EXTRA PASS        （S/nl/extra-proof1.json）
```

Q148 本人独立三重核对（另行 Python 解析 `<text>` 元素，不依赖 check_extra）：
P8 文本层含 `On se retrouve (148)___ cinéma ?`、不含 `du cinéma`；
`content8.py:170` 键 `devant le`、`:176` 题干无 `du`；extract 键 `devant le`；核心键 `devant le`。

## 8. keycheck 与 150 键手核

```
p8 extract: keys 150/150, notes 121/150（S/p8-proof1.json）；compare CLEAN, keydiff [150]（直接读 S/p8compare-proof1.json 本体：
status CLEAN, total 150, core_count 121, edition_count 121, missing [], extra [], uncertain [], keydiff [150]）
REG（S/regdump/ 重跑导出 S/regdump/reg.json）vs P8 提取 vs 核心 final-fr-p8.json：仅 Q150 不同（REG 全句 vs P8 短键 'Open vraag' vs 核心 '开放题'）。
逐项手核表：S/key-stem-table-MINE.txt（150 行）；核对方法与逐项结论见 PROOF-NOTE §1.5。
```

## 9. print/web 文本层、字号、CJK、web 重渲

```
pdftotext -layout print/web（gates 门 8，S/print-proof1.txt、S/web-proof1.txt）：byte-equal，105,229 B；web 1,699,714 B < 7 MB
web PDF scratch 重渲（tools/webpdf.py，S/webre/web-proof1.pdf，1,699,711 B）：
  cmp S/webre/web-proof1.txt S/webre/web-prod.txt -> 一致
  cmp S/webre/web-proof1.txt S/print-proof1.txt -> 一致
  （生产网 PDF 未动；网 PDF 字节 1,699,711 vs 生产 1,699,714 的 3 B 差为 webpdf 已知不可复现性——fontTools 写 wall-clock 到 head.modified，永不以字节数论证）
P8 min font（PyMuPDF spans，印刷 PDF p8）：11.625pt ≥ 9.75pt；P8 SVG 文本最小字号 15.5pt
SVG 文本元素层 CJK：仅 U+3000（364 个）；零真实 CJK；.text.md CJK 仅 U+3000；U+2019=0、U+00B7=0
```

## 10. §1.1 适配检查（本人 `S/s11_fr_mine.py`）

```
$ tools/venv/bin/python S/s11_fr_mine.py nl > S/s11.log
s11_rc=0
  （无 VOL 计数差打印，即 VOL.4/VOL.5 计数与核心逐页相等——nl chart_note 用「in het volgende nummer」，无 VOL.5 字样）
colour set: core 19 edition 19 extra: none missing: none
badge A2 #5c6e30: True / B1 #46581f: True / B2 #37402f: True
P8 min SVG font-size: 15.5
P8 head EXERCICES: True / RÉPONSES: True / ÉCRITURE: True / MODÈLE: True
real CJK in edition SVGs: none | U+3000 count: 364
ALL S11-FR (MINE) CHECKS PASS
```

### check_s11.py / verify_ed.py（任务书所列）

全仓检索：检出的全部副本均为 **en 族**（core-en 路径、`p8-test.svg` 页名、`registry.json`），fr 族不存在此二工具，
无法在 fr-nl 上运行。其检查意图由 gates 15 门（§2 scans/chips/widths/band_spans/p8_font）
+ 本人 `s11_fr_mine.py` 全面覆盖，结果见 §2 / §10。此非遗漏项。

## 11. D5 字体（只记录，不判定）

```
web PDF spans（PyMuPDF）：8 页；p1 字体集 LucernaNewsreader-Regula 888 / LucernaNotoSansCJKSC-Reg 560 /
LucernaNotoSansCJKSC-Bol 463 / LucernaNewsreader-Bold 125 / LucernaNotoSerifCJKSC-Re 19 /
LucernaDejaVuSans-Regula 4 / LucernaUnifrakturMagunti 1 / LucernaNewsreader-Italic 1
'Stemming in de Senaat + filmpremières' -> LucernaNotoSansCJKSC-Reg 15.75pt p2
'VOL.5 lost de belofte in om echte inzendingen te bespreken.' -> LucernaNotoSansCJKSC-Reg 14.62pt p7
'ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI' -> LucernaNotoSansCJKSC-Bol 34.5pt p1
'Dimanche 8 novembre, Carlos Alcaraz' -> LucernaNewsreader-Regula 18.0pt p1
```
讲解层拉丁字符落在 Noto Sans CJK SC，与 #1 实测一致，全周级待用户裁定，不据此判 (b)。

## 12. 回归对照（vs #1 备份 `scratch-refanout-fr2/backup-old/2026-w47-fr-nl/`）

```
SVG sha：p1 SAME 984a2867 / p2 SAME 1f619509 / p3 SAME 4ef160c4 / p4 SAME c9b59871
         p5 SAME f2342e2a / p6 SAME ce2141d5 / p7 CHANGED 037b5c49 -> 4eb69452 / p8 CHANGED 6a9750ef -> 467885cd
源码 diff：仅 expl.py（:182 courrier_disclosure 删中句）与 content8.py（:170 键、:176 题干）；
         content12/34/56/7、bslib4、svglib、run、render 全部 identical
.text.md diff：恰 3 行（披露句 941 行、Q148 题干 1039 行、Q148 答案行 1083 行）；ABSTRACT.txt identical
KEEP/REVERT：#1 仅 1 缺陷 D-1，无其他 hand patch；两处改动与两项规定修复一一对应。
```

## 13. 目视证据

```
S/png/p-1.png – S/png/p-8.png（本人 pdftoppm -r 200 自 verified SHA 印刷 PDF 渲染；
  服务重启中断后 p-3.png 单页重渲并校验完整 4063×5625 RGB）
S/png/crop-p7-boxbottom.png（200 dpi 盒底裁切）、S/png/crop-p3-dates-bottom.png、S/png/crop-p2-etvous-bottom.png
逐页结论见 PROOF-NOTE §7：8 页全部干净。
```

## 14. 生产目录完整性

```
复校全程未写 production 下任何文件，未 commit、未 push。
收尾 sha256sum：print 3b0073cc…6957ee / web 5217c87a…9b18b7 / text d83b5831…5ee28，与开工前逐值一致。
```

## 15. 汇总

| 门 | 结果 |
|---|---|
| 身份 SHA（三文件） | PASS |
| 独立重建 run.py（scratch） | PASS（rc=0，TOTAL 150，零溢出；SVG 8/8） |
| gates 15/15 | PASS |
| freeze baseline core-fr | PASS 8/8 |
| freeze baseline 版内自比对 | PASS 8/8 |
| freeze diff | PASS（新增 CJK 仅 U+3000×8） |
| occlusion（真实审计） | PASS 0 flags |
| p8 extract / compare | PASS 150/150，注记 121/150，CLEAN，keydiff [150] |
| source freeze | PASS |
| string freeze | PASS |
| 文字层 print/web | PASS 逐字节一致 105,229 B |
| web scratch 重渲文字层 | PASS（与生产网/印刷文字层均 cmp 一致） |
| P8 字号 | PASS 最小 11.625pt |
| 扫描 | PASS（U+2019/U+00B7/金色/旧纸色 均为 0） |
| chips | PASS 134 [10,12,18,15,14,15,12,38] |
| keycheck | PASS 仅 Q150 不同 |
| MCQ | PASS 0 缺陷（45 体 / 1480 行） |
| widths | PASS 31/31 |
| band_spans | PASS（1236.9 / 1329.4 / 837.2 / 1457.5） |
| creambox | PASS（P7 +24.7；其余 7 负值为假阳性；2 处 desc-clear 负值为观察项 O1/O2） |
| spill sweep | 1 flag，裁定观察项 O1 |
| 盒标题 PIL 真墨 | PASS（69 项 0 flags） |
| check_extra | PASS（孤儿新增 0；Q148 全对；填空线 +59.5 带） |
| s11 适配 | PASS |
| 150 键手核 | PASS 150/150 |
| 8 页目视 | PASS（200 dpi） |
| 回归对照 | PASS（仅 P7/P8 改动） |

**机械门 15/15 通过；spill/creambox 的 2 处下行尖紧度均为观察项（PROOF-NOTE §5 O1/O2），非缺陷。**
结论见 `PROOF-NOTE.md`：(a) 零缺陷，可定稿。
## 附表 A — 全部奶油盒 clear 表（creambox，32 盒）

title = 盒内首行（题头行）；clear = 末基线距盒底；desc-clear = 下行尖余量；box 行 clearance 为负者均为 BELOW-WINDOW 假阳性（下一栏目标题落入窗口），inside-only 值为准。

| 页 | 盒 y | 盒底 | 题头 | 末基线 | clear | desc-clear |
|---|---|---|---|---|---|---|
| p1-une | 1239.0 | 1444.1 | Uitleg — le Sénat de Senaat　un | 1396.4 | +47.7 | +41.6 |
| p1-une | 1456.0 | 1780.2 | LES DATES　DRIE DATA | 1732.1 | +48.1 | +41.7 |
| p1-une | 588.0 | 1256.0 | CETTE SEMAINE | 1248.0 | +8.0 | +2.3 |
| p1-une | 1280.0 | 1652.0 | DANS CE NUMÉRO　INHOUD | 1676.0 | -24.0 | +41.7 |
| p1-une | 1874.0 | 2298.0 | EN BREF　IN HET KORT | 2259.1 | +38.9 | +33.0 |
| p2-vie | 886.0 | 1090.8 | Uitleg — un vote een stemming　un  | 1127.8 | -37.0 | +41.6 |
| p2-vie | 647.0 | 947.6 | LE SAVIEZ-VOUS ? | 924.2 | +23.4 | +16.9 |
| p2-vie | 974.0 | 1308.6 | ET VOUS ?　EN JIJ? | 1304.2 | +4.4 | -1.6 |
| p3-culture | 200.0 | 405.1 | Uitleg — les vendanges de wijnoogst | 442.1 | -37.0 | +41.6 |
| p3-culture | 660.0 | 1111.6 | LES MOTS DU VIN　DE WIJN | 1074.6 | +37.0 | +30.5 |
| p3-culture | 1138.0 | 1613.6 | ZOOM　LES DATES EN CHIFFRES | 1493.6 | +120.0 | +114.0 |
| p3-culture | 1640.0 | 1969.6 | DATES À RETENIR　DATA | 1966.2 | +3.4 | -2.4 |
| p4-sport | 200.0 | 375.4 | Uitleg — un vainqueur winnaar　le | 412.4 | -37.0 | +41.6 |
| p4-sport | 621.0 | 860.4 | LES PHRASES DU COMMENTATEUR | 811.9 | +48.5 | +42.1 |
| p4-sport | 200.0 | 670.0 | LES CHIFFRES DU SPORT | 550.5 | +119.5 | +113.0 |
| p4-sport | 696.0 | 1112.0 | LES MOTS DU TENNIS　WOORDEN | 1037.0 | +75.0 | +68.5 |
| p4-sport | 1138.0 | 1356.0 | À SUIVRE　WORDT VERVOLGD | 1309.6 | +46.4 | +40.0 |
| p4-sport | 2194.0 | 2560.0 | LE DÉBAT　DEBAT | 2417.7 | +142.3 | +136.3 |
| p5-jeunesse | 2182.0 | 2387.4 | Uitleg — un prequel een prequel　u | 2424.4 | -37.0 | +41.6 |
| p5-jeunesse | 586.0 | 887.9 | REGARDER UN FILM | 841.5 | +46.4 | +40.1 |
| p5-jeunesse | 614.0 | 1083.6 | OÙ SORTIR CETTE SEMAINE | 964.1 | +119.5 | +113.0 |
| p5-jeunesse | 1110.0 | 1509.6 | MOTS DU CINÉMA　DE FILM | 1450.6 | +59.0 | +52.5 |
| p5-jeunesse | 1536.0 | 2015.6 | LE CINÉMA DU MERCREDI | 1991.6 | +24.0 | +18.0 |
| p5-jeunesse | 2042.0 | 2560.0 | LE DÉBAT　DEBAT | 2382.6 | +177.4 | +171.4 |
| p6-politique | 1071.0 | 1275.7 | Uitleg — un projet de loi wetsvoorstel | 1228.0 | +47.7 | +41.6 |
| p6-politique | 1330.0 | 1816.0 | LE CALENDRIER　BEGROTINGSKALENDER  | 1796.0 | +20.0 | +14.3 |
| p6-politique | 463.0 | 789.8 | LES PHRASES DES JOURNAUX | 826.8 | -37.0 | +42.1 |
| p6-politique | 1330.0 | 1656.7 | TROIS DATES POUR COMPRENDRE | 1693.7 | -37.0 | +42.1 |
| p7-langue | 726.0 | 938.4 | LA PHRASE EXEMPLE | 889.9 | +48.5 | +42.1 |
| p7-langue | 692.0 | 843.2 | LA PHRASE EXEMPLE | 794.6 | +48.5 | +42.1 |
| p7-langue | 794.0 | 1006.8 | LA PHRASE EXEMPLE | 958.3 | +48.5 | +42.1 |
| p7-langue | 1878.0 | 2258.0 | LE COURRIER DES LECTEURS　LEZERSBR | 2233.3 | +24.7 | +18.8 |

盒内末行基线 clearance 最小值：+3.4（P3 DATES 盒）；desc-clear 负值仅 2 处：P2 ET VOUS -1.6、P3 DATES -2.4（见 PROOF-NOTE §5 O1/O2）。

## 附表 B — 全部盒标题 PIL 真墨量测表（69 项，0 flags）

每奶油盒取顶行标题 + 盒内全部粗体行；墨边距 = PIL 真墨边到盒四边的距离（px），负值即墨越盒边。

| 页 | 盒 y 范围 | 粗体 | 标题 | L | R | T | B |
|---|---|---|---|---|---|---|---|
| p1-une | 1239.0..1444.1 | 否 | Uitleg — le Sénat de Senaat　un | 18.0 | 98.2 | 20.5 | 161.4 |
| p1-une | 1456.1..1780.2 | 是 | LES DATES　DRIE DATA | 18.0 | 146.0 | 19.8 | 286.8 |
| p1-une | 588.0..1256.0 | 是 | CETTE SEMAINE | 22.0 | 190.2 | 19.8 | 627.5 |
| p1-une | 588.0..1256.0 | 是 | JOUR PAR JOUR | 22.0 | 186.5 | 55.8 | 591.5 |
| p1-une | 588.0..1256.0 | 是 | lun. 16 | 22.0 | 330.8 | 155.0 | 495.8 |
| p1-une | 588.0..1256.0 | 是 | mar. 17 | 22.0 | 324.2 | 218.8 | 433.8 |
| p1-une | 588.0..1256.0 | 是 | mer. 18 | 22.0 | 324.5 | 280.5 | 371.8 |
| p1-une | 588.0..1256.0 | 是 | jeu. 19 | 20.8 | 332.0 | 341.0 | 305.2 |
| p1-une | 588.0..1256.0 | 是 | ven. 20 | 22.0 | 326.5 | 404.5 | 247.8 |
| p1-une | 588.0..1256.0 | 是 | sam. 21 | 22.0 | 321.0 | 466.5 | 185.8 |
| p1-une | 588.0..1256.0 | 是 | dim. 22 | 22.0 | 324.0 | 527.0 | 123.8 |
| p1-une | 1280.0..1652.0 | 是 | DANS CE NUMÉRO　INHOUD | 22.0 | 66.2 | 15.8 | 331.8 |
| p1-une | 1280.0..1652.0 | 是 | p.2 | 22.0 | 368.0 | 68.5 | 283.5 |
| p1-une | 1280.0..1652.0 | 是 | A2 | 378.0 | 22.0 | 70.8 | 288.0 |
| p1-une | 1280.0..1652.0 | 是 | p.3 | 22.0 | 368.0 | 108.5 | 243.5 |
| p1-une | 1280.0..1652.0 | 是 | A2→B1 | 337.2 | 22.0 | 110.8 | 248.0 |
| p1-une | 1280.0..1652.0 | 是 | p.4 | 22.0 | 368.0 | 148.8 | 203.5 |
| p1-une | 1280.0..1652.0 | 是 | B1 | 377.6 | 21.9 | 150.8 | 208.0 |
| p1-une | 1280.0..1652.0 | 是 | p.5 | 22.0 | 368.0 | 188.8 | 163.5 |
| p1-une | 1280.0..1652.0 | 是 | B1 | 377.6 | 21.9 | 190.8 | 168.0 |
| p1-une | 1280.0..1652.0 | 是 | p.6 | 22.0 | 368.0 | 228.5 | 123.5 |
| p1-une | 1280.0..1652.0 | 是 | B2 | 377.6 | 21.9 | 230.8 | 128.0 |
| p1-une | 1280.0..1652.0 | 是 | p.7 | 22.0 | 368.0 | 268.8 | 83.5 |
| p1-une | 1280.0..1652.0 | 是 | A2→B2 | 337.2 | 22.0 | 270.8 | 88.0 |
| p1-une | 1280.0..1652.0 | 是 | p.8 | 22.0 | 368.0 | 308.5 | 43.5 |
| p1-une | 1280.0..1652.0 | 是 | tous | 361.6 | 21.9 | 311.2 | 47.8 |
| p1-une | 1874.0..2298.0 | 是 | EN BREF　IN HET KORT | 22.0 | 127.0 | 22.0 | 383.8 |
| p1-une | 1874.0..2298.0 | 是 | MASTERS | 22.0 | 308.0 | 77.0 | 331.8 |
| p1-une | 1874.0..2298.0 | 是 | BUDGET | 22.0 | 318.5 | 184.0 | 224.7 |
| p1-une | 1874.0..2298.0 | 是 | BEAUJOLAIS | 22.0 | 278.2 | 291.1 | 117.7 |
| p2-vie | 885.7..1090.8 | 否 | Uitleg — un vote een stemming　un vin | 18.0 | 30.5 | 22.0 | 161.4 |
| p2-vie | 647.1..947.6 | 是 | LE SAVIEZ-VOUS ? | 22.0 | 193.2 | 23.2 | 258.2 |
| p2-vie | 973.6..1308.6 | 是 | ET VOUS ?　EN JIJ? | 22.0 | 172.0 | 23.2 | 292.8 |
| p3-culture | 200.0..405.1 | 否 | Uitleg — les vendanges de wijnoogst | 18.0 | 58.8 | 22.0 | 161.4 |
| p3-culture | 659.6..1111.6 | 是 | LES MOTS DU VIN　DE WIJN | 22.0 | 88.0 | 22.8 | 411.8 |
| p3-culture | 1137.6..1613.6 | 是 | ZOOM　LES DATES EN CHIFFRES | 22.0 | 37.0 | 22.8 | 435.8 |
| p3-culture | 1639.6..1969.6 | 是 | DATES À RETENIR　DATA | 22.0 | 124.0 | 16.8 | 289.8 |
| p3-culture | 1639.6..1969.6 | 是 | mer. 18 nov. | 22.0 | 284.5 | 69.8 | 245.8 |
| p3-culture | 1639.6..1969.6 | 是 | jeu. 19 nov. | 20.8 | 291.8 | 110.0 | 199.5 |
| p3-culture | 1639.6..1969.6 | 是 | ven. 20 nov. | 22.0 | 286.5 | 153.8 | 161.8 |
| p3-culture | 1639.6..1969.6 | 是 | sam. 21 nov. | 22.0 | 281.5 | 195.8 | 119.8 |
| p4-sport | 200.0..375.4 | 否 | Uitleg — un vainqueur winnaar　le | 18.0 | 73.5 | 22.0 | 131.6 |
| p4-sport | 621.3..860.4 | 是 | LES PHRASES DU COMMENTATEUR | 18.0 | 17.2 | 19.8 | 201.9 |
| p4-sport | 200.0..670.0 | 是 | LES CHIFFRES DU SPORT | 22.0 | 121.2 | 22.8 | 429.8 |
| p4-sport | 696.0..1112.0 | 是 | LES MOTS DU TENNIS　WOORDEN | 22.0 | 17.0 | 22.8 | 375.8 |
| p4-sport | 1138.0..1356.0 | 是 | À SUIVRE　WORDT VERVOLGD | 21.8 | 63.8 | 16.8 | 177.8 |
| p4-sport | 2193.7..2560.0 | 是 | LE DÉBAT　DEBAT | 22.0 | 197.8 | 16.8 | 326.3 |
| p5-jeunesse | 2182.3..2387.4 | 否 | Uitleg — un prequel een prequel　une | 18.0 | 41.2 | 22.0 | 161.4 |
| p5-jeunesse | 585.6..887.9 | 是 | REGARDER UN FILM | 16.0 | 194.5 | 17.5 | 268.1 |
| p5-jeunesse | 613.6..1083.6 | 是 | OÙ SORTIR CETTE SEMAINE | 22.0 | 91.0 | 16.8 | 429.8 |
| p5-jeunesse | 1109.6..1509.6 | 是 | MOTS DU CINÉMA　DE FILM | 22.0 | 90.8 | 16.8 | 359.8 |
| p5-jeunesse | 1535.6..2015.6 | 是 | LE CINÉMA DU MERCREDI | 22.0 | 117.0 | 16.8 | 439.8 |
| p5-jeunesse | 2041.6..2560.0 | 是 | LE DÉBAT　DEBAT | 22.0 | 197.8 | 16.8 | 478.4 |
| p6-politique | 1070.6..1275.7 | 否 | Uitleg — un projet de loi wetsvoorstel | 18.0 | 50.0 | 22.0 | 161.4 |
| p6-politique | 1330.0..1816.0 | 是 | LE CALENDRIER　BEGROTINGSKALENDER (STEMMING | 22.0 | 155.2 | 20.0 | 441.0 |
| p6-politique | 1330.0..1816.0 | 是 | 23 oct. | 22.0 | 782.0 | 96.5 | 373.8 |
| p6-politique | 1330.0..1816.0 | 是 | 4 nov. | 22.0 | 789.8 | 144.8 | 325.8 |
| p6-politique | 1330.0..1816.0 | 是 | 9–17 nov. | 22.0 | 753.5 | 192.5 | 277.8 |
| p6-politique | 1330.0..1816.0 | 是 | 18 nov. | 22.0 | 777.2 | 240.5 | 229.8 |
| p6-politique | 1330.0..1816.0 | 是 | 20 nov. | 22.0 | 777.2 | 288.5 | 181.8 |
| p6-politique | 1330.0..1816.0 | 是 | 26 nov. | 22.0 | 777.2 | 336.5 | 133.8 |
| p6-politique | 1330.0..1816.0 | 是 | 9 déc. | 22.0 | 790.2 | 380.5 | 85.8 |
| p6-politique | 463.1..789.8 | 是 | LES PHRASES DES JOURNAUX | 18.0 | 69.5 | 19.8 | 289.4 |
| p6-politique | 1330.0..1656.7 | 是 | TROIS DATES POUR COMPRENDRE | 18.0 | 21.0 | 19.8 | 289.4 |
| p7-langue | 725.8..938.4 | 是 | LA PHRASE EXEMPLE | 18.0 | 169.5 | 19.8 | 175.4 |
| p7-langue | 691.6..843.2 | 是 | LA PHRASE EXEMPLE | 18.0 | 169.5 | 19.8 | 114.3 |
| p7-langue | 794.2..1006.8 | 是 | LA PHRASE EXEMPLE | 18.0 | 169.5 | 19.8 | 175.4 |
| p7-langue | 1878.0..2258.0 | 是 | LE COURRIER DES LECTEURS　LEZERSBRIEVEN | 24.0 | 295.5 | 22.0 | 339.8 |
| p8-exercices | 1500.0..1788.0 | 是 | MODÈLE　Model | 22.0 | 663.2 | 14.8 | 249.8 |

共 69 项，flags 0；最紧：L 最小 16.0、R 最小 21.9、T 最小 17.5、B 最小 43.5。
