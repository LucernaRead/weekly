# GATE-LOG — 2026-W47 ja-es 第一轮返修（D1 修补）机械门全记录

- 返修者：叶子（第一轮返修 builder）
- 日期：2026-11-11（UTC 约 07:00–08:00）
- 构建解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3）
- 记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ja-es-fix1/`
  （本目录内文件：`.probe`、FIX-LOG.md、GATE-LOG.md、build-fix1-runA.log、build-fix1-runB.log、
  render-fix1-runA.log、webpdf-fix1.log、pre-sha.txt、post-sha.txt、sha-runA.txt、sha-runB.txt、
  es-occlusion-fix1.json、occlusion-selftest.log、occlusion-fix1.log、es-p8-fix1.json、
  p8extract-fix1.log、es-p8compare-fix1.json、p8compare-fix1.log、print.txt、web.txt、
  extract_textmd.py、svg-text-extract.txt、textmd-content.txt、textmd-diff.txt（空）、
  p8-notes-old.txt、p8-notes-new.txt）

## 1. 构建（run.py / render.py / webpdf.py）

| 步骤 | 命令 | 结果 |
|---|---|---|
| run A | `tools/venv/bin/python run.py` | rc 0；FLOW OVERFLOW 0；HEAD TOO WIDE 0；TOTAL 150；A2 48 / B1 73 / B2 29；分版 10/18/18/18/18/18/12/38；题型 completa 50 / opción múltiple 51 / relacionar 12 / construye una frase 8 / verdadero o falso 11 / cloze 13 / Traduce 4 / Redacción 1；范文 154 字 |
| render A | `tools/venv/bin/python render.py` | rc 0；8 张 cards PNG + 印刷 PDF（29,102,102 B） |
| webpdf | `tools/venv/bin/python tools/webpdf.py svg Lucerna-VOL4-JA-ES-web.pdf` | rc 0；4,482,721 B；47,036 text bytes |
| run B（freeze 对照） | `tools/venv/bin/python run.py` | rc 0；FLOW OVERFLOW 0；registry 与 run A 完全一致 |

## 2. Freeze（SVG sha256，两轮构建）

- runA vs runB：**8/8 字节相同**（`sha-runA.txt` vs `sha-runB.txt`，diff 空）。
- 与改前（`pre-sha.txt`）比：**仅 `svg/p8-tesuto.svg` 变化**
  （`cb2813a7601a5bb7cc6f929790e3c45dd194880a780d0125c2466692685cd382` →
  `25b9510870ed54859776dd2e26ce2ebe97ef0627dd9aff208b31c93d3a03834d`）；
  p1–p7 七个 SVG 与改前逐字节相同。

## 3. 几何遮挡审计（tools/occlusion_audit.py）

- 自检：rc 0，`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`
- 实跑：rc 0，`…/svg: 0 flags`（`es-occlusion-fix1.json`）

## 4. P8 门（tools/p8.py，vs core-ja P8）

- extract `--p8 svg/p8-tesuto.svg --total 150`：rc 0，noted set **150/150**（`es-p8-fix1.json`）
- compare `--core-p8 …/core-ja/svg/p8-tesuto.svg --edition-p8 … --total 150`：rc 0，
  `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]`
  （`es-p8compare-fix1.json`；与改前 keydiff 完全一致）

## 5. 文字层（pdftotext）

- 印刷 PDF：47,036 B；网页 PDF：47,036 B；`cmp` **逐字节相同**（`print.txt` / `web.txt`）。
- 双 PDF 均为 8 页；网页 PDF 4,482,721 B < 7 MB。
- （改前 47,034 B；+2 B 恰为 `Umi`→`Chura` 的 +2 字符，`Fujiryūga`→`Fujiryōga` 等长。）

## 6. P8 字号（PyMuPDF，印刷 PDF 第 8 页）

- 最小字号 **9.975pt**（164 个 span，答案行）≥ 9.75pt；次档 **10.35pt**（79 个 span，题干）——与改前一致，未变。

## 7. U+2019 全扫

- `svg/*.svg`、`2026-w47-ja-es.text.md`、`content*.py`、`run.py`、`render.py`、`bslib4.py`、`svglib.py`：
  全部 **0**。

## 8. §1.1 grep 审计（新 SVG，文本节点）

- 纸色 `#fbfaf6`：1×/页，共 8×；旧纸 `#f7f1e2`：0×；`·`：0×；
  `VOL.4`：P1 3×、其余各页 1×；页码行 `Página N de 8`：1×/页；刊头 196px：P1。

## 9. 150 键逐题复核（O8 人工补查）

- 基准：复校员改前副本 `hidden_files/w47/scratch-proof-ja-es1/rebuild/` 内
  `2026-w47-ja-es.text.md` 与 `svg/p8-tesuto.svg`（p8 hash cb2813a7… 与改前一致，已验）。
- 新旧 P8 注文逐行 diff（text.md P8 段与 SVG 文本节点，双通道）：**仅 6 行不同**，
  即 D1 的 keys 48/49/54/63/111/116；其余 144 条注文逐字相同。
- 键值：p8 compare 已证未变（keydiff 仍 [137, 138, 139, 140]）；E 组 137–140 翻译键与改前一致。
- P8 全部注文人名人工逐条核对：Ōnosato、Hōshōryū、Yoshinofuji、Chura-no-umi、Fujiryōga、
  Miura Riku、Kihara Ryuichi、Miyajima、Shōsetsu、ryuuryuu、Chiikawa
  及 Tori-no-ichi / Ni-no-tori / Ichi-no-tori / Asakusa / Arashiyama / Kioto /
  Monte Takao / Weathernews / Beaujolais Nouveau / Hanshin Umeda —— 全部正确。
- text.md 与新 SVG：逐行比对 1349/1349 完全一致（`textmd-diff.txt` 空）。

## 10. 8 版目视

- P1–P8 逐版看图（cards PNG 缩略图 + P8 全版 1300px + P8 答案区第 1/3 栏高清裁图）：
  无溢出、无重叠、无压页脚；P8 三栏答案流齐整，6 处修正行均在流内、字形完整；
  P7 金句页码引用均为单括号 `(pág. N)`，`((pág.` 0×（F3 回归通过）；
  P6 中栏留白为核心继承版式（复校 O7），非本次引入。
- P1–P7 的 SVG 与改前逐字节相同，目视结果与第一轮复校一致。

## 11. 新双 PDF（最终）

| 文件 | 字节 | SHA-256 | 页数 |
|---|---|---|---|
| `Lucerna-VOL4-JA-ES.pdf` | 29,102,102 | `9947b70c00a378c912ad7cffd198fd19a234ca3d6a3598589f647c3eaff0fce7` | 8 |
| `Lucerna-VOL4-JA-ES-web.pdf` | 4,482,721 | `49665374de81dd2a2ee7dad1b91396b22b69b2e64f5a038d55f03b5246a99550` | 8 |

## 12. 未达门 / 遗留

- 无。本轮全部机械门绿灯；第二轮全量复校待协调员另派。
