# 校对笔记（第四轮）— Lucerna Weekly 2026-W47 韩文核心版（2026-w47-ko-zh-cn，VOL.4）

> **⚠ 停手记录（任务硬性约束）：本轮开工后第一次批量机械门执行中写
> `work/occlusion.log` 遇到 `Disk quota exceeded`，按任务要求立即停手，未硬锤重试。**
> 此时 `df` 显示 /home 仍有 45G 可用（70% 已用），属配额层面的单次写失败，非磁盘写满——
> 与第三轮返修（fix3）run 9 收尾时遇到的同类故障一致（该轮同样在写 `svg-hashes-run9.txt`
> 时报 Disk quota exceeded，后由 fix3b 轮写文件未复现）。
> 停手时状态：成品哈希核对、蛾子 md5、ABSTRACT 去空格三项已核；印刷版渲染只完成 P1–P4
> （P4 为 409,600 字节截断文件，pdftoppm 在第 5 页前段错误 rc=139）；其余机械门
> （occlusion、p8、freeze、文字层比对、check_core/check_gloss、P8 字号）与全文精读、
> 150 题逐题验算、8 版目视均未执行。**本轮未完成全量校对，不能报 (a) 零问题，也不能报
> (b) 缺陷清单——结论为：未完成，需协调员在配额恢复后重派第四轮校对。**

- 校对员：独立校对（第四轮，与 builder 及第一、二、三轮校对员、返修 builder 均不同人）；只读不改；未修改 core-ko 内任何文件；未跑 insert.py / lint --write / git push/add/reset/stash；未碰 W43/W45/W46 的任何文件；未碰 core-ko 以外的 W47 目标语文件。
- 校对对象：`~/workspace/weekly-git/production/2026-w47/core-ko/`；印刷 PDF `Lucerna-VOL4.pdf`（8 页，46,232,133 字节，SHA-256 `48c2fa985529bbf9b1cd7afbc351285133ebb5293afa160aa797ca4c57ac1485`，与任务书一致）；网页 PDF `Lucerna-VOL4-web.pdf`（8 页，4,232,753 字节，SHA-256 `c030926848df2832b084e60ad392a3b07b49fe52023a29f9ce4f8170c865bf8d`，与任务书一致）；text.md（26,014 字节，SHA-256 `81ebd0a392266c0762df33fb73a8ce1b9bf1d8f6912891e107d74e9341e6e8c0`，与任务书一致）。
- 规则依据：SOP.md §8（校对闭环）、§1.1（视觉规范全文）、`~/workspace/weekly-git/AGENTS.md`；第三轮笔记 `hidden_files/w47/scratch-proof-ko3/PROOF-NOTE.md`；返修记录 `hidden_files/w47/scratch-ko-fix3/summary-fix3.md`；收尾记录 `hidden_files/w47/scratch-ko-fix3b/summary-fix3b.md`。
- 校对日期：2026-11-11（刊期 2026-11-16..22）。

## 开工探针（通过）

- 写探针：`work/probe.txt` 真实文件写成功（`probe 2026-11-11T00:37:15Z`），探针通过后才动手。
- 成品核对（动手前，逐项与任务书一致）：见上。

## 停手前已核实的三项（仅此三项，不构成全量校对结论）

1. **蛾子 md5**：ko `assets/lucerna-moth.svg` 与 core-it 同文件 md5 均为 `c22d616d8391af2caab71187097a8094`，与任务书一致。
2. **ABSTRACT.txt**：`grep -c "11 月"` = 0；全文一行，含 `11月19日`、`11月22日`（去空格已落地）。其余 ABSTRACT 内容未逐字核对。
3. **成品哈希**：print / web / text.md 三项哈希与字节数均与任务书逐项一致（见上）。

## 故障经过（时间线，UTC 2026-11-11）

1. 00:37 写探针通过；成品哈希核对通过；蛾子 md5 与 ABSTRACT 计数通过。
2. 00:37–00:38 批量执行：`pdftoppm -r 100` 渲染印刷版 8 页，至 P4 时段错误（Segmentation fault，rc=139），只产出 pg-1.png（1,411,844 字节）、pg-2.png（1,141,504 字节）、pg-3.png（1,251,736 字节）与截断的 pg-4.png（409,600 字节）；P5–P8 未渲染；网页版 P1/P8 未渲染；`pdftotext` 因上游渲染失败未产出 print.txt / web.txt（两版文字层比对未做）。
3. 同一批次内写 `work/occlusion.log` 时报 `Disk quota exceeded`（occlusion_audit 本身未跑出结果，日志文件未建成）；按任务硬约束立即停手，未重试该写操作，也未再跑任何机械门或渲染。

## 未完成清单（需重派后补做）

1. 缺陷 1 边距：8 页 `<text>` x 范围 88.0–1862.0、0 OVERFLOW、头条行宽 1323.5——未验。
2. 缺陷 2 蛾子：P1 蛾子居线中、无重叠、band 下移后错位——未目视（仅 md5 已核）；P1 渲染图 pg-1.png 已产出，可供重派校对员复用，但须其自行重渲核实。
3. 缺陷 4 ABSTRACT：`11 月` 0 次——已核（见上）。
4. 连带修复：P7 泡菜照片盖第 4 栏框、P6 对照表右缘、P4 梯形图第 4 框右缘、P7 孤儿——未验（P7/P6/P4 渲染图未产出；P4 图为截断文件，不可用）。
5. 缺陷 3 裁定：正文 #302c28、#3a3631 全版 0 次、KIT 该句准确性——未验。
6. 150 题逐题验算、全文精读、8 版目视、KIT 核查、F-MAIL 核查——未做。
7. 机械门全套：occlusion、p8 extract/compare、freeze baseline 直接 sha256 比对 8/8、print/web 文字层逐字节一致、check_core、check_gloss、P8 最小字号、§1.1 逐项——未跑。
8. P8 题干 15.375pt、text.md `___` 23 处、刊头 196px、头条 56px 按裁定不动——未复核。

## 工作文件

- 本笔记：`hidden_files/w47/scratch-proof-ko4/PROOF-NOTE.md`
- `hidden_files/w47/scratch-proof-ko4/work/`：`probe.txt`、`pg-1.png`、`pg-2.png`、`pg-3.png`、`pg-4.png`（截断，不可用）、`render.log`（0 字节）、`freeze-run9/`（空目录）。`occlusion.log`、`print.txt`、`web.txt`、网页版渲染图均未建成。
- 未修改 core-ko 内任何文件；未碰其他目标语与 W43/W45/W46。
