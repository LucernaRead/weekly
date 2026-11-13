# W47 ru 家庭第四轮修复 FIX-LOG-4（PROOF-NOTE-4 的 J-1～J-6）

- 任务：只修 PROOF-NOTE-4 6 项 low 发现（全部同一缺陷类：同一俄语词/标签在一版内两种译法），别的什么都不动。
- 日期：2026-11-12（Thu；构建 20:41–21:09 UTC，门禁 21:10–21:13 UTC）
- 前置已读：`scratch-reproof4-w47-ru/PROOF-NOTE-4.md`（J-1～J-6）；`scratch-fix3-w47-ru/FIX-LOG-3.md`（fix2b/2c/3 的构建驱动与门禁清单）。
- 范围：只动 `production/2026-w47/` 的 5 个目录：`2026-w47-ru-pt`、`2026-w47-ru-ja`、`2026-w47-ru-ko`、`core-ru`、`2026-w47-ru-zh-tw`（各 content*.py 源头、SVG、印/网 PDF、text.md、WEEKLY-KIT.md）与本 scratch 目录；不碰其他家庭、其他周；不 commit、不 push、不跑 lint、不改 SOP。
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python` 全程（未用系统 python3）。
- 磁盘：开工 95G 已用、收尾 95G（门限 100G，全程未触发）。
- 工作文件：本目录 `apply4.py` + `apply4-rest.py`（源头修改，断言计数）、`gen_expected.py` + `expected-{pt,ja,ko,core,zh-tw}.json`（回补预期替换）、`backfill4.py`（复用 2b/3 回补逻辑）、`driver.sh`（构建驱动，5 版各一跑）、`verify4.py`（印/网核验 + 全量指纹对照）、`gates4.sh`（门禁驱动）、`update_kit.py`（KIT 更新，断言计数）、`pre-2026-w47-ru-{pt,ja,ko,core,zh-cn,zh-tw}.text.md`（修前 text.md 快照）、`pre-{pt,ja,ko,core,zh-tw}-svg.sha256`（修前 SVG 快照）、`pre-fingerprint.txt`（修前 11 版 34 文件 SHA 快照）、`logs/`（run/render/textmd/backfill/webpdf 日志）、`gates/`（门禁日志/JSON）、`build-{pt,ja,ko,zh-tw,core}.log`、`summary-{pt,ja,ko,zh-tw,core}.txt`。
- 渲染：5 版串行（RAM 紧张，单版一次）；render 一次即成，无需重试；未杀任何进程。

## 1. 源头改动：11 处（每处断言旧串计数与新串原先计数，全部通过）

### 1.1 逐处记录

| # | 版 | 源文件：行号 | 改前 | 改后 | 断言 |
|---|---|---|---|---|---|
| J-1 | ru-pt | `content56.py:184,186` | `Dados de exercício`（各行 `e.ex("B2", "Completar frases", …)` key 串） | `Dados de prática` | 旧 ×2、新原先 ×1（L182 Q85 key）；改后旧 ×0、新 ×3 |
| J-2 | ru-ja | `content56.py:184,186` | `練習データ`（`e.ex("B2", "空所補充", …)` key 串） | `練習用データ` | 旧 ×2、新原先 ×2（L158 标题 + L182 Q85 key）；改后旧 ×0、新 ×4 |
| J-3 | ru-ja | `content56.py:89` | Q79 句译注 `…それから割引コード` | `…それからプロモコード` | 旧 ×1、新原先 ×2（L71、L85）；改后旧 ×0、新 ×3 |
| J-3 | ru-ja | `content7.py:33` | P7 B1 词表行 `промокод 割引コード` | `промокод プロモコード` | 旧 ×1、新原先 ×1（L40）；改后旧 ×0、新 ×2 |
| J-3 | ru-ja | `content8.py:92` | Q147 key 注 `割引コードを確認してください` | `プロモコードを確認してください` | 旧 ×1、新原先 ×0；改后旧 ×0、新 ×1 |
| J-4 | ru-ko | `content56.py:184,186` | `연습 데이터`（`e.ex("B2", "문장 완성", …)` key 串） | `연습용 자료` | 旧 ×2、新原先 ×2（L158 标题 + L182 Q85 key）；改后旧 ×0、新 ×4 |
| J-5 | ru-ko | `content56.py:89` | Q79 句译注 `…그다음 할인 코드` | `…그다음 프로모 코드` | 旧 ×1、新原先 ×2（L71、L85）；改后旧 ×0、新 ×3 |
| J-5 | ru-ko | `content7.py:33` | P7 B1 词表行 `промокод 할인 코드` | `промокод 프로모 코드` | 旧 ×1、新原先 ×1（L40）；改后旧 ×0、新 ×2 |
| J-5 | ru-ko | `content8.py:92` | Q147 key 注 `할인 코드를 확인해 주세요` | `프로모 코드를 확인해 주세요` | 旧 ×1、新原先 ×0；改后旧 ×0、新 ×1 |
| J-6 | core-ru | `content56.py:85` | Q77 配对选项表 `"促销码 a"` | `"折扣码 a"` | 旧 ×1、新原先 ×2（本文件内 L71、L89；全版 content 文件计 ×5）；改后旧 ×0、新 ×3 |
| J-6 | ru-zh-tw | `content56.py:85` | Q77 配对选项表 `"促銷碼 a"` | `"折扣碼 a"` | 旧 ×1、新原先 ×2（本文件内 L71、L89；全版 content 文件计 ×5）；改后旧 ×0、新 ×3 |

- 每处只改字符串本身；行内其他参数、俄语部分、同一行其余选项（J-6 的 `大促销 d` / `退货 b` / `折扣 c`）均未动。
- 旧串全版清零核查（修后）：5 版 content*.py + text.md 内 7 个旧串（`Dados de exercício`、`練習データ`、`割引コード`、`연습 데이터`、`할인 코드`、`促销码`、`促銷碼`）grep 均为 0 处（KIT 历史条目除外，见 §6）。
- `content56.py` SHA-256（前 12 位）：pt `23e50a584e0c` → `d899320e8b7e`；ja `c31748b5bc42` → `b7ad19227d7b`（两处编辑同一文件）；ja `content7.py` `12111e2d070e` → `93198cf987cc`；ja `content8.py` `2a499204cd8e` → `310dad0a36fb`；ko `content56.py` `2f44fd5aa472` → `9afe06c6c75f`；ko `content7.py` `9b2ce3db8fc2` → `772ebe643c15`；ko `content8.py` `4bc39dd9cd8b` → `2dd2165798fa`；core `content56.py` `0e899c29f927` → `cb7953ede458`；zh-tw `content56.py` `29dedee9e721` → `1a427816056f`。

### 1.2 apply 过程中的一次断言失误（已纠正，无源头影响）

- `apply4.py` 首次运行：pt/ja/ko 9 处编辑全部通过后，在 core-ru 断言失败停止——我把 `折扣码` 的“全版 content 文件计 ×5”误写成单文件 `content56.py` 的新串原先计数，实际该文件内为 ×2（L71、L89）。这是我写错的期望值，不是源头问题：core 与 zh-tw 源文件当时尚未改动。
- 处理：修正 `apply4.py` 中两处期望值为 2，另写 `apply4-rest.py` 只跑剩余 core + zh-tw 两处（同一断言逻辑），两处均通过（core `0e899c29f927` → `cb7953ede458`、zh-tw `29dedee9e721` → `1a427816056f`，旧串行号均为 85）。pt/ja/ko 9 处未重复执行。

### 1.3 J-6 共享核查（修 core 前已确认，修后复核）

- 修前：`促销码` 在其余 9 版 content 文件中 0 处；各版 `content56.py:85` 均为独立的本语选项表（en `promo code a`、de `Rabattcode a`、es `código promocional a`、fr `code promo a`、it `codice promozionale a`、pt `código promocional a`、nl `kortingscode a`、ja `プロモコード a`、ko `프로모 코드 a`），core 源头不被他版共享；`ru-p8.json` 不含 `促销码`，Q77 键为字母 `a`（`ru-p8.json:234`）。
- 修后全量指纹对照（`verify4.py`，修前 34 文件快照 vs 盘上实测）：变化的 16 个文件恰为本轮 5 版的印/网 PDF + text.md（core 两份 text.md 计 2 个）；其余 6 版（en/de/es/fr/it/nl）的印/网 PDF 与 text.md SHA 与修前指纹逐一核对不变。core 修复无外溢。
- 其余 9 版 Q77 选项 a 标均与其版内规范形一致，未动。

## 2. 重渲染记录（`driver.sh`，`logs/`、`build-*.log`）

| 步骤 | ru-pt（20:41–20:46 UTC） | ru-ja（20:46–20:54 UTC） | ru-ko（20:54–21:01 UTC） | ru-zh-tw（21:01–21:07 UTC） | core-ru（21:07–21:09 UTC） |
|---|---|---|---|---|---|
| `run.py` | rc=0，TOTAL 150，zero FLOW OVERFLOW / HEAD TOO WIDE | rc=0，TOTAL 150，同左 | rc=0，TOTAL 150，同左 | rc=0，TOTAL 150，同左 | rc=0，TOTAL 150，同左 |
| `render.py` | rc=0；印 PDF mtime 20:44:07 UTC，20,883,714 B | rc=0；印 PDF mtime 20:50:34 UTC，27,365,839 B | rc=0；印 PDF mtime 20:58:18 UTC，21,975,394 B | rc=0；印 PDF mtime 21:04:21 UTC，24,763,427 B | rc=0；印 PDF mtime 21:08:47 UTC，24,713,343 B |
| `ru_textmd.py` 干跑 | rc=0（`/tmp/fix4-dryrun/`） | rc=0 | rc=0 | rc=0 | rc=0 |
| `backfill4.py` | rc=0：干跑丢 4 行标题（与 2b/F-2/补修 3 同批：L45–46 `### СМИ · O QUE DIZEM OS MEDIA` + 空行、L449 `### ЗА И ПРОТИВ · PRÓS E CONTRAS` + 空行），已原位置逐字回补 | rc=0：干跑无丢行 | rc=0：干跑无丢行 | rc=0：干跑无丢行 | rc=0：干跑无丢行 |
| text.md 落盘 | SHA `67ced8562a71…`，65,102 B；diff vs 修前快照恰 4 行对（L476/L477/L768/L769） | SHA `465a2e4ebcd8…`，64,504 B；diff 恰 9 行对（L420/L476/L477/L525/L655/L759/L768/L769/L833） | SHA `050d18839631…`，65,030 B；diff 恰 9 行对（同 ja 行号） | SHA `948538470d3c…`，60,855 B；diff 恰 2 行对（L413/L757） | SHA `2a38d3dab649…`，60,953 B；diff 恰 2 行对（L413/L757）；两份 text.md（core + zh-cn）同步落盘、字节一致（`cmp` 已验） |
| `webpdf.py` | rc=0；网 PDF mtime 20:46:30 UTC，3,337,256 B | rc=0；网 PDF mtime 20:54:16 UTC，3,692,713 B | rc=0；网 PDF mtime 21:01:21 UTC，3,494,572 B | rc=0；网 PDF mtime 21:07:18 UTC，3,975,999 B | rc=0；网 PDF mtime 21:09:58 UTC，3,898,280 B |
| SVG 变动（vs 修前快照 `sha256sum -c`） | 仅 p8 变，p1–p7 不变 | p7 + p8 变，其余不变 | p7 + p8 变，其余不变 | 仅 p8 变，p1–p7 不变 | 仅 p8 变，p1–p7 不变 |

- 附记：`run.py`/`render.py` 会重写全部 8 个 SVG 与 8 张 cards PNG 的 mtime；内容级比对（`sha256sum -c`）证明仅上表所列 SVG 内容变化——与 2b/2c/补修 3 同一行为。SVG 变动页与改动位置一致：pt/ core/ zh-tw 的改动全在 P8（Q77/Q86/Q87 key 与答案区）；ja/ko 另有 P7 B1 词表行。

## 3. 印/网核验（`verify4.py`，全部 PASS）

- 印/网 PDF 各 8 页；印/网提取文字（归一化空白后）一致：pt 37,883 字符、ja 32,161、ko 32,173、core 31,503、zh-tw 31,407。
- text.md 新串行数与旧串清零（`verify4.py` 逐版断言）：

| 版 | text.md 新串 | text.md 旧串 | 印 PDF 新串 / 旧串 | 网 PDF 新串 / 旧串 |
|---|---|---|---|---|
| ru-pt | `Dados de prática` ×6 行 | `Dados de exercício` ×0 | `Dados de prática` ×3 / ×0 | 同印 |
| ru-ja | `練習用データ` ×7 行、`プロモコード` ×11 行 | `練習データ` ×0、`割引コード` ×0 | `練習用データ` ×4、`プロモコード` ×6 / 旧 ×0 | 同印 |
| ru-ko | `연습용 자료` ×7 行、`프로모 코드` ×11 行 | `연습 데이터` ×0、`할인 코드` ×0 | 去空格提取 `연습용자료` ×4、`프로모코드` ×6 / 旧 ×0 | 同印 |
| core-ru | `折扣码` ×11 行 | `促销码` ×0 | `折扣码` ×6 / ×0 | 同印 |
| ru-zh-tw | `折扣碼` ×11 行 | `促銷碼` ×0 | `折扣碼` ×6 / ×0 | 同印 |

- ko 注：印/网 PDF 文字层提取丢韩文词内空格（PROOF-NOTE-4 已记：`연습용자료`、`프로모코드`），故 ko 的 PDF 层计数按去空格形式核验；text.md 层按带空格原形计数（×7/×11），旧串去空格形亦为 ×0。
- 字符数变化与改动一致：pt 归一化 37,887（补修 3 终值）→ 37,883（−4：`exercício`→`prática` 每处 −2 字符 × 印 PDF 层 2 处）；ja/ko/core/zh-tw 的归一化字符数与 PROOF-NOTE-4 原始计数的差恰为去空格提取的 7 字符（pt/ja/ko/core/zh-tw 原始−归一化均为 7）加上本次改动的字符差（ja +5、ko +3、core/zh-tw 0）。
- core 两份 text.md 字节一致（SHA 相同，见 §4）。

## 4. 新旧 SHA 对照（盘上实测全值；网 PDF SHA 为本次重建实时值）

### ru-pt

| 文件 | 改前 SHA-256 | 改后 SHA-256 | 字节（改前 → 改后） |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-pt.pdf` | `7624d63eec28dc6eaba2b41ada0cadd6c58743469fc42c0d51cb56093755db89` | `de64a14d7ce5f49fa92f559d3fb9e33d0a345826fa0da6a66c4b42e3fab21ff3` | 20,883,723 → 20,883,714 |
| 网 PDF `Lucerna-VOL4-ru-pt-web.pdf` | `a8773dcdbcdcd05d1397fbaf8136fb529945dd45f5ac1fa4b8e83241a1ba67b8` | `a8c1afb037223c476adf5fb76a7c6ac942fa852419da2bddb21fab45f989c079` | 3,337,277 → 3,337,256 |
| text.md `2026-w47-ru-pt.text.md` | `93b60dc2d78d1bd260660826585800a460d47d28ee45e7f6432096868e55ff53` | `67ced8562a719470ecce14fc4d19319413754416ee2105212aed2e3e07931e50` | 65,110 → 65,102 |
| `content56.py` | `23e50a584e0c…` | `d899320e8b7e…` | — |

### ru-ja

| 文件 | 改前 SHA-256 | 改后 SHA-256 | 字节（改前 → 改后） |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-ja.pdf` | `f65820348befa4fff7103b816fe4195dd9951f54ae04cb9730916957a3f7e40d` | `bc7bccfe15ca1813f1996794361e1cfd3f71c98f11b4e5af4105e3ec1112f355` | 27,365,531 → 27,365,839 |
| 网 PDF `Lucerna-VOL4-ru-ja-web.pdf` | `b6fed518a3c1ad5ec845ae5dbb8c61b3599e55a9c6a106478136670a4f1ea801` | `dc9f27b03891763b1c986b31a70cca0ef50b77442e632ee63fd600cad9b27c8c` | 3,692,485 → 3,692,713 |
| text.md `2026-w47-ru-ja.text.md` | `2a298d44abc5e5129f5d1b235746e745ce28d9fad5b9769529a3a11146f7605c` | `465a2e4ebcd87b0f638609f9af1fc4d7a830e9a1b2a83bbdb7eb73efb7568f4d` | 64,477 → 64,504 |
| `content56.py` | `c31748b5bc42…` | `b7ad19227d7b…` | — |
| `content7.py` | `12111e2d070e…` | `93198cf987cc…` | — |
| `content8.py` | `2a499204cd8e…` | `310dad0a36fb…` | — |

### ru-ko

| 文件 | 改前 SHA-256 | 改后 SHA-256 | 字节（改前 → 改后） |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-ko.pdf` | `d97e04c036d6c6d6007619565ce12d94b3cce4812b0310c4a3566ff0c1a82c9d` | `fece66f1bfec2ff1f104ad5cbf820745281100ace7348072ee4997f48ed16c73` | 21,975,345 → 21,975,394 |
| 网 PDF `Lucerna-VOL4-ru-ko-web.pdf` | `90059d0d6f401faf3c05ccc68e3076c21beed4c2f4dc0689ec20251d7ee1c025` | `a6a997780723540d904e4d86c2203bb9191362bd3a0124e707e3f3a660bedf6d` | 3,494,537 → 3,494,572 |
| text.md `2026-w47-ru-ko.text.md` | `5e34a2c5d29e1e858b6043f6f52ccb457a2a100171180c043518936a2a8279b5` | `050d188396312cab8e3a8544614799c1f44377a559a51043dfbfc6818e544b71` | 65,015 → 65,030 |
| `content56.py` | `2f44fd5aa472…` | `9afe06c6c75f…` | — |
| `content7.py` | `9b2ce3db8fc2…` | `772ebe643c15…` | — |
| `content8.py` | `4bc39dd9cd8b…` | `2dd2165798fa…` | — |

### core-ru

| 文件 | 改前 SHA-256 | 改后 SHA-256 | 字节（改前 → 改后） |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4.pdf` | `e3c4c0ee155a96a96a56a70326e4df0e0572705e2fff3457599f361b929b60bf` | `a114f1d24694fc11f07d32611111c0b2d508a64d1f970e0c8cb080530533f466` | 24,713,345 → 24,713,343 |
| 网 PDF `Lucerna-VOL4-web.pdf` | `0bdc87e621d75bb35d4a507463237fa05748dfaf1e67090926e68afb58ba45af` | `e37922c048d1a46e32fc0e7e13f6e91e236445f43a5937b9d7c67c63f2dfe195` | 3,898,257 → 3,898,280 |
| text.md `2026-w47-ru-core.text.md` | `a54372a10afc91761f6a8e21a597b7ce2f001c80987f51b3b9789e795ad62c9e` | `2a38d3dab649320e9480ef3b6b3a1824f3cdfd35de822594dabd81f34494a353` | 60,953 → 60,953 |
| text.md `2026-w47-ru-zh-cn.text.md` | `a54372a10afc91761f6a8e21a597b7ce2f001c80987f51b3b9789e795ad62c9e` | `2a38d3dab649320e9480ef3b6b3a1824f3cdfd35de822594dabd81f34494a353` | 60,953 → 60,953 |
| `content56.py` | `0e899c29f927…` | `cb7953ede458…` | — |

### ru-zh-tw

| 文件 | 改前 SHA-256 | 改后 SHA-256 | 字节（改前 → 改后） |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-zh-tw.pdf` | `7db5bece16d64a47984db6babcf58a65ffbd5206334281f9f53afd84a157a069` | `0c4bffc78bdc7aaf8285519d94816124b8ffbc3fe936ae1bc4f0a69a93a1748d` | 24,763,429 → 24,763,427 |
| 网 PDF `Lucerna-VOL4-ru-zh-tw-web.pdf` | `31a07aa54b5aef2b874ca2b37b4234749fc0135691c44390368c133e89d132c8` | `cc348ad4ae16b6f3989b6d7c3966e7f543b658838d1ec3a71817793620ecb462` | 3,976,005 → 3,975,999 |
| text.md `2026-w47-ru-zh-tw.text.md` | `bc0a26a5267ffe9e247d8a52c62e825a80437d986cfc0a529d48ee999d1d8a7b` | `948538470d3cbfb3b0110300daf89c382ce4f555e08567bd1b961c8fcff52e0e` | 60,855 → 60,855 |
| `content56.py` | `29dedee9e721…` | `1a427816056f…` | — |

改前 SHA 与 PROOF-NOTE-4 指纹逐一核对一致。core/zh-tw text.md 字节不变（`促销码`→`折扣码`、`促銷碼`→`折扣碼` 均为等长替换）。

## 5. 门禁（修后重跑，`gates/`，全部 rc=0）

| 门禁 | ru-pt | ru-ja | ru-ko | core-ru | ru-zh-tw |
|---|---|---|---|---|---|
| `p8.py compare --total 150` | **CLEAN**：150/150，missing=[]，extra_count=0，keydiff=[137, 138, 139, 140]（E 节翻译题，预期） | **CLEAN**：同左 | **CLEAN**：同左 | —（核心为比对基准；改跑 `p8.py extract` **150/150**，提取键与生产 `ru-p8.json` 逐键一致，`ru-p8.json` 未改写） | **CLEAN**：同左 |
| `occlusion_audit.py`（svg/） | **0 flags** | **0 flags** | **0 flags** | **0 flags** | **0 flags** |
| `boxtitle_check.py` | **0 DEFECT、0 OBSERVE、0 marginal**（57 标题、683 正文行） | **0 DEFECT、0 OBSERVE、0 marginal**（57 标题、716 正文行） | **0 DEFECT、0 OBSERVE、0 marginal**（67 标题、759 正文行） | **0 DEFECT、0 OBSERVE、0 marginal**（57 标题、704 正文行） | **0 DEFECT、0 OBSERVE、0 marginal**（57 标题、703 正文行） |
| `spill_sweep.py` | **rc=0**（0 SPILL；1 条既有 `[observe]`：Black Friday gloss 行 `= grande saldo.`，同 2b/2c/补修 3，非新缺陷） | **rc=0**（0 SPILL；1 条既有 `[observe]`：同式 `大セール。`） | **rc=0**（0 SPILL；1 条既有 `[observe]`：同式 `.`） | **rc=0**（0 SPILL；1 条既有 `[observe]`：同式 `急。`） | **rc=0**（0 SPILL；1 条既有 `[observe]`：同式 `大促銷，要計劃，別急。`） |
| `pdf_edge_scan.py`（印 PDF） | **0 TOUCH、0 NEAR**（8 页） | **0 TOUCH、0 NEAR**（8 页） | **0 TOUCH、0 NEAR**（8 页） | **0 TOUCH、0 NEAR**（8 页） | **0 TOUCH、0 NEAR**（8 页） |
| `head_check.py`（vs 本次 run.log） | **PASS 0 defects** | **PASS 0 defects** | **PASS 0 defects** | **PASS 0 defects** | **PASS 0 defects** |
| D5 census（`scratch-reproof2-w47-ru/census.py`，11 版全量） | **CJK+Latin=0、CJK+Cyrillic=0，全部 11 版**；本版弯引号 2 处全部 Newsreader（runs 5721） | 同左；本版弯引号 2 处全部 Newsreader（runs 6218） | 同左；本版弯引号 2 处全部 Newsreader（runs 6871） | 同左；本版弯引号 4 处全部 Newsreader（runs 6244） | 同左；本版弯引号 4 处全部 Newsreader（runs 6242） |
| 引号普查（`census_quotes.py`，本版 svg） | **GRAND TOTAL defective: 0** | **GRAND TOTAL defective: 0** | **GRAND TOTAL defective: 0** | **GRAND TOTAL defective: 0** | **GRAND TOTAL defective: 0** |

- 注：`census_quotes.py` 在 `scratch-gatefix-u201c-ru/` 盘上存在，本次 5 版均跑过、均为 0 缺陷；D5 弯引号计数仍以 `census.py` 为准（与 PROOF-NOTE-4 口径一致：core 4、en 2、de 3、es 2、fr 4、it 2、pt 2、nl 2、ja 2、ko 2、zh-tw 4）。
- 门禁驱动 `gates4.sh` 2026-11-12 21:10:36–21:13:36 UTC 全程 rc=0；`gates/summary.txt` 为逐项记录。

## 6. KIT 更新记录（`update_kit.py`，断言计数，全部通过）

- ru-pt：§5 印/网行（L53–54）改为 §4 改后实测值，§5 text.md 字节数 65,110 → 65,102；§7 列表末追加补修 4 条目（L94）；历史条目未动。
- ru-ja：§5 印/网行（L53–54）改为 §4 改后实测值，§5 text.md 字节数 64,477 → 64,504；§7 列表末追加补修 4 条目（L95，J-2 + J-3 两项）；历史条目未动。
- ru-ko：§5 印/网行（L53–54）改为 §4 改后实测值，§5 text.md 字节数 + SHA（65,015 → 65,030）同步；§7 列表末追加补修 4 条目（L96，J-4 + J-5 两项）；历史条目未动。
- core-ru：§9 交付状态印/网行（L161–162）改为 §4 改后实测值（指引由“见 §7.7”改为“见 §7.9”；文本层 56,087 字节经 `pdftotext` 实测不变，保留）；§5 text.md 字节数（60,953）与 §9 text.md 行字节数不变，无需改；§7 末新增 `### 7.9 补修 4` 小节（L150，含 J-6 共享核查与无外溢核查）；§7.7 D5 段等历史条目未动。另修了一个格式问题：§7.9 标题前补空行、§8 前双空行并为单空行（仅空白字符）。
- ru-zh-tw：§1 文件表印/网/text.md 三行（L13–15）改为 §4 改后实测值；文末新增 `## 13. 第四輪修復` 一节（J-6）；§9/§11/§12 历史条目未动。
- KIT 更新后 `verify4.py` 复跑仍 ALL PASS（指纹仍为恰 16 文件变化；KIT 文件不在指纹快照内，但 §5/§1/§9 行已与盘上实测值逐一核对一致）。

## 7. 收尾核对

- 触碰范围：`production/2026-w47/` 的 `2026-w47-ru-pt`、`2026-w47-ru-ja`、`2026-w47-ru-ko`、`core-ru`、`2026-w47-ru-zh-tw`（各源头 content*.py、SVG、印/网 PDF、text.md、WEEKLY-KIT.md）+ 本 scratch 目录；其余家庭/周、SOP、lint 均未碰；未 commit、未 push。
- 进程：本次构建为 5 版串行，无需杀进程；未杀任何进程。
- 磁盘收尾 95G 已用（门限 100G，未触发）。
- 干跑/终版中间件在 `/tmp/fix4-dryrun/`、`/tmp/fix4-final/`（临时件，VM 重启即失）；修前快照 `pre-2026-w47-ru-*.text.md`、`pre-*-svg.sha256` 与 `pre-fingerprint.txt` 留在本目录。
