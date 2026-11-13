# FIX-LOG — 2026-W47 zh-cn × de fix1（修复员，2026-11-11 17:30–18:00 UTC）

- 版：`production/2026-w47/2026-w47-zh-cn-de/`（只改这一版；核心 `core-zh-cn` 只读核对）
- 修复员工作区（唯一 scratch）：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-cn-de1/`
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）
- SOP：仓根 `SOP.md`（§1.1、§8.4）+ `hidden_files/w47/briefs/brief-coordinator.md` 已读
- 未 commit、未 push（协调员统一处理）

## 0. 开工前三 SHA 核对 — 一致（proof1 2026-11-11 17:25 UTC 盘验值）

| 文件 | 字节 | SHA-256 | 核对 |
|---|---|---|---|
| `Lucerna-VOL4-DE.pdf`（印） | 44,829,975 | `e6ed50ab8eedb82c249aee9a9ce5e6ed61d0b06bc2060c79c9cdb94957ac424b` | ✓ |
| `Lucerna-VOL4-DE-web.pdf`（网） | 2,732,464 | `7fb396f13ece42b771beb722811e4ab8df8bb2f9971cf2380e3f06d7e83535e5` | ✓ |
| `2026-w47-zh-cn-de.text.md`（文） | 50,637 | `8940ba88e92d70eb6d54e4759657d187b451e259b1633bb92f9d475e97075b0a` | ✓ |

磁盘：57G 可用。开工前 SVG 基线 SHA 已存 `svg-before.sha256`。

## 1. 缺陷复现（改前实测，与 proof1 一致）

- D1（`gate67.py`，PIL 真墨）：P2 日历盒标题 `本周生活小日历　Kalender der Woche`，
  真墨右缘 1418.0 vs 奶油盒右缘 1411.5，**越过 6.5px**；G6 1 处、G7a 1 处（同行）。
  35 盒中唯一负值，其余最小余量 14.5px（P1 数字盒）。
- D2（`gate8b.py`）：P1 y=1366.3 行首孤立 `》`（`》 startet`），全版 31 处孤儿标点中唯一
  的 `》` 行首；其余 30 处均为核心同款已接受形态。

## 2. 修法（只改 `content12.py` 两行，其余一字不动）

### D1 — `content12.py:187`：德语 gloss 缩短，字号不动（23pt bold）

```diff
-f.box("本周生活小日历　Kalender der Woche", [
+f.box("本周生活小日历　Wochenkalender", [
```

- 理由：`Wochenkalender`（周历）是标准德语复合词，语义与 `Kalender der Woche` 相同；
  不降字号、不动中文部分、不动盒几何。
- 修前测算（`measure-candidates.py`，与 gate67 同款 PIL 真墨）：
  旧标题 advance 411.2 / 真墨右缘 1418.0 / 余量 −6.5px；
  新标题 advance 375.2 / 真墨右缘 1383.0 / **余量 +28.5px**（省 35.0px，核心同盒余量 22px）。
- 注意：fan-out #3 报告的 "21px clear of 照片" 是照片间距，未采用该修法。

### D2 — `content12.py:50`（任务简报称 :51，文件实际行号为 50）：去 `neue`，不断句义

```diff
-    ("21. Nov., Samstag — der neue Film 《试探》 startet", "serif", False, INK, 20, 1.35),
+    ("21. Nov., Samstag — der Film 《试探》 startet", "serif", False, INK, 20, 1.35),
```

- 理由：只删一个德语形容词 `neue`；日期、星期、片名、动词、中文行（P2 190 行
  `周六 11月21日 — 电影《试探》上映`、P1 练习 `Der Film 《试探》 startet am 21. Nov.`）
  均不动。文字内容本身（事件、片名、上映日）不变。
- 修前测算（`wrap()` 同款函数，盒内宽 386.5）：
  旧：2 行 `21. Nov., Samstag — der neue Film 《试探`（378.1）/ `》 startet`（85.5）——孤儿 》；
  新：2 行 `21. Nov., Samstag — der Film 《试探》`（348.8）/ `startet`（60.6）——无孤儿、不断开，
  行数不变（盒高不变）。与核心断行形态一致（`《试探》 / opens`）。

### 绝不动项复核

- badge：`content12.py:24` 仍为拉丁-only `CHINESISCHER TEXT　ERKLÄRUNGEN AUF DEUTSCH`；
  新 SVG + text.md 中 `德语讲解` 0 次。
- 核心 D4/D5 三处限定（`content34.py:130/131/160` 全球总决赛、GEN S16 口径）未动；
  `git diff` 外核对：除 `content12.py` 上述两行外无其他源码改动
  （注：`production/2026-w47/` 在 git 中为 untracked 树，故以 grep + 行号核对为准）。

## 3. 重建（全套，版目录正常流程；全部重定向用绝对路径、落在本 scratch 内）

| 步骤 | 命令 | 结果 |
|---|---|---|
| run.py | `tools/venv/bin/python run.py`（cwd=版目录）→ `run-fix1.log` | rc=0，TOTAL 150（A2 56 / B1 69 / B2 25；页 10/18/18/18/18/18/12/38），overflow/warn/error/traceback 0 命中；P8 keys 尾 y=2521.9（<2560） |
| render.py | `tools/venv/bin/python render.py` → `render-fix1.log` | rc=0，8 张 cards + 印 PDF 44,829,877 B |
| webpdf.py | `tools/venv/bin/python tools/webpdf.py <版>/svg <版>/Lucerna-VOL4-DE-web.pdf` → `webpdf-fix1.log` | rc=0，WROTE 2,732,386 B，44,729 text bytes |
| export | `tools/venv/bin/python <scratch>/export_de.py` → `export-fix1.log` | rc=0，text.md 50,628 B（逐行导出，非 PDF 倒抽） |

铁律①遵守情况：全部四步 stdout 均重定向到本 scratch 内绝对路径；无 `~/…` 波浪路径；
无重定向误写生产目录（生产 SVG 只由 run.py 的版内 OUT 正常写入，即本次交付本身）。

## 4. 新三 SHA（即为准）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-DE.pdf`（印） | 44,829,877 | `b38ffe40ae07b2502766d553d33e50d414d6210288c852ed961259cc2ee97279` |
| `Lucerna-VOL4-DE-web.pdf`（网） | 2,732,386 | `ecd253809c7c4c331a3093dd808fd06337307fb170dc0c0d8a2ab39f79aeaa81` |
| `2026-w47-zh-cn-de.text.md`（文） | 50,628 | `51d6dab11f8b9d857790b8e1c1aba6c5e34259f3eb4b77a19ad77d24106e0a1e` |

text.md 两处改动已验：`:53` 为 `21. Nov., Samstag — der Film 《试探》 startet`，
`:271` 为 `本周生活小日历　Wochenkalender`；`Kalender der Woche` / `neue Film` 在 text.md 中 0 次。

## 5. SVG 变化清单（前后 SHA）

| 页 | 前 SHA | 后 SHA | 变化 |
|---|---|---|---|
| p1-touiban.svg | `eb00af5d…`（`eb00af5d434931043db140ea5aac1034bd9f0e15d2e12f7fd924839fa0c7f6e3`） | `418ad8a2…`（`418ad8a2c78db911aaa75157af05735892c5727113657370c7d25a60d70daba9`） | **变（D2）** |
| p2-shenghuo.svg | `d129d1b4…`（`d129d1b425cb61dbc4f1e91ea16fe55e4905bdd43c030998a1a32ad288d55dcf`） | `cc90a57e…`（`cc90a57e06adecaeaf4d2ba543c88c5e00faa3f17b8f72bd441b5e06c75eeb4b`） | **变（D1）** |
| p3-wenhua.svg | `4115835a0c2b34615eb40817da2f36b3f2fca25320291364da5e7b922a113c27` | 同左 | 不变 |
| p4-tiyu.svg | `6c73abc41299dfdfbd46585d37b218eef64dd63056779c4e14155770017e671a` | 同左 | 不变 |
| p5-qingnian.svg | `e34dd96eb7880abe7e83e0fc12fcce69b44749504132289c58e5ea55eb15c333` | 同左 | 不变 |
| p6-shendu.svg | `44a7a95e5cf1a84270935951bf49075e110448953a3bba274dd318fa73cf12c4` | 同左 | 不变 |
| p7-ciyu.svg | `d82b8b66550e32931804505f7366d2582494fcdb772af5a0bd0b249d0c865b97` | 同左 | 不变 |
| p8-ceyan.svg | `bb46bd5d88f67d9bd1e028c87c91436100532295b88892376dbfdc0c8da64945` | 同左 | 不变 |

仅 P1、P2 两页变化，其余 6 页字节不变（`svg-after-run.sha256` diff 为证）。

## 6. 两缺陷修后验证（源码行 + 实测值 + 渲染证据）

### D1 — 修后标准：标题真墨右缘离盒边 ≥ +5px

- PIL 真墨（`gate67.py`，新 SVG）：标题 `本周生活小日历　Wochenkalender`，
  真墨右缘 **1383.0**，盒右缘 1411.5，**余量 +28.5px**；G6 0、G7a 0、G7b 0、页缘溢出 0；
  35 盒最小余量现为 P1 数字盒 14.5px，P2 日历标题排第 5（+28.5px）。
- 150dpi 渲染像素（`verify-pixels.py`，印 PDF P2）：校准——奶油盒右缘实测 svg x=1410.6
  （标称 1411.5，量化差 0.9px）；标题行带（svg y 210–245）内、盒边右侧条带
  (1411.5, 1439.5] 的暗像素 26 个，**全部位于 svg x=1439.4 单列**，即山谷照片
  （x=1439.5 起）左缘的照片像素（蓝灰色值如 (37,60,73)），**标题真墨越盒像素 0 个**。
- 裁图留证：`p2-cal-title-after.png`（svg x 980–1460, y 195–260）——目视：
  `Wochenkalender` 完整落在奶油底上，右侧留有明显奶油余量后才是山谷照片。

### D2 — 修后标准：SVG run 无孤儿 》 行首 + 渲染裁图确认

- SVG run（新 `p1-touiban.svg`，直接 grep）：
  - y=1339.265, x=556.5：`21. Nov., Samstag — der Film `；
    x=825.3：`《试探》`（同一行、闭合完整）；
  - y=1366.265, x=556.5：`startet`（无 》）。
- `gate8b.py`（新 SVG）：孤儿标点 31→**30 处**，`》` 行首 **0 处**；
  其余 30 处与改前一致，均为核心同款已接受形态。
- 150dpi 渲染裁图：`p1-numbers-box-after.png`（svg x 540–980, y 1290–1400）——目视：
  第一行以 `《试探》` 收尾，第二行仅 `startet`。

## 7. 门禁逐项实测值（详见 GATE-LOG.md）

- gates-zhcn.py：**11/11 全过**（OVERALL: ALL PASS，rc=0）
- freeze baseline：**8/8**（rc=0，8 枚 OK；核心完整性自验通过）
- freeze diff `--strict-cjk`：**TOTAL 新增 CJK 0**（rc=0；各页新增均为 0）
- p8 compare：**CLEAN**（missing/extra/uncertain/keydiff 均空）
- 印/网文字层：8/8 页 token 差 0（posdiff 0，msdiff 0；
  P1 355/355、P2 350/350——较 proof 各少 1/2 个 token，正是删 `neue` 与标题 3 词→1 词所致；
  pdftotext 印/网各 44,729 B）
- P8 最小字号：**9.98pt**（中位 9.98pt，370 spans；≥9.75pt 下限 PASS，与核心同值）
- 150 键复核：REG 键（key-only）vs 核心 **0 差异**、vs proof1 版 **0 差异**；
  页/级/型 0 差异；P8 印出键 vs 核心 0 差异；P8 印出键 vs REG 仅 Q150 不同
  （REG `(开放题，范文如下)` vs P8 `✓`，与核心一致，是设计）

## 8. 过程披露

- 核心 SVG mtime 异常：`core-zh-cn/svg/*.svg` 的 mtime 显示 2026-11-11 17:53:22–17:54:10，
  但**内容未动**：8 枚现 SHA 与 freeze-baseline 记录的 core 哈希逐字节相同
  （如 p1 `6685c71a…`、p8 `ce8692e2…`）；且我本次 freeze-baseline 运行结束于 17:49:30
  （`freeze-out/svg/p1` 17:48:51、`freeze-baseline-fix1.log` 17:49:30），
  17:53 的触碰发生在我运行结束 4 分钟后，系并行他线（zh-cn-fr 线同期在跑）的操作。
  freeze.py 自身的 before/after 哈希守卫亦通过（rc=0）。核心内容零改动。
- 其余并行线：同期 `2026-w47-zh-cn-fr/` 有改动（mtime 17:43 起），与我无关，我未碰该版。
- 本次工作未写任何生产目录之外的文件；所有脚本/日志/裁图均在本 scratch 内。
- 未 commit、未 push。

## 结论

**(a) 修完自验全过。** D1、D2 均按修后标准验证通过，全部机械门禁（11/11 + freeze 8/8 +
strict-CJK 0 + p8 CLEAN + 文字层差 0 + P8 字号 9.98pt + 150 键 0 差异）通过，
仅 P1/P2 两页 SVG 变化。新三 SHA 见 §4。
