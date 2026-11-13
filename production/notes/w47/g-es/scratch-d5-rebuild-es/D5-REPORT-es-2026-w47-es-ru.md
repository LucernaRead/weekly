# D5 重建报告 — 2026-w47-es-ru

日期：2026-11-12（UTC ~08:27–09:00）。构建解释器全程 `tools/venv/bin/python`。

## 安装
- `mechanism/apply_variant.py --svglib <版>/svglib.py --target es --reader ru`（mode ru）。
- `svglib.py` md5 `6a46ee51…` → `74f3fb03…`（安装器同时补 port 了 fix2）；修前基线：印 3,593,735 B `68a76168…`、网 941,912 B `d6d15667…`；D5 普查 587 violations；boxtitle 0 DEFECT；occlusion 0。
- 路由断言说明：`route_assert.py` 3 FAIL 是脚本局限（其前三项检查无条件要求拉丁/数字 sans → `news`，与其自身的 ru 模式检查矛盾），非真实缺陷。实际路由已核实：`_D5_READER='ru'`，拉丁/西里尔/数字 sans → `sans_noto`，U+201C/U+2019 → `news`，CJK → `sans`，serif → `news`；机制 `test_d5_routing.py` FAILURES: 0；普查 Noto Sans 元素 768 个（ru 路径确实触发）。另注：本版无弯引号（curly_total=0）。

## 预修（与 core-es 相同的 3 项共用版式）
P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt；P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt；P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。

## 逐项修（D5 新缺陷，修前基线 0）
- P1 正文行 `Пять главных тем　Para entender la semana` 右超 +16.1px（boxtitle BODY DEFECT 与 creambox DEFECT 一致确认）→ 19→18pt。
- P7 页脚：俄语编者注 `ldcn`（content7.py）在 Noto Sans 下由 4 行变 5 行（+27px），把底部 `LA PRÓXIMA SEMANA` 通栏顶进页脚（occlusion FOOTER+LINEX 同源，墨底 2601.8 超页脚线 2596）→ `ldcn` 19→18pt（`lh` 高度公式与绘制两处同改），通栏回到基线位置。18pt 下最长行 362.8px，余量 15.7px。
- P8 TEXTX：图注 credit `Pluma de cisne — dominio público (Wikimedia Commons)`（content8.py）在 Noto Sans 下 416.2→426.0px，超栏宽 422.5 折成两行，第二行 `Commons)` 与 y=1337 的 RESPUESTAS 标题行相撞（79.2×9.4px）→ `bslib4.caption()` 增加可选参数 `csize`（默认 15.5），P8 此处调用传 `csize=14.5`（398.5px，恢复一行）。以上文字均未动。
- 另：中途一次重建因 content8.py 编辑多出一个反斜杠致 SyntaxError（run rc=1），已修掉并完整重建；该轮混合产物已作废，不计入交付。

## 门禁（最终版全绿）
- run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0；head_check PASS 0 defects；render rc=0。
- D5 普查 0（D5 0/0，curly_in_cjk 0，curly_total=0）；U+201C 普查（`census_quotes.py`）0。
- occlusion 0 flags；p8 extract 150/150；p8 compare vs 新 core-es CLEAN，keydiff=[137, 138]（仅读者语译注）。
- boxtitle 0 DEFECT（body 行 382→381）；creambox（tools 版）PASS 0 defects（P8 250 行、余量 36.4px 不变；ratios n=414 median 1.007, boldT 0.956, boldF 1.03）。
- spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es 新增 CJK 字符 0（新增拉丁串 133 条为读者语翻译，属 fan-out 预期）。
- 印/网文字层 44,167 字符、8,076 词，逐字一致。

## 交付
- 印刷版 `La-Lucerna-VOL4-es-ru.pdf` 3,213,677 B，SHA-256 `707b82670349ab43cc2923388335063001864320ee7b34b002114c12fa273619`。
- 网页版 `La-Lucerna-VOL4-es-ru-web.pdf` 1,062,147 B，SHA-256 `a0889431bde27466d78a63ba7ec67bc6c0ac299063de3f5ff03d22f246f692c8`。
- `text.md` 字节不变（SHA `05e7d6c9…`）。
- KIT 已更新（§8 交付行 + 尾部 D5 记录）。日志在本目录；freeze build-copy 已删。
