# GATE-LOG — 2026-w47-ja-en 第二轮独立复校（叶子）

- 版：`2026-w47-ja-en`，VOL.4
- 日期：2026-11-11（UTC 07:47 起）
- 解释器：一律 `~/workspace/weekly-git/tools/venv/bin/python`（与构建相同）

## 身份复核（开工 + 收工两次）

| 文件 | 字节 | SHA-256 | 与 KIT §8 登记 |
|---|---|---|---|
| `Lucerna-VOL4-JA-EN.pdf`（印刷） | 27,440,481 | `38b0d3ab8db70ce62f491f9f608c05b79125ae336349d26b423ad68bec4bb965` | 一致 |
| `Lucerna-VOL4-JA-EN-web.pdf`（网页） | 4,428,575（< 7 MB） | `95cf9e66f51aa4d01c0f346ac8e052516136657814c9c2aab6ac1dba7d71204b` | 一致 |

两份 PDF 均为 8 页；收工复核 SHA 与开工一致，复校全程未被改动。

## 机械门（全部自跑）

1. **run.py 重跑**：`tools/venv/bin/python run.py` exit 0，
   FLOW OVERFLOW / HEAD TOO WIDE 0 次（`build-en-run13.log`）。
   REGISTRY STATS：150 题；A2 48 / B1 73 / B2 29；
   分版 10/18/18/18/18/18/12/38；
   题型 fill-in 50 / multiple choice 51 / matching 12 /
   sentence building 8 / true/false 11 / cloze 13 / translation 4 /
   writing 1；范文 154 字——与 KIT §1 一致。
2. **Freeze**：重跑前后 8 个 SVG sha256 直接比对 8/8 字节一致
   （`en-sha-before.txt` vs `en-sha-run13.txt`，diff 空）。
3. **Occlusion 审计**：`tools/occlusion_audit.py <svg dir>` 0 flags，
   自检 OK（6 类 planted 全部触发，clean 对照静默）
   （`en-occlusion-run2.json`）。
4. **P8 extract**：`tools/p8.py extract --total 150` noted set 150/150
   （`en-p8-run2.json`）。
5. **P8 compare**：`tools/p8.py compare` vs core-ja P8 SVG——
   status CLEAN，missing=[] extra_count=0 uncertain=[],
   keydiff 恰为 [137, 138, 139, 140]（`en-p8compare-run2.json`）。
   4 条 keydiff 逐条核实为 E 组翻译答案 JA→EN（见 PROOF-NOTE §7）。
6. **Print/web 文字层一致**：pdftotext -layout 双版各 99,988 字节，
   `cmp` 逐字节一致；pdftotext 字节 > 0。
7. **U+2019 全扫**：8 个 SVG 总数 0（U+2018 亦 0）；
   印刷/网页 PDF 文字层 U+2019/U+2018 均为 0。
8. **P8 最小字号**：PyMuPDF 实测印刷 PDF p.8 最小 9.975pt
   （165 spans；次小 10.35pt，79 spans）≥ 9.75pt ✓。

## 补充自跑核查

- D1/D2 回归 grep：`Fujiryūga` / `Umi-no-umi` 在 .py / 8 SVG /
  `.text.md` 中均为 0×；`Fujiryōga` ×5、`Churanōmi` ×1，位置与
  FIX-LOG 清单一致（每处 ×3 文件）。
- 题号连续性：`.text.md` 解析，1–150 无缺重；徽章 141 枚
  （A2 45 / B1 70 / B2 26）。
- 金句 8 条逐字比对正文通过；VOL.4 P1×3 + P2–P8 各×1；
  VOL.3 ×1（P4）、VOL.5 ×4（P4×1 + P7×3），均为冻结正文。
- §1.1 grep 审计：纸色 `#fbfaf6` 每版 1 次，旧色 `#f7f1e2` 0 次，
  金色 0 次，`·` 8 版 0 次；刊头 196px；`Page N of 8` 每版 1 次。
- P8-keys 末行 SVG 实测基线 y=2530.5（key 76 y=2530.476、
  key 114 y=2530.348；底边 2540，余 9.5px；页脚分隔线 2596，净空）。
- 日期星期核对（`date -d`）：11/5 木、11/7 土、11/8 日、11/16 月、
  11/19 木、11/22 日、11/23 月、12/1 火，全部正确。
- 目视：印刷 P1–P8（自渲染 100 dpi）+ 网页 P1/P8 逐版目视，
  无溢出、重叠、压页脚问题（`pages/` 下 10 张 PNG）。
- 源码 diff：core-ja vs fan-out 7 模块，含 CJK 的新增行 170 行逐行审读，
  无中文讲解残留。

## 结果

机械门 8/8 绿；补充核查全部通过；缺陷 0 条。
