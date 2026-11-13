# GATE-LOG — W47 it-es proof2（独立重跑，2026-11-11）

工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-es1/`
（下称 `$S`）。全部输出落 $S；生产只读。`PYTHONDONTWRITEBYTECODE=1`，`TMPDIR=$S/tmp`。
工具栈：`tools/venv/bin/python`（Pillow 13.0.0，FreeType 2.14.3）。

## 0. 探针与 SHA（开工前）

| 检查 | 结果 |
|---|---|
| `git -C ~/workspace/weekly-git hash-object -w /dev/null` | 成功，`e69de29b…` |
| scratch 真实写文件 `$S/probe.txt` | 成功 |
| 印 PDF SHA / 大小 | `8b7547d315a50de4858d6971483f79951c2d497ef28e4f71dc66942bc405411b` / 14,033,641 B ✓ 与任务给定一致 |
| 网 PDF SHA / 大小 | `efc1404b8797a8b133fdafe911c1886a9a2be24158a2e49a4dcaeb657cdb9266` / 1,291,428 B ✓ |
| 文本 SHA / 大小 | `64a8ac2fce4e7063c7bebfcbb5b6cde2f8fe1fbde4f265a510e6abf83d007031` / 56,214 B ✓ |
| KIT §7/§11 三 SHA 与盘上一致 | PASS（`gates2.py` 第 10 门，逐字节比对） |

## 1. run.py（`$S/run.log`；副本 `$S/run-copy/`，生产未动）

- RC=0；TOTAL 150；by level A2 47 / B1 70 / B2 33；by page 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38。
- FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE 出现次数：0。
- P8 exercises flow ends col 3 y=870.1；P8-keys flow ends col 3 y=2529（bottom 2552，余量 23px）。
- **事故（已修复，内容零影响）**：本次 `run-copy` 是 `cp -a` 的裸副本，未重定向 `content*.py:6` 的字面量 `OUT`（`~/workspace/weekly-git/production/2026-w47/2026-w47-it-es/svg`），导致该次运行把 8 个交付 SVG 在原路径重写了一遍（mtime 20:19:33–20:20:07）。内容零变化：重写后 sha256 与 freeze baseline 开工前记录的 before 哈希逐字节一致；印/网 PDF 与 `.text.md` 的 SHA 仍与任务给定值一致；mtime 已用 `cp -a` 保留的原始值（12:15:21–12:15:53）复原并再次验证 SHA 不变。教训：run.py 只许经 `freeze.py baseline`（自带 repoint）或先改 OUT 再跑。详见 PROOF-NOTE §11。
- **PASS**

## 2. SVG 重建 8/8（freeze baseline，`$S/freeze/baseline.log` + `baseline.json`）

- `tools/freeze.py baseline --build <edition> --core-svg <edition>/svg --out $S/freeze`：**8/8 SVGs byte-identical**（repointed files: render.py, content12.py, content34.py, content56.py, content7.py, content8.py）； shipped SVG 在运行前后重哈希一致，未改动。
- **PASS**

## 3. 重渲印 PDF 与交付逐字节相同（`$S/rebuild_print_pdf.py`）

- scratch 副本 SVGs（与交付逐字节一致，已验）经 render.py 同款 cairosvg+pypdf 流程重建印 PDF：sha256 `8b7547d315a50de4858d6971483f79951c2d497ef28e4f71dc66942bc405411b`，14,033,641 B，与交付**逐字节相同**。
- **PASS**

## 4. freeze 核心 baseline 8/8

- 见第 2 门（同一运行即 freeze baseline）。
- **PASS**

## 5. freeze diff（`$S/freeze-diff.json` + `$S/freeze-explain.log`，`explain_freeze.py` 独立实现）

- `tools/freeze.py diff --core-svg core-it/svg --edition-svg it-es/svg`：8 页齐全；added 342 / removed 526 碎片，逐条解释：**0 未解释**（增量全为 translations.py 西语值/键、NOTE 复合、gloss + `(Pagina N)` 复合或家具；减量全为中文核心层键或核心家具）。
- `--strict-cjk`：新增 CJK 仅 8 × U+3000（页脚分隔符，SOP §1.1 豁免）；`rc=1` 系 freeze.py 对任何新增 CJK（含 U+3000）的返回值，非失败。
- **PASS**

## 6. occlusion（`$S/gates2.log`）

- `tools/occlusion_audit.py <edition>/svg`（内含合成自测，先行通过）：**0 flags**，rc=0。
- **PASS**

## 7. 奶油盒 PIL 真墨扫（`$S/creambox.log` + `$S/pixel_boxes.py`）

- canonical `hidden_files/w47/tools/creambox.py`，8 页 29 盒：无真溢出。盒内余量 ≥ +4.5px；6 处负余量皆 BELOW-WINDOW 假阳性（inside-only 余量 +16.0/+47.7/+22.0/+31.2/+90.0）。
- desc-clear 负值 4 处（末行有真实下行字母）交付 PDF 200 dpi 像素裁定：P3 E TU 盒底余量 0.84px、P5 E TU 0.84px、P7 LA PAROLA 0.96px、P7 LETTERE 1.64px；盒底下方 15 渲染 px 内暗像素均为 0。其余 5 处 desc-clear 负值末行无下行字母，属 0.30em allowance 假阳性。
- **PASS（spill 0）**

## 8. PyMuPDF 逐字页边扫描（`$S/geom_scan.log`，交付印 PDF）

- 8 页：超页边字符 0（0.5pt 容差）；0 容差下仅 P1 一字符：VENEZIA 末字母 A 超 0.08pt；300 dpi 裁切目视字形完整（`png/crop-p1-band-right.png`），advance-box 伪影，非缺陷。
- 非页脚文本跨越 1977pt 版心底边：0 处；无字符超页底。
- **PASS**

## 9. 孤儿扫（定义：答案题跨栏断裂 + 栏首续行；`geom_scan.py` 修正版 + 逐页目视）

- P8 逐栏核查：3 栏栏首皆为标题/徽章、非上题续行；栏末题 37./75./150. 均在本栏内结束；跨栏断裂题 **0**。
- 练习小节标题与首题同栏：P6/P7/P8 全部同栏；P2 D、P3 B、P4 B、P5 B 四处标题在栏底、题项在下一栏——位置模式与 core-it 相同（P2 D 逐坐标相同；P3/P4/P5 因西语行较长下移约 30px，同样位于栏底），属冻结核心版式。
- **PASS（孤儿 0）**

## 10. p8 extract 150/150（`$S/p8-extract.json`）

- `tools/p8.py extract --p8 p8-valutazione.svg --total 150`：noted=150，rc=0。
- **PASS**

## 11. p8 compare（`$S/p8-compare.json`）

- `tools/p8.py compare --core-p8 core-it/svg/p8-valutazione.svg --edition-p8 it-es/svg/p8-valutazione.svg --total 150`：verdict=**CLEAN**，**keydiff 实测 [137, 138, 139]**（预期内的重定向翻译键，任务提示值一致，系实测所得）。
- **PASS**

## 12. P8 最小字号 ≥9.75pt

- SVG：P8 font-size 最小 13.0px（= 9.75pt），恰为 SOP §1.1 下限；P1–P5/P7 最小 15.5px，P6 最小 17.0px。
- 交付印 PDF（PyMuPDF，pt）：P8 最小 **9.75pt**；P1–P5/P7 11.62pt；P6 12.75pt。网页 PDF 各页一致。
- **PASS**

## 13. §1.1 扫描（8 个 SVG 全量 grep + 渲染核对）

- 纸色 #fbfaf6 present；禁色（gold/brick/near-black 七色）0 命中；VOL.4 ×9；VOL.5 仅 3 处合法节点（`VOL.5 (pagina 7, «Lettere dei…` / `…la promesa pasa al VOL.5.` / `LA PROSSIMA SETTIMANA　LA PRÓXIMA SEMANA (VOL.5)`）；徽章色 A2 #5c6e30 / B1 #46581f / B2 #37402f 齐全；全页矩形框 0；“·”共 148 处（选项串/词汇表内，与 core 模式一致）。
- 残留语言：非拉丁字符仅 U+3000（125×，家具）、全角冒号 ：（7×，冻结的核心动词范式注释）、`<title>Lucerna 三色蛾</title>`（logo 元数据，不可见，core 亦有）。初版门曾因此 FAIL，后核实为元数据误报并修正检查（剥离 `<title>` 后 PASS）。
- **PASS**

## 14. 日期星期全验（`date`，Europe/Rome）

- 11 月 16 日周一、17 日周二、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二；12 月 2 日周三、12 月 6 日周日、12 月 31 日周四；10 月 15 日周四、10 月 28 日周三、11 月 9 日周一、11 月 12 日周四、11 月 15 日周日；11 月 6 日周五、7 日周六、8 日周日；11 月 13 日周五、14 日周六；1441-10-25 周一——与正文全部一致。
- **PASS**

## 15. 文字层：印/网一致 + web PDF < 7MB（`$S/print.txt` / `$S/web.txt`）

- `pdftotext -layout` 字符多重集一致（chars_equal=True）；印 8001 词 / 网 8001 词；印 PDF 8 页；web PDF 1,291,428 B < 7 MB；印 PDF 14,033,641 B。
- web PDF P1/P8 渲染目视与印版一致，无豆腐块（`png/web-1.png`、`web-8.png`）。
- **PASS**

## 16. text.md validate 0/0

- `validate_edition_textmd.py <edition> 2026-w47-it-es`：forward-miss 0 / reverse-miss 0，rc=0。
- **PASS**

## 17. 150 键与注释审计（vs core `.text.md`，`gates2.py` 独立实现）

- answers count：edition 150 / core 150。
- keys 1–150 与 core 一致（137–139 重定向、写作题除外）：mismatches=[]。
- notes 与 translations.py 一致（137–140 除外；冻结的意语动词范式 16–20/60–61 与算术 85–86 逐字节沿用、无 CJK）：mismatches=[]，table_gaps=[]。
- **PASS**

## 18. 标题数实测（“56 titles”核查）

- 奶油盒 `#f0eee5` 共 29 个：带标题 23 个、Nota 注释盒 5 个、P6 图表盒（标题画于盒上横条）1 个；全大写文本节点共 116 个（含刊头家具、徽章、日期标签）。
- “56”与任一可复现的计数均不对应——**幻数，非缺陷**（PROOF-NOTE §5）。
- **PASS（实测值已报）**

## 19. 其他实测（非门禁，供 PROOF-NOTE 引用）

- 范文 99 词（80–100 词题面要求内）；P7 金句 8 条各出现恰好 2×；题号 1–150 连续无缺；Nota 注释词逐页核实均出现在本页正文（词形变化计入）。
- ABSTRACT.txt：西语单行，无 ASCII 双引号，含 La Lucerna、italiano、A2–B2、150 ejercicios。
- 事实抽查（独立检索 2026-11-11）：意甲第 11 轮 10 场比分 + 积分与公开记录一致；BookCity Milano 2026（第 15 届、11 月 23–29 日、主题《Il senno sulla Luna》、开幕周一 23 日 20:00 Teatro Dal Verme、主宾 Colson Whitehead、1,360/2,487/1,164/443）经多家意媒证实。

## 汇总

| 门 | 结果 |
|---|---|
| run.py RC=0 / 150 题 / 0 溢出 | PASS |
| SVG 重建 8/8 字节一致 | PASS |
| 重渲印 PDF 与交付逐字节相同 | PASS |
| freeze 核心 baseline 8/8 | PASS |
| freeze diff（0 未解释） | PASS |
| occlusion 0 flags | PASS |
| 奶油盒 PIL 真墨扫（spill 0） | PASS |
| PyMuPDF 页边扫描（0 真溢出） | PASS |
| 孤儿扫（0 跨栏断裂） | PASS |
| p8 extract 150/150 | PASS |
| p8 compare CLEAN，keydiff [137,138,139] | PASS |
| P8 最小字号 9.75pt | PASS |
| §1.1 | PASS |
| 日期星期全验 | PASS |
| 印/网文字层一致，web < 7MB | PASS |
| text.md validate 0/0 | PASS |
| 150 键与注释审计 | PASS |
| KIT 三 SHA 与盘上一致 | PASS |
| 标题数实测（56 为幻数） | PASS（实测值已报） |

**门禁汇总：19/19 PASS，0 FAIL。结论 (a) 零缺陷，可定稿。**
