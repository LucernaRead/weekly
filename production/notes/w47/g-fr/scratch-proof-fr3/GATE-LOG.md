# W47 fr 核心版第三轮独立校对 · 门禁日志
- 校对员：叶子（第三轮，与 builder、第一/二轮返修 builder、第一/二轮校对员均不同）
- 日期：2026-11-11 EST
- 写探针 1 `git hash-object -w`：通过（5478d39ecc8e76a0ccbfbc1756889af2eb1b27d0）
- 写探针 2（真实文件写至本目录 .probe）：通过
- SHA 核对（与任务书逐项一致）：
  - 印刷版 La-Lucerna-VOL4.pdf：30,447,011 B，SHA-256 98c8e128a53953e063b28b98fc98e6468c3b72e42a5a9868349a9def1bd2b61c ✓
  - 网页版 La-Lucerna-VOL4-web.pdf：2,205,780 B，SHA-256 e25434430c2b2e0415adf26ef960126665c5c9434a78adf5d03f49c06717250e ✓
  - 2026-w47-fr-zh-cn.text.md：46,445 B，SHA-256 3210f6ba62df8407ffec0272fd6e5d055e6d0ac8a4de39774415287f993abe2c ✓

## 复校结果（2026-11-11）
- D7：几何分类法（逐 <text> 元素、浅底框剔除）4/4 PASS；D3：13/13 PASS；D8：gp4/n_gp4 已为 se terminer en beauté，P7/P8 lieu 0 处，Q100 键 beauté 不动。
- KIT：标题 32px=24pt（font-size="38" 全刊 0 处）、F-MAIL 表述（不查邮箱、不核实邮箱状态）均已改。
- 机械门：occlusion 0 flags；p8 extract 注记 121/150、键 150 与 final-fr-p8.json 逐项相同；compare CLEAN；check_mcq 0 缺陷 0 未定位；freeze 8/8（哈希与 fix2 逐项相同）；文字层逐字节一致（46,695 B）；P8 最小 11.62pt；徽章 134 枚（50/65/19）。
- 150 题键 vs .text.md RÉPONSES：150/150 一致；逐题验算全对；范文 96 词。
- §1.1 逐项重测通过；8 版卡面目视通过。
- 结论：(b) 缺陷清单 —— 新缺陷 1 条 D9（轻微）：P7 金句第 6 句「seize films sortent au cinéma en France」非逐字引用，P5 原文为「dans les salles de cinéma」；Q102 题干同步。金句 8/8 逐字之说实为 7/8。修法：两处改回 P5 原文措辞，键 sortent 不动；改后重渲染并从头再做一轮全量校对。
- 本轮只读不改，未跑 insert.py / lint --write / git push / git add / reset / stash，未提交。
