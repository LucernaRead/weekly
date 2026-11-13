# GATE-LOG — W47 fr-en proof2（独立重跑，re-fanout #2）

工作目录：`hidden_files/w47/scratch-proof-fr-en2/`。解释器一律 `~/workspace/weekly-git/tools/venv/bin/python`
（Pillow 13.0.0 / FreeType 2.14.3）。生产目录零写入；core-fr 只读。
探针：`echo test | git hash-object -w --stdin` 在 repo 内 rc=0（`9daeafb9…`）。

## 身份核对（先于开工，磁盘实测）

| 文件 | 字节 | SHA-256 | 预期 | 结论 |
|---|---|---|---|---|
| `La-Lucerna-VOL4-fr-en.pdf` | 17,418,996 | `7210b3e23c97ef4f683bf695ecc7484bc97fda5cf522abb94fb16ce17f675414` | 同左 | 吻合 |
| `La-Lucerna-VOL4-fr-en-web.pdf` | 1,700,436 | `ca7f8ae3a76fdbb70f8af1724f92bdb6269f8bbc48b41348457e3d6ddbf551a2` | 同左 | 吻合 |
| `2026-w47-fr-en.text.md` | 46,191 | `7b658ae24f265d145455798c39f158d504b39e8034022a06b1c809c8bd7a5c4c` | 同左 | 吻合 |

## 门 1 — run.py（scratch 副本）

- 方法：版目录（除 PDF 外）rsync 至 `run-copy/`，在副本内跑 `run.py`（`run-proof2.log`）。
- 实测：rc=0；`TOTAL 150`（按版 10/15/18/18/17/18/12/42；按级 A2 53 · B1 75 · B2 22；按型：完成句子 49、单选 26、句型转换 7、词汇配对 21、阅读判断 5、图表读数 6、跟练 8、改错 4、完形填空 8、阅读理解 5、翻译 5、对话补全 5、写作 1）；`FLOW OVERFLOW` / `HEAD TOO WIDE` 0 次（grep 计数 0）。
- 重建 SVG 与现盘 8/8 字节一致：p1 `d832422e`、p2 `f200006f`、p3 `4867f169`、p4 `14690fda`、p5 `8d7d907b`、p6 `087ab1a5`、p7 `5476d2d0`、p8 `e027cc89`（前 8 位）。
- 终值（与 KIT 一致）：P6 深读 1288/1300、P6 练习 2527/2560、P8 答案流 2146/2560、P7 金句流 1778/1830。
- **PASS**

## 门 2 — freeze（标准核心比对 + 版内自比对补充）

- `tools/freeze.py baseline --build production/2026-w47/core-fr --core-svg production/2026-w47/core-fr/svg --out freeze-baseline`（`freeze-baseline.log`）：rc=0，**8/8 SVG 字节一致**（`--build` 指 core-fr 构建目录，`--core-svg` 指 core-fr 的 svg 目录；repointed files: render.py；守卫复核： shipped core SVGs unchanged by the run，8 文件重哈希一致）。
- `tools/freeze.py diff --core-svg core-fr/svg --edition-svg edition/svg --json freeze-diff.json`（`freeze-diff.log`）：rc=0；新增 CJK 字符合计 9，全部为 U+3000（P6 1、P7 1、P8 7），无新增汉字；CJK 核心→本版：P1 224→35、P2 283→30、P3 194→19、P4 236→29、P5 244→23、P6 226→25、P7 411→16、P8 1220→189。
- 版内自比对（门 1 的一部分）：scratch 重建 8/8 与现盘一致（见门 1），即确定性复现。
- **PASS**

## 门 3 — occlusion 真实审计 + p8（直读本体）

- `tools/occlusion_audit.py production/2026-w47/2026-w47-fr-en --core production/2026-w47/core-fr/svg --json occlusion-proof2.json`（`occlusion-proof2.log`，未用 `--selftest`）：rc=0；自检 OK（6 类阳性对照全部触发，干净对照静默）；**0 flags**；core 0 flags；NEW vs core 0。
- `tools/p8.py extract --p8 …/svg/p8-exercices.svg --total 150 --json p8-proof2.json`（`p8-extract.log`）：rc=0；keys 150/150，printed notes 121/150。
- `tools/p8.py compare --core-p8 core-fr/svg/p8-exercices.svg --edition-p8 …/svg/p8-exercices.svg --total 150 --json p8compare-proof2.json`（`p8-compare.log`）：rc=0；core 121 noted / edition 121 noted；**status: CLEAN**，missing=[] extra_count=0 uncertain=[] **keydiff=[150]**——直接读 `p8compare-proof2.json` 本体核实（gates.json 的 p8 extra "?" 是误读，不适用）。
- keycheck（`proof_gates2.py` 内，对 `core-fr/final-fr-p8.json`）：150 键逐项比对，**仅 Q150 不同**（写作题键为读者语言说明）。
- **PASS**

## 门 4 — 印/网文字层逐页一致、P8 最小字号、check_s11

- `proof_gates2.py` text_layer：印/网 `pdftotext -layout` 逐字节一致（105,574 B）；网 1,700,436 B < 7MB；印 17,418,996 B。
- 逐页 token 差（`txtpages/`，每页分别 `pdftotext -f N -l N` 后 token 序列比对）：P1–P8 逐页 token 差 **0**（P1 833、P2 843、P3 846、P4 982、P5 913、P6 959、P7 1026、P8 1846 tokens；逐页字节亦全等，合计 105,574 B）。
- P8 最小 PDF 字号（PyMuPDF span 实测）：**11.625pt ≥ 10pt**（简报阈值；亦 ≥ 9.75pt）。SVG 内 P8 最小 font-size 15.5（`check_s11_fr`）。
- check_s11：fr 族无 `check_s11.py`/`verify_ed.py`（全仓搜寻：仅 en 族副本，均为 en 硬编码，不可用）。本轮在自家 scratch 新写 `check_s11_fr.py`（en 原版一字未动），对 core-fr 的 §1.1 等效检查：纸色 `#fbfaf6` 每页在位；色集 core 19 = edition 19，extra/missing 皆无；徽章三色全在；VOL 计数除一处已裁定外全等（见下）；P8 cloze 空白 (109)–(116) 与对话空白 (145)–(149) 全在，选项行 `109. A. lundi` / `113. A. propose` / `116. A. écrit` 全在，`ÉCRITURE` 头在，Q120 [B2] 徽章 OK（head 在 610.5, 332.0），Q148 题干 + 键在。`check_s11_fr.log`：**ALL §1.1/P8 CHECKS PASS (fr adaptation)**。
  - 唯一初报差异已裁定：`p6-politique.svg: VOL.5 count core=0 ed=1`——核心 `expl.py:129` 的 `chart_note`「本页日程为计划安排，18 日投票结果下期跟进。」译作本版 `expl.py:128` "Planned programme only; the 18 Nov vote follows in VOL.5."，下期显化为 VOL.5，事实正确，属同一注记的译法（PROOF-NOTE O-VOL5）。
- **PASS**

## 门 5 — 150 题逐题手验（题干与键逐项适配）

- 登记表 `reg-ed.json`（由 scratch 副本导入 content12/34/56/7/8 后导出 `bslib4.REG`，150 条，字段 n/page/level/type/key/note）与核心 `final-fr-p8.json` 比对：仅 Q150 不同。
- 键 vs `.text.md` P8 答案区：150/150 一致。
- 逐题核对题干与答案（全文通读 `.text.md` 1,088 行 + 对照正文）：Q1–Q149 逐题核实，无错键、无与正文矛盾的答案（详见 PROOF-NOTE「150 题逐题手验」；含日期星期、数字、语法、翻译题配对、配对题串位检查）。
- Q148 五重核对：登记表键 `devant le`；`content8.py` 含 `"devant le"` 与 `On se retrouve ({gnums[3]})___ cinéma ?`；P8 SVG 题干 `(148)___ cinéma ?` + 答案 `148. devant le`；`p8.py extract` 键 148 = `devant le`；`.text.md` 题干 + 答案区 `148. devant le`。全版 `<text>` 中唯一的 `du cinéma` 是 P5 Méliès 图注（核心同文）。
- Q130 (989.0, 843.0) 与核心分毫不差；Q36/Q37 位置档 +59.5（en 版；x=538.5 不变），只记录不判（PROOF-NOTE O-Q130）。
- **PASS**

## 门 6 — 水平盒标题真墨检查（PIL，自写 `boxtitle_overflow.py`）

- 方法：复用 `tools/occlusion_audit.py` 的 `ink_box`（同款字体解析，含 letter-spacing）；盒标题按 `bslib4.box()` 结构识别（粗体橄榄绿文字，基线 ≈ 盒顶+37，x ≈ 盒左+18）。
- 实测：27 个盒标题，**0 越边**；右侧余量最小 1.0px（P1 `DANS CE NUMÉRO　IN THIS ISSUE`，盒右缘 1862.0，真墨右缘 1861.0；300 dpi 裁切 `crop-p1-danscenumero.png` + 像素量测：最右墨像素 svg x=1860.4，E 完整，未裁切）；左侧余量最小 16.0px；与 #1 备份同标题逐项比对，**0 回归**。
- occlusion 0 flags 与 boxtitle_rc 0 对此类是空信号——本门为独立 PIL 实测，不依赖二者。
- **PASS**（最小余量 1.0px 记为观察项 O-T1，非缺陷）

## 门 7 — 溢出横扫（creambox + 自写横扫）

- `creambox.py`（规范版，复制自 repo `hidden_files/w47/scratch-fix-es-fr1/creambox.py`，只读使用）全版扫描 33 盒（`creambox-proof2.log`）：inside-only 清除全为正，最小 +5.0（P2 ET VOUS 盒，末行 `in.`）；BELOW-WINDOW 7 条，全部为下一栏目标题假阳性（+24.0 `LE MOT DE LA SEMAINE` 1 处；+37.0 `LA SEMAINE EN CHIFFRES` / `À VOUS !　YOUR TURN` ×3 / `IL EST PRÉVU QUE + SUBJONCTIF` / `LE DÉBAT　DEBATE` 等）；P7 披露盒（y=1878，盒底 2258.0）末基线 2233.3，清除 +24.7，desc-clear +18.8。
- 自写横扫（`boxtitle_overflow.py`，绘图顺序版）：盒内横向溢出 **0**（全部 in-box 文本真墨左右缘均在所属纯填充盒内）；基线落在盒外的漏检行 **0**（绘图顺序判定：盒矩形后、下一矩形/栏目前的文本流中，基线在盒底+45 至 +120 带内且起于盒内缩进的文本为 0；初版几何判定曾误报 1528/131 行——同栏上下游文本，非盒内容——已修正定义并复核，修正过程见 `boxtitle-overflow.log` 演变与脚本注释）。
- P7 披露框 PIL 复验：末行真墨底 2237.8（距盒底 20.2px），2258–2270 间隙零墨。
- **PASS**

## 门 8 — 弯引号成对、CJK 孤儿标点、禁词/简体残留、填空/改写键合理

- 弯引号：SVG 中 U+2019=0、U+201C=0、U+201D=0；法式引号 « 74 / » 74，成对；`.text.md` 中 U+2019/U+2018/U+201C/U+201D 均为 0，« » 74/74 成对；直撇号一律 U+0027。
- CJK 孤儿标点（`check_extra2.py`，复制 fanout `check_extra.py` 并改输出路径至自家 scratch；`check_extra-proof2.log` / `extra-proof2.json`）：孤儿元素 total=0，new=0，inherited=0，remnant=0，shared_baseline=0；核心自带 "—" 元素 2 处（P4 y=623.13、P6 y=653.69）在本版因折行不同未分拆出；空白行：核心 P3 1864.7/1997.4 + P8 843.0，本版 P3 1924.1/2056.8 + P8 843.0，ok=True；Q148 全通。**EXTRA PASS**。
  - 检测器灵敏度验证（`check_extra-synth.log` / `extra-synth.json`）：向合成副本 P2 植入一个隔离基线的孤儿 `。`（y=2514.2，距邻基线 >14px），检测器判为 `new`（new=1）；植入在共享基线上的同字则正确判为 shared_baseline——旧真孤儿仍能检出，共享基线规则未把真孤儿漏掉。
- 禁词/简体残留：U+00B7=0；金色 `#b49a4a`=0；旧纸色 `#f7f1e2`=0；纸色 `#fbfaf6` ×8；`.text.md` 汉字 0 个；`<text>` 元素中 `Dont`（不含 Dhont）0 处，`NOTE NOTE` 0 处；`NOTE　NOTE` 0 处。
- 填空/改写键合理：Q15–18/Q130–134 改写键逐项核对（aller + 不定式、虚拟式、过去时），Q35–37 否定改写键逐项核对，全部合理（见 PROOF-NOTE 手验）。
- **PASS**

## 其他独立重跑门（`proof_gates2.py`，10/10，`proof_gates2.log` / `proof-gates.json`）

| 门 | 实测值 |
|---|---|
| source_freeze | content/bslib/svglib/run 与核心字节相同；render.py 仅 BASE+PDF 名不同 |
| string_freeze | 核心非 CJK 串全存活；0 核心 E 残留；0 未入账 CJK；1 条豁免（翻译 E 值） |
| text_layer | 印/网 pdftotext 逐字节一致（105,574 B）；网 1,700,436 B < 7MB |
| p8_font | P8 最小字号 11.625pt ≥ 9.75pt（亦 ≥ 简报 10pt） |
| scans | U+2019=0，U+00B7=0，gold=0，旧纸=0，#fbfaf6 ×8 |
| chips | 134 [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck | 150 键 vs core：仅 Q150 不同 |
| mcq | bodies 45，rendered lines 1481，DEFECTS 0，UNLOCATED 0 |
| widths | 31 单行串 + 4 组共行，全部在预算内 |
| band_spans | 法文标题止 1236.9，band_r1 起 1252.1，法文副标题止 837.2，band_r2 起 1467.1 |

## 字体审计 D5（只记录，不判）

- `font-family` 计数：`Noto Sans CJK SC` 692，`Newsreader` 945，`Noto Serif CJK SC` 74，`DejaVu Sans` 4，`UnifrakturMaguntia` 1（与 #1 分毫不差）。
- 印刷 PDF 嵌入字体含多份 `NotoSansCJKsc-Regular/Bold` 子集（cid）。待用户定夺 scope。

## 目视

- 印刷版 PDF 150 dpi 全 8 页（`png-print/p-1.png` … `p-8.png`）：逐版看图，零问题（详见 PROOF-NOTE）。
- 网页版 P8 100 dpi（`png-web/p-8.png`）：与印刷版同版式同内容。
- P1 盒标题 300 dpi 裁切（`crop-p1-danscenumero.png`）：`DANS CE NUMÉRO　IN THIS ISSUE` 末字母 E 完整。

## 证据文件清单（本 scratch 内）

- `PROOF-NOTE.md`、`GATE-LOG.md`（本文件）
- `run-proof2.log`、`freeze-baseline.log`、`freeze-diff.json`、`occlusion-proof2.json`、`occlusion-proof2.log`
- `p8-proof2.json`、`p8compare-proof2.json`、`p8-extract.log`、`p8-compare.log`
- `proof_gates2.log`、`proof-gates.json`、`mcq-proof2.log`、`reg-ed.json`
- `check_s11_fr.py`、`check_s11_fr.log`、`check_extra2.py`、`check_extra-proof2.log`、`extra-proof2.json`
- `check_extra-synth.log`、`extra-synth.json`（检测器灵敏度验证）
- `creambox.py`、`creambox-proof2.log`、`boxtitle_overflow.py`、`boxtitle-overflow.json`、`boxtitle-overflow.log`
- `print-proof2.txt`、`web-proof2.txt`、`txtpages/`（逐页文字层）
- `run-copy/`（scratch 重建副本）、`freeze-baseline/`（freeze 基线构建副本）
- `png-print/`（150 dpi 全 8 页）、`png-web/`（网 P1/P8 100 dpi）、`crop-p1-danscenumero.png`

## 结论

全部上列门禁 **PASS**。结论 (a) 零缺陷，可定稿。
