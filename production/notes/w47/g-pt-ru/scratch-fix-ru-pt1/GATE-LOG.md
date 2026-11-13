# GATE-LOG — 2026-W47 ru-pt fix1（自验门禁，全部实跑）

- 版：`production/2026-w47/2026-w47-ru-pt/`；scratch：
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ru-pt1/`
- 工具 venv：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0，freeze 日志实测）。
- 判定口径：光栅 = 印 PDF 经 PyMuPDF 以 1950px 宽渲染后的像素扫描（与 proof1 同法；
  对照实验 V0 复现 proof1 数值 D1 1886 / D2 1865，方法已校准）。
- 各门日志文件均在本 scratch 内（`logs/` 或根目录），文件名见各节。

## §0 身份核对

- 开工三 SHA 与任务一致（印 `59f01012…` / 21,205,597 B；网 `485a27b6…` / 3,383,529 B；
  文 `54d8a766…` / 65,155 B），磁盘实测，见 FIX-LOG §0。

## §1 occlusion 真实审计（无 --selftest 标志）

- 命令：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-ru-pt/svg --json logs/occlusion.json`
- 结果：**42 flags，全部 TEXTX；COVER 0 / LINEX 0 / FOOTER 0 / EDGE 0 / BOXTITLE 0** → **CLEAR**。
  （工具内置阳性对照自检先行通过，见 `logs/occlusion.log` 首行；rc=1 仅表示有 flag，
  与 proof1 同形态。）
- 与 proof1 的 42 TEXTX 逐条比对（`logs/occlusion.json` vs proof1 同名）：
  页/文本/框体一致；仅 `by: text@N` 元素编号整体后移（中间重建改写 P1–P6 元素数所致）
  及 P6 一处 TEXTX 包围盒收窄（`?　DADOS DE PRÁTICA`，同类假阳性）。无新增缺陷类，
  关键类 BOXTITLE 为 0（D1 框标题类已清）。
- 判定：CLEAR，与 proof1 结论一致（相邻 run 包围盒假阳性）。

## §2 横向溢出三法交叉验证（修后，交付印 PDF 为准）

| 缺陷 | 光栅（MuPDF 1950px） | PIL 真墨（SVG 元素） | PDF span advance | 要求 | 判定 |
|---|---|---|---|---|---|
| D1 P1 标题 | **1844（+18）** | 1842.5（+19.5） | 1844.4（+17.6） | 离 1862 ≥ +5 | 通过 |
| D2 P1 桥接行 | **1855（+7）** | 1849.5（+12.5） | 1857.0（+5.0） | 离 1862 ≥ +5 | 通过 |
| D3 P2 | **1854（+8）** | 1850.3（+11.7） | 1856.3（+5.7） | 离 1862 ≥ +5 | 通过 |
| D3 P3 | **1854（+8）** | 1850.3（+11.7） | 1856.3（+5.7） | 离 1862 ≥ +5 | 通过 |
| D3 P4 | **1854（+8）** | 1850.3（+11.7） | 1856.3（+5.7） | 离 1862 ≥ +5 | 通过 |
| D3 P5 | **1854（+8）** | 1850.3（+11.7） | 1856.3（+5.7） | 离 1862 ≥ +5 | 通过 |
| D3 P6 | **1854（+8）** | 1850.3（+11.7） | 1856.3（+5.7） | 离 1862 ≥ +5 | 通过 |

- 三法一致通过；网 PDF 的 D1/D3 span 与印版相同（D1 1846.2；D3 尾段 1856.3 ×5 页）。
- 全局光栅扫描（逐页全部行，墨 x>1862）：P1–P7 **0 组**；P8 仅 1 组（行 1293–1299，
  最大 1863）——即 D5（只记录、不修，FIX-LOG §4）。D4（P2）已无。
- 证据裁图（印 PDF 光栅裁切）：`crop-p1-palavra-fix1.png`（D1）、
  `crop-p1-bridge-fix1.png`（D2）、`crop-p2-note-fix1.png`（D3 P2 代表页）；三图已目检，
  行尾距右缘留白清晰，无截断、无碰撞。
- 实验记录：`exp.py` + `exp.log`/`exp2.log`/`exp3.log`（V0 对照复现 1886/1865；
  V1 缩短 −51px 仅 1865→1864；V2 锚点 −10px 得 1855；V3 D1 新标题得 1844）。
  候选串量测：`measure.py`。

## §3 run.py（`run.log`）

- rc=0，**TOTAL 150**（A2 50 / B1 76 / B2 24；按页 10+18+18+18+18+18+12+38；
  按类型 Completar 54、Escolha 55、Associação 20、Construção 12、Transformação 4、
  Tradução 4、Escrita 1）。grep `run.log`：无 FLOW OVERFLOW、无 HEAD TOO WIDE、无报错。
- `check_core.py .`（`check_core.log`）：rc=0，golden BAD 0，gloss fails 0；
  1 orphan line-start（P7 y553）与 1 same-baseline collision（P1 y1712），与 KIT 一致。

## §4 freeze

- baseline（`logs/freeze-baseline.log/.json`）：
  `tools/freeze.py baseline --build production/2026-w47/core-ru --core-svg production/2026-w47/core-ru/svg --out <scratch>/freeze-base`，
  rc=0，**8/8 SVG 字节一致**，核心完整性重哈希 OK（core 未被改动）。
- diff（`logs/freeze-diff.log/.json`）：
  `tools/freeze.py diff --core-svg production/2026-w47/core-ru/svg --edition-svg production/2026-w47/2026-w47-ru-pt/svg`，
  rc=0；新增 CJK 仅 U+3000，8 页各 ×1，TOTAL 8（proof1 时为 6；P7 的 +1 来自核心侧
  重建后的 core-ru SVG 变化，本版 P7 SVG 字节未变）。**无新增西里尔串。**
- 本版重建复现（`rebuild-copy/`）：版目录副本删 svg/cards 后跑 run.py，rc=0，
  **8/8 SVG 与线上重建字节一致**。

## §5 p8 extract / compare（`logs/p8-extract.log/.json`、`logs/p8-compare.log/.json`）

- `tools/p8.py extract --p8 …/svg/p8-test.svg --total 150`：rc=0，**noted set 150/150**。
- `tools/p8.py compare --core-p8 core-ru/svg/p8-test.svg --edition-p8 …/svg/p8-test.svg --total 150`：
  rc=0，**status CLEAN**，missing=[]，extra_count=0，uncertain=[]，
  **keydiff=[137, 138, 139, 140]**（四条 E 节 RU→PT 翻译键，proof1 已核为正确翻译）。

## §6 keycheck 150（`keycheck.py` / `keycheck.log`）

- 机械比对：P8 印出键（`p8-extract.json` 的 `keys`，150 条）vs text.md Answers §（150 条）：
  **149/150 一致**；唯一分歧 Q150（P8 印 `✓`，text.md 为开放题说明——与核心一致的
  已知例外，proof1 同结论）。
- 重点键：Q20 `желании`、Q25 `b`、Q73 `заказов`——text.md 与 P8 印出键一致，
  印/网 PDF 的 P8 文字层均含 `20. желании`（`gates2.py` / `gates2.log`）。
- 其余 149 条无回归（题面/选项/键均未动：本次改动的 3 行不含任何练习内容；
  registry 分布与 proof1 一致；text.md 字节一致）。

## §7 印/网文字层一致 + P8 字号（`gates2.py` / `gates2.log`）

- pdftotext（PyMuPDF `get_text`）逐页拼接：印 57,122 字节 / 37,639 字符；
  网 57,122 字节 / 37,639 字符；**字面完全相等**（proof1 时印版少 43 空格的分段噪声
  本次未出现）。
- 网 PDF `pdftotext` 字节 > 0（webpdf 报告 58,327 text bytes；单文件 3,383,546 B < 7 MB）。
- P8 最小字号：印 **9.75pt**，网 **9.75pt**——符合 SOP §1.1 下限 9.75pt（目标 11.25pt）。
- 印/网文字层逐页一致（字面相等即逐页相等）。

## §8 改动范围核对（mtime + 内容）

- 改动的源码仅 `bslib4.py`、`content12.py`、`content34.py`、`content56.py`
  （2026-11-11 17:50）；`content7.py`、`content8.py`、`svglib.py`、`run.py`、
  `render.py`、`ru_textmd.py`、`check_core.py`、`WEEKLY-KIT.md`、`ABSTRACT.txt` 均未动。
- 再生件：`svg/p1–p6`（D1/D2/D3 所致）、`cards/*.png`（8 张）、印/网 PDF；
  `svg/p7`、`p8` 字节不变；text.md 重导出后字节不变（SHA `54d8a766…`）。
- 本 scratch 内全部中间文件：`measure.py`、`exp.py`、`exp*.log`、`verify.py`、
  `verify.log`、`gates2.py`、`gates2.log`、`keycheck.py`、`keycheck.log`、`run.log`、
  `render.log`、`webpdf.log`、`textmd.log`、`check_core.log`、`svg-before.sha256`、
  `svg-after.sha256`、`text-before.md`、`logs/`、`freeze-base/`、`rebuild-copy/`、
  三张裁图、`FIX-LOG.md`、`GATE-LOG.md`。
- 铁律①遵守：run.py/render.py/webpdf/textmd 的 stdout 均重定向到本 scratch 内绝对路径，
  运行前核对目标在 scratch 内；未重渲其他生产文件；未 commit、未 push。

## §9 结论

- **(a) 修完，自验全过**：D1/D2/D3 三法复测全部离边 ≥ +5px（光栅 +18/+7/+8×5）；
  run.py rc=0 TOTAL 150；occlusion 42 TEXTX 全部同类假阳性、CLEAR；
  p8 extract 150/150、compare CLEAN（keydiff [137,138,139,140]）；
  keycheck 149/150（仅 Q150 已知例外）；freeze baseline 8/8；
  印/网文字层字面一致；P8 最小字号 9.75pt（印/网一致）；SVG 只变 P1、P2–P6；
  text.md 字节不变。
- 唯一遗留越界：D5（P8，1863，+1），按任务只记录、不修。
- 新三 SHA：印 `4d726d922b33b6c38ab93e7ed1c47c8913817a5fa4e3bbc59988ff232bec61ed`
  （21,205,591 B）；网 `f21ed9285a7fcca0a3515e2daa2af2518b0e11fb83752280ea448cf80b7864df`
  （3,383,546 B）；文 `54d8a766e18daf5f256e91c76765c9e71fefb48c9435e83d28e103bba603d60e`
  （65,155 B，不变）。
