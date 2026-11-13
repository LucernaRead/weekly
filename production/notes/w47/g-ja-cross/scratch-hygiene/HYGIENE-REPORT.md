# W47 Hygiene 报告 — fanout-nl / 仓根 hidden_files/w47

执行时间：2026-11-12（UTC 约 12:00–13:00，EST 07:00–08:00）。执行者：hygiene 工人。
硬约束遵守：只动这两处；未碰 W43/W45/W46、未动正典版目录内容（只读比对）、未动 covers/tools/issues；无 reset/stash/add/commit/push，未跑 lint。
磁盘：开工 `df` 93G 已用（150G 总，63%），未触 ≥100G 停手线。完工 93G（96,885,980 KB）。

## 结论先行

- **任务 1 fanout-nl/：未删、未移。停手待协调员定夺。** 逐字节比对完成：10 个子目录、0 个唯一文件；但 9 个已追踪 `.text.md` 中 8 个与正典不同，触发任务书明文停手条件（“不同则先报告停手”）。差异方向已证实为正典更新（见 §1.3 逐项证据：Q140 `kort gedicht` 修正 + 间距修正、mtime、KIT 内生产 SHA、`_D5_READER`），fanout-nl 不含正典所缺内容；删除仍需协调员一句话授权。
- **任务 2 仓根 hidden_files/w47/：完成。** 664 个文件全部处理：10 个字节相同→删除；7 个不同→移入目标并加 `-repo` 后缀；647 个目标位置没有→移入目标对应位置。654/654 移入目的地已验存在。仓根 `hidden_files/` 空目录已 rmdir，`git status --porcelain` 不再出现 hidden_files。
- **释放空间：仅 ~95 KB。** 任务 2 的 647+7 个文件是同一文件系统内 `mv`（仓内→目标 hidden_files），不释放磁盘；10 个删除文件共 94,967 B。fanout-nl 301 MB 未动，故磁盘仍为 93G。

## 1. 任务 1 — production/2026-w47/fanout-nl/

### 1.1 背景核实（run-log.md）

- run-log L3437–L3441（pre-insert wave-1 第三报）：fanout-nl 是 11-11 14:26 UTC 旧重扩散版；正典直接目录是 17:08–21:05 UTC fix1/delta 落地的更新定稿版；10 版 30 项中有 29 项 SHA 对不上，移动会回退 D6–D11 等修正，停下条件生效。
- run-log L4223–L4227（nl 家庭验收，协调员 #3 盘上核实）：第二工人在顶层生产重做 9 版、第三工人只做 nl-zh-tw；11/11 版印/网/text.md 尺寸+SHA 前 12 与汇报一致，svglib.py 含 `_D5_READER`（11/11），KIT 含生产实际印/网 SHA；nl 家庭 ACCEPTED（12/12 含 core-nl）。
- run-log L4256（收尾线）：“核实与正典目录重复后删除”。
- 正典目录：`production/2026-w47/2026-w47-nl-{de,en,es,fr,it,ja,ko,pt,ru,zh-tw}/` + `core-nl/`。

### 1.2 逐字节比对总表（SHA-256 全量）

| fanout 子目录 | 文件数 | 总字节 | IDENTICAL | DIFFERS | UNIQUE（正典无此文件） | 仅正典有 |
|---|---|---|---|---|---|---|
| 2026-w47-nl-de | 44 | 27840108 | 30 | 14 | 0 | 0 |
| 2026-w47-nl-en | 46 | 27706997 | 35 | 11 | 0 | 0 |
| 2026-w47-nl-es | 44 | 27770662 | 19 | 25 | 0 | 0 |
| 2026-w47-nl-fr | 44 | 27734981 | 31 | 13 | 0 | 0 |
| 2026-w47-nl-it | 44 | 27715958 | 31 | 13 | 0 | 0 |
| 2026-w47-nl-ja | 44 | 42742284 | 14 | 30 | 0 | 0 |
| 2026-w47-nl-ko | 44 | 33489927 | 15 | 29 | 0 | 0 |
| 2026-w47-nl-pt | 44 | 27800593 | 31 | 13 | 0 | 0 |
| 2026-w47-nl-ru | 44 | 28671599 | 16 | 28 | 0 | 1 |
| 2026-w47-nl-zh-tw | 44 | 42632440 | 15 | 29 | 0 | 0 |
| **合计** | **442** | **314105549** | **237** | **205** | **0** | **1** |

唯一仅正典有的文件：`2026-w47-nl-ru/svglib.py.orig`（D5 移植备份件，在正典内，不受影响）。
**UNIQUE = 0：fanout-nl 里没有任何一个文件是正典目录所没有的。**

### 1.3 停手条件触发：9 个已追踪 .text.md 的比对

`git status` 中 9 个 M 文件（.text.md）与正典同名文件比对：

| 版 | fanout 大小/SHA12 | 正典大小/SHA12 | 结论 |
|---|---|---|---|
| nl-de | 46214B 7d6eee03b87a | 46226B c1342c3fe20d | DIFFERS |
| nl-en | 45106B 05513522b585 | 45115B 9596c4acbb27 | DIFFERS |
| nl-es | 47649B 44fc3d5c4287 | NoneB  | IDENTICAL |
| nl-fr | 47739B 21888192450f | 47744B f1d1154442c4 | DIFFERS |
| nl-it | 47049B 62142f938c6a | 47060B f1d9e3f58b82 | DIFFERS |
| nl-ja | 47796B e890ba135c8c | 47801B 060bfdea2434 | DIFFERS |
| nl-ko | 47580B 1d103d29fcbd | 47585B 75fbaa3004d0 | DIFFERS |
| nl-pt | 47204B 865e659fc2d4 | 47209B 7e6b0c54dcb2 | DIFFERS |
| nl-ru | 57848B 558786fc6247 | 57870B f23da475ff54 | DIFFERS |
| nl-zh-tw（?? 未追踪） | 44315B 54d20ccd80af | 44320B 30af89dfbfe2 | DIFFERS |

**8/9 已追踪 .text.md 为 DIFFERS，仅 nl-es 相同 → 任务书停手条件触发，fanout-nl 全数保留，未删未移。**

差异内容的逐项核查（`diff fanout → 正典`，证明差异方向为正典更新、fanout 为旧版）：

- 全部 8 个差异版共用同一处改动：第 140 题答案 `Ik maak een surprise met een gedicht` → `Ik maak een surprise met een kort gedicht`（各版题干亦同步加 `kort`/短诗限定词）；nl-en 另有 2 处间距修正（`groepswinst=group` → `groepswinst = group`、`gedicht=poem` → `gedicht = poem`）。除此之外 8 版 text.md 再无任何差异行。
- mtime：fanout text.md 2026-11-11 12:40–13:48；正典 text.md 2026-11-11 17:53–19:16（正典更新）。
- HEAD 对照：9 个 .text.md 的 HEAD 版 SHA 与 fanout 工作版、正典版三者全不相同（HEAD 为更旧版）；正典 .text.md 在 git 中为 `??`（未追踪的新版）。
- KIT 互证（nl-de 为例）：正典 KIT 含正典印 PDF SHA `97420549c81e…`，不含 fanout 印 PDF SHA `dc567b1a5a7a…`；fanout KIT 含 fanout 自身 SHA，不含正典 SHA。
- svglib.py：正典 10/10 含 `_D5_READER`；fanout 拉丁 7 版各含 5 处 `_D5` 标记（与正典同数，差异仅 fix2 注释措辞，无机制差异），ja/ko/zh-tw 的 fanout 版为 0 处（未移植 D5，正典 5 处）。fanout svglib 不含正典所缺的任何机制。
- 其余 DIFFERS 文件（PDF/网 PDF/KIT/content*.py/bslib4.py/cards/*.png/svg/*.svg/__pycache__）均为同一版本的重建输出或源码加修复，无一是正典所缺的独立内容；ja/ko/zh-tw 的印 PDF 尺寸差大（fanout ~26MB → 正典 ~13.9–18.8MB）系 D5 重建所致。
- 安全网：目标 hidden_files 下 `scratch-refanout-nl/`（573 个文件，含 `backup/`）仍在，重扩散前旧版另有备份。

### 1.4 差异文件全清单（DIFFERS，按子目录）

#### 2026-w47-nl-de（14 个 DIFFERS）

- `2026-w47-nl-de/2026-w47-nl-de.text.md` — fanout 46214B sha 7d6eee03b87a；正典 46226B sha c1342c3fe20d
- `2026-w47-nl-de/De-Lucerna-VOL4-nl-de-web.pdf` — fanout 1536341B sha 1259cb64766b；正典 1536341B sha 2361bedfd4d5
- `2026-w47-nl-de/De-Lucerna-VOL4-nl-de.pdf` — fanout 12104226B sha dc567b1a5a7a；正典 12104230B sha 97420549c81e
- `2026-w47-nl-de/WEEKLY-KIT.md` — fanout 11191B sha 4ea8dc0064db；正典 21289B sha 478dc86a9dbc
- `2026-w47-nl-de/__pycache__/bslib4.cpython-312.pyc` — fanout 19084B sha d627e64272a3；正典 19085B sha 6fbcd63afeaf
- `2026-w47-nl-de/__pycache__/svglib.cpython-312.pyc` — fanout 44314B sha 7cb1b7c602b1；正典 44304B sha 57a3ffc80bb6
- `2026-w47-nl-de/bslib4.py` — fanout 10143B sha 6119be24bed4；正典 10384B sha d8f485003abd
- `2026-w47-nl-de/cards/p8-toets.png` — fanout 1224047B sha f155995e60fb；正典 1224587B sha 128242fff377
- `2026-w47-nl-de/content34.py` — fanout 15154B sha 4450d7ac6037；正典 15111B sha c8af41173bcf
- `2026-w47-nl-de/content56.py` — fanout 17246B sha bb154997de5a；正典 17370B sha b06cc6b8a998
- `2026-w47-nl-de/content7.py` — fanout 10843B sha 2245b3431988；正典 11054B sha 07a0ea3a520f
- `2026-w47-nl-de/content8.py` — fanout 10818B sha 910ba4b2049c；正典 10830B sha f995c22c33be
- `2026-w47-nl-de/svg/p8-toets.svg` — fanout 193195B sha 3f15844dc3d6；正典 193207B sha 47b4e0010c2e
- `2026-w47-nl-de/svglib.py` — fanout 24004B sha 25291c18d58e；正典 23837B sha a8e2f725fbf5

#### 2026-w47-nl-en（11 个 DIFFERS）

- `2026-w47-nl-en/2026-w47-nl-en.text.md` — fanout 45106B sha 05513522b585；正典 45115B sha 9596c4acbb27
- `2026-w47-nl-en/De-Lucerna-VOL4-nl-en-web.pdf` — fanout 1534341B sha a35d66b1b7c6；正典 1534348B sha db7a9ace064a
- `2026-w47-nl-en/De-Lucerna-VOL4-nl-en.pdf` — fanout 12102278B sha ff89c908aa2f；正典 12102271B sha d87a5242afec
- `2026-w47-nl-en/WEEKLY-KIT.md` — fanout 17385B sha 3a3da8ba0932；正典 25972B sha 08d5ae5d29ec
- `2026-w47-nl-en/__pycache__/bslib4.cpython-312.pyc` — fanout 19033B sha 2b98fba23e72；正典 19034B sha adf4dc00f79c
- `2026-w47-nl-en/__pycache__/svglib.cpython-312.pyc` — fanout 44314B sha b14a8be086d9；正典 44304B sha 07e4e910287b
- `2026-w47-nl-en/bslib4.py` — fanout 10111B sha b280a5012436；正典 10311B sha 175b2336396f
- `2026-w47-nl-en/cards/p8-toets.png` — fanout 1170981B sha bdbd3c6ec4bb；正典 1171252B sha bcf49437d989
- `2026-w47-nl-en/content34.py` — fanout 14891B sha 212c01a5a545；正典 14940B sha d1ff2a197500
- `2026-w47-nl-en/content8.py` — fanout 10654B sha 5a1cdea5407e；正典 10663B sha 3c2e5e8327e9
- `2026-w47-nl-en/svg/p8-toets.svg` — fanout 192808B sha b11806f29960；正典 192817B sha eb3f496a8e60

#### 2026-w47-nl-es（25 个 DIFFERS）

- `2026-w47-nl-es/De-Lucerna-VOL4-nl-es-web.pdf` — fanout 1540063B sha 51cf30c34120；正典 1540062B sha 249fda66604b
- `2026-w47-nl-es/De-Lucerna-VOL4-nl-es.pdf` — fanout 12107935B sha a6f787524e60；正典 12107937B sha 2da02d5b3081
- `2026-w47-nl-es/WEEKLY-KIT.md` — fanout 12769B sha 4f10c48a18d4；正典 21444B sha aff516e85b9f
- `2026-w47-nl-es/__pycache__/bslib4.cpython-312.pyc` — fanout 19066B sha 3ff5ec8a8b81；正典 19105B sha 924005361b0b
- `2026-w47-nl-es/__pycache__/svglib.cpython-312.pyc` — fanout 44314B sha 6ccdff30761e；正典 44304B sha 98d2eaec17f5
- `2026-w47-nl-es/bslib4.py` — fanout 10130B sha 61b50b4dfd8d；正典 10971B sha 3d042a1bc926
- `2026-w47-nl-es/cards/p1-voorpagina.png` — fanout 1094757B sha 309d9952f228；正典 1094761B sha 89d6795e0294
- `2026-w47-nl-es/cards/p2-leven.png` — fanout 938636B sha 680f03b70dbb；正典 938632B sha 34ac65749a46
- `2026-w47-nl-es/cards/p3-cultuur.png` — fanout 835518B sha c6dd35e0841a；正典 835515B sha ac0329ed5b25
- `2026-w47-nl-es/cards/p4-sport.png` — fanout 842012B sha 3c04b7f2e128；正典 842011B sha f85c514c0c9f
- `2026-w47-nl-es/cards/p5-jongeren.png` — fanout 918377B sha dc7fb815cb59；正典 918371B sha 1e1afc50a56c
- `2026-w47-nl-es/cards/p6-verdieping.png` — fanout 656820B sha 56e8767a1e36；正典 656815B sha a73464a3fe07
- `2026-w47-nl-es/cards/p8-toets.png` — fanout 1173157B sha 981bd73cc56e；正典 1173160B sha b304656caf4e
- `2026-w47-nl-es/content12.py` — fanout 19407B sha 14379e494d24；正典 19593B sha 32abbaa30d31
- `2026-w47-nl-es/content34.py` — fanout 15487B sha ab038a5674b2；正典 15765B sha ce7e8253fa7b
- `2026-w47-nl-es/content56.py` — fanout 17522B sha db1b523bf0c1；正典 18155B sha 2656cec6fd75
- `2026-w47-nl-es/content7.py` — fanout 10962B sha 1d25dd35072d；正典 11229B sha cfd5187f3bdb
- `2026-w47-nl-es/content8.py` — fanout 10934B sha 5a4c567b1acc；正典 10987B sha cb09af1c24a3
- `2026-w47-nl-es/svg/p1-voorpagina.svg` — fanout 491041B sha e7256584c24f；正典 491041B sha c704488b59a2
- `2026-w47-nl-es/svg/p2-leven.svg` — fanout 379667B sha 421237c282cf；正典 379667B sha 74691e22c34b
- `2026-w47-nl-es/svg/p3-cultuur.svg` — fanout 983216B sha 22692bb9a5ed；正典 983216B sha e8c9c2634008
- `2026-w47-nl-es/svg/p4-sport.svg` — fanout 382789B sha 3e0a51f59592；正典 382789B sha f6d83cfd070b
- `2026-w47-nl-es/svg/p5-jongeren.svg` — fanout 406188B sha f565b7946007；正典 406188B sha 8ca34e5d3bae
- `2026-w47-nl-es/svg/p6-verdieping.svg` — fanout 33487B sha ff8e6b0267e4；正典 33487B sha 1a37ff4a07d3
- `2026-w47-nl-es/svg/p8-toets.svg` — fanout 192885B sha 7e496252ec57；正典 192885B sha 0b1a61f7af3c

#### 2026-w47-nl-fr（13 个 DIFFERS）

- `2026-w47-nl-fr/2026-w47-nl-fr.text.md` — fanout 47739B sha 21888192450f；正典 47744B sha f1d1154442c4
- `2026-w47-nl-fr/De-Lucerna-VOL4-nl-fr-web.pdf` — fanout 1538529B sha 50bee8b9a1e5；正典 1538511B sha 1b429a3ff61e
- `2026-w47-nl-fr/De-Lucerna-VOL4-nl-fr.pdf` — fanout 12106426B sha 068386464668；正典 12106421B sha 08f57ec27d86
- `2026-w47-nl-fr/WEEKLY-KIT.md` — fanout 12273B sha ba291433093c；正典 16866B sha 3a2e6ce65036
- `2026-w47-nl-fr/__pycache__/bslib4.cpython-312.pyc` — fanout 19070B sha 03bc9b05d28f；正典 19071B sha 6b826e9a8989
- `2026-w47-nl-fr/__pycache__/svglib.cpython-312.pyc` — fanout 44314B sha 78e616505025；正典 44304B sha 54cacd425899
- `2026-w47-nl-fr/bslib4.py` — fanout 10133B sha 8f3fec9236b6；正典 10396B sha 2ac22bb92c78
- `2026-w47-nl-fr/cards/p8-toets.png` — fanout 1160453B sha 98b914d88c38；正典 1160665B sha 85f36fd645fe
- `2026-w47-nl-fr/content34.py` — fanout 15476B sha c0eb430a063c；正典 15471B sha 696aa32b5ca3
- `2026-w47-nl-fr/content56.py` — fanout 17667B sha 519edce6a2d9；正典 17886B sha bc7d9f4a7b39
- `2026-w47-nl-fr/content7.py` — fanout 11153B sha daff68a51487；正典 11497B sha e0eab839c172
- `2026-w47-nl-fr/content8.py` — fanout 10949B sha b988a2a292b1；正典 10954B sha 9264e8c506d3
- `2026-w47-nl-fr/svg/p8-toets.svg` — fanout 193323B sha c50057f13a21；正典 193328B sha bdb2469c711f

#### 2026-w47-nl-it（13 个 DIFFERS）

- `2026-w47-nl-it/2026-w47-nl-it.text.md` — fanout 47049B sha 62142f938c6a；正典 47060B sha f1d9e3f58b82
- `2026-w47-nl-it/De-Lucerna-VOL4-nl-it-web.pdf` — fanout 1534487B sha 68a23245cc52；正典 1534500B sha 81a3ffaf8e8e
- `2026-w47-nl-it/De-Lucerna-VOL4-nl-it.pdf` — fanout 12102400B sha 5a90aa6d2e77；正典 12102402B sha 675f2bf33c42
- `2026-w47-nl-it/WEEKLY-KIT.md` — fanout 13083B sha 5f085d4a574d；正典 21329B sha 75999b4b1135
- `2026-w47-nl-it/__pycache__/bslib4.cpython-312.pyc` — fanout 19052B sha 38e79d2381ce；正典 19053B sha 4011b70f56db
- `2026-w47-nl-it/__pycache__/svglib.cpython-312.pyc` — fanout 44314B sha c34a8b2dc921；正典 44304B sha 1b545f145979
- `2026-w47-nl-it/bslib4.py` — fanout 10123B sha 9460a8824244；正典 10364B sha d09ddf3bcd39
- `2026-w47-nl-it/cards/p8-toets.png` — fanout 1156010B sha ef3f92db8cae；正典 1156734B sha 0a7fa66858b2
- `2026-w47-nl-it/content34.py` — fanout 15351B sha 0885320669fb；正典 15306B sha 4ebd2f5c8dbf
- `2026-w47-nl-it/content56.py` — fanout 17389B sha 1b29d9347791；正典 17511B sha cdb2c9f643c5
- `2026-w47-nl-it/content7.py` — fanout 10968B sha a25a6efe49b9；正典 11175B sha 623042896320
- `2026-w47-nl-it/content8.py` — fanout 10808B sha f92252c33967；正典 10819B sha 0f71d5ea5cd7
- `2026-w47-nl-it/svg/p8-toets.svg` — fanout 192938B sha 72e210860e78；正典 192949B sha ddcc7ee0d35d

#### 2026-w47-nl-ja（30 个 DIFFERS）

- `2026-w47-nl-ja/2026-w47-nl-ja.text.md` — fanout 47796B sha e890ba135c8c；正典 47801B sha 060bfdea2434
- `2026-w47-nl-ja/ABSTRACT.txt` — fanout 367B sha d199b94ef54a；正典 370B sha 9afb13573022
- `2026-w47-nl-ja/De-Lucerna-VOL4-nl-ja-web.pdf` — fanout 2155388B sha 3c60dddbd2f9；正典 1968007B sha 9a4b3dbd5dad
- `2026-w47-nl-ja/De-Lucerna-VOL4-nl-ja.pdf` — fanout 26049308B sha 40e58eb248ea；正典 18803852B sha 67aeebb40b58
- `2026-w47-nl-ja/WEEKLY-KIT.md` — fanout 6875B sha 013d4a9c58a0；正典 15818B sha 16e3f3d180b5
- `2026-w47-nl-ja/__pycache__/bslib4.cpython-312.pyc` — fanout 19086B sha 13ca7cb199d9；正典 19087B sha 3f67dcfb5593
- `2026-w47-nl-ja/__pycache__/svglib.cpython-312.pyc` — fanout 44346B sha bb3b75e958cf；正典 46093B sha bce1a94ce868
- `2026-w47-nl-ja/bslib4.py` — fanout 10144B sha 6079c2dde384；正典 10385B sha 43c42c0f9570
- `2026-w47-nl-ja/cards/p1-voorpagina.png` — fanout 1105038B sha 0dccf7ed6700；正典 1123773B sha 829d12a1c7b1
- `2026-w47-nl-ja/cards/p2-leven.png` — fanout 979907B sha 86f75f9f726f；正典 993331B sha 180fa103cd74
- `2026-w47-nl-ja/cards/p3-cultuur.png` — fanout 854220B sha 52847951929c；正典 868568B sha a7885bd7754c
- `2026-w47-nl-ja/cards/p4-sport.png` — fanout 847385B sha 06184a396ef0；正典 860139B sha 456947651e44
- `2026-w47-nl-ja/cards/p5-jongeren.png` — fanout 939214B sha 987008b0821e；正典 955226B sha bb256ffa1208
- `2026-w47-nl-ja/cards/p6-verdieping.png` — fanout 684154B sha 01156e6c279f；正典 697289B sha 3e6b422a9e05
- `2026-w47-nl-ja/cards/p7-taal.png` — fanout 1154377B sha 284d9001283f；正典 1185195B sha 166c8bda9842
- `2026-w47-nl-ja/cards/p8-toets.png` — fanout 1360132B sha 1d28ff0a1794；正典 1377135B sha 666f54841a06
- `2026-w47-nl-ja/content12.py` — fanout 19223B sha 1901d481e434；正典 19240B sha 3491dc86d15b
- `2026-w47-nl-ja/content34.py` — fanout 15415B sha af63042aab49；正典 15370B sha 33f81f068b2e
- `2026-w47-nl-ja/content56.py` — fanout 17461B sha 8787f928f136；正典 17651B sha c11875fad0e7
- `2026-w47-nl-ja/content7.py` — fanout 11159B sha 8138e8f8e115；正典 11370B sha 3970deef76f0
- `2026-w47-nl-ja/content8.py` — fanout 11078B sha 52806524b38c；正典 11083B sha 9e56c5734d1b
- `2026-w47-nl-ja/svg/p1-voorpagina.svg` — fanout 491639B sha b1797d8c0cc4；正典 496559B sha 66e067536aad
- `2026-w47-nl-ja/svg/p2-leven.svg` — fanout 375849B sha c03cf813fe1b；正典 382217B sha b4fc43b0de22
- `2026-w47-nl-ja/svg/p3-cultuur.svg` — fanout 979919B sha 2ddeb68fc22a；正典 985802B sha 243e04dc1859
- `2026-w47-nl-ja/svg/p4-sport.svg` — fanout 380102B sha 0dd0671e2001；正典 384601B sha f1cbcb2020f2
- `2026-w47-nl-ja/svg/p5-jongeren.svg` — fanout 404139B sha 314d1983e15d；正典 409179B sha d3eb465b5fd7
- `2026-w47-nl-ja/svg/p6-verdieping.svg` — fanout 30206B sha 8041721716df；正典 35359B sha 6d451ef47496
- `2026-w47-nl-ja/svg/p7-taal.svg` — fanout 365627B sha 4608bb65584b；正典 377194B sha 37bc9f4f8a98
- `2026-w47-nl-ja/svg/p8-toets.svg` — fanout 240764B sha 1b16e2bea302；正典 244322B sha e3b288895be4
- `2026-w47-nl-ja/svglib.py` — fanout 20553B sha d690f310f75b；正典 26427B sha 2dea8ab7aaa6

#### 2026-w47-nl-ko（29 个 DIFFERS）

- `2026-w47-nl-ko/2026-w47-nl-ko.text.md` — fanout 47580B sha 1d103d29fcbd；正典 47585B sha 75fbaa3004d0
- `2026-w47-nl-ko/De-Lucerna-VOL4-nl-ko-web.pdf` — fanout 1919763B sha ed38e32febf2；正典 1791910B sha 694720afc0cc
- `2026-w47-nl-ko/De-Lucerna-VOL4-nl-ko.pdf` — fanout 17281343B sha aaeeba2cb7f5；正典 13871308B sha fd8daad8ba7e
- `2026-w47-nl-ko/WEEKLY-KIT.md` — fanout 5924B sha 8cef799c1f14；正典 13829B sha 9ab2889dbbc0
- `2026-w47-nl-ko/__pycache__/bslib4.cpython-312.pyc` — fanout 19099B sha 7368f82e723e；正典 19100B sha aec360b7e4ce
- `2026-w47-nl-ko/__pycache__/svglib.cpython-312.pyc` — fanout 42552B sha 12752fb5560a；正典 44299B sha af3c60fca867
- `2026-w47-nl-ko/bslib4.py` — fanout 10145B sha 2049a73ee8bb；正典 10386B sha 65f78e1ecb46
- `2026-w47-nl-ko/cards/p1-voorpagina.png` — fanout 1070975B sha f8b4f918b2ca；正典 1090181B sha 27a9a5719100
- `2026-w47-nl-ko/cards/p2-leven.png` — fanout 916556B sha 71b5ebb0c110；正典 935614B sha 1622a6c77d29
- `2026-w47-nl-ko/cards/p3-cultuur.png` — fanout 816496B sha 132a2e4748b4；正典 832075B sha e0a67dfa770c
- `2026-w47-nl-ko/cards/p4-sport.png` — fanout 823661B sha e61e2571310b；正典 841668B sha 2fe8d69e4a2a
- `2026-w47-nl-ko/cards/p5-jongeren.png` — fanout 905652B sha 618dcf7e5828；正典 923742B sha 110a619ce291
- `2026-w47-nl-ko/cards/p6-verdieping.png` — fanout 637400B sha 6639ad437d0f；正典 655633B sha e7991ce9b6af
- `2026-w47-nl-ko/cards/p7-taal.png` — fanout 1104306B sha c2e246588855；正典 1142503B sha a4e5b76772b9
- `2026-w47-nl-ko/cards/p8-toets.png` — fanout 1329062B sha 964d8be983d2；正典 1346439B sha d940be3aebc9
- `2026-w47-nl-ko/content12.py` — fanout 19016B sha b86092d4a7bc；正典 18965B sha 131d242a8ba0
- `2026-w47-nl-ko/content34.py` — fanout 15454B sha f44aae8d0cb4；正典 15408B sha 2080d605f2c8
- `2026-w47-nl-ko/content56.py` — fanout 17480B sha a4ddfabee477；正典 17600B sha e1ae94d2954b
- `2026-w47-nl-ko/content7.py` — fanout 11211B sha 161f2da7644d；正典 11447B sha 7473ac7a8afb
- `2026-w47-nl-ko/content8.py` — fanout 10960B sha 521e14e8926b；正典 10965B sha 16a55990c312
- `2026-w47-nl-ko/svg/p1-voorpagina.svg` — fanout 490528B sha 75d4b7670443；正典 506685B sha 37f44771fbfb
- `2026-w47-nl-ko/svg/p2-leven.svg` — fanout 375422B sha 5f79d8542173；正典 398853B sha 117f962bfcda
- `2026-w47-nl-ko/svg/p3-cultuur.svg` — fanout 979824B sha bbdfd827f92e；正典 995515B sha bd2440fed1ab
- `2026-w47-nl-ko/svg/p4-sport.svg` — fanout 379904B sha 991aa73a98da；正典 394289B sha f6d1d5262866
- `2026-w47-nl-ko/svg/p5-jongeren.svg` — fanout 408471B sha ba648865385d；正典 427945B sha a90a492d42ce
- `2026-w47-nl-ko/svg/p6-verdieping.svg` — fanout 29900B sha 8a5ff2df40e4；正典 51246B sha 93e8ea51afa6
- `2026-w47-nl-ko/svg/p7-taal.svg` — fanout 365556B sha 4cfecc9e1269；正典 405968B sha bb09a66fe3f9
- `2026-w47-nl-ko/svg/p8-toets.svg` — fanout 315852B sha 2261ec0fce53；正典 327548B sha 6aaa10c3a65f
- `2026-w47-nl-ko/svglib.py` — fanout 18125B sha 78df28c455e0；正典 23999B sha 10fe1de39983

#### 2026-w47-nl-pt（13 个 DIFFERS）

- `2026-w47-nl-pt/2026-w47-nl-pt.text.md` — fanout 47204B sha 865e659fc2d4；正典 47209B sha 7e6b0c54dcb2
- `2026-w47-nl-pt/De-Lucerna-VOL4-nl-pt-web.pdf` — fanout 1542934B sha cc34b7b36257；正典 1542946B sha b9e2c0d5b7f2
- `2026-w47-nl-pt/De-Lucerna-VOL4-nl-pt.pdf` — fanout 12110804B sha 773eb8bb3a47；正典 12110806B sha dc43c521becb
- `2026-w47-nl-pt/WEEKLY-KIT.md` — fanout 12454B sha fd24a219d6b2；正典 15648B sha 83b6a19a7c95
- `2026-w47-nl-pt/__pycache__/bslib4.cpython-312.pyc` — fanout 19074B sha f1d997e0177d；正典 19075B sha c18bcb6b2007
- `2026-w47-nl-pt/__pycache__/svglib.cpython-312.pyc` — fanout 44314B sha 062fdb46ae57；正典 44304B sha d7c3ab7f4e9a
- `2026-w47-nl-pt/bslib4.py` — fanout 10134B sha 3c6285fdd0d3；正典 10375B sha 029ae00dda20
- `2026-w47-nl-pt/cards/p8-toets.png` — fanout 1193156B sha d9cc1f1406d1；正典 1193363B sha 6a4f453548f0
- `2026-w47-nl-pt/content34.py` — fanout 15433B sha 8f546e212074；正典 15551B sha b96fe030769e
- `2026-w47-nl-pt/content56.py` — fanout 17464B sha d10b0cf30b94；正典 17648B sha 9f56ddaeef25
- `2026-w47-nl-pt/content7.py` — fanout 10931B sha 2e838ad99760；正典 11203B sha d786d372eec3
- `2026-w47-nl-pt/content8.py` — fanout 10833B sha 4bb4aebd0976；正典 10838B sha fa357d85b5b5
- `2026-w47-nl-pt/svg/p8-toets.svg` — fanout 193347B sha ed59c29b7405；正典 193352B sha 81bcac66a4bb

#### 2026-w47-nl-ru（28 个 DIFFERS）

- `2026-w47-nl-ru/2026-w47-nl-ru.text.md` — fanout 57848B sha 558786fc6247；正典 57870B sha f23da475ff54
- `2026-w47-nl-ru/De-Lucerna-VOL4-nl-ru-web.pdf` — fanout 1780189B sha 566ee0197d9d；正典 1779868B sha 69678fdcdd00
- `2026-w47-nl-ru/De-Lucerna-VOL4-nl-ru.pdf` — fanout 12368014B sha 85e2aa0910c7；正典 12367658B sha 8fa079cbd094
- `2026-w47-nl-ru/WEEKLY-KIT.md` — fanout 11133B sha 3a080a9e267a；正典 15608B sha 2d9eee8a015c
- `2026-w47-nl-ru/__pycache__/bslib4.cpython-312.pyc` — fanout 19169B sha bf98c65eec7a；正典 19170B sha 014a3fdf96a3
- `2026-w47-nl-ru/__pycache__/svglib.cpython-312.pyc` — fanout 44312B sha 0a39cf65f9b6；正典 45632B sha 5e27d78d3b8e
- `2026-w47-nl-ru/bslib4.py` — fanout 10216B sha b45e2bec25dd；正典 10457B sha 0f41bd9cdb93
- `2026-w47-nl-ru/cards/p1-voorpagina.png` — fanout 1085685B sha bd2df3097380；正典 1078727B sha 8b231e818b0d
- `2026-w47-nl-ru/cards/p2-leven.png` — fanout 954954B sha b0e69a61d0f3；正典 957034B sha c1b902d4e45b
- `2026-w47-nl-ru/cards/p3-cultuur.png` — fanout 839470B sha f2e3b61fb5ac；正典 837390B sha df176cbd27d4
- `2026-w47-nl-ru/cards/p4-sport.png` — fanout 845323B sha 87a2d155331e；正典 843085B sha ccf51109987b
- `2026-w47-nl-ru/cards/p5-jongeren.png` — fanout 936685B sha 08bba53e666a；正典 938006B sha 93a10e9fdd6a
- `2026-w47-nl-ru/cards/p6-verdieping.png` — fanout 671960B sha 372eef1069b2；正典 669938B sha 6f5781d7e234
- `2026-w47-nl-ru/cards/p7-taal.png` — fanout 1087525B sha 4f4201b02f1a；正典 1086653B sha 6e5e9d3e5af9
- `2026-w47-nl-ru/cards/p8-toets.png` — fanout 1336842B sha a498281b3041；正典 1339457B sha b35d4128ace3
- `2026-w47-nl-ru/content34.py` — fanout 17875B sha 706c7217c7b9；正典 17832B sha ecc0a59b275c
- `2026-w47-nl-ru/content56.py` — fanout 20325B sha b463abc28e00；正典 20447B sha b5ffc71fa759
- `2026-w47-nl-ru/content7.py` — fanout 12439B sha 7ecfd41b9fd2；正典 12692B sha 68469acd3d6a
- `2026-w47-nl-ru/content8.py` — fanout 12467B sha b8ae519bf1b0；正典 12489B sha af5ef1325d4d
- `2026-w47-nl-ru/svg/p1-voorpagina.svg` — fanout 493887B sha 9205e065c27f；正典 493887B sha 1b1bf7913aae
- `2026-w47-nl-ru/svg/p2-leven.svg` — fanout 380842B sha 0354f0b32be4；正典 380842B sha 3e9f63aa5291
- `2026-w47-nl-ru/svg/p3-cultuur.svg` — fanout 983975B sha 6993f9a95a12；正典 983975B sha a61f06039f3c
- `2026-w47-nl-ru/svg/p4-sport.svg` — fanout 383580B sha 6b74d0a87cc2；正典 383580B sha 64aaf1a09c59
- `2026-w47-nl-ru/svg/p5-jongeren.svg` — fanout 412936B sha a01d3a146b0c；正典 412936B sha d5218dfcb91f
- `2026-w47-nl-ru/svg/p6-verdieping.svg` — fanout 34323B sha 379ed2a94ca6；正典 34323B sha da05d0346e95
- `2026-w47-nl-ru/svg/p7-taal.svg` — fanout 369133B sha 09635bc424bb；正典 369133B sha f5688d779eff
- `2026-w47-nl-ru/svg/p8-toets.svg` — fanout 333312B sha a375fcc02281；正典 333565B sha a22fe79d713b
- `2026-w47-nl-ru/svglib.py` — fanout 24001B sha a8971df65808；正典 26864B sha 9faea6132be3

#### 2026-w47-nl-zh-tw（29 个 DIFFERS）

- `2026-w47-nl-zh-tw/2026-w47-nl-zh-tw.text.md` — fanout 44315B sha 54d20ccd80af；正典 44320B sha 30af89dfbfe2
- `2026-w47-nl-zh-tw/De-Lucerna-VOL4-nl-zh-tw-web.pdf` — fanout 2369193B sha aedb0d6e80fd；正典 1976958B sha 42b892b5c065
- `2026-w47-nl-zh-tw/De-Lucerna-VOL4-nl-zh-tw.pdf` — fanout 25993150B sha 3a81e9cf00ff；正典 13888370B sha 90710eae78ae
- `2026-w47-nl-zh-tw/WEEKLY-KIT.md` — fanout 6511B sha fca346f3ad96；正典 17096B sha 29a0df87687b
- `2026-w47-nl-zh-tw/__pycache__/bslib4.cpython-312.pyc` — fanout 19046B sha 0d090f8f6556；正典 19047B sha 064a5681d236
- `2026-w47-nl-zh-tw/__pycache__/svglib.cpython-312.pyc` — fanout 42552B sha 3a5c6fcdfcc8；正典 44299B sha 641f43c717ed
- `2026-w47-nl-zh-tw/bslib4.py` — fanout 10109B sha 7c2d794bb850；正典 10350B sha 9c535a63b97e
- `2026-w47-nl-zh-tw/cards/p1-voorpagina.png` — fanout 1099891B sha 47333b74a709；正典 1116638B sha 6d6bd7cfaabe
- `2026-w47-nl-zh-tw/cards/p2-leven.png` — fanout 936481B sha c3f158d6e65d；正典 950548B sha 0d4d76ee76a2
- `2026-w47-nl-zh-tw/cards/p3-cultuur.png` — fanout 822660B sha bcbbedb84733；正典 836084B sha d81e6f05d856
- `2026-w47-nl-zh-tw/cards/p4-sport.png` — fanout 833234B sha 27311e0f8d5e；正典 847251B sha a43fc150a48c
- `2026-w47-nl-zh-tw/cards/p5-jongeren.png` — fanout 914663B sha b94109bb1755；正典 931333B sha 875be19256f6
- `2026-w47-nl-zh-tw/cards/p6-verdieping.png` — fanout 651454B sha 5c60d60c3461；正典 667069B sha a6cd7d819717
- `2026-w47-nl-zh-tw/cards/p7-taal.png` — fanout 1118311B sha 8069d0c30e09；正典 1149037B sha 2d7ce0402641
- `2026-w47-nl-zh-tw/cards/p8-toets.png` — fanout 1287382B sha 91cda0a8c3bd；正典 1302259B sha a72a07284b01
- `2026-w47-nl-zh-tw/content12.py` — fanout 18350B sha 95478ba17e47；正典 18299B sha 81f9bea5c330
- `2026-w47-nl-zh-tw/content34.py` — fanout 14766B sha b511a11d6ab0；正典 14754B sha d84d39ee438b
- `2026-w47-nl-zh-tw/content56.py` — fanout 16499B sha 78f415282caa；正典 16644B sha bc959d02e4c2
- `2026-w47-nl-zh-tw/content7.py` — fanout 10615B sha 80c72205c1ee；正典 10951B sha b090c396f185
- `2026-w47-nl-zh-tw/content8.py` — fanout 10326B sha 87e04c368e41；正典 10331B sha 9ca9c89224c1
- `2026-w47-nl-zh-tw/svg/p1-voorpagina.svg` — fanout 490940B sha 58466bb42e8e；正典 495175B sha b668ac66be1a
- `2026-w47-nl-zh-tw/svg/p2-leven.svg` — fanout 375008B sha e825c1779807；正典 381125B sha a049a40e3601
- `2026-w47-nl-zh-tw/svg/p3-cultuur.svg` — fanout 979607B sha 5f1c2ba9c917；正典 985490B sha 3a39b268a0cc
- `2026-w47-nl-zh-tw/svg/p4-sport.svg` — fanout 379572B sha c30c34fefb3f；正典 384433B sha 6d2ef11f9ae2
- `2026-w47-nl-zh-tw/svg/p5-jongeren.svg` — fanout 403445B sha 262cdefa0c0d；正典 408763B sha f1a284f5fc8c
- `2026-w47-nl-zh-tw/svg/p6-verdieping.svg` — fanout 29536B sha 11d070b8699d；正典 35288B sha d35cfb4ee152
- `2026-w47-nl-zh-tw/svg/p7-taal.svg` — fanout 364690B sha e800f905f32f；正典 375940B sha e8f066100a7c
- `2026-w47-nl-zh-tw/svg/p8-toets.svg` — fanout 250343B sha 4eafa835fc88；正典 254578B sha 52592a383dc1
- `2026-w47-nl-zh-tw/svglib.py` — fanout 18122B sha 9c14285e6025；正典 23996B sha 51516324c0fe

### 1.5 任务 1 待协调员定夺

- fanout-nl/ 原样保留：301 MB（`du -sh` 301M），`git status --porcelain -- production/2026-w47/fanout-nl/` 仍为 154 项（145 ?? + 9 M）。
- 建议：协调员确认“8 个 .text.md 差异确为已落地的 fix1/D5 修正、fanout-nl 可删”后，一名工人执行 `rm -rf production/2026-w47/fanout-nl` 即可；9 个已追踪 .text.md 的删除会显示为 git 已追踪文件删除，由后续 commit 处理（本次不 commit）。

## 2. 任务 2 — 仓根 hidden_files/w47/ 移出

仓内源：`~/workspace/weekly-git/hidden_files/w47/`（664 个文件，共 294,039,499 B）。目标：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/`（同名文件逐项 SHA-256 比对，仅比对仓内文件对应的目标路径；目标树共 99,087 个文件，未全量哈希）。

比对结果：IDENTICAL 10 个，DIFFERS 7 个，目标位置没有 647 个。

### 2.1 字节相同 → 删除仓内那份（10 个，共 94,967 B）

- `scratch-proof-de-fr1/keycheck-150.json` — 19187B sha e040dd570492 → 已删除
- `scratch-proof-de-fr1/p8compare.json` — 2136B sha 9ff671d6a6d7 → 已删除
- `scratch-proof-ja-es1/GATE-LOG.md` — 10421B sha 5f78ffbffef1 → 已删除
- `scratch-proof-ja-es1/PROOF-NOTE.md` — 14534B sha f8da51223250 → 已删除
- `scratch-proof-ja-fr1/GATE-LOG.md` — 7121B sha 51e8d432c259 → 已删除
- `scratch-proof-ja-fr1/PROOF-NOTE.md` — 10978B sha 306cb14772e5 → 已删除
- `scratch-proof-ja-it1/GATE-LOG.md` — 4424B sha e4b650cef6de → 已删除
- `scratch-proof-ja-it1/PROOF-NOTE.md` — 8744B sha 3a0cd9e09131 → 已删除
- `scratch-proof-ja-pt1/GATE-LOG.md` — 5917B sha 8485ae0a483f → 已删除
- `scratch-proof-ja-pt1/PROOF-NOTE.md` — 11505B sha 3106d9f72b55 → 已删除

### 2.2 不同 → 移入目标，加 `-repo` 后缀，不覆盖（7 个）

命名：`<原名>-repo<扩展名>`，如 `FANOUT-REPORT-ja.md` → `FANOUT-REPORT-ja-repo.md`。目标原文件原样保留。

- `scratch-fanout-ja/FANOUT-REPORT-ja.md` — 7830B sha 739b3e5e0a6e → `hidden_files/w47/scratch-fanout-ja/FANOUT-REPORT-ja-repo.md`（目标原文件 56224B sha b5bc0bdf3071 保留）
- `scratch-proof-de-fr1/GATE-LOG.md` — 5426B sha dd5fde821346 → `hidden_files/w47/scratch-proof-de-fr1/GATE-LOG-repo.md`（目标原文件 5646B sha af59b247747a 保留）
- `scratch-proof-de-fr1/PROOF-NOTE.md` — 15742B sha baaed5919bb5 → `hidden_files/w47/scratch-proof-de-fr1/PROOF-NOTE-repo.md`（目标原文件 6901B sha 8a2b066ccf22 保留）
- `scratch-proof-de-fr1/freeze-direct.json` — 1180B sha 3103ab6b3d8a → `hidden_files/w47/scratch-proof-de-fr1/freeze-direct-repo.json`（目标原文件 1180B sha 8a0f7e1eb9b6 保留）
- `scratch-proof-de-fr1/freeze.json` — 65641B sha 6d663491d4b9 → `hidden_files/w47/scratch-proof-de-fr1/freeze-repo.json`（目标原文件 65634B sha 870317a912c7 保留）
- `scratch-proof-de-fr1/occlusion.json` — 150B sha 0d6e8eeffc4f → `hidden_files/w47/scratch-proof-de-fr1/occlusion-repo.json`（目标原文件 120B sha 721b653978a4 保留）
- `scratch-proof-de-fr1/p8extract.json` — 4442B sha 1fb005d892e3 → `hidden_files/w47/scratch-proof-de-fr1/p8extract-repo.json`（目标原文件 4475B sha d9d498657f91 保留）

### 2.3 目标位置没有 → 移入目标对应位置（647 个，共 293,849,565 B）

按顶层目录汇总：scratch-webpdf-nl-ru-ja 117、scratch-proof-ja-it1 99、scratch-fix-es-fr1 72、scratch-proof-ja-pt1 63、scratch-proof-ja-fr1 62、scratch-fanout-ja 61、scratch-proof-ja-de1 55、scratch-proof-ja-es1 49、scratch-proof-de-fr1 28、scratch-proof-ja-en1 27、Reports-preinsert 12、probe-nl-en2.txt 1、probe-rebuild-B.txt 1。完整逐项清单：

- `Reports-preinsert/__pycache__/cover_data_w47.cpython-312.pyc` — 155616B sha 2626bcf85c54 → `hidden_files/w47/Reports-preinsert/__pycache__/cover_data_w47.cpython-312.pyc`
- `Reports-preinsert/badge-recount-zh-cn-es.md` — 14301B sha a7dabe9d22ca → `hidden_files/w47/Reports-preinsert/badge-recount-zh-cn-es.md`
- `Reports-preinsert/build_cover_json.py` — 1629B sha ced2b1f49c17 → `hidden_files/w47/Reports-preinsert/build_cover_json.py`
- `Reports-preinsert/build_stills_w47.py` — 5251B sha 109b0314ea6a → `hidden_files/w47/Reports-preinsert/build_stills_w47.py`
- `Reports-preinsert/check_cover_w47.py` — 3844B sha 2a1e9b37c051 → `hidden_files/w47/Reports-preinsert/check_cover_w47.py`
- `Reports-preinsert/core-de-route-merge.md` — 7428B sha 94a923f6d5c7 → `hidden_files/w47/Reports-preinsert/core-de-route-merge.md`
- `Reports-preinsert/cover-seed-excerpts.json` — 2339B sha 4ff4d6d18ace → `hidden_files/w47/Reports-preinsert/cover-seed-excerpts.json`
- `Reports-preinsert/cover_data_w47.py` — 165049B sha 0463eb011505 → `hidden_files/w47/Reports-preinsert/cover_data_w47.py`
- `Reports-preinsert/covers-w47.md` — 11844B sha 8bfbdd1d1393 → `hidden_files/w47/Reports-preinsert/covers-w47.md`
- `Reports-preinsert/extract_w47.py` — 3711B sha a56d8cf50a06 → `hidden_files/w47/Reports-preinsert/extract_w47.py`
- `Reports-preinsert/extract_w47.txt` — 89190B sha 8334283d74c6 → `hidden_files/w47/Reports-preinsert/extract_w47.txt`
- `Reports-preinsert/tools-review-p8-occlusion.md` — 8258B sha 46fdd9bfc979 → `hidden_files/w47/Reports-preinsert/tools-review-p8-occlusion.md`
- `probe-nl-en2.txt` — 34B sha afaadb551663 → `hidden_files/w47/probe-nl-en2.txt`
- `probe-rebuild-B.txt` — 198B sha 4fb2838dd7e3 → `hidden_files/w47/probe-rebuild-B.txt`
- `scratch-fanout-ja/.probe-stick8` — 34B sha 0ba3a6be214d → `hidden_files/w47/scratch-fanout-ja/.probe-stick8`
- `scratch-fanout-ja/build-ko-stick8-run1.log` — 2130B sha 8262deda1561 → `hidden_files/w47/scratch-fanout-ja/build-ko-stick8-run1.log`
- `scratch-fanout-ja/build-ko-stick8-run2.log` — 2130B sha 8262deda1561 → `hidden_files/w47/scratch-fanout-ja/build-ko-stick8-run2.log`
- `scratch-fanout-ja/build-zh-tw-stick8-run1.log` — 2077B sha 80748091b322 → `hidden_files/w47/scratch-fanout-ja/build-zh-tw-stick8-run1.log`
- `scratch-fanout-ja/build-zh-tw-stick8-run2.log` — 2077B sha 80748091b322 → `hidden_files/w47/scratch-fanout-ja/build-zh-tw-stick8-run2.log`
- `scratch-fanout-ja/de-occlusion-stick8.json` — 97B sha ac7a7c5058de → `hidden_files/w47/scratch-fanout-ja/de-occlusion-stick8.json`
- `scratch-fanout-ja/de-p8-stick8.json` — 3797B sha ee0ddcebc800 → `hidden_files/w47/scratch-fanout-ja/de-p8-stick8.json`
- `scratch-fanout-ja/de-p8compare-stick8.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-fanout-ja/de-p8compare-stick8.json`
- `scratch-fanout-ja/de-print.txt` — 46834B sha 3b48160ccaf3 → `hidden_files/w47/scratch-fanout-ja/de-print.txt`
- `scratch-fanout-ja/de-web.txt` — 46834B sha 3b48160ccaf3 → `hidden_files/w47/scratch-fanout-ja/de-web.txt`
- `scratch-fanout-ja/en-occlusion-stick8.json` — 97B sha c2bf557b4312 → `hidden_files/w47/scratch-fanout-ja/en-occlusion-stick8.json`
- `scratch-fanout-ja/en-p8-stick8.json` — 3764B sha 6b8ddab4f83a → `hidden_files/w47/scratch-fanout-ja/en-p8-stick8.json`
- `scratch-fanout-ja/en-p8compare-stick8.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-fanout-ja/en-p8compare-stick8.json`
- `scratch-fanout-ja/en-print.txt` — 46044B sha 4deb424773ef → `hidden_files/w47/scratch-fanout-ja/en-print.txt`
- `scratch-fanout-ja/en-web.txt` — 46044B sha 4deb424773ef → `hidden_files/w47/scratch-fanout-ja/en-web.txt`
- `scratch-fanout-ja/es-occlusion-stick8.json` — 97B sha 7c5ddd539392 → `hidden_files/w47/scratch-fanout-ja/es-occlusion-stick8.json`
- `scratch-fanout-ja/es-p8-stick8.json` — 3753B sha 846e49aae986 → `hidden_files/w47/scratch-fanout-ja/es-p8-stick8.json`
- `scratch-fanout-ja/es-p8compare-stick8.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-fanout-ja/es-p8compare-stick8.json`
- `scratch-fanout-ja/es-print.txt` — 47034B sha f035bf452a0c → `hidden_files/w47/scratch-fanout-ja/es-print.txt`
- `scratch-fanout-ja/es-web.txt` — 47034B sha f035bf452a0c → `hidden_files/w47/scratch-fanout-ja/es-web.txt`
- `scratch-fanout-ja/fr-occlusion-stick8.json` — 97B sha da051761cb1a → `hidden_files/w47/scratch-fanout-ja/fr-occlusion-stick8.json`
- `scratch-fanout-ja/fr-p8-stick8.json` — 3771B sha 059cc4a67e1e → `hidden_files/w47/scratch-fanout-ja/fr-p8-stick8.json`
- `scratch-fanout-ja/fr-p8compare-stick8.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-fanout-ja/fr-p8compare-stick8.json`
- `scratch-fanout-ja/fr-print.txt` — 47208B sha 3438536a1825 → `hidden_files/w47/scratch-fanout-ja/fr-print.txt`
- `scratch-fanout-ja/fr-web.txt` — 47208B sha 3438536a1825 → `hidden_files/w47/scratch-fanout-ja/fr-web.txt`
- `scratch-fanout-ja/it-occlusion-stick8.json` — 97B sha 0c527f034c3e → `hidden_files/w47/scratch-fanout-ja/it-occlusion-stick8.json`
- `scratch-fanout-ja/it-p8-stick8.json` — 3786B sha 1d508b6df889 → `hidden_files/w47/scratch-fanout-ja/it-p8-stick8.json`
- `scratch-fanout-ja/it-p8compare-stick8.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-fanout-ja/it-p8compare-stick8.json`
- `scratch-fanout-ja/it-print.txt` — 47000B sha 4efe03ac6d0c → `hidden_files/w47/scratch-fanout-ja/it-print.txt`
- `scratch-fanout-ja/it-web.txt` — 47000B sha 4efe03ac6d0c → `hidden_files/w47/scratch-fanout-ja/it-web.txt`
- `scratch-fanout-ja/ko-occlusion-stick8.json` — 97B sha de454c54b21d → `hidden_files/w47/scratch-fanout-ja/ko-occlusion-stick8.json`
- `scratch-fanout-ja/ko-p8-stick8.json` — 3779B sha baebbcc705a6 → `hidden_files/w47/scratch-fanout-ja/ko-p8-stick8.json`
- `scratch-fanout-ja/ko-p8compare-stick8.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-fanout-ja/ko-p8compare-stick8.json`
- `scratch-fanout-ja/ko-print.txt` — 47997B sha d096f7757759 → `hidden_files/w47/scratch-fanout-ja/ko-print.txt`
- `scratch-fanout-ja/ko-sha-stick8-pre.txt` — 678B sha 8f9e67eab597 → `hidden_files/w47/scratch-fanout-ja/ko-sha-stick8-pre.txt`
- `scratch-fanout-ja/ko-sha-stick8-run1.txt` — 678B sha 8f9e67eab597 → `hidden_files/w47/scratch-fanout-ja/ko-sha-stick8-run1.txt`
- `scratch-fanout-ja/ko-sha-stick8-run2.txt` — 678B sha 8f9e67eab597 → `hidden_files/w47/scratch-fanout-ja/ko-sha-stick8-run2.txt`
- `scratch-fanout-ja/ko-web.txt` — 47997B sha d096f7757759 → `hidden_files/w47/scratch-fanout-ja/ko-web.txt`
- `scratch-fanout-ja/nl-occlusion-stick8.json` — 97B sha 8b1da2b45dc1 → `hidden_files/w47/scratch-fanout-ja/nl-occlusion-stick8.json`
- `scratch-fanout-ja/nl-p8-stick8.json` — 3776B sha 3be41957e4e1 → `hidden_files/w47/scratch-fanout-ja/nl-p8-stick8.json`
- `scratch-fanout-ja/nl-p8compare-stick8.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-fanout-ja/nl-p8compare-stick8.json`
- `scratch-fanout-ja/nl-print.txt` — 45989B sha 73bb13ac403a → `hidden_files/w47/scratch-fanout-ja/nl-print.txt`
- `scratch-fanout-ja/nl-web.txt` — 45989B sha 73bb13ac403a → `hidden_files/w47/scratch-fanout-ja/nl-web.txt`
- `scratch-fanout-ja/pt-occlusion-stick8.json` — 97B sha d2ff1a6e968d → `hidden_files/w47/scratch-fanout-ja/pt-occlusion-stick8.json`
- `scratch-fanout-ja/pt-p8-stick8.json` — 3778B sha 54849455ff54 → `hidden_files/w47/scratch-fanout-ja/pt-p8-stick8.json`
- `scratch-fanout-ja/pt-p8compare-stick8.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-fanout-ja/pt-p8compare-stick8.json`
- `scratch-fanout-ja/pt-print.txt` — 46976B sha 4de357532bfd → `hidden_files/w47/scratch-fanout-ja/pt-print.txt`
- `scratch-fanout-ja/pt-web.txt` — 46976B sha 4de357532bfd → `hidden_files/w47/scratch-fanout-ja/pt-web.txt`
- `scratch-fanout-ja/ru-occlusion-stick8.json` — 97B sha 005d3de0c24c → `hidden_files/w47/scratch-fanout-ja/ru-occlusion-stick8.json`
- `scratch-fanout-ja/ru-p8-stick8.json` — 3881B sha 17ecb5bc60d0 → `hidden_files/w47/scratch-fanout-ja/ru-p8-stick8.json`
- `scratch-fanout-ja/ru-p8compare-stick8.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-fanout-ja/ru-p8compare-stick8.json`
- `scratch-fanout-ja/ru-print.txt` — 53247B sha 8a1e93c54d22 → `hidden_files/w47/scratch-fanout-ja/ru-print.txt`
- `scratch-fanout-ja/ru-web.txt` — 53247B sha 8a1e93c54d22 → `hidden_files/w47/scratch-fanout-ja/ru-web.txt`
- `scratch-fanout-ja/zh-tw-occlusion-stick8.json` — 100B sha 5af7b6dc22a0 → `hidden_files/w47/scratch-fanout-ja/zh-tw-occlusion-stick8.json`
- `scratch-fanout-ja/zh-tw-p8-stick8.json` — 3722B sha 61a1bc20365e → `hidden_files/w47/scratch-fanout-ja/zh-tw-p8-stick8.json`
- `scratch-fanout-ja/zh-tw-p8compare-stick8.json` — 2120B sha 852ae03c6216 → `hidden_files/w47/scratch-fanout-ja/zh-tw-p8compare-stick8.json`
- `scratch-fanout-ja/zh-tw-print.txt` — 44661B sha 2d458de93dcd → `hidden_files/w47/scratch-fanout-ja/zh-tw-print.txt`
- `scratch-fanout-ja/zh-tw-sha-stick8-pre.txt` — 678B sha 43449203e1a2 → `hidden_files/w47/scratch-fanout-ja/zh-tw-sha-stick8-pre.txt`
- `scratch-fanout-ja/zh-tw-sha-stick8-run1.txt` — 678B sha 43449203e1a2 → `hidden_files/w47/scratch-fanout-ja/zh-tw-sha-stick8-run1.txt`
- `scratch-fanout-ja/zh-tw-sha-stick8-run2.txt` — 678B sha 43449203e1a2 → `hidden_files/w47/scratch-fanout-ja/zh-tw-sha-stick8-run2.txt`
- `scratch-fanout-ja/zh-tw-web.txt` — 44661B sha 2d458de93dcd → `hidden_files/w47/scratch-fanout-ja/zh-tw-web.txt`
- `scratch-fix-es-fr1/FIX-LOG.md` — 10694B sha e301876c6f67 → `hidden_files/w47/scratch-fix-es-fr1/FIX-LOG.md`
- `scratch-fix-es-fr1/build4.log` — 2121B sha 289d2415c402 → `hidden_files/w47/scratch-fix-es-fr1/build4.log`
- `scratch-fix-es-fr1/creambox-all4.log` — 2661B sha 6d019ef3fba3 → `hidden_files/w47/scratch-fix-es-fr1/creambox-all4.log`
- `scratch-fix-es-fr1/creambox-diag4.log` — 2090B sha 3efd3f1c1572 → `hidden_files/w47/scratch-fix-es-fr1/creambox-diag4.log`
- `scratch-fix-es-fr1/creambox.py` — 859B sha 5d50e2cb69b1 → `hidden_files/w47/scratch-fix-es-fr1/creambox.py`
- `scratch-fix-es-fr1/creambox_diag.py` — 1169B sha db1dafc20fa8 → `hidden_files/w47/scratch-fix-es-fr1/creambox_diag.py`
- `scratch-fix-es-fr1/crop-p2-sabias.png` — 193718B sha 503fe186071f → `hidden_files/w47/scratch-fix-es-fr1/crop-p2-sabias.png`
- `scratch-fix-es-fr1/crop-p3-youturn.png` — 201172B sha e36408bc745e → `hidden_files/w47/scratch-fix-es-fr1/crop-p3-youturn.png`
- `scratch-fix-es-fr1/crop-p5-votar.png` — 192193B sha e81f8e00737e → `hidden_files/w47/scratch-fix-es-fr1/crop-p5-votar.png`
- `scratch-fix-es-fr1/crop-p5-youturn.png` — 199110B sha 3246c36afd90 → `hidden_files/w47/scratch-fix-es-fr1/crop-p5-youturn.png`
- `scratch-fix-es-fr1/freeze-baseline4.log` — 684B sha 35a4b2e1a102 → `hidden_files/w47/scratch-fix-es-fr1/freeze-baseline4.log`
- `scratch-fix-es-fr1/freeze-diff4.json` — 72758B sha 2fdab94b31d8 → `hidden_files/w47/scratch-fix-es-fr1/freeze-diff4.json`
- `scratch-fix-es-fr1/freeze-diff4.log` — 677B sha 64a0e17df349 → `hidden_files/w47/scratch-fix-es-fr1/freeze-diff4.log`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/2026-w47-es-fr.text.md` — 45272B sha 94476219c438 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/2026-w47-es-fr.text.md`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/ABSTRACT.txt` — 504B sha 33f8688890f4 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/ABSTRACT.txt`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/La-Lucerna-VOL4-es-fr-web.pdf` — 883853B sha f8f786e2432c → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/La-Lucerna-VOL4-es-fr-web.pdf`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/La-Lucerna-VOL4-es-fr.pdf` — 3499799B sha 7ff5b85401a9 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/La-Lucerna-VOL4-es-fr.pdf`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/WEEKLY-KIT.md` — 20029B sha 007c30a2a67a → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/WEEKLY-KIT.md`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/__pycache__/bslib4.cpython-312.pyc` — 19035B sha e1f066058ea3 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/__pycache__/bslib4.cpython-312.pyc`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/__pycache__/svglib.cpython-312.pyc` — 53552B sha 7c93ba1c329d → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/__pycache__/svglib.cpython-312.pyc`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/assets/book_hours.jpg` — 45557B sha fd22dd800bf4 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/assets/book_hours.jpg`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/assets/flamenco_sargent.jpg` — 119187B sha 65ec8a7ef2d8 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/assets/flamenco_sargent.jpg`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/assets/lucerna-moth.svg` — 1324B sha 42487693345a → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/assets/lucerna-moth.svg`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/assets/swan_pen.jpg` — 142261B sha b315bca1dd3d → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/assets/swan_pen.jpg`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/assets/urna_small.jpg` — 77707B sha 27bb94909699 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/assets/urna_small.jpg`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/bslib4.py` — 10102B sha 6b1ef78e8786 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/bslib4.py`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p1-portada.png` — 699805B sha a70275f811b0 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p1-portada.png`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p2-vida.png` — 747804B sha 29e7761795be → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p2-vida.png`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p3-cultura.png` — 906045B sha 39ae6c1ab5da → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p3-cultura.png`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p4-deporte.png` — 640719B sha 6dcf7ac0ef96 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p4-deporte.png`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p5-juventud.png` — 965377B sha 4fc1228bc34a → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p5-juventud.png`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p6-afondo.png` — 667072B sha 1cf7d58dcedd → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p6-afondo.png`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p7-lengua.png` — 686549B sha 2ca12fe24790 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p7-lengua.png`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p8-ejercicios.png` — 1196303B sha 2d030eeeabc4 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/cards/p8-ejercicios.png`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/content12.py` — 19785B sha c4c5228f952b → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/content12.py`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/content34.py` — 16534B sha 73be63243abb → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/content34.py`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/content56.py` — 18031B sha 2b80fbfb0952 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/content56.py`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/content7.py` — 10291B sha 4b9faebca929 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/content7.py`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/content8.py` — 10485B sha 6529d4647b67 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/content8.py`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/render.py` — 1540B sha ab5e955e7c95 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/render.py`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/run.py` — 773B sha a5ca1b7ec7dd → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/run.py`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p1-portada.svg` — 31159B sha cf8be0375430 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p1-portada.svg`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p2-vida.svg` — 30941B sha 7cefcc27fc3e → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p2-vida.svg`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p3-cultura.svg` — 186274B sha c60aefdcfe55 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p3-cultura.svg`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p4-deporte.svg` — 27877B sha d4d068ef068e → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p4-deporte.svg`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p5-juventud.svg` — 132656B sha f7c376c6e5ac → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p5-juventud.svg`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p6-afondo.svg` — 29740B sha b9a8ec2fdaed → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p6-afondo.svg`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p7-lengua.svg` — 88010B sha 2190c844e7d4 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p7-lengua.svg`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p8-ejercicios.svg` — 255554B sha 7cc5b110e731 → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svg/p8-ejercicios.svg`
- `scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svglib.py` — 21892B sha 0e3d72d73dad → `hidden_files/w47/scratch-fix-es-fr1/freeze-es-fr-fix1/build-copy/svglib.py`
- `scratch-fix-es-fr1/ink-after.log` — 2684B sha 43ac2d960df6 → `hidden_files/w47/scratch-fix-es-fr1/ink-after.log`
- `scratch-fix-es-fr1/ink-after2.log` — 2069B sha b78b62a83de0 → `hidden_files/w47/scratch-fix-es-fr1/ink-after2.log`
- `scratch-fix-es-fr1/ink-after3.log` — 2056B sha 78cdca435f5b → `hidden_files/w47/scratch-fix-es-fr1/ink-after3.log`
- `scratch-fix-es-fr1/ink-baseline.log` — 2057B sha 3e3019f36d0a → `hidden_files/w47/scratch-fix-es-fr1/ink-baseline.log`
- `scratch-fix-es-fr1/ink_check.py` — 5153B sha 05e3e5c9ab64 → `hidden_files/w47/scratch-fix-es-fr1/ink_check.py`
- `scratch-fix-es-fr1/occlusion-selftest4.log` — 134B sha 41a33d94ad31 → `hidden_files/w47/scratch-fix-es-fr1/occlusion-selftest4.log`
- `scratch-fix-es-fr1/occlusion4.log` — 183B sha 76db2c08862a → `hidden_files/w47/scratch-fix-es-fr1/occlusion4.log`
- `scratch-fix-es-fr1/p8-compare4.json` — 2127B sha f2b71a3c329f → `hidden_files/w47/scratch-fix-es-fr1/p8-compare4.json`
- `scratch-fix-es-fr1/p8-compare4.log` — 222B sha 98ebb1c95026 → `hidden_files/w47/scratch-fix-es-fr1/p8-compare4.log`
- `scratch-fix-es-fr1/p8-extract4.json` — 4058B sha 242ccba76eaf → `hidden_files/w47/scratch-fix-es-fr1/p8-extract4.json`
- `scratch-fix-es-fr1/p8-extract4.log` — 746B sha 3a8037c1c7c0 → `hidden_files/w47/scratch-fix-es-fr1/p8-extract4.log`
- `scratch-fix-es-fr1/print-layout.txt` — 108334B sha fa1d92402fce → `hidden_files/w47/scratch-fix-es-fr1/print-layout.txt`
- `scratch-fix-es-fr1/print-layout2.txt` — 108334B sha fa1d92402fce → `hidden_files/w47/scratch-fix-es-fr1/print-layout2.txt`
- `scratch-fix-es-fr1/print.txt` — 46246B sha ce3d56e9f8fa → `hidden_files/w47/scratch-fix-es-fr1/print.txt`
- `scratch-fix-es-fr1/render4.log` — 1251B sha cb4e536f29e1 → `hidden_files/w47/scratch-fix-es-fr1/render4.log`
- `scratch-fix-es-fr1/style11-4.log` — 1196B sha 7d1aec8f1595 → `hidden_files/w47/scratch-fix-es-fr1/style11-4.log`
- `scratch-fix-es-fr1/svg-diff-summary.txt` — 161B sha f3ae5b5b53cd → `hidden_files/w47/scratch-fix-es-fr1/svg-diff-summary.txt`
- `scratch-fix-es-fr1/textlayer-compare.txt` — 86B sha a90fd3d1fae1 → `hidden_files/w47/scratch-fix-es-fr1/textlayer-compare.txt`
- `scratch-fix-es-fr1/tmp/probe.txt` — 17B sha 344c6ea4f3a6 → `hidden_files/w47/scratch-fix-es-fr1/tmp/probe.txt`
- `scratch-fix-es-fr1/web-layout.txt` — 108334B sha fa1d92402fce → `hidden_files/w47/scratch-fix-es-fr1/web-layout.txt`
- `scratch-fix-es-fr1/web-layout2.txt` — 108334B sha fa1d92402fce → `hidden_files/w47/scratch-fix-es-fr1/web-layout2.txt`
- `scratch-fix-es-fr1/web.txt` — 46246B sha ce3d56e9f8fa → `hidden_files/w47/scratch-fix-es-fr1/web.txt`
- `scratch-proof-de-fr1/crop-p1-wordofweek.png` — 156855B sha 4801681d48a5 → `hidden_files/w47/scratch-proof-de-fr1/crop-p1-wordofweek.png`
- `scratch-proof-de-fr1/crop-p3-apostrophe.png` — 97739B sha cbe86f576fec → `hidden_files/w47/scratch-proof-de-fr1/crop-p3-apostrophe.png`
- `scratch-proof-de-fr1/crop-p4-undsie.png` — 188360B sha a4daf062e983 → `hidden_files/w47/scratch-proof-de-fr1/crop-p4-undsie.png`
- `scratch-proof-de-fr1/crop-p7-apostrophe.png` — 149207B sha 088ba1faf213 → `hidden_files/w47/scratch-proof-de-fr1/crop-p7-apostrophe.png`
- `scratch-proof-de-fr1/freeze-direct.log` — 1142B sha 54f96b937ac7 → `hidden_files/w47/scratch-proof-de-fr1/freeze-direct.log`
- `scratch-proof-de-fr1/freeze.log` — 756B sha ad1210411d72 → `hidden_files/w47/scratch-proof-de-fr1/freeze.log`
- `scratch-proof-de-fr1/keycheck.log` — 1113B sha 671ff738c233 → `hidden_files/w47/scratch-proof-de-fr1/keycheck.log`
- `scratch-proof-de-fr1/measure.log` — 1483B sha 72540140e0c7 → `hidden_files/w47/scratch-proof-de-fr1/measure.log`
- `scratch-proof-de-fr1/occlusion.log` — 213B sha e84492fd98ec → `hidden_files/w47/scratch-proof-de-fr1/occlusion.log`
- `scratch-proof-de-fr1/p8compare.log` — 223B sha 33f224b13c61 → `hidden_files/w47/scratch-proof-de-fr1/p8compare.log`
- `scratch-proof-de-fr1/p8extract.log` — 745B sha 2ddd8f4ff323 → `hidden_files/w47/scratch-proof-de-fr1/p8extract.log`
- `scratch-proof-de-fr1/print-raw.txt` — 49772B sha dea7bd3afe47 → `hidden_files/w47/scratch-proof-de-fr1/print-raw.txt`
- `scratch-proof-de-fr1/print.txt` — 115242B sha f7aec3d08cc0 → `hidden_files/w47/scratch-proof-de-fr1/print.txt`
- `scratch-proof-de-fr1/render/print-1.png` — 1423746B sha a136fb4e8da2 → `hidden_files/w47/scratch-proof-de-fr1/render/print-1.png`
- `scratch-proof-de-fr1/render/print-2.png` — 896012B sha 1b3641147657 → `hidden_files/w47/scratch-proof-de-fr1/render/print-2.png`
- `scratch-proof-de-fr1/render/print-3.png` — 1451318B sha 030f3abc1724 → `hidden_files/w47/scratch-proof-de-fr1/render/print-3.png`
- `scratch-proof-de-fr1/render/print-4.png` — 1344144B sha 71d8b703b1d3 → `hidden_files/w47/scratch-proof-de-fr1/render/print-4.png`
- `scratch-proof-de-fr1/render/print-5.png` — 1294140B sha 34ad1aef0af1 → `hidden_files/w47/scratch-proof-de-fr1/render/print-5.png`
- `scratch-proof-de-fr1/render/print-6.png` — 957928B sha f8cab277aae9 → `hidden_files/w47/scratch-proof-de-fr1/render/print-6.png`
- `scratch-proof-de-fr1/render/print-7.png` — 972414B sha 409cba13d91a → `hidden_files/w47/scratch-proof-de-fr1/render/print-7.png`
- `scratch-proof-de-fr1/render/print-8.png` — 1545712B sha a9631fb55474 → `hidden_files/w47/scratch-proof-de-fr1/render/print-8.png`
- `scratch-proof-de-fr1/render/web-1.png` — 1331410B sha 0390feb5960f → `hidden_files/w47/scratch-proof-de-fr1/render/web-1.png`
- `scratch-proof-de-fr1/render/web-8.png` — 1519366B sha ac61f30c6a21 → `hidden_files/w47/scratch-proof-de-fr1/render/web-8.png`
- `scratch-proof-de-fr1/svg-sha-after.txt` — 676B sha 3cb9d626ee37 → `hidden_files/w47/scratch-proof-de-fr1/svg-sha-after.txt`
- `scratch-proof-de-fr1/svg-sha-before.txt` — 676B sha 3cb9d626ee37 → `hidden_files/w47/scratch-proof-de-fr1/svg-sha-before.txt`
- `scratch-proof-de-fr1/verify.log` — 5303B sha 77678cb9c0d4 → `hidden_files/w47/scratch-proof-de-fr1/verify.log`
- `scratch-proof-de-fr1/web-raw.txt` — 49772B sha dea7bd3afe47 → `hidden_files/w47/scratch-proof-de-fr1/web-raw.txt`
- `scratch-proof-de-fr1/web.txt` — 115323B sha edf0325cbba6 → `hidden_files/w47/scratch-proof-de-fr1/web.txt`
- `scratch-proof-ja-de1/.probe` — 42B sha d631b23f501d → `hidden_files/w47/scratch-proof-ja-de1/.probe`
- `scratch-proof-ja-de1/GATE-LOG.md` — 5895B sha 9c2d02c6f1cc → `hidden_files/w47/scratch-proof-ja-de1/GATE-LOG.md`
- `scratch-proof-ja-de1/PROOF-NOTE.md` — 14704B sha a2e0cb6394b3 → `hidden_files/w47/scratch-proof-ja-de1/PROOF-NOTE.md`
- `scratch-proof-ja-de1/de-occlusion-proof1.json` — 97B sha ac7a7c5058de → `hidden_files/w47/scratch-proof-ja-de1/de-occlusion-proof1.json`
- `scratch-proof-ja-de1/de-p8-proof1.json` — 3797B sha ee0ddcebc800 → `hidden_files/w47/scratch-proof-ja-de1/de-p8-proof1.json`
- `scratch-proof-ja-de1/de-p8compare-proof1.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-proof-ja-de1/de-p8compare-proof1.json`
- `scratch-proof-ja-de1/render-print/p-1.png` — 1306734B sha d4266774b5aa → `hidden_files/w47/scratch-proof-ja-de1/render-print/p-1.png`
- `scratch-proof-ja-de1/render-print/p-2.png` — 676456B sha ba9156ac9a08 → `hidden_files/w47/scratch-proof-ja-de1/render-print/p-2.png`
- `scratch-proof-ja-de1/render-print/p-3.png` — 932600B sha f0b69ade9f75 → `hidden_files/w47/scratch-proof-ja-de1/render-print/p-3.png`
- `scratch-proof-ja-de1/render-print/p-4.png` — 826319B sha cc80be46c7bf → `hidden_files/w47/scratch-proof-ja-de1/render-print/p-4.png`
- `scratch-proof-ja-de1/render-print/p-5.png` — 952924B sha 6c0a9de77077 → `hidden_files/w47/scratch-proof-ja-de1/render-print/p-5.png`
- `scratch-proof-ja-de1/render-print/p-6.png` — 705736B sha 88b74d58050b → `hidden_files/w47/scratch-proof-ja-de1/render-print/p-6.png`
- `scratch-proof-ja-de1/render-print/p-7.png` — 1447953B sha ff30977a13b0 → `hidden_files/w47/scratch-proof-ja-de1/render-print/p-7.png`
- `scratch-proof-ja-de1/render-print/p-8.png` — 1607682B sha bf661b2f0ff1 → `hidden_files/w47/scratch-proof-ja-de1/render-print/p-8.png`
- `scratch-proof-ja-de1/render-web/p1-1.png` — 1240350B sha 264791bfd797 → `hidden_files/w47/scratch-proof-ja-de1/render-web/p1-1.png`
- `scratch-proof-ja-de1/render-web/p8-8.png` — 1546245B sha 51961b3dff8a → `hidden_files/w47/scratch-proof-ja-de1/render-web/p8-8.png`
- `scratch-proof-ja-de1/rerun-log.txt` — 2110B sha 6ee1786e3bd1 → `hidden_files/w47/scratch-proof-ja-de1/rerun-log.txt`
- `scratch-proof-ja-de1/rerun/2026-w47-ja-de.text.md` — 46516B sha 60707755022b → `hidden_files/w47/scratch-proof-ja-de1/rerun/2026-w47-ja-de.text.md`
- `scratch-proof-ja-de1/rerun/ABSTRACT.txt` — 311B sha 9be2bfd633cb → `hidden_files/w47/scratch-proof-ja-de1/rerun/ABSTRACT.txt`
- `scratch-proof-ja-de1/rerun/Lucerna-VOL4-JA-DE-web.pdf` — 4483732B sha c55dd68cfcd6 → `hidden_files/w47/scratch-proof-ja-de1/rerun/Lucerna-VOL4-JA-DE-web.pdf`
- `scratch-proof-ja-de1/rerun/Lucerna-VOL4-JA-DE.pdf` — 29102629B sha b5d66e17d9ac → `hidden_files/w47/scratch-proof-ja-de1/rerun/Lucerna-VOL4-JA-DE.pdf`
- `scratch-proof-ja-de1/rerun/WEEKLY-KIT.md` — 10929B sha 4be0716288c4 → `hidden_files/w47/scratch-proof-ja-de1/rerun/WEEKLY-KIT.md`
- `scratch-proof-ja-de1/rerun/__pycache__/bslib4.cpython-312.pyc` — 18953B sha a165d2a56838 → `hidden_files/w47/scratch-proof-ja-de1/rerun/__pycache__/bslib4.cpython-312.pyc`
- `scratch-proof-ja-de1/rerun/__pycache__/svglib.cpython-312.pyc` — 39735B sha 61bec19a6e32 → `hidden_files/w47/scratch-proof-ja-de1/rerun/__pycache__/svglib.cpython-312.pyc`
- `scratch-proof-ja-de1/rerun/assets/CREDITS.md` — 1712B sha 688f0e1d0e39 → `hidden_files/w47/scratch-proof-ja-de1/rerun/assets/CREDITS.md`
- `scratch-proof-ja-de1/rerun/assets/arashiyama-pond.jpg` — 257367B sha a30f5fbc940b → `hidden_files/w47/scratch-proof-ja-de1/rerun/assets/arashiyama-pond.jpg`
- `scratch-proof-ja-de1/rerun/assets/arashiyama-temple.jpg` — 289997B sha 9c557d1752a0 → `hidden_files/w47/scratch-proof-ja-de1/rerun/assets/arashiyama-temple.jpg`
- `scratch-proof-ja-de1/rerun/assets/beaujolais.jpg` — 154661B sha a16b99c636b2 → `hidden_files/w47/scratch-proof-ja-de1/rerun/assets/beaujolais.jpg`
- `scratch-proof-ja-de1/rerun/assets/lucerna-moth.svg` — 1324B sha 42487693345a → `hidden_files/w47/scratch-proof-ja-de1/rerun/assets/lucerna-moth.svg`
- `scratch-proof-ja-de1/rerun/assets/maple.jpg` — 474411B sha 140f46d9e41b → `hidden_files/w47/scratch-proof-ja-de1/rerun/assets/maple.jpg`
- `scratch-proof-ja-de1/rerun/assets/tori.jpg` — 400576B sha 5a94b1e05d8f → `hidden_files/w47/scratch-proof-ja-de1/rerun/assets/tori.jpg`
- `scratch-proof-ja-de1/rerun/bslib4.py` — 10012B sha e14ccfff816d → `hidden_files/w47/scratch-proof-ja-de1/rerun/bslib4.py`
- `scratch-proof-ja-de1/rerun/content12.py` — 18499B sha 3cdf06f36044 → `hidden_files/w47/scratch-proof-ja-de1/rerun/content12.py`
- `scratch-proof-ja-de1/rerun/content34.py` — 17146B sha 8ce6d00a452f → `hidden_files/w47/scratch-proof-ja-de1/rerun/content34.py`
- `scratch-proof-ja-de1/rerun/content56.py` — 16450B sha e088d13b25bd → `hidden_files/w47/scratch-proof-ja-de1/rerun/content56.py`
- `scratch-proof-ja-de1/rerun/content7.py` — 10646B sha 230c9a3d7dc2 → `hidden_files/w47/scratch-proof-ja-de1/rerun/content7.py`
- `scratch-proof-ja-de1/rerun/content8.py` — 10733B sha 1d6235f8ae08 → `hidden_files/w47/scratch-proof-ja-de1/rerun/content8.py`
- `scratch-proof-ja-de1/rerun/render.py` — 1184B sha 388df61eac8e → `hidden_files/w47/scratch-proof-ja-de1/rerun/render.py`
- `scratch-proof-ja-de1/rerun/run.py` — 773B sha ca45aabf00da → `hidden_files/w47/scratch-proof-ja-de1/rerun/run.py`
- `scratch-proof-ja-de1/rerun/svg/p1-hyoushi.svg` — 658951B sha 9d35b7415642 → `hidden_files/w47/scratch-proof-ja-de1/rerun/svg/p1-hyoushi.svg`
- `scratch-proof-ja-de1/rerun/svg/p2-kurashi.svg` — 25170B sha 80f4964c3a18 → `hidden_files/w47/scratch-proof-ja-de1/rerun/svg/p2-kurashi.svg`
- `scratch-proof-ja-de1/rerun/svg/p3-bunka.svg` — 229975B sha a42beb0b3837 → `hidden_files/w47/scratch-proof-ja-de1/rerun/svg/p3-bunka.svg`
- `scratch-proof-ja-de1/rerun/svg/p4-supotsu.svg` — 26987B sha cfeaddb4a98f → `hidden_files/w47/scratch-proof-ja-de1/rerun/svg/p4-supotsu.svg`
- `scratch-proof-ja-de1/rerun/svg/p5-wakamono.svg` — 368478B sha ff1ca67b8289 → `hidden_files/w47/scratch-proof-ja-de1/rerun/svg/p5-wakamono.svg`
- `scratch-proof-ja-de1/rerun/svg/p6-fukayomi.svg` — 25748B sha 2ff8500f168b → `hidden_files/w47/scratch-proof-ja-de1/rerun/svg/p6-fukayomi.svg`
- `scratch-proof-ja-de1/rerun/svg/p7-kotoba.svg` — 561273B sha 490ee398a58a → `hidden_files/w47/scratch-proof-ja-de1/rerun/svg/p7-kotoba.svg`
- `scratch-proof-ja-de1/rerun/svg/p8-tesuto.svg` — 446254B sha 28b2344f3507 → `hidden_files/w47/scratch-proof-ja-de1/rerun/svg/p8-tesuto.svg`
- `scratch-proof-ja-de1/rerun/svglib.py` — 14700B sha b50f5ef9e12e → `hidden_files/w47/scratch-proof-ja-de1/rerun/svglib.py`
- `scratch-proof-ja-de1/scan1.txt` — 2271B sha a524d08f3563 → `hidden_files/w47/scratch-proof-ja-de1/scan1.txt`
- `scratch-proof-ja-de1/scan2.txt` — 3136B sha cec606a80486 → `hidden_files/w47/scratch-proof-ja-de1/scan2.txt`
- `scratch-proof-ja-de1/scan3.txt` — 41395B sha 5d183819e8df → `hidden_files/w47/scratch-proof-ja-de1/scan3.txt`
- `scratch-proof-ja-de1/scan4.txt` — 2159B sha 90909618835b → `hidden_files/w47/scratch-proof-ja-de1/scan4.txt`
- `scratch-proof-ja-de1/scan5.txt` — 720B sha 1bc787393b32 → `hidden_files/w47/scratch-proof-ja-de1/scan5.txt`
- `scratch-proof-ja-de1/scan6.txt` — 2731B sha 666946812b25 → `hidden_files/w47/scratch-proof-ja-de1/scan6.txt`
- `scratch-proof-ja-de1/scan7.txt` — 359B sha bd6b0a9bcdeb → `hidden_files/w47/scratch-proof-ja-de1/scan7.txt`
- `scratch-proof-ja-en1/.probe` — 30B sha fad8d8e14edf → `hidden_files/w47/scratch-proof-ja-en1/.probe`
- `scratch-proof-ja-en1/GATE-LOG.md` — 6148B sha d91906d0cb91 → `hidden_files/w47/scratch-proof-ja-en1/GATE-LOG.md`
- `scratch-proof-ja-en1/PROOF-NOTE.md` — 11452B sha 54217b6ccba2 → `hidden_files/w47/scratch-proof-ja-en1/PROOF-NOTE.md`
- `scratch-proof-ja-en1/diff-content12.txt` — 20524B sha 2d901b22e002 → `hidden_files/w47/scratch-proof-ja-en1/diff-content12.txt`
- `scratch-proof-ja-en1/diff-content34.txt` — 19539B sha 29b340fc0f4f → `hidden_files/w47/scratch-proof-ja-en1/diff-content34.txt`
- `scratch-proof-ja-en1/diff-content56.txt` — 20254B sha 2c9139f3c0ac → `hidden_files/w47/scratch-proof-ja-en1/diff-content56.txt`
- `scratch-proof-ja-en1/diff-content7.txt` — 16277B sha 17965e335e36 → `hidden_files/w47/scratch-proof-ja-en1/diff-content7.txt`
- `scratch-proof-ja-en1/diff-content8.txt` — 14602B sha a03989e7e8db → `hidden_files/w47/scratch-proof-ja-en1/diff-content8.txt`
- `scratch-proof-ja-en1/occlusion-proof.json` — 97B sha c2bf557b4312 → `hidden_files/w47/scratch-proof-ja-en1/occlusion-proof.json`
- `scratch-proof-ja-en1/p8-compare-proof.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-proof-ja-en1/p8-compare-proof.json`
- `scratch-proof-ja-en1/p8-extract-proof.json` — 3764B sha 6b8ddab4f83a → `hidden_files/w47/scratch-proof-ja-en1/p8-extract-proof.json`
- `scratch-proof-ja-en1/render/print-1.png` — 1300987B sha e406fd69b75e → `hidden_files/w47/scratch-proof-ja-en1/render/print-1.png`
- `scratch-proof-ja-en1/render/print-2.png` — 664013B sha 6919e8d2570a → `hidden_files/w47/scratch-proof-ja-en1/render/print-2.png`
- `scratch-proof-ja-en1/render/print-3.png` — 925305B sha 5a81cb456a3a → `hidden_files/w47/scratch-proof-ja-en1/render/print-3.png`
- `scratch-proof-ja-en1/render/print-4.png` — 811874B sha 5e946c25a70f → `hidden_files/w47/scratch-proof-ja-en1/render/print-4.png`
- `scratch-proof-ja-en1/render/print-5.png` — 933235B sha 392f66f07f3f → `hidden_files/w47/scratch-proof-ja-en1/render/print-5.png`
- `scratch-proof-ja-en1/render/print-6.png` — 692385B sha 1c8b369b1988 → `hidden_files/w47/scratch-proof-ja-en1/render/print-6.png`
- `scratch-proof-ja-en1/render/print-7.png` — 1433933B sha 0fda25182ba2 → `hidden_files/w47/scratch-proof-ja-en1/render/print-7.png`
- `scratch-proof-ja-en1/render/print-8.png` — 1576616B sha ecc341765932 → `hidden_files/w47/scratch-proof-ja-en1/render/print-8.png`
- `scratch-proof-ja-en1/render/web-p1-1.png` — 1234125B sha 4aadf60a9ec9 → `hidden_files/w47/scratch-proof-ja-en1/render/web-p1-1.png`
- `scratch-proof-ja-en1/render/web-p8-8.png` — 1515316B sha e4d98ac20b80 → `hidden_files/w47/scratch-proof-ja-en1/render/web-p8-8.png`
- `scratch-proof-ja-en1/render/zoom-p7-apos.png` — 35809B sha 42a3c5b17b2d → `hidden_files/w47/scratch-proof-ja-en1/render/zoom-p7-apos.png`
- `scratch-proof-ja-en1/render/zoom-p8-apos.png` — 43760B sha 75cf26a994ea → `hidden_files/w47/scratch-proof-ja-en1/render/zoom-p8-apos.png`
- `scratch-proof-ja-en1/run-proof1.log` — 2106B sha b6d08903cc5b → `hidden_files/w47/scratch-proof-ja-en1/run-proof1.log`
- `scratch-proof-ja-en1/run-proof2.log` — 2106B sha b6d08903cc5b → `hidden_files/w47/scratch-proof-ja-en1/run-proof2.log`
- `scratch-proof-ja-en1/sha-proof1.txt` — 678B sha a27cebaf06fe → `hidden_files/w47/scratch-proof-ja-en1/sha-proof1.txt`
- `scratch-proof-ja-en1/sha-proof2.txt` — 1038B sha b82c5d98e054 → `hidden_files/w47/scratch-proof-ja-en1/sha-proof2.txt`
- `scratch-proof-ja-es1/.probe` — 30B sha fb8c6ece5d28 → `hidden_files/w47/scratch-proof-ja-es1/.probe`
- `scratch-proof-ja-es1/es1-occlusion.json` — 97B sha 7c5ddd539392 → `hidden_files/w47/scratch-proof-ja-es1/es1-occlusion.json`
- `scratch-proof-ja-es1/es1-p8-core.json` — 3702B sha af298a68520f → `hidden_files/w47/scratch-proof-ja-es1/es1-p8-core.json`
- `scratch-proof-ja-es1/es1-p8.json` — 3753B sha 846e49aae986 → `hidden_files/w47/scratch-proof-ja-es1/es1-p8.json`
- `scratch-proof-ja-es1/es1-p8compare.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-proof-ja-es1/es1-p8compare.json`
- `scratch-proof-ja-es1/rebuild-run.log` — 2120B sha 1c5210e4fc9c → `hidden_files/w47/scratch-proof-ja-es1/rebuild-run.log`
- `scratch-proof-ja-es1/rebuild/2026-w47-ja-es.text.md` — 46682B sha 29f99f4507dd → `hidden_files/w47/scratch-proof-ja-es1/rebuild/2026-w47-ja-es.text.md`
- `scratch-proof-ja-es1/rebuild/ABSTRACT.txt` — 308B sha 9058050125e2 → `hidden_files/w47/scratch-proof-ja-es1/rebuild/ABSTRACT.txt`
- `scratch-proof-ja-es1/rebuild/WEEKLY-KIT.md` — 11760B sha 8a583c2237f5 → `hidden_files/w47/scratch-proof-ja-es1/rebuild/WEEKLY-KIT.md`
- `scratch-proof-ja-es1/rebuild/__pycache__/bslib4.cpython-312.pyc` — 18958B sha efd30a9e24a0 → `hidden_files/w47/scratch-proof-ja-es1/rebuild/__pycache__/bslib4.cpython-312.pyc`
- `scratch-proof-ja-es1/rebuild/__pycache__/svglib.cpython-312.pyc` — 39737B sha 9a65b07d9abc → `hidden_files/w47/scratch-proof-ja-es1/rebuild/__pycache__/svglib.cpython-312.pyc`
- `scratch-proof-ja-es1/rebuild/assets/CREDITS.md` — 1712B sha 688f0e1d0e39 → `hidden_files/w47/scratch-proof-ja-es1/rebuild/assets/CREDITS.md`
- `scratch-proof-ja-es1/rebuild/assets/arashiyama-pond.jpg` — 257367B sha a30f5fbc940b → `hidden_files/w47/scratch-proof-ja-es1/rebuild/assets/arashiyama-pond.jpg`
- `scratch-proof-ja-es1/rebuild/assets/arashiyama-temple.jpg` — 289997B sha 9c557d1752a0 → `hidden_files/w47/scratch-proof-ja-es1/rebuild/assets/arashiyama-temple.jpg`
- `scratch-proof-ja-es1/rebuild/assets/beaujolais.jpg` — 154661B sha a16b99c636b2 → `hidden_files/w47/scratch-proof-ja-es1/rebuild/assets/beaujolais.jpg`
- `scratch-proof-ja-es1/rebuild/assets/lucerna-moth.svg` — 1324B sha 42487693345a → `hidden_files/w47/scratch-proof-ja-es1/rebuild/assets/lucerna-moth.svg`
- `scratch-proof-ja-es1/rebuild/assets/maple.jpg` — 474411B sha 140f46d9e41b → `hidden_files/w47/scratch-proof-ja-es1/rebuild/assets/maple.jpg`
- `scratch-proof-ja-es1/rebuild/assets/tori.jpg` — 400576B sha 5a94b1e05d8f → `hidden_files/w47/scratch-proof-ja-es1/rebuild/assets/tori.jpg`
- `scratch-proof-ja-es1/rebuild/bslib4.py` — 10012B sha e1b8c8cc5f55 → `hidden_files/w47/scratch-proof-ja-es1/rebuild/bslib4.py`
- `scratch-proof-ja-es1/rebuild/content12.py` — 18483B sha 0d5395a2c2ba → `hidden_files/w47/scratch-proof-ja-es1/rebuild/content12.py`
- `scratch-proof-ja-es1/rebuild/content34.py` — 17426B sha 2fc58e583b4f → `hidden_files/w47/scratch-proof-ja-es1/rebuild/content34.py`
- `scratch-proof-ja-es1/rebuild/content56.py` — 16491B sha c942cd66695c → `hidden_files/w47/scratch-proof-ja-es1/rebuild/content56.py`
- `scratch-proof-ja-es1/rebuild/content7.py` — 10823B sha 0668f9b31558 → `hidden_files/w47/scratch-proof-ja-es1/rebuild/content7.py`
- `scratch-proof-ja-es1/rebuild/content8.py` — 10786B sha 1332fed4b745 → `hidden_files/w47/scratch-proof-ja-es1/rebuild/content8.py`
- `scratch-proof-ja-es1/rebuild/render.py` — 1184B sha 5a9fa2a951ac → `hidden_files/w47/scratch-proof-ja-es1/rebuild/render.py`
- `scratch-proof-ja-es1/rebuild/run.py` — 773B sha ca45aabf00da → `hidden_files/w47/scratch-proof-ja-es1/rebuild/run.py`
- `scratch-proof-ja-es1/rebuild/svg/p1-hyoushi.svg` — 658940B sha 7dd43e660cf0 → `hidden_files/w47/scratch-proof-ja-es1/rebuild/svg/p1-hyoushi.svg`
- `scratch-proof-ja-es1/rebuild/svg/p2-kurashi.svg` — 25164B sha 0ef2001d7322 → `hidden_files/w47/scratch-proof-ja-es1/rebuild/svg/p2-kurashi.svg`
- `scratch-proof-ja-es1/rebuild/svg/p3-bunka.svg` — 229982B sha 8afb24ccfdea → `hidden_files/w47/scratch-proof-ja-es1/rebuild/svg/p3-bunka.svg`
- `scratch-proof-ja-es1/rebuild/svg/p4-supotsu.svg` — 27011B sha b26e6867be26 → `hidden_files/w47/scratch-proof-ja-es1/rebuild/svg/p4-supotsu.svg`
- `scratch-proof-ja-es1/rebuild/svg/p5-wakamono.svg` — 368032B sha 7170970dadf9 → `hidden_files/w47/scratch-proof-ja-es1/rebuild/svg/p5-wakamono.svg`
- `scratch-proof-ja-es1/rebuild/svg/p6-fukayomi.svg` — 25757B sha c4c405b4e26d → `hidden_files/w47/scratch-proof-ja-es1/rebuild/svg/p6-fukayomi.svg`
- `scratch-proof-ja-es1/rebuild/svg/p7-kotoba.svg` — 561440B sha d00608f91eaf → `hidden_files/w47/scratch-proof-ja-es1/rebuild/svg/p7-kotoba.svg`
- `scratch-proof-ja-es1/rebuild/svg/p8-tesuto.svg` — 446512B sha cb2813a7601a → `hidden_files/w47/scratch-proof-ja-es1/rebuild/svg/p8-tesuto.svg`
- `scratch-proof-ja-es1/rebuild/svglib.py` — 14700B sha b50f5ef9e12e → `hidden_files/w47/scratch-proof-ja-es1/rebuild/svglib.py`
- `scratch-proof-ja-es1/render-print/p-1.png` — 1299790B sha 2c6f08b41ffd → `hidden_files/w47/scratch-proof-ja-es1/render-print/p-1.png`
- `scratch-proof-ja-es1/render-print/p-2.png` — 679267B sha 171de9b4eede → `hidden_files/w47/scratch-proof-ja-es1/render-print/p-2.png`
- `scratch-proof-ja-es1/render-print/p-3.png` — 934732B sha ab3e60c21f31 → `hidden_files/w47/scratch-proof-ja-es1/render-print/p-3.png`
- `scratch-proof-ja-es1/render-print/p-4.png` — 827320B sha 4381f7c6d28b → `hidden_files/w47/scratch-proof-ja-es1/render-print/p-4.png`
- `scratch-proof-ja-es1/render-print/p-5.png` — 951991B sha c209305bd2be → `hidden_files/w47/scratch-proof-ja-es1/render-print/p-5.png`
- `scratch-proof-ja-es1/render-print/p-6.png` — 709618B sha 1c691f8f4a2e → `hidden_files/w47/scratch-proof-ja-es1/render-print/p-6.png`
- `scratch-proof-ja-es1/render-print/p-7.png` — 1443639B sha 35950b3641aa → `hidden_files/w47/scratch-proof-ja-es1/render-print/p-7.png`
- `scratch-proof-ja-es1/render-print/p-8.png` — 1531139B sha 8dcd9b61cd91 → `hidden_files/w47/scratch-proof-ja-es1/render-print/p-8.png`
- `scratch-proof-ja-es1/render-web/p1-1.png` — 1233909B sha 23672f36cf24 → `hidden_files/w47/scratch-proof-ja-es1/render-web/p1-1.png`
- `scratch-proof-ja-es1/render-web/p8-8.png` — 1469985B sha b9c1220807f3 → `hidden_files/w47/scratch-proof-ja-es1/render-web/p8-8.png`
- `scratch-proof-ja-es1/svg-sha-original.txt` — 1038B sha db9e4eb5b489 → `hidden_files/w47/scratch-proof-ja-es1/svg-sha-original.txt`
- `scratch-proof-ja-es1/svg-sha-rebuild.txt` — 678B sha 215f781235e2 → `hidden_files/w47/scratch-proof-ja-es1/svg-sha-rebuild.txt`
- `scratch-proof-ja-es1/text/print.txt` — 102065B sha e981ae55ecdb → `hidden_files/w47/scratch-proof-ja-es1/text/print.txt`
- `scratch-proof-ja-es1/text/web.txt` — 102065B sha e981ae55ecdb → `hidden_files/w47/scratch-proof-ja-es1/text/web.txt`
- `scratch-proof-ja-fr1/gates/french-lines.txt` — 16596B sha 040cdac2138b → `hidden_files/w47/scratch-proof-ja-fr1/gates/french-lines.txt`
- `scratch-proof-ja-fr1/gates/occlusion.json` — 97B sha da051761cb1a → `hidden_files/w47/scratch-proof-ja-fr1/gates/occlusion.json`
- `scratch-proof-ja-fr1/gates/occlusion.log` — 193B sha e6ce0efd791e → `hidden_files/w47/scratch-proof-ja-fr1/gates/occlusion.log`
- `scratch-proof-ja-fr1/gates/p8-compare.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-proof-ja-fr1/gates/p8-compare.json`
- `scratch-proof-ja-fr1/gates/p8-extract-core.json` — 3702B sha af298a68520f → `hidden_files/w47/scratch-proof-ja-fr1/gates/p8-extract-core.json`
- `scratch-proof-ja-fr1/gates/p8-extract.json` — 3771B sha 059cc4a67e1e → `hidden_files/w47/scratch-proof-ja-fr1/gates/p8-extract.json`
- `scratch-proof-ja-fr1/gates/print.txt` — 47208B sha 3438536a1825 → `hidden_files/w47/scratch-proof-ja-fr1/gates/print.txt`
- `scratch-proof-ja-fr1/gates/q124-zoom.png` — 66794B sha c1d412e066af → `hidden_files/w47/scratch-proof-ja-fr1/gates/q124-zoom.png`
- `scratch-proof-ja-fr1/gates/run-rerun.log` — 2124B sha 2f8cb39207a9 → `hidden_files/w47/scratch-proof-ja-fr1/gates/run-rerun.log`
- `scratch-proof-ja-fr1/gates/sha-orig.txt` — 1038B sha 33638b509e15 → `hidden_files/w47/scratch-proof-ja-fr1/gates/sha-orig.txt`
- `scratch-proof-ja-fr1/gates/sha-rerun.txt` — 726B sha c20a85e84fae → `hidden_files/w47/scratch-proof-ja-fr1/gates/sha-rerun.txt`
- `scratch-proof-ja-fr1/gates/svg-text-dump.txt` — 46749B sha 589fadb2dfcc → `hidden_files/w47/scratch-proof-ja-fr1/gates/svg-text-dump.txt`
- `scratch-proof-ja-fr1/gates/web.txt` — 47208B sha 3438536a1825 → `hidden_files/w47/scratch-proof-ja-fr1/gates/web.txt`
- `scratch-proof-ja-fr1/render-print/p-1.png` — 1747261B sha 5e3cc1fb6e68 → `hidden_files/w47/scratch-proof-ja-fr1/render-print/p-1.png`
- `scratch-proof-ja-fr1/render-print/p-2.png` — 642570B sha 22d8a333b5a1 → `hidden_files/w47/scratch-proof-ja-fr1/render-print/p-2.png`
- `scratch-proof-ja-fr1/render-print/p-3.png` — 1003592B sha 8c0ebbed95e3 → `hidden_files/w47/scratch-proof-ja-fr1/render-print/p-3.png`
- `scratch-proof-ja-fr1/render-print/p-4.png` — 766100B sha 439db684d717 → `hidden_files/w47/scratch-proof-ja-fr1/render-print/p-4.png`
- `scratch-proof-ja-fr1/render-print/p-5.png` — 1057543B sha fddddf78acc6 → `hidden_files/w47/scratch-proof-ja-fr1/render-print/p-5.png`
- `scratch-proof-ja-fr1/render-print/p-6.png` — 662374B sha 606014724276 → `hidden_files/w47/scratch-proof-ja-fr1/render-print/p-6.png`
- `scratch-proof-ja-fr1/render-print/p-7.png` — 1857576B sha ceaeb3f92c91 → `hidden_files/w47/scratch-proof-ja-fr1/render-print/p-7.png`
- `scratch-proof-ja-fr1/render-print/p-8.png` — 1536026B sha 352f1190b1ec → `hidden_files/w47/scratch-proof-ja-fr1/render-print/p-8.png`
- `scratch-proof-ja-fr1/render-web/web-p1.png` — 1727357B sha 8d06bf17a188 → `hidden_files/w47/scratch-proof-ja-fr1/render-web/web-p1.png`
- `scratch-proof-ja-fr1/render-web/web-p8.png` — 1507804B sha a02d9d163319 → `hidden_files/w47/scratch-proof-ja-fr1/render-web/web-p8.png`
- `scratch-proof-ja-fr1/rerun/2026-w47-ja-fr.text.md` — 46880B sha 1512a491098a → `hidden_files/w47/scratch-proof-ja-fr1/rerun/2026-w47-ja-fr.text.md`
- `scratch-proof-ja-fr1/rerun/ABSTRACT.txt` — 330B sha 73aefc892b8c → `hidden_files/w47/scratch-proof-ja-fr1/rerun/ABSTRACT.txt`
- `scratch-proof-ja-fr1/rerun/Lucerna-VOL4-JA-FR-web.pdf` — 4458579B sha 99fd99aff8f1 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/Lucerna-VOL4-JA-FR-web.pdf`
- `scratch-proof-ja-fr1/rerun/Lucerna-VOL4-JA-FR.pdf` — 28347993B sha 5903a36b4766 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/Lucerna-VOL4-JA-FR.pdf`
- `scratch-proof-ja-fr1/rerun/WEEKLY-KIT.md` — 10560B sha ab696aae97f4 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/WEEKLY-KIT.md`
- `scratch-proof-ja-fr1/rerun/__pycache__/bslib4.cpython-312.pyc` — 18954B sha 9a2bacf29af5 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/__pycache__/bslib4.cpython-312.pyc`
- `scratch-proof-ja-fr1/rerun/__pycache__/svglib.cpython-312.pyc` — 39735B sha f0a38f3d9313 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/__pycache__/svglib.cpython-312.pyc`
- `scratch-proof-ja-fr1/rerun/assets/CREDITS.md` — 1712B sha 688f0e1d0e39 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/assets/CREDITS.md`
- `scratch-proof-ja-fr1/rerun/assets/arashiyama-pond.jpg` — 257367B sha a30f5fbc940b → `hidden_files/w47/scratch-proof-ja-fr1/rerun/assets/arashiyama-pond.jpg`
- `scratch-proof-ja-fr1/rerun/assets/arashiyama-temple.jpg` — 289997B sha 9c557d1752a0 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/assets/arashiyama-temple.jpg`
- `scratch-proof-ja-fr1/rerun/assets/beaujolais.jpg` — 154661B sha a16b99c636b2 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/assets/beaujolais.jpg`
- `scratch-proof-ja-fr1/rerun/assets/lucerna-moth.svg` — 1324B sha 42487693345a → `hidden_files/w47/scratch-proof-ja-fr1/rerun/assets/lucerna-moth.svg`
- `scratch-proof-ja-fr1/rerun/assets/maple.jpg` — 474411B sha 140f46d9e41b → `hidden_files/w47/scratch-proof-ja-fr1/rerun/assets/maple.jpg`
- `scratch-proof-ja-fr1/rerun/assets/tori.jpg` — 400576B sha 5a94b1e05d8f → `hidden_files/w47/scratch-proof-ja-fr1/rerun/assets/tori.jpg`
- `scratch-proof-ja-fr1/rerun/bslib4.py` — 10013B sha e2cc9b8f3482 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/bslib4.py`
- `scratch-proof-ja-fr1/rerun/cards/p1-hyoushi.png` — 1314636B sha ca8871a6f8e0 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/cards/p1-hyoushi.png`
- `scratch-proof-ja-fr1/rerun/cards/p2-kurashi.png` — 728967B sha 37875acf6fe5 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/cards/p2-kurashi.png`
- `scratch-proof-ja-fr1/rerun/cards/p3-bunka.png` — 952887B sha b869b7932553 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/cards/p3-bunka.png`
- `scratch-proof-ja-fr1/rerun/cards/p4-supotsu.png` — 894206B sha 3cca4c33f03e → `hidden_files/w47/scratch-proof-ja-fr1/rerun/cards/p4-supotsu.png`
- `scratch-proof-ja-fr1/rerun/cards/p5-wakamono.png` — 968734B sha afe354a6c629 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/cards/p5-wakamono.png`
- `scratch-proof-ja-fr1/rerun/cards/p6-fukayomi.png` — 770618B sha b33898d879f2 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/cards/p6-fukayomi.png`
- `scratch-proof-ja-fr1/rerun/cards/p7-kotoba.png` — 1492314B sha ae1a21938940 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/cards/p7-kotoba.png`
- `scratch-proof-ja-fr1/rerun/cards/p8-tesuto.png` — 1484087B sha dbd072c43415 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/cards/p8-tesuto.png`
- `scratch-proof-ja-fr1/rerun/content12.py` — 18492B sha 991599da4f50 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/content12.py`
- `scratch-proof-ja-fr1/rerun/content34.py` — 17339B sha e37f0c41cf4b → `hidden_files/w47/scratch-proof-ja-fr1/rerun/content34.py`
- `scratch-proof-ja-fr1/rerun/content56.py` — 16666B sha d049ff8e8ab1 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/content56.py`
- `scratch-proof-ja-fr1/rerun/content7.py` — 10859B sha 2bfcf8a0cc24 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/content7.py`
- `scratch-proof-ja-fr1/rerun/content8.py` — 10896B sha 65f2e985b525 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/content8.py`
- `scratch-proof-ja-fr1/rerun/render.py` — 1184B sha 213ab06bf176 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/render.py`
- `scratch-proof-ja-fr1/rerun/run.py` — 773B sha ca45aabf00da → `hidden_files/w47/scratch-proof-ja-fr1/rerun/run.py`
- `scratch-proof-ja-fr1/rerun/svg/p1-hyoushi.svg` — 658938B sha ee6170efbf23 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/svg/p1-hyoushi.svg`
- `scratch-proof-ja-fr1/rerun/svg/p2-kurashi.svg` — 25147B sha a09e586bb128 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/svg/p2-kurashi.svg`
- `scratch-proof-ja-fr1/rerun/svg/p3-bunka.svg` — 229970B sha 6cfcf3686c92 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/svg/p3-bunka.svg`
- `scratch-proof-ja-fr1/rerun/svg/p4-supotsu.svg` — 26979B sha 6deffcba8764 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/svg/p4-supotsu.svg`
- `scratch-proof-ja-fr1/rerun/svg/p5-wakamono.svg` — 368162B sha 6860640a3b7c → `hidden_files/w47/scratch-proof-ja-fr1/rerun/svg/p5-wakamono.svg`
- `scratch-proof-ja-fr1/rerun/svg/p6-fukayomi.svg` — 25766B sha b454eb0292d4 → `hidden_files/w47/scratch-proof-ja-fr1/rerun/svg/p6-fukayomi.svg`
- `scratch-proof-ja-fr1/rerun/svg/p7-kotoba.svg` — 561356B sha 2501facf07cf → `hidden_files/w47/scratch-proof-ja-fr1/rerun/svg/p7-kotoba.svg`
- `scratch-proof-ja-fr1/rerun/svg/p8-tesuto.svg` — 446861B sha fbe9bdb844be → `hidden_files/w47/scratch-proof-ja-fr1/rerun/svg/p8-tesuto.svg`
- `scratch-proof-ja-fr1/rerun/svglib.py` — 14700B sha b50f5ef9e12e → `hidden_files/w47/scratch-proof-ja-fr1/rerun/svglib.py`
- `scratch-proof-ja-it1/.probe` — 30B sha 6a109eb383e3 → `hidden_files/w47/scratch-proof-ja-it1/.probe`
- `scratch-proof-ja-it1/cjknet.py` — 1268B sha 767c9e47603e → `hidden_files/w47/scratch-proof-ja-it1/cjknet.py`
- `scratch-proof-ja-it1/freeze/build-copy/2026-w47-ja-it.text.md` — 46676B sha da4d8c94bdf3 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/2026-w47-ja-it.text.md`
- `scratch-proof-ja-it1/freeze/build-copy/ABSTRACT.txt` — 299B sha 829b4723fba6 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/ABSTRACT.txt`
- `scratch-proof-ja-it1/freeze/build-copy/Lucerna-VOL4-JA-IT-web.pdf` — 4476984B sha b3ea6d183dea → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/Lucerna-VOL4-JA-IT-web.pdf`
- `scratch-proof-ja-it1/freeze/build-copy/Lucerna-VOL4-JA-IT.pdf` — 29099162B sha 75986cd7e7b0 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/Lucerna-VOL4-JA-IT.pdf`
- `scratch-proof-ja-it1/freeze/build-copy/WEEKLY-KIT.md` — 10054B sha bc79568f3098 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/WEEKLY-KIT.md`
- `scratch-proof-ja-it1/freeze/build-copy/__pycache__/bslib4.cpython-312.pyc` — 18972B sha 76f5fa221dcf → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/__pycache__/bslib4.cpython-312.pyc`
- `scratch-proof-ja-it1/freeze/build-copy/__pycache__/svglib.cpython-312.pyc` — 39747B sha 3f9bf4584222 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/__pycache__/svglib.cpython-312.pyc`
- `scratch-proof-ja-it1/freeze/build-copy/assets/CREDITS.md` — 1712B sha 688f0e1d0e39 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/assets/CREDITS.md`
- `scratch-proof-ja-it1/freeze/build-copy/assets/arashiyama-pond.jpg` — 257367B sha a30f5fbc940b → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/assets/arashiyama-pond.jpg`
- `scratch-proof-ja-it1/freeze/build-copy/assets/arashiyama-temple.jpg` — 289997B sha 9c557d1752a0 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/assets/arashiyama-temple.jpg`
- `scratch-proof-ja-it1/freeze/build-copy/assets/beaujolais.jpg` — 154661B sha a16b99c636b2 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/assets/beaujolais.jpg`
- `scratch-proof-ja-it1/freeze/build-copy/assets/lucerna-moth.svg` — 1324B sha 42487693345a → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/assets/lucerna-moth.svg`
- `scratch-proof-ja-it1/freeze/build-copy/assets/maple.jpg` — 474411B sha 140f46d9e41b → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/assets/maple.jpg`
- `scratch-proof-ja-it1/freeze/build-copy/assets/tori.jpg` — 400576B sha 5a94b1e05d8f → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/assets/tori.jpg`
- `scratch-proof-ja-it1/freeze/build-copy/bslib4.py` — 10015B sha 0cc8a474cb10 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/bslib4.py`
- `scratch-proof-ja-it1/freeze/build-copy/cards/p1-hyoushi.png` — 1310042B sha 41081f56c281 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/cards/p1-hyoushi.png`
- `scratch-proof-ja-it1/freeze/build-copy/cards/p2-kurashi.png` — 729384B sha 309faf318e02 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/cards/p2-kurashi.png`
- `scratch-proof-ja-it1/freeze/build-copy/cards/p3-bunka.png` — 955015B sha 70ccf917cd69 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/cards/p3-bunka.png`
- `scratch-proof-ja-it1/freeze/build-copy/cards/p4-supotsu.png` — 894197B sha 6d51614bd681 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/cards/p4-supotsu.png`
- `scratch-proof-ja-it1/freeze/build-copy/cards/p5-wakamono.png` — 970803B sha 651c09faa709 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/cards/p5-wakamono.png`
- `scratch-proof-ja-it1/freeze/build-copy/cards/p6-fukayomi.png` — 770349B sha 7e7581d11414 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/cards/p6-fukayomi.png`
- `scratch-proof-ja-it1/freeze/build-copy/cards/p7-kotoba.png` — 1482196B sha e044731dcf0c → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/cards/p7-kotoba.png`
- `scratch-proof-ja-it1/freeze/build-copy/cards/p8-tesuto.png` — 1468432B sha 5538296467d1 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/cards/p8-tesuto.png`
- `scratch-proof-ja-it1/freeze/build-copy/content12.py` — 18561B sha ded4c6a337d2 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/content12.py`
- `scratch-proof-ja-it1/freeze/build-copy/content34.py` — 17366B sha 6d11c3d5c58e → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/content34.py`
- `scratch-proof-ja-it1/freeze/build-copy/content56.py` — 16511B sha ea7f4231cf8a → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/content56.py`
- `scratch-proof-ja-it1/freeze/build-copy/content7.py` — 10809B sha bfdf39c8e056 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/content7.py`
- `scratch-proof-ja-it1/freeze/build-copy/content8.py` — 10840B sha 93822ae6cc3b → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/content8.py`
- `scratch-proof-ja-it1/freeze/build-copy/render.py` — 1184B sha ef955067bb41 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/render.py`
- `scratch-proof-ja-it1/freeze/build-copy/run.py` — 773B sha ca45aabf00da → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/run.py`
- `scratch-proof-ja-it1/freeze/build-copy/svg/p1-hyoushi.svg` — 658943B sha 654e03c44ba0 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/svg/p1-hyoushi.svg`
- `scratch-proof-ja-it1/freeze/build-copy/svg/p2-kurashi.svg` — 25153B sha 4a29d9f14333 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/svg/p2-kurashi.svg`
- `scratch-proof-ja-it1/freeze/build-copy/svg/p3-bunka.svg` — 229964B sha 6bdb2aaee0c0 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/svg/p3-bunka.svg`
- `scratch-proof-ja-it1/freeze/build-copy/svg/p4-supotsu.svg` — 26968B sha d1d67c5c1346 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/svg/p4-supotsu.svg`
- `scratch-proof-ja-it1/freeze/build-copy/svg/p5-wakamono.svg` — 368130B sha 0ea9121eafb7 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/svg/p5-wakamono.svg`
- `scratch-proof-ja-it1/freeze/build-copy/svg/p6-fukayomi.svg` — 25729B sha 9f56540647b7 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/svg/p6-fukayomi.svg`
- `scratch-proof-ja-it1/freeze/build-copy/svg/p7-kotoba.svg` — 561153B sha aab133862fc2 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/svg/p7-kotoba.svg`
- `scratch-proof-ja-it1/freeze/build-copy/svg/p8-tesuto.svg` — 447071B sha 9509da3ed031 → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/svg/p8-tesuto.svg`
- `scratch-proof-ja-it1/freeze/build-copy/svglib.py` — 14700B sha b50f5ef9e12e → `hidden_files/w47/scratch-proof-ja-it1/freeze/build-copy/svglib.py`
- `scratch-proof-ja-it1/it-freediff.json` — 56858B sha a29803c83c3b → `hidden_files/w47/scratch-proof-ja-it1/it-freediff.json`
- `scratch-proof-ja-it1/it-freediff.log` — 908B sha 9486a8620fcd → `hidden_files/w47/scratch-proof-ja-it1/it-freediff.log`
- `scratch-proof-ja-it1/it-freeze.log` — 683B sha 30fbe8179aa1 → `hidden_files/w47/scratch-proof-ja-it1/it-freeze.log`
- `scratch-proof-ja-it1/it-occlusion.json` — 97B sha 0c527f034c3e → `hidden_files/w47/scratch-proof-ja-it1/it-occlusion.json`
- `scratch-proof-ja-it1/it-occlusion.log` — 193B sha 6b656eb3aa1f → `hidden_files/w47/scratch-proof-ja-it1/it-occlusion.log`
- `scratch-proof-ja-it1/it-p8.json` — 3786B sha 1d508b6df889 → `hidden_files/w47/scratch-proof-ja-it1/it-p8.json`
- `scratch-proof-ja-it1/it-p8compare.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-proof-ja-it1/it-p8compare.json`
- `scratch-proof-ja-it1/it-p8compare.log` — 229B sha f997aee252a9 → `hidden_files/w47/scratch-proof-ja-it1/it-p8compare.log`
- `scratch-proof-ja-it1/it-runpy.log` — 2124B sha 631a77a544d2 → `hidden_files/w47/scratch-proof-ja-it1/it-runpy.log`
- `scratch-proof-ja-it1/keydiff.py` — 1323B sha 3b26aba7dd81 → `hidden_files/w47/scratch-proof-ja-it1/keydiff.py`
- `scratch-proof-ja-it1/n58.py` — 413B sha e589c19bddfa → `hidden_files/w47/scratch-proof-ja-it1/n58.py`
- `scratch-proof-ja-it1/render/core-p-3.png` — 800941B sha 71bf7be93b43 → `hidden_files/w47/scratch-proof-ja-it1/render/core-p-3.png`
- `scratch-proof-ja-it1/render/core-p-4.png` — 719976B sha 18c97529c9f2 → `hidden_files/w47/scratch-proof-ja-it1/render/core-p-4.png`
- `scratch-proof-ja-it1/render/core-p-7.png` — 1284988B sha 647cee01f9a8 → `hidden_files/w47/scratch-proof-ja-it1/render/core-p-7.png`
- `scratch-proof-ja-it1/render/core-p-8.png` — 1267940B sha 0d79e3354878 → `hidden_files/w47/scratch-proof-ja-it1/render/core-p-8.png`
- `scratch-proof-ja-it1/render/core-p2-2.png` — 597814B sha 4d4a02d0991c → `hidden_files/w47/scratch-proof-ja-it1/render/core-p2-2.png`
- `scratch-proof-ja-it1/render/core-p5-5.png` — 810390B sha 99223ea2b9a1 → `hidden_files/w47/scratch-proof-ja-it1/render/core-p5-5.png`
- `scratch-proof-ja-it1/render/print-p-1.png` — 1123067B sha 23c2610ddbe9 → `hidden_files/w47/scratch-proof-ja-it1/render/print-p-1.png`
- `scratch-proof-ja-it1/render/print-p-2.png` — 599218B sha 8ea71b344490 → `hidden_files/w47/scratch-proof-ja-it1/render/print-p-2.png`
- `scratch-proof-ja-it1/render/print-p-3.png` — 808857B sha fdff2193e0bd → `hidden_files/w47/scratch-proof-ja-it1/render/print-p-3.png`
- `scratch-proof-ja-it1/render/print-p-4.png` — 725307B sha 0c46dd7471e9 → `hidden_files/w47/scratch-proof-ja-it1/render/print-p-4.png`
- `scratch-proof-ja-it1/render/print-p-5.png` — 821718B sha 492f0d33faa9 → `hidden_files/w47/scratch-proof-ja-it1/render/print-p-5.png`
- `scratch-proof-ja-it1/render/print-p-6.png` — 625104B sha 8d8aeaf7ca13 → `hidden_files/w47/scratch-proof-ja-it1/render/print-p-6.png`
- `scratch-proof-ja-it1/render/print-p-7.png` — 1248412B sha 90217bcde779 → `hidden_files/w47/scratch-proof-ja-it1/render/print-p-7.png`
- `scratch-proof-ja-it1/render/print-p-8.png` — 1368326B sha 334efc440e06 → `hidden_files/w47/scratch-proof-ja-it1/render/print-p-8.png`
- `scratch-proof-ja-it1/render/web-p1-1.png` — 1077042B sha 88fe7f91c8d2 → `hidden_files/w47/scratch-proof-ja-it1/render/web-p1-1.png`
- `scratch-proof-ja-it1/render/web-p8-8.png` — 1325940B sha 57ecbb8baf4d → `hidden_files/w47/scratch-proof-ja-it1/render/web-p8-8.png`
- `scratch-proof-ja-it1/rerun-sha.txt` — 646B sha 8441fdfb9784 → `hidden_files/w47/scratch-proof-ja-it1/rerun-sha.txt`
- `scratch-proof-ja-it1/rerun/__pycache__/bslib4.cpython-312.pyc` — 18960B sha fc3b1efd7cb1 → `hidden_files/w47/scratch-proof-ja-it1/rerun/__pycache__/bslib4.cpython-312.pyc`
- `scratch-proof-ja-it1/rerun/__pycache__/svglib.cpython-312.pyc` — 39735B sha 6f3495a8b149 → `hidden_files/w47/scratch-proof-ja-it1/rerun/__pycache__/svglib.cpython-312.pyc`
- `scratch-proof-ja-it1/rerun/assets/CREDITS.md` — 1712B sha 688f0e1d0e39 → `hidden_files/w47/scratch-proof-ja-it1/rerun/assets/CREDITS.md`
- `scratch-proof-ja-it1/rerun/assets/arashiyama-pond.jpg` — 257367B sha a30f5fbc940b → `hidden_files/w47/scratch-proof-ja-it1/rerun/assets/arashiyama-pond.jpg`
- `scratch-proof-ja-it1/rerun/assets/arashiyama-temple.jpg` — 289997B sha 9c557d1752a0 → `hidden_files/w47/scratch-proof-ja-it1/rerun/assets/arashiyama-temple.jpg`
- `scratch-proof-ja-it1/rerun/assets/beaujolais.jpg` — 154661B sha a16b99c636b2 → `hidden_files/w47/scratch-proof-ja-it1/rerun/assets/beaujolais.jpg`
- `scratch-proof-ja-it1/rerun/assets/lucerna-moth.svg` — 1324B sha 42487693345a → `hidden_files/w47/scratch-proof-ja-it1/rerun/assets/lucerna-moth.svg`
- `scratch-proof-ja-it1/rerun/assets/maple.jpg` — 474411B sha 140f46d9e41b → `hidden_files/w47/scratch-proof-ja-it1/rerun/assets/maple.jpg`
- `scratch-proof-ja-it1/rerun/assets/tori.jpg` — 400576B sha 5a94b1e05d8f → `hidden_files/w47/scratch-proof-ja-it1/rerun/assets/tori.jpg`
- `scratch-proof-ja-it1/rerun/bslib4.py` — 10015B sha 0cc8a474cb10 → `hidden_files/w47/scratch-proof-ja-it1/rerun/bslib4.py`
- `scratch-proof-ja-it1/rerun/content12.py` — 18561B sha ded4c6a337d2 → `hidden_files/w47/scratch-proof-ja-it1/rerun/content12.py`
- `scratch-proof-ja-it1/rerun/content34.py` — 17366B sha 6d11c3d5c58e → `hidden_files/w47/scratch-proof-ja-it1/rerun/content34.py`
- `scratch-proof-ja-it1/rerun/content56.py` — 16511B sha ea7f4231cf8a → `hidden_files/w47/scratch-proof-ja-it1/rerun/content56.py`
- `scratch-proof-ja-it1/rerun/content7.py` — 10809B sha bfdf39c8e056 → `hidden_files/w47/scratch-proof-ja-it1/rerun/content7.py`
- `scratch-proof-ja-it1/rerun/content8.py` — 10840B sha 93822ae6cc3b → `hidden_files/w47/scratch-proof-ja-it1/rerun/content8.py`
- `scratch-proof-ja-it1/rerun/render.py` — 1184B sha ef955067bb41 → `hidden_files/w47/scratch-proof-ja-it1/rerun/render.py`
- `scratch-proof-ja-it1/rerun/run.py` — 773B sha ca45aabf00da → `hidden_files/w47/scratch-proof-ja-it1/rerun/run.py`
- `scratch-proof-ja-it1/rerun/svg/p1-hyoushi.svg` — 658943B sha 654e03c44ba0 → `hidden_files/w47/scratch-proof-ja-it1/rerun/svg/p1-hyoushi.svg`
- `scratch-proof-ja-it1/rerun/svg/p2-kurashi.svg` — 25153B sha 4a29d9f14333 → `hidden_files/w47/scratch-proof-ja-it1/rerun/svg/p2-kurashi.svg`
- `scratch-proof-ja-it1/rerun/svg/p3-bunka.svg` — 229964B sha 6bdb2aaee0c0 → `hidden_files/w47/scratch-proof-ja-it1/rerun/svg/p3-bunka.svg`
- `scratch-proof-ja-it1/rerun/svg/p4-supotsu.svg` — 26968B sha d1d67c5c1346 → `hidden_files/w47/scratch-proof-ja-it1/rerun/svg/p4-supotsu.svg`
- `scratch-proof-ja-it1/rerun/svg/p5-wakamono.svg` — 368130B sha 0ea9121eafb7 → `hidden_files/w47/scratch-proof-ja-it1/rerun/svg/p5-wakamono.svg`
- `scratch-proof-ja-it1/rerun/svg/p6-fukayomi.svg` — 25729B sha 9f56540647b7 → `hidden_files/w47/scratch-proof-ja-it1/rerun/svg/p6-fukayomi.svg`
- `scratch-proof-ja-it1/rerun/svg/p7-kotoba.svg` — 561153B sha aab133862fc2 → `hidden_files/w47/scratch-proof-ja-it1/rerun/svg/p7-kotoba.svg`
- `scratch-proof-ja-it1/rerun/svg/p8-tesuto.svg` — 447071B sha 9509da3ed031 → `hidden_files/w47/scratch-proof-ja-it1/rerun/svg/p8-tesuto.svg`
- `scratch-proof-ja-it1/rerun/svglib.py` — 14700B sha b50f5ef9e12e → `hidden_files/w47/scratch-proof-ja-it1/rerun/svglib.py`
- `scratch-proof-ja-it1/shipped-sha.txt` — 1038B sha 77d712cd9616 → `hidden_files/w47/scratch-proof-ja-it1/shipped-sha.txt`
- `scratch-proof-ja-it1/show_diff.py` — 835B sha d5f9babff7cd → `hidden_files/w47/scratch-proof-ja-it1/show_diff.py`
- `scratch-proof-ja-it1/simp_scan.py` — 1089B sha 733a73e38b7c → `hidden_files/w47/scratch-proof-ja-it1/simp_scan.py`
- `scratch-proof-ja-it1/textnodes.py` — 1066B sha 18eb220929e9 → `hidden_files/w47/scratch-proof-ja-it1/textnodes.py`
- `scratch-proof-ja-pt1/.probe` — 21B sha a7697ca40633 → `hidden_files/w47/scratch-proof-ja-pt1/.probe`
- `scratch-proof-ja-pt1/gates/p2-words-crop.png` — 447189B sha 8010b98414bb → `hidden_files/w47/scratch-proof-ja-pt1/gates/p2-words-crop.png`
- `scratch-proof-ja-pt1/gates/print.txt` — 46976B sha 4de357532bfd → `hidden_files/w47/scratch-proof-ja-pt1/gates/print.txt`
- `scratch-proof-ja-pt1/gates/pt-occlusion.json` — 97B sha d2ff1a6e968d → `hidden_files/w47/scratch-proof-ja-pt1/gates/pt-occlusion.json`
- `scratch-proof-ja-pt1/gates/pt-occlusion.log` — 193B sha 81257e10e3f1 → `hidden_files/w47/scratch-proof-ja-pt1/gates/pt-occlusion.log`
- `scratch-proof-ja-pt1/gates/pt-p8.json` — 3778B sha 54849455ff54 → `hidden_files/w47/scratch-proof-ja-pt1/gates/pt-p8.json`
- `scratch-proof-ja-pt1/gates/pt-p8compare.json` — 2134B sha f4aed132676e → `hidden_files/w47/scratch-proof-ja-pt1/gates/pt-p8compare.json`
- `scratch-proof-ja-pt1/gates/rerun-run.log` — 2128B sha 3674bd488a50 → `hidden_files/w47/scratch-proof-ja-pt1/gates/rerun-run.log`
- `scratch-proof-ja-pt1/gates/s11-grep.txt` — 678B sha a1e67db7f014 → `hidden_files/w47/scratch-proof-ja-pt1/gates/s11-grep.txt`
- `scratch-proof-ja-pt1/gates/sha-rerun.txt` — 638B sha fb4a435b3841 → `hidden_files/w47/scratch-proof-ja-pt1/gates/sha-rerun.txt`
- `scratch-proof-ja-pt1/gates/sha-shipped.txt` — 118B sha d81dc4612d17 → `hidden_files/w47/scratch-proof-ja-pt1/gates/sha-shipped.txt`
- `scratch-proof-ja-pt1/gates/textdiff-core-pt.txt` — 32244B sha 91a2387a0c1f → `hidden_files/w47/scratch-proof-ja-pt1/gates/textdiff-core-pt.txt`
- `scratch-proof-ja-pt1/gates/u2019.txt` — 526B sha a51d328ff87f → `hidden_files/w47/scratch-proof-ja-pt1/gates/u2019.txt`
- `scratch-proof-ja-pt1/gates/web.txt` — 46976B sha 4de357532bfd → `hidden_files/w47/scratch-proof-ja-pt1/gates/web.txt`
- `scratch-proof-ja-pt1/render-print/p-1.png` — 1303875B sha 29de07249f7f → `hidden_files/w47/scratch-proof-ja-pt1/render-print/p-1.png`
- `scratch-proof-ja-pt1/render-print/p-2.png` — 682130B sha 82ee9351affe → `hidden_files/w47/scratch-proof-ja-pt1/render-print/p-2.png`
- `scratch-proof-ja-pt1/render-print/p-3.png` — 937481B sha a0f6e3078f78 → `hidden_files/w47/scratch-proof-ja-pt1/render-print/p-3.png`
- `scratch-proof-ja-pt1/render-print/p-4.png` — 828138B sha 12daf4163507 → `hidden_files/w47/scratch-proof-ja-pt1/render-print/p-4.png`
- `scratch-proof-ja-pt1/render-print/p-5.png` — 953958B sha 0d4a3a8f0b8a → `hidden_files/w47/scratch-proof-ja-pt1/render-print/p-5.png`
- `scratch-proof-ja-pt1/render-print/p-6.png` — 712249B sha 31987576e689 → `hidden_files/w47/scratch-proof-ja-pt1/render-print/p-6.png`
- `scratch-proof-ja-pt1/render-print/p-7.png` — 1445865B sha ff91f0115b80 → `hidden_files/w47/scratch-proof-ja-pt1/render-print/p-7.png`
- `scratch-proof-ja-pt1/render-print/p-8.png` — 1584609B sha 8d016ba37a1d → `hidden_files/w47/scratch-proof-ja-pt1/render-print/p-8.png`
- `scratch-proof-ja-pt1/render-web/wp1-1.png` — 1236863B sha dd999c250b1c → `hidden_files/w47/scratch-proof-ja-pt1/render-web/wp1-1.png`
- `scratch-proof-ja-pt1/render-web/wp8-8.png` — 1523543B sha b36c60912b56 → `hidden_files/w47/scratch-proof-ja-pt1/render-web/wp8-8.png`
- `scratch-proof-ja-pt1/rerun/2026-w47-ja-pt.text.md` — 46703B sha 426437e20aa3 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/2026-w47-ja-pt.text.md`
- `scratch-proof-ja-pt1/rerun/ABSTRACT.txt` — 307B sha 753e3bcc9992 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/ABSTRACT.txt`
- `scratch-proof-ja-pt1/rerun/Lucerna-VOL4-JA-PT-web.pdf` — 4485027B sha 499149398ebe → `hidden_files/w47/scratch-proof-ja-pt1/rerun/Lucerna-VOL4-JA-PT-web.pdf`
- `scratch-proof-ja-pt1/rerun/Lucerna-VOL4-JA-PT.pdf` — 29103006B sha 5e7542bc94e1 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/Lucerna-VOL4-JA-PT.pdf`
- `scratch-proof-ja-pt1/rerun/WEEKLY-KIT.md` — 10072B sha 09cb75f6f3cf → `hidden_files/w47/scratch-proof-ja-pt1/rerun/WEEKLY-KIT.md`
- `scratch-proof-ja-pt1/rerun/__pycache__/bslib4.cpython-312.pyc` — 18960B sha 0cce5993213a → `hidden_files/w47/scratch-proof-ja-pt1/rerun/__pycache__/bslib4.cpython-312.pyc`
- `scratch-proof-ja-pt1/rerun/__pycache__/svglib.cpython-312.pyc` — 39736B sha 55af2d7a718c → `hidden_files/w47/scratch-proof-ja-pt1/rerun/__pycache__/svglib.cpython-312.pyc`
- `scratch-proof-ja-pt1/rerun/assets/CREDITS.md` — 1712B sha 688f0e1d0e39 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/assets/CREDITS.md`
- `scratch-proof-ja-pt1/rerun/assets/arashiyama-pond.jpg` — 257367B sha a30f5fbc940b → `hidden_files/w47/scratch-proof-ja-pt1/rerun/assets/arashiyama-pond.jpg`
- `scratch-proof-ja-pt1/rerun/assets/arashiyama-temple.jpg` — 289997B sha 9c557d1752a0 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/assets/arashiyama-temple.jpg`
- `scratch-proof-ja-pt1/rerun/assets/beaujolais.jpg` — 154661B sha a16b99c636b2 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/assets/beaujolais.jpg`
- `scratch-proof-ja-pt1/rerun/assets/lucerna-moth.svg` — 1324B sha 42487693345a → `hidden_files/w47/scratch-proof-ja-pt1/rerun/assets/lucerna-moth.svg`
- `scratch-proof-ja-pt1/rerun/assets/maple.jpg` — 474411B sha 140f46d9e41b → `hidden_files/w47/scratch-proof-ja-pt1/rerun/assets/maple.jpg`
- `scratch-proof-ja-pt1/rerun/assets/tori.jpg` — 400576B sha 5a94b1e05d8f → `hidden_files/w47/scratch-proof-ja-pt1/rerun/assets/tori.jpg`
- `scratch-proof-ja-pt1/rerun/bslib4.py` — 10015B sha e1e301d61554 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/bslib4.py`
- `scratch-proof-ja-pt1/rerun/cards/p1-hyoushi.png` — 1315923B sha aa86ad4af48c → `hidden_files/w47/scratch-proof-ja-pt1/rerun/cards/p1-hyoushi.png`
- `scratch-proof-ja-pt1/rerun/cards/p2-kurashi.png` — 737813B sha d093204c1e71 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/cards/p2-kurashi.png`
- `scratch-proof-ja-pt1/rerun/cards/p3-bunka.png` — 960864B sha 67a48ea42768 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/cards/p3-bunka.png`
- `scratch-proof-ja-pt1/rerun/cards/p4-supotsu.png` — 900739B sha a51536e6b694 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/cards/p4-supotsu.png`
- `scratch-proof-ja-pt1/rerun/cards/p5-wakamono.png` — 976387B sha 3545413dcc60 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/cards/p5-wakamono.png`
- `scratch-proof-ja-pt1/rerun/cards/p6-fukayomi.png` — 777258B sha 9004b30bcbac → `hidden_files/w47/scratch-proof-ja-pt1/rerun/cards/p6-fukayomi.png`
- `scratch-proof-ja-pt1/rerun/cards/p7-kotoba.png` — 1495332B sha 8508e1a4f727 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/cards/p7-kotoba.png`
- `scratch-proof-ja-pt1/rerun/cards/p8-tesuto.png` — 1461034B sha 710daee634e4 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/cards/p8-tesuto.png`
- `scratch-proof-ja-pt1/rerun/content12.py` — 18516B sha d49808f0634f → `hidden_files/w47/scratch-proof-ja-pt1/rerun/content12.py`
- `scratch-proof-ja-pt1/rerun/content34.py` — 17435B sha 28c2269f0939 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/content34.py`
- `scratch-proof-ja-pt1/rerun/content56.py` — 16526B sha ef5a25343714 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/content56.py`
- `scratch-proof-ja-pt1/rerun/content7.py` — 10790B sha 2332ca6cb5bc → `hidden_files/w47/scratch-proof-ja-pt1/rerun/content7.py`
- `scratch-proof-ja-pt1/rerun/content8.py` — 10803B sha c174898b4ef6 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/content8.py`
- `scratch-proof-ja-pt1/rerun/render.py` — 1184B sha d3cc2bcb2d9e → `hidden_files/w47/scratch-proof-ja-pt1/rerun/render.py`
- `scratch-proof-ja-pt1/rerun/run.py` — 773B sha ca45aabf00da → `hidden_files/w47/scratch-proof-ja-pt1/rerun/run.py`
- `scratch-proof-ja-pt1/rerun/svg/p1-hyoushi.svg` — 658931B sha 2acbca1c2d1f → `hidden_files/w47/scratch-proof-ja-pt1/rerun/svg/p1-hyoushi.svg`
- `scratch-proof-ja-pt1/rerun/svg/p2-kurashi.svg` — 25391B sha fd550234056e → `hidden_files/w47/scratch-proof-ja-pt1/rerun/svg/p2-kurashi.svg`
- `scratch-proof-ja-pt1/rerun/svg/p3-bunka.svg` — 230098B sha e493bb6d9e48 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/svg/p3-bunka.svg`
- `scratch-proof-ja-pt1/rerun/svg/p4-supotsu.svg` — 27014B sha 49af928533b9 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/svg/p4-supotsu.svg`
- `scratch-proof-ja-pt1/rerun/svg/p5-wakamono.svg` — 368030B sha e0b9f4dfe346 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/svg/p5-wakamono.svg`
- `scratch-proof-ja-pt1/rerun/svg/p6-fukayomi.svg` — 25768B sha 0533c2c08673 → `hidden_files/w47/scratch-proof-ja-pt1/rerun/svg/p6-fukayomi.svg`
- `scratch-proof-ja-pt1/rerun/svg/p7-kotoba.svg` — 561290B sha feabca16ca0c → `hidden_files/w47/scratch-proof-ja-pt1/rerun/svg/p7-kotoba.svg`
- `scratch-proof-ja-pt1/rerun/svg/p8-tesuto.svg` — 446331B sha 33c021039cba → `hidden_files/w47/scratch-proof-ja-pt1/rerun/svg/p8-tesuto.svg`
- `scratch-proof-ja-pt1/rerun/svglib.py` — 14700B sha b50f5ef9e12e → `hidden_files/w47/scratch-proof-ja-pt1/rerun/svglib.py`
- `scratch-webpdf-nl-ru-ja/detail-ja.tsv` — 2330B sha 22923b28aa48 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/detail-ja.tsv`
- `scratch-webpdf-nl-ru-ja/detail-nl.tsv` — 1856B sha 9d6712ebfec3 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/detail-nl.tsv`
- `scratch-webpdf-nl-ru-ja/detail-ru.tsv` — 3419B sha 5d42ca25f7c9 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/detail-ru.tsv`
- `scratch-webpdf-nl-ru-ja/detail-smoke.tsv` — 162B sha b3a03df72752 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/detail-smoke.tsv`
- `scratch-webpdf-nl-ru-ja/ja-de.print.txt` — 105192B sha 3507946ae4fd → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-de.print.txt`
- `scratch-webpdf-nl-ru-ja/ja-de.web.txt` — 105192B sha 3507946ae4fd → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-de.web.txt`
- `scratch-webpdf-nl-ru-ja/ja-en.print.txt` — 99988B sha fbe611d189ea → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-en.print.txt`
- `scratch-webpdf-nl-ru-ja/ja-en.web.txt` — 99988B sha fbe611d189ea → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-en.web.txt`
- `scratch-webpdf-nl-ru-ja/ja-es.print.txt` — 102065B sha 7d04e84c711e → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-es.print.txt`
- `scratch-webpdf-nl-ru-ja/ja-es.web.txt` — 102065B sha 7d04e84c711e → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-es.web.txt`
- `scratch-webpdf-nl-ru-ja/ja-fr.print.txt` — 104269B sha 274102b9de5b → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-fr.print.txt`
- `scratch-webpdf-nl-ru-ja/ja-fr.web.txt` — 104269B sha 274102b9de5b → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-fr.web.txt`
- `scratch-webpdf-nl-ru-ja/ja-it.print.txt` — 106304B sha 2e8b39fb13df → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-it.print.txt`
- `scratch-webpdf-nl-ru-ja/ja-it.web.txt` — 106304B sha 2e8b39fb13df → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-it.web.txt`
- `scratch-webpdf-nl-ru-ja/ja-ko.print.txt` — 91550B sha eb0bccfc5e93 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-ko.print.txt`
- `scratch-webpdf-nl-ru-ja/ja-ko.web.txt` — 91550B sha eb0bccfc5e93 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-ko.web.txt`
- `scratch-webpdf-nl-ru-ja/ja-nl-adjudication.md` — 902B sha 18d40489a782 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-nl-adjudication.md`
- `scratch-webpdf-nl-ru-ja/ja-nl.print.txt` — 101713B sha ca9aa877c7b8 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-nl.print.txt`
- `scratch-webpdf-nl-ru-ja/ja-nl.web.txt` — 101713B sha 8cd1a1804152 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-nl.web.txt`
- `scratch-webpdf-nl-ru-ja/ja-pt.print.txt` — 104739B sha 6e767639a7fa → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-pt.print.txt`
- `scratch-webpdf-nl-ru-ja/ja-pt.web.txt` — 104739B sha 6e767639a7fa → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-pt.web.txt`
- `scratch-webpdf-nl-ru-ja/ja-ru.print.txt` — 106357B sha 10bd80a7226e → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-ru.print.txt`
- `scratch-webpdf-nl-ru-ja/ja-ru.web.txt` — 106357B sha 10bd80a7226e → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-ru.web.txt`
- `scratch-webpdf-nl-ru-ja/ja-zh-cn.print.txt` — 85061B sha beacb6d68614 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-zh-cn.print.txt`
- `scratch-webpdf-nl-ru-ja/ja-zh-cn.web.txt` — 85061B sha beacb6d68614 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-zh-cn.web.txt`
- `scratch-webpdf-nl-ru-ja/ja-zh-tw.print.txt` — 82086B sha 4dd83cd8159c → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-zh-tw.print.txt`
- `scratch-webpdf-nl-ru-ja/ja-zh-tw.web.txt` — 82086B sha 4dd83cd8159c → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ja-zh-tw.web.txt`
- `scratch-webpdf-nl-ru-ja/list-ja-zhcn.tsv` — 135B sha f14c88aa38e6 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/list-ja-zhcn.tsv`
- `scratch-webpdf-nl-ru-ja/list-ja.tsv` — 1803B sha b04caa37411f → `hidden_files/w47/scratch-webpdf-nl-ru-ja/list-ja.tsv`
- `scratch-webpdf-nl-ru-ja/list-nl.tsv` — 1869B sha 4a09706bce8d → `hidden_files/w47/scratch-webpdf-nl-ru-ja/list-nl.tsv`
- `scratch-webpdf-nl-ru-ja/list-ru-rest.tsv` — 1638B sha a89db4031a83 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/list-ru-rest.tsv`
- `scratch-webpdf-nl-ru-ja/list-ru.tsv` — 1803B sha b75a63802e80 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/list-ru.tsv`
- `scratch-webpdf-nl-ru-ja/list-smoke.tsv` — 165B sha 2c3a9fd95b38 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/list-smoke.tsv`
- `scratch-webpdf-nl-ru-ja/nl-de.print.txt` — 106161B sha d51d7d31a9e3 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-de.print.txt`
- `scratch-webpdf-nl-ru-ja/nl-de.web.txt` — 106161B sha d51d7d31a9e3 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-de.web.txt`
- `scratch-webpdf-nl-ru-ja/nl-en.print.txt` — 107149B sha 203e74f49137 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-en.print.txt`
- `scratch-webpdf-nl-ru-ja/nl-en.web.txt` — 107149B sha 203e74f49137 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-en.web.txt`
- `scratch-webpdf-nl-ru-ja/nl-es.print.txt` — 106408B sha 327a061c5e67 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-es.print.txt`
- `scratch-webpdf-nl-ru-ja/nl-es.web.txt` — 106408B sha 327a061c5e67 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-es.web.txt`
- `scratch-webpdf-nl-ru-ja/nl-fr.print.txt` — 108312B sha b08661599a50 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-fr.print.txt`
- `scratch-webpdf-nl-ru-ja/nl-fr.web.txt` — 108312B sha b08661599a50 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-fr.web.txt`
- `scratch-webpdf-nl-ru-ja/nl-it.print.txt` — 106945B sha ee52037df5bc → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-it.print.txt`
- `scratch-webpdf-nl-ru-ja/nl-it.web.txt` — 106945B sha ee52037df5bc → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-it.web.txt`
- `scratch-webpdf-nl-ru-ja/nl-ja.print.txt` — 106333B sha b0c7fa53dfda → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-ja.print.txt`
- `scratch-webpdf-nl-ru-ja/nl-ja.web.txt` — 106333B sha b0c7fa53dfda → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-ja.web.txt`
- `scratch-webpdf-nl-ru-ja/nl-ko.print.txt` — 107752B sha e55ba44e17ce → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-ko.print.txt`
- `scratch-webpdf-nl-ru-ja/nl-ko.web.txt` — 107752B sha e55ba44e17ce → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-ko.web.txt`
- `scratch-webpdf-nl-ru-ja/nl-pt.print.txt` — 104925B sha 61295b10aefc → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-pt.print.txt`
- `scratch-webpdf-nl-ru-ja/nl-pt.web.txt` — 104925B sha 61295b10aefc → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-pt.web.txt`
- `scratch-webpdf-nl-ru-ja/nl-ru.print.txt` — 114210B sha e02e4fb78c70 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-ru.print.txt`
- `scratch-webpdf-nl-ru-ja/nl-ru.web.txt` — 114210B sha e02e4fb78c70 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-ru.web.txt`
- `scratch-webpdf-nl-ru-ja/nl-zh-cn.print.txt` — 102307B sha f5e171563b17 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-zh-cn.print.txt`
- `scratch-webpdf-nl-ru-ja/nl-zh-cn.web.txt` — 102307B sha f5e171563b17 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-zh-cn.web.txt`
- `scratch-webpdf-nl-ru-ja/nl-zh-tw.print.txt` — 102287B sha dfa916b0390d → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-zh-tw.print.txt`
- `scratch-webpdf-nl-ru-ja/nl-zh-tw.web.txt` — 102287B sha dfa916b0390d → `hidden_files/w47/scratch-webpdf-nl-ru-ja/nl-zh-tw.web.txt`
- `scratch-webpdf-nl-ru-ja/rebuild-ja-de.log` — 1326B sha 9da4a77af86a → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ja-de.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ja-en.log` — 1087B sha 63106ad2485b → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ja-en.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ja-es.log` — 1089B sha ec07d2b2cb46 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ja-es.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ja-fr.log` — 1089B sha 4bfac5360777 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ja-fr.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ja-it.log` — 1089B sha af663aa8ee5f → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ja-it.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ja-ko.log` — 1484B sha 1551ee7b9426 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ja-ko.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ja-nl.log` — 1429B sha c60376fa55f8 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ja-nl.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ja-pt.log` — 1089B sha 9eff5c70843f → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ja-pt.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ja-ru.log` — 1685B sha 533b687bdd55 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ja-ru.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ja-zh-cn.log` — 1040B sha 128771f0b4d1 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ja-zh-cn.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ja-zh-tw.log` — 1790B sha 20168394b24d → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ja-zh-tw.log`
- `scratch-webpdf-nl-ru-ja/rebuild-nl-de.log` — 1395B sha 54d166542cc5 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-nl-de.log`
- `scratch-webpdf-nl-ru-ja/rebuild-nl-en.log` — 1395B sha b55368268292 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-nl-en.log`
- `scratch-webpdf-nl-ru-ja/rebuild-nl-es.log` — 1513B sha 924b0e18e5d9 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-nl-es.log`
- `scratch-webpdf-nl-ru-ja/rebuild-nl-fr.log` — 1630B sha 7c6bd9e40317 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-nl-fr.log`
- `scratch-webpdf-nl-ru-ja/rebuild-nl-it.log` — 1395B sha f55594b3e4b2 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-nl-it.log`
- `scratch-webpdf-nl-ru-ja/rebuild-nl-ja.log` — 1400B sha 836df2d0091f → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-nl-ja.log`
- `scratch-webpdf-nl-ru-ja/rebuild-nl-ko.log` — 1398B sha 1153beef8dcf → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-nl-ko.log`
- `scratch-webpdf-nl-ru-ja/rebuild-nl-pt.log` — 1396B sha d23179069dcd → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-nl-pt.log`
- `scratch-webpdf-nl-ru-ja/rebuild-nl-ru.log` — 1513B sha 3c693fe235b9 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-nl-ru.log`
- `scratch-webpdf-nl-ru-ja/rebuild-nl-zh-cn.log` — 1550B sha a4eeb9a676b9 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-nl-zh-cn.log`
- `scratch-webpdf-nl-ru-ja/rebuild-nl-zh-tw.log` — 1430B sha 5d80360d4373 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-nl-zh-tw.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ru-de.log` — 1768B sha f6d71b0d052e → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ru-de.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ru-en.log` — 1768B sha fee7acb2546b → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ru-en.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ru-es.log` — 1768B sha 83e7c2dcc96c → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ru-es.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ru-fr.log` — 1768B sha ea1aaf4a27f6 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ru-fr.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ru-it.log` — 1768B sha 321f84efa1ca → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ru-it.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ru-ja.log` — 1772B sha 44e7b04e1a77 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ru-ja.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ru-ko.log` — 1887B sha 155c18d9a2b8 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ru-ko.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ru-nl.log` — 2617B sha b3a2a795fe58 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ru-nl.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ru-pt.log` — 1768B sha d5beb601e883 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ru-pt.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ru-zh-cn.log` — 1803B sha 6720a2d39abd → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ru-zh-cn.log`
- `scratch-webpdf-nl-ru-ja/rebuild-ru-zh-tw.log` — 1802B sha 6379cab88597 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild-ru-zh-tw.log`
- `scratch-webpdf-nl-ru-ja/rebuild.sh` — 2980B sha 6ef33a85696a → `hidden_files/w47/scratch-webpdf-nl-ru-ja/rebuild.sh`
- `scratch-webpdf-nl-ru-ja/ru-de.print.txt` — 111665B sha 7187e8e7712a → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-de.print.txt`
- `scratch-webpdf-nl-ru-ja/ru-de.web.txt` — 111665B sha 7187e8e7712a → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-de.web.txt`
- `scratch-webpdf-nl-ru-ja/ru-en.print.txt` — 111532B sha bd1ed4c70ee3 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-en.print.txt`
- `scratch-webpdf-nl-ru-ja/ru-en.web.txt` — 111532B sha bd1ed4c70ee3 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-en.web.txt`
- `scratch-webpdf-nl-ru-ja/ru-es.print.txt` — 112478B sha 6cab5bd8c0e4 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-es.print.txt`
- `scratch-webpdf-nl-ru-ja/ru-es.web.txt` — 112478B sha 6cab5bd8c0e4 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-es.web.txt`
- `scratch-webpdf-nl-ru-ja/ru-fr.print.txt` — 112709B sha 0764376786bb → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-fr.print.txt`
- `scratch-webpdf-nl-ru-ja/ru-fr.web.txt` — 112709B sha 0764376786bb → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-fr.web.txt`
- `scratch-webpdf-nl-ru-ja/ru-it.print.txt` — 112932B sha 9edc061d5305 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-it.print.txt`
- `scratch-webpdf-nl-ru-ja/ru-it.web.txt` — 112932B sha 9edc061d5305 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-it.web.txt`
- `scratch-webpdf-nl-ru-ja/ru-ja.print.txt` — 107061B sha 2c15e3d1abed → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-ja.print.txt`
- `scratch-webpdf-nl-ru-ja/ru-ja.web.txt` — 107061B sha 2c15e3d1abed → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-ja.web.txt`
- `scratch-webpdf-nl-ru-ja/ru-ko.print.txt` — 108917B sha 9484446ddac9 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-ko.print.txt`
- `scratch-webpdf-nl-ru-ja/ru-ko.web.txt` — 108917B sha 9484446ddac9 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-ko.web.txt`
- `scratch-webpdf-nl-ru-ja/ru-nl.print.txt` — 110989B sha c83daa07452f → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-nl.print.txt`
- `scratch-webpdf-nl-ru-ja/ru-nl.web.txt` — 110989B sha c83daa07452f → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-nl.web.txt`
- `scratch-webpdf-nl-ru-ja/ru-pt.print.txt` — 111033B sha 4be84b6ab54c → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-pt.print.txt`
- `scratch-webpdf-nl-ru-ja/ru-pt.web.txt` — 111033B sha 4be84b6ab54c → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-pt.web.txt`
- `scratch-webpdf-nl-ru-ja/ru-zh-cn.print.txt` — 105307B sha 27384658f8d9 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-zh-cn.print.txt`
- `scratch-webpdf-nl-ru-ja/ru-zh-cn.web.txt` — 105307B sha 27384658f8d9 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-zh-cn.web.txt`
- `scratch-webpdf-nl-ru-ja/ru-zh-tw.print.txt` — 104490B sha a8fe3260b477 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-zh-tw.print.txt`
- `scratch-webpdf-nl-ru-ja/ru-zh-tw.web.txt` — 104490B sha a8fe3260b477 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/ru-zh-tw.web.txt`
- `scratch-webpdf-nl-ru-ja/run-ja-zhcn.out` — 1075B sha 3bd0d365c265 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/run-ja-zhcn.out`
- `scratch-webpdf-nl-ru-ja/run-ja.out` — 13464B sha 1f1ea52578a8 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/run-ja.out`
- `scratch-webpdf-nl-ru-ja/run-nl.done` — 8B sha 5c91bc5fb3c4 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/run-nl.done`
- `scratch-webpdf-nl-ru-ja/run-nl.out` — 16050B sha 14b3991c5d26 → `hidden_files/w47/scratch-webpdf-nl-ru-ja/run-nl.out`
- `scratch-webpdf-nl-ru-ja/run-ru-rest.out` — 18756B sha 950a84c05add → `hidden_files/w47/scratch-webpdf-nl-ru-ja/run-ru-rest.out`
- `scratch-webpdf-nl-ru-ja/verify_flag.py` — 2582B sha 84b064a9ab2c → `hidden_files/w47/scratch-webpdf-nl-ru-ja/verify_flag.py`

### 2.4 任务 2 验核

- 654/654 移入目的地已验存在（`moved` + `moved_repo_suffix` 全数）。
- 仓内 `hidden_files/w47/` 移空后：文件数 0，空目录已 `rmdir`（`hidden_files/w47/` 与 `hidden_files/` 均已删）；`git status --porcelain -- hidden_files/` 返回 0 行，`git status --porcelain | grep hidden_files` 返回 0 行。
- 未动 W43/W45/W46、未动 covers/tools/issues、正典版目录只读。

## 3. 磁盘与剩余工作

- 开工 93G（96,880,528 KB 已用）；完工 93G（96,885,980 KB 已用，期间并发工人又写 ~5 MB）。本次实际释放：任务 2 删除 94,967 B；`mv` 不释放空间。
- 还剩未清：`production/2026-w47/fanout-nl/` 301 MB（154 项 git 状态），待协调员按 §1.5 授权后删除。清掉后 insert.py 全树 clean 检查方可通过该两项。
- 比较脚本与原始 JSON：`/tmp/hygiene_compare.py`、`/tmp/hygiene_fanout_compare.json`、`/tmp/hygiene_hidden_compare.json`、`/tmp/hygiene_hidden_log.json`（/tmp 为临时证据，不随仓保存）。


## §1.5 协调员核实 + 授权删除（2026-11-12 ~12:35 UTC）
- 协调员独立复核（diff -rq 全 10 版 + mtime + _D5_READER 计数）：text.md 差异 9 版（de/en/fr/it/ja/ko/pt/ru/zh-tw），es 相同；每处差异均为正典更新、fanout 为旧版——第 140 题答案 `een gedicht` → `een kort gedicht`（fix1 已落地修正）+ nl-en 2 处间距修正；其余文件差异（PDF/KIT/svglib/content/svg/cards）与 D5 重建一致；正典 svglib 11/11 含 _D5_READER（含 core-nl），fanout 仅 7/10；mtime fanout 11-11 12:25–14:03 vs 正典 17:23–20:54；diff -rq 无 "Only in fanout-nl"（fanout 零唯一文件）；正典独有 1 个 nl-ru/svglib.py.orig（D5 备份，无害）。
- 注：工人报"8 处差异"与协调员实测 9 处差 1——工人计数口径为 9 个已追踪 M 中的 8 个（另 1 个差异 text.md 为未追踪）；方向结论一致，不影响删除决定。
- 授权执行：`rm -rf production/2026-w47/fanout-nl`（301M，442 文件）已删；git status 残留 9 条 fanout-nl 的 " D"（已追踪 .text.md 的删除标记，由后续生产源 commit 处理，预期内）。
