# GATE-LOG — W47 zh-tw-ru fix1（機制層驗證）

- **時間**：2026-11-11 ~09:30–09:37 UTC
- **探針**：開工、編輯前、驗證寫盤前、寫日誌前各重探一次，`git hash-object -w` 均 rc=0；全程無 EDQUOT；df：/home/hatch 77G 可用。/tmp 未用。
- **改動文件**：僅 `scratch-fanout-zh-tw/tables.py`（238 → 242 條；8 處 ru 單行改動 + 4 條新插條目）。

## 1. tables.py 本體驗證

- `python3 -c "import tables"`：成功，`ENTRIES = 242`，`LANGS = ['de','fr','es','it','pt','nl','ru','ja','ko']`；缺語條目 0 條（新條目 9 語齊全）。
- 與修前備份 `tables.py.bak-pre-fix1` 的 diff 計 77 行：8 行 `c` 改動（:252、:274、:329、:373、:1431、:1541、:1728、:2070）+ 44 行新插（4 條目），無其他差異。
- 舊串全表歸零：`Выучите их раз —` / `следующее воскресенье` / `следующего воскресенья` / `шар-Пикачу` / `Рождество в Диснее` / `Накапливать баллы — это 集點。` 計 0 行。
- 新串計數：`Выучите их один раз` ×1；`назначен на это воскресенье` ×2（:252、:329）；`В это воскресенье, 22 нояб.` ×1（:274）；`гигантский надувной Пикачу` ×1 + `Гигантский надувной Пикачу` ×1；`Рождество в Диснейленде — 17` ×1 + `Рождество в Диснейленде начинается` ×2（[165] 修正 + [194] 原已有）；`Накапливать баллы — это 集點.` ×1；N2 新值各 ×1（`Сяосюэ — 22 ноября.` ×1 表內——其餘同句在版內出現 3 次，見 §2）。
- 源鍵與其餘 8 語既有值未動（見備份 diff）。

## 2. Scratch transform（9 語全跑）

- 方法（沿用 it fix1）：筆記目錄 `work/` 內複製盤上 core-zh-tw（33M，已帶 core fix1 D1 + fix2 N3）＋ 改後 tables.py ＋ transform.py（僅 PROD 指針改向 scratch `work/prod`，其餘原樣），逐語重跑。
- 結果：**9/9 TRANSFORM OK**，各 248 行日誌：`transform-de.log` / `transform-es.log` / `transform-fr.log` / `transform-it.log` / `transform-nl.log` / `transform-pt.log` / `transform-ru.log` / `transform-ja.log` / `transform-ko.log`（均留存本目錄，另有 `transform-<lang>.stdout.log`）。
- 新條目替換次數（9 語一致）：`The ceremony is at the Taipei Music Center.` 1×；`Xiaoxue is Nov 22.` 3×；`Four big events fall on the same Sunday.` 1×；`Collecting points is 集點.` 1×。長源 `Xiaoxue is Nov 22, the same day.` 另行替換 1×，無衝突。
- 驗證用副本（core 拷貝 33M ＋ 9 版產出約 300M）已刪，僅留日誌與 diff 檔（`diff-ru.txt`、`diff-other8.txt`）。

## 3. ru：新值流入驗證

scratch-ru（`work/prod/2026-w47-zh-tw-ru/`，已刪，見日誌與 diff）：
- D1-俄語：`content12.py:37`（`назначен на это воскресенье`）、`content12.py:113`（`В это воскресенье, 22 нояб., — Сяосюэ`）、`content34.py:127`（`назначен на это воскресенье`）✓
- N1：`content7.py:18` — `Выучите их один раз — и любой парад станет понятен.` ✓
- N2（6 處）：`content56.py:177`（Церемония）、`:190`（Сяосюэ）、`:194`（Четыре больших события）；`content8.py:26`（Сяосюэ）、`:62`（Накапливать баллы — это 集點.，修正版）、`:70`（Сяосюэ）✓
- N6：`content56.py:28`（P5 注）、`:55`（key 75）— `надувной Пикачу` ✓
- N7：`content56.py:34`（key 65）、`content8.py:22`（key 115）— `Рождество в Диснейленде` ✓（`content7.py:128` 的同串為 [194] 原已有值）
- 舊串在 scratch-ru 全部 content 文件中 0 命中；`Xiaoxue is Nov 22, the same day.` 目標句 `content56.py:171` 保持 `Сяосюэ — 22 нояб., в тот же день.`（長源優先無污染）。

## 4. ru diff 分類（scratch-ru vs 已發版，`diff-ru.txt`，16 hunks，44 行改動）

| Hunk | 位置 | 分類 |
|---|---|---|
| content12.py @@ -30 | P1 標題+正文（D1中文×2）+ 首條注（D1俄語×1） | D1（平行帶入中文 fix1 + 本輪俄語） |
| content12.py @@ -65 | P1 本週大事行（D1中文×1） | D1中文（平行帶入）；`小雪` 仍在——N4 未修，待裁定 |
| content12.py @@ -108 | P2 小雪首句（D1中文×1）+ 注（D1俄語×1） | D1（平行 + 本輪） |
| content34.py @@ -14 | P3 標題+正文（D1中文×2） | D1中文（平行帶入） |
| content34.py @@ -120 | P4 標題+正文（D1中文×2）+ 注（D1俄語×1） | D1（平行 + 本輪） |
| content34.py @@ -193 | P4 圖注（D1中文×1） | D1中文（平行帶入） |
| content56.py @@ -25 | P5 注 N6 [31] + key 65 N7 [138] | 本輪 |
| content56.py @@ -52 | key 75 N6 [148] | 本輪 |
| content56.py @@ -93 | HK box `p.rect 480→418` | N3（core fix2 平行帶入） |
| content56.py @@ -102 | 刪 BABYMONSTER 行 + `by4 = by3 + 436` | N3（core fix2 平行帶入） |
| content56.py @@ -129 | `怎麼辦？先選一件，再看轉播——四件事只能取捨。` | 核心側平行改動（fan-out 後盤上核心新增，非本輪；見 FIX-LOG） |
| content7.py @@ -15 | N1（content7.py:18） | 本輪 |
| content7.py @@ -96 | 讀者園地引文（D1中文×1） | D1中文（平行帶入） |
| content8.py @@ -19 | key 115 N7 [165] | 本輪 |
| content8.py @@ -59 | key 134 N5（`。`→`.`） | 本輪（隨 N2 入表） |
| content8.py @@ -83 | E144 題幹（D1中文×1） | D1中文（平行帶入） |

合計：D1 ×8 hunks（中文 11 處 + 俄語 3 處）+ N1 ×1 + N5 ×1 + N6/N7 ×3 hunks + N3 ×2 + 核心側 ×1 = 16。N2 其餘 5 處與已發版手寫譯文逐字一致，故無 hunk——正是回填正確的證據。`bslib4.py` / `render.py` / `ABSTRACT.txt`：diff 為空。

## 5. 其餘 8 語：零波及驗證

每語 scratch vs 已發版 diff（`diff-other8.txt`，94 hunks，± 行各 120 行，**逐條清點、零未分類**）：

| 語 | hunks | 分類 |
|---|---|---|
| de | 12 | D1中文 ×8 hunks + N3 ×2 + `四件事只能取捨` ×1 + P7 預告條 118↔104 ×1（fan-out 手工修正，見 §6） |
| fr | 12 | D1中文 ×8 + N3 ×2 + `四件事` ×1 + Astuce mémoire ×1（fr-fix1 平行帶入） |
| es | 11 | D1中文 ×8 + N3 ×2 + `四件事` ×1 |
| it | 15 | D1中文 ×8 + N3 ×2 + `四件事` ×1 + D3 ×5 hunks（it-fix1 平行帶入；content34 的 2 處「混合」標記僅為未改動上下文行，刪行清點中 content34 無 D3 刪行） |
| pt / nl / ja / ko | 11/語 | D1中文 ×8 + N3 ×2 + `四件事` ×1 |

- **刪行清點**：120 條刪行 = D1 相關 11 行/語 ×8 + N3 3 行/語 ×8 + `四件事` 1 行/語 ×8 + de 預告條 2 行 + it D3 5 行 + fr Astuce 1 行；**增行 120 條一一對應**。除上述三類前存/平行差異外無任何其他差異。
- **N2 零出現**：8 語 diff 中 6 處 P8 注位置**無任何 hunk**——回填值與各版已發手寫譯文逐字一致（程式核對 36/36 亦證），本輪改動未波及其他語的任何既有值。
- `bslib4.py` / `render.py` / `ABSTRACT.txt`：9 語 diff 全空。

## 6. 重擴注意（非本輪所致）

1. **de P7 預告條會回落**：已發 de 版的 P7 預告條是 fan-out 時手工 118→104px（`p.rect(MX, py, RIGHT - MX, 104…)`、`print("P7 teaser ends", py + 104)`），盤上核心仍為 118；重擴後 scratch-de 為 118。重建輪次須重驗 de 的 P7 幾何（it-fix1 GATE-LOG §5 已記一筆）。
2. **核心側 `四件事只能取捨`**：9 版 diff 人人有份，核心 `content56.py:131` 現句為 `怎麼辦？先選一件，再看轉播——四件事只能取捨。遊行…`；核心目錄未入 git（`git ls-files` 0 條），無提交記錄可查出處。重擴時隨核心帶入 9 版，請協調員核查其歸屬（本輪未動核心）。

## 7. 未做

- 未改核心、未改本版成品、未重建、未跑 insert.py / lint --write、無 git 寫操作（僅探針 `git hash-object -w`）。
- N4 未修（待裁定）。N3、D1中文未碰版文件。P7 欄高與 occlusion 終驗留待重建輪次（見 FIX-LOG）。
