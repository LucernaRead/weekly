# FIX-LOG — W47 es-fr fix1 (D1 + O1, build 4)

**任务**：修 proof1 结论 (b) 的唯一缺陷 D1（轻），顺带核 O1。只改盒高，不改任何文字内容，不碰核心与 `tools/`。不 commit、不 push（proof2 另派）。
**对象**（动工前实测，与 brief 一致）：印刷 `La-Lucerna-VOL4-es-fr.pdf` 3,499,799 B SHA `c1c3ecdc326da7d91a4c55e8ad578e66d574db4436d6ec7a23164d653f54b168`；网页 `La-Lucerna-VOL4-es-fr-web.pdf` 846,204 B SHA `e6e5abbf4f923e4dfbae62777b1cea88f863e444d5be2e61892609005a245065`；`2026-w47-es-fr.text.md` 45,272 B SHA `94476219c438fc47ba2613e45b7a266302540ec57ece4d39203400def46a4bc7`。
**探针**：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4` 成功；scratch 真实写文件成功。全程 `TMPDIR=<scratch>/tmp`，未写 /tmp。
**前置阅读**：`scratch-proof-es-fr1/PROOF-NOTE.md` + `GATE-LOG.md` 全文；SOP §1.1、§8。

## 改动（4 处，均为盒高公式尾常数）

| # | 文件 | 行 | 改动 | 效果 |
|---|---|---|---|---|
| 1 | `content34.py` | 45 | P3「¿Y TÚ?」`eh` 尾 `+ 20` → `+ 29` | 盒高 +9px：底 1594.8 → 1603.75 |
| 2 | `content56.py` | 50 | P5「¿Y TÚ?」`eh` 尾 `+ 20` → `+ 29` | 盒高 +9px：底 1574.55 → 1583.55（未计 VOTAR 位移） |
| 3 | `content12.py` | 198 | P2「¿SABÍAS QUE…?」`sh` 尾 `+ 32` → `+ 37` | 盒高 +5px：底 543.5 → 548.5（O1） |
| 4 | `content56.py` | 41 | P5「VOTAR POR PRIMERA VEZ」`sh` 尾 `+ 32` → `+ 37` | 盒高 +5px：底 1251.5 → 1256.5（O1） |

- **为什么 D1 用 +9 而不用建议的 +5**：+5 只把绝对余量从 −2.75 提到 +2.25，低于任务“清除量 ≥+5px”按绝对余量读的要求；+9 在两种 PIL 测量法下绝对余量都 ≥+5.9，且 P3 盒底 1603.75 距 y=1608 分隔线仍有 4.25px（无 crossing，occlusion LINEX 0 flags，裁图目视有清晰纸面间隙）。
- **连带位移**（非主动改动，是盒高公式的推论）：P2/P5 的「¿Y TÚ?」盒位于 facts 盒下 26px，故随 facts 盒下移 5px，盒内文字逐元验证仅 y +5.0、字符全同（P2 14 元、P5 8 元）。P5「¿Y TÚ?」盒最终底 = 1574.55 + 5（位移）+ 9（自延）= 1588.55；P2「¿Y TÚ?」盒底 1051.0 → 1056.0，P3 facts 盒与 P4「¿Y TÚ?」盒（墨水余量 +1.25px，未被点名）均未动。
- **文字零改动验证**：SVG diff（build 3 freeze 复现件 vs build 4）：p1/p4/p6/p7/p8 逐字节相同；p2/p3/p5 仅 4 个 rect 高度 + P2/P5「¿Y TÚ?」文字 y 位移；全部 `<text>` 字符内容相同。`2026-w47-es-fr.text.md` SHA 不变。

## 实测清除量（PIL 墨水，非基线）

方法：`ink_check.py`（本目录）：取盒内末行文字，以其 SVG 字体实测降部——法语 sans 行用实际渲染字体 Noto Sans CJK SC（19 号降部 5.00px），serif facts 行用 Newsreader（21.5 号降部 5.00px）；同时取渲染 PNG 的实际墨水行（Cairo 次像素抗锯齿，用排除橄榄分隔线的暗像素判定）复核。另用 proof1 的 Newsreader 解析法复算：D1 两盒 +6.25/+6.15px，均 ≥+5。

| 盒 | 盒底 | 墨水底 (PIL) | 余量 PIL | 修前余量 | 改善 | 余量 PNG 实渲 |
|---|---|---|---|---|---|---|
| P3「¿Y TÚ?」D1 | 1603.75 | 1597.83 | **+5.92** | −3.08 | **+9.00** | +6.8（墨水行 1597） |
| P5「¿Y TÚ?」D1 | 1588.55 | 1582.63 | **+5.92** | −3.08 | **+9.00** | +6.5（墨水行 1582） |
| P2「¿SABÍAS QUE…?」O1 | 548.5 | 543.18 | **+5.32** | +0.32 | **+5.00** | +5.5（墨水行 543） |
| P5「VOTAR POR PRIMERA VEZ」O1 | 1256.5 | 1251.20 | **+5.35** | +0.35 | **+5.00** | +5.5（墨水行 1251） |

注：修前余量是本 fix 的复现值（实际渲染字体）；proof1 的 Newsreader 解析值是 −2.75/−2.85/+0.05/+0.05，相差 ≤0.33px，源于解析降部 4.75px 与光栅化 5.00px 之别，两种方法对修前溢出/修后 ≥+5 的结论一致。O1 两盒确认同属降部余量不足，已各延 5px。

## 重建（build 4）

- `run.py`（`build4.log`）：rc=0，FLOW OVERFLOW 0，HEAD TOO WIDE 0，TOTAL 150，MODELO 97 词；P2 col3 1056.0、P3 col3 1603.75、P4 col3 993.5、P5 col3 1588.55、P7 col3 1865.51、P8-keys y=2521。
- `render.py`（`render4.log`）：rc=0，8 页；印刷 3,499,799 B（与 build 3 同字节数纯属巧合，SHA 已变），网页 883,853 B（<7MB；较 build 3 的 846,204 B +37,649，webpdf 字体子集/压缩跨次差异，字形与文字相同；网页图已验为 303px/69ppi 降分辨率）。

## 新 SHA（build 4）

- 印刷 `La-Lucerna-VOL4-es-fr.pdf` 3,499,799 B — `7ff5b85401a93d862411a803903645e2c42c1ff023ecd8cd9404d998162e637e`
- 网页 `La-Lucerna-VOL4-es-fr-web.pdf` 883,853 B — `f8f786e2432c565d738761f95b532d45532e036ee5f8f38679d540a3e06d37fd`
- `2026-w47-es-fr.text.md` 45,272 B — `94476219c438fc47ba2613e45b7a266302540ec57ece4d39203400def46a4bc7`（不变）

## 逐门结果（全部重跑）

| 门 | 命令/方法 | 结果 |
|---|---|---|
| build | `tools/venv/bin/python run.py` | rc=0，OVERFLOW/TOO WIDE 0，TOTAL 150，MODELO 97 |
| render | `tools/venv/bin/python render.py` | rc=0，8 页 PNG + 印/网 PDF |
| creambox.py 全版扫描 | `creambox.py svg/*.svg`（`creambox-all4.log`） | 22 盒；D1 两盒基线余量 +11.0/+10.9；负基线余量仍是 proof1 的同 6 处误报（盒下标题/盒下注文：AHORA TÚ、CINCO CLAVES 注、LA PALABRA、BREVES 图注、DECIR LA HORA、LO QUE QUEDA），与核心同坐标一致，非溢出；无新增负值 |
| PIL 墨水复验 | `ink_check.py`（`ink-after3.log`） | 四盒余量 +5.92/+5.92/+5.32/+5.35，改善 +9/+9/+5/+5；PNG 实渲 +6.8/+6.5/+5.5/+5.5 |
| occlusion 审计 | `tools/occlusion_audit.py …/svg`（`occlusion4.log`） | **0 flags**；自检六类全触发（`occlusion-selftest4.log`） |
| p8 extract | `tools/p8.py extract --p8 … --total 150 --json p8-extract4.json` | **150/150**（parse: lines） |
| p8 compare | `tools/p8.py compare --core-p8 core-es/svg/p8-ejercicios.svg --edition-p8 … --total 150 --json p8-compare4.json` | **CLEAN**，missing=[] extra=0 uncertain=[]，keydiff=**[137, 138, 139]**（见下“待协调事项”） |
| freeze 渲染 | `tools/freeze.py baseline --build …/2026-w47-es-fr --core-svg …/2026-w47-es-fr/svg --out …/freeze-es-fr-fix1`（`freeze-baseline4.log`） | **8/8** SVG 逐字节相同（p1 cf8be0375430 / p2 7cefcc27fc3e / p3 c60aefdcfe55 / p4 d4d068ef068e / p5 f7c376c6e5ac / p6 b9a8ec2fdaed / p7 2190c844e7d4 / p8 7cc5b110e731） |
| freeze diff | `tools/freeze.py diff --core-svg core-es/svg --edition-svg … --json freeze-diff4.json` | 新增 CJK 仅 U+3000 ×1（与 proof1 相同）；与 proof1 diff 相比的新增差异只有 §6.14 的 7 条 `antes del`/`hasta` 串 + 核心 P8 中文注改动 |
| 印/网文字层一致 | `pdftotext`（plain + `-layout`）印版 vs 网版 | plain 各 46,246 B，`cmp` 逐字节一致；`-layout` 各 108,334 B，逐字节一致 |
| 文字内容零改动 | build 3 freeze 复现件 vs build 4 SVG；text.md SHA；pdftotext 词集 | SVG 仅 4 rect + y 位移；text.md SHA 不变；新旧 pdftotext `-layout` 词集相同、去空白字符集相同（46,247→46,246 B 与 108,606→108,334 B 只是 pdftotext 布版重排的空白差异，见 `textlayer-compare.txt`） |
| P8 最小字号 | PyMuPDF 逐页 span（`style11-4.log`） | **P8 min 10.12pt**（≥9.75pt 底线；其余页 11.62–12.75pt；印/网同值） |
| boxtitle | occlusion BOXTITLE 类 | **0 flags**（自检 BOXTITLE 触发） |
| §1.1 | 纸色/调色板/刊头/刊别/CJK | 纸 #fbfaf6；SVG fills 仅调色板色；刊头 196；VOL.4 ×9 / VOL.5 ×3；可见文本 CJK 仅 U+3000 |
| 8 页目视 | 印刷 PNG 全 8 页重点看 P2/P3/P5（`crop-p3-youturn.png`、`crop-p5-youturn.png`、`crop-p2-sabias.png`、`crop-p5-votar.png` + P2/P3/P5 整页） | 四盒末行全在奶油盒内、盒底留白清晰；P3 盒底与分隔线有清晰纸面间隙；无溢出/重叠/压页脚 |

## 待协调事项（未修，需 proof2/协调员裁定）

**核心在 fix1 进行中改了，es-fr 出现新的 core 偏离。** 2026-11-11 约 10:12–10:13（proof1 09:52 之后、fix1 作业期间），另一核心 agent 改了 `core-es/content12.py`（10:12:58）与 `core-es/content8.py`（10:13:04）并重建核心 SVG（10:13:34–10:13:50），把邮寄投票截止表述从 `antes del` 统一为 `hasta el jueves 19`（与 P5 正文“desde la convocatoria y hasta el jueves 19”一致），并在 P8 中文注加了“最迟”。es-fr 仍是改前的 `antes del`，共 7 处西语串（P1 头条段 `Tiene que pedirlo antes del jueves 19:`、P1 图注、P1 快问题干、P2 填空题干、P8 #116 键/注、P8 #139 键、P8 范文 `pido el voto por correo antes del jueves 19`）。后果：`p8 compare` keydiff 由 [137, 138] 变为 [137, 138, **139**]（状态仍 CLEAN）；freeze diff 新增差异仅此 7 串 + 核心 P8 中文注（`邮寄投票须在周四`→`邮寄投票最迟须在周四`，另 2 处为断行伪影）。**未修**：任务限定只修 D1、不改文字；核心改动仍在进行中、是否让各 fan-out 跟进须协调员裁定。另：第一次 `freeze baseline` 误把 `--core-svg` 指到 `core-es/svg` 報 0/8，已废弃；正确指到本版 `svg/` 后为 8/8。

## KIT 更新

`WEEKLY-KIT.md` 已更新：§3 实测值（P2/P3/P5 col3、PDF 大小与新 SHA、文字层字节数）、§6.13（D1/O1 修法与实测）、§6.14（核心抢修事项）、§7（build 4 命令与各门结果）、§8 Round 4 记录。

## 范围确认

- 只改了 `production/2026-w47/2026-w47-es-fr/` 内的 `content12.py`、`content34.py`、`content56.py`（各 1–2 行常数）与 `WEEKLY-KIT.md`；`tools/`、`core-es/`、SOP 均未动（`tools/*.py` 的修改时间 11-10/11-11 05:01，早于本次作业）。
- 未 commit、未 push。工作区其余修改均为其他 agent 的并行作业，与本次无关。
- 遗留文件（本 scratch 内）：`build4.log`、`render4.log`、`creambox-all4.log`、`creambox-diag4.log`、`ink-baseline.log`、`ink-after.log`、`ink-after2.log`、`ink-after3.log`、`ink_check.py`、`creambox.py`、`creambox_diag.py`、`occlusion4.log`、`occlusion-selftest4.log`、`p8-extract4.json/.log`、`p8-compare4.json/.log`、`freeze-baseline4.log`、`freeze-diff4.json/.log`、`freeze-es-fr-fix1/`、`print.txt`、`web.txt`、`print-layout.txt`、`web-layout.txt`、`print-layout2.txt`、`web-layout2.txt`、`textlayer-compare.txt`、`svg-diff-summary.txt`、`style11-4.log`、`crop-p3-youturn.png`、`crop-p5-youturn.png`、`crop-p2-sabias.png`、`crop-p5-votar.png`、`probe.txt`、`tmp/`。
