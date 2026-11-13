# GATE-LOG.md — 2026-w47-ja-pt proof2 机械门日志

- 日期：2026-11-11
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（与第一轮/fix1 同一工具链）
- 对象：`~/workspace/weekly-git/production/2026-w47/fanout-ja/2026-w47-ja-pt/`
- 全部命令均为只读；构建比对在暂存目录的副本上运行（`scratch-proof-ja-pt2/rerun/`），不触碰交付物与已发 core。

## 身份（开工核对）

| 成品 | 字节 | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-JA-PT.pdf` | 29,103,009 | `9591f16cb82a2e2534f141febc1232632ee6cf02eefa64e84e9b74cb3601b8be` |
| `Lucerna-VOL4-JA-PT-web.pdf` | 4,485,030 | `f0cdce302756b0bf118dfaa432af9dfcaf9d66b9d17056adbeb688f26258645f` |
| `2026-w47-ja-pt.text.md` | 46,696 | `53bc548ba01cd32c37f6bc68f2c9fb6503b23b523f8cf48c36300c7fa5f8d63d` |

双 PDF 各 8 页，1462.5 × 2025 pt；网页 PDF < 7 MB。

## 1. occlusion_audit — 0 flags ✓

```
tools/venv/bin/python tools/occlusion_audit.py --edition production/2026-w47/fanout-ja/2026-w47-ja-pt/svg
→ 0 flags, exit 0
```
自测：6 类 planted 对照全部触发，干净对照静默。日志：`gates/pt-occlusion.json`、`gates/pt-occlusion.log`。

## 2. p8 extract + compare — 150/150, CLEAN ✓

```
tools/venv/bin/python tools/p8.py extract --total 150 --edition <edition>
→ 150/150 noted set, exit 0
tools/venv/bin/python tools/p8.py compare --core production/2026-w47/core-ja --edition <edition> --total 150
→ CLEAN；missing=[]；extra_count=0；uncertain=[]
→ keydiff = [137, 138, 139, 140]（预期：E 组 JA→PT 译题答案）
```
日志：`gates/pt-p8.json`、`.log`、`gates/pt-p8compare.json`、`.log`。

## 3. freeze baseline — 8/8 ✓

```
tools/venv/bin/python tools/freeze.py baseline --edition <build dir>
→ baseline: 8/8 SVGs byte-identical (repointed files: none)
  OK p1-hyoushi  core 489e86b741a797df / produced 489e86b741a797df
  OK p2-kurashi  core 091960370c0c88d8 / produced 091960370c0c88d8
  OK p3-bunka    core e493bb6d9e48134e / produced e493bb6d9e48134e
  OK p4-supotsu  core 49af928533b9abee / produced 49af928533b9abee
  OK p5-wakamono core e0b9f4dfe346f84d / produced e0b9f4dfe346f84d
  OK p6-fukayomi core 0533c2c086733f6c / produced 0533c2c086733f6c
  OK p7-kotoba   core e17b9147e4c8d6ee / produced e17b9147e4c8d6ee
  OK p8-tesuto   core 93ebbe963f746309 / produced 93ebbe963f746309
  core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
→ exit 0
```
日志：`gates/freeze-baseline.log`。构建日志中无 FLOW OVERFLOW / HEAD TOO WIDE 行。

## 4. freeze diff --strict-cjk — exit 1，判定为度量口径伪影（非缺陷）

```
tools/venv/bin/python tools/freeze.py diff --core-svg core-ja/svg --edition-svg <edition>/svg --strict-cjk
→ exit 1；多重集 "added" 15 处
```
逐项溯源（`gates/freeze-diff.json`）：

| 页 | 多重集 "added" | 溯源 |
|---|---|---|
| P1 | U+3000 ×1、千秋楽 ×1、鼓 ×1 | 皆出自 core 已有字符串：`第一声鼓　千秋楽 最后一天（闭幕日）`（core P1 移除串） |
| P5 | U+3000 ×1、楽曲 ×1、中 ×1 | `会　楽曲 歌曲。`（core P5 移除串） |
| P8 | ノミネート ×5 字符、千秋楽 ×3 字符、U+3000 ×1 | ノミネート见 core P7（`ノミネート 提名`）；千秋楽见 core P1 |
| 合计 | 15 | — |

集合层面：版 CJK 字符集 498 ⊆ core 集 764，**版独有 CJK 字符 = []**。差异只因字符串重组（日语原词从词汇栏移入练习题/答案注）与 U+3000 分隔符（SOP §1.1 规定）——字符本身无一新增。第一轮的集合层面检查亦为 0 新增。

## 5. 印刷/网页文字层一致 ✓

```
pdftotext Lucerna-VOL4-JA-PT.pdf     → print.txt 46,969 B
pdftotext Lucerna-VOL4-JA-PT-web.pdf → web.txt   46,969 B
→ 两份逐字节相同
```
文件：`gates/print.txt`、`gates/web.txt`。

## 6. .text.md validator — 逐字节重现 ✓

原版导出脚本 `scratch-fanout-ja/export-textmd-pt.py`，以副本运行、输出重定向至本轮暂存（不覆盖交付物）：

```
→ wrote gates/textmd-rederived.md 46,696 bytes; 1,348 text lines
→ sha256(textmd-rederived.md) = 53bc548ba01cd32c37f6bc68f2c9fb6503b23b523f8cf48c36300c7fa5f8d63d
→ 交付 2026-w47-ja-pt.text.md 同 SHA；cmp 逐字节相同；1,375 行
```

## 7. U+2019 全扫 = 0 ✓

- 8 页 SVG 与 text.md 中 U+2019 均为 0；content*.py 中亦 0（content8.py 的 U+0027 仅为 Python f-string 语法，非渲染文本）。

## 8. VOL 核对 ✓

- 文字层：VOL.4 ×10、VOL.5 ×3、VOL.3 ×1。唯一 VOL.3 为正当的 P4 `前号（VOL.3）` 指代（W46=VOL.3）。SVG 中一处裸 "VOL." 只是 P4 `次号（VOL.` + `5）` 跨两 `<text>` 元素换行。

## 9. 徽章计数 ✓（与 core 逐页相同）

| 页 | 徽章 |
|---|---|
| P1 | A2 11 / B1 2 / B2 1 |
| P2 | A2 15 |
| P3 | A2 7 / B1 8 |
| P4 | B1 18 |
| P5 | B1 18 |
| P6 | B2 18 |
| P7 | A2 4 / B1 4 / B2 4 |
| P8 | A2 9 / B1 22 / B2 4 |

题头级别合计 **A2 48 / B1 73 / B2 29 = 150**（每页 10/18/18/18/18/18/12/38），与 KIT/登记一致。徽章元素总数 145 ≠ 150 的解释：P3 43–46 共用一枚（−3）、P8 141–144 共用一枚（−3），另 P1 有章节级徽章。

## 10. P8 最小字号 ✓

- PyMuPDF 测量：最小 **9.975 pt**（162 spans）≥ 9.75 pt 下限；次档 10.35 pt（79 spans，题干，已冻结）。

## 11. §1.1 与页脚 ✓

- 纸色 `#fbfaf6` 每页 1×；旧色 `#f7f1e2` 0×；`·` 0×；禁用色 0×；`Página N de 8` 每页 1×；刊头 font-size 196、头条 font-size 56。

## 12. F3/F4/F5 回归测量

### F3（D1，P2 首格）
- 新释义 `ancinho de bambu para bons negócios`：单行；基线 y=1752.06；词框底缘 y=1768；净空 15.94 px；实测宽 341.1 px ≤ 378.5 px 换行宽（旧释义 420.0 px → 2 行）。
- 2× 裁切目视：`gates/p2-words-crop2.png`——四格释义全部单行、在框内。

### F4（罗马字）
- 旧拼写 grep：`Fujiryūga` / `Umi-no-umi` 在 content*.py、svg/（8 页）、text.md、双 PDF 文字层中 = **0**。
- 旧形仅存：`WEEKLY-KIT.md` 8×（§11/§12 修复记录引文「改前值」，审计轨迹，不计）；`EDITION-RECORD.md` 0×。
- 新拼写 P8 SVG：`Fujiryōga` ×5、`Chura-no-umi` ×1，数目精确。
- 机制表佐证：`scratch-fanout-ja/map-pt.json`、`tm-pt.json`、`tm2-pt.json` 旧拼写 0；Fujiryōga 4×、Chura-no-umi 3×。

### F5（框标题）
- P1 `数字で見る今週　A semana em números` 21 px = 401.0 px ≤ 404.5 px；P7 `今週のフレーム　Estrutura da semana` 21 px = 381.3 px ≤ 400.5 px（23 px 时为 439.2 / 417.6 px，证实改前溢出）。
- 2× 裁切目视：`gates/p1-numbox-crop2.png`、`gates/p7-framebox-crop2.png`——两标题均在框内。

## 13. 罗马字独立核实（公开来源，本轮自查）

- **Fujiryōga**：EN Wikipedia 条目题 "Fujiryōga Masaharu"（藤凌駕 雅治）；`りょう` 为长音 ō。
- **Chura-no-umi**：日刊スポーツ 2018-05-30 记 `美ノ海（ちゅらのうみ）`；EN Wikipedia "Churanoumi Yoshihisa"（美ノ海 義久），2026 年 11 月新小结；冲绳语 *chura* = 美丽。连字符形式与本版惯例（Tori-no-ichi、Ni-no-tori）一致。

## 14. 渲染与目视记录

- `render-print/p-1.png`…`p-8.png`（印刷 PDF，110 dpi，逐页目视）、`render-web/wp8-8.png`（网页 P8 目视，与印刷版一致）及网页 P1。
- O4 重测：P2/P3/P5 `あなたは？` 框末行基线距框底 5.08–5.71 px；遮挡审计 0 flags，目视框内，与 core 同距——度量噪声，非缺陷（详见 PROOF-NOTE.md §8）。

## 15. 边界

- 只读复校：未改源码/成品；未跑 insert.py、lint --write；无 git 写操作；未碰 core-ja、其他家庭、tools/、issues/、scratch-fanout-ja/（仅读导出脚本与三份 JSON 佐证 F6）。
- `production/2026-w47/` 在 git 中为未追踪整树（既有状态），本轮未改变其状态。
