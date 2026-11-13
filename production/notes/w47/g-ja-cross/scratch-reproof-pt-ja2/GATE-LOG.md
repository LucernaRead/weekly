# GATE-LOG — 2026-W47 pt-ja re-proof（第 2 轮）

全部自跑。解释器一律 `~/workspace/weekly-git/tools/venv/bin/python`
（Python 3.12.3，Pillow 13.0.0，FreeType 2.14.3）。生产目录零写入
（收工 88 文件 SHA 与开工快照逐项相同，见 PROOF-NOTE §6）。
重建在 scratch 副本 `scratch-reproof-pt-ja2/rebuild/` 内完成，
run.py 绝未指向生产目录。

## 0. 先验 SHA（开工核对，与任务给定值一致）

- 印 PDF：`568eb36b19a0d285dfbb9058933659e3dd97afae0d5de535a5b47bb7906b6ea5` / 24,991,052 B
- 网 PDF：`7079b9af534836635228e9d5982210dacbecc2257438c9d1d98afbf7761c5444` / 1,680,802 B
- text.md：`90dcdcca7821049a9af8735653d7059e4a111eeaae6dfebf1ea1467941ec9830` / 37,915 B
- p1 SVG 现盘：`fc51c47e6a0bc0d26b05892896369c50aedfe1aa05d972a25cbc01bae8e2474f`（与任务所称 fix1 后值一致）
- 探针：`echo test | git hash-object -w --stdin` → `9daeafb9…` 成功；scratch 写文件成功。

## 1. run.py（scratch 副本，`run-rebuild.log`）

- exit 0；TOTAL 150；by level {A2: 48, B1: 71, B2: 31}；
  by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}；
  model words 88。FLOW OVERFLOW / HEAD TOO WIDE 0 次。
- P8-keys 流末 col 3 y=2504（底 2560）；P8-ex 流末 y=908.62。

## 2. SVG 重建比对（`svg-rebuild-compare.log`）

- p1-capa / p2-vida / p3-cultura / p4-esporte / p5-jovens /
  p6-aprofundamento / p7-lingua / p8-avaliacao：**8/8 IDENTICAL**（cmp 逐字节）。

## 3. gates.py（scratch 副本，`gates.log`）

- **16/16 PASS**，`FAILURES: none`。末行：P1 头条 41 字符 ≤56；
  P7 quotes clear of preview box，max quote-region baseline 2351.17。

## 4. freeze（`freeze/`）

- baseline（--build scratch 副本，--core-svg 副本 svg）：exit 0，
  8 行 `OK`，`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。
- diff（core-pt/svg vs pt-ja/svg）：exit 0；TOTAL added CJK **3,246**；
  分版 +27/+36/+29/+29/+44/+21/+51/+402 strings（讲解层替换，预期）。
- 非 CJK 差分（`freeze/non-cjk-diff.log`）：葡文目标语文本无一字改动；
  差异仅为家具翻译、标点转换、页脚格式与换行边界伪影（已逐项核实，
  详见 PROOF-NOTE §3.1）。

## 5. occlusion_audit.py（`occlusion.log` / `occlusion-core.log`）

- pt-ja svg：`selftest OK`（6 类全触发，干净对照静默），**0 flags**，exit 0。
- core-pt svg：同工具同跑，**0 flags**，exit 0。
  （KIT §6 所记 1 处 LINEX 擦痕属 refanout 前旧版，现版双双为 0。）

## 6. p8.py（`p8extract-*.log/.json`，`p8compare.log/.json`）

- extract（版）：noted set = **150 of 150** (parse: lines)，exit 0。
- extract（核心）：noted set = **150 of 150**，exit 0。
- compare：`status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`，exit 0。
  - Q137 版 `11月20日金曜日は全国の祝日です。` / 核心 `11 月 20 日周五是全国假日。`
  - Q138 版 `パルメイラスはPK戦で5–4で勝ちました。` / 核心 `帕尔梅拉斯在点球大战中 5 比 4 获胜。`

## 7. 印/网文字层（`print.txt` / `web.txt`）

- pdftotext -layout 各 **107,800 字节**，`cmp` 逐字节相同；8 页，1462.5×2025pt；
  网 PDF 1,680,802 B < 7 MB。

## 8. P8 最小字号（`p8-fontsize.log`，PyMuPDF，交付印 PDF）

- P8 最小 **10.125pt**（605 spans，答案区）≥ SOP §1.1 底线 9.75pt；
  其余各页最小 11.625–12.75pt。

## 9. D6 三重量测（`d6-measure.log` / `d6-pixel-measure.log` / `render-print/p1-topstrip.png`）

- 旧串 `ブラジルが読む` 全版 0 处；新串 `ブラジル人が読む`：`tables_ja.py:202` +
  `content12.py:15`（源码 2 处）+ `svg/p1-capa.svg` 1 处。
- SVG 量测：标语元 advance 右缘 **1216.4**（middle 锚 x=663.9）。
- 交付印 PDF 渲染像素（150 dpi，scale 1.5626）：标语墨迹 664.3–**1285.7**，
  中心 975.0；日期行墨迹左缘 **1460.4**；墨迹间隙 **174.7px**。
  （声称 1285 / 1461 / 176px，三项均在 ±1.3px 内吻合。）
- 顶栏裁图目视：居中、无接触、无裁切。

## 10. 其他自测量（`d1-d5-spot.log` / `d4-measure.log` / `misc-checks.log`）

- D1：`Ter 17 — Singapura × Brasil, às 7h`（P1/P3 SVG、text.md）；`7h15` 全版 0 处。
- D5：SVG `土曜日16:30、パルメイラス` / text.md L118 `土曜日16:30` / 核心 `周六 16:30` 三方一致。
- D4：P1 表头墨迹右缘距数字框右缘 **60.5px**（框 x=989 y=786.18 w=422.5 h=434）；
  P6 表头墨迹 88.0–1066.0，距页右缘 796px。
- 范文程序计数 **88 词**。VOL.4 ×9、VOL.5 ×3、VOL.3 ×2（皆在 P7 披露中），与核心相同。
  徽章逐页计数 8 版与核心完全相同。U+2019 0、U+0027 0；简繁中文专属字 0（`会` 1 处为「試験会場」）。
- 日期/星期：`date -d` 核验 11 月 16 日周一～22 日周日、23 日周一、27 日周五、12 月 1 日周二、12 月 6 日周日；
  P6 图表独立验算 16–30 日 = 15 天 = 10 工作日 + 5 休息日，第 10 个工作日窗口 27–30 日。

## 11. 渲染证据

- 印 PDF：`render-print/p-1.png`～`p-8.png`（100 dpi）+ `render-print/p1-topstrip.png`（顶栏裁图）。
- 网 PDF：`render-web/wp1-1.png`、`render-web/wp8-8.png`（100 dpi，与印版一致，无豆腐块）。

## 12. 收工零写入

- `snapshot-end.sha256` vs `snapshot-start.sha256`：88 文件 SHA 全部相同（diff 空）。
