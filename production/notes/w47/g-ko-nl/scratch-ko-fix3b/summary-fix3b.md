# W47 KO core — 第三轮返修收尾记录（fix3b，2026-11-10/11）

> 收尾 builder（叶子，未再派 subagent；与 fix3 builder、第三轮校对员不同人）。
> 任务：只做 fix3 停手后剩下的 3 项收尾，不动任何源码与成品。
> **结论：3 项全部完成。** KIT 文字改写落地、run 9 freeze baseline 直接比对 8/8 通过、
> P4/P6/P7 run-9 渲染图逐版目视通过、`svg-hashes-run9.txt` 已写入。
> 未动：缺陷 1/2/4 源码、P8 题干 15.375pt、刊头 196px、头条 56px、text.md；
> 未跑 insert.py / lint --write / git push / add / reset / stash；未提交；未碰 W43/W45/W46。

## 0. 开工探针与成品核对（先于一切动手）

- 写探针（两次皆通，才动手）：`git hash-object -w`（stdin，返回 `4cf6a5bf…`，rc=0）；
  真实文件写 `scratch-ko-fix3b/work/probe.txt` 成功。前一棒遇到的 Disk quota 写失败
  本轮未复现；`df` 显示 /home 仍有 46G 可用。
- 成品核对（动手前）：印刷版 `Lucerna-VOL4.pdf` 46,232,133 字节、
  SHA-256 `48c2fa985529bbf9b1cd7afbc351285133ebb5293afa160aa797ca4c57ac1485`；
  网页版 `Lucerna-VOL4-web.pdf` 4,232,753 字节、
  SHA-256 `c030926848df2832b084e60ad392a3b07b49fe52023a29f9ce4f8170c865bf8d`；
  text.md 26,014 字节、SHA-256 `81ebd0a392266c0762df33fb73a8ce1b9bf1d8f6912891e107d74e9341e6e8c0`——
  与任务书逐项一致。另核：`print9.txt`/`web9.txt` 各 49,376 字节，`cmp` 逐字节一致。
- run-9 SVG 哈希（实测，与 `summary-fix3.md` 卷首抄录逐字核对，8/8 前缀一致）：
  见本目录 `svg-hashes-run9.txt`（完整 SHA-256，`sha256sum` 直接生成）。
  P1/P2/P3/P5/P8 与 run 8 逐字节同；P4/P6/P7 为本轮改动所致。

## 1. KIT 文字改写（`production/2026-w47/core-ko/WEEKLY-KIT.md`，只改文字）

- (a) 缺陷 3 准确表述：
  - Round 5 记录补 palette note，撤回"§1.1 palette replaced in full"的说法：
    其余色板项均已按 §1.1 替换；正文色 `#3a3631` 未引入——正文/题干用墨色 `#302c28`
   （`svglib.py:142` INK = `"#302c28"`，`text()`/`para()` 默认 fill），与 core-en
    （`svglib.py:151`）和 core-ja（`svglib.py:135`）共享实现一致，两者同样只定义
    INK = `"#302c28"`、无 `#3a3631`（我实测：core-ja `grep -c 3a3631` = 0；
    run-9 SVG 全文 `#3a3631` 0 次，`#302c28` 全文 901 处）。
    裁定为保留项，不修颜色（第三轮校对缺陷 3）。
  - fixes #9 行同步改写："§1.1 palette（all items except the body colour — 见 Round 5 palette note）"。
- (b) 修复记录：补 Round 7/8/9 三节 + fixes #12–14。
  - #12 缺陷 1 边距（MX 65→88、CW 434→422.5、RIGHT 1885→1862、头条行宽 1358→1323.5；
    连带修复 P7 照片/P6 表/P4 梯形跨栏收窄至 1323.5 与 P7 孤儿换行宽 378.5→340）。
  - #13 缺陷 2 蛾子（core-it `lucerna-moth.svg`，md5 `c22d616d8391af2caab71187097a8094`，
    我实测 ko/it 两份 md5 相同；`svglib.py` 加 `moth()`；刊头线 y=405→420、band y=424→470）。
  - #14 缺陷 4 ABSTRACT 去空格（两处日期，`grep "11 月"` = 0）。
  - Round 7（run 7，缺陷 1/2/4 修复落地，TOTAL 150，0 警告）、Round 8（run 8 自查发现
    连带跨栏 + 新孤儿）、Round 9（run 9，跨栏修复落地，最终态）。
- (c) Output files / Mechanical gates 更新到 run 9：print 46,232,133 字节 SHA `48c2fa98…`、
  web 4,232,753 字节 SHA `c0309268…`、text.md 26,014 字节 SHA `81ebd0a3…`（未变）、
  文字层 49,376 字节逐字节一致、occlusion 0、p8 150/150、check_core gloss 0 / 金句 8/8 /
  orphan 0、check_gloss 10 项（日志与 run 6 逐字节同，我直接 `cmp` 验证）、
  freeze 8/8（见 §2）、P8 字号沿用 run-8 实测 9.975pt（P8 SVG run 8→9 逐字节同）。
  「Measured exercise counts」标题改为 final build run 9（build-run9.log TOTAL 150，
  分布与 run 6 完全相同）。
- (d) Deliberately retained (c)(d) 改写为已修复现状：(c) 边距已修至 MX 88px（fix #12）、
  (d) 蛾子已加（fix #13）；(a) text.md `___` 23 处、(b) 源码注释「·」保持原裁定。
- 另两处顺带更新（防过时说法残留）：Occlusion audit 节日志指针改为 run-9；
  「Open verification debts」中"run-6 重校 pending"改为 round 3 已做（4 缺陷，runs 7–9 已处理），
  并注明 run-9 全量校对尚未做、待协调员派第四轮校对员；自查记录 round 2 条内同样过时的
  pending 句同步改写。
- 核对：改后 KIT 全文 grep，"run 6" 仅存于历史记录（Round 6、fix #10、"identical to run 6" 等），
  无残留"边距 65px / 蛾子未加"作为现状的说法。

## 2. run 9 freeze baseline（`tools/freeze.py baseline`）

- 命令：`tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/core-ko
  --core-svg production/2026-w47/core-ko/svg --out <本目录>/freeze-run9`，日志 `freeze-run9.log`。
- 工具自报 **0/8**——已知重定向局限（与 run 8 相同现象）：工具收集的 `freeze-run9/svg/`
  并非副本的新构建产物（其实测哈希与 run-8 的 produced 哈希逐项相同）。
- **直接 sha256 比对为准：`freeze-run9/build-copy/svg/` 8 个文件与在仓 SVG 逐字节相同，8/8 通过。**
  副本 SVGs 的 mtime 为 2026-11-11 00:07（UTC），确为本次运行新写；运行前后在仓 SVG
  经重哈希未变（工具 "core integrity" 行 + 我动手前后两次实测哈希一致）。
- 结论：freeze baseline 通过（直接比对 8/8）。未改用等效验证——工具本身跑通了，
  只需按任务书口径以直接比对为准。

## 3. P4/P6/P7 run-9 渲染图复看（自己从印刷版 PDF 渲染，`pdftoppm -r 100`）

渲染文件：本目录 `work/pg-4.png`、`work/pg-6.png`、`work/pg-7.png`（run-9 印刷版）。
逐版目视 + 几何数核（SVG 实测 + 源码值）：

- **P4（体育）**：梯形图「한국시리즈까지의 길」4 框，第 4 框「한국시리즈」右缘 1411
  （`bw=312、gap=25`，合计 1323，`content34.py:159` 源码值与渲染一致；框标题
  '한국시리즈' 中心 x=1255）；第 4 栏（照片 + 가을야구 달력）左缘 1439.5，
  中间有明晰空隙，图不越栏；图注行宽 1323.5，在跨度内；练习区、页脚完整，无溢出/重叠/压页脚/豆腐块。
- **P6（深读）**：对照表 `tw=[300, 512, 511.5]` 合计 1323.5（`content56.py:142`），
  右缘 1411.5；右栏两框（수능 뉴스 읽는 법 / 이번 달의 D-데이）左缘 1439.5，
  与表右缘留有空隙；表注行宽 1323.5；练习区、页脚完整，无溢出/重叠/压页脚/豆腐块。
- **P7（精讲）**：泡菜照片 `<image x="88" y="1180" width="1323.5" height="380">`，
  右缘 1411.5，第 4 栏两框「이번 주의 틀」「독자의 편지」左缘完整可见，
  「독자의 편지」标题「독」字完好、句行无遮盖；图注在跨度内；
  读者园地披露段 4 行，末行「VOL.5로 이어져요.」（12 字）——孤儿已消：
  `check_core.py` 的 SHORT-TAIL 只报末行 ≤6 字且 ≥3 音节的情形（run-7 态末行单剩
  「이어져요.」5 字即因此被报；run 9 末行 12 字不触发），run-9 check_core orphan issues 0；
  金句 8 条、下期预告 band、页脚完整，无溢出/重叠/压页脚/豆腐块。
- 其余 5 版未重看（run 8 已目视，且 P1/P2/P3/P5/P8 SVG 与 run 8 逐字节同）。

## 工具盲区记录（写明，工具 owner 待修）

- **`tools/occlusion_audit.py` 不检查 `<image>` 元素**：run-8 的 P7 泡菜照片盖住
  第 4 栏两框左缘 36.5px、盖掉「독」字，审计 0 flags 未报。这是该工具的**第二个盲区**
  （第一个是 es 版 P7 色块）。**本次 P4/P6/P7 目视已覆盖该盲区**（第 3 节）：
  照片与图/表均已逐版看图确认无遮盖；该工具只核文字与线框遮盖，不能作为图片遮盖的依据。
- 上述盲区已同时记入 KIT 的 Occlusion audit 节（"Tool blind spot (second known)"）。

## 机械门确认（run 9 最终态）

- freeze baseline：直接 sha256 比对 **8/8**（工具自报 0/8 为已知重定向局限，见 §2）。
- occlusion_audit：**0 flags**（自检 6 类全触发，干净对照静默；run-9 日志在 scratch-ko-fix3）。
- p8.py extract：**150/150**（1–150 无缺重）。
- check_core：gloss fails **0**、P7 金句 **8/8 verbatim**、orphan issues **0**、日期全对。
- check_gloss：10 项，日志与 run 6 **逐字节相同**（已裁定债务 c）。
- print/web 文字层：各 **49,376 字节，逐字节一致**。
- 构建 run 9：exit 0，0 FLOW OVERFLOW / 0 HEAD TOO WIDE，TOTAL **150**
  （A2 51 / B1 72 / B2 27；分版 10/18/18/18/18/18/12/38）。
- P4/P6/P7 目视：三版连带修复全部到位，无溢出/重叠/压页脚/豆腐块（见 §3）。

## 未做 / 遗留

- 未做：第四轮全量校对（run-9 版）尚未进行——按 SOP §8，定稿须一整轮零问题校对；
  本轮只做了 P4/P6/P7 针对性复看 + 机械门，待协调员派独立校对员。
- 沿用：第一轮 5 处归属计数（웨더아이 5 处、공단 0 处）本轮未重跑，
  与 fix3 记录一致（字符多重集 run6→run8、run8→run9 均为空差，内容未变）。
- 本目录文件：`summary-fix3b.md`（本文件）、`svg-hashes-run9.txt`、
  `freeze-run9.log` + `freeze-run9/`（build-copy 含重建 SVG）、
  `work/probe.txt`、`work/pg-4.png`、`work/pg-6.png`、`work/pg-7.png`。
- 唯一改动的生产文件：`production/2026-w47/core-ko/WEEKLY-KIT.md`（纯文字）；
  源码、SVG、PDF、text.md、ABSTRACT.txt 均未动。
