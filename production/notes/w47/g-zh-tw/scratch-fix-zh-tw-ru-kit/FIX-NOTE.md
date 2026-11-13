# FIX-NOTE — W47 zh-tw-ru KIT 一行订正

- 时间：2026-11-11 12:39–12:40 EST
- 文件（唯一改动）：`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-ru/WEEKLY-KIT.md` 第 35 行
- 未 commit、未 push、未重渲染；未碰其他任何文件。

## 探针（开工前，全部通过）
- `ls /dev/null` 存在（`-rw-rw----`，非字符设备但 git 可用，未垫回）
- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc 0
- scratch 目录真实写文件成功：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-tw-ru-kit/`（.probe 已删）

## 改动前后对照（第 35 行尾部片段）
- 改前：`… not missing content. Web PDF 1,993,092 bytes; web text layer 58,581 bytes (Cyrillic UTF-8 is 2 bytes per letter, hence larger than Latin editions' ~48k).`
- 改后：`… not missing content. Web PDF 2,007,900 bytes; web text layer 58,581 bytes (Cyrillic UTF-8 is 2 bytes per letter, hence larger than Latin editions' ~48k).`
- 仅 `1,993,092` → `2,007,900` 一处替换；第 35 行其余内容逐字未动。

## 第 79 行（不动，已核实）
- `… tools/webpdf.py exit 0; 1,993,092 bytes (< 7 MB); …` —— 旧轮次历史记录，保留原样。

## SHA 重验（改前 = 改后，逐字一致）
- 印 `Lucerna-VOL4-RU.pdf` 12,896,218 B — `1dbe1d8ec96fe91eeccb8b2a2f92080dd83c1302d85aed555e2e4e255224eeee`
- 网 `Lucerna-VOL4-RU-web.pdf` 2,007,900 B — `cb05eba2e641e3a200fff8d58648092788f08fca70f1d0ab8736ac76cfb50d52`
- 文 `2026-w47-zh-tw-ru.text.md` 62,492 B — `2fb4b97ef37d490e834dbef5c9553fb476c209222f061f7a17c4274e882ae03b`
- （三件成品位于 `production/2026-w47/2026-w47-zh-tw-ru/`，因 `issues/2026-w47/` 尚不存在——该版尚未 insert 入仓。）

## grep 核对（改后）
- `1,993,092` 全文只剩第 79 行一处
- `2,007,900` 在第 35 行出现 2 处（前半句 `web … 2,007,900 bytes` + 行尾 `Web PDF 2,007,900 bytes`）
