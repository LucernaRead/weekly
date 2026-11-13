# 返修第二轮自查总结 — 2026-W47 en 核心版（D9、D10）

- Builder：第二轮返修（叶子）。对象：`production/2026-w47/core-en/`（2026-w47-en-zh-cn, VOL.4）。
- 工作日志目录：`hidden_files/w47/scratch-en-fix2/`（第一轮 scratch-en 未动）。

## 源码改动（仅 2 个文件）

- `content8.py` 完形选项（键与简析未变）：
  - 114: `A. is continuing` → `A. continuing`（裸分词，无限定动词；B was continued 过去被动与仍在进行的计票冲突；键 C continues）
  - 117: `A. certify` → `A. certified`（过去时；12 月 18 日截止日在故事的 11 月现在之后；C certifies 与复数主语 states 主谓不一致；键 B will certify；与 P2 "States will certify their counts." 及 Q17 键一致）
  - 118: `B. is wearing` → `B. is wear`（be + 动词原形，错误）；`C. will wear` → `C. wearing`（裸分词，无限定动词；键 A wears）
  - 119: `B. watches` → `B. watch`（主语 she 三单，裸形错误；A watched 过去时，周五 11 月 20 日在故事的周三现在之后，P8 范文 "On Friday, we will watch…" 佐证；键 C will watch）
  - 112/113/115/116 未动，复核仍唯一（115 A meet 与单数 Congress 主谓不一致；116 B write 主谓不一致、C is wrote 形式错误）。
- `content7.py:62` 栏首说明：`在句首写 win / won / will / whether，完成下列练习。` → `用下列词填空：won / more / lost / will / published / whether / chose / win。`（8 词按题号 100–107 顺序，与填空任务一致）。
- `registry.json` 未变：重导至 scratch-en-fix2/registry.json，与第一轮 registry.json 及 core-en/registry.json 逐字节一致（键与注记均未动）。
- 未动：tools/p8.py（仅运行；其未提交改动为第一轮所有）、insert.py / lint / git 操作一概未跑；W43/W45/W46 未碰。

## 重渲

- `run.py` rc=0：TOTAL 150，MODEL words 82，FLOW OVERFLOW / HEAD TOO WIDE 0；P7-main 终 y=1613，P8 battery y=1418，P8 keys y=2548（底限 2560）。
- `render.py` rc=0：print PDF 41,407,278 字节；8 张 cards。
- text.md 重导（scratch-en-fix2/make_textmd_w47.py）：50,768 字节，498 blocks，stub registry 150 = real registry 150。
- webpdf.py：首次跑在 120s yield 边界被截（rc=120、无 WROTE 行，文件仍为旧版）——加长 yield 至 300s 重跑成功 rc=0：2,765,419 字节，47,501 文字层字节。

## 三工具

- `occlusion_audit.py`：selftest OK，0 flags。
- `p8.py extract --total 150`：noted set = 60/150（parse: joined），含 108–111 与 112–119。
- `freeze.py baseline --out scratch-en-fix2/freeze`：工具自报 0/8（已知假象：比对空 `<out>/svg` 目录，KIT §9 已记录）；直接 sha256 比对复现 SVG 与交付 SVG **8/8 一致**（p1 31aa7fb85345ea87, p2 1197d8db0b376c8d, p3 efb83ce76688554b, p4 4290f464ea92fecb, p5 cc255d287f24db27, p6 6236f2766f290dd4, p7 1677d47db03231a2, p8 a5ad8d607c21c182；P1–P6 与第一轮基线哈希完全一致，仅 P7/P8 因 D9/D10 改变）。首次 freeze 跑空日志 rc=120（与 webpdf 同类运行时截断现象），重跑正常输出 0/8 假象行，rc=1（符合工具在 0/8 时的返回值）。

## 全量自查（SOP §8.4）

- text.md 全文精读（P1–P8 正文 + 150 条答案附录）：无新问题。
- 150 题逐题复核：registry 与 text.md 附录逐项比对 0 不符；页分布 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；分级 A2 62 / B1 66 / B2 22。
- 完形 112–119 逐题唯一性复核：8/8 唯一（见上）。
- 8 卡逐版看图：无溢出、重叠、压页脚、图片缺失；页脚齐全；P7 新栏首说明两行完整呈现；P8 四题新选项与答案区键/简析完整。
- 法语标点：SVG 文本 ` :` / ` ?` / ` !` / `«` / `»` 全 0；每页弯引号开闭相等（P1 2/2、P2 1/1、P3 10/10、P4 3/3、P5 11/11、P6 2/2、P7 29/29、P8 25/25），直引号 0。
- D1–D8 回归：SVG 文本与两版 PDF 文字层中 `252`/`161` 均为 0（裸 SVG 串匹配到的 252/161 均为坐标属性值，非可见文本）；`254`×24、`162`×10、`36 more`×1、`34 more`×0。
- print/web pdftotext diff 0 行，各 47,501 字节；两版均为 8 页、1462.5 × 2025 pt；web PDF < 7 MB。
- P8 字号：SVG 最小 15.5pt；PDF 实测最小 11.62pt，均 ≥ 9.75pt 下限。
- §1.1 颜色/字体抽查：#fbfaf6/#37402f/#46581f/#f6e08e/#5c6e30 均在 SVG 中；Newsreader/UnifrakturMaguntia/Noto Sans CJK SC 均在；金/蓝色值仅见于 P1 三色蛾标志图形（P1 哈希未变）。
- ABSTRACT.txt：单行、505 字节、0 个 ASCII 双引号（未动）。
- KIT：§7/§8/§9 已更新（新 PDF 尺寸、text.md 50,768 字节、返修第二轮记录、新 p7/p8 哈希）；build-en.log 已换为本轮构建日志。

## 结论

- D9、D10 均已修复；全量自查零发现。定稿条件（SOP §8.4 一整轮全量校对零问题）已满足，待独立校对确认。
