# W47 fr 核心版第三轮返修 · 门禁日志
- 返修 builder：叶子（第三轮返修，与 builder、第一/二轮返修 builder、第一/二/三轮校对员均不同）
- 日期：2026-11-11 EST
- 写探针 1 `git hash-object -w`：通过（0f64ae4741e8a98b916e006efffd46a4ce778464）
- 写探针 2（真实文件写至本目录 .probe）：通过
- SHA 核对（改前，与任务书逐项一致）：
  - 印刷版 La-Lucerna-VOL4.pdf：30,447,011 B，SHA-256 98c8e128a53953e063b28b98fc98e6468c3b72e42a5a9868349a9def1bd2b61c ✓
  - 网页版 La-Lucerna-VOL4-web.pdf：2,205,780 B，SHA-256 e25434430c2b2e0415adf26ef960126665c5c9434a78adf5d03f49c06717250e ✓
  - 2026-w47-fr-zh-cn.text.md：46,445 B，SHA-256 3210f6ba62df8407ffec0272fd6e5d055e6d0ac8a4de39774415287f993abe2c ✓
- D9 独立核实（动手前）：content7.py:83–84 金句/Q102 题干确为「au cinéma」；content56.py:18 P5 原文确为「dans les salles de cinéma」；旧版 P7 SVG 与 .text.md 第 903/907 行同。确认无误后动手。

## 修复（只动 D9 两处，content7.py:83–84）
- 金句 → « Mercredi 18 novembre, seize films sortent dans les salles de cinéma en France. » (page 5)
- Q102 题干 → 「Mercredi, seize films ___ (sortir) dans les salles de cinéma.」
- 键 `sortent` 不动；其余 7 条金句不动；D7/D8/D3/KIT 订正未碰；O6–O8/D4 未动。

## 改后成品
- 印刷版 La-Lucerna-VOL4.pdf：30,446,982 B，SHA-256 db3f2a71206f256b9ee0136afd8a2af663e0b3a33df8924c251a064611f135e7
- 网页版 La-Lucerna-VOL4-web.pdf：2,205,749 B，SHA-256 26593a39c258fd721e11548f0ea8f7e8eb3cd47195c3d87003481aaf5fe17823
- 2026-w47-fr-zh-cn.text.md：46,477 B，SHA-256 2b50c88d6af4c3a9907e61cb71d67d9c9e2bb8992d41fd10bec7d10ca660737e
- SVG 直接比对：P1–P6/P8 与上一轮字节相同；仅 P7 629cfe063bbd → 75237d672f20

## 返修结果（2026-11-11）
- 构建：run.py rc 0（零溢出警告，P7-phrases 1718/1830）、render.py rc 0（一次成功，8/8 卡片）、webpdf rc 0、export rc 0（150 题）。无 exit 120、无 Disk quota exceeded。
- 机械门：occlusion 0 flags；p8 extract 注记 121/150、键 150 与 final-fr-p8.json 逐项相同；compare CLEAN；check_mcq 0 缺陷 0 未定位；freeze 8/8（跑两次，--json 输出，final-fr-freeze.json 已刷新）；文字层逐字节一致（pdftotext -layout 各 103,001 B）；P8 最小 11.62pt；徽章 134 枚（50/65/19）。
- 150 题键 vs .text.md RÉPONSES：150/150 一致（自写脚本 + fix2 脚本交叉，0 不符）；Q102 键 sortent、键位不变；金句逐字 8/8。
- §1.1 逐项重测通过；8 版卡面目视通过（P7 新折行干净，其余 7 版无回归）。
- KIT 已更新（金句注、§七门禁数值、§八第 6 轮）。
- 结论：(a) 零问题（本轮返修后）。未跑 insert.py / lint --write / git push / git add / reset / stash，未提交；未碰 W43/W45/W46、其他目标语、tools。待第四轮全量复校。
