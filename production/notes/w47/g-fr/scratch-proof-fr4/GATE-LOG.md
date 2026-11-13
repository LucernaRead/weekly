# W47 fr 核心版第四轮独立复校 · 门禁日志
- 校对员：叶子（第四轮，与 builder、各轮返修 builder、第一至三轮校对员均不同）
- 日期：2026-11-11 EST
- 写探针 1 `git hash-object -w`：通过（da0c4eb8d9a48d171a33574b380752e183286751）
- 写探针 2（真实文件写至本目录 .probe）：通过
- SHA 核对（与任务书逐项一致）：
  - 印刷版 La-Lucerna-VOL4.pdf：30,446,982 B，SHA-256 db3f2a71206f256b9ee0136afd8a2af663e0b3a33df8924c251a064611f135e7 ✓
  - 网页版 La-Lucerna-VOL4-web.pdf：2,205,749 B，SHA-256 26593a39c258fd721e11548f0ea8f7e8eb3cd47195c3d87003481aaf5fe17823 ✓
  - 2026-w47-fr-zh-cn.text.md：46,477 B，SHA-256 2b50c88d6af4c3a9907e61cb71d67d9c9e2bb8992d41fd10bec7d10ca660737e ✓

## 复校结果（2026-11-11）
- D9：P7 金句第 6 句与 Q102 题干均已改回 P5 原文「dans les salles de cinéma」；键 sortent 不动；金句逐条实测 **8/8 VERBATIM**（均在所注页码内）；仅 p7 SVG 变化，其余 7 页 SHA 与 fix2 基线逐字节相同。
- D7：几何分类法 4/4 PASS；D3：13/13 PASS；D8：gp4/n_gp4 已为 se terminer en beauté，P7/P8 lieu 0 处，Q100 键 beauté 不动。
- KIT：标题 32px=24pt（font-size="38" 全刊 0 处；「28.5pt」仅存于两处历史说明）、F-MAIL 表述（不查邮箱、不核实邮箱状态）均已改。
- 机械门：occlusion 0 flags（自检 OK）；p8 extract 注记 121/150、键 150 与 final-fr-p8.json 内容逐项相同；compare CLEAN；check_mcq 0 缺陷 0 未定位；freeze **8/8**（tools/venv/bin/python，构建解释器，Pillow 13.0.0）；文字层逐字节一致（各 103,001 B）；P8 最小 11.62pt；徽章 134 枚（50/65/19），折算分级 A2 53/B1 75/B2 22。
- 150 题键 vs .text.md RÉPONSES：150/150 一致；逐题验算全对；范文 96 词；日期/星期 `date -d` 全验。
- §1.1 逐项重测通过；禁词扫描（内部流程词/红线政治词/周次标记/「·」）全部 0 处；VOL.5 9 处均为合法下期指称。
- 8 版卡面目视（全新渲染）+ 网页 P1/P8 通过；P6 讨论注记低分辨率下的疑似孤行「。」经放大裁图证实为误读（「。」与「（已定）」同行）。
- 结论：(a) 零问题 —— 本轮全量复校未发现缺陷。是否定稿由协调员定。
- 本轮只读不改，未跑 insert.py / lint --write / git push / git add / reset / stash，未提交。tools/ 与 issues/2026-w43/ 的工作树修改均为开工前已有状态（mtime 早于本轮开工），非本轮所改；freeze 复核确认 8 个交付 SVG 未被本轮改动。
