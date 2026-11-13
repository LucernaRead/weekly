# FIX-LOG — 2026-W47 pt-es（葡萄牙语目标 · 西班牙语读者版）· fix1（D-NEW1）

- 修复：2026-11-11；fix agent（scratch-fix-pt-es1）
- 版目录：`production/2026-w47/2026-w47-pt-es/`；无 commit、无 push
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-pt-es1/`
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3）；`PYTHONDONTWRITEBYTECODE=1`；`TMPDIR=<scratch>/tmp`（未用系统 /tmp）
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0；`/dev/null` 存在；scratch 目录开工前不存在（新建）+ 真实写文件成功。

## 结论

**D-NEW1 已修复。**P1 奶油框标题 `EM POUCAS PALAVRAS　EN BREVE` 在交付 PDF 渲染中由 −3px 变为 **+14px**（修净标准：PDF 渲染 clear ≥ +5px）。其余 7 项首轮缺陷全部存活；150 题逐题手验 150/150；全部机械门通过。P1 顶栏标语「El portugués que lee Brasil」未动。

## §1 改动：1 行源（惟一源码改动）

文件：`production/2026-w47/2026-w47-pt-es/content12.py:139`

```diff
-p.text(bx + 22, 1914, "EM POUCAS PALAVRAS　EN BREVE", 24, "sans", True, OLIVE)
+p.text(bx + 22, 1914, "EM POUCAS PALAVRAS　EN BREVE", 23, "sans", True, OLIVE)
```

- 改法：标题字号 24pt → 23pt；**文字内容一字未改**（gloss `EN BREVE` 保留）。
- 选法依据（先实测再定，`gloss_probe.py` / `gloss_probe.log`，PIL 真墨，框右缘 1862.0，标题 x=1461.5）：
  - 基线 24pt：advance 右 1865.7（clear −3.7）、真墨右 1865.5（clear −3.5）——复现 proof1（−3.6/−3.5）。
  - 候选 A「24pt，`EN BREVE` → `Breve`」：真墨右 1818.5，clear **+43.5**。
  - 候选 B「23pt，原串」：advance 右 1848.8（clear +13.2）、真墨右 1848.5（clear **+13.5**）。
  - 候选 C「24pt，`EN BREVE` → `BREVE`」：真墨右 1827.5，clear +34.5。
  - 定 B：23pt 已是本版框标题既有字号（P2 `PARA NÃO ERRAR　La regla` 即 23pt），不破坏版式一致性；且保留读者可见的完整 gloss 文案——`EN BREVE` 是 `EM POUCAS PALAVRAS` 的自然西语对译，缩成 `Breve` 会丢介词结构。+13.5 真墨 / +14 PDF 渲染远高于 +5 门限，无需更大改动。
- `tables_es.py:111`（`"快讯": "EN BREVE"`）未动：该条目除自身定义外无任何引用，且标题为 content12.py 硬编码字串；text.md 全文 0 处 `EN BREVE`，故 text.md 不受影响（SHA 不变，见 §3）。

## §2 D-NEW1 修复实测（改前 → 改后）

| 方法 | 改前 | 改后 | 门限 |
|---|---|---|---|
| advance（boxtitle_core.py） | 右 1865.6，clear −3.6（proof1；本次基线复测 −3.7） | 右 1848.7，clear **+13.3** | > 0 |
| PIL 真墨（boxtitle_trueink.py，本字号） | 右 1865.5，clear −3.5 | 右 1848.5，clear **+13.5** | > 0 |
| **交付印 PDF 渲染（pdftoppm 96dpi，1:1 单位）** | 右 1865，clear **−3**（x=1863 有 9px、1864 有 6px、1865 有 2px 深色像素） | 右 1848，clear **+14**（x≥1849 0 深色像素） | **≥ +5** |
| **交付网 PDF 渲染（同法，p1）** | 右 1865，clear −3（proof1） | 右 1848，clear **+14**（本次重测，见 GATE-LOG） | ≥ +5 |
| CairoSVG 卡片（同 SVG） | 右 1862，clear +0 | 右 1848，clear +14 | — |

- PDF 渲染裁图证据：`p1-enbreve-title-pdf.png`（改后，4× 裁切，x 1700–1900 / y 1870–1945）：末字母 E 止于奶油盒内，盒右缘外为空白；`p1-enbreve-title-pdf-OLD.png`（改前同法裁切，对照）。
- 交付 P1 整页目视：`render-final/print-p-1.png`（生产印 PDF 渲染）——标题在盒内，顶栏标语、头条、quiz 均正常，无其他可见变化。

## §3 交付物（三 SHA）

| 件 | SHA-256 | 字节数 | 相对改前 |
|---|---|---|---|
| 印 PDF `A-Lucerna-VOL4.pdf` | `75e870cf38a85a5c84ed4d02b19923736dcd4756c3e9d12a52cc1778b982f3d3` | 12,933,061 | −1 B（仅标题字号 24→23） |
| 网 PDF `A-Lucerna-VOL4-web.pdf` | `4e7b30eaa0a1938c28f12fdac1df494b54d94bfccd14261d2de868ff0e36e94d` | 1,140,280 | +4 B（网 PDF 字节数不可复现，见注） |
| text.md `2026-w47-pt-es.text.md` | `96d6f11a5616ab97291115bb9da0577bce8049031f14988576f6cced77b29e27` | 37,467 | **不变**（与 proof1 逐字一致） |

- 注：网 PDF 只以文字层比较论证，永不以 SHA/字节数论证（fontTools 写 wall-clock 到 head.modified，字节不可复现）。本次印/网文字层逐字节相同（109,229 B；改前 109,231 B——仅 P1 标题行 `-layout` 空格少 2 格，见 GATE-LOG §5）。

## §4 改动范围（生产目录开工/收工 SHA 全量复核）

相对开工快照 `prod-snapshot-before.sha256`（47 文件），**恰好 5 个文件变化**：

- `content12.py`（1 行：字号 24→23）
- `svg/p1-capa.svg`（仅标题元素 `font-size="24"` → `"23"`；其余 7 页 SVG 字节不变，见 §5）
- `A-Lucerna-VOL4.pdf`（重渲染）
- `A-Lucerna-VOL4-web.pdf`（重渲染）
- `cards/p1-capa.png`（重渲染的 P1 卡片，与新 SVG 一致；其余 7 张卡片与改前字节相同）

其余 42 个文件（含 text.md、ABSTRACT.txt、其余全部 .py、其余 7 页 SVG、其余 7 张卡片、assets）**字节不变**。core-pt 41 个文件 `core-snapshot-before.sha256` 全 OK，**零改动**。

## §5 只 P1 变化（重建 SVG 比对）

build-copy 内 `run.py` 重建 vs 发货 SVG：

```
p1-capa DIFFERS — 仅标题元素：font-size="24" → "23"（x=1461.5 y=1914，文案不变）
p2-vida / p3-cultura / p4-esporte / p5-jovens / p6-aprofundamento / p7-lingua / p8-avaliacao IDENTICAL
```

## §6 卡片 vs 交付 PDF 假阴性复核（D-NEW1 教训）

同一 SVG，两种渲染路径对同一标题读数不同（`card_vs_pdf.py` / `card-vs-pdf.log`，本轮独立重测，与 proof1 逐项一致）：

| 渲染路径 | 旧标题读数 | 新标题读数 |
|---|---|---|
| CairoSVG 卡片（p1-capa.svg → 1950×2700 PNG） | 1862，clear **+0**（假阴性：首轮 O2 据此判“0px、无缺陷”） | 1848，clear **+14** |
| 交付印 PDF 渲染（pdftoppm 96dpi） | 1865，clear **−3**（列计数 1863:9 / 1864:6 / 1865:2） | 1848，clear **+14** |

- 复核结论：卡片路径把整行收窄约 3px（hinting/字距取整差异；两路径解析到同一字体文件 `NotoSansCJK-Bold.ttc` SC face）。修净标准只认交付 PDF 渲染像素（≥ +5px），卡片与 PIL 真墨只作交叉验证——本次三法一致通过（+13.3 / +13.5 / +14），卡片法未单独作证。
- 附带：proof scratch 内的 `card-probe3.log` 本身是一份 Python Traceback（`NameError: name 'S' is not defined`，其 heredoc 探针未跑成）；其 GATE-LOG §22 的 D7 数值（PDF +33 / 卡片 +22）经本轮用 `d7_essay_measure.py` 在真正的范文 10 行上独立重测得到证实（见 GATE-LOG §4），与该失败日志无关。

## §7 明确不动项

- P1 顶栏标语「El portugués que lee Brasil」**未改动**：`content12.py:15` 与 SVG 各 1 处原文保留；O-S1（首读歧义观察项）协调员已裁定不改。
- 除 D-NEW1 外无任何其他源码、文案、键、页码改动；无 commit、无 push（目录在 git 中仍为 untracked，HEAD 未动）。
