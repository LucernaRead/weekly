# FIX-LOG — 2026-W47 pt-it fix1（仅 D6；D7 已撤销）

- Fix agent: subagent fix-pt-it1，2026-11-11（UTC）
- Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-pt-it1/`
- Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-pt-it/`（只改该版源并重渲染双 PDF；NO commit、NO push；未动 core-pt、未动任何其他版）
- 缺陷来源：proof1 007efa37（`scratch-proof-pt-it2/PROOF-NOTE.md`、`GATE-LOG.md`）
- TMPDIR 全程指到本 scratch 的 `tmp/`；未写 /tmp（除工具自身输出外）；探针通过（repo 内 `echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0；scratch 真实写文件通过）

## 交付三 SHA（重建版，仅 D6 改动；text.md 未变，见注）

| 文件 | SHA-256 | 字节 |
|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | `75fd3847bc5c4f0a8cab338e2e78a632463bc8f4e19e838c00026c34cf9ff67c` | 12,930,798 |
| `A-Lucerna-VOL4-web.pdf`（网） | `a0ccd14c0c51411b37d0733bb21b14f143ad84c04d7212d15319e560f8a670fd` | 1,137,048 |
| `2026-w47-pt-it.text.md` | `37c1980caacc6cef28d9df50133b09b45a51a8d4f17296e34412b2cd88285209` | 37,419 |

注：text.md SHA 与修前（proof1 核对值）逐字节相同——两处改动字符串（P2 框标题 gloss、P1 标语）均不出现在 text.md 中（text.md 第 102 行只有不带 gloss 的 `PARA NÃO ERRAR`，且无 `Ogni settimana` 标语行）；重建未触及其余任何文字，故 text.md 无变化是预期的，不是漏渲染。修前三 SHA（proof1）：印 `6c8a5f3d…11ce` / 12,930,828；网 `5ebf28b4…14e89` / 1,137,080；text.md 同上。

## D6 — P2「PARA NÃO ERRAR」框标题 gloss 过长 → 已修（唯一改动）

- 定位：P2 第二栏奶油框 x[538.5,961.0] y[605.02,846.02]；标题基线 y=642.02，fs=23 粗体，x=556.5。
- 改动（两层同改，沿用 D4/D5 前例的双层修法；tables_it.py 是 fan-out 变换源 SEG，content12.py 是渲染用的字面量）：
  - `tables_it.py:58`：`"口诀": "La regola da ricordare"` → `"口诀": "La regola"`
  - `content12.py:183`：`f.box("PARA NÃO ERRAR　La regola da ricordare", [` → `f.box("PARA NÃO ERRAR　La regola", [`
- 改前实测（proof1 值，本轮改前预量复核一致，见 `premeasure.log`）：PIL 真墨墨右 1020.5，clear −59.5；印/网 PDF 像素 −62.4。
- 改后实测（双法，见 GATE-LOG §2）：
  - PIL 真墨（自身字号 fs=23）：墨右 877.5，**clear +83.5**（≥ +15 要求；与 proof1 预实测值逐字一致）。
  - 交付印 PDF 300dpi 像素：墨右 878.4，**clear +82.6**；网 PDF 同值 +82.6。
  - 目视：`crop-p2-PARA-NAO-ERRAR-fix1.png`（印 PDF 300dpi 裁图）——「PARA NÃO ERRAR　La regola」整行收进奶油框内，右缘余量肉眼清晰；`view-p2-fix1.png`（P2 整页 110dpi）同处无漫出。
- 未动核心、未动其他文字。重渲染后 SVG 变化：**仅 `svg/p2-vida.svg`**（修前 `dbbb6bcc…` → 修后 `1ccd77e4…`）；其余 7 页 SVG 字节不变（见 `svg-pre.sha` / `svg-post.sha`，diff 仅 p2 一行）。

## D7 — P1 顶栏标语：已撤销，未改动（记录在案）

- 简报原列 D7：`tables_it.py:201` / `content12.py:15` 标语「Il portoghese che legge il Brasile」被指主客颠倒，拟改为「Il portoghese che i brasiliani leggono」。
- 撤销：协调员紧急更正——该判断为误判。pt-fr 与 pt-es 两版复校员各自独立判定同构句式成立（法语「Le portugais que lit le Brésil」：que 恒作直接宾语、主语是后置的 le Brésil；西语「El portugués que lee Brasil」：el libro que lee Juan 式，主语后置，反向解析被语义封堵）；意大利语完全同构（「il libro che legge Mario」= Mario 读的那本书），「Il portoghese che legge il Brasile」唯一合语义的解析是 che=宾语、il Brasile=主语，即“巴西人读的葡语”，与中文原文一致，无颠倒。pt-it proof1 O2 本也只写“疑似”。
- 执行过程（如实记录）：本 agent 在收到撤销前已按原简报改了标语两处（tables_it.py:201、content12.py:15）并做过一次中间态重渲染（该中间版印 PDF SHA 未交付、未留存为交付件）；收到撤销后**立即将两处还原为原句「Il portoghese che legge il Brasile」**（`grep -c "che i brasiliani"` 两文件皆为 0；`content12.py:15` 与 `tables_it.py:201` 恢复原句），并以还原后的源码**重新跑 run.py → render.py → webpdf.py 全量重建**，交付的三 SHA 均为此次重建的产物。
- 还原验证：`svg/p1-capa.svg` 修后哈希 `38041cab0b75939696f77a7d92fc4227d3dc5c8730d957615e2d075e4ebe5511`，与修前逐字节相同（P1 零改动）；P1 整页目视图 `view-p1-fix1.png` 中顶栏标语仍为原句「Il portoghese che legge il Brasile」。改前为“新标语”做的 PIL 预量（墨 [564.1, 1386.0]，两侧余量 +476）已作废，不作为交付证据（见 `premeasure.log`，仅留作过程记录）。
- 净源码改动（相对修前）：仅 D6 两行（tables_it.py:58、content12.py:183各一行）；标语两行净零改动。

## 重建命令（全程 tools/venv/bin/python，TMPDIR=本 scratch tmp/）

1. `run.py`（生产目录）：rc=0，TOTAL 150（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38；范文 88 词；0 OVERFLOW / 0 TOO WIDE）——`run-fix1.log`
2. `render.py`：rc=0，印 PDF 12,930,798 字节——`render-fix1.log`
3. `tools/webpdf.py production/2026-w47/2026-w47-pt-it/svg production/2026-w47/2026-w47-pt-it/A-Lucerna-VOL4-web.pdf`：rc=0，网 PDF 1,137,048 字节——`webpdf-fix1.log`
4. 复核用 build-copy（本 scratch 内，生产目录源 + svg + assets 的副本）：run.py rc=0 TOTAL 150；gates.py 16/16；重建 8 张 SVG 与生产目录交付 SVG 逐字节一致 8/8——`run-copy.log`、`gates-fix1.log`
